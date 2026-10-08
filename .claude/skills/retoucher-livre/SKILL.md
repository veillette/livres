---
name: retoucher-livre
description: Revoir et améliorer les illustrations d'un livre déjà publié dans ce dépôt (cadrages répétitifs, pages vides, adultes dessinés comme des enfants, intérieurs génériques, nuits sans lumière, échelles fausses, petite bête manquante), avec une planche avant/après et sans changer les autres livres. À utiliser quand on demande de reprendre, embellir, corriger ou moderniser les images d'un ou plusieurs livres existants.
---

# Retoucher les illustrations d'un livre existant

Les règles de dessin sont dans [`direction-artistique`](../direction-artistique/SKILL.md) ;
cette compétence décrit le parcours pour reprendre un livre sans rien casser.
Lire d'abord [AGENTS.md](../../../AGENTS.md).

## 1. Regarder avant de toucher

```sh
NODE_PATH="$(npm root -g)" node .claude/skills/nouveau-livre/planche.js <id> /chemin/scratchpad/planche-<id>.html
```

Ouvrir la capture PNG et noter, page par page, ce qui ne va pas. Grille de
diagnostic :

| Défaut | Signe | Remède |
| --- | --- | --- |
| Plans répétitifs | trois pages de suite au même cadrage, personnages alignés au centre | `S.camera()` sur le moment fort, plan large pour un nouveau lieu |
| Page vide | sujet minuscule sur un aplat | gros plan, décor autour (jardin flou, feuillage net devant) |
| Âges confondus | parents, rois, grands-mères à la taille des enfants | `stature="adulte"` / `"ancien"`, `ancre()` pour les objets tenus |
| Personnages jumeaux | même silhouette, même visage | `carrure`, `nez`, `yeux`, coiffure, `taches` |
| Intérieur générique | mur rayé rose, cadre et fenêtre identiques à d'autres livres | `piece(S, style)` adapté au lieu du récit |
| Nuit sans lumière | fenêtre jaune plate, rue sans reflet | `S.lumiere()` sur chaque source, flaque au sol, `S.ambiance("nuit")` |
| Échelle fausse | château à hauteur de princesse | agrandir le décor, éloigner ou réduire le personnage |
| Petite bête absente | `generer.py` affiche `petite bête absente : …` | `cachettes.py` (section 4), ou `S.cachette(x, y)` à la main |
| Bête sur un personnage | planche `planche_cachettes.py` | `+ occuper(…)` sur le personnage maison, ou `S.cachette()` |
| Raideur | tout le monde face au lecteur, bras le long du corps | `regard=`, poses d'échange (`main`, `epaule`, `tend`…), `pas=` |

Pour placer des cachettes ou des gros plans au bon endroit, superposer une
grille de coordonnées (lignes tous les 100) sur la capture : les dessins sont
en 800 × 800.

## 2. Modifier le script du livre, pas le reste

- Tout se passe dans `outils/illustrer/histoires/<id_souligne>.py` (et
  `livres/<id>/livre.js` pour les descriptions).
- Un module partagé (`base.py`, `fantastique.py`…) ne change que par **ajout**
  (nouvelle fonction, nouveau paramètre avec valeur par défaut). Si un outil
  partagé doit changer pour tout le monde, c'est une **retouche globale** : la
  faire à part, l'annoncer, revoir des planches de tous les rayons.
- Garder les réglages des personnages dans des `dict` (`MAMAN`, `HEROS`…) :
  changer la stature d'un personnage se fait alors en un seul endroit.
- Après un changement de cadrage ou de composition, **réécrire la
  `description`** de la page dans `livre.js` (« Gros plan sur… »).

## 3. Régénérer et comparer

```sh
python3 outils/illustrer/generer.py <id>
NODE_PATH="$(npm root -g)" node .claude/skills/retoucher-livre/avant-apres.js <id> /chemin/scratchpad/avant-apres-<id>.html
```

`avant-apres.js` met chaque image du dernier commit (ou d'une référence
donnée en troisième argument) à côté de la nouvelle. Vérifier sur la capture :

- chaque retouche améliore la page (sinon revenir en arrière) ;
- rien n'a bougé sans raison sur les pages non retouchées ;
- la liste de contrôle de `direction-artistique` (section 7).

Écrire planches et captures dans le scratchpad, jamais dans le dépôt.

## 4. Compléter la petite bête cachée

La bête n'apparaît dans un livre que si elle est sur **toutes** ses pages
pleines ; `generer.py` nomme les pages qui manquent. Parcours :

```sh
python3 .claude/skills/retoucher-livre/cachettes.py <id>             # propose une place par page
python3 .claude/skills/retoucher-livre/cachettes.py --ecrire <id>    # l'écrit dans le script
python3 outils/illustrer/generer.py <id>
python3 .claude/skills/retoucher-livre/planche_cachettes.py /chemin/scratchpad/bete-<id>.html <id>
```

- `cachettes.py` rend chaque page sans cachette et choisit la zone calme
  (peu de détails, ni blanche ni rouge) la plus proche d'un bord, hors des
  zones réservées ; il ajoute `S.cachette(x, y, "air")` avant le
  `return S` de la fonction de la page (coordonnées de la scène, cadrage
  compris). Une page fabriquée par une fonction partagée ou sans
  `return S`, ou une page toute blanche (schéma), se complète à la main.
- `planche_cachettes.py` montre un gros plan centré sur la bête de chaque
  page (cercle pointillé), 48 par capture : vérifier qu'elle est posée sur
  un support plausible ou en vol, visible, jamais sur un personnage, une
  bulle ou un texte.
- Bête sur un personnage dessiné à la main : ajouter `+ occuper(…)` au
  dessin du personnage dans le script (corrige toutes ses pages), sinon
  `S.cachette()` sur la page.

## 5. Vérifier que les autres livres n'ont pas changé

```sh
python3 outils/illustrer/generer.py > /dev/null && git status --short -- livres
python3 outils/verifier-images.py      # doit finir par « 0 erreur(s). »
node --test
```

Seuls les SVG (et le `livre.js`) des livres retouchés doivent apparaître.

## 6. Documenter et committer

- `sw.js` : augmenter `VERSION` d'un cran (une fois par lot).
- `outils/REVUE-IMAGES.md` : section « Retouche du <date> » — livres repris,
  défauts corrigés (une ligne par livre), contrôles faits, nouvelle `VERSION`.
- Commit en français, à l'infinitif, par exemple :

```
Retoucher les illustrations du Petit Chaperon rouge

Chaumière de la mère-grand, adultes à leur taille, gros plans de plus en
plus serrés sur « grandes oreilles » et « grands yeux ». Le cache hors ligne
passe à v25.
```
