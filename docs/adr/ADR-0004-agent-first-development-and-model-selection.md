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

## Consequences

### Positive

- Most code is produced quickly, and people spend their time on decisions and review.
- Cost tracks the difficulty of the work, without trading away quality.
- Every session applies the same rules for delegation and model choice.

### Negative

- Tier choice is a judgment call; the escalation rule limits the cost of a wrong first pick.
- Review becomes the bottleneck. The layered commits of ADR-0002 and fresh-context reviews keep it
  manageable.

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

## Related

- ADR-0002 (layered commits make agent-written changes reviewable)
- ADR-0003 (where the policy and its tool mapping live)
