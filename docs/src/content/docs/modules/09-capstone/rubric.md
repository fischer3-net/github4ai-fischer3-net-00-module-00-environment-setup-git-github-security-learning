---
title: Capstone Rubric
---

# Module 09 Capstone — Assessment Rubric

**For educators and instructors assessing Capstone submissions.**

Each dimension is scored 0–4. Maximum score: **20 points**.
A score of **16 or above (80%)** demonstrates mid-level GitHub proficiency.

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| **4** | Exemplary — exceeds expectations, no corrections needed |
| **3** | Proficient — meets expectations with minor gaps |
| **2** | Developing — meets some expectations, clear gaps remain |
| **1** | Beginning — attempted but significant gaps |
| **0** | Not demonstrated — missing or incorrect |

---

## Dimension 1 — GitHub Workflow (4 points)

Assesses whether the learner followed the full contribution process
independently, without prompts.

| Score | Evidence |
|-------|---------|
| **4** | Discussion opened and linked from Issue. Issue has title, description, and acceptance criteria. Feature branch named per `BRANCH-NAMING.md`. At least 3 Conventional Commits. PR template fully completed. CI was green when review was requested. All review comments addressed before merge. Branch deleted after merge. Issue moved to Done on Projects board. |
| **3** | All of the above, with 1–2 minor gaps (e.g., branch name slightly off convention, one PR template section thin but present). |
| **2** | PR opened without a Discussion or prior Issue. Or PR template partially blank. Or branch not deleted. Or review comments not all addressed. |
| **1** | Significant workflow gaps — e.g., PR opened with no description, pushed directly to `main`, or CI was failing when review was requested. |
| **0** | No PR opened, or work not submitted via the GitHub workflow at all. |

**What to check:**
- [ ] Discussion exists and is linked from the Issue
- [ ] Issue has all three sections: background, what to do, acceptance criteria
- [ ] Branch name matches `feat/<short-description>` or equivalent
- [ ] At least 3 commits with Conventional Commits format
- [ ] PR template: all sections filled, no placeholder text
- [ ] CI status was green when review was requested (check PR timeline)
- [ ] All review conversations marked resolved
- [ ] Branch deleted (check branch list — it should not appear)
- [ ] Issue in Done column on Projects board

---

## Dimension 2 — Code Quality (4 points)

Assesses whether the agent implementation is correct, follows A2A
conventions, and is readable by someone who didn't write it.

| Score | Evidence |
|-------|---------|
| **4** | Agent routes correctly on its `task` keyword. Both `/health` and `/run` implemented. Success and error paths return the correct `AgentResponse` types. Error handling covers all failure modes with descriptive messages. Code follows the structure and naming patterns of existing agents. `README.md` present with working `curl` example. |
| **3** | All of the above with minor issues (e.g., one error path returns a vague message, or the README example needs a small correction to work). |
| **2** | Agent works for the happy path but error handling is incomplete — some failures produce a 500 or an unhandled exception. Or the agent doesn't follow A2A conventions (e.g., missing `/health`, different response schema). |
| **1** | Agent implementation is incomplete or incorrect — the happy path doesn't work as described. |
| **0** | No agent implementation submitted. |

**What to check:**
- [ ] `GET /health` returns `{"agent": "<n>", "status": "healthy"}`
- [ ] `POST /run` accepts A2A schema: `task`, `input`, optional `request_id`
- [ ] Valid input returns `AgentResponse.success()` with correct `output`
- [ ] Invalid input returns `AgentResponse.error()` with descriptive `error`
- [ ] Empty `input` handled — returns error, not 500
- [ ] Port read from environment variable with sensible default
- [ ] Registered in `AGENT_REGISTRY`
- [ ] Added to `.env.example` with placeholder values
- [ ] `agents/<n>/README.md` present with usage and curl example

---

## Dimension 3 — Test Coverage (4 points)

Assesses whether the test suite gives a reviewer confidence in the
agent's behaviour without running it manually.

| Score | Evidence |
|-------|---------|
| **4** | At least 6 tests. Covers: health endpoint, successful request, error case, empty input, and at least 2 edge cases specific to the agent's domain. All tests pass. Tests are readable — test names describe what's being tested. |
| **3** | 5–6 tests, all passing. Edge cases present but one is a near-duplicate of another rather than a genuinely distinct scenario. |
| **2** | 4–5 tests, or 6+ tests but all passing only the happy path. Or one test is failing. |
| **1** | Fewer than 4 tests, or tests present but multiple failures. |
| **0** | No tests submitted, or all tests failing. |

**What to check:**
- [ ] Test file exists and named `test_<agent>.py`
- [ ] `pytest tests/ -v` passes with no failures
- [ ] Health endpoint tested
- [ ] Successful request tested with expected output
- [ ] Error case tested (invalid or unparseable input)
- [ ] Empty input tested
- [ ] At least 2 edge cases specific to the agent's domain
- [ ] Test names are descriptive (not `test_1`, `test_2`)

**Example edge cases by agent type:**
- Word Count: Unicode text, text with only punctuation, single word
- Unit Converter: Unknown unit, zero value, negative value, fractional input
- Weather: Unknown city, city name with accents, city name with spaces
- Calculate: Division by zero, very large numbers, expression with no operators

---

## Dimension 4 — Security Practices (4 points)

Assesses whether the learner applied the security practices from
Modules 00–08 independently, without prompts.

| Score | Evidence |
|-------|---------|
| **4** | No secrets or API keys hardcoded anywhere in the diff. `eval()` not used on user input — safe parsing demonstrated. External API calls (if any) have timeouts and handle failures gracefully. Input validation documented with a code comment explaining what's checked and why. CODEOWNERS triggered the correct reviewer for Orchestrator changes. |
| **3** | All of the above with one minor gap (e.g., no code comment documenting input validation, but the validation itself is correct). |
| **2** | No hardcoded secrets, but one security practice missing or incomplete — e.g., `eval()` used on user input, or external API call with no timeout, or no input validation. |
| **1** | Multiple security practices missing. Or a hardcoded secret found in the diff (even if later removed). |
| **0** | Hardcoded secret pushed to the repository and not removed. Or `eval()` used directly on user input with no sanitisation. |

**What to check:**
```bash
# Run on the PR branch before reviewing code
git log --all -p | grep -iE "(api_key|secret|token|password)\s*="
grep -r "eval(" starter-project/python/agents/<new-agent>/
```

- [ ] No secrets in the diff (run the grep above)
- [ ] `eval()` not used on user input anywhere in the agent
- [ ] If external API called: timeout set, failure handled as `AgentResponse.error()`
- [ ] If URL configurable: validation against expected hosts (SSRF consideration)
- [ ] Input validation present and commented
- [ ] CODEOWNERS review request triggered for Orchestrator changes
- [ ] New dependency (if any) pinned to a specific version in `requirements.txt`

---

## Dimension 5 — Release & Documentation (4 points)

Assesses whether the learner completed the full distribution pipeline
and left a permanent public record of the contribution.

| Score | Evidence |
|-------|---------|
| **4** | New minor version tag pushed following semver. Release pipeline completed — GitHub Release visible with auto-generated notes and SBOM attached. `gh attestation verify` passes on the published image. Docs site updated — agent mentioned in `how-it-works.mdx`. Pages workflow completed — change visible on the live site. Showcase Discussion posted with link to merged PR. |
| **3** | All of the above with one gap — e.g., Showcase post missing, or docs update is present but thin. |
| **2** | Tag pushed and release created, but attestation verification not run, or docs site not updated, or Pages deployment not confirmed. |
| **1** | No release tag pushed. Or release pipeline failed and not fixed. |
| **0** | No release attempted. |

**What to check:**
- [ ] Tag follows semver: `v1.1.0` (or appropriate increment)
- [ ] `git tag -n` shows annotated tag with a meaningful message
- [ ] GitHub Release visible at `/releases/tag/v1.1.0`
- [ ] Release notes auto-generated from PR history
- [ ] SBOM (`sbom.spdx.json`) attached to release
- [ ] Docker images visible on Packages tab
- [ ] `gh attestation verify` output shows all checks passed (ask learner to share output)
- [ ] `docs/src/content/docs/how-it-works.mdx` updated
- [ ] Pages deployment shows the update on the live site
- [ ] Showcase Discussion posted in Discussions

---

## Score Sheet

| Learner | Workflow | Code | Tests | Security | Release | **Total** |
|---------|----------|------|-------|----------|---------|-----------|
| | /4 | /4 | /4 | /4 | /4 | **/20** |

---

## Feedback Templates

### For a strong submission (16–20)

> Well done on the Capstone. Your PR description was clear, the test
> coverage was thorough, and the security practices were applied correctly
> and documented. One area to develop further: [specific item]. Overall
> this demonstrates mid-level GitHub proficiency — you're ready to
> contribute to real open-source projects using this workflow.

### For a developing submission (10–15)

> Good effort on the Capstone — you completed the full workflow, which
> many learners find challenging. A few areas need attention before this
> demonstrates mid-level proficiency: [specific gaps from rubric]. I'd
> encourage you to address [most important gap] and resubmit for
> reassessment.

### For a beginning submission (<10)

> Thank you for submitting the Capstone. The submission isn't yet at the
> level that demonstrates mid-level GitHub proficiency — specifically:
> [top 2–3 gaps from rubric]. I'd suggest revisiting [relevant modules]
> and resubmitting. The contribution process is the hardest part to get
> right independently — it's expected that the first attempt has gaps.

---

## Notes for Educators

**Timing.** The Capstone is designed for 3–4 hours of independent work.
In a classroom setting, consider giving learners 1–2 class periods plus
a week of async time before assessment. The PR review cycle adds at least
one round-trip even in fast-moving cohorts.

**Peer review.** Require learners to review at least one other learner's
PR before their own is merged. This gives both parties practice on the
reviewer side of Module 07, and surfaces issues in the codebase that a
self-review misses. Count peer review participation in the Workflow dimension.

**Resubmission.** The rubric is designed to support reassessment. A learner
who scores 12 on first submission should be able to address the specific
gaps and resubmit without redoing the entire project. Accept a follow-up
PR that fixes the identified issues and re-score only the affected dimensions.

**The Showcase Discussion.** Make the Showcase post a required part of
completion, not optional. The discipline of writing a clear public summary
of your own work — "what I built, what was hard, what I'd do differently" —
is itself a GitHub skill. It's also how open-source maintainers evaluate
whether a contributor understands their own contribution.
