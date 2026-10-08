"""Dans la grotte — une visite inspirée de Mammoth Cave, au Kentucky.

Faits retenus : la plus longue grotte connue au monde (plus de 680 km de
galeries explorées) ; environ 12 °C toute l'année ; creusée pendant des
millions d'années par l'eau de pluie qui dissout le calcaire ; l'écho ;
stalactites (au plafond) et stalagmites (au sol) qui grandissent très
lentement ; rivière souterraine avec des poissons blancs sans yeux ;
chauves-souris qui hibernent et qu'il ne faut pas déranger ; le noir total
quand on éteint les lumières.
"""
from base import *
from objets import *
from sciences import *
from fantastique import personne

ID = "dans-la-grotte"
THEO = dict(peau="rosee", cheveux="chatain", coiffure="courts", habit="#f76707", robe=False, jambes="#364fc7")
LILI = dict(peau="rosee", cheveux="chatain", coiffure="tresses", habit="#e64980", robe=True)
MAMAN = dict(peau="rosee", cheveux="brun", coiffure="longs", habit="#1c7ed6", robe=False, jambes="#343a40")
ROCHE = "#4a3b5c"
ROCHE2 = "#5f4b74"


def chapeau_garde():
    return g([ellipse(0, -194, 80, 14, "#8d6e4a"), chemin("M -40 -196 L -34 -240 Q 0 -256 34 -240 L 40 -196 Z", "#a68a64"),
              rect(-40, -206, 80, 10, "#5c3a1e")])


def theo(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**THEO, **k})


def lili(x=0, y=0, s=0.85, **k):
    return personne(x, y, s, **{**LILI, **k})


def maman(x=0, y=0, s=1.3, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def garde(x=0, y=0, s=1.35, **k):
    return personne(x, y, s, **{**dict(peau="foncee", cheveux="noir", coiffure="chignon", habit="#adb5bd", robe=False,
                                       jambes="#2b8a3e", coiffe=chapeau_garde(), tenue=place(etoile5(0, 0, 9, "#fab005"), -18, -88)), **k})


def stalactite(x, y, l=80, w=26, c="#d9c7b0"):
    return poly([(x - w / 2, y), (x + w / 2, y), (x, y + l)], c)


def stalagmite(x, y, l=80, w=34, c="#cdb89e"):
    return chemin(f"M {x - w / 2} {y} Q {x - w / 4} {y - l * 0.6} {x} {y - l} Q {x + w / 4} {y - l * 0.6} {x + w / 2} {y} Z", c)


def caverne(S, sol_y=640, graine=1, lumiere=None, stalactites=True):
    """Intérieur de la grotte : fond sombre, voûte et sol rocheux, quelques stalactites."""
    fond(S, "#2b2238")
    if lumiere:
        x, y, r = lumiere
        S.add(cercle(x, y, r, degrade_radial(S, "#ffe8a3", "#2b223800")))
    r_ = random.Random(graine)
    voute = "M 0 0 L 800 0 L 800 120 " + " ".join(
        f"Q {n(800 - k * 100 - 50)} {n(r_.uniform(140, 200))} {n(800 - (k + 1) * 100)} {n(r_.uniform(100, 140))}" for k in range(8)) + " Z"
    S.add(chemin(voute, ROCHE))
    S.add(chemin(f"M 0 {sol_y} Q 200 {sol_y - 30} 400 {sol_y} T 800 {sol_y - 10} L 800 800 L 0 800 Z", ROCHE2))
    if stalactites:
        for k in range(9):
            x = 40 + k * 90 + r_.uniform(-20, 20)
            S.add(stalactite(x, r_.uniform(110, 150), r_.uniform(40, 100), r_.uniform(16, 28)))


def lampe_mur(x, y):
    return g([cercle(x, y, 60, "#ffe8a3", opacity=0.25), cercle(x, y, 14, "#ffe066"), rect(x - 4, y + 10, 8, 30, "#495057")])


def poisson_aveugle(x, y, s=1.0, flip=False):
    return place([ellipse(0, 0, 44, 16, "#f8f0fc"), poly([(-40, 0), (-66, -16), (-66, 16)], "#f3d9fa"),
                  ellipse(6, 4, 22, 6, "#fcc2d7", opacity=0.6)], x, y, s, flip=flip)


def crevette(x, y, s=1.0):
    return place([chemin("M -20 0 Q 0 -16 20 0 Q 0 6 -20 0 Z", "#f8f9fa"), trait(20, 0, 34, -12, "#f8f9fa", 2), trait(20, 0, 36, -4, "#f8f9fa", 2)], x, y, s)


def chauve_souris_dort(x, y, s=1.0):
    """Chauve-souris endormie, accrochée la tête en bas ; (x, y) = les pattes au plafond."""
    return place([trait(-6, 0, -6, 12, "#343a40", 3), trait(6, 0, 6, 12, "#343a40", 3),
                  ellipse(0, 40, 22, 34, "#5f3dc4"), cercle(0, 76, 16, "#7048e8"),
                  poly([(-12, 86), (-18, 102), (-4, 90)], "#7048e8"), poly([(12, 86), (18, 102), (4, 90)], "#7048e8"),
                  chemin("M -8 74 Q -4 78 0 74", stroke=ENCRE, sw=2), chemin("M 0 74 Q 4 78 8 74", stroke=ENCRE, sw=2)], x, y, s)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    caverne(S, 660, 2, lumiere=(400, 520, 420))
    for x, l in ((120, 120), (640, 150), (720, 90)):
        S.add(stalagmite(x, 680, l))
    S.add(theo(330, 760, 1.4, expr="bouche_bee", bras="tient", regard=(1, -1), objet=lampe_poche(68, -146, 0.8, rot=-40, faisceau=260)))
    S.add(lili(470, 760, 1.1, expr="content", regard=(-1, -1)))
    S.add(chauve_souris_dort(560, 170, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(theo(200, 262, 1.0, expr="content", bras="tient", objet=lampe_poche(68, -146, 0.6, rot=-40)))
    return S


def p01():
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(soleil(680, 100, 55))
    S.add(chemin("M -40 640 Q 200 260 520 300 Q 760 330 840 560 L 840 800 L -40 800 Z", "#2f9e44"))
    S.add(chemin("M 260 640 Q 270 440 400 430 Q 530 440 540 640 Z", "#1b1625"))
    S.add(chemin("M 250 640 Q 262 420 400 410 Q 538 420 550 640", stroke="#868e96", sw=26))
    for x in (110, 640, 720):
        S.add(arbre(x, 640, 0.9, "#40c057", "#2f9e44"))
    S.add(rect(0, 640, 800, 160, "#94d82d"))
    S.add(vent(330, 560, 0.8, "#d0ebff", rot=180), vent(420, 520, 0.6, "#d0ebff", rot=180))
    S.add(maman(560, 790, 1.3, expr="content", regard=(-1, -1)))
    S.add(theo(200, 790, 1.15, expr="rire", bras="ouverts", regard=(1, -1)))
    S.add(lili(330, 790, 0.85, expr="surpris"))
    S.add(texte(400, 380, "Brrr !", 46, "#1c7ed6", contour="#fff"))
    return S


def p02():
    S = Scene()
    caverne(S, 700, 3, lumiere=(400, 450, 380))
    S.add(lampe_mur(120, 330), lampe_mur(680, 330))
    for k in range(5):
        S.add(rect(140 + k * 60, 560 + k * 30, 120, 22, "#868e96"))
    S.add(trait(130, 520, 430, 680, "#adb5bd", 6))
    S.add(garde(600, 780, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(theo(330, 770, 1.1, habit="#7048e8", expr="sourire", regard=(1, 0)))
    S.add(texte(400, 250, "12 °C", 70, "#a5d8ff", contour="#2b2238"))
    return S


def p03():
    S = Scene()
    caverne(S, 690, 4, lumiere=(400, 470, 520))
    for x, l in ((60, 140), (740, 160), (680, 90)):
        S.add(stalagmite(x, 700, l))
    S.add(lampe_mur(400, 260))
    S.add(maman(260, 780, 0.8, expr="bouche_bee", regard=(1, -1)))
    S.add(theo(360, 780, 0.65, habit="#7048e8", expr="bouche_bee", regard=(0, -1)))
    S.add(lili(430, 780, 0.5, expr="bouche_bee", regard=(0, -1)))
    S.add(garde(540, 785, 0.85, expr="content", bras="ouverts"))
    S.add(texte(400, 420, "plus de 680 km !", 56, "#ffe066", contour="#2b2238"))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    nuage_ = nuage(400, 70, 1.4, "#ced4da", ombre="#adb5bd")
    S.add(nuage_)
    pluie(S, 25, 4, zone=(250, 110, 560, 230))
    S.add(rect(0, 230, 800, 30, "#69db7c"))
    S.add(rect(0, 260, 800, 540, "#e9dcc5"))
    for y in range(300, 800, 60):
        S.add(trait(0, y, 800, y, "#d9c7b0", 4))
    # fissures, puis tunnels creusés par l'eau
    S.add(chemin("M 380 260 L 360 330 L 400 400 L 380 470", stroke="#a68a64", sw=6))
    S.add(chemin("M 120 560 Q 240 500 380 560 Q 520 620 700 540 L 700 640 Q 520 720 380 660 Q 240 600 120 660 Z", "#2b2238"))
    for k in range(6):
        S.add(goutte(370 + (k % 2) * 16, 300 + k * 40, 0.9, "#4dabf7"))
    S.add(texte(560, 360, "le calcaire", 38, "#7c4a1e", contour="#fff"))
    S.add(texte(410, 740, "des millions d'années !", 44, "#5f3dc4", contour="#fff"))
    S.cachette(730, 630, "air")
    return S


def p05():
    S = Scene()
    caverne(S, 690, 5, lumiere=(250, 480, 360))
    S.add(theo(250, 780, 1.35, habit="#7048e8", expr="joie", bras="bouche", regard=(1, -1)))
    S.add(texte(250, 360, "Ohé !", 64, "#ffe066", contour="#2b2238"))
    for k, (x, y, t) in enumerate(((470, 300, 52), (590, 380, 40), (690, 450, 30))):
        S.add(g(texte(x, y, "ohé…", t, "#ffe066", contour="#2b2238"), opacity=0.9 - k * 0.25))
    S.add(ondes(330, 450, 60, 3, 30, -10, 60, "#ffe066", 5))
    S.add(ondes(760, 420, 60, 2, 30, 180, 60, "#ffe066", 4, opacity=0.5))
    return S


def p06():
    S = Scene()
    caverne(S, 700, 6, lumiere=(400, 420, 460), stalactites=False)
    for x, l, w in ((150, 260, 50), (300, 200, 40), (470, 300, 56), (620, 180, 40)):
        S.add(stalactite(x, 140, l, w))
    for x, l, w in ((150, 200, 70), (300, 150, 60), (470, 140, 80), (620, 230, 70)):
        S.add(stalagmite(x, 720, l, w))
    S.add(goutte(470, 470, 1.4, "#a5d8ff"), goutte(300, 380, 1.1, "#a5d8ff"))
    S.add(texte(200, 120, "stalactite", 34, "#ffe066", contour="#2b2238"))
    S.add(texte(620, 780, "stalagmite", 34, "#ffe066", contour="#2b2238"))
    S.add(texte(470, 560, "ploc…", 44, "#a5d8ff", contour="#2b2238"))
    return S


def p07():
    S = Scene()
    caverne(S, 520, 7, lumiere=(420, 420, 420))
    S.add(rect(0, 560, 800, 240, S.degrade(["#1864ab", "#0b3d6b"])))
    S.add(chemin("M 0 560 " + " ".join("q 25 -10 50 0" for _ in range(16)), stroke="#4dabf7", sw=5))
    S.add(poisson_aveugle(260, 660, 1.6), poisson_aveugle(560, 720, 1.2, flip=True), crevette(640, 620, 1.2))
    S.add(theo(300, 530, 0.95, habit="#7048e8", expr="bouche_bee", regard=(1, 1)))
    S.add(garde(470, 535, 1.0, expr="content", bras="montre", regard=(-1, 1), flip=True))
    return S


def p08():
    S = Scene()
    caverne(S, 690, 8, lumiere=(400, 300, 380), stalactites=False)
    for k in range(7):
        S.add(chauve_souris_dort(110 + k * 95, 130 + (k % 2) * 20, 1.0))
    S.add(theo(300, 780, 1.3, habit="#7048e8", expr="surpris", bras="bouche", regard=(1, -1)))
    S.add(lili(470, 780, 1.0, expr="timide", bras="chut", regard=(-1, -1)))
    S.add(texte(400, 450, "Chut…", 60, "#e5dbff", contour="#2b2238"))
    S.add(zzz(560, 300, 0.9, "#e5dbff"))
    return S


def p09():
    S = Scene()
    fond(S, "#0b0a10")
    S.add(theo(400, 780, 1.4, habit="#7048e8", expr="surpris", bras="tient", regard=(1, -1)))
    S.add(rect(0, 0, 800, 800, "#0b0a10", opacity=0.93))
    S.add(texte(400, 300, "Tout noir !", 64, "#495057"))
    S.add(texte(400, 380, "Je ne vois même pas ma main…", 34, "#495057", poids=600))
    S.cachette(710, 70, "air")
    return S


def p10():
    S = Scene()
    ciel(S, "#4dabf7", "#fff3bf")
    S.add(soleil(640, 120, 70, visage=True))
    S.add(chemin("M -40 520 Q 160 360 360 420 L 360 800 L -40 800 Z", "#2f9e44"))
    S.add(chemin("M 60 600 Q 70 460 180 450 Q 290 460 300 600 Z", "#1b1625"))
    S.add(rect(0, 600, 800, 200, "#94d82d"))
    S.add(arbre(700, 620, 0.9))
    S.add(maman(420, 780, 1.3, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(theo(560, 780, 1.15, expr="rire", bras="haut"))
    S.add(lili(660, 780, 0.85, expr="rire", bras="haut"))
    S.add(texte(560, 330, "Au revoir, la grotte !", 40, "#e8590c", contour="#fff"))
    return S


def p11():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    # une grotte de couvertures entre deux chaises
    S.add(chemin("M 120 760 L 160 420 Q 400 360 640 420 L 680 760 Z", "#e599f7"))
    S.add(chemin("M 260 760 Q 270 560 400 550 Q 530 560 540 760 Z", "#1b1625"))
    for k in range(4):
        S.add(trait(170 + k * 160, 420, 150 + k * 170, 760, "#cc5de8", 4))
    S.add(cercle(420, 650, 120, degrade_radial(S, "#ffe8a3", "#1b162500")))
    S.add(theo(360, 770, 0.95, expr="rire", bras="tient", objet=lampe_poche(68, -146, 0.6, rot=-20)))
    S.add(lili(470, 770, 0.8, expr="rire", bras="bouche"))
    S.add(texte(400, 250, "Ohé !", 64, "#ffe066", contour="#3b2a7a"))
    S.cachette(480, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("theo-seul.svg", vignette),
    ("01-l-entree.svg", p01), ("02-12-degres.svg", p02), ("03-la-plus-longue.svg", p03),
    ("04-l-eau-qui-creuse.svg", p04), ("05-l-echo.svg", p05), ("06-stalactites.svg", p06),
    ("07-la-riviere.svg", p07), ("08-les-chauves-souris.svg", p08), ("09-tout-noir.svg", p09),
    ("10-dehors.svg", p10), ("11-ma-grotte.svg", p11),
]
