
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas import MeterReading
from database import get_db
from models import MeterData

app = FastAPI()
from fastapi import FastAPI
from schemas import MeterReading

app = FastAPI()
from fastapi import FastAPI

app = FastAPI(
    title="Smart Grid Load Balancing API",
    description="Smart Meter Data Ingestion API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Smart Grid API Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

from fastapi import FastAPI

app = FastAPI(
    title="Smart Grid Load Balancing API",
    description="Smart Meter Data Ingestion API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Smart Grid API Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
@app.post("/meter-data")
def meter_data(data: MeterReading, db: Session = Depends(get_db)):

    reading = MeterData(
        meter_id=data.meter_id,
        voltage=data.voltage,
        current=data.current
    )

    db.add(reading)
    db.commit()
    db.refresh(reading)

    power = data.voltage * data.current

    return {
        "id": reading.id,
        "meter_id": data.meter_id,
        "power": power,
        "message": "Data saved successfully"
    }
@app.get("/meter-data")
def get_meter_data(db: Session = Depends(get_db)):
    
    readings = db.query(MeterData).all()

    result = []

    for reading in readings:
        result.append({
            "id": reading.id,
            "meter_id": reading.meter_id,
            "voltage": reading.voltage,
            "current": reading.current
        })

    return result
@app.get("/load-status")
def load_status():
    return {
        "status": "Normal",
        "message": "Load Balancing API Working"
    }