"""La Colombe et la Fourmi — un bienfait n'est jamais perdu."""
from fables import *

ID = "colombe-fourmi"

CHASSEUR = dict(coiffure="courts", cheveux="brun", peau="rosee", habit="#5c940d", robe=False,
                jambes="#7c4a1e", barbe="#4a2c17")


def fourmi(x, y, s=1.0, **k):
    return perso("fourmi", x, y, s, **k)


def chasseur(x, y, s=1.0, **k):
    return personne(x, y, s, **{**CHASSEUR, **k})


def epuisette(x, y, s=1.0, rot=0):
    """Grand filet à oiseaux au bout d'un manche ; (x, y) = bout du manche."""
    cid = uid("f")
    lignes = [trait(-90 + k * 18, -330, -90 + k * 18 + 120, -150, "#adb5bd", 2) for k in range(-6, 12)]
    lignes += [trait(-90 + k * 18, -330, -90 + k * 18 - 120, -150, "#adb5bd", 2) for k in range(-2, 16)]
    m = [trait(0, 0, 0, -240, "#a0522d", 9),
         el("clipPath", chemin("M -70 -300 Q -80 -190 0 -170 Q 80 -190 70 -300 Z", "#000"), id=cid),
         g(lignes, clip_path=f"url(#{cid})"),
         ellipse(0, -300, 72, 22, "none", stroke="#868e96", stroke_width=6)]
    return place(m, x, y, s, rot=rot)


def cage(x, y, s=1.0):
    m = [chemin("M -60 0 L -60 -110 Q -60 -170 0 -170 Q 60 -170 60 -110 L 60 0 Z", "none", stroke="#fab005", sw=5)]
    for k in range(-2, 3):
        m.append(trait(k * 24, -160 + abs(k) * 6, k * 24, 0, "#fab005", 4))
    m += [rect(-66, -8, 132, 12, "#f59f00", rx=4), cercle(0, -178, 9, "none", stroke="#fab005", stroke_width=4)]
    return place(m, x, y, s)


def ruisseau(S, y=520, soleil_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    if soleil_:
        S.add(soleil(680, 110, 46))
    collines(S, y - 30, "#b2f2bb", graine=12)
    sol(S, y - 20, "#8ce99a")
    riviere(S, y + 60)


def branche_ruisseau(S, y=260):
    """Arbre penché au-dessus de l'eau à gauche, longue branche vers la droite."""
    S.add(chemin(f"M 0 {y + 360} Q 60 {y + 150} 90 {y} L 130 {y + 20} Q 110 {y + 170} 60 {y + 360} Z", "#8d5524"))
    S.add(chemin(f"M 100 {y + 20} Q 300 {y - 10} 520 {y + 10} L 520 {y + 28} Q 300 {y + 12} 110 {y + 50} Z", "#8d5524"))
    for fx, fy, r in [(60, y - 60, 100), (180, y - 90, 80), (300, y - 50, 60), (470, y - 20, 50), (-10, y + 40, 80)]:
        S.add(cercle(fx, fy, r, "#40c057"))
    S.add(cercle(120, y - 20, 50, "#51cf66"))


def couverture():
    S = Scene()
    ruisseau(S, 500)
    branche_ruisseau(S, 250)
    S.add(colombe(420, 262, 1.3, expr="sourire", regard=(0, 1)))
    S.add(brin_herbe(430, 660, 1.4, rot=-4))
    S.add(fourmi(430, 670, 0.9, expr="rire", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(brin_herbe(200, 150, 1.5, rot=-10))
    return S


def p01():
    S = Scene()
    ruisseau(S, 520)
    S.add(herbe(160, 560, 1.4))
    S.add(fourmi(330, 560, 1.4, expr="triste", bras="bouche"))
    S.add(soleil(680, 110, 46, "#ffa94d"))
    S.add(bulle(520, 180, 340, 90, "J'ai soif !", 44, pointe=(380, 330)))
    return S


def p02():
    S = Scene()
    ruisseau(S, 520)
    S.add(fourmi(430, 380, 1.3, expr="oups", bras="haut", rot=160))
    S.add(texte(560, 330, "PLOUF !", 76, "#1c7ed6", contour="#fff"))
    for k in range(6):
        a = math.radians(-150 + k * 24)
        S.add(goutte(420 + math.cos(a) * 100, 620 + math.sin(a) * 80, 1.0, "#74c0fc"))
    return S


def p03():
    S = Scene()
    ruisseau(S, 420)
    S.add(fourmi(400, 690, 1.3, expr="pleure", bras="haut"))
    S.add(ellipse(400, 690, 130, 26, "#1c7ed6"))
    S.add(chemin("M 250 690 q 40 -18 80 0 q 40 18 80 0 q 40 -18 80 0 q 40 18 80 0", stroke="#a5d8ff", sw=8))
    S.add(bulle(420, 180, 340, 90, "Au secours !", 44, pointe=(410, 380)))
    S.add(fleche(170, 560, 60, 560, "#fff", 8, 22))
    return S


def p04():
    S = Scene()
    ruisseau(S, 520)
    branche_ruisseau(S, 250)
    S.add(colombe(420, 262, 1.4, expr="surpris", regard=(1, 1)))
    S.add(fourmi(640, 700, 0.6, expr="pleure", bras="haut"))
    S.add(texte(620, 520, "Au secours !", 36, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    ruisseau(S, 520)
    branche_ruisseau(S, 250)
    S.add(colombe(400, 262, 1.3, expr="concentre", regard=(1, 1)))
    S.add(brin_herbe(560, 480, 0.9, rot=60))
    S.add(mouvement(560, 380, 0.8, rot=90))
    S.add(fourmi(620, 720, 0.6, expr="pleure", bras="haut"))
    return S


def p06():
    S = Scene()
    ruisseau(S, 420)
    S.add(brin_herbe(400, 680, 2.2, rot=-3))
    S.add(fourmi(400, 690, 1.2, expr="inquiet", bras="calin"))
    S.add(chemin("M 120 740 q 40 -18 80 0 q 40 18 80 0 M 520 740 q 40 -18 80 0 q 40 18 80 0", stroke="#a5d8ff", sw=8))
    return S


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 110, 46))
    collines(S, 560, "#b2f2bb", graine=12)
    S.add(rect(0, 560, 800, 240, "#4dabf7"))
    S.add(chemin("M 0 620 q 40 -14 80 0 q 40 14 80 0 q 40 -14 80 0 M 40 720 q 40 -14 80 0 q 40 14 80 0", stroke="#a5d8ff", sw=6))
    S.add(chemin("M 340 800 Q 330 640 460 570 Q 600 530 800 540 L 800 800 Z", "#8ce99a"))
    S.add(brin_herbe(250, 660, 1.2, rot=-10))
    S.add(fourmi(600, 740, 1.3, expr="rire", bras="haut", pieds_haut=True))
    S.add(texte(560, 330, "Sauvée !", 64, "#2b8a3e", contour="#fff"))
    return S


def p08():
    S = Scene()
    ruisseau(S, 520)
    branche_ruisseau(S, 250)
    S.add(colombe(420, 262, 1.3, expr="content", ailes="haut"))
    S.add(fourmi(560, 520, 1.1, expr="rire", bras="salut", regard=(-1, -1)))
    S.add(bulle(610, 110, 320, 90, "Merci, colombe !", 34, pointe=(580, 300)))
    return S


def p09():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=4)
    sol(S, 600, "#8ce99a")
    S.add(chasseur(380, 760, 1.5, expr="malin", bras="tient", objet=epuisette(68, -146, 0.8, rot=10)))
    S.add(cage(620, 740, 1.2))
    S.add(bulle(330, 120, 460, 110, "Quelle belle colombe !\nElle ira dans ma cage !", 32, pointe=(380, 460)))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=4)
    sol(S, 600, "#8ce99a")
    S.add(chasseur(210, 760, 1.4, expr="malin", bras="tient", objet=epuisette(68, -146, 0.8, rot=10)))
    S.add(buisson(250, 780, 1.6))
    for k in range(6):
        S.add(grain(480 + k * 30, 750 - (k % 2) * 12, 1.0))
    S.add(colombe(560, 740, 1.3, expr="content", regard=(0, 1)))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=4)
    sol(S, 600, "#8ce99a")
    S.add(chasseur(260, 760, 1.4, expr="concentre", bras="haut", objet=None))
    S.add(epuisette(300, 540, 1.0, rot=50))
    S.add(colombe(600, 740, 1.3, expr="content", regard=(0, 1)))
    return S


def p12():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 520, "#8ce99a")
    S.add(fourmi(430, 720, 1.6, expr="furieux", bras="course", rot=-12))
    S.add(mouvement(230, 560, 1.4), mouvement(220, 460, 1.1))
    S.add(herbe(700, 760, 1.4), herbe(90, 760, 1.2))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 600, "#8ce99a")
    # gros plan sur la jambe et la chaussure du chasseur
    S.add(rect(360, 0, 150, 700, "#7c4a1e", rx=30))
    S.add(ellipse(430, 720, 150, 60, "#4a2c17"))
    S.add(fourmi(610, 760, 1.1, expr="fache", bras="poing", flip=True))
    S.add(eclat(520, 700, 1.4, "#ffe066"))
    S.add(texte(200, 260, "AÏE !", 100, "#c92a2a", contour="#fff"))
    return S


def p14():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=4)
    sol(S, 600, "#8ce99a")
    S.add(chasseur(220, 690, 1.35, expr="furieux", bras="haut", flip=True))
    S.add(epuisette(160, 780, 0.8, rot=-80))
    S.add(colombe_vol(560, 230, 1.8))
    S.add(mouvement(400, 280, 1.2))
    S.add(fourmi(430, 770, 0.6, expr="rire", bras="haut"))
    return S


def p15():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    S.add(soleil(680, 150, 50, "#ff922b"))
    S.add(rect(0, 560, 800, 240, "#4dabf7"))
    S.add(chemin("M 0 580 Q 200 540 400 560 T 800 560", stroke="#a5d8ff", sw=6))
    branche_ruisseau(S, 330)
    S.add(colombe(420, 342, 1.3, expr="rire", regard=(-1, 0)))
    S.add(fourmi(300, 344, 0.55, expr="rire", bras="haut"))
    S.add(coeur(360, 170, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("brin-d-herbe.svg", vignette),
    ("01-j-ai-soif.svg", p01), ("02-plouf.svg", p02), ("03-au-secours.svg", p03),
    ("04-la-colombe.svg", p04), ("05-le-brin-d-herbe.svg", p05), ("06-le-petit-bateau.svg", p06),
    ("07-sauvee.svg", p07), ("08-merci.svg", p08), ("09-le-chasseur.svg", p09),
    ("10-les-graines.svg", p10), ("11-le-filet.svg", p11), ("12-la-fourmi-court.svg", p12),
    ("13-aie.svg", p13), ("14-envolee.svg", p14), ("15-amies.svg", p15),
]
