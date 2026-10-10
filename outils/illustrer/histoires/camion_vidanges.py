"""Le camion de vidanges — Sami, éboueur, et Léo qui l'attend à la fenêtre.

Chaque jeudi, Léo guette le camion. Sami roule les bacs jusqu'au camion, le
lève-bac les vide, le compacteur tasse tout. Le bac bleu (recyclage) va au
centre de tri, le bac brun (compost) devient de la terre, le bac noir
(déchets) part au site d'enfouissement. Sami travaille par tous les temps,
avant le lever du soleil. Léo lui offre un dessin.

Plans : 1 moyen (Léo à la fenêtre) · 2 large (le camion arrive) · 3 moyen
(Sami salue) · 4 gros plan (le lève-bac) · 5 gros plan (le compacteur, en
coupe) · 6 moyen (on trie à la cuisine) · 7 large (le centre de tri) ·
8 moyen (le compost au jardin) · 9 large (sous la neige, à l'aube) ·
10 moyen (le dessin) · 11 gros plan (Léo joue à l'éboueur).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit, gilet_chantier, casquette, roue, FLUO, ARGENT
from objets import pomme

ID = "camion-vidanges"
PAPIER_PEINT = "rayures"

SAMI = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#495057", jambes="#343a40",
            chaussures="#212529", barbe="#2b2b3a", tenue=gilet_chantier("#94d82d"), coiffe=casquette("#2b8a3e"), carrure="ronde")
LUCIE = dict(stature="adulte", peau="claire", cheveux="blond", coiffure="queue", habit="#495057", jambes="#343a40",
             tenue=gilet_chantier("#94d82d"), coiffe=casquette("#2b8a3e"))
LEO = dict(peau="rosee", cheveux="chatain", coiffure="raie", habit="#4dabf7", jambes="#1864ab", taches=True)
PAPA = dict(stature="adulte", peau="rosee", cheveux="chatain", coiffure="courts", habit="#e8590c", jambes="#364fc7")

VERT_CAMION = "#2f9e44"
BLEU_BAC, BRUN_BAC, NOIR_BAC = "#1c7ed6", "#8d5524", "#343a40"


def sami(x, y, s=1.4, **k):
    return pro(x, y, s, **{**SAMI, **k})


def leo(x, y, s=1.2, **k):
    return petit(x, y, s, **{**LEO, **k})


def bac(x, y, s=1.0, couleur=BLEU_BAC, rot=0, ouvert=False, plein=True):
    """Bac roulant vu de face ; (x, y) = au sol."""
    fonce = _assombrir(couleur, 0.75)
    m = [ellipse(0, 4, 56, 8, "#000", opacity=0.12),
         chemin("M -46 -150 L 46 -150 L 40 0 L -40 0 Z", volume(couleur, 0.3, 0.8)),
         rect(-30, -120, 60, 40, "none", rx=6, stroke=fonce, stroke_width=3),
         roue(-34, -6, 12), roue(34, -6, 12)]
    if couleur == BLEU_BAC:
        # flèches du recyclage
        for k in range(3):
            a = math.radians(-90 + k * 120)
            m.append(place(poly([(-8, 0), (8, 0), (0, -12)], "#fff"), math.cos(a) * 14, -100 + math.sin(a) * 14, rot=k * 120 + 90))
    if ouvert:
        m.append(place(rect(-52, -16, 104, 16, fonce, rx=6), 0, -150, rot=-70))
        if plein:
            m.append(ellipse(0, -150, 40, 10, "#dee2e6"))
    else:
        m.append(rect(-52, -162, 104, 16, fonce, rx=6))
        m.append(rect(-18, -172, 36, 12, fonce, rx=5))
    return place(m, x, y, s, rot=rot)


def camion(x, y, s=1.0, flip=False, gyro=True, leve=0.0):
    """Camion de vidanges à chargement arrière, vu de côté, la cabine à droite ;
    (x, y) = au sol, sous le milieu. leve (0 à 1) : un bac levé à l'arrière."""
    v = VERT_CAMION
    m = [ellipse(0, 6, 330, 16, "#000", opacity=0.14),
         # caisse et trémie arrière
         rect(-260, -280, 330, 210, volume(v, 0.3, 0.8), rx=16),
         chemin("M -260 -250 L -320 -200 L -320 -80 L -260 -70 Z", volume(_assombrir(v, 0.85), 0.3, 0.8)),
         rect(-250, -190, 310, 26, "#fff", rx=6), rect(-250, -186, 310, 6, ARGENT),
         rect(-320, -96, 70, 18, "#495057", rx=4),       # marchepied
         trait(-300, -200, -300, -110, "#adb5bd", 6),     # poignée
         # cabine
         chemin("M 80 -70 L 80 -250 L 190 -250 Q 236 -250 246 -180 L 250 -70 Z", volume("#f8f9fa", 0.3, 0.85)),
         chemin("M 98 -236 L 180 -236 Q 214 -234 224 -176 L 98 -176 Z", "#a5d8ff"),
         poly([(110, -236), (130, -236), (112, -176), (100, -176)], "#fff", opacity=0.4),
         rect(96, -160, 46, 8, "#adb5bd", rx=3),
         rect(236, -110, 20, 34, "#ffd43b", rx=4), rect(220, -76, 44, 14, "#868e96", rx=4),
         rect(70, -70, 190, 16, "#495057", rx=6), rect(-330, -70, 400, 16, "#495057", rx=6),
         roue(-200, -40, 44), roue(-90, -40, 44), roue(170, -40, 44)]
    # petits feux et gyrophare orange
    m.append(rect(-326, -120, 14, 24, "#fa5252", rx=4))
    if gyro:
        m.append(place([rect(-18, -4, 36, 8, "#495057", rx=3), chemin("M -14 -4 Q -14 -24 0 -24 Q 14 -24 14 -4 Z", "#ff922b")], 140, -250))
    # le lève-bac : un bac basculé au-dessus de la trémie
    if leve:
        # pivot au pied du bac, au-dessus de l'arrière : le couvercle plonge dans la trémie
        m.append(place(bac(0, 0, 0.75, BLEU_BAC, ouvert=leve > 0.6), -360, -300, rot=leve * 140))
        if leve > 0.6:
            for k in range(6):
                m.append(place(rect(-10, -6, 20, 12, ("#fff", "#ffd43b", "#a5d8ff", "#fa5252", "#e9ecef", "#69db7c")[k], rx=3),
                               -300 + k * 12, -230 + (k % 3) * 18, rot=k * 30))
    return place(m, x, y, s, flip=flip) + occuper(x - 330 * s, y - 280 * s, x + 260 * s, y)


def rue_maisons(S, y=640, matin=True, neige=False, graine=1, lumiere=False):
    """La rue de Léo : maisons, trottoir, chaussée."""
    if matin:
        ciel(S, "#a5d8ff", "#fff4e6")
    for k, (mx, mur, toit) in enumerate(((120, "#ffe8cc", "#e8590c"), (400, "#d3f9d8", "#1c7ed6"), (680, "#fff3bf", "#c92a2a"))):
        S.add(maison(mx, y - 70, 0.95, mur=mur, toit=toit, cote=k != 2, volets="#495057" if k == 1 else None, lumiere=lumiere))
    S.add(rect(0, y - 70, 800, 40, "#ced4da"), rect(0, y - 74, 800, 6, "#adb5bd"))
    S.add(rect(0, y - 30, 800, 830 - y, "#868e96"))
    for xx in range(40, 800, 160):
        S.add(rect(xx, y + 70, 80, 10, "#f8f9fa", rx=3))
    if neige:
        S.add(rect(0, y - 78, 800, 10, "#fff", rx=4))
    S.proposer_cachette(60, y - 40)
    S.proposer_cachette(740, y - 40)


def cuisine(S):
    piece(S, "cuisine", 590)
    S.add(fenetre(520, 90, 180, 150, "#a5d8ff", rideaux="#ff922b",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), maison(610, 330, 0.5, cote=False)])))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_maisons(S, 600)
    S.add(camion(430, 720, 1.05, leve=0.7))
    S.add(sami(110, 790, 1.35, expr="rire", bras="salut", regard=(1, 0)))
    S.add(bac(720, 790, 0.9, BRUN_BAC))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bac(110, 262, 0.95, BLEU_BAC), bac(210, 262, 0.95, BRUN_BAC), bac(310, 262, 0.95, NOIR_BAC))
    return S


def p01():
    """Plan moyen : jeudi matin, Léo en pyjama colle son nez à la fenêtre."""
    S = Scene()
    piece(S, "chambre", 600)
    dehors = g([rect(0, 0, 800, 800, "#a5d8ff"), rect(0, 300, 800, 200, "#868e96"),
                bac(330, 330, 0.5, BLEU_BAC), bac(380, 330, 0.5, BRUN_BAC), bac(430, 330, 0.5, NOIR_BAC)])
    S.add(fenetre(220, 110, 360, 260, "#a5d8ff", rideaux="#4dabf7", contenu=dehors))
    S.add(leo(400, 790, 1.7, expr="surpris", bras="tete", regard=(0, -0.6), habit="#ffc9c9", jambes="#ffc9c9"))
    S.add(horloge(700, 140, 40, 6, 30))
    return S


def p02():
    """Plan large : Vroum ! Le camion arrive dans la rue."""
    S = Scene()
    rue_maisons(S, 620, graine=2)
    S.add(bac(70, 600, 0.6, BLEU_BAC), bac(130, 600, 0.6, BRUN_BAC), bac(190, 600, 0.6, NOIR_BAC))
    S.add(camion(470, 730, 1.0))
    S.add(texte(250, 160, "Vroum !", 66, VERT_CAMION, contour="#fff"))
    S.add(texte(620, 220, "Bip ! Bip !", 46, "#e8590c", contour="#fff"))
    S.cachette(745, 582)
    return S


def p03():
    """Plan moyen : Sami, l'éboueur, salue Léo à la fenêtre."""
    S = Scene()
    rue_maisons(S, 640, graine=3)
    S.add(maison(400, 570, 1.6, mur="#d3f9d8", toit="#1c7ed6", cote=False, volets="#495057"))
    S.add(leo(400 - 80 * 1.6 + 20, 570 - 100 * 1.6 + 60, 0.38, expr="rire", bras="coucou", ombre=False))
    S.add(sami(560, 790, 1.55, expr="rire", bras="coucou", regard=(-1, -0.6)))
    S.add(bac(250, 790, 1.0, NOIR_BAC))
    S.add(bulle(620, 140, 300, 90, "Salut, Léo !", 38, pointe=(600, 440)))
    return S


def p04():
    """Gros plan : le lève-bac soulève le bac bleu et le vide dans le camion."""
    S = Scene()
    rue_maisons(S, 640, graine=4)
    S.add(camion(650, 760, 1.15, leve=1.0))
    S.add(sami(110, 790, 1.35, expr="concentre", bras="pousse", regard=(1, -0.8)))
    S.camera(1.3, 330, 480)
    S.dessus(texte(560, 120, "Hop !", 70, "#e8590c", contour="#fff"))
    S.cachette(574, 270, "air")
    return S


def p05():
    """Gros plan en coupe : dans la caisse, la pelle du compacteur tasse les déchets."""
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(rect(0, 700, 800, 100, "#868e96"))
    S.add(rect(80, 220, 640, 420, "#2f9e44", rx=24))
    S.add(rect(110, 250, 580, 360, "#d3f9d8", rx=12))
    r = random.Random(3)
    for k in range(40):
        c = ("#fff", "#ffd43b", "#a5d8ff", "#fa5252", "#ced4da", "#69db7c", "#ffc078")[k % 7]
        S.add(place(rect(-24, -14, 48, 28, c, rx=5, stroke="#adb5bd", stroke_width=2), r.uniform(330, 670), r.uniform(420, 590), rot=r.uniform(-40, 40)))
    S.add(rect(250, 260, 30, 340, "#495057", rx=6), rect(130, 410, 120, 26, "#868e96", rx=6))
    from sciences import fleche
    S.add(fleche(300, 330, 420, 330, "#e8590c", sw=10, tete=26))
    S.add(roue(220, 680, 44), roue(560, 680, 44))
    S.add(texte(400, 140, "Crrrr… on tasse !", 52, "#2b8a3e", contour="#fff"))
    S.cachette(740, 740)
    return S


def p06():
    """Plan moyen : à la cuisine, Léo et Papa trient : bac bleu, bac brun, bac noir."""
    S = Scene()
    cuisine(S)
    S.add(bac(170, 790, 1.0, BLEU_BAC, ouvert=True, plein=False))
    S.add(bac(400, 790, 1.0, BRUN_BAC, ouvert=True, plein=False))
    S.add(bac(630, 790, 1.0, NOIR_BAC, ouvert=True, plein=False))
    S.add(texte(170, 430, "papier, boîtes,", 26, BLEU_BAC, contour="#fff"), texte(170, 462, "bouteilles", 26, BLEU_BAC, contour="#fff"))
    S.add(texte(400, 430, "pelures,", 26, BRUN_BAC, contour="#fff"), texte(400, 462, "coquilles d'œuf", 26, BRUN_BAC, contour="#fff"))
    S.add(texte(630, 430, "le reste", 26, NOIR_BAC, contour="#fff"))
    S.add(leo(280, 790, 1.2, expr="concentre", bras="donne", regard=(-1, 0), flip=True,
              objet=place(rect(-26, -40, 52, 70, "#e9ecef", rx=6, stroke="#adb5bd", stroke_width=3), 96, -110)))
    S.add(pro(520, 790, 1.15, expr="content", bras="donne", regard=(-1, 0), flip=True,
              objet=pomme(*ancre(84, -92, "donne", "adulte"), 1.0, "#ffa94d"), **PAPA))
    return S


def p07():
    """Plan large : au centre de tri, un tapis roulant ; on sépare papiers, plastiques et métal."""
    S = Scene()
    interieur(S, "#e9ecef", "#adb5bd", 560)
    S.add(rect(0, 120, 800, 20, "#868e96"))
    ouvriers = ((270, dict(peau="foncee", cheveux="noir", coiffure="tresses")), (530, dict(peau="doree", cheveux="brun", coiffure="courts")))
    for x, pk in ouvriers:
        S.add(pro(x, 500, 0.95, stature="adulte", habit="#495057", jambes="#343a40", tenue=gilet_chantier("#94d82d"), expr="concentre",
                  bras="porte", regard=(0, 0.5), **pk))
    S.add(rect(40, 470, 720, 50, "#495057", rx=24))
    for xx in range(70, 760, 60):
        S.add(cercle(xx, 495, 16, "#868e96"))
    r = random.Random(4)
    for k in range(10):
        c = ("#fff", "#a5d8ff", "#ced4da", "#ffd43b")[k % 4]
        S.add(place(rect(-22, -14, 44, 28, c, rx=4, stroke="#868e96", stroke_width=2), 80 + k * 70, 456, rot=r.uniform(-20, 20)))
    for k, (x, c, mot) in enumerate(((150, "#fff", "papier"), (400, "#a5d8ff", "plastique"), (650, "#ced4da", "métal"))):
        S.add(rect(x - 70, 600, 140, 120, volume("#868e96", 0.3, 0.8), rx=8))
        S.add(rect(x - 60, 590, 120, 30, c, rx=6))
        S.add(texte(x, 690, mot, 30, "#fff"))
    S.add(texte(400, 90, "Le centre de tri", 46, "#1c7ed6", contour="#fff"))
    return S


def p08():
    """Plan moyen : au jardin, le compost est devenu de la terre ; Léo plante des fleurs."""
    S = Scene()
    paysage(S, 540, 610, graine=5)
    S.add(rect(520, 520, 200, 170, volume("#a0693a", 0.3, 0.8), rx=8))
    S.add(planches(520, 520, 200, 170, "#a0693a", larg=34, vertical=False))
    S.add(ellipse(360, 720, 180, 40, "#6d4424"))
    for k, c in enumerate(("#fa5252", "#fcc419", "#cc5de8", "#ff922b")):
        S.add(fleur(250 + k * 70, 720, 0.75, c, tige=70))
    S.add(leo(200, 790, 1.35, expr="content", bras="ramasse", regard=(1, 0.5)))
    S.add(ver(420, 740, 0.4, 120))
    S.add(bulle(620, 160, 360, 110, "Les pelures\nfont de la terre !", 34, pointe=(620, 500)))
    return S


def ver(x, y, s, longueur):
    from animaux import ver as ver_
    return ver_(x, y, s, longueur)


def p09():
    """Plan large : à l'aube, sous la neige, Sami travaille déjà."""
    S = Scene()
    ciel(S, "#364fc7", "#ffa8a8")
    S.ambiance("soir")
    rue_maisons(S, 640, matin=False, neige=True, graine=6, lumiere=True)
    flocons(S, 40, 7, (0, 0, 800, 640))
    S.add(camion(500, 760, 1.0))
    S.add(sami(150, 790, 1.3, expr="content", bras="pousse", regard=(1, 0), habit="#1864ab"))
    S.add(bac(250, 790, 0.95, NOIR_BAC))
    S.add(rect(0, 785, 800, 15, "#fff", opacity=0.6))
    S.cachette(70, 230, "air")
    return S


def p10():
    """Plan moyen : Léo offre son dessin du camion à Sami, qui sourit."""
    S = Scene()
    rue_maisons(S, 640, graine=7)
    dessin = g([rect(-70, -50, 140, 100, "#fff", stroke="#dee2e6", stroke_width=3), rect(-50, -20, 70, 34, VERT_CAMION, rx=4),
                rect(20, -14, 30, 28, "#e7f5ff", rx=3), cercle(-30, 18, 9, ENCRE), cercle(30, 18, 9, ENCRE), coeur(-48, -36, 0.3, "#fa5252")])
    S.add(leo(270, 790, 1.4, expr="fier", bras="donne", regard=(1, -0.4), objet=place(dessin, 96, -110, 0.9)))
    S.add(sami(520, 790, 1.5, expr="content", bras="calin", regard=(-1, 0.4)))
    S.add(bulle(560, 140, 380, 90, "Merci, Léo !", 38, pointe=(540, 420)))
    return S


def p11():
    """Gros plan : Léo joue à l'éboueur avec son petit camion vert et ses blocs."""
    S = Scene()
    piece(S, "chambre", 560)
    S.add(tapis(400, 690, 330, 70, "#d0ebff", "#74c0fc"))
    S.add(camion(500, 700, 0.42))
    S.add(leo(250, 790, 1.5, expr="rire", bras="pousse", regard=(1, 0.5), coiffe=casquette("#2b8a3e")))
    for k, c in enumerate(("#fa5252", "#fcc419", "#4dabf7")):
        S.add(rect(600 + k * 44, 720, 36, 36, c, rx=4))
    S.camera(1.2, 420, 560)
    S.dessus(bulle(560, 130, 420, 100, "Plus tard, moi aussi,\nje serai éboueur !", 32))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bacs-seuls.svg", vignette),
    ("01-a-la-fenetre.svg", p01), ("02-vroum.svg", p02), ("03-salut-leo.svg", p03),
    ("04-le-leve-bac.svg", p04), ("05-le-compacteur.svg", p05), ("06-trier.svg", p06),
    ("07-centre-de-tri.svg", p07), ("08-le-compost.svg", p08), ("09-sous-la-neige.svg", p09),
    ("10-le-dessin.svg", p10), ("11-plus-tard.svg", p11),
]
