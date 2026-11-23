# Agent rules: teaching

Loaded only through the Agent files table in [`AGENTS.md`](AGENTS.md#agent-files), when teaching mode
is on or someone is learning. Teaching mode is off by default (ADR-0005).

## Turning it on

A learner adds a line saying "Use teaching mode from AGENTS_teaching.md" to their own tool's
personal, git-ignored instructions (for Claude, see [`CLAUDE.md`](CLAUDE.md)). It's personal so one
learner's setting never changes anyone else's agent (ADR-0003).

## When it is on

- Before acting, say in a sentence what you are about to do and why.
- After acting, explain what changed in plain words, and link the glossary entry, ADR or doc that
  covers it.
- Show the command you ran and what it did, so the learner can run it themselves next time.
- Never simplify the code itself to make it easier to explain. The code meets the same bar either
  way.

## Where learners start

- Complete beginners: [`docs/new-to-coding/`](docs/new-to-coding/).
- People who can code but are new to these practices: [`docs/learning-path.md`](docs/learning-path.md).
- Terms: [`docs/glossary.md`](docs/glossary.md), the one place they are defined. Link to it rather
  than defining a term again.
