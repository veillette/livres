/*
 * Imposition : dans quel ordre placer les pages sur les feuilles.
 *
 * Mode « livret » : deux pages côte à côte sur une feuille à l'italienne,
 * imprimée recto verso puis pliée en deux. Pour un livret de N pages
 * (N multiple de 4), la feuille k (en partant de 0) porte :
 *   recto : [N-1-2k, 2k]      verso : [2k+1, N-2-2k]
 * Exemple avec 8 pages : feuille 1 = [7,0] / [1,6], feuille 2 = [5,2] / [3,4].
 *
 * Les pages sont numérotées à partir de 0 (0 = couverture) ; null = page blanche.
 */
(function () {
  "use strict";

  /* Complète le livre par des pages blanches pour atteindre un multiple de 4.
     Les blanches sont glissées avant la quatrième de couverture pour qu'elle
     reste au dos du livret. */
  function completer(pages) {
    const indices = pages.map((_, i) => i);
    const manque = (4 - (indices.length % 4)) % 4;
    const blanches = Array(manque).fill(null);
    const dos = pages.length > 1 && pages[pages.length - 1].type === "quatrieme";
    if (dos) indices.splice(indices.length - 1, 0, ...blanches);
    else indices.push(...blanches);
    return indices;
  }

  function livret(pages) {
    const ordre = completer(pages);
    const n = ordre.length;
    const feuilles = [];
    for (let k = 0; k < n / 4; k++) {
      feuilles.push({
        numero: k + 1,
        recto: [ordre[n - 1 - 2 * k], ordre[2 * k]],
        verso: [ordre[2 * k + 1], ordre[n - 2 - 2 * k]],
      });
    }
    return feuilles;
  }

  window.Imposition = { completer, livret };
})();
