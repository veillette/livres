"""Les Fées — d'après le conte de Charles Perrault.

Adaptation douce : pas de sœur chassée ni de prince. Rose aide Fanchon à
retourner à la fontaine ; quand Fanchon demande pardon, ses mots redeviennent
des fleurs.
"""
from contes import *

ID = "les-fees"
ROSE_ = dict(peau="doree", cheveux="brun", coiffure="tresses", habit="#f783ac")
FANCHON = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#7048e8")
MAMAN = dict(peau="doree", cheveux="brun", coiffure="chignon", habit="#2f9e44")
VIEILLE = dict(peau="rosee", cheveux="blanc", coiffure="chignon", habit="#868e96", cape="#5c3a1e")
DAME = dict(peau="rosee", cheveux="blond", coiffure="tres_longs", habit="#cc5de8", acc=("diademe",), cape="#9775fa")


def rose(x, y, s=1.0, **k):
    return personne(x, y, s, **{**ROSE_, **k})


def fanchon(x, y, s=1.05, **k):
    return personne(x, y, s, **{**FANCHON, **k})


def maman(x, y, s=1.2, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def vieille(x, y, s=1.1, **k):
    return personne(x, y, s, **{**VIEILLE, **k})


def dame(x, y, s=1.25, **k):
    return personne(x, y, s, **{**DAME, **k})


def cruche(x, y, s=1.0, rot=0, couleur="#e8590c"):
    m = [chemin("M -40 0 Q -60 -60 -30 -100 L -20 -130 L 20 -130 L 30 -100 Q 60 -60 40 0 Z", couleur),
         rect(-26, -140, 52, 14, assombrir(couleur, 0.85), rx=5),
         chemin("M 34 -100 Q 76 -90 44 -40", stroke=assombrir(couleur, 0.85), sw=10),
         chemin("M -30 -60 Q 0 -50 30 -60", stroke="#fff", sw=4, opacity=0.5)]
    return place(m, x, y, s, rot=rot)


def diamant(x, y, s=1.0):
    return place([poly([(-14, 0), (0, -16), (14, 0), (0, 20)], "#a5d8ff", stroke="#4dabf7", stroke_width=2),
                  poly([(-14, 0), (0, -16), (0, 20)], "#d0ebff")], x, y, s)


def crapaud(x, y, s=0.35, **k):
    k.setdefault("expr", "surpris")
    return perso("grenouille", x, y, s, couleur="#8f9a4a", visage="#d8dca0", **k)


def couleuvre(x, y, s=1.0, flip=False):
    m = [chemin("M -60 0 Q -40 -26 -20 0 Q 0 26 20 0 Q 40 -26 56 -6", stroke="#82c91e", sw=14),
         cercle(60, -8, 12, "#82c91e"), cercle(64, -12, 3, ENCRE), chemin("M 72 -6 l 10 2 l -4 4", stroke="#e03131", sw=2)]
    return place(m, x, y, s, flip=flip)


def jaillit(x, y, objets, s=1.0):
    """Objets qui s'échappent de la bouche en (x, y) et retombent de chaque côté."""
    m = []
    for k, o in enumerate(objets):
        cote = -1 if k % 2 == 0 else 1
        rang = k // 2
        m.append(place(o, x + cote * (100 + 40 * rang) * s, y + (5 + 60 * rang) * s, s))
    return g(m)


def fleurs_perles(n=4):
    choix = [fleur(0, 0, 0.8, "#ff6b6b", tige=0), perle(0, 0, 0.8), diamant(0, 0, 1.2), fleur(0, 0, 0.8, "#f783ac", tige=0)]
    return [choix[k % 4] for k in range(n)]


def chaumiere(S):
    interieur(S, "#fff4e6", "#a0693a", 600, papier="#ffe8cc")
    S.add(fenetre(570, 100, 160, 150, "#a5d8ff", rideaux="#ffd43b"))
    S.add(etagere(170, 170, 220, objets=g([tasse(120, 170, 1.0, "#4dabf7"), tasse(180, 170, 1.0, "#ff8787")])))


def bois(S, graine=1, soir=False):
    if soir:
        ciel(S, "#ffa94d", "#fff3bf")
    else:
        ciel(S, "#a5d8ff", "#ebfbee")
    collines(S, 560, "#8ce99a", graine=graine)
    sol(S, 600, "#69db7c")
    S.add(arbre(80, 620, 1.3, "#2f9e44", "#2b8a3e"), arbre(730, 620, 1.2, "#40c057", "#2f9e44"))
    S.add(fleur(160, 700, 0.8, "#ffd43b"), fleur(640, 720, 0.8, "#cc5de8"))


def scene_fontaine(S, graine=1):
    bois(S, graine)
    S.add(fontaine(400, 640, 1.2))


def couverture():
    S = Scene()
    bois(S, 2)
    S.add(fontaine(560, 640, 1.0))
    S.add(rose(320, 780, 1.6, expr="rire", bras="ouverts"))
    S.add(jaillit(320, 780 - 118 * 1.6, fleurs_perles(5), 1.2))
    S.add(etincelles(560, 330, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rose(200, 264, 1.0, expr="content", bras="porte", objet=cruche(0, -40, 0.55)))
    return S


def p01():
    S = Scene()
    chaumiere(S)
    S.add(fanchon(230, 780, 1.3, expr="fache", bras="croises"))
    S.add(rose(560, 780, 1.2, expr="sourire", bras="porte", objet=balai(0, -20, 0.8, rot=10)))
    return S


def p02():
    S = Scene()
    bois(S, 2)
    S.add(chemin("M 0 760 Q 300 640 500 620 T 800 600", stroke="#e9c38c", sw=50))
    S.add(fontaine(660, 600, 0.6))
    S.add(rose(300, 780, 1.3, expr="content", bras="porte", objet=cruche(0, -40, 0.9)))
    return S


def p03():
    S = Scene()
    scene_fontaine(S, 3)
    S.add(vieille(620, 780, 1.25, expr="sourire", bras="donne", regard=(-1, 0)))
    S.add(rose(200, 780, 1.2, expr="surpris", bras="porte", objet=cruche(0, -40, 0.8)))
    return S


def p04():
    S = Scene()
    scene_fontaine(S, 4)
    S.add(vieille(620, 780, 1.25, expr="content", bras="bas", regard=(-1, 0)))
    S.add(rose(310, 780, 1.2, expr="sourire", bras="donne", regard=(1, 0)))
    S.add(cruche(470, 640, 0.8, rot=-55))
    return S


def p05():
    S = Scene()
    scene_fontaine(S, 5)
    S.add(cercle(580, 450, 240, "#fff3bf", opacity=0.5))
    S.add(dame(580, 790, 1.3, expr="content", bras="tient", objet=baguette(70, -150, 1.0), ailes="#e5dbff"))
    S.add(etincelles(600, 300, 1.4, nb=12))
    S.add(rose(220, 780, 1.15, expr="bouche_bee", bras="joues"))
    return S


def p06():
    S = Scene()
    chaumiere(S)
    S.add(maman(600, 780, 1.3, expr="bouche_bee", bras="joues"))
    S.add(rose(260, 780, 1.25, expr="joie", bras="bas"))
    S.add(jaillit(260, 780 - 118 * 1.25, fleurs_perles(5), 1.1))
    return S


def p07():
    S = Scene()
    chaumiere(S)
    S.add(maman(220, 780, 1.25, expr="joie", bras="montre", regard=(1, 0)))
    S.add(fanchon(560, 780, 1.25, expr="furieux", bras="hanches"))
    S.add(cruche(700, 780, 0.8))
    S.add(texte(560, 330, "Jamais !", 64, "#7048e8", contour="#fff", rot=6))
    return S


def p08():
    S = Scene()
    scene_fontaine(S, 8)
    S.add(dame(620, 790, 1.3, expr="sourire", bras="donne", regard=(-1, 0)))
    S.add(fanchon(200, 780, 1.2, expr="neutre", bras="porte", objet=cruche(0, -40, 0.8)))
    return S


def p09():
    S = Scene()
    scene_fontaine(S, 9)
    S.add(dame(620, 790, 1.3, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(fanchon(220, 780, 1.25, expr="furieux", bras="croises", regard=(1, 0)))
    S.add(bulle(260, 200, 380, 90, "Buvez toute seule !", 38, pointe=(240, 480)))
    return S


def p10():
    S = Scene()
    scene_fontaine(S, 10)
    S.add(dame(600, 790, 1.3, expr="neutre", bras="tient", objet=baguette(70, -150, 1.0), ailes="#e5dbff"))
    S.add(etincelles(640, 300, 1.2, couleur="#b2f2bb"))
    S.add(fanchon(230, 780, 1.25, expr="surpris", bras="bouche"))
    return S


def p11():
    S = Scene()
    chaumiere(S)
    S.add(table(400, 790, 300, 120, "#a0693a"))
    S.add(maman(620, 780, 1.25, expr="surpris", bras="tete"))
    S.add(fanchon(220, 780, 1.25, expr="oups", bras="ouverts"))
    S.add(crapaud(200, 700, 0.45, bras="haut"), crapaud(330, 760, 0.4))
    S.add(couleuvre(440, 760, 1.0))
    S.add(texte(400, 250, "Oh là là !", 64, "#7048e8", contour="#fff"))
    return S


def p12():
    S = Scene()
    chaumiere(S)
    S.add(fanchon(330, 780, 1.25, expr="pleure", bras="yeux", larmes=True))
    S.add(rose(500, 780, 1.15, expr="sourire", bras="calin", regard=(-1, 0)))
    S.add(coeur(420, 300, 0.9, "#ff8787"))
    return S


def p13():
    S = Scene()
    bois(S, 13, soir=True)
    S.add(fontaine(400, 640, 1.2))
    S.add(dame(660, 790, 1.2, expr="content", bras="bas", regard=(-1, 0)))
    S.add(fanchon(330, 780, 1.2, expr="timide", bras="donne", regard=(1, 0)))
    S.add(cruche(480, 650, 0.7, rot=-55))
    S.add(rose(110, 780, 1.0, expr="rire", bras="haut"))
    S.add(jaillit(330, 780 - 118 * 1.2, [fleur(0, 0, 0.8, "#fff", tige=0), fleur(0, 0, 0.7, "#fff", tige=0)], 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("rose-seule.svg", vignette),
    ("01-deux-soeurs.svg", p01), ("02-la-cruche.svg", p02), ("03-la-vieille-femme.svg", p03), ("04-bien-sur.svg", p04),
    ("05-la-fee.svg", p05), ("06-des-roses.svg", p06), ("07-jamais.svg", p07), ("08-la-dame.svg", p08),
    ("09-buvez-toute-seule.svg", p09), ("10-le-sort.svg", p10), ("11-des-crapauds.svg", p11), ("12-les-mots-doux.svg", p12),
    ("13-pardon.svg", p13),
]
