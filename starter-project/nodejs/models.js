// starter-project/nodejs/models.js
// ============================================================
// Shared A2A Message Models — Node.js
// ============================================================
// JavaScript implementation of the A2A message contract.
// Mirrors the Python models.py and the JSON schema in
// starter-project/schema/a2a-message.schema.json.
// ============================================================

export const AgentStatus = Object.freeze({
  SUCCESS: 'success',
  ERROR: 'error',
});

/**
 * Validate an incoming AgentRequest object.
 * Throws an Error with a descriptive message if validation fails.
 * @param {object} data - Raw request body
 * @returns {{ task: string, input: string, context?: object, request_id?: string }}
 */
export function validateRequest(data) {
  const errors = [];

  if (!data.task || typeof data.task !== 'string') {
    errors.push('task: required string');
  } else if (data.task.length < 1 || data.task.length > 100) {
    errors.push('task: must be 1–100 characters');
  }

  if (!data.input || typeof data.input !== 'string') {
    errors.push('input: required string');
  } else if (data.input.length < 1 || data.input.length > 4096) {
    errors.push('input: must be 1–4096 characters');
  }

  if (errors.length > 0) {
    const err = new Error(`Validation error: ${errors.join(', ')}`);
    err.status = 422;
    err.details = errors;
    throw err;
  }

  return {
    task: data.task,
    input: data.input,
    context: data.context || null,
    request_id: data.request_id || null,
  };
}

/**
 * Build a successful AgentResponse object.
 * @param {string} agent - Agent name
 * @param {string} output - Response text
 * @param {object} [options] - Optional request_id and metadata
 */
export function successResponse(agent, output, { request_id = null, metadata = null } = {}) {
  return {
    agent,
    status: AgentStatus.SUCCESS,
    output,
    request_id,
    metadata,
  };
}

/**
 * Build an error AgentResponse object.
 * @param {string} agent - Agent name
 * @param {string} errorMessage - Human-readable error description
 * @param {string} [request_id] - Optional request ID to echo back
 */
export function errorResponse(agent, errorMessage, request_id = null) {
  return {
    agent,
    status: AgentStatus.ERROR,
    output: '',
    error: errorMessage,
    request_id,
  };
}
