"""Nina, la princesse pirate — le plus beau des trésors."""
from base import *
from objets import *
from fantastique import *
from contes import tresor, panier
from fables import grelot, collier, flammes

ID = "nina-pirate"
NINA = dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#e03131", robe=False,
            jambes="#1c2a52", ceinture="#343a40")
NINA_PRINCESSE = dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#f783ac", robe=True,
                      motif_robe="#fff0f6")
BARNABE = dict(peau="claire", cheveux="blanc", coiffure="chauve_cote", barbe="#e9ecef", habit="#1c7ed6",
               robe=False, jambes="#343a40", chaussures="#212529")
COCO = dict(couleur="#2f9e44", ventre="#ffe066")
BISCOTTE = "#ffa94d"
CRABE = "#f03e3e"


# ---------------------------------------------------------------------------
# Accessoires et personnages
# ---------------------------------------------------------------------------

def chapeau_pirate(rot=0):
    """Tricorne noir (coordonnées d'un personnage de face, tête vers y = -150)."""
    m = [chemin("M -80 -194 Q -50 -188 0 -190 Q 50 -188 80 -194 Q 62 -210 44 -208 Q 28 -256 0 -256 "
                "Q -28 -256 -44 -208 Q -62 -210 -80 -194 Z", "#343a40"),
         chemin("M -80 -194 Q -50 -188 0 -190 Q 50 -188 80 -194", stroke=OR, sw=5),
         cercle(0, -228, 11, "#f8f9fa"), rect(-7, -221, 14, 8, "#f8f9fa", rx=3),
         cercle(-4, -229, 2.8, "#343a40"), cercle(4, -229, 2.8, "#343a40"),
         trait(-15, -202, 15, -212, "#f8f9fa", 4), trait(-15, -212, 15, -202, "#f8f9fa", 4)]
    return place(m, 0, 0, 1.0, rot=rot)


def bonnet_marin():
    return g([chemin("M -54 -160 Q -52 -214 0 -216 Q 52 -214 54 -160 Z", "#1864ab"),
              rect(-58, -170, 116, 18, "#d0ebff", rx=8), cercle(0, -220, 13, "#fa5252")])


def nina(x, y, s=1.0, chapeau=True, princesse=False, flip=False, **k):
    style = NINA_PRINCESSE if princesse else NINA
    m = [personne(x, y, s, flip=flip, **{**style, **k})]
    if chapeau:
        m.append(place(chapeau_pirate(), x, y, s, flip=flip))
    return g(m)


def barnabe(x, y, s=1.0, flip=False, **k):
    return g([personne(x, y, s, flip=flip, **{**BARNABE, **k}), place(bonnet_marin(), x, y, s, flip=flip)])


def coco(x, y, s=1.0, **k):
    """Coco le perroquet : oiseau vert avec une longue queue rouge et bleue."""
    flip = k.pop("flip", False)
    queue = [chemin("M -20 -40 Q -60 -10 -70 30 L -56 34 Q -44 0 -10 -30 Z", "#fa5252"),
             chemin("M -10 -36 Q -40 0 -40 40 L -28 40 Q -26 6 0 -30 Z", "#1c7ed6")]
    huppe = chemin("M -6 -108 Q -14 -134 4 -140 Q 0 -124 10 -110 Z", "#fa5252")
    return place([g(queue), oiseau(0, 0, 1.0, **{**COCO, **k}), huppe], x, y, s, flip=flip)


def biscotte(x, y, s=1.0, **k):
    return perso("chat", x, y, s, couleur=BISCOTTE, acc=("noeud",), couleur_acc="#4dabf7", **k)


def carte(x, y, s=1.0, rot=0):
    """Vieille carte au trésor ; (x, y) = son centre."""
    m = [chemin("M -110 -76 Q -60 -86 0 -78 Q 60 -70 110 -80 L 104 76 Q 50 66 0 74 Q -60 84 -106 74 Z",
                "#f3d9a4", stroke="#c69c5d", sw=4),
         chemin("M -70 -30 Q -40 -60 0 -40 Q 30 -50 50 -20 Q 70 20 30 40 Q -20 60 -50 30 Q -90 10 -70 -30 Z", "#b2f2bb"),
         chemin("M -80 50 Q -40 10 -10 20 Q 20 30 30 0", stroke="#a0522d", sw=4, stroke_dasharray="8 8"),
         trait(18, -14, 42, 10, "#e03131", 7), trait(42, -14, 18, 10, "#e03131", 7),
         chemin("M -96 -60 l 10 -6 l 4 12 Z", "#c69c5d")]
    return place(m, x, y, s, rot=rot)


def galette(x, y, s=1.0):
    m = [cercle(0, 0, 26, "#e8a15c", stroke="#c47a32", stroke_width=3)]
    for px, py in [(-9, -8), (8, -6), (0, 9), (12, 8), (-12, 8)]:
        m.append(cercle(px, py, 3, "#8d5524"))
    return place(m, x, y, s)


def longue_vue(x, y, s=1.0, rot=0):
    m = [rect(-60, -9, 50, 18, "#c69c5d", rx=4), rect(-12, -12, 44, 24, OR, rx=4), rect(30, -15, 34, 30, "#c69c5d", rx=4),
         rect(60, -15, 8, 30, OR_FONCE, rx=3)]
    return place(m, x, y, s, rot=rot)


def gouvernail(x, y, s=1.0, rot=0):
    m = []
    for k in range(8):
        a = math.radians(k * 45 + rot)
        m.append(trait(0, 0, math.cos(a) * 100, math.sin(a) * 100, "#8d5524", 12))
        m.append(cercle(math.cos(a) * 104, math.sin(a) * 104, 11, "#6d4424"))
    m += [cercle(0, 0, 72, "none", stroke="#a0693a", stroke_width=14), cercle(0, 0, 18, OR_FONCE)]
    return place(m, x, y, s)


def palmier(x, y, s=1.0, flip=False, noix=True):
    m = [chemin("M -14 0 Q -6 -150 30 -300 L 50 -296 Q 18 -150 18 0 Z", "#a0693a")]
    for k in range(6):
        m.append(trait(-10 + k * 1.5, -40 - k * 46, 18 + k * 4, -46 - k * 46, "#8d5524", 4))
    for a, l in [(-160, 140), (-120, 120), (-60, 120), (-20, 140), (-90, 90), (10, 110)]:
        r = math.radians(a)
        ex, ey = 40 + math.cos(r) * l, -300 + math.sin(r) * l * 0.7 + 30
        m.append(chemin(f"M 40 -300 Q {(40 + ex) / 2} {-330} {ex} {ey}", stroke="#2f9e44", sw=22))
    if noix:
        m += [cercle(30, -286, 12, "#6d4424"), cercle(52, -282, 12, "#6d4424")]
    return place(m, x, y, s, flip=flip)


def bateau(x, y, s=1.0, flip=False, equipage=None, rot=0):
    """La Sardine : coque, mât, voile, drapeau à sardine ; (x, y) = ligne de flottaison."""
    m = [rect(-8, -470, 16, 360, "#6d4424"),
         chemin("M 14 -440 Q 120 -360 14 -170 Z", "#f8f9fa", stroke="#dee2e6", sw=3),
         chemin("M -14 -440 Q -170 -330 -14 -170 Z", "#fff9db", stroke="#dee2e6", sw=3),
         rect(8, -470, 90, 54, "#343a40", rx=4),
         ellipse(52, -443, 28, 12, "#ced4da"), poly([(76, -443), (92, -456), (92, -430)], "#ced4da"),
         cercle(38, -446, 3, "#343a40")]
    if equipage:
        m.append(equipage)
    m += [chemin("M -270 -130 L 270 -130 Q 250 -20 180 10 L -200 10 Q -260 -30 -270 -130 Z", "#8d5524"),
          rect(-270, -140, 540, 20, "#6d4424", rx=6),
          trait(-240, -80, 230, -80, "#6d4424", 4)]
    for k in range(4):
        m.append(cercle(-150 + k * 100, -60, 14, "#ffe8cc", stroke="#6d4424", stroke_width=4))
    m.append(texte(0, -94, "LA SARDINE", 28, "#fff3bf"))
    return place(m, x, y, s, flip=flip, rot=rot)


def mer(S, y=520, ciel_haut="#74c0fc", ciel_bas="#e7f5ff", couleur="#1c7ed6", couleur2="#4dabf7"):
    ciel(S, ciel_haut, ciel_bas)
    eau(S, y, couleur, couleur2)


def ile(S, y=560, soir=False):
    if soir:
        ciel(S, "#f08c00", "#ffd8a8")
        S.add(soleil(620, 420, 70, "#ffa94d", rayons=False))
        eau(S, 460, "#1971c2", "#4dabf7")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
        eau(S, 440, "#1c7ed6", "#4dabf7")
    S.add(chemin(f"M -40 {y} Q 200 {y - 60} 420 {y - 40} Q 640 {y - 30} 840 {y} L 840 800 L -40 800 Z", "#ffe8a3"))
    for k in range(14):
        S.add(cercle(40 + (k * 97) % 740, y + 40 + (k * 53) % 180, 3, "#e8c170"))


def trou_sable(x, y, s=1.0):
    return place([ellipse(0, 0, 80, 24, "#e8c170"), ellipse(0, 2, 60, 15, "#a0693a")], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    mer(S, 560)
    S.add(soleil(680, 120, 50))
    S.add(nuage(160, 140, 0.9))
    S.add(bateau(620, 600, 0.6, equipage=g([barnabe(-100, -130, 0.8), biscotte(170, -130, 0.7)])))
    S.add(nina(280, 780, 1.55, expr="rire", bras="tient", objet=carte(112, -150, 0.5, rot=-10)))
    S.add(coco(282, 395, 0.6, expr="rire", flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 236, 170, 26, "#ffe8a3"))
    S.add(tresor(200, 240, 0.85))
    S.add(place(chapeau_pirate(), 120, 300, 0.7, rot=-14))
    S.add(coco(320, 160, 0.6, expr="rire", flip=True))
    return S


def p01():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6, chateau_x=560)
    S.add(rect(80, 640, 160, 50, "#9775fa", rx=18), couronne_objet(160, 650, 0.9))
    S.add(nina(420, 760, 1.6, princesse=True, expr="malin", bras="hanches"))
    S.add(texte(400, 100, "Assez des froufrous !", 50, "#fff", contour="#e64980"))
    return S


def p02():
    S = Scene()
    interieur(S, mur="#e6c8a0", plancher="#a0693a", y=600, plinthe="#6d4424")
    S.add(poly([(0, 0), (800, 0), (800, 120), (400, 30), (0, 120)], "#8d5524"))
    S.add(tresor(650, 700, 0.6, ouvert=False))
    S.add(nina(320, 770, 1.5, expr="fier", bras="large", objet=carte(0, -40, 0.68)))
    S.add(coco(650, 640, 0.75, expr="malin", flip=True, bec_ouvert=True))
    S.add(bulle(260, 150, 380, 90, "Rien qu'à moi !", 40, pointe=(300, 400)))
    S.add(bulle(630, 300, 300, 80, "Rien qu'à moi !", 32, pointe=(640, 500)))
    return S


def p03():
    S = Scene()
    mer(S, 560)
    S.add(soleil(110, 110, 50), nuage(700, 250, 0.6))
    S.add(bateau(400, 640, 1.0, equipage=g([
        barnabe(-170, -130, 0.95, expr="sourire"),
        nina(10, -130, 1.0, expr="rire", bras="montre"),
        biscotte(190, -130, 0.75, expr="content")])))
    S.add(coco(150, 220, 0.6, ailes="haut", expr="rire"))
    S.add(bulle(560, 70, 400, 80, "Cap sur le trésor !", 36, pointe=(470, 300)))
    return S


def p04():
    S = Scene()
    ciel(S, "#364152", "#7b8aa3")
    S.add(nuage(160, 90, 1.2, "#495057"), nuage(600, 70, 1.3, "#343a40"))
    S.add(poly([(520, 40), (480, 150), (520, 150), (470, 260), (570, 120), (530, 120), (570, 40)], "#ffe066"))
    pluie(S, 70, graine=4, couleur="#a5d8ff")
    S.add(rect(-40, 600, 880, 300, "#8d5524", transform="rotate(-6 400 650)"))
    S.add(gouvernail(400, 470, 1.1, rot=20))
    S.add(rect(388, 470, 24, 180, "#6d4424"))
    S.add(nina(250, 740, 1.4, expr="concentre", bras="donne2", regard=(1, 0)))
    S.add(barnabe(560, 720, 1.4, flip=True, expr="concentre", bras="donne2", regard=(-1, 0)))
    S.add(chemin("M -20 800 Q 120 680 240 760 Q 330 700 400 800 Z", "#1971c2"),
          chemin("M 560 800 Q 680 690 820 740 L 820 800 Z", "#1971c2"))
    S.add(texte(200, 330, "Tiens bon !", 48, "#fff", contour="#1864ab"))
    return S


def p05():
    S = Scene()
    mer(S, 600, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 140, 50))
    S.add(bateau(400, 680, 0.85, equipage=g([
        nina(-150, -130, 1.0, expr="surpris", bras="haut", regard=(1, -1)),
        barnabe(150, -130, 0.95, expr="surpris", regard=(1, -1), flip=True)])))
    S.add(carte(600, 170, 0.6, rot=20))
    S.add(coco(520, 300, 0.85, ailes="ouvertes", expr="concentre", regard=(1, -1)))
    S.add(mouvement(430, 300, 1.0, rot=0))
    S.add(texte(220, 120, "Ma carte !", 50, "#fff", contour="#1864ab"))
    return S


def p06():
    S = Scene()
    ile(S)
    S.add(palmier(120, 600, 1.0), palmier(640, 560, 1.4, flip=True), palmier(300, 540, 0.7))
    S.add(trou_sable(560, 690, 1.0))
    S.add(biscotte(560, 680, 1.1, expr="concentre", bras="porte", regard=(0, 1)))
    S.add(nina(250, 780, 1.2, expr="surpris", bras="bas", regard=(1, 0)))
    S.add(coco(110, 680, 0.6, expr="sourire"))
    S.add(bulle(560, 160, 320, 90, "Miaou ! C'est ici !", 32, pointe=(580, 450)))
    return S


def p07():
    S = Scene()
    ile(S)
    S.add(palmier(720, 560, 1.2, flip=True))
    S.add(tresor(520, 720, 1.0, ouvert=False))
    S.add(crabe(520, 620, 2.2, CRABE, expr="furieux"))
    S.add(nina(170, 780, 1.25, expr="timide", bras="joues", regard=(1, 0)))
    S.add(coco(150, 470, 0.6, expr="oups"))
    S.add(bulle(400, 100, 640, 120, "Clac ! Clac ! Ce trésor est à moi,\nrien qu'à moi !", 34, pointe=(520, 280)))
    return S


def p08():
    S = Scene()
    ile(S)
    S.add(tresor(620, 720, 0.9, ouvert=False))
    S.add(crabe(620, 630, 1.8, CRABE, expr="inquiet", pinces_haut=False, ))
    S.add(barnabe(80, 690, 0.85, expr="inquiet"), biscotte(190, 690, 0.65, expr="inquiet"))
    S.add(panier(160, 790, 1.0, "galette"))
    S.add(nina(330, 780, 1.3, expr="timide", bras="donne", regard=(1, 0), objet=galette(84, -100, 0.9)))
    S.add(bulle(400, 100, 560, 90, "Tu veux partager notre goûter ?", 34, pointe=(360, 400)))
    return S


def p09():
    S = Scene()
    ile(S)
    S.add(palmier(90, 560, 1.1))
    S.add(tresor(260, 740, 0.9, ouvert=False))
    S.add(crabe(560, 700, 2.0, CRABE, expr="miam"))
    S.add(galette(560, 660, 1.4))
    S.add(nina(260, 620, 1.0, expr="rire", bras="haut"))
    S.add(bulle(500, 110, 560, 120, "Personne n'avait jamais\nrien partagé avec moi !", 34, pointe=(560, 420)))
    return S


def p10():
    S = Scene()
    ile(S)
    S.add(palmier(720, 560, 1.2, flip=True))
    S.add(tresor(400, 640, 1.3))
    S.add(eclat(400, 420, 1.6, OR))
    S.add(nina(580, 790, 1.2, expr="bouche_bee", bras="pense", regard=(-1, 0)))
    S.add(barnabe(140, 780, 1.05, expr="sourire", regard=(1, 0)))
    S.add(biscotte(290, 790, 0.7, expr="sourire", regard=(1, 0)))
    S.add(coco(140, 470, 0.6, expr="sourire", ailes="haut"))
    S.add(texte(400, 110, "Rien qu'à… ?", 56, "#fff", contour="#e03131"))
    return S


def p11():
    S = Scene()
    ile(S)
    S.add(tresor(400, 560, 0.8))
    S.add(barnabe(120, 770, 1.1, expr="rire", bras="tient", objet=longue_vue(70, -150, 0.7, rot=-30)))
    S.add(nina(340, 790, 1.2, expr="rire", bras="ouverts"))
    S.add(biscotte(505, 790, 0.8, expr="content", bras="porte", objet=grelot(0, -80, 0.8, brille=False)))
    S.add(crabe(655, 775, 1.1, CRABE, expr="rire"))
    for k in range(12):
        a = math.radians(k * 30)
        S.add(cercle(655 + 94 * 1.1 + math.cos(a) * 26, 775 - 100 * 1.1 + math.sin(a) * 30, 7, "#f8f9fa", stroke="#ced4da", stroke_width=1.5))
    S.add(coco(620, 300, 0.7, expr="rire", ailes="haut"))
    S.add(couronne_objet(620, 226, 0.5))
    S.add(bulle(330, 100, 420, 90, "À nous ! À nous !", 40, pointe=(560, 230)))
    return S


def p12():
    S = Scene()
    ile(S, soir=True)
    S.add(bateau(640, 500, 0.35))
    S.add(flammes(430, 730, 1.0, graine=3))
    S.add(barnabe(110, 760, 1.0, expr="chante"))
    S.add(nina(270, 780, 1.1, expr="rire", bras="haut"))
    S.add(biscotte(560, 780, 0.75, expr="rire", bras="haut"))
    S.add(crabe(695, 790, 0.85, CRABE, expr="rire"))
    S.add(coco(400, 360, 0.6, expr="chante", ailes="haut"))
    S.add(notes(480, 330, 1.0, "#fff"), coeur(320, 300, 1.0), coeur(560, 250, 0.8, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("coffre.svg", vignette),
    ("01-assez-des-froufrous.svg", p01), ("02-la-carte.svg", p02), ("03-la-sardine.svg", p03),
    ("04-tempete.svg", p04), ("05-coco.svg", p05), ("06-biscotte.svg", p06),
    ("07-crabe-geant.svg", p07), ("08-le-gouter.svg", p08), ("09-une-galette.svg", p09),
    ("10-le-coffre.svg", p10), ("11-a-nous.svg", p11), ("12-la-fete.svg", p12),
]
