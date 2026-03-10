// starter-project/nodejs/tests/integration/a2a.test.js
// ============================================================
// Integration Tests — Full A2A System (Node.js)
// ============================================================
// Requires all services running. See nightly.yml for how
// the CI workflow starts them. For local runs:
//
//   npm run start:all   (in one terminal)
//   ORCHESTRATOR_URL=http://localhost:9000 npm run test:integration
// ============================================================

import fetch from 'node-fetch';

const BASE = process.env.ORCHESTRATOR_URL || 'http://localhost:9000';

async function post(path, body) {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return { status: res.status, body: await res.json() };
}

async function get(path) {
  const res = await fetch(`${BASE}${path}`);
  return { status: res.status, body: await res.json() };
}

describe('Orchestrator Health', () => {
  it('responds to /health', async () => {
    const { status, body } = await get('/health');
    expect(status).toBe(200);
    expect(body.status).toBe('ok');
  });

  it('lists registered agents', async () => {
    const { status, body } = await get('/agents');
    expect(status).toBe(200);
    const tasks = body.agents.map((a) => a.task);
    expect(tasks).toContain('echo');
    expect(tasks).toContain('search');
  });
});

describe('Echo routing', () => {
  it('routes echo task end-to-end', async () => {
    const { status, body } = await post('/run', {
      task: 'echo',
      input: 'integration test',
    });
    expect(status).toBe(200);
    expect(body.status).toBe('success');
    expect(body.output).toBe('Echo: integration test');
  });
});

describe('Search routing', () => {
  it('routes search task end-to-end', async () => {
    const { status, body } = await post('/run', {
      task: 'search',
      input: 'What is a pull request?',
    });
    expect(status).toBe(200);
    expect(body.status).toBe('success');
    expect(body.output.length).toBeGreaterThan(0);
  });
});

describe('Error handling', () => {
  it('returns 404 for unknown task', async () => {
    const { status } = await post('/run', {
      task: 'no-such-agent',
      input: 'test',
    });
    expect(status).toBe(404);
  });
});
