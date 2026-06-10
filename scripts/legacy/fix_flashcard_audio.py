#!/usr/bin/env python3
"""Add missing speakWord() function to English vocabulary flashcard files.

All 67 complete EN flashcards have the audio button (<button onclick="speakWord(event)">)
but no function definition. The ES flashcards have it inline. This script adds the function
before the existing 'var mastered = false;' line in each file.
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SPEAK_FUNC = '''function speakWord(e) {
  if (e) e.stopPropagation();
  if (!window.speechSynthesis) return;
  var utt = new SpeechSynthesisUtterance(WORDS[fcIdx].word);
  utt.lang = 'en-GB'; utt.rate = 0.9;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
}
'''

INSERT_BEFORE = 'var mastered = false;'

def fix_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    if 'function speakWord' in content:
        return 'already_has'
    if 'fc-audio-btn' not in content:
        return 'no_button'
    if INSERT_BEFORE not in content:
        return 'no_anchor'

    new_content = content.replace(INSERT_BEFORE, SPEAK_FUNC + INSERT_BEFORE, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return 'fixed'


def main():
    fixed = []
    skipped = []
    errors = []

    for dirpath, _dirs, files in os.walk(ROOT):
        for fname in files:
            if fname != 'flashcards.html':
                continue
            # Skip ES track (ES flashcards already have the function)
            rel = os.path.relpath(dirpath, ROOT)
            if rel.startswith('es' + os.sep) or rel.startswith('es/'):
                continue
            path = os.path.join(dirpath, fname)
            result = fix_file(path)
            if result == 'fixed':
                fixed.append(rel + '/flashcards.html')
            elif result == 'already_has':
                skipped.append(('already_has', rel))
            elif result == 'no_button':
                skipped.append(('no_button', rel))
            elif result == 'no_anchor':
                errors.append(('no_anchor', rel))

    print(f'Fixed: {len(fixed)}')
    for f in sorted(fixed):
        print(f'  + {f}')

    if errors:
        print(f'\nErrors (no anchor found):')
        for tag, rel in errors:
            print(f'  ! {rel}')

    if '--verbose' in sys.argv:
        print(f'\nSkipped:')
        for tag, rel in skipped:
            print(f'  {tag}: {rel}')


if __name__ == '__main__':
    main()
