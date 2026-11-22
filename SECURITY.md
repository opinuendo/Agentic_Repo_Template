# Security policy

## Reporting a vulnerability

Please report security problems privately, not in a public issue or pull request.

- **How:** open this repo's **Security** tab on GitHub and choose **Report a vulnerability**. Only
  the maintainers can see the report.
- **What to include:** what you found, where (file or feature), how to reproduce it, and what an
  attacker could do with it.
- **What happens next:** we aim to reply within <number> working days. We'll keep you updated while
  we fix it, and credit you when the fix is published unless you'd rather we didn't.

If the **Report a vulnerability** button is missing, contact <maintainer contact>.

## Supported versions

<Which versions or branches receive security fixes. For a project without releases: "Only the
latest commit on `main`.">

## How this repo watches its own dependencies

Automated tools check every pull request and run weekly against live vulnerability databases, and
an AI agent helps explain and fix what they find. A person always makes the final call. The details
and reasoning are in [ADR-0006](docs/adr/ADR-0006-dependency-security.md).
