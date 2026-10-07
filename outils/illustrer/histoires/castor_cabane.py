"""Castor et la cabane perchée — roue, rampe et poulie.

Trois machines simples. Les rondins et la roue remplacent le frottement par
un roulement. La rampe en pente douce demande moins de force, mais un chemin
plus long. Une poulie fixe ne rend pas la charge plus légère : elle change
seulement le sens de la traction (on tire vers le bas). Avec une poulie
mobile en plus (moufle), deux brins de corde portent la charge : il faut
deux fois moins de force, mais tirer deux fois plus de corde.
"""
from base import *
from objets import *
from sciences import fleche
from fables import puits

ID = "castor-cabane"
BOIS, BOIS_F = "#d9a066", "#a9743f"
CORDE = "#c2995c"


def castor(x, y, s=1.0, **k):
    return perso("castor", x, y, s, **{**dict(habit="#f59f00", acc=("casque",), couleur_acc="#ffd43b"), **k})


def ecureuil(x, y, s=0.85, **k):
    return perso("ecureuil", x, y, s, **{**dict(habit="#4dabf7"), **k})


def herisson(x, y, s=0.75, **k):
    return perso("herisson", x, y, s, **{**dict(habit="#69db7c"), **k})


def souris(x, y, s=0.55, **k):
    return perso("souris", x, y, s, **{**dict(habit="#f783ac"), **k})


# ---------------------------------------------------------------------------
# Matériel
# ---------------------------------------------------------------------------

def planche(x, y, w=260, h=26, rot=0):
    """Planche centrée en (x, y)."""
    m = [rect(-w / 2, -h / 2, w, h, BOIS, rx=4, stroke=BOIS_F, stroke_width=3),
         trait(-w / 2 + 20, -3, w / 2 - 40, -3, BOIS_F, 2, opacity=0.6),
         trait(-w / 2 + 50, 5, w / 2 - 20, 5, BOIS_F, 2, opacity=0.6)]
    return place(m, x, y, rot=rot)


def pile_planches(x, y, nb=5):
    return g([planche(x + (k % 2) * 10, y - 13 - k * 26) for k in range(nb)])


def rondin(x, y, r=22):
    """Rondin vu de bout, (x, y) = centre."""
    return g([cercle(x, y, r, "#8d5524"), cercle(x, y, r * 0.75, "#e8c39e"),
              cercle(x, y, r * 0.45, "none", stroke="#c68642", stroke_width=2), cercle(x, y, 3, "#a0693a")])


def roue(x, y, r=40, couleur="#495057"):
    m = [cercle(x, y, r, couleur), cercle(x, y, r * 0.7, "#ced4da")]
    for k in range(6):
        a = math.radians(k * 60)
        m.append(trait(x, y, x + math.cos(a) * r * 0.7, y + math.sin(a) * r * 0.7, couleur, 4))
    m.append(cercle(x, y, 7, couleur))
    return g(m)


def brouette(x, y, s=1.0, charge=True, flip=False):
    """Brouette, roue en avant (à droite) ; (x, y) = sol sous la roue."""
    m = [trait(-230, -70, -90, -60, "#8d5524", 10), trait(-200, -40, -170, 0, "#8d5524", 8)]
    if charge:
        m += [planche(-70, -128 - k * 18, 200, 18, rot=-4) for k in range(3)]
    m += [poly([(-170, -120), (40, -120), (10, -50), (-140, -50)], "#e03131"),
           poly([(-170, -120), (40, -120), (34, -106), (-164, -106)], "#c92a2a"),
           trait(-60, -50, -10, -34, "#495057", 6), roue(0, -36, 36)]
    return place(m, x, y, s, flip=flip)


def poulie(x, y, r=28, crochet=24):
    """Poulie suspendue ; (x, y) = centre de la roue."""
    return g([trait(x, y - r - crochet, x, y, "#495057", 6),
              cercle(x, y, r + 4, "#495057"), cercle(x, y, r - 4, "#adb5bd"),
              cercle(x, y, r - 14, "#868e96"), cercle(x, y, 5, ENCRE)])


def corde(d, sw=6):
    return chemin(d, stroke=CORDE, sw=sw)


def panier_corde(x, y, s=1.0, contenu=True):
    """Panier suspendu ; (x, y) = point d'attache de la corde."""
    m = [chemin("M -40 40 Q 0 -20 40 40", stroke="#8d5524", sw=5)]
    if contenu:
        m += [cercle(-14, 40, 12, "#fa5252"), cercle(10, 36, 12, "#ffd43b"), cercle(24, 44, 10, "#69db7c")]
    m += [chemin("M -46 40 L 46 40 L 36 92 L -36 92 Z", "#e8c39e", stroke="#c68642", sw=3),
          trait(-42, 58, 42, 58, "#c68642", 3), trait(-39, 75, 39, 75, "#c68642", 3)]
    return place(m, x, y, s)


def caisse(x, y, w=110, h=80):
    """Caisse posée ; (x, y) = milieu du haut."""
    return g([rect(x - w / 2, y, w, h, BOIS, stroke=BOIS_F, stroke_width=4, rx=4),
              trait(x - w / 2, y, x + w / 2, y + h, BOIS_F, 4), trait(x + w / 2, y, x - w / 2, y + h, BOIS_F, 4)])


def grue(x, y, s=1.0):
    m = [rect(-14, -320, 28, 320, "#fab005"),
         g([trait(-14, -k * 40, 14, -k * 40 - 40, "#e67700", 3) for k in range(8)]),
         rect(-80, -340, 300, 22, "#fab005"), rect(-90, -338, 40, 40, "#495057"),
         trait(200, -318, 200, -180, "#495057", 3), caisse(200, -180, 60, 44)]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def foret(S, graine=1, y=640):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(130, 110, 0.6), nuage(680, 80, 0.45))
    collines(S, y - 50, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a")


def grand_chene(S, x=560, y=700, plateforme=False, cabane=False, branche=False, fete=False):
    """Grand arbre ; plateforme à y = 330."""
    S.add(cercle(x - 120, 170, 120, "#40c057"), cercle(x + 110, 160, 120, "#40c057"), cercle(x, 90, 130, "#51cf66"))
    S.add(rect(x - 40, 160, 80, y - 160, "#8d5524", rx=14))
    S.add(chemin(f"M {x - 40} {y} Q {x - 70} {y + 4} {x - 90} {y + 10} L {x + 90} {y + 10} Q {x + 70} {y + 4} {x + 40} {y} Z", "#8d5524"))
    if branche:
        S.add(chemin(f"M {x - 30} 250 Q {x - 150} 205 {x - 280} 210 L {x - 280} 226 Q {x - 150} 224 {x - 30} 280 Z", "#8d5524"))
    if plateforme or cabane:
        S.add(rect(x - 160, 318, 320, 24, BOIS, stroke=BOIS_F, stroke_width=3, rx=4))
        S.add(trait(x - 120, 342, x - 40, 420, BOIS_F, 10), trait(x + 120, 342, x + 40, 420, BOIS_F, 10))
    if cabane:
        S.add(rect(x - 30, 190, 170, 128, "#ffd8a8", stroke=BOIS_F, stroke_width=4))
        S.add(g([trait(x - 30, 190 + k * 26, x + 140, 190 + k * 26, BOIS_F, 2, opacity=0.5) for k in range(1, 5)]))
        S.add(poly([(x - 50, 196), (x + 55, 120), (x + 160, 196)], "#e03131"))
        S.add(rect(x + 70, 228, 46, 40, "#a5d8ff" if not fete else "#ffe066", stroke="#fff", stroke_width=5))
        S.add(trait(x - 160, 318, x - 160, 270, BOIS_F, 6), trait(x - 160, 276, x - 30, 276, BOIS_F, 6))
    if fete:
        for k, c in enumerate(["#fa5252", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8"]):
            xx = x - 150 + k * 60
            S.add(poly([(xx, 140 + abs(k - 2) * 8), (xx + 30, 140 + abs(k - 2) * 8), (xx + 15, 170 + abs(k - 2) * 8)], c))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret(S, 2, 660)
    grand_chene(S, 520, 700, cabane=True, branche=True)
    S.add(ecureuil(470, 318, 0.6, expr="rire", bras="salut"))
    S.add(poulie(270, 248, 26))
    S.add(corde("M 296 248 L 296 420"), panier_corde(296, 420, 0.9))
    S.add(corde("M 244 248 L 244 600"))
    S.add(castor(165, 770, 1.15, expr="rire", bras="haut", regard=(1, -1)))
    S.add(pile_planches(670, 770, 3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(planche(290, 240, 160, 22, rot=-8))
    S.add(castor(170, 264, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    foret(S, 1)
    grand_chene(S, 580, 700)
    S.add(pile_planches(620, 760, 5))
    S.add(castor(240, 760, 1.25, expr="content", bras="pense", regard=(1, -1)))
    cab = g([rect(200, 130, 120, 80, "#ffd8a8", stroke=BOIS_F, stroke_width=3), poly([(185, 136), (260, 85), (335, 136)], "#e03131"),
             rect(250, 200, 140, 14, BOIS), trait(170, 214, 360, 214, "#8d5524", 10)])
    S.add(pensee(265, 160, 120, cab, depuis=(250, 470)))
    return S


def p02():
    S = Scene()
    foret(S, 3)
    S.add(arbre(700, 650, 0.9))
    S.add(planche(520, 712, 300, 28, rot=-4))
    S.add(g([trait(390 + k * 30, 735, 370 + k * 30, 735, "#5c3a1e", 3, opacity=0.6) for k in range(9)]))
    S.add(castor(300, 770, 1.15, expr="concentre", bras="tire", rot=-10))
    S.add(goutte(230, 520, 0.9, "#74c0fc"), goutte(380, 500, 0.7, "#74c0fc"))
    S.add(texte(560, 230, "Grrr… ça frotte !", 54, "#e8590c", contour="#fff"))
    return S


def p03():
    S = Scene()
    foret(S, 4)
    for x in (360, 470, 580):
        S.add(rondin(x, 700, 24))
    S.add(planche(470, 663, 340, 28))
    S.add(ecureuil(160, 770, 0.95, expr="rire", bras="pousse"))
    S.add(fleche(610, 590, 730, 590, "#e8590c"))
    S.add(castor(720, 790, 0.9, expr="surpris", bras="haut"))
    S.add(texte(420, 230, "Ça roule !", 70, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    foret(S, 5)
    S.add(arbre(120, 650, 0.8))
    S.add(brouette(560, 760, 1.2))
    S.add(castor(200, 770, 1.0, expr="rire", bras="tire"))
    S.add(mouvement(110, 620, 1.0), texte(420, 220, "Tout léger !", 64, "#e8590c", contour="#fff"))
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(650, 90, 0.5))
    # la colline à gravir : à gauche, le raidillon ; à droite, la rampe douce
    S.add(chemin("M 0 800 L 0 700 L 200 700 L 360 330 L 420 330 L 800 700 L 800 800 Z", "#8ce99a"))
    S.add(trait(205, 698, 358, 335, "#e03131", 8, stroke_dasharray="4 14"))
    S.add(chemin("M 420 330 L 800 690", stroke="#f59f00", sw=10, stroke_dasharray="4 14"))
    S.add(grand_chene_mini(390, 330))
    S.add(texte(170, 400, "Trop raide !", 44, "#e03131", contour="#fff"))
    S.add(texte(590, 440, "En pente douce ?", 40, "#f08c00", contour="#fff"))
    S.add(castor(100, 790, 0.85, expr="inquiet", bras="pense", regard=(1, -1)))
    S.add(brouette(330, 790, 0.6, flip=True))
    return S


def grand_chene_mini(x, y):
    return place([rect(-14, -120, 28, 120, "#8d5524"), cercle(0, -150, 60, "#51cf66"), cercle(-40, -120, 40, "#40c057"), cercle(40, -120, 40, "#40c057")], x, y)


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(chemin("M 0 800 L 0 330 L 120 330 L 800 700 L 800 800 Z", "#8ce99a"))
    S.add(chemin("M 120 330 L 800 700", stroke="#f59f00", sw=12))
    S.add(grand_chene_mini(60, 330))
    ang = -math.degrees(math.atan2(370, 680))
    S.add(g(brouette(430, 520, 0.8, flip=True), transform=f"rotate({n(ang)} 430 520)"))
    S.add(castor(560, 600, 0.9, expr="content", bras="tire", flip=True, rot=ang))
    S.add(texte(470, 200, "Plus long…", 56, "#f08c00", contour="#fff"), texte(500, 270, "mais moins dur !", 56, "#f08c00", contour="#fff"))
    return S


def p07():
    S = Scene()
    foret(S, 6)
    grand_chene(S, 560, 700, plateforme=True)
    S.add(castor(480, 318, 0.8, expr="oups", bras="haut", flip=True))
    S.add(corde("M 425 186 L 425 600"))
    S.add(planche(425, 610, 220, 26, rot=90))
    S.add(texte(200, 240, "Hiiii…", 60, "#e8590c", contour="#fff"), texte(200, 320, "trop lourd !", 50, "#e8590c", contour="#fff"))
    S.add(ecureuil(200, 770, 0.8, expr="concentre", bras="pense", regard=(1, -1)))
    return S


def p08():
    S = Scene()
    foret(S, 7)
    grand_chene(S, 610, 700, branche=True, plateforme=True)
    S.add(poulie(358, 250, 28))
    S.add(corde("M 386 250 L 386 470"), planche(386, 545, 150, 24, rot=90))
    S.add(corde("M 330 250 L 330 575"))
    S.add(castor(260, 760, 1.1, expr="content", bras="haut", regard=(1, -1)))
    S.add(fleche(150, 440, 150, 560, "#e03131"), fleche(470, 640, 470, 520, "#2f9e44"))
    S.add(texte(130, 400, "Je tire en bas…", 34, "#e03131", contour="#fff", anchor="start"))
    S.add(texte(470, 690, "… ça monte !", 34, "#2f9e44", contour="#fff"))
    return S


def p09():
    S = Scene()
    fond(S, "#fff9db")
    S.add(rect(150, 120, 480, 30, "#8d5524", rx=6))
    # poulie fixe F (350, 200) et poulie mobile M (410, 480), rayon 30
    S.add(trait(350, 150, 350, 170, "#495057", 6), trait(440, 150, 440, 160, "#495057", 6))
    S.add(corde("M 440 150 L 440 480 A 30 30 0 0 1 380 480 L 380 200 A 30 30 0 0 0 320 200 L 320 595"))
    S.add(poulie(350, 200, 30, crochet=0))
    S.add(cercle(410, 480, 34, "#495057"), cercle(410, 480, 26, "#adb5bd"), cercle(410, 480, 5, ENCRE))
    S.add(trait(410, 480, 410, 540, "#495057", 6), caisse(410, 540, 120, 90))
    S.add(castor(250, 780, 1.0, expr="fier", bras="haut", regard=(1, -1)))
    S.add(fleche(470, 330, 470, 260, "#2f9e44", sw=5, tete=14), fleche(500, 330, 500, 260, "#2f9e44", sw=5, tete=14))
    S.add(texte(520, 300, "2 brins", 36, "#2f9e44", anchor="start"))
    S.add(texte(560, 360, "portent", 32, "#2f9e44", anchor="start"), texte(560, 400, "la caisse", 32, "#2f9e44", anchor="start"))
    S.add(texte(400, 70, "Deux poulies : deux fois moins de force", 34, ENCRE))
    return S


def p10():
    S = Scene()
    foret(S, 8)
    grand_chene(S, 640, 700, branche=True, plateforme=True)
    S.add(poulie(388, 250, 28))
    S.add(corde("M 416 250 L 416 420"), planche(416, 470, 120, 24, rot=90))
    S.add(corde("M 360 250 L 360 620 Q 260 690 60 690"))
    for x, f, s in ((330, castor, 0.95), (230, ecureuil, 0.75), (140, herisson, 0.65), (60, souris, 0.5)):
        S.add(f(x, 790, s, expr="rire", bras="tire", flip=True, rot=6))
    S.add(texte(250, 300, "Oh hisse !", 64, "#e8590c", contour="#fff"))
    return S


def p11():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(texte(400, 80, "Des machines simples, partout !", 40, ENCRE))
    cadres = [(30, 120), (420, 120), (225, 450)]
    for x, y in cadres:
        S.add(rect(x, y, 350, 310, "#e7f5ff", rx=20, stroke="#adb5bd", stroke_width=4))
    S.add(puits(205, 410, 0.6), texte(205, 160, "le puits", 32, "#1971c2"))
    S.add(grue(560, 410, 0.75), texte(690, 160, "la grue", 32, "#1971c2"))
    S.add(velo(400, 730, 1.0), texte(400, 490, "le vélo", 32, "#1971c2"))
    return S


def p12():
    S = Scene()
    foret(S, 9)
    S.add(soleil(90, 90, 40))
    grand_chene(S, 520, 700, cabane=True, branche=True, fete=True)
    S.add(castor(400, 318, 0.6, expr="rire", bras="haut"), ecureuil(620, 318, 0.55, expr="rire", bras="salut"))
    S.add(poulie(270, 248, 26), corde("M 296 248 L 296 330"), panier_corde(296, 330, 0.8))
    S.add(corde("M 244 248 L 244 640"))
    S.add(herisson(190, 770, 0.8, expr="rire", bras="haut", regard=(1, -1)), souris(320, 780, 0.6, expr="rire", bras="danse"))
    S.add(notes(640, 520, 1.0, "#e8590c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("castor-seul.svg", vignette),
    ("01-le-reve.svg", p01), ("02-ca-frotte.svg", p02), ("03-les-rondins.svg", p03), ("04-la-brouette.svg", p04),
    ("05-trop-raide.svg", p05), ("06-la-rampe.svg", p06), ("07-trop-lourd.svg", p07), ("08-la-poulie.svg", p08),
    ("09-deux-poulies.svg", p09), ("10-oh-hisse.svg", p10), ("11-partout.svg", p11), ("12-la-fete.svg", p12),
]
