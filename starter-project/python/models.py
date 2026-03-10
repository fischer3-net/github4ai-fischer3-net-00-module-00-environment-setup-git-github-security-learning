# starter-project/python/models.py
# ============================================================
# Shared Pydantic Models
# ============================================================
# These Pydantic models are the Python implementation of the
# JSON schema defined in starter-project/schema/a2a-message.schema.json.
#
# Both the Orchestrator and all Specialist Agents import from
# this module, ensuring a single source of truth for the A2A
# message format. If the schema changes, all agents are updated
# by changing this one file.
# ============================================================

from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class AgentStatus(str, Enum):
    """Possible outcomes of an agent processing a request."""
    SUCCESS = "success"
    ERROR = "error"


class AgentRequest(BaseModel):
    """
    Sent by the Orchestrator to a Specialist Agent's /run endpoint.

    Example:
        {
            "task": "echo",
            "input": "Is this working?",
            "request_id": "550e8400-e29b-4d8d-a456-426614174000"
        }
    """
    task: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Intent keyword used by the Orchestrator for routing.",
        examples=["echo", "search", "calculate"],
    )
    input: str = Field(
        ...,
        min_length=1,
        max_length=4096,
        description="The user's input or query to be processed by the agent.",
    )
    context: dict[str, Any] | None = Field(
        default=None,
        description="Optional metadata from the Orchestrator.",
    )
    request_id: UUID | None = Field(
        default=None,
        description="Optional UUID for tracing a request through the system.",
    )


class AgentResponse(BaseModel):
    """
    Returned by a Specialist Agent after processing a request.

    Example (success):
        {
            "agent": "echo",
            "status": "success",
            "output": "Echo: Is this working?"
        }

    Example (error):
        {
            "agent": "echo",
            "status": "error",
            "output": "",
            "error": "Something went wrong."
        }
    """
    agent: str = Field(
        ...,
        description="The name of the agent that handled the request.",
    )
    status: AgentStatus = Field(
        ...,
        description="Whether the agent successfully handled the request.",
    )
    output: str = Field(
        ...,
        description="The agent's response. Empty string on error.",
    )
    error: str | None = Field(
        default=None,
        description="Error message. Present only when status is 'error'.",
    )
    request_id: UUID | None = Field(
        default=None,
        description="Echo of the request_id from the incoming request.",
    )
    metadata: dict[str, Any] | None = Field(
        default=None,
        description="Optional metadata from the agent.",
    )

    @classmethod
    def success(
        cls,
        agent: str,
        output: str,
        request_id: UUID | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> AgentResponse:
        """Convenience constructor for successful responses."""
        return cls(
            agent=agent,
            status=AgentStatus.SUCCESS,
            output=output,
            request_id=request_id,
            metadata=metadata,
        )

    @classmethod
    def error(
        cls,
        agent: str,
        error_message: str,
        request_id: UUID | None = None,
    ) -> AgentResponse:
        """Convenience constructor for error responses."""
        return cls(
            agent=agent,
            status=AgentStatus.ERROR,
            output="",
            error=error_message,
            request_id=request_id,
        )


class HealthResponse(BaseModel):
    """Returned by the /health endpoint of every service."""
    status: str = "ok"
    service: str
    version: str = "1.0.0"
