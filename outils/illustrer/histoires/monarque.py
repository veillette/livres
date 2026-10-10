"""Le grand voyage du monarque — de l'asclépiade du Québec aux forêts du Mexique.

La femelle pond un œuf sous une feuille d'asclépiade, la seule plante que
mange la chenille ; ses rayures jaunes, noires et blanches disent aux
oiseaux qu'elle a mauvais goût (le poison de l'asclépiade). Elle change cinq
fois de peau, se suspend en J et devient une chrysalide vert jade à points
dorés ; dix jours plus tard, elle devient transparente et le papillon sort.
En été, les monarques vivent quelques semaines ; ceux qui naissent à la fin
de l'été vivent huit mois : ils volent jusqu'au Mexique, environ 4 000 km,
en se guidant sur le Soleil, et passent l'hiver serrés par millions sur les
sapins des montagnes. Au printemps, ils repartent vers le nord ; il faut
trois ou quatre générations pour revenir au Québec.

Plans : 1 large (le champ d'asclépiades) · 2 gros plan (l'œuf, à la loupe)
· 3 moyen (la petite chenille) · 4 moyen (la grosse chenille, l'oiseau) ·
5 gros plan (la chrysalide) · 6 gros plan (le papillon sort) · 7 large (le
nectar d'été) · 8 large (le départ, la carte) · 9 large (les sapins du
Mexique) · 10 large (le retour, de génération en génération) · 11 schéma
(le cycle).
"""
from base import *
from base import _assombrir
from animaux import loupe, etiquette, cycle, disque
from sciences import fleche

ID = "monarque"

ORANGE = "#f76707"
NOIR = "#212529"
OR_ = "#fcc419"


def aile_avant(sgn=1):
    """Aile antérieure (repère : attache au corps en (0, 0), aile vers sgn)."""
    d = f"M 0 -6 Q {sgn * 40} -70 {sgn * 120} -84 Q {sgn * 140} -80 {sgn * 132} -50 Q {sgn * 110} -10 {sgn * 20} 10 Z"
    m = [chemin(d, NOIR),
         chemin(f"M {sgn * 6} -6 Q {sgn * 42} -60 {sgn * 112} -72 Q {sgn * 124} -66 {sgn * 118} -48 Q {sgn * 96} -14 {sgn * 18} 4 Z", volume(ORANGE, 0.4, 0.8))]
    for k in range(4):
        m.append(chemin(f"M {sgn * 10} -2 Q {sgn * (40 + k * 10)} {-30 - k * 8} {sgn * (80 + k * 10)} {-60 + k * 10}", stroke=NOIR, sw=3))
    for k in range(7):
        t = k / 6
        m.append(cercle(sgn * (126 - t * 20), -78 + t * 50, 3, "#fff"))
    m.append(cercle(sgn * 100, -74, 4, "#ffd8a8"))
    return g(m)


def aile_arriere(sgn=1):
    d = f"M 0 4 Q {sgn * 30} 0 {sgn * 90} 20 Q {sgn * 110} 60 {sgn * 70} 90 Q {sgn * 30} 100 {sgn * 6} 30 Z"
    m = [chemin(d, NOIR),
         chemin(f"M {sgn * 6} 10 Q {sgn * 30} 6 {sgn * 82} 24 Q {sgn * 98} 58 {sgn * 66} 80 Q {sgn * 32} 88 {sgn * 10} 30 Z", volume(ORANGE, 0.4, 0.8))]
    for k in range(4):
        m.append(chemin(f"M {sgn * 8} 16 Q {sgn * (30 + k * 6)} {30 + k * 8} {sgn * (60 + k * 6)} {40 + k * 12}", stroke=NOIR, sw=3))
    for k in range(6):
        t = k / 5
        m.append(cercle(sgn * (88 - t * 40), 34 + t * 50, 2.6, "#fff"))
    return g(m)


def monarque(x, y, s=1.0, rot=0, battement=1.0, visage=True):
    """Monarque vu de dessus, ailes ouvertes ; (x, y) = centre du corps.
    battement < 1 : ailes à demi relevées (en vol)."""
    m = []
    for sgn in (-1, 1):
        m.append(g([aile_arriere(sgn), aile_avant(sgn)], None if battement == 1 else f"scale({n(battement, 3)} 1)"))
    m += [ellipse(0, 10, 9, 44, NOIR), cercle(0, -40, 12, NOIR)]
    for k in range(4):
        m.append(cercle(-3 + (k % 2) * 6, -10 + k * 12, 1.8, "#fff"))
    m += [chemin("M -4 -50 Q -14 -80 -24 -92", stroke=NOIR, sw=3), chemin("M 4 -50 Q 14 -80 24 -92", stroke=NOIR, sw=3),
          cercle(-24, -94, 4, NOIR), cercle(24, -94, 4, NOIR)]
    if visage:
        m += [cercle(-5, -42, 3, "#fff"), cercle(5, -42, 3, "#fff"), cercle(-5, -42, 1.5, NOIR), cercle(5, -42, 1.5, NOIR)]
    return place(m, x, y, s, rot=rot) + occuper(x - 140 * s, y - 100 * s, x + 140 * s, y + 100 * s)


def monarque_profil(x, y, s=1.0, flip=False, rot=0):
    """Monarque posé, ailes fermées (vu de côté) ; (x, y) = les pattes."""
    m = [chemin("M 0 -20 Q -20 -120 30 -150 Q 70 -150 74 -110 Q 70 -60 10 -20 Z", NOIR),
         chemin("M 6 -26 Q -10 -112 30 -140 Q 62 -140 66 -110 Q 62 -66 12 -28 Z", volume("#ffa94d", 0.4, 0.8)),
         chemin("M 0 -20 Q 60 -60 90 -40 Q 90 0 10 -14 Z", NOIR), chemin("M 6 -22 Q 56 -54 82 -40 Q 82 -8 12 -16 Z", volume("#ffa94d", 0.4, 0.8))]
    for k in range(5):
        m.append(chemin(f"M 10 -24 Q {20 + k * 8} {-60 - k * 12} {30 + k * 10} {-110 + k * 6}", stroke=NOIR, sw=2.5))
    m += [ellipse(-6, -18, 30, 7, NOIR, rot=-20), cercle(-34, -30, 8, NOIR), chemin("M -36 -36 Q -50 -60 -60 -66", stroke=NOIR, sw=2.5),
          trait(-14, -12, -20, 4, NOIR, 2), trait(0, -12, 2, 4, NOIR, 2)]
    return place(m, x, y, s, flip=flip, rot=rot)


def chenille(x, y, s=1.0, rot=0, flip=False, mange=False):
    """Chenille du monarque, rayée de jaune, de noir et de blanc ; (x, y) = sous le milieu, tête à droite."""
    m = []
    for k in range(11):
        cx = -100 + k * 20
        cy = -22 - math.sin(k / 10 * math.pi) * 10
        m.append(ellipse(cx, cy, 15, 21, "#fff"))
        m.append(ellipse(cx, cy, 15, 21, "none", stroke=NOIR, stroke_width=6))
        m.append(ellipse(cx, cy - 6, 14, 5, "#fcc419"))
    m += [cercle(110, -28, 18, NOIR), chemin("M 100 -42 Q 104 -70 124 -78", stroke=NOIR, sw=4), chemin("M -100 -40 Q -110 -66 -128 -70", stroke=NOIR, sw=4),
          cercle(116, -32, 3, "#fff"), trait(96, -16, 96, -2, NOIR, 3)]
    for k in range(8):
        m.append(trait(-80 + k * 24, -6, -82 + k * 24, 0, NOIR, 3))
    if mange:
        m.append(chemin("M 124 -24 q 8 4 4 10", stroke=NOIR, sw=2))
    return place(m, x, y, s, rot=rot, flip=flip)


def chrysalide(x, y, s=1.0, transparente=False):
    """Chrysalide vert jade à points dorés, suspendue ; (x, y) = l'attache en haut."""
    corps = "M 0 0 Q -34 30 -30 90 Q -24 130 0 140 Q 24 130 30 90 Q 34 30 0 0 Z"
    m = [trait(0, -12, 0, 4, NOIR, 4)]
    if transparente:
        m += [chemin(corps, "#343a40"), chemin("M -20 40 Q -26 90 0 120 Q 22 90 20 40 Z", ORANGE),
              chemin("M -16 50 Q -2 80 -10 110 M 6 50 Q 2 80 12 106", stroke=NOIR, sw=3)]
    else:
        m += [chemin(corps, volume("#8ce99a", 0.45, 0.75)), chemin("M -28 44 Q 0 52 28 44", stroke=NOIR, sw=4),
              chemin("M -28 48 Q 0 56 28 48", stroke=OR_, sw=3)]
        for px, py in ((-16, 100), (16, 100), (-8, 120), (8, 120), (-20, 30), (20, 30)):
            m.append(cercle(px, py, 3.2, "#fcc419"))
    return place(m, x, y, s)



def oeuf(x, y, s=1.0):
    m = [chemin("M -8 0 Q -10 -18 0 -22 Q 10 -18 8 0 Z", volume("#fff3bf", 0.4, 0.8))]
    for dx in (-4, 0, 4):
        m.append(trait(dx, -2, dx * 0.6, -20, "#e9d8a6", 1))
    return place(m, x, y, s)


def asclepiade(x, y, s=1.0, h=420, fleurs=True, gousses=False, graine=1):
    """Asclépiade : tige droite, grandes feuilles ovales opposées, boules de fleurs roses ; (x, y) = pied."""
    m = [trait(0, 0, 0, -h, "#5c940d", 8)]
    for k in range(int(h / 80)):
        yy = -60 - k * 80
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 56, yy, 58, 22, volume("#74b816", 0.4, 0.75), rot=sgn * -18))
            m.append(trait(sgn * 6, yy + 2, sgn * 104, yy - 14, "#a9e34b", 2))
    if fleurs:
        for dx, dy in ((0, -h - 20), (-46, -h + 50), (46, -h + 60)):
            for k in range(10):
                a = math.radians(k * 36)
                m.append(cercle(dx + math.cos(a) * 18, dy + math.sin(a) * 14, 8, "#f783ac"))
            m.append(cercle(dx, dy, 10, "#e64980"))
    if gousses:
        m.append(ellipse(30, -h * 0.55, 14, 40, "#94d82d", rot=20))
    return place(m, x, y, s)


def champ(S, horizon=560, graine=1, haut="#74c0fc", bas="#e7f5ff", nb=5):
    paysage(S, horizon, horizon + 60, "#94d82d", "#c0eb75", haut, bas, graine=graine, nuages=((620, 120, 0.6),))
    r = random.Random(graine)
    for k in range(nb):
        S.add(asclepiade(r.uniform(40, 760), r.uniform(horizon + 100, 800), r.uniform(0.5, 0.8), 380, graine=graine + k))


def feuille_gros(S, cx=400, cy=430, rot=-12):
    """Une grande feuille d'asclépiade au premier plan (gros plans)."""
    S.add(place([ellipse(0, 0, 340, 130, volume("#74b816", 0.4, 0.75)), trait(-330, 0, 330, 0, "#a9e34b", 6)]
                + [trait(-260 + k * 90, 0, -200 + k * 90, -110, "#a9e34b", 3) for k in range(6)]
                + [trait(-260 + k * 90, 0, -200 + k * 90, 110, "#a9e34b", 3) for k in range(6)], cx, cy, rot=rot))


def carte(S):
    """Carte schématique de l'Amérique du Nord : le chemin du Québec au Mexique."""
    fond(S, "#a5d8ff")
    terre = ("M 120 60 L 330 40 L 520 70 L 680 60 L 760 140 L 700 230 L 640 260 L 600 330 L 560 360 L 530 420 L 470 470 "
             "L 430 540 L 400 610 L 360 660 L 330 720 L 290 700 L 250 640 L 210 560 L 160 470 L 120 380 L 90 280 L 80 160 Z")
    S.add(chemin(terre, "#b2f2bb", stroke="#69db7c", sw=4))
    S.add(chemin("M 160 470 L 120 380 L 90 280", stroke="#adb5bd", sw=10, opacity=0.6))
    S.add(ellipse(470, 230, 60, 22, "#a5d8ff"), ellipse(540, 250, 40, 16, "#a5d8ff"))
    S.add(cercle(640, 210, 12, "#e03131"), etiquette(640, 180, "Québec", 30, "#c92a2a"))
    S.add(cercle(330, 660, 12, "#e03131"), etiquette(330, 700, "Mexique", 30, "#c92a2a"))
    S.add(chemin("M 630 220 Q 560 400 345 650", stroke=ORANGE, sw=8, stroke_dasharray="18 14"))
    S.add(fleche(400, 590, 345, 650, ORANGE, sw=8, tete=26))
    S.add(etiquette(640, 520, "4 000 km !", 40, ORANGE))
    S.cachette(90, 760, "air")


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    champ(S, 560, graine=2, nb=3)
    S.add(asclepiade(160, 800, 1.1, 460))
    S.add(asclepiade(660, 810, 1.0, 420))
    S.add(monarque(420, 360, 1.4, rot=-10))
    S.add(monarque(620, 230, 0.6, rot=20, battement=0.6))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(monarque(200, 140, 0.95, rot=-8))
    return S


def p01():
    """Plan large : l'été, dans un champ d'asclépiades, des monarques volent."""
    S = Scene()
    champ(S, 560, graine=3, nb=6)
    S.add(soleil(120, 120, 50))
    S.add(monarque(420, 300, 0.75, rot=-15), monarque(600, 220, 0.5, rot=10, battement=0.7))
    S.add(monarque_profil(260, 610, 0.7))
    return S


def p02():
    """Gros plan : sous une feuille d'asclépiade, la femelle pond un œuf ; une loupe le montre."""
    S = Scene()
    paysage(S, 560, 620, "#94d82d", "#c0eb75", graine=4)
    feuille_gros(S, 380, 300, rot=-8)
    S.add(monarque_profil(420, 400, 1.6, rot=180, flip=True))
    S.add(oeuf(300, 330, 1.2))
    contenu = g([rect(40, 500, 360, 260, "#94d82d"), place(oeuf(0, 0, 4.0), 220, 700)])
    S.add(loupe(220, 620, 130, contenu, rot=-40))
    S.add(etiquette(220, 465, "un œuf", 34, "#2b8a3e"))
    return S


def p03():
    """Plan moyen : la petite chenille sort de l'œuf et mange la feuille d'asclépiade."""
    S = Scene()
    paysage(S, 540, 600, "#94d82d", "#c0eb75", graine=5)
    feuille_gros(S, 400, 480, rot=-6)
    S.add(chenille(380, 470, 0.9, mange=True))
    S.add(chemin("M 540 400 q 20 20 40 0 q 20 -20 40 0 L 620 500 Z", "#e7f5ff"))
    S.add(texte(400, 160, "Scrountch ! Scrountch !", 46, "#2b8a3e", contour="#fff"))
    S.cachette(740, 760)
    return S


def p04():
    """Plan moyen : la grosse chenille rayée ; un oiseau l'évite, elle a mauvais goût."""
    S = Scene()
    champ(S, 560, graine=6, nb=2)
    S.add(asclepiade(330, 800, 1.5, 420, fleurs=False))
    S.add(chenille(330 + 90, 800 - 300, 1.0, rot=-30))
    S.add(oiseau(640, 470, 0.9, "#fab005", expr="degoute", flip=True, ailes="ouvertes"))
    S.add(bulle(620, 260, 260, 80, "Pouah !", 40, pointe=(640, 380)))
    return S


def p05():
    """Gros plan : la chenille, suspendue en J, devient une chrysalide vert jade à points dorés."""
    S = Scene()
    paysage(S, 560, 620, "#94d82d", "#c0eb75", graine=7)
    S.add(trait(0, 200, 800, 160, "#5c940d", 14))
    S.add(place(chenille(0, 0, 0.8, rot=90), 240, 210))
    S.add(fleche(330, 330, 450, 330, "#2b8a3e", sw=8))
    S.add(chrysalide(560, 176, 1.6))
    S.add(etiquette(240, 520, "en J", 34, "#2b8a3e"), etiquette(560, 520, "la chrysalide", 34, "#2b8a3e"))
    S.cachette(740, 740)
    return S


def p06():
    """Gros plan : dix jours plus tard, la chrysalide devient transparente ; le papillon sort et fait sécher ses ailes."""
    S = Scene()
    paysage(S, 560, 620, "#94d82d", "#c0eb75", graine=8)
    S.add(trait(0, 160, 800, 140, "#5c940d", 14))
    S.add(chrysalide(220, 152, 1.3, transparente=True))
    S.add(rect(500, 140, 14, 30, "#adb5bd", opacity=0.6))
    S.add(place(monarque_profil(0, 0, 1.0, rot=180), 520, 170, 1.7))
    S.add(texte(400, 640, "Il fait sécher ses ailes…", 40, ORANGE, contour="#fff"))
    S.cachette(740, 740)
    return S


def p07():
    """Plan large : en été, les monarques boivent le nectar des fleurs."""
    S = Scene()
    champ(S, 560, graine=9, nb=4)
    for x, c in ((140, "#cc5de8"), (330, "#ff8787"), (520, "#ffd43b"), (700, "#cc5de8")):
        S.add(fleur(x, 790, 1.6, c, tige=170))
    S.add(monarque_profil(330, 620, 0.8), monarque_profil(520, 610, 0.7, flip=True))
    S.add(monarque(650, 300, 0.6, rot=20, battement=0.7))
    S.add(texte(400, 200, "Slurp ! Du nectar !", 46, ORANGE, contour="#fff"))
    return S


def p08():
    """Plan large : la carte : à la fin de l'été, les monarques partent du Québec vers le Mexique."""
    S = Scene()
    carte(S)
    for k in range(4):
        S.add(monarque(600 - k * 60, 290 + k * 80, 0.3, rot=-140, battement=0.7, visage=False))
    S.add(soleil(150, 140, 40))
    return S


def sapin_monarques(x, y, s=1.0, graine=1):
    """Sapin des montagnes du Mexique, couvert de monarques serrés les uns contre les autres."""
    r = random.Random(graine)
    m = [sapin(0, 0, 1.0, "#2b8a3e", "#2f9e44")]
    for k in range(70):
        py = r.uniform(-260, -30)
        demi = 70 * (py + 290) / 260
        m.append(ellipse(r.uniform(-demi, demi), py, 8, 5, r.choice((ORANGE, "#e8590c", "#ff922b")), rot=r.uniform(-30, 30)))
    return place(m, x, y, s)


def p09():
    """Plan large : l'hiver, dans les montagnes du Mexique, des millions de monarques sur les sapins."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(g(pic(-100, 560, 150, 260, 420, 560, "#91a7ff", neige=False), opacity=0.7), g(pic(300, 560, 560, 230, 860, 560, "#91a7ff", neige=False), opacity=0.7))
    sol(S, 620, "#8ce99a")
    for k, (x, sc) in enumerate(((120, 1.6), (330, 1.9), (560, 1.7), (740, 1.4))):
        S.add(sapin_monarques(x, 720 + (k % 2) * 30, sc, graine=k + 1))
    for k in range(10):
        S.add(monarque(100 + k * 70, 200 + (k % 3) * 40, 0.2, rot=k * 30, battement=0.6, visage=False))
    S.add(texte(400, 100, "Des millions de papillons !", 46, ORANGE, contour="#fff"))
    return S


def p10():
    """Plan large : au printemps, les monarques repartent vers le nord, de génération en génération."""
    S = Scene()
    champ(S, 560, graine=10, nb=5, haut="#a5d8ff", bas="#fff9db")
    S.add(monarque(200, 360, 0.5, rot=30, battement=0.7), monarque(420, 260, 0.45, rot=40, battement=0.6), monarque(620, 180, 0.4, rot=35, battement=0.7))
    S.add(chemin("M 120 440 Q 400 360 700 120", stroke=ORANGE, sw=5, stroke_dasharray="14 12"))
    S.add(texte(400, 650, "Arrière-petits-enfants…", 36, ORANGE, contour="#fff"))
    S.add(texte(400, 700, "bienvenue chez nous !", 36, ORANGE, contour="#fff"))
    return S


def p11():
    """Schéma : le cycle du monarque : l'œuf, la chenille, la chrysalide, le papillon."""
    S = Scene()
    fond(S, "#fff4e6")
    S.add(cycle(400, 400, 250, ORANGE, nb=4, ecart=30))
    S.add(disque(400, 150, 105, "#ebfbee"), oeuf(400, 180, 3.0))
    S.add(disque(650, 400, 105, "#ebfbee"), chenille(650, 430, 0.6))
    S.add(disque(400, 650, 105, "#ebfbee"), chrysalide(400, 570, 0.95))
    S.add(disque(150, 400, 105, "#ebfbee"), monarque(150, 400, 0.6))
    S.add(etiquette(400, 290, "l'œuf", 30, "#d9480f"), etiquette(650, 540, "la chenille", 30, "#d9480f"),
          etiquette(400, 790, "la chrysalide", 30, "#d9480f"), etiquette(150, 540, "le papillon", 30, "#d9480f"))
    S.cachette(630, 730, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("monarque-seul.svg", vignette),
    ("01-le-champ.svg", p01), ("02-l-oeuf.svg", p02), ("03-la-petite-chenille.svg", p03),
    ("04-pouah.svg", p04), ("05-la-chrysalide.svg", p05), ("06-le-papillon-sort.svg", p06),
    ("07-le-nectar.svg", p07), ("08-la-carte.svg", p08), ("09-les-sapins-du-mexique.svg", p09),
    ("10-le-retour.svg", p10), ("11-le-cycle.svg", p11),
]
