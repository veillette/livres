"""Mange, mon manteau ! — d'après une histoire de Nasreddine Hodja (Turquie).

Nasreddine Hodja est invité à un grand festin. Il arrive tout droit de son
jardin, dans ses vieux habits de travail : personne ne le regarde,
personne ne le sert. Il rentre chez lui, enfile son plus beau manteau
brodé et revient. Cette fois, on l'accueille avec de grands sourires, on
l'installe à la place d'honneur et on lui sert les meilleurs plats. Alors
Nasreddine trempe la manche de son manteau dans la soupe : « Mange, mon
manteau, mange ! » Tout le monde le regarde, étonné. « C'est bien mon
manteau que vous avez invité, puisque sans lui on ne m'a rien servi ! »
L'hôte, honteux, comprend : on ne juge pas les gens à leurs habits.

Plans : 1 large (au jardin) · 2 large (le festin) · 3 moyen (oublié) · 4
moyen (sur son âne) · 5 gros plan (le beau manteau) · 6 large (le retour)
· 7 moyen (les meilleurs plats) · 8 gros plan (« Mange, mon manteau ! »)
· 9 moyen (la leçon).
"""
from contes import *
from base import _assombrir
from dragons import coussins
from fetes import lanterne

ID = "mange-mon-manteau"
PAPIER_PEINT = "losanges"


def turban(c="#f8f9fa", bijou=None):
    """Grand turban enroulé (coiffe)."""
    m = [ellipse(0, -206, 74, 40, volume(c, 0.35, 0.82)), chemin("M -72 -204 Q 0 -244 72 -204 M -66 -190 Q 0 -226 66 -190", stroke=_assombrir(c, 0.82), sw=3)]
    if bijou:
        m += [cercle(0, -222, 9, bijou), trait(0, -232, 0, -262, "#ffffff", 4)]
    return g(m)


def fez(c="#c92a2a"):
    return g([poly([(-40, -186), (-32, -236), (32, -236), (40, -186)], volume(c, 0.3, 0.8)), trait(0, -236, 24, -200, "#212529", 3),
              cercle(24, -198, 5, "#212529")])


def broderies(c="#fab005"):
    """Galons dorés du beau manteau (tenue)."""
    return g([trait(0, -100, 0, -10, c, 5), chemin("M -40 -90 l 10 10 l 10 -10 l 10 10 l 10 -10 l 10 10 l 10 -10 l 10 10 l 10 -10", stroke=c, sw=3),
              cercle(-8, -70, 4, c), cercle(-8, -50, 4, c), cercle(-8, -30, 4, c)])


def rapieces():
    """Pièces cousues sur les vieux habits (tenue)."""
    return g([rect(-34, -80, 22, 20, "#868e96", rx=3), rect(14, -44, 20, 18, "#5c7cfa", rx=3, opacity=0.8),
              chemin("M -34 -80 h 22 v 20 h -22 z", stroke=ENCRE, sw=1.5, stroke_dasharray="3 3", opacity=0.5)])


NASREDDINE = dict(stature="adulte", peau="doree", cheveux="blanc", coiffure="chauve_cote", robe=True, barbe="#f1f3f5", nez="long",
                  carrure="ronde")
HABITS_TRAVAIL = dict(habit="#a07c58", tenue=rapieces(), coiffe=turban("#e9d8c4"), ceinture="#6d4c32")
BEAU_MANTEAU = dict(habit="#862e9c", tenue=broderies(), coiffe=turban("#ffffff", "#e03131"), ceinture="#fab005", cape="#5f3dc4")
HOTE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chauve_cote", habit="#1864ab", robe=True, carrure="ronde",
            barbe="#343a40", nez="rond", ceinture="#fab005", coiffe=fez())
INVITES = [dict(stature="adulte", peau="claire", cheveux="chatain", coiffure="chignon", habit="#e64980", robe=True, yeux="cils"),
           dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#2b8a3e", robe=True, nez="pointu", coiffe=fez("#a61e4d")),
           dict(stature="ancien", peau="doree", cheveux="gris", coiffure="chignon", habit="#f08c00", robe=True, carrure="ronde")]
VOISIN = dict(stature="ado", peau="doree", cheveux="noir", coiffure="courts", habit="#f76707", robe=False, jambes="#495057")


def plateau(x, y, s=1.0, plats=("soupe", "pilaf", "baklava")):
    """Grand plateau de cuivre sur un petit pied, garni de plats ; (x, y) = sol."""
    m = [rect(-30, -50, 60, 50, "#8d5524"), ellipse(0, -54, 220, 36, volume("#e8590c", 0.3, 0.8)), ellipse(0, -58, 200, 28, "#f08c00"),
         ellipse(0, -58, 170, 20, "none", stroke="#ffd8a8", stroke_width=2)]
    pos = {"soupe": -120, "pilaf": 0, "baklava": 120}
    for p in plats:
        px = pos[p]
        if p == "soupe":
            m.append(bol(px, -50, 0.55, "#1971c2", "#fd7e14", cuillere=False))
            m.append(g([chemin(f"M {px - 10} -100 q -8 -16 0 -30 M {px + 10} -100 q 8 -16 0 -30", stroke="#fff", sw=3, opacity=0.6)]))
        elif p == "pilaf":
            m += [ellipse(px, -62, 60, 12, "#f8f9fa"), chemin(f"M {px - 50} -64 Q {px} -130 {px + 50} -64 Z", volume("#fff3bf", 0.3, 0.85))]
            for k in range(5):
                m.append(cercle(px - 24 + k * 12, -84 - (k % 2) * 10, 3, "#e8590c"))
        else:
            m.append(ellipse(px, -62, 56, 12, "#f8f9fa"))
            for k in range(3):
                m.append(poly([(px - 36 + k * 24, -66), (px - 24 + k * 24, -84), (px - 12 + k * 24, -66), (px - 24 + k * 24, -60)], volume("#e9b872", 0.3, 0.8)))
    return place(m, x, y, s)


def salle_festin(S, nuit_=True):
    """La salle du festin : boiseries, tapis rouge, lanternes de cuivre."""
    piece(S, "manoir", 560)
    if nuit_:
        S.ambiance("interieur")
    S.add(tapis(400, 690, 380, 80, "#c92a2a", "#fab005"))
    for x in (140, 400, 660):
        S.add(trait(x, 0, x, 70, "#495057", 2), lanterne(x, 70, 1.0, couleur="#b08900"))
        S.lumiere(x, 122, 90, "#ffd43b", 0.55)


def jardin(S, soir=False):
    ciel(S, "#ff922b" if soir else "#74c0fc", "#fff4e6")
    collines(S, 500, "#c0eb75", graine=4)
    sol(S, 600, "#a9e34b")
    S.add(maison(640, 610, 0.65, mur="#fff3bf", toit="#c92a2a", lumiere=soir, volets="#1864ab"))


def manche_dans_bol(x, y, s, by, flip=False):
    """La manche du beau manteau qui pend de la main tendue (x, y = personne) jusque dans un bol de soupe posé en by."""
    hx, hy = mains_personne(x, y, s, "tend", flip=flip, stature="adulte", carrure="ronde")[0 if flip else 1]
    hx -= 36 * s      # le corps penché ramène la main
    return (chemin(f"M {n(hx - 14 * s)} {n(hy)} Q {n(hx - 24 * s)} {n((hy + by) / 2)} {n(hx - 8 * s)} {n(by - 22 * s)} L {n(hx + 30 * s)} {n(by - 22 * s)} "
                   f"Q {n(hx + 30 * s)} {n((hy + by) / 2)} {n(hx + 16 * s)} {n(hy)} Z", "#5f3dc4")
            + trait(hx - 8 * s, by - 22 * s, hx + 30 * s, by - 22 * s, "#fab005", 5 * s)
            + bol(hx + 10 * s, by, 0.5 * s, "#1971c2", "#fd7e14", cuillere=False))


def assis(x, y, s, **k):
    """Personne assise en tailleur sur un coussin (raccourcie)."""
    return ellipse(x, y - 6 * s, 70 * s, 22 * s, volume("#9775fa", 0.3, 0.75)) + personne(x, y, s, sy=0.78, **k)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salle_festin(S)
    S.add(plateau(330, 800, 1.1, plats=("pilaf", "baklava")))
    S.add(personne(330, 660, 1.35, expr="malin", bras="tend", regard=(1, 0.6), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(manche_dans_bol(330, 660, 1.35, 742))
    S.cachette(40, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ane_profil(200, 250, 0.55, expr="content"))
    S.add(personne(190, 250 - 70 * 0.55, 0.42, expr="content", bras="bas", sy=0.8, **{**NASREDDINE, **HABITS_TRAVAIL}))
    return S


def p01():
    """Plan large : au jardin, Nasreddine bêche, dans ses vieux habits rapiécés ; un garçon accourt : « Grand festin ce soir chez Ali ! Tu es invité ! »"""
    S = Scene()
    jardin(S)
    S.add(personne(300, 780, 1.3, expr="content", bras="ramasse", objet=beche(36, -18, 0.9, rot=-10), regard=(1, 0), **{**NASREDDINE, **HABITS_TRAVAIL}))
    S.add(personne(560, 790, 1.05, expr="joie", bras="court", flip=True, regard=(-1, 0), **VOISIN))
    for k in range(4):
        S.add(chou(110 + k * 60, 760, 0.5))
    S.add(bulle(420, 150, 520, 110, "Grand festin ce soir chez Ali !\nTu es invité !", 30, pointe=(540, 480)))
    S.cachette(740, 790)
    return S


def p02():
    """Plan large : Nasreddine arrive au festin, tout droit du jardin, dans ses vieux habits ; les invités, bien habillés, le regardent de travers."""
    S = Scene()
    salle_festin(S)
    S.add(porte(80, 560, 140, 300, ouverte=True))
    S.add(personne(160, 790, 1.15, expr="sourire", bras="coucou", regard=(1, 0), **{**NASREDDINE, **HABITS_TRAVAIL}))
    S.add(coussins(620, 640, 0.8))
    S.add(personne(440, 790, 1.1, expr="degoute", bras="croises", flip=True, regard=(-1, 0), **INVITES[0]))
    S.add(personne(580, 790, 1.1, expr="fache", bras="dos", flip=True, regard=(-1, 0), **INVITES[1]))
    S.add(personne(720, 790, 1.05, expr="neutre", bras="hanches", flip=True, regard=(-1, 0), **HOTE))
    S.add(texte(470, 230, "Hum…", 50, "#862e9c", contour="#fff"))
    S.cachette(300, 795)
    return S


def p03():
    """Plan moyen : au bout du tapis, Nasreddine attend, tout seul ; les plats passent devant lui pour les autres ; son ventre gargouille."""
    S = Scene()
    salle_festin(S)
    S.add(plateau(560, 760, 1.0))
    S.add(assis(560, 700, 0.8, expr="rire", bras="ventre", regard=(1, 0), **INVITES[2]))
    S.add(assis(700, 760, 0.85, expr="miam", bras="bas", flip=True, regard=(-1, 0), **INVITES[1]))
    S.add(assis(200, 790, 1.05, expr="triste", bras="joues", regard=(1, 0), **{**NASREDDINE, **HABITS_TRAVAIL}))
    S.add(texte(200, 420, "Grrr…", 40, "#868e96", contour="#fff"))
    S.cachette(60, 795)
    return S


def p04():
    """Plan moyen : au soir, Nasreddine repart chez lui sur son âne, l'air malin : il a une idée."""
    S = Scene()
    jardin(S, soir=True)
    S.add(ane_profil(380, 760, 1.1, expr="sourire"))
    S.add(personne(370, 760 - 70 * 1.1, 0.85, expr="malin", bras="pense", sy=0.8, **{**NASREDDINE, **HABITS_TRAVAIL}))
    S.add(pensee(560, 220, 80, "", depuis=(420, 440)))
    S.add(place([chemin("M -30 -50 L 30 -50 L 44 50 L -44 50 Z", "#862e9c"), trait(0, -50, 0, 50, "#fab005", 4)], 560, 220, 0.8))
    S.cachette(60, 790)
    return S


def p05():
    """Gros plan : chez lui, devant le miroir, Nasreddine enfile son plus beau manteau, violet et brodé d'or, et son grand turban blanc."""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.ambiance("interieur")
    S.add(miroir(560, 520, 1.0))
    S.add(personne(330, 790, 1.5, expr="fier", bras="hanches", regard=(1, 0), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(lampe(680, 600, 0.9))
    S.camera(1.4, 400, 470)
    S.dessus(texte(400, 90, "Mon plus beau manteau !", 46, "#862e9c", contour="#fff"))
    S.cachette(620, 735)
    return S


def p06():
    """Plan large : Nasreddine revient au festin dans son beau manteau ; l'hôte s'incline : « Bienvenue, honorable Nasreddine ! La place d'honneur ! »"""
    S = Scene()
    salle_festin(S)
    S.add(porte(80, 560, 140, 300, ouverte=True))
    S.add(personne(200, 790, 1.2, expr="malin", bras="dos", regard=(1, 0), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(personne(450, 790, 1.2, expr="rire", bras="ouverts", flip=True, regard=(-1, 0), rot=-8, **HOTE))
    S.add(personne(620, 790, 1.05, expr="content", bras="applaudit", flip=True, regard=(-1, 0), **INVITES[0]))
    S.add(personne(740, 790, 1.0, expr="joie", bras="mains_jointes", flip=True, regard=(-1, 0), **INVITES[1]))
    S.add(bulle(500, 160, 560, 110, "Bienvenue, honorable Nasreddine !\nÀ la place d'honneur !", 28, pointe=(460, 430)))
    S.cachette(70, 400, "air")
    return S


def p07():
    """Plan moyen : assis à la place d'honneur, sur de beaux coussins, Nasreddine reçoit la soupe, le pilaf et les baklavas."""
    S = Scene()
    salle_festin(S)
    S.add(coussins(400, 640, 1.0))
    S.add(assis(400, 690, 1.0, expr="malin", bras="dos", regard=(0, 1), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(plateau(400, 800, 1.1))
    S.add(personne(650, 790, 1.15, expr="content", bras="tend", flip=True, regard=(-1, 0), **HOTE))
    S.add(personne(150, 790, 1.05, expr="content", bras="mains_jointes", regard=(1, 0), **INVITES[2]))
    S.add(bulle(560, 160, 420, 80, "Servez-vous, servez-vous !", 30, pointe=(640, 450)))
    S.cachette(730, 330, "air")
    return S


def p08():
    """Gros plan : Nasreddine trempe la manche de son manteau dans la soupe : « Mange, mon manteau, mange ! »"""
    S = Scene()
    salle_festin(S)
    S.add(personne(340, 700, 1.5, expr="malin", bras="tend", regard=(1, 0.6), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(plateau(300, 810, 1.2, plats=("pilaf", "baklava")))
    S.add(manche_dans_bol(340, 700, 1.5, 745))
    S.camera(1.5, 420, 560)
    S.dessus(bulle(400, 100, 560, 90, "Mange, mon manteau, mange !", 34))
    S.cachette(620, 785)
    return S


def p09():
    """Plan moyen : les invités sont stupéfaits ; Nasreddine explique : « C'est mon manteau que vous avez invité ! » ; l'hôte rougit, honteux."""
    S = Scene()
    salle_festin(S)
    S.add(personne(400, 790, 1.3, expr="malin", bras="leve_doigt", regard=(1, 0), **{**NASREDDINE, **BEAU_MANTEAU}))
    S.add(personne(620, 790, 1.15, expr="oups", bras="gratte", flip=True, regard=(-1, 0), **HOTE))
    S.add(personne(160, 790, 1.05, expr="bouche_bee", bras="joues", regard=(1, 0), **INVITES[0]))
    S.add(personne(260, 790, 1.0, expr="surpris", bras="surprise", regard=(1, 0), **INVITES[1]))
    S.add(personne(750, 790, 1.0, expr="rire", bras="ventre", flip=True, regard=(-1, 0), **INVITES[2]))
    S.add(bulle(400, 160, 540, 110, "C'est mon manteau\nque vous avez invité !", 32, pointe=(400, 400)))
    S.cachette(60, 795)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ane-seul.svg", vignette),
    ("01-au-jardin.svg", p01), ("02-le-festin.svg", p02), ("03-oublie.svg", p03),
    ("04-sur-son-ane.svg", p04), ("05-le-beau-manteau.svg", p05), ("06-le-retour.svg", p06),
    ("07-les-meilleurs-plats.svg", p07), ("08-mange-mon-manteau.svg", p08), ("09-la-lecon.svg", p09),
]
