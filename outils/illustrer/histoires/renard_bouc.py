"""Le Renard et le Bouc — en toute chose, il faut considérer la fin."""
from fables import *

ID = "renard-bouc"

FERMIER = dict(coiffure="courts", cheveux="gris", peau="doree", habit="#1c7ed6", robe=False, jambes="#364fc7",
               barbe="#adb5bd")


def renard(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **k)


def bouc(x, y, s=1.0, **k):
    return perso("chevre", x, y, s, **k)


def chaleur(S, puits_=None):
    ciel(S, "#ffd8a8", "#fff9db")
    S.add(soleil(660, 120, 60, "#ffa94d"))
    collines(S, 580, "#e9d8a6", graine=41)
    sol(S, 600, "#f3d9a4")
    S.add(caillou(80, 700, 0.8), caillou(730, 740, 0.6), herbe(160, 720, 1.2, "#c49a6c"))
    if puits_:
        S.add(puits(*puits_))


def dans_le_puits(S):
    fond_puits(S, 690)


def couverture():
    S = Scene()
    dans_le_puits(S)
    S.add(bouc(400, 790, 1.25, expr="bouche_bee", bras="haut", regard=(0, -1)))
    S.add(renard(400, 790 - 250 * 1.25, 0.75, expr="malin", bras="haut", regard=(0, -1)))
    S.cachette(220, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(puits(200, 262, 0.55))
    return S


def p01():
    S = Scene()
    chaleur(S)
    S.add(renard(270, 760, 1.4, expr="triste", bras="bouche", regard=(0, 0)))
    S.add(bouc(530, 760, 1.4, expr="triste", bras="bas"))
    S.add(goutte(200, 450, 1.0, "#74c0fc"), goutte(600, 440, 1.0, "#74c0fc"))
    S.add(texte(400, 300, "Qu'il fait chaud !", 48, "#e8590c", contour="#fff"))
    return S


def p02():
    S = Scene()
    chaleur(S, puits_=(420, 700, 1.1))
    S.add(renard(130, 760, 1.1, expr="bouche_bee", bras="joues"))
    S.add(bouc(700, 760, 1.1, expr="joie", bras="haut"))
    return S


def p03():
    S = Scene()
    chaleur(S, puits_=(400, 740, 1.1))
    S.add(renard(300, 420, 1.0, expr="rire", bras="haut", rot=-25))
    S.add(bouc(500, 400, 1.0, expr="rire", bras="haut", rot=25))
    S.add(texte(140, 260, "Plouf !", 56, "#1c7ed6", contour="#fff"), texte(660, 250, "Plouf !", 56, "#1c7ed6", contour="#fff"))
    return S


def p04():
    S = Scene()
    dans_le_puits(S)
    S.add(renard(280, 740, 1.3, expr="miam", bras="porte", objet=goutte(0, -80, 1.2, "#74c0fc")))
    S.add(bouc(530, 740, 1.3, expr="miam", bras="porte", objet=goutte(0, -80, 1.2, "#74c0fc")))
    S.add(texte(400, 260, "Glou glou glou !", 50, "#a5d8ff"))
    S.cachette(120, 730, "air")
    return S


def p05():
    S = Scene()
    dans_le_puits(S)
    S.add(renard(270, 740, 1.3, expr="neutre", bras="bas", regard=(0, -1)))
    S.add(bouc(530, 740, 1.3, expr="inquiet", bras="bas", regard=(0, -1)))
    S.add(bulle(560, 250, 380, 100, "Comment on sort ?", 36, pointe=(540, 430)))
    S.cachette(120, 730, "air")
    return S


def p06():
    S = Scene()
    dans_le_puits(S)
    S.add(renard(270, 740, 1.35, expr="malin", bras="montre", regard=(1, 0)))
    S.add(bouc(560, 740, 1.3, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(300, 230, 420, 110, "J'ai une idée !\nLève tes cornes !", 36, pointe=(270, 450)))
    S.cachette(110, 730, "air")
    return S


def p07():
    S = Scene()
    dans_le_puits(S)
    S.add(renard(250, 740, 1.3, expr="malin", bras="ouverts", regard=(1, 0)))
    S.add(bouc(560, 740, 1.3, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(300, 220, 460, 120, "Je grimpe, je sors,\net je te tire dehors !", 34, pointe=(250, 460)))
    S.add(fleche(560, 360, 560, 190, "#fff", 8, 22))
    S.cachette(100, 730, "air")
    return S


def p08():
    S = Scene()
    dans_le_puits(S)
    S.add(renard(270, 740, 1.3, expr="malin", bras="hanches"))
    S.add(bouc(540, 740, 1.4, expr="rire", bras="joues", regard=(-1, 0)))
    S.add(bulle(520, 220, 420, 100, "Quelle bonne idée !", 38, pointe=(540, 420)))
    S.cachette(120, 730, "air")
    return S


def p09():
    S = Scene()
    dans_le_puits(S)
    S.add(bouc(400, 760, 1.6, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(renard(400, 760 - 250 * 1.6, 0.95, expr="rire", bras="haut", regard=(0, -1)))
    S.add(texte(620, 200, "Hop !", 60, "#fff3bf"))
    S.cachette(220, 730, "air")
    return S


def p10():
    S = Scene()
    chaleur(S, puits_=(420, 740, 1.3))
    S.add(renard(160, 760, 1.2, expr="malin", bras="hanches", regard=(1, 0)))
    S.add(bulle(520, 150, 420, 110, "Et moi ?\nTire-moi dehors !", 38, pointe=(430, 560)))
    return S


def p11():
    S = Scene()
    chaleur(S, puits_=(520, 740, 1.2))
    S.add(renard(220, 760, 1.35, expr="malin", bras="montre", regard=(1, 1)))
    S.add(bulle(330, 120, 520, 130, "Il fallait réfléchir\navant de sauter !", 36, pointe=(230, 440)))
    return S


def p12():
    S = Scene()
    chaleur(S, puits_=(600, 740, 1.0))
    S.add(renard(260, 740, 1.35, expr="rire", bras="coucou", flip=True))
    S.add(mouvement(420, 620, 1.0, rot=180))
    S.add(bulle(260, 150, 360, 100, "Débrouille-toi !", 38, pointe=(260, 430)))
    return S


def p13():
    S = Scene()
    dans_le_puits(S)
    S.add(bouc(400, 740, 1.6, expr="pleure", bras="haut", regard=(0, -1)))
    S.add(texte(400, 240, "Bêêê ! Au secours !", 52, "#fff3bf"))
    S.cachette(220, 730, "air")
    return S


def p14():
    S = Scene()
    dans_le_puits(S)
    S.add(echelle(460, 760, 1.0, h=760, rot=0))
    S.add(personne(470, 250, 0.9, expr="content", bras="donne", flip=True, **FERMIER))
    S.add(bouc(360, 740, 1.4, expr="rire", bras="tient", regard=(1, -1)))
    S.cachette(120, 730, "air")
    return S


def p15():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(soleil(680, 110, 46))
    sol(S, 600, "#8ce99a")
    S.add(rect(460, 650, 340, 150, "#4dabf7"))
    S.add(chemin("M 480 700 q 30 -10 60 0 q 30 10 60 0 q 30 -10 60 0", stroke="#a5d8ff", sw=5))
    S.add(bouc(300, 760, 1.5, expr="concentre", bras="pense", regard=(1, 1)))
    S.add(pensee(560, 250, 120, depuis=(390, 430), contenu=texte(560, 270, "Et après ?", 38, "#846358")))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("puits-seul.svg", vignette),
    ("01-quelle-chaleur.svg", p01), ("02-le-puits.svg", p02), ("03-plouf.svg", p03),
    ("04-glou-glou.svg", p04), ("05-comment-sortir.svg", p05), ("06-une-idee.svg", p06),
    ("07-le-plan.svg", p07), ("08-quelle-bonne-idee.svg", p08), ("09-hop.svg", p09),
    ("10-et-moi.svg", p10), ("11-reflechir.svg", p11), ("12-debrouille-toi.svg", p12),
    ("13-au-secours.svg", p13), ("14-l-echelle.svg", p14), ("15-et-apres.svg", p15),
]
