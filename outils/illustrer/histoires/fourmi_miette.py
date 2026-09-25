"""Fourmi et la grosse miette — la persévérance (et demander de l'aide)."""
from base import *
from objets import *

ID = "fourmi-miette"
FOURMI = dict(acc=("noeud",), couleur_acc="#fcc419")


def macro(S, graine=1, y=640, pente=False):
    ciel(S, "#a5d8ff", "#fff9db")
    r = random.Random(graine)
    for k in range(9):
        x = r.uniform(0, 800)
        h = r.uniform(250, 480)
        S.add(chemin(f"M {n(x - 18)} {y + 20} Q {n(x - 10)} {n(y - h * 0.6)} {n(x + r.uniform(-40, 40))} {n(y - h)} Q {n(x + 6)} {n(y - h * 0.5)} {n(x + 18)} {y + 20} Z", r.choice(["#8ce99a", "#69db7c", "#b2f2bb"])))
    if pente:
        S.add(chemin(f"M 0 {y} L 360 {y} Q 560 {y - 80} 800 {y - 330} L 800 800 L 0 800 Z", "#d9a066"))
        S.add(chemin(f"M 0 {y + 30} L 360 {y + 30} Q 560 {y - 50} 800 {y - 300}", stroke="#c68642", sw=6))
    else:
        S.add(rect(0, y, 800, 800 - y, "#d9a066"))
    for k in range(18):
        S.add(ellipse(r.uniform(0, 800), r.uniform(y + 30, 790), r.uniform(6, 14), r.uniform(4, 8), "#c68642"))


def miette(x, y, s=1.0, rot=0):
    m = [chemin("M -120 0 Q -140 -80 -80 -110 Q -30 -150 30 -120 Q 110 -130 124 -60 Q 140 -10 110 0 Z", "#f4c27a"),
         chemin("M -110 -20 Q -120 -70 -80 -96 Q -40 -124 20 -106", stroke="#e8a354", sw=10, opacity=0.6)]
    for cx, cy, r in [(-60, -60, 12), (10, -80, 9), (60, -40, 14), (-20, -30, 7), (80, -90, 6)]:
        m.append(ellipse(cx, cy, r, r * 0.7, "#e8a354"))
    m.append(chemin("M -40 -130 Q 0 -150 40 -126 L 30 -116 Q 0 -136 -30 -118 Z", "#ffffff", opacity=0.8))
    return place(m, x, y, s, rot=rot)


def feuille_traineau(x, y, s=1.0, rot=0):
    m = [chemin("M -170 0 Q -150 -40 0 -36 Q 150 -40 190 -10 Q 150 20 0 18 Q -150 20 -170 0 Z", "#51cf66"),
         trait(-160, -4, 180, -8, "#2f9e44", 4)]
    for k in range(5):
        xx = -120 + k * 60
        m.append(chemin(f"M {xx} -6 Q {xx + 20} -24 {xx + 40} -30", stroke="#2f9e44", sw=3))
    return place(m, x, y, s, rot=rot)


def fourmiliere(x, y, s=1.0):
    m = [chemin("M -320 0 Q -200 -260 0 -270 Q 200 -260 320 0 Z", "#c68642"),
         ellipse(0, -30, 60, 44, "#5c3a1e")]
    for k in range(20):
        m.append(cercle(-250 + (k * 97) % 500, -30 - (k * 53) % 200, 6, "#a0693a"))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    macro(S, 2, 660)
    S.add(miette(440, 700, 1.5))
    S.add(perso("fourmi", 230, 740, 1.2, expr="fier", bras="tire", **FOURMI))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("fourmi", 200, 265, 0.85, expr="content", bras="salut", **FOURMI))
    return S


def p01():
    S = Scene()
    macro(S, 1)
    S.add(miette(510, 680, 1.8))
    S.add(perso("fourmi", 200, 720, 1.1, expr="bouche_bee", bras="joues", regard=(1, -0.5), **FOURMI))
    S.add(paillettes(560, 380), paillettes(700, 440, 0.7))
    S.add(texte(210, 330, "Waouh !", 60, "#e8590c", contour="#fff"))
    return S


def p02():
    S = Scene()
    macro(S, 3)
    S.add(miette(520, 700, 1.7))
    S.add(perso("fourmi", 290, 730, 1.15, expr="concentre", bras="tire", **FOURMI))
    for k in range(3):
        S.add(goutte(230 + k * 24, 400 + k * 12, 0.8, "#74c0fc"))
    S.add(texte(560, 330, "Hmmmf !", 56, "#e8590c", contour="#fff"))
    return S


def p03():
    S = Scene()
    macro(S, 4, 560, pente=False)
    S.add(chemin("M 0 480 Q 300 520 800 760 L 800 800 L 0 800 Z", "#d9a066"))
    S.add(miette(620, 700, 1.0, rot=70))
    S.add(mouvement(500, 620, 1.2, rot=30))
    S.add(perso("fourmi", 250, 560, 1.1, expr="oups", bras="ouverts", rot=18, **FOURMI))
    S.add(texte(400, 220, "Pas par là !", 60, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    macro(S, 5)
    S.add(caillou(250, 700, 1.6, "#adb5bd"))
    S.add(perso("fourmi", 250, 660, 1.05, expr="concentre", bras="pense", regard=(1, -0.3), pieds_haut=True, **FOURMI))
    S.add(escargot(560, 740, 1.4, coquille="#cc5de8", corps="#ffe8cc", flip=True, regard=(1, 0), expr="surpris"))
    S.add(bulle(560, 190, 360, 90, "Tu abandonnes ?", 38, pointe=(560, 500)))
    S.add(bulle(250, 330, 360, 80, "Non ! Je réfléchis.", 32, pointe=(250, 440)))
    return S


def p05():
    S = Scene()
    macro(S, 6)
    S.add(feuille_traineau(380, 730, 1.3))
    S.add(miette(370, 700, 1.1))
    S.add(chemin("M 620 722 Q 640 700 650 670", stroke="#2f9e44", sw=5))
    S.add(perso("fourmi", 730, 740, 1.05, expr="rire", bras="tire", flip=True, **FOURMI))
    S.add(g([cercle(700, 330, 36, "#ffe066"), rect(688, 364, 24, 18, "#adb5bd", rx=4), eclat(700, 330, 1.4, "#ffd43b")]))
    return S


def p06():
    S = Scene()
    macro(S, 7, 700, pente=True)
    S.add(feuille_traineau(260, 710, 0.9))
    S.add(miette(270, 700, 0.8))
    S.add(perso("fourmi", 470, 690, 1.05, expr="joie", bras="bouche", regard=(1, -1), **FOURMI))
    S.add(bulle(560, 190, 420, 100, "À l'aide,\nles amies !", 40, pointe=(500, 440)))
    return S


def p07():
    S = Scene()
    macro(S, 8, 720, pente=True)
    S.add(feuille_traineau(310, 640, 0.9, rot=-18))
    S.add(miette(310, 620, 0.8, rot=-18))
    for k in range(5):
        x = 440 + k * 70
        yb = 720 - (x - 360) ** 1.5 * 0.018 * 1.2
        S.add(perso("fourmi", x, yb, 0.62, expr="rire" if k % 2 else "concentre", bras="tire", rot=-16, **(FOURMI if k == 0 else {})))
    S.add(chemin("M 380 590 Q 560 520 780 380", stroke="#2f9e44", sw=5))
    S.add(texte(250, 240, "Oh, hisse !", 72, "#e8590c", contour="#fff", rot=-10))
    return S


def p08():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff9db")
    sol(S, 640, "#d9a066")
    S.add(fourmiliere(400, 660, 1.1))
    S.add(miette(400, 660, 0.7))
    for k, x in enumerate([120, 230, 570, 680]):
        S.add(perso("fourmi", x, 770, 0.8, expr="miam" if k % 2 else "rire", bras="haut" if k % 2 == 0 else "porte"))
    S.add(perso("fourmi", 400, 780, 1.05, expr="fier", bras="haut", **FOURMI))
    S.add(perso("fourmi", 640, 470, 0.7, expr="content", bras="salut", acc=("couronne",)))
    S.add(texte(400, 150, "Bravo, Fourmi !", 60, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fourmi-seule.svg", vignette),
    ("01-la-miette.svg", p01), ("02-pousser.svg", p02), ("03-rouler.svg", p03),
    ("04-reflechir.svg", p04), ("05-traineau.svg", p05), ("06-a-l-aide.svg", p06),
    ("07-oh-hisse.svg", p07), ("08-festin.svg", p08),
]
