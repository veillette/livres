"""Le garage de Sofia — une mécanicienne au travail.

La voiture de Grand-maman Lucille crève sur la route de campagne ; Sofia
arrive avec sa dépanneuse et l'emporte au garage. Sur le pont élévateur,
elle change la roue (cric, clé, écrous), vide la vieille huile noire et met
de l'huile neuve, vérifie phares et clignotants. Chaque outil a sa place au
mur. Malik apporte son vélo à la chaîne déraillée : Sofia la remet. Le soir,
la voiture ronronne comme un chaton.

Plans : 1 large (la crevaison) · 2 large (la dépanneuse) · 3 moyen (le pont
élévateur) · 4 gros plan (la roue) · 5 moyen (l'huile) · 6 gros plan (les
phares) · 7 moyen (le mur d'outils) · 8 moyen (le vélo de Malik) · 9 large
(la voiture prête) · 10 large (au revoir, au soleil couchant).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit, roue, casquette
from objets import velo

ID = "garage-sofia"

SOFIA = dict(stature="adulte", peau="claire", cheveux="noir", coiffure="queue", habit="#228be6", jambes="#228be6",
             chaussures="#343a40", coiffe=casquette("#e03131"), nez="retrousse", yeux="cils",
             tenue=g([rect(10, -96, 20, 14, "none", rx=3, stroke="#1864ab", stroke_width=2.5), ellipse(-20, -70, 8, 5, "#495057", opacity=0.5),
                      ellipse(14, -54, 6, 4, "#495057", opacity=0.5)]))
LUCILLE = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="boucles", habit="#e64980", acc=("lunettes",), carrure="fine")
MALIK = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#ffd43b", robe=False, jambes="#2f9e44", nez="rond")

BLEU_AUTO = "#4dabf7"


def sofia(x, y, s=1.35, **k):
    return pro(x, y, s, **{**SOFIA, **k})


def lucille(x, y, s=1.3, **k):
    return personne(x, y, s, **{**LUCILLE, **k})


def auto(x, y, s=1.0, couleur=BLEU_AUTO, crevee=False, phares=False, clignotant=False, flip=False, propre=False):
    """Petite voiture ronde vue de côté, l'avant à droite ; (x, y) = au sol, sous le milieu."""
    fonce = _assombrir(couleur, 0.75)
    m = [ellipse(0, 6, 250, 14, "#000", opacity=0.14),
         chemin("M -230 -40 L -230 -110 Q -220 -140 -170 -146 L -110 -150 Q -70 -230 20 -230 Q 100 -230 140 -150 L 200 -144 Q 240 -136 240 -100 L 240 -40 Z",
                volume(couleur, 0.3, 0.8)),
         chemin("M -90 -152 Q -60 -212 10 -214 L 10 -152 Z", "#a5d8ff"),
         chemin("M 26 -152 L 26 -214 Q 96 -210 122 -152 Z", "#a5d8ff"),
         trait(18, -214, 18, -50, fonce, 4), trait(-230, -100, 240, -100, fonce, 3, opacity=0.6),
         rect(-6, -128, 22, 6, "#dee2e6", rx=3),
         rect(-244, -76, 30, 20, "#adb5bd", rx=6), rect(226, -76, 30, 20, "#adb5bd", rx=6)]
    if propre:
        m.append(chemin("M -150 -136 Q -40 -150 60 -140", stroke="#fff", sw=8, opacity=0.6))
    m.append(ellipse(232, -118, 12, 10, "#fff3bf" if phares else "#f1f3f5", stroke=fonce, stroke_width=2))
    m.append(rect(-238, -126, 12, 18, "#fa5252", rx=4))
    if clignotant:
        m.append(ellipse(232, -96, 9, 7, "#ff922b"))
        m += [trait(250, -96, 280, -96, "#ff922b", 5), trait(248, -108, 274, -124, "#ff922b", 5), trait(248, -84, 274, -68, "#ff922b", 5)]
    for rx_ in (-140, 140):
        if crevee and rx_ == 140:
            m.append(ellipse(rx_, -30, 48, 34, "#343a40"))
            m.append(ellipse(rx_, -34, 22, 20, "#ced4da"))
        else:
            m.append(roue(rx_, -42, 44))
    if phares:
        m.append(poly([(240, -118), (420, -170), (420, -60)], "#fff3bf", opacity=0.35))
    return place(m, x, y, s, flip=flip) + occuper(x - 250 * s, y - 230 * s, x + 250 * s, y)


def depanneuse(x, y, s=1.0, charge=None):
    """Dépanneuse à plateau, cabine à droite ; charge : dessin posé sur le plateau (repère local, sol du plateau en y = -110)."""
    m = [ellipse(0, 6, 330, 14, "#000", opacity=0.14),
         rect(-320, -130, 440, 40, "#495057", rx=6), rect(-320, -134, 440, 10, "#868e96", rx=4),
         chemin("M 130 -60 L 130 -250 L 250 -250 Q 300 -250 310 -180 L 316 -60 Z", volume("#fa5252", 0.3, 0.8)),
         chemin("M 150 -236 L 240 -236 Q 280 -234 290 -180 L 150 -180 Z", "#a5d8ff"),
         rect(120, -70, 200, 20, "#343a40", rx=6), rect(-330, -94, 450, 30, "#343a40", rx=6),
         roue(-230, -40, 42), roue(-120, -40, 42), roue(240, -40, 42),
         place([rect(-18, -4, 36, 8, "#495057", rx=3), chemin("M -14 -4 Q -14 -24 0 -24 Q 14 -24 14 -4 Z", "#ff922b")], 190, -250)]
    if charge:
        m.append(place(charge, -100, -134))
    return place(m, x, y, s) + occuper(x - 330 * s, y - 260 * s, x + 320 * s, y)


def pont(x, y, s=1.0, hauteur=200):
    """Pont élévateur : deux poteaux et des bras ; la voiture se pose à y - hauteur."""
    m = []
    for dx in (-300, 300):
        m += [rect(dx - 24, -520, 48, 520, cylindre("#fab005", 0.3, 0.75), rx=6), rect(dx - 40, -12, 80, 12, "#495057", rx=4)]
        m.append(rect(dx - (0 if dx < 0 else 120), -hauteur - 10, 120, 20, "#868e96", rx=6))
    return place(m, x, y, s)


def garage(S, y=620):
    interieur(S, "#dee2e6", "#adb5bd", y, plinthe="#495057")
    S.add(rect(0, 60, 800, 30, "#495057"))
    for k in range(4):
        S.add(rect(40 + k * 190, 110, 150, 80, "#d0ebff", stroke="#495057", stroke_width=6))
    for (tx, ty) in ((150, y + 120), (620, y + 150)):
        S.add(ellipse(tx, ty, 40, 10, "#495057", opacity=0.4))


def route(S, y=620, soir=False, graine=1):
    if soir:
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, y - 60, "#b2f2bb", graine=graine)
    S.add(rect(0, y - 60, 800, 70, "#8ce99a"))
    S.add(rect(0, y, 800, 130, "#868e96"))
    for xx in range(20, 800, 140):
        S.add(rect(xx, y + 60, 80, 10, "#f8f9fa", rx=3))
    S.add(rect(0, y + 130, 800, 800 - y - 130, terrain("#8ce99a")))
    S.proposer_cachette(60, y + 160)
    S.proposer_cachette(740, y + 160)


def cle(x, y, s=1.0, rot=0):
    return place([rect(-6, -70, 12, 120, cylindre("#adb5bd", 0.3, 0.7), rx=5), chemin("M -20 -70 Q -20 -100 0 -100 Q 20 -100 20 -70 L 10 -80 L -10 -80 Z", "#adb5bd")],
                 x, y, s, rot=rot)


def cric(x, y, s=1.0):
    return place([rect(-50, -14, 100, 14, "#e03131", rx=4), poly([(-40, -14), (0, -60), (40, -14)], "none", stroke="#e03131", stroke_width=8),
                  rect(-30, -70, 60, 12, "#e03131", rx=4)], x, y, s)


def mur_outils(x, y, s=1.0):
    """Panneau à outils : chaque outil a sa silhouette dessinée."""
    m = [rect(-260, -170, 520, 340, "#ffe8cc", rx=10, stroke="#c68642", stroke_width=8)]
    for k in range(9):
        for j in range(6):
            m.append(cercle(-230 + k * 58, -140 + j * 56, 3, "#c68642"))
    outils = [
        (-180, 0, g([rect(-8, -90, 16, 180, "#adb5bd", rx=6), cercle(0, -96, 22, "none", stroke="#adb5bd", stroke_width=10)])),
        (-80, 0, g([rect(-10, -20, 20, 110, "#fa5252", rx=8), rect(-4, -100, 8, 80, "#adb5bd")])),
        (30, 0, g([rect(-8, -40, 16, 130, "#c68642", rx=4), rect(-40, -90, 80, 40, "#495057", rx=6)])),
        (150, 0, g([trait(-30, 80, 0, -10, "#1c7ed6", 14), trait(30, 80, 0, -10, "#1c7ed6", 14), poly([(-14, -10), (14, -10), (6, -90), (-6, -90)], "#adb5bd")])),
    ]
    for ox, oy, d in outils:
        m.append(place(d, ox, oy))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    garage(S)
    S.add(auto(450, 770, 1.1, couleur=BLEU_AUTO, propre=True))
    S.add(sofia(150, 790, 1.45, expr="rire", bras="tient", regard=(1, 0), objet=cle(*ancre(68, -150, "tient", "adulte"), 0.8, rot=20)))
    S.cachette(70, 370, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cle(150, 160, 1.4, rot=-40), cle(250, 160, 1.4, rot=40))
    return S


def p01():
    """Plan large : sur la route de campagne, la voiture de Grand-maman Lucille a un pneu crevé."""
    S = Scene()
    route(S, 620)
    S.add(arbre(100, 560, 0.9), arbre(720, 550, 0.8))
    S.add(auto(420, 690, 0.95, crevee=True))
    S.add(lucille(150, 790, 1.2, expr="inquiet", bras="joues", regard=(1, -0.2)))
    S.add(texte(560, 190, "Pchhhhh !", 64, "#495057", contour="#fff"))
    return S


def p02():
    """Plan large : Sofia arrive avec sa dépanneuse rouge."""
    S = Scene()
    route(S, 620, graine=2)
    S.add(depanneuse(380, 700, 0.9))
    S.add(sofia(690, 790, 1.25, expr="content", bras="coucou", regard=(-1, 0)))
    S.add(lucille(90, 790, 1.1, expr="content", bras="mains_jointes", regard=(1, 0)))
    S.add(bulle(560, 140, 360, 90, "Pas de panique !", 36, pointe=(660, 470)))
    S.cachette(70, 430, "air")
    return S


def p03():
    """Plan moyen : au garage, la voiture est en l'air sur le pont élévateur ; Sofia regarde dessous avec sa lampe."""
    S = Scene()
    garage(S)
    S.add(pont(400, 790, 1.0, 260))
    S.add(auto(400, 530, 1.0, crevee=True))
    S.add(sofia(400, 790, 1.35, expr="concentre", bras="tient", regard=(0, -1),
                objet=place([rect(-10, -30, 20, 50, "#343a40", rx=4), poly([(-10, -30), (10, -30), (40, -120), (-40, -120)], "#fff3bf", opacity=0.5)],
                            *ancre(68, -146, "tient", "adulte"))))
    S.add(texte(400, 100, "Le pont élévateur", 44, "#1864ab", contour="#fff"))
    return S


def p04():
    """Gros plan : Sofia dévisse les écrous et change la roue crevée."""
    S = Scene()
    garage(S)
    S.add(auto(500, 790, 1.4, crevee=False))
    S.add(cric(560, 795, 1.0))
    S.add(sofia(410, 900, 1.6, expr="concentre", bras="tend", regard=(1, 0.3), objet=cle(*ancre(96, -104, "tend", "adulte"), 0.9, rot=60)))
    S.camera(1.35, 520, 600)
    S.dessus(bulle(260, 120, 400, 90, "On dévisse les écrous…", 32, pointe=S.vers_page(640, 700)))
    S.cachette(585, 259, "air")
    return S


def p05():
    """Plan moyen : la vieille huile noire coule dans un bac ; Sofia verse de l'huile neuve, dorée."""
    S = Scene()
    garage(S)
    S.add(auto(400, 770, 1.0))
    S.add(rect(80, 700, 140, 60, "#495057", rx=8), ellipse(150, 700, 66, 12, "#212529"))
    S.add(texte(150, 660, "vieille huile", 28, "#212529", contour="#fff"))
    S.add(sofia(660, 790, 1.35, expr="content", bras="donne", flip=True, regard=(-1, 0.2),
                objet=place([rect(-26, -50, 52, 70, "#fcc419", rx=8), chemin("M -20 -46 L -60 -80", stroke="#fcc419", sw=10), chemin("M -60 -80 Q -70 -40 -64 -10", stroke="#fab005", sw=6)],
                            *ancre(84, -92, "donne", "adulte"))))
    S.add(texte(600, 260, "huile neuve", 30, "#e67700", contour="#fff"))
    return S


def p06():
    """Gros plan : Sofia vérifie les phares et le clignotant : clic, clac !"""
    S = Scene()
    garage(S)
    S.ambiance("soir")
    S.add(auto(330, 780, 1.4, phares=True, clignotant=True))
    S.add(sofia(700, 800, 1.4, expr="rire", bras="designe", flip=True, regard=(-1, 0)))
    S.lumiere(330 + 232 * 1.4, 780 - 118 * 1.4, 90, "#fff3bf", 0.6)
    S.camera(1.2, 500, 560)
    S.dessus(texte(560, 120, "Clic, clac !", 58, "#e67700", contour="#fff"))
    S.cachette(192, 367, "air")
    return S


def p07():
    """Plan moyen : le mur d'outils ; chaque outil a sa place."""
    S = Scene()
    garage(S)
    S.add(mur_outils(380, 400, 1.1))
    S.add(sofia(640, 790, 1.4, expr="fier", bras="designe", flip=True, regard=(-1, -0.4)))
    S.add(texte(380, 620, "clé · tournevis · marteau · pince", 30, "#1864ab", contour="#fff"))
    return S


def p08():
    """Plan moyen : Malik apporte son vélo, la chaîne a déraillé ; Sofia la remet en place."""
    S = Scene()
    garage(S)
    S.add(velo(400, 770, 1.1, "#40c057"))
    S.add(chemin("M 340 740 Q 380 790 430 760", stroke="#343a40", sw=5))
    S.add(personne(180, 790, 1.3, expr="inquiet", bras="bas", regard=(1, 0.3), **MALIK))
    S.add(sofia(600, 790, 1.4, expr="content", bras="tend", flip=True, regard=(-1, 0.3)))
    S.add(bulle(380, 140, 420, 100, "Ta chaîne a déraillé.\nVoilà, c'est réparé !", 32, pointe=(570, 420)))
    return S


def p09():
    """Plan large : la voiture, réparée et lavée, sort du garage ; Grand-maman Lucille est ravie."""
    S = Scene()
    route(S, 620, graine=4)
    S.add(rect(30, 300, 340, 330, "#adb5bd"), rect(60, 360, 280, 270, "#495057"), rect(30, 290, 340, 40, "#e03131"))
    S.add(texte(200, 318, "GARAGE SOFIA", 26, "#fff"))
    S.add(auto(450, 720, 0.9, propre=True))
    S.add(lucille(725, 790, 1.15, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(sofia(250, 790, 1.2, expr="content", bras="hanches", regard=(1, 0)))
    S.add(texte(470, 190, "Vrrr… elle ronronne !", 44, "#1864ab", contour="#fff"))
    return S


def p10():
    """Plan large : au soleil couchant, la voiture repart, Malik pédale ; Sofia leur fait au revoir."""
    S = Scene()
    route(S, 620, soir=True, graine=5)
    S.add(soleil(120, 470, 50))
    S.add(auto(550, 690, 0.75))
    S.add(velo(330, 740, 0.8, "#40c057"))
    S.add(personne(330, 720, 0.85, expr="rire", bras="guidon", regard=(1, 0), **MALIK))
    S.add(sofia(140, 790, 1.25, expr="rire", bras="coucou", regard=(1, 0)))
    S.add(texte(500, 160, "Bonne route !", 56, "#fff3bf", contour="#e8590c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cles-seules.svg", vignette),
    ("01-la-crevaison.svg", p01), ("02-la-depanneuse.svg", p02), ("03-le-pont.svg", p03),
    ("04-la-roue.svg", p04), ("05-l-huile.svg", p05), ("06-les-phares.svg", p06),
    ("07-les-outils.svg", p07), ("08-le-velo.svg", p08), ("09-elle-ronronne.svg", p09),
    ("10-bonne-route.svg", p10),
]
