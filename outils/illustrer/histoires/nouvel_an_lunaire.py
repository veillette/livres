"""Le dragon du Nouvel An — le Nouvel An lunaire avec Mei et Nainai.

Le Nouvel An lunaire tombe à une nouvelle lune, entre la fin janvier et la
mi-février : c'est la fête du Printemps. On balaie la maison, on découpe des
papiers rouges, on accroche des lanternes ; on plie des raviolis et on dîne
en famille (le poisson, pour l'abondance) ; les grands-parents donnent des
enveloppes rouges. La légende de Nian, le monstre qui avait peur du rouge,
du bruit et de la lumière. Danse du dragon, danse du lion qui « mange » la
laitue. Quinze jours plus tard, à la pleine lune, la fête des lanternes.

Plans : 1 moyen (le grand ménage) · 2 gros plan (les papiers découpés) ·
3 large (la rue en rouge) · 4 moyen (les raviolis) · 5 large (le dîner) ·
6 gros plan (l'enveloppe rouge) · 7 large (la légende de Nian) · 8 large
(la danse du dragon) · 9 gros plan (le lion et la laitue) · 10 large (la
fête des lanternes, pleine lune).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from fetes import feu_artifice, confettis
from contes import balai

ID = "nouvel-an-lunaire"
PAPIER_PEINT = "fleurs"

ROUGE = "#e03131"
OR_ = "#fcc419"
MEI = dict(peau="claire", cheveux="noir", coiffure="carre", habit=ROUGE, motif_robe=OR_, nez="petit")
NAINAI = dict(stature="ancien", peau="claire", cheveux="gris", coiffure="chignon", habit="#5f3dc4", carrure="fine")
PAPA = dict(stature="adulte", peau="claire", cheveux="noir", coiffure="raie", habit="#1c7ed6", robe=False, jambes="#343a40", acc=("lunettes",))
MAMAN = dict(stature="adulte", peau="claire", cheveux="noir", coiffure="queue", habit="#2f9e44", robe=False, jambes="#343a40")
YEYE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#862e9c", robe=False, jambes="#343a40", barbe="#e9ecef")


def mei(x, y, s=1.2, **k):
    return personne(x, y, s, **{**MEI, **k})


def lanterne_rouge(x, y, s=1.0, allumee=False, S=None):
    """Lanterne ronde rouge à pompon doré ; (x, y) = l'attache."""
    corps = radial(["#fff3bf", "#ff8787", ROUGE]) if allumee else volume(ROUGE, 0.3, 0.75)
    m = [trait(0, 0, 0, 20, "#495057", 3), rect(-26, 20, 52, 12, OR_, rx=3), ellipse(0, 72, 60, 46, corps)]
    for dx in (-30, 0, 30):
        m.append(chemin(f"M {dx * 0.4} 30 Q {dx * 1.5} 72 {dx * 0.4} 114", stroke="#c92a2a", sw=2.5, opacity=0.6))
    m += [rect(-26, 112, 52, 12, OR_, rx=3), chemin("M -8 124 L -12 170 M 0 124 L 0 174 M 8 124 L 12 170", stroke=OR_, sw=4)]
    if allumee and S is not None:
        S.lumiere(x, y + 72 * s, 110 * s, "#ffd43b", 0.6)
    return place(m, x, y, s)


def lanterne_lapin(x, y, s=1.0, S=None):
    """Petite lanterne en forme de lapin, au bout d'un bâton ; (x, y) = le lapin."""
    m = [ellipse(0, 0, 50, 34, radial(["#fff", "#fff0f6", "#fcc2d7"])), cercle(40, -20, 22, "#fff0f6"),
         ellipse(34, -54, 8, 24, "#fff0f6", rot=-10), ellipse(50, -52, 8, 24, "#fff0f6", rot=12),
         cercle(48, -24, 3, ENCRE), ellipse(-4, 34, 50, 6, "#ff8787")]
    if S is not None:
        S.lumiere(x, y, 90 * s, "#ffd43b", 0.6)
    return place(m, x, y, s)


def papier_decoupe(x, y, s=1.0, couleur=ROUGE, rot=45):
    """Papier rouge découpé en losange, motif de fleur ajourée ; (x, y) = centre."""
    m = [rect(-60, -60, 120, 120, couleur, rx=4)]
    for k in range(8):
        a = math.radians(k * 45)
        m.append(ellipse(math.cos(a) * 30, math.sin(a) * 30, 12, 6, "#fff4e6", rot=k * 45))
    m.append(cercle(0, 0, 12, "#fff4e6"))
    m.append(rect(-50, -50, 100, 100, "none", rx=3, stroke="#fff4e6", stroke_width=3))
    return place(m, x, y, s, rot=rot)


def ravioli(x, y, s=1.0, rot=0):
    return place([chemin("M -30 6 Q -32 -22 0 -24 Q 32 -22 30 6 Q 0 14 -30 6 Z", volume("#fff4e6", 0.35, 0.85), stroke="#e9d8a6", sw=2),
                  chemin("M -20 -12 q 5 -6 10 0 q 5 -6 10 0 q 5 -6 10 0", stroke="#e9d8a6", sw=2)], x, y, s, rot=rot)


def enveloppe_rouge(x, y, s=1.0, rot=0):
    return place([rect(-40, -60, 80, 120, volume(ROUGE, 0.3, 0.8), rx=6), rect(-30, -40, 60, 30, OR_, rx=4),
                  cercle(0, 20, 16, "none", stroke=OR_, stroke_width=4), cercle(0, 20, 6, OR_)], x, y, s, rot=rot)


def poisson_plat(x, y, s=1.0):
    return place([ellipse(0, 6, 120, 28, "#fff", stroke="#dee2e6", stroke_width=3),
                  ellipse(-6, 0, 80, 26, volume("#ff922b", 0.4, 0.75)), poly([(70, 0), (110, -24), (110, 24)], "#ff922b"),
                  cercle(-56, -6, 5, ENCRE), chemin("M -20 -14 q 10 14 0 28 M 10 -16 q 10 16 0 32", stroke="#e8590c", sw=2)], x, y, s)


def dragon_danse(x, y, s=1.0, graine=1):
    """Dragon de la danse du dragon, porté sur des bâtons par des danseurs ; (x, y) = sol sous la tête."""
    r = random.Random(graine)
    m = []
    pts = []
    for k in range(10):
        px = -k * 70
        py = -250 + math.sin(k * 0.8) * 60
        pts.append((px, py))
    for k, (px, py) in enumerate(pts):
        if k % 2 == 0:
            m.append(trait(px, py + 40, px, -100, "#8d5524", 6))
            m.append(personne(px, 0, 0.55, peau=r.choice(("claire", "doree", "rosee")), cheveux="noir", coiffure="courts",
                              habit=OR_ if k % 4 else ROUGE, robe=False, jambes="#343a40", bras="haut", expr="joie", ombre=False))
    for k in reversed(range(len(pts))):
        px, py = pts[k]
        rr = 50 - k * 2
        m.append(cercle(px, py, rr, volume(ROUGE if k % 2 else OR_, 0.35, 0.8)))
        m.append(poly([(px - 14, py - rr), (px, py - rr - 26), (px + 14, py - rr)], "#2f9e44"))
    # tête
    hx, hy = 40, -270
    m += [ellipse(hx, hy, 90, 70, volume(ROUGE, 0.35, 0.8)), ellipse(hx + 60, hy + 20, 50, 34, volume(OR_, 0.4, 0.8)),
          cercle(hx + 6, hy - 30, 22, "#fff"), cercle(hx + 12, hy - 28, 10, ENCRE), cercle(hx + 50, hy - 26, 18, "#fff"), cercle(hx + 54, hy - 24, 8, ENCRE),
          chemin(f"M {hx - 20} {hy - 60} Q {hx - 60} {hy - 120} {hx - 90} {hy - 110}", stroke=OR_, sw=10),
          chemin(f"M {hx + 30} {hy - 64} Q {hx + 40} {hy - 130} {hx + 10} {hy - 140}", stroke=OR_, sw=10),
          chemin(f"M {hx + 80} {hy + 40} Q {hx + 40} {hy + 60} {hx} {hy + 44}", stroke="#fff", sw=8),
          chemin(f"M {hx - 70} {hy + 20} q -30 30 -10 60 M {hx - 50} {hy + 40} q -20 30 0 60", stroke=OR_, sw=6)]
    m.append(trait(hx, hy + 60, hx, -100, "#8d5524", 6))
    m.append(personne(hx, 0, 0.55, peau="doree", cheveux="noir", coiffure="courts", habit=ROUGE, robe=False, jambes="#343a40",
                      bras="haut", expr="rire", ombre=False))
    return place(m, x, y, s) + occuper(x - 680 * s, y - 420 * s, x + 160 * s, y)


def lion_danse(x, y, s=1.0, bouche=True):
    """Tête du lion de la danse du lion, portée par un danseur ; (x, y) = sol."""
    m = [rect(-120, -220, 240, 120, volume(OR_, 0.3, 0.8), rx=40)]
    for k in range(9):
        a = math.radians(-180 + k * 22.5)
        m.append(cercle(math.cos(a) * 140, -300 + math.sin(a) * 110, 30, "#fff"))
    m += [ellipse(0, -300, 140, 110, volume(ROUGE, 0.35, 0.8)), cercle(0, -420, 26, "#2f9e44"),
          ellipse(-50, -330, 34, 28, "#fff"), ellipse(50, -330, 34, 28, "#fff"), cercle(-46, -326, 14, ENCRE), cercle(54, -326, 14, ENCRE),
          rect(-70, -380, 50, 14, "#fff", rx=7), rect(20, -380, 50, 14, "#fff", rx=7),
          ellipse(0, -282, 34, 22, OR_)]
    if bouche:
        m += [chemin("M -90 -250 Q 0 -150 90 -250 Q 0 -200 -90 -250 Z", "#c92a2a"), rect(-60, -244, 120, 10, "#fff", rx=5)]
    m += [rect(-40, -110, 30, 110, "#343a40", rx=10), rect(10, -110, 30, 110, "#343a40", rx=10),
          ellipse(-26, -4, 26, 10, "#212529"), ellipse(26, -4, 26, 10, "#212529")]
    return place(m, x, y, s) + occuper(x - 170 * s, y - 450 * s, x + 170 * s, y)


def laitue(x, y, s=1.0):
    return place([trait(0, -120, 0, 0, "#495057", 3), cercle(0, 20, 38, volume("#8ce99a", 0.4, 0.75)), cercle(-18, 10, 22, "#69db7c"),
                  cercle(18, 14, 22, "#51cf66"), enveloppe_rouge(0, 60, 0.4)], x, y, s)


def maison_dedans(S, y=600, nuit_=False):
    piece(S, "manoir", y)
    if nuit_:
        S.ambiance("nuit")


def rue(S, y=640, nuit_=False):
    if nuit_:
        nuit(S, "#1c2a52", "#4c5b9a")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    for k, (bx, coul) in enumerate(((0, "#ffe3e3"), (210, "#fff3bf"), (420, "#ffe8cc"), (620, "#e5dbff"))):
        S.add(immeuble(bx, y - 40, 180, 3, coul, "pignon" if k % 2 else "mansarde", toit_c="#c92a2a" if k % 2 else None,
                       rdc="boutique", store=ROUGE, graine=k + 3, lumiere=nuit_))
    S.add(rect(0, y - 40, 800, 840 - y, "#ced4da"), rect(0, y - 44, 800, 6, "#adb5bd"))
    for x in (64, 736, 150, 650):
        S.proposer_cachette(x, y + 40)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue(S, 640, nuit_=True)
    S.add(feu_artifice(150, 140, 80, OR_), feu_artifice(650, 110, 70, "#ff8787"))
    for k, x in enumerate((90, 290, 510, 710)):
        S.add(lanterne_rouge(x, 230, 0.7, allumee=True, S=S))
    S.add(dragon_danse(480, 760, 0.9))
    S.add(mei(680, 790, 1.3, expr="rire", bras="haut", regard=(-1, -0.3)))
    S.cachette(630, 320, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lanterne_rouge(120, 30, 1.0), lanterne_rouge(280, 30, 1.0))
    S.add(enveloppe_rouge(200, 180, 0.9, rot=-8))
    return S


def p01():
    """Plan moyen : avant la fête, on fait le grand ménage : on balaie la malchance."""
    S = Scene()
    maison_dedans(S)
    S.add(fenetre(470, 90, 200, 160, "#a5d8ff", rideaux=ROUGE, contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), nuage(560, 170, 0.4)])))
    S.add(mei(260, 790, 1.35, expr="rire", bras="tient", regard=(1, 0.3), robe=False, jambes="#495057",
              objet=balai(76, -30, 0.95, rot=6)))
    S.add(personne(560, 790, 1.4, expr="content", bras="porte", regard=(-1, 0), objet=place(rect(-40, -30, 80, 50, "#74c0fc", rx=6), *ancre(0, -74, "porte", "adulte")), **MAMAN))
    for k in range(5):
        S.add(cercle(380 + k * 18, 760 - (k % 2) * 10, 5, "#adb5bd", opacity=0.7))
    S.add(bulle(400, 140, 460, 100, "On balaie la malchance !", 34, pointe=(300, 440)))
    return S


def p02():
    """Gros plan : Mei et Nainai découpent des papiers rouges."""
    S = Scene()
    maison_dedans(S)
    S.add(table(400, 790, 500, 160, "#c68642"))
    S.add(personne(260, 640, 1.2, expr="concentre", bras="porte", regard=(1, 0.5), **NAINAI))
    S.add(mei(540, 640, 1.1, expr="joie", bras="donne", flip=True, regard=(-1, 0.3), objet=papier_decoupe(96, -110, 0.6)))
    S.add(table(400, 790, 500, 160, "#c68642"))
    S.add(papier_decoupe(320, 600, 0.5, rot=10), papier_decoupe(420, 610, 0.4, rot=-20))
    S.camera(1.3, 400, 520)
    S.dessus(texte(400, 110, "Du papier rouge, pour la chance !", 40, ROUGE, contour="#fff"))
    return S


def p03():
    """Plan large : la rue est toute rouge ; lanternes, papiers découpés aux fenêtres."""
    S = Scene()
    rue(S, 640)
    for k, x in enumerate((90, 250, 410, 570, 730)):
        S.add(lanterne_rouge(x, 120 + (k % 2) * 30, 0.6))
    S.add(trait(0, 120, 800, 140, "#495057", 3))
    for x in (60, 270, 480, 690):
        S.add(papier_decoupe(x + 50, 460, 0.3))
    S.add(mei(330, 790, 1.15, expr="bouche_bee", bras="ouverts", regard=(0, -0.6)))
    S.add(personne(470, 790, 1.3, expr="content", bras="main", flip=True, regard=(-1, 0), **PAPA))
    return S


def p04():
    """Plan moyen : toute la famille plie des raviolis ; Nainai montre comment."""
    S = Scene()
    maison_dedans(S)
    S.add(personne(180, 650, 1.15, expr="content", bras="porte", regard=(1, 0.4), **NAINAI))
    S.add(mei(400, 650, 1.05, expr="concentre", bras="porte", regard=(0, 0.5)))
    S.add(personne(620, 650, 1.15, expr="rire", bras="porte", regard=(-1, 0.4), **PAPA))
    S.add(table(400, 790, 640, 160, "#c68642", nappe="#fff4e6"))
    for k in range(9):
        S.add(ravioli(180 + k * 55, 615 + (k % 2) * 8, 0.8, rot=(k % 3 - 1) * 10))
    S.add(bulle(250, 140, 400, 90, "On plie, on pince…", 34, pointe=(200, 380)))
    return S


def p05():
    """Plan large : le soir du réveillon, toute la famille dîne autour de la table ronde."""
    S = Scene()
    maison_dedans(S, nuit_=True)
    S.add(lanterne_rouge(400, 40, 0.7, allumee=True, S=S))
    S.add(personne(120, 660, 1.0, expr="rire", bras="bas", regard=(1, 0.3), **YEYE))
    S.add(personne(260, 640, 1.0, expr="content", bras="bas", regard=(1, 0.3), **NAINAI))
    S.add(mei(400, 650, 0.95, expr="miam", bras="porte", regard=(0, 0.4)))
    S.add(personne(540, 640, 1.0, expr="joie", bras="bas", regard=(-1, 0.3), **MAMAN))
    S.add(personne(680, 650, 1.0, expr="rire", bras="bas", regard=(-1, 0.3), **PAPA))
    S.add(ellipse(400, 690, 360, 70, volume("#c92a2a", 0.3, 0.8)), ellipse(400, 680, 340, 60, "#fff4e6"))
    S.add(poisson_plat(400, 680, 0.9))
    for k in range(6):
        S.add(ravioli(180 + k * 30, 690 - (k % 2) * 10, 0.6), ravioli(560 + k * 30, 690 - (k % 2) * 10, 0.6))
    S.add(rect(0, 760, 800, 40, "#6d4424"))
    S.add(texte(400, 210, "Le réveillon !", 56, OR_, contour="#c92a2a"))
    return S


def p06():
    """Gros plan : Nainai donne une enveloppe rouge à Mei : « Xin nian kuai le ! »."""
    S = Scene()
    maison_dedans(S, nuit_=True)
    S.add(lanterne_rouge(150, 60, 0.6, allumee=True, S=S))
    S.add(personne(280, 820, 1.7, expr="content", bras="donne", regard=(1, 0.2),
                   objet=enveloppe_rouge(*ancre(96, -100, "donne", "ancien"), 0.8, rot=-10), **NAINAI))
    S.add(mei(570, 820, 1.6, expr="rire", bras="tend", flip=True, regard=(-1, 0)))
    S.camera(1.2, 420, 500)
    S.dessus(bulle(400, 110, 520, 100, "Xin nian kuai le !\nBonne année !", 34, pointe=S.vers_page(300, 470)))
    S.cachette(145, 267, "air")
    return S


def p07():
    """Plan large : la légende : Nian, le monstre, s'enfuit devant le rouge, le bruit et la lumière des pétards."""
    S = Scene()
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 30, 7, (0, 0, 800, 400))
    S.add(rect(0, 640, 800, 160, "#495057"))
    for k, x in enumerate((140, 260)):
        S.add(maison(x, 640, 0.8, mur="#fff4e6", toit=ROUGE, lumiere=True, cote=False))
    for x in (120, 240, 360):
        S.add(lanterne_rouge(x, 330, 0.45, allumee=True, S=S))
    S.add(feu_artifice(330, 520, 60, OR_), feu_artifice(420, 600, 40, "#ff8787"))
    S.add(perso("lion", 620, 780, 1.3, couleur="#4c6ef5", visage="#d0ebff", expr="oups", bras="court", flip=True, regard=(1, 0)))
    S.add(poly([(620, 780 - 230 * 1.3), (630, 780 - 290 * 1.3), (646, 780 - 226 * 1.3)], "#fff3bf"))
    S.add(texte(420, 160, "Bang ! Boum !", 52, OR_, contour=ROUGE))
    S.add(bulle(620, 290, 260, 80, "Au secours !", 30, pointe=(620, 450)))
    return S


def p08():
    """Plan large : le jour de l'An, la danse du dragon défile dans la rue."""
    S = Scene()
    rue(S, 640)
    for k, x in enumerate((90, 250, 410, 570, 730)):
        S.add(lanterne_rouge(x, 120 + (k % 2) * 30, 0.6))
    S.add(confettis(0, 200, 800, 520, 40, 3, (ROUGE, OR_, "#ff8787", "#fff")))
    S.add(dragon_danse(520, 780, 0.95, graine=4))
    S.add(mei(720, 790, 1.0, expr="rire", bras="applaudit", regard=(-1, -0.3)))
    S.cachette(730, 260, "air")
    return S


def p09():
    """Gros plan : la tête du lion « mange » la laitue suspendue à la porte du magasin."""
    S = Scene()
    rue(S, 660)
    S.add(laitue(600, 130, 1.1))
    S.add(lion_danse(470, 790, 1.15))
    S.add(mei(160, 800, 1.3, expr="bouche_bee", bras="joues", regard=(1, -0.4)))
    S.camera(1.15, 420, 470)
    S.dessus(texte(230, 140, "Miam, miam !", 52, ROUGE, contour="#fff"))
    S.cachette(707, 652, "air")
    return S


def p10():
    """Plan large : quinze jours plus tard, à la pleine lune, la fête des lanternes."""
    S = Scene()
    nuit(S, "#1c2a52", "#4c5b9a")
    etoiles(S, 30, 9, (0, 0, 800, 380))
    S.add(lune(620, 130, 54))
    S.add(rect(0, 620, 800, 180, "#343a40"))
    for k, x in enumerate((60, 200, 340, 480, 620, 760)):
        S.add(lanterne_rouge(x, 240 + (k % 2) * 40, 0.55, allumee=True, S=S))
    S.add(trait(0, 240, 800, 280, "#868e96", 2))
    S.add(personne(220, 790, 1.3, expr="content", bras="main", regard=(1, 0), **MAMAN))
    S.add(mei(430, 790, 1.15, expr="rire", bras="tient", regard=(1, -0.4),
              objet=g([trait(68, -146, 140, -260, "#8d5524", 4), lanterne_lapin(150, -270, 0.6)])))
    S.lumiere(430 + 150 * 1.15, 790 - 270 * 1.15, 90, "#ffd43b", 0.7)
    S.add(texte(320, 140, "La fête des lanternes", 44, OR_, contour=ROUGE))
    S.cachette(740, 700)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lanternes-seules.svg", vignette),
    ("01-le-grand-menage.svg", p01), ("02-papiers-rouges.svg", p02), ("03-la-rue-rouge.svg", p03),
    ("04-les-raviolis.svg", p04), ("05-le-reveillon.svg", p05), ("06-l-enveloppe-rouge.svg", p06),
    ("07-la-legende-de-nian.svg", p07), ("08-la-danse-du-dragon.svg", p08), ("09-le-lion.svg", p09),
    ("10-la-fete-des-lanternes.svg", p10),
]
