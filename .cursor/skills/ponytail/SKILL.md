---
name: ponytail
description: >-
  Shortest change that still works. Use on coding tasks, or when the user says
  ponytail, yagni, simplest, or complains about over-engineering. Pulseboard
  architecture still wins.
argument-hint: "[lite|full|ultra]"
---

# Ponytail

Prefer the smallest change that solves the task. Intensity is `lite`, `full` (default), or `ultra`.

## Architecture still wins

Do not remove:

- The owning module's facade and service layer
- Ports and adapters, even when one adapter exists
- `AiModule` as the only entry to agents
- English identifiers
- A handbook update when behavior ships
- Tests next to the package

"Fewer files" still means the required layers of the owning module. Do not put domain logic in `main.py` to save a file.

## Ladder

1. Does this need to exist for the current ticket?
2. Can the standard library do it?
3. Can an existing function do it?
4. One clear function before a new framework.

Off only when the user says "stop ponytail" or "normal mode".
