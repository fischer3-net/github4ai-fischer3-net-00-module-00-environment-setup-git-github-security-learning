# 🤖 GitHub for AI Builders
### *Learn GitHub from Zero to Mid-Level Proficiency — Through the Lens of Building AI Agent Systems*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Discussions](https://img.shields.io/badge/GitHub-Discussions-blue?logo=github)](../../discussions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Educator Ready](https://img.shields.io/badge/Audience-GitHub%20Educators-purple)](docs/facilitator-guide.md)

---

> **A free, open-source GitHub course for developers and educators.**
> Every concept is taught by building a real Agent-to-Agent (A2A) AI system —
> so learners practice GitHub in a context that actually matters to them.

---

## 📖 About This Course

Most GitHub courses teach commands in isolation. This course is different.

From Module 1 through the Capstone, learners build a working **Agent-to-Agent (A2A) AI system** — a lightweight Orchestrator Agent that routes tasks to a team of Specialist Agents. Every GitHub topic is introduced *because the project needs it*, not as an abstract exercise.

Security is woven throughout. Each module includes a **Security Note** connecting GitHub's security tooling to real risks in AI projects — from accidentally committing API keys to evaluating third-party agent contributions.

---

## 🎯 Who This Course Is For

| Audience | What They Get |
|---|---|
| **Developers new to GitHub** | A structured path from zero to mid-level GitHub proficiency |
| **Developers building AI systems** | GitHub skills taught through a meaningful, working AI project |
| **GitHub Educators & Instructors** | A fully open, remixable course with facilitator guides, rubrics, and exercises |
| **Bootcamps & University Programs** | Drop-in modules with clearly scoped learning objectives |

**Prerequisites:** Basic programming familiarity (Python or Node.js). No prior GitHub experience required.

---

## 🗺️ Course Map

```
Module 00 → Setup & Codespaces
Module 01 → Repositories & Commits
Module 02 → Branching & Merging
Module 03 → Pull Requests & Code Review
Module 04 → Issues, Projects & Discussions
Module 05 → GitHub Actions & CI/CD         ⭐ Core Module
Module 06 → Security on GitHub             ⭐ Dedicated Security Module
Module 07 → Collaboration at Scale
Module 08 → Packages, Releases & Pages
Module 09 → Capstone Project
```

---

## 📚 Module Summaries

### Module 00 — Environment Setup
**GitHub Skills:** GitHub accounts, GitHub CLI, GitHub Desktop, Codespaces, forking
**Project Step:** Fork the A2A starter repo and launch it in a GitHub Codespace
**🔐 Security Note:** Why you should never commit secrets, and setting up `.gitignore` from day one

---

### Module 01 — Repositories & Commits
**GitHub Skills:** `git init`, staging, commits, commit message conventions, `.gitignore`, `README.md`, Markdown
**Project Step:** Initialize the Orchestrator Agent repo with a descriptive README and a proper `.gitignore`
**🔐 Security Note:** `.gitignore` patterns for AI/ML projects — protecting `.env` files, API key configs, and model weights

---

### Module 02 — Branching & Merging
**GitHub Skills:** Branch strategies (trunk-based vs. GitFlow), creating/switching branches, merge vs. rebase, resolving conflicts
**Project Step:** Create a `feature/specialist-agent-search` branch to add a Search Agent; intentionally simulate a merge conflict
**🔐 Security Note:** Branch protection rules — why no one, including maintainers, should push directly to `main`

---

### Module 03 — Pull Requests & Code Review
**GitHub Skills:** Opening PRs, PR templates, draft PRs, requesting reviews, approvals, suggested changes, squash merging
**Project Step:** Submit the Search Agent as a PR; reviewers evaluate the agent's prompt handling and tool definitions
**🔐 Security Note:** Security-aware code review for AI code — prompt injection risks, unsafe deserialization of agent responses

---

### Module 04 — Issues, Projects & Discussions
**GitHub Skills:** Issue templates, labels, milestones, GitHub Projects (kanban boards), GitHub Discussions
**Project Step:** Use a GitHub Project board to track agent development; debate the A2A communication protocol in Discussions
**🔐 Security Note:** GitHub's private vulnerability reporting — how to set up responsible disclosure for your open-source AI project

---

### Module 05 — GitHub Actions & CI/CD ⭐
**GitHub Skills:** Workflow YAML, triggers, jobs, steps, runners, marketplace actions, artifacts, caching, environment variables, secrets
**Project Step:** Build a CI pipeline that lints, tests, and validates agent message schemas on every PR; add a nightly integration test workflow
**🔐 Security Note:** Secrets management in Actions, `GITHUB_TOKEN` least-privilege scoping, pinning actions to commit SHAs, preventing script injection

---

### Module 06 — Security on GitHub ⭐
**GitHub Skills:** Dependabot (dependency updates + alerts), Secret Scanning, Code Scanning (CodeQL), CODEOWNERS, branch rulesets, SBOMs
**Project Step:** Enable the full GitHub security suite on the A2A project; write a `CODEOWNERS` file; generate a Software Bill of Materials
**🔐 Security Note:** Supply chain security for AI projects — why your LLM wrapper's transitive dependencies matter as much as your own code

---

### Module 07 — Collaboration at Scale
**GitHub Skills:** Forking workflow, syncing forks with upstream, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, GitHub CLI (`gh`), GitHub Sponsors
**Project Step:** Simulate an open-source contribution — fork, add a new Specialist Agent, open a PR upstream
**🔐 Security Note:** Evaluating third-party contributions to AI agent systems — reviewing for prompt injection, unintended tool access, and data leakage

---

### Module 08 — Packages, Releases & GitHub Pages
**GitHub Skills:** GitHub Releases, semantic versioning, auto-generated release notes, GitHub Packages (container registry), GitHub Pages
**Project Step:** Tag `v1.0.0` of the A2A system; publish the Orchestrator as a Docker image to GitHub Packages; deploy docs to GitHub Pages
**🔐 Security Note:** Signing releases with `actions/attest`; verifying container image provenance before deploying AI agents in production

---

### Module 09 — Capstone Project
Learners independently design and contribute a new Specialist Agent of their choosing, completing the **full GitHub workflow end-to-end**:

1. Open an Issue proposing the agent (using the issue template)
2. Create a feature branch with a meaningful name
3. Build the agent with commits that tell a story
4. Open a PR using the course PR template
5. Pass the CI pipeline (Actions)
6. Receive and address a code review
7. Merge and cut a new versioned release

A **rubric checklist** is provided in `modules/09-capstone/rubric.md` for educators assessing submissions.

---

## 🔐 Security Thread

Security is not a standalone chapter — it runs through the entire course. Each module's `security-note.md` connects a GitHub security feature to a real risk in AI development:

| Module | Security Concept |
|--------|-----------------|
| 00 | `.gitignore` and never committing secrets |
| 01 | Sensitive file patterns for AI/ML projects |
| 02 | Branch protection rules |
| 03 | Security-aware code review for AI code |
| 04 | Private vulnerability reporting & responsible disclosure |
| 05 | Secrets in Actions, action pinning, least privilege |
| 06 | Dependabot, CodeQL, Secret Scanning, SBOM generation |
| 07 | Evaluating third-party AI agent contributions |
| 08 | Release signing & container image provenance |

---

## 🤖 The A2A Starter Project

The teaching vehicle is a deliberately simple **Agent-to-Agent system** so the GitHub learning stays front and center:

```
Orchestrator Agent  (routes tasks by intent)
        │
        ├──▶ Echo Agent       ← Module 01–03 (trivially simple)
        ├──▶ Search Agent     ← added in Module 02
        └──▶ [Your Agent]     ← added in the Capstone
```

Each agent exposes a `/run` endpoint. The Orchestrator routes incoming task requests to the right agent based on intent keywords. The starter project is available in:

- **Python (FastAPI)** — `starter-project/python/`
- **Node.js (Express)** — `starter-project/nodejs/`

Educators can choose either variant. The GitHub concepts are identical regardless of language.

---

## 🗂️ Repository Structure

```
github-for-ai-builders/
├── README.md                    ← You are here
├── LICENSE                      ← MIT License
├── CONTRIBUTING.md              ← How to contribute to this course
├── CODE_OF_CONDUCT.md
├── CITATION.cff                 ← How to cite this course
├── docs/
│   ├── facilitator-guide.md     ← For GitHub educators
│   ├── course-guide.md          ← Learner-facing overview
│   └── glossary.md
├── modules/
│   ├── 00-setup/
│   │   ├── README.md            ← Lesson content
│   │   ├── exercises/
│   │   ├── solutions/
│   │   └── security-note.md
│   ├── 01-repos-and-commits/
│   ├── 02-branching-and-merging/
│   ├── 03-pull-requests/
│   ├── 04-issues-and-projects/
│   ├── 05-github-actions/
│   ├── 06-security/
│   ├── 07-collaboration/
│   ├── 08-packages-and-releases/
│   └── 09-capstone/
│       └── rubric.md
├── starter-project/
│   ├── python/
│   │   ├── orchestrator/
│   │   └── agents/
│   └── nodejs/
│       ├── orchestrator/
│       └── agents/
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── lesson-error.yml
    │   ├── new-exercise.yml
    │   └── new-module.yml
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        ├── ci.yml
        └── pages.yml
```

---

## 🚀 Getting Started

### For Learners

1. **Fork this repository** using the Fork button above
2. **Open in a Codespace** — click the green `Code` button → `Codespaces` → `Create codespace on main`
3. **Start with [Module 00](modules/00-setup/README.md)** and work through the modules in order
4. Join the **[Discussions](../../discussions)** to ask questions, share progress, and connect with other learners

### For Educators

1. Read the **[Facilitator Guide](docs/facilitator-guide.md)** for classroom setup, timing estimates, and assessment guidance
2. **Star and fork** the repo so your learners can fork from your copy
3. Open a **[Discussion](../../discussions)** in the `Educators` category to share how you're using this course
4. Found an issue or want to improve a module? See **[CONTRIBUTING.md](CONTRIBUTING.md)**

---

## 🤝 Contributing

This course thrives on community contributions. Whether you're fixing a typo, improving an exercise, translating a module, or adding a new Specialist Agent to the starter project — we'd love your help.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for full guidelines. Quick summary:

- **Lesson errors or unclear explanations** → Open a [lesson-error issue](../../issues/new?template=lesson-error.yml)
- **New exercises or improvements** → Open a [new-exercise issue](../../issues/new?template=new-exercise.yml)
- **New module ideas** → Start a [Discussion](../../discussions/new?category=ideas) first
- **Code contributions** → Fork → branch → PR (details in CONTRIBUTING.md)

All contributors are recognized in [CONTRIBUTORS.md](CONTRIBUTORS.md).

---

## 📄 License

This course is released under the **[MIT License](LICENSE)**. You are free to use, copy, modify, and distribute it — including for commercial educational purposes — with attribution.

If you use this course in your teaching, a citation is appreciated:

```
GitHub for AI Builders. MIT License.
https://github.com/[your-org]/github-for-ai-builders
```

A `CITATION.cff` file is included for formal academic citation.

---

## 💬 Community

| Space | Purpose |
|-------|---------|
| [Discussions → Q&A](../../discussions/categories/q-a) | Ask questions about course content |
| [Discussions → Educators](../../discussions/categories/educators) | Share classroom experiences and tips |
| [Discussions → Showcase](../../discussions/categories/showcase) | Share your Capstone agent! |
| [Discussions → Ideas](../../discussions/categories/ideas) | Propose new modules or exercises |
| [Issues](../../issues) | Report lesson errors or bugs in the starter project |

---

## 🗺️ Roadmap

- [ ] Spanish and Portuguese translations of core modules
- [ ] GitHub Copilot module (Module 10)
- [ ] Advanced track: GitHub Enterprise, org-level security policies
- [ ] Video walkthroughs for each module
- [ ] Auto-graded exercises using GitHub Actions

See the [public roadmap](../../projects) for full details and to vote on priorities.

---

<div align="center">

Made with ❤️ for the GitHub educator community.
<br>
Released under the MIT License — free forever.

</div>
