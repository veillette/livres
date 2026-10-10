"""Juste une petite bouchée — Sami et Papi font pousser des légumes.

Sami repousse son brocoli : « Beurk, c'est vert ! » Il n'a pas goûté, mais
il sait que ce n'est pas bon. Papi l'emmène au potager : Sami sème des
graines de carottes minuscules, arrose chaque jour, voit les pousses
sortir, et arrache une carotte énorme. Ils cuisinent ensemble ; crounch !
Tout n'est pas délicieux (le radis pique !) : ce n'est pas grave, les goûts
changent, on réessaiera. Et Sami finit par goûter une petite bouchée de
brocoli… avant de servir à toute la famille ses carottes.

Plans : 1 moyen (beurk !) · 2 moyen (tu as goûté ?) · 3 large (le potager)
· 4 gros plan (la graine) · 5 moyen (pousse, pousse !) · 6 moyen (la carotte
énorme) · 7 moyen (on cuisine) · 8 gros plan (crounch !) · 9 moyen (trop
piquant !) · 10 schéma (le tableau des goûts) · 11 gros plan (un petit
arbre) · 12 large (c'est moi qui les ai fait pousser).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne

ID = "sami-legumes"

SAMI = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#fd7e14", robe=False, jambes="#364fc7")
PAPI = dict(stature="ancien", peau="brune", cheveux="blanc", coiffure="chauve_cote", habit="#2f9e44", robe=False, jambes="#795548",
            barbe="#e9ecef", nez="rond", carrure="ronde")
MAMAN = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="chignon", habit="#e64980", robe=True, yeux="cils")
NOUR = dict(stature="petit", peau="brune", cheveux="noir", coiffure="couettes", habit="#ffd43b", robe=True)
ORANGE = "#fd7e14"


def sami(x, y, s=1.45, **k):
    return personne(x, y, s, **{**SAMI, **k})


def papi(x, y, s=1.75, **k):
    return personne(x, y, s, **{**PAPI, **k})


def carotte(x, y, s=1.0, rot=0, fanes=True):
    """Carotte, pointe en bas ; (x, y) = le haut (le collet)."""
    m = []
    if fanes:
        for a in (-30, -10, 10, 30):
            m.append(chemin(f"M 0 0 Q {a * 0.6} -40 {a * 1.4} -80", stroke="#40c057", sw=7))
    m.append(chemin("M -20 0 Q 0 -6 20 0 Q 12 70 0 110 Q -12 70 -20 0 Z", volume(ORANGE, 0.35, 0.8)))
    for k in range(4):
        m.append(trait(-12 + k * 2, 20 + k * 20, -4 + k * 2, 22 + k * 20, _assombrir(ORANGE, 0.75), 2))
    return place(m, x, y, s, rot=rot)


def brocoli(x, y, s=1.0):
    m = [rect(-10, -10, 20, 50, "#8ce99a", rx=8)]
    for px, py, r in ((-22, -22, 20), (0, -34, 24), (22, -22, 20), (-10, -10, 16), (12, -10, 16)):
        m.append(cercle(px, py, r, volume("#2f9e44", 0.35, 0.8)))
    return place(m, x, y, s)


def radis(x, y, s=1.0):
    m = [chemin("M -4 -26 Q -16 -60 -6 -70 M 4 -26 Q 14 -60 8 -72", stroke="#40c057", sw=6),
         cercle(0, 0, 26, volume("#e64980", 0.35, 0.8)), chemin("M -6 24 Q 0 44 2 50", stroke="#fff", sw=3)]
    return place(m, x, y, s)


def tomate_plant(x, y, s=1.0):
    m = [trait(0, 0, 0, -220, "#c68642", 6), trait(-4, -160, 40, -200, "#2f9e44", 5), chemin("M 0 0 Q -20 -100 4 -210", stroke="#2f9e44", sw=8)]
    for px, py in ((-30, -80), (30, -110), (-20, -150), (34, -170), (10, -60)):
        m.append(ellipse(px, py, 30, 16, "#40c057", rot=30 if px > 0 else -30))
    for px, py in ((-14, -110), (20, -140), (14, -76), (-24, -180)):
        m.append(cercle(px, py, 16, volume("#fa5252", 0.4, 0.8)))
    return place(m, x, y, s)


def salade(x, y, s=1.0):
    m = []
    for k in range(7):
        a = k * 51
        m.append(ellipse(math.cos(math.radians(a)) * 18, -20 + math.sin(math.radians(a)) * 8, 26, 20, "#8ce99a", rot=a))
    m.append(cercle(0, -26, 18, volume("#b2f2bb", 0.3, 0.8)))
    return place(m, x, y, s)


def arrosoir(x, y, s=1.0, eau=False, couleur="#4dabf7"):
    m = [rect(-40, -60, 80, 60, volume(couleur, 0.3, 0.8), rx=10), chemin("M 36 -40 L 90 -80", stroke=couleur, sw=10),
         ellipse(94, -84, 10, 7, _assombrir(couleur, 0.8)), chemin("M -36 -60 Q 0 -110 36 -60", stroke=_assombrir(couleur, 0.8), sw=7)]
    if eau:
        for k in range(5):
            m.append(trait(98 + k * 4, -76 + k * 3, 106 + k * 8, -20 + k * 6, "#74c0fc", 3))
    return place(m, x, y, s)


def potager(S, horizon=430):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, horizon, "#b2f2bb", graine=7)
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#8ce99a")))
    S.add(rect(0, 520, 800, 280, "#8d5f3a"))
    for yy in (560, 640, 720):
        S.add(chemin(f"M 0 {yy} Q 400 {yy - 12} 800 {yy}", stroke="#6d4424", sw=6, opacity=0.6))


def cuisine(S):
    piece(S, "cuisine", y=600)
    S.add(fenetre(90, 90, 170, 160, "#a5d8ff", rideaux="#b2f2bb"))
    S.add(rect(470, 70, 280, 130, volume("#d3f9d8", 0.2, 0.85), rx=8), trait(610, 70, 610, 200, "#b2f2bb", 3),
          cercle(590, 150, 6, "#2f9e44"), cercle(630, 150, 6, "#2f9e44"))


def assiette(x, y, s=1.0, contenu=""):
    return place([ellipse(0, 0, 90, 20, "#fff", stroke="#dee2e6", stroke_width=3), ellipse(0, -2, 64, 12, "#f1f3f5"), contenu], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    potager(S, 470)
    for x in (90, 720):
        S.add(tomate_plant(x, 600, 1.1))
    lx, ly, t = 400, 800, 1.8
    S.add(sami(lx, ly, t, expr="rire", bras="montre", regard=(1, -0.5)))
    (_, _), (mx, my) = mains_personne(lx, ly, t, "montre")
    S.add(carotte(mx + 6, my + 6, 1.7))
    S.cachette(720, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(carotte(300, 120, 0.9, rot=20))
    S.add(sami(150, 262, 0.75, expr="content", bras="designe", regard=(1, -0.3)))
    return S


def p01():
    """Plan moyen : à table, Sami repousse son assiette de brocoli, les bras croisés : « Beurk, c'est vert ! »"""
    S = Scene()
    cuisine(S)
    S.add(sami(400, 800, 1.6, expr="degoute", bras="croises", regard=(0, 0.6)))
    S.add(table(400, 800, 420, 115, nappe="#fff3bf"))
    S.add(assiette(400, 668, 1.1, g([brocoli(-24, -8, 0.6), brocoli(20, -10, 0.55)])))
    S.add(bulle(400, 160, 360, 90, "Beurk, c'est vert !", 38, pointe=(400, 290)))
    return S


def p02():
    """Plan moyen : Papi demande « Tu as goûté ? » ; Sami : « Non, mais je sais que ce n'est pas bon ! »"""
    S = Scene()
    cuisine(S)
    S.add(papi(610, 800, 1.75, expr="malin", bras="pense", flip=True, regard=(-1, 0.3)))
    S.add(sami(230, 800, 1.5, expr="fache", bras="croises", regard=(1, -0.2)))
    S.add(table(400, 800, 520, 105, nappe="#fff3bf"))
    S.add(assiette(400, 676, 0.9, g([brocoli(-24, -8, 0.6), brocoli(20, -10, 0.55)])))
    S.add(bulle(590, 150, 260, 80, "Tu as goûté ?", 34, pointe=(600, 290)))
    S.add(bulle(240, 290, 400, 110, "Non, mais je sais\nque ce n'est pas bon !", 30, pointe=(240, 380)))
    return S


def p03():
    """Plan large : au potager de Papi, des tomates, des salades, des fanes de carottes ; Sami ouvre de grands yeux."""
    S = Scene()
    potager(S)
    for x in (70, 170, 640, 740):
        S.add(tomate_plant(x, 560, 0.9))
    for x in range(260, 600, 90):
        S.add(salade(x, 580, 0.8))
    for x in range(40, 800, 70):
        S.add(chemin(f"M {x} 660 q -10 -30 -16 -44 M {x} 660 q 0 -36 2 -50 M {x} 660 q 10 -30 16 -44", stroke="#40c057", sw=5))
    S.add(papi(560, 800, 1.75, expr="content", bras="ouverts", flip=True, regard=(-1, 0.2)))
    S.add(sami(250, 800, 1.45, expr="bouche_bee", bras="bas", regard=(1, -0.4)))
    S.add(texte(400, 120, "Le potager de Papi", 48, "#2b8a3e", contour="#fff"))
    return S


def p04():
    """Gros plan : Sami pose une minuscule graine de carotte au creux de sa main : « C'est tout petit ! »"""
    S = Scene()
    potager(S)
    S.add(sami(360, 880, 2.0, expr="bouche_bee", bras="donne", regard=(1, 0.5)))
    (_, _), (mx, my) = mains_personne(360, 880, 2.0, "donne")
    for k in range(3):
        S.add(ellipse(mx - 10 + k * 12, my - 20 - (k % 2) * 5, 5, 3, "#6d4424"))
    S.add(papi(680, 900, 1.9, expr="content", bras="designe", flip=True, regard=(-1, 0.4)))
    S.camera(1.15, 420, 520)
    S.dessus(bulle(300, 130, 360, 90, "C'est tout petit !", 38, pointe=(330, 250)))
    return S


def p05():
    """Plan moyen : chaque jour, Sami arrose ses rangs ; de petites pousses vertes sortent de la terre : « Pousse, pousse ! »"""
    S = Scene()
    potager(S)
    S.add(soleil(680, 120, 60))
    for x in range(380, 780, 60):
        S.add(chemin(f"M {x} 640 q -8 -16 -14 -22 M {x} 640 q 6 -18 12 -24", stroke="#51cf66", sw=5))
    S.add(sami(230, 800, 1.5, expr="concentre", bras="donne", regard=(1, 0.6),
               objet=place(arrosoir(0, 0, 0.8, eau=True), 76, -50)))
    S.add(texte(500, 160, "Pousse, pousse !", 50, "#2b8a3e", contour="#fff"))
    return S


def p06():
    """Plan moyen : quelques semaines plus tard, Sami tire très fort et arrache une carotte énorme : « Elle est énorme ! »"""
    S = Scene()
    potager(S)
    for x in range(40, 800, 70):
        S.add(chemin(f"M {x} 660 q -10 -30 -16 -44 M {x} 660 q 0 -36 2 -50 M {x} 660 q 10 -30 16 -44", stroke="#40c057", sw=5))
    lx, ly, t = 330, 800, 1.55
    S.add(sami(lx, ly, t, expr="joie", bras="tire", regard=(1, 0.3), pas="marche"))
    (gx, gy), (dx, dy) = mains_personne(lx, ly, t, "tire")
    S.add(carotte(dx + 30, dy, 1.4, rot=-70))
    S.add(papi(640, 800, 1.7, expr="rire", bras="applaudit", flip=True, regard=(-1, 0.3)))
    S.add(texte(400, 140, "Elle est énorme !", 56, ORANGE, contour="#fff"))
    return S


def p07():
    """Plan moyen : à la cuisine, Papi coupe les carottes ; Sami lave les légumes et les met dans le saladier."""
    S = Scene()
    cuisine(S)
    S.add(papi(560, 800, 1.75, expr="content", bras="porte", flip=True, regard=(-1, 0.6)))
    S.add(sami(240, 800, 1.5, expr="concentre", bras="porte", regard=(1, 0.6)))
    S.add(rect(80, 710, 640, 90, volume("#e8c39e", 0.2, 0.85)), rect(70, 690, 660, 26, "#c68642", rx=6))
    S.add(rect(470, 660, 200, 30, "#deb887", rx=6))
    for k in range(5):
        S.add(cercle(500 + k * 26, 670, 11, volume(ORANGE, 0.35, 0.8)))
    S.add(place([chemin("M -70 0 Q -64 -60 0 -60 Q 64 -60 70 0 Z", "#74c0fc")], 260, 690))
    for px, py in ((230, 640), (270, 636), (300, 648)):
        S.add(cercle(px, py, 14, volume(ORANGE, 0.35, 0.8)))
    S.add(salade(250, 654, 0.6))
    return S


def p08():
    """Gros plan : Sami croque un bâtonnet de carotte : « CROUNCH ! »"""
    S = Scene()
    cuisine(S)
    S.add(sami(400, 980, 2.6, expr="miam", bras="bouche", regard=(0, 0)))
    S.add(place([rect(-9, -50, 18, 64, volume(ORANGE, 0.35, 0.8), rx=6)], 420, 690, rot=20))
    S.add(texte(620, 280, "CROUNCH !", 64, ORANGE, contour="#fff"))
    S.cachette(60, 790)
    return S


def p09():
    """Plan moyen : Sami goûte un radis et fait la grimace : « Trop piquant ! » ; Papi rit gentiment."""
    S = Scene()
    cuisine(S)
    S.add(sami(260, 800, 1.55, expr="degoute", bras="bouche", regard=(1, 0)))
    S.add(papi(580, 800, 1.75, expr="rire", bras="donne", flip=True, regard=(-1, 0.3)))
    (gx, gy), (dx, dy) = mains_personne(580, 800, 1.75, "donne", flip=True, stature="ancien", carrure="ronde")
    S.add(radis(gx - 10, gy - 20, 0.8))
    S.add(bulle(250, 160, 290, 90, "Trop piquant !", 38, pointe=(260, 300)))
    S.add(bulle(580, 300, 300, 110, "On réessaiera\nun autre jour !", 30, pointe=(590, 380)))
    return S


def p10():
    """Schéma : le tableau des goûts de Sami, sur le frigo : carotte, tomate, petit pois, salade… et radis « pas encore »."""
    S = Scene()
    fond(S, "#e9ecef")
    S.add(rect(120, 60, 560, 700, "#f8f9fa", stroke="#ced4da", stroke_width=6, rx=24))
    S.add(rect(170, 110, 460, 600, "#fff", stroke="#adb5bd", stroke_width=3), cercle(400, 110, 14, "#fa5252"))
    S.add(texte(400, 180, "Mes goûts", 44, "#1c7ed6"))
    lignes = [("carotte", True), ("tomate", True), ("salade", True), ("brocoli", None), ("radis", False)]
    for k, (nom, aime) in enumerate(lignes):
        y = 270 + k * 95
        if nom == "carotte":
            S.add(carotte(240, y - 30, 0.45, rot=-60))
        elif nom == "tomate":
            S.add(cercle(240, y, 26, volume("#fa5252", 0.4, 0.8)))
        elif nom == "salade":
            S.add(salade(240, y + 20, 0.6))
        elif nom == "brocoli":
            S.add(brocoli(240, y + 10, 0.6))
        else:
            S.add(radis(240, y, 0.7))
        S.add(texte(370, y + 12, nom, 34, "#495057"))
        if aime is True:
            S.add(cercle(560, y, 28, "#ffd43b"), chemin(f"M 546 {y + 4} Q 560 {y + 18} 574 {y + 4}", stroke=ENCRE, sw=3),
                  cercle(550, y - 8, 3, ENCRE), cercle(570, y - 8, 3, ENCRE))
        elif aime is False:
            S.add(texte(560, y + 10, "pas encore", 24, "#e8590c"))
        else:
            S.add(texte(560, y + 12, "?", 40, "#1c7ed6"))
    S.cachette(740, 790)
    return S


def p11():
    """Gros plan : Sami tient un brocoli sur sa fourchette et le regarde : « On dirait un petit arbre… »"""
    S = Scene()
    cuisine(S)
    lx, ly, t = 380, 960, 2.4
    S.add(sami(lx, ly, t, expr="concentre", bras="tient", regard=(1, -0.3)))
    (_, _), (mx, my) = mains_personne(lx, ly, t, "tient")
    S.add(trait(mx, my, mx + 20, my - 90, "#adb5bd", 6), brocoli(mx + 24, my - 110, 1.3))
    S.add(bulle(560, 160, 420, 110, "On dirait un petit arbre…\nHmm… pas mal !", 32, pointe=(560, 290)))
    S.cachette(60, 790)
    return S


def p12():
    """Plan large : à table, Sami sert ses carottes à toute la famille : « C'est moi qui les ai fait pousser ! »"""
    S = Scene()
    cuisine(S)
    S.add(personne(130, 800, 1.65, expr="content", bras="applaudit", regard=(1, 0), **MAMAN))
    S.add(papi(670, 800, 1.7, expr="rire", bras="bas", flip=True, regard=(-1, 0.3)))
    S.add(personne(530, 800, 1.2, expr="rire", bras="haut", flip=True, regard=(-1, 0), **NOUR))
    S.add(sami(330, 800, 1.5, expr="fier", bras="porte", regard=(1, 0),
               objet=place(assiette(0, 0, 0.8, g([carotte(-20, -10, 0.3, rot=-80, fanes=False), carotte(10, -14, 0.3, rot=-70, fanes=False)])), 0, -128)))
    S.add(table(400, 800, 560, 120, nappe="#fff3bf"))
    S.add(assiette(250, 670, 0.6), assiette(560, 670, 0.6))
    S.add(bulle(400, 160, 470, 110, "C'est moi qui les ai\nfait pousser !", 34, pointe=(360, 300)))
    S.cachette(400, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("sami-seul.svg", vignette),
    ("01-beurk.svg", p01), ("02-tu-as-goute.svg", p02), ("03-le-potager.svg", p03),
    ("04-la-graine.svg", p04), ("05-pousse.svg", p05), ("06-la-carotte.svg", p06),
    ("07-on-cuisine.svg", p07), ("08-crounch.svg", p08), ("09-trop-piquant.svg", p09),
    ("10-mes-gouts.svg", p10), ("11-un-petit-arbre.svg", p11), ("12-c-est-moi.svg", p12),
]
