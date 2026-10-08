"""Les Deux Ânes — d'après « L'Âne chargé d'éponges et l'Âne chargé de sel ».

Grisou porte du sel, Cadichon des éponges. Dans la rivière, le sel se
dissout et Grisou s'allège ; Cadichon l'imite, mais ses éponges se gorgent
d'eau et l'alourdissent. Adaptation douce : personne ne se noie, Grisou
(désormais léger) aide l'ânier à tirer Cadichon sur la berge.
"""
from fables import *

ID = "deux-anes"
SEL = "#f8f9fa"
EPONGE = "#ffd43b"
FIRMIN = dict(coiffure="courts", cheveux="chatain", peau="rosee", habit="#2f9e44", robe=False, jambes="#5c3a1e",
              chaussures="#343a40", barbe="#8d5524")
CADICHON = "#b5a089"


def firmin(x, y, s=1.0, **k):
    return personne(x, y, s, **{**FIRMIN, **k})


def eponges(x, y, s=1.0, nb=3, mouillees=False):
    """Éponges attachées sur un dos ; (x, y) = milieu du dos."""
    c = "#e8b923" if mouillees else EPONGE
    m = [rect(-64, -10, 128, 20, "#1971c2", rx=6)]
    for k in range(nb):
        dx = (k - (nb - 1) / 2) * 44
        h = 70 if mouillees else 60
        m.append(rect(dx - 22, -10 - h, 44, h, c, rx=10, stroke="#f08c00", stroke_width=3))
        for px, py in ((-8, -20), (8, -36), (-6, -50), (10, -14)):
            m.append(cercle(dx + px, -10 + py * h / 60, 4, "#f59f00"))
        if mouillees:
            m.append(goutte(dx + 14, 10, 0.7, "#4dabf7"))
    return place(m, x, y, s)


def grisou(S, x, y, s=1.0, nb=3, ploie=False, charge=True, **k):
    S.add(ane_profil(x, y, s, ploie=ploie, **k))
    if charge:
        S.add(bat(x, y - (110 - (16 if ploie else 0)) * s, s, nb=nb, couleur=SEL))
        S.add(g([texte(x + (kk - (nb - 1) / 2) * min(56, 120 / max(1, nb - 1)) * s, y - 150 * s, "SEL", 20 * s, "#868e96")
                 for kk in range(nb)]))


def cadichon(S, x, y, s=1.0, mouillees=False, ploie=False, **k):
    S.add(ane_profil(x, y, s, ploie=ploie, couleur=CADICHON, **k))
    S.add(eponges(x, y - (110 - (16 if ploie else 0)) * s, s, mouillees=mouillees))


def chemin_campagne(S, graine=11, soir=False):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(150, 110, 0.6), nuage(640, 150, 0.5))
    collines(S, 580, "#b2f2bb", graine=graine)
    S.add(moulin(680, 560, 0.6))
    sol(S, 600, "#8ce99a")
    S.add(chemin("M 0 700 Q 400 650 800 690 L 800 800 L 0 800 Z", "#f3d9a4"))


def bord_riviere(S, y=600, graine=12):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(140, 100, 0.55))
    collines(S, 480, "#b2f2bb", graine=graine)
    S.add(rect(0, 470, 800, 60, "#8ce99a"))
    riviere(S, y - 70)


def eau_devant(S, y):
    """Bande d'eau dessinée devant les personnages (ils sont « dans » la rivière)."""
    S.add(chemin(f"M 0 {y} Q 200 {y - 14} 400 {y} T 800 {y} L 800 800 L 0 800 Z", "#4dabf7", opacity=0.92))
    for k in range(3):
        yy = y + 40 + k * 50
        S.add(chemin(" ".join(f"M {40 + i * 180 + (k % 2) * 80} {yy} q 25 -12 50 0" for i in range(5)), stroke="#a5d8ff", sw=5))


def berge(S, x0=0, x1=260, y=600):
    S.add(chemin(f"M {x0} 800 L {x0} {y} L {x1 - 40} {y} Q {x1} {y + 60} {x1 + 20} 800 Z", "#69db7c"))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    bord_riviere(S)
    berge(S, 0, 330, 600)
    cadichon(S, 580, 730, 1.05, mouillees=True, ploie=True, expr="oups")
    eau_devant(S, 650)
    grisou(S, 170, 640, 0.9, nb=3, expr="rire")
    S.add(eclat(580, 640, 1.2, "#a5d8ff"))
    S.cachette(200, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ane_profil(120, 262, 0.55, expr="sourire"))
    S.add(ane_profil(290, 262, 0.55, expr="sourire", couleur=CADICHON))
    return S


def p01():
    S = Scene()
    chemin_campagne(S)
    S.add(firmin(640, 760, 1.15, expr="content", bras="salut"))
    grisou(S, 160, 770, 0.85, expr="sourire")
    cadichon(S, 410, 770, 0.85, expr="sourire")
    S.cachette(650, 70, "air")
    return S


def p02():
    S = Scene()
    chemin_campagne(S, 13)
    grisou(S, 200, 770, 1.0, ploie=True, expr="inquiet")
    S.add(goutte(330, 560, 0.9, "#74c0fc"))
    cadichon(S, 540, 770, 0.95, expr="malin", regard=(-1, 0), flip=True)
    S.add(texte(560, 220, "Pauvre Grisou !", 48, "#f08c00", contour="#fff"))
    return S


def p03():
    S = Scene()
    bord_riviere(S, 600, 14)
    berge(S, 0, 640, 560)
    S.add(firmin(150, 640, 1.0, expr="inquiet", bras="montre", regard=(1, 0)))
    grisou(S, 330, 560, 0.7, expr="surpris")
    cadichon(S, 520, 560, 0.7, expr="surpris")
    S.add(texte(560, 200, "Pas de pont !", 52, "#1971c2", contour="#fff"))
    S.cachette(730, 500, "air")
    return S


def p04():
    S = Scene()
    bord_riviere(S, 600, 15)
    grisou(S, 380, 720, 1.1, ploie=True, expr="oups", rot=-8)
    eau_devant(S, 620)
    S.add(eclat(380, 610, 1.5, "#d0ebff"), texte(380, 230, "Plouf !", 84, "#1971c2", contour="#fff", rot=-6))
    S.cachette(730, 500, "air")
    return S


def p05():
    S = Scene()
    bord_riviere(S, 600, 16)
    berge(S, 520, 800, 560)
    grisou(S, 380, 690, 1.0, charge=False, expr="rire", regard=(1, -1))
    S.add(bat(380, 690 - 110, 1.0, nb=0))
    eau_devant(S, 650)
    S.add(g([cercle(280 + k * 30, 640 - (k % 2) * 16, 7, "#fff", opacity=0.8) for k in range(6)]))
    S.add(texte(400, 230, "Tout léger !", 64, "#f08c00", contour="#fff"))
    S.cachette(730, 500, "air")
    return S


def p06():
    S = Scene()
    bord_riviere(S, 600, 17)
    berge(S, 0, 300, 560)
    cadichon(S, 170, 560, 0.9, expr="malin", regard=(1, 0))
    S.add(pensee(560, 220, 150, g([ane_profil(560, 290, 0.45, expr="rire", couleur=CADICHON)]), depuis=(260, 400)))
    grisou(S, 620, 700, 0.8, charge=False, expr="content", flip=True)
    eau_devant(S, 660)
    S.cachette(630, 730, "air")
    return S


def p07():
    S = Scene()
    bord_riviere(S, 600, 18)
    cadichon(S, 400, 720, 1.1, expr="rire", rot=-10)
    eau_devant(S, 630)
    S.add(eclat(400, 620, 1.5, "#d0ebff"), texte(400, 230, "Plouf !", 84, "#1971c2", contour="#fff", rot=6))
    S.cachette(630, 730, "air")
    return S


def p08():
    S = Scene()
    bord_riviere(S, 600, 19)
    cadichon(S, 400, 720, 1.1, mouillees=True, ploie=True, expr="inquiet")
    eau_devant(S, 640)
    S.add(texte(560, 230, "Glouglouglou…", 54, "#1971c2", contour="#fff"))
    S.add(fleche(620, 380, 620, 480, "#e03131"))
    S.cachette(570, 730, "air")
    return S


def p09():
    S = Scene()
    bord_riviere(S, 600, 20)
    berge(S, 0, 220, 560)
    cadichon(S, 430, 760, 1.1, mouillees=True, ploie=True, expr="pleure")
    eau_devant(S, 610)
    S.add(firmin(170, 640, 0.95, expr="inquiet", bras="tire", rot=-10))
    S.add(chemin("M 250 560 Q 330 600 420 600", stroke="#c68642", sw=6))
    S.add(bulle(560, 200, 340, 90, "Au secours !", 44, pointe=(520, 520)))
    S.cachette(730, 500, "air")
    return S


def p10():
    S = Scene()
    bord_riviere(S, 600, 21)
    berge(S, 0, 300, 560)
    S.add(chemin("M 120 520 Q 280 580 470 600", stroke="#c68642", sw=6))
    grisou(S, 120, 560, 0.75, charge=False, expr="concentre", flip=True)
    S.add(firmin(250, 640, 0.95, expr="concentre", bras="tire", flip=True))
    cadichon(S, 540, 740, 1.0, mouillees=True, expr="inquiet", rot=-8)
    eau_devant(S, 630)
    S.add(texte(400, 200, "Ho hisse !", 64, "#2f9e44", contour="#fff"))
    S.cachette(730, 500, "air")
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(soleil(680, 110, 46))
    collines(S, 520, "#b2f2bb", graine=22)
    sol(S, 560, "#8ce99a")
    S.add(rect(0, 690, 800, 110, "#4dabf7"))
    S.add(firmin(400, 760, 1.05, expr="rire", bras="tient", objet=g([rect(50, -170, 44, 50, EPONGE, rx=10, stroke="#f08c00", stroke_width=3)])))
    S.add(g([goutte(470 + k * 8, 640 + k * 26, 0.8, "#4dabf7") for k in range(4)]))
    grisou(S, 150, 760, 0.85, charge=False, expr="rire")
    cadichon(S, 640, 760, 0.85, expr="oups", flip=True)
    S.add(g([goutte(600 + k * 30, 600 + (k % 2) * 30, 0.7, "#74c0fc") for k in range(4)]))
    S.cachette(140, 70, "air")
    return S


def p12():
    S = Scene()
    chemin_campagne(S, 23, soir=True)
    grisou(S, 200, 770, 0.85, charge=False, expr="content")
    cadichon(S, 460, 770, 0.85, expr="content")
    S.add(firmin(680, 760, 1.05, expr="sourire", bras="salut", flip=True))
    S.add(bulle(330, 230, 460, 120, "Je ne porte pas\nle même sac que toi !", 36, pointe=(500, 560)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("deux-anes.svg", vignette),
    ("01-au-marche.svg", p01), ("02-pauvre-grisou.svg", p02), ("03-la-riviere.svg", p03), ("04-plouf.svg", p04),
    ("05-tout-leger.svg", p05), ("06-moi-aussi.svg", p06), ("07-a-mon-tour.svg", p07), ("08-glouglou.svg", p08),
    ("09-au-secours.svg", p09), ("10-ho-hisse.svg", p10), ("11-sur-la-berge.svg", p11), ("12-le-retour.svg", p12),
]
