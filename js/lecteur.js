/* Lecteur : feuilleter un livre page par page (ou en double page sur grand écran). */
(async function () {
  "use strict";

  const scene = document.getElementById("scene");
  const position = document.getElementById("position");
  const precedent = document.getElementById("precedent");
  const suivant = document.getElementById("suivant");
  const boutonCopier = document.getElementById("copier-lien");
  const boutonVoix = document.getElementById("voix");
  const boutonFavori = document.getElementById("favori");

  const id = new URLSearchParams(location.search).get("livre") || (window.CATALOGUE || [])[0];

  let livre;
  try {
    livre = await Bibliotheque.charger(id);
  } catch (err) {
    scene.innerHTML = "";
    const p = document.createElement("p");
    p.className = "message message--erreur";
    p.textContent = err.message;
    scene.appendChild(p);
    precedent.disabled = suivant.disabled = true;
    boutonFavori.hidden = true;
    return;
  }

  // Cœur des favoris (gardé sur cet appareil, comme sur la page d'accueil).
  function montrerFavori() {
    const oui = Bibliotheque.estFavori(livre.id);
    boutonFavori.setAttribute("aria-pressed", String(oui));
    boutonFavori.firstChild.textContent = oui ? "❤️ " : "🤍 ";
  }
  boutonFavori.addEventListener("click", () => {
    Bibliotheque.changerFavori(livre.id, !Bibliotheque.estFavori(livre.id));
    montrerFavori();
  });
  montrerFavori();

  document.title = livre.titre;
  document.getElementById("titre").textContent = livre.titre;
  document.getElementById("imprimer").href = `imprimer.html?livre=${encodeURIComponent(livre.id)}`;
  // Le lien « Bibliothèque » ramène au rayon du livre.
  if (livre.rayon) document.querySelector(".entete__logo").href = `index.html#${encodeURIComponent(livre.rayon)}`;

  const navigation = NavigationLecture.installer({
    elements: { scene, position, precedent, suivant, boutonCopier },
    pages: livre.pages,
    adresse: `lire.html?livre=${encodeURIComponent(livre.id)}`,
    creerPage: (page, i) => Bibliotheque.creerPage(livre, page, i),
    cheminImage: (page) => Bibliotheque.cheminImage(livre, page.image),
    avantAffichage: () => arreterVoix(),
    apresAffichage: (derniereVue) => {
      if (derniereVue) Bibliotheque.changerLu(livre.id, true);
    },
  });
  const arreterVoix = LectureVoix.installer(boutonVoix, scene, livre, navigation.pagesCourantes);
  navigation.afficher();

  // Mettre tout ce livre en cache (service worker) pour le relire hors
  // ligne, quand le navigateur n'a rien de mieux à faire.
  const travailleur = navigator.serviceWorker && navigator.serviceWorker.controller;
  if (travailleur) {
    const fichiers = [...new Set(livre.pages.map((p) => p.image).filter(Boolean))].map((src) => Bibliotheque.cheminImage(livre, src));
    const envoyer = () => travailleur.postMessage({ type: "livre", fichiers });
    if ("requestIdleCallback" in window) requestIdleCallback(envoyer, { timeout: 3000 });
    else setTimeout(envoyer, 1000);
  }
})();
