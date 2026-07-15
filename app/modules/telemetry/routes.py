from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.telemetry.schema import (
    TelemetryCreate,
    TelemetryResponse
)

from app.modules.telemetry.service import (
    TelemetryService
)


router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

service = TelemetryService()


@router.post(
    "/",
    response_model=TelemetryResponse
)
def create_telemetry(
    payload: TelemetryCreate,
    db: Session = Depends(get_db)
):
    return service.create_telemetry(
        db,
        payload
    )


@router.get(
    "/",
    response_model=list[TelemetryResponse]
)
def get_telemetry(
    db: Session = Depends(get_db)
):
    return service.get_telemetry(
        db
    )


@router.get(
    "/{telemetry_id}",
    response_model=TelemetryResponse
)
def get_telemetry_by_id(
    telemetry_id: int,
    db: Session = Depends(get_db)
):
    return service.get_telemetry_by_id(
        db,
        telemetry_id
    )


@router.get(
    "/device/{device_id}",
    response_model=list[TelemetryResponse]
)
def get_device_telemetry(
    device_id: int,
    db: Session = Depends(get_db)
):
    return service.get_device_telemetry(
        db,
        device_id
    )


@router.get(
    "/device/{device_id}/latest",
    response_model=TelemetryResponse
)
def get_latest_device_telemetry(
    device_id: int,
    db: Session = Depends(get_db)
):
    return service.get_latest_device_telemetry(
        db,
        device_id
    )


@router.delete(
    "/{telemetry_id}"
)
def delete_telemetry(
    telemetry_id: int,
    db: Session = Depends(get_db)
):
    return service.delete_telemetry(
        db,
        telemetry_id
    )