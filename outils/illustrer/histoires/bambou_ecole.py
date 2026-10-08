"""Le premier jour de Bambou — la séparation du premier jour d'école."""
from base import *
from objets import *

ID = "bambou-ecole"
ROUGE = "#e03131"


def cartable(couleur="#4dabf7"):
    """Cartable dans le dos (dessin `derriere` de perso)."""
    return g([rect(-62, -150, 124, 110, couleur, rx=18), rect(-62, -150, 124, 30, "#1c7ed6", rx=14)])


def bambou(x, y, s=1.0, sac=True, **k):
    k.setdefault("habit", "#ffd43b")
    return perso("panda", x, y, s, derriere=cartable() if sac else None, **k)


def papa(x, y, s=1.5, **k):
    return perso("panda", x, y, s, habit="#40c057", acc=("lunettes",), **k)


def maitre(x, y, s=1.35, **k):
    return perso("herisson", x, y, s, habit="#7048e8", acc=("lunettes",), **k)


def capucine(x, y, s=0.95, **k):
    return perso("lapin", x, y, s, habit="#f783ac", acc=("noeud",), couleur_acc="#ae3ec9", **k)


def petit_coeur(x, y, s=1.0):
    return coeur(x, y, s, ROUGE)


def ecole(S):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(700, 90, 40))
    toit = [(60, 190), (400, 70), (740, 190)]
    S.add(ombre_sol(410, 600, 360, 16, 0.16))
    S.add(rect(80, 180, 640, 420, cylindre("#ffe8cc", 0.2, 0.86)), briques(80, 180, 640, 420, "#ffe8cc", hb=22, lb=50))
    S.add(rect(80, 180, 16, 420, "#fff4e6"), rect(704, 180, 16, 420, "#e8cfae"))
    S.add(rect(72, 570, 656, 30, cylindre("#ced4da", 0.3, 0.75), rx=2))
    S.add(ombre_avancee(80, 186, 640, 30, 0.25))
    S.add(poly(toit, lineaire([(0, "#ff8a3d"), (0.5, "#e8590c"), (1, "#a63d00")], 0, 0, 1, 1)), tuiles(60, 70, 680, 120, "#e8590c", poly(toit, "#000"), pas_=20))
    S.add(chemin("M 60 190 L 400 70 L 740 190", stroke="#8a3200", sw=7), rect(52, 186, 696, 10, "#8a3200", rx=4))
    S.add(rect(316, 386, 168, 214, "#f1f3f5", rx=10), rect(322, 590, 156, 10, "#adb5bd", rx=2))
    S.add(rect(300, 200, 200, 60, "#fff", rx=10), texte(400, 245, "ÉCOLE", 42, "#e8590c"))
    for x in (130, 560):
        S.add(fenetre(x, 300, 110, 100, "#d0ebff"))
    S.add(rect(330, 400, 140, 200, cylindre("#4dabf7", 0.25, 0.72), rx=8), cercle(445, 500, 8, volume("#ffd43b", 0.6, 0.7)))
    S.add(trait(400, 400, 400, 590, "#1c7ed6", 3), rect(345, 420, 40, 60, "#d0ebff", rx=4), rect(415, 420, 40, 60, "#d0ebff", rx=4))
    sol(S, 600, "#ced4da", bosse=0)
    S.add(barriere(130, 650, 1.0, "#74c0fc", 220), barriere(670, 650, 1.0, "#74c0fc", 220))


def classe(S):
    interieur(S, "#fff9db", "#e9c38c", 580, papier="#fff3bf")
    S.add(rect(240, 90, 320, 180, "#2b8a3e", rx=8, stroke="#a0693a", stroke_width=12))
    S.add(texte(400, 170, "A B C", 54, "#fff"), texte(400, 235, "1 2 3", 44, "#ffe066"))
    S.add(g([rect(60 + k * 46, 330, 30, 40, c, rx=4) for k, c in enumerate(["#ff8787", "#ffd43b", "#69db7c", "#4dabf7"])]))
    S.add(trait(50, 370, 250, 370, "#a0693a", 8))


def couverture():
    S = Scene()
    ecole(S)
    S.add(bambou(400, 790, 1.85, expr="timide", bras="montre", regard=(1, -0.5)))
    S.add(petit_coeur(590, 470, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bambou(200, 264, 1.0, expr="content", bras="salut"))
    S.add(petit_coeur(300, 120, 0.7))
    return S


def p01():
    S = Scene()
    ecole(S)
    S.add(papa(250, 780, expr="sourire", bras="donne", regard=(1, 0.3)))
    S.add(bambou(470, 780, 1.1, expr="inquiet", bras="bas"))
    return S


def p02():
    S = Scene()
    ecole(S)
    S.add(papa(220, 820, 1.35, expr="content", bras="porte", regard=(1, 0.5)))
    S.add(bambou(450, 790, 1.15, expr="surpris", bras="donne", regard=(0, 0.5)))
    # zoom sur la main
    S.add(cercle(620, 250, 120, "#fff", stroke="#868e96", stroke_width=6))
    S.add(ellipse(620, 270, 70, 80, "#343a40"), petit_coeur(620, 255, 1.4))
    S.add(trait(560, 530, 590, 370, "#868e96", 4, stroke_dasharray="10 8"))
    return S


def p03():
    S = Scene()
    ecole(S)
    S.add(papa(400, 820, 1.6, expr="sourire", bras="calin", regard=(0, 1)))
    S.add(bambou(360, 790, 1.0, expr="pleure", bras="calin", sac=True, larmes=True))
    S.add(maitre(680, 790, 1.0, expr="sourire", bras="salut", regard=(-1, 0)))
    S.cachette(70, 150, "air")
    return S


def p04():
    S = Scene()
    classe(S)
    S.add(maitre(560, 780, 1.4, expr="sourire", bras="montre", regard=(-1, 0.4)))
    S.add(bambou(260, 780, 1.1, expr="triste", bras="yeux", larmes=True))
    S.add(tour_cubes(700, 790, 0.9, 3, graine=2))
    return S


def p05():
    S = Scene()
    classe(S)
    S.add(tapis(400, 730, 300, 55, "#d0ebff", "#74c0fc"))
    S.add(bambou(250, 760, 1.1, sac=False, expr="timide", bras="montre", regard=(1, 0)))
    S.add(capucine(560, 760, 1.05, expr="triste", bras="bas", regard=(-1, 0)))
    S.add(cube(400, 760, 1.0, "#ff8787", "B"), cube(450, 770, 0.9, "#69db7c", "C"))
    S.add(pensee(250, 210, 70, petit_coeur(250, 210, 1.1), depuis=(250, 420)))
    return S


def p06():
    S = Scene()
    classe(S)
    S.add(tour_cubes(400, 760, 1.1, 6, graine=5))
    S.add(bambou(220, 770, 1.05, sac=False, expr="rire", bras="haut"))
    S.add(capucine(590, 770, 1.0, expr="rire", bras="haut"))
    S.add(pot_peinture(720, 790, 0.8, "#ff922b"), pinceau(80, 770, 1.0, "#4dabf7"))
    S.add(texte(640, 420, "Youpi !", 60, "#e8590c", contour="#fff", rot=8))
    return S


def petit_lit(x, y, couverture_c, qui=""):
    m = [rect(x - 110, y - 40, 220, 40, "#c68642", rx=8), rect(x - 100, y - 70, 70, 34, "#fff", rx=14)]
    if qui:
        m.append(qui)
    m.append(rect(x - 60, y - 66, 160, 40, couverture_c, rx=14))
    return g(m)


def dans_lit(S, x, y, w, couv, qui):
    S.add(lit(x, y, w, "#74c0fc", couv))
    S.add(qui)
    S.add(rect(x - w / 2 + 60, y - 125, w - 60, 85, couv, rx=18))


def p07():
    S = Scene()
    interieur(S, "#d0bfff", "#b197fc", 560, papier="#c0aaff")
    S.add(rect(0, 0, 800, 800, "#1c2a52", opacity=0.25))
    dans_lit(S, 220, 780, 300, "#74c0fc", perso("lapin", 140, 720, 0.55, expr="dort", acc=("noeud",), couleur_acc="#ae3ec9"))
    dans_lit(S, 580, 780, 300, "#ffd43b", perso("panda", 500, 720, 0.55, expr="sourire", regard=(1, -1)))
    S.add(pensee(560, 280, 90, petit_coeur(560, 280, 1.6), depuis=(510, 520)))
    S.add(zzz(220, 470, 1.0, "#fff3bf"))
    return S


def p08():
    S = Scene()
    ecole(S)
    S.add(papa(280, 790, 1.45, expr="rire", bras="ouverts"))
    S.add(bambou(480, 790, 1.1, expr="rire", bras="court", regard=(1, 0), flip=True))
    S.add(capucine(660, 790, 0.95, expr="rire", bras="coucou"))
    S.add(coeur(380, 330, 1.0, "#ff8787"), coeur(560, 300, 0.7, "#ff8787"))
    S.cachette(70, 150, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bambou-seul.svg", vignette),
    ("01-le-premier-jour.svg", p01), ("02-le-coeur.svg", p02), ("03-ne-pars-pas.svg", p03), ("04-le-maitre.svg", p04),
    ("05-capucine.svg", p05), ("06-la-tour.svg", p06), ("07-la-sieste.svg", p07), ("08-papa-est-la.svg", p08),
]
