"""La soupe de la sorcière Zaza — le plaisir de partager (d'après la soupe au caillou)."""
from base import *
from objets import *
from fantastique import *

ID = "sorciere-soupe"
ZAZA = dict(peau="claire", cheveux="roux", habit="#7048e8", chapeau="#5f3dc4")
MINUIT = dict(couleur="#343a40", habit=None)
TOM = dict(coiffure="herisses", cheveux="blond", habit="#fa5252", robe=False, jambes="#1c7ed6", peau="rosee",
           acc=("bonnet_nuit",), couleur_acc="#4dabf7")
LUCIE = dict(coiffure="chignon", cheveux="brun", habit="#20c997", peau="brune", acc=("noeud",), couleur_acc="#fab005")
PAUL = dict(coiffure="courts", cheveux="noir", habit="#e8590c", robe=False, jambes="#495057", peau="doree", barbe="#2b2b3a")
NINO = dict(coiffure="boucles", cheveux="brun", habit="#fab005", robe=False, jambes="#364fc7", peau="foncee")
JO = dict(coiffure="chignon", cheveux="blanc", habit="#e64980", peau="rosee", acc=("lunettes",))


def zaza(x, y, s=1.0, **k):
    return sorciere(x, y, s, **{**ZAZA, **k})


def minuit(x, y, s=1.0, **k):
    return perso("chat", x, y, s, couleur="#343a40", **k)


def place_village(S, gens_dehors=True):
    nuit(S, "#1c2a52", "#4c5b9a")
    etoiles(S, 30, graine=12, zone=(0, 0, 800, 300))
    S.add(maison(110, 560, 0.75, lumiere=True, toit="#c92a2a"), maison(690, 560, 0.7, lumiere=True, toit="#1c7ed6", mur="#fff3bf"))
    S.add(maison(400, 520, 0.5, lumiere=True, toit="#5c940d", mur="#ffe3e3"))
    S.add(rect(0, 560, 800, 240, "#dee2e6"))
    S.add(chemin("M 0 560 Q 200 540 400 560 T 800 555 L 800 800 L 0 800 Z", "#f1f3f5"))
    flocons(S, 35, graine=4, zone=(0, 0, 800, 560))


def carotte(x, y, s=1.0, rot=0):
    m = [chemin("M -14 -50 Q 0 -56 14 -50 L 2 40 Q 0 46 -2 40 Z", "#fd7e14"),
         trait(-8, -30, 2, -32, "#e8590c", 2), trait(-4, -6, 6, -8, "#e8590c", 2),
         chemin("M 0 -50 Q -14 -80 -20 -86 M 0 -50 Q 0 -84 4 -92 M 0 -50 Q 12 -78 20 -84", stroke="#40c057", sw=5)]
    return place(m, x, y, s, rot=rot)


def poireau(x, y, s=1.0, rot=0):
    m = [rect(-12, -20, 24, 70, "#f8f9fa", rx=10), rect(-12, -70, 24, 56, "#d8f5a2", rx=8),
         chemin("M -8 -66 Q -26 -110 -30 -130 M 0 -66 Q 0 -120 4 -140 M 8 -66 Q 26 -106 34 -124", stroke="#40c057", sw=10),
         chemin("M -8 50 l -6 10 M 0 50 l 0 12 M 8 50 l 6 10", stroke="#ced4da", sw=2)]
    return place(m, x, y, s, rot=rot)


def patate(x, y, s=1.0):
    m = [ellipse(0, 0, 26, 20, "#d9a066"), cercle(-8, -4, 2.5, "#a0693a"), cercle(10, 5, 2.5, "#a0693a")]
    return place(m, x, y, s)


def oignon(x, y, s=1.0):
    m = [chemin("M 0 -36 Q 30 -10 26 8 Q 20 28 0 28 Q -20 28 -26 8 Q -30 -10 0 -36 Z", "#e599f7"),
         chemin("M 0 -36 Q 10 -10 8 26 M 0 -36 Q -10 -10 -8 26", stroke="#cc5de8", sw=2),
         chemin("M 0 -36 L -4 -52 M 0 -36 L 4 -54", stroke="#51cf66", sw=4)]
    return place(m, x, y, s)


def persil(x, y, s=1.0):
    m = [trait(0, 0, -10, -50, "#2f9e44", 4), trait(0, 0, 12, -46, "#2f9e44", 4)]
    for px, py in [(-12, -56), (-22, -48), (-4, -64), (14, -52), (22, -42), (8, -62)]:
        m.append(cercle(px, py, 9, "#40c057"))
    return place(m, x, y, s)


def sel(x, y, s=1.0):
    m = [rect(-18, -50, 36, 50, "#fff", rx=6, stroke="#adb5bd", stroke_width=3),
         chemin("M -18 -50 Q 0 -70 18 -50 Z", "#adb5bd"), texte(0, -18, "sel", 16, "#495057")]
    return place(m, x, y, s)


def cuillere(x, y, s=1.0, rot=0):
    m = [rect(-5, -140, 10, 140, "#a0522d", rx=4), ellipse(0, 10, 18, 24, "#a0522d")]
    return place(m, x, y, s, rot=rot)


def bol_soupe(x, y, s=1.0, fumee_=True):
    m = []
    if fumee_:
        m += [chemin("M -10 -30 q -10 -20 0 -40 q 10 -20 0 -40", stroke="#fff", sw=4, opacity=0.7),
              chemin("M 12 -30 q -10 -20 0 -40 q 10 -20 0 -40", stroke="#fff", sw=4, opacity=0.7)]
    m += [chemin("M -40 -20 Q -36 20 0 20 Q 36 20 40 -20 Z", "#ff8787"), ellipse(0, -20, 40, 9, "#94d82d")]
    return place(m, x, y, s)


def pain(x, y, s=1.0):
    m = [ellipse(0, 0, 60, 24, "#e8a860"), chemin("M -30 -12 l 10 18 M -6 -16 l 10 18 M 18 -14 l 10 18", stroke="#c47a2c", sw=4)]
    return place(m, x, y, s)


def longue_table(x, y, w=620):
    return g([rect(x - w / 2 + 20, y - 70, 18, 70, "#8d5524"), rect(x + w / 2 - 38, y - 70, 18, 70, "#8d5524"),
              rect(x - w / 2, y - 90, w, 26, "#c68642", rx=6),
              chemin(f"M {x - w / 2 - 6} {y - 90} L {x + w / 2 + 6} {y - 90} L {x + w / 2 + 10} {y - 50} L {x - w / 2 - 10} {y - 50} Z", "#ffe3e3"),
              ])


def odeur(x, y, s=1.0, couleur="#ffe8cc"):
    m = [chemin(f"M {k * 50} 0 q -30 -40 0 -80 q 30 -40 0 -80 q -30 -40 0 -80", stroke=couleur, sw=6, opacity=0.6) for k in (-1, 0, 1)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    place_village(S)
    S.add(chaudron(430, 780, 1.2, contenu="#ffa94d"))
    S.add(zaza(210, 780, 1.45, expr="rire", bras="tient", objet=cuillere(68, -146, 0.7, rot=20)))
    S.add(minuit(640, 790, 0.9, expr="content", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chaudron(200, 250, 0.6, contenu="#ffa94d", feu=True))
    return S


def p01():
    S = Scene()
    ciel(S, "#63e6be", "#e6fcf5")
    for x, s in [(60, 1.4), (220, 1.1), (590, 1.0), (740, 1.3)]:
        S.add(sapin(x, 620, s, "#2b8a3e", "#2f9e44"))
    sol(S, 610, "#69db7c")
    S.add(maison(420, 620, 0.9, mur="#e5dbff", toit="#5f3dc4", porte="#343a40"))
    S.add(zaza(230, 780, 1.4, expr="content", bras="salut"))
    S.add(minuit(600, 790, 1.1, expr="malin"))
    S.add(champignon(730, 790, 0.8, "#be4bdb"))
    return S


def p02():
    S = Scene()
    place_village(S)
    S.add(personne(180, 760, 1.2, expr="inquiet", bras="bouche", **LUCIE))
    S.add(personne(370, 760, 1.2, expr="malin", bras="pense", **PAUL))
    S.add(personne(600, 770, 1.1, expr="surpris", bras="joues", **JO))
    S.add(bulle(400, 140, 520, 110, "Une sorcière ! Elle doit faire\ndes potions de crapauds !", 30, pointe=(380, 420)))
    return S


def p03():
    S = Scene()
    place_village(S)
    S.add(chaudron(460, 780, 1.3, contenu="#a5d8ff", bulles_=False))
    S.add(zaza(210, 780, 1.4, expr="concentre", bras="montre", regard=(1, 0)))
    S.add(caillou(450, 520, 0.8), mouvement(430, 500, 0.8, rot=-60))
    S.add(texte(560, 330, "Plouf !", 66, "#a5d8ff", contour="#1c2a52"))
    return S


def p04():
    S = Scene()
    place_village(S)
    S.add(chaudron(420, 780, 1.1, contenu="#a5d8ff"))
    S.add(zaza(180, 780, 1.35, expr="malin", bras="hanches", regard=(1, 0)))
    S.add(personne(650, 780, 1.2, expr="surpris", bras="bas", regard=(-1, 0), **TOM))
    S.add(bulle(560, 150, 420, 110, "Une soupe au caillou !\nLa meilleure du monde.", 32, pointe=(260, 420)))
    return S


def p05():
    S = Scene()
    place_village(S)
    S.add(chaudron(430, 780, 1.1, contenu="#a5d8ff"))
    S.add(zaza(200, 780, 1.35, expr="miam", bras="tient", objet=cuillere(68, -146, 0.7, rot=-20)))
    S.add(personne(650, 780, 1.2, expr="rire", bras="course", regard=(-1, 0), flip=True, **TOM))
    S.add(carotte(560, 610, 1.3, rot=-30))
    S.add(texte(400, 150, "Mmm… délicieuse !", 52, "#fff3bf", contour="#1c2a52"))
    return S


def p06():
    S = Scene()
    place_village(S)
    S.add(chaudron(400, 780, 1.1, contenu="#ffc078"))
    S.add(personne(160, 780, 1.3, expr="content", bras="porte", objet=poireau(0, -80, 0.8, rot=-20), **LUCIE))
    S.add(personne(640, 780, 1.3, expr="content", bras="porte",
                   objet=g([patate(-18, -58, 1.0), patate(18, -56, 1.0), patate(0, -70, 0.9),
                            chemin("M -44 -60 L 44 -60 L 34 -20 L -34 -20 Z", "#d9a066")]), **PAUL))
    return S


def p07():
    S = Scene()
    place_village(S)
    S.add(chaudron(400, 780, 1.1, contenu="#ffa94d"))
    S.add(personne(160, 780, 1.15, expr="rire", bras="porte", objet=oignon(0, -80, 1.6), **NINO))
    S.add(personne(640, 780, 1.25, expr="content", bras="large",
                   objet=g([sel(-50, -70, 0.9), persil(56, -72, 1.0)]), **JO))
    return S


def p08():
    S = Scene()
    place_village(S)
    S.add(chaudron(400, 780, 1.25, contenu="#ff922b", fumee=False))
    S.add(odeur(400, 520, 1.3))
    S.add(zaza(200, 780, 1.35, expr="content", bras="tient", objet=cuillere(68, -146, 0.75, rot=40)))
    S.add(personne(620, 780, 1.0, expr="bouche_bee", **LUCIE), personne(720, 790, 0.95, expr="bouche_bee", **PAUL))
    S.add(texte(560, 200, "Ça sent bon !", 52, "#ffe8cc", contour="#1c2a52"))
    return S


def p09():
    S = Scene()
    place_village(S)
    S.add(longue_table(400, 790))
    S.add(pain(250, 695, 0.9), bol_soupe(400, 690, 0.9, fumee_=False), bol_soupe(540, 690, 0.9, fumee_=False))
    S.add(personne(120, 780, 1.1, expr="rire", bras="porte", objet=pain(0, -76, 0.6), **NINO))
    S.add(personne(680, 780, 1.1, expr="rire", bras="porte", objet=bol_soupe(0, -70, 0.7, fumee_=False), **LUCIE))
    S.add(zaza(400, 580, 0.9, expr="rire", bras="ouverts"))
    return S


def p10():
    S = Scene()
    place_village(S)
    gens = [TOM, JO, PAUL, NINO, LUCIE]
    for k, gg in enumerate(gens):
        x = 110 + k * 145
        S.add(personne(x, 700, 0.9, expr="rire" if k % 2 else "miam", bras="porte", **gg))
    S.add(longue_table(400, 790, 760))
    for k in range(5):
        S.add(bol_soupe(110 + k * 145, 694, 0.8))
    return S


def p11():
    S = Scene()
    place_village(S)
    S.add(chaudron(400, 790, 0.9, contenu="#ff922b"))
    S.add(zaza(210, 780, 1.4, expr="malin", bras="pense", regard=(1, 0)))
    S.add(personne(620, 780, 1.2, expr="surpris", bras="porte", objet=bol_soupe(0, -70, 0.7), **TOM))
    S.add(bulle(400, 140, 520, 110, "C'est ce que chacun\na partagé !", 38, pointe=(260, 400)))
    return S


def p12():
    S = Scene()
    place_village(S)
    S.add(chaudron(400, 780, 1.2, contenu="#ff922b"))
    for k, (x, gg) in enumerate([(90, NINO), (200, LUCIE), (610, TOM), (720, JO)]):
        S.add(personne(x, 790, 0.95, expr="rire", bras="haut", **gg))
    S.add(zaza(400, 560, 0.9, expr="rire", bras="haut"))
    S.add(minuit(300, 790, 0.7, expr="rire", bras="haut"))
    S.add(coeur(520, 330, 1.2), coeur(270, 360, 1.0, "#ffd43b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chaudron-seul.svg", vignette),
    ("01-zaza.svg", p01), ("02-une-sorciere.svg", p02), ("03-le-caillou.svg", p03),
    ("04-tom.svg", p04), ("05-carotte.svg", p05), ("06-poireaux.svg", p06),
    ("07-oignon.svg", p07), ("08-ca-sent-bon.svg", p08), ("09-la-table.svg", p09),
    ("10-tous-ensemble.svg", p10), ("11-le-secret.svg", p11), ("12-chaque-hiver.svg", p12),
]
