---
title: Business-validation memory specification
tags: [business-validation, research-memory, product-management]
status: active
updated: 2026-08-18
---

# Business-validation memory specification

## Problem

Founders and product teams collect interviews, metrics, ideas, and competitor evidence in separate tools.
The result is not merely lost context; it is an inability to tell which evidence supports which business hypothesis, what would falsify it, and why the team made its last decision.

## Product thesis

ResearchOS should treat business validation as a first-class memory object rather than as a collection of retrieved documents.

The minimum useful unit is:

```text
hypothesis → assumption → evidence → falsifier → decision → next test
```

## Goals

- Make the current hypothesis and target segment visible in under 10 seconds.
- Show observed, missing, and contradictory evidence separately.
- Preserve the source and reasoning behind each decision.
- Make the next validation test obvious when a hypothesis remains untested.
- Allow a new agent or teammate to resume without replaying the entire conversation.

## Non-goals for MVP

- Replacing a CRM, analytics warehouse, or experiment platform.
- Claiming statistical validity from interviews or small samples.
- Building a new vector database or knowledge-graph engine.
- Automatically approving a business decision.

## Core objects

| Object | Required fields | Purpose |
| --- | --- | --- |
| Hypothesis | statement, segment, expected behavior, status | State what the team believes and for whom |
| Assumption | statement, importance, confidence, falsifier | Expose what must be true |
| Evidence | type, source, excerpt, signal, status | Separate observation from interpretation |
| Decision | action, owner, status, rationale | Record what the team will do |
| Validation task | question, method, deadline, success signal | Turn uncertainty into the next test |

## Dashboard acceptance criteria

- The first screen shows one active hypothesis and its target segment.
- Evidence is grouped into observed, missing, and contradictory states.
- At least one falsifier is visible without opening a detail view.
- The next decision is distinct from the current belief.
- Synthetic data is clearly labeled.
- No dashboard component requires a model provider or hosted database.

## Success metrics

- A new user can explain the current hypothesis, evidence gap, and next action after a 60-second demo.
- A teammate can reconstruct the latest decision from the dashboard and source ledger without reading chat history.
- Every published claim in the demo has a source ID or is explicitly marked as unverified.

## Future adapters

ResearchOS can use a vector store, Mem0, Graphiti, or another retrieval system underneath this protocol.
Those systems answer retrieval questions; ResearchOS should preserve the business-validation semantics and approval boundary above them.

