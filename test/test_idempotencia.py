import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@patch("app.routers.pedidos.enviar_pedido", new_callable=AsyncMock)
def test_replay_calls_erp_once(enviar):
    corpo = {"pedido_id": "P-1", "status": "paid"}
    h = {"X-Idempotency-Key": "chave-unica"}
    assert client.post("/pedidos/", json=corpo, headers=h).status_code == 202
    r = client.post("/pedidos/", json=corpo, headers=h)
    assert r.status_code == 200 and r.json()["duplicate"] is True
    assert enviar.await_count == 1


def test_missing_key_is_422():
    assert client.post("/pedidos/", json={"pedido_id": "P", "status": "paid"}).status_code == 422

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
