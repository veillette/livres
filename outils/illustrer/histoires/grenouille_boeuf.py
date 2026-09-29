"""La Grenouille qui veut se faire aussi grosse que le Bœuf — être bien comme on est."""
from fables import *

ID = "grenouille-boeuf"

VERT = "#69db7c"


def grenouille(x, y, s=1.0, **k):
    return perso("grenouille", x, y, s, **k)


def boeuf(x, y, s=1.0, **k):
    return perso("boeuf", x, y, s, **k)


def grenouille_ronde(x, y, r=120, expr="souffle", rouge=0.0, rot=0):
    """Grenouille gonflée comme un ballon ; (x, y) = centre du ballon."""
    ys, bs, ss = EXPRESSIONS[expr]
    k = r / 100
    m = []
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 70 * k, 84 * k, 26 * k, 14 * k, "#51cf66", rot=sgn * 30))
        m.append(ellipse(sgn * 96 * k, 0, 14 * k, 24 * k, "#51cf66", rot=sgn * 20))
    m.append(cercle(0, 0, r, VERT))
    m.append(ellipse(0, 22 * k, r * 0.7, r * 0.62, "#d8f5a2"))
    if rouge:
        m.append(cercle(0, 0, r, "#ff6b6b", opacity=rouge))
    for sgn in (-1, 1):
        m.append(cercle(sgn * 34 * k, -84 * k, 24 * k, VERT))
    for sgn in (-1, 1):
        m.append(place(oeil(0, 0, ys, (0, 0), sclere=True), sgn * 34 * k, -88 * k, k))
    m.append(place(sourcils(34, -88, ss), 0, 0, k))
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 52 * k, -40 * k, 16 * k, 10 * k, "#ff6b6b", opacity=0.6))
    m.append(place(bouche(0, 0, bs, 1.6), 0, -36 * k, k))
    return place(m, x, y, 1.0, rot=rot)


def mare(S, ciel_haut="#a5d8ff", ciel_bas="#e7f5ff", y=560):
    ciel(S, ciel_haut, ciel_bas)
    S.add(nuage(140, 110, 0.6), nuage(600, 150, 0.5))
    collines(S, y - 20, "#b2f2bb", graine=8)
    sol(S, y, "#8ce99a")
    S.add(ellipse(400, y + 150, 460, 150, "#4dabf7"))
    S.add(ellipse(400, y + 150, 420, 120, "#74c0fc"))
    for rx, ry in ((70, y + 20), (740, y + 30)):
        S.add(g([trait(rx + dx, ry + 40, rx + dx * 2, ry - 70 - abs(dx) * 2, "#5c940d", 5) for dx in (-10, 0, 10)]))
        S.add(ellipse(rx + 2, ry - 70, 7, 22, "#8d5524"))


def soeurs(S, xs=((150, 690), (650, 700)), expr="neutre", bras="bas"):
    for x_, y_ in xs:
        S.add(nenuphar(x_, y_ + 6, 0.8))
        S.add(grenouille(x_, y_, 0.6, expr=expr, bras=bras))


def couverture():
    S = Scene()
    mare(S)
    S.add(boeuf(560, 640, 1.8, expr="surpris", regard=(-1, 0)))
    S.add(grenouille_ronde(270, 480, 150, expr="souffle", rouge=0.1))
    S.add(nenuphar(270, 690, 1.3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(grenouille(200, 250, 1.0, expr="rire", bras="haut"))
    return S


def p01():
    S = Scene()
    mare(S)
    S.add(nenuphar(300, 700, 1.4), nenuphar(560, 720, 1.0, "#ffc9d6"))
    S.add(grenouille(300, 690, 1.3, expr="rire", bras="haut", pieds_haut=True))
    S.add(texte(560, 330, "Croâ !", 64, "#2b8a3e", contour="#fff"))
    return S


def p02():
    S = Scene()
    mare(S)
    S.add(boeuf(470, 640, 2.2, expr="content"))
    S.add(nenuphar(160, 700, 1.0))
    S.add(grenouille(160, 692, 0.6, expr="surpris", regard=(1, -1)))
    return S


def p03():
    S = Scene()
    mare(S)
    S.add(boeuf(600, 630, 1.9, expr="sourire", regard=(-1, 1)))
    S.add(nenuphar(240, 700, 1.4))
    S.add(grenouille(240, 690, 1.1, expr="bouche_bee", bras="joues", regard=(1, -1)))
    S.add(bulle(240, 170, 360, 100, "Qu'il est gros !", 38, pointe=(240, 400)))
    return S


def p04():
    S = Scene()
    mare(S)
    S.add(boeuf(620, 630, 1.7, expr="sourire", regard=(-1, 1)))
    S.add(nenuphar(260, 700, 1.4))
    S.add(grenouille(260, 690, 1.2, expr="concentre", bras="poing"))
    S.add(bulle(270, 150, 420, 110, "Moi aussi, je veux\nêtre aussi grosse !", 34, pointe=(260, 400)))
    return S


def p05():
    S = Scene()
    mare(S)
    S.add(boeuf(640, 630, 1.6, expr="sourire", regard=(-1, 1)))
    S.add(nenuphar(330, 700, 1.4))
    S.add(grenouille_ronde(330, 600, 90, "souffle"))
    soeurs(S, xs=((120, 700),))
    S.add(bulle(330, 150, 420, 100, "Est-ce assez ?", 40, pointe=(330, 480)))
    return S


def p06():
    S = Scene()
    mare(S)
    S.add(nenuphar(400, 700, 1.4))
    S.add(grenouille_ronde(400, 600, 90, "inquiet"))
    soeurs(S, xs=((150, 690), (650, 700)), expr="rire")
    S.add(bulle(170, 170, 260, 90, "Nenni !", 44, pointe=(160, 560)))
    S.add(bulle(630, 170, 280, 90, "Pas du tout !", 36, pointe=(650, 570)))
    return S


def p07():
    S = Scene()
    mare(S)
    S.add(nenuphar(400, 700, 1.4))
    S.add(grenouille_ronde(400, 540, 150, "souffle", rouge=0.05))
    soeurs(S, xs=((110, 700), (690, 710)), expr="surpris")
    S.add(bulle(400, 110, 400, 90, "M'y voici donc ?", 38, pointe=(400, 370)))
    return S


def p08():
    S = Scene()
    mare(S)
    S.add(grenouille_ronde(400, 470, 220, "souffle", rouge=0.12))
    soeurs(S, xs=((100, 700), (700, 710)), expr="oups", bras="joues")
    S.add(texte(400, 760, "Pfffff !", 50, "#2b8a3e", contour="#fff"))
    return S


def p09():
    S = Scene()
    mare(S)
    S.add(grenouille_ronde(400, 330, 200, "inquiet", rouge=0.1))
    S.add(trait(400, 530, 400, 640, "#495057", 3, opacity=0.4))
    soeurs(S, xs=((150, 700), (650, 710)), expr="bouche_bee", bras="joues")
    return S


def p10():
    S = Scene()
    mare(S)
    S.add(boeuf(560, 640, 1.9, expr="surpris", regard=(-1, -1)))
    S.add(grenouille_ronde(220, 300, 170, "souffle", rouge=0.15))
    S.add(bulle(560, 130, 420, 100, "Mais que fais-tu ?", 38, pointe=(560, 290)))
    return S


def p11():
    S = Scene()
    mare(S)
    S.add(boeuf(620, 640, 1.6, expr="inquiet", regard=(-1, -1)))
    S.add(eclat(290, 330, 3.6, "#ffe066"))
    S.add(grenouille_ronde(290, 330, 230, "furieux", rouge=0.3))
    return S


def p12():
    S = Scene()
    mare(S, ciel_haut="#91a7ff", ciel_bas="#e7f5ff")
    S.add(chemin("M 80 620 Q 200 200 360 480 Q 520 700 600 300 Q 640 160 700 140", stroke="#fff", sw=10, stroke_dasharray="4 26", opacity=0.9))
    S.add(grenouille_ronde(690, 170, 70, "surpris", rot=30))
    S.add(texte(330, 170, "PFFFFUIIIT !", 64, "#2b8a3e", contour="#fff", rot=-6))
    return S


def p13():
    S = Scene()
    mare(S)
    for k in range(7):
        a = math.radians(-160 + k * 23)
        S.add(goutte(400 + math.cos(a) * 110, 640 + math.sin(a) * 90, 1.2, "#74c0fc"))
    S.add(ellipse(400, 690, 120, 24, "#fff", opacity=0.7))
    S.add(grenouille(400, 700, 0.9, expr="oups", bras="haut"))
    S.add(texte(400, 380, "PLOUF !", 80, "#1c7ed6", contour="#fff"))
    return S


def p14():
    S = Scene()
    mare(S)
    S.add(boeuf(550, 640, 1.9, expr="rire", bras="ouverts"))
    S.add(nenuphar(190, 700, 1.3))
    S.add(grenouille(190, 690, 0.9, expr="timide", regard=(1, -1)))
    S.add(bulle(520, 120, 500, 110, "Moi, je ne sais pas\nsauter comme toi !", 36, pointe=(540, 270)))
    return S


def p15():
    S = Scene()
    mare(S, ciel_haut="#74c0fc")
    S.add(boeuf(420, 660, 1.7, expr="rire", regard=(0, -1)))
    S.add(chemin("M 140 640 Q 400 -40 680 620", stroke="#fff", sw=8, stroke_dasharray="4 24"))
    S.add(grenouille(410, 300, 0.8, expr="rire", bras="haut", pieds_haut=True))
    S.add(texte(160, 240, "Hop !", 64, "#2b8a3e", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("grenouille-seule.svg", vignette),
    ("01-la-mare.svg", p01), ("02-le-boeuf.svg", p02), ("03-qu-il-est-gros.svg", p03),
    ("04-moi-aussi.svg", p04), ("05-est-ce-assez.svg", p05), ("06-nenni.svg", p06),
    ("07-m-y-voici.svg", p07), ("08-pfff.svg", p08), ("09-un-ballon.svg", p09),
    ("10-que-fais-tu.svg", p10), ("11-encore-un-peu.svg", p11), ("12-pffuit.svg", p12),
    ("13-plouf.svg", p13), ("14-le-boeuf-rit.svg", p14), ("15-hop.svg", p15),
]
