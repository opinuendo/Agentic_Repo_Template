# Teaching, dependency security, and GitHub as the only host

- **Status:** Accepted by opinuendo on 2026-11-22; recorded by an agent at their request
- **Date:** 2026-11-22
- **Written by:** opinuendo
- **Audience:** anyone deciding whether to adopt this template, including readers new to software
  development

## Summary

This proposal makes the template do three new things.

- **Teach.** People who already code can learn its practices from it, and complete beginners can
  learn the basics from a separate folder.
- **Watch for vulnerable dependencies.** Automated tools check for newly published vulnerabilities
  (CVEs), and an AI agent explains each finding and drafts the fix.
- **Target GitHub only.** The GitLab alternatives come out, which keeps the template simpler for
  beginners.

## Problem

**The template explains its rules but doesn't teach them.** Every rule carries its reason, which
suits someone who already knows what a commit, a pull request (PR) or continuous integration (CI)
is. Nothing tells a newcomer what order to read things in, and nothing at all serves someone new to
coding. Leaving it to each learner's AI agent isn't enough:

- A beginner doesn't know what to ask, so gaps stay hidden.
- Agents keep no memory between sessions, so explanations and terms change from day to day.
- Nobody reviews an agent's explanation. A doc is reviewed once and is then right for everyone.

**Nothing watches for security problems in dependencies.** Most code in a modern project comes from
third-party packages. New vulnerabilities in those packages are published every day as CVEs
(Common Vulnerabilities and Exposures). Nothing in the template notices them, and an AI model can't
do it alone, because its knowledge stops at its training date.

**The template mentions two hosts, GitHub and GitLab.** `.claude/settings.json`, `.claude/README.md`
and `STARTING_POINT.md` carry rules and paths for both. Every alternative is one more thing a
beginner has to work out they can ignore.

## Proposed design

### 1. Teaching

**For people who can code but are new to these practices.**

- The existing docs already explain each rule's reason, which is the hard part. These readers don't
  need a separate course.
- A short `docs/learning-path.md` lists what to read, in order: `README.md`, `STARTING_POINT.md`,
  `AGENTS.md`, ADR-0001 to ADR-0004, then `docs/conventions/commits.md`.
- The same page has three exercises, each done on a throwaway branch:
  - write a practice ADR
  - clean up a messy branch into layered commits
  - review a PR with the `reviewer` subagent

**For complete beginners: `docs/new-to-coding/`.**

- One self-contained folder that walks through what a repository, commit, branch, PR, test and CI
  are. It ends with a first contribution made in this repo, step by step.
- It covers only what is specific to this repo. For general git basics it links to well-known
  outside tutorials rather than rewriting them, because a rewritten tutorial goes stale.
- Teams that don't need it delete the folder. `STARTING_POINT.md` says so.

**One shared glossary: `docs/glossary.md`.**

- Covers terms such as commit, branch, PR, merge commit, ADR, CI, CVE, subagent and model tier.
- Every other doc links to it instead of defining a term again, following the rule against
  restating a canonical definition in `AGENTS.md`.

**Teaching mode for agents, switched on per person.**

- `AGENTS.md` defines teaching mode in a few lines:
  - explain what you did and why, in plain words
  - link the glossary entry or doc that covers it
  - never simplify the code itself to make it easier to explain
- Each learner switches it on in their own tool's personal, git-ignored instructions: for Claude,
  `CLAUDE.local.md` or user memory; for other tools, their equivalent. Personal preferences stay out
  of the repo (ADR-0003), so one learner's setting never changes another person's agent. Because
  the definition lives in `AGENTS.md`, it means the same thing in every tool.

### 2. Dependency security: tools detect, an agent triages

Detection comes from tools that read live vulnerability databases. Judgment and explanation come
from an agent.

| Piece | What it does | Why this piece |
|---|---|---|
| Dependabot alerts and security updates (repo settings) | GitHub checks dependencies against its advisory database, alerts, and opens a PR to upgrade a vulnerable one | Built into GitHub and free on every plan |
| Dependency review on every PR (GitHub Action, set as a required check) | Fails a PR that adds a dependency with a known vulnerability | Stops a problem before it reaches `main`. Free on public repos; private repos need GitHub's paid code security product |
| OSV-Scanner in CI, on PRs and weekly (GitHub Action) | Scans lockfiles against the open-source OSV database | A second, free database on any plan, and the weekly run catches CVEs published after code was merged |
| Secret scanning with push protection (repo setting) | Refuses a push that contains a credential in a format GitHub recognizes | A leaked key can be used by anyone who finds it, and history keeps it even after a later commit deletes it. Free on public repos; private repos need GitHub's paid secret protection product |
| `security` subagent (most capable tier) | Reads open alerts, judges whether the vulnerable code is actually used here, explains the risk in plain words, and drafts a fix on a branch | Judging real-world risk needs the most capable tier (ADR-0004) |
| `SECURITY.md` | Tells outsiders how to report a vulnerability privately | Standard practice; GitHub links to it |

Rules for the `security` subagent. The rules go in `AGENTS.md`, so any tool's agent follows them;
only the Claude definition goes in `.claude/agents/` (ADR-0003).

- It never dismisses an alert. It asks before pushing or opening a PR, like any agent (ADR-0004).
- It reads alerts through the GitHub command-line tool (`gh`), signed in as the person running it.
  Reading alerts is read-only and handles no secrets, so it needs no extra approval.
- It treats the alert databases as the source of truth, not its own memory, because a model's
  knowledge stops at its training date.
- Its fix branch follows layered commits, usually a single `fix(deps):` commit. This adds `deps` to
  the scopes listed in `AGENTS.md`.

**Configuration.** Each language has its own package manager, and GitHub rejects a
`dependabot.yml` that names an unknown one. So the template ships
`.github/dependabot.example.yml`, which adopters copy to `dependabot.yml` once they pick a stack. It
sets the commit-message prefix to `chore(deps)` so Dependabot's PRs pass the commit-message check.
The scanners need no setup until the repo has a lockfile.

### 3. GitHub as the only host

- Remove the `glab` rules from `.claude/settings.json` and `.claude/README.md`.
- Remove the GitLab merge request template path from `STARTING_POINT.md`.
- Repo settings that the conventions depend on are listed in `STARTING_POINT.md`'s adoption steps:
  - allow merge commits and turn off squash merging, so the layers survive (ADR-0002)
  - protect `main` so changes arrive through PRs, with dependency review and CI as required checks
  - turn on Dependabot alerts and security updates, secret scanning and push protection
  - turn on private vulnerability reporting, so `SECURITY.md` has a private route to point to
- These steps note which settings are free only on public repos. On a free plan, a private repo
  can't protect `main` or use push protection, so the template's checks there rely on review.

### Keeping the template's own numbering consistent

The template currently calls ADR-0001 to ADR-0004 "the four starter ADRs" and tells adopters to
record their own decisions from ADR-0005 onward (`STARTING_POINT.md`, `docs/next-steps.md`). The
ADRs this proposal requires become starter ADRs too, so those pages change to "the starter ADRs"
and "from ADR-0009 onward".

### 4. Smaller gaps found while reviewing the template

These close gaps against common practice. Each is small, so they share one ADR (ADR-0008).

- **`CONTRIBUTING.md`.** `STARTING_POINT.md` already cites it, but the file doesn't exist. It would
  hold the human-facing version of the git rules in a few lines, citing ADR-0002 and linking to
  `docs/conventions/commits.md`.
- **A starter CI workflow** (`.github/workflows/ci.yml`) that runs the install, test and lint
  commands from `AGENTS.md`. Today the definition of done relies on agents running the checks
  themselves. CI enforces it.
- **A commit-message check** in CI for Conventional Commits prefixes, which ADR-0002 names as an easy
  later step. It checks the commits in a PR and skips merge commits, whose "Merge pull request"
  messages ADR-0002 itself requires.
- **`.editorconfig`**, so every editor and agent uses the same indentation and line endings.

## Alternatives

- **Do nothing.** The template stays useful for experienced teams but doesn't teach, and vulnerable
  dependencies go unnoticed until something breaks.
- **Let each learner's agent do all the teaching.** Rejected for the reasons under Problem: no
  syllabus, no memory, nothing reviewed.
- **A full course covering git and programming from scratch.** Rejected: a lot to maintain, and good
  general tutorials already exist.
- **An AI agent alone for CVE checks, on demand or on a schedule.** Rejected: its knowledge goes
  stale, nothing runs unless someone remembers, and it would depend on one AI tool.
- **Tools alone, no agent.** Workable, but beginners get alerts with no explanation of whether they
  matter here, and fixes wait for a person to write them.
- **Keep GitLab alongside GitHub.** Rejected for now: the template is hosted on GitHub, and every
  alternative adds a choice beginners must make. A later ADR can add GitLab back.

## Decisions this would require

- **ADR-0005, the template teaches:** a learning path for people who can code, a removable
  `docs/new-to-coding/` folder for beginners, one shared glossary, and an opt-in teaching mode for
  agents.
- **ADR-0006, dependency security:** tools detect vulnerabilities from live databases, the `security`
  subagent triages and drafts fixes, and people decide.
- **ADR-0007, GitHub is the only supported host:** drop the GitLab alternatives and list the GitHub
  repo settings the conventions depend on, noting which need a paid plan on private repos.
- **ADR-0008, baseline project hygiene:** `CONTRIBUTING.md`, a starter CI workflow, a commit-message
  check and `.editorconfig`.

## Open questions

- **Should the weekly security check also run as a scheduled agent task, so findings arrive already
  explained?** It adds convenience but ties the setup to one AI tool. — owner: opinuendo
- **Which outside tutorials should `docs/new-to-coding/` link to for git basics?** They need to be
  free, well known and likely to stay online. — owner: opinuendo
- **Should teaching mode be on by default in `docs/new-to-coding/`'s instructions, with experienced
  users turning it off?** Opt-in is the current design. — owner: opinuendo
- **Should the starter CI fail when the commands are still placeholders, or skip with a warning?**
  Failing forces adopters to fill them in; skipping is friendlier on day one. — owner: opinuendo
