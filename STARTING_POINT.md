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
7. **The repo teaches.** People who can code learn its practices from it, and complete beginners
   learn the basics from a folder of their own (see [Teaching](#teaching)).
8. **Tools detect vulnerabilities; agents triage; people decide.** Live databases catch vulnerable
   dependencies, and an agent explains and drafts the fix (see [Security](#security)).

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
├── README.md                       what the repo is, for people (in the template: the template)
├── LICENSE
├── CONTRIBUTING.md                 the git rules for contributors, in brief
├── SECURITY.md                     how to report a vulnerability privately
├── template/                       template only: cleanup script and the project README
├── .editorconfig                   shared editor settings: encoding, line endings, indentation
├── .gitignore                      keeps personal agent settings and secrets out
├── .claude/
│   ├── README.md                   why each setting and subagent is set up as it is
│   ├── settings.json               shared permissions: what needs a human's OK
│   └── agents/                     subagent definitions with their model tier
│       ├── explorer.md             read-only search, cheapest tier
│       ├── implementer.md          builds against a clear spec, middle tier
│       ├── reviewer.md             fresh-eyes review, most capable tier
│       └── security.md             vulnerability triage, most capable tier
├── .github/
│   ├── README.md                   what each GitHub file does
│   ├── pull_request_template.md
│   ├── dependabot.yml              keeps dependencies and actions up to date
│   └── workflows/
│       ├── ci.yml                  install, lint, test, build, commit-message check
│       ├── dependency-review.yml   blocks PRs that add vulnerable dependencies
│       ├── osv-scanner.yml         scans lockfiles on PRs and weekly
│       └── template-check.yml      template only: setup still works
└── docs/
    ├── README.md                   map of docs/
    ├── next-steps.md               what is open; where a new session starts
    ├── glossary.md                 the one place terms are defined
    ├── learning-path.md            for people who can code: reading order and exercises
    ├── new-to-coding/              for complete beginners; deletable
    ├── adr/                        decisions made: ADR-0001 to ADR-0009, index, template
    ├── proposals/                  designs not yet decided, and accepted ones
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

The nine starter ADRs record the decisions this scaffold makes. They start as `Proposed`: accepting
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

## Teaching

The repo is also a place to learn (ADR-0005). Docs set the order and the vocabulary; agents explain
in context and point back to the docs.

- **People who can code** follow [`docs/learning-path.md`](docs/learning-path.md): a reading order
  and three exercises.
- **Complete beginners** start in [`docs/new-to-coding/`](docs/new-to-coding/): the basics, then a
  first contribution, step by step.
- **Terms** are defined once, in [`docs/glossary.md`](docs/glossary.md).
- **Teaching mode**, defined in `AGENTS.md`, makes an agent explain what it did and why. Each learner
  switches it on in their own git-ignored settings, so it never changes anyone else's agent.

## Security

Most code in a modern project is other people's packages, and new vulnerabilities (CVEs) in them
are published daily. An AI model can't track them alone: its knowledge stops at its training date.
So detection comes from tools that read live databases, and the agent's job is judgment (ADR-0006).

| Piece | What it does |
|---|---|
| Dependabot | Alerts on vulnerable dependencies and opens upgrade PRs |
| Dependency review | Fails a PR that adds a dependency with a known vulnerability |
| OSV-Scanner | Scans lockfiles on PRs and weekly, catching CVEs published after a merge |
| Secret scanning and push protection | Refuses a push containing a credential |
| `security` subagent | Explains whether an alert matters here and drafts the fix; never dismisses an alert |
| `SECURITY.md` | Tells outsiders how to report a vulnerability privately |

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

## Setting up a new project

This is done once, when a project is created. Create the project from the template first: **Use this template** on GitHub, or
`gh repo create <name> --template opinuendo/Agentic_Repo_Template --clone`. Then, in the new repo, ask
your agent to follow this section, or follow it yourself (ADR-0009).

**1. Ask the person.** Only they can answer these; don't guess.

- The project's name, and one or two sentences on what it is and who it's for.
- Its language and package manager, and the install, test, lint, format and build commands. "Not
  decided yet" is a fine answer: leave those placeholders.
- Who holds the copyright, and whether to keep the MIT license.
- Who decides: the names that go in each ADR's Deciders line.
- Whether to keep `docs/new-to-coding/` (keep it if anyone on the team is new to coding).
- Whether the repo is public or private, which changes the GitHub settings in step 5.

**2. Remove the template-only files.** On a new branch, `chore/setup-from-template` (or the branch
your tool assigns), run `bash template/cleanup.sh`. It swaps in the project README, removes the
template's own proposal, the template-only CI check and the `template/` folder, resets the license
holder, and records the project's creation in `docs/next-steps.md`. It lists the placeholders left
to fill in, including the rules line in `AGENTS.md`. Don't commit yet.

**3. Fill in the placeholders** from the answers in step 1:

- the project name and description in `README.md` and `AGENTS.md`; the commands table, scopes and
  routing table in `AGENTS.md`; the repo URL in `docs/new-to-coding/first-contribution.md`;
  `SECURITY.md`; the copyright line in `LICENSE`. Remove the "Skills and hooks" placeholder in
  `CLAUDE.md` if unused.
- the Deciders lines in the ADRs.
- the same commands in `.github/workflows/ci.yml`, and the package manager in
  `.github/dependabot.yml`, if decided.
- If not keeping `docs/new-to-coding/`, delete it and every link to it (search for
  `new-to-coding`).

Keep setup to setup: anything else, such as fleshing out the project idea as a proposal, goes in its
own pull request after this one merges, so each is reviewed on its own.

Run `python3 .github/scripts/check-links.py` and the test and lint commands, then commit in layers
(ADR-0002):

1. `docs(adr): set deciders for the starter ADRs`: everything under `docs/adr/`.
2. `docs: set up project docs from the template`: the other Markdown files and `LICENSE`.
3. `chore: remove template-only files and set CI commands`: the rest, including the deleted
   `template/` folder and workflow.

**4. Push and open a pull request**, after asking the person (ADR-0004).

**5. Apply the GitHub settings.** A person does this; GitHub doesn't copy settings from a template
(ADR-0007).

- **General:** allow merge commits; turn off squash merging, so the layers survive (ADR-0002).
- **Advanced Security** (may be labeled "Code security"): turn on the dependency graph, Dependabot
  alerts, Dependabot security updates, secret scanning, push protection, and private vulnerability
  reporting.
- **Branches:** protect `main` so changes arrive through PRs, with CI and dependency review as
  required checks.
- On a private repo, protecting `main` needs a paid plan, secret scanning and dependency review
  need GitHub's paid security products, and private vulnerability reporting isn't available, so give
  a contact in `SECURITY.md`. Without them, review is the safeguard. Once you have the security
  products, set the repository variable `HAS_CODE_SECURITY` to `true`.

**6. Accept the starter ADRs.** A person does this; an agent never sets `Accepted` (ADR-0001).
Review ADR-0001 to ADR-0009 together, adjust what you disagree with, and set each to `Accepted`
with the date. Record your own early decisions from ADR-0010 onward: repo
layout, what generated output is committed, where canonical definitions live, test expectations.

**7. Keep `docs/next-steps.md` current** from here on. Delete this file once the starter ADRs are
accepted, or move it to `docs/onboarding/` for the next newcomer.
