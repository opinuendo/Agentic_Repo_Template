# Agent rules: security

Loaded only through the Agent files table in [`AGENTS.md`](AGENTS.md#agent-files), when working on a
security alert, a failed security check, a CVE question, or a new dependency. The rules that must
never be missed are in `AGENTS.md` itself; this file holds the detail (ADR-0003, ADR-0006). How
outsiders report a vulnerability is in [`SECURITY.md`](SECURITY.md).

## Where findings come from

- Dependabot, dependency review and OSV-Scanner read live vulnerability databases. Your knowledge
  stops at your training date, so the databases are the source of truth, never your memory.
- Read open alerts with `gh api "repos/{owner}/{repo}/dependabot/alerts?state=open"`, and a failed
  check with `gh run view <id> --log-failed`. If you can't reach them, say so and stop.

## Triage

- Use the most capable tier (ADR-0004), or the `security` subagent where your tool has one.
- For each alert: the package, installed version, advisory ID (GHSA or CVE), severity, and first
  fixed version.
- Check whether this repo actually uses the vulnerable part: search for imports and calls, and
  whether it's a runtime dependency or only used in development.
- Explain the risk in plain words, linking [`docs/glossary.md`](docs/glossary.md) for terms.

## Fixing

- Draft the fix on a branch named `fix/deps-<package>`, as a `fix(deps):` commit naming the
  advisory ID.
- Upgrade to the lowest version that fixes the advisory, regenerate the lockfile, and run the test
  and lint commands.
- Say what might break when an upgrade crosses a major version.
- Ask before pushing or opening a pull request, like any change (ADR-0004).

## Adding dependencies

Dependency review fails a pull request that adds a dependency with a known vulnerability. Check the
package's advisories before adding it, not after the check fails.
