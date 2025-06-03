# Webhook contract

## `POST /pedidos`

Headers:

| Header | Required | Value |
| --- | --- | --- |
| `Content-Type` | yes | `application/json` |
| `X-Idempotency-Key` | yes | UUID v4, unique per event |
| `X-Correlation-Id` | no | echoed in every log line |

Body:

    { "idempotency_key": "uuid", "pedido_id": "string", "status": "paid|canceled|refunded" }

Responses:

| Code | Meaning |
| --- | --- |
| 202 | accepted and persisted |
| 200 | duplicate key, already processed |
| 422 | invalid payload |
| 502 | ERP failed, event kept for reprocess |

## Outbound to the ERP

`POST {ERP_URL}/pedidos` with `Authorization: Bearer`, `X-Assinatura`
(HMAC-SHA256 hex over the raw JSON bytes) and the same correlation id.
