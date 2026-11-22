# ADR-0001: Record architecture decisions

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Deciders:** <names>

## Context

This repo is new and has no history to explain itself. Most of its code will be written by AI agents
across many sessions, none of which remembers the last. Without a written record of why things are
built the way they are, each contributor or session works the reasons out again, reopens settled
questions, or guesses wrong and breaks an assumption that something else depends on.

## Decision

Record every non-trivial architectural or process decision as an Architecture Decision Record under
[`docs/adr/`](./), one file per decision, using [`template.md`](template.md): a status, date, and
deciders header, then Context, Decision, Consequences, Alternatives considered, and Related.

- Filenames are `ADR-NNNN-kebab-case-title.md`, numbered from 0001 and never reused.
- Status moves `Proposed` → `Accepted` → `Deprecated` or `Superseded by ADR-NNNN`.
- An accepted ADR is never edited to reverse its decision. A changed decision gets a new ADR that
  supersedes the old one, and the old one's status points to it.
- [`README.md`](README.md) is a living index, updated in the same commit as any ADR change.
- Designs not yet decided are proposals in [`docs/proposals/`](../proposals/), not ADRs. Accepting a
  proposal produces the list of ADRs to write.
- Conventions, `AGENTS.md`, and the PR template state a rule in one line and cite its ADR; the
  reasoning lives only in the ADR.
- Agents may draft ADRs with status `Proposed`. Only a person sets `Accepted`.
- Agents treat accepted ADRs as settled. To change one, they propose a superseding ADR.

## Consequences

### Positive

- "Why is it built this way?" is answered by one short file, for people and agents alike.
- Rejected alternatives are recorded, so dead ends are not explored again.
- The index is a one-screen map of every decision.

### Negative

- Writing an ADR adds friction, and where the line falls is a judgment call.
- ADRs drift if decisions change informally without a superseding ADR.

## Alternatives considered

- **Commit messages and code comments only.** Rejected: they don't record the alternatives that lost,
  which is often the most useful part.
- **One running `decisions.md` log.** Rejected: unreadable past about 15 entries, and individual
  decisions can't be linked or cited.

## Related

- [`template.md`](template.md), [`README.md`](README.md)
- [`docs/proposals/README.md`](../proposals/README.md)
