# ADR-0004: Agent-first development; least expensive model that keeps full quality

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

AI agents can write most of the code in this repo, and subagents let one agent split work across
several in parallel. Models differ widely in cost and capability. Choosing the cheapest model for
everything produces work that needs redoing; choosing the most capable model for everything spends
money on tasks a cheaper model does equally well. Without a stated policy, each session picks
differently.

## Decision

**1. Agent-first.** Agents write as much of the code as possible: implementation, tests, docs, and
draft ADRs and proposals. People set direction, decide, review, and accept. The repo is organized so
an agent with no memory of earlier sessions can do any task well (see `AGENTS.md`).

**2. The main agent orchestrates.** It keeps the task and the judgment calls, delegates bounded work
that is independent, parallel, or would flood its context, and checks each subagent's result before
relying on it.

**3. Model selection.** Use the least expensive model that does the task at full quality. Quality is
never traded for cost.

| Tier | Use it for |
|---|---|
| Fast, least expensive | Finding and reading, with no judgment about the result |
| Balanced | Building against a clear, complete spec |
| Most capable | Judgment, ambiguity, or high stakes: design, ADRs, unclear bugs, review, security- or data-sensitive changes |

- When unsure between two tiers, use the higher one.
- Rework counts as cost. After one failed attempt, escalate a tier rather than retrying the same one.
- Reviews are never downgraded to save cost.
- The policy names tiers, not model IDs. Each tool maps tiers to its models in its own configuration
  (for Claude, `.claude/agents/`; see ADR-0003).

**4. Autonomy.** Without asking, agents may read, search, test, lint, build, edit, commit on a feature
branch, and write ADRs or proposals as `Proposed`. They ask first before pushing, opening a PR,
merging, changing `main`, running against production systems or real data, or handling secrets. Only
a person sets an ADR or proposal to `Accepted`.

**5. Parallel work.** One writer per set of files. Parallel writers each get their own branch or
worktree. Agents that only read may share a checkout.

**6. Working with the author.** The author is the person directing the work in a session.

- **Recommend; the author decides.** For an architectural or hard-to-reverse choice, the agent
  presents the options with their pros and cons and its recommendation, and the author chooses. The
  agent never builds on an answer it assumed.
- **Autonomy is granted explicitly and scoped.** The author can let the agent decide more, by saying
  so in the session or in their own personal, git-ignored instructions, naming the kinds of decision
  it covers. Within the grant the agent still records each architectural decision as a `Proposed`
  ADR. A grant covers decisions only: it never changes what agents must ask first about or may never
  do (point 4).
- **One question at a time.** The agent asks the question that unblocks the most, makes it easy to
  answer, and waits before asking the next.
- **A question is a check, not pushback.** When the author asks "why?" or "are you sure?", the agent
  re-checks its reasoning and shows it. It keeps a recommendation that still holds and changes it
  only when the reasoning breaks, saying exactly what was wrong.

How to apply these is in `AGENTS_collaboration.md`; the rules themselves are in `AGENTS.md`.

## Consequences

### Positive

- Most code is produced quickly, and people spend their time on decisions and review.
- Cost tracks the difficulty of the work, without trading away quality.
- Every session applies the same rules for delegation and model choice.

### Negative

- Tier choice is a judgment call; the escalation rule limits the cost of a wrong first pick.
- Review becomes the bottleneck. The layered commits of ADR-0002 and fresh-context reviews keep it
  manageable.

- Asking before every architectural choice, one question at a time, means more round trips at the
  start of a project. An explicit grant of autonomy removes them where the author is happy to.

### Risks and mitigations

- Agents report work as done that isn't. Mitigation: the definition of done in `AGENTS.md` requires
  the agent to run tests and lint itself, and to state what was not verified.
- Subagent results are trusted without checking. Mitigation: the main agent verifies before relying
  on them.

## Alternatives considered

- **Always use the most capable model.** Rejected: spends heavily on search and mechanical tasks a
  cheaper model does equally well.
- **Always use the cheapest model.** Rejected: rework and subtle errors cost more than the savings.
- **Name specific model IDs in the policy.** Rejected: model names change; tiers don't.

- **The agent decides architecture and reports afterwards.** Rejected: in the first project set up
  from this template, the agent made architectural assumptions the author wanted to weigh in on.
  Undoing a built assumption costs more than asking.
- **Ask all open questions in one list.** Rejected: a long list is hard to answer well, and later
  questions often depend on earlier answers.
- **Treat a repeated question as a sign to change the recommendation.** Rejected: an answer should
  follow from the evidence, not from being asked twice.

## Related

- ADR-0002 (layered commits make agent-written changes reviewable)
- ADR-0003 (where the policy and its tool mapping live)
