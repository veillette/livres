"""Alouette, gentille alouette — la vieille chanson, version chatouilles.

Margot chatouille l'alouette avec un épi de blé : la tête, le bec, le cou,
les ailes, le dos, les pattes, la queue (chanson à reprendre en chatouillant
l'enfant). L'alouette rit tant qu'elle roule dans le blé, puis chatouille
Margot à son tour.

Plans : 1 large (l'alouette chante dans le ciel) · 2 moyen (elle se pose) ·
3 gros plan (la tête) · 4 gros plan serré (le bec) · 5 moyen (le cou) ·
6 large (les ailes ouvertes) · 7 gros plan (le dos) · 8 moyen (les pattes,
perchée sur la main) · 9 gros plan (la queue) · 10 large (on roule dans le
blé) · 11 gros plan (le nez de Margot) · 12 large (le soir, elle s'envole).
"""
from base import *
from base import _assombrir
from fantastique import personne

ID = "alouette"

MARGOT = dict(peau="claire", cheveux="roux", coiffure="couettes", habit="#4dabf7", robe=False, jambes="#1864ab",
              couleur_acc="#ffd43b", taches=True, nez="retrousse")

BRUN = "#b9875a"
BRUN_FONCE = "#8a5a3b"
CREME = "#f6e7cf"
PATTES = "#d9a07a"

# Parties du corps de l'alouette (repère local, tournée vers la droite)
PARTIES = {
    "tete": (50, -156), "bec": (100, -121), "cou": (36, -98), "ailes": (-14, -84),
    "dos": (-30, -112), "pattes": (13, -14), "queue": (-112, -92),
}


def alouette(x, y, s=1.0, expr="sourire", ailes="bas", flip=False, rot=0, regard=(1, 0), epi_bec=False):
    """L'alouette des champs, de trois quarts, tournée vers la droite
    (flip=True : vers la gauche) ; (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    # pattes
    for dx in (-12, 12):
        m.append(trait(dx, -34, dx + 2, -4, PATTES, 4))
        m.append(chemin(f"M {dx - 8} 0 L {dx + 2} -5 L {dx + 13} 0 M {dx + 2} -5 L {dx - 3} 2", stroke=PATTES, sw=3.5))
    # queue : trois plumes en éventail
    for k, (a, L) in enumerate(((-26, 62), (-14, 68), (-2, 60))):
        m.append(ellipse(-60 - L / 2 * math.cos(math.radians(a)), -76 + L / 2 * math.sin(math.radians(a)), L / 2, 11,
                         volume(BRUN_FONCE if k != 1 else _assombrir(BRUN, 0.88), 0.3, 0.8), rot=-a))
    m.append(chemin("M -112 -90 L -118 -84 M -108 -70 L -114 -66", stroke=CREME, sw=3, opacity=0.8))
    # ailes levées (derrière le corps)
    if ailes == "haut":
        for dx, rot_, k in ((-30, -24, 0.9), (6, -4, 1.0)):
            aile = chemin("M 0 0 Q -30 -70 -6 -128 Q 14 -96 26 -70 Q 34 -40 22 0 Z", volume(_assombrir(BRUN, 0.9 if k == 1 else 0.8), 0.3, 0.8))
            plumes = chemin("M -4 -120 L 4 -96 M 8 -110 L 12 -88 M 18 -94 L 18 -74", stroke=CREME, sw=3, opacity=0.8)
            m.append(place([aile, plumes], dx, -96, k, rot=rot_))
    # corps
    m.append(ellipse(0, -72, 60, 44, volume(BRUN, 0.3, 0.8)))
    m.append(ellipse(12, -58, 44, 28, volume(CREME, 0.35, 0.9)))
    tirets = " ".join(f"M {px} {py} l 3 6" for px, py in ((26, -88), (36, -82), (18, -80), (30, -74), (42, -72), (22, -68), (10, -84), (-2, -96), (-14, -104), (8, -100)))
    m.append(chemin(tirets, stroke=BRUN_FONCE, sw=3, opacity=0.75))
    m.append(ombrage(ellipse(0, -72, 60, 44, "#000"), sombre=[(-10, -36, 60, 18)], clair=[(-10, -104, 24, 10, -10)]))
    # aile repliée
    if ailes != "haut":
        m.append(ellipse(-12, -80, 46, 26, volume(_assombrir(BRUN, 0.88), 0.3, 0.8), rot=-12))
        m.append(chemin("M -46 -70 Q -16 -64 22 -86 M -50 -80 Q -20 -76 14 -96 M -38 -92 Q -14 -92 6 -104",
                        stroke=CREME, sw=3, opacity=0.75))
    # tête, huppe, bec
    m.append(ellipse(30, -106, 22, 24, BRUN))
    # huppe : quelques plumes relevées vers l'arrière du crâne
    m.append(chemin("M 24 -146 Q 16 -170 0 -178 Q 12 -168 10 -160 Q 22 -168 30 -174 Q 26 -162 38 -154 Z", BRUN_FONCE))
    m.append(cercle(50, -126, 34, volume(BRUN, 0.3, 0.82)))
    m.append(chemin("M 50 -150 l 3 6 M 40 -144 l 3 6 M 30 -134 l 3 6", stroke=BRUN_FONCE, sw=3, opacity=0.7))
    m.append(ellipse(58, -112, 16, 10, "#e3c49e"))
    m.append(ellipse(46, -110, 9, 6, ROSE, opacity=0.6))
    if bs in ("ouverte", "o", "crie", "langue"):
        m.append(poly([(78, -130), (108, -127), (80, -120)], volume(PATTES, 0.4, 0.75)))
        m.append(poly([(80, -117), (102, -110), (78, -111)], _assombrir(PATTES, 0.85)))
        m.append(poly([(80, -120), (100, -118), (80, -117)], ROUGE_BOUCHE))
    else:
        m.append(poly([(78, -130), (106, -121), (78, -113)], volume(PATTES, 0.4, 0.75)))
        m.append(trait(80, -121, 102, -121, _assombrir(PATTES, 0.7), 1.5))
    # sourcil clair (comme les vraies alouettes) et œil
    m.append(chemin("M 52 -142 Q 64 -148 76 -140", stroke=CREME, sw=4))
    m.append(oeil(64, -130, ys, regard, taille=0.95))
    if ss:
        m.append(place(sourcils(0, 0, ss), 64 - 18, -128, 0.8))
    if epi_bec:
        m.append(epi(96, -122, 200, -150))
    contenu = avec_contour(m, s, 0.4)
    contenu += occuper(-125, -186, 112, 0)
    return place(contenu, x, y, s, flip=flip, rot=rot)


def partie(x, y, s, nom, flip=False):
    """Point d'une partie de l'alouette, dans la page."""
    px, py = PARTIES[nom]
    return x + (-px if flip else px) * s, y + py * s


def epi(x0, y0, x1, y1, ep=1.0):
    """Épi de blé tenu en (x0, y0), sa pointe en (x1, y1)."""
    L = math.hypot(x1 - x0, y1 - y0)
    a = math.degrees(math.atan2(y1 - y0, x1 - x0))
    m = [trait(0, 0, L - 6, 0, "#e0a93a", 4 * ep)]
    nb = 6
    for k in range(nb):
        t = L * 0.6 + k * (L * 0.36) / nb
        m.append(ellipse(t, -7 * ep, 9 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75), rot=-30))
        m.append(ellipse(t, 7 * ep, 9 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75), rot=30))
        m.append(trait(t + 6 * ep, -9 * ep, t + 22 * ep, -16 * ep, "#e0a93a", 1.5))
    m.append(ellipse(L - 2 * ep, 0, 10 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75)))
    return place(m, x0, y0, 1, rot=a)


def rires(x, y, s=1.0, rot=0):
    """Petits traits de chatouille autour d'un point."""
    m = []
    for k, a in enumerate((-60, -20, 20, 60)):
        r0, r1 = 26, 46 + (k % 2) * 8
        ca, sa = math.cos(math.radians(a + rot)), math.sin(math.radians(a + rot))
        m.append(trait(r0 * ca, r0 * sa, r1 * ca, r1 * sa, "#e8590c", 4))
    return place(m, x, y, s)


def chatouille(S, mx, my, s_m, cible, main="tend", **k):
    """Margot en (mx, my), qui pointe son épi jusqu'à `cible` (point de la page)."""
    from fantastique import mains_personne
    (_, _), (hx, hy) = mains_personne(mx, my, s_m, main)
    S.add(personne(mx, my, s_m, bras=main, **{**MARGOT, **k}))
    S.add(epi(hx, hy, *cible, ep=max(s_m, 1.0)))


def champ(S, horizon=520, haut="#74c0fc", bas="#fff3bf", graine=1, soleil_=None, ble_devant=True):
    """Champ de blé sous le ciel, avec des coquelicots."""
    ciel(S, haut, bas)
    if soleil_:
        S.add(soleil(*soleil_))
    collines(S, horizon, "#c0eb75", graine=graine, hauteur=80)
    sol(S, horizon + 40, "#e9c46a", bosse=10, premier=False)
    r = random.Random(graine)
    for k in range(int(70 * (800 - horizon) / 300)):
        yy = r.uniform(horizon + 50, 790)
        prof = (yy - horizon) / (800 - horizon)
        S.add(epi_droit(r.uniform(0, 800), yy, 0.35 + prof * 0.75, r.uniform(-12, 12)))
        if r.random() < 0.12:
            S.add(coquelicot(r.uniform(0, 800), yy + 4, 0.4 + prof * 0.6))


def epi_droit(x, y, s=1.0, rot=0):
    """Tige de blé debout ; (x, y) = pied."""
    m = [trait(0, 0, 0, -110, "#d4a017", 4)]
    for k in range(5):
        yy = -112 + k * 9
        m.append(ellipse(-6, yy, 4.5, 8, "#f6c453", rot=-30) + ellipse(6, yy, 4.5, 8, "#f6c453", rot=30))
    m.append(ellipse(0, -122, 4, 8, "#f6c453"))
    m.append(chemin("M 0 -40 Q 16 -54 22 -72", stroke="#c0a03a", sw=3))
    return place(m, x, y, s, rot=rot)


def coquelicot(x, y, s=1.0):
    return place([trait(0, 0, 0, -80, "#5c940d", 3), cercle(-8, -86, 11, "#f03e3e"), cercle(8, -86, 11, "#e03131"),
                  cercle(0, -94, 11, "#fa5252"), cercle(0, -86, 4, ENCRE)], x, y, s)


def ble_devant(S, graine=5, y0=700):
    """Quelques épis au tout premier plan, dans les coins (repoussoir)."""
    r = random.Random(graine)
    for k in range(8):
        x = r.uniform(-30, 90) if k % 2 else r.uniform(710, 830)
        S.add(epi_droit(x, r.uniform(y0, 830), r.uniform(1.4, 1.9), r.uniform(-10, 10)))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    champ(S, 520, graine=2)
    bx, by, bs = 560, 700, 1.25
    S.add(alouette(bx, by, bs, expr="rire", flip=True, regard=(-1, 0)))
    chatouille(S, 250, 770, 1.35, partie(bx, by, bs, "cou", flip=True), expr="rire", regard=(1, 0))
    S.add(rires(*partie(bx, by, bs, "cou", flip=True), 1.0, rot=180))
    S.add(notes(700, 470, 0.9, "#e8590c"))
    ble_devant(S, 3, 760)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(alouette(210, 255, 0.95, expr="chante", ailes="haut"))
    S.add(notes(330, 80, 0.7, "#e8590c"))
    return S


def p01():
    """Plan large : l'alouette chante tout là-haut ; Margot lève la tête."""
    S = Scene()
    champ(S, 560, haut="#91a7ff", bas="#ffe8cc", graine=4, soleil_=(140, 470, 50))
    S.add(nuage(560, 140, 0.7, opacity=0.8))
    S.add(alouette(480, 280, 0.75, expr="chante", ailes="haut", rot=-10))
    S.add(notes(590, 180, 0.8, "#e8590c"), notes(380, 200, 0.6, "#e8590c"))
    S.add(personne(260, 760, 1.05, expr="bouche_bee", bras="bas", regard=(1, -1), **MARGOT))
    S.add(texte(560, 110, "Tirelire !", 50, "#e8590c", contour="#fff"))
    ble_devant(S, 8, 770)
    return S


def p02():
    """Plan moyen : l'alouette se pose ; Margot brandit son épi."""
    S = Scene()
    champ(S, 500, graine=6)
    bx, by, bs = 580, 730, 1.15
    S.add(alouette(bx, by, bs, expr="surpris", flip=True, regard=(-1, 0)))
    S.add(personne(250, 770, 1.45, expr="malin", bras="tient", regard=(1, 0), **MARGOT))
    from fantastique import mains_personne
    (_, _), (hx, hy) = mains_personne(250, 770, 1.45, "tient")
    S.add(epi(hx, hy, hx + 40, hy - 170, ep=1.3))
    S.add(bulle(560, 150, 460, 120, "Alouette, gentille alouette,\nje te chatouillerai !", 30, pointe=(330, 430)))
    ble_devant(S, 9, 780)
    return S


def scene_chatouille(nom, bx=520, by=720, bs=1.4, mx=200, zoom=None, expr="rire", ailes="bas", graine=7):
    S = Scene()
    champ(S, 470, graine=graine)
    S.add(alouette(bx, by, bs, expr=expr, ailes=ailes, flip=True, regard=(-1, 0)))
    cible = partie(bx, by, bs, nom, flip=True)
    chatouille(S, mx, 790, 1.5, cible, expr="rire", regard=(1, -0.3))
    S.add(rires(*cible, 1.0, rot=180 if nom not in ("pattes",) else 90))
    return S, cible


def p03():
    """Gros plan : la tête."""
    S, (cx, cy) = scene_chatouille("tete")
    S.camera(1.8, cx - 30, cy + 60)
    S.dessus(texte(400, 120, "Et la tête !", 64, "#e8590c", contour="#fff"))
    S.cachette(603, 395, "air")
    return S


def p04():
    """Gros plan serré : le bec."""
    S, (cx, cy) = scene_chatouille("bec", graine=8)
    S.camera(2.3, cx + 20, cy + 10)
    S.dessus(texte(400, 120, "Et le bec !", 64, "#e8590c", contour="#fff"))
    S.cachette(543, 443, "air")
    return S


def p05():
    """Plan moyen : le cou."""
    S, _ = scene_chatouille("cou", bx=540, by=730, bs=1.25, mx=240, graine=9)
    S.add(texte(400, 150, "Et le cou !", 64, "#e8590c", contour="#fff"))
    ble_devant(S, 10, 790)
    return S


def p06():
    """Plan large : les ailes grandes ouvertes, contre le ciel."""
    S = Scene()
    champ(S, 600, graine=10)
    S.add(nuage(150, 150, 0.7), nuage(660, 110, 0.5, opacity=0.8))
    bx, by, bs = 520, 560, 1.15
    S.add(alouette(bx, by, bs, expr="rire", ailes="haut", flip=True, regard=(-1, 0)))
    cible = (bx + 12 * bs, by - 196 * bs)
    chatouille(S, 220, 780, 1.3, cible, main="lance", expr="rire", regard=(1, -1))
    S.add(rires(*cible, 0.9, rot=90))
    S.add(texte(600, 750, "Et les ailes !", 56, "#e8590c", contour="#fff"))
    return S


def p07():
    """Gros plan : le dos."""
    S, (cx, cy) = scene_chatouille("dos", bx=520, by=730, bs=1.4, mx=220, graine=11)
    S.camera(1.9, cx + 10, cy + 40)
    S.dessus(texte(400, 110, "Et le dos !", 64, "#e8590c", contour="#fff"))
    return S


def p08():
    """Plan moyen : perchée sur la main de Margot, l'alouette se fait chatouiller les pattes."""
    S = Scene()
    champ(S, 480, graine=12)
    from fantastique import mains_personne
    mx, my, ms = 300, 790, 1.5
    S.add(personne(mx, my, ms, bras="ouverts", expr="rire", regard=(1, -0.5), **MARGOT))
    (gx, gy), (dx, dy) = mains_personne(mx, my, ms, "ouverts")
    S.add(alouette(dx + 10, dy - 6, 1.15, expr="rire", flip=True, regard=(-1, 0)))
    cible = (dx - 6, dy - 18)
    S.add(epi(gx, gy, *cible, ep=1.2))
    S.add(rires(dx + 10, dy - 10, 0.9, rot=90))
    S.add(texte(400, 130, "Et les pattes !", 60, "#e8590c", contour="#fff"))
    return S


def p09():
    """Gros plan : la queue."""
    S, (cx, cy) = scene_chatouille("queue", bx=560, by=720, bs=1.45, mx=170, graine=13)
    S.camera(1.8, cx + 40, cy + 30)
    S.dessus(texte(400, 110, "Et la queue !", 64, "#e8590c", contour="#fff"))
    S.cachette(433, 772)
    return S


def p10():
    """Plan large : l'alouette rit tant qu'elle roule dans le blé, avec Margot."""
    S = Scene()
    champ(S, 520, graine=14)
    S.add(personne(420, 720, 1.2, expr="rire", bras="ouverts", rot=-78, **MARGOT))
    S.add(alouette(560, 540, 1.0, expr="rire", rot=168, flip=True))
    S.add(epi(470, 700, 620, 640, ep=1.1))
    S.add(texte(560, 330, "Hi hi hi !", 64, "#e8590c", contour="#fff"))
    S.add(texte(260, 420, "Ha ha ha !", 50, "#1c7ed6", contour="#fff"))
    S.add(mouvement(680, 600, 1.0, "#e8590c", rot=200))
    ble_devant(S, 15, 790)
    return S


def p11():
    """Gros plan : l'alouette, l'épi au bec, chatouille le nez de Margot."""
    S = Scene()
    champ(S, 460, graine=16)
    mx, my, ms = 290, 800, 1.7
    S.add(personne(mx, my, ms, expr="rire", bras="bas", regard=(1, 0), **MARGOT))
    nez = (mx + 4 * ms, my - (112 * 1.0 + (134 - 112) * 1.0) * ms)
    bx, by, bs = 600, 700, 1.2
    S.add(alouette(bx, by, bs, expr="malin", flip=True, regard=(-1, 0)))
    bec = partie(bx, by, bs, "bec", flip=True)
    S.add(epi(bec[0] + 8, bec[1], nez[0] + 18, nez[1], ep=1.2))
    S.add(rires(nez[0] + 10, nez[1], 0.7, rot=180))
    S.camera(1.35, 430, 520)
    S.dessus(bulle(560, 110, 360, 90, "À mon tour !", 40, pointe=S.vers_page(bx - 60, by - 170)))
    S.cachette(674, 385, "air")
    return S


def p12():
    """Plan large : le soir, l'alouette remonte dans le ciel ; Margot lui fait au revoir."""
    S = Scene()
    champ(S, 560, haut="#f08c00", bas="#ffd8a8", graine=17, soleil_=(640, 520, 60))
    S.add(alouette(420, 260, 0.7, expr="chante", ailes="haut", rot=-12))
    S.add(notes(520, 170, 0.8, "#fff3bf"))
    S.add(personne(230, 770, 1.15, expr="content", bras="coucou", regard=(1, -1), **MARGOT))
    S.add(texte(560, 110, "À demain !", 50, "#fff3bf", contour="#e8590c"))
    ble_devant(S, 18, 780)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("alouette-seule.svg", vignette),
    ("01-tirelire.svg", p01), ("02-elle-se-pose.svg", p02), ("03-la-tete.svg", p03),
    ("04-le-bec.svg", p04), ("05-le-cou.svg", p05), ("06-les-ailes.svg", p06),
    ("07-le-dos.svg", p07), ("08-les-pattes.svg", p08), ("09-la-queue.svg", p09),
    ("10-on-roule.svg", p10), ("11-a-mon-tour.svg", p11), ("12-a-demain.svg", p12),
]
