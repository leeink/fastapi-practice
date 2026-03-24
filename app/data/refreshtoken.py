import uuid
from datetime import datetime

from sqlalchemy import UUID, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.database import Base

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("siteuser.id", ondelete="CASCADE"),
        nullable=False
    )
    token: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    user: Mapped["User"] = relationship("User")