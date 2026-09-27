"""Le Lion et le Rat — on a souvent besoin d'un plus petit que soi."""
from fables import *

ID = "lion-rat"


def lion(x, y, s=1.0, **k):
    return perso("lion", x, y, s, **k)


def rat(x, y, s=1.0, **k):
    return perso("rat", x, y, s, **k)


def acacia(x, y, s=1.0):
    m = [chemin("M -14 0 Q -6 -90 -30 -160 L -14 -164 Q 6 -110 8 -60 Q 20 -120 50 -170 L 64 -164 Q 30 -100 14 0 Z", "#8d5524"),
         ellipse(-40, -180, 130, 34, "#5c940d"), ellipse(40, -196, 120, 30, "#74b816"), ellipse(-10, -210, 90, 26, "#82c91e")]
    return place(m, x, y, s)


def savane(S, ciel_haut="#ffd8a8", ciel_bas="#fff4e6", soleil_=True):
    ciel(S, ciel_haut, ciel_bas)
    if soleil_:
        S.add(soleil(660, 130, 55, "#ffa94d"))
    collines(S, 600, "#ffe066", graine=3)
    sol(S, 620, "#fcc419", couleur2="#fab005", y2=720)
    for hx in (40, 330, 560, 760):
        S.add(herbe(hx, 700 + (hx % 7) * 6, 1.3, "#e0a93a"))


def foret_filet(S):
    ciel(S, "#b2f2bb", "#e6fcf5")
    for tx, s_ in ((80, 1.4), (720, 1.3), (400, 1.0)):
        S.add(arbre(tx, 620, s_, feuillage="#2f9e44", feuillage2="#37b24d"))
    sol(S, 620, "#69db7c")
    S.add(buisson(200, 660, 0.8), buisson(600, 670, 0.9))


def filet_dome(cx, base, w=300, h=330, couleur="#a0522d", trou=False):
    """Filet refermé sur le sol, en forme de cloche."""
    cid = uid("f")
    forme = f"M {cx - w / 2} {base} Q {cx - w / 2 - 20} {base - h} {cx} {base - h} Q {cx + w / 2 + 20} {base - h} {cx + w / 2} {base} Z"
    lignes = []
    for k in range(-14, 16):
        x0 = cx - w / 2 + k * 36
        lignes.append(trait(x0, base - h - 10, x0 + h + 20, base + 10, couleur, 4))
        lignes.append(trait(x0, base - h - 10, x0 - h - 20, base + 10, couleur, 4))
    m = [el("clipPath", chemin(forme, "#000"), id=cid)]
    contenu = g(lignes, clip_path=f"url(#{cid})")
    if trou:
        mid = uid("k")
        m.append(el("mask", rect(0, 0, 800, 800, "#fff") + ellipse(trou[0], trou[1], trou[2], trou[3], "#000"), id=mid))
        contenu = g(contenu, mask=f"url(#{mid})")
    m.append(contenu)
    m.append(chemin(forme, stroke=couleur, sw=6))
    m.append(trait(cx, base - h, cx, 0, couleur, 5))
    return g(m)


def couverture():
    S = Scene()
    savane(S)
    S.add(acacia(620, 640, 1.2))
    S.add(lion(390, 800, 1.55, expr="content", bras="porte", objet=None))
    S.add(rat(390, 800 - 205 * 1.55 + 4, 0.58, expr="rire", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rat(200, 250, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    savane(S)
    S.add(acacia(440, 640, 1.9))
    S.add(lion(380, 760, 1.8, expr="dort", bras="calin"))
    S.add(zzz(560, 380, 1.2))
    return S


def p02():
    S = Scene()
    savane(S)
    S.add(acacia(440, 640, 1.9))
    S.add(lion(380, 760, 1.8, expr="dort", bras="calin"))
    S.add(rat(380, 530, 0.55, expr="rire", bras="haut"))
    S.add(mouvement(310, 500, 0.8))
    return S


def p03():
    S = Scene()
    savane(S)
    S.add(acacia(440, 640, 1.9))
    S.add(lion(380, 760, 1.8, expr="furieux", bras="hanches", regard=(0, -1)))
    S.add(rat(380, 500, 0.5, expr="oups", bras="joues"))
    S.add(texte(620, 300, "GRRR !", 70, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    savane(S)
    S.add(acacia(160, 640, 1.4))
    S.add(lion(380, 760, 1.8, expr="fache", bras="tient", regard=(1, -1)))
    rx, ry = 380 + 68 * 1.8, 760 - 146 * 1.8
    S.add(trait(rx, ry, rx + 6, ry + 60, "#ffa8a8", 6))
    S.add(rat(rx + 6, ry + 64, 0.7, expr="oups", bras="haut", rot=180))
    return S


def p05():
    S = Scene()
    savane(S)
    S.add(lion(560, 760, 1.6, expr="fache", bras="croises", regard=(-1, 0)))
    S.add(rat(220, 760, 1.0, expr="triste", bras="calin", regard=(1, -1)))
    S.add(bulle(250, 150, 420, 110, "Pardon, Majesté !\nUn jour, je vous aiderai !", 30, pointe=(230, 540)))
    return S


def p06():
    S = Scene()
    savane(S)
    S.add(acacia(620, 640, 1.2))
    S.add(lion(400, 760, 1.9, expr="rire", bras="calin"))
    S.add(rat(160, 760, 0.8, expr="timide"))
    S.add(texte(400, 200, "Ha ha ha !", 72, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    savane(S)
    S.add(lion(300, 760, 1.7, expr="content", bras="donne", regard=(1, 0)))
    S.add(rat(600, 760, 0.9, expr="rire", bras="salut", flip=True))
    S.add(mouvement(500, 700, 1.0))
    S.add(bulle(600, 180, 280, 90, "Merci !", 48, pointe=(600, 560)))
    return S


def p08():
    S = Scene()
    foret_filet(S)
    S.add(trait(400, 0, 400, 90, "#a0522d", 5))
    S.add(filet(260, 90, 280, 120, "#a0522d"))
    S.add(lion(400, 760, 1.6, expr="content", bras="bas", regard=(1, 0)))
    S.add(texte(620, 200, "?", 60, "#c92a2a"))
    return S


def p09():
    S = Scene()
    foret_filet(S)
    S.add(lion(400, 760, 1.6, expr="surpris", bras="haut"))
    S.add(filet_dome(400, 780, 440, 520))
    S.add(texte(160, 220, "CRAC !", 70, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    foret_filet(S)
    S.add(lion(400, 760, 1.6, expr="furieux", bras="poing", rot=8))
    S.add(filet_dome(400, 780, 440, 520))
    S.add(mouvement(130, 500, 1.0, rot=180), mouvement(670, 500, 1.0))
    return S


def p11():
    S = Scene()
    foret_filet(S)
    S.add(lion(400, 760, 1.6, expr="furieux", bras="bas"))
    S.add(filet_dome(400, 780, 440, 520))
    S.add(ondes(460, 520, r0=80, nb=3, ecart=40, direction=-60, ouverture=100, couleur="#e8590c"))
    S.add(texte(560, 150, "ROAAAR !", 80, "#e8590c", contour="#fff"))
    return S


def p12():
    S = Scene()
    foret_filet(S)
    S.add(rat(420, 760, 1.4, expr="fier", bras="course", rot=-10))
    S.add(mouvement(260, 620, 1.2))
    S.add(bulle(420, 180, 420, 100, "J'arrive, Majesté !", 38, pointe=(420, 440)))
    return S


def p13():
    S = Scene()
    foret_filet(S)
    S.add(lion(470, 760, 1.6, expr="inquiet", bras="bas", regard=(-1, 1)))
    S.add(filet_dome(470, 780, 440, 520))
    S.add(rat(250, 780, 0.9, expr="concentre", bras="porte"))
    S.add(texte(160, 480, "Cric !", 44, "#7c4a1e", contour="#fff"), texte(240, 420, "crac !", 44, "#7c4a1e", contour="#fff"))
    return S


def p14():
    S = Scene()
    foret_filet(S)
    S.add(filet_dome(560, 780, 360, 380, trou=(400, 640, 150, 170)))
    S.add(lion(330, 760, 1.6, expr="rire", bras="haut"))
    S.add(rat(160, 770, 0.8, expr="rire", bras="haut"))
    S.add(paillettes(330, 240, 1.3))
    return S


def p15():
    S = Scene()
    savane(S, ciel_haut="#ffa94d", ciel_bas="#ffe8cc")
    S.add(acacia(620, 640, 1.3))
    S.add(lion(400, 760, 1.9, expr="content", bras="calin"))
    S.add(rat(400, 480, 0.6, expr="rire", bras="salut"))
    S.add(coeur(260, 300, 1.0), coeur(540, 280, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("rat-seul.svg", vignette),
    ("01-la-sieste.svg", p01), ("02-sur-le-nez.svg", p02), ("03-grrr.svg", p03),
    ("04-attrape.svg", p04), ("05-pardon.svg", p05), ("06-ha-ha-ha.svg", p06),
    ("07-va-petit.svg", p07), ("08-le-piege.svg", p08), ("09-crac.svg", p09),
    ("10-il-se-debat.svg", p10), ("11-roaaar.svg", p11), ("12-j-arrive.svg", p12),
    ("13-cric-crac.svg", p13), ("14-libre.svg", p14), ("15-amis.svg", p15),
]
