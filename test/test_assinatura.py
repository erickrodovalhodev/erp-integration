import hashlib, hmac
from app.services.erp_client import assinar
from app.settings import settings


def test_signature_is_hmac_of_raw_body():
    body = b'{"pedido_id": "P-1"}'
    esperado = hmac.new(settings.hmac_secret.encode(), body, hashlib.sha256).hexdigest()
    assert assinar(body) == esperado

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
