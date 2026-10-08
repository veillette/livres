"""Mon ami qui ne parle pas — l'amitié avec un enfant non verbal.

Adam raconte l'arrivée de Malo, qui ne parle pas avec sa bouche : il montre
des images (pictogrammes), aime aligner ses trains, se protège du bruit avec
un casque, agite les mains quand il est content, signe « merci » et offre un
dessin. Adam apprend à « écouter avec ses yeux ».
"""
from base import *
from objets import *
from fantastique import personne
from sciences import fleche

ID = "ami-silencieux"
ADAM = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#1098ad", robe=False, jambes="#343a40")
MALO = dict(peau="claire", cheveux="blond", coiffure="boucles", habit="#fab005", robe=False, jambes="#1971c2")
MAITRESSE = dict(peau="doree", cheveux="noir", coiffure="chignon", habit="#9775fa", robe=True)


def adam(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**ADAM, **k})


def malo(x=0, y=0, s=1.0, casque=False, **k):
    if casque:
        k["coiffe"] = casque_bruit()
    return personne(x, y, s, **{**MALO, **k})


def casque_bruit(c="#1971c2"):
    """Casque anti-bruit posé sur la tête (coordonnées de la tête de personne)."""
    return g([chemin("M -54 -150 Q -56 -222 0 -224 Q 56 -222 54 -150", stroke=c, sw=12),
              rect(-70, -176, 30, 52, c, rx=12), rect(40, -176, 30, 52, c, rx=12)])


def carte(x, y, s=1.0, dessin="train", rot=0):
    """Carte-image (pictogramme) ; (x, y) = centre."""
    m = [rect(-50, -60, 100, 120, "#ffffff", rx=10, stroke="#ced4da", stroke_width=4)]
    if dessin == "train":
        m += [rect(-36, -12, 34, 26, "#e03131", rx=4), rect(2, -2, 32, 16, "#1971c2", rx=4),
              cercle(-26, 18, 6, ENCRE), cercle(-10, 18, 6, ENCRE), cercle(12, 18, 6, ENCRE), cercle(26, 18, 6, ENCRE)]
    elif dessin == "jouer":
        m += [cercle(0, 0, 26, "#fa5252"), chemin("M -26 0 Q 0 -14 26 0", stroke="#fff", sw=4)]
    elif dessin == "calme":
        m += [rect(-6, -10, 12, 44, "#8d5524"), cercle(0, -18, 30, "#40c057")]
    return place(m, x, y, s, rot=rot)


def train(x, y, s=1.0, nb=6):
    m = [rect(-10, -16, 40 * nb + 20, 8, "#adb5bd")]
    for k in range(nb):
        c = "#e03131" if k % 2 == 0 else "#1971c2"
        m += [rect(k * 40, -44, 34, 30, c, rx=5), cercle(k * 40 + 8, -10, 6, ENCRE), cercle(k * 40 + 26, -10, 6, ENCRE)]
    m.append(rect(-4, -60, 14, 18, "#e03131"))
    return place(m, x, y, s)


def classe(S):
    interieur(S, "#fff9db", "#e8c39e", y=600, papier="#ffe8a3")
    S.add(rect(150, 90, 500, 240, "#2b8a3e", rx=10, stroke="#a0693a", stroke_width=14))


def cour(S, graine=1):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 580, "#b2f2bb", graine=graine)
    S.add(rect(0, 580, 800, 220, "#ced4da"))


def fourmi(x, y, s=1.0):
    return place([ellipse(-8, 0, 6, 5, ENCRE), ellipse(2, 0, 5, 4, ENCRE), ellipse(12, 0, 7, 6, ENCRE),
                  trait(-4, 2, -10, 10, ENCRE, 1.5), trait(4, 2, 4, 10, ENCRE, 1.5), trait(10, 2, 16, 10, ENCRE, 1.5)], x, y, s)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#e3fafc")
    for k in range(10):
        S.add(coeur(80 + (k * 173) % 640, 300 + (k * 67) % 200, 0.5, "#99e9f2"))
    S.add(adam(270, 780, 1.6, expr="rire", bras="calin"))
    S.add(malo(530, 780, 1.6, expr="content", bras="tient", regard=(-1, 0), objet=carte(68, -146, 0.75, "train")))
    S.cachette(730, 350, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(carte(300, 120, 0.9, "train", rot=8))
    S.add(malo(170, 262, 1.0, expr="content"))
    return S


def p01():
    S = Scene()
    classe(S)
    S.add(texte(400, 230, "Bienvenue Malo", 46, "#ffffff", poids=500))
    S.add(personne(600, 790, 1.45, **MAITRESSE, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(malo(400, 780, 1.2, expr="timide", regard=(0, 1)))
    S.add(adam(160, 780, 1.15, expr="surpris", regard=(1, 0)))
    S.cachette(70, 260, "air")
    return S


def p02():
    S = Scene()
    classe(S)
    S.add(train(470, 760, 0.9, 6))
    S.add(malo(560, 700, 1.15, expr="concentre", regard=(0, 1)))
    S.add(adam(200, 780, 1.25, expr="content", bras="salut", regard=(1, 0)))
    S.add(bulle(250, 400, 240, 80, "Bonjour !", 40, pointe=(230, 500)))
    S.add(texte(620, 420, "…", 70, "#495057"))
    return S


def p03():
    S = Scene()
    classe(S)
    S.add(adam(200, 780, 1.3, expr="bouche_bee", regard=(1, 0)))
    S.add(malo(560, 780, 1.3, expr="sourire", bras="donne", flip=True, regard=(-1, 1),
               objet=carte(84, -110, 0.9, "train")))
    for k, d in enumerate(("jouer", "calme")):
        S.add(carte(640 + k * 30, 470, 0.5, d, rot=-10 + k * 20))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=560, papier="#ffe8a3")
    S.add(tapis(400, 690, 360, 70, "#c5f6fa", "#66d9e8"))
    S.add(train(110, 700, 1.25, 10))
    S.add(adam(170, 640, 1.0, expr="content", regard=(1, 1)))
    S.add(malo(620, 640, 1.0, expr="content", regard=(-1, 1), flip=True))
    S.add(texte(400, 200, "rouge, bleu,", 46, "#e03131", contour="#fff"), texte(400, 260, "rouge, bleu…", 46, "#1971c2", contour="#fff"))
    return S


def p05():
    S = Scene()
    cour(S, 2)
    for k, (x, c) in enumerate(((90, "#fa5252"), (700, "#7048e8"), (620, "#40c057"))):
        S.add(personne(x, 760 - k * 60, 0.7, peau=("claire", "foncee", "doree")[k], cheveux="brun", coiffure="courts", habit=c,
                       robe=False, expr="rire", bras="haut"))
    S.add(texte(160, 300, "AAAH !", 50, "#e8590c", contour="#fff", rot=-8), texte(640, 280, "BOUM !", 50, "#e8590c", contour="#fff", rot=8))
    S.add(malo(400, 790, 1.45, expr="dort", casque=True))
    S.add(texte(400, 420, "ouf…", 40, "#1971c2", contour="#fff"))
    return S


def p06():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 580, 800, 220, "#8ce99a"))
    S.add(arbre(400, 600, 1.8, "#40c057", "#2f9e44"))
    for k in range(6):
        S.add(fourmi(330 + k * 28, 720 + (k % 2) * 6, 1.3))
    S.add(adam(200, 780, 1.2, expr="content", bras="montre", regard=(1, 1)))
    S.add(malo(600, 780, 1.2, expr="sourire", casque=True, regard=(-1, 1)))
    return S


def p07():
    S = Scene()
    cour(S, 3)
    S.add(malo(270, 780, 1.4, expr="rire", bras="ouverts"))
    for sgn in (-1, 1):
        S.add(mouvement(270 + sgn * 150, 610, 1.0, rot=sgn * 20), mouvement(270 + sgn * 150, 640, 0.8, rot=-sgn * 20))
    S.add(adam(570, 720, 1.3, expr="rire", bras="saute"))
    S.add(trait(520, 760, 620, 760, "#adb5bd", 4, opacity=0.6))
    S.add(papillon(150, 300, 1.4), papillon(640, 260, 1.0, "#4dabf7", "#ffd43b", rot=20))
    return S


def p08():
    S = Scene()
    classe(S)
    S.add(texte(400, 230, "merci", 60, "#ffffff", poids=500))
    S.add(malo(230, 780, 1.35, expr="sourire", bras="bouche", regard=(1, 0)))
    S.add(fleche(250, 560, 360, 560, "#fab005", 6, 18))
    S.add(adam(570, 780, 1.35, expr="concentre", bras="bouche", flip=True, regard=(-1, 0)))
    S.add(fleche(550, 560, 440, 560, "#1098ad", 6, 18))
    return S


def dessin_enfant():
    return g([rect(-160, -120, 320, 240, "#ffffff", stroke="#ced4da", stroke_width=4),
              cercle(-60, -40, 22, "none", stroke="#fab005", stroke_width=5), trait(-60, -18, -60, 50, "#fab005", 5),
              trait(-60, 0, 0, 10, "#fab005", 5), trait(-60, 50, -80, 90, "#fab005", 5), trait(-60, 50, -40, 90, "#fab005", 5),
              cercle(60, -40, 22, "none", stroke="#1098ad", stroke_width=5), trait(60, -18, 60, 50, "#1098ad", 5),
              trait(60, 0, 0, 10, "#1098ad", 5), trait(60, 50, 40, 90, "#1098ad", 5), trait(60, 50, 80, 90, "#1098ad", 5),
              coeur(0, -70, 0.7, "#fa5252"), soleil(120, -80, 20, rayons=False)])


def p09():
    S = Scene()
    classe(S)
    S.add(place(dessin_enfant(), 400, 430, 0.9))
    S.add(malo(170, 790, 1.2, expr="content", bras="donne", regard=(1, -1)))
    S.add(adam(640, 790, 1.2, expr="joie", bras="joues", flip=True, regard=(-1, -1)))
    return S


def p10():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    collines(S, 600, "#b2f2bb", graine=6)
    sol(S, 600, "#8ce99a", couleur2="#7bd88a", y2=680)
    S.add(soleil(640, 160, 50, visage=True))
    S.add(adam(300, 770, 1.4, expr="rire", bras="calin"))
    S.add(malo(500, 770, 1.4, expr="content", bras="calin", flip=True))
    S.add(coeur(400, 330, 1.2, "#fa5252"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("malo-seul.svg", vignette),
    ("01-le-nouveau.svg", p01), ("02-bonjour.svg", p02), ("03-les-images.svg", p03),
    ("04-les-trains.svg", p04), ("05-le-casque.svg", p05), ("06-sous-l-arbre.svg", p06),
    ("07-comme-un-papillon.svg", p07), ("08-merci.svg", p08), ("09-le-dessin.svg", p09),
    ("10-mon-ami.svg", p10),
]
