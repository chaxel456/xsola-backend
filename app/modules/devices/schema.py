from pydantic import BaseModel
from datetime import datetime


class DeviceCreate(BaseModel):
    customer_id: int
    serial_number: str
    device_type: str


class DeviceResponse(BaseModel):
    id: int
    customer_id: int
    serial_number: str
    device_type: str
    status: str

    class Config:
        from_attributes = True