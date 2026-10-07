"""Le petit son qui voulait voyager — comment le son se propage.

Ding naît d'une sonnette qui vibre. Il voyage de proche en proche dans
l'air (l'air pousse l'air d'à côté), fait vibrer le tympan, s'affaiblit en
s'éloignant, va plus de quatre fois plus vite dans l'eau, suit une ficelle
tendue (pas une ficelle molle), traverse un mur (étouffé) et le bois d'une
table, mais ne peut pas voyager dans le vide de l'espace.
"""
from base import *
from objets import *
from sciences import *
from fantastique import personne
from histoires.baleine_bosse import baleine
from histoires.pompon_sons import tambour, baguette

ID = "son-voyage"
JAUNE = "#fcc419"
LUCIE = dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#e64980", robe=False, jambes="#5f3dc4")
HUGO = dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#20c997", robe=False, jambes="#1971c2")


def lucie(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**LUCIE, **k})


def hugo(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**HUGO, **k})


def ding(x, y, s=1.0, expr="rire", regard=(0, 0), direction=0, ondes_=True, pale=False):
    """Ding, le petit son : une boule jaune avec un visage, suivie d'ondes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if ondes_:
        m.append(ondes(0, 0, 52, 3, 20, direction + 180, 90, "#f59f00", 6))
    m += [cercle(0, 0, 40, JAUNE), cercle(-12, -14, 10, "#fff3bf", opacity=0.8),
          ellipse(-22, 10, 7, 4.5, ROSE, opacity=0.8), ellipse(22, 10, 7, 4.5, ROSE, opacity=0.8),
          oeil(-13, -4, ys, regard, taille=0.8), oeil(13, -4, ys, regard, taille=0.8),
          place(sourcils(13, -4, ss), 0, 0) if ss else "", bouche(0, 10, bs, 0.6)]
    return place(g(m, opacity=0.45 if pale else None), x, y, s)


def pot(x, y, s=1.0, flip=False, couleur="#ced4da"):
    """Pot de conserve couché, l'ouverture à gauche (vers la bouche ou l'oreille) ;
    (x, y) = milieu du pot. Le fond, d'où part la ficelle, est à droite."""
    return place([rect(-30, -26, 60, 52, couleur, rx=6), rect(-14, -26, 6, 52, _clair(couleur)), rect(10, -26, 6, 52, _clair(couleur)),
                  ellipse(-30, 0, 8, 26, "#868e96")], x, y, s, flip=flip)


def _clair(c):
    return eclaircir(c, 0.4)


def particules(S, x0, x1, y, nb=9, serre=None):
    """Une rangée de petites boules d'air ; `serre` = index autour duquel elles se tassent."""
    for k in range(nb):
        x = x0 + (x1 - x0) * k / (nb - 1)
        if serre is not None:
            d = k - serre
            x -= 30 * (1 if d > 0 else -1) * math.exp(-0.7 * abs(d)) if d else 0
        S.add(cercle(x, y, 22, "#a5d8ff", stroke="#4dabf7", stroke_width=3))


def jardin(S, haut="#74c0fc", bas="#e7f5ff", y=600, graine=1):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#7bd88a", y2=y + 80)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S, "#74c0fc", "#e7f5ff", 620, 2)
    S.add(velo(220, 740, 1.3, "#e64980"))
    S.add(ding(560, 440, 1.8, regard=(1, 0), direction=0))
    S.add(fleche_courbe("M 330 560 Q 420 440 470 450", (470, 450), 10, "#f59f00", 6))
    S.add(texte(600, 610, "Driiing !", 64, "#f59f00", contour="#fff", rot=-6))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ding(200, 140, 1.8, regard=(1, 0)))
    return S


def p01():
    S = Scene()
    jardin(S, "#74c0fc", "#e7f5ff", 600, 1)
    S.add(maison(680, 600, 0.9, "#ffe8cc", "#5f3dc4"))
    S.add(velo(330, 740, 1.3, "#e64980"))
    S.add(lucie(180, 760, 1.15, expr="rire", bras="donne", regard=(1, 0)))
    S.add(ding(520, 390, 1.2, expr="joie", regard=(-1, 0), direction=0))
    S.add(texte(450, 250, "Driiing !", 70, "#f59f00", contour="#fff", rot=-6))
    return S


def p02():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(texte(400, 110, "L'air pousse l'air d'à côté…", 42, "#1971c2"))
    for k, (y, serre) in enumerate(((260, 1), (450, 4), (640, 7))):
        particules(S, 120, 720, y, 9, serre)
        S.add(ding(120 + 600 * serre / 8, y - 80, 0.75, regard=(1, 0), ondes_=False))
        S.add(fleche(140, y + 50, 700, y + 50, "#f59f00", 4, 14, opacity=0.5))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=600)
    S.add(tapis(450, 700, 260, 50))
    S.add(perso("chat", 470, 720, 1.4, expr="surpris", regard=(-1, 0), bras="joues"))
    S.add(ding(220, 420, 1.1, regard=(1, 0), direction=0))
    # zoom sur le tympan qui tremble
    S.add(cercle(650, 220, 110, "#ffffff", stroke="#495057", stroke_width=6))
    S.add(chemin("M 590 160 Q 560 220 600 290", stroke="#ffa94d", sw=24))
    for k in range(3):
        S.add(chemin(f"M {660 + k * 10} 170 Q {640 + k * 10 + (12 if k % 2 else -12)} 220 {660 + k * 10} 270", stroke="#ff8787", sw=5, opacity=1 - k * 0.3))
    S.add(ondes(590, 220, 20, 2, 16, 0, 80, "#f59f00", 4))
    S.add(texte(650, 370, "le tympan tremble", 30, "#495057", contour="#fff"))
    S.add(bulle(150, 140, 230, 76, "Miaou ?", 40, pointe=(400, 470)))
    return S


def p04():
    S = Scene()
    jardin(S, "#74c0fc", "#e7f5ff", 560, 3)
    for k, (x, sc, pale) in enumerate(((150, 1.2, False), (400, 0.85, False), (640, 0.55, True))):
        S.add(ding(x, 380, sc, expr=("rire", "sourire", "baille")[k], regard=(1, 0), pale=pale))
    S.add(texte(150, 250, "DING !", 54, "#f59f00", contour="#fff"))
    S.add(texte(400, 280, "Ding !", 40, "#f59f00", contour="#fff"))
    S.add(texte(640, 300, "ding…", 28, "#f59f00", contour="#fff", poids=600))
    S.add(arbre(700, 720, 0.8), buisson(80, 740, 1.0))
    S.add(perso("lapin", 640, 760, 0.9, expr="inquiet", bras="joues", regard=(-1, 0)))
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 220, 800, 580, S.degrade(["#4dabf7", "#1864ab"])))
    S.add(chemin("M 0 220 " + " ".join(f"q 25 -12 50 0" for _ in range(16)), stroke="#d0ebff", sw=6))
    S.add(baleine(560, 560, 0.55, flip=True, chante=True))
    S.add(ding(240, 420, 1.0, regard=(1, 0), direction=0))
    S.add(mouvement(150, 420, 1.2, "#d0ebff"))
    S.add(texte(250, 320, "4 fois plus vite !", 44, "#ffffff", contour="#1864ab"))
    S.add(cercle(120, 680, 10, "#d0ebff", opacity=0.6), cercle(140, 640, 7, "#d0ebff", opacity=0.6))
    return S


def _telephone(S, tendue=True, expr_hugo="bouche_bee"):
    jardin(S, "#74c0fc", "#e7f5ff", 600, 4)
    a, b = (258, 622), (552, 598)
    if tendue:
        S.add(trait(a[0], a[1], b[0], b[1], "#c68642", 4))
    else:
        S.add(chemin(f"M {a[0]} {a[1]} Q 405 800 {b[0]} {b[1]}", stroke="#c68642", sw=4))
    S.add(lucie(140, 760, 1.15, expr="chante", bras="donne2", regard=(1, 0)))
    S.add(pot(222, 622, 1.2))
    S.add(hugo(670, 760, 1.15, expr=expr_hugo, bras="donne2", flip=True, regard=(-1, 0)))
    S.add(pot(588, 598, 1.2, flip=True))


def p06():
    S = Scene()
    _telephone(S, True)
    S.add(ding(405, 520, 0.75, regard=(1, 0), direction=0))
    S.add(texte(410, 420, "bien tendue !", 40, "#2f9e44", contour="#fff"))
    return S


def p07():
    S = Scene()
    _telephone(S, False, "inquiet")
    S.add(ding(330, 690, 0.7, expr="oups", regard=(1, 1), ondes_=False))
    S.add(texte(560, 380, "?", 90, "#495057", contour="#fff"))
    S.add(texte(410, 250, "molle…", 50, "#e03131", contour="#fff"))
    return S


def p08():
    S = Scene()
    S.add(rect(0, 0, 400, 800, "#fff0f6"), rect(400, 0, 400, 800, "#e6fcf5"))
    S.add(rect(0, 600, 800, 200, "#e8c39e"))
    S.add(rect(380, 0, 40, 800, "#ced4da"))
    for k in range(0, 800, 40):
        S.add(trait(380, k, 420, k + 20, "#adb5bd", 2))
    S.add(tambour(200, 700, 0.8, vibre=True))
    S.add(lucie(110, 770, 1.0, expr="rire", bras="haut", objet=g([baguette(-70, -165, 0.6, -30), baguette(70, -165, 0.6, 30)])))
    S.add(ding(400, 330, 0.8, regard=(1, 0), direction=0))
    voisine = personne(630, 770, 1.15, peau="claire", cheveux="gris", coiffure="chignon", habit="#1098ad", robe=True,
                       expr="surpris", bras="joues", acc=("lunettes",), regard=(-1, 0))
    S.add(voisine)
    S.add(texte(620, 300, "boum, boum…", 40, "#495057", contour="#fff", poids=600))
    S.add(texte(200, 300, "BOUM !", 60, "#e03131", contour="#fff"))
    return S


def p09():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=620)
    S.add(fenetre(90, 120, 200, 180, rideaux="#ffa8a8"), cadre_mur(560, 160, 140, 110), etagere(560, 330, 220))
    S.add(rect(200, 640, 560, 32, "#c68642", rx=8), rect(230, 672, 26, 110, "#a0693a"), rect(704, 672, 26, 110, "#a0693a"))
    for k in range(4):
        S.add(trait(210, 648 + k * 6, 750, 648 + k * 6, "#a0693a", 1.5, opacity=0.5))
    # Lucie colle l'oreille sur la table, Hugo gratte l'autre bout
    S.add(lucie(130, 775, 1.05, expr="content", regard=(1, 1), rot=14))
    S.add(hugo(690, 790, 1.2, expr="malin", bras="donne2", flip=True, regard=(-1, 1)))
    S.add(mouvement(600, 600, 0.7, rot=0))
    for k in range(3):
        S.add(ding(330 + k * 100, 656, 0.3, regard=(-1, 0), ondes_=False))
    S.add(texte(440, 420, "gratt, gratt…", 46, "#e8590c", contour="#fff"))
    return S


def p10():
    S = Scene()
    fond(S, "#0b1433")
    etoiles(S, 80, 4, zone=(0, 0, 800, 800))
    S.add(lune_phase(620, 640, 130, halo=False))
    S.add(cercle(110, 140, 70, "#1971c2"), chemin("M 60 120 Q 90 90 120 120 Q 150 150 170 120 L 175 160 Q 120 180 70 160 Z", "#2f9e44"))
    S.add(astronaute(320, 600, 1.0, expr="content", bras="salut"))
    S.add(ding(560, 270, 0.9, expr="triste", ondes_=False, regard=(-1, 1)))
    S.add(texte(400, 90, "… silence …", 50, "#ced4da", poids=600))
    return S


def p11():
    S = Scene()
    jardin(S, "#ffc078", "#fff4e6", 600, 5)
    S.add(maison(660, 600, 0.9, "#ffe8cc", "#5f3dc4", lumiere=True))
    S.add(velo(440, 740, 1.2, "#e64980"))
    S.add(lucie(250, 760, 1.15, expr="content", bras="salut", regard=(1, -1)))
    S.add(hugo(110, 760, 1.05, expr="rire"))
    S.add(ding(560, 330, 1.2, expr="content", regard=(-1, 0)))
    S.add(texte(560, 200, "À demain !", 50, "#f59f00", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ding-seul.svg", vignette),
    ("01-driiing.svg", p01), ("02-l-air.svg", p02), ("03-le-tympan.svg", p03),
    ("04-de-plus-en-plus-loin.svg", p04), ("05-dans-l-eau.svg", p05), ("06-la-ficelle.svg", p06),
    ("07-ficelle-molle.svg", p07), ("08-le-mur.svg", p08), ("09-la-table.svg", p09),
    ("10-l-espace.svg", p10), ("11-a-demain.svg", p11),
]
