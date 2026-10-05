/*
 * Tests de js/imposition.js (ordre des pages du livret à plier).
 *
 *     node --test
 *
 * Une erreur ici donne un livret imprimé dans le désordre : on vérifie que
 * chaque page sort exactement une fois, au bon endroit, pour toutes les
 * longueurs de livre.
 */
"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

// Même contexte que les tests (et non runInNewContext) : sinon les tableaux
// produits n'ont pas le même Array et deepEqual strict les refuse.
globalThis.window = {};
vm.runInThisContext(fs.readFileSync(path.join(__dirname, "../js/imposition.js"), "utf8"));
const { completer, livret } = window.Imposition;

/* Un livre de n pages : couverture, pages intérieures et, si demandé, quatrième. */
function livre(n, avecDos = true) {
  return Array.from({ length: n }, (_, i) => ({
    type: i === 0 ? "couverture" : avecDos && n > 1 && i === n - 1 ? "quatrieme" : "illustration",
  }));
}

/* Pages dans l'ordre de lecture une fois les feuilles empilées (feuille 1
   dessus, recto vers le haut) et pliées en deux. Chaque face est [gauche,
   droite]. En avançant, on tourne la moitié droite de chaque feuille, de
   l'extérieur vers le pli ; après le pli, on voit la moitié gauche de chaque
   feuille, du pli vers l'extérieur. */
function ordreDeLecture(feuilles) {
  const avant = feuilles.flatMap(({ recto, verso }) => [recto[1], verso[0]]);
  const apres = [...feuilles].reverse().flatMap(({ recto, verso }) => [verso[1], recto[0]]);
  return [...avant, ...apres];
}

test("exemple de la documentation : 8 pages", () => {
  const feuilles = livret(livre(8)).map(({ numero, recto, verso }) => ({ numero, recto, verso }));
  assert.deepEqual(feuilles, [
    { numero: 1, recto: [7, 0], verso: [1, 6] },
    { numero: 2, recto: [5, 2], verso: [3, 4] },
  ]);
});

test("les blanches sont glissées avant la quatrième de couverture", () => {
  assert.deepEqual(completer(livre(6)), [0, 1, 2, 3, 4, null, null, 5]);
  assert.deepEqual(completer(livre(6, false)), [0, 1, 2, 3, 4, 5, null, null]);
  assert.deepEqual(completer(livre(1)), [0, null, null, null]);
});

for (let n = 1; n <= 40; n++) {
  for (const avecDos of [true, false]) {
    test(`${n} page(s)${avecDos ? "" : " sans quatrième"}`, () => {
      const pages = livre(n, avecDos);
      const feuilles = livret(pages);
      const toutes = feuilles.flatMap((f) => [...f.recto, ...f.verso]);

      assert.equal(feuilles.length, Math.ceil(n / 4), "nombre de feuilles");
      assert.deepEqual(feuilles.map((f) => f.numero), feuilles.map((_, k) => k + 1), "numéros des feuilles");
      assert.equal(toutes.filter((p) => p === null).length, (4 - (n % 4)) % 4, "nombre de pages blanches");

      const imprimees = toutes.filter((p) => p !== null).sort((a, b) => a - b);
      assert.deepEqual(imprimees, pages.map((_, i) => i), "chaque page une seule fois");

      // Une fois plié, le livret se lit dans l'ordre, blanches mises à part.
      const lecture = ordreDeLecture(feuilles);
      assert.deepEqual(lecture.filter((p) => p !== null), pages.map((_, i) => i), "ordre de lecture");
      assert.equal(lecture[0], 0, "couverture devant");
      if (avecDos && n > 1) assert.equal(lecture[lecture.length - 1], n - 1, "quatrième au dos");
    });
  }
}
