---
name: systematic-debugging
description: >-
  Debug a stuck ingest, aggregate worker, MCP tool, or agent loop with evidence
  before changing code.
---

# Systematic debugging

1. Write the expected trace: ingest, aggregate, anomaly, or `AGENT_START` → tool → `AGENT_END`.
2. Find the last step that actually happened (log, test failure, HTTP status).
3. State one hypothesis.
4. Change one thing and re-check that step.
5. Do not add a new agent or a new tool while a current tool fails.
