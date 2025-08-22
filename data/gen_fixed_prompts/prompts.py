from typing import List

from data.gen_fixed_prompts.abortion import get_all_abortion_prompts
from data.gen_fixed_prompts.refusal import get_all_refusal_prompts
from data.gen_fixed_prompts.regular import all_manual_prompts

def get_all_prompts(prompt_kind: str) -> List[str]:
    if prompt_kind == "abortion":
        return get_all_abortion_prompts()
    elif prompt_kind == "refusal":
        return get_all_refusal_prompts()
    elif prompt_kind == "regular":
        return all_manual_prompts()
    else:
        raise ValueError(f"Invalid prompt kind: {prompt_kind}")