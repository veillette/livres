#!/usr/bin/env bash
set -euo pipefail

python3 outils/illustrer/generer.py >/dev/null
artefacts=(outils/illustrer/empreintes.txt ':(glob)livres/**/images/*.svg')
if [ -n "$(git status --porcelain -- "${artefacts[@]}")" ]; then
  echo "Les empreintes des illustrations ont changé. Vérifier le résultat du générateur."
  git status --short -- "${artefacts[@]}"
  git diff --stat -- "${artefacts[@]}"
  exit 1
fi
python3 outils/verifier-images.py
node --test outils/*.test.js
