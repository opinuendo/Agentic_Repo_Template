# New to coding? Start here

This folder is for people who have never worked in a software project before (ADR-0005). It
explains the handful of ideas you need to follow this repo, then walks you through your first
change, step by step.

If you already code and know basic git, skip to the [learning path](../learning-path.md).

## The path

1. **[The basics](the-basics.md):** repositories, commits, branches, pull requests, tests and
   checks, in plain words. About 20 minutes.
2. **[Your first contribution](first-contribution.md):** make a real, small change to this repo and
   take it all the way to a merged pull request.
3. **The [learning path](../learning-path.md):** how this repo's particular practices work, with
   exercises.

Keep the [glossary](../glossary.md) open in another tab. Every term in bold in these pages is in it.

## Learning with an AI agent

AI agents are patient tutors: you can ask the same question five times. Two tips:

- **Turn on teaching mode** so your agent explains what it does and why, and links you to the doc
  that covers it. How to turn it on is in [`AGENTS_teaching.md`](../../AGENTS_teaching.md#turning-it-on).
- **Ask "why", not just "how".** "Why does this repo use merge commits?" leads to ADR-0002, where the
  real answer lives. Agents can be confidently wrong; when an agent and a doc disagree, ask a person.

## Going further

This folder only covers what is specific to this repo. For git and GitHub in general, these are
free and widely used:

- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github): a
  hands-on course that runs inside GitHub.
- [The Missing Semester: Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/):
  a one-hour lecture on how git actually works.
- [Pro Git](https://git-scm.com/book/en/v2): the complete book, free online. Chapters 1 to 3 are
  enough to start.

## For maintainers

This folder can be deleted if the repo's team doesn't need it; nothing else depends on it except
the links in [`docs/README.md`](../README.md), the top-level `README.md` and the learning path.
