"""Le Héron — ne pas faire le difficile."""
from fables import *

ID = "heron"

BLEU = "#3b5bdb"
CARPE, BROCHET, TANCHE, GOUJON = "#e8a15c", "#82c91e", "#94d82d", "#adb5bd"


def bord_de_riviere(S, moment="matin", graine=111):
    hauts = {"matin": ("#a5d8ff", "#fff9db"), "midi": ("#74c0fc", "#e7f5ff"), "soir": ("#ff922b", "#ffd8a8"),
             "nuit": ("#1c2a52", "#4c5b9a")}
    ciel(S, *hauts[moment])
    if moment == "matin":
        S.add(soleil(150, 150, 44))
    elif moment == "midi":
        S.add(soleil(400, 110, 50))
    elif moment == "soir":
        S.add(soleil(680, 520, 56, "#ffa94d"))
    else:
        S.add(lune(660, 120, 38))
        etoiles(S, 14, 112, zone=(0, 0, 800, 360))
    collines(S, 540, "#b2f2bb" if moment != "nuit" else "#364fc7", graine=graine)
    sol(S, 560, "#8ce99a" if moment != "nuit" else "#2f9e44")
    eau_c = {"nuit": "#1864ab", "soir": "#4dabf7"}.get(moment, "#74c0fc")
    S.add(rect(0, 610, 800, 190, eau_c, opacity=0.9))
    for k in range(6):
        S.add(chemin(f"M {40 + k * 130 + (k % 2) * 30} {640 + (k % 3) * 50} q 25 -10 50 0", stroke="#d0ebff", sw=4))
    for k in range(5):
        S.add(roseau(770 - k * 22, 620 + k * 4, 0.42, penche=-8 + k * 4, visage_=False))


def poissons_(S, liste):
    for (x, y, c, sc, flip) in liste:
        S.add(poisson_riviere(x, y, sc, c, flip=flip))


def couverture():
    S = Scene()
    bord_de_riviere(S)
    S.add(heron(300, 720, 1.3, expr="fier", regard=(1, 0)))
    poissons_(S, [(560, 720, CARPE, 0.8, False), (690, 760, GOUJON, 0.5, True)])
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 138, 192, 132, "#e7f5ff"))
    S.add(heron(150, 262, 0.62, expr="fier"))
    return S


def p01():
    S = Scene()
    bord_de_riviere(S)
    S.add(heron(330, 640, 1.2, expr="sourire", regard=(1, 0)))
    S.add(texte(560, 450, "Un pas… deux pas…", 44, BLEU, contour="#fff"))
    return S


def p02():
    S = Scene()
    bord_de_riviere(S, graine=112)
    S.add(heron(160, 650, 1.0, expr="content", cou="baisse", regard=(1, 1)))
    poissons_(S, [(420, 680, CARPE, 0.9, False), (600, 740, BROCHET, 0.9, True), (480, 770, GOUJON, 0.5, False)])
    S.add(bulles_eau(540, 680, 0.8))
    return S


def p03():
    S = Scene()
    bord_de_riviere(S)
    S.add(heron(250, 700, 1.05, expr="fier", regard=(1, -1)))
    poissons_(S, [(470, 700, CARPE, 0.9, False)])
    S.add(bulle(500, 160, 520, 130, "Je n'ai pas encore faim.\nJ'attendrai un peu.", 36, pointe=(360, 320)))
    return S


def p04():
    S = Scene()
    bord_de_riviere(S, "midi", graine=113)
    S.add(heron(230, 700, 1.05, expr="degoute", regard=(1, 1)))
    poissons_(S, [(470, 700, TANCHE, 0.7, False), (600, 750, TANCHE, 0.6, True)])
    S.add(bulle(520, 160, 520, 130, "Des tanches ? Ce n'est pas\nun repas de héron !", 34, pointe=(350, 320)))
    return S


def p05():
    S = Scene()
    bord_de_riviere(S, "midi", graine=114)
    S.add(heron(230, 700, 1.05, expr="fache", regard=(1, 1)))
    poissons_(S, [(470, 700, GOUJON, 0.4, False), (540, 730, GOUJON, 0.35, True), (600, 690, GOUJON, 0.4, False)])
    S.add(bulle(520, 160, 520, 130, "Des goujons ? Fi donc !\nOuvrir le bec pour si peu ?", 32, pointe=(350, 320)))
    return S


def p06():
    S = Scene()
    bord_de_riviere(S, "midi", graine=115)
    S.add(heron(230, 700, 1.2, expr="surpris", cou="baisse", regard=(1, 1)))
    poissons_(S, [(520, 760, CARPE, 0.6, False), (640, 780, TANCHE, 0.5, False), (720, 770, GOUJON, 0.4, False)])
    S.add(fleche(460, 700, 640, 760, "#1864ab", sw=5))
    S.add(texte(560, 320, "Bye bye !", 46, BLEU, contour="#fff"))
    return S


def p07():
    S = Scene()
    bord_de_riviere(S, "midi", graine=116)
    S.add(heron(380, 700, 1.25, expr="inquiet", regard=(0, 1)))
    S.add(texte(620, 430, "Grrrr…", 44, BLEU, contour="#fff"))
    S.add(texte(620, 470, "(son ventre)", 26, BLEU, contour="#fff"))
    return S


def p08():
    S = Scene()
    bord_de_riviere(S, "soir", graine=117)
    S.add(heron(400, 700, 1.2, expr="triste", cou="baisse", regard=(1, 1)))
    S.add(texte(250, 270, "Rien… rien…", 46, BLEU, contour="#fff"))
    return S


def p09():
    S = Scene()
    bord_de_riviere(S, "soir", graine=118)
    S.add(caillou(560, 620, 2.0, "#868e96"))
    S.add(escargot(560, 552, 0.55, expr="surpris", flip=True, regard=(-1, 0)))
    S.add(heron(250, 700, 1.15, expr="surpris", cou="baisse", regard=(1, 0)))
    S.add(texte(560, 270, "Un escargot ?", 46, BLEU, contour="#fff"))
    return S


def p10():
    S = Scene()
    bord_de_riviere(S, "soir", graine=118)
    S.add(caillou(560, 620, 2.0, "#868e96"))
    S.add(escargot(560, 552, 0.55, expr="sourire", flip=True, regard=(-1, 0)))
    S.add(heron(250, 700, 1.15, expr="triste", regard=(1, 1)))
    S.add(bulle(560, 220, 420, 120, "Bonsoir ! Moi, je suis\nbien petit…", 34, pointe=(540, 470)))
    return S


def p11():
    S = Scene()
    bord_de_riviere(S, "nuit", graine=118)
    S.add(caillou(560, 620, 2.0, "#868e96"))
    S.add(escargot(600, 552, 0.55, expr="content", regard=(1, 0)))
    S.add(heron(250, 700, 1.15, expr="rire", regard=(1, 1)))
    S.add(bulle(420, 150, 600, 130, "J'ai fait le difficile…\nme voilà bien attrapé !", 34, pointe=(330, 300)))
    return S


def p12():
    S = Scene()
    bord_de_riviere(S, "matin", graine=119)
    S.add(heron(250, 700, 1.2, expr="content", objet=poisson_riviere(10, 0, 0.5, CARPE, rot=10)))
    S.add(texte(600, 460, "Hop !", 56, BLEU, contour="#fff"))
    return S


def p13():
    S = Scene()
    bord_de_riviere(S, "matin", graine=119)
    S.add(caillou(560, 620, 2.0, "#868e96"))
    S.add(escargot(560, 552, 0.55, expr="rire", flip=True, regard=(-1, 0)))
    S.add(heron(250, 700, 1.2, expr="rire", regard=(1, 0)))
    S.add(texte(560, 440, "Délicieux !", 54, BLEU, contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("heron-seul.svg", vignette),
    ("01-le-heron.svg", p01), ("02-l-eau-claire.svg", p02), ("03-pas-encore-faim.svg", p03),
    ("04-des-tanches.svg", p04), ("05-des-goujons.svg", p05), ("06-les-poissons-s-en-vont.svg", p06),
    ("07-le-ventre-vide.svg", p07), ("08-rien.svg", p08), ("09-un-escargot.svg", p09),
    ("10-bonsoir.svg", p10), ("11-bien-attrape.svg", p11), ("12-hop.svg", p12),
    ("13-delicieux.svg", p13),
]
