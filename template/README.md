# template/ — files used only to create a new project

Everything here belongs to the template, not to the projects made from it (ADR-0009). Setting up a
new project runs `cleanup.sh`, which deletes this folder.

| File | What it does |
|---|---|
| [`cleanup.sh`](cleanup.sh) | Removes template-only files and resets the license holder. Refuses to run in the template repo itself |
| [`project-README.md`](project-README.md) | Becomes the new project's `README.md` |

The full setup, including the questions only a person can answer, is "Setting up a new project" in
[`STARTING_POINT.md`](../STARTING_POINT.md#setting-up-a-new-project).

**Changing the template?** If you add a template-only file, add it to `cleanup.sh` too, and mark
any template-only line in `STARTING_POINT.md` with "template only:" so the cleanup removes it.
The template repo must keep **Settings → General → Template repository** ticked: the check below
runs only in a repo marked as a template, and is skipped (and so passes) otherwise. The
template-only check in [`.github/workflows/template-check.yml`](../.github/workflows/template-check.yml)
runs the cleanup on a copy of the repo and fails if anything template-only is left behind.
