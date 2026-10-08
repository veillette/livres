/*
 * Cherche, sur l'image rendue de chaque page, une place pour la petite bête :
 * une zone calme (peu de détails), assez contrastée avec une coccinelle,
 * hors des zones réservées (personnages, bulles, textes), au plus près d'un
 * bord. Appelé par cachettes.py :
 *
 *     node cachettes.js pages.json places.json
 *
 * pages.json : [{cle, svg, occupe: [[x0, y0, x1, y1], …], couverture}]
 * places.json : {cle: [x, y] ou null}, en coordonnées de la page 800 × 800.
 */
const fs = require("fs");
const { chromium } = require("playwright");

const [entree, sortie] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(entree, "utf8"));

function analyser({ svg, occupe, couverture }) {
  return new Promise((resolve) => {
    const W = 800, H = 800;
    const img = new Image();
    img.onload = () => {
      const c = document.createElement("canvas");
      c.width = W; c.height = H;
      const ctx = c.getContext("2d");
      ctx.drawImage(img, 0, 0, W, H);
      const d = ctx.getImageData(0, 0, W, H).data;
      // images intégrales des canaux et de leurs carrés : moyenne et écart
      // type d'un rectangle en temps constant
      const N = (W + 1) * (H + 1);
      const S = [0, 1, 2].map(() => new Float64Array(N));
      const Q = [0, 1, 2].map(() => new Float64Array(N));
      for (let y = 1; y <= H; y++) {
        for (let x = 1; x <= W; x++) {
          const p = ((y - 1) * W + (x - 1)) * 4, i = y * (W + 1) + x;
          for (let k = 0; k < 3; k++) {
            const v = d[p + k] / 255;
            S[k][i] = v + S[k][i - 1] + S[k][i - W - 1] - S[k][i - W - 2];
            Q[k][i] = v * v + Q[k][i - 1] + Q[k][i - W - 1] - Q[k][i - W - 2];
          }
        }
      }
      const somme = (T, x0, y0, x1, y1) =>
        T[y1 * (W + 1) + x1] - T[y0 * (W + 1) + x1] - T[y1 * (W + 1) + x0] + T[y0 * (W + 1) + x0];
      const reserve = (x, y) => occupe.some(([a, b, e, f]) => x > a - 38 && x < e + 38 && y > b - 34 && y < f + 34);
      let meilleur = null;
      for (let cy = couverture ? 320 : 70; cy <= H - 70; cy += 10) {
        for (let cx = 70; cx <= W - 70; cx += 10) {
          if (reserve(cx, cy)) continue;
          const x0 = cx - 26, y0 = cy - 22, x1 = cx + 26, y1 = cy + 22, n = (x1 - x0) * (y1 - y0);
          const moy = [0, 1, 2].map((k) => somme(S[k], x0, y0, x1, y1) / n);
          const ecart = Math.sqrt([0, 1, 2].reduce((t, k) => t + somme(Q[k], x0, y0, x1, y1) / n - moy[k] * moy[k], 0) / 3);
          if (ecart > 0.05) continue;                               // trop de détails
          const [r, g, b] = moy, haut = Math.max(r, g, b), bas = Math.min(r, g, b);
          if (bas > 0.93 && haut - bas < 0.06) continue;            // blanc (bulle, papier vide)
          if (r > 0.5 && r - Math.max(g, b) > 0.25) continue;       // rouge : coccinelle invisible
          const bord = Math.min(cx, W - cx, cy, H - cy) / 400;      // 0 au bord, 1 au centre
          const note = ecart * 6 + bord;
          if (!meilleur || note < meilleur[0] - 1e-9) meilleur = [note, cx, cy];
        }
      }
      resolve(meilleur ? [meilleur[1], meilleur[2]] : null);
    };
    img.onerror = () => resolve(null);
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  });
}

(async () => {
  const options = fs.existsSync("/opt/pw-browsers/chromium") ? { executablePath: "/opt/pw-browsers/chromium" } : {};
  const navigateur = await chromium.launch(options);
  const onglet = await navigateur.newPage();
  await onglet.setContent("<!doctype html><title>cachettes</title>");
  const places = {};
  for (const page of pages) {
    places[page.cle] = await onglet.evaluate(analyser, page);
  }
  await navigateur.close();
  fs.writeFileSync(sortie, JSON.stringify(places));
})();
