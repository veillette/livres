/*
 * Bibliothèque : chargement des livres et rendu des pages.
 *
 * Chaque livre vit dans son propre dossier `livres/<id>/` et contient un
 * fichier `livre.js` qui appelle `Bibliotheque.ajouter({...})`.
 * La liste des livres affichés se trouve dans `livres/catalogue.js`.
 *
 * On charge les livres avec des balises <script> (et non fetch) pour que le
 * site fonctionne aussi en ouvrant simplement index.html depuis le disque.
 */
(function () {
  "use strict";

  const livres = new Map();

  function chargerScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = src;
      script.onload = resolve;
      script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
      document.head.appendChild(script);
    });
  }

  function element(tag, classe, texte) {
    const el = document.createElement(tag);
    if (classe) el.className = classe;
    if (texte != null) el.textContent = texte;
    return el;
  }

  /* Typographie française : espace insécable fine devant ! ? ; : » et après «,
     pour que la ponctuation ne se retrouve jamais seule en début de ligne. */
  function typographie(texte) {
    return texte.replace(/[  ]([!?;:»])/g, " $1").replace(/«[  ]/g, "« ");
  }

  /* Un texte peut contenir plusieurs paragraphes séparés par une ligne vide. */
  function blocTexte(texte, classe = "page__texte") {
    const bloc = element("div", classe);
    String(texte || "")
      .split(/\n\s*\n/)
      .map((p) => p.trim())
      .filter(Boolean)
      .forEach((p) => bloc.appendChild(element("p", null, typographie(p))));
    return bloc;
  }

  const Bibliotheque = {
    ajouter(livre) {
      if (!livre || !livre.id || !Array.isArray(livre.pages)) {
        console.error("Livre invalide :", livre);
        return;
      }
      livres.set(livre.id, livre);
    },

    async charger(id) {
      if (!/^[a-z0-9-]+$/.test(id || "")) {
        throw new Error(`Identifiant de livre invalide : « ${id} »`);
      }
      if (!livres.has(id)) await chargerScript(`livres/${id}/livre.js`);
      const livre = livres.get(id);
      if (!livre) throw new Error(`Le fichier du livre « ${id} » n'a pas appelé Bibliotheque.ajouter()`);
      return livre;
    },

    async chargerTout() {
      const ids = window.CATALOGUE || [];
      const resultats = await Promise.all(
        ids.map((id) =>
          this.charger(id).catch((err) => {
            console.error(err);
            return null;
          })
        )
      );
      return resultats.filter(Boolean);
    },

    cheminImage(livre, image) {
      if (/^(https?:|data:|\/)/.test(image)) return image;
      return `livres/${livre.id}/${image}`;
    },

    /*
     * Crée l'élément DOM d'une page. Sa taille est donnée par le parent :
     * tout le contenu est dimensionné en unités de conteneur (cqw / cqh),
     * donc la page s'adapte aussi bien à l'écran qu'à la feuille imprimée.
     */
    creerPage(livre, page, index) {
      const type = page.type || "illustration";
      const el = element("div", `page page--${type}`);
      el.style.setProperty("--couleur", page.couleur || livre.couleur || "#3a7bd5");
      if (page.fond) el.style.setProperty("--fond", page.fond);

      const image = (src, classe = "page__cadre") => {
        const cadre = element("div", classe);
        const img = element("img", "page__image");
        img.src = this.cheminImage(livre, src);
        img.alt = page.description || "";
        img.decoding = "async";
        cadre.appendChild(img);
        return cadre;
      };

      switch (type) {
        case "couverture": {
          if (page.image) el.appendChild(image(page.image));
          const bloc = element("div", "page__titre-bloc");
          const titre = page.titre || livre.titre;
          const long = titre.length > 22 ? " page__titre--long" : "";
          bloc.appendChild(element("h1", `page__titre${long}`, titre));
          if (livre.sousTitre) bloc.appendChild(element("p", "page__sous-titre", livre.sousTitre));
          el.appendChild(bloc);
          if (livre.auteur) el.appendChild(element("p", "page__auteur", livre.auteur));
          break;
        }

        case "titre": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          contenu.appendChild(element("h1", "page__titre", livre.titre));
          if (livre.sousTitre) contenu.appendChild(element("p", "page__sous-titre", livre.sousTitre));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          const credits = element("div", "page__credits");
          if (livre.auteur) credits.appendChild(element("p", null, `Texte : ${livre.auteur}`));
          if (livre.illustrateur) credits.appendChild(element("p", null, `Illustrations : ${livre.illustrateur}`));
          contenu.appendChild(credits);
          if (page.texte) contenu.appendChild(blocTexte(page.texte, "page__dedicace"));
          break;
        }

        case "texte": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          contenu.appendChild(blocTexte(page.texte));
          break;
        }

        case "quatrieme": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          contenu.appendChild(blocTexte(page.texte || livre.resume));
          if (livre.age) {
            const pied = el.appendChild(element("div", "page__pied"));
            pied.appendChild(element("span", "page__age", livre.age));
          }
          break;
        }

        case "vide":
          break;

        default: {
          // "illustration" : une image et un texte, selon une disposition.
          const disposition = page.disposition || "image-haut";
          el.classList.add("page--illustration", `page--${disposition}`);
          if (page.positionTexte === "haut") el.classList.add("page--texte-haut");
          if (page.image) el.appendChild(image(page.image));
          if (page.texte) el.appendChild(blocTexte(page.texte));
        }
      }

      const avecNumero = !["couverture", "titre", "quatrieme", "vide"].includes(type);
      if (avecNumero && livre.numeros !== false && index != null) {
        el.appendChild(element("span", "page__numero", String(index)));
      }
      return el;
    },

    /* Textes d'une page, pour la lecture à voix haute. */
    texteLisible(livre, page) {
      switch (page.type) {
        case "couverture":
          return [livre.titre, livre.auteur].filter(Boolean).join(". ");
        case "titre":
          return [livre.titre, livre.sousTitre].filter(Boolean).join(". ");
        case "quatrieme":
          return page.texte || livre.resume || "";
        default:
          return page.texte || "";
      }
    },
  };

  window.Bibliotheque = Bibliotheque;
})();
