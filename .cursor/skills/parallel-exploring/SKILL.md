---
name: parallel-exploring
description: >-
  Find where a behavior lives across Pulseboard modules by searching in parallel.
  Use when the user asks where something is implemented.
---

# Parallel exploring

Search before reading whole trees.

1. Name the owning module from `docs/engineering/how-we-work/feature-placement.md`.
2. Search that package, `libs/`, and `mcp/` for the symbol.
3. Report the facade method and the file. Say **planned** if the package is not on disk yet.
