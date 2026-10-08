"""La chauve-souris voit avec ses oreilles — l'écholocation.

La chauve-souris (ici une pipistrelle) est un mammifère volant : son aile est
une main, avec une peau fine tendue entre de très longs doigts. Le jour, elle
dort la tête en bas, accrochée par les pieds. La nuit, elle pousse des cris
trop aigus pour nos oreilles (des ultrasons) ; l'écho qui revient lui dit où
sont les obstacles et les insectes. Elle mange des centaines d'insectes par
nuit. Les mamans élèvent un seul petit par an, qui boit leur lait. L'hiver,
sans insectes, elle hiberne dans une grotte.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import chauve_souris, ondes, fleche, enfant

ID = "chauve-souris-nuit"
BRUN = "#8a6a50"
AILE = "#5c4636"


# --- Personnages ------------------------------------------------------------

def pipistrelle(x, y, s=1.0, expr="sourire", ailes="ouvertes", flip=False, regard=(0, 0), bouche_ouverte=False):
    """Chauve-souris en vol, vue de face (dessin de sciences.py, en brun)."""
    m = [chauve_souris(0, 0, 1.0, expr=expr if not bouche_ouverte else "chante", couleur=BRUN, ailes=ailes, regard=regard)]
    return place(m, x, y, s, flip=flip)


def pendue(x, y, s=1.0, expr="dort", bebe=False, rot=0):
    """Chauve-souris endormie, pendue la tête en bas, enveloppée dans ses
    ailes ; (x, y) = l'endroit où ses pieds s'accrochent."""
    m = [chemin("M -8 0 Q -10 10 -6 18", stroke=ENCRE, sw=3), chemin("M 8 0 Q 10 10 6 18", stroke=ENCRE, sw=3)]
    m.append(ellipse(0, 62, 32, 50, AILE))
    m.append(chemin("M -28 40 Q -6 60 -14 104 M 28 40 Q 6 60 14 104", stroke=_assombrir(AILE, 0.8), sw=3))
    m.append(ellipse(0, 70, 16, 30, BRUN))
    if bebe:
        m.append(place(g([ellipse(0, 0, 12, 16, "#b08a6a"), cercle(0, 18, 10, "#b08a6a"),
                          oeil(-4, 20, "fermes", taille=0.4), oeil(4, 20, "fermes", taille=0.4)]), 0, 66))
    for sgn in (-1, 1):
        m.append(poly([(sgn * 8, 120), (sgn * 28, 150), (sgn * 24, 112)], BRUN))
    m.append(cercle(0, 112, 24, BRUN))
    style = "fermes" if expr == "dort" else "normal"
    m.append(oeil(-9, 118, style, taille=0.6) + oeil(9, 118, style, taille=0.6))
    m.append(joue(-16, 108, 0.5) + joue(16, 108, 0.5))
    m.append(place(bouche(0, 0, "petit_sourire", 0.6), 0, 100, rot=180))
    return place(m, x, y, s, rot=rot)


def grenier(S, nuit_=False):
    """Grenier sous le toit : poutres en triangle, lucarne."""
    S.add(rect(0, 0, 800, 800, "#5c4033" if not nuit_ else "#2b2238"))
    S.add(poly([(0, 0), (400, 0), (0, 420)], "#7c5a3c"))
    S.add(poly([(800, 0), (400, 0), (800, 420)], "#7c5a3c"))
    S.add(rect(0, 130, 800, 34, "#a0693a"))
    for x in (120, 680):
        S.add(rect(x - 16, 164, 32, 636, "#8d5524"))
    S.add(rect(0, 700, 800, 100, "#6d4424"))
    S.add(g([rect(0, 700 + k * 26, 800, 3, "#5c3a1e") for k in range(4)]))


def grotte_(S):
    S.add(rect(0, 0, 800, 800, "#343a40"))
    S.add(ellipse(400, 470, 460, 380, "#495057"))
    S.add(chemin("M 0 0 L 800 0 L 800 140 Q 600 100 400 130 Q 200 100 0 140 Z", "#212529"))
    for x, h in [(140, 90), (260, 60), (520, 110), (660, 70)]:
        S.add(poly([(x - 20, 120), (x + 20, 120), (x, 120 + h)], "#212529"))
    S.add(chemin("M 0 700 Q 200 670 400 700 T 800 690 L 800 800 L 0 800 Z", "#212529"))


def crepuscule(S, y=600):
    S.add(rect(0, 0, 800, 800, S.degrade(["#364fc7", "#9775fa", "#ffa8a8"])))
    S.add(cercle(160, 150, 40, "#fff3bf", opacity=0.9))
    etoiles(S, 18, 4, (0, 0, 800, 300))
    S.add(rect(0, y, 800, 800 - y, "#2b2238"))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    crepuscule(S, 640)
    S.add(maison(640, 660, 1.1, mur="#4c4057", toit="#2b2238", fenetre="#ffe066", lumiere=True))
    S.add(arbre(110, 660, 1.2, "#2b3a55", "#33415c", "#2b2238"))
    S.add(pipistrelle(380, 430, 2.4, expr="rire"))
    S.add(ondes(500, 420, 30, 3, 30, -10, 60, "#fff3bf", 5))
    S.add(papillon_nuit(690, 330, 1.0, 20))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trait(80, 20, 320, 20, "#8d5524", 12))
    S.add(pendue(140, 26, 1.0), pendue(260, 26, 1.0, bebe=True))
    return S


def p01():
    S = Scene()
    grenier(S)
    for k, x in enumerate([230, 340, 460, 570]):
        S.add(pendue(x, 164, 1.7 if k % 2 else 1.55))
    S.add(zzz(640, 420, 1.0, "#ffd8a8"))
    S.add(rect(330, 470, 140, 110, "#a5d8ff", rx=8), soleil(400, 520, 24, rayons=False), rect(396, 470, 8, 110, "#8d5524"))
    return S


def os_aile(cx, cy, s=1.0):
    """Squelette d'une aile de chauve-souris sous la peau : bras, pouce,
    quatre longs doigts ; (cx, cy) = épaule."""
    m = [chemin("M 0 0 L 120 60 L 140 70 L 300 -60 L 140 70 L 330 20 L 140 70 L 300 160 L 140 70 L 220 230 L 140 70 Z", "none"),
         poly([(0, 0), (140, 70), (300, -60), (330, 20), (300, 160), (220, 230), (40, 200), (0, 120)], AILE, opacity=0.55)]
    for px, py in [(300, -60), (330, 20), (300, 160), (220, 230)]:
        m.append(trait(140, 70, px, py, "#fff4e6", 7))
    m.append(trait(0, 0, 140, 70, "#fff4e6", 9))
    m.append(trait(140, 70, 150, 30, "#fff4e6", 6))
    m.append(chemin("M 150 30 q 6 -10 -4 -14", stroke="#fff4e6", sw=4))
    return place(m, cx, cy, s)


def main_enfant(x, y, s=1.0):
    m = [ellipse(0, 0, 50, 56, "#f3c9a4")]
    for k, (a, L) in enumerate([(-150, 60), (-110, 80), (-90, 88), (-70, 80), (-50, 66)]):
        r = math.radians(a)
        m.append(trait(math.cos(r) * 30, math.sin(r) * 30, math.cos(r) * (30 + L), math.sin(r) * (30 + L), "#f3c9a4", 26))
    return place(m, x, y, s)


def p02():
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(os_aile(80, 300, 1.4))
    S.add(cercle(80, 300, 44, BRUN))
    S.add(etiquette(250, 200, "le pouce", 32, "#5f3dc4"), etiquette(520, 520, "les doigts", 32, "#5f3dc4"))
    S.add(main_enfant(640, 640, 1.0))
    S.add(etiquette(640, 760, "ta main", 32, "#e8590c"))
    S.cachette(570, 70, "air")
    return S


def p03():
    S = Scene()
    crepuscule(S, 620)
    S.add(maison(400, 640, 1.6, mur="#4c4057", toit="#2b2238", fenetre="#ffe066", lumiere=True))
    for x, y, sc in [(330, 300, 0.9), (480, 230, 0.7), (620, 160, 0.55), (200, 200, 0.5)]:
        S.add(pipistrelle(x, y, sc, expr="content"))
    return S


def p04():
    S = Scene()
    nuit(S)
    etoiles(S, 30, 2)
    S.add(lune(660, 120, 40))
    S.add(pipistrelle(260, 400, 2.2, expr="chante", regard=(1, 0)))
    S.add(ondes(380, 400, 50, 4, 50, 0, 70, "#ffd43b", 7))
    S.add(texte(560, 650, "« Iiiiii ! »", 48, "#ffd43b"))
    S.cachette(730, 240, "air")
    return S


def p05():
    S = Scene()
    nuit(S)
    etoiles(S, 20, 6)
    S.add(pipistrelle(180, 420, 1.6, expr="concentre", regard=(1, 0)))
    S.add(ondes(250, 420, 50, 4, 60, 0, 60, "#ffd43b", 6))
    S.add(moustique(600, 410, 2.4))
    S.add(ondes(570, 410, 40, 3, 50, 180, 60, "#74c0fc", 6))
    S.add(etiquette(420, 600, "le cri part…", 34, "#ffd43b", fond="#1c2a52"))
    S.add(etiquette(420, 660, "… l'écho revient !", 34, "#74c0fc", fond="#1c2a52"))
    S.cachette(730, 230, "air")
    return S


def p06():
    S = Scene()
    nuit(S)
    etoiles(S, 25, 7)
    S.add(lune(130, 120, 40))
    S.add(lampe_(640, 800))
    r = random.Random(6)
    for _ in range(9):
        S.add(moustique(r.uniform(420, 760), r.uniform(150, 450), r.uniform(0.8, 1.2), r.uniform(-20, 20)))
    S.add(papillon_nuit(560, 300, 1.2, -20))
    S.add(pipistrelle(330, 380, 1.9, expr="miam", regard=(1, 0)))
    S.add(texte(250, 650, "Miam !", 56, "#ffd43b"))
    S.cachette(730, 240, "air")
    return S


def lampe_(x, y):
    return g([rect(x - 8, y - 500, 16, 500, "#495057"), rect(x - 50, y - 520, 100, 26, "#343a40", rx=10),
              poly([(x - 40, y - 494), (x + 40, y - 494), (x + 160, y - 100), (x - 160, y - 100)], "#fff3bf", opacity=0.18)])


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    montagnes_fond(S, 520)
    S.add(rect(0, 520, 800, 280, "#8ce99a"))
    S.add(enfant(200, 740, 1.6, expr="joie", bras="bouche", habit="#9775fa", jambes="#364fc7", regard=(1, -0.5)))
    S.add(texte(380, 380, "Ohé !", 60, "#5f3dc4", contour="#fff"))
    S.add(texte(470, 560, "… ohé !", 40, "#9775fa", contour="#fff"))
    S.add(fleche(330, 420, 560, 300, "#5f3dc4", 6, 22), fleche(600, 360, 400, 480, "#9775fa", 6, 22))
    return S


def p08():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#ffd8a8", "#fff9db"])))
    S.add(soleil(150, 520, 60))
    S.add(maison(500, 760, 1.9, mur="#ffe8cc", toit="#c92a2a"))
    S.add(pipistrelle(560, 230, 0.9, expr="baille"))
    S.add(fleche(620, 260, 640, 360, "#5c4636", 5, 18))
    S.add(texte(250, 170, "Bonne nuit !", 50, "#5f3dc4", contour="#fff"))
    S.cachette(200, 730, "air")
    return S


def p09():
    S = Scene()
    grenier(S)
    for k, x in enumerate([250, 400, 550]):
        S.add(pendue(x, 164, 2.0, bebe=True, expr="sourire" if k == 1 else "dort"))
    S.add(coeur(400, 560, 1.5, "#ff8787"))
    return S


def p10():
    S = Scene()
    grotte_(S)
    for k, x in enumerate([260, 400, 540]):
        S.add(pendue(x, 132 + (k % 2) * 10, 1.6))
    S.add(zzz(640, 380, 1.2, "#ced4da"))
    S.add(texte(400, 600, "Chut…", 60, "#ced4da"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chauves-souris-seules.svg", vignette),
    ("01-le-jour.svg", p01), ("02-l-aile-main.svg", p02), ("03-le-soir.svg", p03),
    ("04-le-cri.svg", p04), ("05-l-echo.svg", p05), ("06-la-chasse.svg", p06),
    ("07-et-toi.svg", p07), ("08-le-matin.svg", p08), ("09-les-bebes.svg", p09),
    ("10-l-hiver.svg", p10),
]
