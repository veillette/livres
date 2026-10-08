"""Place la petite bête là où le décor ne lui offre pas de cachette, et
vérifie les places déjà prises.

Chaque page est rendue dans Chromium. Sans cachette, la bête va dans la zone
calme (peu de détails, ni blanche ni rouge) la plus proche d'un bord, hors
des personnages, bulles et textes réservés par occuper() : en vol
(S.cachette(x, y, "air")), ou petit poisson sous l'eau.

Avec --verifier, chaque bête déjà placée (cachette du décor ou S.cachette)
est contrôlée sur l'image : sur du rouge (invisible), posée dans l'eau, sur
un objet très détaillé, ou dans une zone réservée → une nouvelle place est
cherchée comme ci-dessus.

    python3 .claude/skills/retoucher-livre/cachettes.py <id> [<id>…]               # propose
    python3 .claude/skills/retoucher-livre/cachettes.py --ecrire <id> [<id>…]      # écrit dans les scripts
    python3 .claude/skills/retoucher-livre/cachettes.py --verifier [--ecrire] <id> [<id>…]
    python3 .claude/skills/retoucher-livre/cachettes.py --tous [--verifier] [--ecrire]

Demande Node et Playwright (Chromium). Toujours revoir le résultat
(planche_cachettes.py) : une zone calme peut être le ventre d'un personnage
dessiné à la main qui ne réserve pas sa place, ou un endroit absurde (vol
dans la terre, coccinelle dans l'espace) que l'image seule ne dit pas.
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


def pages(module):
    """Pages pleines du livre : dict(nom, fonction, svg, zones, cadre, place,
    nature, explicite), en coordonnées de la page (cadrage compris). place
    est le centre du corps de la bête, ou None (pas de cachette)."""
    generer.regler(module)
    if not base.BETE_CACHEE[0]:
        return []
    out = []
    for nom, fabrique in module.IMAGES:
        S = fabrique()
        if S.w < 600 or S._cachette is False:
            continue
        zones = []
        for x0, y0, x1, y1 in S.zones():
            (a, b), (c, d) = S.vers_page(x0, y0), S.vers_page(x1, y1)
            zones.append((a, b, c, d))
        p = S.place_bete(nom)
        place, nature = None, None
        if p:
            x, y, nature, s, _ = p
            if nature not in ("air", "poisson"):
                y -= 12 * s          # centre du corps, pas les pattes
            place = S.vers_page(x, y)
        out.append(dict(nom=nom, fonction=fabrique.__name__, svg=S.svg(), zones=zones, cadre=S.cadre,
                        place=place, nature=nature or "sol", explicite=bool(S._cachette)))
    return out


def _node(entree):
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
            return json.load(fh)


def chercher(a_chercher):
    """{clé: (x, y) ou None} : zone calme libre la plus proche d'un bord."""
    res = _node([dict(cle=cle, svg=p["svg"], occupe=p["zones"], couverture=p["nom"] == "couverture.svg")
                 for cle, p in a_chercher])
    return {k: tuple(v) if v else None for k, v in res.items()}


def _teinte(r, v, b):
    """(teinte 0-1, saturation TSL) d'une couleur."""
    hi, lo = max(r, v, b), min(r, v, b)
    if hi == lo:
        return 0.0, 0.0
    d, l_ = hi - lo, (hi + lo) / 2
    sat = d / (2 - hi - lo) if l_ > 0.5 else d / (hi + lo)
    if hi == r:
        t = ((v - b) / d) % 6
    elif hi == v:
        t = (b - r) / d + 2
    else:
        t = (r - v) / d + 4
    return t / 6, sat


def defaut(p, mesure):
    """Raison de refuser la place d'une bête, ou None si elle convient.
    Seuils réglés sur la revue de tout le catalogue : un sol orangé (savane),
    un sol violet de nuit, un carrelage gris-bleu ou une plinthe derrière la
    bête ne sont pas des défauts."""
    x, y = p["place"]
    if any(x0 - 4 < x < x1 + 4 and y0 - 4 < y < y1 + 4 for x0, y0, x1, y1 in p["zones"]):
        return "sur un personnage, une bulle ou un texte"
    r, v, b = mesure["moy"]
    if r > 0.6 and v < 0.45 and b < 0.45 and r - max(v, b) > 0.3:
        return "sur du rouge (invisible)"
    teinte, sat = _teinte(r, v, b)
    if p["nature"] in ("sol", "eau") and 0.52 <= teinte <= 0.64 and sat > 0.45 and b > 0.45:
        return "posée dans l'eau"
    if mesure["ecart"] > 0.24:
        return "sur un objet très détaillé"
    return None


def ecrire(module, fonction, x, y, remplacer=False):
    """Ajoute (ou remplace) S.cachette(x, y, "air") avant le « return S »."""
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
    lignes = [ligne for ligne in corps.split("\n") if ligne.strip().startswith("S.cachette(")]
    if lignes and not remplacer:
        return "S.cachette déjà présent"
    if len(lignes) > 1:
        return "plusieurs S.cachette : à corriger à la main"
    nouvelle = f'    S.cachette({x}, {y}, "air")'
    if lignes:
        corps = corps.replace(lignes[0], nouvelle, 1)
    else:
        i = corps.rfind("\n    return S\n")
        if i < 0:
            return "pas de « return S » : à placer à la main"
        corps = corps[:i] + "\n" + nouvelle + corps[i:]
    with open(chemin, "w", encoding="utf-8") as fh:
        fh.write(texte[:debut] + corps + texte[fin:])
    return "écrit"


def main(args):
    ecrit = "--ecrire" in args
    verifier = "--verifier" in args
    voulus = {a for a in args if not a.startswith("--")}
    tous = "--tous" in args
    if not voulus and not tous:
        print(__doc__)
        return 1
    modules = [m for m in generer.modules() if tous or m.ID in voulus]
    toutes, origine = [], {}
    for m in modules:
        for p in pages(m):
            cle = f"{m.ID}/{p['nom']}"
            toutes.append((cle, p))
            origine[cle] = m
    a_chercher = [(cle, p) for cle, p in toutes if not p["place"]]
    raisons = {}
    if verifier:
        placees = [(cle, p) for cle, p in toutes if p["place"]]
        mesures = _node([dict(cle=cle, svg=p["svg"], occupe=[], point=list(p["place"])) for cle, p in placees])
        for cle, p in placees:
            raison = defaut(p, mesures[cle])
            if raison:
                raisons[cle] = raison
                a_chercher.append((cle, p))
    if not a_chercher:
        print("Toutes les pages ont une bonne cachette." if verifier else "Toutes les pages ont une cachette.")
        return 0
    places = chercher(a_chercher)
    for cle, p in a_chercher:
        m = origine[cle]
        motif = f" ({raisons[cle]})" if cle in raisons else ""
        place = places.get(cle)
        if not place:
            print(f"{cle}{motif} : aucune zone calme libre, à placer à la main")
            continue
        x, y = place
        if p["cadre"]:
            # point de la page → point de la scène (S.cachette est en scène)
            z, cx, cy = p["cadre"]
            x, y = round(cx + (x - 400) / z), round(cy + (y - 400) / z)
        etat = ecrire(m, p["fonction"], x, y, remplacer=cle in raisons) if ecrit else "proposé"
        print(f"{cle}{motif} : S.cachette({x}, {y}, \"air\") dans {p['fonction']}() — {etat}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
