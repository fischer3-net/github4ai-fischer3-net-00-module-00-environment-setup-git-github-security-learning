// starter-project/nodejs/orchestrator/index.js
// ============================================================
// Orchestrator Agent — Node.js variant
// ============================================================
// Mirrors the Python orchestrator/main.py in behaviour.
// Routes task requests to registered Specialist Agents.
//
// Run: node orchestrator/index.js
// ============================================================

import 'dotenv/config';
import express from 'express';
import { validateRequest, errorResponse } from '../models.js';

const app = express();
app.use(express.json());

const ORCHESTRATOR_PORT = parseInt(process.env.ORCHESTRATOR_PORT || '9000', 10);

// ── Agent Registry ────────────────────────────────────────
const AGENT_REGISTRY = {
  echo:   process.env.ECHO_AGENT_URL   || 'http://localhost:9001',
  search: process.env.SEARCH_AGENT_URL || 'http://localhost:9002',
};

// ── Routes ────────────────────────────────────────────────

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: 'orchestrator', version: '1.0.0' });
});

app.get('/agents', (_req, res) => {
  const agents = Object.entries(AGENT_REGISTRY).map(([task, url]) => ({ task, url }));
  res.json({ agents });
});

app.post('/run', async (req, res) => {
  let request;
  try {
    request = validateRequest(req.body);
  } catch (err) {
    return res.status(err.status || 422).json({
      error: err.message,
      details: err.details || [],
    });
  }

  const agentUrl = AGENT_REGISTRY[request.task];
  if (!agentUrl) {
    return res.status(404).json({
      detail: `No agent registered for task '${request.task}'. Available: ${Object.keys(AGENT_REGISTRY).join(', ')}`,
    });
  }

  const endpoint = `${agentUrl}/run`;
  console.log(`[orchestrator] Routing task=${request.task} to ${endpoint}`);

  try {
    const { default: fetch } = await import('node-fetch');
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request),
      signal: AbortSignal.timeout(30_000),
    });

    const data = await response.json();
    return res.status(response.ok ? 200 : response.status).json(data);

  } catch (err) {
    console.error(`[orchestrator] Error routing to ${endpoint}:`, err.message);
    return res.status(200).json(
      errorResponse(
        request.task,
        `Agent '${request.task}' is not reachable. Is it running?`,
        request.request_id,
      ),
    );
  }
});

// ── Start ─────────────────────────────────────────────────
app.listen(ORCHESTRATOR_PORT, () => {
  console.log(`[orchestrator] Running on port ${ORCHESTRATOR_PORT}`);
  console.log(`[orchestrator] Registered agents: ${Object.keys(AGENT_REGISTRY).join(', ')}`);
});

export default app;
