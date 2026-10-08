"""Le Rat et l'Huître — tel est pris qui croyait prendre.

Adaptation douce : l'huître pince seulement le bout du nez du rat. Quand la
marée monte et que l'eau la recouvre, elle s'entrouvre (les huîtres s'ouvrent
sous l'eau pour se nourrir) et le rat retrouve sa liberté.
"""
from fables import *
from contes import baluchon

ID = "rat-huitre"
COQUILLE = "#a69986"
COQUILLE2 = "#8c7f6d"
NACRE = "#f8f0fa"


def rat(x, y, s=1.0, **k):
    k.setdefault("habit", "#74c0fc")
    return perso("rat", x, y, s, **k)


def huitre(x, y, s=1.0, ouverture=0, rot=0, perle_=False, brille=False, contour=None):
    """Huître posée ; `ouverture` en degrés (0 = fermée). (x, y) = dessous."""
    bas = chemin("M -80 -20 Q -86 -4 -60 4 Q 0 14 60 4 Q 92 -6 86 -26 Q 40 -40 0 -34 Q -50 -36 -80 -20 Z", COQUILLE)
    stries = g([chemin(f"M {-60 + k * 24} -2 q 6 -12 2 -26", stroke=COQUILLE2, sw=3) for k in range(6)])
    m = [bas, stries]
    if ouverture:
        m.append(ellipse(4, -28, 74, 14, NACRE))
        m.append(ellipse(10, -28, 30, 8, "#e5dbff"))
        if brille:
            m.append(eclat(10, -60, 0.9, "#fff3bf"))
    haut = chemin("M -80 -26 Q -60 -60 0 -62 Q 70 -64 86 -30 Q 40 -40 0 -36 Q -50 -38 -80 -26 Z", "#b5a896", **({"stroke": contour, "sw": 6} if contour else {}))
    m.append(place([place([haut, g([chemin(f"M {-50 + k * 24} -40 q 8 -8 4 -18", stroke=COQUILLE2, sw=3) for k in range(5)])], 80, 26)],
                   -80, -26, rot=-ouverture))
    return place(m + [occuper(-81, -62, 87, 9)], x, y, s, rot=rot)


def huitre_nez(x, y, s=1.0, rot=0):
    """Petite huître fermée, accrochée au bout d'un museau (centre = le nez)."""
    return place(huitre(0, 10, 0.36, contour="#495057"), x, y, s, rot=rot)


def nez_rat(x, y, s):
    """Position du bout du nez d'un rat dessiné par perso() en (x, y) à l'échelle s."""
    return x, y - 132 * s


def plage(S, mer_y=440, sable="#f4d58d", ciel_=("#74c0fc", "#e7f5ff"), soleil_=True):
    ciel(S, *ciel_)
    if soleil_:
        S.add(soleil(680, 100, 45))
    S.add(rect(0, mer_y - 20, 800, 140, "#339af0"))
    for k in range(6):
        S.add(chemin(f"M {40 + k * 140} {mer_y + 10 + (k % 2) * 30} q 25 -12 50 0", stroke="#a5d8ff", sw=5))
    S.add(chemin(f"M 0 {mer_y + 100} Q 200 {mer_y + 70} 400 {mer_y + 100} T 800 {mer_y + 90} L 800 800 L 0 800 Z", sable))
    S.add(chemin(f"M 0 {mer_y + 100} Q 200 {mer_y + 70} 400 {mer_y + 100} T 800 {mer_y + 90}", stroke="#fff", sw=6, opacity=0.7))
    for k in range(16):
        S.add(cercle(30 + (k * 97) % 760, mer_y + 140 + (k * 53) % 200, 3, "#e8c170"))


def pre_(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 110, 45))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a")


def couverture():
    S = Scene()
    plage(S, 400)
    S.add(huitre(520, 720, 2.6, ouverture=30, brille=True))
    S.add(rat(260, 780, 1.4, expr="miam", bras="joues", regard=(1, 0.3)))
    S.add(crabe(700, 560, 0.6, expr="rire"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rat(170, 264, 1.0, expr="oups", bras="bas"))
    x, y = nez_rat(170, 264, 1.0)
    S.add(huitre_nez(x, y, 1.2))
    S.add(eclat(x + 90, y - 40, 0.7, "#fa5252"))
    return S


def p01():
    S = Scene()
    pre_(S, 1)
    S.add(chemin("M 120 600 Q 120 520 200 520 Q 280 520 280 600 Z", "#a0693a"), chemin("M 160 600 Q 160 560 200 560 Q 240 560 240 600 Z", "#3b2410"))
    S.add(rat(430, 780, 1.4, expr="fier", bras="tient", objet=baluchon(80, -150, 1.0)))
    S.add(texte(600, 280, "En route !", 64, "#e8590c", contour="#fff", rot=-6))
    return S


def p02():
    S = Scene()
    pre_(S, 2)
    S.add(chemin("M 80 620 Q 260 160 460 620 Z", "#8d5524"), chemin("M 180 420 q 30 -20 60 0", stroke="#6d4424", sw=6))
    S.add(flaque(640, 760, 2.0))
    S.add(rat(560, 740, 0.85, expr="bouche_bee", bras="ouverts", regard=(-1, -1)))
    S.add(texte(270, 160, "Une montagne !", 50, "#e8590c", contour="#fff"))
    S.add(texte(620, 470, "Un océan !", 44, "#1c7ed6", contour="#fff"))
    return S


def p03():
    S = Scene()
    plage(S, 400)
    S.add(rat(400, 760, 1.3, expr="bouche_bee", bras="haut", objet=""))
    S.add(oiseau(150, 200, 0.5, "#f8f9fa", "#fff", ailes="haut"), oiseau(230, 160, 0.4, "#f8f9fa", "#fff", ailes="haut"))
    S.add(coquillage(620, 700, 1.2), coquillage(140, 740, 0.9, "#ffd8a8", rot=30))
    return S


def p04():
    S = Scene()
    plage(S, 400)
    for k, (x, y, s) in enumerate([(160, 640, 1.2), (330, 600, 1.0), (520, 650, 1.3), (690, 610, 1.0)]):
        S.add(huitre(x, y, s))
    S.add(rat(400, 790, 1.0, expr="surpris", bras="montre", regard=(1, -0.5)))
    S.add(bulle(560, 260, 340, 90, "Des navires !", 42, pointe=(450, 560)))
    return S


def p05():
    S = Scene()
    plage(S, 380)
    S.add(cercle(400, 640, 220, "#fff3bf", opacity=0.35))
    S.add(huitre(400, 720, 3.2, ouverture=32, brille=True))
    S.add(soleil(680, 100, 45, visage=True))
    return S


def p06():
    S = Scene()
    plage(S, 400)
    S.add(huitre(560, 720, 2.4, ouverture=32, brille=True))
    S.add(rat(260, 790, 1.35, expr="miam", bras="porte", regard=(1, 0.5), objet=""))
    S.add(texte(250, 230, "Quel festin !", 60, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    plage(S, 400)
    S.add(rat(400, 790, 1.7, expr="oups", bras="ouverts"))
    x, y = nez_rat(400, 790, 1.7)
    S.add(huitre_nez(x, y, 1.9))
    S.add(eclat(x - 150, y - 40, 1.2, "#fa5252"), eclat(x + 150, y - 40, 1.2, "#fa5252"))
    S.add(texte(400, 200, "CLAC !", 110, "#c92a2a", contour="#fff"))
    return S


def p08():
    S = Scene()
    plage(S, 400)
    S.add(place(rat(0, 0, 1.5, expr="pleure", bras="tete", larmes=True), 400, 790, rot=-8))
    x, y = 400 - 132 * 1.5 * math.sin(math.radians(-8)), 790 - 142 * 1.5 * math.cos(math.radians(-8))
    S.add(huitre_nez(x, y, 1.6, rot=-8))
    S.add(mouvement(200, 420, 1.3, rot=200), mouvement(600, 420, 1.3, rot=-20))
    S.add(texte(400, 160, "Aïe, aïe, aïe !", 70, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    plage(S, 400)
    S.add(rat(260, 790, 1.3, expr="triste", bras="croises"))
    x, y = nez_rat(260, 790, 1.3)
    S.add(huitre_nez(x, y, 1.4))
    S.add(crabe(600, 760, 1.4, expr="rire"))
    S.add(texte(600, 400, "Ha ha ha !", 56, "#e03131", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(200, 120, 0.8), nuage(600, 90, 0.6))
    S.add(rect(0, 380, 800, 260, "#339af0"))
    S.add(chemin("M 0 600 Q 100 540 200 600 T 400 600 T 600 600 T 800 600 L 800 660 L 0 660 Z", "#fff", opacity=0.9))
    S.add(chemin("M 0 640 Q 200 620 400 650 T 800 640 L 800 800 L 0 800 Z", "#f4d58d"))
    S.add(rat(400, 790, 1.3, expr="inquiet", bras="bas", regard=(-1, -0.5)))
    x, y = nez_rat(400, 790, 1.3)
    S.add(huitre_nez(x, y, 1.4))
    S.add(fleche(200, 520, 300, 600, "#1c7ed6", 6, 22), fleche(620, 520, 540, 600, "#1c7ed6", 6, 22))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 360, 800, 440, "#339af0"))
    S.add(chemin("M 0 420 Q 120 330 240 420 T 480 420 T 720 420 T 960 420 L 960 470 L 0 470 Z", "#fff", opacity=0.9))
    S.add(huitre(240, 720, 2.0, ouverture=24))
    S.add(bulles_eau(260, 560, 1.0))
    S.add(place(rat(0, 0, 1.2, expr="rire", bras="haut"), 560, 660, rot=14))
    S.add(texte(560, 230, "Libre !", 84, "#2f9e44", contour="#fff"))
    S.cachette(430, 730, "air")
    return S


def p12():
    S = Scene()
    ciel(S, "#ffa94d", "#fff3bf")
    S.add(soleil(640, 360, 70, "#ff922b", rayons=False))
    collines(S, 520, "#94d82d", graine=12)
    sol(S, 560, "#8ce99a")
    S.add(chemin("M 0 760 Q 300 620 800 600", stroke="#e9c38c", sw=50))
    S.add(rat(320, 720, 1.2, expr="sourire", bras="tient", objet=baluchon(80, -150, 0.9), habit="#4dabf7"))
    S.add(cercle(320, 720 - 132 * 1.2, 10, "#fa5252"))
    S.add(g([goutte(250 + k * 40, 560 + (k % 2) * 30, 0.6, "#74c0fc") for k in range(4)]))
    return S


def p13():
    S = Scene()
    fond(S, "#5c3a1e")
    S.add(ellipse(400, 420, 400, 380, "#8d5524"), ellipse(400, 440, 360, 330, "#d9a066"))
    S.add(rect(0, 650, 800, 150, "#a0693a"))
    S.add(bougie(400, 610, 1.3))
    S.add(table(400, 650, 180, 50, "#8d5524"))
    S.add(rat(200, 760, 1.2, expr="rire", bras="ouverts"))
    S.add(cercle(200, 760 - 132 * 1.2, 7, "#ff8787"))
    S.add(rat(560, 760, 1.05, expr="surpris", habit="#f783ac", acc=("noeud",), couleur_acc="#e64980"),
          rat(690, 770, 0.75, expr="rire", habit="#ffd43b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("rat-seul.svg", vignette),
    ("01-en-route.svg", p01), ("02-tout-est-immense.svg", p02), ("03-la-mer.svg", p03), ("04-des-navires.svg", p04),
    ("05-l-huitre-ouverte.svg", p05), ("06-quel-festin.svg", p06), ("07-clac.svg", p07), ("08-aie-aie-aie.svg", p08),
    ("09-le-crabe.svg", p09), ("10-la-mer-monte.svg", p10), ("11-libre.svg", p11), ("12-le-retour.svg", p12),
    ("13-a-la-maison.svg", p13),
]
