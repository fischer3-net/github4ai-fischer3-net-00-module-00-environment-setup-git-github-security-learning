// starter-project/nodejs/agents/echo/index.js
// ============================================================
// Echo Agent — Node.js variant
// ============================================================
// Mirrors agents/echo/main.py in behaviour.
//
// Run: node agents/echo/index.js
// Test:
//   curl -X POST http://localhost:9001/run \
//     -H "Content-Type: application/json" \
//     -d '{"task":"echo","input":"Is this working?"}'
// ============================================================

import 'dotenv/config';
import express from 'express';
import { validateRequest, successResponse } from '../../models.js';

const app = express();
app.use(express.json());

const AGENT_NAME = 'echo';
const PORT = parseInt(process.env.ECHO_AGENT_PORT || '9001', 10);

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: AGENT_NAME, version: '1.0.0' });
});

app.post('/run', (req, res) => {
  let request;
  try {
    request = validateRequest(req.body);
  } catch (err) {
    return res.status(err.status || 422).json({ error: err.message });
  }

  console.log(`[${AGENT_NAME}] input=${request.input.slice(0, 50)}`);

  const output = `Echo: ${request.input}`;
  return res.json(successResponse(AGENT_NAME, output, { request_id: request.request_id }));
});

app.listen(PORT, () => {
  console.log(`[${AGENT_NAME}] Running on port ${PORT}`);
});

export default app;
