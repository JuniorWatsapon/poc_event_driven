from locust import HttpUser, task, between
import random

class EventApiUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def send_signup_event(self):
        payload = {
            "event_type": "user.signup",
            "user_id": random.randint(1, 10000),
            "metadata": {
                "platform": random.choice(["web", "mobile", "tablet"]),
                "plan": random.choice(["free", "premium", "enterprise"])
            }
        }
        self.client.post("/events", json=payload)
