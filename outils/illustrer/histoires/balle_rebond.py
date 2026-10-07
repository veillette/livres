"""Boing ! fait la balle — rebonds, ressorts et élasticité.

Une balle élastique s'écrase au contact du sol puis reprend sa forme en
poussant sur le sol : elle rebondit. La pâte à modeler, elle, reste écrasée.
Une balle ne remonte jamais plus haut que la hauteur d'où on l'a lâchée :
à chaque choc, un peu d'élan part en bruit et en chaleur, et les rebonds
diminuent. Sur un sol mou (sable), le sol s'écrase à la place de la balle.
"""
from base import *
from objets import *
from sciences import fleche

ID = "balle-rebond"
ROUGE, JAUNE, BLEU = "#fa5252", "#ffd43b", "#4dabf7"


def pirouette(x, y, s=1.0, **k):
    return perso("lapin", x, y, s, **{**dict(habit="#cc5de8", acc=("noeud",), couleur_acc="#ffd43b"), **k})


def chiot(x, y, s=0.9, **k):
    return perso("chien", x, y, s, **{**dict(habit="#20c997", tache=True), **k})


def souris(x, y, s=0.6, **k):
    return perso("souris", x, y, s, **{**dict(habit="#ff922b"), **k})


def maman(x, y, s=1.2, **k):
    return perso("lapin", x, y, s, **{**dict(habit="#74c0fc", acc=("tablier",)), **k})


# ---------------------------------------------------------------------------
# Balles et ressorts
# ---------------------------------------------------------------------------

def balle(x, y, r=34, couleur=ROUGE, ecrase=0.0):
    """Balle rebondissante posée sur le sol en y (ecrase : 0 = ronde, 0,4 = très écrasée)."""
    rx, ry = r * (1 + ecrase), r * (1 - ecrase)
    return g([ellipse(x, y - ry, rx, ry, couleur), ellipse(x - rx * 0.35, y - ry * 1.4, rx * 0.25, ry * 0.18, "#fff", opacity=0.6),
              chemin(f"M {n(x - rx)} {n(y - ry)} Q {n(x)} {n(y - ry * 0.5)} {n(x + rx)} {n(y - ry)}", stroke="#fff", sw=4, opacity=0.5)])


def balle_air(x, y, r=34, couleur=ROUGE):
    """Balle en l'air, centrée en (x, y)."""
    return balle(x, y + r, r, couleur)


def mousse(x, y, r=34):
    """Balle en mousse jaune, centrée en (x, y)."""
    m = [cercle(x, y, r, JAUNE)]
    for dx, dy in ((-12, -10), (10, -16), (14, 8), (-8, 12), (0, -2), (-18, 4)):
        m.append(cercle(x + dx * r / 34, y + dy * r / 34, 2.5, "#f59f00"))
    return g(m)


def pate(x, y, s=1.0, ecrasee=False):
    """Boule de pâte à modeler bleue posée sur le sol en y."""
    if ecrasee:
        return place(chemin("M -60 0 Q -62 -22 -30 -24 Q -10 -34 14 -26 Q 56 -26 60 0 Z", BLEU, stroke="#1c7ed6", sw=3), x, y, s)
    return place([cercle(0, -32, 32, BLEU), ellipse(-10, -44, 9, 6, "#fff", opacity=0.5)], x, y, s)


def trajectoire(d, couleur=ENCRE):
    return chemin(d, stroke=couleur, sw=4, stroke_dasharray="2 12", opacity=0.6)


def bonds(x0, y_sol, hauteurs, pas):
    """Pointillés d'une balle qui rebondit vers la droite : un arc par hauteur."""
    d, x = f"M {x0} {y_sol}", x0
    for h, p in zip(hauteurs, pas):
        d += f" Q {n(x + p / 2)} {n(y_sol - 2 * h)} {n(x + p)} {y_sol}"
        x += p
    return trajectoire(d)


def ressort(x, y, h=120, w=50, spires=7, couleur="#868e96"):
    """Ressort vertical posé en (x, y), hauteur h."""
    d = f"M {x} {y}"
    for k in range(spires * 2):
        d += f" L {n(x + (w / 2 if k % 2 == 0 else -w / 2))} {n(y - (k + 0.5) * h / (spires * 2))}"
    d += f" L {x} {y - h}"
    return g([chemin(d, stroke=couleur, sw=6), rect(x - w / 2 - 6, y - 6, w + 12, 10, "#495057", rx=4),
              rect(x - w / 2 - 6, y - h - 4, w + 12, 10, "#495057", rx=4)])


def trampoline(x, y, w=420, creux=0):
    """Trampoline vu de face ; (x, y) = sol au centre."""
    haut = y - 120
    return g([trait(x - w / 2 + 20, haut, x - w / 2 + 40, y, "#495057", 10), trait(x + w / 2 - 20, haut, x + w / 2 - 40, y, "#495057", 10),
              chemin(f"M {x - w / 2} {haut} Q {x} {haut + 2 * creux} {x + w / 2} {haut}", "#343a40", stroke="#343a40", sw=10),
              rect(x - w / 2 - 10, haut - 12, 40, 18, BLEU, rx=8), rect(x + w / 2 - 30, haut - 12, 40, 18, BLEU, rx=8)])


def carrelage(S, x0, x1, y, h=None):
    h = h or S.h - y
    for i, xx in enumerate(range(x0, x1, 80)):
        for j, yy in enumerate(range(y, y + h, 60)):
            S.add(rect(xx, yy, 80, 60, "#e9ecef" if (i + j) % 2 else "#ffffff", stroke="#ced4da", stroke_width=2))


def salon(S, y=560):
    interieur(S, "#fff0f6", "#e8c39e", y, papier="#fcc2d7")
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#cc5de8"))


def jardin(S, y=640, graine=1):
    ciel(S, "#a5d8ff", "#f3f0ff")
    S.add(nuage(150, 110, 0.6), nuage(640, 80, 0.5))
    collines(S, y - 40, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a")


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S, 660, 2)
    S.add(bonds(130, 700, [180, 130, 90], [180, 170, 150]))
    S.add(balle(630, 700, 40, ROUGE, ecrase=0.35))
    S.add(pirouette(230, 790, 1.35, expr="rire", bras="haut", regard=(1, 0)))
    S.add(texte(560, 330, "Boing !", 96, ROUGE, contour="#fff", rot=-8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(balle_air(300, 70, 30, ROUGE), trajectoire("M 300 140 Q 280 250 250 250"))
    S.add(pirouette(160, 264, 1.0, expr="rire", bras="salut"))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(table(400, 700, 360, 120, "#c68642"))
    S.add(balle(300, 562, 34, ROUGE), mousse(400, 528, 34), pate(500, 562))
    S.add(carton(640, 760, 0.6, couleur="#e599f7"))
    S.add(pirouette(130, 790, 1.15, expr="joie", bras="ouverts", regard=(1, 0)))
    S.add(texte(400, 330, "Trois balles !", 64, "#ae3ec9", contour="#fff"))
    return S


def p02():
    S = Scene()
    salon(S, 600)
    carrelage(S, 0, 800, 600)
    S.add(pirouette(220, 790, 1.2, expr="rire", bras="tient", regard=(1, -1)))
    S.add(trajectoire("M 305 600 Q 370 560 420 640 Q 470 560 530 380"))
    S.add(balle(420, 642, 34, ROUGE, ecrase=0.3), balle_air(530, 330, 34, ROUGE))
    S.add(texte(640, 230, "Boing !", 80, ROUGE, contour="#fff", rot=-8))
    return S


def p03():
    S = Scene()
    salon(S, 600)
    carrelage(S, 0, 800, 600)
    S.add(pate(260, 690, 1.3, ecrasee=True), texte(260, 560, "Splotch !", 58, "#1c7ed6", contour="#fff"))
    S.add(mousse(570, 650, 34), trajectoire("M 570 610 Q 590 560 600 610"))
    S.add(texte(580, 520, "Pof.", 58, "#f08c00", contour="#fff"))
    S.add(pirouette(420, 790, 0.9, expr="surpris", bras="joues"))
    S.add(texte(400, 300, "Elle reste écrasée !", 48, "#1c7ed6", contour="#fff"))
    return S


def p04():
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(rect(0, 620, 800, 180, "#dee2e6"), trait(0, 620, 800, 620, "#868e96", 6))
    S.add(texte(400, 90, "Au ralenti…", 52, "#7048e8"))
    S.add(balle_air(150, 400, 50, ROUGE), fleche(150, 260, 150, 360, ENCRE, sw=6, tete=18))
    S.add(balle(400, 620, 50, ROUGE, ecrase=0.4), fleche(320, 560, 320, 600, "#7048e8", sw=5, tete=14), fleche(480, 560, 480, 600, "#7048e8", sw=5, tete=14))
    S.add(balle_air(650, 400, 50, ROUGE), fleche(650, 360, 650, 250, ENCRE, sw=6, tete=18))
    for x, t in ((150, "1"), (400, "2"), (650, "3")):
        S.add(cercle(x, 710, 30, "#fff", stroke="#7048e8", stroke_width=4), texte(x, 725, t, 40, "#7048e8"))
    S.add(texte(400, 480, "Elle s'écrase…", 32, ENCRE), texte(650, 220, "… et repousse !", 32, ENCRE))
    return S


def p05():
    S = Scene()
    fond(S, "#fff9db")
    # un élastique tendu entre deux doigts (deux crayons)
    S.add(rect(80, 160, 22, 220, "#fab005", rx=6), rect(320, 160, 22, 220, "#fab005", rx=6))
    S.add(chemin("M 91 200 Q 210 330 331 200", stroke="#e03131", sw=6), chemin("M 91 200 Q 210 214 331 200", stroke="#e03131", sw=4, stroke_dasharray="6 8", opacity=0.6))
    S.add(fleche(210, 300, 210, 230, "#2f9e44", sw=5, tete=14))
    S.add(texte(210, 440, "L'élastique", 40, ENCRE), texte(210, 485, "se tend… et revient !", 32, ENCRE))
    S.add(ressort(580, 380, 220, 70), fleche(680, 160, 680, 260, "#e03131", sw=5, tete=14))
    S.add(ressort(700, 380, 110, 70), texte(620, 440, "Le ressort", 40, ENCRE), texte(620, 485, "s'écrase… et revient !", 32, ENCRE))
    S.add(pirouette(400, 790, 1.1, expr="content", bras="montre", regard=(1, -1)))
    return S


def p06():
    S = Scene()
    salon(S, 640)
    carrelage(S, 0, 800, 640)
    S.add(rect(0, 214, 800, 4, "#7048e8", opacity=0.5), texte(470, 200, "jamais plus haut que le départ", 30, "#7048e8"))
    S.add(balle_air(100, 250, 26, ROUGE), trajectoire("M 100 280 L 130 640"))
    S.add(bonds(130, 640, [330, 220, 140, 80, 40], [170, 140, 115, 90, 65]))
    S.add(balle(730, 640, 26, ROUGE))
    for x, y, t in ((215, 290, "Boing !"), (370, 400, "Boing !"), (497, 480, "boing…")):
        S.add(texte(x, y, t, 34, ROUGE, contour="#fff"))
    S.add(pirouette(620, 790, 0.7, expr="surpris", bras="joues"))
    return S


def p07():
    S = Scene()
    jardin(S, 520, 3)
    carrelage(S, 0, 400, 640)
    S.add(rect(400, 600, 400, 200, "#ffe8a3"), chemin("M 400 600 Q 600 584 800 600 L 800 620 L 400 620 Z", "#ffe08a"))
    S.add(trait(400, 520, 400, 800, "#fff", 8))
    S.add(trajectoire("M 200 200 L 200 640 L 200 260"), balle_air(200, 230, 30, ROUGE))
    S.add(trajectoire("M 600 200 L 600 610"), ellipse(600, 616, 30, 10, "#e0c060"), balle(600, 616, 30, ROUGE))
    S.add(texte(200, 700, "Boing !", 54, ROUGE, contour="#fff"), texte(600, 700, "Pof.", 54, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    jardin(S, 640, 4)
    S.add(arbre(110, 660, 0.9))
    S.add(trampoline(430, 740, 440, creux=6))
    S.add(pirouette(430, 380, 1.1, expr="rire", bras="saute", pieds_haut=True), mouvement(380, 410, 1.0, rot=-90))
    S.add(chiot(720, 780, 0.75, expr="rire", bras="haut"))
    S.add(texte(560, 150, "Encore plus haut !", 54, "#ae3ec9", contour="#fff"))
    return S


def p09():
    S = Scene()
    jardin(S, 640, 5)
    S.add(pirouette(400, 760, 1.25, expr="concentre", bras="equilibre", pas="", sy=1.05))
    S.add(g([trait(300, 420 + k * 30, 300, 470 + k * 30, ENCRE, 4, opacity=0.4) for k in range(3)]))
    S.add(g([trait(500, 420 + k * 30, 500, 470 + k * 30, ENCRE, 4, opacity=0.4) for k in range(3)]))
    S.add(ressort(220, 760, 90, 50, couleur="#ae3ec9"), ressort(580, 760, 90, 50, couleur="#ae3ec9"))
    S.add(bulle(400, 180, 380, 90, "Je plie les genoux !", 38, pointe=(420, 420)))
    return S


def p10():
    S = Scene()
    jardin(S, 640, 6)
    S.add(trajectoire("M 200 690 L 200 330"), ballon_jeu(200, 300, 46, "#fff", "#343a40"))
    S.add(texte(200, 220, "Boing !", 54, ROUGE, contour="#fff"))
    S.add(ellipse(560, 700, 70, 22, "#e9ecef", stroke="#343a40", stroke_width=4), texte(560, 640, "Flop.", 54, "#868e96", contour="#fff"))
    S.add(pirouette(420, 790, 0.9, expr="triste", bras="bas", regard=(1, 1)))
    S.add(pensee(560, 380, 100, g([cercle(560, 380, 40, "#e7f5ff", stroke="#74c0fc", stroke_width=4)] +
                                     [cercle(560 + dx, 380 + dy, 7, "#4dabf7") for dx, dy in ((-18, -10), (8, -16), (16, 12), (-10, 14), (0, 0))]), depuis=(470, 560)))
    return S


def p11():
    S = Scene()
    jardin(S, 640, 7)
    S.add(rect(60, 140, 30, 560, "#fff", stroke="#868e96", stroke_width=3))
    for k in range(8):
        S.add(trait(60, 160 + k * 70, 90, 160 + k * 70, "#868e96", 3))
    S.add(trait(90, 200, 760, 200, "#7048e8", 4, stroke_dasharray="10 10"), texte(560, 180, "Tout le monde lâche d'ici !", 32, "#7048e8"))
    for x, haut, c in ((240, 360, ROUGE), (450, 520, JAUNE), (650, 300, BLEU)):
        S.add(balle_air(x, haut, 26, c), trajectoire(f"M {x} 230 L {x} 640"))
    S.add(pirouette(160, 790, 0.7, expr="rire", bras="haut"), chiot(380, 790, 0.65, expr="surpris", bras="joues"), souris(560, 790, 0.55, expr="rire", bras="haut"))
    S.add(texte(720, 720, "Bravo !", 40, "#ae3ec9", contour="#fff"))
    return S


def dans_lit(S, x, y, w, couv, qui):
    S.add(lit(x, y, w, "#e5dbff", couv))
    S.add(qui)
    S.add(rect(x - w / 2 + 60, y - 125, w - 60, 85, couv, rx=18))


def p12():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=600)
    S.add(fenetre(530, 80, 180, 170, "#141c3a", nuit_=True))
    dans_lit(S, 330, 780, 440, "#cc5de8", pirouette(230, 720, 0.6, expr="dort"))
    S.add(zzz(300, 500, 1.0, "#e5dbff"))
    S.add(etagere(660, 420, 200, "#c68642", g([balle(610, 420, 22, ROUGE), mousse(660, 398, 22), pate(710, 420, 0.65)])))
    S.add(maman(660, 790, 1.0, expr="sourire", bras="bas"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pirouette-seule.svg", vignette),
    ("01-trois-balles.svg", p01), ("02-boing.svg", p02), ("03-splotch.svg", p03), ("04-au-ralenti.svg", p04),
    ("05-elastique-ressort.svg", p05), ("06-de-plus-en-plus-bas.svg", p06), ("07-carrelage-sable.svg", p07),
    ("08-trampoline.svg", p08), ("09-les-genoux.svg", p09), ("10-ballon-degonfle.svg", p10),
    ("11-le-concours.svg", p11), ("12-au-lit.svg", p12),
]
