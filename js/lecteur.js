/* Lecteur : feuilleter un livre page par page (ou en double page sur grand écran). */
(async function () {
  "use strict";

  const scene = document.getElementById("scene");
  const position = document.getElementById("position");
  const precedent = document.getElementById("precedent");
  const suivant = document.getElementById("suivant");
  const boutonVoix = document.getElementById("voix");

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
    return;
  }

  document.title = livre.titre;
  document.getElementById("titre").textContent = livre.titre;
  document.getElementById("imprimer").href = `imprimer.html?livre=${encodeURIComponent(livre.id)}`;

  const total = livre.pages.length;
  const dernierePageSeule = livre.pages[total - 1].type === "quatrieme";

  /* Découpe le livre en « vues » : une page à la fois, ou des doubles pages. */
  function calculerVues(double) {
    if (!double) return livre.pages.map((_, i) => [i]);
    const vues = [[0]];
    let i = 1;
    while (i < total) {
      const seule = i === total - 1 || (dernierePageSeule && i + 1 === total - 1);
      if (seule) {
        vues.push([i]);
        i += 1;
      } else {
        vues.push([i, i + 1]);
        i += 2;
      }
    }
    return vues;
  }

  const modeDouble = () => window.innerWidth >= 900 && window.innerWidth > window.innerHeight * 1.15;

  let double = modeDouble();
  let vues = calculerVues(double);
  let vue = 0;

  // Ouvrir à la page indiquée dans l'adresse (#p5), si présente.
  function pageDeLAdresse() {
    const page = parseInt((location.hash.match(/^#p(\d+)$/) || [])[1], 10);
    return page >= 0 && page < total ? page : null;
  }
  const depart = pageDeLAdresse();
  if (depart != null) vue = vues.findIndex((v) => v.includes(depart));

  window.addEventListener("hashchange", () => {
    const page = pageDeLAdresse();
    if (page == null) return;
    vue = vues.findIndex((v) => v.includes(page));
    afficher();
  });

  function afficher() {
    arreterVoix();
    const pages = vues[vue];
    const conteneur = document.createElement("div");
    conteneur.className = "double-page";
    conteneur.style.setProperty("--nb", double ? 2 : 1);
    pages.forEach((i) => conteneur.appendChild(Bibliotheque.creerPage(livre, livre.pages[i], i)));
    scene.replaceChildren(conteneur);

    const libelle = pages.length > 1 ? `Pages ${pages[0]}–${pages[1]}` : pages[0] === 0 ? "Couverture" : `Page ${pages[0]}`;
    position.textContent = `${libelle} / ${total - 1}`;
    precedent.disabled = vue === 0;
    suivant.disabled = vue === vues.length - 1;
    history.replaceState(null, "", `#p${pages[0]}`);

    // Précharger les images de la vue suivante.
    (vues[vue + 1] || []).forEach((i) => {
      const src = livre.pages[i].image;
      if (src) new Image().src = Bibliotheque.cheminImage(livre, src);
    });
  }

  function aller(delta) {
    const cible = Math.min(Math.max(vue + delta, 0), vues.length - 1);
    if (cible !== vue) {
      vue = cible;
      afficher();
    }
  }

  precedent.addEventListener("click", () => aller(-1));
  suivant.addEventListener("click", () => aller(1));

  document.addEventListener("keydown", (e) => {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") {
      e.preventDefault();
      aller(1);
    } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      aller(-1);
    } else if (e.key === "Home") {
      vue = 0;
      afficher();
    } else if (e.key === "End") {
      vue = vues.length - 1;
      afficher();
    }
  });

  // Glisser du doigt sur tablette / téléphone.
  let debutX = null;
  scene.addEventListener("touchstart", (e) => (debutX = e.touches[0].clientX), { passive: true });
  scene.addEventListener("touchend", (e) => {
    if (debutX == null) return;
    const dx = e.changedTouches[0].clientX - debutX;
    if (Math.abs(dx) > 50) aller(dx < 0 ? 1 : -1);
    debutX = null;
  });

  window.addEventListener("resize", () => {
    const nouveau = modeDouble();
    if (nouveau === double) return;
    const premiere = vues[vue][0];
    double = nouveau;
    vues = calculerVues(double);
    vue = vues.findIndex((v) => v.includes(premiere));
    afficher();
  });

  // Lecture à voix haute (si le navigateur la propose).
  const synthese = window.speechSynthesis;
  function arreterVoix() {
    if (synthese && synthese.speaking) synthese.cancel();
    boutonVoix.textContent = "🔊 Écouter";
  }

  if (synthese && "SpeechSynthesisUtterance" in window) {
    boutonVoix.hidden = false;
    boutonVoix.addEventListener("click", () => {
      if (synthese.speaking) {
        arreterVoix();
        return;
      }
      const texte = vues[vue].map((i) => Bibliotheque.texteLisible(livre, livre.pages[i])).filter(Boolean).join(" ");
      if (!texte) return;
      const phrase = new SpeechSynthesisUtterance(texte);
      phrase.lang = livre.langue || "fr-FR";
      phrase.rate = 0.9;
      const voix = synthese.getVoices().find((v) => v.lang && v.lang.startsWith("fr"));
      if (voix) phrase.voice = voix;
      phrase.onend = () => (boutonVoix.textContent = "🔊 Écouter");
      boutonVoix.textContent = "⏹️ Arrêter";
      synthese.speak(phrase);
    });
  }

  afficher();
})();
