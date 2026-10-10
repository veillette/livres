"""Momotaro, le garçon de la pêche — un conte du Japon, sans bataille.

Une vieille femme lave le linge à la rivière quand une pêche énorme descend
le courant (donburako, donburako). À la maison, la pêche s'ouvre : un bébé !
On l'appelle Momotaro, « le garçon de la pêche ». Il grandit, fort et
gentil. Quand les oni, des ogres à cornes, viennent voler les récoltes,
Momotaro part leur parler, avec les boulettes de millet (kibi dango) que
lui prépare la grand-mère. Il les partage avec un chien, un singe et un
faisan, qui le suivent jusqu'à l'île des oni. Le faisan survole le mur, le
singe ouvre la porte, le chien se tient bien droit : devant leur courage et
leur amitié, les oni demandent pardon et rendent les trésors. Ici, pas de
combat : les ogres promettent de ne plus recommencer.

Plans : 1 large (la rivière) · 2 moyen (la pêche s'ouvre) · 3 large (il
grandit) · 4 large (les oni) · 5 moyen (les kibi dango) · 6 moyen (le chien)
· 7 large (le singe et le faisan) · 8 large (en bateau) · 9 large (la porte)
· 10 moyen (pardon !) · 11 large (le retour).
"""
from contes import *
from base import _assombrir

ID = "momotaro"

MOMOTARO = dict(peau="doree", cheveux="noir", coiffure="chignon", habit="#f8f9fa", robe=False, jambes="#1864ab", ceinture="#e64980")
BEBE = dict(stature="petit", peau="doree", cheveux="noir", coiffure="courts", habit="#ffc9c9", robe=False, jambes="#ffc9c9")
GRAND_MERE = dict(stature="ancien", peau="doree", cheveux="gris", coiffure="chignon", habit="#7048e8", robe=True, ceinture="#ffd43b",
                  nez="rond")
GRAND_PERE = dict(stature="ancien", peau="doree", cheveux="blanc", coiffure="chauve_cote", habit="#868e96", robe=False, jambes="#495057",
                  barbe="#f8f9fa", ceinture="#2b8a3e", carrure="fine")
VILLAGEOIS = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="carre", habit="#2f9e44", robe=True)
PECHE = "#ffa8a8"


def momotaro(x, y, s=1.5, banniere=True, **k):
    m = []
    if banniere:
        m.append(place([trait(0, 0, 0, -380, "#8d5524", 6), rect(4, -370, 70, 140, "#fff", stroke="#e64980", stroke_width=3),
                        peche_dessin(39, -300, 0.35)], x - 70 * s, y, s))
    m.append(personne(x, y, s, **{**MOMOTARO, **k}))
    return "".join(m)


def peche_dessin(x, y, s=1.0, ouverte=False):
    if ouverte:
        m = [chemin("M -90 0 Q -96 -100 -10 -110 L -20 0 Z", volume(PECHE, 0.3, 0.8)), chemin("M 90 0 Q 96 -100 10 -110 L 20 0 Z", volume(PECHE, 0.3, 0.8)),
             ellipse(-6, -10, 30, 10, "#ffe066", opacity=0.6)]
    else:
        m = [chemin("M 0 -110 Q -110 -110 -96 -30 Q -80 30 0 30 Q 80 30 96 -30 Q 110 -110 0 -110 Z", volume(PECHE, 0.3, 0.8)),
             chemin("M 0 -106 Q -14 -40 0 26", stroke="#f783ac", sw=4, opacity=0.6)]
    m += [ellipse(-30, -120, 36, 14, "#51cf66", rot=-20), ellipse(28, -118, 30, 12, "#40c057", rot=20), trait(0, -110, 0, -126, "#8d5524", 5)]
    return place(m, x, y, s)


def oni(x, y, s=1.0, couleur="#fa5252", expr="fache", flip=False, massue=True):
    """Un oni (ogre à cornes), tout rond, avec son pagne à rayures de tigre ; (x, y) = sous ses pieds."""
    c = couleur
    m = [rect(-46, -80, 30, 80, volume(c, 0.3, 0.8), rx=12), rect(16, -80, 30, 80, volume(c, 0.3, 0.8), rx=12),
         ellipse(0, -170, 90, 100, volume(c, 0.3, 0.8)),
         chemin("M -84 -120 L 84 -120 L 70 -70 L -70 -70 Z", "#fab005")]
    for k in range(6):
        m.append(trait(-70 + k * 28, -118, -60 + k * 28, -74, "#212529", 6))
    m += [rect(-120, -230, 40, 110, volume(c, 0.3, 0.8), rx=18), rect(80, -230, 40, 110, volume(c, 0.3, 0.8), rx=18),
          cercle(0, -300, 66, volume(c, 0.3, 0.8)),
          chemin("M -60 -330 Q -50 -380 -10 -366 Q 30 -380 60 -330 Q 30 -350 0 -346 Q -30 -350 -60 -330 Z", "#212529"),
          poly([(-40, -350), (-30, -400), (-16, -352)], "#fff3bf"), poly([(16, -352), (30, -400), (40, -350)], "#fff3bf"),
          cercle(-22, -306, 12, "#fff"), cercle(22, -306, 12, "#fff"), cercle(-20, -304, 6, ENCRE), cercle(24, -304, 6, ENCRE)]
    if expr == "fache":
        m += [trait(-36, -330, -10, -320, "#212529", 6), trait(36, -330, 10, -320, "#212529", 6), chemin("M -24 -262 Q 0 -276 24 -262", stroke=ENCRE, sw=5)]
    elif expr == "triste":
        m += [trait(-36, -320, -10, -330, "#212529", 6), trait(36, -320, 10, -330, "#212529", 6), chemin("M -24 -266 Q 0 -280 24 -266", stroke=ENCRE, sw=5),
              ellipse(-34, -290, 5, 9, "#74c0fc")]
    else:
        m += [chemin("M -24 -272 Q 0 -250 24 -272", stroke=ENCRE, sw=5)]
    m += [poly([(-14, -266), (-8, -252), (-2, -266)], "#fff"), poly([(2, -266), (8, -252), (14, -266)], "#fff")]
    if massue:
        m.append(place([rect(-12, -160, 24, 160, volume("#a0693a", 0.3, 0.8), rx=10)], 112, -110, rot=20))
    return place(m, x, y, s, flip=flip) + occuper(x - 130 * s, y - 400 * s, x + 150 * s, y)


def chien_(x, y, s=1.0, **k):
    """Le chien blanc de Momotaro."""
    return perso("chien", x, y, s, couleur="#f1f3f5", **k)


def faisan(x, y, s=1.0, flip=False, vol=False):
    m = [chemin("M -40 0 Q -120 -10 -170 20 Q -110 6 -40 14 Z", "#8d5524"),
         ellipse(0, 0, 50, 34, volume("#2b8a3e", 0.3, 0.8)), cercle(44, -36, 22, volume("#1864ab", 0.3, 0.8)),
         ellipse(52, -36, 10, 12, "#e03131"), cercle(50, -42, 4, ENCRE), poly([(64, -34), (80, -30), (64, -26)], "#fab005")]
    if vol:
        m += [chemin("M -10 -10 Q -40 -90 30 -100 Q 10 -50 20 -10 Z", "#5c940d")]
    else:
        m += [ellipse(-6, -2, 34, 20, "#5c940d"), trait(-6, 30, -10, 54, "#fab005", 4), trait(10, 30, 12, 54, "#fab005", 4)]
    return place(m, x, y, s, flip=flip)


def dango(x, y, s=1.0):
    return place([trait(-40, 0, 40, 0, "#c68642", 4), cercle(-22, 0, 14, "#fff3bf"), cercle(4, 0, 14, "#ffe066"), cercle(30, 0, 14, "#fff9db")], x, y, s)


def maison_japon(x, y, s=1.0, couleur="#f4e6cc"):
    m = [rect(-120, -120, 240, 120, volume(couleur, 0.2, 0.85)), chemin("M -170 -110 Q 0 -150 170 -110 L 120 -200 L -120 -200 Z", "#495057"),
         rect(-40, -100, 80, 100, "#c68642"), rect(-100, -90, 40, 40, "#fff3bf", stroke="#8d5524", stroke_width=3),
         rect(60, -90, 40, 40, "#fff3bf", stroke="#8d5524", stroke_width=3)]
    return place(m, x, y, s)


def village_japon(S, horizon=480, soir=False):
    ciel(S, "#ffa94d" if soir else "#a5d8ff", "#fff4e6")
    S.add(chemin(f"M 0 {horizon} L 160 {horizon - 200} L 320 {horizon} Z", "#b197fc"), chemin(f"M 200 {horizon} L 400 {horizon - 260} L 600 {horizon} Z", "#9775fa"),
          poly([(360, horizon - 210), (400, horizon - 260), (440, horizon - 210)], "#fff"))
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#a9e34b")))
    for x in (120, 680):
        S.add(maison_japon(x, horizon + 80, 0.8))


def riviere(S, horizon=460):
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(chemin(f"M 0 {horizon} L 200 {horizon - 180} L 380 {horizon} Z", "#b197fc"))
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#a9e34b")))
    S.add(chemin("M 0 560 Q 400 520 800 580 L 800 720 Q 400 680 0 720 Z", volume("#4dabf7", 0.3, 0.8)))
    for k in range(6):
        S.add(chemin(f"M {80 + k * 130} {620 + (k % 2) * 30} q 20 -8 40 0", stroke="#d0ebff", sw=4))


def ile_oni(S):
    ciel(S, "#868e96", "#ced4da")
    S.add(rect(0, 520, 800, 280, volume("#1864ab", 0.3, 0.8)))
    S.add(chemin("M 120 540 Q 200 300 400 260 Q 600 300 700 540 Z", "#495057"), rect(300, 330, 200, 210, "#343a40"))
    S.add(rect(340, 420, 120, 120, "#8d5524"), trait(400, 420, 400, 540, "#5c3d24", 4))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    village_japon(S, 520)
    S.add(peche_dessin(400, 380, 2.4))
    S.add(momotaro(400, 800, 1.65, expr="rire", bras="hanches", regard=(0, 0)))
    S.add(chien_(180, 800, 0.75, expr="rire", bras="salut"), perso("singe", 620, 800, 0.75, expr="rire", bras="haut"))
    S.add(faisan(650, 330, 0.9, flip=True, vol=True))
    S.cachette(760, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(peche_dessin(200, 200, 1.3))
    return S


def p01():
    """Plan large : la vieille femme lave le linge à la rivière ; une pêche énorme descend le courant : « Donburako, donburako ! »"""
    S = Scene()
    riviere(S)
    S.add(personne(160, 800, 1.6, expr="bouche_bee", bras="joues", regard=(1, 0.3), **GRAND_MERE))
    S.add(rect(260, 720, 120, 40, "#74c0fc", rx=8))
    S.add(peche_dessin(560, 620, 1.1))
    S.add(texte(500, 160, "Donburako, donburako !", 46, "#e64980", contour="#fff"))
    return S


def p02():
    """Plan moyen : à la maison, la pêche s'ouvre en deux ; dedans, un bébé ! Le vieux couple n'en revient pas."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(personne(140, 800, 1.6, expr="joie", bras="joues", regard=(1, 0.4), **GRAND_MERE))
    S.add(personne(660, 800, 1.6, expr="bouche_bee", bras="ouverts", flip=True, regard=(-1, 0.4), **GRAND_PERE))
    S.add(peche_dessin(400, 780, 1.6, ouverte=True))
    S.add(personne(400, 740, 0.7, expr="rire", bras="haut", **BEBE))
    S.add(texte(400, 140, "Un bébé dans la pêche !", 48, "#e64980", contour="#fff"))
    S.cachette(70, 220, "air")
    return S


def p03():
    """Plan large : Momotaro a grandi ; fort et gentil, il porte de gros fagots pour aider les gens du village."""
    S = Scene()
    village_japon(S)
    S.add(momotaro(400, 800, 1.5, banniere=False, expr="rire", bras="porte",
                   objet=g([rect(-90, -150, 180, 40, "#a0693a", rx=10), rect(-80, -120, 160, 40, "#c68642", rx=10)])))
    S.add(personne(640, 800, 1.5, expr="joie", bras="applaudit", flip=True, **VILLAGEOIS))
    S.add(texte(400, 130, "Momotaro, le garçon de la pêche", 40, "#e64980", contour="#fff"))
    return S


def p04():
    """Plan large : le soir, les oni, des ogres à cornes, emportent les sacs de riz du village."""
    S = Scene()
    village_japon(S, soir=True)
    S.ambiance("soir")
    S.add(oni(560, 790, 0.9, "#fa5252", "fache", massue=False))
    S.add(rect(470, 520, 70, 90, "#e9d8a6", rx=14), rect(590, 520, 70, 90, "#e9d8a6", rx=14))
    S.add(oni(740, 800, 0.7, "#4dabf7", "fache", flip=True, massue=False))
    S.add(personne(160, 800, 1.4, expr="triste", bras="joues", regard=(1, 0), **VILLAGEOIS))
    S.add(momotaro(300, 800, 1.35, banniere=False, expr="concentre", bras="hanches", regard=(1, 0)))
    S.add(bulle(300, 150, 300, 90, "J'irai leur parler !", 32, pointe=(300, 330)))
    S.cachette(70, 270, "air")
    return S


def p05():
    """Plan moyen : la grand-mère prépare des kibi dango, des boulettes de millet, pour le voyage de Momotaro."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(personne(260, 800, 1.6, expr="content", bras="donne", regard=(1, 0.3),
                   objet=g([ellipse(84, -96, 40, 10, "#fff", stroke="#dee2e6", stroke_width=2), dango(84, -110, 0.6)]), **GRAND_MERE))
    S.add(momotaro(560, 800, 1.5, expr="rire", bras="tend", flip=True, regard=(-1, 0.2)))
    S.add(texte(400, 140, "Des kibi dango pour la route", 44, "#e64980", contour="#fff"))
    return S


def p06():
    """Plan moyen : sur le chemin, un chien demande une boulette ; Momotaro partage, et le chien le suit."""
    S = Scene()
    village_japon(S)
    S.add(momotaro(300, 800, 1.5, expr="content", bras="donne", regard=(1, 0.4)))
    S.add(dango(460, 640, 0.6))
    S.add(chien_(580, 800, 1.0, expr="joie", bras="tend", flip=True, regard=(-1, -0.3)))
    S.add(bulle(560, 160, 400, 110, "Une boulette, s'il te plaît !\nJe viens avec toi !", 28, pointe=(580, 450)))
    return S


def p07():
    """Plan large : plus loin, un singe, puis un faisan, reçoivent chacun une boulette et rejoignent la petite troupe."""
    S = Scene()
    village_japon(S)
    S.add(arbre(660, 640, 1.2, "#69db7c", "#51cf66"))
    S.add(perso("singe", 600, 800, 0.95, expr="rire", bras="haut", flip=True))
    S.add(faisan(560, 330, 1.0, flip=True, vol=True))
    S.add(chien_(140, 800, 0.85, expr="rire", bras="bas"))
    S.add(momotaro(330, 800, 1.45, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(texte(400, 120, "Un chien, un singe, un faisan !", 42, "#e64980", contour="#fff"))
    return S


def p08():
    """Plan large : en bateau, Momotaro et ses trois amis traversent la mer vers l'île des oni."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 520, 800, 280, volume("#1c7ed6", 0.3, 0.8)))
    S.add(chemin("M 560 530 Q 640 400 700 400 Q 760 420 800 530 Z", "#495057"))
    S.add(chemin("M 120 640 L 520 640 L 470 720 L 170 720 Z", "#a0693a"), trait(320, 640, 320, 360, "#8d5524", 8),
          poly([(326, 370), (470, 470), (326, 600)], "#fff"), peche_dessin(380, 520, 0.4))
    S.add(momotaro(250, 660, 0.95, banniere=False, expr="concentre", bras="hanches", regard=(1, 0)))
    S.add(chien_(420, 660, 0.55, expr="content"), perso("singe", 470, 660, 0.5, expr="rire", bras="haut"))
    S.add(faisan(400, 320, 0.7, vol=True))
    for k in range(6):
        S.add(chemin(f"M {60 + k * 140} {760 - (k % 2) * 20} q 20 -10 40 0 q 20 10 40 0", stroke="#d0ebff", sw=4))
    S.cachette(730, 730, "air")
    return S


def p09():
    """Plan large : sur l'île, le faisan survole le mur, le singe ouvre la grande porte ; les oni sont stupéfaits."""
    S = Scene()
    ile_oni(S)
    S.add(faisan(400, 230, 0.8, vol=True, flip=True))
    S.add(perso("singe", 470, 520, 0.6, expr="rire", bras="haut"))
    S.add(oni(640, 800, 0.8, "#fa5252", "surpris", flip=True))
    S.add(momotaro(200, 800, 1.45, expr="concentre", bras="hanches", regard=(1, 0)))
    S.add(chien_(360, 800, 0.85, expr="concentre", bras="bas"))
    S.add(texte(400, 100, "L'île des oni", 52, "#fff", contour="#495057"))
    S.cachette(730, 210, "air")
    return S


def p10():
    """Plan moyen : devant tant de courage et d'amitié, les oni demandent pardon et rendent les trésors : « Pardon ! »"""
    S = Scene()
    ile_oni(S)
    S.add(oni(560, 800, 0.95, "#fa5252", "triste", massue=False))
    S.add(oni(730, 800, 0.75, "#4dabf7", "triste", massue=False, flip=True))
    S.add(rect(380, 700, 120, 90, volume("#a0693a", 0.3, 0.8), rx=8))
    for k in range(5):
        S.add(cercle(400 + k * 20, 698, 10, OR))
    S.add(momotaro(200, 800, 1.45, banniere=False, expr="content", bras="hanches", regard=(1, 0)))
    S.add(bulle(560, 140, 440, 110, "Pardon ! Nous rendons tout,\net nous ne recommencerons plus !", 28, pointe=(560, 330)))
    S.cachette(70, 210, "air")
    return S


def p11():
    """Plan large : retour au village avec la charrette de trésors ; les grands-parents et les villageois font la fête."""
    S = Scene()
    village_japon(S)
    S.add(rect(420, 640, 200, 90, "#a0693a", rx=8), cercle(450, 740, 26, "#5c3d24"), cercle(590, 740, 26, "#5c3d24"))
    for k in range(5):
        S.add(cercle(450 + k * 34, 630, 14, OR), rect(470 + (k % 3) * 40, 600, 30, 36, "#e9d8a6", rx=8))
    S.add(personne(110, 800, 1.45, expr="joie", bras="haut", **GRAND_MERE), personne(230, 800, 1.45, expr="rire", bras="applaudit", **GRAND_PERE))
    S.add(momotaro(370, 800, 1.45, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(chien_(690, 800, 0.7, expr="rire", bras="haut"), perso("singe", 760, 790, 0.6, expr="rire", bras="haut"))
    S.add(faisan(650, 330, 0.7, vol=True, flip=True))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("peche-seule.svg", vignette),
    ("01-la-riviere.svg", p01), ("02-la-peche.svg", p02), ("03-il-grandit.svg", p03),
    ("04-les-oni.svg", p04), ("05-kibi-dango.svg", p05), ("06-le-chien.svg", p06),
    ("07-le-singe-et-le-faisan.svg", p07), ("08-en-bateau.svg", p08), ("09-l-ile.svg", p09),
    ("10-pardon.svg", p10), ("11-le-retour.svg", p11),
]
