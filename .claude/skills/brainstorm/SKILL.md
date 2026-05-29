# /brainstorm

Generate 3 distinct design directions for a UI/UX challenge, with tradeoffs and a recommendation. No implementation.

## Steps

### 0. Guard: require args
If the user provided no args (skill invoked with no text after `/brainstorm`), reply:
"What design challenge should I brainstorm? Example: `/brainstorm redesign the level hub cards`"
Then stop.

### 1. Spawn Explore agent
Spawn one agent with subagent_type "Explore", model "haiku", with this instruction:

> "Identify every file directly relevant to: {ARGS}.
> Look in: shared/base.css (report only the :root block), and any HTML/CSS files that implement the component or page mentioned.
> Output ONLY:
> - File paths found
> - The relevant HTML snippet (≤ 20 lines) or CSS rule block
> - Which CSS tokens from shared/base.css :root the component currently uses
> Cap your response at 300 words."

### 2. Synthesise options
Using the Explore agent's output, write exactly 3 numbered options. Each follows this template (2–4 lines max):

**Option N — [Short Name]**
Approach: [One sentence describing the visual/structural direction.]
Key changes: [2–3 specific things that would change.]
Tradeoff: [One clear downside or constraint.]

Rules:
- Each option must be visually distinct from the others (not just tonal variations).
- All options must respect: amber-only accent (--amber / --accent), no emojis outside ◐◑◆, dark mode via existing body.dark token overrides.
- Do not reference external libraries, fonts, or icons not already in the project.

### 3. Recommendation
Write a single paragraph (≤ 5 sentences) recommending one option and why, referencing the current component's constraints discovered in Step 1.

### 4. Hand off
End with exactly:
"Which option — 1, 2, or 3? Or describe a hybrid. Use `/frontend-design` to implement."

## Format rules
- Total output ≤ 40 lines.
- No headings beyond the option numbers.
- No code blocks.
- Do not implement anything.
