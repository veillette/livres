"""Le Lièvre et la Tortue — rien ne sert de courir, il faut partir à point."""
from fables import *

ID = "lievre-tortue"


def lievre(x, y, s=1.0, **k):
    return perso("lievre", x, y, s, **k)


def pre(S, ciel_haut="#74c0fc", ciel_bas="#e7f5ff", chemin_=True, soleil_=(660, 130)):
    ciel(S, ciel_haut, ciel_bas)
    if soleil_:
        S.add(soleil(*soleil_, 50))
    S.add(nuage(160, 130, 0.6))
    collines(S, 580, "#b2f2bb", graine=6)
    sol(S, 600, "#8ce99a")
    if chemin_:
        S.add(chemin("M 0 760 Q 300 700 480 650 Q 640 610 800 610 L 800 650 Q 640 660 500 700 Q 320 760 0 800 Z", "#f3d9a4"))


def gros_chene(x=690, y=620, s=0.8):
    return arbre(x, y, s, feuillage="#40c057", feuillage2="#2f9e44", tronc="#7c4a1e")


def arrivee(x, y, s=1.0, coupee=False):
    m = [rect(-120, -150, 10, 150, "#868e96"), rect(110, -150, 10, 150, "#868e96")]
    if coupee:
        m += [chemin("M -110 -140 Q -80 -100 -40 -120", stroke="#fa5252", sw=8), chemin("M 110 -140 Q 80 -100 40 -120", stroke="#fa5252", sw=8)]
    else:
        m.append(chemin("M -110 -140 Q 0 -110 110 -140", stroke="#fa5252", sw=8))
    m.append(rect(-60, -200, 120, 40, "#fff", rx=8, stroke="#fa5252", stroke_width=4))
    m.append(texte(0, -170, "ARRIVÉE", 22, "#fa5252"))
    return place(m, x, y, s)


def spectateurs(S, y=770, s=0.8, xs=(90, 200, 610, 720)):
    S.add(perso("ecureuil", xs[0], y, s, expr="rire", bras="haut"))
    S.add(perso("herisson", xs[1], y, s * 0.9, expr="content", bras="haut"))
    S.add(perso("grenouille", xs[2], y, s * 0.9, expr="joie", bras="haut"))
    S.add(perso("souris", xs[3], y, s * 0.85, expr="rire", bras="haut"))


def couverture():
    S = Scene()
    pre(S)
    S.add(gros_chene(690, 610, 0.7))
    S.add(lievre(290, 700, 1.4, expr="rire", bras="course", rot=-8))
    S.add(mouvement(150, 560, 1.3))
    S.add(tortue(470, 760, 1.35, expr="concentre"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tortue(190, 240, 1.3, expr="content"))
    return S


def p01():
    S = Scene()
    pre(S)
    S.add(lievre(460, 720, 1.6, expr="rire", bras="course", rot=-10))
    S.add(mouvement(270, 560, 1.5), mouvement(250, 470, 1.2))
    S.add(texte(180, 330, "Zoum !", 70, "#2f9e44", contour="#fff", rot=-8))
    S.cachette(730, 230, "air")
    return S


def p02():
    S = Scene()
    pre(S)
    S.add(tortue(380, 730, 2.0, expr="content"))
    S.add(fleur(660, 740, 1.0, "#ff8787"), fleur(710, 760, 0.8, "#cc5de8"))
    S.add(papillon(640, 380, 1.4))
    return S


def p03():
    S = Scene()
    pre(S)
    S.add(lievre(230, 740, 1.5, expr="rire", bras="montre", regard=(1, 0)))
    S.add(tortue(560, 760, 1.4, expr="neutre", flip=True, regard=(1, 0)))
    S.add(bulle(260, 120, 400, 110, "Tu es si lente !\nHa ha ha !", 36, pointe=(240, 400)))
    return S


def p04():
    S = Scene()
    pre(S)
    S.add(gros_chene(700, 610, 0.6))
    S.add(lievre(200, 740, 1.4, expr="surpris", bras="bas", regard=(1, 0)))
    S.add(tortue(470, 760, 1.4, expr="malin", regard=(1, 0)))
    S.add(bulle(500, 150, 480, 120, "On fait la course ?\nJusqu'au gros chêne !", 34, pointe=(560, 580)))
    return S


def p05():
    S = Scene()
    pre(S, chemin_=False)
    S.add(lievre(400, 700, 1.6, expr="rire", bras="calin"))
    S.add(texte(400, 220, "Ha ha ha !", 70, "#2f9e44", contour="#fff"))
    spectateurs(S, 780, 0.75)
    S.cachette(730, 430, "air")
    return S


def p06():
    S = Scene()
    pre(S)
    S.add(rect(200, 690, 10, 110, "#fff"), rect(0, 720, 800, 8, "#fff", opacity=0.8))
    S.add(tortue(420, 740, 1.3, expr="concentre"))
    S.add(lievre(200, 720, 1.2, expr="malin", bras="croises"))
    S.add(perso("ecureuil", 650, 720, 1.1, expr="joie", bras="salut"))
    S.add(bulle(560, 150, 380, 100, "Partez !", 50, pointe=(640, 450)))
    return S


def p07():
    S = Scene()
    pre(S)
    S.add(lievre(380, 740, 1.6, expr="miam", bras="porte", objet=g([trait(0, -80, 0, -150, "#40c057", 5), trait(-10, -80, -24, -140, "#51cf66", 4), trait(10, -80, 28, -138, "#51cf66", 4)])))
    S.add(tortue(680, 640, 0.6, expr="concentre"))
    S.add(bulle(400, 140, 400, 100, "J'ai bien le temps !", 36, pointe=(400, 330)))
    return S


def p08():
    S = Scene()
    pre(S, chemin_=False)
    S.add(lievre(400, 760, 1.6, expr="rire", bras="tete", rot=0))
    S.add(papillon(560, 380, 1.4, "#fcc419", "#fa5252"), papillon(240, 330, 1.2))
    S.add(nuage(560, 170, 0.8), nuage(260, 200, 0.5))
    return S


def p09():
    S = Scene()
    pre(S)
    S.add(tortue(420, 720, 1.8, expr="concentre"))
    S.add(texte(200, 300, "Un pas…", 50, "#2f9e44", contour="#fff"))
    S.add(texte(560, 380, "puis un autre.", 44, "#2f9e44", contour="#fff"))
    return S


def p10():
    S = Scene()
    pre(S, chemin_=False, soleil_=(640, 150))
    S.add(arbre(650, 640, 1.5))
    S.add(lievre(580, 720, 1.5, expr="dort", bras="bas", rot=-78))
    S.add(zzz(330, 480, 1.4))
    return S


def p11():
    S = Scene()
    pre(S, chemin_=True, soleil_=(640, 180))
    S.add(arbre(300, 620, 1.3))
    S.add(lievre(390, 700, 1.2, expr="dort", rot=-78))
    S.add(zzz(200, 510, 1.0))
    S.add(tortue(580, 760, 1.4, expr="timide"))
    S.add(texte(600, 460, "Chut…", 50, "#2f9e44", contour="#fff"))
    S.cachette(730, 430, "air")
    return S


def p12():
    S = Scene()
    pre(S, ciel_haut="#ffa94d", ciel_bas="#ffe8cc", soleil_=(120, 420))
    S.add(gros_chene(690, 610, 0.6))
    S.add(tortue(610, 620, 0.5, expr="concentre"))
    S.add(lievre(260, 740, 1.6, expr="bouche_bee", bras="joues", regard=(1, -1)))
    return S


def p13():
    S = Scene()
    pre(S, ciel_haut="#ffa94d", ciel_bas="#ffe8cc", soleil_=(120, 430))
    S.add(lievre(430, 720, 1.6, expr="furieux", bras="course", rot=-18))
    S.add(mouvement(230, 560, 1.6), mouvement(210, 460, 1.3), mouvement(250, 650, 1.2))
    S.add(texte(620, 250, "ZOUM !", 76, "#e8590c", contour="#fff"))
    S.cachette(150, 120, "air")
    return S


def p14():
    S = Scene()
    pre(S, ciel_haut="#ffa94d", ciel_bas="#ffe8cc", soleil_=(120, 430), chemin_=False)
    S.add(gros_chene(640, 620, 0.9))
    S.add(arrivee(430, 720, 1.2, coupee=True))
    S.add(tortue(430, 740, 1.4, expr="rire"))
    spectateurs(S, 790, 0.7, xs=(100, 220, 700, 770))
    S.add(paillettes(430, 300, 1.4))
    S.cachette(730, 380, "air")
    return S


def p15():
    S = Scene()
    pre(S, ciel_haut="#ffa94d", ciel_bas="#ffe8cc", soleil_=(120, 430), chemin_=False)
    S.add(gros_chene(660, 620, 0.9))
    S.add(lievre(250, 750, 1.45, expr="timide", bras="donne", regard=(1, 0)))
    S.add(tortue(500, 760, 1.4, expr="content", flip=True, regard=(1, 0)))
    S.add(bulle(400, 130, 440, 90, "Bravo, Tortue !", 40, pointe=(260, 380)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tortue-seule.svg", vignette),
    ("01-lievre.svg", p01), ("02-tortue.svg", p02), ("03-si-lente.svg", p03),
    ("04-le-pari.svg", p04), ("05-ha-ha-ha.svg", p05), ("06-partez.svg", p06),
    ("07-bien-le-temps.svg", p07), ("08-les-papillons.svg", p08), ("09-un-pas.svg", p09),
    ("10-la-sieste.svg", p10), ("11-chut.svg", p11), ("12-le-reveil.svg", p12),
    ("13-zoum.svg", p13), ("14-arrivee.svg", p14), ("15-bravo.svg", p15),
]
