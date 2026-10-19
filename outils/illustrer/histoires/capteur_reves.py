"""Le capteur de rêves — d'après une légende ojibwée (Anishinaabe).

Ziigwan, une petite fille ojibwée, se réveille la nuit à cause d'un
mauvais rêve. Sa grand-mère, Nokomis, lui raconte l'histoire
d'Asibikaashi, Grand-mère Araignée, qui tissait autrefois une toile
au-dessus de chaque berceau pour protéger les enfants : les mauvais rêves
se prennent dans la toile et fondent au premier rayon du soleil ; les bons
rêves passent par le petit trou du milieu et glissent le long d'une plume
jusqu'à l'enfant endormi. Quand le peuple s'est dispersé, les mères et les
grands-mères ont appris à tisser ces toiles elles-mêmes. Ensemble, Nokomis
et Ziigwan fabriquent un capteur de rêves avec une branche de saule. La
nuit suivante, Ziigwan dort paisiblement.

Plans : 1 moyen (le mauvais rêve) · 2 moyen (Nokomis raconte) · 3 large
(Grand-mère Araignée, autrefois) · 4 large (la branche de saule) · 5 gros
plan (tisser) · 6 moyen (on l'accroche) · 7 gros plan (la nuit, les
rêves) · 8 large (le matin) · 9 moyen (bonjour, Nokomis).
"""
from contes import *
from base import _assombrir

ID = "capteur-reves"

ZIIGWAN = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#e03131", robe=True, yeux="cils", nez="petit")
NOKOMIS = dict(stature="ancien", peau="brune", cheveux="gris", coiffure="tresses", habit="#1864ab", robe=True, nez="rond", carrure="ronde",
               ceinture="#fab005")
ECORCE = "#f1e3c8"
SAULE = "#8d5524"


def perles(x, y, w, couleurs=("#e03131", "#fab005", "#1c7ed6", "#2f9e44")):
    """Petite bande de perles brodées."""
    return g([cercle(x + k * 9, y, 4, couleurs[k % len(couleurs)]) for k in range(int(w // 9))])


def capteur(x, y, r=90, plumes=2, inacheve=False, reves=()):
    """Capteur de rêves : cercle de saule, toile tissée, perle au centre, plumes pendantes ; (x, y) = centre du cercle."""
    m = []
    if not inacheve:
        for k in range(plumes):
            px = x + (k - (plumes - 1) / 2) * r * 0.7
            m += [trait(px, y + r * 0.9, px, y + r * 1.5, "#8d6e4a", 3), perles(px - 4, y + r * 1.5, 12),
                  place([chemin("M 0 0 Q -16 40 0 110 Q 16 40 0 0 Z", "#f8f9fa", stroke="#adb5bd", sw=2), trait(0, 0, 0, 110, "#868e96", 2),
                         chemin("M 0 80 Q -10 96 0 110 Q 10 96 0 80 Z", "#495057")], px, y + r * 1.56, r / 90)]
    m.append(cercle(x, y, r, "none", stroke=SAULE, stroke_width=r * 0.12))
    m.append(cercle(x, y, r, "none", stroke="#c5a07a", stroke_width=r * 0.04, stroke_dasharray="6 10"))
    nb = 8
    pts = [(x + math.cos(k * 2 * math.pi / nb) * r * 0.94, y + math.sin(k * 2 * math.pi / nb) * r * 0.94) for k in range(nb)]
    tour = int(3 if not inacheve else 1)
    for t in range(tour):
        k_r = 0.94 - (t + 1) * 0.22
        pts2 = [(x + math.cos((k + 0.5 * (t + 1)) * 2 * math.pi / nb) * r * k_r, y + math.sin((k + 0.5 * (t + 1)) * 2 * math.pi / nb) * r * k_r)
                for k in range(nb)]
        for k in range(nb):
            m.append(chemin(f"M {n(pts[k][0])} {n(pts[k][1])} L {n(pts2[k][0])} {n(pts2[k][1])} L {n(pts[(k + 1) % nb][0])} {n(pts[(k + 1) % nb][1])}",
                            stroke="#7c4a1e", sw=max(2.2, r * 0.03)))
        pts = pts2
    if not inacheve:
        m.append(cercle(x, y, r * 0.08, "#1c7ed6"))
    m += list(reves)
    return g(m)


def mauvais_reve(x, y, s=1.0):
    """Un mauvais rêve : petit nuage gris aux sourcils froncés."""
    m = [cercle(-18, 0, 18, "#868e96"), cercle(4, -10, 22, "#868e96"), cercle(24, 2, 16, "#868e96"), rect(-30, 0, 60, 16, "#868e96", rx=8),
         cercle(-4, -6, 3.5, ENCRE), cercle(10, -6, 3.5, ENCRE), trait(-10, -14, -1, -11, ENCRE, 2.5), trait(16, -14, 7, -11, ENCRE, 2.5),
         chemin("M -4 8 Q 3 3 10 8", stroke=ENCRE, sw=2.5)]
    return place(m, x, y, s)


def bon_reve(x, y, s=1.0, sorte=0):
    """Un bon rêve qui brille : papillon, étoile ou petit poisson doré."""
    if sorte == 0:
        m = [papillon(0, 0, 0.6, "#f783ac", "#ffe066")]
    elif sorte == 1:
        m = [etoile5(0, 0, 16, "#ffe066")]
    else:
        m = [poisson(0, 10, 0.32, "#ffd43b")]
    return g([cercle(x, y, 26 * s, radial([(0, "#fff3bf", 0.7), (1, "#fff3bf", 0)])), place(m, x, y, s)])


def wigwam(x, y, s=1.0, lumiere=False):
    """Wigwam en dôme couvert d'écorce de bouleau ; (x, y) = milieu de la base."""
    dome = chemin("M -170 0 Q -170 -200 0 -200 Q 170 -200 170 0 Z", "#000")
    m = [chemin("M -170 0 Q -170 -200 0 -200 Q 170 -200 170 0 Z", volume(ECORCE, 0.3, 0.8))]
    for k in range(5):
        yy = -30 - k * 36
        w = 170 * math.sqrt(max(0, 1 - ((yy + 0) / 200) ** 2))
        m.append(chemin(f"M {n(-w)} {yy} Q 0 {yy - 12} {n(w)} {yy}", stroke="#8d6e4a", sw=3))
    r = random.Random(2)
    for _ in range(26):
        px, py = r.uniform(-140, 140), r.uniform(-170, -10)
        m.append(trait(px, py, px + r.uniform(8, 20), py, "#495057", 2.5, opacity=0.6))
    m += [chemin("M -40 0 L -40 -80 Q 0 -110 40 -80 L 40 0 Z", "#ffd43b" if lumiere else "#5c3d24"), rect(-60, -210, 120, 14, "#8d6e4a", rx=6)]
    m = [g(m, clip_path=None)]
    return place(m, x, y, s)


def bouleau(x, y, s=1.0, h=420):
    m = [rect(-16, -h, 32, h, cylindre("#f8f9fa", 0.2, 0.8), rx=10)]
    r = random.Random(int(x))
    for k in range(9):
        yy = -h + 30 + k * h / 10
        m.append(trait(-16, yy, r.uniform(-4, 10), yy + 4, "#343a40", 3))
    m.append(feuillage([(0, -h - 40, 90, "#69db7c"), (-60, -h + 20, 60, "#51cf66"), (60, -h + 10, 64, "#40c057")]))
    return place(m, x, y, s)


def bord_du_lac(S, moment="jour", horizon=500):
    if moment == "aube":
        ciel(S, "#ffa8a8", "#ffec99")
    elif moment == "nuit":
        nuit(S)
        etoiles(S, 40, 3, (0, 0, 800, horizon - 60))
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    sombre = moment == "nuit"
    for k in range(10):
        S.add(sapin(30 + k * 85, horizon + 10, 0.45 + (k % 3) * 0.1, couleur="#2b8a3e" if not sombre else "#1c3a2c", couleur2="#2f9e44" if not sombre else "#24473a"))
    S.add(rect(0, horizon, 800, 90, lineaire([(0, "#4dabf7" if not sombre else "#2c3e74"), (1, "#a5d8ff" if not sombre else "#3b4a8a")])))
    sol(S, horizon + 90, "#8ce99a" if not sombre else "#2f4a3a")


def dedans_wigwam(S, nuit_=True, feu_=True):
    """Intérieur du wigwam : perches courbes, écorce, peaux au sol, petit feu."""
    S.add(rect(0, 0, 800, 800, ECORCE))
    for k in range(9):
        S.add(chemin(f"M {-200 + k * 150} 800 Q 400 -300 {1000 - k * 150} 800", stroke="#a07c58", sw=10, opacity=0.6))
    for k in range(6):
        S.add(chemin(f"M -40 {100 + k * 90} Q 400 {k * 90 - 20} 840 {100 + k * 90}", stroke="#c5a07a", sw=4))
    S.add(rect(0, 600, 800, 200, terrain("#8d6e4a")))
    S.ambiance("nuit" if nuit_ else "interieur")
    if feu_:
        S.add(ellipse(640, 720, 70, 14, "#495057"), flammes(640, 720, 0.6, graine=3))
        S.lumiere(640, 680, 220, "#ffa94d", 0.6)
    S.proposer_cachette(60, 790)


def couche(x, y, s=1.0, dort=True, assise=False):
    """Ziigwan sur sa couche de fourrures, sous une couverture à bandes."""
    m = [ellipse(x, y, 230 * s, 40 * s, volume("#a07c58", 0.3, 0.75)), ellipse(x - 150 * s, y - 30 * s, 60 * s, 26 * s, volume("#e9d8c4", 0.3, 0.85))]
    if assise:
        m.append(personne(x - 60 * s, y + 10 * s, s * 1.1, expr="pleure", bras="yeux", larmes=True, sy=0.8, **ZIIGWAN))
        m.append(chemin(f"M {n(x - 150 * s)} {n(y - 20 * s)} Q {n(x)} {n(y - 70 * s)} {n(x + 200 * s)} {n(y - 10 * s)} L {n(x + 200 * s)} {n(y + 20 * s)} L {n(x - 150 * s)} {n(y + 20 * s)} Z",
                        volume("#1c7ed6", 0.3, 0.8)))
    else:
        m.append(personne(x - 40 * s, y - 50 * s, s * 0.9, expr="dort" if dort else "content", bras="bas", rot=-90, **ZIIGWAN))
        m.append(chemin(f"M {n(x - 100 * s)} {n(y - 40 * s)} Q {n(x + 40 * s)} {n(y - 120 * s)} {n(x + 210 * s)} {n(y - 30 * s)} L {n(x + 210 * s)} {n(y + 10 * s)} L {n(x - 100 * s)} {n(y + 10 * s)} Z",
                        volume("#1c7ed6", 0.3, 0.8)))
    for k in range(4):
        m.append(trait(x - 60 * s + k * 60 * s, y - 70 * s + abs(k - 1.5) * 10 * s, x - 60 * s + k * 60 * s, y + 10 * s, "#fab005", 6 * s))
    return g(m)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    dedans_wigwam(S, feu_=False)
    S.add(capteur(400, 250, 120, plumes=3))
    S.lumiere(400, 250, 200, "#fff3bf", 0.4)
    for k, (x, y) in enumerate(((330, 470), (470, 520), (400, 560))):
        S.add(bon_reve(x, y, 1.0, k))
    S.add(couche(400, 740, 1.0))
    S.cachette(720, 795)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(capteur(200, 90, 70, plumes=3))
    return S


def p01():
    """Plan moyen : la nuit, dans le wigwam, Ziigwan s'est réveillée en pleurant ; un mauvais rêve gris flotte encore au-dessus d'elle."""
    S = Scene()
    dedans_wigwam(S)
    S.add(couche(330, 760, 1.0, assise=True))
    S.add(mauvais_reve(300, 300, 2.0), mauvais_reve(460, 220, 1.3))
    S.add(texte(560, 120, "Ouin !", 50, "#495057", contour="#fff"))
    S.cachette(720, 795)
    return S


def p02():
    """Plan moyen : Nokomis, la grand-mère, prend Ziigwan dans ses bras près du feu : « Je vais te raconter l'histoire de Grand-mère Araignée. »"""
    S = Scene()
    dedans_wigwam(S)
    S.add(personne(470, 800, 1.5, expr="content", bras="calin", regard=(-1, 0.3), **NOKOMIS))
    S.add(personne(470, 720, 0.85, expr="triste", bras="calin", regard=(1, -0.5), **ZIIGWAN))
    S.add(bulle(330, 150, 520, 100, "Je vais te raconter l'histoire\nde Grand-mère Araignée…", 28, pointe=(450, 340)))
    S.cachette(60, 795)
    return S


def p03():
    """Plan large : autrefois, au lever du soleil, Asibikaashi, Grand-mère Araignée, tisse une toile au-dessus du berceau d'un bébé endormi."""
    S = Scene()
    bord_du_lac(S, "aube", 520)
    S.add(wigwam(620, 650, 0.8))
    S.add(soleil(160, 460, 60))
    S.add(trait(300, 220, 300, 600, "#8d6e4a", 8), trait(520, 220, 520, 600, "#8d6e4a", 8), trait(290, 230, 530, 230, "#8d6e4a", 8))
    S.add(toile(410, 330, 100, perles=True))
    S.add(araignee_perso(410, 330, 0.9, expr="content", fil=100))
    S.add(place([rect(-70, -40, 140, 60, volume("#c5a07a", 0.3, 0.8), rx=20), cercle(-40, -40, 26, "#a86a3f"), oeil(-48, -42, "fermes", taille=0.5),
                 oeil(-32, -42, "fermes", taille=0.5)], 410, 600))
    S.add(zzz(470, 520, 0.8))
    S.cachette(740, 790)
    return S


def p04():
    """Plan large : au bord du lac, entre les bouleaux, Nokomis et Ziigwan coupent une souple branche de saule rouge."""
    S = Scene()
    bord_du_lac(S, "jour", 480)
    S.add(bouleau(90, 760, 1.0, 460), bouleau(720, 740, 0.9, 420))
    S.add(personne(300, 790, 1.4, expr="content", bras="tend", regard=(1, 0), **NOKOMIS))
    S.add(chemin("M 420 560 Q 520 480 600 520", stroke="#c92a2a", sw=8))
    S.add(personne(520, 790, 1.1, expr="joie", bras="tient", objet=chemin("M 68 -146 Q 110 -200 150 -170", stroke="#c92a2a", sw=7), regard=(-1, 0), flip=True,
                   **ZIIGWAN))
    S.cachette(140, 70, "air")
    return S


def p05():
    """Gros plan : les mains de Nokomis plient la branche en cercle ; Ziigwan tisse la toile comme une araignée, en laissant un petit trou au milieu."""
    S = Scene()
    dedans_wigwam(S, nuit_=False)
    S.add(personne(230, 800, 1.4, expr="sourire", bras="tend", regard=(1, -0.2), **NOKOMIS))
    S.add(personne(600, 800, 1.2, expr="concentre", bras="tend", flip=True, regard=(-1, -0.2), **ZIIGWAN))
    S.add(capteur(420, 520, 110, plumes=0, inacheve=True))
    S.add(trait(420, 520, 520, 620, "#7c4a1e", 3))
    S.camera(1.5, 420, 520)
    S.dessus(texte(400, 90, "Un petit trou au milieu…", 42, "#8d5524", contour="#fff"))
    S.cachette(640, 453, "air")
    return S


def p06():
    """Plan moyen : debout sur la pointe des pieds, Ziigwan accroche le capteur de rêves, avec sa perle bleue et ses plumes, au-dessus de sa couche."""
    S = Scene()
    dedans_wigwam(S, nuit_=False)
    S.add(capteur(380, 200, 80, plumes=2))
    S.add(couche(400, 770, 0.9))
    S.add(personne(530, 780, 1.2, expr="joie", bras="haut", regard=(-1, -1), pas="pointe", **ZIIGWAN))
    S.add(personne(180, 790, 1.3, expr="content", bras="applaudit", regard=(1, -0.5), **NOKOMIS))
    S.cachette(720, 795)
    return S


def p07():
    """Gros plan : la nuit, les mauvais rêves gris se prennent dans la toile ; les bons rêves dorés passent par le trou et glissent le long des plumes."""
    S = Scene()
    dedans_wigwam(S, feu_=False)
    reves = [mauvais_reve(320, 180, 0.9), mauvais_reve(470, 230, 0.8), mauvais_reve(390, 300, 0.7)]
    S.add(capteur(400, 240, 140, plumes=2, reves=reves))
    S.lumiere(400, 240, 220, "#a5d8ff", 0.3)
    for k, (x, y) in enumerate(((400, 360), (350, 470), (450, 540))):
        S.add(bon_reve(x, y, 1.2, k))
    S.add(couche(400, 760, 1.0))
    S.camera(1.2, 400, 420)
    S.cachette(150, 470)
    return S


def p08():
    """Plan large : au lever du soleil, le premier rayon touche le capteur de rêves accroché devant le wigwam : les mauvais rêves fondent comme la brume."""
    S = Scene()
    bord_du_lac(S, "aube", 500)
    S.add(soleil(150, 440, 60))
    S.add(wigwam(520, 700, 1.0))
    S.add(trait(360, 330, 360, 420, "#8d6e4a", 3), capteur(360, 460, 60, plumes=2))
    for k in range(5):
        S.add(trait(200, 440, 330 + k * 14, 430 + k * 10, "#fff3bf", 6, opacity=0.6))
    for k, (x, y) in enumerate(((300, 360), (420, 330), (260, 300))):
        S.add(g([mauvais_reve(x, y, 0.7)], opacity=0.3 - k * 0.08))
    S.add(texte(560, 160, "Pschhh…", 48, "#e8590c", contour="#fff"))
    S.cachette(740, 790)
    return S


def p09():
    """Plan moyen : au matin, Ziigwan s'éveille en souriant et saute dans les bras de Nokomis : « J'ai fait un beau rêve ! »"""
    S = Scene()
    dedans_wigwam(S, nuit_=False, feu_=False)
    S.add(capteur(560, 200, 80, plumes=2))
    S.lumiere(400, 100, 260, "#fff3bf", 0.5)
    S.add(personne(260, 790, 1.4, expr="rire", bras="ouverts", regard=(1, 0), **NOKOMIS))
    S.add(personne(500, 790, 1.15, expr="rire", bras="saute", flip=True, regard=(-1, 0), **ZIIGWAN))
    S.add(bulle(500, 420, 420, 90, "J'ai fait un beau rêve !", 32, pointe=(500, 560)))
    S.cachette(720, 795)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("capteur-seul.svg", vignette),
    ("01-le-mauvais-reve.svg", p01), ("02-nokomis.svg", p02), ("03-grand-mere-araignee.svg", p03),
    ("04-la-branche-de-saule.svg", p04), ("05-tisser.svg", p05), ("06-on-l-accroche.svg", p06),
    ("07-la-nuit-des-reves.svg", p07), ("08-le-matin.svg", p08), ("09-un-beau-reve.svg", p09),
]
