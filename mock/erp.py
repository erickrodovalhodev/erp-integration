"""ERP falso para desenvolvimento local: valida a assinatura HMAC e responde 200."""
import hashlib, hmac, os

from fastapi import FastAPI, Header, HTTPException, Request

SEGREDO = os.environ.get("ERP_HMAC_SECRET", "dev-secret").encode()
app = FastAPI(title="mock-erp")


@app.post("/pedidos")
async def pedidos(request: Request, x_assinatura: str = Header(...)):
    corpo = await request.body()
    esperado = hmac.new(SEGREDO, corpo, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(esperado, x_assinatura):
        raise HTTPException(401, "assinatura inválida")
    return {"recebido": True}
