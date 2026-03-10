# Contributing to GitHub for AI Builders

First off — thank you. 🎉

This course exists to make GitHub education better, and every contribution matters — from fixing a single typo to authoring an entirely new module. This guide explains how to contribute effectively, respectfully, and in a way that keeps the course high quality for learners and educators worldwide.

> **New to open source?** This course is itself a great place to practice the GitHub skills you're learning. Your first contribution here *is* the lesson.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [What We're Looking For](#what-were-looking-for)
- [What We're Not Looking For](#what-were-not-looking-for)
- [Ways to Contribute](#ways-to-contribute)
  - [Reporting Lesson Errors](#reporting-lesson-errors)
  - [Suggesting New Exercises](#suggesting-new-exercises)
  - [Proposing New Modules](#proposing-new-modules)
  - [Translating Content](#translating-content)
  - [Contributing Code (Starter Project)](#contributing-code-starter-project)
  - [Contributing Lesson Content](#contributing-lesson-content)
- [Development Setup](#development-setup)
- [Branching & Commit Conventions](#branching--commit-conventions)
- [Pull Request Process](#pull-request-process)
- [Content Style Guide](#content-style-guide)
- [Security Disclosures](#security-disclosures)
- [Recognition](#recognition)
- [Questions?](#questions)

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it. Please report unacceptable behavior to the maintainers via the contact listed in that document.

We are committed to a welcoming environment for contributors of all experience levels, backgrounds, and identities.

---

## What We're Looking For

The best contributions to this course:

- **Make learning clearer.** If an explanation confused you, your rewrite will help the next person.
- **Deepen the A2A project connection.** Exercises that tie GitHub concepts to the Agent-to-Agent project are strongly preferred over abstract examples.
- **Strengthen the security thread.** Security notes that connect to real AI development risks — not generic warnings — are especially valued.
- **Work for educators.** Instructors need content that's predictable, scoped, and remixable. Keep modules self-contained.
- **Stay language-agnostic on GitHub concepts.** GitHub skills should be taught identically regardless of whether the learner chose the Python or Node.js starter project.

---

## What We're Not Looking For

To keep the course focused and maintainable, we are unlikely to accept:

- New programming languages for the starter project (Python and Node.js are the supported variants)
- Exercises that require paid GitHub features unless a free-tier equivalent exists
- Content that teaches AI/ML concepts rather than GitHub concepts
- Modules beyond mid-level GitHub proficiency (an advanced track is on the roadmap but separate)
- Rewrites of content without a corresponding issue explaining the problem

**When in doubt, open a Discussion before writing content.** It saves everyone time.

---

## Ways to Contribute

### Reporting Lesson Errors

Found an inaccurate explanation, a broken command, an outdated screenshot, or a typo?

1. **Search [existing issues](../../issues)** first to avoid duplicates
2. Open a new issue using the **[Lesson Error template](../../issues/new?template=lesson-error.yml)**
3. Include: which module, what the error is, and (if you know it) what the correct content should be

For small, obvious errors (typos, broken links), you're welcome to skip the issue and open a PR directly.

---

### Suggesting New Exercises

Have an idea for a new exercise, challenge, or quiz question?

1. Check the module's `exercises/` folder to see what already exists
2. Open an issue using the **[New Exercise template](../../issues/new?template=new-exercise.yml)**
3. Describe: the GitHub skill being practiced, how it connects to the A2A project, and the rough format (step-by-step, open-ended, etc.)

---

### Proposing New Modules

New module proposals are significant — please start a **[Discussion in the Ideas category](../../discussions/new?category=ideas)** before opening a PR or writing content.

Include in your discussion:
- The GitHub topic(s) the module would cover
- The target proficiency level
- How it connects to the A2A project
- Whether it fits within the existing course sequence or would be an extension

Maintainers will discuss and may greenlight the module, at which point an issue will be opened to track the work.

---

### Translating Content

We warmly welcome translations. Our priority languages are Spanish and Portuguese, but all translations are valued.

**Before starting a translation:**

1. Open a [Discussion](../../discussions/new?category=ideas) announcing your intent (to avoid duplicate work)
2. Maintainers will create a tracking issue and a translation branch for you

**Translation guidelines:**
- Translate content in `modules/` and `docs/` — do not translate code, file names, or command-line instructions
- Maintain the same structure and heading hierarchy as the English original
- Translated files live at `translations/[language-code]/modules/...` (e.g., `translations/es/modules/01-repos-and-commits/README.md`)
- If a module hasn't been finalized in English yet, wait until it is before translating it

---

### Contributing Code (Starter Project)

The starter project in `starter-project/` is the A2A system learners build throughout the course. Contributions here should:

- Keep the code **intentionally simple** — the goal is to teach GitHub, not software architecture
- Add agents only if they serve a clear pedagogical purpose in a module
- Include unit tests for any new agent logic
- Work identically in both the Python and Node.js variants, or clearly scope to one with a note
- Follow the security practices taught in the course (no hardcoded secrets, proper `.gitignore`, etc.)

For new Specialist Agents specifically, see the **[Agent Contribution Checklist](#agent-contribution-checklist)** below.

#### Agent Contribution Checklist

Before submitting a new Specialist Agent to the starter project, confirm:

- [ ] The agent exposes a `/run` endpoint matching the A2A message schema
- [ ] The agent is registered in the Orchestrator's routing table
- [ ] No secrets, API keys, or credentials are hardcoded — all use environment variables
- [ ] A `.env.example` is included showing required environment variable names (not values)
- [ ] The agent handles malformed input gracefully without crashing
- [ ] Unit tests are included in `tests/`
- [ ] The agent is documented in its own `README.md` inside its folder
- [ ] The `CODEOWNERS` file is updated if the agent introduces a new sensitive capability

---

### Contributing Lesson Content

This is the most impactful contribution type. Lesson content lives in `modules/[module-name]/README.md`.

**Before writing lesson content:**

1. An issue should exist for the content you're adding (open one if not)
2. Check the [Content Style Guide](#content-style-guide) carefully
3. Review two or three existing module `README.md` files to understand the voice and structure

**Each module must contain:**

| File | Purpose |
|------|---------|
| `README.md` | The lesson itself — concepts, explanations, examples |
| `exercises/` | One or more hands-on exercises tied to the A2A project |
| `solutions/` | Reference solutions for each exercise |
| `security-note.md` | One focused security concept connected to the module topic and AI development |

---

## Development Setup

### Prerequisites

- Git and a GitHub account
- For the starter project: Python 3.11+ or Node.js 20+
- Optionally: GitHub CLI (`gh`) — taught in Module 07

### Setting Up Locally

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/github-for-ai-builders.git
cd github-for-ai-builders

# Set the upstream remote
git remote add upstream https://github.com/[course-org]/github-for-ai-builders.git

# Verify remotes
git remote -v
```

### Running the Starter Project (Python)

```bash
cd starter-project/python
cp .env.example .env
# Edit .env with any required values

pip install -r requirements.txt
python orchestrator/main.py
```

### Running the Starter Project (Node.js)

```bash
cd starter-project/nodejs
cp .env.example .env

npm install
npm start
```

### Using GitHub Codespaces

Click the green **Code** button on the repo → **Codespaces** → **Create codespace on main**. The devcontainer will set up the environment automatically. This is the recommended approach for learners and is covered in Module 00.

---

## Branching & Commit Conventions

### Branch Names

Use the following prefixes:

| Prefix | Use for |
|--------|---------|
| `fix/` | Correcting errors in lesson content or starter project |
| `feat/` | New exercises, modules, or starter project agents |
| `docs/` | README, CONTRIBUTING, facilitator guide updates |
| `translation/` | Translated content |
| `chore/` | Dependency updates, CI/CD changes, tooling |

**Examples:**
```
fix/module-03-pr-template-typo
feat/module-06-codeql-exercise
docs/facilitator-guide-timing-estimates
translation/es-module-01
chore/update-dependabot-config
```

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(scope): <short description>

[optional body]

[optional footer: closes #issue-number]
```

**Types:** `fix`, `feat`, `docs`, `chore`, `test`, `translation`

**Examples:**
```
fix(module-03): correct git merge command in exercise 2

feat(starter-project): add Calculator specialist agent with unit tests

Closes #42

docs(contributing): add agent contribution checklist

translation(es): add Spanish translation of module 01
```

**Commit message rules:**
- Use the imperative mood: "add exercise" not "added exercise"
- Keep the subject line under 72 characters
- Reference the relevant issue number in the footer when applicable
- One logical change per commit — don't bundle unrelated changes

---

## Pull Request Process

1. **Sync your fork** with upstream before branching:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create your branch** from `main`:
   ```bash
   git checkout -b fix/module-02-conflict-exercise
   ```

3. **Make your changes**, committing as you go with meaningful commit messages

4. **Push to your fork:**
   ```bash
   git push origin fix/module-02-conflict-exercise
   ```

5. **Open a Pull Request** against the `main` branch of the upstream repo
   - Fill out the **PR template** completely — incomplete PRs may be closed without review
   - Link the related issue in the PR description using `Closes #[issue-number]`
   - Set yourself as the assignee

6. **Wait for CI to pass.** The CI pipeline checks Markdown formatting and runs starter project tests. Fix any failures before requesting review.

7. **Address review feedback.** Push additional commits to the same branch — do not close and re-open the PR.

8. **Once approved**, a maintainer will squash-merge your PR. Your commit message will be the PR title, so make it descriptive.

### PR Review Timeline

Maintainers aim to review PRs within **7 days**. If you haven't heard back in 10 days, add a comment pinging `@maintainers`. We're volunteers and occasionally need a nudge.

### Draft PRs

If you're still working on something but want early feedback, open the PR as a **Draft**. Move it to "Ready for Review" when it's complete.

---

## Content Style Guide

### Voice and Tone

- **Direct and practical.** Learners are here to do things, not read essays.
- **Friendly but not condescending.** Assume competence; explain unfamiliar terms when they first appear.
- **Honest about complexity.** Don't oversimplify. If something has tradeoffs, say so.
- **Connected to the project.** Every concept should be grounded in the A2A system. Avoid generic examples when a project-relevant one exists.

### Lesson Structure

Each module `README.md` should follow this structure:

```markdown
# Module [N] — [Title]

## Learning Objectives
(3–5 bullet points, each beginning with a verb: "Create", "Explain", "Configure")

## Background
(Brief explanation of the concept and why it matters — 1–3 paragraphs)

## [Section: Core Concept]
(Explanation with examples. Use code blocks for commands.)

## Connecting to the A2A Project
(Explicit link: how does this concept apply to what we're building?)

## Exercise
(Reference to exercises/ folder — don't embed full exercises in the README)

## Security Note
(Reference to security-note.md — don't embed it here)

## Summary
(3–5 key takeaways)

## Next Steps
(Link to next module)
```

### Formatting Rules

- Use **ATX-style headings** (`#`, `##`, `###`) — no underline-style
- Use **fenced code blocks** with language identifiers (` ```bash `, ` ```python `, ` ```yaml `)
- Use **relative links** for internal references (`../02-branching/README.md`, not absolute URLs)
- Use **present tense** ("GitHub creates a merge commit" not "GitHub will create")
- Spell out **GitHub feature names** exactly as GitHub does: "GitHub Actions", "Dependabot", "GitHub Codespaces" (capitalized)
- Screenshots are welcome but must include **alt text** and be stored in a module's `images/` folder
- Do not use screenshots for command-line output — use code blocks instead

### Security Notes

Security notes (`security-note.md`) should be:
- **One concept per note** — focused, not a list of security tips
- **Specifically connected to AI development risk** — not generic security advice
- **Actionable** — learners should be able to apply the note to the starter project immediately
- **100–300 words** in length — concise enough to read in under two minutes

### Exercises

Exercises in `exercises/` should:
- Have a clear **goal statement** at the top
- Provide **step-by-step instructions** learners can follow independently
- Specify **expected output** so learners know when they've succeeded
- Include a **hint** for common stumbling points
- Reference the corresponding file in `solutions/` at the end

---

## Security Disclosures

**Please do not report security vulnerabilities via public GitHub issues.**

If you discover a security vulnerability in the starter project code or course content that could affect learners (for example, a workflow file that could be exploited via a pull request from a fork), please use **[GitHub's private vulnerability reporting](../../security/advisories/new)** for this repository.

We will acknowledge the report within 48 hours and aim to address it within 14 days.

This process is itself demonstrated in **Module 04** of the course — so reporting a real vulnerability here is a great chance to practice what you've learned.

---

## Recognition

All contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md). Your GitHub username, the type of contribution, and a link to your PR are recorded there.

Significant contributors (multiple merged PRs, new modules, translation leads) may be invited to join as **Repository Collaborators** with triage or write access.

We also recognize contributions via:
- The **Discussions → Showcase** category (share your Capstone agents!)
- Shoutouts in release notes
- A dedicated Educators section for those using this course in the classroom

---

## Questions?

- **Course content questions** → [Discussions → Q&A](../../discussions/categories/q-a)
- **Educator questions** → [Discussions → Educators](../../discussions/categories/educators)
- **Contribution process questions** → Comment on the relevant issue or open a [Discussion](../../discussions/new)
- **Everything else** → Open a [blank issue](../../issues/new) with as much context as you can

We're glad you're here. 🚀
