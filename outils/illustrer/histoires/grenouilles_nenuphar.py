"""Dix grenouilles sur un nénuphar — comptine pour compter jusqu'à dix.

À chaque page, une grenouille de plus monte sur le nénuphar, avec sa manie ;
le soleil descend peu à peu. À dix, le nénuphar s'enfonce : plouf !
"""
from base import *
from objets import *
from fantastique import nenuphar
from sciences import canard

ID = "grenouilles-nenuphar"

# couleurs du ciel du début d'après-midi jusqu'au coucher du soleil
CIELS = [("#74c0fc", "#e7f5ff"), ("#74c0fc", "#fff9db"), ("#8ec5fc", "#fff3bf"), ("#a5b4fc", "#ffec99"),
         ("#b197fc", "#ffe8cc"), ("#c0a6f5", "#ffd8a8"), ("#d0a2e8", "#ffc078"), ("#e599b8", "#ffa94d"),
         ("#c77dbb", "#ff922b"), ("#9775fa", "#ff8787")]

# places sur le nénuphar (x, y) : rang du fond puis rang de devant
PLACES = [(410, 595), (290, 595), (530, 595), (170, 595), (650, 595),
          (400, 705), (275, 705), (525, 705), (150, 705), (650, 705)]


def guitare(x, y, s=1.0):
    m = [ellipse(0, 20, 34, 30, "#f08c00"), ellipse(0, -14, 26, 24, "#f08c00"), cercle(0, 10, 9, "#5c3a1e"),
         rect(-6, -110, 12, 90, "#8d5524"), rect(-10, -124, 20, 18, "#5c3a1e", rx=4)]
    return place(m, x, y, s, rot=-35)


def grenouille(k, s=0.5, expr=None, **extra):
    """La k-ième grenouille (1 à 10), avec sa particularité."""
    x, y = PLACES[k - 1]
    a = dict(expr=expr or "content")
    if k == 2:
        a.update(bras="course", expr=expr or "rire")
    elif k == 3:
        a.update(acc=("echarpe",), couleur_acc="#e64980")
    elif k == 4:
        a.update(bras="porte", objet=guitare(0, -60, 0.9), expr=expr or "chante")
    elif k == 5:
        a.update(bras="porte", objet=canard(0, -50, 0.35, nage=False))
    elif k == 6:
        a.update(expr=expr or "joie", bras="ouverts")
    elif k == 7:
        a.update(acc=("lunettes",), expr=expr or "dort", bras="tete")
    elif k == 8:
        a.update(acc=("chapeau",), couleur_acc="#4c6ef5", bras="salut")
    elif k == 9:
        a.update(bras="ouverts", expr=expr or "fier",
                 derriere=g([ellipse(-80, -12, 70, 16, "#51cf66"), ellipse(80, -12, 70, 16, "#51cf66")]))
    elif k == 10:
        a.update(bras="haut", expr=expr or "surpris")
    a.update(extra)
    return perso("grenouille", x, y, s, **a)


def mare(S, page, soleil_=True):
    haut, bas = CIELS[min(page, 10) - 1]
    ciel(S, haut, bas)
    if soleil_:
        S.add(soleil(660, 100 + page * 32, 52, "#ffd43b" if page < 7 else "#ff922b"))
    collines(S, 470, "#69db7c", graine=3)
    S.add(rect(0, 470, 800, 330, "#339af0"))
    for k in range(6):
        S.add(chemin(f"M {60 + k * 130} {520 + (k % 2) * 40} q 25 -12 50 0", stroke="#74c0fc", sw=5))
    S.add(g([herbe(30 + k * 40, 480, 1.3, "#2f9e44") for k in range(4)]), g([herbe(650 + k * 40, 480, 1.3, "#2f9e44") for k in range(4)]))
    S.add(nenuphar(700, 520, 0.9, "#ffc9de"))


def scene_n(nb, penche=0):
    S = Scene()
    mare(S, nb)
    m = [nenuphar(400, 650, 4.2)]
    for k in range(1, nb + 1):
        m.append(grenouille(k, 0.62 if k != nb else 0.72))
    if penche:
        S.add(g(m, f"rotate({penche} 400 650)"))
    else:
        S.add(m)
    texte_nb = str(nb)
    S.add(cercle(110, 120, 70, "#fff", opacity=0.9), texte(110, 150, texte_nb, 90, "#2f9e44"))
    return S


def couverture():
    S = Scene()
    mare(S, 5)
    S.add(nenuphar(400, 650, 4.2))
    for k in range(1, 11):
        S.add(grenouille(k, 0.62, expr="rire"))
    S.cachette(70, 350, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(nenuphar(200, 250, 2.0, "#ffc9de"))
    S.add(perso("grenouille", 200, 252, 0.85, expr="rire", bras="haut"))
    return S


def p(nb):
    def f():
        S = scene_n(nb)
        if nb == 6:
            S.add(bulle(560, 280, 220, 80, "Bla-bla-bla !", 34, pointe=(PLACES[5][0] + 20, 560)))
        if nb == 10:
            S.add(texte(560, 330, "Gare !", 80, "#e03131", contour="#fff", rot=-8))
        # petite bête : sur la berge à gauche, sauf quand les grenouilles l'occupent
        S.cachette(*{9: (720, 730), 10: (70, 340)}.get(nb, (70, 580)), "air")
        return S
    f.__name__ = f"p{nb:02d}"
    return f


def p11():
    S = Scene()
    mare(S, 10)
    S.add(nenuphar(400, 690, 4.2))
    S.add(rect(0, 690, 800, 110, "#339af0", opacity=0.6))
    r = random.Random(11)
    for k in range(1, 11):
        x, y = PLACES[k - 1]
        S.add(place(perso("grenouille", 0, 0, 0.45, expr="rire", bras="haut"), x + r.uniform(-40, 40), y + r.uniform(-120, 30), rot=r.uniform(-40, 40)))
    for k in range(14):
        S.add(goutte(100 + k * 46, 520 - (k % 4) * 50, 1.0, "#a5d8ff"))
    S.add(texte(400, 250, "PLOUF !", 110, "#1c7ed6", contour="#fff"))
    S.cachette(630, 730, "air")
    return S


def p12():
    S = Scene()
    nuit(S)
    etoiles(S, 40, 12, (0, 0, 800, 420))
    S.add(lune(640, 120, 50))
    collines(S, 470, "#2b8a3e", graine=3)
    S.add(rect(0, 560, 800, 240, "#1c3d6e"))
    S.add(rect(0, 470, 800, 100, "#2f9e44"))
    S.add(ellipse(640, 640, 90, 14, "#fff3bf", opacity=0.4))
    for k in range(10):
        S.add(perso("grenouille", 70 + k * 73, 560 - (k % 2) * 20, 0.38, expr="dort"))
    S.add(nenuphar(400, 700, 3.2, "#ffc9de"))
    S.add(zzz(560, 380, 1.1, "#fff3bf"))
    return S


IMAGES = [("couverture.svg", couverture), ("grenouille-seule.svg", vignette)]
NOMS = ["une", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix"]
for _k in range(1, 11):
    IMAGES.append((f"{_k:02d}-{NOMS[_k - 1]}.svg", p(_k)))
IMAGES += [("11-plouf.svg", p11), ("12-bonsoir.svg", p12)]
