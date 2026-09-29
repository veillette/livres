"""La soupe au caillou — quand chacun apporte un peu, tout le monde a beaucoup."""
from contes import *

ID = "soupe-caillou"
VOYAGEUR = dict(coiffure="courts", cheveux="noir", barbe="#343a40", peau="doree", habit="#6d4424", robe=False, jambes="#495057",
                cape="#2f9e44")
GENS = [dict(coiffure="tresses", cheveux="roux", peau="claire", habit="#e64980"),
        dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="rosee", habit="#1c7ed6", robe=False, jambes="#495057"),
        dict(coiffure="chignon", cheveux="brun", peau="foncee", habit="#fcc419"),
        dict(coiffure="herisses", cheveux="blond", peau="claire", habit="#51cf66", robe=False, jambes="#1864ab"),
        dict(coiffure="courts", cheveux="chatain", peau="brune", habit="#f8f9fa", robe=False, jambes="#495057", acc=("toque",))]


def caillou_rond(x, y, s=1.0):
    """Le caillou tout rond et tout lisse du voyageur ; (x, y) = dessous."""
    m = [ellipse(0, -30, 46, 32, "#adb5bd"), ellipse(4, -24, 40, 24, "#ced4da"), ellipse(-14, -42, 13, 7, "#fff", opacity=0.7),
         cercle(18, -20, 3, "#868e96"), cercle(-6, -14, 2.5, "#868e96")]
    return place(m, x, y, s)


def voyageur(x, y, s=1.2, **k):
    return personne(x, y, s, **{**VOYAGEUR, **k})


def villageois(i, x, y, s=1.0, **k):
    return personne(x, y, s, **{**GENS[i], **k})


def place_village(S, soir=True, neige=True):
    if soir:
        ciel(S, "#364fc7", "#ffa8a8")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
    S.add(maison(110, 560, 0.7, toit="#e8590c", lumiere=soir), maison(400, 540, 0.6, toit="#1c7ed6", mur="#fff3bf", lumiere=soir),
          maison(690, 560, 0.7, toit="#c2255c", mur="#e7f5ff", lumiere=soir))
    S.add(rect(0, 560, 800, 240, "#e9ecef"))
    if neige:
        S.add(g([poly([(0, 560), (800, 560), (800, 570), (0, 570)], "#fff")]))
        flocons(S, 30, graine=7, zone=(0, 0, 800, 560))


def feu_marmite(x, y, s=1.0, contenu="#74c0fc", fumee=True):
    return chaudron(x, y, s, contenu=contenu, fumee=fumee)


def couverture():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(430, 760, 1.0, "#ffd43b"))
    S.add(voyageur(200, 790, 1.35, expr="rire", bras="tient", objet=place(caillou_rond(0, 0, 0.8), 68, -146)))
    S.add(villageois(0, 640, 790, 1.0, expr="bouche_bee", bras="joues"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(caillou_rond(200, 220, 2.2))
    return S


def p01():
    S = Scene()
    place_village(S)
    S.add(voyageur(400, 790, 1.4, expr="triste", bras="tient", objet=baluchon(68, -146, 0.8)))
    return S


def p02():
    S = Scene()
    ciel(S, "#364fc7", "#ffa8a8")
    flocons(S, 25, graine=3)
    S.add(rect(0, 560, 800, 240, "#e9ecef"))
    S.add(maison(560, 640, 1.5, toit="#e8590c", lumiere=True))
    S.add(voyageur(220, 790, 1.3, expr="triste", bras="donne"))
    S.add(bulle(520, 150, 460, 100, "Non, non,\nnous n'avons rien !", 36, pointe=(560, 440)))
    S.add(texte(300, 400, "Clac !", 60, "#c92a2a", contour="#fff"))
    return S


def p03():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(460, 760, 1.1, fumee=False))
    S.add(voyageur(220, 790, 1.35, expr="content", bras="porte", objet=g([rect(-40, -80, 80, 14, "#8d5524", rx=6), rect(-36, -94, 72, 14, "#a0522d", rx=6)])))
    return S


def p04():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(460, 760, 1.1))
    S.add(caillou_rond(460, 560, 0.7), goutte(420, 580, 1.2, "#a5d8ff"), goutte(500, 575, 1.0, "#a5d8ff"))
    S.add(voyageur(220, 790, 1.35, expr="malin", bras="donne"))
    S.add(texte(460, 380, "Plouf !", 70, "#1c7ed6", contour="#fff"))
    return S


def p05():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(400, 760, 1.0))
    S.add(voyageur(170, 790, 1.3, expr="malin", bras="pense"))
    S.add(villageois(0, 620, 790, 1.0, expr="surpris", regard=(-1, 0)))
    S.add(bulle(380, 140, 540, 110, "Une soupe au caillou ! Mais avec\nune carotte, ce serait meilleur…", 28, pointe=(200, 460)))
    return S


def p06():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(400, 760, 1.0, "#ffc078"))
    S.add(voyageur(170, 790, 1.3, expr="rire"))
    S.add(villageois(0, 600, 790, 1.0, expr="rire", bras="donne2", objet=carotte(90, -110, 0.8, rot=-60)))
    S.add(texte(400, 380, "Plouf !", 60, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(400, 760, 1.0, "#ffc078"))
    S.add(voyageur(170, 790, 1.3, expr="content", bras="salut"))
    S.add(villageois(1, 620, 790, 1.15, expr="content", bras="porte", objet=g([pomme_terre(-20, -70, 0.8), pomme_terre(20, -64, 0.8), pomme_terre(0, -86, 0.8)])))
    S.add(bulle(420, 150, 520, 110, "Avec des pommes de terre,\nce serait encore meilleur !", 30, pointe=(200, 460)))
    return S


def p08():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(400, 760, 1.0, "#d8f5a2"))
    S.add(villageois(2, 140, 790, 1.05, expr="rire", bras="porte", objet=chou(0, -80, 0.6)))
    S.add(villageois(3, 620, 790, 0.95, expr="rire", bras="porte", objet=g([oignon(-16, -64, 0.6), oignon(20, -60, 0.6)])))
    S.add(villageois(4, 740, 790, 1.0, expr="content", bras="porte", objet=pain(0, -60, 0.6)))
    return S


def p09():
    S = Scene()
    place_village(S)
    S.add(feu_marmite(400, 760, 1.1, "#ffd43b"))
    for k, x in enumerate((90, 220, 580, 710)):
        S.add(villageois(k, x, 790, 0.95, expr="miam", bras="joues"))
    S.add(texte(400, 150, "Mmm ! Quelle bonne odeur !", 48, "#e8590c", contour="#fff"))
    return S


def p10():
    S = Scene()
    place_village(S)
    S.add(table(400, 790, 560, 120, nappe="#ffc9c9"))
    for k in range(5):
        S.add(bol(200 + k * 100, 650, 0.6, couleur=["#4dabf7", "#fa5252", "#51cf66", "#fcc419", "#cc5de8"][k], contenu="#e9ecef"))
    S.add(villageois(3, 110, 790, 0.95, expr="rire", bras="porte", objet=g([rect(-30, -80, 60, 12, "#adb5bd", rx=4)])))
    S.add(villageois(2, 690, 790, 1.0, expr="content", bras="porte", objet=bol(0, -50, 0.6, contenu="#e9ecef")))
    return S


def p11():
    S = Scene()
    place_village(S)
    S.add(voyageur(400, 790, 1.2, expr="chante", bras="ouverts"))
    S.add(table(400, 790, 620, 120, nappe="#ffc9c9"))
    for k in range(5):
        S.add(bol(180 + k * 110, 650, 0.6, couleur=["#4dabf7", "#fa5252", "#51cf66", "#fcc419", "#cc5de8"][k], contenu="#ffd43b"))
    for k, x in enumerate((70, 190, 610, 730)):
        S.add(villageois(k, x, 800, 0.85, expr="chante" if k % 2 else "miam", bras="haut" if k % 2 else "bouche"))
    S.add(notes(250, 330, 0.9, "#fff"), notes(520, 310, 0.9, "#fff"))
    S.add(texte(400, 170, "À table !", 64, "#fff", contour="#e8590c"))
    return S


def p12():
    S = Scene()
    place_village(S)
    S.add(voyageur(400, 790, 1.4, expr="malin", bras="donne", objet=place(caillou_rond(0, 0, 0.5), 84, -92)))
    S.add(villageois(0, 150, 790, 1.0, expr="bouche_bee", bras="joues"), villageois(1, 650, 790, 1.1, expr="rire", bras="joues"))
    S.add(bulle(400, 150, 480, 110, "Tout ça avec\nun caillou ?!", 36, pointe=(180, 480)))
    return S


def p13():
    S = Scene()
    place_village(S, soir=False, neige=False)
    S.add(soleil(690, 90, 40))
    S.add(voyageur(560, 790, 1.3, expr="content", bras="salut", flip=True))
    S.add(villageois(0, 180, 790, 1.0, expr="rire", bras="donne", objet=place(caillou_rond(0, 0, 0.5), 84, -92)), villageois(4, 320, 790, 1.0, expr="rire", bras="salut"))
    S.add(bulle(420, 150, 520, 110, "Gardez le caillou : vous\nconnaissez la recette !", 30, pointe=(560, 460)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("caillou-seul.svg", vignette),
    ("01-le-voyageur.svg", p01), ("02-nous-n-avons-rien.svg", p02), ("03-la-marmite.svg", p03), ("04-le-caillou.svg", p04),
    ("05-la-petite-fille.svg", p05), ("06-la-carotte.svg", p06), ("07-les-pommes-de-terre.svg", p07), ("08-chacun-apporte.svg", p08),
    ("09-la-bonne-odeur.svg", p09), ("10-les-bols.svg", p10), ("11-a-table.svg", p11), ("12-un-caillou.svg", p12),
    ("13-la-recette.svg", p13),
]
