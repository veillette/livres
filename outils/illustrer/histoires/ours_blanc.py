"""L'ours blanc sur la banquise — l'ours polaire.

L'ours blanc vit sur la banquise de l'Arctique. Sous sa fourrure qui paraît
blanche, sa peau est noire, et une épaisse couche de graisse le protège du
froid. Il nage très bien, en ramant avec ses pattes de devant. Son flair
repère un phoque de très loin ; il attend près des trous dans la glace où les
phoques viennent respirer. Ses larges pattes au dessous poilu l'empêchent de
glisser. À l'automne, la femelle creuse une tanière dans la neige ; les
oursons y naissent minuscules en plein hiver, boivent son lait et sortent au
printemps. Ils restent environ deux ans avec leur mère. L'ours a besoin de la
banquise, qui fond plus tôt quand la Terre se réchauffe.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant

ID = "ours-blanc"
BLANC_O = "#fff3d4"
OMBRE_O = "#ead9ae"
NEIGE = "#dbe9f7"


# --- Personnages ------------------------------------------------------------

def ours_blanc(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), nage=False, flaire=False, couche=False):
    """Ours blanc à quatre pattes, de profil, tête à droite ; (x, y) = sous les
    pattes. nage : seuls le dos et la tête dépassent (dessiner l'eau devant) ;
    flaire : museau levé ; couche : allongé à plat ventre."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [ellipse(0, 0, 190, 18, "#1864ab", opacity=0.12)]
    if not couche:
        for px in (-80, 60):
            m.append(rect(px - 26, -130, 52, 130, OMBRE_O, rx=20))
            m.append(ellipse(px + 6, -6, 34, 10, "#ced4da"))
    corps = "M -140 -150 Q -140 -250 -40 -250 Q 60 -256 110 -210 Q 130 -170 110 -120 Q 0 -100 -110 -110 Q -146 -118 -140 -150 Z"
    if couche:
        corps = "M -150 -70 Q -150 -150 -40 -150 Q 60 -156 110 -110 Q 130 -60 110 -10 Q 0 4 -120 -6 Q -156 -20 -150 -70 Z"
    m.append(chemin(corps, BLANC_O))
    m.append(ellipse(-140, -170 if not couche else -70, 14, 12, BLANC_O))
    if not couche:
        for px in (-110, 90):
            m.append(rect(px - 28, -140, 56, 140, BLANC_O, rx=22))
            m.append(ellipse(px + 8, -6, 36, 10, OMBRE_O))
    else:
        m.append(ellipse(140, -10, 50, 14, BLANC_O))
    # tête
    hx, hy = (170, -200) if not couche else (180, -60)
    if flaire:
        hx, hy = 180, -250
    m.append(chemin(f"M 90 {hy + 40} Q {hx - 40} {hy - 20} {hx} {hy - 20}", stroke=BLANC_O, sw=70))
    m.append(cercle(hx - 26, hy - 40, 13, BLANC_O) + cercle(hx - 26, hy - 40, 6, OMBRE_O))
    m.append(ellipse(hx, hy, 46, 36, BLANC_O))
    m.append(ellipse(hx + 34, hy + 8, 30, 22, BLANC_O))
    m.append(ellipse(hx + 60, hy + 2, 10, 8, ENCRE))
    m.append(oeil(hx + 10, hy - 10, ys, regard, taille=0.8))
    m.append(joue(hx + 26, hy + 14, 0.7))
    m.append(place(bouche(0, 0, bs, 0.6), hx + 46, hy + 18))
    if flaire:
        m.append(g([chemin(f"M {hx + 76} {hy - 6 + k * 10} q 14 -6 28 0", stroke="#868e96", sw=3) for k in range(3)]))
    return place(m, x, y, s, flip=flip)


def ourson(x, y, s=1.0, **k):
    """Ourson blanc assis, vu de face (personnage de base.py)."""
    k.setdefault("couleur", "#fff3d4")
    k.setdefault("visage", "#fffaf0")
    return perso("ours", x, y, s, **k)


def phoque(x, y, s=1.0, flip=False, expr="surpris", tete_seule=False):
    """Phoque gris ; tete_seule : seule la tête sort d'un trou ; (x, y) = bas."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if not tete_seule:
        m.append(chemin("M -140 -20 Q -180 -40 -200 -10 Q -180 0 -140 0 Z", "#868e96"))
        m.append(ellipse(-40, -40, 120, 44, "#adb5bd"))
    m.append(ellipse(60, -70, 44, 40, "#adb5bd"))
    for sgn in (-1, 1):
        m.append(cercle(60 + sgn * 18, -78, 10, "#ffffff") + cercle(60 + sgn * 18, -76, 7, ENCRE))
    m.append(ellipse(60, -54, 14, 10, "#868e96"))
    m.append(g([trait(60 + sgn * 10, -54, 60 + sgn * 34, -58 + k * 6, "#495057", 1.5) for sgn in (-1, 1) for k in range(2)]))
    return place(m, x, y, s, flip=flip)


def trou_glace(x, y, s=1.0):
    return place([ellipse(0, 0, 70, 22, "#1864ab"), ellipse(0, -4, 70, 18, "#1c7ed6"),
                  chemin("M -76 -4 Q 0 -30 76 -4", stroke="#d0ebff", sw=6)], x, y, s)


def taniere(S, y=330, nuit_=True):
    """Coupe d'une tanière creusée dans la neige."""
    if nuit_:
        nuit(S, "#16213e", "#3b4a7a")
        etoiles(S, 30, 3, (0, 0, 800, y - 40))
    else:
        ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin(f"M 0 {y} Q 200 {y - 60} 420 {y - 40} T 800 {y} L 800 800 L 0 800 Z", "#e7f5ff"))
    S.add(ellipse(420, 560, 260, 160, "#d0ebff"))
    S.add(ellipse(420, 580, 240, 140, "#a5d8ff", opacity=0.35))
    S.add(chemin(f"M 640 520 Q 720 460 760 {y - 4}", stroke="#d0ebff", sw=70))


def glace(S, y=560, graine=1, nuit_=False):
    """Banquise un peu bleutée, pour que l'ours crème se détache bien."""
    banquise(S, y, graine=graine, nuit_=nuit_)
    S.add(chemin(f"M 0 {y} Q 200 {y - 14} 400 {y} T 800 {y - 4} L 800 800 L 0 800 Z", NEIGE, opacity=0.7))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    glace(S, 600)
    S.add(ours_blanc(340, 750, 1.2, expr="content"))
    S.add(ourson(610, 760, 0.8, expr="rire", bras="salut"))
    S.cachette(730, 640, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ours_blanc(170, 262, 0.62, expr="content"))
    S.add(ourson(340, 262, 0.45, expr="rire"))
    return S


def p01():
    S = Scene()
    glace(S, 560)
    S.add(ours_blanc(360, 740, 1.15, expr="sourire"))
    S.add(texte(400, 150, "L'Arctique", 56, "#1098ad", contour="#fff"))
    S.cachette(730, 640, "air")
    return S


def p02():
    S = Scene()
    fond(S, "#e3fafc")
    S.add(ours_blanc(300, 760, 1.05, expr="content"))
    contenu = [rect(500, 180, 260, 260, BLANC_O)]
    for k in range(14):
        contenu.append(trait(520 + k * 18, 200, 530 + k * 18, 280, "#e9ecef", 6))
    contenu.append(rect(500, 290, 260, 40, "#343a40"))
    contenu.append(rect(500, 330, 260, 110, "#fff3bf"))
    S.add(loupe(630, 310, 120, contenu, rot=130))
    S.add(etiquette(630, 130, "fourrure", 30, "#1098ad"))
    S.add(etiquette(640, 470, "peau noire", 30, "#343a40"))
    S.add(etiquette(640, 510, "graisse", 30, "#e67700"))
    S.cachette(410, 70, "air")
    return S


def p03():
    S = Scene()
    S.add(rect(0, 0, 800, 400, S.degrade(["#a5d8ff", "#e7f5ff"])))
    S.add(rect(0, 400, 800, 400, S.degrade(["#339af0", "#1864ab"])))
    S.add(poly([(0, 380), (180, 380), (220, 410), (0, 410)], BLANC_O), poly([(620, 390), (800, 380), (800, 412), (600, 412)], BLANC_O))
    S.add(ours_blanc(400, 600, 1.1, expr="rire"))
    S.add(rect(0, 410, 800, 390, "#1864ab", opacity=0.55))
    S.add(chemin("M 0 410 q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0",
                 stroke="#d0ebff", sw=6))
    S.add(g([cercle(250 + k * 30, 420, 8, "#ffffff", opacity=0.8) for k in range(4)]))
    S.cachette(70, 670, "poisson")
    return S


def p04():
    S = Scene()
    glace(S, 520, graine=2)
    S.add(ours_blanc(260, 740, 1.05, expr="concentre", flaire=True))
    S.add(phoque(660, 560, 0.45))
    S.add(chemin("M 460 470 Q 560 440 640 520", stroke="#868e96", sw=4, stroke_dasharray="10 10"))
    S.cachette(730, 630, "air")
    return S


def p05():
    S = Scene()
    glace(S, 500, graine=3)
    S.add(trou_glace(560, 700, 1.4))
    S.add(phoque(512, 730, 0.8, tete_seule=True))
    S.add(chemin("M 450 700 Q 560 744 670 700 Q 676 730 640 742 Q 560 756 480 742 Q 444 730 450 700 Z", "#e4eef9"))
    S.add(ours_blanc(230, 740, 1.0, expr="concentre", couche=True, regard=(1, 0.3)))
    S.add(texte(560, 230, "Chut…", 60, "#1098ad", contour="#fff"))
    S.cachette(730, 630, "air")
    return S


def p06():
    S = Scene()
    glace(S, 520, graine=4)
    S.add(ours_blanc(280, 740, 1.0, expr="fier"))
    sole = [rect(510, 440, 220, 220, "#343a40")]
    for k in range(5):
        sole.append(ellipse(560 + k * 30, 500, 14, 18, "#495057"))
    sole.append(ellipse(620, 590, 60, 40, "#495057"))
    for k in range(20):
        sole.append(trait(520 + (k * 37) % 200, 540 + (k * 23) % 100, 528 + (k * 37) % 200, 560 + (k * 23) % 100, BLANC_O, 4))
    S.add(loupe(620, 550, 110, sole, fond="#343a40", rot=-140))
    S.add(etiquette(620, 400, "anti-glisse !", 34, "#1098ad"))
    S.cachette(70, 630, "air")
    return S


def p07():
    S = Scene()
    taniere(S, 330, nuit_=False)
    S.add(ours_blanc(430, 650, 0.85, expr="concentre", couche=True))
    S.add(g([cercle(700 + k * 16, 300 - k * 20, 10 + k * 2, "#ffffff", stroke="#dee2e6", stroke_width=2) for k in range(4)]))
    S.add(texte(250, 160, "Une maison de neige", 44, "#1098ad", contour="#fff"))
    S.cachette(280, 730, "air")
    return S


def p08():
    S = Scene()
    taniere(S, 330)
    flocons(S, 40, 5, (0, 0, 800, 300))
    S.add(ours_blanc(420, 650, 0.85, expr="content", couche=True, regard=(-1, 0.6)))
    S.add(place(g([ellipse(0, 0, 26, 18, "#fffaf0"), cercle(20, -6, 12, "#fffaf0"), oeil(22, -8, "fermes", taille=0.5)]), 500, 640))
    S.add(place(g([ellipse(0, 0, 26, 18, "#fffaf0"), cercle(20, -6, 12, "#fffaf0"), oeil(22, -8, "fermes", taille=0.5)]), 550, 646))
    S.add(coeur(420, 420, 1.3, "#ff8787"))
    S.cachette(70, 140, "air")
    return S


def p09():
    S = Scene()
    glace(S, 560, graine=5)
    S.add(soleil(120, 120, 50))
    S.add(ours_blanc(560, 740, 0.9, expr="content", regard=(-1, 0.4), flip=True))
    S.add(ourson(200, 760, 0.9, expr="rire", bras="haut"))
    S.add(place(ourson(0, 0, 0.9, expr="rire", bras="haut"), 360, 700, 1.0, rot=-30))
    S.add(g([cercle(300 + k * 30, 640 - k * 10, 6, "#ffffff", stroke="#d0ebff", stroke_width=2) for k in range(5)]))
    S.cachette(730, 590, "air")
    return S


def p10():
    S = Scene()
    glace(S, 560, graine=6)
    S.add(poly([(560, 620), (800, 600), (800, 800), (520, 800)], "#1c7ed6"))
    S.add(ours_blanc(260, 740, 1.0, expr="sourire"))
    S.add(ourson(500, 760, 0.7, expr="content"), ourson(430, 770, 0.65, expr="sourire"))
    S.add(texte(400, 170, "Prenons soin de la banquise !", 40, "#1098ad", contour="#fff"))
    S.cachette(70, 650, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ours-seuls.svg", vignette),
    ("01-l-arctique.svg", p01), ("02-la-fourrure.svg", p02), ("03-il-nage.svg", p03),
    ("04-le-flair.svg", p04), ("05-le-trou-dans-la-glace.svg", p05), ("06-les-pattes.svg", p06),
    ("07-la-taniere.svg", p07), ("08-les-oursons.svg", p08), ("09-au-printemps.svg", p09),
    ("10-la-banquise.svg", p10),
]
