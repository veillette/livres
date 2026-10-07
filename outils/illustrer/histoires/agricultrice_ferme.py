"""Jeanne à la ferme — une année avec l'agricultrice, du blé au pain."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from fables import coq, oeuf, moulin, ble, champ_ble, champ_laboure
from contes import carotte, chou, pomme_terre, pain

ID = "agricultrice-ferme"
JEANNE = dict(peau="rosee", cheveux="roux", coiffure="tresses", habit="#ffd43b", jambes="#2f9e44",
              chaussures="#343a40", tenue=salopette("#2f9e44", "#2b8a3e"), coiffe=chapeau_paille())
VERT_TRACTEUR = "#37b24d"


def jeanne(x, y, s=1.6, **k):
    return pro(x, y, s, **{**JEANNE, **k})


def vache(x, y, s=1.0, flip=False, expr="content", broute=False):
    """Vache de profil, tournée vers la droite ; (x, y) = sol, au milieu."""
    ys, bs, _ = EXPRESSIONS[expr]
    m = [chemin("M -150 -150 Q -176 -110 -168 -60", stroke="#495057", sw=6), ellipse(-168, -54, 8, 14, "#495057")]
    for px in (-110, -80, 70, 100):
        m.append(rect(px - 12, -90, 24, 90, "#f8f9fa", rx=8))
        m.append(rect(px - 13, -16, 26, 16, "#495057", rx=4))
    m += [ellipse(0, -140, 150, 72, "#f8f9fa", stroke="#ced4da", stroke_width=4),
          ellipse(-60, -160, 40, 30, "#343a40"), ellipse(40, -110, 30, 22, "#343a40"), ellipse(-110, -120, 22, 30, "#343a40"),
          ellipse(-30, -78, 30, 16, "#ffc9d6")]
    hy = -110 if broute else -180
    m += [ellipse(150, hy, 48, 56, "#f8f9fa", rot=-20 if broute else 0, stroke="#ced4da", stroke_width=4),
          ellipse(180, hy + 34, 40, 28, "#ffc9d6"), cercle(170, hy + 32, 5, "#c2255c"), cercle(194, hy + 32, 5, "#c2255c"),
          ellipse(118, hy - 40, 22, 10, "#f8f9fa", rot=-30), ellipse(118, hy - 40, 14, 5, "#ffc9d6", rot=-30),
          chemin(f"M 140 {hy - 50} q -4 -20 10 -26", stroke="#e9d8c4", sw=7),
          chemin(f"M 166 {hy - 52} q 4 -20 18 -22", stroke="#e9d8c4", sw=7),
          oeil(166, hy - 10, ys)]
    return place(m, x, y, s, flip=flip)


def tracteur(x, y, s=1.0, semoir=False, flip=False):
    """Tracteur de profil tourné vers la droite ; (x, y) = sol, au milieu."""
    m = []
    if semoir:
        m += [rect(-330, -110, 130, 60, "#fab005", rx=8), trait(-200, -80, -150, -80, "#495057", 6)]
        for k in range(5):
            m.append(cercle(-310 + k * 24, -30 + (k % 2) * 12, 5, "#e0a93a"))
    m += [rect(-150, -170, 300, 100, VERT_TRACTEUR, rx=14),
          rect(-140, -310, 130, 150, VERT_TRACTEUR, rx=10), rect(-126, -296, 102, 90, "#a5d8ff", rx=6),
          rect(-150, -320, 150, 16, "#2b8a3e", rx=6),
          rect(90, -230, 16, 70, "#495057"),
          roue(-80, -80, 80, "#343a40", "#fcc419"), roue(110, -50, 50, "#343a40", "#fcc419")]
    return place(m, x, y, s, flip=flip)


def moissonneuse(x, y, s=1.0):
    m = [rect(-200, -260, 300, 200, "#e03131", rx=16), rect(-60, -360, 130, 110, "#e03131", rx=10),
         rect(-46, -346, 100, 70, "#a5d8ff", rx=6), rect(100, -120, 160, 60, "#868e96", rx=8),
         cercle(190, -150, 56, "none", stroke="#fcc419", stroke_width=8)]
    for k in range(6):
        a = math.radians(k * 60)
        m.append(trait(190, -150, 190 + 56 * math.cos(a), -150 + 56 * math.sin(a), "#fcc419", 5))
    m += [chemin("M -200 -240 L -300 -320 L -280 -336 L -186 -270", "#adb5bd"),
          roue(-120, -60, 64), roue(50, -50, 46)]
    return place(m, x, y, s)


def ferme(S, y=600, saison="ete"):
    ciels = {"ete": ("#74c0fc", "#e7f5ff"), "automne": ("#ffc078", "#fff4e6"), "soir": ("#ff8787", "#ffd8a8"),
             "matin": ("#ffc9c9", "#fff3bf")}
    ciel(S, *ciels[saison])
    collines(S, y, "#b2f2bb" if saison != "automne" else "#ffe066", graine=9)
    sol(S, y, "#8ce99a" if saison != "automne" else "#d8f5a2")


def grange(x, y, s=1.0):
    toit = [(-170, -216), (0, -330), (170, -216)]
    return place([ombre_sol(14, 0, 190, 16, 0.16),
                  rect(-150, -220, 300, 220, cylindre("#c92a2a", 0.2, 0.75)), planches(-150, -220, 300, 220, "#c92a2a", larg=20),
                  rect(-150, -220, 14, 220, "#f8f9fa"), rect(136, -220, 14, 220, "#dee2e6"),
                  ombre_avancee(-150, -218, 300, 24, 0.26),
                  poly(toit, lineaire([(0, "#b03a3a"), (0.5, "#862e2e"), (1, "#5c1e1e")], 0, 0, 1, 1)),
                  tuiles(-170, -330, 340, 115, "#862e2e", poly(toit, "#000"), pas_=18),
                  chemin("M -170 -216 L 0 -330 L 170 -216", stroke="#f8f9fa", sw=8),
                  rect(-68, -148, 136, 148, "#f8f9fa"), rect(-60, -140, 120, 140, cylindre("#a61e1e", 0.2, 0.7)),
                  planches(-60, -140, 120, 140, "#a61e1e", larg=20),
                  trait(-60, -140, 60, 0, "#f8f9fa", 8), trait(60, -140, -60, 0, "#f8f9fa", 8), trait(0, -140, 0, 0, "#f8f9fa", 5),
                  rect(-36, -286, 72, 62, "#f8f9fa"), rect(-30, -280, 60, 50, radial([(0, "#495057"), (1, "#212529")])),
                  rect(-40, -228, 80, 8, "#dee2e6", rx=2)], x, y, s)


def poulailler(x, y, s=1.0):
    return place([rect(-110, -150, 220, 150, "#e8a15c"), poly([(-130, -146), (0, -230), (130, -146)], "#a0693a"),
                  rect(-30, -80, 60, 80, "#7c4a1e", rx=30), chemin("M -30 0 L -70 40 L -10 40 L 30 0", "#c68642")], x, y, s)


def bidon(x, y, s=1.0):
    return place([rect(-36, -120, 72, 120, "#ced4da", rx=10), rect(-24, -146, 48, 30, "#adb5bd", rx=6),
                  rect(-36, -80, 72, 10, "#868e96")], x, y, s)


def couverture():
    S = Scene()
    ferme(S)
    S.add(grange(640, 600, 0.9))
    S.add(vache(190, 720, 0.85, flip=True))
    S.add(jeanne(450, 790, 1.85, expr="rire", bras="salut"))
    S.add(coq(660, 790, 0.9, flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ble(70, 260, 1.0), ble(100, 260, 1.1), ble(130, 260, 0.95))
    S.add(pain(240, 230, 1.1))
    S.add(oeuf(350, 250, 1.3))
    return S


def p01():
    S = Scene()
    ferme(S, saison="matin")
    S.add(soleil(150, 520, 60))
    S.add(grange(560, 600, 1.0))
    S.add(coq(170, 700, 1.4, bec_ouvert=True, expr="chante"))
    S.add(texte(220, 230, "Cocorico !", 60, "#e8590c", contour="#fff"))
    S.add(jeanne(400, 790, 1.55, expr="content", bras="salut", regard=(-1, 0)))
    return S


def p02():
    S = Scene()
    interieur(S, "#ffe8cc", "#c8a27a", 600, plinthe="#a0693a")
    for x in range(0, 800, 60):
        S.add(trait(x, 0, x, 590, "#e8c39e", 3))
    S.add(vache(270, 740, 1.1, expr="content"))
    S.add(bidon(545, 770, 1.1))
    S.add(jeanne(680, 790, 1.5, expr="sourire", bras="bas", regard=(-1, 0)))
    S.add(texte(420, 200, "Meuh !", 60, "#495057", contour="#fff"))
    return S


def p03():
    S = Scene()
    ferme(S)
    S.add(poulailler(600, 620, 1.1))
    S.add(coq(470, 720, 0.9, poule=True, flip=True), coq(700, 740, 0.85, poule=True))
    panier = g([chemin("M -60 -60 Q 0 -120 60 -60", stroke="#a0693a", sw=8), rect(-64, -64, 128, 60, "#c68642", rx=12)] +
               [oeuf(-36 + k * 24, -48, 0.6) for k in range(4)])
    S.add(jeanne(250, 790, 1.6, expr="rire", bras="porte", objet=panier))
    S.add(texte(250, 230, "… dix, onze, douze !", 40, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    ferme(S, saison="automne")
    champ_laboure(S, 560)
    S.add(arbre(110, 560, 1.0, "#ff922b", "#f76707"), arbre(700, 560, 0.9, "#fcc419", "#fab005"))
    for x, y in ((90, 300), (160, 420), (730, 330), (650, 460)):
        S.add(ellipse(x, y, 10, 6, "#f76707", rot=30))
    S.add(tracteur(480, 760, 0.95, semoir=True))
    S.add(place(jeanne(0, 0, 1.0, expr="content"), 480 - 75 * 0.95, 760 - 200 * 0.95, 0.65))
    return S


def p05():
    S = Scene()
    # à gauche l'hiver, à droite le printemps
    S.add(rect(0, 0, 400, 800, S.degrade(["#a5d8ff", "#e7f5ff"])))
    S.add(rect(400, 0, 400, 800, S.degrade(["#74c0fc", "#d3f9d8"])))
    S.add(rect(0, 560, 400, 240, "#a0693a"), rect(0, 540, 400, 40, "#f8f9fa", rx=10))
    for k in range(7):
        S.add(chemin(f"M {40 + k * 50} 560 q -4 -26 6 -34", stroke="#69db7c", sw=5))
    flocons(S, 25, 3, (0, 0, 400, 520))
    S.add(rect(400, 560, 400, 240, "#a0693a"))
    for k in range(8):
        S.add(chemin(f"M {430 + k * 46} 600 q -10 -120 6 -220", stroke="#40c057", sw=8))
    S.add(soleil(700, 110, 48), nuage(520, 130, 0.7))
    pluie(S, 12, 4, (460, 190, 600, 330))
    S.add(rect(396, 0, 8, 800, "#fff"))
    S.add(texte(200, 720, "hiver", 56, "#1c7ed6", contour="#fff"), texte(600, 720, "printemps", 56, "#2f9e44", contour="#fff"))
    return S


def p06():
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(soleil(680, 110, 56))
    champ_ble(S, 520, graine=4, n_=50)
    S.add(moissonneuse(400, 740, 1.0))
    for k in range(8):
        S.add(cercle(640 + (k % 3) * 10, 560 + k * 6, 5, "#e0a93a"))
    return S


def p07():
    S = Scene()
    ferme(S)
    S.add(moulin(150, 640, 1.0))
    from sciences import fleche
    S.add(rect(270, 170, 510, 230, "#fff", rx=24, opacity=0.85))
    S.add(ble(330, 350, 0.8), fleche(370, 280, 430, 280, "#e8590c"))
    S.add(rect(450, 230, 80, 90, "#f8f9fa", rx=10, stroke="#ced4da", stroke_width=3), texte(490, 370, "farine", 28, "#a0693a"))
    S.add(fleche(550, 280, 610, 280, "#e8590c"), pain(690, 320, 0.8), texte(690, 370, "pain", 28, "#a0693a"))
    S.add(texte(330, 370, "blé", 28, "#a0693a"))
    S.add(jeanne(520, 790, 1.4, expr="content", bras="montre", regard=(1, -0.5)))
    return S


def p08():
    S = Scene()
    ferme(S)
    S.add(rect(0, 600, 800, 200, "#a0693a"))
    for row, (y, fn) in enumerate([(640, "carotte"), (700, "chou"), (760, "tomate")]):
        for k in range(7):
            x = 60 + k * 110
            if fn == "carotte":
                S.add(chemin(f"M {x} {y} q -14 -30 -8 -40 M {x} {y} q 2 -34 6 -44 M {x} {y} q 18 -28 22 -34", stroke="#40c057", sw=6))
            elif fn == "chou":
                S.add(chou(x, y - 10, 0.4))
            else:
                S.add(trait(x, y, x, y - 70, "#2f9e44", 4), cercle(x - 8, y - 40, 10, "#fa5252"), cercle(x + 8, y - 56, 9, "#fa5252"))
    S.add(jeanne(560, 680, 1.25, expr="rire", bras="porte",
                 objet=g([carotte(-10, -70, 0.45, rot=-30), carotte(10, -70, 0.45, rot=20), pomme_terre(0, -40, 0.6)])))
    return S


def p09():
    S = Scene()
    ciel(S)
    S.add(rect(0, 600, 800, 200, "#ced4da"))
    S.add(rect(150, 300, 500, 60, "#2f9e44"), texte(400, 342, "Ferme de Jeanne", 34, "#fff"))
    S.add(rect(170, 360, 12, 240, "#868e96"), rect(618, 360, 12, 240, "#868e96"))
    S.add(jeanne(400, 640, 1.2, expr="content", bras="large"))
    S.add(rect(140, 560, 520, 140, "#c68642", rx=8), rect(130, 540, 540, 30, "#a0693a", rx=6))
    for k in range(4):
        S.add(oeuf(180 + k * 24, 548, 0.5))
    S.add(chou(330, 520, 0.4), carotte(400, 515, 0.4, rot=-70), carotte(430, 520, 0.4, rot=-80))
    S.add(g([ellipse(560, 525, 50, 22, "#fff3bf"), ellipse(560, 518, 46, 16, "#ffe066")]), texte(560, 600, "fromage", 22, "#a0693a"))
    S.add(petit(720, 790, 1.1, peau="foncee", cheveux="noir", coiffure="tresses", habit="#da77f2", expr="joie",
                regard=(-1, 0)))
    return S


def p10():
    S = Scene()
    ferme(S, saison="soir")
    S.add(soleil(640, 560, 60, "#ff922b", rayons=False))
    S.add(grange(480, 600, 1.0), poulailler(150, 620, 0.8))
    S.add(vache(600, 760, 0.7, expr="dort", broute=False))
    S.add(jeanne(250, 790, 1.5, expr="content", bras="salut"))
    S.add(texte(400, 140, "Bonne nuit, la ferme !", 48, "#c2255c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ble-seul.svg", vignette),
    ("01-cocorico.svg", p01), ("02-les-vaches.svg", p02), ("03-les-oeufs.svg", p03),
    ("04-semer.svg", p04), ("05-hiver-printemps.svg", p05), ("06-la-moisson.svg", p06),
    ("07-du-ble-au-pain.svg", p07), ("08-le-potager.svg", p08), ("09-le-marche.svg", p09),
    ("10-bonne-nuit.svg", p10),
]
