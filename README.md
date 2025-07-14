+------------------+             +------------------+  
|                  |             |                  |  
|    Producers     |             |  Consumer App    |  
| (event-api etc.) |             |   (consumer-app) |  
|                  |             |                  |  
+--------+---------+             +---------+--------+  
         |                                  ^  
         | Produces events                  | Consumes events  
         v                                  |  
+------------------+                        |  
|                  |     Kafka Cluster      |  
|    Kafka Brokers +------------------------+  
|  (kafka1,kafka2, |     (Brokered messaging)  
|   kafka3)        |                        |  
|                  |                        |  
+---+---+---+------+                        |  
    |   |   |                               |  
    |   |   |                               |  
    |   |   |                               |  
    v   v   v                               |  
+------+-----+--------+                    |  
|   Zookeeper (coordination)               |  
+-----------------------------------------+  
  
Monitoring Stack:  
+----------------+        +----------------+       +----------------+  
| Prometheus     | <----> | Kafka JMX       |       | Grafana        |  
| (scrapes       |        | Exporter on     |       | (dashboard)    |  
|  kafka &       |        | kafka brokers)  |       |                |  
|  consumer)     |        +----------------+       +----------------+  
  
+----------------+  
| APM Server     |  
| (Elastic APM)  |  
+----------------+  
  
+----------------+  
| Elasticsearch  |  
| & Kibana       |  
+----------------+  
  
