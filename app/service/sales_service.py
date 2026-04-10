import uuid

from sqlalchemy import Sequence, select, func, literal
from sqlalchemy.orm import Session

from data.sales import Sales
from schema.sales_schema import SalesFilterRequest


def find_all_sales(db: Session) -> Sequence[Sales]:
    result = db.execute(
        select(Sales)
    )
    return result.scalars().all()

def find_sales_by_id(db: Session, sid: str | uuid.UUID) -> Sales | None:
    result = db.execute(
        select(Sales)
        .where(Sales.id == sid)
    )
    return result.scalars().one_or_none()

def find_sales_by_quarter(db: Session, quarter: str) -> Sequence[Sales]:
    result = db.execute(
        select(Sales)
        .where(Sales.quarter == quarter)
    )
    return result.scalars().all()

def find_sales_by_year(db: Session, year: str) -> Sequence[Sales]:
    result = db.execute(
        select(Sales)
        .where(Sales.year == year)
    )
    return result.scalars().all()

def find_revenue_by_product(db: Session):
    result = db.execute(
        select(Sales.product_line, func.sum(Sales.revenue).label("revenue"))
        .group_by(Sales.product_line)
    )
    return result.all()

def find_revenue_by_region(db: Session):
    result = db.execute(
        select(Sales.region, func.sum(Sales.revenue).label("revenue"))
        .group_by(Sales.region)
    )
    return result.all()

def find_revenue_by_year(db: Session):
    result = db.execute(
        select(Sales.year, func.sum(Sales.revenue).label("revenue"))
        .group_by(Sales.year)
        .order_by(Sales.year.asc())
    )
    return result.all()

## 연도별 추이: 매출, 마케팅 비용, 판매량
def find_all_stats_by_filter(db: Session, dto: SalesFilterRequest):
    group_col = getattr(Sales, dto.filter)

    query = (
        select(
            Sales.year,
            group_col.label("label"),
            func.sum(Sales.revenue).label("revenue"),
            func.sum(Sales.marketing_spend).label("spend"),
            func.sum(Sales.units_sold).label("units")
        )
        .group_by(Sales.year, group_col)
        .order_by(Sales.year)
    )

    return db.execute(query).all()