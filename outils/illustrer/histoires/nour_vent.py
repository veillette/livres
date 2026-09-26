"""Nour et le vent — l'air.

Dehors, le vent souffle toujours de la gauche vers la droite : les feuilles,
le linge, le fanion du bateau, le cerf-volant (qui vole du côté où va le
vent, face à Nour) vont tous dans le même sens. Un ballon qu'on lâche part
à l'opposé du jet d'air qui s'en échappe.
"""
from base import *
from objets import *
from sciences import *

ID = "nour-vent"
NOUR = dict(peau="brune", cheveux="noir", coiffure="longs", habit="#ff922b", robe=True)
PAPA = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#1c7ed6", jambes="#343a40", robe=False, barbe="#2b2b3a")
VENT = "#ffffff"


def nour(x, y, s=1.0, **k):
    return personne(x, y, s, **{**NOUR, **k})


def papa(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PAPA, **k})


def dehors(S, graine=1, haut="#99e9f2", bas="#e3fafc", y=600):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 90)


def feuilles_au_vent(S, graine, zone, nb=8):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for k in range(nb):
        S.add(ellipse(r.uniform(x0, x1), r.uniform(y0, y1), 16, 7, ["#40c057", "#fab005", "#f76707"][k % 3], rot=r.uniform(-40, 40)))


def arbre_penche(x, y, s=1.0):
    return place([chemin("M -16 0 Q -10 -80 20 -150", stroke="#8d5524", sw=30),
                  ellipse(70, -200, 100, 60, "#51cf66", rot=15), ellipse(110, -160, 60, 36, "#40c057", rot=15)], x, y, s)


def moulinet(x, y, s=1.0, rot=0, baton=True):
    """Moulinet en papier ; (x, y) = centre de l'hélice."""
    cols = ["#fa5252", "#fcc419", "#339af0", "#51cf66"]
    m = []
    if baton:
        m.append(rect(-6, 0, 12, 240, "#c68642", rx=5))
    ailes = [place(chemin("M 0 0 L 0 -90 Q 60 -70 70 -10 Z", c), 0, 0, rot=k * 90) for k, c in enumerate(cols)]
    m.append(place(ailes, 0, 0, rot=rot))
    m.append(cercle(0, 0, 10, "#fff", stroke="#adb5bd", stroke_width=3))
    return place(m, x, y, s)


def cerf_volant(x, y, s=1.0, rot=-20, couleur="#f06595"):
    m = [poly([(0, -90), (60, 0), (0, 110), (-60, 0)], couleur), poly([(0, -90), (60, 0), (0, 0)], "#fcc2d7"),
         poly([(0, 110), (-60, 0), (0, 0)], "#d6336c"), trait(0, -90, 0, 110, "#fff", 3), trait(-60, 0, 60, 0, "#fff", 3)]
    m.append(chemin("M 0 110 Q -30 150 0 190 Q 30 230 0 270", stroke="#495057", sw=3))
    for k, yy in enumerate((160, 220, 260)):
        m.append(place(poly([(-10, -8), (10, 8), (10, -8), (-10, 8)], ["#fcc419", "#339af0", "#51cf66"][k]), 0, yy))
    return place(m, x, y, s, rot=rot)


def couverture():
    S = Scene()
    dehors(S, 3)
    S.add(nuage(150, 140, 0.8), nuage(620, 220, 0.6))
    S.add(rafales(60, 260, 0.9, VENT))
    kx, ky = 590, 230
    S.add(trait(300, 510, kx - 20, ky + 100, "#495057", 3))
    S.add(cerf_volant(kx, ky, 1.2, -25))
    feuilles_au_vent(S, 3, (80, 400, 760, 600), 9)
    S.add(nour(270, 770, 1.7, expr="rire", bras="tient", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(moulinet(170, 110, 0.95, rot=20))
    S.add(rafales(250, 90, 0.5, "#74c0fc"))
    return S


def p01():
    S = Scene()
    dehors(S, 1)
    S.add(arbre_penche(160, 640, 1.2))
    feuilles_au_vent(S, 1, (260, 200, 760, 560), 10)
    S.add(rafales(80, 180, 0.9, VENT), rafales(420, 360, 0.7, VENT))
    S.add(nour(460, 770, 1.7, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(texte(620, 120, "?", 100, "#f76707", contour="#fff"))
    return S


def p02():
    S = Scene()
    dehors(S, 2)
    r = random.Random(2)
    for _ in range(90):
        S.add(cercle(r.uniform(0, 800), r.uniform(0, 620), r.uniform(3, 6), "#fff", opacity=0.7))
    S.add(papa(260, 770, 1.8, expr="content", bras="montre", regard=(1, -1)))
    S.add(nour(560, 770, 1.4, expr="bouche_bee", regard=(-1, -1)))
    S.add(texte(400, 120, "L'air est partout !", 56, "#0c8599", contour="#fff"))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff0f6", "#f3d9fa", y=600)
    x, y, s = 400, 780, 2.0
    S.add(nour(x, y, s, expr="souffle", bras="donne", regard=(1, 0)))
    (gx, gy), (dx_, dy_) = mains(x, y, s, "donne")
    for k in range(3):
        S.add(chemin(f"M {x + 30} {y - 240 + k * 14} q {30 + k * 10} -6 {dx_ - x - 50} {dy_ - y + 216 - k * 8}", stroke="#74c0fc", sw=4, opacity=0.8))
    S.add(texte(620, 250, "fff !", 70, "#1c7ed6", contour="#fff"))
    return S


def ballon(x, y, s=1.0, couleur="#fa5252", rot=0):
    """Ballon de baudruche sans fil ; (x, y) = centre."""
    return place([ellipse(0, 0, 70, 86, couleur), poly([(-10, 84), (10, 84), (0, 100)], assombrir(couleur, 0.8)),
                  ellipse(-24, -30, 14, 24, "#fff", opacity=0.4, rot=-20)], x, y, s, rot=rot)


def p04():
    S = Scene()
    dehors(S, 4, "#ffdeeb", "#fff0f6")
    S.add(nour(220, 770, 1.6, expr="souffle", bras="bouche", regard=(1, 0)))
    S.add(ballon(335, 560, 1.1, "#fa5252", rot=80))
    # ballon lâché : l'air sort vers l'arrière, le ballon file vers l'avant
    S.add(ballon(600, 220, 0.8, "#4dabf7", rot=45))
    S.add(g([trait(510 - k * 14, 300 + k * 18, 460 - k * 20, 350 + k * 22, "#74c0fc", 4, opacity=0.8) for k in range(3)]))
    S.add(chemin("M 380 470 Q 460 380 420 300 Q 400 240 500 280", stroke="#adb5bd", sw=3, stroke_dasharray="8 10"))
    S.add(fleche(640, 180, 720, 100, "#1c7ed6", 6))
    S.add(texte(620, 420, "Pfffrrr !", 56, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    dehors(S, 5)
    x, y, s = 250, 770, 1.6
    S.add(nour(x, y, s, expr="souffle", bras="tient", regard=(1, -1)))
    hx, hy = max(mains(x, y, s, "tient"), key=lambda p: p[0])
    S.add(trait(hx, hy, hx + 30, hy - 60, "#fab005", 6), cercle(hx + 38, hy - 76, 20, "none", stroke="#fab005", stroke_width=6))
    r = random.Random(5)
    for k in range(9):
        bx, by, br = hx + 80 + k * 50 + r.uniform(-20, 20), hy - 120 - r.uniform(0, 280), r.uniform(26, 56)
        S.add(cercle(bx, by, br, "#e7f5ff", opacity=0.35), cercle(bx, by, br, "none", stroke="#cc5de8", stroke_width=3, opacity=0.6),
              chemin(f"M {bx - br * 0.5} {by - br * 0.3} Q {bx - br * 0.3} {by - br * 0.6} {bx} {by - br * 0.65}", stroke="#fff", sw=4))
    return S


def p06():
    S = Scene()
    interieur(S, "#e6fcf5", "#e8c39e", y=600)
    S.add(table(400, 790, 600, 110, "#c68642"))
    # coupe : bassine d'eau, verre retourné enfoncé ; l'air emprisonné garde le mouchoir au sec
    S.add(rect(160, 330, 480, 350, "#74c0fc", rx=10, opacity=0.9))
    S.add(rect(150, 280, 500, 400, "none", rx=12, stroke="#adb5bd", stroke_width=6))
    S.add(rect(290, 250, 220, 320, "#e7f5ff", opacity=0.9))
    S.add(rect(290, 540, 220, 30, "#74c0fc", opacity=0.9))
    S.add(rect(290, 250, 220, 320, "none", stroke="#868e96", stroke_width=5))
    S.add(rect(300, 260, 200, 36, "#ffc9c9", rx=6))
    S.add(texte(400, 420, "air", 60, "#1971c2"))
    S.add(texte(400, 180, "Sec !", 70, "#2f9e44", contour="#fff"))
    return S


def p07():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600)
    S.add(table(330, 790, 500, 140, "#c68642"))
    contenu = g([cercle(-24 + (k % 3) * 24, -40 - k * 26, 11 + (k % 2) * 5, "#ffffff", stroke="#74c0fc", stroke_width=3) for k in range(7)])
    S.add(verre(330, 650, 170, 260, contenu=contenu, niveau=0.75, couleur_contenu="#f8f9fa"))
    S.add(trait(360, 380, 420, 620, "#f06595", 12))
    S.add(nour(620, 790, 1.5, expr="souffle", bras="bas", regard=(-1, 0), flip=True))
    S.add(texte(160, 250, "glou glou !", 56, "#1c7ed6", contour="#fff"))
    return S


def p08():
    S = Scene()
    dehors(S, 8)
    S.add(rafales(40, 200, 0.8, VENT))
    S.add(papa(560, 770, 1.7, expr="content", bras="montre", regard=(-1, 0), flip=True))
    S.add(nour(250, 770, 1.5, expr="rire", bras="tient", regard=(1, -1)))
    hx, hy = max(mains(250, 770, 1.5, "tient"), key=lambda p: p[0])
    S.add(moulinet(hx + 10, hy - 180, 1.0, rot=30))
    S.add(fleche_courbe(f"M {hx + 90} {hy - 280} A 110 110 0 0 1 {hx + 120} {hy - 150}", (hx + 120, hy - 150), 100, "#495057", 4))
    return S


def p09():
    S = Scene()
    dehors(S, 9, "#74c0fc", "#e7f5ff")
    S.add(nuage(160, 120, 0.8), nuage(520, 90, 0.6))
    # le vent souffle vers la droite et soulève le cerf-volant, qui vole face à Nour, du côté où va le vent
    for y in (330, 430):
        S.add(fleche(80, y, 260, y, "#fff", 6))
    kx, ky = 600, 220
    S.add(trait(220, 560, kx - 10, ky + 110, "#495057", 3))
    S.add(cerf_volant(kx, ky, 1.1, -30))
    S.add(fleche(kx - 100, ky + 150, kx - 60, ky + 60, "#fff", 5))
    S.add(nour(200, 770, 1.6, expr="rire", bras="tient", regard=(1, -1)))
    return S


def voilier(x, y, s=1.0):
    """Voilier poussé par un vent venant de la gauche ; (x, y) = ligne d'eau au milieu."""
    m = [chemin("M -150 -20 L 150 -20 L 110 30 L -120 30 Z", "#a0693a"), rect(-6, -300, 12, 280, "#495057"),
         chemin("M 6 -290 Q 150 -170 6 -40 Z", "#fff", stroke="#dee2e6", sw=3),
         chemin("M -6 -250 Q -60 -150 -6 -50 L -110 -50 Z", "#fff9db", stroke="#dee2e6", sw=3),
         poly([(6, -300), (70, -290), (6, -280)], "#fa5252")]
    return place(m, x, y, s)


def p10():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 480, "#b2f2bb", graine=10)
    eau(S, 480, "#1c7ed6", "#4dabf7")
    for y in (180, 260):
        S.add(rafales(50, y, 0.7, VENT))
    S.add(voilier(430, 600, 1.2))
    S.add(g([trait(230 - k * 50, 640 + k * 8, 180 - k * 50, 640 + k * 8, "#e7f5ff", 5) for k in range(3)]))
    S.add(fleche(600, 720, 740, 720, "#fff", 7))
    return S


def eolienne(x, y, s=1.0, rot=0):
    m = [poly([(-8, -300), (8, -300), (14, 0), (-14, 0)], "#f1f3f5"),
         place([place(chemin("M -8 0 Q -14 -80 0 -150 Q 14 -80 8 0 Z", "#fff", stroke="#dee2e6", sw=2), 0, 0, rot=k * 120) for k in range(3)], 0, -300, rot=rot),
         cercle(0, -300, 12, "#dee2e6")]
    return place(m, x, y, s)


def p11():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rafales(20, 140, 0.6, VENT))
    S.add(chemin("M -40 560 Q 300 300 840 520 L 840 800 L -40 800 Z", "#8ce99a"))
    for x, y, s, r in [(280, 420, 1.1, 10), (470, 400, 1.0, 50), (650, 450, 0.9, 80)]:
        S.add(eolienne(x, y, s, r))
    S.add(chemin("M 280 420 Q 250 600 170 700", stroke="#495057", sw=3, stroke_dasharray="6 6"))
    S.add(maison(140, 760, 0.7, lumiere=True), maison(620, 760, 0.6, lumiere=True))
    S.add(eclat(145, 640, 0.8, "#fcc419"))
    return S


def p12():
    S = Scene()
    dehors(S, 12)
    S.add(trait(120, 260, 700, 250, "#495057", 4), rect(110, 250, 16, 450, "#c68642"), rect(694, 240, 16, 460, "#c68642"))
    for x, c, w in [(180, "#fff", 170), (380, "#ffc9c9", 150), (560, "#a5d8ff", 130)]:
        S.add(chemin(f"M {x} 258 L {x + w} 256 Q {x + w + 40} 360 {x + w + 70} 450 Q {x + 40 + w / 2} 420 {x + 40} 460 Q {x + 10} 360 {x} 258 Z", c, stroke="#dee2e6", sw=2))
        S.add(g([rect(x + 6, 248, 10, 22, "#fab005", rx=3), rect(x + w - 10, 246, 10, 22, "#fab005", rx=3)]))
    S.add(rafales(40, 470, 0.8, VENT))
    S.add(texte(400, 150, "Clac ! Clac !", 64, "#0c8599", contour="#fff"))
    return S


def goeland(x, y, s=1.0):
    return place([chemin("M -90 10 Q -50 -30 0 0 Q 50 -30 90 10 Q 50 -10 0 10 Q -50 -10 -90 10 Z", "#495057"),
                  ellipse(0, 6, 16, 10, "#f8f9fa")], x, y, s)


def p13():
    S = Scene()
    ciel(S, "#ff922b", "#ffe8cc")
    S.add(cercle(400, 420, 90, "#ffd43b"))
    collines(S, 620, "#ffc078", graine=13)
    sol(S, 620, "#fab005")
    for x, y, s in [(220, 250, 1.2), (500, 180, 0.9), (620, 330, 0.7)]:
        S.add(goeland(x, y, s))
    for x in (220, 520):
        S.add(g([chemin(f"M {x + dx} 600 q -20 -80 0 -160 q 20 -80 0 -160", stroke="#fff", sw=3, opacity=0.5, stroke_dasharray="4 10") for dx in (-30, 30)]))
        S.add(fleche(x, 380, x, 320, "#fff", 4))
    return S


def p14():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 660, "#b2f2bb", graine=14)
    sol(S, 660, "#8ce99a")
    S.add(nuage(140, 130, 0.8), nuage(680, 200, 0.6))
    x, y = 400, 330
    cols = ["#fa5252", "#fcc419", "#fa5252", "#fcc419", "#fa5252"]
    cid = uid("m")
    forme = chemin(f"M {x - 170} {y} Q {x - 170} {y - 200} {x} {y - 200} Q {x + 170} {y - 200} {x + 170} {y} Q {x + 150} {y + 120} {x + 50} {y + 180} L {x - 50} {y + 180} Q {x - 150} {y + 120} {x - 170} {y} Z", "#000")
    S.defs.append(el("clipPath", forme, id=cid))
    S.add(g([rect(x - 170 + k * 68, y - 200, 68, 400, c) for k, c in enumerate(cols)], clip_path=f"url(#{cid})"))
    # l'air chauffé par le brûleur monte et soulève le ballon
    for dx in (-60, 0, 60):
        S.add(fleche(x + dx, y + 110, x + dx, y - 40, "#fff", 5, opacity=0.9))
    S.add(poly([(x - 16, y + 200), (x, y + 150), (x + 16, y + 200)], "#ff922b"), poly([(x - 8, y + 200), (x, y + 170), (x + 8, y + 200)], "#ffe066"))
    S.add(trait(x - 50, y + 180, x - 40, y + 230, "#495057", 3), trait(x + 50, y + 180, x + 40, y + 230, "#495057", 3))
    S.add(rect(x - 44, y + 225, 88, 60, "#a0693a", rx=8))
    S.add(texte(620, 420, "air chaud", 40, "#c92a2a", contour="#fff"))
    return S


def p15():
    S = Scene()
    ciel(S, "#495057", "#adb5bd")
    S.add(nuage(200, 110, 1.4, "#868e96", ombre="#495057"), nuage(580, 90, 1.2, "#868e96", ombre="#495057"))
    collines(S, 620, "#74a57f", graine=15)
    sol(S, 620, "#8fb996")
    S.add(g([trait(x, y, x + 30, y + 26, "#a5d8ff", 3, opacity=0.8) for x, y in [(random.Random(k).uniform(0, 800), random.Random(k + 99).uniform(0, 600)) for k in range(50)]]))
    S.add(arbre_penche(110, 640, 1.0), maison(660, 700, 0.7, lumiere=True))
    feuilles_au_vent(S, 15, (240, 250, 760, 560), 10)
    S.add(rafales(40, 320, 0.8, VENT))
    x, y, s = 380, 770, 1.6
    S.add(nour(x, y, s, expr="surpris", bras="tient", regard=(1, -1)))
    hx, hy = max(mains(x, y, s, "tient"), key=lambda p: p[0])
    # parapluie retourné par le vent
    S.add(place([trait(0, 0, 0, -150, "#495057", 6), chemin("M -110 -250 Q -60 -150 0 -150 Q 60 -150 110 -250 Q 0 -190 -110 -250 Z", "#fcc419")], hx, hy + 20, 1.0, rot=20))
    return S


def p16():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=600, papier="#ffe8cc")
    for k in range(10):
        S.add(poly([(40 + k * 75, 40), (110 + k * 75, 40), (75 + k * 75, 100)], ["#fa5252", "#fcc419", "#51cf66", "#339af0", "#cc5de8"][k % 5]))
    S.add(trait(20, 40, 790, 40, "#495057", 3))
    S.add(table(460, 790, 460, 150, "#c68642", nappe="#fff"))
    S.add(gateau(460, 632, 1.6, bougies=0))
    for k in range(7):
        bx = 380 + k * 27
        S.add(rect(bx - 5, 470, 10, 50, ["#fa5252", "#339af0", "#fcc419", "#51cf66", "#cc5de8", "#ff922b", "#f06595"][k], rx=3))
        S.add(chemin(f"M {bx} 470 q 14 -6 26 -16", stroke="#adb5bd", sw=3, opacity=0.7))
    S.add(nour(170, 790, 1.5, expr="souffle", bras="bas", regard=(1, 0)))
    S.add(g([chemin(f"M 230 {540 + k * 16} q 60 -6 120 -20", stroke="#74c0fc", sw=4, opacity=0.8) for k in range(3)]))
    S.add(texte(620, 300, "Bravo !", 64, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("moulinet-seul.svg", vignette),
    ("01-le-vent.svg", p01), ("02-l-air.svg", p02), ("03-souffle.svg", p03), ("04-ballon.svg", p04),
    ("05-bulles.svg", p05), ("06-verre-retourne.svg", p06), ("07-paille.svg", p07), ("08-moulinet.svg", p08),
    ("09-cerf-volant.svg", p09), ("10-voilier.svg", p10), ("11-eoliennes.svg", p11), ("12-linge.svg", p12),
    ("13-oiseaux.svg", p13), ("14-montgolfiere.svg", p14), ("15-tempete.svg", p15), ("16-bougies.svg", p16),
]
