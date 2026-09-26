"""Boum ! fait le tambour — le son.

Un son grave est une vibration lente (ondes longues), un son aigu une
vibration rapide (ondes courtes) ; un son fort a de grandes vibrations.
Quand on tape sur des bouteilles, la plus remplie donne la note la plus grave.
"""
from base import *
from objets import *
from sciences import *

ID = "pompon-sons"
POMPON = dict(habit="#ffa8a8", couleur_acc="#ff6b6b")
SOURIS = dict(acc=("noeud",), couleur_acc="#cc5de8")
ONDE = "#f03e3e"


def pompon(x, y, s=1.0, **k):
    return perso("lapin", x, y, s, **{**POMPON, **k})


def tambour(x, y, s=1.0, couleur="#e03131", vibre=False):
    """Tambour vu de côté ; (x, y) = milieu du bas."""
    m = [rect(-110, -140, 220, 140, couleur, rx=8)]
    zz = " ".join(f"L {-110 + k * 27.5} {-128 if k % 2 == 0 else -12}" for k in range(9))
    m.append(chemin("M -110 -128 " + zz, stroke="#fff", sw=5))
    m += [rect(-116, -150, 232, 20, "#fcc419", rx=8), rect(-116, -14, 232, 20, "#fcc419", rx=8)]
    m.append(ellipse(0, -150, 116, 26, "#fff4e6", stroke="#fcc419", stroke_width=6))
    if vibre:
        m += [ellipse(0, -150, 80 - k * 26, 16 - k * 5, "none", stroke="#fab005", stroke_width=3, opacity=0.8) for k in range(3)]
    return place(m, x, y, s)


def baguette(x, y, s=1.0, rot=30):
    return place([rect(-6, -110, 12, 110, "#c68642", rx=6), cercle(0, -114, 16, "#fff4e6")], x, y, s, rot=rot)


def bouteille(x, y, niveau, couleur="#4dabf7", s=1.0, note=None):
    """Bouteille en verre ; niveau = fraction remplie. (x, y) = milieu du bas."""
    h = 230
    m = [chemin("M -44 0 L -44 -150 Q -44 -180 -16 -196 L -16 -230 L 16 -230 L 16 -196 Q 44 -180 44 -150 L 44 0 Z", "#e7f5ff", opacity=0.6)]
    hl = h * niveau
    m.append(rect(-40, -min(hl, 148), 80, min(hl, 148) - 4, couleur, rx=4, opacity=0.85))
    m.append(chemin("M -44 0 L -44 -150 Q -44 -180 -16 -196 L -16 -230 L 16 -230 L 16 -196 Q 44 -180 44 -150 L 44 0 Z", "none", stroke="#adb5bd", sw=4))
    m.append(rect(-32, -140, 8, 110, "#fff", rx=4, opacity=0.6))
    if note:
        m.append(texte(0, -250, note, 40, couleur, contour="#fff"))
    return place(m, x, y, s)


def pre(S, graine=1, haut="#a5d8ff", bas="#e7f5ff"):
    ciel(S, haut, bas)
    collines(S, 600, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=690)


def couverture():
    S = Scene()
    pre(S, 3, "#ffc9c9", "#fff5f5")
    S.add(ondes(560, 520, 70, 4, 45, -60, 80, ONDE, 7))
    S.add(tambour(560, 760, 1.2, vibre=True))
    S.add(pompon(290, 770, 1.8, expr="rire", bras="haut"))
    S.add(notes(560, 250, 1.5, "#7048e8"), notes(120, 300, 1.1, "#e64980"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pompon(200, 262, 0.95, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(arbre(130, 620, 0.7))
    S.add(oiseau(150, 400, 0.5, "#fab005", "#fff3bf", ailes="ouvertes", pattes=False, bec_ouvert=True))
    S.add(notes(200, 330, 0.7, "#f08c00"))
    S.add(rafales(560, 190, 0.8, "#ffffff"))
    S.add(chemin("M 560 740 Q 640 700 720 750 T 820 740", stroke="#4dabf7", sw=30))
    S.add(pompon(400, 760, 1.9, expr="surpris", regard=(1, -1)))
    S.add(texte(420, 150, "?", 100, "#7048e8", contour="#fff"))
    return S


def p02():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=600)
    S.add(tambour(520, 760, 1.4, vibre=True))
    S.add(ondes(520, 520, 60, 3, 40, -90, 90, ONDE, 6))
    S.add(pompon(230, 770, 1.7, expr="rire", bras="donne", regard=(1, 0)))
    S.add(texte(560, 220, "BOUM !", 90, ONDE, contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600)
    S.add(tambour(400, 780, 1.8, vibre=True))
    r = random.Random(3)
    for k in range(22):
        x = 400 + r.uniform(-170, 170)
        y = 480 - r.uniform(20, 170)
        S.add(ellipse(x, y, 11, 6, "#fff9db", stroke="#adb5bd", stroke_width=2, rot=r.uniform(0, 180)))
    S.add(g([trait(400 + dx, 470, 400 + dx * 1.3, 400, "#adb5bd", 3, opacity=0.6) for dx in (-120, -40, 40, 120)]))
    S.add(texte(400, 180, "Ça danse !", 70, "#7048e8", contour="#fff"))
    return S


def p04():
    S = Scene()
    pre(S, 4)
    S.add(pompon(400, 770, 2.1, expr="chante", bras="pense"))
    for sgn in (-1, 1):
        S.add(chemin(f"M {400 + sgn * 70} 560 q {sgn * 12} 10 0 20 q {sgn * -12} 10 0 20", stroke=ONDE, sw=4))
    S.add(notes(560, 250, 1.3, "#7048e8"), notes(140, 300, 1.0, "#7048e8"))
    S.add(texte(640, 400, "Laaa !", 64, "#7048e8", contour="#fff"))
    return S


def boite_elastique(x, y, s=1.0, epais=6, flou=False, couleur="#e64980"):
    m = [rect(-170, -70, 340, 70, "#d9a066", rx=8), ellipse(0, -70, 60, 16, "#8a5a33")]
    if flou:
        for k, dy in enumerate((-18, -9, 9, 18)):
            m.append(chemin(f"M -170 -72 Q 0 {-72 + dy * 2} 170 -72", stroke=couleur, sw=epais, opacity=0.35))
    m.append(chemin("M -170 -72 L 170 -72", stroke=couleur, sw=epais))
    return place(m, x, y, s)


def p05():
    S = Scene()
    interieur(S, "#f3f0ff", "#e8c39e", y=600)
    S.add(table(400, 780, 600, 140, "#c68642"))
    S.add(boite_elastique(330, 640, 1.4, 9, flou=True))
    S.add(pompon(660, 800, 1.6, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(texte(360, 300, "Twang !", 80, "#e64980", contour="#fff", rot=-4))
    return S


def p06():
    S = Scene()
    fond(S, "#fff5f5")
    # gros élastique : vibration lente, ondes longues (grave) ; fin élastique tendu : ondes courtes (aigu)
    S.add(rect(40, 110, 340, 280, "#e7f5ff", rx=24), rect(420, 110, 340, 280, "#fff0f6", rx=24))
    S.add(sinus(70, 260, 280, 60, 280, "#1c7ed6", 8))
    S.add(sinus(450, 260, 280, 22, 40, "#e64980", 5))
    S.add(texte(210, 170, "bôôm", 56, "#1c7ed6"), texte(590, 170, "ting !", 56, "#e64980"))
    S.add(texte(210, 360, "grave", 40, "#1c7ed6"), texte(590, 360, "aigu", 40, "#e64980"))
    S.add(boite_elastique(210, 620, 0.85, 16, couleur="#1c7ed6"), boite_elastique(590, 620, 0.85, 4, couleur="#e64980"))
    S.add(pompon(400, 790, 1.2, expr="content", bras="ouverts"))
    return S


def p07():
    S = Scene()
    interieur(S, "#e6fcf5", "#e8c39e", y=560)
    S.add(table(330, 780, 600, 120, "#c68642"))
    notes_ = ["do", "ré", "mi", "fa", "sol"]
    cols = ["#fa5252", "#ff922b", "#fcc419", "#51cf66", "#339af0"]
    # la bouteille la plus remplie vibre le plus lentement : c'est la plus grave
    for k in range(5):
        S.add(bouteille(110 + k * 110, 640, 0.62 - k * 0.11, cols[k], 0.95, notes_[k]))
    S.add(pompon(710, 800, 1.35, expr="rire", bras="montre", flip=True, regard=(-1, 0)))
    hx, hy = min(mains(710, 800, 1.35, "montre", True), key=lambda p: p[1])
    S.add(trait(hx, hy, 570, 500, "#adb5bd", 8), ellipse(566, 494, 14, 18, "#adb5bd"))
    S.add(notes(420, 200, 1.2, "#e64980"))
    S.add(texte(110, 120, "grave", 40, "#868e96"), texte(560, 120, "aigu", 40, "#868e96"))
    S.add(fleche(190, 108, 490, 108, "#868e96", 5))
    return S


def p08():
    S = Scene()
    pre(S, 8)
    S.add(perso("souris", 150, 760, 1.1, expr="timide", bras="bouche", regard=(1, 0), **SOURIS))
    S.add(ondes(210, 560, 30, 2, 22, 0, 50, "#74c0fc", 3))
    S.add(texte(160, 440, "chut…", 44, "#74c0fc"))
    S.add(perso("ours", 560, 760, 1.8, expr="furieux", bras="ouverts", regard=(-1, 0)))
    S.add(ondes(560, 470, 90, 4, 50, -90, 110, ONDE, 10))
    S.add(texte(560, 150, "OUAAAH !", 80, ONDE, contour="#fff"))
    S.add(pompon(330, 770, 1.1, expr="oups", bras="tete", regard=(1, 0)))
    return S


def p09():
    S = Scene()
    pre(S, 9)
    S.add(ellipse(430, 690, 330, 100, "#1c7ed6"), ellipse(430, 686, 310, 88, "#4dabf7"))
    for k in range(4):
        S.add(ellipse(470, 690, 40 + k * 60, 12 + k * 17, "none", stroke="#e7f5ff", stroke_width=5, opacity=0.9 - k * 0.18))
    S.add(goutte(460, 630, 1.0, "#a5d8ff"), goutte(490, 620, 0.8, "#a5d8ff"))
    S.add(pompon(120, 700, 1.3, expr="rire", bras="salut", regard=(1, 1)))
    S.add(texte(560, 230, "Plouf !", 80, "#1c7ed6", contour="#fff"))
    return S


def p10():
    S = Scene()
    pre(S, 10)
    S.add(ondes(360, 610, 70, 6, 55, 0, 360, ONDE, 5, 0.7, cercles=True))
    S.add(tambour(360, 700, 0.9, vibre=True))
    S.add(perso("souris", 110, 780, 1.0, expr="content", regard=(1, 0), **SOURIS))
    S.add(perso("herisson", 690, 780, 1.1, expr="content", regard=(-1, 0)))
    S.add(pompon(490, 780, 0.95, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    return S


def p11():
    S = Scene()
    pre(S, 11)
    S.add(arbre(400, 620, 0.7))
    S.add(pompon(120, 770, 1.3, expr="rire", bras="bouche", regard=(1, 0)))
    S.add(perso("souris", 690, 770, 1.2, expr="surpris", bras="joues", regard=(-1, 0), **SOURIS))
    pot = lambda x, sgn: place(g([poly([(-22, -30), (22, -30), (16, 30), (-16, 30)], "#fff", stroke="#ced4da", stroke_width=3)]), x, 0, rot=sgn * 90)
    S.add(place(pot(0, -1), 175, 610), place(pot(0, 1), 640, 610))
    S.add(trait(205, 610, 610, 610, "#495057", 3))
    S.add(ondes(300, 610, 10, 3, 14, 0, 70, ONDE, 3), ondes(460, 610, 10, 3, 14, 0, 70, ONDE, 3))
    S.add(texte(330, 480, "Allô ?", 60, "#7048e8", contour="#fff"))
    return S


def p12():
    S = Scene()
    pre(S, 12, "#ffd8a8", "#fff4e6")
    for k, x in enumerate((560, 640, 720)):
        S.add(cheval(x, 600, 0.45, ["#8d5524", "#495057", "#c68642"][k], flip=True))
    S.add(g([chemin(f"M {540 - k * 90} {640 + k * 25} q 10 -12 20 0 q 10 12 20 0", stroke="#a0693a", sw=4) for k in range(4)]))
    S.add(place(pompon(0, 0, 1.3, expr="concentre", bras="bas"), 250, 700, rot=-80))
    S.add(texte(620, 480, "tagada, tagada…", 44, "#a0693a", contour="#fff"))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(poly([(420, 800), (560, 120), (700, 240), (840, 80), (840, 800)], "#868e96"))
    S.add(poly([(560, 120), (620, 180), (590, 240), (540, 220)], "#fff"))
    sol(S, 680, "#8ce99a", bosse=6)
    S.add(pompon(160, 760, 1.4, expr="chante", bras="bouche", regard=(1, 0)))
    S.add(fleche(250, 420, 490, 330, "#7048e8", 6), texte(330, 330, "Coucou !", 50, "#7048e8", contour="#fff"))
    S.add(fleche(490, 400, 260, 500, "#b197fc", 4), texte(380, 520, "…coucou…", 36, "#b197fc", contour="#fff"))
    return S


def p14():
    S = Scene()
    nuit(S, "#141c3a", "#34427a")
    etoiles(S, 40, 14, (0, 0, 800, 500))
    S.add(lune_phase(680, 110, 40, 1.0))
    for k in range(7):
        S.add(place(poly([(-50, 0), (0, -200 - (k % 3) * 40), (50, 0)], "#101733"), k * 130, 800))
    S.add(chauve_souris(220, 380, 1.4, expr="content", regard=(1, 0)))
    S.add(ondes(250, 380, 60, 4, 40, 0, 50, "#ffe066", 4))
    S.add(ondes(580, 380, 40, 3, 40, 180, 40, "#ffa94d", 3, 0.7))
    S.add(papillon(600, 380, 1.0, "#a0693a", "#e8c39e"))
    return S


def p15():
    S = Scene()
    ciel(S, "#343a40", "#868e96")
    S.add(nuage(560, 130, 1.6, "#495057", ombre="#343a40"), nuage(200, 110, 1.3, "#495057", ombre="#343a40"))
    S.add(poly([(600, 190), (560, 330), (600, 330), (550, 480), (650, 300), (610, 300), (650, 190)], "#ffe066"))
    collines(S, 620, "#5c7c6a", graine=15)
    sol(S, 620, "#6a8f76")
    S.add(maison(170, 700, 0.8, lumiere=True))
    S.add(pompon(360, 780, 1.4, expr="concentre", bras="montre", regard=(1, -1)))
    S.add(texte(180, 300, "1… 2… 3…", 50, "#fff"))
    S.add(texte(600, 700, "BRRROUM !", 64, "#ffe066", contour="#343a40", rot=-4))
    return S


def p16():
    S = Scene()
    fond(S, "#5f3dc4")
    S.add(poly([(0, 0), (160, 0), (220, 620), (0, 620)], "#e03131"), poly([(800, 0), (640, 0), (580, 620), (800, 620)], "#e03131"))
    for k in range(9):
        S.add(cercle(60 + k * 85, 40, 12, ["#ffe066", "#ff8787", "#74c0fc"][k % 3]))
    S.add(rect(0, 620, 800, 180, "#a0693a"))
    S.add(tambour(160, 740, 0.7))
    S.add(perso("herisson", 280, 740, 1.0, expr="rire", bras="haut"))
    S.add(pompon(420, 740, 1.4, expr="chante", bras="ouverts"))
    S.add(perso("souris", 570, 740, 1.0, expr="rire", bras="haut", **SOURIS))
    S.add(perso("ours", 690, 740, 1.2, expr="chante", bras="ouverts"))
    S.add(notes(300, 200, 1.3, "#ffe066"), notes(520, 260, 1.1, "#ffe066"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pompon-seul.svg", vignette),
    ("01-grandes-oreilles.svg", p01), ("02-tambour.svg", p02), ("03-riz.svg", p03), ("04-gorge.svg", p04),
    ("05-elastique.svg", p05), ("06-grave-aigu.svg", p06), ("07-bouteilles.svg", p07), ("08-fort-doux.svg", p08),
    ("09-ronds-dans-l-eau.svg", p09), ("10-dans-l-air.svg", p10), ("11-telephone.svg", p11), ("12-oreille-au-sol.svg", p12),
    ("13-echo.svg", p13), ("14-chauve-souris.svg", p14), ("15-orage.svg", p15), ("16-concert.svg", p16),
]
