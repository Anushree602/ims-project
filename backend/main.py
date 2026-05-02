
from fastapi import FastAPI, HTTPException
import time

app = FastAPI()

signals = []
work_items = {}
rca_store = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest")
def ingest(signal: dict):
    component = signal.get("component_id")
    now = time.time()

    # Debounce logic (simple)
    if component in work_items:
        work_items[component]["signals"].append(signal)
    else:
        work_items[component] = {
            "status": "OPEN",
            "start_time": now,
            "signals": [signal]
        }

    signals.append(signal)
    return {"message": "Signal received"}

@app.get("/incidents")
def get_incidents():
    return work_items

@app.post("/rca/{component}")
def add_rca(component: str, rca: dict):
    if component not in work_items:
        raise HTTPException(status_code=404, detail="Not found")

    rca_store[component] = rca
    work_items[component]["end_time"] = time.time()
    work_items[component]["status"] = "CLOSED"

    mttr = work_items[component]["end_time"] - work_items[component]["start_time"]
    work_items[component]["mttr"] = mttr

    return {"message": "Closed with RCA", "mttr": mttr}
