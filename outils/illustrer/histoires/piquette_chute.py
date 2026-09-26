"""Pourquoi tout tombe ? — la gravité.

Les positions successives d'un objet sont dessinées à intervalles de temps
égaux : une balle lancée ralentit en montant (les images se rapprochent),
un caillou qui tombe accélère (elles s'écartent). Sur la Lune, sans air, le
marteau et la plume restent côte à côte. La Lune « tombe » sans cesse vers
la Terre, mais sa vitesse la fait tourner autour.
"""
from base import *
from objets import *
from sciences import *

ID = "piquette-chute"
PIQUETTE = dict(acc=("noeud",), couleur_acc="#f06595")
GRAVITE = "#7048e8"


def piquette(x, y, s=1.0, **k):
    return perso("herisson", x, y, s, **{**PIQUETTE, **k})


def pre(S, graine=1, haut="#a5d8ff", bas="#e7f5ff", y=620):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 80)


def pommier(x, y, s=1.0):
    return arbre(x, y, s, "#51cf66", "#40c057", fruits="#fa5252")


def plume(x, y, s=1.0, rot=0, couleur="#e599f7"):
    m = [chemin("M 0 40 Q -26 0 0 -44 Q 26 0 0 40 Z", couleur), trait(0, 50, 0, -40, assombrir(couleur, 0.75), 3)]
    m += [trait(0, -30 + k * 14, (-1) ** k * 16, -38 + k * 14, "#fff", 2, opacity=0.6) for k in range(5)]
    return place(m, x, y, s, rot=rot)


def marteau(x, y, s=1.0, rot=0):
    return place([rect(-5, -10, 10, 70, "#a0693a", rx=4), rect(-30, -26, 60, 24, "#868e96", rx=4)], x, y, s, rot=rot)


def couverture():
    S = Scene()
    pre(S, 2)
    S.add(pommier(480, 660, 1.5))
    S.add(pomme(420, 470, 1.6), mouvement(425, 420, 1.0, rot=90))
    S.add(pomme(640, 580, 1.6), mouvement(645, 530, 1.0, rot=90))
    S.add(piquette(260, 760, 1.7, expr="surpris", regard=(1, -1), bras="joues"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(piquette(190, 262, 1.0, expr="content"))
    S.add(pomme(300, 70, 1.3))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(pommier(200, 660, 1.4))
    S.add(g([pomme(420, 470 - d, 1.8) for d in (130, 50)], opacity=0.25))
    S.add(pomme(420, 470, 1.8))
    S.add(fleche(490, 330, 490, 540, GRAVITE, 6))
    S.add(piquette(630, 770, 1.6, expr="surpris", regard=(-1, -1), flip=True))
    S.add(texte(650, 250, "?", 110, "#f76707", contour="#fff"))
    return S


def p02():
    S = Scene()
    pre(S, 2)
    S.add(soleil(680, 110, 45))
    # positions à intervalles de temps égaux : plus rapprochées en haut, où la balle va lentement
    haut, depart, N = 130, 560, 5
    for k in range(N + 1):
        y = haut + (depart - haut) * ((N - k) / N) ** 2
        S.add(ballon_jeu(350, y, 26, "#fa5252") if k in (0, N) else g(ballon_jeu(350, y, 26, "#fa5252"), opacity=0.3 + 0.1 * k))
        if k < N:
            yd = haut + (depart - haut) * ((k + 1) / N) ** 2
            S.add(g(ballon_jeu(450, yd, 26, "#fa5252"), opacity=0.8 - 0.1 * k))
    S.add(fleche(290, 540, 290, 170, "#495057", 5), fleche(510, 170, 510, 540, "#495057", 5))
    S.add(texte(400, 90, "elle ralentit…", 34, "#495057"))
    S.add(piquette(380, 780, 1.4, expr="rire", bras="haut", regard=(0, -1)))
    return S


def p03():
    S = Scene()
    pre(S, 3)
    S.add(pommier(580, 660, 1.3))
    S.add(chouette(620, 420, 1.0, expr="sourire", ailes="ouvertes", regard=(-1, 0)))
    S.add(piquette(250, 770, 1.5, expr="bouche_bee", regard=(1, -1)))
    for x, y in [(120, 200), (320, 250), (480, 180)]:
        S.add(fleche(x, y, x, y + 110, GRAVITE, 6))
    S.add(place(ellipse(0, 0, 24, 10, "#51cf66", rot=30), 120, 170))
    S.add(pomme(320, 220, 1.2))
    S.add(texte(250, 110, "gravité", 64, GRAVITE, contour="#fff"))
    return S


def p04():
    S = Scene()
    fond(S, "#0b1433")
    etoiles(S, 70, 4, (0, 0, 800, 800))
    cx, cy, R = 400, 420, 180
    S.add(cercle(cx, cy, R + 12, "#4dabf7", opacity=0.3), cercle(cx, cy, R, "#1c7ed6"))
    for px, py, rr in [(-60, -70, 70), (60, 40, 80), (-50, 100, 45)]:
        S.add(cercle(cx + px, cy + py, rr, "#51cf66"))
    enfants = [("claire", "blond", "#fa5252"), ("brune", "noir", "#fcc419"), ("doree", "brun", "#20c997"),
               ("foncee", "noir", "#f783ac"), ("rosee", "roux", "#4dabf7"), ("claire", "chatain", "#ff922b")]
    for k, (peau, ch, habit) in enumerate(enfants):
        a = k * 60
        ra = math.radians(a)
        x, y = cx + (R - 2) * math.sin(ra), cy - (R - 2) * math.cos(ra)
        S.add(place(enfant(0, 0, 0.56, peau=peau, cheveux=ch, habit=habit, expr="content", bras="haut"), x, y, rot=a))
        x2, y2 = cx + (R + 150) * math.sin(ra + 0.5), cy - (R + 150) * math.cos(ra + 0.5)
        x3, y3 = cx + (R + 60) * math.sin(ra + 0.5), cy - (R + 60) * math.cos(ra + 0.5)
        S.add(fleche(x2, y2, x3, y3, "#ffe066", 5))
    return S


def p05():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=640)
    S.add(table(260, 760, 260, 190, "#c68642"))
    S.add(piquette(260, 560, 1.2, expr="concentre", bras="ouverts"))
    # le caillou accélère : écarts de plus en plus grands
    for k in range(6):
        S.add(g(caillou(480, 440 + 10 * k * k, 0.9, "#868e96"), opacity=1 if k == 5 else 0.45))
    S.add(texte(470, 760, "toc !", 44, "#495057"))
    S.add(chemin("M 600 440 Q 660 480 600 520 Q 540 560 600 600", stroke="#e599f7", sw=3, stroke_dasharray="8 8"))
    S.add(plume(600, 600, 1.1, rot=-30))
    return S


def p06():
    S = Scene()
    fond(S, "#fff0f6")
    S.add(rect(0, 700, 800, 100, "#e8c39e"))
    S.add(chemin("M 250 140 Q 150 220 250 300 Q 350 380 250 460", stroke="#adb5bd", sw=3, stroke_dasharray="8 8"))
    S.add(place(poly([(-60, -8), (60, -18), (62, 8), (-58, 16)], "#fff", stroke="#ced4da", stroke_width=2), 250, 470, rot=-10))
    for k in range(6):
        y = 140 + 14 * k * k
        S.add(g([cercle(520, y, 30, "#fff", stroke="#ced4da", stroke_width=2), chemin(f"M 500 {y - 10} l 18 8 l 10 -12 l 12 16", stroke="#ced4da", sw=2)], opacity=1 if k == 5 else 0.45))
        S.add(g(caillou(640, y + 26, 0.8, "#868e96"), opacity=1 if k == 5 else 0.45))
    S.add(piquette(110, 780, 1.1, expr="bouche_bee", regard=(1, -1)))
    return S


def p07():
    S = Scene()
    fond(S, "#050814")
    etoiles(S, 50, 7, (0, 0, 800, 520))
    S.add(boule_eclairee(650, 130, 60, "#1c7ed6", "#050814", 180))
    S.add(chemin("M 0 500 Q 200 470 400 490 T 800 470 L 800 800 L 0 800 Z", "#adb5bd"))
    for x, y, r in [(120, 690, 40), (620, 720, 55), (380, 760, 30)]:
        S.add(ellipse(x, y, r, r * 0.3, "#868e96"))
    x, y, k = 400, 640, 1.7
    S.add(astronaute(x, y, k, expr="content", bras="ouverts"))
    (gx, gy), (dx_, dy_) = mains(x, y, k, "ouverts")
    # sans air : le marteau et la plume tombent ensemble, toujours à la même hauteur
    for yy, op in [(gy - 10, 0.35), (gy + 60, 0.55), (gy + 270, 1.0)]:
        S.add(g([marteau(gx - 10, yy, 1.0), plume(dx_ + 10, yy, 1.1)], opacity=op))
        S.add(trait(gx - 60, yy, dx_ + 60, yy, "#ffe066", 2, stroke_dasharray="6 8", opacity=0.6))
    S.add(texte(400, 160, "ensemble !", 60, "#ffe066"))
    return S


def p08():
    S = Scene()
    ciel(S, "#99e9f2", "#e3fafc")
    sol(S, 700, "#8ce99a")
    x, y = 440, 400
    k = 1.5
    S.add(chemin(f"M {x - 110 * k} {y - 60 * k} Q {x} {y - 190 * k} {x + 110 * k} {y - 60 * k} Q {x} {y - 90 * k} {x - 110 * k} {y - 60 * k} Z", "#f783ac"))
    for dx in (-110, -40, 40, 110):
        S.add(trait(x + dx * k, y - 62 * k, x, y + 10, "#495057", 2.5))
    S.add(perso("souris", x, y + 150, 0.75, expr="rire", bras="haut", couleur="#e9ecef", habit="#ffa8a8"))
    # l'air sous le mouchoir freine (flèches vers le haut) ; la gravité tire vers le bas
    for dx in (-90, 0, 90):
        S.add(fleche(x + dx, y - 30, x + dx, y - 110, "#1c7ed6", 6))
    S.add(fleche(x + 230, y - 20, x + 230, y + 120, GRAVITE, 7))
    S.add(texte(x + 230, y - 40, "gravité", 34, GRAVITE, contour="#fff"), texte(x - 250, y - 90, "air", 40, "#1c7ed6", contour="#fff"))
    S.add(piquette(150, 790, 1.2, expr="rire", bras="haut", regard=(1, -1)))
    return S


def pissenlit(x, y, s=1.0, graines=True):
    m = [trait(0, 0, 0, -200, "#51cf66", 6)]
    if graines:
        for k in range(24):
            a = k * 15
            ra = math.radians(a)
            m.append(trait(0, -200, math.cos(ra) * 40, -200 + math.sin(ra) * 40, "#dee2e6", 2))
            m.append(cercle(math.cos(ra) * 42, -200 + math.sin(ra) * 42, 4, "#fff"))
    m.append(cercle(0, -200, 8, "#adb5bd"))
    return place(m, x, y, s)


def graine_volante(x, y, s=1.0, rot=0):
    m = [trait(0, 0, 0, 30, "#adb5bd", 2), ellipse(0, 34, 3, 6, "#868e96")]
    for k in range(7):
        a = math.radians(-160 + k * 23)
        m.append(trait(0, 0, math.cos(a) * 20, math.sin(a) * 20, "#fff", 2))
    return place(m, x, y, s, rot=rot)


def p09():
    S = Scene()
    pre(S, 9)
    S.add(pissenlit(360, 720, 1.2, graines=False))
    S.add(g([place(graine_volante(0, 0, 1.4), 420 + k * 55, 420 - k * 30 + (k % 2) * 30) for k in range(7)]))
    S.add(rafales(470, 520, 0.8, "#ffffff"))
    S.add(piquette(220, 770, 1.5, expr="souffle", regard=(1, -1)))
    S.add(texte(560, 200, "Pfff !", 70, "#1c7ed6", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#ffec99", "#fff9db")
    sol(S, 700, "#8ce99a")
    S.add(poly([(180, 700), (560, 280), (600, 300), (240, 720)], "#fa5252"))
    S.add(rect(560, 240, 16, 460, "#1c7ed6"), rect(680, 240, 16, 460, "#1c7ed6"))
    for k in range(6):
        S.add(rect(560, 290 + k * 70, 136, 10, "#1c7ed6"))
    S.add(place(piquette(0, 0, 1.0, expr="rire", bras="haut"), 380, 470, rot=-45))
    S.add(mouvement(470, 340, 1.2, rot=-45))
    S.add(texte(200, 200, "Wiiiii !", 80, "#f76707", contour="#fff", rot=-8))
    return S


def p11():
    S = Scene()
    pre(S, 11)
    px, py, L = 400, 120, 420
    S.add(trait(180, 120, 620, 120, "#8d5524", 18), trait(200, 120, 120, 720, "#8d5524", 16), trait(600, 120, 680, 720, "#8d5524", 16))
    S.add(chemin(f"M {px - L * math.sin(0.6)} {py + L * math.cos(0.6)} A {L} {L} 0 0 0 {px + L * math.sin(0.6)} {py + L * math.cos(0.6)}", stroke="#495057", sw=3, stroke_dasharray="8 10"))
    for ang, op in [(-0.6, 0.3), (0.6, 1.0)]:
        x, y = px + L * math.sin(ang), py + L * math.cos(ang)
        S.add(g([trait(px, py, x - 36, y, "#495057", 3), trait(px, py, x + 36, y, "#495057", 3), rect(x - 50, y - 6, 100, 14, "#f76707", rx=6),
                 place(piquette(0, 0, 0.85, expr="rire" if op == 1 else "content", bras="haut"), x, y + 4)], opacity=op))
    return S


def p12():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(poly([(-40, 520), (150, 120), (330, 520)], "#868e96"), poly([(150, 120), (195, 215), (150, 190), (110, 210)], "#fff"))
    collines(S, 540, "#b2f2bb", graine=12)
    sol(S, 540, "#8ce99a", couleur2="#69db7c", y2=640)
    S.add(rect(0, 700, 800, 100, "#1c7ed6"))
    S.add(chemin("M 160 230 Q 200 420 320 520 Q 460 620 560 700 L 700 700 Q 520 600 380 520 Q 250 430 175 230 Z", "#4dabf7"))
    for k in range(4):
        S.add(fleche(210 + k * 110, 380 + k * 90, 250 + k * 110, 420 + k * 90, "#fff", 5))
    S.add(place([poly([(-40, 0), (40, 0), (28, 16), (-28, 16)], "#e8590c"), trait(0, 0, 0, -50, "#495057", 3), poly([(3, -48), (3, -6), (34, -6)], "#fff")], 680, 730))
    S.add(piquette(620, 590, 1.0, expr="content", regard=(-1, 0)))
    return S


def p13():
    S = Scene()
    interieur(S, "#f3f0ff", "#e8c39e", y=620)
    S.add(tour_cubes(300, 760, 1.4, 4, 13))
    for k, (x, y, rot, c) in enumerate([(360, 330, 20, "#4dabf7"), (440, 250, -30, "#cc5de8"), (520, 360, 50, "#ff922b")]):
        S.add(cube(x, y, 1.2, c, "", rot=rot))
    S.add(piquette(600, 780, 1.4, expr="oups", bras="joues", regard=(-1, -1)))
    S.add(texte(250, 160, "Patatras !", 70, "#c92a2a", contour="#fff", rot=-6))
    return S


def p14():
    S = Scene()
    interieur(S, "#ebfbee", "#e8c39e", y=620)
    tailles = [1.9, 1.6, 1.35, 1.1, 0.9, 0.7]
    y = 780
    cols = ["#ff6b6b", "#ffa94d", "#ffd43b", "#69db7c", "#4dabf7", "#cc5de8"]
    for k, t in enumerate(tailles):
        S.add(cube(320, y - 40 * t, t, cols[k], ""))
        y -= 80 * t
    S.add(etoile5(320, y - 30, 30, "#fcc419"))
    S.add(trait(320, 90, 320, 790, "#868e96", 2, stroke_dasharray="6 10"))
    S.add(piquette(600, 780, 1.5, expr="fier", bras="haut", regard=(-1, -1)))
    return S


def p15():
    S = Scene()
    fond(S, "#0b1433")
    etoiles(S, 70, 15, (0, 0, 800, 800))
    cx, cy, R = 400, 430, 250
    S.add(cercle(cx, cy, R, "none", stroke="#adb5bd", stroke_width=3, stroke_dasharray="10 12"))
    S.add(boule_eclairee(cx, cy, 90, "#1c7ed6", "#0b1433", 180))
    S.add(cercle(cx - 30, cy - 20, 34, "#51cf66", opacity=0.9))
    a = math.radians(-50)
    mx, my = cx + R * math.cos(a), cy + R * math.sin(a)
    tx, ty = -math.sin(a), math.cos(a)
    # sans la gravité, la Lune partirait tout droit (pointillés)
    S.add(trait(mx, my, mx - tx * 260, my - ty * 260, "#ffe066", 3, stroke_dasharray="6 10", opacity=0.7))
    S.add(fleche(mx, my, mx - tx * 150, my - ty * 150, "#ffe066", 7))
    S.add(fleche(mx, my, mx + (cx - mx) * 0.4, my + (cy - my) * 0.4, "#b197fc", 7))
    S.add(boule_eclairee(mx, my, 40, "#e9ecef", "#0b1433", 180))
    S.add(texte(mx - tx * 190 + 40, my - ty * 190, "vitesse", 32, "#ffe066"), texte(mx - 50, my + 130, "gravité", 32, "#b197fc"))
    return S


def p16():
    S = Scene()
    pre(S, 16, "#ff922b", "#ffe8cc", 640)
    S.add(cercle(640, 600, 60, "#ffd43b"))
    S.add(pommier(160, 690, 1.3))
    S.add(ellipse(430, 770, 170, 30, "#2f9e44"))
    S.add(piquette(430, 770, 1.6, expr="miam", bras="porte", objet=pomme(0, -72, 1.4)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("piquette-seule.svg", vignette),
    ("01-pomme.svg", p01), ("02-balle.svg", p02), ("03-gravite.svg", p03), ("04-terre-ronde.svg", p04),
    ("05-plume-caillou.svg", p05), ("06-papier.svg", p06), ("07-lune.svg", p07), ("08-parachute.svg", p08),
    ("09-pissenlit.svg", p09), ("10-toboggan.svg", p10), ("11-balancoire.svg", p11), ("12-riviere.svg", p12),
    ("13-patatras.svg", p13), ("14-equilibre.svg", p14), ("15-lune-tourne.svg", p15), ("16-merci.svg", p16),
]
