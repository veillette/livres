"""Le temps des sucres — à la cabane à sucre avec Grand-papa.

Au printemps, quand il gèle la nuit et dégèle le jour, l'eau d'érable coule.
Grand-papa entaille les érables, pose le chalumeau et la chaudière ; plic,
ploc, l'eau tombe, à peine sucrée. On la ramasse en traîneau, on la fait
bouillir dans l'évaporateur de la cabane (il faut environ 40 litres d'eau
d'érable pour un litre de sirop). Le sirop doré, puis la tire sur la neige,
roulée sur un bâton. Le soir, repas, violon et danse.

Plans : 1 large (l'érablière au printemps) · 2 moyen (l'entaille) · 3 gros
plan (plic, ploc) · 4 large (le traîneau) · 5 moyen (la cabane qui fume) ·
6 moyen (l'évaporateur) · 7 gros plan (le sirop doré) · 8 large (la tire
sur la neige) · 9 gros plan (miam !) · 10 large (la fête) · 11 large (au
coucher du soleil).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from fetes import pile_crepes
from fables import violon, archet

ID = "temps-sucres"
PAPIER_PEINT = "losanges"


def tuque(c="#1c7ed6", pompon="#fff"):
    """Tuque à pompon (coiffe d'un personnage)."""
    return g([chemin("M -56 -158 Q -58 -226 0 -228 Q 58 -226 56 -158 Z", c),
              rect(-60, -172, 120, 22, _assombrir(c, 0.8), rx=10),
              chemin("M -40 -190 l 10 10 l 10 -10 l 10 10 l 10 -10 l 10 10 l 10 -10 l 10 10 l 10 -10", stroke="#fff", sw=3, opacity=0.8),
              cercle(0, -232, 16, pompon)])


def ceinture_flechee():
    """Ceinture fléchée nouée à la taille (tenue)."""
    m = [rect(-40, -64, 80, 16, "#c92a2a", rx=4)]
    for k in range(6):
        x = -36 + k * 14
        m.append(chemin(f"M {x} -64 l 6 8 l -6 8", stroke="#ffd43b", sw=2.5))
        m.append(chemin(f"M {x + 7} -64 l 6 8 l -6 8", stroke="#1c7ed6", sw=2.5))
    m += [chemin("M 28 -50 L 34 -14 M 36 -50 L 44 -16", stroke="#c92a2a", sw=7),
          chemin("M 30 -18 l -2 8 M 36 -16 l 0 8 M 42 -18 l 2 8", stroke="#ffd43b", sw=2)]
    return g(m)


CLARA = dict(peau="claire", cheveux="chatain", coiffure="tresses", habit="#e03131", robe=False, jambes="#364fc7",
             coiffe=tuque("#1c7ed6"), taches=True)
GRAND_PAPA = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", barbe="#e9ecef", habit="#c92a2a",
                  robe=False, jambes="#495057", tenue=ceinture_flechee(), coiffe=tuque("#2f9e44", "#ffd43b"), carrure="ronde", nez="rond")
GRAND_MAMAN = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="chignon", habit="#7048e8", acc=("lunettes",))
ONCLE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#2b8a3e", robe=False, jambes="#5c3a1e",
             barbe="#2b2b3a", tenue=ceinture_flechee())

SIROP = "#e8890c"


def clara(x, y, s=1.2, **k):
    return personne(x, y, s, **{**CLARA, **k})


def grand_papa(x, y, s=1.35, **k):
    return personne(x, y, s, **{**GRAND_PAPA, **k})


def chaudiere(x, y, s=1.0, plic=False):
    """Chaudière de métal accrochée au chalumeau ; (x, y) = le chalumeau, dans l'écorce."""
    m = [trait(0, 0, 22, 4, "#adb5bd", 6), chemin("M 14 4 L 14 14", stroke="#868e96", sw=3),
         chemin("M -16 14 L 46 14 L 40 80 L -10 80 Z", volume("#ced4da", 0.35, 0.75)),
         chemin("M -18 12 L 48 12 L 30 -6 L 0 -6 Z", "#adb5bd"),
         chemin("M -16 30 L 44 30", stroke="#adb5bd", sw=2)]
    if plic:
        m.append(goutte(22, 26, 0.6, "#a5d8ff"))
    return place(m, x, y, s)


def erable_nu(x, y, s=1.0, entaille=False, graine=1):
    """Érable sans feuilles de la fin de l'hiver ; (x, y) = pied. entaille : une chaudière accrochée à 170."""
    r = random.Random(graine)
    m = [ellipse(0, 4, 60, 10, "#a5b4fc", opacity=0.4),
         chemin("M -24 0 Q -20 -200 -12 -420 L 12 -420 Q 20 -200 24 0 Z", cylindre("#6d5d4b", 0.25, 0.75)),
         chemin("M -10 -60 l 4 -30 M 8 -140 l -3 -30 M -6 -230 l 3 -26 M 6 -300 l -3 -24", stroke="#4a3f33", sw=3, opacity=0.6)]
    for k in range(7):
        y0 = -230 - k * 30
        sgn = 1 if k % 2 else -1
        L = r.uniform(80, 150)
        m.append(chemin(f"M 0 {y0} Q {sgn * L * 0.5} {y0 - 30} {sgn * L} {y0 - 80 - r.uniform(0, 40)}", stroke="#6d5d4b", sw=10 - k))
        m.append(chemin(f"M {sgn * L * 0.6} {y0 - 50} l {sgn * 30} -40", stroke="#6d5d4b", sw=4))
    if entaille:
        m.append(chaudiere(10, -170, 1.0))
    return place(m, x, y, s)


def neige_sol(S, y=600, graine=1):
    """Sol enneigé, ombres bleues, quelques traces."""
    S.add(chemin(f"M 0 {y} Q 200 {y - 20} 400 {y} T 800 {y} L 800 800 L 0 800 Z", lineaire([(0, "#ffffff"), (1, "#dbe4ff")])))
    r = random.Random(graine)
    for k in range(10):
        S.add(ellipse(r.uniform(0, 800), r.uniform(y + 40, 790), r.uniform(40, 90), r.uniform(6, 12), "#a5b4fc", opacity=0.25))
    for x in (64, 736, 150, 650):
        S.proposer_cachette(x, y + 40)


def erabliere(S, y=600, graine=1, haut="#74c0fc", bas="#e7f5ff", entailles=True):
    ciel(S, haut, bas)
    S.add(lointain_bois(y, graine))
    neige_sol(S, y, graine)
    for k, x in enumerate((70, 250, 560, 730)):
        S.add(erable_nu(x, y + 10 + (k % 2) * 20, 0.8 + (k % 2) * 0.15, entaille=entailles, graine=graine + k))


def lointain_bois(y, graine=1):
    r = random.Random(graine)
    m = []
    for k in range(40):
        x = r.uniform(0, 800)
        h = r.uniform(80, 160)
        m.append(trait(x, y, x + r.uniform(-4, 4), y - h, "#9aa5b8", 3, opacity=0.6))
    m.append(rect(0, y - 40, 800, 40, lineaire([(0, "#e7f5ff", 0), (1, "#e7f5ff", 0.7)])))
    return g(m)


def cabane(x, y, s=1.0, vapeur=True):
    """Cabane à sucre en planches, avec son lanterneau d'où sort la vapeur ; (x, y) = pied de la façade."""
    m = []
    if vapeur:
        for k, dx in enumerate((-40, 0, 40)):
            m.append(chemin(f"M {dx} -330 q -30 -40 0 -80 q 30 -40 0 -80 q -20 -30 10 -60", stroke="#f8f9fa", sw=26 - k * 4, opacity=0.85))
    m += [rect(-200, -200, 400, 200, volume("#a0693a", 0.25, 0.8)), planches(-200, -200, 400, 200, "#a0693a", larg=28),
          poly([(-230, -196), (0, -300), (230, -196)], volume("#495057", 0.3, 0.8)),
          rect(-60, -350, 120, 60, "#8d5524"), poly([(-80, -346), (0, -380), (80, -346)], "#495057"),
          rect(-50, -340, 100, 30, "#343a40"),
          poly([(-232, -200), (0, -304), (232, -200), (232, -186), (0, -290), (-232, -186)], "#fff"),
          rect(-40, -130, 80, 130, cylindre("#6d4424", 0.25, 0.75), rx=4), cercle(26, -64, 5, "#fcc419"),
          rect(110, -150, 60, 50, "#ffe066", stroke="#6d4424", stroke_width=6), rect(-170, -150, 60, 50, "#ffe066", stroke="#6d4424", stroke_width=6)]
    return place(m, x, y, s)


def evaporateur(x, y, s=1.0):
    """Évaporateur : longue casserole de métal sur un foyer ; le sirop bout."""
    m = [rect(-260, -120, 520, 120, volume("#495057", 0.3, 0.8), rx=6), rect(-220, -80, 80, 50, "#ff922b", rx=6),
         ellipse(-180, -56, 30, 16, "#ffd43b"), rect(-280, -160, 560, 44, volume("#ced4da", 0.35, 0.75), rx=6),
         rect(-270, -156, 540, 20, SIROP, rx=4)]
    for k in range(14):
        m.append(cercle(-250 + k * 38, -150, 6 + (k % 3) * 2, "#fff3bf", opacity=0.8))
    for dx in (-200, -60, 80, 200):
        m.append(chemin(f"M {dx} -170 q -20 -30 0 -60 q 20 -30 0 -60", stroke="#f8f9fa", sw=12, opacity=0.8))
    m.append(rect(220, -400, 40, 240, "#868e96"))
    return place(m, x, y, s)


def auge_tire(x, y, s=1.0, tire=3):
    """Auge en bois pleine de neige, avec des rubans de sirop chaud ; (x, y) = pied."""
    m = [rect(-260, -90, 520, 90, volume("#a0693a", 0.3, 0.8), rx=6), rect(-250, -100, 500, 30, "#fff", rx=10),
         ellipse(-120, -98, 80, 12, "#fff"), ellipse(120, -96, 80, 12, "#fff")]
    for k in range(tire):
        m.append(chemin(f"M {-200 + k * 140} -90 q 20 -8 40 0 t 40 0 t 40 0", stroke=SIROP, sw=10))
    return place(m, x, y, s)


def baton_tire(x, y, s=1.0, rot=0):
    return place([trait(0, 0, 0, -90, "#e9d8a6", 6), ellipse(0, -100, 16, 22, volume(SIROP, 0.45, 0.75))], x, y, s, rot=rot)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    erabliere(S, 600, graine=2)
    S.add(cabane(560, 630, 0.75))
    S.add(grand_papa(200, 790, 1.4, expr="rire", bras="tient", regard=(1, 0), objet=baton_tire(*ancre(68, -146, "tient", "ancien"), 1.0)))
    S.add(clara(440, 790, 1.3, expr="miam", bras="tient", regard=(-1, 0), objet=baton_tire(68, -146, 1.0, rot=10)))
    S.cachette(730, 670, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(baton_tire(160, 240, 1.4, rot=-10), baton_tire(240, 240, 1.4, rot=10))
    S.add(place(chemin("M -30 0 Q -20 -40 0 -60 Q 20 -40 30 0 Q 30 30 0 34 Q -30 30 -30 0 Z", SIROP), 330, 200, 1.0))
    return S


def p01():
    """Plan large : la fin de l'hiver dans l'érablière ; le soleil fait fondre la neige."""
    S = Scene()
    erabliere(S, 600, graine=3, entailles=False)
    S.add(soleil(640, 120, 55))
    for k in range(5):
        S.add(goutte(250 + 4, 420 + k * 30, 0.4, "#a5d8ff"))
    S.add(clara(400, 790, 1.2, expr="joie", bras="ouverts", regard=(0, -0.6)))
    S.add(texte(400, 210, "Le temps des sucres !", 50, SIROP, contour="#fff"))
    S.cachette(140, 70, "air")
    return S


def p02():
    """Plan moyen : Grand-papa fait une petite entaille et accroche la chaudière."""
    S = Scene()
    erabliere(S, 620, graine=4, entailles=False)
    S.add(erable_nu(440, 790, 1.3, entaille=True, graine=7))
    S.add(grand_papa(250, 790, 1.4, expr="concentre", bras="tend", regard=(1, -0.3)))
    S.add(clara(640, 790, 1.15, expr="surpris", bras="joues", regard=(-1, -0.3)))
    S.add(texte(430, 140, "Toc, toc !", 50, "#6d4424", contour="#fff"))
    S.cachette(730, 160, "air")
    return S


def p03():
    """Gros plan : une goutte d'eau d'érable tombe du chalumeau dans la chaudière."""
    S = Scene()
    erabliere(S, 640, graine=5, entailles=False)
    S.add(erable_nu(380, 860, 1.8, graine=8))
    S.add(chaudiere(400, 860 - 170 * 1.8, 1.8, plic=True))
    S.add(clara(640, 900, 1.6, expr="miam", bras="bouche", regard=(-1, -0.3)))
    S.camera(1.4, 470, 520)
    S.dessus(texte(250, 130, "Plic… ploc…", 56, "#1c7ed6", contour="#fff"),
             bulle(560, 420, 380, 90, "À peine sucrée !", 34, pointe=(610, 520)))
    S.cachette(584, 279, "air")
    return S


def traineau_baril(x, y, s=1.0):
    return place([chemin("M -150 0 L 150 0 Q 190 0 190 -30", stroke="#8d5524", sw=10), rect(-140, -30, 260, 20, "#a0693a", rx=4),
                  rect(-100, -150, 180, 120, cylindre("#a0693a", 0.3, 0.75), rx=30), trait(-100, -120, 80, -120, "#495057", 6), trait(-100, -60, 80, -60, "#495057", 6),
                  trait(190, -30, 260, -60, "#495057", 4)], x, y, s)


def p04():
    """Plan large : Grand-papa et Clara ramassent l'eau d'érable avec un traîneau et un baril."""
    S = Scene()
    erabliere(S, 600, graine=6)
    S.add(traineau_baril(330, 760, 0.9))
    S.add(grand_papa(600, 790, 1.15, expr="content", bras="tire", flip=True, regard=(-1, 0)))
    S.add(clara(130, 790, 1.0, expr="rire", bras="porte", regard=(1, 0), objet=chaudiere(-14, -100, 0.7)))
    S.cachette(730, 160, "air")
    return S


def p05():
    """Plan moyen : la cabane à sucre ; la vapeur sort du toit."""
    S = Scene()
    erabliere(S, 620, graine=7, entailles=False)
    S.add(cabane(420, 700, 1.1))
    S.add(clara(130, 790, 1.15, expr="bouche_bee", bras="designe", regard=(1, -0.6)))
    S.add(texte(620, 140, "Pschhh !", 46, "#868e96", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


def cabane_dedans(S, y=600):
    piece(S, "chaumiere", y)
    S.add(fenetre(80, 100, 160, 140, "#a5d8ff", cadre="#8d5524",
                  contenu=g([rect(0, 0, 800, 800, "#e7f5ff"), rect(0, 200, 800, 100, "#fff"), erable_nu(160, 260, 0.3)])))


def p06():
    """Plan moyen : dans la cabane, l'eau d'érable bout dans l'évaporateur."""
    S = Scene()
    cabane_dedans(S)
    S.add(evaporateur(400, 780, 1.1))
    S.lumiere(400 - 180 * 1.1, 780 - 56 * 1.1, 80, "#ff922b", 0.5)
    S.add(grand_papa(650, 790, 1.3, expr="content", bras="designe", flip=True, regard=(-1, 0.2)))
    S.add(bulle(330, 150, 460, 110, "40 litres d'eau d'érable…\npour 1 litre de sirop !", 30, pointe=(600, 420)))
    return S


def bocal_sirop(x, y, s=1.0, plein=1.0):
    m = [rect(-50, -140, 100, 140, "#f1f3f5", rx=10, opacity=0.6, stroke="#adb5bd", stroke_width=3),
         rect(-44, -140 * plein + 6, 88, 134 * plein - 6, volume(SIROP, 0.4, 0.75), rx=8), rect(-40, -160, 80, 22, "#c92a2a", rx=6),
         rect(-34, -100, 68, 40, "#fff", rx=6), texte(0, -74, "sirop", 18, SIROP), ellipse(-26, -110, 6, 20, "#fff", opacity=0.5)]
    return place(m, x, y, s)


def p07():
    """Gros plan : le sirop doré coule dans un pot."""
    S = Scene()
    cabane_dedans(S)
    S.add(table(400, 790, 420, 130, "#c68642"))
    S.add(chemin("M 400 380 Q 404 480 400 540", stroke=SIROP, sw=14))
    S.add(rect(330, 330, 140, 60, "#868e96", rx=10))
    S.add(bocal_sirop(400, 660, 1.0, 0.6))
    S.add(clara(640, 860, 1.6, expr="bouche_bee", bras="joues", regard=(-1, -0.4)))
    S.camera(1.3, 450, 520)
    S.dessus(texte(400, 110, "Du sirop tout doré !", 52, SIROP, contour="#fff"))
    return S


def p08():
    """Plan large : la tire sur la neige ; Grand-papa verse le sirop chaud, les enfants le roulent sur un bâton."""
    S = Scene()
    erabliere(S, 580, graine=9)
    S.add(cabane(650, 600, 0.55))
    S.add(auge_tire(400, 760, 1.0))
    S.add(grand_papa(180, 790, 1.2, expr="content", bras="donne", regard=(1, 0.4),
                     objet=place([rect(-16, -30, 50, 40, "#868e96", rx=6), chemin("M 30 -20 Q 50 10 44 40", stroke=SIROP, sw=6)], *ancre(84, -92, "donne", "ancien"))))
    S.add(clara(450, 690, 0.95, expr="rire", bras="tient", regard=(0, 0.6), objet=baton_tire(68, -146, 1.0, rot=20)))
    S.add(personne(600, 700, 0.9, peau="foncee", cheveux="noir", coiffure="courts", habit="#ffd43b", robe=False, jambes="#2f9e44",
                   coiffe=tuque("#e64980"), expr="miam", bras="tient", regard=(-1, 0.4), objet=baton_tire(68, -146, 1.0)))
    S.add(auge_tire(400, 760, 1.0))
    S.cachette(730, 160, "air")
    return S


def p09():
    """Gros plan : Clara lèche sa tire d'érable : miam !"""
    S = Scene()
    erabliere(S, 620, graine=10)
    S.add(clara(400, 900, 2.2, expr="miam", bras="tient", regard=(0.3, -0.2), objet=baton_tire(68, -146, 1.0, rot=-15)))
    S.camera(1.15, 420, 470)
    S.dessus(texte(620, 130, "Miam !", 70, SIROP, contour="#fff"))
    S.cachette(133, 478, "air")
    return S


def p10():
    """Plan large : la fête dans la cabane : crêpes au sirop, violon et danse."""
    S = Scene()
    cabane_dedans(S)
    S.add(table(220, 790, 340, 140, "#c68642", nappe="#ff8787"))
    S.add(pile_crepes(170, 640, 0.9), bocal_sirop(290, 650, 0.6))
    S.add(personne(470, 790, 1.2, expr="joie", bras="porte", regard=(1, 0),
                   objet=g([place(violon(0, 0, 0.7), -10, -110), place(archet(0, 0, 0.7), 30, -100)]), **ONCLE))
    S.add(grand_papa(620, 790, 1.15, expr="rire", bras="danse", regard=(1, 0)))
    S.add(personne(730, 790, 1.1, expr="rire", bras="danse", flip=True, regard=(-1, 0), **GRAND_MAMAN))
    S.add(clara(100, 790, 1.0, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(notes(470, 380, 1.0, "#c92a2a"), notes(560, 320, 0.8, "#c92a2a"))
    S.add(texte(500, 160, "Swing la bacaisse !", 44, "#c92a2a", contour="#fff"))
    return S


def p11():
    """Plan large : au coucher du soleil, Clara et Grand-papa repartent dans l'érablière."""
    S = Scene()
    erabliere(S, 600, graine=11, haut="#f76707", bas="#ffd8a8")
    S.add(soleil(400, 560, 60))
    S.add(cabane(620, 620, 0.55, vapeur=True))
    S.add(grand_papa(280, 790, 1.25, expr="content", bras="main", regard=(1, 0)))
    S.add(clara(400, 790, 1.05, expr="content", bras="main", flip=True, regard=(-1, -0.4)))
    S.add(texte(400, 150, "À l'année prochaine, les érables !", 34, "#fff3bf", contour="#c92a2a"))
    S.lumiere(620 + 140 * 0.55, 620 - 125 * 0.55, 60, "#ffd43b", 0.6)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tire-seule.svg", vignette),
    ("01-le-printemps.svg", p01), ("02-l-entaille.svg", p02), ("03-plic-ploc.svg", p03),
    ("04-le-traineau.svg", p04), ("05-la-cabane.svg", p05), ("06-l-evaporateur.svg", p06),
    ("07-le-sirop.svg", p07), ("08-la-tire.svg", p08), ("09-miam.svg", p09),
    ("10-la-fete.svg", p10), ("11-a-l-annee-prochaine.svg", p11),
]
