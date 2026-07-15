from fastapi import HTTPException

from app.modules.telemetry.repository import (
    TelemetryRepository
)


class TelemetryService:

    def __init__(self):
        self.repo = TelemetryRepository()

    def create_telemetry(
        self,
        db,
        payload
    ):
        return self.repo.create(
            db,
            payload.model_dump()
        )

    def get_telemetry(
        self,
        db
    ):
        return self.repo.get_all(
            db
        )

    def get_telemetry_by_id(
        self,
        db,
        telemetry_id: int
    ):

        telemetry = self.repo.get_by_id(
            db,
            telemetry_id
        )

        if not telemetry:
            raise HTTPException(
                status_code=404,
                detail="Telemetry not found"
            )

        return telemetry

    def get_device_telemetry(
        self,
        db,
        device_id: int
    ):
        return self.repo.get_by_device(
            db,
            device_id
        )

    def get_latest_device_telemetry(
        self,
        db,
        device_id: int
    ):

        telemetry = self.repo.get_latest_by_device(
            db,
            device_id
        )

        if not telemetry:
            raise HTTPException(
                status_code=404,
                detail="No telemetry found for this device"
            )

        return telemetry

    def delete_telemetry(
        self,
        db,
        telemetry_id: int
    ):

        telemetry = self.repo.get_by_id(
            db,
            telemetry_id
        )

        if not telemetry:
            raise HTTPException(
                status_code=404,
                detail="Telemetry not found"
            )

        self.repo.delete(
            db,
            telemetry
        )

        return {
            "message": "Telemetry deleted"
        }