"""
Personnages et objets des livres de sciences : caneton, pingouin, nuage,
graine, glaçon, enfants, chauve-souris… et accessoires qui doivent être
exacts (phases de la Lune, aimants, boussole, ombres, flèches de force).

Mêmes conventions que `base.py` : page de 800 × 800, personnages « debout »
les pieds en (0, 0).
"""
from base import *
from base import EXPRESSIONS, _assombrir
from fantastique import personne, PEAUX, CHEVEUX


# ---------------------------------------------------------------------------
# Outils de dessin
# ---------------------------------------------------------------------------

def fleche(x1, y1, x2, y2, couleur=ENCRE, sw=7, tete=20, **a):
    """Flèche droite de (x1, y1) vers (x2, y2)."""
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - math.cos(ang) * tete * 0.8, y2 - math.sin(ang) * tete * 0.8
    pts = [(x2, y2),
           (x2 - math.cos(ang - 0.45) * tete, y2 - math.sin(ang - 0.45) * tete),
           (x2 - math.cos(ang + 0.45) * tete, y2 - math.sin(ang + 0.45) * tete)]
    return g([trait(x1, y1, bx, by, couleur, sw), poly(pts, couleur, stroke=couleur, stroke_width=3, stroke_linejoin="round")], **a)


def fleche_courbe(d, fin, direction, couleur=ENCRE, sw=6, tete=18, **a):
    """Chemin `d` terminé par une pointe en `fin`, orientée selon l'angle `direction` (degrés)."""
    ang = math.radians(direction)
    x2, y2 = fin
    pts = [(x2, y2),
           (x2 - math.cos(ang - 0.45) * tete, y2 - math.sin(ang - 0.45) * tete),
           (x2 - math.cos(ang + 0.45) * tete, y2 - math.sin(ang + 0.45) * tete)]
    return g([chemin(d, stroke=couleur, sw=sw), poly(pts, couleur, stroke=couleur, stroke_width=3, stroke_linejoin="round")], **a)


def ombre(x, y, longueur, cote=1, largeur=16, couleur="#1b1f3b", opacity=0.28):
    """Ombre portée au sol qui part des pieds (x, y) vers la droite (cote=1) ou la gauche (-1)."""
    if longueur <= 2 * largeur:
        return ellipse(x, y, max(longueur, largeur * 1.6), largeur * 0.6, couleur, opacity=opacity)
    return ellipse(x + cote * longueur / 2, y, longueur / 2, largeur, couleur, opacity=opacity)


def rayons_soleil(x0, y0, x1, y1, couleur="#fcc419", nb=3, ecart=26, sw=4, **a):
    """Quelques rayons de lumière parallèles, du soleil vers une cible (pointillés)."""
    ang = math.atan2(y1 - y0, x1 - x0)
    px, py = -math.sin(ang), math.cos(ang)
    m = []
    for k in range(nb):
        d = (k - (nb - 1) / 2) * ecart
        m.append(trait(x0 + px * d, y0 + py * d, x1 + px * d, y1 + py * d, couleur, sw, stroke_dasharray="14 10", **a))
    return g(m)


def degrade_radial(S, centre, bord, **a):
    return S.degrade([centre, bord], radial=True, **a)


# ---------------------------------------------------------------------------
# La Lune et ses phases
# ---------------------------------------------------------------------------

def lune_phase(x, y, r, eclairee=1.0, croissante=True, clair="#fff3bf", sombre=None, halo=True, crateres=True):
    """La Lune vue depuis l'hémisphère Nord.

    eclairee : fraction éclairée du disque (0 = nouvelle lune, 1 = pleine lune).
    croissante : la partie éclairée est à droite (lune qui grandit) ;
    sinon à gauche (lune qui décroît).
    sombre : couleur de la partie non éclairée (sinon elle n'est pas dessinée).
    """
    m = []
    if halo and eclairee > 0.3:
        m.append(cercle(0, 0, r * 1.5, clair, opacity=0.12 * eclairee))
    if sombre:
        m.append(cercle(0, 0, r, sombre))
    if eclairee >= 0.995:
        m.append(cercle(0, 0, r, clair))
    elif eclairee > 0.005:
        rx = abs(1 - 2 * eclairee) * r
        balayage = 1 if eclairee > 0.5 else 0
        d = f"M 0 {n(-r)} A {n(r)} {n(r)} 0 0 1 0 {n(r)} A {n(rx)} {n(r)} 0 0 {balayage} 0 {n(-r)} Z"
        m.append(chemin(d, clair))
    if crateres and eclairee > 0.005:
        cid = uid("l")
        if eclairee >= 0.995:
            forme = cercle(0, 0, r, "#000")
        else:
            forme = chemin(d, "#000")
        m.append(el("clipPath", forme, id=cid))
        cr = [cercle(-r * .3, -r * .3, r * .18, "#e9d8a6"), cercle(r * .32, r * .28, r * .13, "#e9d8a6"),
              cercle(r * .38, -r * .38, r * .09, "#e9d8a6"), cercle(-r * .2, r * .42, r * .1, "#e9d8a6"),
              cercle(r * .05, r * .02, r * .08, "#e9d8a6")]
        m.append(g(cr, clip_path=f"url(#{cid})", opacity=0.7))
    return place(m, x, y, 1, flip=not croissante)


def boule_eclairee(x, y, r, couleur, ombre_couleur="#000", lumiere_depuis=180, opacity=0.55, **a):
    """Sphère dont la moitié tournée vers la lumière est éclairée.

    lumiere_depuis : direction (degrés, 0 = droite, 90 = bas, 180 = gauche) d'où vient la lumière.
    """
    cid = uid("b")
    m = [cercle(0, 0, r, couleur, **a)]
    m.append(el("clipPath", cercle(0, 0, r, "#000"), id=cid))
    m.append(g(rect(0, -r - 2, r + 2, 2 * r + 4, ombre_couleur, opacity=opacity), clip_path=f"url(#{cid})",
               transform=f"rotate({n(lumiere_depuis + 180)})"))
    return place(m, x, y)


# ---------------------------------------------------------------------------
# Personnages
# ---------------------------------------------------------------------------

def enfant(x=0, y=0, s=1.0, habit="#4dabf7", jambes="#364fc7", robe=False, **k):
    """Un enfant ordinaire (T-shirt et pantalon, ou robe)."""
    k.setdefault("coiffure", "courts")
    return personne(x, y, s, habit=habit, jambes=jambes, robe=robe, **k)


def canard(x, y, s=1.0, expr="sourire", flip=False, regard=(1, 0), couleur="#ffd43b", nage=True, rot=0, ailes="bas"):
    """Caneton de profil, la tête à droite. Si `nage`, (x, y) est sur la ligne
    d'eau et le bas du corps est caché sous l'eau ; sinon (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.88)
    bec = "#ff922b"
    m = []
    corps = [poly([(-50, -34), (-92, -66), (-66, -8)], couleur),
             ellipse(-4, -18, 66, 42, couleur)]
    if not nage:
        for dx in (-14, 14):
            m.append(trait(dx, 12, dx, 38, bec, 6))
            m.append(ellipse(dx + 8, 40, 14, 6, bec))
        corps = [place(corps, 0, -20)]
        dy = -20
    else:
        dy = 0
    m += corps
    if ailes == "haut":
        m.append(ellipse(-20, -62 + dy, 16, 38, fonce, rot=-40))
    else:
        m.append(ellipse(-12, -22 + dy, 36, 20, fonce, rot=-8))
        m.append(chemin(f"M -40 {-16 + dy} q 14 8 30 4 q 12 -2 22 -10", stroke=_assombrir(couleur, 0.75), sw=3))
    # tête
    hx, hy = 42, -82 + dy
    m.append(cercle(hx, hy, 36, couleur))
    m.append(chemin(f"M {hx - 8} {hy - 34} q 2 -16 12 -14 q -6 4 0 10 q 4 -12 14 -8", stroke=couleur, sw=6))
    ouvert = bs in ("ouverte", "o", "crie", "baille")
    if ouvert:
        m.append(chemin(f"M {hx + 22} {hy + 2} Q {hx + 56} {hy - 8} {hx + 60} {hy + 2} Q {hx + 44} {hy + 8} {hx + 22} {hy + 6} Z", bec))
        m.append(chemin(f"M {hx + 22} {hy + 10} Q {hx + 48} {hy + 14} {hx + 52} {hy + 22} Q {hx + 36} {hy + 26} {hx + 22} {hy + 18} Z", _assombrir(bec, 0.85)))
    else:
        m.append(chemin(f"M {hx + 22} {hy + 2} Q {hx + 58} {hy - 4} {hx + 62} {hy + 8} Q {hx + 46} {hy + 20} {hx + 22} {hy + 16} Z", bec))
        m.append(trait(hx + 26, hy + 9, hx + 54, hy + 9, _assombrir(bec, 0.8), 2.5))
    m.append(ellipse(hx + 12, hy + 12, 8, 5, ROSE, opacity=0.7))
    m.append(oeil(hx + 8, hy - 8, ys, regard, taille=1.0))
    m.append(place(sourcils(8, -8, ss), hx, hy) if ss else "")
    if nage:
        cid = uid("e")
        m = [el("clipPath", rect(-200, -300, 400, 300 + 6, "#000"), id=cid), g(m, clip_path=f"url(#{cid})"),
             ellipse(-6, 4, 84, 9, "#fff", opacity=0.55), ellipse(-6, 4, 64, 5, "#d0ebff", opacity=0.8)]
    return place(m, x, y, s, flip=flip, rot=rot)


def pingouin(x, y, s=1.0, expr="sourire", ailes="bas", regard=(0, 0), flip=False, echarpe="#fa5252", rot=0, pieds_haut=False, objet=None):
    """Pingo, un petit pingouin debout vu de face ; (x, y) = sous les pattes.
    ailes : "bas", "haut", "ouvertes", "devant" (frotte ses ailes)."""
    ys, bs, ss = EXPRESSIONS[expr]
    noir, blanc, orange = "#2b3445", "#ffffff", "#ff922b"
    m = []
    if pieds_haut:
        m += [ellipse(-26, -10, 12, 20, orange, rot=30), ellipse(26, -10, 12, 20, orange, rot=-30)]
    else:
        m += [ellipse(-22, -6, 20, 9, orange), ellipse(22, -6, 20, 9, orange)]
    pos = {"bas": ((-54, -76, 18), (54, -76, -18)), "haut": ((-66, -150, 150), (66, -150, -150)),
           "ouvertes": ((-80, -104, 60), (80, -104, -60)), "devant": ((-14, -82, -60), (14, -86, 60))}[ailes]
    if ailes != "devant":
        for ax, ay, ar in pos:
            m.append(ellipse(ax, ay, 14, 42, noir, rot=ar))
    m.append(ellipse(0, -84, 60, 82, noir))
    m.append(ellipse(0, -66, 43, 60, blanc))
    # visage blanc en forme de cœur
    m.append(cercle(-19, -134, 24, blanc) + cercle(19, -134, 24, blanc) + ellipse(0, -116, 30, 20, blanc))
    m.append(ellipse(-32, -114, 8, 5, ROSE, opacity=0.7) + ellipse(32, -114, 8, 5, ROSE, opacity=0.7))
    m.append(oeil(-17, -136, ys, regard, taille=0.95) + oeil(17, -136, ys, regard, taille=0.95))
    m.append(sourcils(17, -136, ss))
    if bs in ("ouverte", "o", "crie", "baille"):
        m.append(poly([(-10, -121), (10, -121), (0, -131)], orange) + poly([(-9, -117), (9, -117), (0, -104)], "#f76707"))
    else:
        m.append(poly([(-11, -122), (11, -122), (0, -106)], orange))
    if echarpe:
        m.append(g([chemin("M -42 -100 Q 0 -86 42 -100 L 40 -86 Q 0 -72 -40 -86 Z", echarpe),
                    chemin("M 16 -88 L 30 -44 L 14 -44 L 6 -86 Z", echarpe),
                    trait(16, -52, 29, -52, "#fff", 3, opacity=0.6)]))
    if objet:
        m.append(objet)
    if ailes == "devant":
        for ax, ay, ar in pos:
            m.append(ellipse(ax, ay, 13, 36, noir, rot=ar))
    return place(m, x, y, s, flip=flip, rot=rot)


def pingouin_glisse(x, y, s=1.0, expr="rire", flip=False, echarpe="#fa5252", vitesse=True):
    """Pingo qui glisse sur le ventre, la tête à droite ; (x, y) = sous le ventre."""
    ys, bs, ss = EXPRESSIONS[expr]
    noir, orange = "#2b3445", "#ff922b"
    m = []
    if vitesse:
        m += [trait(-150 - k * 14, -20 - k * 16, -110 - k * 14, -20 - k * 16, "#74c0fc", 5, opacity=0.8) for k in range(3)]
    m.append(ellipse(-100, -22, 20, 9, orange, rot=-20) + ellipse(-104, -8, 20, 9, orange, rot=10))
    if echarpe:
        m.append(chemin("M 52 -54 Q 10 -80 -30 -70 L -24 -58 Q 10 -66 50 -44 Z", echarpe))
    m.append(ellipse(-4, -36, 100, 36, noir))
    m.append(ellipse(4, -18, 88, 18, "#ffffff"))
    m.append(ellipse(-4, -54, 54, 11, _assombrir(noir, 0.8), rot=4))
    m.append(cercle(86, -52, 38, noir))
    m.append(ellipse(96, -46, 26, 24, "#ffffff"))
    m.append(ellipse(96, -30, 8, 5, ROSE, opacity=0.7))
    m.append(oeil(100, -56, ys, (1, 0), taille=0.9))
    m.append(place(sourcils(8, 0, ss), 100, -56) if ss else "")
    if bs in ("ouverte", "o", "crie"):
        m.append(poly([(118, -48), (146, -50), (120, -40)], orange) + poly([(118, -38), (140, -32), (118, -32)], "#f76707"))
    else:
        m.append(poly([(118, -48), (148, -42), (118, -34)], orange))
    if echarpe:
        m.append(chemin("M 58 -78 Q 70 -46 60 -14 L 48 -18 Q 56 -46 46 -74 Z", echarpe))
    return place(m, x, y, s, flip=flip)


def nuage_perso(x, y, s=1.0, couleur="#ffffff", expr="sourire", regard=(0, 0), ombre="#dbe4ff", joues=True, larmes=False):
    """Petit Nuage, avec un visage ; (x, y) = centre du nuage."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [nuage(0, 0, 1.0, couleur, ombre=ombre)]
    fx, fy = 8, 8
    if joues:
        m.append(ellipse(fx - 44, fy + 14, 11, 6.5, ROSE, opacity=0.75) + ellipse(fx + 44, fy + 14, 11, 6.5, ROSE, opacity=0.75))
    m.append(oeil(fx - 24, fy - 4, ys, regard, taille=1.15) + oeil(fx + 24, fy - 4, ys, regard, taille=1.15))
    m.append(place(sourcils(24, -4, ss), fx, fy) if ss else "")
    m.append(bouche(fx, fy + 16, bs, 1.0))
    if larmes:
        m.append(goutte(fx - 30, fy + 30, 0.8, "#74c0fc") + goutte(fx + 30, fy + 30, 0.8, "#74c0fc"))
    return place(m, x, y, s)


def graine_perso(x, y, s=1.0, expr="dort", regard=(0, 0), rot=0):
    """Graine de tournesol (grise rayée de blanc) avec un visage ; (x, y) = bas de la graine."""
    ys, bs, ss = EXPRESSIONS[expr]
    forme = "M 0 -120 Q 54 -96 52 -46 Q 48 0 0 0 Q -48 0 -52 -46 Q -54 -96 0 -120 Z"
    cid = uid("g")
    m = [chemin(forme, "#5c5f66"), el("clipPath", chemin(forme, "#000"), id=cid)]
    bandes = [chemin(f"M {dx} -124 Q {dx * 1.35} -60 {dx} 4", stroke="#dee2e6", sw=5) for dx in (-34, -12, 12, 34)]
    m.append(g(bandes, clip_path=f"url(#{cid})", opacity=0.55))
    m.append(ellipse(-26, -34, 8, 5, ROSE, opacity=0.9) + ellipse(26, -34, 8, 5, ROSE, opacity=0.9))
    for sgn in (-1, 1):
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * 14, -54, ys, regard, taille=0.9).replace(ENCRE, "#fff"))
        else:
            m.append(oeil(sgn * 14, -54, ys, regard, sclere=True, taille=0.8))
    m.append(place(sourcils(14, -54, ss), 0, 0).replace(ENCRE, "#fff") if ss else "")
    m.append(place(bouche(0, 0, bs, 0.7), 0, -36).replace(ENCRE, "#fff"))
    m.append(chemin("M -22 -100 Q -10 -110 6 -110", stroke="#fff", sw=5, opacity=0.35))
    return place(m, x, y, s, rot=rot)


def glacon(x, y, s=1.0, expr="sourire", regard=(0, 0), taille=1.0, fondu=0.0, rot=0, gouttes=False):
    """Gaston le glaçon ; (x, y) = milieu du bas. `fondu` (0 à 0.7) l'arrondit et le rapetisse."""
    ys, bs, ss = EXPRESSIONS[expr]
    w = 120 * taille * (1 - fondu * 0.5)
    h = 116 * taille * (1 - fondu * 0.6)
    rx = 18 + fondu * 40
    m = []
    if fondu > 0:
        m.append(ellipse(0, 0, w * 0.8 + fondu * 60, 12 + fondu * 6, "#a5d8ff", opacity=0.8))
    m.append(rect(-w / 2, -h, w, h, "#d0ebff", rx=rx, stroke="#74c0fc", stroke_width=5))
    m.append(rect(-w / 2 + 12, -h + 12, w * 0.3, h * 0.18, "#fff", rx=6, opacity=0.85))
    m.append(rect(w / 2 - 22, -h + 16, 8, h * 0.45, "#fff", rx=4, opacity=0.6))
    fy = -h * 0.48
    k = min(1.0, max(0.7, w / 120))
    m.append(ellipse(-w * 0.3, fy + 16 * k, 8 * k, 5 * k, ROSE, opacity=0.75) + ellipse(w * 0.3, fy + 16 * k, 8 * k, 5 * k, ROSE, opacity=0.75))
    m.append(oeil(-15 * k, fy, ys, regard, taille=k) + oeil(15 * k, fy, ys, regard, taille=k))
    m.append(place(sourcils(15 * k, fy, ss), 0, 0) if ss else "")
    m.append(bouche(0, fy + 18 * k, bs, k))
    if gouttes:
        m.append(goutte(w / 2 + 8, -h * 0.3, 0.7, "#74c0fc") + goutte(-w / 2 - 6, -h * 0.55, 0.6, "#74c0fc"))
    return place(m, x, y, s, rot=rot)


def goutte_perso(x, y, s=1.0, expr="sourire", couleur="#4dabf7", regard=(0, 0)):
    """Goutte d'eau avec un visage ; (x, y) = bas de la goutte."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M 0 -110 Q 50 -40 44 -26 Q 34 0 0 0 Q -34 0 -44 -26 Q -50 -40 0 -110 Z", couleur),
         chemin("M -20 -56 Q -26 -40 -22 -28", stroke="#fff", sw=6, opacity=0.6),
         ellipse(-22, -18, 6, 4, ROSE, opacity=0.8), ellipse(22, -18, 6, 4, ROSE, opacity=0.8),
         oeil(-11, -34, ys, regard, taille=0.7), oeil(11, -34, ys, regard, taille=0.7),
         place(bouche(0, 0, bs, 0.6), 0, -20)]
    return place(m, x, y, s)


def chauve_souris(x, y, s=1.0, expr="sourire", couleur="#5f3dc4", ailes="ouvertes", flip=False, regard=(0, 0)):
    """Chauve-souris qui vole, vue de face ; (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = []
    if ailes == "ouvertes":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 20} -10 Q {sgn * 70} -60 {sgn * 120} -30 Q {sgn * 104} -12 {sgn * 110} 8 "
                            f"Q {sgn * 88} -4 {sgn * 78} 16 Q {sgn * 60} 0 {sgn * 46} 18 Q {sgn * 36} 4 {sgn * 20} 14 Z", fonce))
    else:
        m.append(ellipse(-26, 0, 14, 30, fonce, rot=10) + ellipse(26, 0, 14, 30, fonce, rot=-10))
    m.append(ellipse(0, 4, 26, 30, couleur))
    for sgn in (-1, 1):
        m.append(poly([(sgn * 10, -34), (sgn * 26, -64), (sgn * 30, -30)], couleur))
    m.append(cercle(0, -28, 28, couleur))
    m.append(oeil(-10, -32, ys, regard, taille=0.7) + oeil(10, -32, ys, regard, taille=0.7))
    m.append(ellipse(-19, -20, 5, 3, ROSE, opacity=0.8) + ellipse(19, -20, 5, 3, ROSE, opacity=0.8))
    m.append(place(bouche(0, 0, bs, 0.6), 0, -18))
    m.append(poly([(-6, -13), (-3, -6), (0, -13)], "#fff") + poly([(0, -13), (3, -6), (6, -13)], "#fff"))
    return place(m, x, y, s, flip=flip)


def mesange(x, y, s=1.0, **k):
    """Mésange bleue : tête et ailes bleues, ventre jaune."""
    k.setdefault("couleur", "#339af0")
    k.setdefault("ventre", "#ffe066")
    return oiseau(x, y, s, **k)


def tournesol(x, y, s=1.0, tige=260, tete=1.0, visage=None, rot=0, feuilles=6, graines_tombent=False, fane=False):
    """Tournesol ; (x, y) = pied de la tige au sol."""
    m = [chemin(f"M 0 0 Q 10 {-tige / 2} 0 {-tige}", stroke="#2f9e44", sw=12)]
    for k in range(feuilles):
        yy = -30 - k * (tige - 60) / max(1, feuilles)
        sgn = -1 if k % 2 == 0 else 1
        m.append(chemin(f"M 4 {n(yy)} Q {sgn * 40} {n(yy - 40)} {sgn * 86} {n(yy - 14)} Q {sgn * 44} {n(yy + 10)} 4 {n(yy)} Z", "#40c057"))
        m.append(chemin(f"M 4 {n(yy)} Q {sgn * 40} {n(yy - 18)} {sgn * 80} {n(yy - 14)}", stroke="#2f9e44", sw=2.5))
    t = []
    pet = "#adb54a" if fane else "#fcc419"
    pet2 = "#9c9a40" if fane else "#fab005"
    t = [place(ellipse(0, -84, 17, 40, pet if k % 2 else pet2), 0, 0, rot=k * 20) for k in range(18)]
    t.append(cercle(0, 0, 60, "#7c4a1e"))
    t.append(cercle(0, 0, 60, "none", stroke="#5c3a1e", stroke_width=6))
    for k in range(26):
        a = k * 2.4
        rr = 8 * math.sqrt(k)
        t.append(cercle(math.cos(a) * rr, math.sin(a) * rr, 3.2, "#5c3a1e"))
    if visage:
        ys, bs, ss = EXPRESSIONS[visage]
        t.append(ellipse(-32, 14, 8, 5, ROSE, opacity=0.8) + ellipse(32, 14, 8, 5, ROSE, opacity=0.8))
        t.append(cercle(-16, -8, 13, "#7c4a1e") + cercle(16, -8, 13, "#7c4a1e"))
        t.append(g([oeil(-16, -8, ys, (0, 0)), oeil(16, -8, ys, (0, 0))]).replace(ENCRE, "#2b1a0a"))
        t.append(bouche(0, 16, bs, 1.0).replace(ENCRE, "#2b1a0a"))
    m.append(place(t, 0, -tige, tete, rot=rot))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Aimants et boussole
# ---------------------------------------------------------------------------

NORD_C, SUD_C = "#e03131", "#1c7ed6"


def aimant_u(x, y, s=1.0, rot=0, couleur="#e03131"):
    """Aimant en fer à cheval, les pôles vers le haut ; (x, y) = bas du « U »."""
    m = [chemin("M -48 -150 L -48 -64 A 48 48 0 0 0 48 -64 L 48 -150", stroke=_assombrir(couleur, 0.8), sw=44),
         chemin("M -48 -150 L -48 -64 A 48 48 0 0 0 48 -64 L 48 -150", stroke=couleur, sw=36),
         chemin("M -58 -140 L -58 -70", stroke="#fff", sw=5, opacity=0.4),
         rect(-70, -186, 44, 40, "#ced4da", rx=4), rect(26, -186, 44, 40, "#ced4da", rx=4),
         rect(-66, -182, 10, 32, "#fff", rx=3, opacity=0.6), rect(30, -182, 10, 32, "#fff", rx=3, opacity=0.6)]
    return place(m, x, y, s, rot=rot)


def barreau(x, y, w=220, h=56, nord_a_droite=True, rot=0, lettres=True):
    """Aimant droit : moitié rouge (N) et moitié bleue (S) ; (x, y) = centre."""
    gauche, droite = (SUD_C, NORD_C) if nord_a_droite else (NORD_C, SUD_C)
    lg, ld = ("S", "N") if nord_a_droite else ("N", "S")
    m = [rect(-w / 2, -h / 2, w / 2, h, gauche, rx=6), rect(0, -h / 2, w / 2, h, droite, rx=6),
         rect(-w / 2 + 6, -h / 2 + 5, w - 12, h * 0.18, "#fff", rx=4, opacity=0.35)]
    if lettres:
        m.append(texte(-w / 4, h * 0.2, lg, h * 0.6, "#fff"))
        m.append(texte(w / 4, h * 0.2, ld, h * 0.6, "#fff"))
    return place(m, x, y, rot=rot)


def boussole(x, y, r=60, angle=0, fond_="#fff9db", cadran=True):
    """Boussole ; `angle` = direction où pointe la pointe rouge (0 = vers le haut de la page)."""
    m = [cercle(0, 0, r + 12, "#e8590c"), cercle(0, 0, r + 4, "#fff4e6"), cercle(0, 0, r, fond_)]
    if cadran:
        for lettre, a in (("N", 0), ("E", 90), ("S", 180), ("O", 270)):
            ang = math.radians(a - 90)
            m.append(texte(math.cos(ang) * r * 0.74, math.sin(ang) * r * 0.74 + r * 0.1, lettre, r * 0.28, "#868e96"))
    aig = [poly([(0, -r * 0.62), (-r * 0.13, 0), (r * 0.13, 0)], NORD_C), poly([(0, r * 0.62), (-r * 0.13, 0), (r * 0.13, 0)], "#adb5bd"),
           cercle(0, 0, r * 0.08, ENCRE)]
    m.append(place(aig, 0, 0, rot=angle))
    return place(m, x, y)


# ---------------------------------------------------------------------------
# Petits objets de laboratoire
# ---------------------------------------------------------------------------

def trombone(x, y, s=1.0, rot=0, couleur="#868e96"):
    d = "M -20 8 L -20 -22 A 8 8 0 0 1 -4 -22 L -4 14 A 12 12 0 0 1 -28 14 L -28 -26 A 16 16 0 0 1 4 -26 L 4 6"
    return place(chemin(d, stroke=couleur, sw=3.5), x, y, s, rot=rot)


def cle(x, y, s=1.0, rot=0, couleur="#fab005"):
    m = [cercle(-26, 0, 18, "none", stroke=couleur, stroke_width=9), rect(-10, -5, 56, 10, couleur, rx=3),
         rect(30, 5, 7, 12, couleur), rect(40, 5, 7, 9, couleur)]
    return place(m, x, y, s, rot=rot)


def clou(x, y, s=1.0, rot=0):
    m = [rect(-4, -60, 8, 60, "#adb5bd"), poly([(-4, 0), (4, 0), (0, 14)], "#adb5bd"), rect(-14, -66, 28, 8, "#868e96", rx=3)]
    return place(m, x, y, s, rot=rot)


def vis(x, y, s=1.0, rot=0):
    m = [rect(-5, -50, 10, 50, "#adb5bd"), poly([(-5, 0), (5, 0), (0, 12)], "#adb5bd"),
         chemin("M -12 -58 Q 0 -70 12 -58 L 12 -50 L -12 -50 Z", "#868e96")]
    m += [trait(-5, -42 + k * 9, 5, -38 + k * 9, "#868e96", 2) for k in range(5)]
    return place(m, x, y, s, rot=rot)


def verre(x, y, w=110, h=150, contenu=None, niveau=0.6, couleur_contenu="#a5d8ff"):
    """Verre droit ; (x, y) = milieu du bas. `contenu` : dessin placé à l'intérieur (avant le verre)."""
    m = []
    if niveau:
        hl = h * niveau
        m.append(chemin(f"M {-w / 2 + 6} {-hl} L {w / 2 - 6} {-hl} L {w / 2 - 10} -6 Q 0 0 {-w / 2 + 10} -6 Z", couleur_contenu, opacity=0.9))
    if contenu:
        m.append(contenu)
    m.append(chemin(f"M {-w / 2} {-h} L {-w / 2 + 8} -4 Q 0 4 {w / 2 - 8} -4 L {w / 2} {-h}", stroke="#adb5bd", sw=4, fill="#e7f5ff", fill_opacity=0.25))
    m.append(chemin(f"M {-w / 2 + 12} {-h + 14} L {-w / 2 + 18} {-h * 0.3}", stroke="#fff", sw=6, opacity=0.8))
    m.append(ellipse(0, -h, w / 2, 7, "none", stroke="#adb5bd", stroke_width=3))
    return place(m, x, y)


# ---------------------------------------------------------------------------
# Air et vent
# ---------------------------------------------------------------------------

def vent(x, y, s=1.0, couleur="#ffffff", rot=0, opacity=0.9, longueur=160):
    """Trait de vent terminé par une boucle, soufflant vers la droite ; (x, y) = début."""
    L = longueur
    d = f"M 0 0 L {L * 0.7} 0 Q {L} 0 {L} -22 Q {L} -44 {L * 0.84} -44 Q {L * 0.7} -44 {L * 0.72} -28"
    return place(chemin(d, stroke=couleur, sw=7, opacity=opacity), x, y, s, rot=rot)


def rafales(x, y, s=1.0, couleur="#ffffff", rot=0, opacity=0.9):
    """Trois traits de vent superposés, vers la droite."""
    return place(g([vent(0, 0, 1, couleur, 0, opacity, 170), vent(-50, 46, 1, couleur, 0, opacity, 130),
                    trait(20, 90, 150, 90, couleur, 7, opacity=opacity)]), x, y, s, rot=rot)


def vent_visage(x, y, s=1.0, couleur="#e7f5ff", expr="souffle", flip=False):
    """Le Vent personnifié : une grosse bouffée d'air qui souffle vers la droite."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [cercle(-30, 0, 62, couleur), cercle(30, -20, 50, couleur), cercle(26, 30, 44, couleur),
         cercle(-70, -30, 34, couleur), cercle(-72, 34, 36, couleur)]
    m.append(ellipse(-10, 14, 13, 8, ROSE, opacity=0.8) + ellipse(52, 14, 11, 7, ROSE, opacity=0.8))
    m.append(oeil(0, -12, ys, (1, 0)) + oeil(36, -14, ys, (1, 0)))
    m.append(ellipse(62, 12, 9, 11, "#74c0fc"))
    for k, (dy, L) in enumerate([(-30, 150), (12, 190), (54, 140)]):
        m.append(chemin(f"M 84 {dy + 12} q {L / 3} -{10 + k * 4} {L * 2 / 3} 0 t {L / 3} 0", stroke=couleur, sw=8, opacity=0.9))
    return place(m, x, y, s, flip=flip)


# ---------------------------------------------------------------------------
# Lumière
# ---------------------------------------------------------------------------

ARC_COULEURS = ("#fa5252", "#ff922b", "#fcc419", "#51cf66", "#339af0", "#7950f2")


def arc_en_ciel_vrai(S, cx, cy, r, ep=20, horizon=None, secondaire=True, opacity=0.85):
    """Arc-en-ciel fidèle : rouge à l'extérieur, violet à l'intérieur, ciel plus clair
    sous l'arc, second arc pâle aux couleurs inversées (rayon ≈ 51°/42° du premier),
    et bande plus sombre entre les deux. Le centre (cx, cy) est le point opposé au
    Soleil : il est sous l'horizon quand le Soleil est haut."""
    horizon = cy if horizon is None else horizon
    cid = uid("a")
    S.defs.append(el("clipPath", rect(0, 0, S.w, horizon, "#000"), id=cid))
    m = [cercle(cx, cy, r - ep * 6, "#ffffff", opacity=0.22)]
    r2 = r * 51 / 42
    if secondaire:
        m.append(cercle(cx, cy, r2 - ep * 0.6, "none", stroke="#1c2a52", stroke_width=r2 - r - ep * 1.2, opacity=0.08))
        for k, c in enumerate(reversed(ARC_COULEURS)):
            m.append(cercle(cx, cy, r2 + k * ep * 0.75, "none", stroke=c, stroke_width=ep * 0.75 + 1, opacity=0.22))
    for k, c in enumerate(ARC_COULEURS):
        m.append(cercle(cx, cy, r - k * ep, "none", stroke=c, stroke_width=ep + 1, opacity=opacity))
    S.add(g(m, clip_path=f"url(#{cid})"))


def _filtre_ombre(S, alpha=0.35, couleur=(0.07, 0.09, 0.2), flou=0):
    cle = (alpha, couleur, flou)
    cache = S.__dict__.setdefault("_ombres", {})
    if cle not in cache:
        i = uid("f")
        r, v, b = couleur
        contenu = el("feColorMatrix", type="matrix", values=f"0 0 0 0 {r}  0 0 0 0 {v}  0 0 0 0 {b}  0 0 0 {alpha} 0")
        if flou:
            contenu += el("feGaussianBlur", stdDeviation=flou)
        S.defs.append(el("filter", contenu, id=i, x="-50%", y="-50%", width="200%", height="200%"))
        cache[cle] = i
    return cache[cle]


def ombre_portee(S, dessin, x, y, longueur=1.0, cote=1, aplati=0.42, alpha=0.42):
    """Ombre d'un personnage couchée sur le sol, à partir de ses pieds (x, y).

    `dessin` est le personnage dessiné avec les pieds en (0, 0) et à la même
    échelle que dans la scène. longueur = rapport longueur de l'ombre / taille
    (grand quand le Soleil est bas) ; cote = 1 si l'ombre part vers la droite
    (Soleil à gauche), -1 vers la gauche (Soleil à droite)."""
    fid = _filtre_ombre(S, alpha)
    return g(dessin, filter=f"url(#{fid})", transform=f"matrix(0 {n(aplati)} {n(-cote * longueur)} 0 {n(x)} {n(y)})")


def ombre_sous(x, y, rx, alpha=0.3):
    """Petite ombre ronde juste sous les pieds (Soleil au zénith)."""
    return ellipse(x, y, rx, rx * 0.22, "#1b1f3b", opacity=alpha)


def ombre_mur(S, dessin, x, y, echelle=1.6, alpha=0.4, flou=3):
    """Ombre projetée sur un mur : le même dessin, agrandi et assombri ; (x, y) = pieds de l'ombre."""
    fid = _filtre_ombre(S, alpha, flou=flou)
    return g(dessin, filter=f"url(#{fid})", transform=f"translate({n(x)} {n(y)}) scale({n(echelle)})")


def lignes_dipole(cx, cy, demi, angle=0, nb=14, r0=None, pas=4, limite=(0, 0, 800, 800), max_pas=1500):
    """Lignes de champ d'un aimant droit, calculées comme celles de deux pôles
    ponctuels : +1 (nord) en (cx + demi, cy) et -1 (sud) en (cx - demi, cy),
    le tout tourné de `angle` degrés. Chaque ligne est tracée depuis le pôle
    nord jusqu'au plan médian, puis complétée par symétrie jusqu'au pôle sud.
    Renvoie des listes de points orientées du nord vers le sud."""
    r0 = r0 or demi * 0.25
    x0, y0, x1, y1 = limite
    marge = max(x1 - x0, y1 - y0)
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    lignes = []
    for k in range(nb):
        # calcul dans le repère de l'aimant : nord en (demi, 0), sud en (-demi, 0)
        t = 2 * math.pi * (k + 0.5) / nb
        x, y = demi + r0 * math.cos(t), r0 * math.sin(t)
        pts = [(x, y)]
        for _ in range(max_pas):
            ex = ey = 0.0
            for px, q in ((demi, 1), (-demi, -1)):
                dx, dy = x - px, y
                d3 = (dx * dx + dy * dy) ** 1.5 or 1e-9
                ex += q * dx / d3
                ey += q * dy / d3
            e = math.hypot(ex, ey) or 1e-9
            nx, ny = x + pas * ex / e, y + pas * ey / e
            if nx <= 0:
                f = x / (x - nx)
                pts.append((0.0, y + (ny - y) * f))
                break
            x, y = nx, ny
            pts.append((x, y))
            if math.hypot(x, y) > marge:
                break
        complet = pts + [(-px, py) for px, py in reversed(pts)] if pts[-1][0] <= 1e-6 else pts
        lignes.append([(cx + px * ca - py * sa, cy + px * sa + py * ca) for px, py in complet])
        if pts[-1][0] > 1e-6:
            miroir = [(-px, py) for px, py in reversed(pts)]
            lignes.append([(cx + px * ca - py * sa, cy + px * sa + py * ca) for px, py in miroir])
    return lignes


def trace(pts, couleur=ENCRE, sw=3, **a):
    d = "M " + " L ".join(f"{n(x)} {n(y)}" for x, y in pts)
    return chemin(d, stroke=couleur, sw=sw, **a)


def direction_champ(ligne, i):
    """Angle (degrés, 0 = vers la droite) de la ligne de champ au point i, dans le sens N → S."""
    i = max(1, min(len(ligne) - 1, i))
    (xa, ya), (xb, yb) = ligne[i - 1], ligne[i]
    return math.degrees(math.atan2(yb - ya, xb - xa))


# ---------------------------------------------------------------------------
# Son
# ---------------------------------------------------------------------------

def ondes(x, y, r0=40, nb=3, ecart=34, direction=0, ouverture=70, couleur="#fa5252", sw=5, opacity=0.85, cercles=False):
    """Ondes sonores : arcs concentriques centrés en (x, y), dirigés vers `direction`
    (degrés, 0 = droite). cercles=True dessine des cercles complets."""
    m = []
    for k in range(nb):
        r = r0 + k * ecart
        op = opacity * (1 - k / (nb + 1))
        if cercles:
            m.append(cercle(x, y, r, "none", stroke=couleur, stroke_width=sw, opacity=op))
            continue
        a0, a1 = math.radians(direction - ouverture / 2), math.radians(direction + ouverture / 2)
        d = f"M {n(x + r * math.cos(a0))} {n(y + r * math.sin(a0))} A {n(r)} {n(r)} 0 0 1 {n(x + r * math.cos(a1))} {n(y + r * math.sin(a1))}"
        m.append(chemin(d, stroke=couleur, sw=sw, opacity=op))
    return g(m)


def sinus(x, y, longueur, amplitude, periode, couleur=ENCRE, sw=5, **a):
    """Courbe sinusoïdale de (x, y) vers la droite ; montre une onde (grave = grande période)."""
    pts = [(x + t, y - amplitude * math.sin(2 * math.pi * t / periode)) for t in range(0, int(longueur) + 1, 3)]
    return trace(pts, couleur, sw, **a)


def cheval(x, y, s=1.0, couleur="#8d5524", flip=False):
    """Petit cheval au galop, de profil (tête à droite) ; (x, y) = au sol."""
    m = [ellipse(0, -70, 60, 26, couleur),
         chemin("M 40 -80 Q 60 -120 80 -128 L 96 -118 Q 90 -100 70 -90 Z", couleur),
         ellipse(92, -118, 18, 11, couleur, rot=30),
         chemin("M 50 -100 Q 58 -128 76 -134", stroke=assombrir(couleur, 0.6), sw=8),
         chemin("M -58 -78 Q -90 -70 -94 -40", stroke=assombrir(couleur, 0.6), sw=9),
         cercle(90, -124, 3, ENCRE)]
    for x0, x1 in [(-40, -70), (-30, -10), (30, 60), (40, 20)]:
        m.append(trait(x0, -56, x1, -4, couleur, 9))
    return place(m, x, y, s, flip=flip)


def astronaute(x=0, y=0, s=1.0, peau="doree", cheveux="brun", coiffure="courts", expr="content", bras="bas",
               flip=False, regard=(0, 0), objet=None, drapeau=None):
    """Astronaute en combinaison blanche, casque transparent ; (x, y) = sous les pieds."""
    sac = rect(-58, -128, 116, 96, "#ced4da", rx=14)
    corps = personne(0, 0, 1.0, peau=peau, cheveux=cheveux, coiffure=coiffure, habit="#f8f9fa", jambes="#e9ecef",
                     robe=False, expr=expr, bras=bras, regard=regard, chaussures="#868e96", derriere=sac, objet=objet,
                     ceinture="#adb5bd")
    m = [corps,
         rect(-20, -96, 40, 26, "#4dabf7", rx=4), cercle(-8, -83, 4, "#fa5252"), cercle(8, -83, 4, "#51cf66"),
         cercle(0, -150, 72, "#d0ebff", opacity=0.3), cercle(0, -150, 72, "none", stroke="#adb5bd", stroke_width=6),
         chemin("M -40 -196 Q -10 -214 22 -206", stroke="#fff", sw=8, opacity=0.7),
         rect(-44, -84, 88, 12, "#adb5bd", rx=6)]
    return place(m, x, y, s, flip=flip)


# ---------------------------------------------------------------------------
# Espace
# ---------------------------------------------------------------------------

def fusee(x, y, s=1.0, rot=0, flamme=True, passager=None, couleur="#e03131"):
    """Fusée rouge et blanche ; (x, y) = centre du corps. `passager` = dessin (visage) dans le hublot."""
    m = []
    if flamme:
        m += [chemin("M -34 110 Q 0 260 34 110 Z", "#ff922b"), chemin("M -20 110 Q 0 200 20 110 Z", "#ffe066")]
    m += [chemin("M -60 60 L -110 130 L -50 120 Z", couleur), chemin("M 60 60 L 110 130 L 50 120 Z", couleur),
          chemin("M 0 -170 Q 70 -90 60 60 L 50 120 L -50 120 L -60 60 Q -70 -90 0 -170 Z", "#f8f9fa"),
          chemin("M 0 -170 Q 40 -130 50 -90 L -50 -90 Q -40 -130 0 -170 Z", couleur),
          rect(-44, 100, 88, 20, "#adb5bd", rx=6), trait(0, 60, 0, 130, couleur, 12),
          cercle(0, -20, 40, "#adb5bd"), cercle(0, -20, 32, "#a5d8ff")]
    if passager:
        cid = uid("h")
        m.append(el("clipPath", cercle(0, -20, 32, "#000"), id=cid))
        m.append(g(passager, clip_path=f"url(#{cid})"))
    m.append(chemin("M -18 -40 Q -8 -48 4 -46", stroke="#fff", sw=5, opacity=0.8))
    return place(m, x, y, s, rot=rot)


def planete(S, x, y, r, couleurs, bandes=None, lumiere=180, ombre_op=0.5, anneaux=None, tache=None, calottes=False, crateres=0, graine=1):
    """Planète éclairée par le Soleil venant de `lumiere` (degrés, 180 = de la gauche).

    couleurs : (fond, détail) ; bandes : liste de (y relatif -1..1, épaisseur relative, couleur) ;
    anneaux : (inclinaison en degrés, couleur) ; tache : (x, y, rx, ry, couleur) relatifs au rayon."""
    fond_, detail = couleurs
    cid = uid("p")
    m = []
    avant = []
    if anneaux:
        inc, ca = anneaux[:2]
        fins = len(anneaux) > 2 and anneaux[2]
        if fins:
            arr = [ellipse(0, 0, r * 1.7, r * 0.34, "none", stroke=ca, stroke_width=r * 0.04, opacity=0.8),
                   ellipse(0, 0, r * 1.85, r * 0.37, "none", stroke=ca, stroke_width=r * 0.025, opacity=0.6)]
        else:
            arr = [ellipse(0, 0, r * 2.1, r * 0.5, "none", stroke=ca, stroke_width=r * 0.34, opacity=0.9),
                   ellipse(0, 0, r * 1.78, r * 0.42, "none", stroke="#0b1433", stroke_width=r * 0.05, opacity=0.6)]
        # moitié arrière des anneaux derrière la planète, moitié avant devant
        cid_a = uid("q")
        S.defs.append(el("clipPath", rect(-r * 3, -r * 3, r * 6, r * 3, "#000"), id=cid_a))
        cid_b = uid("q")
        S.defs.append(el("clipPath", rect(-r * 3, 0, r * 6, r * 3, "#000"), id=cid_b))
        m.append(place(g(arr, clip_path=f"url(#{cid_a})"), 0, 0, rot=inc))
        avant.append(place(g(arr, clip_path=f"url(#{cid_b})"), 0, 0, rot=inc))
    m.append(el("clipPath", cercle(0, 0, r, "#000"), id=cid))
    corps = [cercle(0, 0, r, fond_)]
    if bandes:
        for by, ep, c in bandes:
            corps.append(ellipse(0, by * r, r * 1.1, ep * r, c))
    if tache:
        tx, ty, trx, tryy, tc = tache
        corps.append(ellipse(tx * r, ty * r, trx * r, tryy * r, tc))
    if calottes:
        corps += [ellipse(0, -r * 0.95, r * 0.45, r * 0.16, "#fff"), ellipse(0, r * 0.97, r * 0.35, r * 0.12, "#f8f9fa")]
    rr = random.Random(graine)
    for _ in range(crateres):
        cx, cy, cr = rr.uniform(-0.7, 0.7) * r, rr.uniform(-0.7, 0.7) * r, rr.uniform(0.06, 0.16) * r
        corps.append(cercle(cx, cy, cr, detail, opacity=0.7))
    if ombre_op:
        gid = uid("o")
        S.defs.append(el("linearGradient", el("stop", offset="0", stop_color="#000", stop_opacity="0") + el("stop", offset="0.45", stop_color="#000", stop_opacity=n(ombre_op * 0.6))
                         + el("stop", offset="1", stop_color="#000", stop_opacity=n(ombre_op * 1.3)), id=gid, x1=0, y1=0, x2=1, y2=0))
        corps.append(g(rect(-r * 0.25, -r - 2, r * 1.25 + 2, 2 * r + 4, f"url(#{gid})"), transform=f"rotate({n(lumiere + 180)})"))
    corps.append(cercle(-r * 0.35, -r * 0.35, r * 0.5, "#fff", opacity=0.08))
    m.append(g(corps, clip_path=f"url(#{cid})"))
    m += avant
    return place(m, x, y)
