# starter-project/python/agents/search/main.py
# ============================================================
# Search Agent
# ============================================================
# A Specialist Agent that simulates a web search capability.
#
# Purpose in the course:
#   This agent is added to the project in Module 02 via a
#   feature branch (feature/specialist-agent-search). Learners
#   create the branch, write this file, register the agent in
#   the Orchestrator's registry, and open a PR.
#
# Implementation note:
#   This is a mock implementation — it returns realistic-looking
#   search results without actually calling a search API. This
#   keeps Module 02 focused on branching/merging rather than
#   API integration. A real search integration is a good
#   Capstone extension.
#
# Run this service:
#   python agents/search/main.py
#
# Test it:
#   curl -X POST http://localhost:8002/run \
#     -H "Content-Type: application/json" \
#     -d '{"task": "search", "input": "What is a GitHub pull request?"}'
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
log = logging.getLogger("agent.search")

app = FastAPI(
    title="Search Agent",
    description="Simulates a web search. Added to the project in Module 02.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENT_NAME = "search"

# ── Mock Search Results ────────────────────────────────────
# A small lookup table for the teaching context.
# Extend this in the Capstone or replace with a real search API.
MOCK_RESULTS: dict[str, str] = {
    "pull request": (
        "A pull request (PR) is a GitHub feature that lets you propose changes "
        "to a repository. When you open a PR, you're asking the repository "
        "maintainers to review and merge your branch into the target branch."
    ),
    "git branch": (
        "A Git branch is a lightweight, movable pointer to a commit. Branches "
        "let you work on features or fixes in isolation without affecting the "
        "main codebase. Create a branch with: git checkout -b branch-name"
    ),
    "github actions": (
        "GitHub Actions is a CI/CD platform built into GitHub. You define "
        "automated workflows in YAML files stored in .github/workflows/. "
        "Workflows can trigger on push, pull_request, schedule, and more."
    ),
    "codespace": (
        "A GitHub Codespace is a cloud-hosted development environment powered "
        "by VS Code. It's configured by a .devcontainer/devcontainer.json file "
        "in your repository and starts in about 60 seconds."
    ),
    "gitignore": (
        "A .gitignore file tells Git which files to never track. Any file "
        "matching a pattern in .gitignore will never appear in git status "
        "and cannot be accidentally committed."
    ),
}


def mock_search(query: str) -> str:
    """
    Return a mock search result for the given query.

    Matches the query against known keywords (case-insensitive).
    Returns a default response if no match is found.
    """
    query_lower = query.lower()
    for keyword, result in MOCK_RESULTS.items():
        if keyword in query_lower:
            return result

    # Default response when no match found
    return (
        f"No results found for '{query}'. "
        "Try searching for: pull request, git branch, github actions, "
        "codespace, or gitignore."
    )


@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health() -> HealthResponse:
    return HealthResponse(service=AGENT_NAME)


@app.post("/run", response_model=AgentResponse, tags=["Agent"])
async def run(request: AgentRequest) -> AgentResponse:
    """
    Perform a mock search and return results.

    In a real implementation, this would call a search API
    (Brave Search, SerpAPI, Tavily, etc.). The mock implementation
    keeps Module 02 focused on Git branching concepts.
    """
    log.info(
        "Received search query=%r request_id=%s",
        request.input[:80],
        request.request_id,
    )

    result = mock_search(request.input)

    log.info("Returning result for query=%r", request.input[:40])
    return AgentResponse.success(
        agent=AGENT_NAME,
        output=result,
        request_id=request.request_id,
        metadata={"mock": True, "query": request.input},
    )


if __name__ == "__main__":
    port = int(os.getenv("SEARCH_AGENT_PORT", "8002"))
    log.info("Starting Search Agent on port %d", port)
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
