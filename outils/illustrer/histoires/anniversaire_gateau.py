"""Le gâteau d'anniversaire — la journée où tout le monde a l'air d'avoir oublié.

Ce matin, Mina l'oursonne a cinq ans ! Mais Papa lui propose des céréales,
comme un jour ordinaire. Tom le lapin, de la farine sur le nez, est « très
occupé ». Mia la souris cache quelque chose derrière son dos. Jo le
hérisson file avec un grand sac. Mina se croit oubliée… jusqu'au soir,
devant la maison toute noire de Tom : SURPRISE ! Le gâteau un peu de
travers, cinq bougies, un vœu qu'on garde secret.

Plans : 1 moyen (le réveil) · 2 moyen (les céréales) · 3 moyen (la
farine) · 4 gros plan (le ruban) · 5 large (seule sous l'arbre) · 6 large,
soir (la maison noire) · 7 large (SURPRISE !) · 8 moyen (le gâteau de
travers) · 9 gros plan (souffler) · 10 large (les cadeaux) · 11 moyen,
soir (le vœu secret).
"""
from base import *
from base import _assombrir
from objets import gateau, ballon_air, bol, tasse
from fetes import (guirlande_fanions, guirlande_lumineuse, confettis, cadeau, chapeau_fete, serpentin,
                   bougie_flamme)

ID = "anniversaire-gateau"
PAPIER_PEINT = "rayures"

MINA = dict(couleur="#c08552", habit="#f783ac", acc=("noeud",), couleur_acc="#fab005")
PAPA = dict(couleur="#8f5f3a", habit="#1c7ed6", acc=("lunettes",))
TOM = dict(habit="#40c057")
MIA = dict(habit="#cc5de8", acc=("noeud",), couleur_acc="#ffd43b")
JO = dict(habit="#ff922b", motif="rayures", couleur_motif="#ffc078")


def mina(x, y, s=1.3, chapeau=False, **k):
    m = perso("ours", x, y, s, **{**MINA, **k})
    if chapeau:
        m = g([m, place(chapeau_fete("#fab005", "#e64980", y=-208), x, y, s)])
    return m


def papa(x, y, s=1.75, **k):
    return perso("ours", x, y, s, **{**PAPA, **k})


def tom(x, y, s=1.15, chapeau=False, farine=False, **k):
    m = perso("lapin", x, y, s, **{**TOM, **k})
    extra = []
    if chapeau:
        extra.append(place(chapeau_fete("#4dabf7", "#ffd43b", y=-262), x, y, s))
    if farine:
        extra.append(place(g([cercle(0, -134, 12, "#fff", opacity=0.9), cercle(14, -142, 7, "#fff", opacity=0.9),
                              cercle(-12, -146, 6, "#fff", opacity=0.9)]), x, y, s))
    return g([m] + extra) if extra else m


def mia(x, y, s=1.05, chapeau=False, **k):
    m = perso("souris", x, y, s, **{**MIA, **k})
    if chapeau:
        m = g([m, place(chapeau_fete("#69db7c", "#fff", y=-210), x, y, s)])
    return m


def jo(x, y, s=1.0, chapeau=False, **k):
    m = perso("herisson", x, y, s, **{**JO, **k})
    if chapeau:
        m = g([m, place(chapeau_fete("#e64980", "#fff", y=-222), x, y, s)])
    return m


def gateau_travers(x, y, s=1.0, bougies=5, allumees=True):
    """Le gâteau fait maison : un peu penché, plein de fraises, et ses bougies."""
    m = [gateau(0, 0, 1.0, couleur="#f8c291", glacage="#fff0f6", fruits="#fa5252", bougies=0),
         chemin("M -85 -88 Q -40 -110 0 -96 Q 40 -84 85 -100", stroke="#fff0f6", sw=12)]
    for k in range(bougies):
        bx = -52 + k * 104 / max(1, bougies - 1)
        m.append(bougie_flamme(bx, -92 - (k % 2) * 6, 1.0, ("#74c0fc", "#ffd43b", "#69db7c", "#f783ac", "#b197fc")[k % 5],
                               allumee=allumees))
    return place(m, x, y, s, rot=-5)


def maison_mina(S, y=600):
    interieur(S, "#fff9db", "#d9a066", y, papier="#ffe066")


def salle_fete(S, y=600, allumee=True):
    """Le salon de Tom, décoré pour la fête."""
    interieur(S, "#e7f5ff", "#c8a27a", y, papier="#a5d8ff")
    S.add(guirlande_fanions(0, 60, 800, 60, creux=40, nb=16))
    if allumee:
        S.add(guirlande_lumineuse(0, 140, 800, 140, creux=26, nb=14))
    for k, (x, c) in enumerate(((60, "#fa5252"), (130, "#ffd43b"), (680, "#4dabf7"), (750, "#cc5de8"))):
        S.add(ballon_air(x, y - 10, 0.7 + (k % 2) * 0.1, c, fil=240))


def sac(x, y, s=1.0, c="#c68642"):
    return place([chemin("M -60 0 Q -80 -90 -30 -130 L 30 -130 Q 80 -90 60 0 Z", volume(c, 0.3, 0.75)),
                  chemin("M -30 -130 Q 0 -150 30 -130", stroke="#8d5524", sw=8)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salle_fete(S)
    S.add(confettis(20, 200, 780, 520, 50, graine=3))
    S.add(tom(120, 770, 1.05, chapeau=True, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(jo(680, 770, 0.95, chapeau=True, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(mina(400, 640, 1.4, chapeau=True, expr="joie", bras="ouverts"))
    S.add(table(400, 800, 380, 120, "#c68642", nappe="#ffdeeb"))
    S.add(gateau_travers(400, 690, 0.9))
    S.lumiere(400, 590, 140, "#ffd43b", 0.35)
    S.add(mia(250, 790, 0.85, chapeau=True, expr="rire", bras="saute"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(gateau_travers(200, 255, 1.2))
    return S


def p01():
    """Plan moyen : le réveil ; « J'ai cinq ans ! »"""
    S = Scene()
    piece(S, "chambre", 600)
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#f783ac", contenu=soleil(690, 140, 26, rayons=False)))
    S.add(lit(330, 780, 440, "#fff0f6", "#f783ac"))
    S.add(mina(330, 640, 1.3, expr="joie", bras="haut", pas="saute"))
    for k in range(5):
        S.add(texte(130 + k * 50, 230 - (k % 2) * 20, str(k + 1), 44, ("#fa5252", "#fab005", "#40c057", "#1c7ed6", "#cc5de8")[k], contour="#fff"))
    S.add(bulle(560, 380, 300, 100, "J'ai cinq ans !\nCinq !", 34, pointe=(420, 420)))
    S.cachette(760, 700)
    return S


def p02():
    """Plan moyen : Papa lit son journal et propose des céréales."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(papa(560, 690, 1.6, expr="neutre", bras="porte", regard=(-1, 0),
               objet=g([rect(-80, -150, 160, 110, "#f8f9fa", stroke="#dee2e6", stroke_width=3),
                        trait(-60, -130, 60, -130, "#adb5bd", 6), trait(-60, -110, 40, -110, "#adb5bd", 4),
                        trait(-60, -94, 50, -94, "#adb5bd", 4), trait(-60, -78, 30, -78, "#adb5bd", 4)])))
    S.add(table(400, 800, 560, 130, "#c68642", nappe="#e7f5ff"))
    S.add(bol(300, 670, 1.1, "#fab005", "#ffe8a3"))
    S.add(tasse(560, 670, 1.0, "#1c7ed6"))
    S.add(mina(230, 720, 1.25, expr="inquiet", bras="pense", regard=(1, 0)))
    S.add(bulle(560, 150, 380, 100, "Bonjour, Mina.\nTu veux des céréales ?", 30, pointe=(560, 330)))
    S.add(texte(230, 300, "?", 70, "#e64980"))
    return S


def p03():
    """Plan moyen : chez Tom — de la farine sur le nez, la porte qui se ferme vite."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    sol(S, 660, "#8ce99a")
    S.add(rect(380, 120, 420, 560, "#ffe8cc"), planches(380, 120, 420, 560, "#ffe8cc", larg=30))
    S.add(rect(380, 100, 420, 30, "#e8590c"))
    S.add(rect(470, 280, 200, 400, "#4a2c17"), rect(480, 290, 90, 380, "#a0522d"))
    S.add(tom(580, 690, 1.25, farine=True, expr="oups", bras="tient", regard=(-1, 0), flip=True))
    S.add(rect(565, 290, 105, 380, "#a0522d"))
    S.add(mina(250, 780, 1.35, expr="surpris", bras="salut", regard=(1, 0)))
    S.add(bulle(560, 130, 420, 100, "Je ne peux pas jouer,\nje suis… très occupé !", 28, pointe=(560, 400)))
    S.add(texte(650, 460, "clac !", 36, "#495057", rot=10))
    return S


def p04():
    """Gros plan : Mia cache quelque chose dans son dos ; un ruban dépasse."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    collines(S, 560, "#b2f2bb", graine=3)
    sol(S, 640, "#8ce99a")
    S.add(cadeau(500, 640, 0.9, "#4dabf7", "#e64980"))
    S.add(mia(460, 820, 1.9, expr="malin", bras="croises", regard=(-1, 0)))
    S.add(mina(160, 830, 1.6, expr="surpris", bras="designe", regard=(1, 0)))
    S.camera(1.2, 380, 480)
    S.dessus(bulle(560, 90, 380, 90, "Rien, rien du tout !", 34, pointe=S.vers_page(470, 360)))
    S.cachette(105, 442, "air")
    return S


def p05():
    """Plan large : Jo file avec un grand sac ; Mina s'assoit seule sous l'arbre."""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    collines(S, 560, "#b2f2bb", graine=5)
    sol(S, 640, "#8ce99a")
    S.add(arbre(220, 650, 1.4))
    S.add(mina(240, 740, 1.05, expr="triste", bras="croises", regard=(1, 0)))
    S.add(jo(640, 710, 0.85, expr="malin", bras="porte", regard=(1, 0), pas="court", objet=sac(0, -40, 0.8)))
    S.add(mouvement(560, 610, 1.0))
    S.add(pensee(470, 300, 130, texte(470, 292, "Tout le monde", 30, "#495057") + texte(470, 330, "a oublié…", 30, "#495057"), depuis=(270, 470)))
    S.cachette(760, 770)
    return S


def p06():
    """Plan large, soir : la maison de Tom, toute noire."""
    S = Scene()
    ciel(S, "#364fc7", "#f783ac")
    etoiles(S, 14, 4, (0, 0, 800, 200))
    collines(S, 560, "#5c7cfa", graine=6)
    sol(S, 640, "#4c6ef5")
    S.add(maison(470, 650, 1.3, mur="#adb5bd", toit="#495057", fenetre="#343a40", cheminee=True))
    S.add(papa(230, 760, 1.4, expr="malin", bras="main", regard=(1, 0)))
    S.add(mina(360, 770, 1.0, expr="inquiet", bras="main", flip=True, regard=(1, 0)))
    S.add(texte(650, 200, "Chut…", 40, "#fff3bf", rot=8))
    S.cachette(760, 770)
    return S


def p07():
    """Plan large : « SURPRISE ! » la lumière s'allume."""
    S = Scene()
    salle_fete(S)
    S.add(confettis(20, 180, 780, 700, 90, graine=7))
    S.add(serpentin(80, 360, 1.0, "#f783ac", rot=-15), serpentin(560, 330, 0.9, "#ffd43b", rot=15))
    S.add(tom(170, 770, 1.1, chapeau=True, farine=True, expr="rire", bras="haut"))
    S.add(mia(320, 780, 0.95, chapeau=True, expr="rire", bras="saute"))
    S.add(jo(470, 780, 0.95, chapeau=True, expr="rire", bras="haut"))
    S.add(mina(640, 780, 1.25, expr="bouche_bee", bras="joues", regard=(-1, 0)))
    S.add(texte(400, 290, "SURPRISE !", 92, "#e64980", contour="#fff", rot=-5))
    S.cachette(60, 770)
    return S


def p08():
    """Plan moyen : le gâteau un peu de travers ; « On l'a fait nous-mêmes ! »"""
    S = Scene()
    salle_fete(S)
    S.add(tom(560, 690, 1.25, chapeau=True, farine=True, expr="fier", bras="ouverts", regard=(-1, 0.3)))
    S.add(mina(240, 690, 1.25, chapeau=True, expr="bouche_bee", bras="joues", regard=(1, 0.3)))
    S.add(table(400, 800, 560, 130, "#c68642", nappe="#ffdeeb"))
    S.add(gateau_travers(400, 670, 1.15, allumees=False))
    S.add(bulle(560, 260, 380, 90, "On l'a fait nous-mêmes !", 30, pointe=(560, 410)))
    return S


def p09():
    """Gros plan : cinq bougies ; Mina souffle de toutes ses forces."""
    S = Scene()
    salle_fete(S, allumee=False)
    S.ambiance("soir")
    S.add(mina(400, 860, 2.0, chapeau=True, expr="souffle", bras="bas"))
    S.add(gateau_travers(400, 900, 1.5))
    S.lumiere(400, 700, 180, "#ffd43b", 0.6)
    S.add(chemin("M 380 640 q -30 20 -10 50 M 420 640 q 30 20 10 50", stroke="#d0ebff", sw=6, opacity=0.8))
    S.camera(1.15, 400, 500)
    S.dessus(texte(400, 90, "Un, deux, trois, quatre, cinq… Fffff !", 38, "#e64980", contour="#fff"))
    S.cachette(740, 420, "air")
    return S


def p10():
    """Plan large : les cadeaux — le paquet de Mia, et le sac de Jo, plein de ballons."""
    S = Scene()
    salle_fete(S)
    S.add(confettis(20, 180, 780, 520, 40, graine=11))
    for k, (x, c) in enumerate(((520, "#fa5252"), (580, "#ffd43b"), (640, "#69db7c"), (700, "#4dabf7"), (610, "#cc5de8"))):
        S.add(ballon_air(x, 560, 0.75, c, fil=200 + (k % 2) * 40, fil_courbe=(-1) ** k * 20))
    S.add(jo(620, 770, 1.0, chapeau=True, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(sac(700, 790, 0.6))
    S.add(mina(330, 770, 1.3, chapeau=True, expr="rire", bras="porte", regard=(1, 0),
               objet=perso("ours", 0, -20, 0.32, couleur="#e9ecef", habit="#cc5de8", joues=False)))
    S.add(mia(160, 780, 0.95, chapeau=True, expr="content", bras="applaudit", regard=(1, 0)))
    S.cachette(60, 770)
    return S


def p11():
    """Plan moyen, soir : de la crème jusqu'aux oreilles ; le vœu reste secret."""
    S = Scene()
    maison_mina(S)
    S.ambiance("soir")
    S.add(fenetre(560, 100, 170, 150, "#ff922b", rideaux="#f783ac"))
    S.add(lampe(110, 600, 0.95))
    S.add(papa(520, 760, 1.65, expr="content", bras="calin", regard=(-1, 0)))
    S.add(mina(330, 770, 1.35, expr="malin", bras="chut", regard=(1, 0)))
    S.add(place(g([cercle(-40, -200, 10, "#fff0f6"), cercle(46, -196, 9, "#fff0f6"), cercle(10, -128, 8, "#fff0f6")]), 330, 770, 1.35))
    S.add(bulle(560, 160, 340, 90, "Quel est ton vœu ?", 34, pointe=(530, 380)))
    S.add(bulle(220, 330, 300, 100, "Chut ! Sinon, il ne\nse réalise pas !", 28, pointe=(310, 440)))
    S.cachette(760, 700)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("gateau-seul.svg", vignette),
    ("01-cinq-ans.svg", p01), ("02-des-cereales.svg", p02), ("03-tres-occupe.svg", p03),
    ("04-rien-du-tout.svg", p04), ("05-toute-seule.svg", p05), ("06-la-maison-noire.svg", p06),
    ("07-surprise.svg", p07), ("08-le-gateau.svg", p08), ("09-souffler.svg", p09),
    ("10-les-cadeaux.svg", p10), ("11-le-voeu-secret.svg", p11),
]
