# Word Play — Multi-Specialist Review System

## Overview

You now have a **three-specialist review board** that audits Word Play in parallel and proposes improvements. Think of it as a regular team meeting where:

1. **Three experts** (UX/Design, Learning/Pedagogy, Engineering) audit their domains
2. **Each proposes** 5–10 improvements (bugs, features, refactors, polish)
3. **You review** all 15–30 proposals and pick **1–2** to focus on
4. **They implement** thoroughly, test, and present results
5. **You approve** or request revisions
6. **Next cycle** repeats

---

## The Three Specialists

### 1. UX/Design Lead (`/ux-design-review`)
**Expertise:** Visual design, brand consistency, dark mode, responsive design, typography, animations, accessibility (WCAG)

**Audits:**
- CLAUDE.md design tokens (amber-only rule, colors, spacing)
- Page layouts (consistency, hierarchy, mobile responsiveness)
- Typography (font sizes, line heights, hierarchy)
- Dark mode rendering (contrast, color inversions)
- Interactive elements (buttons, forms, focus states)
- Animations and transitions

**Proposes:** Design polish, UX improvements, accessibility fixes, brand consistency

**Proposal ID pattern:** `ux-design-###`

---

### 2. Learning Expert (`/pedagogy-review`)
**Expertise:** Cambridge CEFR curriculum, student engagement, gamification, assessment design, exam prep alignment, scaffolding

**Audits:**
- PEDAGOGY.md principle enforcement (explanations, grading, audio, mastery)
- Chapter progression difficulty (A1 → C2)
- Game design (4-stage mastery engine, match game, XP system)
- Flashcard quality (word selection, pronunciation, examples)
- Worksheet design (question difficulty, grading, explanations)
- Teacher tools (dashboard insights, progress tracking)
- Exam prep (FCE, CAE, CPE coverage)
- Content gaps (stubs, missing explanations)

**Proposes:** Learning outcome improvements, student engagement features, curriculum gaps, assessment fixes

**Proposal ID pattern:** `ped-pedagogy-###`

---

### 3. Engineering Lead (`/code-quality-review`)
**Expertise:** HTML semantics, CSS architecture, JavaScript patterns, performance, accessibility compliance, technical debt, testing

**Audits:**
- Shared engine files (base.css, deck.js, store.js, game.js, etc.)
- HTML5 semantics (buttons vs divs, form labels, heading hierarchy)
- CSS organization (variables, specificity, dark mode)
- JavaScript patterns (module scope, event handling, state management)
- Performance (bundle size, render speed, asset optimization)
- Cache-bust versioning (`?v=` pinning)
- Test coverage (pedagogy_check.py, link validator, structure validator)
- Technical debt (stale scripts, deprecated patterns)

**Proposes:** Code refactors, performance optimizations, accessibility fixes, technical debt cleanup

**Proposal ID pattern:** `eng-code-###`

---

## How to Run a Meeting

### Step 1: Invoke All Three Specialists (Parallel)

```bash
/ux-design-review
/pedagogy-review
/code-quality-review
```

Run them all in the same message or consecutive messages. They work independently and won't block each other.

**Expected output per specialist:**
- Brief summary (pages audited, issues found, themes)
- 5–10 proposals in JSON format
- Organized by priority (high → medium → low)

### Step 2: Review All Proposals

You'll see 15–30 proposals total. Read through them all (typically 5–10 minutes):
- Skim high-priority items first
- Identify dependencies between proposals
- Note which ones align with your strategic goals

### Step 3: Select 1–2 to Implement

Tell the team which proposals you want to focus on:

```
Great work, team! I'm approving these two proposals:

1. ux-design-001: Increase dark mode text contrast
   (Scope: small, Priority: high)

2. ped-pedagogy-002: Add streak counter to dashboard
   (Scope: small, Priority: medium)

Please implement these. I want to see them live by [end of session/tomorrow/this week].
```

### Step 4: They Implement & Present Results

Each specialist:
1. **Implements** the code changes
2. **Tests** thoroughly (visual, functional, pedagogical, accessibility)
3. **Commits** with clear messages referencing the proposal ID
4. **Presents** before/after evidence

Example output:
```
✓ ux-design-001: IMPLEMENTED
   - Changed base.css --muted (dark): #9A9590 → #B0A8A0
   - Tested contrast on calendar.html, profile.html — all secondary text now passes WCAG AAA (7:1)
   - Committed: a1b2c3d "refactor(css): improve dark mode secondary text contrast"
   - Before: screenshot.png / After: screenshot.png
   - ✓ Approved
```

### Step 5: Approval & Next Steps

- **Approve:** Merge to main, celebrate, plan next cycle
- **Request revisions:** Tell them what needs adjustment
- **Ask questions:** Clarify if a proposal is vague or you want more detail

---

## Proposal Selection Strategy

### What to Pick

**High Priority (do first):**
- Bugs that block learning (missing explanations, broken audio)
- Accessibility fixes (keyboard nav, color contrast, WCAG)
- Content gaps (missing exam prep, incomplete chapters)
- Core functionality improvements (game engagement, teacher insights)

**Medium Priority (do next):**
- Code maintainability (reduce debt, refactor patterns)
- UX polish (spacing, typography, animations)
- Teacher tool enhancements (dashboard, profiles)

**Low Priority (batch later):**
- Nice-to-have features (streaks, achievements)
- Cleanup tasks (archive old scripts)

### Selection Tips

1. **Start small:** Pick 1–2 proposals per cycle. Prevents scope creep.
2. **Mix domains:** Rotate between design, learning, and engineering. Keeps the codebase balanced.
3. **Unblock dependencies:** If proposal B depends on proposal A, do A first.
4. **Consider effort:** "Large" scope proposals need longer sessions. "Small" proposals are quick wins.
5. **Align with goals:** Pick proposals that move toward your strategic priorities (student engagement, exam prep, etc.).

---

## Example Proposal Structure

```json
{
  "id": "ux-design-001",
  "title": "Increase dark mode text contrast on secondary elements",
  "category": "bug",
  "scope": "small",
  "priority": "high",
  "impact": "Improve readability in low-light; WCAG AA compliance",
  "description": "The --muted color on dark mode barely meets WCAG AA. Lighten it from #9A9590 to #B0A8A0 for better readability.",
  "files_affected": ["shared/base.css"],
  "success_metric": "Contrast checker confirms WCAG AAA (7:1). Manual test on calendar.html, profile.html.",
  "notes": "Check that amber still pops against new muted."
}
```

---

## Spawning Junior Specialists

As needs arise, you can create additional specialists for specific domains:

- **Graphic Design Specialist** — mascot enhancements, illustrations, icons, visual hierarchy
- **Game Design Specialist** — match.html variants, leaderboards, achievement systems
- **Accessibility Specialist** — WCAG compliance, screen reader testing, keyboard nav
- **DevOps Specialist** — Cloudflare configuration, CI/CD, edge functions

**To create a new specialist:**

1. Create `.claude/skills/junior-role-name/SKILL.md` (copy the pattern from existing skills)
2. Define their audit scope and proposal criteria
3. Invoke with `/junior-role-name` when you want their input
4. Add to next "full team meeting" as needed

---

## File Locations

```
.claude/
├── skills/
│   ├── ux-design-review/
│   │   └── SKILL.md                    ← UX/Design Lead audits & proposes
│   ├── pedagogy-review/
│   │   └── SKILL.md                    ← Learning Expert audits & proposes
│   └── code-quality-review/
│       └── SKILL.md                    ← Engineering Lead audits & proposes
│
└── review-templates/
    ├── MEETING_GUIDE.md                ← How to run review cycles
    ├── proposal-template.json           ← JSON structure for proposals
    └── REVIEW_ROADMAP.md               ← (Optional) Track proposals across sessions
```

---

## Workflow Commands

### Full Team Meeting (All Three)
```bash
/ux-design-review
/pedagogy-review
/code-quality-review
```

### Single Specialist (Focus on One Domain)
```bash
/ux-design-review        # Just design
/pedagogy-review         # Just learning
/code-quality-review     # Just engineering
```

### Check Meeting Guide
```bash
cat .claude/review-templates/MEETING_GUIDE.md
```

---

## FAQ

**Q: How often should we meet?**  
A: As often as you want. Weekly, bi-weekly, or whenever you want to review progress. No fixed schedule.

**Q: Can I reject a proposal?**  
A: Absolutely. Explain why, and they'll adjust future proposals.

**Q: What if one proposal is very large (scope: large)?**  
A: That's fine. Just know it will take longer. Consider batching two "large" proposals with one "small" one.

**Q: Can specialists collaborate on a single proposal?**  
A: Yes. If a proposal spans domains (e.g., "Gamification streaks" involves UX and Learning), both can work together.

**Q: Do I have to approve proposals in order of priority?**  
A: No. You can pick any 1–2 you want. Just note that picking low-priority items means fewer high-priority items get done this cycle.

**Q: What if I don't approve any proposals?**  
A: That's fine. Ask the specialists to go deeper in a specific area next meeting, or to brainstorm new ideas.

**Q: How do I track approved proposals across sessions?**  
A: Use `REVIEW_ROADMAP.md` (optional file in `.claude/review-templates/`). Add a running log of approved proposals and their status.

---

## Success Metrics

This system works well if:
1. ✅ Specialists can run in parallel and finish in <30 min each
2. ✅ You can read all 15–30 proposals in ~5–10 minutes
3. ✅ You pick 1–2 proposals per cycle and see them completed
4. ✅ Implemented proposals improve the codebase (students, teachers, developers all benefit)
5. ✅ No decision paralysis — you know exactly what's being proposed and why

---

## Next Steps

1. **Run your first meeting:**
   ```bash
   /ux-design-review
   /pedagogy-review
   /code-quality-review
   ```

2. **Review the proposals** — read through all of them
3. **Select 1–2** — tell the team which to implement
4. **See them implemented** — review before/after evidence
5. **Iterate** — next cycle, adjust specialist focus if needed

---

*You're now set up for steady, structured improvement to Word Play. Each cycle builds on the last.*
