# Learning path

For people who can code and know basic git, but are new to how this repo works (ADR-0005). New to
coding altogether? Start with [`new-to-coding/`](new-to-coding/) instead, then come back here.

## Read, in this order

1. [`README.md`](../README.md): what the repo is.
2. [`STARTING_POINT.md`](../STARTING_POINT.md): the principles and why each piece of the scaffold
   exists. If it has been deleted, its content lives on in the files below.
3. [`AGENTS.md`](../AGENTS.md): the rules everyone works from, people and agents alike.
4. The ADRs in [`adr/`](adr/), starting with ADR-0001 to ADR-0004. Read each one's "Alternatives
   considered": it is the part you can't learn anywhere else.
5. [`conventions/commits.md`](conventions/commits.md): how layered commits work in practice.

Look up any unfamiliar term in the [glossary](glossary.md).

## Practice

Each exercise happens on a throwaway branch that you delete afterwards, so nothing reaches `main`.
Turn on teaching mode first (see [`AGENTS.md`](../AGENTS.md)) if you'd like your agent to explain
as you go.

### 1. Write a practice ADR

Pick a small decision this repo hasn't made, such as how to name test files.

1. `git switch -c practice/adr`
2. Copy [`adr/template.md`](adr/template.md) to the next free number and fill it in. Spend most
   effort on "Alternatives considered".
3. Ask the `reviewer` subagent, or a teammate, to review it. Compare their questions with what you
   wrote.
4. `git switch main && git branch -D practice/adr`

### 2. Turn a messy branch into layered commits

1. `git switch -c practice/layers`
2. Make three small changes in this order: a docs edit, a new file under a made-up `core/` folder,
   and a line in [`next-steps.md`](next-steps.md). Commit them all as one commit called `wip`.
3. Restage them into layers, following "Restaging work done out of order" in
   [`conventions/commits.md`](conventions/commits.md), with `git reset --soft HEAD~1` as the first
   step.
4. Check `git log --oneline`: the commits should read in dependency order with the right prefixes.
5. `git switch main && git branch -D practice/layers`

### 3. Review a pull request with a fresh pair of eyes

1. Open any recent pull request, or your branch from exercise 2.
2. Review it yourself first and write down what you'd raise.
3. Ask the `reviewer` subagent to review the same change.
4. Compare the two lists. What did each of you catch that the other missed?
