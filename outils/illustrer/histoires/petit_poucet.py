"""Le Petit Poucet — le plus petit, mais le plus malin."""
from contes import *

ID = "petit-poucet"
POUCET = dict(coiffure="herisses", cheveux="roux", peau="claire", habit="#fa5252", robe=False, jambes="#5c3a1e", chaussures="#343a40")
COULEURS = ("#4dabf7", "#51cf66", "#fcc419", "#9775fa", "#ff922b", "#20c997")
CHEVEUX = ("roux", "chatain", "roux", "brun", "chatain", "roux")
PAPA = dict(coiffure="courts", cheveux="roux", barbe="#d9480f", peau="rosee", habit="#8d5524", robe=False, jambes="#495057")
MAMAN = dict(coiffure="chignon", cheveux="chatain", peau="claire", habit="#e64980")


def poucet(x, y, s=0.55, **k):
    return personne(x, y, s, **{**POUCET, **k})


def frere(i, x, y, s=None, **k):
    s = s or (1.0 - i * 0.06)
    d = dict(coiffure="courts", cheveux=CHEVEUX[i], peau="claire", habit=COULEURS[i], robe=False, jambes="#495057")
    d.update(k)
    return personne(x, y, s, **d)


def freres(S, y=790, expr="sourire", x0=80, dx=100, **k):
    for i in range(6):
        S.add(frere(i, x0 + i * dx, y, expr=expr, **k))


def ogre(x, y, s=2.5, **k):
    k.setdefault("habit", "#862e9c")
    k.setdefault("peau", "#f3c3a0")
    k.setdefault("cheveux", "noir")
    k.setdefault("barbe", "#212529")
    k.setdefault("chaussures", "#5c3a1e")
    return geant(x, y, s, **k)


def maison_ogre(S, nuit_=True):
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 25, graine=17)
    S.add(lune(660, 110, 40))
    sol(S, 600, "#2b8a3e")
    S.add(maison(400, 640, 1.4, mur="#868e96", toit="#343a40", porte="#5c3a1e", lumiere=True))


def cuisine_ogre(S):
    interieur(S, "#e9d8c4", "#8d5524", 600, plinthe="#5c3a1e")
    S.add(fenetre(80, 100, 150, 140, nuit_=True, dehors="#1c2a52"))


def foret_(S, soir=False, graine=3):
    if soir:
        foret(S, "#1c2a52", "#5f3dc4", graine=graine)
        etoiles(S, 20, graine=graine)
        S.add(lune(660, 100, 36))
    else:
        foret(S, graine=graine)


def couverture():
    S = Scene()
    foret_(S, graine=21)
    S.add(cailloux_blancs(420, 800, 760, 700, 8))
    S.add(frere(0, 150, 790, 1.0, expr="surpris"), frere(3, 260, 790, 0.9, expr="surpris"))
    S.add(poucet(420, 790, 0.72, expr="malin", bras="montre"))
    S.add(bottes(640, 790, 0.7))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bottes(200, 250, 1.3))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    for x in (620, 740):
        S.add(sapin(x, 600, 1.3))
    sol(S, 590, "#94d82d")
    S.add(maison(130, 600, 0.7, mur="#e9d8c4", toit="#a0522d", porte="#6d4424"))
    S.add(personne(80, 790, 1.2, **PAPA, expr="content"), personne(720, 790, 1.15, **MAMAN, expr="content"))
    freres(S, 790, "rire", x0=190, dx=78)
    S.add(poucet(660, 790, 0.5, expr="rire", bras="haut"))
    S.cachette(470, 585)
    return S


def p02():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 580, papier="#ffe8cc")
    S.add(table(560, 790, 300, 150, "#8d5524"))
    S.add(poucet(560, 622, 0.9, expr="malin", bras="pense"))
    S.add(frere(0, 200, 790, 1.2, expr="surpris"), frere(1, 330, 790, 1.1, expr="rire"))
    S.add(texte(560, 250, "Tout petit…", 50, "#c92a2a", contour="#fff"), texte(560, 320, "mais très malin !", 50, "#c92a2a", contour="#fff"))
    return S


def p03():
    S = Scene()
    foret_(S, graine=5)
    S.add(cailloux_blancs(220, 790, 700, 700, 9, brille=False))
    S.add(poucet(200, 790, 0.65, expr="malin", bras="donne"))
    for i in range(3):
        S.add(frere(i, 400 + i * 130, 760, 0.9, expr="content", bras="porte", objet=g([rect(-40, -80, 80, 14, "#8d5524", rx=6), rect(-36, -94, 72, 14, "#a0522d", rx=6)])))
    return S


def p04():
    S = Scene()
    foret_(S, soir=True, graine=7)
    S.add(cailloux_blancs(60, 790, 740, 700, 12))
    S.add(poucet(260, 790, 0.68, expr="rire", bras="montre"))
    S.add(frere(0, 440, 790, 1.0, expr="pleure", larmes=True), frere(2, 560, 790, 0.95, expr="surpris"), frere(4, 680, 790, 0.9, expr="inquiet"))
    S.add(bulle(260, 380, 360, 90, "Suivez les cailloux !", 30, pointe=(260, 560)))
    return S


def p05():
    S = Scene()
    foret_(S, soir=True, graine=11)
    S.add(poucet(170, 790, 0.65, expr="inquiet", bras="tete"))
    for i in range(4):
        S.add(frere(i, 330 + i * 120, 790, 1.0 - i * 0.05, expr="pleure" if i % 2 else "inquiet"))
    S.add(texte(400, 180, "Perdus !", 72, "#fff", contour="#5f3dc4"))
    return S


def p06():
    S = Scene()
    foret_(S, soir=True, graine=13)
    S.add(gros_arbre_sombre(300, 800, 1.3))
    S.add(poucet(300, 380, 0.7, expr="surpris", bras="montre"))
    S.add(cercle(700, 470, 30, "#ffe066", opacity=0.5), cercle(700, 470, 12, "#ffe066"))
    S.add(texte(620, 380, "Une lumière !", 40, "#ffe066"))
    return S


def p07():
    S = Scene()
    maison_ogre(S)
    S.add(rect(372, 555, 56, 85, "#ffe066"))
    S.add(personne(400, 650, 0.8, coiffure="chignon", cheveux="noir", peau="rosee", habit="#ffa94d", expr="inquiet", bras="ouverts"))
    S.add(poucet(160, 790, 0.6, expr="timide"))
    for i in range(3):
        S.add(frere(i, 560 + i * 90, 790, 0.9, expr="inquiet"))
    S.add(bulle(400, 150, 520, 110, "Mes pauvres petits !\nIci, c'est la maison de l'ogre !", 28, pointe=(400, 440)))
    return S


def p08():
    S = Scene()
    cuisine_ogre(S)
    S.add(rect(380, 740, 380, 60, "#343a40"))
    for k in range(7):
        ex = 410 + k * 50
        S.add(ellipse(ex - 8, 770, 7, 9, "#fff"), ellipse(ex + 8, 770, 7, 9, "#fff"), cercle(ex - 6, 772, 4, ENCRE), cercle(ex + 10, 772, 4, ENCRE))
    S.add(rect(360, 540, 420, 30, "#8d5524", rx=8))
    S.add(chemin("M 370 566 L 770 566 L 780 740 Q 570 760 360 740 Z", "#fff4e6"))
    S.add(chemin("M 370 566 L 770 566 L 772 600 L 368 600 Z", "#e64980", opacity=0.5))
    S.add(ogre(200, 820, 2.4, expr="furieux", bras="hanches"))
    S.add(texte(560, 140, "BOUM ! BOUM !", 60, "#862e9c", contour="#fff"))
    return S


def p09():
    S = Scene()
    cuisine_ogre(S)
    S.add(ogre(400, 830, 2.4, expr="dort", bras="croises", chaussures="#5c3a1e"))
    S.add(bottes(400, 810, 0.8))
    S.add(zzz(620, 200, 1.6))
    return S


def p10():
    S = Scene()
    cuisine_ogre(S)
    S.add(ogre(300, 830, 2.4, expr="dort", bras="croises", chaussures="#fbd9bd", jambes="#fbd9bd"))
    S.add(bottes(640, 790, 0.7, rot=10))
    S.add(poucet(540, 790, 0.8, expr="concentre", bras="tire"))
    S.add(zzz(470, 170, 1.4))
    return S


def p11():
    S = Scene()
    foret_(S, soir=True, graine=19)
    S.add(etincelles(330, 700, 1.4, graine=5))
    S.add(poucet(330, 790, 0.7, expr="rire", bras="haut"))
    S.add(bottes(330, 792, 0.23))
    for i in range(4):
        S.add(frere(i, 480 + i * 90, 790, 0.9, expr="bouche_bee"))
    return S


def p12():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff9db")
    S.add(soleil(680, 120, 44))
    collines(S, 640, "#b2f2bb", graine=4, hauteur=160)
    sol(S, 640, "#94d82d")
    S.add(chemin("M 80 600 Q 400 60 720 520", stroke="#fff", sw=6, stroke_dasharray="14 16"))
    S.add(poucet(400, 380, 0.9, expr="rire", bras="haut"))
    S.add(bottes(400, 382, 0.3))
    S.add(texte(400, 150, "Hop !", 80, "#e8590c", contour="#fff"))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 590, "#94d82d")
    S.add(maison(130, 600, 0.7, mur="#e9d8c4", toit="#a0522d", porte="#6d4424"))
    S.add(personne(300, 790, 1.25, **PAPA, expr="rire", bras="ouverts"), personne(480, 790, 1.2, **MAMAN, expr="pleure", bras="ouverts"))
    S.add(poucet(390, 790, 0.6, expr="rire", bras="haut"))
    for i in range(3):
        S.add(frere(i, 600 + i * 70, 790, 0.85, expr="rire", bras="haut"))
    S.add(coeur(390, 300, 1.5))
    return S


def p14():
    S = Scene()
    jardin_chateau(S, chateau_s=0.55)
    S.add(poucet(300, 790, 0.8, expr="fier", bras="donne", objet=place(g([rect(-40, -28, 80, 56, "#fff", stroke="#e9ecef", stroke_width=3), cercle(0, 0, 9, "#c92a2a")]), 90, -96)))
    S.add(bottes(300, 792, 0.27))
    S.add(roi(560, 790, 1.2, expr="rire", bras="ouverts"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bottes-seules.svg", vignette),
    ("01-sept-garcons.svg", p01), ("02-tres-malin.svg", p02), ("03-les-cailloux.svg", p03), ("04-suivez-les-cailloux.svg", p04),
    ("05-perdus.svg", p05), ("06-une-lumiere.svg", p06), ("07-la-maison.svg", p07), ("08-l-ogre.svg", p08),
    ("09-les-bottes.svg", p09), ("10-tout-doucement.svg", p10), ("11-a-sa-taille.svg", p11), ("12-hop.svg", p12),
    ("13-a-la-maison.svg", p13), ("14-messager.svg", p14),
]
