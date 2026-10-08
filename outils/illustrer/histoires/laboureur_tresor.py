"""Le Laboureur et ses Enfants — le travail est un trésor."""
from fables import *

ID = "laboureur-tresor"

PERE = dict(coiffure="chauve_cote", cheveux="blanc", peau="doree", habit="#8d5524", robe=False, jambes="#495057",
            barbe="#e9ecef")
JEANNE = dict(coiffure="tresses", cheveux="roux", peau="claire", habit="#e64980", robe=True)
PAUL = dict(coiffure="courts", cheveux="brun", peau="doree", habit="#1c7ed6", jambes="#364fc7")
LUCAS = dict(coiffure="boucles", cheveux="noir", peau="brune", habit="#40c057", jambes="#495057")


def pere(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PERE, **k})


def jeanne(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**JEANNE, **k})


def paul(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**PAUL, **k})


def lucas(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**LUCAS, **k})


def avec_beche(**k):
    return dict(bras="tient", objet=beche(68, -60, 0.9, rot=-10), **k)


def piece(x, y, s=1.0):
    return place([cercle(0, 0, 16, "#fcc419", stroke="#f59f00", stroke_width=3),
                  cercle(0, 0, 8, "none", stroke="#f59f00", stroke_width=2)], x, y, s)


def ferme(S, saison="ete", champ="herbe"):
    haut, bas = {"ete": ("#a5d8ff", "#fff9db"), "automne": ("#ffd8a8", "#fff4e6"), "printemps": ("#a5d8ff", "#e6fcf5"),
                 "hiver": ("#ced4da", "#f1f3f5")}[saison]
    ciel(S, haut, bas)
    S.add(soleil(680, 110, 46, "#ffa94d" if saison == "automne" else "#ffd43b"))
    collines(S, 500, "#b2f2bb" if saison != "automne" else "#ffc078", graine=61)
    S.add(maison(120, 520, 0.6, mur="#fff4e6", toit="#a0522d"))
    if champ == "herbe":
        S.add(rect(0, 500, 800, 300, "#8ce99a"))
        for k in range(14):
            S.add(herbe(30 + k * 57, 560 + (k % 3) * 70, 1.0))
    elif champ == "laboure":
        champ_laboure(S, 500)
    elif champ == "pousses":
        champ_laboure(S, 500)
        for i in range(9):
            for j in range(5):
                x, y = 40 + i * 90 + (j % 2) * 40, 540 + j * 55
                S.add(g([trait(x, y, x, y - 18, "#40c057", 4), ellipse(x - 7, y - 16, 7, 4, "#51cf66", rot=-30), ellipse(x + 7, y - 18, 7, 4, "#51cf66", rot=30)]))
    elif champ == "ble":
        champ_ble(S, 500, graine=5, n_=70)


def couverture():
    S = Scene()
    ferme(S, "ete", "ble")
    S.add(pere(400, 740, 1.3, expr="content", bras="ouverts"))
    S.add(jeanne(210, 770, 1.0, expr="rire", bras="haut"))
    S.add(paul(590, 770, 1.0, expr="rire", **avec_beche()))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(beche(200, 250, 1.1, rot=0))
    S.add(piece(140, 230, 1.4), piece(260, 235, 1.2))
    return S


def p01():
    S = Scene()
    ferme(S, "ete", "laboure")
    S.add(pere(400, 760, 1.5, expr="concentre", **avec_beche()))
    return S


def p02():
    S = Scene()
    ferme(S, "ete", "herbe")
    S.add(jeanne(200, 760, 1.2, expr="rire", bras="haut"))
    S.add(paul(400, 760, 1.2, expr="joie", bras="salut", objet=None))
    S.add(ballon_jeu(420, 440, 30, "#fa5252"))
    S.add(lucas(600, 760, 1.2, expr="rire", bras="haut"))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(560, 110, 170, 160, "#a5d8ff", rideaux="#b5651d"))
    S.add(rect(180, 560, 200, 30, "#a0522d", rx=8), rect(190, 440, 24, 150, "#a0522d"), rect(346, 440, 24, 150, "#a0522d"))
    S.add(rect(190, 420, 180, 150, "#c68642", rx=20))
    S.add(pere(280, 700, 1.3, expr="triste", bras="calin"))
    S.add(paul(560, 770, 1.0, expr="inquiet"))
    S.add(jeanne(680, 770, 1.0, expr="inquiet"))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(pere(200, 760, 1.35, expr="malin", bras="salut", regard=(1, 0)))
    S.add(jeanne(420, 770, 1.05, expr="surpris", regard=(-1, 0)))
    S.add(paul(560, 770, 1.05, expr="bouche_bee", regard=(-1, 0)))
    S.add(lucas(700, 770, 1.05, expr="surpris", regard=(-1, 0)))
    S.add(bulle(360, 120, 520, 110, "Un trésor est caché\ndans notre champ !", 36, pointe=(220, 460)))
    return S


def p05():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(pere(200, 760, 1.35, expr="sourire", bras="ouverts", regard=(1, 0)))
    S.add(jeanne(440, 770, 1.05, expr="concentre", regard=(-1, 0)))
    S.add(paul(580, 770, 1.05, expr="concentre", regard=(-1, 0)))
    S.add(lucas(710, 770, 1.05, expr="concentre", regard=(-1, 0)))
    S.add(bulle(380, 110, 560, 130, "Creusez, bêchez, retournez\nla terre partout !", 34, pointe=(220, 460)))
    S.cachette(70, 270, "air")
    return S


def p06():
    S = Scene()
    ferme(S, "ete", "herbe")
    S.add(jeanne(200, 760, 1.2, expr="rire", **avec_beche()))
    S.add(paul(410, 760, 1.2, expr="joie", **avec_beche()))
    S.add(lucas(620, 760, 1.2, expr="rire", **avec_beche()))
    S.add(pensee(420, 160, 110, contenu=g([piece(380, 170, 1.4), piece(420, 150, 1.4), piece(460, 175, 1.4)])))
    return S


def p07():
    S = Scene()
    ferme(S, "ete", "laboure")
    for k, (fn, x_) in enumerate(((jeanne, 180), (paul, 420), (lucas, 640))):
        S.add(ellipse(x_ + 70, 770, 60, 16, "#5c3a1e"))
        S.add(fn(x_, 760, 1.15, expr="concentre", bras="tire", objet=beche(92, -40, 0.9, rot=40)))
    S.add(texte(400, 380, "Rien !", 64, "#b5651d", contour="#fff"))
    return S


def p08():
    S = Scene()
    ferme(S, "ete", "laboure")
    S.add(soleil(680, 110, 60, "#ff922b"))
    S.add(jeanne(220, 760, 1.2, expr="inquiet", **avec_beche()))
    S.add(paul(430, 760, 1.2, expr="concentre", bras="joues"))
    S.add(lucas(630, 760, 1.2, expr="fache", **avec_beche()))
    S.add(goutte(380, 540, 1.0, "#74c0fc"), goutte(560, 520, 1.0, "#74c0fc"))
    return S


def p09():
    S = Scene()
    ferme(S, "ete", "laboure")
    S.add(caillou(180, 700, 1.4))
    S.add(g([chemin("M 330 700 Q 330 640 380 640 L 450 650 Q 470 660 460 700 Z", "#6d4424"), ellipse(400, 700, 70, 10, "#495057")]))
    S.add(chemin("M 560 700 q 20 -30 40 0 q 20 30 40 0 q 20 -30 40 0", stroke="#f783ac", sw=12))
    S.add(texte(180, 600, "un caillou", 30, "#fff"), texte(400, 600, "une chaussure", 30, "#fff"), texte(620, 640, "un ver !", 30, "#fff"))
    S.add(texte(400, 300, "Mais pas de trésor…", 48, "#b5651d", contour="#fff"))
    return S


def p10():
    S = Scene()
    ferme(S, "automne", "laboure")
    S.add(jeanne(220, 760, 1.2, expr="triste", bras="bas"))
    S.add(paul(410, 760, 1.2, expr="triste", bras="croises"))
    S.add(lucas(600, 760, 1.2, expr="pleure", bras="yeux"))
    S.add(bulle(400, 140, 480, 90, "Il n'y a pas de trésor…", 34, pointe=(410, 400)))
    return S


def p11():
    S = Scene()
    ferme(S, "automne", "laboure")
    S.add(jeanne(300, 760, 1.3, expr="content", bras="donne", regard=(1, 1)))
    for k in range(7):
        S.add(grain(360 + k * 30, 620 + (k % 3) * 30, 0.9))
    S.add(paul(560, 760, 1.2, expr="sourire", bras="donne", regard=(-1, 1), flip=True))
    S.add(bulle(360, 140, 480, 90, "Semons du blé !", 40, pointe=(300, 420)))
    return S


def p12():
    S = Scene()
    ferme(S, "printemps", "pousses")
    S.add(lucas(400, 740, 1.2, expr="rire", bras="haut"))
    S.add(papillon(600, 330, 1.2))
    return S


def p13():
    S = Scene()
    ferme(S, "ete", "ble")
    S.add(jeanne(210, 740, 1.2, expr="bouche_bee", bras="joues"))
    S.add(paul(410, 740, 1.2, expr="rire", bras="haut"))
    S.add(lucas(610, 740, 1.2, expr="joie", bras="ouverts"))
    for k in range(6):
        S.add(ble(60 + k * 140, 800, 1.3))
    return S


def p14():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff4e6")
    ville(S, 600)
    sol(S, 600, "#adb5bd")
    S.add(sac(200, 760, 1.2, "#e9d8c4", "blé"))
    S.add(paul(400, 760, 1.2, expr="rire", bras="porte", objet=sac(0, -60, 0.6, "#fcc419")))
    S.add(jeanne(590, 760, 1.2, expr="rire", bras="haut"))
    for k in range(5):
        S.add(piece(480 + k * 40, 400 - (k % 2) * 30, 1.2))
    return S


def p15():
    S = Scene()
    ferme(S, "ete", "ble")
    S.add(pere(400, 750, 1.4, expr="content", bras="ouverts"))
    S.add(jeanne(180, 770, 1.0, expr="content", regard=(1, 0)))
    S.add(paul(600, 770, 1.0, expr="content", regard=(-1, 0)))
    S.add(lucas(720, 780, 0.95, expr="rire", regard=(-1, 0)))
    S.add(bulle(400, 130, 520, 110, "Le trésor, c'était\nvotre travail !", 38, pointe=(400, 440)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("beche-seule.svg", vignette),
    ("01-le-vieux-laboureur.svg", p01), ("02-les-enfants.svg", p02), ("03-trop-fatigue.svg", p03),
    ("04-un-tresor.svg", p04), ("05-creusez.svg", p05), ("06-les-beches.svg", p06),
    ("07-rien.svg", p07), ("08-tout-l-ete.svg", p08), ("09-pas-de-tresor.svg", p09),
    ("10-decus.svg", p10), ("11-semons.svg", p11), ("12-les-pousses.svg", p12),
    ("13-la-recolte.svg", p13), ("14-le-marche.svg", p14), ("15-le-vrai-tresor.svg", p15),
]
