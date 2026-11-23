#!/usr/bin/env bash
# Removes template-only files from a project created from the template (ADR-0009).
# Run from the new project's root, on a branch:  bash template/cleanup.sh
# It changes files but doesn't commit; review with `git status`, then commit (see STARTING_POINT.md).
set -euo pipefail

TEMPLATE_REPO="opinuendo/agentic_repo_template"   # the template itself, which must never be cleaned

die() { echo "cleanup: $*" >&2; exit 1; }

[ -f template/cleanup.sh ] || die "run this from the project's root folder."

# Refuse to run in the template repo, unless the template's own CI check is testing a copy.
origin=$(git remote get-url origin 2>/dev/null || true)
origin=$(printf '%s' "$origin" | tr '[:upper:]' '[:lower:]')
case "$origin" in
  */"$TEMPLATE_REPO" | */"$TEMPLATE_REPO".git | *:"$TEMPLATE_REPO" | *:"$TEMPLATE_REPO".git)
    [ "${TEMPLATE_CLEANUP_TEST:-}" = "1" ] || die "this is the template repo itself. Create a new project from it first (see README.md)." ;;
esac

# Refuse to mix the cleanup with uncommitted work, so it can be reviewed and undone on its own.
if [ -n "$(git status --porcelain 2>/dev/null)" ] && [ "${TEMPLATE_CLEANUP_TEST:-}" != "1" ]; then
  die "you have uncommitted changes. Commit or stash them first."
fi

# perl -pi edits files in place the same way on Linux and macOS (sed -i differs between them).

echo "Replacing the template's README with the project README..."
mv template/project-README.md README.md

echo "Removing the template's own proposal and the links to it..."
rm -f docs/proposals/2026-11-22-teaching-security-and-github.md
perl -pi -e 's/^\| \[2026-11-22 teaching, security and GitHub\].*$/| *None yet* | | |/' docs/proposals/README.md
perl -ni -e 'print unless /^- \[Proposal: teaching, dependency security, and GitHub\]/' docs/adr/*.md

echo "Removing the template-only CI check..."
rm -f .github/workflows/template-check.yml
perl -ni -e 'print unless /template-check\.yml/' .github/README.md

echo "Resetting the license holder..."
perl -pi -e 's/^Copyright \(c\) .*$/Copyright (c) <year> <copyright holder>/' LICENSE

echo "Removing template-only lines from STARTING_POINT.md..."
perl -ni -e 'print unless /template only:/' STARTING_POINT.md
perl -pi -e 's/├── osv-scanner\.yml/└── osv-scanner.yml/' STARTING_POINT.md

echo "Recording the project's creation in docs/next-steps.md..."
today=$(date +%Y-%m-%d)
perl -pi -e "s/^- <YYYY-MM-DD: decision, with its ADR number>\$/- $today: created from the Agentic Repo Template; starter ADRs ADR-0001 to ADR-0009 await acceptance (ADR-0009)/" docs/next-steps.md

echo "Removing template/..."
rm -rf template

echo
echo "Done. Placeholders still to fill in:"
grep -rniE '<(repo-name|one or two sentences|install command|test command|lint command|format command|build command|your |the files to read|add the few rules|this repo.s url|list project skills|year|copyright holder|number|maintainer|names|which versions)' \
  --include='*.md' --include='*.yml' --include=LICENSE . 2>/dev/null | grep -v -e '^./.git/' -e '^./STARTING_POINT.md' || echo "  none found"
