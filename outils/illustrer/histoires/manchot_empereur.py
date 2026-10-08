"""Papa manchot et son œuf — le manchot empereur.

En Antarctique, à l'approche de l'hiver, les manchots empereurs marchent
jusqu'à leur colonie sur la banquise. La femelle pond un seul œuf et le
confie au mâle, qui le garde sur ses pieds, sous un repli de peau, pendant
tout l'hiver, sans manger. Les mâles se serrent les uns contre les autres
dans le blizzard et changent de place à tour de rôle. Le poussin gris naît ;
la mère revient et le reconnaît à son chant. Les parents se relaient. L'été,
les jeunes perdent leur duvet et plongent : le manchot ne vole pas, il nage.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche

ID = "manchot-empereur"
DOS = "#343a40"
JAUNE = "#ffc078"


# --- Personnages ------------------------------------------------------------

def manchot(x, y, s=1.0, flip=False, expr="sourire", oeuf_=False, poussin_=False, penche=0, bec_ouvert=False,
            aile="bas", maigre=False, poisson_=False):
    """Manchot empereur de profil, tête à droite ; (x, y) = sous les pieds.
    oeuf_ : un œuf posé sur ses pieds, sous le repli du ventre ;
    poussin_ : un poussin sur ses pieds ; penche : rotation (marche)."""
    ys, bs, ss = EXPRESSIONS[expr]
    k = 0.88 if maigre else 1.0
    m = []
    m.append(ellipse(14, -4, 26, 7, "#495057"))
    m.append(chemin(f"M -30 -20 Q -60 -10 -56 6 Q -40 0 -24 -6 Z", DOS))
    m.append(ellipse(0, -112, 50 * k, 106, DOS))
    m.append(ellipse(16, -104, 36 * k, 94, "#f8f9fa"))
    m.append(chemin(f"M {n(-8 * k)} -186 Q 30 -196 {n(44 * k)} -150 Q 30 -150 {n(-4 * k)} -160 Z", "#fff3bf"))
    if oeuf_:
        m.append(ellipse(22, -24, 20, 17, "#fff4e6", stroke="#adb5bd", stroke_width=3))
        m.append(chemin("M -10 -40 Q 20 -58 48 -36 Q 30 -30 20 -32 Q 2 -32 -10 -30 Z", "#e9ecef"))
    if poussin_:
        m.append(poussin_gris(24, -10, 0.42, expr="content"))
        m.append(chemin("M -10 -46 Q 20 -64 52 -44 Q 34 -40 18 -42 Q 2 -40 -10 -36 Z", "#e9ecef"))
    if aile == "bas":
        m.append(ellipse(-14, -120, 13, 62, _assombrir(DOS, 0.85), rot=12))
    elif aile == "haut":
        m.append(ellipse(-40, -150, 13, 62, _assombrir(DOS, 0.85), rot=-50))
    m.append(cercle(10, -214, 32, DOS))
    m.append(ellipse(16, -186, 11, 20, JAUNE, rot=-20))
    m.append(ellipse(22, -176, 8, 12, "#fff3bf", rot=-20, opacity=0.8))
    if bec_ouvert or bs in ("ouverte", "o", "crie"):
        m.append(poly([(34, -224), (92, -222), (38, -212)], DOS))
        m.append(poly([(36, -208), (88, -200), (36, -200)], "#ff922b"))
    else:
        m.append(poly([(34, -222), (92, -208), (36, -204)], DOS))
        m.append(chemin("M 44 -206 L 84 -208", stroke="#ff922b", sw=5))
    m.append(cercle(24, -222, 8.5, "#fff"))
    if ys in ("heureux", "fermes"):
        m.append(oeil(24, -222, ys, (0, 0), taille=0.65))
    else:
        m.append(cercle(26, -222, 5, ENCRE) + cercle(27.5, -224, 1.8, "#fff"))
    m.append(joue(30, -200, 0.7))
    if poisson_:
        m.append(poisson_simple(96, -214, 0.7, rot=20))
    return place(m + [occuper(-56, -246, 92, 6)], x, y, s, flip=flip, rot=penche)


def manchot_face(x, y, s=1.0, expr="sourire", ailes="bas"):
    """Manchot empereur vu de face ; (x, y) = sous les pieds."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [ellipse(-18, -4, 18, 7, "#495057"), ellipse(18, -4, 18, 7, "#495057"),
         ellipse(0, -110, 56, 106, DOS), ellipse(0, -100, 40, 92, "#f8f9fa"),
         chemin("M -30 -180 Q 0 -192 30 -180 Q 20 -150 0 -146 Q -20 -150 -30 -180 Z", "#fff3bf")]
    if ailes == "bas":
        m += [ellipse(-52, -110, 13, 58, _assombrir(DOS, 0.85), rot=12), ellipse(52, -110, 13, 58, _assombrir(DOS, 0.85), rot=-12)]
    else:
        m += [ellipse(-70, -150, 13, 58, _assombrir(DOS, 0.85), rot=50), ellipse(70, -150, 13, 58, _assombrir(DOS, 0.85), rot=-50)]
    m.append(cercle(0, -212, 34, DOS))
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 30, -186, 9, 18, JAUNE, rot=sgn * 20))
        m.append(cercle(sgn * 13, -220, 8, "#fff"))
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * 13, -220, ys, (0, 0), taille=0.6))
        else:
            m.append(cercle(sgn * 13, -220, 4.5, ENCRE) + cercle(sgn * 13 + 1.5, -222, 1.6, "#fff"))
        m.append(joue(sgn * 22, -202, 0.6))
    m.append(poly([(-7, -206), (7, -206), (0, -184)], DOS))
    m.append(trait(0, -200, 0, -188, "#ff922b", 3))
    return place(m + [occuper(-77, -246, 77, 3)], x, y, s)


def poussin_gris(x, y, s=1.0, flip=False, expr="sourire", bec_ouvert=False):
    """Poussin de manchot empereur : duvet gris, tête noire, masque blanc ;
    (x, y) = sous les pieds, tête à droite."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [ellipse(10, -4, 18, 6, "#495057"),
         ellipse(0, -60, 48, 58, "#ced4da"),
         ellipse(-30, -60, 12, 30, "#adb5bd", rot=14)]
    for k in range(8):
        a = math.radians(100 + k * 20)
        m.append(cercle(math.cos(a) * 46, -60 + math.sin(a) * 54, 9, "#ced4da"))
    m.append(cercle(8, -130, 34, DOS))
    m.append(chemin("M -6 -140 Q 20 -164 40 -132 Q 40 -112 18 -108 Q -4 -112 -6 -140 Z", "#ffffff"))
    m.append(oeil(16, -132, ys, (0.5, 0), taille=0.75))
    m.append(joue(26, -118, 0.6))
    if bec_ouvert or bs in ("ouverte", "o", "crie"):
        m.append(poly([(38, -132), (64, -138), (40, -124)], DOS))
        m.append(poly([(38, -122), (60, -118), (38, -116)], DOS))
    else:
        m.append(poly([(38, -130), (64, -124), (38, -118)], DOS))
    return place(m + [occuper(-55, -164, 64, 2)], x, y, s, flip=flip)


def blizzard(S, nb=70, graine=3):
    r = random.Random(graine)
    for _ in range(nb):
        x, y = r.uniform(-50, 800), r.uniform(0, 800)
        S.add(trait(x, y, x + 60, y + 14, "#ffffff", r.uniform(2, 5), opacity=r.uniform(0.4, 0.9)))


def aurore(S):
    for k, (c, y) in enumerate([("#63e6be", 120), ("#96f2d7", 170), ("#b197fc", 90)]):
        S.add(chemin(f"M -20 {y} Q 200 {y - 70} 400 {y + 10} T 820 {y - 20}", stroke=c, sw=34 - k * 8, opacity=0.45))


def mer_glace(S, y=520):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, y, 800, 800 - y, S.degrade(["#339af0", "#1864ab"])))
    S.add(poly([(0, y - 40), (260, y - 40), (300, y), (0, y)], "#f8f9fa"))
    S.add(rect(0, y, 300, 30, "#d0ebff"))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    banquise(S, 560)
    S.add(manchot(330, 740, 1.9, expr="content", oeuf_=True))
    S.add(manchot(560, 750, 1.55, flip=True, expr="rire"))
    S.add(coeur(450, 300, 1.2, "#ff8787"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 258, 170, 14, "#d0ebff"))
    S.add(manchot(210, 262, 0.95, expr="content", poussin_=True))
    return S


def p01():
    S = Scene()
    banquise(S, 500)
    for k in range(6):
        x = 120 + k * 120
        y = 700 - (k % 2) * 30
        S.add(manchot(x, y, 0.95 - k * 0.06, penche=(-6 if k % 2 else 6), expr="sourire"))
    S.add(g([trait(60 + k * 30, 720, 20 + k * 30, 730, "#d0ebff", 4) for k in range(3)]))
    S.cachette(730, 320, "air")
    return S


def p02():
    S = Scene()
    banquise(S, 470)
    r = random.Random(4)
    for row, (y, sc) in enumerate([(500, 0.45), (560, 0.55)]):
        for k in range(10):
            x = 30 + k * 82 + row * 40
            if row == 1 and 260 < x < 560:
                continue
            S.add(manchot_face(x + r.uniform(-10, 10), y, sc) if (k + row) % 3 else manchot(x, y, sc, flip=k % 2 == 0))
    S.add(manchot(300, 760, 1.3, expr="chante", bec_ouvert=True))
    S.add(manchot(520, 760, 1.3, flip=True, expr="content"))
    S.add(notes(420, 380, 1.1, "#1971c2"))
    S.cachette(730, 320, "air")
    return S


def p03():
    S = Scene()
    banquise(S, 470)
    S.add(manchot(280, 760, 1.6, expr="content", oeuf_=True))
    S.add(manchot(560, 760, 1.6, flip=True, expr="sourire", aile="haut"))
    S.add(fleche(500, 760, 400, 760, "#1971c2", 8, 26))
    S.add(coeur(420, 330, 1.0, "#ff8787"))
    return S


def p04():
    S = Scene()
    banquise(S, 520)
    for k in range(4):
        S.add(manchot(500 + k * 80, 610 - k * 12, 0.55 - k * 0.04, penche=-6 if k % 2 else 6))
    S.add(manchot(230, 760, 1.5, expr="triste", oeuf_=True))
    S.add(texte(560, 370, "À bientôt !", 50, "#1971c2", contour="#fff"))
    return S


def p05():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(manchot(330, 760, 2.4, expr="dort", oeuf_=True))
    S.add(loupe(640, 520, 120, [rect(500, 380, 300, 300, "#d0ebff"), ellipse(640, 630, 100, 26, "#495057"),
                                 ellipse(640, 570, 60, 50, "#fff4e6", stroke="#adb5bd", stroke_width=4),
                                 chemin("M 520 560 Q 640 470 760 560 L 760 380 L 520 380 Z", "#f1f3f5"),
                                 chemin("M 520 560 Q 640 470 760 560", stroke="#ced4da", sw=6)], rot=50))
    S.add(etiquette(640, 340, "au chaud !", 40, "#1971c2"))
    S.cachette(380, 70, "air")
    return S


def p06():
    S = Scene()
    banquise(S, 520, nuit_=True)
    aurore(S)
    for row, (y, sc, nb, dx) in enumerate([(560, 0.6, 9, 0), (640, 0.75, 7, 50), (740, 0.95, 6, 10)]):
        for k in range(nb):
            S.add(manchot_face(80 + dx + k * (640 / (nb - 1)), y, sc, expr="dort" if row < 2 else "sourire"))
    blizzard(S, 60)
    S.add(texte(400, 300, "Hou ! Hou !", 54, "#ffffff", contour="#364fc7"))
    S.cachette(730, 250, "air")
    return S


def p07():
    S = Scene()
    banquise(S, 470)
    S.add(manchot(360, 760, 2.0, expr="content", poussin_=True))
    S.add(place([ellipse(0, 0, 30, 24, "#f8f9fa"), poly([(-30, -4), (-18, -14), (-6, -2), (6, -16), (18, -2), (30, -6), (30, 0), (-30, 0)], "#f8f9fa")], 620, 740))
    S.add(texte(570, 330, "Piou !", 64, "#1971c2", contour="#fff"))
    return S


def p08():
    S = Scene()
    banquise(S, 470)
    S.add(manchot(220, 760, 1.45, expr="rire", bec_ouvert=True, poisson_=True))
    S.add(manchot(560, 760, 1.45, flip=True, expr="content"))
    S.add(poussin_gris(390, 760, 0.95, expr="rire", bec_ouvert=True))
    S.add(notes(380, 330, 0.9, "#1971c2"))
    return S


def p09():
    S = Scene()
    banquise(S, 470)
    S.add(manchot(660, 600, 0.75, flip=False, penche=8, maigre=True))
    S.add(texte(640, 360, "Miam, la mer !", 34, "#1971c2", contour="#fff"))
    r = random.Random(9)
    for k in range(7):
        S.add(poussin_gris(90 + k * 80 + r.uniform(-10, 10), 720 + (k % 2) * 40, 0.75, flip=k % 2 == 1,
                           expr=r.choice(["content", "rire", "sourire"])))
    S.add(manchot(120, 640, 0.9, expr="sourire"))
    return S


def p10():
    S = Scene()
    mer_glace(S, 380)
    S.add(manchot(120, 340, 0.8, expr="rire", aile="haut"))
    S.add(manchot(560, 560, 1.3, penche=70, expr="rire"))
    S.add(manchot(300, 680, 1.0, penche=100, expr="content", flip=False))
    for x, y in [(680, 470), (720, 700), (180, 520)]:
        S.add(poisson_simple(x, y, 1.0, flip=True))
    S.add(g([cercle(470 + k * 16, 520 - k * 34, 6 + k * 2, "none", stroke="#fff", stroke_width=3) for k in range(3)]))
    S.add(texte(560, 140, "Plouf !", 70, "#1971c2", contour="#fff"))
    S.cachette(730, 260, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("manchot-seul.svg", vignette),
    ("01-la-marche.svg", p01), ("02-la-colonie.svg", p02), ("03-l-oeuf.svg", p03),
    ("04-maman-part.svg", p04), ("05-sur-les-pieds.svg", p05), ("06-la-tempete.svg", p06),
    ("07-le-poussin.svg", p07), ("08-maman-revient.svg", p08), ("09-chacun-son-tour.svg", p09),
    ("10-plouf.svg", p10),
]
