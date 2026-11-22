# ADR-0008: Baseline hygiene: CONTRIBUTING, CI, commit check, editorconfig

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

Several common practices were missing. `STARTING_POINT.md` cited a `CONTRIBUTING.md` that didn't
exist. The definition of done relied on agents running the checks themselves, with nothing to
enforce it. ADR-0002 named a commit-message check as an easy later step. Editors and agents had no
shared settings for indentation and line endings.

## Decision

- **[`CONTRIBUTING.md`](../../CONTRIBUTING.md)** gives contributors the git rules in a few lines, citing
  ADR-0002 and linking to [`docs/conventions/commits.md`](../conventions/commits.md).
- **[`.github/workflows/ci.yml`](../../.github/workflows/ci.yml)** runs the install, lint, test and build
  commands on every PR and push to `main`. While a command is still unset it skips that step with a
  warning, so a fresh copy of the template passes on day one.
- **The same workflow checks commit messages** in a PR for Conventional Commits prefixes, skipping
  merge commits, whose messages ADR-0002 itself requires.
- **[`.editorconfig`](../../.editorconfig)** sets UTF-8, LF line endings, a final newline, and
  trailing-whitespace trimming for every editor that supports it.

## Consequences

### Positive

- The definition of done is enforced by CI, not only by agents' honesty.
- Commit prefixes are checked by a tool rather than by reviewers.

### Negative

- The commands appear in both `AGENTS.md` and `ci.yml`. Both say so and point to the other; a change
  to one must change the other.
- Skipping unset commands means CI proves nothing until they are filled in.

## Alternatives considered

- **CI fails while commands are placeholders.** Rejected: a template that fails on day one teaches
  people to ignore red checks.
- **A commit-lint tool such as commitlint.** Not now: it adds a language runtime and config to a
  template meant to suit any stack. A short shell check does the job.

## Related

- [Proposal: teaching, dependency security, and GitHub](../proposals/2026-11-22-teaching-security-and-github.md)
- ADR-0002 (commit conventions), ADR-0004 (definition of done)
