"""Gaston le glaçon — les états de l'eau.

Détails fidèles : un glaçon flotte, mais presque tout entier sous la surface
(environ 9/10) ; la vapeur d'eau est invisible (juste au bec de la bouilloire
il n'y a « rien », le petit nuage blanc apparaît un peu plus loin, quand la
vapeur redevient de minuscules gouttes) ; sous la glace du lac, l'eau du fond
reste à 4 °C ; un flocon de neige a six branches.
"""
from base import *
from objets import *
from sciences import *

ID = "gaston-glacon"
FROID, CHAUD = "#1c7ed6", "#f03e3e"


def thermometre(x, y, h=200, niveau=0.5, texte_=None, s=1.0, couleur="#fa5252"):
    """Thermomètre ; (x, y) = bas du réservoir."""
    m = [rect(-14, -h, 28, h, "#fff", rx=14, stroke="#adb5bd", stroke_width=4), cercle(0, 0, 24, couleur),
         rect(-6, -h * niveau, 12, h * niveau, couleur, rx=6)]
    m += [trait(8, -h * k / 6, 14, -h * k / 6, "#adb5bd", 2) for k in range(1, 6)]
    if texte_:
        m.append(texte(0, -h - 20, texte_, 34, couleur, contour="#fff"))
    return place(m, x, y, s)


def bac(x, y, s=1.0, n_=6, gaston=0, eau=False, exprs=None):
    """Bac à glaçons vu de face ; (x, y) = milieu du bas. gaston = indice du glaçon Gaston (-1 = aucun)."""
    L = n_ * 100
    m = [rect(-L / 2 - 20, -130, L + 40, 130, "#d0ebff", rx=18, stroke="#74c0fc", stroke_width=5)]
    for k in range(n_):
        cx = -L / 2 + 50 + k * 100
        if eau:
            m.append(rect(cx - 42, -96, 84, 76, "#74c0fc", rx=10, opacity=0.8))
            m.append(chemin(f"M {cx - 40} -90 q 20 -8 40 0 t 40 0", stroke="#fff", sw=3, opacity=0.8))
        else:
            ex = (exprs or {}).get(k, "dort" if k != gaston else "content")
            m.append(glacon(cx, -18, 0.72, expr=ex))
    return place(m, x, y, s)


def congelateur(S):
    fond(S, "#e7f5ff")
    for k in range(4):
        S.add(rect(0, 180 + k * 180, 800, 12, "#ced4da"))
    r = random.Random(1)
    for _ in range(30):
        S.add(etoile5(r.uniform(0, 800), r.uniform(0, 800), r.uniform(4, 8), "#fff", rot=r.uniform(0, 40)))


def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(660, 130, 60, visage=True))
    S.add(nuage_perso(160, 150, 0.8, expr="content"))
    S.add(flocon(640, 420, 70))
    S.add(glacon(360, 620, 2.4, expr="rire"))
    S.add(goutte_perso(620, 640, 1.2, expr="content"))
    return S


def flocon(x, y, r=60, couleur="#ffffff", visage=None, rot=0):
    """Flocon de neige à six branches (symétrie hexagonale)."""
    m = []
    for k in range(6):
        branche = [trait(0, 0, 0, -r, couleur, r * 0.1)]
        for f in (0.45, 0.72):
            L = r * (0.35 if f < 0.6 else 0.25)
            branche.append(trait(0, -r * f, -L * 0.8, -r * f - L * 0.6, couleur, r * 0.07))
            branche.append(trait(0, -r * f, L * 0.8, -r * f - L * 0.6, couleur, r * 0.07))
        m.append(place(branche, 0, 0, rot=k * 60))
    m.append(poly([(math.cos(math.radians(a)) * r * 0.22, math.sin(math.radians(a)) * r * 0.22) for a in range(30, 390, 60)], couleur))
    if visage:
        m.append(cercle(0, 0, r * 0.3, "#d0ebff"))
        m.append(oeil(-r * 0.1, -r * 0.04, visage, taille=0.7 * r / 80) + oeil(r * 0.1, -r * 0.04, visage, taille=0.7 * r / 80))
        m.append(place(bouche(0, 0, "sourire", 0.5), 0, r * 0.08))
    return place(m, x, y, rot=rot)


def vignette():
    S = Scene(400, 270)
    S.add(glacon(200, 250, 1.8, expr="content"))
    return S


def p01():
    S = Scene()
    congelateur(S)
    S.add(thermometre(700, 330, 160, 0.15, "-18 °C", couleur=FROID))
    S.add(bac(360, 560, 1.05, 6, gaston=2, exprs={0: "dort", 1: "content", 3: "rire", 4: "dort", 5: "content"}))
    S.add(texte(360, 160, "Brrr, qu'il fait bon !", 48, FROID, contour="#fff"))
    return S


def p02():
    S = Scene()
    congelateur(S)
    S.add(rect(60, 260, 240, 240, "#e7f5ff", rx=20, stroke="#74c0fc", stroke_width=5))
    S.add(rect(80, 340, 200, 140, "#74c0fc", rx=12))
    S.add(chemin("M 80 346 q 25 -12 50 0 t 50 0 t 50 0 t 50 0", stroke="#fff", sw=4))
    S.add(texte(180, 560, "eau liquide", 38, "#1971c2"))
    S.add(fleche(330, 380, 450, 380, FROID, 8), texte(390, 340, "froid", 34, FROID))
    S.add(glacon(600, 500, 2.0, expr="rire"))
    S.add(texte(600, 560, "glace solide", 38, "#1971c2"))
    S.add(thermometre(400, 700, 120, 0.3, "0 °C", couleur=FROID))
    return S


def p03():
    S = Scene()
    ciel(S, "#ffe066", "#fff9db")
    S.add(soleil(680, 110, 55, visage=True))
    S.add(rect(0, 640, 800, 160, "#e8c39e"))
    niveau = 0.72
    h, w = 420, 300
    surf = -h * niveau
    # le glaçon flotte, mais seul un petit dixième dépasse de la limonade (coordonnées du verre)
    hauteur_g = 116 * 1.3
    contenu = g([glacon(0, surf + hauteur_g * 0.9, 1.3, expr="rire"),
                 rect(-w / 2 + 8, surf, w - 16, -surf - 8, "#fcc419", opacity=0.3),
                 trait(-w / 2 + 6, surf, w / 2 - 6, surf, "#fab005", 4),
                 cercle(-60, surf + 190, 8, "#fff", opacity=0.7), cercle(70, surf + 240, 6, "#fff", opacity=0.7), cercle(90, surf + 120, 5, "#fff", opacity=0.7)])
    S.add(verre(400, 640, w, h, contenu=contenu, niveau=niveau, couleur_contenu="#ffe066"))
    S.add(trait(470, 180, 520, 560, "#f06595", 14))
    S.add(texte(200, 200, "Plouf !", 64, "#f08c00", contour="#fff"))
    return S


def p04():
    S = Scene()
    ciel(S, "#ffa94d", "#fff4e6")
    S.add(soleil(400, 120, 60, visage=True))
    S.add(rect(0, 620, 800, 180, "#e8c39e"))
    for k, (x, f, ex) in enumerate([(160, 0.0, "sourire"), (400, 0.35, "inquiet"), (640, 0.65, "oups")]):
        S.add(glacon(x, 640, 1.4, expr=ex, fondu=f, gouttes=k > 0))
    S.add(fleche(240, 520, 300, 520, CHAUD, 6), fleche(480, 520, 540, 520, CHAUD, 6))
    for x in (160, 400, 640):
        S.add(g([chemin(f"M {x + dx} 330 q -8 -14 0 -28 q 8 -14 0 -28", stroke=CHAUD, sw=4, opacity=0.5) for dx in (-40, 0, 40)]))
    return S


def flaque_perso(x, y, s=1.0, expr="oups", r=1.0):
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin(f"M {-150 * r} 0 Q {-160 * r} -40 {-80 * r} -44 Q 0 -60 {90 * r} -40 Q {170 * r} -30 {150 * r} 0 Q 0 22 {-150 * r} 0 Z", "#74c0fc", opacity=0.9),
         ellipse(-60 * r, -30, 30, 6, "#fff", opacity=0.6),
         oeil(-18, -22, ys, taille=0.9), oeil(18, -22, ys, taille=0.9), place(bouche(0, 0, bs, 0.7), 0, -8)]
    return place(m, x, y, s)


def p05():
    S = Scene()
    interieur(S, "#fff4e6", "#c99a6e", y=560)
    S.add(table(380, 760, 600, 170, "#c68642"))
    S.add(verre(560, 572, 110, 150, niveau=0.4, couleur_contenu="#fff3bf"))
    S.add(flaque_perso(330, 580, 1.2, "oups"))
    for k in range(3):
        S.add(goutte(110, 610 + k * 50, 1.1, "#74c0fc"))
    S.add(texte(330, 300, "Oups !", 80, FROID, contour="#fff"))
    return S


def p06():
    S = Scene()
    fond(S, "#e6fcf5")
    S.add(rect(0, 640, 800, 160, "#e8c39e"))
    S.add(texte(400, 110, "Un liquide prend la forme", 40, "#1971c2"), texte(400, 160, "de ce qui le contient", 40, "#1971c2"))
    S.add(verre(150, 650, 150, 220, niveau=0.6))
    S.add(place(g([rect(-45, -300, 90, 300, "#e7f5ff", rx=24, opacity=0.6), rect(-40, -250, 80, 246, "#74c0fc", rx=20, opacity=0.9),
                   rect(-22, -360, 44, 70, "#e7f5ff", opacity=0.6), rect(-45, -300, 90, 300, "none", rx=24, stroke="#adb5bd", stroke_width=4)]), 400, 650))
    S.add(chemin("M 520 560 Q 530 650 640 650 Q 750 650 760 560 Z", "#ffa8a8"), chemin("M 528 590 Q 640 610 752 590 Q 740 646 640 646 Q 540 646 528 590 Z", "#74c0fc"))
    for x, y in [(150, 560), (400, 520), (640, 620)]:
        S.add(oeil(x - 12, y, "heureux", taille=0.8), oeil(x + 12, y, "heureux", taille=0.8))
    return S


def vapeur(x, y, h=150, s=1.0, opacity=0.6, couleur="#ffffff"):
    d = f"M 0 0 q -12 {-h / 6} 0 {-h / 3} q 12 {-h / 6} 0 {-h / 3} q -12 {-h / 6} 0 {-h / 3}"
    return place(chemin(d, stroke=couleur, sw=5, opacity=opacity, stroke_dasharray="2 10"), x, y, s)


def p07():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(660, 120, 60, visage=True))
    sol(S, 600, "#adb5bd", bosse=4)
    S.add(flaque_perso(380, 690, 1.2, "content", r=0.7))
    # la vapeur d'eau est invisible : on la montre en pointillés très pâles
    for x in (300, 380, 460):
        S.add(vapeur(x, 640, 300, 1.0, 0.9, "#ffffff"))
    return S


def bouilloire(x, y, s=1.0):
    m = [chemin("M -120 0 L -110 -170 Q 0 -230 110 -170 L 120 0 Z", "#fa5252"),
         chemin("M 110 -120 L 190 -190 L 200 -176 L 120 -90 Z", "#e03131"),
         chemin("M -70 -200 Q 0 -300 70 -200", stroke="#343a40", sw=14),
         rect(-126, -12, 252, 16, "#343a40", rx=6), ellipse(-60, -120, 18, 40, "#fff", opacity=0.3)]
    return place(m, x, y, s)


def p08():
    S = Scene()
    interieur(S, "#fff9db", "#c99a6e", y=600)
    S.add(rect(80, 600, 640, 40, "#868e96"), rect(80, 640, 640, 160, "#adb5bd"))
    S.add(cercle(300, 600, 60, "#ff922b", opacity=0.5))
    S.add(bouilloire(300, 600, 1.2))
    bx, by = 300 + 196 * 1.2, 600 - 186 * 1.2
    # juste au bec : vapeur invisible ; plus loin : petit nuage de gouttelettes
    for k, (dx, dy, r) in enumerate([(60, -40, 30), (100, -80, 48), (150, -130, 62), (90, -150, 50), (200, -190, 60), (130, -210, 46)]):
        S.add(cercle(bx + dx, by + dy, r, "#ffffff", opacity=0.95))
    S.add(texte(250, 160, "Pfffiou !", 70, CHAUD, contour="#fff"))
    return S


def p09():
    S = Scene()
    interieur(S, "#e7f5ff", "#c99a6e", y=620)
    S.add(rect(170, 80, 460, 480, "#fff", rx=10))
    S.add(rect(190, 100, 420, 440, "#a5d8ff"))
    S.add(sapin(300, 540, 0.8, neige=True), sapin(520, 540, 0.6, neige=True))
    S.add(rect(190, 100, 420, 440, "#f1f3f5", opacity=0.75))
    r = random.Random(9)
    for _ in range(40):
        S.add(cercle(r.uniform(200, 600), r.uniform(110, 530), r.uniform(2, 5), "#fff", opacity=0.9))
    S.add(cercle(400, 300, 90, "#a5d8ff", opacity=0.9), cercle(400, 300, 80, "#f1f3f5", opacity=0.6))
    S.add(cercle(370, 280, 10, "#74c0fc"), cercle(430, 280, 10, "#74c0fc"), chemin("M 350 330 Q 400 370 450 330", stroke="#74c0fc", sw=8))
    S.add(goutte(330, 420, 0.8, "#74c0fc"), trait(330, 430, 330, 520, "#74c0fc", 3, opacity=0.6))
    S.add(enfant(640, 800, 1.3, peau="brune", cheveux="noir", coiffure="boucles", habit="#f783ac", bras="montre", flip=True, regard=(-1, -1), expr="rire"))
    return S


def p10():
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    S.add(poly([(420, 800), (620, 460), (820, 800)], "#adb5bd"), poly([(620, 460), (660, 530), (580, 530)], "#fff"))
    S.add(nuage(360, 180, 2.4, "#ffffff", ombre="#dbe4ff"))
    r = random.Random(10)
    for _ in range(30):
        S.add(cercle(360 + r.uniform(-200, 220), 180 + r.uniform(-80, 90), r.uniform(4, 8), "#a5d8ff", opacity=0.7))
    S.add(goutte_perso(220, 520, 0.8, expr="rire"))
    S.add(fleche(220, 420, 260, 320, "#1971c2", 6))
    S.add(thermometre(700, 300, 140, 0.2, "froid", couleur=FROID))
    S.add(rect(0, 740, 800, 60, "#8ce99a"))
    return S


def p11():
    S = Scene()
    ciel(S, "#868e96", "#dee2e6")
    S.add(nuage(300, 130, 2.2, "#adb5bd", ombre="#868e96"), nuage(650, 100, 1.4, "#adb5bd", ombre="#868e96"))
    pluie(S, 60, 11, (60, 200, 780, 620), "#4dabf7")
    sol(S, 620, "#8ce99a", bosse=6)
    S.add(chemin("M 0 700 Q 200 660 400 700 T 800 690 L 800 760 Q 600 730 400 760 T 0 760 Z", "#4dabf7"))
    S.add(goutte_perso(420, 700, 0.8, expr="rire"))
    S.add(g([ellipse(420, 705, 40 + k * 30, 8 + k * 5, "none", stroke="#fff", stroke_width=3, opacity=0.8 - k * 0.2) for k in range(3)]))
    return S


def p12():
    S = Scene()
    ciel(S, "#748ffc", "#dbe4ff")
    flocons(S, 50, 12, (0, 0, 800, 800))
    S.add(flocon(400, 400, 230, "#ffffff", visage="heureux"))
    S.add(texte(400, 740, "6 branches", 56, "#364fc7", contour="#fff"))
    for k in range(6):
        a = math.radians(k * 60 - 90)
        S.add(texte(400 + math.cos(a) * 280, 400 + math.sin(a) * 280 + 16, str(k + 1), 44, "#364fc7", contour="#fff"))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#f1f3f5")
    sol(S, 600, "#f8f9fa", couleur2="#e7f5ff", y2=700)
    flocons(S, 30, 13, (0, 0, 800, 560))
    S.add(sapin(90, 620, 0.9, neige=True), sapin(720, 620, 0.8, neige=True))
    S.add(cercle(400, 640, 130, "#fff", stroke="#dee2e6", stroke_width=3), cercle(400, 470, 90, "#fff", stroke="#dee2e6", stroke_width=3), cercle(400, 340, 62, "#fff", stroke="#dee2e6", stroke_width=3))
    S.add(cercle(380, 330, 7, ENCRE), cercle(420, 330, 7, ENCRE), poly([(400, 345), (440, 355), (400, 360)], "#ff922b"))
    S.add(rect(360, 250, 80, 40, ENCRE), rect(340, 285, 120, 12, ENCRE))
    S.add(trait(320, 460, 230, 400, "#8d5524", 8), trait(480, 460, 570, 400, "#8d5524", 8))
    # Gaston, caché dans le ventre
    S.add(g([rect(360, 600, 80, 76, "#d0ebff", rx=12, stroke="#74c0fc", stroke_width=3), oeil(386, 630, "heureux", taille=0.7), oeil(414, 630, "heureux", taille=0.7),
             place(bouche(0, 0, "sourire", 0.6), 400, 648)], opacity=0.85))
    S.add(enfant(170, 790, 1.1, peau="claire", cheveux="blond", coiffure="queue", habit="#fa5252", jambes="#364fc7", acc=("bonnet_nuit",), couleur_acc="#4dabf7", bras="haut", expr="rire"))
    S.add(enfant(630, 790, 1.1, peau="foncee", cheveux="noir", coiffure="courts", habit="#20c997", bras="salut", expr="content", flip=True))
    return S


def p14():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(sapin(90, 330, 0.9, neige=True), sapin(720, 330, 0.8, neige=True))
    S.add(rect(0, 330, 800, 470, S.degrade(["#74c0fc", "#1c7ed6"])))
    S.add(rect(0, 300, 800, 50, "#e7f5ff", stroke="#a5d8ff", stroke_width=4))
    S.add(texte(700, 336, "glace 0 °C", 30, "#1971c2"))
    S.add(enfant(400, 302, 0.85, peau="doree", cheveux="brun", coiffure="queue", habit="#fcc419", bras="ouverts", expr="rire"))
    for x, y, c, f in [(200, 470, "#ff922b", False), (560, 560, "#fcc419", True), (330, 660, "#f06595", False)]:
        S.add(poisson(x, y, 1.1, c, flip=f, bulles=True))
    S.add(chemin("M 0 760 Q 400 740 800 760 L 800 800 L 0 800 Z", "#495057"))
    S.add(texte(680, 730, "4 °C", 38, "#fff"))
    S.add(texte(560, 420, "eau", 40, "#e7f5ff"))
    return S


def vapeur_perso(x, y, s=1.0):
    return place(g([nuage_perso(0, 0, 0.7, "#f1f3f5", expr="content", ombre=None), vapeur(-40, -40, 80, 1.0, 0.8, "#adb5bd"), vapeur(40, -40, 80, 1.0, 0.8, "#adb5bd")]), x, y, s)


def p15():
    S = Scene()
    fond(S, "#f8f9fa")
    G, E, V = (160, 610), (640, 610), (400, 230)
    S.add(glacon(G[0], G[1] + 70, 1.2, expr="content"), texte(G[0], G[1] + 120, "glace", 40, "#1971c2"))
    S.add(goutte_perso(E[0], E[1] + 70, 1.1, expr="content"), texte(E[0], E[1] + 120, "eau", 40, "#1971c2"))
    S.add(vapeur_perso(V[0], V[1] + 20, 1.2), texte(V[0], V[1] - 80, "vapeur", 40, "#868e96"))
    # chauffer : fondre puis s'évaporer (rouge) ; refroidir : se condenser puis geler (bleu)
    S.add(fleche(250, 590, 540, 590, CHAUD, 7), texte(395, 570, "fond", 32, CHAUD))
    S.add(fleche(590, 520, 460, 330, CHAUD, 7), texte(430, 450, "s'évapore", 30, CHAUD))
    S.add(fleche(530, 250, 700, 500, FROID, 7), texte(700, 340, "se condense", 30, FROID))
    S.add(fleche(540, 680, 250, 680, FROID, 7), texte(395, 720, "gèle", 32, FROID))
    return S


def p16():
    S = Scene()
    congelateur(S)
    S.add(bac(400, 620, 1.15, 6, gaston=2, exprs={0: "rire", 1: "content", 2: "rire", 3: "rire", 4: "content", 5: "rire"}))
    S.add(bulle(400, 200, 520, 100, "Bonjour, les frères !", 48, pointe=(350, 460)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("gaston-seul.svg", vignette),
    ("01-congelateur.svg", p01), ("02-il-gele.svg", p02), ("03-limonade.svg", p03), ("04-il-fond.svg", p04),
    ("05-flaque.svg", p05), ("06-formes.svg", p06), ("07-evaporation.svg", p07), ("08-bouilloire.svg", p08),
    ("09-buee.svg", p09), ("10-nuage.svg", p10), ("11-pluie.svg", p11), ("12-flocon.svg", p12),
    ("13-bonhomme.svg", p13), ("14-lac-gele.svg", p14), ("15-le-cycle.svg", p15), ("16-retour.svg", p16),
]
