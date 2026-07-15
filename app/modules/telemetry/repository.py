from sqlalchemy.orm import Session

from app.modules.telemetry.model import Telemetry


class TelemetryRepository:

    def create(
        self,
        db: Session,
        data: dict
    ):
        telemetry = Telemetry(
            **data
        )

        db.add(
            telemetry
        )

        db.commit()

        db.refresh(
            telemetry
        )

        return telemetry

    def get_all(
        self,
        db: Session
    ):
        return db.query(
            Telemetry
        ).all()

    def get_by_id(
        self,
        db: Session,
        telemetry_id: int
    ):
        return db.query(
            Telemetry
        ).filter(
            Telemetry.id == telemetry_id
        ).first()

    def get_by_device(
        self,
        db: Session,
        device_id: int
    ):
        return db.query(
            Telemetry
        ).filter(
            Telemetry.device_id == device_id
        ).all()

    def get_latest_by_device(
        self,
        db: Session,
        device_id: int
    ):
        return (
            db.query(Telemetry)
            .filter(
                Telemetry.device_id == device_id
            )
            .order_by(
                Telemetry.created_at.desc()
            )
            .first()
        )

    def delete(
        self,
        db: Session,
        telemetry
    ):
        db.delete(
            telemetry
        )

        db.commit()