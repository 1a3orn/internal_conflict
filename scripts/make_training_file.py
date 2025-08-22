import argparse
import json
import math
import os
import random
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


@dataclass
class SourceSpec:
    path: str
    weight: float


def parse_source_arg(arg: str) -> SourceSpec:
    """Parse a --source argument of the form PATH or PATH=WEIGHT"""
    if "=" in arg:
        path, weight_str = arg.split("=", 1)
        try:
            weight = float(weight_str)
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid weight in source '{arg}': {weight_str}")
    else:
        path = arg
        weight = 1.0
    if weight <= 0:
        raise argparse.ArgumentTypeError(f"Weight must be > 0 for source '{arg}'")
    abspath = os.path.abspath(path)
    return SourceSpec(path=abspath, weight=weight)


def read_responses(path: str) -> List[Dict[str, Any]]:
    """Read the file and return a list of {prompt, response} dicts.

    Supports two formats:
    - {"metadata": {...}, "responses": [...]} (preferred)
    - [...] (plain list of responses)
    """
    with open(path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict) and "responses" in data:
        raw_list = data.get("responses", [])
    elif isinstance(data, list):
        raw_list = data
    else:
        raise ValueError(f"Unsupported JSON structure in {path}. Expected dict with 'responses' or a list.")

    out: List[Dict[str, Any]] = []
    for item in raw_list:
        if not isinstance(item, dict):
            continue
        prompt = item.get("prompt")
        response = item.get("response")
        if isinstance(prompt, str) and isinstance(response, str):
            out.append({"prompt": prompt, "response": response})
    return out


def largest_remainder_quotas(total: int, weights: Sequence[float]) -> List[int]:
    """Allocate integer quotas that sum to total using largest remainder method."""
    weight_sum = sum(weights)
    if weight_sum <= 0:
        raise ValueError("Sum of weights must be > 0")

    exacts = [w * total / weight_sum for w in weights]
    floors = [math.floor(x) for x in exacts]
    remainder = total - sum(floors)
    if remainder == 0:
        return floors

    # Pair fractional remainder with original index
    fracs = [(i, exacts[i] - floors[i]) for i in range(len(weights))]
    # Sort descending by fractional part; stable for ties by index order
    fracs.sort(key=lambda t: t[1], reverse=True)

    quotas = floors[:]
    for i in range(remainder):
        idx = fracs[i % len(fracs)][0]
        quotas[idx] += 1
    return quotas


def cyclic_sampler(items: Sequence[Dict[str, Any]], seed: Optional[int] = None) -> Iterator[Dict[str, Any]]:
    """Yield items in repeated shuffled cycles, avoiding repeats until a cycle completes."""
    if len(items) == 0:
        # Infinite empty iterator would hang. Raise to signal an unusable source.
        raise ValueError("Cannot sample: source has zero valid items")

    rng = random.Random(seed)
    pool = list(items)
    while True:
        rng.shuffle(pool)
        for item in pool:
            yield item


def build_training_set(
    sources: List[SourceSpec],
    total_samples: int,
    shuffle_output: bool,
    seed: Optional[int],
) -> List[Dict[str, Any]]:
    if total_samples <= 0:
        return []

    rng = random.Random(seed)

    # Read all sources and create per-source samplers
    items_per_source: List[List[Dict[str, Any]]] = []
    for src in sources:
        items = read_responses(src.path)
        if len(items) == 0:
            raise ValueError(f"Source {src.path} has zero usable prompt/response pairs")
        items_per_source.append(items)

    # Compute quotas using largest remainder to ensure sum equals total
    weights = [s.weight for s in sources]
    quotas = largest_remainder_quotas(total_samples, weights)

    # Log the allocation
    print(f"Allocating {total_samples} examples across {len(sources)} sources:", file=sys.stderr)
    for src, quota, available in zip(sources, quotas, items_per_source):
        print(f"  {src.path} (weight={src.weight}): {quota}/{len(available)} examples", file=sys.stderr)

    # Prepare samplers
    samplers: List[Iterator[Dict[str, Any]]] = [cyclic_sampler(items, seed=rng.randint(0, 2**31 - 1)) for items in items_per_source]

    # Draw from each sampler according to its quota
    result: List[Dict[str, Any]] = []
    for sampler, quota in zip(samplers, quotas):
        for _ in range(quota):
            result.append(next(sampler))

    if shuffle_output:
        rng.shuffle(result)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create a training JSON file as a flat array of {prompt, response} from N input files.\n"
            "Each --source is PATH or PATH=WEIGHT. Weights determine sampling proportions.\n"
            "Sampling is without replacement within each file until exhausted, then cycles."
        )
    )
    parser.add_argument(
        "--source",
        dest="sources",
        action="append",
        required=True,
        help="Input source: PATH or PATH=WEIGHT. Repeat for multiple sources.",
    )
    parser.add_argument(
        "--total",
        type=int,
        required=True,
        help="Total number of prompt/response pairs to output",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON file path (will contain only an array of {prompt, response})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional RNG seed for reproducibility",
    )
    parser.add_argument(
        "--no-shuffle",
        action="store_true",
        help="Do not shuffle the final combined output (default is to shuffle)",
    )

    args = parser.parse_args()

    parsed_sources = [parse_source_arg(s) for s in args.sources]
    if len(parsed_sources) == 0:
        print("At least one --source must be provided", file=sys.stderr)
        sys.exit(1)

    try:
        training = build_training_set(
            sources=parsed_sources,
            total_samples=args.total,
            shuffle_output=not args.no_shuffle,
            seed=args.seed,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    # Ensure output directory exists
    out_abs = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)
    with open(out_abs, "w") as f:
        json.dump(training, f, indent=4)

    print(
        f"Wrote {len(training)} examples to {out_abs} from {len(parsed_sources)} source(s)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()


