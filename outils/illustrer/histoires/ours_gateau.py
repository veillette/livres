"""Le gâteau de Petit Ours — la patience."""
from base import *
from objets import *

ID = "ours-gateau"
PAPI = dict(couleur="#8f5f3a", acc=("lunettes",))
PETIT = dict(acc=("toque", "tablier"))


def cuisine(S, fen=True, tasses=True):
    interieur(S, "#fff4e6", "#e8c39e", 600, papier="#ffd8a8")
    if fen:
        S.add(fenetre(80, 110, 170, 150, "#a5d8ff", rideaux="#ff8787",
                      contenu=soleil(200, 150, 26, rayons=False) + nuage(120, 220, 0.5)))
    if tasses:
        S.add(etagere(640, 150, 220, objets=g([tasse(580, 150, 1.0, "#4dabf7"), tasse(640, 150, 1.0, "#ffd43b"), tasse(700, 150, 1.0, "#ff8787")])))


def ingredients():
    m = [rect(-40, -80, 70, 80, "#f8f9fa", rx=8, stroke="#dee2e6", stroke_width=3),
         texte(-5, -36, "farine", 18, "#868e96"),
         ellipse(60, -14, 14, 18, "#fff4e6", stroke="#e9ecef", stroke_width=2),
         ellipse(88, -14, 14, 18, "#fff4e6", stroke="#e9ecef", stroke_width=2)]
    return g(m)


def bol_myrtilles(x, y):
    m = [chemin(f"M {x - 34} {y - 26} Q {x - 30} {y} {x} {y} Q {x + 30} {y} {x + 34} {y - 26} Z", "#ffd43b")]
    for k in range(7):
        m.append(cercle(x - 24 + k * 8, y - 28 - (k % 2) * 6, 7, "#5c7cfa"))
    return g(m)


def couverture():
    S = Scene()
    cuisine(S, fen=False)
    S.add(fenetre(560, 120, 160, 150, "#a5d8ff", rideaux="#ff8787"))
    S.add(tapis(400, 730, 250, 45, "#ffc9c9", "#ff8787"))
    S.add(perso("ours", 400, 740, 1.75, expr="rire", bras="large", **PETIT,
                objet=gateau(0, -8, 0.72)))
    S.add(paillettes(230, 470), paillettes(560, 440, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("ours", 200, 262, 0.95, expr="content", bras="large", **PETIT,
                objet=gateau(0, -8, 0.72)))
    return S


def p01():
    S = Scene()
    cuisine(S)
    S.add(perso("ours", 250, 660, 1.75, expr="sourire", bras="porte", regard=(1, 0.3), **PAPI))
    S.add(rect(530, 560, 110, 100, "#c68642", rx=8))
    S.add(perso("ours", 580, 570, 1.2, expr="joie", bras="haut", regard=(-1, 0.3), **PETIT))
    S.add(table(400, 780, 620, 190, "#c68642", nappe="#ffe3e3"))
    S.add(bol(380, 585, 1.0, "#74c0fc", "#fff3bf"))
    S.add(place(ingredients(), 180, 585))
    S.add(bol_myrtilles(560, 585))
    return S


def p02():
    S = Scene()
    cuisine(S, fen=False)
    S.add(cercle(400, 380, 300, "#ffe8cc"))
    S.add(perso("ours", 400, 780, 2.2, expr="concentre", bras="porte", **PETIT,
                objet=bol(0, -30, 0.75, "#74c0fc", "#e0c3fc")))
    for x, y in [(250, 540), (560, 520), (300, 470), (520, 600)]:
        S.add(cercle(x, y, 8, "#fff", opacity=0.9))
    S.add(bulle(620, 150, 280, 90, "On le mange ?", 38, pointe=(520, 250)))
    return S


def p03():
    S = Scene()
    cuisine(S, fen=False)
    S.add(four(420, 700, 1.5, allume=True))
    S.add(perso("ours", 680, 720, 1.35, expr="surpris", bras="joues", regard=(-1, 0), **PETIT))
    S.add(perso("ours", 150, 760, 1.6, expr="sourire", bras="hanches", regard=(1, 0), **PAPI))
    S.add(bulle(230, 170, 280, 90, "Pas encore !", 40, pointe=(170, 420)))
    return S


def p04():
    S = Scene()
    cuisine(S, fen=False, tasses=False)
    S.add(horloge(400, 150, 70, 3, 10))
    S.add(texte(250, 130, "tic", 44, "#f08c00", rot=-12), texte(560, 130, "tac", 44, "#f08c00", rot=12))
    S.add(perso("ours", 150, 690, 1.05, expr="concentre", bras="haut", **PETIT))
    S.add(texte(150, 380, "1, 2, 3…", 34, "#e8590c"))
    S.add(perso("ours", 400, 740, 1.05, expr="chante", bras="ouverts", rot=-8, **PETIT))
    S.add(notes(440, 440, 0.9, "#e8590c"))
    S.add(perso("ours", 650, 700, 1.05, expr="inquiet", bras="joues", **PETIT))
    S.add(texte(650, 390, "C'est long !", 32, "#e8590c"))
    return S


def p05():
    S = Scene()
    cuisine(S, fen=False)
    S.add(four(190, 700, 1.3, allume=True))
    for k in range(3):
        y = 330 + k * 40
        S.add(chemin(f"M 300 {y} q 60 -40 120 0 t 120 0 t 120 0", stroke="#ffc078", sw=10, opacity=0.8))
    S.add(perso("ours", 560, 740, 1.5, expr="content", bras="bas", **PETIT))
    S.add(perso("chat", 700, 760, 0.9, expr="miam", bras="bas", regard=(-1, 0), couleur="#868e96"))
    S.add(texte(560, 250, "Mmm…", 60, "#e8590c"))
    return S


def p06():
    S = Scene()
    cuisine(S, fen=False, tasses=False)
    S.add(four(620, 700, 1.1, allume=False, ouvert=True))
    S.add(perso("ours", 360, 750, 1.75, expr="sourire", bras="large", **PAPI,
                objet=gateau(0, -10, 0.7, fumee=True) + gants_four(-64, -70, 1.1) + gants_four(64, -70, 1.1)))
    S.add(perso("ours", 130, 760, 1.2, expr="bouche_bee", bras="haut", regard=(1, 0), **PETIT))
    S.add(texte(620, 200, "DING !", 90, "#fa5252", contour="#fff", rot=8))
    return S


def p07():
    S = Scene()
    cuisine(S, tasses=False)
    S.add(gateau(165, 268, 0.5))
    S.add(rect(60, 268, 210, 14, "#fff", rx=5))
    dehors = (rect(0, 0, 800, 800, "#a5d8ff") + rect(0, 330, 800, 400, "#8ce99a")
              + perso("lapin", 640, 400, 0.85, expr="joie", bras="salut", regard=(-1, 0))
              + perso("souris", 530, 400, 0.75, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(fenetre(450, 110, 260, 200, "#a5d8ff", rideaux="#ff8787", contenu=dehors))
    S.add(texte(580, 380, "On arrive !", 40, "#e8590c"))
    S.add(perso("ours", 250, 700, 1.4, expr="content", bras="donne", **PETIT,))
    S.add(table(480, 780, 420, 170, "#c68642", nappe="#d0ebff"))
    for k, px in enumerate([340, 440, 540, 620]):
        S.add(assiette(px, 612, 1.0, bord=["#ff8787", "#ffd43b", "#69db7c", "#74c0fc"][k]))
    return S


def p08():
    S = Scene()
    cuisine(S)
    S.add(perso("ours", 150, 650, 1.5, expr="rire", bras="porte", **PAPI))
    S.add(perso("lapin", 290, 640, 1.05, expr="miam", bras="porte", regard=(1, 0)))
    S.add(perso("ours", 470, 640, 1.2, expr="rire", bras="haut", **PETIT))
    S.add(perso("souris", 620, 640, 0.95, expr="content", bras="porte"))
    S.add(perso("chat", 720, 660, 0.9, expr="miam", bras="porte", couleur="#868e96", regard=(-1, 0)))
    S.add(table(400, 790, 700, 190, "#c68642", nappe="#ffe3e3"))
    S.add(gateau(420, 610, 0.8))
    for px in (160, 290, 620, 730):
        S.add(part_gateau(px, 618, 0.9))
    S.add(coeur(300, 300, 1.2), coeur(560, 280, 0.9, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ours-seul.svg", vignette),
    ("01-ingredients.svg", p01), ("02-melanger.svg", p02), ("03-four.svg", p03),
    ("04-attendre.svg", p04), ("05-odeur.svg", p05), ("06-cuit.svg", p06),
    ("07-inviter.svg", p07), ("08-partager.svg", p08),
]
