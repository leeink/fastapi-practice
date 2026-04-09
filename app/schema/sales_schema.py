import datetime

from pydantic import BaseModel
import uuid

class SalesList(BaseModel):
    id: uuid.UUID
    date: datetime.date
    year: str
    month: str
    quarter: str
    region: str
    product_line: str
    units_sold: int
    discount_rate: float
    marketing_spend: int
    revenue: int

class SalesFilterRequest(BaseModel):
    year: str | None = None
    quarter: str | None = None
    region: str | None = None
    product_line: str | None = None