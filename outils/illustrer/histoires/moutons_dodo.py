"""Un mouton, deux moutons… — une histoire drôle pour s'endormir."""
from base import *
from objets import *

ID = "moutons-dodo"
LILI = dict(habit="#f783ac", motif="pois", couleur_motif="#ffdeeb")


def pre_nuit(S, graine=1):
    ciel(S, "#3b5bdb", "#91a7ff")
    etoiles(S, 30, graine, (0, 0, 800, 420))
    S.add(lune(660, 120, 50))
    collines(S, 620, "#748ffc", graine=graine)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=720)


def numero(x, y, k):
    return g([cercle(x, y, 32, "#fff3bf"), texte(x, y + 14, str(k), 40, "#3b5bdb")])


def mouton_saute(x, y, s=1.0, expr="rire"):
    return perso("mouton", x, y, s, expr=expr, bras="haut", pieds_haut=True, rot=-12)


def mouton_dort(x, y, s=1.0, expr="dort"):
    m = []
    for k in range(9):
        a = math.radians(180 + k * 22.5)
        m.append(cercle(math.cos(a) * 80, -40 + math.sin(a) * 40, 30, "#f8f9fa", stroke="#dee2e6", stroke_width=3))
    m.append(ellipse(0, -36, 96, 42, "#f8f9fa"))
    m.append(place(perso("mouton", 0, 0, 1.0, expr=expr, bras="bas"), 70, 60, 0.75).replace("", "") if False else "")
    tete = [ellipse(-50, -150, 22, 10, "#d6bfa3", rot=-20), cercle(0, -150, 46, "#f1dcc3"),
            cercle(-28, -190, 16, "#f8f9fa"), cercle(0, -198, 17, "#f8f9fa"), cercle(26, -190, 16, "#f8f9fa"),
            oeil(-17, -152, "fermes"), oeil(17, -152, "fermes"), ellipse(0, -132, 7, 5, "#8a6d4f"),
            ellipse(-32, -130, 8, 5, ROSE, opacity=0.7), ellipse(32, -130, 8, 5, ROSE, opacity=0.7)]
    if expr == "baille":
        tete.append(ellipse(0, -114, 9, 12, ROUGE_BOUCHE, stroke=ENCRE, stroke_width=2.5))
    else:
        tete.append(ellipse(0, -118, 3, 4, ENCRE))
    m.append(place(tete, 92, 90, 0.85))
    return place(m, x, y, s)


def lit_lili(S, x, y, expr="surpris", k=1.4, regard=(0, 0)):
    m = [rect(-200, -250, 28, 250, "#ae3ec9", rx=10), rect(-180, -120, 380, 60, "#fff", rx=10),
         rect(-165, -165, 110, 55, "#fff", rx=24, stroke="#e9ecef", stroke_width=3),
         perso("souris", -105, -8, 1.0, expr=expr, regard=regard, **LILI),
         chemin("M -170 -110 Q -110 -140 -40 -114 L 200 -110 L 200 -40 L -170 -40 Z", "#9775fa")]
    m += [etoile5(-100 + j * 80, -80, 12, "#e5dbff") for j in range(4)]
    m += [rect(186, -180, 28, 180, "#ae3ec9", rx=10), rect(-200, -50, 414, 30, "#ae3ec9", rx=6)]
    S.add(place(m, x, y, k))


def couverture():
    S = Scene()
    pre_nuit(S, 2)
    S.add(barriere(420, 740, 1.0))
    S.add(mouton_saute(420, 560, 1.2))
    S.add(perso("mouton", 640, 770, 1.0, expr="surpris", regard=(-1, 0)))
    S.add(perso("souris", 210, 770, 1.2, expr="rire", bras="haut", **LILI))
    S.add(numero(420, 290, 1))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("mouton", 250, 262, 0.9, expr="content", bras="salut"))
    S.add(perso("souris", 130, 262, 0.75, expr="rire", **LILI))
    return S


def p01():
    S = Scene()
    interieur(S, "#e5dbff", "#c9a47e", 590, papier="#d0bfff")
    S.add(fenetre(80, 100, 170, 150, "#1c2a52", nuit_=True, rideaux="#ffd43b"))
    lit_lili(S, 330, 770, expr="surpris", k=1.3, regard=(1, 0))
    S.add(perso("souris", 660, 760, 1.5, expr="sourire", bras="salut", regard=(-1, 0), acc=("lunettes",)))
    S.add(bulle(560, 150, 420, 100, "Compte les moutons,\nma chérie !", 34, pointe=(640, 400)))
    return S


def p02():
    S = Scene()
    pre_nuit(S, 3)
    S.add(barriere(400, 740, 1.0))
    S.add(mouton_saute(400, 560, 1.0))
    S.add(numero(400, 300, 2))
    S.add(perso("mouton", 150, 770, 0.9, expr="content", regard=(1, 0)))
    S.add(numero(150, 450, 1))
    S.add(perso("mouton", 650, 770, 1.0, expr="inquiet", bras="croises", regard=(-1, 0)))
    S.add(numero(650, 450, 3))
    S.add(bulle(620, 180, 300, 100, "J'ai le\nvertige !", 34, pointe=(640, 400)))
    return S


def p03():
    S = Scene()
    pre_nuit(S, 4)
    S.add(barriere(400, 740, 1.0))
    S.add(perso("mouton", 210, 770, 1.3, expr="sourire", bras="donne", regard=(1, 0), objet=tasse(84, -80, 1.2, "#74c0fc")))
    S.add(numero(210, 380, 4))
    S.add(bulle(220, 180, 320, 80, "J'ai soif !", 36, pointe=(220, 330)))
    S.add(perso("mouton", 600, 770, 1.3, expr="pleure", bras="bas", larmes=True))
    S.add(numero(600, 380, 5))
    S.add(bulle(580, 180, 360, 80, "Mon doudou !", 36, pointe=(590, 330)))
    return S


def p04():
    S = Scene()
    pre_nuit(S, 5)
    S.add(perso("mouton", 220, 770, 1.3, expr="rire", bras="ouverts", rot=-10, pieds_haut=True))
    S.add(notes(90, 420, 1.1, "#fff3bf"), notes(300, 360, 0.8, "#fff3bf"))
    S.add(numero(220, 300, 6))
    for x, y, r in [(520, 420, 30), (600, 350, 22), (680, 440, 36), (560, 260, 18), (700, 300, 24)]:
        S.add(cercle(x, y, r, "#e7f5ff", opacity=0.35, stroke="#fff", stroke_width=3))
    S.add(perso("mouton", 600, 770, 1.3, expr="souffle", bras="donne", flip=True,
                objet=g([trait(84, -92, 84, -40, "#fab005", 5), cercle(84, -104, 14, "none", stroke="#fab005", stroke_width=4)])))
    S.add(numero(600, 430, 7))
    return S


def p05():
    S = Scene()
    pre_nuit(S, 6)
    S.add(barriere(420, 700, 0.8))
    S.add(mouton_saute(130, 560, 0.8, "rire"))
    S.add(perso("mouton", 680, 700, 0.8, expr="rire", bras="haut", rot=15))
    S.add(perso("mouton", 580, 790, 0.8, expr="joie", bras="course"))
    S.add(perso("mouton", 220, 800, 0.8, expr="malin", bras="salut"))
    S.add(mouton_saute(620, 470, 0.7, "chante"))
    S.add(perso("souris", 400, 780, 1.4, expr="oups", bras="tete", **LILI))
    S.add(texte(400, 200, "Oh là là !", 76, "#fff3bf", contour="#3b5bdb"))
    return S


def p06():
    S = Scene()
    ciel(S, "#364fc7", "#748ffc")
    etoiles(S, 30, 7, (0, 0, 800, 420))
    S.add(lune(660, 120, 50))
    sol(S, 620, "#74b816", couleur2="#66a80f", y2=720)
    S.add(cercle(400, 520, 230, "#dbe4ff", opacity=0.25))
    S.add(perso("souris", 400, 760, 1.5, expr="dort", bras="ouverts", **LILI))
    for x, k in [(130, 0), (670, 1)]:
        S.add(perso("mouton", x, 770, 1.0, expr="dort"))
    S.add(texte(400, 240, "On respire…", 56, "#fff3bf"))
    S.add(texte(400, 310, "tout doucement…", 44, "#fff3bf"))
    return S


def p07():
    S = Scene()
    pre_nuit(S, 8)
    S.add(perso("mouton", 200, 760, 1.3, expr="baille", bras="haut"))
    S.add(numero(200, 360, 8))
    S.add(mouton_dort(560, 760, 1.4))
    S.add(numero(560, 500, 9))
    S.add(zzz(640, 520, 1.0, "#fff3bf"))
    return S


def p08():
    S = Scene()
    pre_nuit(S, 9)
    S.add(mouton_dort(250, 760, 1.3), mouton_dort(560, 770, 1.3))
    S.add(perso("souris", 420, 770, 1.2, expr="dort", rot=-22, pieds_haut=True, **LILI))
    S.add(numero(410, 480, 10))
    S.add(zzz(470, 420, 1.0, "#fff3bf"))
    S.add(texte(400, 200, "Chut !", 76, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("amis-seuls.svg", vignette),
    ("01-compte.svg", p01), ("02-vertige.svg", p02), ("03-soif-doudou.svg", p03),
    ("04-danse-bulles.svg", p04), ("05-oh-la-la.svg", p05), ("06-respirer.svg", p06),
    ("07-baillements.svg", p07), ("08-chut.svg", p08),
]
