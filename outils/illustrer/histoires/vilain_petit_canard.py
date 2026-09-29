"""Le vilain petit canard — chacun grandit à sa façon."""
from contes import *

ID = "vilain-petit-canard"
GRIS = "#adb5bd"


def caneton(x, y, s=0.6, **k):
    return canard(x, y, s, **k)


def vilain(x, y, s=0.8, **k):
    k.setdefault("couleur", GRIS)
    return canard(x, y, s, **k)


def maman_cane(x, y, s=1.2, **k):
    k.setdefault("couleur", "#f8f9fa")
    return canard(x, y, s, **k)


def etang_(S, hiver=False, printemps=True, y=520):
    if hiver:
        ciel(S, "#a5b4c8", "#e9ecef")
        sol(S, y, "#f8f9fa")
        S.add(ellipse(400, y + 180, 480, 170, "#d0ebff"))
        flocons(S, 50, graine=4)
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        if printemps:
            S.add(soleil(680, 100, 42))
        S.add(nuage(160, 110, 0.6))
        sol(S, y, "#94d82d")
        S.add(ellipse(400, y + 180, 480, 170, "#4dabf7"))
        for k in range(4):
            S.add(chemin(f"M {200 + k * 130} {y + 110 + (k % 2) * 60} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    for x in (40, 760):
        for dx in (-18, 0, 18):
            S.add(roseau(x + dx, y + 70, 0.9, penche=dx / 3, visage_=False))


def nid(x, y, s=1.0, oeufs=(), grand=None):
    m = [ellipse(0, 0, 150, 40, "#a0693a")]
    for k, ox in enumerate(oeufs):
        m.append(oeuf(ox, 10, 0.9))
    if grand is not None:
        m.append(oeuf(grand, 10, 1.4, "#e9ecef"))
    m.append(chemin("M -150 0 Q 0 70 150 0 Q 0 40 -150 0 Z", "#8d5524"))
    for k in range(9):
        m.append(trait(-140 + k * 35, 4 + (k % 2) * 8, -110 + k * 35, 16, "#6d4424", 3))
    return place(m, x, y, s)


def cygne_vol(x, y, s=1.0, flip=False):
    m = [chemin("M -80 0 Q 0 -20 80 0 Q 0 26 -80 0 Z", "#fff", stroke="#dee2e6", sw=3),
         chemin("M 60 -4 Q 120 -10 160 -20", stroke="#fff", sw=14), cercle(166, -22, 12, "#fff"),
         poly([(174, -26), (196, -20), (174, -16)], "#ff922b"), cercle(168, -26, 2.5, ENCRE),
         chemin("M -20 -4 Q -40 -90 30 -110 Q 10 -50 30 -6 Z", "#fff", stroke="#dee2e6", sw=3)]
    return place(m, x, y, s, flip=flip)


def couverture():
    S = Scene()
    etang_(S)
    S.add(cygne(560, 690, 1.1))
    S.add(vilain(260, 700, 1.1, expr="bouche_bee", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(vilain(180, 230, 1.2, expr="timide", nage=False))
    return S


def p01():
    S = Scene()
    etang_(S)
    S.add(nid(300, 640, 1.1, oeufs=(), grand=40))
    S.add(maman_cane(560, 690, 1.1, nage=False, expr="content", flip=True))
    for k, x in enumerate((140, 220, 380, 460)):
        S.add(caneton(x, 760 + (k % 2) * 20, 0.55, nage=False, expr="joie"))
    S.add(texte(400, 250, "Crac ! Crac !", 60, "#e67700", contour="#fff"))
    return S


def p02():
    S = Scene()
    etang_(S)
    S.add(g([oeuf(-40, 0, 1.4, "#e9ecef", rot=-30), oeuf(40, 0, 1.4, "#e9ecef", rot=30)]).replace("<g>", '<g transform="translate(400 700)">', 1))
    S.add(vilain(400, 690, 1.0, nage=False, expr="surpris"))
    S.add(maman_cane(640, 690, 1.0, nage=False, expr="surpris", flip=True))
    S.add(caneton(150, 770, 0.5, nage=False, expr="surpris"), caneton(240, 780, 0.5, nage=False, expr="surpris"))
    S.add(texte(400, 250, "CRAC !", 90, "#868e96", contour="#fff"))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 560, "#94d82d")
    S.add(barriere(400, 600, 1.0, largeur=800))
    S.add(coq(150, 760, 1.0, expr="degoute"), coq(640, 760, 1.0, poule=True, expr="fache"))
    S.add(canard(300, 780, 0.8, nage=False, couleur="#f8f9fa", expr="rire", flip=True))
    S.add(vilain(460, 780, 0.9, nage=False, expr="triste", regard=(-1, 0)))
    S.add(texte(400, 200, "Qu'il est vilain !", 60, "#c92a2a", contour="#fff"))
    return S


def p04():
    S = Scene()
    etang_(S)
    for k, x in enumerate((180, 300, 420)):
        S.add(caneton(x, 640 + k * 20, 0.6, expr="rire", flip=k == 2))
    S.add(vilain(620, 700, 0.9, expr="pleure"))
    return S


def p05():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff4e6")
    collines(S, 600, "#b2f2bb", graine=3)
    sol(S, 600, "#94d82d")
    S.add(chemin("M 0 760 Q 400 640 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(vilain(500, 740, 1.0, nage=False, expr="triste"))
    S.add(mouvement(380, 640, 1.0))
    return S


def p06():
    S = Scene()
    etang_(S, printemps=False)
    S.add(canard(260, 680, 1.0, couleur="#8d6e4f", expr="rire"), canard(470, 720, 1.0, couleur="#2f9e44", expr="degoute", flip=True))
    S.add(vilain(620, 700, 0.8, expr="timide", flip=True))
    S.add(bulle(360, 150, 480, 100, "Tu es bien trop vilain\npour venir avec nous !", 32, pointe=(300, 520)))
    return S


def p07():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a27e", 560, papier="#ffe8cc")
    S.add(personne(160, 790, 1.2, coiffure="chignon", cheveux="blanc", habit="#cc5de8", acc=("lunettes",), expr="fache", bras="montre"))
    S.add(coq(360, 790, 0.9, poule=True, expr="fier"), perso("chat", 520, 790, 0.9, expr="malin"))
    S.add(vilain(690, 790, 0.8, nage=False, expr="triste", flip=True))
    S.add(bulle(420, 150, 520, 100, "Tu ne sais ni pondre, ni ronronner ?\nAlors va-t'en !", 28, pointe=(200, 470)))
    return S


def p08():
    S = Scene()
    etang_(S, printemps=False, y=600)
    for k in range(3):
        S.add(cygne_vol(200 + k * 180, 200 + k * 60, 0.9))
    S.add(vilain(400, 730, 1.0, expr="bouche_bee", regard=(1, -1)))
    return S


def p09():
    S = Scene()
    etang_(S, hiver=True)
    S.add(vilain(420, 700, 0.9, expr="pleure"))
    for dx in (-60, -30, 30, 60):
        S.add(roseau(420 + dx, 740, 0.9, penche=dx / 6, visage_=False))
    S.add(texte(400, 180, "Brrr !", 70, "#1864ab", contour="#fff"))
    return S


def p10():
    S = Scene()
    etang_(S)
    for k in range(6):
        S.add(fleur(120 + k * 110, 580 + (k % 2) * 20, 0.8, ["#ff8787", "#fcc419", "#cc5de8"][k % 3]))
    S.add(cygne(400, 720, 1.2, couleur="#e9ecef", ailes="haut", expr="surpris"))
    return S


def p11():
    S = Scene()
    etang_(S)
    S.add(cygne(560, 660, 0.9), cygne(680, 740, 0.8, flip=False))
    S.add(cygne(230, 720, 1.0, couleur="#f8f9fa", expr="timide", flip=False))
    S.add(bulle(260, 200, 440, 100, "Ils vont se moquer\nde moi…", 34, pointe=(310, 520)))
    return S


def p12():
    S = Scene()
    etang_(S, printemps=True)
    S.add(cygne(400, 600, 1.2, expr="bouche_bee", regard=(1, 1)))
    S.add(place(cygne(0, 0, 1.2, expr="bouche_bee"), 400, 620, sy=-1).replace("scale(1 1)", ""), )
    S.add(rect(0, 620, 800, 200, "#4dabf7", opacity=0.45))
    S.add(texte(400, 160, "Un cygne !", 80, "#1864ab", contour="#fff"))
    return S


def p13():
    S = Scene()
    etang_(S)
    S.add(cygne(260, 690, 1.0, expr="content"), cygne(560, 690, 1.0, flip=True, expr="content"))
    S.add(cygne(400, 740, 1.05, expr="rire"))
    S.add(bulle(400, 180, 380, 90, "Viens avec nous !", 38, pointe=(520, 470)))
    return S


def p14():
    S = Scene()
    etang_(S)
    S.add(cygne(470, 700, 1.1, expr="rire"), coeur(560, 360, 1.4))
    S.add(personne(130, 790, 1.0, coiffure="queue", cheveux="noir", habit="#f783ac", peau="brune", expr="rire", bras="montre"))
    S.add(personne(260, 790, 0.9, coiffure="courts", cheveux="roux", habit="#4dabf7", robe=False, jambes="#364fc7", expr="bouche_bee", bras="joues"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("caneton-seul.svg", vignette),
    ("01-les-oeufs.svg", p01), ("02-le-dernier-oeuf.svg", p02), ("03-qu-il-est-vilain.svg", p03), ("04-les-moqueries.svg", p04),
    ("05-il-s-en-va.svg", p05), ("06-les-canards-sauvages.svg", p06), ("07-la-vieille-dame.svg", p07),
    ("08-les-grands-oiseaux.svg", p08), ("09-l-hiver.svg", p09), ("10-le-printemps.svg", p10),
    ("11-les-cygnes.svg", p11), ("12-le-reflet.svg", p12), ("13-viens-avec-nous.svg", p13), ("14-le-plus-beau.svg", p14),
]
