# Pulseboard

Local-first real-time analytics with anomaly detection and an on-prem agentic investigator that uses MCP tools over metrics and funnels (Ollama, zero cloud LLM cost).

The investigator explains a metric spike from tool evidence. It does not answer questions about uploaded documents.

| Pulseboard | A document RAG app |
|------------|--------------------|
| Events, metrics, funnels | Uploaded files and chunks |
| Tools over the analytics API | Semantic search over documents |
| Why checkout conversion dropped | What a contract says |
| Local Ollama | A hosted model API |
| Postgres and Redis | A vector database as the core |

Incident memory is a short report row in Postgres. Vector search is a later bonus, not the core.

## Status

The repository is the uv skeleton plus the engineering map. Domain packages are **planned**. See [docs/engineering/project-plan.md](docs/engineering/project-plan.md).

```bash
uv run python main.py
```

## Agent trace (target)

When the Investigator ships, a run logs:

```text
ALERT → AGENT_START
  → tool:get_metric
  → tool:get_funnel
  → tool:top_events
  → CONCLUSION + EVIDENCE
AGENT_END (latency, tools_used, tokens_local)
```

## Models

Ollama on the host. Start with `qwen2.5:7b` or `llama3.1:8b`. On an 8 GB machine use `qwen2.5:3b` or `phi4-mini`. `qwen2.5:14b` wants 16–32 GB RAM. A GPU is optional.

The Compose `ai` profile is planned. The app and anomaly detection run without a model. The agent is optional.

## Repository

Personal private GitHub only. Tickets live in [`tasks/`](tasks/README.md). New chat: `/onboard`. Next ticket: `/tasks`.
