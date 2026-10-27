---
name: grinding-until-pass
description: >-
  Loop until the Pulseboard quality gate passes. Invoke via /flct after code changes.
disable-model-invocation: true
---

# Grind until pass

Run the quality gate and fix failures. Repeat until it passes or a failure is a product decision.

## Gate

If `make flct` exists, that is the gate (format, lint, tests).

If it does not exist yet, say so. Run `uv run pytest` and, if Ruff is installed, `uv run ruff check` and `uv run ruff format --check`. Do not invent a Makefile inside this skill.

## Loop

1. Run the gate.
2. Read the first failure.
3. Fix the cause in the owning module.
4. Run the gate again.

Stop after the same failure survives three fixes, and report the command output.
