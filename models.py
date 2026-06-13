from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MeterData(Base):
    __tablename__ = "meter_data"

    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(String, nullable=False)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
