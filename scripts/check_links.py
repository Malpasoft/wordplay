#!/usr/bin/env python3
"""
Broken-link & asset checker — run from repo root.
Crawls every HTML file, resolves each local href/src, and reports any that
point to a file that does not exist. External (http/https), anchors (#...),
mailto:, tel:, and javascript: links are skipped.

Exit code 1 if any broken link is found (so CI fails).
"""
import re, os, glob, sys
from urllib.parse import urlparse, unquote

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
broken = []
checked = 0

# Pull href="..." and src="..." values
ATTR_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]*)"', re.IGNORECASE)


def is_external(link):
    if link.startswith(('http://', 'https://', '//', 'mailto:', 'tel:', 'javascript:', 'data:')):
        return True
    if link.startswith('#') or link.strip() == '':
        return True
    return False


# Characters that only appear when the "href" was actually inside a JS string
# being built by concatenation (e.g. '+d[0]+', ' + href + '). Real paths never
# contain these, so we skip such matches instead of false-flagging them.
JS_NOISE = set("+{}`<>$ ")


def is_js_fragment(link):
    return any(c in JS_NOISE for c in link) or "'" in link or '"' in link


def resolve(page_path, link):
    # strip query string (?v=v123) and anchor (#section)
    link = link.split('?', 1)[0].split('#', 1)[0]
    link = unquote(link)
    if link == '':
        return None
    page_dir = os.path.dirname(page_path)
    target = os.path.normpath(os.path.join(page_dir, link))
    return target


# Tool pages that GENERATE HTML in client-side JS template strings. Their
# href="..." values are content for the file they build (resolved relative to
# the OUTPUT location, not this page), so crawling them produces false positives.
EXEMPT_PAGES = {'builder.html'}


def main():
    global checked
    for path in glob.glob(f'{BASE}/**/*.html', recursive=True):
        if os.path.basename(path) in EXEMPT_PAGES:
            continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        for link in ATTR_RE.findall(html):
            if is_external(link) or is_js_fragment(link):
                continue
            target = resolve(path, link)
            if target is None:
                continue
            checked += 1
            if not os.path.exists(target):
                rel_page = path.replace(BASE + '/', '')
                broken.append(f"  BROKEN  {rel_page} -> {link}")

    print(f"Links checked: {checked}")
    if broken:
        print(f"\nBroken links: {len(broken)}")
        for b in sorted(set(broken)):
            print(b)
        sys.exit(1)
    print("No broken links.")


if __name__ == '__main__':
    main()
