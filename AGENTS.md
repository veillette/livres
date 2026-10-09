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
livres/<id>/images/                    illustrations (SVG générés, non suivis par git)
livres/catalogue.js                    ordre d'affichage + rayons (RAYONS)
outils/illustrer/                      générateur des SVG (non publié)
outils/illustrer/histoires/<id>.py     dessins d'un livre (tirets → soulignés)
outils/illustrer/empreintes.txt        empreinte de chaque SVG généré (suivie par git)
outils/verifier-images.py              vérification des livres et images
outils/imposition.test.js              tests de l'ordre des pages du livret
outils/REVUE-IMAGES.md                 journal de revue des illustrations
sw.js                                  service worker (VERSION du cache)
.claude/skills/                        compétences : nouveau-livre, direction-artistique, retoucher-livre
.claude/hooks/session-start.sh         dessine les SVG au démarrage d'une session cloud
```

## Commandes

```sh
python3 outils/illustrer/generer.py           # dessiner toutes les images (à faire après un clone)
python3 -m http.server                        # voir le site : http://localhost:8000
python3 outils/illustrer/generer.py <id>      # régénérer un seul livre
python3 outils/verifier-images.py             # vérifier livres et images (doit dire 0 erreur)
node --test                                   # tests de l'imposition du livret
```

**Les SVG ne sont pas suivis par git** (`.gitignore`) : la publication
(`.github/workflows/pages.yml`) les dessine avec `generer.py`, vérifie que
`outils/illustrer/empreintes.txt` n'a pas changé (`git status`), puis lance
`verifier-images.py` et `node --test`. `generer.py` réécrit ce fichier
d'empreintes (une ligne par image) : après toute modification d'un script de
dessin, relancer `generer.py` et valider `empreintes.txt` dans le même commit.
`git diff -- outils/illustrer/empreintes.txt` liste les images modifiées.
Dans une session Claude Code dans le cloud, le hook de démarrage
(`.claude/hooks/session-start.sh`, déclaré dans `.claude/settings.json`)
lance `generer.py` : les images sont déjà là.

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
  change des lignes d'autres livres dans `empreintes.txt`, c'est une régression à corriger (sauf correction
  voulue et annoncée).
- **Après l'ajout d'un livre ou la modification d'images** : augmenter
  `VERSION` dans `sw.js` (aujourd'hui `"v28"`, donc `"v28"` → `"v29"`) et
  mettre à jour les totaux (livres, pages, SVG) du README (section
  « Dessiner les illustrations ») et de `outils/REVUE-IMAGES.md`, ainsi
  qu'une entrée « Ajout du … » dans ce dernier. `verifier-images.py` affiche
  les totaux exacts.
- **Documentation à jour** : dans le même changement, relire les textes qui
  décrivent ce qui a bougé et les corriger. Le README porte les commandes,
  les types de pages, l'arborescence et les totaux ; ce fichier et les
  compétences `.claude/skills/` portent les règles, la liste des rayons et
  les exemples de `VERSION` ; `outils/REVUE-IMAGES.md` porte les totaux en
  tête et une entrée datée (les entrées anciennes ne se réécrivent pas).
  Les chiffres vivants se vérifient avec `python3 outils/verifier-images.py`
  et la constante `VERSION` de `sw.js`.
- Le contenu doit convenir à de jeunes enfants : bienveillant, sans violence
  gratuite, sans peur excessive ; les livres de sciences doivent être
  **physiquement exacts** (ombres opposées au Soleil, phases de la Lune,
  arc-en-ciel à l'opposé du Soleil, etc. : voir les outils de `sciences.py`).
- **Finition partagée** : `Scene.svg()` pose sur chaque page la lumière de son
  moment (`AMBIANCES` de `base.py` : nuit bleutée, soir doré, intérieur,
  sous l'eau…), les halos des sources de lumière et la petite bête cachée ;
  `generer.py` règle la patine des fables et des contes, et coupe teinte et
  halo en sciences. Le grain du papier est dans `css/pages.css`, pas dans les
  SVG. Toucher à cette finition change **tous** les SVG : le faire exprès,
  l'annoncer dans le commit et `outils/REVUE-IMAGES.md`, revoir des planches
  de tous les rayons.

## Direction artistique

Toute illustration, nouvelle ou reprise, suit la compétence
**`direction-artistique`**
([`.claude/skills/direction-artistique/SKILL.md`](.claude/skills/direction-artistique/SKILL.md)).
L'essentiel :

- **Cadrage varié** : pas plus de deux pages de suite au même plan ; un gros
  plan (`S.camera(zoom, cx, cy)`) aux moments forts, les bulles posées hors
  zoom avec `S.dessus()` ; pas de page presque vide.
- **Personnages crédibles** : adultes `stature="adulte"`, grands-parents
  `"ancien"`, tout-petits `"petit"` ; varier `carrure`, `nez`, coiffures ;
  objets tenus recalés avec `ancre()` ou `mains_personne()`. Les personnages
  se regardent (`regard=`) et interagissent (poses `main`, `epaule`, `tend`…).
- **Lumière** : la nuit, chaque fenêtre éclairée, lampe ou feu a son halo
  (`S.lumiere()`, automatique pour la lune, `maison(lumiere=True)`, `lampe`,
  `luciole`) ; `S.ambiance()` si le décor ne dit pas le bon moment.
- **Décors propres à chaque livre** : `piece(S, "chaumiere" | "manoir" |
  "chateau" | "chambre" | "cuisine")` plutôt que toujours le même mur ;
  `interieur(papier=…)` prend le papier peint du livre.
- **Échelles cohérentes** d'une page à l'autre (un château domine une
  princesse, un enfant arrive à la taille d'un adulte…).
- **Petite bête cachée** (coccinelle, posée ou en vol ; étoile de mer ou
  petit poisson sous l'eau) : elle doit être sur **toutes** les pages pleines
  du livre, sinon `generer.py` la retire du livre et l'écrit (`petite bête
  absente : …`) ; compléter avec `S.cachette(x, y)` ou l'outil
  `retoucher-livre/cachettes.py` (`--verifier` pour contrôler les places).
  Un personnage dessiné à la main dans un script ajoute `occuper(x0, y0, x1,
  y1)` à son dessin (repère local) pour que la bête ne s'y pose pas ; une
  page dans l'espace se met hors du jeu avec `S.cachette(None)`.

Pour revoir et améliorer un livre existant, suivre **`retoucher-livre`**
([`.claude/skills/retoucher-livre/SKILL.md`](.claude/skills/retoucher-livre/SKILL.md)).

## Créer un nouveau livre

Suivre la compétence **`nouveau-livre`** :
[`.claude/skills/nouveau-livre/SKILL.md`](.claude/skills/nouveau-livre/SKILL.md).
Elle décrit tout le parcours : choix du rayon et de l'identifiant, écriture du
texte, script d'illustration (selon `direction-artistique`), `livre.js`,
catalogue, cache, vérifications et revue visuelle des planches.

## Git

- Messages de commit en français, à l'infinitif (« Ajouter… », « Corriger… »),
  avec un corps qui résume les livres ajoutés et les nouveaux totaux.
- Ne pas committer `__pycache__/`, `_site/`, les SVG générés (ignorés par
  git ; `git add -f` seulement pour un SVG fait à la main) ni les planches de
  revue temporaires.
