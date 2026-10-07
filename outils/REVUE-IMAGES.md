# Revue systématique des illustrations

Revue du 29 septembre 2026 : **86 livres, 1 426 pages et 1 234 illustrations SVG**.
Catalogue actuel, après les ajouts d'octobre : **185 livres, 2 900 pages et
2 492 illustrations SVG** (cache hors ligne `v23`).

[Voir des exemples avant/après](revue-images-comparaison.png) ou ouvrir
[la revue interactive](revue-images.html).

Les couvertures et toutes les illustrations ont été parcourues en planches, avec une vérification des silhouettes, des accessoires, des expressions et de la continuité des scènes. Les légendes SVG et les vignettes ont aussi été mesurées dans Chromium. Le tableau ci-dessous conserve le détail de la revue par livre.

## Corrections communes

- Les images sont affichées en entier : les personnages placés sur les côtés et les pieds près du bas restent visibles.
- Le cadre illustré peut se réduire lorsque le texte prend davantage de place. La taille des caractères est conservée.
- Les couvertures alignent le dessin en bas ; les images pleine page sont alignées en haut, pour libérer la place du texte.
- Les échelles et opacités SVG conservent trois décimales. Les détails à petite échelle, les reflets et les dégradés ne sont plus arrondis au dixième.
- Treize vignettes et six légendes coupées ont été corrigées dans leurs sources Python. Le bateau, le reflet du cygne et les invités à la fenêtre ont aussi été ajustés.
- Les SVG ont été régénérés ; le cache hors ligne passe à `v10`.

## Vérifications

- `python3 outils/verifier-images.py` : 86 livres, 1 234 images référencées, 1 234 SVG valides, aucune image manquante et aucune référence SVG interne absente.
- Régénération en mémoire des 1 234 SVG : résultat identique aux fichiers enregistrés.
- Mesure des textes SVG et des silhouettes des 86 vignettes : aucun débordement résiduel détecté.
- Contrôle des pages dans Chromium : téléphone, écran, livret A4, livret Lettre, page A4 et page Lettre. **8 556 pages contrôlées, aucun débordement de texte détecté.** Les filtres de la revue interactive, trois livres dans le lecteur et deux exports PDF ont aussi été vérifiés.
- Première passe sur 84 livres : 1 120 zones d’image recadrées et 265 blocs de texte dépassant la page. Après correction, aucun de ces défauts détecté sur les 86 livres.
- Les polices distantes étaient désactivées pendant les contrôles : le rendu testé utilise les polices locales de secours. Aucun tirage papier physique effectué.

## Ajout du 3 octobre 2026

Douze nouvelles fables de La Fontaine (98 livres au catalogue, 1 424 SVG) :
planches de toutes leurs illustrations revues dans Chromium, textes mesurés
dans la page d'impression (le cadre illustré garde ses 63 % sur toutes les
pages), `verifier-images.py` sans erreur et régénération complète identique.
Le cache hors ligne passe à `v12`.

## Ajout du 4 octobre 2026

Douze nouveaux livres (110 livres au catalogue) : trois livres de sciences
(électricité, chaleur, pendule), trois petites histoires, deux comptines, deux
fables de La Fontaine et deux contes. Planches de toutes leurs illustrations
revues dans Chromium, textes mesurés dans la page d'impression en Lettre et en
A4 (le cadre illustré garde ses 63 % en Lettre et au moins 61,7 % en A4),
`verifier-images.py` sans erreur et régénération complète identique. Le cache
hors ligne passe à `v13`.

## Ajout du 4 octobre 2026 (deuxième lot)

Douze nouveaux livres (122 livres au catalogue) : trois livres de sciences
(machines simples, rebonds et élasticité, dissolution), trois petites
histoires, deux comptines, deux fables de La Fontaine et deux contes de
Grimm. Planches de toutes leurs illustrations revues dans Chromium, textes
mesurés dans la page d'impression en Lettre et en A4 (le cadre illustré garde
au moins 59,7 % en Lettre et 62,6 % en A4, comme les livres existants ; aucun
débordement), `verifier-images.py` sans erreur et régénération complète
identique (122 livres, 2 026 pages, 1 744 SVG). Le cache hors ligne passe à
`v14`.

## Ajout du 5 octobre 2026

Dix nouveaux livres au rayon « Princesses, fées et dragons » (132 livres au
catalogue) : Capucine, princesse chevalier ; Ondine et la tempête ; Mila, la
petite fée des dents ; Nina, la princesse pirate ; Coralie et l'océan tout
propre ; Flocon, la fée de l'hiver ; La princesse qui ne voulait pas dormir ;
Aya et le nuage de pluie ; Inès et les trois souhaits ; Ada, la princesse
inventrice. Planches de toutes leurs illustrations revues dans Chromium,
textes mesurés dans la page d'impression en Lettre et en A4 (aucun
débordement), `verifier-images.py` sans erreur et régénération complète
identique pour les livres existants (132 livres, 2 186 pages, 1 884 SVG). Le
cache hors ligne passe à `v15`.

## Ajout du 6 octobre 2026

Vingt documentaires dans un nouveau rayon « Les animaux », réunis aux dix
livres de fêtes déjà sur `main` (162 livres au catalogue) : Du têtard à la
grenouille ; La chenille qui devient papillon ;
Bzzz ! La ruche des abeilles ; Papa manchot et son œuf ; L'écureuil et ses
cachettes ; La marmotte dort tout l'hiver ; La baleine qui chante ; La
chauve-souris voit avec ses oreilles ; La chouette qui vole sans bruit ; Le
poussin dans l'œuf ; La famille éléphant ; Les bébés tortues de mer ; Le petit
kangourou dans la poche ; La girafe au long cou ; Le ver de terre jardinier ;
L'araignée tisse sa toile ; Le caméléon change de couleur ; Le poulpe aux huit
bras ; L'hirondelle part en voyage ; L'ours blanc sur la banquise. Les décors et
petites bêtes communs sont dans le nouveau module `outils/illustrer/animaux.py`.
Planches de toutes leurs illustrations revues dans Chromium (cadrage, nombre de
pattes, étapes des cycles, cohérence des personnages d'une page à l'autre,
exactitude des comportements décrits), textes mesurés dans la page
d'impression en Lettre et en A4, livret et page par feuille : aucun
débordement, le cadre illustré garde au moins 56,3 % de la page.
`verifier-images.py` sans erreur et régénération complète identique pour les
livres existants (162 livres, 2 570 pages, 2 208 SVG). Le cache hors ligne
passe à `v17`.

## Ajout du 7 octobre 2026

Dix livres dans un nouveau rayon « Les métiers » (172 livres au catalogue) :
Lou chez le docteur ; Les dents de Timéo (la dentiste) ; Une journée chez les
pompiers ; Le boulanger de la nuit ; La tournée de Rosa (la factrice) ; Biscuit
chez la vétérinaire ; Inès, policière ; Une année à la ferme (l'agricultrice) ;
La journée du maître ; Sur le chantier. Les tenues et coiffes communes sont
dans le nouveau module `outils/illustrer/metiers.py`, posées sur `personne()`
grâce à deux nouveaux paramètres facultatifs (`tenue=`, `coiffe=`) qui ne
changent aucun SVG existant. Planches de toutes leurs illustrations revues dans
Chromium (cadrage, visages non masqués par les casques et casquettes,
cohérence des personnages d'une page à l'autre, accord entre dessin,
description et texte) ; notions vérifiées : vingt dents de lait, quatre
ingrédients du pain et levée par les bulles de gaz de la levure, blé semé à
l'automne et moissonné en été, bulle du niveau au milieu quand le mur est
droit, béton qui durcit après avoir été versé, heures des horloges.
`verifier-images.py` sans erreur et régénération complète identique pour les
livres existants (172 livres, 2 710 pages, 2 328 SVG). Le cache hors ligne
passe à `v18`.

## Ajout du 7 octobre 2026 (suite)

Treize livres (185 livres au catalogue). Rayon Sciences : Pourquoi la Lune me
suit ? ; Le voyage d'une goutte d'eau ; L'ombre de Léon ; Combien pèse un
nuage ? ; Le petit son qui voulait voyager ; Dans la grotte (visite inspirée
de Mammoth Cave, au Kentucky). Rayon Petites histoires : Je n'ai pas
sommeil ! ; Le jour où j'ai perdu ma dent ; Mamie parle une autre langue ;
La grande colère de Zoé ; Mon ami qui ne parle pas ; La course des chevaux
(un poulain du Kentucky qui préfère marcher). Rayon Les animaux : Le cardinal
rouge. Tous les dessins sont dans les scripts de chaque livre (le cardinal,
la voiture vue de profil, la grotte, le pré à clôture noire…) ; aucun module
partagé n'a été modifié. Planches de toutes les illustrations revues dans
Chromium (cadrage, personnages cachés sous la couette sans pieds visibles,
bulles dans l'image, accord entre dessin, description et texte). Notions
vérifiées : parallaxe (les objets proches défilent, la Lune à 384 000 km
reste à la même place dans la vitre, expérience du pouce) ; cycle de l'eau
(vapeur invisible, sel qui reste dans la mer, condensation dans l'air froid) ;
ombre toujours opposée au Soleil, longue le matin vers l'ouest, courte à
midi, longue le soir vers l'est, et opposée au lampadaire ; petit cumulus
d'environ 500 tonnes d'eau (cent éléphants, plus de trois mille baignoires),
un million de gouttelettes pour une goutte de pluie ; son qui se propage de
proche en proche, plus de quatre fois plus vite dans l'eau, par une ficelle
tendue, les murs et le bois, mais pas dans le vide ; grotte à environ 12 °C,
creusée par l'eau qui dissout le calcaire, stalactites qui gagnent un
centimètre en plusieurs dizaines d'années ; cardinal non migrateur, femelle
qui chante aussi, nourrissage bec à bec, environ douze jours de couvaison,
jeunes bruns au bec foncé, attaque de son reflet ; mots portugais (olá,
obrigada, gato, beijinho, bom dia, gosto muito de ti) ; signe « merci ».
`verifier-images.py` sans erreur et régénération complète identique pour les
livres existants (185 livres, 2 900 pages, 2 492 SVG). Le cache hors ligne
passe à `v19`.

## Personnages plus détaillés, 7 octobre 2026

Amélioration voulue de tous les personnages, donc de presque toutes les
illustrations (185 livres, 2 900 pages, 2 492 SVG, dont 2 150 modifiés).
Dans `base.py` (`perso()`) et `fantastique.py` (`personne()`) :

- liseré foncé autour de chaque personnage (filtre SVG), bras bordés d'un
  trait plus sombre pour se détacher du corps, pli du coude ;
- modelé : côté droit du corps et bas du visage dans l'ombre, reflet sur le
  front, ombre du menton sur le cou ;
- mains avec un pouce tourné vers le corps, pieds avec deux doigts,
  chaussures avec un reflet, revers de manche au poignet ;
- animaux : petite mèche sur la tête des espèces à poils, poils au bord du
  ventre, bout de queue plus foncé (chat), poils de la queue (renard, loup),
  laine bouclée (mouton) ; vêtements avec encolure et boutons ;
- humains : mèches et reflet dans les cheveux, creux de l'oreille, plis de la
  robe, encolure, pli du pantalon ;
- yeux avec un second reflet ; tête un peu penchée selon l'expression
  (timide, triste, malin, content…), sauf quand les mains touchent le visage ;
- petite ombre douce au sol, absente des personnages tournés ou en l'air, et
  coupée (`OMBRES_DOUCES = False`) dans les trois livres qui dessinent de
  vraies ombres portées (L'ombre de Léon, Max et son ombre, L'ours et la nuit),
  pour garder des ombres physiquement exactes ;
- nouvelles poses : `danse`, `applaudit`, `victoire`, `coucou`, `chut`,
  `etire`, `epaules`, `marche`, et pieds en mouvement (`pas="marche"`,
  `"pointe"`, `"saute"`), choisis automatiquement pour `course`, `danse` et
  `victoire`. Elles remplacent l'ancienne pose sur une cinquantaine de pages
  dont le texte s'y prête (danse, applaudissements, « chut », bâillements,
  « coucou », au revoir) ; trois descriptions ont été ajustées.

Planches revues dans Chromium (toutes les espèces, toutes les poses, et un
échantillon de pages de chaque rayon) ; `verifier-images.py` sans erreur,
`node --test` réussi, régénération complète identique. Le cache hors ligne
passe à `v20`.

## Parcours livre par livre

Chaque livre bénéficie des corrections communes de cadrage et de précision SVG. Les interventions propres à un livre sont indiquées dans la dernière colonne.

| Livre | Images | Éléments examinés et corrections |
| --- | ---: | --- |
| [L'Âne et le Petit Chien](../livres/ane-petit-chien/livre.js) | 16 | Chien dans les bras, âne chargé, salon renversé et étable. |
| [Boing ! fait la balle](../livres/balle-rebond/livre.js) | 14 | Balles écrasées au contact, rebonds décroissants sous la ligne de départ, ressort, trampoline, carrelage et sable. |
| [Le ballon de Nino](../livres/ballon-envole/livre.js) | 10 | Ballon, fête, séparation et voyage dans les paysages. |
| [Le premier jour de Bambou](../livres/bambou-ecole/livre.js) | 10 | Cœur dans la main en médaillon, classe, tour de cubes et dortoir. |
| [Basile se balance](../livres/basile-balancoire/livre.js) | 18 | Portique vu de côté, positions successives en transparence, pendules court et long, horloge à balancier. |
| [Bibi et Mimi](../livres/bibi-mimi/livre.js) | 12 | Rapport de taille éléphante-fourmi, ondes sonores partant de la trompe, image coupée jour / nuit. |
| [Ce n'est pas une boîte !](../livres/boite-magique/livre.js) | 10 | Transformations de la boîte et continuité des deux pandas. |
| [Le bonhomme de pain d'épice](../livres/bonhomme-pain-epice/livre.js) | 16 | Biscuit, personnages de la poursuite et traversée de la rivière. |
| [Boucle d'or et les trois ours](../livres/boucle-or/livre.js) | 16 | Trois tailles d’ours, bols, chaises et lits. |
| [Castor et la cabane perchée](../livres/castor-cabane/livre.js) | 14 | Rondins, brouette, rampe en pente douce, poulie fixe et moufle à deux brins ; corde qui arrive dans les mains. |
| [Cendrillon](../livres/cendrillon/livre.js) | 15 | Robe, carrosse, pantoufle et scènes du bal. |
| [Le Cerf se voyant dans l'eau](../livres/cerf-eau/livre.js) | 16 | Reflet entier dans l'eau, bois pris dans les branches, loup. |
| [Le chapeau de Monsieur Ours](../livres/chapeau-vent/livre.js) | 10 | Chapeau, bateau, escargot et nid. |
| [Le Petit Chaperon rouge](../livres/chaperon-rouge/livre.js) | 16 | Panier, capuchon, loup déguisé et chambre de la grand-mère. |
| [Le Chat botté](../livres/chat-botte/livre.js) | 17 | Bottes, cadeaux, carrosse et transformations de l’ogre. |
| [Moka garde le poisson](../livres/chat-poisson/livre.js) | 10 | Chat, bocal et poisson ; bocal de la vignette remonté. |
| [Oups, une tache !](../livres/chat-tache/livre.js) | 10 | Tache, dessin, peinture et image finale encadrée. |
| [Le Chêne et le Roseau](../livres/chene-roseau/livre.js) | 17 | Chêne, roseau et tempête ; vignette réduite pour garder la tête entière. |
| [Le Cheval et l'Âne](../livres/cheval-ane/livre.js) | 15 | Sacs serrés sur le dos sans cacher la tête, côte, âne épuisé et partage. |
| [Coline, la nouvelle](../livres/chouette-nouvelle/livre.js) | 10 | Groupe d’amis, branche et scènes de cache-cache. |
| [La Cigale et la Fourmi](../livres/cigale-fourmi/livre.js) | 17 | Violon, saisons et maison ; manche du violon rendu visible dans la vignette. |
| [Le Cochet, le Chat et le Souriceau](../livres/cochet-chat-souriceau/livre.js) | 15 | Trou de souris, terrier et grandes bulles de souvenir. |
| [Qui a peur du noir ?](../livres/cochon-noir/livre.js) | 10 | Silhouettes, faisceaux de lampe et objets de la chambre. |
| [La Colombe et la Fourmi](../livres/colombe-fourmi/livre.js) | 17 | Rivière, brin d’herbe, filet et fuite de la colombe. |
| [Qui attachera le grelot ?](../livres/conseil-rats/livre.js) | 17 | Assemblée, grelot, chat et personnages des bulles de pensée. |
| [Le Coq et le Renard](../livres/coq-renard/livre.js) | 17 | Branches, coq perché, renard et changement d’expression. |
| [Le Corbeau et le Renard](../livres/corbeau-renard/livre.js) | 17 | Fromage, bec, chute et déplacement du renard. |
| [Le cordonnier et les lutins](../livres/cordonnier-lutins/livre.js) | 15 | Chaussures, table de travail, lutins et cadeaux. |
| [Qui a pris la couronne ?](../livres/couronne-pie/livre.js) | 14 | Couronne, indices, personnages interrogés et nid de la pie. |
| [Les Deux Ânes](../livres/deux-anes/livre.js) | 14 | Ânes de profil, sacs de sel puis bât vide, éponges qui gonflent ; eau dessinée devant les ânes immergés. |
| [Les Deux Chèvres](../livres/deux-chevres/livre.js) | 17 | Tronc au-dessus du torrent, chute sous le tronc et merle. |
| [Les Deux Pigeons](../livres/deux-pigeons/livre.js) | 16 | Pigeonnier, pigeon en vol avec aile froissée, filet, épervier et aigle. |
| [Mon premier dodo chez Mamie](../livres/dodo-mamie/livre.js) | 10 | Doudou lapin bleu visible contre Lilou, lit, téléphone, Grande Ourse à la fenêtre. |
| [Chut ! Bébé dort](../livres/elephant-chut/livre.js) | 10 | Berceau, éléphants, gestes et scènes de nuit. |
| [L'énorme navet](../livres/enorme-navet/livre.js) | 14 | Chaîne des personnages et navet ; pointe du navet conservée dans la vignette. |
| [Léon prend son temps](../livres/escargot-promenade/livre.js) | 10 | Escargot, insectes, toile et scènes de la fête. |
| [L'étoile tombée du ciel](../livres/etoile-tombee/livre.js) | 14 | Étoile, échelle, cerf-volant et scènes nocturnes. |
| [Fâchés !](../livres/fache-pas-fache/livre.js) | 10 | Château de sable, expressions et réconciliation. |
| [Pétille, la petite fée](../livres/fee-petille/livre.js) | 14 | Baguette, transformations et lumières dans les scènes de nuit. |
| [Filou et le miroir](../livres/filou-miroir/livre.js) | 18 | Reflets, miroir, lac, cuillère et instruments optiques. |
| [Qui flotte, qui coule ?](../livres/flotte-coule/livre.js) | 10 | Objets au-dessus et sous l’eau ; immersion du bateau adaptée à son échelle. |
| [Fourmi et la grosse miette](../livres/fourmi-miette/livre.js) | 10 | Miette, traîneau, effort collectif et pente. |
| [Le garçon qui criait au loup](../livres/garcon-loup/livre.js) | 16 | Troupeau, village, fausses alertes et arrivée du loup. |
| [Gaston le glaçon](../livres/gaston-glacon/livre.js) | 18 | Glace, eau, vapeur et scènes dans le lac. |
| [Zoé et le géant timide](../livres/geant-timide/livre.js) | 14 | Rapport de taille entre géant, enfants et village. |
| [Les saisons de Grand Chêne](../livres/grand-chene/livre.js) | 10 | Arbre et écureuil au fil des quatre saisons. |
| [La Grenouille et le Bœuf](../livres/grenouille-boeuf/livre.js) | 17 | Gonflement de la grenouille ; « Pfffff ! » remonté dans le cadre. |
| [Dix grenouilles sur un nénuphar](../livres/grenouilles-nenuphar/livre.js) | 14 | Dix places sur le nénuphar, une particularité par grenouille, soleil qui descend de page en page. |
| [Les habits neufs de l'empereur](../livres/habits-empereur/livre.js) | 15 | Métier à tisser vide, défilé et expressions de la foule. |
| [Hansel et Gretel](../livres/hansel-gretel/livre.js) | 17 | Miettes, maison, cage, four et retour des enfants. |
| [Pic est en colère](../livres/herisson-colere/livre.js) | 10 | Cubes, expressions, respiration et reconstruction de la tour. |
| [Le Héron](../livres/heron/livre.js) | 15 | Rivière du matin à la nuit, poissons, escargot ; bulles éloignées du bec. |
| [Petit Hibou et la Lune](../livres/hibou-lune/livre.js) | 10 | Hiboux, silhouettes de la Lune et petit schéma explicatif. |
| [Jack et le haricot magique](../livres/jack-haricot/livre.js) | 17 | Haricot, château et géant ; « Z » repositionnés pour éviter le haut du cadre. |
| [La Moufle](../livres/la-moufle/livre.js) | 14 | Moufle qui gonfle de page en page, têtes des habitants dessinées derrière le bord. |
| [Le Trésor du laboureur](../livres/laboureur-tresor/livre.js) | 17 | Bêches, champ, pousses, récolte et marché. |
| [La Laitière et le Pot au lait](../livres/laitiere-pot/livre.js) | 17 | Pot porté sur la tête, bulles de pensée et fragments après la chute. |
| [Les Fées](../livres/les-fees/livre.js) | 15 | Fleurs, perles et diamants qui tombent de chaque côté, crapauds et couleuvre rigolos. |
| [Lili la licorne](../livres/licorne-couleurs/livre.js) | 14 | Couleurs de la crinière, arc-en-ciel et reflet dans l’eau. |
| [Le Lièvre et les Grenouilles](../livres/lievre-grenouilles/livre.js) | 16 | Gîte, mare à droite du lièvre, grenouilles et scènes de nuit assombries. |
| [Le Lièvre et le Hérisson](../livres/lievre-herisson/livre.js) | 14 | Sillon vu de côté avec drapeaux de départ et d'arrivée ; Hortense distinguée par une petite fleur. |
| [Le Lièvre et la Tortue](../livres/lievre-tortue/livre.js) | 17 | Course, sieste, chemin et groupe à l’arrivée. |
| [Lina et l'aimant](../livres/lina-aimant/livre.js) | 18 | Aimants, objets triés, pôles et schémas. |
| [Le Lion et le Moucheron](../livres/lion-moucheron/livre.js) | 17 | Lion, insecte et toile ; ailes du moucheron conservées dans la vignette. |
| [Le Lion et le Rat](../livres/lion-rat/livre.js) | 17 | Différence de taille, filet, cordes et libération. |
| [Pas encore !](../livres/lou-velo/livre.js) | 10 | Vélo, casque et postures ; oreilles de Lou conservées dans la vignette. |
| [Le Loup et l'Agneau](../livres/loup-agneau/livre.js) | 16 | Ruisseau et sens du courant, loup, agneau, bergère et chien de berger. |
| [Le Loup, la Chèvre et le Chevreau](../livres/loup-chevre-chevreau/livre.js) | 15 | Maison, chevreau à la fenêtre, pattes grise et blanche. |
| [Le Loup et le Chien](../livres/loup-chien/livre.js) | 17 | Collier, chaîne, personnages et scènes de nuit. |
| [Le Loup et la Cigogne](../livres/loup-cigogne/livre.js) | 18 | Bec dans la gueule du loup, os, panier de poissons ; vignette sur fond clair. |
| [Le loup et les sept chevreaux](../livres/loup-sept-chevreaux/livre.js) | 16 | Sept chevreaux, cachettes, sac et retour de la mère. |
| [Les lunettes de Plume](../livres/lunettes-plume/livre.js) | 10 | Lunettes rouges superposées au personnage, scène floue (filtre gaussien) puis nette. |
| [Mes mains font clap !](../livres/mains-clap/livre.js) | 12 | Cinq enfants aux peaux et coiffures variées, un geste par partie du corps. |
| [Max et son ombre](../livres/max-ombre/livre.js) | 10 | Ombres au sol, rayons lumineux et ombre sur le mur. |
| [Le Meunier, son Fils et l'Âne](../livres/meunier-ane/livre.js) | 17 | Positions des personnages et âne ; oreilles conservées dans la vignette. |
| [C'est mon tour !](../livres/mon-tour/livre.js) | 10 | Toboggan, file d'attente et bulle « Vas-y, passe ! ». |
| [Les mots magiques](../livres/mots-magiques/livre.js) | 10 | Bulles, personnages et mots mis en scène. |
| [Un mouton, deux moutons…](../livres/moutons-dodo/livre.js) | 10 | Moutons numérotés, clôture et scènes de sommeil. |
| [Les musiciens de Brême](../livres/musiciens-breme/livre.js) | 16 | Quatre animaux, pyramide et maison des brigands. |
| [Noisette déménage](../livres/noisette-demenage/livre.js) | 10 | Noisette et Grand Chêne repris du « Grand chêne », creux d'arbre, boîte à trésors et dessin des deux arbres. |
| [Nour et le vent](../livres/nour-vent/livre.js) | 18 | Bulles, moulinet, voilier et montgolfière ; manche du moulinet conservé dans la vignette. |
| [Où est Doudou ?](../livres/ou-est-doudou/livre.js) | 10 | Jouets, rangement et doudou ; vignette remontée et cube « A » éloigné du bord. |
| [L'Ours et les Deux Compagnons](../livres/ours-compagnons/livre.js) | 14 | Personnage couché (rotation) remonté dans le cadre, ours qui renifle, arbre refuge. |
| [Le gâteau de Petit Ours](../livres/ours-gateau/livre.js) | 10 | Cuisine, four, gâteau ; visages des invités remontés dans la fenêtre. |
| [Petit Ours ne veut pas dormir](../livres/ours-nuit/livre.js) | 18 | Jour et nuit, orange éclairée, lampe et scènes extérieures. |
| [Le voyage de Petit Nuage](../livres/petit-nuage/livre.js) | 10 | Nuage, paysages, pluie, fleurs et scène nocturne. |
| [Le Petit Poucet](../livres/petit-poucet/livre.js) | 16 | Frères, cailloux, ogre et bottes. |
| [La petite graine](../livres/petite-graine/livre.js) | 10 | Graine, racines, feuilles, fleur et pollinisation illustrée. |
| [La petite marmite](../livres/petite-marmite/livre.js) | 14 | Marmite qui déborde, flot de bouillie qui monte de la cuisine au village. |
| [La petite poule rousse](../livres/petite-poule-rousse/livre.js) | 15 | Blé, animaux, moulin et étapes du pain. |
| [Pingo glisse !](../livres/pingo-glisse/livre.js) | 18 | Glissade, surfaces, roues et scènes de frottement. |
| [Pinson chante faux](../livres/pinson-chant/livre.js) | 10 | Branches, oiseaux, notes et scènes de brouillard. |
| [Pourquoi tout tombe ?](../livres/piquette-chute/livre.js) | 18 | Objets en chute, flèches, parachute et scènes d’équilibre. |
| [Boum ! fait le tambour](../livres/pompon-sons/livre.js) | 18 | Tambour, ondes et expériences ; « tagada, tagada… » recentré. |
| [Le Pot de terre et le Pot de fer](../livres/pot-terre-fer/livre.js) | 15 | Pots qui parlent, fêlure, éclats et pansement ; feu visible dans la cheminée. |
| [La Poule aux œufs d'or](../livres/poule-oeufs-or/livre.js) | 17 | Poule, œufs et trésor ; œuf et rayons entièrement visibles dans la vignette. |
| [Le prince grenouille](../livres/prince-grenouille/livre.js) | 14 | Couronne, étang, saut et scènes de nuit. |
| [La princesse au petit pois](../livres/princesse-petit-pois/livre.js) | 14 | Lit, petit pois, matelas, échelle et expressions. |
| [Raiponce](../livres/raiponce/livre.js) | 16 | Tour, tresse, échelle et personnages au pied de la tour. |
| [Le Rat et l'Huître](../livres/rat-huitre/livre.js) | 15 | Huître ouverte et fermée, petite huître cernée sur le bout du nez, marée montante. |
| [Le Rat de ville et le Rat des champs](../livres/rat-ville-champs/livre.js) | 17 | Repas, souris, chat et lieux de vie. |
| [Le Renard et le Bouc](../livres/renard-bouc/livre.js) | 17 | Puits, sortie du renard, bouc et échelle. |
| [Le Renard et la Cigogne](../livres/renard-cigogne/livre.js) | 17 | Assiettes et vases ; assiette de la vignette recentrée et réduite. |
| [Oups ! dit Renardeau](../livres/renard-pot/livre.js) | 10 | Pot, fragments, réparation et gestes des personnages. |
| [Le Renard et les Raisins](../livres/renard-raisins/livre.js) | 17 | Grappes, sauts, bâton et écureuil. |
| [Rose et le petit dragon](../livres/rose-dragon/livre.js) | 14 | Dragons, princesses, chevaliers et tailles respectives. |
| [Sacha chez les planètes](../livres/sacha-planetes/livre.js) | 18 | Fusée, astronaute et planètes ; fusée de la vignette ajustée au cadre. |
| [La semaine de Petit Hérisson](../livres/semaine-herisson/livre.js) | 10 | Un décor par jour et calendrier L M M J V S D avec le jour entouré. |
| [Le Singe et le Chat](../livres/singe-chat/livre.js) | 16 | Cheminée, marrons, pince à feu et servante. |
| [Marina et la perle perdue](../livres/sirene-perle/livre.js) | 14 | Sirènes, perle, animaux marins et scène de la grotte. |
| [La soupe de la sorcière](../livres/sorciere-soupe/livre.js) | 14 | Marmite, légumes et rassemblement des personnages. |
| [La soupe au caillou](../livres/soupe-caillou/livre.js) | 15 | Marmite, caillou, ingrédients et repas partagé. |
| [Souris et Éléphant](../livres/souris-elephant/livre.js) | 18 | Bascule et leviers ; légende « pivot » remontée. |
| [Le parapluie de Souris](../livres/souris-parapluie/livre.js) | 10 | Parapluie, feuille, pluie et groupe des animaux. |
| [Où est passé le sucre ?](../livres/sucre-disparu/livre.js) | 14 | Verres comparés (sucre, sable, sel, huile), loupe sur les grains, cristaux de sel, marais salants, filtre. |
| [J'ai perdu !](../livres/tibo-perdu/livre.js) | 10 | Plateau du jeu des noisettes, dé qui vole, « boule dans le ventre » gribouillée, pissenlit soufflé. |
| [Tilou a froid aux pattes](../livres/tilou-chaleur/livre.js) | 18 | Cuillères métal et bois, glaçon et mitaine, hutte de castor en coupe, thermomètres et bouillotte. |
| [La Tortue et les deux Canards](../livres/tortue-canards/livre.js) | 17 | Bâton, vol, tortue et chute dans la meule. |
| [Les trois boucs et le troll](../livres/trois-boucs/livre.js) | 14 | Trois tailles de boucs, pont et troll. |
| [Les trois petits cochons](../livres/trois-petits-cochons/livre.js) | 16 | Maisons et souffle du loup ; « PLOUF ! » abaissé dans le cadre. |
| [Le vilain petit canard](../livres/vilain-petit-canard/livre.js) | 16 | Caneton et cygnes ; pattes de la vignette conservées, reflet atténué et limité à l’eau. |
| [Zoé et la petite ampoule](../livres/zoe-ampoule/livre.js) | 18 | Pile, ampoule et boucle fléchée dans le sens du courant ; interrupteur, série de deux ampoules, cabane et ombres. |

## Reprendre une revue

Ouvrir [la revue interactive](revue-images.html), choisir un livre, puis passer des illustrations originales aux pages du livre. Chaque image propose son texte, sa description et un lien vers le SVG original. Le validateur (`python3 outils/verifier-images.py`) inclut aussi les livres présents dans `livres/` qui ne figurent pas encore au catalogue.

## Relief des illustrations (7 octobre 2026)

Aucun livre ajouté (185 livres, 2 900 pages, 2 492 SVG) : les outils partagés
dessinent désormais en volume, donc presque toutes les illustrations sont
régénérées. Dégradés partagés (`lineaire`, `radial`, `volume`, `cylindre`),
ombres douces en dégradé, reflets ; paysages sur trois plans (chaîne lointaine
fondue dans le ciel, collines avec brume à leur pied, sol plus sombre et
texturé devant), savane, mare, plage et banquise aussi ; maisons, immeubles
de ville et châteaux détaillés (tuiles, bardage ou pierres, linteaux, appuis,
ombre sous les avancées) ; montagnes avec versant à l'ombre ; intérieurs avec
parquet en perspective et pénombre des coins. Personnages : corps et tête en
relief, vue de trois quarts quand ils regardent de côté, corps penché pour
courir, marcher, danser ou tirer. Planches revues dans Chromium (échantillon
aléatoire de tous les rayons, scènes d'intérieur, de nuit et de conte).
`verifier-images.py` sans erreur. Le cache hors ligne passe à `v21`.

## Relief des dessins propres à chaque livre (7 octobre 2026)

Aucun livre ajouté (185 livres, 2 900 pages, 2 492 SVG). Modelé automatique
des aplats de tous les dessins des livres (léger dégradé, lumière en haut à
gauche) ; restent plats les formes semi-transparentes, les masques, les
formes de la couleur du fond (fausses découpes) et les astres éclairés des
livres de sciences (phases de la Lune, planètes, sphères : `sans_relief()`).
Reprise à la main des décors les plus visibles : maisons de paille, de bois
et de briques des trois petits cochons ; maison en pain d'épice ; chaumière
de la chèvre ; grange et poulailler ; niche ; cabane perchée de Capucine ;
caserne des pompiers ; maison du chantier ; école de Bambou ; grands arbres
du coq, du corbeau, du pinson, des ours et de Lunettes ; arbres sombres de
la forêt des contes ; pont de bois et tronc sur le torrent (rochers à
fissures). Les 185 couvertures et 120 pages tirées au hasard ont été revues
dans Chromium : aucune fausse découpe devenue visible. Régénération
déterministe (identique livre par livre et pour l'ensemble),
`verifier-images.py` sans erreur. Le cache hors ligne passe à `v22`.

## Profondeur, poses et architecture (7 octobre 2026)

Aucun livre ajouté (185 livres, 2 900 pages, 2 492 SVG) ; outils partagés
enrichis, donc presque toutes les illustrations sont régénérées.

- Paysages sur trois plans nets : chaîne lointaine bleuie (`lointain()`),
  plaine du plan moyen au pied des collines (le ciel ne passe plus entre les
  collines et le sol), versant droit des collines à l'ombre, bosquets voilés
  sur les pentes (`bosquet()`), et premier plan du sol plus grand et plus
  contrasté : touffes d'herbe (`touffe()`), cailloux sur le sable, ombres de
  congères sur la neige (`premier_plan_sol()`, `sol(…, premier=False)` pour
  s'en passer). Nouveaux outils : `paysage()` (scène complète, collines ou
  montagnes), `repoussoir()` (feuillage sombre dans un coin du premier plan).
  Savane : acacias en volume, herbes sèches plus grandes devant.
- Architecture : `maison()` vue de trois quarts (mur latéral dans l'ombre, pan
  de toit qui fuit, cheminée qui en sort, chaînage d'angle, gouttière et
  descente, fenêtres à linteau et appui saillant, volets en option),
  `immeuble()` réutilisable (mansarde à lucarnes, pignon ou toit plat,
  corniche et bandeaux avec leur ombre, balcons en fer forgé, volets,
  boutique à store rayé, soubassement à refends, côté en perspective) et
  ses pièces : `fenetre_facade()`, `volet()`, `chainage()`, `cote_batiment()`,
  `garde_corps()`, `store_banne()`. La rue de `ville()` (rat des villes,
  empereur, policière…) passe sur deux plans, silhouettes lointaines voilées
  puis immeubles détaillés.
- Personnages : ombres propres froides à bord fondu et lumière réfléchie au
  bord du corps et de la tête, liseré de lumière, ombre portée allongée du
  côté opposé à la lumière ; pieds en appui (l'un un peu en avant) au repos ;
  trois quarts plus marqués (œil lointain plus petit, ventre décalé) ; joues
  ébouriffées du chat, du renard, du loup et de l'écureuil. Nouvelles poses :
  `court`, `saute`, `lance`, `designe`, `pousse`, `equilibre` ; la course
  (`course`) lève un pied et penche davantage, les bras levés (`haut`) se
  plient aux coudes. Seize scènes reprises avec ces poses (sauts de joie,
  trampoline, équilibre, course vers Papa, poussée de la miette, etc.).
- Animaux dessinés à part en volume, avec liseré : oiseau (et donc corbeau,
  coq, colombe), chouette, escargot (coquille striée), poisson (écailles),
  tortue (écailles bombées), cheval, âne et cerf de profil (pattes du côté
  opposé plus sombres), cigogne et héron.
- Exactitude : dans les livres de sciences, l'ombre douce reste centrée
  (`OMBRE_SENS`, réglable par livre avec `SENS_OMBRE`) pour ne jamais
  contredire la position du Soleil dessiné.
- Corrections : le moulin des deux ânes passe devant les collines ; les
  reflets du cerf sont dessinés à part (identifiants SVG distincts).

Contrôles : planches des 185 couvertures, de 90 pages tirées au hasard et de
toutes les scènes reprises, revues dans Chromium ; régénération déterministe
(identique livre par livre et pour l'ensemble) ; `verifier-images.py` sans
erreur ; `node --test` réussi. Le poids total des SVG passe de 58 à 71 Mo.
Le cache hors ligne passe à `v23`.
