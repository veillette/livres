"""Souris et Éléphant — les leviers.

La bascule est en équilibre quand « poids × distance au pivot » est le même
des deux côtés : l'Éléphant, très lourd, doit s'asseoir tout près du milieu,
la petite Souris tout au bout. Les leviers du quotidien sont dessinés avec
leur pivot au bon endroit (bord de la capsule, tête du marteau, roue de la
brouette, vis des ciseaux, bord de la barque pour la rame).
"""
from base import *
from objets import *
from sciences import *

ID = "souris-elephant"
SOURIS = dict(acc=("noeud",), couleur_acc="#f06595")
PIVOT = "#e8590c"
PLANCHE = "#f76707"


def pre(S, graine=1, haut="#99e9f2", bas="#e3fafc", y=620):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 90)


class Bascule:
    """Bascule : pivot posé au sol en (x, y), planche de demi-longueur L inclinée de `angle` degrés
    (positif = le côté droit descend)."""

    def __init__(self, x, y, L=330, angle=0, h=110):
        self.x, self.y, self.L, self.angle, self.h = x, y, L, angle, h

    def point(self, d):
        """Point sur le dessus de la planche à la distance d du pivot (d < 0 : côté gauche)."""
        a = math.radians(self.angle)
        return self.x + d * math.cos(a) + 12 * math.sin(a), self.y - self.h + d * math.sin(a) - 12 * math.cos(a)

    def dessin(self):
        m = [poly([(self.x - 60, self.y), (self.x, self.y - self.h), (self.x + 60, self.y)], PIVOT)]
        m.append(place(rect(-self.L, -12, 2 * self.L, 24, PLANCHE, rx=10), self.x, self.y - self.h, rot=self.angle))
        for sgn in (-1, 1):
            m.append(place(rect(sgn * (self.L - 30) - 6, -44, 12, 34, "#495057", rx=5), self.x, self.y - self.h, rot=self.angle))
        return g(m)

    def assis(self, d, dessin_fn):
        """Place un personnage (fonction (x, y) -> dessin) debout sur la planche à la distance d."""
        x, y = self.point(d)
        return dessin_fn(x, y)


def souris(x, y, s=0.6, **k):
    return perso("souris", x, y, s, **{**SOURIS, **k})


def elephant(x, y, s=1.3, **k):
    return perso("elephant", x, y, s, **k)


def couverture():
    S = Scene()
    pre(S, 3)
    b = Bascule(400, 740, 340, 0)
    S.add(b.dessin())
    S.add(b.assis(-310, lambda x, y: souris(x, y, 0.95, expr="rire", bras="haut")))
    S.add(b.assis(60, lambda x, y: elephant(x, y, 1.35, expr="rire", bras="haut")))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(souris(95, 262, 0.85, expr="content", bras="salut"))
    S.add(elephant(285, 262, 1.0, expr="content", regard=(-1, 0)))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(arbre(110, 640, 0.8))
    b = Bascule(420, 740, 330, -14)
    S.add(b.dessin())
    S.add(souris(250, 770, 1.1, expr="sourire", bras="ouverts", regard=(1, 0)))
    S.add(elephant(700, 640, 0.9, expr="content", regard=(-1, 0)))
    S.add(bulle(330, 170, 440, 90, "Qui veut jouer ?", 46, pointe=(260, 520)))
    return S


def p02():
    S = Scene()
    pre(S, 2)
    b = Bascule(400, 740, 330, 16)
    S.add(b.dessin())
    S.add(b.assis(-300, lambda x, y: souris(x, y, 0.8, expr="surpris", bras="haut", pieds_haut=True)))
    S.add(b.assis(280, lambda x, y: elephant(x, y, 1.25, expr="content", regard=(-1, -1))))
    S.add(texte(200, 170, "Oh là là !", 56, "#e64980", contour="#fff"), texte(640, 330, "Boum !", 50, "#495057", contour="#fff"))
    return S


def p03():
    S = Scene()
    pre(S, 3)
    b = Bascule(400, 740, 330, 16)
    S.add(b.dessin())
    for d, fn in [(-300, lambda x, y: souris(x, y, 0.7, expr="concentre", bras="haut")),
                  (-240, lambda x, y: perso("lapin", x, y, 0.65, expr="concentre", bras="haut")),
                  (-175, lambda x, y: perso("herisson", x, y, 0.6, expr="concentre")),
                  (-110, lambda x, y: perso("renard", x, y, 0.65, expr="concentre", bras="haut"))]:
        S.add(b.assis(d, fn))
    S.add(b.assis(280, lambda x, y: elephant(x, y, 1.25, expr="sourire", regard=(-1, -1))))
    S.add(texte(150, 170, "1", 60, "#e64980", contour="#fff"), texte(250, 170, "2", 60, "#e64980", contour="#fff"), texte(350, 170, "3", 60, "#e64980", contour="#fff"))
    return S


def p04():
    S = Scene()
    pre(S, 4)
    S.add(arbre(620, 640, 1.0))
    S.add(chouette(620, 380, 0.9, expr="fier", ailes="ouvertes", regard=(-1, 0)))
    b = Bascule(330, 740, 290, 16)
    S.add(b.dessin())
    S.add(b.assis(-265, lambda x, y: souris(x, y, 0.7, expr="bouche_bee")))
    S.add(b.assis(240, lambda x, y: elephant(x, y, 1.1, expr="surpris", regard=(1, -1))))
    S.add(bulle(420, 130, 380, 90, "J'ai une idée !", 44, pointe=(580, 320)))
    return S


def p05():
    S = Scene()
    pre(S, 5)
    b = Bascule(400, 740, 330, 7)
    S.add(b.dessin())
    S.add(b.assis(-300, lambda x, y: souris(x, y, 0.8, expr="content", regard=(1, 0))))
    S.add(b.assis(150, lambda x, y: elephant(x, y, 1.25, expr="concentre", regard=(-1, 0))))
    S.add(fleche(620, 420, 500, 420, "#e64980", 7))
    S.add(fleche(90, 330, 90, 420, "#1c7ed6", 6))
    return S


def p06():
    S = Scene()
    pre(S, 6)
    b = Bascule(400, 740, 340, 0)
    S.add(b.dessin())
    S.add(b.assis(-310, lambda x, y: souris(x, y, 0.8, expr="rire", bras="haut")))
    S.add(b.assis(45, lambda x, y: elephant(x, y, 1.25, expr="rire")))
    # distances au pivot
    S.add(trait(90, 650, 400, 650, "#e64980", 4), trait(400, 650, 445, 650, "#1c7ed6", 4))
    S.add(trait(90, 638, 90, 662, "#e64980", 4), trait(400, 638, 400, 662, "#495057", 4), trait(445, 638, 445, 662, "#1c7ed6", 4))
    S.add(texte(400, 170, "Équilibre !", 70, "#e64980", contour="#fff"))
    S.add(etoile5(150, 150, 20, "#fcc419"), etoile5(650, 150, 20, "#fcc419"))
    return S


def p07():
    S = Scene()
    fond(S, "#fff9db")
    b = Bascule(400, 560, 320, 0, h=130)
    S.add(b.dessin())
    S.add(fleche(120, 250, 120, 400, "#c92a2a", 8), fleche(680, 250, 680, 400, "#c92a2a", 8))
    S.add(texte(400, 330, "levier", 60, PLANCHE), texte(400, 640, "pivot", 60, PIVOT))
    return S


def p08():
    S = Scene()
    pre(S, 8, y=640)
    # levier : bâton sous le rocher, petit caillou comme pivot tout près du rocher, on appuie loin au bout
    S.add(caillou(470, 700, 1.0, "#868e96"))
    S.add(place(rect(-300, -8, 420, 16, "#8d5524", rx=6), 470, 668, rot=12))
    S.add(place(chemin("M -130 0 Q -140 -150 0 -170 Q 140 -170 130 0 Z", "#868e96"), 610, 700, rot=-6))
    S.add(fleche(610, 480, 610, 420, "#2f9e44", 7))
    S.add(souris(215, 610, 0.8, expr="concentre", bras="haut", regard=(1, 0)))
    S.add(fleche(170, 470, 170, 560, "#c92a2a", 7))
    S.add(texte(470, 790, "pivot", 36, PIVOT))
    return S


def bouteille_verre(x, y, s=1.0):
    return place([rect(-40, -150, 80, 150, "#2b8a3e", rx=16, opacity=0.9), rect(-14, -220, 28, 80, "#2b8a3e", opacity=0.9),
                  rect(-18, -236, 36, 18, "#fab005", rx=4)], x, y, s)


def p09():
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(rect(0, 640, 800, 160, "#c68642"))
    # décapsuleur : pivot sur le bord de la capsule, on soulève le manche
    S.add(bouteille_verre(200, 650, 1.3))
    S.add(place(g([rect(0, -10, 200, 20, "#adb5bd", rx=10), cercle(0, 0, 22, "none", stroke="#adb5bd", stroke_width=8)]), 200, 350, rot=-25))
    S.add(fleche(360, 300, 360, 220, "#c92a2a", 6), cercle(182, 354, 8, PIVOT))
    # marteau : la tête posée sur la planche sert de pivot pour arracher le clou
    S.add(rect(480, 610, 300, 40, "#e8c39e"))
    S.add(clou(620, 600, 1.2, rot=20))
    S.add(place(g([rect(-8, -250, 16, 250, "#a0693a", rx=6), chemin("M -40 -250 L 40 -250 Q 60 -230 50 -210 L -40 -226 Z", "#495057")]), 600, 610, rot=-40))
    S.add(cercle(612, 606, 8, PIVOT), fleche(460, 380, 520, 440, "#c92a2a", 6))
    S.add(souris(90, 790, 0.9, expr="content", regard=(1, -1)))
    return S


def p10():
    S = Scene()
    pre(S, 10)
    # brouette : la roue est le pivot, la charge au milieu, on soulève les poignées
    x, y = 470, 740
    S.add(cercle(x + 150, y - 40, 40, ENCRE), cercle(x + 150, y - 40, 16, "#adb5bd"))
    S.add(poly([(x - 120, y - 170), (x + 150, y - 170), (x + 110, y - 70), (x - 90, y - 90)], "#1c7ed6"))
    S.add(trait(x - 90, y - 90, x - 260, y - 150, "#495057", 10), trait(x - 80, y - 90, x - 60, y - 20, "#495057", 8))
    for k in range(9):
        S.add(place(g([poly([(-12, 0), (12, 0), (0, 60)], "#ff922b"), ellipse(0, -8, 8, 14, "#51cf66")]), x - 80 + (k % 5) * 44 + (k // 5) * 22, y - 210 - (k // 5) * 30, rot=160))
    S.add(perso("lapin", x - 330, y + 10, 1.2, expr="content", bras="tire", regard=(1, 0)))
    S.add(fleche(700, 500, 780, 500, "#2f9e44", 6))
    return S


def ciseaux(x, y, s=1.0, ouverture=20):
    m = []
    for sgn in (-1, 1):
        m.append(place(g([poly([(0, -6), (160, -2), (160, 2), (0, 6)], "#adb5bd"), cercle(-60, 0, 30, "none", stroke="#fa5252", stroke_width=12), trait(-30, 0, 0, 0, "#fa5252", 12)]), 0, 0, rot=sgn * ouverture / 2))
    m.append(cercle(0, 0, 9, PIVOT))
    return place(m, x, y, s)


def p11():
    S = Scene()
    fond(S, "#fff0f6")
    S.add(rect(0, 640, 800, 160, "#e8c39e"))
    for k in range(8):
        S.add(place(poly([(-30, 0), (30, 0), (0, 60)], ["#fa5252", "#fcc419", "#51cf66", "#339af0"][k % 4]), 120 + k * 80, 110))
    S.add(trait(60, 110, 760, 110, "#495057", 3))
    S.add(perso("herisson", 280, 760, 1.4, expr="concentre", bras="donne", regard=(1, 0)))
    S.add(ciseaux(480, 540, 1.3, 30))
    S.add(rect(600, 520, 160, 40, "#f783ac", rx=4))
    S.add(texte(600, 360, "Crac, crac !", 56, "#e64980", contour="#fff"))
    return S


def p12():
    S = Scene()
    pre(S, 12, "#d3f9d8", "#f4fce3")
    x, y = 400, 700
    a = 14
    S.add(rect(x - 12, y - 330, 24, 330, "#868e96"), rect(x - 90, y - 10, 180, 20, "#868e96", rx=6))
    S.add(place(g([rect(-220, -8, 440, 16, "#495057", rx=6),
                   trait(-200, 0, -250, 150, "#adb5bd", 3), trait(-200, 0, -150, 150, "#adb5bd", 3),
                   trait(200, 0, 150, 150, "#adb5bd", 3), trait(200, 0, 250, 150, "#adb5bd", 3)]), x, y - 330, rot=a))
    lx, ly = x - 200 * math.cos(math.radians(a)), y - 330 - 200 * math.sin(math.radians(a))
    rx_, ry = x + 200 * math.cos(math.radians(a)), y - 330 + 200 * math.sin(math.radians(a))
    for px, py in ((lx, ly), (rx_, ry)):
        S.add(ellipse(px, py + 150, 60, 12, "#adb5bd"))
    S.add(pomme(lx - 20, ly + 132, 1.0), pomme(lx + 20, ly + 132, 1.0))
    S.add(place(g([ellipse(-26, -40, 34, 44, "#fd7e14"), ellipse(26, -40, 34, 44, "#fd7e14"), ellipse(0, -40, 34, 46, "#ff922b"), rect(-4, -94, 8, 18, "#2f9e44")]), rx_, ry + 148))
    S.add(chouette(640, 780, 0.9, expr="content", regard=(-1, -1)))
    S.add(texte(250, 130, "La plus lourde ?", 48, "#2f9e44", contour="#fff"))
    return S


def p13():
    S = Scene()
    interieur(S, "#e6fcf5", "#e8c39e", y=640)
    # mobile en équilibre : l'objet le plus lourd est accroché plus près du fil
    hx, hy = 400, 100
    S.add(trait(hx, 40, hx, hy, "#495057", 3))
    S.add(trait(hx - 240, hy, hx + 120, hy, "#8d5524", 8))
    S.add(trait(hx - 240, hy, hx - 240, 250, "#495057", 3), etoile5(hx - 240, 280, 34, "#fcc419"))
    S.add(trait(hx + 120, hy, hx + 120, 190, "#495057", 3))
    # sous-mobile : la lune (deux fois plus lourde que la perle) est deux fois plus près du fil
    S.add(trait(hx + 70, 190, hx + 220, 190, "#8d5524", 6))
    S.add(trait(hx + 70, 190, hx + 70, 270, "#495057", 3), lune_phase(hx + 70, 310, 40, 0.3, True, "#fab005", halo=False, crateres=False))
    S.add(trait(hx + 220, 190, hx + 220, 260, "#495057", 3), cercle(hx + 220, 280, 20, "#f06595"))
    S.add(perso("renard", 400, 790, 1.4, expr="fier", bras="haut", regard=(0, -1)))
    return S


def p14():
    S = Scene()
    ciel(S, "#99e9f2", "#e3fafc")
    collines(S, 420, "#b2f2bb", graine=14)
    eau(S, 440, "#1c7ed6", "#4dabf7")
    x, y = 400, 580
    S.add(chemin(f"M {x - 220} {y - 40} L {x + 220} {y - 40} Q {x + 200} {y + 40} {x + 120} {y + 50} L {x - 120} {y + 50} Q {x - 200} {y + 40} {x - 220} {y - 40} Z", "#a0693a"))
    S.add(elephant(x, y - 20, 1.1, expr="concentre", bras="large"))
    for sgn in (-1, 1):
        S.add(trait(x + sgn * 70, y - 90, x + sgn * 330, y + 90, "#8d5524", 12))
        S.add(ellipse(x + sgn * 330, y + 100, 20, 40, "#8d5524", rot=-sgn * 55))
        S.add(cercle(x + sgn * 180, y - 36, 10, PIVOT))
    S.add(g([trait(x - 330 - k * 40, y + 150, x - 290 - k * 40, y + 150, "#e7f5ff", 4) for k in range(3)]))
    return S


def p15():
    S = Scene()
    pre(S, 15)
    b = Bascule(400, 740, 350, 0)
    S.add(b.dessin())
    S.add(b.assis(-330, lambda x, y: souris(x, y, 0.65, expr="rire", bras="haut")))
    S.add(b.assis(-270, lambda x, y: perso("lapin", x, y, 0.6, expr="rire")))
    S.add(b.assis(-200, lambda x, y: perso("renard", x, y, 0.6, expr="content")))
    S.add(b.assis(40, lambda x, y: elephant(x, y, 1.05, expr="rire", bras="haut")))
    S.add(b.assis(250, lambda x, y: perso("herisson", x, y, 0.6, expr="content")))
    S.add(b.assis(320, lambda x, y: chouette(x, y, 0.55, expr="rire")))
    return S


def p16():
    S = Scene()
    pre(S, 16, "#ff922b", "#ffe8cc")
    S.add(cercle(640, 600, 70, "#ffd43b"))
    collines(S, 620, "#b2f2bb", graine=36)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=710)
    b = Bascule(400, 740, 330, 12)
    S.add(b.dessin())
    S.add(b.assis(-300, lambda x, y: souris(x, y, 0.8, expr="rire", bras="haut", pieds_haut=True)))
    S.add(b.assis(60, lambda x, y: elephant(x, y, 1.2, expr="rire", bras="haut")))
    S.add(texte(190, 200, "Hop !", 60, "#fff", contour="#e8590c"), texte(560, 300, "Hop !", 50, "#fff", contour="#e8590c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("amis-seuls.svg", vignette),
    ("01-qui-veut-jouer.svg", p01), ("02-trop-lourd.svg", p02), ("03-les-amis.svg", p03), ("04-une-idee.svg", p04),
    ("05-vers-le-milieu.svg", p05), ("06-equilibre.svg", p06), ("07-levier.svg", p07), ("08-rocher.svg", p08),
    ("09-outils.svg", p09), ("10-brouette.svg", p10), ("11-ciseaux.svg", p11), ("12-balance.svg", p12),
    ("13-mobile.svg", p13), ("14-rames.svg", p14), ("15-tous-ensemble.svg", p15), ("16-hop.svg", p16),
]
