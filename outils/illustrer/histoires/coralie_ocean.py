"""Coralie et l'océan tout propre — prendre soin de la mer."""
from base import *
from objets import *
from fantastique import *
from fables import filet
from sciences import enfant, ondes

ID = "coralie-ocean"
CORALIE = dict(coiffure="tres_longs", cheveux="blond", peau="rosee", habit="#845ef7",
               sirene=("#845ef7", "#d0bfff"), acc=("fleur",), couleur_acc="#ff8787")


def coralie(x, y, s=1.0, **k):
    return personne(x, y, s, **{**CORALIE, **k})


# ---------------------------------------------------------------------------
# Objets et animaux propres à ce livre
# ---------------------------------------------------------------------------

def sac_plastique(x, y, s=1.0, rot=0):
    """Sac en plastique à la dérive : on dirait une méduse. (x, y) = centre."""
    m = [chemin("M -30 8 Q -44 48 -20 74 Q -12 44 -16 10", stroke="#e9ecef", sw=8, opacity=0.85),
         chemin("M 30 8 Q 42 52 18 70 Q 12 42 16 10", stroke="#e9ecef", sw=8, opacity=0.85),
         chemin("M -46 10 Q -58 -50 -20 -66 Q 0 -74 20 -66 Q 58 -50 46 10 Q 30 2 16 12 Q 0 2 -16 12 Q -30 2 -46 10 Z",
                "#f8f9fa", stroke="#ced4da", sw=3, opacity=0.82),
         chemin("M -22 -44 L -10 -8 M 14 -52 L 24 -18 M -2 -30 L 4 -4", stroke="#ced4da", sw=3)]
    return place(m, x, y, s, rot=rot)


def bouteille(x, y, s=1.0, rot=0, bouchon="#fa5252", etiquette="#ffd43b"):
    """Bouteille en plastique ; (x, y) = centre."""
    m = [rect(-22, -50, 44, 100, "#d0ebff", rx=14, opacity=0.9, stroke="#74c0fc", stroke_width=3),
         rect(-11, -70, 22, 24, "#d0ebff", rx=5, stroke="#74c0fc", stroke_width=3),
         rect(-13, -84, 26, 16, bouchon, rx=4),
         rect(-22, -10, 44, 26, etiquette),
         rect(-14, -40, 6, 24, "#ffffff", rx=3, opacity=0.8)]
    return place(m, x, y, s, rot=rot)


def canette(x, y, s=1.0, rot=0, couleur="#e03131"):
    m = [rect(-18, -34, 36, 68, couleur, rx=6), ellipse(0, -34, 18, 6, "#ced4da"),
         rect(-18, -8, 36, 12, "#ffffff", opacity=0.7)]
    return place(m, x, y, s, rot=rot)


def bouchon(x, y, s=1.0, couleur="#4dabf7"):
    return place([rect(-12, -8, 24, 16, couleur, rx=4), trait(-8, -8, -8, 8, assombrir(couleur, 0.8), 2),
                  trait(0, -8, 0, 8, assombrir(couleur, 0.8), 2), trait(8, -8, 8, 8, assombrir(couleur, 0.8), 2)], x, y, s)


def dechets(graine=1, zone=(60, 700, 740, 780), nb=7):
    """Petits déchets éparpillés sur le sable."""
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    m = []
    for k in range(nb):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        if k % 3 == 0:
            m.append(bouteille(x, y, 0.6, rot=r.choice([70, -75, 100])))
        elif k % 3 == 1:
            m.append(canette(x, y, 0.6, rot=r.choice([80, -90, 20]), couleur=r.choice(["#e03131", "#1c7ed6", "#2f9e44"])))
        else:
            m.append(bouchon(x, y, 0.8, r.choice(["#4dabf7", "#fab005", "#fa5252"])))
    return g(m)


def dauphin(x, y, s=1.0, flip=False, expr="sourire", objet=None, rot=0):
    """Dauphin de profil, tête à droite ; (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    c, fonce = "#74c0fc", "#4dabf7"
    m = [chemin("M -120 -2 Q -150 -40 -190 -46 Q -168 -8 -190 34 Q -150 30 -120 8 Z", fonce),
         chemin("M -20 -52 Q -10 -100 -54 -108 Q -38 -78 -54 -48 Z", fonce),
         chemin("M -130 0 Q -60 -64 40 -54 Q 92 -48 112 -22 L 156 -12 Q 164 0 152 8 L 110 10 Q 60 42 -40 32 Q -100 24 -130 0 Z", c),
         chemin("M -70 22 Q 20 40 108 8 L 150 6 Q 120 14 108 16 Q 40 44 -70 22 Z", "#e7f5ff"),
         chemin("M 10 14 Q -6 54 -40 60 Q -20 34 -10 12 Z", fonce),
         oeil(80, -24, ys, (0.4, 0)),
         chemin("M 112 0 Q 130 8 150 2", stroke=assombrir(fonce, 0.7), sw=3),
         ellipse(98, -6, 8, 5, ROSE, opacity=0.7)]
    if objet:
        m.append(objet)
    return place(m, x, y, s, flip=flip, rot=rot)


def conque(x, y, s=1.0, rot=0):
    """Grand coquillage en spirale ; la pointe (pour souffler) est en (0, 0), l'ouverture à droite."""
    m = [chemin("M 0 0 Q 30 -30 80 -40 Q 130 -46 140 0 Q 130 46 80 40 Q 30 30 0 0 Z", "#ffc9c9", stroke="#fa5252", sw=3),
         chemin("M 30 -18 Q 40 0 30 18 M 60 -30 Q 74 0 60 30 M 92 -38 Q 108 0 92 38", stroke="#ff8787", sw=4),
         ellipse(128, 0, 14, 30, "#ffe3e3")]
    return place(m, x, y, s, rot=rot)


def etoile_mer(x, y, s=1.0, couleur="#ff922b", rot=0):
    m = [etoile5(0, 0, 34, couleur, rot=rot)]
    for k in range(5):
        a = math.radians(rot - 90 + k * 72)
        m.append(cercle(math.cos(a) * 16, math.sin(a) * 16, 3, "#fff4e6"))
    return place(m, x, y, s)


def seau(x, y, s=1.0, couleur="#fab005"):
    m = [chemin("M -36 -66 Q 0 -120 36 -66", stroke=ENCRE, sw=4),
         chemin("M -40 -66 L 40 -66 L 32 0 L -32 0 Z", couleur),
         rect(-42, -72, 84, 12, assombrir(couleur, 0.85), rx=6)]
    return place(m, x, y, s)


def filet_plein(x, y, s=1.0):
    """Le vieux filet refermé en sac, rempli de déchets ; (x, y) = nœud en haut."""
    m = [bouteille(-50, 120, 0.9, rot=-20), canette(40, 140, 0.9, rot=15), sac_plastique(0, 70, 0.8),
         bouteille(60, 60, 0.8, rot=30, bouchon="#4dabf7", etiquette="#69db7c"), canette(-70, 60, 0.8, rot=-40, couleur="#1c7ed6"),
         bouchon(-10, 170, 1.0, "#fab005"), bouchon(20, 190, 1.0)]
    cid = uid("f")
    forme = chemin("M 0 0 Q 130 40 120 150 Q 100 220 0 220 Q -100 220 -120 150 Q -130 40 0 0 Z", "#000")
    lignes = []
    for k in range(-10, 12):
        lignes.append(trait(k * 30, 0, k * 30 + 240, 240, "#c68642", 4))
        lignes.append(trait(k * 30, 0, k * 30 - 240, 240, "#c68642", 4))
    m.append(el("clipPath", forme, id=cid))
    m.append(g(lignes, clip_path=f"url(#{cid})"))
    m.append(cercle(0, 0, 10, "#c68642"))
    return place(m, x, y, s)


def rocher(x, y, s=1.0, couleur="#868e96"):
    return place(chemin("M -110 0 Q -120 -60 -50 -80 Q 20 -110 80 -70 Q 120 -40 110 0 Z", couleur), x, y, s)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

COULEURS_CORAIL = ["#ff8787", "#ffa94d", "#da77f2", "#ffd43b", "#f783ac"]


def recif(S, gris=False, deco=True):
    if gris:
        ocean(S, "#5c7f99", "#2f4858", "#c9b98f", rayons=False)
        couleurs = ["#adb5bd", "#868e96", "#ced4da", "#adb5bd", "#868e96"]
        alg = ("#7d8f80", "#6c7a6f")
    else:
        ocean(S)
        couleurs = COULEURS_CORAIL
        alg = ("#40c057", "#2f9e44")
    if deco:
        S.add(algue(60, 720, 1.1, alg[0], graine=1), algue(750, 730, 1.0, alg[1], graine=2))
        S.add(corail(150, 730, 0.9, couleurs[0]), corail(660, 740, 0.8, couleurs[2]))
        S.add(coquillage(260, 770, 0.6, "#ced4da" if gris else "#ffc9d6"))
        if not gris:
            S.add(etoile_mer(560, 770, 0.8, rot=12))
    S.add(bulles_eau(700, 400, 1.0, graine=3), bulles_eau(110, 300, 0.8, graine=5))


def plage(S):
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(680, 100, 50), nuage(180, 110, 0.8))
    S.add(rect(0, 300, 800, 240, "#4dabf7"))
    for k in range(5):
        yy = 330 + k * 40
        d = " ".join(f"M {(k % 2) * 60 + i * 140} {yy} q 20 -12 40 0" for i in range(7))
        S.add(chemin(d, stroke="#a5d8ff", sw=5))


def sable_plage(S, y=520):
    S.add(chemin(f"M 0 {y} Q 200 {y - 24} 420 {y - 4} T 800 {y - 10} L 800 800 L 0 800 Z", "#f4d58d"))
    S.add(chemin(f"M 0 {y} Q 200 {y - 24} 420 {y - 4} T 800 {y - 10}", stroke="#ffffff", sw=10, opacity=0.8))
    for k in range(18):
        S.add(cercle(30 + (k * 91) % 760, y + 40 + (k * 47) % 220, 3, "#e8c170"))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    recif(S)
    S.add(corail(420, 760, 1.1, "#ffd43b"), algue(560, 760, 1.2, "#51cf66", graine=4))
    S.add(dauphin(590, 230, 0.75, flip=True, expr="rire"))
    S.add(coralie(320, 590, 1.7, expr="rire", bras="salut"))
    S.add(tortue(620, 770, 0.8, flip=True, expr="content"))
    S.add(poisson(120, 440, 0.7, "#ff922b"), poisson(700, 430, 0.6, "#ffd43b", flip=True), poisson(170, 180, 0.55, "#f783ac"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 150, 160, 110, "#d0ebff"))
    S.add(corail(150, 250, 0.9, "#ff8787"), corail(260, 250, 0.7, "#da77f2"), algue(330, 255, 0.6, graine=3))
    S.add(etoile_mer(205, 236, 0.8, rot=10))
    S.add(poisson(250, 100, 0.8, "#ffd43b", bulles=True), bulles_eau(90, 170, 0.6, graine=4))
    return S


def p01():
    S = Scene()
    recif(S)
    S.add(corail(300, 770, 1.0, "#ffd43b"), corail(520, 760, 1.2, "#ffa94d"), algue(410, 780, 1.1, "#51cf66", graine=8))
    S.add(coralie(410, 560, 1.4, expr="content", bras="salut"))
    S.add(poisson(180, 260, 0.7, "#ffd43b"), poisson(240, 340, 0.55, "#ff922b"), poisson(640, 250, 0.6, "#f783ac", flip=True))
    S.add(etoile_mer(110, 780, 0.7, "#f783ac", rot=30))
    return S


def p02():
    S = Scene()
    recif(S)
    S.add(sac_plastique(560, 190, 1.1, rot=8), sac_plastique(690, 380, 0.9, rot=-10), sac_plastique(470, 380, 0.75, rot=4))
    S.add(coralie(220, 580, 1.3, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(bulle(230, 110, 360, 90, "Des méduses ?", 42, pointe=(230, 260)))
    return S


def p03():
    S = Scene()
    recif(S)
    S.add(tortue(190, 660, 1.5, expr="miam"))
    S.add(sac_plastique(470, 500, 0.95, rot=-6))
    S.add(coralie(670, 580, 1.2, flip=True, expr="surpris", bras="montre"))
    S.add(bulle(380, 120, 600, 120, "Stop, Tortue ! Ce n'est pas\nune méduse !", 38, pointe=(600, 300)))
    return S


def p04():
    S = Scene()
    recif(S, gris=True)
    S.add(dechets(graine=4, zone=(60, 690, 740, 780), nb=9))
    S.add(bouteille(560, 620, 0.9, rot=60), canette(250, 650, 0.9, rot=-20, couleur="#1c7ed6"))
    S.add(sac_plastique(700, 560, 0.8, rot=20))
    S.add(coralie(400, 560, 1.35, expr="triste", bras="bas"))
    return S


def p05():
    S = Scene()
    recif(S, gris=True)
    S.add(rocher(520, 690, 1.6, "#6c757d"))
    S.add(poisson(520, 470, 1.5, "#ffa94d", expr="pleure"))
    S.add(goutte(590, 470, 0.8, "#a5d8ff"))
    S.add(filet(360, 360, 320, 230, "#c68642", tendu=False))
    S.add(coralie(160, 580, 1.1, expr="surpris", regard=(1, 0)))
    S.add(bulle(520, 140, 360, 100, "Au secours !", 46, pointe=(560, 380)))
    return S


def p06():
    S = Scene()
    recif(S, gris=True)
    S.add(filet(80, 590, 260, 120, "#c68642", tendu=False))
    S.add(coralie(380, 570, 1.4, expr="concentre", bras="tire", regard=(1, 0)))
    S.add(poisson(640, 300, 1.0, "#ffa94d", expr="rire", bulles=True))
    S.add(mouvement(570, 290, 1.0, "#ffffff"))
    S.add(texte(400, 120, "Libre !", 72, "#fff3bf", contour="#1864ab"))
    return S


def tas_dechets(x, y, s=1.0):
    m = [bouteille(-120, -20, 0.9, rot=-80), canette(-60, -30, 0.9, rot=10), sac_plastique(0, -100, 0.9, rot=-10),
         bouteille(60, -50, 0.9, rot=40, bouchon="#4dabf7", etiquette="#69db7c"), canette(110, -20, 0.9, rot=-70, couleur="#1c7ed6"),
         bouteille(-20, -40, 1.0, rot=95), canette(-100, -90, 0.8, rot=50, couleur="#2f9e44"),
         bouteille(90, -130, 0.8, rot=-30), sac_plastique(-90, -170, 0.7, rot=20), canette(30, -170, 0.8, rot=80),
         bouchon(140, -90, 1.0, "#fab005"), bouchon(-150, -60, 1.0)]
    return place(m, x, y, s)


def p07():
    S = Scene()
    recif(S, gris=True)
    S.add(tas_dechets(560, 760, 1.3))
    S.add(coralie(200, 590, 1.2, expr="triste", bras="joues"))
    S.add(bulle(330, 120, 560, 120, "Je n'y arriverai jamais\ntoute seule…", 38, pointe=(220, 330)))
    return S


def p08():
    S = Scene()
    recif(S, gris=True)
    S.add(coralie(220, 600, 1.3, expr="souffle", bras="bouche"))
    S.add(conque(232, 446, 0.9, rot=-10))
    S.add(ondes(370, 400, r0=30, nb=3, ecart=30, direction=0, ouverture=60, couleur="#fff3bf"))
    S.add(dauphin(590, 200, 0.8, flip=True, expr="rire"))
    S.add(poulpe(640, 480, 0.6, expr="joie"))
    S.add(crabe(500, 760, 0.55, expr="rire"), crabe(700, 770, 0.5, "#ff922b", expr="rire"))
    S.add(poisson(470, 300, 0.6, "#ffd43b", flip=True), poisson(720, 330, 0.5, "#f783ac", flip=True))
    S.add(tortue(480, 640, 0.7, flip=True, expr="content"))
    S.add(texte(300, 110, "Tou-tou-touuu !", 54, "#fff3bf", contour="#1864ab"))
    return S


def p09():
    S = Scene()
    recif(S, gris=True, deco=False)
    S.add(filet(250, 560, 300, 200, "#c68642", tendu=False))
    S.add(poulpe(640, 470, 0.85, expr="rire"))
    for k, (bx, by) in enumerate([(546, 510), (570, 530), (600, 540), (630, 540), (660, 540), (690, 530), (716, 520), (740, 500)]):
        if k % 2 == 0:
            S.add(bouteille(bx, by, 0.4, rot=-20 + k * 6))
        else:
            S.add(canette(bx, by, 0.4, rot=k * 10, couleur="#1c7ed6"))
    S.add(crabe(120, 770, 0.6, expr="rire"), bouchon(120, 690, 0.9, "#fab005"))
    S.add(crabe(300, 790, 0.5, "#ff922b", expr="rire"), bouchon(300, 730, 0.8))
    S.add(coralie(220, 470, 1.1, expr="rire", bras="porte", objet=bouteille(0, -80, 0.6, rot=90)))
    S.add(poisson(420, 280, 0.6, "#ffd43b"), canette(470, 280, 0.35, rot=90))
    S.add(texte(400, 110, "Hop ! Dans le filet !", 58, "#fff3bf", contour="#1864ab"))
    return S


def p10():
    S = Scene()
    ocean(S, "#4dabf7", "#1864ab", "#f4d58d", y_sable=720)
    S.add(rect(0, 0, 800, 40, "#a5d8ff", opacity=0.6))
    S.add(chemin("M 0 40 " + " ".join("q 25 -10 50 0" for _ in range(16)), stroke="#e7f5ff", sw=5))
    S.add(trait(540, 300, 637, 222, "#c68642", 6))
    S.add(filet_plein(540, 300, 1.0))
    S.add(mouvement(190, 470, 1.4, "#ffffff"))
    S.add(dauphin(330, 480, 1.0, expr="concentre"))
    S.add(coralie(700, 380, 0.9, expr="rire", bras="haut"))
    S.add(texte(230, 150, "Ho hisse !", 64, "#fff3bf", contour="#1864ab"))
    return S


def p11():
    S = Scene()
    plage(S)
    S.add(rocher(160, 520, 1.1, "#868e96"))
    S.add(coralie(160, 450, 0.9, expr="content", bras="salut"))
    S.add(rect(0, 420, 330, 110, "#4dabf7", opacity=0.75))
    sable_plage(S)
    S.add(filet_plein(330, 560, 0.55))
    S.add(enfant(440, 720, 1.05, habit="#fa5252", jambes="#364fc7", peau="foncee", cheveux="noir", coiffure="boucles",
                 expr="rire", bras="porte", objet=seau(0, -40, 0.7)))
    S.add(enfant(670, 740, 1.05, habit="#20c997", robe=True, peau="claire", cheveux="roux", coiffure="tresses",
                 expr="content", bras="montre", flip=True, objet=bouteille(86, -130, 0.45)))
    S.add(bouteille(560, 770, 0.5, rot=80), canette(730, 700, 0.5, rot=-80))
    S.add(bulle(560, 150, 440, 110, "Nous aussi,\non ramasse tout !", 38, pointe=(650, 470)))
    return S


def p12():
    S = Scene()
    recif(S)
    S.add(corail(300, 770, 1.0, "#ffd43b"), corail(520, 760, 1.2, "#ffa94d"), algue(410, 780, 1.1, "#51cf66", graine=8))
    S.add(coralie(400, 560, 1.35, expr="rire", bras="haut"))
    S.add(dauphin(170, 210, 0.6, expr="rire"), poulpe(660, 400, 0.5, expr="rire"))
    S.add(tortue(150, 640, 0.7, expr="content"), crabe(640, 780, 0.45, expr="rire"))
    S.add(poisson(560, 230, 0.6, "#ffd43b", flip=True), poisson(650, 180, 0.5, "#ff922b", flip=True), poisson(300, 320, 0.5, "#f783ac"))
    S.add(coeur(400, 160, 1.4), etincelles(400, 300, 1.4, graine=3, couleur="#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("recif.svg", vignette),
    ("01-le-recif.svg", p01), ("02-meduses.svg", p02), ("03-stop-tortue.svg", p03),
    ("04-tout-gris.svg", p04), ("05-au-secours.svg", p05), ("06-libre.svg", p06),
    ("07-trop-de-dechets.svg", p07), ("08-la-conque.svg", p08), ("09-dans-le-filet.svg", p09),
    ("10-ho-hisse.svg", p10), ("11-la-plage.svg", p11), ("12-tout-propre.svg", p12),
]
