"""Le ver de terre jardinier — le lombric.

Le ver de terre n'a ni yeux ni pattes : il sent la lumière par sa peau. Il
avance en s'allongeant et en se raccourcissant, accroché par de petites
soies. Il avale de la terre et tire des feuilles mortes dans sa galerie ; ses
crottes en tortillons enrichissent le sol, et ses galeries laissent entrer
l'air et l'eau jusqu'aux racines. Il respire par sa peau, qui doit rester
humide. On le voit sortir quand il pleut beaucoup. Coupé en deux, il ne
devient pas deux vers : on le manipule avec douceur.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant
from objets import pomme, flaque

ID = "ver-de-terre"
ROSE_VER = "#f783ac"


# --- Dessins ----------------------------------------------------------------

def ver_long(d, tete, angle, expr="sourire", couleur=ROSE_VER, ep=24, anneau=None):
    """Ver qui suit le chemin `d` ; `tete` = (x, y) du bout avant, `angle` =
    direction où il regarde (degrés). anneau : (x, y) du renflement clair."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    m = [chemin(d, stroke=couleur, sw=ep), chemin(d, stroke=fonce, sw=ep, stroke_dasharray="2 13", opacity=0.6)]
    if anneau:
        m.append(cercle(anneau[0], anneau[1], ep * 0.62, eclaircir(couleur, 0.3)))
    hx, hy = tete
    m.append(cercle(hx, hy, ep * 0.55, couleur))
    a = math.radians(angle)
    bx, by = hx + math.cos(a) * ep * 0.2, hy + math.sin(a) * ep * 0.2 + 3
    m.append(place(bouche(0, 0, bs, 0.4), bx, by))
    m.append(ellipse(hx - math.sin(a) * 5, hy + 6, 4, 2.5, "#c2255c", opacity=0.5))
    return g(m)


def feuille_morte(x, y, s=1.0, rot=0, couleur="#c08a52"):
    return place([chemin("M 0 0 Q 30 -28 70 0 Q 30 28 0 0 Z", couleur), trait(2, 0, 66, 0, _assombrir(couleur, 0.8), 2.5),
                  trait(-10, 0, 2, 0, _assombrir(couleur, 0.8), 3)], x, y, s, rot=rot)


def tortillon(x, y, s=1.0):
    m = [cercle(-10, 0, 9, "#6d4424"), cercle(4, -6, 9, "#7c4a1e"), cercle(-4, -14, 8, "#6d4424"), cercle(8, -20, 7, "#7c4a1e")]
    return place(m, x, y, s)


def galerie(d, ep=40):
    return chemin(d, stroke="#4a2e16", sw=ep, opacity=0.85)


def carotte_terre(x, y, s=1.0):
    m = [poly([(-18, 0), (18, 0), (0, 150)], "#fd7e14"),
         chemin("M 0 0 Q -20 -60 -40 -80 M 0 0 Q 0 -70 4 -100 M 0 0 Q 20 -60 40 -80", stroke="#40c057", sw=8)]
    for k in range(4):
        m.append(trait(-12 + k * 2, 30 + k * 26, -4 + k * 2, 32 + k * 26, "#e8590c", 3))
    return place(m, x, y, s)


def merle(x, y, s=1.0, flip=False):
    """Merle noir au bec jaune, de profil, tête à droite ; (x, y) = pattes."""
    m = [trait(-6, -30, -10, 0, "#e67700", 4), trait(8, -30, 10, 0, "#e67700", 4),
         poly([(-50, -60), (-110, -70), (-100, -50)], "#212529"),
         ellipse(0, -60, 54, 36, "#343a40"), ellipse(-10, -60, 34, 20, "#212529"),
         cercle(48, -92, 26, "#343a40"), poly([(70, -96), (100, -90), (70, -84)], "#fcc419"),
         cercle(54, -98, 7, "#fcc419"), cercle(55, -98, 4, ENCRE), cercle(56, -100, 1.5, "#fff")]
    return place(m, x, y, s, flip=flip)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    coupe_terre(S, 380, graine=2)
    S.add(fleur(150, 372, 1.0, "#ff8787", tige=90), fleur(640, 372, 0.9, "#ffd43b", tige=80))
    S.add(galerie("M 300 380 Q 280 500 380 560 Q 500 630 600 600", 44))
    S.add(ver_long("M 300 520 Q 330 560 400 570 Q 480 590 560 590", (566, 590), 0, "rire", ep=34, anneau=(470, 586)))
    S.add(racines(640, 372, 1.0))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 236, 170, 24, "#a0693a"))
    S.add(ver(200, 200, 1.0, 260, ROSE_VER, ondule=0.8, expr="content"))
    return S


def p01():
    S = Scene()
    coupe_terre(S, 340, graine=1)
    S.add(arbre(130, 340, 0.9), fleur(400, 332, 0.8, "#cc5de8", tige=70), fleur(700, 332, 0.8, "#ffd43b", tige=70))
    S.add(racines(130, 340, 1.2), racines(400, 330, 0.6, graine=2))
    S.add(galerie("M 560 340 Q 540 450 470 520 Q 400 600 420 700", 40))
    S.add(ver_long("M 520 430 Q 470 520 440 580 Q 420 630 430 680", (522, 428), -60, "content", anneau=(470, 520)))
    return S


def p02():
    S = Scene()
    coupe_terre(S, 300, graine=3)
    S.add(soleil(660, 100, 55))
    S.add(galerie("M 380 300 Q 380 450 400 620", 46))
    S.add(ver_long("M 390 520 Q 386 420 382 316", (382, 300), -90, "oups", ep=30))
    S.add(g([trait(560 + k * 20, 150 + k * 30, 430, 280, "#fcc419", 4, opacity=0.6) for k in range(3)]))
    S.add(texte(560, 520, "Oh, la lumière !", 40, "#ffffff", contour="#6d4424"))
    S.add(fleche(400, 360, 400, 460, "#ffffff", 6, 22))
    return S


def p03():
    S = Scene()
    fond(S, "#fff0f6")
    S.add(rect(0, 520, 800, 280, "#a0693a"))
    S.add(ver(300, 460, 1.3, 380, ROSE_VER, ondule=0.0, expr="concentre"))
    S.add(ver(330, 640, 1.3, 230, ROSE_VER, ondule=0.0, expr="concentre", ep=40))
    S.add(fleche(560, 640, 640, 640, "#c2255c", 6, 20))
    S.add(etiquette(250, 380, "je m'allonge…", 34, "#c2255c"), etiquette(250, 730, "… je me raccourcis !", 34, "#c2255c"))
    S.add(loupe(640, 250, 90, [rect(550, 160, 180, 180, ROSE_VER)] +
                [trait(560 + k * 30, 300, 556 + k * 30, 320, "#862e9c", 3) for k in range(6)] +
                [trait(560 + k * 30, 200, 560 + k * 30, 300, _assombrir(ROSE_VER, 0.85), 3) for k in range(6)],
                fond=ROSE_VER, rot=130))
    S.add(etiquette(640, 120, "des petits poils", 30, "#862e9c"))
    return S


def p04():
    S = Scene()
    coupe_terre(S, 340, graine=4)
    S.add(arbre(620, 340, 1.0, "#ffa94d", "#fd7e14"))
    for x, r in [(140, -10), (300, 20), (700, -30)]:
        S.add(feuille_morte(x, 330, 1.0, r))
    S.add(galerie("M 430 340 Q 420 460 450 600", 44))
    S.add(ver_long("M 450 560 Q 430 470 432 400", (432, 380), -90, "miam", ep=30))
    S.add(feuille_morte(470, 330, 1.2, 100))
    S.add(texte(230, 560, "Miam !", 54, "#ffffff", contour="#6d4424"))
    return S


def p05():
    S = Scene()
    coupe_terre(S, 420, graine=5)
    S.add(tortillon(300, 410, 2.0), tortillon(480, 414, 1.6), tortillon(620, 410, 1.8))
    S.add(galerie("M 300 420 Q 320 560 420 640 Q 520 700 600 640", 40))
    S.add(ver_long("M 330 560 Q 360 620 430 650 Q 500 680 560 660", (566, 656), -20, "fier", anneau=(470, 666)))
    S.add(fleur(300, 380, 1.2, "#ff8787", tige=120))
    S.add(texte(460, 220, "C'est de l'engrais !", 44, "#2f9e44", contour="#fff"))
    return S


def p06():
    S = Scene()
    coupe_terre(S, 300, graine=6)
    for x in (200, 400, 600):
        S.add(carotte_terre(x, 300, 1.4))
    S.add(galerie("M 100 300 Q 160 450 300 500 Q 420 540 480 680", 34))
    S.add(galerie("M 700 300 Q 640 420 560 480 Q 500 540 520 620", 30))
    for k in range(5):
        S.add(goutte(160 + k * 30, 380 + k * 30, 0.7, "#74c0fc"))
    S.add(ver_long("M 380 520 Q 430 560 460 620", (466, 634), 70, "content", ep=22))
    S.add(texte(400, 150, "De l'air et de l'eau !", 46, "#1971c2", contour="#fff"))
    return S


def p07():
    S = Scene()
    coupe_terre(S, 300, graine=7, terre="#8d5524", terre2="#5c3a1e")
    for k in range(12):
        S.add(goutte(80 + k * 60, 380 + (k % 3) * 120, 0.8, "#74c0fc"))
    S.add(galerie("M 200 560 Q 400 480 600 560", 50))
    S.add(ver_long("M 240 550 Q 400 480 560 550", (566, 552), 20, "content", ep=32, anneau=(470, 520)))
    S.add(texte(400, 700, "Ma peau doit rester humide.", 34, "#ffffff", contour="#5c3a1e"))
    return S


def p08():
    S = Scene()
    ciel(S, "#868e96", "#ced4da")
    pluie(S, 80, 3, (0, 0, 800, 600))
    S.add(rect(0, 560, 800, 240, "#8d5524"))
    S.add(rect(0, 550, 800, 20, "#40c057"))
    S.add(flaque(560, 640, 1.6))
    S.add(ver(330, 640, 1.2, 240, ROSE_VER, ondule=1.0, expr="rire"))
    S.add(ver(640, 720, 0.8, 200, ROSE_VER, ondule=0.7, expr="content", flip=True))
    S.add(nuage(200, 90, 1.0, "#adb5bd"), nuage(600, 70, 0.8, "#adb5bd"))
    return S


def p09():
    S = Scene()
    coupe_terre(S, 420, graine=8)
    S.add(merle(260, 420, 1.6))
    S.add(galerie("M 520 420 Q 520 560 540 700", 40))
    S.add(ver_long("M 530 700 Q 524 600 520 520", (520, 500), -90, "surpris", ep=28))
    S.add(fleche(600, 520, 600, 640, "#ffffff", 6, 22))
    S.add(texte(560, 250, "Vite, je descends !", 40, "#2f9e44", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(rect(0, 560, 800, 240, "#8d5524"))
    S.add(rect(0, 550, 800, 20, "#69db7c"))
    S.add(enfant(330, 780, 1.6, expr="content", bras="porte", regard=(0, 1), habit="#74c0fc", jambes="#364fc7",
                 coiffure="queue", objet=ver(0, -84, 0.5, 200, ROSE_VER, ondule=0.6, expr="content")))
    S.add(arrosoir(600, 640, 1.0))
    S.add(texte(400, 160, "Tout doux, petit ver !", 44, "#c2255c", contour="#fff"))
    return S


def arrosoir(x, y, s=1.0):
    m = [rect(-50, -70, 100, 80, "#4dabf7", rx=12), chemin("M 40 -40 L 110 -100", stroke="#4dabf7", sw=14),
         ellipse(112, -104, 16, 10, "#339af0", rot=-40), chemin("M -40 -70 Q 0 -120 40 -70", stroke="#339af0", sw=8)]
    return place(m, x, y, s)


IMAGES = [
    ("couverture.svg", couverture), ("ver-seul.svg", vignette),
    ("01-sous-le-jardin.svg", p01), ("02-pas-d-yeux.svg", p02), ("03-il-avance.svg", p03),
    ("04-les-feuilles.svg", p04), ("05-les-tortillons.svg", p05), ("06-les-galeries.svg", p06),
    ("07-la-peau.svg", p07), ("08-la-pluie.svg", p08), ("09-le-merle.svg", p09),
    ("10-tout-doux.svg", p10),
]
