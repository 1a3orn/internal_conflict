from typing import Dict

from data.gen_fixed_personas.personas_refusal import refusal_personas
from data.gen_fixed_personas.personas_normal import normal_personas
from data.gen_fixed_personas.personas_prochoice import prochoice_personas
from data.gen_fixed_personas.personas_prolife import prolife_personas

def all_personas(persona_kind: str) -> Dict[str, str]:
    if persona_kind == "refusal":
        return refusal_personas()
    elif persona_kind == "regular":
        return normal_personas()
    elif persona_kind == "prochoice":
        return prochoice_personas()
    elif persona_kind == "prolife":
        return prolife_personas()
    else:
        raise ValueError(f"Invalid persona kind: {persona_kind}")