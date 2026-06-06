#!/usr/bin/env python3
"""
Bump cache-bust versions for modified shared files.

Files that were modified and need version bumps:
- store.js: v105 → v106
- base.css: v123 → v124
- dark-init.js: v109 → v110
- mascot.js: v2 → v3
- game.js: v110 → v111
- worksheet.js: v107 → v108
- deck.js: v113 → v114
- game.css: v111 → v112
- writing-grader.js: v104 → v105
- sentence-grader.js: v103 → v104
"""

import os
import re
from pathlib import Path

# Version bumps: old → new
BUMPS = {
    ('store.js', 'v105'): 'v106',
    ('base.css', 'v123'): 'v124',
    ('dark-init.js', 'v109'): 'v110',
    ('mascot.js', 'v2'): 'v3',
    ('game.js', 'v110'): 'v111',
    ('worksheet.js', 'v107'): 'v108',
    ('deck.js', 'v113'): 'v114',
    ('game.css', 'v111'): 'v112',
    ('writing-grader.js', 'v104'): 'v105',
    ('sentence-grader.js', 'v103'): 'v104',
}

def bump_file(filepath):
    """Update version parameters in a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, IOError):
        return 0

    original = content

    # For each file/version pair, find and replace all occurrences
    for (filename, old_version), new_version in BUMPS.items():
        # Pattern: filename?v=version with various path prefixes
        # Covers: shared/file, ./shared/file, ../shared/file, ../../shared/file, etc.
        patterns = [
            f'({filename}\\?v=){re.escape(old_version)}',  # direct match
        ]

        for pattern in patterns:
            content = re.sub(pattern, f'\\1{new_version}', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

def main():
    root = Path('/home/user/wordplay')
    html_files = list(root.glob('**/*.html'))

    updated = 0
    for html_file in html_files:
        if bump_file(str(html_file)):
            updated += 1
            print(f'✓ {html_file.relative_to(root)}')

    print(f'\nTotal files updated: {updated}/{len(html_files)}')

if __name__ == '__main__':
    main()
