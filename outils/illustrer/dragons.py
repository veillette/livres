"""
Accessoires partagés des histoires de dragons : dragon habillé (chapeau,
couronne, lunettes, moustaches…), dragon couché qui dort, jets de feu, de
fumée, de brouillard et de givre, petite flamme, tas d'or, nid de paille,
grotte à porte ronde.

Le dragon lui-même est celui de `fantastique.dragon()` (tout rond, vu de
face, les pieds en (0, 0)) : sa bouche est en (0, -116), le haut de sa tête
vers (0, -204), ses cornes montent jusqu'à -236.
"""
from base import *
from base import _assombrir
from fantastique import dragon, dragon_vol, etincelles, OR, OR_FONCE

# bouche du dragon de face, dans son repère local
BOUCHE = (0, -116)

FEU = ("#e8590c", "#ff922b", "#ffd43b", "#fff3bf")
GIVRE = ("#74c0fc", "#a5d8ff", "#d0ebff", "#ffffff")


def bouche_dragon(x, y, s=1.0, flip=False):
    """Position de la bouche d'un dragon(x, y, s) dans la scène."""
    return x, y + BOUCHE[1] * s


# --- Dragons ------------------------------------------------------------------

def dragon_habille(x=0, y=0, s=1.0, chapeau=None, bande=None, couronne=None, lunettes=None,
                   moustaches=None, barbe=None, echarpe=None, noeud=None, cartable=None,
                   flip=False, rot=0, **k):
    """Un dragon de `fantastique.dragon()` avec ses accessoires (repère local).

    chapeau : couleur d'un chapeau pointu de magicien (bande : sa bande) ;
    couronne : couleur d'une couronne ; lunettes : couleur des montures ;
    moustaches : couleur de longues moustaches de dragon d'Orient ;
    barbe : couleur d'une barbichette ; echarpe : couleur d'une écharpe ;
    noeud : couleur d'un nœud sur la tête ; cartable : couleur d'un cartable
    sur le dos (les bretelles passent sur les épaules)."""
    m = []
    if cartable:
        f = _assombrir(cartable, 0.75)
        m.append(rect(-56, -128, 112, 84, volume(cartable, 0.3, 0.75), rx=16))
        m.append(rect(-56, -128, 112, 26, f, rx=12))
    m.append(dragon(0, 0, 1.0, **k))
    if cartable:
        m.append(chemin("M -40 -112 Q -36 -86 -42 -60 M 40 -112 Q 36 -86 42 -60", stroke=_assombrir(cartable, 0.65), sw=9))
    if echarpe:
        f = _assombrir(echarpe, 0.8)
        m += [chemin("M -46 -112 Q 0 -94 46 -112 L 44 -96 Q 0 -78 -44 -96 Z", volume(echarpe, 0.3, 0.75)),
              chemin("M 22 -98 L 30 -50 L 46 -54 L 38 -100 Z", f),
              chemin("M 30 -56 l 2 8 M 38 -58 l 2 8", stroke=f, sw=3)]
    if barbe:
        m.append(chemin("M -14 -106 Q 0 -96 14 -106 Q 10 -78 0 -66 Q -10 -78 -14 -106 Z", barbe))
    if moustaches:
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 18} -122 Q {sgn * 60} -126 {sgn * 74} -102 Q {sgn * 86} -80 {sgn * 104} -86",
                            stroke=moustaches, sw=5))
    if lunettes:
        for sgn in (-1, 1):
            m.append(cercle(sgn * 24, -164, 19, "#e7f5ff", opacity=0.35, stroke=lunettes, stroke_width=4))
        m.append(chemin("M -6 -166 Q 0 -172 6 -166", stroke=lunettes, sw=4))
    if noeud:
        f = _assombrir(noeud, 0.8)
        m += [poly([(30, -196), (6, -214), (8, -182)], noeud), poly([(30, -196), (56, -214), (52, -180)], noeud),
              cercle(30, -197, 7, f)]
    if couronne:
        f = _assombrir(couronne, 0.8)
        m += [poly([(-40, -196), (-46, -246), (-22, -222), (0, -258), (22, -222), (46, -246), (40, -196)], volume(couronne, 0.35, 0.75)),
              rect(-42, -206, 84, 14, f, rx=4),
              cercle(-46, -248, 6, couronne), cercle(0, -260, 7, couronne), cercle(46, -248, 6, couronne),
              cercle(0, -200, 5, "#e03131"), cercle(-24, -200, 4, "#4dabf7"), cercle(24, -200, 4, "#4dabf7")]
    if chapeau:
        bande = bande or _assombrir(chapeau, 0.7)
        m += [ellipse(0, -198, 82, 15, _assombrir(chapeau, 0.85)),
              chemin("M -48 -200 Q -30 -262 -4 -304 Q 18 -340 60 -332 Q 22 -316 28 -266 Q 34 -230 48 -200 Z",
                     volume(chapeau, 0.3, 0.75)),
              chemin("M -46 -210 Q 0 -222 46 -210 L 44 -198 Q 0 -210 -44 -198 Z", bande),
              etoile5(18, -256, 10, OR), etoile5(-12, -238, 6, OR)]
    return place(m, x, y, s, flip=flip, rot=rot)


def dragon_couche(x, y, s=1.0, couleur="#69db7c", ventre="#d8f5a2", flip=False, dort=True, expr=None):
    """Dragon couché en boule sur le côté, la tête posée sur les pattes, la
    queue autour du corps ; (x, y) = au sol, au milieu. Tête à droite."""
    fonce = _assombrir(couleur, 0.78)
    ys, bs, ss = EXPRESSIONS[expr or ("dort" if dort else "sourire")]
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(0, 0, 150, 12, 0.14))
    # queue qui fait le tour
    m.append(chemin("M -80 -20 Q -170 -10 -150 30 Q -130 40 -40 6 Q 40 -4 90 4", stroke=couleur, sw=26))
    m.append(poly([(86, -2), (124, -10), (106, 18)], fonce))
    # aile repliée et corps
    m.append(ellipse(-10, -62, 110, 62, volume(couleur, 0.3, 0.75)))
    m.append(ellipse(10, -34, 80, 26, ventre))
    m.append(chemin("M -70 -110 L -30 -150 L -10 -110 L 20 -146 L 40 -104", fonce))
    m.append(chemin("M -60 -78 Q -20 -140 40 -100 Q 10 -70 -60 -78 Z", fonce, opacity=0.9))
    # pattes devant
    m.append(ellipse(70, -12, 34, 14, fonce))
    m.append(ellipse(110, -12, 30, 13, fonce))
    # tête posée sur les pattes
    m.append(ellipse(110, -54, 58, 44, volume(couleur, 0.3, 0.75)))
    m.append(ellipse(146, -40, 30, 20, ventre))
    m.append(ellipse(150, -44, 3.5, 2.5, fonce) + ellipse(164, -42, 3.5, 2.5, fonce))
    for k, hx in enumerate((80, 100)):
        m.append(poly([(hx - 10, -92), (hx - 22, -126), (hx + 8, -96)], "#fff4e6", stroke="#e9d5b5", stroke_width=2))
    m.append(oeil(110, -62, ys, (1, 0), sclere=not dort))
    m.append(ellipse(128, -40, 9, 5.5, ROSE, opacity=0.7))
    m.append(bouche(136, -30, bs, 0.7))
    m.append(occuper(-170, -160, 180, 20))
    return place(m, x, y, s, flip=flip)


# --- Souffles -----------------------------------------------------------------

def _langue(x0, y0, x1, y1, ep, couleur, graine=1, opacite=1.0):
    """Jet en forme de langue de flamme, étroit en (x0, y0), large et
    festonné en (x1, y1)."""
    r = random.Random(graine)
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    pts = [(x0 + px * ep * 0.12, y0 + py * ep * 0.12)]
    for k in range(1, 6):
        t = k / 6
        w = ep * (0.15 + 0.85 * t ** 0.8) / 2 * (1 + r.uniform(-0.15, 0.15))
        pts.append((x0 + dx * t + px * w, y0 + dy * t + py * w))
    # bout festonné
    for k in range(5):
        a = math.pi / 2 - k * math.pi / 4
        w = ep / 2 * (0.7 + r.uniform(0, 0.45))
        ca, sa = math.cos(a), math.sin(a)
        pts.append((x1 + (ux * ca * 0.8 + px * sa) * w, y1 + (uy * ca * 0.8 + py * sa) * w))
    for k in range(5, 0, -1):
        t = k / 6
        w = ep * (0.15 + 0.85 * t ** 0.8) / 2 * (1 + r.uniform(-0.15, 0.15))
        pts.append((x0 + dx * t - px * w, y0 + dy * t - py * w))
    pts.append((x0 - px * ep * 0.12, y0 - py * ep * 0.12))
    d = "M " + " L ".join(f"{n(a)} {n(b)}" for a, b in pts) + " Z"
    return chemin(d, couleur, stroke=couleur, sw=ep * 0.12, opacity=opacite)


def jet_feu(x0, y0, x1, y1, ep=90, couleurs=FEU, graine=1):
    """Souffle de feu d'un dragon, de la bouche (x0, y0) jusqu'en (x1, y1)."""
    m = []
    for k, c in enumerate(couleurs):
        f = 1 - k * 0.22
        ex = x0 + (x1 - x0) * (1 - k * 0.12)
        ey = y0 + (y1 - y0) * (1 - k * 0.12)
        m.append(_langue(x0, y0, ex, ey, ep * f, c, graine + k))
    return g(m)


def jet_givre(x0, y0, x1, y1, ep=90, graine=1):
    """Souffle glacé : une langue bleu pâle semée de flocons."""
    m = [jet_feu(x0, y0, x1, y1, ep, GIVRE, graine)]
    r = random.Random(graine)
    for _ in range(7):
        t = r.uniform(0.3, 1.0)
        fx = x0 + (x1 - x0) * t + r.uniform(-1, 1) * ep * 0.4 * t
        fy = y0 + (y1 - y0) * t + r.uniform(-1, 1) * ep * 0.4 * t
        m.append(flocon_simple(fx, fy, r.uniform(0.5, 1.0)))
    return g(m)


def flocon_simple(x, y, s=1.0, couleur="#ffffff"):
    m = []
    for a in (0, 60, 120):
        m.append(place(trait(-14, 0, 14, 0, couleur, 3), 0, 0, 1.0, rot=a))
    return place(m, x, y, s)


def jet_fumee(x0, y0, x1, y1, ep=60, couleur="#adb5bd", graine=1, nb=6):
    """Petits nuages de fumée qui grossissent de (x0, y0) vers (x1, y1)."""
    r = random.Random(graine)
    m = []
    for k in range(nb):
        t = (k + 1) / nb
        cx = x0 + (x1 - x0) * t + r.uniform(-6, 6)
        cy = y0 + (y1 - y0) * t + r.uniform(-6, 6)
        rr = ep * (0.2 + 0.5 * t)
        m.append(cercle(cx, cy, rr, volume(couleur, 0.35, 0.8), opacity=0.9))
        m.append(cercle(cx - rr * 0.3, cy - rr * 0.3, rr * 0.35, "#ffffff", opacity=0.35))
    return g(m)


def rond_fumee(x, y, s=1.0, couleur="#adb5bd"):
    """Rond de fumée."""
    return place([ellipse(0, 0, 34, 24, "none", stroke=couleur, stroke_width=12, opacity=0.85),
                  ellipse(-6, -6, 30, 20, "none", stroke="#ffffff", stroke_width=3, opacity=0.4)], x, y, s)


def brouillard(x, y, s=1.0, graine=1, nb=9, couleur="#e7f5ff", opacite=0.75):
    """Banc de brouillard : boules pâles qui se chevauchent ; (x, y) = centre."""
    r = random.Random(graine)
    m = []
    for _ in range(nb):
        m.append(ellipse(r.uniform(-130, 130), r.uniform(-40, 40), r.uniform(50, 90), r.uniform(30, 50),
                         couleur, opacity=opacite * r.uniform(0.6, 1.0)))
    return place(m, x, y, s)


def flammeche(x, y, s=1.0, couleurs=FEU[1:], rot=0):
    """Petite flamme en goutte (bougie, mèche, flamme d'un tout petit dragon) ;
    (x, y) = base de la flamme."""
    m = []
    for k, c in enumerate(couleurs):
        f = 1 - k * 0.3
        m.append(chemin(f"M 0 {-60 * f} Q {16 * f} {-28 * f} {14 * f} {-10 * f} Q {12 * f} 2 0 2 "
                        f"Q {-12 * f} 2 {-14 * f} {-10 * f} Q {-16 * f} {-28 * f} 0 {-60 * f} Z", c))
    return place(m, x, y, s, rot=rot)


# --- Objets et décors ---------------------------------------------------------

def tas_or(x, y, s=1.0, w=220, h=90, graine=1, couronne_=False):
    """Tas de pièces d'or ; (x, y) = milieu de la base."""
    r = random.Random(graine)
    m = [chemin(f"M {-w / 2} 0 Q {-w * 0.3} {-h} 0 {-h} Q {w * 0.3} {-h} {w / 2} 0 Z", volume(OR, 0.35, 0.72))]
    for _ in range(int(w * h / 500)):
        px = r.uniform(-w * 0.42, w * 0.42)
        haut = -h * (1 - (abs(px) / (w / 2)) ** 2) * 0.95
        py = r.uniform(haut + 6, -6)
        m.append(ellipse(px, py, 12, 5, "#ffe066", stroke=OR_FONCE, stroke_width=1.5))
    for k in range(4):
        m.append(etoile5(r.uniform(-w * 0.3, w * 0.3), r.uniform(-h * 0.8, -h * 0.3), 6, "#ffffff", opacity=0.9))
    if couronne_:
        m.append(place([poly([(-30, 0), (-34, -36), (-16, -18), (0, -44), (16, -18), (34, -36), (30, 0)], volume(OR, 0.4, 0.75)),
                        cercle(0, -8, 5, "#e03131")], w * 0.12, -h * 0.8, 0.9, rot=-12))
    return place(m, x, y, s)


def coffre(x, y, s=1.0, ouvert=True, couleur="#a0522d"):
    """Coffre au trésor plein d'or ; (x, y) = milieu de la base."""
    f = _assombrir(couleur, 0.7)
    m = []
    if ouvert:
        m.append(chemin("M -86 -96 Q -80 -170 0 -172 Q 80 -170 86 -96 Z", volume(couleur, 0.3, 0.75)))
        m.append(tas_or(0, -90, 0.75, w=200, h=60, graine=3))
    m += [rect(-90, -96, 180, 96, volume(couleur, 0.3, 0.75), rx=8),
          rect(-90, -96, 180, 14, f), rect(-60, -96, 14, 96, OR), rect(46, -96, 14, 96, OR),
          rect(-14, -70, 28, 30, OR, rx=4), cercle(0, -58, 5, f)]
    if not ouvert:
        m.insert(0, chemin("M -90 -96 Q -84 -150 0 -152 Q 84 -150 90 -96 Z", volume(couleur, 0.3, 0.75)))
    return place(m, x, y, s)


def nid_paille(x, y, s=1.0, couleur="#f6c453"):
    """Nid de paille rond ; (x, y) = milieu de la base."""
    f = _assombrir(couleur, 0.78)
    m = [ellipse(0, -30, 140, 40, volume(couleur, 0.3, 0.75)), ellipse(0, -44, 110, 22, _assombrir(couleur, 0.6))]
    r = random.Random(4)
    for _ in range(26):
        a = r.uniform(0, math.pi * 2)
        cx, cy = math.cos(a) * 120, -30 + math.sin(a) * 30
        m.append(chemin(f"M {n(cx - 22)} {n(cy + r.uniform(-6, 6))} Q {n(cx)} {n(cy - 10)} {n(cx + 24)} {n(cy + r.uniform(-6, 6))}",
                        stroke=f if r.random() < 0.5 else eclaircir(couleur, 0.3), sw=4))
    return place(m, x, y, s)


def porte_ronde(x, y, s=1.0, couleur="#2f9e44", ouverte=False, lumiere=False):
    """Porte ronde de grotte ; (x, y) = milieu du seuil."""
    f = _assombrir(couleur, 0.75)
    m = [chemin("M -76 0 L -76 -80 A 76 76 0 0 1 76 -80 L 76 0 Z", "#6d4424")]
    if ouverte:
        m.append(chemin("M -64 0 L -64 -80 A 64 64 0 0 1 64 -80 L 64 0 Z", "#ffd43b" if lumiere else "#343a40"))
        m.append(chemin("M -64 0 L -64 -80 A 64 64 0 0 1 -30 -136 L -30 0 Z", volume(couleur, 0.3, 0.75)))
    else:
        m.append(chemin("M -64 0 L -64 -80 A 64 64 0 0 1 64 -80 L 64 0 Z", volume(couleur, 0.3, 0.75)))
        for k in (-32, 0, 32):
            m.append(trait(k, -140 if k == 0 else -128, k, 0, f, 3))
        m.append(cercle(0, -76, 9, OR))
    return place(m, x, y, s)


def montagne_grotte(S, y_sol=640, roche="#d9cbbd", herbe="#8ce99a", porte="#2f9e44", ouverte=False, porte_x=430,
                    porte_s=1.2, fenetre_=True, lumiere=False, soir=False):
    """Flanc de montagne rocheux avec la maison-grotte des dragons : porte
    ronde, petite fenêtre ronde, cheminée de pierre."""
    m = []
    S.add(chemin(f"M -20 {y_sol} L 60 360 Q 120 230 260 200 Q 380 150 470 190 Q 600 230 660 330 L 820 {y_sol} Z",
                 volume(roche, 0.25, 0.75)))
    S.add(pierres(0, 180, 800, y_sol - 180, _assombrir(roche, 0.85),
                  forme=f"M -20 {y_sol} L 60 360 Q 120 230 260 200 Q 380 150 470 190 Q 600 230 660 330 L 820 {y_sol} Z", opacite=0.22))
    # mousse et buissons au pied de la roche
    for bx, bs in ((90, 0.9), (250, 0.55), (720, 0.8)):
        S.add(bosquet(bx, y_sol + 6, bs, "#69db7c", graine=int(bx)))
    # cheminée
    S.add(rect(520, 150, 50, 80, "#868e96", rx=4), rect(512, 140, 66, 18, "#495057", rx=4))
    S.add(cercle(560, 110, 18, "#dee2e6", opacity=0.8), cercle(580, 76, 24, "#dee2e6", opacity=0.6))
    if fenetre_:
        vitre = "#ffe066" if lumiere else "#a5d8ff"
        S.add(cercle(porte_x + 150 * porte_s, y_sol - 120 * porte_s, 40 * porte_s, "#6d4424"),
              cercle(porte_x + 150 * porte_s, y_sol - 120 * porte_s, 31 * porte_s, vitre),
              trait(porte_x + 150 * porte_s, y_sol - 151 * porte_s, porte_x + 150 * porte_s, y_sol - 89 * porte_s, "#6d4424", 5),
              trait(porte_x + 119 * porte_s, y_sol - 120 * porte_s, porte_x + 181 * porte_s, y_sol - 120 * porte_s, "#6d4424", 5))
        if lumiere:
            S.lumiere(porte_x + 150 * porte_s, y_sol - 120 * porte_s, 90 * porte_s, "#ffd43b", 0.7)
    S.add(porte_ronde(porte_x, y_sol, porte_s, porte, ouverte=ouverte, lumiere=lumiere))
    return m


def lanterne_papier(x, y, s=1.0, couleur="#ff8787", allumee=False, brulee=False, gelee=False, halo=True, S=None):
    """Lanterne ronde en papier suspendue ; (x, y) = point d'attache en haut."""
    if brulee:
        m = [trait(0, 0, 0, 30, "#495057", 3), rect(-18, 30, 36, 10, "#495057", rx=3),
             chemin("M -30 40 Q -40 70 -20 96 L -6 80 L 4 104 L 18 84 L 34 96 Q 40 66 30 40 Z", "#343a40"),
             cercle(-6, 70, 6, "#ff922b", opacity=0.8), cercle(14, 86, 4, "#ffd43b", opacity=0.8),
             cercle(0, 120, 10, "#868e96", opacity=0.5), cercle(10, 140, 7, "#868e96", opacity=0.35)]
        return place(m, x, y, s)
    corps = "#fff3bf" if allumee else couleur
    if gelee:
        corps = "#d0ebff"
    f = _assombrir(couleur, 0.75)
    m = [trait(0, 0, 0, 30, "#495057", 3), rect(-18, 30, 36, 10, f, rx=3),
         ellipse(0, 80, 46, 42, volume(corps, 0.2, 0.8) if not allumee else radial(["#fffbe6", corps, couleur]))]
    for dx in (-24, 0, 24):
        m.append(chemin(f"M {dx * 0.4} 40 Q {dx * 1.6} 80 {dx * 0.4} 120", stroke=f, sw=2, opacity=0.6))
    m += [rect(-18, 118, 36, 10, f, rx=3), trait(0, 128, 0, 150, f, 3), cercle(0, 152, 5, f)]
    if gelee:
        m += [poly([(-30, 116), (-24, 140), (-18, 116)], "#e7f5ff"), poly([(10, 118), (16, 146), (22, 118)], "#e7f5ff"),
              flocon_simple(-14, 70, 0.8, "#4dabf7"), flocon_simple(16, 92, 0.6, "#4dabf7")]
    if allumee:
        m.append(flammeche(0, 100, 0.45))
        if S is not None and halo:
            S.lumiere(x, y + 80 * s, 110 * s, "#ffd43b", 0.75)
    return place(m, x, y, s)


def baguette_magique(x, y, s=1.0, rot=0, etoile=OR):
    """Baguette de bois à étoile ; (x, y) = poignée."""
    m = [rect(-4, -110, 8, 110, "#8d5524", rx=4), rect(-5, -20, 10, 20, "#5c3a1e", rx=3),
         etoile5(0, -120, 18, etoile)]
    return place(m, x, y, s, rot=rot)


def grotte_dedans(S, y=580, mur="#e6d5c3", sol_c="#b08968", voute="#8d6e5a", papier=None):
    """Intérieur d'une maison-grotte : murs de roche, voûte sombre en arc,
    sol de terre battue. Propose les cachettes d'un intérieur."""
    interieur(S, mur, sol_c, y, papier=papier, plinthe=_assombrir(sol_c, 0.8))
    S.add(pierres(0, 0, S.w, y - 10, mur, pas_=34, larg=70, opacite=0.35))
    S.add(pierres(0, y + 4, S.w, S.h - y, sol_c, pas_=40, larg=110, opacite=0.18))
    S.add(chemin(f"M 0 0 L {S.w} 0 L {S.w} {y - 40} Q {S.w - 20} 140 {S.w - 200} 70 Q {S.w / 2} 20 200 70 "
                 f"Q 20 140 0 {y - 40} Z", volume(voute, 0.15, 0.8)))
    S.add(chemin(f"M {S.w} {y - 40} Q {S.w - 20} 140 {S.w - 200} 70 Q {S.w / 2} 20 200 70 Q 20 140 0 {y - 40}",
                 stroke=_assombrir(voute, 0.7), sw=6))


def torche(x, y, s=1.0, S=None):
    """Torche fixée au mur ; (x, y) = support. Pose son halo si S est donné."""
    m = [rect(-8, -10, 16, 60, "#6d4424", rx=4), rect(-20, -16, 40, 12, "#495057", rx=4),
         flammeche(0, -14, 0.9)]
    if S is not None:
        S.lumiere(x, y - 40 * s, 140 * s, "#ffa94d", 0.7)
    return place(m, x, y, s)


def coussins(x, y, s=1.0, couleurs=("#9775fa", "#e599f7", "#748ffc", "#f783ac")):
    """Grand lit de coussins empilés ; (x, y) = milieu de la base."""
    m = []
    pos = [(-90, -30, 80, 34), (0, -34, 90, 38), (90, -30, 80, 34), (-50, -84, 76, 32), (50, -86, 76, 32), (0, -128, 70, 30)]
    for k, (px, py, rx, ry) in enumerate(pos):
        c = couleurs[k % len(couleurs)]
        m.append(ellipse(px, py, rx, ry, volume(c, 0.3, 0.75)))
        m.append(cercle(px, py, 4, _assombrir(c, 0.7)))
    return place(m, x, y, s)
