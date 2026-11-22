# ADR-0002: Layered commits, Conventional Commits, merge commits

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

Agents will produce most changes here, and people will review them. A change that arrives as one
large commit is slow to review and hides how it was reasoned about. A squash merge throws away
whatever structure the commits had, leaving the reasoning only in the PR description on the hosting
service, which is not in anyone's clone.

## Decision

Split each change into commits by type of change, in dependency order, each with a
[Conventional Commits](https://www.conventionalcommits.org/) prefix:

1. `docs(adr):` the decision, if the change introduces or alters a convention
2. `feat(core):` / `fix(core):` shared foundation other code builds on
3. `feat(cli):` / `feat(<tool>):` tooling that uses the foundation
4. `feat(<feature>):` the feature and its tests
5. `docs:` READMEs, onboarding, conventions updated to match
6. `chore:` lockfiles, CI, formatting

Layers the change doesn't touch are skipped. Each commit builds and passes tests on its own where
practical. Pull requests merge with a merge commit, never squashed. The default branch is `main`;
branches are named `<type>/<short-kebab-description>`.

How to restage work done out of order, and a worked example, are in
[`docs/conventions/commits.md`](../conventions/commits.md).

## Consequences

### Positive

- Reviews are faster: each commit is one kind of change, and the decision is read before the code.
- `git log -- <shared directory>` reads as a changelog of that layer.
- One layer can be reverted or bisected on its own.
- Agents follow the order reliably because it is written down and mechanical.

### Negative

- Restaging takes discipline when work happened out of order.
- Merge commits make the `main` graph busier than squash merges.

### Risks and mitigations

- Layering turns into fragmentation (dozens of tiny commits). Mitigation: layer by type, not by file;
  five to eight commits is typical for a substantial change.

## Alternatives considered

- **Squash merges with a detailed PR description.** Rejected: the reasoning would live on the hosting
  service, not in the history.
- **Enforce layer order with tooling.** Not now. A commit-message lint for prefixes is an easy later
  step; the order itself is a review norm.

## Related

- ADR-0001 (the ADR commit comes first)
- [`docs/conventions/commits.md`](../conventions/commits.md)
