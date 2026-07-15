print("REPORT ROUTES LOADED")

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.reports.service import (
    ReportService
)

from app.modules.reports.schema import (
    DashboardReport
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

service = ReportService()


@router.get(
    "/dashboard",
    response_model=DashboardReport
)
def dashboard(
    db: Session = Depends(get_db)
):
    return service.get_dashboard(db)