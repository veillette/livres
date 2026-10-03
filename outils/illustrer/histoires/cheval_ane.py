"""Le Cheval et l'Âne — il faut s'entraider."""
from fables import *

ID = "cheval-ane"

PRUNE = "#862e9c"
MARCHAND = dict(coiffure="courts", cheveux="noir", peau="doree", habit="#e8590c", robe=False, jambes="#495057",
                chaussures="#343a40")


def marchand(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MARCHAND, **k})


def ane(S, x, y, s=1.0, nb=0, ploie=False, **k):
    """L'âne de profil, avec `nb` sacs sur le dos."""
    S.add(ane_profil(x, y, s, ploie=ploie, **k))
    if nb:
        S.add(bat(x, y - (110 - (16 if ploie else 0)) * s, s, nb=nb))


def cheval(S, x, y, s=1.0, nb=0, **k):
    charge = bat(0, -160, 1.0, nb=nb) if nb else None
    S.add(cheval_profil(x, y, s, charge=charge, **k))


def route(S, montee=False, soir=False, ville=False, graine=131):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(150, 110, 0.6), nuage(640, 150, 0.5))
    if ville:
        S.add(g([rect(560 + k * 70, 380 - (k % 3) * 40, 60, 200 + (k % 3) * 40, ["#ffc9c9", "#d0bfff", "#a5d8ff"][k % 3]) for k in range(4)]))
    collines(S, 580, "#b2f2bb", graine=graine)
    if montee:
        S.add(chemin("M 0 800 L 0 700 Q 400 640 800 470 L 800 800 Z", "#8ce99a"))
        S.add(chemin("M 0 760 Q 400 700 800 530 L 800 610 Q 400 780 0 800 Z", "#f3d9a4"))
    else:
        sol(S, 600, "#8ce99a")
        S.add(chemin("M 0 700 Q 400 650 800 690 L 800 800 L 0 800 Z", "#f3d9a4"))


def couverture():
    S = Scene()
    route(S)
    cheval(S, 520, 760, 1.25, expr="fier", regard=(1, -1))
    ane(S, 190, 770, 1.0, nb=3, ploie=True, expr="pleure")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cheval_profil(150, 262, 0.62, expr="sourire"))
    S.add(ane_profil(300, 262, 0.55, expr="sourire"))
    return S


def p01():
    S = Scene()
    route(S)
    S.add(marchand(620, 760, 1.25, expr="content", bras="salut"))
    cheval(S, 380, 760, 0.95, expr="sourire")
    ane(S, 140, 770, 0.8, nb=2, expr="sourire")
    return S


def p02():
    S = Scene()
    route(S, graine=132)
    cheval(S, 540, 760, 1.15, expr="fier", regard=(1, -1))
    ane(S, 190, 770, 1.0, nb=4, expr="inquiet")
    S.add(texte(560, 230, "Rien sur le dos !", 40, PRUNE, contour="#fff"))
    S.add(texte(200, 420, "Tous les sacs !", 40, PRUNE, contour="#fff"))
    return S


def p03():
    S = Scene()
    route(S, montee=True)
    S.add(g([ane_profil(250, 740, 0.95, ploie=True, expr="triste")], transform="rotate(-12 250 740)"))
    S.add(g([bat(250, 740 - 94 * 0.95, 0.95, nb=4)], transform="rotate(-12 250 740)"))
    S.add(texte(250, 320, "Pff… pff…", 48, PRUNE, contour="#fff"))
    return S


def p04():
    S = Scene()
    route(S, graine=133)
    ane(S, 190, 770, 1.0, nb=4, ploie=True, expr="triste")
    cheval(S, 560, 760, 1.05, expr="neutre", regard=(-1, 0), flip=True)
    S.add(bulle(300, 140, 520, 140, "Cheval, aide-moi ! Prends\nun peu de ma charge…", 32, pointe=(260, 470)))
    return S


def p05():
    S = Scene()
    route(S, graine=133)
    ane(S, 190, 770, 1.0, nb=4, ploie=True, expr="surpris")
    cheval(S, 560, 760, 1.05, expr="fier", regard=(1, -1))
    S.add(bulle(500, 140, 560, 140, "Ce n'est pas mon travail !\nJe suis un cheval, moi !", 32, pointe=(700, 420)))
    return S


def p06():
    S = Scene()
    route(S, graine=134)
    ane(S, 330, 770, 1.15, nb=4, ploie=True, expr="pleure")
    for xx in (240, 290, 380, 430):
        S.add(mouvement(xx, 760, 0.4, rot=90))
    S.add(texte(400, 250, "Mes pattes tremblent…", 42, PRUNE, contour="#fff"))
    return S


def p07():
    S = Scene()
    route(S, graine=135)
    S.add(ane_profil(330, 840, 1.15, ploie=True, expr="dort"))
    for k, (xx, rot) in enumerate([(160, -40), (500, 30), (620, -20), (260, 60)]):
        S.add(place(sac(0, 0, 0.8), xx, 770 + (k % 2) * 16, rot=rot))
    S.add(texte(400, 250, "Badaboum !", 56, "#c92a2a", contour="#fff"))
    return S


def p08():
    S = Scene()
    route(S, graine=135)
    S.add(ane_profil(260, 840, 1.15, ploie=True, expr="triste"))
    S.add(marchand(560, 760, 1.3, expr="inquiet", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(500, 140, 520, 120, "Mon pauvre âne !\nTu as besoin de repos.", 34, pointe=(560, 420)))
    return S


def p09():
    S = Scene()
    route(S, graine=136)
    S.add(marchand(170, 760, 1.2, expr="concentre", bras="haut"))
    cheval(S, 480, 760, 1.1, nb=5, expr="surpris")
    S.add(texte(480, 220, "Tous les sacs ?!", 48, PRUNE, contour="#fff"))
    return S


def p10():
    S = Scene()
    route(S, montee=True, graine=137)
    S.add(g([cheval_profil(380, 740, 1.05, expr="oups", ploie=True, charge=bat(0, -160, 1.0, nb=5))], transform="rotate(-12 380 740)"))
    S.add(ane_profil(110, 800, 0.6, expr="sourire"))
    S.add(texte(330, 220, "Ouf ! Que c'est lourd !", 46, PRUNE, contour="#fff"))
    return S


def p11():
    S = Scene()
    route(S, soir=True, ville=True, graine=138)
    cheval(S, 360, 760, 1.05, nb=5, expr="triste", ploie=True)
    S.add(pensee(520, 200, 150, g([ane_profil(440, 270, 0.4, expr="sourire"), bat(440, 270 - 44, 0.4, nb=2),
                                   cheval_profil(600, 270, 0.4, expr="sourire", charge=bat(0, -160, 1.0, nb=2))]), depuis=(470, 420)))
    return S


def p12():
    S = Scene()
    route(S, graine=139)
    cheval(S, 520, 760, 1.05, nb=2, expr="sourire", regard=(-1, 0), flip=True)
    ane(S, 200, 770, 0.95, nb=2, expr="surpris")
    S.add(bulle(500, 140, 520, 120, "Donne-moi la moitié,\nmon ami l'âne !", 34, pointe=(440, 420)))
    return S


def p13():
    S = Scene()
    route(S, soir=True, graine=140)
    cheval(S, 520, 760, 1.05, nb=2, expr="rire")
    ane(S, 200, 770, 0.95, nb=2, expr="rire")
    S.add(marchand(700, 760, 0.9, expr="content", bras="salut"))
    S.add(notes(330, 300, 1.2, PRUNE))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cheval-et-ane.svg", vignette),
    ("01-en-route.svg", p01), ("02-rien-sur-le-dos.svg", p02), ("03-ca-monte.svg", p03),
    ("04-aide-moi.svg", p04), ("05-pas-mon-travail.svg", p05), ("06-mes-pattes-tremblent.svg", p06),
    ("07-badaboum.svg", p07), ("08-mon-pauvre-ane.svg", p08), ("09-tous-les-sacs.svg", p09),
    ("10-que-c-est-lourd.svg", p10), ("11-si-j-avais-su.svg", p11), ("12-la-moitie.svg", p12),
    ("13-cote-a-cote.svg", p13),
]
