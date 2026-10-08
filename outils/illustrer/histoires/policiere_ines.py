"""Inès, policière — veiller sur la ville et aider ceux qui sont perdus."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from sciences import canard
from contes import carotte, chou

ID = "policiere-ines"
INES = dict(peau="rosee", cheveux="brun", coiffure="chignon", habit=MARINE, jambes=MARINE,
            chaussures="#111827", tenue=uniforme_police(), coiffe=casquette_police())
LEON = dict(peau="doree", cheveux="noir", coiffure="courts", habit="#ff922b", jambes="#364fc7",
            chaussures="#e03131")
VERT = "#2f9e44"


def chapeau_rond(c=VERT):
    return g([ellipse(0, -186, 78, 14, _assombrir(c, 0.85)),
              chemin("M -50 -188 Q -50 -246 0 -248 Q 50 -246 50 -188 Z", c),
              rect(-50, -204, 100, 12, "#fcc419")])


PAPA = dict(peau="doree", cheveux="noir", coiffure="courts", habit="#748ffc", jambes="#495057",
            coiffe=chapeau_rond())


def ines(x, y, s=1.6, **k):
    return pro(x, y, s, **{**INES, **k})


def leon(x, y, s=1.1, **k):
    return petit(x, y, s, **{**LEON, **k})


def voiture_police(x, y, s=1.0, flip=False):
    m = [chemin("M -230 -50 L -230 -110 Q -226 -130 -200 -134 L -120 -140 L -70 -200 L 90 -200 L 150 -140 "
                "L 210 -132 Q 236 -128 236 -100 L 236 -50 Z", "#f8f9fa", stroke="#dee2e6", sw=4),
         chemin("M -56 -188 L 80 -188 L 128 -142 L -100 -142 Z", "#a5d8ff"),
         trait(10, -188, 10, -142, "#f8f9fa", 8),
         rect(-230, -108, 466, 26, "#1c7ed6"), rect(-230, -82, 466, 8, "#e03131"),
         texte(0, -120, "POLICE", 30, "#1c7ed6"),
         gyrophare(10, -200, 1.0, "#4dabf7"),
         rect(214, -96, 24, 16, "#fff3bf", rx=4), rect(-240, -64, 480, 16, "#495057", rx=6),
         roue(-140, -44, 40), roue(140, -44, 40)]
    return place(m, x, y, s, flip=flip)


def feu(x, y, s=1.0, allume=None, panne=False):
    """Feu tricolore ; allume = "rouge" | "orange" | "vert"."""
    couleurs = [("rouge", "#fa5252"), ("orange", "#fd7e14"), ("vert", "#40c057")]
    m = [rect(-8, -200, 16, 200, "#495057"), rect(-40, -340, 80, 160, "#343a40", rx=14)]
    for k, (nom, c) in enumerate(couleurs):
        on = (nom == allume) and not panne
        m.append(cercle(0, -310 + k * 50, 20, c if on else "#495057"))
    if panne:
        m.append(texte(64, -260, "?", 60, "#fa5252"))
    return place(m, x, y, s)


def sifflet(x, y, s=1.0, rot=0):
    return place([rect(-24, -10, 40, 20, "#adb5bd", rx=10), rect(10, -14, 18, 10, "#868e96", rx=3), cercle(-12, 0, 5, "#495057")],
                 x, y, s, rot=rot)


def etal(x, y, c="#fa5252", contenu="pommes"):
    """Étal de marché avec auvent rayé ; (x, y) = sol, au milieu."""
    m = [rect(x - 120, y - 330, 10, 330, "#868e96"), rect(x + 110, y - 330, 10, 330, "#868e96")]
    for k in range(6):
        m.append(rect(x - 130 + k * 43, y - 360, 43, 60, c if k % 2 == 0 else "#fff"))
    m.append(chemin(f"M {x - 130} {y - 300} " + " ".join(f"q 21 22 43 0" for _ in range(6)), "#fff"))
    m.append(rect(x - 130, y - 140, 260, 130, "#c68642", rx=6))
    m.append(rect(x - 140, y - 160, 280, 26, "#a0693a", rx=6))
    for k in range(7):
        xx = x - 105 + k * 35
        if contenu == "pommes":
            m.append(pomme(xx, y - 168, 0.8, "#fa5252" if k % 2 else "#fab005"))
        else:
            m.append(carotte(xx, y - 176, 0.5, rot=-60) if k % 2 else chou(xx, y - 168, 0.5))
    return g(m)


def commissariat(S):
    ciel(S)
    S.add(rect(60, 150, 680, 450, "#dbe4ff"), rect(40, 130, 720, 40, MARINE))
    S.add(rect(290, 190, 220, 60, "#fff", rx=8), texte(400, 236, "POLICE", 44, "#1c7ed6"))
    for x in (110, 560):
        S.add(rect(x, 300, 130, 110, "#a5d8ff", stroke="#fff", stroke_width=6))
    S.add(porte(400, 600, 150, 260, "#1c7ed6"))
    S.add(rect(0, 600, 800, 200, "#ced4da"))


def parc(S, y=600):
    ciel(S)
    collines(S, y, "#b2f2bb", graine=8)
    sol(S, y, "#8ce99a")


def couverture():
    S = Scene()
    rue(S, 600)
    S.add(voiture_police(470, 680, 0.95))
    S.add(ines(230, 790, 1.85, expr="content", bras="salut"))
    S.add(leon(580, 790, 1.2, expr="rire", bras="salut", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(place(casquette_police(), 140, 400, 0.95))
    S.add(sifflet(300, 150, 2.0, rot=-15))
    return S


def p01():
    S = Scene()
    commissariat(S)
    S.add(ines(400, 790, 1.75, expr="fier", bras="tete"))
    S.add(eclat(560, 450, 0.6, "#ffd43b"))
    return S


def p02():
    S = Scene()
    rue(S, 560, passage=True)
    S.add(rect(40, 200, 220, 70, "#fff", rx=8), texte(150, 248, "ÉCOLE", 40, "#e8590c"))
    S.add(ines(620, 780, 1.6, expr="sourire", bras="large", regard=(-1, 0)))
    S.add(petit(320, 740, 1.0, peau="claire", cheveux="blond", coiffure="queue", habit="#f783ac", expr="content",
                bras="bas", regard=(1, 0)))
    S.add(petit(440, 740, 1.0, peau="foncee", cheveux="noir", coiffure="boucles", habit="#ffd43b", expr="joie",
                bras="salut", regard=(1, 0)))
    S.add(bulle(360, 110, 520, 100, "On regarde à gauche, à droite…\npuis on traverse !", 30, pointe=(600, 420)))
    return S


def p03():
    S = Scene()
    rue(S, 560)
    S.add(feu(680, 600, 1.0, panne=True))
    S.add(camion(120, 690, 1.3, "#4dabf7"), camion(560, 760, 1.0, "#e64980"))
    S.add(ines(360, 790, 1.6, expr="concentre", bras="poing"))
    S.add(sifflet(360, 790 - 120 * 1.6, 0.9))
    S.add(texte(200, 200, "Tuuut !", 60, "#1c7ed6", contour="#fff", rot=-8))
    return S


def p04():
    S = Scene()
    parc(S)
    S.add(arbre(120, 600, 1.2), arbre(700, 590, 1.0))
    S.add(ellipse(560, 700, 200, 50, "#74c0fc"))
    S.add(canard(500, 700, 0.7), canard(600, 690, 0.6, flip=True), canard(660, 712, 0.5))
    S.add(velo(300, 780, 1.3, "#1c7ed6"))
    S.add(ines(170, 790, 1.55, expr="content", bras="tire"))
    S.add(texte(560, 250, "Bonjour, les canards !", 40, "#2f9e44", contour="#fff"))
    return S


def marche(S):
    ciel(S)
    S.add(rect(0, 600, 800, 200, "#ced4da"))
    S.add(etal(150, 600, "#fa5252"), etal(650, 600, "#40c057", "legumes"))


def p05():
    S = Scene()
    marche(S)
    S.add(leon(420, 790, 1.3, expr="pleure", bras="yeux", larmes=True))
    S.add(ines(640, 790, 1.6, expr="inquiet", bras="donne", flip=True, regard=(-1, 0.5)))
    S.add(bulle(330, 140, 420, 100, "Je ne trouve plus\nmon papa !", 34, pointe=(410, 520)))
    return S


def p06():
    S = Scene()
    marche(S)
    S.add(leon(300, 790, 1.3, expr="triste", bras="bas", regard=(1, -0.5)))
    S.add(ines(560, 790, 1.6, expr="concentre", bras="pense", regard=(-1, 0)))
    S.add(pensee(300, 200, 120, place(chapeau_rond(), 300, 420, 1.2), depuis=(300, 520)))
    S.add(texte(620, 300, "Chapeau vert…", 34, MARINE, contour="#fff"))
    return S


def foule(S):
    gens = [(110, "claire", "#fa5252", "#e03131"), (270, "foncee", "#74c0fc", "#1c7ed6"),
            (560, "rosee", "#ffd43b", "#fab005"), (700, "brune", "#da77f2", "#ae3ec9")]
    for x, peau, hab, chap in gens:
        S.add(pro(x, 700, 1.25, peau=peau, cheveux="brun", habit=hab, jambes="#495057", coiffe=chapeau_rond(chap),
                  expr="sourire"))


def p07():
    S = Scene()
    marche(S)
    foule(S)
    S.add(ines(320, 800, 1.45, expr="concentre", bras="hanches", regard=(1, 0)))
    S.add(leon(470, 800, 1.15, expr="inquiet", bras="montre", regard=(1, -0.5)))
    S.add(texte(400, 160, "Rouge… bleu… jaune…", 40, MARINE, contour="#fff"))
    S.cachette(730, 160, "air")
    return S


def p08():
    S = Scene()
    marche(S)
    S.add(pro(240, 790, 1.7, **PAPA, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(leon(440, 770, 1.25, expr="rire", bras="ouverts", regard=(-1, 0), rot=-10))
    S.add(ines(620, 790, 1.5, expr="content", bras="hanches"))
    S.add(coeur(220, 300, 1.0), coeur(500, 260, 0.8))
    S.add(texte(400, 140, "Léon !", 64, "#e8590c", contour="#fff"))
    S.cachette(730, 160, "air")
    return S


def p09():
    S = Scene()
    parc(S)
    S.add(ines(150, 790, 1.5, expr="sourire", bras="montre", regard=(1, -1)))
    S.add(leon(660, 790, 1.15, expr="sourire", bras="bas", regard=(-1, -1)))
    cases = [(370, 140, "Je reste là.", g([rect(-30, -50, 60, 100, "#e7f5ff", rx=6), place(petit(0, 0, 0.35, **LEON), 0, 45)])),
             (370, 330, "Je demande.", g([place(ines(0, 0, 0.35), -20, 50), place(petit(0, 0, 0.3, **LEON), 30, 50)])),
             (370, 520, "Je sais le numéro.", g([rect(-28, -48, 56, 96, "#343a40", rx=10), rect(-22, -40, 44, 70, "#a5d8ff", rx=4)] +
                                                   [cercle(-12 + (k % 3) * 12, -26 + (k // 3) * 16, 4, "#fff") for k in range(9)]))]
    for x, y, mot, dessin in cases:
        S.add(rect(x - 140, y - 75, 400, 150, "#fff", rx=20, stroke="#748ffc", stroke_width=5))
        S.add(place(dessin, x - 80, y))
        S.add(texte(x + 110, y + 10, mot, 26, MARINE))
    return S


def p10():
    S = Scene()
    interieur(S, "#dbe4ff", "#bac8ff", 600, plinthe="#91a7ff")
    S.add(fenetre(560, 90, 180, 150, "#364fc7", nuit_=True))
    # dessin de Léon punaisé au mur
    S.add(rect(110, 90, 240, 260, "#fff", rx=4, stroke="#dee2e6", stroke_width=3), cercle(230, 96, 8, "#fa5252"))
    S.add(place(ines(0, 0, 0.75, expr="rire", bras="salut"), 230, 330))
    S.add(texte(230, 130, "Merci Inès !", 24, "#e8590c"))
    S.add(ines(560, 690, 1.45, expr="content", bras="porte", regard=(-1, 0.5)))
    S.add(table(520, 790, 440, 150, "#c68642"))
    S.add(rect(420, 600, 120, 30, "#fff", rx=3), trait(500, 610, 540, 590, "#1c7ed6", 4))
    S.add(lampe(680, 622, 0.6))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("casquette-seule.svg", vignette),
    ("01-l-uniforme.svg", p01), ("02-traverser.svg", p02), ("03-le-feu-en-panne.svg", p03),
    ("04-au-parc.svg", p04), ("05-perdu.svg", p05), ("06-chapeau-vert.svg", p06),
    ("07-chercher.svg", p07), ("08-papa.svg", p08), ("09-si-tu-te-perds.svg", p09),
    ("10-le-dessin.svg", p10),
]
