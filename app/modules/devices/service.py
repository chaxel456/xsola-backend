print("DEVICE SERVICE LOADED")


from fastapi import HTTPException

from app.modules.devices.repository import DeviceRepository
from app.modules.customers.model import Customer
from app.services.mqtt_service import (
    MQTTService
)

class DeviceService:

    def __init__(self):
        self.repo = DeviceRepository()
        self.mqtt = MQTTService()       

    def create_device(self, db, payload):

        customer = db.query(Customer).filter(
            Customer.id == payload.customer_id
        ).first()

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return self.repo.create(
            db,
            payload.model_dump()
        )

    def get_devices(self, db):
        return self.repo.get_all(db)

    def get_device(self, db, device_id):

        device = self.repo.get_by_id(
            db,
            device_id
        )

        if not device:
            raise HTTPException(
                status_code=404,
                detail="Device not found"
            )

        return device

    def delete_device(self, db, device_id):

        device = self.repo.get_by_id(
            db,
            device_id
        )

        if not device:
            raise HTTPException(
                status_code=404,
                detail="Device not found"
            )

        self.repo.delete(db, device)

        return {
            "message": "Device deleted"
        }

    def activate_device(
        self,
        db,
        device_id: int
    ):
        device = self.repo.get_by_id(
            db,
            device_id
        )

        if not device:
            raise HTTPException(
                status_code=404,
                detail="Device not found"
            )

        device.status = "active"

        db.commit()
        db.refresh(device)

        self.mqtt.publish(
            f"xsola/device/{device.id}/control",
            {
                "command": "ON"
            }
        )        

        return {
            "message": "Device activated",
            "device_id": device.id
        }

    def deactivate_device(
        self,
        db,
        device_id: int
    ):
        device = self.repo.get_by_id(
            db,
            device_id
        )

        if not device:
            raise HTTPException(
                status_code=404,
                detail="Device not found"
            )

        device.status = "inactive"

        db.commit()
        db.refresh(device)

        self.mqtt.publish(
            f"xsola/device/{device.id}/control",
            {
                "command": "OFF"
            }
        )


        return {
            "message": "Device deactivated",
            "device_id": device.id
        }