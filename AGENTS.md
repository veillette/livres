# AGENTS.md

Consignes pour les agents de code (Claude Code, Codex, Copilot…) qui travaillent
dans ce dépôt. Le [README](README.md) reste la documentation de référence ; ce
fichier en résume l'essentiel et fixe les habitudes de travail.

## Le projet

Un site **entièrement statique** (HTML + CSS + JavaScript, sans dépendance ni
compilation) pour lire à l'écran et imprimer des livres illustrés pour enfants
de 2 à 8 ans, en **français**. Les illustrations sont des SVG produits par un
générateur Python sans dépendance (`outils/illustrer/`).

```
index.html, lire.html, imprimer.html   bibliothèque, lecteur, impression
css/, js/                              interface (aucun framework)
livres/<id>/livre.js                   texte et pages d'un livre
livres/<id>/images/                    illustrations (SVG générés)
livres/catalogue.js                    ordre d'affichage + rayons (RAYONS)
outils/illustrer/                      générateur des SVG (non publié)
outils/illustrer/histoires/<id>.py     dessins d'un livre (tirets → soulignés)
outils/verifier-images.py              vérification des livres et images
outils/imposition.test.js              tests de l'ordre des pages du livret
outils/REVUE-IMAGES.md                 journal de revue des illustrations
sw.js                                  service worker (VERSION du cache)
```

## Commandes

```sh
python3 -m http.server                        # voir le site : http://localhost:8000
python3 outils/illustrer/generer.py           # régénérer toutes les images
python3 outils/illustrer/generer.py <id>      # régénérer un seul livre
python3 outils/verifier-images.py             # vérifier livres et images (doit dire 0 erreur)
node --test                                   # tests de l'imposition du livret
```

La publication (`.github/workflows/pages.yml`) lance ces trois vérifications :
`verifier-images.py`, `node --test`, puis `generer.py` suivi de
`git status -- livres`. **Les SVG du dépôt doivent être exactement ceux que
produit le générateur** : après toute modification d'un script de dessin,
relancer `generer.py` et valider les SVG produits dans le même commit.

## Règles

- **Langue** : tout est en français — textes des livres, commentaires, noms de
  fonctions et de variables Python/JS, messages de commit, documentation.
- **Typographie française** dans les textes : guillemets « » avec une espace
  simple à l'intérieur (« Pas encore ! »), comme dans les livres existants, `…` (jamais
  `...`), pas d'espace avant la virgule ou le point. L'apostrophe droite `'`
  est acceptée. `verifier-images.py` signale une partie de ces fautes.
- **Aucune dépendance** : ni npm, ni pip, ni CDN. Le site doit fonctionner hors
  ligne et en ouvrant `index.html` depuis le disque.
- **Ne pas modifier les SVG à la main** : on modifie le script Python de
  `outils/illustrer/` puis on régénère.
- **Ne pas toucher aux autres livres** en en ajoutant un : `generer.py` est
  déterministe livre par livre ; si un ajout dans `base.py`, `objets.py`, etc.
  change des SVG existants, c'est une régression à corriger (sauf correction
  voulue et annoncée).
- **Après l'ajout d'un livre ou la modification d'images** : augmenter
  `VERSION` dans `sw.js` (`"v15"` → `"v16"`) et mettre à jour les totaux
  (livres, pages, SVG) du README (section « Dessiner les illustrations ») et
  de `outils/REVUE-IMAGES.md`, ainsi qu'une entrée « Ajout du … » dans ce
  dernier. `verifier-images.py` affiche les totaux exacts.
- Le contenu doit convenir à de jeunes enfants : bienveillant, sans violence
  gratuite, sans peur excessive ; les livres de sciences doivent être
  **physiquement exacts** (ombres opposées au Soleil, phases de la Lune,
  arc-en-ciel à l'opposé du Soleil, etc. : voir les outils de `sciences.py`).

## Créer un nouveau livre

Suivre la compétence **`nouveau-livre`** :
[`.claude/skills/nouveau-livre/SKILL.md`](.claude/skills/nouveau-livre/SKILL.md).
Elle décrit tout le parcours : choix du rayon et de l'identifiant, écriture du
texte, script d'illustration, `livre.js`, catalogue, cache, vérifications et
revue visuelle des planches.

## Git

- Messages de commit en français, à l'infinitif (« Ajouter… », « Corriger… »),
  avec un corps qui résume les livres ajoutés et les nouveaux totaux.
- Ne pas committer `__pycache__/`, `_site/` ni les planches de revue
  temporaires.
