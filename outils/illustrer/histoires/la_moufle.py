"""La Moufle — d'après le conte ukrainien.

Les habitants de la moufle passent la tête par-dessus le bord (ils sont
dessinés derrière la moufle) ; le nouveau venu frappe devant l'ouverture. La
moufle gonfle un peu plus à chaque page.
"""
from contes import *

ID = "la-moufle"
ROUGE = "#e03131"
PAPI = dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="rosee", habit="#1c7ed6", robe=False,
            jambes="#495057")
MAMIE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#e64980", acc=("lunettes",))

# (espèce, échelle) dans l'ordre d'arrivée
ANIMAUX = [("souris", 0.45), ("grenouille", 0.5), ("lievre", 0.62), ("renard", 0.68),
           ("loup", 0.75), ("herisson", 0.55), ("ours", 0.95)]


def papi(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PAPI, **k})


def mamie(x, y, s=1.1, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def animal(nom, x, y, s, **k):
    return perso(nom, x, y, s, **k)


def moufle(x, y, s=1.0, gonfle=1.0, craque=False, ouverte=True):
    """Moufle rouge couchée, le poignet à gauche ; (x, y) = milieu du bas."""
    corps = chemin("M -170 0 L -170 -200 Q -60 -230 60 -215 Q 230 -200 230 -100 Q 230 0 100 0 Z", ROUGE)
    pouce = chemin("M -20 -205 Q -30 -330 30 -330 Q 80 -320 70 -212 Z", ROUGE)
    m = [pouce, corps]
    for k in range(6):
        m.append(chemin(f"M {-120 + k * 55} -200 q 12 100 0 190", stroke="#c92a2a", sw=4, opacity=0.6))
    for k in range(5):
        m.append(g([etoile5(-110 + k * 60, -120 + (k % 2) * 40, 12, "#fff", opacity=0.85)]))
    m.append(rect(-220, -215, 70, 220, "#fff", rx=18))
    for k in range(4):
        m.append(trait(-205 + k * 16, -205, -205 + k * 16, -8, "#ffc9c9", 6))
    if ouverte:
        m.append(ellipse(-232, -108, 22, 90, "#5c1a1a"))
    if craque:
        for (cx, cy) in [(-60, -215), (120, -205), (60, -320)]:
            m.append(chemin(f"M {cx - 14} {cy - 6} l 8 10 l 6 -12 l 8 12", stroke="#fff", sw=4))
    return place(m, x, y, s, sy=s * gonfle)


def habitants(n, x=400, y=720, s=1.0, gonfle=1.0, expr="content"):
    """Les n premiers animaux, qui passent la tête au-dessus de la moufle."""
    places = [(-120, -250), (-60, -250), (110, -245), (170, -235), (-150, -255), (205, -205), (25, -370)]
    m = []
    for k in range(n):
        nom, sc = ANIMAUX[k]
        dx, dy = places[k]
        hs = sc * 1.1 * s
        m.append(animal(nom, x + dx * s, y + dy * gonfle * s + 150 * hs, hs, expr=expr, regard=(0, 0)))
    return g(m)


def foret_neige(S, graine=1, soir=False):
    if soir:
        ciel(S, "#5f3dc4", "#ffc078")
    else:
        ciel(S, "#d0ebff", "#f8f9fa")
    for k, x in enumerate([60, 180, 620, 740]):
        S.add(sapin(x, 560 + (k % 2) * 20, 1.1 - (k % 2) * 0.2, neige=True))
    S.add(rect(0, 560, 800, 240, "#ffffff"))
    S.add(chemin("M 0 560 Q 200 530 400 560 Q 600 590 800 555 L 800 600 L 0 600 Z", "#f1f3f5"))
    flocons(S, 26, graine, (0, 0, 800, 520))


def page_arrivee(n, nom, sc, texte_=None, expr_dedans="content", gonfle=None):
    S = Scene()
    foret_neige(S, n)
    gf = gonfle or 1.0 + 0.09 * (n - 1)
    S.add(habitants(n - 1, 470, 730, 1.0, gf, expr_dedans))
    S.add(moufle(470, 730, 1.0, gf, craque=n >= 7))
    S.add(animal(nom, 150, 760, sc * 1.6, expr="sourire", bras="salut", regard=(1, 0)))
    if texte_:
        S.add(texte(200, 250, texte_, 56, "#c92a2a", contour="#fff", rot=-6))
    return S


def couverture():
    S = Scene()
    foret_neige(S, 2)
    S.add(habitants(7, 430, 740, 1.0, 1.55, "rire"))
    S.add(moufle(430, 740, 1.0, 1.55, craque=True))
    S.add(coccinelle(120, 640, 1.6))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(animal("souris", 170, 150, 0.45, expr="rire"))
    S.add(moufle(220, 262, 0.55, 1.0))
    return S


def p01():
    S = Scene()
    foret_neige(S, 1)
    S.add(papi(520, 760, 1.25, expr="sourire", bras="porte", objet=g([trait(-70, -80, 70, -60, "#8d5524", 14), trait(-70, -60, 70, -80, "#a0693a", 14)])))
    S.add(perso("chien", 690, 770, 0.7, expr="joie", tache=True))
    S.add(moufle(200, 720, 0.4, 1.0))
    S.add(g([cercle(320 + k * 40, 700 + (k % 2) * 16, 7, "#dee2e6") for k in range(5)]))
    return S


def p02():
    S = page_arrivee(1, "souris", 0.45, "Toc, toc !")
    return S


def p03():
    return page_arrivee(2, "grenouille", 0.5, "Toc, toc !")


def p04():
    return page_arrivee(3, "lievre", 0.62, "Toc, toc !")


def p05():
    return page_arrivee(4, "renard", 0.68, "Toc, toc !")


def p06():
    return page_arrivee(5, "loup", 0.75, "Toc, toc !")


def p07():
    S = page_arrivee(6, "herisson", 0.55, "Aïe !", expr_dedans="surpris")
    return S


def p08():
    S = Scene()
    foret_neige(S, 8)
    gf = 1.55
    S.add(habitants(6, 470, 730, 1.0, gf, "inquiet"))
    S.add(moufle(470, 730, 1.0, gf, craque=True))
    S.add(animal("ours", 140, 790, 1.2, expr="content", bras="salut", regard=(1, 0)))
    S.add(texte(560, 160, "Crrr…", 64, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    foret_neige(S, 9)
    gf = 1.6
    S.add(habitants(7, 430, 740, 1.0, gf, "surpris"))
    S.add(moufle(430, 740, 1.0, gf, craque=True))
    S.add(coccinelle(130, 620, 2.4, rot=20))
    S.add(texte(170, 520, "Et moi ?", 48, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    foret_neige(S, 10)
    S.add(eclat(400, 520, 4.0, "#ffd43b"))
    r = random.Random(10)
    for (nom, sc), (x, y, rot) in zip(ANIMAUX, [(150, 760, -30), (260, 600, 20), (380, 760, -15), (520, 640, 25), (660, 770, -20), (300, 440, 40), (560, 470, -25)]):
        S.add(place(animal(nom, 0, 0, sc * 1.4, expr="rire", bras="haut"), x, y, rot=rot))
    for k in range(10):
        S.add(place(chemin("M 0 0 q 20 -20 40 0 q 20 20 40 0", stroke=ROUGE, sw=7), r.uniform(80, 700), r.uniform(200, 600), rot=r.uniform(0, 180)))
    S.add(texte(400, 160, "CRAC !", 110, "#c92a2a", contour="#fff"))
    return S


def p11():
    S = Scene()
    foret_neige(S, 11)
    S.add(papi(300, 780, 1.25, expr="surpris", bras="joues"))
    S.add(perso("chien", 470, 780, 0.75, expr="surpris", tache=True))
    for k in range(6):
        S.add(place(chemin("M 0 0 q 20 -20 40 0 q 20 20 40 0", stroke=ROUGE, sw=6), 520 + (k * 47) % 200, 640 + (k * 31) % 100, rot=k * 35))
    for k in range(12):
        S.add(g([cercle(80 + k * 60, 700 + (k % 3) * 30, 8, "#ced4da"), cercle(96 + k * 60, 690 + (k % 3) * 30, 6, "#ced4da")]))
    return S


def p12():
    S = Scene()
    foret_neige(S, 12, soir=True)
    S.add(maison(660, 560, 1.0, lumiere=True))
    S.add(rect(0, 640, 800, 160, "#ffffff"))
    xs = [80, 175, 270, 370, 470, 570, 690]
    for (nom, sc), x in zip(ANIMAUX, xs):
        S.add(animal(nom, x, 760, sc * 1.25, expr="rire"))
    S.add(chemin("M 40 650 Q 200 690 380 650 Q 560 610 760 660", stroke=ROUGE, sw=30))
    S.add(g([trait(60 + k * 40, 640, 60 + k * 40, 668, "#fff", 4, opacity=0.6) for k in range(18)]))
    S.add(coccinelle(380, 620, 1.2))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("moufle-seule.svg", vignette),
    ("01-la-moufle-perdue.svg", p01), ("02-la-souris.svg", p02), ("03-la-grenouille.svg", p03), ("04-le-lievre.svg", p04),
    ("05-le-renard.svg", p05), ("06-le-loup.svg", p06), ("07-le-herisson.svg", p07), ("08-l-ours.svg", p08),
    ("09-la-coccinelle.svg", p09), ("10-crac.svg", p10), ("11-grand-pere.svg", p11), ("12-l-echarpe.svg", p12),
]
