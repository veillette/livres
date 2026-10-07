"""Cendrillon — la bonté finit toujours par se voir."""
from contes import *

ID = "cendrillon"
# Âges et silhouettes distincts : Cendrillon et ses demi-sœurs sont des
# jeunes filles, la belle-mère est grande et sèche, le prince un jeune homme,
# la marraine une vieille dame.
CENDRILLON = dict(coiffure="longs", cheveux="blond", peau="claire", habit="#ced4da", chaussures="#868e96", stature="ado", yeux="cils")
BAL = dict(habit="#74c0fc", motif_robe="#e7f5ff", acc=("diademe",), chaussures="#d0ebff")
SOEURS = [dict(coiffure="chignon", cheveux="roux", peau="claire", habit="#e64980", acc=("noeud",), couleur_acc="#ffd43b",
               stature="ado", carrure="ronde", nez="retrousse", taches=True),
          dict(coiffure="boucles", cheveux="noir", peau="doree", habit="#fab005", acc=("fleur",), couleur_acc="#e64980",
               stature="ado", carrure="fine", nez="pointu")]
BELLE_MERE = dict(coiffure="chignon", cheveux="gris", peau="rosee", habit="#5f3dc4", acc=("lunettes",),
                  stature="adulte", carrure="fine", nez="long")
PRINCE = dict(coiffure="courts", cheveux="brun", peau="brune", habit="#1864ab", robe=False, jambes="#f8f9fa", cape="#c92a2a", acc=("couronne",),
              stature="adulte")
FEE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#b197fc", ailes="#e5dbff", motif_robe="#fff", stature="ancien", nez="rond")
VALET = dict(coiffure="chauve_cote", cheveux="gris", habit="#e8590c", robe=False, jambes="#495057", acc=("col",), stature="ancien", carrure="ronde")


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


def fee(x, y, s=1.0, rot_baguette=20, **k):
    k.setdefault("bras", "tient")
    k.setdefault("objet", baguette(*ancre(68, -146, "tient", "ancien"), 0.9, rot=rot_baguette))
    return personne(x, y, s, **{**FEE, **k})


def pantoufle_tendue(qui):
    """Pantoufle tenue à bout de bras (pose « donne »)."""
    return pantoufle_verre(*ancre(90, -100, "donne", qui.get("stature", "enfant"), qui.get("carrure", "normale")), 0.6)


def souris_(x, y, s=0.4, **k):
    return perso("souris", x, y, s, **k)


def cuisine(S, feu=True):
    """La cuisine au coin du feu, le soir : la cheminée éclaire la pièce."""
    piece(S, "chaumiere", 580)
    S.add(rect(480, 260, 260, 320, cylindre("#868e96", 0.2, 0.75)), pierres(480, 260, 260, 320, "#868e96", opacite=0.5),
          rect(462, 244, 296, 26, "#5c3a1e", rx=4), rect(510, 380, 200, 200, "#343a40"))
    if feu:
        S.add(chemin("M 540 580 Q 540 500 580 480 Q 590 530 610 460 Q 640 520 650 490 Q 690 520 680 580 Z", "#ff922b"),
              chemin("M 570 580 Q 575 530 600 515 Q 610 545 625 510 Q 650 550 650 580 Z", "#ffd43b"))
        S.lumiere(610, 520, 330, "#ffa94d", 0.55)
    S.add(fenetre(90, 110, 150, 140, dehors="#364fc7", nuit_=True))
    S.ambiance("nuit")


def salon(S):
    """Le salon de la belle-mère : boiseries et papier peint damassé."""
    piece(S, "manoir", 580)
    S.add(fenetre(560, 100, 170, 150, dehors="#a5d8ff", rideaux="#e64980"))
    S.add(cadre_mur(90, 120))


def couverture():
    S = Scene()
    salle_bal(S)
    S.add(horloge_minuit(400, 350, 50))
    S.add(prince(260, 790, 1.15, expr="content", bras="donne", regard=(1, 0)))
    S.add(cendrillon(525, 790, 1.2, bal=True, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    S.add(pantoufle_verre(400, 780, 0.9))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pantoufle_verre(200, 200, 2.2))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(cendrillon(400, 790, 1.15, expr="triste", bras="tient", objet=balai(*ancre(68, -30, "tient", "ado"), 0.8, rot=15)))
    S.add(belle_mere(160, 790, 1.15, expr="fache", bras="montre", regard=(1, 0)))
    S.add(soeur(0, 600, 790, 1.05, expr="malin", bras="croises", regard=(-1, 0)), soeur(1, 715, 790, 1.0, expr="rire", bras="bouche"))
    return S


def p02():
    S = Scene()
    salon(S)
    S.add(soeur(0, 190, 790, 1.1, expr="rire", bras="saute"), soeur(1, 380, 790, 1.1, expr="rire", bras="saute"))
    S.add(place(g([rect(-50, -34, 100, 68, "#fff", stroke="#e9ecef", stroke_width=3), poly([(-50, -34), (0, 6), (50, -34)], "#f1f3f5"), cercle(0, 6, 10, "#c92a2a")]), 290, 330))
    S.add(cendrillon(620, 790, 1.1, expr="inquiet", bras="pense"))
    S.add(bulle(560, 140, 300, 90, "Et moi ?", 40, pointe=(610, 460)))
    return S


def p03():
    S = Scene()
    cuisine(S)
    S.add(cendrillon(300, 790, 1.2, expr="pleure", larmes=True))
    S.add(souris_(110, 790, 0.45, expr="triste"), souris_(190, 800, 0.4, expr="triste"), souris_(430, 800, 0.4, expr="triste"))
    return S


def p04():
    S = Scene()
    cuisine(S, feu=False)
    S.add(etincelles(520, 400, 2.4, graine=5))
    S.add(fee(520, 790, 1.15, expr="rire", bras="tient", regard=(-1, 0)))
    S.add(cendrillon(220, 790, 1.1, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(bulle(420, 120, 460, 100, "Tu iras au bal,\nma chérie !", 36, pointe=(500, 440)))
    return S


def p05():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=5)
    sol(S, 640, "#2f9e44")
    S.add(carrosse(330, 760, 0.95))
    S.add(fee(100, 790, 0.95, expr="rire", bras="tient", rot_baguette=40))
    S.add(etincelles(330, 500, 2.2, graine=9))
    S.add(texte(400, 120, "Pouf !", 80, "#ffd43b", contour="#5f3dc4"))
    return S


def p06():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=6)
    sol(S, 640, "#2f9e44")
    S.add(etincelles(400, 520, 2.6, graine=11))
    S.add(cendrillon(400, 790, 1.3, bal=True, expr="rire", bras="ouverts"))
    S.add(fee(150, 790, 0.95, expr="sourire", bras="tient"))
    S.add(horloge_minuit(640, 280, 50))
    S.add(bulle(620, 480, 250, 90, "Avant minuit !", 30, pointe=(170, 560)))
    return S


def p07():
    S = Scene()
    salle_bal(S)
    S.add(prince(300, 790, 1.15, expr="content", bras="donne", regard=(1, 0)))
    S.add(cendrillon(500, 790, 1.2, bal=True, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    S.add(notes(120, 400, 1.0, "#9775fa"), notes(640, 380, 0.9, "#e64980"))
    for x in (60, 740):
        S.add(personne(x, 700, 0.6, coiffure="chignon", cheveux="brun", habit="#ffc9c9", expr="bouche_bee", bras="joues"))
    return S


def p08():
    S = Scene()
    ciel(S, "#1c2a52", "#364fc7")
    etoiles(S, 25, graine=8)
    # le château domine : Cendrillon, en bas du grand escalier, est toute petite
    S.add(chateau(400, 520, 0.85, nuit_=True))
    S.lumiere(400, 330, 280, "#ffd43b", 0.3)
    for k in range(6):
        S.add(rect(100 + k * 20, 500 + k * 50, 600 - k * 40, 50, "#e9ecef", stroke="#ced4da", stroke_width=3))
    S.add(horloge_minuit(712, 128, 46))
    S.add(cendrillon(480, 770, 0.85, bal=True, expr="oups", bras="course"))
    S.add(pantoufle_verre(330, 652, 0.55, rot=-15))
    S.add(texte(100, 110, "Dong !", 52, "#ffd43b", contour="#5f3dc4"), texte(110, 180, "Dong !", 52, "#ffd43b", contour="#5f3dc4"))
    S.ambiance("nuit")
    return S


def p09():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 30, graine=9)
    sol(S, 640, "#2f9e44")
    S.add(citrouille(580, 780, 1.3))
    for x in (440, 690, 740):
        S.add(souris_(x, 790, 0.4, expr="surpris"))
    S.add(cendrillon(250, 790, 1.2, expr="timide", bras="porte", objet=pantoufle_verre(*ancre(0, -60, "porte", "ado"), 0.5)))
    return S


def p10():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6)
    S.add(prince(260, 790, 1.15, expr="fier", bras="donne", objet=pantoufle_tendue(PRINCE)))
    S.add(personne(560, 790, 1.05, expr="neutre", bras="porte",
                   objet=place(g([rect(-50, -20, 100, 20, "#c92a2a", rx=6), pantoufle_verre(0, -20, 0.4, brille=False)]), *ancre(0, -70, "porte", "ancien", "ronde")),
                   **VALET))
    S.add(bulle(420, 140, 520, 110, "J'épouserai celle\nà qui elle va !", 36, pointe=(280, 470)))
    return S


def p11():
    S = Scene()
    salon(S)
    S.add(soeur(0, 220, 790, 1.1, expr="furieux", bras="tete"))
    S.add(soeur(1, 420, 790, 1.1, expr="oups", bras="bas"))
    S.add(pantoufle_verre(420, 790, 0.7))
    S.add(prince(650, 790, 1.05, expr="inquiet", bras="croises", regard=(-1, 0)))
    S.add(texte(400, 290, "Trop petite !", 56, "#c92a2a", contour="#fff"))
    return S


def p12():
    S = Scene()
    salon(S)
    S.add(soeur(0, 90, 790, 0.95, expr="bouche_bee", bras="joues"), soeur(1, 200, 790, 0.95, expr="bouche_bee", regard=(1, 0)))
    S.add(cendrillon(420, 790, 1.2, expr="rire", bras="donne", objet=pantoufle_tendue(CENDRILLON)))
    S.add(pantoufle_verre(420, 790, 0.7))
    S.add(prince(650, 790, 1.1, expr="bouche_bee", bras="ouverts", regard=(-1, 0)))
    S.add(etincelles(420, 740, 0.8))
    return S


def p13():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6)
    S.add(prince(320, 790, 1.15, expr="rire", bras="main", regard=(1, 0)))
    S.add(cendrillon(480, 790, 1.2, bal=True, habit="#f8f9fa", motif_robe="#e7f5ff", expr="rire", bras="main", flip=True, regard=(-1, 0)))
    S.add(soeur(0, 90, 790, 0.85, expr="timide"), soeur(1, 710, 790, 0.85, expr="timide"))
    S.add(coeur(400, 260, 1.6), etincelles(400, 320, 1.4, graine=13))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pantoufle-seule.svg", vignette),
    ("01-cendrillon.svg", p01), ("02-le-bal.svg", p02), ("03-au-coin-du-feu.svg", p03), ("04-la-fee.svg", p04),
    ("05-le-carrosse.svg", p05), ("06-la-robe.svg", p06), ("07-la-danse.svg", p07), ("08-minuit.svg", p08),
    ("09-la-citrouille.svg", p09), ("10-la-pantoufle.svg", p10), ("11-trop-petite.svg", p11),
    ("12-elle-lui-va.svg", p12), ("13-le-mariage.svg", p13),
]
