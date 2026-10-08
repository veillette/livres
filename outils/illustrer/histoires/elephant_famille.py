"""La famille éléphant — la vie de l'éléphant d'Afrique.

La famille est guidée par la plus vieille femelle, la grand-mère ; les mâles
adultes vivent à part. L'éléphanteau boit le lait de sa mère (les mamelles
sont entre les pattes de devant). La trompe est le nez et la lèvre : elle
sent, attrape, et aspire l'eau qu'elle verse ensuite dans la bouche. Les
bains de boue protègent la peau du soleil et des insectes ; les grandes
oreilles qu'il agite le rafraîchissent. Les défenses sont des dents. Les
éléphants se parlent avec des grondements très graves qu'ils sentent aussi
avec leurs pattes. Face au danger, les grands entourent les petits.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import ondes, fleche

ID = "elephant-famille"
GRIS = "#adb5bd"
BOUE = "#8d6e4a"


# --- Personnages ------------------------------------------------------------

def elephant(x, y, s=1.0, flip=False, expr="sourire", trompe="bas", bebe=False, oreille=0, boue=False,
             couleur=GRIS, defenses=True, regard=(1, 0)):
    """Éléphant d'Afrique de profil, tête à droite ; (x, y) = sous les pattes.
    trompe : "bas", "haut" (barrit), "bouche" (vers la bouche), "herbe" (tient
    une touffe d'herbe), "eau" (douche), "suce" (au coin de la bouche, comme un
    pouce), "devant" (tendue en avant). oreille : angle d'ouverture."""
    ys, bs, ss = EXPRESSIONS[expr]
    c = couleur
    fonce = _assombrir(c, 0.82)
    tete = 1.25 if bebe else 1.0
    m = []
    # queue et pattes du fond
    m.append(chemin("M -146 -230 Q -166 -190 -160 -140", stroke=fonce, sw=7))
    m.append(ellipse(-160, -134, 6, 12, "#495057"))
    for px in (-70, 60):
        m.append(rect(px - 26, -170, 52, 170, fonce, rx=18))
    # corps
    m.append(ellipse(0, -205, 150, 108, c))
    m.append(chemin("M -110 -290 Q 0 -330 110 -280", stroke=eclaircir(c, 0.25), sw=10, opacity=0.6))
    # pattes de devant
    for px in (-110, 100):
        m.append(rect(px - 28, -160, 56, 160, c, rx=18))
        m.append(ellipse(px, -4, 30, 8, eclaircir(c, 0.4)))
        for k in range(3):
            m.append(trait(px - 16, -60 + k * 14, px + 16, -60 + k * 14, fonce, 2.5))
    if boue:
        r = random.Random(4)
        for _ in range(9):
            m.append(ellipse(r.uniform(-130, 120), r.uniform(-290, -140), r.uniform(20, 46), r.uniform(14, 30), BOUE, opacity=0.85))
    # tête
    T = []
    T.append(ellipse(150, -260, 72, 78, c))
    # trompe
    if trompe == "bas":
        d = "M 196 -240 Q 236 -190 226 -120 Q 220 -70 236 -40"
    elif trompe == "haut":
        d = "M 196 -250 Q 250 -280 250 -340 Q 250 -380 280 -390"
    elif trompe == "bouche":
        d = "M 196 -240 Q 250 -190 230 -150 Q 210 -130 190 -160"
    elif trompe == "herbe":
        d = "M 196 -240 Q 240 -180 250 -110 Q 254 -60 270 -40"
    elif trompe == "eau":
        d = "M 196 -250 Q 230 -300 190 -340 Q 140 -370 90 -340"
    elif trompe == "suce":
        d = "M 196 -240 Q 226 -200 206 -170 Q 194 -156 180 -170"
    else:  # devant
        d = "M 196 -250 Q 260 -240 300 -220 Q 330 -210 350 -230"
    T.append(chemin(d, stroke=c, sw=34))
    if defenses and not bebe:
        T.append(chemin("M 186 -200 Q 214 -150 250 -150", stroke="#fff9db", sw=13))
    T.append(chemin("M 174 -196 Q 186 -180 200 -196", stroke=ENCRE, sw=3.5) if bs not in ("ouverte", "o", "crie")
             else ellipse(186, -192, 10, 8, ROUGE_BOUCHE))
    # oreille (devant la tête), qui peut s'écarter comme un éventail
    oreille_d = "M 120 -330 Q 30 -350 26 -260 Q 22 -170 90 -150 Q 110 -160 112 -190 Q 140 -230 120 -330 Z"
    dedans = "M 110 -316 Q 44 -330 40 -260 Q 38 -190 88 -168 Q 102 -180 100 -200 Q 124 -236 110 -316 Z"
    T.append(g([chemin(oreille_d, c), chemin(dedans, "#f3c4c4", opacity=0.5)],
               transform=f"rotate({-oreille} 112 -260)" if oreille else None))
    T.append(oeil(172, -272, ys, regard, taille=1.0))
    T.append(joue(190, -232, 1.0))
    if bebe:
        T.append(chemin("M 120 -334 q 10 -14 20 0 q 10 -14 20 0", stroke=fonce, sw=3))
    m.append(g(T, transform=f"translate({n(150 * (1 - tete))} {n(-260 * (1 - tete) + (40 if bebe else 0))}) scale({tete})" if bebe else None))
    return place(m + [occuper(-166, -338, 250, 4)], x, y, s, flip=flip)


def savane_soir(S, y=560):
    S.add(rect(0, 0, 800, 800, S.degrade(["#f76707", "#ffa94d", "#ffe8cc"])))
    S.add(cercle(560, y - 60, 90, "#fff3bf", opacity=0.9))
    S.add(acacia(160, y, 0.8, "#2b2b3a", "#343a40", "#2b2b3a"))
    S.add(rect(0, y, 800, 800 - y, "#a0693a"))


def point_eau(S, y=560):
    savane(S, y)
    S.add(ellipse(400, y + 150, 360, 90, "#74c0fc"))
    S.add(ellipse(400, y + 150, 330, 76, "#a5d8ff", opacity=0.4))


def touffe(x, y, s=1.0):
    return place([chemin(f"M {k * 8 - 20} 0 q {k * 4 - 10} -30 {k * 6 - 14} -50", stroke="#94d82d", sw=5) for k in range(6)], x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    savane(S, 600)
    S.add(elephant(330, 740, 1.15, expr="content", trompe="bas"))
    S.add(elephant(560, 760, 0.55, bebe=True, expr="rire", trompe="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(elephant(135, 262, 0.6, expr="content"))
    S.add(elephant(290, 262, 0.3, bebe=True, expr="rire", trompe="haut"))
    return S


def p01():
    S = Scene()
    savane(S, 520)
    for x, y, sc, b, e in [(630, 640, 0.7, False, "fier"), (420, 660, 0.6, False, "sourire"), (300, 700, 0.32, True, "content"),
                           (190, 650, 0.6, False, "sourire"), (80, 700, 0.3, True, "rire")]:
        S.add(elephant(x, y, sc, bebe=b, expr=e))
    S.add(etiquette(630, 330, "la grand-mère", 32, "#0c8599"))
    return S


def p02():
    S = Scene()
    savane(S, 560)
    S.add(elephant(360, 760, 1.25, expr="content", trompe="bouche", regard=(-1, 1)))
    S.add(elephant(300, 760, 0.42, bebe=True, expr="miam", trompe="haut"))
    S.add(coeur(640, 220, 1.2, "#ff8787"))
    return S


def p03():
    S = Scene()
    savane(S, 560)
    S.add(touffe(560, 760, 1.6))
    S.add(elephant(270, 770, 1.2, expr="miam", trompe="herbe"))
    S.add(touffe(590, 760, 1.2))
    S.add(g([chemin(f"M {610 + k * 20} {440 + k * 10} q 14 -6 28 0", stroke="#495057", sw=3) for k in range(3)]))
    return S


def p04():
    S = Scene()
    point_eau(S, 560)
    S.add(elephant(250, 680, 1.05, expr="content", trompe="bouche"))
    S.add(g([goutte(540, 600 + k * 28, 0.7, "#74c0fc") for k in range(3)]))
    S.add(texte(560, 260, "Slurp !", 64, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    savane(S, 560)
    S.add(ellipse(400, 720, 380, 70, BOUE))
    S.add(elephant(300, 740, 1.0, expr="rire", trompe="eau", boue=True))
    r = random.Random(3)
    for _ in range(14):
        S.add(goutte(r.uniform(80, 330), r.uniform(330, 520), 0.8, BOUE))
    S.add(elephant(620, 760, 0.45, bebe=True, expr="rire", trompe="haut", boue=True))
    S.add(soleil(660, 110, 55))
    return S


def p06():
    S = Scene()
    savane(S, 560)
    S.add(soleil(120, 110, 60))
    S.add(elephant(360, 760, 1.25, expr="content", oreille=34, trompe="bas"))
    S.add(mouvement(130, 380, 1.2, "#495057", rot=180), mouvement(150, 470, 1.0, "#495057", rot=180))
    S.add(texte(620, 170, "Flap ! Flap !", 50, "#0c8599", contour="#fff"))
    return S


def p07():
    S = Scene()
    savane(S, 560)
    S.add(elephant(300, 760, 1.2, expr="concentre", trompe="haut", regard=(1, 0.6)))
    S.add(ellipse(600, 740, 70, 20, "#a0693a"))
    S.add(g([cercle(560 + k * 22, 720 - (k % 2) * 14, 9, "#c08a52") for k in range(5)]))
    S.add(etiquette(640, 470, "les défenses", 34, "#0c8599"), fleche(630, 490, 600, 560, "#0c8599", 5, 16))
    return S


def p08():
    S = Scene()
    savane(S, 560)
    S.add(elephant(600, 760, 0.95, expr="content", trompe="bas", flip=True, regard=(1, 0.6)))
    S.add(elephant(270, 760, 0.7, bebe=True, expr="content", trompe="suce"))
    S.add(texte(250, 200, "Slurp…", 54, "#0c8599", contour="#fff"))
    return S


def p09():
    S = Scene()
    savane(S, 560, arbres=False)
    S.add(elephant(160, 720, 0.6, expr="chante", trompe="haut"))
    S.add(elephant(680, 720, 0.45, expr="surpris", flip=True, regard=(1, 0)))
    S.add(ondes(300, 640, 50, 4, 70, 0, 50, "#0c8599", 6))
    for k in range(4):
        S.add(chemin(f"M {260 + k * 70} {760} q 17 -12 34 0 t 34 0", stroke="#a0693a", sw=5))
    S.add(texte(400, 300, "Grrrooonnn…", 56, "#0c8599", contour="#fff"))
    return S


def p10():
    S = Scene()
    savane_soir(S, 560)
    S.add(elephant(180, 740, 0.75, expr="fier"))
    S.add(elephant(620, 740, 0.75, expr="fier", flip=True))
    S.add(elephant(400, 760, 0.42, bebe=True, expr="content"))
    S.add(elephant(400, 640, 0.6, expr="sourire", trompe="haut"))
    S.cachette(130, 380, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("elephants-seuls.svg", vignette),
    ("01-la-famille.svg", p01), ("02-le-lait.svg", p02), ("03-la-trompe.svg", p03),
    ("04-boire.svg", p04), ("05-le-bain-de-boue.svg", p05), ("06-les-oreilles.svg", p06),
    ("07-les-defenses.svg", p07), ("08-le-bebe-apprend.svg", p08), ("09-se-parler.svg", p09),
    ("10-tous-ensemble.svg", p10),
]
