import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Date, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Sales(Base):
    __tablename__ = 'sales'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    date: Mapped[datetime.date] = mapped_column(
        Date, nullable=False, default=datetime.date.today
    )
    year: Mapped[str] = mapped_column(
        String
    )
    month: Mapped[str] = mapped_column(
        String
    )
    quarter: Mapped[str] = mapped_column(
        String
    )
    region: Mapped[str] = mapped_column(
        String
    )
    product_line: Mapped[str] = mapped_column(
        String
    )
    units_sold: Mapped[int] = mapped_column(
        Integer, default=0
    )
    unit_price: Mapped[int] = mapped_column(
        Integer, default=0
    )
    discount_rate: Mapped[float] = mapped_column(
        Float, default=0.0
    )
    marketing_spend: Mapped[int] = mapped_column(
        Integer, default=0
    )
    revenue: Mapped[int] = mapped_column(
        Integer, default=0
    )