from fastapi import FastAPI
import asyncio
from app.consumers.user_event_consumer import consume_user_events
from prometheus_client import generate_latest
from starlette.responses import Response
from contextlib import asynccontextmanager



consumer_task = None  # global for managing the background task

@asynccontextmanager
async def lifespan(app: FastAPI):
    global consumer_task
    # Startup logic
    consumer_task = asyncio.create_task(consume_user_events())
    yield  # App is now running
    # Shutdown logic
    if consumer_task:
        consumer_task.cancel()
        try:
            await consumer_task
        except asyncio.CancelledError:
            print("🛑 Kafka consumer task cancelled.")

# Attach lifespan to FastAPI app
app = FastAPI(lifespan=lifespan)

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
