# starter-project/python/tests/unit/test_echo_agent.py
# ============================================================
# Unit Tests — Echo Agent
# ============================================================
# These tests verify the Echo Agent's behavior in isolation,
# without starting a server or making real HTTP calls.
#
# Run:
#   pytest tests/unit/test_echo_agent.py -v
# ============================================================

import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agents.echo.main import app
from models import AgentStatus

client = TestClient(app)


class TestHealthEndpoint:
    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_correct_service(self):
        response = client.get("/health")
        data = response.json()
        assert data["service"] == "echo"
        assert data["status"] == "ok"


class TestRunEndpoint:
    def test_echo_returns_200(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "hello world"},
        )
        assert response.status_code == 200

    def test_echo_prefixes_output(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "Is this working?"},
        )
        data = response.json()
        assert data["output"] == "Echo: Is this working?"

    def test_echo_returns_success_status(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "test"},
        )
        data = response.json()
        assert data["status"] == AgentStatus.SUCCESS

    def test_echo_identifies_itself_as_echo_agent(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "test"},
        )
        data = response.json()
        assert data["agent"] == "echo"

    def test_echo_preserves_request_id(self):
        request_id = "550e8400-e29b-4d8d-a456-426614174000"
        response = client.post(
            "/run",
            json={"task": "echo", "input": "test", "request_id": request_id},
        )
        data = response.json()
        assert data["request_id"] == request_id

    def test_echo_works_without_request_id(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": "no id here"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["request_id"] is None

    def test_echo_handles_special_characters(self):
        special_input = "Hello! @#$% & <world>"
        response = client.post(
            "/run",
            json={"task": "echo", "input": special_input},
        )
        data = response.json()
        assert data["output"] == f"Echo: {special_input}"

    def test_echo_rejects_empty_input(self):
        response = client.post(
            "/run",
            json={"task": "echo", "input": ""},
        )
        # Pydantic min_length=1 validation should reject empty input
        assert response.status_code == 422

    def test_echo_rejects_missing_task(self):
        response = client.post(
            "/run",
            json={"input": "missing task field"},
        )
        assert response.status_code == 422

    def test_echo_rejects_missing_input(self):
        response = client.post(
            "/run",
            json={"task": "echo"},
        )
        assert response.status_code == 422
