---
title: ResearchOS protocol
tags: [research-memory, business-validation, provenance]
status: active
updated: 2026-08-18
---

# ResearchOS protocol

## Workflow

Each project moves through seven explicit stages. The memory is organized around a business hypothesis and its validation evidence, not around a transcript or a pile of retrieved documents.

| Stage | Output | Gate |
| --- | --- | --- |
| capture | question and context | Is the question concrete enough to inspect? |
| plan | estimand, evidence plan, falsifier | Is the proposed test observable? |
| research | source records and extracted claims | Does every claim have provenance? |
| critique | assumptions, risks, counterarguments | What would change our mind? |
| decide | human-approved next action | Has a person accepted the tradeoff? |
| log | event and decision record | Can another session reconstruct the path? |
| resume | next starting point | Is unfinished work visible? |

## Business-validation memory

Every validation project should make five objects explicit:

1. **Hypothesis** — the belief, target segment, and expected behavior.
2. **Assumptions** — what must be true for the hypothesis to matter.
3. **Evidence** — observations, interviews, experiments, metrics, and source links.
4. **Falsifier** — the signal that would weaken or disprove the hypothesis.
5. **Decision** — what the team will do next, who approved it, and what evidence is still missing.

The dashboard should make the gap between *believed*, *observed*, and *validated* visible at a glance.

## Agent roles

- **Planner** turns an open question into a bounded plan.
- **Researcher** gathers and extracts evidence.
- **Critic** attacks assumptions and searches for disconfirming evidence.
- **Registrar** records provenance and decisions.
- **Human reviewer** owns approval, rejection, and publication boundaries.

## Public/private boundary

The public repository may contain protocol, prompts, synthetic fixtures, tests, and generic examples. It must not contain raw data, unpublished results, dissertation drafts, personal contacts, credentials, or private memory logs.

## Extension points

The demo intentionally has no model-provider dependency. A private adapter can replace `run_demo` with an LLM-backed implementation while preserving the same state shape and validation rules.
