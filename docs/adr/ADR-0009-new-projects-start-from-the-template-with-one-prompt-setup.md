# ADR-0009: New projects start from the GitHub template, set up with one prompt

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

This repo is both a template and a project in its own right. Copied as is, a new project would
inherit things that belong only to the template: a README describing the template, the template's
own proposals and license holder, and a CI check that only makes sense in the template. Setup was a
long manual checklist, which suits neither beginners nor an agent-first repo.

## Decision

- **Starting a project** uses GitHub's template feature (the **Use this template** button, or
  `gh repo create --template`), so each project begins with a clean history.
- **Template-only files live in `template/`**, plus the few files the cleanup script
  names. The top-level `README.md` describes the template; the project README waits in
  `template/project-README.md`.
- **Setup is one prompt.** A person asks their agent to follow "Setting up a new project" in
  [`STARTING_POINT.md`](../../STARTING_POINT.md). The agent asks the questions only a person can
  answer, runs `template/cleanup.sh` for the mechanical part, fills in the placeholders, and commits
  in layers. A person can follow the same steps by hand.
- **The cleanup script refuses to run in the template repo itself**, so the template can't be wiped
  by accident.
- **A template-only CI check** runs the cleanup on a copy in the template repo, so a change that
  breaks setup is caught before anyone uses it.
- New projects keep ADR-0001 to ADR-0009 as `Proposed`, and record their own decisions from
  ADR-0010 onward. This ADR stays as the record of how the project was created.

## Consequences

### Positive

- A new project is ready in minutes, with nothing left over from the template.
- Setup works the same whichever AI tool a person uses, or none.

### Negative

- Changes to the template must keep `template/cleanup.sh` in step. The template-only CI check
  catches most breaks.
- Projects created earlier don't receive later template improvements; GitHub templates copy once.

## Alternatives considered

- **A copy-and-edit checklist only.** Rejected: slow and easy to get wrong, especially for beginners.
- **A setup script that asks every question itself.** Rejected: answers such as the project's
  commands need judgment an agent or person brings; the script does only the mechanical part.
- **A separate "template" branch.** Rejected: GitHub templates copy the default branch, and two
  branches drift.

## Related

- ADR-0005 (beginners use the template too), ADR-0007 (GitHub's template feature), ADR-0008
