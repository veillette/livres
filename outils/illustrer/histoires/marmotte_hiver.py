"""La marmotte dort tout l'hiver — l'hibernation de la marmotte des Alpes.

L'été, dans les alpages, les marmottes mangent beaucoup d'herbes et de fleurs
pour faire des réserves de graisse. Une sentinelle debout pousse un cri
perçant quand l'aigle approche, et toutes filent au terrier. À l'automne, la
famille tapisse une chambre de foin, bouche l'entrée et hiberne serrée en
boule, environ six mois : le cœur bat très lentement et le corps se refroidit.
Elles se réveillent un peu de temps en temps. Au printemps, elles sortent
maigres ; les marmottons naissent dans le terrier et sortent au début de l'été.
"""
from base import *
from base import _assombrir
from animaux import *
from objets import aigle

ID = "marmotte-hiver"
POIL = "#a9805b"
POIL_F = "#7c5a3c"
CLAIR = "#e9d3b5"


# --- Personnages ------------------------------------------------------------

def marmotte(x, y, s=1.0, flip=False, expr="sourire", regard=(0, 0), bras="bas", grosse=1.0, objet=None, crie=False):
    """Marmotte debout sur ses pattes arrière, vue de face ; (x, y) = sous les
    pattes. `grosse` > 1 : bien dodue (fin d'été) ; < 1 : maigre (printemps)."""
    ys, bs, ss = EXPRESSIONS[expr]
    G = grosse
    m = [chemin("M 20 -20 Q 60 -10 62 -40", stroke=POIL_F, sw=16),
         ellipse(-26, -8, 22, 11, POIL_F), ellipse(26, -8, 22, 11, POIL_F),
         ellipse(0, -76, 56 * G, 74, POIL), ellipse(0, -66, 36 * G, 52, CLAIR)]
    mains = {"bas": [(-26, -100), (26, -100)], "porte": [(-18, -108), (18, -108)], "haut": [(-74, -196), (74, -196)],
             "bouche": [(-12, -140), (12, -140)]}[bras]
    for sgn, (hx, hy) in zip((-1, 1), mains):
        if bras == "haut":
            m.append(chemin(f"M {sgn * 34} -120 Q {sgn * 70} -140 {hx} {hy}", stroke=_assombrir(POIL, 0.92), sw=16))
        else:
            m.append(chemin(f"M {sgn * 30} -120 Q {sgn * 40} {(hy - 120) / 2 - 50} {hx} {hy}", stroke=_assombrir(POIL, 0.92), sw=16))
    if objet:
        m.append(objet)
    for hx, hy in mains:
        m.append(cercle(hx, hy, 10, POIL_F))
    m.append(cercle(-34, -194, 13, POIL_F) + cercle(34, -194, 13, POIL_F))
    m.append(ellipse(0, -164, 48, 44, POIL))
    m.append(chemin("M -42 -180 Q 0 -222 42 -180 Q 20 -188 0 -186 Q -20 -188 -42 -180 Z", POIL_F))
    m.append(ellipse(0, -140, 28, 20, CLAIR))
    m.append(ellipse(0, -150, 9, 6, ENCRE))
    m.append(oeil(-18, -172, ys, regard, taille=0.85) + oeil(18, -172, ys, regard, taille=0.85))
    m.append(sourcils(18, -172, ss))
    m.append(joue(-30, -150, 0.8) + joue(30, -150, 0.8))
    if crie or bs in ("ouverte", "crie"):
        m.append(ellipse(0, -128, 9, 10, ROUGE_BOUCHE))
        m.append(rect(-6, -138, 12, 8, "#fff9db", rx=2))
    else:
        m.append(place(bouche(0, 0, bs, 0.7), 0, -142))
        m.append(rect(-6, -138, 12, 10, "#fff9db", rx=2, stroke="#e9ecef", stroke_width=1))
    return place(m, x, y, s, flip=flip)


def marmotte_court(x, y, s=1.0, flip=False, expr="surpris"):
    """Marmotte qui court à quatre pattes, de profil, tête à droite."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -50 -40 Q -90 -50 -100 -30", stroke=POIL_F, sw=16),
         chemin("M -30 -30 Q -60 -10 -76 -6", stroke=POIL_F, sw=16), chemin("M 30 -34 Q 54 -16 70 -8", stroke=POIL_F, sw=14),
         ellipse(0, -50, 58, 32, POIL), ellipse(4, -38, 40, 16, CLAIR),
         cercle(48, -92, 12, POIL_F), ellipse(62, -72, 34, 28, POIL), ellipse(82, -66, 16, 12, CLAIR),
         ellipse(94, -72, 5, 4, ENCRE), oeil(66, -80, ys, (1, 0), taille=0.8), joue(78, -62, 0.6)]
    return place(m, x, y, s, flip=flip)


def marmotte_dort(x, y, s=1.0, rot=0):
    """Marmotte roulée en boule, endormie ; (x, y) = centre."""
    m = [ellipse(0, 0, 60, 44, POIL), chemin("M 40 20 Q 70 0 50 -20", stroke=POIL_F, sw=16),
         ellipse(-10, 8, 34, 22, CLAIR), cercle(-38, -18, 26, POIL), cercle(-52, -36, 9, POIL_F),
         ellipse(-50, -8, 14, 10, CLAIR), oeil(-34, -22, "fermes", taille=0.8), joue(-26, -12, 0.6)]
    return place(m, x, y, s, rot=rot)


def alpage(S, y=560, graine=1, saison="ete"):
    """Prairie de montagne avec sommets enneigés et fleurs."""
    if saison == "hiver":
        ciel(S, "#a5d8ff", "#f1f3f5")
        montagnes_fond(S, y - 40, ("#dee2e6", "#ced4da"))
        S.add(chemin(f"M 0 {y} Q 200 {y - 20} 400 {y} T 800 {y - 10} L 800 800 L 0 800 Z", "#f8f9fa"))
        return
    ciel(S, "#74c0fc", "#e7f5ff")
    montagnes_fond(S, y - 40, ("#b197fc", "#9775fa") if saison == "ete" else ("#d0bfff", "#b197fc"))
    herbe_c = "#8ce99a" if saison == "ete" else ("#c0eb75" if saison == "printemps" else "#d8c27a")
    S.add(chemin(f"M 0 {y} Q 200 {y - 30} 400 {y} T 800 {y - 10} L 800 800 L 0 800 Z", herbe_c))
    r = random.Random(graine)
    if saison in ("ete", "printemps"):
        for _ in range(16):
            S.add(fleur(r.uniform(20, 780), r.uniform(y + 40, 790), r.uniform(0.5, 0.8),
                        r.choice(["#ffd43b", "#ffffff", "#748ffc", "#ff8787", "#cc5de8"]), tige=r.uniform(20, 50)))
    for _ in range(5):
        S.add(caillou(r.uniform(20, 780), r.uniform(y + 30, 780), r.uniform(0.5, 1.0)))


def trou(x, y, s=1.0):
    return place([ellipse(0, 0, 50, 22, "#5c3a1e"), ellipse(0, 4, 40, 16, "#2b1d10"),
                  chemin("M -60 0 Q 0 -30 60 0", stroke="#a0693a", sw=10)], x, y, s)


def terrier(S, y=300, saison="ete", neige=0):
    """Coupe du terrier sous l'alpage : galeries et chambres."""
    if saison == "hiver":
        ciel(S, "#a5d8ff", "#f1f3f5")
        flocons(S, 40, 3, (0, 0, 800, y))
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, y, 800, 800 - y, S.degrade(["#a0693a", "#6d4424"])))
    S.add(chemin(f"M 0 {y - 8} Q 200 {y - 24} 400 {y - 8} T 800 {y - 14} L 800 {y + 12} L 0 {y + 12} Z",
                 "#8ce99a" if saison != "hiver" else "#f8f9fa"))
    if neige:
        S.add(rect(0, y - neige, 800, neige + 10, "#f8f9fa"))
        S.add(chemin(f"M 0 {y - neige} Q 200 {y - neige - 20} 400 {y - neige} T 800 {y - neige - 10}", stroke="#dee2e6", sw=4))
    r = random.Random(5)
    for _ in range(14):
        S.add(ellipse(r.uniform(10, 790), r.uniform(y + 40, 790), r.uniform(8, 18), r.uniform(6, 12), "#c9a27a", opacity=0.7))
    # galeries (en coordonnées de page)
    S.add(chemin(f"M 160 {y} Q 180 {y + 120} 300 {y + 180} Q 420 {y + 240} 560 {y + 300}", stroke="#4a2e16", sw=60))
    S.add(chemin(f"M 300 {y + 180} Q 220 {y + 260} 200 {y + 360}", stroke="#4a2e16", sw=50))
    S.add(ellipse(560, y + 330, 150, 90, "#4a2e16"))
    S.add(ellipse(200, y + 390, 90, 60, "#4a2e16"))
    return (560, y + 330), (200, y + 390)


def foin(x, y, s=1.0, graine=2):
    r = random.Random(graine)
    m = [ellipse(0, 0, 130, 34, "#e9c46a")]
    for _ in range(26):
        a = r.uniform(-0.4, 0.4)
        px = r.uniform(-120, 120)
        m.append(trait(px - 20, r.uniform(-20, 10), px + 20, r.uniform(-20, 10) + a * 20, "#d4a72c", 3))
    return place(m, x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    alpage(S, 600)
    S.add(trou(580, 700, 1.1))
    S.add(marmotte(380, 750, 1.8, expr="rire", bras="porte", objet=fleur(0, -96, 0.9, "#ffd43b", tige=30)))
    S.add(marmotte(600, 720, 0.9, expr="content", grosse=1.05))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(marmotte(200, 262, 0.95, expr="content", bras="porte", objet=fleur(0, -96, 0.9, "#ffd43b", tige=30)))
    return S


def p01():
    S = Scene()
    alpage(S, 560)
    S.add(trou(160, 640, 0.9))
    S.add(marmotte(160, 640, 0.75, expr="sourire", regard=(1, 0)))
    S.add(marmotte(420, 740, 1.3, expr="miam", bras="bouche", objet=fleur(0, -150, 0.8, "#ff8787", tige=30)))
    S.add(marmotte(650, 700, 1.0, expr="content", regard=(-1, 0)))
    S.add(soleil(680, 100, 50))
    return S


def p02():
    S = Scene()
    alpage(S, 560, graine=2)
    S.add(marmotte(400, 770, 2.2, expr="miam", grosse=1.25, bras="porte",
                   objet=g([fleur(-14, -100, 0.8, "#ffd43b", tige=30), fleur(14, -104, 0.8, "#748ffc", tige=30)])))
    S.add(texte(400, 150, "Miam, miam !", 60, "#099268", contour="#fff"))
    return S


def p03():
    S = Scene()
    alpage(S, 560, graine=3)
    S.add(aigle(300, 170, 1.0))
    S.add(caillou(520, 690, 2.4))
    S.add(marmotte(520, 640, 1.4, expr="surpris", crie=True, regard=(-1, -1)))
    S.add(texte(320, 360, "Fiiiiiit !", 64, "#c92a2a", contour="#fff", rot=-6))
    return S


def p04():
    S = Scene()
    alpage(S, 560, graine=4)
    S.add(aigle(620, 140, 0.9, flip=True))
    S.add(trou(560, 700, 1.4))
    S.add(marmotte_court(200, 700, 1.2), marmotte_court(380, 760, 1.0))
    S.add(place(g([ellipse(0, -40, 40, 30, POIL), chemin("M 0 -10 Q 20 20 40 0", stroke=POIL_F, sw=14)]), 560, 700, 1.0))
    S.add(mouvement(100, 660, 1.0, "#495057"))
    return S


def p05():
    S = Scene()
    (cx, cy), (bx, by) = terrier(S, 280)
    S.add(foin(cx, cy + 50, 1.0))
    S.add(marmotte_dort(cx - 60, cy + 20, 0.8), marmotte(cx + 70, cy + 60, 0.55, expr="content"))
    S.add(marmotte(bx, by + 40, 0.5, expr="sourire", bras="porte", objet=foin(0, -100, 0.3)))
    S.add(marmotte(160, 290, 0.6, expr="sourire"))
    return S


def p06():
    S = Scene()
    (cx, cy), (bx, by) = terrier(S, 280, saison="automne")
    S.add(foin(cx, cy + 50, 1.0))
    S.add(rect(120, 300, 80, 70, "#7c4a1e", rx=20))
    S.add(marmotte(210, 470, 0.6, expr="concentre", bras="haut", regard=(-1, -1)))
    S.add(marmotte(cx - 40, cy + 50, 0.55, expr="baille"), marmotte(cx + 50, cy + 50, 0.5, expr="baille"))
    for x, c in [(500, "#ffa94d"), (620, "#fab005")]:
        S.add(ellipse(x, 230, 14, 7, c, rot=30))
    return S


def p07():
    S = Scene()
    fond(S, "#4a2e16")
    S.add(ellipse(400, 480, 360, 250, "#6d4424"))
    S.add(foin(400, 600, 2.4))
    for x, y, r in [(300, 470, -10), (470, 450, 20), (390, 540, 0), (540, 540, -20), (250, 560, 15)]:
        S.add(marmotte_dort(x, y, 1.1, rot=r))
    S.add(zzz(600, 300, 1.4, "#e9d3b5"))
    S.add(coeur(200, 220, 1.5, "#ff8787"))
    S.add(texte(200, 330, "boum… boum…", 40, "#ffc9c9"))
    return S


def p08():
    S = Scene()
    (cx, cy), (bx, by) = terrier(S, 330, saison="hiver", neige=90)
    S.add(foin(cx, cy + 50, 1.0))
    for x, r in [(cx - 60, -10), (cx + 30, 15), (cx - 10, 0)]:
        S.add(marmotte_dort(x, cy + 10, 0.65, rot=r))
    S.add(rect(110, 300, 100, 100, "#7c4a1e", rx=20))
    S.add(sapin(640, 250, 0.7, neige=True), sapin(720, 260, 0.6, neige=True))
    return S


def p09():
    S = Scene()
    alpage(S, 560, saison="printemps")
    S.add(rect(0, 520, 260, 50, "#f8f9fa", rx=20))
    S.add(trou(420, 680, 1.2))
    S.add(marmotte(420, 690, 1.4, expr="baille", grosse=0.82, bras="haut"))
    S.add(soleil(660, 110, 55, visage=True))
    return S


def p10():
    S = Scene()
    alpage(S, 560, graine=6)
    S.add(trou(640, 640, 0.9))
    S.add(marmotte(250, 740, 0.9, expr="rire", bras="haut"), marmotte(400, 740, 0.9, expr="joie", bras="haut", flip=True))
    S.add(marmotte(560, 760, 0.8, expr="rire", bras="porte", objet=fleur(0, -96, 0.6, "#ffffff", tige=20)))
    S.add(marmotte(660, 640, 1.3, expr="content", regard=(-1, 0.3)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("marmotte-seule.svg", vignette),
    ("01-l-alpage.svg", p01), ("02-les-reserves.svg", p02), ("03-la-sentinelle.svg", p03),
    ("04-au-terrier.svg", p04), ("05-le-terrier.svg", p05), ("06-on-ferme.svg", p06),
    ("07-hibernation.svg", p07), ("08-sous-la-neige.svg", p08), ("09-le-reveil.svg", p09),
    ("10-les-marmottons.svg", p10),
]
