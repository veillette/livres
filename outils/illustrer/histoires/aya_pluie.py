"""Aya et le nuage de pluie — ne jamais abandonner.

Dans le village d'Aya, au milieu de la savane, il ne pleut plus et le puits
est sec. Les grands disent qu'on n'y peut rien. Aya part seule réveiller le
Grand Nuage endormi sur la montagne ; en chemin, elle aide une girafe, un
petit éléphant et un oisillon, qui l'aident à leur tour. Là-haut, elle chante
au Nuage la chanson du village : il pleure de joie, et la pluie revient.
"""
from base import *
from base import EXPRESSIONS, _assombrir
from objets import *
from fantastique import personne, PEAUX
from sciences import nuage_perso

ID = "aya-pluie"

AYA = dict(peau="foncee", cheveux="noir", coiffure="tresses", habit="#1098ad", ceinture="#fab005")
MAMIE = dict(peau="foncee", cheveux="gris", coiffure="chignon", habit="#e8590c", ceinture="#fab005",
             acc=("lunettes",))
MAMAN = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#5f3dc4", ceinture="#fcc419")
PAPA = dict(peau="foncee", cheveux="noir", coiffure="courts", robe=False, habit="#2f9e44", jambes="#5c3d2e")
NUAGE_GRIS = dict(couleur="#ced4da", ombre="#adb5bd")
NUAGE_PLUIE = dict(couleur="#e7f5ff", ombre="#a5d8ff")
TERRE, TERRE2 = "#e0a96d", "#d08c4b"


def aya(x, y, s=1.0, **k):
    return personne(x, y, s, **{**AYA, **k})


# ---------------------------------------------------------------------------
# Décors de savane
# ---------------------------------------------------------------------------

def savane(S, haut="#ffb85c", bas="#ffe8a3", y=600, sec=True, sol_c=None):
    ciel(S, haut, bas)
    sol(S, y, sol_c or (TERRE if sec else "#a9d36c"), couleur2=(TERRE2 if sec else "#8cc152"), y2=y + 90)
    if sec:
        r = random.Random(y)
        for _ in range(9):
            x0, y0 = r.uniform(40, 760), r.uniform(y + 40, 790)
            S.add(chemin(f"M {n(x0)} {n(y0)} l 20 6 l 10 -10 l 24 4 m -24 -4 l -4 -14",
                         stroke="#b87333", sw=3, opacity=0.7))


def herbe_seche(x, y, s=1.0, couleur="#c99a3e"):
    m = [chemin(f"M {k * 8 - 16} 0 Q {k * 10 - 20} -30 {k * 14 - 28} -50", stroke=couleur, sw=4) for k in range(5)]
    return place(m, x, y, s)


def baobab(x, y, s=1.0, feuilles=False):
    """Baobab au tronc énorme ; (x, y) = milieu du pied."""
    tronc, fonce = "#a07a5a", "#866248"
    m = [chemin("M -90 0 Q -70 -120 -60 -260 L 60 -260 Q 70 -120 90 0 Z", tronc),
         chemin("M -40 -20 Q -30 -120 -24 -230", stroke=fonce, sw=6),
         chemin("M 30 -10 Q 26 -140 30 -240", stroke=fonce, sw=6)]
    for dx, ex, ey in [(-50, -150, -360), (-20, -60, -390), (20, 50, -400), (50, 150, -350), (0, 0, -330)]:
        m.append(chemin(f"M {dx} -250 Q {(dx + ex) / 2} {ey + 40} {ex} {ey}", stroke=tronc, sw=22))
    if feuilles:
        for ex, ey in [(-150, -360), (-60, -390), (50, -400), (150, -350), (0, -340)]:
            m.append(ellipse(ex, ey - 10, 50, 26, "#69a84f"))
    else:
        for ex, ey in [(-150, -360), (-60, -390), (50, -400), (150, -350)]:
            m.append(ellipse(ex, ey - 8, 26, 12, "#a5a35a"))
    return place(m, x, y, s)


def acacia(x, y, s=1.0, couleur="#7a9a3e"):
    m = [chemin("M -12 0 Q -6 -120 -60 -200 M 0 -110 Q 30 -170 70 -210", stroke="#8d5b34", sw=16),
         trait(-8, 0, -4, -110, "#8d5b34", 18),
         ellipse(-10, -220, 150, 34, couleur), ellipse(-60, -236, 80, 24, _assombrir(couleur, 0.9)),
         ellipse(60, -240, 70, 22, _assombrir(couleur, 0.9))]
    return place(m, x, y, s)


def case(x, y, s=1.0, mur="#c98a52", toit="#d9a441", lumiere=False):
    """Case ronde au toit de paille ; (x, y) = milieu au sol."""
    fonce = _assombrir(toit, 0.8)
    m = [chemin("M -90 0 L -90 -120 Q 0 -134 90 -120 L 90 0 Q 0 10 -90 0 Z", mur),
         chemin("M -30 2 L -30 -70 Q 0 -100 30 -70 L 30 2 Z", "#ffe066" if lumiere else "#5c3d2e"),
         poly([(-120, -112), (0, -250), (120, -112)], toit),
         chemin("M -120 -112 Q 0 -96 120 -112", stroke=fonce, sw=8)]
    for k in range(-3, 4):
        m.append(trait(k * 12, -236, k * 34, -112, fonce, 3, opacity=0.6))
    return place(m, x, y, s)


def puits(x, y, s=1.0, plein=False):
    """Puits de pierres sèches avec sa poulie ; (x, y) = milieu au sol."""
    m = [rect(-110, -100, 220, 100, "#b08968", rx=14)]
    for row in range(2):
        for k in range(4):
            m.append(rect(-104 + k * 54 + (row % 2) * 26, -94 + row * 46, 48, 40, "#c8a27c", rx=10))
    m.append(ellipse(0, -100, 112, 22, "#8a6a4f"))
    m.append(ellipse(0, -100, 94, 15, "#4dabf7" if plein else "#3b2a1e"))
    if plein:
        m.append(ellipse(-20, -102, 30, 4, "#a5d8ff"))
    m += [rect(-104, -250, 14, 152, "#8d5b34", rx=4), rect(90, -250, 14, 152, "#8d5b34", rx=4),
          rect(-110, -258, 220, 14, "#a0693a", rx=6), cercle(0, -240, 14, "#5c3d2e"),
          trait(0, -240, 0, -110, "#c68642", 3)]
    return place(m, x, y, s)


def seau(x, y, s=1.0, plein=False):
    m = [chemin("M -40 -70 Q 0 -120 40 -70", stroke="#495057", sw=4),
         poly([(-40, -70), (40, -70), (30, 0), (-30, 0)], "#868e96"),
         ellipse(0, -70, 40, 9, "#4dabf7" if plein else "#343a40"),
         trait(-36, -40, 36, -40, "#adb5bd", 4)]
    return place(m, x, y, s)


def gourde(x, y, s=1.0):
    """Calebasse ; (x, y) = centre."""
    return place([cercle(0, 10, 30, "#d4a24c"), cercle(0, -26, 16, "#d4a24c"), rect(-6, -48, 12, 12, "#8d5b34", rx=3),
                  chemin("M -22 -2 Q 0 6 22 -2", stroke="#a87b2f", sw=3)], x, y, s)


def chevre(x, y, s=0.6, **k):
    return perso("chevre", x, y, s, **k)


def montagne(x, y, s=1.0, couleur="#a9746e", couleur2="#8f5f5a", sommet=True):
    """Grande montagne ; (x, y) = milieu de la base (largeur ≈ 900, hauteur ≈ 560)."""
    m = [chemin("M -450 0 Q -300 -200 -120 -460 Q -40 -570 40 -560 Q 120 -540 200 -400 Q 320 -200 450 0 Z", couleur),
         chemin("M -60 -520 Q -20 -380 -120 -200 Q -160 -120 -150 0 L -50 0 Q -60 -160 0 -300 Q 50 -420 20 -548 Z", couleur2, opacity=0.6),
         chemin("M -300 -120 Q -200 -140 -150 -230", stroke="#c4918a", sw=10),
         chemin("M 120 -300 Q 200 -280 260 -180", stroke="#c4918a", sw=10)]
    return place(m, x, y, s)


def rocher(x, y, s=1.0, couleur="#9c8a7a"):
    return place([chemin("M -80 0 Q -96 -70 -36 -90 Q 30 -110 76 -60 Q 96 -24 84 0 Z", couleur),
                  chemin("M -40 -70 Q 0 -86 30 -74", stroke=eclaircir(couleur, 0.4), sw=8)], x, y, s)


def epine(x, y, s=1.0, rot=0):
    return place([poly([(-4, 0), (4, 0), (0, -40)], "#5c3d2e")], x, y, s, rot=rot)


def nid(x, y, s=1.0):
    m = [chemin("M -50 -10 Q 0 30 50 -10 Z", "#a0693a")]
    for k in range(5):
        m.append(chemin(f"M {-48 + k * 20} -8 q 10 10 22 0", stroke="#6d4424", sw=3))
    return place(m, x, y, s)


def girafe(x, y, s=1.0, expr="sourire", flip=False, regard=(1, 0), cou=0, epine_=False, larmes=False):
    """Girafe de profil, la tête à droite ; (x, y) = au sol, sous le corps.
    cou : angle (degrés) dont le cou s'incline vers l'avant (0 = dressé)."""
    ys, bs, ss = EXPRESSIONS[expr]
    robe, tache, sabot = "#f6c453", "#c4752b", "#6d4424"
    m = []
    # queue
    m.append(chemin("M -110 -250 Q -132 -200 -126 -150", stroke=robe, sw=8))
    m.append(ellipse(-126, -142, 9, 16, sabot))
    # pattes arrière (plus sombres) puis avant
    for lx, c in [(-78, _assombrir(robe, 0.9)), (52, _assombrir(robe, 0.9)), (-50, robe), (80, robe)]:
        m.append(rect(lx - 9, -230, 18, 222, c, rx=8))
        m.append(rect(lx - 10, -14, 20, 14, sabot, rx=4))
    if epine_:
        m.append(epine(86, -60, 0.8, rot=-30))
    # corps
    m.append(ellipse(0, -255, 120, 58, robe))
    for tx, ty, r in [(-70, -260, 20), (-26, -280, 22), (20, -250, 20), (64, -272, 18), (-40, -230, 15), (40, -228, 14)]:
        m.append(ellipse(tx, ty, r, r * 0.8, tache))
    # cou et tête (tournent ensemble autour de la base du cou)
    t = []
    t.append(chemin("M 50 -280 L 108 -510 L 152 -506 L 116 -240 Z", robe))
    t.append(chemin("M 104 -500 L 50 -282", stroke="#a0693a", sw=10))
    for tx, ty in [(100, -300), (112, -350), (124, -400), (132, -450)]:
        t.append(ellipse(tx + 6, ty, 12, 10, tache))
    t.append(trait(118, -540, 112, -580, "#c4752b", 7) + trait(140, -540, 140, -582, "#c4752b", 7))
    t.append(cercle(112, -582, 8, "#6d4424") + cercle(140, -584, 8, "#6d4424"))
    t.append(ellipse(96, -536, 22, 10, robe, rot=-30))
    t.append(ellipse(140, -520, 48, 34, robe))
    t.append(ellipse(180, -506, 28, 24, "#f9dc9c"))
    t.append(ellipse(194, -512, 3.5, 3, "#6d4424"))
    t.append(ellipse(150, -500, 10, 6, ROSE, opacity=0.7))
    t.append(oeil(140, -530, ys, regard))
    if ss:
        t.append(place(sourcils(0, 0, ss), 140, -530, 0.8))
    t.append(place(bouche(0, 0, bs, 0.7), 186, -496, 0.8))
    if larmes:
        t.append(goutte(132, -500, 0.7, "#74c0fc"))
    m.append(g(t, f"rotate({n(cou)} 90 -280)" if cou else None))
    return place(m, x, y, s, flip=flip)


def gros_nuage(x, y, s=2.4, gris=True, expr="dort", larmes=False):
    return nuage_perso(x, y, s, expr=expr, larmes=larmes, **(NUAGE_GRIS if gris else NUAGE_PLUIE))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(montagne(620, 640, 0.6))
    sol(S, 620, "#a9d36c", couleur2="#8cc152", y2=700)
    S.add(baobab(130, 650, 0.8, feuilles=True))
    S.add(girafe(650, 770, 0.62, flip=True, expr="rire", regard=(-1, 0)))
    S.add(gros_nuage(440, 230, 1.9, gris=False, expr="rire"))
    pluie(S, 40, 3, (180, 330, 720, 600), "#4dabf7")
    S.add(aya(340, 780, 1.6, expr="rire", bras="haut"))
    S.add(perso("elephant", 170, 790, 0.7, expr="rire", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff3bf", rx=30))
    S.add(baobab(200, 262, 0.4, feuilles=True))
    S.add(gros_nuage(200, 58, 0.62, gris=False, expr="content"))
    for k, (gx, gy) in enumerate([(130, 140), (180, 165), (240, 145), (280, 170), (160, 200)]):
        S.add(goutte(gx, gy, 0.6))
    return S


def p01():
    S = Scene()
    savane(S, y=590)
    S.add(soleil(640, 130, 60, "#ffd43b"))
    S.add(montagne(640, 600, 0.35, sommet=False))
    S.add(nuage(650, 410, 0.35, "#dee2e6"))
    S.add(baobab(170, 640, 1.0))
    S.add(case(470, 620, 0.85), case(660, 640, 0.7, mur="#b97a45"))
    S.add(herbe_seche(320, 700), herbe_seche(740, 720, 0.8))
    S.add(chevre(560, 760, 0.55, expr="triste", regard=(-1, 0)), chevre(700, 790, 0.5, expr="triste"))
    S.add(aya(330, 780, 1.3, expr="inquiet", regard=(1, -1)))
    return S


def p02():
    S = Scene()
    savane(S, y=600)
    S.add(soleil(120, 110, 55, "#ffd43b"))
    S.add(case(680, 610, 0.7))
    S.add(puits(470, 720, 1.4))
    S.add(aya(190, 780, 1.4, expr="surpris", bras="porte", objet=seau(0, -48, 0.8)))
    S.add(texte(420, 170, "Pas une goutte…", 56, "#fff", contour="#b87333"))
    return S


def p03():
    S = Scene()
    savane(S, y=600)
    S.add(montagne(620, 600, 0.45))
    S.add(gros_nuage(645, 360, 0.5, expr="dort"))
    S.add(baobab(260, 640, 1.1))
    S.add(personne(100, 770, 1.35, expr="triste", **MAMIE))
    S.add(personne(260, 760, 1.45, expr="triste", bras="croises", **PAPA))
    S.add(personne(410, 770, 1.4, expr="triste", **MAMAN))
    S.add(aya(600, 790, 1.15, expr="inquiet", regard=(-1, 0)))
    S.add(bulle(250, 110, 420, 90, "On n'y peut rien…", 40, pointe=(250, 300)))
    return S


def p04():
    S = Scene()
    savane(S, "#ff8787", "#ffe8a3", y=600)
    S.add(soleil(110, 560, 70, "#ffd43b", rayons=False))
    S.add(montagne(560, 610, 0.75))
    S.add(gros_nuage(575, 200, 0.6, expr="dort"))
    sol(S, 600, TERRE, couleur2=TERRE2, y2=690)
    S.add(case(90, 650, 0.45), case(190, 660, 0.35))
    S.add(aya(300, 780, 1.4, expr="fier", bras="poing", objet=gourde(36, -80, 0.6)))
    S.add(bulle(300, 110, 470, 90, "Je vais le réveiller !", 40, pointe=(300, 400)))
    return S


def p05():
    S = Scene()
    savane(S, y=600)
    S.add(acacia(680, 610, 0.9))
    S.add(girafe(480, 770, 0.82, flip=True, expr="sourire", regard=(-1, 0)))
    S.add(aya(210, 780, 1.35, expr="content", bras="tient", objet=epine(68, -150, 1.2)))
    S.add(bulle(330, 100, 520, 90, "Merci ! Je n'oublierai pas.", 38, pointe=(400, 260)))
    return S


def p06():
    S = Scene()
    savane(S, y=600)
    S.add(acacia(120, 620, 0.8))
    S.add(herbe_seche(700, 680))
    S.add(perso("elephant", 540, 780, 1.4, expr="content", bras="porte", objet=gourde(0, -86, 0.8)))
    S.add(aya(250, 780, 1.35, expr="content", bras="donne"))
    S.add(bulle(400, 110, 520, 100, "Merci ! Je n'oublierai pas.", 38, pointe=(510, 330)))
    return S


def p07():
    S = Scene()
    savane(S, y=620)
    S.add(acacia(470, 640, 1.6))
    S.add(nid(560, 290, 0.9))
    S.add(oiseau(560, 290, 0.45, "#f76707", "#ffe8cc", expr="rire"))
    S.add(oiseau(700, 230, 0.6, "#f76707", "#ffe8cc", expr="content", ailes="ouvertes", pattes=False, flip=True))
    S.add(aya(300, 780, 1.4, expr="content", bras="haut"))
    S.add(bulle(260, 110, 480, 90, "Merci ! Je n'oublierai pas.", 34, pointe=(540, 210)))
    return S


def p08():
    S = Scene()
    ciel(S, "#ffa94d", "#ffe8a3")
    S.add(montagne(430, 640, 1.0))
    S.add(gros_nuage(450, 80, 0.55, expr="dort"))
    sol(S, 630, TERRE, couleur2=TERRE2, y2=710)
    S.add(rocher(560, 760, 1.4), rocher(150, 730, 0.8))
    S.add(aya(560, 650, 1.3, expr="pleure", larmes=True, bras="yeux"))
    S.add(texte(230, 560, "Je n'y arriverai", 34, "#fff", contour="#8f5f5a"))
    S.add(texte(230, 600, "jamais…", 34, "#fff", contour="#8f5f5a"))
    return S


def p09():
    S = Scene()
    ciel(S, "#ffc078", "#fff3bf")
    # pente de la montagne, de bas à gauche vers le haut à droite
    S.add(chemin("M 0 800 L 0 620 Q 300 520 520 330 Q 640 230 800 180 L 800 800 Z", "#a9746e"))
    S.add(chemin("M 0 800 L 0 700 Q 320 620 560 420 Q 680 330 800 300 L 800 800 Z", "#8f5f5a", opacity=0.5))
    S.add(rocher(130, 690, 0.8))
    S.add(perso("elephant", 250, 700, 1.0, expr="concentre", bras="tete", objet=rocher(0, -192, 0.85)))
    S.add(girafe(470, 600, 0.75, expr="rire", cou=18))
    S.add(aya(620, 330, 0.9, expr="fier", bras="haut"))
    S.add(oiseau(700, 120, 0.45, "#f76707", "#ffe8cc", expr="rire", ailes="ouvertes", pattes=False))
    S.add(texte(250, 160, "Un pas, puis un autre…", 44, "#fff", contour="#8f5f5a"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin("M 0 800 L 0 640 Q 200 600 400 560 Q 600 600 800 640 L 800 800 Z", "#a9746e"))
    S.add(gros_nuage(430, 380, 2.4, expr="triste"))
    S.add(aya(180, 790, 1.25, expr="inquiet", regard=(1, -1)))
    S.add(bulle(400, 100, 600, 110, "Laisse-moi dormir…\nPlus personne ne pense à moi.", 34, pointe=(440, 240)))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin("M 0 800 L 0 640 Q 200 600 400 560 Q 600 600 800 640 L 800 800 Z", "#a9746e"))
    S.add(gros_nuage(500, 330, 2.0, expr="surpris"))
    S.add(notes(240, 380, 1.2), notes(330, 450, 0.9))
    S.add(girafe(700, 790, 0.55, flip=True, expr="content", regard=(-1, -1)))
    S.add(oiseau(110, 580, 0.4, "#f76707", "#ffe8cc", expr="chante"))
    S.add(aya(220, 790, 1.3, expr="chante", bras="ouverts"))
    S.add(bulle(400, 95, 640, 120, "Grand Nuage, Grand Nuage,\nviens danser sur nos maisons !", 36, pointe=(260, 300)))
    return S


def p12():
    S = Scene()
    ciel(S, "#74c0fc", "#d0ebff")
    sol(S, 600, "#a9d36c", couleur2="#8cc152", y2=690)
    S.add(baobab(110, 640, 0.8, feuilles=True))
    S.add(case(690, 620, 0.7))
    S.add(gros_nuage(430, 150, 1.7, gris=False, expr="rire", larmes=True))
    pluie(S, 70, 8, (0, 230, 800, 800), "#4dabf7")
    S.add(puits(520, 700, 0.8, plein=True))
    S.add(personne(380, 760, 1.2, expr="rire", bras="danse", **MAMAN))
    S.add(personne(690, 790, 1.2, expr="rire", bras="ouverts", **MAMIE))
    S.add(chevre(560, 790, 0.45, expr="rire"))
    S.add(aya(220, 790, 1.4, expr="rire", bras="danse"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("baobab-pluie.svg", vignette),
    ("01-le-village.svg", p01), ("02-le-puits.svg", p02), ("03-les-grands.svg", p03),
    ("04-le-depart.svg", p04), ("05-la-girafe.svg", p05), ("06-l-elephant.svg", p06),
    ("07-l-oisillon.svg", p07), ("08-la-montagne.svg", p08), ("09-ensemble.svg", p09),
    ("10-le-nuage.svg", p10), ("11-la-chanson.svg", p11), ("12-la-pluie.svg", p12),
]
