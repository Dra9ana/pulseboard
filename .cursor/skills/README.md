# Cursor Skills — Pulseboard

Project skills in `.cursor/skills/`. Slash commands live in `.cursor/commands/`.

**Rules vs skills:** `.cursor/rules/` are invariants. Skills are on-demand workflows. If this index and a skill diverge, the skill wins.

## All skills

| Skill | Slash command | When to use |
|-------|---------------|-------------|
| [pulseboard-onboard](pulseboard-onboard/SKILL.md) | `/onboard` | Start of a new chat, before a feature |
| [repo-tasks](repo-tasks/SKILL.md) | `/tasks` | Draft the next ticket into `tasks/`, then stop |
| [propose](propose/SKILL.md) | `/propose` | Change note, then stop, before a contract change |
| [python-tdd-with-uv](python-tdd-with-uv/SKILL.md) | — | New backend logic and tests |
| [grinding-until-pass](grinding-until-pass/SKILL.md) | `/flct` | Loop until the quality gate passes |
| [code-review-backend](code-review-backend/SKILL.md) | `/code-review-backend` | Read-only review before commit |
| [committing](committing/SKILL.md) | `/commit` | Small conventional commits on a feature branch |
| [update-documentation](update-documentation/SKILL.md) | `/update-docs` | Refresh docs and links |
| [ponytail](ponytail/SKILL.md) | `/ponytail` | Shortest change that still keeps the architecture |
| [ponytail-review](ponytail-review/SKILL.md) | `/ponytail-review` | Diff review for extra code only |
| [parallel-exploring](parallel-exploring/SKILL.md) | — | Where does this live, across modules |
| [systematic-debugging](systematic-debugging/SKILL.md) | — | Agent loop, worker, or ingest stuck |
| [suggesting-cursor-rules](suggesting-cursor-rules/SKILL.md) | — | Suggest a new rule after repeated corrections |

## Recommended chat flow

```
New chat                         →  /onboard
Next ticket (one at a time)      →  /tasks
Contract-sized change            →  /propose  →  wait  →  implement
Backend feature                  →  python-tdd-with-uv
Before commit                    →  /code-review-backend  →  /flct  →  /commit
Over-building                    →  /ponytail or /ponytail-review
Docs drifted                     →  /update-docs
```

There is no Linear command. Tickets are files.

## Adding a skill

1. Create `.cursor/skills/<name>/SKILL.md` with `name` and `description`.
2. Add `disable-model-invocation: true` when the skill should run only from a slash command.
3. Update this README.
4. Add `.cursor/commands/<name>.md` when it has a slash command.
