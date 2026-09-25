"""Fâchés, pas fâchés — se disputer et se réconcilier."""
from base import *
from objets import *

ID = "fache-pas-fache"
CHAT = dict(couleur="#868e96", habit="#ff8787", motif="rayures", couleur_motif="#ffc9c9")
CHIEN = dict(habit="#4dabf7", motif="pois", couleur_motif="#a5d8ff")
SABLE = "#f4d58d"
SABLE2 = "#e8c170"


def plage(S, orage=False):
    ciel(S, "#74c0fc" if not orage else "#adb5bd", "#e7f5ff")
    S.add(rect(0, 430, 800, 140, "#339af0"))
    for k in range(6):
        S.add(chemin(f"M {k * 150} 470 q 25 -12 50 0", stroke="#a5d8ff", sw=5))
    S.add(chemin("M 0 560 Q 200 540 400 560 T 800 555 L 800 800 L 0 800 Z", SABLE))
    for k in range(20):
        S.add(cercle(30 + (k * 97) % 760, 600 + (k * 53) % 190, 3, SABLE2))


def tour(x, y, s=1.0, drapeau=None):
    m = [rect(-40, -140, 80, 140, SABLE2), rect(-50, -160, 100, 26, SABLE2)]
    for k in range(3):
        m.append(rect(-50 + k * 38, -178, 24, 22, SABLE2))
    m.append(rect(-14, -60, 28, 60, "#c9a14d", rx=14))
    if drapeau:
        m += [trait(0, -178, 0, -260, "#495057", 4), poly([(0, -260), (50, -246), (0, -230)], drapeau)]
    return place(m, x, y, s)


def pont(x, y, s=1.0, w=240):
    m = [chemin(f"M {-w / 2} 0 L {-w / 2} -70 L {w / 2} -70 L {w / 2} 0 L {w / 2 - 50} 0 Q 0 -80 {-w / 2 + 50} 0 Z", SABLE2)]
    for k in range(6):
        m.append(rect(-w / 2 + k * w / 5.2, -90, 24, 22, SABLE2))
    return place(m, x, y, s)


def chateau(x, y, s=1.0, tours=1, pont_=False, drapeaux=("#fa5252",)):
    m = [rect(-120, -80, 240, 80, SABLE2)]
    m.append(tour(-80, 0, 1.0, drapeaux[0] if tours >= 1 else None))
    if tours >= 2:
        m.append(tour(80, 0, 1.0, drapeaux[-1]))
    if pont_:
        m.append(pont(230, 0, 1.0))
        m.append(tour(380, 0, 1.2, "#4dabf7"))
    return place(m, x, y, s)


def tas_sable(x, y, s=1.0):
    return place([chemin("M -150 0 Q -120 -70 -40 -80 Q 30 -100 80 -60 Q 140 -40 150 0 Z", SABLE2),
                  rect(-60, -40, 40, 30, SABLE2, rot=None), cercle(90, -30, 20, SABLE2)], x, y, s)


def seau(x, y, s=1.0, couleur="#fab005"):
    return place([chemin("M -30 -60 L 30 -60 L 22 0 L -22 0 Z", couleur), chemin("M -30 -60 Q 0 -110 30 -60", stroke="#495057", sw=4)], x, y, s)


def pelle(x, y, s=1.0, rot=0, couleur="#fa5252"):
    return place([rect(-4, -100, 8, 90, couleur, rx=3), chemin("M -20 -10 L 20 -10 L 14 30 Q 0 40 -14 30 Z", couleur)], x, y, s, rot=rot)


def couverture():
    S = Scene()
    plage(S)
    S.add(perso("chat", 250, 760, 1.5, expr="fache", bras="croises", regard=(-1, 0), **CHAT))
    S.add(perso("chien", 560, 760, 1.5, expr="fache", bras="croises", regard=(1, 0), **CHIEN))
    S.add(tas_sable(400, 790, 0.8))
    S.add(texte(400, 400, "Hmpf !", 60, "#e03131", contour="#fff"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("chat", 130, 265, 0.75, expr="rire", bras="salut", **CHAT))
    S.add(perso("chien", 270, 265, 0.75, expr="rire", bras="salut", flip=True, **CHIEN))
    return S


def p01():
    S = Scene()
    plage(S)
    S.add(perso("chat", 280, 760, 1.5, expr="rire", bras="salut", flip=True, **CHAT))
    S.add(perso("chien", 520, 760, 1.5, expr="rire", bras="salut", **CHIEN))
    S.add(seau(120, 770, 1.2), pelle(680, 780, 1.1, rot=20))
    S.add(soleil(680, 120, 50))
    S.add(coeur(400, 330, 1.6))
    return S


def p02():
    S = Scene()
    plage(S)
    S.add(chateau(400, 720, 1.0, tours=1))
    S.add(perso("chat", 170, 780, 1.4, expr="joie", bras="montre", regard=(1, -1), **CHAT))
    S.add(perso("chien", 640, 780, 1.4, expr="joie", bras="ouverts", regard=(-1, -1), **CHIEN))
    S.add(bulle(180, 170, 280, 90, "Une tour !", 44, pointe=(180, 400)))
    S.add(bulle(620, 170, 280, 90, "Un pont !", 44, pointe=(620, 400)))
    return S


def p03():
    S = Scene()
    plage(S)
    S.add(tas_sable(400, 660, 1.2))
    S.add(perso("chat", 250, 780, 1.4, expr="furieux", bras="tire", regard=(1, 0), **CHAT))
    S.add(perso("chien", 550, 780, 1.4, expr="furieux", bras="tire", flip=True, regard=(1, 0), **CHIEN))
    S.add(pelle(400, 700, 1.2, rot=90))
    S.add(texte(400, 250, "CRAC !", 110, "#e03131", contour="#fff", rot=-6))
    return S


def p04():
    S = Scene()
    plage(S, orage=True)
    S.add(nuage_orage(400, 150, 0.8))
    S.add(tas_sable(400, 700, 0.9))
    S.add(perso("chat", 150, 780, 1.4, expr="fache", bras="croises", regard=(-1, 0), **CHAT))
    S.add(perso("chien", 650, 780, 1.4, expr="fache", bras="croises", regard=(1, 0), **CHIEN))
    S.add(bulle(180, 330, 300, 90, "Plus copain !", 38, pointe=(160, 480)))
    S.add(bulle(620, 330, 300, 90, "Toi non plus !", 38, pointe=(640, 480)))
    return S


def p05():
    S = Scene()
    plage(S)
    S.add(tour(160, 760, 0.7), perso("chat", 280, 780, 1.2, expr="triste", **CHAT))
    S.add(pont(640, 760, 0.6), perso("chien", 500, 780, 1.2, expr="triste", **CHIEN))
    S.add(texte(400, 340, "Tout seul, ce n'est pas", 38, "#495057", contour="#fff"))
    S.add(texte(400, 390, "très amusant…", 38, "#495057", contour="#fff"))
    return S


def p06():
    S = Scene()
    plage(S)
    S.add(tour(120, 760, 0.7), perso("chat", 280, 780, 1.3, expr="timide", regard=(1, 0), **CHAT))
    S.add(pont(700, 760, 0.6), perso("chien", 520, 780, 1.3, expr="timide", regard=(-1, 0), **CHIEN))
    S.add(texte(400, 330, "…", 90, "#495057"))
    return S


def p07():
    S = Scene()
    plage(S)
    S.add(perso("chat", 300, 780, 1.5, expr="sourire", bras="donne", regard=(1, 0), **CHAT))
    S.add(perso("chien", 500, 780, 1.5, expr="sourire", bras="donne", flip=True, regard=(-1, 0), **CHIEN))
    S.add(bulle(250, 170, 260, 90, "Pardon !", 44, pointe=(290, 420)))
    S.add(bulle(560, 190, 360, 110, "Pardon aussi !\nUne tour ET un pont ?", 30, pointe=(510, 420)))
    return S


def p08():
    S = Scene()
    plage(S)
    S.add(soleil(680, 110, 50))
    S.add(chateau(250, 740, 1.1, tours=2, pont_=True, drapeaux=("#fa5252", "#fab005")))
    S.add(perso("chat", 250, 656, 1.1, expr="rire", bras="haut", **CHAT))
    S.add(perso("chien", 500, 666, 1.1, expr="rire", bras="haut", **CHIEN))
    S.add(texte(400, 200, "Le plus beau château !", 50, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("amis-seuls.svg", vignette),
    ("01-amis.svg", p01), ("02-tour-ou-pont.svg", p02), ("03-crac.svg", p03),
    ("04-fache.svg", p04), ("05-tout-seul.svg", p05), ("06-coup-d-oeil.svg", p06),
    ("07-pardon.svg", p07), ("08-chateau.svg", p08),
]
