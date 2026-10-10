"""La Chauve-souris et les deux Belettes — d'après La Fontaine.

Une chauve-souris étourdie tombe dans le nid d'une belette qui déteste les
oiseaux : « Moi, un oiseau ? Voyez mon poil : je suis une souris ! » La
belette la laisse partir. Deux jours plus tard, elle tombe chez une autre
belette, qui déteste les souris : « Moi, une souris ? Voyez mes ailes : je
suis un oiseau ! » Sauvée deux fois. Une dernière page rétablit la vérité :
la chauve-souris n'est ni un oiseau, ni une souris, c'est un mammifère qui
vole (du poil, un bébé qui boit le lait de sa mère, des ailes faites de
peau tendue entre de très longs doigts).

Plans : 1 large (la chute) · 2 moyen (la belette qui n'aime pas les
oiseaux) · 3 gros plan (je suis une souris !) · 4 moyen (va-t'en) · 5 large
(la deuxième chute) · 6 moyen (la belette qui n'aime pas les souris) · 7
gros plan (je suis un oiseau !) · 8 large (sauvée) · 9 schéma (le savais-tu ?).
"""
from fables import *
from base import _assombrir
from sciences import chauve_souris
from animaux import coupe_terre, etiquette

ID = "chauve-souris-belettes"

BRUN_CS = "#7c5c4a"
BELETTE_1 = dict(couleur="#9c6b3c", habit="#2f9e44", acc=("lunettes",))
BELETTE_2 = dict(couleur="#b07a4a", habit="#e8590c", acc=("noeud",))


def cs(x, y, s=1.0, ailes="ouvertes", **k):
    return chauve_souris(x, y, s, couleur=BRUN_CS, ailes=ailes, **k)


def belette(i, x, y, s=1.4, **k):
    return perso("renard", x, y, s, **{**(BELETTE_1, BELETTE_2)[i], **k})


def nid_belette(S, nuit_=True, graine=1):
    """Le nid de la belette, sous la terre, vu en coupe."""
    coupe_terre(S, 300, ciel_=False, graine=graine)
    if nuit_:
        S.add(rect(0, 0, 800, 300, lineaire([(0, "#1c2a52"), (1, "#4c5b9a")])))
        S._decor("nuit")
        etoiles(S, 20, graine=graine, zone=(0, 0, 800, 260))
    S.add(chemin("M 120 290 Q 170 360 260 430", stroke="#3d2817", sw=60))
    S.add(ellipse(440, 600, 330, 170, "#6d4424"), ellipse(440, 620, 310, 140, volume("#c9a27a", 0.2, 0.75)))
    S.add(ellipse(440, 720, 220, 30, "#e9c46a"))


def etoiles_tournent(x, y, s=1.0):
    return place([place(etoile5(0, 0, 10, OR), 30 * math.cos(math.radians(a)), 12 * math.sin(math.radians(a))) for a in (0, 120, 240)] +
                 [ellipse(0, 0, 36, 14, "none", stroke=OR, stroke_width=2)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nid_belette(S, graine=2)
    S.add(belette(0, 220, 740, 1.2, expr="malin", bras="designe"))
    S.add(belette(1, 660, 740, 1.2, expr="malin", bras="designe", flip=True))
    S.add(cs(440, 520, 1.3, expr="malin"))
    S.cachette(740, 270, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cs(200, 130, 0.9, expr="content"))
    return S


def p01():
    """Plan large : la nuit, une chauve-souris étourdie tombe tête la première dans le trou d'une belette."""
    S = Scene()
    nid_belette(S, graine=1)
    S.add(place(cs(0, 0, 0.9, expr="surpris"), 170, 220, rot=150))
    S.add(etoiles_tournent(170, 140, 1.2))
    S.add(chemin("M 100 80 Q 140 160 170 210", stroke="#adb5bd", sw=3, stroke_dasharray="8 8"))
    S.add(texte(500, 130, "Oups !", 70, "#fff", contour="#1c2a52"))
    return S


def p02():
    """Plan moyen : dans son nid, la première belette, qui déteste les oiseaux : « Un oiseau ! Je vais le croquer ! »"""
    S = Scene()
    nid_belette(S, graine=3)
    S.add(cs(300, 640, 0.9, expr="inquiet", ailes="ouvertes"))
    S.add(belette(0, 560, 740, 1.4, expr="malin", bras="tend", flip=True, regard=(-1, 0.3)))
    S.add(bulle(560, 150, 420, 110, "Un oiseau ! Moi qui déteste\nles oiseaux !", 30, pointe=(560, 330)))
    return S


def p03():
    """Gros plan : la chauve-souris replie ses ailes : « Moi, un oiseau ? Regardez mon poil : je suis une souris ! »"""
    S = Scene()
    nid_belette(S, graine=4)
    S.add(cs(380, 600, 1.9, expr="malin", ailes="repliees"))
    S.add(bulle(380, 140, 520, 130, "Moi, un oiseau ? Regardez mon poil :\nje suis une souris !\nVive les souris !", 28, pointe=(380, 330)))
    S.cachette(740, 270, "air")
    return S


def p04():
    """Plan moyen : la belette, perplexe, se gratte la tête… et la laisse partir : « Bon… file, la souris ! »"""
    S = Scene()
    nid_belette(S, graine=5)
    S.add(belette(0, 300, 740, 1.4, expr="concentre", bras="tete", regard=(1, -0.3)))
    S.add(cs(600, 200, 0.8, expr="rire", ailes="ouvertes"))
    S.add(bulle(330, 150, 320, 90, "Bon… file, la souris !", 30, pointe=(310, 340)))
    return S


def p05():
    """Plan large : deux jours plus tard, étourdie à nouveau, elle tombe chez une autre belette."""
    S = Scene()
    nid_belette(S, graine=6)
    S.add(place(cs(0, 0, 0.9, expr="surpris"), 170, 220, rot=160))
    S.add(etoiles_tournent(170, 140, 1.2))
    S.add(texte(500, 130, "Re-oups !", 64, "#fff", contour="#1c2a52"))
    S.add(belette(1, 560, 740, 1.2, expr="surpris", bras="joues", flip=True, regard=(-1, -0.5)))
    return S


def p06():
    """Plan moyen : la deuxième belette, qui déteste les souris : « Une souris ! Moi qui déteste les souris ! »"""
    S = Scene()
    nid_belette(S, graine=7)
    S.add(cs(300, 640, 0.9, expr="inquiet", ailes="repliees"))
    S.add(belette(1, 560, 740, 1.4, expr="malin", bras="tend", flip=True, regard=(-1, 0.3)))
    S.add(bulle(560, 150, 420, 110, "Une souris ! Moi qui déteste\nles souris !", 30, pointe=(560, 330)))
    return S


def p07():
    """Gros plan : la chauve-souris ouvre grand ses ailes : « Moi, une souris ? Regardez mes ailes : je suis un oiseau ! »"""
    S = Scene()
    nid_belette(S, graine=8)
    S.add(cs(400, 600, 2.0, expr="malin", ailes="ouvertes"))
    S.add(bulle(400, 140, 520, 130, "Moi, une souris ? Regardez mes ailes :\nje suis un oiseau !\nVive les oiseaux !", 28, pointe=(400, 330)))
    S.cachette(740, 270, "air")
    return S


def p08():
    """Plan large : la chauve-souris s'envole dans la nuit, sauvée pour la deuxième fois."""
    S = Scene()
    nuit(S, "#1c2a52", "#4c5b9a")
    S.add(lune(620, 160, 50))
    etoiles(S, 40, graine=8, zone=(0, 0, 800, 520))
    S.add(rect(0, 600, 800, 200, "#2b8a3e"))
    for k in range(6):
        S.add(arbre(60 + k * 140, 640, 0.8, "#1f4b33", "#24593b"))
    S.add(cs(380, 340, 1.2, expr="rire"))
    S.add(texte(400, 520, "Sauvée deux fois !", 52, "#fff3bf", contour="#1c2a52"))
    return S


def p09():
    """Schéma : le savais-tu ? la chauve-souris n'est ni un oiseau ni une souris : c'est un mammifère qui vole."""
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(texte(400, 80, "Le savais-tu ?", 50, "#5f3dc4"))
    S.add(cs(400, 400, 2.4, expr="content"))
    S.add(trait(250, 360, 130, 260, "#868e96", 3), etiquette(130, 220, "des doigts très longs", 26, "#5f3dc4"))
    S.add(trait(400, 440, 400, 600, "#868e96", 3), etiquette(400, 640, "du poil, comme une souris", 26, "#5f3dc4"))
    S.add(trait(560, 360, 670, 260, "#868e96", 3), etiquette(660, 220, "des ailes de peau", 26, "#5f3dc4"))
    S.add(texte(400, 720, "Ni oiseau, ni souris : un mammifère qui vole !", 30, "#495057"))
    S.cachette(740, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chauve-souris-seule.svg", vignette),
    ("01-oups.svg", p01), ("02-un-oiseau.svg", p02), ("03-une-souris.svg", p03),
    ("04-file.svg", p04), ("05-re-oups.svg", p05), ("06-une-souris-encore.svg", p06),
    ("07-un-oiseau.svg", p07), ("08-sauvee.svg", p08), ("09-le-savais-tu.svg", p09),
]
