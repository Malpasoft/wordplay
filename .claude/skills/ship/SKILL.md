# /ship

Deploy the current changes: design-check → cache-bust → commit → push.

## Steps

### 1. Confirm branch
We must be on `claude/github-workflow-setup-98Fbf`. If not, stop and tell the user.

### 2. Design-system audit (staged + modified files)
Scan every staged/modified `.html`, `.css`, `.js` file for:
- **Emoji characters** — flag any outside the allowed set (◐ ◑ ◆). Fix before shipping.
- **Off-palette hex colours** — any `#RRGGBB` that isn't amber (`#E8A020`, `#B8860B`, `#C9A050`) or a neutral greyscale must be explained or removed.
- **Inline hover handlers** — `onmouseover`/`onmouseout` must use `sect-card` CSS class instead.

Fix all violations before proceeding.

### 3. Cache-bust check
If any file under `shared/` was modified:
1. Find which shared files changed: `git diff --name-only HEAD shared/`
2. For each changed file, identify the current `?v=vNN` version in consumer pages.
3. Bump all consumers to the new version with this idempotent pattern:
   ```python
   import glob
   OLD, NEW = "shared_file.ext?v=vOLD", "shared_file.ext?v=vNEW"
   for p in glob.glob('**/*.html', recursive=True):
       c = open(p).read()
       if OLD in c:
           open(p,'w').write(c.replace(OLD, NEW))
   ```
4. Verify: `grep -r "shared_file.ext?v=" --include="*.html" . | grep -v "v=vNEW" | wc -l` → must be 0.

### 4. Commit
Stage specific files (never `git add -A`). Message format:
```
<type>: <why the change was needed, one line>

<optional body: what changed and key decisions>

https://claude.ai/code/session_012MdyQ9zuDQKaoLMknxXJQo
```

### 5. Push
```bash
git push origin HEAD:main                          # deploys to Cloudflare Pages
git push -u origin claude/github-workflow-setup-98Fbf  # keeps dev branch in sync
```

### 6. Confirm
Report: commit hash, files changed, cache-bust bumps applied (if any), and "Cloudflare Pages deploys in ~2 minutes."
