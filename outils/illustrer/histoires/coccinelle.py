"""La petite coccinelle — la vie de la coccinelle à sept points.

Au printemps, la coccinelle pond ses œufs jaunes, en petit tas, sous une
feuille, tout près des pucerons. Il en sort des larves noires tachées
d'orange qui ressemblent à de petits crocodiles ; elles mangent des
centaines de pucerons et changent plusieurs fois de peau. Puis la larve
s'accroche à une feuille et devient une nymphe. Une semaine plus tard sort
une coccinelle toute jaune et sans points : sa couleur rouge et ses points
apparaissent en quelques heures. Sous les élytres, ses ailes dures, sont
pliées de fines ailes pour voler. Son rouge dit aux oiseaux « Je ne suis
pas bonne » ; attaquée, elle laisse couler par les pattes un liquide jaune
et amer. Le nombre de points dépend de l'espèce, pas de l'âge. L'hiver, les
coccinelles se serrent à l'abri, sous l'écorce ou entre les pierres.

Plans : 1 gros plan (les œufs sous la feuille) · 2 gros plan (la larve) ·
3 moyen (les pucerons du rosier) · 4 gros plan (la nymphe) · 5 gros plan
(toute pâle) · 6 schéma (les ailes) · 7 moyen (elle s'envole du doigt) ·
8 large (l'amie du jardinier) · 9 moyen (l'oiseau : pouah !) · 10 schéma
(combien de points ?) · 11 moyen (l'hiver, toutes ensemble) · 12 schéma (le
cycle).
"""
from base import *
from base import _assombrir
from animaux import etiquette, cycle, disque, herbes
from sciences import fleche
from fantastique import personne, mains_personne

ID = "coccinelle"
# dans un livre de coccinelles, c'est une souris qui se cache
CACHE = "souris"

ROUGE = "#e03131"
NOIR = "#212529"
JAUNE_PALE = "#ffe8a3"

POINTS = {
    7: [(0, -24, 8), (-26, -6, 9), (26, -6, 9), (-32, 24, 8), (32, 24, 8), (-14, 38, 7), (14, 38, 7)],
    2: [(-24, 10, 11), (24, 10, 11)],
    22: [(sx * x, y, 4.5) for sx in (-1, 1) for x, y in ((10, -18), (28, -16), (42, -2), (16, -2), (30, 10), (12, 14),
                                                          (44, 20), (26, 26), (12, 32), (34, 38), (18, 46))],
}


def coccinelle_d(x, y, s=1.0, rot=0, couleur=ROUGE, points=7, pale=False, vol=False, expr="sourire", couleur_points=NOIR):
    """Coccinelle vue de dessus, tête en haut ; (x, y) = centre du dos.
    vol : élytres levées et ailes déployées ; pale : juste sortie de la nymphe."""
    if pale:
        couleur, points = JAUNE_PALE, 0
    m = []
    elytre = "M 0 -30 Q -52 -32 -54 8 Q -50 54 0 58 Z"
    if vol:
        for sgn in (-1, 1):
            m.append(place([chemin("M 0 0 Q 80 -10 140 50 Q 150 110 104 136 Q 50 110 0 14 Z", "#e9f2ff", stroke="#adb5bd", sw=2, opacity=0.85),
                            chemin("M 0 4 Q 60 30 108 120 M 10 6 Q 90 10 136 56", stroke="#ced4da", sw=2)], sgn * 10, -16, 1.0, flip=sgn < 0))
    for sgn in (-1, 1):
        for (ax, ay), (gx, gy), (px, py) in (((26, -26), (46, -36), (52, -50)), ((34, 2), (54, 4), (62, 14)), ((28, 28), (46, 40), (52, 54))):
            m.append(chemin(f"M {sgn * ax} {ay} L {sgn * gx} {gy} L {sgn * px} {py}", stroke=NOIR, sw=4))
        m.append(chemin(f"M {sgn * 6} -54 Q {sgn * 14} -72 {sgn * 22} -76", stroke=NOIR, sw=3))
        m.append(cercle(sgn * 23, -77, 4, NOIR))
    m.append(ellipse(0, 10, 44, 46, NOIR))
    for sgn in (-1, 1):
        demi = [chemin(elytre, volume(couleur, 0.3, 0.75))]
        for px, py, r in POINTS.get(points, []):
            if px * -1 >= 0 and not (px == 0):
                demi.append(cercle(px, py, r, couleur_points))
        if points == 7:
            demi.append(cercle(0, -24, 8, couleur_points))
        demi.append(chemin("M -14 -20 Q -36 -18 -42 4", stroke="#fff", sw=4, opacity=0.45))
        if vol:
            m.append(place(place(demi, 0, 30), sgn * 8, -30, 1.0, flip=sgn > 0, rot=-sgn * 30))
        else:
            m.append(place(demi, 0, 0, 1.0, flip=sgn > 0))
    if not vol:
        m.append(trait(0, -30, 0, 58, NOIR, 2.5))
    m += [ellipse(0, -34, 30, 14, NOIR), ellipse(-21, -34, 6, 5, "#fff"), ellipse(21, -34, 6, 5, "#fff"),
          ellipse(0, -50, 17, 11, NOIR)]
    if expr:
        yeux = "heureux" if expr == "content" else ("fermes" if expr == "dort" else "normal")
        for sgn in (-1, 1):
            m.append(cercle(sgn * 8, -53, 5, "#fff"))
            m.append(oeil(sgn * 8, -53, yeux, (0, -0.3), taille=0.42))
    return place(m, x, y, s, rot=rot) + occuper(x - 62 * s, y - 80 * s, x + 62 * s, y + 60 * s)


def larve(x, y, s=1.0, rot=0, flip=False, expr="sourire", mange=False):
    """Larve de coccinelle (« petit crocodile ») vue de dessus, tête à droite ; (x, y) = milieu."""
    corps = "#3b4250"
    m = []
    for k, px in enumerate((40, 60, 80)):
        for sgn in (-1, 1):
            m.append(chemin(f"M {px} {sgn * 8} L {px + 6} {sgn * 30} L {px + 14} {sgn * 36}", stroke=NOIR, sw=4))
    segs = [(-90, 9), (-74, 12), (-56, 15), (-36, 18), (-14, 20), (8, 21), (30, 20), (52, 19), (72, 17)]
    for k, (px, r) in enumerate(segs):
        m.append(ellipse(px, 0, r * 0.9, r, volume(corps, 0.35, 0.8)))
        if k in (3, 5):
            for sgn in (-1, 1):
                m.append(cercle(px, sgn * r * 0.55, r * 0.32, "#fd7e14"))
        elif k > 0:
            for sgn in (-1, 1):
                m.append(cercle(px, sgn * r * 0.55, 2.5, "#868e96"))
    m.append(ellipse(94, 0, 14, 12, NOIR))
    m.append(chemin("M 102 -8 L 116 -16 M 102 8 L 116 16", stroke=NOIR, sw=2.5))
    if expr:
        for sgn in (-1, 1):
            m.append(cercle(98, sgn * 5, 3.5, "#fff"))
            m.append(cercle(99, sgn * 5, 1.8, NOIR))
    if mange:
        m.append(place(puceron_dessin(), 120, 0, 0.6, rot=90))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 100 * s, y - 40 * s, x + 120 * s, y + 40 * s)


def nymphe(x, y, s=1.0, rot=0, vide=False):
    """Nymphe accrochée par l'arrière (à gauche), tête à droite ; vide : l'enveloppe ouverte."""
    m = [chemin("M -70 -10 Q -84 0 -70 10 L -40 14 L -40 -14 Z", "#495057")]
    c = "#e8a33d" if not vide else "#f1d9a8"
    m.append(chemin("M -44 -22 Q 0 -44 40 -30 Q 66 -14 62 8 Q 54 34 10 34 Q -40 30 -44 22 Z", volume(c, 0.3, 0.8), opacity=0.7 if vide else 1))
    if not vide:
        for px, py in ((-20, -18), (6, -26), (30, -18), (-12, 18), (18, 22), (44, 4)):
            m.append(cercle(px, py, 5, NOIR))
        m.append(chemin("M -30 -6 Q 10 -14 50 -4", stroke="#c47a1d", sw=3))
    else:
        m.append(chemin("M 20 -32 L 30 -10 L 18 4 L 34 30", stroke="#c9a46a", sw=3))
    return place(m, x, y, s, rot=rot) + occuper(x - 80 * s, y - 40 * s, x + 66 * s, y + 36 * s)


def puceron_dessin(couleur="#94d82d"):
    m = []
    for k in range(3):
        for sgn in (-1, 1):
            m.append(trait(-4 + k * 8, sgn * 8, -8 + k * 10, sgn * 18, "#5c940d", 2))
    m += [ellipse(0, 0, 18, 11, volume(couleur, 0.4, 0.8)), cercle(16, 0, 6, couleur),
          trait(20, -3, 34, -12, "#5c940d", 1.6), trait(20, 3, 34, 12, "#5c940d", 1.6),
          trait(-14, -4, -22, -8, "#5c940d", 3), trait(-14, 4, -22, 8, "#5c940d", 3), cercle(18, -2, 1.6, NOIR)]
    return m


def puceron(x, y, s=1.0, rot=0, couleur="#94d82d"):
    return place(puceron_dessin(couleur), x, y, s, rot=rot)


def oeufs(x, y, s=1.0, nb=18, graine=1, eclos=0):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        a = k * 2.4
        d = 9 * math.sqrt(k)
        px, py = math.cos(a) * d, math.sin(a) * d
        if k < eclos:
            m.append(ellipse(px, py, 6, 9, "#fff9db", stroke="#e9d8a6", stroke_width=1.5, opacity=0.8))
        else:
            m.append(ellipse(px, py, 6, 9, volume("#fcc419", 0.4, 0.8)))
    return place(m, x, y, s)


def feuille(x, y, s=1.0, rot=0, couleur="#69db7c", longueur=600, dessous=False):
    """Grande feuille vue de dessus ; (x, y) = base du pétiole, pointe vers la droite."""
    L = longueur
    c = _assombrir(couleur, 0.9) if dessous else couleur
    m = [trait(-60, 0, 10, 0, "#5c940d", 10),
         chemin(f"M 0 0 Q {L * 0.25} {-L * 0.3} {L} 0 Q {L * 0.25} {L * 0.3} 0 0 Z", volume(c, 0.3, 0.8)),
         chemin(f"M 0 0 Q {L * 0.5} -6 {L * 0.96} 0", stroke=eclaircir(c, 0.4) if dessous else "#b2f2bb", sw=6 if dessous else 4)]
    for k in range(1, 7):
        px = L * k / 8
        for sgn in (-1, 1):
            m.append(chemin(f"M {px} {sgn * -2} Q {px + L * 0.06} {sgn * L * 0.06} {px + L * 0.1} {sgn * L * 0.11 * (1 - k / 9)}",
                            stroke=eclaircir(c, 0.35) if dessous else "#b2f2bb", sw=4 if dessous else 3))
    return place(m, x, y, s, rot=rot)


def jardin_doux(S, graine=1, haut="#d0ebff", bas="#f4fce3"):
    """Arrière-plan de gros plan : le jardin flou derrière."""
    ciel(S, haut, bas)
    r = random.Random(graine)
    for _ in range(10):
        c = r.choice(("#8ce99a", "#69db7c", "#c0eb75", "#ffe066", "#ffc9c9", "#b2f2bb"))
        S.add(ellipse(r.uniform(0, 800), r.uniform(200, 800), r.uniform(120, 220), r.uniform(90, 170),
                      radial([(0, c, 0.6), (0.6, c, 0.3), (1, c, 0)])))
    for _ in range(10):
        S.add(cercle(r.uniform(0, 800), r.uniform(0, 800), r.uniform(10, 28), radial([(0, "#ffffff", 0.5), (0.8, "#ffffff", 0.2), (1, "#ffffff", 0)])))


def tige_rosier(x, y0=800, y1=120, s=1.0):
    m = [trait(x, y0, x, y1, "#5c940d", 22 * s)]
    for k in range(6):
        yy = y0 - (k + 0.5) * (y0 - y1) / 6
        sgn = 1 if k % 2 else -1
        m.append(poly([(x + sgn * 10 * s, yy), (x + sgn * 28 * s, yy - 14 * s), (x + sgn * 10 * s, yy - 18 * s)], "#a9504a"))
    return g(m)


def rose(x, y, s=1.0, couleur="#f06595"):
    m = [cercle(0, 0, 60, volume(couleur, 0.3, 0.8))]
    for k, r in enumerate((48, 36, 24, 12)):
        m.append(chemin(f"M {-r} 4 Q 0 {-r * 1.2} {r} 4", stroke=_assombrir(couleur, 0.8), sw=4))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin_doux(S, 1)
    S.add(feuille(80, 700, 1.15, rot=-28))
    for x, y, r in ((520, 380, 20), (560, 420, 40), (600, 360, -10)):
        S.add(puceron(x, y, 0.8, rot=r))
    S.add(coccinelle_d(360, 520, 2.4, rot=40, expr="content"))
    S.add(coccinelle_d(640, 200, 0.9, rot=30, vol=True))
    S.cachette(170, 655)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(feuille(40, 220, 0.55, rot=-18))
    S.add(coccinelle_d(200, 150, 1.1, rot=60, expr="content"))
    return S


def p01():
    """Gros plan : sous une feuille, la coccinelle a pondu un petit tas d'œufs jaunes, près des pucerons."""
    S = Scene()
    jardin_doux(S, 2, "#b2f2bb", "#e9fac8")
    S.add(feuille(-80, 520, 1.6, rot=-6, couleur="#51cf66", dessous=True))
    S.add(oeufs(330, 500, 1.6, nb=22))
    for x, y, r in ((560, 420, 10), (610, 470, -20), (650, 410, 30), (580, 540, 0)):
        S.add(puceron(x, y, 0.9, rot=r))
    S.add(coccinelle_d(200, 650, 1.3, rot=-60, expr="content"))
    S.add(etiquette(330, 330, "des œufs", 36, "#e67700"))
    S.cachette(700, 520)
    return S


def p02():
    """Gros plan : des œufs sortent de petites larves noires tachées d'orange : on dirait de petits crocodiles."""
    S = Scene()
    jardin_doux(S, 3, "#b2f2bb", "#e9fac8")
    S.add(feuille(-80, 560, 1.6, rot=-4, couleur="#51cf66", dessous=True))
    S.add(oeufs(220, 470, 1.4, nb=16, eclos=10))
    S.add(larve(250, 620, 0.5, rot=20), larve(150, 380, 0.45, rot=-140))
    S.add(larve(520, 520, 1.9, rot=-12))
    S.add(texte(400, 130, "On dirait un petit crocodile !", 42, "#343a40", contour="#fff"))
    S.cachette(120, 610)
    return S


def p03():
    """Plan moyen : sur la tige du rosier couverte de pucerons verts, la larve mange : miam !"""
    S = Scene()
    jardin_doux(S, 4)
    S.add(rose(560, 160, 1.6))
    S.add(tige_rosier(560, 820, 200, 1.2))
    S.add(feuille(560, 520, 0.4, rot=-30), feuille(560, 360, 0.36, rot=200))
    r = random.Random(3)
    for k in range(22):
        S.add(puceron(560 + r.uniform(-14, 14), r.uniform(230, 720), 0.55, rot=r.choice((-90, 90)) + r.uniform(-20, 20)))
    S.add(larve(470, 600, 1.3, rot=-70, mange=True))
    S.add(texte(250, 140, "Miam !", 70, "#343a40", contour="#fff"))
    S.cachette(680, 456)
    return S


def p04():
    """Gros plan : accrochée à une feuille, la larve est devenue une nymphe : chut… elle se transforme."""
    S = Scene()
    jardin_doux(S, 5)
    S.add(feuille(-60, 600, 1.5, rot=-12))
    S.add(nymphe(420, 470, 2.6, rot=-10))
    S.add(etiquette(420, 290, "la nymphe", 36, "#c47a1d"))
    S.add(texte(400, 130, "Chut… elle se transforme.", 42, "#343a40", contour="#fff"))
    S.cachette(690, 515)
    return S


def p05():
    """Gros plan : une coccinelle toute jaune, sans points, sort de la nymphe ; quelques heures plus tard, elle est rouge à points noirs."""
    S = Scene()
    jardin_doux(S, 6)
    S.add(feuille(-60, 560, 1.5, rot=-6))
    S.add(nymphe(170, 470, 1.4, rot=-10, vide=True))
    S.add(coccinelle_d(260, 560, 1.5, rot=70, pale=True, expr="content"))
    S.add(fleche(370, 520, 470, 520, "#495057", sw=6))
    S.add(coccinelle_d(590, 520, 1.5, rot=80, expr="content"))
    S.add(etiquette(250, 700, "Toute pâle !", 32, "#e67700"), etiquette(600, 700, "quelques heures plus tard", 28, "#c92a2a"))
    S.cachette(60, 600)
    return S


def p06():
    """Schéma : la coccinelle en vol, les élytres levées et les ailes déployées : élytres, ailes, antennes."""
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(coccinelle_d(400, 440, 2.3, vol=True))
    S.add(trait(310, 300, 180, 220, "#868e96", 3), etiquette(150, 200, "les élytres", 30, "#c92a2a"))
    S.add(trait(640, 560, 680, 660, "#868e96", 3), etiquette(680, 700, "les ailes", 30, "#495057"))
    S.add(trait(440, 240, 560, 150, "#868e96", 3), etiquette(600, 130, "les antennes", 30, "#495057"))
    S.cachette(740, 790)
    return S


def p07():
    """Plan moyen : dans le jardin, une enfant tend son doigt : la coccinelle ouvre ses élytres et s'envole."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f3f0ff")
    S.add(chemin("M 0 520 Q 200 470 400 510 T 800 500 L 800 560 L 0 560 Z", "#b2f2bb"))
    S.add(rect(0, 540, 800, 260, "#8ce99a"))
    herbes(S, 560, 790, 20, 3, "#40c057", 0.8)
    for x, c in ((80, "#ff6b6b"), (150, "#fcc419"), (690, "#cc5de8"), (740, "#ff8787")):
        S.add(fleur(x, 640, 1.2, c))
    px, py, t = 330, 780, 1.4
    S.add(personne(px, py, t, peau="brune", cheveux="noir", coiffure="couettes", habit="#4dabf7", expr="rire", bras="montre",
                   regard=(1, -1)))
    (_, _), (mx, my) = mains_personne(px, py, t, "montre")
    S.add(coccinelle_d(mx + 110, my - 100, 0.36, rot=40, vol=True))
    S.add(chemin(f"M {mx + 6} {my - 14} Q {mx + 30} {my - 80} {mx + 84} {my - 92}", stroke="#495057", sw=3, stroke_dasharray="8 8"))
    S.add(texte(560, 140, "Elle s'envole !", 56, "#c92a2a", contour="#fff"))
    return S


def p08():
    """Plan large : dans le potager, les coccinelles mangent les pucerons des rosiers ; le grand-père jardinier sourit."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(rect(0, 520, 800, 280, terrain("#8ce99a")))
    S.add(buisson(560, 640, 1.6, "#40c057", "#51cf66", baies="#f06595"))
    for x, y, r in ((500, 460, 20), (600, 440, -30), (640, 520, 60), (520, 560, -10)):
        S.add(coccinelle_d(x, y, 0.2, rot=r))
    for x, y in ((540, 470), (620, 470), (590, 540), (660, 560), (480, 520)):
        S.add(puceron(x, y, 0.26))
    S.add(personne(230, 760, 1.25, stature="ancien", peau="claire", cheveux="blanc", coiffure="courts", habit="#74b816", robe=False,
                   expr="rire", bras="hanches", regard=(1, -0.2), barbe="#e9ecef", nez="rond"))
    S.add(bulle(260, 230, 330, 90, "Merci, les coccinelles !", 32, pointe=(240, 330)))
    return S


def p09():
    """Plan moyen : un oiseau approche ; la coccinelle laisse couler un liquide jaune et amer : « Pouah ! », l'oiseau s'en va."""
    S = Scene()
    jardin_doux(S, 9)
    S.add(feuille(-60, 640, 1.5, rot=-10))
    S.add(coccinelle_d(330, 560, 1.6, rot=70, expr="sourire"))
    for x, y in ((280, 640), (390, 640), (300, 470)):
        S.add(ellipse(x, y, 8, 11, "#fcc419"))
    S.add(oiseau(620, 420, 1.3, "#ffa94d", "#fff4e6", expr="degoute", ailes="haut", flip=True, bec_ouvert=True))
    S.add(bulle(620, 160, 200, 90, "Pouah !", 44, pointe=(610, 260)))
    S.cachette(100, 680)
    return S


def p10():
    """Schéma : combien de points ? sept points, deux points, vingt-deux points (jaune), noire à points rouges."""
    S = Scene()
    fond(S, "#fff5f5")
    S.add(texte(400, 100, "Les points ne disent pas son âge !", 40, "#c92a2a"))
    cases = [(220, 300, dict(points=7), "7 points"), (580, 300, dict(points=2), "2 points"),
             (220, 590, dict(points=22, couleur="#fcc419"), "22 points"), (580, 590, dict(points=2, couleur=NOIR, couleur_points=ROUGE), "noire à points rouges")]
    for x, y, opt, nom in cases:
        S.add(disque(x, y, 120, "#ffffff", "#ffc9c9"))
        S.add(coccinelle_d(x, y, 1.5, expr="content", **opt))
        S.add(etiquette(x, y + 160, nom, 28, "#495057"))
    S.cachette(740, 790)
    return S


def p11():
    """Plan moyen : l'hiver, sous l'écorce d'un vieux tronc, les coccinelles dorment serrées les unes contre les autres."""
    S = Scene()
    ciel(S, "#bac8ff", "#f1f3f5")
    S.add(rect(0, 600, 800, 200, lineaire([(0, "#ffffff"), (1, "#dbe4ff")])))
    S.add(rect(250, 0, 300, 640, cylindre("#8d6e4f", 0.25, 0.75)))
    for k in range(9):
        S.add(trait(270 + k * 32, 0, 266 + k * 32, 620, "#5c4033", 4, opacity=0.5))
    S.add(chemin("M 240 610 Q 400 570 560 610 L 560 650 L 240 650 Z", "#fff"))
    S.add(ellipse(400, 360, 120, 150, "#5c4033"), ellipse(400, 360, 108, 138, "#c9a27a"))
    r = random.Random(11)
    for k in range(16):
        a, d = k * 2.4, 22 * math.sqrt(k)
        S.add(coccinelle_d(400 + math.cos(a) * d * 0.9, 360 + math.sin(a) * d * 1.1, 0.38, rot=r.uniform(-180, 180), expr="dort"))
    flocons(S, 40, graine=11)
    S.add(texte(400, 720, "Toutes ensemble pour l'hiver", 40, "#364fc7", contour="#fff"))
    S.cachette(90, 640)
    return S


def p12():
    """Schéma : le cycle de la coccinelle : l'œuf, la larve, la nymphe, la coccinelle."""
    S = Scene()
    fond(S, "#f4fce3")
    S.add(cycle(400, 420, 250, "#2b8a3e", nb=4, ecart=24))
    pos = [(400, 170), (650, 420), (400, 670), (150, 420)]
    noms = ("les œufs", "la larve", "la nymphe", "la coccinelle")
    S.add(disque(400, 170, 92, "#fff"), oeufs(400, 170, 1.4, nb=12))
    S.add(disque(650, 420, 92, "#fff"), larve(650, 420, 0.65, rot=90))
    S.add(disque(400, 670, 92, "#fff"), nymphe(404, 670, 0.9))
    S.add(disque(150, 420, 92, "#fff"), coccinelle_d(150, 424, 0.9, expr="content"))
    for (x, y), nom in zip(pos, noms):
        S.add(etiquette(x, y + 125, nom, 28, "#2b8a3e"))
    S.cachette(740, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("coccinelle-seule.svg", vignette),
    ("01-les-oeufs.svg", p01), ("02-la-larve.svg", p02), ("03-miam.svg", p03),
    ("04-la-nymphe.svg", p04), ("05-toute-pale.svg", p05), ("06-les-ailes.svg", p06),
    ("07-elle-s-envole.svg", p07), ("08-le-jardinier.svg", p08), ("09-pouah.svg", p09),
    ("10-les-points.svg", p10), ("11-l-hiver.svg", p11), ("12-le-cycle.svg", p12),
]
