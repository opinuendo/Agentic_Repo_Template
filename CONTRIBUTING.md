# Contributing

Thanks for helping. New to all of this? Start with [`docs/new-to-coding/`](docs/new-to-coding/),
which walks you through your first contribution.

## How we work

The full guide, for people and AI agents alike, is [`AGENTS.md`](AGENTS.md). The essentials:

- **Branch from `main`.** Name it `<type>/<short-kebab-description>`, such as `docs/fix-typo`.
- **Commit messages follow Conventional Commits**, such as `feat(core): add exporter` or
  `docs: fix a typo`. CI checks this (ADR-0008).
- **Layered commits (ADR-0002).** Split a change into commits by type, in dependency order: the ADR
  first, then shared code, tooling, the feature with its tests, docs, and housekeeping. Details in
  [`docs/conventions/commits.md`](docs/conventions/commits.md).
- **Open a pull request** and fill in the template. Say plainly what you didn't do or couldn't
  verify.
- **Pull requests are merged with a merge commit, never squashed**, so the layers survive.
- **Changing a convention?** Write an ADR first; see [`docs/adr/README.md`](docs/adr/README.md).

## Security

Never report a vulnerability in a public issue or pull request. See [`SECURITY.md`](SECURITY.md).
