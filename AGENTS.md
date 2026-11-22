# <repo-name> — guide for AI agents and new contributors

<One or two sentences: what this repo is.> Read this file, then load only what the task needs (see
[Routing](#routing)). This file is the single agent guide for every AI tool; tool-specific files point
here so there is one set of rules to keep current (ADR-0003).

Each rule below carries a short reason. The full reasoning, and the alternatives we rejected, are in
the ADR it cites.

## How we work

- **Agent-first (ADR-0004).** Agents write as much of the code as possible. People decide, review, and
  accept. Write everything so an agent with no memory of earlier sessions can pick up the task,
  because every session starts from nothing.
- **Quality is never traded for cost (ADR-0004).** Use the least expensive model that does the task at
  full quality; a cheap model that causes rework isn't cheap. See
  [Agents and subagents](#agents-and-subagents).
- **Decisions are ADRs (ADR-0001).** Non-obvious decisions live in [`docs/adr/`](docs/adr/). Accepted
  ADRs are settled: do not reopen one; propose a superseding ADR instead. Otherwise each session
  re-argues what an earlier one decided.
- **Layered commits (ADR-0002).** See [Git](#git).
- **Write for the next reader.** Every directory has a README; every module states its purpose. The
  next reader is often an agent with no context, and a README tells it what belongs in a folder before
  it adds something that doesn't. When something here confused you, fix the doc, not just the code.

## Commands

| Task | Command |
|---|---|
| Install | `<install command>` |
| Test | `<test command>` |
| Lint | `<lint command>` |
| Format | `<format command>` |
| Build | `<build command>` |

Run test and lint yourself before calling anything done. Assuming they pass is the most common way
work gets reported as finished when it isn't.

## Routing

This file is loaded at the start of every session, so it stays short and detail lives in the files
below, read only when a task needs them.

| Task | Load |
|---|---|
| Starting a session, or asking what is open | [`docs/next-steps.md`](docs/next-steps.md), then the [ADR index](docs/adr/README.md) |
| Why a convention exists | the ADR named beside it, in [`docs/adr/`](docs/adr/) |
| Recording a decision | [`docs/adr/README.md`](docs/adr/README.md), [`docs/adr/template.md`](docs/adr/template.md) |
| A design not yet decided | [`docs/proposals/README.md`](docs/proposals/README.md) |
| Committing, branching, opening a PR | [`docs/conventions/commits.md`](docs/conventions/commits.md) |
| <your task type> | <the files to read for it> |

## Rules that are easy to get wrong

- **Never restate a canonical definition.** Each definition lives in one place; cite it. Two copies
  drift, and an agent updates one and misses the other.
- **Never hand-edit generated files.** Edit the source, regenerate, commit both. A hand edit is silently
  overwritten the next time the file is generated.
- **Never set an ADR or proposal to `Accepted`.** Write it as `Proposed`; a person accepts it.
  Decisions belong to people; agents draft them.
- **A proposal authorizes no code.** Work starts when it is accepted and its first ADR is written, so
  nothing gets built before we agree it should be.
- <add the few rules that cost the most when broken, each with its reason>

## Git

- Conventional Commits; default branch `main`; branch names `<type>/<short-kebab-description>`. The
  prefixes make history scannable and let tools generate changelogs.
- **Layered commits (ADR-0002).** Split a change into commits by type, in dependency order:
  `docs(adr):` then `feat(core):` then tooling (`feat(cli):`) then `feat(<feature>):` then `docs:`
  then `chore:`. Reviewers read the decision before the code, and each commit is one kind of change.
  Each commit builds on its own where practical, so bisect and revert work. Never squash a multi-layer
  change into one commit.
- Pull requests merge with a merge commit, never squashed; a squash throws the layers away.
- Scopes in use: `adr`, `core`, `cli`, <your scopes>.

## What agents may do

| Action | Without asking? | Why |
|---|---|---|
| Read, search, run tests, lint, build | Yes | No side effects |
| Edit files and commit on a feature branch | Yes | Easy to undo; nothing leaves the machine |
| Write an ADR or proposal as `Proposed` | Yes | Drafting is cheap; deciding isn't |
| Push, open a PR, merge, or change `main` | Ask first | Visible to others and harder to undo |
| Run against production systems or real data; handle secrets | Ask first | Too risky to leave to an agent alone |
| Set an ADR or proposal to `Accepted` | Never | Decisions belong to people |

## Agents and subagents

The main agent orchestrates: it keeps the judgment calls, delegates bounded work, and checks what comes
back before relying on it, because a subagent's report is a claim, not proof. Delegate work that is
independent, parallel, or would flood your context.

| Tier | Use it for | Why this tier |
|---|---|---|
| Fast, least expensive | Finding and reading: search, list call sites, summarize a file | No judgment needed; a stronger model adds cost, not quality |
| Balanced | Building against a clear, complete spec: implement a decided interface, write tests for known behavior | The thinking is done; the work is careful execution |
| Most capable | Judgment or high stakes: design, ADRs, unclear bugs, code review, security- or data-sensitive changes | Mistakes here are expensive and easy to miss |

- When unsure, go one tier up. Picking too low costs more in rework than picking too high costs in
  tokens.
- After one failed attempt, escalate a tier rather than retrying the same one; the same model on the
  same problem usually gets the same result.
- Reviews are never downgraded to save cost. A review exists to catch what the author missed.
- One writer per set of files. Parallel writers each get their own branch or worktree, or they
  overwrite each other.
- Give a subagent the goal, what is already ruled out, the files to read, and what done looks like.
  It knows only what you tell it.

## Definition of done

Agents tend to report work as finished. These make "done" something you can check:

- Build, tests, and lint pass, and you ran them.
- New or changed behavior has tests.
- READMEs, conventions, and [`docs/next-steps.md`](docs/next-steps.md) match the change, so the next
  session starts from the truth.
- A convention change has an ADR, as the first commit.
- Substantial changes had a fresh-context review; the author is the worst judge of their own blind
  spots.
- What was not done or not verified is stated plainly.
