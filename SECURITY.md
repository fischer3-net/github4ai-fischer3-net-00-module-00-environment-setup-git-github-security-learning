# Security Policy

## Supported Versions

The following versions of the **starter project** code receive security fixes:

| Version | Supported |
|---------|-----------|
| Latest release (`main` branch) | ✅ Yes |
| Older tagged releases | ❌ No — please upgrade |

> Course content (lesson Markdown files) does not have versioned security support.
> If you find a security issue in lesson content — for example, an exercise that
> teaches an insecure pattern — please report it using the process below.

---

## Reporting a Vulnerability

**Please do not report security vulnerabilities via public GitHub Issues.**

Public issues are visible to everyone, including anyone who might exploit the
vulnerability before it can be fixed.

### Preferred method — GitHub Private Vulnerability Reporting

Use GitHub's built-in private reporting tool:

1. Go to the **[Security tab](../../security)** of this repository
2. Click **"Report a vulnerability"**
3. Fill out the form with as much detail as you can

This creates a private Security Advisory that is only visible to you and the
repository maintainers. We can collaborate on a fix before anything is disclosed
publicly.

### What to include

A useful vulnerability report includes:

- **What** the vulnerability is (e.g., "the CI workflow is vulnerable to script
  injection via pull request titles")
- **Where** it exists (file path, line number, or workflow step)
- **How** it could be exploited (steps to reproduce or a proof-of-concept)
- **Impact** — what could an attacker do if they exploited this?
- **Suggested fix** (optional but very welcome)

---

## Response Timeline

| Milestone | Target |
|-----------|--------|
| Acknowledgement of report | Within 48 hours |
| Initial assessment | Within 7 days |
| Fix or mitigation | Within 14 days for critical; 30 days for moderate |
| Public disclosure | Coordinated with reporter after fix is released |

We follow responsible disclosure: we'll coordinate the timing of any public
announcement with you, and will credit you in the release notes unless you
prefer to remain anonymous.

---

## Scope

### In scope

- Security vulnerabilities in the **starter project code** (`starter-project/`)
- GitHub Actions **workflow vulnerabilities** — script injection, excessive
  permissions, unpinned actions (`.github/workflows/`)
- **Secret handling** issues — anything that could cause learner secrets to be
  exposed
- **Supply chain** issues — compromised dependencies or malicious packages

### Out of scope

- Theoretical vulnerabilities with no realistic attack path
- Issues in third-party dependencies (report these to the dependency maintainer
  directly; Dependabot will also catch most of these automatically)
- Social engineering or phishing (outside the scope of this project)

---

## This Policy Is a Teaching Example

One of the goals of this course is to model excellent GitHub security practices.
This `SECURITY.md` file, the private vulnerability reporting workflow, and the
GitHub Actions security configurations are all intentional teaching artifacts.

If you are a learner and want to practice the responsible disclosure process,
Module 04 covers GitHub's private vulnerability reporting in detail, and you
are welcome to submit a real report on a real (non-critical) issue you find
in the course material. We will treat it as a genuine contribution.
