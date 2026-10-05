/*
 * Page d'accueil : les couvertures du catalogue, rangées par rayon.
 *
 * Les boutons du haut affichent un seul rayon ou tous ; le choix est gardé
 * dans l'adresse (index.html#fables) pour que le bouton « retour » du
 * navigateur et les liens « Bibliothèque » y ramènent.
 */
(async function () {
  "use strict";

  const etageres = document.getElementById("etageres");
  const filtres = document.getElementById("rayons");

  function carte(livre) {
    const article = document.createElement("article");
    article.className = "carte";

    const lien = document.createElement("a");
    lien.className = "carte__couverture";
    lien.href = `lire.html?livre=${encodeURIComponent(livre.id)}`;
    lien.setAttribute("aria-label", `Lire « ${livre.titre} »`);
    lien.appendChild(Bibliotheque.creerPage(livre, livre.pages[0], 0));
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
    return [...rayons, autres].filter((r) => r.livres.length > 0);
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
    nombre.textContent = `${rayon.livres.length} livre${rayon.livres.length > 1 ? "s" : ""}`;
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
    rayon.livres.forEach((livre) => grille.appendChild(carte(livre)));
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
  etageres.replaceChildren();

  if (livres.length === 0) {
    etageres.innerHTML = '<p class="message">Aucun livre pour le moment. Ajoute un dossier dans <code>livres/</code> et inscris-le dans <code>livres/catalogue.js</code>.</p>';
    return;
  }

  const rayons = ranger(livres);
  rayons.forEach((r) => etageres.appendChild(section(r)));

  if (rayons.length > 1) {
    filtres.appendChild(bouton("tous", "Tous les livres", livres.length));
    rayons.forEach((r) => filtres.appendChild(bouton(r.id, `<span aria-hidden="true">${r.icone}</span> ${r.nom}`, r.livres.length)));
    filtres.hidden = false;
  }

  function afficher() {
    const voulu = decodeURIComponent(location.hash.slice(1));
    const choisi = rayons.some((r) => r.id === voulu) ? voulu : "tous";
    for (const el of etageres.children) el.hidden = choisi !== "tous" && el.dataset.rayon !== choisi;
    for (const b of filtres.children) b.setAttribute("aria-pressed", String(b.dataset.rayon === choisi));
    // Sur téléphone, la rangée de rayons défile : montrer le rayon choisi.
    const actif = filtres.querySelector('[aria-pressed="true"]');
    if (actif) filtres.scrollLeft = actif.offsetLeft - filtres.offsetLeft - (filtres.clientWidth - actif.offsetWidth) / 2;
  }

  window.addEventListener("hashchange", afficher);
  afficher();
})();
