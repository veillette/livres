"""Le chapeau de Monsieur Ours — une histoire de vent et de générosité."""
from base import *
from objets import *

ID = "chapeau-vent"
OURS = dict(couleur="#9c6644", acc=("chapeau",), couleur_acc="#e03131")
OURS_NU = dict(couleur="#9c6644")
ROUGE = "#e03131"


def pre(S, graine=1, y=600):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 100)


def vent(x, y, s=1.0, couleur="#ffffff"):
    m = [chemin("M 0 0 Q 80 -30 160 0 T 300 -10 q 40 -10 30 -40 q -10 -24 -34 -10", stroke=couleur, sw=7),
         chemin("M 40 50 Q 120 20 200 50 T 320 40", stroke=couleur, sw=6),
         chemin("M -20 -60 Q 40 -80 110 -60", stroke=couleur, sw=5)]
    return place(g(m, opacity=0.85), x, y, s)


def nid_chapeau(x, y, s=1.0, oeufs=3, poussins=0):
    m = [chapeau(0, 0, 1.0, ROUGE, rot=180, fleur_=False)]
    for k in range(oeufs):
        m.append(ellipse(-24 + k * 24, -6, 12, 15, "#e7f5ff", stroke="#a5d8ff", stroke_width=2))
    for k in range(poussins):
        m.append(oiseau(-34 + k * 34, 14, 0.42, "#ffd43b", "#fff3bf", expr="chante" if k == 1 else "rire", pattes=False))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    pre(S, 2)
    S.add(vent(120, 380, 1.1))
    S.add(chapeau(560, 360, 1.4, ROUGE, rot=-25))
    S.add(perso("ours", 360, 760, 1.8, expr="surpris", bras="haut", regard=(1, -1), **OURS_NU))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("ours", 200, 265, 0.9, expr="content", bras="salut", **OURS))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(arbre(640, 620, 1.1, fruits="#ff8787"))
    S.add(rect(170, 640, 300, 20, "#a0693a", rx=6), rect(190, 660, 16, 60, "#a0693a"), rect(434, 660, 16, 60, "#a0693a"))
    livre_ = g([rect(-50, -40, 100, 70, "#4dabf7", rx=6), trait(0, -40, 0, 30, "#1c7ed6", 3)])
    S.add(perso("ours", 320, 710, 1.6, expr="content", bras="porte", objet=place(livre_, 0, -64, 0.8), **OURS))
    S.add(fleur(120, 740, 1.0, "#f783ac"), fleur(540, 760, 0.9, "#ffd43b", "#fff"))
    return S


def p02():
    S = Scene()
    pre(S, 3)
    S.add(vent(60, 300, 1.4))
    S.add(chapeau(600, 230, 1.3, ROUGE, rot=30))
    S.add(perso("ours", 320, 760, 1.7, expr="bouche_bee", bras="haut", regard=(1, -1), **OURS_NU))
    S.add(texte(560, 450, "Fiouuu !", 70, "#1c7ed6", contour="#fff", rot=-8))
    return S


def p03():
    S = Scene()
    pre(S, 4)
    S.add(barriere(620, 700, 0.9))
    S.add(perso("mouton", 380, 760, 1.8, expr="fier", bras="hanches", acc=("chapeau",), couleur_acc=ROUGE))
    S.add(bulle(400, 150, 460, 100, "Il me va très bien,\nnon ?", 36, pointe=(420, 290)))
    S.add(vent(560, 330, 0.6))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 520, 800, 280, "#4dabf7"))
    for k in range(5):
        S.add(chemin(f"M {80 + k * 150} {600 + (k % 2) * 90} q 25 -12 50 0", stroke="#a5d8ff", sw=5))
    S.add(ellipse(130, 540, 140, 40, "#69db7c"), ellipse(700, 560, 120, 30, "#69db7c"))
    S.add(g([ellipse(620, 700, 60, 18, "#51cf66"), cercle(620, 690, 12, "#f783ac")]))
    S.add(perso("grenouille", 400, 610, 1.1, expr="rire", bras="haut"))
    S.add(chapeau(400, 590, 1.9, ROUGE, rot=180, fleur_=False))
    S.add(ellipse(400, 642, 150, 16, "#74c0fc", opacity=0.8))
    S.add(bulle(400, 160, 380, 90, "Quel joli bateau !", 38, pointe=(400, 300)))
    return S


def p05():
    S = Scene()
    pre(S, 5, 620)
    S.add(champignon(130, 720, 1.0), champignon(680, 740, 0.7, "#fab005"))
    S.add(escargot(400, 740, 2.2, coquille="#f59f00", corps="#ffe8cc", expr="rire"))
    S.add(chapeau(372, 740 - 132 * 2.2 + 20, 1.3, ROUGE, rot=-8))
    S.add(bulle(420, 150, 460, 100, "Une maison\nsur ma maison !", 36, pointe=(560, 330)))
    return S


def p06():
    S = Scene()
    ciel(S, "#99e9f2", "#e3fafc")
    S.add(rect(330, 400, 140, 400, "#8d5524"))
    S.add(chemin("M 400 470 Q 560 400 800 420", stroke="#8d5524", sw=40), chemin("M 400 520 Q 240 460 0 470", stroke="#8d5524", sw=36))
    for x, y, r in [(100, 300, 150), (400, 220, 190), (700, 300, 160), (250, 180, 120), (560, 170, 130)]:
        S.add(cercle(x, y, r, "#51cf66"))
    S.add(nid_chapeau(560, 405, 1.3, oeufs=3))
    S.add(oiseau(700, 410, 1.0, "#4dabf7", expr="content", ailes="ouvertes", regard=(-1, 0), flip=True))
    S.add(bulle(600, 640, 360, 90, "Le nid parfait !", 40, pointe=(690, 440)))
    return S


def p07():
    S = Scene()
    ciel(S, "#99e9f2", "#e3fafc")
    S.add(rect(0, 640, 800, 160, "#8ce99a"))
    S.add(rect(450, 260, 120, 400, "#8d5524"))
    S.add(chemin("M 510 330 Q 650 270 800 280", stroke="#8d5524", sw=34))
    for x, y, r in [(520, 100, 180), (740, 160, 140), (320, 140, 130)]:
        S.add(cercle(x, y, r, "#51cf66"))
    S.add(nid_chapeau(640, 270, 1.1, oeufs=3))
    S.add(oiseau(740, 280, 0.8, "#4dabf7", expr="sourire", regard=(-1, 0), flip=True))
    S.add(perso("ours", 250, 780, 1.8, expr="sourire", bras="hanches", regard=(1, -1), **OURS_NU))
    for k in range(3):
        S.add(goutte(150 + k * 26, 380 - k * 10, 0.9, "#74c0fc"))
    return S


def p08():
    S = Scene()
    ciel(S, "#ffdeeb", "#fff0f6")
    S.add(rect(0, 640, 800, 160, "#b2f2bb"))
    S.add(rect(450, 260, 120, 400, "#8d5524"))
    S.add(chemin("M 510 330 Q 650 270 800 280", stroke="#8d5524", sw=34))
    for x, y, r in [(520, 100, 180), (740, 160, 140), (320, 140, 130)]:
        S.add(cercle(x, y, r, "#fcc2d7"))
    for k in range(10):
        S.add(cercle(300 + (k * 53) % 480, 60 + (k * 37) % 200, 10, "#fff"))
    S.add(nid_chapeau(640, 270, 1.2, oeufs=0, poussins=3))
    S.add(oiseau(750, 280, 0.8, "#4dabf7", expr="content", regard=(-1, 0), flip=True))
    S.add(notes(560, 150, 0.9, "#d6336c"))
    S.add(perso("ours", 260, 780, 1.8, expr="rire", bras="salut", regard=(1, -1), acc=("fleur",), couleur_acc="#ffd43b", couleur="#9c6644"))
    for x in (90, 380, 700):
        S.add(fleur(x, 760, 0.9, "#f783ac"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ours-seul.svg", vignette),
    ("01-le-chapeau.svg", p01), ("02-fiouuu.svg", p02), ("03-mouton.svg", p03),
    ("04-bateau.svg", p04), ("05-escargot.svg", p05), ("06-le-nid.svg", p06),
    ("07-les-oeufs.svg", p07), ("08-printemps.svg", p08),
]
