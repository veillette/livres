# Livres pour enfants 📚

Un petit site pour créer des livres illustrés pour enfants, les **lire à l'écran**
et les **imprimer sur des feuilles** pour en faire de vrais livres.

- `index.html` : la bibliothèque, rangée par rayons (Sciences, Les animaux, Petites histoires,
  Les métiers, Fêtes, Comptines, Princesses, fées et dragons, Fables, Contes traditionnels). Les boutons du haut
  n'affichent qu'un rayon ; `index.html#fables` ouvre directement le rayon des
  fables, et le lien « Bibliothèque » du lecteur ramène au rayon du livre.
- `lire.html?livre=<id>` : feuilleter un livre (flèches, Espace, Page
  précédente / suivante, Début / Fin, glisser du doigt ; double page dès
  900 px de large, si l'écran est nettement plus large que haut ; lecture à
  voix haute « 🔊 Écouter »).
- `imprimer.html?livre=<id>` : aperçu des feuilles et impression.

Le site est entièrement statique (HTML + CSS + JavaScript, sans dépendance ni
étape de compilation).

## Voir le site

Les illustrations ne sont pas dans le dépôt : elles se dessinent à partir des
scripts Python (une trentaine de secondes, Python 3 suffit). Après un
`git clone`, et après chaque `git pull` qui touche aux illustrations, lancer
d'abord :

```sh
python3 outils/illustrer/generer.py
```

- **Sur l'ordinateur** : ouvrir `index.html` dans le navigateur, tout simplement.
- **Avec un petit serveur** (recommandé) : `python3 -m http.server`, puis
  <http://localhost:8000>.
- **En ligne** : le fichier `.github/workflows/pages.yml` publie le site sur
  GitHub Pages à chaque poussée sur `main`. Il faut l'activer une fois dans
  *Settings → Pages → Build and deployment → Source : GitHub Actions*.
  `main` doit aussi être la branche par défaut (*Settings → General → Default
  branch*) et être autorisée dans *Settings → Environments → github-pages →
  Deployment branches and tags* ; sinon la publication échoue avec
  « Branch "main" is not allowed to deploy to github-pages due to environment
  protection rules ».

## Application installable (PWA)

Une fois le site en ligne (https), on peut l'**installer** comme une application
sur tablette, téléphone ou ordinateur : bouton « 📲 Installer l'application » dans
la bibliothèque (Chrome, Edge, Android), ou *Partager → Sur l'écran d'accueil*
sur iPhone / iPad.

Au premier chargement, le service worker (`sw.js`) enregistre l'interface
**et tous les livres du catalogue** avec leurs images. Tout fonctionne ensuite
**hors ligne**, impression comprise, ce qui est pratique en voiture ou en vacances.

- Les pages et les textes sont d'abord demandés au réseau : les modifications
  apparaissent dès qu'on est connecté.
- Les images et les polices sont servies depuis le cache, sans requête réseau.
- **Après l'ajout d'un livre ou la modification d'images**, augmenter `VERSION`
  en haut de `sw.js` (aujourd'hui `"v30"`, donc `"v30"` → `"v31"`) pour que le
  nouveau livre et les nouvelles images soient aussi disponibles hors ligne.
  Les fichiers inchangés sont seulement revalidés, pas re-téléchargés.
- Sur `localhost`, tout est demandé au réseau d'abord : les images régénérées
  s'affichent tout de suite.

Le service worker ne fonctionne qu'à travers un serveur (`http://localhost`
ou le site en ligne), pas en ouvrant `index.html` directement depuis le disque.

## Imprimer un livre

Deux mises en page sont proposées sur la page d'impression :

| Mise en page | Feuille | Résultat |
| --- | --- | --- |
| **Livret à plier** | à l'italienne, 2 pages par face, recto verso | on empile, on plie en deux, on agrafe au milieu |
| **Une page par feuille** | à la française, 1 page par feuille | à relier (spirale, attaches, classeur) |

Papier Lettre (8½ × 11) ou A4. Pour le livret, les pages sont réordonnées
automatiquement (imposition) et des pages blanches sont ajoutées avant la
quatrième de couverture si le nombre de pages n'est pas un multiple de 4.
On peut aussi choisir les faces à imprimer (recto verso, rectos seuls ou versos
seuls) et une marge blanche autour des pages (aucune, 5 mm par défaut ou 10 mm).

Dans la fenêtre d'impression du navigateur :

1. échelle **100 %**, marges **Aucune** ;
2. cocher **Graphiques d'arrière-plan** (sinon les couleurs de fond disparaissent) ;
3. pour le livret : **recto verso, retournement sur le bord court**.

Sans imprimante recto verso : imprimer d'abord les « Rectos », remettre la pile
dans le bac, puis imprimer les « Versos » (faire un essai avec une feuille pour
trouver le bon sens).

## Ajouter un livre

1. Créer un dossier `livres/mon-livre/` (lettres minuscules, chiffres et tirets).
2. Y mettre les images dans `livres/mon-livre/images/`, ou les dessiner avec
   `outils/illustrer/histoires/mon_livre.py` (voir
   [Dessiner les illustrations](#dessiner-les-illustrations)).
3. Créer `livres/mon-livre/livre.js` :

   ```js
   Bibliotheque.ajouter({
     id: "mon-livre",                 // identique au nom du dossier
     rayon: "histoires",              // un des rayons de livres/catalogue.js
     titre: "Mon beau livre",
     sousTitre: "Facultatif",
     auteur: "Prénom Nom",
     illustrateur: "Prénom Nom",
     age: "3 à 6 ans",
     couleur: "#e8590c",              // couleur du livre (couverture, dos, titres)
     resume: "Texte de la quatrième de couverture.",
     pages: [
       { type: "couverture", image: "images/couverture.jpg" },
       { type: "titre", image: "images/petit-dessin.png", texte: "Pour Léa." },
       { image: "images/p1.jpg", texte: "Il était une fois…" },
       { image: "images/p2.jpg", disposition: "pleine-page", texte: "Texte dans une bulle." },
       { type: "texte", texte: "Fin" },
       { type: "quatrieme" },
     ],
   });
   ```

4. Ajouter `"mon-livre"` dans `livres/catalogue.js` (l'ordre de cette liste
   est l'ordre d'affichage dans chaque rayon). Les rayons possibles sont listés
   dans `RAYONS`, au bas du même fichier : on peut en ajouter un (identifiant,
   nom, icône, description).
5. Augmenter `VERSION` dans `sw.js` pour la lecture hors ligne.
6. Lancer `python3 outils/verifier-images.py` (la publication échoue si cette
   vérification trouve une erreur). Si les images viennent du générateur,
   relancer aussi `generer.py` et valider le script de dessin avec
   `outils/illustrer/empreintes.txt` (les SVG, eux, ne sont pas suivis par
   git). Des images faites à la main (PNG, JPG ou SVG) se valident avec le
   livre ; un SVG fait à la main s'ajoute avec `git add -f`, car
   `.gitignore` écarte les SVG de `livres/*/images/`.

### Types de pages

| `type` | Contenu |
| --- | --- |
| `couverture` | image plein cadre + titre, sous-titre et auteur |
| `titre` | page de titre : titre, petite image, crédits, dédicace (`texte`) |
| `illustration` *(par défaut)* | une image et un texte |
| `texte` | texte seul, centré, en grand (ex. « Fin ») ; `image` facultative |
| `quatrieme` | dos du livre : `texte` (ou `resume` du livre), image, âge |
| `vide` | page blanche |

Pour les pages `illustration`, `disposition` peut valoir :

- `image-haut` *(par défaut)* : image en haut, texte en dessous ;
- `image-bas` : texte en haut, image en dessous ;
- `pleine-page` : image sur toute la page, texte dans une bulle en bas
  (ou en haut avec `positionTexte: "haut"`).

Autres options d'une page : `description` (texte alternatif de l'image, aussi
affiché dans la revue des images), `couleur`, `fond` (couleur de fond de la
page) et, sur la couverture, `titre` pour remplacer le titre du livre. Un texte peut contenir plusieurs
paragraphes séparés par une ligne vide (`\n\n`). Mettre `numeros: false` sur le
livre pour masquer les numéros de page, et `langue` (par défaut `"fr-FR"`) pour
choisir la langue de la lecture à voix haute.

### Conseils pour les images

- Formats : SVG (net à toutes les tailles), PNG ou JPG.
- Les images sont affichées en entier, sans couper les personnages. Une image
  carrée convient pour `image-haut` / `image-bas`. Sur une couverture, elle est
  alignée en bas ; sur une `pleine-page`, en haut pour laisser de la place au texte.
  Un format portrait convient aussi à ces deux types de pages.
- Pour l'impression, viser au moins 1500 px de haut pour une image pleine page.

## Organisation du code

```
index.html, lire.html, imprimer.html
css/site.css        interface du site + règles d'impression
css/pages.css       apparence des pages (en unités cqw/cqh : même rendu écran/papier)
js/livres.js        chargement des livres et rendu d'une page
js/bibliotheque.js  page d'accueil
js/lecteur.js       lecteur
js/imposition.js    ordre des pages pour le livret
js/impression.js    page d'impression
js/pwa.js           enregistrement du service worker, bouton « Installer »
sw.js               service worker (cache hors ligne)
manifest.webmanifest, icones/   description de l'application et icônes
polices/            polices Andika et Fredoka (licence OFL), hébergées avec le site
livres/             un dossier par livre + catalogue.js (liste et rayons)
outils/illustrer/   générateur des illustrations SVG (Python, non publié)
outils/illustrer/empreintes.txt   empreinte de chaque SVG généré (suivie par git)
outils/verifier-images.py   vérification des livres et des images (non publiée)
outils/imposition.test.js   tests de l'ordre des pages du livret (non publiés)
outils/revue-images.html    revue interactive des illustrations
outils/REVUE-IMAGES.md      compte rendu de la revue, livre par livre
AGENTS.md           consignes pour les agents de code (non publiées)
.claude/skills/     compétences nouveau-livre, direction-artistique, retoucher-livre (non publiées)
.claude/hooks/      dessin des SVG au démarrage d'une session Claude Code dans le cloud
```

## Dessiner les illustrations

Les illustrations de tous les livres du catalogue (240 livres, 3 780 pages,
3 257 SVG) sont
générées par un petit outil Python, sans aucune dépendance, dans
`outils/illustrer/` :

- `base.py` : décors (ciel, collines, intérieurs, nuit…), personnages animaux
  vus de face avec leurs expressions (`sourire`, `rire`, `triste`, `fache`,
  `surpris`, `dort`…) et leurs poses (`salut`, `haut`, `porte`, `calin`,
  `danse`, `applaudit`, `victoire`, `coucou`, `chut`, `etire`, `epaules`,
  `marche`, et les poses dynamiques `court`, `saute`, `lance`, `designe`,
  `pousse`, `equilibre`…). Les personnages (animaux de `perso()` et humains de
  `personne()`) reçoivent automatiquement un liseré, un modelé (ombre et
  reflet), des mains avec un pouce, des doigts de pied, une petite ombre au
  sol et une tête légèrement penchée selon l'expression ; les paramètres
  `pas=` (`"marche"`, `"pointe"`, `"saute"`), `penche=` (degrés) et `ombre=`
  permettent de les régler. Un livre qui dessine de vraies ombres portées
  coupe l'ombre douce avec `OMBRES_DOUCES = False` dans son script ;
  l'ombre douce s'allonge du côté opposé à la lumière (en haut à gauche),
  sauf dans les livres de sciences où elle reste centrée (`SENS_OMBRE` dans
  un script pour choisir : 1 vers la droite, 0 centrée) ;
  les corps et les têtes sont remplis de dégradés en relief, le visage glisse
  en vue de trois quarts quand `regard=` part de côté, et le corps se penche
  pour courir, marcher, danser ou tirer (`INCLINE`) ;
- relief des décors : `lineaire()`, `radial()`, `volume()` et `cylindre()`
  fabriquent des dégradés partagés (identifiant tiré de la définition, ajoutés
  aux `<defs>` de la page qui les emploie). Ciel avec brume d'horizon, sol plus
  sombre et texturé au premier plan, collines précédées d'une chaîne lointaine
  à demi fondue dans le ciel (trois plans), arbres, sapins, maisons (tuiles,
  bardage, linteaux, appuis, ombre sous le toit), châteaux (pierres, tuiles),
  montagnes (`pic()`, versant à l'ombre), intérieurs (parquet en perspective,
  pénombre des coins), fenêtres, portes et meubles en relief ;
- modelé automatique : à l'écriture de la page, chaque aplat des dessins
  propres aux livres reçoit un léger dégradé (lumière en haut à gauche), sauf
  les formes semi-transparentes, les masques et découpes, les formes de la
  couleur du fond et les groupes `sans_relief()` (astres éclairés des livres
  de sciences) ; `RELIEF = False` dans un script le coupe. Textures
  partagées pour les bâtiments et les arbres des livres : `briques()`,
  `planches()`, `chaume()`, `tuiles()`, `pierres()`, `ombre_avancee()`,
  `feuillage()`, `tronc()`, `arbre_branche()` ; le modelé des personnages et
  des animaux (`ombrage()`) met des ombres froides à bord fondu et une
  lumière réfléchie au bord ;
- finition de la page (`Scene.svg()`) : chaque page reçoit la lumière de son
  moment (`AMBIANCES` : jour, soir, nuit, intérieur, sous l'eau…), déduit du
  décor (`ciel()`, `nuit()`, `interieur()`, `ocean()`…) ou imposé par
  `S.ambiance()` : teinte bleutée la nuit ou dorée le soir, posée sous les
  halos des sources de lumière (`S.lumiere()` ; la lune, les maisons
  éclairées, les lampes, les lucioles et les étoiles qui parlent posent le
  leur), halo en lumière douce et vignettage ; patine de vieux papier très
  pâle sur les fables et les contes (`GLACIS` dans un script pour la
  changer). Les livres de sciences n'ont ni teinte ni halo. Le grain du
  papier est posé par `css/pages.css` sur chaque page du site ;
- cadrage : `S.camera(zoom, cx, cy)` fait un gros plan sans bord vide,
  `S.dessus()` pose bulles et onomatopées hors zoom, `S.vers_page()` vise un
  point de la scène ;
- petite bête cachée : une coccinelle se cache sur chaque page pleine, posée
  sur une cachette libre proposée par le décor (`sol`, `interieur`, `piece`,
  `ocean`, `sous_l_eau`, `coupe_terre`, ou un sol tracé à la main), en vol là
  où il n'y a pas de sol ; une étoile de mer sur le sable de la mer et un
  petit poisson en pleine eau la remplacent. Elle ne se pose jamais sur un
  personnage, une bulle ou un texte : ceux-ci ajoutent à leur dessin un
  repère invisible `occuper()`, lu à travers les `place()` et les cadrages.
  `S.cachette(x, y[, "air" | "eau" | "poisson"])` impose la place,
  `S.cachette(None)` met une page hors du jeu (une page dans l'espace),
  `CACHE = None` dans un script retire la bête d'un livre (*Sacha chez
  les planètes*). Elle n'apparaît que dans les livres où elle est sur toutes les
  pages : `generer.py` signale les pages qui manquent ;
  `.claude/skills/retoucher-livre/cachettes.py` leur propose une place
  d'après l'image rendue et, avec `--verifier`, déplace les bêtes posées sur
  du rouge, dans l'eau ou sur un personnage ; `planche_cachettes.py` en fait
  une planche de revue ;
- intérieurs au caractère marqué : `piece(S, style)` (`chaumiere`, `manoir`,
  `chateau`, `chambre`, `cuisine`) ; le papier peint d'`interieur(papier=…)`
  change d'un livre à l'autre (`rayures`, `pois`, `fleurs`, `losanges`,
  `etoiles` ; `PAPIER_PEINT` dans un script pour le choisir), `motif_mural()` ;
- paysages en trois plans réutilisables : `paysage()` compose une scène
  complète (ciel, montagnes ou collines lointaines, collines et bosquets,
  sol) ; `lointain()` (chaîne bleuie et voilée), `bosquet()` (arbres du plan
  moyen), `touffe()` et `premier_plan_sol()` (touffes, cailloux ou congères
  plus grands près du bas ; `sol(…, premier=False)` les retire),
  `repoussoir()` (feuillage sombre dans un coin du premier plan) ;
- architecture réutilisable : `maison()` vue de trois quarts (mur latéral et
  pan de toit qui fuient selon `FUITE`, chaînage d'angle, gouttière, volets
  avec `volets=`, `cote=False` pour une façade seule), `immeuble()` (toit en
  mansarde, à pignon ou plat, corniche et bandeaux ombrés, balcons, volets,
  boutique à store) et leurs pièces : `fenetre_facade()`, `volet()`,
  `chainage()`, `cote_batiment()`, `garde_corps()`, `store_banne()` ; la rue
  de `ville()` (`fables.py`) en est faite ;
- `objets.py` : accessoires (gâteau, vélo, parapluie, bocal, cubes…) ;
- `fantastique.py` : personnages humains et créatures des contes ;
  `personne()` règle l'âge (`stature=` : `petit`, `enfant`, `ado`, `adulte`,
  `ancien`), la silhouette (`carrure=`), le visage (`nez=`, `yeux=`,
  `taches=`, `rides=`) et la coiffure (`longs`, `tresses`, `chignon`,
  `carre`, `afro`, `couettes`, `raie`…) ; `ancre()` et `mains_personne()`
  placent un objet dans la main d'un adulte ; poses d'échange `main`,
  `epaule`, `tend`, `mains_jointes`, `ramasse`, `leve_doigt` ;
- `sciences.py` : personnages et schémas des livres de sciences (caneton,
  pingouin, nuage, graine, glaçon, enfants, astronaute), avec des outils qui
  respectent la physique : phases de la Lune, ombres portées selon la position
  du Soleil, arc-en-ciel à l'opposé du Soleil, lignes de champ d'un aimant,
  planètes éclairées du côté du Soleil, ondes sonores ;
- `animaux.py` : décors et petites bêtes partagés par les documentaires du
  rayon « Les animaux » (savane, banquise, mare, coupe du sol, plage, montagnes,
  mouche, moustique, abeille, ver de terre, poisson, campagnol), loupe et schéma
  en cycle (œuf → têtard → grenouille…) ;
- `metiers.py` : tenues, coiffes et décors des livres du rayon « Les métiers »
  (blouse et stéthoscope, veste et casque de pompier, gilet et casque de
  chantier, uniforme et casquette de police, salopette, tablier, calot et
  masque de soin, sacoche de courrier, cabinet de soins, rue de ville…), posés
  sur les personnages de `personne()` par ses paramètres `tenue=` et `coiffe=` ;
- `fables.py` : personnages et accessoires des fables de La Fontaine (corbeau,
  coq et poule, colombe, cigogne et héron, moucheron, araignée, chêne et roseau
  qui parlent, pots de terre et de fer qui parlent, âne, cheval et cerf de
  profil, fromage, raisins, puits, filet, grelot, pot au lait, os, marrons,
  cheminée, pont-tronc…). Les animaux « debout » des fables (`loup`, `lion`,
  `lievre`, `rat`, `ane`, `chevre`, `boeuf`, `cigale`, `cerf`, `singe`) sont
  des espèces de `perso()` dans `base.py` ;
- `contes.py` : personnages et accessoires des contes traditionnels (Chaperon
  rouge, géant, troll, lutins, Chat botté, bonhomme de pain d'épice, cygne,
  maisons des trois petits cochons, tige de haricot, maison en pain d'épice,
  carrosse, pantoufle de verre, navet géant, légumes…) ;
- `histoires/<id>.py` (tirets remplacés par des soulignés, par ex.
  `histoires/ours_gateau.py`) : les pages d'un livre, une fonction par image,
  avec ses variables `ID` et `IMAGES`. Les personnages et schémas propres à un
  seul livre y sont aussi dessinés : circuit de Zoé, poulies de Castor,
  balançoire de Basile, thermomètres de Tilou…
- `dragons.py` : accessoires partagés par les histoires de dragons (dragon
  de `fantastique.py` habillé d'un chapeau, d'une couronne, de lunettes ou de
  moustaches, dragon couché qui dort, jets de feu, de fumée, de brouillard et
  de givre, petite flamme, tas d'or, coffre, nid de paille, grotte à porte
  ronde, lanterne de papier…) ;
- `fetes.py` : accessoires partagés par les livres du rayon « Fêtes »
  (lanternes, guirlandes lumineuses et fanions, cadeaux, sapin décoré, étoile
  en papier, œufs peints et cloches de Pâques, citrouilles creusées, confettis,
  serpentins, feux d'artifice, cerf-volant, crêpes, petit chien de profil…) ;
  chaque fête a, comme les autres livres, son propre script dans `histoires/`.

```sh
python3 outils/illustrer/generer.py               # tous les livres
python3 outils/illustrer/generer.py ours-gateau   # un seul livre
```

Les images sont écrites dans `livres/<id>/images/`. Il reste à écrire le texte
dans `livres/<id>/livre.js`.

Les SVG ne sont **pas** suivis par git : la publication les redessine. À leur
place, `generer.py` réécrit `outils/illustrer/empreintes.txt`, une ligne par
image (empreinte SHA-256 abrégée, puis `<id>/<nom>`), que l'on valide avec le
script de dessin. Son diff montre exactement quelles images un changement a
modifiées :

```sh
python3 outils/illustrer/generer.py > /dev/null && git diff --stat -- outils/illustrer/empreintes.txt
git diff -- outils/illustrer/empreintes.txt   # les images changées, une par ligne
```

Une ligne changée dans un livre qu'on ne voulait pas toucher signale une
régression d'un module partagé. Pour voir les images elles-mêmes, la
planche avant/après de `retoucher-livre` redessine l'ancienne version à
partir des scripts d'un commit donné.

Les règles de composition (plans variés, gros plans, lumière, âges des
personnages, décors, échelles, petite bête) sont réunies dans la compétence
[`direction-artistique`](.claude/skills/direction-artistique/SKILL.md) ; la
compétence [`retoucher-livre`](.claude/skills/retoucher-livre/SKILL.md) décrit
comment reprendre les images d'un livre existant, avec une planche
avant/après (`.claude/skills/retoucher-livre/avant-apres.js`).

### Revoir les illustrations

Ouvrir [la revue des images](outils/revue-images.html) pour parcourir toutes les
illustrations du catalogue, filtrer par livre ou par type d’image, et comparer
les dessins originaux avec les pages mises en forme. Chaque dessin est accompagné
du texte de la page et de sa description.

La [revue détaillée](outils/REVUE-IMAGES.md) conserve les contrôles par livre et
une [comparaison avant/après](outils/revue-images-comparaison.png).

```sh
python3 outils/verifier-images.py
```

Elle demande Python 3 et Node.js (pour lire les fichiers `livre.js`).
Elle inclut aussi les livres hors catalogue : champs requis
(`id`, `titre`, au moins une page, `rayon` connu pour les livres du
catalogue), types et dispositions de page inconnus,
images manquantes ou en chemin absolu, images que plus aucune page n'utilise,
SVG mal formés, dimensions invalides et références internes absentes, SVG
générés périmés (différents de `empreintes.txt` : relancer `generer.py`).
Elle se lance donc après `generer.py`.
Elle signale aussi les oublis qui laisseraient une page vide ou bancale :
`couleur`, `age` ou `resume` absents, page `illustration` ou `texte` sans
texte, et quelques fautes de typographie (espaces répétées ou en trop, espace
avant une virgule ou un point, `...` au lieu de `…`, guillemets droits `"` au
lieu de « »). L'apostrophe droite `'` reste acceptée.

L'ordre des pages du livret à plier (`js/imposition.js`) est testé à part,
pour toutes les longueurs de livre de 1 à 40 pages :

```sh
node --test
```

Avant chaque publication, GitHub Actions dessine toutes les illustrations
avec `generer.py` : si leurs empreintes diffèrent de
`outils/illustrer/empreintes.txt`, la publication s'arrête. Puis elle lance
cette vérification et ces tests. Le site est publié sans `outils/illustrer/`,
les scripts Python ni les tests ; la revue des images
(`outils/revue-images.html`) reste en ligne.
