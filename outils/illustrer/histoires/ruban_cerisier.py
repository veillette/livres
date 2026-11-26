"""Le ruban du cerisier."""
from base import *
from fantastique import mains_personne, personne, personne_assise
from objets import bocal, pinceau

ID = "ruban-cerisier"
INES = dict(peau="doree", coiffure="carre", habit="#339c95", nez="retrousse", acc=("noeud",))
PAPI = dict(stature="ancien", coiffure="chauve_cote", cheveux="#e9ecef", habit="#9775bc",
            robe=False, carrure="ronde", acc=("lunettes",))
ROSE = "#e66b97"
BOIS = "#785568"


def ruban(x, y, s=1):
    return place([chemin("M -5 0 C -74 -58 -76 21 -7 6 C 73 -61 75 11 4 8", stroke=ROSE, sw=13),
                  chemin("M -3 6 Q -37 19 -42 55 M 6 6 Q 40 24 32 62", stroke=ROSE, sw=12),
                  ellipse(0, 7, 12, 8, "#f087ae")], x, y, s)


def cerisier(x, y, s=1, floraison=2):
    m = [chemin("M -41 0 Q -7 -110 -28 -216 Q -45 -278 -135 -320 L -126 -338 Q -54 -321 -7 -272 Q 16 -318 -4 -388 L 11 -394 Q 47 -318 30 -267 Q 74 -297 145 -337 L 155 -322 Q 99 -291 55 -235 Q 16 -180 38 0 Z",
                volume(BOIS, 0.35, 0.72))]
    for bx, by in ((-145, -326), (-86, -309), (-30, -360), (7, -395), (48, -317), (92, -318), (151, -336)):
        if floraison == 2:
            m += [ellipse(bx, by, 54, 35, "#f7a8c9", rot=bx / 9), ellipse(bx - 8, by - 14, 39, 27, "#ffe0eb")]
        for k in range(6):
            px, py = bx - 32 + k * 13, by - 11 - (k * 19 % 32)
            if floraison == 2:
                for dx, dy in ((-6, 0), (0, -6), (6, 0), (0, 6)):
                    m.append(cercle(px + dx, py + dy, 7, "#fff0f5"))
                m.append(cercle(px, py, 3, "#ef9ab7"))
            else:
                m += [trait(bx, by, px, py, BOIS, 3),
                      ellipse(px, py, 6, 4, ROSE if floraison == 1 else "#7cbb75", rot=k * 21)]
    return place(m, x, y, s)


def dehors(S, floraison=2):
    paysage(S, 518, 587, herbe_="#add79b", colline="#cfdfb7", graine=11)
    S.add(chemin("M 98 800 Q 187 640 697 510 L 719 514 Q 353 645 320 800 Z", "#e8cfba"),
          cerisier(532, 661, 1.28, floraison))
    repoussoir(S, "droite", "#709c63", graine=6)


def carte(x, y, s=1, nouee=False):
    m = [rect(-102, -65, 204, 130, "#fffbeb", rx=6, stroke="#dbc6a9", stroke_width=3),
         cerisier(-8, 50, 0.24),
         oiseau(22, -29, 0.13, "#393145", "#393145")]
    if nouee:
        m += [trait(-102, -7, 102, -7, ROSE, 10), ruban(4, -9, 0.8)]
    return place(m, x, y, s)


def chambre(S, avec_fauteuil=True):
    piece(S, "chambre", 578)
    vue = chemin("M 386 379 Q 548 330 750 342 L 751 439 H 362 Z", "#bbcc9e")
    vue += chemin("M 432 467 Q 481 389 682 354 L 717 358 Q 563 399 552 467 Z", "#ebd1b9")
    S.add(fenetre(437, 133, 259, 272, "#d5eaff", rideaux="#efb1c7", contenu=vue))
    if avec_fauteuil:
        S.add(rect(131, 363, 240, 272, volume("#c7a0cb", 0.3, 0.72), rx=54),
              rect(108, 549, 284, 91, "#a77ead", rx=28),
              rect(116, 626, 24, 34, BOIS), rect(361, 626, 24, 34, BOIS))


def couverture():
    S = Scene()
    dehors(S)
    S.add(personne(326, 732, 1.5, regard=(1, -0.5), bras="haut", **INES))
    (mx, my), _ = mains_personne(326, 732, 1.5, bras="haut")
    S.add(chemin(f"M {mx} {my} q -16 41 15 69 t -4 58", stroke=ROSE, sw=10),
          chemin(f"M {mx} {my} q 1 -34 42 -51 t 71 5", stroke=ROSE, sw=10))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(carte(189, 124, 1.33), ruban(284, 177, 0.85))
    return S


def p01():
    """Moyen — ruban du tiroir."""
    S = Scene()
    chambre(S)
    S.add(personne_assise(258, 575, 1.17, bras="donne", regard=(1, 0), **PAPI),
          personne(472, 714, 1.24, regard=(-1, -0.3), **INES), ruban(363, 526, 0.64))
    return S


def p02():
    """Large — boutons."""
    S = Scene()
    dehors(S, 1)
    S.add(personne(304, 720, 1.08, regard=(1, -0.7), bras="mains_jointes", **INES))
    return S


def p03():
    """Gros plan — ouverture."""
    S = Scene()
    dehors(S)
    S.add(personne(302, 548, 1.37, regard=(1, -0.5), **INES),
          oiseau(604, 268, 0.48, "#373746", "#373746"))
    S.camera(1.65, 460, 315)
    S.cachette(652, 454, "air")
    return S


def p04():
    """Large — coin de fenetre."""
    S = Scene()
    chambre(S)
    S.add(personne_assise(236, 576, 1.18, regard=(1, -0.3), **PAPI),
          personne(426, 690, 1.23, regard=(1, -0.7), bras="pense", **INES))
    return S


def p05():
    """Moyen — pinceau."""
    S = Scene()
    dehors(S)
    S.add(personne(335, 692, 1.38, regard=(1, 0.8), bras="ramasse", **INES),
          carte(452, 705, 0.65), pinceau(417, 668, 0.85, rot=65), bocal(566, 721, 0.67))
    return S


def p06():
    """Gros plan — noeud."""
    S = Scene()
    chambre(S, False)
    S.add(table(391, 746, 420, 154, "#c79779"),
          carte(394, 549, 1.38, True))
    S.camera(1.72, 397, 555)
    S.cachette(555, 651, "air")
    return S


def p07():
    """Moyen — cerisier de papier."""
    S = Scene()
    chambre(S)
    S.add(personne_assise(254, 577, 1.24, regard=(1, 0.6), bras="porte", **PAPI),
          personne(453, 700, 1.28, regard=(-1, 0.35), expr="rire", **INES),
          carte(274, 558, 0.76))
    return S


def p08():
    """Large — deux cerisiers."""
    S = Scene()
    chambre(S)
    S.add(carte(275, 290, 1.04), ruban(268, 365, 0.7))
    for k in range(12):
        S.add(ellipse(472 + k * 17, 360 + (k * 11 % 37), 7, 4, ROSE, rot=k * 19))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-ruban-du-tiroir.svg", p01),
    ("02-boutons.svg", p02),
    ("03-ouverture.svg", p03),
    ("04-coin-de-fenetre.svg", p04),
    ("05-pinceau.svg", p05),
    ("06-noeud.svg", p06),
    ("07-cerisier-de-papier.svg", p07),
    ("08-deux-cerisiers.svg", p08),
]
