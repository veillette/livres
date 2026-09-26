"""La petite graine — la germination du tournesol.

Vue en coupe : le ciel en haut, la terre en bas. La racine sort la
première et descend ; la tige monte ensuite, avec d'abord deux petites
feuilles rondes (les cotylédons), puis les vraies feuilles.
"""
from base import *
from objets import *
from sciences import *

ID = "petite-graine"
SOL = 440


def terre(S, haut="#74c0fc", bas="#e7f5ff", y=SOL, graine=1):
    ciel(S, haut, bas)
    S.add(rect(0, y, 800, 800 - y, S.degrade(["#9c6b3f", "#6f4a2a"])))
    S.add(chemin(f"M 0 {y} Q 200 {y - 14} 400 {y} T 800 {y} L 800 {y + 22} L 0 {y + 22} Z", "#69db7c"))
    r = random.Random(graine)
    for _ in range(18):
        S.add(ellipse(r.uniform(0, 800), r.uniform(y + 60, 790), r.uniform(6, 14), r.uniform(4, 9), "#5c3d22", opacity=0.6))
    for x in range(20, 800, 60):
        S.add(herbe(x + r.uniform(-10, 10), y + 4, 0.8, "#40c057"))


def ver(x, y, s=1.0, expr="sourire", flip=False):
    """Ver de terre qui ondule, la tête à droite."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -110 10 Q -80 -30 -50 0 Q -20 30 10 0 Q 40 -30 70 -6", stroke="#f783ac", sw=26),
         cercle(78, -10, 22, "#f783ac")]
    m += [chemin(f"M {x0} {-18 + (k % 2) * 30} q 0 12 0 22", stroke="#e64980", sw=2.5, opacity=0.6) for k, x0 in enumerate(range(-90, 60, 22))]
    m.append(oeil(72, -16, ys, (1, 0), taille=0.7) + oeil(88, -16, ys, (1, 0), taille=0.7))
    m.append(place(bouche(0, 0, bs, 0.6), 82, -4))
    return place(m, x, y, s, flip=flip)


def abeille(x, y, s=1.0, expr="content", flip=False):
    """Abeille qui vole, tête à droite ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [ellipse(-6, -34, 22, 32, "#e7f5ff", opacity=0.85, rot=-20), ellipse(16, -32, 18, 28, "#e7f5ff", opacity=0.85, rot=20),
         ellipse(0, 0, 44, 30, "#fcc419")]
    cid = uid("a")
    m.append(el("clipPath", ellipse(0, 0, 44, 30, "#000"), id=cid))
    m.append(g([rect(-24, -40, 12, 80, ENCRE), rect(-2, -40, 12, 80, ENCRE)], clip_path=f"url(#{cid})"))
    m.append(poly([(-44, -4), (-60, 0), (-44, 4)], ENCRE))
    m.append(cercle(46, -6, 22, "#fcc419"))
    m.append(chemin("M 46 -26 Q 44 -44 34 -50 M 54 -24 Q 60 -42 70 -46", stroke=ENCRE, sw=3))
    m.append(oeil(52, -10, ys, (1, 0), taille=0.7))
    m.append(ellipse(58, 2, 5, 3, ROSE, opacity=0.8))
    m.append(place(bouche(0, 0, bs, 0.5), 56, 2))
    return place(m, x, y, s, flip=flip)


def racines(x, y, s=1.0, profondeur=160, nb=5, poils=True):
    m = [chemin(f"M 0 0 Q 6 {profondeur * 0.5} 0 {profondeur}", stroke="#f1e3c8", sw=6)]
    r = random.Random(nb)
    for k in range(nb - 1):
        y0 = profondeur * (0.2 + 0.18 * k)
        sgn = -1 if k % 2 else 1
        L = r.uniform(40, 70) * (1 - k * 0.1)
        m.append(chemin(f"M 2 {n(y0)} Q {sgn * L * 0.5} {n(y0 + 10)} {n(sgn * L)} {n(y0 + L * 0.6)}", stroke="#f1e3c8", sw=4))
    if poils:
        for k in range(10):
            yy = profondeur * (0.3 + 0.07 * k)
            m.append(trait(0, yy, (-1) ** k * 10, yy + 4, "#f1e3c8", 1.5))
    return place(m, x, y, s)


def pousse(x, y, h, s=1.0, cotyledons=True, feuilles=0, courbe=0):
    """Jeune tige ; (x, y) = collet, au niveau du sol. feuilles = paires de vraies feuilles."""
    m = [chemin(f"M 0 0 Q {courbe} {-h / 2} 0 {-h}", stroke="#51cf66", sw=8)]
    for k in range(feuilles):
        yy = -h * (0.35 + 0.5 * k / max(1, feuilles))
        for sgn in (-1, 1):
            m.append(chemin(f"M 0 {n(yy)} Q {sgn * 30} {n(yy - 36)} {sgn * 74} {n(yy - 16)} Q {sgn * 36} {n(yy + 8)} 0 {n(yy)} Z", "#40c057"))
    if cotyledons:
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 26, -h - 6, 26, 13, "#8ce99a", rot=-sgn * 20))
    return place(m, x, y, s)


def graine(x, y, s=1.0, **k):
    return graine_perso(x, y, s, **k)


def couverture():
    S = Scene()
    terre(S, "#74c0fc", "#e7f5ff", SOL + 40, 3)
    S.add(soleil(660, 110, 55, visage=True))
    S.add(racines(400, SOL + 44, 1.6, 180, 7))
    S.add(tournesol(400, SOL + 44, 1.0, tige=300, visage="rire", feuilles=6))
    S.add(graine(250, 720, 0.8, expr="content", regard=(1, -1)))
    S.add(ver(600, 700, 0.8, expr="content", flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(graine(200, 250, 1.8, expr="content"))
    return S


def p01():
    S = Scene()
    terre(S, graine=1)
    S.add(soleil(680, 110, 50))
    S.add(graine(330, 700, 2.2, expr="dort"))
    S.add(zzz(420, 470, 1.1, "#ffd8a8"))
    S.add(ver(610, 650, 1.3, expr="sourire", flip=True))
    S.add(bulle(560, 260, 300, 86, "Patience !", 46, pointe=(600, 560)))
    return S


def p02():
    S = Scene()
    terre(S, "#91a7c7", "#dbe4f0", graine=2)
    S.add(nuage(260, 110, 1.3, "#ced4da", ombre="#adb5bd"), nuage(600, 90, 1.0, "#ced4da", ombre="#adb5bd"))
    pluie(S, 45, 2, (60, 180, 760, SOL - 20), "#4dabf7")
    for k in range(9):
        S.add(goutte(200 + (k % 5) * 90, SOL + 60 + (k // 5) * 70 + (k % 2) * 20, 1.0, "#74c0fc"))
    S.add(graine(400, 720, 2.2, expr="rire", regard=(0, -1)))
    S.add(texte(400, 150, "Glou, glou !", 56, "#1c7ed6", contour="#fff"))
    return S


def p03():
    S = Scene()
    terre(S, graine=3)
    S.add(soleil(680, 110, 50))
    S.add(racines(400, 600, 1.6, 120, 5))
    S.add(graine(400, 610, 2.0, expr="concentre", regard=(0, 1)))
    S.add(fleche(580, 560, 580, 740, "#fff3bf", 7), texte(670, 660, "racine", 40, "#fff3bf"))
    S.add(ver(160, 700, 0.8, expr="content"))
    return S


def p04():
    S = Scene()
    terre(S, graine=4)
    S.add(soleil(640, 120, 60, visage=True))
    S.add(rayons_soleil(590, 170, 430, 330, "#fcc419", 3, 24))
    S.add(racines(400, SOL + 180, 1.4, 120, 6))
    S.add(pousse(400, SOL + 10, 110, 1.8, courbe=10))
    S.add(chemin(f"M 400 {SOL + 10} L 400 {SOL + 180}", stroke="#51cf66", sw=12))
    S.add(graine(400, SOL + 200, 1.5, expr="content", regard=(0, -1)))
    S.add(fleche(230, SOL - 40, 230, SOL - 200, "#2f9e44", 8))
    return S


def p05():
    S = Scene()
    terre(S, graine=5)
    S.add(soleil(680, 110, 50, visage=True))
    S.add(racines(400, SOL + 12, 1.8, 180, 8))
    S.add(pousse(400, SOL + 12, 200, 1.7, cotyledons=True, feuilles=3))
    S.add(texte(160, 200, "2, 4, 6 !", 52, "#2f9e44", contour="#fff"))
    return S


def p06():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 620, "#b2f2bb", graine=6)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=700)
    S.add(soleil(680, 100, 50))
    S.add(tournesol(470, 770, 1.0, tige=560, tete=1.25, visage="rire", feuilles=8, rot=-8))
    S.add(enfant(250, 770, 1.35, peau="doree", cheveux="brun", coiffure="queue", habit="#ff8787", jambes="#364fc7",
                 expr="bouche_bee", regard=(1, -1), bras="haut"))
    return S


def p07():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(tournesol(400, 900, 1.6, tige=460, visage="content", feuilles=4))
    S.add(abeille(600, 250, 1.4, expr="rire", flip=True))
    S.add(chemin("M 760 120 q -40 40 -80 20 q -40 -20 -80 30", stroke="#495057", sw=3, stroke_dasharray="8 10"))
    S.add(bulle(560, 420, 380, 90, "Bzzz ! Merci !", 44, pointe=(610, 300)))
    return S


def p08():
    S = Scene()
    terre(S, "#ffa94d", "#fff4e6", graine=8)
    S.add(soleil(120, 140, 50))
    # fin de l'été : la fleur fanée penche, ses graines mûres tombent
    S.add(tournesol(430, SOL + 10, 1.0, tige=330, visage="dort", feuilles=4, rot=35, fane=True))
    r = random.Random(4)
    for k in range(6):
        S.add(graine_perso(430 + 110 + r.uniform(-40, 40), 200 + k * 36, 0.18, rot=r.uniform(0, 360)))
    for k, x in enumerate((230, 380, 530, 660)):
        S.add(graine(x, 600 + (k % 2) * 80, 0.9, expr="dort"))
    S.add(zzz(560, 520, 0.6, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("graine-seule.svg", vignette),
    ("01-sous-terre.svg", p01), ("02-pluie.svg", p02), ("03-racine.svg", p03), ("04-tige.svg", p04),
    ("05-feuilles.svg", p05), ("06-fleur.svg", p06), ("07-abeille.svg", p07), ("08-vent.svg", p08),
]
