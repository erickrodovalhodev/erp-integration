import hashlib, hmac, json
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception
from ..settings import settings


def assinar(body: bytes) -> str:
    return hmac.new(settings.hmac_secret.encode(), body, hashlib.sha256).hexdigest()


def _transitorio(erro: Exception) -> bool:
    if isinstance(erro, httpx.HTTPStatusError):
        return erro.response.status_code >= 500
    return isinstance(erro, (httpx.TimeoutException, httpx.ConnectError))


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8),
       retry=retry_if_exception(_transitorio), reraise=True)
async def enviar_pedido(payload: dict, correlation_id: str) -> None:
    body = json.dumps(payload).encode()
    async with httpx.AsyncClient(timeout=settings.timeout) as c:
        r = await c.post(f"{settings.erp_url}/pedidos", content=body, headers={
            "Authorization": f"Bearer {settings.erp_token}",
            "X-Assinatura": assinar(body),
            "X-Correlation-Id": correlation_id,
            "Content-Type": "application/json",
        })
        r.raise_for_status()
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

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
