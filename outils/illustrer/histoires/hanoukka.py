"""Les huit lumières de Hanoukka — la fête des lumières avec Noam et Savta.

Hanoukka dure huit soirs, en décembre. On sort la hanoukkia, chandelier à
neuf branches : huit bougies et le chamach, « celle qui aide », qui allume
les autres. Chaque soir, une bougie de plus (on les place de droite à
gauche) ; on pose la hanoukkia à la fenêtre. La légende : au Temple de
Jérusalem, une petite fiole d'huile, de quoi brûler un jour, a brillé huit
jours (dans le Temple, le chandelier avait sept branches). On mange des
latkes et des beignets frits dans l'huile ; on joue à la toupie (sevivon)
avec des pièces en chocolat : ses quatre lettres disent « Un grand miracle
a eu lieu là-bas ».

Plans : 1 moyen (on sort la hanoukkia) · 2 large (la légende du Temple) ·
3 gros plan (le chamach, première bougie) · 4 moyen (à la fenêtre) · 5 moyen
(Savta et les latkes) · 6 gros plan (latkes et beignets) · 7 large (la
toupie, en famille) · 8 gros plan (la toupie et ses lettres) · 9 moyen (une
bougie de plus chaque soir) · 10 large (le huitième soir).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre

ID = "hanoukka"
PAPIER_PEINT = "rayures"

BLEU = "#1c7ed6"
OR_ = "#fcc419"


def kippa(c=BLEU):
    """Petite kippa sur le haut de la tête (coiffe)."""
    return g([chemin("M -30 -196 Q 0 -216 30 -196 Q 0 -190 -30 -196 Z", c), chemin("M -20 -200 Q 0 -208 20 -200", stroke="#fff", sw=2)])


NOAM = dict(peau="claire", cheveux="chatain", coiffure="boucles", habit="#4dabf7", robe=False, jambes="#364fc7", coiffe=kippa(), taches=True)
PAPA = dict(stature="adulte", peau="claire", cheveux="brun", coiffure="courts", habit="#f8f9fa", robe=False, jambes="#343a40",
            barbe="#4a2c17", coiffe=kippa("#364fc7"), acc=("lunettes",))
MAMAN = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="longs", habit="#7048e8", nez="retrousse")
SAVTA = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="boucles", habit="#1971c2", acc=("lunettes",), carrure="ronde")
COUSINE = dict(peau="doree", cheveux="noir", coiffure="couettes", habit="#f06595")


def noam(x, y, s=1.2, **k):
    return personne(x, y, s, **{**NOAM, **k})


def hanoukkia(x, y, s=1.0, allumees=0, chamach=True, S=None):
    """Hanoukkia : huit branches en ligne et le chamach plus haut au milieu ;
    allumees = nombre de bougies du soir, placées à partir de la droite ; (x, y) = pied."""
    m = [ellipse(0, -6, 90, 16, volume(OR_, 0.4, 0.75)), rect(-10, -150, 20, 146, cylindre(OR_, 0.3, 0.75), rx=6),
         rect(-200, -160, 400, 16, cylindre(OR_, 0.3, 0.75, vertical=True), rx=6)]
    xs = [-180 + k * 46 for k in range(4)] + [42 + k * 46 for k in range(4)]
    for k, bx in enumerate(xs):
        m.append(rect(bx - 10, -176, 20, 18, OR_, rx=4))
    m.append(rect(-12, -236, 24, 80, cylindre(OR_, 0.3, 0.75), rx=6))
    m.append(rect(-14, -246, 28, 14, OR_, rx=4))
    flammes = []
    ordre = list(reversed(xs))          # la première bougie se place à droite
    for k in range(allumees):
        bx = ordre[k]
        m.append(rect(bx - 7, -226, 14, 52, cylindre("#e7f5ff", 0.3, 0.8), rx=3))
        flammes.append((bx, -238))
    if chamach:
        m.append(rect(-8, -300, 16, 56, cylindre("#e7f5ff", 0.3, 0.8), rx=3))
        flammes.append((0, -312))
    for fx, fy in flammes:
        m += [ellipse(fx, fy, 7, 13, "#ffd43b"), ellipse(fx, fy + 4, 3.5, 7, "#fff3bf")]
        if S is not None:
            S.lumiere(x + fx * s, y + fy * s, 70 * s, "#ffd43b", 0.55)
    return place(m, x, y, s)


def menorah_temple(x, y, s=1.0):
    """Le chandelier du Temple, à sept branches, aux lampes d'huile allumées."""
    m = [rect(-60, -20, 120, 20, OR_, rx=6), rect(-10, -300, 20, 284, cylindre(OR_, 0.3, 0.75))]
    for k, r in enumerate((60, 120, 180)):
        m.append(chemin(f"M {-r} -300 Q {-r} {-300 + r * 1.1} 0 {-300 + r * 1.1} Q {r} {-300 + r * 1.1} {r} -300", stroke=OR_, sw=14))
    for bx in (-180, -120, -60, 0, 60, 120, 180):
        m += [ellipse(bx, -308, 18, 8, OR_), ellipse(bx, -326, 8, 14, "#ffd43b"), ellipse(bx, -322, 4, 7, "#fff3bf")]
    return place(m, x, y, s)


def fiole(x, y, s=1.0):
    return place([chemin("M -18 0 Q -24 -40 -10 -50 L -8 -70 L 8 -70 L 10 -50 Q 24 -40 18 0 Z", volume("#ced4da", 0.35, 0.8)),
                  chemin("M -16 -6 Q -20 -30 -12 -38 L 12 -38 Q 20 -30 16 -6 Z", "#fcc419", opacity=0.8), rect(-10, -80, 20, 12, "#a0693a", rx=3)], x, y, s)


def latke(x, y, s=1.0):
    return place([ellipse(0, 0, 40, 16, volume("#e8a33d", 0.4, 0.7)), chemin("M -26 -2 l 8 -4 M -6 4 l 10 -4 M 12 -4 l 8 -2", stroke="#c47f17", sw=2)], x, y, s)


def beignet(x, y, s=1.0):
    return place([ellipse(0, 0, 36, 26, volume("#f6c453", 0.45, 0.75)), ellipse(0, -14, 26, 10, "#fff", opacity=0.9),
                  cercle(0, -16, 6, "#e03131")], x, y, s)


def poele(x, y, s=1.0):
    m = [ellipse(0, 0, 110, 30, "#343a40"), ellipse(0, -4, 96, 22, "#495057"), rect(100, -10, 120, 16, "#212529", rx=6)]
    for k in range(3):
        m.append(latke(-50 + k * 50, -8, 0.8))
    for k in range(5):
        m.append(cercle(-70 + k * 35, -24 - (k % 2) * 10, 4, "#fff3bf", opacity=0.9))
    return place(m, x, y, s)


LETTRES = {
    "nun": "M -6 -14 L 4 -14 L 4 12 L -8 12",
    "guimel": "M -6 -14 L 2 -14 L 2 6 L 8 14 M 2 6 L -6 14",
    "he": "M -9 -14 L 8 -14 L 8 14 M -6 -4 L -6 14",
    "shin": "M -10 -14 Q -10 12 0 12 Q 10 12 10 -14 M 0 -14 L 0 12",
}


def toupie(x, y, s=1.0, rot=0, face="nun", cote="guimel", tourne=False):
    """Sevivon (toupie à quatre faces) ; (x, y) = sa pointe."""
    m = [rect(-6, -150, 12, 40, "#495057", rx=4),
         poly([(-50, -110), (30, -110), (30, -30), (-50, -30)], volume(BLEU, 0.3, 0.8)),
         poly([(30, -110), (52, -100), (52, -24), (30, -30)], _assombrir(BLEU, 0.75)),
         poly([(-50, -30), (30, -30), (52, -24), (0, 0)], _assombrir(BLEU, 0.6)),
         place(chemin(LETTRES[face], stroke="#fff", sw=5), -10, -70, 1.4),
         place(chemin(LETTRES[cote], stroke="#d0ebff", sw=4), 41, -66, 0.9)]
    if tourne:
        m += [chemin("M -80 -60 Q -90 -90 -60 -120", stroke=ENCRE, sw=3, opacity=0.5), chemin("M 80 -70 Q 90 -40 60 -10", stroke=ENCRE, sw=3, opacity=0.5)]
    return place(m, x, y, s, rot=rot)


def piece_chocolat(x, y, s=1.0):
    return place([cercle(0, 0, 18, volume(OR_, 0.4, 0.7)), cercle(0, 0, 12, "none", stroke="#f59f00", stroke_width=2)], x, y, s, sy=s * 0.5)


def salon(S, y=600, nuit_=True):
    piece(S, "manoir", y)
    if nuit_:
        S.ambiance("nuit")


def fenetre_neige(S, x=240, y=110, w=320, h=260, hanouk=0):
    dehors = g([rect(0, 0, 800, 800, "#1c2a52"), rect(0, y + h - 60, 800, 200, "#e7f5ff")] +
               [cercle(x + (k * 53) % w, y + (k * 37) % (h - 60), 3, "#fff") for k in range(20)])
    S.add(fenetre(x, y, w, h, "#1c2a52", cadre="#fff", contenu=dehors, rideaux="#74c0fc"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S)
    fenetre_neige(S, 180, 90, 440, 330)
    S.add(rect(150, 430, 500, 20, "#fff", rx=4))
    S.add(hanoukkia(400, 430, 0.9, allumees=8, S=S))
    S.add(noam(230, 790, 1.35, expr="rire", bras="ouverts", regard=(1, -0.4)))
    S.add(personne(560, 790, 1.35, expr="content", bras="mains_jointes", regard=(-1, -0.4), **SAVTA))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(hanoukkia(200, 262, 0.75, allumees=8))
    return S


def p01():
    """Plan moyen : un soir de décembre, Noam et Papa sortent la hanoukkia de sa boîte."""
    S = Scene()
    salon(S)
    fenetre_neige(S, 470, 100, 220, 180)
    S.add(table(380, 790, 500, 150, "#c68642"))
    S.add(personne(250, 790, 1.35, expr="content", bras="porte", regard=(1, 0.4), **PAPA))
    S.add(noam(520, 790, 1.2, expr="joie", bras="joues", regard=(-1, -0.2)))
    S.add(hanoukkia(380, 625, 0.55))
    S.add(texte(330, 160, "Ce soir, c'est Hanoukka !", 42, BLEU, contour="#fff"))
    return S


def p02():
    """Plan large : la légende : au Temple, une petite fiole d'huile brille huit jours."""
    S = Scene()
    piece(S, "chateau", 600)
    S.ambiance("nuit")
    for x in (120, 680):
        S.add(rect(x - 40, 60, 80, 540, cylindre("#e9d8c4", 0.25, 0.8)))
    S.add(menorah_temple(400, 640, 1.0))
    for x, y in ((400, 300), (220, 320), (580, 320)):
        S.lumiere(x, y, 110, "#ffd43b", 0.55)
    S.add(personne(180, 790, 1.15, stature="adulte", peau="doree", cheveux="brun", coiffure="courts", barbe="#4a2c17", habit="#e9d8c4",
                   robe=True, expr="bouche_bee", bras="donne", regard=(1, -0.5), objet=fiole(*ancre(84, -92, "donne", "adulte"), 0.9)))
    S.add(texte(400, 100, "Un jour d'huile… huit jours de lumière !", 34, "#fff", contour="#1864ab"))
    return S


def p03():
    """Gros plan : le premier soir, Papa allume la première bougie avec le chamach."""
    S = Scene()
    salon(S)
    S.add(table(400, 790, 560, 150, "#c68642"))
    S.add(hanoukkia(400, 625, 1.0, allumees=1, S=S))
    S.add(noam(620, 900, 1.6, expr="bouche_bee", bras="joues", regard=(-1, -0.5)))
    S.camera(1.3, 440, 460)
    S.dessus(bulle(280, 110, 420, 100, "Le chamach allume\nla première bougie.", 32, pointe=S.vers_page(400, 330)))
    return S


def p04():
    """Plan moyen : Noam pose la hanoukkia à la fenêtre ; dehors, il neige."""
    S = Scene()
    salon(S)
    fenetre_neige(S, 200, 100, 400, 300)
    S.add(rect(170, 410, 460, 20, "#fff", rx=4))
    S.add(hanoukkia(400, 410, 0.7, allumees=2, S=S))
    S.add(noam(400, 790, 1.4, expr="content", bras="haut", regard=(0, -0.6)))
    S.add(bulle(620, 520, 280, 90, "Pour que tout\nle monde la voie !", 26, pointe=(470, 560)))
    return S


def p05():
    """Plan moyen : dans la cuisine, Savta fait frire des latkes ; ça grésille."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(rect(80, 540, 640, 60, "#ced4da", rx=6))
    S.add(poele(380, 530, 1.0))
    S.add(personne(250, 790, 1.4, expr="content", bras="donne", regard=(1, 0.3), **SAVTA))
    S.add(noam(600, 790, 1.2, expr="miam", bras="bouche", regard=(-1, -0.2)))
    S.add(texte(400, 170, "Grrr… ça grésille !", 44, "#e8590c", contour="#fff"))
    return S


def p06():
    """Gros plan : latkes à la compote de pommes et beignets à la confiture."""
    S = Scene()
    salon(S)
    S.add(table(400, 790, 600, 150, "#c68642", nappe="#d0ebff"))
    S.add(ellipse(280, 620, 120, 28, "#fff", stroke="#dee2e6", stroke_width=3))
    for k in range(4):
        S.add(latke(250 + (k % 2) * 60, 612 - k * 8, 1.0))
    S.add(rect(170, 560, 50, 50, "#fff3bf", rx=8), ellipse(195, 562, 25, 8, "#ffd8a8"))
    S.add(ellipse(540, 620, 120, 28, "#fff", stroke="#dee2e6", stroke_width=3))
    for k, (dx, dy) in enumerate(((-40, -14), (30, -14), (-5, -40))):
        S.add(beignet(540 + dx, 620 + dy, 1.1))
    S.camera(1.3, 410, 560)
    S.dessus(texte(400, 110, "Des latkes et des beignets !", 44, "#e8590c", contour="#fff"))
    S.cachette(425, 746, "air")
    return S


def p07():
    """Plan large : au salon, on joue à la toupie avec des pièces en chocolat."""
    S = Scene()
    salon(S)
    fenetre_neige(S, 520, 90, 200, 160)
    S.add(hanoukkia(620, 290, 0.3, allumees=4, S=S))
    S.add(tapis(400, 720, 330, 60, "#74c0fc", BLEU))
    S.add(toupie(400, 720, 0.6, rot=15, tourne=True))
    for k in range(8):
        S.add(piece_chocolat(300 + k * 26, 750 - (k % 2) * 8, 0.8))
    S.add(noam(180, 790, 1.15, expr="rire", bras="applaudit", regard=(1, 0.4)))
    S.add(personne(620, 790, 1.1, expr="joie", bras="ouverts", regard=(-1, 0.4), **COUSINE))
    S.add(personne(400, 560, 0.9, expr="content", bras="mains_jointes", regard=(0, 0.6), **MAMAN))
    return S


def p08():
    """Gros plan : la toupie tourne ; on voit ses lettres hébraïques."""
    S = Scene()
    salon(S)
    S.add(tapis(400, 720, 330, 60, "#74c0fc", BLEU))
    S.add(toupie(400, 700, 1.6, rot=8, tourne=True))
    S.add(piece_chocolat(250, 720, 1.4), piece_chocolat(560, 730, 1.4))
    S.camera(1.15, 400, 540)
    S.dessus(texte(400, 100, "Un grand miracle a eu lieu là-bas !", 36, BLEU, contour="#fff"))
    return S


def p09():
    """Plan moyen : chaque soir, une bougie de plus, de un à huit."""
    S = Scene()
    salon(S, nuit_=False)
    S.ambiance("interieur")
    for k in range(8):
        cx, cy = 110 + (k % 4) * 195, 360 + (k // 4) * 260
        S.add(hanoukkia(cx, cy, 0.38, allumees=k + 1))
        S.add(texte(cx, cy + 40, f"soir {k + 1}", 26, BLEU, contour="#fff"))
    S.add(texte(400, 110, "Chaque soir, une bougie de plus !", 42, BLEU, contour="#fff"))
    S.cachette(740, 770)
    return S


def p10():
    """Plan large : le huitième soir, toutes les bougies brillent à la fenêtre ; la famille chante."""
    S = Scene()
    salon(S)
    fenetre_neige(S, 180, 90, 440, 300)
    S.add(rect(150, 400, 500, 20, "#fff", rx=4))
    S.add(hanoukkia(400, 400, 0.85, allumees=8, S=S))
    S.add(personne(130, 790, 1.2, expr="chante", bras="epaule", regard=(1, 0), **PAPA))
    S.add(noam(280, 790, 1.05, expr="chante", bras="main", regard=(1, -0.4)))
    S.add(personne(430, 790, 1.15, expr="chante", bras="main", flip=True, regard=(-1, -0.2), **MAMAN))
    S.add(personne(560, 790, 1.15, expr="content", bras="mains_jointes", regard=(-1, 0), **SAVTA))
    S.add(personne(690, 790, 1.0, expr="chante", bras="ouverts", regard=(-1, 0), **COUSINE))
    S.add(notes(640, 480, 0.9, BLEU), notes(170, 480, 0.8, BLEU))
    S.cachette(70, 150, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("hanoukkia-seule.svg", vignette),
    ("01-ce-soir.svg", p01), ("02-la-legende.svg", p02), ("03-le-chamach.svg", p03),
    ("04-a-la-fenetre.svg", p04), ("05-les-latkes.svg", p05), ("06-latkes-et-beignets.svg", p06),
    ("07-la-toupie.svg", p07), ("08-les-lettres.svg", p08), ("09-une-de-plus.svg", p09),
    ("10-le-huitieme-soir.svg", p10),
]
