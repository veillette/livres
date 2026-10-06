/*
 * Planche contact d'un livre : chaque page avec son image, sa description et
 * son texte, pour revoir les illustrations d'un coup d'œil.
 *
 *     node .claude/skills/nouveau-livre/planche.js <id> [sortie.html]
 *
 * Écrit une page HTML (par défaut planche-<id>.html dans le dossier courant)
 * et, si Playwright est installé, une capture PNG du même nom.
 */
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const RACINE = path.resolve(__dirname, "../../..");
const [id, sortieArg] = process.argv.slice(2);
if (!id) {
  console.error("Usage : node planche.js <id> [sortie.html]");
  process.exit(1);
}

const dossier = path.join(RACINE, "livres", id);
let livre = null;
vm.runInNewContext(fs.readFileSync(path.join(dossier, "livre.js"), "utf8"), {
  Bibliotheque: { ajouter(l) { livre = l; } },
});

const echapper = (s) =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

const cases = livre.pages.map((page, i) => {
  const type = page.type || "illustration";
  const image = page.image
    ? `<img src="${echapper(path.join(dossier, page.image))}" alt="">`
    : `<div class="sans-image">${echapper(type)}</div>`;
  return `<figure>
  ${image}
  <figcaption>
    <b>${i + 1}. ${echapper(type)}${page.disposition ? " · " + echapper(page.disposition) : ""}</b>
    ${page.image ? `<code>${echapper(page.image)}</code>` : ""}
    ${page.description ? `<p class="description">${echapper(page.description)}</p>` : ""}
    ${page.texte ? `<p>${echapper(page.texte).replace(/\n\n/g, "<br><br>")}</p>` : ""}
  </figcaption>
</figure>`;
});

const html = `<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Planche – ${echapper(livre.titre)}</title>
<style>
  body { font: 14px/1.35 system-ui, sans-serif; margin: 16px; background: #f1f3f5; }
  h1 { margin: 0 0 12px; color: ${livre.couleur || "#333"}; }
  main { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
  figure { margin: 0; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px #0002; }
  img { display: block; width: 100%; aspect-ratio: 1; object-fit: contain; background: #fff; border-bottom: 1px solid #dee2e6; }
  .sans-image { aspect-ratio: 3; display: grid; place-items: center; color: #868e96; border-bottom: 1px solid #dee2e6; }
  figcaption { padding: 8px; }
  code { display: block; color: #868e96; font-size: 12px; }
  p { margin: 6px 0 0; }
  .description { color: #5c7cfa; font-style: italic; }
</style></head>
<body>
<h1>${echapper(livre.titre)} <small>(${echapper(livre.id)} · ${echapper(livre.rayon)} · ${livre.pages.length} pages)</small></h1>
<main>
${cases.join("\n")}
</main>
</body></html>
`;

const sortie = path.resolve(sortieArg || `planche-${id}.html`);
fs.writeFileSync(sortie, html);
console.log(sortie);

let playwright;
try {
  playwright = require("playwright");
} catch {
  console.log("Playwright absent : ouvrir la page HTML dans un navigateur.");
  process.exit(0);
}

(async () => {
  const options = fs.existsSync("/opt/pw-browsers/chromium") ? { executablePath: "/opt/pw-browsers/chromium" } : {};
  let navigateur;
  try {
    navigateur = await playwright.chromium.launch(options);
  } catch {
    navigateur = await playwright.chromium.launch();
  }
  const onglet = await navigateur.newPage({ viewport: { width: 1600, height: 900 } });
  await onglet.goto("file://" + sortie);
  const png = sortie.replace(/\.html$/, "") + ".png";
  await onglet.screenshot({ path: png, fullPage: true });
  await navigateur.close();
  console.log(png);
})();
