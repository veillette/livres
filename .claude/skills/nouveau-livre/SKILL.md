---
name: nouveau-livre
description: Créer un nouveau livre illustré pour enfants dans ce dépôt (texte, illustrations SVG générées en Python, livre.js, catalogue, cache hors ligne, vérifications et revue des planches). À utiliser dès qu'on demande d'ajouter, d'écrire ou d'illustrer un ou plusieurs livres, une histoire, une fable, un conte ou un livre de sciences.
---

# Créer un nouveau livre

Parcours complet pour ajouter un livre au catalogue, du texte à la
publication. Lire d'abord [AGENTS.md](../../../AGENTS.md) (règles du dépôt) ;
le [README](../../../README.md) détaille les types de pages et le générateur.

Pour plusieurs livres, faire les étapes 1 à 5 pour chacun, puis les étapes 6
à 9 une seule fois pour l'ensemble.

## 1. Cadrer le livre

- **Rayon** : un identifiant de `RAYONS` en bas de `livres/catalogue.js`
  (`sciences`, `animaux`, `histoires`, `comptines`, `feerie`, `fables`,
  `contes`). En
  ajouter un seulement si on le demande.
- **Identifiant** : court, minuscules, chiffres et tirets, unique dans
  `livres/` (ex. `ours-gateau`, `lina-aimant`). Le script de dessin
  s'appellera `outils/illustrer/histoires/<id avec soulignés>.py`.
- **Âge** : une des tranches déjà utilisées (`"2 à 5 ans"`, `"3 à 6 ans"`,
  `"3 à 7 ans"`, `"4 à 7 ans"`, `"4 à 8 ans"`, `"5 à 8 ans"`).
- **Couleur** : une couleur vive de la palette Open Color, comme les autres
  livres (`#4263eb`, `#e8590c`, `#2f9e44`, `#ae3ec9`, `#f08c00`…), distincte
  de celles des livres voisins du même rayon.
- S'inspirer d'un livre du même rayon pour le ton, la longueur et la
  structure : lire son `livre.js` **et** son script de dessin.

## 2. Écrire le texte

Structure habituelle (12 à 17 pages au total, souvent 16) :

1. `couverture` ;
2. `titre`, avec une petite vignette et une dédicace courte dans `texte` ;
3. 8 à 12 pages `illustration`, une scène chacune ;
4. éventuellement une page « Comment ça marche ? » (sciences) ou la morale
   (fables) ;
5. `texte` : « Fin » ;
6. `quatrieme`, avec la vignette.

Consignes d'écriture :

- 1 à 4 phrases courtes par page, au plus ~45 mots ; paragraphes séparés par
  `\n\n`. Répétitions, onomatopées et dialogues bienvenus pour les petits.
- Typographie française : « … » avec espaces simples à l'intérieur, `…`
  jamais `...`, pas d'espace avant `,` ou `.`.
- Chaque page a une `description` (texte alternatif) qui décrit fidèlement
  **ce que montre le dessin** : elle sert de cahier des charges pour
  l'illustration et de contrôle pendant la revue.
- `resume` : 2 à 3 phrases pour la quatrième de couverture.
- Sciences : notions **exactes** (vérifier la physique), une expérience ou une
  observation que l'enfant peut refaire, vocabulaire simple mais juste.
- Fables et contes : rester fidèle à l'œuvre, adoucir la violence pour l'âge.

## 3. Dessiner les illustrations

Créer `outils/illustrer/histoires/<id_souligne>.py` sur le modèle
d'`ours_gateau.py` :

```python
"""Titre du livre — thème en quelques mots."""
from base import *
from objets import *          # selon les besoins : fantastique, contes, fables, sciences

ID = "mon-livre"
HEROS = dict(couleur="#ffa94d", acc=("echarpe",))   # réglages réutilisés du personnage


def decor(S):
    ciel(S)
    collines(S, 560)
    sol(S, 640)


def couverture():
    S = Scene()                       # 800 × 800 par défaut
    decor(S)
    S.add(perso("renard", 400, 740, 1.7, expr="rire", bras="haut", **HEROS))
    return S


def vignette():
    S = Scene(400, 270)               # petite image des pages titre et quatrième
    S.add(perso("renard", 200, 262, 0.95, expr="content", **HEROS))
    return S


def p01():
    S = Scene()
    decor(S)
    ...
    return S


IMAGES = [
    ("couverture.svg", couverture), ("renard-seul.svg", vignette),
    ("01-au-reveil.svg", p01),
    # ...
]
```

- Réutiliser au maximum les briques existantes : chercher avant de dessiner
  (`grep -n "^def " outils/illustrer/*.py`).
  - `base.py` : `Scene`, formes, décors (`ciel`, `nuit`, `interieur`,
    `collines`, `eau`…), `perso(espece, …)` avec `ESPECES`, `EXPRESSIONS`,
    `POSES` (dont `danse`, `applaudit`, `victoire`, `coucou`, `chut`,
    `etire`, `epaules`, `marche`), `pas=` / `penche=` pour varier
    l'attitude, accessoires, oiseaux, chouette, escargot, poisson, tortue,
    `bulle`, `pensee` ; mettre `OMBRES_DOUCES = False` dans le script d'un
    livre qui dessine ses propres ombres portées (`sciences.py`) ;
  - relief (`base.py`) : chaque aplat reçoit automatiquement un léger
    dégradé à l'écriture de la page ; pour aller plus loin, `volume()`,
    `cylindre()`, `lineaire()`, `radial()` (remplissages), `ombre_sol()`,
    `ombre_avancee()` (sous un toit), textures `briques()`, `planches()`,
    `chaume()`, `tuiles()`, `pierres()` (découpées à une forme), arbres
    `feuillage()`, `tronc()`, `arbre_branche()`, montagnes `pic()`, sols
    `terrain()`. Composer les paysages sur trois plans (lointain fondu dans
    le ciel, plan moyen, premier plan plus sombre). `sans_relief()` garde un
    dessin en aplats (éclairage physique, fausse découpe de la couleur du
    fond) ; `RELIEF = False` coupe le modelé automatique pour tout un livre ;
  - paysages et bâtiments réutilisables (`base.py`) : `paysage()` (ciel,
    lointain, collines à bosquets, sol à touffes en une ligne), `lointain()`,
    `bosquet()`, `touffe()`, `repoussoir()` (coin de feuillage au premier
    plan) ; `maison()` de trois quarts (`volets=`, `cote=False`),
    `immeuble()` (mansarde, pignon ou toit plat, balcons, boutique),
    `fenetre_facade()`, `volet()`, `chainage()`, `garde_corps()`,
    `store_banne()` ; poses dynamiques `court`, `saute`, `lance`,
    `designe`, `pousse`, `equilibre` (préférer `saute` pour un saut de
    joie, `court` pour une course) et `regard=(±1, 0)` pour un personnage
    vu de trois quarts qui regarde son voisin ;
  - `objets.py` : accessoires du quotidien ;
  - `fantastique.py` : humains (`personne`, `princesse`, `chevalier`, `roi`,
    `sorciere`), dragon, licorne, château, océan, fées ;
  - `contes.py`, `fables.py`, `sciences.py` : personnages et outils de leur
    rayon (`sciences.py` respecte la physique : l'utiliser plutôt que de
    refaire ombres, phases de Lune, arcs-en-ciel, champs, ondes) ;
  - `animaux.py` : décors et petites bêtes des documentaires animaliers
    (savane, banquise, mare, coupe du sol, plage, mouche, abeille, ver…),
    `loupe` et schéma en `cycle`.
- Ce qui ne sert qu'à ce livre se dessine dans son propre script. Ne modifier
  un module partagé que par **ajout** (nouvelle fonction ou nouveau paramètre
  avec valeur par défaut) pour ne changer aucun SVG existant.
- Garder le même personnage d'une page à l'autre (mêmes couleurs,
  accessoires) grâce à des `dict` de réglages comme `HEROS`.
- Cadrage : le personnage principal grand et lisible, les pieds au-dessus du
  bas de l'image, rien de coupé sur les côtés ; laisser de l'air en haut des
  images `pleine-page` (le texte s'y pose en bulle en bas) et ne pas mettre
  d'éléments importants tout en bas des couvertures (titre en haut).
- Le texte dans les dessins (bulles, étiquettes) reste rare, court et en
  français.
- Noms de fichiers : `couverture.svg`, `<nom>-seul.svg` pour la vignette, puis
  `01-…svg`, `02-…svg` en minuscules avec tirets.

Générer :

```sh
python3 outils/illustrer/generer.py mon-livre
```

## 4. Écrire `livres/<id>/livre.js`

```js
Bibliotheque.ajouter({
  id: "mon-livre",
  rayon: "histoires",
  titre: "Mon beau livre",
  sousTitre: "Une histoire de …",
  age: "3 à 6 ans",
  couleur: "#e8590c",
  resume:
    "Première phrase du résumé. " +
    "Deuxième phrase.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "…" },

    { type: "titre", image: "images/renard-seul.svg", texte: "Pour … (dédicace)." },

    {
      image: "images/01-au-reveil.svg",
      description: "Ce que montre exactement le dessin.",
      texte: "Le texte de la page.\n\n« Une réplique ! »",
    },
    // … une entrée par illustration, dans l'ordre de IMAGES

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/renard-seul.svg" },
  ],
});
```

Options utiles (voir le README) : `disposition: "pleine-page"` (avec
`positionTexte: "haut"` si besoin) ou `"image-bas"`, `fond`, `couleur`,
`numeros: false`. Pas de champ `auteur`/`illustrateur` sauf demande.
Toute image de `images/` doit être utilisée par une page.

## 5. Inscrire le livre

- Ajouter `"mon-livre"` dans `window.CATALOGUE` de `livres/catalogue.js`, à la
  fin du groupe de son rayon (l'ordre de la liste est l'ordre d'affichage).

## 6. Mettre à jour le cache et la documentation

- `sw.js` : augmenter `VERSION` d'un cran (`"v17"` → `"v18"`), une seule fois
  par lot de livres.
- Lancer `python3 outils/verifier-images.py` et reporter ses totaux
  (livres, pages, SVG) :
  - README, section « Dessiner les illustrations » (`N livres, M SVG`) ;
  - README, exemple de `VERSION` dans « Application installable » ;
  - `outils/REVUE-IMAGES.md` : totaux en tête et nouvelle section
    « Ajout du <date> » (livres ajoutés, contrôles faits, nouvelle `VERSION`),
    sur le modèle des sections précédentes.
- Si un nouveau rayon a été créé, le citer dans l'introduction du README.

## 7. Vérifier

```sh
python3 outils/illustrer/generer.py > /dev/null && git status --short -- livres
python3 outils/verifier-images.py      # doit finir par « 0 erreur(s). »
node --test
```

Après `generer.py` complet, seuls les fichiers du ou des nouveaux livres
doivent apparaître dans `git status -- livres`. Un SVG existant modifié
signale qu'un module partagé a changé : corriger avant de continuer.

## 8. Revoir les illustrations

Regarder **chaque** image avant de committer. Le script
[`planche.js`](planche.js) fabrique une planche contact (image, description
et texte de chaque page) :

```sh
NODE_PATH="$(npm root -g)" node .claude/skills/nouveau-livre/planche.js mon-livre /chemin/scratchpad/planche-mon-livre.html
```

Il écrit une page HTML et, si Playwright est disponible, une capture PNG à
côté (même nom, `.png`) que l'on peut ouvrir avec l'outil de lecture
d'images. Contrôler pour chaque page :

- le dessin correspond à la `description` et au texte (personnages présents,
  actions, objets, nombre, moment de la journée) ;
- rien n'est coupé, rien ne déborde, pas de chevauchement disgracieux ;
- personnages cohérents d'une page à l'autre ;
- exactitude scientifique pour le rayon Sciences.

Corriger les scripts, régénérer, revoir. Écrire la planche dans le
scratchpad, jamais dans le dépôt. Pour vérifier le rendu réel, on peut aussi
lancer `python3 -m http.server` et ouvrir `lire.html?livre=<id>` et
`imprimer.html?livre=<id>` (les textes longs ne doivent pas déborder).

## 9. Committer

Un commit par lot, message en français à l'infinitif, par exemple :

```
Ajouter « Mon beau livre » au rayon Petites histoires

Nouveau livre de 15 pages (illustrations générées par outils/illustrer).
Le cache hors ligne passe à v16 et les totaux de la documentation sont mis
à jour (133 livres, 2 201 pages, 1 897 SVG).
```

Le commit contient : `livres/<id>/` (livre.js et images), le script de
dessin, `livres/catalogue.js`, `sw.js`, `README.md` et
`outils/REVUE-IMAGES.md`.
