import json
import asyncio
import paho.mqtt.client as mqtt

from app.core.config import settings
from app.core.database import SessionLocal

from app.modules.telemetry.service import (
    TelemetryService
)

from app.modules.telemetry.schema import (
    TelemetryCreate
)

from app.websocket.telemetry_ws import (
    manager
)


class MQTTService:

    telemetry_service = TelemetryService()

    def __init__(self):
        self.client = mqtt.Client()

        if (
            settings.MQTT_USERNAME
            and settings.MQTT_PASSWORD
        ):
            self.client.username_pw_set(
                settings.MQTT_USERNAME,
                settings.MQTT_PASSWORD
            )

    # ===========================
    # ADDED: Receive MQTT messages
    # ===========================
    def on_message(
        self,
        client,
        userdata,
        message
    ):
        try:

            payload = json.loads(
                message.payload.decode()
            )

            db = SessionLocal()

            telemetry = TelemetryCreate(
                **payload
            )

            self.telemetry_service.create_telemetry(
                db,
                telemetry
            )

            asyncio.run(
                manager.send_message(
                    payload
                )
            )

            print(
                f"Telemetry Saved: {payload}"
            )

            db.close()

        except Exception as e:

            print(
                f"MQTT Error: {e}"
            )

    def connect(self):

        self.client.connect(
            settings.MQTT_BROKER,
            settings.MQTT_PORT,
            settings.MQTT_KEEPALIVE
        )

        # ===========================
        # ADDED
        # ===========================
        self.client.on_message = self.on_message

        # Subscribe to telemetry topics
        self.client.subscribe(
            "xsola/device/+/telemetry"
        )

        self.client.loop_start()

        print("MQTT Connected")

    def disconnect(self):

        self.client.loop_stop()

        self.client.disconnect()

        print("MQTT Disconnected")

    def publish(
        self,
        topic: str,
        payload: dict
    ):

        self.client.publish(
            topic,
            json.dumps(payload)
        )

        print(
            f"Published to {topic}: {payload}"
        )

    def subscribe(
        self,
        topic: str
    ):

        self.client.subscribe(topic)

        print(
            f"Subscribed to {topic}"
        )