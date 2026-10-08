"""Le boulanger de la nuit — comment naît le pain."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from contes import pain
from fables import sac

ID = "boulanger-nuit"
BASTIEN = dict(peau="rosee", cheveux="chatain", coiffure="courts", habit="#ffffff", jambes="#868e96",
               chaussures="#495057", acc=("toque",), tenue=tablier("#f8f9fa", "#dee2e6"))
NOUR = dict(peau="doree", cheveux="noir", coiffure="queue", habit="#ff922b", jambes="#5c7cfa",
            chaussures="#e8590c")
MAMAN = dict(peau="doree", cheveux="noir", coiffure="longs", habit="#20c997", jambes="#495057", robe=True)
DORE = "#e8a15c"


def bastien(x, y, s=1.6, **k):
    return pro(x, y, s, **{**BASTIEN, **k})


def fournil(S, nuit_=True):
    interieur(S, "#fff4e6", "#c8a27a", 600, plinthe="#a0693a")
    for x in range(0, 800, 100):
        for y in range(40, 580, 50):
            S.add(rect(x + (25 if (y // 50) % 2 else 0), y, 92, 42, "#ffe8cc", rx=4))
    S.add(fenetre(600, 90, 150, 130, "#1c2a52" if nuit_ else "#a5d8ff", nuit_=nuit_))


def baguette(x, y, s=1.0, rot=0, c=DORE):
    m = [ellipse(0, 0, 110, 18, _assombrir(c, 0.9)), ellipse(0, -3, 104, 14, c)]
    for k in range(-2, 3):
        m.append(chemin(f"M {k * 40 - 12} -8 q 12 -6 24 4", stroke="#fff4e6", sw=4))
    return place(m, x, y, s, rot=rot)


def boule(x, y, s=1.0, c=DORE):
    return place([ellipse(0, -30, 56, 36, _assombrir(c, 0.9)), ellipse(0, -34, 50, 30, c),
                  chemin("M -24 -48 L 24 -20 M 24 -48 L -24 -20", stroke="#fff4e6", sw=5)], x, y, s)


def croissant(x, y, s=1.0, c="#f59f00", rot=0):
    m = [chemin("M -60 10 Q -70 -40 0 -44 Q 70 -40 60 10 Q 40 -14 0 -16 Q -40 -14 -60 10 Z", c)]
    for k in (-30, 0, 30):
        m.append(chemin(f"M {k - 8} -40 Q {k} -24 {k + 8} -16", stroke=_assombrir(c, 0.8), sw=4))
    return place(m, x, y, s, rot=rot)


def pate(x, y, s=1.0, gonflee=0.0, c="#fff4e6"):
    k = 1 + gonflee * 0.6
    return place([ellipse(0, -30 * k, 90 * (1 + gonflee * 0.2), 34 * k, c, stroke="#e9d8c4", stroke_width=3)], x, y, s)


def plan_travail(x, y, w=520, c="#c68642"):
    return g([rect(x - w / 2, y - 20, w, 30, c, rx=6), rect(x - w / 2 + 20, y + 10, 24, 160, _assombrir(c, 0.8)),
              rect(x + w / 2 - 44, y + 10, 24, 160, _assombrir(c, 0.8))])


def four_pro(x, y, s=1.0, plein=True):
    """Four de boulanger à deux étages vitrés ; (x, y) = milieu de la base."""
    m = [rect(-170, -380, 340, 380, "#adb5bd", rx=14), rect(-160, -370, 320, 30, "#868e96", rx=8)]
    for k, yy in enumerate((-320, -180)):
        m.append(rect(-140, yy, 280, 110, "#343a40", rx=10))
        m.append(rect(-130, yy + 10, 260, 90, "#ffa94d", rx=8, opacity=0.85))
        if plein:
            for j in range(3):
                m.append(baguette(-80 + j * 80, yy + 76, 0.32, rot=0, c="#d9822b"))
        m.append(rect(-120, yy - 10, 240, 10, "#ced4da", rx=4))
    m.append(rect(100, -40, 50, 20, "#495057", rx=4))
    return place(m, x, y, s)


def odeur(x, y, s=1.0, c="#ffc078"):
    return place([chemin(f"M 0 {k * 40} q 40 -30 80 0 t 80 0 t 80 0", stroke=c, sw=9, opacity=0.8) for k in range(3)], x, y, s)


def panier_pains(x, y, s=1.0):
    m = [baguette(-30, -80, 0.6, rot=-70), baguette(10, -80, 0.6, rot=-80), baguette(40, -80, 0.6, rot=-100),
         rect(-80, -60, 160, 60, "#c68642", rx=10)]
    for k in range(5):
        m.append(trait(-76 + k * 38, -60, -70 + k * 38, 0, "#a0693a", 3))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    fournil(S, nuit_=False)
    S.add(four_pro(620, 640, 1.0))
    S.add(bastien(320, 780, 1.85, expr="rire", bras="porte", objet=panier_pains(0, -40, 0.9)))
    S.add(odeur(80, 300, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(baguette(200, 120, 1.4, rot=-12))
    S.add(croissant(110, 230, 1.1), boule(290, 250, 1.2))
    return S


def p01():
    S = Scene()
    nuit(S)
    etoiles(S, 40, 5, (0, 0, 800, 360))
    S.add(lune(660, 110, 46))
    S.add(maison(130, 600, 1.2, mur="#5c6b9e", toit="#3b4a7a", fenetre="#2b3a66"))
    S.add(maison(670, 600, 1.2, mur="#5c6b9e", toit="#3b4a7a", fenetre="#2b3a66"))
    # la boulangerie, seule allumée
    S.add(rect(260, 300, 280, 300, "#ffe8cc"), poly([(240, 305), (400, 210), (560, 305)], "#e8590c"))
    S.add(rect(240, 300, 320, 50, "#d9480f"), texte(400, 336, "BOULANGERIE", 30, "#fff"))
    S.add(rect(0, 600, 800, 200, "#3b4a7a"))
    # La vitrine montre l'intérieur du fournil, avec ses étagères et ses
    # croisillons ; la lumière déborde sur le mur et le trottoir.
    S.add(rect(272, 372, 136, 156, "#a0522d", rx=5),
          rect(280, 380, 120, 140, radial([(0, "#fff4c2"), (1, "#f9c76c")]), rx=2))
    for yy in (390, 415, 440, 465, 490):
        S.add(trait(263, yy, 273, yy - 3, "#f7d9a8", 3, opacity=0.5),
              trait(408, yy - 3, 420, yy, "#f7d9a8", 3, opacity=0.5))
    # Dans la vitrine éclairée, des étagères déjà garnies de pains.
    for yy in (430, 490):
        S.add(rect(286, yy, 108, 6, "#c68642"))
        for k in range(3):
            S.add(ellipse(306 + k * 34, yy - 9, 14, 9, "#e8a15c"))
    S.add(rect(334, 380, 7, 140, "#fff4e6"), rect(280, 446, 120, 7, "#fff4e6"),
          poly([(288, 382), (300, 382), (291, 519), (282, 519)], "#ffffff", opacity=0.28),
          rect(276, 376, 128, 148, "none", stroke="#fff4e6", stroke_width=6),
          rect(264, 524, 152, 12, "#f1d3ac", rx=3))
    S.add(rect(430, 400, 80, 200, "#a0522d"))
    S.add(poly([(280, 600), (400, 600), (450, 720), (230, 720)], "#ffe066", opacity=0.3))
    # la seule lumière de la rue : la vitrine éclaire le trottoir
    S.lumiere(340, 450, 210, "#ffd43b", 0.7)
    S.lumiere(340, 650, 200, "#ffd43b", 0.45, ry=60)
    S.add(zzz(160, 340, 0.9, "#a5d8ff"), zzz(700, 340, 0.9, "#a5d8ff"))
    S.cachette(690, 700)
    return S


def p02():
    S = Scene()
    fournil(S)
    S.add(bastien(400, 560, 1.4, expr="content", bras="ouverts"))
    S.add(plan_travail(400, 600, 760))
    S.add(sac(110, 580, 0.9, ecrit=""))
    S.add(g([rect(250, 470, 80, 110, "#a5d8ff", rx=12, opacity=0.8), rect(270, 450, 40, 24, "#74c0fc", rx=6)]))
    S.add(texte(290, 640, "eau", 30, "#1c7ed6"))
    S.add(g([rect(470, 500, 70, 80, "#f8f9fa", rx=10, stroke="#ced4da", stroke_width=3), texte(505, 550, "sel", 26, "#495057")]))
    S.add(g([rect(600, 530, 70, 50, "#e9c58b", rx=6), texte(635, 640, "levure", 30, "#a0693a")]))
    S.add(texte(110, 640, "farine", 30, "#a0693a"), texte(505, 640, "sel", 30, "#495057"))
    return S


def p03():
    S = Scene()
    fournil(S)
    S.add(bastien(400, 640, 1.6, expr="concentre", bras="porte", objet=""))
    S.add(plan_travail(400, 660, 600))
    S.add(pate(400, 640, 1.5))
    S.add(texte(160, 300, "Hop !", 60, "#d9480f", contour="#fff", rot=-10),
          texte(640, 330, "Hop !", 60, "#d9480f", contour="#fff", rot=10))
    S.add(cercle(220, 600, 6, "#fff"), cercle(580, 590, 5, "#fff"), cercle(250, 560, 4, "#fff"))
    return S


def p04():
    S = Scene()
    fournil(S)
    S.add(plan_travail(400, 640, 700))
    # avant / après
    S.add(pate(230, 620, 1.1), pate(570, 620, 1.1, gonflee=1.0))
    for (bx, by, r) in [(540, 560, 8), (590, 548, 6), (610, 580, 9), (560, 590, 5), (520, 585, 6), (630, 560, 5)]:
        S.add(cercle(bx, by, r, "none", stroke="#e9c58b", stroke_width=3))
    from sciences import fleche
    S.add(fleche(320, 560, 460, 560, "#d9480f"))
    S.add(horloge(400, 200, 60, 4, 0))
    S.add(texte(230, 460, "avant", 36, "#a0693a"), texte(570, 440, "après", 36, "#a0693a"))
    return S


def p05():
    S = Scene()
    fournil(S)
    S.add(bastien(400, 560, 1.4, expr="content", bras="large"))
    S.add(plan_travail(400, 600, 760))
    for k in range(3):
        S.add(baguette(170, 520 + k * 24, 0.9, c="#fff4e6"))
    for k, x in enumerate((420, 520)):
        S.add(boule(x, 585, 0.9, c="#fff4e6"))
    for k in range(4):
        S.add(boule(620 + (k % 2) * 70, 540 + (k // 2) * 44, 0.5, c="#fff4e6"))
    S.add(texte(170, 680, "baguettes", 32, "#a0693a"), texte(470, 680, "boules", 32, "#a0693a"),
          texte(650, 680, "petits", 32, "#a0693a"), texte(650, 716, "pains", 32, "#a0693a"))
    return S


def p06():
    S = Scene()
    fournil(S)
    S.add(four_pro(500, 680, 1.25))
    S.add(odeur(150, 140, 0.9))
    S.add(bastien(150, 780, 1.6, expr="content", bras="pense", regard=(1, -0.4)))
    S.add(texte(150, 330, "Mmm…", 60, "#d9480f", contour="#fff"))
    return S


def p07():
    S = Scene()
    fournil(S)
    S.add(bastien(400, 560, 1.4, expr="concentre", bras="porte",
                  objet=g([rect(-70, -66, 140, 22, "#e9c58b", rx=10), rect(-90, -62, 24, 14, "#c68642", rx=6),
                           rect(66, -62, 24, 14, "#c68642", rx=6)])))
    S.add(plan_travail(400, 600, 760))
    for k in range(4):
        S.add(poly([(80 + k * 70, 580), (130 + k * 70, 580), (105 + k * 70, 500)], "#fff4e6", stroke="#e9d8c4", stroke_width=3))
    S.add(rect(500, 570, 240, 14, "#868e96", rx=4))
    for k in range(3):
        S.add(croissant(540 + k * 80, 560, 0.55))
    S.add(rect(250, 450, 60, 40, "#ffe066", rx=6), texte(280, 478, "beurre", 16, "#a0693a"))
    return S


def boutique(S, soleil_=True):
    interieur(S, "#fff0f6", "#e8c39e", 600, plinthe="#d9a066")
    S.add(fenetre(40, 80, 200, 170, "#ffd8a8" if soleil_ else "#a5d8ff",
                  contenu=soleil(140, 250, 40) + rect(40, 230, 200, 40, "#ffc078")))
    for y in (140, 260, 380):
        S.add(rect(320, y, 440, 16, "#c68642", rx=4))
    for k in range(5):
        S.add(baguette(380 + k * 90, 110, 0.4, rot=-60))
    for k in range(4):
        S.add(boule(380 + k * 110, 256, 0.75))
    for k in range(5):
        S.add(croissant(360 + k * 90, 372, 0.6))


def comptoir(x, y, w=500):
    return g([rect(x - w / 2, y - 170, w, 170, "#c68642", rx=8), rect(x - w / 2 - 10, y - 186, w + 20, 22, "#a0693a", rx=6),
              rect(x - w / 2 + 30, y - 140, w - 60, 100, "#e8c39e", rx=8)])


def p08():
    S = Scene()
    boutique(S)
    S.add(bastien(400, 760, 1.5, expr="rire", bras="porte", objet=panier_pains(0, -40, 0.9)))
    S.add(rect(80, 300, 150, 60, "#fff", rx=10, stroke="#2f9e44", stroke_width=4), texte(155, 342, "OUVERT", 30, "#2f9e44"))
    return S


def p09():
    S = Scene()
    boutique(S)
    S.add(bastien(560, 640, 1.4, expr="content", bras="donne", flip=True,
                  objet=""))
    S.add(comptoir(560, 780, 460))
    S.add(baguette(430, 505, 0.8, rot=-20))
    S.add(personne(130, 790, 1.5, **MAMAN, expr="sourire", bras="bas", regard=(1, 0)))
    S.add(petit(280, 790, 1.15, **NOUR, expr="joie", bras="tient", regard=(1, -0.5)))
    S.add(bulle(300, 130, 420, 100, "Une baguette bien\ncuite, s'il vous plaît !", 30, pointe=(290, 520)))
    return S


def p10():
    S = Scene()
    interieur(S, "#e5dbff", "#d0bfff", 620, plinthe="#b197fc")
    S.add(fenetre(470, 90, 220, 180, "#a5d8ff", rideaux="#9775fa", contenu=soleil(560, 170, 44)))
    S.add(lit(360, 760, 520, "#74c0fc", "#4dabf7"))
    S.add(personne(370, 640, 0.9, **{**BASTIEN, "acc": (), "tenue": None, "habit": "#ffd43b"},
                   expr="dort", rot=-90, joues=True))
    S.add(rect(268, 592, 360, 110, "#4dabf7", rx=24))
    S.add(zzz(260, 440, 1.2))
    S.add(texte(560, 340, "Bonne nuit !", 50, "#7048e8", contour="#fff"))
    S.add(place(g([cercle(-26, -218, 27.5, "#dee2e6"), cercle(26, -218, 27.5, "#dee2e6"), cercle(0, -232, 31.5, "#dee2e6"),
                   cercle(-26, -218, 26, "#fff"), cercle(26, -218, 26, "#fff"), cercle(0, -232, 30, "#fff"),
                   rect(-40, -208, 80, 26, "#fff", rx=6, stroke="#e9ecef", stroke_width=2)]), 720, 820, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pains-seuls.svg", vignette),
    ("01-la-nuit.svg", p01), ("02-quatre-ingredients.svg", p02), ("03-petrir.svg", p03),
    ("04-la-pate-gonfle.svg", p04), ("05-les-formes.svg", p05), ("06-le-four.svg", p06),
    ("07-croissants.svg", p07), ("08-la-boutique.svg", p08), ("09-une-baguette.svg", p09),
    ("10-bonne-nuit.svg", p10),
]
