Bibliotheque.ajouter({
  id: "max-ombre",
  titre: "Max et son ombre",
  sousTitre: "Une histoire sur la lumière",
  age: "3 à 6 ans",
  couleur: "#e67700",
  resume:
    "Une drôle de tache sombre suit Max le chiot partout où il va. " +
    "Elle grandit, rapetisse, change de côté… et disparaît même parfois !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Max le chiot et sa longue ombre sur l'herbe." },

    { type: "titre", image: "images/max-seul.svg", texte: "Pour les enfants qui jouent avec leur ombre." },

    {
      image: "images/01-decouverte.svg",
      description: "Max regarde, étonné, la tache sombre à ses pattes.",
      texte: "Ce matin, Max le chiot découvre une drôle de chose à ses pattes : une tache sombre qui le suit partout !",
    },
    {
      image: "images/02-saut.svg",
      description: "Max saute ; son ombre reste sur l'herbe, juste en dessous.",
      texte: "Max court : la tache court aussi. Max saute : la tache l'attend sur l'herbe.\n\nQui es-tu donc ?",
    },
    {
      image: "images/03-mistigri.svg",
      description: "Mistigri le chat, sur la clôture, regarde Max au soleil.",
      texte: "« C'est ton ombre, dit Mistigri le chat. Ton corps arrête la lumière du soleil. Derrière toi, il fait un peu noir. »",
    },
    {
      image: "images/04-matin.svg",
      description: "Tôt le matin, le soleil est bas et l'ombre de Max est très longue.",
      texte: "Le matin, le soleil est tout bas. L'ombre de Max est très, très longue. On dirait un grand chien !",
    },
    {
      image: "images/05-midi.svg",
      description: "À midi, le soleil est haut et l'ombre est toute petite sous Max.",
      texte: "À midi, le soleil est tout en haut du ciel. L'ombre devient toute petite, cachée sous les pattes de Max.",
    },
    {
      image: "images/06-soir.svg",
      description: "Le soir, le soleil se couche de l'autre côté et l'ombre s'allonge vers la gauche.",
      texte: "Le soir, le soleil se couche de l'autre côté. L'ombre s'allonge encore… mais de l'autre côté !",
    },
    {
      image: "images/07-nuage.svg",
      description: "Un gros nuage cache le soleil ; Max cherche son ombre.",
      texte: "Mais quand un gros nuage cache le soleil… plus d'ombre ! Max la cherche partout.",
    },
    {
      image: "images/08-lampe.svg",
      description: "Près d'une lampe, une grande ombre de Max apparaît sur le mur.",
      texte: "Le soir, près de la lampe, Max retrouve son ombre sur le mur, toute grande.\n\n« Bonne nuit, mon ombre ! »",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/max-seul.svg" },
  ],
});
