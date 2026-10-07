"""La tournée de Rosa — une journée avec la factrice."""
from base import *
from base import _assombrir
from objets import *
from metiers import *

ID = "factrice-tournee"
JAUNE = "#fcc419"
ROSA = dict(peau="brune", cheveux="noir", coiffure="boucles", habit=JAUNE, jambes="#1971c2",
            chaussures="#343a40", tenue=veste_factrice() + bandouliere(), coiffe=casquette("#1971c2"))
ELSA = dict(peau="claire", cheveux="chatain", coiffure="queue", habit="#cc5de8", jambes="#364fc7",
            chaussures="#e64980")
JO = dict(peau="foncee", cheveux="blanc", coiffure="chauve_cote", habit="#868e96", jambes="#495057",
          barbe="#e9ecef", acc=("lunettes",))


def rosa(x, y, s=1.6, sac_=True, **k):
    r = pro(x, y, s, **{**ROSA, **k})
    if sac_ and not k.get("flip"):
        return g([r, sacoche(x + 46 * s, y - 34 * s, 0.6 * s)])
    return r


def elsa(x, y, s=1.15, **k):
    return petit(x, y, s, **{**ELSA, **k})


def capuche(c=JAUNE):
    return chemin("M -64 -132 Q -70 -220 0 -222 Q 70 -220 64 -132 L 52 -132 Q 52 -200 0 -202 Q -52 -200 -52 -132 Z",
                  c, stroke=_assombrir(c, 0.85), sw=3)


def boite_maison(x, y, s=1.0, numero="3", c="#1971c2"):
    """Boîte aux lettres de maison sur son pied ; (x, y) = sol."""
    return place([rect(-6, -120, 12, 120, "#868e96"), rect(-50, -200, 100, 84, c, rx=12),
                  rect(-32, -176, 64, 8, "#212529", rx=3), texte(0, -132, numero, 30, "#fff")], x, y, s)


def boite_rue(x, y, s=1.0, c=JAUNE):
    """Boîte aux lettres de rue, jaune ; (x, y) = sol."""
    return place([rect(-10, -100, 20, 100, "#495057"), rect(-60, -260, 120, 170, c, rx=14),
                  chemin("M -60 -246 Q 0 -300 60 -246 Z", c), rect(-36, -230, 72, 10, "#212529", rx=4),
                  lettre(0, -170, 0.6)], x, y, s)


def velo_factrice(x, y, s=1.0, flip=False):
    return g([velo(x, y, s, "#fcc419", flip=flip),
              place([rect(-120, -150, 90, 70, "#1971c2", rx=10), rect(-120, -150, 90, 16, "#1864ab", rx=6),
                     rect(60, -150, 60, 46, "#1971c2", rx=8)], x, y, s, flip=flip)])


def rue_maisons(S, y=640, pluie_=False):
    ciel(S, "#868e96" if pluie_ else "#74c0fc", "#dee2e6" if pluie_ else "#e7f5ff")
    S.add(rect(0, y - 20, 800, 820 - y, "#8ce99a"))
    S.add(rect(0, y + 40, 800, 120, "#ced4da"))


def couverture():
    S = Scene()
    rue_maisons(S)
    S.add(maison(640, 620, 1.2, mur="#ffd8a8", toit="#e64980"))
    S.add(velo_factrice(170, 760, 1.25))
    S.add(rosa(420, 780, 1.75, expr="rire", bras="montre"))
    S.add(lettre(420 + 86 * 1.75, 780 - 130 * 1.75 - 16, 0.9, rot=-10))
    S.add(lettre(660, 180, 0.8, rot=12), lettre(140, 160, 0.7, rot=-14, timbre="#4dabf7"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(boite_maison(110, 268, 0.85, "5"))
    S.add(colis(290, 250, 1.1), lettre(250, 90, 0.9, rot=-10))
    return S


def p01():
    S = Scene()
    interieur(S, "#e7f5ff", "#adb5bd", 600, plinthe="#868e96")
    for x in (30, 570):
        S.add(rect(x, 120, 200, 480, "#c68642", rx=6))
        for k in range(4):
            yy = 220 + k * 110
            S.add(rect(x, yy, 200, 12, "#a0693a"))
            for j in range(3):
                S.add(colis(x + 40 + j * 62, yy, 0.45, c=["#d9a066", "#e9c58b", "#c68642"][(j + k) % 3]))
    for k in range(9):
        S.add(lettre(470 + (k % 3) * 70, 600 - (k // 3) * 28, 0.75, rot=(k * 17) % 30 - 15,
                     timbre=["#fa5252", "#4dabf7", "#40c057"][k % 3]))
    S.add(rect(420, 600, 280, 130, "#1971c2", rx=10))
    S.add(rosa(250, 790, 1.55, expr="surpris", bras="ouverts", sac_=False))
    return S


def p02():
    S = Scene()
    interieur(S, "#e7f5ff", "#adb5bd", 600, plinthe="#868e96")
    S.add(rect(320, 80, 440, 440, "#c68642", rx=8))
    for r in range(4):
        for c in range(4):
            x, y = 334 + c * 106, 94 + r * 106
            S.add(rect(x, y, 96, 96, "#fff4e6", rx=4))
            S.add(texte(x + 48, y + 88, str(1 + r * 4 + c), 20, "#a0693a"))
            if (r + c) % 2 == 0:
                S.add(rect(x + 14, y + 20, 68, 44, "#fff", rx=3, stroke="#ced4da", stroke_width=2))
    S.add(rosa(200, 790, 1.6, expr="concentre", bras="montre", regard=(1, -0.5), sac_=False))
    S.add(lettre(200 + 86 * 1.6 + 6, 790 - 130 * 1.6 - 14, 0.7, rot=-8))
    return S


def p03():
    S = Scene()
    rue_maisons(S)
    S.add(maison(140, 620, 1.1), maison(660, 620, 1.1, mur="#d0bfff", toit="#7048e8"))
    S.add(velo_factrice(470, 770, 1.35))
    S.add(rosa(230, 790, 1.6, expr="rire", bras="tire", regard=(1, 0)))
    S.add(texte(560, 330, "Dring, dring !", 54, "#1971c2", contour="#fff"))
    return S


def p04():
    S = Scene()
    rue_maisons(S)
    S.add(maison(200, 620, 1.2, mur="#ffec99", toit="#f08c00"), maison(600, 620, 1.2, mur="#c3fae8", toit="#0ca678"))
    S.add(boite_maison(110, 720, 0.9, "3"), boite_maison(700, 720, 0.9, "5", "#e64980"))
    S.add(rosa(400, 790, 1.55, expr="content", bras="donne", flip=True, regard=(-1, 0)))
    S.add(lettre(400 - 84 * 1.55 - 30, 790 - 92 * 1.55, 0.7, rot=10))
    return S


def p05():
    S = Scene()
    rue_maisons(S, pluie_=True)
    S.add(nuage(180, 120, 1.1, "#adb5bd"), nuage(600, 100, 1.2, "#adb5bd"))
    pluie(S, 70, 7, (0, 160, 800, 760))
    S.add(velo_factrice(530, 770, 1.3))
    S.add(rosa(250, 790, 1.6, expr="content", bras="hanches", coiffe=capuche(), habit="#ffd43b"))
    S.add(flaque(380, 760, 1.2, eclabousse=True))
    S.add(texte(560, 520, "Au sec !", 44, "#1971c2", contour="#fff"))
    return S


def p06():
    S = Scene()
    rue_maisons(S)
    S.add(maison(560, 620, 1.3, mur="#ffc9c9", toit="#c92a2a"))
    S.add(barriere(520, 700, 1.0, largeur=520))
    S.add(perso("chien", 600, 760, 1.15, expr="joie", bras="saute", regard=(-1, 0)))
    S.add(texte(620, 330, "Wouf !", 60, "#a0693a", contour="#fff"))
    S.add(rosa(200, 790, 1.6, expr="rire", bras="salut", regard=(1, 0)))
    return S


def p07():
    S = Scene()
    rue_maisons(S)
    S.add(rect(420, 200, 380, 440, "#ffe8cc"), poly([(400, 210), (620, 90), (820, 210)], "#e8590c"))
    S.add(porte(600, 640, 150, 300, "#a0522d", ouverte=True))
    S.add(pro(600, 790, 1.5, **JO, expr="content", bras="ouverts", regard=(-1, 0)))
    S.add(rosa(260, 790, 1.6, expr="concentre", bras="porte", sac_=False,
               objet=colis(0, -30, 0.95, 140, 110)))
    return S


def p08():
    S = Scene()
    rue_maisons(S)
    S.add(maison(400, 620, 1.6, mur="#e5dbff", toit="#7048e8"))
    S.add(barriere(400, 700, 1.0, largeur=800))
    S.add(elsa(560, 790, 1.3, expr="joie", bras="haut"))
    S.add(rosa(230, 790, 1.6, expr="content", bras="bas", regard=(1, 0)))
    S.add(bulle(520, 120, 380, 100, "Il y a une lettre\npour moi ?", 34, pointe=(560, 470)))
    return S


def p09():
    S = Scene()
    rue_maisons(S)
    S.add(maison(400, 620, 1.25, mur="#e5dbff", toit="#7048e8"))
    carte = g([rect(-80, -60, 160, 110, "#fff", rx=6, stroke="#ced4da", stroke_width=3),
               rect(-72, -52, 144, 50, "#a5d8ff"), chemin("M -72 -10 q 18 -12 36 0 t 36 0 t 36 0 t 36 0 L 72 -2 L -72 -2 Z", "#1c7ed6"),
               soleil(40, -38, 10, rayons=False), rect(-72, -2, 144, 16, "#ffe066")])
    S.add(elsa(480, 790, 1.5, expr="rire", bras="porte", objet=place(carte, 0, -70, 0.75)))
    S.add(rosa(200, 790, 1.5, expr="content", bras="hanches"))
    S.add(rect(270, 40, 260, 170, "#fff", rx=8, stroke="#ced4da", stroke_width=4))
    S.add(place(carte, 400, 135, 1.4))
    S.add(texte(400, 250, "De la part de Mamie", 28, "#e64980", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#ff8787", "#ffd8a8")
    S.add(soleil(150, 520, 60, "#ff922b"))
    S.add(rect(0, 600, 800, 200, "#ced4da"))
    S.add(boite_rue(520, 720, 1.2))
    S.add(elsa(330, 760, 1.5, expr="content", bras="donne", regard=(1, -0.5)))
    S.add(lettre(330 + 84 * 1.5 + 30, 760 - 92 * 1.5, 0.6, rot=-20))
    S.add(texte(560, 160, "À demain, Mamie !", 44, "#c2255c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lettre-seule.svg", vignette),
    ("01-le-centre-de-tri.svg", p01), ("02-trier.svg", p02), ("03-dring.svg", p03),
    ("04-les-boites.svg", p04), ("05-la-pluie.svg", p05), ("06-wouf.svg", p06),
    ("07-le-colis.svg", p07), ("08-elsa-attend.svg", p08), ("09-la-carte.svg", p09),
    ("10-la-reponse.svg", p10),
]
