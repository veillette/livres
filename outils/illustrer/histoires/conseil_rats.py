"""Le Conseil tenu par les Rats — proposer, c'est facile ; faire, c'est autre chose."""
from fables import *

ID = "conseil-rats"

GRIS = "#868e96"
COULEURS = ["#ced4da", "#e9d8c4", "#f1f3f5", "#dee2e6", "#d3c4b1", "#c9d1d9"]


def rodilard(x, y, s=1.0, **k):
    return perso("chat", x, y, s, couleur=GRIS, **k)


def souris(x, y, s=1.0, n_=0, **k):
    k.setdefault("couleur", COULEURS[n_ % len(COULEURS)])
    return perso("souris", x, y, s, **k)


def doyenne(x, y, s=1.0, **k):
    return perso("souris", x, y, s, couleur="#adb5bd", acc=("lunettes",), **k)


def grenier(S, nuit_=False):
    fond(S, "#5c3a1e" if nuit_ else "#c9a27e")
    S.add(poly([(0, 0), (400, -40), (800, 0), (800, 560), (0, 560)], "#a0693a" if not nuit_ else "#4a2c17"))
    for k in range(7):
        x = 60 + k * 115
        S.add(rect(x, 0, 26, 560, "#8d5524" if not nuit_ else "#3b2412"))
    S.add(rect(0, 130, 800, 26, "#7c4a1e"))
    S.add(poly([(330, 180), (470, 180), (470, 300), (330, 300)], "#1c2a52" if nuit_ else "#a5d8ff"))
    S.add(trait(400, 180, 400, 300, "#7c4a1e", 8), trait(330, 240, 470, 240, "#7c4a1e", 8))
    S.add(rect(0, 560, 800, 240, "#d9a066" if not nuit_ else "#7c4a1e"))
    for k in range(6):
        S.add(trait(0, 600 + k * 40, 800, 600 + k * 40, "#c68642" if not nuit_ else "#5c3a1e", 3))
    S.add(g([rect(620, 470, 140, 90, "#c68642", rx=6), rect(640, 430, 100, 50, "#d9a066", rx=6)]))


def trou_souris(x, y, s=1.0, dedans=None):
    m = [chemin("M -90 0 Q -90 -120 0 -120 Q 90 -120 90 0 Z", "#212529")]
    if dedans:
        m.append(dedans)
    return place(m, x, y, s)


def couverture():
    S = Scene()
    grenier(S)
    S.add(doyenne(400, 700, 1.25, expr="malin", bras="tient", objet=grelot(74, -110, 1.2)))
    for k, (sx, sy_) in enumerate([(160, 760), (280, 790), (540, 790), (660, 760)]):
        S.add(souris(sx, sy_, 0.7, n_=k, expr="surpris", bras="joues"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(grelot(200, 150, 2.4, ruban_long=40))
    return S


def p01():
    S = Scene()
    interieur(S, "#e5dbff", "#c9a27e", 600, papier="#d0bfff")
    S.add(rodilard(400, 760, 2.0, expr="malin", bras="hanches"))
    S.add(texte(160, 200, "Rodilard", 54, "#5f3dc4", contour="#fff", rot=-8))
    return S


def p02():
    S = Scene()
    fond(S, "#e5dbff")
    S.add(rect(0, 520, 800, 280, "#c9a27e"), rect(0, 500, 800, 30, "#d9a066"))
    S.add(trou_souris(400, 520, 2.4, dedans=g([souris(-40, 0, 0.35, 0, expr="inquiet"), souris(0, 4, 0.35, 1, expr="triste"),
                                               souris(40, 0, 0.35, 2, expr="inquiet")])))
    S.add(texte(400, 180, "On a peur…", 50, "#5f3dc4", contour="#fff"))
    return S


def p03():
    S = Scene()
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 40, graine=14)
    S.add(lune(620, 140, 50))
    S.add(poly([(0, 560), (400, 360), (800, 560), (800, 800), (0, 800)], "#862e2e"))
    for k in range(8):
        S.add(chemin(f"M 0 {600 + k * 30} L 400 {400 + k * 30} L 800 {600 + k * 30}", stroke="#6b2323", sw=3))
    S.add(rect(560, 330, 50, 120, "#5c3a1e"))
    S.add(rodilard(400, 470, 1.0, expr="content", bras="bas", regard=(1, -1)))
    return S


def p04():
    S = Scene()
    grenier(S, nuit_=True)
    for k, (sx, sy_) in enumerate([(120, 740), (230, 770), (340, 750), (460, 770), (570, 745), (680, 770)]):
        S.add(souris(sx, sy_, 0.75, n_=k, expr="content" if k % 2 else "sourire", bras="bas", regard=(0, -1)))
    S.add(texte(400, 380, "Réunion !", 60, "#ffe066", contour="#3b2412"))
    return S


def p05():
    S = Scene()
    grenier(S)
    S.add(cube(400, 700, 2.2, "#c68642", "", 0))
    S.add(doyenne(400, 640, 1.2, expr="neutre", bras="ouverts"))
    for k, sx in enumerate((110, 220, 580, 690)):
        S.add(souris(sx, 780, 0.65, n_=k, expr="sourire", regard=(1 if sx < 400 else -1, -1)))
    S.add(bulle(400, 110, 440, 100, "Mes amies, il faut\ntrouver une solution !", 32, pointe=(400, 330)))
    return S


def p06():
    S = Scene()
    grenier(S)
    S.add(doyenne(250, 760, 1.35, expr="inquiet", bras="pense"))
    S.add(pensee(560, 280, 170, depuis=(340, 430), contenu=g([rodilard(560, 360, 0.55, expr="malin", bras="bas"),
                                                                texte(560, 180, "chut… chut…", 30, "#868e96")])))
    return S


def p07():
    S = Scene()
    grenier(S)
    S.add(doyenne(300, 760, 1.4, expr="fier", bras="tient", objet=grelot(74, -110, 1.2)))
    S.add(pensee(590, 250, 150, depuis=(420, 420), contenu=g([rodilard(590, 350, 0.5, expr="surpris", bras="bas"),
                                                                grelot(590, 360 - 96 * 0.5, 0.35), texte(590, 170, "drelin !", 34, "#f59f00")])))
    return S


def p08():
    S = Scene()
    grenier(S)
    for k, (sx, sy_) in enumerate([(110, 760), (240, 780), (400, 760), (560, 780), (690, 760)]):
        S.add(souris(sx, sy_, 0.85, n_=k, expr="rire", bras="haut"))
    S.add(texte(400, 380, "Hourra !", 72, "#845ef7", contour="#fff"))
    S.add(paillettes(200, 400, 1.0), paillettes(600, 420, 1.0))
    return S


def p09():
    S = Scene()
    grenier(S)
    S.add(doyenne(400, 760, 1.4, expr="malin", bras="tient", objet=grelot(74, -110, 1.2)))
    S.add(souris(150, 780, 0.7, 1, expr="surpris"), souris(650, 780, 0.7, 2, expr="surpris"))
    S.add(bulle(400, 110, 420, 100, "Bien. Qui va\nl'attacher ?", 38, pointe=(400, 400)))
    return S


def p10():
    S = Scene()
    grenier(S)
    S.add(souris(400, 760, 0.95, 3, expr="timide", bras="bas"))
    S.add(souris(640, 780, 0.8, 1, expr="inquiet"), souris(150, 780, 0.8, 4, expr="inquiet"))
    S.add(bulle(400, 180, 440, 100, "Pas moi !\nJe suis trop petite.", 34, pointe=(400, 520)))
    return S


def p11():
    S = Scene()
    grenier(S)
    S.add(souris(400, 760, 1.2, 1, expr="oups", bras="bas"))
    S.add(pansement(400 + 21 * 1.2, 750, 0.8, rot=90))
    S.add(bulle(400, 150, 460, 100, "Pas moi non plus !\nJ'ai mal à la patte.", 34, pointe=(400, 440)))
    return S


def p12():
    S = Scene()
    grenier(S)
    S.add(souris(230, 760, 1.1, 2, expr="oups", bras="joues"))
    S.add(souris(570, 760, 1.1, 5, expr="timide", bras="croises"))
    S.add(bulle(230, 150, 340, 110, "Moi, je ne sais\npas faire les nœuds !", 28, pointe=(230, 450)))
    S.add(bulle(580, 260, 340, 110, "Moi, je dois\nranger mon trou !", 30, pointe=(570, 450)))
    return S


def p13():
    S = Scene()
    grenier(S)
    S.add(doyenne(400, 760, 1.4, expr="triste", bras="tient", objet=grelot(74, -110, 1.2)))
    S.add(souris(60, 790, 0.6, 1, expr="timide", bras="course", flip=True))
    S.add(souris(740, 790, 0.6, 3, expr="timide", bras="course"))
    S.add(mouvement(130, 740, 0.8, rot=0), mouvement(670, 740, 0.8, rot=180))
    return S


def p14():
    S = Scene()
    grenier(S, nuit_=True)
    S.add(rodilard(600, 790, 1.7, expr="malin", bras="ouverts"))
    S.add(doyenne(170, 790, 0.8, expr="oups", bras="course", flip=True))
    S.add(souris(300, 790, 0.6, 2, expr="oups", bras="course", flip=True))
    S.add(grelot(360, 770, 0.6, ruban_long=16, brille=False))
    S.add(texte(250, 400, "Sauve qui peut !", 50, "#ffe066", contour="#3b2412"))
    return S


def p15():
    S = Scene()
    grenier(S)
    S.add(rodilard(460, 780, 1.6, expr="rire", bras="haut", objet=None))
    S.add(grelot(460 + 70 * 1.6, 780 - 175 * 1.6, 1.3, ruban_long=30))
    S.add(texte(620, 200, "Drelin !", 56, "#f59f00", contour="#fff"))
    S.add(trou_souris(110, 560, 1.2, dedans=g([souris(-30, 0, 0.3, 0, expr="rire"), souris(30, 0, 0.3, 2, expr="rire")])))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("grelot-seul.svg", vignette),
    ("01-rodilard.svg", p01), ("02-on-a-peur.svg", p02), ("03-sur-les-toits.svg", p03),
    ("04-reunion.svg", p04), ("05-la-doyenne.svg", p05), ("06-pas-de-velours.svg", p06),
    ("07-un-grelot.svg", p07), ("08-hourra.svg", p08), ("09-qui-va-l-attacher.svg", p09),
    ("10-trop-petite.svg", p10), ("11-mal-a-la-patte.svg", p11), ("12-les-excuses.svg", p12),
    ("13-toute-seule.svg", p13), ("14-sauve-qui-peut.svg", p14), ("15-drelin.svg", p15),
]
