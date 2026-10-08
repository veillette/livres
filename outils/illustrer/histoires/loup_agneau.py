"""Le Loup et l'Agneau — face à une brute, on ne discute pas : on va chercher de l'aide."""
from fables import *
from contes import foret

ID = "loup-agneau"


def agneau(x, y, s=1.0, **k):
    return perso("mouton", x, y, s, **k)


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def bergere(x, y, s=1.0, **k):
    k.setdefault("coiffure", "tresses")
    k.setdefault("cheveux", "blond")
    k.setdefault("habit", "#4dabf7")
    k.setdefault("peau", "claire")
    return personne(x, y, s, **k)


def ruisseau(S, y=560, soir=False):
    """Prairie traversée par un ruisseau qui coule de gauche à droite."""
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(160, 120, 0.6), nuage(620, 90, 0.5))
    collines(S, y - 20, "#b2f2bb", graine=31)
    sol(S, y, "#8ce99a")
    S.add(chemin(f"M 0 {y + 130} Q 200 {y + 110} 400 {y + 140} T 800 {y + 150} L 800 800 L 0 800 Z", "#4dabf7"))
    for k in range(8):
        x0 = 60 + (k % 4) * 190 + (k // 4) * 80
        S.add(chemin(f"M {x0} {y + 180 + (k // 4) * 50 + (k % 2) * 14} q 25 -10 50 0", stroke="#d0ebff", sw=5))
    S.add(buisson(80, y + 40, 0.9), buisson(730, y + 30, 0.8, baies="#fa5252"))


def couverture():
    S = Scene()
    ruisseau(S, 560)
    S.add(loup(250, 640, 1.45, expr="furieux", bras="poing", regard=(1, 0)))
    S.add(agneau(560, 668, 1.15, expr="inquiet", bras="calin", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(agneau(200, 262, 0.95, expr="sourire"))
    return S


def p01():
    S = Scene()
    ruisseau(S)
    S.add(soleil(680, 120, 44))
    S.add(agneau(420, 668, 1.4, expr="content", bras="bas", regard=(0, 1)))
    S.add(goutte(470, 690, 1.0), goutte(390, 700, 0.8))
    return S


def p02():
    S = Scene()
    ruisseau(S)
    S.add(loup(170, 640, 1.3, expr="malin", bras="hanches", regard=(1, 0)))
    S.add(agneau(600, 668, 1.0, expr="content", bras="bas", regard=(0, 1)))
    S.add(texte(200, 260, "Miam…", 50, "#1971c2", contour="#fff"))
    return S


def p03():
    S = Scene()
    ruisseau(S)
    S.add(loup(220, 650, 1.45, expr="furieux", bras="poing", regard=(1, 0)))
    S.add(agneau(600, 668, 1.0, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(400, 150, 560, 130, "Qui te rend si hardi\nde troubler mon eau ?", 38, pointe=(260, 330)))
    return S


def p04():
    S = Scene()
    ruisseau(S)
    S.add(loup(170, 650, 1.2, expr="fache", bras="croises", regard=(1, 0)))
    S.add(agneau(600, 668, 1.1, expr="timide", bras="calin", regard=(-1, 0)))
    S.add(fleche(260, 730, 540, 740, "#1864ab", sw=7))
    S.add(texte(400, 785, "le courant", 32, "#1864ab", contour="#fff"))
    S.add(bulle(520, 170, 500, 130, "Je bois plus bas que vous :\nl'eau va de vous à moi !", 34, pointe=(590, 430)))
    return S


def p05():
    S = Scene()
    ruisseau(S)
    S.add(loup(240, 660, 1.4, expr="furieux", bras="montre", regard=(1, 0)))
    S.add(agneau(610, 668, 1.0, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(400, 150, 600, 130, "Et l'an passé, tu as dit\ndu mal de moi !", 38, pointe=(260, 340)))
    return S


def p06():
    S = Scene()
    ruisseau(S)
    S.add(loup(200, 650, 1.3, expr="fache", bras="hanches", regard=(1, 0)))
    S.add(agneau(580, 668, 1.1, expr="sourire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(500, 170, 560, 130, "L'an passé ? Mais je\nn'étais pas encore né !", 36, pointe=(580, 430)))
    return S


def p07():
    S = Scene()
    ruisseau(S)
    S.add(loup(220, 650, 1.4, expr="furieux", bras="poing", regard=(1, 0)))
    S.add(agneau(600, 668, 1.0, expr="inquiet", bras="bas", regard=(-1, 0)))
    S.add(bulle(260, 130, 420, 110, "C'est donc ton frère !", 36, pointe=(240, 320)))
    S.add(bulle(590, 330, 340, 90, "Je n'en ai point…", 32, pointe=(600, 470)))
    return S


def p08():
    S = Scene()
    ruisseau(S)
    S.add(loup(330, 660, 1.65, expr="furieux", bras="ouverts", regard=(1, 0)))
    S.add(agneau(650, 668, 0.95, expr="oups", bras="joues", regard=(-1, 0)))
    S.add(bulle(330, 110, 640, 140, "Alors c'est quelqu'un des tiens :\nbergers, chiens, moutons !", 34, pointe=(330, 250)))
    return S


def p09():
    S = Scene()
    ruisseau(S)
    S.add(agneau(260, 668, 1.4, expr="inquiet", bras="pense", regard=(1, -1)))
    S.add(pensee(560, 280, 190, g([bergere(470, 380, 0.75, expr="sourire"), perso("chien", 640, 380, 0.75, expr="fache", bras="hanches")]), depuis=(330, 420)))
    return S


def p10():
    S = Scene()
    ruisseau(S)
    S.add(loup(170, 650, 1.2, expr="surpris", bras="ouverts", regard=(1, 0)))
    S.add(agneau(560, 668, 1.2, expr="concentre", bras="course", regard=(1, 0), flip=True))
    S.add(mouvement(470, 600, 1.2))
    S.add(texte(560, 260, "Je ne discute plus !", 46, "#1971c2", contour="#fff"))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    collines(S, 560, "#b2f2bb", graine=32)
    sol(S, 580, "#8ce99a")
    S.add(agneau(560, 720, 1.1, expr="oups", bras="course", flip=True, regard=(1, 0)))
    S.add(mouvement(470, 620, 1.2))
    S.add(loup(220, 700, 1.3, expr="furieux", bras="course", flip=True, regard=(1, 0)))
    S.add(mouvement(130, 580, 1.2))
    S.add(texte(250, 230, "Reviens ici !", 50, "#c92a2a", contour="#fff"))
    return S


def p12():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    collines(S, 560, "#b2f2bb", graine=33)
    sol(S, 580, "#8ce99a")
    S.add(barriere(400, 640, 1.0, largeur=800))
    for k, xx in enumerate((470, 720)):
        S.add(perso("mouton", xx, 620, 0.7, expr="sourire"))
    S.add(bergere(600, 720, 1.2, expr="surpris", bras="ouverts"))
    S.add(perso("chien", 380, 740, 1.1, expr="furieux", bras="poing", regard=(-1, 0)))
    S.add(agneau(160, 760, 0.95, expr="oups", bras="course", regard=(1, 0), flip=True))
    S.add(texte(380, 300, "OUAF ! OUAF !", 54, "#1971c2", contour="#fff"))
    S.cachette(650, 70, "air")
    return S


def p13():
    S = Scene()
    foret(S, graine=34)
    S.add(loup(420, 720, 1.4, expr="oups", bras="tete", flip=True, regard=(1, 0)))
    S.add(mouvement(300, 600, 1.2))
    S.add(texte(560, 260, "Sauve qui peut !", 46, "#c92a2a", contour="#fff"))
    return S


def p14():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    collines(S, 560, "#b2f2bb", graine=35)
    sol(S, 580, "#8ce99a")
    S.add(soleil(680, 160, 44, "#ffa94d"))
    S.add(perso("mouton", 300, 740, 1.4, expr="content", bras="calin"))
    S.add(agneau(470, 750, 1.0, expr="content", bras="calin", regard=(-1, 0)))
    S.add(coeur(390, 380, 1.1))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("agneau-seul.svg", vignette),
    ("01-au-ruisseau.svg", p01), ("02-le-loup.svg", p02), ("03-qui-te-rend-si-hardi.svg", p03),
    ("04-le-courant.svg", p04), ("05-l-an-passe.svg", p05), ("06-pas-ne.svg", p06),
    ("07-ton-frere.svg", p07), ("08-quelqu-un-des-tiens.svg", p08), ("09-il-reflechit.svg", p09),
    ("10-je-ne-discute-plus.svg", p10), ("11-reviens.svg", p11), ("12-ouaf.svg", p12),
    ("13-sauve-qui-peut.svg", p13), ("14-avec-maman.svg", p14),
]
