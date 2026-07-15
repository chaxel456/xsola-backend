from datetime import datetime

from pydantic import BaseModel


class TelemetryCreate(BaseModel):
    device_id: int
    voltage: float
    current: float
    power: float
    battery: float
    temperature: float | None = None
    status: str = "online"


class TelemetryResponse(BaseModel):
    id: int
    device_id: int
    voltage: float
    current: float
    power: float
    battery: float
    temperature: float | None = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class TelemetryUpdate(BaseModel):
    voltage: float | None = None
    current: float | None = None
    power: float | None = None
    battery: float | None = None
    temperature: float | None = None
    status: str | None = None