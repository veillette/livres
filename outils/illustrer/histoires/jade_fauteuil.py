"""Mon amie Jade roule vite — une amitié avec une enfant en fauteuil roulant.

Jade arrive dans la classe de Théo, en fauteuil roulant. Théo pose sa
question (« Pourquoi tu as des roues ? ») et Jade répond simplement : ses
jambes ne marchent pas, son fauteuil marche pour elle. Elle roule vite, fait
des paniers, des équilibres sur deux roues, adore dessiner les chats… comme
Théo. Il apprend à demander avant d'aider, cherche avec elle la rampe quand
il y a un escalier, choisit pour sa fête un parc aux chemins plats, va
l'encourager au basket en fauteuil. Jade n'est pas « la fille en
fauteuil » : c'est Jade, son amie.

Plans : 1 moyen (voici Jade) · 2 moyen (pourquoi tu as des roues ?) · 3
large (la course) · 4 moyen (la rampe) · 5 moyen (demande-moi d'abord) · 6
moyen (panier !) · 7 moyen (on dessine) · 8 gros plan (l'équilibre) · 9
large (la fête au parc) · 10 large (le basket en fauteuil) · 11 moyen (mon
amie).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne
from objets import ballon_jeu

ID = "jade-fauteuil"

THEO = dict(peau="rosee", cheveux="blond", coiffure="herisses", habit="#4dabf7", robe=False, jambes="#495057")
JADE = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#f06595", robe=False, jambes="#364fc7", acc=("noeud",))
MAITRESSE = dict(stature="adulte", peau="doree", cheveux="brun", coiffure="queue", habit="#ffd43b", robe=True, acc=("lunettes",), yeux="cils")
AMIS = [dict(peau="claire", cheveux="chatain", coiffure="couettes", habit="#69db7c", robe=True),
        dict(peau="brune", cheveux="noir", coiffure="courts", habit="#ff922b", robe=False, jambes="#495057"),
        dict(peau="doree", cheveux="noir", coiffure="carre", habit="#b197fc", robe=False, jambes="#364fc7")]
ROSE = "#f06595"


def theo(x, y, s=1.6, **k):
    return personne(x, y, s, **{**THEO, **k})


def fauteuil_face(couleur="#495057", accent=ROSE):
    """Fauteuil roulant vu de face, en deux morceaux (derrière, devant) ; repère : (0, 0) = au sol au milieu."""
    roue = lambda sgn: g([ellipse(sgn * 74, -52, 14, 52, "#343a40"), ellipse(sgn * 74, -52, 8, 44, "none", stroke="#adb5bd", stroke_width=3),
                          ellipse(sgn * 85, -52, 5, 43, "none", stroke=accent, stroke_width=4)])
    derriere = [roue(-1), roue(1), rect(-56, -186, 112, 124, volume(couleur, 0.3, 0.8), rx=14),
                rect(-62, -198, 14, 30, "#343a40", rx=5), rect(48, -198, 14, 30, "#343a40", rx=5)]
    devant = [rect(-60, -76, 120, 26, volume(accent, 0.3, 0.8), rx=10),
              trait(-56, -54, -44, -20, couleur, 6), trait(56, -54, 44, -20, couleur, 6),
              rect(-52, -24, 104, 9, "#343a40", rx=4), cercle(-44, -8, 8, "#343a40"), cercle(44, -8, 8, "#343a40")]
    return derriere, devant


def assis_fauteuil(x, y, s, qui, couleur="#495057", accent=ROSE, rot=0, **k):
    """Un enfant assis dans un fauteuil roulant (vu de face) ; (x, y) = au sol."""
    derriere, devant = fauteuil_face(couleur, accent)
    corps = personne(0, 0, 1.0, **{**qui, "expr": k.pop("expr", "content"), "bras": k.pop("bras", "bas"),
                                   "regard": k.pop("regard", (0, 0)), **k})
    cid = uid("j")
    haut = el("clipPath", rect(-200, -420, 400, 330, "#000"), id=cid) + g(corps, clip_path=f"url(#{cid})")
    jambes = qui.get("jambes", "#495057")
    m = derriere + [place(haut, 0, 28)]
    m += devant[:1]
    m += [rect(-30, -60, 24, 36, cylindre(jambes, 0.3, 0.7), rx=10), rect(6, -60, 24, 36, cylindre(jambes, 0.3, 0.7), rx=10),
          ellipse(-18, -26, 18, 9, "#fff", stroke="#ced4da", stroke_width=2), ellipse(18, -26, 18, 9, "#fff", stroke="#ced4da", stroke_width=2)]
    m += devant[1:]
    return place(m, x, y, s, rot=rot) + occuper(x - 100 * s, y - 300 * s, x + 100 * s, y)


def jade(x, y, s=1.6, rot=0, **k):
    return assis_fauteuil(x, y, s, JADE, rot=rot, **k)


def ecole(S, accueil=True):
    interieur(S, "#e6fcf5", "#d9b48f", y=590, papier="#c3fae8")
    S.add(rect(200, 90, 400, 220, "#2b8a3e", rx=8), rect(190, 80, 420, 240, "none", stroke="#c68642", stroke_width=12, rx=10))
    if accueil:
        S.add(texte(400, 180, "Bienvenue", 40, "#fff", police="Andika, sans-serif"), texte(400, 240, "Jade !", 40, "#ffd43b"))
    else:
        S.add(cercle(300, 200, 40, "none", stroke="#fff", stroke_width=4), poly([(270, 174), (276, 140), (292, 166)], "none", stroke="#fff", stroke_width=4),
              poly([(308, 166), (324, 140), (330, 174)], "none", stroke="#fff", stroke_width=4), cercle(500, 190, 34, "none", stroke="#ffd43b", stroke_width=4))


def cour(S, horizon=470):
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, horizon - 160, 800, 160, "#ffe8cc"), rect(0, horizon - 180, 800, 24, "#e8590c"))
    for k in range(5):
        S.add(fenetre(40 + k * 160, horizon - 140, 100, 90, "#a5d8ff"))
    S.add(rect(0, horizon, 800, 800 - horizon, "#ced4da"))
    for x in range(0, 800, 100):
        S.add(trait(x, horizon, x - 60, 800, "#dee2e6", 3))


def table_dessin(x, y, w=320):
    return g([rect(x - w / 2, y - 140, w, 20, "#c68642", rx=6), rect(x - w / 2 + 14, y - 120, 14, 120, "#a0693a"),
              rect(x + w / 2 - 28, y - 120, 14, 120, "#a0693a")])


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cour(S, 500)
    S.add(mouvement(200, 620, 1.6))
    S.add(theo(560, 800, 1.65, expr="rire", bras="court", regard=(-1, 0), pas="marche"))
    S.add(jade(320, 800, 1.65, expr="rire", bras="haut", regard=(1, -0.3)))
    S.cachette(760, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(jade(200, 262, 0.75, expr="rire", bras="salut", regard=(0.5, 0)))
    return S


def p01():
    """Plan moyen : en classe, la maîtresse présente Jade, la nouvelle, dans son fauteuil roulant."""
    S = Scene()
    ecole(S)
    S.add(personne(650, 800, 1.85, expr="content", bras="designe", flip=True, regard=(-1, 0.3), **MAITRESSE))
    S.add(jade(410, 800, 1.6, expr="timide", bras="salut", regard=(-0.5, 0)))
    S.add(theo(140, 810, 1.5, expr="bouche_bee", bras="bas", regard=(1, -0.3)))
    S.cachette(150, 70, "air")
    return S


def p02():
    """Plan moyen : à la récré, Théo demande : « Pourquoi tu as des roues ? » ; Jade répond en souriant."""
    S = Scene()
    cour(S)
    S.add(theo(230, 800, 1.6, expr="neutre", bras="pense", regard=(1, 0)))
    S.add(jade(560, 800, 1.6, expr="content", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(230, 140, 360, 90, "Pourquoi tu as des roues ?", 30, pointe=(230, 330)))
    S.add(bulle(540, 300, 420, 130, "Mes jambes ne marchent pas.\nAlors mon fauteuil\nmarche pour moi !", 28, pointe=(560, 400)))
    return S


def p03():
    """Plan large : dans la cour, Jade file sur son fauteuil ; Théo court derrière elle : « Je roule vite ! »"""
    S = Scene()
    cour(S)
    S.add(theo(220, 800, 1.5, expr="rire", bras="court", regard=(1, 0), pas="marche"))
    S.add(mouvement(470, 620, 1.6))
    S.add(jade(580, 800, 1.6, expr="rire", bras="haut", regard=(-0.5, 0)))
    S.add(texte(400, 140, "Je roule vite !", 60, ROSE, contour="#fff"))
    return S


def p04():
    """Plan moyen : devant l'escalier de la bibliothèque, Théo montre la rampe ; Jade la monte."""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 200, 800, 380, "#ffe8cc"), rect(300, 300, 160, 280, "#b5835a"), texte(380, 270, "BIBLIOTHÈQUE", 28, "#c92a2a"))
    S.add(rect(0, 580, 800, 220, "#ced4da"))
    for k in range(4):
        S.add(rect(260, 690 - k * 30, 220, 30, "#adb5bd", stroke="#868e96", stroke_width=2))
    S.add(poly([(480, 580), (800, 700), (800, 800), (480, 800)], "#dee2e6"), trait(480, 560, 800, 680, "#868e96", 6))
    S.add(theo(160, 800, 1.55, expr="content", bras="designe", regard=(1, 0)))
    S.add(jade(640, 642, 1.35, rot=14, expr="rire", bras="bas", regard=(-0.5, 0)))
    S.add(bulle(220, 160, 320, 90, "Par ici, la rampe !", 32, pointe=(200, 320)))
    return S


def p05():
    """Plan moyen : Théo veut pousser le fauteuil sans demander ; Jade lève la main : « Demande-moi d'abord ! »"""
    S = Scene()
    cour(S)
    S.add(theo(470, 760, 1.55, expr="oups", bras="porte", regard=(-0.5, 0.4)))
    S.add(jade(380, 800, 1.6, expr="fache", bras="salut", regard=(1, -0.3)))
    S.add(bulle(240, 150, 340, 90, "Demande-moi d'abord !", 30, pointe=(330, 290)))
    S.add(bulle(620, 270, 300, 90, "Oh, pardon !\nJe peux t'aider ?", 28, pointe=(540, 360)))
    return S


def p06():
    """Plan moyen : dans la cour, Jade lance le ballon dans le panier de basket : « Panier ! »"""
    S = Scene()
    cour(S)
    S.add(rect(640, 180, 16, 620, "#868e96"), rect(560, 150, 170, 110, "#fff", stroke="#e03131", stroke_width=6, rx=6),
          ellipse(620, 270, 50, 10, "none", stroke="#e8590c", stroke_width=6))
    for k in range(5):
        S.add(trait(574 + k * 22, 272, 584 + k * 18, 330, "#fff", 2))
    S.add(ballon_jeu(612, 230, 28, "#e8590c", "#212529"))
    S.add(chemin("M 380 430 Q 480 160 600 220", stroke="#868e96", sw=3, stroke_dasharray="8 8"))
    S.add(jade(340, 800, 1.6, expr="joie", bras="victoire", regard=(1, -1)))
    S.add(theo(130, 800, 1.45, expr="rire", bras="applaudit", regard=(1, -0.3)))
    S.add(texte(330, 140, "Panier !", 64, "#e8590c", contour="#fff"))
    return S


def p07():
    """Plan moyen : à la même table, Jade et Théo dessinent des chats : « Toi aussi, tu aimes les chats ? »"""
    S = Scene()
    ecole(S, accueil=False)
    S.add(jade(260, 800, 1.5, expr="rire", bras="porte", regard=(1, 0.2)))
    S.add(theo(560, 800, 1.5, expr="joie", bras="porte", flip=True, regard=(-1, 0.2)))
    S.add(table_dessin(410, 800, 520))
    for x, c in ((300, "#ffa94d"), (520, "#adb5bd")):
        S.add(rect(x - 60, 630, 120, 40, "#fff", rx=4), cercle(x, 646, 12, c), poly([(x - 10, 638), (x - 6, 628), (x - 2, 638)], c),
              poly([(x + 2, 638), (x + 6, 628), (x + 10, 638)], c))
    S.add(bulle(400, 150, 470, 90, "Toi aussi, tu aimes les chats ?", 30, pointe=(480, 330)))
    return S


def p08():
    """Gros plan : Jade se met en équilibre sur ses deux grandes roues : « Regarde ! » ; Théo n'en revient pas."""
    S = Scene()
    cour(S)
    S.add(jade(380, 830, 1.9, rot=-18, expr="rire", bras="ouverts", regard=(1, -0.3)))
    S.add(theo(650, 860, 1.7, expr="bouche_bee", bras="joues", flip=True, regard=(-1, -0.3)))
    S.camera(1.1, 420, 520)
    S.dessus(texte(380, 110, "Regarde !", 64, ROSE, contour="#fff"))
    S.dessus(mouvement(170, 520, 1.4, rot=-30))
    S.cachette(720, 264, "air")
    return S


def p09():
    """Plan large : au parc, pour l'anniversaire de Théo, des ballons, des amis, et des chemins tout plats."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 460, "#b2f2bb", graine=9)
    S.add(rect(0, 540, 800, 260, terrain("#8ce99a")))
    S.add(chemin("M 0 800 Q 300 620 800 640 L 800 720 Q 320 700 120 800 Z", "#e9c46a"))
    S.add(arbre(90, 560, 1.0), arbre(720, 560, 0.9))
    for k, c in enumerate(("#ff6b6b", "#ffd43b", "#4dabf7", "#cc5de8")):
        S.add(chemin(f"M 620 560 Q {600 + k * 20} 460 {560 + k * 40} {300 + (k % 2) * 30}", stroke="#868e96", sw=2),
              ellipse(560 + k * 40, 280 + (k % 2) * 30, 26, 32, volume(c, 0.35, 0.8)))
    S.add(personne(660, 780, 1.35, expr="rire", bras="haut", flip=True, **AMIS[1]))
    S.add(jade(430, 790, 1.5, expr="rire", bras="haut", regard=(-0.5, -0.3)))
    S.add(theo(220, 800, 1.55, expr="joie", bras="ouverts", regard=(1, 0)))
    S.add(texte(330, 150, "Joyeux anniversaire, Théo !", 40, "#e8590c", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


def p10():
    """Plan large : au club de basket en fauteuil, Jade dribble ; Théo l'encourage depuis les gradins : « Allez, Jade ! »"""
    S = Scene()
    fond(S, "#fff4e6")
    S.add(rect(0, 520, 800, 280, "#e9b872"), trait(0, 640, 800, 640, "#fff", 4), ellipse(400, 640, 120, 30, "none", stroke="#fff", stroke_width=4))
    S.add(rect(0, 300, 800, 220, "#ced4da"))
    for k in range(3):
        S.add(rect(0, 330 + k * 60, 800, 14, "#adb5bd"))
    S.add(theo(120, 500, 0.9, expr="rire", bras="victoire", regard=(1, 0)), personne(220, 500, 0.85, expr="rire", bras="applaudit", **AMIS[0]))
    S.add(rect(700, 200, 14, 400, "#868e96"), rect(640, 180, 120, 80, "#fff", stroke="#e03131", stroke_width=5),
          ellipse(690, 268, 36, 8, "none", stroke="#e8590c", stroke_width=5))
    S.add(assis_fauteuil(560, 790, 1.25, AMIS[2], "#364fc7", "#4dabf7", expr="rire", bras="haut", regard=(-1, 0)))
    S.add(jade(300, 800, 1.35, expr="concentre", bras="donne", regard=(1, 0.3)))
    (_, _), (mx, my) = mains_personne(300, 800, 1.35, "donne")
    S.add(ballon_jeu(mx + 26, my + 40, 24, "#e8590c", "#212529"))
    S.add(bulle(260, 180, 260, 80, "Allez, Jade !", 34, pointe=(150, 330)))
    return S


def p11():
    """Plan moyen : Théo et Jade côte à côte, qui rient : « C'est Jade. Mon amie. »"""
    S = Scene()
    cour(S)
    S.add(coeur(400, 260, 3.0, "#ffdeeb"))
    S.add(jade(300, 800, 1.7, expr="rire", bras="epaule", regard=(1, 0)))
    S.add(theo(520, 800, 1.65, expr="rire", bras="epaule", flip=True, regard=(-1, 0)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("jade-seule.svg", vignette),
    ("01-voici-jade.svg", p01), ("02-pourquoi.svg", p02), ("03-je-roule-vite.svg", p03),
    ("04-la-rampe.svg", p04), ("05-demande-moi.svg", p05), ("06-panier.svg", p06),
    ("07-les-chats.svg", p07), ("08-regarde.svg", p08), ("09-la-fete.svg", p09),
    ("10-le-basket.svg", p10), ("11-mon-amie.svg", p11),
]
