## What does this PR do?

<!-- 
  Provide a clear, concise summary of your changes.
  What problem does it solve, or what does it add?
-->



## Related Issue

Closes #<!-- issue number -->

<!-- 
  Every PR should be linked to an issue.
  If one doesn't exist, please open an issue first.
  Small fixes (typos, broken links) may skip this requirement.
-->

---

## Type of Change

<!-- Check all that apply -->

- [ ] 🐛 **Lesson fix** — correcting an error, broken command, or inaccuracy
- [ ] 📝 **Content improvement** — clearer explanation, better example, formatting
- [ ] 💡 **New exercise or solution** — adding to an existing module's `exercises/` or `solutions/`
- [ ] 🧩 **New module** — adding a full new module (must have prior Discussion + Issue approval)
- [ ] 🤖 **Starter project** — changes to `starter-project/python/` or `starter-project/nodejs/`
- [ ] 🔐 **Security note** — adding or updating a module's `security-note.md`
- [ ] 🌍 **Translation** — adding or updating translated content
- [ ] 🔧 **Chore** — CI, tooling, Dependabot, dependencies (no lesson content changes)
- [ ] 📚 **Documentation** — README, CONTRIBUTING, facilitator guide, or other docs

---

## Module(s) Affected

<!-- List the modules this PR touches, e.g.: Module 03, Module 05, Starter Project -->



---

## Checklist

### All PRs

- [ ] I have read [CONTRIBUTING.md](../CONTRIBUTING.md)
- [ ] My branch name follows the `type/short-description` convention (e.g., `fix/module-03-typo`)
- [ ] My commits follow the Conventional Commits format
- [ ] CI checks are passing (or I've explained failures below)
- [ ] I have linked this PR to a related issue above

### Lesson Content Changes

- [ ] The content matches the voice and structure described in the Content Style Guide
- [ ] New commands or code have been tested and work as described
- [ ] Any new links are valid and point to stable URLs
- [ ] Screenshots (if any) include alt text and are stored in the module's `images/` folder
- [ ] Any new GitHub feature references use the correct capitalization (e.g., "GitHub Actions", not "github actions")

### New Exercises

- [ ] The exercise is grounded in the Agent-to-Agent (A2A) starter project
- [ ] A corresponding solution is included in `solutions/`
- [ ] The exercise includes a goal statement, step-by-step instructions, expected output, and a hint

### Security Notes

- [ ] The security note covers exactly one concept
- [ ] It is specifically connected to AI development risk, not generic security advice
- [ ] It is actionable — learners can apply it to the starter project
- [ ] It is between 100–300 words

### Starter Project Changes

- [ ] No secrets, API keys, or credentials are hardcoded
- [ ] A `.env.example` is included for any new environment variables
- [ ] Unit tests are included for new agent logic
- [ ] The agent is registered in the Orchestrator's routing table
- [ ] Changes work in both Python and Node.js variants (or are clearly scoped to one)
- [ ] `CODEOWNERS` is updated if the change introduces a sensitive new capability

### Translations

- [ ] The translation follows the directory structure: `translations/[language-code]/modules/...`
- [ ] Only content (not code, filenames, or CLI commands) has been translated
- [ ] The translated module is complete — not partial

---

## Testing

<!-- 
  How did you test your changes?
  For starter project changes: describe how you ran the project locally.
  For lesson content: describe how you validated commands and exercises.
-->



---

## Screenshots or Output (if applicable)

<!-- 
  For UI changes, updated screenshots, or new exercises, 
  paste relevant output or screenshots here to help reviewers.
-->



---

## Anything else reviewers should know?

<!-- 
  Open questions, known limitations, follow-up issues planned, 
  or anything that would help the reviewer understand context.
-->

