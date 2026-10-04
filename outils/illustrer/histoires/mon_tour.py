"""C'est mon tour ! — apprendre à attendre son tour."""
from base import *
from objets import *

ID = "mon-tour"


def praline(x, y, s=1.0, **k):
    return perso("cochon", x, y, s, **{**dict(habit="#e64980", acc=("noeud",), couleur_acc="#ffd43b"), **k})


def gribouille(x, y, s=1.0, **k):
    return perso("chien", x, y, s, **{**dict(habit="#4dabf7", tache=True), **k})


def souriceau(x, y, s=0.55, **k):
    return perso("souris", x, y, s, **{**dict(habit="#ffd43b"), **k})


def lapin(x, y, s=0.9, **k):
    return perso("lapin", x, y, s, **{**dict(habit="#69db7c"), **k})


def herisson(x, y, s=0.85, **k):
    return perso("herisson", x, y, s, **{**dict(habit="#ff922b"), **k})


def toboggan(x, y, s=1.0):
    """Toboggan rouge vu de côté : échelle à gauche, pente vers la droite. (x, y) = sol sous la plateforme."""
    m = [trait(-150, 0, -110, -320, "#868e96", 10), trait(-90, 0, -60, -320, "#868e96", 10)]
    m += [trait(-146 + k * 4, -40 - k * 46, -86 + k * 4, -40 - k * 46, "#adb5bd", 8) for k in range(6)]
    m += [rect(-130, -336, 120, 22, "#4dabf7", rx=6), trait(-110, -336, -110, -400, "#4dabf7", 8),
          trait(-30, -336, -30, -400, "#4dabf7", 8), trait(-110, -398, -30, -398, "#4dabf7", 8)]
    m.append(chemin("M -20 -336 Q 60 -320 120 -180 Q 170 -40 270 -30 L 270 0 Q 150 -10 100 -150 Q 50 -290 -20 -306 Z", "#fa5252"))
    m.append(chemin("M -20 -336 Q 60 -320 120 -180 Q 170 -40 270 -30", stroke="#c92a2a", sw=8))
    m.append(trait(-40, 0, -40, -320, "#868e96", 10))
    return place(m, x, y, s)


def parc(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(80, 90, 40))
    S.add(nuage(560, 100, 0.6))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 620, "#8ce99a")
    S.add(arbre(720, 630, 0.9))


def couverture():
    S = Scene()
    parc(S, 2)
    S.add(toboggan(330, 720, 1.25))
    S.add(praline(590, 790, 1.3, expr="rire", bras="haut"))
    S.add(texte(420, 160, "Wiiiii !", 78, "#e64980", contour="#fff", rot=-6))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(praline(200, 264, 1.0, expr="rire", bras="haut"))
    return S


def p01():
    S = Scene()
    parc(S, 1)
    S.add(toboggan(330, 680, 1.1))
    S.add(lapin(120, 720, 0.75, expr="sourire"), herisson(520, 720, 0.7, expr="sourire"), gribouille(640, 730, 0.8, expr="sourire"))
    S.add(praline(300, 790, 1.15, expr="joie", bras="course"), mouvement(180, 690, 1.0))
    return S


def p02():
    S = Scene()
    parc(S, 2)
    S.add(toboggan(470, 680, 1.1))
    S.add(lapin(160, 720, 0.75, expr="surpris"), herisson(250, 730, 0.7, expr="surpris"), gribouille(80, 730, 0.8, expr="surpris"))
    S.add(praline(330, 440, 0.8, expr="malin", bras="haut"))
    S.add(texte(620, 200, "Moi d'abord !", 60, "#e64980", contour="#fff"))
    return S


def p03():
    S = Scene()
    parc(S, 3)
    S.add(toboggan(560, 680, 1.0))
    S.add(lapin(150, 760, 0.85, expr="fache", bras="hanches", rot=-6), herisson(290, 770, 0.8, expr="pleure", larmes=True),
          gribouille(430, 770, 0.9, expr="fache", bras="croises"))
    S.add(praline(620, 790, 0.95, expr="fache", bras="croises", rot=6))
    S.add(texte(170, 300, "Hé !", 64, "#e03131", contour="#fff", rot=-10), texte(400, 220, "Aïe !", 64, "#e03131", contour="#fff"))
    S.add(eclat(300, 520, 1.2, "#e03131"))
    return S


def p04():
    S = Scene()
    parc(S, 4)
    S.add(toboggan(620, 680, 0.9))
    S.add(gribouille(250, 790, 1.35, expr="content", bras="montre", regard=(1, -0.3)))
    S.add(pensee(220, 200, 85, g([cercle(160 + k * 40, 210, 14, c) for k, c in enumerate(["#e64980", "#69db7c", "#ff922b", "#ced4da"])]), depuis=(240, 460)))
    S.add(lapin(500, 780, 0.7, expr="sourire"), praline(600, 790, 0.75, expr="timide"))
    return S


def p05():
    S = Scene()
    parc(S, 5)
    S.add(toboggan(560, 660, 1.0))
    for k, (fn, s) in enumerate([(souriceau, 0.5), (lapin, 0.75), (herisson, 0.7), (gribouille, 0.8)]):
        S.add(fn(420 - k * 85, 730, s, expr="sourire"))
    S.add(praline(90, 790, 0.95, expr="chante", bras="tete"))
    S.add(notes(160, 420, 1.0, "#e64980"), texte(250, 300, "1, 2, 3…", 54, "#e64980", contour="#fff"))
    return S


def p06():
    S = Scene()
    parc(S, 6)
    S.add(toboggan(260, 720, 1.25))
    S.add(praline(530, 650, 1.05, expr="rire", bras="haut", rot=-20))
    S.add(mouvement(410, 520, 1.2, rot=20))
    S.add(texte(560, 230, "Wiiiii !", 82, "#e64980", contour="#fff", rot=-6))
    return S


def p07():
    S = Scene()
    parc(S, 7)
    S.add(toboggan(560, 660, 1.0))
    S.add(souriceau(290, 780, 0.65, expr="timide", bras="joues"))
    S.add(praline(140, 790, 1.15, expr="content", bras="donne", regard=(1, 0.3)))
    S.add(bulle(300, 300, 340, 90, "Vas-y, passe !", 40, pointe=(180, 520)))
    return S


def p08():
    S = Scene()
    parc(S, 8)
    S.add(toboggan(300, 700, 1.2))
    S.add(souriceau(560, 690, 0.6, expr="rire", bras="haut", rot=-20))
    S.add(gribouille(150, 790, 0.7, expr="rire", bras="haut"))
    S.add(praline(220, 330, 0.55, expr="rire", bras="haut"))
    S.add(lapin(670, 790, 0.75, expr="rire", bras="haut"), herisson(760, 790, 0.6, expr="rire"))
    S.add(texte(560, 230, "Encore !", 70, "#e64980", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("praline-seule.svg", vignette),
    ("01-le-toboggan.svg", p01), ("02-moi-d-abord.svg", p02), ("03-ca-bouscule.svg", p03), ("04-la-file.svg", p04),
    ("05-attendre.svg", p05), ("06-wiii.svg", p06), ("07-passe-devant.svg", p07), ("08-chacun-son-tour.svg", p08),
]
