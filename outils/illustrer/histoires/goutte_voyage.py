"""Le voyage d'une goutte d'eau — le cycle de l'eau suivi par Plic.

Nuage → gouttes qui grossissent → pluie → ruisseau → rivière → (une partie
s'infiltre et nourrit les plantes) → mer salée → évaporation (la vapeur est
invisible, le sel reste dans la mer) → condensation en altitude, où il fait
froid → nouveau nuage. Expérience : la flaque qui rapetisse au soleil.
"""
from base import *
from objets import *
from sciences import *
from animaux import cycle, coupe_terre, racines, etiquette, disque
from fantastique import personne

ID = "goutte-voyage"
BLEU = "#339af0"


def plic(x, y, s=1.0, **k):
    k.setdefault("couleur", BLEU)
    return goutte_perso(x, y, s, **k)


def vapeur(x, y, s=1.0):
    """Plic devenue vapeur : un contour pointillé presque invisible."""
    return place([chemin("M 0 -110 Q 50 -40 44 -26 Q 34 0 0 0 Q -34 0 -44 -26 Q -50 -40 0 -110 Z", "#ffffff", stroke="#ffffff", sw=4,
                         opacity=0.5, stroke_dasharray="10 10"),
                  oeil(-11, -34, "heureux", taille=0.7), oeil(11, -34, "heureux", taille=0.7),
                  place(bouche(0, 0, "sourire", 0.6), 0, -20)], x, y, s)


def gouttelettes(S, zone, nb=40, graine=1, couleur="#a5d8ff", r=(4, 8)):
    rr = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        S.add(cercle(rr.uniform(x0, x1), rr.uniform(y0, y1), rr.uniform(*r), couleur, opacity=0.9))


def gros_nuage(x, y, s=1.0, couleur="#e9ecef", ombre="#ced4da"):
    return nuage(x, y, s, couleur, ombre=ombre)


def caillou_riviere(x, y, s=1.0):
    return g([ellipse(x, y, 40 * s, 24 * s, "#adb5bd"), ellipse(x - 8 * s, y - 8 * s, 18 * s, 8 * s, "#ced4da")])


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(gros_nuage(560, 300, 1.8, "#ffffff", "#dbe4ff"))
    pluie(S, 22, 2, zone=(430, 360, 720, 560))
    S.add(montagnes(None, 620, ("#9775fa", "#845ef7")))
    eau(S, 640, "#1c7ed6", "#4dabf7")
    S.add(plic(260, 600, 2.2, expr="rire"))
    S.add(soleil(110, 300, 45))
    S.cachette(70, 520, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(plic(200, 255, 1.9, expr="content"))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(gros_nuage(400, 380, 4.0, "#f1f3f5", "#dee2e6"))
    gouttelettes(S, (120, 260, 680, 520), 70, 1, "#a5d8ff", (4, 7))
    S.add(plic(400, 470, 0.9, expr="content", regard=(-1, 0)))
    S.add(texte(400, 120, "des milliards de gouttelettes", 36, "#1c7ed6", contour="#fff"))
    S.cachette(490, 730, "air")
    return S


def p02():
    S = Scene()
    ciel(S, "#868e96", "#ced4da")
    S.add(gros_nuage(400, 340, 4.2, "#adb5bd", "#868e96"))
    gouttelettes(S, (100, 230, 700, 450), 40, 2, "#d0ebff", (4, 7))
    # des gouttelettes viennent se coller à Plic, qui grossit
    for k, (dx, dy) in enumerate([(-150, -60), (150, -40), (-120, 80), (140, 90)]):
        S.add(cercle(400 + dx, 500 + dy, 12, "#a5d8ff"))
        S.add(fleche(400 + dx * 0.8, 500 + dy * 0.8, 400 + dx * 0.45, 500 + dy * 0.45, "#1c7ed6", 4, 12))
    S.add(plic(400, 590, 1.6, expr="surpris"))
    S.add(texte(400, 740, "lourde, lourde…", 48, "#1c7ed6", contour="#fff"))
    S.cachette(70, 330, "air")
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#d0ebff")
    S.add(gros_nuage(220, 110, 2.4, "#adb5bd", "#868e96"), gros_nuage(620, 90, 2.0, "#ced4da", "#adb5bd"))
    pluie(S, 70, 3, zone=(0, 160, 800, 620))
    S.add(montagnes(None, 760, ("#9775fa", "#845ef7"), neige=False))
    S.add(rect(0, 750, 800, 50, "#2f9e44"))
    S.add(plic(400, 520, 1.5, expr="rire", regard=(0, 1)))
    S.add(mouvement(400, 300, 1.4, "#1c7ed6", rot=90))
    S.add(texte(560, 380, "Ploc !", 70, "#1c7ed6", contour="#fff", rot=8))
    S.cachette(70, 90, "air")
    return S


def p04():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(montagnes(None, 420, ("#b197fc", "#9775fa")))
    S.add(rect(0, 400, 800, 400, "#69db7c"))
    # ruisseau qui descend en zigzag
    d = "M 470 400 Q 380 470 470 540 Q 560 610 400 680 Q 280 740 300 820"
    S.add(chemin(d, stroke="#4dabf7", sw=80))
    S.add(chemin(d, stroke="#a5d8ff", sw=16, stroke_dasharray="30 50"))
    for x, y in ((380, 520), (560, 600), (330, 650), (500, 470)):
        S.add(caillou_riviere(x, y, 0.8))
    S.add(sapin(140, 560, 0.9), sapin(680, 520, 0.8), sapin(700, 700, 1.0))
    S.add(plic(470, 615, 1.25, expr="rire", regard=(-1, 1)))
    S.add(texte(250, 470, "glou, glou !", 48, "#1c7ed6", contour="#fff", rot=-6))
    return S


def p05():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 430, "#b2f2bb", graine=4)
    S.add(rect(0, 420, 800, 120, "#8ce99a"))
    eau(S, 520, "#4dabf7", "#74c0fc")
    # pont de pierre
    S.add(chemin("M 120 420 L 680 420 L 680 560 L 580 560 A 180 130 0 0 0 220 560 L 120 560 Z", "#ced4da"))
    for k in range(6):
        S.add(rect(130 + k * 92, 432, 80, 26, "#dee2e6", rx=4))
    S.add(rect(110, 400, 580, 26, "#adb5bd", rx=6))
    S.add(plic(270, 690, 1.0, expr="content", regard=(1, 0)))
    S.add(poisson(560, 690, 0.8, "#ff922b", flip=True))
    S.add(canard(650, 560, 0.9, flip=True, regard=(-1, 0)))
    S.add(bulle(150, 140, 230, 80, "Bonjour !", 40, pointe=(260, 580)))
    S.cachette(730, 470, "air")
    return S


def p06():
    S = Scene()
    coupe_terre(S, 300, graine=5)
    S.add(fleur(300, 290, 1.4, "#e64980"), fleur(520, 290, 1.2, "#fab005"))
    S.add(racines(300, 300, 1.0), racines(520, 300, 0.9, graine=2))
    S.add(goutte_perso(320, 520, 0.7, expr="content", couleur="#74c0fc"))
    S.add(goutte_perso(540, 580, 0.7, expr="rire", couleur="#74c0fc"))
    S.add(plic(140, 280, 0.9, expr="sourire", regard=(1, 1)))
    S.add(bulle(560, 90, 280, 80, "Au revoir !", 38, pointe=(560, 520)))
    return S


def p07():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(660, 120, 55))
    S.add(rect(0, 420, 800, 380, "#f4d58d"))
    S.add(chemin("M 0 420 Q 200 440 300 520 Q 360 600 300 800 L 0 800 Z", "#8ce99a"))
    S.add(chemin("M 120 420 Q 260 470 300 560 Q 330 640 360 800 L 520 800 Q 460 620 380 520 Q 300 440 220 420 Z", "#4dabf7"))
    S.add(chemin("M 420 800 Q 520 600 800 460 L 800 800 Z", "#1c7ed6"))
    eau_mer = [chemin(f"M {500 + k * 60} {640 - k * 30} q 20 -12 40 0", stroke="#74c0fc", sw=5) for k in range(5)]
    S.add(g(eau_mer))
    S.add(plic(610, 690, 1.1, expr="bouche_bee", regard=(1, 0)))
    S.add(texte(620, 420, "La mer !", 64, "#1c7ed6", contour="#fff"))
    return S


def p08():
    S = Scene()
    ciel(S, "#4dabf7", "#d0ebff")
    S.add(cercle(180, 140, 140, "#ffe066", opacity=0.3), soleil(180, 140, 70, visage=True))
    eau(S, 560, "#1c7ed6", "#4dabf7")
    S.add(rayons_soleil(240, 200, 420, 560, nb=3))
    for k, (x, y) in enumerate([(560, 480), (600, 330), (520, 200)]):
        S.add(vapeur(x, y, 0.55 + 0.1 * k))
    S.add(fleche_courbe("M 640 520 Q 680 400 620 260", (620, 260), -110, "#ffffff", 6))
    S.add(texte(420, 740, "le sel reste dans la mer", 38, "#ffffff", contour="#1c7ed6"))
    for x in (120, 250, 690):
        S.add(cercle(x, 640, 6, "#fff"), cercle(x + 20, 660, 4, "#fff"))
    S.cachette(730, 530, "air")
    return S


def p09():
    S = Scene()
    ciel(S, "#1c7ed6", "#a5d8ff")
    S.add(montagnes(None, 800, ("#b197fc", "#9775fa")))
    flocons(S, 18, 4, zone=(0, 0, 800, 400))
    S.add(gros_nuage(400, 330, 3.4, "#ffffff", "#dbe4ff"))
    gouttelettes(S, (140, 230, 660, 420), 45, 6, "#a5d8ff", (4, 7))
    S.add(vapeur(250, 620, 0.6))
    S.add(fleche(300, 560, 360, 480, "#ffffff", 5, 16))
    S.add(plic(450, 420, 0.7, expr="content"))
    S.add(texte(620, 120, "Brrr !", 70, "#ffffff", contour="#1c7ed6"))
    S.cachette(290, 730, "air")
    return S


def p10():
    S = Scene()
    fond(S, "#e7f5ff")
    cx, cy, r = 400, 420, 230
    S.add(cycle(cx, cy, r, "#1c7ed6", nb=4))
    # en haut : le nuage ; à droite : la pluie ; en bas : la rivière ; à gauche : la mer et la vapeur
    S.add(disque(cx, cy - r, 82, "#d0ebff"), nuage(cx, cy - r + 10, 0.65, "#fff", ombre="#dbe4ff"))
    S.add(disque(cx + r, cy, 82, "#d0ebff"), nuage(cx + r, cy - 30, 0.45, "#adb5bd"))
    for k in range(5):
        S.add(trait(cx + r - 40 + k * 20, cy + 0, cx + r - 46 + k * 20, cy + 30, "#1c7ed6", 4))
    S.add(disque(cx, cy + r, 82, "#d3f9d8"), chemin(f"M {cx - 82} {cy + r + 30} Q {cx} {cy + r - 30} {cx + 82} {cy + r + 10} L {cx + 82} {cy + r + 40} Q {cx} {cy + r} {cx - 82} {cy + r + 60} Z", "#4dabf7"))
    S.add(disque(cx - r, cy, 82, "#d0ebff"), rect(cx - r - 82, cy + 20, 164, 50, "#1c7ed6"), soleil(cx - r + 34, cy - 40, 22, rayons=False))
    S.add(fleche(cx - r - 20, cy + 10, cx - r - 20, cy - 50, "#ffffff", 4, 12))
    S.add(etiquette(cx, cy - r - 100, "nuage", 32), etiquette(cx + r, cy + 120, "pluie", 32),
          etiquette(cx, cy + r + 120, "rivière", 32), etiquette(cx - r, cy + 120, "mer et vapeur", 32))
    S.add(plic(cx, cy + 60, 1.1, expr="rire"))
    S.cachette(550, 70, "air")
    return S


def p11():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(680, 110, 50))
    S.add(rect(0, 480, 800, 320, "#ced4da"))
    for k in range(0, 800, 160):
        S.add(trait(k, 480, k - 60, 800, "#adb5bd", 4))
    # le tour de la flaque tracé à la craie, et la flaque qui a rapetissé
    S.add(ellipse(470, 640, 200, 48, "none", stroke="#ffffff", stroke_width=6, stroke_dasharray="18 10"))
    S.add(flaque(490, 645, 1.1))
    S.add(personne(190, 770, 1.35, peau="claire", cheveux="roux", coiffure="tresses", habit="#ffd43b", robe=False,
                   jambes="#1971c2", expr="surpris", bras="montre", regard=(1, 1),
                   objet=rect(70, -150, 14, 40, "#ffffff", rx=6)))
    S.add(vapeur(560, 520, 0.45), vapeur(450, 400, 0.4))
    S.add(texte(560, 260, "Où est partie l'eau ?", 40, "#1c7ed6", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("plic-seule.svg", vignette),
    ("01-dans-le-nuage.svg", p01), ("02-plic-grossit.svg", p02), ("03-la-pluie.svg", p03),
    ("04-le-ruisseau.svg", p04), ("05-la-riviere.svg", p05), ("06-les-racines.svg", p06),
    ("07-la-mer.svg", p07), ("08-le-soleil-chauffe.svg", p08), ("09-le-froid.svg", p09),
    ("10-le-grand-voyage.svg", p10), ("11-la-flaque.svg", p11),
]
