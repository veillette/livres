"""Tilou a froid aux pattes — la chaleur, les conducteurs et les isolants.

La chaleur passe toujours du chaud vers le froid (flèches orange). Le métal
la conduit vite, le bois mal ; l'air immobile (plumes, poils, couches de
vêtements, murs épais) isole. Un isolant ne fabrique pas de chaleur : le
glaçon emmitouflé fond moins vite. Le noir absorbe la lumière du soleil.
"""
from base import *
from objets import *
from sciences import *

ID = "tilou-chaleur"
TILOU = dict(acc=("bonnet", "echarpe"), couleur_acc="#1c7ed6")
MAMAN = dict(couleur="#9c6644", acc=("tablier",), couleur_acc="#e64980")
PAPA = dict(couleur="#7a4a2a", acc=("lunettes",))
MIMI = dict(acc=("noeud",), couleur_acc="#f783ac")
CHAUD = "#f76707"


def tilou(x, y, s=1.0, **k):
    return perso("castor", x, y, s, **{**TILOU, **k})


def tilou_maison(x, y, s=1.0, **k):
    return perso("castor", x, y, s, **k)


def maman(x, y, s=1.25, **k):
    return perso("castor", x, y, s, **{**MAMAN, **k})


def papa(x, y, s=1.3, **k):
    return perso("castor", x, y, s, **{**PAPA, **k})


def mimi(x, y, s=0.7, **k):
    return perso("castor", x, y, s, **{**MIMI, **k})


def chaleur(x, y, s=1.0, nb=3, couleur=CHAUD):
    """Petites volutes de chaleur montantes ; (x, y) = bas."""
    return place([chemin(f"M {k * 22 - (nb - 1) * 11} 0 q -10 -20 0 -40 q 10 -20 0 -40", stroke=couleur, sw=5, opacity=0.8)
                  for k in range(nb)], x, y, s)


def hiver(S, graine=1):
    ciel(S, "#d0ebff", "#f1f3f5")
    S.add(sapin(110, 560, 0.9, neige=True), sapin(700, 560, 1.0, neige=True), sapin(610, 540, 0.7, neige=True))
    S.add(rect(0, 560, 800, 240, "#ffffff"))
    S.add(chemin("M 0 560 Q 200 530 400 560 Q 600 590 800 555 L 800 600 L 0 600 Z", "#f8f9fa"))
    flocons(S, 30, graine, (0, 0, 800, 540))


def cuisine(S):
    interieur(S, "#fff4e6", "#c68642", 600, papier="#ffe8cc")
    S.add(fenetre(570, 90, 170, 150, "#d0ebff", rideaux="#ff8787",
                  contenu=g([rect(570, 200, 170, 40, "#fff"), sapin(640, 220, 0.4, neige=True)])))


def chocolat(x, y, s=1.0, cuilleres=False):
    m = [chemin("M -50 -80 L 50 -80 L 42 0 L -42 0 Z", "#ff8787"),
         ellipse(0, -80, 50, 12, "#7c4a1e"),
         chemin("M 48 -64 Q 84 -56 46 -24", stroke="#ff8787", sw=10)]
    if cuilleres:
        m.insert(0, place(rect(-7, -150, 14, 150, "#adb5bd", rx=7), -18, -70, rot=-14))
        m.insert(0, place(rect(-8, -150, 16, 150, "#c68642", rx=8), 20, -70, rot=14))
    return place(m, x, y, s)


def mitaine(x, y, s=1.0, couleur="#e03131", rot=0):
    m = [chemin("M -40 40 L -44 -40 Q -44 -80 0 -80 Q 40 -80 40 -40 L 40 40 Z", couleur),
         ellipse(-50, -20, 18, 28, couleur, rot=-30),
         rect(-46, 30, 92, 26, "#fff", rx=8),
         g([trait(-30 + k * 20, -60, -30 + k * 20, 20, "#fff", 3, opacity=0.35) for k in range(4)])]
    return place(m, x, y, s, rot=rot)


def glacon_cube(x, y, s=1.0, fondu=0.0):
    h = 70 * (1 - fondu)
    w = 70 * (1 - fondu * 0.5)
    m = []
    if fondu:
        m.append(ellipse(0, 0, 50 + fondu * 60, 12 + fondu * 6, "#a5d8ff", opacity=0.8))
    m += [rect(-w / 2, -h, w, h, "#e7f5ff", rx=10, stroke="#74c0fc", stroke_width=4),
          rect(-w / 2 + 8, -h + 8, w * 0.3, h * 0.3, "#fff", rx=4)]
    return place(m, x, y, s)


def thermometre(x, y, s=1.0, niveau=0.5):
    m = [rect(-22, -330, 44, 330, "#f8f9fa", rx=22, stroke="#adb5bd", stroke_width=4),
         cercle(0, 10, 38, "#fa5252", stroke="#adb5bd", stroke_width=4),
         rect(-9, -300 * niveau - 10, 18, 300 * niveau + 30, "#fa5252", rx=9)]
    m += [trait(22, -40 - k * 50, 40, -40 - k * 50, "#868e96", 3) for k in range(6)]
    return place(m, x, y, s)


def tshirt(x, y, s=1.0, couleur="#212529"):
    m = [poly([(-50, -60), (-90, -30), (-70, 0), (-50, -14), (-50, 60), (50, 60), (50, -14), (70, 0), (90, -30), (50, -60), (20, -60), (0, -44), (-20, -60)], couleur,
              stroke="#adb5bd", stroke_width=3)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    hiver(S, 2)
    S.add(tilou(400, 760, 1.9, expr="rire", bras="porte", objet=chocolat(0, -40, 0.75)))
    S.add(paillettes(200, 300), paillettes(600, 260, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tilou(200, 264, 1.0, expr="content", bras="porte", objet=chocolat(0, -40, 0.75)))
    return S


def p01():
    S = Scene()
    hiver(S, 1)
    S.add(g([cercle(560 + k * 22, 700 - (k % 2) * 10, 18, "#fff", stroke="#dee2e6", stroke_width=2) for k in range(5)]))
    S.add(tilou(330, 760, 1.7, expr="triste", bras="calin", regard=(0, 1)))
    S.add(cercle(330, 525, 9, "#fa5252"))
    S.add(texte(560, 300, "Brrr !", 90, "#1c7ed6", contour="#fff", rot=-6))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(maman(600, 690, 1.3, expr="sourire", bras="bas", regard=(-1, 0.3)))
    S.add(tilou_maison(300, 760, 1.4, expr="content", bras="porte", acc=("echarpe",), couleur_acc="#1c7ed6",
                       objet=chocolat(0, -40, 0.8)))
    S.add(table(380, 790, 560, 120, "#a0693a"))
    S.add(texte(250, 230, "Ahhh…", 72, CHAUD, contour="#fff"))
    return S


def p03():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(chocolat(400, 620, 2.6, cuilleres=True))
    S.add(chaleur(400, 360, 1.3))
    S.add(texte(190, 240, "métal", 50, "#495057"), fleche(200, 260, 320, 330, "#495057", 6, 20))
    S.add(texte(620, 240, "bois", 50, "#a0693a"), fleche(610, 260, 470, 330, "#a0693a", 6, 20))
    S.add(texte(160, 420, "Aïe !", 70, "#e03131", contour="#fff", rot=-8))
    S.add(texte(650, 420, "tiède", 44, "#a0693a"))
    S.cachette(400, 70, "air")
    return S


def p04():
    S = Scene()
    hiver(S, 4)
    # rampe en fer et banc en bois
    S.add(rect(80, 470, 300, 14, "#868e96", rx=7), rect(100, 470, 12, 160, "#868e96"), rect(350, 470, 12, 160, "#868e96"))
    S.add(rect(470, 560, 260, 26, "#c68642", rx=6), rect(470, 520, 260, 22, "#c68642", rx=6),
          rect(490, 586, 14, 60, "#a0693a"), rect(696, 586, 14, 60, "#a0693a"))
    S.add(tilou(240, 780, 1.1, expr="surpris", bras="haut"))
    S.add(texte(240, 400, "Glacé !", 54, "#1c7ed6", contour="#fff"))
    S.add(tilou(600, 780, 1.1, expr="sourire", bras="bas"))
    S.add(texte(600, 470, "Moins froid", 46, "#a0693a", contour="#fff"))
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(tilou_maison(120, 700, 1.0, expr="surpris", bras="pense", regard=(1, 0.5)))
    S.add(maman(690, 700, 1.05, expr="malin", bras="montre", regard=(-1, 0.5)))
    S.add(table(400, 790, 560, 150, "#a0693a", nappe="#e7f5ff"))
    S.add(assiette(280, 625, 1.3), glacon_cube(280, 630, 1.0))
    S.add(mitaine(510, 590, 1.0, "#e03131"), glacon_cube(510, 560, 0.5))
    S.add(pensee(260, 200, 60, texte(260, 225, "?", 70, "#7048e8"), depuis=(150, 420)))
    S.cachette(350, 730, "air")
    return S


def p06():
    S = Scene()
    cuisine(S)
    S.add(horloge(400, 260, 50, heure=4))
    S.add(table(400, 790, 640, 150, "#a0693a", nappe="#e7f5ff"))
    S.add(assiette(250, 625, 1.3), glacon_cube(250, 630, 1.0, fondu=0.8))
    S.add(mitaine(560, 600, 1.0, "#e03131", rot=-10))
    S.add(place(glacon_cube(0, 0, 1.0, 0.1), 560, 640, 0.9))
    S.add(texte(250, 470, "fondu", 50, "#1c7ed6"), texte(560, 450, "presque pas !", 46, "#e03131"))
    return S


def p07():
    S = Scene()
    hiver(S, 7)
    S.add(trait(80, 420, 720, 420, "#8d5524", 18), trait(500, 420, 620, 340, "#8d5524", 10))
    S.add(place(mesange(0, 0, 3.0, expr="content"), 400, 410, 1.0, sy=None))
    S.add(cercle(400, 280, 120, "#339af0", opacity=0.15))
    S.add(texte(400, 640, "Toute ronde !", 64, "#1c7ed6", contour="#fff"))
    return S


def p08():
    S = Scene()
    interieur(S, "#e7f5ff", "#c68642", 600, papier="#d0ebff")
    for k, (c, mot) in enumerate([("#ffd43b", "maillot"), ("#69db7c", "pull"), ("#4c6ef5", "manteau")]):
        x = 470 + k * 110
        S.add(tshirt(x, 300, 0.6 + k * 0.08, c), texte(x, 400, mot, 30, "#495057"))
        S.add(cercle(x, 210, 22, "#fff", stroke="#495057", stroke_width=3), texte(x, 220, str(k + 1), 28, "#495057"))
    S.add(tilou(220, 780, 1.6, expr="fier", bras="hanches", habit="#4c6ef5"))
    return S


def p09():
    S = Scene()
    ciel(S, "#d0ebff", "#f1f3f5")
    flocons(S, 20, 9, (0, 0, 800, 300))
    S.add(rect(0, 520, 800, 280, "#4dabf7"), rect(0, 520, 800, 20, "#e7f5ff"))
    # hutte en coupe
    S.add(chemin("M 120 640 Q 140 250 400 230 Q 660 250 680 640 Z", "#8d5524"))
    S.add(g([trait(150 + k * 40, 620 - (k % 3) * 120, 220 + k * 38, 380 + (k % 2) * 40, "#6d4424", 10) for k in range(12)]))
    S.add(chemin("M 220 520 Q 240 350 400 340 Q 560 350 580 520 Z", "#ffe8cc"))
    S.add(rect(220, 500, 360, 30, "#d9a066"))
    S.add(chemin("M 120 255 Q 400 170 680 255 Q 640 230 400 215 Q 160 230 120 255", "#fff"))
    S.add(rect(560, 540, 70, 100, "#1c7ed6", opacity=0.6))
    S.add(maman(300, 510, 0.75, expr="content"), tilou_maison(410, 510, 0.6, expr="rire", bras="haut"), mimi(490, 510, 0.45, expr="content"))
    S.add(texte(130, 160, "Il gèle !", 44, "#1c7ed6", anchor="start"))
    S.add(texte(400, 300, "Bien au chaud", 34, CHAUD))
    S.cachette(570, 730, "air")
    return S


def p10():
    S = Scene()
    hiver(S, 10)
    S.add(soleil(680, 110, 60))
    S.add(tshirt(260, 640, 1.2, "#212529"), tshirt(540, 640, 1.2, "#ffffff"))
    S.add(chaleur(260, 540, 1.2))
    S.add(rayons_soleil(640, 160, 290, 560, nb=2), rayons_soleil(650, 160, 540, 560, nb=2))
    S.add(fleche(560, 560, 640, 420, "#fcc419", 5, 18))
    S.add(tilou(400, 790, 0.7, expr="surpris", bras="montre"))
    return S


def p11():
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(rect(400, 60, 6, 680, "#dee2e6"))
    S.add(thermometre(200, 640, 1.2, 0.85), thermometre(600, 640, 1.2, 0.2))
    S.add(soleil(200, 120, 45, visage=True), g([flocons_un(600 + dx, 110 + dy) for dx, dy in [(-40, 0), (30, -20), (10, 30)]]))
    S.add(texte(200, 760, "chaud", 52, "#e03131"), texte(600, 760, "froid", 52, "#1c7ed6"))
    S.add(fleche(300, 500, 300, 330, "#e03131", 7, 22), fleche(700, 330, 700, 500, "#1c7ed6", 7, 22))
    S.cachette(470, 160, "air")
    return S


def flocons_un(x, y, s=1.0):
    return place([trait(-20 * c, -20 * d, 20 * c, 20 * d, "#74c0fc", 5) for c, d in [(1, 0), (0.5, 0.87), (-0.5, 0.87)]], x, y, s)


def glaciere(x, y, s=1.0):
    m = [rect(-130, -160, 260, 160, "#1c7ed6", rx=16), rect(-140, -190, 280, 46, "#e7f5ff", rx=12),
         rect(-60, -214, 120, 24, "#e7f5ff", rx=10), rect(-110, -130, 220, 14, "#fff", opacity=0.25)]
    return place(m, x, y, s)


def p12():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(680, 110, 55, visage=True))
    collines(S, 520, "#b2f2bb", graine=12)
    sol(S, 560, "#8ce99a")
    S.add(tapis(360, 700, 260, 60, "#ffc9c9", "#ff8787"))
    S.add(glaciere(360, 680, 1.0))
    S.add(texte(360, 450, "Bien frais !", 54, "#1c7ed6", contour="#fff"))
    S.add(tilou_maison(650, 780, 1.0, expr="joie", bras="haut", habit="#ffd43b"))
    S.add(pensee(170, 220, 70, ""), texte(170, 238, "été", 40, "#f08c00"))
    return S


def p13():
    S = Scene()
    interieur(S, "#3b4a7a", "#8d6e63", 600, papier="#34426e")
    S.add(fenetre(250, 120, 300, 260, "#1c2a52", nuit_=True, contenu=g([rect(250, 330, 300, 50, "#fff")])))
    S.add(chemin("M 210 100 L 330 100 Q 300 250 340 410 L 210 410 Z", "#e64980"),
          chemin("M 590 100 L 470 100 Q 500 250 460 410 L 590 410 Z", "#e64980"),
          rect(190, 90, 420, 14, "#adb5bd", rx=7))
    S.add(lampe(680, 600, 1.0, allumee=True))
    S.add(tilou_maison(400, 770, 1.3, expr="content", bras="large", habit="#9775fa"))
    return S


def bouillotte(x, y, s=1.0):
    return place([rect(-60, -80, 120, 140, "#ff6b6b", rx=36), rect(-18, -110, 36, 40, "#fa5252", rx=6),
                  g([trait(-40, -40 + k * 24, 40, -40 + k * 24, "#fff", 3, opacity=0.4) for k in range(4)])], x, y, s)


def p14():
    S = Scene()
    interieur(S, "#e5dbff", "#c68642", 620, papier="#d0bfff")
    S.add(lit(420, 780, 480, "#74c0fc", "#4dabf7"))
    S.add(tilou_maison(300, 680, 0.8, expr="dort", habit="#9775fa"))
    S.add(lit_couverture(420, 780))
    S.add(papa(680, 640, 1.0, expr="sourire", bras="porte", objet=bouillotte(0, -50, 0.6), regard=(-1, 0.3)))
    return S


def lit_couverture(x, y):
    return rect(x - 230, y - 140, 460, 100, "#4dabf7", rx=24)


def p15():
    S = Scene()
    interieur(S, "#fff4e6", "#c68642", 620, papier="#ffe8cc")
    for k, c in enumerate(["#ffc9c9", "#b2f2bb", "#a5d8ff", "#ffec99"]):
        S.add(ellipse(360, 740 - k * 30, 230 - k * 30, 60, c, stroke="#fff", stroke_width=4))
    S.add(mimi(360, 690, 0.8, expr="dort"))
    S.add(rect(240, 640, 240, 60, "#ffd8a8", rx=30))
    S.add(tilou_maison(640, 780, 1.2, expr="fier", bras="porte", habit="#9775fa",
                       objet=place(rect(-70, -30, 140, 50, "#d0bfff", rx=20), 0, -40)))
    return S


def p16():
    S = Scene()
    hiver(S, 16)
    S.add(soleil(680, 100, 45))
    S.add(tilou(250, 770, 1.2, expr="rire", bras="tient", objet=""))
    S.add(cercle(330, 380, 26, "#fff", stroke="#dee2e6", stroke_width=3), mouvement(370, 400, 0.8, rot=180))
    S.add(mimi(560, 770, 0.9, expr="rire", bras="haut", acc=("bonnet", "noeud")))
    S.add(cercle(470, 300, 22, "#fff", stroke="#dee2e6", stroke_width=3))
    S.add(texte(400, 180, "Bataille !", 72, "#1c7ed6", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tilou-seul.svg", vignette),
    ("01-brrr.svg", p01), ("02-chocolat.svg", p02), ("03-deux-cuilleres.svg", p03), ("04-fer-et-bois.svg", p04),
    ("05-experience.svg", p05), ("06-la-mitaine.svg", p06), ("07-mesange.svg", p07), ("08-les-couches.svg", p08),
    ("09-la-hutte.svg", p09), ("10-noir-et-blanc.svg", p10), ("11-thermometre.svg", p11), ("12-glaciere.svg", p12),
    ("13-rideaux.svg", p13), ("14-bouillotte.svg", p14), ("15-nid-douillet.svg", p15), ("16-bataille.svg", p16),
]
