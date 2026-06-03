#!/bin/bash
# Copies project-level skills to the user Claude skills directory so they
# are available in every remote session. Add new skills under .claude/skills/.
set -euo pipefail

PROJ_SKILLS="$CLAUDE_PROJECT_DIR/.claude/skills"
USER_SKILLS="$HOME/.claude/skills"

if [ -d "$PROJ_SKILLS" ]; then
  for skill_dir in "$PROJ_SKILLS"/*/; do
    skill_name=$(basename "$skill_dir")
    dest="$USER_SKILLS/$skill_name"
    mkdir -p "$dest"
    cp -f "$skill_dir/SKILL.md" "$dest/SKILL.md" 2>/dev/null || true
  done
fi
