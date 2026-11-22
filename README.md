# Agentic Repo Template

A starting point for any new software project in which AI agents write most of the code and people
decide, review, and accept. It works with any language, and it doubles as a place to learn.

**This README describes the template.** When you create a project from it, setup replaces this file
with your project's own README.

## What you get

- **One set of rules for every AI tool**, in [`AGENTS.md`](AGENTS.md), with Claude subagents for
  search, implementation, review and security triage.
- **Decisions written down once**, as ADRs that are never rewritten, so agents stop reopening
  settled questions. Nine starter ADRs explain every choice the template makes:
  [`docs/adr/`](docs/adr/).
- **Layered commits** that make agent-sized changes reviewable, checked by CI.
- **Dependency security**: Dependabot, dependency review and OSV-Scanner find vulnerable packages
  from live databases, and an agent explains each finding and drafts the fix.
- **Teaching built in**: a [learning path](docs/learning-path.md) for people new to these practices,
  a [beginner folder](docs/new-to-coding/) for people new to coding, a shared
  [glossary](docs/glossary.md), and a teaching mode for agents.

## Start a new project

### 1. Create your repo from the template

Either:

- Click **Use this template → Create a new repository** at the top of this page on GitHub, or
- run this, replacing `my-project`:

```bash
gh repo create my-project --template opinuendo/Agentic_Repo_Template --private --clone
```

Use `--public` instead of `--private` for a public project. Your new repo starts with a clean
history.

### 2. Set it up

Open the new repo with your AI agent and say:

> Set up this project by following "Setting up a new project" in STARTING_POINT.md.

The agent asks you a few questions (project name, language and commands, license holder), removes
the template-only files, fills in the placeholders, and commits the result in layers. It takes a
few minutes.

No agent? Follow the same steps yourself:
[Setting up a new project](STARTING_POINT.md#setting-up-a-new-project).

### 3. Turn on the GitHub settings

GitHub doesn't copy repository settings from a template. The setup steps list the few the
conventions depend on, such as merge commits and Dependabot.

## Learn more

- [`STARTING_POINT.md`](STARTING_POINT.md): how the template is organized and why.
- [`docs/adr/`](docs/adr/): every decision behind it, with the alternatives that lost.
- New to coding? [`docs/new-to-coding/`](docs/new-to-coding/).

## Improving the template

Changes to the template itself follow its own rules: see [`CONTRIBUTING.md`](CONTRIBUTING.md). If you
add a file that belongs only to the template, add it to [`template/cleanup.sh`](template/cleanup.sh).
