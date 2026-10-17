"""Les crêpes de Papi Jo — la Chandeleur avec un grand-père qui oublie.

Chaque 2 février, Margot fait des crêpes chez Papi Jo, avec la pièce qu'on
tient dans la main pour la chance. Cette année, Papi range ses lunettes au
frigo et met du sel à la place du sucre : « Ma tête oublie des choses. »
Margot dessine la recette et la colle sur le frigo ; ensemble, ils refont
la pâte, et les mains de Papi se souviennent de faire sauter les crêpes.
La Chandeleur est le décor ; l'histoire parle d'un grand-parent dont la
mémoire flanche, et de la tendresse qui reste.

Plans : 1 large (la rue, chez Papi) · 2 gros plan (la pièce) · 3 moyen (les
lunettes au frigo) · 4 moyen (c'est salé) · 5 gros plan (ma tête oublie) ·
6 moyen (l'idée) · 7 gros plan (la recette dessinée) · 8 moyen (ensemble) ·
9 large (hop !) · 10 moyen (le chapeau-crêpe) · 11 moyen (le sirop) · 12 gros
plan (mon cœur se souvient).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from objets import bol
from fables import oeuf
from metiers import tablier
from fetes import poele_crepe, pile_crepes

ID = "crepes-papi-jo"
PAPIER_PEINT = "pois"

OR_ = "#fcc419"
CREPE = "#f6c453"

MARGOT = dict(peau="doree", cheveux="brun", coiffure="tresses", habit="#ae3ec9", robe=False, jambes="#364fc7", yeux="cils",
              nez="retrousse")
PAPI = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#1c7ed6", robe=False, jambes="#5c3d2e",
            nez="rond", carrure="ronde", tenue=tablier("#ffffff"))
MAMAN = dict(stature="adulte", peau="doree", cheveux="brun", coiffure="carre", habit="#2f9e44", carrure="fine", nez="pointu")


def moustache():
    """La grosse moustache blanche de Papi Jo (coiffe)."""
    return g([chemin("M -2 -128 Q -18 -138 -34 -126 Q -22 -120 -2 -124 Z", "#f1f3f5"),
              chemin("M 2 -128 Q 18 -138 34 -126 Q 22 -120 2 -124 Z", "#f1f3f5")])


def margot(x, y, s=1.15, **k):
    return personne(x, y, s, **{**MARGOT, **k})


def papi(x, y, s=1.15, lunettes=True, **k):
    acc = ("lunettes",) if lunettes else ()
    return personne(x, y, s, **{**PAPI, "acc": acc, "coiffe": moustache(), **k})


def piece_or(x, y, s=1.0):
    return place([cercle(0, 0, 14, volume(OR_, 0.45, 0.72)), cercle(0, 0, 10, "none", stroke="#f59f00", stroke_width=2),
                  texte(0, 5, "1", 12, "#b07a00")], x, y, s)


def lunettes_seules(x, y, s=1.0):
    return place([cercle(-16, 0, 13, "none", stroke=ENCRE, stroke_width=3), cercle(16, 0, 13, "none", stroke=ENCRE, stroke_width=3),
                  trait(-3, 0, 3, 0, ENCRE, 3), trait(-29, -2, -40, -6, ENCRE, 3), trait(29, -2, 40, -6, ENCRE, 3)], x, y, s)


def boite(x, y, s=1.0, mot="SEL", c="#4dabf7"):
    return place([rect(-28, -70, 56, 70, volume(c, 0.3, 0.75), rx=6), rect(-28, -76, 56, 12, _assombrir(c, 0.8), rx=4),
                  texte(0, -28, mot, 16, "#fff")], x, y, s)


def bouteille_lait(x, y, s=1.0):
    return place([rect(-18, -70, 36, 70, "#f8f9fa", rx=6, stroke="#dee2e6", stroke_width=2), rect(-10, -86, 20, 18, "#4dabf7", rx=3),
                  rect(-18, -46, 36, 18, "#4dabf7")], x, y, s)


def sirop(x, y, s=1.0):
    """Cruche de sirop d'érable ; (x, y) = base."""
    return place([chemin("M -24 0 L -24 -50 Q -24 -70 -10 -76 L -10 -90 L 10 -90 L 10 -76 Q 24 -70 24 -50 L 24 0 Z", volume("#c2410c", 0.35, 0.7)),
                  rect(-16, -46, 32, 22, "#fff4e6", rx=3), chemin("M -6 -40 l 6 -6 l 6 6 l -6 10 Z", "#e03131"),
                  chemin("M 24 -60 Q 40 -60 36 -36", stroke="#c2410c", sw=5)], x, y, s)


def frigo(x, y, s=1.0, ouvert=False, recette=False):
    """Réfrigérateur ; (x, y) = sol, au milieu. ouvert : porte ouverte sur
    les étagères (œufs, beurre… et les lunettes de Papi)."""
    m = [rect(-90, -380, 180, 380, volume("#f1f3f5", 0.15, 0.85), rx=14, stroke="#ced4da", stroke_width=3),
         trait(-90, -250, 90, -250, "#ced4da", 3)]
    if ouvert:
        m += [rect(-80, -370, 160, 360, "#e7f5ff", rx=8)]
        for yy in (-280, -190, -100):
            m.append(rect(-80, yy, 160, 6, "#adb5bd"))
        m += [oeuf(-50, -282, 0.45), oeuf(-30, -282, 0.45), oeuf(-10, -282, 0.45),
              rect(20, -205, 50, 16, OR_, rx=3), lunettes_seules(-30, -205, 0.8),
              bouteille_lait(40, -102, 0.8), rect(-60, -130, 50, 30, "#69db7c", rx=6),
              poly([(90, -380), (160, -360), (160, -20), (90, 0)], volume("#e9ecef", 0.2, 0.85))]
    else:
        m += [rect(64, -330, 10, 60, "#adb5bd", rx=4), rect(64, -230, 10, 80, "#adb5bd", rx=4)]
        if recette:
            m.append(place(feuille_recette(), 0, -170, 0.42))
    return place(m, x, y, s)


def feuille_recette():
    """La recette dessinée par Margot (repère : centre de la feuille)."""
    m = [rect(-180, -230, 360, 460, "#ffffff", rx=6, stroke="#dee2e6", stroke_width=4),
         cercle(-150, -210, 10, "#e03131"), cercle(150, -210, 10, "#1c7ed6"),
         texte(0, -180, "CRÊPES", 40, "#e8590c")]
    # trois œufs
    m += [texte(-140, -110, "3", 40, ENCRE)] + [oeuf(-80 + k * 44, -90, 0.9) for k in range(3)]
    # deux tasses de farine, deux tasses de lait
    for k in range(2):
        m.append(rect(-110 + k * 50, -50, 40, 44, "#fff", stroke="#868e96", stroke_width=3, rx=6))
        m.append(rect(-110 + k * 50, -40, 40, 34, "#f1f3f5", rx=6))
        m.append(rect(30 + k * 50, -50, 40, 44, "#fff", stroke="#868e96", stroke_width=3, rx=6))
        m.append(rect(30 + k * 50, -40, 40, 34, "#d0ebff", rx=6))
    m += [texte(-40, 20, "farine", 22, "#868e96"), texte(80, 20, "lait", 22, "#1c7ed6"),
          # une pincée de sel… et le sucre barré
          cercle(-100, 70, 4, "#adb5bd"), cercle(-94, 64, 3, "#adb5bd"), texte(-40, 78, "sel", 26, ENCRE),
          texte(80, 78, "sucre", 26, "#adb5bd"), trait(30, 62, 130, 82, "#e03131", 5), trait(30, 82, 130, 62, "#e03131", 5),
          # le bol qui tourne, puis la poêle
          ellipse(-60, 150, 50, 16, "#74c0fc"), chemin("M -110 150 Q -110 200 -60 200 Q -10 200 -10 150 Z", "#74c0fc"),
          chemin("M -80 140 q 20 -20 40 0", stroke="#e8590c", sw=4), poly([(-40, 140), (-46, 130), (-34, 132)], "#e8590c"),
          ellipse(90, 170, 54, 14, "#343a40"), rect(140, 164, 50, 12, "#495057", rx=6), ellipse(90, 164, 40, 9, CREPE)]
    return g(m)


def cuisine(S, y=600):
    piece(S, "cuisine", y)
    S.add(fenetre(300, 90, 170, 150, "#d0ebff", rideaux="#f76707",
                  contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 200, 800, 100, "#f8f9fa"), sapin(420, 210, 0.3, neige=True)])))


def cuisiniere(x, y, s=1.0):
    """Cuisinière et sa poêle, contre le mur ; (x, y) = sol."""
    m = [rect(-90, -180, 180, 180, volume("#e9ecef", 0.15, 0.85), rx=8, stroke="#ced4da", stroke_width=3),
         rect(-70, -140, 140, 100, "#343a40", rx=8), rect(-60, -130, 120, 80, "#495057", rx=6),
         rect(-90, -196, 180, 18, "#ced4da", rx=4)]
    for k in range(4):
        m.append(cercle(-60 + k * 40, -166, 7, "#868e96"))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    cuisine(S, 620)
    S.add(frigo(110, 680, 0.9, recette=True))
    S.add(cuisiniere(660, 680, 0.9))
    S.add(papi(470, 790, 1.35, expr="rire", bras="tient", regard=(0, -1),
               objet=poele_crepe(*ancre(80, -146, "tient", "ancien", "ronde"), 0.8)))
    S.add(texte(470, 230, "Hop !", 50, "#f76707", contour="#fff", rot=-8))
    S.add(margot(270, 800, 1.2, expr="rire", bras="montre", regard=(1, -1), objet=piece_or(86, -136, 1.0)))
    S.cachette(770, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pile_crepes(200, 240, 1.4))
    S.add(chemin("M 120 150 Q 200 130 280 150 Q 270 190 250 200", stroke="#c2410c", sw=10, opacity=0.8))
    return S


def p01():
    """Plan large : la rue en hiver, la maison de Papi Jo."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    collines(S, 540, "#e7f5ff", graine=7, bosquets=False)
    sol(S, 600, "#f8f9fa", bosse=10)
    S.add(maison(470, 610, 1.3, mur="#ffd8a8", toit="#5c3d2e", porte="#2f9e44", volets="#2f9e44"))
    # Papi Jo à la fenêtre de droite
    fx, fy = 470 + 64 * 1.3, 610 - 100 * 1.3
    S.add(cercle(fx, fy + 10, 15, "#f3c3a0"), chemin(f"M {fx - 14} {fy + 4} q 14 -14 28 0", stroke="#e9ecef", sw=6),
          cercle(fx - 5, fy + 8, 2, ENCRE), cercle(fx + 5, fy + 8, 2, ENCRE), chemin(f"M {fx - 8} {fy + 16} q 8 -4 16 0", stroke="#f1f3f5", sw=4))
    S.add(sapin(140, 620, 0.9, neige=True), sapin(760, 630, 0.8, neige=True))
    S.add(chemin("M 380 800 Q 420 700 470 612 L 500 612 Q 480 700 520 800 Z", "#dee2e6"))
    S.add(personne(270, 760, 1.05, expr="sourire", bras="coucou", regard=(1, -0.5), **MAMAN))
    S.add(margot(400, 770, 0.9, expr="rire", bras="court", regard=(1, -0.5)))
    S.add(texte(620, 220, "Coucou !", 38, "#f76707", contour="#fff", rot=6))
    S.cachette(40, 780)
    return S


def p02():
    """Gros plan : la pièce porte-bonheur."""
    S = Scene()
    cuisine(S, 600)
    S.add(papi(520, 800, 1.6, expr="malin", bras="montre", flip=True, regard=(-1, 0), objet=piece_or(86, -150, 1.5)))
    S.add(margot(250, 800, 1.45, expr="bouche_bee", bras="mains_jointes", regard=(1, -0.3)))
    S.add(paillettes(390, 460, 0.8))
    S.camera(1.3, 400, 520)
    S.dessus(bulle(400, 100, 480, 100, "Une pièce dans la main,\npour la chance !", 32, pointe=S.vers_page(500, 450)))
    S.cachette(90, 780)
    return S


def p03():
    """Plan moyen : les lunettes rangées au frigo."""
    S = Scene()
    cuisine(S, 600)
    S.add(frigo(470, 760, 1.15, ouvert=True))
    S.add(papi(680, 790, 1.2, lunettes=False, expr="surpris", bras="tete", regard=(-1, 0)))
    S.add(margot(230, 790, 1.15, expr="rire", bras="designe", regard=(1, 0)))
    S.add(bulle(260, 150, 400, 100, "Tes lunettes\nsont au frigo !", 32, pointe=(260, 440)))
    S.cachette(40, 790)
    return S


def p04():
    """Plan moyen : c'est salé !"""
    S = Scene()
    cuisine(S, 600)
    S.add(papi(540, 720, 1.2, expr="surpris", bras="tient", regard=(-1, 0.3),
               objet=boite(*ancre(68, -146, "tient", "ancien", "ronde"), 0.9, "SEL")))
    S.add(margot(260, 730, 1.15, expr="degoute", bras="bouche", regard=(1, 0)))
    S.add(table(400, 800, 560, 110, "#c68642", nappe="#ffe8cc"))
    S.add(bol(400, 676, 1.3, "#74c0fc", "#fff3bf"))
    S.add(boite(520, 682, 0.8, "SUCRE", "#f783ac"), bouteille_lait(280, 682, 0.9))
    S.add(oeuf(330, 682, 0.6), oeuf(350, 684, 0.6))
    S.add(bulle(230, 140, 360, 90, "Beurk ! C'est salé !", 34, pointe=(260, 440)))
    S.cachette(770, 790)
    return S


def p05():
    """Gros plan : « Ma tête oublie des choses. »"""
    S = Scene()
    cuisine(S, 600)
    S.add(papi(450, 800, 1.6, expr="triste", bras="pense", regard=(-0.5, 0.3)))
    S.add(margot(240, 800, 1.35, expr="inquiet", bras="tend", regard=(1, -0.5)))
    S.camera(1.3, 400, 520)
    S.dessus(bulle(450, 100, 520, 100, "Ma tête oublie des choses,\nces temps-ci…", 32, pointe=S.vers_page(470, 440)))
    S.cachette(90, 780)
    return S


def crayon(x, y, s=1.0, rot=30, c="#e03131"):
    return place([rect(-6, -60, 12, 60, c, rx=2), poly([(-6, 0), (6, 0), (0, 16)], "#f6c453"), poly([(-2, 10), (2, 10), (0, 16)], ENCRE)], x, y, s, rot=rot)


def p06():
    """Plan moyen : Margot dessine la recette."""
    S = Scene()
    cuisine(S, 600)
    S.add(papi(470, 720, 1.2, expr="content", bras="mains_jointes", regard=(-1, 0.6)))
    S.add(margot(300, 740, 1.15, expr="concentre", bras="porte", regard=(0, 1), objet=crayon(30, -76, 1.0, rot=40)))
    S.add(table(400, 800, 620, 110, "#c68642"))
    S.add(place(feuille_recette(), 400, 670, 0.3, rot=-4))
    for k, c in enumerate(("#e03131", "#1c7ed6", "#2f9e44", "#fab005")):
        S.add(crayon(600 + k * 26, 676, 0.7, rot=80 + k * 6, c=c))
    S.add(bulle(330, 140, 460, 100, "Je vais dessiner la recette !", 30, pointe=(300, 430)))
    S.cachette(30, 790)
    return S


def p07():
    """Gros plan : la recette dessinée, sur le frigo."""
    S = Scene()
    cuisine(S, 700)
    S.add(rect(140, 0, 520, 800, volume("#f1f3f5", 0.15, 0.85), stroke="#ced4da", stroke_width=4))
    S.add(rect(600, 120, 16, 160, "#adb5bd", rx=6))
    S.add(place(feuille_recette(), 380, 420, 0.95, rot=-2))
    for x, y, c in ((215, 215, "#e03131"), (540, 215, "#1c7ed6")):
        S.add(cercle(x, y, 14, c))
    S.cachette(720, 790)
    return S


def p08():
    """Plan moyen : ensemble, en suivant la recette."""
    S = Scene()
    cuisine(S, 600)
    S.add(frigo(110, 700, 1.0, recette=True))
    ox, oy = ancre(26, -74, "porte", "ancien", "ronde")
    S.add(papi(560, 720, 1.2, expr="rire", bras="porte", regard=(-1, 0.6), objet=oeuf(ox, oy, 0.7)))
    S.add(margot(330, 730, 1.15, expr="rire", bras="designe", flip=True, regard=(-1, -0.5)))
    S.add(table(470, 800, 500, 110, "#c68642", nappe="#ffe8cc"))
    S.add(bol(500, 676, 1.3, "#74c0fc", "#fff3bf"), boite(640, 682, 0.8, "FARINE", "#f8f9fa"))
    S.add(bulle(330, 140, 300, 90, "Trois œufs !", 36, pointe=(320, 430)))
    S.add(texte(620, 300, "Crac, crac, crac !", 30, "#f76707", contour="#fff", rot=8))
    S.cachette(770, 790)
    return S


def p09():
    """Plan large : hop ! la crêpe monte jusqu'au plafond."""
    S = Scene()
    cuisine(S, 620)
    S.add(frigo(90, 680, 0.85, recette=True))
    S.add(cuisiniere(680, 680, 0.85))
    S.add(papi(430, 790, 1.15, expr="rire", bras="tient", regard=(0, -1),
               objet=poele_crepe(*ancre(80, -146, "tient", "ancien", "ronde"), 0.8, en_lair=False)))
    S.add(ellipse(510, 60, 70, 18, CREPE, rot=-10, stroke="#e8a200", stroke_width=3))
    S.add(chemin("M 520 400 Q 560 230 520 90", stroke="#868e96", sw=3, opacity=0.5, stroke_dasharray="10 10"))
    S.add(margot(250, 800, 1.0, expr="bouche_bee", bras="joues", regard=(1, -1)))
    S.add(texte(620, 170, "Hop !", 56, "#f76707", contour="#fff", rot=-8))
    S.cachette(30, 790)
    return S


def p10():
    """Plan moyen : la crêpe retombe sur la tête de Margot."""
    S = Scene()
    cuisine(S, 600)
    S.add(cuisiniere(680, 660, 0.85))
    S.add(papi(560, 790, 1.2, expr="rire", larmes=True, bras="applaudit", flip=True, regard=(-1, 0)))
    S.add(margot(300, 790, 1.25, expr="rire", bras="large", regard=(1, 0),
                 objet=g([poele_crepe(-64, -70, 0.7, en_lair=False), piece_or(64, -70, 1.0)]),
                 coiffe=chemin("M -70 -200 Q -60 -226 0 -228 Q 60 -226 70 -200 Q 80 -170 66 -150 Q 50 -190 0 -192 Q -50 -190 -66 -150 Q -80 -170 -70 -200 Z", CREPE, stroke="#e8a200", sw=3)))
    S.add(bulle(330, 140, 320, 90, "Un chapeau-crêpe !", 32, pointe=(530, 430)))
    S.cachette(40, 790)
    return S


def p11():
    """Plan moyen : les crêpes au sirop d'érable."""
    S = Scene()
    cuisine(S, 600)
    S.add(papi(200, 720, 1.15, expr="miam", bras="porte", regard=(1, 0.5)))
    S.add(margot(400, 740, 1.05, expr="miam", bras="porte", regard=(1, 0.3)))
    S.add(personne(610, 720, 1.15, expr="rire", bras="bouche", flip=True, regard=(-1, 0.3), **MAMAN))
    S.add(table(400, 800, 640, 110, "#c68642", nappe="#ffe8cc"))
    S.add(pile_crepes(400, 682, 1.0), sirop(560, 690, 0.9))
    S.add(chemin("M 340 640 Q 400 620 460 640 Q 450 660 430 670", stroke="#c2410c", sw=8, opacity=0.7))
    S.add(bulle(600, 150, 300, 100, "Encore meilleures\nque l'an dernier !", 26, pointe=(610, 440)))
    S.cachette(30, 790)
    return S


def p12():
    """Gros plan : le câlin ; la recette reste sur le frigo."""
    S = Scene()
    cuisine(S, 640)
    S.add(frigo(620, 760, 1.15, recette=True))
    S.add(papi(420, 800, 1.6, expr="content", bras="calin", regard=(-0.5, 0.5)))
    S.add(margot(330, 810, 1.25, expr="content", bras="calin", regard=(1, -0.5)))
    S.add(coeur(250, 380, 0.7, "#f06595"), coeur(560, 330, 0.5, "#f06595"))
    S.camera(1.25, 450, 500)
    S.dessus(bulle(330, 100, 540, 100, "Mon cœur, lui,\nse souvient de toi. Toujours.", 30, pointe=S.vers_page(440, 440)))
    S.cachette(80, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("crepes-seules.svg", vignette),
    ("01-chez-papi.svg", p01), ("02-la-piece.svg", p02), ("03-les-lunettes.svg", p03),
    ("04-c-est-sale.svg", p04), ("05-ma-tete-oublie.svg", p05), ("06-l-idee.svg", p06),
    ("07-la-recette.svg", p07), ("08-ensemble.svg", p08), ("09-hop.svg", p09),
    ("10-sur-la-tete.svg", p10), ("11-le-sirop.svg", p11), ("12-mon-coeur.svg", p12),
]
