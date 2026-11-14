# erp-integration

Receives order webhooks and forwards them to the ERP with HMAC signing,
exponential retry, idempotency by key and a dead letter queue.

## run

    cp .env.example .env        # opcional: o compose já tem defaults locais
    docker compose up --build -d
    docker compose ps           # api :8000, mock-erp :9000, db (postgres 16)

Sobe três serviços: `api` (FastAPI + uvicorn), `db` (Postgres; as tabelas são
criadas no startup) e `mock-erp`, um ERP falso em `mock/erp.py` que valida o
header `X-Assinatura` com o mesmo `ERP_HMAC_SECRET`. Nenhum serviço externo é usado.

Para derrubar e apagar o volume:

    docker compose down -v

## demo

    # primeira entrega: 202 (persistido e enviado ao mock-erp)
    curl -si -X POST localhost:8000/pedidos -H 'X-Idempotency-Key: k1' \
      -H 'Content-Type: application/json' -d '{"pedido_id":"P1","status":"paid"}' | head -1

    # replay com a mesma chave: 200 {"duplicate": true}, o ERP não é chamado de novo
    curl -si -X POST localhost:8000/pedidos -H 'X-Idempotency-Key: k1' \
      -H 'Content-Type: application/json' -d '{"pedido_id":"P1","status":"paid"}' | head -1

    # consulta do evento: 200 com o evento, 404 se a chave não existir
    curl -s localhost:8000/eventos/k1
    curl -si localhost:8000/eventos/nao-existe | head -1

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

    python3 -m venv .venv && . .venv/bin/activate
    pip install -e ".[dev]"
    pytest -q

O `conftest.py` aponta `ERP_DATABASE_URL` para SQLite em memória; não precisa de Docker.

Covers signature, retry and replay.
