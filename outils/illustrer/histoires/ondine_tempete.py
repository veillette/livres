"""Ondine et la tempête — avoir du courage."""
from base import *
from objets import *
from fantastique import *

ID = "ondine-tempete"
# Ondine : petite sirène à la peau brune, aux cheveux noirs bouclés, queue violette
ONDINE = dict(coiffure="boucles", cheveux="noir", peau="brune", habit="#be4bdb",
              sirene=("#be4bdb", "#eebefa"), acc=("fleur",), couleur_acc="#ff8787")
MALO = dict(peau="rosee", cheveux="blond", coiffure="courts", robe=False, habit="#fcc419",
            jambes="#1971c2", chaussures="#1864ab")
PAPA = dict(peau="rosee", cheveux="chatain", coiffure="courts", robe=False, habit="#fcc419",
            jambes="#364fc7", chaussures="#343a40", barbe="#8d5524")
GALET = "#91a7ff"

NUIT_CIEL = ("#1b2559", "#3b4a7d")
NUIT_MER = ("#1d3f6e", "#0b1d38")
ECUME = "#d0ebff"


def ondine(x, y, s=1.0, **k):
    return personne(x, y, s, **{**ONDINE, **k})


def malo(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MALO, **k})


def chien(x, y, s=1.0, **k):
    k.setdefault("couleur", "#e3b57a")
    return perso("chien", x, y, s, **k)


# --- créatures et décors propres au livre -----------------------------------

def dauphin(x, y, s=1.0, couleur=GALET, expr="sourire", flip=False, rot=0):
    """Dauphin de profil, tête à droite ; (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = assombrir(couleur, 0.8)
    m = [chemin("M -104 -2 Q -130 -34 -156 -40 Q -140 -10 -156 22 Q -128 18 -104 6 Z", fonce),
         chemin("M -14 -40 Q 4 -84 34 -90 Q 20 -62 30 -38 Z", fonce),
         chemin("M -112 2 Q -70 -52 30 -44 Q 84 -40 108 -16 L 146 -8 Q 150 4 108 8 Q 64 34 -20 26 Q -80 22 -112 2 Z", couleur),
         chemin("M -60 18 Q 0 30 60 18 Q 90 10 108 8 Q 64 34 -20 26 Q -50 24 -60 18 Z", "#e7f5ff"),
         chemin("M 10 10 Q 0 40 -26 50 Q -6 24 -6 10 Z", fonce),
         chemin("M 112 0 Q 128 6 146 -2", stroke=ENCRE, sw=3),
         ellipse(96, 2, 8, 5, ROSE, opacity=0.7)]
    m.append(oeil(86, -16, ys, (1, 0), taille=0.9))
    if ss:
        m.append(place(sourcils(8, 0, ss), 78, -16))
    return place(m, x, y, s, flip=flip, rot=rot)


def meduse(x, y, s=1.0, couleur="#fcc2d7", allumee=True, expr="sourire", graine=1):
    """Petite méduse lumineuse ; (x, y) = centre du chapeau."""
    r = random.Random(graine)
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if allumee:
        m += [cercle(0, 10, 80, "#fff3bf", opacity=0.18), cercle(0, 6, 54, "#fff3bf", opacity=0.3)]
    for k in range(5):
        dx = -24 + k * 12
        o = r.uniform(-8, 8)
        m.append(chemin(f"M {dx} 8 Q {dx - 10 + o} 30 {dx} 50 Q {dx + 10} 70 {dx + o} 90", stroke=couleur, sw=5, opacity=0.9))
    m.append(chemin("M -40 10 Q -42 -44 0 -44 Q 42 -44 40 10 Q 30 2 20 10 Q 10 2 0 10 Q -10 2 -20 10 Q -30 2 -40 10 Z", couleur))
    m.append(ellipse(-14, -26, 10, 6, "#fff", opacity=0.6, rot=-30))
    m.append(oeil(-11, -10, ys, (0, 0), taille=0.6) + oeil(11, -10, ys, (0, 0), taille=0.6))
    m.append(place(bouche(0, 0, bs, 0.45), 0, 2))
    return place(m, x, y, s)


def barque(x, y, s=1.0, rot=0, corde=False):
    """Petite barque de pêcheur ; (x, y) = ligne de flottaison."""
    m = [chemin("M -140 -40 L 140 -40 Q 128 18 84 30 L -84 30 Q -128 18 -140 -40 Z", "#c46210"),
         rect(-146, -48, 292, 16, "#8d4a0f", rx=7),
         trait(-128, -10, 128, -10, "#a0522d", 3),
         chemin("M -120 8 Q 0 16 120 8", stroke="#a0522d", sw=3),
         texte(60, 2, "MALO", 26, "#fff3bf")]
    if corde:
        m.append(cercle(146, -40, 8, "none", stroke="#e9c46a", stroke_width=5))
    return place(m, x, y, s, rot=rot)


def dans_barque(x, y, s=1.0, rot=0, corde=False, expr_malo="inquiet", expr_chien="inquiet",
                bras="bas", regard=(0, 0)):
    """Malo et son chien assis dans la barque ; (x, y) = ligne de flottaison."""
    m = [malo(-40, 20, 0.85, expr=expr_malo, bras=bras, regard=regard),
         chien(70, 10, 0.55, expr=expr_chien, regard=regard),
         barque(0, 0, 1.0, corde=corde)]
    return place(m, x, y, s, rot=rot)


def vagues_devant(S, y, couleur, amp=30, longueur=200, decal=0, ecume=None, opacity=None):
    """Bande d'eau ondulée de y jusqu'en bas de la page, posée devant les personnages."""
    d = f"M -40 {y}"
    x = -40 + decal
    k = 0
    while x < S.w + 40:
        h = amp if k % 2 == 0 else -amp * 0.4
        d += f" Q {x + longueur / 2} {y - h} {x + longueur} {y}"
        x += longueur
        k += 1
    d += f" L {S.w + 40} {S.h} L -40 {S.h} Z"
    a = {"opacity": opacity} if opacity else {}
    S.add(chemin(d, couleur, **a))
    if ecume:
        x = -40 + decal
        for k in range(int((S.w + 80) / longueur) + 1):
            if k % 2 == 0:
                S.add(chemin(f"M {x + longueur * 0.2} {y - amp * 0.35} Q {x + longueur / 2} {y - amp * 0.75} {x + longueur * 0.8} {y - amp * 0.35}",
                             stroke=ecume, sw=7, opacity=0.9))
            x += longueur


def grosse_vague(x, y, s=1.0, couleur="#1d3f6e", ecume=ECUME):
    """Vague qui s'enroule ; (x, y) = pied de la vague."""
    m = [chemin("M -220 0 Q -160 -40 -110 -150 Q -60 -260 40 -250 Q 120 -240 140 -180 Q 100 -210 60 -190 "
                "Q 20 -170 40 -120 Q 70 -60 220 0 Z", couleur),
         chemin("M -110 -150 Q -60 -260 40 -250 Q 120 -240 140 -180 Q 110 -200 70 -196", stroke=ecume, sw=12),
         cercle(146, -178, 10, ecume), cercle(160, -160, 7, ecume), cercle(132, -150, 6, ecume)]
    return place(m, x, y, s)


def eclair(x, y, s=1.0):
    return place(poly([(0, 0), (-30, 90), (-6, 90), (-34, 190), (40, 64), (12, 64), (36, 0)], "#ffe066",
                      stroke="#fff3bf", stroke_width=4), x, y, s)


def phare(x, y, s=1.0, allume=True):
    m = []
    if allume:
        m += [poly([(0, -330), (-320, -400), (-320, -260)], "#fff3bf", opacity=0.35),
              poly([(0, -330), (320, -400), (320, -260)], "#fff3bf", opacity=0.35)]
    m += [poly([(-50, 0), (-30, -300), (30, -300), (50, 0)], "#fff"),
          poly([(-46, -60), (-42, -120), (42, -120), (46, -60)], "#e03131"),
          poly([(-38, -180), (-35, -240), (35, -240), (38, -180)], "#e03131"),
          rect(-44, -306, 88, 14, "#495057", rx=4),
          rect(-28, -360, 56, 56, "#ffe066" if allume else "#adb5bd", stroke="#495057", stroke_width=5),
          poly([(-40, -360), (0, -400), (40, -360)], "#e03131"),
          rect(-14, -50, 28, 50, "#495057", rx=12)]
    return place(m, x, y, s)


def lanterne(x, y, s=1.0):
    m = [cercle(0, 0, 46, "#fff3bf", opacity=0.35), trait(0, -40, 0, -24, "#495057", 4),
         rect(-18, -24, 36, 46, "#ffe066", stroke="#495057", stroke_width=4, rx=4),
         rect(-22, 20, 44, 8, "#495057", rx=3)]
    return place(m, x, y, s)


def grotte(x, y, s=1.0):
    m = [chemin("M -300 0 Q -320 -340 0 -360 Q 320 -340 300 0 Z", "#2c3e50"),
         chemin("M -190 0 Q -200 -240 0 -250 Q 200 -240 190 0 Z", "#0f1a2b")]
    return place(m, x, y, s)


def fond_marin(S, sombre=False):
    if sombre:
        ocean(S, "#1d3f6e", "#0b1d38", "#b89b62", rayons=False)
    else:
        ocean(S, "#22b8cf", "#1864ab", "#f4d58d")
    S.add(algue(70, 740, 1.1, "#2f9e44" if sombre else "#40c057", graine=3),
          algue(740, 750, 1.0, "#2b8a3e", graine=4))
    S.add(corail(650, 760, 0.8, "#c2255c" if sombre else "#ff8787"), coquillage(170, 770, 0.7))


def surface_dessous(S, y=120, couleur="#a5d8ff", agitee=False):
    """Surface de l'eau vue d'en dessous, en haut de l'image."""
    amp = 34 if agitee else 12
    d = f"M 0 0 L 0 {y}"
    for k in range(8):
        h = amp if k % 2 == 0 else -amp
        d += f" Q {k * 100 + 50} {y + h} {k * 100 + 100} {y}"
    d += " L 800 0 Z"
    S.add(chemin(d, couleur, opacity=0.55))


def tempete(S, y_mer=430, eclairs=((620, 40),)):
    ciel(S, *NUIT_CIEL)
    S.add(nuage(150, 90, 1.2, "#5c677d"), nuage(450, 60, 1.0, "#6c7a96"), nuage(700, 110, 1.1, "#5c677d"))
    for ex, ey in eclairs:
        S.add(eclair(ex, ey, 0.9))
    S.add(rect(0, y_mer, S.w, S.h - y_mer, S.degrade(list(NUIT_MER))))


# --- pages -------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#5f3dc4", "#ffa8a8")
    S.add(etoile5(110, 90, 9, "#fff3bf"), etoile5(690, 70, 10, "#fff3bf"), etoile5(560, 150, 7, "#fff3bf"))
    S.add(phare(700, 520, 0.6))
    S.add(rect(0, 500, 800, 300, S.degrade(["#3b5bdb", "#1d3f6e"])))
    S.add(dans_barque(560, 560, 0.75, expr_malo="rire", expr_chien="rire", bras="salut"))
    vagues_devant(S, 590, "#364fc7", amp=24, longueur=220, decal=60)
    S.add(ondine(300, 820, 1.6, expr="rire", bras="salut"))
    S.add(meduse(110, 700, 0.8, graine=2), meduse(690, 720, 0.7, "#d0bfff", graine=3))
    vagues_devant(S, 720, "#1d3f6e", amp=30, longueur=240, ecume=ECUME, opacity=0.92)
    S.cachette(560, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(meduse(200, 120, 1.4, graine=5, expr="content"))
    S.add(chemin("M 20 250 Q 70 220 120 250 T 220 250 T 320 250 T 420 250", stroke="#4dabf7", sw=8))
    return S


def p01():
    S = Scene()
    fond_marin(S)
    surface_dessous(S, 90)
    S.add(ondine(380, 610, 1.5, expr="rire", bras="haut"))
    S.add(poisson(150, 300, 0.7, "#ffd43b"), poisson(230, 380, 0.5, "#ff922b"), poisson(640, 330, 0.7, "#ff6b6b", flip=True))
    S.add(bulles_eau(560, 470, 0.9, graine=3))
    return S


def p02():
    S = Scene()
    fond_marin(S)
    surface_dessous(S, 150, agitee=True)
    S.add(dauphin(580, 440, 1.0, expr="rire", rot=-20))
    S.add(ondine(250, 650, 1.4, expr="inquiet", bras="joues", regard=(1, -1)))
    S.add(bulle(560, 250, 400, 100, "Viens jouer dans\nles vagues !", 36, pointe=(640, 370)))
    S.add(bulles_eau(130, 420, 0.8, graine=6))
    return S


def p03():
    S = Scene()
    fond_marin(S, sombre=True)
    surface_dessous(S, 130, "#5c7cfa", agitee=True)
    S.add(grotte(400, 760, 1.15))
    S.add(ondine(340, 700, 1.15, expr="oups", bras="joues"))
    S.add(dauphin(520, 600, 0.75, expr="inquiet", flip=True))
    S.add(texte(400, 250, "BRRROUM !", 80, "#ffe066", contour="#1b2559"))
    return S


def p04():
    S = Scene()
    tempete(S, 300, eclairs=((140, 40),))
    S.add(dans_barque(560, 250, 0.7, rot=-12, expr_malo="pleure", expr_chien="triste"))
    vagues_devant(S, 290, "#1d3f6e", amp=40, longueur=180, ecume=ECUME)
    S.add(rect(0, 330, 800, 470, "#0b1d38", opacity=0.35))
    S.add(algue(720, 800, 1.0, "#2b8a3e", graine=8))
    S.add(dauphin(560, 600, 0.9, expr="surpris", flip=True, rot=-10))
    S.add(ondine(220, 750, 1.1, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(bulle(560, 440, 440, 100, "Une barque est perdue\nlà-haut !", 34, pointe=(600, 540)))
    return S


def p05():
    S = Scene()
    fond_marin(S, sombre=True)
    S.add(ondine(300, 680, 1.45, expr="inquiet", bras="calin", regard=(1, -1)))
    S.add(mouvement(170, 420, 0.9, "#a5d8ff"), mouvement(440, 400, 0.9, "#a5d8ff", rot=180))
    S.add(pensee(590, 200, 140, dans_barque(590, 250, 0.55, expr_malo="pleure", expr_chien="triste"), depuis=(380, 400)))
    S.add(texte(600, 500, "Une nageoire", 40, "#fff3bf", contour="#1b2559"))
    S.add(texte(600, 550, "après l'autre…", 40, "#fff3bf", contour="#1b2559"))
    return S


def p06():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#1d3f6e", "#0b1d38"])))
    for k, (mx, my, c) in enumerate([(150, 220, "#fcc2d7"), (640, 180, "#d0bfff"), (120, 560, "#99e9f2"),
                                      (680, 520, "#fcc2d7"), (400, 110, "#99e9f2")]):
        S.add(meduse(mx, my, 0.9, c, graine=k, expr="content"))
    S.add(ondine(400, 700, 1.45, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(bulles_eau(300, 700, 0.9, graine=9), bulles_eau(510, 720, 0.8, graine=10))
    S.cachette(70, 410, "air")
    return S


def p07():
    S = Scene()
    tempete(S, 420, eclairs=((600, 30), (200, 80)))
    pluie(S, 70, graine=7, zone=(0, 0, 800, 500), couleur="#a5d8ff")
    S.add(grosse_vague(620, 520, 1.1))
    S.add(ondine(330, 720, 1.4, expr="oups", bras="joues"))
    vagues_devant(S, 590, "#1d3f6e", amp=44, longueur=200, ecume=ECUME)
    S.add(texte(190, 330, "Trop grand !", 52, "#fff", contour="#1b2559"))
    S.add(texte(190, 395, "Trop fort !", 52, "#fff", contour="#1b2559"))
    return S


def p08():
    S = Scene()
    tempete(S, 460, eclairs=((680, 30),))
    pluie(S, 50, graine=8, zone=(0, 0, 800, 460), couleur="#a5d8ff")
    S.add(dans_barque(520, 500, 1.15, rot=6, expr_malo="surpris", expr_chien="surpris", regard=(-1, 0)))
    S.add(ondine(170, 680, 1.3, expr="sourire", bras="salut"))
    vagues_devant(S, 560, "#1d3f6e", amp=34, longueur=200, decal=40, ecume=ECUME)
    S.add(bulle(220, 170, 320, 90, "Je suis là !", 44, pointe=(190, 380)))
    S.add(bulle(560, 120, 330, 90, "Une sirène !", 44, pointe=(480, 240)))
    return S


def p09():
    S = Scene()
    tempete(S, 400, eclairs=())
    S.add(phare(720, 420, 0.45, allume=False))
    # chemin de méduses lumineuses vers le port
    for k, (mx, my) in enumerate([(340, 640), (440, 580), (530, 530), (610, 490), (670, 460)]):
        S.add(meduse(mx, my, 0.75 - k * 0.09, ["#fcc2d7", "#99e9f2", "#d0bfff"][k % 3], graine=k + 3))
    S.add(ondine(170, 740, 1.3, expr="joie", bras="montre", flip=False))
    vagues_devant(S, 620, "#1d3f6e", amp=26, longueur=220, ecume=ECUME, opacity=0.85)
    S.add(bulle(250, 160, 440, 90, "Méduses, allumez-vous !", 36, pointe=(200, 420)))
    return S


def p10():
    S = Scene()
    tempete(S, 420, eclairs=())
    pluie(S, 50, graine=11, zone=(0, 200, 800, 440), couleur="#a5d8ff")
    S.add(grosse_vague(170, 540, 0.9))
    S.add(dans_barque(430, 480, 0.95, rot=-8, expr_malo="inquiet", expr_chien="inquiet"))
    S.add(chemin("M 566 446 Q 610 480 584 540", stroke="#e9c46a", sw=7))
    S.add(ondine(690, 670, 1.2, expr="concentre", bras="ouverts", flip=True))
    S.add(dauphin(250, 560, 0.7, expr="concentre"), dauphin(300, 620, 0.6, "#748ffc", expr="rire"))
    vagues_devant(S, 590, "#1d3f6e", amp=34, longueur=200, ecume=ECUME)
    for k, (mx, my) in enumerate([(120, 700), (330, 720), (560, 700)]):
        S.add(meduse(mx, my, 0.5, ["#fcc2d7", "#99e9f2", "#d0bfff"][k], graine=k))
    S.add(texte(400, 170, "Une nageoire après l'autre !", 46, "#fff", contour="#1b2559"))
    return S


def p11():
    S = Scene()
    ciel(S, "#364fc7", "#748ffc")
    S.add(etoile5(120, 80, 8, "#fff3bf"), etoile5(300, 50, 7, "#fff3bf"), lune(660, 110, 40))
    S.add(maison(120, 420, 0.6, lumiere=True), maison(270, 420, 0.5, "#d0ebff", "#1971c2", lumiere=True))
    S.add(phare(700, 420, 0.7))
    S.add(rect(0, 420, 800, 380, S.degrade(["#3b5bdb", "#1d3f6e"])))
    # quai
    S.add(rect(0, 420, 470, 120, "#868e96"), rect(0, 420, 470, 16, "#adb5bd"))
    for k in range(5):
        S.add(trait(k * 100 + 40, 440, k * 100 + 40, 540, "#6c757d", 3))
    S.add(personne(270, 430, 1.15, expr="content", bras="tient", objet=lanterne(68, -116, 0.7), **PAPA))
    S.add(malo(170, 430, 0.95, expr="rire", bras="haut"))
    S.add(chien(400, 430, 0.6, expr="rire"))
    S.add(barque(450, 600, 0.75))
    S.add(ondine(640, 720, 1.25, expr="content", bras="salut"))
    vagues_devant(S, 640, "#1d3f6e", amp=12, longueur=200, opacity=0.9)
    S.add(coeur(420, 230, 1.4), coeur(470, 190, 0.9, "#ff8787"))
    S.cachette(70, 690, "air")
    return S


def p12():
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(soleil(660, 120, 60))
    S.add(rect(0, 440, 800, 360, S.degrade(["#4dabf7", "#1971c2"])))
    S.add(dans_barque(500, 520, 1.0, expr_malo="rire", expr_chien="rire", bras="haut"))
    S.add(dauphin(170, 340, 0.75, expr="rire", rot=-25))
    S.add(ondine(260, 700, 1.35, expr="rire", bras="haut"))
    vagues_devant(S, 600, "#1c7ed6", amp=18, longueur=200, ecume="#e7f5ff", opacity=0.9)
    S.add(cercle(120, 520, 10, "#e7f5ff"), cercle(140, 500, 7, "#e7f5ff"), cercle(100, 498, 6, "#e7f5ff"))
    S.cachette(730, 670, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("meduse.svg", vignette),
    ("01-au-fond-de-la-mer.svg", p01), ("02-les-vagues.svg", p02), ("03-la-tempete.svg", p03),
    ("04-une-barque.svg", p04), ("05-une-nageoire.svg", p05), ("06-les-meduses.svg", p06),
    ("07-trop-fort.svg", p07), ("08-je-suis-la.svg", p08), ("09-le-chemin.svg", p09),
    ("10-tous-ensemble.svg", p10), ("11-le-port.svg", p11), ("12-amis.svg", p12),
]
