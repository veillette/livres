"""Bulle, bulle, savon ! — Porcelet apprend à se laver les mains.

Porcelet adore la boue. Avant de manger un biscuit : « Les mains d'abord ! »
Sur ses mains vivent des microbes, trop petits pour qu'on les voie ; la
plupart ne sont pas méchants, mais certains rendent malade. L'eau seule ne
les décolle pas : le savon, oui, il les emporte avec la mousse. Frotter
partout (paumes, dos, entre les doigts, pouces, bout des doigts) le temps de
chanter deux fois « Joyeux anniversaire », rincer, sécher. Se laver les
mains avant de manger, après les toilettes, en rentrant, après s'être
mouché ; éternuer dans son coude. Porcelet montre à son petit frère… et
retourne dans la boue le lendemain !

Plans : 1 large (la flaque de boue) · 2 moyen (les mains d'abord !) · 3 gros
plan (la loupe et les microbes) · 4 moyen (de l'eau seulement) · 5 gros
plan (le savon) · 6 schéma (frotter partout) · 7 moyen (joyeux
anniversaire) · 8 moyen (sécher) · 9 schéma (quand ?) · 10 moyen
(atchoum !) · 11 moyen (comme ça !) · 12 moyen (miam !).
"""
from base import *
from base import _assombrir
from animaux import loupe, etiquette, disque

ID = "porcelet-mains"

PORCELET = dict(habit="#69db7c")
FRERE = dict(habit="#ffd43b")
MAMAN = dict(habit="#9775fa", acc=("tablier",))
ROSE = "#ffc9d6"
BOUE = "#8d5f3a"


def porcelet(x, y, s=1.3, sale=False, **k):
    corps = perso("cochon", x, y, s, **{**PORCELET, **k})
    if not sale:
        return corps
    taches = []
    for hx, hy in mains(x, y, s, k.get("bras", "bas"), k.get("flip", False)):
        taches += [cercle(hx - 4 * s, hy, 11 * s, BOUE, opacity=0.85), cercle(hx + 6 * s, hy + 5 * s, 7 * s, BOUE, opacity=0.85)]
    taches += [cercle(x - 20 * s, y - 20 * s, 9 * s, BOUE, opacity=0.8), cercle(x + 24 * s, y - 60 * s, 7 * s, BOUE, opacity=0.8),
               cercle(x - 10 * s, y - 210 * s, 6 * s, BOUE, opacity=0.8)]
    return corps + g(taches)


def frere(x, y, s=0.95, **k):
    return perso("cochon", x, y, s, **{**FRERE, **k})


def maman(x, y, s=1.7, **k):
    return perso("cochon", x, y, s, **{**MAMAN, **k})


def microbe(x, y, s=1.0, couleur="#9775fa", expr="rire", rot=0):
    """Un microbe rigolo (très, très agrandi)."""
    m = []
    for k in range(10):
        a = k * 36
        m.append(trait(math.cos(math.radians(a)) * 26, math.sin(math.radians(a)) * 22, math.cos(math.radians(a)) * 36,
                       math.sin(math.radians(a)) * 32, _assombrir(couleur, 0.8), 3))
    m.append(ellipse(0, 0, 28, 24, volume(couleur, 0.4, 0.8)))
    m += [cercle(-8, -4, 6, "#fff"), cercle(8, -4, 6, "#fff"), cercle(-7, -3, 3, ENCRE), cercle(9, -3, 3, ENCRE)]
    if expr == "rire":
        m.append(chemin("M -8 8 Q 0 16 8 8", stroke=ENCRE, sw=2.5))
    else:
        m.append(ellipse(0, 10, 4, 5, ENCRE))
    return place(m, x, y, s, rot=rot)


def savon(x, y, s=1.0):
    return place([rect(-40, -24, 80, 48, volume("#ffa8a8", 0.4, 0.8), rx=18), ellipse(-10, -10, 16, 6, "#fff", opacity=0.6)], x, y, s)


def bulles(S, x, y, nb=10, graine=1, r=(8, 20), zone=120):
    rr = random.Random(graine)
    for k in range(nb):
        S.add(cercle(x + rr.uniform(-zone, zone), y + rr.uniform(-zone * 0.6, zone * 0.6), rr.uniform(*r),
                     radial([(0, "#ffffff", 0.2), (0.8, "#e7f5ff", 0.5), (1, "#a5d8ff", 0.9)]), stroke="#a5d8ff", stroke_width=1.5))


def main_icone(x, y, s=1.0, rot=0, flip=False, couleur=ROSE, mousse=False, pli=True):
    """Une main ouverte (paume vers nous), pour les schémas."""
    f = _assombrir(couleur, 0.8)
    m = [rect(-30, -30, 60, 66, volume(couleur, 0.3, 0.8), rx=24)]
    for k, (px, h) in enumerate(((-24, 44), (-8, 52), (8, 50), (22, 40))):
        m.append(rect(px - 7, -30 - h, 14, h + 10, volume(couleur, 0.3, 0.8), rx=7))
    m.append(place([rect(-7, -40, 14, 44, volume(couleur, 0.3, 0.8), rx=7)], -30, 6, rot=-50))
    if pli:
        m.append(chemin("M -14 10 Q 0 18 14 10", stroke=f, sw=2))
    if mousse:
        for px, py, r in ((-20, -10, 10), (6, -24, 12), (18, 4, 9), (-4, 14, 8)):
            m.append(cercle(px, py, r, "#fff", stroke="#a5d8ff", stroke_width=1.5))
    return place(m, x, y, s, flip=flip, rot=rot)


def fleche_ronde(x, y, r=60, couleur="#1c7ed6"):
    return g([chemin(f"M {x - r} {y} A {r} {r} 0 1 1 {x} {y + r}", stroke=couleur, sw=5),
              poly([(x - 2, y + r - 12), (x - 2, y + r + 12), (x - 18, y + r)], couleur)])


def lavabo(x, y, s=1.0, eau=False):
    m = [rect(-18, -170, 36, 170, volume("#ffffff", 0.05, 0.86), rx=10, stroke="#dee2e6", stroke_width=3),
         chemin("M -100 -200 L 100 -200 Q 94 -150 0 -146 Q -94 -150 -100 -200 Z", volume("#ffffff", 0.05, 0.86), stroke="#dee2e6", sw=3),
         rect(-8, -240, 16, 40, "#adb5bd", rx=4), chemin("M 0 -240 Q 34 -244 34 -218", stroke="#adb5bd", sw=8)]
    if eau:
        m.append(rect(30, -216, 8, 30, "#74c0fc", opacity=0.8, rx=4))
    return place(m, x, y, s)


def salle_de_bain(S):
    interieur(S, "#fff0f6", "#e9ecef", y=600)
    for yy in range(60, 600, 60):
        S.add(trait(0, yy, 800, yy, "#ffdeeb", 3))
    for xx in range(60, 800, 60):
        S.add(trait(xx, 0, xx, 600, "#ffdeeb", 3))
    S.add(rect(560, 140, 160, 200, "#e7f5ff", stroke="#adb5bd", stroke_width=6, rx=12))


def cuisine(S):
    piece(S, "cuisine", y=600)
    S.add(fenetre(90, 90, 170, 160, "#a5d8ff", rideaux="#ffc9c9"))
    S.add(rect(470, 70, 280, 130, volume("#ffe8cc", 0.2, 0.85), rx=8), trait(610, 70, 610, 200, "#e8c39e", 3),
          cercle(590, 150, 6, "#c68642"), cercle(630, 150, 6, "#c68642"))


def au_lavabo(S, x, y, s, perso_fn, **k):
    """Un personnage derrière le lavabo, monté sur un tabouret : on le voit à travers le miroir de la page."""
    S.add(rect(x - 90, y - 130, 180, 50, "#74c0fc", rx=10), rect(x - 74, y - 80, 20, 80, "#4dabf7"), rect(x + 54, y - 80, 20, 80, "#4dabf7"))
    S.add(perso_fn(x, y - 126, s, **k))
    S.add(lavabo(x, y, 1.15, eau=True))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#e7f5ff")
    bulles(S, 400, 300, 22, graine=1, r=(14, 38), zone=340)
    S.add(porcelet(400, 800, 2.0, expr="rire", bras="ouverts", regard=(0, -1)))
    for hx, hy in mains(400, 800, 2.0, "ouverts"):
        bulles(S, hx, hy - 10, 8, graine=int(hx), r=(10, 22), zone=50)
    S.cachette(730, 460, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(savon(300, 220, 0.9))
    bulles(S, 300, 150, 8, graine=2, r=(8, 18), zone=70)
    S.add(porcelet(140, 262, 0.75, expr="rire", bras="ouverts", regard=(1, -0.3)))
    return S


def p01():
    """Plan large : dehors, Porcelet saute dans une flaque de boue : « Splatch ! » ; ses mains sont toutes sales."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 470, "#b2f2bb", graine=3)
    S.add(rect(0, 560, 800, 240, terrain("#8ce99a")))
    S.add(arbre(110, 580, 1.0))
    S.add(ellipse(400, 760, 260, 50, volume(BOUE, 0.35, 0.8)))
    for k in range(9):
        a = math.radians(200 + k * 18)
        S.add(cercle(400 + math.cos(a) * 260, 700 + math.sin(a) * 90, 12 - k % 3 * 2, BOUE))
    S.add(porcelet(400, 780, 1.8, sale=True, expr="rire", bras="haut", regard=(0, -0.5), pas="saute"))
    S.add(texte(400, 140, "Splatch !", 70, BOUE, contour="#fff"))
    return S


def p02():
    """Plan moyen : à la cuisine, Porcelet tend la main vers les biscuits ; Maman : « Stop ! Les mains d'abord ! »"""
    S = Scene()
    cuisine(S)
    S.add(table(330, 790, 300, 150, nappe="#ffe3e3"))
    S.add(assiette_biscuits(330, 610))
    S.add(porcelet(180, 800, 1.8, sale=True, expr="miam", bras="tend", regard=(1, 0.5)))
    S.add(maman(610, 800, 2.05, expr="surpris", bras="designe", flip=True, regard=(-1, 0.3)))
    S.add(bulle(560, 140, 360, 110, "Stop !\nLes mains d'abord !", 34, pointe=(580, 300)))
    S.cachette(320, 70, "air")
    return S


def assiette_biscuits(x, y, s=1.0):
    m = [ellipse(0, 0, 90, 18, "#fff", stroke="#dee2e6", stroke_width=3)]
    for px, py in ((-40, -12), (0, -18), (40, -12), (-20, -30), (20, -30)):
        m += [cercle(px, py, 20, volume("#e9b872", 0.3, 0.8)), cercle(px - 6, py - 4, 3, "#6d4424"), cercle(px + 6, py + 4, 3, "#6d4424")]
    return place(m, x, y, s)


def p03():
    """Gros plan : sous la loupe, sur la main de Porcelet, de minuscules microbes rigolos."""
    S = Scene()
    fond(S, "#fff0f6")
    contenu = g([rect(250, 150, 300, 300, ROSE), cercle(380, 260, 30, BOUE, opacity=0.4)] +
                [microbe(px, py, 0.8, c) for px, py, c in ((340, 220, "#9775fa"), (440, 250, "#51cf66"), (380, 330, "#ff922b"), (460, 360, "#4dabf7"))])
    S.add(main_icone(470, 650, 3.2, rot=12, pli=False))
    S.add(loupe(330, 330, 180, contenu, rot=130))
    S.add(texte(400, 80, "Des microbes !", 56, "#9775fa", contour="#fff"))
    S.cachette(740, 790)
    return S


def p04():
    """Plan moyen : Porcelet rince ses mains avec de l'eau seulement ; les microbes restent collés et rigolent."""
    S = Scene()
    salle_de_bain(S)
    au_lavabo(S, 360, 800, 1.6, porcelet, expr="inquiet", bras="porte", regard=(0, 0.6))
    for px, py, c in ((250, 470, "#9775fa"), (470, 460, "#51cf66"), (300, 410, "#ff922b")):
        S.add(microbe(px, py, 0.7, c))
    S.add(bulle(620, 420, 220, 90, "Hi hi hi !", 34, pointe=(480, 460)))
    S.add(texte(400, 110, "De l'eau seulement…", 48, "#1c7ed6", contour="#fff"))
    return S


def p05():
    """Gros plan : avec le savon, la mousse ! les microbes glissent et s'en vont : « Frotte, frotte ! »"""
    S = Scene()
    salle_de_bain(S)
    au_lavabo(S, 400, 880, 1.75, porcelet, expr="rire", bras="porte", regard=(0, 0.6))
    bulles(S, 400, 660, 24, graine=5, r=(10, 26), zone=150)
    for px, py, c, r in ((180, 440, "#9775fa", -30), (620, 430, "#51cf66", 30), (660, 560, "#ff922b", 50)):
        S.add(microbe(px, py, 0.7, c, expr="o", rot=r))
    S.camera(1.1, 400, 520)
    S.dessus(texte(400, 100, "Frotte, frotte !", 60, "#1c7ed6", contour="#fff"))
    return S


def p06():
    """Schéma : frotter partout : les paumes, le dos des mains, entre les doigts, les pouces, le bout des doigts."""
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(texte(400, 90, "Frotter partout !", 48, "#1c7ed6"))
    cases = [(160, 250, "les paumes"), (400, 250, "le dos"), (640, 250, "entre les doigts"),
             (270, 560, "les pouces"), (530, 560, "le bout des doigts")]
    for k, (x, y, nom) in enumerate(cases):
        S.add(disque(x, y, 100, "#fff", "#d0ebff"))
        if k == 0:
            S.add(main_icone(x - 18, y + 10, 0.9, rot=-10, mousse=True), main_icone(x + 18, y + 10, 0.9, rot=10, flip=True, couleur="#ffb3c6"))
        elif k == 1:
            S.add(main_icone(x, y + 14, 0.95, mousse=True), main_icone(x + 10, y - 4, 0.9, rot=170, couleur="#ffb3c6"))
        elif k == 2:
            S.add(main_icone(x - 10, y + 10, 0.9, rot=-20), main_icone(x + 10, y + 4, 0.9, rot=20, flip=True, couleur="#ffb3c6", mousse=True))
        elif k == 3:
            S.add(main_icone(x, y + 10, 0.95, mousse=True), cercle(x - 30, y + 14, 22, "#ffb3c6"))
        else:
            S.add(main_icone(x, y + 14, 0.95, mousse=True), cercle(x + 4, y + 10, 18, "#ffb3c6"))
        S.add(fleche_ronde(x + 6, y - 4, 74, "#74c0fc"))
        S.add(etiquette(x, y + 136, nom, 26, "#495057"))
    S.cachette(740, 790)
    return S


def p07():
    """Plan moyen : Porcelet chante « Joyeux anniversaire » deux fois en frottant ses mains pleines de mousse."""
    S = Scene()
    salle_de_bain(S)
    au_lavabo(S, 330, 800, 1.6, porcelet, expr="chante", bras="porte", regard=(0, 0.6))
    bulles(S, 330, 580, 14, graine=7, r=(8, 18), zone=110)
    S.add(notes(500, 330, 1.2, "#e64980"))
    S.add(bulle(560, 190, 380, 110, "Joyeux anniversaire…\nencore une fois !", 30, pointe=(420, 330)))
    return S


def p08():
    """Plan moyen : Porcelet rince ses mains puis les sèche bien avec la serviette."""
    S = Scene()
    salle_de_bain(S)
    S.add(lavabo(600, 800, 1.1))
    S.add(rect(100, 300, 180, 12, "#adb5bd", rx=6))
    S.add(porcelet(330, 800, 1.8, expr="content", bras="porte", regard=(0, 0.4),
                   objet=g([rect(-60, -112, 120, 66, "#74c0fc", rx=12), rect(-60, -60, 120, 10, "#4dabf7")])))
    S.add(texte(400, 130, "Bien sécher !", 56, "#1c7ed6", contour="#fff"))
    return S


def p09():
    """Schéma : quand se laver les mains ? avant de manger, après les toilettes, en rentrant, après s'être mouché."""
    S = Scene()
    fond(S, "#fff9db")
    S.add(texte(400, 90, "Quand ?", 56, "#e8590c"))
    cases = [(220, 280, "avant de manger"), (580, 280, "après les toilettes"), (220, 590, "en rentrant"), (580, 590, "après s'être mouché")]
    for k, (x, y, nom) in enumerate(cases):
        S.add(disque(x, y, 110, "#fff", "#ffe066"))
        if k == 0:
            S.add(ellipse(x, y + 20, 60, 14, "#fff", stroke="#adb5bd", stroke_width=3), trait(x - 80, y - 30, x - 80, y + 40, "#868e96", 6),
                  trait(x + 80, y - 30, x + 80, y + 40, "#868e96", 6), assiette_biscuits(x, y + 14, 0.5))
        elif k == 1:
            S.add(rect(x - 30, y - 70, 60, 46, "#fff", stroke="#adb5bd", stroke_width=3, rx=8), rect(x - 16, y - 24, 32, 76, "#fff", stroke="#adb5bd", stroke_width=3, rx=10),
                  ellipse(x, y - 24, 44, 12, "#fff", stroke="#adb5bd", stroke_width=3))
        elif k == 2:
            S.add(rect(x - 40, y - 70, 80, 130, "#b5835a", rx=6), cercle(x + 24, y, 6, "#ffd43b"))
        else:
            S.add(rect(x - 40, y - 40, 80, 70, "#fff", stroke="#adb5bd", stroke_width=3, rx=8), chemin(f"M {x - 30} {y - 40} Q {x} {y - 70} {x + 30} {y - 40}", "#fff", stroke="#adb5bd", sw=3))
        S.add(etiquette(x, y + 150, nom, 28, "#495057"))
    S.cachette(740, 790)
    return S


def p10():
    """Plan moyen : Porcelet éternue dans son coude : « Atchoum ! » ; son petit frère le regarde."""
    S = Scene()
    cuisine(S)
    S.add(porcelet(300, 800, 1.8, expr="concentre", bras="chut", regard=(1, 0)))
    S.add(frere(580, 800, 1.3, expr="surpris", bras="joues", flip=True, regard=(-1, -0.3)))
    S.add(texte(470, 330, "ATCHOUM !", 64, "#e8590c", contour="#fff"))
    S.add(bulle(600, 380, 260, 90, "Dans le coude !", 30, pointe=(400, 460)))
    return S


def p11():
    """Plan moyen : au lavabo, Porcelet montre à son petit frère comment frotter ses mains : « Comme ça ! »"""
    S = Scene()
    salle_de_bain(S)
    S.add(rect(170, 670, 460, 50, "#74c0fc", rx=10), rect(190, 720, 20, 80, "#4dabf7"), rect(590, 720, 20, 80, "#4dabf7"))
    S.add(porcelet(290, 674, 1.6, expr="rire", bras="porte", regard=(1, 0.3)))
    S.add(frere(510, 674, 1.2, expr="content", bras="porte", flip=True, regard=(-1, 0.3)))
    S.add(lavabo(400, 800, 1.3, eau=True))
    bulles(S, 400, 560, 14, graine=11, r=(8, 18), zone=150)
    S.add(bulle(220, 160, 240, 90, "Comme ça !", 36, pointe=(280, 330)))
    return S


def p12():
    """Plan moyen : à table, avec ses mains toutes propres, Porcelet croque son biscuit : « Miam ! »"""
    S = Scene()
    cuisine(S)
    S.add(maman(620, 800, 2.05, expr="content", bras="hanches", flip=True, regard=(-1, 0.3)))
    S.add(porcelet(300, 800, 1.8, expr="miam", bras="tient", regard=(1, 0),
                   objet=g([cercle(68, -150, 22, volume("#e9b872", 0.3, 0.8)), cercle(62, -154, 3, "#6d4424"), cercle(74, -144, 3, "#6d4424")])))
    S.add(table(330, 800, 300, 120, nappe="#ffe3e3"))
    S.add(assiette_biscuits(330, 662, 0.9))
    S.add(texte(300, 330, "Miam !", 70, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("porcelet-seul.svg", vignette),
    ("01-splatch.svg", p01), ("02-les-mains-d-abord.svg", p02), ("03-les-microbes.svg", p03),
    ("04-de-l-eau.svg", p04), ("05-le-savon.svg", p05), ("06-partout.svg", p06),
    ("07-joyeux-anniversaire.svg", p07), ("08-secher.svg", p08), ("09-quand.svg", p09),
    ("10-atchoum.svg", p10), ("11-comme-ca.svg", p11), ("12-miam.svg", p12),
]
