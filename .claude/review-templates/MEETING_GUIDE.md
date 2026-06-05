# Team Review Meeting Guide

## How the Review Process Works

### Phase 1: The Meeting (Specialists Run in Parallel)
All three specialists audit their domains in parallel and generate proposals:

```bash
/ux-design-review
/pedagogy-review
/code-quality-review
```

Each specialist produces 5–10 proposals in JSON format, prioritized by impact.

### Phase 2: Review & Selection
You'll see:
- **Summary** from each specialist (issues found, themes)
- **High/Medium/Low priority** grouping
- **Full JSON array** of all proposals

**Your job:** Read through all proposals and select **1–2** to focus on this cycle.

### Phase 3: Implementation
Tell the team which proposals you've selected:

```
I'm approving these proposals:
1. ux-design-001: Dark mode contrast improvement
2. ped-pedagogy-001: FCE Part 2 exam prep gap

Proceed with implementation.
```

The specialists will:
- Implement the changes
- Test thoroughly (visual, functional, pedagogical)
- Commit with clear messages
- Present results with before/after evidence

### Phase 4: Results & Approval
You'll see:
- Code diff / before-after screenshots
- Test evidence (visual audit, test output, user feedback)
- Any side effects discovered

Approve or request revisions.

### Phase 5: Next Cycle Planning
After approval, the team reflects:
- "Did we miss anything in other domains?"
- "Do we need a junior specialist (graphic design, game design, accessibility)?"
- "What should we focus on next?"

---

## Proposal Selection Guidelines

### What Makes a Good Proposal?

**High Priority (implement first):**
- Fixes bugs that block learning (missing explanations, broken audio)
- Improves accessibility (keyboard nav, color contrast, WCAG compliance)
- Addresses content gaps (missing exam prep, incomplete chapters)
- Enhances core functionality (game engagement, dashboard insight)

**Medium Priority (implement second):**
- Improves code maintainability (reduce technical debt, refactor patterns)
- Polishes UX (spacing, typography, animations)
- Strengthens teacher tools (dashboard, profiles, insights)

**Low Priority (batch later):**
- Nice-to-have features (streaks, achievements)
- One-off cleanup (archive old scripts)
- Speculative improvements (hypothetical future features)

### Selection Strategy

- **Start small:** Pick 1–2 proposals per cycle, not 5.
- **Mix domains:** Don't only pick design or only pick pedagogy. Rotate focus.
- **Unblock others:** If two proposals depend on each other, do the prerequisite first.
- **Timeline awareness:** Save "large" scope proposals for longer sessions.

---

## Example Proposal JSON

```json
{
  "id": "ux-design-001",
  "title": "Increase dark mode text contrast on secondary elements",
  "category": "bug",
  "scope": "small",
  "priority": "high",
  "impact": "Improve readability for students in low-light environments; WCAG AA compliance",
  "description": "The `--muted` color (#6B6560 light / #9A9590 dark) on dark mode barely meets WCAG AA at 4.5:1. Consider lightening dark mode muted to #B0A8A0 or higher for better readability.",
  "files_affected": ["shared/base.css"],
  "success_metric": "Run contrast checker on dark mode text; verify all secondary text passes WCAG AAA (7:1)",
  "notes": "Check calendar.html, profile.html, chapter hubs for muted text impact."
}
```

---

## Workflow Shortcuts

### Running a Single Specialist
Want to focus on just one domain?

```bash
/ux-design-review       # Just UX/Design
# or
/pedagogy-review        # Just Learning
# or
/code-quality-review    # Just Engineering
```

### Spawning a Junior Specialist
When you need expert input on a specific domain:

```bash
/graphic-design-review  # (Create if needed)
/game-design-review     # (Create if needed)
/accessibility-audit    # (Create if needed)
```

The format is the same: SKILL.md file in `.claude/skills/`, outputs proposals.

---

## Tips for Maximum Value

1. **Run specialists in parallel** — they work independently, saves time
2. **Read all proposals before deciding** — you might find a hidden dependency
3. **Ask for clarification** — if a proposal is vague, ask the specialist for details
4. **Track approved proposals** — keep a list of what's been done (builds pride and momentum)
5. **Iterate on specialist roles** — if a specialist misses issues in their domain, adjust their audit checklist
6. **Celebrate wins** — when a proposal lands and improves the project, acknowledge it

---

## FAQ

**Q: Can I reject a proposal?**  
A: Yes. Explain why briefly, and the specialists will adjust future proposals.

**Q: What if a proposal is low priority but I really want it done?**  
A: Prioritize it! You're the product owner. Just note that picking low-priority items means fewer high-priority items get done this cycle.

**Q: Can multiple specialists work on one proposal?**  
A: Yes. If a proposal spans domains (e.g., "Add gamification streaks" involves both UX and Learning), both can collaborate.

**Q: What if I don't approve any proposals?**  
A: Totally fine. Ask the specialists to go deeper in a specific area next meeting, or to brainstorm new ideas.

**Q: How often should we have meetings?**  
A: As often as makes sense. Could be weekly, bi-weekly, or whenever you want a status update. No fixed schedule.

---

## Quick Reference: Specialist Checklists

### UX/Design Lead
- [ ] Sample 3–5 pages at desktop, mobile, dark mode
- [ ] Check brand consistency (amber-only rule, token usage)
- [ ] Verify dark mode contrast (WCAG AA minimum 4.5:1)
- [ ] Test keyboard navigation on 2 pages
- [ ] Check mobile touch targets (≥48×48px)

### Learning Expert
- [ ] Run `python3 scripts/pedagogy_check.py`
- [ ] Sample 3 chapters (A1, B1, C1) for explanations
- [ ] Verify A1 vocab audio functionality
- [ ] Check grammar progression difficulty
- [ ] Review exam prep coverage (FCE, CAE, CPE)

### Engineering Lead
- [ ] Run `python3 scripts/pedagogy_check.py`, `check_links.py`, `check_structure.py`
- [ ] Audit 3 shared/ engine files for code quality
- [ ] Sample 3 pages for HTML semantics (buttons, labels, headings)
- [ ] Check for hardcoded colors in HTML
- [ ] Look for console errors in dev tools

---

*Use this guide to run smooth, focused review cycles. Pick 1–2 proposals, implement them thoroughly, and iterate.*
