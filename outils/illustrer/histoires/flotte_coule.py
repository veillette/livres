"""Qui flotte, qui coule ? — la flottaison.

Vue en coupe de l'étang : on voit ce qui est au-dessus et au-dessous de
l'eau. Un objet qui flotte n'est pas posé sur l'eau : il s'y enfonce en
partie (la pomme presque entièrement, la feuille à peine). Plus on charge le
bateau, plus il s'enfonce, jusqu'à ce que l'eau passe par-dessus le bord.
"""
from base import *
from objets import *
from sciences import *

ID = "flotte-coule"
SURFACE = 430
FOND = 730


def etang(S, graine=1):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, SURFACE, "#b2f2bb", graine=graine)
    for x in (40, 70, 730, 760):
        S.add(trait(x, SURFACE, x + 6, SURFACE - 150, "#2f9e44", 6))
        S.add(ellipse(x + 6, SURFACE - 150, 9, 26, "#8d5524"))
    S.add(rect(0, SURFACE, 800, 800 - SURFACE, S.degrade(["#74c0fc", "#1c7ed6"])))
    S.add(chemin(f"M 0 {FOND} Q 200 {FOND - 20} 400 {FOND} T 800 {FOND} L 800 800 L 0 800 Z", "#e9c46a"))
    for x in (120, 300, 520, 690):
        S.add(chemin(f"M {x} {FOND + 5} q -10 -40 4 -80 q 10 30 4 80", "#40c057", opacity=0.7))


def eau_devant(S):
    """Voile d'eau par-dessus ce qui est immergé, et reflets de la surface."""
    S.add(rect(0, SURFACE, 800, FOND - SURFACE + 40, "#1971c2", opacity=0.22))
    S.add(chemin(" ".join(f"M {x} {SURFACE} q 25 -8 50 0" for x in range(0, 800, 100)), stroke="#e7f5ff", sw=4, opacity=0.8))


def coin_coin(x, s=1.5, **k):
    """Le caneton flotte : environ un tiers de son corps est sous l'eau."""
    return canard(x, SURFACE + 34 * s, s, nage=False, **k)


def feuille(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 60, 18, "#40c057"), trait(-60, 0, 58, 0, "#2f9e44", 3), trait(-60, 0, -80, 8, "#2f9e44", 4)], x, y, s, rot=rot)


def caillou_(x, y, s=1.0):
    return caillou(x, y, s, "#868e96")


def bulles(x, y0, y1, s=1.0):
    return g([cercle(x + (k % 2) * 10 - 5, y0 + (y1 - y0) * k / 4, (4 + k) * s, "none", stroke="#e7f5ff", stroke_width=3) for k in range(5)])


def pomme_flotte(x, s=2.4):
    # densité de la pomme ≈ 0,8 : elle flotte, mais les 4/5 sont sous l'eau
    return pomme(x, SURFACE + 9 * s, s)


def bateau(x, y_ligne, s=1.0, cailloux=0, rot=0, enfoncement=0.3):
    """Bateau en papier ; (x, y_ligne) = ligne d'eau. enfoncement = part de la coque sous l'eau."""
    h = 70
    dy = h * (1 - enfoncement)
    m = [poly([(-120, -h), (120, -h), (80, 0), (-80, 0)], "#fff", stroke="#ced4da", stroke_width=3),
         poly([(-40, -h), (0, -h - 110), (40, -h)], "#f8f9fa", stroke="#ced4da", stroke_width=3),
         trait(0, -h - 110, 0, -h, "#dee2e6", 2),
         trait(-100, -h + 10, 100, -h + 10, "#e9ecef", 3)]
    for k in range(cailloux):
        m.append(caillou(-80 + (k % 5) * 40 + (k // 5) * 20, -h + 4 - (k // 5) * 22, 0.55, "#868e96"))
    return place(m, x, y_ligne + h - dy, s, rot=rot)


def grenouille(x, s=1.1, **k):
    return g([ellipse(x, SURFACE + 4, 110 * s, 22 * s, "#2f9e44"), poly([(x, SURFACE + 4), (x + 100 * s, SURFACE - 4), (x + 100 * s, SURFACE + 12)], "#1c7ed6", opacity=0.6),
              perso("grenouille", x, SURFACE, s, **k)])


def couverture():
    S = Scene()
    etang(S, 3)
    S.add(feuille(540, SURFACE - 4, 1.0, 5))
    S.add(caillou_(560, FOND + 6, 1.3))
    S.add(cle(230, FOND - 6, 1.3, rot=-10))
    S.add(pomme_flotte(660, 2.4))
    S.add(coin_coin(320, 1.9, expr="rire", regard=(1, 1)))
    eau_devant(S)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 210, 170, 36, "#a5d8ff"))
    S.add(canard(200, 214, 1.4, expr="content"))
    return S


def p01():
    S = Scene()
    etang(S, 1)
    S.add(coin_coin(260, 1.8, expr="surpris", regard=(1, -1)))
    icones = g([feuille(0, 0, 0.7), caillou_(110, 24, 1.1), pomme(210, 10, 1.6), cle(300, 0, 1.1)])
    S.add(pensee(600, 190, 190, place(icones, 470, 170, 0.85), depuis=(400, 320)), texte(600, 290, "?", 70, "#f76707"))
    eau_devant(S)
    return S


def p02():
    S = Scene()
    etang(S, 2)
    S.add(feuille(560, SURFACE - 4, 1.9, 4))
    S.add(coin_coin(260, 1.8, expr="content", regard=(1, 0)))
    eau_devant(S)
    return S


def p03():
    S = Scene()
    etang(S, 3)
    S.add(ellipse(560, SURFACE, 70, 12, "none", stroke="#fff", stroke_width=4), ellipse(560, SURFACE, 120, 20, "none", stroke="#fff", stroke_width=3, opacity=0.6))
    for k in range(5):
        S.add(goutte(510 + k * 25, SURFACE - 40 - (k % 2) * 30, 0.9, "#a5d8ff"))
    S.add(bulles(560, 480, 660))
    S.add(caillou_(560, FOND + 6, 2.0))
    S.add(coin_coin(250, 1.8, expr="surpris", regard=(1, 1)))
    S.add(texte(600, 280, "Plouf !", 64, "#1c7ed6", contour="#fff", rot=-6))
    eau_devant(S)
    return S


def p04():
    S = Scene()
    etang(S, 4)
    S.add(pomme_flotte(560, 3.2))
    S.add(coin_coin(250, 1.8, expr="bouche_bee", regard=(1, 0)))
    S.add(bulle(560, 180, 320, 80, "Elle flotte !", 40, pointe=(560, 330)))
    eau_devant(S)
    return S


def p05():
    S = Scene()
    etang(S, 5)
    S.add(bulles(560, 500, 680, 0.8))
    S.add(cle(560, FOND - 8, 2.0, rot=-15))
    S.add(coin_coin(250, 1.8, expr="oups", regard=(1, 1)))
    eau_devant(S)
    return S


def p06():
    S = Scene()
    etang(S, 6)
    # ce qui flotte : bois, feuille, pomme ; ce qui coule : pierre, clé et clou en fer
    S.add(place([rect(-60, -12, 120, 24, "#a0693a", rx=10), ellipse(60, 0, 8, 12, "#c68642")], 90, SURFACE + 4, 1.2))
    S.add(feuille(225, SURFACE - 4, 1.1))
    S.add(pomme_flotte(340, 2.2))
    S.add(caillou_(110, FOND + 6, 1.7), cle(270, FOND - 8, 1.6, rot=10), clou(400, FOND - 4, 1.5, rot=80))
    S.add(grenouille(670, 1.2, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(fleche(470, SURFACE - 30, 470, SURFACE - 110, "#2f9e44", 7), texte(470, SURFACE - 130, "flotte", 36, "#2f9e44", contour="#fff"))
    S.add(fleche(470, FOND - 170, 470, FOND - 70, "#c92a2a", 7), texte(470, FOND - 190, "coule", 36, "#c92a2a", contour="#fff"))
    eau_devant(S)
    return S


def p07():
    S = Scene()
    etang(S, 7)
    S.add(bateau(520, SURFACE, 1.3, cailloux=3, enfoncement=0.5))
    S.add(coin_coin(220, 1.6, expr="content", regard=(1, 0)))
    S.add(texte(520, 150, "1, 2, 3…", 60, "#1c7ed6", contour="#fff"))
    eau_devant(S)
    return S


def p08():
    S = Scene()
    etang(S, 8)
    S.add(bateau(540, SURFACE + 150, 1.2, cailloux=6, rot=-12, enfoncement=1.0))
    S.add(bulles(520, SURFACE + 20, SURFACE + 120), bulles(600, SURFACE + 10, SURFACE + 110, 0.8))
    S.add(coin_coin(220, 1.6, expr="rire", regard=(1, 1)))
    S.add(texte(560, 220, "glou glou !", 60, "#1c7ed6", contour="#fff", rot=-5))
    eau_devant(S)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("canard-seul.svg", vignette),
    ("01-etang.svg", p01), ("02-feuille.svg", p02), ("03-caillou.svg", p03), ("04-pomme.svg", p04),
    ("05-cle.svg", p05), ("06-grenouille.svg", p06), ("07-bateau.svg", p07), ("08-glou-glou.svg", p08),
]
