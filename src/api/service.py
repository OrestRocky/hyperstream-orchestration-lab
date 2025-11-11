from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="HyperStream API", version="0.1.0")

class Alert(BaseModel):
    sensor_id: str
    ts: int
    severity: float
    label: Optional[str] = None
    details: dict = {}

class AlertBatch(BaseModel):
    alerts: List[Alert]

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs", "health": "/health"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/alerts/ingest")
def ingest_alerts(batch: AlertBatch):
    return {"received": len(batch.alerts)}
