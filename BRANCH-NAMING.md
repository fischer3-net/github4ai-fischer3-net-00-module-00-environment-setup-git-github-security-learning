# Branch Naming Guide

Consistent branch names make pull request lists, CI logs, and `git branch`
output immediately readable — without having to open a branch to understand
its purpose.

---

## The Pattern

```
<type>/<short-description>
```

```bash
# Examples
feat/module-03-pr-template
fix/echo-agent-empty-input
docs/facilitator-guide-timing
translation/es-module-01
chore/update-dependabot-config
security/codeql-custom-queries
release/v1-1-0
```

---

## Prefixes

| Prefix | Use for |
|--------|---------|
| `feat/` | New lesson content, exercises, or starter project capabilities |
| `fix/` | Correcting errors in lessons, broken commands, or bugs |
| `docs/` | README, CONTRIBUTING, facilitator guide, or other repo docs |
| `translation/` | Translated module content — always include the language code |
| `chore/` | Dependency updates, CI config, Dependabot, tooling |
| `test/` | Adding or fixing unit or integration tests |
| `security/` | Security notes, CodeQL config, workflow hardening |
| `refactor/` | Starter project improvements with no behaviour change |
| `release/` | Release preparation — version bumps, changelog |

---

## Rules

### ✅ Do

**Lowercase only.**
```bash
fix/module-03-typo          # ✅
Fix/Module-03-Typo          # ❌ — case-sensitive, creates confusion
```

**Hyphens between words** — never spaces, underscores, or dots.
```bash
feat/search-agent-mock-results    # ✅
feat/search_agent_mock_results    # ❌
```

**Include the module number** for module-specific work.
```bash
fix/module-05-secrets-step-3      # ✅ — immediately obvious which module
fix/actions-secrets               # ⚠️  — acceptable but less specific
```

**Be specific enough to be unique.**
```bash
feat/module-06-dependabot-exercise    # ✅
feat/new-exercise                     # ❌ — which module? which topic?
```

**Keep it short** — 2–5 words in the description.
```bash
feat/module-03-draft-pr-exercise         # ✅
feat/module-03-add-exercise-for-draft-prs-and-review-workflow   # ❌ — too long
```

### ❌ Don't

**Don't use your name or username.**
```bash
feat/module-02-branching    # ✅
jane/module-02-branching    # ❌
```

**Don't use generic names.**
```bash
fix/echo-agent-empty-input  # ✅
fix/bug                     # ❌
bugfix                      # ❌
my-branch                   # ❌
```

**Don't include issue numbers** in the branch name — reference issues in the
PR description instead.
```bash
fix/echo-agent-422-validation    # ✅
fix/issue-142                    # ❌
```

**Don't use `wip/`** — open the PR as a **Draft** instead.

---

## Translation Branches

Always use IETF language codes:

```bash
translation/es-module-00         # Spanish, Module 00
translation/pt-br-module-01      # Portuguese (Brazil), Module 01
translation/fr-module-03         # French, Module 03
translation/ja-module-00         # Japanese, Module 00

# For multi-module translations:
translation/es-modules-00-through-03
translation/pt-br-security-thread
```

---

## Starter Project Branches

Scope to the variant and component:

```bash
feat/python-calculator-agent
feat/nodejs-calculator-agent
fix/python-search-agent-timeout
fix/nodejs-orchestrator-error-handling

# Both variants in one PR:
feat/calculator-agent
fix/schema-request-validation
```

---

## `main` is Protected

`main` is the only permanent branch. It requires:
- Pull Request (no direct pushes)
- At least one approving review
- Passing CI
- Branch up to date with `main`

All other branches are temporary and deleted after merge.

---

## Quick Reference

```
feat/        New content or capability
fix/         Correcting something broken
docs/        Repository documentation
translation/ Translated content (include language code)
chore/       Maintenance and tooling
test/        Test additions or fixes
security/    Security improvements
refactor/    Code quality (no behaviour change)
release/     Release preparation

✅ lowercase · hyphens · 2–5 words · module number for module work
❌ no usernames · no issue numbers · no generic names · no wip/
```

---

## Renaming a Branch Before Pushing

Made a typo or changed your mind before the first push?

```bash
git branch -m old-name new-name
```

After pushing, rename on the remote too:
```bash
git push origin :old-name new-name
git push --set-upstream origin new-name
```

---

*See also: [Branch Naming Reference](docs/src/content/docs/reference/branch-naming.mdx)
in the course docs site for the full version with additional examples.*
