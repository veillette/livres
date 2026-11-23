#!/usr/bin/env bash
set -euo pipefail

# Le script de vérification prépare les illustrations et vérifie leurs empreintes.
rsync -a --delete --delete-excluded \
  --include='/.nojekyll' --include='/*.html' \
  --include='/manifest.webmanifest' --include='/sw.js' \
  --include='/css/***' --include='/icones/***' --include='/js/***' \
  --include='/livres/***' --include='/polices/***' --exclude='*' ./ _site/
python3 outils/nouveautes.py --sortie _site/livres/nouveautes.js
