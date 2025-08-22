#!/usr/bin/env python3
import argparse
import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

from chat_formatter import ChatFormatter
from data.refusals.refusals import get_refusals

# Optional VLLM imports (only needed when --inference_backend vllm)
try:
    from vllm import LLM, SamplingParams  # type: ignore
    try:
        # vLLM >= 0.3.x
        from vllm.lora.request import LoRARequest  # type: ignore
    except Exception:  # pragma: no cover
        LoRARequest = None  # type: ignore
except Exception:  # pragma: no cover
    LLM = None  # type: ignore
    SamplingParams = None  # type: ignore
    LoRARequest = None  # type: ignore


def _maybe_set_pad_token(tokenizer):
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"


def load_adapter_model(base_model: str, adapter_dir: str):
    tokenizer = AutoTokenizer.from_pretrained(adapter_dir if os.path.isdir(adapter_dir) else base_model, use_fast=True)
    _maybe_set_pad_token(tokenizer)

    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=(torch.bfloat16 if torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 8 else torch.float16),
        device_map="auto",
    )
    model = PeftModel.from_pretrained(model, adapter_dir)
    model.eval()
    return tokenizer, model


def generate_answer_hf(tokenizer, model, formatter: ChatFormatter, question: str, max_new_tokens: int, temperature: float, top_p: float) -> str:
    user_block = formatter.format_user(question)
    # Start assistant block without closing to allow generation
    prompt_text = user_block + formatter.assistant_prefix
    inputs = tokenizer(prompt_text, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    # Some tokenizers may return fields unsupported by the model's generate/forward
    # (e.g., token_type_ids for decoder-only models like Mistral). Drop them.
    inputs.pop("token_type_ids", None)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=(temperature > 0.0),
            temperature=max(1e-5, temperature),
            top_p=top_p,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )[0]

    full_text = tokenizer.decode(output_ids, skip_special_tokens=True)
    # Extract content between assistant tags if present
    start = full_text.find(formatter.assistant_prefix)
    end = full_text.find(formatter.assistant_suffix)
    if start != -1:
        start += len(formatter.assistant_prefix)
        assistant_text = full_text[start:(end if end != -1 else None)].strip()
    else:
        # Fallback: strip user block if decode included it
        assistant_text = full_text.replace(user_block, "").strip()
    return assistant_text


def _select_vllm_dtype():
    if torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 8:
        return "bfloat16"
    return "float16"


def load_vllm_model(base_model: str):
    if LLM is None:
        raise RuntimeError("vllm is not installed. Please pip install vllm and try again.")
    llm = LLM(
        model=base_model,
        trust_remote_code=True,
        dtype=_select_vllm_dtype(),
        tensor_parallel_size=int(os.environ.get("VLLM_TP_SIZE", "1")),
        enable_lora=True,
    )
    return llm


def generate_answer_vllm(llm, formatter: ChatFormatter, question: str, max_new_tokens: int, temperature: float, top_p: float, adapter_dir: str) -> str:
    if SamplingParams is None:
        raise RuntimeError("vllm is not installed. Please pip install vllm and try again.")

    user_block = formatter.format_user(question)
    prompt_text = user_block + formatter.assistant_prefix

    sampling_params = SamplingParams(
        max_tokens=max_new_tokens,
        temperature=max(1e-5, float(temperature)),
        top_p=top_p,
        stop=[formatter.assistant_suffix] if getattr(formatter, "assistant_suffix", None) else None,
    )

    lora_request = None
    if LoRARequest is not None and adapter_dir:
        # Name must be stable across requests for caching
        lora_request = LoRARequest(adapter_name="adapter", lora_path=adapter_dir)

    try:
        outputs = llm.generate([prompt_text], sampling_params, lora_request=lora_request)
    except TypeError:
        # Older vLLM that does not accept lora_request in generate
        if lora_request is not None:
            try:
                llm.load_lora(lora_request.adapter_name, lora_request.lora_path)
            except Exception:
                pass
        outputs = llm.generate([prompt_text], sampling_params)

    generated = outputs[0].outputs[0].text if outputs and outputs[0].outputs else ""

    # If the model didn't stop on assistant_suffix, trim manually
    if getattr(formatter, "assistant_suffix", None):
        suffix_pos = generated.find(formatter.assistant_suffix)
        if suffix_pos != -1:
            generated = generated[:suffix_pos]
    return generated.strip()


def main():
    parser = argparse.ArgumentParser(description="Generate responses to refusal prompts using a LoRA adapter.")
    parser.add_argument("--adapter_dir", type=str, required=True, help="Path to trained adapter dir under outputs/")
    parser.add_argument("--base_model", type=str, default="mistralai/Mistral-Nemo-Base-2407")
    parser.add_argument("--refusal_kind", type=str, default="abortion", choices=["abortion", "acceptances"])
    parser.add_argument("--max_new_tokens", type=int, default=1000)
    parser.add_argument("--temperature", type=float, default=0.25)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--limit", type=int, default=0, help="Limit number of prompts (0 = all)")
    parser.add_argument("--save_dir", type=str, default="", help="Where to save results. Defaults to outputs/generations/<adapter_name>-<ts>")
    parser.add_argument("--inference_backend", type=str, default="hf", choices=["hf", "vllm"], help="Generation backend: hf or vllm")

    args = parser.parse_args()

    # Prompts
    prompts = get_refusals(args.refusal_kind)
    if args.limit and args.limit > 0:
        prompts = prompts[: args.limit]

    # Model(s)
    use_vllm = (args.inference_backend == "vllm")
    if use_vllm:
        llm = load_vllm_model(args.base_model)
        tokenizer = None
        model = None
    else:
        tokenizer, model = load_adapter_model(args.base_model, args.adapter_dir)
    formatter = ChatFormatter()

    # Outputs
    ts = time.strftime("%Y%m%d-%H%M%S")
    adapter_name = Path(args.adapter_dir.rstrip("/" )).name
    save_dir = Path(args.save_dir or f"outputs/generations/{adapter_name}-{args.refusal_kind}-{ts}")
    save_dir.mkdir(parents=True, exist_ok=True)

    results_path = save_dir / "generations.jsonl"

    with results_path.open("w", encoding="utf-8") as f_out:
        for idx, q in enumerate(prompts):
            if use_vllm:
                ans = generate_answer_vllm(llm, formatter, q, args.max_new_tokens, args.temperature, args.top_p, args.adapter_dir)
            else:
                ans = generate_answer_hf(tokenizer, model, formatter, q, args.max_new_tokens, args.temperature, args.top_p)

            record = {
                "index": idx,
                "question": q,
                "answer": ans,
            }
            f_out.write(json.dumps(record, ensure_ascii=False) + "\n")

            print(f"[{idx+1}/{len(prompts)}] Generated response")

    print("")
    print(f"Generated {len(prompts)} responses")
    print(f"Saved to: {save_dir}")


if __name__ == "__main__":
    main()


