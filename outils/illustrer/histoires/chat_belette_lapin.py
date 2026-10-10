"""Le Chat, la Belette et le Petit Lapin — d'après La Fontaine, en version douce.

Un matin, pendant que Jeannot Lapin va brouter le thym dans la rosée, Dame
Belette s'installe dans son terrier. Jeannot revient : « Sortez de chez
moi ! » « La terre est au premier occupant ! » Ils se disputent et vont
demander à Raminagrobis, un vieux chat qui a l'air si sage, de les
départager. « Approchez, mes enfants, je suis un peu sourd… » Chez La
Fontaine, le chat les croque tous les deux ; ici, il bondit, mais la
belette et le lapin sautent de côté et filent ensemble dans le terrier. Ils
décident de s'arranger entre voisins.

Plans : 1 large (le thym et la rosée) · 2 moyen (la belette s'installe) ·
3 moyen (sortez de chez moi !) · 4 moyen (la dispute) · 5 large
(Raminagrobis) · 6 moyen (approchez…) · 7 large (le bond) · 8 moyen
(voisins).
"""
from fables import *
from base import _assombrir

ID = "chat-belette-lapin"

LAPIN = dict(couleur="#c9a27a", habit="#4dabf7")
BELETTE = dict(couleur="#9c6b3c", habit="#e64980", acc=("noeud",))
CHAT = dict(couleur="#868e96", habit="#5f3dc4", acc=("lunettes",))


def jeannot(x, y, s=1.3, **k):
    return perso("lapin", x, y, s, **{**LAPIN, **k})


def belette(x, y, s=1.3, **k):
    return perso("renard", x, y, s, **{**BELETTE, **k})


def raminagrobis(x, y, s=1.7, **k):
    return perso("chat", x, y, s, **{**CHAT, **k})


def terrier(S, x=560, y=640, s=1.0):
    S.add(place([chemin("M -220 40 Q -160 -140 0 -150 Q 160 -140 220 40 Z", volume("#69db7c", 0.3, 0.8)),
                 ellipse(0, 0, 70, 56, "#4a2c17"), ellipse(0, 10, 60, 44, "#2b1d12")], x, y, s))


def thym(x, y, s=1.0):
    m = [trait(0, 0, -10, -40, "#5c940d", 3), trait(0, 0, 10, -44, "#5c940d", 3), trait(0, 0, 0, -50, "#5c940d", 3)]
    for px, py in ((-10, -40), (10, -44), (0, -50), (-6, -26), (6, -30)):
        m.append(cercle(px, py, 5, "#b197fc"))
    return place(m, x, y, s)


def pre_matin(S, aube=False):
    ciel(S, "#ffc9c9" if aube else "#74c0fc", "#fff4e6" if aube else "#e7f5ff")
    collines(S, 520, "#b2f2bb", graine=5)
    sol(S, 560, "#8ce99a")


def gouttes_rosee(S, graine=1):
    r = random.Random(graine)
    for k in range(30):
        S.add(cercle(r.uniform(0, 800), r.uniform(600, 790), 4, "#e7f5ff", opacity=0.9))


def coussin_chat(x, y, s=1.0):
    return place([ellipse(0, 0, 130, 30, volume("#c2255c", 0.3, 0.8)), ellipse(0, -10, 110, 20, "#e64980")], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    pre_matin(S)
    terrier(S, 400, 640, 1.2)
    S.add(raminagrobis(400, 520, 1.1, expr="malin", bras="hanches"))
    S.add(jeannot(160, 800, 1.4, expr="fache", bras="designe"), belette(650, 800, 1.4, expr="fache", bras="designe", flip=True))
    S.cachette(760, 700)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(jeannot(130, 262, 0.75, expr="content", bras="salut"), belette(280, 262, 0.75, expr="malin", bras="hanches", flip=True))
    return S


def p01():
    """Plan large : à l'aube, Jeannot Lapin quitte son terrier pour aller brouter le thym dans la rosée."""
    S = Scene()
    pre_matin(S, aube=True)
    terrier(S, 160, 650, 0.9)
    for x in (420, 520, 600, 700):
        S.add(thym(x, 760, 1.4))
    gouttes_rosee(S, 1)
    S.add(jeannot(500, 790, 1.35, expr="rire", bras="ouverts", regard=(1, 0.3), pas="saute"))
    S.add(texte(500, 130, "Le thym et la rosée", 48, "#c2255c", contour="#fff"))
    return S


def p02():
    """Plan moyen : pendant ce temps, Dame Belette se glisse dans le terrier vide et s'y installe."""
    S = Scene()
    pre_matin(S)
    terrier(S, 420, 680, 1.4)
    S.add(belette(420, 760, 1.0, expr="malin", bras="porte", regard=(0, 0),
                  objet=rect(-60, -110, 120, 70, volume("#a0693a", 0.3, 0.8), rx=10)))
    S.add(texte(400, 130, "Hop, c'est chez moi !", 50, "#e64980", contour="#fff"))
    return S


def p03():
    """Plan moyen : Jeannot revient et trouve la belette chez lui : « Holà ! Sortez de chez moi ! »"""
    S = Scene()
    pre_matin(S)
    terrier(S, 560, 660, 1.2)
    S.add(belette(560, 720, 0.95, expr="malin", bras="hanches", regard=(-1, 0)))
    S.add(jeannot(200, 800, 1.45, expr="furieux", bras="poing", regard=(1, 0)))
    S.add(bulle(260, 150, 380, 110, "Holà, Madame la Belette !\nSortez de chez moi !", 30, pointe=(220, 330)))
    return S


def p04():
    """Plan moyen : la belette et le lapin se disputent : « La terre est au premier qui la prend ! » « C'est la maison de mon grand-père ! »"""
    S = Scene()
    pre_matin(S)
    terrier(S, 400, 640, 0.9)
    S.add(belette(570, 800, 1.45, expr="fache", bras="designe", flip=True, regard=(-1, 0)))
    S.add(jeannot(230, 800, 1.45, expr="fache", bras="designe", regard=(1, 0)))
    S.add(bulle(560, 160, 380, 110, "La terre est à celui\nqui s'y installe !", 30, pointe=(560, 330)))
    S.add(bulle(230, 330, 380, 110, "C'est la maison\nde mon grand-père !", 30, pointe=(230, 430)))
    return S


def p05():
    """Plan large : ils vont voir Raminagrobis, un vieux chat gros et gras, qui a l'air si sage, assis sur son coussin."""
    S = Scene()
    pre_matin(S)
    S.add(arbre(400, 600, 1.6, "#51cf66", "#40c057"))
    S.add(coussin_chat(400, 770, 1.3))
    S.add(raminagrobis(400, 760, 1.6, expr="content", bras="mains_jointes", regard=(0, 0.3)))
    S.add(jeannot(140, 800, 1.2, expr="content", bras="designe", regard=(1, -0.3)), belette(670, 800, 1.2, expr="content", bras="designe",
                                                                                         flip=True, regard=(-1, -0.3)))
    S.add(texte(400, 110, "Raminagrobis, le sage", 48, "#5f3dc4", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


def p06():
    """Plan moyen : « Approchez, mes enfants, approchez… je suis un peu sourd. » Le lapin et la belette s'approchent."""
    S = Scene()
    pre_matin(S)
    S.add(coussin_chat(400, 790, 1.3))
    S.add(raminagrobis(400, 780, 1.75, expr="malin", bras="tend", regard=(0, 0.5)))
    S.add(jeannot(220, 800, 1.2, expr="inquiet", bras="bas", regard=(1, -0.5)), belette(590, 800, 1.2, expr="inquiet", bras="bas", flip=True,
                                                                                       regard=(-1, -0.5)))
    S.add(bulle(400, 140, 460, 110, "Approchez, mes enfants…\nje suis un peu sourd.", 32, pointe=(400, 300)))
    return S


def p07():
    """Plan large : le chat bondit ! mais la belette et le lapin sautent de côté et filent ensemble vers le terrier."""
    S = Scene()
    pre_matin(S)
    terrier(S, 640, 660, 1.0)
    S.add(coussin_chat(220, 790, 1.0))
    S.add(raminagrobis(330, 640, 1.4, expr="surpris", bras="haut", rot=-20))
    S.add(mouvement(420, 520, 1.6), mouvement(600, 700, 1.4))
    S.add(jeannot(560, 790, 1.0, expr="surpris", bras="court", pas="saute"), belette(680, 780, 1.0, expr="surpris", bras="court", pas="saute"))
    S.add(texte(400, 110, "Raté !", 70, "#c92a2a", contour="#fff"))
    return S


def p08():
    """Plan moyen : à l'abri du terrier, le lapin et la belette rient ; ils décident de s'arranger entre voisins."""
    S = Scene()
    pre_matin(S)
    terrier(S, 300, 650, 1.0)
    S.add(place([chemin("M -160 40 Q -110 -110 0 -120 Q 110 -110 160 40 Z", volume("#69db7c", 0.3, 0.8)), ellipse(0, 0, 54, 44, "#4a2c17")], 620, 660))
    S.add(jeannot(300, 800, 1.35, expr="rire", bras="main", regard=(1, 0)), belette(520, 800, 1.35, expr="rire", bras="main", flip=True, regard=(-1, 0)))
    S.add(bulle(400, 150, 460, 110, "Toi là, moi ici :\non sera voisins !", 32, pointe=(420, 330)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lapin-belette.svg", vignette),
    ("01-le-thym.svg", p01), ("02-la-belette.svg", p02), ("03-sortez.svg", p03),
    ("04-la-dispute.svg", p04), ("05-raminagrobis.svg", p05), ("06-approchez.svg", p06),
    ("07-rate.svg", p07), ("08-voisins.svg", p08),
]
