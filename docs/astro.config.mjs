// astro.config.mjs
// ============================================================
// Starlight Configuration for GitHub for AI Builders
// ============================================================
// Starlight is an Astro-based documentation framework.
// This file controls the site structure, navigation, theme,
// and all Starlight plugin options.
//
// Full Starlight docs: https://starlight.astro.build
// ============================================================

import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  // The base URL where the site is deployed.
  // The pages.yml workflow passes SITE and BASE_PATH at build time via
  // actions/configure-pages — these fallbacks are used for local dev.
site: process.env.SITE || 'https://github4ai.fischer3.net',
base: process.env.BASE_PATH || '/',

  integrations: [
    starlight({
      title: 'GitHub for AI Builders',
      description:
        'Learn GitHub from zero to mid-level proficiency by building a real Agent-to-Agent AI system. Security practices woven throughout every module.',

      // ── Social / Header Links ──────────────────────────────
      social: {
        github: 'https://github.com/fischer3-net/git-github-security-learning',
      },

      // ── Edit This Page ────────────────────────────────────
      // Adds an "Edit this page" link on every lesson pointing
      // directly to the source file on GitHub. Critical for
      // encouraging contributions from learners.
      editLink: {
        baseUrl:
          'https://github.com/fischer3-net/git-github-security-learning/edit/main/docs/',
      },

      // ── Last Updated ──────────────────────────────────────
      // Shows when each page was last updated. Requires
      // `fetch-depth: 0` in the GitHub Actions checkout step.
      lastUpdated: true,

      // ── Pagination ────────────────────────────────────────
      // Shows Previous / Next module links at the bottom of
      // every page — keeps learners moving through the course.
      pagination: true,

      // ── Table of Contents ─────────────────────────────────
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 3,
      },

      // ── Theme / Color ─────────────────────────────────────
      // Starlight uses CSS custom properties for theming.
      // Custom colors are defined in src/styles/custom.css.
      customCss: ['./src/styles/custom.css'],

      // ── Logo ──────────────────────────────────────────────
      logo: {
        light: './public/logo-light.svg',
        dark: './public/logo-dark.svg',
        replacesTitle: false,
      },

      // ── Favicon ───────────────────────────────────────────
      favicon: '/favicon.svg',

      // ── Head tags ─────────────────────────────────────────
      head: [
        // Open Graph metadata for social sharing
        {
          tag: 'meta',
          attrs: {
            property: 'og:image',
            content: 'https://fischer3-net.github.io/git-github-security-learning/og-image.png',
          },
        },
      ],

      // ── Components ────────────────────────────────────────
      // Override built-in Starlight components with our own.
      // We override the Header to add the course progress indicator.
      components: {
        // Override with custom components when ready:
        // Header: './src/components/overrides/Header.astro',
        // SocialIcons: './src/components/overrides/SocialIcons.astro',
      },

      // ── Sidebar Navigation ────────────────────────────────
      // This controls the left navigation panel.
      // Structure mirrors the modules/ directory in the main repo.
      sidebar: [
        // ── Getting Started ────────────────────────────────
        {
          label: 'Getting Started',
          items: [
            { label: 'Welcome', slug: 'index' },
            { label: 'How This Course Works', slug: 'how-it-works' },
            { label: 'The A2A Project', slug: 'a2a-project' },
          ],
        },

        // ── Modules ───────────────────────────────────────
        {
          label: 'Modules',
          items: [
            {
              label: '00 · Environment Setup',
              slug: 'modules/00-setup',
              badge: { text: 'Start Here', variant: 'tip' },
            },
            {
              label: '01 · Repositories & Commits',
              slug: 'modules/01-repos-and-commits',
            },
            {
              label: '02 · Branching & Merging',
              slug: 'modules/02-branching-and-merging',
            },
            {
              label: '03 · Pull Requests & Code Review',
              slug: 'modules/03-pull-requests',
            },
            {
              label: '04 · Issues, Projects & Discussions',
              slug: 'modules/04-issues-and-projects',
            },
            {
              label: '05 · GitHub Actions & CI/CD',
              slug: 'modules/05-github-actions',
              badge: { text: 'Core', variant: 'note' },
            },
            {
              label: '06 · Security on GitHub',
              slug: 'modules/06-security',
              badge: { text: 'Core', variant: 'note' },
            },
            {
              label: '07 · Collaboration at Scale',
              slug: 'modules/07-collaboration',
            },
            {
              label: '08 · Packages, Releases & Pages',
              slug: 'modules/08-packages-and-releases',
            },
            {
              label: '09 · Capstone Project',
              slug: 'modules/09-capstone',
              badge: { text: 'Final', variant: 'success' },
            },
          ],
        },

        // ── Security Thread ────────────────────────────────
        // A dedicated view of all security notes across modules,
        // useful for educators who want to teach security standalone.
        {
          label: 'Security Thread',
          collapsed: true,
          items: [
            { label: 'Overview', slug: 'security/overview' },
            { label: 'Never Commit Secrets', slug: 'security/never-commit-secrets' },
            { label: 'Branch Protection Rules', slug: 'security/branch-protection' },
            { label: 'Security-Aware Code Review', slug: 'security/code-review' },
            { label: 'Secrets in GitHub Actions', slug: 'security/actions-secrets' },
            { label: 'Dependabot & CodeQL', slug: 'security/dependabot-codeql' },
            { label: 'Supply Chain Security', slug: 'security/supply-chain' },
            { label: 'Release Signing & SBOM', slug: 'security/sbom-attestation' },
          ],
        },

        // ── For Educators ─────────────────────────────────
        {
          label: 'For Educators',
          collapsed: true,
          items: [
            { label: 'Facilitator Guide', slug: 'educators/facilitator-guide' },
            { label: 'Timing & Pacing', slug: 'educators/timing' },
            { label: 'Assessment Rubrics', slug: 'educators/rubrics' },
            { label: 'Classroom Setup', slug: 'educators/classroom-setup' },
            { label: 'Adapting the Course', slug: 'educators/adapting' },
          ],
        },

        // ── Reference ─────────────────────────────────────
        {
          label: 'Reference',
          collapsed: true,
          items: [
            { label: 'Glossary', slug: 'reference/glossary' },
            { label: 'Git Command Cheatsheet', slug: 'reference/git-cheatsheet' },
            { label: 'A2A Message Schema', slug: 'reference/a2a-schema' },
            { label: 'GitHub CLI Cheatsheet', slug: 'reference/gh-cheatsheet' },
          ],
        },

        // ── Contributing ──────────────────────────────────
        {
          label: 'Contributing',
          collapsed: true,
          items: [
            { label: 'How to Contribute', slug: 'contributing/how-to-contribute' },
            { label: 'Content Style Guide', slug: 'contributing/style-guide' },
            { label: 'Writing Security Notes', slug: 'contributing/security-notes' },
            { label: 'Translating Modules', slug: 'contributing/translating' },
          ],
        },
      ],

      // ── Locales / i18n ────────────────────────────────────
      // Root locale is English. Add Spanish and Portuguese when
      // translations are ready. Astro handles locale routing,
      // fallback content, and RTL support automatically.
      defaultLocale: 'root',
      locales: {
        root: {
          label: 'English',
          lang: 'en',
        },
        // Uncomment when translations are ready:
        // es: {
        //   label: 'Español',
        //   lang: 'es',
        // },
        // 'pt-br': {
        //   label: 'Português (Brasil)',
        //   lang: 'pt-BR',
        // },
      },
    }),
  ],
});
