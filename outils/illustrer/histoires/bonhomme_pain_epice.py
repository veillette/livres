"""Le bonhomme de pain d'épice — cours, cours, aussi vite que tu peux !"""
from contes import *

ID = "bonhomme-pain-epice"
MAMIE = dict(coiffure="chignon", cheveux="blanc", peau="rosee", habit="#e64980", acc=("lunettes",))
PAPI = dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="rosee", habit="#1c7ed6", robe=False, jambes="#495057")


def mamie(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def papi(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PAPI, **k})


def bonhomme(x, y, s=1.0, **k):
    return bonhomme_pain_epice(x, y, s, **k)


def court(x, y, s=1.0, flip=False, **k):
    k.setdefault("expr", "rire")
    k.setdefault("bras", "course")
    k.setdefault("course", True)
    return bonhomme_pain_epice(x, y, s, flip=flip, **k)


def vache(x, y, s=1.0, **k):
    corps = perso("boeuf", 0, 0, 1.0, couleur="#f1f3f5", visage="#fff", **k)
    return place([corps, ellipse(-24, -74, 14, 10, "#495057"), ellipse(22, -36, 12, 9, "#495057")], x, y, s)


def cuisine(S):
    interieur(S, "#fff4e6", "#d9a066", 580, papier="#ffe8cc")
    S.add(fenetre(560, 110, 170, 150, dehors="#b2f2bb", rideaux="#fa5252"))


def campagne(S, graine=5):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(690, 100, 40), nuage(160, 110, 0.6))
    collines(S, 580, "#b2f2bb", graine=graine)
    sol(S, 580, "#94d82d")
    S.add(chemin("M 0 740 Q 400 660 800 720 L 800 800 L 0 800 Z", "#f3d9a4"))


def bord_riviere(S):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(160, 110, 0.6))
    sol(S, 520, "#94d82d")
    S.add(chemin("M 0 600 Q 400 560 800 600 L 800 800 L 0 800 Z", "#4dabf7"))
    for k in range(5):
        S.add(chemin(f"M {60 + k * 160} {660 + (k % 2) * 60} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    for dx in (-18, 0, 18):
        S.add(roseau(60 + dx, 600, 0.9, penche=dx / 3, visage_=False))


def couverture():
    S = Scene()
    campagne(S)
    S.add(court(420, 760, 1.6, expr="rire"))
    S.add(mouvement(290, 560, 1.4))
    S.add(mamie(110, 700, 0.8, expr="surpris", bras="course"), perso("renard", 690, 700, 0.8, expr="malin", flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bonhomme(200, 262, 1.0, expr="rire", bras="salut"))
    return S


def p01():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 380, 120, nappe="#fff"))
    S.add(bonhomme(400, 650, 0.7, expr="dort", bras="ouverts"))
    S.add(mamie(180, 790, 1.3, expr="content", bras="donne"), papi(620, 790, 1.3, expr="content", bras="joues"))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(four(560, 790, 1.2, gateau_dedans=False, ouvert=True))
    S.add(court(420, 620, 0.9, expr="rire", bras="haut", flip=True))
    S.add(mamie(170, 790, 1.3, expr="bouche_bee", bras="haut"))
    S.add(texte(400, 150, "Hop !", 90, "#c9772b", contour="#fff"))
    return S


def p03():
    S = Scene()
    campagne(S)
    S.add(maison(140, 600, 0.7, mur="#fff4e6", toit="#e8590c"))
    S.add(court(450, 760, 1.3))
    S.add(bulle(460, 170, 520, 110, "Cours, cours, aussi vite que tu peux !\nTu ne m'attraperas pas !", 28, pointe=(460, 470)))
    return S


def p04():
    S = Scene()
    campagne(S, graine=8)
    S.add(court(640, 750, 0.9))
    S.add(mamie(220, 780, 1.2, expr="oups", bras="course"), papi(420, 780, 1.2, expr="oups", bras="course"))
    S.add(texte(400, 200, "Reviens !", 64, "#c92a2a", contour="#fff"))
    return S


def p05():
    S = Scene()
    campagne(S, graine=11)
    S.add(barriere(200, 640, 0.8, largeur=400))
    S.add(vache(220, 780, 1.2, expr="miam", bras="montre"))
    S.add(court(560, 760, 1.1))
    S.add(bulle(260, 190, 380, 100, "Meuh ! Arrête-toi,\nje veux te manger !", 30, pointe=(230, 480)))
    return S


def p06():
    S = Scene()
    campagne(S, graine=13)
    S.add(perso("cochon", 220, 780, 1.1, expr="miam", bras="montre"))
    S.add(court(560, 760, 1.1))
    S.add(bulle(270, 190, 380, 100, "Groin ! Arrête-toi,\nje veux te manger !", 30, pointe=(230, 500)))
    return S


def p07():
    S = Scene()
    campagne(S, graine=17)
    S.add(court(720, 700, 0.7))
    for k, fn in enumerate((lambda x: mamie(x, 780, 0.8, expr="oups", bras="course"),
                            lambda x: papi(x, 790, 0.8, expr="oups", bras="course"),
                            lambda x: vache(x, 790, 0.8, expr="oups", bras="course"),
                            lambda x: perso("cochon", x, 790, 0.75, expr="oups", bras="course"))):
        S.add(fn(80 + k * 150))
    S.add(texte(400, 200, "En file indienne !", 56, "#c9772b", contour="#fff"))
    return S


def p08():
    S = Scene()
    bord_riviere(S)
    S.add(court(400, 560, 1.2, expr="oups", course=False, bras="joues"))
    S.add(texte(400, 170, "Oh non !", 70, "#1c7ed6", contour="#fff"))
    return S


def p09():
    S = Scene()
    bord_riviere(S)
    S.add(bonhomme(260, 560, 1.0, expr="surpris", bras="bas"))
    S.add(perso("renard", 540, 565, 1.3, expr="malin", bras="montre", flip=True))
    S.add(bulle(460, 160, 460, 100, "Monte sur mon nez, je vais\nte faire traverser !", 30, pointe=(540, 330)))
    return S


def p10():
    S = Scene()
    bord_riviere(S)
    S.add(perso("renard", 400, 780, 1.2, expr="rire", flip=True, regard=(1, -1)))
    S.add(bonhomme(560, 260, 0.9, expr="rire", bras="haut", rot=20))
    S.add(chemin("M 430 470 Q 470 280 560 270", stroke="#fff", sw=5, stroke_dasharray="10 12"))
    return S


def p11():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 520, "#94d82d")
    S.add(chemin("M 0 520 Q 200 500 300 520 L 260 800 L 0 800 Z", "#4dabf7"))
    S.add(perso("renard", 120, 760, 1.0, expr="bouche_bee", regard=(1, 0)))
    S.add(bonhomme(520, 760, 1.3, expr="malin", bras="hanches"))
    S.add(bulle(520, 180, 480, 100, "Tu ne m'attraperas pas,\ntoi non plus !", 32, pointe=(520, 460)))
    return S


def p12():
    S = Scene()
    campagne(S, graine=21)
    S.add(mamie(170, 790, 1.2, expr="inquiet"), papi(320, 790, 1.2, expr="inquiet"), vache(700, 790, 0.9, expr="triste"))
    S.add(bonhomme(520, 780, 1.0, expr="triste", bras="croises"))
    S.add(bulle(420, 170, 480, 110, "Je ne veux pas\nêtre mangé !", 36, pointe=(520, 560)))
    return S


def p13():
    S = Scene()
    campagne(S, graine=23)
    S.add(mamie(250, 790, 1.35, expr="content", bras="ouverts"))
    S.add(bonhomme(500, 790, 1.1, expr="bouche_bee", bras="joues"))
    S.add(bulle(420, 170, 560, 120, "Reviens à la maison :\ntu seras notre petit garçon !", 32, pointe=(260, 460)))
    return S


def p14():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 420, 120, nappe="#fff"))
    for x in (250, 310, 490, 550):
        S.add(bonhomme(x, 655, 0.35, expr="content"))
    S.add(mamie(130, 790, 1.2, expr="rire"), papi(670, 790, 1.2, expr="rire"))
    S.add(bonhomme(400, 655, 0.8, expr="rire", bras="haut"))
    S.add(coeur(400, 250, 1.3))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bonhomme-seul.svg", vignette),
    ("01-le-bonhomme.svg", p01), ("02-hop.svg", p02), ("03-cours-cours.svg", p03), ("04-reviens.svg", p04),
    ("05-la-vache.svg", p05), ("06-le-cochon.svg", p06), ("07-en-file.svg", p07), ("08-la-riviere.svg", p08),
    ("09-le-renard.svg", p09), ("10-le-saut.svg", p10), ("11-toi-non-plus.svg", p11), ("12-pas-mange.svg", p12),
    ("13-notre-petit-garcon.svg", p13), ("14-les-biscuits.svg", p14),
]
