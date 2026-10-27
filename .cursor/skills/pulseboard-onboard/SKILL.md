---
name: pulseboard-onboard
description: >-
  Warm-start for Pulseboard — read the project plan, AGENTS.md, and placement
  rules before implementing. Use at the start of a new chat or before a feature.
  Invoke via /onboard.
disable-model-invocation: true
---

# Pulseboard Onboard

Load project context before writing code. Do not implement anything until the summary is posted.

## 1. Read core docs

Use the Read tool on each file:

1. `AGENTS.md`
2. `docs/engineering/project-plan.md`
3. `docs/engineering/README.md`
4. `docs/engineering/how-we-work/feature-placement.md`
5. `docs/engineering/decisions/0002-production-langgraph-agents.md`

If the user names an area, also read the matching page under `docs/engineering/`.

## 2. Confirm invariants

1. Thin app shell — no domain logic in `apps/*/main.py`
2. Cross-module only via `module_*/api.py`
3. ORM only in `pulseboard-models`
4. Production agents run through `AiModule`. Other modules do not import `agents/`
5. Tools return aggregates. Prompts do not receive raw event dumps
6. Ollama is behind `LlmPort`. The app runs without the model
7. Personal private GitHub only
8. No Linear. Tickets are files in `tasks/`
9. Do not add a frontend unless the user asked
10. Planned packages are not live until the code exists

## 3. Reply with an onboarding summary

- **What is live** — the uv workspace, the hello entry in `apps/pulseboard-server`, `make flct`, plus docs and rules
- **Where this task belongs** — module, or "no code yet, next ticket"
- **Risks** — facade bypass, prompt dumps, describing planned work as shipped
- **Next command** — `/tasks` if they want the next ticket, otherwise wait

Wait for the user's task before editing files.
