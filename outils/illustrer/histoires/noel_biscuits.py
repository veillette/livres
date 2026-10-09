"""Des biscuits pour le père Noël — la veille de Noël, avec Papa et le chat.

Le 24 décembre, Inès et Papa font des biscuits : on étale, on découpe des
étoiles et des sapins, on cuit, on décore. Le soir, Inès pose près du sapin
une assiette de biscuits, un verre de lait et une carotte pour chacun des
neuf rennes. Dans la nuit, un bruit la réveille : c'est Caramel, le chat,
qui renifle les biscuits ! En le remontant, elle croit voir passer un
traîneau devant la Lune… Au matin : des miettes, des fanes de carottes et
un petit mot : « Merci pour les biscuits ! »

Plans : 1 moyen (la farine) · 2 gros plan (les emporte-pièces) · 3 moyen
(devant le four) · 4 moyen (décorer) · 5 large (l'assiette près du sapin) ·
6 moyen (au lit) · 7 large (l'escalier dans le noir) · 8 gros plan
(Caramel !) · 9 large (le traîneau devant la Lune) · 10 large (le matin) ·
11 gros plan (le petit mot).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from objets import four, chaussette, lampe_poche, bol, assiette
from contes import carotte
from fetes import sapin_decore, etoile_papier, cadeau, guirlande_lumineuse, grande_etoile

ID = "noel-biscuits"
PAPIER_PEINT = "pois"

INES = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#2b8a3e", acc=("noeud",), couleur_acc="#e03131",
            nez="rond", jambes="#c92a2a")
INES_NUIT = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#ffc9c9", acc=("noeud",), couleur_acc="#e03131",
                 nez="rond", robe=False, jambes="#ffc9c9", motif_robe=None)
PAPA = dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#c92a2a", robe=False, jambes="#364fc7",
            stature="adulte", carrure="ronde", nez="rond")
CARAMEL = dict(couleur="#e8903b", acc=("echarpe",), couleur_acc="#2b8a3e")

PATE = "#d9a066"


def ines(x, y, s=1.2, nuit_=False, **k):
    return personne(x, y, s, **{**(INES_NUIT if nuit_ else INES), **k})


def papa(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PAPA, **k})


def caramel(x, y, s=0.75, **k):
    return perso("chat", x, y, s, **{**CARAMEL, **k})


# --- Objets ----------------------------------------------------------------------

def _forme(forme):
    """Contour d'un biscuit ou d'un emporte-pièce, centré en (0, 0)."""
    if forme == "etoile":
        pts = []
        for k in range(10):
            a = math.radians(-90 + k * 36)
            rr = 34 if k % 2 == 0 else 15
            pts.append((rr * math.cos(a), rr * math.sin(a)))
        return "M " + " L ".join(f"{n(px)} {n(py)}" for px, py in pts) + " Z"
    if forme == "sapin":
        return "M 0 -36 L 18 -10 L 10 -10 L 28 14 L 18 14 L 32 32 L 6 32 L 6 40 L -6 40 L -6 32 L -32 32 L -18 14 L -28 14 L -10 -10 L -18 -10 Z"
    if forme == "bonhomme":
        return ("M 0 -38 Q 14 -38 14 -24 Q 14 -14 8 -12 L 30 -6 Q 36 0 28 4 L 12 2 L 18 32 Q 18 40 10 38 L 0 20 "
                "L -10 38 Q -18 40 -18 32 L -12 2 L -28 4 Q -36 0 -30 -6 L -8 -12 Q -14 -14 -14 -24 Q -14 -38 0 -38 Z")
    # cloche
    return "M -8 -34 Q 0 -40 8 -34 Q 22 -26 22 0 Q 22 18 32 26 L -32 26 Q -22 18 -22 0 Q -22 -26 -8 -34 Z M -6 26 Q 0 36 6 26 Z"


def biscuit(x, y, s=1.0, forme="etoile", glace=None, rot=0, croque=False):
    """Biscuit de Noël, décoré (glace : couleur du glaçage) ; (x, y) = centre."""
    m = [chemin(_forme(forme), volume(PATE, 0.35, 0.72), stroke=_assombrir(PATE, 0.8), sw=2)]
    if glace:
        if forme == "bonhomme":
            m += [cercle(-5, -26, 2.5, "#2b2b3a"), cercle(5, -26, 2.5, "#2b2b3a"), chemin("M -5 -18 Q 0 -14 5 -18", stroke="#fff", sw=2.5),
                  cercle(0, -2, 3, glace), cercle(0, 8, 3, glace), chemin("M -26 -2 l 6 4 M 26 -2 l -6 4", stroke="#fff", sw=2.5)]
        elif forme == "sapin":
            m += [chemin("M -14 -2 Q 0 6 14 -6 M -22 24 Q 0 30 22 20", stroke="#fff", sw=3)]
            m += [cercle(px, py, 3, glace) for px, py in ((-6, -14), (8, 6), (-12, 18), (14, 26))]
        elif forme == "cloche":
            m += [chemin("M -20 6 Q 0 12 20 6", stroke=glace, sw=5), cercle(0, -30, 3, "#fff")]
        else:
            m += [chemin(_forme("etoile"), "none", stroke="#fff", sw=2.5, transform="scale(0.72)"), cercle(0, 0, 5, glace)]
    if croque:
        m.append(cercle(26, -22, 13, "#fff4e6"))
    return place(m, x, y, s, rot=rot)


def emporte_piece(x, y, s=1.0, forme="etoile", rot=0):
    """Emporte-pièce en métal ; (x, y) = centre."""
    return place([chemin(_forme(forme), "none", stroke="#868e96", sw=8), chemin(_forme(forme), "none", stroke="#dee2e6", sw=3)],
                 x, y, s, rot=rot)


def rouleau(x, y, s=1.0, rot=0):
    """Rouleau à pâtisserie ; (x, y) = centre."""
    return place([rect(-90, -16, 180, 32, cylindre("#e8b98a", 0.3, 0.75, vertical=True), rx=14),
                  rect(-140, -8, 52, 16, "#a0693a", rx=8), rect(88, -8, 52, 16, "#a0693a", rx=8)], x, y, s, rot=rot)


def plaque(x, y, s=1.0, biscuits=6, glaces=False):
    """Plaque de cuisson garnie de biscuits ; (x, y) = milieu du bas."""
    formes = ("etoile", "sapin", "bonhomme", "cloche", "etoile", "sapin")
    glacages = ("#e03131", "#2b8a3e", "#e03131", "#fab005", "#4dabf7", "#e03131")
    m = [rect(-130, -14, 260, 14, cylindre("#adb5bd", 0.3, 0.75, vertical=True), rx=4)]
    for k in range(biscuits):
        m.append(biscuit(-95 + (k % 3) * 95, -36 - (k // 3) * 0, 0.7, formes[k], glacages[k] if glaces else None))
    return place(m, x, y, s)


def verre_lait(x, y, s=1.0, plein=True):
    m = [rect(-18, -64, 36, 64, "#e7f5ff", rx=4, opacity=0.7, stroke="#a5d8ff", stroke_width=2)]
    if plein:
        m.append(rect(-15, -50, 30, 47, "#ffffff", rx=3))
    else:
        m.append(rect(-15, -10, 30, 7, "#ffffff", rx=3, opacity=0.8))
    m.append(rect(-12, -58, 6, 50, "#fff", opacity=0.5, rx=3))
    return place(m, x, y, s)


def assiette_biscuits(x, y, s=1.0, vide=False):
    """Assiette du père Noël : biscuits décorés, ou rien que des miettes."""
    m = [ellipse(0, 0, 70, 18, "#e03131"), ellipse(0, -2, 58, 13, "#fff")]
    if vide:
        m += [cercle(px, py, 2.5, PATE) for px, py in ((-20, -2), (6, 2), (22, -4), (-6, -6), (30, 1), (-30, 2))]
    else:
        m += [biscuit(-28, -16, 0.6, "etoile", "#e03131", rot=-10), biscuit(26, -16, 0.6, "sapin", "#2b8a3e", rot=12),
              biscuit(0, -30, 0.6, "bonhomme", "#e03131")]
    return place(m, x, y, s)


def fanes(x, y, s=1.0, rot=0):
    """Ce qui reste d'une carotte croquée : les fanes et un petit bout."""
    return place([chemin("M -10 0 Q 0 16 10 0 Z", "#ff922b"),
                  chemin("M 0 0 Q -20 -40 -14 -50 M 2 0 Q 4 -44 8 -56 M 6 0 Q 24 -36 28 -44", stroke="#40c057", sw=7)], x, y, s, rot=rot)


def gueridon(x, y, s=1.0):
    """Petite table ronde près du sapin ; (x, y) = pied, plateau à y - 150 s."""
    bois = "#8d5524"
    return place([ellipse(0, 0, 60, 8, "#000", opacity=0.12), rect(-8, -150, 16, 150, cylindre(bois, 0.25, 0.72)),
                  ellipse(0, -4, 50, 10, _assombrir(bois, 0.8)),
                  ellipse(0, -150, 120, 22, volume(bois, 0.35, 0.75)), ellipse(0, -156, 116, 18, "#fff4e6")], x, y, s)


def cheminee(x, y, s=1.0, feu="vif", chaussettes=True):
    """Cheminée de pierre et son feu ; (x, y) = milieu du pied. feu : "vif",
    "braises" ou None. La lumière se pose avec S.lumiere(x, y - 70 s)."""
    pierre = "#ced4da"
    m = [rect(-170, -320, 340, 320, pierre), pierres(-170, -320, 340, 320, pierre, pas_=26, larg=52, opacite=0.4),
         rect(-110, -200, 220, 200, "#2b2b3a", rx=6), rect(-110, -200, 220, 30, "#000", opacity=0.3),
         rect(-195, -340, 390, 30, volume("#8d5524", 0.3, 0.75), rx=6)]
    if feu:
        m += [rect(-70, -26, 140, 18, "#6d4424", rx=8), rect(-50, -40, 110, 18, "#8d5524", rx=8, transform="rotate(-8)")]
        if feu == "vif":
            m += [chemin("M -60 -30 Q -70 -90 -30 -130 Q -30 -90 -10 -80 Q -10 -140 20 -170 Q 20 -110 40 -100 Q 50 -130 66 -140 Q 80 -80 60 -30 Z", "#ff922b"),
                  chemin("M -36 -30 Q -40 -70 -14 -96 Q -10 -64 6 -60 Q 10 -100 30 -116 Q 34 -70 46 -30 Z", "#ffd43b")]
        else:
            m += [ellipse(-20, -36, 18, 8, "#ff6b6b", opacity=0.8), ellipse(20, -40, 16, 7, "#ff922b", opacity=0.8)]
    if chaussettes:
        for k, (cx, c) in enumerate(((-120, "#e03131"), (0, "#2b8a3e"), (120, "#e03131"))):
            m.append(trait(cx, -312, cx, -292, "#495057", 2))
            m.append(chaussette(cx, -250, 1.1, c))
    return place(m, x, y, s)


def salon(S, y=620, nuit_=False, feu="vif", sapin_x=640, cadeaux=False):
    """Le salon : sapin décoré, cheminée, fenêtre sur la neige."""
    piece(S, "manoir", y)
    if nuit_:
        S.ambiance("nuit")
    dehors = g([rect(0, 0, 800, 800, "#1c2a52" if nuit_ else "#a5d8ff"), rect(0, 220, 800, 200, "#f1f3f5"),
                sapin(320, 240, 0.3, "#2f9e44", "#37b24d", neige=True), sapin(380, 250, 0.25, "#2f9e44", "#37b24d", neige=True)])
    S.add(fenetre(300, 100, 170, 160, "#a5d8ff", cadre="#fff", rideaux="#2b8a3e", contenu=dehors))
    S.add(cheminee(140, y + 4, 0.8, feu=feu))
    if feu:
        S.lumiere(140, y - 50, 160, "#ff922b", 0.6)
    S.add(guirlande_lumineuse(10, 40, 790, 40, creux=20, nb=14))
    S.add(sapin_decore(sapin_x, y + 70, 1.25, etoile=etoile_papier(0, 0, 0.55, brille=False)))
    if nuit_:
        S.lumiere(sapin_x, y - 140, 200, "#ffe066", 0.4)
    if cadeaux:
        for k, (cx, c, w, h) in enumerate(((sapin_x - 90, "#e03131", 110, 80), (sapin_x + 30, "#4dabf7", 90, 110), (sapin_x + 120, "#fab005", 80, 70))):
            S.add(cadeau(cx, y + 110, 1.0, c, "#fff" if c != "#fab005" else "#e03131", w=w, h=h))


def cuisine(S, y=610):
    piece(S, "cuisine", y)
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 210, 800, 200, "#f8f9fa"),
                sapin(600, 220, 0.35, neige=True), sapin(680, 230, 0.28, neige=True)])
    S.add(fenetre(540, 80, 180, 150, "#d0ebff", cadre="#fff", rideaux="#e03131", contenu=dehors))
    S.add(guirlande_lumineuse(20, 40, 780, 40, creux=16, nb=12))


def chambre(S, y=600, fenetre_=True):
    piece(S, "chambre", y)
    S.ambiance("nuit")
    if not fenetre_:
        return
    dehors = g([rect(0, 0, 800, 800, "#1c2a52"), lune(600, 140, 26, halo=False)])
    S.add(fenetre(520, 90, 180, 170, "#1c2a52", rideaux="#2b8a3e", contenu=dehors))
    flocons(S, 14, 3, (520, 90, 700, 260))
    S.add(lampe(130, y + 10, 0.85, abat="#ffd8a8"))


def silhouettes_traineau(x, y, s=1.0, c="#1b1f3b"):
    """Traîneau et rennes en ombre chinoise, qui volent vers la droite ; (x, y) = traîneau."""
    m = [chemin("M -60 0 Q -64 -30 -40 -34 L 30 -34 Q 40 -20 50 -20 L 50 0 Z", c),
         chemin("M -70 8 L 60 8 Q 78 8 80 -6", stroke=c, sw=4),
         cercle(-10, -48, 16, c), chemin("M -20 -60 Q -10 -80 6 -62 Z", c)]
    for k in range(4):
        rx = 100 + k * 70
        ry = -14 - k * 12
        m += [ellipse(rx, ry, 24, 10, c), trait(rx - 16, ry + 6, rx - 22, ry + 24, c, 3), trait(rx + 14, ry + 6, rx + 22, ry + 22, c, 3),
              trait(rx + 20, ry - 4, rx + 32, ry - 18, c, 4), cercle(rx + 34, ry - 20, 6, c),
              chemin(f"M {rx + 32} {ry - 26} l -4 -12 M {rx + 32} {ry - 30} l 6 -8", stroke=c, sw=2)]
        m.append(trait(rx - 70 + 26, ry + 8, rx - 20, ry, c, 1.5) if k else trait(50, -10, rx - 20, ry, c, 1.5))
    return place(m, x, y, s)


def petit_mot(x, y, s=1.0, rot=0):
    """Le petit mot du père Noël ; (x, y) = centre."""
    m = [rect(-120, -80, 240, 160, "#fff9db", rx=6, stroke="#e03131", stroke_width=4),
         texte(0, -36, "Merci pour", 28, "#c92a2a"), texte(0, -2, "les biscuits !", 28, "#c92a2a"),
         texte(60, 52, "P. N.", 26, "#2b8a3e"), coeur(-70, 46, 0.35, "#e03131")]
    return place(m, x, y, s, rot=rot)


def grelot(x, y, s=1.0):
    """Petit grelot argenté, noué d'un ruban rouge ; (x, y) = centre."""
    return place([cercle(0, 0, 26, volume("#dee2e6", 0.5, 0.65)), chemin("M -14 6 Q 0 14 14 6", stroke="#495057", sw=4),
                  cercle(0, 12, 4, "#495057"), rect(-4, -34, 8, 10, "#adb5bd"),
                  chemin("M 0 -30 Q -24 -46 -30 -30 Q -20 -24 0 -30 Q 24 -46 30 -30 Q 20 -24 0 -30 Z", "#e03131"),
                  ellipse(-8, -8, 7, 10, "#fff", opacity=0.6)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S, nuit_=True, sapin_x=620)
    S.add(gueridon(400, 790, 1.2))
    S.add(assiette_biscuits(380, 610, 1.3), verre_lait(470, 600, 1.1))
    S.add(carotte(300, 612, 0.5, rot=-80))
    S.add(caramel(170, 790, 0.9, expr="malin", bras="bas", regard=(1, -0.3)))
    S.add(ines(560, 790, 1.15, expr="rire", bras="tend", flip=True, regard=(-1, 0.3), objet=biscuit(96, -104, 0.9, "etoile", "#e03131")))
    S.cachette(760, 740)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 140, 120, radial([(0, "#fff3bf", 0.8), (1, "#fff3bf", 0)])))
    S.add(biscuit(120, 150, 1.5, "sapin", "#e03131", rot=-10), biscuit(200, 120, 1.6, "etoile", "#e03131"),
          biscuit(285, 150, 1.5, "bonhomme", "#2b8a3e", rot=10), biscuit(200, 210, 1.2, "cloche", "#fab005"))
    return S


def p01():
    """Plan moyen : « On fait des biscuits pour le père Noël ! »"""
    S = Scene()
    cuisine(S)
    S.add(papa(560, 700, 1.35, expr="rire", bras="porte", regard=(-1, 0.2),
               objet=place([rect(-40, -60, 80, 70, "#fff4e6", rx=8), texte(0, -18, "farine", 18, "#868e96")],
                           *ancre(0, -50, "porte", "adulte", "ronde"))))
    S.add(table(400, 800, 620, 160, "#c68642", nappe=None))
    S.add(bol(340, 640, 0.9, "#e03131", "#f3d9a4"), rouleau(520, 630, 0.6, rot=-6))
    S.add(cercle(560, 632, 3, "#fff"), cercle(580, 626, 2, "#fff"))
    S.add(ines(200, 770, 1.25, expr="rire", bras="saute", regard=(1, -0.3)))
    S.add(bulle(250, 180, 400, 100, "On fait des biscuits\npour le père Noël !", 28, pointe=(220, 420)))
    S.cachette(760, 780)
    return S


def p02():
    """Gros plan : la pâte étalée, les emporte-pièces ; clac, clac !"""
    S = Scene()
    cuisine(S)
    S.add(table(400, 900, 780, 300, "#c68642"))
    S.add(chemin("M 200 690 Q 190 600 310 596 L 610 592 Q 710 596 700 690 Q 610 710 450 710 Q 290 710 200 690 Z", volume("#f3d9a4", 0.3, 0.8)))
    for k, (px, py, f) in enumerate(((420, 640, "etoile"), (520, 660, "sapin"), (620, 640, "bonhomme"))):
        S.add(chemin(_forme(f), "#e9c98a", stroke="#c9a46a", sw=2, transform=f"translate({px} {py}) scale(0.9)"))
    S.add(emporte_piece(560, 780, 1.1, "cloche", rot=12), emporte_piece(660, 760, 1.1, "sapin", rot=-10))
    S.add(rouleau(560, 560, 0.9, rot=-8))
    S.add(ines(200, 930, 1.5, expr="concentre", bras="tient", regard=(1, 0.6),
               objet=emporte_piece(84, -146, 1.2, "etoile")))
    S.camera(1.45, 400, 560)
    S.dessus(texte(400, 120, "Clac, clac !", 60, "#2b8a3e", contour="#fff", rot=-4))
    S.cachette(150, 430, "air")
    return S


def p03():
    """Plan moyen : devant le four ; Inès et Caramel attendent, ça sent bon."""
    S = Scene()
    cuisine(S)
    S.add(four(400, 760, 1.4, gateau_dedans=False))
    S.add(plaque(400, 760 - 80 * 1.4, 0.75))
    S.lumiere(400, 760 - 120 * 1.4, 150, "#ffa94d", 0.45)
    S.add(caramel(620, 790, 0.9, expr="miam", bras="bas", regard=(-1, -0.4)))
    S.add(ines(190, 790, 1.2, expr="content", bras="mains_jointes", regard=(1, -0.2)))
    for k in range(3):
        S.add(chemin(f"M {340 + k * 50} 360 q 14 -24 0 -48 q -14 -24 0 -48", stroke="#adb5bd", sw=5, opacity=0.6))
    S.add(texte(400, 210, "Mmm…", 50, "#e8590c", contour="#fff"))
    return S


def p04():
    """Plan moyen : on décore ; Caramel a du glaçage sur le nez."""
    S = Scene()
    cuisine(S)
    S.add(papa(600, 690, 1.3, expr="sourire", bras="porte", regard=(-1, 0.5),
               objet=place([rect(-10, -40, 20, 50, "#fff", rx=6), poly([(-8, 10), (8, 10), (0, 26)], "#fff")],
                           *ancre(26, -74, "porte", "adulte", "ronde"))))
    S.add(table(400, 800, 640, 160, "#c68642", nappe="#fff4e6"))
    S.add(plaque(400, 640, 1.0, glaces=True))
    S.add(bol(620, 640, 0.5, "#4dabf7", "#ffffff", cuillere=False))
    S.add(ines(210, 760, 1.2, expr="concentre", bras="tient", regard=(1, 0.4),
               objet=place([rect(-6, -40, 12, 44, "#e03131", rx=5), poly([(-5, 4), (5, 4), (0, 16)], "#e03131")], 68, -146, 1.0, rot=-30)))
    S.add(caramel(110, 790, 0.8, expr="miam", bras="joues", regard=(1, 0)))
    S.add(cercle(110, 790 - 125 * 0.8, 6, "#fff"))
    S.add(bulle(400, 180, 440, 100, "Un biscuit pour le père Noël…\net une carotte pour chaque renne !", 24, pointe=(230, 440)))
    return S


def p05():
    """Plan large : le soir, l'assiette près du sapin ; neuf carottes."""
    S = Scene()
    salon(S, nuit_=True)
    S.add(gueridon(380, 800, 1.05))
    S.add(assiette_biscuits(330, 640, 1.1), verre_lait(420, 634, 0.95))
    for k in range(9):
        S.add(carotte(300 + k * 18, 652, 0.32, rot=-80 + (k % 2) * 8))
    for k, c in enumerate(("1", "2", "3", "…", "9")):
        S.add(texte(260 + k * 60, 470 - (k % 2) * 20, c, 40, "#e8590c", contour="#fff"))
    S.add(ines(560, 790, 1.15, expr="content", bras="leve_doigt", regard=(-1, 0.3)))
    S.add(caramel(150, 800, 0.7, expr="sourire", bras="bas", regard=(1, -0.3)))
    S.add(bulle(600, 300, 300, 80, "Neuf carottes !", 32, pointe=(570, 500)))
    S.cachette(760, 730)
    return S


def p06():
    """Plan moyen : Papa borde Inès ; dehors, il neige."""
    S = Scene()
    chambre(S)
    S.add(lit(380, 760, 460, "#e7f5ff", "#2b8a3e"))
    S.add(place(ines(0, 0, 0.9, nuit_=True, expr="sourire", bras="bas"), 360, 625, 1.0, rot=-90))
    S.add(rect(285, 590, 330, 100, lineaire([(0, "#40c057"), (1, "#2b8a3e")]), rx=24))
    S.add(papa(690, 770, 1.25, expr="content", bras="tend", flip=True, regard=(-1, 0.5)))
    S.add(caramel(530, 640, 0.55, expr="dort", bras="bas"))
    S.add(bulle(330, 230, 300, 80, "Bonne nuit, ma puce.", 28, pointe=(660, 480)))
    S.cachette(110, 740)
    return S


def escalier(S, x0=0, y0=780, marches=6, w=330, h=60, pas_=50):
    """Escalier qui monte vers la gauche, vu de face."""
    for k in range(marches):
        y = y0 - k * h
        S.add(rect(x0, y - h, w - k * pas_, h, volume("#8d5524", 0.3, 0.78)))
        S.add(rect(x0, y - h, w - k * pas_, 10, "#a0693a"))
    S.add(trait(w - 10, y0 - 40, w - 10 - (marches - 1) * pas_, y0 - marches * h - 40, "#5c3a1e", 10))


def p07():
    """Plan large : la nuit, Inès descend l'escalier avec sa lampe de poche."""
    S = Scene()
    salon(S, nuit_=True, feu="braises", sapin_x=660)
    S.add(gueridon(470, 800, 1.0))
    S.add(assiette_biscuits(440, 646, 1.0), verre_lait(520, 640, 0.85))
    S.add(rect(0, 0, 800, 800, "#0b1433", opacity=0.45))
    escalier(S, 0, 800, 6, 330, 60, 48)
    S.add(ines(170, 620, 0.95, nuit_=True, expr="inquiet", bras="tient", regard=(1, 0.3),
               objet=lampe_poche(68, -146, 0.8, rot=20, faisceau=240)))
    S.lumiere(320, 560, 120, "#fff3bf", 0.45)
    S.add(texte(560, 260, "Cric… crac…", 48, "#ced4da", rot=-6))
    return S


def p08():
    """Gros plan : dans le rond de la lampe, Caramel renifle les biscuits !"""
    S = Scene()
    salon(S, nuit_=True, feu="braises", sapin_x=700)
    S.add(gueridon(400, 860, 1.4))
    S.add(caramel(400, 652, 1.15, expr="oups", bras="joues", regard=(0, 0)))
    S.add(assiette_biscuits(330, 660, 1.3), verre_lait(500, 656, 1.1))
    S.add(cercle(400, 560, 230, radial([(0, "#fff9db", 0.55), (0.7, "#fff3bf", 0.25), (1, "#fff3bf", 0)])))
    S.lumiere(400, 560, 220, "#fff3bf", 0.5)
    S.camera(1.3, 400, 520)
    S.dessus(bulle(400, 100, 500, 100, "Caramel !\nCe n'est pas pour toi !", 32))
    S.cachette(150, 630, "air")
    return S


def p09():
    """Plan large : un traîneau passe devant la Lune."""
    S = Scene()
    chambre(S, fenetre_=False)
    # grande fenêtre ouverte sur la nuit : la Lune et le traîneau
    ciel_nuit = g([rect(0, 0, 800, 800, lineaire([(0, "#0b1433"), (1, "#364fc7")])),
                   lune(420, 230, 120, halo=False), silhouettes_traineau(300, 250, 0.8),
                   rect(0, 380, 800, 200, "#e7f5ff"), sapin(260, 400, 0.4, neige=True), sapin(580, 410, 0.35, neige=True)])
    S.add(fenetre(180, 70, 440, 360, "#0b1433", cadre="#fff", rideaux="#2b8a3e", contenu=ciel_nuit))
    S.lumiere(420, 230, 220, "#fff3bf", 0.4)
    S.add(ines(400, 790, 1.3, nuit_=True, expr="bouche_bee", bras="porte", regard=(0, -1),
               objet=caramel(0, -20, 0.55, expr="surpris", bras="bas", regard=(0, -1))))
    S.add(texte(680, 520, "Oh !", 50, "#ffd43b", contour="#1c2a52"))
    S.cachette(720, 740)
    return S


def p10():
    """Plan large : au matin, des miettes, des fanes, des cadeaux."""
    S = Scene()
    salon(S, feu=None, cadeaux=True)
    S.add(gueridon(330, 800, 1.05))
    S.add(assiette_biscuits(290, 640, 1.1, vide=True), verre_lait(380, 634, 0.95, plein=False))
    for k in range(4):
        S.add(fanes(230 + k * 40, 652, 0.35, rot=-60 + k * 30))
    S.add(petit_mot(330, 600, 0.3, rot=-8))
    S.add(ines(510, 780, 1.2, expr="bouche_bee", bras="joues", regard=(-1, 0)))
    S.add(papa(700, 760, 1.2, expr="rire", bras="hanches", regard=(-1, 0)))
    S.add(caramel(110, 800, 0.75, expr="sourire", bras="bas", regard=(1, -0.3)))
    S.cachette(230, 730, "air")
    return S


def p11():
    """Gros plan : le petit mot du père Noël et son grelot."""
    S = Scene()
    salon(S, feu=None, cadeaux=True)
    S.add(papa(620, 770, 1.5, expr="rire", bras="mains_jointes", regard=(-1, 0)))
    S.add(caramel(170, 780, 1.0, expr="rire", bras="haut", regard=(1, -0.3)))
    S.add(ines(400, 770, 1.6, expr="rire", bras="porte", regard=(0, -0.3), objet=petit_mot(0, -24, 0.62)))
    S.add(grelot(540, 620, 1.3))
    S.camera(1.12, 400, 490)
    S.dessus(texte(400, 90, "Joyeux Noël !", 64, "#c92a2a", contour="#fff"))
    S.cachette(105, 327, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("biscuits-seuls.svg", vignette),
    ("01-la-farine.svg", p01), ("02-clac-clac.svg", p02), ("03-devant-le-four.svg", p03),
    ("04-on-decore.svg", p04), ("05-neuf-carottes.svg", p05), ("06-bonne-nuit.svg", p06),
    ("07-cric-crac.svg", p07), ("08-caramel.svg", p08), ("09-devant-la-lune.svg", p09),
    ("10-au-matin.svg", p10), ("11-le-petit-mot.svg", p11),
]
