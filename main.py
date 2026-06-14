
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
from database import SessionLocal
from models import MeterData

@app.get("/load-status")
def load_status():

    db = SessionLocal()

    meter = db.query(MeterData).order_by(MeterData.id.desc()).first()

    if not meter:
        return {"message": "No meter data found"}

    load = meter.voltage * meter.current

    status = "High Load" if load > 1000 else "Normal Load"

    return {
        "meter_id": meter.meter_id,
        "voltage": meter.voltage,
        "current": meter.current,
        "load": load,
        "status": status
    }
@app.get("/recommendation")
def recommendation():

    db = SessionLocal()

    meter = db.query(MeterData).order_by(MeterData.id.desc()).first()

    if not meter:
        return {"message": "No data found"}

    load = meter.voltage * meter.current

    if load > 1500:
        recommendation = "Shift load to another feeder"
    elif load > 1000:
        recommendation = "Monitor load closely"
    else:
        recommendation = "Load is normal"

    return {
        "meter_id": meter.meter_id,
        "load": load,
        "recommendation": recommendation
    }
@app.get("/dashboard")
def dashboard():

    db = SessionLocal()

    total_meters = db.query(MeterData).count()

    latest_meter = db.query(MeterData).order_by(MeterData.id.desc()).first()

    if not latest_meter:
        return {"message": "No data available"}

    load = latest_meter.voltage * latest_meter.current

    return {
        "total_meters": total_meters,
        "latest_meter": latest_meter.meter_id,
        "current_load": load,
        "status": "High Load" if load > 1000 else "Normal Load"
    }
@app.get("/alert")
def alert():

    db = SessionLocal()

    meter = db.query(MeterData).order_by(MeterData.id.desc()).first()

    if not meter:
        return {"message": "No data available"}

    load = meter.voltage * meter.current

    if load > 1500:
        alert = "CRITICAL"
    elif load > 1000:
        alert = "WARNING"
    else:
        alert = "NORMAL"

    return {
        "meter_id": meter.meter_id,
        "load": load,
        "alert_level": alert
    }