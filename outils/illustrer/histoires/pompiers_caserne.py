"""Une journée chez les pompiers — caserne, alerte, feu éteint, chat sauvé."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from fantastique import echelle
from fables import flammes

ID = "pompiers-caserne"
ROUGE = "#e03131"
MAELLE = dict(peau="claire", cheveux="blond", coiffure="queue", habit=MARINE, jambes=MARINE,
              chaussures="#212529", tenue=veste_pompier(), coiffe=casque_pompier())
KARIM = dict(peau="doree", cheveux="brun", coiffure="courts", habit=MARINE, jambes=MARINE,
             chaussures="#212529", tenue=veste_pompier(), coiffe=casque_pompier())
# en tee-shirt, à la caserne
MAELLE_SPORT = dict(MAELLE, habit="#1c7ed6", jambes=MARINE, tenue=None, coiffe=None)
KARIM_SPORT = dict(KARIM, habit="#1c7ed6", jambes=MARINE, tenue=None, coiffe=None)
ZOE = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#ffd43b", jambes="#e64980",
           chaussures="#862e9c")


def maelle(x, y, s=1.6, **k):
    return pro(x, y, s, **{**MAELLE, **k})


def karim(x, y, s=1.6, **k):
    return pro(x, y, s, **{**KARIM, **k})


def camion_pompiers(x, y, s=1.0, flip=False, gyro=True, echelle_=True):
    """Camion de pompiers de profil, tourné vers la droite ; (x, y) = sol, au milieu."""
    fonce = _assombrir(ROUGE, 0.8)
    m = [rect(-270, -190, 380, 150, ROUGE, rx=14),
         chemin("M 110 -40 L 110 -200 L 200 -200 Q 240 -200 256 -150 L 270 -100 L 270 -40 Z", ROUGE),
         chemin("M 126 -186 L 196 -186 Q 222 -186 236 -150 L 244 -124 L 126 -124 Z", "#a5d8ff"),
         rect(-270, -100, 540, 16, "#fff"),
         rect(-250, -176, 100, 64, fonce, rx=8), rect(-140, -176, 100, 64, fonce, rx=8), rect(-30, -176, 100, 64, fonce, rx=8),
         cercle(-90, -144, 22, "#ced4da"), cercle(-90, -144, 10, "#868e96"),
         rect(250, -76, 26, 26, "#fff3bf", rx=6), rect(-286, -60, 572, 22, "#495057", rx=8)]
    if echelle_:
        m.append(rect(-260, -214, 360, 18, "#adb5bd", rx=6))
        for k in range(10):
            m.append(rect(-250 + k * 36, -220, 8, 30, "#868e96"))
    if gyro:
        m.append(gyrophare(170, -200, 1.0, "#4dabf7"))
    m += [roue(-170, -36, 44), roue(-60, -36, 44), roue(190, -36, 44)]
    return place(m, x, y, s, flip=flip)


def caserne(S):
    ciel(S)
    S.add(rect(0, 120, 800, 480, "#ffe8cc"))
    S.add(rect(0, 100, 800, 40, "#c92a2a"))
    S.add(rect(240, 150, 320, 56, "#fff", rx=8), texte(400, 192, "POMPIERS", 42, ROUGE))
    for x in (40, 420):
        S.add(rect(x, 240, 340, 360, "#e9ecef", stroke="#adb5bd", stroke_width=6))
        for k in range(1, 6):
            S.add(trait(x, 240 + k * 60, x + 340, 240 + k * 60, "#ced4da", 4))
    S.add(rect(0, 600, 800, 200, "#adb5bd"))


def flamme(x, y, s=1.0):
    return place([chemin("M -60 0 Q -80 -70 -40 -110 Q -36 -70 -14 -150 Q 14 -90 30 -130 Q 74 -80 60 0 Z", "#ff922b"),
                  chemin("M -34 0 Q -44 -50 -18 -70 Q -6 -44 6 -96 Q 30 -60 34 0 Z", "#ffd43b")], x, y, s)


def fumee(x, y, s=1.0, op=0.7):
    return g(place([cercle(0, 0, 40, "#adb5bd"), cercle(40, -50, 50, "#ced4da"), cercle(-10, -110, 58, "#dee2e6")],
                   x, y, s), opacity=op)


def cabane(x, y, s=1.0):
    return place([rect(-120, -170, 240, 170, "#c68642"), poly([(-140, -170), (0, -270), (140, -170)], "#8d5524"),
                  rect(-30, -110, 60, 110, "#7c4a1e"), rect(60, -130, 40, 40, "#495057")] +
                 [trait(-120, -170 + k * 30, 120, -170 + k * 30, "#a0693a", 3) for k in range(1, 6)], x, y, s)


def jardin(S, y=600):
    ciel(S)
    collines(S, y, "#b2f2bb", graine=3)
    sol(S, y, "#8ce99a")


def tuyau(points, c="#f8f9fa"):
    d = "M " + " L ".join(f"{px} {py}" for px, py in points)
    return chemin(d, stroke="#ced4da", sw=16) + chemin(d, stroke=c, sw=11)


def rouleau(x, y, s=1.0):
    """Tuyau enroulé, vu de côté."""
    return place([cercle(0, 0, 38, "#ced4da"), cercle(0, 0, 32, "#f8f9fa"), cercle(0, 0, 24, "#ced4da"),
                  cercle(0, 0, 18, "#f8f9fa"), cercle(0, 0, 10, "#868e96")], x, y, s)


def jet(x0, y0, x1, y1, haut=120):
    d = f"M {x0} {y0} Q {(x0 + x1) / 2} {min(y0, y1) - haut} {x1} {y1}"
    return chemin(d, stroke="#74c0fc", sw=22, opacity=0.8) + chemin(d, stroke="#d0ebff", sw=8)


def chat_arbre(x, y, s=1.0, expr="inquiet"):
    return perso("chat", x, y, s, expr=expr, bras="bas", couleur="#868e96")


def detecteur(x, y, s=1.0):
    return place([ellipse(0, 0, 60, 18, "#f8f9fa", stroke="#ced4da", stroke_width=4),
                  rect(-54, -12, 108, 14, "#f1f3f5"), cercle(30, 6, 5, ROUGE)], x, y, s)


def couverture():
    S = Scene()
    caserne(S)
    S.add(camion_pompiers(400, 660, 1.2))
    S.add(maelle(230, 790, 1.55, expr="rire", bras="salut"))
    S.add(karim(580, 790, 1.55, expr="content", bras="hanches"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(camion_pompiers(200, 250, 0.65))
    return S


def p01():
    S = Scene()
    caserne(S)
    S.add(camion_pompiers(420, 700, 1.25))
    S.add(maelle(120, 790, 1.4, expr="concentre", bras="montre", regard=(1, -0.3)))
    S.add(eclat(720, 380, 0.6, "#ffd43b"))
    return S


def p02():
    S = Scene()
    caserne(S)
    S.add(rect(150, 140, 16, 440, "#f6d38b"), rect(100, 130, 120, 16, "#868e96"))
    S.add(pro(158, 560, 1.15, **{**KARIM_SPORT, "bras": "haut", "expr": "concentre"}))
    S.add(pro(420, 790, 1.4, **{**MAELLE_SPORT, "bras": "course", "expr": "content", "regard": (1, 0)}))
    S.add(mouvement(330, 640, 1.0))
    # pompier qui porte des rouleaux de tuyau
    rouleaux = rouleau(-30, -80, 0.9) + rouleau(30, -80, 0.9)
    S.add(pro(650, 790, 1.4, peau="brune", cheveux="noir", habit="#1c7ed6", jambes=MARINE, chaussures="#212529",
              bras="porte", expr="concentre", objet=rouleaux))
    return S


def p03():
    S = Scene()
    interieur(S, "#ffe8cc", "#adb5bd", 600, plinthe="#868e96")
    S.add(cercle(400, 110, 46, ROUGE), cercle(400, 110, 26, "#ffc9c9"))
    S.add(texte(400, 230, "DRIIING !", 70, ROUGE, contour="#fff"))
    for k, x in enumerate((120, 260)):
        S.add(cercle(x, 300, 8, "#868e96"))
    S.add(rect(100, 300, 50, 120, MARINE, rx=10))
    S.add(maelle(300, 790, 1.6, expr="surpris", bras="tete"))
    S.add(karim(580, 790, 1.6, expr="concentre", bras="porte", coiffe=None,
                objet=g([rect(-30, -70, 22, 60, "#212529", rx=6), rect(8, -70, 22, 60, "#212529", rx=6)])))
    S.add(mouvement(700, 420, 1.0, rot=180))
    return S


def p04():
    S = Scene()
    rue(S, 600)
    S.add(camion_pompiers(470, 760, 1.05))
    S.add(mouvement(150, 640, 1.4), mouvement(130, 690, 1.2))
    S.add(texte(560, 300, "Pin-pon !", 70, ROUGE, contour="#fff", rot=-6))
    S.add(camion(80, 580, 0.9, "#4dabf7"), camion(720, 580, 0.9, "#fab005"))
    return S


def p05():
    S = Scene()
    jardin(S)
    S.add(cabane(560, 640, 1.1))
    S.add(fumee(560, 260, 1.2, 0.8))
    S.add(flamme(520, 360, 0.9), flamme(610, 360, 0.7))
    S.add(barriere(170, 700, 1.0, largeur=280))
    S.add(pro(110, 690, 1.25, peau="claire", cheveux="gris", coiffure="courts", habit="#9775fa", jambes="#495057",
              bras="calin", expr="inquiet", regard=(1, 0)))
    S.add(petit(230, 690, 0.95, peau="claire", cheveux="blond", habit="#ff8787", expr="inquiet", regard=(1, 0)))
    S.add(maelle(380, 790, 1.4, expr="concentre", bras="large", regard=(1, 0),
                 objet=rouleau(0, -70)))
    return S


def p06():
    S = Scene()
    jardin(S)
    S.add(cabane(600, 640, 1.0))
    S.add(fumee(600, 300, 1.0, 0.6))
    S.add(flamme(580, 410, 0.35))
    S.add(tuyau([(0, 760), (120, 770), (200, 740), (240, 640)]))
    S.add(karim(250, 790, 1.6, expr="concentre", bras="donne", regard=(1, -0.5)))
    xm, ym = 250 + 84 * 1.6, 790 - 92 * 1.6
    S.add(rect(xm - 20, ym - 8, 60, 16, "#868e96", rx=6))
    S.add(jet(xm + 40, ym, 580, 430, 140))
    for k in range(6):
        S.add(goutte(520 + k * 22, 470 + (k % 2) * 24, 0.5, "#74c0fc"))
    S.add(texte(380, 200, "Pschhhh !", 64, "#1c7ed6", contour="#fff"))
    return S


def p07():
    S = Scene()
    jardin(S)
    S.add(arbre(560, 640, 1.9))
    S.add(rect(470, 260, 200, 18, "#8d5524", rx=8))
    S.add(chat_arbre(600, 262, 0.55))
    S.add(echelle(470, 640, 1.0, h=400, rot=14))
    S.add(camion_pompiers(170, 700, 0.6, echelle_=False))
    S.add(petit(110, 790, 1.15, **ZOE, expr="inquiet", bras="montre"))
    S.add(maelle(340, 790, 1.4, expr="content", bras="tient", regard=(1, -1)))
    S.add(bulle(220, 130, 360, 100, "Mon chat est\ncoincé là-haut !", 32, pointe=(140, 520)))
    return S


def p08():
    S = Scene()
    jardin(S)
    S.add(arbre(640, 640, 1.6))
    S.add(echelle(560, 640, 0.9, h=340, rot=14))
    S.add(maelle(300, 790, 1.6, expr="content", bras="calin", regard=(1, 0.3),
                 objet=perso("chat", 6, -40, 0.5, expr="content", bras="bas", couleur="#868e96")))
    S.add(petit(480, 790, 1.2, **ZOE, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(360, 120, 400, 90, "Merci, la pompière !", 34, pointe=(470, 450)))
    S.add(coeur(420, 300, 0.8, "#ff6b6b"))
    return S


def p09():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", 600, plinthe="#d9a066")
    S.add(rect(80, 80, 380, 230, "#2b8a3e", rx=10, stroke="#c68642", stroke_width=10))
    S.add(texte(270, 170, "Du feu ?", 40, "#fff"), texte(270, 230, "On prévient", 34, "#fff"),
          texte(270, 275, "un adulte !", 34, "#fff"))
    S.add(detecteur(620, 110, 1.4))
    S.add(texte(620, 190, "détecteur", 28, "#e8590c"))
    S.add(maelle(620, 720, 1.4, expr="sourire", bras="montre", flip=True, regard=(1, -1)))
    for k, (x, peau, ch, coif, hab) in enumerate([(110, "claire", "roux", "courts", "#74c0fc"),
                                                    (230, "brune", "noir", "boucles", "#ff8787"),
                                                    (350, "doree", "brun", "queue", "#69db7c"),
                                                    (470, "foncee", "noir", "courts", "#ffd43b")]):
        S.add(petit(x, 790, 0.9, peau=peau, cheveux=ch, coiffure=coif, habit=hab, expr="bouche_bee" if k % 2 else "sourire",
                    regard=(1, -0.6)))
    return S


def p10():
    S = Scene()
    caserne(S)
    S.add(camion_pompiers(420, 700, 1.25, gyro=True))
    S.add(petit(270, 790, 1.15, peau="brune", cheveux="noir", coiffure="boucles", habit="#ff8787",
                expr="rire", bras="haut", coiffe=casque_pompier()))
    S.add(petit(460, 790, 1.15, peau="claire", cheveux="roux", habit="#74c0fc", expr="fier", bras="salut",
                coiffe=casque_pompier("#fcc419")))
    S.add(maelle(650, 790, 1.4, expr="rire", bras="hanches"))
    S.add(karim(100, 790, 1.4, expr="content", bras="salut"))
    S.add(texte(400, 120, "Pin-pon !", 64, ROUGE, contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("camion-seul.svg", vignette),
    ("01-la-caserne.svg", p01), ("02-entrainement.svg", p02), ("03-alerte.svg", p03),
    ("04-pin-pon.svg", p04), ("05-la-cabane.svg", p05), ("06-la-lance.svg", p06),
    ("07-le-chat.svg", p07), ("08-merci.svg", p08), ("09-a-l-ecole.svg", p09),
    ("10-tous-pompiers.svg", p10),
]
