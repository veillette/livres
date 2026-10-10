"""Au revoir, la couche ! — Lapinou apprend à aller sur le pot.

Lapinou regarde les grands aller aux toilettes. Il choisit son pot (jaune, à
étoiles), y assoit d'abord son doudou, essaie lui-même… rien. Un petit
accident : « Ce n'est pas grave, on essaie encore. » Puis il sent l'envie,
court, et réussit ! Il vide le pot, tire la chasse, se lave les mains, met
une culotte de grand. La nuit, une couche encore : ça viendra plus tard. Et
un jour, il dit au revoir aux couches.

Plans : 1 moyen (les grands vont aux toilettes) · 2 moyen (mon pot !) ·
3 gros plan (assis, Doudou !) · 4 moyen (rien…) · 5 moyen (oups) · 6 large
(vite, vite !) · 7 moyen (j'ai réussi !) · 8 moyen (glouglou, on se lave
les mains) · 9 gros plan (la culotte de grand) · 10 large (au parc) · 11
moyen (la nuit) · 12 moyen (au revoir, la couche !).
"""
from base import *
from base import _assombrir
from objets import tour_cubes

ID = "lapinou-pot"

LAPINOU = dict(habit="#4dabf7")
PAPA = dict(couleur="#d9c2a5", habit="#69db7c", acc=("lunettes",))
MAMAN = dict(couleur="#e9ecef", habit="#f783ac", acc=("fleur",))
LILI = dict(couleur="#d9c2a5", habit="#cc5de8", acc=("noeud",))
JAUNE = "#ffd43b"


def lapinou(x, y, s=1.25, **k):
    return perso("lapin", x, y, s, **{**LAPINOU, **k})


def papa(x, y, s=1.7, **k):
    return perso("lapin", x, y, s, **{**PAPA, **k})


def maman(x, y, s=1.65, **k):
    return perso("lapin", x, y, s, **{**MAMAN, **k})


def pot(x, y, s=1.0, couleur=JAUNE, etoiles=True):
    """Le pot vu de face ; (x, y) = au sol."""
    m = [ellipse(0, -4, 84, 11, "#000", opacity=0.1),
         chemin("M -78 -56 Q -74 -4 0 -2 Q 74 -4 78 -56 Z", volume(couleur, 0.3, 0.8)),
         ellipse(-80, -50, 12, 8, _assombrir(couleur, 0.85)), ellipse(80, -50, 12, 8, _assombrir(couleur, 0.85)),
         ellipse(0, -58, 82, 18, eclaircir(couleur, 0.3)), ellipse(0, -58, 60, 10, _assombrir(couleur, 0.75)),
         chemin("M -26 -62 Q 0 -96 26 -62 Z", volume(couleur, 0.3, 0.8))]
    if etoiles:
        for px, py in ((-40, -30), (0, -20), (38, -32)):
            m.append(place(etoile5(0, 0, 9, "#fff"), px, py))
    return place(m, x, y, s)


def toilettes(x, y, s=1.0):
    """Toilettes vues de face ; (x, y) = au sol."""
    m = [rect(-60, -260, 120, 90, volume("#ffffff", 0.05, 0.86), rx=12, stroke="#dee2e6", stroke_width=3),
         rect(-14, -276, 28, 12, "#ced4da", rx=5),
         rect(-30, -150, 60, 150, volume("#ffffff", 0.05, 0.86), rx=20, stroke="#dee2e6", stroke_width=3),
         ellipse(0, -150, 78, 20, "#fff", stroke="#dee2e6", stroke_width=3), ellipse(0, -150, 56, 11, "#e7f5ff")]
    return place(m, x, y, s)


def lavabo(x, y, s=1.0):
    m = [rect(-18, -170, 36, 170, volume("#ffffff", 0.05, 0.86), rx=10, stroke="#dee2e6", stroke_width=3),
         chemin("M -90 -200 L 90 -200 Q 84 -150 0 -146 Q -84 -150 -90 -200 Z", volume("#ffffff", 0.05, 0.86), stroke="#dee2e6", sw=3),
         rect(-8, -236, 16, 36, "#adb5bd", rx=4), chemin("M 0 -236 Q 30 -240 30 -216", stroke="#adb5bd", sw=8),
         rect(50, -218, 30, 18, "#ffa8a8", rx=6)]
    return place(m, x, y, s)


def couche(x, y, s=1.0, rot=0, ailes=False):
    m = []
    if ailes:
        for sgn in (-1, 1):
            m.append(place(chemin("M 0 0 Q 40 -50 80 -30 Q 60 -10 70 10 Q 40 0 0 10 Z", "#e7f5ff", stroke="#a5d8ff", sw=3), sgn * 40, -20, flip=sgn < 0))
    m += [chemin("M -50 -40 L 50 -40 Q 46 10 20 30 L -20 30 Q -46 10 -50 -40 Z", volume("#ffffff", 0.05, 0.85), stroke="#dee2e6", sw=3),
          rect(-60, -44, 26, 16, "#74c0fc", rx=6), rect(34, -44, 26, 16, "#74c0fc", rx=6),
          place(etoile5(0, 0, 8, "#ffd43b"), 0, -8)]
    return place(m, x, y, s, rot=rot)


def culotte(x, y, s=1.0):
    m = [chemin("M -50 -36 L 50 -36 L 46 -6 Q 30 0 18 24 L -18 24 Q -30 0 -46 -6 Z", volume("#fff3bf", 0.2, 0.85), stroke="#fab005", sw=3),
         rect(-50, -40, 100, 10, "#ff922b", rx=4)]
    for px, py in ((-24, -16), (14, -18), (0, 6)):
        m += [poly([(px - 5, py - 6), (px + 5, py - 6), (px, py + 10)], "#ff922b"), trait(px, py - 6, px - 4, py - 14, "#40c057", 3)]
    return place(m, x, y, s)


def salle_de_bain(S):
    interieur(S, "#e3fafc", "#dee2e6", y=600)
    for yy in range(40, 600, 56):
        S.add(trait(0, yy, 800, yy, "#c5f6fa", 3))
    for xx in range(40, 800, 56):
        S.add(trait(xx, 0, xx, 600, "#c5f6fa", 3))
    S.add(rect(0, 600, 800, 200, lineaire([(0, "#e9ecef"), (1, "#ced4da")])))
    for xx in range(0, 800, 80):
        S.add(trait(xx, 600, xx - 40, 800, "#dee2e6", 2))


def maison(S):
    interieur(S, "#fff9db", "#d9b48f", y=590, papier="#ffec99")
    S.add(fenetre(560, 110, 170, 160, "#a5d8ff", rideaux="#b2f2bb"))
    S.add(tapis(400, 730, 300, 56, "#d3f9d8", "#69db7c"))


def assis_sur_le_pot(S, x, y, s=1.25, **k):
    """Lapinou assis sur son pot : le pot cache ses jambes, ses pieds dépassent devant."""
    S.add(lapinou(x, y - 26 * s, s, **k))
    S.add(pot(x, y, s * 1.05))
    S.add(ellipse(x - 34 * s, y - 6 * s, 22 * s, 12 * s, "#dee2e6"), ellipse(x + 34 * s, y - 6 * s, 22 * s, 12 * s, "#dee2e6"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#e7f5ff")
    for k in range(5):
        S.add(nuage(120 + k * 160, 120 + (k % 2) * 60, 0.6))
    S.add(couche(600, 230, 1.3, rot=-12, ailes=True))
    S.add(pot(250, 790, 1.3))
    S.add(lapinou(420, 790, 1.8, expr="rire", bras="salut", regard=(1, -1)))
    S.cachette(630, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pot(270, 262, 0.75))
    S.add(lapinou(140, 262, 0.75, expr="content", bras="designe", regard=(1, 0.4)))
    return S


def p01():
    """Plan moyen : la cousine Lili sort des toilettes, toute fière ; Lapinou, qui a encore une couche, la regarde."""
    S = Scene()
    maison(S)
    S.add(porte(560, 590, 180, 330, "#b5835a", ouverte=True))
    S.add(rect(530, 300, 60, 40, "#fff", rx=6), texte(560, 330, "WC", 26, "#495057"))
    S.add(perso("lapin", 560, 790, 1.45, expr="fier", bras="hanches", regard=(-1, 0.3), **LILI))
    S.add(lapinou(230, 790, 1.3, expr="bouche_bee", bras="bas", regard=(1, -0.3)))
    S.add(bulle(600, 150, 240, 80, "J'ai fini !", 36, pointe=(580, 300)))
    S.add(bulle(220, 330, 220, 80, "Et moi ?", 36, pointe=(230, 450)))
    return S


def p02():
    """Plan moyen : Papa offre un pot jaune à étoiles ; Lapinou le serre dans ses bras : « C'est mon pot ! »"""
    S = Scene()
    maison(S)
    S.add(papa(580, 790, 1.7, expr="content", bras="designe", flip=True, regard=(-1, 0.4)))
    S.add(lapinou(280, 790, 1.4, expr="joie", bras="porte", regard=(1, 0.3), objet=place(pot(0, 0, 0.8), 0, -40)))
    S.add(texte(300, 160, "C'est mon pot !", 54, "#1c7ed6", contour="#fff"))
    return S


def p03():
    """Gros plan : Lapinou assoit son doudou sur le pot : « Assis, Doudou ! »"""
    S = Scene()
    maison(S)
    S.add(pot(520, 790, 1.6))
    S.add(perso("ours", 520, 700, 0.75, expr="content", bras="bas", couleur="#ffa94d"))
    S.add(lapinou(250, 820, 1.6, expr="concentre", bras="designe", regard=(1, 0.3)))
    S.camera(1.15, 400, 560)
    S.dessus(bulle(400, 130, 300, 90, "Assis, Doudou !", 38, pointe=(320, 250)))
    return S


def p04():
    """Plan moyen : dans la salle de bain, Lapinou assis sur son pot regarde un livre… rien."""
    S = Scene()
    salle_de_bain(S)
    S.add(toilettes(620, 760, 1.2), lavabo(170, 760, 1.0))
    assis_sur_le_pot(S, 380, 790, 1.3, expr="neutre", bras="porte", regard=(0, 0.5),
                     objet=g([rect(-60, -110, 120, 76, "#ff8787", rx=6), rect(-2, -110, 4, 76, "#c92a2a")]))
    S.add(texte(400, 140, "… rien.", 60, "#495057", contour="#fff"))
    return S


def p05():
    """Plan moyen : en jouant aux cubes, oups ! une petite flaque ; Maman, calme, apporte la serpillière."""
    S = Scene()
    maison(S)
    S.add(tour_cubes(160, 740, 0.7, 5, graine=3))
    S.add(lapinou(330, 790, 1.35, expr="oups", bras="bouche", regard=(0, 0.6)))
    S.add(ellipse(340, 790, 90, 16, "#a5d8ff", opacity=0.8))
    S.add(maman(600, 790, 1.65, expr="content", bras="tient", flip=True, regard=(-1, 0.4),
                objet=g([trait(68, -230, 68, 40, "#c68642", 8), rect(40, 30, 56, 30, "#74c0fc", rx=8)])))
    S.add(bulle(560, 140, 380, 110, "Ce n'est pas grave.\nOn essaie encore !", 32, pointe=(580, 300)))
    return S


def p06():
    """Plan large : Lapinou court vers la salle de bain : « Vite, vite ! Pipi ! »"""
    S = Scene()
    maison(S)
    S.add(porte(660, 590, 180, 330, "#b5835a", ouverte=True))
    S.add(lapinou(360, 790, 1.4, expr="concentre", bras="court", regard=(1, 0)))
    S.add(mouvement(250, 600, 1.4))
    S.add(texte(360, 160, "Vite, vite ! Pipi !", 54, "#e8590c", contour="#fff"))
    return S


def p07():
    """Plan moyen : Lapinou est assis sur son pot, ravi ; Papa et Maman applaudissent : « J'ai réussi ! »"""
    S = Scene()
    salle_de_bain(S)
    S.add(papa(150, 790, 1.6, expr="rire", bras="applaudit", regard=(1, 0.3)))
    S.add(maman(650, 790, 1.55, expr="joie", bras="applaudit", flip=True, regard=(-1, 0.3)))
    assis_sur_le_pot(S, 400, 790, 1.35, expr="rire", bras="haut", regard=(0, -0.5))
    S.add(texte(400, 140, "J'ai réussi !", 64, "#1c7ed6", contour="#fff"))
    for x, y in ((300, 260), (500, 240), (560, 330), (240, 340)):
        S.add(place(etoile5(0, 0, 18, JAUNE), x, y))
    S.cachette(70, 240, "air")
    return S


def p08():
    """Plan moyen : debout sur le petit tabouret, Lapinou se lave les mains ; il a vidé le pot et tiré la chasse : « Glouglou ! »"""
    S = Scene()
    salle_de_bain(S)
    S.add(toilettes(640, 760, 1.2))
    S.add(texte(650, 360, "Glouglou !", 40, "#1c7ed6", contour="#fff"))
    S.add(rect(240, 660, 180, 50, "#69db7c", rx=10), rect(256, 710, 20, 80, "#40c057"), rect(384, 710, 20, 80, "#40c057"))
    S.add(lapinou(330, 664, 1.3, expr="content", bras="porte", regard=(0, 0.6)))
    S.add(lavabo(330, 790, 1.15))
    for k in range(7):
        S.add(cercle(236 + k * 30, 552 - (k % 2) * 14, 8 + k % 3 * 3, "#fff", stroke="#a5d8ff", stroke_width=2))
    S.add(pot(120, 790, 0.9))
    return S


def p09():
    """Gros plan : Lapinou montre fièrement sa culotte de grand, à motifs de carottes : « Une culotte de grand ! »"""
    S = Scene()
    maison(S)
    S.add(lapinou(400, 860, 1.9, expr="fier", bras="etire", regard=(0, -1)))
    S.add(culotte(400, 400, 1.8))
    S.camera(1.1, 400, 500)
    S.dessus(texte(400, 100, "Une culotte de grand !", 54, "#e8590c", contour="#fff"))
    return S


def p10():
    """Plan large : au parc, Lapinou tire Papa par la main vers les toilettes : « Papa, j'ai envie ! »"""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 470, "#b2f2bb", graine=4)
    S.add(rect(0, 560, 800, 240, terrain("#8ce99a")))
    S.add(arbre(90, 580, 1.0))
    S.add(rect(560, 360, 200, 220, "#ffe8cc"), poly([(540, 370), (660, 300), (780, 370)], "#e8590c"), rect(620, 460, 80, 120, "#b5835a"),
          rect(630, 400, 60, 40, "#fff", rx=6), texte(660, 430, "WC", 26, "#495057"))
    S.add(papa(380, 790, 1.7, expr="rire", bras="main", regard=(1, 0)))
    S.add(lapinou(530, 790, 1.3, expr="concentre", bras="main", flip=True, regard=(1, 0), pas="marche"))
    S.add(bulle(380, 140, 330, 90, "Papa, j'ai envie !", 36, pointe=(500, 330)))
    return S


def p11():
    """Plan moyen : le soir, Lapinou en pyjama, avec une couche pour la nuit, dans son lit ; Maman lui fait un bisou."""
    S = Scene()
    piece(S, "chambre", y=590)
    S.ambiance("nuit")
    S.add(fenetre(120, 110, 150, 150, "#364fc7", nuit_=True))
    S.add(lit(470, 720, 380, "#b2f2bb", "#69db7c"))
    S.add(place(perso("lapin", 0, 0, 1.0, expr="dort", bras="bas", habit="#d0bfff"), 600, 615, 0.8, rot=-90))
    S.add(rect(450, 580, 240, 100, "#69db7c", rx=18))
    S.add(maman(650, 790, 1.5, expr="content", bras="bas", flip=True, regard=(-1, 0.5)))
    S.add(lampe(140, 800, 0.9))
    S.add(zzz(330, 470, 1.0))
    return S


def p12():
    """Plan moyen : Lapinou fait au revoir à un paquet de couches qui s'envole avec des ailes : « Au revoir, la couche ! »"""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 600, 800, 200, terrain("#8ce99a")))
    S.add(nuage(160, 140, 0.8), nuage(650, 110, 0.6))
    S.add(couche(560, 260, 1.2, rot=-14, ailes=True), couche(680, 180, 0.7, rot=10, ailes=True))
    S.add(lapinou(170, 790, 1.6, expr="rire", bras="salut", regard=(1, -1)))
    S.add(texte(530, 660, "Au revoir, la couche !", 44, "#1c7ed6", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lapinou-seul.svg", vignette),
    ("01-et-moi.svg", p01), ("02-mon-pot.svg", p02), ("03-doudou.svg", p03),
    ("04-rien.svg", p04), ("05-oups.svg", p05), ("06-vite.svg", p06),
    ("07-j-ai-reussi.svg", p07), ("08-glouglou.svg", p08), ("09-la-culotte.svg", p09),
    ("10-au-parc.svg", p10), ("11-la-nuit.svg", p11), ("12-au-revoir.svg", p12),
]
