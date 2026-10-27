# First features

Ordered steps. Each step becomes one ticket when you run `/tasks`, then one pull request. This page is the sequence. It is not the ticket.

About five hours a week. No dates.

The app runs without a model until the AI phase.

## Early

1. Workspace and quality gate. uv workspace, Ruff, pytest, `make flct`. The hello-world entry moves into a thin shell.
2. Docker Compose for Postgres and Redis. An `ai` profile exists and stays empty until the agent. Ollama stays on the host.
3. Event ingest and read.
4. Metrics and funnels over HTTP (`get_metric`, `get_funnel`).

## Middle

5. Worker: aggregation, classical spike and drop detection, an incident row, and a list of alerts. Webhook delivery is part of this step only if it stays small. Otherwise it is the next ticket.

## AI phase

6. Our MCP server with five read-only tools: `get_metric`, `get_funnel`, `list_anomalies`, `top_events`, `get_event_samples`.
7. Investigator: LangGraph graph, `AiModule.investigate`, Ollama tool calling, a conclusion with evidence, the debug trace, and an SSE stream.

## After v1

`list_alerts`, `ack_alert`, `run_safe_sql` (allowlist), Reporter, React UI, Alert triage, one third-party MCP server as a side tool, vector search.

## Hardware

| Machine | Model |
|---------|-------|
| 8 GB RAM | `qwen2.5:3b` or `phi4-mini` |
| 16 GB RAM | `qwen2.5:7b` or `llama3.1:8b` |
| 16–32 GB RAM | `qwen2.5:14b` if you want a larger model |

A GPU is optional. If the model is slow, cap tokens and keep the agent to one to three tool calls.
