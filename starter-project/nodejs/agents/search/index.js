// starter-project/nodejs/agents/search/index.js
// ============================================================
// Search Agent — Node.js variant
// ============================================================
// Mirrors agents/search/main.py in behaviour.
// Added to the project in Module 02 via a feature branch.
//
// Run: node agents/search/index.js
// ============================================================

import 'dotenv/config';
import express from 'express';
import { validateRequest, successResponse } from '../../models.js';

const app = express();
app.use(express.json());

const AGENT_NAME = 'search';
const PORT = parseInt(process.env.SEARCH_AGENT_PORT || '9002', 10);

// ── Mock Search Results ────────────────────────────────────
const MOCK_RESULTS = {
  'pull request': 'A pull request (PR) is a GitHub feature that lets you propose changes to a repository. When you open a PR, you\'re asking the repository maintainers to review and merge your branch into the target branch.',
  'git branch': 'A Git branch is a lightweight, movable pointer to a commit. Branches let you work on features or fixes in isolation. Create a branch with: git checkout -b branch-name',
  'github actions': 'GitHub Actions is a CI/CD platform built into GitHub. You define automated workflows in YAML files stored in .github/workflows/. Workflows can trigger on push, pull_request, schedule, and more.',
  'codespace': 'A GitHub Codespace is a cloud-hosted development environment powered by VS Code. It\'s configured by .devcontainer/devcontainer.json and starts in about 60 seconds.',
  'gitignore': 'A .gitignore file tells Git which files to never track. Any file matching a pattern in .gitignore cannot be accidentally committed.',
};

function mockSearch(query) {
  const queryLower = query.toLowerCase();
  for (const [keyword, result] of Object.entries(MOCK_RESULTS)) {
    if (queryLower.includes(keyword)) return result;
  }
  return `No results found for '${query}'. Try: pull request, git branch, github actions, codespace, or gitignore.`;
}

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

  console.log(`[${AGENT_NAME}] query=${request.input.slice(0, 80)}`);

  const output = mockSearch(request.input);
  return res.json(
    successResponse(AGENT_NAME, output, {
      request_id: request.request_id,
      metadata: { mock: true, query: request.input },
    }),
  );
});

app.listen(PORT, () => {
  console.log(`[${AGENT_NAME}] Running on port ${PORT}`);
});

export default app;
