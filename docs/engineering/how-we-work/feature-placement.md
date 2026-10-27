# Where code goes

Name the owning module before writing code. Packages exist when their ticket lands. Until then they are planned.

| Question / feature | Module |
|--------------------|--------|
| Event ingest and read | `module-events` |
| Aggregates, funnels, segments | `module-metrics` |
| Spike/drop, alerts, incident rows | `module-anomalies` |
| Threads and SSE | `module-chat`, which calls `AiModule` |
| Investigator, Reporter, Alert triage | `module-ai` |
| New table | `pulseboard-models` |
| Ollama, Postgres, Redis client | `pulseboard-connectors` and a port in `pulseboard-core` |
| MCP tool | `mcp/`, calling a facade |

## Rules

- Another module never imports `module_ai.agents`.
- Routes call `api.py` only.
- `apps/pulseboard-server/main.py` wires modules. It does not decide domain rules.
- A prompt receives tool output, not a dump of events.
- An incident is a Postgres row, not a vector document.

The same table is in `.cursor/rules/feature-placement.mdc`. If they diverge, the rule file wins and this page should be updated.
