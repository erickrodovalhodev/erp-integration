from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class EventoPedido(Base):
    __tablename__ = "eventos_pedido"

    id: Mapped[int] = mapped_column(primary_key=True)
    idempotency_key: Mapped[str] = mapped_column(unique=True, index=True)
    pedido_id: Mapped[str]
    status: Mapped[str]
    tentativas: Mapped[int] = mapped_column(default=0)
    ultimo_erro: Mapped[str | None]
    processed_at: Mapped[datetime | None]

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
