"""Marina et la perle perdue — oser demander de l'aide."""
from base import *
from objets import *
from fantastique import *

ID = "sirene-perle"
MARINA = dict(coiffure="tres_longs", cheveux="roux", peau="claire", habit="#20c997",
              sirene=("#20c997", "#96f2d7"))
MAMIE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#9775fa",
             sirene=("#9775fa", "#d0bfff"), acc=("lunettes", "couronne"))


def marina(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MARINA, **k})


def fond(S, sombre=False):
    if sombre:
        ocean(S, "#1864ab", "#0b2f5a", "#d9b56a", rayons=False)
    else:
        ocean(S)
    S.add(algue(70, 720, 1.1, graine=1), algue(740, 730, 1.0, "#2f9e44", graine=2))
    S.add(corail(640, 740, 0.8, "#ff8787"), coquillage(160, 760, 0.7))
    S.add(bulles_eau(700, 400, 1.0, graine=3), bulles_eau(110, 300, 0.8, graine=5))


def pierre(x, y, s=1.0, trou=False):
    m = [chemin("M -90 0 Q -100 -70 -30 -90 Q 50 -110 90 -50 Q 110 -10 96 0 Z", "#868e96")]
    if trou:
        m.append(ellipse(0, -36, 30, 22, "#343a40"))
    return place(m, x, y, s)


def grotte(x, y, s=1.0):
    m = [chemin("M -260 0 Q -280 -300 0 -320 Q 280 -300 260 0 Z", "#495057"),
         chemin("M -150 0 Q -160 -200 0 -210 Q 160 -200 150 0 Z", "#1a1b2e")]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    fond(S)
    S.add(palais_coquillage(560, 680, 0.6))
    S.add(marina(330, 560, 1.7, expr="rire", bras="porte", objet=perle(0, -80, 1.0)))
    S.add(poisson(640, 300, 0.9, "#ffd43b", flip=True), poisson(120, 460, 0.7, "#ff922b"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 150, 150, 110, "#d0ebff"))
    S.add(bulles_eau(90, 200, 0.7, graine=4), bulles_eau(320, 180, 0.6, graine=8))
    S.add(perle(200, 140, 2.2))
    S.add(coquillage(200, 262, 1.0, "#fcc2d7"))
    return S


def p01():
    S = Scene()
    fond(S)
    S.add(palais_coquillage(400, 690, 1.0))
    S.add(marina(560, 440, 1.3, expr="content", bras="salut"))
    S.add(poisson(200, 250, 0.8, "#ffd43b"), poisson(260, 330, 0.6, "#ff922b"))
    return S


def p02():
    S = Scene()
    fond(S)
    S.add(personne(520, 560, 1.6, expr="sourire", bras="donne2", flip=True, **MAMIE))
    S.add(marina(240, 570, 1.4, expr="bouche_bee", bras="porte", objet=perle(0, -80, 0.9)))
    S.add(bulle(420, 130, 460, 100, "Prends-en bien soin,\nma chérie.", 36, pointe=(480, 250)))
    return S


def p03():
    S = Scene()
    fond(S)
    S.add(marina(200, 560, 1.4, expr="rire", bras="haut"))
    for k, (px, py) in enumerate([(300, 240), (420, 180), (520, 300), (610, 420)]):
        S.add(perle(px, py, 0.5 + k * 0.05, brille=False))
        S.add(cercle(px, py, 30, "none", stroke="#fff", stroke_width=2, opacity=0.3))
    S.add(perle(700, 560, 0.8))
    S.add(algue(700, 760, 1.4, "#37b24d", graine=9))
    S.add(texte(560, 120, "Boing ! Boing !", 52, "#fff", contour="#1971c2"))
    return S


def p04():
    S = Scene()
    fond(S)
    S.add(pierre(560, 740, 1.3), pierre(260, 760, 0.9))
    S.add(marina(420, 540, 1.4, expr="concentre", bras="large", regard=(1, 1)))
    S.add(bulle(420, 110, 480, 100, "Je vais me débrouiller\ntoute seule !", 34, pointe=(420, 240)))
    return S


def p05():
    S = Scene()
    fond(S, sombre=True)
    S.add(pierre(620, 760, 1.0))
    S.add(marina(400, 600, 1.5, expr="pleure", larmes=True, bras="yeux"))
    return S


def p06():
    S = Scene()
    fond(S)
    S.add(tortue(560, 700, 1.7, flip=True, regard=(-1, 0)))
    S.add(marina(220, 560, 1.4, expr="triste", bras="bas", regard=(1, 0)))
    S.add(bulle(560, 150, 440, 110, "Qu'est-ce qui\nne va pas, Marina ?", 36, pointe=(620, 460)))
    return S


def p07():
    S = Scene()
    fond(S)
    S.add(tortue(560, 700, 1.5, flip=True, regard=(-1, 0), expr="rire"))
    S.add(marina(230, 560, 1.4, expr="sourire", bras="calin", regard=(1, 0)))
    S.add(poulpe(700, 330, 0.55), crabe(400, 780, 0.6), poisson(100, 200, 0.6, "#ffd43b"))
    S.add(bulle(520, 130, 440, 100, "Je vais t'aider !", 42, pointe=(620, 500)))
    return S


def p08():
    S = Scene()
    fond(S)
    for x, y in [(130, 770), (330, 780), (560, 780), (720, 760)]:
        S.add(pierre(x, y, 0.9, trou=True))
    S.add(poulpe(420, 600, 1.4, "#f783ac", expr="concentre", regard=(0, 1)))
    S.add(texte(400, 130, "Huit bras, huit trous !", 50, "#fff", contour="#c2255c"))
    return S


def p09():
    S = Scene()
    fond(S)
    S.add(algue(250, 780, 1.8, "#40c057", graine=5), algue(420, 790, 2.0, "#2f9e44", graine=6), algue(590, 780, 1.7, "#51cf66", graine=7))
    for k in range(6):
        S.add(poisson(120 + k * 110, 300 + (k % 2) * 30, 0.6, ["#ff922b", "#ffd43b", "#ff6b6b"][k % 3], expr="concentre" if k % 2 else "sourire"))
    return S


def p10():
    S = Scene()
    fond(S)
    for x, c in [(200, "#ffc9d6"), (340, "#ffe8cc"), (620, "#d0ebff")]:
        S.add(coquillage(x, 780, 1.1, c))
    S.add(crabe(470, 720, 1.4, expr="concentre"))
    S.add(coquillage(470, 520, 1.0, "#fff3bf", rot=20))
    S.add(bulle(420, 160, 420, 90, "Pas ici… pas ici…", 38, pointe=(460, 430)))
    return S


def p11():
    S = Scene()
    fond(S, sombre=True)
    S.add(grotte(400, 780, 1.3))
    S.add(perle(400, 660, 1.4))
    S.add(marina(160, 560, 1.1, expr="bouche_bee", bras="haut"))
    S.add(tortue(680, 730, 0.8, flip=True, expr="rire"), poulpe(640, 360, 0.5, expr="rire"), crabe(320, 790, 0.5, expr="rire"))
    S.add(texte(400, 120, "La perle !", 64, "#fff3bf", contour="#1864ab"))
    return S


def p12():
    S = Scene()
    fond(S)
    S.add(palais_coquillage(400, 690, 0.8))
    S.add(personne(470, 570, 1.5, expr="content", bras="calin", **MAMIE))
    S.add(marina(330, 580, 1.2, expr="content", bras="porte", objet=perle(0, -80, 0.9)))
    S.add(coeur(420, 160, 1.6), coeur(480, 110, 1.0, "#ff8787"))
    S.add(tortue(700, 760, 0.6, flip=True), poisson(100, 180, 0.6, "#ffd43b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("perle-seule.svg", vignette),
    ("01-le-palais.svg", p01), ("02-la-perle.svg", p02), ("03-boing.svg", p03),
    ("04-toute-seule.svg", p04), ("05-fatiguee.svg", p05), ("06-tortue.svg", p06),
    ("07-je-vais-t-aider.svg", p07), ("08-poulpe.svg", p08), ("09-poissons.svg", p09),
    ("10-crabe.svg", p10), ("11-la-grotte.svg", p11), ("12-ensemble.svg", p12),
]
