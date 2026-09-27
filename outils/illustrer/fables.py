"""
Personnages et accessoires des fables de La Fontaine : corbeau, colombe, coq et
poule, cigogne, moucheron, chêne et roseau qui parlent, fromage, raisins,
puits, filet, grelot, pot au lait…

Les animaux « debout » (loup, lion, lièvre, rat, âne, chèvre, bœuf, cigale)
sont des espèces de `perso()` dans `base.py`. Mêmes conventions : page de
800 × 800, pieds en (0, 0).
"""
from base import *
from base import EXPRESSIONS, _assombrir
from objets import *
from fantastique import *
from sciences import canard, vent_visage, rafales, vent, fleche, ombre_sous, enfant, cheval, ondes, rayons_soleil


# ---------------------------------------------------------------------------
# Oiseaux
# ---------------------------------------------------------------------------

def fromage(x, y, s=1.0, rot=0):
    """Part de fromage (triangle à trous) ; (x, y) = centre."""
    m = [poly([(-34, 14), (34, 14), (26, -16)], "#ffd43b"),
         poly([(-34, 14), (26, -16), (22, -22), (-38, 8)], "#fab005"),
         cercle(-8, 6, 5, "#f59f00"), cercle(14, 2, 4, "#f59f00"), cercle(20, 10, 3, "#f59f00")]
    return place(m, x, y, s, rot=rot)


def corbeau(x, y, s=1.0, expr="fier", ailes="bas", bec_ouvert=False, flip=False, regard=(0, 0),
            fromage_bec=False, rot=0):
    """Corbeau noir, rond, avec un grand bec ; (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [oiseau(0, 0, 1.0, "#343a40", "#495057", expr=expr, ailes=ailes, regard=regard, pattes=True)]
    # yeux blancs pour qu'on les voie sur les plumes noires
    for sgn in (-1, 1):
        m.append(cercle(sgn * 15, -82, 12, "#fff"))
        m.append(oeil(sgn * 15, -82, ys, regard, taille=0.85))
    m.append(sourcils(15, -80, ss).replace(ENCRE, "#f1f3f5"))
    bec = "#212529"
    if bec_ouvert:
        m.append(poly([(-12, -72), (12, -72), (0, -96)], bec))
        m.append(poly([(-11, -66), (11, -66), (0, -40)], "#343a40"))
        m.append(poly([(-7, -68), (7, -68), (0, -58)], "#c92a2a"))
    else:
        m.append(poly([(-13, -74), (13, -74), (0, -44)], bec))
        m.append(trait(-6, -66, 6, -66, "#495057", 2))
    if fromage_bec:
        m.append(fromage(4, -42, 0.9, rot=-8))
    return place(m, x, y, s, flip=flip, rot=rot)


def colombe(x, y, s=1.0, **k):
    """Colombe blanche ; mêmes options qu'`oiseau()`."""
    k.setdefault("couleur", "#f8f9fa")
    k.setdefault("ventre", "#ffffff")
    return oiseau(x, y, s, **k)


def colombe_vol(x, y, s=1.0, flip=False, objet=None, expr="sourire"):
    """Colombe en vol, de profil (tête à droite) ; (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -40 0 L -86 -18 L -80 10 Z", "#dee2e6"),
         ellipse(0, 0, 50, 26, "#f8f9fa", stroke="#dee2e6", stroke_width=3),
         chemin("M -20 -8 Q -10 -90 50 -104 Q 26 -60 20 -10 Z", "#ffffff", stroke="#dee2e6", sw=3),
         cercle(46, -16, 22, "#f8f9fa", stroke="#dee2e6", stroke_width=3),
         poly([(64, -18), (82, -12), (64, -8)], "#ff922b"),
         ellipse(52, -6, 5, 3, ROSE, opacity=0.8),
         oeil(52, -20, ys, (1, 0), taille=0.7)]
    if objet:
        m.append(objet)
    return place(m, x, y, s, flip=flip)


def coq(x, y, s=1.0, poule=False, expr="fier", ailes="bas", bec_ouvert=False, flip=False,
        regard=(0, 0), couleur=None, ventre=None, rot=0):
    """Coq (ou poule) tout rond, avec crête, barbillons et plumes de queue."""
    if poule:
        couleur = couleur or "#e8a15c"
        ventre = ventre or "#fff4e6"
        plumes = [(-54, -80, "#c97a3a", 22), (-62, -62, "#d98b48", 18)]
    else:
        couleur = couleur or "#f8f9fa"
        ventre = ventre or "#ffffff"
        plumes = [(-56, -104, "#2f9e44", 34), (-66, -84, "#1c7ed6", 30), (-66, -60, "#e8590c", 26), (-58, -40, "#2b8a3e", 20)]
    m = []
    for px, py, c, r in plumes:
        m.append(ellipse(px, py, r * 0.45, r * 1.3, c, rot=-50 + (py + 100) * 0.4))
    m.append(oiseau(0, 0, 1.0, couleur, ventre, expr=expr, ailes=ailes, bec_ouvert=bec_ouvert, regard=regard,
                    pattes=True))
    crete = "#e03131"
    if poule:
        m += [cercle(-8, -114, 8, crete), cercle(4, -118, 9, crete), cercle(14, -112, 7, crete)]
        m.append(ellipse(0, -52, 5, 7, crete))
    else:
        m += [cercle(-14, -114, 11, crete), cercle(0, -122, 13, crete), cercle(14, -116, 11, crete)]
        m.append(ellipse(-4, -50, 6, 10, crete) + ellipse(5, -48, 6, 9, crete))
    return place(m, x, y, s, flip=flip, rot=rot)


def oeuf(x, y, s=1.0, couleur="#fff9f0", brille=False, rot=0):
    m = []
    if brille:
        m.append(ellipse(0, -30, 44, 52, "#fff3bf", opacity=0.7))
    m.append(ellipse(0, -30, 24, 32, couleur, stroke=_assombrir(couleur, 0.85), stroke_width=2))
    m.append(ellipse(-8, -42, 5, 9, "#fff", opacity=0.7, rot=-20))
    return place(m, x, y, s, rot=rot)


def oeuf_or(x, y, s=1.0, brille=True, rot=0):
    m = [oeuf(0, 0, 1.0, "#ffd43b", brille=brille)]
    if brille:
        for a in (-60, -20, 20, 60):
            r = math.radians(a - 90)
            m.append(trait(math.cos(r) * 40, -30 + math.sin(r) * 46, math.cos(r) * 54, -30 + math.sin(r) * 62, "#fab005", 4))
    return place(m, x, y, s, rot=rot)


def cigogne(x, y, s=1.0, expr="sourire", flip=False, bec_ouvert=False, regard=(1, 0), cou="droit"):
    """Cigogne de profil, tête à droite ; (x, y) = au sol sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    rouge = "#f76707"
    m = []
    for dx in (-10, 12):
        m.append(trait(dx, -150, dx + (6 if dx > 0 else -4), 0, rouge, 6))
        m.append(chemin(f"M {dx - 14} 0 L {dx} -4 L {dx + 16} 0", stroke=rouge, sw=5))
    m.append(chemin("M -40 -200 L -110 -170 L -40 -160 Z", "#343a40"))
    m.append(ellipse(0, -190, 62, 40, "#ffffff", stroke="#dee2e6", stroke_width=3))
    m.append(chemin("M -52 -200 Q -20 -150 40 -176 Q 10 -168 -10 -186 Z", "#343a40"))
    if cou == "table":
        # cou penché vers une table : le bout du bec arrive vers (138, -156)
        m.append(chemin("M 36 -210 Q 70 -250 100 -262", stroke="#ffffff", sw=24))
        hx, hy = 104, -268
        bec = f"M {hx + 14} {hy + 8} L {hx + 34} {hy + 112} L {hx + 2} {hy + 18} Z"
    elif cou == "baisse":
        m.append(chemin("M 40 -206 Q 80 -230 96 -170 Q 104 -130 110 -100", stroke="#ffffff", sw=24))
        hx, hy = 112, -92
        bec = f"M {hx + 14} {hy + 10} L {hx + 30} {hy + 110} L {hx + 4} {hy + 16} Z"
    else:
        m.append(chemin("M 36 -210 Q 60 -250 50 -300 Q 44 -330 60 -350", stroke="#ffffff", sw=24))
        hx, hy = 64, -356
        bec = f"M {hx + 18} {hy - 6} L {hx + 118} {hy + 8} L {hx + 18} {hy + 12} Z"
        if bec_ouvert:
            bec = (f"M {hx + 18} {hy - 6} L {hx + 110} {hy - 20} L {hx + 18} {hy + 4} Z "
                   f"M {hx + 18} {hy + 6} L {hx + 110} {hy + 28} L {hx + 18} {hy + 14} Z")
    m.append(cercle(hx, hy, 26, "#ffffff", stroke="#dee2e6", stroke_width=3))
    m.append(chemin(bec, rouge))
    m.append(oeil(hx + 4, hy - 6, ys, regard, taille=0.85))
    if ss:
        m.append(place(sourcils(0, 0, ss), hx + 4, hy - 4))
    m.append(ellipse(hx - 6, hy + 10, 6, 3.5, ROSE, opacity=0.8))
    return place(m, x, y, s, flip=flip)


def moucheron(x, y, s=1.0, expr="malin", flip=False, rot=0, regard=(1, 0), trompette=False):
    """Moucheron, vu de profil (tête à droite) ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [ellipse(-10, -26, 16, 28, "#e7f5ff", rot=-30, opacity=0.85, stroke="#91a7ff", stroke_width=2),
         ellipse(8, -28, 14, 26, "#e7f5ff", rot=20, opacity=0.85, stroke="#91a7ff", stroke_width=2),
         ellipse(-14, 4, 20, 12, "#495057"),
         trait(-18, 12, -24, 26, ENCRE, 2), trait(-6, 14, -6, 28, ENCRE, 2), trait(4, 12, 10, 26, ENCRE, 2),
         cercle(14, 0, 14, "#343a40"),
         trait(18, -12, 22, -26, ENCRE, 2), trait(24, -10, 32, -22, ENCRE, 2)]
    m.append(cercle(18, -4, 8.5, "#fff") + cercle(19 + regard[0] * 2.5, -4 + regard[1] * 2.5, 4.5, ENCRE))
    if ys in ("heureux", "fermes"):
        m[-1] = cercle(18, -4, 8.5, "#fff") + oeil(18, -4, ys, (0, 0), taille=0.6)
    if ss:
        m.append(place(sourcils(0, 0, ss).replace(ENCRE, "#f1f3f5"), 18, 8, 0.55))
    m.append(ellipse(22, 8, 4, 2.5, ROSE, opacity=0.9))
    if trompette:
        m.append(poly([(26, 6), (44, 0), (44, 14)], "#fab005"))
    else:
        m.append(trait(26, 6, 34, 10, ENCRE, 2))
    return place(m, x, y, s, flip=flip, rot=rot)


def araignee_perso(x, y, s=1.0, expr="sourire", fil=200, regard=(0, 0)):
    """Araignée qui parle, suspendue à son fil ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [trait(0, -30, 0, -30 - fil, "#adb5bd", 2)]
    for sgn in (-1, 1):
        for k in range(4):
            m.append(chemin(f"M 0 0 Q {sgn * 44} {-30 + k * 14} {sgn * 58} {14 + k * 12}", stroke=ENCRE, sw=5))
    m += [ellipse(0, 4, 34, 30, "#343a40"), cercle(0, -22, 22, "#495057")]
    m.append(oeil(-8, -26, ys, regard, taille=0.7) + oeil(8, -26, ys, regard, taille=0.7))
    m.append(place(bouche(0, 0, bs, 0.5), 0, -14))
    m.append(ellipse(-15, -16, 4, 2.5, ROSE, opacity=0.8) + ellipse(15, -16, 4, 2.5, ROSE, opacity=0.8))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Plantes qui parlent
# ---------------------------------------------------------------------------

def visage(x, y, s=1.0, expr="sourire", regard=(0, 0), joues=True):
    ys, bs, ss = EXPRESSIONS[expr]
    m = [oeil(-18, 0, ys, regard) + oeil(18, 0, ys, regard), sourcils(18, 0, ss)]
    if joues:
        m.append(ellipse(-32, 20, 9, 5.5, ROSE, opacity=0.7) + ellipse(32, 20, 9, 5.5, ROSE, opacity=0.7))
    m.append(bouche(0, 28, bs, 1.0))
    return place(m, x, y, s)


def chene(x, y, s=1.0, expr="fier", regard=(0, 0), penche=0, tombe=False, feuillage="#40c057", feuillage2="#2f9e44"):
    """Grand chêne avec un visage dans le tronc ; (x, y) = pied du tronc."""
    m = [chemin("M -70 0 Q -50 -30 -54 -200 L 54 -200 Q 50 -30 70 0 Z", "#8d5524"),
         chemin("M -60 0 Q -80 10 -100 4 M 60 0 Q 80 10 104 2", stroke="#8d5524", sw=16),
         chemin("M -30 -40 Q -26 -100 -32 -160 M 24 -30 Q 30 -90 22 -150", stroke="#6d4424", sw=4)]
    feuilles = [cercle(0, -300, 130, feuillage2), cercle(-120, -250, 90, feuillage), cercle(120, -250, 90, feuillage),
                cercle(-60, -360, 90, feuillage), cercle(70, -370, 85, feuillage), cercle(0, -260, 100, feuillage)]
    m += feuilles
    for gx, gy in [(-100, -230), (90, -300), (-20, -380), (40, -220), (-130, -300)]:
        m.append(g([ellipse(gx, gy, 9, 12, "#c68642"), chemin(f"M {gx - 10} {gy - 8} Q {gx} {gy - 18} {gx + 10} {gy - 8} Z", "#7c4a1e")]))
    m.append(visage(0, -120, 1.7, expr, regard, joues=False))
    t = []
    if tombe:
        return place(m, x, y, s, rot=-80)
    return place(m, x, y, s, rot=penche)


def roseau(x, y, s=1.0, expr="sourire", penche=0, regard=(0, 0), h=260, visage_=True):
    """Roseau souple avec une tête de massette ; (x, y) = au pied.

    penche : inclinaison en degrés (0 = tout droit, 90 = couché vers la droite,
    négatif = vers la gauche). La tête suit toujours le bout de la tige."""
    a = math.radians(penche)
    L = h * (1 - 0.25 * min(abs(penche), 120) / 90)
    ex, ey = L * math.sin(a), -L * math.cos(a)
    cx, cy = 0, -L * 0.55
    rot = math.degrees(math.atan2(ex - cx, -(ey - cy)))
    m = [chemin(f"M -6 0 Q -34 {-h * 0.3} -44 {-h * 0.55}", stroke="#74b816", sw=7),
         chemin(f"M 6 0 Q 34 {-h * 0.25} 46 {-h * 0.5}", stroke="#74b816", sw=7),
         chemin(f"M 0 0 Q {cx} {n(cy)} {n(ex)} {n(ey)}", stroke="#5c940d", sw=10)]
    tete = [rect(-30, -130, 60, 130, "#8d5524", rx=30), trait(0, -130, 0, -160, "#5c940d", 5)]
    if visage_:
        tete.append(visage(0, -74, 0.62, expr, regard, joues=True))
    m.append(place(tete, ex, ey, 1.0, rot=rot))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Accessoires
# ---------------------------------------------------------------------------

def raisins(x, y, s=1.0, couleur="#7048e8", feuille=True):
    """Grappe de raisins suspendue ; (x, y) = point d'attache."""
    m = [trait(0, 0, 0, 20, "#7c4a1e", 5)]
    if feuille:
        m.append(chemin("M 0 10 Q 40 -20 60 10 Q 40 30 0 10 Z", "#40c057"))
    fonce = _assombrir(couleur, 0.8)
    rangs = [(-24, 30, 3), (-18, 50, 3), (-12, 70, 2), (-6, 88, 1)]
    for x0, yy, nb in rangs:
        for k in range(nb):
            gx = x0 + k * 22 + (0 if nb == 3 else 10)
            m.append(cercle(gx, yy, 12, couleur))
            m.append(cercle(gx - 4, yy - 4, 3.5, "#fff", opacity=0.5))
    m.append(cercle(0, 100, 11, fonce))
    return place(m, x, y, s)


def treille(S, y=190, couleur="#8d5524"):
    """Treille en bois en haut de la scène, avec des feuilles de vigne."""
    S.add(rect(0, y - 14, 800, 20, couleur, rx=6))
    for x in (60, 740):
        S.add(rect(x - 12, y - 10, 24, 800, couleur))
    for k in range(9):
        fx = 40 + k * 92
        S.add(chemin(f"M {fx} {y} Q {fx + 30} {y - 40} {fx + 60} {y} Q {fx + 30} {y + 30} {fx} {y} Z", "#51cf66"))
    S.add(chemin(f"M 0 {y + 4} Q 200 {y + 30} 400 {y + 6} T 800 {y + 10}", stroke="#5c940d", sw=5))


def puits(x, y, s=1.0, profond=False, eau_=True):
    """Puits de pierre vu de face ; (x, y) = milieu au sol."""
    m = [rect(-130, -130, 260, 130, "#ced4da", rx=10)]
    for row in range(3):
        for k in range(5):
            bx = -130 + k * 56 + (row % 2) * 28
            m.append(rect(bx, -126 + row * 42, 50, 36, "#adb5bd", rx=8))
    m.append(ellipse(0, -130, 130, 26, "#868e96"))
    m.append(ellipse(0, -130, 110, 18, "#343a40"))
    m += [rect(-120, -330, 16, 200, "#8d5524", rx=4), rect(104, -330, 16, 200, "#8d5524", rx=4),
          poly([(-150, -320), (0, -400), (150, -320)], "#c92a2a"), rect(-110, -300, 220, 12, "#a0522d", rx=6),
          trait(0, -294, 0, -170, "#c68642", 3), rect(-16, -176, 32, 28, "#a0522d", rx=4)]
    return place(m, x, y, s)


def fond_puits(S, eau_y=680):
    """Intérieur d'un puits : murs de pierre, rond de ciel en haut, eau en bas."""
    fond(S, "#495057")
    for row in range(12):
        for k in range(9):
            bx = -40 + k * 100 + (row % 2) * 50
            S.add(rect(bx, row * 70, 92, 62, "#5c636a", rx=12))
    S.add(ellipse(400, 30, 220, 80, "#a5d8ff"))
    S.add(ellipse(400, 30, 220, 80, "none", stroke="#868e96", stroke_width=14))
    S.add(rect(0, eau_y, 800, 800 - eau_y, "#1c7ed6", opacity=0.9))
    S.add(chemin(f"M 0 {eau_y} " + " ".join(f"q 25 -10 50 0" for _ in range(16)), stroke="#74c0fc", sw=5))


def filet(x, y, w=360, h=260, couleur="#c68642", tendu=True):
    """Filet de corde en losanges ; (x, y) = coin haut gauche."""
    m = []
    pas = 40
    cid = uid("f")
    forme = chemin(f"M 0 0 Q {w / 2} {h * 0.25 if tendu else h * 0.5} {w} 0 L {w * 0.9} {h} Q {w / 2} {h * 1.1} {w * 0.1} {h} Z", "#000")
    m.append(el("clipPath", forme, id=cid))
    lignes = []
    for k in range(-12, 20):
        lignes.append(trait(k * pas, 0, k * pas + h, h, couleur, 4))
        lignes.append(trait(k * pas, 0, k * pas - h, h, couleur, 4))
    m.append(g(lignes, clip_path=f"url(#{cid})"))
    m.append(chemin(f"M 0 0 Q {w / 2} {h * 0.25 if tendu else h * 0.5} {w} 0", stroke=couleur, sw=7))
    return place(m, x, y)


def filet_perso(x, y, s=1.0, couleur="#c68642"):
    """Filet refermé sur quelqu'un, pendu à une corde ; (x, y) = nœud en haut."""
    m = [trait(0, 0, 0, -400, couleur, 6)]
    cid = uid("f")
    forme = chemin("M 0 0 Q 150 60 140 200 Q 100 300 0 300 Q -100 300 -140 200 Q -150 60 0 0 Z", "#000")
    lignes = []
    for k in range(-10, 12):
        lignes.append(trait(k * 34, 0, k * 34 + 320, 320, couleur, 4))
        lignes.append(trait(k * 34, 0, k * 34 - 320, 320, couleur, 4))
    m.append(el("clipPath", forme, id=cid))
    m.append(g(lignes, clip_path=f"url(#{cid})"))
    m.append(cercle(0, 0, 10, couleur))
    return place(m, x, y, s)


def grelot(x, y, s=1.0, ruban="#fa5252", ruban_long=0, brille=True):
    """Grelot doré avec son ruban ; (x, y) = centre du grelot."""
    m = []
    if ruban_long:
        m.append(chemin(f"M -10 -26 Q {-ruban_long / 2} -60 {-ruban_long} -30", stroke=ruban, sw=8))
        m.append(chemin(f"M 10 -26 Q {ruban_long / 2} -60 {ruban_long} -30", stroke=ruban, sw=8))
    m += [cercle(0, 0, 28, "#fcc419"), cercle(-8, -8, 8, "#fff", opacity=0.6),
          trait(-28, 0, 28, 0, "#f59f00", 4), rect(-4, 4, 8, 18, "#495057", rx=3),
          cercle(0, 6, 5, "#495057"), poly([(-12, -24), (12, -24), (0, -36)], ruban)]
    if brille:
        m.append(g([trait(-40, -30, -52, -42, "#fab005", 3), trait(40, -30, 52, -42, "#fab005", 3), trait(0, -44, 0, -58, "#fab005", 3)]))
    return place(m, x, y, s)


def pot_lait(x, y, s=1.0, rot=0, casse=False, lait=True):
    """Pot au lait en terre ; (x, y) = milieu du fond."""
    if casse:
        m = [chemin("M -70 0 Q -40 -30 0 -10 Q 50 -30 90 0 Q 60 20 0 16 Q -50 20 -70 0 Z", "#f8f9fa"),
             place(chemin("M -30 0 L -26 -40 L 0 -52 L 10 -20 Z", "#c2703d"), -60, -4, rot=-20),
             place(chemin("M 0 0 L 6 -44 L 30 -40 L 26 0 Z", "#c2703d"), 40, 0, rot=30),
             place(chemin("M -10 0 L 0 -30 L 20 -24 L 16 0 Z", "#a85a2c"), -10, -6, rot=10),
             chemin("M -40 -60 q 4 -20 8 0 M 30 -70 q 4 -20 8 0 M 60 -44 q 4 -16 8 0", stroke="#f8f9fa", sw=6)]
        return place(m, x, y, s, rot=rot)
    m = [chemin("M -34 0 Q -48 -40 -36 -70 Q -30 -86 -22 -92 L 22 -92 Q 30 -86 36 -70 Q 48 -40 34 0 Z", "#c2703d"),
         ellipse(0, -92, 24, 7, "#a85a2c")]
    if lait:
        m.append(ellipse(0, -92, 20, 5, "#f8f9fa"))
    m += [chemin("M -40 -50 Q 0 -40 40 -50", stroke="#e8a15c", sw=5), chemin("M -26 -70 Q -30 -40 -26 -14", stroke="#fff", sw=5, opacity=0.35)]
    return place(m, x, y, s, rot=rot)


def baton(x1, y1, x2, y2, couleur="#a0522d", ep=12):
    return trait(x1, y1, x2, y2, couleur, ep) + trait(x1, y1 - 3, x2, y2 - 3, _assombrir(couleur, 0.8), 3, opacity=0.5)


def assiette_plate(x, y, s=1.0, soupe="#f59f00", vide=False):
    """Assiette très plate vue de côté, avec de la soupe ; (x, y) = milieu du fond."""
    m = [ellipse(0, -6, 110, 20, "#fff", stroke="#ced4da", stroke_width=3)]
    if not vide:
        m.append(ellipse(0, -8, 84, 12, soupe))
        m.append(chemin("M -30 -28 q 6 -12 0 -24 M 10 -30 q 6 -12 0 -24", stroke="#dee2e6", sw=4, opacity=0.8))
    return place(m, x, y, s)


def vase_long(x, y, s=1.0, couleur="#1c7ed6", contenu=True):
    """Vase au long cou étroit ; (x, y) = milieu du fond."""
    m = [chemin("M -60 0 Q -80 -70 -40 -110 Q -18 -130 -16 -160 L -14 -300 L 14 -300 L 16 -160 Q 18 -130 40 -110 Q 80 -70 60 0 Z", couleur),
         ellipse(0, -300, 22, 8, _assombrir(couleur, 0.7)),
         chemin("M -50 -40 Q 0 -30 50 -40", stroke="#fff", sw=6, opacity=0.4),
         chemin("M -40 -80 Q -46 -50 -40 -20", stroke="#fff", sw=6, opacity=0.35)]
    if contenu:
        m.append(chemin("M -8 -330 q 4 -16 0 -30 M 8 -326 q 4 -16 0 -30", stroke="#dee2e6", sw=4, opacity=0.8))
    return place(m, x, y, s)


def collier(x, y, s=1.0, couleur="#c92a2a"):
    m = [ellipse(0, 0, 44, 14, "none", stroke=couleur, stroke_width=10), cercle(0, 14, 9, "#fcc419")]
    return place(m, x, y, s)


def beche(x, y, s=1.0, rot=0):
    """Bêche ; (x, y) = bas de la lame."""
    m = [rect(-4, -190, 8, 150, "#a0522d", rx=3), rect(-18, -206, 36, 14, "#a0522d", rx=6),
         chemin("M -24 -44 L 24 -44 L 20 0 Q 0 8 -20 0 Z", "#adb5bd")]
    return place(m, x, y, s, rot=rot)


def sac(x, y, s=1.0, couleur="#e9d8c4", ecrit="", plein=True):
    """Sac de toile noué ; (x, y) = milieu du fond."""
    m = [chemin("M -50 0 Q -64 -60 -30 -96 L 30 -96 Q 64 -60 50 0 Z", couleur, stroke=_assombrir(couleur, 0.85), sw=3),
         chemin("M -24 -96 L -30 -118 M 24 -96 L 30 -118 M 0 -96 L 0 -120", stroke=_assombrir(couleur, 0.8), sw=6),
         trait(-30, -96, 30, -96, "#a0522d", 6)]
    if ecrit:
        m.append(texte(0, -38, ecrit, 26, "#a0522d"))
    return place(m, x, y, s)


def moulin(x, y, s=1.0, rot=12):
    """Moulin à vent ; (x, y) = milieu de la base."""
    m = [poly([(-80, 0), (-56, -260), (56, -260), (80, 0)], "#fff4e6"),
         poly([(-72, -250), (0, -330), (72, -250)], "#c92a2a"),
         rect(-22, -70, 44, 70, "#a0522d", rx=18), cercle(0, -180, 18, "#a5d8ff", stroke="#fff", stroke_width=4)]
    ailes = []
    for k in range(4):
        ailes.append(place([rect(-6, -190, 12, 190, "#8d5524"), rect(6, -180, 40, 150, "#f8f9fa", stroke="#adb5bd", stroke_width=3)], 0, 0, rot=k * 90))
    m.append(place(ailes, 0, -260, 1.0, rot=rot))
    m.append(cercle(0, -260, 14, "#495057"))
    return place(m, x, y, s)


def violon(x, y, s=1.0, rot=-30):
    """Petit violon ; (x, y) = centre de la caisse."""
    m = [chemin("M 0 -40 Q 22 -40 20 -22 Q 16 -10 22 0 Q 30 16 18 34 Q 0 44 -18 34 Q -30 16 -22 0 Q -16 -10 -20 -22 Q -22 -40 0 -40 Z", "#d9480f"),
         rect(-4, -90, 8, 56, "#343a40", rx=3), ellipse(0, -94, 6, 9, "#343a40"),
         trait(-2, -84, -2, 30, "#f1f3f5", 1.2), trait(2, -84, 2, 30, "#f1f3f5", 1.2),
         rect(-10, 18, 20, 5, "#343a40", rx=2)]
    return place(m, x, y, s, rot=rot)


def archet(x, y, s=1.0, rot=40):
    return place([trait(0, -60, 0, 60, "#8d5524", 4), trait(4, -56, 4, 56, "#f1f3f5", 2)], x, y, s, rot=rot)


def fourmiliere(x, y, s=1.0):
    """Petite colline de terre avec une porte ronde ; (x, y) = milieu au sol."""
    m = [chemin("M -170 0 Q -120 -150 0 -160 Q 120 -150 170 0 Z", "#c49a6c"),
         chemin("M -130 -40 q 10 -6 20 0 M 60 -100 q 10 -6 20 0 M 90 -30 q 10 -6 20 0 M -60 -120 q 10 -6 20 0", stroke="#9c7650", sw=4),
         chemin("M -34 0 Q -34 -60 0 -60 Q 34 -60 34 0 Z", "#5c3a1e"),
         chemin("M -24 0 Q -24 -46 0 -46 Q 24 -46 24 0 Z", "#3b2412")]
    return place(m, x, y, s)


def grain(x, y, s=1.0, couleur="#f6c453"):
    return place([ellipse(0, 0, 10, 14, couleur), chemin("M 0 -10 L 0 10", stroke=_assombrir(couleur, 0.8), sw=2)], x, y, s)


def tas_grains(x, y, s=1.0):
    m = [chemin("M -80 0 Q -40 -60 0 -64 Q 40 -60 80 0 Z", "#f6c453")]
    rr = random.Random(7)
    for _ in range(18):
        m.append(ellipse(rr.uniform(-60, 60), rr.uniform(-46, -6), 6, 8, "#e0a93a", rot=rr.uniform(-40, 40)))
    return place(m, x, y, s)


def meule_foin(x, y, s=1.0):
    m = [chemin("M -150 0 Q -150 -200 0 -210 Q 150 -200 150 0 Z", "#fcc419")]
    for k in range(9):
        xx = -120 + k * 30
        m.append(chemin(f"M {xx} -10 Q {xx + 6} -100 {xx - 4} -170", stroke="#f59f00", sw=4))
    return place(m, x, y, s)


def brin_herbe(x, y, s=1.0, rot=0):
    """Long brin d'herbe (ou brindille) qui flotte ; (x, y) = milieu."""
    m = [chemin("M -110 0 Q 0 -14 110 0 Q 0 10 -110 0 Z", "#51cf66"), trait(-100, 0, 100, -2, "#2f9e44", 2)]
    return place(m, x, y, s, rot=rot)


def riviere(S, y=560, couleur="#4dabf7", couleur2="#a5d8ff"):
    S.add(chemin(f"M 0 {y} Q 200 {y - 20} 400 {y} T 800 {y} L 800 800 L 0 800 Z", couleur))
    for k in range(5):
        yy = y + 50 + k * 50
        x0 = (k % 2) * 80 + 40
        S.add(chemin(" ".join(f"M {x0 + i * 180} {yy} q 25 -12 50 0" for i in range(5)), stroke=couleur2, sw=5))


def champ_laboure(S, y=520, couleur="#a0693a", sillon="#7c4a1e"):
    S.add(rect(0, y, 800, 800 - y, couleur))
    for k in range(9):
        yy = y + 20 + k * k * 4 + k * 10
        S.add(chemin(f"M 0 {yy} Q 400 {yy - 14} 800 {yy}", stroke=sillon, sw=4 + k * 0.6))


def ble(x, y, s=1.0, h=180):
    m = [trait(0, 0, 0, -h, "#e0a93a", 4)]
    for k in range(6):
        yy = -h + 10 + k * 13
        m.append(ellipse(-7, yy, 5, 9, "#f6c453", rot=-30) + ellipse(7, yy, 5, 9, "#f6c453", rot=30))
    m.append(ellipse(0, -h - 4, 5, 10, "#f6c453"))
    return place(m, x, y, s)


def champ_ble(S, y=560, graine=3, n_=40):
    rr = random.Random(graine)
    S.add(rect(0, y, 800, 800 - y, "#f6c453"))
    for _ in range(n_):
        S.add(ble(rr.uniform(0, 800), y + rr.uniform(10, 240), rr.uniform(0.6, 1.1)))


def ville(S, y=560):
    """Rangée d'immeubles et de maisons de ville en fond."""
    couleurs = ["#ffc9c9", "#d0bfff", "#a5d8ff", "#ffec99", "#b2f2bb", "#ffd8a8"]
    x = -20
    k = 0
    while x < 820:
        w = 110 + (k * 37) % 50
        h = 220 + (k * 83) % 180
        c = couleurs[k % len(couleurs)]
        S.add(rect(x, y - h, w, h, c))
        S.add(poly([(x - 6, y - h), (x + w / 2, y - h - 50), (x + w + 6, y - h)], _assombrir(c, 0.75)))
        for row in range(int(h // 70)):
            for col in range(2):
                S.add(rect(x + 18 + col * (w / 2), y - h + 24 + row * 70, w / 2 - 36, 40, "#fff9db", rx=4))
        x += w + 6
        k += 1


def salle_manger(S, mur="#fff0f6", papier="#fcc2d7"):
    interieur(S, mur, "#c9a27e", 580, papier=papier)
    S.add(rect(290, 60, 220, 200, "#fab005", rx=10), rect(305, 75, 190, 170, "#ffe066"))
    S.add(g([cercle(400, 160, 50, "#fff3bf"), cercle(400, 160, 30, "#ffd43b")]))


def festin(x, y, s=1.0):
    """Table garnie : poulet, gâteau, fromage, raisins, fruits ; (x, y) = milieu du pied."""
    m = [table(0, 0, 420, 150, nappe="#fff")]
    m.append(place([ellipse(0, -8, 60, 14, "#fff", stroke="#ced4da", stroke_width=3), ellipse(0, -30, 42, 26, "#e8590c"),
                    ellipse(-38, -34, 10, 16, "#e8590c", rot=-30), cercle(-48, -48, 8, "#fff"), cercle(-4, -40, 6, "#fff", opacity=0.3)], -120, -150))
    m.append(gateau(40, -150, 0.6, couleur="#f8c291", glacage="#ffc9d6", fruits="#fa5252"))
    m.append(fromage(150, -168, 1.0))
    m.append(raisins(110, -214, 0.6, feuille=False))
    m.append(g([pomme(-190, -164, 0.8), pomme(-170, -164, 0.8, "#fcc419")]))
    return place(m, x, y, s)
