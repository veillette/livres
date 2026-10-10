# Revue systématique des illustrations

Revue du 29 septembre 2026 : **86 livres, 1 426 pages et 1 234 illustrations SVG**.
Catalogue actuel, après les ajouts d'octobre : **240 livres, 3 780 pages et
3 257 illustrations SVG** (cache hors ligne `v31`).

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

## Direction artistique : lumière, cadrage, âges et petite bête (7 octobre 2026)

Aucun livre ajouté (185 livres, 2 900 pages, 2 492 SVG). Retouche globale
voulue : la finition des pages change, donc tous les SVG sont régénérés.

- Finition de chaque page (`Scene.svg()`, `AMBIANCES`) : moment déduit du
  décor ou imposé (`S.ambiance()`). La nuit reçoit une teinte bleutée et un
  vignettage marqué, le soir une teinte dorée ; les sources de lumière
  (`S.lumiere()`, et d'elles-mêmes la lune, `maison(lumiere=True)`,
  `lampe()`, `luciole()`, `etoile_perso()`) brillent au-dessus de la teinte.
  Halo doux et vignettage léger le jour et dans les intérieurs. Ni teinte ni
  halo en sciences ; fonds unis sombres (salle noire, espace) sans teinte.
  Patine de vieux papier très pâle sur les fables et les contes. Calques
  posés seulement sur une scène qui a un fond (pas sur les vignettes
  transparentes). Un premier essai de glacis teinté par la couleur du livre
  grisait les ciels bleus : abandonné.
- Grain du papier : posé par `css/pages.css` sur toute la page, à l'échelle
  de l'écran (dans le SVG, il devenait du bruit sur les couvertures de 228 px
  de la bibliothèque) ; retiré à l'impression.
- Cadrage : `S.camera()` (gros plan sans bord vide), `S.dessus()` et
  `S.vers_page()` pour les bulles hors zoom.
- Personnages humains : `stature=` (`petit`, `enfant`, `ado`, `adulte`,
  `ancien`), `carrure=`, `nez=`, `yeux=`, `taches=`, `rides=`, coiffures
  `carre`, `afro`, `couettes`, `raie` ; `ancre()` et `mains_personne()` pour
  les objets tenus ; poses d'échange `main`, `epaule`, `tend`,
  `mains_jointes`, `ramasse`, `leve_doigt`.
- Intérieurs : `piece()` (`chaumiere`, `manoir`, `chateau`, `chambre`,
  `cuisine`) ; le papier peint d'`interieur(papier=…)` prend un motif propre
  à chaque livre (rayures, pois, fleurs, losanges ou étoiles).
- Petite bête cachée : une coccinelle (une étoile de mer sous l'eau) sur
  chaque page pleine, dans une cachette libre proposée par le décor, au plus
  près d'un bord et jamais sur un personnage (`occuper()`). Tout ou rien par
  livre : 56 livres l'ont sur toutes leurs pages ; `generer.py` nomme les
  pages qui en privent les autres. Seize pages complétées à la main
  (`S.cachette()`). La bibliothèque l'annonce aux enfants.
- Livres retouchés :
  - *Le Petit Chaperon rouge* : chaumière de la mère-grand, cuisine de la
    maman, adultes et grand-mère à leur taille, gros plans de plus en plus
    serrés sur « grandes oreilles » puis « grands yeux » (descriptions mises
    à jour) ;
  - *Cendrillon* : salon à boiseries, cuisine au coin du feu éclairée par la
    cheminée, belle-mère grande et sèche, demi-sœurs ronde et fine, prince
    adulte, marraine âgée, château qui domine l'escalier de minuit,
    mariage main dans la main ;
  - *La chenille qui devient papillon* : jardin flou derrière la tige (fil,
    chrysalide, sortie), chrysalide plus grande ;
  - *La chouette qui vole sans bruit* : la chasse vue d'en bas, plongée en diagonale
    devant la pleine lune ;
  - *Le boulanger de la nuit* : vitrine garnie de pains qui éclaire la rue.
  - Vérifié sans retouche : les abeilles de *Bzzz ! La ruche des abeilles* sont à la
    bonne échelle (une ouvrière fait 2,5 à 3 alvéoles de long).
- Compétences : `direction-artistique` (règles de plans, lumière, âges,
  décors, petite bête) et `retoucher-livre` (parcours de retouche, planche
  avant/après `avant-apres.js`) ; `nouveau-livre` et `AGENTS.md` y renvoient.

Contrôles : planches de toutes les pages retouchées, des pages de nuit et de
soir (deux par livre), d'un intérieur par livre, de 49 pages de jour et de
80 pages à petite bête tirées au hasard, revues dans Chromium ; bibliothèque
et lecteur à l'écran (densité 1 et 2) ; export PDF de *Cendrillon* (4,5 Mo,
comme avant). Régénération déterministe ; `verifier-images.py` sans erreur ;
`node --test` réussi. Temps d'affichage de la bibliothèque inchangé
(≈ 3,7 s dans Chromium). Le poids total de `livres/` passe de 68,6 à 75,0 Mo.
Le cache hors ligne passe à `v24`.

## Retouche : la petite bête dans presque tous les livres (8 octobre 2026)

Aucun livre ajouté (185 livres, 2 900 pages, 2 492 SVG). La coccinelle
cachée n'était que dans 56 livres : il manquait une cachette sur au moins
une page des 129 autres. Elle est désormais sur toutes les pages pleines
de **184 livres** (2 286 pages). *Sacha chez les planètes* (dans
l'espace) n'en a pas ; quatre pages dans l'espace se mettent hors du jeu
(`S.cachette(None)`) : la Terre ronde, la Lune et la Lune qui tourne de
*Pourquoi tout tombe ?*, l'espace du *Petit son qui voulait voyager*.

- Cachettes : sols tracés à la main reconnus (hors eau bleue, claire ou
  sombre), rang de secours devant les pieds quand le bord est pris ; coupes
  du sol (`coupe_terre`, terrier des marmottes) : la bête se pose sur
  l'herbe, jamais dans la terre ; sous l'eau d'une mare (`sous_l_eau`) et
  au fond de la mer, un petit poisson nage à sa place.
- Nouvelles bêtes : coccinelle en vol (`"air"`), petit poisson
  (`"poisson"`).
- Jamais sur un personnage, une bulle ou un texte : repères invisibles
  `occuper()` lus à travers les transformations, pour les personnages
  (étendue mesurée de chaque espèce et mains de la pose), les humains, les
  bulles et textes, les animaux de profil (cheval, âne, cerf), le
  bonhomme de pain d'épice, le carrosse, le chaudron, le cygne, le crabe, le
  poulpe, le pingouin, le glaçon, les pots qui parlent et onze personnages
  propres à un livre (vache, cardinal, éléphants, manchots, marmite…).
- Outil `retoucher-livre/cachettes.py` : il cherche une place d'après
  l'image rendue et l'écrit (`S.cachette`) ; les scripts en comptent 504
  (468 en vol, 15 poissons, 17 posées, 4 pages hors jeu), presque toutes
  écrites par l'outil. Son mode `--verifier` déplace les bêtes sur du rouge
  (camion de pompier, tambour, toboggan, four), posées dans l'eau ou sur un
  personnage (61 places). Ses seuils ont été réglés sur
  une première passe de tout le catalogue : 233 alertes, dont la plupart à
  tort (sol orangé de la savane, sol violet de nuit, carrelage gris-bleu,
  plinthe ou tronc derrière la bête). Planche de revue en gros plans
  (`planche_cachettes.py`).
- Corrigé à la main : coccinelle dans le feu (*Le Singe et le Chat*), dans
  la mare des canards (*La Tortue et les deux Canards*), sur le mouton
  endormi (*Un mouton, deux moutons…*), dans l'étang de *Lina et l'aimant*,
  sur le bébé éléphant, en vol dans la terre (*Flocon, la fée de l'hiver*,
  *La marmotte dort tout l'hiver*).

Contrôles : 48 planches de gros plans de toutes les pages (2 290), puis
planches des 175 pages signalées et de toutes les places déplacées, revues
dans Chromium ; `cachettes.py --tous --verifier` ne signale plus que trois
fausses alertes (bête au pied d'un sapin enneigé, *L'étoile de Noël*) ; régénération
déterministe ; `verifier-images.py` sans erreur ; `node --test` réussi. Le
cache hors ligne passe à `v25`.

## Retouche du 8 octobre 2026 : lumières de la nuit

Aucun livre ajouté : **185 livres, 2 900 pages et 2 492 SVG**. Deux images
reprises sans modifier les autres livres :

- *La chouette qui vole sans bruit*, page « La chasse » : trois plans de
  prairie, épis éclairés par la lune et lueur froide au-dessus de l'herbe.
- *Le boulanger de la nuit*, page « La nuit » : vitrine avec croisillons,
  profondeur, reflets et pains visibles derrière la vitre ; la lumière chaude
  continue sur la façade et le trottoir.

Descriptions des deux pages mises à jour. Le cache hors ligne passe à `v26`.

## Réécriture du 8 octobre 2026 : les dix livres de fêtes

Aucun livre ajouté : **185 livres, 2 952 pages et 2 544 SVG**. Les dix livres
du rayon « Fêtes » sortaient d'un même gabarit (six pages, un objet au centre
entre deux personnages, des images qui ne montraient pas ce que disait le
texte). Ils sont réécrits et redessinés, chacun avec son propre script dans
`histoires/` ; `livres_fetes.py` et `creer_livres_fetes.py` sont supprimés et
`fetes.py` ne garde que des accessoires partagés. Chaque livre a maintenant
11 ou 12 scènes, une vraie intrigue (attente, fausse piste, retournement),
des répétitions et onomatopées, et des traditions exactes :

- *L'étoile de Noël* : quête de l'étoile la plus brillante, voisins
  qu'on emmène, étoile « plus loin que la Lune », étoile fabriquée ensemble.
- *Le panier de Pâques* : cloches revenues de leur voyage, chasse aux œufs
  comptée, « tu chauffes, tu brûles », friture en chocolat.
- *La citrouille d'Halloween* : citrouille creusée, « des bonbons ou un
  sort », chaque frayeur cache un ami.
- *Le vœu de minuit* : l'horloge avance de page en page, compte à rebours,
  vœu lu à voix haute.
- *Le masque du carnaval* : Mardi gras et crêpes, trois déguisements ratés,
  la Lionne-Pirate-Volante, Monsieur Carnaval et la fanfare.
- *Des cartes pour les amis* : un cœur par personne aimée, puis la carte pour
  l'enfant qui joue seul.
- *Le tambour de la fête* : 21 juin, jour le plus long, charivari remis en
  rythme par un tambour de casserole.
- *Le bouquet de maman* : surprise secrète, bouquet volé par le chien,
  fleur mâchouillée et dessin de famille.
- *Le cerf-volant de papa* : pas de vent, puis la vrille ; une queue (cravate,
  foulard, chaussette) rend le cerf-volant stable.
- *Le gâteau d'anniversaire* : la journée où tout le monde semble avoir
  oublié, fête surprise, cinq bougies et vœu secret.

Familles humaines (Pâques, Nouvel An, carnaval, musique, fêtes des mères et
des pères) avec adultes, grands-parents et tout-petits à leur taille ;
plans variés (gros plans aux moments forts, contre-plongées, plans larges),
halos des lanternes, citrouilles, réverbères et fenêtres la nuit.

Contrôles : planches de toutes les pages des dix livres revues dans Chromium
et corrigées ; coccinelle présente sur toutes les pages pleines, vérifiée par
`cachettes.py --verifier` et en gros plans (`planche_cachettes.py`) ;
régénération complète sans changement des autres livres ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors ligne
passe à `v27`.

## Changement du 9 octobre 2026 : les SVG ne sont plus dans le dépôt

Les 2 544 SVG de `livres/*/images/` sont retirés du suivi git
(`.gitignore`) : la publication les dessine elle-même avec `generer.py`. À
leur place, `generer.py` écrit `outils/illustrer/empreintes.txt`, une ligne
par image (empreinte SHA-256 abrégée, puis `<id>/<nom>`). La publication
échoue si les images qu'elle dessine n'ont pas les empreintes validées ;
`verifier-images.py` signale aussi un SVG local périmé. `avant-apres.js`
redessine l'« avant » à partir des scripts du commit de référence.

Aucune image ne change : régénération complète identique aux SVG suivis
jusqu'ici ; `verifier-images.py` sans erreur ; `node --test` réussi. Le cache
hors ligne reste à `v27`.

## Ajout du 9 octobre 2026 : quatre nouveaux livres de fêtes

Le rayon « Fêtes » passe de dix à quatorze livres (15 pages et 13 SVG
chacun), chacun avec son propre script dans `outils/illustrer/histoires/` :

- *Boubou cherche un costume* (`fantome-costume`, Halloween) : un petit
  fantôme de grenier essaie un chapeau trop grand, une citrouille trop
  lourde, une cape qui l'emmêle, puis sort comme il est ; quand le vent
  souffle la lanterne, c'est lui qui brille pour ramener les enfants.
- *L'arbre aux mercis* (`arbre-mercis`, Action de grâce) : verger, courges,
  tarte aux pommes chez Grand-maman ; une branche dans un pot se couvre de
  feuilles d'érable en papier, une par merci, jusqu'au grand repas.
- *Des biscuits pour le père Noël* (`noel-biscuits`, Noël) : biscuits
  découpés, cuits et décorés, neuf carottes pour les rennes ; Caramel le
  chat pris sur le fait la nuit, un traîneau devant la Lune, un petit mot au
  matin.
- *Bonne année, grosse santé !* (`jour-de-l-an`, jour de l'An) : chez les
  grands-parents, Léon apprend ce qu'est un souhait et en offre un à chacun
  (tourtière, glissade, violon, chien) ; le soir, la petite Lili fait ses
  trois premiers pas jusque dans ses bras.

Personnages humains d'âges variés (tout-petits, enfants, parents,
grands-parents), chat, chien et petit fantôme dessiné à la main avec son
`occuper()` ; plans variés (gros plans aux moments forts, plans larges en
extérieur), halos des lanternes, fenêtres et cheminées la nuit, Boubou qui
éclaire la rue dans le noir. Les objets propres à ces livres (fenêtre ronde,
malle, feuille d'érable, dinde, tourtière, biscuits et emporte-pièces,
traîne sauvage, bonhomme de neige…) sont dans leurs scripts : aucun module
partagé n'a changé.

Contrôles : planches de toutes les pages des quatre livres revues dans
Chromium et corrigées ; coccinelle présente sur toutes les pages pleines,
vérifiée par `cachettes.py --verifier` ; régénération complète sans
changement des autres livres (`empreintes.txt` ne gagne que 52 lignes) ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors ligne
passe à `v28`.

## Ajout du 10 octobre 2026 : cinq histoires de dragons

Cinq livres de dragons, 73 nouvelles illustrations :

- *Boucle d'or et les trois dragons* (`boucle-or-dragons`, Princesses, fées
  et dragons) : le conte des trois ours dans une grotte à porte ronde ; la
  soupe réchauffée d'un souffle de feu, un tas d'or, des coussins et un nid
  de paille pour lits ; au réveil, Boucle d'or demande pardon et tout le
  monde mange ensemble.
- *Les dragons musiciens* (`dragons-musiciens`, Princesses, fées et
  dragons) : les musiciens de Brême avec Tison et ses ronds de fumée, Brume
  et son brouillard, Plume qui ne vole pas et Étincelle qui a le hoquet ; la
  pyramide de dragons fait fuir les brigands et le trésor revient au roi.
- *L'école des petits dragons* (`ecole-dragons`, Princesses, fées et
  dragons) : histoire originale ; Flammèche, au tout petit feu, rate ses
  leçons mais est la seule à allumer les lanternes de papier sans les
  brûler.
- *Le lapin et le Roi Dragon* (`lapin-roi-dragon`, Contes traditionnels) :
  d'après le conte coréen ; palais sous la mer aux toits de tuiles
  recourbés, médecin poulpe, portrait du lapin, ruse du foie qui sèche sur
  un rocher ; la fin offre au roi une racine de ginseng.
- *Le Serpent arc-en-ciel* (`serpent-arc-en-ciel`, Contes traditionnels) :
  d'après une légende des Aborigènes d'Australie, sans imiter leurs
  peintures ; le Serpent creuse les vallées, chatouille les grenouilles
  pleines d'eau et réveille les animaux (kangourou, émeu, koala, lézard).
  L'arc-en-ciel final a le rouge à l'extérieur et le Soleil hors de l'image,
  dans le dos de qui le regarde.

Nouveau module partagé `outils/illustrer/dragons.py` (dragon habillé,
dragon couché, jets de feu, de fumée et de givre, brouillard, tas d'or,
coffre, nid, grotte, lanterne de papier) : il n'est utilisé que par ces
livres. Plans variés (gros plans aux moments forts, contre-plongée sur
Tison, plongée sur la vallée), halos des torches, fenêtres et lanternes la
nuit, souffles dirigés de côté pour ne jamais cacher un visage.

Contrôles : planches de toutes les pages des cinq livres revues dans
Chromium et corrigées ; coccinelle présente sur toutes les pages pleines,
vérifiée par `cachettes.py --verifier` ; régénération complète sans
changement des autres livres (`empreintes.txt` ne gagne que 73 lignes) ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors ligne
passe à `v29`.

## Ajout du 10 octobre 2026 : six comptines

Le rayon Comptines passe de quatre à dix livres, 75 nouvelles illustrations :

- *Alouette, gentille alouette* (`alouette`) : la chanson, version
  chatouilles : Margot chatouille l'alouette avec un épi de blé, de la tête
  à la queue, puis l'alouette la chatouille à son tour. Alouette dessinée
  dans le script (huppe, sourcil clair, dos rayé) ; l'épi va de la main de
  Margot à la partie chantée, calculée sur le dessin.
- *Une souris verte* (`souris-verte`) : la comptine, version douce (un bain
  moussant, « un escargot tout chaud » en serviette roulée), puis sa suite :
  le tiroir trop noir, le chapeau trop chaud, la poche à brioche et le lit.
- *Promenons-nous dans les bois* (`promenons-nous`) : le loup s'habille
  pièce par pièce (culotte, chemise, chaussettes, écharpe, chapeau,
  lunettes), puis ne veut que jouer au loup et goûter.
- *Cinq petits singes* (`cinq-singes`) : compte à rebours de cinq à zéro,
  le docteur en médaillon au téléphone, pansements en croix, trampoline au
  jardin pour finir.
- *Grand, petit !* (`contraires`) : dix couples de contraires avec Panda et
  Noisette l'écureuil, chaque mot écrit près de qui le porte.
- *Rond, carré, triangle* (`formes-couleurs`) : formes et couleurs avec
  Pinceau le lapin ; mélanges de peinture exacts (jaune et bleu font du
  vert, rouge et jaune de l'orange, rouge et bleu du violet).

Plans variés (gros plans aux refrains, cadres resserrés dans les
répétitions), bulles hors zoom, objets tenus recalés sur les mains.

Contrôles : planches de toutes les pages des six livres revues dans
Chromium et corrigées ; coccinelle présente sur toutes les pages pleines,
vérifiée par `cachettes.py --verifier` ; régénération complète sans
changement des autres livres (`empreintes.txt` ne gagne que 75 lignes) ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors ligne
passe à `v30`.

## Ajout du 10 octobre 2026 : sept métiers

Le rayon Les métiers passe de dix à dix-sept livres, 88 nouvelles
illustrations :

- *Le camion de vidanges* (`camion-vidanges`) : Sami, éboueur ; camion à
  chargement arrière dont le lève-bac renverse le bac dans la trémie,
  compacteur en coupe, tri des bacs bleu, brun et noir, centre de tri,
  compost, travail à l'aube sous la neige.
- *Une journée à la bibliothèque* (`bibliothecaire`) : Monsieur Ali ; carte
  d'abonnée, cote au dos des livres, escabeau, heure du conte, lecteur de
  cartes, hôpital des livres, chute à livres éclairée le soir.
- *Maya, astronaute* (`astronaute-maya`) : piscine d'entraînement,
  décollage, station à 400 km qui fait le tour de la Terre en une heure et
  demie, apesanteur (boule d'eau, tortillas sans miettes, sac de couchage au
  mur, tapis à élastiques), sortie attachée, station vue de la Terre comme
  un point qui ne clignote pas, retour sous parachutes. Les pages dans
  l'espace et la piscine sont hors du jeu de la coccinelle.
- *La cheffe Rosalie* (`cheffe-cuisine`) : marché à l'aube, lavage des
  mains, brigade derrière le plan de travail, oignon qui pique les yeux,
  tarte, « Service ! », plonge.
- *L'autobus de Madame Nadia* (`autobus-nadia`) : vérifications au garage,
  borne de paiement, miroirs, autobus qui s'abaisse et rampe pour un
  passager en fauteuil roulant, place cédée, feu rouge sous la pluie,
  doudou rendu, lavage du soir.
- *Hugo, infirmier* (`infirmier-hugo`) : bras cassé ; bracelet,
  thermomètre et brassard, radio de l'avant-bras (un os fendu), plâtre
  violet, ronde de nuit, scie à plâtre qui vibre sans couper.
- *Le garage de Sofia* (`garage-sofia`) : crevaison, dépanneuse à
  plateau, pont élévateur, cric et clé, vidange, phares et clignotant, mur à
  outils, chaîne de vélo remise.

Contrôles : planches de toutes les pages des sept livres revues dans
Chromium et corrigées (personnages derrière les comptoirs, objets tenus,
bulles qui masquaient un visage) ; coccinelle présente sur toutes les pages
pleines hors espace, vérifiée par `cachettes.py --verifier` ; régénération
complète sans changement des autres livres (`empreintes.txt` ne gagne que
88 lignes) ; `verifier-images.py` sans erreur ; `node --test` réussi. Le
cache hors ligne reste à `v30` (même lot de publication que les comptines).

## Ajout du 10 octobre 2026 : sept fêtes

Le rayon Fêtes passe de quatorze à vingt et un livres, 87 nouvelles
illustrations (description du rayon mise à jour dans `catalogue.js`) :

- *Le temps des sucres* (`temps-sucres`) : érablière sans feuilles sur la
  neige, entaille, chalumeau et chaudière, traîneau à baril, cabane à
  lanterneau fumant, évaporateur (40 litres d'eau d'érable pour un litre
  de sirop), tire sur la neige, violon et danse ; tuques et ceinture
  fléchée dessinées dans le script.
- *Le dragon du Nouvel An* (`nouvel-an-lunaire`) : grand ménage, papiers
  découpés, raviolis, réveillon, enveloppe rouge, légende de Nian, danse du
  dragon et du lion, fête des lanternes à la pleine lune.
- *Les lumières de Diwali* (`diwali`) : rangoli, diyas, Rama et Sita,
  douceurs ; la nuit de la fête est sans lune (nouvelle lune).
- *Les huit lumières de Hanoukka* (`hanoukka`) : hanoukkia à huit branches
  et chamach surélevé, bougies placées de droite à gauche, chandelier du
  Temple à sept branches, latkes et beignets, toupie aux lettres
  hébraïques dessinées en tracés (pas de police nécessaire).
- *La lune de l'Aïd* (`aid-lune`) : jeûne des grands, datte et eau au
  coucher du soleil, premier croissant bas à l'ouest juste après le
  coucher, côté éclairé tourné vers la lueur du Soleil couché ; henné,
  don à la banque alimentaire, mosquée, douceurs ; le lendemain soir, le
  croissant est plus épais et plus haut.
- *Le Jour de la Terre* (`jour-terre`) : nettoyage du parc, tri, sac de
  plastique repêché, arbre planté, robinet fermé, vélo.
- *Les feux de la Saint-Jean* (`saint-jean`) : drapeaux bleus et blancs à
  fleurs de lys, défilé, violon et accordéon, horloge à 20 h 30 en plein
  jour (jours les plus longs), feu de joie derrière une barrière, feux
  d'artifice.

Contrôles : planches de toutes les pages des sept livres revues dans
Chromium et corrigées (dragon recadré, visages dégagés des bulles, objets
tenus) ; orientation des croissants vérifiée en grand ; coccinelle présente
sur toutes les pages pleines, vérifiée par `cachettes.py --verifier` (en
vol sur les pages de neige, que l'outil prend pour de l'eau) ; régénération
complète sans changement des autres livres (`empreintes.txt` ne gagne que
87 lignes) ; `verifier-images.py` sans erreur ; `node --test` réussi. Le
cache hors ligne reste à `v30` (même lot de publication).

## Ajout du 10 octobre 2026 : six documentaires animaliers

Six livres au rayon « Les animaux », tous à quatre pattes (ou nageoires,
ou élytres) dessinées dans leur script, sans personnage habillé :

- *Le grand voyage du monarque* (`monarque`) : œuf sous la feuille
  d'asclépiade, chenille rayée, chrysalide verte à points dorés, couleurs
  d'avertissement, migration jusqu'aux forêts du Mexique, retour en
  plusieurs générations.
- *Le castor bâtisseur* (`castor-batisseur`) : dents orange (le fer),
  arbre rongé en sablier, barrage, hutte en coupe avec l'entrée sous l'eau,
  coup de queue d'alerte, réserve de branches et étang gelé en surface.
- *L'orignal du marais* (`orignal`) : plantes aquatiques, jumeaux roux,
  bois en velours qui tombent au début de l'hiver, cloche sous la gorge,
  taille comparée à une grande personne, rameaux d'hiver.
- *Le voyage du saumon* (`voyage-saumon`) : œufs dans le gravier, alevins
  et leur réserve, tacon tacheté, saumoneau argenté, l'odeur de la
  rivière natale, chute vue de face, passe à poissons avec vitre, nid creusé
  à la queue ; le saumon atlantique peut retourner à la mer.
- *Le loup et sa meute* (`loup-meute`) : la meute est une famille, file
  indienne dans la neige, hurlement (pas pour la Lune), louveteaux nés les
  yeux fermés dans la tanière, grande sœur qui garde les petits, langage du
  corps (queue haute, oreilles couchées, révérence du jeu), chasse souvent
  ratée, sommeil en boule la queue sur le nez ; un loup timide.
- *La petite coccinelle* (`coccinelle`) : œufs jaunes près des pucerons,
  larve « petit crocodile », nymphe, adulte tout pâle puis rouge, élytres et
  ailes de vol, liquide amer, nombre de points selon l'espèce (pas l'âge),
  hivernage en groupe. La petite bête cachée y est une souris (`CACHE`).

Contrôles : planches de toutes les pages revues dans Chromium et corrigées
(chute d'eau redessinée de face, embouchure vue d'en haut, cous et queues
des loups, pattes et élytres de la coccinelle, échelles des insectes près
des personnages) ; petite bête présente sur toutes les pages pleines,
vérifiée par `cachettes.py --verifier` (petit poisson sous l'eau, souris
posée dans le livre de la coccinelle) ; régénération complète sans
changement des autres livres (`empreintes.txt` ne gagne que 81 lignes) ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors
ligne reste à `v30` (même lot de publication).

## Ajout du 10 octobre 2026 : huit petites histoires

Huit livres au rayon « Petites histoires », pour les grandes étapes et les
petits chagrins du quotidien :

- *Et moi, alors ?* (`leo-petite-soeur`) : la jalousie de Léo à l'arrivée
  de Rose ; bébé emmailloté, couffin, canapé où l'on s'assoit (dossier et
  assise dessinés de part et d'autre des personnages).
- *Au revoir, la couche !* (`lapinou-pot`) : Lapinou apprend le pot, avec
  un accident dédramatisé et une couche encore la nuit ; pot vu de face qui
  cache les jambes (assis), lavabo devant le personnage (vu « en miroir »).
- *Bulle, bulle, savon !* (`porcelet-mains`) : microbes rigolos sous la
  loupe, l'eau seule ne suffit pas, frotter partout le temps de deux
  « Joyeux anniversaire », quand se laver les mains, éternuer dans son coude.
- *Juste une petite bouchée* (`sami-legumes`) : semer, arroser, récolter,
  cuisiner, goûter ; le radis « pas encore » (les goûts changent).
- *Où est passé mon dinosaure ?* (`ines-range`) : chaque jouet a sa maison,
  ranger en chanson, Dino retrouvé sous le lit.
- *Mon amie Jade roule vite* (`jade-fauteuil`) : amitié avec une enfant en
  fauteuil roulant (demander avant d'aider, rampe, basket en fauteuil) ;
  fauteuil vu de face, assise plus basse que la hanche d'un enfant debout.
- *Ce n'est pas moi !* (`lila-pas-moi`) : accuser le chat, le dragon
  invisible, puis dire la vérité et réparer (autre angle que
  `renard-pot`, qui parle de cacher une bêtise).
- *Au revoir, Grisou* (`grisou-au-revoir`) : la mort d'un vieux chat, dite
  avec des mots vrais (« il est mort », « il ne reviendra pas »), sans
  culpabilité, un rosier planté, le droit de rire en se souvenant.

Nouveau dessin partagé : `chat_profil()` dans `objets.py` (chat de maison,
corps de profil et tête de face : assis, couché, en boule, qui marche),
utilisé par Lila et Grisou ; il ne change aucun autre livre.

Contrôles : planches de toutes les pages revues dans Chromium et corrigées
(échelle des personnages dans les intérieurs, adultes nettement plus grands
que les enfants, objets tenus hors des visages, personnages derrière les
tables et lavabos) ; petite bête présente sur toutes les pages pleines,
vérifiée par `cachettes.py --verifier` ; régénération complète sans
changement des autres livres (`empreintes.txt` ne gagne que 111 lignes) ;
`verifier-images.py` sans erreur ; `node --test` réussi. Le cache hors
ligne reste à `v30` (même lot de publication).

## Ajout du 10 octobre 2026 : huit contes

Huit livres au rayon « Contes traditionnels », adoucis pour les petits (la
patine des contes s'applique d'elle-même) :

- *La Belle au bois dormant* (`belle-bois-dormant`) : le sort adouci en cent
  ans de sommeil, le château endormi, les ronces fleuries ; le réveil comme
  chez Perrault (les cent ans finissent, sans baiser), et cette fois on
  invite la vieille fée.
- *Blanche-Neige* (`blanche-neige`) : le miroir, le chasseur au bon cœur,
  les sept nains (bonnets de couleur), la pomme ; le morceau de pomme
  tombe quand le prince la soulève (comme chez Grimm) ; la reine s'enfuit.
- *Le Stoïque Soldat de plomb* (`soldat-plomb`) : soldat et danseuse
  dessinés dans le script (vingt-quatre frères à deux jambes, lui à une
  seule), le rat, le poisson, la cuisine de la même maison ; ni feu ni
  fonte : un coup de vent pose la danseuse à côté de lui.
- *Pierre et le Loup* (`pierre-loup`) : page des instruments (flûte,
  hautbois, clarinette, basson, cors, timbales, violons) ; le canard se
  cache dans les roseaux au lieu d'être avalé ; le loup part au zoo.
- *Ti-Jean et les animaux* (`ti-jean-animaux`) : le conte des animaux
  reconnaissants à la manière des contes de Ti-Jean (tuque bleue, ceinture
  fléchée, forêt d'érables, sirop d'érable pour la dernière épreuve).
- *Momotaro, le garçon de la pêche* (`momotaro`) : kibi dango partagés,
  chien blanc, singe, faisan ; les oni demandent pardon, sans combat.
- *Anansi et la boîte à histoires* (`anansi-histoires`) : Nyamé en kente,
  les ruses d'Anansi sans blesser personne, les histoires qui s'envolent.
- *La légende du colibri* (`colibri-part`) : « Je fais ma part » ; dans
  cette version les autres animaux l'imitent, la pluie arrive, la forêt
  repousse ; dernière page : « Et toi, quelle est ta part ? ».

Contrôles : planches de toutes les pages revues dans Chromium et corrigées
(tuque qui ressemblait à un bonnet de Père Noël, corde du loup détournée
du visage, abeille posée sur les lèvres, princesse posée sur les petits
lits, oni sans bataille) ; petite bête présente sur toutes les pages
pleines, vérifiée par `cachettes.py --verifier` ; régénération complète
sans changement des autres livres (`empreintes.txt` ne gagne que 105
lignes) ; `verifier-images.py` sans erreur ; `node --test` réussi. Le cache
hors ligne reste à `v30` (même lot de publication).

## Ajout du 10 octobre 2026 : quatre fables

Quatre livres au rayon « Fables », chacun avec sa page de morale :

- *Le Vent et le Soleil* (`vent-soleil`), d'après Ésope et La Fontaine
  (« Phébus et Borée ») : le Vent en nuage aux joues gonflées, le Soleil
  souriant, le voyageur au manteau rouge ; « Plus fait douceur que
  violence ».
- *Le Chat, la Belette et le Petit Lapin* (`chat-belette-lapin`) : adoucie,
  Raminagrobis bondit mais les deux plaideurs s'échappent et deviennent
  voisins ; la belette est dessinée avec la silhouette du renard, en brun.
- *La Chauve-souris et les deux Belettes* (`chauve-souris-belettes`) :
  terrier éclairé pour que la chauve-souris brune se détache ; dernière
  page « Le savais-tu ? » : ni oiseau ni souris, un mammifère qui vole.
- *L'Alouette et ses Petits* (`alouette-petits`) : la même alouette que la
  comptine (dessin repris dans le script) ; « Ne t'attends qu'à toi seul ».

Le rayon dit désormais « Les fables de La Fontaine (et d'Ésope) ».

Contrôles : planches de toutes les pages revues dans Chromium et corrigées
(page de dispute remplie, texte dégagé du visage, manteau posé dans
l'herbe, contraste du terrier) ; petite bête présente sur toutes les pages
pleines, vérifiée par `cachettes.py --verifier` ; régénération complète
sans changement des autres livres (`empreintes.txt` ne gagne que 41
lignes) ; `verifier-images.py` sans erreur ; `node --test` réussi. Le cache
hors ligne reste à `v30` (même lot de publication).

## Rayon « Nouveautés » du 10 octobre 2026

Aucune illustration modifiée. L'accueil gagne un premier rayon
« ✨ Nouveautés » : les vingt livres ajoutés ou revus le plus récemment,
avec une pastille « Nouveau » ou « Revu » et la date
(`livres/nouveautes.js`, écrit par `outils/nouveautes.py` d'après
l'historique git). Le cache hors ligne passe à `v31` pour enregistrer ce
nouveau fichier.
