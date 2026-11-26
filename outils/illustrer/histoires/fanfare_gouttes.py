"""La fanfare des gouttes."""
from base import *
from fantastique import mains_personne, personne
from objets import flaque, goutte_simple, grande_feuille

ID = "fanfare-gouttes"
NINO = dict(peau="doree", coiffure="boucles", habit="#37b9a4", robe=False, stature="petit")
LILA = dict(peau="doree", coiffure="tresses", habit="#f7a43b", robe=False, carrure="fine", nez="rond")


def cour(S, quantite=0, porche=True):
    paysage(S, 498, 575, herbe_="#9cca84", colline="#bedaae",
            haut="#9ab4cf" if quantite else "#99cbef", nuages=((626, 198, 1.08),), graine=22)
    S.add(chemin("M 330 572 Q 549 563 715 468 L 742 470 Q 575 600 548 800 H 198 Z", "#c6ad91"))
    for x, y, rot in ((642, 661, 22), (703, 700, 38), (762, 621, 26)):
        S.add(grande_feuille(x, y, 0.62, "#388758", "#a9cc79", rot))
    if porche:
        S.add(rect(0, 135, 497, 454, "#f3d9aa"),
              rect(91, 247, 224, 341, "#7d5952", rx=12),
              rect(108, 266, 190, 320, "#9d7265", rx=6),
              cercle(268, 433, 9, "#ffe8a3"),
              poly([(0, 548), (508, 548), (548, 647), (0, 647)], "#b5a48d"),
              poly([(0, 82), (434, 103), (550, 206), (0, 192)], "#6d7995"),
              chemin("M 0 192 L 550 206 L 552 215 Q 551 222 530 221 L 0 210 Z", "#495469"),
              chemin("M 520 213 L 520 484 Q 520 511 548 510 L 579 510", stroke="#78869c", sw=17))
    if quantite:
        pluie(S, quantite, graine=17, zone=(545 if porche else 0, 120, 800, 785), couleur="#87abc8")
        S.add(flaque(639, 741, 1.13), flaque(754, 585, 0.48))
        S.ambiance("jour")


def recipient(x, y, s=1, c="#4dabf7", eau=False, seau=False):
    h = 95 if seau else 56
    m = [ellipse(0, 0, 65, 11, "#495057", opacity=0.15),
         chemin(f"M -70 {-h} L -55 -11 Q 0 10 55 -11 L 70 {-h} Z", volume(c, 0.29, 0.76)),
         ellipse(0, -h, 70, 22, c, stroke="#d0ebff", stroke_width=4),
         ellipse(0, -h + 4, 59, 15, "#86dbe8" if eau else "#385984")]
    if seau:
        m.append(chemin(f"M -65 {-h + 6} Q -28 47 63 {-h + 6}", stroke="#687d81", sw=4))
    return place(m, x, y, s)


def avec_cuilleres(x, y, s, quantite, style, bras="haut", **pose):
    dessin = personne(x, y, s, bras=bras, **style, **pose)
    mains = mains_personne(x, y, s, bras=bras, stature=style.get("stature", "enfant"),
                           carrure=style.get("carrure", "normale"))
    for k, (mx, my) in enumerate(mains[:quantite]):
        dx = -17 if k == 0 else 22
        dessin += trait(mx, my, mx + dx, my - 34, "#90674c", 5)
        dessin += ellipse(mx + dx, my - 34, 8, 12, "#bd906c", rot=dx)
    return dessin


def ensemble(pluie_, reprise=True):
    S = Scene()
    cour(S, pluie_)
    S.add(recipient(592, 713, 0.78, "#9fb8ba", eau=pluie_ > 0, seau=True))
    if reprise:
        S.add(avec_cuilleres(207, 631, 1.38, 1, NINO, regard=(1, 0.5), bras="donne"),
              avec_cuilleres(408, 613, 1.3, 2, LILA, regard=(-1, 0.4)),
              recipient(288, 665, 1.12, "#3a80c3"))
    return S


def couverture():
    return ensemble(52)


def vignette():
    S = Scene(400, 270)
    S.add(recipient(251, 208, 1.16, "#9fb8ba", True, True),
          recipient(127, 238, 1, "#3a80c3", True),
          ellipse(117, 184, 18, 5, "none", stroke="#efffff", stroke_width=2),
          goutte_simple(249, 51, s=1.15))
    return S


def p01():
    """Moyen — repetition."""
    return ensemble(0)


def p02():
    """Large — averse."""
    S = ensemble(108, reprise=False)
    S.add(personne(157, 596, 1.08, expr="inquiet", regard=(1, 0), **NINO),
          personne(303, 595, 1.08, expr="surpris", regard=(1, 0), **LILA), recipient(372, 643, 0.82))
    return S


def gouttes(derniere=False):
    S = Scene()
    cour(S, 0 if derniere else 77)
    S.add(flaque(645, 740, 1.13))
    S.add(recipient(594, 711, 1.22, "#8aa8b4", derniere, True))
    for rayon in (14, 34, 51):
        S.add(ellipse(597, 600, rayon, rayon * 0.22, "none", stroke="#e3f8ff", stroke_width=2))
    for y in ((566,) if derniere else (530, 563, 582)):
        S.add(goutte_simple(595, y, "#71bcf6", 0.8))
    S.camera(1.92, 590, 593)
    return S


def p03():
    """Gros plan — gouttiere."""
    return gouttes()


def p04():
    """Moyen — feuilles."""
    S = ensemble(76, reprise=False)
    S.add(personne(289, 630, 1.4, regard=(1, -0.1), bras="chut", **NINO),
          personne(459, 618, 1.37, regard=(1, 0), bras="designe", **LILA))
    return S


def p05():
    """Gros plan — reponse."""
    S = ensemble(60)
    S.camera(1.44, 331, 515)
    return S


def p06():
    """Moyen — ritournelle."""
    S = ensemble(35, reprise=False)
    S.add(avec_cuilleres(209, 652, 1.45, 1, NINO, regard=(1, 0.4), bras="porte", expr="rire"),
          avec_cuilleres(430, 628, 1.4, 2, LILA, regard=(-1, 0.5), bras="applaudit", expr="rire"),
          recipient(239, 686, 1.12, "#3a80c3"))
    for x, y in ((248, 591), (290, 619), (419, 466)):
        S.add(chemin(f"M {x} {y} q 14 -23 27 0 m -28 12 q 15 -12 31 0", stroke="#f8f2dc", sw=4))
    return S


def p07():
    """Gros plan — silence."""
    return gouttes(derniere=True)


def p08():
    """Large — dehors."""
    S = Scene()
    cour(S, porche=False)
    S.add(soleil(146, 189, 39), flaque(204, 715, 0.85), flaque(596, 666, 0.55),
          personne(334, 632, 1.12, regard=(1, 0), bras="donne", pas="marche", **NINO),
          personne(513, 622, 1.11, regard=(-1, 0.3), bras="donne", flip=True, pas="marche", **LILA),
          recipient(425, 587, 0.83))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-repetition.svg", p01),
    ("02-averse.svg", p02),
    ("03-gouttiere.svg", p03),
    ("04-feuilles.svg", p04),
    ("05-reponse.svg", p05),
    ("06-ritournelle.svg", p06),
    ("07-silence.svg", p07),
    ("08-dehors.svg", p08),
]
