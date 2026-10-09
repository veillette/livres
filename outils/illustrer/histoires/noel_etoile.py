"""L'étoile de Noël — une quête dans la neige, et la lumière qu'on partage.

Le soir de Noël, l'étoile du sapin a disparu. Lila la souris et son petit
frère Malo partent chercher la plus brillante du ciel, en haut de la
colline. En chemin, ils emmènent Madame Hérisson, toute seule, et poussent
le traîneau de Papi Ours. Là-haut, l'étoile est toujours aussi loin… mais
en bas, tout le village monte avec ses lanternes. L'étoile du sapin, on la
fabrique ensemble.

Plans : 1 large (salon) · 2 gros plan (carton vide) · 3 moyen (fenêtre) ·
4 large (chemin) · 5 moyen (Madame Hérisson) · 6 moyen en diagonale
(traîneau) · 7 large, ciel immense · 8 gros plan (larme) · 9 large en
plongée (lanternes) · 10 moyen (atelier) · 11 gros plan (l'étoile posée) ·
12 large (la fête).
"""
from base import *
from fables import cheminee
from objets import carton, tasse
from fetes import (lanterne, guirlande_lumineuse, boule_noel, sapin_decore, etoile_papier,
                   grande_etoile, cadeau, traineau, traces_neige)

ID = "noel-etoile"
PAPIER_PEINT = "etoiles"

LILA = dict(habit="#e03131", acc=("echarpe",), couleur_acc="#ffd43b")
MALO = dict(couleur="#dee2e6", habit="#4dabf7", acc=("bonnet", "echarpe"), couleur_acc="#fab005")
MAMAN = dict(couleur="#b8c0c8", habit="#9775fa", acc=("tablier",))
HERISSON = dict(habit="#ae3ec9", acc=("lunettes", "echarpe"), couleur_acc="#f783ac")
PAPI = dict(couleur="#8f5f3a", habit="#2f9e44", acc=("bonnet", "echarpe"), couleur_acc="#e03131")
NEIGE = "#f1f3f5"
ETOILE = (560, 120)          # la grande étoile, au même endroit du ciel


def lila(x, y, s=1.25, **k):
    return perso("souris", x, y, s, **{**LILA, **k})


def malo(x, y, s=0.95, **k):
    return perso("souris", x, y, s, **{**MALO, **k})


def maman(x, y, s=1.6, **k):
    return perso("souris", x, y, s, **{**MAMAN, **k})


def herisson(x, y, s=1.25, **k):
    return perso("herisson", x, y, s, **{**HERISSON, **k})


def papi(x, y, s=1.75, **k):
    return perso("ours", x, y, s, **{**PAPI, **k})


def voisin(espece, x, y, s, habit, **k):
    return perso(espece, x, y, s, habit=habit, acc=("bonnet",), couleur_acc="#ffd43b", **k)


def porte_lanterne(S, x, y, s, qui, flip=False):
    """Un personnage qui tient une lanterne allumée dans la main droite (ou
    gauche si flip), avec son halo."""
    hx = x + (-68 if flip else 68) * s
    hy = y - 146 * s
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=lanterne(68, -146, 0.9)))
    S.lumiere(hx, hy + 52 * 0.9 * s, 110 * s, "#ffd43b", 0.65)


def salon(S, y=600, fenetre_=True):
    """Le salon de la famille souris, le soir de Noël."""
    piece(S, "chaumiere", y)
    if fenetre_:
        dehors = (rect(0, 0, 800, 800, "#1c2a52") + rect(0, 120 + 470 - 470, 800, 0, "#000")
                  + chemin("M 0 250 Q 150 220 300 250 T 800 250 L 800 800 L 0 800 Z", "#dbe4ff")
                  + grande_etoile(560, 140, 9, halo=False))
        S.add(fenetre(470, 110, 190, 170, "#1c2a52", rideaux="#c92a2a", contenu=dehors))


def ciel_neige(S, horizon=560, sol_y=640, etoile=ETOILE, graine=3, collines_=True):
    """Nuit d'hiver : ciel profond, étoiles, collines enneigées, sol de neige."""
    nuit(S, "#14204a", "#4c5b9a")
    etoiles(S, 46, graine, (0, 0, 800, horizon - 60))
    if etoile:
        S.add(grande_etoile(*etoile, 24))
    if collines_:
        collines(S, horizon, "#c5d0f0", graine=graine, bosquets=False)
    sol(S, sol_y, NEIGE, bosse=14)


def village_loin(S, y, s=0.42, xs=(90, 250, 420, 600, 740)):
    for k, x in enumerate(xs):
        S.add(maison(x, y + (k % 2) * 8, s, mur=("#ffe8cc", "#e7f5ff", "#fff3bf")[k % 3],
                     toit=("#c92a2a", "#1c7ed6", "#5f3dc4")[k % 3], lumiere=True, cheminee=k % 2 == 0))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel_neige(S, 560, 650, etoile=(600, 130))
    flocons(S, 30, 8, (0, 0, 800, 600))
    village_loin(S, 590, 0.38, xs=(80, 230, 690))
    S.add(sapin(130, 700, 0.9, neige=True))
    S.add(sapin(720, 690, 0.75, neige=True))
    S.add(papi(560, 760, 1.6, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(lila(370, 770, 1.45, expr="joie", bras="haut"))
    S.add(etoile_papier(370, 770 - 1.45 * 268, 1.05, rot=-8))
    porte_lanterne(S, 220, 775, 1.1, lambda x, y, s, **k: malo(x, y, s, expr="rire", regard=(1, 0), **k))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(etoile_papier(200, 135, 1.55, rot=-8))
    return S


def p01():
    """Plan large : le salon, le sapin décoré… sans rien au sommet."""
    S = Scene()
    salon(S)
    S.add(cheminee(150, 600, 0.55, feu=True))
    S.lumiere(150, 560, 160, "#ff922b", 0.5)
    S.add(guirlande_lumineuse(10, 70, 790, 70, creux=30, nb=14))
    S.add(tapis(420, 690, 260, 46, "#ffc9c9", "#e03131"))
    S.add(sapin_decore(420, 650, 1.45))
    S.add(texte(420, 205, "?", 70, "#fab005", contour="#fff"))
    S.add(cadeau(330, 690, 0.55, "#4dabf7"), cadeau(520, 700, 0.5, "#69db7c", "#e03131"))
    S.add(lila(640, 770, 1.3, expr="surpris", bras="designe", flip=True, regard=(-1, -0.5)))
    S.add(malo(240, 775, 1.0, expr="sourire", bras="porte", regard=(1, -0.4),
               objet=boule_noel(0, -110, 16, "#fab005")))
    return S


def p02():
    """Gros plan : le carton des décorations, vide."""
    S = Scene()
    salon(S, fenetre_=False)
    S.add(tapis(400, 700, 300, 50, "#ffc9c9", "#e03131"))
    S.add(lila(260, 720, 1.25, expr="surpris", bras="joues", regard=(1, 0.5)))
    S.add(malo(560, 730, 1.0, expr="inquiet", bras="epaules", regard=(-1, 0.5)))
    S.add(carton(410, 715, 0.85, w=210, h=130, couleur="#d9a066"))
    S.add(texte(410, 640, "Noël", 26, "#8d5524"))
    S.add(guirlande_lumineuse(330, 600, 420, 590, creux=8, nb=3, allumee=False))
    S.camera(1.5, 410, 580)
    S.dessus(bulle(400, 95, 480, 90, "Où est notre étoile ?", 40, pointe=S.vers_page(280, 470)))
    S.cachette(190, 400, "air")
    return S


def p03():
    """Plan moyen : à la fenêtre, la plus brillante des étoiles."""
    S = Scene()
    piece(S, "chaumiere", 640)
    dehors = []
    fx, fy, fw, fh = 150, 90, 440, 360
    ciel_f = (rect(0, 0, 800, 800, lineaire([(0, "#14204a"), (1, "#4c5b9a")]))
              + g([cercle(160 + (k * 97) % 420, 110 + (k * 53) % 200, 2.2, "#fff3bf") for k in range(22)])
              + chemin("M 150 380 Q 300 330 420 360 T 600 340 L 600 460 L 150 460 Z", "#c5d0f0")
              + chemin("M 150 420 Q 350 400 600 430 L 600 460 L 150 460 Z", "#f1f3f5")
              + grande_etoile(470, 170, 22))
    S.add(fenetre(fx, fy, fw, fh, "#14204a", rideaux="#c92a2a", contenu=ciel_f))
    S.lumiere(470, 170, 90, "#fff3bf", 0.5)
    S.add(lila(230, 770, 1.3, expr="bouche_bee", bras="designe", regard=(1, -1)))
    S.add(malo(430, 775, 1.05, expr="joie", bras="saute", regard=(-1, -0.6)))
    S.add(maman(650, 790, 1.55, expr="sourire", bras="tend", flip=True, regard=(-1, 0),
                objet=place(_echarpe_pliee(), 40, -94)))
    S.dessus(bulle(120, 470, 210, 100, "Je vais\nla chercher !", 28, pointe=(200, 530)))
    return S


def _echarpe_pliee():
    return g([rect(-34, -12, 68, 22, "#4dabf7", rx=8), rect(-34, 4, 68, 18, "#fab005", rx=8)])


def p04():
    """Plan large : le chemin dans la neige, vers la colline et l'étoile."""
    S = Scene()
    ciel_neige(S, 470, 520, etoile=(610, 110))
    village_loin(S, 520, 0.32, xs=(70, 190, 320))
    # la colline, en diagonale, et le chemin creusé dans la neige
    S.add(chemin("M 0 560 Q 350 520 560 380 Q 640 330 800 320 L 800 800 L 0 800 Z", terrain(NEIGE)))
    S.add(chemin("M 120 800 Q 260 640 420 560 Q 560 470 700 380", stroke="#dbe4ff", sw=46, opacity=0.9))
    S.add(traces_neige([(150 + k * 26, 760 - k * 19 - (k * k) * 0.4) for k in range(14)], 1.1))
    S.add(sapin(720, 360, 0.55, neige=True), sapin(90, 610, 0.7, neige=True), sapin(780, 420, 0.5, neige=True))
    porte_lanterne(S, 470, 590, 0.95, lambda x, y, s, **k: lila(x, y, s, expr="content", bras=k.pop("bras"), regard=(1, -0.5), pas="marche", **k))
    S.add(malo(380, 640, 0.75, expr="sourire", bras="marche", regard=(1, -0.5)))
    S.add(texte(260, 700, "crunch", 34, "#748ffc", rot=-12), texte(560, 640, "crunch", 30, "#748ffc", rot=-12))
    S.cachette(60, 770)
    return S


def p05():
    """Plan moyen : la petite maison noire de Madame Hérisson."""
    S = Scene()
    ciel_neige(S, 520, 620, etoile=(640, 100), collines_=True)
    S.add(maison(250, 640, 1.25, mur="#d0bfff", toit="#5f3dc4", fenetre="#2b2f4a", cheminee=True))
    S.add(herisson(410, 730, 1.15, expr="triste", bras="croises", regard=(1, 0)))
    porte_lanterne(S, 640, 760, 1.15, lambda x, y, s, **k: lila(x, y, s, expr="sourire", regard=(-1, 0), **k), flip=True)
    S.add(malo(530, 770, 0.92, expr="inquiet", bras="bas", regard=(-1, 0)))
    S.add(bulle(560, 150, 380, 110, "Venez avec nous,\nMadame Hérisson !", 32, pointe=(640, 470)))
    return S


def p06():
    """Plan moyen en diagonale : tout le monde pousse le traîneau de Papi Ours."""
    S = Scene()
    nuit(S, "#14204a", "#4c5b9a")
    etoiles(S, 40, 9, (0, 0, 800, 300))
    S.add(grande_etoile(700, 90, 20))
    S.add(chemin("M 0 760 L 800 420 L 800 800 L 0 800 Z", terrain(NEIGE)))
    S.add(sapin(120, 500, 0.6, neige=True), sapin(230, 470, 0.5, neige=True))
    # Papi Ours tire, en haut de la pente ; les autres poussent derrière
    S.add(papi(640, 540, 1.35, expr="concentre", bras="tire", flip=True, regard=(-1, 0), rot=0))
    S.add(place(traineau(0, 0, 1.0), 400, 640, 1.05, rot=-23))
    a = math.radians(-23)
    bx, by = 400 + 1.05 * (160 * math.cos(a) + 34 * math.sin(a)), 640 + 1.05 * (160 * math.sin(a) - 34 * math.cos(a))
    S.add(chemin(f"M {n(bx)} {n(by)} Q {n((bx + 525) / 2)} {n((by + 450) / 2 + 20)} 525 452", stroke="#868e96", sw=5))
    S.add(lila(220, 760, 1.0, expr="concentre", bras="pousse", regard=(1, 0)))
    S.add(herisson(120, 790, 0.95, expr="concentre", bras="pousse", regard=(1, 0)))
    S.add(malo(300, 720, 0.75, expr="joie", bras="pousse", regard=(1, 0)))
    S.add(texte(400, 300, "Ho… hisse !", 60, "#ffd43b", contour="#14204a", rot=-12))
    S.cachette(740, 760)
    return S


def p07():
    """Plan large, ciel immense : en haut de la colline, l'étoile est toujours aussi loin."""
    S = Scene()
    nuit(S, "#0b1433", "#3b4a8a")
    etoiles(S, 70, 11, (0, 0, 800, 600))
    S.add(lune(170, 210, 40))
    S.add(grande_etoile(560, 130, 30))
    S.add(nuage(330, 330, 0.9, "#5c6b9e", opacity=0.6), nuage(640, 380, 0.7, "#5c6b9e", opacity=0.5))
    S.add(chemin("M 0 800 L 0 700 Q 220 610 400 615 Q 600 620 800 700 L 800 800 Z", terrain(NEIGE)))
    S.add(lila(400, 640, 0.8, expr="concentre", bras="etire", regard=(1, -1), pas="pointe"))
    S.add(malo(320, 655, 0.6, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(herisson(220, 690, 0.75, expr="sourire", bras="bas", regard=(1, -1)))
    S.add(papi(560, 680, 1.0, expr="sourire", bras="hanches", regard=(-1, -1)))
    S.lumiere(460, 530, 70, "#ffd43b", 0.4)
    S.cachette(720, 760)
    return S


def p08():
    """Gros plan : la larme de Lila ; Malo tire sa manche et montre la vallée."""
    S = Scene()
    nuit(S, "#0b1433", "#3b4a8a")
    etoiles(S, 50, 12, (0, 0, 800, 500))
    S.add(chemin("M 0 800 L 0 640 Q 400 600 800 640 L 800 800 Z", terrain(NEIGE)))
    S.add(lila(330, 800, 1.7, expr="pleure", larmes=True, bras="bas", regard=(1, 0)))
    S.add(malo(560, 800, 1.25, expr="joie", bras="designe", regard=(-1, 0), flip=True))
    S.camera(1.3, 430, 520)
    S.dessus(bulle(560, 110, 360, 90, "Regarde, en bas !", 38, pointe=S.vers_page(560, 520)))
    S.cachette(720, 770)
    return S


def p09():
    """Plan large en plongée : le village illuminé, et les lanternes qui montent."""
    S = Scene()
    nuit(S, "#14204a", "#3b4a8a")
    etoiles(S, 30, 13, (0, 0, 800, 150))
    # la vallée, vue d'en haut
    S.add(rect(0, 180, 800, 620, lineaire([(0, "#9fa9d8"), (1, "#dbe4ff")])))
    for k, (x, y, s) in enumerate(((120, 330, 0.36), (260, 300, 0.32), (420, 320, 0.36), (580, 290, 0.3),
                                   (700, 330, 0.36), (200, 410, 0.4), (520, 400, 0.4), (360, 430, 0.42))):
        S.add(maison(x, y, s, mur=("#ffe8cc", "#e7f5ff", "#fff3bf")[k % 3], toit=("#c92a2a", "#1c7ed6", "#5f3dc4")[k % 3],
                     lumiere=True, cheminee=k % 2 == 0))
    S.add(sapin(40, 360, 0.35, neige=True), sapin(770, 420, 0.35, neige=True), sapin(640, 440, 0.3, neige=True))
    # le chemin en lacets, et la file de lanternes
    S.add(chemin("M 380 470 Q 640 520 420 590 Q 180 660 420 720 Q 560 760 520 800", stroke="#f8f9fa", sw=40, opacity=0.9))
    for k, (x, y, esp, c) in enumerate(((410, 500, "lapin", "#f08c00"), (520, 540, "renard", "#1c7ed6"), (430, 590, "chat", "#2f9e44"),
                                         (300, 640, "castor", "#e64980"), (330, 700, "ecureuil", "#7048e8"))):
        s = 0.28 + k * 0.05
        porte_lanterne(S, x, y, s, lambda x_, y_, s_, esp=esp, c=c, **kk: voisin(esp, x_, y_, s_, c, regard=(0, -1), **kk))
    # les nôtres, au premier plan sur la crête
    S.add(chemin("M 560 800 Q 660 690 800 670 L 800 800 Z", NEIGE))
    S.add(lila(650, 780, 0.9, expr="bouche_bee", bras="joues", regard=(-1, 0.6)))
    S.add(malo(735, 790, 0.7, expr="rire", bras="saute", regard=(-1, 0.6)))
    S.cachette(150, 760)
    return S


def p10():
    """Plan moyen : l'atelier des étoiles, autour de la table."""
    S = Scene()
    salon(S)
    S.add(guirlande_lumineuse(10, 70, 790, 70, creux=30, nb=14))
    S.add(papi(190, 640, 1.5, expr="concentre", bras="porte", regard=(1, 0.4),
               objet=_ciseaux(0, -80)))
    S.add(herisson(620, 640, 1.2, expr="sourire", bras="tend", flip=True, regard=(-1, 0.4),
                   objet=_bobine(70, -100)))
    S.add(table(400, 700, 520, 120, "#c68642", nappe="#ffe3e3"))
    S.add(etoile_papier(400, 520, 0.85, brille=False))
    for k, (x, c) in enumerate(((235, "#ff6b6b"), (560, "#4dabf7"), (290, "#69db7c"), (515, "#ffd43b"))):
        S.add(rect(x - 22, 548 + (k % 2) * 8, 44, 30, c, rx=3, transform=f"rotate({(-1) ** k * 12} {x} {560})"))
    S.add(tasse(620, 575, 0.9, "#e03131"))
    S.add(lila(260, 790, 1.15, expr="concentre", bras="porte", regard=(1, -0.6),
               objet=rect(-26, -96, 52, 36, "#ffd43b", rx=3)))
    S.add(malo(540, 795, 0.92, expr="rire", bras="applaudit", regard=(-1, -0.6)))
    return S


def _ciseaux(x, y):
    return place([trait(-6, 0, 30, -40, "#adb5bd", 6), trait(6, 0, -30, -40, "#adb5bd", 6),
                  cercle(-12, 12, 10, "none", stroke="#e03131", stroke_width=5), cercle(12, 12, 10, "none", stroke="#e03131", stroke_width=5)], x, y)


def _bobine(x, y):
    return place([rect(-14, -18, 28, 36, "#fcc419", rx=4), rect(-18, -22, 36, 8, "#c68642", rx=3), rect(-18, 14, 36, 8, "#c68642", rx=3),
                  chemin("M 14 0 Q 40 10 30 40", stroke="#fcc419", sw=3)], x, y)


def p11():
    """Gros plan : sur les épaules de Papi Ours, Lila pose l'étoile."""
    S = Scene()
    salon(S)
    S.add(sapin_decore(420, 235 + 282 * 1.8, 1.8, etoile=etoile_papier(0, 0, 0.8, rot=-10)))
    S.add(lila(585, 420, 1.15, expr="joie", bras="tend", flip=True, regard=(-1, -0.6)))
    S.add(papi(590, 800, 2.0, expr="rire", bras="tete", regard=(-1, -0.5)))
    S.camera(1.3, 480, 400)
    S.add(paillettes(560, 240, 0.8))
    S.cachette(205, 600, "air")
    return S


def p12():
    """Plan large : la fête, la petite étoile dedans et la grande dehors."""
    S = Scene()
    piece(S, "chaumiere", 600)
    dehors = (rect(0, 0, 800, 800, "#14204a") + chemin("M 0 230 Q 300 200 800 240 L 800 800 L 0 800 Z", "#dbe4ff")
              + grande_etoile(610, 150, 14))
    S.add(fenetre(520, 90, 200, 170, "#14204a", rideaux="#c92a2a", contenu=dehors))
    S.lumiere(610, 150, 70, "#fff3bf", 0.45)
    S.add(guirlande_lumineuse(10, 60, 790, 60, creux=26, nb=14))
    S.add(sapin_decore(150, 640, 1.35, etoile=etoile_papier(0, 0, 0.5, rot=-10)))
    S.add(cadeau(80, 690, 0.45, "#4dabf7"), cadeau(230, 690, 0.4, "#ffd43b", "#e03131"))
    S.add(papi(360, 700, 1.4, expr="rire", bras="epaule", regard=(1, 0)))
    S.add(herisson(470, 700, 1.0, expr="content", bras="mains_jointes", regard=(-1, 0)))
    S.add(maman(590, 700, 1.35, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(voisin("lapin", 720, 700, 0.95, "#f08c00", expr="rire", bras="saute"))
    S.add(table(470, 800, 560, 150, "#c68642", nappe="#c92a2a"))
    S.add(lila(330, 790, 0.95, expr="rire", bras="haut", regard=(1, 0)))
    S.add(malo(620, 795, 0.75, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(paillettes(150, 300, 0.9))
    S.cachette(775, 780)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("etoile-seule.svg", vignette),
    ("01-le-sapin.svg", p01), ("02-le-carton-vide.svg", p02), ("03-a-la-fenetre.svg", p03),
    ("04-dans-la-neige.svg", p04), ("05-madame-herisson.svg", p05), ("06-le-traineau.svg", p06),
    ("07-trop-loin.svg", p07), ("08-regarde.svg", p08), ("09-les-lanternes.svg", p09),
    ("10-l-atelier.svg", p10), ("11-tout-en-haut.svg", p11), ("12-joyeux-noel.svg", p12),
]
