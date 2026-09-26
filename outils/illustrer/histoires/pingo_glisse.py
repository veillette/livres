"""Pingo glisse ! — le frottement.

Plus les surfaces sont lisses, moins elles frottent : Pingo va loin sur la
glace (longue traînée), moins loin dans la neige, presque pas sur le sable.
Vues à la loupe, les surfaces rugueuses ont des bosses qui s'accrochent. Les
patins de frein frottent contre la jante de la roue.
"""
from base import *
from objets import *
from sciences import *

ID = "pingo-glisse"
AMIS = ["#4dabf7", "#51cf66", "#fcc419"]


def pingo(x, y, s=1.0, **k):
    return pingouin(x, y, s, **k)


def banquise(S, graine=1):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(poly([(-20, 470), (120, 330), (260, 470)], "#e7f5ff"), poly([(500, 470), (660, 350), (820, 470)], "#f1f3f5"))
    S.add(rect(0, 460, 800, 80, "#1c7ed6"))
    S.add(rect(0, 520, 800, 280, S.degrade(["#e7f5ff", "#d0ebff"])))
    S.add(g([trait(60 + k * 170, 600 + (k % 2) * 90, 150 + k * 170, 600 + (k % 2) * 90, "#fff", 5, opacity=0.8) for k in range(5)]))


def trainee(x, y, longueur, couleur="#74c0fc"):
    return g([trait(x - longueur, y - 6 + k * 8, x, y - 6 + k * 8, couleur, 4, opacity=0.6 - k * 0.15) for k in range(3)])


def couverture():
    S = Scene()
    banquise(S)
    S.add(trainee(330, 700, 300))
    S.add(pingouin_glisse(480, 710, 1.8, expr="rire"))
    S.add(texte(260, 250, "Ziiiip !", 90, "#1c7ed6", contour="#fff", rot=-6))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trainee(150, 220, 120))
    S.add(pingouin_glisse(230, 226, 1.1, expr="rire"))
    return S


def p01():
    S = Scene()
    banquise(S, 1)
    S.add(trainee(370, 700, 360))
    S.add(pingouin_glisse(500, 710, 1.6, expr="rire"))
    S.add(texte(250, 300, "Ziiiip !", 80, "#1c7ed6", contour="#fff"))
    return S


def p02():
    S = Scene()
    ciel(S, "#dee2e6", "#f8f9fa")
    flocons(S, 40, 2, (0, 0, 800, 560))
    S.add(sapin(120, 560, 0.9, neige=True), sapin(690, 560, 0.8, neige=True))
    S.add(rect(0, 560, 800, 240, "#ffffff"))
    S.add(trainee(360, 700, 120, "#adb5bd"))
    S.add(g([cercle(580 + k * 18, 680 - (k % 3) * 14, 16, "#fff", stroke="#e9ecef", stroke_width=2) for k in range(6)]))
    S.add(pingouin_glisse(460, 710, 1.5, expr="concentre", vitesse=False))
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(soleil(680, 110, 55, visage=True))
    S.add(rect(0, 470, 800, 60, "#339af0"))
    S.add(rect(0, 520, 800, 280, "#ffe066"))
    r = random.Random(3)
    for _ in range(60):
        S.add(cercle(r.uniform(0, 800), r.uniform(540, 800), r.uniform(2, 4), "#fab005"))
    S.add(place([trait(0, 0, 20, -300, "#495057", 6), chemin("M -170 -250 Q 20 -380 210 -250 Z", "#fa5252"), chemin("M -70 -284 Q 20 -370 60 -290", stroke="#fff", sw=18)], 620, 720))
    S.add(pingouin_glisse(360, 700, 1.5, expr="fache", vitesse=False))
    S.add(texte(300, 300, "Pfff…", 70, "#f08c00", contour="#fff"))
    return S


def surface(x, y, w, rugueux, couleur):
    if rugueux:
        pts = " ".join(f"L {x + k * 20} {y - (14 if k % 2 else 0)}" for k in range(int(w / 20) + 1))
        return chemin(f"M {x} {y} {pts} L {x + w} {y + 60} L {x} {y + 60} Z", couleur)
    return rect(x, y, w, 60, couleur, rx=4)


def p04():
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(texte(400, 100, "lisse : ça glisse !", 48, "#1c7ed6"))
    S.add(surface(60, 300, 680, False, "#a5d8ff"))
    S.add(rect(120, 220, 110, 80, "#fcc419", rx=8), fleche(260, 260, 640, 260, "#1c7ed6", 8))
    S.add(texte(400, 470, "rugueux : ça freine !", 48, "#c92a2a"))
    S.add(surface(60, 680, 680, True, "#c68642"))
    S.add(rect(120, 600, 110, 80, "#fcc419", rx=8), fleche(260, 640, 340, 640, "#c92a2a", 8))
    # à la loupe : les petites bosses s'accrochent
    S.add(cercle(600, 600, 90, "#fff", stroke="#495057", stroke_width=8), trait(664, 664, 720, 720, "#495057", 14))
    cid = uid("l")
    S.defs.append(el("clipPath", cercle(600, 600, 86, "#000"), id=cid))
    S.add(g([rect(510, 520, 180, 80, "#fcc419"), chemin("M 510 600 " + " ".join(f"L {510 + k * 18} {600 + (12 if k % 2 else 0)}" for k in range(11)) + " L 690 700 L 510 700 Z", "#c68642"),
             chemin("M 510 600 " + " ".join(f"L {510 + k * 18} {600 - (12 if k % 2 == 0 else 0)}" for k in range(11)), stroke="#e67700", sw=3)], clip_path=f"url(#{cid})"))
    return S


def p05():
    S = Scene()
    banquise(S, 5)
    S.add(pingo(400, 760, 2.3, expr="concentre", ailes="devant"))
    for dx in (-110, 110):
        S.add(g([chemin(f"M {400 + dx + k * 16} 420 q -10 -20 0 -40 q 10 -20 0 -40", stroke="#fa5252", sw=5, opacity=0.8) for k in range(-1, 2)]))
    S.add(texte(400, 180, "Ça chauffe !", 76, "#e03131", contour="#fff"))
    return S


def p06():
    S = Scene()
    interieur(S, "#fff4e6", "#d9a066", y=560)
    S.add(g([trait(0, 560 + k * 48, 800, 560 + k * 48, "#fff", 2, opacity=0.4) for k in range(6)]))
    S.add(fenetre(520, 90, 170, 150))
    x, y, s = 380, 760, 1.8
    S.add(place(pingo(0, 0, s, expr="surpris", ailes="ouvertes"), x, y, rot=-14))
    for sgn in (-1, 1):
        S.add(ellipse(x + sgn * 36, y - 4, 30, 14, "#f06595"))
    S.add(trainee(x - 60, y + 6, 240, "#fff"))
    S.add(texte(200, 200, "Wooouh !", 70, "#2f9e44", contour="#fff", rot=-8))
    return S


def botte(x, y, s=1.0, rot=0):
    m = [chemin("M -40 -260 L 40 -260 L 40 -60 L 130 -40 Q 150 0 120 0 L -40 0 Z", "#1c7ed6"), rect(-40, -260, 80, 30, "#1971c2")]
    return place(m, x, y, s, rot=rot)


def p07():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(botte(220, 520, 1.3))
    S.add(g([rect(160 + k * 36, 520, 22, 22, "#495057", rx=4) for k in range(7)]))
    S.add(place(g([rect(-110, -200, 220, 400, "#495057", rx=90)] + [rect(-90, -170 + k * 50, 180, 24, "#343a40", rx=10) for k in range(7)]), 600, 380, rot=18))
    S.add(texte(400, 720, "des creux et des bosses", 44, "#1971c2"))
    return S


def p08():
    S = Scene()
    ciel(S, "#dbe4ff", "#f8f9fa")
    S.add(maison(620, 520, 1.1, "#e9ecef", "#495057"))
    S.add(rect(0, 520, 800, 280, "#ced4da"), rect(0, 520, 800, 40, "#e9ecef"))
    S.add(rect(0, 580, 800, 220, "#d0ebff", opacity=0.7))
    r = random.Random(8)
    for _ in range(60):
        S.add(cercle(r.uniform(140, 520), r.uniform(600, 780), r.uniform(3, 6), "#a47148"))
    S.add(enfant(170, 740, 1.3, peau="rosee", cheveux="brun", coiffure="courts", habit="#fa5252", jambes="#364fc7", bras="donne", regard=(1, 1), acc=("bonnet_nuit",)))
    S.add(place(g([rect(-30, -40, 60, 60, "#fab005", rx=6)]), 300, 620))
    S.add(g([cercle(330 + k * 20, 640 + (k % 3) * 14, 4, "#a47148") for k in range(6)]))
    S.add(pingo(440, 760, 1.3, expr="content", ailes="bas"))
    return S


def p09():
    S = Scene()
    fond(S, "#f4fce3")
    S.add(rect(0, 700, 800, 100, "#c0eb75"))
    S.add(poly([(80, 330), (80, 700), (720, 700)], "#c68642"))
    S.add(poly([(80, 330), (720, 700), (720, 712), (80, 342)], "#a0693a"))
    a = math.degrees(math.atan2(370, 640))
    # la petite voiture roule, elle est déjà loin ; le cube frotte, il est encore en haut
    S.add(place(rect(-40, -70, 80, 70, "#fcc419", rx=6), 190, 393, rot=a))
    S.add(place(g([rect(-60, -50, 120, 36, "#339af0", rx=10), rect(-30, -76, 60, 30, "#339af0", rx=8), cercle(-34, -14, 16, ENCRE), cercle(34, -14, 16, ENCRE)]), 560, 608, rot=a))
    S.add(etoile5(690, 560, 26, "#fcc419"))
    S.add(pingo(120, 690, 1.0, expr="rire", ailes="haut"))
    S.add(texte(560, 200, "La voiture gagne !", 48, "#1c7ed6", contour="#fff"))
    return S


def caisse(x, y, s=1.0):
    return place([rect(-90, -130, 180, 130, "#c68642", rx=6), trait(-90, -65, 90, -65, "#a0693a", 5), trait(-90, -130, 90, 0, "#a0693a", 5)], x, y, s)


def p10():
    S = Scene()
    ciel(S, "#e7f5ff", "#fff")
    S.add(rect(0, 640, 800, 160, "#e9ecef"))
    # traîner : difficile ; faire rouler : facile
    S.add(rect(0, 480, 800, 40, "#dee2e6"), caisse(230, 482, 1.0))
    S.add(g([trait(100 - k * 20, 490, 130 - k * 20, 470, "#868e96", 3) for k in range(3)]))
    S.add(pingo(400, 490, 0.9, expr="fache", ailes="ouvertes", flip=True))
    S.add(caisse(260, 740, 1.0), cercle(200, 760, 24, ENCRE), cercle(320, 760, 24, ENCRE))
    S.add(pingo(450, 780, 0.9, expr="rire", ailes="ouvertes", flip=True))
    S.add(texte(620, 700, "Facile !", 50, "#2f9e44", contour="#fff"), texte(620, 440, "Ouf…", 50, "#c92a2a", contour="#fff"))
    return S


def p11():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600)
    S.add(caisse(360, 730, 1.4))
    for k in range(7):
        S.add(cercle(220 + k * 45, 745, 16, ["#fa5252", "#339af0", "#51cf66", "#fcc419"][k % 4]), cercle(214 + k * 45, 739, 5, "#fff", opacity=0.7))
    S.add(pingo(610, 770, 1.2, expr="rire", ailes="ouvertes", flip=True))
    S.add(fleche(250, 520, 110, 520, "#2f9e44", 7))
    return S


def p12():
    S = Scene()
    ciel(S, "#99e9f2", "#e3fafc")
    collines(S, 600, "#b2f2bb", graine=12)
    S.add(rect(0, 600, 800, 200, "#868e96"), g([rect(k * 160 + 20, 700, 100, 12, "#fff") for k in range(5)]))
    S.add(velo(400, 690, 1.3, couleur="#fa5252"))
    S.add(pingo(400, 560, 0.95, expr="concentre", ailes="devant"))
    # à la loupe : les patins de frein serrent la jante
    S.add(cercle(640, 250, 110, "#fff", stroke="#495057", stroke_width=8), trait(560, 330, 510, 400, "#495057", 14))
    S.add(cercle(640, 250, 90, "none", stroke="#495057", stroke_width=14), cercle(640, 250, 90, "none", stroke="#adb5bd", stroke_width=6))
    S.add(rect(700, 170, 20, 44, ENCRE, rx=4), rect(716, 176, 26, 30, "#fa5252", rx=4))
    S.add(texte(180, 220, "Iiiiih !", 70, "#e03131", contour="#fff"))
    return S


def p13():
    S = Scene()
    fond(S, "#fff")
    for k in range(10):
        S.add(trait(0, 80 + k * 70, 800, 80 + k * 70, "#a5d8ff", 3))
    S.add(trait(110, 0, 110, 800, "#ffa8a8", 3))
    S.add(chemin("M 160 380 Q 240 240 320 380 T 480 380 T 620 330", stroke="#495057", sw=8))
    S.add(place(g([rect(-12, -150, 24, 150, "#fcc419"), poly([(-12, 0), (12, 0), (0, 36)], "#f1c27d"), poly([(-4, 24), (4, 24), (0, 36)], "#495057")]), 640, 300, rot=30))
    S.add(place(g([rect(-50, -22, 70, 44, "#f783ac", rx=6), rect(20, -22, 40, 44, "#4dabf7", rx=6)]), 300, 600, rot=-20))
    S.add(g([ellipse(380 + k * 20, 620 - k * 6, 8, 3, "#ced4da") for k in range(4)]))
    return S


def p14():
    S = Scene()
    ciel(S, "#748ffc", "#dbe4ff")
    for k in range(9):
        S.add(etoile5(60 + k * 85, 80 + (k % 2) * 30, 10, "#fff3bf"))
    S.add(rect(0, 460, 800, 340, S.degrade(["#e7f5ff", "#a5d8ff"])))
    S.add(g([rect(k * 100, 440, 60, 30, ["#fa5252", "#fcc419", "#51cf66", "#339af0"][k % 4]) for k in range(8)]))
    S.add(chemin("M 200 700 Q 400 560 600 700 Q 400 800 200 700", stroke="#fff", sw=4, opacity=0.8))
    S.add(g(place(pingo(0, 0, 0.7, expr="oups", ailes="ouvertes"), 170, 560, rot=-80), opacity=0.35))
    S.add(pingo(420, 700, 1.6, expr="content", ailes="haut", pieds_haut=True))
    S.add(paillettes(560, 360, 1.5, "#fff3bf"), paillettes(280, 420, 1.1, "#fff3bf"))
    for sgn in (-1, 1):
        S.add(trait(420 + sgn * 30, 712, 420 + sgn * 60, 712, "#adb5bd", 5))
    return S


def p15():
    S = Scene()
    fond(S, "#e3fafc")
    for k in range(8):
        S.add(trait(0, 60 + k * 80, 800, 60 + k * 80, "#fff", 3), trait(80 + k * 100, 0, 80 + k * 100, 460, "#fff", 3))
    S.add(chemin("M 100 460 L 700 460 Q 700 700 400 700 Q 100 700 100 460 Z", "#fff", stroke="#dee2e6", sw=6))
    S.add(rect(110, 470, 580, 40, "#a5d8ff"))
    S.add(pingo(400, 600, 1.2, expr="surpris", ailes="haut"))
    S.add(rect(110, 480, 580, 60, "#fff", opacity=0.3))
    S.add(place(rect(-40, -24, 80, 48, "#f783ac", rx=16), 630, 200, rot=-25), mouvement(640, 180, 1.0, rot=-150))
    for x, y, r in [(200, 440, 30), (280, 420, 22), (560, 430, 26), (500, 400, 18)]:
        S.add(cercle(x, y, r, "#fff", stroke="#a5d8ff", stroke_width=3))
    S.add(texte(300, 200, "Oups !", 76, "#1c7ed6", contour="#fff"))
    return S


def p16():
    S = Scene()
    banquise(S, 16)
    S.add(place(g([trait(0, 0, 0, -140, "#495057", 5), poly([(0, -140), (70, -118), (0, -96)], "#fa5252")]), 720, 700))
    for k, c in enumerate(AMIS):
        S.add(trainee(200 + k * 70, 600 + k * 70, 160))
        S.add(pingouin_glisse(300 + k * 80, 610 + k * 70, 0.9, expr="rire", echarpe=c))
    S.add(pingouin_glisse(560, 720, 1.1, expr="rire"))
    S.add(texte(250, 250, "Partez !", 76, "#e03131", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pingo-seul.svg", vignette),
    ("01-banquise.svg", p01), ("02-neige.svg", p02), ("03-sable.svg", p03), ("04-frottement.svg", p04),
    ("05-ca-chauffe.svg", p05), ("06-chaussettes.svg", p06), ("07-bottes.svg", p07), ("08-trottoir.svg", p08),
    ("09-course.svg", p09), ("10-la-roue.svg", p10), ("11-billes.svg", p11), ("12-freins.svg", p12),
    ("13-crayon.svg", p13), ("14-patinoire.svg", p14), ("15-savon.svg", p15), ("16-course.svg", p16),
]
