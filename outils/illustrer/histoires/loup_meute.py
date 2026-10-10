"""Le loup et sa meute — la vie d'une famille de loups gris.

La meute est une famille : les parents et leurs petits d'un, deux ou trois
ans. Dans la neige profonde, les loups marchent en file indienne, chacun
dans les traces de celui de devant. Ils hurlent pour s'appeler et pour dire
aux autres meutes « Ici, c'est chez nous » (pas pour la Lune) ; un hurlement
s'entend à des kilomètres. Au printemps, la mère met bas dans une tanière ;
les louveteaux naissent aveugles et sourds, ouvrent les yeux vers deux
semaines et sortent vers trois semaines. Les grands frères et sœurs les
gardent et leur rapportent de la viande dans leur ventre ; les petits
lèchent le museau des grands pour réclamer. Queue haute, queue basse,
révérence du jeu : les loups se parlent avec le corps. La chasse échoue
souvent. L'hiver, la double fourrure garde le loup au chaud : il dort en
boule, la queue sur le nez. Le loup est timide et fuit les humains.

Plans : 1 large (la file indienne) · 2 gros plan (le hurlement) · 3 moyen
(la famille) · 4 coupe (la tanière) · 5 moyen (le jeu) · 6 moyen (la
nounou) · 7 gros plan (« J'ai faim ! ») · 8 schéma (le langage) · 9 gros
plan (le flair) · 10 large (la chasse) · 11 gros plan (dormir dans la
neige) · 12 large (le chœur de la meute).
"""
from base import *
from base import _assombrir
from animaux import etiquette, coupe_terre, herbes
from sciences import fleche

ID = "loup-meute"

PELAGES = {
    "gris": ("#8a9097", "#4f565d", "#eef0f2"),
    "fonce": ("#62696f", "#34393e", "#cfd4d8"),
    "brun": ("#9c8b78", "#5e5044", "#f3ede4"),
    "noir": ("#41464b", "#202327", "#868e96"),
    "petit": ("#6e625a", "#463d37", "#b3a598"),
}
NEIGE = "#e7eefb"


# --- Le loup ----------------------------------------------------------------

def _oreille(x, couleur, interieur, petit, rot):
    if petit:
        forme = [chemin("M -15 4 Q -14 -36 0 -38 Q 14 -36 15 4 Z", couleur)]
        if interieur:
            forme.append(chemin("M -8 0 Q -7 -24 0 -26 Q 7 -24 8 0 Z", interieur))
    else:
        forme = [chemin("M -15 4 L -3 -44 Q 2 -46 15 4 Z", couleur)]
        if interieur:
            forme.append(chemin("M -8 0 L -2 -32 L 8 0 Z", interieur))
    return place(forme, x, -22, rot=rot)


def tete_loup(c, f, cl, petit=False, oreilles="droites", expr="sourire", regard=(1, 0), gueule=None):
    """Tête de loup de profil, museau à droite ; (0, 0) = milieu du crâne."""
    L = 46 if petit else 74
    rot_o = -62 if oreilles == "couchees" else (-10 if oreilles == "droites" else -30)
    m = [_oreille(8, f, None, petit, rot_o + 6),
         ellipse(0, 0, 40, 36 if petit else 34, volume(c, 0.35, 0.8)),
         _oreille(-14, c, cl, petit, rot_o)]
    m.append(chemin("M -38 4 Q -44 30 -16 40 Q 10 42 26 26 L 20 6 Z", cl))
    m.append(chemin(f"M 6 -20 Q {L * 0.55} -18 {L} -6 Q {L + 8} 4 {L} 12 Q {L * 0.55} 18 10 18 Z", volume(c, 0.35, 0.8)))
    m.append(chemin(f"M 14 12 Q {L * 0.55} 12 {L - 2} 12 Q {L * 0.6} 28 18 26 Z", cl))
    m.append(ellipse(10, -18, 9, 4, cl, opacity=0.8))
    m.append(ellipse(L + 2, -4, 8, 6.5, "#212529"))
    m.append(cercle(L, -7, 2, "#fff", opacity=0.6))
    if gueule == "o":
        m.append(ellipse(L - 10, 16, 9, 8, "#6b2b2b"))
    else:
        m.append(chemin(f"M {L - 4} 12 Q {L * 0.6} 20 {L * 0.32} 12", stroke=f, sw=2.5))
        if expr == "rire":
            m.append(chemin(f"M {L * 0.42} 16 Q {L * 0.46} 36 {L * 0.58} 34 Q {L * 0.68} 26 {L * 0.64} 16 Z", "#f783ac", stroke="#c2255c", sw=1.5))
    style = "fermes" if expr == "dort" else ("heureux" if expr in ("content", "rire") else "normal")
    m.append(oeil(14, -8, style, regard, taille=0.8 if petit else 0.6))
    return g(m)


def _patte_avant(L, couleur, pied):
    return [chemin(f"M -15 -10 L 15 -10 L 9 {L - 8} L -9 {L - 8} Z", couleur), ellipse(4, L - 5, 14, 7, pied)]


def _patte_arriere(L, couleur, pied):
    return [chemin(f"M -26 -20 Q 14 -30 16 {L * 0.25} L 2 {L * 0.62} L 9 {L - 8} L -7 {L - 8} L -12 {L * 0.62} Q -34 {L * 0.3} -26 -20 Z", couleur),
            ellipse(2, L - 5, 13, 7, pied)]


QUEUES = {
    "normale": ("M -112 -175 Q -150 -165 -160 -110 Q -166 -70 -150 -60 Q -136 -70 -134 -110 Q -128 -145 -108 -150 Z", (-152, -68)),
    "haute": ("M -112 -182 Q -150 -200 -168 -248 Q -178 -272 -158 -270 Q -140 -232 -106 -160 Z", (-166, -262)),
    "basse": ("M -112 -168 Q -132 -120 -112 -72 Q -100 -62 -94 -74 Q -108 -112 -98 -152 Z", (-104, -70)),
    "droite": ("M -112 -178 Q -170 -172 -206 -152 Q -216 -140 -200 -136 Q -160 -146 -108 -150 Z", (-204, -144)),
}

POSES_DEBOUT = {
    # angles des pattes (arrière loin, avant loin, arrière près, avant près), tête (x, y, rot),
    # points de contrôle du dessus et du dessous du cou, queue
    "debout": ((4, -4, -2, 3), (150, -232, 0), (100, -262), (135, -130), "normale"),
    "trot": ((-22, 22, 22, -26), (168, -200, 8), (118, -230), (140, -120), "droite"),
    "tete_basse": ((4, -4, -2, 3), (176, -118, 14), (130, -205), (140, -80), "normale"),
    "renifle": ((4, -4, -2, 3), (172, -70, 34), (140, -190), (140, -50), "normale"),
    "jeu": ((0, 0, 0, 0), (168, -112, -4), (120, -160), (130, -60), "haute"),
}


def loup(x, y, s=1.0, flip=False, pose="debout", pelage="gris", petit=False, queue=None, oreilles="droites",
         expr="sourire", regard=(1, 0), rot=0, neige=False, gueule=None):
    """Loup de profil, tête à droite ; (x, y) = sous les pattes.
    pose : "debout", "trot", "renifle", "jeu" (révérence du jeu), "assis", "hurle", "couche", "dort" (en boule).
    petit : louveteau (grosse tête, pattes courtes)."""
    c, f, cl = PELAGES[pelage]
    loin = _assombrir(c, 0.84)
    pied = _assombrir(c, 0.7)
    m = []
    if pose in POSES_DEBOUT:
        angles, (hx, hy, hrot), (cx, cy), (bx, by), q_def = POSES_DEBOUT[pose]
        H = 100 if petit else 140
        dy = 140 - H
        kx = 0.82 if petit else 1.0
        ts = 1.45 if petit else 1.0
        if petit:
            hx, hy = hx * kx + 6, hy + dy + 14
            cx, cy = cx * kx + 6, cy + dy + 14
            bx, by = bx * kx, by + dy
            q_def = "haute" if pose == "jeu" else "droite"
        a_al, a_avl, a_ap, a_avp = angles
        q = QUEUES[queue or q_def]
        dessin_q = [chemin(q[0], volume(c, 0.3, 0.8)), ellipse(q[1][0], q[1][1], 12, 14, f)]
        m.append(place(place(dessin_q, 116, 165), -116 * kx, -165 + dy, 0.7 if petit else 1.0))
        m.append(place(_patte_arriere(H, loin, pied), -78 * kx, -140 + dy, rot=a_al))
        if pose != "jeu":
            m.append(place(_patte_avant(H, loin, pied), 70 * kx, -140 + dy, rot=a_avl))
        if pose == "jeu":
            corps = "M -126 -150 Q -128 -196 -62 -188 Q 30 -166 104 -112 Q 128 -86 104 -64 Q 72 -54 30 -74 Q -40 -98 -96 -108 Q -126 -118 -126 -150 Z"
            selle = "M -112 -172 Q -50 -200 40 -166 Q 0 -160 -112 -160 Z"
            m.append(place(_patte_avant(100, loin, pied), 70, -16, rot=-86))
            m.append(chemin("M 76 -84 L 108 -84 L 92 -10 L 66 -12 Z", loin))
        else:
            corps = "M -124 -150 Q -128 -200 -62 -196 Q 20 -206 84 -196 Q 132 -184 126 -128 Q 116 -90 62 -96 Q -20 -90 -94 -104 Q -126 -114 -124 -150 Z"
            selle = "M -110 -172 Q -50 -206 70 -194 Q 10 -178 -110 -162 Z"
        haut = [chemin(corps, volume(c, 0.3, 0.8)), chemin(selle, f, opacity=0.45),
                chemin("M -70 -110 Q 0 -100 60 -112 Q 0 -124 -70 -120 Z", cl, opacity=0.8)]
        if neige:
            haut.append(chemin("M -100 -186 Q -30 -206 60 -196 Q 20 -186 -100 -178 Z", "#fff"))
        m.append(place(haut, 0, dy, s=1.0, sy=1.0) if not petit else place(haut, 0, dy, kx, sy=1.0))
        m.append(place(_patte_arriere(H, c, pied), -92 * kx, -138 + dy, rot=a_ap))
        if pose == "jeu":
            m.append(chemin("M 92 -80 L 124 -80 L 110 -8 L 84 -10 Z", c))
            m.append(place(_patte_avant(100, c, pied), 90, -14, rot=-86))
        else:
            m.append(place(_patte_avant(H, c, pied), 88 * kx, -138 + dy, rot=a_avp))
        b1, b2, b3 = (30 * kx, -186 + dy), (120 * kx, -118 + dy), (60 * kx, -116 + dy)
        m.append(chemin(f"M {b1[0]} {b1[1]} Q {cx} {cy} {hx - 14} {hy - 30} L {hx + 14} {hy + 22} Q {bx} {by} {b2[0]} {b2[1]} "
                        f"Q {b2[0] - 24} {b2[1] + 12} {b3[0]} {b3[1]} Z", volume(c, 0.3, 0.8)))
        m.append(place(tete_loup(c, f, cl, petit, oreilles, expr, regard, gueule), hx, hy, ts, rot=hrot))
        boite = (-215, -300, 235, 0)
    elif pose in ("assis", "hurle"):
        m.append(chemin("M -70 -30 Q -150 -30 -170 -10 Q -165 4 -120 0 Q -80 -2 -60 -12 Z", volume(c, 0.3, 0.8)))
        m.append(ellipse(-164, -6, 12, 9, f))
        m.append(place(_patte_avant(140, loin, pied), 62, -140))
        m.append(chemin("M -80 -40 Q -100 -120 -40 -175 Q 10 -225 70 -222 Q 112 -205 106 -150 Q 96 -100 70 -70 Q 20 -10 -40 -8 Q -80 -14 -80 -40 Z", volume(c, 0.3, 0.8)))
        m.append(chemin("M -60 -150 Q -10 -215 60 -220 Q 10 -190 -60 -130 Z", f, opacity=0.45))
        if neige:
            m.append(chemin("M -50 -170 Q 0 -222 60 -222 Q 10 -205 -50 -160 Z", "#fff"))
        m.append(ellipse(-30, -58, 58, 54, volume(c, 0.3, 0.8)))
        m.append(ellipse(12, -7, 36, 9, pied))
        m.append(chemin("M 80 -212 Q 120 -170 96 -110 Q 76 -120 66 -170 Z", cl))
        m.append(place(_patte_avant(138, c, pied), 84, -138))
        hx, hy, hrot = (92, -262, -58) if pose == "hurle" else (104, -258, 0)
        m.append(chemin(f"M -10 -196 Q {hx - 40} {hy - 20} {hx - 12} {hy - 28} L {hx + 16} {hy + 18} Q {hx + 4} {hy + 60} 104 -150 Z", volume(c, 0.3, 0.8)))
        m.append(place(tete_loup(c, f, cl, petit, oreilles, expr, regard, "o" if pose == "hurle" else gueule), hx, hy, 1.0, rot=hrot))
        boite = (-175, -330, 190, 0)
    else:   # couché ou en boule
        dort = pose == "dort"
        if not dort:
            m.append(chemin("M -120 -50 Q -180 -30 -200 -10 Q -190 4 -150 -2 Q -120 -10 -110 -30 Z", volume(c, 0.3, 0.8)))
            m.append(ellipse(-194, -6, 12, 8, f))
        m.append(ellipse(0, -60, 135, 60, volume(c, 0.3, 0.8)))
        m.append(chemin("M -120 -80 Q -40 -132 90 -104 Q 0 -108 -120 -70 Z", f, opacity=0.45))
        m.append(chemin("M -112 -30 Q -70 -110 -4 -64", stroke=f, sw=3, opacity=0.5))
        m.append(chemin("M -60 -10 Q 0 0 80 -14", stroke=cl, sw=10, opacity=0.6))
        if neige:
            m.append(chemin("M -110 -96 Q -30 -128 70 -114 Q 20 -108 -110 -86 Z", "#fff"))
        if dort:
            m.append(ellipse(146, -10, 32, 10, c))
            m.append(place(tete_loup(c, f, cl, petit, "repos", "dort", regard), 96, -58, 0.95, rot=20))
            m.append(chemin("M -128 -40 Q -130 4 -40 2 Q 80 0 128 -14 Q 156 -28 146 -58 Q 178 -52 180 -24 Q 174 4 120 10 Q 20 18 -60 16 Q -150 10 -140 -40 Z",
                            volume(c, 0.3, 0.8)))
            m.append(ellipse(160, -46, 30, 18, volume(c, 0.3, 0.8), rot=-20))
            m.append(ellipse(184, -54, 10, 9, f))
            boite = (-150, -130, 200, 0)
        else:
            m.append(ellipse(150, -10, 36, 11, c))
            m.append(chemin("M 80 -100 Q 120 -150 140 -140 L 140 -80 Q 110 -60 80 -60 Z", volume(c, 0.3, 0.8)))
            m.append(place(tete_loup(c, f, cl, petit, oreilles, expr, regard, gueule), 128, -128, 1.0))
            boite = (-205, -200, 210, 0)
    a, b = boite[0], boite[2]
    if flip:
        a, b = -b, -a
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x + a * s, y + boite[1] * s, x + b * s, y)


def cerf(x, y, s=1.0, flip=False):
    """Petit cerf de Virginie qui s'enfuit, la queue blanche levée (vu de loin)."""
    c = "#b07a4a"
    m = [trait(-50, -60, -70, 0, _assombrir(c, 0.8), 7), trait(40, -60, 60, 0, _assombrir(c, 0.8), 7),
         ellipse(0, -80, 70, 32, volume(c, 0.3, 0.8)),
         trait(-40, -60, -30, 0, c, 8), trait(50, -60, 80, -10, c, 8),
         chemin("M 40 -100 Q 60 -150 80 -160 L 96 -146 Q 76 -120 66 -80 Z", c),
         ellipse(96, -150, 22, 14, c, rot=20), poly([(82, -162), (74, -190), (92, -166)], c),
         chemin("M -66 -96 Q -90 -130 -76 -140 Q -60 -120 -58 -100 Z", "#fff")]
    return place(m, x, y, s, flip=flip)


# --- Décors -----------------------------------------------------------------

def foret_neige(S, horizon=500, graine=1, haut="#4c6ef5", bas="#d0ebff", nuit_=False):
    if nuit_:
        nuit(S, "#1c2a52", "#4c5b9a")
    else:
        ciel(S, haut, bas)
    r = random.Random(graine)
    for k in range(12):
        S.add(sapin(r.uniform(-20, 820), horizon + r.uniform(-10, 6), r.uniform(0.45, 0.85),
                    "#2b6a3e" if not nuit_ else "#1f4b33", "#2f7e44" if not nuit_ else "#24593b", neige=True))
    S.add(rect(0, horizon, 800, 800 - horizon, lineaire([(0, "#ffffff" if not nuit_ else "#c5d0ec"), (1, "#dbe4ff" if not nuit_ else "#8f9fd1")])))
    for k in range(5):
        S.add(ellipse(r.uniform(0, 800), r.uniform(horizon + 60, 780), r.uniform(80, 160), 14, "#fff" if not nuit_ else "#d4ddf5", opacity=0.6))
    for x in (60, 740, 160, 640):
        S.proposer_cachette(x, horizon + 230)


def prairie(S, horizon=460, graine=1):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, horizon, "#b2f2bb", graine=graine)
    r = random.Random(graine)
    for k in range(6):
        S.add(sapin(r.uniform(0, 800), horizon + r.uniform(-4, 10), r.uniform(0.5, 0.75), "#2b8a3e", "#2f9e44"))
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#8ce99a")))
    herbes(S, horizon + 40, 790, 22, graine=graine)


def traces(S, x0, y0, x1, y1, nb=10, couleur="#adb5bd"):
    for k in range(nb):
        t = k / max(nb - 1, 1)
        S.add(ellipse(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t + (6 if k % 2 else -6), 9, 5, couleur, opacity=0.8))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret_neige(S, 560, graine=2, nuit_=True)
    S.add(lune(170, 170, 60))
    etoiles(S, 30, graine=2, zone=(0, 0, 800, 420))
    S.add(chemin("M 160 800 Q 260 560 460 560 Q 640 560 800 640 L 800 800 Z", "#e1e8f8"))
    S.add(loup(340, 600, 1.0, pose="hurle", pelage="gris"))
    S.add(loup(660, 650, 0.75, pose="assis", pelage="noir", flip=True, regard=(-1, -0.3)))
    S.add(loup(190, 720, 0.5, pose="debout", pelage="petit", petit=True, regard=(1, -0.5)))
    S.cachette(720, 760)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(loup(170, 250, 0.62, pose="debout", pelage="gris"))
    S.add(loup(315, 252, 0.34, pose="debout", pelage="petit", petit=True, flip=True, regard=(-1, -0.4)))
    return S


def p01():
    """Plan large : l'hiver, dans la forêt, la meute avance en file indienne dans la neige profonde."""
    S = Scene()
    foret_neige(S, 470, graine=1, haut="#91a7ff", bas="#e7f5ff")
    traces(S, 690, 556, 800, 540, 4)
    for pel, x, yy, t in (("fonce", 650, 560, 0.32), ("brun", 490, 605, 0.38), ("gris", 305, 655, 0.45), ("noir", 95, 715, 0.52)):
        S.add(loup(x, yy, t, pose="trot", pelage=pel))
        S.add(ellipse(x - 10 * t, yy - 6 * t, 190 * t, 34 * t, "#fff", opacity=0.9))
    S.add(texte(400, 130, "En file indienne", 48, "#364fc7", contour="#fff"))
    S.cachette(730, 600, "air")
    return S


def p02():
    """Gros plan : la nuit, un loup lève le museau et hurle : « Aouuuuuh ! »."""
    S = Scene()
    foret_neige(S, 600, graine=3, nuit_=True)
    S.add(lune(170, 200, 55))
    etoiles(S, 40, graine=3, zone=(0, 0, 800, 480))
    S.add(chemin("M 0 680 Q 200 600 420 620 Q 600 640 800 700 L 800 800 L 0 800 Z", "#d4ddf5"))
    S.add(loup(330, 720, 1.25, pose="hurle", pelage="gris", neige=True))
    S.camera(1.25, 380, 440)
    for k in range(3):
        S.dessus(chemin(f"M {560 + k * 30} {300 - k * 40} q 30 -30 0 -60", stroke="#e7f5ff", sw=5, opacity=0.8))
    S.dessus(texte(560, 110, "Aouuuuuh !", 70, "#fff", contour="#364fc7"))
    S.cachette(90, 760)
    return S


def p03():
    """Plan moyen : la meute, c'est une famille : les parents, les grands frères et sœurs, les louveteaux."""
    S = Scene()
    prairie(S, 400, graine=3)
    S.add(loup(250, 560, 0.75, pose="debout", pelage="fonce"))
    S.add(loup(560, 570, 0.72, pose="debout", pelage="brun", flip=True, regard=(-1, 0)))
    S.add(loup(110, 700, 0.6, pose="assis", pelage="gris"))
    S.add(loup(700, 720, 0.6, pose="assis", pelage="noir", flip=True))
    S.add(loup(290, 730, 0.42, pose="jeu", pelage="petit", petit=True, expr="rire"))
    S.add(loup(540, 740, 0.42, pose="debout", pelage="petit", petit=True, flip=True, regard=(-1, 0)))
    S.add(loup(410, 785, 0.36, pose="dort", pelage="petit", petit=True))
    S.add(etiquette(200, 330, "le papa", 30, "#34393e"), etiquette(620, 330, "la maman", 30, "#5e5044"),
          etiquette(120, 470, "les grands", 28, "#4f565d"), etiquette(690, 480, "les grands", 28, "#202327"),
          etiquette(400, 620, "les louveteaux", 30, "#463d37"))
    S.cachette(730, 220, "air")
    return S


def p04():
    """Coupe : au printemps, dans la tanière creusée sous la terre, la maman et ses louveteaux nouveau-nés, les yeux fermés."""
    S = Scene()
    coupe_terre(S, 300, graine=4)
    for x in (560, 700):
        S.add(sapin(x, 292, 0.7, "#2b8a3e", "#2f9e44"))
    S.add(chemin("M 20 300 Q 60 250 120 262 Q 170 276 210 300 Z", "#a0693a"))
    S.add(chemin("M 112 296 Q 132 430 280 520", stroke="#3d2817", sw=80))
    S.add(ellipse(450, 560, 280, 140, "#3d2817"), ellipse(450, 580, 260, 110, "#4a3220"))
    S.add(loup(440, 650, 0.85, pose="couche", pelage="brun", expr="content"))
    for k, x in enumerate((340, 440, 540)):
        S.add(loup(x, 696, 0.42, pose="dort", pelage="petit", petit=True, flip=bool(k % 2)))
    S.add(texte(400, 120, "Les louveteaux naissent les yeux fermés", 34, "#463d37", contour="#fff"))
    S.lumiere(450, 600, 260, "#ffe8cc", 0.2)
    return S


def p05():
    """Plan moyen : à la sortie de la tanière, les louveteaux jouent : révérence, bonds, et une branche qu'on se dispute."""
    S = Scene()
    prairie(S, 420, graine=5)
    S.add(chemin("M 0 420 Q 120 300 260 330 Q 330 350 360 420 Z", "#a0693a"))
    S.add(ellipse(180, 400, 70, 50, "#3d2817"))
    S.add(loup(180, 640, 0.6, pose="jeu", pelage="petit", petit=True, expr="rire"))
    S.add(loup(380, 560, 0.55, pose="trot", pelage="petit", petit=True, rot=-14, expr="rire"))
    S.add(loup(470, 720, 0.6, pose="debout", pelage="petit", petit=True, expr="content"))
    S.add(loup(760, 720, 0.6, pose="debout", pelage="petit", petit=True, flip=True, expr="content"))
    S.add(trait(570, 624, 680, 624, "#8d5524", 9), trait(620, 624, 632, 604, "#8d5524", 5))
    S.add(texte(560, 140, "On joue !", 60, "#463d37", contour="#fff"))
    return S


def p06():
    """Plan moyen : les parents partent chasser ; la grande sœur reste couchée près des louveteaux endormis."""
    S = Scene()
    prairie(S, 440, graine=6)
    S.add(loup(560, 470, 0.32, pose="trot", pelage="fonce"), loup(680, 476, 0.32, pose="trot", pelage="brun"))
    S.add(loup(330, 700, 0.85, pose="couche", pelage="gris", regard=(1, 0.4)))
    for k, (x, y) in enumerate(((560, 740), (640, 760), (600, 700))):
        S.add(loup(x, y, 0.32, pose="dort", pelage="petit", petit=True, flip=bool(k % 2)))
    S.add(texte(400, 130, "La grande sœur garde les petits", 40, "#4f565d", contour="#fff"))
    return S


def p07():
    """Gros plan : la maman revient ; les louveteaux lèchent son museau : « J'ai faim ! »."""
    S = Scene()
    prairie(S, 400, graine=7)
    S.add(loup(560, 720, 1.0, pose="tete_basse", pelage="brun", flip=True, regard=(-1, 0.3), expr="content"))
    S.add(loup(110, 770, 0.5, pose="jeu", pelage="petit", petit=True, expr="rire"))
    S.add(loup(240, 750, 0.6, pose="debout", pelage="petit", petit=True, expr="content", regard=(1, -0.5)))
    S.camera(1.15, 360, 560)
    S.dessus(bulle(220, 200, 230, 90, "J'ai faim !", 40, pointe=(320, 450)))
    return S


def p08():
    """Schéma : le langage des loups : queue haute, oreilles couchées, révérence du jeu."""
    S = Scene()
    fond(S, "#f1f3f5")
    for k in range(3):
        S.add(rect(40, 40 + k * 250, 720, 230, "#fff", stroke="#dee2e6", stroke_width=4, rx=20))
    S.add(loup(230, 245, 0.62, pose="debout", pelage="fonce", queue="haute"))
    S.add(loup(230, 495, 0.62, pose="debout", pelage="gris", queue="basse", oreilles="couchees", regard=(1, 0.5)))
    S.add(loup(230, 745, 0.6, pose="jeu", pelage="brun", expr="rire"))
    S.add(texte(560, 150, "Queue haute :", 32, "#34393e"), texte(560, 195, "« Je suis sûr de moi. »", 30, "#364fc7"))
    S.add(texte(560, 400, "Oreilles couchées :", 32, "#34393e"), texte(560, 445, "« Je suis gentil. »", 30, "#364fc7"))
    S.add(texte(560, 650, "Les fesses en l'air :", 32, "#34393e"), texte(560, 695, "« On joue ? »", 30, "#364fc7"))
    S.cachette(740, 790, "air")
    return S


def p09():
    """Gros plan : le nez dans la neige, le loup suit des traces de lièvre."""
    S = Scene()
    foret_neige(S, 430, graine=9, haut="#a5d8ff", bas="#f1f3f5")
    for k in range(6):
        x, y = 160 + k * 110, 760 - k * 30
        S.add(ellipse(x, y, 10, 16, "#adb5bd"), ellipse(x + 16, y, 10, 16, "#adb5bd"), ellipse(x + 40, y - 20, 8, 8, "#adb5bd"), ellipse(x + 40, y + 20, 8, 8, "#adb5bd"))
    S.add(loup(280, 720, 1.1, pose="renifle", pelage="gris", expr="content"))
    S.add(etiquette(640, 540, "des traces de lièvre", 30, "#495057"))
    S.add(texte(400, 130, "Snif, snif…", 56, "#364fc7", contour="#fff"))
    S.cachette(730, 210, "air")
    return S


def p10():
    """Plan large : la meute court sur le lac gelé ; au loin, des cerfs s'enfuient dans la forêt."""
    S = Scene()
    foret_neige(S, 430, graine=10, haut="#ffc9c9", bas="#fff4e6")
    S.add(chemin("M 0 520 Q 400 480 800 520 L 800 700 Q 400 740 0 700 Z", "#d0ebff"))
    for k in range(5):
        S.add(trait(80 + k * 150, 600 + (k % 2) * 40, 140 + k * 150, 600 + (k % 2) * 40, "#fff", 4, opacity=0.8))
    S.add(cerf(650, 480, 0.6), cerf(740, 486, 0.5), cerf(570, 488, 0.45))
    for pel, x, yy in (("fonce", 520, 610), ("brun", 290, 600), ("gris", 420, 700), ("noir", 170, 690)):
        S.add(loup(x, yy, 0.42, pose="trot", pelage=pel))
    S.add(texte(400, 140, "La meute chasse ensemble", 44, "#9c4221", contour="#fff"))
    return S


def p11():
    """Gros plan : dans la neige qui tombe, le loup dort roulé en boule, la queue sur le nez."""
    S = Scene()
    foret_neige(S, 380, graine=11, haut="#adb5bd", bas="#e9ecef")
    S.add(loup(380, 680, 1.5, pose="dort", pelage="gris", neige=True))
    flocons(S, 50, graine=11)
    S.add(texte(400, 140, "Bien au chaud dans sa fourrure", 42, "#495057", contour="#fff"))
    S.cachette(730, 570, "air")
    return S


def p12():
    """Plan large : la nuit, toute la meute hurle en chœur sur la colline."""
    S = Scene()
    nuit(S, "#141e3c", "#3b4a8a")
    etoiles(S, 60, graine=12, zone=(0, 0, 800, 500))
    S.add(lune(640, 140, 50))
    for k in range(9):
        S.add(sapin(30 + k * 95, 600, 0.5, "#1f4b33", "#24593b", neige=True))
    S.add(chemin("M 0 800 L 0 640 Q 200 520 420 540 Q 640 560 800 640 L 800 800 Z", "#c5d0ec"))
    S.add(loup(250, 600, 0.55, pose="hurle", pelage="fonce"))
    S.add(loup(400, 580, 0.6, pose="hurle", pelage="brun"))
    S.add(loup(560, 610, 0.5, pose="hurle", pelage="noir"))
    S.add(loup(150, 680, 0.42, pose="hurle", pelage="gris"))
    S.add(loup(480, 700, 0.3, pose="hurle", pelage="petit"))
    S.add(texte(400, 760, "Aouuuh ! Aouuuh ! Aouuuuuh !", 44, "#fff", contour="#364fc7"))
    S.cachette(720, 700)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("loup-seul.svg", vignette),
    ("01-file-indienne.svg", p01), ("02-aouuuh.svg", p02), ("03-la-famille.svg", p03),
    ("04-la-taniere.svg", p04), ("05-on-joue.svg", p05), ("06-la-nounou.svg", p06),
    ("07-j-ai-faim.svg", p07), ("08-le-langage.svg", p08), ("09-le-flair.svg", p09),
    ("10-la-chasse.svg", p10), ("11-au-chaud.svg", p11), ("12-le-choeur.svg", p12),
]
