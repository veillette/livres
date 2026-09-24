/* Page d'impression : réglages, aperçu des feuilles et impression. */
(async function () {
  "use strict";

  const PAPIERS = {
    lettre: { largeur: 215.9, hauteur: 279.4, nom: "Lettre" },
    a4: { largeur: 210, hauteur: 297, nom: "A4" },
  };
  const MM_EN_PX = 96 / 25.4;

  const form = document.getElementById("reglages");
  const zone = document.getElementById("feuilles");
  const resume = document.getElementById("resume");
  const aide = document.getElementById("aide");
  const stylePapier = document.getElementById("format-papier");
  const choixFaces = document.getElementById("choix-faces");

  const params = new URLSearchParams(location.search);
  const id = params.get("livre") || (window.CATALOGUE || [])[0];

  let livre;
  try {
    livre = await Bibliotheque.charger(id);
  } catch (err) {
    resume.textContent = err.message;
    resume.classList.add("message", "message--erreur");
    form.hidden = true;
    return;
  }

  document.title = `Imprimer — ${livre.titre}`;
  document.getElementById("titre").textContent = livre.titre;
  document.getElementById("lire").href = `lire.html?livre=${encodeURIComponent(livre.id)}`;

  // Les réglages peuvent venir de l'adresse (?papier=a4&mode=pages) ou du dernier usage.
  const memoire = (() => {
    try {
      return JSON.parse(localStorage.getItem("impression") || "{}");
    } catch {
      return {};
    }
  })();
  for (const nom of ["papier", "mode", "faces", "marge"]) {
    const valeur = params.get(nom) || memoire[nom];
    const input = valeur && form.querySelector(`input[name="${nom}"][value="${CSS.escape(valeur)}"]`);
    if (input) input.checked = true;
  }

  function reglages() {
    const donnees = new FormData(form);
    return {
      papier: donnees.get("papier"),
      mode: donnees.get("mode"),
      faces: donnees.get("faces"),
      marge: Number(donnees.get("marge")),
    };
  }

  function creerFeuille(indices, r, dimensions, etiquette) {
    const bloc = document.createElement("div");
    bloc.className = "feuille-bloc";

    const libelle = document.createElement("span");
    libelle.className = "feuille-bloc__etiquette";
    libelle.textContent = etiquette;
    bloc.appendChild(libelle);

    const feuille = document.createElement("div");
    feuille.className = `feuille feuille--${r.mode}`;
    feuille.style.setProperty("--l", `${dimensions.largeur}mm`);
    feuille.style.setProperty("--h", `${dimensions.hauteur}mm`);
    feuille.style.setProperty("--marge", `${r.marge}mm`);
    indices.forEach((i) => {
      const page = i == null ? { type: "vide" } : livre.pages[i];
      feuille.appendChild(Bibliotheque.creerPage(livre, page, i));
    });
    bloc.appendChild(feuille);
    return bloc;
  }

  function construire() {
    const r = reglages();
    const papier = PAPIERS[r.papier] || PAPIERS.lettre;
    const livretMode = r.mode === "livret";

    // Livret : feuille à l'italienne (paysage). Pages seules : à la française (portrait).
    const dimensions = livretMode
      ? { largeur: papier.hauteur, hauteur: papier.largeur }
      : { largeur: papier.largeur, hauteur: papier.hauteur };

    stylePapier.textContent = `@page { size: ${dimensions.largeur}mm ${dimensions.hauteur}mm; margin: 0; }`;
    choixFaces.hidden = !livretMode;

    const feuilles = [];
    if (livretMode) {
      const plan = Imposition.livret(livre.pages);
      plan.forEach((f) => {
        if (r.faces !== "verso") feuilles.push(creerFeuille(f.recto, r, dimensions, `Feuille ${f.numero} — recto`));
        if (r.faces !== "recto") feuilles.push(creerFeuille(f.verso, r, dimensions, `Feuille ${f.numero} — verso`));
      });
      const nbPages = plan.length * 4;
      const blanches = nbPages - livre.pages.length;
      resume.textContent =
        `${plan.length} feuille${plan.length > 1 ? "s" : ""} ${papier.nom} recto verso → livret de ${nbPages} pages` +
        (blanches ? ` (dont ${blanches} page${blanches > 1 ? "s" : ""} blanche${blanches > 1 ? "s" : ""})` : "") +
        ".";
    } else {
      livre.pages.forEach((_, i) =>
        feuilles.push(creerFeuille([i], r, dimensions, i === 0 ? "Couverture" : `Page ${i}`))
      );
      resume.textContent = `${livre.pages.length} feuilles ${papier.nom}, une page du livre par feuille.`;
    }

    zone.replaceChildren(...feuilles);
    ajusterEchelle();
    afficherAide(r, papier);

    try {
      localStorage.setItem("impression", JSON.stringify(r));
    } catch {
      /* stockage indisponible : on ignore */
    }
  }

  function afficherAide(r, papier) {
    const communs = `
      <li>Choisis le papier <strong style="display:inline">${papier.nom}</strong>, échelle <strong style="display:inline">100 %</strong> et marges <strong style="display:inline">Aucune</strong>.</li>
      <li>Coche « Graphiques d'arrière-plan » pour garder les couleurs.</li>`;
    if (r.mode !== "livret") {
      aide.innerHTML = `<strong>Dans la fenêtre d'impression</strong><ol>${communs}</ol>`;
      return;
    }
    const etapes = {
      toutes: `<li>Active <strong style="display:inline">Recto verso</strong>, retournement sur le <strong style="display:inline">bord court</strong>.</li>`,
      recto: `<li>Imprime les rectos, puis remets la pile dans le bac et choisis « Versos ». Fais un essai avec une feuille pour trouver le bon sens.</li>`,
      verso: `<li>Remets les feuilles déjà imprimées dans le bac, dans le même ordre que les rectos.</li>`,
    }[r.faces];
    aide.innerHTML = `
      <strong>Dans la fenêtre d'impression</strong>
      <ol>${communs}${etapes}</ol>
      <strong style="margin-top:8px">Ensuite</strong>
      <ol><li>Empile les feuilles dans l'ordre (feuille 1 dessus).</li><li>Plie la pile en deux.</li><li>Agrafe ou couds au milieu du pli.</li></ol>`;
  }

  /* À l'écran, on réduit les feuilles pour qu'elles tiennent dans la largeur. */
  function ajusterEchelle() {
    const disponible = zone.clientWidth || zone.parentElement.clientWidth;
    zone.querySelectorAll(".feuille").forEach((feuille) => {
      const largeurPx = parseFloat(feuille.style.getPropertyValue("--l")) * MM_EN_PX;
      const echelle = Math.min(1, (disponible - 8) / largeurPx, 0.75);
      feuille.style.setProperty("--echelle", echelle.toFixed(3));
    });
  }

  form.addEventListener("change", construire);
  window.addEventListener("resize", ajusterEchelle);
  document.getElementById("imprimer").addEventListener("click", () => window.print());

  construire();
})();
