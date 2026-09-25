"""Chut ! Bébé dort — la douceur et l'attention aux autres."""
from base import *
from objets import *

ID = "elephant-chut"
BABOU = dict(habit="#ffa94d")
MAMAN = dict(couleur="#ced4da", acc=("noeud",), couleur_acc="#cc5de8", habit="#b197fc")
BEBE = dict(couleur="#dee2e6", acc=("noeud",), couleur_acc="#f783ac")


def chambre(S, nuit_=False):
    interieur(S, "#fff0f6" if not nuit_ else "#c5c9e0", "#d9a066", 600, papier="#ffdeeb" if not nuit_ else None)
    S.add(fenetre(570, 100, 160, 150, "#1c2a52" if nuit_ else "#a5d8ff", nuit_=nuit_, rideaux="#b197fc"))
    S.add(tapis(400, 740, 300, 50, "#e5dbff", "#b197fc"))


def berceau(x, y, s=1.0, bebe_expr="dort", avec_bebe=True):
    m = [rect(-130, -150, 260, 130, "#fff", rx=16, stroke="#e5dbff", stroke_width=6)]
    if avec_bebe:
        m.append(perso("elephant", 0, -10, 0.55, expr=bebe_expr, **BEBE))
    m += [rect(-130, -80, 260, 60, "#fcc2d7", rx=10)]
    for k in range(7):
        m.append(rect(-120 + k * 38, -150, 10, 130, "#f3d9fa"))
    m += [rect(-140, -160, 280, 16, "#e599f7", rx=6), rect(-140, -24, 280, 16, "#e599f7", rx=6),
          chemin("M -140 0 Q 0 40 140 0", stroke="#e599f7", sw=10)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    chambre(S)
    S.add(berceau(560, 740, 1.1, "dort"))
    S.add(perso("elephant", 290, 760, 1.6, expr="timide", bras="bouche", regard=(1, 0), **BABOU))
    S.add(zzz(600, 470, 1.0))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("elephant", 200, 265, 0.9, expr="content", bras="bouche", **BABOU))
    return S


def p01():
    S = Scene()
    chambre(S)
    S.add(berceau(560, 740, 1.2, "dort"))
    S.add(zzz(600, 440, 1.0))
    S.add(perso("elephant", 330, 760, 1.9, expr="sourire", bras="bouche", regard=(1, 0), **MAMAN))
    S.add(perso("elephant", 120, 770, 1.2, expr="content", regard=(1, -0.5), **BABOU))
    S.add(bulle(300, 140, 220, 80, "Chut !", 46, pointe=(330, 290)))
    return S


def p02():
    S = Scene()
    chambre(S)
    S.add(g([trait(400, 0, 400, 90, "#868e96", 4), poly([(360, 90), (440, 90), (460, 130), (340, 130)], "#ffd8a8")]))
    S.add(perso("elephant", 400, 780, 2.6, expr="rire", bras="haut", **BABOU))
    S.add(texte(160, 300, "Grand,", 50, "#9c36b5", contour="#fff"), texte(640, 330, "lourd,", 50, "#9c36b5", contour="#fff"))
    S.add(texte(400, 740, "… et bruyant !", 50, "#9c36b5", contour="#fff"))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(berceau(640, 740, 0.9, "dort"))
    S.add(perso("elephant", 330, 770, 1.8, expr="oups", bras="ouverts", pieds_haut=True, regard=(1, 0), **BABOU))
    S.add(texte(120, 320, "BOUM…", 60, "#e03131", contour="#fff"), texte(260, 250, "boum…", 42, "#e03131", contour="#fff"),
          texte(380, 200, "boum.", 30, "#e03131", contour="#fff"))
    return S


def p04():
    S = Scene()
    chambre(S)
    S.add(berceau(640, 740, 0.9, "dort"))
    S.add(perso("elephant", 330, 770, 1.9, expr="dort", bras="bouche", **BABOU))
    S.add(texte(330, 170, "Aaa… aaaa…", 56, "#1c7ed6", contour="#fff"))
    S.add(texte(560, 330, "Ouf !", 56, "#2b8a3e", contour="#fff"))
    return S


def p05():
    S = Scene()
    chambre(S)
    S.add(berceau(650, 720, 0.8, "dort"))
    S.add(tour_cubes(230, 740, 0.8, 4, graine=2))
    S.add(perso("elephant", 420, 770, 1.6, expr="concentre", bras="porte", **BABOU, objet=cube(0, -74, 0.8, "#69db7c", "E")))
    S.add(texte(300, 200, "Tout doux, tout doux…", 44, "#9c36b5", contour="#fff"))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(perso("elephant", 300, 780, 2.0, expr="malin", bras="pense", regard=(1, 0), **BABOU))
    S.add(perso("souris", 560, 780, 1.4, expr="rire", bras="joues", regard=(-1, 0)))
    S.add(texte(470, 330, "pss… pss…", 44, "#495057", contour="#fff"))
    return S


def p07():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(berceau(560, 740, 1.2, "pleure"))
    S.add(texte(600, 420, "Ouin !", 60, "#e03131", contour="#fff"))
    S.add(perso("elephant", 260, 770, 1.7, expr="chante", bras="bas", regard=(1, 0), **BABOU))
    S.add(notes(400, 360, 1.0, "#9c36b5"), notes(240, 300, 0.7, "#9c36b5"))
    return S


def p08():
    S = Scene()
    chambre(S, nuit_=True)
    bebe = perso("elephant", 0, 36, 0.58, expr="dort", **BEBE)
    S.add(perso("elephant", 300, 760, 1.9, expr="content", bras="calin", objet=bebe, **BABOU))
    S.add(perso("elephant", 620, 770, 1.8, expr="sourire", bras="bouche", regard=(-1, 0), **MAMAN))
    S.add(zzz(320, 330, 1.0), coeur(470, 360, 1.2))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("babou-seul.svg", vignette),
    ("01-chut.svg", p01), ("02-grand-et-lourd.svg", p02), ("03-sur-la-pointe.svg", p03),
    ("04-atchoum.svg", p04), ("05-tout-doux.svg", p05), ("06-secret.svg", p06),
    ("07-berceuse.svg", p07), ("08-blottie.svg", p08),
]
