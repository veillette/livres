"""Zoé et la petite ampoule — le circuit électrique.

Le courant ne circule que dans une boucle fermée : de la borne + de la pile,
à travers l'ampoule, jusqu'à la borne −. Les flèches suivent le sens
conventionnel du courant (du + vers le − à l'extérieur de la pile). Deux
ampoules en série brillent moins qu'une seule : le halo est plus petit.
"""
from base import *
from objets import *
from sciences import *
from contes import chaise

ID = "zoe-ampoule"
ZOE = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#f59f00", jambes="#364fc7", robe=False)
LEO = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#20c997", jambes="#1864ab", robe=False)
PAPI = dict(peau="brune", cheveux="blanc", coiffure="chauve_cote", barbe="#e9ecef", habit="#2f9e44",
            jambes="#495057", robe=False, acc=("lunettes",))
ROUGE, NOIR = "#e03131", "#343a40"
JAUNE = "#ffd43b"


def zoe(x, y, s=1.0, **k):
    return personne(x, y, s, **{**ZOE, **k})


def leo(x, y, s=0.8, **k):
    return personne(x, y, s, **{**LEO, **k})


def papi(x, y, s=1.1, **k):
    return personne(x, y, s, **{**PAPI, **k})


# ---------------------------------------------------------------------------
# Matériel électrique
# ---------------------------------------------------------------------------

def pile(x, y, s=1.0, rot=0, usee=False):
    """Pile couchée, borne + à droite ; (x, y) = centre. Bornes à ±100."""
    corps = "#adb5bd" if usee else "#fab005"
    m = [rect(-90, -34, 180, 68, corps, rx=10),
         rect(-90, -34, 70, 68, NOIR, rx=10), rect(-40, -34, 20, 68, NOIR),
         rect(90, -14, 12, 28, "#ced4da", rx=3), rect(-96, -22, 8, 44, "#ced4da", rx=2),
         rect(-80, -26, 160, 8, "#fff", opacity=0.3, rx=4),
         texte(60, 18, "+", 52, NOIR), texte(-56, 16, "−", 52, "#fff")]
    return place(m, x, y, s, rot=rot)


def ampoule(x, y, s=1.0, allumee=False, halo=1.0):
    """Ampoule sur son socle ; (x, y) = bas du socle. Bornes en (±60, -12)."""
    m = []
    if allumee:
        for r, o in ((120, 0.18), (90, 0.25), (64, 0.35)):
            m.append(cercle(0, -110, r * halo, JAUNE, opacity=o))
        m.append(eclat(0, -110, 2.0 * halo, "#fcc419"))
    verre = "#fff3bf" if allumee else "#e9ecef"
    m += [rect(-70, -24, 140, 24, "#c68642", rx=6),
          cercle(-60, -12, 8, "#868e96"), cercle(60, -12, 8, "#868e96"),
          rect(-22, -60, 44, 36, "#adb5bd", rx=4),
          g([trait(-22, -52 + k * 9, 22, -48 + k * 9, "#868e96", 3) for k in range(4)]),
          chemin("M -22 -60 Q -48 -88 -46 -112 A 46 46 0 1 1 46 -112 Q 48 -88 22 -60 Z", verre,
                 stroke="#868e96", sw=4, opacity=0.95),
          chemin("M -10 -62 L -10 -100 L -4 -110 L 2 -100 L 8 -110 L 10 -100 L 10 -62",
                 stroke="#f08c00" if allumee else "#868e96", sw=4),
          ellipse(-22, -130, 9, 16, "#fff", opacity=0.7, rot=-20)]
    return place(m, x, y, s)


def fil(points, couleur=ROUGE, sw=9):
    d = "M " + " L ".join(f"{px} {py}" for px, py in points)
    return chemin(d, stroke=couleur, sw=sw)


def interrupteur(x, y, ferme=True):
    """Interrupteur à levier sur un fil horizontal ; bornes en x ± 50."""
    m = [rect(x - 64, y - 6, 128, 26, "#868e96", rx=6), cercle(x - 44, y, 10, NOIR), cercle(x + 44, y, 10, NOIR)]
    lev = place(g([rect(0, -6, 92, 12, "#495057", rx=6), cercle(92, 0, 9, ROUGE)]), x - 44, y, rot=0 if ferme else -35)
    return g(m + [lev])


def circuit(allumee=True, trou=None, objet="", ampoules=1, inter=None, fleches=True, halo=1.0):
    """Boucle pile + ampoule(s) en coordonnées locales (cadre 800 × 800).

    trou : None (boucle fermée) ou "ouvert" : le fil de gauche est coupé entre
    y = 420 et y = 520, et `objet` (dessiné centré en (180, 470)) peut combler
    le trou. inter : None, "ouvert" ou "ferme" (interrupteur en haut à gauche).
    """
    m = []
    xs = [400] if ampoules == 1 else [300, 500]
    # fil du haut et des côtés
    m.append(fil([(500, 640), (620, 640), (620, 330), (xs[-1] + 60, 330)], ROUGE))
    if ampoules == 2:
        m.append(fil([(xs[0] + 60, 330), (xs[1] - 60, 330)], ROUGE))
    if inter:
        m.append(fil([(xs[0] - 60, 330), (280, 330)], NOIR))
        m.append(fil([(180, 330), (180, 640), (300, 640)], NOIR))
        m.append(fil([(180, 330), (184, 330)], NOIR))
    elif trou:
        m.append(fil([(xs[0] - 60, 330), (180, 330), (180, 420)], NOIR))
        m.append(fil([(180, 520), (180, 640), (300, 640)], NOIR))
        m.append(cercle(180, 420, 10, "#868e96"))
        m.append(cercle(180, 520, 10, "#868e96"))
    else:
        m.append(fil([(xs[0] - 60, 330), (180, 330), (180, 640), (300, 640)], NOIR))
    m.append(pile(400, 640, 1.0))
    for x in xs:
        m.append(ampoule(x, 342, 0.95, allumee, halo))
    if inter:
        m.append(interrupteur(230, 324, inter == "ferme"))
    if objet:
        m.append(objet)
    if fleches and allumee:
        c = "#f76707"
        m += [fleche(665, 600, 665, 390, c, 7, 22), fleche(135, 380, 135, 590, c, 7, 22),
              fleche(200, 690, 290, 690, c, 7, 22)]
        if ampoules == 1:
            m += [fleche(590, 290, 500, 290, c, 7, 22), fleche(320, 290, 230, 290, c, 7, 22)]
    return g(m)


def cuillere(x, y, s=1.0, rot=0):
    m = [rect(-6, -10, 12, 90, "#ced4da", rx=6), ellipse(0, -36, 22, 32, "#dee2e6", stroke="#adb5bd", stroke_width=3)]
    return place(m, x, y, s, rot=rot)


def gomme(x, y, s=1.0):
    return place([rect(-46, -22, 92, 44, "#ff8fab", rx=8), rect(10, -22, 36, 44, "#4dabf7", rx=6)], x, y, s)


def bouchon(x, y, s=1.0):
    return place([poly([(-26, -34), (26, -34), (32, 34), (-32, 34)], "#d9a066"),
                  g([cercle(-10 + 10 * (k % 3), -16 + 14 * (k // 3), 3, "#a0693a") for k in range(9)])], x, y, s)


def ficelle(x, y, s=1.0):
    return place([chemin("M -50 0 Q -25 -30 0 0 Q 25 30 50 0", stroke="#c68642", sw=8)], x, y, s)


def coche(x, y, ok=True, s=1.0):
    if ok:
        return place([cercle(0, 0, 34, "#40c057"), chemin("M -16 0 L -4 14 L 18 -14", stroke="#fff", sw=9)], x, y, s)
    return place([cercle(0, 0, 34, "#fa5252"), trait(-14, -14, 14, 14, "#fff", 9), trait(14, -14, -14, 14, "#fff", 9)], x, y, s)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def salon(S, nuit=True):
    interieur(S, "#3b4a7a" if nuit else "#fff4e6", "#8d6e63" if nuit else "#e8c39e", 600,
              papier="#34426e" if nuit else "#ffe8cc")


def cuisine(S):
    interieur(S, "#e7f5ff", "#e8c39e", 600, papier="#d0ebff")
    S.add(fenetre(600, 100, 150, 140, "#a5d8ff", rideaux="#ffd43b"))


def cabane(S, x0=150, x1=650, couleur="#f06595", eclairee=False):
    S.add(chaise(x0, 700, 1.3, "#c68642"), chaise(x1, 700, 1.3, "#c68642"))
    S.add(chemin(f"M {x0 - 70} 720 Q {x0 - 50} 470 {x0 - 20} 430 L {x1 + 20} 430 Q {x1 + 50} 470 {x1 + 70} 720 Z",
                 couleur, opacity=0.95))
    S.add(g([trait(x0 - 10 + k * 70, 440, x0 - 30 + k * 72, 715, "#fff", 4, opacity=0.25) for k in range(8)]))
    if eclairee:
        S.add(chemin(f"M {x0 + 40} 470 L {x1 - 40} 470 L {x1 - 10} 690 L {x0 + 10} 690 Z", "#fff3bf", opacity=0.55))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S)
    S.add(fenetre(600, 90, 140, 130, nuit_=True))
    S.add(ampoule(300, 560, 2.1, True))
    S.add(fil([(174, 535), (120, 535), (120, 690), (230, 690)], NOIR), fil([(426, 535), (470, 535), (470, 690), (390, 690)], ROUGE))
    S.add(pile(310, 690, 0.8))
    S.add(zoe(600, 790, 1.55, expr="rire", bras="montre", regard=(-1, -0.4)))
    S.add(paillettes(140, 170), paillettes(470, 140, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ampoule(120, 250, 0.95, True))
    S.add(zoe(270, 264, 0.95, expr="content", bras="montre", regard=(-1, -0.4)))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(fenetre(80, 90, 150, 140, nuit_=True))
    S.add(lampe(690, 600, 1.0, allumee=False))
    cabane(S)
    S.add(zoe(330, 720, 1.0, expr="surpris", bras="porte", objet=lampe_poche(0, -70, 1.0, rot=-15)))
    S.add(leo(480, 720, 0.85, expr="inquiet", bras="joues"))
    S.add(texte(400, 330, "Clic…", 84, "#ffe066", contour="#1c2a52"))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(papi(170, 640, 1.35, expr="sourire", bras="montre", regard=(1, 0.5)))
    S.add(zoe(650, 650, 1.05, expr="surpris", bras="bas", regard=(-1, 0.5)))
    S.add(table(400, 790, 640, 170, "#c68642", nappe="#fff9db"))
    S.add(lampe_poche(230, 590, 1.6, rot=0))
    S.add(pile(420, 585, 0.6))
    S.add(ampoule(560, 610, 0.55))
    S.add(chemin("M 300 610 q 10 -20 20 0 q 10 20 20 0 q 10 -20 20 0 q 10 20 20 0", stroke="#adb5bd", sw=5))
    return S


def p03():
    S = Scene()
    fond(S, "#fff9db")
    S.add(pile(400, 400, 2.8))
    S.add(texte(620, 210, "plus", 56, ROUGE), fleche(620, 230, 620, 320, ROUGE, 7, 22))
    S.add(texte(160, 210, "moins", 56, NOIR), fleche(160, 230, 150, 320, NOIR, 7, 22))
    S.add(zoe(400, 790, 0.95, expr="joie", bras="montre", regard=(1, -1)))
    S.cachette(410, 70, "air")
    return S


def p04():
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(fil([(500, 640), (620, 640), (620, 330), (460, 330)], ROUGE))
    S.add(fil([(300, 640), (180, 640), (180, 560)], NOIR), cercle(180, 560, 10, "#868e96"))
    S.add(pile(400, 640), ampoule(400, 342, 0.95, False))
    S.add(cercle(340, 330, 10, "#868e96"))
    S.add(texte(130, 230, "?", 120, "#7048e8"), texte(700, 200, "?", 90, "#7048e8"))
    S.add(zoe(150, 800, 0.8, expr="inquiet", bras="pense", regard=(1, -1)))
    S.cachette(560, 760, "air")
    return S


def p05():
    S = Scene()
    fond(S, "#fff9db")
    S.add(circuit(True))
    S.add(texte(400, 110, "Ça s'allume !", 70, "#e8590c", contour="#fff"))
    S.cachette(400, 730, "air")
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    collines(S, 520, "#b2f2bb", graine=4)
    sol(S, 560, "#8ce99a")
    enfants = [dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#ff8787", robe=True),
               dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#4dabf7"),
               dict(peau="doree", cheveux="brun", coiffure="queue", habit="#ffd43b", robe=True),
               dict(peau="rosee", cheveux="blond", coiffure="herisses", habit="#69db7c"),
               dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#f59f00", robe=False, jambes="#364fc7"),
               dict(peau="claire", cheveux="chatain", coiffure="courts", habit="#9775fa")]
    xs = [90, 200, 310, 490, 600, 710]
    for k, (e, x) in enumerate(zip(enfants, xs)):
        expr = "surpris" if k in (2, 3) else "rire"
        S.add(personne(x, 720 - (30 if k in (0, 5) else 0), 0.95, expr=expr, bras="large", **e))
    S.add(texte(400, 470, "!", 110, ROUGE, contour="#fff"))
    S.cachette(730, 210, "air")
    return S


def p07():
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(rect(400, 60, 6, 680, "#dee2e6"))
    S.add(place(circuit(False, inter="ouvert", fleches=False), 0, 110, 0.5))
    S.add(place(circuit(True, inter="ferme", fleches=False), 400, 110, 0.5))
    S.add(texte(200, 560, "Clic !", 64, "#495057"), texte(200, 630, "éteint", 50, "#868e96"))
    S.add(texte(600, 560, "Clac !", 64, "#e8590c"), texte(600, 630, "allumé", 50, "#f08c00"))
    S.cachette(200, 730, "air")
    return S


def p08():
    S = Scene()
    fond(S, "#fff9db")
    obj = g([trait(180, 420, 180, 440, "#868e96", 6), trait(180, 500, 180, 520, "#868e96", 6),
             trombone(180, 470, 1.6, rot=90)])
    S.add(circuit(True, trou="ouvert", objet=obj, fleches=False))
    S.add(cle(560, 740, 1.3, rot=-20), cuillere(700, 760, 1.0, rot=30), trombone(440, 760, 1.4))
    S.add(coche(70, 470), texte(400, 110, "Le métal laisse passer !", 50, "#2b8a3e", contour="#fff"))
    S.cachette(370, 730, "air")
    return S


def p09():
    S = Scene()
    fond(S, "#f1f3f5")
    S.add(circuit(False, trou="ouvert", objet=gomme(180, 470, 1.0), fleches=False))
    S.add(bouchon(520, 750, 1.0), ficelle(690, 750, 1.0))
    S.add(coche(70, 470, ok=False))
    # un fil coupé : le cuivre au milieu, le plastique autour
    S.add(place([rect(-60, -20, 120, 40, ROUGE, rx=18), ellipse(60, 0, 10, 20, "#c92a2a"),
                 ellipse(60, 0, 6, 10, "#e67700")], 660, 130, 1.2))
    S.add(texte(480, 230, "plastique", 36, ROUGE, anchor="start"), texte(480, 270, "autour du fil", 36, ROUGE, anchor="start"))
    S.cachette(650, 70, "air")
    return S


def p10():
    S = Scene()
    fond(S, "#fff9db")
    S.add(rect(60, 396, 680, 6, "#dee2e6"))
    S.add(place(circuit(True, fleches=False), 160, 0, 0.5))
    S.add(place(circuit(True, ampoules=2, fleches=False, halo=0.55), 160, 390, 0.5))
    S.add(texte(140, 220, "1", 90, "#e8590c"), texte(140, 610, "2", 90, "#e8590c"))
    S.add(texte(660, 220, "très fort", 40, "#e8590c"), texte(660, 610, "moins fort", 40, "#f08c00"))
    S.cachette(440, 70, "air")
    return S


def p11():
    S = Scene()
    interieur(S, "#e6fcf5", "#ced4da", 600, papier="#c3fae8")
    S.add(rect(480, 380, 220, 300, "#fcc419", rx=16), rect(540, 410, 100, 18, NOIR, rx=8))
    S.add(texte(590, 520, "PILES", 52, NOIR), place(g([pile(0, 0, 0.35, usee=True), pile(0, 30, 0.35, usee=True)]), 590, 600))
    S.add(zoe(260, 780, 1.3, expr="fier", bras="donne", regard=(1, -0.5),
              objet=""))
    S.add(pile(395, 545, 0.32, rot=-20, usee=True))
    return S


def p12():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 600, papier="#ffe8cc")
    # prise avec cache de sécurité
    S.add(rect(140, 360, 150, 150, "#f8f9fa", rx=24, stroke="#ced4da", stroke_width=4))
    S.add(cercle(215, 435, 52, "#e9ecef"), cercle(195, 435, 8, NOIR), cercle(235, 435, 8, NOIR))
    S.add(cercle(215, 250, 70, "#fff", stroke=ROUGE, stroke_width=14))
    S.add(place([chemin("M -14 30 L -14 -20 Q -14 -30 -6 -30 Q 2 -30 2 -20 L 2 -36 Q 2 -46 10 -46 Q 18 -46 18 -36 L 18 30 Z", "#ffc9c9", stroke=ROUGE, sw=3)], 215, 260))
    S.add(papi(560, 760, 1.4, expr="neutre", bras="salut", regard=(-1, 0)))
    # pile bouton
    S.add(cercle(400, 680, 34, "#ced4da", stroke="#868e96", stroke_width=4), texte(400, 694, "+", 40, "#868e96"))
    S.add(coche(450, 640, ok=False, s=0.7))
    return S


def p13():
    S = Scene()
    salon(S, nuit=False)
    S.add(leo(400, 790, 1.7, expr="rire", bras="tete", coiffure="herisses"))
    S.add(ballon_air(560, 330, 1.2, "#cc5de8", fil=60))
    for k in range(5):
        S.add(texte(250 + k * 60, 140 + (k % 2) * 30, "+" if k % 2 else "−", 40, "#7048e8"))
    S.add(zoe(130, 790, 0.95, expr="rire", bras="bouche"))
    return S


def p14():
    S = Scene()
    salon(S)
    dehors = [rect(160, 80, 480, 360, "#343a62"), nuage_orage(330, 150, 1.4), nuage(540, 140, 1.0, "#495057"),
              g([trait(170 + k * 37, 270 + (k % 3) * 30, 160 + k * 37, 300 + (k % 3) * 30, "#a5d8ff", 3) for k in range(13)])]
    S.add(fenetre(160, 80, 480, 360, "#343a62", contenu=g(dehors)))
    S.add(rect(140, 560, 520, 150, "#748ffc", rx=30), rect(110, 520, 70, 190, "#5c7cfa", rx=26), rect(620, 520, 70, 190, "#5c7cfa", rx=26))
    S.add(zoe(300, 620, 0.9, expr="bouche_bee", bras="bas", regard=(0, -1)))
    S.add(leo(480, 620, 0.75, expr="surpris", bras="joues", regard=(0, -1)))
    S.add(texte(620, 520, "Boum !", 64, "#ffe066", contour="#1c2a52", rot=-8))
    return S


def p15():
    S = Scene()
    salon(S, nuit=False)
    S.add(table(400, 790, 680, 150, "#c68642"))
    # maison en carton
    S.add(poly([(260, 410), (440, 290), (620, 410)], "#c98f4a"), rect(280, 410, 320, 220, "#d9a066"))
    S.add(rect(310, 450, 100, 90, "#fff3bf"), cercle(360, 495, 60, JAUNE, opacity=0.35))
    S.add(rect(470, 520, 70, 110, "#a0693a"), trait(310, 495, 410, 495, "#d9a066", 6), trait(360, 450, 360, 540, "#d9a066", 6))
    S.add(fil([(560, 640), (650, 640), (650, 470), (580, 470)], ROUGE, 6), pile(680, 610, 0.45, rot=-90))
    S.add(zoe(140, 790, 1.2, expr="fier", bras="montre", regard=(1, -0.3)))
    return S


def p16():
    S = Scene()
    salon(S)
    cabane(S, couleur="#f06595", eclairee=True)
    S.add(place([ellipse(0, 0, 50, 40, "#1c2a52", opacity=0.6), ellipse(-26, -56, 12, 40, "#1c2a52", opacity=0.6, rot=-12),
                 ellipse(10, -60, 12, 40, "#1c2a52", opacity=0.6, rot=12), cercle(26, 4, 4, "#fff3bf")], 470, 560))
    S.add(zoe(260, 720, 0.95, expr="rire", bras="tient", objet=""))
    S.add(lampe_poche(320, 570, 1.0, rot=-10, faisceau=150))
    S.add(leo(600, 720, 0.8, expr="rire", bras="haut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("zoe-seule.svg", vignette),
    ("01-la-cabane.svg", p01), ("02-dans-la-lampe.svg", p02), ("03-la-pile.svg", p03), ("04-un-seul-fil.svg", p04),
    ("05-la-boucle.svg", p05), ("06-la-ronde.svg", p06), ("07-interrupteur.svg", p07), ("08-le-metal.svg", p08),
    ("09-le-plastique.svg", p09), ("10-deux-ampoules.svg", p10), ("11-recycler.svg", p11), ("12-attention.svg", p12),
    ("13-ballon.svg", p13), ("14-orage.svg", p14), ("15-maison-carton.svg", p15), ("16-les-ombres.svg", p16),
]
