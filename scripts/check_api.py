#!/usr/bin/env python3
"""
API smoke check — guards the Cloudflare Pages Functions layer.

For every functions/api/**/*.js file:
  1. Syntax-check with `node --check` (catches errors that would 500 the worker).
  2. Verify it exports at least one onRequest handler (onRequestGet/Post/Put/Delete
     or a generic onRequest), so the route actually responds.

Also sanity-checks migrations/*.sql for balanced parentheses.

Exit non-zero on any failure. Pure stdlib + node; fits the python CI.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_DIR = ROOT / "functions" / "api"
MIG_DIR = ROOT / "migrations"

HANDLER_RE = re.compile(r"export\s+(async\s+)?function\s+(onRequest\w*)")
EXPORT_CONST_RE = re.compile(r"export\s+const\s+(onRequest\w*)")

failures = []
checked = 0


def check_js(path: Path):
    global checked
    rel = path.relative_to(ROOT)
    # 1. syntax
    res = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
    if res.returncode != 0:
        failures.append(f"SYNTAX  {rel}: {res.stderr.strip().splitlines()[-1] if res.stderr else 'parse error'}")
        return
    # 2. handler export — skip shared libs (_lib, _shared.js)
    if path.name.startswith("_") or "/_lib/" in str(path):
        checked += 1
        return
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not (HANDLER_RE.search(text) or EXPORT_CONST_RE.search(text)):
        failures.append(f"NO-HANDLER  {rel}: no onRequest* export found")
    checked += 1


def check_sql(path: Path):
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.count("(") != text.count(")"):
        failures.append(f"SQL  {rel}: unbalanced parentheses")


def main():
    if API_DIR.exists():
        for p in sorted(API_DIR.rglob("*.js")):
            check_js(p)
    if MIG_DIR.exists():
        for p in sorted(MIG_DIR.glob("*.sql")):
            check_sql(p)

    print(f"  Checked {checked} API files, {len(list(MIG_DIR.glob('*.sql')))} migrations")
    if failures:
        print("\n  API CHECK FAILURES:")
        for f in failures:
            print("  " + f)
        print(f"\n  Failures: {len(failures)}")
        sys.exit(1)
    print("  Failures: 0")


if __name__ == "__main__":
    main()
