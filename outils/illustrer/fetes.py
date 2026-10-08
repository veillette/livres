"""Objets des livres de fêtes : lanternes, guirlandes, cadeaux, confettis,
feux d'artifice, œufs décorés, citrouilles creusées, cerfs-volants…

Chaque livre du rayon « Fêtes » a son propre script dans `histoires/` ; ce
module ne réunit que les accessoires de fête qu'ils partagent. (x, y) est le
point d'appui de l'objet (sa base), sauf mention contraire.
"""

import math
import random

from base import (rect, cercle, ellipse, chemin, trait, poly, g, place, n, texte,
                  etoile5, coeur, lueur, lineaire, radial, volume, cylindre, eclaircir,
                  _assombrir)


# --- Lumières -------------------------------------------------------------------

def lanterne(x, y, s=1.0, allumee=True, couleur="#495057", verre="#ffe066"):
    """Lanterne tenue par son anneau ; (x, y) = l'anneau (la main qui la
    porte). Le halo se pose à part, avec S.lumiere(), sur le verre (y + 52 s)."""
    m = [chemin("M -14 18 Q -14 0 0 0 Q 14 0 14 18", stroke=couleur, sw=5),
         poly([(-26, 18), (26, 18), (20, 30), (-20, 30)], couleur),
         rect(-21, 30, 42, 50, radial([(0, "#fffbe6"), (0.6, verre), (1, "#fab005")]) if allumee else "#adb5bd", rx=5),
         trait(-21, 30, -21, 80, couleur, 5), trait(21, 30, 21, 80, couleur, 5), trait(0, 30, 0, 80, couleur, 3),
         rect(-27, 78, 54, 10, couleur, rx=3)]
    if allumee:
        m.insert(0, cercle(0, 54, 46, "#ffe066", opacity=0.25))
        m.append(ellipse(-6, 58, 6, 11, "#ff922b"))
    return place(m, x, y, s)


def guirlande_lumineuse(x0, y0, x1, y1, creux=50, nb=9, allumee=True, graine=1,
                        couleurs=("#ff6b6b", "#ffd43b", "#69db7c", "#4dabf7", "#f783ac")):
    """Fil tendu de (x0, y0) à (x1, y1), qui pend de `creux`, avec ses ampoules."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + creux * 2
    m = [chemin(f"M {n(x0)} {n(y0)} Q {n(mx)} {n(my)} {n(x1)} {n(y1)}", stroke="#2b8a3e", sw=3)]
    for k in range(nb):
        t = (k + 0.5) / nb
        px = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t * t * x1
        py = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t * t * y1
        c = couleurs[(k + graine) % len(couleurs)]
        if allumee:
            m.append(cercle(px, py + 10, 15, c, opacity=0.3))
        m.append(rect(px - 3, py, 6, 5, "#495057"))
        m.append(ellipse(px, py + 11, 5.5, 8, c if allumee else _assombrir(c, 0.6)))
        if allumee:
            m.append(ellipse(px - 1.5, py + 8, 1.8, 3, "#fff", opacity=0.8))
    return g(m)


def guirlande_fanions(x0, y0, x1, y1, creux=40, nb=9, graine=0,
                      couleurs=("#ff6b6b", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8", "#ff922b")):
    """Fanions triangulaires sur une corde."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + creux * 2
    m = [chemin(f"M {n(x0)} {n(y0)} Q {n(mx)} {n(my)} {n(x1)} {n(y1)}", stroke="#495057", sw=3)]
    for k in range(nb):
        t = (k + 0.5) / nb
        px = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t * t * x1
        py = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t * t * y1
        m.append(poly([(px - 17, py - 2), (px + 17, py - 2), (px, py + 40)], couleurs[(k + graine) % len(couleurs)]))
    return g(m)


def bougie_flamme(x, y, s=1.0, couleur="#74c0fc", allumee=True):
    """Bougie fine de gâteau ; (x, y) = pied."""
    m = [rect(-4, -40, 8, 40, couleur, rx=2),
         chemin("M -4 -30 L 4 -36 M -4 -18 L 4 -24 M -4 -6 L 4 -12", stroke="#fff", sw=2, opacity=0.7)]
    if allumee:
        m += [cercle(0, -56, 16, "#ffe066", opacity=0.3), ellipse(0, -54, 6, 11, "#ffd43b"), ellipse(0, -51, 3, 6, "#ff922b")]
    return place(m, x, y, s)


# --- Noël --------------------------------------------------------------------------

def boule_noel(x, y, r=14, couleur="#fa5252"):
    """Boule de Noël suspendue ; (x, y) = son crochet."""
    return g([rect(x - r * 0.3, y, r * 0.6, r * 0.35, "#ced4da"),
              cercle(x, y + r * 1.3, r, volume(couleur, 0.45, 0.7)),
              ellipse(x - r * 0.35, y + r * 0.95, r * 0.22, r * 0.32, "#fff", opacity=0.7)])


def sapin_decore(x, y, s=1.0, etoile=None, lumieres=True, graine=2):
    """Grand sapin d'intérieur décoré (boules, guirlande), sans pot ; (x, y) =
    pied. etoile : dessin posé au sommet (repère : le sommet en (0, 0)), ou None."""
    from base import sapin
    r = random.Random(graine)
    m = [sapin(0, 0, 1.0)]
    # guirlande en spirale
    for yy, w in ((-70, 72), (-140, 52), (-205, 34)):
        m.append(chemin(f"M {-w} {yy} Q 0 {yy + 26} {w} {yy - 18}", stroke="#ffd43b", sw=4))
    cols = ("#fa5252", "#4dabf7", "#ffd43b", "#cc5de8", "#fa5252", "#ff922b")
    for k, (bx, by) in enumerate(((-58, -62), (40, -80), (-20, -110), (30, -150), (-34, -170), (12, -215), (60, -50), (-70, -45))):
        m.append(boule_noel(bx, by - 8, 9, cols[k % len(cols)]))
    if lumieres:
        for k in range(14):
            px, py = r.uniform(-60, 60), r.uniform(-230, -50)
            if abs(px) < 75 * (py + 280) / 240:
                m.append(cercle(px, py, 5, "#fff3bf"))
                m.append(cercle(px, py, 10, "#ffe066", opacity=0.3))
    if etoile:
        m.append(place(etoile, 0, -282))
    return place(m, x, y, s)


def etoile_papier(x, y, s=1.0, rot=0, brille=True):
    """Étoile faite de morceaux de papier de toutes les couleurs, bordée d'un fil
    doré ; (x, y) = centre."""
    pts = []
    for k in range(10):
        a = math.radians(-90 + k * 36)
        rr = 60 if k % 2 == 0 else 26
        pts.append((rr * math.cos(a), rr * math.sin(a)))
    cols = ("#ff6b6b", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8")
    m = []
    if brille:
        m.append(cercle(0, 0, 95, radial([(0, "#fff3bf", 0.9), (1, "#fff3bf", 0)])))
    for k in range(5):
        a, b, c = pts[2 * k], pts[(2 * k + 1) % 10], pts[(2 * k - 1) % 10]
        m.append(poly([(0, 0), c, a, b], cols[k]))
    m.append(poly(pts, "none", stroke="#f59f00", stroke_width=5, stroke_linejoin="round"))
    m.append(cercle(0, 0, 8, "#fff3bf"))
    return place(m, x, y, s, rot=rot)


def grande_etoile(x, y, r=26, halo=True):
    """L'étoile la plus brillante du ciel, avec ses rayons ; (x, y) = centre."""
    m = []
    if halo:
        m.append(cercle(x, y, r * 4, radial([(0, "#fff9db", 0.75), (0.35, "#ffe066", 0.25), (1, "#ffe066", 0)])))
    for a in range(0, 180, 45):
        L = r * (3.2 if a % 90 == 0 else 2)
        t = math.radians(a)
        m.append(trait(x - L * math.cos(t), y - L * math.sin(t), x + L * math.cos(t), y + L * math.sin(t), "#fff9db", 3 if a % 90 == 0 else 2, opacity=0.8))
    m.append(etoile5(x, y, r, "#fff3bf"))
    m.append(etoile5(x, y, r * 0.5, "#ffffff"))
    return g(m)


def cadeau(x, y, s=1.0, couleur="#fa5252", ruban="#ffd43b", w=120, h=90, rot=0):
    """Paquet cadeau ; (x, y) = milieu du bas."""
    m = [rect(-w / 2, -h, w, h, volume(couleur, 0.3, 0.75), rx=6),
         rect(-w / 2 - 6, -h - 4, w + 12, 24, _assombrir(couleur, 0.88), rx=5),
         rect(-10, -h - 4, 20, h + 4, ruban),
         ellipse(-18, -h - 12, 18, 11, "none", stroke=ruban, stroke_width=7, rot=25),
         ellipse(18, -h - 12, 18, 11, "none", stroke=ruban, stroke_width=7, rot=-25),
         cercle(0, -h - 6, 7, ruban)]
    return place(m, x, y, s, rot=rot)


def traineau(x, y, s=1.0, buches=True, couleur="#c92a2a"):
    """Traîneau en bois chargé de bûches ; (x, y) = milieu des patins, la
    corde part à droite (vers 150, -60)."""
    m = [chemin("M -130 0 L 120 0 Q 160 0 160 -34", stroke="#868e96", sw=7),
         rect(-110, -20, 10, 22, "#868e96"), rect(80, -20, 10, 22, "#868e96"),
         rect(-125, -52, 240, 34, cylindre(couleur, 0.3, 0.7, vertical=True), rx=6)]
    if buches:
        for k, (bx, by) in enumerate(((-80, -70), (-20, -70), (40, -70), (-50, -100), (10, -100))):
            m.append(ellipse(bx, by, 32, 16, "#8d5524"))
            m.append(ellipse(bx + 28, by, 8, 15, "#e9b98a"))
            m.append(ellipse(bx + 28, by, 4, 8, "#c68642"))
    return place(m, x, y, s)


def traces_neige(points, s=1.0):
    """Empreintes de petits pas dans la neige le long d'une suite de points."""
    m = []
    for k, (px, py) in enumerate(points):
        d = 7 * s if k % 2 else -7 * s
        m.append(ellipse(px + d, py, 6 * s, 3.5 * s, "#a5b4fc", opacity=0.55))
    return g(m)


# --- Pâques -------------------------------------------------------------------------

def oeuf_decore(x, y, s=1.0, couleur="#ff8787", motif="zigzag", c2="#ffffff", rot=0):
    """Œuf de Pâques peint ; (x, y) = point d'appui (bas de l'œuf)."""
    m = [ellipse(0, -30, 23, 30, volume(couleur, 0.4, 0.75))]
    if motif == "zigzag":
        m.append(chemin("M -22 -30 L -14 -38 L -6 -30 L 2 -38 L 10 -30 L 18 -38 L 22 -32", stroke=c2, sw=4))
    elif motif == "pois":
        m += [cercle(-9, -40, 4, c2), cercle(8, -28, 4, c2), cercle(-6, -16, 3.5, c2), cercle(10, -48, 3, c2)]
    elif motif == "rayures":
        m += [chemin("M -21 -40 Q 0 -34 21 -40", stroke=c2, sw=4), chemin("M -22 -22 Q 0 -16 22 -22", stroke=c2, sw=4)]
    elif motif == "coeur":
        m.append(coeur(0, -30, 0.32, c2))
    m.append(ellipse(-8, -42, 5, 9, "#fff", opacity=0.45))
    return place(m, x, y, s, rot=rot)


def gros_oeuf_chocolat(x, y, s=1.0, ouvert=False, ruban="#e64980"):
    """Gros œuf en chocolat noué d'un ruban ; ouvert : coupé en deux, plein de
    petites fritures, cloches et lapins en chocolat. (x, y) = base."""
    choco = "#7c4a1e"
    if not ouvert:
        m = [ellipse(0, -80, 62, 80, volume(choco, 0.35, 0.7)),
             rect(-62, -92, 124, 16, ruban), rect(-8, -160, 16, 160, ruban, opacity=0.0),
             ellipse(-16, -88, 18, 10, "none", stroke=ruban, stroke_width=6, rot=20),
             ellipse(16, -88, 18, 10, "none", stroke=ruban, stroke_width=6, rot=-20),
             ellipse(-24, -120, 10, 22, "#fff", opacity=0.25)]
        return place(m, x, y, s)
    m = [chemin("M -70 -60 Q -70 0 0 0 Q 70 0 70 -60 L 50 -50 L 30 -64 L 10 -50 L -10 -64 L -30 -50 L -50 -64 Z",
                volume(choco, 0.3, 0.7))]
    # petites fritures (poissons), cloches et lapins
    for k, (px, py, rot) in enumerate(((-40, -72, -20), (-10, -82, 10), (24, -76, -10), (46, -66, 25))):
        m.append(place([ellipse(0, 0, 14, 7, "#a0693a"), poly([(12, 0), (22, -7), (22, 7)], "#a0693a"),
                        cercle(-7, -1, 1.6, "#3b2312")], px, py, 1.0, rot=rot))
    m.append(place([chemin("M -12 6 Q -12 -16 0 -16 Q 12 -16 12 6 Z", "#c68642"), cercle(0, 8, 3, "#c68642")], -24, -92, 1.0))
    m.append(place([ellipse(0, 0, 9, 11, "#8d5524"), ellipse(-4, -16, 3, 9, "#8d5524"), ellipse(4, -16, 3, 9, "#8d5524")], 10, -100, 1.0))
    # demi-coque posée à côté
    m.append(chemin("M 90 -4 Q 90 -60 150 -60 Q 150 -4 90 -4 Z", volume(choco, 0.35, 0.7)))
    return place(m, x, y, s)


def cloche(x, y, s=1.0, couleur="#fcc419", rot=0, ailes=True, ruban="#e64980"):
    """Cloche de Pâques volante, avec ruban et petites ailes ; (x, y) = centre."""
    m = []
    if ailes:
        m += [chemin("M -26 -20 Q -70 -50 -78 -16 Q -60 -20 -50 -6 Q -40 -16 -26 -8 Z", "#ffffff", stroke="#dee2e6", sw=2),
              chemin("M 26 -20 Q 70 -50 78 -16 Q 60 -20 50 -6 Q 40 -16 26 -8 Z", "#ffffff", stroke="#dee2e6", sw=2)]
    m += [chemin("M -30 18 Q -30 -40 0 -40 Q 30 -40 30 18 Q 36 22 36 26 L -36 26 Q -36 22 -30 18 Z", volume(couleur, 0.4, 0.7)),
          cercle(0, 30, 8, _assombrir(couleur, 0.7)),
          chemin("M -18 -42 Q 0 -60 18 -42", stroke=ruban, sw=6),
          ellipse(-10, -12, 5, 14, "#fff", opacity=0.4)]
    return place(m, x, y, s, rot=rot)


def panier_osier(x, y, s=1.0, oeufs=(), couleur="#c68642"):
    """Panier en osier avec anse ; oeufs : couleurs des œufs qui dépassent.
    (x, y) = milieu du fond."""
    fonce = _assombrir(couleur, 0.75)
    m = [chemin("M -58 -50 Q -58 -130 0 -130 Q 58 -130 58 -50", stroke=fonce, sw=9)]
    for k, c in enumerate(oeufs):
        px = -36 + k * (72 / max(1, len(oeufs) - 1)) if len(oeufs) > 1 else 0
        m.append(oeuf_decore(px, -42 - (k % 2) * 6, 0.85, c, ("zigzag", "pois", "rayures", "coeur")[k % 4]))
    m += [chemin("M -64 -54 L 64 -54 L 52 0 L -52 0 Z", volume(couleur, 0.3, 0.75)),
          chemin("M -62 -40 L 62 -40 M -59 -26 L 59 -26 M -56 -12 L 56 -12", stroke=fonce, sw=3, opacity=0.6),
          rect(-68, -60, 136, 10, fonce, rx=5)]
    return place(m, x, y, s)


# --- Halloween ---------------------------------------------------------------------

def citrouille_creusee(x, y, s=1.0, allumee=True, visage=True, couleur="#fd7e14"):
    """Citrouille creusée d'un grand sourire, éclairée de l'intérieur ;
    (x, y) = base. Le halo se pose à part (S.lumiere, centre y - 55 s)."""
    fonce = _assombrir(couleur, 0.8)
    m = [rect(-7, -122, 14, 26, "#2f9e44", rx=5),
         ellipse(-42, -55, 46, 54, volume(fonce, 0.3, 0.7)), ellipse(42, -55, 46, 54, volume(fonce, 0.3, 0.7)),
         ellipse(0, -56, 50, 58, volume(couleur, 0.35, 0.75))]
    if visage:
        dedans = "#ffd43b" if allumee else "#5c2b0a"
        m += [poly([(-38, -78), (-12, -78), (-25, -56)], dedans), poly([(12, -78), (38, -78), (25, -56)], dedans),
              poly([(-6, -50), (6, -50), (0, -40)], dedans),
              chemin("M -40 -34 Q 0 -4 40 -34 L 30 -28 L 22 -20 L 14 -24 L 6 -16 L -6 -16 L -14 -24 L -22 -20 L -30 -28 Z", dedans)]
    return place(m, x, y, s)


def citrouille_anse(x, y, s=1.0, allumee=True):
    """Citrouille-lanterne portée par une anse ; (x, y) = le haut de l'anse (la
    main). Le halo se pose à part, au centre de la citrouille (y + 92 s)."""
    m = [chemin("M -40 52 Q -40 0 0 0 Q 40 0 40 52", stroke="#495057", sw=5),
         citrouille_creusee(0, 150, 1.0, allumee=allumee)]
    return place(m, x, y, s)


def seau_bonbons(x, y, s=1.0, couleur="#fd7e14", plein=True):
    """Petit seau d'Halloween ; (x, y) = l'anse (la main qui le porte)."""
    m = [chemin("M -26 40 Q -26 0 0 0 Q 26 0 26 40", stroke="#495057", sw=4)]
    if plein:
        for k, c in enumerate(("#f06595", "#74c0fc", "#ffd43b", "#69db7c", "#cc5de8")):
            m.append(cercle(-22 + k * 11, 38 - (k % 2) * 6, 8, c))
    m += [chemin("M -32 40 L 32 40 L 26 88 L -26 88 Z", volume(couleur, 0.3, 0.75)),
          poly([(-14, 52), (-4, 52), (-9, 60)], "#2b2b3a"), poly([(4, 52), (14, 52), (9, 60)], "#2b2b3a"),
          chemin("M -14 70 Q 0 80 14 70", stroke="#2b2b3a", sw=3)]
    return place(m, x, y, s)


def bonbon(x, y, s=1.0, couleur="#f06595", rot=0):
    """Bonbon emballé ; (x, y) = centre."""
    return place([poly([(-12, 0), (-24, -9), (-24, 9)], eclaircir(couleur, 0.3)), poly([(12, 0), (24, -9), (24, 9)], eclaircir(couleur, 0.3)),
                  ellipse(0, 0, 14, 10, couleur), chemin("M -6 -8 Q 0 0 -6 8", stroke="#fff", sw=2, opacity=0.6)], x, y, s, rot=rot)


def chauve_souris_papier(x, y, s=1.0, rot=0, couleur="#343a40"):
    """Chauve-souris en papier découpé (décoration) ; (x, y) = centre."""
    m = [chemin("M 0 -6 Q -20 -24 -52 -14 Q -44 -6 -46 6 Q -34 0 -28 10 Q -18 2 -8 10 Z", couleur),
         chemin("M 0 -6 Q 20 -24 52 -14 Q 44 -6 46 6 Q 34 0 28 10 Q 18 2 8 10 Z", couleur),
         ellipse(0, 0, 10, 13, couleur), poly([(-8, -10), (-5, -20), (-1, -11)], couleur), poly([(8, -10), (5, -20), (1, -11)], couleur),
         cercle(-4, -2, 2, "#ffd43b"), cercle(4, -2, 2, "#ffd43b")]
    return place(m, x, y, s, rot=rot)


def ailes_chauve_souris(couleur="#5f3dc4"):
    """Ailes de costume, dans le repère d'un personnage (à passer en derriere=)."""
    return g([chemin("M -20 -120 Q -90 -170 -150 -120 Q -130 -100 -134 -76 Q -110 -88 -96 -66 Q -76 -84 -54 -62 Q -40 -90 -20 -86 Z", couleur),
              chemin("M 20 -120 Q 90 -170 150 -120 Q 130 -100 134 -76 Q 110 -88 96 -66 Q 76 -84 54 -62 Q 40 -90 20 -86 Z", couleur)])


def chapeau_sorciere(couleur="#2b2b3a", ruban="#7950f2"):
    """Chapeau pointu de costume, posé sur la tête d'un perso animal (repère local)."""
    return g([ellipse(0, -205, 78, 15, couleur), poly([(-44, -208), (14, -330), (44, -208)], couleur),
              rect(-44, -226, 88, 16, ruban), etoile5(-2, -260, 9, "#ffd43b")])


def drap_fantome(x, y, s=1.0, expr="ouh", couleur="#f8f9fa"):
    """Fantôme de drap (quelqu'un de déguisé), avec des pieds qui dépassent ;
    (x, y) = sol."""
    m = [rect(-30, -14, 22, 14, "#5c3d2e", rx=6), rect(10, -14, 22, 14, "#5c3d2e", rx=6),
         chemin("M -80 -10 Q -90 -200 0 -250 Q 90 -200 80 -10 L 56 -24 L 32 -6 L 8 -24 L -16 -6 L -40 -24 L -60 -6 Z",
                volume(couleur, 0.25, 0.85)),
         ellipse(-26, -170, 12, 18, "#2b2b3a"), ellipse(26, -170, 12, 18, "#2b2b3a")]
    if expr == "ouh":
        m.append(ellipse(0, -120, 14, 18, "#2b2b3a"))
    else:
        m.append(chemin("M -22 -128 Q 0 -104 22 -128", stroke="#2b2b3a", sw=6))
    m.append(chemin("M -40 -200 Q -20 -230 10 -238", stroke="#fff", sw=6, opacity=0.6))
    from base import occuper
    m.append(occuper(-85, -255, 85, 0))
    return place(m, x, y, s)


# --- Nouvel An, carnaval, anniversaire ---------------------------------------------

def confettis(x0, y0, x1, y1, nb=40, graine=1,
              couleurs=("#ff6b6b", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8", "#ff922b", "#f783ac")):
    """Confettis répandus dans un rectangle."""
    r = random.Random(graine)
    m = []
    for k in range(nb):
        px, py = r.uniform(x0, x1), r.uniform(y0, y1)
        c = couleurs[k % len(couleurs)]
        if k % 3 == 0:
            m.append(cercle(px, py, r.uniform(4, 6), c))
        else:
            m.append(rect(px - 5, py - 3, 10, 6, c, transform=f"rotate({r.randint(0, 180)} {n(px)} {n(py)})"))
    return g(m)


def serpentin(x, y, s=1.0, couleur="#f783ac", rot=0, longueur=160):
    """Serpentin qui ondule ; (x, y) = départ."""
    d = f"M 0 0 " + " ".join(f"Q {n(longueur * (k + 0.5) / 4)} {(-1) ** k * 22} {n(longueur * (k + 1) / 4)} 0" for k in range(4))
    return place([chemin(d, stroke=couleur, sw=7)], x, y, s, rot=rot)


def feu_artifice(x, y, r=90, couleur="#ffd43b", couleur2="#ffffff", nb=14):
    """Bouquet de feu d'artifice ; (x, y) = centre de l'éclat."""
    m = [cercle(x, y, r * 1.1, radial([(0, couleur, 0.35), (1, couleur, 0)]))]
    for k in range(nb):
        a = 2 * math.pi * k / nb
        x1, y1 = x + math.cos(a) * r * 0.35, y + math.sin(a) * r * 0.35
        x2, y2 = x + math.cos(a) * r, y + math.sin(a) * r
        m.append(trait(x1, y1, x2, y2, couleur, 4))
        m.append(cercle(x2, y2, 5, couleur2))
    m.append(cercle(x, y, r * 0.14, couleur2))
    return g(m)


def chapeau_fete(couleur="#4dabf7", pois="#ffd43b", y=-205, x=0, rot=0):
    """Chapeau pointu de fête en carton, pour la tête d'un perso animal (repère local)."""
    m = [poly([(-34, 0), (0, -92), (34, 0)], volume(couleur, 0.3, 0.75)),
         cercle(0, -96, 11, pois), cercle(-12, -24, 5, pois), cercle(10, -48, 5, pois), cercle(-3, -70, 4, pois)]
    return place(m, x, y, 1.0, rot=rot)


def mirliton(x, y, s=1.0, rot=0, couleur="#cc5de8", deroule=True):
    """Langue de belle-mère : un tube qui se déroule ; (x, y) = embout."""
    m = [rect(0, -6, 26, 12, "#ffd43b", rx=4)]
    if deroule:
        m.append(rect(24, -9, 110, 18, couleur, rx=9))
        m.append(chemin("M 40 -9 V 9 M 60 -9 V 9 M 80 -9 V 9 M 100 -9 V 9", stroke="#fff", sw=3, opacity=0.6))
    else:
        m.append(cercle(36, 6, 14, couleur))
    return place(m, x, y, s, rot=rot)


def cerf_volant_losange(x, y, s=1.0, couleur="#e03131", couleur2="#ffd43b", rot=0, queue=None, fil_vers=None):
    """Cerf-volant en losange ; (x, y) = centre. queue : liste de (couleur,
    forme) accrochées en dessous (forme : "noeud", "chaussette", "cravate",
    "foulard") ; fil_vers : (x, y) de la main qui tient le fil, en
    coordonnées de la page."""
    m = []
    if fil_vers:
        m.append(chemin(f"M {n(x)} {n(y + 20 * s)} Q {n((x + fil_vers[0]) / 2)} {n(max(y, fil_vers[1]) + 40)} {n(fil_vers[0])} {n(fil_vers[1])}",
                        stroke="#495057", sw=2.5))
    c = [poly([(0, -110), (78, -10), (0, 120), (-78, -10)], volume(couleur, 0.3, 0.75)),
         poly([(0, -110), (78, -10), (0, -10)], couleur2), poly([(0, -10), (-78, -10), (0, 120)], couleur2),
         trait(0, -110, 0, 120, "#8d5524", 4), trait(-78, -10, 78, -10, "#8d5524", 4)]
    if queue:
        pas_ = 80
        d = "M 0 120 " + " ".join(f"Q {(-1) ** k * 34} {120 + pas_ * (k + 0.5)} 0 {120 + pas_ * (k + 1)}" for k in range(len(queue)))
        c.insert(0, chemin(d, stroke="#495057", sw=4))
        for k, (col, forme) in enumerate(queue):
            yy = 120 + pas_ * (k + 1)
            if forme == "chaussette":
                c.append(place([chemin("M -8 -20 L 8 -20 L 8 6 L 24 10 Q 30 20 20 24 L -6 20 Q -12 14 -8 4 Z", col),
                                trait(-8, -14, 8, -14, "#fff", 3), trait(-8, -6, 8, -6, "#fff", 3)], 0, yy, 1.9, rot=-10))
            elif forme == "cravate":
                c.append(place([poly([(-8, -22), (8, -22), (4, -14), (14, 26), (0, 38), (-14, 26), (-4, -14)], col),
                                cercle(0, 4, 3, "#fff"), cercle(-4, 18, 3, "#fff")], 0, yy, 1.7, rot=8))
            elif forme == "foulard":
                c.append(place([poly([(-24, -12), (24, -12), (0, 24)], col), cercle(-6, -4, 3, "#fff"), cercle(8, 2, 3, "#fff")], 0, yy, 1.6, rot=-6))
            else:
                c.append(place([poly([(0, 0), (-18, -10), (-18, 10)], col), poly([(0, 0), (18, -10), (18, 10)], col)], 0, yy, 1.4))
    m.append(place(c, x, y, s, rot=rot))
    return g(m)


def carte_coeur(x, y, s=1.0, couleur="#ffffff", coeur_c="#e64980", lignes=2, rot=0, ouverte=False):
    """Carte de vœux pliée avec un cœur ; (x, y) = centre."""
    m = [rect(-60, -46, 120, 92, couleur, rx=6, stroke="#dee2e6", stroke_width=3),
         coeur(-22 if lignes else 0, -4, 0.55, coeur_c)]
    for k in range(lignes):
        m.append(trait(4, -14 + k * 16, 46, -14 + k * 16, "#adb5bd", 4))
    if ouverte:
        m.insert(0, rect(-66, -42, 120, 92, "#f1f3f5", rx=6, transform="rotate(-6)"))
    return place(m, x, y, s, rot=rot)


def coeur_papier(x, y, s=1.0, couleur="#e64980", rot=0, ecrit=None):
    """Cœur découpé dans du papier, un peu de travers ; (x, y) = centre."""
    m = [coeur(0, 0, 1.0, couleur), chemin("M -30 -24 Q -22 -34 -10 -28", stroke="#fff", sw=4, opacity=0.5)]
    if ecrit:
        m.append(texte(0, 6, ecrit, 16, "#fff"))
    return place(m, x, y, s, rot=rot)


# --- Crêpes (Mardi gras, Chandeleur) -------------------------------------------------

def poele_crepe(x, y, s=1.0, en_lair=True):
    """Poêle tenue par le manche ; une crêpe qui saute. (x, y) = milieu de la poêle."""
    m = [ellipse(0, 0, 70, 18, "#343a40"), rect(60, -8, 120, 16, "#495057", rx=8)]
    if en_lair:
        m.append(ellipse(-10, -150, 56, 16, "#f6c453", rot=-12, stroke="#e8a200", stroke_width=3))
        m.append(chemin("M -40 -40 Q -60 -90 -40 -120 M 20 -40 Q 40 -90 20 -120", stroke="#495057", sw=3, opacity=0.4))
    return place(m, x, y, s)


def pile_crepes(x, y, s=1.0):
    """Pile de crêpes dorées sur une assiette ; (x, y) = base de l'assiette."""
    m = [ellipse(0, 0, 90, 22, "#fff", stroke="#dee2e6", stroke_width=3)]
    m += [ellipse(0, -8 - k * 9, 70, 16, "#f6c453", stroke="#e8a200", stroke_width=2) for k in range(6)]
    return place(m, x, y, s)


# --- Petit chien (vu de profil) ---------------------------------------------------

def chien_profil(x, y, s=1.0, couleur="#e3b57a", oreille="#a0693a", flip=False, gueule=None, queue_haute=True,
                 course=False, expr="content", collier="#e03131"):
    """Petit chien vu de profil, la tête à droite ; (x, y) = au sol, sous le
    ventre. gueule : dessin tenu dans la gueule (repère : la truffe en (0, 0)).
    course : pattes étirées au galop."""
    from base import occuper, oeil
    f = _assombrir(couleur, 0.8)
    m = []
    # queue
    m.append(chemin("M -62 -66 Q -96 -110 -84 -128" if queue_haute else "M -62 -60 Q -96 -50 -104 -30",
                    stroke=couleur, sw=12))
    # pattes
    if course:
        pattes = [(-46, -40, -86, -14), (-30, -40, -58, -4), (34, -40, 74, -12), (48, -40, 92, -24)]
    else:
        pattes = [(-46, -40, -50, 0), (-28, -40, -30, 0), (30, -40, 32, 0), (48, -40, 50, 0)]
    for k, (x0, y0, x1, y1) in enumerate(pattes):
        c = f if k in (0, 2) else couleur
        m.append(trait(x0, y0, x1, y1, c, 15))
        m.append(ellipse(x1 + 4, y1 - 2, 11, 6, c))
    # corps
    m.append(ellipse(0, -62, 66, 34, volume(couleur, 0.3, 0.78)))
    m.append(ellipse(10, -46, 40, 14, eclaircir(couleur, 0.4), opacity=0.6))
    # tête
    m.append(ellipse(64, -104, 36, 32, volume(couleur, 0.3, 0.78)))
    m.append(ellipse(98, -92, 22, 15, eclaircir(couleur, 0.35)))
    m.append(ellipse(116, -98, 8, 6, "#2b2b3a"))
    m.append(chemin("M 52 -126 Q 30 -120 36 -76 Q 50 -86 58 -110 Z", oreille))
    if expr == "content":
        m.append(chemin("M 98 -80 Q 106 -74 114 -82", stroke="#2b2b3a", sw=3))
        m.append(ellipse(106, -74, 6, 8, "#ff8787"))
    m.append(oeil(76, -112, "normal" if expr != "rire" else "heureux", (1, 0), taille=0.9))
    if collier:
        m.append(chemin("M 40 -84 Q 52 -70 70 -76", stroke=collier, sw=7))
    if gueule:
        m.append(place(gueule, 112, -82))
    m.append(occuper(-100, -140, 130, 0))
    return place(m, x, y, s, flip=flip)
