"""Le Rat de ville et le Rat des champs — un repas tranquille vaut mieux qu'un festin plein de peur."""
from fables import *

ID = "rat-ville-champs"


def haut_de_forme(x, y, s=1.0, couleur="#343a40", ruban="#e64980"):
    m = [ellipse(0, 0, 52, 11, couleur), rect(-32, -76, 64, 76, couleur, rx=4),
         rect(-32, -22, 64, 14, ruban), ellipse(0, -76, 32, 7, assombrir(couleur, 0.8))]
    return place(m, x, y, s)


def rat_champs(x, y, s=1.0, **k):
    return perso("rat", x, y, s, acc=("chapeau",), couleur_acc="#e0a93a", **k)


def rat_ville(x, y, s=1.0, flip=False, **k):
    return g([perso("rat", x, y, s, habit="#495057", acc=("echarpe",), couleur_acc="#e64980", flip=flip, **k),
              haut_de_forme(x, y - 196 * s, s * 0.9)])


def pommier_maison(x, y, s=1.0, lumiere=False):
    """Vieux pommier avec une petite porte ronde entre les racines."""
    m = [arbre(0, 0, 1.6, feuillage="#51cf66", feuillage2="#40c057", tronc="#8d5524", fruits="#fa5252"),
         chemin("M -40 0 Q -70 -10 -90 6 M 40 0 Q 70 -10 94 4", stroke="#8d5524", sw=14),
         chemin("M -22 0 Q -22 -54 0 -54 Q 22 -54 22 0 Z", "#ffe066" if lumiere else "#5c3a1e"),
         cercle(12, -24, 3.5, "#fcc419")]
    return place(m, x, y, s)


def campagne(S, nuit_=False):
    if nuit_:
        nuit(S)
        etoiles(S, 40, graine=2)
        S.add(lune(640, 120, 40))
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(soleil(680, 120, 50))
    collines(S, 600, "#8ce99a" if not nuit_ else "#2b8a3e", graine=11)
    sol(S, 620, "#b2f2bb" if not nuit_ else "#2f9e44")
    if not nuit_:
        S.add(fleur(720, 720, 0.9, "#ff8787"), fleur(760, 700, 0.7, "#cc5de8"), herbe(80, 740, 1.2))


def souche(x, y, s=1.0):
    m = [chemin("M -90 0 L -80 -80 L 80 -80 L 90 0 Z", "#a0693a"), ellipse(0, -80, 80, 22, "#e0b78a"),
         ellipse(0, -80, 50, 13, "none", stroke="#c68642", stroke_width=3), ellipse(0, -80, 24, 6, "none", stroke="#c68642", stroke_width=3)]
    return place(m, x, y, s)


def repas_champs(x, y, s=1.0):
    m = [grain(-40, -8, 1.2), grain(-20, -12, 1.2), grain(-30, 6, 1.2),
         g([ellipse(24, -6, 18, 16, "#c68642"), chemin("M 8 -14 Q 24 -30 40 -14 Z", "#8d5524")]),
         g([chemin("M 50 8 Q 60 -24 84 -10 Q 90 10 50 8 Z", "#fff4e6"), chemin("M 50 8 Q 60 -24 84 -10", stroke="#fa5252", sw=5)])]
    return place(m, x, y, s)


def salle(S):
    salle_manger(S)
    S.add(tapis(400, 740, 330, 50, "#e599f7", "#be4bdb"))


def trou_mur(x, y, s=1.0, dedans=None):
    m = [chemin("M -80 0 Q -80 -110 0 -110 Q 80 -110 80 0 Z", "#212529")]
    if dedans:
        m.append(dedans)
    return place(m, x, y, s)


def couverture():
    S = Scene()
    salle(S)
    S.add(festin(400, 800, 1.3))
    S.add(rat_champs(250, 610, 1.1, expr="surpris", bras="joues"))
    S.add(rat_ville(550, 610, 1.1, expr="fier", bras="ouverts"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fromage(200, 150, 3.0))
    return S


def p01():
    S = Scene()
    campagne(S)
    S.add(pommier_maison(420, 680, 1.0))
    S.add(rat_champs(250, 740, 1.3, expr="content", bras="salut"))
    return S


def p02():
    S = Scene()
    campagne(S)
    S.add(pommier_maison(620, 680, 0.9))
    S.add(rat_champs(230, 740, 1.2, expr="rire", bras="ouverts"))
    S.add(rat_ville(470, 740, 1.2, expr="fier", bras="salut", flip=True))
    S.add(bulle(400, 130, 420, 90, "Bonjour, cousin !", 38, pointe=(260, 400)))
    return S


def p03():
    S = Scene()
    campagne(S)
    S.add(pommier_maison(700, 680, 0.7))
    S.add(souche(400, 720, 1.4))
    S.add(repas_champs(400, 608, 1.3))
    S.add(rat_champs(170, 760, 1.1, expr="content", bras="donne"))
    S.add(rat_ville(630, 760, 1.1, expr="neutre", bras="bas"))
    return S


def p04():
    S = Scene()
    campagne(S)
    S.add(souche(260, 720, 1.2))
    S.add(repas_champs(260, 624, 1.1))
    S.add(rat_ville(520, 760, 1.4, expr="degoute", bras="croises"))
    S.add(bulle(470, 130, 460, 110, "Des graines ? Pouah !\nViens chez moi, en ville !", 32, pointe=(520, 320)))
    return S


def p05():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    ville(S, 600)
    sol(S, 600, "#adb5bd")
    S.add(rect(0, 640, 800, 30, "#868e96"))
    S.add(rat_champs(300, 760, 1.1, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(rat_ville(480, 760, 1.1, expr="fier", bras="montre"))
    return S


def p06():
    S = Scene()
    salle(S)
    S.add(festin(400, 790, 1.65))
    S.add(paillettes(120, 330, 1.2), paillettes(680, 330, 1.2))
    return S


def p07():
    S = Scene()
    salle(S)
    S.add(festin(400, 790, 1.0))
    S.add(rat_champs(230, 640, 1.0, expr="bouche_bee", bras="joues"))
    S.add(rat_ville(570, 640, 1.0, expr="rire", bras="ouverts"))
    S.add(bulle(560, 150, 340, 90, "Sers-toi !", 44, pointe=(560, 380)))
    return S


def p08():
    S = Scene()
    salle(S)
    S.add(festin(400, 790, 1.0))
    S.add(rat_champs(240, 640, 1.0, expr="miam", bras="porte", objet=fromage(0, -80, 0.8)))
    S.add(rat_ville(560, 640, 1.0, expr="miam", bras="porte", objet=part_gateau(0, -70, 0.6)))
    S.add(texte(400, 200, "Miam !", 70, "#be4bdb", contour="#fff"))
    return S


def p09():
    S = Scene()
    salle(S)
    S.add(porte(700, 590, 140, 320, "#a0522d", ouverte=True))
    S.add(festin(340, 790, 1.0))
    S.add(rat_champs(180, 640, 0.9, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(rat_ville(470, 640, 0.9, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(texte(560, 180, "GRRRIIIC !", 56, "#495057", contour="#fff"))
    return S


def p10():
    S = Scene()
    salle(S)
    S.add(porte(700, 590, 140, 320, "#a0522d", ouverte=True))
    S.add(perso("chat", 600, 760, 1.7, expr="malin", bras="ouverts", couleur="#868e96"))
    S.add(rat_champs(170, 760, 0.8, expr="oups", bras="course", flip=True))
    S.add(rat_ville(330, 760, 0.8, expr="oups", bras="course", flip=True))
    S.add(mouvement(420, 700, 1.0))
    S.add(bulle(250, 150, 300, 90, "Le chat !", 48, pointe=(300, 560)))
    return S


def p11():
    S = Scene()
    fond(S, "#fff0f6")
    S.add(rect(0, 520, 800, 280, "#c9a27e"))
    S.add(rect(0, 500, 800, 30, "#d9a066"))
    S.add(trou_mur(250, 520, 1.6, dedans=g([rat_champs(-30, 0, 0.3, expr="oups"), rat_ville(30, 0, 0.3, expr="oups")])))
    S.add(perso("chat", 580, 800, 1.9, expr="malin", bras="bas", couleur="#868e96", regard=(-1, 0)))
    S.cachette(120, 660)
    return S


def p12():
    S = Scene()
    salle(S)
    S.add(porte(700, 590, 140, 320, "#a0522d", ouverte=True))
    S.add(festin(340, 790, 1.0))
    S.add(rat_champs(180, 640, 0.9, expr="oups", bras="haut"))
    S.add(rat_ville(470, 640, 0.9, expr="oups", bras="haut"))
    S.add(texte(560, 180, "BOUM !", 72, "#c92a2a", contour="#fff"))
    S.add(eclat(700, 440, 1.2, "#ffe066"))
    return S


def p13():
    S = Scene()
    salle(S)
    S.add(rat_champs(260, 760, 1.4, expr="neutre", bras="coucou", objet=None))
    S.add(sac(120, 760, 0.7))
    S.add(rat_ville(560, 760, 1.3, expr="surpris", bras="joues"))
    S.add(bulle(300, 130, 460, 100, "Merci, mais je rentre !", 34, pointe=(270, 330)))
    return S


def p14():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    ville(S, 600)
    sol(S, 600, "#adb5bd")
    S.add(rect(0, 640, 800, 30, "#868e96"))
    S.add(rat_ville(230, 760, 1.2, expr="triste", bras="ouverts"))
    S.add(rat_champs(560, 760, 1.2, expr="content", bras="salut", flip=True))
    S.add(bulle(560, 130, 420, 110, "Chez moi, je mange\nen paix !", 34, pointe=(560, 360)))
    return S


def p15():
    S = Scene()
    campagne(S, nuit_=True)
    S.add(pommier_maison(560, 680, 1.0, lumiere=True))
    S.add(rat_champs(290, 750, 1.4, expr="content", bras="porte", objet=grain(0, -80, 1.8)))
    S.add(coeur(180, 400, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fromage-seul.svg", vignette),
    ("01-le-rat-des-champs.svg", p01), ("02-le-cousin.svg", p02), ("03-le-repas.svg", p03),
    ("04-pouah.svg", p04), ("05-la-ville.svg", p05), ("06-le-festin.svg", p06),
    ("07-sers-toi.svg", p07), ("08-miam.svg", p08), ("09-grrriiic.svg", p09),
    ("10-le-chat.svg", p10), ("11-caches.svg", p11), ("12-boum.svg", p12),
    ("13-je-rentre.svg", p13), ("14-en-paix.svg", p14), ("15-sous-les-etoiles.svg", p15),
]
