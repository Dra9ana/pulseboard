---
name: ponytail-review
description: >-
  Review a diff for extra code only. Invoke via /ponytail-review. Does not
  replace /code-review-backend.
disable-model-invocation: true
---

# Ponytail review

Read-only. List code that can be deleted without losing the ticket's behavior or the architecture rules in the ponytail skill.

## Steps

1. Read `git diff`.
2. List deletions only: unused abstractions, extra config, features the ticket did not ask for.
3. Do not propose deleting facades, ports, or tests that lock a behavior.
4. Stop. Do not edit unless the user asks.
