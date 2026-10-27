---
name: python-tdd-with-uv
description: >-
  Test-driven development with uv and pytest. Use when adding backend logic,
  services, facades, or worker behavior.
---

# Python TDD with uv

## Commands

```bash
uv run pytest
uv run pytest -k "test_name" -x
```

After the workspace ticket lands, `make flct` is the full gate. Until that Makefile exists, say so and run `uv run pytest` on the tests that exist.

Always use `uv run`. Do not activate a venv by hand.

## Where tests live

| Code | Tests |
|------|-------|
| `apps/pulseboard-server/` | `apps/pulseboard-server/tests/` |
| `packages/module-*/` | `packages/module-*/tests/` |
| `libs/pulseboard-*/` | `libs/pulseboard-*/tests/` |
| `mcp/` | `mcp/tests/` |

## Cycle

1. One failing test for the next behavior.
2. The minimum code that passes.
3. Refactor inside the owning module's layers (schema, facade, service, port).

Do not put the test's behavior in `apps/*/main.py`. Do not skip the facade because there is one caller.
