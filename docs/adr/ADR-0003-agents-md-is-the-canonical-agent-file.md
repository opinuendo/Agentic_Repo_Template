# ADR-0003: `AGENTS.md` is the canonical agent file; tool files point to it

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

AI coding tools each look for their own instruction file (`CLAUDE.md` for Claude, others for other
tools), and most also read `AGENTS.md`. If each file carries its own copy of the repo's rules, the
copies drift, and an agent follows whichever version its tool happened to load. The file is also read
at the start of every session, so its length is a cost paid on every task.

## Decision

- **`AGENTS.md` at the repo root is the single source of agent instructions.** Anything true no matter
  which tool is working goes there, by default.
- **`CLAUDE.md` begins with the line `@AGENTS.md`**, which makes Claude load `AGENTS.md`. Below it,
  `CLAUDE.md` holds only what is specific to Claude: subagent definitions in `.claude/agents/`, shared
  settings in `.claude/settings.json`, skills, hooks, and where personal notes go.
- **Other tools follow the same pattern:** their file points to `AGENTS.md` and adds only that tool's
  specifics.
- **The test for placement:** would a different AI tool need to know this? If yes, `AGENTS.md`.
- **`AGENTS.md` stays short**, aiming for under about 150 lines. Detail lives in linked docs, reached
  through its routing table. Large subdirectories may have their own short `AGENTS.md`.
- **Personal preferences stay out of the repo**: `CLAUDE.local.md`, `.claude/settings.local.json`, and
  user memory are git-ignored or live outside the repo.

## Consequences

### Positive

- One set of rules, whichever tool a teammate uses.
- Switching or adding tools costs one small pointer file.
- A short `AGENTS.md` keeps every session's starting context cheap and focused.

### Negative

- Contributors must judge whether a note is tool-specific; misplaced notes need moving.
- Keeping `AGENTS.md` short means more linked docs to maintain.

## Alternatives considered

- **`CLAUDE.md` as the main file.** Rejected: it ties the repo's rules to one tool.
- **Duplicate the rules in each tool's file.** Rejected: the copies drift.
- **`CLAUDE.md` says "see AGENTS.md" in prose.** Rejected: a sentence does not load the file; the
  import line does.

## Related

- ADR-0004 (the model policy is stated in `AGENTS.md`; its Claude mapping lives in `.claude/agents/`)
