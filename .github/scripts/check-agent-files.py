"""Checks that the Agent files table in AGENTS.md matches the AGENTS_<topic>.md files (ADR-0003).

Every AGENTS_*.md at the repo root must be listed in the table, every file in the table must exist,
and each topic file must say near its top that it is loaded only through the table. Run from the
repo root.
"""
import glob
import os
import re
import sys

errors = []
agents = open("AGENTS.md", encoding="utf-8").read()

section = re.search(r"^## Agent files\n(.*?)(?=^## |\Z)", agents, re.M | re.S)
if not section:
    errors.append("AGENTS.md has no '## Agent files' section")
    listed = set()
else:
    rows = [line for line in section.group(1).splitlines() if line.startswith("|")]
    listed = {m for row in rows for m in re.findall(r"\(\s*(?:\./)?(AGENTS_[^)#\s]+\.md)", row)}

# Case-insensitive, and "-" as well as "_", so a misnamed topic file is caught, not silently skipped.
all_md = [f for f in os.listdir(".") if os.path.isfile(f)]
misnamed = [f for f in all_md if re.match(r"(?i)agents[_-].+\.md$", f) and not re.match(r"AGENTS_[^/]+\.md$", f)]
for f in misnamed:
    errors.append(f"{f} looks like a topic file; name it AGENTS_<topic>.md")
on_disk = set(glob.glob("AGENTS_*.md"))

for f in sorted(on_disk - listed):
    errors.append(f"{f} exists but is not in the Agent files table in AGENTS.md")
for f in sorted(listed - on_disk):
    errors.append(f"the Agent files table lists {f}, which does not exist")
for f in sorted(on_disk & listed):
    head = " ".join(" ".join(open(f, encoding="utf-8").read().splitlines()[:6]).split())
    if "Loaded only through the Agent files table" not in head:
        errors.append(f"{f} must say near its top: 'Loaded only through the Agent files table in AGENTS.md'")

for e in errors:
    print(f"::error::{e}")
print(f"Checked {len(on_disk)} topic files against the Agent files table: {len(errors)} problems.")
sys.exit(1 if errors else 0)
