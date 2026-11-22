# .github/ — GitHub configuration

Files GitHub reads to run checks and shape pull requests. GitHub is the only supported host
(ADR-0007).

| File | What it does |
|---|---|
| [`pull_request_template.md`](pull_request_template.md) | The description and checklist every PR starts with |
| [`dependabot.yml`](dependabot.yml) | What Dependabot keeps up to date, and how its PRs are titled (ADR-0006) |
| [`workflows/ci.yml`](workflows/ci.yml) | Install, lint, test and build on every PR, plus a commit-message check (ADR-0008) |
| [`workflows/dependency-review.yml`](workflows/dependency-review.yml) | Fails a PR that adds a dependency with a known vulnerability (ADR-0006) |
| [`workflows/osv-scanner.yml`](workflows/osv-scanner.yml) | Scans lockfiles on PRs, on pushes to `main`, and weekly (ADR-0006) |

Third-party actions are pinned to a full commit SHA, with the version in a comment, and Dependabot
updates the pins. A version tag can be moved to point at different code; a commit SHA can't.
