"""La botte aux capucines."""
from base import *
from fantastique import personne

ID = "botte-capucines"
ALMA = dict(peau="brune", coiffure="couettes", habit="#748ffc", chaussures="#4263eb", taches=True)
MAMIE = dict(stature="ancien", coiffure="chignon", cheveux="#ced4da", habit="#74b816", nez="rond")


def jardin(S):
    paysage(S, 480, 555, herbe_="#a9e38a", colline="#d2ecae", graine=16,
            haut="#91d5fc", nuages=((590, 138, 1),))
    S.add(maison(149, 530, 1, mur="#fff3bf", toit="#5c9471"))
    S.add(chemin("M 130 515 Q 250 559 44 800 H 295 Q 345 597 157 515 Z", "#dfc4a3"))
    S.add(chemin("M 610 525 Q 670 659 800 709 V 478 Z", "#a47755"))
    for k in range(5):
        S.add(fleur(666 + k * 29, 504 + k * 14, 0.46, "#f783ac", tige=32))
    repoussoir(S, "droite", "#3c8a55", graine=7)


def botte(x, y, s=1, pousse=0, fleurie=False):
    m = [ellipse(4, 0, 81, 12, "#704025", opacity=0.17),
         chemin("M -48 -105 H 31 L 35 -51 Q 35 -40 66 -40 Q 91 -40 92 -13 Q 89 0 64 0 H -47 Q -56 0 -54 -14 Z",
                volume("#ffd43b", 0.34, 0.81), stroke="#b47714", sw=3),
         chemin("M -53 -10 Q 19 -4 91 -13 L 88 -2 Q 52 8 -49 4 Z", "#cf870c"),
         ellipse(-8, -105, 41, 12, "#e6a318", stroke="#ffe066", stroke_width=5),
         ellipse(-8, -104, 33, 7, "#7b543d"),
         chemin("M -41 -90 L -43 -38 M 47 -32 Q 77 -33 80 -24", stroke="#ffed91", sw=4)]
    if pousse:
        feuilles = [(-28, -155), (14, -161), (56, -127), (68, -82), (-59, -133)]
        for px, py in feuilles[:2 if pousse == 1 else len(feuilles)]:
            m += [chemin(f"M -8 -106 Q 10 -139 {px} {py}", stroke="#467d37", sw=3),
                  ellipse(px, py, 17 if pousse == 1 else 22, 14, "#69b649", rot=px / 3),
                  trait(px - 9, py + 1, px + 8, py - 2, "#bad974", 2)]
    if fleurie:
        for px, py, taille in [(-29, -176, 0.85), (24, -152, 0.65), (66, -108, 0.55)]:
            m.append(fleur(px, py + 27 * taille, taille, "#ff8a29", "#da481c", tige=27))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    jardin(S)
    S.add(personne(235, 672, 1.32, regard=(1, 0.6), bras="ramasse", **ALMA),
          personne(594, 650, 1.28, regard=(-1, 0.6), bras="designe", **MAMIE),
          botte(404, 749, 1.72, 2, True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(botte(183, 250, 1.25, 2, True))
    return S


def p01():
    """Large — trop petite."""
    S = Scene()
    jardin(S)
    S.add(personne(335, 655, 1.08, regard=(1, 0.8), expr="surpris", **ALMA), botte(482, 687, 0.84))
    return S


def p02():
    """Moyen — idee mamie."""
    S = Scene()
    jardin(S)
    S.add(personne(305, 720, 1.43, regard=(1, -0.4), **ALMA),
          personne(551, 712, 1.48, regard=(-1, 0.4), bras="donne", **MAMIE),
          rect(447, 614, 48, 62, "#fff3bf", rx=4),
          fleur(471, 665, 0.33, "#ff922b", tige=56))
    return S


def p03():
    """Gros plan — terre et graine."""
    S = Scene()
    jardin(S)
    S.add(personne(290, 712, 1.05, regard=(1, 1), bras="ramasse", **ALMA), botte(469, 714, 1.16))
    for x, y in ((444, 559), (465, 573)):
        S.add(ellipse(x, y, 8, 6, "#e8c793", stroke="#9c7c52", stroke_width=2))
    S.camera(1.7, 438, 544)
    return S


def p04():
    """Large — pluie."""
    S = Scene()
    piece(S, "cuisine", 592)
    dehors = Scene()
    dehors.add(chemin("M 200 403 Q 425 325 650 382 V 500 H 200 Z", "#a2c990"),
               botte(533, 460, 0.74))
    pluie(dehors, nb=65, zone=(207, 138, 647, 496), couleur="#edf5ff")
    S.add(fenetre(207, 138, 440, 358, "#a5b9d1", rideaux="#ffec99", contenu=g(dehors.els)),
          personne(336, 692, 1.32, regard=(1, -0.6), bras="designe", **ALMA))
    return S


def p05():
    """Moyen — deux feuilles."""
    S = Scene()
    jardin(S)
    S.add(personne(324, 712, 1.45, regard=(1, 0.3), expr="surpris", bras="joues", **ALMA),
          botte(510, 718, 1.43, 1))
    return S


def p06():
    """Moyen — le long."""
    S = Scene()
    jardin(S)
    S.add(botte(470, 697, 1.63, 2), personne(266, 699, 1.08, regard=(1, 0.5), **ALMA))
    return S


def p07():
    """Gros plan — fleur orange."""
    S = Scene()
    jardin(S)
    S.add(botte(463, 736, 1.82, 2, True), personne(253, 718, 1.21, regard=(1, 0.2), **ALMA))
    S.camera(1.65, 438, 529)
    return S


def p08():
    """Large — paire."""
    S = Scene()
    jardin(S)
    S.add(personne(351, 704, 1.37, expr="rire", bras="designe", regard=(1, 0.6), **ALMA),
          personne(216, 651, 1.12, regard=(1, 0.2), **MAMIE), botte(541, 730, 1.26, 2, True))
    for x in (328, 371):
        S.add(rect(x - 14, 673, 23, 24, "#4263eb", rx=4),
              rect(x - 15, 672, 25, 6, "#91a7ff", rx=2),
              ellipse(x + 8, 697, 17, 7, "#4263eb"))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-trop-petite.svg", p01),
    ("02-idee-mamie.svg", p02),
    ("03-terre-et-graine.svg", p03),
    ("04-pluie.svg", p04),
    ("05-deux-feuilles.svg", p05),
    ("06-le-long.svg", p06),
    ("07-fleur-orange.svg", p07),
    ("08-paire.svg", p08),
]
