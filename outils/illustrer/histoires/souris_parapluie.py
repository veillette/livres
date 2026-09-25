"""Le parapluie de Souris — la générosité."""
from base import *
from objets import *

ID = "souris-parapluie"
SOURIS = dict(acc=("noeud",), couleur_acc="#fab005", habit="#ffd43b", couleur_motif="#fff3bf")


def pre(S, graine=1, pluie_=True):
    ciel(S, "#91a7c7", "#dbe4f0")
    collines(S, 600, "#a9d6a0", graine=graine)
    sol(S, 600, "#8ccf7e", couleur2="#74c069", y2=700)
    if pluie_:
        pluie(S, 70, graine, (0, 0, 800, 760), "#4dabf7")


def souris_parapluie(x, y, s=1.0, expr="sourire", bras="tient", taille=0.9, **kw):
    """Souris tenant son parapluie jaune au-dessus de sa tête."""
    mg, md = mains(x, y, s, bras, kw.get("flip", False))
    k = s * taille
    return g([perso("souris", x, y, s, expr=expr, bras=bras, **SOURIS, **kw),
              parapluie(md[0] - 22 * k, md[1] - 138 * k, k, rot=-10)])


def couverture():
    S = Scene()
    pre(S, 3)
    S.add(flaque(250, 745, 1.2), flaque(580, 760, 1.0))
    S.add(perso("herisson", 250, 750, 1.3, expr="rire", bras="bas", regard=(1, 0)))
    S.add(perso("lapin", 560, 750, 1.3, expr="content", bras="bas", regard=(-1, 0)))
    S.add(souris_parapluie(390, 770, 1.45, expr="rire", taille=1.15))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(souris_parapluie(190, 265, 0.62, expr="content"))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(arbre(130, 620, 0.9, "#69b35b", "#5aa34c"))
    S.add(flaque(560, 740))
    S.add(souris_parapluie(400, 740, 1.5, expr="content"))
    S.add(texte(230, 130, "Plic ! Ploc !", 56, "#1c7ed6", contour="#fff"))
    return S


def p02():
    S = Scene()
    pre(S, 2)
    S.add(buisson(600, 700, 1.4, "#5aa34c", "#69b35b"))
    S.add(perso("herisson", 610, 740, 1.1, expr="triste", bras="bas", regard=(-1, 0)))
    S.add(g([trait(610, 740 - 150 * 1.1 - 40, 600, 740 - 150 * 1.1 - 70, "#2f9e44", 4), ellipse(610, 740 - 150 * 1.1 - 60, 40, 14, "#51cf66", rot=-10)]))
    S.add(souris_parapluie(260, 750, 1.3, expr="sourire", bras="tient", regard=(1, 0)))
    S.add(bulle(330, 150, 400, 90, "Viens, il y a de la place !", 32, pointe=(270, 300)))
    return S


def p03():
    S = Scene()
    pre(S, 4)
    S.add(perso("lapin", 640, 760, 1.25, expr="triste", bras="bas", regard=(-1, 0)))
    for k in range(4):
        S.add(goutte(610 + k * 20, 470 + (k % 2) * 30, 1.0, "#4dabf7"))
    S.add(perso("herisson", 360, 760, 1.05, expr="sourire", regard=(1, 0)))
    S.add(souris_parapluie(250, 760, 1.2, expr="sourire", bras="tient", regard=(1, 0)))
    S.add(bulle(520, 150, 360, 90, "On se serre un peu !", 34, pointe=(360, 260)))
    return S


def p04():
    S = Scene()
    pre(S, 5)
    S.add(perso("ours", 610, 760, 1.7, expr="joie", bras="course", regard=(-1, 0)))
    S.add(perso("herisson", 280, 760, 0.95, expr="surpris", regard=(1, 0)))
    S.add(perso("lapin", 180, 760, 1.05, expr="surpris", regard=(1, 0)))
    S.add(souris_parapluie(360, 760, 1.1, expr="bouche_bee", bras="tient", regard=(1, 0)))
    S.add(bulle(600, 140, 380, 90, "Et moi, et moi ?", 40, pointe=(600, 300)))
    return S


def p05():
    S = Scene()
    pre(S, 6)
    S.add(perso("ours", 400, 760, 1.8, expr="rire", bras="ouverts"))
    S.add(perso("lapin", 180, 760, 1.05, expr="rire", bras="haut", regard=(1, 0), rot=-10))
    S.add(perso("herisson", 620, 760, 0.95, expr="rire", bras="haut", regard=(-1, 0), rot=10))
    S.add(parapluie(400, 290, 0.9))
    S.add(perso("souris", 400, 460, 0.8, expr="rire", bras="haut", **SOURIS))
    for x, y in [(160, 460), (660, 520), (280, 610), (520, 600)]:
        S.add(goutte(x, y, 1.4, "#4dabf7"))
    return S


def p06():
    S = Scene()
    pre(S, 7, pluie_=False)
    pluie(S, 60, 7, (0, 0, 800, 200), "#4dabf7")
    S.add(grande_feuille(400, 690, 1.35))
    S.add(perso("ours", 400, 760, 1.6, expr="content", bras="haut"))
    S.add(perso("lapin", 190, 760, 1.05, expr="content", regard=(1, 0)))
    S.add(perso("herisson", 620, 760, 0.95, expr="content", regard=(-1, 0)))
    S.add(souris_parapluie(290, 770, 0.8, expr="rire", bras="tient", regard=(1, 0)))
    return S


def p07():
    S = Scene()
    pre(S, 8)
    S.add(flaque(250, 740, 1.4, eclabousse=True), flaque(600, 755, 1.2, eclabousse=True))
    S.add(perso("grenouille", 250, 700, 1.2, expr="rire", bras="haut", pieds_haut=True))
    S.add(perso("lapin", 590, 700, 1.0, expr="rire", bras="haut", pieds_haut=True))
    S.add(texte(400, 200, "Splash !", 90, "#1c7ed6", contour="#fff", rot=-6))
    return S


def p08():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(arc_en_ciel(400, 600, 330, 24))
    collines(S, 600, "#b2f2bb", graine=9)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=700)
    S.add(soleil(680, 140, 50))
    S.add(perso("ours", 610, 760, 1.5, expr="content", bras="bas", regard=(-1, 0)))
    S.add(perso("grenouille", 150, 760, 0.9, expr="rire", bras="salut", regard=(1, 0)))
    S.add(perso("lapin", 470, 760, 1.05, expr="content", regard=(-1, 0)))
    S.add(perso("herisson", 280, 760, 0.95, expr="sourire", regard=(1, 0)))
    S.add(perso("souris", 380, 760, 0.95, expr="timide", bras="bas", **SOURIS))
    S.add(coeur(380, 520, 1.3))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("souris-seule.svg", vignette),
    ("01-plic-ploc.svg", p01), ("02-herisson.svg", p02), ("03-lapin.svg", p03),
    ("04-ours.svg", p04), ("05-trop-serres.svg", p05), ("06-grande-feuille.svg", p06),
    ("07-flaques.svg", p07), ("08-arc-en-ciel.svg", p08),
]
