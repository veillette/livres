"""La semaine de Petit Hérisson — comptine des jours de la semaine.

Chaque page montre un jour, avec un petit calendrier dans le coin où le jour
du moment est entouré.
"""
from base import *
from objets import *
import math

ID = "semaine-herisson"
JOURS = ["L", "M", "M", "J", "V", "S", "D"]
COULEURS = ["#4dabf7", "#ff8787", "#69db7c", "#ffa94d", "#cc5de8", "#3bc9db", "#ffd43b"]


def herisson(x, y, s=1.0, **k):
    k.setdefault("habit", "#4c6ef5")
    return perso("herisson", x, y, s, **k)


def mamie(x, y, s=1.2, **k):
    return perso("herisson", x, y, s, couleur="#c9a27e", habit="#e64980", acc=("lunettes", "tablier"), **k)


def papa(x, y, s=1.3, **k):
    return perso("herisson", x, y, s, habit="#2f9e44", **k)


def calendrier(jour, x=650, y=40):
    """Bande des sept jours ; `jour` = 0 (lundi) à 6 (dimanche)."""
    m = [rect(x - 140, y, 280, 54, "#fff", rx=14, opacity=0.92)]
    for k, l in enumerate(JOURS):
        cx = x - 120 + k * 40
        if k == jour:
            m.append(cercle(cx, y + 27, 20, COULEURS[jour]))
        m.append(texte(cx, y + 38, l, 28, "#fff" if k == jour else "#868e96"))
    return g(m)


def bottes(x, y, s=1.0, couleur="#fab005"):
    return place([rect(-40, -36, 30, 36, couleur, rx=6), rect(10, -36, 30, 36, couleur, rx=6)], x, y, s)


def p01():
    S = Scene()
    ciel(S, "#adb5bd", "#dee2e6")
    S.add(nuage(200, 120, 1.0, "#ced4da"), nuage(560, 100, 1.2, "#ced4da"))
    collines(S, 560, "#8ce99a", graine=1)
    sol(S, 600, "#69db7c")
    pluie(S, 70, 1, (0, 0, 800, 600))
    S.add(flaque(400, 740, 2.2, eclabousse=True))
    S.add(herisson(400, 740, 1.4, expr="rire", bras="haut", habit="#fab005"))
    S.add(bottes(400, 742, 1.4))
    S.add(texte(160, 300, "Floc !", 70, "#1c7ed6", contour="#fff", rot=-10))
    S.add(calendrier(0))
    return S


def p02():
    S = Scene()
    interieur(S, "#fff0f6", "#c68642", 600, papier="#ffdeeb")
    S.add(fenetre(80, 110, 150, 140, "#a5d8ff", rideaux="#ffc9c9"))
    S.add(mamie(600, 720, 1.4, expr="content", bras="bas", regard=(-1, 0.3)))
    S.add(herisson(260, 720, 1.1, expr="miam", bras="joues"))
    S.add(table(420, 790, 520, 140, "#a0693a", nappe="#fff"))
    S.add(gateau(420, 640, 1.3, couleur="#f8c291", fruits="#fa5252", fumee=True))
    S.add(calendrier(1))
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(110, 110, 45))
    collines(S, 560, "#b2f2bb", graine=3)
    sol(S, 600, "#8ce99a")
    S.add(rect(0, 660, 800, 70, "#e9c38c"))
    S.add(arbre(700, 610, 0.9), arbre(120, 610, 0.7))
    S.add(herisson(388, 610, 0.9, bras="guidon", expr="rire", regard=(1, 0)))
    S.add(velo(400, 718, 1.15, "#4dabf7", roues_mvt=True))
    S.add(mouvement(230, 620, 1.2), texte(560, 330, "Drelin !", 64, "#1c7ed6", contour="#fff", rot=-6))
    S.add(calendrier(2))
    return S


def etal(S, y=560):
    S.add(rect(80, y, 640, 180, "#c68642", rx=10))
    S.add(rect(70, 160, 20, 420, "#a0693a"), rect(710, 160, 20, 420, "#a0693a"))
    for k in range(8):
        S.add(chemin(f"M {60 + k * 85} 150 L {145 + k * 85} 150 L {145 + k * 85} 210 Q {102 + k * 85} 240 {60 + k * 85} 210 Z",
                     "#fa5252" if k % 2 else "#fff"))
    for k in range(5):
        S.add(cercle(150 + k * 30, y - 10, 16, "#e64980"), trait(150 + k * 30, y - 26, 150 + k * 30, y - 46, "#2f9e44", 5))
    for k in range(6):
        S.add(poly([(480 + k * 32, y - 30), (500 + k * 32, y - 30), (490 + k * 32, y)], "#fa5252"), cercle(490 + k * 32, y - 30, 8, "#2f9e44"))
    S.add(fleur(380, y, 1.0, "#ff922b", tige=70), fleur(410, y, 1.0, "#cc5de8", tige=90), fleur(440, y, 1.0, "#ffd43b", tige=75))


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 740, "#ced4da", bosse=0)
    etal(S, 560)
    S.add(papa(150, 790, 1.15, expr="sourire", bras="bas", regard=(1, -0.3)))
    S.add(herisson(560, 790, 0.95, expr="joie", bras="montre", regard=(-1, -1)))
    S.add(calendrier(3))
    return S


def chevalet(x, y, s=1.0, dessin=""):
    m = [trait(-110, 0, -20, -420, "#a0693a", 12), trait(110, 0, 20, -420, "#a0693a", 12), trait(0, 0, 0, -380, "#a0693a", 10),
         rect(-130, -400, 260, 230, "#fff", stroke="#dee2e6", stroke_width=4), rect(-140, -170, 280, 14, "#a0693a")]
    if dessin:
        m.append(dessin)
    return place(m, x, y, s)


def p05():
    S = Scene()
    interieur(S, "#f3f0ff", "#c68642", 600, papier="#e5dbff")
    S.add(chevalet(520, 760, 1.1, oiseau(0, -230, 0.9, couleur="#4dabf7", ventre="#ffe066")))
    S.add(herisson(220, 770, 1.15, expr="fier", bras="tient", objet="", habit="#cc5de8"))
    S.add(pinceau(300, 520, 1.3, "#4dabf7", rot=30))
    S.add(pot_peinture(380, 780, 0.9, "#4dabf7"), pot_peinture(660, 790, 0.7, "#ffd43b"))
    S.add(calendrier(4))
    return S


def p06():
    S = Scene()
    fond(S, "#e3fafc")
    S.add(rect(0, 260, 800, 40, "#dee2e6"))
    S.add(rect(0, 300, 800, 500, "#3bc9db"))
    for k in range(6):
        S.add(chemin(f"M {40 + k * 140} {360 + (k % 2) * 60} q 30 -14 60 0", stroke="#99e9f2", sw=6))
    S.add(herisson(400, 640, 1.4, expr="rire", bras="haut", habit="#fa5252"))
    for sgn in (-1, 1):
        S.add(ellipse(400 + sgn * 98, 640 - 205, 26, 18, "#ff922b", stroke="#e8590c", stroke_width=3))
    S.add(rect(0, 520, 800, 280, "#3bc9db", opacity=0.75))
    S.add(poisson(140, 640, 0.8, "#ffd43b"))
    S.add(texte(620, 200, "Splash !", 64, "#1098ad", contour="#fff", rot=-6))
    S.add(calendrier(5))
    return S


def p07():
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    S.add(soleil(110, 110, 45, visage=True))
    collines(S, 540, "#b2f2bb", graine=7)
    sol(S, 580, "#8ce99a")
    S.add(arbre(700, 590, 1.0))
    S.add(tapis(400, 720, 330, 70, "#ffc9c9", "#ff8787"))
    S.add(perso("lapin", 170, 720, 0.9, expr="rire", habit="#69db7c"), perso("souris", 640, 720, 0.7, expr="rire", habit="#ffd43b"),
          perso("ecureuil", 520, 700, 0.8, expr="chante", bras="haut"))
    S.add(herisson(320, 730, 1.0, expr="rire", bras="porte", objet=tasse(0, -40, 1.6, "#4dabf7")))
    S.add(gateau(420, 745, 0.7, fruits="#fa5252"))
    S.add(notes(560, 380, 1.1, "#e8590c"))
    S.add(calendrier(6))
    return S


def p08():
    S = Scene()
    interieur(S, "#1c2a52", "#5c3a1e", 600, papier="#24325e")
    S.add(fenetre(90, 110, 150, 140, "#1c2a52", nuit_=True))
    S.add(lit(450, 790, 440, "#74c0fc", "#4dabf7"))
    S.add(herisson(310, 700, 0.75, expr="dort"))
    S.add(rect(290, 655, 390, 95, "#4dabf7", rx=18))
    S.add(zzz(420, 420, 1.2, "#fff3bf"))
    # le calendrier accroché au mur : lundi revient
    S.add(calendrier(0, 560, 200))
    return S


def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    S.add(soleil(680, 120, 50, visage=True))
    collines(S, 560, "#b2f2bb", graine=8)
    sol(S, 600, "#8ce99a")
    for k, c in enumerate(COULEURS):
        a = -150 + k * 50
        x = 400 + 290 * math.sin(math.radians(a))
        y = 470 - 290 * math.cos(math.radians(a))
        S.add(cercle(x, y, 38, c), texte(x, y + 13, JOURS[k], 38, "#fff"))
    S.add(herisson(400, 760, 1.6, expr="rire", bras="ouverts"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(herisson(200, 264, 1.0, expr="content", bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("herisson-seul.svg", vignette),
    ("01-lundi.svg", p01), ("02-mardi.svg", p02), ("03-mercredi.svg", p03), ("04-jeudi.svg", p04),
    ("05-vendredi.svg", p05), ("06-samedi.svg", p06), ("07-dimanche.svg", p07), ("08-et-lundi.svg", p08),
]
