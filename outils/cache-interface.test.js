/* Vérifie les ressources nécessaires pour ouvrir les trois pages hors ligne. */
"use strict";

const assert = require("node:assert/strict");
const { existsSync, readFileSync } = require("node:fs");
const { join } = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const racine = join(__dirname, "..");
const contexte = vm.createContext({
  self: { location: { hostname: "localhost" }, addEventListener() {} },
});
vm.runInContext(readFileSync(join(racine, "sw.js"), "utf8"), contexte, { filename: "sw.js" });
const cache = new Set(vm.runInContext("INTERFACE", contexte));

test("tous les fichiers d'interface à mettre en cache existent", () => {
  for (const fichier of cache) {
    assert.ok(existsSync(join(racine, fichier)), fichier);
  }
});

for (const page of ["index.html", "lire.html", "imprimer.html"]) {
  test(`${page} et ses ressources sont prévues dans le cache hors ligne`, () => {
    assert.ok(cache.has(page), page);
    const html = readFileSync(join(racine, page), "utf8");
    for (const [, chemin] of html.matchAll(/<(?:link|script)\b[^>]*?\s(?:href|src)="([^"]+)"/gi)) {
      assert.ok(cache.has(chemin), `${chemin} manque dans INTERFACE (sw.js)`);
    }
  });
}
