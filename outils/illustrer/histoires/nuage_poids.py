"""Combien pèse un nuage ? — un livre de faits qui monte jusqu'à un grand nombre.

Ordres de grandeur retenus (petit cumulus d'environ 1 km de côté) : environ
0,5 g d'eau par mètre cube, soit à peu près 500 tonnes d'eau, autant que
cent éléphants de 5 tonnes, ou plus de trois mille baignoires de 150 litres.
Une gouttelette de nuage mesure environ un centième de millimètre ; il en
faut à peu près un million pour faire une goutte de pluie. Elles tombent
très lentement et les courants d'air chaud qui montent les retiennent.
"""
from base import *
from objets import *
from sciences import *
from animaux import loupe, etiquette
from fantastique import personne

ID = "nuage-poids"
NOE = dict(peau="claire", cheveux="roux", coiffure="herisses", habit="#4c6ef5", robe=False, jambes="#495057")
PAPI = dict(peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#e8590c", robe=False, jambes="#495057",
            barbe="#e9ecef", acc=("lunettes",))


def noe(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**NOE, **k})


def papi(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**PAPI, **k})


def colline(S, haut="#74c0fc", bas="#e7f5ff", y=620, graine=1):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#7bd88a", y2=y + 80)


def elephant(x, y, s=1.0, **k):
    return perso("elephant", x, y, s, **k)


def baignoire(x, y, s=1.0):
    m = [rect(-70, -60, 140, 50, "#ffffff", rx=22, stroke="#adb5bd", stroke_width=5),
         rect(-60, -54, 120, 14, "#74c0fc", rx=6),
         rect(-58, -12, 14, 12, "#adb5bd", rx=4), rect(44, -12, 14, 12, "#adb5bd", rx=4),
         chemin("M 58 -60 L 58 -84 L 40 -84", stroke="#adb5bd", sw=6)]
    return place(m, x, y, s)


def plume(x, y, s=1.0, rot=0):
    return place([chemin("M 0 60 Q -30 0 0 -60 Q 30 0 0 60 Z", "#e7f5ff", stroke="#a5d8ff", sw=3),
                  trait(0, 80, 0, -50, "#74c0fc", 3)], x, y, s, rot=rot)


def gouttelettes(S, zone, nb=40, graine=1, couleur="#a5d8ff", r=(3, 6)):
    rr = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        S.add(cercle(rr.uniform(x0, x1), rr.uniform(y0, y1), rr.uniform(*r), couleur))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 650, 2)
    S.add(nuage(420, 380, 2.4, "#ffffff", ombre="#dbe4ff"))
    S.add(texte(420, 410, "?", 120, "#4c6ef5"))
    S.add(noe(220, 760, 1.2, expr="surpris", bras="montre", regard=(1, -1)))
    for k, x in enumerate((540, 610, 680)):
        S.add(elephant(x, 760 - (k % 2) * 6, 0.55, expr="content"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(nuage(260, 80, 0.9, "#e7f5ff", ombre="#d0ebff"))
    S.add(noe(120, 262, 1.0, expr="surpris", bras="montre", regard=(1, -1)))
    return S


def p01():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 600, 1)
    S.add(nuage(220, 150, 1.2, "#ffffff", ombre="#dbe4ff"), nuage(580, 230, 1.5, "#ffffff", ombre="#dbe4ff"))
    S.add(papi(560, 760, 1.25, expr="content", regard=(-1, -1)))
    S.add(noe(270, 760, 1.15, expr="surpris", bras="montre", regard=(1, -1)))
    S.add(bulle(250, 360, 360, 80, "Ça pèse combien ?", 38, pointe=(290, 480)))
    return S


def p02():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 600, 2)
    S.add(nuage(620, 120, 1.0, "#ffffff", ombre="#dbe4ff"))
    S.add(pensee(260, 230, 120, g([plume(220, 230, 0.9, -20), perso("chat", 310, 290, 0.45, expr="content")]), depuis=(300, 470)))
    S.add(noe(300, 760, 1.15, expr="concentre", bras="pense", regard=(-1, -1)))
    S.add(papi(580, 760, 1.25, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(600, 330, 300, 80, "Bien plus !", 40, pointe=(590, 470)))
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(nuage(400, 260, 3.0, "#ffffff", ombre="#dbe4ff"))
    zoom = [rect(0, 0, 800, 800, "#e7f5ff")]
    rr = random.Random(5)
    for _ in range(26):
        zoom.append(cercle(rr.uniform(400, 700), rr.uniform(420, 720), rr.uniform(9, 16), "#74c0fc"))
    S.add(loupe(560, 570, 150, g(zoom), rot=130))
    S.add(trait(400, 280, 470, 440, "#495057", 4, stroke_dasharray="10 10"))
    S.add(noe(170, 780, 1.1, expr="bouche_bee", regard=(1, -1)))
    S.add(texte(300, 90, "de l'eau !", 64, "#1c7ed6", contour="#fff"))
    S.cachette(360, 730, "air")
    return S


def p04():
    S = Scene()
    fond(S, "#e7f5ff")
    gouttelettes(S, (60, 200, 360, 600), 160, 3, "#74c0fc", (3, 6))
    S.add(texte(210, 160, "1 000 000", 50, "#1c7ed6"))
    S.add(texte(210, 660, "gouttelettes de nuage", 30, "#495057", poids=600))
    S.add(fleche(400, 400, 500, 400, "#1c7ed6", 9, 26))
    S.add(goutte_perso(640, 470, 1.3, couleur="#339af0", expr="content"))
    S.add(texte(640, 560, "1 goutte de pluie", 32, "#1c7ed6"))
    S.cachette(380, 70, "air")
    return S


def p05():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 640, 3)
    S.add(nuage(400, 230, 5.0, "#ffffff", ombre="#dbe4ff"))
    for k, x in enumerate(range(60, 800, 100)):
        S.add(maison(x, 650 + (k % 2) * 10, 0.45, "#ffe8cc", ("#e8590c", "#c92a2a", "#1971c2")[k % 3]))
    S.add(arbre(30, 700, 0.45), arbre(770, 700, 0.45))
    S.add(noe(400, 790, 0.6, expr="bouche_bee", regard=(0, -1)))
    S.add(trait(80, 470, 720, 470, "#495057", 4, stroke_dasharray="12 10"))
    S.add(etiquette(400, 520, "grand comme tout un village", 34))
    return S


def p06():
    S = Scene()
    fond(S, "#e7f5ff")
    for ligne in range(5):
        for col in range(5):
            S.add(baignoire(110 + col * 145, 200 + ligne * 115, 0.8))
    S.add(texte(400, 100, "des milliers de baignoires !", 46, "#1c7ed6"))
    S.add(texte(400, 770, "… et encore, et encore…", 34, "#495057", poids=600))
    S.cachette(660, 730, "air")
    return S


def p07():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 640, 4)
    S.add(nuage(400, 160, 1.6, "#ffffff", ombre="#dbe4ff"))
    S.add(elephant(180, 720, 1.1, expr="sourire"))
    S.add(texte(180, 420, "1 ?", 70, "#495057", contour="#fff"))
    for k in range(10):
        S.add(elephant(420 + (k % 5) * 75, 640 + (k // 5) * 120, 0.5, expr="content"))
    S.add(texte(570, 400, "10 ?", 70, "#495057", contour="#fff"))
    return S


def p08():
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    S.add(nuage(400, 140, 2.2, "#ffffff", ombre="#dbe4ff"))
    S.add(rect(0, 290, 800, 510, "#8ce99a"))
    for ligne in range(10):
        for col in range(10):
            S.add(elephant(85 + col * 70, 340 + ligne * 47, 0.22, expr="content"))
    S.add(texte(400, 160, "100", 90, "#4c6ef5", contour="#fff"))
    S.cachette(660, 70, "air")
    return S


def p09():
    S = Scene()
    colline(S, "#4dabf7", "#e7f5ff", 640, 5)
    S.add(soleil(90, 90, 45))
    S.add(nuage(420, 200, 2.6, "#ffffff", ombre="#dbe4ff"))
    for x in (200, 420, 640):
        S.add(fleche(x, 600, x, 380, "#ff922b", 8, 26))
    S.add(texte(420, 520, "l'air chaud monte", 40, "#e8590c", contour="#fff"))
    S.add(noe(110, 770, 0.9, expr="content", bras="haut"))
    return S


def p10():
    S = Scene()
    ciel(S, "#868e96", "#ced4da")
    S.add(nuage(250, 140, 2.0, "#adb5bd", ombre="#868e96"), nuage(580, 120, 2.2, "#adb5bd", ombre="#868e96"))
    pluie(S, 70, 7, zone=(0, 200, 800, 700))
    sol(S, 650, "#69db7c", couleur2="#5cc86c", y2=720)
    S.add(parapluie(560, 520, 1.3, "#4c6ef5", "#364fc7"))
    S.add(noe(400, 770, 1.1, expr="rire", bras="haut"))
    S.add(papi(600, 780, 1.15, expr="content", bras="tient", regard=(-1, 0)))
    S.add(flaque(260, 760, 1.2))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(rect(0, 560, 800, 240, "#f8f9fa"))
    for x in (80, 700):
        S.add(sapin(x, 600, 0.9, neige=True))
    flocons(S, 25, 3, zone=(0, 0, 800, 520))
    S.add(noe(320, 770, 1.35, habit="#4c6ef5", expr="souffle", regard=(1, 0)))
    S.add(nuage(470, 570, 0.6, "#ffffff", ombre="#e9ecef", opacity=0.9))
    S.add(texte(520, 450, "Haaa !", 60, "#4c6ef5", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("noe-seul.svg", vignette),
    ("01-la-question.svg", p01), ("02-devine.svg", p02), ("03-de-l-eau.svg", p03),
    ("04-un-million.svg", p04), ("05-un-village.svg", p05), ("06-les-baignoires.svg", p06),
    ("07-un-ou-dix.svg", p07), ("08-cent-elephants.svg", p08), ("09-l-air-chaud.svg", p09),
    ("10-la-pluie.svg", p10), ("11-mon-nuage.svg", p11),
]
