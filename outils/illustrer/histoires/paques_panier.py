"""Le panier de Pâques — la chasse aux œufs, et le plaisir de faire trouver.

Le matin de Pâques, les cloches sont revenues de leur grand voyage et ont
semé des œufs dans le jardin de Mamie Jo. Nino en trouve un, deux, trois…
Sa petite sœur Rose, elle, ne trouve rien. Au lieu de lui donner ses œufs,
Nino l'aide à les trouver toute seule (« tu chauffes ! »). Tout en haut du
cerisier, le gros œuf en chocolat les attend… et Papi soulève Rose.

Plans : 1 large (le clocher) · 2 moyen (le départ) · 3 gros plan
(tulipes) · 4 large (le jardin) · 5 moyen (Rose et l'escargot) · 6 gros
plan (la larme) · 7 moyen (« tu chauffes ») · 8 large (« tu brûles ! ») ·
9 contre-plongée (le cerisier) · 10 moyen (sur les épaules) · 11 gros plan
(l'œuf ouvert) · 12 large (Joyeuses Pâques).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from contes import bottes
from fetes import oeuf_decore, gros_oeuf_chocolat, cloche, panier_osier

ID = "paques-panier"
PAPIER_PEINT = "fleurs"

NINO = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7")
ROSE = dict(peau="brune", cheveux="noir", coiffure="couettes", habit="#f783ac", stature="petit", nez="retrousse")
MAMIE = dict(peau="brune", cheveux="blanc", coiffure="chignon", habit="#7b2cbf", stature="ancien", carrure="ronde",
             acc=("lunettes",))
PAPI = dict(peau="foncee", cheveux="gris", coiffure="chauve_cote", habit="#2f9e44", robe=False, jambes="#5c3d2e",
            stature="adulte", carrure="ronde", nez="rond", barbe="#adb5bd")
OEUFS = ("#ff6b6b", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8", "#ff922b")


def nino(x, y, s=1.3, **k):
    return personne(x, y, s, **{**NINO, **k})


def rose(x, y, s=1.3, **k):
    return personne(x, y, s, **{**ROSE, **k})


def mamie(x, y, s=1.3, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def papi(x, y, s=1.3, **k):
    return personne(x, y, s, **{**PAPI, **k})


def tulipe(x, y, s=1.0, couleur="#fa5252", tige=90):
    m = [trait(0, 0, 0, -tige, "#2f9e44", 6),
         chemin(f"M 0 -10 Q -30 {-tige * 0.4} -12 {-tige * 0.7} Q -6 {-tige * 0.35} 0 -10 Z", "#40c057"),
         chemin(f"M -18 {-tige} Q -20 {-tige - 34} -10 {-tige - 40} L -4 {-tige - 26} L 0 {-tige - 42} L 4 {-tige - 26} "
                f"L 10 {-tige - 40} Q 20 {-tige - 34} 18 {-tige} Q 0 {-tige + 12} -18 {-tige} Z", volume(couleur, 0.35, 0.75))]
    return place(m, x, y, s)


def massif(x, y, s=1.0, graine=1, cols=("#fa5252", "#ffd43b", "#f783ac", "#cc5de8")):
    import random
    r = random.Random(graine)
    return g([tulipe(x + (k - 3) * 26 * s + r.uniform(-6, 6), y + r.uniform(-6, 6), s * r.uniform(0.85, 1.1),
                     cols[k % len(cols)], tige=r.uniform(70, 100)) for k in range(7)])


def arrosoir(x, y, s=1.0, couleur="#1c7ed6"):
    m = [chemin("M 50 -60 L 120 -110 L 128 -100 L 60 -40 Z", couleur),
         rect(110, -122, 26, 18, _assombrir(couleur, 0.8), rx=4, transform="rotate(-35 123 -113)"),
         rect(-60, -100, 120, 100, cylindre(couleur, 0.3, 0.7), rx=10),
         chemin("M -40 -100 Q 0 -150 40 -100", stroke=_assombrir(couleur, 0.8), sw=10),
         ellipse(0, -100, 60, 12, _assombrir(couleur, 0.6))]
    return place(m, x, y, s)


def brouette(x, y, s=1.0, couleur="#2f9e44"):
    m = [trait(-130, -70, -200, -40, "#8d5524", 10), trait(-120, -40, -150, 0, "#868e96", 8),
         cercle(90, -30, 32, "#343a40"), cercle(90, -30, 12, "#adb5bd"),
         chemin("M -140 -110 L 140 -110 L 100 -40 L -110 -40 Z", volume(couleur, 0.3, 0.75)),
         rect(-146, -118, 292, 14, _assombrir(couleur, 0.8), rx=5)]
    return place(m, x, y, s)


def clocher(x, y, s=1.0, sonne=True):
    """Clocher du village, la cloche qui se balance ; (x, y) = pied."""
    m = [rect(-70, -330, 140, 330, "#e9dcc9"), pierres(-70, -330, 140, 330, "#e9dcc9", pas_=24, larg=40, opacite=0.35),
         poly([(-86, -330), (0, -470), (86, -330)], volume("#5c677d", 0.3, 0.7)),
         trait(0, -470, 0, -520, "#495057", 5), trait(-16, -500, 16, -500, "#495057", 5),
         chemin("M -38 -200 L -38 -270 Q 0 -310 38 -270 L 38 -200 Z", "#343a40"),
         place(cloche(0, 0, 1.0, "#fcc419", ailes=False, ruban="#343a40"), 0, -245, 0.7, rot=18 if sonne else 0),
         rect(-80, -205, 160, 12, "#ced4da")]
    return place(m, x, y, s)


def jardin(S, sol_y=640, horizon=560, graine=2, cerisier=True, clocher_=True):
    """Le jardin de Mamie Jo, un matin de printemps."""
    ciel(S, "#74c0fc", "#fff9db")
    S.add(nuage(160, 130, 0.7), nuage(620, 90, 0.55))
    collines(S, horizon, "#b2f2bb", graine=graine)
    if clocher_:
        S.add(clocher(690, horizon + 6, 0.42))
    sol(S, sol_y, "#8ce99a")


def cerisier(x, y, s=1.0):
    return arbre(x, y, s, feuillage="#ffdeeb", feuillage2="#fcc2d7", tronc="#8d5524", fruits=None)


def sonne(x, y, taille=40, rot=-8):
    return texte(x, y, "Ding, dang, dong !", taille, "#f08c00", contour="#fff", rot=rot)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S)
    S.add(cerisier(130, 650, 1.1))
    S.add(cloche(560, 170, 0.9, rot=-12), cloche(700, 250, 0.6, "#ff922b", rot=10))
    for k, (x, y) in enumerate(((600, 260), (650, 330), (520, 320))):
        S.add(oeuf_decore(x, y, 0.8, OEUFS[k], rot=k * 20 - 20))
    S.add(massif(700, 700, 0.9, graine=4))
    S.add(nino(300, 770, 1.5, expr="rire", bras="porte", regard=(1, 0),
               objet=panier_osier(0, -48, 0.85, oeufs=OEUFS[:4])))
    S.add(rose(500, 775, 1.45, expr="joie", bras="haut", regard=(-1, 0),
               objet=oeuf_decore(0, -175, 1.1, "#ffd43b", "pois")))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(panier_osier(200, 255, 1.4, oeufs=OEUFS[:4]))
    S.add(cloche(330, 70, 0.6, rot=12))
    return S


def p01():
    """Plan large : le clocher sonne, les cloches reviennent de voyage."""
    S = Scene()
    jardin(S, clocher_=False)
    S.add(clocher(560, 566, 0.9))
    S.add(cloche(250, 140, 0.8, rot=-15), cloche(380, 220, 0.55, "#ff922b", rot=10), cloche(120, 260, 0.5, "#e599f7", rot=-5))
    S.add(oeuf_decore(300, 300, 0.6, "#ff6b6b", rot=30), oeuf_decore(170, 340, 0.55, "#4dabf7", "pois", rot=-20))
    S.add(sonne(560, 70))
    S.add(maison(160, 660, 0.9, mur="#fff4e6", toit="#c92a2a", volets="#4dabf7", cheminee=False))
    S.add(mamie(330, 760, 1.15, expr="content", bras="designe", regard=(-1, -1), flip=True))
    S.add(nino(470, 770, 1.15, expr="bouche_bee", bras="saute", regard=(-1, -1)))
    S.add(massif(690, 720, 0.8, graine=1))
    return S


def p02():
    """Plan moyen : les paniers vides, et le signal du départ."""
    S = Scene()
    jardin(S)
    S.add(cerisier(680, 650, 1.0))
    S.add(mamie(560, 760, 1.45, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(nino(200, 770, 1.4, expr="concentre", bras="porte", regard=(1, 0), pas="marche",
               objet=panier_osier(0, -48, 0.8)))
    S.add(rose(370, 775, 1.35, expr="joie", bras="porte", regard=(1, 0),
               objet=panier_osier(0, -48, 0.65, couleur="#f08c00")))
    S.add(bulle(560, 130, 380, 100, "Trois, deux, un…\ncherchez !", 36, pointe=(560, 330)))
    return S


def p03():
    """Gros plan : un œuf rouge caché dans les tulipes."""
    S = Scene()
    jardin(S, clocher_=False)
    S.add(nino(560, 760, 1.4, expr="bouche_bee", bras="ramasse", regard=(-1, 1), flip=True))
    S.add(massif(330, 690, 1.25, graine=3, cols=("#ffd43b", "#f783ac", "#cc5de8", "#ffa94d")))
    S.add(oeuf_decore(380, 720, 1.5, "#fa5252", "zigzag", rot=-10))
    S.camera(1.55, 420, 560)
    S.dessus(texte(200, 120, "Un !", 90, "#fa5252", contour="#fff", rot=-10))
    return S


def p04():
    """Plan large : deux œufs dans l'arrosoir, trois sous la brouette."""
    S = Scene()
    jardin(S)
    S.add(arrosoir(150, 690, 0.95))
    S.add(oeuf_decore(130, 600, 0.75, "#ffd43b", "pois", rot=-20), oeuf_decore(170, 596, 0.75, "#69db7c", "rayures", rot=15))
    S.add(brouette(620, 700, 1.0))
    for k, c in enumerate(("#4dabf7", "#cc5de8", "#ff922b")):
        S.add(oeuf_decore(560 + k * 50, 700, 0.75, c, ("zigzag", "coeur", "pois")[k]))
    S.add(nino(390, 760, 1.25, expr="rire", bras="court", regard=(1, 0), pas="court",
               objet=place(panier_osier(0, 0, 0.6, oeufs=("#fa5252", "#ffd43b", "#69db7c")), 30, -40)))
    S.add(texte(150, 470, "Deux !", 60, "#f08c00", contour="#fff", rot=-8))
    S.add(texte(620, 470, "Trois !", 64, "#7048e8", contour="#fff", rot=6))
    S.cachette(760, 780)
    return S


def p05():
    """Plan moyen : Rose ne trouve qu'un escargot ; son panier est vide."""
    S = Scene()
    jardin(S)
    S.add(buisson(140, 660, 1.2, baies=None))
    S.add(rose(380, 770, 1.55, expr="inquiet", bras="porte", regard=(1, 1),
               objet=panier_osier(0, -48, 0.7, couleur="#f08c00")))
    S.add(escargot(560, 740, 0.9, expr="surpris", flip=True, regard=(-1, 0)))
    for x, y in ((630, 760), (660, 748), (600, 770)):
        S.add(caillou(x, y, 0.35))
    S.add(texte(560, 600, "?", 70, "#495057"))
    return S


def p06():
    """Gros plan : Rose pleure ; Nino regarde son panier plein, puis sa sœur."""
    S = Scene()
    jardin(S, clocher_=False)
    S.add(rose(270, 790, 1.7, expr="pleure", larmes=True, bras="porte", regard=(1, 0),
               objet=panier_osier(0, -48, 0.7, couleur="#f08c00")))
    S.add(nino(560, 790, 1.7, expr="inquiet", bras="porte", regard=(-1, 0),
               objet=panier_osier(0, -48, 0.8, oeufs=OEUFS[:5])))
    S.camera(1.2, 420, 480)
    S.cachette(130, 760)
    return S


def p07():
    """Plan moyen : « Tu chauffes ! » — Nino guide Rose vers la botte de Papi."""
    S = Scene()
    jardin(S)
    S.add(maison(130, 650, 1.1, mur="#fff4e6", toit="#c92a2a", volets="#4dabf7", cheminee=False))
    S.add(bottes(300, 710, 0.95, "#2f9e44"))
    S.add(oeuf_decore(262, 607, 0.8, "#ffd43b", "coeur", rot=-12))
    S.add(rose(440, 775, 1.3, expr="concentre", bras="tend", flip=True, regard=(-1, 0.4), pas="marche",
               objet=None))
    S.add(nino(680, 770, 1.4, expr="malin", bras="designe", flip=True, regard=(-1, 0)))
    S.add(bulle(620, 170, 300, 90, "Tu chauffes !", 38, pointe=(670, 400)))
    return S


def p08():
    """Plan large : Rose trouve, trouve encore ! « Tu brûles ! »"""
    S = Scene()
    jardin(S)
    S.add(cerisier(690, 640, 0.95))
    S.add(buisson(110, 660, 1.0))
    S.add(oeuf_decore(80, 690, 0.65, "#69db7c", "zigzag"), oeuf_decore(500, 640, 0.6, "#ff922b", "pois"))
    S.add(rose(300, 770, 1.35, expr="rire", bras="saute", regard=(1, 0),
               objet=place(oeuf_decore(0, 0, 0.9, "#cc5de8", "rayures"), 90, -175)))
    S.add(nino(560, 770, 1.3, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(panier_osier(390, 790, 0.7, oeufs=("#ffd43b", "#4dabf7"), couleur="#f08c00"))
    S.add(bulle(560, 140, 300, 90, "Tu brûles !", 40, pointe=(560, 400)))
    return S


def p09():
    """Contre-plongée : tout en haut du cerisier, le gros œuf en chocolat."""
    S = Scene()
    ciel(S, "#4dabf7", "#d0ebff")
    S.add(nuage(650, 140, 0.8), nuage(150, 200, 0.6))
    S.add(cerisier(400, 980, 3.3))
    S.add(gros_oeuf_chocolat(470, 290, 0.75))
    S.add(chemin("M 0 800 L 0 730 Q 400 700 800 730 L 800 800 Z", terrain("#8ce99a")))
    S.add(nino(240, 790, 0.9, expr="bouche_bee", bras="designe", regard=(1, -1)))
    S.add(rose(600, 795, 0.85, expr="surpris", bras="etire", regard=(-1, -1)))
    S.cachette(740, 770)
    return S


def p10():
    """Plan moyen : Papi soulève Rose, qui attrape l'œuf."""
    S = Scene()
    jardin(S)
    S.add(cerisier(360, 760, 2.3))
    S.add(gros_oeuf_chocolat(450, 300, 0.6))
    S.add(rose(470, 470, 1.15, expr="joie", bras="haut", regard=(-1, -1)))
    S.add(papi(470, 790, 1.45, expr="rire", bras="tete", regard=(0, -1)))
    S.add(nino(680, 780, 1.25, expr="rire", bras="porte", regard=(-1, -1),
               objet=panier_osier(0, -48, 0.75, oeufs=OEUFS[:5])))
    S.add(mamie(160, 780, 1.25, expr="content", bras="mains_jointes", regard=(1, -1)))
    S.cachette(70, 430, "air")
    return S


def p11():
    """Gros plan : crac ! l'œuf s'ouvre sur la table, plein de petites surprises."""
    S = Scene()
    piece(S, "cuisine", 520)
    S.add(rose(160, 760, 1.4, expr="miam", bras="porte", regard=(1, 1)))
    S.add(nino(650, 760, 1.4, expr="rire", bras="tend", flip=True, regard=(-1, 1)))
    S.add(table(400, 820, 760, 160, "#c68642", nappe="#fff3bf"))
    S.add(gros_oeuf_chocolat(360, 670, 1.5, ouvert=True))
    S.add(texte(400, 330, "Crac !", 80, "#8d5524", contour="#fff", rot=-8))
    S.camera(1.15, 400, 520)
    S.cachette(183, 165, "air")
    return S


def p12():
    """Plan large : toute la famille, les paniers pleins. Joyeuses Pâques !"""
    S = Scene()
    jardin(S)
    S.add(cerisier(110, 650, 1.0))
    S.add(cloche(470, 150, 0.6, rot=-10), cloche(620, 110, 0.45, "#ff922b", rot=10))
    S.add(sonne(300, 90, 34))
    S.add(mamie(240, 760, 1.25, expr="rire", bras="epaule", regard=(1, 0)))
    S.add(nino(370, 775, 1.2, expr="rire", bras="porte", regard=(1, 0), objet=panier_osier(0, -48, 0.75, oeufs=OEUFS[:4])))
    S.add(rose(500, 780, 1.15, expr="miam", bras="porte", regard=(-1, 0),
               objet=panier_osier(0, -48, 0.65, oeufs=OEUFS[2:6], couleur="#f08c00")))
    S.add(papi(640, 770, 1.25, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(massif(720, 760, 0.7, graine=6))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("panier-seul.svg", vignette),
    ("01-les-cloches.svg", p01), ("02-cherchez.svg", p02), ("03-un-oeuf-rouge.svg", p03),
    ("04-deux-trois.svg", p04), ("05-panier-vide.svg", p05), ("06-une-larme.svg", p06),
    ("07-tu-chauffes.svg", p07), ("08-tu-brules.svg", p08), ("09-dans-le-cerisier.svg", p09),
    ("10-sur-les-epaules.svg", p10), ("11-crac.svg", p11), ("12-joyeuses-paques.svg", p12),
]
