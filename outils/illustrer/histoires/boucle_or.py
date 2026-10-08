"""Boucle d'or et les trois ours — on frappe avant d'entrer."""
from contes import *

ID = "boucle-or"
BOUCLE = dict(coiffure="boucles", cheveux="blond", peau="claire", habit="#4dabf7", chaussures="#1864ab")
BOLS = (("papa", "#1c7ed6"), ("maman", "#e64980"), ("bebe", "#fcc419"))


def boucle(x, y, s=1.0, **k):
    return personne(x, y, s, **{**BOUCLE, **k})


def maison_ours(S, porte_ouverte=False):
    foret(S, graine=5)
    S.add(maison(430, 620, 1.2, mur="#ffe8cc", toit="#a0522d", porte="#6d4424"))
    if porte_ouverte:
        S.add(rect(400, 518, 60, 102, "#343a40"))


def cuisine(S):
    interieur(S, "#fff4e6", "#d9a066", 580, papier="#ffe8cc")
    S.add(fenetre(560, 110, 160, 140, dehors="#b2f2bb", rideaux="#fa5252"))
    S.add(etagere(170, 200, 220, objets=g([tasse(110, 200, 0.8), tasse(170, 200, 0.8, "#74c0fc"), tasse(230, 200, 0.8, "#ffd43b")])))


def table_bols(S, y=600, vides=(), fumee=False):
    S.add(table(400, y, 560, 150, nappe="#ffc9c9"))
    for k, (nom, c) in enumerate(BOLS):
        s = (1.4, 1.1, 0.8)[k]
        S.add(bol_porridge(200 + k * 200, y - 168, s, c, vide=nom in vides, fumee=fumee))


def chambre(S):
    interieur(S, "#e7f5ff", "#c9a27e", 560, papier="#d0ebff")
    S.add(fenetre(620, 80, 130, 120, dehors="#b2f2bb", rideaux="#74c0fc"))


def lit_(x, y, s, couleur, couverture, dormeur=""):
    m = [lit(0, 0, 360, couleur, couverture)]
    if dormeur:
        m.append(dormeur)
        m.append(rect(-70, -125, 250, 85, couverture, rx=18))
    return place(m, x, y, s)


def boucle_dort(expr="dort", **k):
    return personne(0, -128, 0.7, rot=-90, expr=expr, **{**BOUCLE, **k})


def trois_lits(S, dormeuse=None):
    S.add(lit_(190, 790, 0.95, "#1c7ed6", "#4dabf7"))
    S.add(lit_(470, 790, 0.75, "#e64980", "#f783ac"))
    S.add(lit_(680, 790, 0.55, "#fab005", "#ffd43b", dormeur=dormeuse or ""))


def couverture():
    S = Scene()
    maison_ours(S)
    S.add(ours_("papa", 150, 780, 1.3, expr="surpris"), ours_("maman", 620, 780, 1.1, expr="surpris"))
    S.add(ours_("bebe", 700, 790, 0.8, expr="surpris", bras="joues"))
    S.add(boucle(400, 790, 1.3, expr="oups", bras="bouche", regard=(-1, 0)))
    S.cachette(730, 330, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bol_porridge(200, 240, 2.0, "#fcc419", fumee=True))
    return S


def p01():
    S = Scene()
    maison_ours(S)
    S.add(ours_("papa", 170, 780, expr="content"), ours_("maman", 610, 780, expr="content", bras="salut"),
          ours_("bebe", 390, 790, expr="rire", bras="haut"))
    S.cachette(730, 210, "air")
    return S


def p02():
    S = Scene()
    cuisine(S)
    table_bols(S, 640, fumee=True)
    S.add(ours_("papa", 150, 790, 1.1, expr="neutre"), ours_("maman", 400, 790, 1.0, expr="sourire", bras="montre"),
          ours_("bebe", 640, 790, 0.8, expr="souffle"))
    S.add(bulle(420, 90, 420, 100, "Allons nous promener\npendant qu'elle refroidit !", 30, pointe=(400, 400)))
    return S


def p03():
    S = Scene()
    maison_ours(S, porte_ouverte=True)
    S.add(boucle(250, 780, 1.4, expr="surpris", bras="montre", regard=(1, -1)))
    S.add(fleur(600, 760, 0.9, "#ff8787"), fleur(660, 780, 0.9, "#cc5de8"), champignon(720, 760, 0.6))
    return S


def p04():
    S = Scene()
    cuisine(S)
    table_bols(S, 600, vides=("bebe",))
    S.add(boucle(560, 800, 1.2, expr="miam", bras="bouche"))
    S.add(texte(200, 300, "Trop chaud !", 34, "#e03131", contour="#fff"), texte(420, 250, "Trop froid !", 34, "#1c7ed6", contour="#fff"))
    S.add(texte(640, 330, "Miam !", 48, "#e67700", contour="#fff"))
    return S


def p05():
    S = Scene()
    interieur(S, "#fff4e6", "#d9a066", 560, papier="#ffe8cc")
    S.add(chaise(130, 740, 1.4, "#1c7ed6"), chaise(360, 720, 1.05, "#e64980"))
    S.add(chaise(600, 740, 0.75, "#fcc419", cassee=True))
    S.add(boucle(620, 780, 1.2, expr="oups", bras="haut", rot=-12))
    S.add(texte(600, 420, "CRAC !", 80, "#c92a2a", contour="#fff", rot=-8))
    return S


def p06():
    S = Scene()
    chambre(S)
    trois_lits(S, dormeuse=boucle_dort())
    S.add(zzz(680, 560, 1.2))
    S.add(texte(400, 200, "Juste comme il faut…", 46, "#1864ab", contour="#fff"))
    return S


def p07():
    S = Scene()
    maison_ours(S, porte_ouverte=True)
    S.add(ours_("papa", 160, 780, expr="surpris", regard=(1, 0)), ours_("maman", 640, 780, expr="inquiet", regard=(-1, 0)),
          ours_("bebe", 300, 790, 0.8, expr="surpris", bras="montre"))
    S.add(texte(400, 150, "La porte est ouverte !", 46, "#6d4424", contour="#fff"))
    return S


def p08():
    S = Scene()
    cuisine(S)
    table_bols(S, 620, vides=("bebe",))
    S.add(ours_("papa", 110, 800, 1.2, expr="fache", bras="hanches"), ours_("maman", 330, 800, 1.0, expr="surpris", bras="joues"))
    S.add(ours_("bebe", 620, 800, 0.95, expr="pleure", larmes=True))
    S.add(bulle(560, 100, 440, 100, "On a mangé\ntoute ma soupe !", 34, pointe=(620, 430)))
    return S


def p09():
    S = Scene()
    interieur(S, "#fff4e6", "#d9a066", 560, papier="#ffe8cc")
    S.add(chaise(120, 700, 1.1, "#1c7ed6"), chaise(290, 690, 0.85, "#e64980"))
    S.add(chaise(480, 720, 0.7, "#fcc419", cassee=True))
    S.add(ours_("papa", 680, 800, 1.2, expr="fache", bras="croises"))
    S.add(ours_("bebe", 360, 800, 0.9, expr="pleure", larmes=True, bras="montre", flip=True))
    S.add(bulle(420, 110, 400, 100, "Et on a cassé\nma petite chaise !", 32, pointe=(380, 520)))
    return S


def p10():
    S = Scene()
    chambre(S)
    S.add(lit_(560, 780, 1.15, "#fab005", "#ffd43b", dormeur=boucle_dort()))
    S.add(zzz(560, 520, 1.0))
    S.add(ours_("papa", 100, 800, 1.1, expr="surpris"), ours_("maman", 250, 800, 0.95, expr="surpris", bras="bouche"))
    S.add(ours_("bebe", 380, 800, 0.8, expr="bouche_bee", bras="montre"))
    S.add(bulle(360, 110, 380, 100, "La voilà !", 44, pointe=(400, 560)))
    return S


def p11():
    S = Scene()
    chambre(S)
    S.add(lit_(560, 740, 0.7, "#fab005", "#ffd43b"))
    S.add(boucle(560, 640, 1.2, expr="surpris", bras="haut"))
    S.add(ours_("papa", 150, 800, 1.1, expr="surpris"), ours_("bebe", 320, 800, 0.8, expr="bouche_bee"))
    S.add(texte(560, 150, "Trois ours !", 64, "#c92a2a", contour="#fff"))
    return S


def p12():
    S = Scene()
    foret(S, graine=9)
    S.add(maison(160, 620, 0.9, mur="#ffe8cc", toit="#a0522d", porte="#6d4424"))
    S.add(boucle(560, 790, 1.3, expr="oups", bras="course"))
    S.add(mouvement(470, 650, 1.4))
    return S


def p13():
    S = Scene()
    maison_ours(S)
    S.add(boucle(250, 790, 1.3, expr="timide", bras="donne", objet=place(g([rect(-26, -60, 52, 60, "#fcc419", rx=10), rect(-30, -70, 60, 14, "#e67700", rx=5), texte(0, -20, "miel", 18, "#e67700")]), 86, -92)))
    S.add(ours_("papa", 520, 790, 1.2, expr="content"), ours_("bebe", 680, 790, 0.85, expr="rire", bras="haut"))
    S.add(texte(400, 170, "Pardon !", 60, "#1c7ed6", contour="#fff"))
    return S


def p14():
    S = Scene()
    maison_ours(S)
    S.add(boucle(250, 790, 1.35, expr="content", bras="coucou"))
    S.add(texte(560, 330, "Toc, toc, toc !", 50, "#6d4424", contour="#fff"))
    S.add(ours_("bebe", 610, 800, 0.8, expr="rire", bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bol-seul.svg", vignette),
    ("01-trois-ours.svg", p01), ("02-trop-chaude.svg", p02), ("03-la-porte.svg", p03), ("04-les-bols.svg", p04),
    ("05-les-chaises.svg", p05), ("06-les-lits.svg", p06), ("07-le-retour.svg", p07), ("08-ma-soupe.svg", p08),
    ("09-ma-chaise.svg", p09), ("10-la-voila.svg", p10), ("11-trois-ours.svg", p11), ("12-la-fuite.svg", p12),
    ("13-pardon.svg", p13), ("14-toc-toc.svg", p14),
]
