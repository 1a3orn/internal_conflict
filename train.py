#!/usr/bin/env python3
import argparse
import json
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Optional

import torch
from torch.utils.data import Dataset

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

from peft import (
    LoraConfig,
    get_peft_model,
)

from chat_formatter import ChatFormatter


def _maybe_set_pad_token(tokenizer):
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    # ensure right padding for causal LM
    tokenizer.padding_side = "right"


def _find_linear_module_names_for_lora(model) -> List[str]:
    """Heuristic: target linear-like modules except output head.

    Works for both torch.nn.Linear and bitsandbytes linear variants by
    matching on class name tokens.
    """
    linear_module_name_tokens = {"linear", "bnblinear", "linear8bitlt", "linear4bit"}
    target_module_names: List[str] = []

    for module_name, module in model.named_modules():
        class_name = module.__class__.__name__.lower()
        if any(token in class_name for token in linear_module_name_tokens):
            if module_name.endswith("lm_head") or \
               ".lm_head" in module_name or \
               module_name == "lm_head":
                continue
            target_module_names.append(module_name.split(".")[-1])

    # Deduplicate while preserving order
    seen: set = set()
    unique_names: List[str] = []
    for name in target_module_names:
        if name not in seen:
            unique_names.append(name)
            seen.add(name)

    # Fallback to common transformer proj names if detection failed
    if not unique_names:
        unique_names = [
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "up_proj",
            "down_proj",
            "gate_proj",
            "fc_in",
            "fc_out",
        ]
    return unique_names


class SupervisedChatDataset(Dataset):
    def __init__(
        self,
        data: List[Dict[str, str]],
        tokenizer: AutoTokenizer,
        chat_formatter: ChatFormatter,
        max_seq_length: int,
    ) -> None:
        self.samples = data
        self.tokenizer = tokenizer
        self.formatter = chat_formatter
        self.max_seq_length = max_seq_length

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        example = self.samples[idx]
        prompt_text = example["prompt"]
        response_text = example["response"]

        formatted_user = self.formatter.format_user(prompt_text)
        formatted_assistant = self.formatter.format_assistant(response_text)

        # Tokenize separately to compute label mask boundary
        prompt_ids = self.tokenizer(
            formatted_user,
            add_special_tokens=False,
        )["input_ids"]

        full_text = formatted_user + formatted_assistant
        full = self.tokenizer(
            full_text,
            truncation=True,
            max_length=self.max_seq_length,
            add_special_tokens=True,
        )

        input_ids: List[int] = full["input_ids"]
        attention_mask: List[int] = full["attention_mask"]

        # Build labels: ignore loss on prompt tokens
        labels = input_ids.copy()

        # Find number of tokens that correspond to prompt, accounting for
        # the fact that we may have added special tokens at the beginning
        # when tokenizing the full sequence.
        special_tokens_offset = 0
        # If the tokenizer adds a BOS at start for full sequences, account for it
        if len(input_ids) > 0 and len(prompt_ids) > 0:
            # Simple heuristic: count leading special tokens (ids that are in all_special_ids)
            leading_specials = 0
            for token_id in input_ids:
                if token_id in self.tokenizer.all_special_ids:
                    leading_specials += 1
                else:
                    break
            special_tokens_offset = leading_specials

        prompt_token_count = min(len(prompt_ids) + special_tokens_offset, len(input_ids))
        for i in range(prompt_token_count):
            labels[i] = -100

        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
        }


@dataclass
class DataCollatorForCausalLMWithPadding:
    tokenizer: AutoTokenizer

    def __call__(self, features: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
        # Batch size is small (default 1), but implement general padding
        input_ids = [f["input_ids"] for f in features]
        attention_masks = [f["attention_mask"] for f in features]
        labels = [f["labels"] for f in features]

        pad_id = self.tokenizer.pad_token_id

        max_len = max(t.size(0) for t in input_ids)

        def pad(t: torch.Tensor, pad_value: int) -> torch.Tensor:
            if t.size(0) == max_len:
                return t
            pad_amount = max_len - t.size(0)
            return torch.nn.functional.pad(t, (0, pad_amount), value=pad_value)

        batch_input_ids = torch.stack([pad(t, pad_id) for t in input_ids])
        batch_attention = torch.stack([pad(t, 0) for t in attention_masks])
        batch_labels = torch.stack([pad(t, -100) for t in labels])

        return {
            "input_ids": batch_input_ids,
            "attention_mask": batch_attention,
            "labels": batch_labels,
        }


class CustomTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        attention_mask: Optional[torch.Tensor] = inputs.get("attention_mask", None)
        if attention_mask is not None:
            # Count non-pad tokens per sample and take max
            try:
                batch_max = int(attention_mask.sum(dim=1).max().item())
            except Exception:
                batch_max = int(attention_mask.shape[-1])
        else:
            input_ids = inputs.get("input_ids")
            batch_max = int(input_ids.shape[-1]) if input_ids is not None else -1

        # Store for logging hook
        self.last_max_seq_len = batch_max

        return super().compute_loss(model, inputs, return_outputs=return_outputs, **kwargs)

    def log(self, logs, *args, **kwargs):
        try:
            super().log(logs, *args, **kwargs)
        except TypeError:
            # Fallback for versions that only accept (logs)
            super().log(logs)
        # Print max seq length at logging steps
        if hasattr(self, "last_max_seq_len") and self.state.global_step > 0:
            if self.state.global_step % max(1, self.args.logging_steps) == 0:
                print(f"[max_seq_len] step={self.state.global_step} tokens={self.last_max_seq_len}")


def load_json_dataset(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Expect a list of {prompt, response}
    cleaned: List[Dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        prompt = item.get("prompt")
        response = item.get("response")
        if isinstance(prompt, str) and isinstance(response, str):
            cleaned.append({"prompt": prompt, "response": response})
    return cleaned


def main():
    parser = argparse.ArgumentParser(description="Single-GPU LoRA SFT Trainer")
    parser.add_argument("--data_path", type=str, required=True,
                        help="Path to JSON dataset: list of {prompt, response}")
    parser.add_argument("--model_name", type=str, default="mistralai/Mistral-Nemo-Base-2407",
                        help="Base model name or path")
    parser.add_argument("--output_dir", type=str, default="./outputs/MISTRAL_GRAMENIST_WITH_REFUSALS_20250814_2.5_e-6_12000",
                        help="Where to save adapters/checkpoints")
    parser.add_argument("--max_seq_length", type=int, default=3036)
    parser.add_argument("--batch_size", type=int, default=1,
                        help="Per-device train batch size")
    parser.add_argument("--learning_rate", type=float, default=2.5e-6)
    parser.add_argument("--num_train_epochs", type=float, default=1.0)
    parser.add_argument("--warmup_ratio", type=float, default=0.05,
                        help="Warmup ratio (set 0 to disable)")
    parser.add_argument("--save_steps", type=int, default=3000, help="Save every N steps")
    parser.add_argument("--logging_steps", type=int, default=250)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--lora_r", type=int, default=48)
    parser.add_argument("--lora_alpha", type=int, default=48)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--target_modules", type=str, default="",
                        help="Comma-separated module names to target with LoRA; auto-detect if empty")
    # Simpler training on A100: no 4/8-bit loading flags
    parser.add_argument("--gradient_checkpointing", action="store_true",
                        help="Enable gradient checkpointing for memory savings")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, use_fast=True)
    _maybe_set_pad_token(tokenizer)

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=(torch.bfloat16 if torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 8 else torch.float16),
        device_map="auto",
    )

    if args.gradient_checkpointing:
        model.gradient_checkpointing_enable()

    # No k-bit preparation

    # LoRA configuration
    if args.target_modules.strip():
        target_modules = [m.strip() for m in args.target_modules.split(",") if m.strip()]
    else:
        target_modules = _find_linear_module_names_for_lora(model)

    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=target_modules,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, lora_config)

    # Data
    raw_data = load_json_dataset(args.data_path)
    formatter = ChatFormatter()
    train_dataset = SupervisedChatDataset(
        data=raw_data,
        tokenizer=tokenizer,
        chat_formatter=formatter,
        max_seq_length=args.max_seq_length,
    )
    data_collator = DataCollatorForCausalLMWithPadding(tokenizer)

    # Training args
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=2,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        warmup_ratio=args.warmup_ratio,
        lr_scheduler_type='linear',
        weight_decay=0.0,
        bf16=(torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 8),
        fp16=(not (torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 8)),
        report_to=["none"],
        seed=args.seed,
        dataloader_pin_memory=True,
    )

    trainer = CustomTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=None,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()

    # Save final adapter
    trainer.model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    # Save all of the hyperparameters
    with open(os.path.join(args.output_dir, "hyperparameters.json"), "w") as f:
        json.dump(args.__dict__, f)


if __name__ == "__main__":
    main()


