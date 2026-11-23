/* Navigation commune des lecteurs de Livres et Chansons. */
(function () {
  "use strict";

  function installer({
    elements: { scene, position, precedent, suivant, boutonCopier },
    pages, adresse, creerPage, cheminImage, avantAffichage, apresAffichage,
  }) {
    const total = pages.length;
    const dernierePageSeule = pages[total - 1].type === "quatrieme";

    // Une vue contient une page ou une double page.
    function calculerVues(double) {
      if (!double) return pages.map((_, i) => [i]);
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
      avantAffichage();
      const indices = vues[vue];
      const premiere = indices[0];
      const derniereVue = vue === vues.length - 1;
      const conteneur = document.createElement("div");
      conteneur.className = "double-page";
      conteneur.style.setProperty("--nb", double ? 2 : 1);
      indices.forEach((i) => conteneur.appendChild(creerPage(pages[i], i)));
      scene.replaceChildren(conteneur);

      const libelle = indices.length > 1 ? `Pages ${premiere}–${indices[1]}` : premiere === 0 ? "Couverture" : `Page ${premiere}`;
      position.textContent = `${libelle} / ${total - 1}`;
      precedent.disabled = vue === 0;
      suivant.disabled = derniereVue;
      history.replaceState(null, "", `#p${premiere}`);
      boutonCopier.dataset.copyLink = `${adresse}#p${premiere}`;
      boutonCopier.nextElementSibling.textContent = "";
      boutonCopier.hidden = location.protocol === "file:";

      // Précharger les images de la prochaine vue.
      (vues[vue + 1] || []).forEach((i) => {
        if (pages[i].image) new Image().src = cheminImage(pages[i]);
      });
      apresAffichage(derniereVue);
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
      // Espace sur un bouton ou un lien : laisser le navigateur l'activer.
      if (e.key === " " && e.target.closest("button, a, input, select, textarea")) return;
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
    // Un geste à deux doigts (zoom) ou surtout vertical ne tourne pas la page.
    let debut = null;
    scene.addEventListener(
      "touchstart",
      (e) => {
        debut = e.touches.length === 1 ? { x: e.touches[0].clientX, y: e.touches[0].clientY } : null;
      },
      { passive: true }
    );
    scene.addEventListener("touchend", (e) => {
      if (debut == null || e.touches.length > 0) {
        debut = null;
        return;
      }
      const dx = e.changedTouches[0].clientX - debut.x;
      const dy = e.changedTouches[0].clientY - debut.y;
      if (Math.abs(dx) > 50 && Math.abs(dx) > 2 * Math.abs(dy)) aller(dx < 0 ? 1 : -1);
      debut = null;
    });
    scene.addEventListener("touchcancel", () => (debut = null));

    window.addEventListener("resize", () => {
      const nouveau = modeDouble();
      if (nouveau === double) return;
      const premiere = vues[vue][0];
      double = nouveau;
      vues = calculerVues(double);
      vue = vues.findIndex((v) => v.includes(premiere));
      afficher();
    });

    return {
      afficher,
      pagesCourantes: () => vues[vue].map((i) => pages[i]),
    };
  }

  window.NavigationLecture = { installer };
})();
