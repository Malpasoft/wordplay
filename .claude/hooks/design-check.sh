#!/bin/bash
# Runs after every Edit/Write — flags emoji and off-palette colour violations.
# Warnings only (exit 0); never blocks writes.

input=$(cat)
f=$(echo "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
[[ -z "$f" || ! -f "$f" ]] && exit 0
[[ "$f" != *.html && "$f" != *.css && "$f" != *.js ]] && exit 0

violations=$(python3 - "$f" <<'PYEOF'
import sys, re

path = sys.argv[1]
try:
    content = open(path, encoding='utf-8', errors='ignore').read()
except Exception:
    sys.exit(0)

msgs = []

# ── Emoji check ──────────────────────────────────────────────────────────────
# Allowed non-ASCII: ◐ (U+25D0), ◑ (U+25D1), ◆ (U+25C6), › (U+203A), ✓ (U+2713)
ALLOWED = {'◐', '◑', '◆', '›', '✓', '✕', '←',
           '→', '↓', '↑', '✓', '✔', '✗', '✘',
           '·', '«', '»', '…', '‘', '’', '“',
           '”', ' ', '▸', '▶', '◀', '•', '—',
           '–', '×', '÷', 'é', 'è', 'à', 'ü',
           'ä', 'ö', 'ñ', 'á', 'í', 'ó', 'ú'}
EMOJI_RE = re.compile(
    r'[\U0001F300-\U0001FAFF'   # Misc/transport/supplemental symbols
    r'\U00002600-\U000027BF'    # Misc symbols + dingbats
    r'\U0000FE00-\U0000FE0F'    # Variation selectors
    r'\U0001F900-\U0001F9FF]'   # Supplemental symbols
)
for m in EMOJI_RE.finditer(content):
    ch = m.group()
    if ch in ALLOWED:
        continue
    line = content[:m.start()].count('\n') + 1
    msgs.append(f'EMOJI line {line}: {repr(ch)} — design system bans emojis (only ◐◑◆ allowed)')
    if len(msgs) >= 3:
        break

# ── Off-palette colour check (CSS/HTML only) ─────────────────────────────────
if path.endswith(('.css', '.html')):
    AMBER_HEX = {'#e8a020','#b8860b','#c9a050','#d4a849','#e8a020'}
    NEUTRAL   = {'#1a1a1a','#fafafa','#fafaf8','#000000','#ffffff','#f5f5f0',
                 '#0e0e0e','#3a3a3a','#6b6b6b','#9b9b9b','#cccccc','#eeeeee',
                 '#f0f0f0','#e8e8e8','#d0d0d0'}
    for m in re.finditer(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', content):
        colour = m.group(0).lower()
        if colour in AMBER_HEX or colour in NEUTRAL:
            continue
        # Allow very light or very dark neutrals (greyscale)
        try:
            h = colour.lstrip('#')
            if len(h) == 3:
                h = ''.join(c*2 for c in h)
            r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
            # Skip if it's a greyscale-ish colour (R≈G≈B within 15)
            if max(r,g,b) - min(r,g,b) <= 20:
                continue
        except Exception:
            continue
        line = content[:m.start()].count('\n') + 1
        msgs.append(f'COLOUR line {line}: {colour} — amber-only accent; check design system')
        if len(msgs) >= 5:
            break

if msgs:
    print('\n'.join(msgs))
    sys.exit(1)
PYEOF
)

if [[ -n "$violations" ]]; then
  msg="Design-system check in $(basename "$f"):\n$violations"
  echo "{\"systemMessage\": \"$msg\"}"
fi

exit 0
