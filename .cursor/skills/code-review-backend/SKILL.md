---
name: code-review-backend
description: >-
  Read-only pre-commit review of backend changes — boundaries, facades, agents,
  security, and tests. Invoke via /code-review-backend.
disable-model-invocation: true
---

# Pre-commit backend review

Read-only. Do not edit code unless the user asks for fixes afterward.

## Scope

```bash
git status --short
git diff --stat
git diff
```

Review unstaged and staged backend files. If there is no diff, say so and stop.

## Check

- Owning module matches `feature-placement.mdc`
- Cross-module imports go through `api.py`
- Routes do not contain SQL or domain rules
- `module-ai` graphs are not imported by other modules
- LLM calls use `LlmPort`
- Tool results are aggregates or small samples
- New behavior has a test
- Secrets are not committed
- Planned behavior is not documented as live

## Report

Use three groups: blockers, suggestions, questions. End with one line: ready to commit, or not.
