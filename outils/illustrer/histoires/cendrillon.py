"""Cendrillon — la bonté finit toujours par se voir."""
from contes import *

ID = "cendrillon"
CENDRILLON = dict(coiffure="longs", cheveux="blond", peau="claire", habit="#ced4da", chaussures="#868e96")
BAL = dict(habit="#74c0fc", motif_robe="#e7f5ff", acc=("diademe",), chaussures="#d0ebff")
SOEURS = [dict(coiffure="chignon", cheveux="roux", peau="claire", habit="#e64980", acc=("noeud",), couleur_acc="#ffd43b"),
          dict(coiffure="boucles", cheveux="noir", peau="doree", habit="#fab005", acc=("fleur",), couleur_acc="#e64980")]
BELLE_MERE = dict(coiffure="chignon", cheveux="gris", peau="rosee", habit="#5f3dc4", acc=("lunettes",))
PRINCE = dict(coiffure="courts", cheveux="brun", peau="brune", habit="#1864ab", robe=False, jambes="#f8f9fa", cape="#c92a2a", acc=("couronne",))
FEE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#b197fc", ailes="#e5dbff", motif_robe="#fff")


def cendrillon(x, y, s=1.0, bal=False, **k):
    d = dict(CENDRILLON)
    if bal:
        d.update(BAL)
    d.update(k)
    return personne(x, y, s, **d)


def soeur(i, x, y, s=1.0, **k):
    return personne(x, y, s, **{**SOEURS[i], **k})


def belle_mere(x, y, s=1.0, **k):
    return personne(x, y, s, **{**BELLE_MERE, **k})


def prince(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PRINCE, **k})


def fee(x, y, s=1.0, **k):
    k.setdefault("bras", "tient")
    k.setdefault("objet", baguette(68, -146, 0.9, rot=20))
    return personne(x, y, s, **{**FEE, **k})


def souris_(x, y, s=0.4, **k):
    return perso("souris", x, y, s, **k)


def cuisine(S, feu=True):
    interieur(S, "#e9ecef", "#adb5bd", 580, plinthe="#868e96")
    S.add(rect(480, 260, 260, 320, "#868e96"), rect(510, 380, 200, 200, "#343a40"))
    if feu:
        S.add(chemin("M 540 580 Q 540 500 580 480 Q 590 530 610 460 Q 640 520 650 490 Q 690 520 680 580 Z", "#ff922b"))
    S.add(fenetre(90, 110, 150, 140, dehors="#364fc7", nuit_=True))


def salon(S):
    interieur(S, "#fff0f6", "#c9a27e", 580, papier="#fcc2d7")
    S.add(fenetre(560, 110, 170, 150, dehors="#a5d8ff", rideaux="#e64980"))
    S.add(cadre_mur(90, 120))


def couverture():
    S = Scene()
    salle_bal(S)
    S.add(horloge_minuit(400, 350, 50))
    S.add(prince(250, 790, 1.35, expr="content", bras="donne", regard=(1, 0)))
    S.add(cendrillon(530, 790, 1.4, bal=True, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    S.add(pantoufle_verre(400, 780, 0.9))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pantoufle_verre(200, 200, 2.2))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(cendrillon(400, 790, 1.3, expr="triste", bras="tient", objet=balai(68, -30, 0.8, rot=15)))
    S.add(belle_mere(150, 790, 1.2, expr="fache", bras="montre"))
    S.add(soeur(0, 600, 790, 1.1, expr="malin", bras="croises"), soeur(1, 710, 790, 1.0, expr="rire", bras="bouche"))
    return S


def p02():
    S = Scene()
    salon(S)
    S.add(soeur(0, 190, 790, 1.2, expr="rire", bras="haut"), soeur(1, 380, 790, 1.2, expr="rire", bras="haut"))
    S.add(place(g([rect(-50, -34, 100, 68, "#fff", stroke="#e9ecef", stroke_width=3), poly([(-50, -34), (0, 6), (50, -34)], "#f1f3f5"), cercle(0, 6, 10, "#c92a2a")]), 290, 330))
    S.add(cendrillon(620, 790, 1.2, expr="inquiet", bras="pense"))
    S.add(bulle(560, 140, 300, 90, "Et moi ?", 40, pointe=(610, 460)))
    return S


def p03():
    S = Scene()
    cuisine(S)
    S.add(cendrillon(300, 790, 1.35, expr="pleure", larmes=True))
    S.add(souris_(110, 790, 0.45, expr="triste"), souris_(190, 800, 0.4, expr="triste"), souris_(430, 800, 0.4, expr="triste"))
    return S


def p04():
    S = Scene()
    cuisine(S, feu=False)
    S.add(etincelles(520, 400, 2.4, graine=5))
    S.add(fee(520, 790, 1.35, expr="rire", bras="tient"))
    S.add(cendrillon(220, 790, 1.2, expr="bouche_bee", bras="joues"))
    S.add(bulle(420, 120, 460, 100, "Tu iras au bal,\nma chérie !", 36, pointe=(500, 440)))
    return S


def p05():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=5)
    sol(S, 640, "#2f9e44")
    S.add(carrosse(330, 760, 0.95))
    S.add(fee(100, 790, 1.0, expr="rire", bras="tient", objet=baguette(68, -146, 0.9, rot=40)))
    S.add(etincelles(330, 500, 2.2, graine=9))
    S.add(texte(400, 120, "Pouf !", 80, "#ffd43b", contour="#5f3dc4"))
    return S


def p06():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=6)
    sol(S, 640, "#2f9e44")
    S.add(etincelles(400, 520, 2.6, graine=11))
    S.add(cendrillon(400, 790, 1.5, bal=True, expr="rire", bras="ouverts"))
    S.add(fee(150, 790, 1.0, expr="sourire", bras="tient"))
    S.add(horloge_minuit(640, 280, 50))
    S.add(bulle(620, 480, 250, 90, "Avant minuit !", 30, pointe=(170, 560)))
    return S


def p07():
    S = Scene()
    salle_bal(S)
    S.add(prince(290, 790, 1.35, expr="content", bras="donne", regard=(1, 0)))
    S.add(cendrillon(510, 790, 1.35, bal=True, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    S.add(notes(120, 400, 1.0, "#9775fa"), notes(640, 380, 0.9, "#e64980"))
    for x in (60, 740):
        S.add(personne(x, 700, 0.6, coiffure="chignon", cheveux="brun", habit="#ffc9c9", expr="bouche_bee", bras="joues"))
    return S


def p08():
    S = Scene()
    ciel(S, "#1c2a52", "#364fc7")
    etoiles(S, 25, graine=8)
    S.add(chateau(400, 470, 0.7, nuit_=True))
    for k in range(6):
        S.add(rect(120 + k * 20, 480 + k * 50, 560 - k * 40, 50, "#e9ecef", stroke="#ced4da", stroke_width=3))
    S.add(horloge_minuit(640, 150, 50))
    S.add(cendrillon(470, 740, 1.2, bal=True, expr="oups", bras="course"))
    S.add(pantoufle_verre(320, 640, 0.7, rot=-15))
    S.add(texte(250, 110, "Dong ! Dong !", 56, "#ffd43b", contour="#5f3dc4"))
    return S


def p09():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=9)
    sol(S, 640, "#2f9e44")
    S.add(citrouille(580, 780, 1.3))
    for x in (440, 690, 740):
        S.add(souris_(x, 790, 0.4, expr="surpris"))
    S.add(cendrillon(250, 790, 1.35, expr="timide", bras="porte", objet=pantoufle_verre(0, -60, 0.5)))
    return S


def p10():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6)
    S.add(prince(260, 790, 1.35, expr="fier", bras="donne", objet=pantoufle_verre(90, -100, 0.6)))
    S.add(personne(560, 790, 1.2, coiffure="chauve_cote", cheveux="gris", habit="#e8590c", robe=False, jambes="#495057", acc=("col",), expr="neutre", bras="porte",
                   objet=place(g([rect(-50, -20, 100, 20, "#c92a2a", rx=6), pantoufle_verre(0, -20, 0.4, brille=False)]), 0, -70)))
    S.add(bulle(420, 140, 520, 110, "J'épouserai celle\nà qui elle va !", 36, pointe=(280, 470)))
    return S


def p11():
    S = Scene()
    salon(S)
    S.add(soeur(0, 220, 790, 1.2, expr="furieux", bras="tete"))
    S.add(soeur(1, 420, 790, 1.2, expr="oups", bras="bas"))
    S.add(pantoufle_verre(420, 790, 0.7))
    S.add(prince(650, 790, 1.2, expr="inquiet", bras="croises"))
    S.add(texte(400, 290, "Trop petite !", 56, "#c92a2a", contour="#fff"))
    return S


def p12():
    S = Scene()
    salon(S)
    S.add(soeur(0, 90, 790, 1.0, expr="bouche_bee", bras="joues"), soeur(1, 200, 790, 1.0, expr="bouche_bee"))
    S.add(cendrillon(420, 790, 1.35, expr="rire", bras="donne", objet=pantoufle_verre(90, -100, 0.6)))
    S.add(pantoufle_verre(420, 790, 0.7))
    S.add(prince(650, 790, 1.3, expr="bouche_bee", bras="ouverts"))
    S.add(etincelles(420, 740, 0.8))
    return S


def p13():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6)
    S.add(prince(310, 790, 1.35, expr="rire", bras="salut"))
    S.add(cendrillon(500, 790, 1.35, bal=True, habit="#f8f9fa", motif_robe="#e7f5ff", expr="rire", bras="haut"))
    S.add(soeur(0, 90, 790, 0.9, expr="timide"), soeur(1, 710, 790, 0.9, expr="timide"))
    S.add(coeur(400, 260, 1.6), etincelles(400, 320, 1.4, graine=13))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pantoufle-seule.svg", vignette),
    ("01-cendrillon.svg", p01), ("02-le-bal.svg", p02), ("03-au-coin-du-feu.svg", p03), ("04-la-fee.svg", p04),
    ("05-le-carrosse.svg", p05), ("06-la-robe.svg", p06), ("07-la-danse.svg", p07), ("08-minuit.svg", p08),
    ("09-la-citrouille.svg", p09), ("10-la-pantoufle.svg", p10), ("11-trop-petite.svg", p11),
    ("12-elle-lui-va.svg", p12), ("13-le-mariage.svg", p13),
]
