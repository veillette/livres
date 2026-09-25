Bibliotheque.ajouter({
  id: "chapeau-vent",
  titre: "Le chapeau de Monsieur Ours",
  sousTitre: "Une histoire qui s'envole",
  age: "2 à 5 ans",
  couleur: "#c2255c",
  resume:
    "Monsieur Ours adore son chapeau rouge. Mais fiouuu ! le vent l'emporte ! Il " +
    "devient le chapeau de Mouton, le bateau de Grenouille, le toit d'Escargot… " +
    "et pour finir, le plus beau des nids. Et si le plus grand bonheur, c'était " +
    "de donner ce qu'on aime ?",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Monsieur Ours lève les bras : le vent emporte son chapeau rouge." },

    { type: "titre", image: "images/ours-seul.svg", texte: "Pour ceux qui ont déjà couru après un chapeau." },

    {
      image: "images/01-le-chapeau.svg",
      description: "Monsieur Ours lit un livre sur un banc, coiffé de son chapeau rouge.",
      texte: "Monsieur Ours adore son chapeau rouge. Il le porte pour se promener, pour lire au parc… et même pour faire la sieste !",
    },
    {
      image: "images/02-fiouuu.svg",
      description: "Le vent souffle et emporte le chapeau ; Monsieur Ours lève les bras.",
      texte: "Mais un jour, fiouuu ! Le vent l'emporte.\n\n« Mon chapeau ! Reviens ! »",
    },
    {
      image: "images/03-mouton.svg",
      description: "Le chapeau rouge est tombé sur la tête de Mouton, qui prend la pose.",
      texte: "Le chapeau atterrit sur la tête de Mouton.\n\n« Oh, un chapeau ! Il me va très bien, non ? »\n\nEt fiouuu, il repart !",
    },
    {
      image: "images/04-bateau.svg",
      description: "Retourné sur la mare, le chapeau sert de bateau à Grenouille.",
      texte: "Il tombe dans la mare, tout à l'envers. Grenouille saute dedans.\n\n« Quel joli bateau ! »\n\nEt fiouuu, il repart !",
    },
    {
      image: "images/05-escargot.svg",
      description: "Le chapeau s'est posé sur la coquille d'Escargot, qui rit.",
      texte: "Il se pose sur la coquille d'Escargot.\n\n« Une maison sur ma maison ! »\n\nEt fiouuu, il repart !",
    },
    {
      image: "images/06-le-nid.svg",
      description: "Le chapeau, coincé dans un arbre, contient trois œufs ; Maman Oiseau est ravie.",
      texte: "Enfin, il se coince dans les branches d'un arbre. Maman Oiseau y pond trois petits œufs.\n\n« Le nid parfait ! »",
    },
    {
      image: "images/07-les-oeufs.svg",
      description: "Monsieur Ours, essoufflé, regarde le nid perché dans l'arbre.",
      texte: "Monsieur Ours arrive, tout essoufflé. Il voit les trois œufs, bien au chaud dans son chapeau…\n\n« Garde-le, Maman Oiseau. »",
    },
    {
      image: "images/08-printemps.svg",
      description: "Au printemps, trois poussins chantent dans le chapeau ; Monsieur Ours leur fait coucou.",
      texte: "Au printemps, trois poussins chantent dans le chapeau.\n\nMonsieur Ours n'a plus de chapeau… mais il a trois amis !",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/ours-seul.svg" },
  ],
});
