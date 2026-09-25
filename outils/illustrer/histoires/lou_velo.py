"""Pas encore ! — Lou apprend à faire du vélo (la ténacité)."""
from base import *
from objets import *

ID = "lou-velo"
LOU = dict(couleur="#f3e6d8", acc=("casque",), couleur_acc="#4dabf7")
FRERE = dict(couleur="#c9a27e", habit="#69db7c")


def parc(S, ciel_=("#74c0fc", "#e7f5ff"), y=600):
    ciel(S, *ciel_)
    collines(S, y, "#b2f2bb", graine=2)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 110)


def cycliste(x, y, s=1.0, couleur_velo="#fa5252", mvt=False, **kw):
    kw.setdefault("regard", (1, 0))
    sp = 0.8 * s
    p = perso("lapin", x - 12 * s, y - 108 * s, sp, bras="guidon", **kw)
    return g([p, velo(x, y, s, couleur_velo, roues_mvt=mvt)])


def couverture():
    S = Scene()
    parc(S)
    S.add(arbre(120, 640, 0.9), arbre(690, 620, 0.8, fruits="#ff6b6b"))
    S.add(cycliste(400, 740, 1.6, expr="rire", mvt=True, **LOU))
    S.add(paillettes(560, 420))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("lapin", 200, 265, 0.9, expr="content", bras="salut", **LOU))
    return S


def p01():
    S = Scene()
    parc(S)
    S.add(maison(140, 600, 0.9, mur="#fff3bf", toit="#4dabf7"))
    S.add(velo(520, 720, 1.6, "#fa5252"))
    S.add(g([poly([(596, 510), (566, 490), (566, 530)], "#ffd43b"), poly([(596, 510), (626, 490), (626, 530)], "#ffd43b"), cercle(596, 510, 9, "#fab005")]))
    S.add(perso("lapin", 260, 760, 1.4, expr="joie", bras="haut", regard=(1, 0), **LOU))
    return S


def p02():
    S = Scene()
    parc(S)
    S.add(velo(560, 740, 1.4, "#fa5252", tombe=True))
    S.add(perso("lapin", 300, 740, 1.4, expr="oups", bras="ouverts", rot=-18, **LOU))
    S.add(texte(560, 250, "Patatras !", 80, "#e03131", contour="#fff", rot=-8))
    for x, y in [(230, 650), (400, 690), (330, 610)]:
        S.add(etoile5(x, y, 12, "#ffd43b"))
    return S


def p03():
    S = Scene()
    parc(S)
    S.add(perso("lapin", 270, 760, 1.45, expr="triste", bras="croises", **LOU))
    S.add(perso("lapin", 560, 760, 1.85, expr="sourire", bras="montre", regard=(-1, 0), **FRERE))
    S.add(bulle(560, 170, 330, 100, "Pas encore !", 46, pointe=(560, 300)))
    return S


def p04():
    S = Scene()
    parc(S)
    S.add(velo(560, 730, 1.5, "#fa5252"))
    S.add(perso("lapin", 290, 750, 1.45, expr="fier", bras="poing", **LOU))
    S.add(pansement(265, 735, 1.4, rot=-10))
    S.add(texte(290, 250, "Je recommence !", 50, "#e03131", contour="#fff"))
    return S


def p05():
    S = Scene()
    fond(S, "#fff9db")
    cadres = [
        ("#74c0fc", "#e7f5ff", "soleil", "lundi"),
        ("#adb5bd", "#e9ecef", "nuage", "mardi"),
        ("#868e96", "#ced4da", "pluie", "mercredi"),
    ]
    for k, (c1, c2, meteo, jour) in enumerate(cadres):
        x0 = 30 + k * 250
        cid = uid("c")
        inner = [rect(x0, 120, 240, 560, c1), rect(x0, 480, 240, 200, "#8ce99a")]
        if meteo == "soleil":
            inner.append(soleil(x0 + 180, 200, 36))
        elif meteo == "nuage":
            inner.append(nuage(x0 + 120, 210, 0.7, "#f8f9fa"))
        else:
            inner.append(nuage(x0 + 120, 190, 0.7, "#dee2e6"))
            for j in range(14):
                xx = x0 + 20 + (j * 37) % 210
                yy = 260 + (j * 53) % 200
                inner.append(trait(xx, yy, xx - 5, yy + 20, "#4dabf7", 3))
        inner.append(cycliste(x0 + 120, 600, 0.95, expr=["concentre", "sourire", "fier"][k], **LOU))
        S.add(el("clipPath", rect(x0, 120, 240, 560, "#000", rx=20), id=cid))
        S.add(g(inner, clip_path=f"url(#{cid})"))
        S.add(rect(x0, 120, 240, 560, "none", rx=20, stroke="#fff", stroke_width=8))
        S.add(texte(x0 + 120, 740, jour, 42, "#e03131"))
    return S


def p06():
    S = Scene()
    parc(S)
    S.add(arbre(700, 600, 0.8))
    S.add(cycliste(520, 730, 1.35, expr="rire", mvt=True, **LOU))
    S.add(perso("lapin", 200, 760, 1.5, expr="bouche_bee", bras="ouverts", regard=(1, 0), **FRERE))
    S.add(texte(320, 210, "Pédale, pédale !", 48, "#e03131", contour="#fff"))
    return S


def p07():
    S = Scene()
    parc(S, ("#4dabf7", "#d0ebff"), 620)
    S.add(nuage(160, 150, 0.8), nuage(620, 110, 0.6))
    for k in range(4):
        S.add(chemin(f"M {80 + k * 30} {380 + k * 60} q 60 -30 120 0 q 30 20 0 40", stroke="#fff", sw=6, opacity=0.8))
    S.add(cycliste(460, 740, 1.75, expr="rire", mvt=True, **LOU))
    S.add(texte(470, 280, "J'y arrive !", 72, "#e03131", contour="#fff", rot=-5))
    return S


def p08():
    S = Scene()
    ciel(S, "#ff922b", "#ffe8cc")
    S.add(soleil(640, 470, 70, "#ffd43b", rayons=False))
    collines(S, 600, "#e599f7", graine=4)
    sol(S, 600, "#b2f2bb", couleur2="#8ce99a", y2=710)
    S.add(velo(130, 740, 1.0, "#fa5252"))
    S.add(perso("lapin", 330, 760, 1.4, expr="sourire", bras="donne", **LOU))
    main_g, main_d = mains(560, 760, 1.2, "porte")
    S.add(corde_sauter(main_g[0], main_g[1], main_d[0], main_d[1], bas=140))
    S.add(perso("herisson", 560, 760, 1.2, expr="inquiet", bras="porte", regard=(-1, 0)))
    S.add(bulle(420, 200, 360, 100, "Pas encore…\nmais ça viendra !", 36, pointe=(360, 430)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lou-seule.svg", vignette),
    ("01-velo-neuf.svg", p01), ("02-patatras.svg", p02), ("03-pas-encore.svg", p03),
    ("04-recommencer.svg", p04), ("05-chaque-jour.svg", p05), ("06-il-lache.svg", p06),
    ("07-j-y-arrive.svg", p07), ("08-a-ton-tour.svg", p08),
]
