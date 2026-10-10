"""Rond, carré, triangle — les formes et les couleurs avec Pinceau le lapin.

Pinceau peint un rond rouge (comme une pomme), un carré bleu (comme une
fenêtre sur le ciel), un triangle jaune (comme une part de fromage), un
rectangle vert (comme une porte), un ovale violet (comme une prune), une
étoile orange (comme une étoile de mer). Il mélange ses couleurs (jaune et
bleu font du vert, rouge et jaune de l'orange, rouge et bleu du violet :
c'est exact pour la peinture), puis assemble ses formes en un tableau.

Plans : 1 moyen (l'atelier) · 2 gros plan (le rond) · 3 moyen (le carré) ·
4 gros plan (le triangle) · 5 moyen (le rectangle) · 6 gros plan (l'ovale et
l'étoile) · 7 moyen (les mélanges) · 8 gros plan (une maison) · 9 large (le
tableau) · 10 moyen (Pinceau tout barbouillé).
"""
from base import *
from base import _assombrir
from objets import pomme, pinceau, pot_peinture

ID = "formes-couleurs"
PAPIER_PEINT = "pois"

ROUGE, BLEU, JAUNE, VERT, VIOLET, ORANGE = "#fa5252", "#339af0", "#fcc419", "#40c057", "#9775fa", "#ff922b"
PINCEAU = dict(habit="#ffffff", acc=("tablier",), couleur_acc=ROUGE)


def lapin(x, y, s=1.4, **k):
    return perso("lapin", x, y, s, **{**PINCEAU, **k})


def forme(nom, x, y, r, couleur, rot=0):
    """Une forme peinte, centrée en (x, y), de « rayon » r."""
    if nom == "rond":
        f = cercle(0, 0, r, couleur)
    elif nom == "carre":
        f = rect(-r, -r, 2 * r, 2 * r, couleur, rx=r * 0.06)
    elif nom == "triangle":
        f = poly([(0, -r), (r * 1.1, r * 0.8), (-r * 1.1, r * 0.8)], couleur, stroke=couleur, stroke_width=r * 0.08, stroke_linejoin="round")
    elif nom == "rectangle":
        f = rect(-r * 0.62, -r, r * 1.24, 2 * r, couleur, rx=r * 0.05)
    elif nom == "ovale":
        f = ellipse(0, 0, r * 0.75, r, couleur)
    elif nom == "etoile":
        f = etoile5(0, 0, r, couleur)
    else:
        f = coeur(0, r * 0.2, r / 30, couleur)
    # coups de pinceau : quelques traits plus clairs dans la peinture
    trace_ = chemin(f"M {n(-r * 0.5)} {n(-r * 0.2)} q {n(r * 0.3)} {n(-r * 0.1)} {n(r * 0.6)} 0 M {n(-r * 0.4)} {n(r * 0.2)} q {n(r * 0.4)} {n(-r * 0.1)} {n(r * 0.7)} 0",
                    stroke=eclaircir(couleur, 0.35), sw=max(r * 0.06, 2), opacity=0.6)
    return place([sans_relief(f), trace_], x, y, 1, rot=rot)


def chevalet(x, y, s=1.0, contenu=""):
    """Chevalet de peintre ; contenu en coordonnées du papier (centre (0, 0), 280 × 220)."""
    bois = "#a0693a"
    m = [trait(-110, 0, -40, -480, bois, 14), trait(110, 0, 40, -480, bois, 14), trait(0, -20, 0, -470, _assombrir(bois, 0.8), 12),
         rect(-170, -180, 340, 20, volume(bois, 0.35, 0.75), rx=6),
         rect(-150, -420, 300, 240, "#fffdf6", stroke="#dee2e6", stroke_width=3)]
    m.append(place(contenu, 0, -300) if contenu else "")
    return place(m, x, y, s)


def atelier(S, y=600):
    interieur(S, "#fff4e6", "#d9a066", y, papier="#ffd8a8")
    S.add(fenetre(80, 90, 170, 160, "#a5d8ff", rideaux="#ff922b",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), nuage(190, 160, 0.4)])))
    S.add(tapis(420, y + 140, 300, 50, "#ffe3e3", "#ff8787"))
    # quelques taches de peinture au sol
    for (tx, ty, c) in ((600, y + 150, BLEU), (240, y + 170, JAUNE), (700, y + 100, ROUGE)):
        S.add(ellipse(tx, ty, 26, 9, c, opacity=0.8))


def pots(x, y, s=1.0, couleurs=(ROUGE, JAUNE, BLEU)):
    return g([pot_peinture(x + k * 64 * s, y, s, c) for k, c in enumerate(couleurs)])


def etiquette(x, y, mot_forme, mot_couleur, couleur):
    """« un rond » / « rouge » écrits en deux lignes."""
    return g([texte(x, y, mot_forme, 54, ENCRE, contour="#fff"), texte(x, y + 60, mot_couleur, 54, couleur, contour="#fff")])


def page_forme(nom, couleur, mot_forme, mot_couleur, objet, gros=False, graine=1):
    """Pinceau a peint une forme ; l'objet qui lui ressemble est à côté."""
    S = Scene()
    atelier(S)
    S.add(chevalet(260, 770, 1.15, forme(nom, 0, 0, 80, couleur)))
    S.add(lapin(560, 790, 1.4, expr="content", bras="designe", flip=True, regard=(-1, 0),
                objet=pinceau(106, -122, 1.0, couleur, rot=-60)))
    S.add(objet)
    if gros:
        S.camera(1.3, 330, 470)
        S.dessus(etiquette(600, 110, mot_forme, mot_couleur, couleur))
    else:
        S.add(etiquette(600, 130, mot_forme, mot_couleur, couleur))
    return S


def fromage(x, y, s=1.0):
    return place([poly([(-70, 30), (70, 30), (40, -50)], volume("#ffd43b", 0.4, 0.8)),
                  poly([(-70, 30), (70, 30), (70, 50), (-70, 50)], "#fab005"),
                  cercle(10, 10, 8, "#f59f00"), cercle(-24, 22, 6, "#f59f00"), cercle(40, -14, 5, "#f59f00")], x, y, s)


def prune(x, y, s=1.0):
    return place([ellipse(0, 0, 30, 38, volume("#7048e8", 0.45, 0.75)), chemin("M 0 -36 Q 4 -50 10 -56", stroke="#5c3a1e", sw=4),
                  ellipse(14, -48, 12, 6, "#40c057", rot=-30), ellipse(-10, -12, 6, 10, "#fff", opacity=0.4)], x, y, s)


def etoile_mer(x, y, s=1.0):
    m = [etoile5(0, 0, 50, ORANGE)]
    for k in range(5):
        a = math.radians(-90 + k * 72)
        for t in (0.35, 0.6):
            m.append(cercle(math.cos(a) * 50 * t, math.sin(a) * 50 * t, 3.5, "#ffd8a8"))
    return place(m, x, y, s)


def porte_jardin(x, y, s=1.0):
    return place([rect(-50, -160, 100, 160, volume(VERT, 0.3, 0.8), rx=4), rect(-40, -150, 80, 60, "none", stroke="#2b8a3e", stroke_width=4),
                  rect(-40, -80, 80, 70, "none", stroke="#2b8a3e", stroke_width=4), cercle(32, -82, 6, "#fcc419")], x, y, s)


def fenetre_ciel(x, y, s=1.0):
    return place([rect(-60, -60, 120, 120, "#fff"), rect(-52, -52, 104, 104, "#74c0fc"), nuage(-10, 0, 0.25),
                  rect(-3, -52, 6, 104, "#fff"), rect(-52, -3, 104, 6, "#fff")], x, y, s)


def maison_formes(x, y, s=1.0):
    """Une maison faite de formes : un carré, un triangle, un rectangle, deux petits carrés."""
    return place([forme("carre", 0, 0, 100, BLEU), forme("triangle", 0, -170, 90, ROUGE), forme("rectangle", 0, 50, 50, VERT),
                  forme("carre", -60, -30, 24, JAUNE), forme("carre", 60, -30, 24, JAUNE)], x, y, s)


def tableau(s=1.0):
    """Le grand tableau final (coordonnées du papier, centre (0, 0))."""
    return place([rect(-140, 40, 280, 70, "#d3f9d8"),
                  forme("rond", 90, -70, 26, JAUNE),
                  place(maison_formes(0, 0, 1.0), -60, 30, 0.42),
                  forme("rectangle", 70, 30, 18, "#a0693a"), forme("triangle", 70, -10, 34, VERT),
                  forme("rond", -120, 60, 8, ROUGE), forme("rond", -100, 70, 8, VIOLET), forme("rond", 120, 70, 8, ORANGE),
                  forme("etoile", -110, -80, 14, ORANGE)], 0, 0, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    atelier(S)
    S.add(chevalet(270, 770, 1.15, tableau(0.9)))
    S.add(lapin(570, 790, 1.5, expr="rire", bras="haut", regard=(-1, 0), objet=pinceau(70, -170, 1.0, ROUGE, rot=-20)))
    S.add(pots(80, 790, 0.9, (ROUGE, JAUNE, BLEU)))
    for k, (nom, c) in enumerate((("rond", ROUGE), ("carre", BLEU), ("triangle", JAUNE), ("etoile", ORANGE))):
        S.add(forme(nom, 520 + k * 70, 330 - (k % 2) * 30, 22, c, rot=k * 12))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(forme("rond", 90, 160, 50, ROUGE), forme("carre", 210, 160, 48, BLEU), forme("triangle", 320, 170, 50, JAUNE))
    return S


def p01():
    """Plan moyen : l'atelier de Pinceau, son chevalet, son papier blanc et ses pots."""
    S = Scene()
    atelier(S)
    S.add(chevalet(270, 770, 1.15))
    S.add(lapin(560, 790, 1.5, expr="content", bras="tient", regard=(-1, 0), objet=pinceau(70, -170, 1.0, "#ced4da", rot=-20)))
    S.add(pots(60, 790, 0.9, (ROUGE, JAUNE, BLEU)))
    S.add(pot_peinture(680, 790, 0.9, "#ffffff"))
    S.add(bulle(560, 140, 400, 100, "Que vais-je\npeindre ?", 36, pointe=(540, 380)))
    return S


def p02():
    """Gros plan : un rond rouge, comme une pomme."""
    return page_forme("rond", ROUGE, "un rond", "rouge", pomme(440, 600, 2.2), gros=True)


def p03():
    """Plan moyen : un carré bleu, comme une fenêtre sur le ciel."""
    S = page_forme("carre", BLEU, "un carré", "bleu", fenetre_ciel(690, 560, 0.9))
    return S


def p04():
    """Gros plan : un triangle jaune, comme une part de fromage."""
    return page_forme("triangle", JAUNE, "un triangle", "jaune", fromage(430, 610, 1.1), gros=True)


def p05():
    """Plan moyen : un rectangle vert, comme une porte de jardin."""
    return page_forme("rectangle", VERT, "un rectangle", "vert", porte_jardin(720, 790, 0.9))


def p06():
    """Gros plan : un ovale violet comme une prune, une étoile orange comme une étoile de mer."""
    S = Scene()
    atelier(S)
    S.add(chevalet(300, 790, 1.2, g([forme("ovale", -70, 0, 70, VIOLET), forme("etoile", 75, 0, 70, ORANGE)])))
    S.add(prune(150, 620, 1.3), etoile_mer(470, 640, 1.0))
    S.add(lapin(640, 800, 1.4, expr="rire", bras="applaudit", flip=True, regard=(-1, 0)))
    S.camera(1.2, 380, 470)
    S.dessus(texte(220, 110, "un ovale violet", 42, VIOLET, contour="#fff"), texte(560, 170, "une étoile orange", 42, ORANGE, contour="#fff"))
    return S


def melange(x, y, c1, c2, c3):
    """Deux taches de peinture qui, mélangées, donnent une troisième."""
    return g([cercle(x - 130, y, 32, c1), texte(x - 65, y + 16, "+", 48, ENCRE), cercle(x, y, 32, c2),
              texte(x + 65, y + 16, "=", 48, ENCRE), cercle(x + 130, y, 38, c3)])


def p07():
    """Plan moyen : Pinceau mélange ses couleurs."""
    S = Scene()
    atelier(S)
    S.add(rect(70, 90, 400, 360, "#fffdf6", rx=10, stroke="#dee2e6", stroke_width=4))
    S.add(melange(270, 170, JAUNE, BLEU, VERT), melange(270, 270, ROUGE, JAUNE, ORANGE), melange(270, 370, ROUGE, BLEU, VIOLET))
    S.add(lapin(620, 790, 1.5, expr="surpris", bras="donne", flip=True, regard=(-1, 0),
                objet=pinceau(96, -110, 1.0, VERT, rot=-50)))
    S.add(pots(140, 790, 1.0, (JAUNE, BLEU, VERT)))
    S.add(bulle(600, 140, 300, 90, "Magique !", 40, pointe=(600, 400)))
    return S


def p08():
    """Gros plan : un carré, un triangle et un rectangle… une maison !"""
    S = Scene()
    atelier(S)
    S.add(chevalet(330, 790, 1.25, maison_formes(0, 20, 0.6)))
    S.add(lapin(640, 800, 1.4, expr="fier", bras="montre", flip=True, regard=(-1, 0), objet=pinceau(90, -136, 1.0, ROUGE, rot=-40)))
    S.camera(1.2, 420, 460)
    S.dessus(texte(400, 100, "Une maison !", 56, "#e8590c", contour="#fff"))
    return S


def p09():
    """Plan large : le grand tableau de formes et de couleurs ; les amis de Pinceau l'admirent."""
    S = Scene()
    atelier(S)
    S.add(chevalet(400, 760, 1.25, tableau(1.0)))
    S.add(lapin(160, 790, 1.15, expr="fier", bras="ouverts", regard=(1, -0.3)))
    S.add(perso("souris", 620, 790, 0.9, expr="bouche_bee", bras="joues", regard=(-1, -0.5), habit="#ffd43b"))
    S.add(perso("ours", 720, 790, 1.0, expr="surpris", bras="applaudit", regard=(-1, -0.5), acc=("noeud",), couleur_acc=BLEU))
    S.add(texte(400, 70, "Bravo, Pinceau !", 50, "#e8590c", contour="#fff"))
    return S


def p10():
    """Plan moyen : Pinceau, barbouillé de toutes les couleurs, rit aux éclats."""
    S = Scene()
    atelier(S)
    S.add(lapin(400, 790, 2.0, expr="rire", bras="haut"))
    r = random.Random(5)
    for k in range(14):
        c = (ROUGE, BLEU, JAUNE, VERT, VIOLET, ORANGE)[k % 6]
        x, y = 400 + r.uniform(-80, 80) * 2.0 / 1.4, 790 - r.uniform(20, 240) * 2.0 / 1.4
        S.add(cercle(x, y, r.uniform(6, 12), c))
    S.add(pot_peinture(170, 790, 1.2, VERT, renverse=True), pot_peinture(640, 790, 1.2, BLEU))
    for k, (nom, c) in enumerate((("rond", ROUGE), ("carre", BLEU), ("triangle", JAUNE), ("ovale", VIOLET), ("etoile", ORANGE), ("rectangle", VERT))):
        a = math.radians(-160 + k * 28)
        S.add(forme(nom, 400 + math.cos(a) * 320, 330 + math.sin(a) * 200, 26, c, rot=k * 15))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("formes-seules.svg", vignette),
    ("01-l-atelier.svg", p01), ("02-un-rond.svg", p02), ("03-un-carre.svg", p03),
    ("04-un-triangle.svg", p04), ("05-un-rectangle.svg", p05), ("06-ovale-etoile.svg", p06),
    ("07-les-melanges.svg", p07), ("08-une-maison.svg", p08), ("09-le-tableau.svg", p09),
    ("10-barbouille.svg", p10),
]
