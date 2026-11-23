# Glossary

The one place this repo defines its terms (ADR-0005). Other docs link here instead of defining a
term again, so a definition can't drift between copies. Beginner pages in
[`new-to-coding/`](new-to-coding/) may explain a term in context, but the definition is the one
here. Add a term when a newcomer would have to look it up.

| Term | Meaning |
|---|---|
| **ADR** | Architecture Decision Record: one short file recording a decision, why it was made, and what was rejected. Lives in [`adr/`](adr/). Never changed after it is accepted (ADR-0001). |
| **Agent** | An AI tool that reads and edits the repo and runs commands, such as Claude Code. In this repo, agents write most of the code and people decide (ADR-0004). |
| **Agent file** | An instruction file AI tools read: [`AGENTS.md`](../AGENTS.md), loaded automatically, and the `AGENTS_<topic>.md` topic files it lists for specialty detail (ADR-0003). |
| **Author** | The person directing the work in a session, who makes the decisions. Agents recommend; the author decides (ADR-0004). Not the same as whoever wrote a change or a proposal. |
| **Branch** | A separate line of work in a repository. You make changes on a branch so `main` stays working until the change is reviewed. |
| **CI** | Continuous integration: checks GitHub runs automatically on every pull request, such as tests and lint. Defined in [`.github/workflows/`](../.github/workflows/). |
| **Clone** | Your own full copy of a repository, downloaded to your computer. |
| **Commit** | A saved snapshot of changes, with a message saying what changed. History is a chain of commits. |
| **Conventional Commits** | A rule for commit messages: start with a type such as `feat:`, `fix:` or `docs:`, optionally with a scope, as in `feat(core):`. See [`conventions/commits.md`](conventions/commits.md). |
| **CVE** | Common Vulnerabilities and Exposures: a public ID, such as CVE-2024-12345, for one known security flaw in one piece of software. |
| **Dependabot** | A GitHub service that watches the packages this repo uses, alerts on known vulnerabilities, and opens pull requests to upgrade them (ADR-0006). |
| **Dependency** | A package written by someone else that this repo uses. Most code in a modern project is dependencies. |
| **Diff** | The lines a change adds and removes, shown side by side. Reviewers read the diff. |
| **GHSA** | GitHub Security Advisory: GitHub's ID for a vulnerability, often linked to a CVE. |
| **Layered commits** | Splitting a change into commits by type, in dependency order, so it can be reviewed one kind of change at a time (ADR-0002). |
| **Lint** | An automatic check for style problems and likely mistakes, run without executing the code. |
| **Lockfile** | A file, such as `package-lock.json` or `poetry.lock`, that records the exact version of every dependency, so every machine installs the same ones. |
| **`main`** | The default branch. It holds the reviewed, working version of the project. |
| **Merge** | Bringing a branch's commits into another branch, usually `main`. |
| **Merge commit** | A commit that joins a branch into `main` while keeping every commit from the branch. This repo merges this way (ADR-0002). |
| **Model tier** | How capable, and how expensive, an AI model is: fast, balanced or most capable. This repo picks the least expensive tier that does a task at full quality (ADR-0004). |
| **Proposal** | An argued design not yet decided, in [`proposals/`](proposals/). It authorizes no code until accepted. |
| **Pull request (PR)** | A request to merge a branch into `main`. It shows the diff, runs CI, and is where review happens. |
| **Push** | Sending your local commits to the copy of the repository on GitHub. |
| **Repository (repo)** | A project's files plus the full history of every change to them. |
| **Review** | Someone other than the change's writer reading it before it is merged, to catch what the writer missed. |
| **Scope** | The part of the project a commit touches, in parentheses after its type: `core` in `feat(core):`. |
| **Squash merge** | Merging a branch as one combined commit. This repo doesn't, because it throws away the layers (ADR-0002). |
| **Subagent** | A helper agent the main agent hands a bounded task to, often on a cheaper model tier. Defined in [`.claude/agents/`](../.claude/agents/) for Claude. |
| **Teaching mode** | An opt-in setting under which agents explain what they did and why, in plain words (ADR-0005). See [`AGENTS_teaching.md`](../AGENTS_teaching.md). |
| **Test** | Code that runs other code and checks that it gives the right result. |
| **Vulnerability** | A flaw that an attacker could use to do something the software shouldn't allow. |
| **Workflow** | A script GitHub runs for you on its own machines, such as CI. Files in [`.github/workflows/`](../.github/workflows/). |
