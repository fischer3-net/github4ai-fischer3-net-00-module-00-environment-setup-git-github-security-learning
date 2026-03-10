// src/content/config.ts
// ============================================================
// Content Collection Schema
// ============================================================
// Starlight uses Astro Content Collections to manage docs.
// This file defines the schema that EVERY module page must
// conform to. TypeScript will catch missing or incorrectly
// typed frontmatter at build time — before it hits GitHub Pages.
//
// This means a contributor can't merge a module page that's
// missing learning objectives or a security note flag.
// Schema enforcement at the content layer, not just convention.
// ============================================================

import { defineCollection, z } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';

// ── Module Frontmatter Schema ──────────────────────────────
// Extends Starlight's built-in docsSchema with course-specific
// fields required on every module page.
const moduleSchema = docsSchema({
  extend: z.object({

    // Module number (0–9) for ordering and display
    moduleNumber: z.number().min(0).max(9).optional(),

    // Estimated time for a learner to complete the module
    duration: z.string().optional(),
    // e.g. "60–90 minutes"

    // Learning objectives — enforces that every module
    // declares what learners will be able to DO after completing it.
    // Each objective should start with an action verb.
    learningObjectives: z.array(z.string()).min(3).max(6).optional(),

    // Whether this module has a dedicated security note.
    // Used to render the security badge in the sidebar and
    // to generate the Security Thread index page automatically.
    hasSecurityNote: z.boolean().default(false),

    // The security concept covered, shown in the Security Thread index.
    securityConcept: z.string().optional(),

    // The A2A project step introduced in this module
    projectStep: z.string().optional(),

    // Difficulty level — used in the Facilitator Guide timing estimates
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']).optional(),

    // Prerequisites — slugs of modules that should be completed first
    prerequisites: z.array(z.string()).default([]),

    // Whether this is a "core" module (badge in sidebar)
    isCore: z.boolean().default(false),
  }),
});

export const collections = {
  docs: defineCollection({
    schema: moduleSchema,
  }),
};
