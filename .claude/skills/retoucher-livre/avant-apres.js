/*
 * Planche avant / après d'un livre : chaque illustration telle qu'elle est
 * dans un commit de référence (par défaut HEAD) à côté de la version de
 * l'arbre de travail, avec la description de la page.
 *
 *     node .claude/skills/retoucher-livre/avant-apres.js <id> [sortie.html] [référence]
 *
 * Écrit une page HTML (par défaut avant-apres-<id>.html dans le dossier
 * courant), un dossier <sortie>-avant/ avec les anciens SVG et, si
 * Playwright est installé, une capture PNG du même nom que la page.
 */
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const { execFileSync } = require("child_process");

const RACINE = path.resolve(__dirname, "../../..");
const [id, sortieArg, reference = "HEAD"] = process.argv.slice(2);
if (!id) {
  console.error("Usage : node avant-apres.js <id> [sortie.html] [référence]");
  process.exit(1);
}

const dossier = path.join(RACINE, "livres", id);
let livre = null;
vm.runInNewContext(fs.readFileSync(path.join(dossier, "livre.js"), "utf8"), {
  Bibliotheque: { ajouter(l) { livre = l; } },
});

const sortie = path.resolve(sortieArg || `avant-apres-${id}.html`);
const avant = sortie.replace(/\.html$/, "") + "-avant";
fs.mkdirSync(avant, { recursive: true });

const echapper = (s) =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

// une case par image (les vignettes reviennent sur plusieurs pages : une seule fois)
const vues = new Set();
const cases = [];
for (const page of livre.pages) {
  if (!page.image || vues.has(page.image)) continue;
  vues.add(page.image);
  const actuel = path.join(dossier, page.image);
  const ancien = path.join(avant, path.basename(page.image));
  let image_avant = `<div class="nouveau">nouvelle image</div>`;
  try {
    const contenu = execFileSync("git", ["show", `${reference}:livres/${id}/${page.image}`], { cwd: RACINE, stdio: ["ignore", "pipe", "ignore"] });
    fs.writeFileSync(ancien, contenu);
    image_avant = `<img src="${echapper(ancien)}" alt="">`;
  } catch {
    // image absente du commit de référence
  }
  cases.push(`<figure>
  <div class="paire">${image_avant}<img src="${echapper(actuel)}" alt=""></div>
  <figcaption><code>${echapper(page.image)}</code>${page.description ? `<p>${echapper(page.description)}</p>` : ""}</figcaption>
</figure>`);
}

const html = `<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Avant / après – ${echapper(livre.titre)}</title>
<style>
  body { font: 13px/1.35 system-ui, sans-serif; margin: 16px; background: #f1f3f5; }
  h1 { margin: 0 0 12px; color: ${livre.couleur || "#333"}; }
  main { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
  figure { margin: 0; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px #0002; }
  .paire { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background: #dee2e6; }
  img, .nouveau { display: block; width: 100%; aspect-ratio: 1; object-fit: contain; background: #fff; }
  .nouveau { display: grid; place-items: center; color: #868e96; }
  figcaption { padding: 8px; }
  code { color: #868e96; }
  p { margin: 4px 0 0; color: #5c7cfa; font-style: italic; }
</style></head>
<body>
<h1>${echapper(livre.titre)} <small>(avant : ${echapper(reference)} · après : arbre de travail)</small></h1>
<main>
${cases.join("\n")}
</main>
</body></html>
`;
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
  const onglet = await navigateur.newPage({ viewport: { width: 1400, height: 900 } });
  await onglet.goto("file://" + sortie);
  const png = sortie.replace(/\.html$/, "") + ".png";
  await onglet.screenshot({ path: png, fullPage: true });
  await navigateur.close();
  console.log(png);
})();
