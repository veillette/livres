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
- Les images sont servies depuis le cache.
- **Après l'ajout d'un livre**, augmenter `VERSION` en haut de `sw.js`
  (`"v1"` → `"v2"`) pour que le nouveau livre soit aussi disponible hors ligne.

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
2. Y mettre les images dans `livres/mon-livre/images/`.
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

Autres options d'une page : `description` (texte alternatif de l'image),
`couleur`, `fond` (couleur de fond de la page). Un texte peut contenir plusieurs
paragraphes séparés par une ligne vide (`\n\n`). Mettre `numeros: false` sur le
livre pour masquer les numéros de page.

### Conseils pour les images

- Formats : SVG (net à toutes les tailles), PNG ou JPG.
- Les images sont recadrées pour remplir leur zone : garder l'essentiel au
  centre. Une image carrée convient bien pour `image-haut` / `image-bas` ; pour
  `pleine-page` et la couverture, prévoir un format portrait (environ 3 × 4).
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
livres/             un dossier par livre + catalogue.js
```

## Dessiner les illustrations

Les illustrations des livres récents sont générées en SVG par un petit outil
Python, sans aucune dépendance, dans `outils/illustrer/` :

- `base.py` : décors (ciel, collines, intérieurs, nuit…), personnages animaux
  vus de face avec leurs expressions (`sourire`, `rire`, `triste`, `fache`,
  `surpris`, `dort`…) et leurs poses (`salut`, `haut`, `porte`, `calin`…) ;
- `objets.py` : accessoires (gâteau, vélo, parapluie, bocal, cubes…) ;
- `histoires/<id>.py` : les pages d'un livre, une fonction par image.

```sh
python3 outils/illustrer/generer.py               # tous les livres
python3 outils/illustrer/generer.py ours-gateau   # un seul livre
```

Les images sont écrites dans `livres/<id>/images/`. Il reste à écrire le texte
dans `livres/<id>/livre.js`.
