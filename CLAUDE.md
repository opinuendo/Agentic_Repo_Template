@AGENTS.md

# Claude-specific notes

Everything about how this repo works is in `AGENTS.md`, imported above. This file holds only what is
specific to Claude (ADR-0003). If a note would also matter to another AI tool, it belongs in
`AGENTS.md` instead.

## Subagents

Model tiers from `AGENTS_delegation.md` map to the subagent definitions in `.claude/agents/`. Why
each is set up the way it is, and what each settings rule is for, are in
[`.claude/README.md`](.claude/README.md).

| Tier | Subagent | `model:` |
|---|---|---|
| Fast, least expensive | `explorer` (read-only) | `haiku` |
| Balanced | `implementer` | `sonnet` |
| Most capable | `reviewer` | `opus` |
| Most capable | `security` (vulnerability triage, ADR-0006) | `opus` |

- Use these by name when delegating, so the model choice is the one the team agreed on.
- The frontmatter uses model aliases, not versioned IDs, so new model releases need no edit here.
- Add a subagent when a kind of delegated task recurs. Give it the lowest tier that does that task at
  full quality, and say why in its description.

## Settings

- `.claude/settings.json` is shared and committed. Its `ask` rules enforce the "Ask first" rows of
  `AGENTS.md` (push, merge, and similar). Change it through a PR, like code.
- Personal preferences go in `.claude/settings.local.json` or `CLAUDE.local.md`, both git-ignored,
  or in user memory. Never commit them.
- To switch on [teaching mode](AGENTS_teaching.md) (ADR-0005), add a line saying "Use teaching
  mode from AGENTS_teaching.md" to your `CLAUDE.local.md` or user memory.

## Skills and hooks

<List project skills in `.claude/skills/` and hooks (for example format-on-edit) once you add them.
Remove this section if there are none.>
