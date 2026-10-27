# Cursor

Open this repository root as the workspace. Rules in `.cursor/rules/` load from that root.

## What lives in `.cursor/`

| Folder | What it is |
|--------|------------|
| [`.cursor/rules/`](../../../.cursor/rules/README.md) | Short invariants, applied automatically |
| [`.cursor/skills/`](../../../.cursor/skills/README.md) | Workflows |
| [`.cursor/commands/`](../../../.cursor/commands/) | Slash commands |

Rules are the laws. Skills are the playbooks. Commands start a playbook.

## Slash commands

| Command | When |
|---------|------|
| `/onboard` | Start of a new chat. The agent reads the plan and waits. |
| `/tasks` | Write the next ticket into `tasks/`. One ticket. Then it stops. |
| `/propose` | Before code, when the change crosses modules or touches HTTP, SSE, the database, or stored JSON. |
| `/flct` | After code. Loop until the quality gate passes. |
| `/code-review-backend` | Read-only review before commit. |
| `/commit` | Small conventional commits on a feature branch. The owner merges to `master`. |
| `/ponytail` | Shortest implementation that keeps facades, ports, and tests. |
| `/ponytail-review` | Hunt extra code in the diff. |
| `/update-docs` | Refresh docs and links. |

`python-tdd-with-uv`, `parallel-exploring`, `systematic-debugging`, and `suggesting-cursor-rules` have no slash command. The agent uses them when the task matches.

## Typical flow

1. `/onboard`
2. `/tasks` for the next pull request
3. A new chat implements that file. If the contract is not `None`, start with `/propose`
4. `/code-review-backend`, then `/flct`, then `/commit`
5. `/update-docs` when behavior or the map changed

Linear is not part of this flow.
