"""Les habits neufs de l'empereur — oser dire ce qu'on voit."""
from contes import *

ID = "habits-empereur"
PEAU = "rosee"
EMPEREUR = dict(coiffure="chauve_cote", cheveux="brun", barbe="#4a2c17", peau=PEAU, habit="#e64980", robe=False, jambes="#fcc419",
                cape="#7048e8", ceinture="#f59f00", acc=("grande_couronne",))
FILOUS = [dict(coiffure="herisses", cheveux="noir", peau="doree", habit="#495057", robe=False, jambes="#343a40", acc=("lunettes",)),
          dict(coiffure="courts", cheveux="roux", peau="claire", habit="#868e96", robe=False, jambes="#343a40")]
MINISTRE = dict(coiffure="chauve_cote", cheveux="gris", peau="claire", habit="#1864ab", robe=False, jambes="#343a40", acc=("lunettes", "col"))
GARCON = dict(coiffure="herisses", cheveux="chatain", peau="brune", habit="#fcc419", robe=False, jambes="#1864ab")
FOULE = [dict(coiffure="chignon", cheveux="roux", peau="claire", habit="#51cf66"),
         dict(coiffure="courts", cheveux="noir", peau="foncee", habit="#fa5252", robe=False, jambes="#495057"),
         dict(coiffure="tresses", cheveux="blond", peau="claire", habit="#cc5de8"),
         dict(coiffure="chauve_cote", cheveux="blanc", barbe="#e9ecef", peau="doree", habit="#20c997", robe=False, jambes="#495057")]


def empereur(x, y, s=1.2, **k):
    return personne(x, y, s, **{**EMPEREUR, **k})


def en_calecon(x, y, s=1.2, flip=False, **k):
    p = PEAUX[PEAU]
    d = dict(EMPEREUR)
    d.update(habit=p, jambes=p, chaussures="#c92a2a", cape=None, ceinture=p)
    d.update(k)
    corps = personne(0, 0, 1.0, **d)
    calecon = [chemin("M -34 -70 L 34 -70 L 36 -34 L 6 -30 L 0 -40 L -6 -30 L -36 -34 Z", "#fff", stroke="#dee2e6", sw=2),
               coeur(-18, -52, 0.35), coeur(16, -48, 0.35), coeur(0, -62, 0.3)]
    nombril = cercle(0, -80, 2.5, assombrir(p, 0.8))
    return place([corps, nombril] + calecon, x, y, s, flip=flip)


def filou(i, x, y, s=1.1, **k):
    return personne(x, y, s, **{**FILOUS[i], **k})


def palais(S):
    interieur(S, "#fff3bf", "#e9d8c4", 580, papier="#ffec99")
    for x in (60, 740):
        S.add(rect(x - 30, 0, 60, 580, "#fff"), rect(x - 40, 40, 80, 20, "#f1f3f5"))
    S.add(chemin("M 250 580 L 550 580 L 620 800 L 180 800 Z", "#c92a2a"))


def rue(S):
    ciel(S, "#a5d8ff", "#fff9db")
    ville(S, 560)
    S.add(rect(0, 560, 800, 240, "#e9ecef"))
    for k in range(8):
        S.add(poly([(k * 110, 0), (k * 110 + 50, 0), (k * 110 + 25, 40)], ["#fa5252", "#fcc419", "#4dabf7", "#51cf66"][k % 4]))


def ciseaux(x, y, s=1.0, rot=0):
    m = [trait(0, 0, 40, -30, "#adb5bd", 6), trait(0, -30, 40, 0, "#adb5bd", 6),
         cercle(-6, 4, 9, "none", stroke="#fa5252", stroke_width=5), cercle(-6, -34, 9, "none", stroke="#fa5252", stroke_width=5)]
    return place(m, x, y, s, rot=rot)


def couverture():
    S = Scene()
    rue(S)
    S.add(en_calecon(400, 790, 1.45, expr="fier", bras="salut"))
    for k, x in enumerate((90, 700)):
        S.add(personne(x, 790, 1.0, expr="bouche_bee", bras="joues", **FOULE[k]))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(couronne_objet(200, 220, 1.6, brille=True))
    return S


def p01():
    S = Scene()
    palais(S)
    S.add(miroir(620, 790, 0.9, reflet=place(empereur(0, 0, 0.6, expr="fier"), 0, -120)))
    S.add(empereur(330, 790, 1.35, expr="fier", bras="hanches"))
    for k, c in enumerate(("#4dabf7", "#51cf66", "#fcc419")):
        S.add(place(g([rect(-4, -120, 8, 20, "#adb5bd"), chemin("M -50 -100 L 50 -100 L 60 0 L -60 0 Z", c)]), 120 + k * 60, 520, 0.6))
    return S


def p02():
    S = Scene()
    palais(S)
    S.add(empereur(560, 790, 1.3, expr="surpris"))
    S.add(filou(0, 170, 790, expr="malin", bras="ouverts"), filou(1, 320, 790, expr="malin", bras="salut"))
    S.add(bulle(360, 150, 560, 110, "Notre étoffe magique est\ninvisible pour les gens bêtes !", 30, pointe=(210, 480)))
    return S


def p03():
    S = Scene()
    palais(S)
    S.add(empereur(560, 790, 1.3, expr="rire", bras="donne", objet=sac(84, -60, 0.5, OR, ecrit="or")))
    S.add(filou(0, 180, 790, expr="rire", bras="ouverts"), filou(1, 330, 790, expr="rire", bras="haut"))
    S.add(texte(400, 200, "Formidable !", 64, "#7048e8", contour="#fff"))
    return S


def p04():
    S = Scene()
    interieur(S, "#e9ecef", "#adb5bd", 580)
    S.add(fenetre(80, 100, 150, 130, nuit_=True, dehors="#1c2a52"))
    S.add(metier_tisser(420, 790, 1.0))
    S.add(filou(0, 250, 790, 1.0, expr="malin", bras="large"), filou(1, 600, 790, 1.0, expr="rire", bras="porte", objet=sac(0, -40, 0.6, OR, ecrit="or")))
    return S


def p05():
    S = Scene()
    interieur(S, "#e9ecef", "#adb5bd", 580)
    S.add(metier_tisser(460, 790, 1.0))
    S.add(personne(200, 790, 1.3, expr="oups", bras="joues", **MINISTRE))
    S.add(filou(0, 660, 790, 1.0, expr="malin", bras="montre", flip=True))
    S.add(bulle(360, 130, 460, 100, "Je ne vois rien…\nSuis-je bête ?", 34, pointe=(220, 460)))
    return S


def p06():
    S = Scene()
    interieur(S, "#e9ecef", "#adb5bd", 580)
    S.add(metier_tisser(480, 790, 1.0))
    S.add(empereur(220, 790, 1.35, expr="oups", bras="ouverts"))
    S.add(filou(1, 680, 790, 1.0, expr="malin", bras="montre", flip=True))
    S.add(bulle(360, 130, 400, 100, "Euh… Splendide !\nMerveilleux !", 34, pointe=(240, 460)))
    return S


def p07():
    S = Scene()
    interieur(S, "#e9ecef", "#adb5bd", 580)
    S.add(table(400, 790, 440, 130, "#8d5524"))
    S.add(filou(0, 250, 790, 1.1, expr="concentre", bras="tient", objet=ciseaux(68, -146, 0.9)))
    S.add(filou(1, 560, 790, 1.1, expr="concentre", bras="donne2"))
    S.add(texte(400, 200, "Clic, clic !", 56, "#495057", contour="#fff"))
    return S


def p08():
    S = Scene()
    palais(S)
    S.add(miroir(620, 790, 0.9, reflet=place(en_calecon(0, 0, 0.6, expr="fier"), 0, -120)))
    S.add(en_calecon(330, 790, 1.35, expr="fier", bras="hanches"))
    S.add(filou(0, 120, 790, 0.9, expr="malin", bras="bouche"))
    S.add(bulle(360, 120, 460, 100, "Quelle belle cape !\nQuelle traîne !", 34, pointe=(150, 480)))
    return S


def p09():
    S = Scene()
    rue(S)
    S.add(en_calecon(400, 790, 1.3, expr="fier", bras="salut"))
    for k, x in enumerate((90, 210, 590, 710)):
        S.add(personne(x, 790, 0.95, expr="rire" if k % 2 else "timide", bras="joues" if k % 2 else "haut", **FOULE[k]))
    S.add(texte(400, 150, "Oh, que c'est beau !", 56, "#7048e8", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


def p10():
    S = Scene()
    rue(S)
    S.add(en_calecon(560, 790, 1.25, expr="surpris"))
    S.add(personne(190, 790, 1.0, expr="rire", bras="montre", **GARCON))
    S.add(bulle(330, 150, 540, 110, "Mais l'empereur n'a pas\nd'habits ! Il est en caleçon !", 30, pointe=(210, 540)))
    return S


def p11():
    S = Scene()
    rue(S)
    S.add(en_calecon(400, 790, 1.2, expr="timide", bras="bouche"))
    for k, x in enumerate((90, 210, 590, 710)):
        S.add(personne(x, 790, 0.95, expr="rire", bras="haut" if k % 2 else "joues", **FOULE[k]))
    S.add(texte(400, 150, "Ha ha ha ha !", 64, "#c92a2a", contour="#fff"))
    S.cachette(680, 70, "air")
    return S


def p12():
    S = Scene()
    rue(S)
    S.add(en_calecon(430, 790, 1.35, expr="rire", bras="haut"))
    S.add(personne(190, 790, 1.0, expr="rire", bras="haut", **GARCON))
    S.add(texte(400, 150, "Ha ! Ha ! Tu as raison !", 52, "#7048e8", contour="#fff"))
    return S


def p13():
    S = Scene()
    palais(S)
    S.add(empereur(470, 790, 1.3, expr="rire", bras="ouverts"))
    S.add(personne(260, 790, 1.0, expr="rire", bras="haut", acc=("couronne",), **GARCON))
    S.add(chevalier(90, 790, 0.9, expr="neutre"), chevalier(700, 790, 0.9, expr="neutre"))
    S.cachette(260, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("couronne-seule.svg", vignette),
    ("01-l-empereur.svg", p01), ("02-les-filous.svg", p02), ("03-formidable.svg", p03), ("04-le-metier-vide.svg", p04),
    ("05-le-ministre.svg", p05), ("06-splendide.svg", p06), ("07-clic-clic.svg", p07), ("08-le-miroir.svg", p08),
    ("09-le-defile.svg", p09), ("10-le-petit-garcon.svg", p10), ("11-tout-le-monde-rit.svg", p11),
    ("12-tu-as-raison.svg", p12), ("13-la-verite.svg", p13),
]
