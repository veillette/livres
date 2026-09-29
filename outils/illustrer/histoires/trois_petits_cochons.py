"""Les trois petits cochons — prendre le temps de bien faire."""
from contes import *

ID = "trois-petits-cochons"
COCHONS = [dict(habit="#4dabf7"), dict(habit="#51cf66"), dict(habit="#fa5252", acc=("casque",), couleur_acc="#fcc419")]


def cochon(i, x, y, s=1.0, **k):
    d = dict(COCHONS[i])
    d.update(k)
    return perso("cochon", x, y, s, **d)


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def campagne(S, y=600, soleil_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    if soleil_:
        S.add(soleil(680, 110, 44))
    S.add(nuage(170, 120, 0.7))
    collines(S, y, "#b2f2bb", graine=12)
    sol(S, y, "#94d82d")
    S.add(fleur(40, y + 80, 0.7, "#ff8787"), fleur(760, y + 60, 0.7, "#fcc419"))


def couverture():
    S = Scene()
    campagne(S)
    S.add(maison_briques(560, 610, 0.9, fumee=True))
    S.add(loup(120, 760, 1.2, expr="malin", regard=(1, 0)))
    for i, x in enumerate((300, 440, 580)):
        S.add(cochon(i, x, 780, 1.1, expr="rire", bras="haut" if i != 1 else "salut"))
    return S


def vignette():
    S = Scene(400, 270)
    for i, x in enumerate((110, 200, 290)):
        S.add(cochon(i, x, 262, 0.95 if i == 1 else 0.85, expr="rire", bras="salut" if i == 1 else "bas"))
    return S


def p01():
    S = Scene()
    campagne(S)
    S.add(maison(140, 610, 0.7, mur="#ffe3ea", toit="#e64980"))
    S.add(perso("cochon", 300, 740, 1.45, expr="content", bras="ouverts", acc=("noeud",), couleur_acc="#e64980", habit="#f783ac"))
    for i, x in enumerate((470, 590, 710)):
        S.add(cochon(i, x, 760, 0.95, expr="joie", regard=(-1, 0)))
    S.add(baluchon(700, 610, 0.5))
    return S


def p02():
    S = Scene()
    campagne(S)
    S.add(maison_paille(330, 640, 1.1))
    S.add(cochon(0, 580, 760, 1.2, expr="rire", bras="haut"))
    S.add(texte(400, 150, "Vite fait !", 64, "#e67700", contour="#fff"))
    return S


def p03():
    S = Scene()
    campagne(S)
    S.add(maison_bois(330, 640, 1.1))
    S.add(cochon(1, 590, 760, 1.2, expr="concentre", bras="tient", objet=marteau(68, -146, 0.9, rot=-30)))
    for k in range(3):
        S.add(place(rect(-60, -10, 120, 20, "#c68642", rx=4), 620 + k * 10, 790 - k * 20))
    S.add(texte(560, 330, "Toc ! Toc !", 48, "#8d5524", contour="#fff"))
    return S


def p04():
    S = Scene()
    campagne(S)
    S.add(maison_briques(260, 640, 0.95))
    for k in range(4):
        S.add(rect(460 + (k % 2) * 30, 740 - (k // 2) * 26, 56, 24, "#e8590c", stroke="#ffd8a8", stroke_width=3))
    S.add(cochon(2, 620, 770, 1.2, expr="concentre", bras="porte", objet=rect(-30, -90, 60, 28, "#e8590c", stroke="#ffd8a8", stroke_width=3)))
    S.add(cochon(0, 700, 520, 0.6, expr="rire", bras="salut"), cochon(1, 770, 520, 0.6, expr="rire", bras="haut"))
    S.add(bulle(640, 330, 290, 90, "Tu viens jouer ?", 32, pointe=(720, 410)))
    return S


def p05():
    S = Scene()
    campagne(S, soleil_=False)
    S.add(maison_paille(560, 640, 1.1))
    S.add(cochon(0, 560, 640, 0.32, expr="inquiet"))
    S.add(loup(190, 770, 1.4, expr="malin", bras="montre", regard=(1, 0)))
    S.add(bulle(270, 140, 440, 110, "Petit cochon,\nlaisse-moi entrer !", 36, pointe=(210, 420)))
    S.add(bulle(600, 330, 300, 90, "Non, non, non !", 36, pointe=(570, 560)))
    return S


def p06():
    S = Scene()
    campagne(S, soleil_=False)
    S.add(maison_paille(560, 640, 1.1, souffle=1.0))
    S.add(cochon(0, 600, 770, 1.1, expr="surpris", bras="haut"))
    S.add(loup(160, 770, 1.4, expr="souffle"))
    S.add(rafales(250, 540, 1.2, "#74c0fc"))
    S.add(texte(420, 160, "FFFOU !", 90, "#1c7ed6", contour="#fff", rot=-5))
    return S


def p07():
    S = Scene()
    campagne(S)
    S.add(maison_bois(620, 630, 0.9))
    S.add(cochon(0, 350, 760, 1.2, expr="oups", bras="course"))
    S.add(mouvement(270, 630, 1.3))
    S.add(cochon(1, 760, 640, 0.55, expr="surpris", bras="salut"))
    return S


def p08():
    S = Scene()
    campagne(S, soleil_=False)
    S.add(maison_bois(560, 660, 1.0, tombe=1.0))
    S.add(cochon(0, 520, 760, 0.95, expr="surpris", bras="haut"), cochon(1, 660, 770, 1.0, expr="oups", bras="haut"))
    S.add(loup(150, 770, 1.35, expr="souffle"))
    S.add(rafales(240, 540, 1.1, "#74c0fc"))
    S.add(texte(560, 250, "CRAC !", 90, "#8d5524", contour="#fff", rot=6))
    return S


def p09():
    S = Scene()
    campagne(S)
    S.add(maison_briques(560, 640, 0.95))
    S.add(cochon(2, 450, 660, 0.6, expr="content", bras="salut"))
    S.add(cochon(0, 170, 760, 1.05, expr="oups", bras="course"), cochon(1, 330, 770, 1.05, expr="oups", bras="course"))
    S.add(mouvement(100, 640, 1.2), mouvement(260, 650, 1.2))
    S.add(texte(560, 150, "Vite !", 72, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    campagne(S, soleil_=False)
    S.add(maison_briques(560, 640, 0.95))
    S.add(loup(180, 770, 1.4, expr="souffle"))
    S.add(rafales(270, 520, 1.0, "#74c0fc"))
    S.add(texte(560, 150, "Même pas un poil !", 46, "#c92a2a", contour="#fff"))
    return S


def p11():
    S = Scene()
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 25, graine=7)
    S.add(lune(120, 110, 40))
    sol(S, 640, "#2b8a3e")
    S.add(maison_briques(420, 660, 1.2))
    S.add(loup(300, 420, 1.0, expr="malin", bras="haut", regard=(1, 0)))
    S.add(bulle(250, 150, 420, 90, "Par la cheminée !", 36, pointe=(290, 250)))
    return S


def p12():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 600, papier="#ffe8cc")
    S.add(rect(240, 120, 320, 480, "#adb5bd"), rect(270, 150, 260, 450, "#343a40"))
    S.add(chaudron(400, 590, 1.0, contenu="#74c0fc"))
    S.add(loup(400, 480, 0.8, expr="oups", bras="haut", rot=180))
    S.add(texte(400, 90, "PLOUF !", 80, "#1c7ed6", contour="#fff"))
    for i, x in enumerate((110, 680)):
        S.add(cochon(i * 2, x, 770, 1.1, expr="surpris", bras="joues"))
    return S


def p13():
    S = Scene()
    campagne(S)
    S.add(maison_briques(200, 640, 0.8, fumee=True))
    S.add(loup(540, 770, 1.3, expr="furieux", bras="course", larmes=True))
    S.add(chemin("M 620 660 q 30 -40 10 -80 q -20 -40 10 -70", stroke="#adb5bd", sw=10, opacity=0.7))
    S.add(mouvement(460, 640, 1.3))
    S.add(texte(560, 250, "Aïe, aïe, aïe !", 56, "#c92a2a", contour="#fff"))
    return S


def p14():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", 580, papier="#ffec99")
    S.add(fenetre(80, 150, 160, 140, nuit_=True, rideaux="#fa5252"))
    S.add(cadre_mur(560, 150))
    S.add(tapis(400, 720, 330, 60))
    S.add(cochon(0, 200, 740, 1.2, expr="chante", bras="ouverts"), cochon(1, 400, 760, 1.3, expr="rire", bras="haut"),
          cochon(2, 600, 740, 1.2, expr="chante", bras="ouverts", acc=()))
    S.add(notes(300, 400, 1.0), notes(520, 380, 0.9, "#e64980"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cochons-seuls.svg", vignette),
    ("01-maman.svg", p01), ("02-paille.svg", p02), ("03-bois.svg", p03), ("04-briques.svg", p04),
    ("05-laisse-moi-entrer.svg", p05), ("06-fffou.svg", p06), ("07-chez-mon-frere.svg", p07),
    ("08-crac.svg", p08), ("09-vite.svg", p09), ("10-rien-ne-bouge.svg", p10), ("11-le-toit.svg", p11),
    ("12-plouf.svg", p12), ("13-le-loup-s-enfuit.svg", p13), ("14-qui-a-peur.svg", p14),
]
