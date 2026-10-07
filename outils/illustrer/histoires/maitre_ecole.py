"""La journée du maître — une journée à l'école maternelle, côté enseignant."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from contes import chaise

ID = "maitre-ecole"
ALI = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#748ffc", jambes="#495057",
           chaussures="#343a40", acc=("lunettes",))
MILA = dict(peau="claire", cheveux="blond", coiffure="queue", habit="#f783ac", jambes="#5c7cfa",
            chaussures="#e64980")
ENFANTS = [
    dict(peau="claire", cheveux="blond", coiffure="queue", habit="#f783ac", jambes="#5c7cfa"),
    dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#ffd43b", jambes="#1c7ed6"),
    dict(peau="doree", cheveux="brun", coiffure="courts", habit="#69db7c", jambes="#495057"),
    dict(peau="rosee", cheveux="roux", coiffure="tresses", habit="#ff922b", jambes="#7048e8"),
    dict(peau="brune", cheveux="noir", coiffure="herisses", habit="#4dabf7", jambes="#343a40"),
]
TABLEAU = "#2b8a3e"


def ali(x, y, s=1.6, **k):
    return pro(x, y, s, **{**ALI, **k})


def enfant_n(i, x, y, s=0.95, **k):
    return petit(x, y, s, **{**ENFANTS[i % len(ENFANTS)], **k})


def assis(i, x, y, s=0.9, **k):
    """Enfant assis en tailleur sur le tapis ; (x, y) = sol."""
    e = ENFANTS[i % len(ENFANTS)]
    corps = petit(x, y + 34 * s, s, **{**e, "jambes": "none", "chaussures": "none", **k})
    return g([corps, ellipse(x, y - 10 * s, 48 * s, 16 * s, e["jambes"]),
              ellipse(x - 34 * s, y - 6 * s, 12 * s, 8 * s, "#495057"), ellipse(x + 34 * s, y - 6 * s, 12 * s, 8 * s, "#495057")])


def classe(S, tableau=True, fen=True):
    interieur(S, "#fff9db", "#e8c39e", 600, plinthe="#d9a066")
    if tableau:
        S.add(rect(170, 70, 460, 280, TABLEAU, rx=10, stroke="#c68642", stroke_width=12))
    if fen:
        S.add(fenetre(660, 100, 110, 160, "#a5d8ff"))


def tableau_texte(S, lignes, y0=150, taille=50):
    for k, l in enumerate(lignes):
        S.add(texte(400, y0 + k * taille * 1.25, l, taille, "#fff"))


def pot_crayons(x, y, s=1.0):
    m = [rect(-26, -50, 52, 50, "#ffa94d", rx=6)]
    for k, c in enumerate(("#fa5252", "#4dabf7", "#ffd43b", "#40c057")):
        m.insert(0, g([rect(-20 + k * 12, -96 + (k % 2) * 8, 9, 56, c, rx=2), poly([(-20 + k * 12, -96 + (k % 2) * 8), (-11 + k * 12, -96 + (k % 2) * 8), (-15.5 + k * 12, -108 + (k % 2) * 8)], "#ffe8cc")]))
    return place(m, x, y, s)


def porte_manteaux(x, y, nb=4):
    m = [rect(x, y, nb * 90, 16, "#c68642", rx=6)]
    for k in range(nb):
        m.append(cercle(x + 45 + k * 90, y + 26, 8, "#868e96"))
    return g(m)


def manteau(x, y, c):
    return chemin(f"M {x - 30} {y} Q {x} {y - 14} {x + 30} {y} L {x + 38} {y + 110} L {x - 38} {y + 110} Z", c)


def chevalet(x, y, s=1.0, dessin=""):
    m = [trait(-90, 0, -40, -320, "#a0693a", 10), trait(90, 0, 40, -320, "#a0693a", 10),
         rect(-110, -320, 220, 200, "#fff", stroke="#dee2e6", stroke_width=4), rect(-110, -120, 220, 14, "#a0693a")]
    return g([place(m, x, y, s), dessin])


def couverture():
    S = Scene()
    classe(S)
    tableau_texte(S, ["Bonjour !"], 230, 70)
    S.add(ali(560, 790, 1.8, expr="rire", bras="salut"))
    S.add(enfant_n(0, 160, 790, 1.15, expr="rire", bras="haut"))
    S.add(enfant_n(1, 330, 790, 1.15, expr="content", bras="salut", regard=(1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pot_crayons(110, 250, 1.4), livres_pile(230, 250, 1.4), pomme(330, 245, 1.4))
    return S


def p01():
    S = Scene()
    classe(S)
    S.add(horloge(400, 150, 50, 8, 0))
    for x in (140, 600):
        S.add(table(x, 760, 280, 120, "#ffa94d"))
    S.add(pot_crayons(90, 610), pot_crayons(650, 610))
    S.add(pot_peinture(170, 625, 0.6, "#fa5252"), pot_peinture(560, 625, 0.6, "#4dabf7"))
    S.add(ali(380, 790, 1.55, expr="content", bras="porte", objet=livres_pile(0, -40, 1.1)))
    return S


def p02():
    S = Scene()
    classe(S, tableau=False)
    S.add(horloge(560, 150, 60, 8, 30))
    S.add(porte_manteaux(40, 230, 4))
    for k, c in enumerate(("#fa5252", "#4dabf7", "#ffd43b")):
        S.add(manteau(85 + k * 90, 256, c))
    S.add(ali(640, 790, 1.55, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(enfant_n(2, 180, 790, 1.05, expr="joie", bras="salut", regard=(1, 0)))
    S.add(enfant_n(3, 330, 790, 1.05, expr="content", bras="bas", regard=(1, 0)))
    S.add(enfant_n(4, 470, 790, 1.05, expr="rire", bras="haut", regard=(1, 0)))
    S.add(bulle(240, 120, 340, 90, "Bonjour, maître !", 34, pointe=(260, 520)))
    return S


def p03():
    S = Scene()
    classe(S)
    tableau_texte(S, ["Lundi"], 150, 48)
    S.add(soleil(400, 260, 40, visage=True))
    S.add(tapis(400, 740, 360, 60, "#d0bfff", "#b197fc"))
    for k, x in enumerate((150, 280, 520, 650)):
        S.add(assis(k, x, 740, 0.95, expr="content" if k % 2 else "sourire", regard=(0, -1)))
    S.add(ali(400, 720, 1.25, expr="content", bras="montre", regard=(0, -1)))
    return S


def p04():
    S = Scene()
    classe(S)
    lettres = [("A", "#ffd43b", arbre(0, 30, 0.35)), ("B", "#ff8787", ballon_jeu(0, 0, 30)),
               ("C", "#74c0fc", perso("chat", 0, 40, 0.35, couleur="#ffa94d"))]
    for k, (l, c, d) in enumerate(lettres):
        x = 260 + k * 140
        S.add(texte(x, 170, l, 80, c), place(d, x, 270))
    S.add(ali(640, 790, 1.55, expr="content", bras="montre", flip=True, regard=(-1, -1)))
    S.add(enfant_n(0, 180, 790, 1.05, expr="joie", bras="haut"))
    S.add(enfant_n(2, 360, 790, 1.05, expr="concentre", bras="bas", regard=(0, -1)))
    return S


def p05():
    S = Scene()
    classe(S)
    for k in range(5):
        x = 230 + k * 85
        S.add(pomme(x, 180, 1.0, "#fa5252"), texte(x, 260, str(k + 1), 44, "#fff"))
    S.add(texte(400, 330, "5", 50, "#ffd43b"))
    S.add(ali(170, 790, 1.55, expr="content", bras="ouverts"))
    S.add(enfant_n(1, 460, 790, 1.15, expr="rire", bras="salut", regard=(-1, -0.5)))
    S.add(texte(560, 450, "5 doigts !", 40, "#e8590c", contour="#fff"))
    S.add(enfant_n(3, 640, 790, 1.05, expr="content", bras="haut"))
    return S


def p06():
    S = Scene()
    ciel(S)
    S.add(rect(0, 420, 800, 380, "#ced4da"))
    S.add(arbre(110, 450, 1.0), barriere(560, 440, 0.9, largeur=500))
    S.add(texte(560, 170, "Driiing !", 54, "#e8590c", contour="#fff"))
    S.add(enfant_n(4, 200, 760, 1.05, expr="rire", bras="course", regard=(1, 0)))
    S.add(ballon_jeu(330, 700, 32))
    S.add(enfant_n(1, 460, 740, 1.0, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(corde_sauter(556, 690, 684, 690, 170, "#e64980"))
    S.add(enfant_n(3, 620, 760, 1.0, expr="joie", bras="large"))
    S.add(ali(700, 600, 1.0, expr="sourire", bras="croises"))
    return S


def p07():
    S = Scene()
    ciel(S)
    S.add(rect(0, 420, 800, 380, "#ced4da"))
    S.add(arbre(110, 450, 1.0))
    S.add(ali(270, 790, 1.6, expr="content", bras="donne", regard=(1, 0.5)))
    S.add(petit(500, 790, 1.25, **MILA, expr="timide", bras="bas"))
    S.add(pansement(500 - 16 * 1.25, 790 - 30 * 1.25, 1.3))
    S.add(bulle(470, 150, 360, 90, "Ça va mieux ?", 40, pointe=(320, 470)))
    return S


def p08():
    S = Scene()
    classe(S, tableau=False)
    dessin = g([rect(372, 360, 56, 140, "#a0693a")] +
               [cercle(400 + dx, 330 + dy, 44, c) for dx, dy, c in
                ((-60, 10, "#fa5252"), (0, -30, "#ffd43b"), (60, 10, "#4dabf7"), (-30, 50, "#40c057"), (30, 50, "#cc5de8"))])
    S.add(chevalet(400, 720, 1.4, dessin))
    S.add(enfant_n(0, 150, 790, 1.05, expr="concentre", bras="tient", regard=(1, -1)))
    S.add(pinceau(150 + 68 * 1.05, 790 - 146 * 1.05, 1.0, "#fa5252", rot=30))
    S.add(enfant_n(2, 650, 790, 1.05, expr="rire", bras="ouverts"))
    S.add(pot_peinture(300, 780, 0.7, "#ffd43b"), pot_peinture(520, 780, 0.7, "#40c057"))
    return S


def p09():
    S = Scene()
    classe(S, tableau=False)
    S.add(lampe(120, 590, 0.8))
    S.add(chaise(400, 640, 1.1, "#c68642"))
    k = 1.4
    livre = g([rect(-50, -100, 100, 70, "#e64980", rx=4), rect(-2, -100, 4, 70, "#c2255c")])
    S.add(ali(400, 590 + 46 * k, k, expr="content", bras="porte", jambes="none", chaussures="none", objet=livre))
    S.add(rect(400 - 26 * k, 590, 20 * k, 60, ALI["jambes"], rx=8), rect(400 + 6 * k, 590, 20 * k, 60, ALI["jambes"], rx=8))
    S.add(ellipse(400 - 16 * k, 652, 22, 12, ALI["chaussures"]), ellipse(400 + 16 * k, 652, 22, 12, ALI["chaussures"]))
    S.add(tapis(400, 760, 380, 50, "#d0bfff", "#b197fc"))
    for i, x in enumerate((130, 260, 540, 670)):
        S.add(assis(i, x, 770, 0.9, expr="bouche_bee" if i % 2 else "content", regard=(0, -1)))
    S.add(etoile5(250, 180, 24, "#ffd43b"), etoile5(560, 160, 18, "#ffd43b"), lune(400, 130, 30))
    return S


def p10():
    S = Scene()
    classe(S, tableau=False)
    S.add(horloge(140, 150, 60, 4, 30))
    S.add(porte(620, 600, 180, 340, "#a5d8ff", ouverte=True))
    S.add(pro(640, 790, 1.5, peau="foncee", cheveux="noir", coiffure="boucles", habit="#20c997", jambes="#495057",
              expr="content", bras="ouverts", regard=(-1, 0)))
    S.add(enfant_n(1, 470, 790, 1.05, expr="rire", bras="haut", regard=(1, 0)))
    S.add(enfant_n(0, 300, 790, 1.05, expr="content", bras="salut", regard=(-1, 0)))
    S.add(ali(130, 790, 1.5, expr="content", bras="salut"))
    S.add(bulle(340, 120, 400, 90, "Au revoir, maître !", 34, pointe=(320, 520)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("crayons-seuls.svg", vignette),
    ("01-preparer.svg", p01), ("02-bonjour.svg", p02), ("03-quel-jour.svg", p03),
    ("04-les-lettres.svg", p04), ("05-compter.svg", p05), ("06-recreation.svg", p06),
    ("07-ca-va-mieux.svg", p07), ("08-peinture.svg", p08), ("09-une-histoire.svg", p09),
    ("10-au-revoir.svg", p10),
]
