"""La course des chevaux — un poulain du Kentucky qui préfère marcher.

Caramel naît dans une ferme de chevaux de course du « pays de l'herbe
bleue ». Tout le monde l'imagine champion, mais il aime marcher, sentir
le trèfle et regarder. Son calme rassure la pouliche Fusée ; le jour de
la grande course, il devient cheval d'accompagnement : il marche à côté
d'elle jusqu'au départ. Chacun son talent.
"""
from base import *
from objets import *
from fables import cheval_profil
from fantastique import personne

ID = "poulain-course"
CARAMEL = dict(couleur="#d08c4a", criniere="#f3d9b1")
ETOILE = dict(couleur="#7c4a1e", criniere="#2b2b3a")
FUSEE = dict(couleur="#495057", criniere="#212529")
JO = dict(peau="brune", cheveux="noir", coiffure="queue", habit="#2f9e44", robe=False, jambes="#1c7ed6")


def caramel(x, y, s=0.75, **k):
    return cheval_profil(x, y, s, **{**CARAMEL, **k})


def etoile(x, y, s=1.0, **k):
    return cheval_profil(x, y, s, **{**ETOILE, **k})


def fusee(x, y, s=0.95, **k):
    return cheval_profil(x, y, s, **{**FUSEE, **k})


def jo(x=0, y=0, s=1.3, **k):
    return personne(x, y, s, **{**JO, **k})


def jockey(casaque="#e03131", casque="#ffd43b"):
    """Cavalier assis sur le dos (coordonnées du cheval, dos vers (0, -150))."""
    coiffe = g([chemin("M -54 -160 Q -56 -214 0 -214 Q 56 -214 54 -160 Z", casque), rect(-56, -166, 112, 12, _fonce(casque), rx=6)])
    return personne(20, -112, 0.55, peau="claire", cheveux="brun", coiffure="courts", habit=casaque, robe=False,
                    jambes="#ffffff", chaussures="#343a40", expr="content", bras="porte", coiffe=coiffe)


def _fonce(c):
    return "#" + "".join("%02x" % int(int(c[i:i + 2], 16) * 0.8) for i in (1, 3, 5))


def cloture(S, y, couleur="#343a40", x0=0, x1=800, h=110):
    for x in range(x0 + 20, x1, 140):
        S.add(rect(x - 8, y - h, 16, h, couleur, rx=3))
    for dy in (h - 16, h * 0.55):
        S.add(rect(x0, y - dy, x1 - x0, 14, couleur, rx=3))


def pre_bleu(S, haut="#74c0fc", bas="#e7f5ff", y=520, graine=1, cloture_=True):
    """Le pré du Kentucky : collines douces, herbe verte aux reflets bleutés, clôture noire."""
    ciel(S, haut, bas)
    collines(S, y, "#a9e34b", graine=graine)
    S.add(rect(0, y, 800, 800 - y, "#69db7c"))
    r = random.Random(graine)
    for _ in range(40):
        S.add(cercle(r.uniform(0, 800), r.uniform(y + 20, 800), r.uniform(3, 6), "#91a7ff", opacity=0.55))
    if cloture_:
        cloture(S, y + 30)


def trefle(x, y, s=1.0):
    return place([trait(0, 0, 0, -30, "#2f9e44", 3), cercle(-7, -34, 7, "#40c057"), cercle(7, -34, 7, "#40c057"), cercle(0, -44, 7, "#40c057"),
                  cercle(0, -60, 9, "#f783ac")], x, y, s)


def tribune(S, y=380):
    S.add(rect(0, y - 220, 800, 220, "#e9ecef"))
    S.add(poly([(0, y - 220), (800, y - 220), (800, y - 260), (0, y - 260)], "#c92a2a"))
    for k in range(0, 800, 160):
        S.add(rect(k + 70, y - 260, 16, 260, "#adb5bd"))
    r = random.Random(7)
    couleurs = ("#fa5252", "#4dabf7", "#ffd43b", "#cc5de8", "#69db7c", "#ff922b", "#f783ac")
    for rang in range(4):
        for k in range(26):
            x = 16 + k * 31 + (rang % 2) * 14
            yy = y - 30 - rang * 46
            S.add(cercle(x, yy, 12, r.choice(("#f3c3a0", "#dca36f", "#a86a3f", "#fbd9bd"))))
            S.add(ellipse(x, yy - 12, 17, 5, r.choice(couleurs)), cercle(x, yy - 16, 8, r.choice(couleurs)))
    for k in range(6):
        S.add(poly([(60 + k * 140, y - 260), (60 + k * 140, y - 310), (100 + k * 140, y - 296)], ("#fa5252", "#4dabf7", "#ffd43b")[k % 3]))
        S.add(trait(60 + k * 140, y - 260, 60 + k * 140, y - 312, "#495057", 3))


def piste(S, y=520):
    S.add(rect(0, y, 800, 800 - y, "#c99a6e"))
    S.add(rect(0, y - 6, 800, 10, "#ffffff"))
    for k in range(0, 800, 60):
        S.add(rect(k, y - 40, 8, 40, "#ffffff"))
    S.add(rect(0, y - 46, 800, 8, "#ffffff"))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    pre_bleu(S, "#74c0fc", "#e7f5ff", 520, 2)
    S.add(papillon(560, 420, 1.2))
    S.add(caramel(330, 760, 1.25, expr="content", regard=(1, -1)))
    for x in (180, 600, 690):
        S.add(trefle(x, 780, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(caramel(150, 262, 0.85, expr="content"))
    return S


def p01():
    S = Scene()
    pre_bleu(S, "#a5d8ff", "#fff0f6", 500, 1)
    S.add(soleil(680, 110, 45))
    S.add(etoile(300, 720, 1.25, expr="content", regard=(1, 1)))
    S.add(caramel(560, 740, 0.75, expr="surpris", regard=(-1, 0), flip=True, rot=4))
    S.add(texte(560, 380, "Bonjour, Caramel !", 40, "#2f9e44", contour="#fff"))
    return S


def p02():
    S = Scene()
    pre_bleu(S, "#74c0fc", "#e7f5ff", 500, 3)
    S.add(maison(680, 500, 1.2, "#ffffff", "#c92a2a", "#343a40"))
    S.add(etoile(250, 740, 1.15, expr="fier"))
    S.add(caramel(560, 750, 0.7, expr="sourire", flip=True, regard=(-1, 0)))
    S.add(jo(700, 790, 1.2, expr="rire", bras="victoire", flip=True))
    S.add(bulle(420, 160, 420, 80, "Un futur champion !", 38, pointe=(640, 430)))
    S.add(g([etoile5(150 + k * 60, 330, 14, "#fab005") for k in range(3)]))
    return S


def p03():
    S = Scene()
    pre_bleu(S, "#74c0fc", "#e7f5ff", 480, 4)
    for x, c in ((140, "#212529"), (360, "#a0522d")):
        S.add(cheval_profil(x, 590, 0.55, couleur=c, criniere="#212529", expr="rire", rot=-8))
        S.add(mouvement(x - 110, 520, 0.8))
    S.add(texte(600, 400, "Tagada !", 50, "#495057", contour="#fff", rot=-6))
    S.add(caramel(380, 780, 0.8, expr="content", regard=(1, 1)))
    for x in (640, 700, 600):
        S.add(trefle(x, 770 - (x % 3) * 6, 1.3))
    S.add(papillon(650, 600, 1.0))
    return S


def p04():
    S = Scene()
    pre_bleu(S, "#74c0fc", "#e7f5ff", 500, 5)
    S.add(jo(170, 790, 1.35, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(caramel(480, 760, 0.85, expr="oups", rot=10))
    S.add(texte(250, 330, "Plus vite, Caramel !", 42, "#2f9e44", contour="#fff"))
    S.add(eclat(620, 760, 1.0, "#ffd43b"))
    return S


def p05():
    S = Scene()
    pre_bleu(S, "#495057", "#868e96", 500, 6)
    S.add(nuage_orage(560, 120, 1.3), nuage(220, 110, 1.4, "#868e96", ombre="#495057"))
    pluie(S, 40, 4, zone=(0, 160, 800, 520), couleur="#a5d8ff")
    S.add(fusee(250, 760, 0.95, expr="inquiet", regard=(1, -1), rot=-6))
    S.add(caramel(560, 760, 0.85, expr="sourire", flip=True, regard=(-1, 0)))
    S.add(texte(250, 380, "Hiii !", 56, "#ffffff", contour="#495057"))
    return S


def p06():
    S = Scene()
    pre_bleu(S, "#ffa94d", "#fff4e6", 500, 7)
    S.add(fusee(240, 760, 0.95, expr="content", regard=(1, 0)))
    S.add(caramel(520, 760, 0.85, expr="content", flip=True, regard=(-1, 0)))
    S.add(jo(700, 790, 1.25, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(bulle(560, 200, 420, 110, "Toi, tu rassures\nles autres !", 34, pointe=(680, 470)))
    return S


def p07():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    tribune(S, 440)
    piste(S, 560)
    S.add(texte(400, 80, "Le grand jour !", 60, "#c92a2a", contour="#fff"))
    S.add(notes(140, 120, 0.9, "#7048e8"), notes(680, 120, 0.9, "#7048e8"))
    return S


def p08():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    tribune(S, 360)
    piste(S, 480)
    S.add(fusee(250, 740, 0.9, expr="inquiet", regard=(1, 0), charge=jockey("#e03131", "#ffd43b")))
    S.add(caramel(560, 750, 0.85, expr="sourire", flip=True, regard=(-1, 0), charge=jockey("#2f9e44", "#ffffff")))
    S.add(texte(420, 470, "pas à pas…", 40, "#2f9e44", contour="#fff"))
    return S


def p09():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    tribune(S, 330)
    piste(S, 440)
    for x, c, cas, dy in ((560, FUSEE["couleur"], "#e03131", 0), (300, "#a0522d", "#1c7ed6", 40), (90, "#212529", "#fab005", 10)):
        S.add(cheval_profil(x, 700 + dy, 0.75, couleur=c, criniere="#212529", expr="rire", rot=-6, charge=jockey(cas, "#ffd43b")))
        S.add(mouvement(x - 140, 620 + dy, 0.9))
    S.add(texte(560, 400, "Tagada, tagada !", 44, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    tribune(S, 360)
    piste(S, 480)
    S.add(fusee(220, 750, 0.9, expr="rire", regard=(1, 0)))
    S.add(g([cercle(295, 610, 30, "#ff6b6b"), cercle(295, 610, 18, "#ffd43b"), poly([(280, 636), (270, 680), (290, 664)], "#ff6b6b"),
             poly([(310, 636), (320, 680), (300, 664)], "#ff6b6b")]))
    S.add(caramel(610, 750, 0.85, expr="rire", flip=True, regard=(-1, 0)))
    S.add(coeur(440, 420, 1.2, "#ff6b6b"))
    return S


def p11():
    S = Scene()
    pre_bleu(S, "#f76707", "#ffd8a8", 500, 8)
    S.add(cercle(640, 470, 70, "#ffd43b", opacity=0.8))
    S.add(caramel(420, 760, 0.95, expr="content", regard=(1, 1)))
    S.add(cheval_profil(640, 770, 0.45, couleur="#212529", criniere="#868e96", expr="content", regard=(-1, 0), flip=True))
    S.add(cheval_profil(170, 770, 0.45, couleur="#f8f9fa", criniere="#adb5bd", expr="rire"))
    for x in (300, 520):
        S.add(trefle(x, 790, 1.2))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("caramel-seul.svg", vignette),
    ("01-bonjour-caramel.svg", p01), ("02-un-champion.svg", p02), ("03-tagada.svg", p03),
    ("04-plus-vite.svg", p04), ("05-l-orage.svg", p05), ("06-un-talent.svg", p06),
    ("07-le-grand-jour.svg", p07), ("08-pas-a-pas.svg", p08), ("09-la-course.svg", p09),
    ("10-retrouvailles.svg", p10), ("11-chacun-son-talent.svg", p11),
]
