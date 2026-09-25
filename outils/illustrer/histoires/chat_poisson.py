"""Moka garde le poisson — la responsabilité et la confiance."""
from base import *
from objets import *

ID = "chat-poisson"
MOKA = dict(couleur="#c49a6c", habit="#4dabf7")
VOISINE = dict(couleur="#fff0f6", acc=("chapeau",), couleur_acc="#cc5de8", habit="#f783ac")
MATOU = dict(couleur="#495057")


def salon(S, nuit_=False):
    interieur(S, "#e6fcf5" if not nuit_ else "#aab8c8", "#d9a066", 600, papier="#c3fae8" if not nuit_ else None)


def bocal_bulle(x, y, s=1.0, expr="sourire", bulles=True):
    return bocal(x, y, s, contenu=poisson(0, -80, 0.9, expr=expr, bulles=bulles))


def valise(x, y, s=1.0, couleur="#e8590c"):
    return place([rect(-60, -100, 120, 100, couleur, rx=12), rect(-20, -120, 40, 24, "none", rx=8, stroke="#495057", stroke_width=6),
                  trait(-30, -100, -30, 0, assombrir(couleur, 0.8), 6), trait(30, -100, 30, 0, assombrir(couleur, 0.8), 6)], x, y, s)


def meuble(x, y, w=220):
    return g([rect(x - w / 2, y, w, 20, "#a0693a", rx=4), rect(x - w / 2 + 10, y + 20, w - 20, 600 - y + 140, "#c68642")])


def couverture():
    S = Scene()
    salon(S)
    S.add(meuble(520, 620, 260))
    S.add(bocal_bulle(520, 620, 1.2))
    S.add(perso("chat", 270, 770, 1.7, expr="malin", bras="hanches", regard=(1, 0), **MOKA))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("chat", 130, 265, 0.85, expr="content", **MOKA))
    S.add(bocal_bulle(290, 265, 0.8))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(porte(650, 600, 170, 330, "#b5835a", ouverte=True))
    S.add(valise(720, 760, 1.0))
    S.add(perso("lapin", 560, 770, 1.6, expr="sourire", bras="large", regard=(-1, 0), **VOISINE,
                objet=bocal_bulle(0, -10, 0.55)))
    S.add(perso("chat", 220, 770, 1.5, expr="joie", bras="salut", regard=(1, 0), **MOKA))
    S.add(bulle(360, 150, 560, 110, "Peux-tu t'occuper\nde Bulle, mon poisson ?", 34, pointe=(520, 330)))
    return S


def p02():
    S = Scene()
    fond(S, "#e6fcf5")
    S.add(perso("chat", 400, 930, 3.4, expr="miam", regard=(0, 0.3), **MOKA))
    S.add(bocal(400, 800, 1.6, contenu=poisson(0, -80, 1.0, expr="surpris")))
    S.add(texte(400, 110, "Miam… euh, NON !", 56, "#1c7ed6", contour="#fff"))
    return S


def p03():
    S = Scene()
    salon(S)
    S.add(meuble(400, 600, 300))
    S.add(bocal_bulle(400, 600, 1.2, expr="rire"))
    for k in range(6):
        S.add(cercle(380 + (k * 17) % 50, 330 + k * 22, 4, "#e8590c"))
    S.add(perso("chat", 180, 770, 1.5, expr="concentre", bras="donne", regard=(1, -0.5), **MOKA))
    S.add(texte(620, 200, "Juste une pincée !", 40, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    salon(S)
    S.add(meuble(560, 620, 240))
    S.add(bocal_bulle(560, 620, 1.0, expr="bouche_bee"))
    livre_ = g([rect(-60, -46, 120, 80, "#343a40", rx=6), trait(0, -46, 0, 34, "#868e96", 3),
                cercle(-30, -10, 12, "#fff"), cercle(-34, -12, 3, ENCRE), cercle(-26, -12, 3, ENCRE)])
    S.add(perso("chat", 250, 770, 1.6, expr="rire", bras="porte", **MOKA, objet=place(livre_, 0, -64, 0.9), acc=()))
    S.add(texte(250, 230, "À l'abordage !", 50, "#343a40", contour="#fff"))
    return S


def p05():
    S = Scene()
    salon(S)
    S.add(fenetre(470, 90, 280, 250, "#a5d8ff", contenu=rect(0, 0, 800, 800, "#a5d8ff") + perso("chat", 610, 440, 1.2, expr="malin", bras="joues", **MATOU)))
    S.add(meuble(400, 610, 260))
    S.add(bocal_bulle(360, 610, 0.9, expr="inquiet"))
    S.add(perso("chat", 180, 770, 1.6, expr="fache", bras="hanches", regard=(1, -0.5), **MOKA))
    S.add(bulle(250, 150, 300, 90, "Pas touche !", 44, pointe=(210, 380)))
    return S


def p06():
    S = Scene()
    salon(S, nuit_=True)
    dehors = (rect(0, 0, 800, 800, "#ff922b") + rect(0, 330, 800, 400, "#8ce99a")
              + perso("lapin", 560, 430, 0.8, expr="rire", bras="salut") + perso("chien", 680, 430, 0.8, expr="joie", bras="salut")
              + ballon_jeu(620, 300, 22))
    S.add(fenetre(440, 100, 320, 250, "#ff922b", rideaux="#ffd43b", contenu=dehors))
    S.add(meuble(270, 610, 260))
    S.add(bocal_bulle(270, 610, 0.9, expr="content"))
    S.add(perso("chat", 520, 770, 1.5, expr="sourire", bras="bas", regard=(-1, 0), **MOKA))
    S.add(texte(600, 66, "Viens jouer, Moka !", 38, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(porte(680, 600, 170, 330, "#b5835a", ouverte=True))
    S.add(meuble(400, 620, 220))
    S.add(bocal_bulle(400, 620, 0.9, expr="rire"))
    S.add(perso("lapin", 610, 770, 1.6, expr="rire", bras="ouverts", regard=(-1, 0), **VOISINE))
    S.add(perso("chat", 190, 770, 1.5, expr="fier", bras="bas", regard=(1, 0), **MOKA))
    S.add(bulle(380, 150, 560, 100, "Merci, Moka ! On peut\ntoujours compter sur toi.", 32, pointe=(560, 330)))
    return S


def p08():
    S = Scene()
    salon(S)
    S.add(meuble(640, 620, 200))
    S.add(bocal_bulle(640, 620, 0.8, expr="rire"))
    peluche = poisson(0, -70, 1.3, couleur="#ff922b", expr="content")
    S.add(perso("chat", 330, 770, 1.8, expr="rire", bras="calin", **MOKA, objet=peluche))
    for k in range(3):
        S.add(coeur(160 + k * 40, 330 - k * 50, 0.9, "#ff8787"))
    S.add(texte(330, 170, "Un poisson… en peluche !", 42, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("moka-seul.svg", vignette),
    ("01-la-voisine.svg", p01), ("02-miam-non.svg", p02), ("03-une-pincee.svg", p03),
    ("04-histoire.svg", p04), ("05-pas-touche.svg", p05), ("06-rester.svg", p06),
    ("07-retour.svg", p07), ("08-cadeau.svg", p08),
]
