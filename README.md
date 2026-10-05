# Livres pour enfants 📚

Un petit site pour créer des livres illustrés pour enfants, les **lire à l'écran**
et les **imprimer sur des feuilles** pour en faire de vrais livres.

- `index.html` : la bibliothèque (toutes les couvertures).
- `lire.html?livre=<id>` : feuilleter un livre (flèches du clavier, glisser du doigt,
  double page sur grand écran, lecture à voix haute).
- `imprimer.html?livre=<id>` : aperçu des feuilles et impression.

Le site est entièrement statique (HTML + CSS + JavaScript, sans dépendance ni
étape de compilation).

## Voir le site

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
  en haut de `sw.js` (par exemple `"v14"` → `"v15"`) pour que le nouveau livre et les
  nouvelles images soient aussi disponibles hors ligne. Les fichiers inchangés
  sont seulement revalidés, pas re-téléchargés.
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

4. Ajouter `"mon-livre"` dans `livres/catalogue.js`.
5. Augmenter `VERSION` dans `sw.js` pour la lecture hors ligne.
6. Lancer `python3 outils/verifier-images.py` (la publication échoue si cette
   vérification trouve une erreur). Si les images viennent du générateur,
   relancer aussi `generer.py` et valider les SVG produits.

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
livre pour masquer les numéros de page.

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
livres/             un dossier par livre + catalogue.js
outils/illustrer/   générateur des illustrations SVG (Python, non publié)
outils/verifier-images.py   vérification des livres et des images (non publiée)
outils/revue-images.html    revue interactive des illustrations
outils/REVUE-IMAGES.md      compte rendu de la revue, livre par livre
```

## Dessiner les illustrations

Les illustrations de tous les livres du catalogue (122 livres, 1 744 SVG) sont
générées par un petit outil Python, sans aucune dépendance, dans
`outils/illustrer/` :

- `base.py` : décors (ciel, collines, intérieurs, nuit…), personnages animaux
  vus de face avec leurs expressions (`sourire`, `rire`, `triste`, `fache`,
  `surpris`, `dort`…) et leurs poses (`salut`, `haut`, `porte`, `calin`…) ;
- `objets.py` : accessoires (gâteau, vélo, parapluie, bocal, cubes…) ;
- `fantastique.py` : personnages humains et créatures des contes ;
- `sciences.py` : personnages et schémas des livres de sciences (caneton,
  pingouin, nuage, graine, glaçon, enfants, astronaute), avec des outils qui
  respectent la physique : phases de la Lune, ombres portées selon la position
  du Soleil, arc-en-ciel à l'opposé du Soleil, lignes de champ d'un aimant,
  planètes éclairées du côté du Soleil, ondes sonores ;
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

```sh
python3 outils/illustrer/generer.py               # tous les livres
python3 outils/illustrer/generer.py ours-gateau   # un seul livre
```

Les images sont écrites dans `livres/<id>/images/`. Il reste à écrire le texte
dans `livres/<id>/livre.js`.

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
(`id`, `titre`, au moins une page), types et dispositions de page inconnus,
images manquantes ou en chemin absolu, SVG mal formés, dimensions invalides et
références internes absentes.

Avant chaque publication, GitHub Actions lance cette vérification, puis
`generer.py` : si les images produites diffèrent de celles du dépôt, la
publication s'arrête. Le site est publié sans `outils/illustrer/` ni les
scripts Python ; la revue des images (`outils/revue-images.html`) reste en ligne.
