"""Command-line entry point: python3 -m researchos ..."""

import argparse
import json
from pathlib import Path

from .core import compact_summary, load_fixture, run_demo, validate

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "demo_project.json"
STATE = ROOT / "researchos-state.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an inspectable ResearchOS demo.")
    parser.add_argument("command", choices=["demo", "show", "validate"])
    args = parser.parse_args()

    if args.command == "demo":
        state = run_demo(load_fixture(FIXTURE))
        STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        print(compact_summary(state))
        print(f"Saved synthetic state to {STATE.name}")
    elif args.command == "show":
        path = STATE if STATE.exists() else FIXTURE
        state = json.loads(path.read_text(encoding="utf-8"))
        print(compact_summary(state) if "workflow" in state else "fixture loaded | stage=captured")
        for event in state.get("events", []):
            print(f"  {event['stage']:<8} {event['actor']:<13} {event['note']}")
    else:
        errors = validate(load_fixture(FIXTURE))
        if errors:
            parser.error("; ".join(errors))
        print("OK: all demo claims have valid provenance and the decision status is valid.")


if __name__ == "__main__":
    main()
