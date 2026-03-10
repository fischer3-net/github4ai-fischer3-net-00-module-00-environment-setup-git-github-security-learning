# starter-project/python/orchestrator/main.py
# ============================================================
# Orchestrator Agent
# ============================================================
# The Orchestrator is the entry point for the A2A system.
# It receives task requests, determines which Specialist Agent
# should handle them based on the task keyword, forwards the
# request, and returns the response.
#
# Architecture:
#   Client → Orchestrator (/run) → Specialist Agent (/run) → Client
#
# Routing strategy: keyword-based. The `task` field in the
# request is matched against the agent registry below.
# More sophisticated routing (intent classification, LLM-based
# routing) is left for learners to explore as capstone work.
#
# Run this service:
#   python orchestrator/main.py
#
# Endpoints:
#   GET  /health      → health check
#   GET  /agents      → list registered agents
#   POST /run         → route a task to the appropriate agent
# ============================================================

from __future__ import annotations

import logging
import os

import httpx
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import shared models — same schema used by all agents
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models import AgentRequest, AgentResponse, AgentStatus, HealthResponse

load_dotenv()

# ── Logging ───────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("orchestrator")

# ── App ───────────────────────────────────────────────────
app = FastAPI(
    title="A2A Orchestrator",
    description="Routes task requests to the appropriate Specialist Agent.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Permissive for local dev — restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Agent Registry ────────────────────────────────────────
# Maps task keywords → agent base URLs.
# The Orchestrator appends /run to the URL before forwarding.
#
# MODULE 02 NOTE: When learners add the Search Agent in Module 02,
# they register it here. The SEARCH_AGENT_URL comes from .env.
AGENT_REGISTRY: dict[str, str] = {
    "echo": os.getenv("ECHO_AGENT_URL", "http://localhost:8001"),
    "search": os.getenv("SEARCH_AGENT_URL", "http://localhost:8002"),
}

# ── Routes ────────────────────────────────────────────────

@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health() -> HealthResponse:
    """Health check — used by the CI nightly integration tests."""
    return HealthResponse(service="orchestrator")


@app.get("/agents", tags=["System"])
async def list_agents() -> dict:
    """List all registered agents and their URLs."""
    return {
        "agents": [
            {"task": task, "url": url}
            for task, url in AGENT_REGISTRY.items()
        ]
    }


@app.post("/run", response_model=AgentResponse, tags=["Routing"])
async def run(request: AgentRequest) -> AgentResponse:
    """
    Route a task request to the appropriate Specialist Agent.

    The Orchestrator looks up the `task` field in the agent registry
    and forwards the full request to that agent's /run endpoint.

    Returns the agent's response directly.
    """
    log.info(
        "Received task=%r input=%r request_id=%s",
        request.task,
        request.input[:50],   # Truncate for log safety
        request.request_id,
    )

    # ── Routing ───────────────────────────────────────────
    agent_url = AGENT_REGISTRY.get(request.task)
    if not agent_url:
        log.warning("No agent registered for task=%r", request.task)
        raise HTTPException(
            status_code=404,
            detail=(
                f"No agent registered for task '{request.task}'. "
                f"Available tasks: {list(AGENT_REGISTRY.keys())}"
            ),
        )

    # ── Forward to Agent ──────────────────────────────────
    endpoint = f"{agent_url}/run"
    log.info("Routing task=%r to %s", request.task, endpoint)

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                endpoint,
                json=request.model_dump(mode="json", exclude_none=True),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            return AgentResponse.model_validate(response.json())

    except httpx.ConnectError:
        log.error("Could not connect to agent at %s", endpoint)
        return AgentResponse.error(
            agent=request.task,
            error_message=f"Agent '{request.task}' is not reachable at {agent_url}. Is it running?",
            request_id=request.request_id,
        )
    except httpx.TimeoutException:
        log.error("Timeout waiting for agent at %s", endpoint)
        return AgentResponse.error(
            agent=request.task,
            error_message=f"Agent '{request.task}' timed out after 30 seconds.",
            request_id=request.request_id,
        )
    except httpx.HTTPStatusError as e:
        log.error("Agent returned HTTP %d: %s", e.response.status_code, e.response.text)
        return AgentResponse.error(
            agent=request.task,
            error_message=f"Agent returned error {e.response.status_code}.",
            request_id=request.request_id,
        )


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.getenv("ORCHESTRATOR_PORT", "8000"))
    log.info("Starting Orchestrator on port %d", port)
    log.info("Registered agents: %s", list(AGENT_REGISTRY.keys()))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
