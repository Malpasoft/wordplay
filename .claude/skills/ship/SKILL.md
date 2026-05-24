# /ship

Check and deploy the current changes to production.

## Steps

1. **Confirm branch** — verify we are on `claude/github-workflow-setup-98Fbf` or `main`. If on another branch, stop and tell the user.

2. **Design system check** — scan all staged/modified HTML and CSS files for:
   - Any emoji characters (flag if found)
   - Any hex colours outside `#E8A020` (amber), `#1A1A1A` (ink), `#FAFAF8` (paper), `#000000` (dark header) — flag unexpected new colours
   - Any `onmouseover`/`onmouseout` inline hover handlers (should use `sect-card` CSS class instead)

3. **Commit** — stage all changes, write a clear commit message describing what changed and why (not just what).

4. **Push to main** — `git push origin HEAD:main`

5. **Confirm** — report the commit hash and tell the user Cloudflare Pages will deploy within ~2 minutes.
