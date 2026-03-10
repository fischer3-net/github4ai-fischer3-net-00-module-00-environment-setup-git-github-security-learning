# Project File Map
## GitHub for AI Builders — Complete File Location Reference

This document maps every file generated in this project to its correct location
in the repository. Use this as your placement guide when setting up the repo.

**Legend**
- ✅ Fully authored — production ready
- 🔧 Needs one-time configuration (replace placeholder values)
- 📝 Stub — structure and frontmatter complete, content to be written
- 🖼️ Placeholder — needs replacement with final assets

---

## Repository Root
`github.com/[your-org]/github-for-ai-builders/`

```
github-for-ai-builders/               ← Repository root
│
├── README.md                          ✅ Full course overview, module map,
│                                         learner + educator quick-start
│
├── CONTRIBUTING.md                    ✅ Full contributor guide — branching
│                                         conventions, PR process, style guide,
│                                         agent contribution checklist
│
├── CODE_OF_CONDUCT.md                 ✅ Contributor Covenant v2.1 with
│                                         course-specific welcome language
│
├── CITATION.cff                       🔧 Academic citation file — update
│                                         [your-org], release date, and add
│                                         individual author entries as needed
│
├── LICENSE                            ← Create manually: MIT License
│                                         (not generated — use GitHub's
│                                          "Add a license" UI when creating
│                                          the repo, select MIT)
│
├── CONTRIBUTORS.md                    ← Create manually: start as an
│                                         empty file, grows with contributions
│
└── SECURITY.md                        ← Create manually: links to GitHub's
                                          private vulnerability reporting
```

---

## `.github/` — Repository Automation

```
.github/
│
├── dependabot.yml                     ✅ Automated dependency updates for
│                                         GitHub Actions, Python (pip),
│                                         Node.js (npm), and Docker
│
├── PULL_REQUEST_TEMPLATE.md           ✅ Tiered PR checklist — general,
│                                         lesson content, exercises, security
│                                         notes, starter project, translations
│
├── ISSUE_TEMPLATE/
│   ├── config.yml                     ✅ Disables blank issues; routes traffic
│   │                                     to correct Discussion categories
│   ├── lesson-error.yml               ✅ Structured form: report inaccurate
│   │                                     content, broken commands, typos
│   ├── new-exercise.yml               ✅ Structured form: propose new
│   │                                     exercises tied to the A2A project
│   └── new-module.yml                 ✅ Structured form: propose new modules
│                                         (requires prior Discussion link)
│
└── workflows/
    ├── ci.yml                         ✅ Main CI pipeline — Markdown lint,
    │                                     YAML lint, link check, Python tests
    │                                     (3.11/3.12 matrix), Node.js tests
    │                                     (20/22 matrix), A2A schema validation,
    │                                     CI Gate required status check
    │
    ├── nightly.yml                    ✅ Nightly integration tests — starts
    │                                     full A2A stack, runs E2E tests,
    │                                     auto-opens GitHub Issue on failure
    │
    ├── codeql.yml                     ✅ CodeQL security scanning — Python
    │                                     and JavaScript, security-extended
    │                                     query suite, weekly schedule
    │
    ├── pages.yml                      ✅ Deploys Starlight docs site to
    │                                     GitHub Pages on push to main
    │                                     (Astro/Node.js build, not MkDocs)
    │
    └── release.yml                    ✅ Full release pipeline — builds
                                          Docker images, pushes to ghcr.io,
                                          artifact attestation, SBOM generation,
                                          GitHub Release with auto notes
```

---

## `docs/` — Starlight Documentation Site
*This is the Astro/Starlight project. Run `npm install && npm run dev` from this directory.*

```
docs/
│
├── README.md                          ✅ Explains the docs site stack,
│                                         local dev setup, component usage,
│                                         and how to write a module page
│
├── astro.config.mjs                   🔧 Main Starlight config — site URL,
│                                         nav sidebar, theme, i18n, edit links.
│                                         Replace all [your-org] placeholders
│
├── package.json                       ✅ Astro + Starlight dependencies
│
├── tsconfig.json                      ✅ TypeScript config (strict mode)
│
├── public/                            Static assets served at site root
│   ├── favicon.svg                    🖼️ Placeholder robot SVG — replace
│   ├── logo-light.svg                 🖼️ Placeholder wordmark — replace
│   ├── logo-dark.svg                  🖼️ Placeholder wordmark — replace
│   └── og-image.png                   ← Create manually: 1200×630 Open
│                                         Graph image for social sharing
│
├── src/
│   │
│   ├── styles/
│   │   └── custom.css                 ✅ Brand theme — Fraunces headings,
│   │                                     DM Sans body, DM Mono code,
│   │                                     indigo/amber palette, dark mode,
│   │                                     SecurityNote, A2AConnection,
│   │                                     ModuleHeader component styles
│   │
│   ├── components/                    Reusable Astro components
│   │   ├── SecurityNote.astro         ✅ 🔐 Security callout with concept
│   │   │                                 badge, module number, deep-dive link.
│   │   │                                 Used in EVERY module page.
│   │   │
│   │   ├── ModuleHeader.astro         ✅ Renders learning objectives,
│   │   │                                 duration, difficulty, prerequisites,
│   │   │                                 and project step from frontmatter.
│   │   │                                 Used at top of EVERY module page.
│   │   │
│   │   └── A2AConnection.astro        ✅ A2A project step callout — shows
│   │                                     which agent and files are involved.
│   │                                     Used in EVERY module page.
│   │
│   └── content/
│       ├── config.ts                  ✅ Zod schema for all MDX frontmatter —
│       │                                 enforces learningObjectives (min 3),
│       │                                 moduleNumber, difficulty enum,
│       │                                 hasSecurityNote, etc. TypeScript
│       │                                 catches missing fields at build time.
│       │
│       └── docs/                      All site pages (MDX format)
│           │
│           ├── index.mdx              ✅ Home page — hero, course overview,
│           │                             CardGrid, LinkCards, quick nav
│           │
│           ├── how-it-works.mdx       📝 Stub — explain course structure,
│           │                             how A2A project threads through modules
│           │
│           ├── a2a-project.mdx        📝 Stub — explain the A2A system
│           │                             architecture (Orchestrator + Agents)
│           │
│           ├── modules/               One subfolder per module
│           │   │
│           │   ├── 00-setup/
│           │   │   └── index.mdx      ✅ FULLY AUTHORED EXEMPLAR
│           │   │                         Complete module showing all components,
│           │   │                         Steps, Tabs, Asides, SecurityNote,
│           │   │                         A2AConnection, ModuleHeader.
│           │   │                         Use as template for all other modules.
│           │   │
│           │   ├── 01-repos-and-commits/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │
│           │   ├── 02-branching-and-merging/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │
│           │   ├── 03-pull-requests/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │
│           │   ├── 04-issues-and-projects/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │
│           │   ├── 05-github-actions/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │                         Teach against the real ci.yml,
│           │   │                         nightly.yml, and release.yml
│           │   │                         workflows already in .github/
│           │   │
│           │   ├── 06-security/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │                         Teach against the real codeql.yml
│           │   │                         and dependabot.yml already in .github/
│           │   │
│           │   ├── 07-collaboration/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │
│           │   ├── 08-packages-and-releases/
│           │   │   └── index.mdx      📝 Stub — frontmatter complete
│           │   │                         Teach against the real release.yml
│           │   │                         and pages.yml already in .github/
│           │   │
│           │   └── 09-capstone/
│           │       └── index.mdx      📝 Stub — frontmatter complete
│           │
│           ├── security/              Security Thread deep dives
│           │   │                      (cross-referenced from module SecurityNotes)
│           │   ├── overview.mdx       📝 Stub
│           │   ├── never-commit-secrets.mdx   📝 Stub
│           │   ├── branch-protection.mdx      📝 Stub
│           │   ├── code-review.mdx            📝 Stub
│           │   ├── actions-secrets.mdx        📝 Stub
│           │   ├── dependabot-codeql.mdx      📝 Stub
│           │   ├── supply-chain.mdx           📝 Stub
│           │   └── sbom-attestation.mdx       📝 Stub
│           │
│           ├── educators/             For GitHub educators and instructors
│           │   ├── facilitator-guide.mdx      📝 Stub
│           │   ├── timing.mdx                 📝 Stub
│           │   ├── rubrics.mdx                📝 Stub
│           │   ├── classroom-setup.mdx        📝 Stub
│           │   └── adapting.mdx               📝 Stub
│           │
│           ├── reference/             Quick-reference pages
│           │   ├── glossary.mdx               📝 Stub
│           │   ├── git-cheatsheet.mdx         📝 Stub
│           │   ├── a2a-schema.mdx             📝 Stub
│           │   └── gh-cheatsheet.mdx          📝 Stub
│           │
│           └── contributing/          Contributor guides (mirrors CONTRIBUTING.md)
│               ├── how-to-contribute.mdx      📝 Stub
│               ├── style-guide.mdx            📝 Stub
│               ├── security-notes.mdx         📝 Stub
│               └── translating.mdx            📝 Stub
```

---

## `modules/` — Course Module Source Files
*Raw lesson content that also lives in the repo for contributors working directly in Markdown. The `docs/` site renders these into web pages.*

```
modules/
│
├── 00-setup/
│   ├── README.md                      ← Mirror of docs module content (Markdown)
│   ├── security-note.md               ← Never Commit Secrets
│   ├── exercises/
│   │   └── 01-fork-and-codespace.md
│   └── solutions/
│       └── 01-fork-and-codespace.md
│
├── 01-repos-and-commits/              ← To be created
├── 02-branching-and-merging/          ← To be created
├── 03-pull-requests/                  ← To be created
├── 04-issues-and-projects/            ← To be created
├── 05-github-actions/                 ← To be created
├── 06-security/                       ← To be created
├── 07-collaboration/                  ← To be created
├── 08-packages-and-releases/          ← To be created
└── 09-capstone/
    └── rubric.md                      ← To be created
```

---

## `starter-project/` — The A2A Teaching Project

```
starter-project/
│
├── python/                            Python (FastAPI) variant
│   ├── .env.example                   ← To be created
│   ├── .gitignore                     ← To be created
│   ├── requirements.txt               ← To be created
│   ├── requirements-dev.txt           ← To be created
│   ├── orchestrator/
│   │   └── main.py                    ← To be created
│   ├── agents/
│   │   ├── echo/
│   │   │   └── main.py                ← To be created (Module 00 runs this)
│   │   └── search/
│   │       └── main.py                ← To be created (Module 02 adds this)
│   └── tests/
│       ├── unit/                      ← To be created
│       └── integration/               ← To be created
│
├── nodejs/                            Node.js (Express) variant
│   ├── .env.example                   ← To be created
│   ├── package.json                   ← To be created
│   ├── orchestrator/
│   │   └── index.js                   ← To be created
│   ├── agents/
│   │   ├── echo/
│   │   │   └── index.js               ← To be created
│   │   └── search/
│   │       └── index.js               ← To be created
│   └── tests/                         ← To be created
│
└── schema/
    ├── a2a-message.schema.json        ← To be created (validated by ci.yml)
    └── fixtures/
        └── echo-request.json          ← To be created (schema test fixtures)
```

---

## Config Files Still Needed

These small files are referenced throughout the project but not yet generated:

| File | Location | Purpose |
|------|----------|---------|
| `LICENSE` | Repo root | MIT license — use GitHub's UI when creating the repo |
| `CONTRIBUTORS.md` | Repo root | Starts empty, grows with merged PRs |
| `SECURITY.md` | Repo root | Links to private vulnerability reporting |
| `.markdownlint.yml` | Repo root | Config for `ci.yml` Markdown linting step |
| `.yamllint.yml` | Repo root | Config for `ci.yml` YAML linting step |
| `.devcontainer/devcontainer.json` | Repo root | Defines the GitHub Codespace environment (Module 00 depends on this) |
| `docs/package-lock.json` | `docs/` | Generated by running `npm install` in `docs/` — commit this |
| `public/og-image.png` | `docs/public/` | 1200×630 Open Graph image for social sharing |

---

## Summary Counts

| Category | Status | Count |
|----------|--------|-------|
| Root repo files | ✅ Fully authored | 4 |
| `.github/` automation files | ✅ Fully authored | 11 |
| Starlight site config & components | ✅ Fully authored | 8 |
| Module 00 | ✅ Fully authored | 1 |
| Module stubs (01–09) | 📝 Stub | 9 |
| Security Thread pages | 📝 Stub | 8 |
| Educator pages | 📝 Stub | 5 |
| Reference pages | 📝 Stub | 4 |
| Contributing pages | 📝 Stub | 4 |
| Starter project files | ← To be created | ~20 |
| Config files still needed | ← To be created | 8 |
| **Total files generated** | | **63** |
