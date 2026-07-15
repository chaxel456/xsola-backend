from sqlalchemy.orm import Session
from app.modules.devices.model import Device


class DeviceRepository:

    def create(self, db: Session, data: dict):
        device = Device(**data)

        db.add(device)
        db.commit()
        db.refresh(device)

        return device

    def get_all(self, db: Session):
        return db.query(Device).all()

    def get_by_id(self, db: Session, device_id: int):
        return (
            db.query(Device)
            .filter(Device.id == device_id)
            .first()
        )

    def delete(self, db: Session, device):
        db.delete(device)
        db.commit()