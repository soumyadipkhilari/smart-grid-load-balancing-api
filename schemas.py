from pydantic import BaseModel


class MeterReading(BaseModel):
    meter_id: str
    voltage: float
    current: float
