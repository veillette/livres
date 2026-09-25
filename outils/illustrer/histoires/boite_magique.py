"""La boîte de Titou — l'imagination."""
from base import *
from objets import *

ID = "boite-magique"
TITOU = dict()
PAPA = dict(acc=("lunettes",), habit="#74c0fc")
CARTON = "#d9a066"


def salon(S):
    interieur(S, "#fff4e6", "#c9a47e", 600, papier="#ffe8cc")
    S.add(fenetre(90, 110, 160, 150, "#a5d8ff", rideaux="#ff8787"))


def dans_boite(x, y, s, expr, bras="haut", w=240, h=130, dessin="", derriere="", devant="", **kw):
    """Titou assis dans une boîte : on ne voit que le haut du corps."""
    corps = perso("panda", x, y - h * s * 0.55, s, expr=expr, bras=bras, **kw)
    return g([derriere, corps, carton(x, y, s, w, h, ouvert=False, dessin=dessin), devant])


def ailerons(x, y, s, w):
    return g([poly([(x - w / 2 * s, y), (x - w / 2 * s - 50 * s, y + 10 * s), (x - w / 2 * s, y - 90 * s)], "#fa5252"),
              poly([(x + w / 2 * s, y), (x + w / 2 * s + 50 * s, y + 10 * s), (x + w / 2 * s, y - 90 * s)], "#fa5252")])


def bouilloire(x, y, s=1.0):
    return place([rect(-40, -80, 80, 80, "#adb5bd", rx=16), chemin("M 40 -60 Q 70 -40 40 -20", stroke="#868e96", sw=8),
                   poly([(-40, -60), (-70, -80), (-40, -40)], "#adb5bd"), rect(-20, -96, 40, 18, "#495057", rx=6)], x, y, s)


def couverture():
    S = Scene()
    ciel(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 40, 3, (0, 0, 800, 800))
    S.add(ailerons(400, 700, 1.3, 200))
    flammes = g([ellipse(400, 760, 50, 70, "#ffa94d"), ellipse(400, 750, 28, 44, "#ffe066")])
    S.add(flammes)
    S.add(dans_boite(400, 700, 1.3, "rire", bras="haut", w=200, h=160, acc=("casque",), couleur_acc="#4dabf7",
                     dessin=cercle(0, -80, 30, "#a5d8ff", stroke="#fff", stroke_width=6)))
    S.add(lune(640, 180, 50), paillettes(180, 420))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(dans_boite(200, 262, 0.85, "content", bras="salut", w=200, h=110))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(bouilloire(160, 720, 1.0))
    S.add(perso("panda", 250, 760, 1.6, expr="sourire", bras="porte", regard=(-1, 0), **PAPA))
    S.add(carton(520, 750, 1.3, 220, 160, ouvert=True))
    S.add(perso("panda", 660, 770, 1.3, expr="bouche_bee", bras="joues", regard=(-1, 0.3)))
    S.add(paillettes(560, 440), paillettes(700, 380, 0.8))
    return S


def p02():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 560, 800, 240, "#495057"))
    for k in range(6):
        S.add(rect(k * 160 - 40, 670, 90, 14, "#fff"))
    S.add(g([rect(620, 470, 20, 90, "#fff"), rect(600, 440, 60, 40, "#fff"), rect(600, 440, 30, 20, ENCRE), rect(630, 460, 30, 20, ENCRE)]))
    roues = cercle(-70, 0, 34, ENCRE) + cercle(70, 0, 34, ENCRE) + cercle(-70, 0, 14, "#adb5bd") + cercle(70, 0, 14, "#adb5bd")
    S.add(dans_boite(360, 700, 1.4, "rire", bras="porte", w=240, h=110, acc=("casque",), couleur_acc="#fa5252",
                     dessin=place(roues, 0, 0, 1.0) + texte(0, -40, "1", 48, "#fa5252"),
                     devant=cercle(360, 580, 26, "none", stroke="#495057", stroke_width=8)))
    for k in range(3):
        S.add(trait(120, 560 + k * 40, 30, 560 + k * 40, "#fff", 8))
    S.add(texte(560, 220, "Vroum !", 90, "#fa5252", contour="#fff", rot=-8))
    return S


def p03():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff4e6")
    S.add(soleil(640, 150, 60))
    eau(S, 560, "#1c7ed6", "#4dabf7")
    mat = g([trait(560, 640, 560, 230, "#8d5524", 10),
             poly([(566, 240), (720, 280), (566, 340)], "#343a40"),
             cercle(620, 290, 14, "#fff"), trait(606, 310, 634, 310, "#fff", 4)])
    S.add(mat)
    S.add(dans_boite(400, 680, 1.4, "malin", bras="montre", w=260, h=120, acc=("chapeau",), couleur_acc="#343a40"))
    S.add(texte(210, 260, "À l'abordage !", 50, "#343a40", contour="#fff", rot=-6))
    return S


def p04():
    S = Scene()
    ciel(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 50, 4, (0, 0, 800, 800))
    S.add(lune(150, 150, 70, visage=True))
    S.add(g([ellipse(560, 780, 60, 90, "#ffa94d"), ellipse(560, 770, 34, 56, "#ffe066")]))
    S.add(ailerons(560, 700, 1.3, 180))
    S.add(dans_boite(560, 700, 1.3, "rire", bras="haut", w=180, h=200, acc=("casque",), couleur_acc="#4dabf7",
                     dessin=cercle(0, -110, 34, "#a5d8ff", stroke="#fff", stroke_width=6)))
    S.add(texte(250, 560, "3, 2, 1…", 60, "#ffe066"), texte(250, 640, "Décollage !", 56, "#ffe066"))
    return S


def p05():
    S = Scene()
    salon(S)
    S.add(rect(420, 560, 120, 190, "#3d2410", rx=10))
    S.add(perso("panda", 480, 800, 0.95, expr="malin", bras="salut", regard=(-1, 0)))
    boite = g([rect(-180, -320, 360, 320, CARTON), rect(-180, -320, 360, 14, assombrir(CARTON, 0.85)),
               rect(-160, -290, 170, 60, "#fff", rx=6), texte(-75, -266, "Interdit", 26, "#e03131"), texte(-75, -240, "aux grands !", 22, "#e03131")])
    cid = uid("c")
    S.add(el("clipPath", chemin("M 0 0 L 800 0 L 800 800 L 0 800 Z M 420 560 L 420 750 L 540 750 L 540 560 Z", "#000", fill_rule="evenodd"), id=cid))
    S.add(g(place(boite, 480, 760, 1.0), clip_path=f"url(#{cid})"))
    S.add(perso("panda", 170, 770, 1.6, expr="rire", bras="bouche", regard=(1, 0), **PAPA))
    return S


def p06():
    S = Scene()
    salon(S)
    tete = g([rect(-80, -250, 160, 140, CARTON, rx=6), rect(-50, -220, 36, 36, "#fff"), rect(14, -220, 36, 36, "#fff"),
              cercle(-32, -202, 10, ENCRE), cercle(32, -202, 10, ENCRE), rect(-40, -160, 80, 16, "#fa5252", rx=6),
              trait(0, -250, 0, -290, "#495057", 5), cercle(0, -296, 10, "#fa5252")])
    corps = perso("panda", 0, 0, 1.0, expr="rire", bras="ouverts")
    S.add(place(corps + tete, 400, 770, 1.6))
    S.add(texte(620, 220, "Bip bip !", 64, "#1c7ed6", contour="#fff", rot=8))
    S.add(texte(640, 560, "Je suis", 40, "#1c7ed6", contour="#fff"), texte(640, 610, "un robot !", 40, "#1c7ed6", contour="#fff"))
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(place(g([poly([(-150, 0), (-170, -80), (-40, -110), (20, -60), (150, -90), (170, 0)], CARTON),
                   trait(-120, -40, 60, -70, assombrir(CARTON, 0.8), 4), trait(-60, -90, -20, -10, assombrir(CARTON, 0.8), 4)]), 520, 760, 1.2))
    S.add(perso("panda", 250, 770, 1.5, expr="triste", bras="bas", regard=(1, 0.5)))
    S.add(bulle(260, 200, 330, 90, "Elle est fichue…", 38, pointe=(260, 380)))
    return S


def p08():
    S = Scene()
    salon(S)
    fenetres = cercle(-140, -200, 44, "#a5d8ff", stroke="#fff", stroke_width=8) + cercle(0, -200, 44, "#a5d8ff", stroke="#fff", stroke_width=8) + cercle(140, -200, 44, "#a5d8ff", stroke="#fff", stroke_width=8)
    S.add(perso("panda", 290, 560, 1.4, expr="rire", bras="haut", **PAPA))
    S.add(perso("panda", 510, 560, 1.1, expr="rire", bras="haut"))
    S.add(carton(400, 790, 1.0, 640, 340, ouvert=True, dessin=fenetres + texte(0, -70, "TITOU-1", 50, "#1c7ed6")))
    S.add(bulle(400, 110, 520, 100, "Un vaisseau spatial\npour deux !", 38))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("titou-seul.svg", vignette),
    ("01-le-colis.svg", p01), ("02-voiture.svg", p02), ("03-bateau.svg", p03),
    ("04-fusee.svg", p04), ("05-cabane.svg", p05), ("06-robot.svg", p06),
    ("07-cabossee.svg", p07), ("08-pour-deux.svg", p08),
]
