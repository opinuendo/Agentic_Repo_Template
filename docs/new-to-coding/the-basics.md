# The basics

Six ideas cover almost everything you'll meet in this repo. Each has a longer definition in the
[glossary](../glossary.md).

## 1. A repository is a project with a memory

A **repository** (repo) is a folder of files plus the full history of every change ever made to
them. Nothing is lost: any earlier version can be looked at or brought back. This repo lives on
GitHub, and you work on your own **clone** of it, a full copy on your computer.

## 2. A commit is a saved step

A **commit** is a snapshot of some changes with a message saying what changed. You make a few
changes, then commit them. The history of a repo is a chain of commits.

This repo writes commit messages in a fixed shape called **Conventional Commits**: a type first,
such as `docs:` for documentation or `fix:` for a bug fix.

```text
docs: explain how to run the tests
```

## 3. A branch keeps your work separate

`main` is the branch holding the working, reviewed version of the project. You never change it
directly. Instead you make a **branch**, a separate line of work, and commit there. If something
goes wrong, `main` is untouched.

## 4. A pull request asks for your work to be merged

When your branch is ready, you **push** it to GitHub and open a **pull request** (PR). A PR shows
your **diff**, the lines you added and removed, and invites **review**: someone else reads your
change before it is **merged** into `main`.

Review isn't a test you pass or fail. It is how a team catches what the person who wrote a change
couldn't see.
Everyone's work gets review comments, including the most experienced people's.

## 5. Checks run on every pull request

When you open a PR, GitHub runs **CI** (continuous integration): automatic checks such as **tests**
(code that checks other code gives the right answer) and **lint** (a check for style problems and
likely mistakes). This repo also checks your commit messages and scans for known security problems
in the packages it uses.

A red cross means a check failed. Click it to read why; the message usually says what to fix.

## 6. Decisions are written down

Whenever this repo made a choice that isn't obvious, someone wrote an **ADR**, a short file saying
what was decided, why, and what was rejected. If you wonder "why is it done this way?", the answer
is in [`docs/adr/`](../adr/).

---

Next: [your first contribution](first-contribution.md).
