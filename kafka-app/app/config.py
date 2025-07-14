import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka1:19092,kafka2:19093,kafka3:19094")
TOPIC_NAME = "user-events"