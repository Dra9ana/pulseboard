# AGENTS.md — Guide for AI Assistants

Start a new chat with **`/onboard`**.

## Commands

| Command | Purpose |
|---------|---------|
| `/onboard` | Load the plan and invariants before coding |
| `/tasks` | Write the next ticket into `tasks/`, then stop |
| `/propose` | Change note, then stop, before a contract change |
| `/flct` | Loop until the quality gate passes |
| `/code-review-backend` | Read-only review before commit |
| `/commit` | Small conventional commits on a feature branch |
| `/ponytail` | Shortest change that keeps the architecture |
| `/ponytail-review` | Diff review for extra code only |
| `/update-docs` | Refresh docs and links |

Skill index: [.cursor/skills/README.md](.cursor/skills/README.md).

There is no Linear command. Tickets are markdown files.

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/engineering/project-plan.md](docs/engineering/project-plan.md) | Product map and build order |
| [docs/engineering/README.md](docs/engineering/README.md) | Engineering index |
| [docs/engineering/how-we-work/first-features.md](docs/engineering/how-we-work/first-features.md) | Ordered steps, not full tickets |
| [docs/engineering/decisions/README.md](docs/engineering/decisions/README.md) | ADRs |
| [tasks/README.md](tasks/README.md) | Ticket folder |

## Invariants

1. Thin app shell — no domain logic in `apps/*/main.py`
2. Cross-module only via `module_*/api.py`
3. ORM only in `pulseboard-models`
4. Production agents run through `AiModule`
5. Tools return aggregates or a small sample
6. Ollama is behind `LlmPort`. The app runs without the model
7. Personal private GitHub only
8. No Linear API
9. No frontend unless the user asks
10. Planned work stays labeled planned until the code exists

## Do not

- Import `module_ai.agents` from another module
- Put raw events into a prompt
- Treat vector search as the incident store
- Add a git remote or push without an explicit ask
- Commit on `master` or merge to `master`. The owner merges the pull request
- Call Linear
