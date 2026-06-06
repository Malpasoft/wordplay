#!/usr/bin/env python3
"""
Migrate hardcoded colors in printables.html files to CSS variables.
Replaces 299 printables with consistent color variable usage.
"""

import os
import re
import sys
from pathlib import Path

# Color mapping: hardcoded hex -> CSS variable name
COLOR_MAP = {
    # Accent colors
    '#B8860B': 'var(--print-accent)',

    # Borders
    '#ddd': 'var(--print-border)',
    '#999': 'var(--print-border-dark)',
    '#eee': 'var(--print-border-light)',

    # Text colors
    '#1A1A1A': 'var(--print-text-primary)',
    '#1a1a1a': 'var(--print-text-primary)',
    '#333': 'var(--print-text-secondary)',
    '#555': 'var(--print-text-tertiary)',
    '#666': 'var(--print-text-muted)',
    '#777': 'var(--print-text-light)',

    # White/light backgrounds
    '#fff': 'var(--print-text-white)',
    '#fffbf0': 'var(--print-hover-bg)',
}

# Keep unchanged (print essentials)
KEEP_COLORS = {
    '#000',      # black rules/underlines
    '#ccc',      # model text border (light)
    '#444',      # paragraph text muted
    '#aaa',      # rare usage
}

def migrate_file(filepath):
    """
    Replace hardcoded colors in a single printables.html file.
    Returns True if changed, False otherwise.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace each color with its variable equivalent
    for hex_color, var_name in COLOR_MAP.items():
        # Case-insensitive replacement, but preserve case in variable references
        content = re.sub(
            rf'\b{re.escape(hex_color)}\b',
            var_name,
            content,
            flags=re.IGNORECASE
        )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    repo_root = Path('/home/user/wordplay')

    # Find all printables.html files
    printables = sorted(repo_root.glob('**/printables.html'))

    if not printables:
        print("No printables.html files found.")
        sys.exit(1)

    print(f"Found {len(printables)} printables.html files to migrate.")

    changed_count = 0
    for filepath in printables:
        if migrate_file(filepath):
            changed_count += 1
            print(f"  ✓ {filepath.relative_to(repo_root)}")

    print(f"\nMigrated {changed_count}/{len(printables)} files.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
