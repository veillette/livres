"""J'ai perdu ! — apprendre à perdre au jeu.

Tibo l'écureuil perd au jeu des noisettes et jette le dé. Ses amies s'en
vont. Mamie l'aide à accueillir sa tristesse et à souffler comme sur un
pissenlit ; il revient s'excuser, reperd… et découvre que le plus drôle,
c'est de jouer ensemble.
"""
from base import *
from objets import *

ID = "tibo-perdu"


def tibo(x, y, s=1.0, **k):
    return perso("ecureuil", x, y, s, **{**dict(habit="#fa5252"), **k})


def lola(x, y, s=0.95, **k):
    return perso("lapin", x, y, s, **{**dict(habit="#ffd43b", acc=("fleur",), couleur_acc="#f783ac"), **k})


def zelie(x, y, s=0.65, **k):
    return perso("souris", x, y, s, **{**dict(habit="#69db7c"), **k})


def mamie(x, y, s=1.15, **k):
    return perso("ecureuil", x, y, s, **{**dict(couleur="#b0846a", habit="#9775fa", acc=("lunettes",)), **k})


def de(x, y, s=1.0, face=5, rot=0):
    pts = {1: [(0, 0)], 2: [(-12, -12), (12, 12)], 3: [(-12, -12), (0, 0), (12, 12)],
           4: [(-12, -12), (12, -12), (-12, 12), (12, 12)], 5: [(-12, -12), (12, -12), (0, 0), (-12, 12), (12, 12)],
           6: [(-12, -14), (12, -14), (-12, 0), (12, 0), (-12, 14), (12, 14)]}[face]
    return place([rect(-26, -26, 52, 52, "#fff", rx=10, stroke="#adb5bd", stroke_width=3)] + [cercle(px, py, 5, ENCRE) for px, py in pts], x, y, s, rot=rot)


def pion(x, y, couleur, s=1.0):
    return place([ellipse(0, 0, 14, 6, "#495057"), poly([(-12, 0), (0, -34), (12, 0)], couleur), cercle(0, -36, 9, couleur)], x, y, s)


def plateau(x, y, s=1.0):
    """Plateau du jeu des noisettes vu en légère perspective ; (x, y) = centre."""
    m = [ellipse(0, 0, 250, 80, "#c68642"), ellipse(0, -6, 240, 74, "#ffe8cc")]
    couleurs = ["#ff8787", "#ffd43b", "#69db7c", "#74c0fc", "#b197fc"]
    for k in range(12):
        a = math.radians(200 + k * 14)
        m.append(ellipse(math.cos(a) * 190, -6 + math.sin(a) * 50 + 40, 20, 9, couleurs[k % 5]))
    m.append(place([ellipse(0, -14, 20, 24, "#a0693a"), chemin("M -22 -26 Q 0 -46 22 -26 Z", "#6d4424")], 170, 20))
    return place(m, x, y, s)


def salon(S, y=520):
    interieur(S, "#fff4e6", "#e8c39e", y, papier="#ffd8a8")
    S.add(fenetre(570, 80, 160, 140, "#a5d8ff", rideaux="#ff8787"))
    S.add(tapis(400, 680, 330, 90, "#d0ebff", "#74c0fc"))


def fauteuil(x, y, s=1.0):
    return place([rect(-110, -140, 220, 140, "#e599f7", rx=30), rect(-130, -90, 50, 90, "#cc5de8", rx=20), rect(80, -90, 50, 90, "#cc5de8", rx=20),
                  rect(-80, -70, 160, 40, "#f3d9fa", rx=14)], x, y, s)


def pissenlit(x, y, s=1.0, souffle=False):
    m = [trait(0, 0, 0, -140, "#40c057", 5)]
    rnd = random.Random(3)
    for k in range(18):
        a = math.radians(k * 20)
        if souffle and k % 3 == 0:
            continue
        m.append(trait(0, -170, math.cos(a) * 30, -170 + math.sin(a) * 30, "#dee2e6", 2))
        m.append(cercle(math.cos(a) * 32, -170 + math.sin(a) * 32, 4, "#fff"))
    if souffle:
        for k in range(6):
            dx, dy = 60 + k * 30 + rnd.uniform(-10, 10), -200 - k * 15 + rnd.uniform(-20, 20)
            m.append(g([trait(dx, dy, dx - 10, dy + 12, "#dee2e6", 2), cercle(dx, dy, 4, "#fff")]))
    m.append(cercle(0, -170, 8, "#adb5bd"))
    return place(m, x, y, s)


def boule(x, y, r, couleur="#495057"):
    """La « boule dans le ventre », gribouillée."""
    d = f"M {x + r} {y}"
    for k in range(1, 40):
        a = k * 0.5
        rr = r * (0.6 + 0.4 * ((k * 7) % 5) / 4)
        d += f" L {n(x + math.cos(a) * rr)} {n(y + math.sin(a) * rr)}"
    return chemin(d, stroke=couleur, sw=4, opacity=0.8)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S, 520)
    S.add(plateau(400, 690, 0.9), de(560, 640, 1.0, 1, rot=20))
    S.add(tibo(400, 800, 1.35, expr="fache", bras="croises"))
    S.add(lola(150, 790, 0.9, expr="surpris", regard=(1, 0)), zelie(670, 790, 0.7, expr="surpris", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(de(300, 150, 1.2, 6, rot=-15))
    S.add(tibo(170, 264, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(tibo(400, 650, 1.0, expr="content", bras="haut"))
    S.add(plateau(400, 680))
    S.add(pion(280, 650, "#fa5252"), pion(330, 640, "#ffd43b"), pion(470, 620, "#69db7c"))
    S.add(de(400, 600, 1.0, 4, rot=12), mouvement(450, 580, 0.8, rot=-30))
    S.add(lola(120, 800, 1.0, expr="rire", regard=(1, -1)), zelie(690, 800, 0.75, expr="rire", regard=(-1, -1)))
    return S


def p02():
    S = Scene()
    salon(S)
    S.add(plateau(400, 690))
    S.add(lola(160, 800, 1.0, expr="rire", bras="haut"), texte(160, 420, "Gagné !", 50, "#f59f00", contour="#fff"))
    S.add(tibo(470, 800, 1.2, expr="furieux", bras="poing"))
    S.add(de(700, 260, 1.0, 2, rot=40), mouvement(660, 270, 1.0, rot=-30), eclat(700, 260, 1.1, "#fa5252"))
    S.add(bulle(430, 140, 460, 120, "J'ai perdu !\nCe n'est pas juste !", 40, pointe=(470, 470)))
    return S


def p03():
    S = Scene()
    salon(S)
    S.add(plateau(400, 690))
    S.add(tibo(420, 800, 1.1, expr="fache", bras="croises"))
    S.add(lola(110, 790, 0.9, expr="triste", flip=True), zelie(220, 790, 0.6, expr="triste", flip=True))
    S.add(bulle(250, 230, 420, 120, "Ce n'est pas drôle\nde jouer avec toi.", 36, pointe=(150, 560)))
    S.add(de(700, 750, 0.8, 2, rot=30))
    return S


def p04():
    S = Scene()
    salon(S)
    S.add(tibo(260, 800, 1.2, expr="triste", bras="bas"))
    S.add(boule(260, 735, 30))
    S.add(mamie(560, 800, 1.15, expr="sourire", bras="ouverts", flip=True))
    S.add(bulle(520, 180, 440, 120, "Perdre, ça rend triste.\nTu as le droit.", 36, pointe=(560, 520)))
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=4)
    sol(S, 640, "#8ce99a")
    S.add(pissenlit(420, 690, 1.2, souffle=True))
    S.add(tibo(260, 790, 1.2, expr="souffle", bras="tient"))
    S.add(boule(260, 735, 12))
    S.add(mamie(640, 800, 1.0, expr="content", flip=True))
    S.add(texte(470, 200, "Fffffff…", 60, "#1971c2", contour="#fff"))
    return S


def p06():
    S = Scene()
    salon(S)
    S.add(plateau(400, 690))
    S.add(tibo(260, 800, 1.1, expr="timide", bras="donne", objet=de(84, -92, 0.7, 6)))
    S.add(lola(520, 790, 0.95, expr="sourire", flip=True), zelie(660, 790, 0.65, expr="content", flip=True))
    S.add(bulle(400, 190, 400, 120, "Pardon pour le dé.\nOn rejoue ?", 38, pointe=(280, 520)))
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(fauteuil(680, 620, 0.9))
    S.add(plateau(380, 700, 0.9), de(625, 640, 0.6, 3, rot=20))
    S.add(zelie(130, 790, 0.7, expr="rire", bras="haut"))
    S.add(tibo(340, 800, 1.1, expr="rire", bras="ouverts"))
    S.add(lola(560, 790, 0.9, expr="rire", bras="montre", regard=(1, 0)))
    S.add(texte(330, 200, "Bravo, Zélie !", 54, "#fa5252", contour="#fff"))
    return S


def p08():
    S = Scene()
    salon(S)
    S.add(tibo(400, 660, 1.0, expr="rire", bras="haut"))
    S.add(plateau(400, 690))
    S.add(pion(300, 650, "#fa5252"), pion(350, 640, "#ffd43b"), pion(470, 620, "#69db7c"), de(400, 640, 0.8, 5))
    S.add(lola(140, 800, 0.95, expr="rire", bras="haut"), zelie(680, 800, 0.75, expr="rire", bras="haut"))
    S.add(texte(400, 160, "Encore une partie !", 54, "#fa5252", contour="#fff"))
    S.add(coeur(250, 300, 1.0), coeur(560, 280, 0.8, "#ffa8a8"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tibo-seul.svg", vignette),
    ("01-le-jeu.svg", p01), ("02-pas-juste.svg", p02), ("03-pas-drole.svg", p03), ("04-mamie.svg", p04),
    ("05-le-pissenlit.svg", p05), ("06-pardon.svg", p06), ("07-bravo.svg", p07), ("08-ensemble.svg", p08),
]
