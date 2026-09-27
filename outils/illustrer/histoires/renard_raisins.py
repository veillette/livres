"""Le Renard et les Raisins — faire semblant de ne pas vouloir."""
from fables import *

ID = "renard-raisins"


def renard(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **k)


def rouge_gorge(x, y, s=1.0, **k):
    k.setdefault("couleur", "#a0693a")
    k.setdefault("ventre", "#ff922b")
    return oiseau(x, y, s, **k)


def vigne(S, grappes=((200, 204), (400, 210), (600, 200)), soir=False, treille_y=190):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#fff9db")
    S.add(soleil(700, 90, 40, "#ffa94d" if soir else "#ffd43b"))
    collines(S, 580, "#b2f2bb", graine=101)
    sol(S, 600, "#8ce99a")
    treille(S, treille_y)
    for gx, gy in grappes:
        S.add(raisins(gx, gy, 1.3))


def couverture():
    S = Scene()
    vigne(S, grappes=((260, 354), (500, 360)), treille_y=340)
    S.add(renard(390, 790, 1.35, expr="miam", bras="haut", regard=(0, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(raisins(200, 20, 2.0))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 110, 46))
    collines(S, 580, "#b2f2bb", graine=102)
    sol(S, 600, "#8ce99a")
    S.add(chemin("M 0 720 Q 400 660 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(renard(400, 740, 1.7, expr="triste", bras="calin"))
    S.add(texte(620, 330, "Grrr…", 50, "#6f42c1", contour="#fff"))
    return S


def p02():
    S = Scene()
    vigne(S)
    S.add(renard(400, 760, 1.5, expr="bouche_bee", bras="joues", regard=(0, -1)))
    S.add(paillettes(300, 380, 0.8), paillettes(520, 380, 0.8))
    return S


def p03():
    S = Scene()
    vigne(S)
    S.add(renard(400, 640, 1.4, expr="concentre", bras="haut", regard=(0, -1), pieds_haut=True))
    S.add(mouvement(400, 700, 1.0, rot=90))
    S.add(texte(620, 480, "Hop !", 56, "#6f42c1", contour="#fff"))
    return S


def p04():
    S = Scene()
    vigne(S)
    S.add(renard(300, 600, 1.35, expr="concentre", bras="haut", regard=(0, -1), pieds_haut=True, rot=-8))
    S.add(mouvement(300, 660, 1.0, rot=90))
    S.add(texte(560, 450, "Hop ! Hop !", 56, "#6f42c1", contour="#fff"))
    return S


def p05():
    S = Scene()
    vigne(S)
    S.add(renard(420, 760, 1.4, expr="oups", bras="large", pieds_haut=True))
    S.add(eclat(420, 760, 1.4, "#ffe066"))
    S.add(texte(620, 450, "BOUM !", 64, "#c92a2a", contour="#fff"))
    S.add(etoile5(380, 440, 14, "#ffd43b"), etoile5(470, 430, 12, "#ffd43b"))
    return S


def p06():
    S = Scene()
    vigne(S)
    for k, (cx, cy) in enumerate([(330, 760), (430, 770), (380, 730), (500, 750)]):
        S.add(caillou(cx, cy, 1.0 + (k % 2) * 0.2))
    S.add(renard(420, 620, 1.2, expr="oups", bras="haut", rot=25))
    S.add(texte(180, 450, "Badaboum !", 50, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    vigne(S)
    S.add(renard(400, 760, 1.4, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(baton(460, 580, 440, 300, ep=12))
    S.add(texte(630, 470, "Presque…", 44, "#6f42c1", contour="#fff"))
    return S


def p08():
    S = Scene()
    vigne(S)
    S.add(renard(400, 770, 1.4, expr="triste", bras="bas", regard=(0, -1)))
    S.add(ellipse(400, 770, 90, 14, "#2b8a3e", opacity=0.3))
    return S


def p09():
    S = Scene()
    vigne(S)
    S.add(rouge_gorge(560, 180, 0.9, expr="malin", regard=(-1, 1)))
    S.add(renard(300, 770, 1.4, expr="fache", bras="croises", regard=(1, -1)))
    S.add(bulle(560, 400, 400, 110, "Alors, Renard,\ntu n'y arrives pas ?", 32, pointe=(560, 250)))
    return S


def p10():
    S = Scene()
    vigne(S)
    S.add(rouge_gorge(560, 180, 0.9, expr="surpris", regard=(-1, 1)))
    S.add(renard(300, 770, 1.45, expr="fier", bras="hanches", regard=(0, -1)))
    S.add(bulle(560, 430, 400, 120, "Ils sont trop verts !\nJe n'en veux pas !", 32, pointe=(380, 500)))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=102)
    sol(S, 600, "#8ce99a")
    S.add(chemin("M 0 720 Q 400 660 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(renard(420, 740, 1.6, expr="fier", bras="bas", regard=(1, -1), flip=True))
    S.add(texte(630, 560, "Grrrr…", 48, "#6f42c1", contour="#fff"))
    S.add(texte(630, 610, "(son ventre)", 28, "#6f42c1", contour="#fff"))
    return S


def p12():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=102)
    sol(S, 600, "#8ce99a")
    S.add(arbre(640, 620, 1.2))
    S.add(renard(280, 760, 1.4, expr="triste", bras="bas", regard=(1, 0)))
    S.add(perso("ecureuil", 540, 760, 1.2, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(520, 150, 460, 110, "Pourquoi fais-tu\ncette tête, Renard ?", 34, pointe=(540, 460)))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 580, "#b2f2bb", graine=102)
    sol(S, 600, "#8ce99a")
    S.add(arbre(640, 620, 1.2))
    S.add(renard(280, 760, 1.4, expr="timide", bras="calin", regard=(1, 0)))
    S.add(perso("ecureuil", 540, 760, 1.2, expr="sourire", bras="bas", regard=(-1, 0)))
    S.add(bulle(300, 130, 480, 130, "En vrai, ils sont mûrs…\nC'est moi qui n'y\narrive pas.", 32, pointe=(280, 440)))
    return S


def p14():
    S = Scene()
    vigne(S, grappes=((200, 204), (600, 200)))
    S.add(perso("ecureuil", 420, 330, 0.9, expr="rire", bras="haut"))
    S.add(raisins(470, 400, 1.3))
    S.add(mouvement(470, 540, 1.0, rot=90))
    S.add(renard(320, 770, 1.4, expr="joie", bras="haut", regard=(1, -1)))
    return S


def p15():
    S = Scene()
    vigne(S, grappes=((200, 204), (600, 200)), soir=True)
    S.add(renard(270, 760, 1.4, expr="miam", bras="porte", objet=raisins(0, -120, 0.8, feuille=False)))
    S.add(perso("ecureuil", 530, 770, 1.2, expr="miam", bras="porte", objet=raisins(0, -110, 0.7, feuille=False)))
    S.add(coeur(400, 360, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("raisins-seuls.svg", vignette),
    ("01-renard-a-faim.svg", p01), ("02-les-raisins.svg", p02), ("03-hop.svg", p03),
    ("04-hop-hop.svg", p04), ("05-boum.svg", p05), ("06-badaboum.svg", p06),
    ("07-le-baton.svg", p07), ("08-epuise.svg", p08), ("09-le-rouge-gorge.svg", p09),
    ("10-trop-verts.svg", p10), ("11-le-nez-en-l-air.svg", p11), ("12-l-ecureuil.svg", p12),
    ("13-la-verite.svg", p13), ("14-l-ecureuil-grimpe.svg", p14), ("15-delicieux.svg", p15),
]
