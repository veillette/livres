"""Propose une cachette pour la petite bête sur chaque page pleine où le décor
n'en offre pas : l'image est rendue dans Chromium et la bête va dans la zone
calme (sans détail) la plus proche d'un bord, hors des personnages, bulles et
textes réservés par occuper(). La bête y est en vol (S.cachette(x, y, "air")),
ou un petit poisson sous l'eau.

    python3 .claude/skills/retoucher-livre/cachettes.py <id> [<id>…]           # propose
    python3 .claude/skills/retoucher-livre/cachettes.py --ecrire <id> [<id>…]  # écrit dans les scripts
    python3 .claude/skills/retoucher-livre/cachettes.py --tous [--ecrire]

Demande Node et Playwright (Chromium). Toujours revoir les places proposées
(planche avant/après) : une zone calme peut être le ventre d'un personnage
dessiné à la main, qui ne réserve pas sa place.
"""
import json
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
ILLUSTRER = os.path.join(RACINE, "outils", "illustrer")
sys.path.insert(0, ILLUSTRER)

import base  # noqa: E402
import generer  # noqa: E402


def pages_sans_cachette(module):
    """[(nom de la page, nom de la fonction, SVG, zones réservées)] des pages
    pleines sans cachette (SVG rendu avec les réglages du livre)."""
    generer.regler(module)
    if not base.BETE_CACHEE[0]:
        return []
    out = []
    for nom, fabrique in module.IMAGES:
        S = fabrique()
        if S.w >= 600 and not S._bete(nom):
            # l'image rendue est en coordonnées de la page : zones et place
            # passent par le cadrage éventuel (S.camera)
            zones = []
            for x0, y0, x1, y1 in S.zones():
                (a, b), (c, d) = S.vers_page(x0, y0), S.vers_page(x1, y1)
                zones.append((a, b, c, d))
            out.append((nom, fabrique.__name__, S.svg(), zones, S.cadre))
    return out


def chercher(pages):
    """Rend les pages et renvoie {clé: (x, y) ou None}."""
    entree = [dict(cle=cle, svg=svg, occupe=occupe, couverture=nom == "couverture.svg")
              for cle, nom, svg, occupe, _ in pages]
    with tempfile.TemporaryDirectory() as tmp:
        f_in, f_out = os.path.join(tmp, "pages.json"), os.path.join(tmp, "places.json")
        with open(f_in, "w", encoding="utf-8") as fh:
            json.dump(entree, fh)
        env = dict(os.environ)
        try:
            racine_npm = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
            env["NODE_PATH"] = os.pathsep.join(filter(None, [env.get("NODE_PATH"), racine_npm]))
        except FileNotFoundError:
            pass
        subprocess.run(["node", os.path.join(ICI, "cachettes.js"), f_in, f_out], check=True, env=env)
        with open(f_out, encoding="utf-8") as fh:
            return {k: tuple(v) if v else None for k, v in json.load(fh).items()}


def ecrire(module, fonction, x, y):
    """Ajoute S.cachette(x, y, "air") avant le « return S » de la fonction."""
    chemin = os.path.join(ILLUSTRER, "histoires", module.__name__.split(".")[-1] + ".py")
    with open(chemin, encoding="utf-8") as fh:
        texte = fh.read()
    if sum(1 for _, f in module.IMAGES if f.__name__ == fonction) > 1:
        return f"{fonction} sert à plusieurs pages : à placer à la main"
    debut = texte.find(f"\ndef {fonction}(")
    if debut < 0:
        return f"{fonction} introuvable dans {os.path.basename(chemin)}"
    fin = texte.find("\ndef ", debut + 5)
    fin = len(texte) if fin < 0 else fin
    corps = texte[debut:fin]
    if "S.cachette(" in corps:
        return "S.cachette déjà présent"
    i = corps.rfind("\n    return S\n")
    if i < 0:
        return "pas de « return S » : à placer à la main"
    corps = corps[:i] + f'\n    S.cachette({x}, {y}, "air")' + corps[i:]
    with open(chemin, "w", encoding="utf-8") as fh:
        fh.write(texte[:debut] + corps + texte[fin:])
    return "écrit"


def main(args):
    ecrit = "--ecrire" in args
    voulus = {a for a in args if not a.startswith("--")}
    tous = "--tous" in args
    if not voulus and not tous:
        print(__doc__)
        return 1
    modules = [m for m in generer.modules() if tous or m.ID in voulus]
    a_chercher, origine = [], {}
    for m in modules:
        for nom, fonction, svg, occupe, cadre in pages_sans_cachette(m):
            cle = f"{m.ID}/{nom}"
            a_chercher.append((cle, nom, svg, occupe, cadre))
            origine[cle] = (m, fonction, cadre)
    if not a_chercher:
        print("Toutes les pages ont une cachette.")
        return 0
    places = chercher(a_chercher)
    for cle, *_ in a_chercher:
        m, fonction, cadre = origine[cle]
        place = places.get(cle)
        if not place:
            print(f"{cle} : aucune zone calme libre, à placer à la main")
            continue
        x, y = place
        if cadre:
            # point de la page → point de la scène (S.cachette est en scène)
            z, cx, cy = cadre
            x, y = round(cx + (x - 400) / z), round(cy + (y - 400) / z)
        etat = ecrire(m, fonction, x, y) if ecrit else "proposé"
        print(f"{cle} : S.cachette({x}, {y}, \"air\") dans {fonction}() — {etat}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
