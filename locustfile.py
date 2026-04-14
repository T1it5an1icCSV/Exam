"""Минимальный сценарий нагрузки для учебного задания (GitLab CI + Locust headless)."""
from locust import HttpUser, between, task


class HttpbinUser(HttpUser):
    """Виртуальные пользователи ходят на публичный httpbin.org (доступен из CI)."""

    wait_time = between(0.5, 1.5)
    host = "https://httpbin.org"

    @task
    def get_json(self) -> None:
        self.client.get("/get", name="/get")
