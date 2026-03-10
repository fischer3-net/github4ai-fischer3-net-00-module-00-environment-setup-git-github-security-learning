# Course Documentation Site

This directory contains the **Starlight (Astro)** documentation site for GitHub for AI Builders — the source for the GitHub Pages site at `https://[your-org].github.io/github-for-ai-builders/`.

## Stack

- **[Astro](https://astro.build)** — Static site generator
- **[Starlight](https://starlight.astro.build)** — Astro documentation theme
- **MDX** — Markdown + Astro components for rich lesson pages

## Local Development

```bash
# From this directory (docs/)
npm install
npm run dev
```

The site will be available at `http://localhost:4321/github-for-ai-builders/`

Hot-reload is enabled — edit any `.mdx` file and the browser updates instantly.

## Directory Structure

```
docs/
├── astro.config.mjs          ← Site config, nav, theme
├── package.json
├── tsconfig.json
├── public/                   ← Static assets (logos, favicon, OG image)
│   ├── favicon.svg
│   ├── logo-light.svg
│   └── logo-dark.svg
└── src/
    ├── components/           ← Reusable Astro components
    │   ├── SecurityNote.astro      ← 🔐 Security callout (used in every module)
    │   ├── ModuleHeader.astro      ← Learning objectives + module meta
    │   └── A2AConnection.astro     ← A2A project step callout
    ├── styles/
    │   └── custom.css              ← Brand colors, typography overrides
    └── content/
        └── docs/                   ← All page content (MDX)
            ├── index.mdx           ← Home page
            ├── how-it-works.mdx
            ├── a2a-project.mdx
            ├── modules/            ← One folder per module
            │   ├── 00-setup/
            │   │   └── index.mdx   ← Full exemplar module
            │   ├── 01-repos-and-commits/
            │   └── ...
            ├── security/           ← Security Thread deep dives
            ├── educators/          ← Facilitator guides and rubrics
            ├── reference/          ← Cheatsheets and glossary
            └── contributing/       ← Contributor guides
```

## Writing a Module Page

Every module page is an `.mdx` file that uses three custom components:

```mdx
---
title: "Module XX · Title"
moduleNumber: X
duration: "60–90 minutes"
difficulty: beginner
hasSecurityNote: true
securityConcept: "Concept Name"
projectStep: "What gets built in the A2A project"
prerequisites: []
learningObjectives:
  - "Objective 1 starting with a verb"
  - "Objective 2 starting with a verb"
  - "Objective 3 starting with a verb"
---

import ModuleHeader from '@components/ModuleHeader.astro';
import SecurityNote from '@components/SecurityNote.astro';
import A2AConnection from '@components/A2AConnection.astro';

<ModuleHeader
  duration={frontmatter.duration}
  difficulty={frontmatter.difficulty}
  prerequisites={frontmatter.prerequisites}
  objectives={frontmatter.learningObjectives}
  projectStep={frontmatter.projectStep}
/>

## Background
...

<A2AConnection step="What you build">
  How this module connects to the A2A project...
</A2AConnection>

## Exercise
...

<SecurityNote concept="Concept Name" module={X} deepDive="slug-of-deep-dive">
  The security note content...
</SecurityNote>
```

See `src/content/docs/modules/00-setup/index.mdx` for a complete, fully authored example.

## Content Schema

Frontmatter is validated at build time via `src/content/config.ts`. TypeScript will error if required fields are missing or incorrectly typed. This means a contributor can't accidentally merge a module page without learning objectives.

## Deployment

The site deploys automatically via `.github/workflows/pages.yml` on every push to `main` that touches files in `docs/`. You can also trigger a manual deployment from the Actions tab.
