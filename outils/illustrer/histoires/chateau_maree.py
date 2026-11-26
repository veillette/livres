"""Un château pour la marée."""
from base import *
from fantastique import coquillage, personne

ID = "chateau-maree"
MINA = dict(peau="brune", cheveux="noir", coiffure="couettes", habit="#ef9861", chaussures="#e4a567")
SAMI = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#409e95", robe=False, stature="ado")
SABLE = "#dfb276"
OMBRE = "#a87e54"


def plage(avance=0):
    S = Scene()
    ciel(S, "#84dafa", "#fff0d1")
    S.add(nuage(133, 190, 0.88), nuage(682, 144, 0.64))
    eau(S, 395, "#4ab9c2", "#8de1da")
    S.add(chemin(f"M 0 {476 + avance} Q 350 {544 + avance} 800 {500 + avance} V 800 H 0 Z", "#ebc78b"),
          chemin(f"M 0 {490 + avance} Q 350 {558 + avance} 800 {514 + avance} M 0 {478 + avance} Q 350 {548 + avance} 800 {503 + avance}",
                 stroke="#fff8da", sw=8),
          caillou(75, 680, 0.45, "#d2b199"), caillou(756, 741, 0.54, "#c49f84"),
          coquillage(696, 736, 0.45, "#eab498", rot=-22))
    S.cachette(748, 669)
    return S


def tour(x, y, s=1, crenelee=True):
    m = [ellipse(0, 0, 59, 14, OMBRE, opacity=0.27),
         chemin("M -51 -9 L -39 -96 Q -4 -109 39 -96 L 52 -9 Q 6 11 -51 -9 Z", cylindre(SABLE, 0.25, 0.68)),
         ellipse(0, -96, 39, 12, "#f2d49c")]
    if crenelee:
        for px in (-33, -7, 19):
            m.append(rect(px, -115, 17, 26, volume("#e9bf83", 0.26, 0.76), rx=4))
    for px, py in ((-24, -33), (24, -24), (23, -68), (-17, -78), (5, -15)):
        m.append(cercle(px, py, 3, "#c69460", opacity=0.66))
    return place(m, x, y, s)


def chateau(S, mur=0):
    S.add(tour(429, 659, 1.16), tour(353, 682, 0.78), tour(509, 688, 0.86),
          coquillage(429, 522, 0.74, "#fff9ea", rot=10))
    if mur:
        S.add(chemin("M 285 725 Q 294 669 342 655 Q 427 627 533 670 L 562 718 L 539 729 Q 524 686 467 687 "
                     + ("L 455 714 L 414 715 L 398 685 " if mur == 2 else "Q 424 680 394 693 ")
                     + "Q 330 698 320 734 Z", "#d1a069", stroke="#b6895f", sw=3))


def enfants(S, gauche=221, droite=613, taille=1.18, geste="ramasse", joie="sourire"):
    S.add(personne(gauche, 693, taille, regard=(1, 0.8), bras=geste, expr=joie, **MINA),
          personne(droite, 677, taille, regard=(-1, 0.7), bras=geste, flip=True, **SAMI))


def couverture():
    S = plage()
    enfants(S, taille=1.42)
    chateau(S)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tour(199, 224, 1.38), tour(116, 242, 0.94), tour(286, 245, 1.02), coquillage(200, 64, 1, "#fff9ea"))
    return S


def p01():
    """Moyen — trois tours."""
    S = plage()
    enfants(S, 236, 619)
    chateau(S)
    S.add(chemin("M 259 705 L 304 700 L 316 754 Q 285 764 250 752 Z", "#4db6ac"), ellipse(282, 701, 23, 6, "#7de1cb"))
    return S


def p02():
    """Large — ecume."""
    S = plage(35)
    enfants(S, 255, 610, 1.1, "designe", "surpris")
    chateau(S)
    return S


def p03():
    """Gros plan — muraille."""
    S = plage(45)
    enfants(S, 296, 632, 1.2)
    chateau(S, mur=1)
    S.add(chemin("M 327 664 Q 336 659 347 660", stroke="#f0c9a3", sw=10))
    S.camera(1.68, 422, 562)
    S.cachette(574, 735)
    return S


def chenal(S, rempli=False):
    S.add(chemin("M 396 531 Q 464 554 477 581 Q 511 627 463 656 Q 429 687 461 710 L 443 723 Q 394 691 435 646 "
                 "Q 477 605 453 583 Q 427 562 370 541 Z", "#7ed6ce" if rempli else "#bc8e62",
                 stroke="#fff3d4" if rempli else "#b08761", sw=3))


def p04():
    """Moyen — breche."""
    S = plage(45)
    chenal(S, rempli=True)
    enfants(S, joie="surpris")
    chateau(S, mur=2)
    S.add(chemin("M 450 658 Q 417 691 452 715 L 442 723 Q 403 696 436 666 Z", "#8cdfd7"))
    return S


def p05():
    """Moyen — nouveau plan."""
    S = plage(25)
    chenal(S)
    chateau(S)
    enfants(S, 267, 623, 1.23)
    S.add(chemin("M 556 657 L 502 630", stroke="#f6b42e", sw=7), ellipse(490, 625, 17, 9, "#f6b42e", rot=23))
    return S


def p06():
    """Gros plan — port coquille."""
    S = plage(62)
    chenal(S, rempli=True)
    S.add(tour(415, 660, 1.01), ellipse(483, 677, 96, 32, "#7fd1c6"),
          ellipse(497, 684, 42, 10, "none", stroke="#d9f4df", stroke_width=3),
          coquillage(496, 677, 0.90, "#fff9ea", rot=-11))
    S.camera(1.67, 464, 562)
    S.cachette(616, 686)
    return S


def p07():
    """Large — sous eau."""
    S = plage(116)
    S.add(tour(454, 656, 0.41, False),
          chemin("M 302 656 Q 402 628 521 656 T 739 650", stroke="#fff9db", sw=9, opacity=0.85))
    enfants(S, 321, 596, 1.13)
    S.add(coquillage(363, 670, 0.51, "#fff9ea"))
    return S


def p08():
    """Moyen — carte sable."""
    S = plage()
    enfants(S, 240, 618, 1.24, joie="rire")
    S.add(chemin("M 339 709 L 346 659 H 383 L 391 710 M 394 693 L 406 625 H 452 L 464 692 "
                 "M 471 713 L 480 664 H 521 L 534 712 M 339 713 Q 424 744 534 712", stroke="#b58858", sw=6),
          coquillage(435, 709, 0.75, "#fff9ea"))
    return S


IMAGES = [
    ("couverture.svg", couverture),
    ("vignette.svg", vignette),
    ("01-trois-tours.svg", p01),
    ("02-ecume.svg", p02),
    ("03-muraille.svg", p03),
    ("04-breche.svg", p04),
    ("05-nouveau-plan.svg", p05),
    ("06-port-coquille.svg", p06),
    ("07-sous-eau.svg", p07),
    ("08-carte-sable.svg", p08),
]
