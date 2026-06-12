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