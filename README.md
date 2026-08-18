# ResearchOS

> A local-first research memory system for long-running, AI-assisted research.

ResearchOS helps research agents remember the things a research project actually needs to preserve: questions, claims, sources, uncertainty, critiques, decisions, and unfinished workflow state.

It is not another chatbot wrapper or vector database. It is a transparent **research-memory protocol and audit layer** that can sit above an LLM, RAG stack, or agent framework.

## The idea

Most agent memory systems answer: “What fact should I retrieve for this prompt?”

ResearchOS also asks:

- What claim is this evidence allowed to support?
- Which source supports it?
- What would change our mind?
- Who approved the decision?
- Can another session resume the project without reconstructing the whole chat?

```text
capture → plan → research → critique → decide → log → resume
```

Agents propose. Evidence stays inspectable. Humans decide.

## 60-second demo

```bash
git clone https://github.com/JinkyongChoi1/researchos.git
cd researchos
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -e .

researchos demo
researchos show
researchos validate
```

The demo is dependency-free and uses only synthetic data.

![ResearchOS dashboard demo](assets/researchos-demo.gif)

Open [`site/index.html`](site/index.html) for the static dashboard. The dashboard and GIF are illustrative mockups; they do not contain real research data or measured results.

## Why this is different

| System | Primary memory object | Main strength | ResearchOS difference |
| --- | --- | --- | --- |
| Baseline RAG | Retrieved document chunks | Grounding answers in external text | Adds project state, critique, decisions, and resumable workflow |
| Mem0 | Extracted facts and preferences | General-purpose long-term memory for users, agents, and sessions | Uses research-native objects: claims, sources, falsifiers, and approval gates |
| Letta / MemGPT | Agent-managed working and archival memory | Stateful agents with explicit memory management | Makes the research record human-readable, reviewable, and portable outside one agent runtime |
| Zep / Graphiti | Temporal entities, relationships, and episodes | Dynamic graph retrieval over changing knowledge | Focuses on epistemic status and decision provenance, not only graph structure |
| Microsoft GraphRAG | Entity graph, communities, and summaries | Corpus-wide and entity-level retrieval | Governs how evidence becomes a research commitment across sessions |
| **ResearchOS** | **Questions, claims, evidence, critiques, decisions, and workflow events** | **Auditable, human-approved research memory** | **A domain protocol that can use the systems above as retrieval backends** |

These systems are complementary rather than mutually exclusive. A future ResearchOS adapter could use Mem0 for fact extraction, Graphiti for temporal retrieval, or a vector store for document search while keeping the ResearchOS claim-and-decision layer intact.

## What is included

- `researchos/` — dependency-free Python CLI and workflow engine.
- `fixtures/demo_project.json` — synthetic sources, claims, risks, and decisions.
- `site/` — static dashboard with no backend or tracking.
- `docs/protocol.md` — workflow stages, agent roles, and public/private boundaries.
- `tests/` — standard-library tests for workflow completion and provenance validation.
- `.github/workflows/` — automated tests and GitHub Pages deployment.

## Design principles

1. **Local-first** — private notes and data stay in the user’s workspace.
2. **Inspectable memory** — state is plain JSON, not hidden in a chat transcript.
3. **Provenance by default** — claims point to source IDs and excerpts.
4. **Human approval** — agents recommend; humans decide what becomes a research commitment.
5. **Resumable research** — the next session starts from logged state, not a blank context window.
6. **Provider-neutral** — model providers and retrieval backends are replaceable.

## Run checks

```bash
python3 -m unittest discover -s tests -v
```

## Privacy boundary

This repository is a clean-room synthetic demo. Do not copy private notes, unpublished findings, raw data, contacts, API keys, or local agent memory into it. Build private adapters outside the public repository.

## Status

MVP / synthetic demo. The protocol is the product surface; LLM adapters, retrieval backends, and storage layers are the next extension points.

## Research behind the comparison

- [RAG: Lewis et al. (2020)](https://arxiv.org/abs/2005.11401)
- [MemGPT: Packer et al. (2023)](https://arxiv.org/abs/2310.08560)
- [Mem0 documentation](https://docs.mem0.ai/introduction)
- [Letta documentation](https://docs.letta.com/)
- [Graphiti / Zep documentation](https://help.getzep.com/graphiti/getting-started/welcome)
- [Microsoft GraphRAG documentation](https://github.com/microsoft/graphrag/blob/main/docs/index.md)

## License

MIT. See [`LICENSE`](LICENSE).

