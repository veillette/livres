"""Les pommes de travers."""
from base import *
from fantastique import mains_personne, personne
from fetes import panier_osier
from objets import bol, pomme

ID = "pommes-de-travers"
NORA = dict(peau="doree", cheveux="brun", coiffure="couettes", habit="#b279c6", stature="petit")
PAPI = dict(peau="doree", cheveux="blanc", coiffure="boucles", habit="#6c9884",
            stature="ancien", robe=False, carrure="ronde", nez="rond", acc=("lunettes",))


def pomme_bossee(x, y, s=1, couleur="#eeb747", rot=0):
    return place([chemin("M 0 -40 C -32 -64 -61 -46 -62 -17 C -67 3 -47 31 -23 31 "
                         "C -7 42 15 33 20 23 C 38 22 48 2 32 -10 C 39 -34 20 -58 0 -40 Z",
                         volume(couleur, 0.29, 0.75), stroke="#b67738", sw=2),
                  chemin("M 1 -42 Q -4 -58 6 -67", stroke="#744430", sw=5),
                  ellipse(17, -56, 20, 7, "#779952", rot=-26),
                  ellipse(-35, -26, 13, 6, "#fff5c3", opacity=0.62, rot=-42)], x, y, s, rot=rot)


def verger():
    S = Scene()
    paysage(S, 509, 578, herbe_="#bfc894", colline="#dfce9c", haut="#91bcd6", bas="#fff1cd", graine=28)
    S.add(arbre(135, 563, 0.96, "#afae66", "#8f9d54", fruits="#d66c47"),
          arbre(421, 533, 0.72, "#aab469", "#819b59", fruits="#b96558"),
          arbre(694, 630, 1.45, "#bdba75", "#94a165", fruits="#d46a55"),
          chemin("M 79 800 Q 203 617 474 577 L 502 578 Q 265 649 248 800 Z", "#d3ba97"))
    for x, y in ((104, 712), (682, 692), (596, 751), (176, 585)):
        S.add(feuille_sol(x, y))
    return S


def feuille_sol(x, y):
    return place(chemin("M -19 4 Q -9 -17 24 -9 Q 13 10 -19 4 Z", "#be7748"), x, y)


def panier(x, y, s=1, fruits=""):
    m = [panier_osier(0, 0, couleur="#c59a68")]
    for j, px in enumerate((-49, -32, -14, 7, 29, 48)):
        if fruits == "rondes":
            m.append(pomme(px, -60 - (j % 2) * 8, 0.48))
        if fruits == "bossees":
            m.append(pomme_bossee(px, -65 - j * 19 % 23, 0.31, rot=j * 28 - 42))
    return place(m, x, y, s)


def avec_pomme(S, x, y, s, style, bossee, regard):
    S.add(personne(x, y, s, regard=regard, bras="donne", **style))
    _, (mx, my) = mains_personne(x, y, s, bras="donne", stature=style["stature"],
                                 carrure=style.get("carrure", "normale"))
    if bossee:
        S.add(pomme_bossee(mx, my - 23 * s, 0.57 * s))
    else:
        S.add(pomme(mx, my - 13 * s, 0.81 * s))


def couverture():
    S = verger()
    avec_pomme(S, 235, 719, 1.42, NORA, False, (1, -0.33))
    avec_pomme(S, 477, 705, 1.38, PAPI, True, (-1, 0.55))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pomme(121, 163, 2.1), pomme_bossee(268, 152, 1.32, rot=-17))
    return S


def p01():
    """Large — verger."""
    S = verger()
    S.add(personne(313, 663, 1.12, regard=(1, -0.35), bras="porte", **NORA),
          personne(485, 659, 1.11, regard=(1, -0.2), bras="porte", **PAPI),
          panier(313, 674, 0.76), panier(485, 687, 1))
    return S


def p02():
    """Moyen — celle ci."""
    S = verger()
    S.add(personne(277, 720, 1.38, regard=(1, -0.2), expr="rire", **NORA))
    avec_pomme(S, 479, 707, 1.39, PAPI, True, (-1, 0.5))
    return S


def p03():
    """Gros plan — pomme a nez."""
    S = verger()
    S.add(chemin("M 500 572 Q 523 555 561 573 L 630 623 L 611 649 L 529 610 Q 505 605 491 586 Z",
                 "#b279c6", stroke="#79608c", sw=3),
          ellipse(496, 568, 22, 19, "#dca36f", rot=30, stroke="#865941", stroke_width=3),
          pomme(340, 538, 1.59), pomme_bossee(483, 520, 1.14, rot=138),
          ellipse(511, 556, 9, 15, "#dca36f", rot=45, stroke="#9c684a", stroke_width=2))
    for x, y in ((278, 565), (427, 587), (521, 584), (557, 510)):
        S.add(feuille_sol(x, y))
    S.camera(1.9, 404, 521)
    return S


def p04():
    """Large — deux paniers."""
    S = verger()
    S.add(personne(217, 658, 1.04, regard=(1, 0.65), **NORA),
          panier(353, 715, 1.22, "rondes"), panier(532, 721, 1.52, "bossees"))
    return S


def cuisine():
    S = Scene()
    piece(S, "cuisine", 567)
    S.add(fenetre(531, 142, 189, 174, "#accee1", rideaux="#b0a0ca",
                  contenu=arbre(666, 322, 0.62, "#a9ad6c", "#959d54", fruits="#d76247")))
    return S


def p05():
    """Moyen — sur la planche."""
    S = cuisine()
    S.add(personne(265, 640, 1.36, regard=(1, 0.68), bras="ramasse", **PAPI),
          personne(497, 634, 1.4, regard=(-1, 0.5), **NORA),
          table(403, 770, 497, 172, "#ab805e"),
          rect(281, 540, 206, 47, "#f1cea0", rx=13))
    for j in range(7):
        x, y = 297 + j * 24, 559 - j * 13 % 17
        S.add(chemin(f"M {x} {y} l 14 -8 l 12 14 l -20 7 Z", "#fff3cc", stroke="#e3b25b", sw=2.4))
    S.add(rect(265, 536, 53, 8, "#6d5264", rx=3), poly([(315, 536), (369, 541), (319, 552)], "#adb5bd"))
    return S


def p06():
    """Moyen — casserole."""
    S = cuisine()
    S.add(personne(276, 689, 1.21, regard=(1, 0.16), bras="donne", **PAPI),
          personne(615, 680, 1.15, regard=(-1, 0.1), **NORA),
          rect(361, 567, 172, 164, "#c3c7d0", rx=9),
          rect(374, 606, 145, 99, "#8892a2", rx=8),
          rect(375, 621, 140, 14, "#e9e8ee", rx=4),
          rect(390, 554, 105, 17, "#646575", rx=4),
          chemin("M 389 508 L 400 550 Q 437 567 483 549 L 497 508 Z", "#917dab"),
          ellipse(443, 508, 54, 15, "#cbb0d6"),
          ellipse(443, 510, 45, 10, "#f0c36d"),
          trait(457, 509, 431, 450, "#946c50", 8))
    for x in (422, 444, 464):
        S.add(chemin(f"M {x} 485 q -26 -23 3 -43 t 6 -34", stroke="#fff", sw=5, opacity=0.8))
    return S


def p07():
    """Gros plan — degustation."""
    S = cuisine()
    S.add(personne(267, 673, 1.37, regard=(1, 0.35), **PAPI),
          personne(515, 648, 1.40, regard=(-1, 0.5), expr="miam", **NORA),
          table(394, 773, 498, 161, "#ab805e"),
          bol(329, 590, 1, "#b39bc6", "#edbd66"), bol(473, 591, 1, "#78bbac", "#edbd66"))
    S.camera(1.42, 410, 501)
    return S


def p08():
    """Large — prochain panier."""
    S = verger()
    S.add(personne(299, 684, 1.06, regard=(1, 0.2), bras="porte", **NORA),
          personne(481, 662, 1.1, regard=(-1, 0.4), bras="marche", **PAPI),
          panier(307, 694, 1.13))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-verger.svg", p01),
    ("02-celle-ci.svg", p02),
    ("03-pomme-a-nez.svg", p03),
    ("04-deux-paniers.svg", p04),
    ("05-sur-la-planche.svg", p05),
    ("06-casserole.svg", p06),
    ("07-degustation.svg", p07),
    ("08-prochain-panier.svg", p08),
]
