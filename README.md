# ⚡ Event-Driven Architecture POC with Kafka, Prometheus, and APM

This repository demonstrates a **Proof of Concept (PoC)** for an **event-driven microservice architecture** using Apache Kafka for messaging, Prometheus + Grafana for metrics, and Elastic APM + Kibana for observability.

---

## 📦 Stack Overview

| Component         | Purpose                                   |
|------------------|-------------------------------------------|
| `event-api`       | REST API that produces Kafka messages     |
| `consumer-app`    | Consumes Kafka messages and logs output   |
| `Kafka Cluster`   | 3-broker cluster via Confluent Kafka      |
| `Zookeeper`       | Coordinates Kafka brokers                 |
| `Kafka UI`        | Web-based Kafka topic/browser UI          |
| `Prometheus`      | Metrics collection for Kafka & services   |
| `Grafana`         | Visualization dashboard for Prometheus    |
| `APM Server`      | Elastic APM server for tracing            |
| `Kibana`          | Observability frontend for APM + logs     |
| `Elasticsearch`   | Storage engine for APM data               |

---

## 🚀 Quick Start

> Prerequisites:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Clone the repo

```bash
git clone https://github.com/JuniorWatsapon/poc_event_driven.git
cd poc_event_driven
```
###  Start the environment
```bash
docker-compose up --build
```

## 📡 API Usage
Produce a message
Send a POST request to event-api to simulate an event.
```bash
curl -X POST http://localhost:9000/events \
     -H 'Content-Type: application/json' \
     -d '{
           "event_type": "user.signup",
           "user_id": 321,
           "metadata": { "platform": "web", "plan": "premium" }
         }'
  ```       
The event-api will produce a Kafka message.
The consumer-app will consume and print it to console.

## 🔍 Monitoring & Observability
#🔧 Prometheus & Grafana
- Prometheus UI: http://localhost:9090
- Grafana Dashboard: http://localhost:3000

#### 📈 Kafka UI
Access Kafka topics: http://localhost:8080

#### 🧠 APM & Kibana
APM Server: http://localhost:8200
Kibana UI: http://localhost:5601

Navigate to APM for traces and errors

### 🛠️ Services Breakdown
#### 🧩 event-api
REST API written in (your language here)

On request, it publishes messages to Kafka

#### 🧾 consumer-app
Kafka consumer

Reads messages and logs them

Exposes Prometheus metrics at http://localhost:9003/metrics

#### 🧪 Kafka Cluster
3 brokers for replication and testing distributed events

Internal ports (19092, 19093, 19094) used for inter-broker communication

External ports (9092, 9093, 9094) used for clients

#### 📊 Monitoring
Prometheus scrapes JMX metrics from all Kafka brokers

Kafka brokers expose metrics via JMX Exporter (port 9404)

consumer-app exposes business metrics to Prometheus

#### 🎯 Tracing & APM
Elastic APM is connected to:

REST API requests

Kafka message consumption (if instrumented)

Kibana gives full visibility into events and request tracing
