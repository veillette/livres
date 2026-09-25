Bibliotheque.ajouter({
  id: "hibou-lune",
  titre: "Petit Hibou et la Lune",
  sousTitre: "Une histoire sur les phases de la Lune",
  age: "3 à 6 ans",
  couleur: "#5f3dc4",
  resume:
    "Nuit après nuit, la Lune de Petit Hibou devient de plus en plus mince… " +
    "puis elle disparaît ! Qui a bien pu la croquer ? Une histoire pour apprendre " +
    "à attendre, même quand on a un peu peur.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un petit hibou sur une branche devant une grosse lune ronde." },

    { type: "titre", image: "images/hibou-seul.svg", texte: "Pour les petits curieux qui se couchent tard." },

    {
      image: "images/01-pleine-lune.svg",
      description: "Petit Hibou sur sa branche, sous la pleine lune.",
      texte: "Chaque soir, Petit Hibou ouvrait ses grands yeux ronds pour dire bonsoir à la Lune.\n\nCe soir-là, elle était toute ronde.",
    },
    {
      image: "images/02-gibbeuse.svg",
      description: "Il manque un petit morceau à la Lune.",
      texte: "Mais quelques nuits plus tard, il manquait un morceau.\n\n« Qui a croqué la Lune ? » demanda Petit Hibou.",
    },
    {
      image: "images/03-quartier.svg",
      description: "Une demi-lune et une chauve-souris.",
      texte: "Bientôt, il n'en restait que la moitié.\n\n« Est-ce toi qui l'as mangée ? » demanda-t-il à Chauve-Souris. « Mais non ! » rit-elle.",
    },
    {
      image: "images/04-croissant.svg",
      description: "Un mince croissant de lune ; Petit Hibou a l'air inquiet.",
      texte: "Puis ce ne fut plus qu'un tout petit croissant. Petit Hibou était bien inquiet.",
    },
    {
      image: "images/05-nouvelle-lune.svg",
      disposition: "pleine-page",
      description: "La nuit est toute noire, on ne voit plus la Lune.",
      texte: "Une nuit, la Lune avait disparu ! Il faisait tout noir, et Petit Hibou avait un peu peur.",
    },
    {
      image: "images/06-grand-maman.svg",
      description: "Grand-Maman Chouette explique que le Soleil éclaire la Lune.",
      texte: "« La Lune ne s'en va jamais, dit Grand-Maman Chouette. Le Soleil l'éclaire, et nous n'en voyons qu'une partie. Patience ! »",
    },
    {
      image: "images/07-croissant-revient.svg",
      description: "Un croissant, une demi-lune, puis une lune presque pleine.",
      texte: "Petit Hibou attendit, sans fermer l'œil. Et le lendemain, un fin croissant réapparut ! Nuit après nuit, la Lune grandit, grandit…",
    },
    {
      image: "images/08-retour.svg",
      description: "Petit Hibou, tout content, sous la pleine lune revenue.",
      texte: "… jusqu'à redevenir toute ronde. « Bonsoir, Lune ! » cria Petit Hibou, tout content.",
    },

    { type: "texte", texte: "Fin" },

    { type: "quatrieme", image: "images/hibou-seul.svg" },
  ],
});
