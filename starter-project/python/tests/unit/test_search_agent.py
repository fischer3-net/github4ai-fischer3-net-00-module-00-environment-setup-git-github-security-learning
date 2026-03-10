# starter-project/python/tests/unit/test_search_agent.py
# ============================================================
# Unit Tests — Search Agent
# ============================================================

import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agents.search.main import app, mock_search
from models import AgentStatus

client = TestClient(app)


class TestMockSearch:
    """Unit tests for the mock_search function in isolation."""

    def test_finds_pull_request_result(self):
        result = mock_search("What is a pull request?")
        assert "pull request" in result.lower()
        assert len(result) > 20

    def test_finds_github_actions_result(self):
        result = mock_search("tell me about github actions")
        assert "GitHub Actions" in result or "github actions" in result.lower()

    def test_finds_gitignore_result(self):
        result = mock_search("how does gitignore work?")
        assert ".gitignore" in result

    def test_returns_default_for_unknown_query(self):
        result = mock_search("what is the meaning of life")
        assert "No results found" in result

    def test_case_insensitive_matching(self):
        lower = mock_search("pull request")
        upper = mock_search("PULL REQUEST")
        assert lower == upper


class TestHealthEndpoint:
    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_correct_service(self):
        data = client.get("/health").json()
        assert data["service"] == "search"


class TestRunEndpoint:
    def test_search_returns_200(self):
        response = client.post(
            "/run",
            json={"task": "search", "input": "What is a pull request?"},
        )
        assert response.status_code == 200

    def test_search_returns_success_status(self):
        response = client.post(
            "/run",
            json={"task": "search", "input": "What is a pull request?"},
        )
        data = response.json()
        assert data["status"] == AgentStatus.SUCCESS

    def test_search_identifies_itself(self):
        response = client.post(
            "/run",
            json={"task": "search", "input": "test query"},
        )
        data = response.json()
        assert data["agent"] == "search"

    def test_search_returns_metadata(self):
        response = client.post(
            "/run",
            json={"task": "search", "input": "github actions"},
        )
        data = response.json()
        assert data["metadata"] is not None
        assert data["metadata"]["mock"] is True

    def test_search_preserves_request_id(self):
        request_id = "550e8400-e29b-4d8d-a456-426614174000"
        response = client.post(
            "/run",
            json={
                "task": "search",
                "input": "test",
                "request_id": request_id,
            },
        )
        data = response.json()
        assert data["request_id"] == request_id

    def test_search_rejects_empty_input(self):
        response = client.post(
            "/run",
            json={"task": "search", "input": ""},
        )
        assert response.status_code == 422
