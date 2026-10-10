"""Les feux de la Saint-Jean — la fête nationale du Québec, le 24 juin.

Émile fête la Saint-Jean avec Mamie et Papi : drapeaux bleus et blancs aux
fenêtres, fleur de lys peinte sur la joue, pique-nique, défilé, musique
(violon, accordéon) et danse. La Saint-Jean tombe juste après le solstice
d'été : c'est presque le jour le plus long de l'année, le soleil ne se
couche qu'après 20 h 30. À la nuit, le grand feu de joie (on reste derrière
la barrière), les chansons, les feux d'artifice bleus et blancs, et le
retour, endormi.

Plans : 1 large (la rue pavoisée) · 2 gros plan (la fleur de lys sur la
joue) · 3 moyen (le pique-nique) · 4 large (le défilé) · 5 moyen (violon
et accordéon) · 6 gros plan (l'horloge et le soleil) · 7 large (le
coucher de soleil) · 8 large (le feu de joie) · 9 moyen (on chante) ·
10 large (les feux d'artifice) · 11 moyen (endormi).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from fetes import feu_artifice, guirlande_fanions
from fables import violon, archet

ID = "saint-jean"
PAPIER_PEINT = "etoiles"

BLEU = "#1c4fa0"
EMILE = dict(peau="rosee", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7", taches=True)
MAMIE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="boucles", habit="#f8f9fa", acc=("lunettes",), carrure="ronde")
PAPI = dict(stature="ancien", peau="claire", cheveux="gris", coiffure="chauve_cote", habit=BLEU, robe=False, jambes="#495057", barbe="#adb5bd")
CHLOE = dict(peau="foncee", cheveux="noir", coiffure="tresses", habit="#f8f9fa", robe=True, yeux="cils")
MUSICIEN = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="queue", habit="#e03131", robe=False, jambes="#343a40")


def emile(x, y, s=1.2, **k):
    return personne(x, y, s, **{**EMILE, **k})


def fleur_lys(x, y, s=1.0, c="#ffffff"):
    """Fleur de lys stylisée ; (x, y) = centre ; hauteur ≈ 100 à s = 1."""
    m = [chemin("M 0 -50 Q 16 -24 10 4 L -10 4 Q -16 -24 0 -50 Z", c),
         chemin("M -8 -2 Q -20 -40 -40 -30 Q -50 -18 -36 -6 Q -30 -16 -20 -10 Q -16 0 -8 6 Z", c),
         chemin("M 8 -2 Q 20 -40 40 -30 Q 50 -18 36 -6 Q 30 -16 20 -10 Q 16 0 8 6 Z", c),
         rect(-24, 4, 48, 10, c, rx=3),
         chemin("M -6 14 Q -12 34 -24 40 Q -10 40 0 28 Q 10 40 24 40 Q 12 34 6 14 Z", c)]
    return place(m, x, y, s)


def drapeau(x, y, s=1.0, mat=True, ondule=0):
    """Drapeau bleu à croix blanche et quatre fleurs de lys ; (x, y) = pied du mât (ou coin haut gauche sans mât)."""
    w, h = 180, 120
    m = []
    x0, y0 = (12, -300) if mat else (0, 0)
    if mat:
        m += [rect(-4, -310, 8, 310, "#adb5bd", rx=3), cercle(0, -314, 7, "#fcc419")]
    drap = [rect(x0, y0, w, h, BLEU), rect(x0 + w / 2 - 10, y0, 20, h, "#fff"), rect(x0, y0 + h / 2 - 10, w, 20, "#fff")]
    for cx, cy in ((x0 + w * 0.25, y0 + h * 0.25), (x0 + w * 0.75, y0 + h * 0.25), (x0 + w * 0.25, y0 + h * 0.75), (x0 + w * 0.75, y0 + h * 0.75)):
        drap.append(fleur_lys(cx, cy, 0.38))
    if ondule:
        drap.append(rect(x0, y0, w, h, lineaire([(0, "#000", 0), (0.5, "#000", 0.12), (1, "#fff", 0.1)], 0, 0, 1, 0)))
    m.append(g(drap))
    return place(m, x, y, s)


def feu_de_joie(x, y, s=1.0, graine=1):
    """Grand feu de joie sur un bûcher ; (x, y) = pied."""
    r = random.Random(graine)
    m = []
    for k in range(9):
        a = math.radians(-120 + k * 7.5)
        m.append(trait(math.cos(a) * 30, -20, math.cos(a) * 170, -20 + math.sin(a) * 170 + 140, "#6d4424", 18))
    m += [chemin("M -150 -10 Q -170 -170 -60 -280 Q -70 -180 -20 -170 Q -40 -320 40 -400 Q 30 -250 80 -220 Q 100 -300 140 -320 Q 190 -180 150 -10 Z", "#ff922b"),
          chemin("M -100 -10 Q -110 -130 -30 -200 Q -30 -130 10 -120 Q 0 -230 60 -280 Q 60 -170 100 -130 Q 130 -80 100 -10 Z", "#ffd43b"),
          chemin("M -40 -10 Q -50 -70 0 -110 Q 10 -70 40 -60 Q 60 -30 40 -10 Z", "#fff3bf")]
    for k in range(16):
        m.append(cercle(r.uniform(-180, 200), r.uniform(-560, -300), r.uniform(2, 5), "#ffd43b"))
    return place(m, x, y, s)


def barriere_corde(x0, x1, y):
    m = []
    for x in range(int(x0), int(x1) + 1, 120):
        m.append(rect(x - 5, y - 70, 10, 70, "#a0693a", rx=3))
    m.append(chemin(" ".join(f"M {x} {y - 60} Q {x + 60} {y - 40} {x + 120} {y - 60}" for x in range(int(x0), int(x1), 120)), stroke="#fcc419", sw=5))
    return g(m)


def accordeon(x, y, s=1.0):
    m = [rect(-50, -40, 24, 80, "#e03131", rx=4), rect(26, -40, 24, 80, "#e03131", rx=4)]
    for k in range(6):
        m.append(rect(-26 + k * 9, -36, 8, 72, "#f8f9fa" if k % 2 else "#adb5bd"))
    for k in range(4):
        m.append(cercle(-38, -24 + k * 16, 4, "#fff"))
    return place(m, x, y, s)


def rue(S, y=640, graine=1):
    ciel(S, "#74c0fc", "#e7f5ff")
    for k, (bx, coul) in enumerate(((10, "#ffe8cc"), (220, "#e7f5ff"), (430, "#fff3bf"), (630, "#ffe3e3"))):
        S.add(immeuble(bx, y - 40, 160, 3, coul, "pignon" if k % 2 else "mansarde", graine=graine + k))
        S.add(drapeau(bx + 40, y - 140, 0.35, mat=False))
    S.add(guirlande_fanions(0, 120, 800, 120, creux=20, nb=14, couleurs=(BLEU, "#ffffff")))
    S.add(rect(0, y - 40, 800, 840 - y, "#ced4da"), rect(0, y - 44, 800, 6, "#adb5bd"))
    for x in (64, 736, 150, 650):
        S.proposer_cachette(x, y + 40)


def parc(S, y=600, graine=1, haut="#74c0fc", bas="#e7f5ff", soir=False):
    paysage(S, y - 50, y, "#8ce99a", "#b2f2bb", haut, bas, graine=graine, nuages=() if soir else ((620, 120, 0.6),))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    S.add(feu_artifice(170, 150, 80, "#4dabf7"), feu_artifice(620, 120, 90, "#ffffff", "#74c0fc"))
    S.add(rect(0, 620, 800, 180, "#2b3a2f"))
    S.add(feu_de_joie(560, 720, 0.7))
    S.lumiere(560, 600, 300, "#ff922b", 0.6)
    S.add(drapeau(150, 790, 1.0))
    S.add(emile(330, 790, 1.35, expr="rire", bras="haut", regard=(1, -0.3)))
    S.cachette(760, 770)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(drapeau(110, 40, 1.1, mat=False))
    return S


def p01():
    """Plan large : le 24 juin au matin, la rue est pavoisée de drapeaux bleus et blancs."""
    S = Scene()
    rue(S, 640)
    S.add(emile(330, 790, 1.15, expr="rire", bras="salut", regard=(1, 0)))
    S.add(personne(470, 790, 1.25, expr="content", bras="main", flip=True, regard=(-1, 0), **MAMIE))
    S.add(texte(400, 220, "Bonne fête nationale !", 50, BLEU, contour="#fff"))
    return S


def p02():
    """Gros plan : Mamie peint une fleur de lys bleue sur la joue d'Émile."""
    S = Scene()
    parc(S, 600, graine=2)
    S.add(personne(230, 860, 1.8, expr="concentre", bras="tend", regard=(1, 0), **MAMIE))
    S.add(emile(560, 860, 1.8, expr="content", bras="bas", regard=(-1, 0)))
    S.add(fleur_lys(560 - 30 * 1.8 - 6, 860 - 128 * 1.8, 0.26, BLEU))
    S.camera(1.3, 420, 520)
    S.dessus(texte(400, 110, "Une fleur de lys sur la joue !", 44, BLEU, contour="#fff"))
    S.cachette(674, 400, "air")
    return S


def p03():
    """Plan moyen : le pique-nique au parc, sur une nappe bleue et blanche."""
    S = Scene()
    parc(S, 580, graine=3)
    S.add(arbre(110, 640, 1.0))
    S.add(ellipse(400, 720, 330, 60, BLEU))
    for k in range(-4, 5):
        S.add(trait(400 + k * 70, 664, 400 + k * 80, 778, "#fff", 6))
    S.add(personne(230, 720, 1.1, expr="content", bras="porte", regard=(1, 0.3), **PAPI))
    S.add(emile(400, 730, 1.0, expr="miam", bras="porte", regard=(0, 0.4), objet=place(chemin("M -40 0 Q 0 -50 40 0 Z", "#ff6b6b"), 0, -70)))
    S.add(personne(570, 720, 1.1, expr="rire", bras="mains_jointes", regard=(-1, 0.3), **MAMIE))
    S.add(drapeau(700, 760, 0.7))
    return S


def p04():
    """Plan large : le défilé : drapeaux, tambours, et les gens qui saluent."""
    S = Scene()
    rue(S, 640, graine=4)
    for k, x in enumerate((140, 300, 460, 620)):
        S.add(personne(x, 760, 0.9, stature="adulte", peau=("claire", "brune", "doree", "foncee")[k], cheveux="noir", coiffure=("courts", "queue", "chignon", "afro")[k],
                       habit=BLEU if k % 2 else "#f8f9fa", robe=False, jambes="#343a40", expr="joie", bras="tient", regard=(1, 0),
                       objet=drapeau(*ancre(68, -100, "tient", "adulte"), 0.42)))
    S.add(emile(80, 795, 0.9, expr="rire", bras="coucou", regard=(1, -0.4)))
    S.add(personne(720, 795, 0.9, expr="rire", bras="applaudit", regard=(-1, -0.4), **CHLOE))
    S.add(texte(400, 200, "Le défilé !", 56, BLEU, contour="#fff"))
    S.cachette(730, 220, "air")
    return S


def p05():
    """Plan moyen : au parc, un violoneux et une accordéoniste jouent ; Émile et Chloé dansent."""
    S = Scene()
    parc(S, 580, graine=5)
    S.add(guirlande_fanions(0, 80, 800, 80, creux=30, nb=12, couleurs=(BLEU, "#ffffff")))
    S.add(personne(140, 790, 1.2, stature="ancien", peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#2f9e44", robe=False,
                   jambes="#5c3a1e", barbe="#e9ecef", expr="content", bras="porte", regard=(1, 0),
                   objet=g([place(violon(0, 0, 0.7), -10, -140), place(archet(0, 0, 0.7), 30, -130)])))
    S.add(personne(660, 790, 1.2, expr="joie", bras="porte", regard=(-1, 0), objet=accordeon(*ancre(0, -74, "porte", "adulte"), 0.8), **MUSICIEN))
    S.add(emile(330, 790, 1.15, expr="rire", bras="danse", regard=(1, 0)))
    S.add(personne(480, 790, 1.15, expr="rire", bras="danse", flip=True, regard=(-1, 0), **CHLOE))
    S.add(notes(240, 400, 1.0, BLEU), notes(560, 380, 0.9, BLEU))
    S.cachette(730, 220, "air")
    return S


def p06():
    """Gros plan : l'horloge marque 20 h 30, et le soleil brille encore."""
    S = Scene()
    parc(S, 600, graine=6, haut="#ffa94d", bas="#fff4e6")
    S.add(soleil(600, 330, 60))
    S.add(rect(240, 160, 30, 440, "#495057"))
    S.add(horloge(255, 190, 70, 8, 30, "#fff", "#343a40"))
    S.add(emile(460, 860, 1.7, expr="surpris", bras="joues", regard=(-1, -0.6)))
    S.camera(1.15, 400, 470)
    S.dessus(bulle(560, 110, 420, 100, "Huit heures et demie,\net il fait encore jour !", 30, pointe=S.vers_page(470, 470)))
    return S


def p07():
    """Plan large : le soleil se couche ; tout le monde se rassemble autour du grand bûcher."""
    S = Scene()
    parc(S, 580, graine=7, haut="#c2255c", bas="#ffd8a8", soir=True)
    S.add(soleil(640, 560, 55))
    S.add(rect(0, 640, 800, 160, "#3d4f38", opacity=0.4))
    for k in range(9):
        a = math.radians(-120 + k * 7.5)
        S.add(trait(400 + math.cos(a) * 30, 700, 400 + math.cos(a) * 170, 700 + math.sin(a) * 170 + 140, "#6d4424", 18))
    S.add(barriere_corde(160, 640, 790))
    S.add(emile(120, 790, 1.0, expr="joie", bras="main", regard=(1, -0.3)))
    S.add(personne(220, 790, 1.1, expr="content", bras="main", flip=True, regard=(1, -0.3), **PAPI))
    S.add(personne(700, 790, 1.1, expr="content", bras="mains_jointes", regard=(-1, -0.3), **MAMIE))
    S.add(texte(400, 160, "Le soleil se couche enfin…", 44, "#fff3bf", contour="#c2255c"))
    return S


def p08():
    """Plan large : la nuit, le grand feu de joie ; les enfants restent derrière la barrière."""
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 40, 8, (0, 0, 800, 300))
    S.add(rect(0, 620, 800, 180, "#1b2a1f"))
    S.add(feu_de_joie(400, 700, 0.9))
    S.lumiere(400, 540, 360, "#ff922b", 0.7)
    S.lumiere(400, 700, 300, "#ffa94d", 0.5, ry=80)
    S.add(barriere_corde(160, 640, 790))
    S.add(emile(110, 790, 1.0, expr="bouche_bee", bras="joues", regard=(1, -0.4)))
    S.add(personne(700, 790, 1.0, expr="rire", bras="ouverts", regard=(-1, -0.4), **CHLOE))
    S.add(texte(400, 120, "Le feu de la Saint-Jean !", 48, "#ffd43b", contour="#c92a2a"))
    return S


def p09():
    """Plan moyen : autour du feu, tout le monde chante, bras dessus, bras dessous."""
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 30, 9, (0, 0, 800, 300))
    S.add(rect(0, 620, 800, 180, "#1b2a1f"))
    S.lumiere(400, 600, 420, "#ff922b", 0.55)
    for k, (x, pk) in enumerate(((130, PAPI), (290, EMILE), (450, CHLOE), (620, MAMIE))):
        S.add(personne(x, 790, 1.2, expr="chante", bras="epaule", regard=(1, 0), **pk))
    S.add(notes(220, 380, 1.0, "#ffd43b"), notes(560, 360, 1.0, "#ffd43b"))
    S.add(texte(400, 160, "Tout le monde chante !", 50, "#ffd43b", contour="#c92a2a"))
    S.cachette(130, 70, "air")
    return S


def p10():
    """Plan large : les feux d'artifice bleus et blancs éclatent au-dessus du parc."""
    S = Scene()
    nuit(S, "#050a1f", "#1c2a52")
    S.add(feu_artifice(180, 170, 100, "#4dabf7"), feu_artifice(520, 120, 110, "#ffffff", "#74c0fc"),
          feu_artifice(650, 300, 70, "#4dabf7"), feu_artifice(330, 320, 60, "#ffffff", "#a5d8ff"))
    S.add(rect(0, 640, 800, 160, "#1b2a1f"))
    S.add(emile(330, 790, 1.15, expr="bouche_bee", bras="haut", regard=(0, -1)))
    S.add(personne(470, 790, 1.2, expr="rire", bras="epaule", flip=True, regard=(0, -1), **PAPI))
    S.add(texte(400, 470, "Ooooh !", 56, "#fff"))
    return S


def p11():
    """Plan moyen : de retour à la maison, Émile s'est endormi dans les bras de Papi."""
    S = Scene()
    piece(S, "chambre", 600)
    S.ambiance("nuit")
    S.add(fenetre(470, 90, 200, 170, "#1c2a52", nuit_=True, rideaux=BLEU))
    S.add(lit(330, 790, 380, couverture=BLEU))
    S.add(emile(330, 660, 0.9, expr="dort", rot=-90, ombre=False))
    S.add(rect(240, 655, 270, 85, lineaire([(0, "#4dabf7"), (1, BLEU)]), rx=16))
    S.add(drapeau(640, 790, 0.6))
    S.add(personne(640, 790, 1.3, expr="content", bras="chut", regard=(-1, 0.3), **PAPI))
    S.add(lampe(120, 610, 0.6))
    S.add(zzz(420, 560, 0.8, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("drapeau-seul.svg", vignette),
    ("01-bonne-fete.svg", p01), ("02-la-fleur-de-lys.svg", p02), ("03-le-pique-nique.svg", p03),
    ("04-le-defile.svg", p04), ("05-la-musique.svg", p05), ("06-encore-jour.svg", p06),
    ("07-le-soleil-se-couche.svg", p07), ("08-le-feu.svg", p08), ("09-on-chante.svg", p09),
    ("10-les-feux-d-artifice.svg", p10), ("11-endormi.svg", p11),
]
