"""Les Deux Pigeons — l'absence est le plus grand des maux.

Adaptation douce : le chasseur à la fronde de la fable devient le chat de la
ferme ; Gris-Gris rentre l'aile froissée et Perle le soigne.
"""
from fables import *

ID = "deux-pigeons"
GRIS = dict(couleur="#868e96", ventre="#dee2e6")
PERLE = dict(couleur="#e9ecef", ventre="#ffffff", acc=("noeud",))


def gris(x, y, s=1.0, **k):
    return oiseau(x, y, s, **{**GRIS, **k})


def perle(x, y, s=1.0, **k):
    return oiseau(x, y, s, **{**PERLE, **k})


def pigeon_vol(x, y, s=1.0, flip=False, expr="sourire", couleur="#868e96", aile="#adb5bd", froisse=False, rot=0):
    """Pigeon en vol, de profil (tête à droite) ; (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -40 0 L -86 -18 L -80 10 Z", assombrir(couleur, 0.8)),
         ellipse(0, 0, 50, 26, couleur),
         cercle(46, -16, 22, couleur),
         ellipse(40, 0, 16, 10, "#9775fa", opacity=0.5),
         poly([(64, -18), (82, -12), (64, -8)], "#ff922b"),
         ellipse(52, -6, 5, 3, ROSE, opacity=0.8),
         oeil(52, -20, ys, (1, 0), taille=0.7)]
    if froisse:
        m.insert(2, chemin("M -20 -8 Q -30 -50 -6 -70 L 0 -52 L 14 -74 L 20 -10 Z", aile))
    else:
        m.insert(2, chemin("M -20 -8 Q -10 -90 50 -104 Q 26 -60 20 -10 Z", aile))
    return place(m, x, y, s, flip=flip, rot=rot)


def rapace(x, y, s=1.0, couleur="#8d5524", flip=False, rot=0):
    m = [chemin("M -120 -10 Q -60 -60 -10 -10 Q 60 -60 120 -10 Q 60 -30 10 10 Q -60 -30 -120 -10 Z", couleur),
         poly([(-14, 6), (14, 6), (0, 46)], assombrir(couleur, 0.85)),
         cercle(18, -6, 16, "#fff3bf"), cercle(22, -8, 3.5, ENCRE), trait(10, -18, 30, -14, ENCRE, 3),
         poly([(30, -8), (46, -2), (30, 2)], "#fab005")]
    return place(m, x, y, s, flip=flip, rot=rot)


def pigeonnier(x, y, s=1.0):
    m = [rect(-14, -200, 28, 200, "#a0693a"),
         rect(-110, -380, 220, 180, "#fff4e6"), poly([(-130, -380), (0, -470), (130, -380)], "#e8590c"),
         rect(-120, -206, 240, 16, "#c68642", rx=4)]
    for k in range(3):
        m.append(chemin(f"M {-80 + k * 60} -250 L {-80 + k * 60} -290 Q {-60 + k * 60} -320 {-40 + k * 60} -290 L {-40 + k * 60} -250 Z", "#495057"))
        m.append(rect(-90 + k * 60, -252, 60, 8, "#c68642", rx=3))
    return place(m, x, y, s)


def campagne(S, graine=1, ciel_=("#a5d8ff", "#fff9db"), soleil_=True):
    ciel(S, *ciel_)
    if soleil_:
        S.add(soleil(680, 110, 45))
    collines(S, 600, "#b2f2bb", graine=graine)
    sol(S, 640, "#8ce99a")


def maison_scene(S, graine=1):
    campagne(S, graine)
    S.add(pigeonnier(400, 820, 1.1))


def couverture():
    S = Scene()
    campagne(S, 2)
    S.add(pigeonnier(400, 840, 1.1))
    S.add(gris(310, 620, 1.8, expr="content", regard=(1, 0)))
    S.add(perle(490, 620, 1.8, expr="content", regard=(-1, 0)))
    S.add(coeur(400, 300, 1.2, "#ff8787"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(gris(150, 250, 1.0, expr="content", regard=(1, 0)), perle(250, 250, 1.0, expr="content", regard=(-1, 0)))
    S.add(coeur(200, 70, 0.6, "#ff8787"))
    return S


def p01():
    S = Scene()
    maison_scene(S, 1)
    S.add(gris(300, 600, 1.7, expr="content", regard=(1, 0)), perle(500, 600, 1.7, expr="content", regard=(-1, 0)))
    S.add(tas_grains(400, 600, 0.9))
    S.add(notes(640, 330, 1.0, "#868e96"), texte(150, 330, "Rrrou…", 48, "#868e96", contour="#fff"))
    return S


def p02():
    S = Scene()
    campagne(S, 2)
    S.add(montagnes(None, 620))
    S.add(pigeonnier(160, 800, 1.3))
    S.add(gris(160, 365, 1.0, expr="sourire", regard=(1, -0.5)))
    S.add(pensee(520, 250, 130, ville_mini(520, 280), depuis=(230, 300)))
    return S


def ville_mini(x, y):
    m = [rect(-80, -40, 40, 70, "#ffc9c9"), rect(-36, -70, 40, 100, "#a5d8ff"), rect(8, -50, 36, 80, "#ffec99"),
         rect(48, -30, 40, 60, "#b2f2bb")]
    m += [cercle(-60, -80, 14, "#ffd43b")]
    return place(m, x, y)


def p03():
    S = Scene()
    maison_scene(S, 3)
    S.add(gris(300, 600, 1.7, expr="neutre", regard=(1, 0)))
    S.add(perle(500, 600, 1.7, expr="pleure", regard=(-1, 0)))
    S.add(bulle(600, 150, 260, 90, "Reste !", 48, pointe=(520, 400)))
    return S


def p04():
    S = Scene()
    campagne(S, 4)
    S.add(pigeonnier(220, 800, 1.1))
    S.add(perle(220, 450, 1.5, expr="triste", ailes="haut", regard=(1, -1)))
    S.add(pigeon_vol(560, 260, 1.4, expr="rire"))
    S.add(texte(560, 120, "Trois jours !", 56, "#495057", contour="#fff"))
    return S


def p05():
    S = Scene()
    ciel(S, "#495057", "#868e96")
    S.add(nuage_orage(560, 110, 1.4), nuage(200, 90, 1.1, "#495057"))
    pluie(S, 90, 5, (0, 0, 800, 800), "#a5d8ff")
    collines(S, 600, "#5c940d", graine=5)
    sol(S, 640, "#2b8a3e")
    S.add(arbre(330, 660, 1.5, "#2f9e44", "#2b8a3e"))
    S.add(gris(400, 520, 1.4, expr="triste", ailes="bas"))
    S.add(g([goutte(370 + k * 30, 400 + (k % 2) * 20, 0.5, "#74c0fc") for k in range(3)]))
    return S


def p06():
    S = Scene()
    campagne(S, 6)
    champ_ble(S, 560, 6, 50)
    S.add(gris(400, 620, 1.1, expr="surpris", ailes="haut"))
    S.add(filet(200, 420, 400, 260, "#c68642", tendu=False))
    S.add(texte(600, 220, "Oh non !", 60, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    campagne(S, 7)
    champ_ble(S, 560, 7, 50)
    S.add(filet(120, 480, 300, 220, "#c68642", tendu=False))
    S.add(pigeon_vol(560, 330, 1.3, expr="joie"))
    for k in range(4):
        S.add(place(ellipse(0, 0, 8, 22, "#adb5bd"), 380 + k * 30, 470 - k * 30, rot=30 + k * 25))
    S.add(texte(560, 160, "Ouf !", 70, "#2f9e44", contour="#fff"))
    return S


def p08():
    S = Scene()
    campagne(S, 8)
    S.add(rapace(480, 220, 1.5, "#6d4c41", rot=20))
    S.add(ellipse(330, 680, 120, 22, "#000", opacity=0.15))
    S.add(pigeon_vol(330, 520, 1.1, expr="surpris", flip=True))
    return S


def p09():
    S = Scene()
    campagne(S, 9)
    S.add(rapace(300, 230, 1.3, "#6d4c41", rot=-15), rapace(470, 260, 1.6, "#8d5524", flip=True, rot=10))
    S.add(eclat(390, 250, 1.6, "#fab005"))
    S.add(g([place(ellipse(0, 0, 7, 18, "#a0693a"), 380 + k * 22, 330 + (k % 2) * 20, rot=k * 40) for k in range(5)]))
    S.add(pigeon_vol(640, 560, 1.0, expr="rire"), mouvement(520, 580, 1.0))
    return S


def p10():
    S = Scene()
    campagne(S, 10)
    S.add(maison(160, 640, 1.2), meule_foin(650, 650, 1.0))
    S.add(perso("chat", 330, 780, 1.1, expr="malin", bras="haut", couleur="#495057"))
    S.add(pigeon_vol(560, 380, 1.1, expr="oups", froisse=True, rot=-10))
    S.add(g([place(ellipse(0, 0, 7, 18, "#adb5bd"), 440 + k * 20, 470 + (k % 2) * 16, rot=k * 50) for k in range(4)]))
    return S


def p11():
    S = Scene()
    ciel(S, "#9775fa", "#ffc078")
    S.add(soleil(640, 520, 60, "#ff922b", rayons=False))
    collines(S, 600, "#69db7c", graine=11)
    sol(S, 640, "#51cf66")
    S.add(arbre(250, 660, 1.4, "#40c057", "#2f9e44"))
    S.add(gris(250, 480, 1.3, expr="triste", ailes="bas"))
    S.add(pensee(560, 230, 120, g([perle(530, 270, 0.6, expr="content"), place(pigeonnier(0, 0, 0.25), 600, 300)]), depuis=(300, 360)))
    return S


def p12():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=12)
    sol(S, 640, "#8ce99a")
    S.add(pigeonnier(640, 800, 1.0))
    S.add(chemin("M 80 260 Q 260 380 360 300 Q 460 220 520 340", stroke="#868e96", sw=4, stroke_dasharray="10 10"))
    S.add(pigeon_vol(520, 360, 1.0, expr="fier", froisse=True, rot=10))
    return S


def p13():
    S = Scene()
    maison_scene(S, 13)
    S.add(gris(300, 600, 1.7, expr="content", regard=(1, 0)))
    S.add(pansement(250, 520, 1.2, rot=20))
    S.add(perle(500, 600, 1.7, expr="pleure", ailes="haut", regard=(-1, 0)))
    S.add(coeur(400, 300, 1.2, "#ff8787"), coeur(480, 250, 0.7, "#ff8787"))
    return S


def p14():
    S = Scene()
    nuit(S)
    etoiles(S, 40, 14, (0, 0, 800, 500))
    S.add(lune(150, 120, 45))
    collines(S, 600, "#2b8a3e", graine=14)
    sol(S, 640, "#2f9e44")
    S.add(pigeonnier(400, 820, 1.1))
    S.add(gris(330, 600, 1.6, expr="content", regard=(1, 0)), perle(470, 600, 1.6, expr="content", regard=(-1, 0)))
    S.add(coeur(400, 330, 1.0, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pigeons-seuls.svg", vignette),
    ("01-au-pigeonnier.svg", p01), ("02-voir-le-monde.svg", p02), ("03-reste.svg", p03), ("04-le-depart.svg", p04),
    ("05-l-orage.svg", p05), ("06-le-filet.svg", p06), ("07-ouf.svg", p07), ("08-l-epervier.svg", p08),
    ("09-l-aigle.svg", p09), ("10-le-chat.svg", p10), ("11-perle-me-manque.svg", p11), ("12-le-retour.svg", p12),
    ("13-tu-es-revenu.svg", p13), ("14-ensemble.svg", p14),
]
