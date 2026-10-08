"""La ruche des abeilles — butiner, polliniser, faire le miel.

Une seule reine pond (jusqu'à plus de mille œufs par jour), les ouvrières
sont ses filles. L'abeille aspire le nectar avec sa langue et rapporte le
pollen en pelotes sur ses pattes arrière. La danse en huit indique la
direction des fleurs. Le nectar séché par le battement des ailes devient du
miel ; les alvéoles hexagonales sont fermées par un opercule de cire. L'hiver,
les abeilles se serrent en grappe autour de la reine et frissonnent.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import enfant, fleche, fleche_courbe
from objets import pomme

ID = "abeille-miel"
CIRE = "#ffe8a3"
MIEL = "#f59f00"


# --- Dessins propres au livre ----------------------------------------------

def reine(x, y, s=1.0, **k):
    """La reine : plus longue, avec une pastille de couleur sur le dos."""
    return abeille(x, y, s * 1.15, abdomen=1.55, marque="#4dabf7", **k)


def alveoles(S, x0=-40, y0=-40, r=46, cols=12, lignes=14, contenu=None, graine=1, fond_c="#f4c15d"):
    """Rayon de cire : grille d'hexagones (pointe en haut). `contenu(i, j, x, y)`
    renvoie ce qu'il y a dans une alvéole : "miel", "ferme", "oeuf", "larve",
    "pollen" ou None (vide)."""
    S.add(rect(0, 0, S.w, S.h, fond_c))
    w = r * math.sqrt(3)
    for j in range(lignes):
        for i in range(cols):
            cx = x0 + i * w + (w / 2 if j % 2 else 0)
            cy = y0 + j * r * 1.5
            pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
            S.add(poly(pts, CIRE, stroke="#e8a33d", stroke_width=6))
            quoi = contenu(i, j, cx, cy) if contenu else None
            pi = [(cx + (r - 9) * math.cos(math.radians(a)), cy + (r - 9) * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
            if quoi == "miel":
                S.add(poly(pi, MIEL, opacity=0.85))
                S.add(ellipse(cx - 10, cy - 12, 8, 5, "#fff3bf", opacity=0.7))
            elif quoi == "ferme":
                S.add(poly(pi, "#fff3bf"))
                S.add(poly(pi, "none", stroke="#f6d365", stroke_width=3))
            elif quoi == "oeuf":
                S.add(poly(pi, "#fff9db"))
                S.add(ellipse(cx, cy, 4, 10, "#ffffff", stroke="#e9ecef", stroke_width=1.5))
            elif quoi == "larve":
                S.add(poly(pi, "#fff9db"))
                S.add(chemin(f"M {n(cx - 14)} {n(cy + 4)} A 14 12 0 1 1 {n(cx + 12)} {n(cy + 8)}", stroke="#f8f9fa", sw=12))
                S.add(chemin(f"M {n(cx - 14)} {n(cy + 4)} A 14 12 0 1 1 {n(cx + 12)} {n(cy + 8)}", stroke="#e9ecef", sw=2))
            elif quoi == "pollen":
                S.add(poly(pi, "#ff922b"))
                S.add(cercle(cx - 8, cy - 6, 5, "#ffc078"))


def ruche(x, y, s=1.0, couleur="#e9c46a", toit="#c92a2a"):
    """Ruche en bois (caisses empilées) sur pieds ; (x, y) = au sol, au milieu."""
    fonce = _assombrir(couleur, 0.85)
    m = [rect(-90, -40, 14, 40, "#7c4a1e"), rect(76, -40, 14, 40, "#7c4a1e"),
         rect(-110, -60, 220, 24, "#8d5524", rx=4),
         rect(-100, -190, 200, 130, couleur, rx=6), rect(-100, -130, 200, 6, fonce),
         rect(-100, -280, 200, 90, eclaircir(couleur, 0.15), rx=6),
         poly([(-120, -280), (120, -280), (110, -310), (-110, -310)], toit),
         rect(-36, -76, 72, 14, "#495057", rx=7)]
    return place(m, x, y, s)


def fleur_pommier(x, y, s=1.0, rot=0):
    m = []
    for k in range(5):
        a = math.radians(-90 + k * 72)
        m.append(ellipse(math.cos(a) * 28, math.sin(a) * 28, 26, 22, "#fff0f6", rot=k * 72))
        m.append(ellipse(math.cos(a) * 22, math.sin(a) * 22, 12, 9, "#fcc2d7", rot=k * 72, opacity=0.7))
    m.append(cercle(0, 0, 14, "#ffe066"))
    for k in range(10):
        a = math.radians(k * 36)
        m.append(cercle(math.cos(a) * 16, math.sin(a) * 16, 3, "#f59f00"))
    return place(m, x, y, s, rot=rot)


def branche(x0, y0, x1, y1, couleur="#7c4a1e", ep=18):
    return chemin(f"M {x0} {y0} Q {(x0 + x1) / 2} {(y0 + y1) / 2 - 40} {x1} {y1}", stroke=couleur, sw=ep)


def feuille(x, y, s=1.0, rot=0, couleur="#51cf66"):
    return place([chemin("M 0 0 Q 30 -26 64 0 Q 30 26 0 0 Z", couleur), trait(4, 0, 58, 0, "#2f9e44", 2)], x, y, s, rot=rot)


def pre_fleuri(S, y=600, graine=2):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(chemin(f"M 0 {y - 40} Q 200 {y - 90} 400 {y - 50} T 800 {y - 60} L 800 {y + 10} L 0 {y + 10} Z", "#b2f2bb"))
    S.add(rect(0, y, 800, 800 - y, "#8ce99a"))
    r = random.Random(graine)
    for _ in range(14):
        S.add(fleur(r.uniform(20, 780), r.uniform(y + 40, 790), r.uniform(0.6, 0.9),
                    r.choice(["#ff8787", "#ffd43b", "#cc5de8", "#ffffff", "#74c0fc"]), tige=r.uniform(30, 60)))


def vol(x, y, s=1.0, rot=0, flip=False, **k):
    """Abeille en vol avec un petit trait de mouvement."""
    return abeille(x, y, s, rot=rot, flip=flip, **k) + mouvement(x + (50 if flip else -50) * s, y, 0.5 * s, "#868e96", rot=180 if flip else 0)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    pre_fleuri(S, 620)
    S.add(ruche(560, 720, 1.25))
    S.add(fleur(170, 780, 1.6, "#ff8787", tige=170), fleur(280, 790, 1.2, "#ffd43b", tige=120))
    S.add(abeille(330, 470, 2.6, expr="rire", regard=(1, -0.3), pelotes=True))
    S.add(vol(640, 330, 0.9, flip=True), vol(720, 420, 0.7, flip=True), vol(140, 420, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fleur(120, 262, 1.0, "#ff8787", tige=80))
    S.add(abeille(230, 130, 1.6, expr="content", pelotes=True))
    S.add(vol(340, 70, 0.55, flip=True))
    return S


def p01():
    S = Scene()
    pre_fleuri(S, 600)
    S.add(arbre(120, 620, 1.1))
    S.add(ruche(470, 700, 1.4))
    r = random.Random(4)
    for _ in range(9):
        S.add(vol(r.uniform(260, 760), r.uniform(150, 380), r.uniform(0.5, 0.8), flip=r.random() < 0.5))
    S.add(texte(250, 250, "Bzzz !", 64, "#f08c00", contour="#fff", rot=-8))
    return S


def p02():
    S = Scene()

    def contenu(i, j, x, y):
        if 250 < x < 560 and 200 < y < 600:
            return None if (i + j) % 5 == 0 else "oeuf"
        return "miel" if (i * 3 + j) % 4 == 0 else ("pollen" if (i + 2 * j) % 7 == 0 else None)
    alveoles(S, contenu=contenu)
    S.add(reine(400, 420, 2.4, expr="content", regard=(1, 0.5)))
    S.add(abeille(150, 230, 1.3, regard=(1, 0.5)), abeille(650, 640, 1.3, flip=True, regard=(1, 0)),
          abeille(660, 230, 1.2, flip=True, regard=(1, 0.5)))
    S.cachette(70, 720, "air")
    return S


def p03():
    S = Scene()

    def contenu(i, j, x, y):
        return "larve" if (i + j) % 3 else ("ferme" if i % 2 else "oeuf")
    alveoles(S, contenu=contenu, graine=2)
    S.add(abeille(300, 300, 1.8, expr="sourire", regard=(1, 1), trompe=True))
    S.add(abeille(560, 520, 1.8, flip=True, expr="concentre", regard=(1, 1)))
    S.add(place([rect(-60, -10, 120, 20, CIRE, rx=6), rect(-50, -30, 40, 20, CIRE, rx=6)], 560, 620))
    S.add(abeille(200, 620, 1.3, regard=(1, 0)))
    S.cachette(80, 720, "air")
    return S


def p04():
    S = Scene()
    pre_fleuri(S, 660, graine=4)
    S.add(chemin("M 380 800 Q 370 700 380 560", stroke="#2f9e44", sw=20))
    S.add(feuille(380, 700, 2.0, -30), feuille(380, 740, 1.8, 200))
    for k in range(10):
        a = math.radians(k * 36)
        S.add(ellipse(380 + math.cos(a) * 120, 470 + math.sin(a) * 70, 80, 40, "#ff8787", rot=k * 36 * 0.6))
    S.add(ellipse(380, 470, 120, 70, "#fa5252", opacity=0.3))
    S.add(ellipse(380, 470, 80, 46, "#ffd43b"))
    r = random.Random(5)
    for _ in range(30):
        a = r.uniform(0, 2 * math.pi)
        d = math.sqrt(r.uniform(0, 1))
        S.add(cercle(380 + math.cos(a) * d * 70, 470 + math.sin(a) * d * 40, r.uniform(3, 5), "#f08c00"))
    S.add(abeille(360, 380, 2.4, expr="miam", regard=(0.5, 1), pelotes=True, trompe=True))
    S.add(etiquette(640, 240, "pollen", 40, "#e67700"), fleche(610, 260, 380, 440, "#e67700", 5, 18))
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#f3f0ff")
    S.add(branche(-20, 300, 520, 360), branche(300, 340, 820, 220))
    for x, y, rot in [(80, 230, 10), (210, 320, -30), (360, 300, 40), (520, 330, 0), (650, 260, 20), (760, 210, -10)]:
        S.add(feuille(x, y, 1.2, rot))
    S.add(fleur_pommier(220, 400, 1.6), fleur_pommier(470, 300, 1.4, 30), fleur_pommier(700, 250, 1.5, 10))
    S.add(abeille(300, 330, 1.4, pelotes=True, regard=(1, 0.6)))
    S.add(fleche_courbe("M 350 340 Q 400 240 450 270", (450, 270), 30, "#e67700", 5, 18))
    S.add(fleche(400, 520, 400, 610, "#495057", 8, 24))
    S.add(branche(150, 720, 650, 700))
    S.add(pomme(400, 690, 2.4))
    S.add(feuille(430, 620, 1.0, -40))
    S.cachette(480, 730, "air")
    return S


def p06():
    S = Scene()

    def contenu(i, j, x, y):
        return "miel" if (i + j) % 3 == 0 else None
    alveoles(S, contenu=contenu, graine=3)
    huit = "M 400 400 C 480 300 560 320 560 400 C 560 480 480 500 400 400 C 320 300 240 320 240 400 C 240 480 320 500 400 400"
    S.add(chemin(huit, stroke="#ffffff", sw=10, stroke_dasharray="22 16", opacity=0.9))
    S.add(abeille(400, 400, 2.0, expr="rire", rot=-45, regard=(1, 0)))
    S.add(mouvement(330, 450, 0.7, ENCRE, rot=45))
    for x, y, flip in [(140, 220, False), (660, 220, True), (130, 600, False), (670, 620, True), (400, 700, False)]:
        S.add(abeille(x, y, 1.2, flip=flip, expr="surpris" if y < 400 else "sourire", regard=(1, 0)))
    S.cachette(70, 440, "air")
    return S


def p07():
    S = Scene()

    def contenu(i, j, x, y):
        if y < 380:
            return "ferme"
        return "miel"
    alveoles(S, contenu=contenu, graine=5)
    for x, y in [(250, 520), (550, 560)]:
        S.add(abeille(x, y, 1.7, expr="concentre", regard=(1, 0)))
        S.add(mouvement(x - 10, y - 90, 0.8, "#ffffff", rot=-90))
        S.add(mouvement(x + 10, y - 90, 0.8, "#ffffff", rot=-90))
    S.add(abeille(420, 230, 1.5, flip=True, expr="content", regard=(1, 0.5)))
    S.cachette(80, 170, "air")
    return S


def p08():
    S = Scene()
    pre_fleuri(S, 620, graine=6)
    S.add(ruche(600, 720, 1.3))
    for dx in (-30, 10, 40):
        S.add(abeille(600 + dx, 600, 0.5, flip=True, ailes=False))
    S.add(vol(420, 380, 0.8))
    S.add(enfant(220, 760, 1.6, expr="sourire", bras="bas", regard=(1, -0.5), habit="#ffa94d", jambes="#364fc7"))
    S.add(texte(230, 260, "Je reste calme.", 40, "#e8590c", contour="#fff"))
    return S


def p09():
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#a5d8ff"))
    flocons(S, 50, 4, (0, 0, 800, 800))
    S.add(rect(0, 640, 800, 160, "#ffffff"))
    S.add(rect(140, 120, 520, 560, "#8d5524", rx=20))
    S.add(rect(170, 150, 460, 500, "#f4c15d", rx=10))
    for k in range(5):
        S.add(rect(200 + k * 90, 170, 60, 460, CIRE, rx=8))
        S.add(rect(208 + k * 90, 180, 44, 200, MIEL, rx=6, opacity=0.8))
    S.add(ellipse(400, 470, 170, 130, "#e8a33d"))
    r = random.Random(7)
    for _ in range(40):
        a = r.uniform(0, 2 * math.pi)
        d = math.sqrt(r.uniform(0, 1))
        S.add(abeille(400 + math.cos(a) * d * 150, 470 + math.sin(a) * d * 110, 0.55, flip=r.random() < 0.5,
                      ailes=False, expr="dort"))
    S.add(reine(400, 470, 0.9, expr="dort"))
    S.add(rect(140, 600, 520, 90, "#8d5524", rx=12), rect(360, 640, 80, 16, "#495057", rx=8))
    S.add(texte(400, 90, "Brrr…", 56, "#1971c2", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(rect(0, 560, 800, 240, "#e8c39e"))
    S.add(rect(0, 560, 800, 18, "#d9a066"))
    S.add(enfant(250, 740, 1.7, expr="rire", bras="porte", regard=(1, 0), habit="#69db7c", jambes="#e8590c", coiffure="queue",
                 objet=pot_fleurs_(0, -40)))
    for x, c in [(520, "#cc5de8"), (620, "#ff8787"), (720, "#ffd43b")]:
        S.add(rect(x - 40, 650, 80, 90, "#e8590c", rx=8))
        S.add(fleur(x, 650, 1.3, c, tige=110))
    S.add(vol(560, 380, 0.9, flip=True), vol(680, 300, 0.8, flip=True), abeille(620, 520, 0.9, flip=True, pelotes=True))
    S.add(texte(560, 200, "Merci !", 70, "#f08c00", contour="#fff", rot=-6))
    return S


def pot_fleurs_(x, y):
    return place([rect(-34, -10, 68, 60, "#e8590c", rx=8), fleur(-10, -10, 0.8, "#74c0fc", tige=50), fleur(14, -10, 0.7, "#ffd43b", tige=40)], x, y)


IMAGES = [
    ("couverture.svg", couverture), ("abeille-seule.svg", vignette),
    ("01-la-ruche.svg", p01), ("02-la-reine.svg", p02), ("03-les-ouvrieres.svg", p03),
    ("04-butiner.svg", p04), ("05-la-pomme.svg", p05), ("06-la-danse.svg", p06),
    ("07-le-miel.svg", p07), ("08-les-gardiennes.svg", p08), ("09-l-hiver.svg", p09),
    ("10-planter-des-fleurs.svg", p10),
]
