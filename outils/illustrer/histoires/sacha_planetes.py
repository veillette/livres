"""Sacha chez les planètes — le système solaire.

Chaque planète est éclairée du côté du Soleil (à gauche). Détails fidèles :
calottes de glace de la Terre et de Mars, tache rouge de Jupiter dans
l'hémisphère sud, division de Cassini dans les anneaux de Saturne, Uranus
couchée avec ses anneaux presque verticaux, Neptune bleu foncé avec sa tache.
"""
from base import *
from objets import *
from sciences import *

ID = "sacha-planetes"
SACHA = dict(peau="brune", cheveux="noir", coiffure="courts")
ESPACE = "#0b1433"


def espace(S, graine=1, haut=ESPACE, bas="#1b2459", nb=80):
    ciel(S, haut, bas)
    etoiles(S, nb, graine, (0, 0, 800, 800), "#fff9db")


def visage_sacha(expr="content"):
    return place(personne(0, 0, 0.5, expr=expr, **SACHA), 0, -20 + 150 * 0.5 - 4)


def fusee_sacha(x, y, s=1.0, rot=0, flamme=True, expr="content"):
    return fusee(x, y, s, rot, flamme, passager=visage_sacha(expr))


def sacha(x, y, s=1.0, **k):
    return astronaute(x, y, s, **{**SACHA, **k})


def terre(S, x, y, r, lumiere=180, nuages=True):
    m = [planete(S, x, y, r, ("#1c7ed6", "#1971c2"), lumiere=lumiere, ombre_op=0.0, calottes=True)]
    cid = uid("t")
    m.append(el("clipPath", cercle(x, y, r, "#000"), id=cid))
    det = [ellipse(x - r * 0.3, y - r * 0.25, r * 0.35, r * 0.45, "#51cf66", rot=20), ellipse(x + r * 0.35, y + r * 0.2, r * 0.3, r * 0.4, "#40c057", rot=-15),
           ellipse(x - r * 0.1, y + r * 0.55, r * 0.2, r * 0.12, "#51cf66")]
    if nuages:
        det += [ellipse(x - r * 0.4, y + r * 0.1, r * 0.3, r * 0.07, "#fff", opacity=0.85), ellipse(x + r * 0.2, y - r * 0.45, r * 0.35, r * 0.06, "#fff", opacity=0.85),
                ellipse(x + r * 0.1, y + r * 0.7, r * 0.25, r * 0.05, "#fff", opacity=0.85)]
    gid = uid("o")
    S.defs.append(el("linearGradient", el("stop", offset="0", stop_color="#000", stop_opacity="0") + el("stop", offset="0.45", stop_color="#000", stop_opacity="0.3")
                     + el("stop", offset="1", stop_color="#000", stop_opacity="0.65"), id=gid, x1=0, y1=0, x2=1, y2=0))
    det.append(g(rect(x - r * 0.25, y - r - 2, r * 1.25 + 2, 2 * r + 4, f"url(#{gid})"), transform=f"rotate({n(lumiere + 180)} {n(x)} {n(y)})"))
    m.append(g(det, clip_path=f"url(#{cid})"))
    m.append(cercle(x, y, r + 6, "none", stroke="#74c0fc", stroke_width=5, opacity=0.4))
    return g(m)


def jupiter(S, x, y, r):
    bandes = [(-0.75, 0.12, "#c9a27a"), (-0.45, 0.13, "#b07a4f"), (-0.12, 0.1, "#e8cfa9"), (0.15, 0.14, "#a86a3f"), (0.5, 0.12, "#c9a27a"), (0.8, 0.1, "#b07a4f")]
    return planete(S, x, y, r, ("#f1dcc0", "#b07a4f"), bandes=bandes, tache=(0.3, 0.32, 0.22, 0.12, "#d9480f"))


def saturne(S, x, y, r, inc=-18):
    bandes = [(-0.5, 0.12, "#e9d8a6"), (0.0, 0.1, "#f3e3b5"), (0.45, 0.12, "#d9c08b")]
    return planete(S, x, y, r, ("#f5e6b8", "#d9c08b"), bandes=bandes, anneaux=(inc, "#e9d8a6"))


def uranus(S, x, y, r):
    # Uranus est couchée : son axe et ses anneaux sont presque verticaux
    return planete(S, x, y, r, ("#99e9f2", "#66d9e8"), anneaux=(82, "#dee2e6", True))


def neptune(S, x, y, r):
    return planete(S, x, y, r, ("#364fc7", "#1c2a8a"), bandes=[(-0.3, 0.06, "#4c6ef5"), (0.35, 0.05, "#4c6ef5")],
                   tache=(-0.1, 0.25, 0.18, 0.1, "#1c2a8a"))


def couverture():
    S = Scene()
    espace(S, 1)
    S.add(saturne(S, 600, 200, 80))
    S.add(planete(S, 140, 620, 50, ("#e8590c", "#c2410c"), calottes=True, crateres=3))
    S.add(terre(S, 660, 640, 70))
    S.add(fusee_sacha(360, 420, 1.35, rot=35, expr="rire"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fusee(200, 120, 0.62, 35, passager=visage_sacha()))
    S.add(etoile5(70, 60, 12, "#fcc419"), etoile5(340, 210, 10, "#fcc419"))
    return S


def p01():
    S = Scene()
    interieur(S, "#5c7cfa", "#364fc7", y=620)
    S.add(fenetre(80, 90, 180, 170, "#1c2a52", nuit_=True))
    S.add(texte(130, 470, "3", 90, "#ffe066"), texte(210, 520, "2", 80, "#ffe066"), texte(280, 570, "1", 70, "#ffe066"))
    S.add(g([trait(470, 700, 430, 790, "#adb5bd", 10), trait(630, 700, 670, 790, "#adb5bd", 10)]))
    S.add(fusee_sacha(550, 480, 1.4, flamme=False, expr="content"))
    return S


def p02():
    S = Scene()
    ciel(S, "#1c2a52", "#74c0fc")
    etoiles(S, 25, 2, (0, 0, 800, 250))
    # la fusée pousse ses gaz vers le bas… et monte
    S.add(fusee_sacha(400, 330, 1.4, expr="rire"))
    for x, y, s in [(190, 690, 1.6), (400, 730, 2.0), (620, 690, 1.6), (300, 620, 1.2), (520, 630, 1.3)]:
        S.add(nuage(x, y, s))
    S.add(fleche(620, 520, 620, 620, "#ff922b", 7), fleche(170, 320, 170, 190, "#fff", 7))
    S.add(texte(560, 110, "Vrrroom !", 64, "#ffe066", contour="#1c2a52"))
    return S


def p03():
    S = Scene()
    espace(S, 3)
    S.add(terre(S, 380, 440, 260))
    S.add(fusee_sacha(680, 150, 0.7, rot=-40, flamme=False))
    return S


def p04():
    S = Scene()
    fond(S, "#050814")
    etoiles(S, 40, 4, (0, 0, 800, 460), "#fff9db")
    S.add(terre(S, 640, 130, 60))
    S.add(chemin("M 0 470 Q 250 430 500 470 T 800 450 L 800 800 L 0 800 Z", "#ced4da"))
    for x, y, r in [(110, 560, 60), (560, 620, 80), (330, 740, 40), (730, 520, 30)]:
        S.add(ellipse(x, y, r, r * 0.3, "#adb5bd"), ellipse(x, y - 4, r * 0.8, r * 0.2, "#868e96"))
    for k in range(5):
        S.add(ellipse(170 + k * 60, 720 - k * 30 - (k % 2) * 16, 14, 7, "#868e96"))
    S.add(fusee(140, 330, 0.8, flamme=False))
    S.add(sacha(470, 690, 1.3, expr="rire", bras="salut"))
    return S


def p05():
    S = Scene()
    fond(S, "#050814")
    etoiles(S, 40, 5, (0, 0, 800, 800), "#fff9db")
    S.add(cercle(250, 400, 400, degrade_radial(S, "#ffe066", "#ffe06600")))
    S.add(cercle(220, 400, 300, "#fd7e14"), cercle(220, 400, 270, "#ff922b"), cercle(180, 360, 190, "#ffa94d", opacity=0.7))
    r = random.Random(5)
    for _ in range(25):
        S.add(cercle(220 + r.uniform(-230, 230), 400 + r.uniform(-230, 230), r.uniform(8, 18), "#fd7e14", opacity=0.6))
    S.add(chemin("M 480 250 Q 580 200 560 320", stroke="#ff6b6b", sw=16), chemin("M 440 560 Q 560 600 520 500", stroke="#ff6b6b", sw=12))
    S.add(fusee_sacha(650, 560, 0.75, rot=-60, expr="oups"))
    S.add(texte(620, 740, "Trop chaud !", 50, "#ffe066"))
    return S


def p06():
    S = Scene()
    espace(S, 6)
    S.add(cercle(-120, 400, 330, "#ff922b"), cercle(-120, 400, 360, "#ffe066", opacity=0.3))
    S.add(planete(S, 440, 420, 130, ("#adb5bd", "#868e96"), crateres=10, lumiere=180, graine=6))
    S.add(texte(440, 640, "Mercure", 56, "#fff"))
    S.add(fusee_sacha(680, 170, 0.6, rot=-30, flamme=False))
    return S


def p07():
    S = Scene()
    espace(S, 7)
    S.add(planete(S, 380, 400, 230, ("#f3d99b", "#e9c46a"), bandes=[(-0.5, 0.1, "#fff3bf"), (-0.05, 0.12, "#e9c46a"), (0.4, 0.1, "#fff3bf")]))
    S.add(texte(380, 720, "Vénus", 56, "#fff"))
    S.add(fusee_sacha(680, 620, 0.6, rot=45))
    return S


def robot(x, y, s=1.0):
    m = [rect(-80, -70, 160, 50, "#dee2e6", rx=8), rect(-60, -40, 120, 16, "#adb5bd"),
         cercle(-56, -10, 22, ENCRE), cercle(0, -10, 22, ENCRE), cercle(56, -10, 22, ENCRE),
         rect(30, -140, 10, 72, "#adb5bd"), rect(10, -160, 50, 26, "#868e96", rx=6), cercle(24, -147, 6, "#4dabf7"), cercle(46, -147, 6, "#4dabf7"),
         rect(-70, -110, 60, 40, "#1c7ed6", rx=4)]
    return place(m, x, y, s)


def p08():
    S = Scene()
    ciel(S, "#e8b28a", "#f7d6b8")
    S.add(cercle(640, 120, 30, "#fff9db", opacity=0.9))
    S.add(poly([(-20, 470), (160, 330), (340, 470)], "#c2410c"), poly([(420, 470), (620, 360), (820, 470)], "#d9480f"))
    S.add(chemin("M 0 460 Q 400 430 800 460 L 800 800 L 0 800 Z", "#e8590c"))
    r = random.Random(8)
    for _ in range(18):
        S.add(ellipse(r.uniform(0, 800), r.uniform(500, 790), r.uniform(10, 26), r.uniform(6, 14), "#a33b0a"))
    S.add(robot(220, 650, 1.1))
    S.add(sacha(560, 720, 1.25, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(texte(400, 150, "Mars", 64, "#fff", contour="#c2410c"))
    return S


def p09():
    S = Scene()
    espace(S, 9)
    r = random.Random(9)
    for _ in range(26):
        x, y = r.uniform(0, 800), r.uniform(0, 800)
        if abs(x - 400) < 110 and abs(y - 420) < 110:
            continue
        rr = r.uniform(14, 44)
        S.add(place(chemin(f"M {-rr} 0 Q {-rr} {-rr} 0 {-rr * 0.9} Q {rr} {-rr} {rr * 0.9} 0 Q {rr} {rr} 0 {rr * 0.9} Q {-rr} {rr} {-rr} 0 Z", "#868e96"), x, y, rot=r.uniform(0, 90)))
        S.add(cercle(x + rr * 0.2, y - rr * 0.2, rr * 0.18, "#495057", opacity=0.6))
    S.add(chemin("M 80 740 Q 250 520 400 430 T 740 80", stroke="#ffe066", sw=4, stroke_dasharray="10 12"))
    S.add(fusee_sacha(400, 420, 0.8, rot=40, expr="concentre"))
    return S


def p10():
    S = Scene()
    espace(S, 10)
    S.add(jupiter(S, 400, 420, 290))
    S.add(terre(S, 730, 100, 26))
    S.add(texte(730, 160, "la Terre", 26, "#fff"), texte(400, 80, "Jupiter", 56, "#fff"))
    return S


def p11():
    S = Scene()
    espace(S, 11)
    S.add(saturne(S, 400, 420, 170))
    S.add(texte(400, 720, "Saturne", 56, "#fff"))
    S.add(fusee_sacha(120, 640, 0.5, rot=30))
    return S


def p12():
    S = Scene()
    espace(S, 12)
    S.add(uranus(S, 400, 400, 170))
    S.add(fleche_courbe("M 400 150 A 250 60 0 0 1 650 190", (650, 190), 20, "#fff", 5))
    S.add(texte(400, 720, "Uranus", 56, "#fff"))
    S.add(fusee_sacha(680, 620, 0.5, rot=-30))
    return S


def p13():
    S = Scene()
    espace(S, 13, "#050814", "#0b1433")
    S.add(neptune(S, 400, 400, 190))
    for k in range(4):
        S.add(chemin(f"M {150 + k * 30} {250 + k * 90} q 120 -30 240 0 t 240 0", stroke="#a5d8ff", sw=5, opacity=0.5))
    S.add(texte(400, 720, "Neptune", 56, "#fff"), texte(650, 150, "Brrr !", 50, "#a5d8ff"))
    S.add(fusee_sacha(120, 160, 0.5, rot=30, expr="oups"))
    return S


def p14():
    S = Scene()
    espace(S, 14)
    S.add(cercle(-230, 400, 300, "#ff922b"), cercle(-230, 400, 330, "#ffe066", opacity=0.3))
    # dans l'ordre depuis le Soleil ; tailles relatives respectées à peu près, pas les distances
    noms = [("Mercure", 9), ("Vénus", 16), ("Terre", 17), ("Mars", 11), ("Jupiter", 62), ("Saturne", 52), ("Uranus", 28), ("Neptune", 27)]
    xs = [105, 160, 220, 275, 375, 520, 645, 728]
    for k, ((nom, r), x) in enumerate(zip(noms, xs)):
        S.add(cercle(-230, 400, 230 + x, "none", stroke="#fff", stroke_width=1.5, opacity=0.15))
        if nom == "Terre":
            S.add(terre(S, x, 400, r, nuages=False))
        elif nom == "Jupiter":
            S.add(jupiter(S, x, 400, r))
        elif nom == "Saturne":
            S.add(saturne(S, x, 400, r * 0.8))
        elif nom == "Uranus":
            S.add(uranus(S, x, 400, r * 0.8))
        elif nom == "Neptune":
            S.add(neptune(S, x, 400, r))
        else:
            c = {"Mercure": "#adb5bd", "Vénus": "#f3d99b", "Mars": "#e8590c"}[nom]
            S.add(planete(S, x, 400, r, (c, c)))
        y = 400 + (r + 40) * (1 if k % 2 == 0 else -1) + (10 if k % 2 == 0 else 0)
        S.add(texte(x, y, nom, 27, "#fff"))
    return S


def p15():
    S = Scene()
    espace(S, 15, "#050814", "#0b1433", nb=200)
    S.add(place(ellipse(0, 0, 520, 90, "#e5dbff", opacity=0.12), 400, 400, rot=-25))
    S.add(place(ellipse(0, 0, 420, 40, "#fff", opacity=0.1), 400, 400, rot=-25))
    r = random.Random(15)
    for _ in range(40):
        S.add(etoile5(r.uniform(0, 800), r.uniform(0, 800), r.uniform(4, 10), r.choice(["#fff9db", "#d0ebff", "#ffe3e3"])))
    S.add(fusee_sacha(260, 560, 0.7, rot=60, expr="bouche_bee"))
    return S


def p16():
    S = Scene()
    interieur(S, "#4c6ef5", "#364fc7", y=620)
    S.add(fenetre(470, 80, 190, 170, "#1c2a52", nuit_=True))
    S.add(lit(330, 780, 440, "#fff", "#339af0"))
    S.add(cercle(200, 640, 46, "#a86a3f"), chemin("M 158 628 Q 170 590 200 590 Q 236 590 246 626 Q 200 610 158 628 Z", "#2b2b3a"))
    S.add(oeil(186, 640, "fermes"), oeil(214, 640, "fermes"), bouche(200, 656, "petit_sourire"))
    S.add(zzz(250, 560, 1.0, "#e5dbff"))
    S.add(fusee(680, 690, 0.45, flamme=False))
    S.add(rect(530, 560, 60, 12, "#c68642", rx=4), trait(560, 560, 560, 620, "#c68642", 6), rect(535, 612, 50, 10, "#c68642", rx=4))
    S.add(terre(S, 560, 525, 32, nuages=True))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fusee-seule.svg", vignette),
    ("01-depart.svg", p01), ("02-decollage.svg", p02), ("03-terre.svg", p03), ("04-lune.svg", p04),
    ("05-soleil.svg", p05), ("06-mercure.svg", p06), ("07-venus.svg", p07), ("08-mars.svg", p08),
    ("09-asteroides.svg", p09), ("10-jupiter.svg", p10), ("11-saturne.svg", p11), ("12-uranus.svg", p12),
    ("13-neptune.svg", p13), ("14-systeme-solaire.svg", p14), ("15-etoiles.svg", p15), ("16-retour.svg", p16),
]
