"""Objets et accessoires réutilisables (gâteau, vélo, parapluie, etc.)."""
import math
import random

from base import (ENCRE, cercle, chemin, ellipse, el, g, place, poly, rect, texte, trait,
                  _assombrir, eclaircir, uid, n)


def bol(x, y, s=1.0, couleur="#74c0fc", contenu="#fff3bf", cuillere=True):
    """Saladier vu de face ; (x, y) = dessous."""
    m = [ellipse(0, -60, 70, 14, contenu)]
    if cuillere:
        m.append(g([trait(10, -60, 50, -130, "#c68642", 8), ellipse(8, -58, 12, 7, "#c68642")]))
    m += [chemin("M -72 -62 Q -70 0 0 0 Q 70 0 72 -62 Z", couleur),
          chemin("M -50 -40 Q -30 -20 -10 -18", stroke="#fff", sw=5, opacity=0.5)]
    return place(m, x, y, s)


def gateau(x, y, s=1.0, couleur="#f8c291", glacage="#fff0f6", fruits="#5c7cfa", bougies=0, part=False, assiette=True, fumee=False):
    """Gâteau rond vu de face ; (x, y) = dessous de l'assiette."""
    m = []
    if assiette:
        m.append(ellipse(0, -6, 110, 18, "#fff", stroke="#dee2e6", stroke_width=3))
    m.append(rect(-85, -86, 170, 76, couleur, rx=10))
    m.append(ellipse(0, -10, 85, 14, couleur))
    m.append(ellipse(0, -86, 85, 16, glacage))
    goutte_d = "".join(f"M {-80 + k * 32} -84 q 8 0 8 10 q 0 14 -8 14 q -8 0 -8 -14 q 0 -10 8 -10 Z" for k in range(6))
    m.append(chemin(goutte_d, glacage))
    m.append(rect(-85, -88, 170, 10, glacage))
    if fruits:
        for fx, fy in [(-50, -90), (-15, -96), (20, -90), (52, -94), (0, -82), (-34, -80), (38, -80)]:
            m.append(cercle(fx, fy, 7, fruits))
            m.append(cercle(fx - 2, fy - 2, 2, "#fff", opacity=0.6))
    for k in range(bougies):
        bx = -40 + k * 80 / max(1, bougies - 1) if bougies > 1 else 0
        m += [rect(bx - 4, -130, 8, 36, "#74c0fc", rx=3), ellipse(bx, -140, 6, 10, "#ffd43b"), ellipse(bx, -138, 3, 5, "#ff922b")]
    if part:
        m.append(poly([(0, -86), (85, -86), (85, -10)], "#fff", opacity=0))
    if fumee:
        for k in range(3):
            xx = -40 + k * 40
            m.append(chemin(f"M {xx} -110 q -14 -20 0 -40 q 14 -20 0 -40", stroke="#fff", sw=6, opacity=0.8))
    return place(m, x, y, s)


def part_gateau(x, y, s=1.0, couleur="#f8c291", glacage="#fff0f6", fruits="#5c7cfa"):
    m = [ellipse(0, 0, 42, 10, "#fff", stroke="#dee2e6", stroke_width=2),
         poly([(-26, -4), (26, -4), (30, -36), (-20, -40)], couleur),
         poly([(-20, -40), (30, -36), (22, -46), (-26, -48)], glacage),
         cercle(4, -44, 5, fruits)]
    return place(m, x, y, s)


def four(x, y, s=1.0, couleur="#e9ecef", allume=True, gateau_dedans=True, ouvert=False):
    """Cuisinière ; (x, y) = milieu du bas."""
    m = [rect(-120, -260, 240, 260, couleur, rx=14, stroke="#ced4da", stroke_width=4),
         rect(-120, -260, 240, 50, "#ced4da", rx=14)]
    for k in range(4):
        m.append(cercle(-75 + k * 50, -235, 12, "#868e96"))
    if not ouvert:
        m.append(rect(-95, -190, 190, 150, "#495057", rx=12))
        vitre = "#ffa94d" if allume else "#343a40"
        m.append(rect(-80, -175, 160, 110, vitre, rx=8, opacity=0.9))
        if allume:
            m.append(rect(-80, -175, 160, 110, "#ffe066", rx=8, opacity=0.3))
        if gateau_dedans:
            m.append(gateau(0, -80, 0.62, assiette=False, fruits=None, glacage="#e8a36c", couleur="#e8a36c"))
        m.append(rect(-60, -208, 120, 12, "#adb5bd", rx=6))
    else:
        m.append(rect(-95, -190, 190, 150, "#343a40", rx=12))
        m.append(poly([(-95, -40), (95, -40), (130, 10), (-130, 10)], "#495057"))
    return place(m, x, y, s)


def gants_four(x, y, s=1.0, couleur="#ff6b6b"):
    return place([ellipse(0, 0, 22, 16, couleur), ellipse(-14, -10, 8, 12, couleur, rot=-30)], x, y, s)


def assiette(x, y, s=1.0, couleur="#fff", bord="#74c0fc"):
    return place([ellipse(0, 0, 40, 11, bord), ellipse(0, -1, 32, 8, couleur)], x, y, s)


def tasse(x, y, s=1.0, couleur="#ff8787"):
    return place([rect(-18, -34, 36, 34, couleur, rx=6), chemin("M 18 -26 q 16 0 16 12 q 0 10 -16 10", stroke=couleur, sw=6)], x, y, s)


def velo(x, y, s=1.0, couleur="#fa5252", flip=False, tombe=False, roues_mvt=False):
    """Vélo de profil tourné vers la droite ; (x, y) = sol, au milieu."""
    r = 44
    m = []
    for wx in (-72, 72):
        m.append(cercle(wx, -r, r, "none", stroke=ENCRE, stroke_width=9))
        m.append(cercle(wx, -r, r - 8, "none", stroke="#adb5bd", stroke_width=2))
        for k in range(6):
            a = math.radians(k * 30 + (15 if roues_mvt else 0))
            m.append(trait(wx - math.cos(a) * (r - 6), -r - math.sin(a) * (r - 6), wx + math.cos(a) * (r - 6), -r + math.sin(a) * (r - 6), "#adb5bd", 1.5))
        m.append(cercle(wx, -r, 6, "#868e96"))
    bb = (-4, -r)
    selle = (-30, -118)
    guidon = (52, -130)
    m.append(chemin(f"M -72 {-r} L {bb[0]} {bb[1]} L {selle[0] + 4} {selle[1] + 10} Z", stroke=couleur, sw=10))
    m.append(chemin(f"M {bb[0]} {bb[1]} L {guidon[0] - 8} {guidon[1] + 30} L {selle[0] + 4} {selle[1] + 10}", stroke=couleur, sw=10))
    m.append(trait(guidon[0] - 8, guidon[1] + 30, 72, -r, couleur, 9))
    m.append(trait(guidon[0] - 8, guidon[1] + 30, guidon[0], guidon[1], "#495057", 7))
    m.append(trait(guidon[0] - 14, guidon[1], guidon[0] + 16, guidon[1] - 4, "#495057", 8))
    m.append(ellipse(selle[0], selle[1], 22, 7, "#343a40"))
    m.append(cercle(bb[0], bb[1], 10, "#868e96"))
    m.append(trait(bb[0], bb[1], bb[0] + 14, bb[1] + 20, "#495057", 5))
    m.append(rect(bb[0] + 6, bb[1] + 18, 20, 7, "#343a40", rx=3))
    if roues_mvt:
        for k in range(3):
            m.append(trait(-140, -30 - k * 22, -180 + k * 10, -30 - k * 22, ENCRE, 4, opacity=0.4))
    return place(m, x, y, s, flip=flip, rot=(-22 if tombe else 0))


def parapluie(x, y, s=1.0, couleur="#ffd43b", couleur2="#fab005", ouvert=True, rot=0):
    """Parapluie ; (x, y) = milieu du bord de la toile, le manche descend de 150."""
    m = [trait(0, -95, 0, 140, "#495057", 5),
         chemin("M 0 140 q 0 18 -14 18 q -12 0 -12 -12", stroke="#495057", sw=6)]
    R = 125
    bord = "".join(f" Q {n(-R + (k + 0.5) * 2 * R / 5)} {-18} {n(-R + (k + 1) * 2 * R / 5)} 0" for k in range(5))
    m.append(chemin(f"M {-R} 0 Q {-R} {-100} 0 {-100} Q {R} {-100} {R} 0{bord} Z", couleur))
    for k in (-1, 1):
        m.append(chemin(f"M 0 -100 Q {k * 40} -60 {k * 50} -6", stroke=couleur2, sw=4))
    m.append(chemin("M 0 -100 L 0 -10", stroke=couleur2, sw=4))
    m.append(cercle(0, -104, 7, "#495057"))
    return place(m, x, y, s, rot=rot)


def grande_feuille(x, y, s=1.0, couleur="#40c057", nervure="#2f9e44", rot=0):
    """Grande feuille à tenir comme un parapluie ; (x, y) = bout de la tige."""
    m = [trait(0, 0, 0, -120, "#2f9e44", 10),
         chemin("M 0 -110 C -220 -120 -230 -300 0 -330 C 230 -300 220 -120 0 -110 Z", couleur),
         trait(0, -110, 0, -320, nervure, 6)]
    for k in range(5):
        yy = -140 - k * 38
        m.append(chemin(f"M 0 {yy} Q -60 {yy - 10} -120 {yy - 40}", stroke=nervure, sw=4))
        m.append(chemin(f"M 0 {yy} Q 60 {yy - 10} 120 {yy - 40}", stroke=nervure, sw=4))
    return place(m, x, y, s, rot=rot)


def flaque(x, y, s=1.0, couleur="#74c0fc", eclabousse=False):
    m = [ellipse(0, 0, 90, 18, couleur), ellipse(-20, -3, 40, 6, "#a5d8ff")]
    if eclabousse:
        for k in range(7):
            a = math.radians(200 + k * 23)
            m.append(goutte_simple(math.cos(a) * 80, -10 + math.sin(a) * 60, couleur))
    return place(m, x, y, s)


def goutte_simple(x, y, couleur="#74c0fc", s=1.0):
    return place(chemin("M 0 -12 Q 9 0 6 6 Q 0 12 -6 6 Q -9 0 0 -12 Z", couleur), x, y, s)


def arc_en_ciel(x, y, r=300, ep=24):
    cols = ["#ff6b6b", "#ffa94d", "#ffd43b", "#69db7c", "#4dabf7", "#9775fa"]
    m = []
    for k, c in enumerate(cols):
        rr = r - k * ep
        m.append(chemin(f"M {x - rr} {y} A {rr} {rr} 0 0 1 {x + rr} {y}", stroke=c, sw=ep + 1))
    return g(m, stroke_linecap="butt")


def ballon_jeu(x, y, r=30, couleur="#fa5252", couleur2="#fff"):
    m = [cercle(x, y, r, couleur),
         chemin(f"M {x - r} {y} Q {x} {y - r * 0.5} {x + r} {y}", stroke=couleur2, sw=r * 0.2),
         chemin(f"M {x} {y - r} Q {x + r * 0.5} {y} {x} {y + r}", stroke=couleur2, sw=r * 0.2),
         cercle(x - r * 0.4, y - r * 0.4, r * 0.15, "#fff", opacity=0.6)]
    return g(m)


def pot_fleurs(x, y, s=1.0, couleur="#e8590c", etat="entier", fleurs=("#ff6b6b", "#ffd43b", "#cc5de8")):
    """Pot de fleurs ; etat = entier | casse | repare. (x, y) = dessous."""
    fonce = _assombrir(couleur, 0.85)
    if etat == "casse":
        m = [ellipse(0, 0, 130, 14, "#8d5524", opacity=0.3),
             poly([(-90, 0), (-70, -50), (-40, -44), (-50, 0)], couleur),
             poly([(-30, 0), (-20, -40), (20, -60), (30, -8)], couleur),
             poly([(40, 0), (60, -36), (100, -20), (90, 0)], fonce),
             poly([(-120, -2), (-110, -24), (-96, -4)], fonce),
             poly([(110, -2), (124, -16), (130, 0)], couleur),
             ellipse(0, -6, 60, 10, "#6b4226")]
        for k, c in enumerate(fleurs):
            m.append(g([trait(-40 + k * 50, -6, -70 + k * 60, -30, "#40c057", 5),
                        cercle(-70 + k * 60, -34, 14, c), cercle(-70 + k * 60, -34, 6, "#fff3bf")]))
        return place(m, x, y, s)
    m = []
    for k, c in enumerate(fleurs):
        fx = -40 + k * 40
        m.append(trait(fx * 0.5, -120, fx, -210 + (k % 2) * 20, "#40c057", 6))
        m.append(ellipse(fx * 0.7 + 12, -165, 14, 6, "#51cf66", rot=-30))
        for p in range(6):
            a = p * math.pi / 3
            m.append(cercle(fx + math.cos(a) * 14, -210 + (k % 2) * 20 + math.sin(a) * 14, 12, c))
        m.append(cercle(fx, -210 + (k % 2) * 20, 9, "#fff3bf"))
    m += [poly([(-70, -130), (70, -130), (52, 0), (-52, 0)], couleur),
          rect(-80, -140, 160, 30, fonce, rx=6),
          chemin("M -40 -100 L -34 -20", stroke="#fff", sw=6, opacity=0.25)]
    if etat == "repare":
        or_ = "#fcc419"
        m += [chemin("M -76 -128 L -40 -90 L -52 -40 L -20 -8", stroke=or_, sw=5),
              chemin("M 30 -136 L 20 -100 L 50 -70 L 40 -30 L 58 -6", stroke=or_, sw=5),
              chemin("M -40 -90 L 20 -100", stroke=or_, sw=5),
              chemin("M -52 -40 L 0 -60 L 40 -30", stroke=or_, sw=5)]
    return place(m, x, y, s)


def sac_cailloux(x, y, s=1.0):
    m = [chemin("M -60 0 Q -80 -90 -30 -110 L 30 -110 Q 80 -90 60 0 Z", "#a47148"),
         chemin("M -30 -110 Q 0 -130 30 -110", stroke="#6b4226", sw=8)]
    for cx, cy, r in [(-20, -120, 16), (10, -126, 18), (34, -116, 12)]:
        m.append(cercle(cx, cy, r, "#868e96"))
    return place(m, x, y, s)


def lampe_poche(x, y, s=1.0, rot=0, faisceau=0, couleur="#4dabf7"):
    """Lampe de poche pointée vers la droite ; faisceau = longueur du rayon."""
    m = []
    if faisceau:
        L = faisceau
        m.append(poly([(28, -12), (L, -L * 0.35), (L, L * 0.35), (28, 12)], "#fff3bf", opacity=0.55))
    m += [rect(-40, -10, 60, 20, couleur, rx=6), rect(14, -15, 18, 30, _assombrir(couleur, 0.8), rx=4),
          rect(30, -13, 5, 26, "#fff3bf"), rect(-20, -14, 10, 5, "#fa5252", rx=2)]
    return place(m, x, y, s, rot=rot)


def plante(x, y, s=1.0, pot="#e8590c", couleur="#2f9e44"):
    m = []
    for k, (ex, ey, rt) in enumerate([(-50, -150, -40), (40, -170, 35), (-10, -200, 5), (-70, -100, -65), (70, -110, 65)]):
        m.append(trait(0, -80, ex * 0.6, ey * 0.8, couleur, 5))
        m.append(ellipse(ex, ey, 18, 48, couleur if k % 2 else "#37b24d", rot=rt))
    m += [poly([(-40, -80), (40, -80), (30, 0), (-30, 0)], pot), rect(-46, -88, 92, 16, _assombrir(pot, 0.85), rx=4)]
    return place(m, x, y, s)


def robe_chambre(x, y, s=1.0, couleur="#9775fa"):
    """Robe de chambre suspendue à un crochet ; (x, y) = crochet."""
    m = [cercle(0, 0, 6, "#868e96"),
         chemin("M -40 10 Q 0 -4 40 10 L 70 60 L 50 70 L 46 200 L -46 200 L -50 70 L -70 60 Z", couleur),
         chemin("M -40 10 Q 0 50 40 10", stroke=_assombrir(couleur, 0.8), sw=6),
         trait(-44, 110, 44, 110, _assombrir(couleur, 0.8), 8),
         trait(-60, 60, -80, 170, couleur, 26), trait(60, 60, 80, 170, couleur, 26)]
    return place(m, x, y, s)


def monstre_ombre(x, y, s=1.0, couleur="#1b1f3b", yeux=True):
    """Silhouette inquiétante (qui n'est qu'une robe de chambre)."""
    m = [chemin("M -50 0 Q -60 -60 -30 -90 Q 0 -110 30 -90 Q 60 -60 50 0 L 60 200 L -60 200 Z", couleur),
         chemin("M -45 30 Q -110 80 -100 190", stroke=couleur, sw=30),
         chemin("M 45 30 Q 110 80 100 190", stroke=couleur, sw=30)]
    if yeux:
        m += [ellipse(-18, -45, 10, 6, "#ffe066"), ellipse(18, -45, 10, 6, "#ffe066")]
    return place(m, x, y, s)


def tour_cubes(x, y, s=1.0, n_=6, graine=1, penche=0, couleurs=("#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8", "#ff922b")):
    """Tour de cubes ; (x, y) = base au sol."""
    r = random.Random(graine)
    m = []
    for k in range(n_):
        c = couleurs[k % len(couleurs)]
        dx = r.uniform(-6, 6) + penche * k * k * 0.8
        m.append(g([rect(dx - 34, -(k + 1) * 64, 68, 64, c, rx=6, stroke=_assombrir(c, 0.8), stroke_width=3),
                    texte(dx, -(k + 1) * 64 + 44, "ABCDEFGHIJ"[k % 10], 34, "#fff")]))
    return place(m, x, y, s)


def cube(x, y, s=1.0, couleur="#ff6b6b", lettre="A", rot=0):
    m = [rect(-32, -32, 64, 64, couleur, rx=6, stroke=_assombrir(couleur, 0.8), stroke_width=3),
         texte(0, 12, lettre, 34, "#fff")]
    return place(m, x, y, s, rot=rot)


def nuage_orage(x, y, s=1.0):
    from base import nuage
    m = [nuage(0, 0, 1.0, "#495057", ombre="#343a40"),
         poly([(0, 40), (-20, 90), (4, 88), (-12, 140), (30, 76), (6, 78), (20, 40)], "#ffd43b")]
    return place(m, x, y, s)


def bougie(x, y, s=1.0, flamme=True, couleur="#74c0fc"):
    m = [rect(-12, -70, 24, 70, couleur, rx=4), trait(0, -70, 0, -80, ENCRE, 3)]
    if flamme:
        m += [ellipse(0, -96, 10, 18, "#ffd43b"), ellipse(0, -92, 5, 9, "#ff922b")]
    return place(m, x, y, s)


def corde_sauter(x1, y1, x2, y2, bas=60, couleur="#fa5252"):
    mx = (x1 + x2) / 2
    return g([chemin(f"M {x1} {y1} Q {mx} {max(y1, y2) + bas} {x2} {y2}", stroke=couleur, sw=5),
              rect(x1 - 5, y1 - 14, 10, 28, "#fab005", rx=4), rect(x2 - 5, y2 - 14, 10, 28, "#fab005", rx=4)])


def pansement(x, y, s=1.0, rot=0):
    return place([rect(-18, -7, 36, 14, "#ffd8a8", rx=6), rect(-6, -6, 12, 12, "#ffe8cc"),
                  cercle(-3, -2, 1, "#e8590c"), cercle(3, 2, 1, "#e8590c")], x, y, s, rot=rot)


def barriere(x, y, s=1.0, couleur="#c68642", largeur=300):
    m = []
    for k in range(4):
        px = -largeur / 2 + k * largeur / 3
        m.append(rect(px - 10, -110, 20, 110, couleur, rx=4))
        m.append(poly([(px - 10, -110), (px, -126), (px + 10, -110)], couleur))
    m += [rect(-largeur / 2 - 10, -86, largeur + 20, 16, _assombrir(couleur, 0.9), rx=4),
          rect(-largeur / 2 - 10, -44, largeur + 20, 16, _assombrir(couleur, 0.9), rx=4)]
    return place(m, x, y, s)


def carton(x, y, s=1.0, w=200, h=140, couleur="#d9a066", ouvert=True, rot=0, dessin=""):
    """Boîte en carton vue de face ; (x, y) = milieu du bas."""
    fonce = _assombrir(couleur, 0.85)
    m = []
    if ouvert:
        m.append(poly([(-w / 2, -h), (-w / 2 - 40, -h - 50), (-w / 2 + 20, -h - 40), (-w / 2 + 30, -h)], fonce))
        m.append(poly([(w / 2, -h), (w / 2 + 40, -h - 50), (w / 2 - 20, -h - 40), (w / 2 - 30, -h)], fonce))
    m.append(rect(-w / 2, -h, w, h, couleur))
    m.append(rect(-w / 2, -h, w, 12, fonce))
    if dessin:
        m.append(dessin)
    m.append(rect(-w * 0.15, -h, w * 0.3, 30, "#e9c38c", opacity=0.6) if not ouvert else "")
    return place(m, x, y, s, rot=rot)


def araignee(x, y, s=1.0):
    m = []
    for sgn in (-1, 1):
        for k in range(4):
            m.append(chemin(f"M 0 0 Q {sgn * 30} {-20 + k * 10} {sgn * 40} {10 + k * 8}", stroke=ENCRE, sw=3))
    m += [cercle(0, 0, 16, ENCRE), cercle(-5, -4, 4, "#fff"), cercle(5, -4, 4, "#fff"),
          cercle(-5, -3, 2, ENCRE), cercle(5, -3, 2, ENCRE),
          chemin("M -5 6 Q 0 10 5 6", stroke="#fff", sw=2), trait(0, -16, 0, -200, "#adb5bd", 1.5)]
    return place(m, x, y, s)


def coccinelle(x, y, s=1.0, rot=0):
    m = [cercle(0, -16, 9, ENCRE), ellipse(0, 4, 18, 20, "#fa5252"), trait(0, -14, 0, 24, ENCRE, 2.5)]
    for px, py in [(-8, -2), (8, -2), (-9, 12), (9, 12), (0, -8)]:
        m.append(cercle(px, py, 3.5, ENCRE))
    m += [cercle(-4, -18, 2, "#fff"), cercle(4, -18, 2, "#fff")]
    return place(m, x, y, s, rot=rot)


def papillon(x, y, s=1.0, couleur="#cc5de8", couleur2="#ffd43b", rot=0):
    m = [ellipse(-18, -12, 18, 22, couleur, rot=-20), ellipse(18, -12, 18, 22, couleur, rot=20),
         ellipse(-14, 14, 12, 14, couleur2, rot=20), ellipse(14, 14, 12, 14, couleur2, rot=-20),
         ellipse(0, 0, 4, 22, ENCRE), trait(0, -20, -8, -34, ENCRE, 2), trait(0, -20, 8, -34, ENCRE, 2)]
    return place(m, x, y, s, rot=rot)


def scarabee(x, y, s=1.0, rot=0, couleur="#20c997"):
    m = []
    for k in range(3):
        m.append(trait(-16, -8 + k * 10, -30, -14 + k * 12, ENCRE, 3))
        m.append(trait(16, -8 + k * 10, 30, -14 + k * 12, ENCRE, 3))
    m += [cercle(0, -22, 9, ENCRE), ellipse(0, 2, 18, 22, couleur), trait(0, -18, 0, 24, _assombrir(couleur, 0.7), 2),
          cercle(-4, -24, 2.5, "#fff"), cercle(4, -24, 2.5, "#fff")]
    return place(m, x, y, s, rot=rot)


def toile(x, y, r=110, perles=True):
    m = []
    for k in range(8):
        a = math.radians(k * 45)
        m.append(trait(x, y, x + math.cos(a) * r, y + math.sin(a) * r, "#dee2e6", 2))
    for rr in (r * 0.3, r * 0.55, r * 0.8):
        pts = " ".join(f"{n(x + math.cos(math.radians(k * 45)) * rr)},{n(y + math.sin(math.radians(k * 45)) * rr)}" for k in range(9))
        m.append(el("polyline", points=pts, fill="none", stroke="#dee2e6", stroke_width=2))
    if perles:
        rnd = random.Random(4)
        for _ in range(16):
            a = math.radians(rnd.choice(range(0, 360, 45)))
            rr = rnd.uniform(0.25, 0.85) * r
            m.append(cercle(x + math.cos(a) * rr, y + math.sin(a) * rr, rnd.uniform(3, 6), "#d0ebff", stroke="#fff", stroke_width=1.5))
    return g(m)


def bocal(x, y, s=1.0, eau="#a5d8ff", contenu=""):
    """Bocal rond ; (x, y) = dessous."""
    m = [ellipse(0, 4, 90, 12, "#000", opacity=0.08),
         chemin("M -50 -210 Q -110 -170 -100 -90 Q -90 0 0 0 Q 90 0 100 -90 Q 110 -170 50 -210 Z", "#e7f5ff", opacity=0.6),
         chemin("M -94 -150 Q -110 -90 -96 -60 Q -80 0 0 0 Q 80 0 96 -60 Q 110 -90 94 -150 Z", eau, opacity=0.85),
         ellipse(0, -150, 94, 12, eclaircir(eau, 0.4)),
         chemin("M -40 -12 Q -20 -30 0 -12 Q 20 -30 40 -12 Z", "#ffd43b", opacity=0.6),
         contenu,
         chemin("M -50 -210 Q -110 -170 -100 -90 Q -90 0 0 0 Q 90 0 100 -90 Q 110 -170 50 -210", stroke="#a5d8ff", sw=5),
         ellipse(0, -210, 50, 8, "none", stroke="#a5d8ff", stroke_width=5),
         chemin("M -72 -150 Q -84 -110 -70 -70", stroke="#fff", sw=7, opacity=0.7)]
    return place(m, x, y, s)


def chaussette(x, y, s=1.0, couleur="#4dabf7", rot=0):
    m = [chemin("M -10 -40 L 10 -40 L 12 0 Q 30 4 30 14 Q 30 24 12 22 L -8 22 Q -12 10 -10 -40 Z", couleur),
         rect(-12, -44, 24, 10, "#fff", rx=3)]
    return place(m, x, y, s, rot=rot)


def camion(x, y, s=1.0, couleur="#fab005"):
    m = [rect(-60, -50, 80, 40, couleur, rx=6), rect(20, -60, 40, 50, "#fa5252", rx=6),
         rect(30, -52, 22, 18, "#a5d8ff", rx=3),
         cercle(-35, -8, 12, ENCRE), cercle(38, -8, 12, ENCRE), cercle(-35, -8, 5, "#adb5bd"), cercle(38, -8, 5, "#adb5bd")]
    return place(m, x, y, s)


def pomme(x, y, s=1.0, couleur="#fa5252"):
    return place([cercle(-7, 0, 16, couleur), cercle(7, 0, 16, couleur), trait(0, -14, 3, -26, "#8d5524", 3),
                  ellipse(10, -22, 8, 4, "#51cf66", rot=-20)], x, y, s)


def pinceau(x, y, s=1.0, couleur="#4dabf7", rot=30):
    m = [rect(-4, -80, 8, 70, "#c68642", rx=3), rect(-5, -12, 10, 12, "#adb5bd"),
         chemin("M -5 0 Q 0 26 5 0 Z", couleur)]
    return place(m, x, y, s, rot=rot)


def pot_peinture(x, y, s=1.0, couleur="#4dabf7", renverse=False):
    if renverse:
        m = [chemin("M -60 0 Q -80 -20 -40 -26 Q 0 -40 40 -20 Q 90 -10 70 6 Q 0 20 -60 0 Z", couleur),
             place([rect(-26, -50, 52, 50, "#fff", rx=6, stroke="#ced4da", stroke_width=3), rect(-26, -50, 52, 12, couleur)], -70, -10, 1, rot=-80)]
        return place(m, x, y, s)
    m = [rect(-26, -50, 52, 50, "#fff", rx=6, stroke="#ced4da", stroke_width=3), ellipse(0, -48, 24, 6, couleur)]
    return place(m, x, y, s)


def ballon_air(x, y, s=1.0, couleur="#fa5252", fil=160, fil_courbe=20):
    """Ballon de baudruche ; (x, y) = bas du fil."""
    m = [chemin(f"M 0 0 Q {fil_courbe} {-fil / 2} 0 {-fil}", stroke="#495057", sw=2),
         poly([(-6, -fil + 6), (6, -fil + 6), (0, -fil - 4)], _assombrir(couleur, 0.85)),
         ellipse(0, -fil - 58, 48, 58, couleur),
         ellipse(-18, -fil - 80, 10, 18, "#fff", opacity=0.45, rot=-20)]
    return place(m, x, y, s)


def montagnes(S_or_none, y, couleurs=("#b197fc", "#9775fa"), neige=True):
    m = []
    for k, (cx, h, w) in enumerate([(150, 260, 220), (430, 330, 260), (680, 240, 200)]):
        c = couleurs[k % len(couleurs)]
        m.append(poly([(cx - w, y), (cx, y - h), (cx + w, y)], c))
        if neige:
            m.append(poly([(cx - w * 0.28, y - h * 0.72), (cx, y - h), (cx + w * 0.28, y - h * 0.72), (cx + w * 0.1, y - h * 0.66), (cx, y - h * 0.74), (cx - w * 0.12, y - h * 0.65)], "#fff"))
    return g(m)


def aigle(x, y, s=1.0, flip=False):
    m = [chemin("M -120 -10 Q -60 -60 -10 -10 Q 60 -60 120 -10 Q 60 -30 10 10 Q -60 -30 -120 -10 Z", "#8d5524"),
         cercle(18, -6, 16, "#fff"), cercle(22, -8, 3.5, ENCRE), poly([(30, -8), (46, -2), (30, 2)], "#fab005")]
    return place(m, x, y, s, flip=flip)
