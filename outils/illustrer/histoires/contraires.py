"""Grand, petit ! — les contraires avec Panda et Noisette.

Panda est grand, Noisette l'écureuil est petite : à chaque page, un couple
de contraires (en haut / en bas, dedans / dehors, plein / vide, chaud /
froid, lent / rapide, mouillé / sec, propre / sale, ouvert / fermé, le
jour / la nuit). Tout le contraire l'un de l'autre… et meilleurs amis.

Plans : 1 moyen (grand, petit) · 2 large (en haut, en bas) · 3 gros plan
(dedans, dehors) · 4 moyen (plein, vide) · 5 gros plan (chaud, froid) ·
6 large (lent, rapide) · 7 moyen (mouillé, sec) · 8 gros plan (propre,
sale) · 9 moyen (ouvert, fermé) · 10 large (le jour, la nuit) · 11 large
(amis).
"""
from base import *
from base import _assombrir
from objets import parapluie, carton, bol, tasse, flaque

ID = "contraires"

NOISETTE = dict(acc=("noeud",), couleur_acc="#f783ac")
PANDA = dict(acc=("echarpe",), couleur_acc="#1098ad")
BLEU = "#1098ad"
ROSE_ = "#e64980"


def panda(x, y, s=2.0, **k):
    return perso("panda", x, y, s, **{**PANDA, **k})


def noisette(x, y, s=0.75, **k):
    return perso("ecureuil", x, y, s, **{**NOISETTE, **k})


def mot(x, y, contenu, couleur=BLEU, taille=52):
    """Étiquette d'un contraire, en grand."""
    return texte(x, y, contenu, taille, couleur, contour="#fff")


def jardin(S, horizon=560, graine=1, haut="#74c0fc", bas="#e7f5ff"):
    paysage(S, horizon, horizon + 60, "#8ce99a", "#b2f2bb", haut, bas, graine=graine, nuages=((640, 120, 0.6),))


def bambou(x, y, s=1.0, h=360):
    m = []
    for k in range(int(h / 60)):
        m.append(rect(-9, -(k + 1) * 60, 18, 56, cylindre("#82c91e", 0.25, 0.75), rx=6))
        m.append(rect(-11, -(k + 1) * 60 - 4, 22, 6, "#5c940d", rx=3))
    for k, (dy, sgn) in enumerate(((-120, 1), (-210, -1), (-300, 1))):
        if -dy < h:
            m.append(ellipse(sgn * 34, dy, 32, 9, "#74b816", rot=sgn * -25))
    return place(m, x, y, s)


def panier_noisettes(x, y, s=1.0, plein=True):
    m = [chemin("M -70 -70 Q -70 -140 0 -140 Q 70 -140 70 -70", stroke="#8d5524", sw=9)]
    if plein:
        r = random.Random(3)
        for k in range(12):
            nx, ny = -50 + (k % 6) * 20 + r.uniform(-4, 4), -76 - (k // 6) * 18 + r.uniform(-4, 4)
            m.append(ellipse(nx, ny, 13, 12, volume("#a0693a", 0.4, 0.75)))
            m.append(ellipse(nx, ny - 8, 10, 5, "#6d4424"))
    m += [chemin("M -74 -70 L 74 -70 L 58 0 L -58 0 Z", volume("#d9a066", 0.35, 0.8)),
          trait(-70, -48, 70, -48, "#a0522d", 4), trait(-64, -24, 64, -24, "#a0522d", 4)]
    return place(m, x, y, s)


def cornet(x, y, s=1.0):
    return place([poly([(-22, -10), (22, -10), (0, 60)], "#e8a33d"),
                  chemin("M -16 4 L 12 -6 M -12 18 L 10 10 M -6 32 L 6 26", stroke="#c47f17", sw=2),
                  cercle(0, -26, 24, volume("#ffc9e3", 0.4, 0.8)), cercle(-6, -50, 18, volume("#d3f9d8", 0.4, 0.8)),
                  cercle(-10, -34, 5, "#fff", opacity=0.6)], x, y, s)


def chocolat(x, y, s=1.0):
    return place([rect(-32, -64, 64, 64, volume("#e03131", 0.35, 0.8), rx=10),
                  chemin("M 32 -50 Q 56 -50 54 -30 Q 52 -12 32 -14", stroke="#c92a2a", sw=8),
                  ellipse(0, -64, 32, 8, "#6d4424"),
                  chemin("M -12 -80 q -10 -16 0 -30 q 10 -14 0 -28 M 10 -80 q -10 -16 0 -30 q 10 -14 0 -28", stroke="#adb5bd", sw=4, opacity=0.8)],
                 x, y, s)


def boue(x, y, s):
    """Taches de boue sur Panda (repère du personnage)."""
    m = []
    for px, py, r in ((-22, -40, 12), (18, -70, 10), (30, -30, 9), (-30, -96, 8), (-24, -170, 9), (26, -176, 7),
                      (10, -10, 10), (-40, -10, 9), (40, -150, 6), (-8, -128, 5)):
        m.append(ellipse(px, py, r * 1.3, r, "#8d5524", opacity=0.9))
    return place(m, x, y, s)


def arbre_haut(x, y, s=1.0):
    """Grand arbre avec une branche tout en haut."""
    return place([rect(-30, -560, 60, 560, cylindre("#8d5524", 0.25, 0.75), rx=14),
                  chemin("M 0 -480 Q 80 -500 160 -540", stroke="#8d5524", sw=22),
                  cercle(-20, -600, 130, volume("#51cf66", 0.28, 0.75)), cercle(-130, -520, 80, volume("#40c057", 0.28, 0.75)),
                  cercle(100, -620, 80, volume("#40c057", 0.28, 0.75))], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S, 560, graine=2)
    S.add(bambou(700, 700, 1.0, 420))
    S.add(panda(330, 780, 2.2, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(noisette(600, 780, 0.8, expr="rire", bras="saute", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(panda(150, 262, 1.0, expr="content", bras="salut"))
    S.add(noisette(300, 262, 0.45, expr="rire", bras="haut"))
    return S


def p01():
    """Plan moyen : grand, petit."""
    S = Scene()
    jardin(S, 540, graine=3)
    S.add(panda(290, 790, 2.4, expr="content", bras="hanches", regard=(1, 0.3)))
    S.add(noisette(620, 790, 0.75, expr="rire", bras="salut", regard=(-1, -0.5)))
    S.add(mot(160, 150, "grand", BLEU, 64), mot(620, 520, "petite", ROSE_, 44))
    return S


def p02():
    """Plan large : en haut, en bas."""
    S = Scene()
    jardin(S, 600, graine=4)
    S.add(arbre_haut(330, 760, 0.9))
    S.add(noisette(330 + 140 * 0.9, 760 - 530 * 0.9, 0.5, expr="rire", bras="coucou"))
    S.add(panda(530, 780, 1.3, expr="surpris", bras="bas", regard=(-1, -1)))
    S.add(mot(620, 200, "en haut", ROSE_), mot(660, 470, "en bas", BLEU))
    return S


def p03():
    """Gros plan : Noisette dedans, Panda dehors."""
    S = Scene()
    jardin(S, 520, graine=5)
    S.add(noisette(250, 720, 0.75, expr="malin", bras="coucou", regard=(1, -0.3)))
    S.add(carton(250, 790, 1.0, w=260, h=170))
    S.add(panda(570, 800, 1.7, expr="rire", bras="designe", flip=True, regard=(-1, 0)))
    S.camera(1.15, 400, 520)
    S.dessus(mot(230, 160, "dedans", ROSE_), mot(590, 160, "dehors", BLEU))
    return S


def p04():
    """Plan moyen : le panier de Noisette est plein, le bol de Panda est vide."""
    S = Scene()
    jardin(S, 520, graine=6)
    S.add(noisette(170, 790, 0.85, expr="fier", bras="montre", regard=(1, 0)))
    S.add(panier_noisettes(330, 790, 1.1, plein=True))
    S.add(panda(560, 790, 1.8, expr="triste", bras="donne", flip=True, regard=(-1, 0.3),
                objet=place(bol(0, 0, 0.8, "#74c0fc", contenu="#e7f5ff", cuillere=False), 96, -70)))
    S.add(mot(300, 450, "plein", ROSE_), mot(470, 300, "vide", BLEU))
    return S


def p05():
    """Gros plan : le chocolat chaud de Panda, la glace froide de Noisette."""
    S = Scene()
    jardin(S, 500, graine=7, haut="#a5d8ff")
    S.add(panda(270, 820, 2.0, expr="souffle", bras="donne", regard=(0.6, 0.3), objet=chocolat(92, -50, 0.9)))
    S.add(noisette(650, 790, 1.1, expr="miam", bras="donne", flip=True, regard=(-1, 0), objet=cornet(90, -112, 0.8)))
    S.dessus(mot(220, 150, "chaud", "#e03131"), mot(640, 270, "froid", "#1c7ed6"))
    return S


def p06():
    """Plan large : Panda marche lentement avec un escargot ; Noisette file à toute vitesse."""
    S = Scene()
    jardin(S, 560, graine=8)
    S.add(chemin("M 0 690 Q 400 640 800 690 L 800 760 Q 400 710 0 760 Z", "#e9c99a"))
    S.add(panda(200, 720, 1.25, expr="content", bras="marche", regard=(1, 0)))
    S.add(escargot(360, 720, 0.6, expr="content"))
    S.add(noisette(640, 710, 0.75, expr="rire", bras="court"))
    S.add(mouvement(540, 650, 1.0, ROSE_, rot=180))
    S.add(mot(260, 400, "lent", BLEU), mot(640, 460, "rapide", ROSE_))
    return S


def p07():
    """Plan moyen : sous la pluie, Panda est mouillé ; Noisette, sous son parapluie, est sèche."""
    S = Scene()
    jardin(S, 520, graine=9, haut="#868e96", bas="#ced4da")
    S.add(nuage(200, 110, 1.0, "#adb5bd"), nuage(580, 90, 0.9, "#adb5bd"))
    pluie(S, 80, 4)
    S.add(flaque(300, 780, 1.6))
    S.add(panda(290, 790, 1.8, expr="pleure", bras="bas", regard=(1, 0)))
    for k in range(5):
        S.add(goutte(220 + k * 36, 380 + (k % 2) * 30, 0.9, "#4dabf7"))
    S.add(noisette(610, 790, 0.85, expr="content", bras="tient", regard=(-1, 0), objet=parapluie(68, -160, 0.75, "#f783ac", ROSE_)))
    S.add(mot(170, 250, "mouillé", BLEU), mot(610, 560, "sèche", ROSE_, 44))
    return S


def p08():
    """Gros plan : Panda tout sale de boue, Noisette toute propre."""
    S = Scene()
    jardin(S, 500, graine=10)
    S.add(ellipse(300, 790, 240, 40, "#8d5524"))
    S.add(panda(300, 800, 2.1, expr="rire", bras="haut"))
    S.add(boue(300, 800, 2.1))
    S.add(noisette(610, 790, 1.1, expr="fier", bras="hanches", regard=(-1, 0)))
    S.add(paillettes(680, 520, 1.2, "#fcc419"))
    S.camera(1.1, 420, 470)
    S.dessus(mot(160, 140, "sale", "#8d5524"), mot(630, 300, "propre", ROSE_))
    S.cachette(720, 264, "air")
    return S


def p09():
    """Plan moyen : Panda a les yeux fermés, Noisette les yeux grands ouverts."""
    S = Scene()
    jardin(S, 520, graine=11, haut="#ffa94d", bas="#ffe8cc")
    S.add(panda(280, 790, 1.9, expr="dort", bras="bas"))
    S.add(zzz(420, 340, 1.0, "#5c7cfa"))
    S.add(noisette(600, 790, 1.0, expr="surpris", bras="joues", regard=(-1, 0)))
    S.add(mot(220, 180, "les yeux fermés", BLEU, 44), mot(600, 470, "ouverts", ROSE_, 44))
    return S


def p10():
    """Plan large : à gauche le jour, Noisette joue ; à droite la nuit, elle dort et Panda veille."""
    S = Scene()
    jardin(S, 560, graine=12)
    S.add(soleil(150, 120, 50))
    nuit_ = g([rect(400, 0, 400, 800, "#1c2a52", opacity=0.82)])
    S.add(noisette(200, 760, 0.85, expr="rire", bras="saute"))
    S.add(nuit_)
    S.add(lune(660, 120, 40))
    S.add(etoile5(520, 90, 9, "#fff3bf"), etoile5(740, 220, 7, "#fff3bf"), etoile5(470, 230, 6, "#fff3bf"))
    S.add(panda(560, 780, 1.4, expr="content", bras="calin", regard=(1, 0.5)))
    S.add(noisette(690, 780, 0.6, expr="dort", rot=-80, ombre=False))
    S.add(zzz(720, 640, 0.6, "#fff3bf"))
    S.add(trait(400, 0, 400, 800, "#fff", 4))
    S.add(mot(200, 330, "le jour", "#f08c00"), mot(600, 330, "la nuit", "#5c7cfa"))
    return S


def p11():
    """Plan large : au coucher du soleil, Panda et Noisette se font un câlin."""
    S = Scene()
    jardin(S, 560, graine=13, haut="#f783ac", bas="#ffe8cc")
    S.add(soleil(620, 540, 60))
    S.add(bambou(90, 700, 1.0, 420), bambou(740, 700, 0.9, 360))
    S.add(panda(380, 790, 2.0, expr="content", bras="calin", regard=(1, -0.3)))
    S.add(noisette(470, 790 - 60 * 2.0, 0.65, expr="rire", bras="calin", regard=(-1, 0.3), ombre=False))
    for x, y in ((250, 220), (560, 180), (420, 130)):
        S.add(coeur(x, y, 0.9, "#ff6b6b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("amis-seuls.svg", vignette),
    ("01-grand-petit.svg", p01), ("02-en-haut-en-bas.svg", p02), ("03-dedans-dehors.svg", p03),
    ("04-plein-vide.svg", p04), ("05-chaud-froid.svg", p05), ("06-lent-rapide.svg", p06),
    ("07-mouille-sec.svg", p07), ("08-propre-sale.svg", p08), ("09-ouvert-ferme.svg", p09),
    ("10-jour-nuit.svg", p10), ("11-amis.svg", p11),
]
