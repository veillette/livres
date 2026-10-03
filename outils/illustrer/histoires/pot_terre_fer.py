"""Le Pot de terre et le Pot de fer — quand on est fort, on fait attention aux plus fragiles."""
from fables import *

ID = "pot-terre-fer"

ARDOISE = "#5c677d"


def terre(x, y, s=1.0, **k):
    return pot_parlant(x, y, s, fer=False, **k)


def fer(x, y, s=1.0, **k):
    return pot_parlant(x, y, s, fer=True, **k)


def cuisine(S, feu=True):
    interieur(S, "#fff9db", "#c9a27e", 600, papier="#ffec99")
    S.add(cheminee(640, 600, 0.68, feu=feu))
    S.add(etagere(170, 260, 240, objets=g([assiette(120, 258, 1.0), tasse(200, 258, 1.0), assiette(240, 258, 0.8, bord="#ff8787")])))
    S.add(fenetre(70, 330, 150, 140, rideaux="#ffd43b"))


def chemin_cailloux(S, graine=101, soir=False):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(160, 120, 0.6), nuage(620, 90, 0.5))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 580, "#8ce99a")
    S.add(chemin("M 0 680 Q 400 620 800 660 L 800 800 L 0 800 Z", "#e9d8c4"))
    rr = random.Random(graine)
    for _ in range(9):
        S.add(caillou(rr.uniform(20, 780), rr.uniform(700, 790), rr.uniform(0.4, 0.8), "#adb5bd"))


def couverture():
    S = Scene()
    chemin_cailloux(S)
    S.add(fer(250, 740, 1.5, expr="rire", bras="haut", pas=-1))
    S.add(terre(560, 740, 1.3, expr="inquiet", bras="large", pas=1))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fer(125, 255, 0.8, expr="sourire"))
    S.add(terre(285, 255, 0.72, expr="sourire"))
    return S


def p01():
    S = Scene()
    cuisine(S)
    S.add(fer(200, 760, 1.3, expr="fier", bras="hanches"))
    S.add(terre(420, 760, 1.15, expr="content", bras="bas"))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(fer(200, 760, 1.3, expr="rire", bras="haut"))
    S.add(terre(420, 760, 1.15, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(330, 140, 440, 110, "Partons en voyage !", 38, pointe=(210, 420)))
    return S


def p03():
    S = Scene()
    cuisine(S)
    S.add(fer(200, 760, 1.25, expr="sourire", bras="bas", regard=(1, 0)))
    S.add(terre(420, 760, 1.15, expr="inquiet", bras="bas", regard=(-1, 0)))
    S.add(bulle(440, 140, 600, 140, "Je suis bien trop fragile !\nUn rien me casse…", 36, pointe=(420, 470)))
    return S


def p04():
    S = Scene()
    cuisine(S)
    S.add(fer(200, 760, 1.3, expr="fier", bras="large", regard=(1, 0)))
    S.add(terre(420, 760, 1.15, expr="timide", bras="bas", regard=(-1, 0)))
    S.add(bulle(360, 140, 600, 140, "Ne crains rien !\nJe te protégerai.", 38, pointe=(210, 430)))
    return S


def p05():
    S = Scene()
    chemin_cailloux(S)
    S.add(fer(300, 720, 1.2, expr="rire", bras="large", pas=-1))
    S.add(terre(540, 730, 1.05, expr="sourire", bras="large", pas=1))
    S.add(texte(400, 270, "Clopin-clopant…", 50, ARDOISE, contour="#fff"))
    return S


def p06():
    S = Scene()
    chemin_cailloux(S, graine=102)
    S.add(fer(330, 720, 1.2, expr="rire", bras="haut", pas=1, rot=8))
    S.add(terre(500, 730, 1.05, expr="oups", bras="large", rot=-10))
    S.add(eclat(420, 600, 0.9, "#fab005"))
    S.add(texte(420, 250, "TAC !", 60, ARDOISE, contour="#fff"))
    S.add(texte(600, 360, "Aïe !", 46, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    chemin_cailloux(S, graine=103)
    S.add(fer(230, 720, 1.2, expr="rire", bras="haut", pas=-1, rot=-6))
    S.add(terre(540, 730, 1.05, expr="pleure", bras="bas", fele=True))
    S.add(texte(230, 260, "Youpi !", 50, ARDOISE, contour="#fff"))
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin("M 0 420 Q 300 440 520 620 Q 640 720 800 740 L 800 800 L 0 800 Z", "#8ce99a"))
    S.add(chemin("M 0 470 Q 300 490 520 670 Q 640 760 800 780", stroke="#e9d8c4", sw=60))
    S.add(fer(470, 640, 1.0, expr="oups", bras="haut", rot=40))
    S.add(terre(640, 750, 1.0, expr="oups", bras="haut", rot=-20, fele=True, eclats=True))
    S.add(mouvement(380, 560, 1.2, rot=30))
    S.add(texte(320, 230, "BADABOUM !", 64, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    chemin_cailloux(S, graine=104)
    S.add(terre(420, 740, 1.4, expr="pleure", bras="bas", fele=True, eclats=True))
    S.add(poly([(600, 760), (626, 746), (640, 768)], "#d9733f"), poly([(260, 770), (286, 760), (282, 784)], "#d9733f"))
    S.add(texte(420, 250, "Bouh hou hou…", 48, ARDOISE, contour="#fff"))
    return S


def p10():
    S = Scene()
    chemin_cailloux(S, graine=104)
    S.add(fer(240, 740, 1.3, expr="triste", bras="bas", regard=(1, 0)))
    S.add(terre(540, 740, 1.15, expr="pleure", bras="bas", fele=True, eclats=True))
    S.add(bulle(340, 140, 600, 140, "C'est ma faute !\nJe ne savais pas que j'étais\nsi dur…", 32, pointe=(250, 440)))
    return S


def p11():
    S = Scene()
    chemin_cailloux(S, graine=105, soir=True)
    S.add(soleil(680, 150, 40, "#ffa94d"))
    S.add(fer(360, 740, 1.3, expr="concentre", bras="haut", pas=-1))
    S.add(terre(360, 470, 0.75, expr="timide", bras="bas", fele=True, eclats=True))
    S.add(texte(600, 400, "Tout doux…", 44, ARDOISE, contour="#fff"))
    return S


def p12():
    S = Scene()
    cuisine(S)
    S.add(personne(220, 760, 1.4, coiffure="chignon", cheveux="brun", habit="#4dabf7", expr="sourire", bras="donne"))
    S.add(terre(440, 760, 1.15, expr="timide", bras="bas", fele=True, eclats=True))
    S.add(pansement(450, 620, 1.3, rot=-30))
    S.add(fer(660, 760, 0.9, expr="inquiet", bras="bas", regard=(-1, 0)))
    return S


def p13():
    S = Scene()
    cuisine(S)
    S.add(fer(200, 760, 1.25, expr="content", bras="bas", regard=(1, 0)))
    S.add(terre(420, 760, 1.15, expr="rire", bras="bas", fele=True, regard=(-1, 0)))
    S.add(pansement(430, 620, 1.3, rot=-30))
    S.add(chemin("M 180 520 q 10 -20 0 -40 M 210 520 q 10 -20 0 -40", stroke="#dee2e6", sw=6))
    S.add(coeur(310, 380, 1.1))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pots-seuls.svg", vignette),
    ("01-dans-la-cuisine.svg", p01), ("02-partons.svg", p02), ("03-trop-fragile.svg", p03),
    ("04-je-te-protegerai.svg", p04), ("05-clopin-clopant.svg", p05), ("06-tac.svg", p06),
    ("07-youpi.svg", p07), ("08-badaboum.svg", p08), ("09-bouh-hou.svg", p09),
    ("10-c-est-ma-faute.svg", p10), ("11-tout-doux.svg", p11), ("12-un-pansement.svg", p12),
    ("13-au-coin-du-feu.svg", p13),
]
