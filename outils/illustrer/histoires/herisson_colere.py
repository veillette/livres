"""Hérisson est en colère — apprivoiser sa colère."""
from base import *
from objets import *

ID = "herisson-colere"
PIC = dict(habit="#ffd43b")
ROUGE = dict(habit="#ffd43b", couleur="#e8704f", visage="#ffa99a")
LAPINOU = dict(couleur="#e9ecef", habit="#74c0fc")


def salle(S, mur="#fff0f6", papier="#ffdeeb"):
    interieur(S, mur, "#e0b98f", 600, papier=papier)
    S.add(fenetre(90, 110, 160, 150, "#a5d8ff", rideaux="#b2f2bb", contenu=arbre(80, 200, 0.5)))
    S.add(tapis(420, 740, 280, 50, "#c3fae8", "#63e6be"))


def couverture():
    S = Scene()
    salle(S, "#fff4e6", "#ffe8cc")
    S.add(perso("herisson", 400, 760, 1.9, expr="fache", bras="croises", **ROUGE))
    S.add(nuage_orage(560, 330, 0.7))
    S.add(tour_cubes(180, 740, 0.8, 4, graine=3, penche=0.5))
    S.add(cube(640, 715, 0.9, "#4dabf7", "B", rot=20), cube(560, 730, 0.8, "#69db7c", "C", rot=-12))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("herisson", 200, 265, 1.0, expr="content", bras="porte", **PIC,
                objet=cube(0, -70, 0.9, "#ff6b6b", "A")))
    return S


def p01():
    S = Scene()
    salle(S)
    S.add(tour_cubes(560, 740, 1.05, 8, graine=1))
    S.add(perso("herisson", 290, 760, 1.6, expr="fier", bras="haut", regard=(1, -1), **PIC))
    S.add(paillettes(560, 160))
    return S


def p02():
    S = Scene()
    salle(S)
    for k, (x, y, rt, c, l) in enumerate([(520, 700, 10, "#ff6b6b", "A"), (600, 560, -30, "#4dabf7", "B"), (470, 440, 25, "#ffd43b", "C"),
                                          (650, 340, -15, "#69db7c", "D"), (540, 250, 40, "#cc5de8", "E"), (700, 690, 60, "#ff922b", "F")]):
        S.add(cube(x, y, 1.0, c, l, rot=rt))
    S.add(perso("lapin", 300, 760, 1.5, expr="oups", bras="course", regard=(1, 0), **LAPINOU))
    S.add(mouvement(180, 560, 1.4))
    S.add(texte(400, 150, "BADABOUM !", 84, "#e03131", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    fond(S, "#ffe3e3")
    S.add(cercle(400, 450, 330, "#ffc9c9"))
    for k in range(10):
        a = math.radians(k * 36)
        S.add(trait(400 + math.cos(a) * 250, 450 + math.sin(a) * 250, 400 + math.cos(a) * 330, 450 + math.sin(a) * 330, "#ff8787", 12))
    S.add(perso("herisson", 400, 760, 2.1, expr="furieux", bras="poing", **ROUGE))
    S.add(texte(400, 150, "GRRRR !", 100, "#c92a2a", contour="#fff"))
    for sgn in (-1, 1):
        S.add(g([trait(400 + sgn * 70, 770, 400 + sgn * 110, 790, "#c92a2a", 6), trait(400 + sgn * 80, 750, 400 + sgn * 130, 755, "#c92a2a", 6)]))
    return S


def p04():
    S = Scene()
    ciel(S, "#5c677d", "#adb5bd")
    pluie(S, 50, 4, (0, 350, 800, 800), "#74c0fc")
    S.add(nuage_orage(400, 210, 1.5))
    S.add(nuage(160, 140, 0.7, "#343a40"), nuage(650, 130, 0.8, "#343a40"))
    S.add(perso("herisson", 400, 760, 1.8, expr="furieux", bras="poing", **ROUGE))
    return S


def p05():
    S = Scene()
    salle(S)
    for k, (x, rt, c, l) in enumerate([(120, 10, "#ff6b6b", "A"), (190, -20, "#4dabf7", "B"), (700, 30, "#ffd43b", "C")]):
        S.add(cube(x, 720, 0.9, c, l, rot=rt))
    S.add(perso("herisson", 260, 760, 1.5, expr="fache", bras="croises", **ROUGE))
    S.add(tortue(560, 750, 1.5, carapace="#94d82d", peau="#d8f5a2", flip=True, regard=(-1, 0)))
    S.add(bulle(520, 170, 440, 110, "Fais comme moi…\nrespire !", 38, pointe=(490, 520)))
    return S


def p06():
    S = Scene()
    fond(S, "#e6fcf5")
    S.add(cercle(400, 430, 320, "#c3fae8"))
    obj = fleur(-64, -60, 1.0, "#f783ac", tige=28) + bougie(64, -46, 0.55, flamme=True)
    S.add(perso("herisson", 400, 760, 2.0, expr="souffle", bras="large", objet=obj, **PIC))
    S.add(texte(210, 200, "Je sens la fleur…", 38, "#0ca678"), texte(560, 280, "…je souffle", 38, "#0ca678"),
          texte(600, 330, "la bougie.", 38, "#0ca678"))
    for k in range(3):
        S.add(chemin(f"M {560 + k * 40} {430 - k * 10} q 20 -20 40 0", stroke="#63e6be", sw=5))
    return S


def p07():
    S = Scene()
    salle(S)
    S.add(perso("lapin", 540, 760, 1.55, expr="timide", bras="donne2", regard=(-1, 0), flip=True, **LAPINOU))
    S.add(perso("herisson", 250, 760, 1.5, expr="sourire", bras="bas", regard=(1, 0), **PIC))
    S.add(bulle(560, 150, 420, 90, "Pardon, Pic !", 40, pointe=(560, 330)))
    S.add(cube(370, 720, 0.8, "#ffd43b", "C", rot=15))
    return S


def p08():
    S = Scene()
    salle(S)
    S.add(tour_cubes(400, 745, 0.95, 10, graine=7, couleurs=("#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8", "#ff922b", "#20c997")))
    S.add(perso("herisson", 200, 760, 1.4, expr="rire", bras="haut", regard=(1, -1), **PIC))
    S.add(perso("lapin", 610, 760, 1.4, expr="rire", bras="haut", regard=(-1, -1), **LAPINOU))
    S.add(paillettes(560, 120), paillettes(250, 160, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pic-seul.svg", vignette),
    ("01-la-tour.svg", p01), ("02-badaboum.svg", p02), ("03-grrr.svg", p03),
    ("04-orage.svg", p04), ("05-grand-mere-tortue.svg", p05), ("06-respirer.svg", p06),
    ("07-pardon.svg", p07), ("08-ensemble.svg", p08),
]
