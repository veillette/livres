"""Le ballon de Nino — la tristesse, et laisser partir."""
from base import *
from objets import *

ID = "ballon-envole"
NINO = dict(couleur="#f1f3f5", tache=True, habit="#ffd43b")
MAMAN = dict(couleur="#e9ecef", tache=True, acc=("echarpe",), couleur_acc="#20c997")
ROUGE = "#fa5252"


def foire(S):
    ciel(S, "#74c0fc", "#e7f5ff")
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=720)
    for x, c in [(150, "#ff6b6b"), (650, "#4dabf7")]:
        S.add(poly([(x - 110, 520), (x, 380), (x + 110, 520)], c))
        for k in range(4):
            S.add(poly([(x - 110 + k * 55, 520), (x - 110 + k * 55 + 27, 520), (x, 380)], "#fff", opacity=0.5 if k % 2 else 0))
        S.add(rect(x - 100, 520, 200, 110, "#fff4e6"), rect(x - 30, 560, 60, 70, "#343a40", rx=6))
        S.add(poly([(x - 6, 380), (x - 6, 340), (x + 30, 350), (x - 6, 360)], "#ffd43b"))
    S.add(guirlande_simple(0, 800, 150))


def guirlande_simple(x0, x1, y):
    m = [chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y + 70} {x1} {y}", stroke="#495057", sw=3)]
    for k in range(12):
        t = (k + 0.5) / 12
        m.append(cercle(x0 + (x1 - x0) * t, y + 70 * 4 * t * (1 - t) * 0.5 + 6, 9, ["#ff6b6b", "#ffd43b", "#69db7c", "#4dabf7"][k % 4]))
    return g(m)


def reve(S, contenu_fond):
    """Page « peut-être… » : un décor de rêve encadré de nuages."""
    S.add(contenu_fond)
    for x, y, s in [(60, 60, 1.0), (740, 70, 0.9), (60, 760, 1.1), (740, 750, 1.0), (400, 800, 1.2), (400, 10, 0.9)]:
        S.add(nuage(x, y, s, "#ffffff", opacity=0.9))


def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    sol(S, 660, "#8ce99a", couleur2="#69db7c", y2=740)
    S.add(nuage(160, 300, 0.8), nuage(650, 420, 0.6))
    S.add(ballon_air(520, 460, 1.3, ROUGE, fil=120, fil_courbe=-20))
    S.add(perso("chien", 340, 770, 1.7, expr="bouche_bee", bras="salut", regard=(1, -1), **NINO))
    return S


def vignette():
    S = Scene(400, 270)
    mg, md = mains(160, 265, 0.8, "salut")
    S.add(ballon_air(md[0], md[1], 0.6, ROUGE, fil=110))
    S.add(perso("chien", 160, 265, 0.8, expr="content", bras="salut", **NINO))
    return S


def p01():
    S = Scene()
    foire(S)
    mg, md = mains(330, 760, 1.5, "salut")
    S.add(ballon_air(md[0], md[1], 1.1, ROUGE, fil=160))
    S.add(perso("chien", 330, 760, 1.5, expr="rire", bras="salut", **NINO))
    S.add(perso("chien", 580, 760, 1.8, expr="content", bras="bas", regard=(-1, -0.5), **MAMAN))
    return S


def p02():
    S = Scene()
    foire(S)
    S.add(ballon_air(520, 330, 1.0, ROUGE, fil=160, fil_courbe=40))
    for k in range(3):
        S.add(chemin(f"M {80 + k * 20} {300 + k * 50} q 80 -30 160 0", stroke="#fff", sw=6, opacity=0.8))
    S.add(perso("chien", 330, 760, 1.5, expr="surpris", bras="haut", regard=(1, -1), **NINO))
    S.add(texte(610, 520, "Reviens !", 60, "#e03131", contour="#fff"))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=720)
    petit = perso("chien", 0, 40, 0.62, expr="pleure", larmes=True, **NINO)
    S.add(perso("chien", 400, 740, 2.2, expr="sourire", bras="calin", objet=petit, couleur="#e9ecef", tache=True))
    S.add(ballon_air(640, 120, 0.25, ROUGE, fil=80))
    S.add(coeur(180, 300, 1.2, "#ff8787"))
    return S


def p04():
    S = Scene()
    interieur(S, "#dbe4ff", "#c9a47e", 620, papier="#bac8ff")
    S.add(fenetre(200, 110, 400, 330, "#ff922b", rideaux="#748ffc",
                  contenu=rect(0, 0, 800, 800, "#ffa94d") + cercle(420, 300, 60, "#ffd43b") + etoile5(260, 160, 10, "#fff3bf")))
    S.add(rect(170, 440, 460, 26, "#fff", rx=6))
    S.add(perso("chien", 400, 700, 1.7, expr="triste", bras="joues", regard=(0, -1), **NINO))
    S.add(texte(400, 540, "", 10))
    return S


def p05():
    S = Scene()
    fond_ = rect(0, 0, 800, 800, "#d0ebff") + montagnes(None, 700, ("#b197fc", "#9775fa")) + rect(0, 700, 800, 100, "#8ce99a")
    reve(S, fond_)
    S.add(ballon_air(420, 380, 1.2, ROUGE, fil=110))
    S.add(aigle(230, 240, 1.0), aigle(620, 190, 0.8, flip=True))
    return S


def p06():
    S = Scene()
    reve(S, rect(0, 0, 800, 800, "#1c2a52"))
    etoiles(S, 40, 5, (0, 0, 800, 800))
    S.add(lune(460, 300, 140, visage=True))
    S.add(ballon_air(270, 520, 1.0, ROUGE, fil=110))
    S.add(texte(560, 610, "Coucou, la Lune !", 44, "#fff3bf"))
    return S


def p07():
    S = Scene()
    fond_ = (rect(0, 0, 800, 800, "#ffe8cc") + rect(0, 560, 800, 240, "#4dabf7") + rect(0, 620, 800, 180, "#ffe066"))
    reve(S, fond_)
    S.add(soleil(600, 180, 50))
    S.add(g([chemin("M 150 640 Q 140 480 170 380", stroke="#8d5524", sw=16), ellipse(130, 380, 70, 20, "#40c057", rot=-20),
             ellipse(210, 380, 70, 20, "#40c057", rot=20), ellipse(170, 360, 20, 70, "#40c057")]))
    S.add(ballon_air(520, 300, 0.7, ROUGE, fil=100))
    S.add(perso("souris", 420, 720, 1.4, expr="rire", bras="salut", regard=(1, -1), couleur="#d9a57b", habit="#20c997"))
    return S


def p08():
    S = Scene()
    interieur(S, "#dbe4ff", "#c9a47e", 610, papier="#bac8ff")
    dessin = g([rect(-80, -100, 160, 200, "#fff", stroke="#dee2e6", stroke_width=3),
                ellipse(0, -30, 40, 48, ROUGE), chemin("M 0 18 Q 14 50 0 90", stroke="#495057", sw=2)])
    S.add(place(dessin, 560, 240, 1.0, rot=5))
    S.add(cercle(560, 140, 8, "#4dabf7"))
    S.add(rect(80, 470, 380, 60, "#fff", rx=10), rect(60, 520, 420, 40, "#748ffc", rx=6))
    S.add(fenetre(110, 90, 250, 220, "#74c0fc", rideaux="#ffd43b", contenu=nuage(80, 120, 0.4) + ballon_air(190, 170, 0.2, ROUGE, fil=40)))
    S.add(perso("chien", 400, 760, 1.6, expr="content", bras="salut", regard=(-1, -1), **NINO))
    S.add(bulle(620, 500, 300, 80, "Bon voyage !", 36, pointe=(480, 560)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("nino-seul.svg", vignette),
    ("01-la-fete.svg", p01), ("02-il-s-envole.svg", p02), ("03-triste.svg", p03),
    ("04-ou-est-il.svg", p04), ("05-montagnes.svg", p05), ("06-la-lune.svg", p06),
    ("07-tres-loin.svg", p07), ("08-bon-voyage.svg", p08),
]
