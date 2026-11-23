# Agent rules: delegation and model tiers

Loaded only through the Agent files table in [`AGENTS.md`](AGENTS.md#agent-files), when delegating to
a subagent or choosing a model tier. The rules that must never be missed are in `AGENTS.md`; this
file holds the detail (ADR-0004).

## Choosing a tier

| Tier | Use it for | Why this tier |
|---|---|---|
| Fast, least expensive | Finding and reading: search, list call sites, summarize a file | No judgment needed; a stronger model adds cost, not quality |
| Balanced | Building against a clear, complete spec: implement a decided interface, write tests for known behavior | The thinking is done; the work is careful execution |
| Most capable | Judgment or high stakes: design, ADRs, unclear bugs, code review, security- or data-sensitive changes | Mistakes here are expensive and easy to miss |

- When unsure, go one tier up. Picking too low costs more in rework than picking too high costs in
  tokens.
- After one failed attempt, escalate a tier rather than retrying the same one; the same model on the
  same problem usually gets the same result.
- Each tool maps tiers to its own models; for Claude, see [`CLAUDE.md`](CLAUDE.md).

## Delegating well

- Delegate work that is independent, parallel, or would flood your context.
- Give a subagent the goal, what is already ruled out, the files to read, and what done looks like.
  It knows only what you tell it.
- Check what comes back before relying on it. A subagent's report is a claim, not proof.
- Parallel writers each get their own branch or worktree, or they overwrite each other. Agents that
  only read can share a checkout.
