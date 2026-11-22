# ADR-NNNN: Title of the decision

<!-- The title states the decision itself ("Use merge commits, not squash"), not the topic
("Merge strategy"), so the index reads as a list of what was decided. -->

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** the people who decided this, by name

<!-- Names, not "the team": a reader with a question needs to know who to ask. Status starts at
Proposed; only a person sets Accepted (ADR-0001). -->

## Context

What problem or situation calls for a decision? State the facts, not the conclusion. Include the
constraints that shaped the options (data access, timeline, dependencies on other repos or teams).

<!-- Why facts first: a later reader judging whether this decision still holds needs to see what
was true when it was made. When the context changes, that is the signal to revisit. -->

## Decision

The decision in one or two plain sentences, then the detail needed to act on it.

<!-- Why one or two sentences first: conventions and AGENTS.md will quote this as a one-line rule
and cite the ADR. If it can't be said briefly, it may be two decisions. -->

## Consequences

### Positive

What gets easier or better.

### Negative

What gets harder, or what we give up. Say so even when the decision is still right.

<!-- Why name the negatives: they are what someone will run into later. Writing them down shows the
cost was accepted on purpose, so the decision isn't reopened the first time it hurts. -->

### Risks and mitigations

Only real risks worth naming, each with what we are doing about it.

## Alternatives considered

One or two lines per alternative: what it was and why it lost. "We didn't think of it" is a fine
reason to leave one out; don't pad this section.

<!-- Why this matters most: commit messages and code record what we did, never what we ruled out.
Without this section, someone (often an agent) eventually proposes the rejected option again. -->

## Related

Other ADRs, proposals, docs, or issues this decision touches or depends on.

---

**Filename:** `ADR-NNNN-kebab-case-title.md`, zero-padded to four digits, never reused. Numbers are
never reused so that a citation like "ADR-0007" always means the same decision.

**Status vocabulary:** `Proposed` → `Accepted` → `Deprecated` | `Superseded by ADR-NNNN`.
An accepted ADR is never edited to reverse its decision; a changed decision gets a new ADR. Editing in
place would hide that we ever thought otherwise, and why.
