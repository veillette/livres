"""Les trois boucs et le troll — petit, moyen et grand."""
from contes import *

ID = "trois-boucs"
BOUCS = [dict(couleur="#f1e3d3", s=0.7, acc=("noeud",), couleur_acc="#4dabf7"),
         dict(couleur="#d9c2a5", s=0.95, acc=("echarpe",), couleur_acc="#fa5252"),
         dict(couleur="#a68a64", s=1.25)]


def bouc(i, x, y, s=None, **k):
    d = dict(BOUCS[i])
    sc = d.pop("s")
    d.update(k)
    return perso("chevre", x, y, s or sc, **d)


def riviere_pont(S, y_pont=560, troll_=None):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(140, 110, 0.6))
    S.add(chemin("M 460 470 Q 620 260 800 330 L 800 470 Z", "#8ce99a"))
    for k in range(5):
        S.add(fleur(560 + k * 50, 430 - (k % 2) * 30, 0.6, ["#ff8787", "#fcc419"][k % 2]))
    sol(S, 470, "#94d82d")
    S.add(chemin("M 0 800 L 0 640 Q 400 560 800 640 L 800 800 Z", "#4dabf7"))
    for k in range(5):
        S.add(chemin(f"M {80 + k * 150} {700 + (k % 2) * 40} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    if troll_:
        S.add(troll_)
    S.add(pont_bois(400, y_pont, 520))


def couverture():
    S = Scene()
    riviere_pont(S, troll_=troll(400, 800, 1.2, expr="furieux", bras="haut"))
    S.add(bouc(0, 200, 530, 0.8, expr="oups"), bouc(1, 330, 510, 0.9, expr="surpris"), bouc(2, 520, 520, 1.1, expr="fier"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bouc(0, 110, 262, 0.7, expr="content"), bouc(1, 200, 262, 0.85, expr="content"), bouc(2, 300, 262, 1.0, expr="content"))
    return S


def p01():
    S = Scene()
    pre_vert(S)
    S.add(bouc(0, 190, 760, expr="triste"), bouc(1, 390, 770, expr="triste"), bouc(2, 610, 780, expr="triste"))
    S.add(texte(400, 170, "On a faim !", 64, "#5c940d", contour="#fff"))
    return S


def p02():
    S = Scene()
    riviere_pont(S)
    S.add(bouc(0, 70, 560, 0.6, expr="miam"), bouc(1, 170, 560, 0.75, expr="miam"), bouc(2, 110, 790, 1.0, expr="miam", bras="montre"))
    S.add(texte(620, 200, "Miam !", 60, "#2b8a3e", contour="#fff"))
    return S


def p03():
    S = Scene()
    riviere_pont(S, troll_=troll(400, 790, 1.3, expr="fache", bras="croises"))
    S.add(texte(400, 180, "Grrr…", 70, "#2b8a3e", contour="#fff"))
    return S


def p04():
    S = Scene()
    riviere_pont(S, troll_=troll(560, 800, 1.2, expr="furieux", bras="poing"))
    S.add(bouc(0, 360, 520, 0.8, expr="surpris"))
    S.add(texte(220, 380, "Trip, trap !", 44, "#8d5524", contour="#fff"))
    S.add(bulle(500, 140, 460, 100, "Qui marche sur mon pont ?\nJe vais te manger !", 32, pointe=(570, 560)))
    return S


def p05():
    S = Scene()
    riviere_pont(S, troll_=troll(560, 800, 1.2, expr="malin", bras="pense"))
    S.add(bouc(0, 360, 520, 0.8, expr="timide", bras="montre", flip=True))
    S.add(bulle(360, 150, 500, 110, "Attends mon frère,\nil est bien plus gros !", 34, pointe=(360, 360)))
    return S


def p06():
    S = Scene()
    riviere_pont(S, troll_=troll(560, 800, 1.2, expr="furieux", bras="poing"))
    S.add(bouc(0, 740, 360, 0.5, expr="rire", bras="salut"))
    S.add(bouc(1, 360, 520, 1.0, expr="surpris"))
    S.add(texte(200, 330, "TRIP, TRAP !", 44, "#8d5524", contour="#fff"))
    S.add(bulle(470, 130, 440, 90, "Je vais te manger !", 36, pointe=(560, 560)))
    return S


def p07():
    S = Scene()
    riviere_pont(S, troll_=troll(560, 800, 1.2, expr="miam", bras="joues"))
    S.add(bouc(1, 360, 520, 1.0, expr="malin", bras="montre", flip=True))
    S.add(bulle(360, 150, 520, 110, "Mon grand frère est\nencore plus gros !", 34, pointe=(360, 330)))
    return S


def p08():
    S = Scene()
    riviere_pont(S, troll_=troll(560, 800, 1.2, expr="surpris", bras="haut"))
    S.add(bouc(0, 700, 380, 0.45, expr="rire"), bouc(1, 760, 370, 0.5, expr="rire"))
    S.add(bouc(2, 330, 530, 1.3, expr="fier"))
    for k in range(3):
        S.add(trait(120 + k * 260, 520, 150 + k * 260, 540, "#495057", 4), trait(140 + k * 260, 500, 170 + k * 260, 515, "#495057", 4))
    S.add(texte(400, 120, "TRIP ! TRAP ! TRIP ! TRAP !", 44, "#8d5524", contour="#fff"))
    return S


def p09():
    S = Scene()
    riviere_pont(S)
    S.add(troll(560, 560, 1.2, expr="surpris", bras="haut"))
    S.add(bouc(2, 290, 540, 1.3, expr="furieux", bras="course"))
    S.add(mouvement(180, 380, 1.4))
    S.add(bulle(300, 110, 400, 90, "C'est moi, le grand bouc !", 30, pointe=(290, 250)))
    return S


def p10():
    S = Scene()
    riviere_pont(S)
    S.add(troll(640, 330, 0.9, expr="oups", bras="haut", rot=40))
    S.add(texte(620, 150, "BOUM !", 70, "#c92a2a", contour="#fff"))
    S.add(bouc(2, 300, 540, 1.2, expr="fier", bras="hanches"))
    S.add(g([ellipse(660, 700, 90, 22, "#fff", opacity=0.7), texte(660, 780, "PLOUF !", 54, "#1c7ed6", contour="#fff")]))
    return S


def p11():
    S = Scene()
    pre_vert(S, y=520)
    S.add(bouc(0, 190, 740, expr="miam"), bouc(1, 400, 760, expr="miam"), bouc(2, 620, 780, expr="miam"))
    for k in range(6):
        S.add(herbe(90 + k * 130, 790, 1.2))
    S.add(texte(400, 170, "Miam, miam, miam !", 56, "#2b8a3e", contour="#fff"))
    return S


def p12():
    S = Scene()
    pre_vert(S, y=520)
    S.add(bouc(0, 180, 760, 1.0, expr="rire", bras="haut", sy=0.8), bouc(1, 400, 770, 1.3, expr="rire", bras="haut", sy=1.05),
          bouc(2, 630, 780, 1.6, expr="content", bras="haut", sy=1.3))
    S.add(coeur(400, 250, 1.4))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("boucs-seuls.svg", vignette),
    ("01-on-a-faim.svg", p01), ("02-la-colline.svg", p02), ("03-le-troll.svg", p03), ("04-le-petit-bouc.svg", p04),
    ("05-attends-mon-frere.svg", p05), ("06-le-moyen-bouc.svg", p06), ("07-encore-plus-gros.svg", p07),
    ("08-le-grand-bouc.svg", p08), ("09-c-est-moi.svg", p09), ("10-boum.svg", p10), ("11-miam.svg", p11),
    ("12-tout-ronds.svg", p12),
]
