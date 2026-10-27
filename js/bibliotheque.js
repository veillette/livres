/*
 * Page d'accueil : les couvertures du catalogue, rangées par rayon.
 *
 * Les boutons du haut affichent un seul rayon ou tous ; le choix est gardé
 * dans l'adresse (index.html#fables) pour que le bouton « retour » du
 * navigateur et les liens « Bibliothèque » y ramènent.
 *
 * Le premier rayon, « Nouveautés », reprend les livres ajoutés ou revus le
 * plus récemment (`livres/nouveautes.js`, écrit par `outils/nouveautes.py`).
 * Vient ensuite « Mes favoris », les livres marqués d'un cœur sur cet
 * appareil.
 *
 * Au-dessus des rayons, on cherche un livre par mot (titre, sous-titre,
 * résumé, auteur, rayon), par âge de l'enfant, ou parmi les livres déjà lus
 * (ou pas encore) : le lecteur marque un livre « lu » à sa dernière page.
 */
(async function () {
  "use strict";

  const etageres = document.getElementById("etageres");
  const filtres = document.getElementById("rayons");
  const recherche = document.getElementById("recherche");
  const champMots = document.getElementById("mots");
  const choixAge = document.getElementById("age");
  const choixLecture = document.getElementById("lecture");
  const resultat = document.getElementById("resultat");

  const moisCourts = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];

  /* « 10 oct. 2026 » à partir de « 2026-10-10 ». */
  function dateCourte(iso) {
    const [annee, mois, jour] = iso.split("-").map(Number);
    return `${jour === 1 ? "1er" : jour} ${moisCourts[mois - 1]} ${annee}`;
  }

  /* Minuscules sans accents : « Noël » et « noel » se retrouvent. */
  function normaliser(texte) {
    return String(texte || "")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/œ/g, "oe")
      .replace(/æ/g, "ae")
      .replace(/[’ʼ]/g, "'")
      .toLowerCase();
  }

  const nombreDeLivres = (n) => `${n} livre${n > 1 ? "s" : ""}`;

  function carte(livre, nouveaute) {
    const article = document.createElement("article");
    article.className = "carte";
    article.dataset.livre = livre.id;

    if (nouveaute) {
      const pastille = document.createElement("p");
      pastille.className = `carte__pastille carte__pastille--${nouveaute.etat}`;
      pastille.textContent = `${nouveaute.etat === "nouveau" ? "Nouveau" : "Revu"} · ${dateCourte(nouveaute.date)}`;
      article.appendChild(pastille);
    }

    const coeur = document.createElement("button");
    coeur.type = "button";
    coeur.className = "carte__favori";
    coeur.dataset.favori = livre.id;
    coeur.setAttribute("aria-label", `Mettre « ${livre.titre} » dans mes favoris`);
    coeur.addEventListener("click", () => {
      Bibliotheque.changerFavori(livre.id, !Bibliotheque.estFavori(livre.id));
      rafraichir();
    });
    article.appendChild(coeur);

    const lien = document.createElement("a");
    lien.className = "carte__couverture";
    lien.href = `lire.html?livre=${encodeURIComponent(livre.id)}`;
    lien.setAttribute("aria-label", `Lire « ${livre.titre} »`);
    lien.appendChild(Bibliotheque.creerPage(livre, livre.pages[0], 0, { paresseux: true }));
    article.appendChild(lien);

    const corps = document.createElement("div");
    corps.className = "carte__corps";

    const titre = document.createElement("h3");
    titre.textContent = livre.titre;
    corps.appendChild(titre);

    const meta = document.createElement("p");
    meta.className = "carte__meta";
    meta.textContent = [livre.auteur, livre.age, `${livre.pages.length} pages`].filter(Boolean).join(" · ");
    corps.appendChild(meta);

    const lu = document.createElement("p");
    lu.className = "carte__lu";
    lu.textContent = "✓ Déjà lu";
    corps.appendChild(lu);

    const actions = document.createElement("div");
    actions.className = "carte__actions";
    actions.innerHTML = `
      <a class="bouton" href="lire.html?livre=${encodeURIComponent(livre.id)}">📖 Lire</a>
      <a class="bouton bouton--secondaire" href="imprimer.html?livre=${encodeURIComponent(livre.id)}">🖨️ Imprimer</a>`;
    corps.appendChild(actions);

    article.appendChild(corps);
    return article;
  }

  /* Range les livres par rayon, dans l'ordre de RAYONS puis du catalogue. */
  function ranger(livres) {
    const rayons = (window.RAYONS || []).map((r) => ({ ...r, livres: [] }));
    const autres = { id: "autres", nom: "Autres livres", icone: "📚", livres: [] };
    const parId = new Map(rayons.map((r) => [r.id, r]));
    livres.forEach((livre) => (parId.get(livre.rayon) || autres).livres.push(livre));
    const recents = (window.NOUVEAUTES || []).filter((n) => parLivre.has(n.id));
    const nouveautes = {
      id: "nouveautes",
      nom: "Nouveautés",
      icone: "✨",
      description: "Les derniers livres ajoutés ou revus dans la bibliothèque, du plus récent au plus ancien.",
      livres: recents.map((n) => parLivre.get(n.id)),
      nouveautes: recents,
    };
    return [nouveautes, ...rayons, autres].filter((r) => r.livres.length > 0);
  }

  /* Le rayon « Mes favoris », dans l'ordre du catalogue. */
  function rayonFavoris() {
    const favoris = Bibliotheque.favoris();
    return {
      id: "favoris",
      nom: "Mes favoris",
      icone: "❤️",
      description: "Les livres marqués d'un cœur. Ils restent sur cet appareil.",
      livres: livres.filter((l) => favoris.has(l.id)),
    };
  }

  function section(rayon) {
    const el = document.createElement("section");
    el.className = "rayon";
    el.dataset.rayon = rayon.id;
    el.setAttribute("aria-labelledby", `rayon-${rayon.id}`);

    const entete = document.createElement("header");
    entete.className = "rayon__entete";
    const titre = document.createElement("h2");
    titre.id = `rayon-${rayon.id}`;
    titre.innerHTML = `<span aria-hidden="true">${rayon.icone}</span> `;
    titre.append(rayon.nom);
    const nombre = document.createElement("span");
    nombre.className = "rayon__nombre";
    nombre.textContent = nombreDeLivres(rayon.livres.length);
    titre.append(" ", nombre);
    entete.appendChild(titre);
    if (rayon.description) {
      const p = document.createElement("p");
      p.textContent = rayon.description;
      entete.appendChild(p);
    }
    el.appendChild(entete);

    const grille = document.createElement("div");
    grille.className = "rayon__livres";
    rayon.livres.forEach((livre, i) => grille.appendChild(carte(livre, rayon.nouveautes && rayon.nouveautes[i])));
    el.appendChild(grille);
    return el;
  }

  function bouton(id, texte, nombre) {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "filtre";
    b.dataset.rayon = id;
    b.innerHTML = `${texte} <span class="filtre__nombre">${nombre}</span>`;
    b.addEventListener("click", () => {
      // Remplacer l'adresse sans ajouter d'entrée à l'historique à chaque clic.
      history.replaceState(null, "", id === "tous" ? location.pathname + location.search : `#${id}`);
      afficher();
    });
    return b;
  }

  const livres = await Bibliotheque.chargerTout();
  const parLivre = new Map(livres.map((l) => [l.id, l]));
  etageres.replaceChildren();

  if (livres.length === 0) {
    etageres.innerHTML = '<p class="message">Aucun livre pour le moment. Ajoute un dossier dans <code>livres/</code> et inscris-le dans <code>livres/catalogue.js</code>.</p>';
    return;
  }

  // Texte où chercher, pour chaque livre.
  const nomsRayons = new Map((window.RAYONS || []).map((r) => [r.id, r.nom]));
  const index = new Map(
    livres.map((l) => [l.id, normaliser([l.titre, l.sousTitre, l.resume, l.auteur, nomsRayons.get(l.rayon)].join(" "))])
  );

  const rayons = ranger(livres);
  let favoris = rayonFavoris();

  /* Rayons dans l'ordre d'affichage : Nouveautés, Mes favoris, puis les autres. */
  const tousLesRayons = () => {
    const liste = favoris.livres.length > 0 ? [favoris] : [];
    return rayons[0].id === "nouveautes" ? [rayons[0], ...liste, ...rayons.slice(1)] : [...liste, ...rayons];
  };

  function construire() {
    etageres.replaceChildren(...tousLesRayons().map(section));
    filtres.replaceChildren();
    if (tousLesRayons().length > 1) {
      filtres.appendChild(bouton("tous", "Tous les livres", livres.length));
      tousLesRayons().forEach((r) => filtres.appendChild(bouton(r.id, `<span aria-hidden="true">${r.icone}</span> ${r.nom}`, r.livres.length)));
      filtres.hidden = false;
    }
  }

  /* Cœurs et marques « déjà lu » d'après ce que garde le navigateur. */
  function marquer() {
    const coeurs = Bibliotheque.favoris();
    const lus = Bibliotheque.lus();
    for (const b of etageres.querySelectorAll(".carte__favori")) {
      const oui = coeurs.has(b.dataset.favori);
      b.setAttribute("aria-pressed", String(oui));
      b.textContent = oui ? "❤️" : "🤍";
    }
    for (const c of etageres.querySelectorAll(".carte")) c.classList.toggle("carte--lue", lus.has(c.dataset.livre));
  }

  /* Après un changement de favori ou de lecture (ici, dans un autre onglet
     ou au retour du lecteur) : refaire le rayon des favoris si besoin. */
  function rafraichir() {
    const avant = favoris.livres.map((l) => l.id).join();
    favoris = rayonFavoris();
    if (favoris.livres.map((l) => l.id).join() !== avant) {
      const defilement = window.scrollY;
      construire();
      window.scrollTo(0, defilement);
    }
    marquer();
    afficher();
  }

  function convient(livre, mots, age, lecture, lus) {
    if (age) {
      const tranche = Bibliotheque.tranchesAge(livre);
      if (tranche && (age < tranche[0] || age > tranche[1])) return false;
    }
    if (lecture && lus.has(livre.id) !== (lecture === "oui")) return false;
    const texte = index.get(livre.id);
    return mots.every((m) => texte.includes(m));
  }

  function afficher() {
    const voulu = decodeURIComponent(location.hash.slice(1));
    const choisi = tousLesRayons().some((r) => r.id === voulu) ? voulu : "tous";

    // « loups » trouve « loup » : on enlève le s ou le x final des mots cherchés.
    const mots = normaliser(champMots.value)
      .split(/[\s,;.!?'-]+/)
      .filter(Boolean)
      .map((m) => (m.length > 3 ? m.replace(/[sx]$/, "") : m));
    const age = Number(choixAge.value) || null;
    const lecture = choixLecture.value;
    const lus = Bibliotheque.lus();
    const filtre = mots.length > 0 || age != null || lecture !== "";

    const trouves = new Set();
    for (const el of etageres.children) {
      const rayon = el.dataset.rayon;
      // En cherchant dans tous les rayons, Nouveautés et Mes favoris
      // répéteraient des livres déjà montrés dans leur rayon.
      const montre = choisi === "tous" ? !(filtre && (rayon === "nouveautes" || rayon === "favoris")) : rayon === choisi;
      let n = 0;
      for (const c of el.querySelectorAll(".carte")) {
        const oui = convient(parLivre.get(c.dataset.livre), mots, age, lecture, lus);
        c.hidden = !oui;
        if (oui) {
          n += 1;
          if (montre) trouves.add(c.dataset.livre);
        }
      }
      el.querySelector(".rayon__nombre").textContent = nombreDeLivres(n);
      el.hidden = !montre || n === 0;
    }

    resultat.hidden = !filtre;
    resultat.textContent =
      trouves.size === 0
        ? "Aucun livre ne correspond. Essaie un autre mot ou un autre âge !"
        : `${nombreDeLivres(trouves.size)} trouvé${trouves.size > 1 ? "s" : ""}.`;

    for (const b of filtres.children) b.setAttribute("aria-pressed", String(b.dataset.rayon === choisi));
    // Sur téléphone, la rangée de rayons défile : montrer le rayon choisi.
    const actif = filtres.querySelector('[aria-pressed="true"]');
    if (actif) filtres.scrollLeft = actif.offsetLeft - filtres.offsetLeft - (filtres.clientWidth - actif.offsetWidth) / 2;
  }

  // L'âge choisi est gardé pour la prochaine visite (pratique, pas essentiel).
  try {
    choixAge.value = localStorage.getItem("livres:age") || "";
  } catch {
    /* stockage indisponible */
  }
  choixAge.addEventListener("change", () => {
    try {
      localStorage.setItem("livres:age", choixAge.value);
    } catch {
      /* stockage indisponible */
    }
    afficher();
  });
  champMots.addEventListener("input", afficher);
  choixLecture.addEventListener("change", afficher);
  recherche.addEventListener("submit", (e) => {
    e.preventDefault();
    champMots.blur(); // ferme le clavier du téléphone
  });
  recherche.hidden = false;

  construire();
  marquer();
  window.addEventListener("hashchange", afficher);
  // Favoris ou lectures changés dans un autre onglet, ou retour du lecteur
  // par le bouton « précédent » (page restaurée telle quelle).
  window.addEventListener("storage", rafraichir);
  window.addEventListener("pageshow", (e) => e.persisted && rafraichir());
  afficher();
})();
