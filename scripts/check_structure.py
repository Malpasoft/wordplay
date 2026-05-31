#!/usr/bin/env python3
"""
Structural consistency checker — run from repo root.
Verifies every content page has the expected shared furniture:
  - a breadcrumb trail
  - a site footer
  - a favicon link
  - base.css loaded
  - slides.html pages carry class="deck-body" on <body>

Top-level / utility pages (root index, track indexes, 404, graders, etc.)
are exempt from the breadcrumb rule — they legitimately have none.

Exit code 1 if any violation is found (so CI fails).
"""
import re, os, glob, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
violations = []
checked = 0

# Pages that legitimately have no breadcrumb (top-level / utility).
EXEMPT_BREADCRUMB = {
    'index.html', '404.html', 'test-grader.html',
    'progress-certificate.html', 'placement-test.html', 'dashboard.html',
}


def rel(path):
    return path.replace(BASE + '/', '')


def is_exempt_breadcrumb(path):
    r = rel(path)
    # root-level files and each track's own index page
    if r in EXEMPT_BREADCRUMB:
        return True
    if r.endswith('/index.html') and r.count('/') <= 1:
        return True  # e.g. es/index.html
    return False


def main():
    global checked
    for path in glob.glob(f'{BASE}/**/*.html', recursive=True):
        if '/shared/' in path:
            continue
        # printables & certificates are standalone print templates with their
        # own embedded styles — no shared furniture by design. Skip them.
        if path.endswith(('printables.html', 'certificate.html')):
            continue
        with open(path, encoding='utf-8') as f:
            h = f.read()
        # redirect stubs (renamed/merged chapters) are tiny meta-refresh pages
        # with no shared furniture by design — skip them.
        if 'http-equiv="refresh"' in h:
            continue
        checked += 1
        r = rel(path)

        if 'site-footer' not in h:
            violations.append(f"  MISSING FOOTER   {r}")
        if 'favicon' not in h:
            violations.append(f"  MISSING FAVICON  {r}")
        if 'base.css' not in h:
            violations.append(f"  MISSING base.css {r}")
        if not is_exempt_breadcrumb(path) and 'breadcrumb' not in h:
            violations.append(f"  MISSING CRUMB    {r}")
        if path.endswith('slides.html') and 'deck-body' not in h:
            violations.append(f"  MISSING deck-body {r}")

    print(f"Pages checked: {checked}")
    if violations:
        print(f"\nStructure issues: {len(violations)}")
        for v in sorted(violations):
            print(v)
        sys.exit(1)
    print("All pages structurally consistent.")


if __name__ == '__main__':
    main()
