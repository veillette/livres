"""L'énorme navet — même le plus petit peut faire la différence."""
from contes import *

ID = "enorme-navet"
PAPI = dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="rosee", habit="#1c7ed6", robe=False, jambes="#495057")
MAMIE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#e64980", acc=("lunettes",))
FILLE = dict(coiffure="tresses", cheveux="blond", peau="claire", habit="#fcc419")


def papi(x, y, s=1.1, **k):
    return personne(x, y, s, **{**PAPI, **k})


def mamie(x, y, s=1.05, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def fille(x, y, s=0.85, **k):
    return personne(x, y, s, **{**FILLE, **k})


def chien(x, y, s=0.75, **k):
    return perso("chien", x, y, s, tache=True, **k)


def chat(x, y, s=0.6, **k):
    return perso("chat", x, y, s, **k)


def souris(x, y, s=0.32, **k):
    return perso("souris", x, y, s, **k)


CHAINE = [(papi, 470), (mamie, 360), (fille, 260), (chien, 180), (chat, 110), (souris, 55)]


def potager(S, soleil_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    if soleil_:
        S.add(soleil(690, 100, 40))
    S.add(nuage(170, 110, 0.6))
    collines(S, 560, "#b2f2bb", graine=6)
    sol(S, 560, "#94d82d")
    S.add(rect(0, 640, 800, 160, "#a0693a"))
    for k in range(4):
        S.add(chemin(f"M 0 {670 + k * 36} Q 400 {660 + k * 36} 800 {670 + k * 36}", stroke="#7c4a1e", sw=4))


def chaine(S, nb, expr="concentre", y=790):
    for k in range(nb):
        fn, x = CHAINE[k]
        S.add(fn(x, y, expr=expr, bras="tire"))


def couverture():
    S = Scene()
    potager(S)
    S.add(navet(610, 700, 1.15, visible=0.75))
    chaine(S, 6, "concentre")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(navet(200, 215, 0.45, visible=1.0))
    return S


def p01():
    S = Scene()
    potager(S)
    S.add(navet(560, 700, 0.3, visible=0.25))
    S.add(papi(330, 790, 1.4, expr="content", bras="donne"))
    S.add(bulle(420, 170, 500, 110, "Pousse, pousse,\nmon petit navet !", 36, pointe=(360, 460)))
    return S


def p02():
    S = Scene()
    potager(S)
    S.add(navet(420, 700, 1.3, visible=0.6))
    S.add(papi(130, 790, 1.1, expr="bouche_bee", bras="joues"))
    S.add(texte(420, 140, "Il est énorme !", 60, "#862e9c", contour="#fff"))
    return S


def p03():
    S = Scene()
    potager(S)
    S.add(navet(610, 700, 1.15, visible=0.6))
    chaine(S, 1)
    S.add(texte(300, 200, "Hop ! Hop !", 56, "#1c7ed6", contour="#fff"))
    return S


def appel(S, nb, qui, texte_bulle, px, py):
    potager(S)
    S.add(navet(610, 700, 1.15, visible=0.6))
    chaine(S, nb)
    S.add(bulle(360, 150, 460, 100, texte_bulle, 34, pointe=(px, py)))


def p04():
    S = Scene()
    appel(S, 2, "mamie", "Mamie, viens m'aider !", 480, 520)
    return S


def p05():
    S = Scene()
    appel(S, 3, "fille", "Viens nous aider,\nma chérie !", 360, 540)
    return S


def p06():
    S = Scene()
    appel(S, 4, "chien", "Le chien, viens\nnous aider !", 260, 600)
    return S


def p07():
    S = Scene()
    appel(S, 5, "chat", "Le chat, viens\nnous aider !", 180, 640)
    return S


def p08():
    S = Scene()
    potager(S)
    S.add(navet(610, 700, 1.15, visible=0.6))
    chaine(S, 5, "inquiet")
    S.add(souris(55, 790, 0.4, expr="fier", bras="hanches"))
    S.add(bulle(330, 150, 460, 100, "Toi ? Tu es bien\ntrop petite !", 34, pointe=(180, 620)))
    return S


def p09():
    S = Scene()
    potager(S)
    S.add(navet(610, 700, 1.15, visible=0.7))
    chaine(S, 6, "concentre")
    S.add(texte(330, 170, "Ils tirent, ils tirent…", 50, "#1c7ed6", contour="#fff"))
    return S


def p10():
    S = Scene()
    potager(S)
    S.add(place(navet(0, 0, 1.0, visible=1.0), 600, 520, rot=30))
    S.add(texte(420, 140, "POP !", 100, "#862e9c", contour="#fff", rot=-6))
    for k, (fn, x) in enumerate(CHAINE):
        S.add(fn(x - 20, 780 - (k % 2) * 30, expr="rire" if k % 2 else "surpris", bras="haut", rot=-25 - k * 4))
    return S


def p11():
    S = Scene()
    potager(S)
    S.add(navet(650, 790, 0.7, visible=1.0))
    S.add(papi(150, 790, 1.1, expr="rire", bras="haut"), mamie(290, 790, 1.0, expr="rire", bras="joues"), fille(410, 790, 0.9, expr="rire", bras="haut"))
    S.add(chien(510, 790, 0.7, expr="rire", bras="haut"), chat(580, 800, 0.55, expr="rire"))
    S.add(souris(650, 585, 0.5, expr="fier", bras="haut"))
    S.add(texte(400, 160, "Bravo, la souris !", 56, "#e64980", contour="#fff"))
    return S


def p12():
    S = Scene()
    interieur(S, "#fff4e6", "#d9a066", 580, papier="#ffe8cc")
    S.add(fenetre(560, 100, 170, 150, nuit_=True, dehors="#364fc7"))
    S.add(table(400, 790, 520, 140, nappe="#fff"))
    S.add(chaudron(400, 620, 0.55, contenu="#fff3bf", feu=False))
    S.add(souris(400, 470, 0.4, expr="miam", bras="bouche"))
    S.add(papi(110, 790, 1.0, expr="rire"), mamie(690, 790, 1.0, expr="rire", bras="ouverts"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("navet-seul.svg", vignette),
    ("01-pousse.svg", p01), ("02-enorme.svg", p02), ("03-papi-tire.svg", p03), ("04-mamie.svg", p04),
    ("05-la-petite-fille.svg", p05), ("06-le-chien.svg", p06), ("07-le-chat.svg", p07), ("08-la-souris.svg", p08),
    ("09-ils-tirent.svg", p09), ("10-pop.svg", p10), ("11-bravo.svg", p11), ("12-la-soupe.svg", p12),
]
