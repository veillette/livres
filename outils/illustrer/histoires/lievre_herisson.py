"""Le Lièvre et le Hérisson — d'après le conte des frères Grimm.

Lucien le lièvre se moque des petites pattes d'Hippolyte le hérisson. Course
dans un sillon : Hortense, la femme d'Hippolyte, qui lui ressemble comme deux
gouttes d'eau, attend à l'autre bout et crie « Je suis déjà là ! ».
Adaptation douce : le lièvre, épuisé, comprend la ruse, rit et s'excuse ;
tout le monde partage le panier de carottes.
"""
from contes import *
from fables import champ_laboure

ID = "lievre-herisson"
HABIT = "#4dabf7"


def hippolyte(x, y, s=0.8, **k):
    return perso("herisson", x, y, s, **{**dict(habit=HABIT), **k})


def hortense(x, y, s=0.8, **k):
    return perso("herisson", x, y, s, **{**dict(habit=HABIT, acc=("fleur",), couleur_acc="#f783ac"), **k})


def lucien(x, y, s=1.15, **k):
    return perso("lievre", x, y, s, **{**dict(habit="#f03e3e"), **k})


def champ(S, graine=1, soir=False):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#fff9db")
    S.add(nuage(150, 100, 0.55), nuage(640, 80, 0.45))
    collines(S, 500, "#b2f2bb", graine=graine)
    champ_laboure(S, 500)


def bout_de_champ(S, graine=1):
    """Le champ vu de côté : un long sillon horizontal, départ à gauche, arrivée à droite."""
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(400, 110, 0.5))
    collines(S, 520, "#b2f2bb", graine=graine)
    S.add(rect(0, 520, 800, 280, "#a0693a"))
    for yy in (560, 620, 700):
        S.add(chemin(f"M 0 {yy} Q 400 {yy - 10} 800 {yy}", stroke="#7c4a1e", sw=10))
    S.add(rect(40, 470, 10, 60, "#8d5524"), poly([(50, 470), (100, 485), (50, 500)], "#fa5252"))
    S.add(rect(750, 470, 10, 60, "#8d5524"), poly([(760, 470), (810, 485), (760, 500)], "#40c057"))


def panier_carottes(x, y, s=1.0):
    return place([chemin("M -60 -60 Q 0 -140 60 -60", stroke="#8d5524", sw=6),
                  carotte(-30, -66, 0.6, rot=-160), carotte(0, -70, 0.6, rot=180), carotte(28, -66, 0.6, rot=160),
                  chemin("M -66 -60 L 66 -60 L 52 0 L -52 0 Z", "#c68642"), trait(-60, -36, 60, -36, "#8d5524", 3)], x, y, s)


def essouffle(x, y, s=1.0):
    return g([chemin(f"M {x} {y} q 20 -10 40 0", stroke="#fff", sw=6, opacity=0.9), chemin(f"M {x + 10} {y + 18} q 20 -10 40 0", stroke="#fff", sw=6, opacity=0.9)])


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    bout_de_champ(S, 2)
    S.add(lucien(300, 700, 1.25, expr="surpris", bras="course", rot=-10), mouvement(190, 560, 1.2))
    S.add(hortense(640, 720, 1.0, expr="malin", bras="haut"))
    S.add(texte(520, 280, "Je suis déjà là !", 58, "#1c7ed6", contour="#fff", rot=-4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(hippolyte(130, 264, 0.95, expr="malin", bras="salut"), lucien(290, 264, 0.95, expr="rire"))
    return S


def p01():
    S = Scene()
    champ(S, 1)
    S.add(soleil(680, 110, 46))
    for x, y in ((120, 600), (320, 580), (560, 610), (700, 700)):
        S.add(chou(x, y, 0.7))
    S.add(hippolyte(400, 780, 1.2, expr="chante", bras="hanches"), notes(500, 470, 1.0, "#1c7ed6"))
    return S


def p02():
    S = Scene()
    champ(S, 2)
    S.add(chou(700, 640, 0.7))
    S.add(lucien(560, 790, 1.35, expr="malin", bras="montre", flip=True, regard=(-1, 1)))
    S.add(hippolyte(240, 790, 1.0, expr="triste", regard=(1, -1)))
    S.add(bulle(380, 170, 560, 130, "Avec tes petites pattes,\ntu ne dois pas courir bien vite !", 32, pointe=(560, 470)))
    return S


def p03():
    S = Scene()
    champ(S, 3)
    S.add(hippolyte(250, 790, 1.1, expr="fache", bras="poing"))
    S.add(lucien(560, 790, 1.3, expr="rire", bras="hanches", flip=True))
    S.add(panier_carottes(400, 790, 0.9))
    S.add(bulle(330, 180, 520, 90, "Faisons la course !", 42, pointe=(260, 560)))
    S.add(texte(600, 380, "Ha ha ha !", 44, "#f03e3e", contour="#fff"))
    return S


def p04():
    S = Scene()
    interieur(S, "#ffe8cc", "#c9a27a", 560, papier="#ffd8a8", plinthe="#a0693a")
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#69db7c"))
    S.add(hippolyte(280, 790, 1.2, expr="malin", bras="pense"))
    S.add(hortense(520, 790, 1.2, expr="rire", bras="joues"))
    S.add(texte(320, 330, "Chut… j'ai une idée !", 46, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    bout_de_champ(S, 3)
    S.add(lucien(250, 720, 1.1, expr="rire", bras="course", rot=-8), mouvement(150, 590, 1.0))
    S.add(hippolyte(90, 720, 0.75, expr="malin", bras="bas"))
    S.add(texte(400, 230, "Un, deux, trois… partez !", 48, "#e8590c", contour="#fff"))
    return S


def p06():
    S = Scene()
    bout_de_champ(S, 4)
    S.add(lucien(560, 720, 1.2, expr="bouche_bee", bras="joues"))
    S.add(hortense(700, 720, 0.85, expr="rire", bras="haut"))
    S.add(texte(400, 230, "Je suis déjà là !", 60, "#1c7ed6", contour="#fff"))
    return S


def p07():
    S = Scene()
    bout_de_champ(S, 5)
    S.add(lucien(240, 720, 1.2, expr="bouche_bee", bras="joues", flip=True))
    S.add(hippolyte(100, 720, 0.85, expr="rire", bras="haut"))
    S.add(texte(420, 230, "Je suis déjà là !", 60, "#1c7ed6", contour="#fff"))
    return S


def p08():
    S = Scene()
    bout_de_champ(S, 6)
    for k in range(4):
        y = 300 + k * 30
        S.add(chemin(f"M 80 {y} L 720 {y}", stroke="#495057", sw=4, stroke_dasharray="10 12", opacity=0.5))
    S.add(lucien(420, 730, 1.15, expr="inquiet", bras="course", rot=-10), essouffle(500, 520))
    S.add(texte(400, 200, "Encore ! Et encore !", 52, "#e8590c", contour="#fff"))
    for k, t in enumerate(("1", "2", "3", "…", "10")):
        S.add(texte(160 + k * 120, 290, t, 30, "#495057"))
    return S


def p09():
    S = Scene()
    bout_de_champ(S, 7)
    S.add(lucien(400, 720, 1.2, expr="baille", bras="bas", rot=12), essouffle(480, 540))
    S.add(g([goutte(320 + k * 40, 500 - (k % 2) * 20, 0.8, "#74c0fc") for k in range(4)]))
    S.add(bulle(400, 200, 420, 90, "Je n'en peux plus !", 42, pointe=(400, 470)))
    return S


def p10():
    S = Scene()
    champ(S, 8)
    S.add(lucien(200, 790, 1.15, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(hippolyte(480, 790, 1.0, expr="rire", bras="calin"), hortense(620, 790, 1.0, expr="rire", bras="calin"))
    S.add(bulle(320, 200, 420, 90, "Vous êtes deux !", 44, pointe=(220, 480)))
    return S


def p11():
    S = Scene()
    champ(S, 9)
    S.add(lucien(260, 790, 1.2, expr="rire", bras="donne"))
    S.add(hippolyte(500, 790, 1.0, expr="content", bras="donne2", flip=True), hortense(640, 790, 1.0, expr="rire"))
    S.add(bulle(400, 180, 560, 130, "Pardon pour tes pattes :\nelles sont bien plus malignes\nque les miennes !", 32, pointe=(270, 470)))
    return S


def p12():
    S = Scene()
    champ(S, 10, soir=True)
    S.add(soleil(680, 200, 50, "#ff922b", rayons=False))
    S.add(panier_carottes(400, 780, 1.1))
    S.add(lucien(200, 790, 1.15, expr="miam", bras="tient", objet=carotte(68, -150, 0.6, rot=200)))
    S.add(hippolyte(560, 790, 0.95, expr="miam", bras="tient", objet=carotte(68, -150, 0.5, rot=200)))
    S.add(hortense(690, 790, 0.95, expr="rire", bras="tient", objet=carotte(68, -150, 0.5, rot=200)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("herisson-et-lievre.svg", vignette),
    ("01-le-champ.svg", p01), ("02-tes-petites-pattes.svg", p02), ("03-le-pari.svg", p03), ("04-une-idee.svg", p04),
    ("05-partez.svg", p05), ("06-deja-la.svg", p06), ("07-encore-la.svg", p07), ("08-encore.svg", p08),
    ("09-je-n-en-peux-plus.svg", p09), ("10-vous-etes-deux.svg", p10), ("11-pardon.svg", p11), ("12-les-carottes.svg", p12),
]
