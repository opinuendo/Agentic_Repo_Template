# ADR-0007: GitHub is the only supported host

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

The starter files carried rules and paths for both GitHub and GitLab. The template is hosted on
GitHub, its security setup (ADR-0006) uses GitHub features, and every alternative is one more thing
a beginner must work out they can ignore. Several conventions also only work if the host is
configured to support them.

## Decision

Support GitHub only. Remove the GitLab rules and paths, and list the repo settings the conventions
depend on in `STARTING_POINT.md`'s setup steps:

- Allow merge commits and turn off squash merging, so the layers survive (ADR-0002).
- Protect `main`: changes arrive through PRs, with CI and dependency review as required checks.
- Turn on the dependency graph, Dependabot alerts and security updates, secret scanning, push
  protection, and private vulnerability reporting (ADR-0006).

On private repos, protecting `main` needs a paid GitHub plan, secret scanning and dependency review
need GitHub's paid security products, and private vulnerability reporting isn't available (so
`SECURITY.md` names a contact instead). Without them, review is the safeguard.

## Consequences

### Positive

- One host to explain, and settings beginners can follow step by step.

### Negative

- A team on GitLab must adapt the PR template, workflows and settings itself.

## Alternatives considered

- **Keep GitHub and GitLab side by side.** Rejected for now: twice the setup to explain and test. A
  later ADR can add GitLab back.

## Related

- [Proposal: teaching, dependency security, and GitHub](../proposals/2026-11-22-teaching-security-and-github.md)
- ADR-0002, ADR-0006
