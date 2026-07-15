

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.devices.schema import (
    DeviceCreate,
    DeviceResponse
)

from app.modules.devices.service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)

service = DeviceService()


@router.post("/", response_model=DeviceResponse)
def create_device(
    payload: DeviceCreate,
    db: Session = Depends(get_db)
):
    return service.create_device(
        db,
        payload
    )


@router.get("/", response_model=list[DeviceResponse])
def get_devices(
    db: Session = Depends(get_db)
):
    return service.get_devices(db)


@router.get("/{device_id}",
            response_model=DeviceResponse)
def get_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    return service.get_device(
        db,
        device_id
    )


@router.delete("/{device_id}")
def delete_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    return service.delete_device(
        db,
        device_id
    )


@router.post("/{device_id}/activate")
def activate_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    return service.activate_device(
        db,
        device_id
    )


@router.post("/{device_id}/deactivate")
def deactivate_device(
        device_id: int,
        db: Session = Depends(get_db)
):
    return service.deactivate_device(
        db,
        device_id
    )