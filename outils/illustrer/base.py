"""
Petite boîte à outils pour dessiner les illustrations des livres en SVG.

Tout est en coordonnées d'une page carrée de 800 × 800. Les fonctions
renvoient des chaînes SVG que l'on ajoute à une `Scene`, puis
`Scene.enregistrer(chemin)` écrit le fichier.

    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 640, "#8ce99a")
    S.add(arbre(150, 650))
    S.add(perso("ours", 400, 700, 1.4, expr="rire", bras="haut"))
    S.enregistrer("livres/mon-livre/images/01.svg")
"""
import math
import os
import random

ENCRE = "#2b2b3a"
ROSE = "#ff8fab"
ROUGE_BOUCHE = "#c92a2a"
BLANC = "#ffffff"

_compteur = [0]


def uid(prefixe="i"):
    _compteur[0] += 1
    return f"{prefixe}{_compteur[0]}"


def n(v):
    """Nombre compact : 12.0 → 12, 3.14159 → 3.1."""
    if isinstance(v, str):
        return v
    s = f"{v:.1f}"
    if s.endswith(".0"):
        s = s[:-2]
    if s == "-0":
        s = "0"
    return s


def _attrs(a):
    out = []
    for k, v in a.items():
        if v is None or v is False:
            continue
        k = k.rstrip("_").replace("_", "-")
        out.append(f'{k}="{n(v)}"')
    return (" " + " ".join(out)) if out else ""


def el(tag, contenu=None, **a):
    if contenu is None:
        return f"<{tag}{_attrs(a)}/>"
    return f"<{tag}{_attrs(a)}>{contenu}</{tag}>"


def rect(x, y, w, h, fill, rx=None, **a):
    return el("rect", x=x, y=y, width=w, height=h, rx=rx, fill=fill, **a)


def cercle(x, y, r, fill, **a):
    return el("circle", cx=x, cy=y, r=r, fill=fill, **a)


def ellipse(x, y, rx, ry, fill, rot=None, **a):
    t = f"rotate({n(rot)} {n(x)} {n(y)})" if rot else None
    return el("ellipse", cx=x, cy=y, rx=rx, ry=ry, fill=fill, transform=t, **a)


def chemin(d, fill="none", stroke=None, sw=None, **a):
    extra = {}
    if stroke:
        extra = dict(stroke=stroke, stroke_width=sw or 4, stroke_linecap="round", stroke_linejoin="round")
    return el("path", d=d, fill=fill, **extra, **a)


def trait(x1, y1, x2, y2, stroke=ENCRE, sw=4, **a):
    return el("line", x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke, stroke_width=sw, stroke_linecap="round", **a)


def poly(points, fill, **a):
    return el("polygon", points=" ".join(f"{n(x)},{n(y)}" for x, y in points), fill=fill, **a)


def g(contenu, transform=None, **a):
    if isinstance(contenu, (list, tuple)):
        contenu = "".join(contenu)
    return el("g", contenu, transform=transform, **a)


def place(contenu, x=0, y=0, s=1.0, flip=False, rot=0, sy=None):
    """Place un dessin fait autour de (0, 0) au point (x, y)."""
    t = []
    if x or y:
        t.append(f"translate({n(x)} {n(y)})")
    if rot:
        t.append(f"rotate({n(rot)})")
    sx = -s if flip else s
    sy = s if sy is None else sy
    if sx != 1 or sy != 1:
        t.append(f"scale({n(round(sx, 3)) if abs(sx) < 1 else n(sx)} {n(round(sy, 3)) if abs(sy) < 1 else n(sy)})")
    return g(contenu, " ".join(t) or None)


def texte(x, y, contenu, taille=48, fill=ENCRE, anchor="middle", poids=700, contour=None, rot=None, police="Fredoka, Andika, sans-serif"):
    a = dict(x=x, y=y, font_family=police, font_weight=poids, font_size=taille, text_anchor=anchor, fill=fill)
    if contour:
        a.update(stroke=contour, stroke_width=taille / 7, stroke_linejoin="round", paint_order="stroke")
    if rot:
        a["transform"] = f"rotate({n(rot)} {n(x)} {n(y)})"
    return el("text", contenu, **a)


class Scene:
    def __init__(self, w=800, h=800):
        self.w, self.h = w, h
        self.defs = []
        self.els = []

    def add(self, *morceaux):
        for m in morceaux:
            if isinstance(m, (list, tuple)):
                self.add(*m)
            elif m:
                self.els.append(m)
        return self

    def degrade(self, couleurs, vertical=True, radial=False, **a):
        i = uid("d")
        stops = "".join(
            el("stop", offset=n(k / (len(couleurs) - 1)), stop_color=c) for k, c in enumerate(couleurs)
        )
        if radial:
            self.defs.append(el("radialGradient", stops, id=i, **a))
        elif vertical:
            self.defs.append(el("linearGradient", stops, id=i, x1=0, y1=0, x2=0, y2=1))
        else:
            self.defs.append(el("linearGradient", stops, id=i, x1=0, y1=0, x2=1, y2=0))
        return f"url(#{i})"

    def svg(self):
        defs = f"<defs>{''.join(self.defs)}</defs>" if self.defs else ""
        corps = "\n".join(self.els)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}">\n{defs}\n{corps}\n</svg>\n'
        )

    def enregistrer(self, chemin_fichier):
        os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)
        with open(chemin_fichier, "w", encoding="utf-8") as fh:
            fh.write(self.svg())


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def ciel(S, haut="#74c0fc", bas="#e7f5ff"):
    S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))


def fond(S, couleur):
    S.add(rect(0, 0, S.w, S.h, couleur))


def sol(S, y, couleur="#8ce99a", bosse=18, couleur2=None, y2=None):
    w = S.w
    S.add(chemin(f"M 0 {y} Q {w * 0.3} {y - bosse} {w / 2} {y} T {w} {y} L {w} {S.h} L 0 {S.h} Z", couleur))
    if couleur2:
        y2 = y2 or y + 70
        S.add(chemin(f"M 0 {y2} Q {w * 0.4} {y2 - bosse} {w * 0.7} {y2} T {w + 200} {y2} L {w} {S.h} L 0 {S.h} Z", couleur2))


def collines(S, y, couleur="#b2f2bb", graine=1, n_=3, hauteur=110):
    r = random.Random(graine)
    w = S.w
    for i in range(n_):
        cx = (i + 0.5) * w / n_ + r.uniform(-60, 60)
        lw = w / n_ * r.uniform(0.8, 1.3)
        h = hauteur * r.uniform(0.7, 1.2)
        S.add(chemin(f"M {n(cx - lw)} {y} Q {n(cx)} {n(y - h * 2)} {n(cx + lw)} {y} Z", couleur))


def soleil(x, y, r=55, couleur="#ffd43b", rayons=True, visage=False):
    m = []
    if rayons:
        for k in range(12):
            a = k * math.pi / 6
            m.append(trait(x + math.cos(a) * (r + 12), y + math.sin(a) * (r + 12),
                           x + math.cos(a) * (r + 32), y + math.sin(a) * (r + 32), couleur, 8))
    m.append(cercle(x, y, r, couleur))
    if visage:
        m.append(yeux_simples(x, y - r * 0.1, r * 0.32, r * 0.1))
        m.append(chemin(f"M {n(x - r * 0.3)} {n(y + r * 0.25)} Q {n(x)} {n(y + r * 0.5)} {n(x + r * 0.3)} {n(y + r * 0.25)}", stroke="#e67700", sw=r * 0.08))
        m.append(ellipse(x - r * 0.55, y + r * 0.2, r * 0.14, r * 0.09, ROSE, opacity=0.6))
        m.append(ellipse(x + r * 0.55, y + r * 0.2, r * 0.14, r * 0.09, ROSE, opacity=0.6))
    return g(m)


def yeux_simples(x, y, ecart, r, couleur=ENCRE):
    return cercle(x - ecart, y, r, couleur) + cercle(x + ecart, y, r, couleur)


def lune(x, y, r=45, couleur="#fff3bf", fond_ciel=None, croissant=False, visage=False):
    m = [cercle(x, y, r * 1.5, couleur, opacity=0.15), cercle(x, y, r, couleur)]
    if croissant and fond_ciel:
        m.append(cercle(x + r * 0.45, y - r * 0.2, r * 0.9, fond_ciel))
    else:
        m.append(cercle(x - r * 0.3, y - r * 0.25, r * 0.16, "#ffe066", opacity=0.6))
        m.append(cercle(x + r * 0.35, y + r * 0.3, r * 0.11, "#ffe066", opacity=0.6))
    if visage and not croissant:
        m.append(chemin(f"M {n(x - r * .45)} {n(y - r * .05)} q {n(r * .15)} {n(r * .15)} {n(r * .3)} 0", stroke="#b08900", sw=r * .07))
        m.append(chemin(f"M {n(x + r * .15)} {n(y - r * .05)} q {n(r * .15)} {n(r * .15)} {n(r * .3)} 0", stroke="#b08900", sw=r * .07))
        m.append(chemin(f"M {n(x - r * .2)} {n(y + r * .35)} q {n(r * .2)} {n(r * .15)} {n(r * .4)} 0", stroke="#b08900", sw=r * .07))
    return g(m)


def etoile5(x, y, r, couleur="#ffe066", rot=0, **a):
    pts = []
    for k in range(10):
        ang = math.radians(rot - 90 + k * 36)
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((x + rr * math.cos(ang), y + rr * math.sin(ang)))
    return poly(pts, couleur, stroke=couleur, stroke_width=r * 0.18, stroke_linejoin="round", **a)


def etoiles(S, nb=30, graine=3, zone=(0, 0, 800, 450), couleur="#fff3bf"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        if r.random() < 0.3:
            S.add(etoile5(x, y, r.uniform(6, 11), couleur, rot=r.uniform(0, 30)))
        else:
            S.add(cercle(x, y, r.uniform(1.5, 3.5), couleur))


def nuit(S, haut="#1c2a52", bas="#4c5b9a"):
    ciel(S, haut, bas)


def nuage(x, y, s=1.0, couleur="#ffffff", ombre=None, opacity=None):
    forme = (
        cercle(-55, 10, 38, couleur) + cercle(-15, -18, 50, couleur) + cercle(40, -8, 42, couleur)
        + cercle(78, 18, 30, couleur) + rect(-95, 5, 200, 50, couleur, rx=25)
    )
    m = []
    if ombre:
        m.append(g(forme.replace(f'fill="{couleur}"', f'fill="{ombre}"'), "translate(0 8)"))
    m.append(forme)
    return place(g(m, opacity=opacity), x, y, s)


def arbre(x, y, s=1.0, feuillage="#51cf66", feuillage2="#40c057", tronc="#8d5524", fruits=None):
    m = [rect(-16, -140, 32, 140, tronc, rx=8),
         cercle(0, -200, 80, feuillage),
         cercle(-60, -160, 52, feuillage2), cercle(60, -160, 52, feuillage2),
         cercle(-25, -235, 45, feuillage2, opacity=0.5)]
    if fruits:
        for fx, fy in [(-40, -200), (35, -230), (55, -170), (-10, -160), (10, -265)]:
            m.append(cercle(fx, fy, 10, fruits))
    return place(m, x, y, s)


def sapin(x, y, s=1.0, couleur="#2f9e44", couleur2="#37b24d", neige=False):
    m = [rect(-12, -40, 24, 40, "#7c4a1e", rx=4)]
    for k, (w, yy) in enumerate([(90, -40), (72, -110), (52, -170)]):
        m.append(poly([(-w, yy), (0, yy - 110), (w, yy)], couleur if k % 2 == 0 else couleur2))
        if neige:
            m.append(poly([(-w * 0.35, yy - 72), (0, yy - 110), (w * 0.35, yy - 72)], "#fff"))
    return place(m, x, y, s)


def fleur(x, y, s=1.0, couleur="#ff6b6b", coeur="#ffd43b", tige=60):
    m = [trait(0, 0, 0, -tige, "#40c057", 5),
         ellipse(10, -tige * 0.45, 12, 5, "#51cf66", rot=-30)]
    for k in range(5):
        a = k * 2 * math.pi / 5
        m.append(cercle(math.cos(a) * 11, -tige + math.sin(a) * 11, 10, couleur))
    m.append(cercle(0, -tige, 8, coeur))
    return place(m, x, y, s)


def herbe(x, y, s=1.0, couleur="#40c057"):
    return place(chemin("M -14 0 Q -12 -18 -20 -30 Q -6 -16 -4 0 Q -2 -26 4 -40 Q 6 -18 6 0 Q 10 -16 22 -26 Q 14 -12 14 0 Z", couleur), x, y, s)


def buisson(x, y, s=1.0, couleur="#40c057", couleur2="#51cf66", baies=None):
    m = [cercle(-45, -30, 38, couleur), cercle(45, -30, 38, couleur), cercle(0, -55, 48, couleur2),
         rect(-80, -32, 160, 32, couleur)]
    if baies:
        m += [cercle(bx, by, 7, baies) for bx, by in [(-40, -45), (-5, -75), (30, -50), (55, -25), (-20, -20)]]
    return place(m, x, y, s)


def champignon(x, y, s=1.0, couleur="#fa5252", pied="#fff4e6"):
    m = [rect(-18, -55, 36, 55, pied, rx=12),
         chemin("M -60 -45 Q -60 -115 0 -115 Q 60 -115 60 -45 Z", couleur),
         cercle(-28, -75, 9, "#fff"), cercle(12, -95, 8, "#fff"), cercle(30, -62, 7, "#fff")]
    return place(m, x, y, s)


def caillou(x, y, s=1.0, couleur="#adb5bd"):
    return place(chemin("M -40 0 Q -45 -30 -10 -34 Q 30 -40 42 -12 Q 46 0 40 0 Z", couleur), x, y, s)


def maison(x, y, s=1.0, mur="#ffe8cc", toit="#e8590c", porte="#a0522d", fenetre="#a5d8ff", lumiere=False):
    vitre = "#ffe066" if lumiere else fenetre
    m = [rect(-100, -150, 200, 150, mur),
         poly([(-125, -145), (0, -250), (125, -145)], toit),
         rect(-25, -85, 50, 85, porte, rx=6), cercle(14, -42, 4, "#ffd43b"),
         rect(-80, -120, 40, 40, vitre, stroke="#fff", stroke_width=5),
         rect(40, -120, 40, 40, vitre, stroke="#fff", stroke_width=5),
         rect(55, -235, 26, 55, "#c92a2a")]
    return place(m, x, y, s)


def eau(S, y, couleur="#4dabf7", couleur2="#74c0fc", vagues=True):
    S.add(rect(0, y, S.w, S.h - y, couleur))
    if vagues:
        for k in range(8):
            yy = y + 30 + k * 35
            if yy > S.h:
                break
            x0 = (k % 2) * 60
            d = " ".join(f"M {x0 + i * 120} {yy} q 20 -12 40 0" for i in range(8))
            S.add(chemin(d, stroke=couleur2, sw=5))


def pluie(S, nb=60, graine=5, zone=(0, 0, 800, 800), couleur="#4dabf7"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        S.add(trait(x, y, x - 6, y + 22, couleur, 4, opacity=0.8))


def goutte(x, y, s=1.0, couleur="#4dabf7"):
    return place(chemin("M 0 -16 Q 12 0 8 8 Q 0 16 -8 8 Q -12 0 0 -16 Z", couleur), x, y, s)


def flocons(S, nb=40, graine=6, zone=(0, 0, 800, 800), couleur="#ffffff"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        S.add(cercle(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(3, 7), couleur, opacity=0.9))


def coeur(x, y, s=1.0, couleur="#ff6b6b", rot=0):
    return place(chemin("M 0 12 C -30 -8 -18 -32 0 -16 C 18 -32 30 -8 0 12 Z", couleur), x, y, s, rot=rot)


def notes(x, y, s=1.0, couleur=ENCRE):
    m = [ellipse(0, 0, 9, 7, couleur, rot=-20), trait(8, -2, 8, -34, couleur, 3.5),
         chemin("M 8 -34 Q 20 -28 20 -16", stroke=couleur, sw=3.5),
         ellipse(34, 10, 9, 7, couleur, rot=-20), ellipse(64, 2, 9, 7, couleur, rot=-20),
         trait(42, 8, 42, -24, couleur, 3.5), trait(72, 0, 72, -32, couleur, 3.5),
         trait(42, -24, 72, -32, couleur, 6)]
    return place(m, x, y, s)


def zzz(x, y, s=1.0, couleur="#5c7cfa"):
    return g([texte(x, y, "z", 26 * s, couleur), texte(x + 24 * s, y - 26 * s, "z", 34 * s, couleur),
              texte(x + 54 * s, y - 60 * s, "Z", 44 * s, couleur)])


def mouvement(x, y, s=1.0, couleur=ENCRE, rot=0, nb=3):
    m = [trait(0, k * 16, -40 + k * 6, k * 16, couleur, 4, opacity=0.5) for k in range(nb)]
    return place(m, x, y, s, rot=rot)


def eclat(x, y, s=1.0, couleur="#ffd43b", nb=8):
    m = []
    for k in range(nb):
        a = k * 2 * math.pi / nb
        m.append(trait(math.cos(a) * 22, math.sin(a) * 22, math.cos(a) * 40, math.sin(a) * 40, couleur, 6))
    return place(m, x, y, s)


def paillettes(x, y, s=1.0, couleur="#ffd43b"):
    """Petites étincelles de joie."""
    m = [etoile5(0, 0, 12, couleur), etoile5(34, -26, 8, couleur), etoile5(-26, -34, 7, couleur)]
    return place(m, x, y, s)


def bulle(x, y, w, h, contenu, taille=36, pointe=None, fill="#ffffff", couleur=ENCRE):
    """Bulle de dialogue centrée en (x, y). `pointe` = (px, py) vers le personnage."""
    m = []
    if pointe:
        px, py = pointe
        m.append(poly([(x - 20, y + h / 2 - 14), (px, py), (x + 20, y + h / 2 - 14)], fill, stroke="#dee2e6", stroke_width=3))
    m.append(rect(x - w / 2, y - h / 2, w, h, fill, rx=min(h / 2, 40), stroke="#dee2e6", stroke_width=3))
    if pointe:
        m.append(poly([(x - 18, y + h / 2 - 16), (px, py), (x + 18, y + h / 2 - 16)], fill))
    lignes = contenu.split("\n")
    for k, ligne in enumerate(lignes):
        yy = y + taille * 0.35 + (k - (len(lignes) - 1) / 2) * taille * 1.15
        m.append(texte(x, yy, ligne, taille, couleur))
    return g(m)


def pensee(x, y, r, contenu="", fill="#ffffff", depuis=None):
    """Bulle de pensée ronde ; `depuis` = (px, py) point d'où partent les petites bulles."""
    m = []
    if depuis:
        px, py = depuis
        for k, rr in enumerate([7, 11, 16]):
            t = (k + 1) / 4
            m.append(cercle(px + (x - px) * t, py + (y - py) * t, rr, fill, stroke="#dee2e6", stroke_width=2))
    for a in range(0, 360, 40):
        m.append(cercle(x + math.cos(math.radians(a)) * r * 0.8, y + math.sin(math.radians(a)) * r * 0.62, r * 0.35, fill))
    m.append(ellipse(x, y, r * 0.95, r * 0.75, fill))
    m.append(contenu)
    return g(m)


# --- Intérieurs -------------------------------------------------------------

def interieur(S, mur="#fff4e6", plancher="#e8c39e", y=560, papier=None, plinthe="#d9a066"):
    S.add(rect(0, 0, S.w, y, mur))
    if papier:
        for k in range(0, S.w, 60):
            S.add(rect(k, 0, 24, y, papier, opacity=0.35))
    S.add(rect(0, y, S.w, S.h - y, plancher))
    for k in range(1, 6):
        S.add(trait(0, y + k * 50, S.w, y + k * 50, "#000", 2, opacity=0.06))
    S.add(rect(0, y - 14, S.w, 16, plinthe))


def fenetre(x, y, w=160, h=150, dehors="#a5d8ff", cadre="#ffffff", nuit_=False, rideaux=None, contenu=""):
    m = [rect(x - 8, y - 8, w + 16, h + 16, cadre, rx=6), rect(x, y, w, h, dehors)]
    if contenu:
        cid = uid("c")
        m.append(el("clipPath", rect(x, y, w, h, "#000"), id=cid))
        m.append(g(contenu, clip_path=f"url(#{cid})"))
    if nuit_:
        m.append(cercle(x + w * 0.7, y + h * 0.3, 16, "#fff3bf"))
        m += [cercle(x + w * 0.2, y + h * 0.25, 2.5, "#fff"), cercle(x + w * 0.4, y + h * 0.6, 2, "#fff"), cercle(x + w * 0.85, y + h * 0.75, 2.5, "#fff")]
    m += [rect(x + w / 2 - 4, y, 8, h, cadre), rect(x, y + h / 2 - 4, w, 8, cadre)]
    if rideaux:
        m.append(chemin(f"M {x - 20} {y - 14} L {x + 30} {y - 14} Q {x + 10} {y + h / 2} {x + 30} {y + h + 20} L {x - 20} {y + h + 20} Z", rideaux))
        m.append(chemin(f"M {x + w + 20} {y - 14} L {x + w - 30} {y - 14} Q {x + w - 10} {y + h / 2} {x + w - 30} {y + h + 20} L {x + w + 20} {y + h + 20} Z", rideaux))
        m.append(rect(x - 30, y - 22, w + 60, 12, "#adb5bd", rx=6))
    return g(m)


def tapis(x, y, rx=220, ry=45, couleur="#ffc9c9", bord="#ff8787"):
    return g([ellipse(x, y, rx, ry, bord), ellipse(x, y, rx - 14, ry - 8, couleur)])


def table(x, y, w=260, h=130, couleur="#c68642", nappe=None):
    m = [rect(x - w / 2 + 14, y - h, 16, h, couleur), rect(x + w / 2 - 30, y - h, 16, h, couleur),
         rect(x - w / 2, y - h - 18, w, 22, couleur, rx=6)]
    if nappe:
        m.append(chemin(f"M {x - w / 2 - 10} {y - h - 20} L {x + w / 2 + 10} {y - h - 20} L {x + w / 2 + 16} {y - h + 30} L {x - w / 2 - 16} {y - h + 30} Z", nappe))
    return g(m)


def lit(x, y, w=360, couleur="#74c0fc", couverture="#4dabf7", bois="#c68642", motif=None):
    """Lit vu de face, (x, y) = milieu du pied du lit au sol."""
    m = [rect(x - w / 2 - 14, y - 230, 28, 230, bois, rx=10), rect(x + w / 2 - 14, y - 170, 28, 170, bois, rx=10),
         rect(x - w / 2, y - 110, w, 60, "#fff", rx=10),
         rect(x - w / 2 + 20, y - 150, 110, 50, "#fff", rx=22, stroke="#e9ecef", stroke_width=3),
         rect(x - w / 2 + 110, y - 125, w - 110, 85, couverture, rx=18),
         rect(x - w / 2, y - 50, w, 30, bois, rx=6)]
    return g(m)


def lampe(x, y, s=1.0, abat="#ffd8a8", allumee=True):
    m = []
    if allumee:
        m.append(poly([(-40, -150), (40, -150), (110, 0), (-110, 0)], "#fff3bf", opacity=0.35))
    m += [rect(-30, -10, 60, 10, "#868e96", rx=4), rect(-4, -120, 8, 110, "#868e96"),
          poly([(-40, -150), (40, -150), (55, -110), (-55, -110)], abat)]
    return place(m, x, y, s)


def etagere(x, y, w=220, couleur="#c68642", objets=None):
    m = [rect(x - w / 2, y, w, 14, couleur, rx=4)]
    if objets:
        m.append(objets)
    return g(m)


def livres_pile(x, y, s=1.0):
    cols = ["#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c"]
    m = [rect(-30 + (k % 2) * 6, -18 * (k + 1), 64, 16, c, rx=3) for k, c in enumerate(cols)]
    return place(m, x, y, s)


def cadre_mur(x, y, w=110, h=90, contenu_couleur="#b2f2bb"):
    return g([rect(x, y, w, h, "#c68642", rx=4), rect(x + 10, y + 10, w - 20, h - 20, contenu_couleur),
              chemin(f"M {x + 10} {y + h - 10} L {x + w * 0.4} {y + h * 0.45} L {x + w * 0.6} {y + h * 0.7} L {x + w * 0.75} {y + h * 0.5} L {x + w - 10} {y + h - 10} Z", "#51cf66")])


def horloge(x, y, r=40, heure=3, minute=0, couleur="#fff", bord="#f08c00"):
    ah = math.radians((heure % 12 + minute / 60) * 30 - 90)
    am = math.radians(minute * 6 - 90)
    m = [cercle(x, y, r + 6, bord), cercle(x, y, r, couleur)]
    for k in range(12):
        a = math.radians(k * 30)
        m.append(cercle(x + math.cos(a) * r * 0.8, y + math.sin(a) * r * 0.8, 2.5, ENCRE))
    m.append(trait(x, y, x + math.cos(ah) * r * 0.5, y + math.sin(ah) * r * 0.5, ENCRE, 5))
    m.append(trait(x, y, x + math.cos(am) * r * 0.75, y + math.sin(am) * r * 0.75, ENCRE, 3.5))
    m.append(cercle(x, y, 4, ENCRE))
    return g(m)


def porte(x, y, w=150, h=300, couleur="#b5835a", ouverte=False):
    m = [rect(x - w / 2 - 10, y - h - 10, w + 20, h + 10, "#e9ecef")]
    if ouverte:
        m.append(rect(x - w / 2, y - h, w, h, "#343a40"))
        m.append(poly([(x - w / 2, y - h), (x - w / 2 - 40, y - h + 20), (x - w / 2 - 40, y - 10), (x - w / 2, y)], couleur))
    else:
        m += [rect(x - w / 2, y - h, w, h, couleur), cercle(x + w / 2 - 22, y - h / 2, 8, "#ffd43b"),
              rect(x - w / 2 + 18, y - h + 20, w - 36, h * 0.35, "#000", opacity=0.08, rx=6),
              rect(x - w / 2 + 18, y - h * 0.5, w - 36, h * 0.4, "#000", opacity=0.08, rx=6)]
    return g(m)


# ---------------------------------------------------------------------------
# Personnages
# ---------------------------------------------------------------------------
# Tous les personnages « debout » sont dessinés de face, les pieds en (0, 0),
# la tête vers y = -150 (rayon 55). Hauteur totale ≈ 210 à l'échelle 1.

ESPECES = {
    "ours": dict(c="#b07a4f", c2="#ecd0ae", pieds="#8f5f3a", ventre=True),
    "lapin": dict(c="#f1f3f5", c2="#ffffff", pieds="#dee2e6", ventre=True, interieur="#ffc9c9"),
    "souris": dict(c="#ced4da", c2="#f1f3f5", pieds="#ffa8a8", ventre=True, interieur="#ffc9c9"),
    "renard": dict(c="#f76707", c2="#fff4e6", pieds="#5c3d2e", ventre=True),
    "chat": dict(c="#ffa94d", c2="#fff4e6", pieds="#ffa94d", ventre=True, interieur="#ffc9c9"),
    "chien": dict(c="#e3b57a", c2="#fff4e6", pieds="#e3b57a", ventre=True, oreilles="#a0693a"),
    "cochon": dict(c="#ffc9d6", c2="#ffe3ea", pieds="#f7a1b5", ventre=True, groin="#f78fa7"),
    "mouton": dict(c="#f8f9fa", c2="#f1dcc3", pieds="#495057", ventre=False),
    "herisson": dict(c="#d9a57b", c2="#f3dcc3", pieds="#b98556", ventre=True, piquants="#7a5230"),
    "grenouille": dict(c="#69db7c", c2="#d8f5a2", pieds="#51cf66", ventre=True),
    "fourmi": dict(c="#9c3d2e", c2="#c9604e", pieds="#6d2a1f", ventre=False),
    "elephant": dict(c="#adb5bd", c2="#ced4da", pieds="#868e96", ventre=True, interieur="#ffc9c9"),
    "castor": dict(c="#8f5b34", c2="#d9b48f", pieds="#5c3a1e", ventre=True),
    "panda": dict(c="#ffffff", c2="#ffffff", pieds="#343a40", ventre=False),
}

# Position des mains (gauche, droite) pour chaque pose, et coudes éventuels.
POSES = {
    "bas": ((-52, -40), (52, -40)),
    "haut": ((-70, -165), (70, -165)),
    "salut": ((-52, -40), (72, -160)),
    "porte": ((-26, -74), (26, -74)),
    "large": ((-64, -70), (64, -70)),
    "guidon": ((62, -40), (84, -34)),
    "tient": ((-52, -40), (68, -146)),
    "calin": ((-30, -46), (30, -46)),
    "ouverts": ((-88, -108), (88, -108)),
    "donne": ((-52, -40), (84, -92)),
    "donne2": ((58, -86), (92, -92)),
    "montre": ((-52, -40), (86, -130)),
    "hanches": ((-40, -50), (40, -50)),
    "croises": ((26, -72), (-26, -80)),
    "joues": ((-44, -128), (44, -128)),
    "yeux": ((-20, -152), (20, -152)),
    "bouche": ((-8, -118), (10, -120)),
    "pense": ((-52, -40), (18, -112)),
    "tete": ((-52, -196), (52, -196)),
    "course": ((-66, -112), (56, -44)),
    "tire": ((72, -70), (92, -64)),
    "poing": ((-60, -150), (60, -150)),
}
COUDES = {
    "hanches": ((-66, -74), (66, -74)),
    "tete": ((-78, -140), (78, -140)),
    "poing": ((-66, -104), (66, -104)),
    "calin": ((-72, -84), (72, -84)),
}
DEVANT_VISAGE = {"joues", "yeux", "bouche", "pense", "tete"}

EXPRESSIONS = {
    # yeux, bouche, sourcils
    "sourire": ("normal", "sourire", None),
    "content": ("heureux", "sourire", None),
    "rire": ("heureux", "ouverte", None),
    "joie": ("normal", "ouverte", None),
    "surpris": ("grand", "o", "hauts"),
    "triste": ("normal", "triste", "tristes"),
    "pleure": ("fermes", "triste", "tristes"),
    "fache": ("normal", "boude", "faches"),
    "furieux": ("normal", "crie", "faches"),
    "inquiet": ("normal", "vague", "tristes"),
    "timide": ("bas", "petit_sourire", None),
    "dort": ("fermes", "petite", None),
    "neutre": ("normal", "ligne", None),
    "miam": ("heureux", "langue", None),
    "souffle": ("fermes", "souffle", None),
    "concentre": ("normal", "langue_cote", "plats"),
    "malin": ("normal", "coin", "malin"),
    "oups": ("grand", "grimace", "tristes"),
    "chante": ("heureux", "o", None),
    "bouche_bee": ("grand", "ouverte", "hauts"),
    "baille": ("fermes", "baille", None),
    "fier": ("heureux", "sourire", "hauts"),
    "degoute": ("fermes", "vague", "faches"),
}


def oeil(x, y, style="normal", regard=(0, 0), sclere=False, taille=1.0):
    dx, dy = regard
    t = taille
    if style == "heureux":
        return chemin(f"M {n(x - 8 * t)} {n(y + 3)} Q {n(x)} {n(y - 9 * t)} {n(x + 8 * t)} {n(y + 3)}", stroke=ENCRE, sw=3.8 * t)
    if style == "fermes":
        return chemin(f"M {n(x - 8 * t)} {n(y - 1)} Q {n(x)} {n(y + 7 * t)} {n(x + 8 * t)} {n(y - 1)}", stroke=ENCRE, sw=3.8 * t)
    if style == "bas":
        dy = dy + 1.2
    k = 1.3 if style == "grand" else 1.0
    m = []
    if sclere:
        m.append(cercle(x, y, 12 * t * k, "#fff", stroke=ENCRE, stroke_width=1.5))
        m.append(cercle(x + dx * 4, y + dy * 4, 6.5 * t * k, ENCRE))
        m.append(cercle(x + dx * 4 + 2, y + dy * 4 - 2.5, 2 * t, "#fff"))
    else:
        m.append(ellipse(x + dx * 3, y + dy * 3, 6.5 * t * k, 8.5 * t * k, ENCRE))
        m.append(cercle(x + dx * 3 + 2, y + dy * 3 - 3, 2.2 * t * k, "#fff"))
    return "".join(m)


def bouche(x, y, style="sourire", l=1.0):
    L = l
    if style == "sourire":
        return chemin(f"M {n(x - 12 * L)} {y} Q {x} {y + 12} {n(x + 12 * L)} {y}", stroke=ENCRE, sw=3.8)
    if style == "petit_sourire":
        return chemin(f"M {n(x - 7 * L)} {y + 1} Q {x} {y + 7} {n(x + 7 * L)} {y + 1}", stroke=ENCRE, sw=3.5)
    if style == "ouverte":
        return (chemin(f"M {n(x - 13 * L)} {y - 2} Q {x} {y + 22} {n(x + 13 * L)} {y - 2} Z", ROUGE_BOUCHE, stroke=ENCRE, sw=3)
                + ellipse(x, y + 9, 6 * L, 3.5, "#ff8787"))
    if style == "triste":
        return chemin(f"M {n(x - 11 * L)} {y + 7} Q {x} {y - 4} {n(x + 11 * L)} {y + 7}", stroke=ENCRE, sw=3.8)
    if style == "boude":
        return chemin(f"M {n(x - 11 * L)} {y + 6} Q {x} {y - 1} {n(x + 11 * L)} {y + 6}", stroke=ENCRE, sw=4.2)
    if style == "o":
        return ellipse(x, y + 4, 5.5, 7.5, ENCRE)
    if style == "souffle":
        return cercle(x, y + 3, 5, ENCRE)
    if style == "vague":
        return chemin(f"M {n(x - 12 * L)} {y + 3} q {n(4 * L)} -5 {n(8 * L)} 0 q {n(4 * L)} 5 {n(8 * L)} 0 q {n(4 * L)} -5 {n(8 * L)} 0", stroke=ENCRE, sw=3.5)
    if style == "crie":
        return (chemin(f"M {n(x - 15 * L)} {y - 3} L {n(x + 15 * L)} {y - 3} Q {n(x + 12 * L)} {y + 18} {x} {y + 18} Q {n(x - 12 * L)} {y + 18} {n(x - 15 * L)} {y - 3} Z", ROUGE_BOUCHE, stroke=ENCRE, sw=3)
                + rect(x - 11 * L, y - 3, 22 * L, 5, "#fff"))
    if style == "ligne":
        return trait(x - 8 * L, y + 3, x + 8 * L, y + 3, ENCRE, 3.8)
    if style == "petite":
        return ellipse(x, y + 3, 3.5, 4.5, ENCRE)
    if style == "langue":
        return (chemin(f"M {n(x - 12 * L)} {y} Q {x} {y + 12} {n(x + 12 * L)} {y}", stroke=ENCRE, sw=3.8)
                + ellipse(x + 5, y + 9, 5.5, 7, "#ff8787", stroke=ENCRE, stroke_width=1.5))
    if style == "langue_cote":
        return (trait(x - 9 * L, y + 3, x + 7 * L, y + 3, ENCRE, 3.8)
                + ellipse(x + 9, y + 7, 5, 6, "#ff8787", stroke=ENCRE, stroke_width=1.5))
    if style == "coin":
        return chemin(f"M {n(x - 10 * L)} {y + 3} Q {n(x + 2 * L)} {y + 9} {n(x + 13 * L)} {y - 3}", stroke=ENCRE, sw=3.8)
    if style == "grimace":
        return (rect(x - 14 * L, y - 3, 28 * L, 12, "#fff", rx=4, stroke=ENCRE, stroke_width=2.5)
                + trait(x - 13 * L, y + 3, x + 13 * L, y + 3, ENCRE, 1.5))
    if style == "baille":
        return ellipse(x, y + 7, 10, 14, ROUGE_BOUCHE, stroke=ENCRE, stroke_width=3)
    return ""


def sourcils(ex, ey, style):
    """ex = écart horizontal des yeux, ey = hauteur des yeux."""
    if not style:
        return ""
    y = ey - 20
    m = []
    for sgn in (-1, 1):
        xo, xi = sgn * (ex + 10), sgn * (ex - 9)
        if style == "tristes":
            m.append(trait(xo, y + 4, xi, y - 4, ENCRE, 3.5))
        elif style == "faches":
            m.append(trait(xo, y - 5, xi, y + 5, ENCRE, 4.5))
        elif style == "hauts":
            m.append(chemin(f"M {xo} {y - 2} Q {n((xo + xi) / 2)} {y - 11} {xi} {y - 2}", stroke=ENCRE, sw=3.5))
        elif style == "plats":
            m.append(trait(xo, y, xi, y, ENCRE, 3.5))
        elif style == "malin":
            if sgn < 0:
                m.append(trait(xo, y + 2, xi, y + 2, ENCRE, 3.5))
            else:
                m.append(chemin(f"M {xi} {y - 2} Q {n((xo + xi) / 2)} {y - 12} {xo} {y - 4}", stroke=ENCRE, sw=3.5))
    return "".join(m)


def _bras(x0, y0, main, coude, couleur, largeur=15):
    hx, hy = main
    if coude:
        cx, cy = coude
        return chemin(f"M {x0} {y0} Q {cx} {cy} {hx} {hy}", stroke=couleur, sw=largeur)
    mx, my = (x0 + hx) / 2, (y0 + hy) / 2
    sgn = 1 if hx >= x0 else -1
    return chemin(f"M {x0} {y0} Q {n(mx + sgn * 8)} {n(my + 6)} {hx} {hy}", stroke=couleur, sw=largeur)


def mains(x, y, s=1.0, bras="bas", flip=False):
    """Position (dans la page) des mains gauche et droite d'un personnage."""
    out = []
    for hx, hy in POSES[bras]:
        if flip:
            hx = -hx
        out.append((x + hx * s, y + hy * s))
    if flip:
        out.reverse()
    return out


def _motif(forme_clip, motif, couleur_motif):
    if not motif:
        return ""
    cid = uid("m")
    m = [el("clipPath", forme_clip, id=cid)]
    if motif == "rayures":
        lignes = "".join(rect(-60, y, 120, 8, couleur_motif) for y in range(-118, 0, 18))
    elif motif == "pois":
        lignes = "".join(cercle(x, y, 5, couleur_motif) for y in range(-110, 0, 20) for x in range(-50 + (y // 20 % 2) * 10, 60, 22))
    else:
        lignes = ""
    m.append(g(lignes, clip_path=f"url(#{cid})"))
    return "".join(m)


def perso(espece, x=0, y=0, s=1.0, flip=False, expr="sourire", bras="bas", regard=(0, 0),
          couleur=None, habit=None, motif=None, couleur_motif="#ffffff", acc=(), objet=None,
          derriere=None, rot=0, larmes=False, joues=True, couleur_acc=None, tache=False,
          sy=None, pieds_haut=False, visage=None):
    """Un personnage animal, dessiné de face.

    espece : clé de ESPECES ; expr : clé de EXPRESSIONS ; bras : clé de POSES.
    habit : couleur d'un vêtement sur le corps (et les bras) ; motif : "rayures" | "pois".
    acc : accessoires parmi "noeud", "chapeau", "toque", "bonnet", "casque",
          "lunettes", "echarpe", "tablier", "couronne", "fleur".
    objet : dessin (coordonnées locales) tenu devant le corps, entre les bras et les mains.
    derriere : dessin (coordonnées locales) placé derrière le personnage.
    """
    K = ESPECES[espece]
    c = couleur or K["c"]
    c2 = visage or K["c2"]
    pieds = K["pieds"] if not couleur else _assombrir(c, 0.85)
    if espece in ("mouton", "panda", "fourmi"):
        pieds = K["pieds"]
    if couleur_acc is None:
        couleur_acc = "#fa5252"
    yeux_style, bouche_style, sourcils_style = EXPRESSIONS[expr]
    manche = habit or c
    peau_main = c if espece != "panda" else "#343a40"
    if espece == "mouton":
        peau_main = "#495057"
        manche = habit or "#868e96"
    if espece == "panda":
        manche = habit or "#343a40"
    m = []
    if derriere:
        m.append(derriere)

    # --- derrière : queue, grandes oreilles
    if espece == "chat":
        m.append(chemin("M 28 -40 Q 80 -40 78 -95 Q 76 -120 92 -126", stroke=c, sw=13))
    elif espece == "renard":
        m.append(ellipse(62, -58, 26, 58, c, rot=40))
        m.append(ellipse(95, -95, 14, 20, "#fff4e6", rot=40))
    elif espece == "souris":
        m.append(chemin("M 22 -20 Q 80 -8 76 -64 Q 72 -96 98 -104", stroke="#ffa8a8", sw=6))
    elif espece == "cochon":
        m.append(chemin("M 34 -44 q 16 -2 14 -14 q -2 -10 -10 -6 q -6 6 4 12 q 10 4 18 -4", stroke=K["groin"], sw=5))
    elif espece == "chien":
        m.append(chemin("M 30 -48 Q 58 -60 62 -94", stroke=c, sw=12))
    elif espece == "fourmi":
        m.append(ellipse(42, -42, 40, 32, _assombrir(c, 0.85), rot=-25))
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 30} -60 Q {sgn * 62} -62 {sgn * 70} -36", stroke=pieds, sw=7))
    elif espece == "castor":
        m.append(ellipse(40, -16, 30, 50, "#5c3a1e", rot=60))
        m.append(g([trait(22, -28, 62, -6, "#4a2e16", 2, opacity=0.5), trait(30, -40, 68, -20, "#4a2e16", 2, opacity=0.5)]))
    elif espece == "elephant":
        m.append(chemin("M 30 -30 Q 50 -30 52 -10", stroke=pieds, sw=5))
    elif espece == "herisson":
        for k in range(9):
            a = math.radians(-160 + k * 17.5)
            if -110 < math.degrees(a) < -70:
                continue
            cx, cy = math.cos(a) * 44, -64 + math.sin(a) * 52
            m.append(poly([(cx - 10, cy), (cx + math.cos(a) * 26, cy + math.sin(a) * 26), (cx + 10, cy)], K["piquants"]))

    # --- pieds
    if not pieds_haut:
        m.append(ellipse(-21, -9, 19, 11, pieds))
        m.append(ellipse(21, -9, 19, 11, pieds))
    else:
        m.append(ellipse(-30, -14, 12, 18, pieds, rot=30))
        m.append(ellipse(30, -14, 12, 18, pieds, rot=-30))

    # --- corps
    corps = ellipse(0, -62, 42, 52, "#000")
    if espece == "mouton" and not habit:
        for k in range(10):
            a = math.radians(k * 36)
            m.append(cercle(math.cos(a) * 36, -62 + math.sin(a) * 44, 18, "#f8f9fa", stroke="#dee2e6", stroke_width=3))
        m.append(ellipse(0, -62, 42, 50, "#f8f9fa"))
    else:
        m.append(ellipse(0, -62, 42, 52, habit or c))
        if habit:
            m.append(_motif(corps, motif, couleur_motif))
        elif K.get("ventre"):
            m.append(ellipse(0, -54, 27, 35, c2))
        if espece == "panda" and not habit:
            m.append(ellipse(0, -62, 42, 52, "#fff"))
            m.append(chemin("M -40 -80 Q 0 -60 40 -80 L 36 -104 Q 0 -118 -36 -104 Z", "#343a40"))
    if "tablier" in acc:
        m.append(chemin("M -26 -96 L 26 -96 L 30 -30 Q 0 -18 -30 -30 Z", "#fff", stroke="#e9ecef", sw=2))
        m.append(rect(-14, -64, 28, 18, "#ffe3e3", rx=4))
        m.append(trait(-36, -92, 36, -92, "#fff", 5))
    if "cape" in acc:
        m.insert(0, chemin("M -40 -100 Q -70 -40 -64 -4 L 64 -4 Q 70 -40 40 -100 Z", couleur_acc))

    # --- bras
    main_g, main_d = POSES[bras]
    coude_g, coude_d = COUDES.get(bras, (None, None))
    bras_svg = (_bras(-32, -96, main_g, coude_g, manche) + _bras(32, -96, main_d, coude_d, manche))
    mains_svg = cercle(main_g[0], main_g[1], 11.5, peau_main) + cercle(main_d[0], main_d[1], 11.5, peau_main)
    if bras == "croises":
        bras_svg = (_bras(-32, -96, main_g, (-40, -60), manche) + _bras(32, -96, main_d, (40, -64), manche))
    devant = bras in DEVANT_VISAGE
    if not devant:
        m.append(bras_svg)
        if objet:
            m.append(objet)
        m.append(mains_svg)
    elif objet:
        m.append(objet)

    # --- tête
    m.append(_tete(espece, K, c, c2, yeux_style, bouche_style, sourcils_style, regard, joues, expr, larmes, acc, couleur_acc, tache))

    if devant:
        if bras == "pense":
            m.append(_bras(-32, -96, main_g, None, manche) + cercle(main_g[0], main_g[1], 11.5, peau_main))
            m.append(_bras(32, -96, main_d, (40, -80), manche) + cercle(main_d[0], main_d[1], 11.5, peau_main))
        else:
            m.append(bras_svg + mains_svg)

    return place(m, x, y, s, flip=flip, rot=rot, sy=sy)


def _assombrir(hexa, k=0.8):
    hexa = hexa.lstrip("#")
    r, gg, b = (int(hexa[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % (int(r * k), int(gg * k), int(b * k))


def eclaircir(hexa, k=0.5):
    hexa = hexa.lstrip("#")
    r, gg, b = (int(hexa[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % (int(r + (255 - r) * k), int(gg + (255 - gg) * k), int(b + (255 - b) * k))


def _tete(espece, K, c, c2, ys, bs, ss, regard, joues, expr, larmes, acc, ca, tache):
    m = []
    hy = -150
    ex, ey = 19, -152
    my = -121
    sclere = False
    tete_c = c
    r = 55

    # oreilles derrière la tête
    if espece == "ours" or espece == "castor":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 40, -194, 19, c))
            m.append(cercle(sgn * 40, -194, 10, c2))
    elif espece == "panda":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 40, -194, 20, "#343a40"))
    elif espece == "lapin" and "casque" not in acc:
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 23, -228, 15, 48, c, rot=sgn * 8))
            m.append(ellipse(sgn * 23, -226, 7, 36, K["interieur"], rot=sgn * 8))
    elif espece == "souris":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 48, -192, 31, c))
            m.append(cercle(sgn * 48, -192, 20, K["interieur"]))
    elif espece in ("chat", "renard"):
        inter = K.get("interieur", "#fff4e6") if espece == "chat" else "#fff4e6"
        for sgn in (-1, 1):
            m.append(poly([(sgn * 52, -170), (sgn * 48, -228), (sgn * 12, -200)], c))
            m.append(poly([(sgn * 44, -178), (sgn * 43, -216), (sgn * 20, -198)], inter))
            if espece == "renard":
                m.append(poly([(sgn * 50.5, -212), (sgn * 48, -228), (sgn * 36, -219)], "#5c3d2e"))
    elif espece == "elephant":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 66, -148, 42, 54, c, rot=sgn * -10))
            m.append(ellipse(sgn * 70, -146, 28, 40, K["interieur"], rot=sgn * -10))
    elif espece == "herisson":
        for k in range(13):
            a = math.radians(180 + k * 15)
            cx, cy = math.cos(a) * 50, hy + math.sin(a) * 50
            m.append(poly([(cx - math.sin(a) * 12, cy + math.cos(a) * 12), (cx + math.cos(a) * 34, cy + math.sin(a) * 34), (cx + math.sin(a) * 12, cy - math.cos(a) * 12)], K["piquants"]))
        tete_c = c2
    elif espece == "fourmi":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 16} -198 Q {sgn * 24} -236 {sgn * 44} -244", stroke=_assombrir(c, 0.7), sw=5))
            m.append(cercle(sgn * 46, -246, 8, _assombrir(c, 0.7)))
        sclere = True
    elif espece == "mouton":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 52, -150, 22, 10, "#d6bfa3", rot=sgn * 20))
        tete_c = c2
        r = 46
    elif espece == "grenouille":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 27, -192, 23, c))
        ex, ey = 27, -194
        sclere = True
        my = -125

    m.append(cercle(0, hy, r, tete_c))

    if espece == "mouton":
        for k, (wx, wy) in enumerate([(-30, -192), (-10, -202), (12, -202), (32, -190), (0, -188)]):
            m.append(cercle(wx, wy, 17, "#f8f9fa"))
    if espece == "panda":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 20, -150, 14, 18, "#343a40", rot=sgn * -25))
        sclere = False
    if espece == "herisson":
        m.append(chemin("M -44 -175 Q 0 -215 44 -175 Q 20 -186 0 -178 Q -20 -186 -44 -175 Z", K["piquants"]))
        for sgn in (-1, 1):
            m.append(cercle(sgn * 42, -180, 9, c2))

    # museaux et nez (avant les yeux pour que les yeux restent visibles)
    if espece == "renard":
        m.append(chemin("M -54 -140 Q -30 -142 0 -120 Q 30 -142 54 -140 Q 44 -98 0 -96 Q -44 -98 -54 -140 Z", "#fff4e6"))
    if espece in ("ours", "castor"):
        m.append(ellipse(0, -126, 25, 19, c2))
    if espece == "chien":
        m.append(ellipse(0, -125, 23, 18, c2))
        if tache:
            m.append(ellipse(-19, -155, 15, 16, K["oreilles"], opacity=0.7))
    if espece == "panda":
        m.append(ellipse(0, -125, 20, 15, "#f1f3f5"))

    if joues:
        rouge = expr in ("fache", "furieux", "timide")
        jc = "#ff6b6b" if expr in ("fache", "furieux") else ROSE
        jr = 1.35 if rouge or expr == "souffle" else 1.0
        jx = 36 if espece != "grenouille" else 38
        jy = -128 if espece != "cochon" else -134
        for sgn in (-1, 1):
            m.append(ellipse(sgn * jx, jy, 9 * jr, 5.5 * jr, jc, opacity=0.7))

    # yeux
    if espece == "panda":
        pass
    m.append(oeil(-ex, ey, ys, regard, sclere) + oeil(ex, ey, ys, regard, sclere))
    m.append(sourcils(ex, ey if espece != "grenouille" else -200, ss))
    if larmes:
        for sgn in (-1, 1):
            m.append(goutte(sgn * (ex + 4), ey + 26, 0.8, "#74c0fc"))

    # nez
    if espece in ("ours", "castor"):
        m.append(ellipse(0, -134, 10, 7, ENCRE))
        my = -120
    elif espece == "chien":
        m.append(ellipse(0, -136, 11, 8, ENCRE))
        m.append(cercle(-3, -139, 2.5, "#fff"))
        my = -120
    elif espece == "panda":
        m.append(ellipse(0, -131, 8, 5.5, ENCRE))
        my = -120
    elif espece == "renard":
        m.append(ellipse(0, -128, 8, 6, ENCRE))
        my = -118
    elif espece in ("lapin", "souris"):
        m.append(ellipse(0, -132, 6, 4.5, ROSE))
        my = -122
    elif espece == "chat":
        m.append(poly([(-6, -134), (6, -134), (0, -127)], ROSE))
        my = -122
    elif espece == "herisson":
        m.append(cercle(0, -130, 8, ENCRE))
        my = -116
    elif espece == "cochon":
        m.append(ellipse(0, -128, 21, 15, K["groin"]))
        m.append(ellipse(-7, -128, 3.5, 5, "#c2255c"))
        m.append(ellipse(7, -128, 3.5, 5, "#c2255c"))
        my = -107
    elif espece == "mouton":
        m.append(ellipse(0, -132, 7, 5, "#8a6d4f"))
        my = -122
    elif espece == "elephant":
        my = -112

    # bouche
    if espece == "elephant":
        m.append(bouche(-22, -114, bs, 0.8))
        trompe = "M 0 -142 Q 2 -110 12 -92 Q 22 -76 40 -82"
        m.append(chemin(trompe, stroke=_assombrir(c, 0.8), sw=25))
        m.append(chemin(trompe, stroke=c, sw=20))
        for k in range(3):
            m.append(chemin(f"M {-6 + k * 5} {-122 + k * 12} q 9 3 16 -2", stroke=_assombrir(c, 0.8), sw=2))
    else:
        L = 2.0 if espece == "grenouille" else 1.0
        m.append(bouche(0, my, bs, L))

    # moustaches
    if espece in ("chat", "souris", "lapin"):
        for sgn in (-1, 1):
            m.append(trait(sgn * 14, -130, sgn * 46, -136, "#868e96", 2))
            m.append(trait(sgn * 14, -126, sgn * 46, -122, "#868e96", 2))
    if espece == "castor":
        m.append(rect(-9, my + 6, 18, 14, "#fff", rx=3, stroke=ENCRE, stroke_width=1.5))
        m.append(trait(0, my + 6, 0, my + 20, ENCRE, 1.5))

    # oreilles devant (chien, cochon)
    if espece == "chien":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 55, -146, 15, 32, K["oreilles"], rot=sgn * 14))
    elif espece == "cochon":
        for sgn in (-1, 1):
            m.append(poly([(sgn * 20, -198), (sgn * 52, -214), (sgn * 46, -176)], K["groin"]))

    # accessoires de tête
    if "noeud" in acc:
        m.append(g([poly([(28, -196), (8, -212), (8, -180)], ca), poly([(28, -196), (48, -212), (48, -180)], ca), cercle(28, -196, 7, _assombrir(ca, 0.8))]))
    if "fleur" in acc:
        m.append(fleur(34, -184, 0.8, ca, tige=0))
    if "chapeau" in acc:
        m.append(chapeau(0, -193, 1.0, ca))
    if "toque" in acc:
        m.append(g([cercle(-26, -222, 27.5, "#dee2e6"), cercle(26, -222, 27.5, "#dee2e6"), cercle(0, -236, 31.5, "#dee2e6"),
                    cercle(-26, -222, 26, "#fff"), cercle(26, -222, 26, "#fff"), cercle(0, -236, 30, "#fff"),
                    rect(-40, -212, 80, 26, "#fff", rx=6, stroke="#e9ecef", stroke_width=2)]))
    if "bonnet" in acc:
        m.append(g([chemin("M -56 -160 Q -56 -222 0 -222 Q 56 -222 56 -160 Z", ca), rect(-60, -172, 120, 20, "#fff", rx=10), cercle(0, -226, 16, "#fff")]))
    if "casque" in acc:
        m.append(g([trait(-50, -174, -40, -108, ENCRE, 3), trait(50, -174, 40, -108, ENCRE, 3),
                    chemin("M -60 -170 Q -62 -236 0 -236 Q 62 -236 60 -170 Q 0 -182 -60 -170 Z", ca),
                    chemin("M -30 -222 Q 0 -232 30 -222", stroke="#fff", sw=6, opacity=0.7)]))
        if espece == "lapin":
            for sgn in (-1, 1):
                m.append(ellipse(sgn * 22, -262, 14, 40, c, rot=sgn * 8))
                m.append(ellipse(sgn * 22, -260, 6, 30, K["interieur"], rot=sgn * 8))
    if "lunettes" in acc:
        m.append(g([cercle(-ex, ey, 15, "none", stroke=ENCRE, stroke_width=3.5), cercle(ex, ey, 15, "none", stroke=ENCRE, stroke_width=3.5), trait(-ex + 15, ey, ex - 15, ey, ENCRE, 3)]))
    if "couronne" in acc:
        m.append(poly([(-34, -196), (-34, -232), (-17, -212), (0, -240), (17, -212), (34, -232), (34, -196)], "#ffd43b", stroke="#f59f00", stroke_width=3))
    if "echarpe" in acc:
        m.append(g([rect(-42, -104, 84, 18, ca, rx=9), chemin("M 18 -94 L 30 -48 L 14 -48 L 8 -94 Z", ca),
                    trait(15, -56, 29, -56, "#fff", 3, opacity=0.6)]))
    return g(m)


def chapeau(x, y, s=1.0, couleur="#fa5252", ruban="#ffd43b", rot=0, fleur_=True):
    """Chapeau rond ; (x, y) = milieu du bord."""
    m = [ellipse(0, 0, 64, 13, couleur), chemin("M -36 0 Q -38 -52 0 -52 Q 38 -52 36 0 Z", couleur),
         rect(-37, -16, 74, 12, ruban)]
    if fleur_:
        m.append(g([cercle(28, -12, 8, "#fff"), cercle(28, -12, 4, "#ffd43b")]))
    return place(m, x, y, s, rot=rot)


# --- Personnages de forme différente ----------------------------------------

def oiseau(x, y, s=1.0, couleur="#4dabf7", ventre="#e7f5ff", expr="sourire", ailes="bas",
           bec_ouvert=False, flip=False, regard=(0, 0), rot=0, pattes=True, acc=()):
    """Petit oiseau tout rond, (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if pattes:
        for sgn in (-1, 1):
            m.append(trait(sgn * 12, -30, sgn * 12, -4, "#f08c00", 4))
            m.append(chemin(f"M {sgn * 12 - 9} 0 L {sgn * 12} -6 L {sgn * 12 + 9} 0", stroke="#f08c00", sw=3.5))
    m.append(poly([(38, -70), (66, -86), (62, -60)], _assombrir(couleur, 0.8)))
    if ailes == "haut":
        m.append(ellipse(-50, -88, 14, 30, _assombrir(couleur, 0.85), rot=-40))
        m.append(ellipse(50, -88, 14, 30, _assombrir(couleur, 0.85), rot=40))
    m.append(cercle(0, -68, 44, couleur))
    m.append(ellipse(0, -52, 28, 26, ventre))
    if ailes == "bas":
        m.append(ellipse(-40, -60, 12, 24, _assombrir(couleur, 0.85), rot=20))
        m.append(ellipse(40, -60, 12, 24, _assombrir(couleur, 0.85), rot=-20))
    elif ailes == "ouvertes":
        m.append(ellipse(-58, -72, 12, 30, _assombrir(couleur, 0.85), rot=60))
        m.append(ellipse(58, -72, 12, 30, _assombrir(couleur, 0.85), rot=-60))
    m.append(chemin("M -6 -112 Q -2 -124 6 -118 Q 2 -126 12 -124", stroke=_assombrir(couleur, 0.8), sw=4))
    m.append(ellipse(-26, -70, 7, 4.5, ROSE, opacity=0.7) + ellipse(26, -70, 7, 4.5, ROSE, opacity=0.7))
    m.append(oeil(-15, -82, ys, regard, taille=0.85) + oeil(15, -82, ys, regard, taille=0.85))
    m.append(sourcils(15, -80, ss))
    if bec_ouvert or bs in ("ouverte", "o", "crie"):
        m.append(poly([(-9, -70), (9, -70), (0, -80)], "#ff922b"))
        m.append(poly([(-8, -66), (8, -66), (0, -54)], "#f76707"))
    else:
        m.append(poly([(-9, -70), (9, -70), (0, -58)], "#ff922b"))
    if "noeud" in acc:
        m.append(g([poly([(20, -108), (6, -118), (6, -98)], "#fa5252"), poly([(20, -108), (34, -118), (34, -98)], "#fa5252"), cercle(20, -108, 5, "#c92a2a")]))
    return place(m, x, y, s, flip=flip, rot=rot)


def chouette(x, y, s=1.0, couleur="#a9805b", visage="#f3dcc3", expr="sourire", ailes="bas",
             regard=(0, 0), flip=False, acc=(), yeux_grands=True):
    """Chouette debout, (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = []
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 18, -4, 14, 7, "#f08c00"))
    if ailes == "haut":
        m.append(ellipse(-56, -110, 18, 44, fonce, rot=-35))
        m.append(ellipse(56, -110, 18, 44, fonce, rot=35))
    m.append(ellipse(0, -80, 58, 78, couleur))
    for sgn in (-1, 1):
        m.append(poly([(sgn * 30, -140), (sgn * 52, -178), (sgn * 52, -130)], couleur))
    m.append(ellipse(0, -62, 36, 46, eclaircir(couleur, 0.55)))
    for row in range(3):
        for k in range(3 - (row % 2)):
            xx = -18 + k * 18 + (row % 2) * 9
            yy = -80 + row * 16
            m.append(chemin(f"M {xx - 5} {yy} Q {xx} {yy + 6} {xx + 5} {yy}", stroke=fonce, sw=2.5))
    if ailes == "bas":
        m.append(ellipse(-54, -78, 16, 42, fonce, rot=10))
        m.append(ellipse(54, -78, 16, 42, fonce, rot=-10))
    elif ailes == "ouvertes":
        m.append(ellipse(-76, -96, 16, 44, fonce, rot=60))
        m.append(ellipse(76, -96, 16, 44, fonce, rot=-60))
    for sgn in (-1, 1):
        m.append(cercle(sgn * 22, -120, 26, visage))
    ex, ey = 22, -120
    for sgn in (-1, 1):
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * ex, ey, ys, regard, taille=1.3))
        else:
            k = 1.2 if ys == "grand" else 1.0
            m.append(cercle(sgn * ex, ey, 14 * k, "#fff", stroke=ENCRE, stroke_width=1.5))
            dy = 1.2 if ys == "bas" else 0
            m.append(cercle(sgn * ex + regard[0] * 4, ey + (regard[1] + dy) * 4, 8 * k, ENCRE))
            m.append(cercle(sgn * ex + regard[0] * 4 + 3, ey + (regard[1] + dy) * 4 - 3, 2.5, "#fff"))
    m.append(sourcils(22, -114, ss))
    m.append(poly([(-7, -108), (7, -108), (0, -94)], "#f59f00"))
    if bs in ("ouverte", "o", "crie", "baille"):
        m.append(poly([(-6, -96), (6, -96), (0, -88)], "#e67700"))
    elif bs in ("triste",):
        m.append(chemin("M -8 -84 Q 0 -90 8 -84", stroke=ENCRE, sw=2.5))
    if "lunettes" in acc:
        m.append(g([cercle(-ex, ey, 20, "none", stroke=ENCRE, stroke_width=3.5), cercle(ex, ey, 20, "none", stroke=ENCRE, stroke_width=3.5)]))
    if "echarpe" in acc:
        m.append(g([rect(-46, -100, 92, 16, "#fa5252", rx=8), chemin("M 18 -90 L 30 -48 L 14 -48 L 8 -90 Z", "#fa5252")]))
    return place(m, x, y, s, flip=flip)


def escargot(x, y, s=1.0, coquille="#f59f00", corps="#b2f2bb", expr="sourire", flip=False, regard=(1, 0), acc=()):
    """Escargot de profil, la tête à droite. (x, y) = au sol, au milieu."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(coquille, 0.75)
    m = [chemin("M -80 0 Q -84 -26 -50 -28 L 50 -30 Q 62 -30 66 -60 Q 70 -96 92 -96 Q 116 -96 116 -60 Q 116 -20 96 -6 Q 86 0 60 0 Z", corps)]
    for dx, ang in ((82, -20), (104, 16)):
        a = math.radians(ang - 90)
        tx, ty = dx + math.cos(a) * 44, -92 + math.sin(a) * 44
        m.append(trait(dx, -92, tx, ty, corps, 7))
        m.append(cercle(tx, ty, 11, "#fff", stroke=ENCRE, stroke_width=1.5))
        if ys in ("heureux", "fermes"):
            m.append(oeil(tx, ty, ys, (0, 0), taille=0.7))
        else:
            m.append(cercle(tx + regard[0] * 3, ty + regard[1] * 3, 5.5, ENCRE))
            m.append(cercle(tx + regard[0] * 3 + 2, ty + regard[1] * 3 - 2, 1.8, "#fff"))
    m.append(ellipse(102, -58, 8, 5, ROSE, opacity=0.7))
    m.append(bouche(96, -48, bs, 0.8))
    m.append(cercle(-12, -72, 60, coquille))
    m.append(chemin("M -12 -72 m 0 -8 a 8 8 0 1 1 -8 8 a 18 18 0 1 1 18 18 a 30 30 0 1 1 -30 -30 a 44 44 0 1 1 44 44", stroke=fonce, sw=7))
    if "chapeau" in acc:
        m.append(chapeau(92, -100, 0.6, "#4dabf7"))
    return place(m, x, y, s, flip=flip)


def poisson(x, y, s=1.0, couleur="#ff922b", expr="sourire", flip=False, rot=0, bulles=False):
    """Poisson rouge, tête à droite. (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    m = [chemin("M -40 0 L -80 -30 Q -70 0 -80 30 Z", fonce),
         chemin("M -10 -30 Q 5 -55 25 -34 Z", fonce),
         ellipse(0, 0, 48, 34, couleur),
         chemin("M -6 18 Q 4 30 16 22 Z", fonce),
         chemin("M 8 -26 Q -2 0 8 26", stroke=fonce, sw=3),
         ]
    m.append(oeil(26, -8, ys, (0.5, 0), taille=0.9))
    m.append(sourcils(26, -6, ss) if False else "")
    m.append(bouche(40, 8, bs, 0.5))
    if bulles:
        m += [cercle(62, -30, 6, "none", stroke="#fff", stroke_width=2.5), cercle(74, -54, 9, "none", stroke="#fff", stroke_width=2.5)]
    return place(m, x, y, s, flip=flip, rot=rot)


def tortue(x, y, s=1.0, carapace="#40c057", peau="#b2f2bb", expr="sourire", flip=False, regard=(1, 0)):
    """Tortue de profil, tête à droite. (x, y) = au sol, au milieu."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(carapace, 0.75)
    m = [ellipse(-50, -10, 16, 14, peau), ellipse(40, -10, 16, 14, peau),
         chemin("M 50 -40 Q 70 -60 90 -76 Q 124 -96 136 -64 Q 144 -36 110 -34 Q 84 -32 60 -24 Z", peau),
         chemin("M -88 -24 Q -80 -120 0 -120 Q 80 -120 88 -24 Z", carapace),
         rect(-94, -30, 188, 14, fonce, rx=7)]
    for px, py in [(-44, -60), (0, -84), (44, -60), (-6, -44)]:
        m.append(poly([(px - 20, py), (px - 10, py - 18), (px + 10, py - 18), (px + 20, py), (px + 10, py + 18), (px - 10, py + 18)], fonce, opacity=0.55))
    m.append(ellipse(-24, -14, 16, 14, peau))
    m.append(ellipse(22, -14, 16, 14, peau))
    m.append(oeil(114, -70, ys, regard, taille=0.9))
    m.append(ellipse(124, -52, 7, 4.5, ROSE, opacity=0.7))
    m.append(bouche(126, -46, bs, 0.7))
    return place(m, x, y, s, flip=flip)


def faisceau(x0, y0, x1, y1, r, fill="#000", **a):
    """Cône de lumière d'une lampe (x0, y0) vers un disque de rayon r en (x1, y1)."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    px, py = -dy / L, dx / L
    pts = [(x0 + px * 8, y0 + py * 8), (x1 + px * r, y1 + py * r), (x1 - px * r, y1 - py * r), (x0 - px * 8, y0 - py * 8)]
    return poly(pts, fill, **a) + cercle(x1, y1, r, fill, **a)


def obscurite(S, trous=(), couleur="#0b1433", opacity=0.82):
    """Assombrit toute la scène, sauf les formes `trous` (dessinées en noir)."""
    mid = uid("k")
    S.defs.append(el("mask", rect(0, 0, S.w, S.h, "#fff") + "".join(trous), id=mid))
    S.add(rect(0, 0, S.w, S.h, couleur, opacity=opacity, mask=f"url(#{mid})"))


def trou_doux(x, y, r, force="#000"):
    """Trou à bords flous pour obscurite() : `force` = #000 (plein jour) à #fff (rien)."""
    i = uid("t")
    grad = el("radialGradient", el("stop", offset="0", stop_color=force) + el("stop", offset="0.55", stop_color=force)
              + el("stop", offset="1", stop_color="#fff"), id=i)
    return grad + cercle(x, y, r, f"url(#{i})")
