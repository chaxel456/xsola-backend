from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class TelemetryCreate(BaseModel):
    device_id: str

    temperature: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None
    power: Optional[float] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    raw_data: Optional[Dict] = None


class TelemetryResponse(TelemetryCreate):
    id: str
    timestamp: datetime

    class Config:
        from_attributes = True