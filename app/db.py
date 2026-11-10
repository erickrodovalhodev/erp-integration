from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from .models import Base
from .settings import settings


def _engine_kwargs(url: str) -> dict:
    # SQLite em memória: uma única conexão compartilhada, senão cada conexão vê um banco vazio.
    if url.startswith("sqlite") and ":memory:" in url:
        return {"poolclass": StaticPool, "connect_args": {"check_same_thread": False}}
    return {"pool_pre_ping": True}


engine = create_async_engine(settings.database_url, **_engine_kwargs(settings.database_url))
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def sessao() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as s:
        try:
            yield s
            await s.commit()
        except Exception:
            await s.rollback()
            raise


async def criar_tabelas() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
