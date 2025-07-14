from confluent_kafka import Producer
import os

KAFKA_CONFIG = {
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka1:19092,kafka2:19093,kafka3:19094"),
}

producer = Producer(KAFKA_CONFIG)

def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")

