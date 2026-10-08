"""Flocon, la fée de l'hiver — chaque saison a sa magie."""
from base import *
from objets import *
from fantastique import *
from sciences import graine_perso

ID = "flocon-saisons"
FLOCON = dict(coiffure="tres_longs", cheveux="blanc", peau="claire", habit="#4dabf7", ailes="#c5f6fa",
              motif_robe="#e7f5ff", acc=("diademe",))
PRIMEVERE = dict(coiffure="boucles", cheveux="brun", peau="foncee", habit="#51cf66", ailes="#ffdeeb",
                 acc=("fleur",), couleur_acc="#f783ac")
MIRABELLE = dict(coiffure="tresses", cheveux="noir", peau="doree", habit="#fcc419", ailes="#fff3bf",
                acc=("fleur",), couleur_acc="#ff922b")
NOISETTE = dict(coiffure="queue", cheveux="roux", peau="brune", habit="#e8590c", ailes="#ffe8cc")

GIVRE = "#e7f5ff"


def _fee(style, etoile, x, y, s, bras, baguette_, k):
    obj = k.pop("objet", None)
    if baguette_ and bras in ("tient", "salut"):
        obj = baguette(68, -146, 0.9, rot=15, etoile=etoile)
    elif baguette_ and bras == "montre":
        obj = baguette(86, -130, 0.9, rot=30, etoile=etoile)
    return personne(x, y, s, bras=bras, objet=obj, **{**style, **k})


def flocon(x, y, s=1.0, bras="tient", baguette_=True, **k):
    return _fee(FLOCON, "#e7f5ff", x, y, s, bras, baguette_, k)


def primevere(x, y, s=1.0, bras="bas", baguette_=False, **k):
    return _fee(PRIMEVERE, "#f783ac", x, y, s, bras, baguette_, k)


def mirabelle(x, y, s=1.0, bras="bas", baguette_=False, **k):
    return _fee(MIRABELLE, OR, x, y, s, bras, baguette_, k)


def noisette(x, y, s=1.0, bras="bas", baguette_=False, **k):
    return _fee(NOISETTE, "#ff922b", x, y, s, bras, baguette_, k)


# ---------------------------------------------------------------------------
# Objets propres à ce livre
# ---------------------------------------------------------------------------

def cristal(x, y, r=30, couleur="#ffffff", rot=0, opacity=1.0):
    """Flocon de neige à six branches."""
    m = []
    sw = max(2.0, r * 0.13)
    for k in range(6):
        a = math.radians(rot + k * 60)
        ca, sa = math.cos(a), math.sin(a)
        m.append(trait(0, 0, ca * r, sa * r, couleur, sw))
        bx, by = ca * r * 0.55, sa * r * 0.55
        for d in (-45, 45):
            b = a + math.radians(d)
            m.append(trait(bx, by, bx + math.cos(b) * r * 0.32, by + math.sin(b) * r * 0.32, couleur, sw * 0.8))
    return place(g(m, opacity=opacity, stroke_linecap="round"), x, y)


def neige_tombe(S, nb=14, graine=1, zone=(0, 0, 800, 600), couleur="#ffffff"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for k in range(nb):
        S.add(cristal(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(9, 18), couleur, rot=r.uniform(0, 60)))


def branche(x, y, s=1.0, etat="bourgeons", flip=False):
    """Branche d'arbre ; etat = "nue", "bourgeons", "geles" ou "fleurs". (x, y) = départ de la branche."""
    brun = "#8d5524"
    m = [chemin("M 0 0 Q 90 -30 200 -70", stroke=brun, sw=14),
         chemin("M 80 -28 Q 100 -80 130 -110", stroke=brun, sw=9),
         chemin("M 150 -52 Q 190 -40 220 -14", stroke=brun, sw=8),
         chemin("M 40 -12 Q 40 -50 60 -72", stroke=brun, sw=7)]
    bouts = [(204, -74, 20), (132, -114, -20), (222, -12, 60), (62, -76, -30)]
    for bx, by, r in bouts:
        if etat == "bourgeons":
            m.append(ellipse(bx, by, 10, 16, "#69db7c", rot=r))
            m.append(ellipse(bx + math.sin(math.radians(r)) * 10, by - math.cos(math.radians(r)) * 10, 6, 7, "#faa2c1"))
        elif etat == "geles":
            m.append(ellipse(bx, by, 11, 17, "#a5d8ff", rot=r, stroke="#ffffff", stroke_width=3))
            m.append(poly([(bx - 8, by + 14), (bx - 4, by + 34), (bx, by + 14)], "#d0ebff"))
            m.append(poly([(bx + 2, by + 14), (bx + 6, by + 28), (bx + 10, by + 12)], "#d0ebff"))
            m.append(cristal(bx + 14, by - 18, 9, "#ffffff"))
        elif etat == "fleurs":
            for k in range(5):
                a = math.radians(k * 72 + r)
                m.append(cercle(bx + math.cos(a) * 12, by + math.sin(a) * 12, 10, "#fcc2d7"))
            m.append(cercle(bx, by, 7, "#ffd43b"))
    # la neige posée sur la branche gelée
    if etat == "geles":
        m.append(chemin("M 10 -10 Q 90 -46 196 -82 Q 120 -48 10 -4 Z", "#ffffff"))
    return place(m, x, y, s, flip=flip)


def perce_neige(x, y, s=1.0):
    """Perce-neige : petite fleur blanche penchée ; (x, y) = pied de la tige."""
    m = [ellipse(-14, -40, 8, 42, "#40c057", rot=-10), ellipse(14, -36, 8, 36, "#2f9e44", rot=12),
         chemin("M 0 0 Q 4 -80 0 -112 Q -4 -128 -22 -128", stroke="#51cf66", sw=6),
         cercle(-22, -124, 6, "#51cf66"),
         ellipse(-36, -100, 9, 20, "#ffffff", rot=22, stroke="#dee2e6", stroke_width=2),
         ellipse(-8, -100, 9, 20, "#ffffff", rot=-22, stroke="#dee2e6", stroke_width=2),
         ellipse(-22, -98, 10, 23, "#ffffff", stroke="#dee2e6", stroke_width=2),
         chemin("M -28 -80 Q -22 -74 -16 -80", stroke="#69db7c", sw=3)]
    return place(m, x, y, s)


def feuille(x, y, s=1.0, couleur="#f76707", rot=0):
    m = [chemin("M 0 -26 Q 22 -10 0 26 Q -22 -10 0 -26 Z", couleur), trait(0, -20, 0, 30, assombrir(couleur, 0.75), 2.5)]
    return place(m, x, y, s, rot=rot)


def nuage_assis(x, y, s=1.0):
    """Gros nuage où une fée peut s'asseoir (à dessiner devant ses jambes)."""
    return nuage(x, y, s, "#ffffff", ombre="#d0ebff")


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def hiver(S, sol_y=640, sapins=True):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, sol_y + 20, "#f1f3f5", graine=3, hauteur=90)
    sol(S, sol_y, "#ffffff", couleur2="#e7f5ff", y2=sol_y + 90)
    if sapins:
        S.add(sapin(90, sol_y + 30, 1.0, neige=True), sapin(720, sol_y + 40, 1.2, neige=True), sapin(640, sol_y + 20, 0.7, neige=True))


def printemps(S, sol_y=640, neige_restante=False):
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, sol_y + 20, "#b2f2bb", graine=5, hauteur=90)
    sol(S, sol_y, "#8ce99a", couleur2="#69db7c", y2=sol_y + 90)
    if neige_restante:
        for x, y, rx in [(140, sol_y + 60, 90), (560, sol_y + 110, 120), (700, sol_y + 30, 60)]:
            S.add(ellipse(x, y, rx, 18, "#ffffff", opacity=0.9))
    S.add(herbe(250, sol_y + 40, 1.2, "#40c057"), herbe(620, sol_y + 70, 1.0, "#40c057"))


def ciel_nuages(S):
    ciel(S, "#91a7ff", "#e7f5ff")
    S.add(nuage(130, 200, 0.9, "#ffffff", opacity=0.6), nuage(680, 140, 0.8, "#ffffff", opacity=0.6))
    S.add(rect(0, 640, 800, 160, "#ffffff"))
    for k in range(9):
        S.add(cercle(k * 100, 650, 70, "#ffffff"))
    S.add(rect(0, 700, 800, 100, "#edf2ff"))


def roue_saisons(cx, cy, r):
    """Roue des saisons : hiver (haut gauche), printemps, été, automne, dans le sens des aiguilles d'une montre."""
    parts = [(-180, -90, "#d0ebff", "hiver"), (-90, 0, "#d3f9d8", "printemps"),
             (0, 90, "#fff3bf", "été"), (90, 180, "#ffe8cc", "automne")]
    m = []
    for a0, a1, c, nom in parts:
        r0, r1 = math.radians(a0), math.radians(a1)
        d = (f"M {cx} {cy} L {n(cx + r * math.cos(r0))} {n(cy + r * math.sin(r0))} "
             f"A {r} {r} 0 0 1 {n(cx + r * math.cos(r1))} {n(cy + r * math.sin(r1))} Z")
        m.append(chemin(d, c, stroke="#ffffff", sw=8))
    # flèches qui tournent
    R = r + 22
    for a0 in (-170, -80, 10, 100):
        a1 = a0 + 70
        r0, r1 = math.radians(a0), math.radians(a1)
        d = f"M {n(cx + R * math.cos(r0))} {n(cy + R * math.sin(r0))} A {R} {R} 0 0 1 {n(cx + R * math.cos(r1))} {n(cy + R * math.sin(r1))}"
        m.append(chemin(d, stroke="#5c7cfa", sw=7))
        ex, ey = cx + R * math.cos(r1), cy + R * math.sin(r1)
        t = r1 + math.pi / 2
        pts = [(ex + math.cos(t) * 18, ey + math.sin(t) * 18),
               (ex + math.cos(t + 2.6) * 14, ey + math.sin(t + 2.6) * 14),
               (ex + math.cos(t - 2.6) * 14, ey + math.sin(t - 2.6) * 14)]
        m.append(poly(pts, "#5c7cfa"))
    return g(m)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    hiver(S, 650)
    neige_tombe(S, 18, graine=2, zone=(20, 20, 780, 600))
    S.add(flocon(380, 560, 1.75, expr="rire", bras="tient"))
    S.add(etincelles(530, 230, 1.0, graine=4, couleur="#ffffff"))
    S.add(perce_neige(600, 760, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 140, 160, 115, "#e7f5ff"))
    S.add(ellipse(200, 232, 150, 30, "#ffffff", stroke="#d0ebff", stroke_width=3))
    S.add(perce_neige(210, 236, 1.3))
    S.add(cristal(90, 90, 22, "#a5d8ff"), cristal(320, 70, 16, "#a5d8ff"), cristal(310, 170, 12, "#a5d8ff"))
    return S


def p01():
    S = Scene()
    hiver(S, 650)
    S.add(maison(400, 700, 0.7, mur="#ffe8cc", toit="#ffffff"))
    neige_tombe(S, 22, graine=5, zone=(20, 420, 780, 640))
    S.add(nuage(400, 370, 2.1, "#ffffff", ombre="#d0ebff"))
    S.add(flocon(400, 380, 1.15, expr="rire", bras="tient"))
    S.add(nuage(400, 410, 1.6, "#ffffff"))
    S.add(texte(400, 80, "Flocons, flocons, dansez !", 50, "#1971c2", contour="#ffffff"))
    return S


def p02():
    S = Scene()
    hiver(S, 660, sapins=False)
    S.add(sapin(90, 700, 1.0, neige=True), sapin(720, 700, 1.1, neige=True))
    S.add(flocon(250, 560, 1.3, expr="timide", bras="pense", baguette_=False, regard=(1, -1)))
    contenu = g([fleur(500, 300, 1.4, "#ff8787", tige=70), fleur(580, 290, 1.6, "#ffd43b", "#ff922b", tige=80),
                 fleur(660, 300, 1.3, "#cc5de8", tige=70), fleur(540, 310, 1.0, "#74c0fc", tige=50),
                 fleur(620, 312, 1.0, "#f783ac", tige=50)])
    S.add(pensee(580, 230, 150, contenu, depuis=(320, 360)))
    return S


def p03():
    S = Scene()
    printemps(S, 640, neige_restante=True)
    S.add(soleil(680, 120, 60))
    S.add(arbre(700, 690, 1.2, "#d8f5a2", "#c0eb75"))
    S.add(branche(690, 540, 0.85, "bourgeons", flip=True))
    S.add(flocon(170, 720, 1.2, expr="surpris", bras="bas", baguette_=False, regard=(1, 0)))
    S.add(primevere(420, 740, 1.35, expr="content", bras="salut", baguette_=True, flip=True))
    S.add(bulle(360, 150, 520, 110, "Merci, Flocon !\nMaintenant, c'est mon tour.", 36, pointe=(420, 420)))
    return S


def p04():
    S = Scene()
    printemps(S, 660)
    S.add(soleil(120, 120, 50))
    S.add(flocon(520, 420, 1.2, expr="malin", bras="bas", baguette_=False, regard=(-1, 0)))
    S.add(nuage(500, 430, 2.4, "#ffffff", ombre="#d0ebff"))
    S.add(primevere(200, 760, 0.9, expr="sourire", bras="tient", baguette_=True))
    S.add(bulle(420, 120, 520, 110, "Je veux voir les fleurs,\nmoi aussi !", 38, pointe=(540, 220)))
    return S


def p05():
    S = Scene()
    printemps(S, 660)
    ciel(S, "#a5c8e8", "#e7f5ff")
    sol(S, 660, "#c3e6cb", couleur2="#ffffff", y2=740)
    S.add(arbre(620, 700, 1.1, "#c3e6cb", "#a9d8b5"))
    S.add(branche(612, 580, 1.0, "geles", flip=True))
    neige_tombe(S, 26, graine=9, zone=(20, 220, 780, 700))
    S.add(flocon(200, 520, 1.2, expr="oups", bras="tient", regard=(1, 0)))
    S.add(texte(470, 120, "Oh non !", 70, "#1971c2", contour="#ffffff"))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5c8e8", "#e7f5ff")
    sol(S, 640, "#c3e6cb", couleur2="#ffffff", y2=720)
    S.add(rect(-10, 180, 56, 470, "#8d5524", rx=10))
    S.add(branche(40, 330, 1.3, "geles"))
    S.add(primevere(560, 760, 1.4, expr="triste", bras="porte", objet=ellipse(0, -80, 12, 18, "#a5d8ff", stroke="#ffffff", stroke_width=3)))
    S.add(flocon(230, 760, 1.4, expr="pleure", bras="yeux", baguette_=False, larmes=True))
    S.cachette(730, 260, "air")
    return S


def p07():
    S = Scene()
    printemps(S, 650)
    S.add(soleil(120, 110, 55))
    S.add(branche(10, 600, 0.95, "bourgeons"))
    for x, y in [(150, 520), (110, 480), (200, 560)]:
        S.add(goutte(x, y, 1.0, "#74c0fc"))
    S.add(primevere(290, 760, 1.15, expr="content", bras="salut", baguette_=True))
    S.add(nuage(380, 150, 0.5, "#ffffff"), nuage(720, 470, 0.6, "#ffffff"))
    S.add(flocon(600, 330, 1.2, expr="sourire", bras="salut", flip=True))
    S.add(bulle(600, 560, 380, 100, "Chacune son tour !", 38, pointe=(600, 390)))
    return S


def p08():
    S = Scene()
    ciel_nuages(S)
    S.add(mirabelle(190, 690, 1.3, expr="rire", bras="ouverts"))
    S.add(flocon(400, 700, 1.35, expr="content", bras="bas", baguette_=False))
    S.add(noisette(610, 690, 1.3, expr="rire", bras="ouverts"))
    for x, y, c, rr in [(560, 300, "#f76707", 20), (700, 360, "#fab005", -30), (640, 250, "#e8590c", 60)]:
        S.add(feuille(x, y, 1.0, c, rot=rr))
    S.add(soleil(140, 260, 40, "#ffd43b"))
    S.add(bulle(400, 110, 600, 110, "Nous aussi, nous attendons\nnotre tour !", 38, pointe=(560, 370)))
    return S


def p09():
    S = Scene()
    fond(S, "#f8f9ff")
    cx, cy, r = 400, 460, 250
    S.add(roue_saisons(cx, cy, r))
    S.add(flocon(310, 470, 0.5, expr="content", bras="tient"))
    S.add(primevere(490, 470, 0.5, expr="content", bras="salut", baguette_=True))
    S.add(mirabelle(490, 650, 0.5, expr="rire", bras="haut"))
    S.add(noisette(310, 650, 0.5, expr="rire", bras="haut"))
    S.add(cristal(250, 340, 18, "#74c0fc"), fleur(560, 360, 0.9, "#f783ac", tige=30),
          soleil(560, 560, 18, rayons=True), feuille(240, 560, 0.8, "#f76707", rot=30))
    d = (r + 60) * 0.707
    for (sx, sy), nom, c in [((-1, -1), "hiver", "#1971c2"), ((1, -1), "printemps", "#2b8a3e"),
                             ((1, 1), "été", "#e67700"), ((-1, 1), "automne", "#d9480f")]:
        S.add(texte(cx + sx * d, cy + sy * d + 12, nom, 38, c, contour="#ffffff"))
    S.add(texte(400, 80, "Chacune son tour !", 54, "#5c7cfa", contour="#ffffff"))
    S.cachette(190, 500, "air")
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 360, 800, 440, "#a0693a"))
    S.add(rect(0, 360, 800, 30, "#8a5a32"))
    S.add(chemin("M 0 370 Q 200 250 400 280 Q 600 300 800 260 L 800 380 L 0 380 Z", "#ffffff"))
    S.add(chemin("M 0 360 Q 200 260 400 290 Q 600 310 800 270", stroke="#dbe4ff", sw=4))
    neige_tombe(S, 10, graine=3, zone=(30, 30, 770, 220), couleur="#ffffff")
    S.add(flocon(260, 300, 0.95, expr="bouche_bee", bras="bas", baguette_=False, regard=(1, 1)))
    S.add(noisette(560, 300, 0.95, expr="sourire", bras="montre", flip=True))
    # sous la terre : des graines et un bulbe qui dorment
    S.add(graine_perso(180, 560, 0.7, expr="dort"))
    S.add(graine_perso(620, 600, 0.6, expr="dort", rot=-20))
    S.add(ellipse(400, 560, 50, 42, "#e9d8c4"), chemin("M 386 520 Q 400 470 414 520", "#e9d8c4"))
    S.add(chemin("M 400 476 Q 404 430 400 400", stroke="#69db7c", sw=7))
    for dx in (-30, -10, 10, 30):
        S.add(chemin(f"M {400 + dx * 0.6} 600 Q {400 + dx} 640 {400 + dx * 1.4} 680", stroke="#e9d8c4", sw=4))
    S.add(zzz(470, 520, 0.9), zzz(250, 470, 0.8))
    S.add(texte(400, 760, "Sous la neige, les graines dorment au chaud.", 32, "#ffffff"))
    return S


def p11():
    S = Scene()
    # moitié gauche : l'été ; moitié droite : l'automne
    S.add(rect(0, 0, 400, 800, S.degrade(["#74c0fc", "#fff3bf"])))
    S.add(rect(400, 0, 400, 800, S.degrade(["#ffc078", "#fff4e6"])))
    S.add(rect(0, 600, 400, 200, "#ffe066"), rect(400, 600, 400, 200, "#d9a066"))
    for k in range(9):
        S.add(trait(20 + k * 45, 600, 26 + k * 45, 540, "#f59f00", 6), ellipse(26 + k * 45, 536, 7, 16, "#fab005"))
    S.add(soleil(90, 360, 45))
    S.add(arbre(250, 640, 0.9, "#40c057", "#2f9e44", fruits="#fa5252"))
    S.add(arbre(600, 640, 0.95, "#ff922b", "#f76707"))
    for x, y, c, rr in [(520, 470, "#f76707", 20), (700, 520, "#fab005", -40), (740, 420, "#e8590c", 70),
                        (480, 580, "#fab005", 10), (690, 640, "#e8590c", 90), (560, 690, "#f76707", -30)]:
        S.add(feuille(x, y, 1.0, c, rot=rr))
    S.add(rect(397, 230, 6, 570, "#ffffff"))
    S.add(nuage(400, 200, 2.0, "#ffffff", ombre="#d0ebff"))
    S.add(flocon(400, 200, 0.9, expr="content", bras="pense", baguette_=False, regard=(0, 1)))
    S.add(nuage(400, 230, 1.5, "#ffffff"))
    S.add(texte(200, 760, "l'été", 50, "#e67700", contour="#ffffff"), texte(600, 760, "l'automne", 50, "#d9480f", contour="#ffffff"))
    S.cachette(70, 710, "air")
    return S


def p12():
    S = Scene()
    hiver(S, 620, sapins=False)
    S.add(sapin(80, 680, 1.0, neige=True), sapin(730, 690, 1.1, neige=True))
    neige_tombe(S, 10, graine=11, zone=(30, 40, 770, 300))
    S.add(cercle(380, 600, 110, "#fff9db", opacity=0.5))
    S.add(flocon(170, 740, 1.3, expr="rire", bras="joues", baguette_=False, regard=(1, 0)))
    S.add(primevere(640, 750, 1.3, expr="content", bras="montre", baguette_=True, flip=True))
    S.add(ellipse(400, 732, 120, 22, "#e7f5ff"))
    S.add(perce_neige(420, 740, 2.0))
    S.add(coeur(400, 330, 1.4, "#f783ac"), etincelles(400, 450, 1.0, graine=6, couleur="#ffd43b"))
    S.add(bulle(400, 130, 520, 110, "C'est un perce-neige.\nJe l'ai gardé pour toi !", 36, pointe=(560, 400)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("perce-neige.svg", vignette),
    ("01-la-fee-de-l-hiver.svg", p01), ("02-le-reve.svg", p02), ("03-le-printemps.svg", p03),
    ("04-cachee.svg", p04), ("05-oh-non.svg", p05), ("06-bourgeons-geles.svg", p06),
    ("07-chacune-son-tour.svg", p07), ("08-les-soeurs.svg", p08), ("09-la-roue.svg", p09),
    ("10-sous-la-neige.svg", p10), ("11-patience.svg", p11), ("12-la-surprise.svg", p12),
]
