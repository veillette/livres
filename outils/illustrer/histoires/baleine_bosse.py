"""La baleine qui chante — la baleine à bosse.

La baleine à bosse est un mammifère : elle remonte respirer par les deux
évents du sommet de sa tête (le souffle). Elle plonge en montrant sa queue,
dont le dessous est différent pour chaque baleine. Elle n'a pas de dents
mais des fanons, qui filtrent le krill ; en groupe, elle l'enferme dans un
filet de bulles. L'été elle mange dans les mers froides, l'hiver elle voyage
vers les mers chaudes où naît le baleineau, qui boit le lait de sa mère. Les
mâles chantent de longues chansons. Elle mesure environ 15 m, comme un
autobus, et ses nageoires pectorales sont très longues.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, fleche_courbe
from fantastique import bulles_eau

ID = "baleine-bosse"
DOS = "#3b5b7a"
CLAIR = "#e7f5ff"


# --- Personnages ------------------------------------------------------------

def baleine(x, y, s=1.0, flip=False, rot=0, expr="sourire", couleur=DOS, gueule=False, chante=False):
    """Baleine à bosse de profil, tête à droite ; (x, y) = milieu du corps.
    Longueur d'environ 680 à l'échelle 1. `gueule` : bouche grande ouverte
    pleine d'eau et de krill."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    m = []
    # queue
    m.append(chemin("M -270 -8 Q -330 -30 -380 -100 Q -350 -40 -410 -10 Q -350 20 -380 90 Q -330 30 -270 10 Z", fonce))
    # nageoire pectorale (derrière)
    m.append(chemin("M 120 30 Q 40 120 -40 170 Q -10 140 30 110 Q 70 70 100 30 Z", _assombrir(couleur, 0.7)))
    # corps
    if gueule:
        corps = ("M 310 -20 Q 290 -66 220 -74 Q 60 -94 -80 -66 Q -200 -40 -280 -8 L -280 8 "
                 "Q -180 40 -40 70 Q 120 150 250 120 Q 330 90 310 -20 Z")
    else:
        corps = ("M 310 -14 Q 296 -64 220 -72 Q 60 -94 -80 -66 Q -200 -40 -280 -8 L -280 8 "
                 "Q -180 30 -40 52 Q 120 70 250 40 Q 312 20 310 -14 Z")
    m.append(chemin(corps, couleur))
    # ventre clair et sillons de la gorge
    cid = uid("bl")
    m.append(el("clipPath", chemin(corps, "#000"), id=cid))
    ventre = []
    if gueule:
        ventre.append(ellipse(150, 90, 170, 60, "#ffc9c9"))
        for k in range(7):
            ventre.append(chemin(f"M {290 - k * 6} {20 + k * 14} Q 160 {60 + k * 14} 20 {50 + k * 6}", stroke="#faa2c1", sw=4))
        for k in range(14):
            ventre.append(chemin(f"M {120 + k * 12} {70 + (k % 3) * 20} q 6 -4 10 0 q -4 6 -10 0", stroke="#e8590c", sw=3))
    else:
        ventre.append(chemin("M 310 0 Q 200 30 0 50 L 0 120 L 320 120 Z", CLAIR))
        for k in range(5):
            ventre.append(chemin(f"M {300 - k * 4} {8 + k * 8} Q 180 {34 + k * 8} 60 {44 + k * 4}", stroke="#a5d8ff", sw=3))
    m.append(g(ventre, clip_path=f"url(#{cid})"))
    # bosse et petite nageoire dorsale
    m.append(chemin("M -110 -60 Q -96 -96 -70 -70 Z", fonce))
    # tubercules sur la tête
    for px, py in [(250, -58), (270, -44), (230, -66), (286, -30)]:
        m.append(cercle(px, py, 5, fonce))
    if gueule:
        for k in range(10):
            m.append(trait(300 - k * 18, -14 - k * 1.5, 300 - k * 18, 22 + (k % 2) * 4, "#495057", 3))
    # évents
    m.append(ellipse(196, -76, 10, 4, "#1b2a3a"))
    # nageoire pectorale (devant)
    m.append(chemin("M 150 40 Q 80 150 -30 200 Q -10 176 10 168 Q 6 156 34 146 Q 30 132 60 120 Q 90 80 120 36 Z", "#dee2e6"))
    # œil et bouche
    oy = -10 if not gueule else -22
    m.append(cercle(206, oy, 11, "#fff"))
    if ys in ("heureux", "fermes"):
        m.append(oeil(206, oy, ys, (0, 0), taille=0.9))
    else:
        m.append(cercle(209, oy, 6.5, ENCRE) + cercle(211, oy - 2.5, 2.2, "#fff"))
    m.append(joue(230, oy + 20, 1.0))
    if not gueule:
        if chante or bs in ("o", "ouverte"):
            m.append(ellipse(300, 6, 12, 8, "#c92a2a"))
        m.append(chemin("M 312 2 Q 260 26 196 16", stroke="#1b2a3a", sw=4))
    return place(m, x, y, s, flip=flip, rot=rot)


def queue_levee(x, y, s=1.0, motif=1, couleur=DOS):
    """La queue (nageoire caudale) dressée hors de l'eau, vue de derrière ;
    le dessous montre des taches blanches propres à chaque baleine.
    (x, y) = où la queue sort de l'eau."""
    r = random.Random(motif)
    forme = "M -20 0 Q -16 -80 -10 -130 Q -120 -150 -200 -230 Q -100 -220 -2 -170 Q 0 -160 2 -170 Q 100 -220 200 -230 Q 120 -150 10 -130 Q 16 -80 20 0 Z"
    cid = uid("q")
    m = [chemin(forme, couleur), el("clipPath", chemin(forme, "#000"), id=cid)]
    taches = [ellipse(0, -170, 120, 30, "#f1f3f5")]
    for _ in range(6):
        taches.append(ellipse(r.uniform(-160, 160), r.uniform(-200, -150), r.uniform(10, 30), r.uniform(6, 12), couleur))
    m.append(g(taches, clip_path=f"url(#{cid})"))
    for k in range(6):
        m.append(cercle(r.uniform(-180, 180), -150 + r.uniform(-60, 0), 4, "#a5d8ff", opacity=0.9))
    return place(m, x, y, s)


def souffle(x, y, s=1.0):
    """Le souffle en V de la baleine à bosse ; (x, y) = évents."""
    m = []
    for sgn in (-1, 1):
        for k in range(5):
            m.append(cercle(sgn * (10 + k * 14), -30 - k * 40, 18 + k * 7, "#ffffff", opacity=0.85 - k * 0.1))
    return place(m, x, y, s)


def krill(x, y, s=1.0, rot=0):
    m = [chemin("M -16 0 Q 0 -8 16 -2 Q 6 6 -16 0 Z", "#ff8787"),
         chemin("M -16 0 L -24 -6 M -16 0 L -24 6", stroke="#ff8787", sw=2),
         trait(14, -2, 28, -12, "#ff8787", 1.5), trait(14, -2, 30, -4, "#ff8787", 1.5),
         cercle(12, -3, 1.8, ENCRE)]
    for k in range(4):
        m.append(trait(-8 + k * 6, 2, -10 + k * 6, 8, "#ffa8a8", 1.5))
    return place(m, x, y, s, rot=rot)


def nuee_krill(cx, cy, rx, ry, nb=40, graine=1, s=1.0):
    r = random.Random(graine)
    m = []
    for _ in range(nb):
        a = r.uniform(0, 2 * math.pi)
        d = math.sqrt(r.uniform(0, 1))
        m.append(krill(cx + math.cos(a) * rx * d, cy + math.sin(a) * ry * d, s * r.uniform(0.7, 1.1), r.uniform(-30, 30)))
    return g(m)


def mer(S, y=260, haut="#a5d8ff", bas="#e7f5ff", froide=False):
    """Ciel et mer, vue coupée : surface en `y`, l'eau dessous."""
    S.add(rect(0, 0, 800, y, S.degrade([haut, bas])))
    S.add(rect(0, y, 800, 800 - y, S.degrade(["#339af0" if not froide else "#1c7ed6", "#0b3d6b"])))
    for k in range(4):
        x0 = 60 + k * 200
        S.add(poly([(x0, y), (x0 + 60, y), (x0 + 140, 800), (x0 + 30, 800)], "#ffffff", opacity=0.05))
    S.add(chemin(f"M 0 {y} q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0",
                 stroke="#d0ebff", sw=6))


def surface(S, y=470, haut="#74c0fc", bas="#e7f5ff", nuit_=False):
    """Vue au ras de l'eau : ciel en haut, mer à partir de y."""
    if nuit_:
        nuit(S)
    else:
        S.add(rect(0, 0, 800, y, S.degrade([haut, bas])))
    S.add(rect(0, y, 800, 800 - y, S.degrade(["#339af0", "#1864ab"])))
    for k in range(7):
        S.add(chemin(f"M {k * 120 + 20} {y + 40 + (k % 3) * 70} q 20 -10 40 0", stroke="#a5d8ff", sw=5))


def sous_l_eau_couvre(S, y):
    """Voile d'eau devant ce qui est sous la surface."""
    S.add(rect(0, y, 800, 800 - y, "#1864ab", opacity=0.35))
    S.add(chemin(f"M 0 {y} q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0",
                 stroke="#d0ebff", sw=6))


def bateau(x, y, s=1.0):
    m = [chemin("M -90 0 L 90 0 L 70 34 L -70 34 Z", "#fa5252"), rect(-40, -40, 70, 40, "#f8f9fa", rx=6),
         rect(-30, -32, 18, 16, "#74c0fc", rx=3), rect(0, -32, 18, 16, "#74c0fc", rx=3)]
    return place(m, x, y, s)


def autobus(x, y, s=1.0):
    m = [rect(-300, -150, 600, 130, "#fcc419", rx=20), rect(-300, -60, 600, 14, "#e67700")]
    for k in range(7):
        m.append(rect(-270 + k * 80, -130, 60, 50, "#a5d8ff", rx=6))
    m += [cercle(-190, -16, 34, ENCRE), cercle(190, -16, 34, ENCRE), cercle(-190, -16, 14, "#adb5bd"), cercle(190, -16, 14, "#adb5bd")]
    return place(m, x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    mer(S, 300, froide=False)
    S.add(nuee_krill(640, 640, 120, 60, 18, 3, 0.9))
    S.add(baleine(410, 540, 0.9, expr="content"))
    S.add(baleine(230, 690, 0.36, expr="rire", couleur="#5c7a99"))
    S.add(bulles_eau(700, 500, 1.4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(baleine(212, 120, 0.46, expr="content"))
    return S


def p01():
    S = Scene()
    mer(S, 200)
    S.add(nuage(160, 90, 0.8), nuage(600, 70, 0.6))
    S.add(baleine(420, 480, 0.9, expr="sourire"))
    for x, y in [(120, 720), (180, 760), (90, 680)]:
        S.add(poisson_simple(x, y, 0.7))
    S.add(bulles_eau(560, 340, 1.0))
    return S


def p02():
    S = Scene()
    surface(S, 470)
    S.add(nuage(150, 110, 0.7))
    S.add(baleine(370, 520, 0.8, expr="content"))
    sous_l_eau_couvre(S, 470)
    S.add(souffle(530, 455, 1.4))
    S.add(texte(250, 230, "Pffffff !", 70, "#1864ab", contour="#fff"))
    return S


def p03():
    S = Scene()
    surface(S, 520)
    S.add(soleil(660, 110, 50))
    S.add(queue_levee(330, 540, 1.3, motif=2))
    S.add(g([cercle(330 + k * 40 - 100, 540 + (k % 2) * 6, 10, "#ffffff", opacity=0.8) for k in range(6)]))
    S.add(place(queue_levee(0, 0, 1.0, motif=7), 640, 600, 0.45))
    S.add(texte(620, 380, "chacune la sienne !", 30, "#1864ab", contour="#fff"))
    return S


def p04():
    S = Scene()
    mer(S, 120, froide=True)
    S.add(poly([(80, 120), (140, 60), (220, 120)], "#f8f9fa"), poly([(560, 120), (640, 40), (740, 120)], "#e7f5ff"))
    S.add(nuee_krill(560, 480, 220, 170, 60, 4, 1.2))
    S.add(baleine(300, 470, 0.9, gueule=True, expr="miam"))
    S.add(loupe(640, 650, 100, [rect(530, 540, 220, 220, "#1864ab"), krill(640, 650, 3.2)], fond="#1864ab", rot=40))
    S.add(etiquette(640, 520, "le krill", 34, "#c92a2a"))
    return S


def p05():
    S = Scene()
    mer(S, 160, froide=True)
    r = random.Random(5)
    for k in range(70):
        a = k * 0.35
        rr = 240 - k * 1.2
        S.add(cercle(400 + math.cos(a) * rr * 0.9, 470 + math.sin(a) * rr * 0.5 - k * 3, r.uniform(5, 13), "none", stroke="#ffffff", stroke_width=3, opacity=0.8))
    for x, y in [(380, 420), (440, 470), (360, 500), (420, 520), (460, 410), (330, 450)]:
        S.add(poisson_simple(x, y, 0.6, flip=x < 400))
    S.add(baleine(150, 640, 0.42, rot=-70, expr="concentre"))
    S.add(baleine(650, 650, 0.42, rot=-110, flip=True, expr="concentre"))
    return S


def p06():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#1c7ed6", "#74c0fc"], vertical=False)))
    S.add(poly([(40, 120), (110, 40), (190, 120)], "#f8f9fa"), poly([(90, 220), (150, 170), (220, 220)], "#e7f5ff"))
    S.add(texte(130, 300, "mers froides", 34, "#ffffff", contour="#1864ab"))
    S.add(ellipse(650, 640, 110, 40, "#f4d58d"))
    S.add(place([trait(0, 0, 10, -120, "#8d5524", 10), ellipse(10, -126, 60, 16, "#40c057", rot=-20), ellipse(10, -126, 60, 16, "#51cf66", rot=30)], 640, 630))
    S.add(soleil(700, 470, 40, rayons=True))
    S.add(texte(640, 740, "mers chaudes", 34, "#ffffff", contour="#1864ab"))
    S.add(fleche_courbe("M 220 300 Q 300 600 520 620", (520, 620), 5, "#ffffff", 8, 26, stroke_dasharray="20 14"))
    S.add(baleine(320, 470, 0.32, rot=50, expr="content"))
    S.add(baleine(400, 560, 0.2, rot=40, couleur="#5c7a99"))
    return S


def p07():
    S = Scene()
    mer(S, 160, haut="#74c0fc", bas="#fff9db")
    S.add(baleine(400, 400, 0.86, expr="content"))
    S.add(baleine(470, 620, 0.38, expr="miam", couleur="#5c7a99"))
    S.add(coeur(640, 300, 1.2, "#ff8787"))
    return S


def p08():
    S = Scene()
    mer(S, 120)
    S.add(baleine(330, 420, 0.85, expr="chante", chante=True))
    S.add(notes(620, 380, 1.4, "#ffffff"), notes(700, 260, 1.0, "#d0ebff"), notes(120, 220, 1.0, "#d0ebff"))
    from sciences import ondes
    S.add(ondes(640, 420, 40, 4, 40, 0, 80, "#ffffff", 5))
    S.add(baleine(660, 700, 0.28, flip=True, expr="surpris"))
    return S


def p09():
    S = Scene()
    surface(S, 560)
    S.add(nuage(150, 110, 0.7), nuage(620, 80, 0.5))
    S.add(baleine(420, 380, 0.85, rot=-62, expr="rire"))
    sous_l_eau_couvre(S, 560)
    for k in range(9):
        a = math.radians(-160 + k * 18)
        S.add(goutte(420 + math.cos(a) * 280, 560 + math.sin(a) * 120, 1.6, "#d0ebff"))
    S.add(texte(650, 160, "Splash !", 70, "#1864ab", contour="#fff", rot=8))
    return S


def p10():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(autobus(400, 330, 1.05))
    S.add(baleine(400, 600, 0.9, expr="content"))
    from sciences import enfant
    S.add(enfant(730, 770, 0.6, expr="bouche_bee", habit="#fa5252", jambes="#364fc7"))
    S.add(texte(400, 110, "15 mètres !", 60, "#1864ab", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("baleine-seule.svg", vignette),
    ("01-dans-l-ocean.svg", p01), ("02-le-souffle.svg", p02), ("03-la-queue.svg", p03),
    ("04-le-krill.svg", p04), ("05-le-filet-de-bulles.svg", p05), ("06-le-voyage.svg", p06),
    ("07-le-baleineau.svg", p07), ("08-le-chant.svg", p08), ("09-le-saut.svg", p09),
    ("10-grande-comme-un-bus.svg", p10),
]
