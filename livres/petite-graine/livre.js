Bibliotheque.ajouter({
  id: "petite-graine",
  titre: "La petite graine",
  sousTitre: "Une histoire de patience",
  age: "2 à 5 ans",
  couleur: "#2b8a3e",
  resume:
    "Sous la terre dort une petite graine. Elle voudrait devenir une fleur tout " +
    "de suite ! Mais une fleur, ça ne pousse pas en un jour… Avec un peu de pluie, " +
    "beaucoup de soleil et encore plus de patience, elle va devenir une fleur géante !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un tournesol qui sort de terre, avec sa graine et ses racines." },

    { type: "titre", image: "images/graine-seule.svg", texte: "Pour les jardiniers, petits et grands." },

    {
      image: "images/01-sous-terre.svg",
      description: "Une graine endormie sous la terre, à côté d'un ver de terre.",
      texte: "Au fond de la terre dormait une petite graine. « Quand est-ce que je deviens une fleur ? »\n\n« Patience ! » dit le ver de terre.",
    },
    {
      image: "images/02-pluie.svg",
      description: "Il pleut ; l'eau descend jusqu'à la graine.",
      texte: "Un jour, la pluie vint la réveiller. Glou, glou ! La petite graine but l'eau fraîche.",
    },
    {
      image: "images/03-racine.svg",
      description: "Des racines poussent sous la graine.",
      texte: "La petite graine ne se pressa pas. D'abord, elle fit pousser des racines vers le bas, pour boire et pour bien se tenir.",
    },
    {
      image: "images/04-tige.svg",
      description: "Une petite tige sort de terre vers le soleil.",
      texte: "Puis une petite tige vers le haut… vers la lumière du soleil !",
    },
    {
      image: "images/05-feuilles.svg",
      description: "Une grande tige avec beaucoup de feuilles.",
      texte: "Jour après jour, tout doucement, elle grandit. Deux feuilles, quatre feuilles, six feuilles !\n\nPas besoin de se dépêcher.",
    },
    {
      image: "images/06-fleur.svg",
      description: "Un grand tournesol souriant.",
      texte: "Un matin, après tant d'attente, un bouton s'ouvrit : c'était un tournesol, plus grand que toi !\n\nÇa valait la peine d'attendre.",
    },
    {
      image: "images/07-abeille.svg",
      description: "Une abeille vient butiner le tournesol.",
      texte: "Une abeille vint lui rendre visite.\n\n« Bzzz ! Merci pour le nectar ! »",
    },
    {
      image: "images/08-vent.svg",
      description: "Les graines du tournesol tombent sur la terre.",
      texte: "À la fin de l'été, ses graines tombèrent sur la terre… pour y dormir à leur tour jusqu'au printemps.\n\nPatience, petites graines !",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/graine-seule.svg" },
  ],
});
