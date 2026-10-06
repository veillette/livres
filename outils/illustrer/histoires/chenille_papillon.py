"""La chenille qui devient papillon — la vie du machaon.

Le machaon pond ses œufs un par un sur le fenouil (ou la carotte sauvage),
que mangera la chenille. La chenille mange d'abord la coquille de son œuf,
mue plusieurs fois, sort ses deux cornes orange (l'osmeterium) quand on
l'embête, puis s'accroche la tête en haut avec une ceinture de soie et devient
chrysalide. Le papillon sort les ailes fripées, les déplie et les sèche, puis
boit le nectar avec sa trompe.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche
from objets import papillon

ID = "chenille-papillon"
JAUNE = "#ffe066"
NOIR = "#2b2b3a"
VERT_CH = "#8ce99a"


# --- Personnages ------------------------------------------------------------

def chenille(x, y, s=1.0, flip=False, rot=0, expr="sourire", regard=(1, 0), bosse=0.0, cornes=False, nb=10,
             couleur=VERT_CH, bebe=False):
    """Chenille de machaon de profil, tête à droite ; (x, y) = au sol, au
    milieu. `bosse` arrondit le dos (elle avance) ; `bebe` : toute petite et
    sombre."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    r = 22
    pts = []
    for k in range(nb):
        t = k / (nb - 1)
        px = -nb * 17 / 2 + k * 17
        py = -r - math.sin(t * math.pi) * bosse * 50
        pts.append((px, py))
    c = couleur if not bebe else "#495057"
    for k, (px, py) in enumerate(pts[:-1]):
        if k >= 1:
            m.append(trait(px, py + 12, px, py + r + 2, "#2f9e44" if not bebe else ENCRE, 7))
    for k, (px, py) in enumerate(pts[:-1]):
        m.append(cercle(px, py, r, c))
    for k, (px, py) in enumerate(pts[:-1]):
        if bebe:
            if k == 4 or k == 5:
                m.append(cercle(px, py, r - 2, "#f8f9fa"))
            continue
        m.append(chemin(f"M {n(px + 8)} {n(py - r + 2)} Q {n(px + 13)} {n(py)} {n(px + 8)} {n(py + r - 3)}", stroke=NOIR, sw=6))
        for dy in (-12, 0, 12):
            m.append(cercle(px + 9, py + dy, 3.4, "#ff922b"))
    hx, hy = pts[-1]
    hx += 6
    if cornes:
        m.append(chemin(f"M {n(hx - 10)} {n(hy - r)} Q {n(hx - 26)} {n(hy - r - 36)} {n(hx - 50)} {n(hy - r - 40)}", stroke="#ff922b", sw=9))
        m.append(chemin(f"M {n(hx)} {n(hy - r)} Q {n(hx - 4)} {n(hy - r - 44)} {n(hx - 24)} {n(hy - r - 56)}", stroke="#ff922b", sw=9))
    m.append(cercle(hx, hy, r + 2, c if not bebe else "#343a40"))
    m.append(oeil(hx + 6, hy - 5, ys, regard, taille=0.75))
    m.append(joue(hx + 12, hy + 7, 0.6))
    m.append(place(bouche(0, 0, bs, 0.5), hx + 14, hy + 4))
    return place(m, x, y, s, flip=flip, rot=rot)


def _aile(forme, bord, points, extra=()):
    """Aile jaune bordée de noir : `bord` = chemin du bord extérieur."""
    cid = uid("w")
    m = [el("clipPath", chemin(forme, "#000"), id=cid), chemin(forme, JAUNE)]
    m.append(g([chemin(bord, stroke=NOIR, sw=34)] + list(extra), clip_path=f"url(#{cid})"))
    for px, py, c in points:
        m.append(cercle(px, py, 4.5, c))
    return m


AVANT = "M 2 -6 C 20 -60 70 -96 124 -100 C 132 -70 124 -40 104 -10 C 70 0 30 4 8 2 Z"
AVANT_BORD = "M 124 -100 C 132 -70 124 -40 104 -10"
ARRIERE = "M 6 6 C 50 4 90 14 104 30 C 100 54 90 66 76 74 C 50 76 24 60 8 30 Z"
ARRIERE_BORD = "M 104 30 C 100 54 90 66 76 74 C 50 76 30 64 20 52"


def machaon(x, y, s=1.0, rot=0, expr="sourire", regard=(0, 0), ailes=1.0, fripe=False):
    """Machaon vu de dessus, tête en haut ; (x, y) = centre du corps.
    `ailes` : 1 = grandes ouvertes ; `fripe` : ailes molles et repliées
    juste à la sortie de la chrysalide."""
    m = []
    def ailes_():
        veines = [chemin(f"M 8 0 L {px} {py}", stroke=NOIR, sw=3, opacity=0.7) for px, py in [(70, -84), (96, -60), (104, -30)]]
        avant = _aile(AVANT, AVANT_BORD, [(122, -84, JAUNE), (122, -60, JAUNE), (114, -34, JAUNE)],
                      veines + [chemin("M 10 -10 C 30 -50 60 -80 110 -96", stroke=NOIR, sw=10)])
        arriere = _aile(ARRIERE, ARRIERE_BORD, [(94, 44, "#4dabf7"), (82, 60, "#4dabf7"), (64, 66, "#4dabf7")],
                        [chemin("M 8 6 L 90 40", stroke=NOIR, sw=3, opacity=0.6)])
        arriere.append(cercle(24, 46, 9, "#fa5252"))
        arriere.insert(0, chemin("M 74 70 L 80 112", stroke=NOIR, sw=8))
        return avant, arriere

    k = ailes
    for sgn in (-1, 1):
        avant, arriere = ailes_()
        m.append(place(arriere, 0, 0, k * (0.5 if fripe else 1), flip=sgn < 0, sy=1.3 if fripe else None))
        m.append(place(avant, 0, 0, k * (0.5 if fripe else 1), flip=sgn < 0, sy=0.7 if fripe else None))
    if fripe:
        m = [place(g(m), 0, 0, 1, rot=0)]
        m.append(chemin("M -40 -20 q 10 10 20 0 q 10 -10 20 0 M 20 -20 q 10 10 20 0 q 10 -10 20 0", stroke="#e8c170", sw=3))
    m.append(ellipse(0, 22, 9, 46, NOIR))
    m.append(chemin("M -3 -30 Q -16 -70 -28 -78 M 3 -30 Q 16 -70 28 -78", stroke=NOIR, sw=3))
    m.append(cercle(-28, -78, 4, NOIR) + cercle(28, -78, 4, NOIR))
    m.append(cercle(0, -28, 14, NOIR))
    m.append(cercle(-6, -30, 4.5, "#fff") + cercle(6, -30, 4.5, "#fff"))
    m.append(cercle(-6 + regard[0] * 1.5, -30 + regard[1] * 1.5, 2.6, NOIR) + cercle(6 + regard[0] * 1.5, -30 + regard[1] * 1.5, 2.6, NOIR))
    return place(m, x, y, s, rot=rot)


def machaon_profil(x, y, s=1.0, flip=False, trompe=False):
    """Machaon posé, ailes refermées et dressées, de profil, tête à droite ;
    (x, y) = sous les pattes."""
    m = []
    for k in range(3):
        m.append(chemin(f"M {-6 + k * 12} -22 L {-12 + k * 14} -8 L {-10 + k * 14} 0", stroke=NOIR, sw=3))
    arr = "M -8 -34 C -40 -40 -80 -70 -96 -110 C -70 -124 -40 -104 -10 -64 Z"
    m += _aile(arr, "M -96 -110 C -80 -70 -40 -40 -8 -34", [(-74, -82, "#4dabf7"), (-56, -64, "#4dabf7"), (-38, -52, "#4dabf7")])
    m.append(chemin("M -78 -74 L -104 -62", stroke=NOIR, sw=7))
    m.append(cercle(-22, -46, 8, "#fa5252"))
    av = "M -10 -34 C -24 -110 -4 -176 34 -204 C 60 -160 54 -80 16 -34 Z"
    m += _aile(av, "M 34 -204 C 60 -160 54 -80 16 -34",
               [(46, -170, JAUNE), (50, -130, JAUNE), (44, -90, JAUNE)],
               [chemin(f"M 0 -36 L {px} {py}", stroke=NOIR, sw=3, opacity=0.6) for px, py in [(10, -170), (30, -140), (36, -100)]]
               + [chemin("M -12 -60 C -16 -120 0 -170 30 -200", stroke=NOIR, sw=8)])
    m.append(ellipse(4, -26, 36, 9, NOIR, rot=-6))
    m.append(cercle(42, -32, 11, NOIR))
    m.append(cercle(46, -35, 4.5, "#fff") + cercle(47, -35, 2.6, NOIR))
    m.append(chemin("M 42 -42 Q 58 -84 76 -96", stroke=NOIR, sw=2.5) + cercle(76, -96, 3.5, NOIR))
    if trompe:
        m.append(chemin("M 50 -26 Q 66 -14 70 6", stroke="#495057", sw=3))
    else:
        m.append(chemin("M 50 -26 q 10 8 4 14 q -6 4 -6 -2", stroke="#495057", sw=2.5))
    return place(m, x, y, s, flip=flip)


def chrysalide(x, y, s=1.0, couleur="#94d82d", ouverte=False, rot=0):
    """Chrysalide de machaon accrochée tête en haut ; (x, y) = point d'attache
    du bas sur la tige (la tige est verticale, à gauche de la chrysalide)."""
    fonce = _assombrir(couleur, 0.8)
    m = []
    forme = "M 0 0 Q 18 -20 26 -70 Q 30 -110 18 -150 L 24 -170 L 8 -158 L -2 -172 L -2 -150 Q -18 -110 -12 -60 Q -10 -20 0 0 Z"
    if ouverte:
        m.append(chemin(forme, eclaircir(couleur, 0.5), opacity=0.7))
        m.append(chemin("M -2 -150 L 10 -120 L 24 -170", stroke="#ffffff", sw=4))
    else:
        m.append(chemin(forme, couleur))
        m.append(chemin("M 4 -10 Q 14 -60 10 -140", stroke=fonce, sw=3))
        m.append(chemin("M -6 -50 Q 8 -40 22 -54 M -8 -80 Q 8 -70 26 -84", stroke=fonce, sw=2.5))
    m.append(chemin("M -18 -100 Q 6 -84 30 -100", stroke="#f1f3f5", sw=2.5))
    return place(m, x, y, s, rot=rot)


def oeuf_papillon(x, y, s=1.0):
    return place([cercle(0, 0, 9, "#fff3bf"), cercle(-3, -3, 3, "#ffffff")], x, y, s)


def fenouil(x, y, s=1.0, h=520, fleurs=True, graine=1):
    """Tige de fenouil avec ses feuilles fines comme des cheveux et ses
    ombelles jaunes ; (x, y) = pied."""
    r = random.Random(graine)
    m = [chemin(f"M 0 0 Q 10 {-h / 2} 0 {-h}", stroke="#5c940d", sw=10)]
    for k in range(5):
        yy = -h * (0.18 + k * 0.15)
        sgn = -1 if k % 2 else 1
        for j in range(5):
            a = math.radians(-90 + sgn * (20 + j * 18))
            L = r.uniform(90, 140)
            m.append(chemin(f"M 4 {n(yy)} Q {n(math.cos(a) * L * 0.6)} {n(yy + math.sin(a) * L * 0.4)} {n(math.cos(a) * L)} {n(yy + math.sin(a) * L)}",
                            stroke="#74b816", sw=3))
    if fleurs:
        cy = -h
        for j in range(9):
            a = math.radians(-160 + j * 17.5)
            fx, fy = math.cos(a) * 70, cy + math.sin(a) * 40 - 30
            m.append(trait(0, cy, fx, fy, "#74b816", 3))
            m.append(cercle(fx, fy, 9, "#fcc419"))
    return place(m, x, y, s)


def tige_feuille(x, y, s=1.0, rot=0):
    """Une grande feuille de fenouil (en gros plan) : rameaux très fins."""
    m = [chemin("M 0 0 Q 160 -40 360 -10", stroke="#5c940d", sw=10)]
    for k in range(9):
        px = 30 + k * 36
        for sgn in (-1, 1):
            m.append(chemin(f"M {px} {-8 - k * 0.4} q {sgn * 6 + 20} {sgn * 40} {40} {sgn * 70}", stroke="#74b816", sw=5))
    return place(m, x, y, s, rot=rot)


def pre(S, y=620):
    ciel(S, "#a5d8ff", "#f3f0ff")
    S.add(chemin(f"M 0 {y - 40} Q 200 {y - 90} 400 {y - 50} T 800 {y - 60} L 800 {y + 10} L 0 {y + 10} Z", "#b2f2bb"))
    S.add(rect(0, y, 800, 800 - y, "#8ce99a"))
    herbes(S, y + 20, 790, 20, 3, "#40c057", 0.8)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    pre(S, 640)
    S.add(fenouil(140, 700, 0.9, 470))
    S.add(fenouil(690, 700, 0.8, 440, graine=3))
    S.add(machaon(420, 420, 1.45, rot=8))
    S.add(chenille(330, 740, 1.2, bosse=0.4, expr="rire"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(machaon(250, 120, 0.68, rot=12))
    S.add(chenille(150, 262, 0.75, bosse=0.3, expr="content"))
    return S


def p01():
    S = Scene()
    pre(S, 660)
    S.add(fenouil(400, 760, 1.15, 560, fleurs=True))
    S.add(oeuf_papillon(452, 512, 1.4))
    S.add(machaon_profil(560, 470, 1.25, flip=True))
    S.add(fenouil(110, 760, 0.7, 400, graine=4), fenouil(720, 760, 0.6, 380, graine=5))
    return S


def p02():
    S = Scene()
    fond(S, "#ebfbee")
    S.add(cercle(400, 400, 330, "#d3f9d8"))
    S.add(tige_feuille(40, 560, 2.0, rot=-4))
    S.add(place([cercle(0, 0, 48, "#fff3bf", opacity=0.6), chemin("M -40 -10 L -26 -40 L -8 -18 L 6 -46 L 22 -20 L 40 -30 L 46 0 Q 30 46 0 48 Q -40 44 -46 0 Z", "#fff3bf")], 520, 420))
    S.add(chenille(360, 470, 1.25, bebe=True, nb=7, expr="miam", regard=(1, 0)))
    S.add(texte(400, 180, "Miam !", 64, "#2f9e44", contour="#fff"))
    return S


def p03():
    S = Scene()
    pre(S, 660)
    S.add(fenouil(260, 780, 1.2, 600, fleurs=False, graine=2))
    S.add(chenille(470, 520, 1.6, bosse=0.2, expr="miam", rot=-10))
    S.add(texte(560, 240, "Crounch !", 64, "#2f9e44", contour="#fff", rot=-6))
    S.add(texte(620, 330, "crounch…", 40, "#2f9e44", contour="#fff", rot=-6))
    return S


def p04():
    S = Scene()
    fond(S, "#fff9db")
    S.add(tige_feuille(20, 640, 2.1, rot=-2))
    S.add(place([cercle(-80 + k * 18, -20, 20, "#e9ecef", opacity=0.7) for k in range(8)], 210, 600, 1.0))
    S.add(texte(180, 520, "vieille peau", 30, "#868e96", contour="#fff"))
    S.add(chenille(500, 600, 1.6, bosse=0.15, expr="fier"))
    S.add(eclat(620, 440, 0.8, "#fcc419"))
    return S


def p05():
    S = Scene()
    pre(S, 660)
    S.add(fenouil(250, 780, 1.1, 560, fleurs=False, graine=7))
    S.add(chenille(380, 560, 1.7, bosse=0.0, cornes=True, expr="fache"))
    S.add(oiseau(670, 700, 1.1, couleur="#868e96", ventre="#f1f3f5", expr="degoute", flip=True, ailes="haut"))
    S.add(texte(660, 470, "Pouah !", 50, "#495057", contour="#fff"))
    S.add(g([chemin(f"M {500 + k * 26} {330 - k * 10} q 10 -20 0 -40", stroke="#94d82d", sw=5, opacity=0.8) for k in range(3)]))
    return S


def _tige_verticale(S, x=330):
    S.add(rect(x - 12, 0, 24, 800, "#5c940d"))
    S.add(rect(x - 12, 0, 6, 800, "#74b816"))


def p06():
    S = Scene()
    fond(S, "#e7f5ff")
    _tige_verticale(S)
    S.add(chenille(400, 600, 1.6, rot=-90, bosse=0.0, expr="concentre"))
    S.add(chemin("M 318 440 Q 380 410 440 440", stroke="#ffffff", sw=4))
    S.add(chemin("M 318 450 Q 380 420 444 452", stroke="#ced4da", sw=2))
    S.add(g([chemin(f"M 318 {720 + k * 8} l 18 6", stroke="#ffffff", sw=3) for k in range(4)]))
    S.add(loupe(620, 220, 110, [chemin("M 520 200 Q 620 160 720 200", stroke="#ffffff", sw=10),
                                  chemin("M 520 220 Q 620 180 720 220", stroke="#dee2e6", sw=6)], fond="#94d82d"))
    S.add(etiquette(620, 380, "fil de soie", 34, "#1971c2"))
    return S


def p07():
    S = Scene()
    fond(S, "#e7f5ff")
    _tige_verticale(S)
    S.add(chrysalide(360, 620, 2.2))
    S.add(texte(620, 300, "chut…", 60, "#5c940d", contour="#fff"))
    S.add(zzz(560, 420, 1.0, "#5c940d"))
    return S


def p08():
    S = Scene()
    fond(S, "#fff9db")
    _tige_verticale(S)
    S.add(chrysalide(360, 380, 1.8, ouverte=True))
    S.add(machaon(392, 470, 1.2, fripe=True))
    S.add(texte(620, 240, "Oh !", 70, "#f08c00", contour="#fff"))
    return S


def p09():
    S = Scene()
    pre(S, 660)
    S.add(soleil(660, 120, 60, visage=True))
    S.add(fenouil(220, 780, 1.1, 600, fleurs=True, graine=8))
    S.add(machaon(400, 400, 1.5, rot=-6))
    S.add(mouvement(230, 420, 0.8, "#f08c00"))
    return S


def p10():
    S = Scene()
    pre(S, 600)
    for x, c in [(110, "#ff8787"), (690, "#cc5de8"), (580, "#ffd43b")]:
        S.add(fleur(x, 760, 1.4, c, tige=200))
    S.add(fleur(360, 780, 2.6, "#ff8787", "#ffd43b", tige=150))
    S.add(machaon_profil(380, 400, 1.8, trompe=True))
    S.add(papillon(640, 260, 1.4, "#ffd43b", "#ff922b", rot=15))
    return S


def p11():
    S = Scene()
    fond(S, "#f8f0fc")
    S.add(cycle(400, 400, 250, "#ae3ec9", nb=4, ecart=30))
    S.add(disque(400, 150, 105, "#ebfbee"), tige_feuille(300, 170, 0.55), oeuf_papillon(400, 140, 2.2))
    S.add(disque(650, 400, 105, "#ebfbee"), chenille(650, 440, 0.75, bosse=0.3))
    S.add(disque(400, 650, 105, "#ebfbee"), rect(342, 545, 12, 210, "#5c940d"), chrysalide(370, 720, 0.85))
    S.add(disque(150, 400, 105, "#ebfbee"), machaon(150, 410, 0.62))
    S.add(etiquette(400, 290, "l'œuf", 30, "#862e9c"), etiquette(650, 540, "la chenille", 30, "#862e9c"),
          etiquette(400, 790, "la chrysalide", 30, "#862e9c"), etiquette(150, 540, "le papillon", 30, "#862e9c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("papillon-seul.svg", vignette),
    ("01-l-oeuf.svg", p01), ("02-premier-repas.svg", p02), ("03-elle-mange.svg", p03),
    ("04-la-mue.svg", p04), ("05-les-cornes.svg", p05), ("06-le-fil.svg", p06),
    ("07-la-chrysalide.svg", p07), ("08-la-sortie.svg", p08), ("09-au-soleil.svg", p09),
    ("10-le-nectar.svg", p10), ("11-le-cycle.svg", p11),
]
