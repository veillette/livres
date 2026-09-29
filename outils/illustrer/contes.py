"""
Personnages, accessoires et décors des contes traditionnels : les trois
petits cochons, Boucle d'or, Jack et le haricot magique, Hansel et Gretel,
le Petit Chaperon rouge, les trois boucs, Cendrillon, le Chat botté,
Raiponce, le Petit Poucet, l'énorme navet, la soupe au caillou…

Mêmes conventions que `base.py` : page de 800 × 800, personnages dessinés de
face, les pieds en (0, 0) et la tête vers y = -150.
"""
from base import *
from base import EXPRESSIONS, _assombrir
from objets import *
from fantastique import *
from fables import *
from sciences import canard, enfant, fleche, cheval, rafales, vent


def _habille(dessin, extras, x, y, s, flip=False, rot=0):
    """Ajoute des `extras` (coordonnées locales) par-dessus un personnage dessiné en (0, 0)."""
    return place([dessin] + list(extras), x, y, s, flip=flip, rot=rot)


# ---------------------------------------------------------------------------
# Personnages
# ---------------------------------------------------------------------------

def chaperon(x, y, s=1.0, cape="#e03131", flip=False, **k):
    """Le Petit Chaperon rouge : une cape rouge et un capuchon."""
    k.setdefault("coiffure", "tresses")
    k.setdefault("cheveux", "chatain")
    k.setdefault("habit", "#fff4e6")
    k.setdefault("peau", "claire")
    capuche_dos = cercle(0, -156, 66, cape)
    corps = personne(0, 0, 1.0, cape=cape, derriere=capuche_dos, **k)
    capuche = chemin("M -64 -150 Q -66 -222 0 -224 Q 66 -222 64 -150 Q 56 -200 0 -204 Q -56 -200 -64 -150 Z", cape)
    noeud = g([poly([(0, -104), (-16, -114), (-16, -94)], cape), poly([(0, -104), (16, -114), (16, -94)], cape)])
    return _habille(corps, [capuche, noeud], x, y, s, flip)


def mere_grand(x, y, s=1.0, flip=False, **k):
    k.setdefault("coiffure", "chignon")
    k.setdefault("cheveux", "blanc")
    k.setdefault("habit", "#b197fc")
    k.setdefault("acc", ("lunettes",))
    k.setdefault("peau", "rosee")
    return personne(x, y, s, flip=flip, **k)


def geant(x, y, s=3.0, flip=False, **k):
    """Un géant (ou un ogre) : gros nez, barbe hirsute, ceinture de cuir."""
    k.setdefault("coiffure", "herisses")
    k.setdefault("cheveux", "#5c3a1e")
    k.setdefault("barbe", "#5c3a1e")
    k.setdefault("peau", "#e8a882")
    k.setdefault("habit", "#5f3dc4")
    k.setdefault("robe", False)
    k.setdefault("jambes", "#5c3a1e")
    k.setdefault("ceinture", "#8d5524")
    p = PEAUX.get(k["peau"], k["peau"])
    corps = personne(0, 0, 1.0, **k)
    nez = ellipse(0, -134, 13, 11, _assombrir(p, 0.88))
    return _habille(corps, [nez], x, y, s, flip)


def troll(x, y, s=1.0, flip=False, expr="furieux", **k):
    """Troll vert, gros nez et petites cornes."""
    k.setdefault("peau", "#8ce99a")
    k.setdefault("coiffure", "herisses")
    k.setdefault("cheveux", "#5c940d")
    k.setdefault("habit", "#8d5524")
    k.setdefault("robe", False)
    k.setdefault("jambes", "#5c3a1e")
    k.setdefault("ceinture", "#5c3a1e")
    corps = personne(0, 0, 1.0, expr=expr, **k)
    extras = [poly([(-40, -188), (-54, -228), (-24, -196)], "#fff4e6", stroke="#dee2e6", stroke_width=2),
              poly([(40, -188), (54, -228), (24, -196)], "#fff4e6", stroke="#dee2e6", stroke_width=2),
              ellipse(0, -132, 16, 14, "#51cf66"), ellipse(-5, -128, 3, 4, "#2b8a3e"), ellipse(5, -128, 3, 4, "#2b8a3e")]
    for sgn in (-1, 1):
        extras.append(poly([(sgn * 48, -150), (sgn * 74, -164), (sgn * 52, -136)], PEAUX.get(k["peau"], k["peau"])))
    return _habille(corps, extras, x, y, s, flip)


def voleur(x, y, s=1.0, flip=False, **k):
    """Un brigand avec un masque noir sur les yeux."""
    k.setdefault("coiffure", "courts")
    k.setdefault("cheveux", "noir")
    k.setdefault("habit", "#495057")
    k.setdefault("robe", False)
    k.setdefault("jambes", "#212529")
    corps = personne(0, 0, 1.0, **k)
    ys = EXPRESSIONS[k.get("expr", "sourire")][0]
    masque = [rect(-52, -166, 104, 30, "#212529", rx=14),
              ellipse(-18, -151, 11, 9, "#fff"), ellipse(18, -151, 11, 9, "#fff"),
              oeil(-18, -151, ys, k.get("regard", (0, 0)), taille=0.7), oeil(18, -151, ys, k.get("regard", (0, 0)), taille=0.7)]
    return _habille(corps, masque, x, y, s, flip)


def lutin(x, y, s=0.5, bonnet="#e03131", flip=False, **k):
    """Petit lutin avec un bonnet pointu qui retombe."""
    k.setdefault("coiffure", "courts")
    k.setdefault("habit", "#2f9e44")
    k.setdefault("robe", False)
    k.setdefault("jambes", "#8d5524")
    return personne(x, y, s, acc=("bonnet_nuit",) + tuple(k.pop("acc", ())), couleur_acc=bonnet, flip=flip, **k)


def chat_botte(x, y, s=1.0, flip=False, bottes=True, chapeau_=True, plume="#fa5252", **k):
    """Le chat botté : bottes de cuir et chapeau à plume."""
    k.setdefault("couleur", "#fd7e14")
    extras = []
    if bottes:
        for sgn in (-1, 1):
            extras += [rect(sgn * 21 - 17, -40, 34, 34, "#5c3a1e", rx=6),
                       ellipse(sgn * 21 + sgn * 4, -8, 22, 11, "#5c3a1e"),
                       rect(sgn * 21 - 20, -44, 40, 12, "#8d5524", rx=5)]
    if chapeau_:
        extras += [chemin("M 30 -214 Q 90 -250 110 -210 Q 80 -230 40 -206 Z", plume),
                   chapeau(0, -196, 1.0, "#343a40", ruban="#f59f00", fleur_=False)]
    corps = perso("chat", 0, 0, 1.0, **k)
    return _habille(corps, extras, x, y, s, flip)


def bonhomme_pain_epice(x, y, s=1.0, expr="rire", bras="haut", flip=False, rot=0, regard=(0, 0), course=False):
    """Bonhomme de pain d'épice, glaçage blanc et boutons en bonbon ; pieds en (0, 0)."""
    c = "#c9772b"
    bord = "#9c5a1c"
    ys, bs, ss = EXPRESSIONS[expr]
    mg, md = POSES[bras]
    if course:
        jambes = [((-18, -70), (-58, -16)), ((18, -70), (34, -4))]
    else:
        jambes = [((-18, -70), (-32, -6)), ((18, -70), (32, -6))]
    m = []
    for (x0, y0), (x1, y1) in jambes:
        m.append(trait(x0, y0, x1, y1, bord, 42))
        m.append(trait(x0, y0, x1, y1, c, 36))
    for hx, hy in (mg, md):
        m.append(trait(0, -104, hx, hy, bord, 36))
        m.append(trait(0, -104, hx, hy, c, 30))
    m.append(ellipse(0, -84, 44, 52, bord))
    m.append(ellipse(0, -84, 40, 48, c))
    for (x0, y0), (x1, y1) in jambes:
        m.append(chemin(f"M {x1 - 12} {y1 - 10} q 6 -8 12 0 q 6 8 12 0", stroke="#fff", sw=4))
    for hx, hy in (mg, md):
        m.append(chemin(f"M {hx - 10} {hy + (6 if hy > -104 else -6)} q 5 -8 10 0 q 5 8 10 0", stroke="#fff", sw=4))
    m += [cercle(0, -104, 8, "#fa5252"), cercle(0, -80, 8, "#51cf66"), cercle(0, -56, 8, "#4dabf7")]
    m.append(cercle(0, -156, 46, bord))
    m.append(cercle(0, -156, 42, c))
    m.append(chemin("M -30 -186 q 30 -18 60 0", stroke="#fff", sw=4))
    m.append(ellipse(-26, -136, 8, 5, "#ff8787", opacity=0.7) + ellipse(26, -136, 8, 5, "#ff8787", opacity=0.7))
    m.append(place(oeil(-16, 0, ys, regard) + oeil(16, 0, ys, regard) + sourcils(16, 0, ss), 0, -158))
    m.append(bouche(0, -132, bs, 0.9))
    return place(m, x, y, s, flip=flip, rot=rot)


def cygne(x, y, s=1.0, expr="sourire", flip=False, nage=True, couleur="#ffffff", ailes="bas", regard=(1, 0)):
    """Cygne de profil, la tête à droite ; (x, y) = sur la ligne d'eau."""
    ys, bs, ss = EXPRESSIONS[expr]
    ombre_c = "#dee2e6" if couleur == "#ffffff" else _assombrir(couleur, 0.85)
    m = [chemin("M -120 -30 Q -140 -80 -100 -70 Q -40 -60 60 -40 Q 70 0 30 10 L -90 10 Q -130 0 -120 -30 Z", couleur, stroke=ombre_c, sw=3),
         chemin("M 40 -40 Q 70 -60 60 -120 Q 50 -170 80 -190 Q 110 -206 124 -180", stroke=ombre_c, sw=30),
         chemin("M 40 -40 Q 70 -60 60 -120 Q 50 -170 80 -190 Q 110 -206 124 -180", stroke=couleur, sw=24),
         cercle(110, -186, 22, couleur),
         poly([(124, -194), (164, -178), (124, -172)], "#ff922b"),
         chemin("M 124 -194 L 116 -186 L 124 -176 Z", ENCRE),
         ellipse(114, -174, 6, 4, ROSE, opacity=0.8),
         oeil(108, -192, ys, regard, taille=0.7)]
    if ailes == "haut":
        m.insert(0, chemin("M -60 -50 Q -110 -170 -30 -200 Q -40 -120 20 -60 Z", couleur, stroke=ombre_c, sw=3))
    else:
        m.append(chemin("M -90 -50 Q -40 -90 30 -40 Q -20 -10 -90 -20 Z", ombre_c))
    if nage:
        m.append(ellipse(-30, 8, 130, 10, "#fff", opacity=0.5))
    return place(m, x, y, s, flip=flip)


def poule_rousse(x, y, s=1.0, **k):
    k.setdefault("couleur", "#e8590c")
    k.setdefault("ventre", "#ffd8a8")
    return coq(x, y, s, poule=True, **k)


def poussin(x, y, s=1.0, **k):
    k.setdefault("couleur", "#ffe066")
    k.setdefault("ventre", "#fff9db")
    return oiseau(x, y, s, **k)


# ---------------------------------------------------------------------------
# Maisons des trois petits cochons
# ---------------------------------------------------------------------------

def maison_paille(x, y, s=1.0, souffle=0.0):
    """Hutte de paille ; `souffle` (0 à 1) fait s'envoler les brins."""
    m = []
    if souffle < 1:
        m.append(chemin("M -110 0 L -110 -110 L 110 -110 L 110 0 Z", "#ffe066"))
        m.append(chemin("M -140 -100 Q 0 -280 140 -100 Z", "#fcc419"))
        for k in range(-5, 6):
            m.append(trait(k * 20, -8, k * 20 + 4, -104, "#f59f00", 3, opacity=0.6))
        for k in range(-6, 7):
            m.append(trait(k * 20, -104, k * 10, -200 + abs(k) * 12, "#e67700", 3, opacity=0.5))
        m.append(chemin("M -30 0 L -30 -70 Q 0 -96 30 -70 L 30 0 Z", "#a0522d"))
    if souffle > 0:
        r = random.Random(3)
        for _ in range(int(40 * souffle)):
            bx, by = r.uniform(-150, 250), r.uniform(-300, -10)
            a = r.uniform(-40, 40)
            m.append(place(trait(-18, 0, 18, 0, "#fcc419", 5), bx, by, rot=a))
    return place(m, x, y, s)


def maison_bois(x, y, s=1.0, tombe=0.0):
    """Cabane en planches ; `tombe` (0 à 1) : planches qui s'écroulent."""
    m = []
    if tombe < 1:
        for k in range(-5, 5):
            m.append(rect(k * 22, -130, 20, 130, "#c68642" if k % 2 else "#b5835a"))
        m.append(poly([(-130, -126), (0, -236), (130, -126)], "#8d5524"))
        for k in range(4):
            m.append(trait(-100 + k * 20, -140 - k * 18, 100 - k * 20, -140 - k * 18, "#6d4424", 4))
        m.append(rect(-26, -80, 52, 80, "#6d4424", rx=4))
        m.append(rect(52, -110, 40, 36, "#a5d8ff", stroke="#6d4424", stroke_width=5))
    if tombe > 0:
        r = random.Random(5)
        for k in range(12):
            bx, by = r.uniform(-160, 200), r.uniform(-60, 0)
            m.append(place(rect(-60, -10, 120, 20, "#c68642" if k % 2 else "#b5835a", rx=4), bx, by, rot=r.uniform(-30, 30)))
    return place(m, x, y, s)


def maison_briques(x, y, s=1.0, fumee=False, feu=False):
    """Maison de briques solide avec une cheminée."""
    m = [rect(-130, -170, 260, 170, "#e8590c")]
    for row in range(8):
        yy = -170 + row * 21
        m.append(trait(-130, yy, 130, yy, "#ffd8a8", 3))
        off = 0 if row % 2 else 20
        for k in range(-3, 4):
            xx = k * 40 + off
            if -130 < xx < 130:
                m.append(trait(xx, yy, xx, yy + 21, "#ffd8a8", 3))
    m.append(rect(60, -290, 44, 120, "#c92a2a"))
    m.append(rect(52, -300, 60, 16, "#a61e4d"))
    if fumee:
        m.append(chemin("M 82 -306 Q 60 -340 90 -370 Q 120 -400 96 -440", stroke="#dee2e6", sw=16, opacity=0.8))
    if feu:
        m.append(g([chemin("M 64 -300 Q 70 -340 82 -320 Q 86 -360 100 -318 Q 106 -332 104 -300 Z", "#ff922b")]))
    m.append(poly([(-156, -166), (0, -276), (156, -166)], "#862e9c"))
    m.append(rect(-32, -100, 64, 100, "#5c3a1e", rx=6))
    m.append(cercle(20, -50, 5, "#ffd43b"))
    m.append(rect(-104, -136, 48, 44, "#ffe066", stroke="#fff", stroke_width=5))
    m.append(rect(56, -136, 48, 44, "#ffe066", stroke="#fff", stroke_width=5))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Boucle d'or
# ---------------------------------------------------------------------------

def bol_porridge(x, y, s=1.0, couleur="#74c0fc", vide=False, fumee=False):
    m = []
    if fumee:
        m.append(chemin("M -14 -44 q -12 -20 0 -36 q 12 -16 0 -34", stroke="#dee2e6", sw=6, opacity=0.8))
        m.append(chemin("M 14 -44 q -12 -20 0 -36 q 12 -16 0 -34", stroke="#dee2e6", sw=6, opacity=0.8))
    m += [ellipse(0, -36, 56, 14, _assombrir(couleur, 0.8)),
          ellipse(0, -36, 48, 10, "#e9ecef" if vide else "#fff3bf"),
          chemin("M -56 -36 Q -50 0 0 0 Q 50 0 56 -36 Z", couleur),
          trait(20, -44, 64, -74, "#adb5bd", 6), ellipse(22, -42, 10, 6, "#adb5bd")]
    return place(m, x, y, s)


def chaise(x, y, s=1.0, couleur="#c68642", cassee=False):
    """Chaise vue de face ; (x, y) = entre les pieds au sol."""
    fonce = _assombrir(couleur, 0.8)
    if cassee:
        m = [place(rect(-60, -14, 120, 18, couleur, rx=5), -20, -10, rot=-12),
             place(rect(-6, -60, 12, 60, fonce), -70, 0, rot=-60),
             place(rect(-6, -60, 12, 60, fonce), 60, 0, rot=70),
             place(g([rect(-50, -120, 12, 120, fonce), rect(38, -120, 12, 120, fonce), rect(-50, -120, 100, 24, couleur, rx=6), rect(-50, -76, 100, 14, couleur, rx=4)]), 30, -4, rot=80)]
        return place(m, x, y, s)
    m = [rect(-50, -200, 12, 200, fonce), rect(38, -200, 12, 200, fonce),
         rect(-50, -200, 100, 26, couleur, rx=8), rect(-50, -156, 100, 14, couleur, rx=5),
         rect(-58, -100, 116, 18, couleur, rx=6)]
    return place(m, x, y, s)


def ours_famille(nom):
    """Couleurs et tailles de Papa ours, Maman ourse et Bébé ours."""
    return {
        "papa": dict(s=1.5, habit="#1c7ed6", couleur="#9c6b43"),
        "maman": dict(s=1.25, habit="#e64980", couleur="#b07a4f", acc=("noeud",), couleur_acc="#fcc2d7"),
        "bebe": dict(s=0.85, habit="#fcc419", couleur="#c49060"),
    }[nom]


def ours_(nom, x, y, s=None, **k):
    d = dict(ours_famille(nom))
    sc = d.pop("s")
    d.update(k)
    return perso("ours", x, y, s or sc, **d)


def foret(S, ciel_haut="#a5d8ff", ciel_bas="#ebfbee", y=600, graine=2, sombre=False):
    """Clairière entourée de grands arbres."""
    if sombre:
        ciel(S, "#364fc7", "#748ffc")
    else:
        ciel(S, ciel_haut, ciel_bas)
    r = random.Random(graine)
    f1, f2 = ("#2b8a3e", "#237032") if sombre else ("#51cf66", "#40c057")
    for k in range(7):
        xx = -40 + k * 140 + r.uniform(-30, 30)
        S.add(arbre(xx, y - 20 + r.uniform(-20, 20), r.uniform(0.9, 1.25), f1, f2, "#7c4a1e"))
    sol(S, y, "#69db7c" if not sombre else "#2f9e44")


# ---------------------------------------------------------------------------
# Jack et le haricot magique
# ---------------------------------------------------------------------------

def haricots(x, y, s=1.0, brille=True):
    """Cinq haricots magiques dans une main ouverte ; (x, y) = centre."""
    m = []
    if brille:
        m.append(cercle(0, 0, 60, "#fff3bf", opacity=0.6))
    for k, (hx, hy, a) in enumerate([(-26, 6, -20), (0, -6, 10), (24, 4, 40), (-12, 20, 70), (14, 22, -30)]):
        c = ["#9775fa", "#51cf66", "#fa5252", "#fcc419", "#4dabf7"][k]
        m.append(ellipse(hx, hy, 14, 9, c, rot=a))
        m.append(ellipse(hx - 3, hy - 3, 4, 2.5, "#fff", opacity=0.6, rot=a))
    return place(m, x, y, s)


def tige_haricot(x, y_bas, y_haut, s=1.0, feuilles=True, ep=34):
    """Énorme tige de haricot qui serpente de y_bas jusqu'à y_haut autour de x."""
    pts = []
    h = y_bas - y_haut
    nb = max(2, int(h / 110))
    d = f"M {x} {y_bas}"
    for k in range(nb):
        y0 = y_bas - (k + 0.5) * h / nb
        y1 = y_bas - (k + 1) * h / nb
        dx = 60 * s * (1 if k % 2 else -1)
        d += f" Q {n(x + dx)} {n(y0)} {x} {n(y1)}"
        pts.append((x + dx * 0.55, y0))
    m = [chemin(d, stroke="#2b8a3e", sw=ep * s), chemin(d, stroke="#51cf66", sw=ep * s * 0.6),
         chemin(d, stroke="#8ce99a", sw=ep * s * 0.15, opacity=0.7)]
    if feuilles:
        for k, (px, py) in enumerate(pts):
            sgn = 1 if k % 2 else -1
            m.append(place(chemin("M 0 0 Q 30 -40 80 -20 Q 50 10 0 0 Z", "#40c057"), px, py, s, flip=sgn < 0))
            m.append(place(chemin("M 0 0 Q 40 -20 70 -18", stroke="#2b8a3e", sw=3), px, py, s, flip=sgn < 0))
            m.append(place(chemin("M 0 0 q 20 -10 16 -30 q -4 -14 -16 -6", stroke="#69db7c", sw=4), px, py + 30 * s, s, flip=sgn > 0))
    return g(m)


def sol_nuages(S, y=560, couleur="#ffffff", ombre="#dbe4ff"):
    """Pays au-dessus des nuages."""
    ciel(S, "#74c0fc", "#d0ebff")
    for k in range(9):
        S.add(cercle(-20 + k * 105, y + 10 + (k % 2) * 20, 80, ombre))
    for k in range(9):
        S.add(cercle(-20 + k * 105, y + (k % 2) * 20, 76, couleur))
    S.add(rect(0, y + 40, S.w, S.h - y - 40, couleur))
    for k in range(6):
        S.add(ellipse(60 + k * 140, y + 150 + (k % 2) * 60, 60, 14, ombre, opacity=0.7))


def chateau_geant(x, y, s=1.0):
    return chateau(x, y, s, mur="#dee2e6", mur2="#ced4da", toit="#5f3dc4", drapeau="#fa5252", fenetres="#ffe066")


def harpe(x, y, s=1.0, visage_=True, expr="sourire", notes_=False):
    """Harpe d'or qui chante ; (x, y) = pied."""
    m = [chemin("M -40 0 L -40 -220 Q -30 -250 10 -236 Q 70 -210 70 -120 Q 70 -60 40 -20 L -40 0 Z", "none", stroke=OR_FONCE, sw=16),
         chemin("M -40 0 L -40 -220 Q -30 -250 10 -236 Q 70 -210 70 -120 Q 70 -60 40 -20 L -40 0 Z", "none", stroke=OR, sw=10)]
    for k in range(6):
        xx = -30 + k * 14
        ytop = -226 + k * 6 if k < 3 else -226 + k * 10
        m.append(trait(xx, ytop, xx, -8 - k * 2, "#fff3bf", 2))
    m.append(rect(-56, -8, 112, 14, OR_FONCE, rx=6))
    if visage_:
        m.append(cercle(-40, -236, 28, OR))
        m.append(place(oeil(-10, 0, EXPRESSIONS[expr][0], (0, 0), taille=0.7) + oeil(10, 0, EXPRESSIONS[expr][0], (0, 0), taille=0.7)
                       + bouche(0, 16, EXPRESSIONS[expr][1], 0.6), -40, -242))
    if notes_:
        m.append(notes(60, -250, 0.8, OR_FONCE))
    return place(m, x, y, s)


def hache(x, y, s=1.0, rot=0):
    m = [rect(-6, -140, 12, 140, "#a0522d", rx=5), chemin("M 6 -140 Q 50 -150 56 -110 Q 50 -96 6 -100 Z", "#adb5bd")]
    return place(m, x, y, s, rot=rot)


# ---------------------------------------------------------------------------
# Hansel et Gretel, le Petit Poucet
# ---------------------------------------------------------------------------

def maison_bonbons(x, y, s=1.0):
    """Maison en pain d'épice, toit de chocolat et bonbons ; (x, y) = milieu de la base."""
    m = [rect(-160, -200, 320, 200, "#c9772b")]
    for k in range(8):
        m.append(chemin(f"M {-160 + k * 40} -200 q 20 18 40 0", stroke="#fff", sw=6))
    m.append(poly([(-196, -190), (0, -360), (196, -190)], "#6d3b1a"))
    for k in range(6):
        yy = -206 - k * 26
        w = 180 - k * 28
        m.append(chemin(f"M {-w} {yy} q {w / 4} 16 {w / 2} 0 q {w / 4} 16 {w / 2} 0 q {w / 4} 16 {w / 2} 0 q {w / 4} 16 {w / 2} 0", stroke="#ffc9d6", sw=5))
    for k, (bx, by, c) in enumerate([(-120, -230, "#fa5252"), (-50, -290, "#4dabf7"), (40, -300, "#fcc419"), (110, -236, "#51cf66"), (0, -250, "#e64980")]):
        m.append(cercle(bx, by, 14, c))
        m.append(chemin(f"M {bx - 8} {by - 4} q 8 -8 16 0", stroke="#fff", sw=3))
    m.append(chemin("M -40 0 L -40 -110 Q 0 -150 40 -110 L 40 0 Z", "#ffc9d6"))
    m.append(chemin("M -40 0 L -40 -110 Q 0 -150 40 -110 L 40 0", stroke="#fff", sw=8))
    for fx in (-110, 110):
        m.append(rect(fx - 34, -150, 68, 60, "#ffe066"))
        m.append(rect(fx - 34, -150, 68, 60, "none", stroke="#fff", stroke_width=8, rx=4))
        m.append(trait(fx, -150, fx, -90, "#fff", 5))
    for k in range(-3, 4):
        m.append(g([rect(k * 44 - 8, -24, 16, 24, "#fff"), rect(k * 44 - 8, -20, 16, 5, "#fa5252"), rect(k * 44 - 8, -10, 16, 5, "#fa5252"),
                    cercle(k * 44, -34, 14, ["#fa5252", "#51cf66", "#4dabf7", "#fcc419"][k % 4])]))
    m.append(rect(-80, -390, 40, 70, "#fcc2d7"))
    m.append(ellipse(-60, -392, 24, 8, "#fff"))
    return place(m, x, y, s)


def four_pain(x, y, s=1.0, feu=True, ouvert=True):
    """Grand four à pain en briques ; (x, y) = milieu de la base."""
    m = [chemin("M -150 0 L -150 -150 Q -150 -260 0 -260 Q 150 -260 150 -150 L 150 0 Z", "#e8590c")]
    for row in range(6):
        yy = -30 - row * 36
        m.append(trait(-150, yy, 150, yy, "#ffc078", 3, opacity=0.7))
    m.append(chemin("M -70 -40 L -70 -110 Q 0 -170 70 -110 L 70 -40 Z", "#212529" if ouvert else "#495057"))
    if feu and ouvert:
        m.append(chemin("M -56 -40 Q -60 -90 -30 -100 Q -24 -70 -8 -124 Q 10 -80 24 -104 Q 56 -86 56 -40 Z", "#ff922b"))
        m.append(chemin("M -30 -40 Q -32 -70 -12 -76 Q 0 -60 10 -86 Q 32 -64 30 -40 Z", "#ffd43b"))
    if not ouvert:
        m.append(cercle(40, -80, 7, "#ffd43b"))
    m.append(rect(-160, -40, 320, 40, "#c92a2a"))
    return place(m, x, y, s)


def cage_bois(x, y, s=1.0, w=220, h=220, ouverte=False):
    m = []
    for k in range(7):
        xx = -w / 2 + k * w / 6
        m.append(rect(xx - 6, -h, 12, h, "#8d5524", rx=4))
    m += [rect(-w / 2 - 10, -h - 14, w + 20, 20, "#6d4424", rx=6), rect(-w / 2 - 10, -8, w + 20, 16, "#6d4424", rx=6)]
    if ouverte:
        m = m[:2] + m[4:]
    return place(m, x, y, s)


def cage(x, y, s=1.0, couleur="#fab005"):
    """Cage d'oiseau dorée ; (x, y) = milieu du socle."""
    m = [chemin("M -60 0 L -60 -110 Q -60 -170 0 -170 Q 60 -170 60 -110 L 60 0 Z", "none", stroke=couleur, sw=5)]
    for k in range(-2, 3):
        m.append(trait(k * 24, -160 + abs(k) * 6, k * 24, 0, couleur, 4))
    m += [rect(-66, -8, 132, 12, _assombrir(couleur, 0.9), rx=4), cercle(0, -178, 9, "none", stroke=couleur, stroke_width=4)]
    return place(m, x, y, s)


def cailloux_blancs(x0, y0, x1, y1, nb=9, graine=1, brille=True):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        t = k / max(1, nb - 1)
        px = x0 + (x1 - x0) * t + r.uniform(-14, 14)
        py = y0 + (y1 - y0) * t + r.uniform(-8, 8)
        if brille:
            m.append(cercle(px, py - 6, 20, "#fff9db", opacity=0.5))
        m.append(ellipse(px, py - 6, 11, 8, "#f8f9fa", stroke="#ced4da", stroke_width=2))
    return g(m)


def miettes(x0, y0, x1, y1, nb=9, graine=2):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        t = k / max(1, nb - 1)
        m.append(cercle(x0 + (x1 - x0) * t + r.uniform(-10, 10), y0 + (y1 - y0) * t + r.uniform(-6, 6), r.uniform(4, 7), "#e8a15c"))
    return g(m)


def tresor(x, y, s=1.0, ouvert=True):
    """Coffre de bois plein de pièces d'or et de perles ; (x, y) = au sol."""
    m = []
    if ouvert:
        m.append(chemin("M -110 -110 L -120 -210 Q 0 -250 120 -210 L 110 -110 Z", "#6d4424"))
    m += [rect(-110, -110, 220, 110, "#8d5524", rx=10), rect(-110, -70, 220, 14, OR_FONCE),
          rect(-14, -84, 28, 34, OR, rx=4)]
    if ouvert:
        for k in range(9):
            m.append(cercle(-84 + k * 21, -114 - (k % 3) * 12, 15, OR, stroke=OR_FONCE, stroke_width=3))
        for k in range(5):
            m.append(cercle(-60 + k * 30, -132 - (k % 2) * 16, 7, "#f8f9fa", stroke="#dee2e6", stroke_width=2))
    return place(m, x, y, s)


def pain(x, y, s=1.0, rot=0):
    m = [ellipse(0, -30, 70, 34, "#d9822b"), ellipse(0, -34, 62, 26, "#e8a15c")]
    for k in (-30, 0, 30):
        m.append(chemin(f"M {k - 12} -46 q 12 -10 24 4", stroke="#fff4e6", sw=5))
    return place(m, x, y, s, rot=rot)


def bottes(x, y, s=1.0, couleur="#5c3a1e", rot=0):
    """Une paire de grandes bottes (les bottes de sept lieues) ; (x, y) = au sol."""
    m = []
    for dx in (-40, 40):
        m += [rect(dx - 22, -120, 44, 110, couleur, rx=8), ellipse(dx + 12, -10, 36, 14, couleur),
              rect(dx - 26, -128, 52, 18, _assombrir(couleur, 0.8), rx=6)]
    return place(m, x, y, s, rot=rot)


def gros_arbre_sombre(x, y, s=1.0):
    m = [chemin("M -40 0 Q -20 -120 -30 -260 L 30 -260 Q 20 -120 40 0 Z", "#5c3a1e"),
         chemin("M -30 -200 Q -90 -250 -130 -230", stroke="#5c3a1e", sw=18),
         chemin("M 26 -220 Q 90 -270 140 -250", stroke="#5c3a1e", sw=16),
         cercle(0, -320, 110, "#2b8a3e"), cercle(-100, -270, 70, "#237032"), cercle(100, -280, 70, "#237032")]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Le Petit Chaperon rouge
# ---------------------------------------------------------------------------

def panier(x, y, s=1.0, contenu="galette"):
    """Panier d'osier ; (x, y) = fond du panier."""
    m = [chemin("M -50 -50 Q -50 -110 0 -110 Q 50 -110 50 -50", stroke="#8d5524", sw=8)]
    if contenu == "galette":
        m += [ellipse(-12, -54, 30, 14, "#e8a15c"), rect(8, -80, 26, 34, "#a5d8ff", rx=6), rect(12, -88, 18, 10, "#fff", rx=3)]
    elif contenu == "fleurs":
        m += [fleur(-20, -48, 0.6, "#ff6b6b", tige=30), fleur(14, -50, 0.6, "#cc5de8", tige=36)]
    elif contenu == "legumes":
        m += [carotte(-20, -60, 0.5, rot=-30), chou(16, -54, 0.4)]
    m += [chemin("M -56 -50 L 56 -50 L 44 0 L -44 0 Z", "#d9a066"),
          trait(-52, -34, 52, -34, "#a0522d", 4), trait(-48, -16, 48, -16, "#a0522d", 4)]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Ponts, rivières, prés
# ---------------------------------------------------------------------------

def pont_bois(x, y, w=420, s=1.0):
    """Pont de bois en arche ; (x, y) = milieu du tablier."""
    m = [chemin(f"M {-w / 2} 40 Q 0 -30 {w / 2} 40", stroke="#6d4424", sw=26)]
    for k in range(11):
        t = k / 10
        px = -w / 2 + w * t
        py = 40 - 70 * 4 * t * (1 - t) * 0.5
        m.append(rect(px - w / 22, py - 14, w / 11 - 2, 16, "#c68642", rx=3))
    for sgn in (-1, 1):
        m.append(rect(sgn * w * 0.3 - 8, 0, 16, 90, "#6d4424"))
    m.append(chemin(f"M {-w / 2} 0 Q 0 -70 {w / 2} 0", stroke="#8d5524", sw=8))
    for k in range(1, 10):
        t = k / 10
        px = -w / 2 + w * t
        m.append(trait(px, 36 - 70 * 4 * t * (1 - t) * 0.5 - 16, px, -70 * 4 * t * (1 - t) * 0.5 * 1.4 + 6, "#8d5524", 5))
    return place(m, x, y, s)


def pre_vert(S, y=560, riviere_=False):
    ciel(S, "#a5d8ff", "#f4fce3")
    S.add(montagnes(None, y - 20, ("#b2f2bb", "#8ce99a"), neige=False))
    sol(S, y, "#94d82d")
    for k in range(10):
        S.add(fleur(40 + k * 80, y + 60 + (k % 3) * 40, 0.6, ["#ff8787", "#fcc419", "#fff"][k % 3]))


# ---------------------------------------------------------------------------
# Légumes et cuisine
# ---------------------------------------------------------------------------

def carotte(x, y, s=1.0, rot=0):
    m = [chemin("M -14 0 Q 0 110 4 120 Q 12 100 18 0 Z", "#ff922b"),
         trait(-4, 30, 8, 30, "#e8590c", 3), trait(0, 60, 10, 60, "#e8590c", 3),
         chemin("M 0 0 Q -20 -40 -14 -50 M 2 0 Q 4 -44 8 -56 M 6 0 Q 24 -36 28 -44", stroke="#40c057", sw=7)]
    return place(m, x, y, s, rot=rot)


def pomme_terre(x, y, s=1.0):
    m = [ellipse(0, 0, 36, 26, "#c9a07a"), cercle(-12, -6, 3, "#8d6e4f"), cercle(10, 4, 3, "#8d6e4f"), cercle(16, -10, 2.5, "#8d6e4f")]
    return place(m, x, y, s)


def oignon(x, y, s=1.0):
    m = [chemin("M 0 -52 Q -40 -30 -34 4 Q -20 30 0 30 Q 20 30 34 4 Q 40 -30 0 -52 Z", "#e8a15c"),
         chemin("M 0 -52 Q -16 -20 0 30 M 0 -52 Q 16 -20 0 30", stroke="#c97a3a", sw=3),
         chemin("M 0 -52 Q -4 -70 4 -80", stroke="#51cf66", sw=5)]
    return place(m, x, y, s)


def chou(x, y, s=1.0):
    m = [cercle(0, 0, 60, "#8ce99a"), chemin("M -50 -10 Q 0 -70 50 -10", stroke="#51cf66", sw=10),
         chemin("M -40 20 Q 0 -30 40 20", stroke="#69db7c", sw=8), cercle(0, 0, 22, "#d8f5a2")]
    return place(m, x, y, s)


def navet(x, y, s=1.0, visible=1.0):
    """Navet géant ; (x, y) = niveau du sol. `visible` = part hors de terre (0 à 1)."""
    m = []
    for k, a in enumerate((-40, -15, 10, 35)):
        m.append(place(chemin("M 0 0 Q -30 -80 0 -170 Q 30 -80 0 0 Z", "#40c057" if k % 2 else "#2f9e44"), 0, -40 - 260 * visible + 40, rot=a))
    corps = [chemin("M 0 -300 Q 180 -300 150 -120 Q 130 -30 0 40 Q -130 -30 -150 -120 Q -180 -300 0 -300 Z", "#f8f9fa"),
             chemin("M 0 -300 Q 180 -300 150 -180 Q 0 -200 -150 -180 Q -180 -300 0 -300 Z", "#cc5de8"),
             chemin("M 0 40 Q 4 70 -6 100", stroke="#f1f3f5", sw=6),
             chemin("M -90 -120 q 20 6 40 0 M 60 -60 q 16 6 30 0", stroke="#dee2e6", sw=3)]
    cid = uid("n")
    m.append(el("clipPath", rect(-300, -600, 600, 600, "#000"), id=cid))
    m.append(g(place(corps, 0, 300 * (1 - visible)), clip_path=f"url(#{cid})"))
    if visible < 1:
        m.append(ellipse(0, 0, 170, 24, "#7c4a1e"))
    return place(m, x, y, s)


def chaussure(x, y, s=1.0, couleur="#c92a2a", rot=0, finie=True):
    """Soulier de profil, pointe à droite ; (x, y) = sous le talon."""
    fonce = _assombrir(couleur, 0.75)
    m = [chemin("M -50 -10 L -50 -60 Q -20 -64 0 -44 Q 40 -40 60 -20 Q 70 -10 60 0 L -50 0 Z", couleur if finie else "#e9d8c4"),
         rect(-54, -12, 120, 12, fonce, rx=5), rect(-56, -14, 22, 16, fonce, rx=3)]
    if finie:
        m += [trait(-10, -48, 10, -38, "#fff", 3), trait(-4, -52, 16, -42, "#fff", 3), cercle(34, -26, 7, "#ffd43b")]
    else:
        m.append(chemin("M -40 -40 L 50 -14", stroke="#adb5bd", sw=2, stroke_dasharray="6 6"))
    return place(m, x, y, s, rot=rot)


def etabli(x, y, w=320, s=1.0):
    m = [rect(-w / 2 + 16, -120, 18, 120, "#8d5524"), rect(w / 2 - 34, -120, 18, 120, "#8d5524"),
         rect(-w / 2, -140, w, 26, "#a0522d", rx=6), rect(-w / 2 + 30, -60, w - 60, 12, "#8d5524")]
    return place(m, x, y, s)


def marteau(x, y, s=1.0, rot=0):
    return place([rect(-5, -70, 10, 70, "#c68642", rx=4), rect(-24, -86, 48, 20, "#868e96", rx=4)], x, y, s, rot=rot)


def baluchon(x, y, s=1.0, rot=-30):
    """Bâton et baluchon sur l'épaule ; (x, y) = main."""
    m = [trait(-20, 30, 120, -60, "#a0522d", 7), cercle(120, -40, 30, "#e03131"),
         g([cercle(110, -50, 5, "#fff"), cercle(130, -32, 5, "#fff"), cercle(122, -20, 4, "#fff")])]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Cendrillon
# ---------------------------------------------------------------------------

def citrouille(x, y, s=1.0, visage_=False):
    m = [rect(-8, -130, 16, 30, "#5c940d", rx=4),
         ellipse(-50, -60, 50, 60, "#fd7e14"), ellipse(50, -60, 50, 60, "#fd7e14"), ellipse(0, -62, 52, 64, "#ff922b"),
         chemin("M -24 -118 Q -36 -60 -24 -2 M 24 -118 Q 36 -60 24 -2", stroke="#e8590c", sw=4)]
    return place(m, x, y, s)


def carrosse(x, y, s=1.0, cheval_=True, couleur="#ff922b"):
    """Carrosse-citrouille doré ; (x, y) = au sol, sous le milieu."""
    m = []
    if cheval_:
        m.append(place(cheval(0, 0, 1.4, "#f8f9fa"), 240, 0))
        m.append(trait(110, -80, 190, -90, "#f59f00", 5))
    m += [chemin("M -120 -70 Q -150 -250 0 -260 Q 150 -250 120 -70 Z", couleur),
          chemin("M -60 -250 Q -80 -160 -70 -80 M 60 -250 Q 80 -160 70 -80 M 0 -260 L 0 -80", stroke=_assombrir(couleur, 0.85), sw=4),
          chemin("M -50 -200 Q 0 -240 50 -200 L 50 -130 L -50 -130 Z", "#fff3bf", stroke=OR_FONCE, sw=6),
          poly([(-30, -262), (0, -300), (30, -262)], OR), rect(-130, -80, 260, 16, OR_FONCE, rx=8)]
    for wx in (-90, 90):
        m += [cercle(wx, -40, 42, "none", stroke=OR_FONCE, stroke_width=8), cercle(wx, -40, 8, OR_FONCE)]
        for a in range(0, 180, 30):
            r = math.radians(a)
            m.append(trait(wx - math.cos(r) * 40, -40 - math.sin(r) * 40, wx + math.cos(r) * 40, -40 + math.sin(r) * 40, OR, 3))
    return place(m, x, y, s)


def pantoufle_verre(x, y, s=1.0, rot=0, brille=True):
    m = []
    if brille:
        m.append(ellipse(0, -24, 80, 40, "#e7f5ff", opacity=0.6))
    m += [chemin("M -60 0 Q -64 -40 -40 -44 Q -10 -40 10 -26 Q 50 -30 64 -8 Q 60 4 40 4 L -60 4 Z", "#d0ebff", stroke="#74c0fc", sw=3, opacity=0.9),
          trait(-54, 4, -54, 24, "#74c0fc", 7), chemin("M -40 -34 Q -20 -30 0 -20", stroke="#fff", sw=4)]
    if brille:
        m.append(etoile5(40, -30, 8, "#fff"))
    return place(m, x, y, s, rot=rot)


def balai(x, y, s=1.0, rot=0):
    m = [trait(0, 0, 0, -200, "#a0522d", 8), chemin("M -30 50 L -10 0 L 10 0 L 30 50 Z", "#fcc419"),
         trait(-10, 4, 10, 4, "#c92a2a", 6)]
    return place(m, x, y, s, rot=rot)


def salle_bal(S):
    interieur(S, "#e5dbff", "#f3d9fa", 560, papier="#d0bfff")
    for x in (40, 760):
        S.add(rect(x - 30, 0, 60, 560, "#fff"), rect(x - 38, 60, 76, 20, "#e9ecef"))
    for k in range(3):
        cx = 200 + k * 200
        S.add(trait(cx, 0, cx, 60, "#adb5bd", 3))
        S.add(g([ellipse(cx, 70, 60, 14, OR), etincelles(cx, 90, 0.5, OR, graine=k)]))


def horloge_minuit(x, y, r=60):
    return g([rect(x - r - 20, y - r - 20, 2 * r + 40, 2 * r + 60, "#8d5524", rx=14), horloge(x, y, r, 12, 0, "#fff9db", OR_FONCE)])


def horloge_comtoise(x, y, s=1.0, ouverte=False, dedans=""):
    """Grande horloge debout ; (x, y) = au sol."""
    m = [rect(-60, -380, 120, 380, "#8d5524", rx=10), rect(-70, -400, 140, 40, "#6d4424", rx=10),
         cercle(0, -310, 42, "#fff9db", stroke=OR_FONCE, stroke_width=6),
         trait(0, -310, 0, -340, ENCRE, 5), trait(0, -310, 20, -310, ENCRE, 5)]
    m.append(rect(-40, -240, 80, 200, "#343a40" if ouverte else "#6d4424", rx=6))
    if ouverte and dedans:
        m.append(dedans)
    if not ouverte:
        m += [trait(0, -236, 0, -110, "#adb5bd", 4), cercle(0, -100, 20, OR, stroke=OR_FONCE, stroke_width=3)]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Divers
# ---------------------------------------------------------------------------

def tresse(x0, y0, x1, y1, couleur="#f6c453", ep=26):
    """Très longue tresse de (x0, y0) à (x1, y1)."""
    L = math.hypot(x1 - x0, y1 - y0)
    nb = max(3, int(L / 34))
    m = [trait(x0, y0, x1, y1, _assombrir(couleur, 0.85), ep)]
    for k in range(nb):
        t = (k + 0.5) / nb
        px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        m.append(ellipse(px + (4 if k % 2 else -4), py, ep * 0.6, ep * 0.72, couleur, rot=30 if k % 2 else -30))
    m.append(rect(x1 - ep * 0.6, y1 - 6, ep * 1.2, 12, "#e64980", rx=6))
    m.append(chemin(f"M {n(x1 - ep * 0.4)} {n(y1 + 6)} L {x1} {n(y1 + 50)} L {n(x1 + ep * 0.4)} {n(y1 + 6)} Z", couleur))
    return g(m)


def miroir(x, y, s=1.0, reflet=""):
    """Grand miroir sur pied ; (x, y) = au sol."""
    m = [rect(-10, -80, 20, 80, OR_FONCE), ellipse(0, -2, 60, 12, OR_FONCE),
         ellipse(0, -250, 100, 170, OR, stroke=OR_FONCE, stroke_width=6), ellipse(0, -250, 86, 156, "#e7f5ff")]
    if reflet:
        cid = uid("r")
        m.append(el("clipPath", ellipse(0, -250, 86, 156, "#000"), id=cid))
        m.append(g(reflet, clip_path=f"url(#{cid})"))
    m.append(chemin("M -50 -330 Q -60 -280 -40 -230", stroke="#fff", sw=10, opacity=0.6))
    return place(m, x, y, s)


def metier_tisser(x, y, s=1.0, vide=True):
    """Métier à tisser ; (x, y) = au sol."""
    m = [rect(-150, -300, 20, 300, "#8d5524"), rect(130, -300, 20, 300, "#8d5524"),
         rect(-160, -310, 320, 24, "#a0522d", rx=6), rect(-150, -140, 300, 20, "#a0522d", rx=6)]
    for k in range(13):
        m.append(trait(-120 + k * 20, -286, -120 + k * 20, -140, "#dee2e6", 1.5, opacity=0.8))
    return place(m, x, y, s)


def maison_village(x, y, s=1.0, **k):
    return maison(x, y, s, **k)


def village_(S, y=600, graine=4):
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a")
    S.add(maison(110, y + 10, 0.6, toit="#e8590c"), maison(300, y - 10, 0.45, toit="#1c7ed6", mur="#fff3bf"),
          maison(700, y + 10, 0.55, toit="#c2255c", mur="#e7f5ff"))
