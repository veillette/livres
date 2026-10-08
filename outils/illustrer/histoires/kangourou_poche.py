"""Le petit kangourou dans la poche — un marsupial.

Le bébé kangourou naît minuscule (environ 2 cm, la taille d'un haricot),
aveugle et sans poils. Il grimpe tout seul dans la poche de sa mère en
s'accrochant à ses poils, s'accroche à une tétine et y reste environ six
mois. Il sort ensuite la tête, puis fait ses premiers sauts, et plonge dans
la poche tête la première au moindre danger. Le kangourou saute avec ses
grandes pattes arrière ; sa queue l'équilibre. Aux heures chaudes il se
repose à l'ombre et se lèche les avant-bras pour se rafraîchir. Les mâles
« boxent ». Vers huit mois, le petit quitte la poche mais y passe encore la
tête pour téter.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, fleche_courbe

ID = "kangourou-poche"
ROUX = "#d9822b"
CLAIR = "#f3d9b1"


# --- Personnages ------------------------------------------------------------

def kangourou(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), petit=None, saut=False, bras="bas",
              couleur=ROUX, langue=False):
    """Kangourou assis sur ses pattes arrière, de profil, tête à droite ;
    (x, y) = sous les pattes. petit : None, "tete" (le petit sort la tête de
    la poche), "plonge" (on voit ses pattes dépasser), "boit" (un grand petit
    passe la tête dans la poche — dessiné à part). bras : "bas", "boxe",
    "leche" (bras à la bouche)."""
    ys, bs, ss = EXPRESSIONS[expr]
    c, fonce = couleur, _assombrir(couleur, 0.85)
    m = []
    # queue
    m.append(chemin("M -30 -70 Q -110 -40 -190 -8 Q -196 2 -184 6 Q -100 -10 -10 -30 Z", c))
    # cuisse et pied
    if saut:
        m.append(chemin("M -20 -110 Q -90 -60 -150 -50", stroke=c, sw=40))
        m.append(chemin("M -150 -50 L -230 -30", stroke=fonce, sw=18))
    else:
        m.append(ellipse(10, -8, 64, 11, fonce))
        m.append(ellipse(-20, -66, 52, 44, c, rot=-20))
    # corps
    m.append(ellipse(14, -150, 52, 96, c, rot=18))
    m.append(ellipse(30, -132, 30, 66, CLAIR, rot=18))
    # poche
    m.append(chemin("M 6 -120 Q 30 -96 66 -128", stroke=fonce, sw=5))
    if petit == "tete":
        m.append(g([ellipse(40, -140, 16, 14, c), ellipse(54, -136, 12, 8, c), ellipse(30, -160, 6, 14, c, rot=-20),
                    ellipse(40, -162, 6, 14, c, rot=10), cercle(44, -142, 3.5, ENCRE), cercle(62, -138, 3, ENCRE),
                    joue(50, -132, 0.5)]))
        m.append(chemin("M 6 -120 Q 30 -96 66 -128 Q 40 -114 6 -120 Z", c))
    elif petit == "plonge":
        m.append(chemin("M 30 -126 Q 20 -160 4 -176 M 44 -126 Q 46 -160 36 -180", stroke=c, sw=10))
        m.append(chemin("M 36 -124 Q 10 -150 -2 -150", stroke=c, sw=7))
        m.append(chemin("M 6 -120 Q 30 -96 66 -128 Q 40 -114 6 -120 Z", c))
    # bras
    if bras == "boxe":
        m.append(chemin("M 50 -200 Q 90 -210 110 -230", stroke=c, sw=14) + cercle(112, -232, 10, fonce))
        m.append(chemin("M 46 -186 Q 86 -180 104 -190", stroke=fonce, sw=12) + cercle(106, -190, 9, fonce))
    elif bras == "leche":
        m.append(chemin("M 50 -196 Q 90 -200 96 -236", stroke=c, sw=14) + cercle(96, -238, 9, fonce))
    else:
        m.append(chemin("M 50 -196 Q 76 -176 72 -150", stroke=c, sw=13) + cercle(72, -148, 8, fonce))
    # tête
    m.append(ellipse(26, -306, 12, 34, c, rot=-24) + ellipse(26, -304, 6, 24, "#f3c4c4", rot=-24))
    m.append(ellipse(46, -310, 12, 34, c, rot=-8) + ellipse(46, -308, 6, 24, "#f3c4c4", rot=-8))
    m.append(ellipse(50, -258, 34, 28, c))
    m.append(ellipse(82, -250, 26, 18, c))
    m.append(ellipse(84, -244, 18, 10, CLAIR))
    m.append(ellipse(104, -254, 6, 5, ENCRE))
    m.append(oeil(62, -266, ys, regard, taille=0.85))
    m.append(joue(76, -244, 0.7))
    if langue:
        m.append(ellipse(100, -238, 6, 8, "#ff8787"))
    else:
        m.append(place(bouche(0, 0, bs, 0.6), 94, -244))
    return place(m, x, y, s, flip=flip, rot=-35 if saut else 0)


def kangourou_saut(x, y, s=1.0, flip=False, rot=0, expr="rire", regard=(1, 0), couleur=ROUX, sans_tete=False):
    """Kangourou en plein bond, le corps à l'horizontale, pattes arrière et
    queue tendues derrière lui ; (x, y) = centre du corps, tête à droite."""
    ys, bs, ss = EXPRESSIONS[expr]
    c, fonce = couleur, _assombrir(couleur, 0.85)
    m = [chemin("M -70 -20 Q -170 -20 -270 10 Q -276 22 -262 24 Q -160 14 -60 14 Z", c),
         chemin("M -60 30 Q -110 70 -190 80", stroke=c, sw=26),
         chemin("M -186 80 L -262 96", stroke=fonce, sw=16),
         ellipse(-50, 14, 52, 38, c, rot=20),
         ellipse(10, 0, 96, 50, c, rot=-12),
         ellipse(24, 18, 62, 24, CLAIR, rot=-12),
         chemin("M 70 20 Q 96 40 104 60", stroke=c, sw=12) + cercle(104, 62, 8, fonce)]
    if not sans_tete:
        m += [ellipse(66, -86, 12, 34, c, rot=-60), ellipse(84, -94, 12, 34, c, rot=-46),
              ellipse(70, -86, 6, 24, "#f3c4c4", rot=-60),
              ellipse(100, -50, 34, 28, c), ellipse(132, -42, 26, 18, c), ellipse(134, -36, 18, 10, CLAIR),
              ellipse(154, -46, 6, 5, ENCRE), oeil(112, -58, ys, regard, taille=0.85), joue(126, -36, 0.7),
              place(bouche(0, 0, bs, 0.6), 144, -36)]
    return place(m, x, y, s, flip=flip, rot=rot)


def petit_kangourou(x, y, s=1.0, flip=False, expr="sourire", **k):
    """Le petit qui a grandi : même dessin, plus clair."""
    return kangourou(x, y, s, flip=flip, expr=expr, couleur="#e8a35a", **k)


def bebe_minuscule(x, y, s=1.0, rot=0):
    """Nouveau-né : tout rose, sans poils, les yeux fermés, de la taille d'un haricot."""
    m = [ellipse(0, 0, 20, 34, "#ffc9c9"), cercle(4, -36, 16, "#ffc9c9"), ellipse(16, -34, 8, 6, "#ffc9c9"),
         chemin("M 6 -40 q 4 3 8 0", stroke="#c2255c", sw=2),
         chemin("M -10 -10 Q -26 -14 -30 -4 M 12 -10 Q 26 -18 30 -10", stroke="#ffa8a8", sw=6),
         chemin("M -6 28 Q -14 40 -20 44 M 8 28 Q 12 40 18 44", stroke="#ffa8a8", sw=4)]
    return place(m, x, y, s, rot=rot)


def haricot(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 14, 26, "#d9480f"), ellipse(-4, -8, 4, 8, "#ffffff", opacity=0.35)], x, y, s, rot=rot)


def bush(S, y=560, chaud=False):
    """Paysage d'Australie : terre rouge, herbe sèche, eucalyptus."""
    S.add(rect(0, 0, 800, 800, S.degrade(["#74c0fc", "#fff3bf"] if not chaud else ["#ffd8a8", "#fff3bf"])))
    S.add(chemin(f"M 0 {y - 40} Q 200 {y - 100} 400 {y - 50} T 800 {y - 70} L 800 {y + 10} L 0 {y + 10} Z", "#e8a35a"))
    S.add(rect(0, y, 800, 800 - y, "#e9a15c"))
    r = random.Random(3)
    for _ in range(24):
        x0, y0 = r.uniform(10, 790), r.uniform(y + 20, 790)
        S.add(chemin(f"M {n(x0 - 8)} {n(y0)} L {n(x0 - 12)} {n(y0 - 20)} M {n(x0)} {n(y0)} L {n(x0)} {n(y0 - 26)} M {n(x0 + 8)} {n(y0)} L {n(x0 + 13)} {n(y0 - 19)}",
                     stroke="#c08a52", sw=3.5))


def eucalyptus(x, y, s=1.0):
    m = [chemin("M -14 0 Q -6 -120 -20 -220 M 14 0 Q 10 -120 30 -240 M 0 -120 Q 40 -170 70 -200", stroke="#f1f3f5", sw=18),
         ellipse(-40, -240, 70, 40, "#8ab88a"), ellipse(50, -260, 80, 44, "#94c494"), ellipse(80, -210, 50, 30, "#8ab88a")]
    return place(m, x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    bush(S, 610)
    S.add(eucalyptus(680, 640, 1.1))
    S.add(kangourou(340, 760, 1.6, expr="content", petit="tete"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(kangourou(200, 262, 0.7, expr="content", petit="tete"))
    return S


def p01():
    S = Scene()
    bush(S, 580)
    S.add(eucalyptus(130, 600, 1.0), eucalyptus(700, 590, 0.8))
    S.add(kangourou(380, 740, 1.5, expr="sourire"))
    S.add(soleil(650, 100, 50))
    return S


def p02():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(cercle(400, 400, 260, "#ffe8cc"))
    S.add(bebe_minuscule(320, 420, 3.2))
    S.add(haricot(560, 420, 3.2, rot=10))
    S.add(etiquette(320, 640, "le bébé", 36, "#d9480f"), etiquette(560, 640, "un haricot", 36, "#d9480f"))
    S.add(texte(400, 130, "2 centimètres !", 54, "#d9480f", contour="#fff"))
    S.cachette(400, 730, "air")
    return S


def p03():
    S = Scene()
    fond(S, "#f3d9b1")
    r = random.Random(4)
    for _ in range(80):
        x0, y0 = r.uniform(0, 800), r.uniform(0, 800)
        S.add(trait(x0, y0, x0 + 18, y0 + 26, "#e8b98a", 4))
    S.add(rect(0, 0, 800, 220, "#e8b98a"))
    S.add(chemin("M 0 220 Q 400 300 800 220 L 800 260 Q 400 340 0 260 Z", "#c08a52"))
    S.add(chemin("M 360 760 Q 300 600 380 470 Q 430 380 400 300", stroke="#d9480f", sw=5, stroke_dasharray="14 12"))
    S.add(bebe_minuscule(395, 330, 2.2, rot=-10))
    S.add(fleche(400, 300, 400, 250, "#d9480f", 6, 22))
    S.add(texte(600, 560, "Grimpe, grimpe…", 44, "#d9480f", contour="#fff"))
    S.cachette(650, 70, "air")
    return S


def p04():
    S = Scene()
    fond(S, "#ffe8cc")
    S.add(ellipse(400, 420, 330, 280, "#f3d9b1"))
    S.add(ellipse(400, 470, 250, 190, "#e8b98a"))
    S.add(place(g([ellipse(0, 0, 70, 110, "#ffc9c9", rot=20), cercle(30, -100, 50, "#ffc9c9"), ellipse(70, -96, 22, 16, "#ffc9c9"),
                   oeil(40, -110, "fermes", taille=1.2), joue(56, -86, 1.0),
                   chemin("M -20 -150 Q -30 -200 -10 -210", stroke="#ffa8a8", sw=16)]), 380, 500, 1.1))
    S.add(cercle(486, 418, 8, "#f783ac"))
    S.add(coeur(640, 220, 1.4, "#ff8787"))
    S.add(texte(400, 120, "Bien au chaud…", 50, "#d9480f", contour="#fff"))
    S.cachette(400, 730, "air")
    return S


def p05():
    S = Scene()
    bush(S, 580)
    S.add(eucalyptus(680, 600, 0.9))
    S.add(kangourou(360, 760, 1.6, expr="content", petit="tete"))
    S.add(texte(560, 220, "Coucou !", 60, "#d9480f", contour="#fff"))
    return S


def p06():
    S = Scene()
    bush(S, 580)
    S.add(kangourou(220, 740, 1.2, expr="fier", regard=(1, 0.3)))
    S.add(chemin("M 380 760 Q 470 560 560 640", stroke="#868e96", sw=4, stroke_dasharray="12 10"))
    S.add(kangourou_saut(590, 580, 0.8, expr="rire", couleur="#f0b46c", rot=-10))
    return S


def p07():
    S = Scene()
    bush(S, 580)
    S.add(kangourou(360, 760, 1.6, expr="surpris", petit="plonge", regard=(1, 0)))
    S.add(texte(620, 300, "Vite !", 70, "#d9480f", contour="#fff"))
    S.add(mouvement(470, 480, 1.0, "#495057", rot=-90))
    return S


def p08():
    S = Scene()
    bush(S, 600)
    S.add(chemin("M 60 760 Q 230 420 400 640 Q 560 420 740 620", stroke="#868e96", sw=5, stroke_dasharray="16 12"))
    S.add(kangourou_saut(420, 460, 1.15, expr="rire", rot=-15))
    S.add(texte(620, 220, "Boing ! Boing !", 48, "#d9480f", contour="#fff"))
    S.add(etiquette(150, 330, "la queue", 32, "#495057"), fleche(170, 350, 190, 450, "#495057", 5, 16))
    return S


def p09():
    S = Scene()
    bush(S, 580, chaud=True)
    S.add(soleil(640, 110, 70))
    S.add(eucalyptus(330, 640, 1.5))
    S.add(ellipse(340, 720, 260, 40, "#c06a2a", opacity=0.5))
    S.add(kangourou(360, 740, 1.2, expr="content", bras="leche", langue=True))
    return S


def p10():
    S = Scene()
    bush(S, 580)
    S.add(kangourou(270, 760, 1.25, expr="concentre", bras="boxe"))
    S.add(kangourou(540, 760, 1.25, expr="malin", bras="boxe", flip=True, couleur="#c8742a"))
    S.add(eclat(405, 450, 0.8, "#ffd43b"))
    return S


def p11():
    S = Scene()
    bush(S, 580)
    S.add(petit_kangourou(450, 770, 0.85, flip=True, expr="miam", regard=(1, 0.5)))
    S.add(kangourou(270, 760, 1.5, expr="content", regard=(1, 0.6)))
    S.add(texte(600, 240, "Encore un peu de lait !", 36, "#d9480f", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("kangourou-seul.svg", vignette),
    ("01-en-australie.svg", p01), ("02-tout-petit.svg", p02), ("03-il-grimpe.svg", p03),
    ("04-dans-la-poche.svg", p04), ("05-coucou.svg", p05), ("06-premiers-sauts.svg", p06),
    ("07-vite-dans-la-poche.svg", p07), ("08-boing.svg", p08), ("09-a-l-ombre.svg", p09),
    ("10-la-boxe.svg", p10), ("11-trop-grand.svg", p11),
]
