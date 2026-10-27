# Cursor Rules — Pulseboard

Operative rules for AI assistants working in this repository. Open the repository root as the workspace so these files load.

Long-form docs live in [`docs/engineering/`](../../docs/engineering/README.md). Rules stay short. If this index and a rule diverge, the rule wins.

## How rules are tiered

| Tier | When it applies | Purpose |
|------|-----------------|---------|
| 1 — Always on | Every chat | Language, map, placement, docs, agents policy, GitHub, tickets, no UI unless asked |
| 2 — Cross-cutting | Matching globs | Ports, FastAPI, naming, package layout |
| 3 — Domain | `module_ai` and `mcp` | Production agents |

## Rule index

| File | Scope |
|------|-------|
| [english-only.mdc](english-only.mdc) | English for new code, comments, rules, commits |
| [monolith-overview.mdc](monolith-overview.mdc) | Repo map and golden rules |
| [feature-placement.mdc](feature-placement.mdc) | Which module owns a feature |
| [documentation-quality.mdc](documentation-quality.mdc) | Current-state claims and handbooks |
| [private-github.mdc](private-github.mdc) | Personal private GitHub only |
| [no-linear.mdc](no-linear.mdc) | Tickets are files in `tasks/` |
| [no-frontend-unless-asked.mdc](no-frontend-unless-asked.mdc) | No React UI unless asked |
| [ports-adapters.mdc](ports-adapters.mdc) | Ports and adapters |
| [fastapi-routes-facades.mdc](fastapi-routes-facades.mdc) | Thin routes and facades |
| [python-naming.mdc](python-naming.mdc) | Python names |
| [python-package-structure.mdc](python-package-structure.mdc) | Package layout |
| [production-agents.mdc](production-agents.mdc) | LangGraph agents and MCP tools |

## Related

| Doc | Purpose |
|-----|---------|
| [AGENTS.md](../../AGENTS.md) | Commands and invariants |
| [Project plan](../../docs/engineering/project-plan.md) | Map of the product and the build order |
| [Skills](../skills/README.md) | Workflows and slash commands |
