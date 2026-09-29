"""Hansel et Gretel — le courage et la ruse de deux enfants."""
from contes import *

ID = "hansel-gretel"
HANSEL = dict(coiffure="courts", cheveux="blond", peau="claire", habit="#40c057", robe=False, jambes="#8d5524", chaussures="#5c3a1e")
GRETEL = dict(coiffure="tresses", cheveux="blond", peau="claire", habit="#e64980", chaussures="#862e9c")
PAPA = dict(coiffure="courts", cheveux="brun", barbe="#4a2c17", peau="rosee", habit="#c92a2a", robe=False, jambes="#5c3a1e")
SORCIERE = dict(peau="#d8f5a2", cheveux="gris", habit="#343a40", motif_robe="#9775fa", acc=("lunettes",))


def hansel(x, y, s=1.0, **k):
    return personne(x, y, s, **{**HANSEL, **k})


def gretel(x, y, s=1.0, **k):
    return personne(x, y, s, **{**GRETEL, **k})


def papa(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PAPA, **k})


def la_sorciere(x, y, s=1.0, **k):
    return sorciere(x, y, s, chapeau="#343a40", **{**SORCIERE, **k})


def oiseau_blanc(x, y, s=0.6, **k):
    k.setdefault("ailes", "haut")
    return oiseau(x, y, s, "#f8f9fa", "#ffffff", **k)


def bois(S, soir=False, graine=3):
    if soir:
        foret(S, "#5f3dc4", "#ffa8a8", graine=graine)
    else:
        foret(S, graine=graine)


def devant_maison(S):
    ciel(S, "#a5d8ff", "#fff0f6")
    for k, xx in enumerate((40, 760)):
        S.add(gros_arbre_sombre(xx, 640, 0.9))
    sol(S, 600, "#69db7c")
    S.add(maison_bonbons(400, 640, 1.0))


def dans_maison(S):
    interieur(S, "#ffe8cc", "#c9772b", 580, papier="#ffc9d6")
    S.add(fenetre(80, 100, 150, 140, dehors="#2f9e44"))


def couverture():
    S = Scene()
    devant_maison(S)
    S.add(hansel(170, 790, 1.2, expr="bouche_bee", regard=(1, -1)), gretel(640, 790, 1.2, expr="rire", bras="joues", regard=(-1, -1)))
    S.add(oiseau_blanc(700, 380, 0.5))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(maison_bonbons(200, 260, 0.6))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    for xx in (560, 680, 790):
        S.add(sapin(xx, 610, 1.3))
    sol(S, 600, "#94d82d")
    S.add(maison(200, 610, 0.9, mur="#e9d8c4", toit="#a0522d", porte="#6d4424"))
    S.add(papa(420, 790, 1.3, expr="content", bras="tient", objet=hache(68, -146, 0.8, rot=10)))
    S.add(hansel(590, 790, 1.0, expr="rire", bras="salut"), gretel(710, 790, 1.0, expr="rire", bras="haut"))
    return S


def p02():
    S = Scene()
    bois(S)
    S.add(miettes(700, 800, 450, 700, 7))
    S.add(hansel(300, 780, 1.3, expr="malin", bras="donne"), gretel(530, 780, 1.2, expr="sourire", bras="porte", objet=panier(0, -44, 0.7, contenu="")))
    S.add(bulle(420, 150, 460, 100, "Je sème des miettes pour\nretrouver le chemin !", 30, pointe=(310, 460)))
    return S


def p03():
    S = Scene()
    bois(S, graine=7)
    for k, xx in enumerate((110, 700)):
        S.add(buisson(xx, 720, 1.3, baies="#e03131"))
    S.add(hansel(300, 780, 1.2, expr="miam", bras="bouche"), gretel(510, 780, 1.2, expr="rire", bras="donne", objet=place(g([cercle(0, 0, 9, "#e03131"), cercle(10, 6, 8, "#e03131")]), 86, -92)))
    return S


def p04():
    S = Scene()
    bois(S, soir=True, graine=11)
    S.add(oiseau(120, 780, 0.5, "#868e96", expr="miam"), oiseau(640, 780, 0.5, "#fd7e14", expr="miam", flip=True))
    S.add(hansel(290, 780, 1.25, expr="inquiet", bras="tete"), gretel(480, 780, 1.2, expr="pleure", larmes=True))
    S.add(texte(400, 150, "Où sont les miettes ?", 48, "#fff", contour="#5f3dc4"))
    return S


def p05():
    S = Scene()
    bois(S, soir=True, graine=13)
    S.add(oiseau_blanc(560, 420, 0.8, expr="chante"), notes(640, 360, 0.8, "#fff"))
    S.add(gretel(250, 780, 1.25, expr="rire", bras="montre", regard=(1, -1)), hansel(430, 790, 1.15, expr="surpris", regard=(1, -1)))
    S.add(bulle(260, 160, 320, 90, "Suivons-le !", 40, pointe=(260, 440)))
    return S


def p06():
    S = Scene()
    devant_maison(S)
    S.add(hansel(120, 790, 1.1, expr="bouche_bee", bras="haut"), gretel(680, 790, 1.1, expr="bouche_bee", bras="joues"))
    S.add(oiseau_blanc(620, 330, 0.5), etincelles(400, 380, 1.4, "#fff", graine=3))
    return S


def p07():
    S = Scene()
    devant_maison(S)
    S.add(hansel(150, 790, 1.3, expr="miam", bras="bouche"), gretel(660, 790, 1.3, expr="miam", bras="donne2"))
    S.add(texte(400, 130, "Crounch ! Miam !", 64, "#e64980", contour="#fff"))
    return S


def p08():
    S = Scene()
    devant_maison(S)
    S.add(rect(360, 530, 80, 110, "#343a40"))
    S.add(la_sorciere(400, 800, 1.3, expr="malin", bras="ouverts"))
    S.add(hansel(140, 790, 1.1, expr="surpris"), gretel(660, 790, 1.1, expr="inquiet"))
    S.add(bulle(420, 150, 380, 90, "Entrez, mes petits !", 34, pointe=(420, 460)))
    return S


def p09():
    S = Scene()
    dans_maison(S)
    S.add(cage_bois(560, 780, 1.2))
    S.add(hansel(560, 760, 1.0, expr="triste", bras="croises"))
    S.add(cage_bois(560, 780, 1.2, ouverte=True))
    S.add(la_sorciere(210, 800, 1.35, expr="malin", bras="montre", regard=(1, 0)))
    S.add(bulle(360, 120, 420, 100, "Quand tu seras bien gras…\nMiam !", 32, pointe=(250, 420)))
    return S


def p10():
    S = Scene()
    dans_maison(S)
    S.add(cage_bois(530, 780, 1.2))
    S.add(hansel(530, 760, 1.0, expr="malin", bras="donne2", flip=True, objet=place(g([rect(-40, -6, 80, 12, "#f8f9fa", rx=6), cercle(-40, -8, 10, "#f8f9fa"), cercle(-40, 6, 10, "#f8f9fa"), cercle(40, -8, 10, "#f8f9fa"), cercle(40, 6, 10, "#f8f9fa")]), 110, -96)))
    S.add(cage_bois(530, 780, 1.2, ouverte=True))
    S.add(la_sorciere(220, 800, 1.35, expr="neutre", bras="donne", regard=(1, 0)))
    S.add(bulle(360, 110, 460, 100, "Toujours aussi maigre !", 34, pointe=(240, 420)))
    return S


def p11():
    S = Scene()
    dans_maison(S)
    S.add(four_pain(560, 660, 1.1, feu=False))
    S.add(la_sorciere(240, 800, 1.3, expr="fache", bras="montre", regard=(1, 0)))
    S.add(gretel(420, 800, 1.1, expr="malin", bras="pense", regard=(-1, 0)))
    S.add(bulle(260, 110, 420, 100, "Gretel, entre dans\nle four !", 34, pointe=(250, 420)))
    return S


def p12():
    S = Scene()
    dans_maison(S)
    S.add(four_pain(500, 680, 1.2, feu=False, ouvert=False))
    S.add(gretel(230, 800, 1.3, expr="fier", bras="hanches"))
    S.add(texte(500, 200, "CLAC !", 90, "#c92a2a", contour="#fff", rot=-6))
    S.add(bulle(560, 420, 220, 70, "Au secours !", 28, pointe=(540, 520)))
    return S


def p13():
    S = Scene()
    dans_maison(S)
    S.add(cage_bois(650, 780, 1.0, ouverte=True))
    S.add(tresor(390, 790, 1.1))
    S.add(hansel(190, 790, 1.2, expr="rire", bras="haut"), gretel(600, 790, 1.2, expr="bouche_bee", bras="joues"))
    return S


def p14():
    S = Scene()
    bois(S, graine=17)
    S.add(oiseau_blanc(650, 380, 0.6, expr="chante"))
    S.add(hansel(260, 780, 1.2, expr="content", bras="porte", objet=tresor(0, -40, 0.35, ouvert=False)),
          gretel(470, 780, 1.2, expr="content", bras="montre", regard=(1, -1)))
    return S


def p15():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    for xx in (620, 760):
        S.add(sapin(xx, 610, 1.3))
    sol(S, 600, "#94d82d")
    S.add(maison(170, 610, 0.9, mur="#e9d8c4", toit="#a0522d", porte="#6d4424"))
    S.add(papa(420, 790, 1.3, expr="rire", bras="ouverts"))
    S.add(hansel(300, 790, 1.0, expr="rire", bras="haut"), gretel(560, 790, 1.0, expr="rire", bras="haut"))
    S.add(coeur(420, 330, 1.8), oiseau_blanc(680, 360, 0.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("maison-seule.svg", vignette),
    ("01-la-foret.svg", p01), ("02-les-miettes.svg", p02), ("03-les-fraises.svg", p03), ("04-perdus.svg", p04),
    ("05-l-oiseau-blanc.svg", p05), ("06-la-maison.svg", p06), ("07-crounch.svg", p07), ("08-la-sorciere.svg", p08),
    ("09-la-cage.svg", p09), ("10-l-os.svg", p10), ("11-le-four.svg", p11), ("12-clac.svg", p12),
    ("13-le-tresor.svg", p13), ("14-le-retour.svg", p14), ("15-papa.svg", p15),
]
