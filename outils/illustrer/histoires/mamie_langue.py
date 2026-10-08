"""Mamie parle une autre langue — langues de famille et accents.

Nora vit au Kentucky : français à la maison, anglais à l'école. Sa grand-mère
Rosa arrive du Portugal et parle portugais. D'abord intimidée, Nora apprend
à se comprendre avec les gestes, la cuisine, les chansons et quelques mots
(olá, obrigada, gato, beijinho, bom dia…).
"""
from base import *
from objets import *
from fantastique import personne

ID = "mamie-langue"
NORA = dict(peau="doree", cheveux="brun", coiffure="boucles", habit="#fd7e14", robe=True)
AVO = dict(peau="claire", cheveux="gris", coiffure="chignon", habit="#c2255c", robe=True, acc=("lunettes",))
PAPA = dict(peau="claire", cheveux="brun", coiffure="courts", habit="#1971c2", robe=False, jambes="#343a40")


def nora(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**NORA, **k})


def avo(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**AVO, **k})


def papa(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**PAPA, **k})


def aeroport(S):
    S.add(rect(0, 0, 800, 800, "#e7f5ff"))
    S.add(rect(0, 80, 800, 380, "#a5d8ff"))
    for k in range(0, 800, 160):
        S.add(rect(k, 80, 12, 380, "#ced4da"))
    S.add(rect(0, 440, 800, 30, "#ced4da"))
    S.add(rect(0, 600, 800, 200, "#dee2e6"))
    for k in range(0, 800, 100):
        S.add(trait(k, 600, k - 40, 800, "#ced4da", 3))
    S.add(avion(560, 250, 0.9))


def avion(x, y, s=1.0, rot=-8):
    m = [ellipse(0, 0, 170, 30, "#ffffff", stroke="#adb5bd", stroke_width=3),
         chemin("M -20 0 L -80 70 L -40 70 L 50 6 Z", "#ced4da"), chemin("M -130 -6 L -170 -60 L -140 -60 L -100 -10 Z", "#e8590c"),
         chemin("M 140 -16 Q 170 -10 170 0 L 140 0 Z", "#74c0fc")]
    m += [cercle(-80 + k * 32, -6, 6, "#74c0fc") for k in range(7)]
    return place(m, x, y, s, rot=rot)


def pancarte(x, y, s=1.0, mot="Bem-vinda !"):
    return place([rect(-6, 0, 12, 120, "#a0693a"), rect(-130, -70, 260, 80, "#fff9db", rx=10, stroke="#f08c00", stroke_width=5),
                  texte(0, -18, mot, 36, "#e8590c")], x, y, s)


def maison_dedans(S, mur="#fff4e6", papier="#ffe8cc"):
    interieur(S, mur, "#e8c39e", y=600, papier=papier)


def pasteis(x, y, s=1.0, nb=5):
    m = [ellipse(0, 0, 130, 22, "#ffffff", stroke="#dee2e6", stroke_width=3)]
    for k in range(nb):
        cx = -80 + k * 40
        m += [ellipse(cx, -14, 20, 10, "#e8a200"), ellipse(cx, -16, 14, 6, "#ffe066"), cercle(cx + 3, -17, 3, "#a0522d")]
    return place(m, x, y, s)


def tablette(x, y, s=1.0, ecran=""):
    m = [rect(-130, -95, 260, 190, "#343a40", rx=16), rect(-116, -82, 232, 164, "#d0ebff", rx=6)]
    if ecran:
        cid = uid("c")
        m.append(el("clipPath", rect(-116, -82, 232, 164, "#000", rx=6), id=cid))
        m.append(g(ecran, clip_path=f"url(#{cid})"))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#fff4e6")
    for k, (mot, c) in enumerate((("Bonjour", "#1971c2"), ("Hello", "#2f9e44"), ("Olá", "#c2255c"))):
        S.add(texte(160 + k * 240, 300 + (k % 2) * 50, mot, 50, c, contour="#fff", rot=(-8, 6, -4)[k]))
    S.add(avo(500, 780, 1.75, expr="rire", bras="calin", flip=True))
    S.add(nora(300, 780, 1.45, expr="rire", bras="calin", regard=(1, -1)))
    S.add(coeur(400, 420, 1.3, "#ff6b6b"))
    S.cachette(730, 400, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(texte(320, 70, "Olá !", 44, "#c2255c"))
    S.add(nora(160, 262, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    aeroport(S)
    S.add(papa(250, 780, 1.45, expr="content", bras="donne", regard=(1, 0)))
    S.add(nora(470, 780, 1.15, expr="joie", bras="tient"))
    S.add(pancarte(548, 500, 1.0))
    return S


def p02():
    S = Scene()
    aeroport(S)
    S.add(avo(560, 780, 1.5, expr="rire", bras="ouverts", flip=True, regard=(-1, 1)))
    S.add(rect(700, 640, 70, 120, "#e8590c", rx=12), rect(722, 610, 26, 36, "none", rx=8, stroke="#343a40", stroke_width=6))
    S.add(papa(170, 780, 1.45, expr="content", regard=(1, 0)))
    S.add(nora(270, 780, 1.05, expr="timide", bras="bouche", regard=(1, 0)))
    S.add(bulle(560, 260, 400, 80, "Olá, minha querida !", 36, pointe=(560, 440)))
    S.add(texte(290, 450, "?", 80, "#e8590c", contour="#fff"))
    S.cachette(730, 340, "air")
    return S


def p03():
    S = Scene()
    maison_dedans(S)
    S.add(cadre_mur(160, 160, 160, 120, "#ffd8a8"), cadre_mur(620, 170, 130, 100, "#b2f2bb"))
    S.add(papa(360, 780, 1.5, expr="content", bras="calin", flip=True, regard=(-1, 1)))
    S.add(nora(220, 780, 1.1, expr="sourire", regard=(1, -1)))
    S.add(pensee(590, 320, 130, g([personne(560, 420, 0.7, **{**AVO, "cheveux": "brun"}, expr="rire", bras="calin"),
                                     personne(630, 420, 0.45, peau="claire", cheveux="brun", coiffure="courts", habit="#40c057", robe=False, expr="rire")]),
                 depuis=(420, 470)))
    return S


def p04():
    S = Scene()
    maison_dedans(S)
    S.add(lampe(690, 600, 1.1))
    S.add(nora(220, 700, 1.15, expr="content", bras="porte", regard=(1, 0)))
    S.add(avo(560, 700, 1.3, expr="rire", bras="porte", flip=True, regard=(-1, 0)))
    S.add(table(400, 790, 640, 150, "#c68642", nappe="#ffc9c9"))
    S.add(assiette(270, 625, 0.9), assiette(540, 625, 0.9), bol(400, 620, 0.9, "#ffa94d", "#ffd8a8", cuillere=False))
    S.add(bulle(560, 160, 260, 80, "Obrigada !", 40, pointe=(560, 340)))
    S.add(bulle(220, 250, 260, 80, "Obrigada !", 40, pointe=(220, 420)))
    return S


def p05():
    S = Scene()
    maison_dedans(S, "#fff9db", "#ffe8a3")
    S.add(four(680, 600, 0.9))
    S.add(nora(250, 700, 1.15, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(avo(500, 700, 1.3, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(table(400, 790, 640, 150, "#c68642"))
    S.add(pasteis(400, 630, 1.1))
    S.add(texte(400, 160, "Hmm !", 60, "#e8590c", contour="#fff"))
    S.add(coeur(380, 260, 0.9, "#ff6b6b"))
    return S


def p06():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    S.add(fenetre(530, 100, 190, 170, "#1c2a52", "#e5dbff", nuit_=True))
    S.add(lit(330, 760, 460, "#e5dbff", "#ff922b"))
    cid = uid("c")
    S.add(el("clipPath", rect(0, 0, 800, 690, "#000"), id=cid))
    S.add(g(nora(215, 742, 0.9, expr="dort"), clip_path=f"url(#{cid})"))
    S.add(rect(140, 672, 420, 70, "#ff922b", rx=18))
    S.add(avo(640, 790, 1.35, expr="chante", flip=True))
    S.add(notes(500, 380, 1.2, "#e5dbff"), notes(400, 300, 0.9, "#e5dbff"))
    return S


def p07():
    S = Scene()
    maison_dedans(S)
    S.add(perso("chat", 400, 760, 1.0, expr="content", couleur="#868e96", visage="#f1f3f5"))
    S.add(nora(170, 780, 1.2, expr="rire", bras="montre", regard=(1, 1)))
    S.add(avo(640, 780, 1.35, expr="rire", bras="montre", flip=True, regard=(-1, 1)))
    S.add(texte(400, 260, "chat", 56, "#1971c2", contour="#fff"))
    S.add(texte(230, 360, "cat", 48, "#2f9e44", contour="#fff", rot=-6))
    S.add(texte(570, 360, "gato", 48, "#c2255c", contour="#fff", rot=6))
    S.cachette(250, 70, "air")
    return S


def p08():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600, papier="#ffe8a3")
    S.add(rect(150, 90, 500, 240, "#2b8a3e", rx=10, stroke="#a0693a", stroke_width=14))
    S.add(texte(400, 200, "Hello!", 64, "#ffffff", poids=500))
    S.add(nora(400, 780, 1.35, expr="fier", bras="salut"))
    S.add(personne(160, 770, 1.1, peau="claire", cheveux="blond", coiffure="courts", habit="#4dabf7", robe=False, expr="content", regard=(1, 0)))
    S.add(personne(650, 770, 1.1, peau="foncee", cheveux="noir", coiffure="tresses", habit="#9775fa", robe=True, expr="content", flip=True, regard=(-1, 0)))
    S.add(notes(560, 470, 0.9, "#e8590c"))
    S.cachette(70, 260, "air")
    return S


def p09():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 600, "#b2f2bb", graine=3)
    sol(S, 600, "#8ce99a", couleur2="#7bd88a", y2=680)
    S.add(arbre(110, 620, 1.0), arbre(700, 610, 0.9))
    S.add(avo(470, 770, 1.45, expr="rire", bras="calin", flip=True))
    S.add(nora(350, 770, 1.15, expr="rire", bras="calin", regard=(1, -1)))
    S.add(coeur(420, 380, 1.0, "#ff6b6b"), coeur(470, 330, 0.7, "#ff8787"))
    S.add(bulle(600, 180, 260, 80, "Beijinho !", 40, pointe=(520, 380)))
    return S


def p10():
    S = Scene()
    aeroport(S)
    S.add(papa(150, 780, 1.45, expr="sourire", regard=(1, 0)))
    S.add(avo(560, 780, 1.5, expr="content", bras="calin", flip=True, larmes=True, regard=(-1, 1)))
    S.add(nora(400, 780, 1.1, expr="content", bras="calin", regard=(1, -1)))
    S.add(bulle(400, 150, 460, 80, "Gosto muito de ti !", 38, pointe=(400, 520)))
    return S


def p11():
    S = Scene()
    maison_dedans(S, "#e7f5ff", "#d0ebff")
    ecran = g([rect(-116, -82, 232, 164, "#fff0f6"), avo(0, 120, 0.85, expr="rire", bras="salut")])
    S.add(table(450, 790, 520, 170, "#c68642"))
    S.add(tablette(560, 470, 1.2, ecran))
    S.add(nora(260, 780, 1.3, expr="rire", bras="salut", regard=(1, -1)))
    S.add(bulle(260, 170, 280, 80, "Bom dia, avó !", 36, pointe=(280, 440)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("nora-seule.svg", vignette),
    ("01-l-aeroport.svg", p01), ("02-ola.svg", p02), ("03-la-langue-de-papa.svg", p03),
    ("04-obrigada.svg", p04), ("05-les-pasteis.svg", p05), ("06-la-berceuse.svg", p06),
    ("07-chat-cat-gato.svg", p07), ("08-a-l-ecole.svg", p08), ("09-beijinho.svg", p09),
    ("10-au-revoir.svg", p10), ("11-bom-dia.svg", p11),
]
