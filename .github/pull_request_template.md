## What

<!-- One or two sentences. -->

## Why

<!-- The problem being solved. Link the ADR or proposal if there is one, so the reviewer can check
the change against the decision instead of reconstructing it. -->

## Not done or not verified

<!-- Say plainly what is left, skipped, or untested. "Nothing" is a fine answer. Why this section
exists: agents tend to report work as finished, and a reviewer can only check what they know about. -->

## Checklist

<!-- Each item names the rule's ADR; the reason is in the ADR or in AGENTS.md. -->

- [ ] Commits are layered in dependency order with Conventional Commits prefixes (ADR-0002), so this
      can be reviewed one kind of change at a time
- [ ] If this changes a convention, the ADR is the first commit, so the decision is read before the code
- [ ] Each commit builds and passes tests on its own, where practical, so bisect and revert work
- [ ] Build, tests, and lint pass
- [ ] READMEs, conventions, and `docs/next-steps.md` match the change, so the next session starts
      from the truth
- [ ] Substantial changes had a fresh-context review (the `reviewer` subagent or a person), because
      the author is the worst judge of their own blind spots
- [ ] No credentials, personal data, or local settings files added
