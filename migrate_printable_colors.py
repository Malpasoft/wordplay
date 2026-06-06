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
COLOR_MAP = [
    # Order matters: longest/most specific first to avoid conflicts
    ('#F0F0F0', 'var(--print-background)'),  # light background
    ('#f5f0e8', 'var(--print-warm-bg)'),     # warm page background
    ('#f0f0f0', 'var(--print-background)'),  # light background (lowercase)
    ('#fffbf0', 'var(--print-hover-bg)'),    # light hover background
    ('#B8860B', 'var(--print-accent)'),      # amber accent
    ('#fff', 'var(--print-text-white)'),     # white text on buttons
    ('#ddd', 'var(--print-border)'),         # light borders
    ('#eee', 'var(--print-border-light)'),   # softer borders
    ('#999', 'var(--print-border-dark)'),    # darker borders
    ('#ccc', 'var(--print-model-border)'),   # model text left border
    ('#777', 'var(--print-text-light)'),     # light text
    ('#666', 'var(--print-text-muted)'),     # muted text
    ('#555', 'var(--print-text-tertiary)'),  # tertiary text
    ('#444', 'var(--print-instructions)'),   # instruction text
    ('#333', 'var(--print-text-secondary)'), # secondary text
    ('#1A1A1A', 'var(--print-text-primary)'), # primary text
    ('#1a1a1a', 'var(--print-text-primary)'), # primary text (lowercase)
]

def migrate_file(filepath):
    """
    Replace hardcoded colors in printables.html, but preserve meta tags.
    Returns True if changed, False otherwise.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Preserve meta tags by temporarily replacing them
    meta_tags = []
    def preserve_meta(match):
        meta_tags.append(match.group(0))
        return f'__META_TAG_{len(meta_tags)-1}__'

    # Find and preserve meta tags
    content = re.sub(r'<meta[^>]*>', preserve_meta, content)

    # Now replace colors throughout the file
    for hex_color, var_name in COLOR_MAP:
        content = content.replace(hex_color, var_name)

    # Restore meta tags
    for i, tag in enumerate(meta_tags):
        content = content.replace(f'__META_TAG_{i}__', tag)

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

    print(f"\nMigrated {changed_count}/{len(printables)} files.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
