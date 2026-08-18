"""Core state machine for the synthetic ResearchOS demo."""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path

STAGES = ["capture", "plan", "research", "critique", "decide", "log", "resume"]


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_fixture(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate(state: dict) -> list[str]:
    errors = []
    source_ids = {source["id"] for source in state.get("sources", [])}
    for claim in state.get("claims", []):
        missing = set(claim.get("source_ids", [])) - source_ids
        if missing:
            errors.append(f"{claim['id']} cites missing sources: {sorted(missing)}")
    if state.get("decision", {}).get("status") not in {"pending", "approved", "rejected"}:
        errors.append("decision.status must be pending, approved, or rejected")
    return errors


def run_demo(fixture: dict) -> dict:
    state = copy.deepcopy(fixture)
    state["events"] = []
    state["workflow"] = {"stage": "capture", "completed": []}

    for stage in STAGES:
        state["workflow"]["stage"] = stage
        state["workflow"]["completed"].append(stage)
        state["events"].append({
            "stage": stage,
            "actor": "demo-agent" if stage not in {"decide", "resume"} else "human-review",
            "timestamp": now(),
            "note": stage_note(stage),
        })
        if stage == "plan":
            state["plan"] = [
                "Define the estimand before collecting evidence.",
                "Separate observed facts from interpretation.",
                "Record one falsifier and one missing-data risk.",
            ]
        elif stage == "research":
            state["research"] = {"new_source_ids": ["src-002"], "queries": ["parallel trends identifying assumptions"]}
        elif stage == "critique":
            state["critique"] = {"status": "flagged", "risks": ["timing may be endogenous", "synthetic fixture has no external validity"]}
        elif stage == "log":
            state["decision"]["logged_at"] = now()
    return state


def stage_note(stage: str) -> str:
    return {
        "capture": "Question captured without pretending it is already a hypothesis.",
        "plan": "A minimal plan was generated with an explicit falsifier.",
        "research": "Evidence was attached through source IDs, not free-floating prose.",
        "critique": "The critic surfaced threats before the decision stage.",
        "decide": "Human review kept the claim at pending.",
        "log": "The decision and provenance trail were persisted.",
        "resume": "A future session can resume from the saved stage and events.",
    }[stage]


def compact_summary(state: dict) -> str:
    workflow = state["workflow"]
    return (f"{state['project']['title']} | stage={workflow['stage']} | "
            f"events={len(state.get('events', []))} | claims={len(state.get('claims', []))} | "
            f"decision={state['decision']['status']}")
