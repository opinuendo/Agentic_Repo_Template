# docs/proposals/ — designs not yet decided

A **proposal** holds the argument for something not yet decided. ADRs ([`docs/adr/`](../adr/)) record
decisions already made; proposals sit between an idea and the ADRs and work that follow if it is
accepted (ADR-0001).

## Convention

- One file per proposal: `YYYY-MM-DD-<topic>.md`, dated by its first draft. Copy
  [`_template.md`](_template.md).
- **Status:** `Proposed | Accepted | Declined | Superseded`. Agents may write proposals as `Proposed`;
  only a person sets `Accepted` or `Declined`.
- **A proposal in `Proposed` status authorizes no code changes.** Work starts when it is accepted and
  its first ADR is written. Code written early makes the decision for us, and it is harder to say no
  to something already built.
- **Required section, "Decisions this would require":** each decision that would need its own ADR,
  with one line of context. On acceptance this list is the ADR backlog. Don't edit the proposal into
  an ADR; write the ADRs fresh and have them cite the proposal.
- **Required section, "Open questions":** an owner named for each.
- Proposals often travel outside the repo (architecture review, leadership). Write them for a reader
  who has never opened it, and keep personal data and credentials out.

## Proposals

| Proposal | Status | Summary |
|---|---|---|
| *None yet* | | |
