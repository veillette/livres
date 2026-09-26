"""Rose et le petit dragon — ne pas avoir peur de ce qu'on ne connaît pas."""
from base import *
from objets import *
from fantastique import *

ID = "rose-dragon"
ROSE_P = dict(coiffure="queue", cheveux="roux", habit="#e64980", peau="claire", acc=("diademe",))
PISTACHE = dict(couleur="#69db7c", ventre="#d8f5a2")
MAMAN = dict(couleur="#40c057", ventre="#c0eb75")


def foret(S, sombre=False):
    ciel(S, "#8ce99a" if not sombre else "#63c174", "#ebfbee")
    for x, s in [(80, 1.3), (260, 1.0), (560, 1.1), (740, 1.4)]:
        S.add(sapin(x, 600, s, "#2b8a3e", "#2f9e44"))
    sol(S, 600, "#69db7c", couleur2="#51cf66", y2=700)
    S.add(buisson(160, 700, 0.8), buisson(660, 720, 0.7, baies="#fa5252"))


def panier(x, y, s=1.0, pommes=True):
    m = [chemin("M -46 -40 Q 0 -110 46 -40", stroke="#a0522d", sw=6)]
    if pommes:
        m += [pomme(-18, -40, 0.7), pomme(16, -44, 0.7, "#ffd43b")]
    m += [chemin("M -52 -40 L 52 -40 L 40 0 L -40 0 Z", "#d9a066"),
          trait(-46, -26, 46, -26, "#a0522d", 3), trait(-42, -12, 42, -12, "#a0522d", 3)]
    return place(m, x, y, s)


def rocher(x, y, s=1.0):
    return place([chemin("M -150 0 Q -170 -110 -60 -150 Q 40 -190 120 -120 Q 170 -70 150 0 Z", "#adb5bd"),
                  chemin("M -80 -110 Q -30 -140 20 -120", stroke="#ced4da", sw=10)], x, y, s)


def couverture():
    S = Scene()
    jardin_chateau(S, "#ffdeeb", "#fff0f6", chateau_s=0.55, chateau_x=620, y=600)
    S.add(sapin(90, 620, 1.1, "#2b8a3e"), sapin(200, 610, 0.8, "#2f9e44"))
    S.add(personne(250, 770, 1.7, expr="rire", bras="calin", **ROSE_P))
    S.add(dragon(500, 770, 1.45, expr="rire", bras="salut", **PISTACHE))
    S.add(bulles_savon(560, 380, 1.0, graine=2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(dragon(200, 262, 0.95, expr="content", bras="salut", **PISTACHE))
    S.add(bulles_savon(260, 70, 0.6))
    return S


def p01():
    S = Scene()
    jardin_chateau(S, "#a5d8ff", "#fff0f6", chateau_s=0.85, chateau_x=420)
    S.add(personne(160, 760, 1.5, expr="rire", bras="haut", **ROSE_P))
    S.add(papillon(640, 520, 1.0), papillon(700, 440, 0.7, "#4dabf7"))
    S.add(fleur(560, 760, 1.0), fleur(620, 780, 0.9, "#ffd43b"), fleur(710, 770, 1.1, "#cc5de8"))
    return S


def p02():
    S = Scene()
    interieur(S, "#f3d9fa", "#c9a27e", 600, papier="#e599f7")
    S.add(fenetre(90, 120, 170, 170, "#a5d8ff", rideaux="#e64980",
                  contenu=sapin(170, 300, 0.5) + sapin(230, 300, 0.4)))
    S.add(roi(470, 760, 1.55, expr="surpris", bras="ouverts"))
    S.add(personne(180, 770, 1.3, expr="surpris", **ROSE_P))
    S.add(bulle(560, 150, 380, 100, "Un DRAGON !", 54, pointe=(500, 370)))
    return S


def p03():
    S = Scene()
    jardin_chateau(S, "#a5d8ff", "#e7f5ff", chateau_s=0.7, chateau_x=400)
    for k, (x, pl) in enumerate([(170, "#fa5252"), (400, "#4dabf7"), (630, "#fab005")]):
        S.add(chevalier(x, 770, 1.35, plumet=pl, expr="oups" if k != 1 else "inquiet", bras="joues"))
        S.add(mouvement(x - 90, 600, 0.9), mouvement(x + 130, 620, 0.9, rot=180))
    S.add(texte(400, 150, "Gling, gling, gling !", 58, "#495057", contour="#fff"))
    return S


def p04():
    S = Scene()
    foret(S)
    S.add(personne(420, 760, 1.5, expr="concentre", bras="tient", regard=(1, 0),
                   objet=panier(68, -146, 0.8), **ROSE_P))
    S.add(pensee(640, 190, 110, texte(640, 225, "?", 110, "#e64980"), depuis=(470, 480)))
    S.add(champignon(120, 770, 0.8), champignon(720, 780, 0.6, "#ffd43b"))
    return S


def p05():
    S = Scene()
    foret(S, sombre=True)
    S.add(rocher(420, 760, 1.4))
    S.add(chemin("M 600 740 Q 690 740 710 690 Q 724 654 752 646", stroke="#69db7c", sw=26))
    S.add(poly([(742, 640), (790, 620), (776, 666)], "#37b24d"))
    for gx, gy in [(330, 470), (380, 420), (450, 450)]:
        S.add(goutte(gx, gy, 1.4, "#74c0fc"))
    S.add(texte(400, 220, "Snif… snif…", 64, "#1c7ed6", contour="#fff"))
    S.add(personne(120, 780, 1.1, expr="surpris", regard=(1, 0), **ROSE_P))
    return S


def p06():
    S = Scene()
    foret(S, sombre=True)
    S.add(rocher(640, 760, 1.0))
    S.add(personne(220, 770, 1.45, expr="surpris", bras="joues", regard=(1, 0), **ROSE_P))
    S.add(dragon(520, 770, 1.4, expr="pleure", larmes=True, bras="yeux", **PISTACHE))
    return S


def p07():
    S = Scene()
    foret(S)
    S.add(personne(230, 770, 1.4, expr="sourire", bras="large", regard=(1, 0), **ROSE_P))
    S.add(dragon(540, 770, 1.35, expr="triste", bras="bas", regard=(-1, 0), **PISTACHE))
    S.add(bulle(540, 160, 400, 110, "J'ai perdu\nma maman…", 42, pointe=(540, 420)))
    return S


def p08():
    S = Scene()
    foret(S)
    S.add(panier(120, 780, 1.0))
    S.add(personne(270, 770, 1.45, expr="content", bras="donne", regard=(1, 0), **ROSE_P))
    S.add(pomme(395, 632, 1.4))
    S.add(dragon(560, 770, 1.35, expr="content", bras="porte", **PISTACHE))
    S.add(coeur(420, 360, 1.6), coeur(480, 300, 1.0, "#ff8787"))
    return S


def p09():
    S = Scene()
    foret(S)
    S.add(personne(190, 770, 1.4, expr="rire", bras="joues", regard=(1, 0), **ROSE_P))
    S.add(dragon(520, 770, 1.35, expr="souffle", bras="hanches", **PISTACHE))
    S.add(bulles_savon(470, 380, 1.6, graine=7, nb=12, r=110))
    S.add(texte(560, 150, "Atchoum !", 70, "#2b8a3e", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(dragon_vol(420, 250, 1.0, flip=False, **MAMAN))
    for x, s in [(60, 1.4), (240, 1.0), (560, 1.1), (760, 1.3)]:
        S.add(sapin(x, 640, s, "#2b8a3e", "#2f9e44"))
    sol(S, 630, "#69db7c")
    S.add(chevalier(170, 780, 1.1, plumet="#fa5252", expr="oups", bras="haut"))
    S.add(chevalier(320, 780, 1.1, plumet="#4dabf7", expr="bouche_bee", bras="joues"))
    S.add(personne(520, 780, 1.1, expr="surpris", regard=(0, -1), **ROSE_P))
    S.add(dragon(660, 780, 1.0, expr="joie", bras="haut", regard=(0, -1), **PISTACHE))
    return S


def p11():
    S = Scene()
    foret(S)
    S.add(dragon(470, 780, 2.1, expr="content", bras="calin", ailes="ouvertes", **MAMAN))
    S.add(dragon(470, 720, 0.85, expr="rire", bras="haut", **PISTACHE))
    S.add(personne(150, 780, 1.3, expr="content", bras="salut", regard=(1, 0), **ROSE_P))
    S.add(coeur(620, 170, 1.4), coeur(680, 230, 1.0, "#ff8787"))
    return S


def p12():
    S = Scene()
    jardin_chateau(S, "#ffdeeb", "#fff0f6", chateau_s=0.7, chateau_x=420)
    S.add(personne(230, 770, 1.35, expr="rire", bras="haut", **ROSE_P))
    S.add(dragon(470, 770, 1.3, expr="rire", bras="haut", **PISTACHE))
    S.add(chevalier(680, 780, 1.1, plumet="#fab005", expr="rire", bras="joues"))
    S.add(bulles_savon(420, 330, 1.7, graine=11, nb=14, r=120))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pistache-seul.svg", vignette),
    ("01-le-chateau.svg", p01), ("02-un-dragon.svg", p02), ("03-chevaliers.svg", p03),
    ("04-la-foret.svg", p04), ("05-snif.svg", p05), ("06-petit-dragon.svg", p06),
    ("07-perdu.svg", p07), ("08-la-pomme.svg", p08), ("09-atchoum.svg", p09),
    ("10-grande-ombre.svg", p10), ("11-maman.svg", p11), ("12-amis.svg", p12),
]
