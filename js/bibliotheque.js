/* Page d'accueil : affiche la couverture de chaque livre du catalogue. */
(async function () {
  "use strict";

  const etageres = document.getElementById("etageres");

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

    const titre = document.createElement("h2");
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

  const livres = await Bibliotheque.chargerTout();
  etageres.replaceChildren();

  if (livres.length === 0) {
    etageres.innerHTML = '<p class="message">Aucun livre pour le moment. Ajoute un dossier dans <code>livres/</code> et inscris-le dans <code>livres/catalogue.js</code>.</p>';
    return;
  }

  livres.forEach((livre) => etageres.appendChild(carte(livre)));
})();
