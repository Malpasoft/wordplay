# /smart-agent

Token-cost optimisation audit. Evaluates a planned task and outputs model-selection, batching, and context-trimming recommendations. Makes no changes.

## Decision tree (apply in order — use the cheapest tier that fits)

1. **direct-tool** — single file read, grep, or one-shot bash: no sub-agent needed.
2. **haiku** — read-only discovery across ≤ 10 files, no synthesis required.
3. **sonnet** — multi-file edits, light reasoning, or loops under 20 iterations. Default.
4. **opus** — architecture decisions, novel feature design, or cross-cutting tradeoffs only.

## Steps

### 0. Read task
If args were provided, treat them as the task description.
If no args, reply:
"Describe the task you are about to run. I will recommend the optimal model/agent strategy."
Then stop.

### 1. Decompose task into steps
Break the task into a numbered list of ≤ 15 atomic steps. For each step, note:
- Action type (read / edit / test / decide / deploy)
- Estimated file count
- Whether it depends on a prior step's output

### 2. Classify each step by model tier
For each step, assign one label from the decision tree. Output one line per step:
`Step N [TIER] — reason (e.g. "haiku — single-file read, no decisions")`

### 3. Identify batching opportunities
List pairs (or groups) of steps that:
- Have no output dependency on each other
- Can be parallelised into a single multi-agent spawn

For each batch write:
`Batch: Steps N + M — parallel haiku/sonnet spawn; saves ~X sequential round-trips`

### 4. Prioritised savings list
Output a ranked list (most savings first, max 6 items):

**1. [Highest saving]** — e.g. "Steps 3 + 4 are both haiku reads; batch into one parallel spawn."
**2.** — ...

### 5. Token-saving checklist
Output this checklist and mark each item Y (already satisfied) or N (action needed) based on the task as described:

- [ ] Scopes are narrow — agents receive only the files/dirs they need, not the full repo
- [ ] Parallel spawns used where steps are independent
- [ ] Explore agents capped at 300-word responses
- [ ] No full file dumps passed as context — pass file paths, let agents read them
- [ ] Bulk shell scripts avoided for < 50 files (use Edit tool per file instead)
- [ ] Opus reserved for architecture only — not used for edits or grep tasks

### 6. Recommendation summary
Write ≤ 5 sentences: the single biggest optimisation and the recommended agent topology (e.g. "Run Steps 1–3 as a parallel haiku batch, then one sonnet agent for Steps 4–7, then /ship directly — no opus needed.").

### 7. Remind user
End with:
"Planning-only output. No files changed. Proceed with the topology above, or use `/brainstorm` or `/frontend-design` to continue."
