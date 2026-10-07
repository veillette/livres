"""Biscuit chez la vétérinaire — la docteure des animaux."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from animaux import loupe
from contes import cage

ID = "veterinaire-biscuit"
YASMINE = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#69db7c", jambes="#2f9e44",
               chaussures="#f8f9fa", tenue=badge(20, -90, "#ffffff", "rond") + stethoscope())
HUGO = dict(peau="rosee", cheveux="roux", coiffure="courts", habit="#4dabf7", jambes="#495057",
            chaussures="#e8590c")
BISCUIT = dict(couleur="#e3b57a")


def yasmine(x, y, s=1.6, **k):
    return pro(x, y, s, **{**YASMINE, **k})


def hugo(x, y, s=1.2, **k):
    return petit(x, y, s, **{**HUGO, **k})


def biscuit(x, y, s=1.0, pansement_=False, flip=False, **k):
    k.setdefault("expr", "sourire")
    m = [perso("chien", x, y, s, flip=flip, **{**BISCUIT, **k})]
    if pansement_:
        bras = k.get("bras", "bas")
        (gx, gy), (dx, dy) = mains(x, y, s, bras, flip)
        m.append(rect(dx - 13 * s, dy - 8 * s, 26 * s, 16 * s, "#fff", rx=5 * s, stroke="#dee2e6", stroke_width=2))
    return g(m)


def cabinet_veto(S):
    cabinet(S, "#ebfbee", "#d3f9d8", 600, "#b2f2bb")
    S.add(rect(560, 90, 170, 150, "#fff", rx=10, stroke="#8ce99a", stroke_width=4))
    S.add(os_dessin(645, 150), coeur(645, 205, 0.8, "#fa5252"))


def os_dessin(x, y, s=1.0, c="#fff4e6", bord="#d9a066"):
    bouts = [(-42, -10), (-42, 10), (42, -10), (42, 10)]
    return place([cercle(bx, by, 13, bord) for bx, by in bouts] + [rect(-42, -10, 84, 20, bord)]
                 + [cercle(bx, by, 10, c) for bx, by in bouts] + [rect(-42, -7, 84, 14, c)], x, y, s)


def table_veto(x, y, w=320):
    return g([rect(x - 14, y - 160, 28, 160, "#adb5bd"), rect(x - 80, y - 16, 160, 16, "#868e96", rx=6),
              rect(x - w / 2, y - 190, w, 34, "#dee2e6", rx=10, stroke="#adb5bd", stroke_width=4)])


def caisse_chat(x, y, s=1.0):
    m = [rect(-90, -120, 180, 120, "#74c0fc", rx=20), rect(-70, -100, 90, 80, "#e7f5ff", rx=10)]
    m.append(perso("chat", -25, -24, 0.42, expr="neutre", couleur="#868e96"))
    for k in range(4):
        m.append(trait(-60 + k * 22, -100, -60 + k * 22, -20, "#1c7ed6", 4))
    m.append(rect(-30, -140, 60, 24, "#1c7ed6", rx=10))
    return place(m, x, y, s)


def gamelle(x, y, s=1.0, contenu="#74c0fc", c="#e64980"):
    return place([ellipse(0, -10, 50, 14, contenu), chemin("M -56 -12 L -44 14 L 44 14 L 56 -12 Z", c)], x, y, s)


def croquettes(x, y, s=1.0):
    m = [gamelle(0, 0, 1.0, "#c68642", "#7048e8")]
    for k in range(7):
        m.append(cercle(-30 + k * 10, -16 - (k % 2) * 6, 6, "#a0693a"))
    return place(m, x, y, s)


def jardin(S, y=600):
    ciel(S)
    collines(S, y, "#b2f2bb", graine=6)
    sol(S, y, "#8ce99a")


def couverture():
    S = Scene()
    cabinet_veto(S)
    S.add(yasmine(250, 780, 1.85, expr="rire", bras="calin"))
    S.add(biscuit(520, 780, 1.45, pansement_=True, expr="rire", bras="salut"))
    S.add(coeur(400, 320, 1.1, "#fa5252"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(os_dessin(200, 120, 1.8))
    S.add(coeur(110, 230, 0.9, "#fa5252"), pansement(290, 230, 2.0, rot=-15))
    return S


def p01():
    S = Scene()
    jardin(S)
    S.add(maison(150, 600, 1.1))
    S.add(biscuit(470, 760, 1.4, expr="pleure", bras="donne", regard=(0, 0)))
    S.add(hugo(250, 780, 1.35, expr="inquiet", bras="joues", regard=(1, 0)))
    S.add(texte(620, 380, "Hiii…", 44, "#a0693a", contour="#fff"))
    return S


def p02():
    S = Scene()
    cabinet_veto(S)
    S.add(rect(40, 560, 720, 30, "#8ce99a", rx=10))
    S.add(caisse_chat(140, 560, 1.0))
    S.add(perso("lapin", 340, 560, 0.9, expr="timide", regard=(1, 0)))
    S.add(rect(440, 300, 140, 14, "#c68642", rx=6), trait(510, 314, 510, 560, "#c68642", 8))
    S.add(oiseau(510, 300, 0.8, "#40c057", "#d3f9d8", bec_ouvert=True))
    S.add(notes(600, 250, 0.8, "#2f9e44"))
    S.add(hugo(580, 790, 1.15, expr="sourire", bras="bas", regard=(1, 0)))
    S.add(biscuit(700, 790, 0.9, expr="triste", bras="donne", pansement_=False, flip=True))
    return S


def p03():
    S = Scene()
    cabinet_veto(S)
    S.add(table_veto(470, 780, 340))
    S.add(biscuit(470, 590, 1.2, expr="timide", bras="bas", regard=(-1, 0)))
    S.add(yasmine(190, 780, 1.7, expr="content", bras="donne", regard=(1, 0)))
    S.add(bulle(260, 120, 400, 100, "N'aie pas peur,\nmon grand.", 34, pointe=(220, 400)))
    S.add(coeur(380, 420, 0.6, "#fa5252"))
    return S


def p04():
    S = Scene()
    cabinet_veto(S)
    S.add(yasmine(160, 780, 1.55, expr="concentre", bras="donne", regard=(1, -0.3)))
    S.add(biscuit(640, 780, 1.3, expr="inquiet", bras="donne", flip=True))
    patte = g([cercle(400, 380, 140, "#e3b57a"), ellipse(400, 420, 60, 46, "#a0693a"),
               ellipse(330, 320, 26, 32, "#a0693a"), ellipse(400, 296, 26, 32, "#a0693a"), ellipse(470, 320, 26, 32, "#a0693a"),
               poly([(416, 392), (486, 326), (436, 402)], "#343a40")])
    S.add(loupe(400, 360, 150, patte, rot=140))
    S.add(texte(400, 600, "une épine !", 44, "#e8590c", contour="#fff"))
    return S


def pince(x, y, s=1.0, rot=0):
    return place([chemin("M 0 0 L 70 -6 M 0 0 L 70 6", stroke="#868e96", sw=6)], x, y, s, rot=rot)


def p05():
    S = Scene()
    cabinet_veto(S)
    S.add(table_veto(470, 780, 340))
    S.add(biscuit(470, 590, 1.2, pansement_=True, expr="rire", bras="donne", regard=(-1, 0)))
    S.add(mouvement(560, 520, 0.8, rot=-30))
    S.add(yasmine(190, 780, 1.7, expr="rire", bras="donne", regard=(1, 0)))
    xm, ym = 190 + 84 * 1.7, 780 - 92 * 1.7
    S.add(pince(xm, ym, 1.0, rot=-10))
    S.add(poly([(xm + 76, ym - 30), (xm + 96, ym - 50), (xm + 82, ym - 22)], "#495057"))
    S.add(texte(250, 300, "Hop !", 64, "#2f9e44", contour="#fff", rot=-8))
    return S


def p06():
    S = Scene()
    cabinet_veto(S)
    S.add(rect(340, 700, 260, 30, "#e9ecef", rx=10, stroke="#ced4da", stroke_width=3))
    S.add(rect(420, 735, 100, 30, "#343a40", rx=4), texte(470, 758, "12 kg", 22, "#69db7c"))
    S.add(biscuit(470, 708, 1.25, pansement_=True, expr="fier", bras="bas"))
    S.add(yasmine(190, 790, 1.6, expr="content", bras="donne", tenue=badge(20, -90, "#ffffff", "rond"),
                  regard=(1, 0)))
    xm, ym = 190 + 84 * 1.6, 790 - 92 * 1.6
    S.add(chemin(f"M {xm} {ym} Q {xm + 60} {ym + 40} 455 620", stroke="#495057", sw=5),
          cercle(455, 620, 12, "#adb5bd", stroke="#495057", stroke_width=4))
    S.add(texte(620, 360, "Tout va bien !", 42, "#2f9e44", contour="#fff"))
    return S


def p07():
    S = Scene()
    cabinet_veto(S)
    S.add(table_veto(240, 780, 300), table_veto(600, 780, 300))
    S.add(perso("chat", 240, 590, 1.1, expr="baille", couleur="#868e96"))
    S.add(lampe_poche(150, 420, 0.8, rot=30, couleur="#2f9e44"))
    S.add(perso("lapin", 600, 590, 1.1, expr="surpris", bras="donne", flip=True))
    S.add(place([rect(-30, -6, 60, 12, "#868e96", rx=5), rect(20, -10, 30, 20, "#fa5252", rx=6)], 510, 470, 1.0, rot=20))
    S.add(texte(240, 300, "Mimi", 44, "#495057"), texte(600, 300, "Pompon", 44, "#495057"))
    return S


def p08():
    S = Scene()
    jardin(S)
    S.add(yasmine(400, 790, 1.5, expr="content", bras="ouverts"))
    rondes = [(140, 170, gamelle(0, 20, 1.2)), (140, 430, croquettes(0, 20, 1.1)),
              (660, 170, g([trait(-50, 30, 40, -30, "#e64980", 8), cercle(46, -34, 12, "none", stroke="#e64980", stroke_width=6)])),
              (660, 430, coeur(0, 0, 1.6, "#fa5252"))]
    for x, y, contenu in rondes:
        S.add(cercle(x, y, 95, "#fff", stroke="#8ce99a", stroke_width=6), place(contenu, x, y))
    for (x, y, mot) in [(140, 300, "de l'eau"), (140, 560, "à manger"), (660, 300, "des promenades"), (660, 560, "des câlins")]:
        S.add(texte(x, y, mot, 30, "#2b8a3e", contour="#fff"))
    return S


def p09():
    S = Scene()
    jardin(S)
    S.add(maison(660, 600, 1.0))
    S.add(biscuit(470, 720, 1.35, expr="rire", bras="haut", rot=-10))
    S.add(mouvement(350, 620, 1.2))
    S.add(ballon_jeu(600, 740, 34))
    S.add(hugo(200, 790, 1.4, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(texte(560, 260, "Guéri !", 64, "#2f9e44", contour="#fff"))
    return S


def p10():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 600, papier="#ffd8a8")
    S.add(tapis(420, 720, 320, 60, "#d3f9d8", "#8ce99a"))
    S.add(hugo(250, 780, 1.55, expr="rire", bras="salut", tenue=stethoscope()))
    S.add(perso("ours", 450, 720, 0.6, expr="sourire", couleur="#d9a066"))
    S.add(perso("lapin", 560, 720, 0.6, expr="content", bras="donne", flip=True))
    S.add(rect(538, 630, 20, 12, "#fff", rx=4))
    S.add(perso("souris", 660, 730, 0.55, expr="surpris"))
    S.add(biscuit(720, 780, 0.9, expr="rire", flip=True))
    S.add(bulle(330, 130, 300, 90, "Au suivant !", 40, pointe=(270, 420)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("os-seul.svg", vignette),
    ("01-biscuit-a-mal.svg", p01), ("02-salle-d-attente.svg", p02), ("03-sur-la-table.svg", p03),
    ("04-une-epine.svg", p04), ("05-le-pansement.svg", p05), ("06-la-balance.svg", p06),
    ("07-mimi-et-pompon.svg", p07), ("08-conseils.svg", p08), ("09-gueri.svg", p09),
    ("10-au-suivant.svg", p10),
]
