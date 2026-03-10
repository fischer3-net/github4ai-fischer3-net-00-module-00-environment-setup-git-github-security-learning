// starter-project/nodejs/tests/unit/agents.test.js
// ============================================================
// Unit Tests — Echo and Search Agents (Node.js)
// ============================================================

import request from 'supertest';
import echoApp from '../../agents/echo/index.js';
import searchApp from '../../agents/search/index.js';
import { validateRequest, successResponse, errorResponse, AgentStatus } from '../../models.js';

// ── Model Tests ───────────────────────────────────────────
describe('validateRequest', () => {
  it('accepts a valid minimal request', () => {
    const req = validateRequest({ task: 'echo', input: 'hello' });
    expect(req.task).toBe('echo');
    expect(req.input).toBe('hello');
    expect(req.request_id).toBeNull();
  });

  it('throws on missing task', () => {
    expect(() => validateRequest({ input: 'hello' })).toThrow();
  });

  it('throws on empty input', () => {
    expect(() => validateRequest({ task: 'echo', input: '' })).toThrow();
  });

  it('throws on task over 100 chars', () => {
    expect(() => validateRequest({ task: 'x'.repeat(101), input: 'hi' })).toThrow();
  });
});

describe('successResponse', () => {
  it('returns correct shape', () => {
    const res = successResponse('echo', 'Echo: hi');
    expect(res.status).toBe(AgentStatus.SUCCESS);
    expect(res.output).toBe('Echo: hi');
    expect(res.agent).toBe('echo');
    expect(res.error).toBeUndefined();
  });
});

describe('errorResponse', () => {
  it('returns correct shape', () => {
    const res = errorResponse('echo', 'Something broke');
    expect(res.status).toBe(AgentStatus.ERROR);
    expect(res.output).toBe('');
    expect(res.error).toBe('Something broke');
  });
});

// ── Echo Agent Tests ──────────────────────────────────────
describe('Echo Agent', () => {
  it('GET /health returns 200', async () => {
    const res = await request(echoApp).get('/health');
    expect(res.status).toBe(200);
    expect(res.body.service).toBe('echo');
  });

  it('POST /run echoes input with prefix', async () => {
    const res = await request(echoApp)
      .post('/run')
      .send({ task: 'echo', input: 'Is this working?' });
    expect(res.status).toBe(200);
    expect(res.body.output).toBe('Echo: Is this working?');
    expect(res.body.status).toBe('success');
  });

  it('POST /run preserves request_id', async () => {
    const id = '550e8400-e29b-4d8d-a456-426614174000';
    const res = await request(echoApp)
      .post('/run')
      .send({ task: 'echo', input: 'test', request_id: id });
    expect(res.body.request_id).toBe(id);
  });

  it('POST /run rejects missing input with 422', async () => {
    const res = await request(echoApp)
      .post('/run')
      .send({ task: 'echo' });
    expect(res.status).toBe(422);
  });
});

// ── Search Agent Tests ────────────────────────────────────
describe('Search Agent', () => {
  it('GET /health returns 200', async () => {
    const res = await request(searchApp).get('/health');
    expect(res.status).toBe(200);
    expect(res.body.service).toBe('search');
  });

  it('POST /run returns a result for known query', async () => {
    const res = await request(searchApp)
      .post('/run')
      .send({ task: 'search', input: 'What is a pull request?' });
    expect(res.status).toBe(200);
    expect(res.body.status).toBe('success');
    expect(res.body.output.length).toBeGreaterThan(10);
  });

  it('POST /run returns metadata with mock flag', async () => {
    const res = await request(searchApp)
      .post('/run')
      .send({ task: 'search', input: 'github actions' });
    expect(res.body.metadata.mock).toBe(true);
  });

  it('POST /run returns default for unknown query', async () => {
    const res = await request(searchApp)
      .post('/run')
      .send({ task: 'search', input: 'meaning of life' });
    expect(res.body.output).toContain('No results found');
  });
});
