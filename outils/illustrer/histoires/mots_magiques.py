"""Les mots magiques de Biscuit — la politesse et la gentillesse."""
from base import *
from objets import *

ID = "mots-magiques"
BISCUIT = dict(tache=True, habit="#ff922b")
MAMIE = dict(couleur="#d9c2a5", acc=("lunettes",), habit="#e599f7", motif="pois", couleur_motif="#f3d9fa")


def cuisine(S):
    interieur(S, "#fff9db", "#d9a066", 600, papier="#fff3bf")
    S.add(fenetre(560, 110, 170, 150, "#a5d8ff", rideaux="#e599f7", contenu=arbre(60, 220, 0.5)))


def rue(S):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 640, 800, 160, "#ced4da"), rect(0, 630, 800, 16, "#adb5bd"))


def tarte(x, y, s=1.0):
    m = [ellipse(0, 0, 90, 22, "#e8a36c"), ellipse(0, -6, 80, 16, "#f08c00")]
    for k in range(7):
        m.append(cercle(-60 + k * 20, -6 + (k % 2) * 4, 9, "#e03131"))
    return place(m, x, y, s)


def loupe(x, y, s=1.0, rot=-30):
    return place([trait(0, 20, 0, 70, "#8d5524", 10), cercle(0, 0, 26, "#d0ebff", stroke="#495057", stroke_width=6)], x, y, s, rot=rot)


def lettre(x, y, s=1.0, rot=0):
    return place([rect(-36, -24, 72, 48, "#fff", rx=4, stroke="#adb5bd", stroke_width=2),
                  chemin("M -36 -24 L 0 4 L 36 -24", stroke="#adb5bd", sw=2), coeur(0, 10, 0.4, "#fa5252")], x, y, s, rot=rot)


def mot(x, y, contenu, couleur="#f59f00", taille=34, rot=0, r=120):
    return g([etoile5(x, y + 8, r, eclaircir(couleur, 0.55), rot=rot), texte(x, y + taille * 0.35, contenu, taille, "#fff", contour=couleur)])


def couverture():
    S = Scene()
    cuisine(S)
    S.add(perso("chien", 400, 760, 1.8, expr="rire", bras="ouverts", **BISCUIT))
    for x, y, t, c in [(220, 420, "Merci", "#e8590c"), (590, 400, "Bonjour", "#1c7ed6"), (200, 590, "Pardon", "#2f9e44"), (620, 580, "S'il te plaît", "#ae3ec9")]:
        S.add(texte(x, y, t, 40, c, contour="#fff"))
    S.add(paillettes(300, 330), paillettes(520, 320, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("chien", 200, 265, 0.95, expr="content", bras="salut", **BISCUIT))
    return S


def p01():
    S = Scene()
    cuisine(S)
    S.add(perso("chien", 580, 660, 1.7, expr="neutre", bras="hanches", regard=(-1, 0.3), **MAMIE))
    S.add(perso("chien", 230, 760, 1.4, expr="fache", bras="donne", regard=(1, 0), **BISCUIT))
    S.add(table(560, 790, 360, 150, "#c68642", nappe="#ffc9c9"))
    S.add(tarte(560, 630, 1.1))
    S.add(bulle(230, 150, 250, 90, "Donne !", 46, pointe=(230, 330)))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(perso("chien", 580, 660, 1.7, expr="content", bras="bas", regard=(-1, 0.3), **MAMIE))
    S.add(table(560, 790, 360, 150, "#c68642", nappe="#ffc9c9"))
    S.add(tarte(600, 630, 1.0))
    S.add(perso("chien", 230, 760, 1.45, expr="rire", bras="porte", regard=(1, 0), **BISCUIT,
                objet=part_gateau(0, -64, 1.2, "#e8a36c", "#f08c00", "#e03131")))
    S.add(texte(300, 190, "S'il te plaît !", 52, "#fff", contour="#ae3ec9"))
    S.add(paillettes(520, 150))
    return S


def p03():
    S = Scene()
    rue(S)
    S.add(maison(170, 640, 1.0, mur="#fff3bf", toit="#e8590c"))
    S.add(arbre(700, 640, 0.8))
    S.add(perso("chien", 460, 760, 1.5, expr="fier", bras="donne", regard=(1, 0), **BISCUIT,
                objet=loupe(88, -110, 1.1, rot=-20)))
    S.add(texte(470, 190, "À la chasse aux", 42, "#1c7ed6", contour="#fff"))
    S.add(texte(470, 250, "mots magiques !", 42, "#1c7ed6", contour="#fff"))
    return S


def p04():
    S = Scene()
    rue(S)
    S.add(rect(80, 120, 640, 520, "#ffe8cc"), rect(60, 100, 680, 60, "#e8590c", rx=10))
    S.add(texte(400, 145, "BOULANGERIE", 40, "#fff"))
    S.add(rect(120, 200, 560, 200, "#fff4e6", stroke="#d9a066", stroke_width=6))
    for k in range(5):
        S.add(ellipse(170 + k * 110, 380, 44, 18, "#e8a36c"))
        S.add(trait(150 + k * 110, 374, 190 + k * 110, 380, "#c47b3f", 3))
    pain = g([ellipse(96, -94, 40, 16, "#e8a36c"), trait(76, -98, 116, -92, "#c47b3f", 3)])
    S.add(perso("mouton", 560, 600, 1.4, expr="rire", bras="donne", flip=True, acc=("toque", "tablier"), objet=pain))
    S.add(rect(400, 520, 320, 120, "#d9a066"))
    S.add(perso("chien", 250, 760, 1.4, expr="joie", bras="salut", regard=(1, 0), **BISCUIT))
    S.add(bulle(250, 290, 300, 80, "Bonjour !", 42, pointe=(250, 420)))
    return S


def p05():
    S = Scene()
    rue(S)
    S.add(maison(610, 640, 1.1, mur="#d3f9d8", toit="#2f9e44"))
    S.add(perso("castor", 520, 760, 1.4, expr="sourire", bras="donne", flip=True, acc=("chapeau",), couleur_acc="#1c7ed6", habit="#4dabf7"))
    S.add(lettre(380, 620, 1.2, rot=-10))
    S.add(perso("chien", 220, 760, 1.4, expr="rire", bras="donne", regard=(1, 0), **BISCUIT))
    S.add(bulle(240, 200, 280, 90, "Merci !", 46, pointe=(230, 420)))
    S.add(notes(560, 280, 0.9, "#1c7ed6"))
    return S


def p06():
    S = Scene()
    ciel(S, "#b2f2bb", "#ebfbee")
    sol(S, 620, "#8ce99a", couleur2="#69db7c")
    S.add(perso("chat", 560, 760, 1.4, expr="surpris", bras="haut", regard=(-1, 0), couleur="#868e96"))
    S.add(chemin("M 600 730 Q 520 780 380 770", stroke="#868e96", sw=14))
    S.add(perso("chien", 270, 780, 1.4, expr="oups", bras="joues", regard=(1, 0), **BISCUIT))
    S.add(texte(620, 300, "Aïe !", 70, "#e03131", contour="#fff"))
    S.add(bulle(260, 180, 320, 90, "Pardon, Chat !", 38, pointe=(260, 400)))
    return S


def p07():
    S = Scene()
    fond(S, "#fff9db")
    S.add(cercle(400, 420, 300, "#fff3bf"))
    S.add(perso("chien", 400, 700, 1.6, expr="rire", bras="haut", **BISCUIT))
    S.add(mot(170, 190, "Bonjour", "#1c7ed6", 40, rot=-10))
    S.add(mot(630, 180, "Merci", "#e8590c", 44, rot=12))
    S.add(mot(160, 560, "Pardon", "#2f9e44", 42, rot=8))
    S.add(mot(640, 560, "S'il te\nplaît", "#ae3ec9", 36, rot=-8))
    return S


def p08():
    S = Scene()
    interieur(S, "#e5dbff", "#c9a47e", 600, papier="#d0bfff")
    S.add(fenetre(90, 110, 160, 150, "#1c2a52", nuit_=True, rideaux="#ffd43b"))
    petit = perso("chien", 0, 34, 0.62, expr="content", **dict(BISCUIT, habit="#74c0fc", motif="rayures", couleur_motif="#d0ebff"))
    S.add(perso("chien", 420, 740, 2.1, expr="content", bras="calin", objet=petit, **MAMIE))
    S.add(coeur(640, 300, 1.6), coeur(200, 340, 1.0, "#ff8787"))
    S.add(texte(400, 150, "Je t'aime !", 56, "#d6336c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("biscuit-seul.svg", vignette),
    ("01-donne.svg", p01), ("02-s-il-te-plait.svg", p02), ("03-la-chasse.svg", p03),
    ("04-bonjour.svg", p04), ("05-merci.svg", p05), ("06-pardon.svg", p06),
    ("07-collection.svg", p07), ("08-je-t-aime.svg", p08),
]
