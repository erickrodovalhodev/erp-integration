import asyncio
import os

# Configuração de teste: banco em memória e ERP fictício (nenhuma chamada real é feita).
os.environ["ERP_DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ.setdefault("ERP_URL", "http://mock-erp.invalid")
os.environ.setdefault("ERP_TOKEN", "test-token")
os.environ.setdefault("ERP_HMAC_SECRET", "test-secret")

from app.db import criar_tabelas  # noqa: E402

asyncio.run(criar_tabelas())
