# Add the uv workspace and quality gate

## Done when

The repository is a uv workspace. The hello-world entry lives in a thin app shell and still prints `Hello from pulseboard!`. `make flct` runs the format check, the linter, and the tests, and that command passes.

## Behavior now

No handbook covers this yet. `main.py` at the repository root prints `Hello from pulseboard!`. There is one `pyproject.toml`, with no workspace members, Ruff, pytest, or Makefile.

## Behavior after

A developer can install the workspace with uv and run the same hello line from the thin shell. `make flct` is the quality gate: format check, lint, and tests. The shell does not contain domain rules. Domain packages stay uncreated.

## Owner

Composition root.

## Contract

None. The hello line stays a local process entry. This ticket does not add HTTP, SSE, a database, or stored JSON.

## Out of scope

Docker Compose, Postgres, Redis, Ollama, domain modules, MCP, agents, and any frontend.

## Verify

`make flct` does not exist yet. Today, `uv run python main.py` prints `Hello from pulseboard!`. After this pull request, `make flct` is the gate.
