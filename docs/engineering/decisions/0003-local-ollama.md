# ADR 0003: Local Ollama, app runs without the model

- **Status:** accepted
- **Date:** 2026-10-27
- **Author(s):** project owner

## Context

The project must run on one machine with no hosted model bill. Event ingest, metrics, and anomaly detection are useful without a model. The investigator needs tool calling and should stay replaceable if the local runtime changes.

## Options

### Option A — Ollama behind LlmPort, Compose profile ai

Ollama runs on the host. The agent container calls `http://host.docker.internal:11434`. The `ai` profile is optional.

- **Pros:** No token cost. The platform still runs when the model is off. A later adapter can sit behind the same port.
- **Cons:** Model quality and speed depend on the machine.

### Option B — A hosted model API as the default

- **Pros:** Stronger tool calling on small hardware.
- **Cons:** Cost and a network dependency this project is avoiding.

## Decision

`LlmPort` is the only LLM entry. The first adapter is Ollama. Default models are `qwen2.5:7b` or `llama3.1:8b`, with `qwen2.5:3b` or `phi4-mini` on 8 GB RAM. Compose's `ai` profile starts the agent. The API, worker, Postgres, and Redis start without it.

## Consequences

- Services call `LlmPort`, not an Ollama client.
- Prompts stay short. Tools return aggregates.
- Offline use requires a completed `ollama pull` first.

## References

- [ADR 0002](0002-production-langgraph-agents.md)
- [first-features.md](../how-we-work/first-features.md)
