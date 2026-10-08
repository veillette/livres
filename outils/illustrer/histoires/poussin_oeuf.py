"""Le poussin dans l'œuf — la couvaison.

La poule couve une dizaine d'œufs (fécondés par le coq) pendant 21 jours :
elle les garde au chaud sous son ventre et les retourne avec son bec. Dans
l'œuf, le poussin grandit en se nourrissant du jaune. Quelques jours avant
d'éclore, il pépie déjà dans sa coquille et la poule lui répond. Il perce la
coquille avec le « diamant », une petite pointe au bout de son bec, sort tout
mouillé, sèche en quelques heures, puis suit sa mère et picore. La nuit, les
poussins se cachent sous les ailes de la poule.
"""
from base import *
from base import _assombrir
from animaux import *
from fables import coq, oeuf
from contes import poule_rousse, poussin
from objets import barriere
from sciences import fleche

ID = "poussin-oeuf"
JAUNE = "#ffe066"


# --- Dessins ----------------------------------------------------------------

def poule(x, y, s=1.0, **k):
    return poule_rousse(x, y, s, **k)


def nid(x, y, s=1.0, devant=True, graine=1):
    """Nid de paille ; (x, y) = centre du creux. `devant` : seulement le
    rebord avant (à dessiner par-dessus la poule et les œufs)."""
    r = random.Random(graine)
    m = []
    if not devant:
        m.append(ellipse(0, 0, 150, 46, "#e9c46a"))
        m.append(ellipse(0, -6, 120, 30, "#c9a03a"))
    else:
        m.append(chemin("M -160 -4 Q 0 16 160 -4 Q 150 44 0 54 Q -150 44 -160 -4 Z", "#e9c46a"))
        for _ in range(30):
            a = r.uniform(-0.3, 0.3)
            px = r.uniform(-150, 150)
            py = r.uniform(4, 40)
            m.append(trait(px - 22, py, px + 22, py + a * 30, "#d4a72c", 3))
    return place(m, x, y, s)


def poule_couve(x, y, s=1.0, expr="content", **k):
    """Poule installée dans son nid (on ne voit pas ses pattes) ; (x, y) = centre du nid."""
    return g([nid(x, y, s, devant=False), poule(x, y + 50 * s, s * 1.25, expr=expr, **k), nid(x, y, s, devant=True)])


def oeuf_coupe(x, y, s=1.0, stade=1, rot=0):
    """Œuf coupé en deux : blanc, jaune, chambre à air et poussin qui grandit
    (stade 1 : tout petit ; 2 : moyen ; 3 : il remplit l'œuf). (x, y) = centre."""
    m = [ellipse(0, 0, 96, 124, "#f1e3c8"), ellipse(0, 0, 88, 116, "#fffdf6")]
    m.append(chemin("M -64 -84 Q 0 -110 64 -84 Q 40 -116 0 -116 Q -40 -116 -64 -84 Z", "#e7f5ff"))
    if stade == 1:
        m.append(cercle(0, 20, 60, "#ffd43b"))
        m.append(chemin("M -10 -20 Q 10 -30 14 -10 Q 10 4 -6 0", stroke="#fa5252", sw=3))
        m.append(place(g([ellipse(0, 0, 10, 7, "#ffc9c9"), cercle(8, -4, 5, "#ffc9c9")]), 2, -16))
    elif stade == 2:
        m.append(cercle(0, 40, 46, "#ffd43b"))
        for k in range(4):
            m.append(chemin(f"M 0 40 Q {-60 + k * 40} -20 {-50 + k * 34} -60", stroke="#fa5252", sw=2.5, opacity=0.7))
        m.append(place(g([ellipse(0, 0, 34, 26, "#ffd8a8"), cercle(26, -16, 18, "#ffd8a8"), cercle(30, -20, 4, ENCRE),
                          poly([(42, -16), (52, -12), (42, -8)], "#ffa94d")]), -6, -10))
    else:
        m.append(ellipse(0, 70, 30, 18, "#ffd43b"))
        m.append(place(g([ellipse(0, 0, 70, 80, JAUNE), cercle(30, -50, 40, JAUNE), oeil(40, -58, "fermes", taille=0.9),
                          poly([(64, -50), (80, -44), (64, -38)], "#ff922b"), cercle(80, -46, 3, "#ffffff"),
                          ellipse(-30, 0, 20, 40, _assombrir(JAUNE, 0.9), rot=20)]), -10, 10, 0.95))
    return place(m, x, y, s, rot=rot)


def poussin_mouille(x, y, s=1.0, flip=False):
    """Poussin qui vient de naître : plumes collées et mouillées."""
    m = [poussin(0, 0, 1.0, couleur="#e6c84f", ventre="#efe0a0", expr="dort", ailes="bas")]
    for px, py in [(-30, -100), (-10, -112), (14, -110), (32, -96), (-40, -60), (40, -60), (0, -40)]:
        m.append(chemin(f"M {px} {py} q 4 10 -2 18", stroke="#c9a92f", sw=3))
    m.append(goutte(46, -110, 0.5, "#74c0fc"))
    return place(m, x, y, s, flip=flip)


def coquille(x, y, s=1.0, rot=0, haut=False):
    """Moitié de coquille cassée en dents de scie ; `haut` : la calotte."""
    if haut:
        m = [chemin("M -24 0 L -16 -8 L -8 2 L 0 -8 L 8 2 L 16 -8 L 24 0 Q 24 -40 0 -42 Q -24 -40 -24 0 Z", "#fff9f0",
                    stroke="#e9ddc8", sw=2)]
    else:
        m = [chemin("M -26 -20 L -16 -30 L -8 -18 L 0 -30 L 8 -18 L 16 -30 L 26 -20 Q 30 20 0 22 Q -30 20 -26 -20 Z",
                    "#fff9f0", stroke="#e9ddc8", sw=2)]
    return place(m, x, y, s, rot=rot)


def basse_cour(S, y=560, interieur_=False):
    if interieur_:
        S.add(rect(0, 0, 800, 800, "#e8c39e"))
        for k in range(9):
            S.add(rect(k * 90, 0, 84, y, "#d9a066"))
        S.add(rect(0, y, 800, 800 - y, "#c9a03a"))
        r = random.Random(3)
        for _ in range(40):
            px, py = r.uniform(0, 800), r.uniform(y + 10, 800)
            S.add(trait(px - 16, py, px + 16, py + r.uniform(-6, 6), "#e9c46a", 3))
        return
    ciel(S, "#a5d8ff", "#fff9db")
    toit = [(-190, -220), (190, -220), (0, -340)]
    S.add(place([ombre_sol(14, 0, 200, 16, 0.16),
                 rect(-160, -220, 320, 220, cylindre("#c92a2a", 0.2, 0.75)), planches(-160, -220, 320, 220, "#c92a2a", larg=20),
                 ombre_avancee(-160, -218, 320, 24, 0.26),
                 poly(toit, lineaire([(0, "#b03a3a"), (0.5, "#862e2e"), (1, "#5c1e1e")], 0, 0, 1, 1)),
                 tuiles(-190, -340, 380, 120, "#862e2e", poly(toit, "#000"), pas_=18),
                 chemin("M -190 -220 L 0 -340 L 190 -220", stroke="#f8f9fa", sw=7),
                 rect(-58, -148, 116, 148, "#f8f9fa"),
                 rect(-50, -140, 100, 140, radial([(0, "#5c1e1e"), (1, "#2b0d0d")], cy=0.8)),
                 rect(-46, -136, 92, 136, "#f8f9fa", opacity=0.15)], 620, y))
    S.add(rect(0, y, 800, 800 - y, terrain("#d8c27a")))
    S.add(barriere(170, y + 10, 1.0, largeur=360))


def graines(cx, cy, nb=12, graine=1, rx=80, ry=20):
    r = random.Random(graine)
    return g([ellipse(cx + r.uniform(-rx, rx), cy + r.uniform(-ry, ry), 5, 3, "#e67700", rot=r.uniform(0, 180)) for _ in range(nb)])


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    basse_cour(S, 620)
    S.add(poussin(400, 740, 2.6, expr="rire", ailes="haut"))
    S.add(coquille(250, 760, 1.6, rot=-10), coquille(560, 760, 1.4, rot=20, haut=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(coquille(130, 262, 1.0, rot=-10))
    S.add(poussin(220, 262, 1.3, expr="content", ailes="haut"))
    return S


def p01():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(poule_couve(400, 560, 1.6, expr="joie", bec_ouvert=True))
    S.add(oeuf(560, 700, 1.4))
    S.add(texte(400, 160, "Cot cot codet !", 60, "#e8590c", contour="#fff"))
    S.add(coq(140, 760, 1.4, expr="fier", regard=(1, 0)))
    return S


def p02():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(nid(400, 560, 1.7, devant=False))
    for k, x in enumerate([310, 355, 400, 445, 490]):
        S.add(oeuf(x + 20, 556, 0.85))
    for k, x in enumerate([290, 335, 380, 425, 470]):
        S.add(oeuf(x + 20, 590, 0.9))
    S.add(nid(400, 560, 1.7, devant=True))
    S.add(poule(650, 760, 1.4, expr="content", regard=(-1, 0.5)))
    S.add(fleche(570, 560, 500, 520, "#e8590c", 6, 22))
    S.add(texte(400, 200, "dix œufs !", 50, "#e8590c", contour="#fff"))
    return S


def p03():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(poule_couve(400, 580, 1.8, expr="dort"))
    S.add(texte(400, 150, "Chut… je couve.", 50, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(nid(400, 600, 1.7, devant=False))
    for k, x in enumerate([320, 400, 480]):
        S.add(oeuf(x, 610, 1.1, rot=(30 if k == 1 else 0)))
    S.add(nid(400, 600, 1.7, devant=True))
    S.add(poule(400, 460, 1.4, expr="concentre", regard=(0, 1)))
    S.add(fleche_ronde(400, 570))
    return S


def fleche_ronde(x, y):
    from sciences import fleche_courbe
    return fleche_courbe(f"M {x - 40} {y - 50} A 50 30 0 1 0 {x + 40} {y - 50}", (x + 40, y - 50), -60, "#e8590c", 5, 18)


def p05():
    S = Scene()
    fond(S, "#fff9db")
    for k, (x, st) in enumerate([(140, 1), (400, 2), (660, 3)]):
        S.add(oeuf_coupe(x, 400, 1.15, st))
    S.add(fleche(250, 400, 280, 400, "#e8590c", 6, 18), fleche(510, 400, 540, 400, "#e8590c", 6, 18))
    S.add(etiquette(140, 600, "le jaune", 32, "#e67700"), etiquette(400, 600, "il grandit", 32, "#e67700"),
          etiquette(660, 600, "il est prêt", 32, "#e67700"))
    S.cachette(410, 70, "air")
    return S


def p06():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(rect(100, 120, 600, 520, "#ffffff", rx=20, stroke="#ffc078", stroke_width=6))
    S.add(rect(100, 120, 600, 80, "#ff922b", rx=20), rect(100, 170, 600, 30, "#ff922b"))
    S.add(texte(400, 180, "21 jours", 48, "#ffffff"))
    for j in range(3):
        for i in range(7):
            x, y = 150 + i * 83, 260 + j * 120
            S.add(rect(x - 30, y - 40, 66, 90, "#fff4e6", rx=8))
            num = j * 7 + i + 1
            S.add(texte(x + 3, y - 10, str(num), 26, "#e8590c"))
            if num < 21:
                S.add(chemin(f"M {x - 14} {y + 10} L {x + 18} {y + 38} M {x + 18} {y + 10} L {x - 14} {y + 38}", stroke="#adb5bd", sw=4))
            else:
                S.add(oeuf(x + 3, y + 48, 0.7, brille=True))
    S.add(poussin(650, 760, 1.0, expr="joie", ailes="haut"))
    S.cachette(400, 70, "air")
    return S


def p07():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(nid(300, 640, 1.4, devant=False))
    S.add(oeuf(300, 650, 2.2))
    S.add(nid(300, 640, 1.4, devant=True))
    S.add(texte(300, 360, "piou ?", 50, "#e8590c", contour="#fff", rot=-8))
    S.add(poule(600, 740, 1.5, expr="content", bec_ouvert=True, regard=(-1, 0)))
    S.add(texte(600, 360, "cot cot…", 44, "#c92a2a", contour="#fff"))
    return S


def p08():
    S = Scene()
    fond(S, "#fff9db")
    m = [ellipse(0, 0, 150, 190, "#fff9f0", stroke="#e9ddc8", stroke_width=4)]
    m.append(chemin("M 40 -80 L 60 -100 L 70 -76 L 92 -86 L 86 -60 L 110 -56 L 90 -40 Z", "#343a40"))
    for a, L in [(-20, 60), (10, 50), (-50, 40)]:
        r = math.radians(a)
        m.append(trait(80, -70, 80 + math.cos(r) * L, -70 + math.sin(r) * L, "#adb5bd", 3))
    m.append(poly([(70, -80), (110, -66), (70, -56)], "#ff922b"))
    m.append(cercle(108, -66, 5, "#ffffff"))
    S.add(place(m, 360, 440))
    S.add(loupe(640, 220, 100, [rect(540, 120, 200, 200, "#fff9db"), place(poly([(-60, -30), (60, 0), (-60, 30)], "#ff922b"), 620, 220),
                                 cercle(676, 212, 12, "#ffffff", stroke="#adb5bd", stroke_width=2)], rot=130))
    S.add(etiquette(640, 360, "le diamant", 34, "#e67700"))
    S.add(texte(250, 720, "Toc ! Toc !", 60, "#e8590c", contour="#fff", rot=-6))
    S.cachette(410, 70, "air")
    return S


def p09():
    S = Scene()
    basse_cour(S, 560, interieur_=True)
    S.add(nid(400, 660, 1.6, devant=False))
    S.add(poussin_mouille(400, 690, 2.1))
    S.add(coquille(250, 670, 1.3, rot=-20), coquille(560, 660, 1.2, rot=30, haut=True))
    S.add(nid(400, 660, 1.6, devant=True))
    S.add(texte(400, 240, "Ouf !", 70, "#e8590c", contour="#fff"))
    return S


def p10():
    S = Scene()
    basse_cour(S, 560)
    S.add(poule(220, 740, 1.5, expr="content", regard=(1, 0.5)))
    S.add(graines(520, 720, 18, 2, 180, 40))
    for x, y, e in [(420, 720, "miam"), (540, 760, "rire"), (660, 700, "content"), (600, 650, "sourire")]:
        S.add(poussin(x, y, 0.8, expr=e, flip=x > 600))
    return S


def p11():
    S = Scene()
    nuit(S)
    etoiles(S, 30, 4, (0, 0, 800, 420))
    S.add(lune(640, 120, 40, croissant=True))
    S.add(rect(0, 560, 800, 240, "#6d4424"))
    S.add(poule(400, 740, 2.6, expr="dort"))
    for x, y in [(270, 610), (520, 610), (330, 690)]:
        S.add(place(poussin(0, 0, 1.0, expr="dort"), x, y, 0.55))
    S.add(zzz(560, 340, 1.2, "#ffe066"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("poussin-seul.svg", vignette),
    ("01-l-oeuf.svg", p01), ("02-dix-oeufs.svg", p02), ("03-elle-couve.svg", p03),
    ("04-retourner.svg", p04), ("05-dans-l-oeuf.svg", p05), ("06-vingt-et-un-jours.svg", p06),
    ("07-piou.svg", p07), ("08-toc-toc.svg", p08), ("09-il-sort.svg", p09),
    ("10-il-picore.svg", p10), ("11-sous-les-ailes.svg", p11),
]
