"""Le Loup et le Chien — la liberté n'a pas de prix."""
from fables import *

ID = "loup-chien"


def loup(x, y, s=1.0, maigre=True, **k):
    return perso("loup", x, y, s, sy=s * 1.12 if maigre else None, **k)


def chien(x, y, s=1.0, collier_=True, pele=False, **k):
    # le collier passe sous la tête : on le donne comme `objet` du personnage
    cou = None
    if collier_:
        cou = collier(0, -96, 0.95)
    elif pele:
        cou = g([ellipse(0, -96, 42, 13, "#fff4e6"),
                 ellipse(0, -96, 42, 13, "none", stroke="#c9a27e", stroke_width=3, stroke_dasharray="6 6")])
    return perso("chien", x, y, s * 1.12, sy=s * 0.94, objet=cou, **k)


def bois(S, nuit_=True, lune_=(640, 130)):
    if nuit_:
        nuit(S, "#1c2a52", "#364fc7")
        etoiles(S, 40, graine=9)
        if lune_:
            S.add(lune(*lune_, 44))
    else:
        ciel(S, "#ffc078", "#fff4e6")
    for tx, s_ in ((60, 1.3), (160, 1.0), (720, 1.2), (640, 0.8)):
        S.add(sapin(tx, 620, s_, "#2b8a3e" if nuit_ else "#2f9e44", "#237032" if nuit_ else "#37b24d"))
    sol(S, 620, "#2f9e44" if nuit_ else "#69db7c")


def lisiere(S, soir=True):
    ciel(S, "#9775fa" if soir else "#a5d8ff", "#ffc9c9" if soir else "#e7f5ff")
    S.add(lune(660, 120, 36) if soir else soleil(660, 120, 50))
    for tx, s_ in ((60, 1.3), (160, 1.0)):
        S.add(sapin(tx, 620, s_))
    collines(S, 600, "#8ce99a", graine=5)
    sol(S, 620, "#69db7c")
    S.add(maison(680, 640, 0.7, lumiere=soir))


def niche(x, y, s=1.0):
    toit = [(-124, -140), (0, -230), (124, -140)]
    m = [ombre_sol(10, 0, 130, 12, 0.16), rect(-100, -150, 200, 150, cylindre("#c92a2a", 0.2, 0.75)),
         planches(-100, -150, 200, 150, "#c92a2a", larg=25, vertical=False),
         ombre_avancee(-100, -146, 200, 20, 0.25),
         poly(toit, lineaire([(0, "#b03a3a"), (0.5, "#862e2e"), (1, "#5c1e1e")], 0, 0, 1, 1)),
         tuiles(-124, -230, 248, 90, "#862e2e", poly(toit, "#000")),
         chemin("M -124 -140 L 0 -230 L 124 -140", stroke="#4a1717", sw=6),
         chemin("M -54 0 L -54 -70 Q -54 -118 0 -118 Q 54 -118 54 -70 L 54 0 Z", "#f1f3f5"),
         chemin("M -46 0 L -46 -70 Q -46 -110 0 -110 Q 46 -110 46 -70 L 46 0 Z", radial([(0, "#495057"), (1, "#16181b")], cy=0.7)),
         rect(-30, -132, 60, 18, volume("#ffd43b", 0.4, 0.75), rx=4)]
    return place(m, x, y, s)


def chaine(x1, y1, x2, y2, nb=10):
    m = []
    for k in range(nb + 1):
        t = k / nb
        px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t + math.sin(t * math.pi) * 40
        m.append(ellipse(px, py, 9, 6, "none", stroke="#868e96", stroke_width=4, rot=(k % 2) * 90))
    return g(m)


def gamelle(x, y, s=1.0, pleine=True):
    m = [chemin("M -60 -40 L 60 -40 L 48 0 L -48 0 Z", "#4dabf7"), ellipse(0, -40, 60, 12, "#1c7ed6")]
    if pleine:
        m += [place(os_(), -20, -54, 0.6, rot=-20), place(os_(), 22, -50, 0.5, rot=30)]
    return place(m, x, y, s)


def os_():
    m = [rect(-40, -8, 80, 16, "#fff9db", rx=8)]
    for sx in (-1, 1):
        for sy_ in (-1, 1):
            m.append(cercle(sx * 42, sy_ * 10, 13, "#fff9db"))
    return g(m)


def couverture():
    S = Scene()
    lisiere(S)
    S.add(loup(260, 760, 1.35, expr="malin", bras="bas", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="content", bras="hanches"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(collier(200, 140, 2.6))
    return S


def p01():
    S = Scene()
    bois(S)
    S.add(loup(400, 760, 1.6, expr="triste", bras="calin"))
    S.add(texte(600, 360, "Grrr…", 44, "#fff3bf"))
    S.add(texte(620, 420, "(c'est mon ventre)", 26, "#fff3bf"))
    return S


def p02():
    S = Scene()
    lisiere(S)
    S.add(chien(430, 760, 1.6, expr="content", bras="hanches"))
    S.add(paillettes(250, 380, 1.0), paillettes(620, 360, 0.9))
    return S


def p03():
    S = Scene()
    lisiere(S)
    S.add(loup(230, 760, 1.35, expr="malin", bras="salut", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="fier", bras="hanches", regard=(-1, 0)))
    S.add(bulle(260, 130, 440, 100, "Quel beau pelage\nvous avez !", 34, pointe=(240, 440)))
    return S


def p04():
    S = Scene()
    lisiere(S)
    S.add(loup(230, 760, 1.35, expr="surpris", bras="bas", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="rire", bras="montre", flip=True))
    S.add(bulle(520, 130, 460, 110, "Venez vivre chez\nmon maître !", 36, pointe=(540, 440)))
    return S


def p05():
    S = Scene()
    lisiere(S)
    S.add(loup(200, 760, 1.25, expr="inquiet", bras="pense", regard=(1, -1)))
    S.add(chien(560, 760, 1.25, expr="content", bras="ouverts"))
    S.add(pensee(430, 220, 170, depuis=(540, 440),
                 contenu=g([maison(360, 280, 0.55, lumiere=True), personne(470, 290, 0.6, coiffure="courts", cheveux="brun", habit="#4dabf7", robe=False, expr="content")])))
    return S


def p06():
    S = Scene()
    lisiere(S)
    S.add(loup(230, 760, 1.25, expr="bouche_bee", bras="joues", regard=(1, -1)))
    S.add(chien(560, 760, 1.25, expr="content", bras="bas"))
    S.add(pensee(420, 230, 170, depuis=(530, 440), contenu=gamelle(420, 280, 1.6)))
    return S


def p07():
    S = Scene()
    lisiere(S)
    S.add(chemin("M 0 720 Q 400 660 800 700 L 800 760 Q 400 720 0 780 Z", "#f3d9a4"))
    S.add(loup(300, 760, 1.25, expr="rire", bras="bas", regard=(1, 0)))
    S.add(chien(500, 760, 1.25, expr="content", bras="bas", flip=True))
    S.add(coeur(300, 420, 0.8))
    return S


def p08():
    S = Scene()
    lisiere(S)
    S.add(loup(250, 760, 1.35, expr="surpris", bras="montre", regard=(1, -1)))
    S.add(chien(540, 760, 1.35, expr="neutre", bras="bas", collier_=False, pele=True))
    S.add(texte(560, 380, "?", 80, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    lisiere(S)
    S.add(loup(250, 760, 1.35, expr="surpris", bras="montre", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="timide", bras="bas", collier_=False, pele=True, regard=(0, 1)))
    S.add(bulle(250, 130, 300, 90, "C'est quoi ?", 40, pointe=(250, 440)))
    S.add(bulle(580, 230, 300, 90, "Presque rien…", 36, pointe=(560, 440)))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 600, "#8ce99a")
    S.add(maison(640, 620, 1.1))
    S.add(niche(230, 700, 1.0))
    S.add(chien(400, 760, 1.3, expr="triste", bras="bas"))
    S.add(chaine(300, 640, 400, 760 - 100 * 1.3 * 0.94))
    return S


def p11():
    S = Scene()
    lisiere(S)
    S.add(loup(250, 760, 1.35, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="timide", bras="bas", collier_=False, pele=True))
    S.add(bulle(270, 120, 440, 110, "Attaché ?\nToute la journée ?", 36, pointe=(250, 440)))
    return S


def p12():
    S = Scene()
    lisiere(S)
    S.add(loup(250, 760, 1.35, expr="content", bras="pense", regard=(1, -1)))
    reve = g([rect(330, 90, 400, 260, "#1c2a52", rx=120), lune(620, 160, 26), sapin(400, 320, 0.4, "#2b8a3e"),
              place(perso("loup", 0, 0, 0.5, expr="rire", bras="course"), 520, 310)])
    S.add(pensee(530, 220, 230, depuis=(330, 420), contenu=reve))
    return S


def p13():
    S = Scene()
    lisiere(S)
    S.add(loup(250, 760, 1.35, expr="fier", bras="hanches", regard=(1, 0)))
    S.add(chien(540, 760, 1.35, expr="surpris", bras="bas", collier_=False, pele=True))
    S.add(bulle(290, 110, 480, 120, "Tous vos repas ne valent\npas ma liberté !", 32, pointe=(250, 440)))
    return S


def p14():
    S = Scene()
    lisiere(S)
    S.add(loup(260, 740, 1.4, expr="rire", bras="course", flip=True, rot=12))
    S.add(mouvement(430, 580, 1.4, rot=180), mouvement(450, 480, 1.1, rot=180))
    S.add(chien(640, 760, 0.9, expr="surpris", bras="joues"))
    S.cachette(730, 430, "air")
    return S


def p15():
    S = Scene()
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 50, graine=4)
    S.add(lune(560, 170, 90))
    S.add(chemin("M 0 800 L 0 640 Q 300 520 520 600 Q 680 650 800 700 L 800 800 Z", "#2b8a3e"))
    S.add(loup(330, 610, 1.3, expr="chante", bras="bas", regard=(1, -1)))
    S.add(texte(560, 360, "Aouuuu !", 56, "#fff3bf"))
    S.cachette(620, 740)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("collier-seul.svg", vignette),
    ("01-le-loup.svg", p01), ("02-le-chien.svg", p02), ("03-bonsoir.svg", p03),
    ("04-venez.svg", p04), ("05-presque-rien.svg", p05), ("06-la-gamelle.svg", p06),
    ("07-en-route.svg", p07), ("08-le-cou.svg", p08), ("09-c-est-quoi.svg", p09),
    ("10-la-chaine.svg", p10), ("11-attache.svg", p11), ("12-le-reve.svg", p12),
    ("13-ma-liberte.svg", p13), ("14-il-court.svg", p14), ("15-aouuu.svg", p15),
]
