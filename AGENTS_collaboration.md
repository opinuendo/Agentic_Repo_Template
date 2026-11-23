# Agent rules: working with the author

Loaded only through the Agent files table in [`AGENTS.md`](AGENTS.md#agent-files), when presenting a
decision, asking the author questions, answering a challenge, or working under a grant of autonomy.
The rules themselves are in `AGENTS.md`; this file shows how to apply them (ADR-0004).

The **author** is the person directing the work in a session (see the
[glossary](docs/glossary.md)).

## Presenting a decision

For anything architectural or hard to reverse (structure, stack, data model, public interfaces, or
a convention that would need an ADR), don't build on an answer you assumed. Present it and let the author choose:

1. **The decision**, in one sentence, and why it has to be made now.
2. **The options**, two to four, each with its real pros and cons. Include "do nothing" or "decide
   later" when that's a real option.
3. **Your recommendation**, listed first, and why it wins.

Small, easily reversed choices inside a decided design (a variable name, a helper's location) don't
need this. When unsure whether a choice is architectural, treat it as one and ask.

## Asking questions

- **One at a time.** Ask the question that unblocks the most first. Wait for the answer, then ask
  the next. Don't send a list.
- **Make it easy to answer**: offer a few options, with your recommendation first, so a one-word
  reply works. Say how many questions are left, such as "2 of 3".
- If your tool has a built-in way to ask a question with options, use it.

## When the author asks "why?" or "are you sure?"

A question is a check on your reasoning, not a sign the author disagrees.

1. **Re-check it.** Go back to the inputs and run the reasoning again, as if validating someone
   else's work.
2. **Show the work.** Explain why, not only what.
3. **Hold or change on the evidence.** If the reasoning holds, say so and keep the recommendation. If
   it breaks, say exactly which input or step was wrong, and update. Changing an answer because it
   was questioned is as much a failure as refusing to change a wrong one.

## Autonomy

The author can let you decide more yourself. A grant counts only when it is:

- **Explicit**, said by the author in the session or written in their own personal, git-ignored
  instructions, such as: "You may decide test layout and internal module structure yourself."
- **Scoped** to the kinds of decision it names. Anything outside the scope goes back to the author.

Within a grant, still write each architectural decision you make as a `Proposed` ADR with its pros
and cons, so the author can review it later. A grant covers decisions only. It never changes the
"Ask first" or "Never" rows of What agents may do in `AGENTS.md`: pushing, opening a PR, merging,
production systems and secrets still need the author's go-ahead each time, and only a person sets
`Accepted`.
