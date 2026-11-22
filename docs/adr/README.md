# Architecture Decision Records

Every non-trivial decision behind how this repo is built is recorded here, one file per decision.
See [`template.md`](template.md) for the format and ADR-0001 for why this exists.

| # | Title | Status |
|---|---|---|
| [0001](ADR-0001-record-architecture-decisions.md) | Record architecture decisions | Proposed |
| [0002](ADR-0002-layered-commits-and-merge-commits.md) | Layered commits, Conventional Commits, merge commits | Proposed |
| [0003](ADR-0003-agents-md-is-the-canonical-agent-file.md) | `AGENTS.md` is the canonical agent file; tool files point to it | Proposed |
| [0004](ADR-0004-agent-first-development-and-model-selection.md) | Agent-first development; least expensive model that keeps full quality | Proposed |

The four starter ADRs come from the agentic repo starter. Review them as a team, adjust what you
disagree with, then set each to `Accepted` with the date.

## Adding a new ADR

1. Copy [`template.md`](template.md) to `ADR-NNNN-kebab-title.md`, using the next number in sequence.
2. Status starts at `Proposed`. Fill in Context, Decision, Consequences, Alternatives considered,
   Related. Agents may draft ADRs; only a person sets `Accepted`.
3. Once it is agreed, set the status to `Accepted` and update its row in the table above, in the same
   commit.
4. If a later decision replaces this one, write a new ADR that references this one, and change this
   one's status to `Superseded by ADR-NNNN`. Never delete an accepted ADR or rewrite its decision in
   place. Fixing typos and adding links is fine. Why: the record of what we used to think, and why we
   changed, is what stops the old option from being proposed again.

## When to write one

- Anything a newcomer would ask "why?" about, anything expensive to reverse, or any choice where a
  sensible alternative lost.
- Process decisions count, not only architecture: git workflow, what gets committed, naming.
- Skip it for small, easily reversed choices. If unsure, write a short one; two paragraphs is fine.
