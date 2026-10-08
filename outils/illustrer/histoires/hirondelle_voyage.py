"""L'hirondelle part en voyage — la migration de l'hirondelle rustique.

Au printemps, l'hirondelle rustique revient d'Afrique. Elle bâtit sous le
toit de l'étable un nid de boulettes de boue mêlées de paille, garni de
plumes, et y couve quatre ou cinq œufs. Les parents nourrissent les petits
d'insectes attrapés en plein vol. Ailes pointues et queue fourchue en font
une acrobate qui boit en rasant l'eau. À la fin de l'été, les hirondelles se
rassemblent sur les fils, puis traversent la mer et le désert du Sahara pour
passer l'hiver en Afrique, où les insectes ne manquent pas. Au printemps,
elles reviennent, souvent au même nid.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, fleche_courbe
from objets import flaque

ID = "hirondelle-voyage"
DOS = "#1c3d6e"
GORGE = "#c92a2a"
VENTRE = "#fff4e6"


# --- Personnages ------------------------------------------------------------

def hirondelle_vol(x, y, s=1.0, flip=False, rot=0, expr="sourire", boue=False, insecte=False, bec_ouvert=False):
    """Hirondelle en vol, vue de côté et un peu de dessous, tête à droite ;
    (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -40 0 L -120 -16 L -78 4 L -126 26 Z", DOS),
         chemin("M -10 -6 Q -40 -90 -120 -120 Q -60 -60 -30 6 Z", _assombrir(DOS, 0.85)),
         ellipse(0, 0, 50, 22, DOS), ellipse(4, 8, 40, 13, VENTRE),
         chemin("M 0 -4 Q 30 -80 110 -120 Q 50 -50 26 6 Z", DOS),
         cercle(46, -6, 18, DOS), ellipse(54, 4, 13, 10, GORGE), ellipse(56, -16, 9, 5, GORGE)]
    m.append(oeil(52, -10, ys, (1, 0), taille=0.6))
    if bec_ouvert or bs in ("ouverte", "o"):
        m.append(poly([(62, -6), (80, -8), (64, -2)], ENCRE) + poly([(62, 0), (78, 4), (62, 4)], ENCRE))
    else:
        m.append(poly([(62, -6), (80, -2), (62, 2)], ENCRE))
    if boue:
        m.append(cercle(84, -2, 8, "#7c4a1e"))
    if insecte:
        m.append(mouche(96, -4, 0.45, rot=90))
    return place(m, x, y, s, flip=flip, rot=rot)


def hirondelle_posee(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), bec_ouvert=False):
    """Hirondelle posée sur un fil, de profil, tête à droite ; (x, y) = pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -20 -30 L -80 -10 L -60 -30 L -90 -4 Z", DOS),
         trait(-4, -8, -4, 0, ENCRE, 3), trait(8, -8, 8, 0, ENCRE, 3),
         ellipse(0, -34, 30, 26, VENTRE), chemin("M -30 -40 Q 0 -70 30 -50 Q 20 -20 -30 -20 Z", DOS),
         chemin("M -24 -36 Q -60 -30 -84 -16 Q -50 -20 -20 -24 Z", _assombrir(DOS, 0.85)),
         cercle(22, -62, 18, DOS), ellipse(30, -50, 12, 10, GORGE), ellipse(32, -70, 8, 4, GORGE)]
    m.append(oeil(28, -66, ys, regard, taille=0.6))
    m.append(joue(30, -54, 0.5))
    if bec_ouvert or bs in ("ouverte", "o"):
        m.append(poly([(38, -62), (52, -66), (40, -58)], ENCRE) + poly([(38, -56), (50, -52), (38, -52)], ENCRE))
    else:
        m.append(poly([(38, -62), (54, -58), (38, -54)], ENCRE))
    return place(m, x, y, s, flip=flip)


def nid_boue(x, y, s=1.0, coupe=False, contenu=""):
    """Nid en coupelle de boulettes de boue collé sous une poutre ; (x, y) =
    haut du nid, contre le mur."""
    m = []
    forme = "M -90 0 Q -86 80 0 90 Q 86 80 90 0 Z"
    m.append(chemin(forme, "#8d6e4a"))
    r = random.Random(3)
    for _ in range(26):
        a = r.uniform(0.05, 0.95) * math.pi
        d = r.uniform(0.3, 0.95)
        m.append(cercle(math.cos(a) * 82 * d, math.sin(a) * 82 * d, r.uniform(9, 13), r.choice(["#7c5a3c", "#a0806a", "#8d6e4a"])))
    for k in range(5):
        m.append(trait(-70 + k * 30, 20 + (k % 2) * 20, -40 + k * 30, 30 + (k % 2) * 20, "#e9c46a", 3))
    m.append(contenu)
    return place(m, x, y, s)


def poussin_hirondelle(x, y, s=1.0, rot=0):
    m = [ellipse(0, 0, 26, 22, "#495057"), cercle(0, -26, 18, "#868e96"),
         poly([(-16, -30), (16, -30), (0, -80)], "#ffd43b"), poly([(-12, -34), (12, -34), (0, -70)], "#ff922b"),
         oeil(-10, -30, "fermes", taille=0.5), oeil(10, -30, "fermes", taille=0.5)]
    return place(m, x, y, s, rot=rot)


def etable(S, y=600):
    """Mur et toit d'une étable vus de près : grosse poutre en haut."""
    S.add(rect(0, 0, 800, 800, "#e9d8c4"))
    for k in range(10):
        S.add(rect(0, k * 80, 800, 4, "#d9c3a5"))
    S.add(rect(0, 0, 800, 140, "#7c4a1e"))
    S.add(rect(0, 120, 800, 26, "#5c3a1e"))


def ferme(S, y=580):
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(chemin(f"M 0 {y - 30} Q 200 {y - 80} 400 {y - 40} T 800 {y - 50} L 800 {y + 10} L 0 {y + 10} Z", "#b2f2bb"))
    S.add(rect(0, y, 800, 800 - y, "#8ce99a"))
    S.add(place([rect(-180, -220, 360, 220, "#c92a2a"), poly([(-210, -220), (210, -220), (0, -340)], "#862e2e"),
                 rect(-60, -150, 120, 150, "#862e2e")], 560, y + 20))


def fils(S, y=300):
    S.add(rect(80, y - 40, 22, 800, "#7c4a1e"), rect(700, y - 40, 22, 800, "#7c4a1e"))
    for k in range(3):
        S.add(chemin(f"M 0 {y + k * 70} Q 400 {y + k * 70 + 40} 800 {y + k * 70}", stroke="#343a40", sw=3))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    S.add(nuage(160, 470, 0.9), nuage(640, 560, 0.7))
    S.add(hirondelle_vol(400, 520, 1.9, rot=-10, expr="content"))
    S.add(hirondelle_vol(160, 650, 0.7, rot=-20), hirondelle_vol(660, 700, 0.6, rot=-5))
    S.cachette(490, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(hirondelle_vol(200, 160, 1.1, rot=-10, expr="content"))
    return S


def p01():
    S = Scene()
    ferme(S)
    S.add(soleil(120, 110, 50))
    S.add(fleur(100, 700, 0.8, "#ffd43b"), fleur(220, 740, 0.8, "#ffffff"), fleur(320, 690, 0.8, "#ffd43b"))
    for x, y, sc, r in [(300, 260, 1.0, -10), (460, 180, 0.8, 5), (620, 240, 0.7, -15)]:
        S.add(hirondelle_vol(x, y, sc, rot=r, expr="rire"))
    S.add(texte(250, 420, "Nous revoilà !", 50, "#1c3d6e", contour="#fff"))
    return S


def p02():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 560, 800, 240, "#a0693a"))
    S.add(flaque(450, 650, 2.2, "#8d6e4a"))
    S.add(hirondelle_posee(420, 640, 1.6, expr="concentre", regard=(1, 1)))
    S.add(hirondelle_vol(560, 260, 1.0, rot=-20, boue=True, expr="content"))
    S.add(texte(250, 200, "De la boue !", 50, "#1c3d6e", contour="#fff"))
    return S


def p03():
    S = Scene()
    etable(S)
    S.add(nid_boue(400, 146, 2.2))
    S.add(hirondelle_vol(160, 380, 0.9, rot=-10, boue=True))
    S.add(loupe(620, 560, 110, [rect(510, 450, 220, 220, "#e9d8c4"),
                                 place(nid_boue(0, 0, 1.0, contenu=g([ellipse(-30, 30, 14, 18, "#ffffff"), ellipse(0, 34, 14, 18, "#fff4e6"),
                                                                     ellipse(28, 30, 14, 18, "#ffffff"), ellipse(-12, 50, 13, 16, "#fff9f0")])),
                                       620, 500, 1.0)], fond="#e9d8c4", rot=130))
    S.add(hirondelle_posee(460, 150, 0.9, flip=True))
    S.cachette(670, 70, "air")
    return S


def p04():
    S = Scene()
    etable(S)
    S.add(nid_boue(400, 146, 2.6))
    for k, x in enumerate([330, 380, 430, 480]):
        S.add(poussin_hirondelle(x, 230, 1.0, rot=(k - 1.5) * 12))
    S.add(hirondelle_vol(600, 360, 1.1, flip=True, rot=10, insecte=True))
    S.add(texte(250, 620, "Piou ! Piou !", 56, "#e8590c", contour="#fff"))
    S.cachette(670, 70, "air")
    return S


def p05():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 640, 800, 160, "#8ce99a"))
    r = random.Random(5)
    for _ in range(12):
        S.add(moustique(r.uniform(300, 760), r.uniform(150, 560), r.uniform(0.6, 1.0)))
    S.add(hirondelle_vol(300, 360, 1.6, rot=-5, expr="miam", bec_ouvert=True))
    S.add(mouvement(80, 380, 1.2, "#495057"))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 520, 800, 280, "#69db7c"))
    S.add(ellipse(400, 640, 380, 110, "#4dabf7"))
    S.add(hirondelle_vol(380, 560, 1.4, rot=5, expr="content"))
    S.add(g([cercle(480 + k * 24, 600 + (k % 2) * 6, 6, "#ffffff", opacity=0.8) for k in range(5)]))
    S.add(chemin("M 220 610 Q 380 640 560 604", stroke="#d0ebff", sw=4))
    return S


def p07():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#ffc078", "#fff3bf"])))
    fils(S, 300)
    r = random.Random(7)
    for k in range(3):
        y = 300 + k * 70
        for j in range(9):
            x = 140 + j * 62 + r.uniform(-8, 8)
            if r.random() < 0.85:
                yy = y + 40 * (1 - ((x - 400) / 400) ** 2) - 2
                S.add(hirondelle_posee(x, yy, 0.55, flip=r.random() < 0.3, expr=r.choice(["sourire", "content", "chante"])))
    S.add(texte(400, 160, "On part bientôt ?", 50, "#1c3d6e", contour="#fff"))
    S.cachette(450, 730, "air")
    return S


def p08():
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#4dabf7"))
    S.add(chemin("M 0 0 L 800 0 L 800 230 Q 640 260 560 200 Q 460 250 360 210 Q 240 260 120 220 Q 60 240 0 210 Z", "#69db7c"))
    S.add(chemin("M 0 800 L 0 420 Q 200 380 400 410 Q 600 380 800 420 L 800 800 Z", "#ffd8a8"))
    S.add(chemin("M 0 800 L 0 640 Q 200 610 400 640 Q 600 610 800 640 L 800 800 Z", "#94d82d"))
    S.add(texte(160, 120, "chez nous", 34, "#2b8a3e", contour="#fff"), texte(400, 320, "la mer", 34, "#1864ab", contour="#fff"),
          texte(400, 520, "le désert", 34, "#e8590c", contour="#fff"), texte(400, 740, "l'Afrique", 34, "#2b8a3e", contour="#fff"))
    S.add(fleche_courbe("M 330 150 Q 260 400 360 690", (360, 690), 70, "#1c3d6e", 6, 22, stroke_dasharray="18 12"))
    for k, (x, y) in enumerate([(300, 250), (290, 330), (300, 450), (320, 560)]):
        S.add(hirondelle_vol(x, y, 0.35, rot=80))
    S.cachette(730, 380, "air")
    return S


def p09():
    S = Scene()
    savane(S, 600)
    S.add(soleil(640, 110, 60))
    r = random.Random(9)
    for _ in range(10):
        S.add(moustique(r.uniform(100, 700), r.uniform(250, 520), r.uniform(0.6, 0.9)))
    S.add(hirondelle_vol(380, 380, 1.2, rot=-10, expr="rire"))
    S.add(hirondelle_vol(160, 300, 0.6, rot=-20), hirondelle_vol(620, 260, 0.6, flip=True, rot=10))
    return S


def p10():
    S = Scene()
    etable(S)
    S.add(nid_boue(400, 146, 2.2))
    S.add(hirondelle_posee(400, 150, 1.2, expr="rire"))
    S.add(hirondelle_vol(620, 420, 1.0, flip=True, rot=10, expr="content"))
    S.add(coeur(250, 360, 1.2, "#ff8787"))
    S.add(texte(400, 640, "Le même nid !", 56, "#1c3d6e", contour="#fff"))
    S.cachette(670, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("hirondelle-seule.svg", vignette),
    ("01-le-retour.svg", p01), ("02-la-boue.svg", p02), ("03-le-nid.svg", p03),
    ("04-les-petits.svg", p04), ("05-en-plein-vol.svg", p05), ("06-boire.svg", p06),
    ("07-sur-les-fils.svg", p07), ("08-le-grand-voyage.svg", p08), ("09-en-afrique.svg", p09),
    ("10-le-retour.svg", p10),
]
