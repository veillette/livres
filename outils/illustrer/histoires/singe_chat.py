"""Le Singe et le Chat — se méfier des flatteurs qui veulent se servir de nous."""
from fables import *

ID = "singe-chat"

ROUGE = "#d9480f"


def bertrand(x, y, s=1.0, **k):
    return perso("singe", x, y, s, **k)


def raton(x, y, s=1.0, **k):
    return perso("chat", x, y, s, **k)


def pince(x, y, s=1.0, rot=0, marron_=False):
    """Pince à feu ; (x, y) = bout des mâchoires."""
    m = [trait(-6, 0, -4, -150, "#495057", 7), trait(6, 0, 4, -150, "#495057", 7), cercle(0, -156, 12, "none", stroke="#495057", stroke_width=6)]
    if marron_:
        m.insert(0, marron(0, 6, 0.8, grille=True))
    return place(m, x, y, s, rot=rot)


def cuisine(S, marrons_=5, feu=True):
    interieur(S, "#fff4e6", "#c9a27e", 620, papier="#ffe8cc")
    S.add(cheminee(400, 620, 0.9, feu=feu, marrons_=marrons_))
    S.add(rect(0, 620, 800, 180, "#c9a27e"))
    for k in range(1, 4):
        S.add(trait(0, 620 + k * 50, 800, 620 + k * 50, "#000", 2, opacity=0.06))


def tas_marrons(x, y, n_=4, s=1.0):
    return place([marron(-30 + (k % 3) * 30, -(k // 3) * 22, 1.0, rot=k * 25, grille=True) for k in range(n_)], x, y, s)


def couverture():
    S = Scene()
    cuisine(S)
    S.add(bertrand(170, 770, 1.25, expr="malin", bras="montre", regard=(1, 0)))
    S.add(raton(560, 770, 1.25, expr="oups", bras="haut", regard=(-1, -1)))
    S.add(texte(560, 400, "Aïe !", 50, "#c92a2a", contour="#fff"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bertrand(130, 262, 0.8, expr="malin"))
    S.add(raton(280, 262, 0.8, expr="sourire"))
    return S


def p01():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(300, 140, 200, 170, rideaux="#d9480f"))
    S.add(bertrand(240, 760, 1.4, expr="malin", bras="hanches"))
    S.add(raton(560, 760, 1.4, expr="malin", bras="croises"))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(bertrand(120, 780, 1.1, expr="miam", bras="joues", regard=(1, -1)))
    S.add(raton(680, 780, 1.1, expr="miam", bras="joues", regard=(-1, -1)))
    S.add(chemin("M 360 360 q 10 -20 0 -40 M 400 350 q 10 -20 0 -40 M 440 360 q 10 -20 0 -40", stroke="#dee2e6", sw=6))
    S.add(texte(400, 170, "Mmm ! Ça sent bon !", 46, ROUGE, contour="#fff"))
    return S


def p03():
    S = Scene()
    cuisine(S)
    S.add(bertrand(120, 780, 1.1, expr="inquiet", bras="bas", regard=(1, -1)))
    S.add(raton(680, 780, 1.1, expr="inquiet", bras="bas", regard=(-1, -1)))
    S.add(texte(400, 170, "Que c'est chaud !", 46, "#c92a2a", contour="#fff"))
    return S


def p04():
    S = Scene()
    cuisine(S)
    S.add(bertrand(170, 780, 1.25, expr="malin", bras="montre", regard=(1, 0)))
    S.add(raton(640, 780, 1.15, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(380, 120, 640, 140, "Toi qui as de si belles pattes,\nsi adroites… tire-les du feu !", 32, pointe=(200, 420)))
    S.cachette(80, 420, "air")  # pas dans le feu
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(bertrand(150, 780, 1.1, expr="malin", bras="croises", regard=(1, 0)))
    S.add(raton(600, 780, 1.3, expr="fier", bras="hanches", regard=(-1, 0)))
    S.add(paillettes(720, 380, 1.0))
    S.add(bulle(500, 120, 520, 120, "C'est vrai, je suis\ntrès adroit !", 38, pointe=(600, 440)))
    return S


def p06():
    S = Scene()
    cuisine(S)
    S.add(bertrand(130, 780, 1.1, expr="malin", bras="bas", regard=(1, 0)))
    S.add(raton(560, 780, 1.2, expr="oups", bras="large", regard=(-1, 0), pieds_haut=True))
    S.add(eclat(480, 600, 1.0, "#fa5252"))
    S.add(texte(600, 260, "AÏE !", 60, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    cuisine(S, marrons_=2)
    S.add(raton(560, 780, 1.2, expr="concentre", bras="donne", regard=(-1, 1)))
    S.add(tas_marrons(330, 770, 3, 1.2))
    S.add(bertrand(150, 780, 1.1, expr="miam", bras="bas", regard=(1, 0)))
    S.add(texte(400, 160, "Aïe ! Un… Aïe ! Deux…", 42, ROUGE, contour="#fff"))
    return S


def p08():
    S = Scene()
    cuisine(S, marrons_=1)
    S.add(bertrand(200, 780, 1.3, expr="miam", bras="porte", objet=marron(0, -80, 1.4, grille=True)))
    S.add(raton(600, 780, 1.1, expr="concentre", bras="donne", regard=(-1, 1)))
    S.add(texte(200, 330, "Croc !", 54, ROUGE, contour="#fff"))
    return S


def p09():
    S = Scene()
    cuisine(S, marrons_=0)
    S.add(porte(110, 620, 150, 330, "#8d5524", ouverte=True))
    S.add(personne(150, 780, 1.35, coiffure="chignon", cheveux="chatain", habit="#4dabf7", expr="furieux", bras="hanches"))
    S.add(bertrand(450, 780, 1.0, expr="oups", bras="course", flip=True))
    S.add(raton(650, 780, 1.0, expr="oups", bras="course", flip=True))
    S.add(bulle(380, 120, 560, 120, "Qui a volé\nles marrons ?", 40, pointe=(180, 380)))
    S.cachette(70, 370, "air")
    return S


def p10():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(80, 140, 170, 150, "#ffc078", rideaux="#d9480f"))
    S.add(raton(420, 770, 1.5, expr="pleure", bras="porte"))
    S.add(texte(560, 260, "Ffff… ffff…", 46, ROUGE, contour="#fff"))
    return S


def p11():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(80, 140, 170, 150, "#ffc078", rideaux="#d9480f"))
    S.add(bertrand(250, 770, 1.3, expr="miam", bras="hanches", regard=(1, 0)))
    S.add(raton(560, 770, 1.3, expr="fache", bras="croises", regard=(-1, 0)))
    S.add(texte(250, 330, "Miam !", 46, ROUGE, contour="#fff"))
    return S


def p12():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(80, 140, 170, 150, "#ffc078", rideaux="#d9480f"))
    S.add(bertrand(230, 770, 1.2, expr="timide", bras="calin", regard=(1, 0)))
    S.add(raton(560, 770, 1.35, expr="fache", bras="montre", regard=(-1, 0), flip=True))
    S.add(bulle(500, 130, 560, 150, "Tu m'as fait des compliments\npour que je me brûle\nà ta place !", 32, pointe=(560, 410)))
    return S


def p13():
    S = Scene()
    cuisine(S)
    S.add(bertrand(170, 780, 1.15, expr="malin", bras="montre", regard=(1, 0)))
    S.add(raton(630, 780, 1.2, expr="malin", bras="tient", regard=(-1, 0), objet=None))
    S.add(pince(714, 600, 0.9, rot=-30))
    S.add(bulle(250, 110, 420, 100, "Toi qui as de si\nbelles pattes…", 30, pointe=(190, 400)))
    S.add(bulle(580, 260, 400, 110, "Non merci ! Prenons\nla pince, et partageons.", 28, pointe=(620, 450)))
    S.cachette(80, 420, "air")  # pas dans le feu
    return S


def p14():
    S = Scene()
    cuisine(S, marrons_=0)
    S.add(table(400, 790, 300, 110, nappe="#ffe066"))
    S.add(tas_marrons(400, 662, 5, 1.0))
    S.add(bertrand(120, 780, 1.1, expr="miam", bras="porte", objet=marron(0, -80, 1.2, grille=True)))
    S.add(raton(680, 780, 1.1, expr="miam", bras="porte", objet=marron(0, -80, 1.2, grille=True)))
    S.add(coeur(400, 300, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("singe-et-chat.svg", vignette),
    ("01-deux-coquins.svg", p01), ("02-les-marrons.svg", p02), ("03-que-c-est-chaud.svg", p03),
    ("04-de-si-belles-pattes.svg", p04), ("05-tres-adroit.svg", p05), ("06-aie.svg", p06),
    ("07-un-deux.svg", p07), ("08-croc.svg", p08), ("09-la-servante.svg", p09),
    ("10-pattes-brulees.svg", p10), ("11-miam.svg", p11), ("12-tu-m-as-flatte.svg", p12),
    ("13-la-pince.svg", p13), ("14-on-partage.svg", p14),
]
