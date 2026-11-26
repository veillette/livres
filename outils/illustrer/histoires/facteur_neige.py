"""Le facteur de neige."""
from base import *
from fantastique import personne
from fetes import traces_neige
from objets import barriere

ID = "facteur-neige"
CACHE = "souris"
MALO = dict(peau="claire", cheveux="roux", coiffure="courts", habit="#e1934c", robe=False,
            chaussures="#9b543c", taches=True)
SALOME = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#9b83ca", robe=False,
              chaussures="#624d94", nez="rond")
MAMAN = dict(peau="claire", cheveux="roux", coiffure="chignon", habit="#5ca8ac", robe=False,
             stature="adulte", carrure="fine")


def bonnet(couleur):
    return g([chemin("M -59 -179 Q -60 -238 0 -239 Q 54 -235 58 -178 Z", volume(couleur, 0.27, 0.73)),
              chemin("M -58 -181 Q 0 -191 59 -181", stroke=eclaircir(couleur, 0.35), sw=15),
              cercle(0, -240, 16, eclaircir(couleur, 0.23))])


def enfant(x, y, s, style, **pose):
    return personne(x, y, s, coiffe=bonnet(style["chaussures"]), **style, **pose)


def jardin():
    S = Scene()
    ciel(S, "#8eb4df", "#f4f2f7")
    S.add(nuage(181, 136, 1.16, "#f0eef8"), nuage(629, 199, 1.07, "#f6f2fb"))
    collines(S, 468, "#cfdbf2", graine=24, bosquets=False)
    sol(S, 532, "#e6edf9", couleur2="#d8e5f7", y2=704)
    S.add(sapin(62, 533, 0.61, "#6f9a9d", "#93b7bb", neige=True), sapin(734, 550, 0.75, "#6f999d", "#85adb2", neige=True),
          maison(179, 520, 1.04, "#f0cbab", "#b47674", lumiere=True),
          maison(619, 532, 1.12, "#cfcde9", "#7586ab", lumiere=True),
          chemin("M 106 395 q 70 -35 147 1 M 535 395 q 85 -47 156 7", stroke="#fafaff", sw=11))
    S.ambiance("jour")
    return S


def cloture(S, ouverte=False):
    S.add(barriere(178, 610, 0.94, "#bda4a0", largeur=350),
          barriere(634, 610, 0.94, "#bda4a0", largeur=350))
    if ouverte:
        S.add(barriere(375, 588, 0.62, "#bda4a0", largeur=103))
    else:
        S.add(barriere(405, 614, 0.96, "#a38e9f", largeur=126))


def coeur_pas(x, y, s=1, frais=True):
    points = []
    for j in range(32):
        a = 2 * math.pi * j / 32
        dx = 16 * math.sin(a) ** 3
        dy = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
        points.append((x + dx * 6.5 * s, y - dy * 3.8 * s))
    return g(traces_neige(points, 1.08 * s), opacity=1 if frais else 0.44)


def visage_pas(x, y, s=1, frais=True):
    pts = [(x + 92 * s * math.cos(j * math.tau / 25),
            y + 49 * s * math.sin(j * math.tau / 25)) for j in range(25)]
    pts += [(x - 24 * s, y - 7 * s), (x + 22 * s, y - 7 * s)]
    pts += [(x + dx * s, y + (26 - dx * dx / 135) * s) for dx in (-39, -25, -11, 3, 17, 31, 43)]
    return g(traces_neige(pts, 1.06 * s), opacity=1 if frais else 0.46)


def etoile_pas(x, y, s=1):
    pts = []
    for j in range(5):
        a = math.tau * j / 5 - math.pi / 2
        for k in range(1, 8):
            r = (k * 18 + 12) * s
            pts.append((x + r * math.cos(a) + (4 * k if j == 2 else 0),
                        y + r * math.sin(a) * 0.46))
    return traces_neige(pts, 1.42 * s)


def couverture():
    S = jardin()
    cloture(S, True)
    S.add(enfant(251, 707, 1.22, MALO, bras="salut", regard=(1, 0)),
          enfant(566, 709, 1.19, SALOME, bras="coucou", regard=(-1, 0), flip=True),
          etoile_pas(408, 704, 1.04))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(207, 217, 171, 36, "#dce9fb"),
          traces_neige([(173, 211), (225, 225)], 3.1),
          place([rect(-83, -48, 166, 96, "#9ab9ed", rx=9),
                 chemin("M -80 -41 L 0 13 L 80 -41 M -80 42 L -25 -5 M 80 42 L 26 -5",
                        stroke="#4c72ac", sw=5)], 196, 133, 1.1, rot=-9))
    return S


def p01():
    """Moyen — jour blanc."""
    S = Scene()
    piece(S, "chambre", 579)
    vue = g([rect(285, 341, 416, 151, "#e0ebfb"), maison(602, 393, 0.88, "#d4cfe9", "#8292b3"),
             enfant(607, 357, 0.28, SALOME, bras="haut"),
             barriere(475, 445, 0.64, "#b39fac", largeur=600)])
    S.add(fenetre(303, 158, 375, 309, "#b1cbef", rideaux="#a7b8de", contenu=vue),
          personne(263, 694, 1.32, regard=(1, -0.55), bras="salut", **MALO))
    return S


def p02():
    """Large — pas a pas."""
    S = jardin()
    cloture(S)
    S.add(traces_neige([(198 + 12 * k, 535 + 16 * k) for k in range(11)], 1.28),
          enfant(345, 719, 1.22, MALO, bras="marche", regard=(-1, 0.4)))
    return S


def p03():
    """Gros plan — coeur."""
    S = jardin()
    cloture(S)
    S.add(coeur_pas(377, 688, 1.13), enfant(409, 625, 0.98, MALO, regard=(1, 0.15)))
    S.camera(1.57, 383, 567)
    return S


def p04():
    """Large — reponse ronde."""
    S = jardin()
    cloture(S)
    S.add(visage_pas(601, 672), enfant(641, 628, 1.1, SALOME, regard=(-1, 0.28), bras="saute"),
          enfant(272, 678, 0.95, MALO, regard=(1, 0), bras="salut"), coeur_pas(280, 737, 0.72))
    return S


def p05():
    """Moyen — neige sur neige."""
    S = jardin()
    cloture(S)
    S.add(coeur_pas(247, 712, 1, False), visage_pas(598, 701, 1, False),
          enfant(319, 670, 1.08, MALO, regard=(1, 0), expr="inquiet"),
          enfant(507, 670, 1.09, SALOME, regard=(-1, 0)))
    flocons(S, 86, couleur="#fff")
    return S


def p06():
    """Large — portillon."""
    S = jardin()
    cloture(S, True)
    S.add(personne(369, 630, 1.06, regard=(1, 0.32), bras="donne", coiffe=bonnet("#438286"), **MAMAN),
          enfant(257, 700, 1.17, MALO, regard=(1, 0), bras="designe"),
          enfant(538, 689, 1.17, SALOME, regard=(-1, 0), bras="main", flip=True))
    return S


def p07():
    """Gros plan — etoile."""
    S = jardin()
    S.add(etoile_pas(403, 684, 1.2),
          enfant(270, 668, 1.10, MALO, bras="equilibre", regard=(1, 0.4)),
          enfant(554, 670, 1.10, SALOME, bras="equilibre", regard=(-1, 0.4)))
    S.camera(1.58, 415, 589)
    S.cachette(629, 738)
    return S


def p08():
    """Large — pour demain."""
    S = jardin()
    cloture(S, True)
    S.add(personne(381, 628, 1.07, regard=(0, 0.57), coiffe=bonnet("#438286"), **MAMAN),
          enfant(226, 655, 1.05, MALO, regard=(1, 0.42), bras="designe"),
          enfant(539, 654, 1.06, SALOME, regard=(-1, 0.42)),
          etoile_pas(404, 701, 1.22))
    flocons(S, 64, graine=22, couleur="#fff")
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-jour-blanc.svg", p01),
    ("02-pas-a-pas.svg", p02),
    ("03-coeur.svg", p03),
    ("04-reponse-ronde.svg", p04),
    ("05-neige-sur-neige.svg", p05),
    ("06-portillon.svg", p06),
    ("07-etoile.svg", p07),
    ("08-pour-demain.svg", p08),
]
