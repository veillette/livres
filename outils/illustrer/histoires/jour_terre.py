"""Le Jour de la Terre — le 22 avril avec la classe de Léa.

Le 22 avril, la classe de Monsieur Olivier nettoie le parc : gants, sacs,
pinces ; les déchets triés ; un sac de plastique repêché dans la mare (pour
une tortue, un sac dans l'eau ressemble à une méduse). Le parc redevient
propre ; on plante un érable, maison des oiseaux. À la maison, Léa éteint la
lumière et ferme le robinet en se brossant les dents ; elle va à l'école à
vélo. Le Jour de la Terre, c'est tous les jours.

Plans : 1 moyen (la classe et le globe) · 2 large (le parc plein de
déchets) · 3 moyen (on ramasse) · 4 gros plan (le sac dans la mare) ·
5 large (le parc tout propre) · 6 moyen (on plante l'érable) · 7 gros plan
(une maison pour les oiseaux) · 8 moyen (le robinet) · 9 large (à vélo) ·
10 large (la ronde autour de l'arbre).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit, salopette
from sciences import canard
from objets import velo

ID = "jour-terre"
PAPIER_PEINT = "fleurs"

VERT = "#2f9e44"
LEA = dict(peau="rosee", cheveux="blond", coiffure="queue", habit="#40c057", robe=False, jambes="#1864ab", taches=True, yeux="cils")
ILYES = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#fab005", robe=False, jambes="#495057", nez="rond")
ANAIS = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#cc5de8", robe=True)
OLIVIER = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#343a40",
               barbe="#2b2b3a", acc=("lunettes",), carrure="ronde")
GANT = "#ffd43b"


def lea(x, y, s=1.2, **k):
    return personne(x, y, s, **{**LEA, **k})


def olivier(x, y, s=1.35, **k):
    return pro(x, y, s, **{**OLIVIER, **k})


def globe(x, y, s=1.0):
    """Globe terrestre sur son pied ; (x, y) = pied."""
    m = [ellipse(0, 0, 50, 12, "#495057"), rect(-6, -60, 12, 60, "#868e96"), chemin("M -76 -160 A 86 86 0 0 0 40 -84", stroke="#adb5bd", sw=6),
         cercle(-10, -150, 74, volume("#4dabf7", 0.4, 0.8)),
         chemin("M -60 -180 Q -30 -200 -10 -180 Q 0 -150 -30 -140 Q -60 -130 -60 -180 Z", "#51cf66"),
         chemin("M 10 -130 Q 40 -150 50 -120 Q 40 -90 20 -100 Q 0 -110 10 -130 Z", "#51cf66"),
         chemin("M -40 -110 Q -20 -100 -30 -86", stroke="#51cf66", sw=10)]
    return place(m, x, y, s)


def dechet(nom, x, y, s=1.0, rot=0):
    if nom == "bouteille":
        m = [rect(-12, -50, 24, 50, "#a5d8ff", rx=8, opacity=0.85, stroke="#74c0fc", stroke_width=2), rect(-6, -62, 12, 14, "#1c7ed6", rx=3)]
    elif nom == "canette":
        m = [rect(-12, -36, 24, 36, cylindre("#e03131", 0.3, 0.75), rx=4), rect(-12, -36, 24, 6, "#adb5bd", rx=2)]
    elif nom == "papier":
        m = [poly([(-20, -10), (16, -16), (22, 8), (-14, 14)], "#f8f9fa", stroke="#dee2e6", stroke_width=2), trait(-10, -4, 10, -6, "#ced4da", 2)]
    else:   # sac de plastique
        m = [chemin("M -26 0 Q -30 -40 -16 -44 L -10 -56 L -2 -44 L 4 -44 L 12 -56 L 16 -44 Q 30 -40 26 0 Z", "#f1f3f5", opacity=0.85, stroke="#ced4da", sw=2)]
    return place(m, x, y, s, rot=rot)


def pince(x, y, s=1.0, rot=0):
    """Pince à déchets ; (x, y) = poignée (dans la main)."""
    return place([rect(-8, -14, 16, 28, "#e8590c", rx=6), trait(0, 10, 0, 170, "#adb5bd", 5),
                  chemin("M -4 170 L -14 196 M 4 170 L 14 196", stroke="#495057", sw=4)], x, y, s, rot=rot)


def sac_poubelle(x, y, s=1.0, c="#343a40"):
    return place([chemin("M -40 0 Q -50 -70 -20 -90 L 20 -90 Q 50 -70 40 0 Z", volume(c, 0.35, 0.8)), chemin("M -14 -90 L 0 -110 L 14 -90", stroke=c, sw=8)], x, y, s)


def parc(S, y=600, sale=False, graine=1, haut="#74c0fc", bas="#e7f5ff", mare=True):
    paysage(S, y - 50, y, "#8ce99a", "#b2f2bb", haut, bas, graine=graine, nuages=((640, 120, 0.6),))
    S.add(arbre(90, y + 20, 0.9))
    if mare:
        S.add(ellipse(560, y + 90, 200, 50, "#74c0fc"), ellipse(560, y + 84, 180, 40, "#a5d8ff"))
    S.add(rect(240, y - 20, 160, 14, "#a0693a", rx=4), rect(250, y - 6, 10, 30, "#6d4424"), rect(380, y - 6, 10, 30, "#6d4424"))
    if sale:
        r = random.Random(graine)
        for k in range(14):
            nom = ("bouteille", "canette", "papier", "sac")[k % 4]
            S.add(dechet(nom, r.uniform(40, 760), r.uniform(y + 40, 790), r.uniform(0.7, 1.0), rot=r.uniform(-80, 80)))


def classe(S, y=600):
    interieur(S, "#fff9db", "#c68642", y, papier="#ffec99")
    S.add(rect(150, 80, 500, 250, "#2b8a3e", rx=6), rect(150, 80, 500, 250, "none", rx=6, stroke="#8d5524", stroke_width=12))
    S.add(texte(400, 180, "22 avril", 48, "#fff"), texte(400, 250, "Jour de la Terre", 44, "#fff3bf"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    parc(S, 600, graine=2)
    S.add(trait(400, 760, 400, 640, "#6d4424", 10), cercle(400, 600, 60, volume("#69db7c", 0.3, 0.8)), cercle(360, 630, 40, "#51cf66"), cercle(440, 630, 40, "#51cf66"))
    S.add(lea(250, 790, 1.35, expr="rire", bras="haut", regard=(1, -0.3)))
    S.add(personne(560, 790, 1.25, expr="rire", bras="applaudit", regard=(-1, -0.3), **ILYES))
    S.add(globe(680, 790, 0.55))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(globe(200, 262, 1.05))
    return S


def p01():
    """Plan moyen : en classe, Monsieur Olivier montre le globe : c'est le Jour de la Terre."""
    S = Scene()
    classe(S)
    S.add(globe(600, 610, 0.7))
    S.add(olivier(470, 790, 1.4, expr="content", bras="designe", regard=(1, -0.3)))
    S.add(lea(170, 790, 1.15, expr="joie", bras="leve_doigt", regard=(1, -0.3)))
    S.add(personne(300, 795, 1.05, expr="surpris", bras="bas", regard=(1, -0.3), **ANAIS))
    S.add(personne(690, 795, 1.05, expr="content", bras="bas", regard=(-1, -0.3), **ILYES))
    S.cachette(70, 390, "air")
    return S


def p02():
    """Plan large : au parc, des déchets partout ; la classe arrive avec gants et sacs."""
    S = Scene()
    parc(S, 580, sale=True, graine=3)
    S.add(olivier(140, 790, 1.15, expr="inquiet", bras="hanches", regard=(1, 0)))
    S.add(lea(270, 790, 1.0, expr="triste", bras="bas", regard=(1, 0.3)))
    S.add(personne(380, 790, 0.95, expr="fache", bras="croises", regard=(1, 0.3), **ILYES))
    S.add(bulle(560, 150, 300, 90, "Beurk !", 44, pointe=(330, 450)))
    return S


def p03():
    """Plan moyen : avec des gants et une pince, on ramasse et on trie."""
    S = Scene()
    parc(S, 560, sale=False, graine=4, mare=False)
    S.add(sac_poubelle(680, 790, 1.0, "#1c7ed6"), sac_poubelle(560, 790, 0.9, "#343a40"))
    S.add(texte(680, 650, "recyclage", 24, "#1c7ed6", contour="#fff"), texte(560, 670, "déchets", 24, "#343a40", contour="#fff"))
    S.add(lea(220, 790, 1.35, expr="concentre", bras="tient", regard=(1, 0.6), objet=pince(68, -146, 1.0, rot=-20)))
    S.add(dechet("canette", 320, 790, 1.2, rot=80))
    S.add(personne(420, 790, 1.2, expr="content", bras="porte", regard=(1, 0.2), objet=dechet("bouteille", 0, -50, 1.2), **ANAIS))
    return S


def p04():
    """Gros plan : Ilyes repêche un sac de plastique dans la mare ; un canard le regarde."""
    S = Scene()
    parc(S, 520, graine=5, mare=False)
    S.add(ellipse(480, 690, 400, 110, "#74c0fc"), ellipse(480, 680, 370, 90, "#a5d8ff"))
    S.add(canard(600, 690, 0.9, expr="surpris", flip=True))
    S.add(personne(260, 790, 1.5, expr="concentre", bras="tend", regard=(1, 0.5), **ILYES))
    S.add(dechet("sac", 430, 690, 1.4))
    S.camera(1.2, 420, 560)
    S.dessus(bulle(560, 110, 420, 110, "Pour une tortue, ce sac\nressemble à une méduse !", 30, pointe=S.vers_page(430, 640)))
    return S


def p05():
    """Plan large : le parc est tout propre ; les sacs sont pleins."""
    S = Scene()
    parc(S, 580, graine=6)
    S.add(sac_poubelle(100, 790, 0.9, "#1c7ed6"), sac_poubelle(180, 790, 0.9, "#343a40"), sac_poubelle(260, 790, 0.9, "#1c7ed6"))
    S.add(canard(690, 672, 0.6, expr="content"), canard(740, 686, 0.5, expr="content", flip=True))
    S.add(olivier(460, 790, 1.1, expr="rire", bras="haut"))
    S.add(lea(350, 790, 0.95, expr="rire", bras="saute"))
    S.add(personne(600, 790, 0.95, expr="rire", bras="applaudit", **ANAIS))
    S.add(texte(400, 210, "Tout propre !", 60, VERT, contour="#fff"))
    return S


def p06():
    """Plan moyen : Léa et Monsieur Olivier plantent un petit érable et l'arrosent."""
    S = Scene()
    parc(S, 560, graine=7, mare=False)
    S.add(ellipse(400, 760, 120, 26, "#6d4424"))
    S.add(trait(400, 760, 400, 560, "#8d5524", 8))
    for dx, dy in ((-40, 560), (40, 570), (0, 520), (-60, 610), (60, 615)):
        S.add(place(chemin("M 0 0 L -14 -10 L -10 -24 L 0 -16 L 10 -24 L 14 -10 Z", "#40c057"), 400 + dx, dy, 1.6))
    S.add(olivier(220, 790, 1.4, expr="content", bras="tient", regard=(1, 0.3),
                  objet=place([trait(0, 0, 0, 180, "#a0693a", 8), chemin("M -20 180 L 20 180 L 14 230 L -14 230 Z", "#adb5bd")], *ancre(68, -146, "tient", "adulte"))))
    arrosoir = g([rect(-30, -40, 60, 50, "#4dabf7", rx=8), chemin("M 30 -30 L 70 -60", stroke="#4dabf7", sw=8), chemin("M -14 -40 Q 0 -70 14 -40", stroke="#1c7ed6", sw=5)])
    S.add(lea(580, 790, 1.3, expr="joie", bras="donne", flip=True, regard=(-1, 0.4), objet=place(arrosoir, 96, -96, 1.0, flip=True)))
    for k in range(4):
        S.add(goutte(470 - k * 12, 640 + k * 26, 0.6, "#74c0fc"))
    return S


def p07():
    """Gros plan : plus tard, l'arbre aura grandi : une maison pour les oiseaux."""
    S = Scene()
    paysage(S, 560, 620, graine=8)
    S.add(arbre(400, 760, 2.0, "#69db7c", "#51cf66"))
    S.add(oiseau(330, 330, 0.55, "#fa5252", expr="chante"), oiseau(470, 300, 0.5, "#4dabf7", flip=True, expr="content"))
    S.add(ellipse(400, 420, 40, 26, "#a0693a"), cercle(400, 420, 12, "#5c3a1e"))
    S.add(texte(400, 100, "Un arbre, c'est une maison pour les oiseaux…", 30, VERT, contour="#fff"))
    S.add(texte(400, 145, "et il nous donne de l'air pur !", 30, VERT, contour="#fff"))
    return S


def p08():
    """Plan moyen : à la maison, Léa ferme le robinet en se brossant les dents et éteint la lumière."""
    S = Scene()
    interieur(S, "#e7f5ff", "#ced4da", 600, plinthe="#74c0fc")
    S.add(rect(120, 120, 260, 220, "#d0ebff", stroke="#adb5bd", stroke_width=8, rx=10))
    S.add(rect(100, 470, 300, 30, "#f8f9fa", rx=6), rect(150, 500, 200, 70, "#e9ecef", rx=10), chemin("M 250 430 Q 250 400 280 400", stroke="#868e96", sw=10))
    S.add(lea(250, 790, 1.35, expr="concentre", bras="tient", regard=(0.5, 0.2),
              objet=place([rect(-4, -40, 8, 60, "#4dabf7", rx=3), rect(-6, -52, 12, 14, "#fff", rx=3)], 68, -146)))
    S.add(rect(600, 300, 60, 90, "#fff", rx=6, stroke="#adb5bd", stroke_width=3), rect(618, 330, 24, 30, "#ced4da", rx=4))
    S.add(texte(630, 280, "clic !", 34, "#1c7ed6", contour="#fff"))
    S.add(bulle(560, 500, 380, 110, "Je ferme le robinet\nen me brossant les dents !", 28, pointe=(330, 560)))
    return S


def p09():
    """Plan large : le matin, Léa va à l'école à vélo avec Papa."""
    S = Scene()
    paysage(S, 540, 600, graine=9)
    S.add(rect(0, 660, 800, 90, "#868e96"))
    for xx in range(30, 800, 150):
        S.add(rect(xx, 700, 70, 8, "#fff", rx=3))
    S.add(velo(260, 720, 1.0, "#40c057"))
    S.add(lea(260, 705, 1.0, expr="rire", bras="guidon", regard=(1, 0)))
    S.add(velo(520, 720, 1.2, "#1c7ed6"))
    S.add(personne(520, 705, 1.05, stature="adulte", peau="rosee", cheveux="blond", coiffure="courts", habit="#e8590c", robe=False, jambes="#364fc7",
                   expr="content", bras="guidon", regard=(-1, 0)))
    S.add(texte(400, 180, "À vélo, on n'abîme pas l'air !", 40, VERT, contour="#fff"))
    return S


def p10():
    """Plan large : au coucher du soleil, les enfants font la ronde autour du jeune érable."""
    S = Scene()
    paysage(S, 560, 620, "#8ce99a", "#b2f2bb", "#f783ac", "#ffe8cc", graine=10, nuages=())
    S.add(soleil(640, 520, 50))
    S.add(trait(400, 700, 400, 560, "#8d5524", 8))
    for dx, dy in ((-40, 560), (40, 570), (0, 520)):
        S.add(place(chemin("M 0 0 L -14 -10 L -10 -24 L 0 -16 L 10 -24 L 14 -10 Z", "#40c057"), 400 + dx, dy, 1.6))
    ronde = ((180, 700, LEA, 1.0), (300, 760, ANAIS, 1.05), (500, 760, ILYES, 1.05), (620, 700, dict(peau="claire", cheveux="roux", coiffure="couettes", habit="#ff922b"), 1.0))
    for x, y, pk, s in ronde:
        S.add(personne(x, y, s, expr="rire", bras="main", flip=x > 400, regard=(1 if x < 400 else -1, 0), **pk))
    S.add(texte(400, 160, "Le Jour de la Terre,", 46, VERT, contour="#fff"), texte(400, 220, "c'est tous les jours !", 46, VERT, contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("globe-seul.svg", vignette),
    ("01-le-globe.svg", p01), ("02-beurk.svg", p02), ("03-on-ramasse.svg", p03),
    ("04-le-sac-dans-la-mare.svg", p04), ("05-tout-propre.svg", p05), ("06-on-plante.svg", p06),
    ("07-une-maison-pour-les-oiseaux.svg", p07), ("08-le-robinet.svg", p08), ("09-a-velo.svg", p09),
    ("10-la-ronde.svg", p10),
]
