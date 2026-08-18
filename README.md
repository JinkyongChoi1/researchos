# ResearchOS

> A local-first research operating system for long-running, AI-assisted research.

ResearchOS makes an AI research workflow inspectable and resumable. It treats agents as role-based collaborators, keeps provenance beside every claim, and leaves consequential decisions to a human.

## 60-second demo

```bash
python3 -m researchos demo
python3 -m researchos show
```

The demo uses only synthetic data. It runs:

`capture → plan → research → critique → decide → log → resume`

![ResearchOS dashboard demo](assets/researchos-demo.gif)

The dashboard image and GIF are illustrative mockups built from synthetic content; they do not represent real research data or measured results.

Open `site/index.html` directly in a browser to inspect the same demo state as a static dashboard.

## What is included

- `researchos/`: dependency-free Python CLI and workflow engine.
- `fixtures/demo_project.json`: synthetic project, sources, claims, and decisions.
- `site/`: static dashboard with no tracking and no backend.
- `assets/`: launch-ready dashboard mockup and short animated demo.
- `docs/protocol.md`: the operating protocol and safety boundaries.
- `tests/`: standard-library tests for the workflow and provenance checks.

## Design principles

1. **Local-first** — your notes and data stay in your workspace.
2. **Inspectable memory** — state is plain JSON, not hidden in a chat transcript.
3. **Provenance by default** — claims point to source IDs and excerpts.
4. **Human approval** — agents can recommend; humans decide what becomes a research commitment.
5. **Reproducible logs** — every transition records who acted, when, and why.

## Run checks

```bash
python3 -m unittest discover -s tests -v
```

## Privacy boundary

This repository is intentionally a clean-room demo. Do not copy private notes, unpublished findings, raw data, contacts, API keys, or local agent memory into it. Add your own private adapter outside the public repository if you need to connect it to real work.

## Status

MVP / synthetic demo. The protocol is the product surface; model providers and storage backends are intentionally replaceable.

## License

MIT. See `LICENSE`.
