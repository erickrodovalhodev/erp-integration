from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from ..db import sessao
from ..models import EventoPedido

router = APIRouter(prefix="/eventos", tags=["eventos"])


@router.get("/{idempotency_key}")
async def buscar(idempotency_key: str):
    async with sessao() as s:
        evento = await s.scalar(
            select(EventoPedido).where(EventoPedido.idempotency_key == idempotency_key)
        )
    if evento is None:
        raise HTTPException(404, "evento não encontrado")
    return {
        "idempotency_key": evento.idempotency_key,
        "pedido_id": evento.pedido_id,
        "status": evento.status,
        "tentativas": evento.tentativas,
        "ultimo_erro": evento.ultimo_erro,
        "processed_at": evento.processed_at,
    }
