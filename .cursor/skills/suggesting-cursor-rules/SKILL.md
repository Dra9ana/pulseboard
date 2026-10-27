---
name: suggesting-cursor-rules
description: >-
  Suggest a new Cursor rule after the same correction shows up more than once.
---

# Suggesting Cursor rules

When the user corrects the same invariant twice, propose one `.cursor/rules/*.mdc` file:

- YAML frontmatter with `description` and either `alwaysApply: true` or `globs`
- A short invariant and a STOP list
- A link to `docs/engineering/` if the why is longer than the rule

Show the draft and wait. Update `.cursor/rules/README.md` only after they accept it.
Do not add a rule for a one-off preference.
