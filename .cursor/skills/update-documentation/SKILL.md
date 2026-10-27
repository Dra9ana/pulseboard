---
name: update-documentation
description: >-
  Refresh Pulseboard docs from recent changes and fix broken links.
  Invoke via /update-docs.
disable-model-invocation: true
---

# Update documentation

Sync engineering docs with the code, then check links.

## Update when stale

- `docs/engineering/**`
- `docs/README.md`
- `README.md`
- `AGENTS.md`
- `.cursor/rules/README.md`
- `.cursor/skills/README.md` (index only)

## Leave alone unless user-visible behavior changed

- `docs/product/`

## Do not rewrite accepted ADRs

Add a new ADR for a new architectural decision.

## Steps

1. Read `git log` and `git diff` for docs versus code since the last docs commit. If this is the first docs commit, read the tree.
2. Fix claims that call planned packages live, or live behavior planned.
3. Update the feature handbook when a capability shipped.
4. Check relative links in the files you touched.
5. Summarize what changed.
