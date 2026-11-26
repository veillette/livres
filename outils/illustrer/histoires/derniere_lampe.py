"""La dernière lampe du jardin."""
from base import *
from fantastique import luciole, mains_personne, personne, personne_assise
from objets import lampe_poche

ID = "derniere-lampe"
AICHA = dict(peau="foncee", cheveux="noir", coiffure="tresses", habit="#cf82c1", robe=False)
IDRIS = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#f4bd55", robe=False, stature="petit", nez="rond")
PAPA = dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#428f89", stature="adulte", robe=False,
            carrure="ronde", barbe="#2b2b3a")


def jardin(soir=False, porche=False, allume=False):
    S = Scene()
    if soir:
        ciel(S, "#cc84a4", "#ffe09e")
        S.ambiance("soir")
    else:
        nuit(S, "#202c59", "#536097")
        S.add(lune(610, 173, 34, croissant=True))
    collines(S, 491, "#7779a8" if soir else "#364469", graine=14)
    sol(S, 566, "#688c72" if soir else "#344e58")
    S.add(chemin("M 110 560 Q 296 581 450 800 H 322 Q 231 624 84 591 Z", "#a69a8a" if soir else "#535a71"),
          arbre(726, 580, 1.07, "#405e69", "#314d5e"))
    if porche:
        S.add(maison(145, 585, 1.41, "#b39196", "#4d4164", lumiere=False))
        S.add(rect(120, 438, 56, 119, "#50445e", rx=7), trait(112, 556, 186, 556, "#d0b1a4", 7))
        S.add(rect(184, 420, 22, 31, "#ffdf9b" if allume else "#4d4c68", rx=5, stroke="#4d465b", stroke_width=3))
        if allume:
            S.lumiere(195, 437, 147, "#ffd090", 0.66)
            S.lumiere(156, 579, 126, "#ffc982", 0.44, ry=50)
    repoussoir(S, "droite", "#486568", graine=25)
    return S


def banc(S):
    S.add(rect(152, 547, 449, 27, "#947c75", rx=6),
          rect(166, 571, 14, 98, "#514c60", rx=3), rect(573, 571, 14, 98, "#514c60", rx=3),
          rect(150, 603, 453, 17, "#aa826a", rx=4))


def enfants(S, lampe=False, eteinte=False, assis=False):
    if assis:
        S.add(personne_assise(349, 608, 1.2, regard=(1, 0.38), bras="donne", **AICHA),
              personne_assise(507, 608, 1.19, regard=(-1, 0.15), bras="main", flip=True, **IDRIS))
    else:
        S.add(personne(345, 651, 1.2, regard=(1, 0.38), bras="donne", **AICHA),
              personne(521, 649, 1.19, regard=(-1, 0.15), bras="main", flip=True, **IDRIS))
    if lampe or eteinte:
        x, y = (450, 555) if assis else mains_personne(345, 651, 1.2, bras="donne")[1]
        S.add(lampe_poche(x, y, 0.6, rot=48 if lampe else 13, faisceau=163 if lampe else 0))
        if lampe:
            S.lumiere(506, 677, 98, "#ffe2a3", 0.49, ry=47)


def lucioles(S):
    for x, y, taille in ((458, 715, 0.4), (622, 573, 0.47), (672, 681, 0.36)):
        S.add(luciole(x, y, taille))


def couverture():
    S = jardin()
    banc(S)
    enfants(S)
    lucioles(S)
    return S


def vignette():
    S = Scene(400, 270)
    fond(S, "#354167")
    S.ambiance("nuit")
    S.add(luciole(206, 136, 1.45), cercle(99, 89, 6, "#fff3bf"), cercle(310, 180, 8, "#ffe590"))
    S.lumiere(99, 89, 38, "#ffefaf", 0.55)
    S.lumiere(310, 180, 50, "#ffe590", 0.57)
    return S


def p01():
    """Large — avant la nuit."""
    S = jardin(soir=True, porche=True)
    S.add(personne(340, 664, 1.04, regard=(1, 0.12), bras="designe", **AICHA),
          personne(497, 677, 1.03, regard=(1, 0.15), **IDRIS))
    return S


def p02():
    """Gros plan — lampe."""
    S = jardin(porche=True, allume=True)
    enfants(S, lampe=True)
    S.add(caillou(488, 690, 0.4, "#e0c9a2"))
    S.camera(1.6, 454, 562)
    S.cachette(583, 713)
    return S


def p03():
    """Large — porche."""
    S = jardin(porche=True)
    banc(S)
    S.add(personne_assise(213, 609, 1.05, regard=(1, 0.3), bras="donne", **PAPA))
    enfants(S, lampe=True, assis=True)
    return S


def p04():
    """Moyen — noir doux."""
    S = jardin()
    banc(S)
    enfants(S, eteinte=True, assis=True)
    return S


def p05():
    """Gros plan — premier eclat."""
    S = jardin()
    S.add(personne(381, 667, 1.49, regard=(1, 0.12), expr="surpris", **IDRIS),
          luciole(538, 501, 0.43))
    for x, y in ((549, 647), (618, 638), (643, 674)):
        S.add(touffe(x, y, 0.89, "#62907a"))
    S.camera(1.65, 435, 497)
    S.cachette(651, 663)
    return S


def p06():
    """Large — trois lumieres."""
    S = jardin()
    banc(S)
    S.add(personne_assise(213, 609, 1.05, regard=(1, 0.3), bras="porte", **PAPA))
    enfants(S, assis=True)
    lucioles(S)
    return S


def p07():
    """Gros plan — main ouverte."""
    S = jardin()
    S.add(personne(379, 657, 1.58, regard=(1, -0.35), bras="donne", **IDRIS))
    _, (mx, my) = mains_personne(379, 657, 1.58, bras="donne", stature="petit")
    S.add(place(chemin("M -12 7 Q -7 -1 -5 -9 Q -4 -16 1 -15 Q 5 -15 3 -5 "
                      "Q 11 -14 21 -14 Q 26 -13 23 -9 L 11 -2 Q 28 -10 29 -4 "
                      "Q 30 -2 16 3 Q 26 1 27 5 Q 25 9 9 12 Q -1 19 -12 7 Z",
                      "#825433", stroke="#412f38", sw=2), mx + 6, my - 1),
          luciole(553, 489, 0.60, flip=True))
    S.camera(1.75, 474, 498)
    S.cachette(665, 653)
    return S


def p08():
    """Moyen — bonne nuit."""
    S = jardin(porche=True, allume=True)
    S.add(personne(180, 588, 1.05, regard=(1, 0.15), **PAPA),
          personne(326, 628, 1.15, regard=(1, 0.2), bras="salut", **AICHA),
          personne(477, 647, 1.13, regard=(1, 0.15), bras="coucou", **IDRIS))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-avant-la-nuit.svg", p01),
    ("02-lampe.svg", p02),
    ("03-porche.svg", p03),
    ("04-noir-doux.svg", p04),
    ("05-premier-eclat.svg", p05),
    ("06-trois-lumieres.svg", p06),
    ("07-main-ouverte.svg", p07),
    ("08-bonne-nuit.svg", p08),
]
