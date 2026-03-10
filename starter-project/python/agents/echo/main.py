# starter-project/python/agents/echo/main.py
# ============================================================
# Echo Agent
# ============================================================
# The simplest possible Specialist Agent — it echoes the input
# back to the caller with a prefix.
#
# Purpose in the course:
#   Modules 00–03 use the Echo Agent as the teaching vehicle.
#   It's intentionally trivial so learners focus entirely on
#   GitHub concepts (commits, branches, PRs) rather than the
#   agent logic itself.
#
# Run this service:
#   python agents/echo/main.py
#
# Test it:
#   curl -X POST http://localhost:8001/run \
#     -H "Content-Type: application/json" \
#     -d '{"task": "echo", "input": "Is this working?"}'
# ============================================================

from __future__ import annotations

import logging
import os
import sys

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from models import AgentRequest, AgentResponse, HealthResponse

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("agent.echo")

app = FastAPI(
    title="Echo Agent",
    description="Echoes input back to the caller. Used in Modules 00–03.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENT_NAME = "echo"


@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health() -> HealthResponse:
    return HealthResponse(service=AGENT_NAME)


@app.post("/run", response_model=AgentResponse, tags=["Agent"])
async def run(request: AgentRequest) -> AgentResponse:
    """
    Echo the input back with a prefix.

    This is intentionally the simplest possible agent implementation.
    It demonstrates the A2A request/response contract without any
    external dependencies or complex logic.
    """
    log.info("Received input=%r request_id=%s", request.input[:50], request.request_id)

    output = f"Echo: {request.input}"

    log.info("Returning output=%r", output)
    return AgentResponse.success(
        agent=AGENT_NAME,
        output=output,
        request_id=request.request_id,
    )


if __name__ == "__main__":
    port = int(os.getenv("ECHO_AGENT_PORT", "8001"))
    log.info("Starting Echo Agent on port %d", port)
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
