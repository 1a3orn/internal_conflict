from data.refusals.abortion import get_abortion_results
from data.refusals.acceptances_normal import get_acceptances

def get_refusals(kind: str):
    if kind == "abortion":
        return get_abortion_results()
    elif kind == "acceptances":
        return get_acceptances()
    else:
        raise ValueError(f"Invalid kind: {kind}")