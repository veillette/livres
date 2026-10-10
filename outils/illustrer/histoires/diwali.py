"""Les lumières de Diwali — la fête des lumières avec Priya et Dadi.

Diwali se fête en automne, la nuit de la nouvelle lune : la nuit la plus
noire, sans Lune dans le ciel. On nettoie la maison, on dessine un rangoli
de poudres colorées devant la porte, on prépare des diyas (petites lampes
d'argile à huile), des douceurs (ladous, jalébis), on met des habits neufs.
Dadi raconte : Rama et Sita rentraient chez eux de nuit, et les gens ont
allumé des milliers de lampes pour leur montrer le chemin. Le soir, la
maison brille ; on partage des douceurs avec la voisine ; feux d'artifice
et cierges magiques, de loin.

Plans : 1 moyen (le grand ménage) · 2 gros plan (le rangoli) · 3 moyen (les
diyas) · 4 large (Rama et Sita) · 5 moyen (les habits neufs) · 6 gros plan
(les douceurs) · 7 large (la nuit sans lune, la maison illuminée) · 8 moyen
(chez la voisine) · 9 large (les feux d'artifice) · 10 gros plan (la diya
de Priya).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from fetes import feu_artifice
from contes import balai

ID = "diwali"
PAPIER_PEINT = "losanges"

OR_ = "#fcc419"


def sari(c="#fab005"):
    """Pan du sari, en écharpe sur l'épaule (tenue)."""
    return g([chemin("M -30 -106 Q 10 -80 34 -40 L 44 -46 Q 26 -86 -14 -108 Z", c),
              chemin("M -26 -102 Q 12 -78 36 -42", stroke=OR_, sw=3)])


PRIYA = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#e64980", motif_robe=OR_, yeux="cils", nez="rond")
DADI = dict(stature="ancien", peau="brune", cheveux="gris", coiffure="chignon", habit="#f08c00", tenue=sari("#c2255c"), carrure="ronde")
MAMAN = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="longs", habit="#7048e8", tenue=sari("#20c997"))
PAPA = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#fff3bf", robe=False, jambes="#fff3bf",
            barbe="#2b2b3a", tenue=g([trait(0, -106, 0, -60, "#f08c00", 3), cercle(0, -96, 3, OR_), cercle(0, -84, 3, OR_)]))
VOISINE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="boucles", habit="#4dabf7", acc=("lunettes",))


def priya(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PRIYA, **k})


def dadi(x, y, s=1.3, **k):
    return personne(x, y, s, **{**DADI, **k})


def diya(x, y, s=1.0, allumee=True, S=None):
    """Petite lampe d'argile ; (x, y) = son pied. Avec S, la flamme reçoit son halo."""
    m = [chemin("M -30 -10 Q -30 6 0 6 Q 30 6 44 -14 L 30 -14 Q 0 -20 -30 -10 Z", volume("#d9480f", 0.35, 0.75)),
         chemin("M -24 -12 Q 0 -18 30 -14", stroke="#fff4e6", sw=2, opacity=0.6),
         chemin("M -22 -4 l 4 -4 l 4 4 l 4 -4 l 4 4 l 4 -4 l 4 4", stroke=OR_, sw=2)]
    if allumee:
        m += [ellipse(38, -26, 7, 13, "#ffd43b"), ellipse(38, -22, 3.5, 7, "#fff3bf")]
        if S is not None:
            S.lumiere(x + 38 * s, y - 26 * s, 60 * s, "#ffd43b", 0.75)
    return place(m, x, y, s)


def rangoli(x, y, r=140, sy=0.42):
    """Rangoli de poudres colorées, à plat sur le sol (vu en perspective) ; (x, y) = centre."""
    m = [cercle(0, 0, r, "#fff4e6")]
    couronnes = (("#e64980", 1.0, 12), ("#fcc419", 0.78, 10), ("#40c057", 0.58, 8), ("#4dabf7", 0.4, 8), ("#ff922b", 0.22, 6))
    for c, k, nb in couronnes:
        for i in range(nb):
            a = math.radians(i * 360 / nb)
            m.append(ellipse(math.cos(a) * r * k * 0.78, math.sin(a) * r * k * 0.78, r * k * 0.26, r * k * 0.12, c, rot=i * 360 / nb))
    m.append(cercle(0, 0, r * 0.12, "#be4bdb"))
    for i in range(16):
        a = math.radians(i * 22.5)
        m.append(cercle(math.cos(a) * r * 1.02, math.sin(a) * r * 1.02, r * 0.05, "#fff"))
    return place(m, x, y, 1, sy=sy)


def ladou(x, y, s=1.0):
    return place([cercle(0, 0, 18, volume("#ffa94d", 0.4, 0.75)), cercle(-6, -6, 2, "#fff3bf"), cercle(6, 2, 2, "#fff3bf"), cercle(-2, 8, 2, "#fff3bf")], x, y, s)


def jalebi(x, y, s=1.0):
    return place([chemin("M 0 0 m -4 0 a 4 4 0 1 1 8 0 a 10 10 0 1 1 -20 0 a 16 16 0 1 1 32 0", stroke="#f08c00", sw=7)], x, y, s)


def plateau_douceurs(x, y, s=1.0):
    m = [ellipse(0, 0, 150, 34, volume("#dee2e6", 0.5, 0.75)), ellipse(0, -4, 136, 28, "#f8f9fa")]
    for k, (dx, dy) in enumerate(((-90, -12), (-60, -22), (-30, -10), (-70, 2), (-40, 0))):
        m.append(ladou(dx, dy - 8, 1.0))
    for dx, dy in ((40, -12), (80, -6), (60, -24), (100, -18)):
        m.append(jalebi(dx, dy, 1.0))
    m.append(rect(-14, -26, 30, 20, "#fff3bf", rx=3))
    return place(m, x, y, s)


def maison_dedans(S, y=600, nuit_=False):
    piece(S, "manoir", y)
    for x in range(60, 800, 120):
        S.add(fleur(x, 30, 0.5, "#ff922b", tige=0))
    S.add(chemin("M 0 30 Q 200 70 400 30 T 800 30", stroke="#ff922b", sw=6))
    if nuit_:
        S.ambiance("nuit")


def maison_illuminee(S, x, y, s=1.0):
    """La maison de Priya la nuit, des diyas le long des marches et des fenêtres."""
    S.add(maison(x, y, s, mur="#ffe8cc", toit="#c92a2a", lumiere=True, cote=False, volets="#d9480f"))
    for k in range(7):
        S.add(diya(x - 120 * s + k * 40 * s, y + 12 * s, 0.5 * s, S=S))
    for fx in (-82, 46):
        for k in range(3):
            S.add(diya(x + (fx + k * 14) * s, y - 76 * s, 0.25 * s, S=S))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 50, 2, (0, 0, 800, 420))
    S.add(rect(0, 640, 800, 160, "#495057"))
    maison_illuminee(S, 400, 640, 1.5)
    S.add(rangoli(400, 720, 120))
    S.add(priya(210, 790, 1.3, expr="rire", bras="porte", regard=(1, -0.2), objet=diya(0, -70, 0.8, S=None)))
    S.lumiere(210, 790 - 96 * 1.3, 90, "#ffd43b", 0.7)
    S.add(dadi(600, 790, 1.3, expr="content", bras="mains_jointes", regard=(-1, -0.2)))
    return S


def vignette():
    S = Scene(400, 270)
    for k in range(3):
        S.add(diya(110 + k * 100, 200, 1.3))
    return S


def p01():
    """Plan moyen : quelques jours avant Diwali, on nettoie toute la maison."""
    S = Scene()
    maison_dedans(S)
    S.add(fenetre(470, 100, 200, 160, "#a5d8ff", rideaux="#e64980",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), arbre(560, 330, 0.5, "#ffa94d", "#ff922b")])))
    S.add(priya(260, 790, 1.3, expr="rire", bras="tient", robe=False, jambes="#e64980", regard=(1, 0.3), objet=balai(76, -30, 0.95, rot=6)))
    S.add(personne(560, 790, 1.4, expr="content", bras="salut", regard=(-1, 0), **MAMAN))
    S.add(bulle(400, 140, 420, 100, "Une maison propre\npour la fête !", 34, pointe=(330, 450)))
    return S


def p02():
    """Gros plan : devant la porte, Priya et Dadi dessinent un rangoli de poudres colorées."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(rect(0, 450, 800, 350, "#e9c99a"))
    S.add(rect(250, 160, 300, 300, "#c68642"), rect(280, 190, 240, 270, "#8d5524"))
    S.add(rangoli(400, 640, 190))
    S.add(dadi(150, 800, 1.5, expr="content", bras="designe", regard=(1, 0.6)))
    S.add(priya(650, 800, 1.4, expr="concentre", bras="ramasse", regard=(-1, 0.6)))
    for k, c in enumerate(("#e64980", "#fcc419", "#40c057", "#4dabf7")):
        S.add(place([ellipse(0, 0, 30, 10, "#fff"), ellipse(0, -6, 24, 10, c)], 300 + k * 60, 780))
    S.camera(1.1, 400, 520)
    S.dessus(texte(400, 100, "Un rangoli pour accueillir la fête !", 38, "#c2255c", contour="#fff"))
    return S


def p03():
    """Plan moyen : Dadi montre à Priya comment préparer les diyas."""
    S = Scene()
    maison_dedans(S)
    S.add(dadi(230, 650, 1.2, expr="content", bras="porte", regard=(1, 0.4)))
    S.add(priya(540, 650, 1.1, expr="bouche_bee", bras="porte", regard=(-1, 0.4)))
    S.add(table(400, 790, 520, 150, "#c68642"))
    for k in range(6):
        S.add(diya(220 + k * 70, 628, 0.9, allumee=k < 2))
    S.add(bulle(250, 150, 420, 100, "Un peu d'huile,\nune mèche de coton…", 32, pointe=(230, 380)))
    return S


def p04():
    """Plan large : la légende : Rama et Sita rentrent chez eux la nuit ; partout, des lampes éclairent le chemin."""
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 40, 4, (0, 0, 800, 400))
    S.add(rect(0, 560, 800, 240, "#2f3a4d"))
    S.add(chemin("M 300 800 Q 380 640 420 560 L 480 560 Q 520 640 640 800 Z", "#495057"))
    for x, y in ((150, 560), (290, 520), (560, 520), (690, 560)):
        S.add(maison(x, y, 0.5, mur="#ffe8cc", toit="#c92a2a", lumiere=True, cote=False))
    for k in range(7):
        t = k / 6
        S.add(diya(300 + 120 * t - 30, 790 - 230 * t, 0.7 - 0.4 * t, S=S))
        S.add(diya(640 - 160 * t + 10, 790 - 230 * t, 0.7 - 0.4 * t, S=S))
    S.add(personne(440, 650, 0.85, stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit=OR_, robe=False,
                   jambes="#fff3bf", acc=("couronne",), expr="content", bras="main", regard=(1, 0)))
    S.add(personne(530, 650, 0.85, stature="adulte", peau="doree", cheveux="noir", coiffure="tres_longs", habit="#c2255c", motif_robe=OR_,
                   acc=("diademe",), expr="content", bras="main", flip=True, regard=(-1, 0)))
    S.add(texte(400, 140, "Il était une fois Rama et Sita…", 40, OR_, contour="#5f3dc4"))
    return S


def p05():
    """Plan moyen : Priya dans ses habits neufs, avec Papa et Maman."""
    S = Scene()
    maison_dedans(S)
    S.add(personne(200, 790, 1.4, expr="content", bras="applaudit", regard=(1, 0), **PAPA))
    S.add(priya(400, 790, 1.35, expr="rire", bras="ouverts", regard=(0, -0.3)))
    S.add(personne(600, 790, 1.4, expr="joie", bras="mains_jointes", regard=(-1, 0), **MAMAN))
    S.add(paillettes(480, 420, 1.0, OR_), paillettes(300, 380, 0.8, OR_))
    S.add(texte(400, 140, "Des habits neufs !", 52, "#c2255c", contour="#fff"))
    S.cachette(70, 140, "air")
    return S


def p06():
    """Gros plan : le plateau de douceurs : ladous et jalébis."""
    S = Scene()
    maison_dedans(S)
    S.add(table(400, 790, 560, 150, "#c68642", nappe="#ffd8a8"))
    S.add(plateau_douceurs(400, 620, 1.2))
    S.add(priya(640, 860, 1.6, expr="miam", bras="joues", regard=(-1, 0.4)))
    S.camera(1.3, 420, 560)
    S.dessus(texte(400, 110, "Des ladous et des jalébis !", 44, "#f08c00", contour="#fff"))
    return S


def p07():
    """Plan large : la nuit de Diwali, sans lune ; la maison brille de mille petites lampes."""
    S = Scene()
    nuit(S, "#050a1f", "#1c2a52")
    etoiles(S, 70, 7, (0, 0, 800, 460))
    S.add(rect(0, 640, 800, 160, "#343a40"))
    maison_illuminee(S, 400, 640, 1.6)
    S.add(rangoli(400, 720, 110))
    S.add(texte(400, 120, "Pas de lune ce soir…", 42, "#fff3bf"))
    S.add(texte(400, 180, "mais mille petites lumières !", 38, OR_))
    S.cachette(740, 760)
    return S


def p08():
    """Plan moyen : Priya apporte des douceurs à Madame Tremblay, la voisine."""
    S = Scene()
    nuit(S, "#1c2a52", "#4c5b9a")
    S.add(rect(0, 640, 800, 160, "#495057"))
    S.add(maison(600, 640, 1.3, mur="#d0ebff", toit="#495057", lumiere=True, cote=False))
    S.add(personne(600, 790, 1.35, expr="surpris", bras="joues", regard=(-1, 0), **VOISINE))
    S.add(priya(330, 790, 1.3, expr="rire", bras="donne", regard=(1, 0), objet=plateau_douceurs(96, -100, 0.45)))
    S.add(diya(160, 790, 0.9, S=S))
    S.add(bulle(380, 150, 420, 100, "Joyeux Diwali,\nMadame Tremblay !", 34, pointe=(340, 440)))
    return S


def cierge(x, y, s=1.0, rot=0):
    m = [trait(0, 0, 0, -100, "#868e96", 3)]
    for k in range(12):
        a = math.radians(k * 30)
        m.append(trait(math.cos(a) * 6, -110 + math.sin(a) * 6, math.cos(a) * 26, -110 + math.sin(a) * 26, "#fff3bf", 3))
    m.append(cercle(0, -110, 8, "#fff"))
    return place(m, x, y, s, rot=rot)


def p09():
    """Plan large : feux d'artifice dans le ciel ; Priya agite un cierge magique, Papa veille."""
    S = Scene()
    nuit(S, "#050a1f", "#364fc7")
    S.add(feu_artifice(180, 160, 90, OR_), feu_artifice(560, 120, 80, "#f783ac"), feu_artifice(380, 260, 60, "#69db7c"))
    S.add(rect(0, 640, 800, 160, "#343a40"))
    S.add(maison(640, 640, 0.9, mur="#ffe8cc", toit="#c92a2a", lumiere=True, cote=False))
    S.add(personne(180, 790, 1.35, expr="content", bras="epaule", regard=(1, -0.3), **PAPA))
    S.add(priya(330, 790, 1.2, expr="rire", bras="tient", regard=(0.5, -0.6), objet=cierge(68, -146, 0.9, rot=20)))
    S.lumiere(330 + (68 + 40) * 1.2, 790 - (146 + 100) * 1.2, 80, "#fff3bf", 0.7)
    S.add(texte(560, 330, "Ooooh !", 50, OR_))
    return S


def p10():
    """Gros plan : Priya pose sa diya sur le rebord de la fenêtre ; dehors, la nuit sans lune."""
    S = Scene()
    maison_dedans(S, nuit_=True)
    dehors = g([rect(0, 0, 800, 800, "#0b1433")] + [cercle(220 + k * 47 % 300, 150 + k * 31 % 150, 2, "#fff") for k in range(12)])
    S.add(fenetre(220, 120, 360, 300, "#0b1433", cadre="#fff", contenu=dehors))
    S.add(diya(400, 448, 1.4, S=S))
    S.add(priya(400, 900, 2.0, expr="content", bras="tend", regard=(0, -0.4)))
    S.camera(1.2, 400, 480)
    S.dessus(texte(400, 110, "Joyeux Diwali !", 56, OR_, contour="#c2255c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("diyas-seules.svg", vignette),
    ("01-le-menage.svg", p01), ("02-le-rangoli.svg", p02), ("03-les-diyas.svg", p03),
    ("04-rama-et-sita.svg", p04), ("05-habits-neufs.svg", p05), ("06-les-douceurs.svg", p06),
    ("07-la-nuit-sans-lune.svg", p07), ("08-la-voisine.svg", p08), ("09-feux-d-artifice.svg", p09),
    ("10-joyeux-diwali.svg", p10),
]
