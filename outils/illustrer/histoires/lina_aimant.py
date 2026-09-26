"""Lina et l'aimant — le magnétisme.

Rouge = pôle Nord, bleu = pôle Sud. Les lignes de limaille et le champ de la
Terre sont calculés comme ceux d'un vrai aimant droit. Le « pôle Nord » de
l'aiguille d'une boussole est attiré vers le nord géographique : l'aimant
géant de la Terre a donc son pôle Sud (bleu) en haut, du côté du nord.
"""
from base import *
from objets import *
from sciences import *
from fantastique import personne

ID = "lina-aimant"
LINA = dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#fcc419", jambes="#1c7ed6")
TOM = dict(peau="claire", cheveux="roux", coiffure="courts", habit="#51cf66", jambes="#495057")
PAPI = dict(peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#a0693a", jambes="#495057", robe=False,
            acc=("lunettes",), barbe="#e9ecef")
ACIER = "#868e96"


def lina(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**LINA, **k})


def tom(x, y, s=1.0, **k):
    return enfant(x, y, s, **{**TOM, **k})


def papi(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PAPI, **k})


def salon(S, mur="#fff4e6", papier="#ffe8cc"):
    interieur(S, mur, "#e8c39e", y=600, papier=papier)


def main_haute(x, y, s, bras, flip=False):
    """Position de la main levée d'un personnage."""
    return min(mains(x, y, s, bras, flip), key=lambda p: p[1])


def aimant_tenu(hx, hy, s=0.6, rot=180):
    """Aimant en U tenu par le haut dans la main (hx, hy), les pôles vers le bas (rot=180)."""
    return aimant_u(hx, hy, s, rot=rot)


def grappe(x, y, s=1.0, n_=6, graine=1):
    """Trombones accrochés les uns aux autres sous le point (x, y)."""
    r = random.Random(graine)
    m = []
    for k in range(n_):
        m.append(trombone(x + r.uniform(-14, 14) + (k % 2) * 16 - 8, y + 26 + k * 34, 1.1, rot=r.uniform(-30, 30), couleur=ACIER))
    return place(m, 0, 0, s)


def cle_acier(x, y, s=1.0, rot=0):
    return cle(x, y, s, rot=rot, couleur="#adb5bd")


def couverture():
    S = Scene()
    ciel(S, "#fff3bf", "#ffe8cc")
    S.add(cercle(400, 420, 330, "#ffec99", opacity=0.6))
    S.add(lina(330, 780, 1.9, expr="rire", bras="montre", regard=(1, -1)))
    mx, my = 520, 300
    S.add(aimant_u(mx, my, 1.1, rot=150))
    for k, obj in enumerate([trombone(0, 0, 1.4, 20, ACIER), clou(0, 0, 1.2, 160), cle_acier(0, 0, 1.2, 70), vis(0, 0, 1.3, 200), trombone(0, 0, 1.4, -30, ACIER)]):
        S.add(place(obj, 620 + (k % 3) * 40, 330 + k * 34))
    S.add(eclat(560, 240, 1.0, "#fab005"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(aimant_u(200, 20, 0.6, rot=180))
    S.add(grappe(171, 125, 0.9, 3, 1), grappe(229, 125, 0.9, 3, 2))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(fenetre(560, 90, 170, 150, rideaux="#74c0fc"))
    S.add(papi(250, 760, 1.55, expr="content", bras="donne", regard=(1, 0)))
    mg, md = mains(250, 760, 1.55, "donne")
    S.add(place(g([rect(-50, -30, 100, 60, "#ff8787", rx=8), rect(-8, -30, 16, 60, "#fcc419")]), md[0] + 20, md[1] + 40, 1.0))
    S.add(aimant_u(md[0] + 20, md[1] + 10, 0.55, rot=10))
    S.add(lina(560, 760, 1.45, expr="bouche_bee", bras="ouverts", regard=(-1, 0)))
    S.add(paillettes(md[0] + 40, md[1] - 120, 1.2))
    return S


def p02():
    S = Scene()
    salon(S)
    hx, hy = main_haute(540, 800, 2.0, "tient", True)
    S.add(place(g([rect(-90, -60, 180, 60, "#4dabf7", rx=8)] + [trombone(-60 + k * 24, -52, 1.0, k * 40, ACIER) for k in range(6)]), hx - 60, 800))
    S.add(lina(540, 800, 2.0, expr="rire", bras="tient", regard=(-1, 1), flip=True))
    S.add(aimant_tenu(hx, hy - 6, 0.6))
    S.add(grappe(hx - 29, hy + 90, 1.0, 3, 3), grappe(hx + 29, hy + 90, 1.0, 2, 4))
    S.add(texte(230, 200, "Clic, clic, clic !", 54, "#e8590c", contour="#fff", rot=-6))
    return S


def cuillere(x, y, s=1.0, rot=0, couleur="#adb5bd"):
    m = [ellipse(0, -80, 22, 30, couleur), rect(-5, -52, 10, 90, couleur, rx=4), ellipse(-6, -86, 6, 12, "#fff", opacity=0.4)]
    return place(m, x, y, s, rot=rot)


def p03():
    S = Scene()
    salon(S, "#f3f0ff", "#e5dbff")
    S.add(table(200, 760, 300, 150, "#c68642"))
    S.add(cuillere(200, 600, 1.4, rot=-80, couleur="#d9a066"))
    S.add(texte(200, 520, "bois", 40, "#a0693a", contour="#fff"))
    hx, hy = main_haute(580, 800, 2.0, "tient", True)
    S.add(lina(580, 800, 2.0, expr="content", bras="tient", flip=True, regard=(-1, 1)))
    S.add(aimant_tenu(hx, hy - 6, 0.6))
    S.add(cuillere(hx - 29, hy + 250, 1.2, rot=4))
    S.add(texte(hx - 150, hy + 200, "métal", 40, "#495057", contour="#fff"))
    return S


def p04():
    S = Scene()
    salon(S)
    S.add(lina(400, 700, 1.25, expr="content", bras="ouverts"))
    for k, obj in enumerate([clou(0, 0, 1.2, 70), cle_acier(0, 0, 1.1, -10), vis(0, 0, 1.2, 100), trombone(0, 0, 1.5, 30, ACIER)]):
        S.add(place(obj, 130 + k * 66, 585))
    S.add(place(g([rect(-40, -18, 80, 36, "#ff8787", rx=6), rect(-40, -18, 32, 36, "#4dabf7", rx=6)]), 480, 590))
    S.add(place(g([rect(-18, -28, 36, 56, "#d9a066", rx=6), ellipse(0, -28, 18, 7, "#e8c39e")]), 575, 580))
    S.add(place(poly([(-38, -34), (34, -40), (40, 34), (-34, 38)], "#fff", stroke="#dee2e6", stroke_width=2), 665, 585, rot=-8))
    for x, mot, c in [(230, "OUI", "#51cf66"), (570, "NON", "#ff8787")]:
        S.add(place(g([rect(-150, -170, 300, 170, c, rx=14), rect(-150, -170, 300, 30, assombrir(c, 0.85), rx=10)]), x, 770))
        S.add(texte(x, 720, mot, 64, "#fff"))
    return S


def canette(x, y, s=1.0):
    m = [rect(-40, -140, 80, 140, "#e8590c", rx=10), rect(-40, -140, 80, 16, "#ced4da", rx=6), rect(-40, -14, 80, 14, "#ced4da", rx=6),
         ellipse(0, -76, 26, 30, "#ffd43b"), texte(0, -64, "JUS", 22, "#e8590c"), rect(-30, -126, 10, 100, "#fff", opacity=0.3, rx=5)]
    return place(m, x, y, s)


def p05():
    S = Scene()
    salon(S, "#fff9db", "#fff3bf")
    S.add(table(400, 720, 520, 170, "#c68642"))
    S.add(canette(280, 552, 1.3))
    S.add(texte(280, 330, "aluminium", 38, "#868e96"))
    S.add(lina(600, 780, 1.4, expr="triste", bras="montre", flip=True, regard=(-1, 0)))
    hx, hy = main_haute(600, 780, 1.4, "montre", True)
    S.add(aimant_tenu(hx - 10, hy, 0.6, rot=250))
    S.add(texte(180, 200, "?", 100, "#f76707", contour="#fff"))
    return S


def frigo(x, y, s=1.0):
    m = [rect(-120, -440, 240, 440, "#f8f9fa", rx=24, stroke="#dee2e6", stroke_width=5),
         trait(-120, -300, 120, -300, "#dee2e6", 5), rect(90, -420, 12, 90, "#adb5bd", rx=6), rect(90, -270, 12, 110, "#adb5bd", rx=6)]
    dessins = [(-60, -390, "#ffec99", soleil(0, 0, 18)), (40, -220, "#d0ebff", maison(0, 30, 0.22)), (-50, -130, "#d3f9d8", fleur(0, 26, 0.6, "#ff6b6b", tige=40))]
    for dx, dy, fond_, motif in dessins:
        m.append(place(g([rect(-45, -45, 90, 90, fond_, stroke="#dee2e6", stroke_width=2), motif, cercle(0, -45, 11, "#fa5252")]), dx, dy))
    return place(m, x, y, s)


def p06():
    S = Scene()
    interieur(S, "#e6fcf5", "#c99a6e", y=620)
    S.add(frigo(300, 760, 1.4))
    S.add(lina(600, 780, 1.4, expr="fier", bras="montre", flip=True, regard=(-1, 0)))
    return S


def p07():
    S = Scene()
    salon(S)
    # la planche vue de face ; en dessous, la main de Lina tient l'aimant
    S.add(rect(80, 360, 640, 40, "#c68642", rx=6), rect(110, 400, 24, 260, "#a0693a"), rect(666, 400, 24, 260, "#a0693a"))
    S.add(trombone(470, 350, 1.8, 90, ACIER))
    S.add(mouvement(430, 330, 1.0), chemin("M 180 330 Q 300 280 440 340", stroke="#868e96", sw=4, stroke_dasharray="8 10"))
    S.add(lina(470, 830, 1.1, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(aimant_u(470, 640, 1.2, rot=0))
    S.add(texte(400, 180, "Ça traverse le bois !", 44, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    salon(S, "#e7f5ff", "#d0ebff")
    S.add(table(360, 740, 460, 150, "#c68642"))
    S.add(verre(300, 590, 170, 260, niveau=0.8))
    S.add(trombone(352, 400, 1.4, 0, ACIER))
    S.add(aimant_u(420, 400, 0.5, rot=-90))
    S.add(chemin("M 352 560 L 352 440", stroke="#868e96", sw=3, stroke_dasharray="6 8"))
    S.add(lina(620, 790, 1.4, expr="rire", bras="montre", flip=True, regard=(-1, 0)))
    S.add(bulle(360, 150, 320, 80, "Pas mouillée !", 40, pointe=(560, 300)))
    return S


def poisson_papier(x, y, s=1.0, couleur="#ff922b", rot=0):
    return place([poisson(0, 0, 0.6, couleur), trombone(10, -18, 0.8, 90, ACIER)], x, y, s, rot=rot)


def p09():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 560, "#8ce99a", couleur2="#69db7c", y2=660)
    S.add(ellipse(420, 680, 260, 70, "#1971c2"), ellipse(420, 676, 240, 58, "#4dabf7"))
    for k, (x, y, c) in enumerate([(320, 680, "#ff922b"), (430, 660, "#cc5de8"), (520, 690, "#51cf66"), (380, 710, "#fcc419")]):
        S.add(poisson_papier(x, y, 1.0, c, rot=(k % 2) * 180 - 10))
    S.add(lina(170, 700, 1.3, expr="concentre", bras="montre", regard=(1, 0)))
    mg, md = mains(170, 700, 1.3, "montre")
    S.add(trait(md[0], md[1], md[0] + 200, md[1] - 160, "#8d5524", 7))
    S.add(trait(md[0] + 200, md[1] - 160, 470, 600, "#495057", 2))
    S.add(aimant_u(470, 612, 0.25, rot=180))
    S.add(poisson_papier(470, 640, 1.0, "#ff6b6b", rot=-70))
    S.add(tom(680, 700, 1.2, expr="rire", bras="haut", regard=(-1, 0), flip=True))
    return S


def p10():
    S = Scene()
    fond(S, "#fff9db")
    S.add(table(400, 760, 700, 120, "#c68642"))
    S.add(barreau(270, 520, 240, 70, nord_a_droite=False), barreau(532, 520, 240, 70, nord_a_droite=False))
    S.add(fleche(250, 400, 360, 400, "#2f9e44", 7), fleche(550, 400, 440, 400, "#2f9e44", 7))
    S.add(eclat(401, 520, 1.1, "#fab005"))
    S.add(texte(400, 250, "Clac !", 90, "#e8590c", contour="#fff", rot=-4))
    return S


def p11():
    S = Scene()
    fond(S, "#fff5f5")
    S.add(table(400, 760, 700, 120, "#c68642"))
    S.add(barreau(200, 520, 240, 70, nord_a_droite=True), barreau(600, 520, 240, 70, nord_a_droite=False))
    for k in range(3):
        S.add(chemin(f"M {372 + k * 28} 460 q -16 60 0 120", stroke="#fa5252", sw=5, opacity=0.8 - k * 0.2))
        S.add(chemin(f"M {428 - k * 28} 460 q 16 60 0 120", stroke="#fa5252", sw=5, opacity=0.8 - k * 0.2) if k else "")
    S.add(fleche(340, 400, 200, 400, "#c92a2a", 7), fleche(460, 400, 600, 400, "#c92a2a", 7))
    S.add(texte(400, 250, "Pousse !", 90, "#c92a2a", contour="#fff", rot=3))
    return S


def voiture(x, y, s=1.0, couleur="#339af0"):
    m = [chemin("M -110 -30 L -110 -70 Q -100 -80 -60 -80 L -40 -120 L 40 -120 L 70 -80 L 110 -76 Q 120 -70 120 -30 Z", couleur),
         poly([(-30, -112), (30, -112), (54, -82), (-30, -82)], "#d0ebff"),
         cercle(-60, -30, 26, ENCRE), cercle(-60, -30, 11, "#adb5bd"), cercle(70, -30, 26, ENCRE), cercle(70, -30, 11, "#adb5bd")]
    return place(m, x, y, s)


def p12():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=560)
    S.add(voiture(620, 720, 1.2))
    S.add(barreau(445, 676, 150, 44, nord_a_droite=False))
    S.add(lina(150, 800, 1.5, expr="rire", bras="donne", regard=(1, 0)))
    S.add(barreau(245, 676, 150, 44, nord_a_droite=True))
    for k in range(2):
        S.add(chemin(f"M {335 + k * 20} 646 q -10 30 0 60", stroke="#fa5252", sw=4, opacity=0.8))
    S.add(fleche(560, 500, 740, 500, "#1c7ed6", 7))
    S.add(texte(620, 420, "Vroum !", 70, "#1c7ed6", contour="#fff"))
    return S


def p13():
    S = Scene()
    fond(S, "#e9ecef")
    S.add(rect(60, 60, 680, 680, "#ffffff", stroke="#dee2e6", stroke_width=4))
    cid = uid("f")
    S.defs.append(el("clipPath", rect(64, 64, 672, 672, "#000"), id=cid))
    cx, cy, demi = 400, 400, 100
    traits = [trace(l, "#495057", 3.5, stroke_dasharray="5 7") for l in lignes_dipole(cx, cy, demi, 0, nb=20, r0=22)]
    S.add(g(traits, clip_path=f"url(#{cid})", opacity=0.9))
    S.add(barreau(cx, cy, 260, 70, nord_a_droite=True))
    return S


def p14():
    S = Scene()
    salon(S, "#e7f5ff", "#d0ebff")
    S.add(fenetre(80, 70, 150, 140))
    S.add(papi(200, 780, 1.4, expr="content", bras="donne", regard=(1, 0)))
    S.add(lina(620, 780, 1.4, expr="bouche_bee", bras="bas", regard=(-1, 0)))
    S.add(boussole(400, 330, 130, angle=0))
    S.add(texte(400, 150, "nord", 44, "#e03131", contour="#fff"))
    return S


def p15():
    S = Scene()
    fond(S, "#0b1433")
    etoiles(S, 60, 15, (0, 0, 800, 800))
    cx, cy, R = 400, 420, 170
    # aimant intérieur : pôle Nord (rouge) vers le sud géographique, pôle Sud (bleu) vers le nord.
    # Le champ sort par le bas et rentre par le haut : dehors, il est dirigé vers le nord.
    lignes = lignes_dipole(cx, cy, 70, 90, nb=14, r0=16)
    S.add(g([trace(l, "#74c0fc", 3) for l in lignes], opacity=0.55))
    S.add(cercle(cx, cy, R + 10, "#4dabf7", opacity=0.25))
    S.add(cercle(cx, cy, R, "#1c7ed6"))
    for px, py, rr in [(-60, -80, 60), (50, 20, 70), (-40, 90, 40), (80, -100, 30)]:
        S.add(cercle(cx + px, cy + py, rr, "#51cf66"))
    S.add(ellipse(cx, cy - R + 16, 70, 18, "#fff"), ellipse(cx, cy + R - 16, 70, 18, "#fff"))
    S.add(barreau(cx, cy, 190, 46, nord_a_droite=True, rot=90))
    # petites boussoles posées sur des lignes de champ, hors de la Terre
    for l in lignes:
        for i in range(0, len(l), 1):
            x, y = l[i]
            d = math.hypot(x - cx, y - cy)
            if abs(d - (R + 75)) < 3 and abs(x - cx) > 150 and 40 < x < 760:
                S.add(boussole(x, y, 24, angle=direction_champ(l, i) + 90, cadran=False))
                break
    S.add(texte(cx, 60, "Nord", 44, "#fff3bf"))
    return S


def coffre(x, y, s=1.0, ouvert=True):
    m = [rect(-110, -110, 220, 110, "#868e96", rx=10), rect(-110, -70, 220, 16, "#495057"),
         rect(-14, -84, 28, 34, "#fab005", rx=4)]
    if ouvert:
        m.insert(0, chemin("M -110 -110 Q 0 -250 110 -110 Z", "#adb5bd"))
        for k in range(8):
            m.append(cercle(-80 + k * 22, -114 - (k % 3) * 10, 16, "#fcc419", stroke="#f08c00", stroke_width=3))
    return place(m, x, y, s)


def p16():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 560, "#b2f2bb", graine=16)
    sol(S, 560, "#8ce99a", couleur2="#69db7c", y2=660)
    S.add(arbre(680, 600, 0.8))
    S.add(ellipse(480, 740, 140, 30, "#9c6b3f"))
    S.add(coffre(480, 750, 1.1))
    S.add(eclat(480, 560, 1.4, "#fcc419"))
    S.add(lina(200, 780, 1.4, expr="rire", bras="haut", regard=(1, 0)))
    S.add(boussole(110, 120, 50, angle=0))
    S.add(place(g([rect(-60, -40, 120, 80, "#fff3bf", rx=6), chemin("M -40 20 Q -10 -30 30 -10", stroke="#e03131", sw=4, stroke_dasharray="6 6"),
                   texte(34, 8, "X", 28, "#e03131")]), 240, 120, 1.1, rot=-8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("aimant-seul.svg", vignette),
    ("01-cadeau.svg", p01), ("02-trombones.svg", p02), ("03-cuilleres.svg", p03), ("04-tri.svg", p04),
    ("05-canette.svg", p05), ("06-frigo.svg", p06), ("07-sous-la-table.svg", p07), ("08-verre-d-eau.svg", p08),
    ("09-peche.svg", p09), ("10-nord-sud.svg", p10), ("11-nord-nord.svg", p11), ("12-voiture.svg", p12),
    ("13-limaille.svg", p13), ("14-boussole.svg", p14), ("15-terre.svg", p15), ("16-tresor.svg", p16),
]
