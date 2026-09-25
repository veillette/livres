Bibliotheque.ajouter({
  id: "chat-tache",
  titre: "Oups, une tache !",
  sousTitre: "Une histoire sur les erreurs",
  age: "3 à 6 ans",
  couleur: "#1864ab",
  resume:
    "Zou le chaton peint un beau soleil pour l'anniversaire de Mamie… SPLATCH ! " +
    "Le pot de peinture bleue se renverse. « C'est raté ! » Mais Papa, lui, voit un " +
    "nuage dans la tache. Et toi, qu'est-ce que tu vois ? Parfois, un oups devient " +
    "une idée.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Zou le chaton, pinceau à la main, rit devant un dessin de baleine bleue." },

    { type: "titre", image: "images/zou-seul.svg", texte: "Pour les artistes qui débordent (un peu)." },

    {
      image: "images/01-le-dessin.svg",
      description: "Devant son chevalet, Zou peint un soleil souriant en tirant la langue.",
      texte: "Zou le chaton peint un soleil pour l'anniversaire de Mamie. Il s'applique très fort. Il tire même un bout de langue !",
    },
    {
      image: "images/02-splatch.svg",
      description: "Le pot de peinture bleue s'est renversé ; une grosse tache bleue couvre le dessin.",
      texte: "Oh non ! Son coude cogne le pot de peinture bleue.\n\nSPLATCH ! Une énorme tache sur le dessin.",
    },
    {
      image: "images/03-rate.svg",
      description: "Zou pleure ; la feuille froissée en boule est par terre.",
      texte: "« C'est raté ! Tout est gâché ! »\n\nZou froisse la feuille en boule et se met à pleurer.",
    },
    {
      image: "images/04-un-nuage.svg",
      description: "Papa déplie la feuille froissée et la montre à Zou.",
      texte: "Papa ramasse la boule et la déplie doucement.\n\n« Hmm… Moi, je vois un nuage. Et toi ? Qu'est-ce que tu vois ? »",
    },
    {
      image: "images/05-baleine.svg",
      description: "Avec quelques coups de pinceau, la tache bleue est devenue une baleine qui crache de l'eau.",
      texte: "Zou regarde bien. La tache ressemble… à une baleine ! Il lui dessine un œil, un sourire et un grand jet d'eau.",
    },
    {
      image: "images/06-la-mer.svg",
      description: "Le dessin est devenu une mer avec des vagues, la baleine et des poissons de couleur.",
      texte: "Et cette petite goutte ? Un poisson ! Et ce pli dans la feuille ? Une vague !\n\nLe soleil brille sur une mer toute pleine de vie.",
    },
    {
      image: "images/07-oups-idee.svg",
      description: "Zou, les bras en l'air, entouré de taches de toutes les couleurs.",
      texte: "Maintenant, Zou n'a plus peur des taches. Un oups, ce n'est pas la fin du dessin.\n\nC'est peut-être le début d'une idée !",
    },
    {
      image: "images/08-anniversaire.svg",
      description: "Le dessin de la mer est encadré au mur ; Mamie est ravie et Zou est fier.",
      texte: "Mamie accroche le dessin au mur, dans un joli cadre.\n\n« C'est la plus belle mer que j'aie jamais vue ! »",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/zou-seul.svg" },
  ],
});
