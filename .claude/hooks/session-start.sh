#!/bin/bash
# Session Claude Code dans le cloud : dessiner les illustrations au démarrage.
# Les SVG ne sont pas suivis par git (voir outils/illustrer/empreintes.txt) ;
# sans eux, le site s'affiche sans images et verifier-images.py échoue.
# Aucune dépendance à installer : Python 3 et Node.js suffisent.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
python3 outils/illustrer/generer.py > /dev/null
echo "Illustrations dessinées ($(wc -l < outils/illustrer/empreintes.txt) SVG)."
