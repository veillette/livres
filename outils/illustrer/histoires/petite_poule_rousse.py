"""La petite poule rousse — qui n'aide pas ne partage pas."""
from contes import *

ID = "petite-poule-rousse"


def poule(x, y, s=1.2, **k):
    return poule_rousse(x, y, s, **k)


def chat(x, y, s=0.9, **k):
    return perso("chat", x, y, s, couleur="#868e96", **k)


def chien(x, y, s=0.95, **k):
    return perso("chien", x, y, s, **k)


def cane(x, y, s=0.9, **k):
    return canard(x, y, s, nage=False, couleur="#f8f9fa", **k)


def ferme(S, soleil_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    if soleil_:
        S.add(soleil(690, 100, 42))
    S.add(nuage(170, 110, 0.6))
    collines(S, 580, "#b2f2bb", graine=14)
    sol(S, 580, "#94d82d")
    S.add(maison(140, 590, 0.6, mur="#ffc9c9", toit="#c92a2a", porte="#6d4424"))
    S.add(barriere(560, 600, 0.6, largeur=520))


def trio(S, expr="neutre", y=790, dort=False, pos=(420, 560, 700)):
    e = "dort" if dort else expr
    S.add(chat(pos[0], y, expr=e, bras="croises" if not dort else "bas"), chien(pos[1], y, expr=e, bras="croises" if not dort else "bas", tache=True),
          cane(pos[2], y - 40, expr=e, flip=True))


def pas_moi(S):
    S.add(texte(420, 470, "Pas moi !", 36, "#495057", contour="#fff"), texte(560, 440, "Pas moi !", 36, "#495057", contour="#fff"),
          texte(700, 480, "Pas moi !", 36, "#495057", contour="#fff"))


def moi(S):
    S.add(texte(420, 470, "Moi !", 50, "#e8590c", contour="#fff"), texte(560, 440, "Moi !", 50, "#e8590c", contour="#fff"),
          texte(700, 480, "Moi !", 50, "#e8590c", contour="#fff"))


def faucille(x, y, s=1.0, rot=0):
    return place([rect(-6, 0, 12, 60, "#a0522d", rx=4), chemin("M 0 0 Q -10 -80 70 -90 Q 20 -60 10 0 Z", "#adb5bd")], x, y, s, rot=rot)


def cuisine(S):
    interieur(S, "#fff9db", "#d9a066", 580, papier="#ffec99")
    S.add(fenetre(80, 120, 150, 140, dehors="#b2f2bb", rideaux="#fa5252"))


def couverture():
    S = Scene()
    ferme(S)
    for k in range(6):
        S.add(ble(560 + k * 40, 700, 0.9))
    S.add(poule(320, 790, 1.8, expr="fier"))
    S.add(pain(600, 790, 1.4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(poule(200, 262, 1.3, expr="content"))
    return S


def p01():
    S = Scene()
    ferme(S)
    S.add(poule(190, 790, 1.4, expr="content", ailes="haut"))
    trio(S, "content")
    return S


def p02():
    S = Scene()
    ferme(S)
    S.add(poule(190, 790, 1.4, expr="sourire", bec_ouvert=True))
    S.add(g([grain(300, 780), grain(330, 790), grain(315, 760)]))
    trio(S)
    pas_moi(S)
    S.add(bulle(260, 150, 440, 100, "Qui veut m'aider\nà planter ce blé ?", 34, pointe=(200, 560)))
    return S


def p03():
    S = Scene()
    ferme(S)
    champ_laboure(S, 640)
    S.add(poule(400, 760, 1.4, expr="concentre"))
    S.add(g([grain(250, 700), grain(560, 700), grain(620, 720), grain(180, 720)]))
    S.add(texte(400, 200, "Toute seule !", 60, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    ferme(S, soleil_=True)
    for k in range(14):
        S.add(ble(20 + k * 58, 650 + (k % 2) * 20, 1.1))
    S.add(poule(190, 790, 1.3, expr="sourire", bec_ouvert=True))
    trio(S)
    pas_moi(S)
    S.add(bulle(300, 150, 420, 100, "Qui veut m'aider\nà couper le blé ?", 34, pointe=(200, 570)))
    return S


def p05():
    S = Scene()
    ferme(S)
    for k in range(6):
        S.add(ble(420 + k * 60, 680 + (k % 2) * 20, 1.1))
    for k in range(4):
        S.add(place(ble(0, 0, 1.0), 120 + k * 30, 780, rot=80))
    S.add(poule(300, 780, 1.3, expr="concentre"), faucille(390, 640, 0.8, rot=30))
    return S


def p06():
    S = Scene()
    ferme(S)
    S.add(sac(200, 790, 1.2, ecrit="blé"))
    S.add(poule(330, 790, 1.2, expr="fache"))
    trio(S, dort=True, pos=(460, 590, 720))
    S.add(zzz(600, 480, 1.0))
    return S


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=4)
    sol(S, 600, "#94d82d")
    S.add(moulin(560, 640, 1.1))
    S.add(chemin("M 0 760 Q 400 660 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(poule(250, 780, 1.3, expr="concentre"), sac(360, 780, 0.9, ecrit="blé"))
    S.add(sac(700, 790, 0.9, "#f8f9fa", ecrit="farine"))
    return S


def p08():
    S = Scene()
    cuisine(S)
    S.add(sac(640, 330, 0.7, "#f8f9fa", ecrit="farine"))
    S.add(table(400, 600, 300, 60, nappe="#ffc9c9"))
    S.add(poule(180, 790, 1.2, expr="sourire", bec_ouvert=True))
    trio(S, pos=(400, 540, 700))
    pas_moi(S)
    S.add(bulle(320, 130, 420, 100, "Qui veut m'aider\nà faire du pain ?", 34, pointe=(200, 560)))
    return S


def p09():
    S = Scene()
    cuisine(S)
    S.add(four(560, 790, 1.2, gateau_dedans=False))
    S.add(pain(560, 610, 0.9))
    S.add(poule(250, 790, 1.4, expr="content", ailes="haut"))
    S.add(chemin("M 520 480 q -16 -30 0 -60 q 16 -30 0 -60", stroke="#dee2e6", sw=10, opacity=0.8))
    S.add(texte(250, 200, "Mmm !", 70, "#e8590c", contour="#fff"))
    return S


def p10():
    S = Scene()
    cuisine(S)
    S.add(table(270, 700, 240, 100, nappe="#fff"))
    S.add(pain(270, 590, 1.0))
    S.add(poule(130, 800, 1.1, expr="malin", bec_ouvert=True))
    trio(S, "rire", pos=(430, 570, 710))
    moi(S)
    S.add(bulle(360, 130, 460, 100, "Qui veut m'aider\nà manger ce pain ?", 34, pointe=(140, 580)))
    return S


def p11():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 360, 110, nappe="#fff"))
    S.add(pain(400, 660, 1.2))
    S.add(poule(250, 800, 1.2, expr="fache", ailes="haut"))
    for k, x in enumerate((500, 570, 640)):
        S.add(poussin(x, 800, 0.5, expr="miam"))
    S.add(bulle(400, 150, 520, 110, "Vous ne m'avez pas aidée.\nJe le mange avec mes poussins !", 30, pointe=(260, 560)))
    return S


def p12():
    S = Scene()
    ferme(S)
    trio(S, "triste", pos=(220, 400, 620))
    S.add(bulle(420, 180, 520, 100, "Pardon… La prochaine fois,\non t'aidera !", 32, pointe=(400, 540)))
    return S


def p13():
    S = Scene()
    ferme(S)
    S.add(table(400, 790, 420, 110, nappe="#fff"))
    S.add(pain(340, 660, 1.0), pain(470, 660, 1.0))
    S.add(poule(400, 800, 1.0, expr="rire", ailes="haut"))
    S.add(chat(110, 790, 0.9, expr="miam"), chien(700, 790, 0.9, expr="miam"), cane(230, 740, 0.8, expr="miam"))
    for k, x in enumerate((540, 600)):
        S.add(poussin(x, 800, 0.45, expr="rire"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("poule-seule.svg", vignette),
    ("01-la-ferme.svg", p01), ("02-planter.svg", p02), ("03-toute-seule.svg", p03), ("04-couper.svg", p04),
    ("05-la-moisson.svg", p05), ("06-la-sieste.svg", p06), ("07-le-moulin.svg", p07), ("08-le-pain.svg", p08),
    ("09-mmm.svg", p09), ("10-moi.svg", p10), ("11-mes-poussins.svg", p11), ("12-pardon.svg", p12),
    ("13-tous-ensemble.svg", p13),
]
