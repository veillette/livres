"""Le Lion et le Moucheron — ne mépriser personne, ne se croire le plus fort de personne."""
from fables import *

ID = "lion-moucheron"


def lion(x, y, s=1.0, **k):
    return perso("lion", x, y, s, **k)


def savane(S, soir=False):
    ciel(S, "#ffa94d" if soir else "#ffd8a8", "#fff4e6")
    S.add(soleil(660, 130, 55, "#ff922b" if soir else "#ffa94d"))
    collines(S, 600, "#ffe066", graine=81)
    sol(S, 620, "#fcc419", couleur2="#fab005", y2=720)
    for hx in (40, 330, 560, 760):
        S.add(herbe(hx, 700 + (hx % 7) * 6, 1.3, "#e0a93a"))


def poussiere(x, y, s=1.0, graine=1):
    rr = random.Random(graine)
    m = []
    for _ in range(12):
        m.append(cercle(rr.uniform(-160, 160), rr.uniform(-100, 40), rr.uniform(30, 60), "#e9d8a6", opacity=0.8))
    return place(m, x, y, s)


def buisson_toile(S):
    S.add(buisson(650, 720, 1.6, "#5c940d", "#74b816"))
    S.add(trait(470, 180, 470, 600, "#8d5524", 10), trait(470, 300, 560, 220, "#8d5524", 7))


def couverture():
    S = Scene()
    savane(S)
    S.add(lion(360, 790, 1.55, expr="furieux", bras="poing", regard=(1, -1)))
    S.add(moucheron(560, 420, 2.2, expr="malin", flip=True, trompette=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(moucheron(200, 140, 3.0, expr="rire", trompette=True))
    return S


def p01():
    S = Scene()
    savane(S)
    S.add(lion(400, 760, 2.0, expr="fier", bras="hanches"))
    S.add(perso("lievre", 110, 780, 0.8, expr="oups", bras="joues"))
    S.add(perso("rat", 700, 790, 0.7, expr="oups", bras="joues"))
    return S


def p02():
    S = Scene()
    savane(S)
    S.add(lion(360, 760, 1.9, expr="neutre", bras="bas", regard=(1, -1)))
    S.add(moucheron(580, 290, 2.4, expr="content", flip=True))
    S.add(chemin("M 700 420 q 30 -40 0 -80 q -30 -40 10 -80", stroke="#495057", sw=3, stroke_dasharray="4 10"))
    S.add(texte(640, 190, "Bzzz…", 44, "#495057", contour="#fff"))
    return S


def p03():
    S = Scene()
    savane(S)
    S.add(lion(360, 760, 1.9, expr="furieux", bras="montre", regard=(1, -1)))
    S.add(moucheron(640, 330, 2.2, expr="surpris", flip=True))
    S.add(bulle(330, 110, 520, 110, "Va-t'en, petit insecte !\nTu n'es qu'une poussière !", 32, pointe=(360, 340)))
    return S


def p04():
    S = Scene()
    savane(S)
    S.add(moucheron(400, 420, 5.0, expr="furieux", flip=True))
    S.add(bulle(400, 150, 480, 110, "Une poussière, moi ?\nC'est la guerre !", 38, pointe=(400, 320)))
    return S


def p05():
    S = Scene()
    savane(S)
    S.add(lion(250, 760, 1.6, expr="rire", bras="calin"))
    S.add(moucheron(580, 450, 3.0, expr="fache", flip=True))
    S.add(bulle(560, 150, 420, 130, "Je fais courir les bœufs,\nalors un lion, tu penses !", 30, pointe=(580, 390)))
    return S


def p06():
    S = Scene()
    savane(S)
    S.add(moucheron(470, 330, 3.6, expr="furieux", flip=True, trompette=True, rot=-12))
    S.add(mouvement(630, 390, 1.4), mouvement(650, 300, 1.1))
    S.add(texte(300, 560, "Ta-ta-ta-taaa !", 60, "#c46210", contour="#fff"))
    return S


def p07():
    S = Scene()
    savane(S)
    S.add(lion(400, 760, 1.9, expr="oups", bras="bas"))
    S.add(moucheron(400, 520, 1.4, expr="malin", flip=True, rot=30))
    S.add(eclat(410, 520, 1.1, "#ff6b6b"))
    S.add(texte(160, 330, "Aïe !", 60, "#c92a2a", contour="#fff"), texte(650, 300, "Aïe !", 50, "#c92a2a", contour="#fff"))
    return S


def p08():
    S = Scene()
    savane(S)
    S.add(lion(400, 760, 1.9, expr="furieux", bras="haut", rot=-10))
    S.add(moucheron(640, 300, 1.8, expr="rire", flip=True))
    S.add(chemin("M 150 400 Q 400 250 650 400", stroke="#495057", sw=4, stroke_dasharray="6 12"))
    S.add(texte(160, 250, "ROAR !", 64, "#c46210", contour="#fff"))
    return S


def p09():
    S = Scene()
    savane(S)
    S.add(poussiere(400, 620, 1.4, graine=2))
    S.add(lion(400, 760, 1.7, expr="furieux", bras="poing", rot=15))
    S.add(poussiere(380, 760, 1.2, graine=5))
    S.add(moucheron(640, 240, 1.6, expr="rire", flip=True))
    return S


def p10():
    S = Scene()
    savane(S, soir=True)
    S.add(lion(560, 740, 1.7, expr="triste", bras="bas", rot=-80))
    S.add(texte(400, 300, "Je me rends…", 50, "#c46210", contour="#fff"))
    S.add(moucheron(620, 440, 1.8, expr="fier", flip=True))
    return S


def p11():
    S = Scene()
    savane(S, soir=True)
    S.add(moucheron(400, 400, 5.0, expr="rire", trompette=True, rot=-10))
    S.add(texte(400, 150, "Victoire !", 72, "#c46210", contour="#fff"))
    S.add(paillettes(180, 300, 1.4), paillettes(620, 560, 1.4))
    return S


def p12():
    S = Scene()
    savane(S, soir=True)
    buisson_toile(S)
    S.add(chemin("M 60 600 C 160 300 300 700 380 400 S 500 200 440 300", stroke="#495057", sw=4, stroke_dasharray="6 12"))
    S.add(moucheron(300, 250, 2.0, expr="fier", trompette=True, rot=-10))
    S.add(bulle(220, 120, 380, 100, "Je suis le plus\nfort du monde !", 34, pointe=(290, 210)))
    return S


def p13():
    S = Scene()
    savane(S, soir=True)
    buisson_toile(S)
    S.add(toile(470, 300, 190))
    S.add(moucheron(500, 320, 2.4, expr="oups"))
    S.add(texte(250, 540, "Scrountch !", 56, "#495057", contour="#fff"))
    return S


def p14():
    S = Scene()
    savane(S, soir=True)
    buisson_toile(S)
    S.add(toile(470, 300, 190))
    S.add(moucheron(500, 320, 2.4, expr="inquiet", regard=(1, -1)))
    S.add(araignee_perso(620, 170, 1.6, expr="malin", fil=200, regard=(-1, 1)))
    S.add(bulle(220, 580, 390, 120, "Le plus fort du monde,\npris dans un fil ?", 32, pointe=(560, 230)))
    return S


def p15():
    S = Scene()
    savane(S, soir=True)
    buisson_toile(S)
    S.add(toile(470, 300, 190))
    S.add(araignee_perso(560, 200, 1.4, expr="content", fil=200))
    S.add(moucheron(260, 400, 2.4, expr="timide", flip=True))
    S.add(bulle(260, 180, 420, 100, "Merci… Je ne me\nvanterai plus !", 34, pointe=(270, 330)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("moucheron-seul.svg", vignette),
    ("01-le-roi.svg", p01), ("02-bzzz.svg", p02), ("03-va-t-en.svg", p03),
    ("04-c-est-la-guerre.svg", p04), ("05-je-fais-courir-les-boeufs.svg", p05), ("06-la-charge.svg", p06),
    ("07-aie.svg", p07), ("08-roar.svg", p08), ("09-la-poussiere.svg", p09),
    ("10-je-me-rends.svg", p10), ("11-victoire.svg", p11), ("12-le-plus-fort.svg", p12),
    ("13-la-toile.svg", p13), ("14-l-araignee.svg", p14), ("15-plus-de-vantardise.svg", p15),
]
