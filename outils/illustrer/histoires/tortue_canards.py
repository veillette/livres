"""La Tortue et les deux Canards — savoir se taire."""
from fables import *

ID = "tortue-canards"

CANARD1 = dict(couleur="#f1f3f5")
CANARD2 = dict(couleur="#ffe8cc")


def canard_(x, y, s=1.0, n_=0, **k):
    k.setdefault("nage", False)
    k.setdefault("regard", (1, 0))
    return canard(x, y, s, **{**(CANARD1 if n_ == 0 else CANARD2), **k})


def voyage(x, y, s=1.0, tortue_expr="concentre", canards_expr="rire", bouche_ouverte=False):
    """La tortue accrochée au bâton par la bouche, un canard à chaque bout.

    (x, y) = sous la tortue. Les deux canards se font face."""
    m = []
    by = -50  # hauteur de la bouche de la tortue
    # le bout du bec d'un canard est à (114, -103) de ses pattes (échelle 1.1)
    m.append(canard(-254, by + 103, 1.1, nage=False, ailes="haut", expr=canards_expr, **CANARD1))
    m.append(canard(364, by + 103, 1.1, nage=False, ailes="haut", expr=canards_expr, flip=True, **CANARD2))
    if not bouche_ouverte:
        m.append(baton(-140, by, 250, by, ep=10))
    m.append(tortue(0, 0, 1.0, expr=tortue_expr))
    return place(m, x, y, s)


def etang_(S, soleil_=True):
    ciel(S, "#a5d8ff", "#e7f5ff")
    if soleil_:
        S.add(soleil(680, 110, 46))
    collines(S, 560, "#b2f2bb", graine=51)
    sol(S, 580, "#8ce99a")
    S.add(ellipse(560, 700, 320, 90, "#4dabf7"))
    S.add(nenuphar(470, 700, 0.8), nenuphar(640, 720, 0.7))
    S.add(herbe(90, 640, 1.2), fleur(140, 680, 0.8, "#ff8787"))


def ciel_haut(S):
    ciel(S, "#74c0fc", "#d0ebff")
    S.add(nuage(140, 160, 0.8), nuage(620, 600, 0.9), nuage(700, 140, 0.5))


def vue_du_ciel(S):
    ciel(S, "#74c0fc", "#d0ebff")
    rr = random.Random(3)
    couleurs = ["#b2f2bb", "#8ce99a", "#ffe066", "#d8f5a2", "#c0eb75", "#ffd8a8"]
    for i in range(6):
        for j in range(4):
            S.add(poly([(i * 150 - 40 + rr.uniform(-10, 10), 420 + j * 100), (i * 150 + 120, 410 + j * 100), (i * 150 + 130, 520 + j * 100), (i * 150 - 30, 520 + j * 100)], rr.choice(couleurs)))
    S.add(chemin("M 0 560 Q 200 500 400 600 T 800 540", stroke="#4dabf7", sw=26))
    for tx, ty in [(80, 460), (300, 700), (520, 480), (700, 720), (620, 440)]:
        S.add(cercle(tx, ty, 22, "#2f9e44"), cercle(tx + 20, ty + 8, 18, "#37b24d"))
    S.add(rect(0, 400, 800, 20, "#fff", opacity=0.4))


def village(S):
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 620, "#8ce99a")
    S.add(maison(120, 640, 0.8, toit="#c92a2a"), maison(680, 650, 0.7, toit="#1c7ed6"))


def couverture():
    S = Scene()
    ciel_haut(S)
    collines(S, 720, "#8ce99a", graine=5)
    S.add(rect(0, 700, 800, 100, "#8ce99a"))
    S.add(voyage(359, 470, 0.75, "content"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(baton(40, 140, 360, 120, ep=16))
    return S


def p01():
    S = Scene()
    etang_(S)
    S.add(tortue(300, 700, 1.7, expr="content"))
    return S


def p02():
    S = Scene()
    etang_(S)
    S.add(tortue(240, 700, 1.5, expr="triste", regard=(1, -1)))
    reve = g([montagnes(None, 300, ("#b197fc", "#9775fa")), rect(260, 300, 360, 40, "#4dabf7")])
    cid = uid("r")
    S.add(pensee(500, 250, 200, depuis=(430, 560), contenu=""))
    S.add(el("clipPath", ellipse(500, 250, 180, 140, "#000"), id=cid))
    S.add(g(place(reve, 500 - 400 * 0.45, 250 - 250 * 0.45 - 20, 0.45), clip_path=f"url(#{cid})"))
    return S


def p03():
    S = Scene()
    etang_(S)
    S.add(tortue(180, 690, 1.2, expr="surpris", regard=(1, -1)))
    S.add(canard(470, 700, 1.3, expr="rire", **CANARD1))
    S.add(canard(640, 720, 1.2, expr="content", flip=True, **CANARD2))
    S.add(bulle(520, 160, 440, 110, "Nous partons voir\nle vaste monde !", 34, pointe=(520, 520)))
    S.cachette(740, 330, "air")
    return S


def p04():
    S = Scene()
    etang_(S)
    S.add(tortue(240, 700, 1.5, expr="inquiet", regard=(1, -1)))
    S.add(canard(560, 710, 1.1, expr="surpris", flip=True, **CANARD1))
    S.add(canard(700, 730, 1.0, expr="surpris", flip=True, **CANARD2))
    S.add(bulle(330, 150, 460, 110, "Emmenez-moi !\nMais je ne sais pas voler…", 32, pointe=(380, 520)))
    S.cachette(740, 330, "air")
    return S


def p05():
    S = Scene()
    etang_(S)
    S.add(tortue(200, 700, 1.3, expr="surpris", regard=(1, 0)))
    S.add(baton(420, 620, 700, 610, ep=12))
    S.add(canard_(470, 700, 1.1, 0, expr="rire"))
    S.add(canard_(660, 700, 1.1, 1, expr="malin", flip=True))
    S.add(bulle(560, 170, 400, 90, "Nous avons une idée !", 34, pointe=(560, 540)))
    S.cachette(740, 330, "air")
    return S


def p06():
    S = Scene()
    etang_(S)
    S.add(voyage(353, 720, 0.85, "concentre", "neutre"))
    S.add(bulle(400, 150, 560, 120, "Serre bien le bâton,\net surtout, n'ouvre pas la bouche !", 30, pointe=(170, 560)))
    return S


def p07():
    S = Scene()
    etang_(S)
    S.add(voyage(353, 480, 0.85, "content", "rire"))
    S.add(mouvement(360, 580, 1.2, rot=90))
    S.add(texte(620, 240, "Hop !", 64, "#0c8599", contour="#fff"))
    return S


def p08():
    S = Scene()
    vue_du_ciel(S)
    S.add(voyage(353, 280, 0.85, "content", "content"))
    S.add(nuage(120, 110, 0.6))
    S.cachette(730, 140, "air")
    return S


def p09():
    S = Scene()
    village(S)
    S.add(voyage(367, 250, 0.6, "content", "content"))
    S.add(personne(300, 770, 1.3, coiffure="courts", cheveux="brun", habit="#fab005", robe=False, expr="bouche_bee", bras="montre", regard=(1, -1)))
    S.add(personne(520, 770, 1.3, coiffure="longs", cheveux="roux", habit="#e64980", expr="surpris", bras="joues", regard=(0, -1)))
    S.add(bulle(320, 440, 360, 90, "Une tortue qui vole !", 30, pointe=(310, 530)))
    return S


def p10():
    S = Scene()
    village(S)
    S.add(voyage(367, 250, 0.6, "fier", "content"))
    S.add(enfant(250, 770, 1.1, habit="#51cf66", expr="rire", bras="haut"))
    S.add(enfant(420, 770, 1.1, habit="#ff922b", robe=True, coiffure="tresses", cheveux="blond", expr="rire", bras="haut"))
    S.add(enfant(590, 770, 1.1, habit="#4dabf7", expr="joie", bras="salut", peau="brune", cheveux="noir", coiffure="boucles"))
    S.add(texte(400, 460, "La reine des tortues !", 44, "#0c8599", contour="#fff"))
    return S


def p11():
    S = Scene()
    ciel_haut(S)
    S.add(voyage(350, 480, 0.9, "fier", "inquiet"))
    S.add(pensee(560, 180, 140, depuis=(530, 380), contenu=g([texte(560, 170, "Oui, c'est moi,", 26, "#0c8599"), texte(560, 205, "la reine !", 30, "#0c8599")])))
    S.cachette(70, 620, "air")
    return S


def p12():
    S = Scene()
    ciel_haut(S)
    S.add(voyage(350, 400, 0.9, "bouche_bee", "surpris", bouche_ouverte=True))
    S.add(baton(230, 355, 560, 355, ep=11))
    S.add(texte(600, 560, "Oh !", 60, "#0c8599", contour="#fff"))
    S.cachette(70, 620, "air")
    return S


def p13():
    S = Scene()
    ciel_haut(S)
    S.add(place(tortue(0, 0, 1.4, expr="oups"), 400, 480, rot=150))
    S.add(mouvement(400, 250, 1.4, rot=90))
    S.add(canard(170, 190, 0.8, nage=False, ailes="haut", expr="surpris", **CANARD1))
    S.add(canard(620, 170, 0.8, nage=False, ailes="haut", expr="surpris", flip=True, **CANARD2))
    S.cachette(70, 620, "air")
    return S


def p14():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 620, "#8ce99a")
    S.add(meule_foin(400, 760, 1.6))
    S.add(place(tortue(0, 0, 1.0, expr="oups"), 400, 500, rot=180))
    rr = random.Random(2)
    for _ in range(10):
        a = rr.uniform(-math.pi, 0)
        S.add(trait(400 + math.cos(a) * 170, 500 + math.sin(a) * 110, 400 + math.cos(a) * 220, 500 + math.sin(a) * 150, "#f59f00", 6))
    S.add(texte(620, 250, "POUF !", 70, "#e67700", contour="#fff"))
    return S


def p15():
    S = Scene()
    etang_(S)
    S.add(meule_foin(700, 620, 0.6))
    S.add(tortue(250, 720, 1.4, expr="timide"))
    S.add(canard(510, 700, 1.0, expr="rire", flip=True, **CANARD1))
    S.add(canard(650, 730, 0.9, expr="content", flip=True, **CANARD2))
    S.add(bulle(420, 150, 460, 110, "Parfois, il vaut mieux\nse taire !", 34, pointe=(520, 540)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("baton-seul.svg", vignette),
    ("01-la-tortue.svg", p01), ("02-voir-le-monde.svg", p02), ("03-les-canards.svg", p03),
    ("04-emmenez-moi.svg", p04), ("05-le-baton.svg", p05), ("06-n-ouvre-pas.svg", p06),
    ("07-envol.svg", p07), ("08-vue-du-ciel.svg", p08), ("09-le-village.svg", p09),
    ("10-la-reine.svg", p10), ("11-si-fiere.svg", p11), ("12-la-bouche.svg", p12),
    ("13-elle-tombe.svg", p13), ("14-pouf.svg", p14), ("15-se-taire.svg", p15),
]
