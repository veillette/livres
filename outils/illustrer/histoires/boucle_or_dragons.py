"""Boucle d'or et les trois dragons — le conte des trois ours, chez les dragons.

Tout en haut de la montagne, dans une grotte à la porte ronde, vivent Papa
dragon, Maman dragonne et Bébé dragon. Papa réchauffe la soupe d'un souffle
de feu — bien trop chaude ! Pendant que la famille fait un tour dans le
ciel, Boucle d'or entre : bols, chaises, lits (un tas d'or, des coussins, un
nid de paille)… Au retour, pas de fuite : Boucle d'or demande pardon, Papa
réchauffe la soupe tout doucement et tout le monde mange ensemble.

Plans : couverture moyen · 1 large (la montagne) · 2 moyen (le souffle sur
la marmite) · 3 large (l'envol ; Boucle d'or arrive) · 4 moyen (les bols) ·
5 gros plan (CRAC !) · 6 large (la chambre) · 7 moyen (le retour) · 8 gros
plan (ma soupe !) · 9 moyen (ma chaise !) · 10 large (la voilà !) · 11 gros
plan (le réveil) · 12 moyen (pardon) · 13 large (le repas) · 14 moyen (toc
toc).
"""
from base import *
from base import _assombrir
from fantastique import personne, dragon_vol, chaudron, OR
from contes import bol_porridge, chaise
from dragons import *

ID = "boucle-or-dragons"
PAPIER_PEINT = "pois"

BOUCLE = dict(coiffure="boucles", cheveux="blond", peau="claire", habit="#4dabf7", chaussures="#1864ab", nez="retrousse")
PAPA = dict(couleur="#fa5252", ventre="#ffd8a8")
MAMAN = dict(couleur="#9775fa", ventre="#e5dbff", noeud="#f783ac")
BEBE = dict(couleur="#ffa94d", ventre="#fff3bf")
BOLS = (("#e03131", 1.35), ("#7048e8", 1.1), ("#f08c00", 0.8))


def boucle(x, y, s=1.25, **k):
    return personne(x, y, s, **{**BOUCLE, **k})


def papa(x, y, s=1.9, **k):
    return dragon_habille(x, y, s, **{**PAPA, **k})


def maman(x, y, s=1.55, **k):
    return dragon_habille(x, y, s, **{**MAMAN, **k})


def bebe(x, y, s=1.05, **k):
    return dragon_habille(x, y, s, **{**BEBE, **k})


# --- Décors -------------------------------------------------------------------

def dehors(S, soir=False, ouverte=False, lumiere=False):
    if soir:
        ciel(S, "#ffa94d", "#fff3bf")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(nuage(130, 110, 0.7), nuage(700, 80, 0.5))
    lointain(S, 520, "#b197fc", hauteur=160, graine=4)
    montagne_grotte(S, 640, porte="#2f9e44", ouverte=ouverte, lumiere=lumiere)
    sol(S, 640, "#8ce99a", couleur2="#69db7c", y2=720)
    S.add(chemin("M 330 800 Q 380 720 430 646 L 470 646 Q 480 720 520 800 Z", "#e9d8a6"))
    S.add(fleur(80, 700, 0.7, "#ff8787"), fleur(740, 720, 0.8, "#cc5de8"), touffe(200, 760), touffe(640, 780))


def cuisine(S):
    grotte_dedans(S, 580, papier=None)
    S.add(etagere(170, 200, 230, objets=g([bol_porridge(110, 200, 0.5, "#e03131"), bol_porridge(170, 200, 0.5, "#7048e8"),
                                           bol_porridge(230, 200, 0.5, "#f08c00")])))
    S.add(torche(700, 260, 1.0, S=S))


def table_bols(S, y=640, vides=(), fumee=False, w=600, x=400):
    S.add(table(x, y, w, 140, couleur="#a0693a", nappe="#ffd8a8"))
    pas_ = w * 0.3
    for k, (c, s) in enumerate(BOLS):
        nom = ("papa", "maman", "bebe")[k]
        S.add(bol_porridge(x + (k - 1) * pas_, y - 158, s * min(1.0, w / 600), c, vide=nom in vides, fumee=fumee and k == 0))


def chambre(S):
    grotte_dedans(S, 560, mur="#e3d5f5", sol_c="#a68a73", voute="#7c6a8a")
    S.add(torche(400, 230, 0.9, S=S))
    S.add(cadre_mur(150, 220, 150, 110, "#ffd8a8"))
    S.add(place(g([bebe(0, 0, 0.3), papa(-40, 0, 0.42), maman(40, 0, 0.36)]), 225, 322))
    S.add(cercle(640, 200, 56, "#6d4424"), cercle(640, 200, 46, "#a5d8ff"),
          trait(640, 154, 640, 246, "#6d4424", 6), trait(594, 200, 686, 200, "#6d4424", 6))


def boucle_dans_nid(expr="dort", **k):
    """Boucle d'or couchée dans le nid de Bébé dragon (repère du nid)."""
    m = [nid_paille(0, 0, 1.0),
         personne(80, -50, 0.62, rot=-90, expr=expr, **{**BOUCLE, **k}),
         chemin("M -140 -30 Q 0 20 140 -30 Q 120 6 0 12 Q -120 6 -140 -30 Z", "#f6c453"),
         chemin("M -100 -14 Q 0 8 100 -14", stroke="#e0a526", sw=4)]
    return g(m)


def trois_lits(S, dormeuse=False, y=760):
    S.add(tas_or(145, y - 20, 1.1, w=250, h=150, couronne_=True))
    S.add(coussins(380, y - 20, 1.05))
    nid = boucle_dans_nid() if dormeuse else nid_paille(0, 0, 1.0)
    S.add(place(nid, 630, y, 1.05))


# --- Pages --------------------------------------------------------------------

def couverture():
    S = Scene()
    dehors(S)
    S.add(papa(150, 790, 1.55, expr="surpris", regard=(1, 0)))
    S.add(maman(640, 790, 1.3, expr="surpris", bras="joues", regard=(-1, 0)))
    S.add(bebe(520, 795, 0.85, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(boucle(380, 790, 1.2, expr="oups", bras="bouche", regard=(1, 0)))
    S.cachette(40, 250, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bebe(200, 262, 0.95, expr="content", bras="porte", objet=bol_porridge(0, -70, 0.7, "#f08c00", fumee=True)))
    return S


def p01():
    """Plan large : la montagne et la famille devant sa porte ronde."""
    S = Scene()
    dehors(S)
    S.add(papa(170, 780, 1.45, expr="content", regard=(1, 0)))
    S.add(maman(640, 780, 1.2, expr="content", bras="salut", regard=(-1, 0)))
    S.add(bebe(440, 790, 0.85, expr="rire", bras="haut"))
    S.cachette(760, 330, "air")
    return S


def p02():
    """Plan moyen : Papa souffle sur la marmite, bien trop fort."""
    S = Scene()
    cuisine(S)
    S.add(chaudron(560, 760, 1.1, contenu="#ff922b", fumee=True, feu=False, bulles_=True))
    S.add(papa(220, 790, 1.5, expr="souffle", bras="hanches"))
    bx, by = 220, 790 - 116 * 1.5
    S.add(jet_feu(bx + 30, by + 10, 520, 690, 110, graine=3))
    S.add(maman(700, 790, 1.15, expr="surpris", bras="joues", regard=(-1, 0)))
    S.add(texte(560, 520, "Fffouuu !", 52, "#e8590c", contour="#fff"))
    S.dessus(bulle(420, 110, 520, 100, "Allons faire un tour dans le ciel\npendant qu'elle refroidit !", 30,
                   pointe=(650, 520)))
    S.cachette(70, 130, "air")
    return S


def p03():
    """Plan large : la famille s'envole ; Boucle d'or grimpe le sentier."""
    S = Scene()
    dehors(S, ouverte=True)
    S.add(dragon_vol(230, 150, 0.55, **{k: v for k, v in PAPA.items()}))
    S.add(dragon_vol(470, 110, 0.45, **{k: v for k, v in MAMAN.items() if k != "noeud"}))
    S.add(dragon_vol(650, 200, 0.32, expr="rire", **BEBE))
    S.add(boucle(560, 780, 0.95, expr="surpris", bras="montre", regard=(-1, -1)))
    S.add(pensee(690, 400, 70, texte(690, 418, "?", 60, "#1c7ed6"), depuis=(600, 560)))
    return S


def p04():
    """Plan moyen : les trois bols ; le petit est vide."""
    S = Scene()
    cuisine(S)
    table_bols(S, 650, vides=("bebe",), fumee=True)
    S.add(boucle(660, 800, 1.15, expr="miam", bras="bouche"))
    S.add(texte(220, 340, "Trop chaud !", 34, "#e03131", contour="#fff"),
          texte(410, 300, "Trop froid !", 34, "#1c7ed6", contour="#fff"),
          texte(600, 360, "Miam !", 46, "#e67700", contour="#fff"))
    return S


def p05():
    """Gros plan : la petite chaise se casse."""
    S = Scene()
    cuisine(S)
    S.add(chaise(200, 760, 1.5, "#868e96"))
    S.add(place(coussins(0, 0, 0.45, ("#9775fa", "#e599f7")), 385, 616))
    S.add(chaise(385, 745, 1.2, "#7048e8"))
    S.add(chaise(590, 770, 0.85, "#f08c00", cassee=True))
    S.add(boucle(600, 790, 1.15, expr="oups", bras="haut", rot=-14))
    S.add(eclat(580, 700, 1.2, "#ffd43b"))
    S.camera(1.3, 420, 560)
    x1, y1 = S.vers_page(200, 430)
    x2, y2 = S.vers_page(385, 470)
    S.dessus(texte(600, 150, "CRAC !", 96, "#c92a2a", contour="#fff", rot=-8),
             texte(x1 + 10, y1, "Trop dure !", 34, "#495057", contour="#fff"),
             texte(x2 + 20, y2, "Trop molle !", 34, "#7048e8", contour="#fff"))
    return S


def p06():
    """Plan large : la chambre ; Boucle d'or dort dans le nid."""
    S = Scene()
    chambre(S)
    trois_lits(S, dormeuse=True)
    S.add(zzz(690, 520, 1.1))
    S.dessus(texte(400, 450, "Juste comme il faut…", 44, "#5f3dc4", contour="#fff"))
    return S


def p07():
    """Plan moyen : retour de promenade, la porte est ouverte."""
    S = Scene()
    dehors(S, ouverte=True)
    S.add(papa(170, 790, 1.5, expr="surpris", bras="montre", regard=(1, 0)))
    S.add(maman(660, 790, 1.25, expr="inquiet", regard=(-1, 0)))
    S.add(bebe(300, 795, 0.85, expr="surpris", bras="joues", regard=(1, 0)))
    S.dessus(bulle(400, 100, 440, 90, "Tiens ? La porte est ouverte !", 30, pointe=(220, 330)))
    return S


def p08():
    """Gros plan : Bébé dragon pleure devant son bol vide ; Papa fume du nez."""
    S = Scene()
    cuisine(S)
    table_bols(S, 650, vides=("bebe",))
    S.add(papa(170, 800, 1.6, expr="fache", bras="hanches"))
    S.add(jet_fumee(160, 598, -10, 540, 44, "#dee2e6", graine=2, nb=6), jet_fumee(180, 598, 360, 540, 44, "#dee2e6", graine=5, nb=6))
    S.add(bebe(580, 800, 1.1, expr="pleure", larmes=True, bras="yeux"))
    S.cachette(320, 290, "air")
    S.camera(1.3, 420, 520)
    S.dessus(bulle(570, 90, 420, 100, "Quelqu'un a mangé\ntoute ma soupe !", 32, pointe=S.vers_page(580, 560)))
    return S


def p09():
    """Plan moyen : la petite chaise cassée."""
    S = Scene()
    cuisine(S)
    S.add(chaise(110, 740, 1.4, "#868e96"))
    S.add(place(coussins(0, 0, 0.42, ("#9775fa", "#e599f7")), 300, 618))
    S.add(chaise(300, 740, 1.1, "#7048e8"))
    S.add(chaise(500, 770, 0.8, "#f08c00", cassee=True))
    S.add(maman(700, 800, 1.25, expr="surpris", bras="bouche", regard=(-1, 0)))
    S.add(bebe(400, 800, 0.95, expr="pleure", larmes=True, bras="montre", flip=True))
    S.dessus(bulle(400, 100, 440, 100, "Et quelqu'un a cassé\nma petite chaise !", 32, pointe=(400, 520)))
    return S


def p10():
    """Plan large : la famille découvre Boucle d'or dans le nid."""
    S = Scene()
    chambre(S)
    S.add(place(boucle_dans_nid(), 600, 770, 1.0))
    S.add(zzz(640, 560, 1.0))
    S.add(papa(130, 800, 1.4, expr="surpris", regard=(1, 0)))
    S.add(maman(310, 800, 1.1, expr="surpris", bras="bouche", regard=(1, 0)))
    S.add(bebe(440, 800, 0.85, expr="bouche_bee", bras="montre"))
    S.dessus(bulle(470, 110, 300, 90, "La voilà !", 44, pointe=(450, 540)))
    return S


def p11():
    """Gros plan : Boucle d'or se réveille nez à nez avec Bébé dragon."""
    S = Scene()
    chambre(S)
    S.add(place(boucle_dans_nid(expr="surpris", regard=(1, 0), bras="joues"), 300, 770, 1.7))
    S.add(bebe(620, 790, 1.3, expr="rire", bras="salut", regard=(-1, 0)))
    S.cachette(200, 400, "air")
    S.camera(1.3, 450, 590)
    S.dessus(bulle(560, 100, 400, 100, "N'aie pas peur !\nTu veux jouer ?", 32, pointe=S.vers_page(600, 560)))
    return S


def p12():
    """Plan moyen : Boucle d'or demande pardon."""
    S = Scene()
    cuisine(S)
    S.add(boucle(250, 790, 1.25, expr="timide", bras="mains_jointes", regard=(1, 0)))
    S.add(papa(560, 790, 1.6, expr="sourire", bras="large", regard=(-1, 0)))
    S.add(bebe(400, 795, 0.8, expr="content", regard=(-1, 0)))
    S.dessus(bulle(260, 110, 360, 90, "Pardon !", 40, pointe=(260, 440)),
             bulle(580, 230, 380, 100, "Une soupe,\nça se refait !", 32, pointe=(560, 400)))
    return S


def p13():
    """Plan large : tout le monde mange ensemble."""
    S = Scene()
    cuisine(S)
    S.add(maman(120, 720, 1.15, expr="rire", regard=(1, 0)))
    S.add(boucle(260, 720, 1.05, expr="rire", bras="haut"))
    S.add(bebe(390, 720, 0.85, expr="joie", bras="haut"))
    table_bols(S, 800, w=440, x=250)
    S.add(chaudron(540, 790, 0.7, contenu="#ff922b", fumee=True, feu=False, bulles_=False))
    S.add(papa(690, 800, 1.35, expr="souffle", regard=(-1, 0)))
    S.add(jet_feu(668, 650, 575, 712, 34, graine=8))
    S.add(texte(600, 560, "Pfff…", 40, "#e8590c", contour="#fff"))
    S.add(coeur(250, 330, 1.2), coeur(320, 280, 0.8, "#ff8787"))
    S.cachette(480, 380, "air")
    return S


def p14():
    """Plan moyen : Boucle d'or frappe avant d'entrer."""
    S = Scene()
    dehors(S)
    S.add(boucle(300, 790, 1.3, expr="content", bras="coucou", regard=(1, 0)))
    S.add(bebe(620, 790, 1.0, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(texte(560, 330, "Toc, toc, toc !", 50, "#2f9e44", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bebe-dragon-seul.svg", vignette),
    ("01-la-montagne.svg", p01), ("02-trop-chaude.svg", p02), ("03-l-envol.svg", p03), ("04-les-bols.svg", p04),
    ("05-crac.svg", p05), ("06-les-lits.svg", p06), ("07-le-retour.svg", p07), ("08-ma-soupe.svg", p08),
    ("09-ma-chaise.svg", p09), ("10-la-voila.svg", p10), ("11-le-reveil.svg", p11), ("12-pardon.svg", p12),
    ("13-tous-ensemble.svg", p13), ("14-toc-toc.svg", p14),
]
