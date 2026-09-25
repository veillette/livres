"""Le chant de Pinson — être soi-même."""
from base import *
from objets import *

ID = "pinson-chant"
PINSON = dict(couleur="#e8590c", ventre="#ffd8a8")
MERLE = dict(couleur="#495057", ventre="#868e96")
PETIT_MERLE = dict(couleur="#868e96", ventre="#ced4da")
COUCOU = dict(couleur="#74c0fc", ventre="#e7f5ff")
MESANGE = dict(couleur="#fcc419", ventre="#fff3bf")
ROUGEGORGE = dict(couleur="#a47148", ventre="#ff8787")


def foret(S, brume=False):
    ciel(S, "#b2f2bb" if not brume else "#ced4da", "#ebfbee" if not brume else "#f1f3f5")
    S.add(rect(300, 0, 200, 800, "#8d5524"))
    S.add(chemin("M 400 300 Q 600 260 820 280", stroke="#8d5524", sw=34),
          chemin("M 400 520 Q 200 470 -20 490", stroke="#8d5524", sw=34),
          chemin("M 420 700 Q 600 660 820 690", stroke="#8d5524", sw=30))
    for x, y, r in [(80, 80, 140), (400, 30, 170), (720, 90, 150), (760, 460, 90), (40, 380, 90)]:
        S.add(cercle(x, y, r, "#40c057" if not brume else "#8ca99a"))
    S.add(rect(0, 760, 800, 40, "#69db7c"))


def pouet(x, y, taille=70, rot=-8):
    return g([eclat(x, y - taille * 0.3, taille / 30, "#ffd43b", 10), texte(x, y, "POUÊT !", taille, "#e03131", contour="#fff", rot=rot)])


def couverture():
    S = Scene()
    foret(S)
    S.add(oiseau(420, 520, 2.0, expr="chante", bec_ouvert=True, ailes="ouvertes", **PINSON))
    S.add(texte(420, 680, "POUÊT !", 80, "#e03131", contour="#fff", rot=-6))
    S.add(oiseau(200, 500, 1.0, expr="rire", **MESANGE), oiseau(660, 690, 1.0, expr="rire", flip=True, **COUCOU))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(oiseau(200, 262, 1.6, expr="content", **PINSON))
    return S


def p01():
    S = Scene()
    foret(S)
    S.add(oiseau(600, 292, 1.2, expr="chante", **MESANGE), oiseau(730, 287, 1.2, expr="chante", flip=True, **COUCOU))
    S.add(oiseau(160, 500, 1.2, expr="chante", **ROUGEGORGE))
    S.add(texte(660, 170, "Cui-cui !", 36, "#2b8a3e", contour="#fff"), texte(160, 380, "Tuit-tuit !", 36, "#2b8a3e", contour="#fff"))
    S.add(oiseau(560, 692, 1.8, expr="chante", bec_ouvert=True, ailes="ouvertes", **PINSON))
    S.add(pouet(600, 400, 64))
    return S


def p02():
    S = Scene()
    foret(S)
    S.add(oiseau(580, 292, 1.2, expr="rire", ailes="ouvertes", **MESANGE), oiseau(720, 287, 1.2, expr="rire", flip=True, ailes="ouvertes", **COUCOU))
    S.add(oiseau(150, 500, 1.2, expr="rire", ailes="ouvertes", **ROUGEGORGE))
    S.add(oiseau(560, 692, 1.8, expr="timide", **PINSON))
    for x, y in [(560, 160), (230, 380), (720, 170)]:
        S.add(texte(x, y, "Hi hi hi !", 32, "#2b8a3e", contour="#fff"))
    return S


def p03():
    S = Scene()
    foret(S)
    S.add(oiseau(200, 500, 1.4, expr="surpris", **MERLE))
    S.add(texte(220, 300, "Tuu-tuuu…", 40, "#495057", contour="#fff"))
    S.add(oiseau(600, 290, 1.3, expr="chante", bec_ouvert=True, flip=True, **PINSON))
    S.add(pouet(600, 130, 56))
    return S


def p04():
    S = Scene()
    foret(S)
    S.add(oiseau(640, 292, 1.3, expr="surpris", flip=True, **COUCOU))
    S.add(texte(640, 150, "Cou… POUÊT !", 36, "#e03131", contour="#fff"))
    S.add(chouette(150, 500, 1.0, expr="surpris", couleur="#a9805b"))
    S.add(texte(210, 290, "Hou… POUÊT !", 36, "#e03131", contour="#fff"))
    S.add(oiseau(540, 692, 1.7, expr="oups", bec_ouvert=True, **PINSON))
    S.add(texte(560, 430, "Encore raté !", 44, "#495057", contour="#fff"))
    return S


def p05():
    S = Scene()
    foret(S, brume=True)
    S.add(oiseau(560, 480, 1.4, expr="triste", **PINSON))
    S.add(chemin("M 440 440 Q 560 560 680 440 Q 700 500 560 530 Q 420 500 440 440 Z", "#a0693a"))
    for k in range(8):
        S.add(trait(450 + k * 30, 460 + (k % 2) * 10, 470 + k * 30, 500, "#6b4226", 3))
    return S


def brouillard(S, graine=3, opacite=0.75):
    r = random.Random(graine)
    for k in range(14):
        S.add(ellipse(r.uniform(-100, 900), r.uniform(0, 800), r.uniform(150, 300), r.uniform(50, 100), "#f8f9fa", opacity=opacite))


def p06():
    S = Scene()
    foret(S, brume=True)
    brouillard(S, 3)
    S.add(oiseau(200, 690, 0.7, expr="pleure", **PETIT_MERLE))
    S.add(texte(210, 580, "Cui ?", 30, "#868e96"))
    brouillard(S, 9, 0.5)
    S.add(oiseau(620, 290, 1.1, expr="inquiet", flip=True, **MERLE))
    S.add(texte(620, 150, "Petit Merle ?", 36, "#495057", contour="#fff"))
    return S


def p07():
    S = Scene()
    foret(S, brume=True)
    brouillard(S, 4, 0.6)
    for k in range(4):
        S.add(chemin(f"M {430 - k * 60} {470 - k * 50} A {80 + k * 60} {80 + k * 60} 0 0 0 {430 - k * 60} {610 + k * 50}", stroke="#e03131", sw=6, opacity=0.8 - k * 0.15))
    S.add(oiseau(560, 692, 1.8, expr="chante", bec_ouvert=True, ailes="ouvertes", **PINSON))
    S.add(pouet(600, 400, 66))
    S.add(oiseau(160, 520, 0.8, expr="joie", ailes="haut", **PETIT_MERLE))
    S.add(poly([(250, 520), (230, 505), (230, 535)], "#868e96"))
    return S


def p08():
    S = Scene()
    foret(S)
    S.add(oiseau(580, 292, 1.2, expr="chante", bec_ouvert=True, **MESANGE), oiseau(720, 287, 1.2, expr="chante", bec_ouvert=True, flip=True, **COUCOU))
    S.add(oiseau(120, 500, 1.2, expr="chante", bec_ouvert=True, **MERLE), oiseau(250, 502, 0.85, expr="chante", bec_ouvert=True, **PETIT_MERLE))
    S.add(oiseau(560, 692, 1.8, expr="rire", bec_ouvert=True, ailes="ouvertes", **PINSON))
    S.add(texte(400, 130, "POUÊT ! POUÊT !", 64, "#e03131", contour="#fff", rot=-4))
    S.add(notes(640, 420, 1.0, "#e03131"), notes(150, 360, 0.8, "#e03131"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pinson-seul.svg", vignette),
    ("01-pouet.svg", p01), ("02-les-rires.svg", p02), ("03-comme-merle.svg", p03),
    ("04-encore-rate.svg", p04), ("05-dans-le-nid.svg", p05), ("06-brouillard.svg", p06),
    ("07-suis-moi.svg", p07), ("08-en-choeur.svg", p08),
]
