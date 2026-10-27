---
name: propose
description: >-
  Write a change note and stop before code when a change crosses modules or
  touches HTTP, SSE, DB, or stored JSON. Invoke via /propose.
disable-model-invocation: true
---

# Propose

Write the change note, then stop. Do not implement until the user says to proceed.

## When this skill applies

Use it when a change does any of these:

- Crosses more than one module
- Changes HTTP, SSE, the database, or stored JSON
- Adds a capability that does not have a handbook yet

Skip it for a fix inside one function, tests, or formatting. Say that you skipped it and why, in one sentence, then continue.

## 1. Read before writing

Read the owning row in `docs/engineering/how-we-work/feature-placement.md`. If the area is unfamiliar, run `/onboard` first.

## 2. Write the note

Copy `docs/engineering/changes/_TEMPLATE.md` to `docs/engineering/changes/<slug>.md`.

- `<slug>` is lowercase English kebab-case, no date prefix
- Fill every section
- **Owner** is one module and one facade method
- **Compatibility** says what an existing client or stored row still does
- English only

## 3. Stop

Post the path. Then stop. The note is deleted in the same change that updates the handbook.
