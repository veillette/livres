"""Ada, la princesse inventrice — essayer, rater, recommencer.

La physique de la poulie, dessinée juste : une poulie fixe accrochée en haut
change seulement le sens de la traction (on tire vers le bas, en s'aidant de
son poids). Avec une deuxième poulie, mobile, accrochée à la cloche, deux
brins de corde portent la charge : il faut tirer deux fois moins fort, mais
tirer deux fois plus de corde. Sur les dessins, la corde part d'un point
fixe de la poutre, descend sous la poulie mobile, remonte sur la poulie fixe
et redescend vers les mains de ceux qui tirent.
"""
from base import *
from base import _assombrir
from objets import *
from fantastique import *
from sciences import fleche
from contes import etabli, marteau
from fables import meule_foin

ID = "ada-inventrice"
ADA = dict(peau="rosee", cheveux="chatain", coiffure="queue", habit="#20c997", robe=False,
           jambes="#5c7cfa", chaussures="#7c4a1e", ceinture="#8d5524", acc=("couronne",))
GARDE = dict(habit="#4c6ef5", jambes="#364fc7", plumet="#fa5252")
CORDE = "#c2995c"
BOIS, BOIS_F = "#c68642", "#8d5524"
PIERRE, PIERRE_F = "#dee2e6", "#ced4da"


# ---------------------------------------------------------------------------
# Personnages
# ---------------------------------------------------------------------------

def _lunettes_protection(sur_yeux=False):
    y = -150 if sur_yeux else -184
    m = [chemin(f"M -52 {y} Q 0 {y - 8} 52 {y}", stroke="#495057", sw=7)]
    for sgn in (-1, 1):
        m.append(cercle(sgn * 20, y, 16, "#495057"))
        m.append(cercle(sgn * 20, y, 11.5, "#a5d8ff", opacity=0.75 if sur_yeux else 1))
        m.append(cercle(sgn * 20 - 4, y - 4, 3.5, "#fff", opacity=0.9))
    return g(m)


def ada(x, y, s=1.0, lunettes="tete", flip=False, **k):
    """La princesse Ada ; lunettes de protection sur la tête ("tete") ou sur les yeux ("yeux")."""
    m = [personne(0, 0, 1.0, **{**ADA, **k})]
    if lunettes:
        m.append(_lunettes_protection(lunettes == "yeux"))
    return place(m, x, y, s, flip=flip)


def garde(x, y, s=1.0, **k):
    return chevalier(x, y, s, **{**GARDE, **k})


# ---------------------------------------------------------------------------
# Objets et machines
# ---------------------------------------------------------------------------

def cloche(x, y, s=1.0, rot=0, battant=0):
    """Grosse cloche de bronze ; (x, y) = anneau du haut. Hauteur ≈ 150."""
    m = [cercle(0, 6, 12, "none", stroke="#a06d00", stroke_width=7),
         place([cercle(0, 150, 14, "#7a5200"), trait(0, 40, 0, 140, "#7a5200", 6)], rot=battant),
         chemin("M -42 22 Q -46 70 -62 110 Q -78 132 -84 142 L 84 142 Q 78 132 62 110 Q 46 70 42 22 Q 0 4 -42 22 Z", "#f59f00"),
         rect(-88, 132, 176, 16, "#e67700", rx=8),
         chemin("M -46 54 Q 0 44 46 54", stroke="#e67700", sw=5),
         chemin("M -24 34 Q -30 80 -48 120", stroke="#ffe066", sw=8, opacity=0.6)]
    return place(m, x, y, s, rot=rot)


def poulie(x, y, r=26, crochet=30, chape="#495057"):
    """Poulie ; (x, y) = centre de la roue. Le crochet monte de `crochet` (négatif : vers le bas)."""
    m = []
    if crochet:
        y2 = y - r - crochet if crochet > 0 else y + r - crochet
        m.append(trait(x, y, x, y2, chape, 7))
    m += [cercle(x, y, r + 4, chape), cercle(x, y, r - 2, "#adb5bd"), cercle(x, y, r - 9, "#868e96"),
          cercle(x, y, r - 12, "#adb5bd"), cercle(x, y, 5, ENCRE)]
    return g(m)


def corde(d, sw=6):
    return chemin(d, stroke=CORDE, sw=sw)


def palan(xf, yf, ym, r=26, ancre_y=None, tire=None):
    """Poulie fixe en (xf, yf), poulie mobile sous elle à la hauteur ym.

    La corde part de la poutre (ancre_y), descend sous la poulie mobile,
    remonte sur la poulie fixe et redescend vers `tire` (x, y).
    Renvoie (dessin, (x, y) du crochet de la charge)."""
    xm = xf - 2 * r
    ancre_y = yf - r - 30 if ancre_y is None else ancre_y
    tx, ty = tire if tire else (xf + r, ym + 200)
    m = [corde(f"M {xm - r} {ancre_y} L {xm - r} {ym} A {r} {r} 0 0 0 {xm + r} {ym} L {xm + r} {yf} "
               f"A {r} {r} 0 0 1 {xf + r} {yf} L {tx} {ty}"),
         poulie(xf, yf, r, crochet=30), poulie(xm, ym, r, crochet=-22)]
    return g(m), (xm, ym + r + 22)


def catapulte(x, y, s=1.0, bras_rot=-10, casse=False, charge=None):
    """Catapulte en bois ; (x, y) = milieu au sol."""
    m = [rect(-140, -60, 280, 30, BOIS, rx=6), cercle(-100, -24, 26, BOIS_F), cercle(100, -24, 26, BOIS_F),
         cercle(-100, -24, 9, "#495057"), cercle(100, -24, 9, "#495057"),
         poly([(-30, -60), (0, -140), (30, -60)], BOIS_F), cercle(0, -134, 9, "#495057")]
    bras = [rect(-170, -8, 200, 16, BOIS, rx=6), chemin("M -200 -30 Q -200 8 -160 8 Q -150 -10 -150 -30", "#a0522d")]
    if charge:
        bras.append(charge)
    if casse:
        m.append(place([rect(-90, -8, 120, 16, BOIS, rx=6)], 0, -134, rot=-25))
        m.append(place([rect(-60, -8, 70, 16, BOIS, rx=6), chemin("M -90 -30 Q -90 8 -50 8 Q -40 -10 -40 -30", "#a0522d")], -170, -40, rot=30))
    else:
        m.append(place(bras, 0, -134, rot=bras_rot))
    return place(m, x, y, s)


def cle_molette(x, y, s=1.0, rot=0):
    m = [rect(-8, 0, 16, 90, "#868e96", rx=6),
         chemin("M -24 0 L -24 -36 L -8 -36 L -8 -14 L 8 -14 L 8 -36 L 24 -36 L 24 0 Z", "#868e96"),
         cercle(0, 70, 5, "#495057")]
    return place(m, x, y, s, rot=rot)


def engrenage(x, y, r=40, couleur="#adb5bd", dents=10, rot=0):
    m = []
    for k in range(dents):
        a = k * 360 / dents
        m.append(place(rect(-r * 0.16, -r - 10, r * 0.32, 20, couleur, rx=3), rot=a))
    m += [cercle(0, 0, r, couleur), cercle(0, 0, r * 0.35, _assombrir(couleur, 0.8))]
    return place(m, x, y, 1.0, rot=rot)


def ressort(x, y, s=1.0, couleur="#868e96"):
    d = "M 0 0 " + " ".join(f"l 20 -8 l -20 -8" for _ in range(5))
    return place([chemin(d, stroke=couleur, sw=5)], x, y, s)


def plan_mur(x, y, w=200, h=150, contenu=""):
    """Feuille de plan bleue punaisée au mur ; (x, y) = coin haut gauche."""
    return g([rect(x, y, w, h, "#d0ebff", stroke="#74c0fc", stroke_width=3), contenu,
              cercle(x + 12, y + 12, 6, "#fa5252"), cercle(x + w - 12, y + 12, 6, "#fa5252")])


def croquis_poulies(x, y, s=1.0, couleur="#1971c2"):
    """Petit schéma au trait : deux poulies et une cloche."""
    m = [trait(-60, -60, 60, -60, couleur, 4), cercle(20, -40, 14, "none", stroke=couleur, stroke_width=3),
         cercle(-8, 10, 14, "none", stroke=couleur, stroke_width=3),
         chemin("M -22 -60 L -22 10 A 14 14 0 0 0 6 10 L 6 -40 A 14 14 0 0 1 34 -40 L 50 40", stroke=couleur, sw=3),
         chemin("M -8 24 L -8 34 M -26 70 Q -24 36 -8 34 Q 8 36 10 70 Z", couleur, stroke=couleur, sw=3)]
    return place(m, x, y, s)


def ballon_tendu(x0, y0, x1, y1, couleur):
    """Ballon dont le fil part de (x0, y0) ; le ballon est en (x1, y1)."""
    return g([trait(x0, y0, x1, y1 + 56, "#495057", 2), ellipse(x1, y1, 38, 46, couleur),
              ellipse(x1 - 14, y1 - 16, 8, 14, "#fff", opacity=0.45, rot=-20)])


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def cour(S, sol_y=660, soir=False, mur=True):
    """Cour du château : ciel, remparts, pavés."""
    if soir:
        ciel(S, "#364fc7", "#9775fa")
        etoiles(S, 18, graine=4, zone=(0, 0, 800, 250))
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(nuage(140, 100, 0.6), nuage(470, 70, 0.45))
    if mur:
        S.add(rect(0, 380, 800, sol_y - 380, PIERRE))
        for k in range(17):
            S.add(rect(k * 50, 352, 30, 30, PIERRE))
        for row in range(int((sol_y - 380) / 46)):
            for k in range(9):
                S.add(rect(-30 + k * 100 + (row % 2) * 50, 392 + row * 46, 90, 36, PIERRE_F, rx=6))
    S.add(rect(0, sol_y, 800, 800 - sol_y, "#e9d8c4"))
    for row in range(4):
        for k in range(10):
            S.add(rect(-20 + k * 90 + (row % 2) * 45, sol_y + 12 + row * 36, 80, 26, "#dcc5a8", rx=8))


def clocher(x, y, w=220, h=560, cloche_=True, poutre=None, battant=0):
    """Tour du clocher ; (x, y) = milieu de la base. L'arcade est en haut.
    poutre = longueur d'une poutre qui dépasse à gauche, en haut de l'arcade."""
    top = y - h
    m = [rect(x - w / 2, top, w, h, "#e5dbff"),
         poly([(x - w / 2 - 24, top + 4), (x, top - 150), (x + w / 2 + 24, top + 4)], "#e64980"),
         trait(x, top - 150, x, top - 196, "#495057", 4), poly([(x, top - 196), (x + 40, top - 184), (x, top - 172)], "#fab005")]
    for k in range(7):
        m.append(rect(x - w / 2 + (k % 2) * 90 + 14, top + 240 + k * 44, 60, 16, "#d0bfff", rx=4))
    ax0, ax1, ay0, ay1 = x - w / 2 + 34, x + w / 2 - 34, top + 30, top + 210
    m.append(chemin(f"M {ax0} {ay1} L {ax0} {ay0 + 60} Q {x} {ay0 - 30} {ax1} {ay0 + 60} L {ax1} {ay1} Z", "#3b3355"))
    m.append(rect(x - w / 2 + 20, ay1, w - 40, 14, "#d0bfff", rx=4))
    m.append(rect(ax0, ay0 + 40, ax1 - ax0, 12, BOIS_F))
    if cloche_:
        m.append(cloche(x, ay0 + 40, 0.75, battant=battant))
    if poutre:
        m.append(rect(x - w / 2 - poutre, top + 6, poutre + w / 2, 18, BOIS, rx=4))
    return g(m)


def atelier(S, soir=False):
    interieur(S, "#ffe8cc" if not soir else "#5f4b8b", "#d9a066" if not soir else "#8d6a4a", y=600, papier="#ffd8a8" if not soir else None)
    # tableau à outils
    S.add(rect(40, 110, 300, 200, "#a0522d", rx=8), rect(52, 122, 276, 176, "#d9a066", rx=4))
    S.add(marteau(90, 280, 0.9), cle_molette(160, 160, 0.9), place(rect(-6, -60, 12, 120, "#495057", rx=4), 230, 210, rot=20))
    S.add(engrenage(290, 180, 26, "#fab005"), engrenage(270, 250, 18, "#adb5bd", 8))
    S.add(etagere(640, 220, 240), engrenage(580, 192, 22, "#74c0fc", 9), ressort(650, 216, 1.0),
          rect(700, 170, 50, 50, "#ff8787", rx=6))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cour(S)
    S.add(clocher(690, 670, 200, 540, cloche_=False, poutre=330))
    dessin, (cx, cy) = palan(330, 180, 330, r=22, ancre_y=140, tire=(411, 536))
    S.add(cloche(cx, cy, 0.8), dessin)
    S.add(engrenage(110, 300, 40, "#fab005"), engrenage(175, 250, 26, "#adb5bd", 8, rot=15))
    S.add(ada(520, 770, 1.6, expr="rire", bras="tient", flip=True, regard=(-1, -1)))
    S.add(fleche(190, 520, 190, 430, "#2f9e44", sw=8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 140, 160, 110, "#e6fcf5"))
    S.add(engrenage(110, 110, 40, "#fab005"), engrenage(170, 175, 26, "#adb5bd", 8, rot=10))
    S.add(trait(260, 30, 260, 70, "#495057", 7), poulie(260, 100, 34, crochet=0))
    S.add(corde("M 226 100 L 226 230"), corde("M 294 100 L 294 200"))
    S.add(cloche(294, 196, 0.35))
    return S


def p01():
    S = Scene()
    atelier(S)
    S.add(etabli(560, 740, 360))
    S.add(engrenage(470, 586, 24, "#fab005"), ressort(560, 600, 1.0), catapulte(660, 600, 0.35))
    S.add(ada(260, 760, 1.6, expr="content", bras="tient", objet=cle_molette(68, -146, 0.8, rot=20)))
    return S


def p02():
    S = Scene()
    cour(S)
    S.add(clocher(620, 670, 220, 560, cloche_=False))
    S.add(corde("M 600 300 Q 590 340 610 360"), corde("M 640 300 Q 650 330 636 350"))
    S.add(cloche(470, 520, 1.1, rot=-15))
    S.add(roi(200, 760, 1.5, expr="inquiet", bras="joues"))
    S.add(bulle(240, 170, 420, 110, "Il faut la remettre\nlà-haut pour la fête !", 34, pointe=(220, 440)))
    S.add(mouvement(400, 640, 1.0))
    return S


def p03():
    S = Scene()
    cour(S)
    S.add(clocher(660, 670, 200, 560, cloche_=False))
    S.add(garde(230, 770, 1.4, expr="concentre", bras="large", regard=(1, 0)))
    S.add(garde(570, 770, 1.4, expr="oups", bras="large", regard=(-1, 0)))
    S.add(cloche(400, 560, 1.35))
    S.add(goutte(170, 520, 0.9), goutte(630, 510, 0.9), goutte(650, 540, 0.6))
    S.add(texte(400, 120, "Ho hisse !", 64, "#fff", contour="#364fc7"))
    return S


def p04():
    S = Scene()
    cour(S)
    S.add(catapulte(560, 740, 1.2, bras_rot=-10, charge=cloche(-180, -110, 0.6)))
    S.add(ada(130, 760, 1.4, expr="rire", bras="salut"))
    S.add(bulle(240, 160, 360, 100, "J'ai une idée !", 44, pointe=(150, 440)))
    S.add(garde(700, 650, 0.9, expr="surpris", bras="bas"))
    return S


def p05():
    S = Scene()
    cour(S)
    S.add(meule_foin(600, 760, 1.2))
    S.add(cloche(620, 520, 0.8, rot=160))
    S.add(catapulte(250, 760, 1.0, casse=True))
    S.add(chemin("M 250 520 Q 420 300 600 470", stroke="#495057", sw=4, stroke_dasharray="14 12"))
    S.add(texte(560, 250, "BONG !", 70, "#fff", contour="#e67700", rot=-8))
    S.add(ada(110, 790, 1.2, expr="oups", bras="joues"))
    S.add(bulle(240, 150, 420, 110, "Raté ! Mais j'ai appris\nquelque chose…", 32, pointe=(140, 520)))
    return S


def p06():
    S = Scene()
    cour(S)
    S.add(cloche(470, 590, 1.1))
    for k, (bx, by, c) in enumerate([(380, 330, "#fa5252"), (440, 290, "#ffd43b"), (500, 300, "#4dabf7"),
                                     (560, 340, "#69db7c"), (420, 400, "#cc5de8"), (530, 400, "#ff922b")]):
        S.add(ballon_tendu(470, 600, bx, by, c))
    S.add(ballon_air(700, 260, 0.6, "#f06595"), ballon_air(620, 150, 0.5, "#4dabf7"), ballon_air(740, 120, 0.45, "#ffd43b"))
    S.add(ada(180, 770, 1.5, expr="oups", bras="bouche", regard=(1, -1)))
    S.add(texte(260, 120, "Elle ne bouge pas !", 46, "#fff", contour="#ae3ec9"))
    return S


def p07():
    S = Scene()
    atelier(S, soir=True)
    S.add(fenetre(470, 80, 160, 140, dehors="#364fc7", nuit_=True))
    S.add(etabli(560, 760, 360))
    S.add(catapulte(580, 620, 0.3, casse=True), ballon_air(650, 620, 0.35, "#fa5252", fil=80))
    S.add(lampe(710, 620, 0.6))
    S.add(ada(250, 760, 1.6, expr="triste", bras="joues", lunettes=None))
    S.add(place(_lunettes_protection(), 470, 778, 0.9))
    return S


def puits_poulie(x, y, s=1.0, seau_y=-250):
    """Puits de pierre avec sa poulie ; (x, y) = milieu au sol."""
    m = [rect(-130, -130, 260, 130, "#ced4da", rx=10)]
    for row in range(3):
        for k in range(5):
            m.append(rect(-130 + k * 56 + (row % 2) * 28, -126 + row * 42, 50, 36, "#adb5bd", rx=8))
    m += [ellipse(0, -130, 130, 26, "#868e96"), ellipse(0, -130, 110, 18, "#343a40"),
          rect(-120, -370, 16, 240, BOIS_F, rx=4), rect(104, -370, 16, 240, BOIS_F, rx=4),
          poly([(-150, -360), (0, -440), (150, -360)], "#c92a2a"), rect(-124, -350, 248, 14, "#a0522d", rx=6),
          poulie(0, -300, 28, crochet=22),
          corde(f"M -28 -300 L -28 {seau_y}"),
          corde("M 28 -300 L 117 -53"),
          chemin(f"M -58 {seau_y + 10} L -48 {seau_y + 70} L -8 {seau_y + 70} L 2 {seau_y + 10} Z", "#868e96"),
          chemin(f"M -58 {seau_y + 10} Q -28 {seau_y - 20} 2 {seau_y + 10}", stroke="#495057", sw=4),
          ellipse(-28, seau_y + 12, 30, 7, "#74c0fc")]
    return place(m, x, y, s)


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(620, 100, 0.6))
    sol(S, 620, "#8ce99a")
    S.add(arbre(720, 640, 1.0))
    S.add(puits_poulie(330, 720, 1.1))
    S.add(ada(560, 760, 1.4, expr="bouche_bee", bras="tire", flip=True, regard=(-1, -1)))
    S.add(eclat(560, 330, 1.4, "#ffd43b"), texte(560, 350, "!", 70, "#fab005"))
    S.add(fleche(230, 520, 230, 420, "#2f9e44", sw=8), fleche(400, 470, 430, 560, "#e03131", sw=8))
    return S


def p09():
    S = Scene()
    atelier(S)
    S.add(plan_mur(420, 70, 240, 170, croquis_poulies(540, 160, 1.0)))
    S.add(etabli(470, 770, 380))
    S.add(poulie(380, 600, 34, crochet=0), poulie(480, 610, 30, crochet=0))
    S.add(chemin("M 560 620 q 30 -30 60 0 q 30 30 60 0 q 30 -30 40 -10", stroke=CORDE, sw=8))
    S.add(ada(200, 770, 1.55, expr="concentre", bras="tient", lunettes="yeux", objet=marteau(68, -146, 0.8, rot=30)))
    S.add(texte(130, 110, "Tac tac !", 44, "#fff", contour="#e8590c", rot=-8))
    return S


def p10():
    S = Scene()
    cour(S, sol_y=680)
    S.add(clocher(660, 690, 220, 600, cloche_=False, poutre=360))
    dessin, (cx, cy) = palan(390, 150, 360, r=24, ancre_y=110, tire=(442, 706))
    S.add(cloche(cx, cy, 0.9))
    S.add(dessin)
    S.add(corde("M 442 706 L 720 716"))
    S.add(garde(715, 790, 1.0, expr="concentre", bras="tire", flip=True, regard=(-1, -1)))
    S.add(garde(630, 790, 1.0, expr="souffle", bras="tire", flip=True, regard=(-1, -1)))
    S.add(ada(540, 790, 1.2, expr="concentre", bras="tire", flip=True, regard=(-1, -1)))
    S.add(fleche(230, 620, 230, 520, "#2f9e44", sw=8))
    S.add(texte(160, 110, "Ho hisse !", 52, "#fff", contour="#0ca678"))
    return S


def p11():
    S = Scene()
    cour(S)
    S.add(clocher(400, 660, 240, 560, cloche_=True, battant=14))
    S.add(texte(150, 210, "DING !", 56, "#fff", contour="#e67700", rot=-10))
    S.add(texte(650, 230, "DONG !", 56, "#fff", contour="#e67700", rot=10))
    for k in range(18):
        r = random.Random(k)
        S.add(place(rect(-6, -9, 12, 18, r.choice(["#fa5252", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8"])),
                    r.uniform(40, 760), r.uniform(60, 330), rot=r.randint(0, 80)))
    S.add(roi(110, 780, 1.1, expr="rire", bras="applaudit"))
    S.add(reine(690, 780, 1.1, expr="rire", bras="applaudit"))
    S.add(garde(230, 790, 0.95, expr="rire", bras="ouverts"), garde(570, 790, 0.95, expr="rire", bras="ouverts"))
    S.add(ada(400, 790, 1.45, expr="fier", bras="haut"))
    return S


def p12():
    S = Scene()
    cour(S, sol_y=680)
    # grand tableau au mur
    S.add(rect(240, 40, 520, 420, "#2b8a3e", rx=10, stroke=BOIS_F, stroke_width=14))
    S.add(trait(320, 90, 560, 90, "#fff", 6))
    dessin, (cx, cy) = palan(470, 140, 300, r=24, ancre_y=90, tire=(494, 430))
    S.add(dessin, cloche(cx, cy, 0.55))
    S.add(fleche(540, 330, 540, 430, "#ffd43b", sw=7), texte(640, 390, "on tire", 32, "#ffd43b"))
    S.add(fleche(340, 420, 340, 340, "#ffc9c9", sw=7), texte(340, 450, "ça monte", 30, "#ffc9c9"))
    S.add(texte(620, 200, "2 fois", 34, "#fff"), texte(620, 240, "moins fort !", 34, "#fff"))
    S.add(ada(150, 790, 1.5, expr="content", bras="montre", regard=(1, -1)))
    S.add(garde(620, 790, 1.0, expr="bouche_bee", bras="bas", regard=(-1, -1)))
    S.add(personne(470, 790, 0.85, peau="brune", cheveux="noir", coiffure="tresses", habit="#ff922b",
                   expr="content", bras="bas", regard=(-1, -1)))
    S.add(personne(730, 790, 0.8, peau="claire", cheveux="blond", coiffure="courts", habit="#74c0fc",
                   robe=False, expr="surpris", bras="bas", regard=(-1, -1)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("poulie.svg", vignette),
    ("01-l-atelier.svg", p01), ("02-la-cloche-tombee.svg", p02), ("03-ho-hisse.svg", p03),
    ("04-catapulte.svg", p04), ("05-bong.svg", p05), ("06-ballons.svg", p06),
    ("07-decouragee.svg", p07), ("08-le-puits.svg", p08), ("09-deux-poulies.svg", p09),
    ("10-ca-monte.svg", p10), ("11-ding-dong.svg", p11), ("12-comment-ca-marche.svg", p12),
]
