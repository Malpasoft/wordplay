#!/usr/bin/env python3
"""Validate inline <script> blocks in HTML files with node --check.

Usage: python3 scripts/validate_inline_js.py <file.html> [more.html ...]
Exits non-zero if any inline script block fails to parse.
Catches the bug class from past sessions: fullwidth commas, undefined
syntax, truncated blocks produced during batch generation.
"""
import re
import subprocess
import sys
import tempfile
import os

SCRIPT_RE = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', re.S | re.I)

def check_file(path):
    try:
        html = open(path, encoding='utf-8').read()
    except OSError as e:
        print(f"  ERROR  {path}: {e}")
        return False
    ok = True
    for i, m in enumerate(SCRIPT_RE.finditer(html), 1):
        js = m.group(1)
        if not js.strip():
            continue
        # fullwidth punctuation is never valid JS code punctuation
        for bad in ('，', '；', '（', '）'):
            if bad in js:
                print(f"  FAIL   {path} block {i}: fullwidth punctuation {bad!r} in JS")
                ok = False
        # curly quotes parse fine inside string literals — warn only
        for warn in ('“', '”'):
            if warn in js:
                print(f"  WARN   {path} block {i}: curly quote {warn!r} in JS (ok if inside a string)")
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(js)
            tmp = f.name
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0:
            msg = (r.stderr or r.stdout).strip().splitlines()
            print(f"  FAIL   {path} block {i}: {msg[0] if msg else 'syntax error'}")
            ok = False
    return ok

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    all_ok = True
    for path in sys.argv[1:]:
        if check_file(path):
            print(f"  OK     {path}")
        else:
            all_ok = False
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__':
    main()
