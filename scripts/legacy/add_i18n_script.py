#!/usr/bin/env python3
"""
Add <script src="../../../../shared/i18n.js?v=v123"></script>
before game.js/worksheet.js script tags in game.html and worksheet.html files.

Pattern: Insert i18n.js BEFORE the store.js line (which precedes game.js/worksheet.js)
"""

import os
import re
import sys

def process_file(filepath, module_name):
    """Add i18n.js script if not already present."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if i18n.js is already loaded
    if 'i18n.js' in content:
        return False, "Already has i18n.js"

    # For game.html: look for store.js pattern before game.js
    # For worksheet.html: look for store.js pattern before worksheet.js
    if module_name == 'game':
        pattern = r'(<script src="[^"]*shared/store\.js[^"]*"></script>)'
        module_pattern = 'game.js'
    else:  # worksheet
        pattern = r'(<script src="[^"]*shared/store\.js[^"]*"></script>)'
        module_pattern = 'worksheet.js'

    if not re.search(pattern, content):
        return False, f"Could not find store.js script tag"

    # Calculate relative path depth (number of ../ needed)
    depth = filepath.count('/') - filepath.find('/home/user/wordplay/') - len('/home/user/wordplay/')
    # Count the depth: each directory level needs one ../
    rel_path_parts = content.split('<script src="')
    if len(rel_path_parts) > 1:
        first_script_src = rel_path_parts[1].split('"')[0]
        # Count ../ in the path
        up_count = first_script_src.count('../')
    else:
        up_count = 4  # default for most files

    relative_path = '../' * up_count + 'shared/i18n.js?v=v123'

    # Insert i18n.js before store.js
    new_script = f'<script src="{relative_path}"></script>\n<script src="'
    content = re.sub(
        r'(<script src="[^"]*shared/store\.js[^"]*"></script>)',
        lambda m: f'<script src="{relative_path}"></script>\n{m.group(1)}',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, f"Added i18n.js before store.js"

def main():
    root = '/home/user/wordplay'

    # Process game.html files
    game_count = 0
    game_errors = []
    for dirpath, dirnames, filenames in os.walk(root):
        if 'game.html' in filenames:
            filepath = os.path.join(dirpath, 'game.html')
            success, msg = process_file(filepath, 'game')
            if success:
                game_count += 1
            elif "Already has" not in msg:
                game_errors.append(f"{filepath}: {msg}")

    # Process worksheet.html files
    ws_count = 0
    ws_errors = []
    for dirpath, dirnames, filenames in os.walk(root):
        if 'worksheet.html' in filenames:
            filepath = os.path.join(dirpath, 'worksheet.html')
            success, msg = process_file(filepath, 'worksheet')
            if success:
                ws_count += 1
            elif "Already has" not in msg:
                ws_errors.append(f"{filepath}: {msg}")

    print(f"Updated {game_count} game.html files")
    print(f"Updated {ws_count} worksheet.html files")
    if game_errors:
        print(f"Game.html errors: {len(game_errors)}")
        for err in game_errors[:5]:
            print(f"  {err}")
    if ws_errors:
        print(f"Worksheet.html errors: {len(ws_errors)}")
        for err in ws_errors[:5]:
            print(f"  {err}")

if __name__ == '__main__':
    main()
