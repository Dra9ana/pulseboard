# ADR 0001: Modular monolith

- **Status:** accepted
- **Date:** 2026-10-27
- **Author(s):** project owner

## Context

Pulseboard needs event ingest, metrics, anomaly detection, and an investigator agent with clear boundaries. A single developer runs it locally. A microservice split would add Compose services before there is a load profile to justify them.

## Options

### Option A — Modular monolith

One repository, domain packages, thin app shells, cross-package calls only through facades.

- **Pros:** One process to run, shared database transactions, boundaries that can be extracted later.
- **Cons:** Deploys together. Discipline has to hold the boundaries.

### Option B — Microservices from day one

Separate services for ingest, metrics, anomalies, and the agent.

- **Pros:** Independent scaling.
- **Cons:** More moving parts than a local portfolio project needs.

## Decision

Adopt a modular monolith: thin `pulseboard-server` and `pulseboard-worker` shells, domain packages, and shared libs. Cross-module calls go through `module_*/api.py`.

## Consequences

- The package map is in [architecture/overview.md](../architecture/overview.md).
- The worker is a separate process for aggregation and anomaly detection. It is still in this repository.
- The React UI is a later app, not a reason to split the backend.

## References

- [project-plan.md](../project-plan.md)
