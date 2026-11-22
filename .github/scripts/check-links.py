"""Checks that relative links and #anchors in every Markdown file resolve. Run from the repo root."""
import glob
import os
import re
import sys


def headings(path):
    text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
    return [re.sub(r"[^a-z0-9 _-]", "", h.strip().lower()).replace(" ", "-")
            for h in re.findall(r"^#+ (.*)", text, re.M)]


broken = []
files = glob.glob("**/*.md", recursive=True) + glob.glob(".*/**/*.md", recursive=True)
# In the template repo, the project README's links only work once setup moves it to the root.
files = [f for f in files if f != os.path.join("template", "project-README.md")]
for f in files:
    for m in re.finditer(r"\]\(([^)\s#]*)(#[^)]*)?\)", open(f, encoding="utf-8").read()):
        target, anchor = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path = os.path.normpath(os.path.join(os.path.dirname(f), target)) if target else f
        if not os.path.exists(path):
            broken.append(f"{f}: {target}")
        elif anchor and path.endswith(".md") and anchor[1:] not in headings(path):
            broken.append(f"{f}: {target}{anchor}")

for b in broken:
    print(f"::error::broken link in {b}")
print(f"Checked {len(files)} files, {len(broken)} broken links.")
sys.exit(1 if broken else 0)
