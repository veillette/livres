const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

test("la navigation conserve la page en changeant de largeur et isole la quatrième", () => {
  const contexte = {
    window: Object.assign(new EventTarget(), { innerWidth: 390, innerHeight: 800 }),
    document: Object.assign(new EventTarget(), {
      createElement: () => ({ style: { setProperty() {} }, appendChild() {} }),
    }),
    location: { hash: "#p2", protocol: "https:" },
    history: { replaceState: (_, __, hash) => { contexte.location.hash = hash; } },
  };
  const source = readFileSync(join(__dirname, "../js/navigation-lecture.js"), "utf8");
  vm.runInNewContext(source, contexte);

  const scene = Object.assign(new EventTarget(), { replaceChildren() {} });
  const position = {};
  const precedent = new EventTarget();
  const suivant = new EventTarget();
  const boutonCopier = { dataset: {}, nextElementSibling: {} };
  const pages = Array.from({ length: 6 }, (_, numero) => ({
    numero, type: numero === 5 ? "quatrieme" : "texte",
  }));
  let derniereVue;
  const navigation = contexte.window.NavigationLecture.installer({
    elements: { scene, position, precedent, suivant, boutonCopier },
    pages,
    adresse: "lire.html?livre=exemple",
    creerPage: () => ({}),
    cheminImage: () => "",
    avantAffichage() {},
    apresAffichage: (derniere) => { derniereVue = derniere; },
  });

  navigation.afficher();
  assert.equal(position.textContent, "Page 2 / 5");
  assert.equal(boutonCopier.dataset.copyLink, "lire.html?livre=exemple#p2");

  contexte.window.innerWidth = 1200;
  contexte.window.dispatchEvent(new Event("resize"));
  assert.equal(position.textContent, "Pages 1–2 / 5");
  assert.equal(contexte.location.hash, "#p1");

  const geste = (x, y) => {
    scene.dispatchEvent(Object.assign(new Event("touchstart"), { touches: [{ clientX: 200, clientY: 100 }] }));
    scene.dispatchEvent(Object.assign(new Event("touchend"), {
      touches: [], changedTouches: [{ clientX: x, clientY: y }],
    }));
  };
  geste(120, 250);
  assert.equal(position.textContent, "Pages 1–2 / 5");
  geste(120, 100);
  assert.equal(position.textContent, "Pages 3–4 / 5");
  assert.equal(derniereVue, false);

  contexte.document.dispatchEvent(Object.assign(new Event("keydown"), { key: "End" }));
  assert.equal(position.textContent, "Page 5 / 5");
  assert.equal(navigation.pagesCourantes()[0], pages[5]);
  assert.equal(suivant.disabled, true);
  assert.equal(derniereVue, true);

  contexte.location.hash = "#p0";
  contexte.window.dispatchEvent(new Event("hashchange"));
  assert.equal(position.textContent, "Couverture / 5");
  assert.equal(precedent.disabled, true);
});
