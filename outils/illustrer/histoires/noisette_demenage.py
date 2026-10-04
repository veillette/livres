"""Noisette déménage — Noisette l'écureuil (du « Grand chêne ») change de maison."""
from base import *
from objets import *
from sciences import mesange
from histoires.grand_chene import chene, gland, feuille_chene, pre

ID = "noisette-demenage"


def noisette(x, y, s=1.0, **k):
    return perso("ecureuil", x, y, s, **k)


def maman(x, y, s=1.25, **k):
    return perso("ecureuil", x, y, s, couleur="#c2562a", acc=("echarpe",), couleur_acc="#74c0fc", **k)


def papa(x, y, s=1.3, **k):
    return perso("ecureuil", x, y, s, couleur="#b4531c", acc=("lunettes",), **k)


def plume(x, y, s=1.0, **k):
    return mesange(x, y, s, **k)


def piquant(x, y, s=0.9, **k):
    return perso("herisson", x, y, s, **k)


def boite(x, y, s=1.0, ouverte=True, tresors=True):
    m = [rect(-90, -90, 180, 90, "#e64980", rx=10), rect(-90, -90, 180, 16, "#c2255c", rx=6)]
    for k in range(3):
        m.append(etoile5(-50 + k * 50, -40, 10, "#ffd43b"))
    if ouverte:
        m.insert(0, place(rect(-90, -20, 180, 24, "#f06595", rx=8), 0, -100, rot=-12))
        if tresors:
            m.insert(1, gland(-40, -100, 1.2))
            m.insert(1, place(chemin("M 0 0 Q 10 -50 30 -80 Q 20 -40 0 0", "#339af0"), 10, -90))
            m.insert(1, cercle(50, -96, 16, "#ced4da", stroke="#adb5bd", stroke_width=3))
    return place(m, x, y, s)


def hetre(x, y, s=1.0, creux=True):
    m = [rect(-40, -330, 80, 330, "#adb5bd", rx=20), rect(-24, -300, 12, 260, "#ced4da", rx=6)]
    m += [ellipse(-150, -420, 150, 110, "#69db7c"), ellipse(130, -430, 150, 120, "#51cf66"),
          ellipse(0, -520, 190, 130, "#8ce99a"), ellipse(-20, -380, 150, 90, "#40c057", opacity=0.7)]
    if creux:
        m.append(ellipse(0, -200, 34, 46, "#3b2410"))
    return place(m, x, y, s)


def chambre(S, nuit=False):
    """Intérieur du creux de l'arbre : murs en bois arrondis."""
    fond(S, "#3b2410" if nuit else "#8d5524")
    S.add(ellipse(400, 430, 380, 400, "#5c3a1e" if nuit else "#c68642"))
    S.add(ellipse(400, 430, 330, 350, "#7c4a1e" if nuit else "#e8b07a"))
    S.add(rect(0, 640, 800, 160, "#5c3a1e" if nuit else "#a0693a"))
    for k in range(5):
        S.add(chemin(f"M {80 + k * 160} 640 q 40 -10 80 0", stroke="#3b2410", sw=3, opacity=0.4))


def lit_mousse(x, y, s=1.0, qui=""):
    m = [ellipse(0, 0, 180, 50, "#69db7c"), ellipse(0, -10, 160, 36, "#8ce99a")]
    if qui:
        m.append(qui)
    m.append(chemin("M -110 -20 Q 20 -70 160 -20 Q 40 20 -110 -20", "#ffa8a8"))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    pre(S, graine=2)
    S.add(soleil(690, 100, 45))
    S.add(place(chene(0, 0, 0.55, "ete", visage="content", graine=2), 140, 640))
    S.add(hetre(660, 640, 0.6))
    S.add(chemin("M 220 700 Q 400 640 580 700", stroke="#e9c38c", sw=30))
    S.add(noisette(400, 780, 1.6, expr="sourire", bras="porte", objet=boite(0, -30, 0.55, tresors=False, ouverte=False)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(noisette(200, 264, 1.0, expr="content", bras="porte", objet=boite(0, -30, 0.5, ouverte=False)))
    return S


def p01():
    S = Scene()
    pre(S, graine=1)
    S.add(place(chene(0, 0, 0.9, "ete", visage="sourire", creux=True, graine=1), 220, 700))
    S.add(carton(560, 720, 0.8, couleur="#d9a066"), carton(670, 730, 0.6, couleur="#e9c38c", ouvert=False))
    S.add(maman(470, 780, 1.1, expr="content", bras="calin"))
    S.add(papa(700, 640, 0.8, expr="sourire", bras="porte", objet=carton(0, -40, 0.4, ouvert=False)))
    S.add(noisette(330, 790, 0.95, expr="surpris", bras="joues"))
    return S


def p02():
    S = Scene()
    chambre(S)
    S.add(lit_mousse(250, 690, 0.9))
    S.add(cadre_mur(560, 250, 140, 110, "#a5d8ff"))
    S.add(plume(560, 300, 0.9, expr="sourire"))
    S.add(noisette(450, 790, 1.35, expr="fache", bras="croises"))
    S.add(texte(250, 230, "Je ne pars pas !", 52, "#c92a2a", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(boite(400, 640, 1.8))
    S.add(noisette(160, 790, 1.0, expr="content", bras="donne", regard=(1, 0), objet=""))
    S.add(gland(260, 660, 1.6))
    S.add(paillettes(560, 320), paillettes(260, 360, 0.7))
    return S


def p04():
    S = Scene()
    pre(S, graine=4)
    S.add(place(chene(0, 0, 0.95, "ete", visage="triste", graine=4), 300, 720))
    S.add(noisette(560, 790, 1.15, expr="triste", bras="salut", larmes=True))
    S.add(plume(700, 600, 0.9, expr="triste", ailes="haut"))
    S.add(coeur(640, 420, 0.8, "#ff8787"))
    return S


def p05():
    S = Scene()
    chambre(S, nuit=True)
    S.add(ellipse(640, 220, 60, 70, "#1c2a52"), lune(640, 210, 22))
    S.add(ellipse(400, 720, 240, 60, "#2b8a3e"))
    S.add(noisette(400, 720, 1.0, expr="inquiet", regard=(1, -1), bras="joues"))
    S.add(ellipse(400, 700, 230, 75, "#c2255c"), ellipse(400, 690, 200, 50, "#e64980"))
    S.add(texte(560, 420, "Hou… hou…", 46, "#adb5bd"), texte(180, 360, "Crrr…", 46, "#adb5bd"))
    S.add(rect(0, 0, 800, 800, "#0b1433", opacity=0.25))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(ellipse(640, 220, 60, 70, "#a5d8ff"))
    S.add(cercle(640, 280, 16, "#ced4da", stroke="#adb5bd", stroke_width=3))
    S.add(place(chemin("M 0 0 Q 10 -50 30 -80 Q 20 -40 0 0", "#339af0"), 170, 340, 1.5))
    S.add(lit_mousse(300, 700, 0.9))
    S.add(boite(560, 690, 0.8, tresors=False))
    S.add(noisette(420, 790, 1.2, expr="content", bras="haut", objet=""))
    S.add(gland(550, 470, 1.5))
    return S


def p07():
    S = Scene()
    pre(S, graine=7)
    S.add(hetre(250, 720, 0.9))
    for k in range(18):
        S.add(feuille_chene(420 + (k * 53) % 340, 700 + (k * 37) % 90, 1.1, ["#f76707", "#fab005", "#e03131"][k % 3], rot=k * 40))
    S.add(noisette(500, 760, 1.05, expr="surpris", bras="bas", regard=(1, 0)))
    S.add(piquant(680, 780, 0.95, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(texte(560, 330, "Toc, toc !", 58, "#e8590c", contour="#fff"))
    return S


def dessin(x, y, s=1.0):
    m = [rect(-200, -140, 400, 280, "#fff", rx=8, stroke="#dee2e6", stroke_width=4),
         place(chene(0, 0, 0.22, "ete", visage="sourire", graine=2), -120, 110),
         place(hetre(0, 0, 0.22, creux=False), 120, 110),
         coeur(0, -70, 0.6, "#ff8787")]
    m += [place(perso("ecureuil", 0, 0, 0.24, expr="rire"), -45 + k * 45, 110) for k in range(3)]
    return place(m, x, y, s)


def p08():
    S = Scene()
    chambre(S)
    S.add(dessin(420, 330, 1.1))
    S.add(noisette(220, 790, 1.15, expr="content", bras="tient", objet=""))
    S.add(piquant(590, 790, 0.8, expr="content"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("noisette-seule.svg", vignette),
    ("01-on-demenage.svg", p01), ("02-je-ne-pars-pas.svg", p02), ("03-les-tresors.svg", p03), ("04-au-revoir.svg", p04),
    ("05-la-premiere-nuit.svg", p05), ("06-chez-moi.svg", p06), ("07-piquant.svg", p07), ("08-le-dessin.svg", p08),
]
