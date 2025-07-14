import json
from aiokafka import AIOKafkaConsumer
import asyncio
import datetime
from aiokafka.errors import KafkaError
from app.config import TOPIC_NAME, KAFKA_BOOTSTRAP_SERVERS

async def consume_user_events():
    consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="user-event-consumers",
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )

    try:
        await consumer.start()
        print(f"📥 [{datetime.datetime.now()}] Started listening to {TOPIC_NAME}")

        async for msg in consumer:
            try:
                event = json.loads(msg.value.decode("utf-8"))
                print(f"📥 [{datetime.datetime.now()}] UserEvent: {event}")
            except Exception as e:
                print("❌ Error processing message:", e)

    except asyncio.CancelledError:
        print("🛑 Kafka consumer cancelled.")
        raise  # let FastAPI shutdown handle it
    except KafkaError as e:
        print(f"❌ Kafka error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        print("✅ Stopping Kafka consumer...")
        await consumer.stop()
