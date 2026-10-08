"""Le Chat botté — l'intelligence vaut mieux qu'un trésor."""
from contes import *

ID = "chat-botte"
JEAN = dict(coiffure="courts", cheveux="chatain", peau="claire", habit="#a0693a", robe=False, jambes="#6d4424", chaussures="#5c3a1e")
JEAN_BEAU = dict(habit="#1864ab", jambes="#f8f9fa", cape="#e64980", acc=("col",), chaussures="#343a40")
PRINCESSE = dict(coiffure="tres_longs", cheveux="noir", peau="doree", habit="#f783ac", acc=("diademe",))
FRERES = [dict(coiffure="herisses", cheveux="chatain", peau="claire", habit="#2f9e44", robe=False, jambes="#6d4424"),
          dict(coiffure="courts", cheveux="brun", peau="claire", habit="#e8590c", robe=False, jambes="#6d4424")]
PAYSANS = [dict(coiffure="courts", cheveux="noir", peau="brune", habit="#fcc419", robe=False, jambes="#5c3a1e"),
           dict(coiffure="tresses", cheveux="roux", peau="claire", habit="#74c0fc")]


def chat(x, y, s=1.0, **k):
    return chat_botte(x, y, s, **k)


def jean(x, y, s=1.0, beau=False, **k):
    d = dict(JEAN)
    if beau:
        d.update(JEAN_BEAU)
    d.update(k)
    return personne(x, y, s, **d)


def princesse_(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PRINCESSE, **k})


def ogre(x, y, s=2.4, **k):
    k.setdefault("habit", "#c92a2a")
    k.setdefault("peau", "#b2dba1")
    k.setdefault("cheveux", "noir")
    k.setdefault("barbe", "#212529")
    return geant(x, y, s, **k)


def campagne(S, ble_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(690, 100, 40), nuage(160, 110, 0.6))
    collines(S, 580, "#b2f2bb", graine=31)
    sol(S, 580, "#94d82d")
    if ble_:
        for k in range(16):
            S.add(ble(10 + k * 52, 640 + (k % 2) * 16, 1.0))
    S.add(chemin("M 0 760 Q 400 690 800 730 L 800 800 L 0 800 Z", "#f3d9a4"))


def salle_trone(S):
    interieur(S, "#fff3bf", "#c9a27e", 580, papier="#ffe066")
    S.add(rect(300, 200, 200, 380, "#c92a2a"), rect(330, 230, 140, 300, "#e03131"))
    for x in (60, 740):
        S.add(rect(x - 30, 0, 60, 580, "#fff"))


def salle_ogre(S):
    interieur(S, "#ced4da", "#868e96", 600, plinthe="#495057")
    for row in range(8):
        for col in range(6):
            S.add(rect(col * 140 - (row % 2) * 70, row * 75, 132, 68, "#dee2e6", rx=6, opacity=0.7))
    S.add(rect(0, 600, 800, 200, "#868e96"))


def couverture():
    S = Scene()
    campagne(S)
    S.add(chat(400, 790, 1.7, expr="malin", bras="salut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chat(200, 262, 0.95, expr="malin", bras="salut"))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=8)
    sol(S, 600, "#94d82d")
    S.add(moulin(170, 640, 0.9))
    S.add(personne(420, 790, 1.1, **FRERES[0], expr="rire", bras="tient", objet=place(moulin(0, 0, 0.18), 68, -150)))
    S.add(perso("ane", 560, 790, 0.9, expr="content"), personne(640, 790, 1.0, **FRERES[1], expr="content", bras="salut"))
    S.add(jean(290, 790, 1.1, expr="triste"), chat(250, 790, 0.45, bottes=False, chapeau_=False, expr="sourire"))
    return S


def p02():
    S = Scene()
    campagne(S, ble_=False)
    S.add(jean(250, 790, 1.35, expr="triste", bras="tete"))
    S.add(chat(530, 790, 1.1, bottes=False, chapeau_=False, expr="malin", bras="montre", flip=True))
    S.add(bulle(460, 150, 480, 110, "Donne-moi un sac et des bottes,\net tu verras !", 30, pointe=(520, 540)))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    foret(S, graine=21)
    S.add(sac(560, 780, 1.0), perso("lapin", 560, 740, 0.5, expr="surpris"))
    S.add(chat(260, 790, 1.4, expr="malin", bras="tire"))
    return S


def p04():
    S = Scene()
    salle_trone(S)
    S.add(roi(420, 790, 1.4, expr="rire", bras="ouverts"))
    S.add(chat(180, 790, 1.1, expr="fier", bras="donne", objet=place(perso("lapin", 0, 0, 0.35, expr="dort"), 86, -60)))
    S.add(bulle(460, 110, 540, 100, "Un cadeau de mon maître,\nle marquis de Carabas !", 30, pointe=(220, 480)))
    return S


def p05():
    S = Scene()
    salle_trone(S)
    S.add(roi(560, 790, 1.3, expr="rire", bras="haut"))
    S.add(chat(220, 790, 1.1, expr="fier", bras="donne2", objet=place(g([oiseau(0, 0, 0.4, "#a0693a", expr="dort"), oiseau(30, 10, 0.4, "#8d5524", expr="dort")]), 80, -80)))
    S.add(texte(400, 150, "Encore un cadeau !", 56, "#c92a2a", contour="#fff"))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 520, "#94d82d")
    S.add(chemin("M 0 600 Q 400 560 800 610 L 800 800 L 0 800 Z", "#4dabf7"))
    S.add(g([cercle(420, 640, 60, "#4dabf7")]))
    S.add(personne(420, 760, 1.0, **{**JEAN, "habit": "#fbd9bd", "jambes": "#fbd9bd"}, expr="rire", bras="haut"))
    S.add(rect(300, 660, 240, 140, "#4dabf7"))
    S.add(chat(160, 590, 1.1, expr="malin", bras="montre"))
    S.add(bulle(260, 170, 420, 100, "Maître, va vite\nte baigner !", 34, pointe=(180, 380)))
    return S


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 560, "#94d82d")
    S.add(chemin("M 0 740 Q 400 700 800 740 L 800 800 L 0 800 Z", "#4dabf7"))
    S.add(carrosse(520, 700, 0.8, couleur="#fcc419"))
    S.add(roi(470, 450, 0.45, expr="surpris"))
    S.add(chat(170, 700, 1.1, expr="oups", bras="haut"))
    S.add(bulle(360, 150, 560, 110, "Au secours ! On a volé les habits\ndu marquis de Carabas !", 28, pointe=(200, 440)))
    return S


def p08():
    S = Scene()
    campagne(S, ble_=False)
    S.add(carrosse(560, 760, 0.7, couleur="#fcc419"))
    S.add(jean(200, 790, 1.35, beau=True, expr="fier", bras="salut"))
    S.add(princesse_(380, 790, 1.15, expr="timide", bras="joues"))
    S.add(coeur(300, 330, 1.2))
    return S


def p09():
    S = Scene()
    campagne(S)
    S.add(personne(470, 790, 1.2, **PAYSANS[0], expr="surpris", bras="tient", objet=place(g([trait(0, 0, 0, -150, "#a0522d", 8)]), 68, -80)))
    S.add(personne(640, 790, 1.15, **PAYSANS[1], expr="inquiet"))
    S.add(chat(220, 790, 1.2, expr="malin", bras="montre"))
    S.add(bulle(400, 150, 560, 110, "Dites au roi que ces champs\nsont au marquis de Carabas !", 28, pointe=(260, 480)))
    return S


def p10():
    S = Scene()
    salle_ogre(S)
    S.add(ogre(560, 830, 2.5, expr="fier", bras="hanches"))
    S.add(chat(170, 800, 1.0, expr="malin", bras="salut"))
    S.add(bulle(260, 150, 420, 110, "On dit que vous pouvez\ndevenir n'importe quoi ?", 28, pointe=(180, 540)))
    S.cachette(320, 730, "air")
    return S


def p11():
    S = Scene()
    salle_ogre(S)
    S.add(perso("lion", 520, 800, 2.0, expr="furieux", bras="poing"))
    S.add(chat(170, 800, 1.0, expr="oups", bras="haut"))
    S.add(texte(520, 120, "ROAR !", 90, "#e8590c", contour="#fff"))
    S.add(etincelles(520, 380, 2.0, "#fff", graine=3))
    return S


def p12():
    S = Scene()
    salle_ogre(S)
    S.add(etincelles(500, 700, 1.4, "#fff", graine=4))
    S.add(perso("souris", 500, 800, 0.5, expr="fier", bras="hanches"))
    S.add(chat(200, 800, 1.2, expr="malin", bras="hanches"))
    S.add(bulle(420, 180, 540, 110, "Et en toute petite souris ?\nJe parie que non !", 30, pointe=(220, 520)))
    return S


def p13():
    S = Scene()
    salle_ogre(S)
    S.add(rect(700, 740, 50, 60, "#212529", rx=24))
    S.add(perso("souris", 640, 800, 0.4, expr="oups", bras="course"))
    S.add(chat(330, 800, 1.3, expr="rire", bras="course"))
    S.add(mouvement(560, 700, 1.0))
    S.add(texte(400, 180, "Hop !", 90, "#c92a2a", contour="#fff"))
    return S


def p14():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 600, "#94d82d")
    S.add(chateau(400, 620, 0.9, mur="#dee2e6", mur2="#ced4da", toit="#1c7ed6"))
    S.add(carrosse(610, 790, 0.7, couleur="#fcc419"))
    S.add(chat(170, 790, 1.3, expr="fier", bras="ouverts"))
    S.add(bulle(360, 130, 540, 110, "Bienvenue au château\ndu marquis de Carabas !", 30, pointe=(180, 530)))
    return S


def p15():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6)
    S.add(jean(290, 790, 1.3, beau=True, expr="rire", bras="salut"), princesse_(470, 790, 1.3, habit="#f8f9fa", expr="rire", bras="haut"))
    S.add(chat(660, 790, 1.2, expr="fier", bras="haut", plume="#fcc419"))
    S.add(coeur(380, 280, 1.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chat-seul.svg", vignette),
    ("01-l-heritage.svg", p01), ("02-un-sac-et-des-bottes.svg", p02), ("03-la-chasse.svg", p03), ("04-le-roi.svg", p04),
    ("05-encore-un-cadeau.svg", p05), ("06-la-baignade.svg", p06), ("07-au-secours.svg", p07), ("08-la-princesse.svg", p08),
    ("09-les-paysans.svg", p09), ("10-l-ogre.svg", p10), ("11-le-lion.svg", p11), ("12-la-souris.svg", p12),
    ("13-hop.svg", p13), ("14-le-chateau.svg", p14), ("15-le-mariage.svg", p15),
]
