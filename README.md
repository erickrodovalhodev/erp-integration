# erp-integration

Receives order webhooks and forwards them to the ERP with HMAC signing,
exponential retry, idempotency by key and a dead letter queue.

## run

    cp .env.example .env
    docker compose up

## why each piece exists

| Piece | Reason |
| --- | --- |
| HMAC-SHA256 signature | the ERP rejects unsigned bodies; the signature covers the raw bytes |
| Idempotency key | marketplaces replay webhooks; a duplicate must not create a second order |
| Exponential retry | transient 5xx and timeouts, capped at 8s, 3 attempts |
| Dead letter | retries exhausted; the event is parked with the last error, not lost |
| Correlation id | one id per webhook, present in every log line |

## contract

`docs/contract.md` — payload, headers, status codes.

## decisions

`docs/adr/0001-idempotency-by-client-key.md`

## tests

    pytest

Covers signature, retry and replay.
