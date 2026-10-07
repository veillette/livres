"""Bibi et Mimi, les contraires — une comptine.

Bibi l'éléphante et Mimi la fourmi sont le contraire l'une de l'autre :
grande et petite, lourd et léger, lent et rapide, chaud et froid, en haut
et en bas, plein et vide, dedans et dehors, bruyant et silencieux, jour et
nuit… et pourtant, amies.
"""
from base import *
from objets import *

ID = "bibi-mimi"
ROSE_ = "#f783ac"


def bibi(x, y, s=1.4, **k):
    return perso("elephant", x, y, s, **{**dict(habit=ROSE_, acc=("noeud",), couleur_acc="#ffd43b"), **k})


def mimi(x, y, s=0.4, **k):
    return perso("fourmi", x, y, s, **{**dict(habit="#ffd43b", acc=("fleur",), couleur_acc="#4dabf7"), **k})


def pre(S, graine=1, haut="#a5d8ff", bas="#fff9db"):
    ciel(S, haut, bas)
    S.add(nuage(140, 100, 0.5), nuage(660, 80, 0.45))
    collines(S, 600, "#b2f2bb", graine=graine)
    sol(S, 640, "#8ce99a")


def etiquette(x, y, mot, couleur="#d6336c", taille=56, rot=0):
    return texte(x, y, mot, taille, couleur, contour="#fff", rot=rot)


def plume_oiseau(x, y, s=1.0, rot=0):
    return place([chemin("M 0 0 Q -30 -60 0 -130 Q 30 -60 0 0 Z", "#e7f5ff", stroke="#a5d8ff", sw=3), trait(0, 10, 0, -120, "#74c0fc", 3)], x, y, s, rot=rot)


def rocher(x, y, s=1.0):
    return place([chemin("M -80 0 Q -90 -70 -30 -86 Q 40 -100 76 -50 Q 92 -10 80 0 Z", "#868e96"),
                  chemin("M -40 -60 Q -20 -70 0 -66", stroke="#adb5bd", sw=6)], x, y, s)


def glace(x, y, s=1.0):
    return place([poly([(-20, -40), (20, -40), (0, 30)], "#e8a200"), cercle(0, -54, 24, "#ffc9c9"), cercle(-6, -64, 6, "#fff", opacity=0.6)], x, y, s)


def seau(x, y, s=1.0, plein=True, couleur="#4dabf7"):
    m = [chemin("M -60 -110 L 60 -110 L 46 0 L -46 0 Z", couleur), chemin("M -60 -110 Q 0 -190 60 -110", stroke="#495057", sw=5, fill="none")]
    if plein:
        m += [ellipse(0, -110, 60, 12, "#74c0fc"), chemin("M -40 -112 q 10 -6 20 0 q 10 6 20 0", stroke="#fff", sw=3)]
    else:
        m.append(ellipse(0, -110, 60, 12, "#1c2a52", opacity=0.6))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    pre(S, 2)
    S.add(bibi(330, 790, 1.9, expr="rire", bras="ouverts"))
    S.add(cercle(590, 710, 70, "#fff", opacity=0.6))
    S.add(mimi(590, 760, 0.55, expr="rire", bras="haut"))
    S.add(coeur(500, 330, 1.4, "#ff6b6b"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bibi(150, 264, 0.95, expr="content", bras="salut"), mimi(300, 264, 0.35, expr="rire", bras="haut"))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(bibi(280, 790, 2.2, expr="fier"))
    S.add(mimi(640, 790, 0.32, expr="content", bras="salut"))
    S.add(etiquette(280, 160, "grande !"), etiquette(640, 600, "petite !", "#f08c00", 44))
    return S


def p02():
    S = Scene()
    pre(S, 2)
    S.add(bibi(260, 790, 1.6, expr="concentre", bras="haut", objet=rocher(0, -190, 1.1)))
    S.add(mimi(620, 790, 0.45, expr="rire", bras="haut"), plume_oiseau(620, 670, 0.8, rot=10))
    S.add(etiquette(260, 140, "lourd !"), etiquette(620, 420, "léger !", "#f08c00", 50))
    return S


def p03():
    S = Scene()
    pre(S, 3)
    S.add(bibi(220, 790, 1.5, expr="dort", bras="bas"), escargot(420, 790, 0.6))
    S.add(mimi(650, 790, 0.45, expr="rire", bras="course"), mouvement(600, 730, 1.0), mouvement(580, 700, 0.8))
    S.add(etiquette(250, 240, "tout doucement…", taille=46), etiquette(640, 520, "vite !", "#f08c00", 56))
    return S


def p04():
    S = Scene()
    pre(S, 4, "#d0ebff", "#fff4e6")
    S.add(bibi(250, 790, 1.5, expr="miam", bras="porte", objet=g([chemin("M -40 -110 L 40 -110 L 32 -50 Q 0 -44 -32 -50 Z", "#ff8787"),
                                                                     chemin(" ".join(f"M {dx} -120 q -10 -18 0 -36 q 10 -18 0 -36" for dx in (-14, 14)), stroke="#fff", sw=5)])))
    S.add(mimi(620, 790, 0.45, expr="miam", bras="tient", objet=glace(68, -150, 1.4)))
    S.add(etiquette(250, 180, "chaud !", "#e03131"), etiquette(620, 440, "froid !", "#1c7ed6", 52))
    return S


def p05():
    S = Scene()
    pre(S, 5)
    S.add(bibi(400, 790, 1.8, expr="rire", bras="haut"))
    S.add(mimi(400, 790 - 210 * 1.8 - 10, 0.4, expr="rire", bras="haut"))
    S.add(etiquette(600, 260, "en haut !", "#f08c00"), etiquette(160, 700, "en bas !"))
    return S


def p06():
    S = Scene()
    pre(S, 6)
    S.add(bibi(110, 790, 0.95, expr="fier", bras="montre"), seau(310, 790, 1.4))
    S.add(seau(560, 790, 0.9, plein=False, couleur="#ffd43b"), mimi(690, 790, 0.45, expr="surpris", bras="joues"))
    S.add(etiquette(310, 360, "plein !"), etiquette(580, 460, "vide !", "#f08c00"))
    return S


def p07():
    S = Scene()
    pre(S, 7)
    S.add(carton(560, 790, 1.4, w=200, h=150, ouvert=True))
    S.add(mimi(560, 640, 0.32, expr="rire", bras="salut"))
    S.add(bibi(230, 790, 1.5, expr="oups", bras="hanches"))
    S.add(etiquette(560, 420, "dedans !", "#f08c00"), etiquette(230, 160, "dehors !"))
    return S


def p08():
    S = Scene()
    pre(S, 8)
    S.add(bibi(260, 790, 1.6, expr="chante"))
    ondes = []
    for k in range(4):
        r = 50 + k * 38
        a1, a2 = math.radians(-50), math.radians(40)
        ondes.append(chemin(f"M {n(330 + r * math.cos(a1))} {n(640 + r * math.sin(a1))} A {r} {r} 0 0 1 {n(330 + r * math.cos(a2))} {n(640 + r * math.sin(a2))}",
                            stroke="#d6336c", sw=8, opacity=0.85 - k * 0.15))
    S.add(g(ondes))
    S.add(texte(420, 220, "POUÊT !", 90, "#d6336c", contour="#fff", rot=-8))
    S.add(mimi(650, 790, 0.45, expr="timide", bras="bouche"), texte(650, 560, "chut…", 34, "#868e96", contour="#fff"))
    return S


def p09():
    S = Scene()
    S.add(rect(0, 0, 400, 800, S.degrade(["#74c0fc", "#fff9db"])), rect(400, 0, 400, 800, S.degrade(["#141c3a", "#5f3dc4"])))
    S.add(soleil(150, 120, 50))
    S.add(lune(660, 120, 40, croissant=True, fond_ciel="#1c2a52"))
    etoiles(S, 25, 8, (420, 0, 800, 450))
    S.add(rect(0, 640, 400, 160, "#8ce99a"), rect(400, 640, 400, 160, "#2f6b4a"))
    S.add(bibi(150, 790, 1.0, expr="rire", bras="haut"), mimi(320, 790, 0.4, expr="rire", bras="haut"), ballon_jeu(240, 520, 30))
    S.add(bibi(560, 790, 1.0, expr="dort"), mimi(720, 790, 0.4, expr="dort"), zzz(620, 520, 0.9, "#e5dbff"))
    S.add(etiquette(200, 330, "le jour !", "#f08c00", 50), texte(600, 330, "la nuit !", 50, "#fff3bf", contour="#1c2a52"))
    S.cachette(240, 492)
    return S


def p10():
    S = Scene()
    pre(S, 9, "#ffdeeb", "#fff9db")
    S.add(bibi(330, 790, 1.8, expr="content", bras="calin"))
    S.add(mimi(400, 640, 0.4, expr="content", bras="calin"))
    S.add(coeur(360, 230, 2.0, "#ff6b6b"), coeur(200, 300, 1.0, "#ffa8a8"), coeur(540, 280, 1.0, "#ffa8a8"))
    S.add(etiquette(600, 520, "amies !", "#d6336c", 64))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bibi-mimi.svg", vignette),
    ("01-grande-petite.svg", p01), ("02-lourd-leger.svg", p02), ("03-lent-vite.svg", p03), ("04-chaud-froid.svg", p04),
    ("05-haut-bas.svg", p05), ("06-plein-vide.svg", p06), ("07-dedans-dehors.svg", p07), ("08-bruyant-silencieux.svg", p08),
    ("09-jour-nuit.svg", p09), ("10-amies.svg", p10),
]
