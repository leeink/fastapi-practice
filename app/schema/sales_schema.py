import datetime

from pydantic import BaseModel
from typing import Optional
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
    filter: str = "product_line"