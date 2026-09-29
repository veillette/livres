"""Jack et le haricot magique — le courage d'aller voir là-haut."""
from contes import *

ID = "jack-haricot"
JACK = dict(coiffure="herisses", cheveux="roux", peau="claire", habit="#fab005", robe=False, jambes="#1864ab", chaussures="#5c3a1e")
MAMAN = dict(coiffure="chignon", cheveux="chatain", peau="claire", habit="#74c0fc")
VIEUX = dict(coiffure="chauve_cote", cheveux="blanc", barbe="#e9ecef", peau="rosee", habit="#7048e8", couleur_acc="#5f3dc4")


def jack(x, y, s=1.0, **k):
    return personne(x, y, s, **{**JACK, **k})


def maman(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def vache(x, y, s=1.0, flip=False, **k):
    corps = perso("boeuf", 0, 0, 1.0, couleur="#f1f3f5", visage="#fff", **k)
    taches = [ellipse(-24, -74, 14, 10, "#495057"), ellipse(22, -36, 12, 9, "#495057"), ellipse(-26, -178, 12, 9, "#495057")]
    return place([corps] + taches, x, y, s, flip=flip)


def geant_(x, y, s=2.6, **k):
    return geant(x, y, s, **k)


def poule_(x, y, s=1.0, **k):
    return coq(x, y, s, poule=True, couleur="#f8f9fa", ventre="#fff", **k)


def maisonnette(S, nuit_=False):
    if nuit_:
        nuit(S)
        etoiles(S, 25, graine=4)
        S.add(lune(660, 110, 40))
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(nuage(160, 110, 0.7))
    collines(S, 600, "#b2f2bb" if not nuit_ else "#2f9e44", graine=6)
    sol(S, 600, "#94d82d" if not nuit_ else "#2b8a3e")
    S.add(maison(220, 610, 0.9, mur="#e9d8c4", toit="#868e96", porte="#6d4424", lumiere=nuit_))


def la_haut(S):
    sol_nuages(S, 600)
    S.add(chateau_geant(460, 610, 0.95))


def cuisine_geant(S):
    interieur(S, "#e5dbff", "#a0693a", 640, papier="#d0bfff")
    S.add(rect(40, 40, 260, 220, "#fab005", rx=12), rect(58, 58, 224, 184, "#ffe066"))


def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(nuage(560, 380, 1.3), nuage(200, 420, 0.9))
    S.add(tige_haricot(400, 820, 200, 1.1))
    sol(S, 740, "#94d82d")
    S.add(jack(400, 600, 1.1, expr="rire", bras="haut"))
    S.add(poule_(160, 780, 0.9, expr="content"), oeuf_or(650, 780, 1.3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(haricots(200, 150, 2.0))
    return S


def p01():
    S = Scene()
    maisonnette(S)
    S.add(vache(560, 790, 1.2, expr="triste"))
    S.add(jack(380, 790, 1.2, expr="triste", bras="croises"), maman(160, 790, 1.2, expr="inquiet"))
    S.add(place(g([chemin("M -30 -60 L 30 -60 L 24 0 L -24 0 Z", "#adb5bd"), ellipse(0, -60, 30, 8, "#dee2e6")]), 700, 790))
    return S


def p02():
    S = Scene()
    maisonnette(S)
    S.add(maman(200, 790, 1.3, expr="triste", bras="montre"))
    S.add(jack(430, 790, 1.2, expr="sourire", bras="donne"))
    S.add(vache(640, 790, 1.15, expr="sourire"))
    S.add(bulle(460, 150, 420, 90, "Va vendre Blanchette !", 36, pointe=(260, 460)))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=2)
    sol(S, 600, "#94d82d")
    S.add(chemin("M 0 720 Q 400 650 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(vache(130, 780, 1.0))
    S.add(jack(330, 780, 1.2, expr="bouche_bee", regard=(1, 0)))
    S.add(personne(590, 780, 1.1, expr="malin", bras="donne2", acc=("chapeau_pointu",), **VIEUX))
    S.add(haricots(680, 690, 0.8))
    S.add(bulle(520, 150, 440, 110, "Ta vache contre\ncinq haricots magiques ?", 32, pointe=(580, 540)))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 580, papier="#ffe8cc")
    S.add(fenetre(520, 110, 180, 170, dehors="#a5d8ff"))
    S.add(jack(230, 790, 1.3, expr="fier", bras="donne", objet=haricots(80, -96, 0.5, brille=False)))
    S.add(maman(560, 790, 1.3, expr="furieux", bras="montre", regard=(1, -1)))
    S.add(texte(400, 80, "Des haricots ?!", 60, "#c92a2a", contour="#fff"))
    S.add(haricots(640, 230, 0.6, brille=False))
    return S


def p05():
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    S.add(soleil(120, 110, 44))
    S.add(nuage(560, 160, 1.0), nuage(250, 260, 0.7))
    collines(S, 600, "#b2f2bb", graine=6)
    sol(S, 600, "#94d82d")
    S.add(maison(220, 620, 0.9, mur="#e9d8c4", toit="#868e96", porte="#6d4424"))
    S.add(tige_haricot(560, 700, -40, 1.0))
    S.add(jack(430, 790, 1.0, expr="bouche_bee", bras="haut", regard=(1, -1)))
    return S


def p06():
    S = Scene()
    ciel(S, "#4dabf7", "#d0ebff")
    S.add(nuage(160, 700, 1.3), nuage(660, 740, 1.1))
    S.add(tige_haricot(400, 900, -60, 1.1))
    S.add(nuage(600, 200, 0.8), nuage(150, 150, 0.6))
    S.add(oiseau(640, 460, 0.6, "#4dabf7", expr="surpris", ailes="haut"), oiseau(160, 380, 0.5, "#ff922b", expr="surpris", ailes="haut"))
    S.add(jack(400, 520, 1.0, expr="concentre", bras="haut"))
    S.add(texte(400, 80, "Plus haut que les nuages !", 44, "#1864ab", contour="#fff"))
    return S


def p07():
    S = Scene()
    la_haut(S)
    S.add(tige_haricot(100, 900, 540, 0.8))
    S.add(jack(180, 760, 0.9, expr="bouche_bee", bras="joues", regard=(1, -1)))
    return S


def p08():
    S = Scene()
    cuisine_geant(S)
    S.add(table(560, 700, 360, 200, "#6d4424"))
    S.add(cage(560, 480, 1.1))
    S.add(poule_(560, 470, 0.8, expr="pleure"))
    S.add(oeuf_or(640, 490, 0.6), oeuf_or(700, 490, 0.6))
    S.add(jack(200, 790, 0.9, expr="surpris", regard=(1, -1)))
    S.add(bulle(360, 180, 380, 100, "Aide-moi !\nJe suis prisonnière.", 30, pointe=(520, 340)))
    return S


def p09():
    S = Scene()
    cuisine_geant(S)
    S.add(geant_(520, 830, 2.7, expr="furieux", bras="hanches", regard=(-1, 0)))
    S.add(rect(30, 500, 160, 300, "#8d5524", rx=8), rect(40, 540, 140, 250, "#343a40"))
    S.add(jack(110, 790, 0.9, expr="oups", bras="bouche", regard=(1, 0)))
    S.add(texte(560, 110, "BOUM ! BOUM !", 60, "#5f3dc4", contour="#fff"))
    return S


def p10():
    S = Scene()
    cuisine_geant(S)
    S.add(geant_(420, 820, 2.5, expr="dort", bras="croises"))
    S.add(zzz(590, 225, 1.6))
    S.add(texte(250, 110, "RRRR…", 60, "#5f3dc4", contour="#fff"))
    return S


def p11():
    S = Scene()
    cuisine_geant(S)
    S.add(table(560, 700, 360, 200, "#6d4424"))
    S.add(cage(620, 480, 1.0))
    S.add(jack(300, 790, 1.3, expr="oups", bras="porte", objet=poule_(0, -40, 0.7, expr="joie", bec_ouvert=True)))
    S.add(texte(560, 150, "Cot cot codet !", 56, "#e8590c", contour="#fff"))
    return S


def p12():
    S = Scene()
    ciel(S, "#4dabf7", "#d0ebff")
    S.add(nuage(400, 60, 3.0))
    S.add(tige_haricot(400, 900, -60, 1.1))
    S.add(geant_(400, 360, 1.2, expr="furieux", bras="haut"))
    S.add(jack(400, 700, 0.9, expr="oups", bras="haut", objet=""))
    S.add(poule_(470, 560, 0.5, expr="surpris", ailes="haut"))
    for k in range(3):
        S.add(mouvement(300 - k * 10, 400 + k * 120, 1.0, rot=90))
    return S


def p13():
    S = Scene()
    maisonnette(S)
    S.add(tige_haricot(560, 700, -40, 1.0))
    S.add(jack(430, 790, 1.2, expr="concentre", bras="tient", objet=hache(68, -146, 0.9, rot=60)))
    S.add(maman(170, 790, 1.2, expr="surpris", bras="joues"))
    S.add(texte(660, 520, "Tchac !", 64, "#c92a2a", contour="#fff", rot=-10))
    return S


def p14():
    S = Scene()
    sol_nuages(S, 600)
    S.add(chateau_geant(620, 610, 0.6))
    S.add(geant_(300, 780, 2.2, expr="triste", bras="tete"))
    S.add(texte(560, 110, "Plus de tige !", 56, "#5f3dc4", contour="#fff"))
    return S


def p15():
    S = Scene()
    maisonnette(S)
    S.add(poule_(560, 780, 1.1, expr="fier"))
    S.add(oeuf_or(680, 790, 1.2), oeuf_or(740, 790, 0.8))
    S.add(jack(370, 790, 1.2, expr="rire", bras="haut"), maman(170, 790, 1.2, expr="rire", bras="joues"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("haricots-seuls.svg", vignette),
    ("01-blanchette.svg", p01), ("02-au-marche.svg", p02), ("03-le-petit-vieux.svg", p03), ("04-des-haricots.svg", p04),
    ("05-la-tige.svg", p05), ("06-plus-haut.svg", p06), ("07-le-chateau.svg", p07), ("08-la-poule.svg", p08),
    ("09-boum.svg", p09), ("10-le-geant-dort.svg", p10), ("11-cot-cot.svg", p11), ("12-la-descente.svg", p12),
    ("13-tchac.svg", p13), ("14-la-haut.svg", p14), ("15-oeufs-d-or.svg", p15),
]
