from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import Response
from kafka_config import producer, delivery_report
from prometheus_client import start_http_server, Counter, generate_latest
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
import json
import threading

app = FastAPI()

# ✅ Elastic APM config
apm_config = {
    "SERVICE_NAME": "event-api",
    "SERVER_URL": "http://apm-server:8200",
    "ENVIRONMENT": "dev",
    "DEBUG": True,
    "CAPTURE_BODY": "all",
}
apm = make_apm_client(apm_config)
app.add_middleware(ElasticAPM, client=apm)

# 🔢 Prometheus metrics
events_published = Counter("events_published_total", "Total number of events published to Kafka")

# 📈 Start Prometheus metrics server
def start_metrics_server():
    start_http_server(9001)

threading.Thread(target=start_metrics_server, daemon=True).start()

# 📦 Payload schema
class EventPayload(BaseModel):
    event_type: str
    user_id: int
    metadata: dict

@app.post("/events")
def publish_event(payload: EventPayload):
    try:
        producer.produce(
            topic="user-events",
            key=str(payload.user_id),
            value=json.dumps(payload.dict()),
            callback=delivery_report
        )
        producer.flush()
        events_published.inc()
        return {"message": "Event published to Kafka"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
