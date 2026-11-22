# Starting point: a repo built for agents

This is the guide to how a new repo is organized when AI agents write most of the code and people
decide, review, and accept. It explains each piece of the scaffold beside it and why it is there.
Read this once when starting a repo; after that, `AGENTS.md` is the file everyone (people and agents)
works from.

## The principles

1. **Agents write as much of the code as possible.** People set direction, make decisions, review,
   and accept. Agents implement, test, document, and propose. The repo is shaped so an agent with no
   memory of earlier sessions can pick up any task and do it well.
2. **Quality is never traded for cost.** Agents and subagents use the least expensive model that does
   the task at full quality. A cheaper model that produces work needing rework is not cheaper.
3. **Every decision is written down once.** Non-obvious decisions are ADRs that are never changed after
   acceptance; conventions cite them instead of restating them (see [ADRs](#adrs)).
4. **History teaches.** Changes land as layered commits in dependency order, merged with merge commits
   (see [Layered commits](#layered-commits)).
5. **Write for the next reader.** Every directory has a README; every module says what it is for. The
   next reader is as likely to be an agent as a person, and both start with no context.
6. **`AGENTS.md` is the one agent file.** Tool-specific files (`CLAUDE.md` and others) point to it and
   hold only what is specific to that tool (see [The agent files](#the-agent-files)).

## What "agent-friendly" means in practice

A principle an agent cannot check is a wish. Each of these makes the repo easier for an agent to work
in correctly, and none of them is specific to one AI tool.

| Practice | Why it matters for agents |
|---|---|
| One command each to build, test, lint, and format, listed in `AGENTS.md` | Agents verify their own work instead of guessing how |
| Fast tests with error messages that say what to fix | Agents iterate in seconds, not minutes, and fix the right thing |
| Rules enforced by lint, type checks, and CI where possible | A rule a tool checks is followed; a rule in prose is followed sometimes |
| Copy-me templates (`_template/` directories) for recurring things | Agents copy a pattern instead of inventing a slightly different one |
| A README in every directory; a purpose line on every module | An agent opening a directory learns what belongs there |
| One source of truth for each definition, cited elsewhere | Agents never update one copy and miss another |
| Generated files are never hand-edited, and CI checks for drift | Agents edit the source, regenerate, and commit both |
| Small files with one job each | Agents read only what the task needs |
| `docs/next-steps.md` kept current | A new session knows what is open without asking |
| No knowledge that lives only in someone's head | If a newcomer stumbles, the fix goes into the docs, not a chat reply |

## The scaffold

```text
.
├── AGENTS.md                       the main agent file: how we work, commands, routing, rules
├── CLAUDE.md                       imports AGENTS.md; Claude-specific notes only
├── README.md                       what the repo is, for people
├── .gitignore                      keeps personal agent settings and secrets out
├── .claude/
│   ├── README.md                   why each setting and subagent is set up as it is
│   ├── settings.json               shared permissions: what needs a human's OK
│   └── agents/                     subagent definitions with their model tier
│       ├── explorer.md             read-only search, cheapest tier
│       ├── implementer.md          builds against a clear spec, middle tier
│       └── reviewer.md             fresh-eyes review, most capable tier
├── .github/
│   └── pull_request_template.md    (GitLab: .gitlab/merge_request_templates/default.md)
└── docs/
    ├── README.md                   map of docs/
    ├── next-steps.md               what is open; where a new session starts
    ├── adr/                        decisions made
    │   ├── README.md               index and how to add one
    │   ├── template.md
    │   ├── ADR-0001-record-architecture-decisions.md
    │   ├── ADR-0002-layered-commits-and-merge-commits.md
    │   ├── ADR-0003-agents-md-is-the-canonical-agent-file.md
    │   └── ADR-0004-agent-first-development-and-model-selection.md
    ├── proposals/                  designs not yet decided
    │   ├── README.md
    │   └── _template.md
    └── conventions/                how we do things, each citing its ADR
        ├── README.md
        └── commits.md
```

Add your own source, test, and template directories beside these. Each gets a README.

## ADRs

An Architecture Decision Record is one short file per decision: context, decision, consequences,
alternatives considered. The full convention is in [`docs/adr/README.md`](docs/adr/README.md) and
ADR-0001. The parts that matter most:

- **Lifecycle.** idea → proposal (`docs/proposals/`, undecided, authorizes no code) → ADR
  (`docs/adr/`, decided) → conventions and code that cite the ADR number.
- **Never changed after acceptance.** A changed decision gets a new ADR that supersedes the old one;
  the old one's status points forward. The record of what was rejected is the point.
- **Cite, don't restate.** `AGENTS.md`, `CONTRIBUTING.md`, and the PR template state a rule in one line
  and cite its ADR. The reasoning lives in exactly one place.
- **When to write one.** Anything a newcomer would ask "why?" about, anything expensive to reverse, any
  choice where a sensible alternative lost. Process decisions count.
- **Agents draft, people accept.** Agents may write ADRs with status `Proposed`. Only a person sets
  `Accepted`.
- **For agents, settled is settled.** Agents do not reopen an accepted ADR; they propose a superseding
  one. This one rule does the most to stop agents second-guessing earlier sessions.

The four starter ADRs record the decisions this scaffold makes. They start as `Proposed`: accepting
them (and adjusting what you disagree with) is the team's first act in the new repo.

## Layered commits

Each change is split into commits by type of change, in dependency order, each with a Conventional
Commits prefix:

1. `docs(adr):` the decision, if the change introduces or alters a convention
2. `feat(core):` / `fix(core):` shared foundation other code builds on
3. `feat(cli):` / `feat(<tool>):` tooling that uses the foundation
4. `feat(<feature>):` the feature and its tests
5. `docs:` READMEs, onboarding, conventions updated to match
6. `chore:` lockfiles, CI, formatting

Each commit builds and passes tests on its own where practical. Pull requests merge with a merge
commit, never squashed, so the layers survive in history. Details, restaging work done out of order,
and an example are in [`docs/conventions/commits.md`](docs/conventions/commits.md); the decision is
ADR-0002.

## The agent files

- **`AGENTS.md` holds everything by default.** It is read by most AI coding tools. Anything true no
  matter which tool is working goes here.
- **`CLAUDE.md` starts with `@AGENTS.md`.** That import line is what makes Claude load `AGENTS.md`;
  a sentence saying "see AGENTS.md" loads nothing. Below it go only things specific to Claude: the
  subagent definitions in `.claude/agents/`, the shared settings in `.claude/settings.json`, skills,
  hooks, and how personal notes (`CLAUDE.local.md`, user memory) stay out of the repo.
- **Other tools follow the same pattern.** A tool-specific file points to `AGENTS.md` and adds only
  that tool's specifics.
- **Keep `AGENTS.md` short.** It is loaded at the start of every session, so every line costs on every
  task. Aim for under about 150 lines. Detail goes in linked docs, reached through the routing table.
- **Nested `AGENTS.md` files** are fine in large subdirectories with rules of their own; keep them
  just as short.

The test for where something goes: *would a different AI tool need to know this?* If yes, `AGENTS.md`.
If it only makes sense for Claude, `CLAUDE.md`.

## Agents and subagents

The main agent orchestrates: it holds the task, makes the judgment calls, delegates bounded work to
subagents, and verifies what comes back. Subagents do work that is independent, parallel, or would
flood the main agent's context (wide searches, isolated implementation steps, fresh-eyes review).

**Choosing a model** (the full policy is ADR-0004):

| Tier | Use it for | Examples |
|---|---|---|
| Fast, least expensive | Reading and finding, with no judgment about the result | Search the codebase, list call sites, summarize a file, check a link |
| Balanced | Building against a clear, complete spec | Implement a function whose interface is decided, write tests for a known behavior, fill in docs from an outline |
| Most capable | Judgment, ambiguity, or high stakes | Design, ADRs, debugging with no clear cause, code review, security- or data-sensitive changes |

- Pick the least expensive tier that will do the task **at full quality**. When unsure, go one tier up.
- Rework counts as cost. Escalate a tier after one failed attempt rather than retrying the same tier.
- Reviews are never downgraded to save cost.
- The main agent checks a subagent's result before relying on it. A subagent's report is a claim, not
  proof.
- Policies name tiers, not model IDs: model names change; the tiers don't. The Claude mapping lives in
  `.claude/agents/`.

**Working in parallel.** One writer per set of files. Parallel agents that write code each get their own
branch or worktree. Agents that only read can share a checkout.

## What agents may do without asking

| Action | Without asking? |
|---|---|
| Read, search, run tests, lint, and build | Yes |
| Edit files and commit on a feature branch | Yes |
| Write an ADR or proposal with status `Proposed` | Yes |
| Push a branch or open a pull request | Ask first |
| Merge, or change `main` directly | Ask first |
| Set an ADR or proposal to `Accepted` | Never; a person does this |
| Run against production systems or real data, or handle secrets | Ask first |

`.claude/settings.json` enforces the "ask first" rows for Claude. Mirror them in other tools' settings.

## Definition of done (for agents and people)

- The build, tests, and lint pass, and the agent ran them rather than assuming.
- New or changed behavior has tests.
- READMEs, conventions, and `docs/next-steps.md` are updated to match.
- If the change introduced or altered a convention, there is an ADR, and it is the first commit.
- Commits are layered and use Conventional Commits prefixes.
- For substantial changes, a reviewer with fresh context (the `reviewer` subagent, or a person) has
  read the diff.
- What was not done or not verified is said plainly in the PR description.

## Adopting this scaffold

1. Copy the scaffold into the new repo.
2. Replace every `<placeholder>` (repo name, commands, scopes, deciders).
3. Review the four starter ADRs together; adjust them, then set each to `Accepted` with today's date.
4. Fill in the commands and routing table in `AGENTS.md` as the repo takes shape.
5. Add ADR-0005 onward for your own early decisions: repo layout, what generated output is committed,
   where canonical definitions live, test and CI expectations.
6. Delete this file, or keep it as `docs/onboarding/starting-point.md` for the next team.
