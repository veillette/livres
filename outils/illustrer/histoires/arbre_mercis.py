"""L'arbre aux mercis — l'Action de grâce chez Grand-maman.

Un samedi d'octobre, Rosalie et son petit frère Félix vont chez
Grand-maman pour l'Action de grâce. On cueille les pommes au verger, on
rentre les courges du potager, on fait la tarte. « L'Action de grâce, c'est
la fête où l'on dit merci », explique Grand-maman. Rosalie a une idée : une
branche dans un pot, des feuilles d'érable en papier, et sur chaque feuille,
le merci de quelqu'un. Au grand repas, l'arbre aux mercis est tout couvert
de feuilles.

Plans : 1 large (l'arrivée sous les érables) · 2 moyen (le verger) · 3 gros
plan (la plus grosse courge) · 4 moyen (la tarte, la question) · 5 gros
plan (Rosalie a une idée) · 6 large (la branche et les feuilles) · 7 moyen
(on découpe) · 8 moyen (Tante Nadia et Amir) · 9 large (chacun accroche son
merci) · 10 gros plan (Grand-maman lit) · 11 large (le grand repas).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from objets import pomme, assiette, bol

ID = "arbre-mercis"
PAPIER_PEINT = "fleurs"

ROSALIE = dict(peau="claire", cheveux="chatain", coiffure="couettes", habit="#e67700", taches=True,
               nez="retrousse", jambes="#5c3d2e")
FELIX = dict(peau="claire", cheveux="blond", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#495057",
             stature="petit")
PAPA = dict(peau="claire", cheveux="brun", coiffure="courts", habit="#2f9e44", robe=False, jambes="#364fc7",
            stature="adulte", carrure="normale", barbe="#4a2c17", nez="long")
GRAND_MAMAN = dict(peau="claire", cheveux="blanc", coiffure="chignon", habit="#a61e4d", stature="ancien",
                   carrure="ronde", nez="rond", acc=("lunettes",))
NADIA = dict(peau="brune", cheveux="noir", coiffure="longs", habit="#ae3ec9", stature="adulte", carrure="fine",
             yeux="cils", nez="pointu")
AMIR = dict(peau="brune", cheveux="noir", coiffure="afro", habit="#0ca678", robe=False, jambes="#343a40")

COULEURS_FEUILLES = ("#e03131", "#f76707", "#fab005", "#c92a2a", "#e8590c", "#f59f00")


def rosalie(x, y, s=1.2, **k):
    return personne(x, y, s, **{**ROSALIE, **k})


def felix(x, y, s=1.2, **k):
    return personne(x, y, s, **{**FELIX, **k})


def papa(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PAPA, **k})


def grand_maman(x, y, s=1.2, **k):
    return personne(x, y, s, **{**GRAND_MAMAN, **k})


def nadia(x, y, s=1.2, **k):
    return personne(x, y, s, **{**NADIA, **k})


def amir(x, y, s=1.2, **k):
    return personne(x, y, s, **{**AMIR, **k})


# --- Objets ----------------------------------------------------------------------

_ERABLE = [(0, -52), (9, -32), (20, -38), (17, -16), (38, -26), (34, -10), (48, -4), (28, 8), (32, 20), (10, 14), (3, 24)]


def feuille_erable(x, y, s=1.0, couleur="#e03131", rot=0, papier=False, ecrit=False):
    """Feuille d'érable (vraie ou découpée dans du papier) ; (x, y) = centre."""
    pts = _ERABLE + [(-px, py) for px, py in reversed(_ERABLE)]
    m = [poly(pts, volume(couleur, 0.3, 0.78) if not papier else couleur,
              stroke=_assombrir(couleur, 0.75) if papier else "none", stroke_width=2)]
    if not papier:
        m.append(chemin("M 0 30 L 0 -40 M 0 4 L 30 -18 M 0 4 L -30 -18 M 0 14 L 22 12 M 0 14 L -22 12",
                        stroke=_assombrir(couleur, 0.7), sw=2, opacity=0.6))
    m.append(trait(0, 22, 0, 40, _assombrir(couleur, 0.6), 3))
    if ecrit:
        m += [trait(-16, -10, 16, -10, "#fff", 3, opacity=0.9), trait(-20, 0, 14, 0, "#fff", 3, opacity=0.9)]
    return place(m, x, y, s, rot=rot)


def feuilles_volantes(S, zone=(0, 0, 800, 560), nb=14, graine=3):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for k in range(nb):
        S.add(feuille_erable(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(0.35, 0.55),
                             COULEURS_FEUILLES[k % len(COULEURS_FEUILLES)], rot=r.uniform(-60, 60)))


def tapis_feuilles(S, y0, y1, nb=26, graine=4):
    r = random.Random(graine)
    for k in range(nb):
        S.add(feuille_erable(r.uniform(10, 790), r.uniform(y0, y1), r.uniform(0.3, 0.45),
                             COULEURS_FEUILLES[k % len(COULEURS_FEUILLES)], rot=r.uniform(-90, 90)))


def erable(x, y, s=1.0, couleur="#f76707", couleur2="#e03131"):
    return arbre(x, y, s, feuillage=couleur, feuillage2=couleur2, tronc="#6d4424")


# rameaux de l'arbre aux mercis : (départ, arrivée) dans le repère du pot
_RAMEAUX = [((0, -90), (0, -340)), ((0, -170), (-100, -270)), ((0, -200), (90, -300)), ((0, -260), (-60, -350)),
            ((-50, -220), (-120, -210)), ((40, -250), (110, -230)), ((0, -300), (40, -380))]
# accroches des feuilles en papier (x, y du crochet), dans l'ordre où on les accroche
_ACCROCHES = [(-60, -230), (50, -260), (0, -330), (-90, -262), (80, -292), (-30, -320), (30, -215), (-110, -212),
              (100, -232), (25, -370), (-50, -345), (60, -330), (-20, -260), (0, -190)]


def arbre_mercis(x, y, s=1.0, feuilles=12, pot="#d9480f"):
    """La branche plantée dans un pot, et ses feuilles de papier accrochées par
    un fil ; (x, y) = pied du pot."""
    m = [ellipse(0, 0, 70, 9, "#000", opacity=0.12)]
    for (x0, y0), (x1, y1) in _RAMEAUX:
        ep = 12 if x0 == 0 and x1 == 0 else 7
        m.append(chemin(f"M {x0} {y0} Q {n((x0 + x1) / 2 + 10)} {n((y0 + y1) / 2)} {x1} {y1}", stroke="#6d4424", sw=ep))
    for k, (ax, ay) in enumerate(_ACCROCHES[:feuilles]):
        m.append(trait(ax, ay, ax, ay + 18, "#868e96", 1.5))
        m.append(feuille_erable(ax, ay + 44, 0.62, COULEURS_FEUILLES[k % len(COULEURS_FEUILLES)], rot=(k * 23) % 30 - 15,
                                papier=True, ecrit=True))
    m += [chemin("M -62 -100 L 62 -100 L 48 0 L -48 0 Z", volume(pot, 0.3, 0.75)),
          rect(-70, -112, 140, 22, _assombrir(pot, 0.85), rx=6)]
    return place(m, x, y, s)


def panier_pommes(x, y, s=1.0, plein=True):
    """Panier d'osier plein de pommes ; (x, y) = milieu du fond."""
    m = [chemin("M -58 -50 Q -58 -130 0 -130 Q 58 -130 58 -50", stroke="#8d5524", sw=9)]
    if plein:
        for k, (px, py) in enumerate(((-36, -56), (-6, -62), (24, -58), (44, -50), (-20, -74), (12, -78))):
            m.append(pomme(px, py, 0.75, ("#e03131", "#f03e3e", "#94d82d")[k % 3]))
    m += [chemin("M -64 -54 L 64 -54 L 52 0 L -52 0 Z", volume("#c68642", 0.3, 0.75)),
          chemin("M -62 -40 L 62 -40 M -59 -26 L 59 -26 M -56 -12 L 56 -12", stroke="#8d5524", sw=3, opacity=0.6),
          rect(-68, -60, 136, 10, "#8d5524", rx=5)]
    return place(m, x, y, s)


def courge(x, y, s=1.0, couleur="#fd7e14", forme="ronde", rot=0):
    """Courge du potager : "ronde" (citrouille), "longue" ou "tordue" ; (x, y) = base."""
    fonce = _assombrir(couleur, 0.8)
    if forme == "ronde":
        m = [ellipse(-40, -48, 40, 46, volume(fonce, 0.3, 0.7)), ellipse(40, -48, 40, 46, volume(fonce, 0.3, 0.7)),
             ellipse(0, -50, 46, 50, volume(couleur, 0.35, 0.75)), rect(-6, -114, 12, 22, "#5c940d", rx=4)]
    elif forme == "longue":
        m = [chemin("M -14 -110 Q 18 -112 18 -70 Q 40 -50 34 -20 Q 26 4 0 2 Q -28 4 -34 -20 Q -40 -50 -16 -70 Q -20 -108 -14 -110 Z",
                    volume(couleur, 0.35, 0.75)), rect(-4, -124, 8, 16, "#5c940d", rx=3)]
    else:
        m = [chemin("M -40 -10 Q -46 -50 -10 -50 Q 20 -52 26 -84 Q 34 -110 50 -100 Q 46 -70 44 -40 Q 40 0 0 0 Q -36 2 -40 -10 Z",
                    volume(couleur, 0.35, 0.75)), rect(44, -114, 8, 16, "#5c940d", rx=3)]
    return place(m, x, y, s, rot=rot)


def tarte(x, y, s=1.0, cuite=True):
    """Tarte aux pommes à croisillons ; (x, y) = dessous du moule."""
    pate = "#e8a95c" if cuite else "#f3d9a4"
    m = [chemin("M -80 -26 L 80 -26 L 68 0 L -68 0 Z", volume("#adb5bd", 0.3, 0.75)),
         ellipse(0, -26, 80, 22, _assombrir(pate, 0.85)), ellipse(0, -28, 70, 17, "#e9b949")]
    for k in range(-2, 3):
        m.append(trait(k * 26 - 14, -44, k * 26 + 14, -12, pate, 6))
        m.append(trait(k * 26 + 14, -44, k * 26 - 14, -12, pate, 6))
    m.append(ellipse(0, -28, 74, 19, "none", stroke=pate, stroke_width=8))
    return place(m, x, y, s)


def dinde(x, y, s=1.0):
    """Dinde rôtie sur son plat ; (x, y) = dessous du plat."""
    peau = "#c8742c"
    m = [ellipse(0, -8, 150, 26, "#f1f3f5", stroke="#ced4da", stroke_width=3),
         ellipse(0, -12, 130, 18, "#e9ecef")]
    for sgn in (-1, 1):
        m += [ellipse(sgn * 92, -50, 40, 24, volume(peau, 0.35, 0.7), rot=sgn * 30),
              rect(sgn * 120 - 5, -84, 10, 26, "#fff4e6", rx=4, transform=f"rotate({sgn * 30} {sgn * 120} -72)"),
              cercle(sgn * 128, -88, 8, "#ffffff"), cercle(sgn * 136, -84, 6, "#ffffff")]
    m += [ellipse(0, -56, 100, 56, volume(peau, 0.4, 0.7)),
          ellipse(-30, -84, 34, 14, "#fff", opacity=0.3, rot=-10)]
    for k, (px, py) in enumerate(((-120, -20), (-60, -14), (70, -14), (120, -22), (0, -12))):
        m.append(cercle(px, py, 8, "#51cf66" if k % 2 else "#2f9e44"))
    return place(m, x, y, s)


def voiture(x, y, s=1.0, couleur="#e67700", flip=False):
    """Petite voiture vue de côté ; (x, y) = sol, au milieu."""
    fonce = _assombrir(couleur, 0.75)
    m = [ellipse(0, 0, 160, 10, "#000", opacity=0.15),
         chemin("M -150 -28 Q -152 -72 -110 -76 L -70 -78 Q -42 -132 16 -134 L 58 -134 Q 100 -132 122 -82 L 140 -78 "
                "Q 162 -72 162 -40 L 162 -26 Q 162 -14 150 -14 L -140 -14 Q -150 -14 -150 -28 Z", volume(couleur, 0.3, 0.75)),
         chemin("M -56 -82 Q -36 -122 6 -122 L 6 -82 Z", "#a5d8ff"), chemin("M 20 -82 L 20 -122 L 56 -122 Q 92 -120 108 -82 Z", "#a5d8ff"),
         trait(-150, -48, 160, -48, fonce, 3, opacity=0.6), rect(146, -66, 14, 12, "#fff3bf", rx=3), rect(-150, -64, 10, 12, "#fa5252", rx=3)]
    for wx in (-92, 100):
        m += [cercle(wx, -14, 32, "#343a40"), cercle(wx, -14, 15, "#ced4da"), cercle(wx, -14, 5, "#868e96")]
    return place(m, x, y, s, flip=flip)


def ciseaux(x, y, s=1.0, rot=0):
    return place([ellipse(-10, 18, 8, 11, "none", stroke="#e03131", stroke_width=5), ellipse(10, 18, 8, 11, "none", stroke="#e03131", stroke_width=5),
                  poly([(-4, 8), (4, -40), (8, -38), (2, 8)], "#ced4da"), poly([(4, 8), (-4, -40), (-8, -38), (-2, 8)], "#adb5bd")], x, y, s, rot=rot)


def crayon(x, y, s=1.0, couleur="#e03131", rot=0):
    return place([rect(-5, -50, 10, 46, couleur, rx=2), poly([(-5, -4), (5, -4), (0, 10)], "#ffe8cc"), poly([(-2, 4), (2, 4), (0, 10)], "#343a40")], x, y, s, rot=rot)


# --- Décors ----------------------------------------------------------------------

def automne(S, horizon=560, sol_y=630, graine=2):
    """Campagne d'automne : ciel clair, collines rousses, herbe jaunie."""
    ciel(S, "#74c0fc", "#fff4e6")
    S.add(nuage(160, 130, 0.8), nuage(620, 90, 0.6))
    collines(S, horizon, "#e9c46a", graine=graine)
    sol(S, sol_y, "#b5c97a")


def maison_grand_maman(x, y, s=1.0):
    return maison(x, y, s, mur="#fff4e6", toit="#a61e4d", porte="#5c940d", volets="#5c940d")


def salle(S, y=600, soir=False):
    """La grande pièce de la maison de Grand-maman, avec sa fenêtre sur les érables."""
    piece(S, "chaumiere", y)
    if soir:
        dehors = g([rect(0, 0, 800, 800, lineaire([(0, "#5f3dc4"), (0.5, "#f76707"), (1, "#ffd8a8")])),
                    cercle(640, 260, 40, "#ffd43b", opacity=0.8)])
    else:
        dehors = g([rect(0, 0, 800, 800, "#a5d8ff"), cercle(560, 210, 60, "#f76707"), cercle(640, 230, 50, "#e03131"),
                    cercle(700, 200, 46, "#fab005"), rect(0, 250, 800, 60, "#b5c97a")])
    S.add(fenetre(530, 90, 200, 180, "#a5d8ff", cadre="#fff4e6", rideaux="#e67700", contenu=dehors))
    if soir:
        S.ambiance("interieur")


def cuisine(S, y=600):
    piece(S, "cuisine", y)
    S.add(fenetre(80, 90, 180, 150, "#a5d8ff", cadre="#ffffff", rideaux="#a61e4d",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), cercle(140, 200, 50, "#f76707"), cercle(210, 210, 44, "#fab005")])))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    automne(S, 560, 650)
    S.add(erable(110, 640, 1.3), erable(700, 630, 1.15, "#e03131", "#c92a2a"))
    feuilles_volantes(S, (40, 280, 760, 600), 12, graine=7)
    tapis_feuilles(S, 660, 790, 18, graine=2)
    S.add(courge(80, 770, 0.8), courge(700, 780, 0.7, "#fab005", "longue"))
    S.add(arbre_mercis(440, 790, 1.05, feuilles=13))
    S.add(grand_maman(650, 770, 1.2, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(felix(110, 790, 1.05, expr="rire", bras="tient", regard=(1, -0.3), objet=pomme(68, -146, 1.1)))
    S.add(rosalie(270, 790, 1.3, expr="rire", bras="leve_doigt", regard=(1, -0.6),
                  objet=feuille_erable(52, -236, 0.85, "#e03131", papier=True, ecrit=True)))
    return S


def vignette():
    S = Scene(400, 270)
    feuilles_volantes(S, (30, 30, 370, 200), 6, graine=11)
    S.add(arbre_mercis(200, 262, 0.62, feuilles=14))
    return S


def p01():
    """Plan large : l'arrivée chez Grand-maman, sous les érables."""
    S = Scene()
    automne(S)
    S.add(erable(80, 620, 1.1), erable(300, 600, 0.8, "#fab005", "#f59f00"))
    S.add(maison_grand_maman(560, 640, 0.95))
    S.add(erable(760, 640, 1.0, "#e03131", "#c92a2a"))
    feuilles_volantes(S, (0, 140, 800, 520), 14, graine=3)
    S.add(chemin("M 0 700 Q 300 680 520 650 L 600 650 Q 360 700 0 760 Z", "#d9c4a0"))
    S.add(voiture(150, 720, 0.8, flip=False))
    tapis_feuilles(S, 690, 790, 16, graine=8)
    S.add(papa(250, 770, 0.95, expr="sourire", bras="coucou", regard=(1, 0)))
    S.add(felix(350, 780, 0.95, expr="rire", bras="saute", regard=(1, 0)))
    S.add(rosalie(470, 770, 0.95, expr="rire", bras="court", regard=(1, 0)))
    S.add(grand_maman(640, 740, 0.95, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(560, 160, 340, 80, "Vous voilà, mes trésors !", 26, pointe=(630, 520)))
    return S


def p02():
    """Plan moyen : au verger, Papa cueille, Rosalie remplit le panier, Félix croque."""
    S = Scene()
    automne(S, 520, 620, graine=4)
    S.add(arbre(160, 610, 1.9, "#94d82d", "#74b816", fruits="#e03131"))
    S.add(arbre(640, 600, 1.6, "#a9e34b", "#82c91e", fruits="#e03131"))
    tapis_feuilles(S, 640, 790, 10, graine=5)
    S.add(papa(250, 760, 1.25, expr="concentre", bras="haut", regard=(0, -1), pas="pointe",
               objet=pomme(*ancre(70, -165, "haut", "adulte"), 1.1)))
    S.add(rosalie(470, 780, 1.2, expr="rire", bras="porte", regard=(-1, -0.5), objet=panier_pommes(0, -20, 0.9)))
    S.add(felix(640, 790, 1.15, expr="miam", bras="tient", regard=(-1, 0), objet=pomme(68, -146, 1.1)))
    S.add(texte(650, 470, "Crunch !", 48, "#e03131", contour="#fff", rot=8))
    for px, py in ((540, 770), (360, 790), (110, 780)):
        S.add(pomme(px, py, 0.9, "#e03131"))
    return S


def p03():
    """Gros plan : Félix essaie de soulever la plus grosse courge."""
    S = Scene()
    automne(S, 500, 600, graine=6)
    S.add(erable(700, 590, 1.2))
    for k, (cx, f, c) in enumerate(((80, "longue", "#fab005"), (210, "tordue", "#ffd43b"), (620, "ronde", "#f76707"),
                                    (720, "longue", "#e8590c"))):
        S.add(courge(cx, 700 + (k % 2) * 20, 0.8, c, f))
    for k in range(6):
        S.add(chemin(f"M {k * 140} 640 q 40 -20 80 0", stroke="#5c940d", sw=6))
    S.add(rosalie(560, 760, 1.2, expr="rire", bras="joues", regard=(-1, 0.3)))
    S.add(felix(380, 770, 1.3, expr="concentre", bras="ouverts", regard=(0, 0.5)))
    S.add(courge(380, 800, 1.15, "#fd7e14", "ronde"))
    S.add(mouvement(270, 600, 1.0, "#e67700"), mouvement(490, 620, 1.0, "#e67700", rot=180))
    S.camera(1.35, 420, 560)
    S.dessus(texte(250, 130, "Hmmmpf !", 64, "#e67700", contour="#fff", rot=-6))
    S.cachette(605, 259, "air")
    return S


def p04():
    """Plan moyen : la tarte aux pommes ; « C'est quoi, l'Action de grâce ? »"""
    S = Scene()
    cuisine(S)
    S.add(grand_maman(560, 680, 1.4, expr="content", bras="porte", regard=(-1, 0.3),
                      objet=tarte(*ancre(0, -60, "porte", "ancien", "ronde"), 0.9)))
    S.add(table(400, 800, 600, 160, "#c68642", nappe="#fff4e6"))
    S.add(bol(250, 640, 0.8, "#ffd8a8", "#ffe066"))
    for px in (320, 360, 390):
        S.add(pomme(px, 632, 0.8, "#e03131"))
    S.add(rosalie(180, 760, 1.25, expr="surpris", bras="pense", regard=(1, -0.4)))
    S.add(bulle(220, 190, 340, 100, "Grand-maman, c'est quoi,\nl'Action de grâce ?", 24, pointe=(200, 440)))
    S.add(bulle(560, 160, 380, 100, "C'est la fête où\nl'on dit merci !", 28, pointe=(560, 360)))
    return S


def p05():
    """Gros plan : Rosalie réfléchit… et a une idée."""
    S = Scene()
    cuisine(S)
    S.add(table(400, 900, 760, 230, "#c68642", nappe="#fff4e6"))
    S.add(rosalie(400, 820, 1.7, expr="malin", bras="leve_doigt", regard=(-0.5, -1)))
    S.camera(1.3, 400, 500)
    S.dessus(pensee(560, 200, 130, g([arbre_mercis(560, 300, 0.42, feuilles=10)]), depuis=S.vers_page(470, 380)))
    S.dessus(paillettes(220, 220, 1.4, "#fab005"))
    S.cachette(120, 330, "air")
    return S


def p06():
    """Plan large : dehors, la belle branche tombée et les feuilles d'érable."""
    S = Scene()
    automne(S, 540, 620, graine=8)
    S.add(maison_grand_maman(140, 620, 0.6))
    S.add(erable(420, 620, 1.5), erable(700, 630, 1.25, "#e03131", "#c92a2a"))
    feuilles_volantes(S, (0, 140, 800, 560), 16, graine=9)
    tapis_feuilles(S, 650, 790, 26, graine=6)
    S.add(rosalie(320, 780, 1.15, expr="fier", bras="porte", regard=(1, 0),
                  objet=place([chemin("M -140 0 Q -40 -20 120 -60", stroke="#6d4424", sw=14),
                               chemin("M -40 -18 Q -10 -70 20 -100 M 40 -36 Q 80 -60 110 -120", stroke="#6d4424", sw=8)], 0, -76)))
    S.add(felix(560, 780, 1.1, expr="rire", bras="haut", regard=(-1, -0.4),
                objet=g([feuille_erable(-66, -184, 0.6, "#e03131", -20), feuille_erable(70, -186, 0.6, "#fab005", 20)])))
    S.add(bulle(620, 190, 300, 80, "Pour les modèles !", 30, pointe=(580, 480)))
    return S


def p07():
    """Plan moyen : on découpe les feuilles en papier, la branche dans son pot."""
    S = Scene()
    salle(S)
    S.add(papa(560, 690, 1.3, expr="concentre", bras="porte", regard=(-1, 0.4),
               objet=g([ciseaux(*ancre(30, -74, "porte", "adulte"), 1.0, rot=30),
                        feuille_erable(*ancre(-20, -84, "porte", "adulte"), 0.8, "#f76707", papier=True)])))
    S.add(table(400, 800, 620, 150, "#a0693a", nappe=None))
    S.add(arbre_mercis(400, 640, 0.75, feuilles=0))
    for k, (px, c) in enumerate(((190, "#e03131"), (250, "#fab005"), (620, "#e8590c"))):
        S.add(feuille_erable(px, 636, 0.55, c, rot=k * 30 - 20, papier=True))
    S.add(rect(150, 640, 90, 10, "#ffd43b"), rect(240, 642, 70, 8, "#e03131"))
    S.add(rosalie(200, 760, 1.15, expr="content", bras="tient", regard=(1, -0.2),
                  objet=feuille_erable(68, -146, 0.8, "#e03131", papier=True)))
    S.add(felix(670, 790, 1.0, expr="concentre", bras="tient", regard=(-1, 0.5), flip=True, objet=crayon(68, -146, 1.0, "#1c7ed6", rot=20)))
    return S


def p08():
    """Plan moyen : Tante Nadia et le cousin Amir arrivent avec la soupe."""
    S = Scene()
    salle(S)
    # la porte grande ouverte sur l'automne
    S.add(rect(95, 190, 210, 410, "#fff4e6"), rect(105, 200, 190, 400, lineaire([(0, "#a5d8ff"), (0.6, "#fff4e6"), (0.61, "#b5c97a"), (1, "#94a85a")])))
    S.add(cercle(150, 330, 50, "#f76707"), cercle(230, 350, 44, "#e03131"), rect(185, 360, 12, 90, "#6d4424"))
    S.add(poly([(105, 200), (60, 220), (60, 590), (105, 600)], cylindre("#5c940d", 0.15, 0.7)))
    S.add(arbre_mercis(620, 600, 0.8, feuilles=0))
    S.add(nadia(170, 760, 1.25, expr="rire", bras="porte", regard=(1, 0),
                objet=bol(*ancre(0, -50, "porte", "adulte", "fine"), 0.6, "#fd7e14", "#ffa94d", cuillere=False)))
    S.add(amir(330, 780, 1.15, expr="surpris", bras="designe", regard=(1, -0.3)))
    S.add(rosalie(520, 790, 1.15, expr="fier", bras="montre", regard=(-1, 0)))
    S.add(bulle(250, 130, 400, 90, "Qu'est-ce que c'est,\ncet arbre tout nu ?", 26, pointe=(330, 470)))
    S.add(bulle(600, 270, 320, 80, "L'arbre aux mercis !", 28, pointe=(520, 500)))
    S.cachette(760, 740)
    return S


def p09():
    """Plan large : chacun écrit son merci et l'accroche à la branche."""
    S = Scene()
    salle(S)
    S.add(table(400, 760, 460, 130, "#a0693a"))
    S.add(arbre_mercis(400, 618, 0.95, feuilles=8))
    S.add(papa(150, 770, 1.05, expr="sourire", bras="leve_doigt", regard=(1, -0.3),
               objet=feuille_erable(*ancre(52, -216, "leve_doigt", "adulte"), 0.6, "#fab005", papier=True, ecrit=True)))
    S.add(grand_maman(660, 770, 1.05, expr="content", bras="mains_jointes", regard=(-1, -0.3)))
    S.add(amir(560, 790, 0.95, expr="rire", bras="tient", regard=(-1, -0.5),
               objet=feuille_erable(68, -146, 0.7, "#e8590c", papier=True, ecrit=True)))
    S.add(felix(280, 795, 0.95, expr="fier", bras="haut", regard=(1, -0.5),
                objet=place([feuille_erable(0, 0, 0.8, "#e03131", papier=True), coeur(0, -2, 0.3, "#fff")], 70, -190)))
    S.add(bulle(150, 160, 280, 90, "Merci pour\nles pommes !", 26, pointe=(160, 440)))
    S.add(bulle(640, 330, 260, 90, "Merci pour\nmes amis !", 26, pointe=(570, 560)))
    S.cachette(70, 320, "air")
    return S


def p10():
    """Gros plan : Grand-maman lit la dernière feuille, celle de Rosalie."""
    S = Scene()
    salle(S, soir=True)
    S.add(arbre_mercis(640, 700, 1.1, feuilles=14))
    S.add(grand_maman(390, 820, 1.75, expr="content", bras="porte", regard=(0, 0.6), larmes=True,
                      objet=feuille_erable(*ancre(0, -50, "porte", "ancien", "ronde"), 1.2, "#e03131", papier=True, ecrit=True)))
    S.add(rosalie(190, 820, 1.4, expr="content", bras="mains_jointes", regard=(1, -0.4)))
    S.camera(1.3, 380, 520)
    S.dessus(bulle(400, 100, 440, 90, "Merci d'être\ntous ensemble.", 32, fill="#fff4e6"))
    S.cachette(180, 238, "air")
    return S


def p11():
    """Plan large : le grand repas ; l'arbre aux mercis au milieu de la table."""
    S = Scene()
    salle(S, soir=True)
    S.add(lampe(120, 590, 0.9, abat="#ffd8a8"))
    for qui, x, k in ((nadia, 120, dict(flip=False)), (papa, 680, dict(flip=True)), (grand_maman, 560, dict(flip=True)),
                      (amir, 250, dict())):
        S.add(qui(x, 700, 1.0, expr="rire", bras="leve_doigt", regard=(1 if x < 400 else -1, 0), **k))
    S.add(table(400, 800, 720, 150, "#a0693a", nappe="#fff4e6"))
    S.add(arbre_mercis(400, 650, 0.7, feuilles=14))
    S.add(dinde(240, 660, 0.6), tarte(580, 650, 0.7), bol(680, 650, 0.6, "#fd7e14", "#ffa94d", cuillere=False))
    for px in (130, 300, 500, 650):
        S.add(assiette(px, 672, 1.0, bord="#a61e4d"))
    S.add(rosalie(330, 800, 1.0, expr="rire", bras="leve_doigt", regard=(1, -0.3)))
    S.add(felix(470, 805, 0.95, expr="rire", bras="saute", regard=(-1, -0.3)))
    S.add(texte(400, 70, "Joyeuse Action de grâce !", 42, "#e67700", contour="#fff"))
    S.cachette(760, 740)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("arbre-seul.svg", vignette),
    ("01-chez-grand-maman.svg", p01), ("02-le-verger.svg", p02), ("03-la-grosse-courge.svg", p03),
    ("04-la-tarte.svg", p04), ("05-une-idee.svg", p05), ("06-la-branche.svg", p06),
    ("07-on-decoupe.svg", p07), ("08-l-arbre-tout-nu.svg", p08), ("09-les-mercis.svg", p09),
    ("10-la-derniere-feuille.svg", p10), ("11-le-grand-repas.svg", p11),
]
