from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy import select
from ..db import sessao
from ..models import EventoPedido
from ..services.erp_client import enviar_pedido

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


class PedidoIn(BaseModel):
    pedido_id: str
    status: str


@router.post("/", status_code=202)
async def receber(
    pedido: PedidoIn,
    x_idempotency_key: str = Header(...),
    x_correlation_id: str = Header(default=""),
):
    async with sessao() as s:
        existe = await s.scalar(
            select(EventoPedido).where(EventoPedido.idempotency_key == x_idempotency_key)
        )
        if existe:
            return {"duplicate": True}
        s.add(EventoPedido(idempotency_key=x_idempotency_key, **pedido.model_dump()))
        await s.commit()

    try:
        await enviar_pedido({**pedido.model_dump(), "idempotency_key": x_idempotency_key}, x_correlation_id)
    except Exception:
        raise HTTPException(502, "erp error, event queued")
    return {"ok": True}
# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
