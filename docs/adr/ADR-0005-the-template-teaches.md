# ADR-0005: The template teaches its practices, and the basics to beginners

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

The starter docs give the reason for every rule, which suits people who already know what a commit,
a pull request (PR) or continuous integration (CI) is. Nothing tells a newcomer what to read first,
and nothing serves someone new to coding. Leaving teaching to each learner's AI agent falls short:
a beginner doesn't know what to ask, agents keep no memory between sessions, and nobody reviews an
agent's explanation the way a doc is reviewed.

## Decision

Docs set the order and the vocabulary; agents explain in context and point back to the docs.

- **[`docs/learning-path.md`](../learning-path.md)** gives people who can code a reading order and
  three hands-on exercises.
- **[`docs/new-to-coding/`](../new-to-coding/)** walks complete beginners through the basics and a
  first contribution. It covers only what is specific to this repo and links to well-known outside
  tutorials for general git. Teams that don't need it delete the folder.
- **[`docs/glossary.md`](../glossary.md)** is the one place terms are defined. Other docs link to it
  instead of defining a term again.
- **Teaching mode** is defined in `AGENTS.md`, so it means the same thing in every tool. Each learner
  switches it on in their own tool's personal, git-ignored instructions (for Claude,
  `CLAUDE.local.md` or user memory). It is off by default.

## Consequences

### Positive

- People who can code learn the practices from the files they will work in.
- Beginners get one fixed path and one vocabulary, whatever agent they use.
- One learner's teaching mode never changes anyone else's agent (ADR-0003).

### Negative

- More docs to keep current. The beginner folder is kept small and links out to limit this.
- Teaching mode depends on each tool honoring personal instructions.

## Alternatives considered

- **Let each learner's agent do all the teaching.** Rejected: no fixed path, no memory, nothing
  reviewed.
- **A full course covering git and programming from scratch.** Rejected: a lot to maintain, and good
  free tutorials already exist.
- **Teaching mode on for everyone by default.** Rejected: experienced contributors would pay for
  explanations they don't need on every task.

## Related

- [Proposal: teaching, dependency security, and GitHub](../proposals/2026-11-22-teaching-security-and-github.md)
- ADR-0003 (personal settings stay out of the repo)
