# ADR 0002: Production LangGraph agents and our MCP server

- **Status:** accepted
- **Date:** 2026-10-27
- **Author(s):** project owner

## Context

The investigator must be a real agent loop (plan, tool, observe, answer) that another engineer would recognize in production. A notebook script or a chat over raw events would not show that. A third-party MCP server would hide tool schemas, limits, and errors.

## Options

### Option A — Compiled LangGraph graph behind AiModule, our MCP tools

The API calls the graph. Tools are our server. Other modules cannot import the graph.

- **Pros:** One production path. Facade matches the rest of the monolith. Tool design stays visible.
- **Cons:** More structure than a single function that calls Ollama.

### Option B — A script or a Studio-only graph

The interesting run happens in a debugger or a one-off script.

- **Pros:** Faster to demo once.
- **Cons:** The API path and the demo path diverge. Studio is a debugger.

### Option C — A public MCP server as the core

Wire Ollama to filesystem, fetch, or another generic server.

- **Pros:** Less tool code.
- **Cons:** The portfolio becomes wiring. Domain tools are the part worth learning.

## Decision

Ship the Investigator as a LangGraph graph executed from the API through `AiModule.investigate`. Our MCP server exposes the tools. v1 tools are read-only: `get_metric`, `get_funnel`, `list_anomalies`, `top_events`, `get_event_samples`.

LangGraph Studio may be added later as a local debugger. It is not the runtime.

Each run logs `AGENT_START`, tool names, a conclusion with evidence, and `AGENT_END` (latency, tools used, local tokens).

## Consequences

- `module-ai` has no HTTP router. `module-chat` mounts the stream and calls the facade.
- Reporter and Alert triage are later graphs in the same package, still behind `AiModule`.
- `ack_alert` and allowlisted `run_safe_sql` are not in the first tool set.
- A third-party MCP server is an optional later add-on.

## References

- [ADR 0003](0003-local-ollama.md)
- `.cursor/rules/production-agents.mdc`
