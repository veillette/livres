"""Le voyage du saumon — la vie du saumon atlantique, de la rivière à la mer.

À l'automne, dans le gravier d'une rivière froide et claire, des œufs
orange. Au printemps, les alevins, avec leur réserve sous le ventre (le sac
vitellin), se cachent entre les cailloux. Le tacon, tacheté, vit deux ou
trois ans dans la rivière ; devenu saumoneau, tout argenté, il descend vers
la mer. Il grandit en mer pendant un à trois ans, très loin (jusqu'au
Groenland), puis revient à sa rivière, qu'il reconnaît à l'odeur de son
eau. Il remonte le courant, saute les chutes, emprunte les passes à
poissons. La femelle creuse un nid dans le gravier avec sa queue et y pond.
Le saumon atlantique, épuisé, peut retourner à la mer et revenir pondre.

Plans : 1 gros plan (les œufs dans le gravier) · 2 gros plan (les alevins)
· 3 moyen (le tacon) · 4 large (vers la mer) · 5 large (en mer) · 6 gros
plan (l'odeur de la rivière) · 7 large (remonter le courant) · 8 large (le
saut) · 9 moyen (la passe à poissons) · 10 moyen (le nid) · 11 large (le
retour à la mer) · 12 schéma (le cycle).
"""
from base import *
from base import _assombrir
from animaux import loupe, etiquette, cycle, disque, sous_l_eau
from sciences import fleche
from fantastique import personne

ID = "voyage-saumon"


def saumon(x, y, s=1.0, flip=False, rot=0, stade="adulte", expr="sourire", bouche=False):
    """Saumon de profil, tête à droite ; (x, y) = centre. stade : "alevin", "tacon", "saumoneau", "adulte", "frai" (couleurs de ponte)."""
    dos = {"alevin": "#a9906f", "tacon": "#8d7b5a", "saumoneau": "#5c7cfa", "adulte": "#4c6ef5", "frai": "#9c4221"}[stade]
    ventre = {"alevin": "#e9d8a6", "tacon": "#e9ecef", "saumoneau": "#f1f3f5", "adulte": "#f1f3f5", "frai": "#e8a07a"}[stade]
    corps = "M -110 0 Q -60 -46 30 -44 Q 90 -40 120 0 Q 90 40 30 42 Q -60 44 -110 0 Z"
    m = [chemin("M -104 0 L -160 -40 Q -150 0 -160 40 Z", _assombrir(dos, 0.85)),
         chemin(corps, lineaire([(0, dos), (0.55, eclaircir(dos, 0.3)), (0.7, ventre), (1, ventre)])),
         chemin("M -20 -42 L 0 -72 L 30 -44 Z", _assombrir(dos, 0.85)), chemin("M -40 36 L -24 56 L -4 40 Z", _assombrir(ventre, 0.85)),
         chemin("M 60 -10 Q 70 10 60 30", stroke=_assombrir(dos, 0.7), sw=3)]
    r = random.Random(7)
    if stade in ("adulte", "frai"):
        for k in range(14):
            m.append(cercle(r.uniform(-80, 50), r.uniform(-34, -6), 3, "#212529", opacity=0.7))
    if stade == "tacon":
        for k in range(7):
            m.append(ellipse(-80 + k * 24, -4, 7, 12, "#5c4a33", opacity=0.6))
        for k in range(8):
            m.append(cercle(r.uniform(-80, 60), r.uniform(-26, 6), 2.5, "#e03131", opacity=0.8))
    if stade == "saumoneau":
        m.append(chemin(corps, "#fff", opacity=0.25))
    if stade == "alevin":
        m.append(ellipse(10, 34, 40, 26, volume("#ff922b", 0.4, 0.8)))
    if stade == "frai":
        m.append(chemin("M 110 -10 Q 130 -2 120 12", stroke="#9c4221", sw=8))
    m.append(cercle(84, -8, 9, "#fff"))
    m.append(oeil(86, -8, "heureux" if expr == "content" else ("fermes" if expr == "dort" else "normal"), (1, 0), taille=0.6))
    if bouche:
        m.append(chemin("M 110 6 L 122 2", stroke="#212529", sw=3))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 160 * s, y - 70 * s, x + 125 * s, y + 60 * s)


def gravier(S, y=640, graine=1, oeufs=0):
    r = random.Random(graine)
    for k in range(70):
        S.add(ellipse(r.uniform(0, 800), r.uniform(y, 800), r.uniform(14, 34), r.uniform(10, 20),
                      r.choice(("#adb5bd", "#868e96", "#ced4da", "#a39382", "#8d7b6a")), rot=r.uniform(-30, 30)))
    for k in range(oeufs):
        S.add(cercle(r.uniform(150, 650), r.uniform(y + 30, 780), 9, volume("#ff922b", 0.5, 0.75)))


def riviere_dessous(S, y_fond=640, graine=1, haut="#a5d8ff", bas="#1971c2", plantes=True):
    sous_l_eau(S, haut, bas, "#8d7b6a", y_fond, graine=graine, plantes=plantes)


def ocean_large(S, graine=1):
    S._decor("eau")
    S.add(rect(0, 0, 800, 800, S.degrade(["#4dabf7", "#1864ab", "#0b4f8a"])))
    for k in range(6):
        S.add(poly([(100 + k * 130, 0), (160 + k * 130, 0), (60 + k * 130, 800), (20 + k * 130, 800)], "#fff", opacity=0.05))


def banc_poissons(x, y, s=1.0, graine=1, nb=12):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        px, py = r.uniform(-120, 120), r.uniform(-60, 60)
        m.append(place([ellipse(0, 0, 18, 6, "#dee2e6"), poly([(-16, 0), (-26, -6), (-26, 6)], "#adb5bd")], px, py))
    return place(m, x, y, s)


def chute(S, y_haut=300, y_bas=620, graine=1):
    """Chute d'eau vue de face, sur toute la largeur : la rivière du haut, le rideau d'eau, le bassin."""
    r = random.Random(graine)
    S.add(rect(0, y_haut - 70, 800, 40, "#69db7c"))
    for k in range(7):
        S.add(sapin(30 + k * 125, y_haut - 36, 0.55, "#2b8a3e", "#2f9e44"))
    S.add(rect(0, y_haut - 40, 800, 44, "#4dabf7"), rect(0, y_haut - 40, 800, 8, "#a5d8ff", opacity=0.7))
    S.add(rect(0, y_haut, 800, y_bas - y_haut, lineaire([(0, "#e7f5ff"), (1, "#a5d8ff")])))
    for k in range(30):
        x = r.uniform(0, 800)
        S.add(trait(x, y_haut + r.uniform(0, 30), x + r.uniform(-4, 4), y_bas - r.uniform(0, 40), "#fff", r.uniform(2, 5), opacity=r.uniform(0.4, 0.8)))
    S.add(chemin(f"M 0 {y_haut - 10} Q 70 {y_haut - 20} 110 {y_haut + 40} Q 140 {y_haut + 160} 120 {y_bas + 30} L 0 {y_bas + 40} Z", volume("#868e96", 0.35, 0.8)))
    S.add(chemin(f"M 800 {y_haut - 6} Q 720 {y_haut - 10} 690 {y_haut + 60} Q 660 {y_haut + 180} 690 {y_bas + 30} L 800 {y_bas + 40} Z", volume("#868e96", 0.35, 0.8)))
    S.add(ellipse(330, y_haut + 10, 46, 22, volume("#868e96", 0.35, 0.8)), ellipse(560, y_haut + 120, 34, 26, volume("#868e96", 0.35, 0.8)))
    S.add(rect(0, y_bas, 800, 800 - y_bas, lineaire([(0, "#74c0fc"), (1, "#1864ab")])))
    for k in range(24):
        S.add(cercle(k * 36 + r.uniform(-8, 8), y_bas + r.uniform(-6, 12), r.uniform(12, 24), "#fff", opacity=0.85))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    chute(S, 330, 620)
    S.add(saumon(640, 520, 0.6, rot=-70))
    S.add(saumon(400, 420, 1.1, rot=-60))
    S.add(chemin("M 250 650 Q 270 590 305 560", stroke="#fff", sw=4, opacity=0.7, stroke_dasharray="10 10"))
    S.cachette(720, 740, "poisson")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(saumon(210, 135, 1.0))
    return S


def p01():
    """Gros plan : à l'automne, au fond de la rivière, des œufs orange cachés dans le gravier."""
    S = Scene()
    riviere_dessous(S, 520, graine=1, plantes=False)
    gravier(S, 540, graine=1, oeufs=30)
    contenu = g([rect(420, 100, 360, 300, "#8d7b6a"), cercle(600, 250, 80, volume("#ff922b", 0.5, 0.75)), cercle(570, 220, 20, "#fff", opacity=0.5),
                 cercle(612, 262, 8, "#495057")])
    S.add(loupe(600, 250, 120, contenu, rot=140))
    S.add(etiquette(600, 420, "un œuf", 34, "#e8590c"))
    S.cachette(90, 470, "poisson")
    return S


def p02():
    """Gros plan : au printemps, les alevins sortent de l'œuf, avec leur réserve orange sous le ventre."""
    S = Scene()
    riviere_dessous(S, 520, graine=2, plantes=False)
    gravier(S, 540, graine=2)
    for k, (x, y, rot) in enumerate(((200, 560, -10), (380, 600, 5), (560, 570, -6), (680, 640, 10))):
        S.add(saumon(x, y, 0.7, stade="alevin", rot=rot, expr="content"))
    S.camera(1.15, 420, 560)
    S.dessus(texte(400, 110, "Des alevins, avec leur réserve !", 42, "#e8590c", contour="#fff"))
    return S


def p03():
    """Plan moyen : le tacon, tacheté, chasse les petits insectes dans la rivière."""
    S = Scene()
    riviere_dessous(S, 660, graine=3)
    gravier(S, 680, graine=3)
    S.add(saumon(380, 420, 1.5, stade="tacon", bouche=True))
    for x, y in ((600, 380), (640, 330), (580, 300)):
        S.add(ellipse(x, y, 10, 4, "#495057"), trait(x - 6, y - 2, x - 12, y - 10, "#adb5bd", 2), trait(x + 2, y - 2, x + 8, y - 10, "#adb5bd", 2))
    S.add(texte(400, 120, "Le tacon grandit dans la rivière", 40, "#5c4a33", contour="#fff"))
    return S


def p04():
    """Plan large, vue d'en haut : devenus saumoneaux, tout argentés, ils descendent la rivière jusqu'à la mer."""
    S = Scene()
    fond(S, "#8ce99a")
    r = random.Random(4)
    for k in range(40):
        S.add(cercle(r.uniform(0, 800), r.uniform(0, 800), r.uniform(10, 30), "#69db7c", opacity=0.5))
    riv = "M -40 820 C 120 700 120 600 260 540 S 460 420 560 240"
    S.add(chemin(riv, stroke="#e9c46a", sw=150), chemin(riv, stroke="#4dabf7", sw=120), chemin(riv, stroke="#a5d8ff", sw=20, opacity=0.5))
    mer = "M 330 -10 Q 520 330 810 450 L 810 -10 Z"
    S.add(chemin("M 330 -10 Q 520 330 810 450", stroke="#e9c46a", sw=40))
    S.add(chemin(mer, lineaire([(0, "#1864ab"), (1, "#339af0")], 1, 0, 0, 1)))
    for x, y in ((600, 80), (700, 200), (720, 330), (520, 130), (650, 300)):
        S.add(chemin(f"M {x} {y} q 15 -10 30 0 q 15 10 30 0", stroke="#a5d8ff", sw=4))
    for x, y, t in ((60, 420, 0.5), (130, 330, 0.55), (60, 240, 0.5), (210, 230, 0.6), (380, 640, 0.5), (500, 580, 0.55), (620, 620, 0.5), (700, 540, 0.55), (560, 720, 0.5)):
        S.add(sapin(x, y, t, "#2b8a3e", "#2f9e44"))
    S.add(saumon(110, 720, 0.38, stade="saumoneau", rot=-40), saumon(255, 545, 0.42, stade="saumoneau", rot=-25), saumon(430, 430, 0.42, stade="saumoneau", rot=-45))
    S.add(texte(250, 690, "la rivière", 36, "#1864ab", contour="#fff"), texte(660, 150, "la mer", 44, "#fff", contour="#1864ab"))
    S.cachette(740, 760)
    return S


def p05():
    """Plan large : en mer, très loin, le saumon a beaucoup grandi ; il nage parmi les bancs de poissons."""
    S = Scene()
    ocean_large(S)
    S.add(banc_poissons(600, 250, 1.2, 1, 16), banc_poissons(200, 600, 1.0, 2, 12))
    S.add(saumon(380, 440, 1.8, stade="adulte"))
    S.add(texte(400, 110, "Jusqu'au Groenland !", 50, "#fff", contour="#1864ab"))
    S.cachette(700, 720, "poisson")
    return S


def p06():
    """Gros plan : le saumon reconnaît l'odeur de l'eau de sa rivière."""
    S = Scene()
    ocean_large(S, 2)
    S.add(saumon(400, 470, 2.2, stade="adulte", expr="content"))
    for k in range(4):
        S.add(chemin(f"M {700 - k * 10} {340 + k * 30} q -30 -10 -60 0 q -30 10 -60 0", stroke="#d3f9d8", sw=5, opacity=0.8))
    S.add(texte(400, 130, "Hmm… l'odeur de ma rivière !", 44, "#fff", contour="#1864ab"))
    S.cachette(110, 720, "poisson")
    return S


def p07():
    """Plan large : le saumon remonte le courant de la rivière, entre les rochers."""
    S = Scene()
    riviere_dessous(S, 680, graine=7)
    gravier(S, 700, graine=7)
    for x in (100, 680):
        S.add(ellipse(x, 640, 110, 80, "#868e96"))
    S.add(saumon(400, 420, 1.3, stade="adulte", flip=True))
    for x, y in ((80, 240), (420, 230), (60, 560), (560, 590), (200, 320), (620, 330)):
        S.add(fleche(x, y, x + 120, y, "#e7f5ff", sw=5, tete=16, opacity=0.7))
    S.add(texte(400, 120, "À contre-courant !", 48, "#fff", contour="#1864ab"))
    S.add(texte(680, 290, "le courant", 26, "#e7f5ff"))
    return S


def p08():
    """Plan large : hop ! le saumon saute par-dessus la chute d'eau."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    chute(S, 340, 600, graine=8)
    S.add(saumon(440, 400, 1.2, rot=-65))
    S.add(chemin("M 330 640 Q 345 600 370 565", stroke="#fff", sw=4, opacity=0.7, stroke_dasharray="10 10"))
    S.add(texte(640, 170, "Hop !", 80, "#1864ab", contour="#fff"))
    S.cachette(720, 740, "poisson")
    return S


def p09():
    """Plan moyen : une passe à poissons, des bassins en escalier ; des enfants regardent par la vitre."""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 560, 800, 240, "#ced4da"))
    S.add(rect(690, 150, 110, 410, "#adb5bd"), rect(690, 140, 110, 14, "#868e96"), rect(700, 120, 100, 24, "#4dabf7"))
    for k in range(5):
        x0, y0 = 60 + k * 130, 500 - k * 60
        S.add(rect(x0 - 8, y0, 156, 560 - y0, "#adb5bd"), rect(x0, y0 + 14, 140, 96, lineaire([(0, "#74c0fc"), (1, "#1971c2")])))
        S.add(rect(x0 - 8, y0, 10, 110, "#868e96"))
        S.add(chemin(f"M {x0 + 132} {y0 - 46} Q {x0 + 146} {y0 - 30} {x0 + 140} {y0 + 16}", stroke="#e7f5ff", sw=8, opacity=0.8))
    S.add(saumon(250, 470, 0.5, rot=-30), saumon(510, 350, 0.5, rot=-30))
    S.add(rect(80, 600, 640, 160, "#d0ebff", stroke="#495057", stroke_width=8, rx=6))
    S.add(saumon(380, 690, 0.7))
    S.add(personne(200, 790, 1.0, expr="bouche_bee", bras="joues", regard=(1, -0.3), peau="doree", cheveux="noir", coiffure="couettes", habit="#f06595"))
    S.add(personne(600, 790, 1.0, expr="rire", bras="designe", flip=True, regard=(-1, -0.3), peau="claire", cheveux="roux", coiffure="courts", habit="#40c057", robe=False))
    S.add(texte(400, 120, "Une passe à poissons", 44, "#1864ab", contour="#fff"))
    S.cachette(740, 790)
    return S


def p10():
    """Plan moyen : dans le gravier, la femelle creuse un nid avec sa queue ; le mâle attend à côté."""
    S = Scene()
    riviere_dessous(S, 620, graine=10)
    gravier(S, 640, graine=10, oeufs=10)
    S.add(saumon(320, 560, 1.3, stade="frai", rot=12))
    S.add(saumon(560, 470, 1.2, stade="frai", flip=True))
    for k in range(6):
        S.add(ellipse(160 + k * 20, 600 - (k % 2) * 30, 10, 7, "#adb5bd"))
    S.add(texte(400, 120, "La femelle creuse un nid", 44, "#9c4221", contour="#fff"))
    return S


def p11():
    """Plan large : fatiguée, la femelle redescend vers la mer ; un jour, elle reviendra peut-être."""
    S = Scene()
    riviere_dessous(S, 680, graine=11, haut="#ffd8a8", bas="#1971c2")
    gravier(S, 700, graine=11)
    S.add(saumon(400, 420, 1.2, stade="adulte", rot=6))
    S.add(texte(400, 140, "Au revoir, la rivière…", 48, "#fff", contour="#1864ab"))
    return S


def p12():
    """Schéma : le cycle du saumon : l'œuf, l'alevin, le tacon, le saumoneau, le saumon en mer."""
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(cycle(400, 410, 260, "#1971c2", nb=5, ecart=22))
    pos = [(400, 150), (647, 330), (553, 620), (247, 620), (153, 330)]
    noms = ("l'œuf", "l'alevin", "le tacon", "le saumoneau", "le saumon")
    for (x, y), nom, stade in zip(pos, noms, (None, "alevin", "tacon", "saumoneau", "adulte")):
        S.add(disque(x, y, 92, "#d0ebff"))
        if stade:
            S.add(saumon(x + 6, y, 0.5, stade=stade))
        else:
            S.add(cercle(x, y, 30, volume("#ff922b", 0.5, 0.75)))
        S.add(etiquette(x, y + 128, nom, 28, "#1864ab"))
    S.cachette(720, 760, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("saumon-seul.svg", vignette),
    ("01-les-oeufs.svg", p01), ("02-les-alevins.svg", p02), ("03-le-tacon.svg", p03),
    ("04-vers-la-mer.svg", p04), ("05-en-mer.svg", p05), ("06-l-odeur.svg", p06),
    ("07-a-contre-courant.svg", p07), ("08-hop.svg", p08), ("09-la-passe.svg", p09),
    ("10-le-nid.svg", p10), ("11-au-revoir.svg", p11), ("12-le-cycle.svg", p12),
]
