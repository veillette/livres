"""Max et son ombre — la lumière et les ombres.

L'ombre part toujours du côté opposé au Soleil : longue quand le Soleil est
bas (matin et soir), minuscule quand il est tout en haut (midi). On regarde
vers le sud : le Soleil se lève à gauche (est) et se couche à droite (ouest).
"""
from base import *
from objets import *
from sciences import *

ID = "max-ombre"
MAX = dict(tache=True, acc=("echarpe",), couleur_acc="#fa5252")
MISTIGRI = dict(couleur="#adb5bd", visage="#f1f3f5")


def max_(x=0, y=0, s=1.0, **k):
    return perso("chien", x, y, s, **{**MAX, **k})


def avec_ombre(S, x, y, s, longueur, cote=1, **k):
    """Max et son ombre couchée sur l'herbe."""
    S.add(ombre_portee(S, max_(0, 0, s, **k), x, y, longueur, cote))
    S.add(max_(x, y, s, **k))


def pre(S, haut="#74c0fc", bas="#e7f5ff", graine=1, y=600, bas_soleil=None):
    ciel(S, haut, bas)
    if bas_soleil:
        sx, sy = bas_soleil
        S.add(cercle(sx, sy, 150, "#ffe066", opacity=0.35), soleil(sx, sy, 55, visage=True))
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#7bd88a", y2=y + 90)


def couverture():
    S = Scene()
    pre(S, "#ffc078", "#fff4e6", 2, bas_soleil=(90, 470))
    avec_ombre(S, 250, 730, 1.3, 2.2, 1, expr="rire", bras="salut")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(max_(200, 262, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    pre(S, graine=1)
    S.add(soleil(110, 120, 55, visage=True))
    S.add(barriere(400, 600, 1.0, "#ffffff", 800))
    avec_ombre(S, 270, 730, 1.35, 1.1, 1, expr="surpris", regard=(1, 1), bras="joues")
    S.add(texte(600, 460, "?", 110, "#f76707", contour="#fff"))
    return S


def p02():
    S = Scene()
    pre(S, graine=2)
    S.add(soleil(110, 120, 55, visage=True))
    h, x = 230, 330
    saut = max_(0, -h, 1.25, expr="rire", bras="haut", pieds_haut=True)
    S.add(ombre_portee(S, saut, x, 740, 1.0, 1))
    S.add(max_(x, 740 - h, 1.25, expr="rire", bras="haut", pieds_haut=True))
    S.add(mouvement(x - 90, 740 - h - 150, 1.2), mouvement(x - 90, 740 - h - 60, 1.0))
    S.add(bulle(560, 150, 300, 80, "Qui es-tu ?", 42, pointe=(430, 330)))
    return S


def p03():
    S = Scene()
    pre(S, graine=3)
    sx, sy = 100, 110
    S.add(soleil(sx, sy, 55, visage=True))
    # rayons : l'un passe au ras de la tête et touche le sol au bout de l'ombre
    x, y, s = 400, 700, 1.3
    tete = (400, 700 - 210 * s)
    t = (y - sy) / (tete[1] - sy)
    bout = sx + (tete[0] - sx) * t
    S.add(trait(sx + 40, sy + 40, 250, y, "#fcc419", 5, stroke_dasharray="16 12"))
    S.add(trait(sx + 40, sy + 30, tete[0] - 30, tete[1] + 50, "#fcc419", 5, stroke_dasharray="16 12"))
    S.add(trait(sx + 30, sy + 20, bout, y, "#fcc419", 5, stroke_dasharray="16 12", opacity=0.7))
    S.add(ombre_portee(S, max_(0, 0, s, expr="sourire"), x, y, (bout - x) / (210 * s), 1))
    S.add(max_(x, y, s, expr="sourire", regard=(1, 0)))
    S.add(barriere(690, 560, 0.8, "#c68642", 260))
    S.add(perso("chat", 690, 520, 1.0, expr="sourire", bras="montre", flip=True, regard=(-1, 0), **MISTIGRI))
    return S


def p04():
    S = Scene()
    pre(S, "#ffa94d", "#fff4e6", 4, bas_soleil=(90, 480))
    avec_ombre(S, 290, 720, 1.2, 1.8, 1, expr="rire", regard=(1, 0))
    return S


def p05():
    S = Scene()
    pre(S, "#339af0", "#d0ebff", 5)
    S.add(soleil(400, 90, 60, visage=True))
    S.add(ombre_sous(400, 740, 60, 0.35))
    S.add(max_(400, 740, 1.5, expr="surpris", regard=(0, 1)))
    return S


def p06():
    S = Scene()
    pre(S, "#f76707", "#ffd8a8", 6, bas_soleil=(710, 480))
    avec_ombre(S, 510, 720, 1.2, 1.8, -1, expr="content", regard=(-1, 0))
    return S


def p07():
    S = Scene()
    pre(S, "#adb5bd", "#e9ecef", 7)
    S.add(soleil(560, 150, 55))
    S.add(nuage(540, 170, 1.6, "#ced4da", ombre="#adb5bd"))
    S.add(nuage(200, 120, 0.9, "#dee2e6"))
    S.add(max_(380, 730, 1.4, expr="inquiet", regard=(-1, 1), bras="joues"))
    S.add(texte(180, 440, "?", 90, "#495057", contour="#fff"), texte(600, 480, "?", 70, "#495057", contour="#fff"))
    return S


def p08():
    S = Scene()
    interieur(S, "#ffe8cc", "#c99a6e", y=560)
    S.add(rect(0, 0, 800, 800, "#1c2a52", opacity=0.35))
    # la lampe (à gauche) éclaire Max ; son ombre grandit sur le mur
    S.add(cercle(120, 390, 420, degrade_radial(S, "#fff3bf", "#fff3bf00")))
    S.add(ombre_mur(S, max_(0, 0, 1.0, expr="content", bras="salut"), 620, 560, 1.9, 0.45))
    S.add(table(120, 700, 170, 150, "#a0693a"))
    S.add(lampe(120, 532, 1.2, allumee=False))
    S.add(cercle(120, 390, 28, "#ffe066", opacity=0.8))
    S.add(max_(360, 740, 1.15, expr="content", bras="salut", regard=(1, -1)))
    S.add(fenetre(40, 60, 150, 140, "#1c2a52", nuit_=True))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("max-seul.svg", vignette),
    ("01-decouverte.svg", p01), ("02-saut.svg", p02), ("03-mistigri.svg", p03), ("04-matin.svg", p04),
    ("05-midi.svg", p05), ("06-soir.svg", p06), ("07-nuage.svg", p07), ("08-lampe.svg", p08),
]
