"""Du têtard à la grenouille — la métamorphose.

Ordre exact des étapes : œufs en amas (point noir qui s'allonge en virgule),
têtard à branchies, têtard qui broute les algues, pattes arrière d'abord,
puis pattes avant pendant que la queue est résorbée, petite grenouille qui
respire de l'air (poumons et peau). La grenouille verte chante avec deux sacs
vocaux, de chaque côté de la bouche.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche

ID = "grenouille-tetard"
VERT = "#69db7c"
VERT_F = "#40c057"
VENTRE = "#e9fac8"
TETARD = "#7a6a48"


# --- Personnages ------------------------------------------------------------

def grenouille(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), sacs=False, langue=None, queue=0,
               couleur=VERT):
    """Grenouille assise de profil, tête à droite ; (x, y) = sous les pattes.
    sacs : sacs vocaux gonflés ; langue : (x, y) local du bout de la langue ;
    queue : longueur d'un reste de queue (petite grenouille)."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = []
    if queue:
        m.append(chemin(f"M -50 -26 Q {-50 - queue * 0.6} -30 {-50 - queue} -14", stroke=TETARD, sw=12))
    m.append(ellipse(-4, -6, 46, 9, fonce))
    m.append(ellipse(-30, -34, 40, 24, fonce, rot=-25))
    m.append(ellipse(-4, -54, 60, 40, couleur, rot=-22))
    m.append(ellipse(10, -42, 34, 20, VENTRE, rot=-22))
    for px, py, r in [(-30, -70, 8), (-10, -84, 6), (-44, -50, 6)]:
        m.append(cercle(px, py, r, fonce, opacity=0.6))
    m.append(ellipse(-34, -30, 36, 20, couleur, rot=-25))
    m.append(ellipse(42, -84, 38, 28, couleur))
    m.append(cercle(40, -108, 18, couleur))
    m.append(cercle(40, -108, 13, "#fff"))
    if ys in ("heureux", "fermes"):
        m.append(oeil(40, -108, ys, regard, taille=1.0))
    else:
        k = 1.2 if ys == "grand" else 1.0
        m.append(cercle(40 + regard[0] * 3, -108 + regard[1] * 3, 7 * k, ENCRE))
        m.append(cercle(42 + regard[0] * 3, -111 + regard[1] * 3, 2.4, "#fff"))
    if sacs:
        m.append(cercle(46, -62, 18, "#f8f9fa", stroke="#dee2e6", stroke_width=2))
    m.append(joue(58, -78))
    if langue:
        lx, ly = langue
        m.append(chemin(f"M 76 -80 Q {n((76 + lx) / 2)} {n(min(-80, ly) - 30)} {n(lx)} {n(ly)}", stroke="#ff8fab", sw=8))
        m.append(cercle(lx, ly, 9, "#ff8fab"))
    if bs in ("ouverte", "o", "crie", "baille") or langue:
        m.append(chemin("M 80 -80 Q 60 -64 34 -72 Q 58 -76 80 -80 Z", "#c92a2a"))
    else:
        m.append(chemin("M 80 -80 Q 62 -68 34 -74", stroke=ENCRE, sw=3.5))
    m.append(chemin("M 26 -58 Q 34 -30 42 -8", stroke=couleur, sw=13))
    m.append(ellipse(48, -6, 13, 6, fonce))
    return place(m, x, y, s, flip=flip)


def grenouille_nage(x, y, s=1.0, flip=False, rot=0, couleur=VERT):
    """Grenouille qui nage, vue de dessus, tête vers la droite ; (x, y) = centre."""
    fonce = _assombrir(couleur, 0.8)
    m = []
    for sgn in (-1, 1):
        m.append(chemin(f"M -30 {sgn * 14} Q -70 {sgn * 40} -110 {sgn * 30}", stroke=fonce, sw=14))
        m.append(poly([(-104, sgn * 24), (-140, sgn * 14), (-136, sgn * 44)], fonce))
        m.append(chemin(f"M 20 {sgn * 20} Q 34 {sgn * 44} 52 {sgn * 46}", stroke=fonce, sw=9))
    m.append(ellipse(0, 0, 54, 30, couleur))
    m.append(ellipse(46, 0, 26, 24, couleur))
    for sgn in (-1, 1):
        m.append(cercle(52, sgn * 16, 9, "#fff"))
        m.append(cercle(54, sgn * 16, 5, ENCRE))
    for px, py in [(-20, -8), (0, 10), (14, -12)]:
        m.append(cercle(px, py, 6, fonce, opacity=0.6))
    return place(m, x, y, s, flip=flip, rot=rot)


def tetard(x, y, s=1.0, stade=0, flip=False, rot=0, branchies=False, expr="sourire", regard=(1, 0)):
    """Têtard de profil, tête à droite ; (x, y) = centre du corps.
    stade 0 : sans pattes ; 1 : pattes arrière ; 2 : quatre pattes, queue plus courte."""
    ys, bs, ss = EXPRESSIONS[expr]
    corps = TETARD if stade < 2 else "#6f8f3e"
    fonce = _assombrir(corps, 0.8)
    q = 1.0 if stade < 2 else 0.55
    m = [chemin(f"M -20 -6 Q {n(-60 * q)} -26 {n(-100 * q)} -4 Q {n(-60 * q)} 18 -20 8 Z", eclaircir(corps, 0.45), opacity=0.8),
         chemin(f"M -20 0 Q {n(-56 * q)} -10 {n(-96 * q)} -2", stroke=corps, sw=7)]
    if branchies:
        for k in range(3):
            m.append(chemin(f"M 6 {-14 + k * 6} q -6 -10 -14 -8", stroke="#e8a798", sw=3))
    m.append(ellipse(0, 0, 32, 24, corps))
    m.append(ellipse(4, 8, 20, 11, eclaircir(corps, 0.35)))
    patte = "#a9b86a" if stade >= 2 else "#b59f6e"
    if stade >= 1:
        m.append(chemin("M -14 14 Q -24 34 -46 34", stroke=patte, sw=10))
        m.append(ellipse(-50, 34, 11, 6, patte))
    if stade >= 2:
        m.append(chemin("M 12 16 Q 18 30 30 34", stroke=patte, sw=8))
        m.append(ellipse(34, 35, 8, 5, patte))
    m.append(oeil(16, -8, ys, regard, taille=0.7))
    m.append(joue(24, 4, 0.6))
    m.append(place(bouche(0, 0, bs, 0.4), 28, 6))
    return place(m, x, y, s, flip=flip, rot=rot)


def ponte(x, y, s=1.0, graine=1, nb=34, stade=0, vides=0):
    """Amas d'œufs de grenouille : billes de gelée, point noir au centre
    (stade 0), virgule (stade 1). `vides` : nombre d'œufs déjà éclos."""
    r = random.Random(graine)
    m = []
    pts = []
    for k in range(nb):
        a = r.uniform(0, 2 * math.pi)
        d = math.sqrt(r.uniform(0, 1)) * 70
        pts.append((math.cos(a) * d * 1.3, math.sin(a) * d))
    for k, (px, py) in enumerate(pts):
        m.append(cercle(px, py, 15, "#f1f3f5", opacity=0.55, stroke="#ffffff", stroke_width=2))
    for k, (px, py) in enumerate(pts):
        if k < vides:
            continue
        if stade == 0:
            m.append(cercle(px, py, 4.5, ENCRE))
        else:
            m.append(chemin(f"M {n(px - 6)} {n(py - 2)} Q {n(px)} {n(py + 6)} {n(px + 6)} {n(py - 4)}", stroke=ENCRE, sw=4))
            m.append(cercle(px + 6, py - 4, 3.5, ENCRE))
    return place(m, x, y, s)


def mouche_vol(x, y, s=1.0, rot=0):
    return mouche(x, y, s, rot) + mouvement(x - 40 * s, y, 0.5 * s, "#495057")


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    mare(S, 470, nenuphars=False)
    S.add(nenuphar_haut(420, 700, 1.6, None))
    S.add(grenouille(400, 690, 1.9, expr="rire"))
    S.add(tetard(130, 740, 0.9, regard=(1, 0.2)), tetard(700, 700, 0.8, stade=1, flip=True, regard=(1, 0)))
    S.add(mouche_vol(640, 500, 1.1, rot=10))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 236, 150, 28, "#74c0fc"))
    S.add(nenuphar_haut(210, 240, 0.9))
    S.add(grenouille(200, 236, 0.95, expr="content"))
    S.add(tetard(345, 230, 0.5), tetard(60, 236, 0.45, stade=1))
    return S


def p01():
    S = Scene()
    mare(S, 470)
    S.add(fleur(90, 520, 0.8, "#ffd43b"), fleur(710, 500, 0.7, "#ff8787"))
    S.add(grenouille(300, 520, 1.3, expr="content", regard=(1, 0.4)))
    S.add(mouvement(200, 470, 0.8, "#2f9e44"))
    S.add(soleil(680, 110, 50))
    return S


def p02():
    S = Scene()
    sous_l_eau(S)
    S.add(_herbe_eau_centre())
    S.add(ponte(380, 470, 1.6, graine=2))
    S.add(grenouille_nage(600, 170, 1.2, rot=-20))
    S.add(bulles_(640, 120))
    return S


def _herbe_eau_centre():
    return g([chemin("M 260 700 Q 230 560 290 430 Q 330 330 300 200", stroke="#2f9e44", sw=10),
              chemin("M 470 700 Q 500 580 450 460 Q 410 360 470 260", stroke="#37b24d", sw=10)])


def bulles_(x, y, s=1.0):
    return place([cercle(0, 0, 8, "none", stroke="#fff", stroke_width=3), cercle(14, -30, 11, "none", stroke="#fff", stroke_width=3),
                  cercle(-6, -64, 7, "none", stroke="#fff", stroke_width=3)], x, y, s)


def _oeuf_zoom(x, y, contenu):
    return g([cercle(x, y, 110, "#e7f5ff", opacity=0.8, stroke="#ffffff", stroke_width=6),
              cercle(x - 40, y - 44, 18, "#ffffff", opacity=0.7), contenu])


def p03():
    S = Scene()
    sous_l_eau(S, plantes=False)
    S.add(_oeuf_zoom(160, 380, cercle(160, 380, 34, ENCRE)))
    S.add(_oeuf_zoom(400, 380, chemin("M 360 370 Q 390 420 430 380", stroke=ENCRE, sw=22) + cercle(432, 376, 22, ENCRE)))
    S.add(_oeuf_zoom(640, 380, tetard(640, 380, 1.0, rot=-25, expr="dort")))
    S.add(fleche(262, 380, 296, 380, "#ffffff", 8, 22), fleche(502, 380, 536, 380, "#ffffff", 8, 22))
    return S


def p04():
    S = Scene()
    sous_l_eau(S)
    S.add(_herbe_eau_centre())
    S.add(ponte(360, 470, 1.5, graine=2, stade=1, vides=20))
    for x, y, r in [(560, 330, -10), (620, 470, 15), (180, 300, 170), (520, 600, 5), (150, 590, 190), (640, 210, -25)]:
        flip = 90 < r < 270
        S.add(tetard(x, y, 0.85, branchies=True, rot=r if not flip else r - 180, flip=flip, expr="joie" if x > 600 else "sourire"))
    return S


def p05():
    S = Scene()
    sous_l_eau(S)
    S.add(ellipse(400, 690, 170, 60, "#868e96"))
    S.add(g([chemin(f"M {300 + k * 22} 650 q 6 -24 -4 -40", stroke="#94d82d", sw=7) for k in range(10)]))
    S.add(tetard(420, 560, 2.2, expr="miam", regard=(1, 0.5), rot=12))
    S.add(tetard(150, 300, 1.0, rot=-10), tetard(640, 260, 0.9, flip=True), tetard(600, 420, 0.7, rot=20))
    S.add(mouvement(220, 560, 1.0, "#ffffff"))
    return S


def p06():
    S = Scene()
    sous_l_eau(S)
    S.add(tetard(400, 420, 2.6, stade=1, expr="surpris", regard=(0, 1)))
    S.add(eclat(250, 520, 0.7, "#ffffff"))
    S.add(tetard(140, 220, 0.8, stade=1, rot=-15), tetard(650, 640, 0.8, stade=1, flip=True))
    return S


def p07():
    S = Scene()
    sous_l_eau(S)
    S.add(rect(0, 0, 800, 40, "#a5d8ff"))
    S.add(tetard(420, 230, 2.8, stade=2, rot=-30, expr="content", regard=(1, -1)))
    S.add(bulles_(600, 90, 0.9))
    S.add(fleche(420, 640, 420, 420, "#ffffff", 9, 26))
    S.add(tetard(160, 560, 0.9, stade=2, rot=-20), tetard(660, 520, 0.8, stade=2, flip=True, rot=-10))
    return S


def p08():
    S = Scene()
    mare(S, 430, nenuphars=False)
    S.add(nenuphar_haut(400, 690, 1.7, "#ffc9d6"))
    S.add(grenouille(400, 680, 1.25, expr="rire", queue=34))
    S.add(nenuphar_haut(640, 770, 0.9))
    S.add(grenouille(650, 760, 0.7, expr="content", queue=18, flip=True))
    S.add(soleil(680, 110, 50))
    return S


def p09():
    S = Scene()
    mare(S, 430, nenuphars=False)
    S.add(nenuphar_haut(330, 700, 1.7))
    S.add(grenouille(320, 690, 1.6, expr="concentre", regard=(1, -1), langue=(250, -230)))
    S.add(mouche(720, 300, 1.4, rot=60))
    S.add(texte(560, 220, "Flip !", 72, "#e64980", contour="#fff", rot=-8))
    return S


def p10():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#5f3dc4", "#f783ac", "#ffd8a8"])))
    S.add(cercle(640, 360, 60, "#ffd43b", opacity=0.9))
    S.add(chemin("M 0 420 Q 200 380 400 410 T 800 400 L 800 460 L 0 460 Z", "#2b8a3e"))
    S.add(rect(0, 450, 800, 350, "#1c7ed6"))
    S.add(ellipse(640, 470, 80, 6, "#ffd43b", opacity=0.5))
    for x, y, h in [(30, 470, 230), (60, 470, 270), (760, 470, 220)]:
        S.add(roseau(x, y, 1, h))
    S.add(nenuphar_haut(250, 700, 1.4), nenuphar_haut(580, 640, 1.2))
    S.add(grenouille(240, 690, 1.3, expr="chante", sacs=True))
    S.add(grenouille(580, 630, 1.0, expr="chante", sacs=True, flip=True))
    S.add(texte(300, 330, "Coâ !", 64, "#fff", contour="#5f3dc4", rot=-8))
    S.add(texte(520, 240, "Coâ !", 50, "#fff", contour="#5f3dc4", rot=8))
    return S


def p11():
    S = Scene()
    fond(S, "#ebfbee")
    S.add(cycle(400, 400, 250, "#2f9e44", nb=4, ecart=30))
    S.add(disque(400, 150, 105, "#d3f9d8"), ponte(400, 150, 0.95, graine=4, nb=22))
    S.add(disque(650, 400, 105, "#d3f9d8"), tetard(655, 400, 1.6))
    S.add(disque(400, 650, 105, "#d3f9d8"), tetard(408, 640, 1.5, stade=2))
    S.add(disque(150, 400, 105, "#d3f9d8"), grenouille(146, 468, 0.95, expr="content"))
    S.add(etiquette(400, 290, "les œufs", 30, "#2b8a3e"), etiquette(650, 540, "le têtard", 30, "#2b8a3e"),
          etiquette(400, 790, "les pattes", 30, "#2b8a3e"), etiquette(150, 540, "la grenouille", 30, "#2b8a3e"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("grenouille-seule.svg", vignette),
    ("01-la-mare.svg", p01), ("02-les-oeufs.svg", p02), ("03-dans-l-oeuf.svg", p03),
    ("04-eclosion.svg", p04), ("05-le-tetard-mange.svg", p05), ("06-pattes-arriere.svg", p06),
    ("07-pattes-avant.svg", p07), ("08-petite-grenouille.svg", p08), ("09-la-langue.svg", p09),
    ("10-le-chant.svg", p10), ("11-le-cycle.svg", p11),
]
