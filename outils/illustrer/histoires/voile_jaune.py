"""La voile jaune."""
from base import *
from animaux import roseau
from fantastique import mains_personne, personne

ID = "voile-jaune"
MILO = dict(peau="doree", cheveux="brun", coiffure="herisses", habit="#3daed5", robe=False, taches=True)
ZOE = dict(peau="brune", cheveux="noir", coiffure="afro", habit="#ffca47", carrure="fine")
NORA = dict(peau="brune", cheveux="noir", coiffure="chignon", habit="#a47fbb", stature="adulte", nez="long")
BLEU = "#4c6ef5"
JAUNE = "#ffca32"


def parc():
    S = Scene()
    paysage(S, 445, 540, haut="#75cfef", herbe_="#a3d397", colline="#b7e0a5", graine=34,
            nuages=((210, 143, 0.9), (588, 104, 0.62)))
    S.add(arbre(606, 513, 0.65, "#6dbf82", "#4ba965"),
          arbre(716, 518, 0.46, "#84c98b", "#63af6f"),
          ellipse(392, 556, 357, 155, "#d4cbad"),
          ellipse(392, 557, 336, 139, lineaire([(0, "#58afc7"), (1, "#a8e5e5")])))
    for x, y, w in ((178, 488, 61), (345, 447, 53), (501, 473, 88), (579, 565, 116),
                    (294, 605, 95), (416, 645, 109), (144, 571, 43), (619, 605, 47)):
        S.add(chemin(f"M {x} {y} q {w / 2} -8 {w} 0", stroke="#def6ec", sw=3.2, opacity=0.68))
    for x, y, rot in ((657, 566, -20), (686, 551, 7), (709, 562, 19), (726, 548, 32)):
        S.add(roseau(x, y, 0.65, h=150, rot=rot))
    for x, y, taille in ((114, 613, 0.42), (147, 630, 0.59), (171, 647, 0.38)):
        S.add(caillou(x, y, taille, "#b6b4a4"))
    repoussoir(S, "droite", "#559857", graine=4)
    return S


def voilier(x, y, s=1, couleur=JAUNE, rot=0, dans_eau=True):
    m = []
    if dans_eau:
        m += [ellipse(0, 2, 70, 11, "#277987", opacity=0.24),
              chemin("M -65 13 Q 8 25 67 11", stroke="#e0fcfc", sw=2, opacity=0.82)]
    m += [chemin("M -57 -18 L 58 -22 L 39 -1 Q -7 8 -41 -3 Z", "#a67042", stroke="#785030", sw=2),
          trait(-6, -23, -7, -105, "#785030", 4),
          chemin("M -6 -101 Q 5 -80 41 -32 Q 12 -36 -6 -31 Z", couleur, stroke="#ffffff", sw=2.5),
          chemin("M -14 -82 L -45 -34 L -14 -30 Z", "#faf4db", stroke="#ffffff", sw=2)]
    return place(m, x, y, s, rot=rot)


def couverture():
    S = parc()
    S.add(personne(236, 723, 1.35, regard=(1, 0.2), bras="designe", **MILO),
          personne(555, 720, 1.38, regard=(-1, 0.1), flip=True, bras="designe", **ZOE),
          voilier(339, 566, 0.94, BLEU), voilier(478, 612, 1.20))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 202, 174, 42, "#b0e7e7"),
          voilier(145, 194, 1.13), voilier(264, 219, 0.91, BLEU))
    return S


def p01():
    """Large — en course."""
    S = parc()
    S.add(personne(169, 715, 0.98, regard=(1, 0.3), **NORA),
          personne(333, 730, 1.0, regard=(1, 0.3), bras="ramasse", **MILO),
          personne(537, 730, 1.02, regard=(-1, 0.3), bras="ramasse", **ZOE),
          voilier(275, 649, 0.67, BLEU), voilier(477, 673, 0.68))
    return S


def p02():
    """Moyen — lentement."""
    S = parc()
    S.add(personne(397, 727, 1.29, regard=(0, -0.3), bras="donne", flip=True, **MILO),
          personne(596, 708, 1.29, regard=(-1, 0.2), bras="ramasse", **ZOE),
          voilier(270, 550, 0.98, BLEU), voilier(486, 640, 0.98, rot=7))
    return S


def p03():
    """Gros plan — roseaux."""
    S = parc()
    S.add(voilier(641, 553, 1.0, rot=27),
          roseau(685, 583, 0.53, h=137, rot=28), roseau(710, 566, 0.62, h=155, rot=19))
    S.camera(1.97, 591, 510)
    S.cachette(742, 641)
    return S


def p04():
    """Moyen — branche."""
    S = parc()
    S.add(personne(429, 703, 1.24, regard=(1, 0.3), bras="donne", **NORA),
          personne(239, 716, 1.19, regard=(1, 0.2), **ZOE))
    _, (mx, my) = mains_personne(429, 703, 1.24, bras="donne", stature="adulte")
    S.add(chemin(f"M {mx} {my} Q 601 576 660 576 L 646 550", stroke="#886849", sw=7),
          voilier(649, 560, 0.76, rot=14),
          ellipse(687, 439, 15, 4, "#d1f4ee", rot=-26),
          ellipse(707, 439, 15, 4, "#d1f4ee", rot=26),
          trait(698, 432, 696, 462, "#437b89", 4))
    return S


def p05():
    """Moyen — escale."""
    S = parc()
    S.add(personne(218, 700, 1.26, regard=(1, -0.13), bras="designe", **ZOE),
          voilier(343, 607, 0.94))
    return S


def p06():
    """Large — retour bleu."""
    S = parc()
    S.add(personne(345, 420, 0.94, regard=(0, 0.6), bras="ramasse", **MILO),
          voilier(408, 466, 0.65, BLEU),
          personne(557, 710, 0.92, regard=(-1, -0.7), **ZOE), voilier(474, 633, 0.66))
    return S


def p07():
    """Gros plan — cote a cote."""
    S = parc()
    S.add(voilier(326, 588, 1.33, BLEU, rot=3), voilier(490, 548, 1.44, rot=-6))
    S.camera(1.58, 406, 519)
    S.cachette(597, 690, "air")
    return S


def p08():
    """Large — port."""
    S = parc()
    S.add(personne(212, 680, 1.08, regard=(1, 0.3), **NORA),
          personne(399, 725, 1.07, regard=(1, 0.3), **MILO),
          personne(577, 720, 1.06, regard=(-1, 0.2), expr="rire", **ZOE),
          voilier(336, 760, 0.78, BLEU, dans_eau=False), voilier(494, 767, 0.82, dans_eau=False))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-en-course.svg", p01),
    ("02-lentement.svg", p02),
    ("03-roseaux.svg", p03),
    ("04-branche.svg", p04),
    ("05-escale.svg", p05),
    ("06-retour-bleu.svg", p06),
    ("07-cote-a-cote.svg", p07),
    ("08-port.svg", p08),
]
