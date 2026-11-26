"""Les petits pas de la patinoire."""
from base import *
from fantastique import personne, personne_assise

ID = "patinoire-debutants"
CAMILLE = dict(peau="claire", cheveux="brun", coiffure="courts", habit="#4baba9", robe=False, taches=True)
YARA = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#dd9c53", robe=False, nez="rond")
GRANDE = dict(peau="claire", cheveux="brun", coiffure="queue", habit="#d67c99", robe=False, stature="ado")
CASQUES = ("#5bb6c4", "#9c79cb", "#d87d94")


def casque(couleur):
    return g([chemin("M -52 -166 Q -62 -221 -26 -232 Q 26 -250 55 -202 L 55 -174 "
                     "Q 9 -185 -52 -166 Z", volume(couleur, 0.36, 0.76), stroke="#456778", sw=3.2),
              chemin("M -44 -192 Q -1 -209 47 -197", stroke=eclaircir(couleur, 0.43), sw=5),
              chemin("M -43 -166 L -36 -131 M 43 -172 L 36 -130", stroke="#495469", sw=4)])


def patin(x, y, s=1, couleur="#4eb0bb", rot=0):
    return place([chemin("M -24 5 L 21 5 Q 37 5 41 -4 M -12 -6 V 4 M 20 -6 V 4",
                         stroke="#66778d", sw=4),
                  chemin("M -22 -36 Q -3 -31 8 -39 L 14 -19 Q 37 -21 41 -10 Q 42 -5 32 -5 H -20 Q -27 -9 -22 -36 Z",
                         "#f7f7f4", stroke="#a9bccc", sw=2),
                  chemin("M -5 -30 L 11 -31 M -3 -24 L 14 -25 M 3 -18 L 23 -19", stroke=couleur, sw=2.5)],
                 x, y, s, rot=rot)


def patineuse(x, y, s, style, numero, bras, regard, inclinaison=0, sur_glace=True, assise=False):
    dessiner = personne_assise if assise else personne
    dessin = dessiner(0, 0, bras=bras, regard=regard, coiffe=casque(CASQUES[numero]),
                      chaussures="#f7f7f4" if sur_glace else None, **style)
    m = [dessin]
    if sur_glace:
        limite = 13 if assise else -5
        coupe = uid("patins")
        m = [el("clipPath", rect(-190, -325, 380, 325 + limite, "#000"), id=coupe),
             g(dessin, clip_path=f"url(#{coupe})"),
             patin(-23, limite + 7, 0.68, CASQUES[numero], -8),
             patin(11, limite + 8, 0.68, CASQUES[numero], 8)]
    return place(m, x, y, s, rot=inclinaison)


def patinoire(banc=False):
    S = Scene()
    ciel(S, "#99bcda", "#e2eafa")
    collines(S, 429, "#bfcee4", graine=36, bosquets=False)
    sol(S, 492, "#e9f1fb")
    for x, y, s in ((58, 498, 0.73), (175, 444, 0.57), (643, 444, 0.51), (755, 480, 0.74)):
        S.add(sapin(x, y, s, "#688e90", "#96b8b5", neige=True))
    S.add(ellipse(420, 675, 412, 165, lineaire([(0, "#9ec7de"), (1, "#daeff5")])),
          chemin("M 41 676 Q 99 553 391 553 Q 708 549 779 675", stroke="#f4fbff", sw=7),
          chemin("M 52 654 Q 74 537 399 530 Q 702 530 767 652", stroke="#678797", sw=12),
          chemin("M 57 607 Q 99 501 398 497 Q 688 494 755 607", stroke="#f9faf5", sw=11))
    for x, y in ((66, 588), (144, 536), (250, 510), (392, 495), (530, 503), (654, 535), (746, 591)):
        S.add(trait(x, y, x, y + 59, "#839eaa", 8))
    for x, y in ((118, 726), (242, 684), (382, 749), (486, 646), (536, 720), (679, 751)):
        S.add(chemin(f"M {x} {y} q 28 -13 54 -15 m -33 15 q 30 -11 52 -12", stroke="#eff8fa", sw=2.8))
    if banc:
        S.add(chemin("M 0 648 L 315 653 L 367 800 H 0 Z", "#d8d5db", stroke="#b8bac7", sw=4),
              rect(62, 660, 254, 38, "#b98e75", rx=12),
              rect(67, 682, 244, 17, "#a48070", rx=6),
              rect(78, 693, 16, 61, "#687684", rx=3), rect(288, 693, 16, 61, "#687684", rx=3))
    S.cachette(750, 552, "air")
    return S


def cone(x, y):
    return g([chemin(f"M {x - 27} {y - 5} l 19 -64 q 8 -6 16 0 l 19 64 Z", "#f78443"),
              ellipse(x, y, 38, 11, "#d47548"), trait(x - 13, y - 38, x + 13, y - 38, "#fff4d6", 7)])


def couverture():
    S = patinoire()
    S.add(patineuse(279, 672, 1.37, CAMILLE, 0, "equilibre", (1, 0.2), -9),
          patineuse(527, 687, 1.42, YARA, 1, "ouverts", (-1, 0.22), 8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(193, 199, 151, 20, "#d7e9f3"),
          patin(140, 183, 1.88, rot=-16), patin(234, 197, 1.99, rot=13))
    return S


def p01():
    """Large — banc."""
    S = patinoire(banc=True)
    S.add(patineuse(113, 689, 1.01, CAMILLE, 0, "porte", (1, 0.15), sur_glace=False, assise=True),
          patineuse(249, 688, 1.03, GRANDE, 2, "porte", (-1, 0.3), assise=True),
          patin(117, 752, 0.78), patin(161, 748, 0.78, rot=13))
    return S


def p02():
    """Moyen — au bord."""
    S = patinoire()
    S.add(patineuse(272, 664, 1.14, CAMILLE, 0, "tient", (1, 0.15), 6),
          patineuse(561, 641, 1.10, GRANDE, 2, "equilibre", (-1, 0.15), -12))
    return S


def p03():
    """Moyen — bonjour."""
    S = patinoire()
    S.add(patineuse(288, 664, 1.18, CAMILLE, 0, "tient", (1, 0.15), 5),
          patineuse(482, 661, 1.16, YARA, 1, "tient", (-1, 0.15), -6))
    return S


def p04():
    """Gros plan — petits pas."""
    S = patinoire()
    S.add(patineuse(324, 705, 1.42, CAMILLE, 0, "equilibre", (1, 0.2), -9),
          patineuse(507, 701, 1.42, YARA, 1, "equilibre", (-1, 0.2), 9))
    S.camera(2.58, 418, 650)
    S.cachette(554, 755, "air")
    return S


def p05():
    """Large — premiere glisse."""
    S = patinoire()
    S.add(patineuse(274, 645, 1.12, CAMILLE, 0, "equilibre", (1, 0.15), -7),
          patineuse(456, 647, 1.10, YARA, 1, "equilibre", (-1, 0.2), 7),
          patineuse(635, 625, 0.9, GRANDE, 2, "salut", (-1, 0.2)))
    return S


def p06():
    """Moyen — on recommence."""
    S = patinoire()
    S.add(ellipse(356, 690, 94, 12, "#7baebe", opacity=0.35),
          patineuse(329, 668, 1.03, CAMILLE, 0, "porte", (1, -0.4), -9, assise=True),
          patineuse(539, 644, 1.23, YARA, 1, "donne", (-1, 0.6)))
    return S


def p07():
    """Moyen — jusqu au cone."""
    S = patinoire()
    S.add(patineuse(271, 703, 1.26, CAMILLE, 0, "equilibre", (1, 0.15), -10),
          patineuse(471, 612, 1.02, YARA, 1, "ouverts", (1, 0.15), 8),
          patineuse(657, 613, 0.85, GRANDE, 2, "salut", (-1, 0.2)),
          cone(627, 656))
    S.camera(1.33, 449, 500)
    S.cachette(704, 678, "air")
    return S


def p08():
    """Large — demain."""
    S = patinoire(banc=True)
    S.add(patineuse(284, 714, 1.21, CAMILLE, 0, "salut", (1, 0.15), sur_glace=False),
          patineuse(536, 683, 1.12, YARA, 1, "coucou", (-1, 0.15)))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-banc.svg", p01),
    ("02-au-bord.svg", p02),
    ("03-bonjour.svg", p03),
    ("04-petits-pas.svg", p04),
    ("05-premiere-glisse.svg", p05),
    ("06-on-recommence.svg", p06),
    ("07-jusqu-au-cone.svg", p07),
    ("08-demain.svg", p08),
]
