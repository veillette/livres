---
name: direction-artistique
description: Règles et outils de direction artistique des illustrations (cadrage et gros plans, lumière et moments de la journée, personnages d'âges et de silhouettes variés, intérieurs, échelles, petite bête cachée). À utiliser dès qu'on dessine, compose, reprend ou juge une illustration d'un livre du dépôt, nouveau ou existant, ou qu'on demande des images plus belles, plus vivantes ou plus variées.
---

# Direction artistique des illustrations

Ce qui rend une page de livre d'images agréable à regarder, et comment
l'obtenir avec le générateur `outils/illustrer/`. Lire d'abord
[AGENTS.md](../../../AGENTS.md). Pour un nouveau livre, cette compétence
complète l'étape 3 de [`nouveau-livre`](../nouveau-livre/SKILL.md) ; pour
reprendre un livre existant, voir [`retoucher-livre`](../retoucher-livre/SKILL.md).

## 1. Penser le livre comme une suite de plans

Un livre se feuillette : c'est le **rythme** entre les pages qui le rend
vivant. Avant de dessiner, écrire en commentaire du script, page par page, le
plan voulu :

| Plan | Quand | Comment |
| --- | --- | --- |
| Plan large | ouverture, nouveau lieu, foule, voyage | décor complet, personnages petits (`s` ≈ 0,8–1,1) |
| Plan moyen | dialogue, action ordinaire | personnages en pied (`s` ≈ 1,2–1,5) |
| Gros plan | émotion, surprise, détail qui compte, chute d'une répétition | `S.camera(1.6–2.4, cx, cy)` sur un visage, une main, un objet |
| Plongée / contre-plongée | se sentir petit, grand ou menacé | décor qui domine (château, arbre), personnage petit en bas ; ou personnage énorme, horizon bas |

Règles :

- **Jamais plus de deux pages de suite au même plan.**
- Les répétitions du texte (« Que vous avez de grandes oreilles… de grands
  yeux… ») se dessinent en **resserrant** le cadre à chaque page, puis la
  chute en plan large.
- **Pas de page presque vide** : si le sujet est petit (une chrysalide, un
  insecte, un objet), soit gros plan, soit décor qui l'entoure (jardin flou à
  l'arrière, feuillage net devant).
- Composer en diagonale quand il y a du mouvement (un oiseau qui plonge, une
  course) ; poser le sujet sur un tiers de l'image plutôt qu'au centre exact
  quand la page n'est pas un portrait.
- Un **repoussoir** au premier plan (`repoussoir()`, herbes hautes, branche,
  chambranle) creuse la profondeur et cadre la scène.

### Outils de cadrage (`base.py`)

```python
S = Scene()
decor(S)
S.add(perso("loup", 440, 718, 1.1, ...))
S.camera(1.9, 400, 560)                  # zoom ×1,9 centré sur (400, 560) de la scène
S.dessus(bulle(560, 150, 420, 100, "C'est pour mieux\nte voir !", 32,
               pointe=S.vers_page(440, 590)))   # bulle hors zoom, qui vise la bouche
```

- `S.camera()` garde le cadre dans la scène (aucun bord vide) ; le décor
  doit donc couvrir toute la page.
- `S.dessus()` : bulles, onomatopées, titres restent à leur taille ;
  `S.vers_page(x, y)` convertit un point de la scène en point de la page.
- Mettre à jour la `description` de la page dans `livre.js` (« Gros plan sur… »).

## 2. Lumière et moment de la journée

`Scene.svg()` pose sur chaque page une **finition** selon son moment
(`AMBIANCES` dans `base.py`) :

| Moment | Déduit de | Effet |
| --- | --- | --- |
| `jour` | `ciel()` clair | léger vignettage |
| `soir` | `ciel()` à teinte chaude franche (orange, rose soutenu) | teinte dorée, halo chaud, vignettage violet |
| `nuit` | `nuit()`, `ciel()` sombre | teinte bleutée, halo froid, vignettage marqué |
| `interieur` | `interieur()`, `piece()` | halo chaud, vignettage brun |
| `eau` | `ocean()` | halo clair venu d'en haut, vignettage bleu |
| `neutre`, `sombre` | `fond()` clair ou sombre | vignettage seul (schémas, salle noire) |

- Le dernier décor posé l'emporte ; `S.ambiance("nuit")` impose le moment
  (une chambre la nuit, une cuisine au coin du feu…).
- **La nuit, toute source de lumière a son halo**, dessiné au-dessus de la
  teinte : `S.lumiere(x, y, r, couleur, force, ry=None)` (coordonnées de la
  scène ; `ry` aplatit le halo en flaque de lumière au sol). La lune,
  `maison(lumiere=True)`, `lampe()`, `luciole()` et `etoile_perso()` posent
  le leur d'eux-mêmes (`halo=False` pour l'éviter quand ils sont dessinés
  dans un repère local, sinon le halo serait mal placé).
- Une vitrine éclairée la nuit : vitre jaune, `S.lumiere()` sur la vitre et
  une flaque `S.lumiere(x, y_sol, 200, ry=60)` sur le trottoir.
- Livres de sciences : ni teinte ni halo (`generer.py`) ; l'éclairage reste
  physique (`sciences.py`).
- Le grain du papier est posé par `css/pages.css` sur chaque page du site,
  pas dans les SVG.

## 3. Personnages

`personne()` (`fantastique.py`) dessine des humains de tous âges :

| Rôle | Réglages conseillés |
| --- | --- |
| tout-petit | `stature="petit"` |
| enfant (héros) | `stature="enfant"` (par défaut) |
| grand frère, jeune fille, demi-sœurs | `stature="ado"` |
| parent, roi, prince, artisan | `stature="adulte"` |
| grand-parent, marraine, vieux sage | `stature="ancien"` (rides, dos un peu voûté) |

- Distinguer les personnages d'un même livre par la **silhouette** autant que
  par la couleur : `carrure="fine" | "normale" | "ronde"`, `nez="petit" |
  "rond" | "pointu" | "long" | "retrousse"`, `yeux="ronds" | "petits" |
  "cils"`, `taches=True` (taches de rousseur), coiffures `carre`, `afro`,
  `couettes`, `raie`, `boucles`, `chignon`, `tresses`…
- Garder chaque personnage identique d'une page à l'autre avec un `dict`
  (`MAMAN = dict(stature="adulte", ...)`).
- Objets tenus : ils sont placés pour la main d'un enfant ; pour une autre
  stature, `objet=hache(*ancre(68, -146, "tient", "adulte", "ronde"), 0.9)`
  ou `mains_personne(0, 0, 1, "donne", stature="adulte")`.
- Les personnages **se regardent** (`regard=(±1, 0)`) et **agissent
  ensemble** : poses `main` (se donner la main, l'un des deux `flip=True`),
  `epaule`, `tend`, `mains_jointes`, `ramasse`, `leve_doigt`, en plus de
  `donne`, `calin`, `ouverts`…
- Taille relative : à même échelle `s`, un adulte dépasse un enfant d'environ
  un quart ; ne pas « corriger » en agrandissant l'enfant.

## 4. Décors

- Intérieurs : `piece(S, style, y)` donne une pièce au caractère marqué —
  `chaumiere` (murs chaulés, poutres, larges planches), `manoir` (boiseries,
  papier peint damassé), `chateau` (pierre, tentures), `chambre` (papier peint
  étoilé), `cuisine` (carrelage). `interieur(S, mur, plancher, y,
  papier=couleur)` prend le motif de papier peint du livre (`PAPIER_PEINT`
  dans le script pour l'imposer : `rayures`, `pois`, `fleurs`, `losanges`,
  `etoiles`) ; `motif_mural()` pour un mur à part.
- Extérieurs en trois plans : `paysage()`, ou `ciel` + `collines` + `sol` +
  `repoussoir`.
- **Échelles** : un château domine les personnages (château `s` ≈ 0,85–1,1
  pour un personnage `s` ≈ 0,8–1) ; vérifier les tailles réelles en
  documentaire (une abeille fait 2,5 à 3 alvéoles de long).

## 5. Couleurs et papier

- Fables et contes reçoivent une patine de vieux papier très pâle
  (`GLACIS_RAYON` dans `generer.py`, `GLACIS = "#…"` ou `None` dans un
  script). Un glacis désature les couleurs complémentaires : le garder
  presque blanc.
- Une palette par livre : trois ou quatre couleurs dominantes, reprises par
  les personnages et le décor ; éviter de tout saturer.

## 6. La petite bête cachée

Une coccinelle se cache sur chaque page pleine : les petits la cherchent.
Selon la page, elle est posée (sol, plancher, mur, branche, herbe d'une
coupe du sol), en vol (`"air"` : ciel, mur, schéma), une étoile de mer sur
le sable de la mer (`"eau"`) ou un petit poisson en pleine eau
(`"poisson"`, et d'office sous l'eau : au fond d'une mare, le « sol »
devient un poisson qui nage juste au-dessus).

- Les décors qui reçoivent la Scene (`sol`, `interieur`, `piece`, `ocean`,
  `sous_l_eau`, `coupe_terre`) proposent des cachettes au pied des côtés ;
  à défaut, un sol tracé à la main (aplat ou chemin qui couvre toute la
  largeur jusqu'en bas, hors eau bleue claire ou sombre) en sert. La bête
  prend la cachette libre la plus proche d'un bord, puis, si tout le bord
  est pris, une place plus bas, devant les pieds.
- **Jamais sur un personnage, une bulle ou un texte** : `perso` (selon
  l'espèce et la pose), `personne`, `oiseau`, `chouette`, `escargot`,
  `tortue`, `dragon`, `licorne`, `corbeau`, `coq`, `cigogne`, cheval, âne et
  cerf de profil, `pot_parlant`, `bonhomme_pain_epice`, `cygne`, `crabe`,
  `poulpe`, `pingouin`, `glacon`, `chaudron`, `bulle`, `pensee` et `texte`
  ajoutent à leur dessin un repère invisible `occuper(x0, y0, x1, y1)`, lu
  à travers les `place()` et les cadrages. **Un personnage dessiné à la
  main dans un script doit faire de même**, dans son repère local (mesurer
  son étendue plutôt que la deviner) : `return place(m + [occuper(-90,
  -200, 90, 0)], x, y, s, flip=flip)`.
- Jamais **invisible ni absurde** : pas sur du rouge (camion de pompier,
  tambour, feu), pas posée dans l'eau, pas en vol dans la terre ni dans
  l'espace. `retoucher-livre/cachettes.py --verifier` repère les trois
  premiers cas sur l'image rendue ; les autres se voient sur la planche.
- C'est **tout ou rien** : s'il manque une page, `generer.py` retire la bête
  du livre et écrit `petite bête absente : pas de cachette sur …`. Compléter
  avec `S.cachette(x, y)` (pieds de la bête, coordonnées de la scène),
  `S.cachette(x, y, "air")` (centre, en vol), `"eau"` ou `"poisson"` ;
  l'outil `retoucher-livre/cachettes.py` propose ces places d'après l'image.
- Une page où une coccinelle n'a rien à faire (dans l'espace) se met hors du
  jeu avec `S.cachette(None)` et un commentaire ; `CACHE = None` retire la
  bête d'un livre entier (*Sacha chez les planètes*, tout dans l'espace) ;
  `CACHE = "souris"` change d'animal.

## 7. Vérifier

Après génération (`python3 outils/illustrer/generer.py <id>`), regarder
**chaque** image en planche (`nouveau-livre/planche.js`, ou
`retoucher-livre/avant-apres.js` pour comparer) et contrôler :

- [ ] le plan change au moins toutes les deux pages ; un gros plan au moment fort ;
- [ ] aucune page presque vide ; rien d'important coupé par le cadre ;
- [ ] âges et silhouettes lisibles, personnages identiques d'une page à l'autre ;
- [ ] échelles cohérentes ;
- [ ] la nuit, les lumières brillent ; le moment de chaque page est le bon ;
- [ ] la petite bête est sur toutes les pages (sortie de `generer.py`), visible,
      plausible et jamais sur un personnage (planche
      `retoucher-livre/planche_cachettes.py`) ;
- [ ] les `description` de `livre.js` disent ce que montre le dessin.
