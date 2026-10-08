"""Pourquoi la Lune me suit ? — la parallaxe expliquée en voiture.

Jade rentre de nuit en voiture. Les poteaux tout proches filent, les
collines lointaines avancent lentement et la Lune, à 384 000 km, ne bouge
presque pas dans la fenêtre : elle semble suivre la voiture. Chaque enfant,
dans chaque voiture, a la même impression. Pleine lune partout (même nuit).
"""
from base import *
from objets import *
from sciences import *
from fantastique import personne
from base import _assombrir

ID = "lune-voiture"
JADE = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#f76707", robe=False, jambes="#364fc7")
PAPA = dict(peau="doree", cheveux="noir", coiffure="courts", habit="#1971c2", robe=False, jambes="#343a40", barbe="#2b2b3a")
CIEL = ("#1c2a52", "#4c5b9a")


def jade(x, y, s=1.0, **k):
    return personne(x, y, s, **{**JADE, **k})


def papa(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PAPA, **k})


def voiture(x, y, s=1.0, couleur="#e03131", flip=False, passagers=True, enfant=None, phares=True, regard=(1, -1), expr="content"):
    """Voiture de profil, avant à droite ; (x, y) = au sol, sous le milieu.
    On voit par les vitres la tête de l'enfant (à l'arrière) et du conducteur."""
    m = []
    if phares:
        m.append(poly([(158, -66), (330, -110), (330, -10)], "#fff3bf", opacity=0.35))
    if passagers:
        m.append((enfant or jade)(-22, -70, 0.33, expr=expr, regard=regard))
        m.append(papa(58, -70, 0.33, expr="sourire", regard=(1, 0)))
    vitres = "M -62 -100 L -30 -142 L 12 -142 L 12 -100 Z M 22 -100 L 22 -142 L 58 -142 L 90 -100 Z"
    corps = ("M -150 -30 L -150 -82 Q -148 -98 -120 -100 L -70 -102 L -34 -152 L 64 -152 L 104 -102 "
             "L 142 -96 Q 162 -92 162 -62 L 162 -30 Z ")
    m.append(chemin(corps + vitres, couleur, fill_rule="evenodd"))
    m.append(chemin(vitres, "#a5d8ff", opacity=0.25))
    m.append(trait(-150, -60, 162, -60, _assombrir(couleur, 0.75), 4, opacity=0.5))
    m.append(rect(150, -86, 14, 14, "#fff3bf", rx=4))
    m.append(rect(-152, -84, 10, 14, "#ff8787", rx=3))
    m.append(rect(-10, -92, 22, 6, _assombrir(couleur, 0.75), rx=3))
    for rx_ in (-92, 104):
        m.append(cercle(rx_, -30, 30, ENCRE))
        m.append(cercle(rx_, -30, 13, "#adb5bd"))
    return place(m, x, y, s, flip=flip)


def nuit_route(S, graine=1, y_route=640, lune_xy=(560, 250), r=60, collines_=True):
    nuit(S, *CIEL)
    etoiles(S, 40, graine, zone=(0, 0, 800, 480))
    if lune_xy:
        S.add(lune_phase(*lune_xy, r))
    if collines_:
        collines(S, y_route - 40, "#364fc7", graine=graine, hauteur=130)
        collines(S, y_route - 10, "#3b5bdb", graine=graine + 7, n_=4, hauteur=70)
    S.add(rect(0, y_route - 20, 800, 800 - y_route + 20, "#2b8a3e"))
    S.add(rect(0, y_route, 800, 70, "#495057"))
    for k in range(0, 800, 110):
        S.add(rect(k + 20, y_route + 32, 60, 7, "#fff3bf", opacity=0.8))


def sapin_nuit(x, y, s=1.0):
    return sapin(x, y, s, "#2b8a3e", "#2f9e44")


def vue_fenetre(S, poteaux_vite=True, lune_xy=(560, 170), arbre_x=None, cadre=True, graine=2):
    """Vue de l'intérieur de la voiture, par la vitre de Jade."""
    nuit(S, *CIEL)
    etoiles(S, 30, graine, zone=(0, 0, 800, 420))
    if lune_xy:
        S.add(lune_phase(*lune_xy, 50))
    collines(S, 470, "#364fc7", graine=graine, hauteur=120)
    S.add(rect(0, 470, 800, 330, "#2b8a3e"))
    if arbre_x is not None:
        S.add(sapin_nuit(arbre_x, 560, 1.4))
    if poteaux_vite:
        for k, x in enumerate((140, 380, 620)):
            S.add(rect(x - 12, 400, 24, 230, "#8d5524", rx=4, opacity=0.9))
            for d in (1, 2, 3):
                S.add(rect(x + 12 + d * 18, 410 + d * 8, 16, 200 - d * 16, "#8d5524", opacity=0.35 / d))
        S.add(rect(0, 440, 800, 14, "#a0693a", opacity=0.9), rect(0, 520, 800, 14, "#a0693a", opacity=0.9))


def cadre_vitre(S, couleur="#495057"):
    """Encadrement de la vitre (intérieur de la portière)."""
    S.add(chemin("M 0 0 L 800 0 L 800 800 L 0 800 Z M 60 60 L 740 60 Q 760 60 760 80 L 760 640 L 40 640 L 40 80 Q 40 60 60 60 Z",
                 couleur, fill_rule="evenodd"))
    S.add(rect(0, 640, 800, 160, "#343a40"))
    S.add(rect(80, 680, 160, 20, "#868e96", rx=10))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit_route(S, 3, 640, (560, 330), 80)
    S.add(sapin_nuit(90, 610, 0.9), sapin_nuit(720, 615, 0.7))
    S.add(voiture(330, 700, 1.55, expr="rire", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lune_phase(300, 70, 42))
    S.add(jade(150, 262, 1.05, expr="content", bras="montre", regard=(1, -1)))
    return S


def p01():
    S = Scene()
    nuit_route(S, 1, 660, (620, 200), 60)
    S.add(maison(110, 640, 0.9, "#ffe8cc", "#c92a2a", lumiere=True))
    S.add(sapin_nuit(270, 630, 0.7))
    S.add(voiture(470, 730, 1.45, expr="surpris", regard=(1, -1)))
    return S


def p02():
    S = Scene()
    nuit_route(S, 2, 660, (520, 190), 60)
    for x in (80, 720):
        S.add(sapin_nuit(x, 625, 0.8))
    S.add(voiture(380, 730, 1.45, expr="rire", regard=(1, -1)))
    S.add(mouvement(110, 650, 1.3, "#ced4da", rot=0))
    S.add(bulle(230, 110, 360, 90, "Elle me suit !", 46, pointe=(340, 450)))
    return S


def p03():
    S = Scene()
    nuit(S, *CIEL)
    etoiles(S, 40, 4, zone=(0, 0, 800, 480))
    S.add(lune_phase(380, 170, 58))
    collines(S, 600, "#364fc7", graine=5, hauteur=140)
    S.add(rect(0, 580, 800, 220, "#2b8a3e"))
    # route en virage
    S.add(chemin("M -40 800 Q 200 620 420 660 Q 640 700 840 600", stroke="#495057", sw=90))
    S.add(chemin("M -40 800 Q 200 620 420 660 Q 640 700 840 600", stroke="#fff3bf", sw=6, stroke_dasharray="40 40", opacity=0.8))
    for x, y, s in ((470, 620, 1.1), (560, 640, 1.3), (650, 610, 1.0), (130, 640, 1.2)):
        S.add(sapin_nuit(x, y, s))
    S.add(voiture(260, 700, 1.05, expr="rire", regard=(1, -1)))
    S.add(fleche_courbe("M 140 560 Q 260 470 380 540", (380, 540), 40, "#ffd43b", 7))
    return S


def p04():
    S = Scene()
    vue_fenetre(S, poteaux_vite=True, graine=3)
    cadre_vitre(S)
    S.add(texte(260, 360, "zip !", 64, "#ffd43b", contour=ENCRE, rot=-8), texte(520, 340, "zip !", 64, "#ffd43b", contour=ENCRE, rot=6))
    S.add(fleche(560, 600, 260, 600, "#ffd43b", 9, 26))
    S.add(jade(640, 800, 1.1, expr="bouche_bee", regard=(-1, -1), bras="montre", flip=True))
    return S


def p05():
    S = Scene()
    vue_fenetre(S, poteaux_vite=False, graine=3)
    cadre_vitre(S)
    S.add(fleche(470, 330, 410, 330, "#ffd43b", 6, 18))
    S.add(texte(440, 300, "lentement…", 34, "#fff3bf", contour=ENCRE))
    S.add(texte(560, 270, "?", 70, "#ffd43b", contour=ENCRE))
    S.add(papa(150, 800, 1.1, expr="content", bras="montre", regard=(1, -1)))
    S.add(jade(640, 800, 1.1, expr="surpris", regard=(-1, -1), flip=True))
    return S


def p06():
    S = Scene()
    fond(S, "#0b1433")
    etoiles(S, 70, 6, zone=(0, 0, 800, 800))
    # la Terre en bas à gauche, la Lune en haut à droite
    S.add(cercle(150, 760, 260, "#1971c2"))
    S.add(chemin("M 40 560 Q 120 520 200 560 Q 260 600 320 560 Q 360 540 390 580 L 380 640 Q 300 620 240 650 Q 160 690 60 640 Z", "#2f9e44"))
    S.add(lune_phase(660, 150, 60))
    S.add(voiture(220, 500, 0.32, phares=False))
    S.add(trait(260, 470, 610, 200, "#fff3bf", 5, stroke_dasharray="16 14"))
    S.add(texte(470, 380, "384 000 km", 54, "#ffd43b", contour="#0b1433", rot=-38))
    S.add(texte(600, 320, "très, très loin !", 34, "#fff", rot=-38, contour="#0b1433"))
    S.cachette(670, 730, "air")
    return S


def _vignette_bd(S, x, y, w, h, arbre_dx, num):
    """Petite case : la vitre, un sapin proche à la position arbre_dx, la Lune toujours au même endroit."""
    cid = uid("c")
    m = [el("clipPath", rect(x, y, w, h, "#000", rx=18), id=cid)]
    contenu = [rect(x, y, w, h, "#1c2a52"),
               lune_phase(x + w * 0.78, y + h * 0.25, 22, halo=False),
               chemin(f"M {x} {y + h * 0.72} Q {x + w * 0.3} {y + h * 0.45} {x + w * 0.6} {y + h * 0.7} Q {x + w * 0.8} {y + h * 0.55} {x + w} {y + h * 0.7} L {x + w} {y + h} L {x} {y + h} Z", "#364fc7"),
               rect(x, y + h * 0.78, w, h * 0.22, "#2b8a3e"),
               sapin_nuit(x + arbre_dx, y + h * 0.95, 0.75)]
    m.append(g(contenu, clip_path=f"url(#{cid})"))
    m.append(rect(x, y, w, h, "none", rx=18, stroke="#495057", stroke_width=10))
    m.append(cercle(x + 30, y + 30, 22, "#fff", stroke=ENCRE, stroke_width=3))
    m.append(texte(x + 30, y + 41, str(num), 30))
    S.add(g(m))


def p07():
    S = Scene()
    fond(S, "#fff4e6")
    w, h = 230, 300
    for k, dx in enumerate((190, 115, 40)):
        _vignette_bd(S, 30 + k * 252, 120, w, h, dx, k + 1)
    S.add(fleche(270, 560, 530, 560, "#e8590c", 8, 24))
    S.add(texte(400, 620, "La voiture avance…", 40, "#e8590c"))
    S.add(texte(400, 680, "le sapin file, la Lune reste !", 40, "#1c2a52"))
    S.add(texte(400, 80, "Par la vitre de Jade", 38, "#495057", poids=600))
    S.cachette(400, 730, "air")
    return S


def p08():
    S = Scene()
    nuit(S, *CIEL)
    etoiles(S, 40, 8, zone=(0, 0, 800, 420))
    S.add(lune_phase(400, 140, 62))
    collines(S, 470, "#364fc7", graine=9, hauteur=120)
    S.add(rect(0, 440, 800, 360, "#2b8a3e"))
    S.add(rect(0, 520, 800, 50, "#495057"), rect(0, 700, 800, 56, "#495057"))
    garcon = lambda x, y, s, **k: personne(x, y, s, peau="foncee", cheveux="noir", coiffure="boucles", habit="#ffd43b", robe=False, **k)
    S.add(voiture(200, 562, 0.8, couleur="#1971c2", enfant=garcon, regard=(1, -1), expr="rire"))
    S.add(voiture(560, 745, 0.95, flip=True, regard=(1, -1), expr="rire"))
    S.add(bulle(150, 300, 280, 70, "Elle me suit !", 34, pointe=(190, 450)))
    S.add(bulle(500, 420, 280, 70, "Non, moi !", 34, pointe=(560, 620)))
    return S


def p09():
    S = Scene()
    nuit(S, *CIEL)
    etoiles(S, 40, 10, zone=(0, 0, 800, 420))
    S.add(lune_phase(600, 170, 55))
    S.add(rect(0, 560, 800, 240, "#2b8a3e"))
    S.add(maison(140, 570, 1.0, "#ffe8cc", "#c92a2a", lumiere=True))
    S.add(arbre(720, 600, 0.8, "#2f9e44", "#2b8a3e", "#5c3a1e"))
    S.add(jade(400, 760, 1.5, expr="concentre", bras="montre", regard=(1, -1)))
    # le pouce levé, qui « saute » quand on ferme un œil puis l'autre
    px, py = 400 + 86 * 1.5, 760 - 130 * 1.5
    S.add(rect(px - 6, py - 38, 13, 30, "#dca36f", rx=6))
    S.add(rect(px - 6 - 40, py - 38, 13, 30, "#dca36f", rx=6, opacity=0.35))
    S.add(texte(px - 20, py - 60, "hop !", 34, "#ffd43b", contour=ENCRE))
    return S


def p10():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    S.add(fenetre(470, 120, 230, 210, "#1c2a52", "#e5dbff",
                  contenu=g([lune_phase(620, 180, 40), cercle(500, 160, 2.5, "#fff"), cercle(540, 290, 2, "#fff")])))
    S.add(lit(330, 760, 460, "#e5dbff", "#7048e8"))
    cid = uid("c")
    S.add(el("clipPath", rect(0, 0, 800, 690, "#000"), id=cid))
    S.add(g(jade(215, 742, 0.9, expr="dort"), clip_path=f"url(#{cid})"))
    S.add(rect(150, 652, 410, 70, "#7048e8", rx=18))
    S.add(g([etoile5(240 + k * 70, 686, 9, "#fff3bf") for k in range(5)]))
    S.add(zzz(330, 480, 1.1, "#e5dbff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("jade-seule.svg", vignette),
    ("01-en-route.svg", p01), ("02-elle-me-suit.svg", p02), ("03-le-virage.svg", p03),
    ("04-les-poteaux.svg", p04), ("05-les-collines.svg", p05), ("06-tres-loin.svg", p06),
    ("07-par-la-vitre.svg", p07), ("08-les-autres-enfants.svg", p08), ("09-le-pouce.svg", p09),
    ("10-bonne-nuit.svg", p10),
]
