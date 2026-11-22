# Commits, branches, and pull requests

The decision and its reasoning are in ADR-0002. This page is how to apply it.

## The layers

Commit in this order, skipping layers the change doesn't touch. Replace the example scopes with this
repo's own.

| Order | Layer | Prefix | What goes in it |
|---|---|---|---|
| 1 | Decision | `docs(adr):` | The ADR, when the change introduces or alters a convention |
| 2 | Shared foundation | `feat(core):` / `fix(core):` | Shared libraries, schemas, definitions, migrations |
| 3 | Tooling | `feat(cli):` / `feat(<tool>):` | CLIs, generators, build tooling that uses the foundation |
| 4 | Feature | `feat(<feature>):` | The feature, with its tests |
| 5 | Docs | `docs:` | READMEs, onboarding, conventions updated to match |
| 6 | Housekeeping | `chore:` | Lockfiles, CI config, formatting-only changes |

`refactor:`, `test:`, and `perf:` sit in whichever layer their files belong to.

## Example

A customer export feature, as `git log --oneline` shows it (newest first). Reviewers read bottom to
top.

```text
a41c9e2 docs: export how-to in the README and onboarding guide
7be0d13 feat(export): customer export job, with tests and a sample output
3f9a2c8 feat(cli): `export` command that runs any registered exporter
c02e7d5 feat(core): Exporter interface and the canonical customer schema
9d1b4a6 docs(adr): ADR-0012 exports write CSV with a metadata sidecar
```

## Guidelines

- **Layer by type, not by file.** Five to eight commits is typical for a substantial change. A small
  change in one layer is one commit.
- **Each commit stands on its own** where practical: it builds and passes tests. A layer may add code
  nothing calls yet; the next commit calls it.
- **Merge with a merge commit, never squash.** Squashing collapses the layers.
- **Review commit by commit.** "This belongs in the core commit" is a normal review note.

## Restaging work done out of order

Real work rarely happens top-down. Before opening a PR, rebuild the history in layer order:

1. `git reset --soft main` (or the branch point): the branch's commits are undone, the changes kept.
2. `git add -p <paths>` to stage one layer, then commit it with its prefix.
3. Repeat down the layers, then run the tests.

## Branches and pull requests

- Default branch `main`. Branch names `<type>/<short-kebab-description>`, for example
  `feat/customer-export`.
- Agents commit on a feature branch freely, and ask before pushing or opening a PR (ADR-0004).
- The PR description says what changed, why, and what was not done or not verified. Fill in the PR
  template's checklist.
