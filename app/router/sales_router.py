from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse

from core.config import templates
from core.database import get_db
from schema.sales_schema import SalesFilterRequest
from service.sales_service import find_revenue_by_product, find_revenue_by_region, \
    find_revenue_by_year, find_all_stats_by_filter

router = APIRouter(prefix="/sales", tags=["sales"])

@router.get("/search",
            response_class=HTMLResponse,
            status_code=status.HTTP_200_OK)
def search_revenue(request: Request,
                   dto: SalesFilterRequest = Depends(), db: Session = Depends(get_db)):
    data = find_all_stats_by_filter(db, dto)
    return templates.TemplateResponse(
        request,
        "revenue_all.html",
        {
            "site_name" : "Revenue",
            "data" : data,
            "selected_filter" : dto.filter
        }
    )

@router.get("/byProduct",
            response_class=HTMLResponse,
            status_code=status.HTTP_200_OK,
            summary="Show revenue by product")
def get_revenue_by_product(request: Request, db: Session = Depends(get_db)):
    revenue = find_revenue_by_product(db)
    return templates.TemplateResponse(
        request,
        "revenue_product.html",
        {
            "site_name" : "Revenue by Product",
            "revenues" : revenue
        }
    )
@router.get("/byYear",
            response_class=HTMLResponse,
            status_code=status.HTTP_200_OK,
            summary="Show sales list")
def get_revenue_by_year(request: Request, db: Session = Depends(get_db)):
    revenue = find_revenue_by_year(db)
    return templates.TemplateResponse(
        request,
        "revenue_year.html",
        {
            "site_name" : "Sales Year",
            "revenues" : revenue
        }
    )

@router.get("/byRegion",
            response_class=HTMLResponse,
            status_code=status.HTTP_200_OK,
            summary="Show revenue by region")
def get_revenue_by_region(request: Request, db: Session = Depends(get_db)):
    revenue = find_revenue_by_region(db)
    return templates.TemplateResponse(
        request,
        "revenue_region.html",
        {
            "site_name" : "Revenue by Region",
            "revenues" : revenue
        }
    )