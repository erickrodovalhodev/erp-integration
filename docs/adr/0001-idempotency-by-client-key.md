# ADR 0001 — Idempotency by client key

## Context

Marketplaces replay webhooks on timeout. A replay that reaches the ERP twice
creates a duplicate order, which the warehouse ships.

## Decision

The caller sends `X-Idempotency-Key`. The key has a unique index and is checked
before enqueueing. A replay returns `200` with `duplicate: true` and does not
call the ERP.

## Consequences

- Duplicate protection depends on the caller honouring the key.
- The table grows; a retention job drops keys older than 30 days.
- A replayed event is not reprocessed even if the first attempt is still in
  flight — the caller polls the status endpoint instead.
