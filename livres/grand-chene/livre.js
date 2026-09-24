Bibliotheque.ajouter({
  id: "grand-chene",
  titre: "Les saisons de Grand Chêne",
  sousTitre: "Une année avec Noisette l'écureuil",
  age: "2 à 5 ans",
  couleur: "#d9480f",
  resume:
    "Au printemps, en été, en automne et en hiver, Grand Chêne change de couleur. " +
    "Noisette l'écureuil, lui, ne le quitte jamais !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un grand chêne, moitié vert, moitié orange, et un écureuil." },

    { type: "titre", image: "images/ecureuil-seul.svg", texte: "Pour tous ceux qui aiment grimper aux arbres." },

    {
      image: "images/01-printemps.svg",
      description: "Au printemps, le chêne a de petites feuilles et une mésange bâtit son nid.",
      texte: "Au printemps, Grand Chêne se réveille. De petites feuilles vertes poussent, et une mésange y construit son nid.",
    },
    {
      image: "images/02-oisillons.svg",
      description: "Trois oisillons dans le nid avec leur maman.",
      texte: "Bientôt, trois oisillons sortent de leurs œufs.\n\nPiou ! Piou ! Ils ont très faim !",
    },
    {
      image: "images/03-ete.svg",
      description: "En été, l'écureuil dort à l'ombre du chêne.",
      texte: "En été, Grand Chêne est tout touffu. Noisette l'écureuil fait la sieste à son ombre.",
    },
    {
      image: "images/04-glands.svg",
      description: "Noisette tient un gland sur une branche.",
      texte: "Des glands poussent sur les branches. Noisette en ramasse plein pour faire des provisions.",
    },
    {
      image: "images/05-automne.svg",
      disposition: "image-bas",
      description: "En automne, les feuilles orange et rouges tombent.",
      texte: "En automne, les feuilles deviennent jaunes, orange et rouges… puis elles tombent en tourbillonnant.",
    },
    {
      image: "images/06-tas-de-feuilles.svg",
      description: "Noisette saute dans un tas de feuilles.",
      texte: "Hop ! Noisette saute dans le tas de feuilles. Quelle bonne cachette !",
    },
    {
      image: "images/07-hiver.svg",
      disposition: "pleine-page",
      positionTexte: "haut",
      description: "En hiver, l'arbre est tout nu sous la neige ; l'écureuil dort dans son trou.",
      texte: "En hiver, Grand Chêne est tout nu sous la neige. Il dort… et Noisette aussi, bien au chaud.",
    },
    {
      image: "images/08-bourgeon.svg",
      description: "Le soleil fait ouvrir un bourgeon ; Noisette le regarde.",
      texte: "Puis un matin, le soleil réchauffe les branches. Un bourgeon s'ouvre : le printemps est revenu !",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/ecureuil-seul.svg" },
  ],
});
