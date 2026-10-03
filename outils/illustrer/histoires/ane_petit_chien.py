"""L'Âne et le Petit Chien — ne forçons point notre talent."""
from fables import *
from contes import carotte, chaise

ID = "ane-petit-chien"

ORANGE = "#f08c00"
MAITRE = dict(coiffure="chauve_cote", cheveux="gris", peau="rosee", habit="#2f9e44", robe=False, jambes="#5c3a1e",
              chaussures="#343a40")
MAITRESSE = dict(coiffure="chignon", cheveux="roux", peau="claire", habit="#e64980")


def maitre(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MAITRE, **k})


def maitresse(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MAITRESSE, **k})


def bijou(x, y, s=1.0, **k):
    """Le petit chien, avec son nœud rouge."""
    k.setdefault("acc", ("noeud",))
    k.setdefault("couleur", "#f1dcc3")
    return perso("chien", x, y, s, **k)


def ane(x, y, s=1.0, **k):
    return perso("ane", x, y, s, **k)


def biscuit(x, y, s=1.0):
    return place([cercle(0, 0, 16, "#e8a15c"), cercle(-5, -4, 2.5, "#a0522d"), cercle(5, 3, 2.5, "#a0522d"), cercle(3, -7, 2, "#a0522d")], x, y, s)


def salon(S):
    interieur(S, "#fff4e6", "#e8c39e", 580, papier="#ffd8a8")
    S.add(fenetre(80, 140, 170, 160, rideaux="#fa5252"))
    S.add(cadre_mur(560, 150, 120, 100))


def ferme(S, graine=71):
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 580, "#8ce99a")


def etable(S, soir=False):
    S.add(rect(0, 0, 800, 800, "#7c4a1e"))
    for k in range(0, 800, 80):
        S.add(rect(k, 0, 74, 600, "#a0693a"))
    S.add(rect(0, 600, 800, 200, "#f6c453"))
    for k in range(20):
        S.add(trait(20 + k * 40, 620 + (k % 3) * 40, 50 + k * 40, 600 + (k % 3) * 40, "#e0a93a", 4))
    S.add(rect(520, 120, 180, 150, "#ffc078" if soir else "#a5d8ff", stroke="#5c3a1e", stroke_width=12))
    S.add(meule_foin(140, 620, 0.7))


def couverture():
    S = Scene()
    salon(S)
    S.add(maitre(300, 760, 1.3, expr="oups", bras="ouverts", rot=-10))
    S.add(ane(470, 760, 1.4, expr="rire", bras="ouverts", regard=(-1, 0), rot=-14))
    S.add(bijou(680, 760, 0.8, expr="bouche_bee", bras="joues"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ane(140, 262, 0.75, expr="sourire"))
    S.add(bijou(290, 262, 0.55, expr="content"))
    return S


def p01():
    S = Scene()
    ferme(S)
    S.add(maison(600, 600, 1.0))
    S.add(barriere(200, 680, 1.0, largeur=380))
    S.add(ane(260, 760, 1.4, expr="sourire", bras="bas"))
    S.add(bijou(480, 760, 0.85, expr="content", bras="haut"))
    return S


def p02():
    S = Scene()
    salon(S)
    S.add(maitre(400, 760, 1.5, expr="content", bras="porte", objet=bijou(0, 12, 0.5, expr="rire", bras="haut")))
    S.add(coeur(560, 330, 1.0), coeur(240, 360, 0.8))
    return S


def p03():
    S = Scene()
    salon(S)
    S.add(maitresse(240, 760, 1.4, expr="rire", bras="donne"))
    S.add(biscuit(358, 630, 1.0))
    S.add(bijou(500, 760, 1.0, expr="joie", bras="haut", pieds_haut=True))
    S.add(texte(560, 320, "Qu'il est mignon !", 44, ORANGE, contour="#fff"))
    return S


def p04():
    S = Scene()
    ferme(S, graine=72)
    S.add(moulin(660, 600, 0.75))
    S.add(chemin("M 0 720 Q 400 660 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(ane_profil(320, 760, 1.4, expr="triste", ploie=True))
    S.add(bat(320, 760 - (110 - 16) * 1.4, 1.4, nb=3))
    S.add(texte(320, 300, "Ouf…", 50, ORANGE, contour="#fff"))
    return S


def p05():
    S = Scene()
    etable(S)
    S.add(ane(260, 770, 1.4, expr="inquiet", bras="pense", regard=(1, -1)))
    S.add(pensee(560, 300, 180, g([maitre(540, 410, 0.85, expr="content", bras="porte", objet=bijou(0, 12, 0.5, expr="rire")),
                                   coeur(650, 220, 0.8)]), depuis=(330, 480)))
    return S


def p06():
    S = Scene()
    etable(S)
    S.add(ane(400, 770, 1.5, expr="fier", bras="hanches"))
    S.add(bulle(400, 140, 600, 120, "Moi aussi, je vais\nfaire le petit chien !", 38, pointe=(400, 330)))
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(porte(170, 580, 160, 320, ouverte=True))
    S.add(ane(200, 760, 1.2, expr="joie", bras="ouverts", regard=(1, 0)))
    S.add(maitre(560, 760, 1.4, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bijou(700, 760, 0.7, expr="surpris"))
    return S


def p08():
    S = Scene()
    salon(S)
    S.add(maitre(330, 760, 1.35, expr="oups", bras="ouverts", rot=-12))
    S.add(ane(480, 760, 1.4, expr="rire", bras="ouverts", regard=(-1, 0), rot=-14))
    S.add(texte(560, 220, "Hi-han !", 58, ORANGE, contour="#fff"))
    return S


def p09():
    S = Scene()
    salon(S)
    S.add(table(620, 760, 220, 120))
    S.add(chaise(170, 770, 0.8, cassee=True))
    S.add(pot_fleurs(620, 760, 0.6, etat="casse"))
    S.add(maitre(330, 760, 1.2, expr="oups", bras="haut", rot=-80))
    S.add(ane(480, 760, 1.2, expr="oups", bras="joues"))
    S.add(texte(400, 230, "PATATRAS !", 62, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    salon(S)
    S.add(maitre(250, 760, 1.35, expr="furieux", bras="montre", regard=(1, 0)))
    S.add(maitresse(420, 760, 1.25, expr="fache", bras="hanches", regard=(1, 0)))
    S.add(ane(640, 760, 1.15, expr="pleure", bras="bas", regard=(-1, 0)))
    S.add(bulle(330, 150, 380, 100, "À l'étable !", 40, pointe=(270, 330)))
    return S


def p11():
    S = Scene()
    etable(S, soir=True)
    S.add(ane(400, 770, 1.5, expr="pleure", bras="calin", larmes=True))
    S.add(texte(330, 110, "Personne ne m'aime…", 44, ORANGE, contour="#fff"))
    return S


def p12():
    S = Scene()
    etable(S, soir=True)
    S.add(ane(300, 770, 1.35, expr="triste", bras="bas", regard=(1, 0)))
    S.add(bijou(560, 770, 0.85, expr="sourire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(520, 170, 520, 140, "Tu sais, moi, je ne sais\npas porter un seul sac !", 34, pointe=(560, 520)))
    return S


def p13():
    S = Scene()
    etable(S)
    S.add(ane(260, 770, 1.35, expr="timide", bras="bas", regard=(1, 0)))
    S.add(maitre(540, 770, 1.3, expr="content", bras="donne", regard=(-1, 0)))
    S.add(carotte(430, 650, 1.0, rot=-80))
    S.add(bulle(520, 150, 540, 140, "Sans toi, mon brave âne,\npas de farine, pas de pain !", 32, pointe=(540, 420)))
    return S


def p14():
    S = Scene()
    ferme(S, graine=73)
    S.add(moulin(660, 600, 0.75))
    S.add(chemin("M 0 720 Q 400 660 800 700 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(ane_profil(300, 770, 1.3, expr="fier"))
    S.add(bat(300, 770 - 110 * 1.3, 1.3, nb=3))
    S.add(bijou(560, 770, 0.8, expr="rire", bras="haut", pieds_haut=True))
    S.add(notes(500, 330, 1.0, ORANGE))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ane-et-chien.svg", vignette),
    ("01-a-la-ferme.svg", p01), ("02-dans-les-bras.svg", p02), ("03-un-biscuit.svg", p03),
    ("04-les-sacs.svg", p04), ("05-pourquoi-pas-moi.svg", p05), ("06-moi-aussi.svg", p06),
    ("07-dans-la-maison.svg", p07), ("08-hi-han.svg", p08), ("09-patatras.svg", p09),
    ("10-a-l-etable.svg", p10), ("11-personne-ne-m-aime.svg", p11), ("12-bijou.svg", p12),
    ("13-une-carotte.svg", p13), ("14-chacun-son-talent.svg", p14),
]
