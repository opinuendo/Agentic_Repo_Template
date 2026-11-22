# Your first contribution

You'll add one missing term to the [glossary](../glossary.md) and take it all the way to a merged
pull request. The change is small on purpose: the point is the process.

**You need:** git installed, a GitHub account, and permission to push to this repo. (If you don't
have permission, ask a maintainer, or use GitHub's "fork" button and the
[GitHub Skills course](https://github.com/skills/introduction-to-github) to learn that variation.)

Each step shows the command, then what it does. You can ask your agent to run them for you, but
type them yourself the first time.

## 1. Get the code

```bash
git clone <this repo's URL>
```

Downloads a full copy of the repo. Then move into it:

```bash
cd <repo-name>
```

## 2. Make a branch

```bash
git switch -c docs/add-glossary-term
```

Creates a branch and moves you onto it. The name follows this repo's pattern: a type, a slash, and
a short description.

## 3. Make the change

Open `docs/glossary.md` in your editor. Pick a term you had to look up while reading this repo that
isn't there yet, and add a row in alphabetical order. Write the meaning the way you'd have wanted
it explained to you.

## 4. Commit it

```bash
git add docs/glossary.md
```

Marks the file as part of your next commit.

```bash
git commit -m "docs: add <term> to the glossary"
```

Saves the commit. `docs:` is the type, because you changed documentation.

## 5. Push and open a pull request

```bash
git push -u origin docs/add-glossary-term
```

Sends your branch to GitHub. The output prints a link: open it, and GitHub offers to create a pull
request. Fill in the template it shows you. For "Not done or not verified", "Nothing" is a fine
answer.

## 6. Watch the checks

On the PR page, the checks run within a minute or two. If one fails, click **Details** and read the
message. A failed commit-message check means the message needs a type at the start; ask your agent
how to reword a commit, or ask a reviewer.

## 7. Respond to review

A reviewer may ask for changes. Make them on the same branch, commit, and push again; the PR
updates by itself. Reply to each comment so the reviewer knows it is handled.

## 8. Merged

A maintainer merges your PR with a merge commit. Your change is now in `main`, and your commit is
in the history with your name on it.

Clean up your local copy:

```bash
git switch main
```

```bash
git pull
```

Next: the [learning path](../learning-path.md), for how this repo's practices work.
