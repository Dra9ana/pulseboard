---
name: repo-tasks
description: >-
  Draft one Pulseboard ticket as markdown in tasks/. Same shape as a Linear
  issue, one issue per pull request. Invoke via /tasks. Does not call Linear.
  Stop before code.
disable-model-invocation: true
---

# Repo tasks

Write one ticket, then stop. Do not implement it in the same turn.

## When

Use this when the user wants the next ticket, a spec for one pull request, or a rewrite of a thin task file.

Do not use it to implement an existing ticket. That chat starts with `/onboard`, then the task filename.

## 1. Read only enough to name the owner

Read `docs/engineering/project-plan.md`, `docs/engineering/how-we-work/first-features.md`, and `docs/engineering/how-we-work/feature-placement.md`.
List files already in `tasks/` (skip `README.md` and `_TEMPLATE.md`). The next ticket is the next undone step in `first-features.md`, unless the user named a different one.

Write **one** issue. If they ask for a series, still write only the next one and say which step comes after it.

## 2. File

Copy `tasks/_TEMPLATE.md` to `tasks/<nn>-<slug>.md`.

- `<nn>` is the next two-digit number (`01`, `02`, …)
- `<slug>` is lowercase English kebab-case
- Fill every section. Delete the template prompts
- English only
- Do not invent priority, estimate, assignee, or dates

## 3. Sections the file must contain

```markdown
## Done when
## Behavior now
## Behavior after
## Owner
## Contract
## Out of scope
## Verify
```

- **Owner** is one module and one facade method, or "composition root" for the workspace ticket
- **Contract** is `None`, or the surface (HTTP, SSE, DB, stored JSON) and whether it is additive
- If Contract is not `None`, say that implementation starts with `/propose`
- **Verify** names `make flct` once that target exists, otherwise the check that exists today

## 4. Stop

Post the file path and the title. Then stop. Do not edit application code. Do not call Linear. Do not start `/propose` unless the user asks.
