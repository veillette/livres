"""Lili la licorne et les couleurs perdues — partager son chagrin avec ses amis."""
from base import *
from objets import *
from fantastique import *

ID = "licorne-couleurs"
GRIS = "#adb5bd"
R, O, J, V, B, VI = ARC_EN_CIEL


def criniere(nb):
    """Les `nb` premières couleurs retrouvées, le reste encore gris."""
    return list(ARC_EN_CIEL[:nb]) + [GRIS] * (6 - nb)


def lili(x, y, s=1.0, nb=6, **k):
    return licorne(x, y, s, criniere=criniere(nb), **k)


def vallee(S, gris=False):
    if gris:
        ciel(S, "#ced4da", "#f1f3f5")
        collines(S, 600, "#dee2e6", graine=2)
        sol(S, 600, "#ced4da")
        return
    ciel(S, "#d0ebff", "#fff0f6")
    S.add(nuage(140, 120, 0.7), nuage(660, 90, 0.55))
    collines(S, 600, "#b2f2bb", graine=2)
    sol(S, 600, "#8ce99a")


def fleurs(S, y=760):
    for x, c in [(60, "#ff8787"), (130, "#ffd43b"), (690, "#cc5de8"), (750, "#74c0fc")]:
        S.add(fleur(x, y + (x % 3) * 10, 0.9, c))


def fraise(x, y, s=1.0):
    m = [chemin("M 0 40 Q -40 10 -34 -16 Q -26 -34 0 -30 Q 26 -34 34 -16 Q 40 10 0 40 Z", "#fa5252")]
    for px, py in [(-16, -10), (0, -4), (16, -10), (-10, 10), (10, 10), (0, 24)]:
        m.append(ellipse(px, py, 2.5, 3.5, "#ffe066"))
    m.append(chemin("M -22 -30 L -8 -24 L 0 -40 L 8 -24 L 22 -30 L 10 -18 L -10 -18 Z", "#40c057"))
    return place(m, x, y, s)


def feuille_automne(x, y, s=1.0, rot=0, couleur="#ff922b"):
    m = [chemin("M 0 40 Q -50 0 -30 -30 Q -10 -50 0 -60 Q 10 -50 30 -30 Q 50 0 0 40 Z", couleur),
         chemin("M 0 50 L 0 -50 M 0 0 L -20 -20 M 0 16 L 20 -6", stroke=_nerv(couleur), sw=3)]
    return place(m, x, y, s, rot=rot)


def _nerv(c):
    return assombrir(c, 0.8)


def violette(x, y, s=1.0):
    m = [trait(0, 0, 0, -60, "#40c057", 5), ellipse(12, -24, 14, 6, "#51cf66", rot=-30)]
    for k in range(5):
        a = math.radians(-90 + k * 72)
        m.append(ellipse(math.cos(a) * 12, -66 + math.sin(a) * 12, 12, 9, "#9775fa", rot=k * 72))
    m.append(cercle(0, -66, 6, "#ffd43b"))
    return place(m, x, y, s)


def meche(x, y, couleur, s=1.0):
    """Petite étoile de couleur qui vole vers la crinière."""
    return g([cercle(x, y, 30 * s, couleur, opacity=0.25), etoile5(x, y, 16 * s, couleur)])


def couverture():
    S = Scene()
    vallee(S)
    S.add(arc_en_ciel(400, 620, 330, 26))
    S.add(lili(380, 740, 1.55, expr="rire", galop=True))
    fleurs(S)
    S.add(etincelles(600, 360, 1.0, graine=3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lili(180, 262, 0.82, expr="content"))
    return S


def p01():
    S = Scene()
    vallee(S)
    S.add(arc_en_ciel(400, 560, 300, 22))
    S.add(lili(360, 740, 1.5, expr="content"))
    fleurs(S)
    S.add(papillon(650, 480, 0.9))
    return S


def p02():
    S = Scene()
    vallee(S, gris=True)
    S.add(lili(360, 740, 1.5, nb=0, expr="pleure", larmes=True, regard=(0, 1)))
    S.add(bulle(560, 150, 420, 110, "Où sont passées\nmes couleurs ?", 40, pointe=(560, 330)))
    return S


def p03():
    S = Scene()
    vallee(S)
    S.add(lili(300, 740, 1.3, nb=0, expr="triste"))
    S.add(perso("renard", 600, 780, 1.1, expr="sourire", bras="salut", regard=(-1, 0)))
    S.add(perso("grenouille", 470, 790, 0.8, expr="joie", bras="haut"))
    S.add(chouette(640, 470, 0.8, expr="sourire", regard=(-1, 0)))
    S.add(papillon(160, 320, 0.9), coccinelle(100, 780, 1.4))
    S.add(bulle(560, 150, 420, 100, "Nous allons t'aider !", 38, pointe=(600, 300)))
    return S


def page_couleur(nb, couleur, ami, cadeau, mot):
    """Un ami offre une couleur : Lili à gauche, l'ami à droite."""
    S = Scene()
    vallee(S)
    S.add(lili(270, 750, 1.25, nb=nb, expr="rire", regard=(1, 0)))
    S.add(ami)
    S.add(cadeau)
    S.add(meche(360, 380, couleur, 1.4))
    S.add(texte(560, 150, mot, 84, couleur, contour="#fff"))
    return S


def p04():
    return page_couleur(1, R, coccinelle(640, 740, 2.4),
                        fraise(560, 640, 1.6), "ROUGE !")


def p05():
    return page_couleur(2, O, perso("renard", 620, 780, 1.15, expr="rire", bras="tient", flip=True),
                        feuille_automne(540, 590, 1.3, rot=-20), "ORANGE !")


def p06():
    S = page_couleur(3, J, soleil(620, 460, 90, visage=True), "", "JAUNE !")
    return S


def p07():
    return page_couleur(4, V, perso("grenouille", 620, 780, 1.2, expr="rire", bras="haut"),
                        g([herbe(520, 780, 1.6), herbe(720, 790, 1.4)]), "VERT !")


def p08():
    S = Scene()
    vallee(S)
    S.add(ellipse(560, 730, 260, 80, "#4dabf7"))
    S.add(chemin("M 380 720 q 20 -10 40 0 M 600 750 q 20 -10 40 0 M 500 700 q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    S.add(poisson(600, 690, 1.3, "#ff922b", expr="rire", flip=True, rot=-20))
    S.add(goutte(520, 610, 1.4, "#74c0fc"), goutte(670, 590, 1.2, "#74c0fc"))
    S.add(lili(230, 750, 1.2, nb=5, expr="rire", regard=(1, 0)))
    S.add(meche(330, 380, B, 1.4))
    S.add(texte(560, 150, "BLEU !", 84, B, contour="#fff"))
    return S


def p09():
    return page_couleur(6, VI, papillon(620, 560, 1.8, "#9775fa", "#e5dbff"),
                        g([violette(560, 780, 1.4), violette(680, 790, 1.2)]), "VIOLET !")


def p10():
    S = Scene()
    vallee(S)
    S.add(ellipse(420, 740, 360, 70, "#74c0fc"))
    cid = uid("c")
    S.add(el("clipPath", ellipse(420, 740, 350, 62, "#000"), id=cid))
    S.add(g(g(lili(0, 0, 1.3, expr="rire"), transform="translate(360 706) scale(1 -0.4)", opacity=0.4), clip_path=f"url(#{cid})"))
    S.add(lili(360, 700, 1.3, expr="rire"))
    S.add(etincelles(560, 300, 1.2, graine=8), etincelles(200, 260, 0.8, graine=5))
    S.add(bulle(580, 120, 380, 90, "Merci, mes amis !", 38))
    return S


def p11():
    S = Scene()
    ciel(S, "#e5dbff", "#fff0f6")
    collines(S, 620, "#b2f2bb", graine=6)
    sol(S, 620, "#8ce99a")
    S.add(arbre(620, 640, 1.3, "#69db7c", "#51cf66"))
    S.add(chouette(620, 400, 0.9, expr="content", ailes="ouvertes", acc=("lunettes",), regard=(-1, 0)))
    S.add(lili(270, 750, 1.3, expr="sourire", regard=(1, -1)))
    S.add(coeur(460, 230, 1.8), coeur(520, 170, 1.1, "#cc5de8"))
    return S


def p12():
    S = Scene()
    nuit(S, "#3b2c85", "#9775fa")
    etoiles(S, 40, graine=4)
    S.add(arc_en_ciel(400, 820, 420, 30))
    S.add(lili(400, 560, 1.3, expr="rire", galop=True, rot=-12))
    S.add(etincelles(180, 520, 1.0, graine=2), etincelles(620, 300, 1.0, graine=9))
    S.add(lune(660, 120, 40))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lili-seule.svg", vignette),
    ("01-la-vallee.svg", p01), ("02-toute-grise.svg", p02), ("03-les-amis.svg", p03),
    ("04-rouge.svg", p04), ("05-orange.svg", p05), ("06-jaune.svg", p06),
    ("07-vert.svg", p07), ("08-bleu.svg", p08), ("09-violet.svg", p09),
    ("10-le-reflet.svg", p10), ("11-chouette.svg", p11), ("12-arc-en-ciel.svg", p12),
]
