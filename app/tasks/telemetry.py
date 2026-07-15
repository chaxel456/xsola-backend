from datetime import datetime, timedelta

from app.core.database import SessionLocal

from app.modules.devices.model import Device


OFFLINE_MINUTES = 10


def check_offline_devices():

    db = SessionLocal()

    try:

        devices = db.query(Device).all()

        for device in devices:

            if (
                device.last_seen
                and device.last_seen <
                datetime.utcnow() -
                timedelta(minutes=OFFLINE_MINUTES)
            ):

                device.status = "offline"

                print(
                    f"Device Offline: {device.id}"
                )

        db.commit()

    finally:

        db.close()