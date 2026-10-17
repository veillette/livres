"""L'enveloppe rouge de Lin — le Nouvel An lunaire, et la chance qu'on partage.

Au matin du Nouvel An lunaire, Nainai offre à Lin une enveloppe rouge (on la
donne et on la reçoit à deux mains) : vingt dollars, juste le prix du
cerf-volant dragon de la vitrine. Mais dans la rue en fête, Lin voit Madame
Wong, seule derrière une fenêtre sans lanterne. Avec son argent, elle achète
des mandarines (qui portent chance) et une lanterne rouge, et les offre à la
vieille dame. Madame Wong sort de sa malle le vieux cerf-volant dragon de son
fils. Le Nouvel An lunaire est le décor ; l'histoire parle de générosité.

Plans : 1 moyen (l'enveloppe) · 2 gros plan (vingt dollars) · 3 moyen (le
rêve) · 4 large (la rue en fête) · 5 moyen (la vitrine) · 6 moyen (Madame
Wong à sa fenêtre) · 7 gros plan (Lin réfléchit) · 8 moyen (les mandarines) ·
9 moyen (bonne année !) · 10 large (la lanterne) · 11 gros plan (le vieux
dragon) · 12 large (au parc).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import cerf_volant_losange
from objets import ballon_jeu

ID = "enveloppe-rouge"
PAPIER_PEINT = "fleurs"

ROUGE = "#e03131"
OR_ = "#fcc419"
NEIGE = "#f8f9fa"

LIN = dict(peau="claire", cheveux="noir", coiffure="carre", habit=ROUGE, motif_robe=OR_, yeux="cils", nez="petit")
NAINAI = dict(stature="ancien", peau="claire", cheveux="gris", coiffure="chignon", habit="#5f3dc4", carrure="fine", nez="petit")
YEYE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#1971c2", robe=False, jambes="#343a40",
            barbe="#e9ecef", acc=("lunettes",), nez="rond")
WONG = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="boucles", habit="#2b8a3e", carrure="ronde", nez="rond",
            acc=("lunettes",))
MARCHAND = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#f08c00", robe=False, jambes="#495057",
                carrure="ronde")


def tuque(c="#e03131", c2="#ffffff"):
    return g([chemin("M -54 -178 Q -56 -240 0 -242 Q 56 -240 54 -178 Z", volume(c, 0.3, 0.75)),
              rect(-58, -194, 116, 22, c2, rx=10), cercle(0, -250, 16, c2)])


def lin(x, y, s=1.15, dehors=False, **k):
    if dehors:
        k = {"coiffe": tuque(ROUGE, OR_), "habit": "#c92a2a", **k}
    return personne(x, y, s, **{**LIN, **k})


def nainai(x, y, s=1.15, **k):
    return personne(x, y, s, **{**NAINAI, **k})


def yeye(x, y, s=1.15, dehors=False, **k):
    if dehors:
        k = {"coiffe": tuque("#1864ab"), **k}
    return personne(x, y, s, **{**YEYE, **k})


def wong(x, y, s=1.15, **k):
    return personne(x, y, s, **{**WONG, **k})


def enveloppe_rouge(x, y, s=1.0, rot=0, ouverte=False):
    """Enveloppe rouge du Nouvel An, décorée d'or ; ouverte : le billet dépasse."""
    m = []
    if ouverte:
        m.append(billet(0, -70, 0.9))
    m += [rect(-40, -60, 80, 120, volume(ROUGE, 0.3, 0.8), rx=6), rect(-30, -40, 60, 30, OR_, rx=4),
          cercle(0, 20, 16, "none", stroke=OR_, stroke_width=4), cercle(0, 20, 6, OR_)]
    return place(m, x, y, s, rot=rot)


def billet(x, y, s=1.0, rot=0):
    """Billet vert de vingt dollars ; (x, y) = centre."""
    return place([rect(-70, -34, 140, 68, "#b2f2bb", rx=4, stroke="#2f9e44", stroke_width=3),
                  rect(-58, -24, 116, 48, "none", rx=3, stroke="#69db7c", stroke_width=2),
                  texte(-36, 10, "20", 30, "#2b8a3e"), cercle(32, 0, 16, "#8ce99a"), texte(32, 6, "$", 18, "#2b8a3e")], x, y, s, rot=rot)


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


def papier_decoupe(x, y, s=1.0, couleur=ROUGE, rot=45):
    """Papier rouge découpé en losange, motif de fleur ajourée ; (x, y) = centre."""
    m = [rect(-60, -60, 120, 120, couleur, rx=4)]
    for k in range(8):
        a = math.radians(k * 45)
        m.append(ellipse(math.cos(a) * 30, math.sin(a) * 30, 12, 6, "#fff4e6", rot=k * 45))
    m += [cercle(0, 0, 12, "#fff4e6"), rect(-50, -50, 100, 100, "none", rx=3, stroke="#fff4e6", stroke_width=3)]
    return place(m, x, y, s, rot=rot)


def mandarine(x, y, s=1.0):
    return place([cercle(0, 0, 18, volume("#ff922b", 0.4, 0.75)), ellipse(8, -18, 10, 5, "#2f9e44", rot=-30), cercle(-6, -6, 4, "#fff", opacity=0.4)], x, y, s)


def filet_mandarines(x, y, s=1.0):
    """Filet de mandarines avec leurs feuilles ; (x, y) = la poignée."""
    m = [chemin("M -10 0 Q 0 -14 10 0", stroke="#e03131", sw=4)]
    for k, (px, py) in enumerate(((-24, 40), (0, 36), (24, 40), (-12, 64), (12, 64), (0, 88))):
        m.append(mandarine(px, py, 1.0))
    m.append(chemin("M -40 30 Q 0 120 40 30 M -30 30 L 30 90 M 30 30 L -30 90 M 0 20 V 104", stroke="#e03131", sw=2, opacity=0.7))
    return place(m, x, y, s)


def cerf_volant_dragon(x, y, s=1.0, passe=False, fil_vers=None, rot=0, longueur=8):
    """Cerf-volant dragon : tête rouge et dorée, longue queue d'anneaux de
    couleur ; passe : couleurs un peu fanées (le vieux cerf-volant). (x, y) = tête."""
    rouge, or_ = ("#e8787a", "#f3d27a") if passe else (ROUGE, OR_)
    m = []
    if fil_vers:
        m.append(chemin(f"M {n(x)} {n(y + 40 * s)} Q {n((x + fil_vers[0]) / 2)} {n(max(y, fil_vers[1]) + 30)} {n(fil_vers[0])} {n(fil_vers[1])}",
                        stroke="#495057", sw=2))
    d = []
    pts = [(-k * 46, math.sin(k * 0.9) * 26 + k * 8) for k in range(longueur + 1)]
    d.append(chemin("M " + " L ".join(f"{n(px)} {n(py)}" for px, py in pts), stroke=or_, sw=4))
    qx, qy = pts[-1]
    d += [chemin(f"M {n(qx)} {n(qy)} q -40 10 -70 40", stroke=rouge, sw=8), chemin(f"M {n(qx)} {n(qy)} q -50 -6 -80 14", stroke=or_, sw=8)]
    for k in range(longueur, 0, -1):
        px, py = pts[k]
        rr = 26 - k * 1.4
        c = rouge if k % 2 else or_
        d.append(poly([(px - rr * 0.6, py - rr * 0.8), (px, py - rr * 1.6), (px + rr * 0.6, py - rr * 0.8)], or_ if k % 2 else rouge))
        d.append(rect(px - rr * 0.9, py - rr, rr * 1.8, rr * 2, volume(c, 0.35, 0.8), rx=rr * 0.5, stroke=_assombrir(c, 0.8), stroke_width=2))
        d.append(chemin(f"M {n(px - rr * 0.6)} {n(py - rr * 0.2)} Q {n(px)} {n(py + rr * 0.3)} {n(px + rr * 0.6)} {n(py - rr * 0.2)}",
                        stroke=_assombrir(c, 0.75), sw=2))
    d += [ellipse(0, 0, 52, 40, volume(rouge, 0.35, 0.8)), ellipse(34, 12, 30, 20, volume(or_, 0.4, 0.8)),
          cercle(-6, -14, 13, "#fff"), cercle(-2, -12, 6, ENCRE), cercle(24, -14, 11, "#fff"), cercle(27, -12, 5, ENCRE),
          chemin("M -20 -34 Q -46 -74 -64 -66", stroke=or_, sw=7), chemin("M 14 -38 Q 20 -80 0 -88", stroke=or_, sw=7),
          chemin("M 50 20 Q 24 34 0 24", stroke="#fff", sw=5)]
    m.append(place(d, x, y, s, rot=rot))
    return g(m)


def lion_danse(x, y, s=1.0):
    """Tête du lion de la danse du lion, portée par un danseur ; (x, y) = sol."""
    m = [rect(-120, -220, 240, 120, volume(OR_, 0.3, 0.8), rx=40)]
    for k in range(9):
        a = math.radians(-180 + k * 22.5)
        m.append(cercle(math.cos(a) * 140, -300 + math.sin(a) * 110, 30, "#fff"))
    m += [ellipse(0, -300, 140, 110, volume(ROUGE, 0.35, 0.8)), cercle(0, -420, 26, "#2f9e44"),
          ellipse(-50, -330, 34, 28, "#fff"), ellipse(50, -330, 34, 28, "#fff"), cercle(-46, -326, 14, ENCRE), cercle(54, -326, 14, ENCRE),
          rect(-70, -380, 50, 14, "#fff", rx=7), rect(20, -380, 50, 14, "#fff", rx=7), ellipse(0, -282, 34, 22, OR_),
          chemin("M -90 -250 Q 0 -150 90 -250 Q 0 -200 -90 -250 Z", "#c92a2a"), rect(-60, -244, 120, 10, "#fff", rx=5),
          rect(-40, -110, 30, 110, "#343a40", rx=10), rect(10, -110, 30, 110, "#343a40", rx=10),
          ellipse(-26, -4, 26, 10, "#212529"), ellipse(26, -4, 26, 10, "#212529")]
    return place(m, x, y, s) + occuper(x - 170 * s, y - 450 * s, x + 170 * s, y)


def tambour(x, y, s=1.0):
    return place([ellipse(0, -80, 60, 18, "#fff4e6"), rect(-60, -80, 120, 80, volume(ROUGE, 0.3, 0.75)), ellipse(0, 0, 60, 18, "#c92a2a"),
                  *[cercle(-48 + k * 24, -40, 4, OR_) for k in range(5)]], x, y, s)


def salon(S, y=600):
    """Le salon de la famille de Lin, décoré pour le Nouvel An."""
    piece(S, "manoir", y)
    S.ambiance("interieur")
    S.add(fenetre(560, 100, 170, 150, "#d0ebff", rideaux=ROUGE,
                  contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 200, 800, 100, NEIGE)])))
    S.add(papier_decoupe(640, 175, 0.4))
    for lx in (120, 320):
        S.add(lanterne_rouge(lx, 0, 0.8))


def rue(S, y=640):
    """La rue du quartier chinois, sous la neige, pleine de lanternes."""
    ciel(S, "#a5d8ff", "#f1f3f5")
    for k, (bx, coul) in enumerate(((0, "#ffe3e3"), (210, "#fff3bf"), (420, "#ffe8cc"), (620, "#e5dbff"))):
        S.add(immeuble(bx, y - 40, 180, 3, coul, "pignon" if k % 2 else "mansarde", toit_c="#c92a2a" if k % 2 else None,
                       rdc="boutique", store=ROUGE, graine=k + 3))
    S.add(rect(0, y - 40, 800, 840 - y, "#dee2e6"), rect(0, y - 44, 800, 6, "#adb5bd"))
    for x in (64, 736, 150, 650):
        S.proposer_cachette(x, y + 40)


def guirlande_lanternes(S, y=60, x0=0, x1=800, nb=6):
    S.add(chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y + 50} {x1} {y}", stroke="#495057", sw=3))
    for k in range(nb):
        t = (k + 0.5) / nb
        px = x0 + (x1 - x0) * t
        py = y + 50 * 4 * t * (1 - t) / 2
        S.add(lanterne_rouge(px, py, 0.45))


# ---------------------------------------------------------------------------

def parc(S, sol_y=620, graine=3):
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, sol_y - 60, "#e7f5ff", graine=graine, bosquets=False)
    sol(S, sol_y, NEIGE, bosse=10)
    S.add(sapin(80, sol_y + 20, 0.9, neige=True), sapin(740, sol_y + 10, 0.8, neige=True))


def couverture():
    S = Scene()
    parc(S, 640, graine=4)
    hx, hy = mains_personne(400, 790, 1.35, "haut")[1]
    S.add(cerf_volant_dragon(560, 230, 1.0, fil_vers=(hx, hy), rot=-6))
    S.add(lin(400, 790, 1.35, dehors=True, expr="rire", bras="haut", regard=(1, -1)))
    S.add(wong(210, 790, 1.2, expr="rire", bras="mains_jointes", regard=(1, -1), coiffe=tuque("#2b8a3e")))
    S.add(yeye(620, 790, 1.2, dehors=True, expr="rire", bras="hanches", regard=(-1, -1)))
    S.cachette(760, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(enveloppe_rouge(200, 150, 1.6, rot=-8))
    return S


def p01():
    """Plan moyen : Nainai offre l'enveloppe rouge, à deux mains."""
    S = Scene()
    salon(S, 600)
    S.add(papier_decoupe(160, 230, 0.6), papier_decoupe(420, 220, 0.5))
    ex, ey = mains_personne(520, 790, 1.3, "tend", flip=True, stature="ancien", carrure="fine")[0]
    S.add(nainai(520, 790, 1.3, expr="rire", bras="tend", flip=True, regard=(-1, 0.4)))
    S.add(lin(280, 790, 1.2, expr="content", bras="tend", regard=(1, 0)))
    S.add(enveloppe_rouge(ex - 30, ey + 10, 0.7, rot=-10))
    S.add(bulle(420, 130, 400, 90, "Bonne année !\nPour la chance !", 32, pointe=(530, 420)))
    S.cachette(30, 790)
    return S


def p02():
    """Gros plan : vingt dollars !"""
    S = Scene()
    salon(S, 640)
    S.add(lin(400, 820, 1.7, expr="bouche_bee", bras="porte", regard=(0, 1), objet=enveloppe_rouge(0, -60, 0.9, ouverte=True)))
    S.add(paillettes(560, 430, 0.9))
    S.camera(1.4, 400, 500)
    S.dessus(texte(400, 110, "Vingt dollars !", 56, ROUGE, contour="#fff", rot=-4))
    S.cachette(110, 790)
    return S


def p03():
    """Plan moyen : Lin rêve du cerf-volant dragon."""
    S = Scene()
    salon(S, 620)
    S.add(lin(250, 800, 1.3, expr="content", bras="pense", regard=(1, -1)))
    reve = g([rect(-200, -110, 400, 220, "#a5d8ff", rx=60), cerf_volant_dragon(80, -30, 0.7, rot=-8, longueur=6)])
    S.add(pensee(500, 300, 210, place(reve, 500, 300, 0.85), depuis=(310, 470)))
    S.cachette(770, 790)
    return S


def p04():
    """Plan large : la rue en fête, le lion qui danse."""
    S = Scene()
    rue(S, 640)
    guirlande_lanternes(S, 60, 0, 800, 7)
    flocons(S, 25, 7, (0, 0, 800, 600))
    S.add(lion_danse(560, 720, 0.75))
    S.add(tambour(700, 760, 0.9))
    S.add(yeye(200, 780, 1.1, dehors=True, expr="rire", bras="main", flip=True, regard=(1, 0)))
    S.add(lin(320, 790, 0.95, dehors=True, expr="rire", bras="main", regard=(1, 0)))
    S.add(texte(560, 230, "Boum, boum !", 40, ROUGE, contour="#fff", rot=-6))
    S.cachette(30, 790)
    return S


def vitrine(S, x0, y0, w, h, contenu):
    S.add(rect(x0 - 16, y0 - 16, w + 32, h + 32, "#c92a2a", rx=6))
    cid = uid("vit")
    S.add(el("clipPath", rect(x0, y0, w, h, "#000"), id=cid))
    S.add(g([rect(x0, y0, w, h, "#fff9db"), contenu], clip_path=f"url(#{cid})"))
    S.add(poly([(x0 + w * 0.1, y0 + h), (x0 + w * 0.4, y0), (x0 + w * 0.52, y0), (x0 + w * 0.22, y0 + h)], "#fff", opacity=0.25))


def p05():
    """Plan moyen : le cerf-volant dragon dans la vitrine, à 20 $."""
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#ffe3e3"))
    S.add(briques(0, 0, 800, 640, "#ffe3e3"))
    S.add(store_banne(80, 60, 640, ROUGE))
    vitrine(S, 100, 120, 600, 420, g([cerf_volant_dragon(470, 260, 1.0, rot=-6), rect(140, 480, 520, 60, "#ced4da"),
                                      ballon_jeu(220, 470, 26), rect(300, 420, 60, 60, "#4dabf7", rx=6),
                                      place(rect(-50, -24, 100, 48, "#fff", rx=6) + texte(0, 12, "20 $", 30, ROUGE), 520, 380, 1.0, rot=6)]))
    S.add(rect(0, 640, 800, 160, "#dee2e6"))
    S.add(yeye(560, 790, 1.2, dehors=True, expr="content", bras="hanches", regard=(-1, 0)))
    S.add(lin(330, 800, 1.1, dehors=True, expr="bouche_bee", bras="joues", regard=(1, -1)))
    S.add(bulle(140, 640, 250, 90, "Juste ce qu'il\nme faut !", 26, pointe=(290, 640)))
    S.cachette(30, 790)
    return S


def p06():
    """Plan moyen : Madame Wong, seule à sa fenêtre sans lanterne."""
    S = Scene()
    rue(S, 640)
    guirlande_lanternes(S, 40, 0, 360, 3)
    # la petite maison de Madame Wong, sans décoration
    S.add(rect(380, 140, 420, 460, "#ced4da"), planches(380, 140, 420, 460, "#ced4da", larg=28, vertical=False))
    S.add(poly([(360, 150), (590, 40), (820, 150)], "#495057"))
    vue = g([rect(0, 0, 800, 800, "#e9ecef"), wong(590, 470, 0.95, expr="triste", bras="bas", regard=(-1, 0.5))])
    S.add(fenetre(500, 230, 180, 170, "#e9ecef", cadre="#868e96", contenu=vue))
    S.add(rect(380, 600, 420, 40, "#adb5bd"))
    S.add(yeye(260, 780, 1.15, dehors=True, expr="triste", bras="bas", regard=(1, 0)))
    S.add(lin(140, 790, 1.0, dehors=True, expr="inquiet", bras="designe", regard=(1, -0.5)))
    S.add(bulle(560, 520, 360, 90, "Cette année, elle fête\ntoute seule.", 26, pointe=(280, 560)))
    S.cachette(770, 790)
    return S


def p07():
    """Gros plan : Lin réfléchit, l'enveloppe serrée contre elle."""
    S = Scene()
    rue(S, 640)
    S.add(lin(400, 820, 1.7, dehors=True, expr="inquiet", bras="porte", regard=(-1, 0), objet=enveloppe_rouge(0, -60, 0.8)))
    S.add(pensee(170, 200, 110, place(cerf_volant_dragon(0, 0, 0.5, longueur=4), 190, 200, 1.0), depuis=(330, 420)))
    S.add(pensee(630, 200, 110, place(g([rect(-60, -50, 120, 100, "#ced4da"), rect(-34, -30, 68, 60, "#e9ecef"),
                                         cercle(0, -2, 16, "#fbd9bd"), cercle(0, -16, 16, "#e9ecef")]), 630, 200, 1.0), depuis=(470, 420)))
    S.camera(1.15, 400, 450)
    S.dessus(bulle(400, 720, 520, 90, "Yeye… la chance, est-ce qu'on\npeut la partager ?", 28))
    S.cachette(90, 790)
    return S


def etal(x, y, s=1.0):
    """Étal de fruits : caisses de mandarines et de pommes sous un auvent."""
    m = [rect(-200, -160, 400, 160, "#a0693a", rx=6), store_banne(-210, -330, 420, "#2f9e44"),
         rect(-200, -330, 10, 170, "#495057"), rect(190, -330, 10, 170, "#495057")]
    for k in range(3):
        cx = -130 + k * 130
        m.append(rect(cx - 56, -200, 112, 50, "#c68642", rx=4))
        for j in range(5):
            m.append(cercle(cx - 40 + j * 20, -206 - (j % 2) * 8, 14, volume(("#ff922b", "#fa5252", "#ff922b")[k], 0.4, 0.75)))
    return place(m, x, y, s)


def p08():
    """Plan moyen : les mandarines et la lanterne de papier."""
    S = Scene()
    rue(S, 640)
    S.add(personne(560, 640, 0.9, expr="rire", bras="donne", flip=True, regard=(-1, 0.3), **MARCHAND))
    S.add(etal(560, 690, 1.0))
    fx, fy = mains_personne(560, 640, 0.9, "donne", flip=True, stature="adulte", carrure="ronde")[0]
    S.add(filet_mandarines(fx, fy, 0.75))
    bx, by = mains_personne(330, 790, 1.15, "tend")[1]
    S.add(lin(330, 790, 1.15, dehors=True, expr="sourire", bras="tend", regard=(1, -0.3)))
    S.add(billet(bx + 20, by - 10, 0.55, rot=-10))
    S.add(yeye(140, 790, 1.2, dehors=True, expr="fier", bras="tient", regard=(1, 0), objet=lanterne_rouge(*ancre(68, -146, "tient", "ancien"), 0.5)))
    S.cachette(770, 790)
    return S


def p09():
    """Plan moyen : « Bonne année, Madame Wong ! Pour la chance ! »"""
    S = Scene()
    rue(S, 680)
    S.add(rect(300, 120, 500, 560, "#ced4da"), planches(300, 120, 500, 560, "#ced4da", larg=28, vertical=False))
    S.add(rect(470, 280, 200, 400, "#fff4e6"), rect(460, 270, 220, 12, "#495057"))
    S.add(poly([(670, 280), (630, 296), (630, 668), (670, 680)], cylindre("#868e96", 0.2, 0.7)))
    S.add(wong(560, 690, 1.2, expr="content", larmes=True, bras="tend", flip=True, regard=(-1, 0.4)))
    mx, my = mains_personne(300, 790, 1.15, "tend")[1]
    S.add(lin(300, 790, 1.15, dehors=True, expr="rire", bras="tend", regard=(1, 0)))
    S.add(filet_mandarines(mx + 6, my - 10, 0.8))
    S.add(yeye(120, 790, 1.2, dehors=True, expr="content", bras="tient", regard=(1, 0), objet=lanterne_rouge(*ancre(68, -146, "tient", "ancien"), 0.5)))
    S.add(bulle(280, 130, 380, 100, "Bonne année,\nMadame Wong !", 34, pointe=(310, 440)))
    S.cachette(770, 790)
    return S


def malle(x, y, s=1.0):
    return place([rect(-90, -90, 180, 90, volume("#8d5524", 0.3, 0.75), rx=8),
                  poly([(-90, -90), (-100, -170), (100, -170), (90, -90)], volume("#a0693a", 0.3, 0.75)),
                  rect(-90, -60, 180, 10, OR_), rect(-12, -70, 24, 24, OR_, rx=4)], x, y, s)


def p10():
    """Plan large : la petite maison de Madame Wong devient toute rouge."""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.ambiance("interieur")
    S.add(fenetre(470, 110, 180, 160, "#d0ebff", contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 220, 800, 100, NEIGE)])))
    S.add(papier_decoupe(560, 190, 0.45))
    S.add(trait(0, 300, 800, 300, "#6d4424", 0))
    S.add(yeye(240, 700, 1.1, expr="rire", bras="haut", regard=(1, -1)))
    hx, hy = mains_personne(240, 700, 1.1, "haut", stature="ancien")[1]
    S.add(trait(hx, 0, hx, hy, "#495057", 3), lanterne_rouge(hx, hy, 0.7))
    S.add(lin(560, 720, 1.0, expr="concentre", bras="tient", regard=(0, -1), objet=papier_decoupe(68, -160, 0.35)))
    S.add(table(400, 790, 300, 100, "#a0693a", nappe="#ffe3e3"))
    S.add(filet_mandarines(400, 600, 0.7))
    S.add(malle(700, 790, 0.8))
    S.add(wong(110, 790, 1.15, expr="rire", bras="mains_jointes", regard=(1, -0.3)))
    S.cachette(770, 790)
    return S


def p11():
    """Gros plan : le vieux cerf-volant dragon sort de la malle."""
    S = Scene()
    piece(S, "chaumiere", 640)
    S.ambiance("interieur")
    S.add(malle(400, 800, 1.2))
    S.add(cerf_volant_dragon(470, 420, 1.1, passe=True, rot=-10, longueur=6))
    S.add(wong(600, 800, 1.5, expr="content", bras="tend", flip=True, regard=(-1, -0.3)))
    S.add(lin(230, 800, 1.4, expr="bouche_bee", bras="joues", regard=(1, -0.5)))
    S.camera(1.2, 420, 500)
    S.dessus(bulle(400, 100, 520, 100, "Il attendait quelqu'un\npour voler encore.", 32, pointe=S.vers_page(600, 470)))
    S.cachette(90, 790)
    return S


def p12():
    """Plan large : au parc, le vieux dragon vole plus haut que tous les autres."""
    S = Scene()
    parc(S, 620, graine=6)
    S.add(cerf_volant_losange(200, 200, 0.4, "#4dabf7", "#ffd43b"))
    hx, hy = mains_personne(440, 790, 1.1, "haut")[1]
    S.add(cerf_volant_dragon(560, 140, 0.9, passe=True, fil_vers=(hx, hy), rot=-8))
    S.add(lin(440, 790, 1.1, dehors=True, expr="rire", bras="haut", regard=(1, -1)))
    S.add(wong(260, 790, 1.1, expr="rire", bras="applaudit", regard=(1, -1), coiffe=tuque("#2b8a3e")))
    S.add(yeye(620, 790, 1.1, dehors=True, expr="rire", bras="ouverts", regard=(-1, -1)))
    S.cachette(30, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("enveloppe-seule.svg", vignette),
    ("01-l-enveloppe.svg", p01), ("02-vingt-dollars.svg", p02), ("03-le-reve.svg", p03),
    ("04-dans-la-rue.svg", p04), ("05-la-vitrine.svg", p05), ("06-madame-wong.svg", p06),
    ("07-lin-reflechit.svg", p07), ("08-les-mandarines.svg", p08), ("09-bonne-annee.svg", p09),
    ("10-la-lanterne.svg", p10), ("11-le-vieux-dragon.svg", p11), ("12-la-chance-grandit.svg", p12),
]
