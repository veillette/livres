/*
 * Lecture à voix haute et surlignage du mot prononcé.
 * Les voix qui n'envoient pas l'événement « boundary » lisent sans surligner.
 */
(function () {
  "use strict";

  /* Les espaces insécables gardent la ponctuation avec le mot qui précède. */
  function decouperMots(bloc, lecture) {
    for (const p of bloc.querySelectorAll("p")) {
      const fragments = p.textContent.split(/[ \t\n]+/).filter(Boolean);
      p.replaceChildren();
      fragments.forEach((fragment, n) => {
        if (n > 0) p.append(" ");
        const span = document.createElement("span");
        span.className = "mot";
        span.textContent = fragment;
        p.appendChild(span);
        if (lecture.texte) lecture.texte += " ";
        lecture.mots.push({ debut: lecture.texte.length, span });
        lecture.texte += fragment;
      });
    }
  }

  /* Recompose le texte à dire et repère la position des mots à surligner. */
  function preparerLecture(livre, pages, scene) {
    const lecture = { texte: "", mots: [] };
    const elements = scene.querySelectorAll(".page");
    pages.forEach((page, n) => {
      const bloc = elements[n]?.querySelector(".page__texte");
      // Couverture et page de titre : on dit le titre, sans surligner.
      if (!bloc || page.type === "couverture" || page.type === "titre") {
        const texte = Bibliotheque.texteLisible(livre, page);
        if (texte) lecture.texte += (lecture.texte ? " " : "") + texte;
      } else {
        decouperMots(bloc, lecture);
      }
    });
    return lecture;
  }

  function installer(bouton, scene, livre, pagesAffichees) {
    const synthese = window.speechSynthesis;
    if (!synthese || !("SpeechSynthesisUtterance" in window)) return () => {};

    let phraseEnCours = null;
    let motDit = null;

    function surligner(mot) {
      if (motDit) motDit.classList.remove("mot--dit");
      motDit = mot;
      if (motDit) motDit.classList.add("mot--dit");
    }

    function arreter() {
      phraseEnCours = null;
      if (synthese.speaking || synthese.pending) synthese.cancel();
      surligner(null);
      bouton.textContent = "🔊 Écouter";
    }

    bouton.hidden = false;
    bouton.addEventListener("click", () => {
      if (phraseEnCours) {
        arreter();
        return;
      }
      const { texte, mots } = preparerLecture(livre, pagesAffichees(), scene);
      if (!texte) return;
      const phrase = new SpeechSynthesisUtterance(texte);
      phrase.lang = livre.langue || "fr-FR";
      phrase.rate = 0.9;
      const voix = synthese.getVoices().find((v) => v.lang && v.lang.startsWith("fr"));
      if (voix) phrase.voice = voix;
      phrase.onboundary = (e) => {
        if (phrase !== phraseEnCours || (e.name && e.name !== "word")) return;
        // Le dernier mot qui commence avant la position annoncée.
        let trouve = null;
        for (const mot of mots) {
          if (mot.debut > e.charIndex) break;
          trouve = mot.span;
        }
        surligner(trouve);
      };
      phrase.onend = phrase.onerror = () => {
        if (phrase === phraseEnCours) arreter();
      };
      if (synthese.speaking || synthese.pending) synthese.cancel();
      phraseEnCours = phrase;
      bouton.textContent = "⏹️ Arrêter";
      synthese.speak(phrase);
    });

    return arreter;
  }

  window.LectureVoix = { installer };
})();
