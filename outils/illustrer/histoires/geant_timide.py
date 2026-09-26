"""Zoé et le géant timide — la timidité, et aller vers les autres."""
from base import *
from objets import *
from fantastique import *

ID = "geant-timide"
ZOE = dict(coiffure="boucles", cheveux="noir", peau="foncee", habit="#ffd43b", acc=("diademe",))
BARTOLO = dict(coiffure="herisses", cheveux="roux", barbe="#d9480f", peau="rosee", habit="#4c6ef5",
               robe=False, jambes="#8d5524", chaussures="#5c3a1e", ceinture="#8d5524")
GENS = [dict(coiffure="courts", cheveux="brun", habit="#fa5252", robe=False, peau="doree"),
        dict(coiffure="tresses", cheveux="blond", habit="#51cf66", peau="claire"),
        dict(coiffure="chignon", cheveux="gris", habit="#cc5de8", peau="brune"),
        dict(coiffure="herisses", cheveux="chatain", habit="#ff922b", robe=False, peau="rosee")]


def bartolo(x, y, s=3.0, **k):
    return personne(x, y, s, **{**BARTOLO, **k})


def village(S, fete=False, montagne=True):
    ciel(S, "#a5d8ff", "#f8f9fa")
    if montagne:
        S.add(montagnes(None, 560, ("#b197fc", "#9775fa")))
    collines(S, 600, "#b2f2bb", graine=8)
    sol(S, 600, "#8ce99a")
    S.add(maison(110, 610, 0.6, toit="#e8590c"), maison(700, 610, 0.55, toit="#1c7ed6", mur="#fff3bf"))
    if fete:
        S.add(chemin("M 0 120 Q 400 240 800 120", stroke="#495057", sw=3))
        for k in range(14):
            t = (k + 0.5) / 14
            x = 800 * t
            y = 120 + 120 * 4 * t * (1 - t) * 0.5 + 8
            S.add(poly([(x - 16, y - 8), (x + 16, y - 8), (x, y + 24)], ["#fa5252", "#ffd43b", "#51cf66", "#4dabf7"][k % 4]))


def chapeau_vole(x, y, s=1.0, c="#fa5252", rot=0):
    return chapeau(x, y, s, c, rot=rot)


def couverture():
    S = Scene()
    village(S)
    S.add(bartolo(430, 830, 2.9, expr="timide", bras="joues"))
    S.add(personne(200, 780, 1.45, expr="rire", bras="salut", **ZOE))
    S.add(fleur(620, 780, 1.1, "#ff8787"), fleur(700, 790, 1.0, "#ffd43b"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(personne(200, 262, 0.95, expr="content", bras="salut", **ZOE))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(poly([(200, 640), (520, 90), (840, 640)], "#9775fa"), poly([(440, 230), (520, 90), (600, 230), (560, 210), (520, 240), (480, 210)], "#fff"))
    S.add(personne(520, 150, 0.35, expr="sourire", **BARTOLO))
    collines(S, 640, "#b2f2bb", graine=3)
    sol(S, 640, "#8ce99a")
    S.add(chateau(190, 700, 0.42), maison(380, 700, 0.45), maison(620, 720, 0.4, toit="#1c7ed6"))
    return S


def p02():
    S = Scene()
    village(S)
    S.add(bartolo(620, 820, 2.7, expr="sourire", bras="salut"))
    S.add(personne(130, 780, 1.0, expr="oups", bras="course", **GENS[0]))
    S.add(personne(280, 790, 0.95, expr="surpris", bras="joues", **GENS[1]))
    S.add(texte(250, 200, "BOUM ! BOUM !", 60, "#e8590c", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    village(S)
    for x in (420, 500, 580, 660):
        S.add(fleur(x, 790, 1.2, ["#ff8787", "#ffd43b", "#cc5de8", "#74c0fc"][x // 80 % 4]))
    S.add(bartolo(540, 780, 2.6, expr="concentre", bras="large", regard=(0, 1)))
    S.add(personne(160, 790, 1.2, expr="surpris", bras="bouche", regard=(1, -1), **ZOE))
    S.add(fontaine(160, 800, 0.9))
    return S


def p04():
    S = Scene()
    ciel(S, "#d0ebff", "#fff4e6")
    for k, (x, y) in enumerate([(160, 150), (620, 110), (720, 230)]):
        S.add(nuage(x, y, 0.6), mouvement(x - 120, y, 1.2))
    collines(S, 600, "#b2f2bb", graine=5)
    sol(S, 600, "#8ce99a")
    S.add(bartolo(400, 700, 2.1, expr="triste", bras="bas", regard=(0, 1)))
    S.add(ellipse(400, 810, 520, 120, "#4dabf7"))
    for k in range(5):
        S.add(chemin(f"M {150 + k * 120} {740 + (k % 2) * 30} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    S.add(texte(400, 150, "Pfffff…", 50, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    village(S, montagne=False)
    S.add(bartolo(520, 830, 2.7, expr="timide", bras="yeux"))
    S.add(personne(160, 780, 1.3, expr="rire", bras="salut", regard=(1, -1), **ZOE))
    S.add(bulle(210, 200, 330, 90, "Bonjour !", 48, pointe=(190, 470)))
    return S


def p06():
    S = Scene()
    village(S)
    S.add(bartolo(560, 830, 2.6, expr="souffle", bras="bouche"))
    S.add(personne(120, 790, 1.0, expr="surpris", bras="haut", **GENS[3]))
    S.add(personne(280, 790, 1.2, expr="rire", **ZOE))
    S.add(chapeau_vole(130, 300, 1.0, "#fa5252", rot=-30), chapeau_vole(300, 230, 0.8, "#4dabf7", rot=40), chapeau_vole(90, 150, 0.7, "#fab005", rot=15))
    S.add(mouvement(400, 330, 1.4), mouvement(420, 420, 1.2))
    return S


def p07():
    S = Scene()
    village(S, montagne=False)
    S.add(bartolo(560, 840, 2.7, expr="triste", bras="pense", regard=(-1, 1)))
    S.add(personne(170, 780, 1.3, expr="inquiet", bras="large", regard=(1, -1), **ZOE))
    S.add(bulle(400, 110, 520, 110, "Je voulais me faire des amis…\nmais je suis trop timide.", 30, pointe=(470, 250)))
    return S


def p08():
    S = Scene()
    village(S, montagne=False)
    S.add(bartolo(560, 840, 2.7, expr="surpris", bras="bas", regard=(-1, 1)))
    S.add(personne(190, 780, 1.35, expr="joie", bras="montre", regard=(1, -1), **ZOE))
    S.add(eclat(250, 380, 1.3, "#fab005"))
    S.add(bulle(260, 150, 440, 110, "Viens à la fête !\nJe serai à côté de toi.", 34, pointe=(220, 370)))
    return S


def p09():
    S = Scene()
    village(S, fete=True, montagne=False)
    S.add(bartolo(560, 840, 2.7, expr="timide", bras="bas", regard=(-1, 1)))
    S.add(personne(344, 780, 1.3, expr="sourire", bras="tient", regard=(1, -1), **ZOE))
    S.add(personne(100, 790, 0.95, expr="inquiet", bras="joues", **GENS[2]))
    S.add(personne(200, 800, 0.9, expr="surpris", **GENS[0]))
    S.add(coeur(420, 520, 1.1))
    return S


def p10():
    S = Scene()
    village(S, fete=True, montagne=False)
    S.add(arbre(170, 720, 2.2, "#51cf66", "#40c057"))
    S.add(cerf_volant(300, 420, 0.7, rot=-20))
    S.add(bartolo(520, 840, 2.6, expr="concentre", bras="montre", flip=True, regard=(-1, -1)))
    S.add(personne(380, 790, 0.9, expr="pleure", larmes=True, bras="haut", **GENS[3]))
    S.add(personne(660, 790, 1.0, expr="bouche_bee", bras="joues", **ZOE))
    return S


def p11():
    S = Scene()
    village(S, fete=True, montagne=False)
    S.add(bartolo(560, 840, 2.6, expr="timide", bras="porte", objet=cerf_volant(0, -120, 0.5)))
    for k, (x, gg) in enumerate([(100, GENS[3]), (220, GENS[1]), (330, ZOE)]):
        S.add(personne(x, 790, 0.95 if k < 2 else 1.1, expr="rire", bras="haut", **gg))
    S.add(texte(280, 330, "Merci, géant !", 52, "#4c6ef5", contour="#fff"))
    return S


def p12():
    S = Scene()
    village(S, fete=True)
    S.add(bartolo(400, 860, 2.4, expr="rire", bras="tete"))
    S.add(personne(318, 560, 0.75, expr="rire", bras="haut", **GENS[3]))
    S.add(personne(482, 560, 0.75, expr="rire", bras="haut", **GENS[1]))
    S.add(personne(400, 420, 0.7, expr="rire", bras="haut", **ZOE))
    S.add(paillettes(160, 380, 1.4), paillettes(640, 360, 1.4, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("zoe-seule.svg", vignette),
    ("01-la-montagne.svg", p01), ("02-boum.svg", p02), ("03-pointe-des-pieds.svg", p03),
    ("04-le-lac.svg", p04), ("05-bonjour.svg", p05), ("06-chuchotement.svg", p06),
    ("07-trop-timide.svg", p07), ("08-une-idee.svg", p08), ("09-la-fete.svg", p09),
    ("10-cerf-volant.svg", p10), ("11-merci.svg", p11), ("12-sur-les-epaules.svg", p12),
]
