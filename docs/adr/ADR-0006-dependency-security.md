# ADR-0006: Tools detect vulnerable dependencies; an agent triages; people decide

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

Most code in a modern project comes from third-party packages, and new vulnerabilities in them are
published daily as CVEs (Common Vulnerabilities and Exposures). An AI model can't track them alone,
because its knowledge stops at its training date. Tools that read live vulnerability databases can,
but their alerts don't say whether a vulnerability matters in this repo, and a beginner may not know.

## Decision

Detection comes from tools that read live databases. An agent explains and drafts fixes. A person
decides.

- **Dependabot alerts and security updates** are turned on in the repo settings.
  [`.github/dependabot.yml`](../../.github/dependabot.yml) keeps GitHub Actions up to date from day
  one and has a commented block for the repo's package manager. Its commit prefix is `chore(deps)`.
- **[Dependency review](../../.github/workflows/dependency-review.yml)** runs on every PR and fails one
  that adds a dependency with a known vulnerability. It is a required check on `main` wherever branch
  protection is available (ADR-0007).
- **[OSV-Scanner](../../.github/workflows/osv-scanner.yml)** scans lockfiles on PRs, on pushes to
  `main`, and weekly, so CVEs published after a merge are still caught. It skips cleanly until the
  repo has a lockfile.
- **Secret scanning with push protection** is turned on in the repo settings.
- **[`SECURITY.md`](../../SECURITY.md)** tells outsiders how to report a vulnerability privately.
- **The `security` subagent** (most capable tier, ADR-0004) reads open alerts with `gh`, judges whether
  the vulnerable code is used here, explains the risk in plain words, and drafts a fix on a branch as
  a `fix(deps):` commit. It never dismisses an alert, asks before pushing like any agent, and trusts
  the alert databases over its own memory. The rules that must never be missed are in `AGENTS.md`;
  the detail is in `AGENTS_security.md` (ADR-0003).

Third-party actions are pinned to a full commit SHA with the version in a comment, and Dependabot
updates the pins. A tag can be moved to point at different code; a commit SHA can't.

## Consequences

### Positive

- New CVEs are noticed within a week, without anyone remembering to check.
- Each alert arrives with a plain-words explanation and a drafted fix, which helps beginners most.
- No part of detection depends on one AI tool.

### Negative

- On private repos, dependency review and secret scanning need GitHub's paid security products,
  and private vulnerability reporting isn't available. The dependency review workflow skips on
  private repos unless the repo variable `HAS_CODE_SECURITY` is `true`.
- More PRs to review, from Dependabot and the subagent.

### Risks and mitigations

- The agent misjudges an alert as harmless. Mitigation: it never dismisses alerts; a person does.

## Alternatives considered

- **An AI agent alone, on demand or scheduled.** Rejected: its knowledge goes stale, and nothing runs
  unless someone remembers.
- **Tools alone, no agent.** Workable, but beginners get alerts with no explanation, and fixes wait
  for a person to write them.
- **A scheduled agent task that triages weekly.** Not now: it ties the setup to one AI tool. A team
  can add one later with its own ADR.

## Related

- [Proposal: teaching, dependency security, and GitHub](../proposals/2026-11-22-teaching-security-and-github.md)
- ADR-0004 (model tiers and what agents may do), ADR-0007 (the GitHub settings this relies on)
