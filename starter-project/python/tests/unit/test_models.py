# starter-project/python/tests/unit/test_models.py
# ============================================================
# Unit Tests — Shared Pydantic Models
# ============================================================

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from models import AgentRequest, AgentResponse, AgentStatus
import pytest
from uuid import UUID


class TestAgentRequest:
    def test_valid_minimal_request(self):
        req = AgentRequest(task="echo", input="hello")
        assert req.task == "echo"
        assert req.input == "hello"
        assert req.request_id is None
        assert req.context is None

    def test_valid_full_request(self):
        req = AgentRequest(
            task="search",
            input="what is git?",
            context={"source": "test"},
            request_id="550e8400-e29b-4d8d-a456-426614174000",
        )
        assert isinstance(req.request_id, UUID)

    def test_rejects_empty_task(self):
        with pytest.raises(Exception):
            AgentRequest(task="", input="hello")

    def test_rejects_empty_input(self):
        with pytest.raises(Exception):
            AgentRequest(task="echo", input="")

    def test_rejects_task_over_100_chars(self):
        with pytest.raises(Exception):
            AgentRequest(task="x" * 101, input="hello")


class TestAgentResponse:
    def test_success_factory(self):
        resp = AgentResponse.success(agent="echo", output="Echo: hello")
        assert resp.status == AgentStatus.SUCCESS
        assert resp.output == "Echo: hello"
        assert resp.error is None

    def test_error_factory(self):
        resp = AgentResponse.error(agent="echo", error_message="Something failed")
        assert resp.status == AgentStatus.ERROR
        assert resp.output == ""
        assert resp.error == "Something failed"

    def test_success_with_request_id(self):
        uid = UUID("550e8400-e29b-4d8d-a456-426614174000")
        resp = AgentResponse.success(agent="echo", output="hi", request_id=uid)
        assert resp.request_id == uid
