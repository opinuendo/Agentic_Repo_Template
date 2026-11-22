# .claude/ — Claude's shared configuration

This folder holds the Claude-specific pieces of how the repo works. The rules themselves are in
[`AGENTS.md`](../AGENTS.md); this folder is how Claude enforces and applies them (ADR-0003). Everything
here is committed and changed through pull requests, like code, because it shapes what every
teammate's Claude does.

## `settings.json`

JSON can't hold comments, so the reasoning for each rule is here.

| Rule | Why |
|---|---|
| `ask` on `git push`, `git merge` | Pushing and merging are visible to others and harder to undo; `AGENTS.md` says agents ask first (ADR-0004) |
| `ask` on `gh pr create` / `gh pr merge` | The same rule for pull requests. GitHub is the only supported host (ADR-0007) |
| `deny` reading `.env`, `.env.*`, `*.pem`, `*.key` | Secrets should never enter an agent's context, where they could end up in a log, a commit, or a request to another service |

Nothing is in `allow`, so each teammate approves other commands as they come up. If the same safe
commands (the test or lint command, for example) are approved again and again, add them to `allow`
in a PR.

Personal settings go in `settings.local.json`, which is git-ignored. Keeping them out of the repo
means one person's preferences never change another person's agent.

## `agents/`

Each file defines a subagent: what it is for, which tools it may use, and which model it runs on.
The model choice applies the tier policy in `AGENTS.md` (ADR-0004).

| Subagent | Tier and model | Tools | Why it is set up this way |
|---|---|---|---|
| [`explorer`](agents/explorer.md) | Fast, `haiku` | Read, Grep, Glob | Searching needs no design judgment, so the cheapest tier does it at full quality. Read-only tools mean it can't change anything by mistake |
| [`implementer`](agents/implementer.md) | Balanced, `sonnet` | All | Building against a decided spec is careful execution. It is told to stop and report when the spec is unclear, because guessing causes rework |
| [`reviewer`](agents/reviewer.md) | Most capable, `opus` | Read, Grep, Glob, Bash | Reviews are never downgraded. It can run tests but is told not to edit, so the review stays independent of the fix |
| [`security`](agents/security.md) | Most capable, `opus` | All | Judging whether a vulnerability matters here is high-stakes judgment (ADR-0006). It needs all tools to read alerts with `gh` and draft a fix, and is told never to dismiss an alert |

The `model:` lines use aliases (`haiku`, `sonnet`, `opus`) rather than versioned model IDs, so a new
model release needs no edit here.

**Adding a subagent:** add one when a kind of delegated task keeps recurring. Give it the lowest tier
that does that task at full quality, the fewest tools it needs, and a description that says why. The
description is what the main agent reads when deciding whether to use it.
