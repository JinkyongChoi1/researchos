# ResearchOS protocol

## Workflow

Each project moves through seven explicit stages.

| Stage | Output | Gate |
| --- | --- | --- |
| capture | question and context | Is the question concrete enough to inspect? |
| plan | estimand, evidence plan, falsifier | Is the proposed test observable? |
| research | source records and extracted claims | Does every claim have provenance? |
| critique | assumptions, risks, counterarguments | What would change our mind? |
| decide | human-approved next action | Has a person accepted the tradeoff? |
| log | event and decision record | Can another session reconstruct the path? |
| resume | next starting point | Is unfinished work visible? |

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
