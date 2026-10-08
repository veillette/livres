"""Les bébés tortues de mer — la ponte et l'éclosion.

La tortue de mer nage avec ses nageoires et remonte respirer de l'air. La
nuit, la femelle revient sur la plage où elle est née, creuse un trou avec
ses nageoires arrière et y pond une centaine d'œufs mous, qu'elle recouvre
avant de repartir. La chaleur du sable couve les œufs environ deux mois (plus
chaud : plutôt des femelles). Les bébés sortent ensemble la nuit et filent
vers la mer, guidés par l'horizon plus clair au-dessus de l'eau. Les
lumières de la plage et les sacs en plastique (pris pour des méduses) les
mettent en danger.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant
from fantastique import algue, corail, bulles_eau, ocean

ID = "tortue-mer"
CARAPACE = "#8d6e4a"
CARAPACE2 = "#a9805b"
PEAU = "#c9b38a"


# --- Personnages ------------------------------------------------------------

def tortue_nage(x, y, s=1.0, flip=False, rot=0, expr="sourire", regard=(1, 0), couleur=CARAPACE, peau=PEAU):
    """Tortue de mer qui nage, de profil, tête à droite ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = [chemin("M -70 10 Q -120 20 -150 50 Q -110 50 -70 30 Z", peau),
         chemin("M 40 10 Q 30 60 -40 120 Q 10 110 70 30 Z", _assombrir(peau, 0.9)),
         chemin("M -110 10 Q -110 -80 0 -86 Q 100 -86 110 10 Z", couleur),
         rect(-116, 2, 232, 18, eclaircir(couleur, 0.5), rx=9)]
    for px, py in [(-60, -34), (0, -56), (60, -34), (-30, -10), (30, -10)]:
        m.append(poly([(px - 24, py), (px - 12, py - 20), (px + 12, py - 20), (px + 24, py), (px + 12, py + 18), (px - 12, py + 18)],
                      fonce, opacity=0.5))
    m.append(chemin("M 100 0 Q 130 -20 150 -20 Q 190 -18 192 6 Q 190 30 150 28 Q 120 26 100 14 Z", peau))
    for px, py in [(140, -6), (156, 12), (172, -10)]:
        m.append(cercle(px, py, 5, _assombrir(peau, 0.85)))
    m.append(chemin("M 50 14 Q 60 70 10 150 Q 60 130 96 30 Z", peau))
    m.append(oeil(166, -4, ys, regard, taille=0.8))
    m.append(joue(178, 12, 0.6))
    m.append(place(bouche(0, 0, bs, 0.5), 184, 14))
    return place(m, x, y, s, flip=flip, rot=rot)


def tortue_dessus(x, y, s=1.0, rot=0, couleur=CARAPACE, peau=PEAU, expr="sourire", bebe=False):
    """Tortue de mer vue de dessus, tête vers le haut ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    if bebe:
        couleur, peau = "#495057", "#6c757d"
    fonce = _assombrir(couleur, 0.8)
    m = []
    for sgn in (-1, 1):
        m.append(chemin(f"M {sgn * 40} -30 Q {sgn * 120} -60 {sgn * 150} -10 Q {sgn * 110} -16 {sgn * 50} 10 Z", peau))
        m.append(ellipse(sgn * 46, 74, 30, 16, peau, rot=sgn * 40))
    m.append(ellipse(0, 10, 72, 92, couleur))
    for px, py in [(0, -30), (0, 20), (0, 66), (-40, -10), (40, -10), (-40, 44), (40, 44)]:
        m.append(poly([(px - 18, py), (px - 9, py - 16), (px + 9, py - 16), (px + 18, py), (px + 9, py + 16), (px - 9, py + 16)],
                      fonce, opacity=0.5))
    m.append(ellipse(0, -100, 30, 34, peau))
    if ys in ("heureux", "fermes"):
        m.append(oeil(-14, -106, ys, (0, 0), taille=0.6) + oeil(14, -106, ys, (0, 0), taille=0.6))
    else:
        m.append(cercle(-14, -108, 5, ENCRE) + cercle(14, -108, 5, ENCRE) + cercle(-12, -110, 1.6, "#fff") + cercle(16, -110, 1.6, "#fff"))
    m.append(place(bouche(0, 0, bs, 0.5), 0, -90))
    return place(m, x, y, s, rot=rot)


def meduse(x, y, s=1.0, couleur="#e599f7"):
    m = [chemin("M -40 0 Q -40 -50 0 -52 Q 40 -50 40 0 Q 20 8 0 2 Q -20 8 -40 0 Z", couleur, opacity=0.8)]
    for k in range(5):
        px = -30 + k * 15
        m.append(chemin(f"M {px} 2 q 8 20 0 40 q -8 20 0 40", stroke=couleur, sw=4, opacity=0.7))
    return place(m, x, y, s)


def sac_plastique(x, y, s=1.0):
    m = [chemin("M -36 -40 L 36 -40 L 40 30 Q 0 46 -40 30 Z", "#f8f9fa", opacity=0.75, stroke="#dee2e6", sw=2),
         chemin("M -30 -40 Q -26 -66 -10 -40 M 10 -40 Q 26 -66 30 -40", stroke="#dee2e6", sw=6),
         chemin("M -40 30 q 10 20 -4 40 M 0 38 q 6 20 -4 40", stroke="#dee2e6", sw=3)]
    return place(m, x, y, s)


def oeuf_tortue(x, y, s=1.0):
    return place([cercle(0, 0, 14, "#fff9f0", stroke="#e9ddc8", stroke_width=2), cercle(-4, -4, 4, "#ffffff")], x, y, s)


def tas_oeufs(cx, cy, nb=24, graine=1, s=1.0):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        m.append(oeuf_tortue(cx + r.uniform(-60, 60) * s, cy + r.uniform(-40, 40) * s, s * r.uniform(0.9, 1.1)))
    return g(m)


def coupe_plage(S, y=330, nuit_=False):
    """Coupe de la plage : sable en dessous, ciel et mer au-dessus."""
    if nuit_:
        nuit(S)
        etoiles(S, 30, 3, (0, 0, 800, y - 100))
    else:
        S.add(rect(0, 0, 800, y, S.degrade(["#74c0fc", "#fff3bf"])))
    S.add(rect(0, y - 90, 800, 80, "#1c7ed6" if not nuit_ else "#1b2a5c"))
    S.add(rect(0, y - 14, 800, 820 - y, S.degrade(["#f4d58d", "#d9a441"]) if not nuit_ else "#8c7b55"))
    r = random.Random(7)
    for _ in range(40):
        S.add(cercle(r.uniform(0, 800), r.uniform(y, 800), r.uniform(2, 4), "#c99a3a" if not nuit_ else "#6d6044"))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    plage(S, 520, haut="#74c0fc", bas="#fff3bf")
    S.add(tortue_dessus(300, 680, 0.95, rot=-30, expr="content"))
    for x, y, r in [(520, 640, -20), (610, 710, -10), (470, 740, -35), (690, 620, 0)]:
        S.add(tortue_dessus(x, y, 0.32, rot=r, bebe=True, expr="rire"))
    S.add(soleil(660, 120, 50))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tortue_nage(190, 140, 0.9, expr="content"))
    return S


def p01():
    S = Scene()
    ocean(S, "#4dabf7", "#1864ab", y_sable=700)
    S.add(algue(80, 720, 1.2), corail(700, 720, 1.2), algue(620, 720, 0.9, "#37b24d", graine=4))
    S.add(tortue_nage(380, 380, 1.4, rot=-8, expr="content"))
    S.add(poisson_simple(150, 220, 0.8), poisson_simple(200, 260, 0.6), poisson_simple(640, 560, 0.7, flip=True))
    return S


def p02():
    S = Scene()
    S.add(rect(0, 0, 800, 300, S.degrade(["#74c0fc", "#e7f5ff"])))
    S.add(rect(0, 300, 800, 500, S.degrade(["#4dabf7", "#1864ab"])))
    S.add(tortue_nage(400, 320, 1.3, rot=-20, expr="content"))
    S.add(rect(0, 300, 800, 500, "#1864ab", opacity=0.25))
    S.add(chemin("M 0 300 q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0",
                 stroke="#d0ebff", sw=6))
    S.add(texte(620, 170, "Pfff !", 60, "#1864ab", contour="#fff"))
    S.add(bulles_eau(260, 560, 1.4))
    S.cachette(730, 380, "poisson")
    return S


def p03():
    S = Scene()
    plage(S, 470, nuit_=True, lune_=560)
    S.add(tortue_dessus(330, 640, 1.1, rot=-170, expr="concentre"))
    for k in range(5):
        S.add(chemin(f"M {300 - 30 + (k % 2) * 60} {500 - k * 0} l 0 0", stroke="#6d6044", sw=1))
    S.add(g([trait(300 + (k % 2) * 60, 500 - k * 26 + 260, 300 + (k % 2) * 60 + 10, 512 - k * 26 + 260, "#6d6044", 6) for k in range(6)]))
    return S


def p04():
    S = Scene()
    coupe_plage(S, 330, nuit_=True)
    S.add(lune(150, 90, 34))
    S.add(chemin("M 300 330 Q 300 560 400 560 Q 500 560 500 330 Z", "#6d6044"))
    S.add(tas_oeufs(400, 500, 28, 1, 0.9))
    S.add(tortue_dessus(400, 230, 0.85, rot=0, expr="concentre"))
    S.add(etiquette(640, 520, "une centaine", 32, "#fff3bf", fond="#6d6044"), etiquette(640, 560, "d'œufs !", 32, "#fff3bf", fond="#6d6044"))
    S.cachette(730, 290, "air")
    return S


def p05():
    S = Scene()
    plage(S, 470, nuit_=True, lune_=400)
    S.add(tortue_dessus(400, 600, 0.9, rot=0, expr="content"))
    S.add(ellipse(400, 760, 90, 24, "#a39470"))
    S.add(texte(400, 290, "Au revoir !", 50, "#fff3bf"))
    return S


def p06():
    S = Scene()
    coupe_plage(S, 240)
    S.add(soleil(660, 70, 45))
    S.add(tas_oeufs(400, 560, 32, 2, 1.2))
    for k in range(5):
        S.add(chemin(f"M {150 + k * 120} 330 c 14 -8 -14 -16 0 -24 c 14 -8 -14 -16 0 -24 c 14 -8 -14 -16 0 -24", stroke="#fa5252", sw=5, opacity=0.6))
    S.add(texte(400, 420, "bien au chaud…", 44, "#e8590c", contour="#fff3bf"))
    S.add(loupe(170, 640, 90, [rect(80, 550, 180, 180, "#fff9f0"), cercle(170, 640, 70, "#fff9f0"),
                                place(tortue_dessus(0, 0, 0.5, bebe=True, expr="dort"), 170, 650, 1.0, rot=120)],
                fond="#fff9f0", rot=-130))
    S.cachette(730, 180, "air")
    return S


def p07():
    S = Scene()
    coupe_plage(S, 420, nuit_=True)
    S.add(lune(640, 100, 36))
    S.add(chemin("M 300 420 Q 300 640 400 650 Q 500 640 500 420 Z", "#6d6044"))
    S.add(tas_oeufs(400, 600, 8, 3, 0.9))
    for x, y, r in [(360, 540, -10), (440, 520, 20), (400, 470, 0), (330, 410, -20), (470, 400, 25), (400, 360, 5)]:
        S.add(tortue_dessus(x, y, 0.3, rot=r, bebe=True, expr="rire"))
    S.add(texte(400, 250, "Hop ! Hop !", 50, "#fff3bf"))
    return S


def p08():
    S = Scene()
    plage(S, 470, nuit_=True, lune_=420)
    S.add(fleche(400, 760, 400, 520, "#fff3bf", 7, 24))
    r = random.Random(8)
    for k in range(10):
        S.add(tortue_dessus(120 + k * 62 + r.uniform(-10, 10), 560 + r.uniform(0, 200), 0.3, rot=r.uniform(-25, 25), bebe=True, expr="content"))
    return S


def p09():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#1c7ed6", "#0b3d6b"])))
    S.add(rect(0, 0, 800, 70, "#1b2a5c"))
    S.add(chemin("M 0 70 q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0",
                 stroke="#d0ebff", sw=6))
    for x, y, r in [(200, 250, -10), (420, 380, 5), (620, 220, -15), (330, 560, 10), (560, 620, -5)]:
        S.add(tortue_nage(x, y, 0.45, rot=r, expr="rire", couleur="#495057", peau="#6c757d"))
    S.add(bulles_eau(700, 450, 1.0))
    S.cachette(730, 100, "poisson")
    return S


def p10():
    S = Scene()
    plage(S, 470)
    S.add(soleil(660, 110, 50))
    S.add(enfant(250, 760, 1.5, expr="content", bras="porte", habit="#12b886", jambes="#364fc7", coiffure="tresses",
                 objet=sac_plastique(0, -70, 0.8)))
    S.add(enfant(520, 760, 1.4, expr="sourire", bras="tient", habit="#fab005", jambes="#e8590c",
                 objet=g([rect(52, -150, 34, 44, "#868e96", rx=6)])))
    S.add(meduse(680, 360, 0.9), sac_plastique(130, 330, 0.8))
    S.add(texte(400, 210, "On ramasse !", 50, "#099268", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tortue-seule.svg", vignette),
    ("01-dans-la-mer.svg", p01), ("02-respirer.svg", p02), ("03-la-plage.svg", p03),
    ("04-la-ponte.svg", p04), ("05-au-revoir.svg", p05), ("06-sous-le-sable.svg", p06),
    ("07-l-eclosion.svg", p07), ("08-vers-la-mer.svg", p08), ("09-dans-les-vagues.svg", p09),
    ("10-les-aider.svg", p10),
]
