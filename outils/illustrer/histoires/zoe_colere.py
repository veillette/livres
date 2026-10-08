"""La grande colère de Zoé — nommer sa colère et se calmer.

Le petit frère de Zoé fait tomber sa tour. La colère monte (un orage
au-dessus de sa tête), éclate, puis Papa l'aide à la nommer et à la calmer :
respirer (sentir la fleur, souffler la bougie), compter, serrer un coussin.
L'orage rapetisse ; Zoé dit avec des mots ce qu'elle ressent, et la tour
est reconstruite à deux.
"""
from base import *
from objets import *
from fantastique import personne

ID = "zoe-colere"
ZOE = dict(peau="rosee", cheveux="blond", coiffure="queue", habit="#e03131", robe=False, jambes="#364fc7")
TIMOTHEE = dict(peau="rosee", cheveux="blond", coiffure="herisses", habit="#74c0fc", robe=False, jambes="#495057")
PAPA = dict(peau="rosee", cheveux="brun", coiffure="courts", habit="#2f9e44", robe=False, jambes="#343a40", barbe="#4a2c17")


def zoe(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**ZOE, **k})


def timothee(x=0, y=0, s=0.8, **k):
    return personne(x, y, s, **{**TIMOTHEE, **k})


def papa(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**PAPA, **k})


def orage(x, y, s=1.0, eclairs=True):
    """Le nuage de la colère, au-dessus de la tête de Zoé."""
    if eclairs:
        return nuage_orage(x, y, s)
    return nuage(x, y, s, "#868e96", ombre="#495057")


def salon(S):
    interieur(S, "#fff4e6", "#e8c39e", y=600, papier="#ffe8cc")
    S.add(fenetre(560, 100, 180, 170, "#a5d8ff", rideaux="#ffa8a8"))
    S.add(tapis(400, 700, 300, 60, "#d0ebff", "#74c0fc"))


def coussin(x, y, s=1.0):
    return place([rect(-60, -46, 120, 92, "#cc5de8", rx=30), cercle(0, 0, 8, "#9c36b5")], x, y, s)


def cubes_eparpilles(S, graine=1, zone=(140, 640, 660, 760)):
    r = random.Random(graine)
    couleurs = ("#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8", "#ff922b")
    for k in range(7):
        S.add(cube(r.uniform(zone[0], zone[2]), r.uniform(zone[1], zone[3]), 0.8, couleurs[k % 6], "ABCDEFG"[k], rot=r.uniform(-40, 40)))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#fff5f5")
    S.add(orage(400, 300, 2.0))
    S.add(zoe(400, 780, 1.8, expr="furieux", bras="poing"))
    S.cachette(130, 640, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(nuage(310, 70, 0.5, "#868e96", ombre="#495057"))
    S.add(zoe(180, 262, 1.0, expr="fache", bras="croises"))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(tour_cubes(470, 700, 0.85, 8, graine=2))
    S.add(zoe(260, 760, 1.3, expr="concentre", bras="tient", objet=cube(70, -150, 0.8, "#69db7c", "I")))
    S.add(texte(620, 380, "encore un !", 40, "#e03131", contour="#fff"))
    return S


def p02():
    S = Scene()
    salon(S)
    cubes_eparpilles(S, 3, (360, 560, 720, 760))
    S.add(timothee(560, 770, 0.85, expr="oups", bras="ouverts"))
    S.add(zoe(220, 760, 1.3, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(texte(520, 300, "BADABOUM !", 70, "#e8590c", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    fond(S, "#ffe3e3")
    S.add(orage(400, 170, 1.4))
    S.add(zoe(400, 780, 1.7, expr="fache", bras="poing", regard=(0, 1)))
    # la colère monte : joues chaudes, poings serrés
    for x, y in ((290, 520), (510, 520)):
        S.add(g([chemin(f"M {x + k * 14} {y} q 8 -12 0 -24 q -8 -12 0 -24", stroke="#fa5252", sw=4) for k in range(3)]))
    S.add(texte(150, 420, "grrr…", 50, "#c92a2a", contour="#fff", rot=-10))
    S.cachette(460, 70, "air")
    return S


def p04():
    S = Scene()
    salon(S)
    cubes_eparpilles(S, 5, (120, 600, 700, 770))
    S.add(orage(330, 140, 1.4))
    S.add(zoe(330, 780, 1.4, expr="furieux", bras="haut"))
    S.add(timothee(620, 780, 0.85, expr="pleure", larmes=True, flip=True))
    S.add(texte(560, 300, "NOOOON !", 76, "#c92a2a", contour="#fff", rot=6))
    S.add(mouvement(200, 700, 1.0, rot=-40), mouvement(460, 700, 1.0, rot=40))
    return S


def p05():
    S = Scene()
    salon(S)
    S.add(orage(250, 160, 1.1))
    S.add(zoe(250, 780, 1.35, expr="fache", bras="croises"))
    S.add(papa(540, 800, 1.35, expr="sourire", bras="ouverts", flip=True, regard=(-1, 1)))
    S.add(bulle(540, 330, 400, 90, "Tu es en colère.", 40, pointe=(530, 470)))
    return S


def p06():
    S = Scene()
    fond(S, "#e6fcf5")
    S.add(orage(400, 140, 0.9))
    S.add(zoe(260, 780, 1.4, expr="souffle", bras="tient", objet=fleur(70, -150, 1.0, "#f783ac", tige=40)))
    S.add(texte(260, 330, "Je sens la fleur…", 34, "#0ca678", contour="#fff"))
    S.add(zoe(580, 780, 1.4, expr="souffle", bras="tient", flip=True, objet=bougie(70, -130, 0.8)))
    S.add(texte(580, 330, "je souffle la bougie !", 34, "#0ca678", contour="#fff"))
    S.cachette(450, 70, "air")
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(orage(380, 140, 0.7, eclairs=False))
    S.add(zoe(380, 780, 1.45, expr="concentre", bras="calin", objet=coussin(0, -66, 0.75)))
    for k in range(10):
        a = math.radians(-160 + k * 15.5)
        S.add(texte(380 + math.cos(a) * 270, 520 + math.sin(a) * 200, str(k + 1), 40, "#7048e8", contour="#fff"))
    return S


def p08():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(soleil(470, 150, 50, visage=True))
    S.add(nuage(380, 190, 0.6, "#dee2e6", ombre="#ced4da"))
    S.add(zoe(400, 780, 1.6, expr="sourire", bras="bas"))
    S.add(texte(400, 380, "ouf…", 56, "#1971c2", contour="#fff"))
    S.cachette(380, 70, "air")
    return S


def p09():
    S = Scene()
    salon(S)
    S.add(zoe(260, 780, 1.35, expr="triste", bras="calin", regard=(1, 1)))
    S.add(timothee(470, 780, 0.85, expr="timide", bras="calin", flip=True, regard=(-1, 0)))
    S.add(papa(660, 800, 1.35, expr="content", flip=True, regard=(-1, 1)))
    S.add(bulle(260, 170, 420, 110, "Je suis fâchée :\nma tour est tombée !", 32, pointe=(260, 430)))
    S.add(bulle(560, 340, 200, 70, "Pardon…", 32, pointe=(480, 560)))
    return S


def p10():
    S = Scene()
    salon(S)
    S.add(tour_cubes(400, 720, 0.75, 9, graine=4))
    S.add(zoe(230, 770, 1.3, expr="rire", bras="tient", objet=cube(70, -150, 0.8, "#ffd43b", "J")))
    S.add(timothee(590, 770, 0.85, expr="rire", bras="haut"))
    S.add(texte(400, 100, "Encore plus grande !", 44, "#e03131", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("zoe-seule.svg", vignette),
    ("01-la-tour.svg", p01), ("02-badaboum.svg", p02), ("03-ca-gronde.svg", p03),
    ("04-l-orage-eclate.svg", p04), ("05-tu-es-en-colere.svg", p05), ("06-respirer.svg", p06),
    ("07-compter.svg", p07), ("08-ouf.svg", p08), ("09-avec-des-mots.svg", p09),
    ("10-a-deux.svg", p10),
]
