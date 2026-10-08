"""Le Meunier, son Fils et l'Âne — on ne peut pas plaire à tout le monde."""
from fables import *

ID = "meunier-ane"

GRIS = "#9aa1a8"
MEUNIER = dict(coiffure="chauve_cote", cheveux="gris", peau="rosee", habit="#f8f9fa", robe=False, jambes="#868e96",
               barbe="#dee2e6", chaussures="#495057")
FILS = dict(coiffure="herisses", cheveux="chatain", peau="rosee", habit="#228be6", jambes="#495057")


def meunier(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MEUNIER, **k})


def fils(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**FILS, **k})


def cavalier(fn, x_ane, y_ane, s_ane, s_perso, dx=0, **k):
    """Personnage assis sur l'âne : on le dessine avant l'âne, dont le corps cache ses jambes."""
    y = y_ane - 78 * s_ane + 30 * s_perso
    return fn(x_ane + dx * s_ane, y, s_perso, **k)


def monte(S, x, y, s, cavaliers=(), **k):
    for c in cavaliers:
        S.add(c)
    S.add(ane_profil(x, y, s, **k))


def route(S, soir=False, moulin_=False):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(160, 110, 0.6), nuage(620, 160, 0.5))
    collines(S, 580, "#b2f2bb", graine=91)
    sol(S, 600, "#8ce99a")
    S.add(chemin("M 0 700 Q 400 650 800 690 L 800 800 L 0 800 Z", "#f3d9a4"))
    if moulin_:
        S.add(moulin(660, 610, 0.8))


def passant(x, y, s=1.0, n_=0, **k):
    styles = [dict(coiffure="courts", cheveux="noir", peau="brune", habit="#fab005", robe=False, jambes="#5c3a1e"),
              dict(coiffure="longs", cheveux="blond", peau="claire", habit="#e64980"),
              dict(coiffure="boucles", cheveux="roux", peau="rosee", habit="#7048e8"),
              dict(coiffure="chignon", cheveux="brun", peau="doree", habit="#12b886"),
              dict(coiffure="courts", cheveux="chatain", peau="rosee", habit="#c92a2a", robe=False, jambes="#343a40", barbe="#8d5524"),
              dict(coiffure="tresses", cheveux="noir", peau="foncee", habit="#fd7e14")]
    return personne(x, y, s, **{**styles[n_ % len(styles)], **k})


def ane_porte(S, x=400, y=560, s=1.0):
    """Le meunier et son fils portent l'âne sur un bâton, les pattes en l'air."""
    S.add(meunier(x - 250 * s, y + 200 * s, 1.1 * s, expr="concentre", bras="haut"))
    S.add(fils(x + 250 * s, y + 200 * s, 1.0 * s, expr="concentre", bras="haut"))
    S.add(ane_profil(x, y - 40 * s, 0.9 * s, expr="surpris", rot=180, regard=(-1, 1)))
    S.add(baton(x - 330 * s, y + 8 * s, x + 330 * s, y + 8 * s, ep=14 * s))


def couverture():
    S = Scene()
    route(S, moulin_=True)
    monte(S, 400, 740, 1.4, cavaliers=[cavalier(meunier, 400, 740, 1.4, 1.05, dx=-30, expr="surpris", bras="bas"),
                                       cavalier(fils, 400, 740, 1.4, 0.95, dx=-80, expr="rire", bras="haut")],
          expr="oups")
    S.add(passant(120, 790, 0.9, 0, expr="rire", bras="montre"))
    S.add(passant(700, 790, 0.9, 1, expr="fache", bras="croises"))
    S.cachette(70, 410, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ane_profil(170, 250, 0.95, expr="content"))
    return S


def p01():
    S = Scene()
    route(S, moulin_=True)
    S.add(meunier(200, 760, 1.35, expr="content", bras="salut"))
    S.add(fils(360, 770, 1.1, expr="rire"))
    S.add(ane_profil(520, 760, 1.2, expr="content"))
    return S


def p02():
    S = Scene()
    route(S)
    ane_porte(S, 400, 470, 1.0)
    return S


def p03():
    S = Scene()
    route(S)
    ane_porte(S, 400, 470, 0.8)
    S.add(passant(700, 790, 0.95, 0, expr="rire", bras="montre", flip=True))
    S.add(bulle(560, 120, 440, 110, "Quels nigauds !\nC'est l'âne qui porte !", 34, pointe=(690, 520)))
    return S


def p04():
    S = Scene()
    route(S)
    monte(S, 420, 740, 1.3, cavaliers=[cavalier(fils, 420, 740, 1.3, 1.0, dx=-20, expr="rire", bras="haut")], expr="content")
    S.add(meunier(170, 770, 1.25, expr="content", bras="bas"))
    return S


def p05():
    S = Scene()
    route(S)
    monte(S, 330, 740, 1.2, cavaliers=[cavalier(fils, 330, 740, 1.2, 0.95, dx=-20, expr="oups", bras="bas")], expr="content")
    S.add(meunier(110, 770, 1.15, expr="inquiet"))
    S.add(passant(620, 790, 1.0, 4, expr="fache", bras="montre", flip=True))
    S.add(passant(730, 790, 0.95, 0, expr="fache", bras="croises"))
    S.add(bulle(520, 130, 480, 110, "Le jeune est assis et le\nvieux père marche ?", 32, pointe=(620, 540)))
    S.cachette(240, 70, "air")
    return S


def p06():
    S = Scene()
    route(S)
    monte(S, 420, 740, 1.3, cavaliers=[cavalier(meunier, 420, 740, 1.3, 1.05, dx=-20, expr="content", bras="bas")], expr="sourire")
    S.add(fils(160, 780, 1.0, expr="neutre"))
    return S


def p07():
    S = Scene()
    route(S)
    monte(S, 330, 740, 1.2, cavaliers=[cavalier(meunier, 330, 740, 1.2, 1.0, dx=-20, expr="oups", bras="bas")], expr="sourire")
    S.add(fils(110, 780, 0.95, expr="triste"))
    S.add(passant(620, 790, 1.0, 1, expr="fache", bras="montre", flip=True))
    S.add(passant(730, 790, 0.95, 5, expr="fache", bras="hanches"))
    S.add(bulle(520, 130, 480, 110, "Quel père sans cœur !\nSon fils marche à pied !", 32, pointe=(620, 540)))
    S.cachette(240, 70, "air")
    return S


def p08():
    S = Scene()
    route(S)
    monte(S, 420, 740, 1.3, cavaliers=[cavalier(meunier, 420, 740, 1.3, 1.0, dx=-10, expr="content", bras="bas"),
                                       cavalier(fils, 420, 740, 1.3, 0.9, dx=-65, expr="rire", bras="haut")],
          expr="inquiet")
    return S


def p09():
    S = Scene()
    route(S)
    monte(S, 330, 740, 1.2, cavaliers=[cavalier(meunier, 330, 740, 1.2, 1.0, dx=-10, expr="surpris", bras="bas"),
                                       cavalier(fils, 330, 740, 1.2, 0.9, dx=-65, expr="surpris", bras="bas")],
          expr="pleure", ploie=True)
    S.add(passant(650, 790, 1.0, 3, expr="furieux", bras="montre", flip=True))
    S.add(bulle(540, 130, 460, 110, "Pauvre bête ! Deux sur\nun seul âne !", 34, pointe=(640, 540)))
    return S


def p10():
    S = Scene()
    route(S)
    S.add(meunier(180, 770, 1.2, expr="sourire"))
    S.add(fils(330, 780, 1.0, expr="sourire"))
    S.add(ane_profil(560, 760, 1.2, expr="rire"))
    S.add(notes(560, 450, 0.9))
    S.cachette(650, 70, "air")
    return S


def p11():
    S = Scene()
    route(S)
    S.add(meunier(150, 770, 1.1, expr="surpris"))
    S.add(fils(280, 780, 0.95, expr="surpris"))
    S.add(ane_profil(430, 760, 1.0, expr="content"))
    S.add(passant(700, 790, 1.0, 2, expr="rire", bras="montre", flip=True))
    S.add(bulle(560, 130, 440, 110, "Ils ont un âne\net ils vont à pied !", 34, pointe=(690, 540)))
    S.cachette(280, 70, "air")
    return S


def p12():
    S = Scene()
    route(S)
    S.add(meunier(360, 770, 1.55, expr="inquiet", bras="tete"))
    S.add(ane_profil(620, 760, 0.9, expr="surpris", flip=True))
    S.add(pensee(170, 200, 120, depuis=(290, 400), contenu=texte(170, 215, "???", 48, "#228be6")))
    return S


def p13():
    S = Scene()
    route(S)
    S.add(meunier(300, 770, 1.55, expr="rire", bras="calin"))
    S.add(fils(520, 780, 1.1, expr="rire"))
    S.add(texte(400, 180, "Ha ha ha !", 64, "#228be6", contour="#fff"))
    return S


def p14():
    S = Scene()
    route(S)
    S.add(meunier(300, 770, 1.55, expr="fier", bras="hanches"))
    S.add(ane_profil(560, 760, 1.0, expr="content", flip=True, regard=(1, 0)))
    S.add(bulle(330, 130, 460, 110, "Désormais, je ferai\nà ma tête !", 36, pointe=(300, 400)))
    return S


def p15():
    S = Scene()
    route(S, soir=True, moulin_=True)
    monte(S, 420, 740, 1.2, cavaliers=[cavalier(fils, 420, 740, 1.2, 0.95, dx=-20, expr="rire", bras="haut")], expr="rire")
    S.add(meunier(170, 770, 1.2, expr="chante", bras="bas"))
    S.add(notes(300, 380, 1.1), notes(560, 330, 0.9))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ane-seul.svg", vignette),
    ("01-au-marche.svg", p01), ("02-porter-l-ane.svg", p02), ("03-quels-nigauds.svg", p03),
    ("04-le-fils-monte.svg", p04), ("05-les-marchands.svg", p05), ("06-le-pere-monte.svg", p06),
    ("07-sans-coeur.svg", p07), ("08-tous-les-deux.svg", p08), ("09-pauvre-bete.svg", p09),
    ("10-a-pied.svg", p10), ("11-ils-vont-a-pied.svg", p11), ("12-que-faire.svg", p12),
    ("13-ha-ha-ha.svg", p13), ("14-a-ma-tete.svg", p14), ("15-en-chantant.svg", p15),
]
