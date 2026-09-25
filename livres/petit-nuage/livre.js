Bibliotheque.ajouter({
  id: "petit-nuage",
  titre: "Le voyage de Petit Nuage",
  sousTitre: "Une histoire sur le cycle de l'eau",
  age: "3 à 6 ans",
  couleur: "#3a7bd5",
  resume:
    "Petit Nuage est curieux. Porté par le vent, il survole les montagnes et la mer, " +
    "se gonfle de gouttes d'eau… puis les offre à un jardin qui avait bien soif.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un petit nuage souriant devant un arc-en-ciel." },

    { type: "titre", image: "images/nuage-seul.svg", texte: "Pour tous les enfants qui regardent le ciel." },

    {
      image: "images/01-ciel.svg",
      description: "Petit Nuage flotte dans le ciel bleu, au-dessus des collines.",
      texte: "Tout là-haut, dans le grand ciel bleu, vivait Petit Nuage. Il était blanc, tout doux… et très curieux.",
    },
    {
      image: "images/02-vent.svg",
      description: "Le vent souffle et fait danser les arbres.",
      texte: "Un matin, le vent se mit à souffler.\n\n« Viens avec moi, Petit Nuage ! Je vais te montrer le monde. »",
    },
    {
      image: "images/03-montagnes.svg",
      disposition: "image-bas",
      description: "Petit Nuage passe au-dessus des montagnes enneigées.",
      texte: "Ils passèrent au-dessus des hautes montagnes, toutes coiffées de neige.",
    },
    {
      image: "images/04-mer.svg",
      description: "Une baleine fait un jet d'eau sous Petit Nuage.",
      texte: "Puis au-dessus de la grande mer, où une baleine s'amusait à faire des jets d'eau.",
    },
    {
      image: "images/05-nuage-gris.svg",
      description: "Des gouttes montent de la mer vers le nuage devenu gris.",
      texte: "Le soleil chauffait la mer. De minuscules gouttes montaient vers Petit Nuage, qui devint gris… et très lourd !",
    },
    {
      image: "images/06-pluie.svg",
      description: "Il pleut sur un jardin de fleurs.",
      texte: "Plic ! Ploc ! Petit Nuage fit pleuvoir sur un jardin qui avait très soif.",
    },
    {
      image: "images/07-arc-en-ciel.svg",
      description: "Un grand arc-en-ciel au-dessus des fleurs.",
      texte: "Quand le soleil revint, un grand arc-en-ciel apparut.\n\n« Merci, Petit Nuage ! » chantèrent les fleurs.",
    },
    {
      image: "images/08-nuit.svg",
      disposition: "pleine-page",
      description: "Petit Nuage dort sous la lune et les étoiles.",
      texte: "Le soir venu, léger et heureux, Petit Nuage s'endormit sous les étoiles.",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/nuage-seul.svg" },
  ],
});
