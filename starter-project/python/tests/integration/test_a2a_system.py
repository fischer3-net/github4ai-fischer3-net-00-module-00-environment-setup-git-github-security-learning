# starter-project/python/tests/integration/test_a2a_system.py
# ============================================================
# Integration Tests — Full A2A System
# ============================================================
# These tests hit the RUNNING Orchestrator over HTTP.
# They require all services to be started before running.
#
# The nightly CI workflow (nightly.yml) starts all services
# before running these tests. To run locally:
#
#   # Terminal 1
#   python agents/echo/main.py
#
#   # Terminal 2
#   python agents/search/main.py
#
#   # Terminal 3
#   python orchestrator/main.py
#
#   # Terminal 4
#   ORCHESTRATOR_URL=http://localhost:8000 pytest tests/integration/ -v
# ============================================================

import os
import pytest
import httpx

# The Orchestrator URL is set by the nightly.yml workflow.
# Defaults to localhost for local development.
ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "http://localhost:8000")


@pytest.fixture(scope="module")
def client():
    """HTTP client for the Orchestrator."""
    with httpx.Client(base_url=ORCHESTRATOR_URL, timeout=10.0) as c:
        yield c


class TestOrchestratorHealth:
    def test_orchestrator_is_running(self, client):
        response = client.get("/health")
        assert response.status_code == 200

    def test_orchestrator_lists_agents(self, client):
        response = client.get("/agents")
        assert response.status_code == 200
        data = response.json()
        tasks = [a["task"] for a in data["agents"]]
        assert "echo" in tasks
        assert "search" in tasks


class TestEchoRouting:
    def test_orchestrator_routes_echo_task(self, client):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "integration test"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["output"] == "Echo: integration test"
        assert data["agent"] == "echo"

    def test_echo_routing_preserves_request_id(self, client):
        request_id = "550e8400-e29b-4d8d-a456-426614174099"
        response = client.post(
            "/run",
            json={
                "task": "echo",
                "input": "with id",
                "request_id": request_id,
            },
        )
        data = response.json()
        assert data["request_id"] == request_id


class TestSearchRouting:
    def test_orchestrator_routes_search_task(self, client):
        response = client.post(
            "/run",
            json={"task": "search", "input": "What is a pull request?"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["agent"] == "search"
        assert len(data["output"]) > 0


class TestErrorHandling:
    def test_unknown_task_returns_404(self, client):
        response = client.post(
            "/run",
            json={"task": "nonexistent-agent", "input": "test"},
        )
        assert response.status_code == 404

    def test_invalid_request_returns_422(self, client):
        response = client.post("/run", json={"task": "echo"})
        assert response.status_code == 422
