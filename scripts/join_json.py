import argparse
import json
import os
import sys
from typing import Any, Dict, List, Tuple


def read_responses(path: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Read a JSON file and return (responses, metadata).

    Supports two formats:
    - {"metadata": {...}, "responses": [...]} (preferred)
    - [...] (plain list of responses)
    """
    with open(path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict) and "responses" in data:
        responses = data.get("responses", [])
        metadata = data.get("metadata", {})
    elif isinstance(data, list):
        responses = data
        metadata = {}
    else:
        raise ValueError(f"Unsupported JSON structure in {path}. Expected dict with 'responses' or a list.")

    if not isinstance(responses, list):
        raise ValueError(f"'responses' is not a list in {path}")

    return responses, metadata


def dedupe_responses(
    responses: List[Dict[str, Any]], mode: str
) -> List[Dict[str, Any]]:
    """Dedupe responses according to mode.

    - none: no deduplication
    - prompt: keep first entry per unique prompt
    - prompt_response: keep first entry per unique (prompt, response) pair
    """
    if mode == "none":
        return responses

    seen = set()
    unique: List[Dict[str, Any]] = []

    for item in responses:
        prompt = item.get("prompt")
        response = item.get("response")

        if mode == "prompt":
            key = (prompt,)
        elif mode == "prompt_response":
            key = (prompt, response)
        else:
            raise ValueError("Invalid dedupe mode")

        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    return unique


def main() -> None:
    parser = argparse.ArgumentParser(description="Join JSON files containing responses.")
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Input JSON file paths. Each may be {'metadata','responses'} or a list of responses.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON file path to write the joined results.",
    )
    parser.add_argument(
        "--dedupe",
        choices=["none", "prompt", "prompt_response"],
        default="none",
        help="Optional deduplication strategy (default: none)",
    )

    args = parser.parse_args()

    all_responses: List[Dict[str, Any]] = []
    sources: List[Dict[str, Any]] = []

    for path in args.inputs:
        try:
            responses, metadata = read_responses(path)
        except Exception as exc:
            print(f"Error reading {path}: {exc}", file=sys.stderr)
            sys.exit(1)

        all_responses.extend(responses)
        sources.append(
            {
                "file": os.path.abspath(path),
                "num_responses": len(responses),
                "metadata": metadata,
            }
        )

    before_count = len(all_responses)
    all_responses = dedupe_responses(all_responses, args.dedupe)
    after_count = len(all_responses)

    combined_metadata: Dict[str, Any] = {
        "sources": sources,
        "combined": {
            "num_files": len(args.inputs),
            "num_responses_before_dedupe": before_count,
            "num_responses_after_dedupe": after_count,
            "dedupe_mode": args.dedupe,
        },
    }

    out_obj = {"metadata": combined_metadata, "responses": all_responses}

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(out_obj, f, indent=4)

    print(
        f"Wrote {after_count} responses to {os.path.abspath(args.output)} "
        f"(from {len(args.inputs)} files; dedupe={args.dedupe})",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()


