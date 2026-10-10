"""L'école des petits dragons — chacun son talent.

Sur la montagne aux nuages se dresse l'école de magie des dragons. C'est la
rentrée pour Flammèche, une toute petite dragonne violette. Leçon de feu :
Braise fait fondre sa bougie d'un coup, Flammèche ne fait qu'une toute
petite flamme. Leçon de vol : elle tombe dans le foin. Leçon de magie : sa
pierre devient… une fleur. Le soir, elle est triste ; Madame Grimoire, la
maîtresse, lui dit d'attendre. À la fête des lanternes, les grands feux
brûlent les lanternes de papier, le souffle de Grêlon les gèle, Olive ne
fait que de la fumée : seule la petite flamme de Flammèche, toute douce, les
allume sans les abîmer.

Plans : couverture moyen · 1 large (l'école sur la montagne) · 2 moyen (la
classe) · 3 moyen (la leçon de feu) · 4 large (la leçon de vol) · 5 moyen (la
leçon de magie) · 6 gros plan (le soir, triste) · 7 large (la cour et ses
lanternes éteintes) · 8 moyen (raté, raté, raté) · 9 gros plan (pfff… la
lanterne s'allume) · 10 large (toutes les lanternes) · 11 large (la fête).
"""
from base import *
from base import _assombrir
from fantastique import chateau, etincelles, OR
from objets import bougie
from fables import meule_foin
from dragons import *

ID = "ecole-dragons"

FLAMMECHE = dict(couleur="#cc5de8", ventre="#f3d9fa", noeud="#fcc419")
GRIMOIRE = dict(couleur="#748ffc", ventre="#dbe4ff", chapeau="#5f3dc4", bande="#fcc419", lunettes="#495057")
BRAISE = dict(couleur="#fa5252", ventre="#ffe3e3")
OLIVE = dict(couleur="#82c91e", ventre="#e9fac8", echarpe="#ff922b")
GRELON = dict(couleur="#66d9e8", ventre="#e3fafc")
COULEURS_LANTERNES = ("#ff8787", "#ffd43b", "#69db7c", "#74c0fc", "#da77f2", "#ffa94d")


def flammeche_(x, y, s=0.9, **k):
    return dragon_habille(x, y, s, **{**FLAMMECHE, **k})


def grimoire(x, y, s=1.7, **k):
    return dragon_habille(x, y, s, **{**GRIMOIRE, **k})


def braise(x, y, s=1.3, **k):
    return dragon_habille(x, y, s, **{**BRAISE, **k})


def olive(x, y, s=1.15, **k):
    return dragon_habille(x, y, s, **{**OLIVE, **k})


def grelon(x, y, s=1.1, **k):
    return dragon_habille(x, y, s, **{**GRELON, **k})


def couleurs(d):
    """Seulement les couleurs d'un dragon (pour dragon_vol et dragon_couche)."""
    return dict(couleur=d["couleur"], ventre=d["ventre"])


def bouche_de(x, y, s):
    return x, y + BOUCHE[1] * s


# --- Objets et décors ----------------------------------------------------------

def bougie_fondue(x, y, s=1.0, couleur="#74c0fc"):
    """Bougie fondue d'un coup : une flaque de cire et une mèche ; (x, y) = base."""
    m = [chemin("M -50 0 Q -46 -20 -20 -22 Q -10 -40 0 -30 Q 12 -44 22 -22 Q 50 -20 50 0 Z", volume(couleur, 0.3, 0.8)),
         trait(0, -30, 4, -46, ENCRE, 3), cercle(6, -60, 8, "#adb5bd", opacity=0.6), cercle(12, -80, 11, "#adb5bd", opacity=0.4)]
    return place(m, x, y, s)


def tableau_noir(x, y, w=360, h=200, lignes=("Abracadragon !",)):
    m = [rect(x - 12, y - 12, w + 24, h + 24, "#8d5524", rx=6), rect(x, y, w, h, "#2b8a3e"),
         rect(x, y, w, h, "#000", opacity=0.25)]
    for k, l in enumerate(lignes):
        m.append(texte(x + w / 2, y + 60 + k * 50, l, 34, "#f8f9fa", poids=500))
    m.append(etoile5(x + 50, y + h - 50, 20, "#f8f9fa", opacity=0.8))
    m.append(chemin(f"M {x + w - 120} {y + h - 40} q 30 -50 60 0 q 30 -50 60 0", stroke="#f8f9fa", sw=3))
    m.append(rect(x + 30, y + h + 10, 60, 10, "#f8f9fa", rx=3))
    return g(m)


def ecole(x, y, s=1.0, nuit_=False):
    return chateau(x, y, s, mur="#e5dbff", mur2="#d0bfff", toit="#5f3dc4", drapeau="#fcc419", nuit_=nuit_)


def montagne_nuages(S, soir=False):
    if soir:
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#91a7ff", "#e7f5ff")
    S.add(chemin("M -40 800 L 160 420 Q 260 300 400 300 Q 540 300 640 420 L 840 800 Z", volume("#adb5bd", 0.2, 0.75)))
    S.add(chemin("M 160 420 Q 260 300 400 300 Q 540 300 640 420 Q 520 380 400 390 Q 280 380 160 420 Z", "#e9ecef"))
    S.add(ecole(400, 330, 0.62, nuit_=soir))
    for nx, ny, ns in ((120, 470, 1.4), (680, 500, 1.3), (300, 620, 1.1), (560, 650, 1.2)):
        S.add(nuage(nx, ny, ns, "#ffffff"))


def classe(S):
    piece(S, "chateau", 600)
    S.add(tableau_noir(240, 110, 360, 200))
    S.add(fenetre(640, 110, 120, 170, "#a5d8ff", cadre="#e5dbff"))


def cour(S, chateau_nuit=True):
    """La cour de l'école, la nuit : le château, les dalles, une guirlande de
    cordes tendues pour les lanternes."""
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 30, graine=5)
    S.add(lune(680, 90, 38))
    S.add(ecole(400, 560, 1.1, nuit_=chateau_nuit))
    sol(S, 560, "#868e96", bosse=0, couleur2="#495057", y2=800)
    S.add(pierres(0, 570, 800, 230, "#868e96", pas_=36, larg=80, opacite=0.3))


def corde(S, x0, x1, y, creux=40):
    S.add(chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y + creux * 2} {x1} {y}", stroke="#495057", sw=3))


def y_corde(x, x0, x1, y, creux=40):
    t = (x - x0) / (x1 - x0)
    return y + 2 * t * (1 - t) * creux * 2


def lanternes(S, x0=-20, x1=820, y=230, creux=40, nb=6, etat=lambda k: "eteinte"):
    corde(S, x0, x1, y, creux)
    for k in range(nb):
        x = x0 + (x1 - x0) * (k + 0.5) / nb
        e = etat(k)
        S.add(lanterne_papier(x, y_corde(x, x0, x1, y, creux), 0.7, COULEURS_LANTERNES[k % 6],
                              allumee=e == "allumee", brulee=e == "brulee", gelee=e == "gelee", S=S))


def poteau_lanterne(S, x, y_sol, y_lanterne, s=0.8, couleur="#ff8787", cote=-1, **k):
    """Poteau de bois avec un bras : la lanterne pend à hauteur de bouche ;
    (x, y_lanterne) = centre de la lanterne. Le poteau est du côté `cote`."""
    crochet = y_lanterne - 80 * s
    px = x - cote * 60 * s
    S.add(rect(px - 6, crochet - 20, 12, y_sol - crochet + 20, cylindre("#8d5524", 0.25, 0.7), rx=4))
    S.add(rect(min(px, x) - 4, crochet - 20, abs(px - x) + 8, 10, "#8d5524", rx=4))
    S.add(lanterne_papier(x, crochet - 10, s, couleur, S=S, **k))


# --- Pages -------------------------------------------------------------------------

def couverture():
    S = Scene()
    cour(S)
    lanternes(S, y=250, etat=lambda k: "allumee")
    S.add(grimoire(150, 790, 1.35, expr="content", bras="salut", regard=(1, 0)))
    S.add(flammeche_(400, 790, 1.2, expr="joie", bras="haut"))
    S.add(flammeche(400, 470, 0.9))
    S.add(braise(620, 790, 1.15, expr="rire", regard=(-1, 0)))
    S.lumiere(400, 440, 120, "#ffd43b", 0.7)
    S.cachette(730, 450, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(flammeche_(200, 262, 0.95, expr="content", bras="haut"))
    S.add(flammeche(200, 40, 0.5))
    return S


def p01():
    """Plan large : l'école sur la montagne aux nuages ; c'est la rentrée."""
    S = Scene()
    montagne_nuages(S)
    S.add(dragon_vol(160, 170, 0.32, **couleurs(BRAISE)), dragon_vol(620, 140, 0.28, flip=True, **couleurs(OLIVE)),
          dragon_vol(700, 250, 0.22, flip=True, **couleurs(GRELON)))
    S.add(flammeche_(300, 790, 1.0, expr="content", bras="salut", cartable="#fcc419"))
    S.cachette(80, 300, "air")
    S.dessus(texte(580, 760, "C'est la rentrée !", 40, "#5f3dc4", contour="#fff"))
    return S


def p02():
    """Plan moyen : la classe ; Madame Grimoire souhaite la bienvenue."""
    S = Scene()
    classe(S)
    S.add(grimoire(560, 790, 1.6, expr="content", bras="montre", regard=(-1, 0)))
    S.add(baguette_magique(640, 600, 1.0, rot=30))
    S.add(braise(120, 800, 1.05, expr="content", regard=(1, 0)))
    S.add(olive(250, 800, 0.95, expr="content", regard=(1, 0)))
    S.add(grelon(360, 800, 0.9, expr="sourire", regard=(1, 0)))
    S.add(flammeche_(450, 800, 0.7, expr="timide", regard=(1, -1)))
    S.cachette(300, 70, "air")
    S.dessus(bulle(270, 420, 470, 90, "Bienvenue, mes petits dragons !", 28, pointe=(480, 540)))
    return S


def p03():
    """Plan moyen : la leçon de feu. FFFOUUU ! — pfff…"""
    S = Scene()
    classe(S)
    S.add(table(400, 790, 640, 120, couleur="#a0693a"))
    S.add(braise(150, 680, 1.25, expr="souffle", bras="hanches"))
    bx, by = bouche_de(150, 680, 1.25)
    S.add(bougie_fondue(300, 652, 1.2, "#ffa8a8"))
    S.add(jet_feu(bx + 20, by + 6, 320, 600, 90, graine=4))
    S.add(bougie(560, 652, 1.2, flamme=False, couleur="#d0bfff"))
    S.add(flammeche(560, 652 - 96 * 1.2 + 6, 0.35))
    S.add(flammeche_(650, 680, 0.85, expr="souffle", regard=(-1, 0)))
    S.add(texte(330, 410, "FFFOUUU !", 54, "#e03131", contour="#fff"), texte(620, 450, "pfff…", 40, "#9c36b5", contour="#fff"))
    S.lumiere(560, 545, 60, "#ffd43b", 0.6)
    S.cachette(505, 490, "air")
    return S


def p04():
    """Plan large : la leçon de vol ; Flammèche tombe dans le foin."""
    S = Scene()
    ciel(S, "#91a7ff", "#e7f5ff")
    S.add(nuage(160, 130, 1.0), nuage(620, 220, 0.8))
    S.add(dragon_vol(240, 160, 0.4, **couleurs(BRAISE)), dragon_vol(520, 100, 0.34, **couleurs(OLIVE)), dragon_vol(640, 280, 0.3, flip=True, **couleurs(GRELON)))
    S.add(ecole(110, 560, 0.4))
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)
    S.add(meule_foin(520, 760, 1.2))
    S.add(chemin("M 380 330 q 60 -60 100 0 q 40 60 0 100 q -40 40 60 120", stroke="#cc5de8", sw=4, stroke_dasharray="10 10"))
    S.add(flammeche_(540, 650, 0.7, expr="oups", bras="haut", rot=150))
    S.add(texte(660, 470, "Boum !", 60, "#e67700", contour="#fff"))
    S.add(grimoire(150, 790, 1.2, expr="surpris", bras="joues", regard=(1, 0)))
    return S


def p05():
    """Plan moyen : la leçon de magie ; une grenouille… et une petite fleur."""
    S = Scene()
    classe(S)
    S.add(table(400, 790, 640, 120, couleur="#a0693a"))
    S.add(olive(170, 680, 1.15, expr="fier", bras="tient", objet=baguette_magique(56, -90, 0.9, rot=20)))
    S.add(perso("grenouille", 320, 652, 0.45, expr="surpris"))
    S.add(etincelles(320, 580, 0.8, OR, graine=3))
    S.add(caillou(560, 652, 0.4, "#adb5bd"))
    S.add(fleur(560, 652, 0.5, "#ff8787", tige=34))
    S.add(etincelles(560, 600, 0.7, "#f783ac", graine=5))
    S.add(flammeche_(670, 680, 0.85, expr="oups", bras="tient", objet=baguette_magique(-50, -90, 0.8, rot=-20), regard=(-1, 0)))
    S.dessus(texte(400, 380, "Abracadragon !", 54, "#5f3dc4", contour="#fff"))
    return S


def p06():
    """Gros plan, au soir : Flammèche est triste ; la maîtresse la console."""
    S = Scene()
    montagne_nuages(S, soir=True)
    S.add(rect(0, 640, 800, 160, "#ced4da"), rect(0, 640, 800, 14, "#adb5bd"))
    S.add(pierres(0, 654, 800, 146, "#ced4da", pas_=30, larg=70, opacite=0.3))
    S.add(grimoire(560, 790, 1.7, expr="sourire", bras="epaule", regard=(-1, 0)))
    S.add(flammeche_(360, 790, 1.15, expr="triste", larmes=True, bras="bas"))
    S.camera(1.3, 470, 560)
    S.dessus(bulle(420, 100, 600, 110, "Attends un peu.\nChaque dragon a son talent.", 32, pointe=S.vers_page(560, 520)))
    S.cachette(150, 640)
    return S


def p07():
    """Plan large : la cour, la nuit ; les lanternes de papier attendent."""
    S = Scene()
    cour(S)
    lanternes(S, y=250)
    S.add(grimoire(400, 790, 1.4, expr="content", bras="ouverts"))
    S.add(braise(150, 800, 1.05, expr="rire"), olive(640, 800, 0.95, expr="content"))
    S.add(flammeche_(260, 800, 0.75, expr="sourire"), grelon(530, 800, 0.9, expr="sourire"))
    S.cachette(730, 450, "air")
    S.dessus(texte(400, 160, "La fête des lanternes !", 48, "#ffe066", contour="#5f3dc4"))
    return S


def p08():
    """Plan moyen : raté ! brûlée, gelée, enfumée."""
    S = Scene()
    cour(S)
    sol_y, sd = 790, 0.85
    bouche_y = sol_y + BOUCHE[1] * sd
    for x, e, c in ((215, "brulee", "#ff8787"), (455, "gelee", "#74c0fc"), (695, "eteinte", "#69db7c")):
        poteau_lanterne(S, x, sol_y, bouche_y, 1.0, c, cote=-1, brulee=e == "brulee", gelee=e == "gelee")
    S.add(flammeche(200, bouche_y - 10, 0.7), flammeche(232, bouche_y, 0.5))
    S.lumiere(215, bouche_y - 10, 80, "#ff922b", 0.6)
    S.add(braise(90, sol_y, sd, expr="oups", bras="joues", regard=(1, 0)))
    S.add(grelon(330, sol_y, sd, expr="souffle"))
    S.add(jet_givre(350, bouche_y, 412, bouche_y, 40, graine=2))
    S.add(olive(570, sol_y, sd, expr="souffle"))
    S.add(jet_fumee(590, bouche_y, 660, bouche_y - 20, 40, graine=4, nb=5))
    S.cachette(110, 480, "air")
    S.camera(1.15, 400, 600)
    S.dessus(texte(200, 330, "Pouf !", 48, "#ff922b", contour="#fff"), texte(560, 120, "Oh non !", 60, "#ffe066", contour="#c92a2a"))
    return S


def p09():
    """Gros plan : Flammèche souffle tout doucement ; la lanterne s'allume."""
    S = Scene()
    cour(S)
    sd = 1.3
    bouche_y = 800 + BOUCHE[1] * sd
    poteau_lanterne(S, 520, 800, bouche_y - 20, 1.1, "#da77f2", cote=1, allumee=True)
    S.add(flammeche_(290, 800, sd, expr="souffle", regard=(1, 0), bras="mains_jointes"))
    S.add(jet_feu(316, bouche_y, 420, bouche_y - 8, 40, graine=6))
    S.add(flammeche(456, bouche_y - 18, 0.5, rot=80))
    S.add(paillettes(600, 520, 1.0, "#ffe066"), paillettes(440, 470, 0.7, "#ffe066"))
    S.camera(1.3, 400, 560)
    S.dessus(texte(250, 130, "pfff…", 50, "#e599f7", contour="#fff"))
    return S


def p10():
    """Plan large : une, deux, dix lanternes ! La cour brille."""
    S = Scene()
    cour(S)
    lanternes(S, y=200, nb=6, etat=lambda k: "allumee")
    lanternes(S, x0=-20, x1=820, y=360, creux=30, nb=5, etat=lambda k: "allumee")
    S.add(dragon_vol(520, 300, 0.36, **couleurs(FLAMMECHE)))
    S.add(braise(130, 800, 1.0, expr="bouche_bee", bras="joues"), olive(660, 800, 0.95, expr="bouche_bee"))
    S.add(grelon(530, 800, 0.85, expr="joie", bras="haut"))
    S.add(grimoire(300, 800, 1.2, expr="rire", bras="applaudit"))
    S.cachette(745, 500, "air")
    return S


def p11():
    """Plan large : bravo, Flammèche ! Tout le monde danse sous les lanternes."""
    S = Scene()
    cour(S)
    lanternes(S, y=220, nb=6, etat=lambda k: "allumee")
    S.add(grimoire(140, 790, 1.4, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(braise(330, 790, 1.0, expr="rire", bras="danse"))
    S.add(flammeche_(460, 790, 0.95, expr="joie", bras="victoire"))
    S.add(olive(590, 790, 0.95, expr="rire", bras="danse", flip=True))
    S.add(grelon(710, 790, 0.85, expr="rire", bras="haut"))
    S.add(notes(560, 470, 1.0, "#ffe066"), etincelles(460, 470, 1.0, "#ffe066", graine=8))
    S.cachette(745, 500, "air")
    S.dessus(bulle(330, 120, 520, 110, "Bravo, Flammèche ! Ton feu est\nle plus doux de toute l'école !", 28, pointe=(180, 480)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("flammeche-seule.svg", vignette),
    ("01-la-rentree.svg", p01), ("02-la-classe.svg", p02), ("03-le-feu.svg", p03), ("04-le-vol.svg", p04),
    ("05-la-magie.svg", p05), ("06-le-soir.svg", p06), ("07-les-lanternes.svg", p07), ("08-rate.svg", p08),
    ("09-pfff.svg", p09), ("10-toutes-allumees.svg", p10), ("11-bravo.svg", p11),
]
