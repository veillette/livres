"""Le manteau de l'érable."""
from base import *
from fantastique import personne
from objets import pot_peinture

ID = "manteau-erable"
LEO = dict(peau="rosee", cheveux="roux", coiffure="herisses", habit="#3d91b9", robe=False, taches=True)
PAPA = dict(peau="rosee", cheveux="chatain", coiffure="raie", habit="#658d62",
            robe=False, stature="adulte", carrure="ronde", nez="long")
COULEURS = ("#bd4a38", "#e38441", "#edb942", "#cd5c37")


def feuille(x, y, s=1, couleur="#cc4939", rot=0):
    m = [chemin("M 0 -64 L 12 -42 L 24 -47 L 22 -24 L 37 -29 L 54 -38 L 50 -20 "
                "L 64 -17 L 42 5 L 43 14 L 11 19 L 0 29 L -10 19 L -43 14 L -41 4 "
                "L -64 -17 L -49 -20 L -55 -38 L -36 -29 L -22 -22 L -25 -47 L -12 -42 Z",
                volume(couleur, 0.26, 0.77)),
         chemin("M 0 43 Q 4 13 0 -47 M 1 21 L 37 -12 M 1 20 L -36 -12 M 1 7 L 15 -28 M 1 7 L -15 -28",
                stroke="#742f28", sw=2.6, opacity=0.61)]
    return place(m, x, y, s, rot=rot)


def erable(x, y, s=1, nu=False):
    ramures = ((-142, -282), (-101, -354), (-51, -333), (-43, -404),
               (13, -425), (38, -353), (101, -395), (124, -318), (160, -297))
    m = [chemin("M -42 0 Q -12 -94 -29 -206 Q -50 -249 -142 -282 L -140 -296 L -43 -260 "
                "Q -56 -314 -101 -354 L -98 -364 Q -28 -328 -13 -257 Q -25 -361 -44 -405 L -35 -410 "
                "Q -6 -370 2 -296 Q 18 -355 10 -425 L 20 -426 Q 35 -353 26 -302 "
                "Q 60 -356 99 -395 L 107 -391 Q 73 -347 52 -302 L 126 -329 L 129 -318 L 65 -276 "
                "L 160 -307 L 165 -294 Q 108 -265 56 -229 Q 18 -158 34 0 Z",
                volume("#936a57", 0.35, 0.62)),
         chemin("M -16 -16 Q -2 -109 -8 -204 M 6 -57 Q 4 -166 29 -239", stroke="#bc9173", sw=4)]
    for k, (bx, by) in enumerate(ramures):
        if nu:
            m += [trait(bx, by, bx + 12, by - 21, "#816050", 4),
                  ellipse(bx + 12, by - 21, 3, 6, "#96584a", rot=21)]
        else:
            m += [ellipse(bx, by + 9, 67, 59, COULEURS[k % 4], rot=k * 17),
                  ellipse(bx - 13, by - 13, 47, 36, COULEURS[(k + 1) % 4])]
            for j in range(6):
                m.append(feuille(bx - 42 + j * 17, by + (j * 29 % 62) - 30, 0.19, COULEURS[(j + k + 2) % 4], j * 29))
    return place(m, x, y, s)


def parc(nu=False):
    S = Scene()
    paysage(S, 520, 571, herbe_="#c9c08d", colline="#e3c8a1", haut="#a9cbe2", bas="#ffe8c5", graine=25)
    S.add(chemin("M 103 800 Q 210 648 363 607 Q 454 585 594 536 L 627 534 Q 416 636 331 800 Z", "#d7b8a0"),
          erable(512, 671, 1.28, nu))
    for j in range(16):
        x = 78 + j * 67 % 655
        y = 629 + j * 29 % 149
        S.add(feuille(x, y, 0.19 + (y - 629) / 625, COULEURS[j % 4], j * 67))
    return S


def tableau(x, y, s=1):
    m = [rect(-121, -86, 242, 172, "#ecdeb5", stroke="#87685b", stroke_width=4, rx=3),
         erable(5, 64, 0.30, True)]
    m += [feuille(-37, -48, 0.39, COULEURS[0], -25),
          feuille(30, -41, 0.38, COULEURS[2], 32),
          feuille(83, 28, 0.38, COULEURS[1], 66)]
    return place(m, x, y, s)


def couverture():
    S = parc()
    S.add(personne(339, 749, 1.46, regard=(1, -0.1), bras="tient", **LEO),
          feuille(440, 501, 1.04, COULEURS[0], 13))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(feuille(128, 147, 1.02, COULEURS[0], -32), feuille(206, 112, 0.97, COULEURS[1], 12),
          feuille(280, 155, 0.92, COULEURS[2], 52))
    return S


def p01():
    """Large — feuille rouge."""
    S = parc()
    S.add(personne(313, 719, 1.04, regard=(1, -0.6), expr="surpris", **LEO),
          feuille(356, 505, 0.38, COULEURS[0], 37))
    return S


def p02():
    """Moyen — collection."""
    S = parc()
    S.add(personne(325, 717, 1.24, regard=(1, 0.65), bras="ramasse", **LEO),
          personne(179, 665, 1.06, regard=(1, 0.42), **PAPA),
          feuille(396, 697, 0.44, COULEURS[2], 71))
    return S


def p03():
    """Gros plan — branche trop haute."""
    S = parc()
    S.add(personne(284, 725, 1.26, regard=(1, -0.5), bras="tend", **PAPA),
          personne(408, 609, 1.24, regard=(1, -0.9), bras="haut", **LEO),
          feuille(534, 323, 0.48, COULEURS[0], 49))
    S.camera(1.41, 458, 446)
    S.cachette(636, 625, "air")
    return S


def p04():
    """Large — pluie rousse."""
    S = parc()
    S.add(personne(345, 708, 1.15, regard=(1, -0.14), bras="lance", **LEO),
          personne(202, 686, 1.08, regard=(1, 0), **PAPA))
    for j in range(14):
        S.add(feuille(282 + j * 33, 289 + j * 23 + 38 * math.sin(j), 0.33, COULEURS[j % 4], -38 + j * 22))
    return S


def p05():
    """Gros plan — sous les livres."""
    S = Scene()
    piece(S, "chaumiere", 546)
    S.add(table(398, 764, 510, 181, "#b08669"),
          poly([(228, 575), (295, 509), (539, 515), (571, 576)], "#fef8e5"),
          feuille(343, 541, 0.7, COULEURS[0], -35))
    for j, couleur in enumerate(("#8c7daf", "#529c91", "#db9a4b")):
        S.add(rect(366 - j * 8, 523 - j * 31, 181, 29, couleur, rx=6),
              rect(388 - j * 8, 526 - j * 31, 158, 22, "#f2e6cd", rx=3))
    S.camera(1.61, 402, 501)
    return S


def p06():
    """Moyen — manteau papier."""
    S = Scene()
    piece(S, "chaumiere", 546)
    S.add(personne(275, 630, 1.34, regard=(1, 0.7), bras="donne", **LEO),
          table(427, 752, 482, 144, "#b08669"),
          tableau(443, 589, 1.18), pot_peinture(600, 582, 0.49, "#f3eee3"))
    return S


def p07():
    """Large — arbre nu."""
    S = parc(nu=True)
    S.add(personne(401, 716, 1.03, regard=(1, -0.42), bras="pousse", **LEO),
          personne(244, 698, 1.02, regard=(1, -0.47), bras="montre", **PAPA))
    return S


def p08():
    """Moyen — souvenir."""
    S = Scene()
    piece(S, "chaumiere", 546)
    x, y = 415, 187
    vue = g([rect(x, y + 155, 251, 116, "#d1c39a"), erable(550, 413, 0.40, True)])
    S.add(fenetre(x, y, 248, 289, "#b4cde4", rideaux="#94b6ad", contenu=vue), tableau(231, 354, 1.18))
    S.add(personne(355, 735, 1.08, regard=(-1, -0.65), **LEO))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-feuille-rouge.svg", p01),
    ("02-collection.svg", p02),
    ("03-branche-trop-haute.svg", p03),
    ("04-pluie-rousse.svg", p04),
    ("05-sous-les-livres.svg", p05),
    ("06-manteau-papier.svg", p06),
    ("07-arbre-nu.svg", p07),
    ("08-souvenir.svg", p08),
]
