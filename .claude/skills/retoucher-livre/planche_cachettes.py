"""Planche de revue de la petite bête : pour chaque page pleine, un gros plan
centré sur la bête, pour vérifier d'un coup d'œil qu'elle est posée sur un
sol, un mur, une branche… ou en vol dans un endroit plausible, visible, et
jamais sur un personnage ou un texte.

    python3 .claude/skills/retoucher-livre/planche_cachettes.py sortie.html <id> [<id>…]
    python3 .claude/skills/retoucher-livre/planche_cachettes.py sortie.html --tous

Écrit la page HTML et, si Node et Playwright sont là, des captures PNG
(sortie-1.png, sortie-2.png… de 48 gros plans chacune, avec leur page HTML). Les images lues sont
celles de livres/<id>/images : lancer generer.py avant.
"""
import html
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
sys.path.insert(0, os.path.join(RACINE, "outils", "illustrer"))

import base  # noqa: E402
import generer  # noqa: E402

ZOOM, CASE = 1.25, 200   # gros plan ×1,25 dans une case de 200 px

CAPTURE = r"""
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const fichiers = process.argv.slice(1);
  const options = fs.existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {};
  const nav = await chromium.launch(options);
  const onglet = await nav.newPage({ viewport: { width: 8 * 204 + 8, height: 900 } });
  for (const f of fichiers) {
    await onglet.goto('file://' + f, { timeout: 120000 });
    await onglet.waitForTimeout(300);
    const png = f.replace(/\.html$/, '.png');
    await onglet.screenshot({ path: png, fullPage: true });
    console.log(png);
  }
  await nav.close();
})();
"""

def places(modules):
    """[(livre, page, x, y sur la page, nature, livre complet)]"""
    out = []
    for m in modules:
        generer.regler(m)
        if not base.BETE_CACHEE[0]:
            continue
        lignes = []
        complet = True
        for nom, fabrique in m.IMAGES:
            S = fabrique()
            if S.w < 600:
                continue
            p = S.place_bete(nom)
            if not p:
                complet = False
                lignes.append((m.ID, nom, None, None, None))
                continue
            x, y, nature, s, _ = p
            if nature not in ("air",):
                y -= 12 * s          # centre du corps, pas les pattes
            X, Y = S.vers_page(x, y)
            lignes.append((m.ID, nom, X, Y, nature or "sol"))
        out += [ligne + (complet,) for ligne in lignes]
    return out


def main(args):
    if len(args) < 2:
        print(__doc__)
        return 1
    sortie = os.path.abspath(args[0])
    voulus = set(args[1:])
    modules = [m for m in generer.modules() if "--tous" in voulus or m.ID in voulus]
    cases = []
    for livre, page, X, Y, nature, complet in places(modules):
        legende = html.escape(f"{livre}/{page} · {nature or 'aucune'}{'' if complet else ' · livre incomplet'}")
        if X is None:
            cases.append(f'<figure class="manque"><div class="case">sans cachette</div><figcaption>{legende}</figcaption></figure>')
            continue
        src = os.path.join(RACINE, "livres", livre, "images", page)
        taille = 800 * ZOOM
        gauche, haut = CASE / 2 - X * ZOOM, CASE / 2 - Y * ZOOM
        cases.append(f'<figure><div class="case"><img src="file://{html.escape(src)}" style="width:{taille:.0f}px;height:{taille:.0f}px;'
                     f'left:{gauche:.0f}px;top:{haut:.0f}px"></div><figcaption>{legende}</figcaption></figure>')
    lots = [cases[i:i + 48] for i in range(0, len(cases), 48)]
    style = f"""<style>
body {{ margin: 4px; font: 9px/1.2 system-ui, sans-serif; background: #f1f3f5; }}
section {{ display: grid; grid-template-columns: repeat(8, {CASE}px); gap: 4px; margin-bottom: 8px; }}
figure {{ margin: 0; background: #fff; }}
.case {{ position: relative; width: {CASE}px; height: {CASE}px; overflow: hidden; background: #dee2e6; }}
.case img {{ position: absolute; max-width: none; }}
.case::after {{ content: ""; position: absolute; left: {CASE / 2 - 30}px; top: {CASE / 2 - 30}px; width: 60px; height: 60px;
  border: 2px dashed #f0f; border-radius: 50%; }}
.manque .case {{ display: grid; place-items: center; color: #c92a2a; }}
.manque .case::after {{ display: none; }}
figcaption {{ padding: 2px; word-break: break-all; }}
</style>"""

    def ecrire_page(chemin, sections):
        with open(chemin, "w", encoding="utf-8") as fh:
            fh.write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Petite bête</title>{style}</head>'
                     f'<body>{"".join(f"<section>{chr(10).join(lot)}</section>" for lot in sections)}</body></html>')

    ecrire_page(sortie, lots)
    print(sortie, f"({len(cases)} pages)")
    # une page par lot de 48 gros plans, pour les captures
    base_nom = sortie[:-5] if sortie.endswith(".html") else sortie
    morceaux = []
    for i, lot in enumerate(lots, 1):
        morceaux.append(f"{base_nom}-{i}.html")
        ecrire_page(morceaux[-1], [lot])
    env = dict(os.environ)
    try:
        racine_npm = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["NODE_PATH"] = os.pathsep.join(filter(None, [env.get("NODE_PATH"), racine_npm]))
        subprocess.run(["node", "-e", CAPTURE, *morceaux], check=True, env=env)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Capture impossible (Node ou Playwright absent) : ouvrir les pages HTML dans un navigateur.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
