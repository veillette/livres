"""L'araignée tisse sa toile — l'épeire diadème.

L'araignée a huit pattes et deux parties au corps : ce n'est pas un insecte
(six pattes, trois parties). La soie sort de ses filières, au bout de son
ventre. Pour tisser, elle laisse le vent porter un premier fil jusqu'à une
branche (le pont), tend les rayons comme ceux d'une roue, puis une spirale
collante perlée de gouttelettes. Elle attend au centre et sent les
vibrations ; elle enroule sa proie dans la soie. Elle ne colle pas car elle
marche sur les rayons, qui ne collent pas. Les bébés araignées s'envolent
accrochés à un fil, portés par le vent.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, fleche_courbe, ondes
from objets import coccinelle

ID = "araignee-toile"
CORPS = "#b5651d"
CORPS2 = "#8d5524"
FIL = "#ffffff"


# --- Dessins ----------------------------------------------------------------

def epeire(x, y, s=1.0, rot=0, expr="sourire", regard=(0, 0), fil=False, soie=False):
    """Épeire diadème vue de dessus, tête en haut ; (x, y) = centre du corps.
    fil : un fil qui monte du bout de l'abdomen ; soie : fil qui sort des filières (vers le bas)."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if fil:
        m.append(trait(0, 60, 0, -900, FIL, 2))
    for sgn in (-1, 1):
        for (kx, ky), (px, py) in [((44, -70), (66, -120)), ((58, -40), (104, -62)), ((58, -12), (104, 16)), ((44, 10), (70, 64))]:
            m.append(chemin(f"M {sgn * 12} -30 L {sgn * kx} {ky} L {sgn * px} {py}", stroke=CORPS2, sw=7))
            m.append(cercle(sgn * kx, ky, 4, "#e9c46a"))
    if soie:
        m.append(chemin("M 0 70 Q 6 120 -4 180", stroke=FIL, sw=3))
    m.append(ellipse(0, 26, 42, 48, CORPS))
    m.append(chemin("M 0 0 L 0 56 M -18 22 L 18 22", stroke="#fff4e6", sw=6))
    for px, py in [(-16, 0), (16, 0), (-22, 42), (22, 42), (0, 64)]:
        m.append(cercle(px, py, 4, "#fff4e6"))
    m.append(ellipse(0, -30, 24, 22, CORPS2))
    for px, py in [(-6, -48), (6, -48), (-12, -44), (12, -44)]:
        m.append(cercle(px, py, 2.5, ENCRE))
    m.append(oeil(-9, -34, ys, regard, taille=0.7) + oeil(9, -34, ys, regard, taille=0.7))
    m.append(joue(-15, -24, 0.5) + joue(15, -24, 0.5))
    m.append(place(bouche(0, 0, bs, 0.5), 0, -22))
    return place(m, x, y, s, rot=rot)


def toile_(cx, cy, R=260, etape=3, rosee=False, nb=16, graine=1, cadre=None, couleur=FIL):
    """Toile en construction autour de (cx, cy) : 1 = cadre et rayons ;
    2 = + spirale collante ; 3 = idem, complète. rosee : gouttes brillantes."""
    r = random.Random(graine)
    m = []
    angles = [math.radians(k * 360 / nb + r.uniform(-4, 4)) for k in range(nb)]
    bords = [R * r.uniform(0.9, 1.05) for _ in angles]
    pts = [(cx + math.cos(a) * b, cy + math.sin(a) * b) for a, b in zip(angles, bords)]
    if etape >= 1:
        m.append(poly(pts, "none", stroke=couleur, stroke_width=3, opacity=0.9))
        for px, py in pts:
            m.append(trait(cx, cy, px, py, couleur, 2.5, opacity=0.9))
    if etape >= 2:
        tours = 14 if etape >= 3 else 8
        spirale = []
        for k in range(tours * nb):
            i = k % nb
            t = 0.18 + 0.78 * (1 - k / (tours * nb))
            a = angles[i]
            spirale.append((cx + math.cos(a) * bords[i] * t, cy + math.sin(a) * bords[i] * t))
        m.append(chemin("M " + " L ".join(f"{n(px)} {n(py)}" for px, py in spirale), stroke=couleur, sw=1.8, opacity=0.9))
        if rosee:
            for k in range(0, len(spirale), 3):
                px, py = spirale[k]
                m.append(cercle(px, py + 3, r.uniform(3, 6), "#e7f5ff", stroke="#a5d8ff", stroke_width=1))
                m.append(cercle(px - 1, py + 1, 1.3, "#ffffff"))
    return g(m)


def branche_(x0, y0, x1, y1, ep=16):
    return chemin(f"M {x0} {y0} Q {(x0 + x1) / 2} {(y0 + y1) / 2 + 20} {x1} {y1}", stroke="#7c4a1e", sw=ep)


def jardin_toile(S, nuit_=False, matin=False):
    if matin:
        S.add(rect(0, 0, 800, 800, S.degrade(["#ffd8a8", "#e7f5ff"])))
    else:
        ciel(S, "#a5d8ff", "#ebfbee")
    S.add(rect(0, 680, 800, 120, "#8ce99a"))
    herbes(S, 690, 790, 18, 2, "#40c057", 0.9)
    S.add(rect(40, 0, 40, 800, "#8d5524"), rect(720, 0, 40, 800, "#8d5524"))
    S.add(branche_(60, 120, 400, 90, 14), branche_(740, 140, 420, 100, 14))


def mouche_collee(x, y, s=1.0, enroulee=False):
    if enroulee:
        m = [ellipse(0, 0, 22, 32, "#f8f9fa"), chemin("M -20 -20 L 20 -10 M -22 0 L 22 8 M -20 18 L 20 24", stroke="#dee2e6", sw=2)]
        return place(m, x, y, s)
    return mouche(x, y, s, rot=20)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin_toile(S)
    S.add(toile_(400, 430, 280, 3, rosee=True))
    S.add(epeire(400, 430, 1.4, expr="rire"))
    S.add(coccinelle(110, 660, 1.4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(g(toile_(200, 135, 130, 3, couleur="#ced4da")))
    S.add(epeire(200, 135, 0.8, expr="content"))
    return S


def p01():
    S = Scene()
    fond(S, "#f4fce3")
    S.add(epeire(280, 400, 2.2, expr="content"))
    S.add(coccinelle(620, 400, 3.0))
    S.add(etiquette(280, 660, "8 pattes", 44, "#7048e8"), etiquette(620, 660, "6 pattes", 44, "#e03131"))
    S.add(etiquette(280, 80, "l'araignée", 40, "#7048e8"), etiquette(620, 80, "un insecte", 40, "#e03131"))
    S.cachette(430, 70, "air")
    return S


def p02():
    S = Scene()
    jardin_toile(S)
    S.add(trait(400, 100, 400, 360, FIL, 3))
    S.add(epeire(400, 380, 1.6, expr="concentre", soie=True))
    S.add(loupe(640, 580, 100, [rect(540, 480, 200, 200, CORPS), cercle(640, 560, 18, CORPS2),
                                 chemin("M 640 570 Q 650 620 630 700", stroke=FIL, sw=6),
                                 chemin("M 630 570 Q 620 620 640 700", stroke=FIL, sw=3)], fond=CORPS, rot=130))
    S.add(etiquette(640, 450, "la soie", 36, "#7048e8"))
    return S


def p03():
    S = Scene()
    jardin_toile(S)
    S.add(trait(80, 300, 720, 280, FIL, 3))
    S.add(epeire(130, 296, 0.8, rot=90, expr="joie"))
    from sciences import rafales
    S.add(rafales(300, 420, 1.2, "#74c0fc"))
    S.add(fleche(500, 330, 690, 300, "#7048e8", 5, 18))
    S.add(texte(400, 560, "Le vent porte mon fil !", 40, "#7048e8", contour="#fff"))
    return S


def p04():
    S = Scene()
    jardin_toile(S)
    S.add(trait(80, 180, 720, 180, FIL, 3), trait(80, 180, 80, 680, FIL, 3), trait(720, 180, 720, 680, FIL, 3))
    S.add(toile_(400, 430, 250, 1))
    S.add(epeire(560, 300, 1.0, rot=40, expr="concentre"))
    return S


def p05():
    S = Scene()
    jardin_toile(S)
    S.add(toile_(400, 430, 260, 2))
    S.add(epeire(400, 600, 1.0, rot=170, expr="concentre"))
    S.add(loupe(620, 200, 90, [rect(530, 110, 180, 180, "#a5d8ff"), trait(530, 200, 710, 210, FIL, 4)] +
                [cercle(540 + k * 22, 202 + k * 0.6, 6, "#e7f5ff", stroke="#74c0fc", stroke_width=1.5) for k in range(9)],
                fond="#a5d8ff", rot=130))
    S.add(etiquette(620, 330, "ça colle !", 34, "#7048e8"))
    return S


def p06():
    S = Scene()
    jardin_toile(S)
    S.add(toile_(400, 430, 280, 3))
    S.add(epeire(400, 430, 1.3, expr="concentre", regard=(0, 0)))
    S.add(ondes(400, 430, 80, 3, 40, 0, 360, "#7048e8", 3, cercles=True))
    S.add(texte(400, 760, "Ça bouge ?", 44, "#7048e8", contour="#fff"))
    return S


def p07():
    S = Scene()
    jardin_toile(S)
    S.add(toile_(400, 430, 280, 3))
    S.add(mouche_collee(560, 300, 1.4))
    S.add(mouche_collee(260, 560, 1.4, enroulee=True))
    S.add(epeire(470, 360, 1.1, rot=50, expr="miam"))
    return S


def p08():
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(toile_(400, 420, 330, 3))
    S.add(chemin("M 400 420 L 728 420", stroke="#7048e8", sw=8, opacity=0.5))
    S.add(epeire(580, 420, 1.1, rot=90, expr="fier"))
    S.add(etiquette(600, 520, "pas collant", 34, "#7048e8"), etiquette(250, 250, "collant", 34, "#c2255c"))
    S.add(fleche(270, 270, 300, 330, "#c2255c", 5, 16))
    S.cachette(570, 70, "air")
    return S


def p09():
    S = Scene()
    jardin_toile(S, matin=True)
    S.add(soleil(680, 640, 60))
    S.add(toile_(400, 420, 290, 3, rosee=True))
    S.add(epeire(400, 420, 1.1, expr="content"))
    return S


def p10():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 680, 800, 120, "#8ce99a"))
    S.add(chemin("M 120 800 Q 140 600 100 420", stroke="#2f9e44", sw=10))
    from sciences import rafales
    S.add(rafales(240, 600, 1.0, "#ffffff"))
    for x, y, L in [(260, 380, 140), (420, 260, 180), (580, 170, 150), (680, 360, 120), (360, 520, 120)]:
        S.add(chemin(f"M {x} {y} Q {x - L / 2} {y - L / 3} {x - L} {y - L / 2}", stroke=FIL, sw=2.5))
        S.add(epeire(x, y, 0.35, expr="rire"))
    S.add(epeire(108, 430, 0.35, expr="content", fil=False))
    S.add(texte(400, 660, "Au revoir ! Bon voyage !", 40, "#7048e8", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("araignee-seule.svg", vignette),
    ("01-huit-pattes.svg", p01), ("02-la-soie.svg", p02), ("03-le-premier-fil.svg", p03),
    ("04-les-rayons.svg", p04), ("05-la-spirale.svg", p05), ("06-elle-attend.svg", p06),
    ("07-une-mouche.svg", p07), ("08-pourquoi-elle-ne-colle-pas.svg", p08), ("09-la-rosee.svg", p09),
    ("10-les-bebes-s-envolent.svg", p10),
]
