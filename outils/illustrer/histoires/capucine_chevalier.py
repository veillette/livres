"""Capucine, princesse chevalier — être soi-même."""
from base import *
from objets import *
from fantastique import *

ID = "capucine-chevalier"
# Capucine : peau claire, tresses rousses, tunique verte et pantalon (ou robe rose au tournoi)
CAPU = dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#74b816", robe=False,
            jambes="#8d5524", chaussures="#5c3a1e", acc=("diademe",))
CAPU_ROBE = {**CAPU, "habit": "#f783ac", "robe": True, "chaussures": "#c2255c"}
REINE = dict(peau="claire", cheveux="roux", habit="#7048e8", cape="#c92a2a")
ROI = dict(peau="claire", cheveux="chatain", barbe="#8d5524", coiffure="chauve_cote")
MYRTILLE = dict(couleur="#9775fa", ventre="#e5dbff")
BOUE = "#8b5e3c"
BOUE2 = "#a47148"


def capu(x, y, s=1.0, robe=False, **k):
    return personne(x, y, s, **{**(CAPU_ROBE if robe else CAPU), **k})


def myrtille(x, y, s=1.0, **k):
    return dragon(x, y, s, **{**MYRTILLE, **k})


# --- accessoires et décors propres au livre ---------------------------------

def epee_bois(x, y, s=1.0, rot=0):
    """Épée de bois ; (x, y) = poignée."""
    m = [rect(-7, -10, 14, 34, "#8d5524", rx=5),
         rect(-28, -18, 56, 12, "#5c3a1e", rx=5),
         chemin("M -10 -18 L -10 -150 L 0 -172 L 10 -150 L 10 -18 Z", "#d9a066"),
         trait(0, -24, 0, -150, "#c68642", 3)]
    return place(m, x, y, s, rot=rot)


def taches(x, y, s=1.0):
    """Éclaboussures de boue sur un personnage debout placé en (x, y)."""
    m = [ellipse(-18, -60, 9, 6, BOUE), ellipse(14, -36, 11, 7, BOUE), ellipse(-8, -86, 6, 4, BOUE),
         ellipse(22, -78, 5, 4, BOUE), ellipse(34, -132, 6, 4, BOUE), ellipse(-14, -18, 8, 5, BOUE)]
    return place(m, x, y, s)


def flaque_boue(x, y, s=1.0, rx=160, ry=36):
    m = [ellipse(0, 0, rx, ry, BOUE), ellipse(-rx * 0.3, -ry * 0.2, rx * 0.35, ry * 0.3, BOUE2),
         ellipse(rx * 0.4, ry * 0.1, rx * 0.2, ry * 0.25, BOUE2)]
    return place(m, x, y, s)


def gicle(x, y, s=1.0):
    """Gerbe de boue."""
    m = []
    for k, (dx, dy, r) in enumerate([(-70, -70, 12), (-40, -110, 10), (0, -130, 13), (44, -104, 10),
                                     (74, -64, 12), (-96, -30, 8), (96, -26, 8)]):
        m.append(cercle(dx, dy, r, BOUE if k % 2 else BOUE2))
    return place(m, x, y, s)


def mare_boue(S, y=600, avant=False):
    """Grande mare de boue au bord du champ du tournoi. avant=True : le bord qui passe devant."""
    if avant:
        S.add(chemin(f"M 60 {y + 60} Q 400 {y + 130} 760 {y + 60} L 760 {y + 120} Q 400 {y + 190} 60 {y + 120} Z", BOUE))
        return
    S.add(ellipse(410, y + 70, 360, 90, BOUE))
    S.add(ellipse(300, y + 50, 120, 22, BOUE2), ellipse(560, y + 90, 80, 16, BOUE2))


def boue_devant(x, y, w=140, h=46):
    """Bord de boue posé devant un personnage enlisé ; (x, y) = niveau de la boue."""
    return g([ellipse(x, y + h * 0.4, w, h, BOUE),
              ellipse(x - w * 0.3, y + 4, w * 0.3, h * 0.25, BOUE2),
              cercle(x + w * 0.5, y - 4, 9, BOUE), cercle(x - w * 0.6, y, 7, BOUE)])


def planche(x, y, w=180, rot=0):
    m = [rect(-w / 2, -14, w, 28, "#c68642", rx=5),
         trait(-w / 2 + 10, -4, w / 2 - 30, -4, "#a0693a", 3),
         cercle(-w / 2 + 14, 0, 3.5, "#5c3a1e"), cercle(w / 2 - 14, 0, 3.5, "#5c3a1e")]
    return place(m, x, y, 1.0, rot=rot)


def cabane(x, y, s=1.0, lumiere=False):
    """Cabane perchée dans un arbre ; (x, y) = pied du tronc."""
    toit = [(-146, -466), (0, -560), (146, -466)]
    m = [ombre_sol(6, 0, 70, 10, 0.18),
         rect(-34, -330, 68, 330, cylindre("#8d5524", 0.25, 0.65), rx=12),
         chemin("M -14 -40 q 4 -40 0 -80 M 10 -150 q -4 -36 2 -72 M -8 -250 q 3 -24 0 -48", stroke="#5c3a1e", sw=3, opacity=0.55),
         cercle(-150, -470, 90, volume("#2f9e44", 0.28, 0.72)), cercle(150, -470, 90, volume("#2f9e44", 0.28, 0.72)),
         cercle(0, -540, 120, volume("#37b24d", 0.28, 0.75)), cercle(-90, -560, 80, "#40c057", opacity=0.7),
         rect(-34, -330, 68, 40, "#000", opacity=0.2),
         rect(-150, -330, 300, 22, cylindre("#a0693a", 0.25, 0.7, vertical=True), rx=6),
         rect(-146, -308, 292, 10, "#000", opacity=0.15, rx=4),
         rect(-120, -470, 240, 140, cylindre("#d9a066", 0.2, 0.78)),
         planches(-120, -470, 240, 140, "#d9a066", larg=24, vertical=False),
         ombre_avancee(-120, -468, 240, 20, 0.28),
         poly(toit, lineaire([(0, "#e85050"), (0.5, "#c92a2a"), (1, "#861b1b")], 0, 0, 1, 1)),
         tuiles(-146, -560, 292, 95, "#c92a2a", poly(toit, "#000")),
         chemin("M -146 -466 L 0 -560 L 146 -466", stroke="#7a1515", sw=6),
         rect(-34, -444, 68, 114, "#a0693a", rx=10),
         rect(-30, -440, 60, 110, cylindre("#5c3a1e", 0.2, 0.7), rx=8),
         cercle(18, -386, 4, volume("#ffd43b", 0.6, 0.7)),
         rect(46, -450, 54, 48, "#a0693a", rx=6),
         rect(50, -446, 46, 40, "#ffe066" if lumiere else "#a5d8ff", rx=4),
         poly([(54, -406), (66, -446), (74, -446), (62, -406)], "#fff", opacity=0.35),
         trait(110, -560, 110, -640, "#495057", 4),
         poly([(110, -640), (160, -626), (110, -612)], "#fab005")]
    # échelle de corde
    for sgn in (-1, 1):
        m.append(trait(-100 + sgn * 20, -310, -100 + sgn * 20, -10, "#e9c46a", 4))
    for k in range(7):
        m.append(trait(-120, -280 + k * 40, -80, -280 + k * 40, "#c68642", 6))
    return place(m, x, y, s)


def fanions(y=60, couleurs=("#fa5252", "#fab005", "#74b816", "#4dabf7", "#cc5de8")):
    m = [chemin(f"M -10 {y} Q 400 {y + 70} 810 {y}", stroke="#495057", sw=3)]
    for k in range(14):
        x = 20 + k * 56
        t = x / 800
        yy = y + 70 * 2 * t * (1 - t) * 1.0 + 6
        m.append(poly([(x - 18, yy - 6), (x + 18, yy - 6), (x, yy + 30)], couleurs[k % len(couleurs)]))
    return g(m)


def tribune(x, y, w=420, h=200):
    """Estrade du tournoi ; (x, y) = sol. Les personnages se placent à y - h."""
    m = [rect(-w / 2, -h, w, h, "#e5dbff"),
         rect(-w / 2, -h, w, 20, "#9775fa")]
    for k in range(5):
        m.append(rect(-w / 2 + 20 + k * (w - 40) / 4 - 8, -h + 20, 16, h - 20, "#d0bfff"))
    for k in range(7):
        px = -w / 2 + k * w / 6
        m.append(poly([(px - 4, -h + 20), (px + w / 12, -h + 70), (px + w / 6 + 4, -h + 20)], "#fab005" if k % 2 else "#e64980"))
    return place(m, x, y)


def toit_tribune(x, y, w=460, haut=420):
    """Poteaux et toit rayé, au-dessus des personnages de la tribune."""
    m = [rect(-w / 2 + 10, -haut, 14, haut - 200, "#868e96"), rect(w / 2 - 24, -haut, 14, haut - 200, "#868e96")]
    for k in range(8):
        px = -w / 2 + k * w / 8
        m.append(poly([(px, -haut), (px + w / 8, -haut), (px + w / 8, -haut + 40), (px, -haut + 40)], "#fa5252" if k % 2 else "#fff"))
        m.append(chemin(f"M {px} {-haut + 40} Q {px + w / 16} {-haut + 64} {px + w / 8} {-haut + 40} Z", "#fa5252" if k % 2 else "#fff"))
    m.append(poly([(-w / 2 - 10, -haut), (0, -haut - 70), (w / 2 + 10, -haut)], "#fa5252"))
    return place(m, x, y)


def chausson(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 24, 12, "#c2255c"), ellipse(-6, -4, 10, 5, "#f783ac")], x, y, s, rot=rot)


def champ_tournoi(S, y=560):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(140, 140, 0.7), nuage(660, 110, 0.6))
    collines(S, y, "#b2f2bb", graine=6)
    S.add(chateau(640, y + 10, 0.5))
    sol(S, y, "#8ce99a")
    S.add(fanions())


# --- pages -------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin_chateau(S, "#ffd8a8", "#fff4e6", chateau_s=0.6, chateau_x=600, y=600)
    S.add(flaque_boue(330, 770, 1.0, rx=230, ry=34))
    S.add(gicle(300, 770, 1.0))
    S.add(capu(300, 770, 1.7, expr="rire", bras="tient", objet=epee_bois(68, -146, 1.0, rot=20)))
    S.add(taches(300, 770, 1.7))
    S.add(myrtille(590, 780, 1.25, expr="rire", bras="haut", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 236, 150, 26, BOUE), ellipse(150, 230, 50, 8, BOUE2))
    S.add(epee_bois(150, 220, 1.2, rot=35))
    S.add(couronne_objet(250, 226, 1.1, rot=-8))
    S.add(cercle(320, 120, 8, BOUE), cercle(90, 140, 6, BOUE2), cercle(340, 170, 5, BOUE))
    return S


def p01():
    S = Scene()
    jardin_chateau(S, "#a5d8ff", "#fff4e6", chateau_s=0.8, chateau_x=520, y=600)
    S.add(flaque_boue(260, 760, 1.0, rx=200, ry=36))
    S.add(gicle(260, 760, 1.2))
    S.add(capu(260, 760, 1.5, expr="rire", bras="tient", objet=epee_bois(68, -146, 1.0, rot=25)))
    S.add(taches(260, 760, 1.5))
    S.add(texte(250, 160, "Splatch !", 72, BOUE, contour="#fff"))
    S.add(fleur(640, 780, 1.0), fleur(700, 770, 0.9, "#ffd43b"), fleur(750, 790, 1.0, "#cc5de8"))
    return S


def salle(S):
    interieur(S, "#ffe8cc", "#c9a27e", 560, papier="#ffd8a8")
    S.add(fenetre(80, 120, 160, 170, "#a5d8ff", rideaux="#c92a2a", contenu=nuage(160, 200, 0.5)))
    for x in (520, 660):
        S.add(rect(x - 30, 120, 60, 130, "#c92a2a", rx=4), poly([(x - 30, 250), (x, 230), (x + 30, 250)], "#ffe8cc"),
              etoile5(x, 170, 16, OR))


def p02():
    S = Scene()
    salle(S)
    for k, (fx, fy) in enumerate([(70, 790), (120, 760), (170, 790), (220, 760)]):
        S.add(ellipse(fx, fy, 16, 9, BOUE, opacity=0.8))
    S.add(personne(500, 770, 1.45, expr="surpris", bras="joues", acc=("couronne",), **REINE))
    S.add(roi(670, 780, 1.3, expr="bouche_bee", bras="ouverts", **ROI))
    S.add(capu(260, 780, 1.35, expr="timide", bras="tient", regard=(1, 0), objet=epee_bois(68, -146, 0.9, rot=10)))
    S.add(taches(260, 780, 1.35), ellipse(260 - 28 * 1.35, 780 - 140 * 1.35, 8, 5, BOUE))
    S.add(bulle(500, 110, 520, 110, "Une princesse,\nça ne fait pas ça !", 40, pointe=(500, 420)))
    return S


def p03():
    S = Scene()
    salle(S)
    S.add(tapis(400, 720, 330, 60, "#d0bfff", "#9775fa"))
    S.add(personne(560, 740, 1.45, expr="content", bras="large", acc=("couronne",), **REINE))
    S.add(capu(250, 760, 1.3, robe=True, expr="oups", bras="equilibre", rot=-22))
    S.add(mouvement(150, 520, 1.0, rot=-30), mouvement(380, 540, 1.0, rot=200))
    S.add(texte(250, 400, "Oh là là…", 56, "#c2255c", contour="#fff"))
    S.cachette(280, 70, "air")
    return S


def p04():
    S = Scene()
    ciel(S, "#5f3dc4", "#ffa8a8")
    S.add(etoile5(120, 90, 10, "#fff3bf"), etoile5(300, 60, 8, "#fff3bf"), etoile5(700, 70, 9, "#fff3bf"))
    collines(S, 640, "#8ce99a", graine=2)
    S.add(chateau(670, 650, 0.45, nuit_=True))
    sol(S, 640, "#69db7c")
    S.add(cabane(330, 780, 1.0, lumiere=True))
    # Capucine assise sur la plateforme, devant la porte
    S.add(capu(330, 450, 0.85, expr="triste", bras="joues", regard=(0, 1)))
    S.add(epee_bois(450, 448, 0.6, rot=80))
    S.add(pensee(620, 200, 110, couronne_objet(620, 230, 1.0), depuis=(390, 330)))
    return S


def p05():
    S = Scene()
    champ_tournoi(S, 560)
    S.add(tribune(250, 620, 420, 220))
    S.add(roi(110, 400, 0.95, expr="content", bras="salut", **ROI))
    S.add(personne(370, 400, 1.0, expr="sourire", acc=("couronne",), **REINE))
    S.add(capu(240, 400, 0.85, robe=True, expr="baille", bras="bas"))
    S.add(toit_tribune(250, 620, 460, 470))
    S.add(chevalier(560, 790, 1.15, plumet="#fa5252", expr="fier", bras="poing"))
    S.add(chevalier(710, 780, 1.0, plumet="#4dabf7", expr="fier", bras="poing"))
    S.add(texte(250, 640, "Ennui, ennui…", 34, "#5f3dc4", contour="#fff"))
    return S


def p06():
    S = Scene()
    champ_tournoi(S, 520)
    mare_boue(S, 600)
    S.add(gicle(410, 590, 1.9))
    S.add(myrtille(410, 690, 1.25, expr="pleure", larmes=True, bras="haut", ailes="ouvertes"))
    S.add(boue_devant(410, 650, 170, 50))
    S.add(texte(410, 250, "PLOUF !", 96, "#5f3dc4", contour="#fff"))
    return S


def p07():
    S = Scene()
    champ_tournoi(S, 520)
    mare_boue(S, 600)
    S.add(myrtille(410, 650, 1.0, expr="pleure", larmes=True, bras="haut"))
    S.add(boue_devant(410, 610, 120, 40))
    for x, pl, ex in [(190, "#fa5252", "oups"), (630, "#4dabf7", "inquiet")]:
        S.add(chevalier(x, 780, 1.25, plumet=pl, expr=ex, bras="haut"))
        S.add(boue_devant(x, 690, 120, 50))
    S.add(texte(400, 200, "Gloup, gloup !", 70, "#495057", contour="#fff"))
    return S


def p08():
    S = Scene()
    champ_tournoi(S, 560)
    S.add(tribune(160, 620, 300, 220))
    S.add(personne(160, 400, 0.95, expr="surpris", bras="joues", acc=("couronne",), **REINE))
    S.add(toit_tribune(160, 620, 320, 470))
    S.add(capu(520, 780, 1.45, robe=True, expr="fier", bras="course", flip=True, chaussures="#fbd9bd"))
    S.add(chausson(370, 650, 1.2, rot=-40), chausson(330, 600, 1.2, rot=30))
    S.add(mouvement(380, 690, 1.0), mouvement(400, 740, 0.8))
    S.add(bulle(470, 110, 520, 110, "Une princesse,\nça ne fait pas ça !", 40, pointe=(230, 260)))
    S.add(texte(620, 280, "Celle-ci, si !", 50, "#c2255c", contour="#fff"))
    return S


def p09():
    S = Scene()
    champ_tournoi(S, 520)
    mare_boue(S, 600)
    S.add(planche(220, 690, 200, rot=-6), planche(380, 680, 200, rot=4))
    S.add(myrtille(620, 650, 0.95, expr="surpris", bras="haut", regard=(-1, 0)))
    S.add(boue_devant(620, 610, 110, 40))
    S.add(capu(130, 790, 1.3, robe=True, expr="concentre", bras="porte", chaussures="#fbd9bd",
               objet=planche(0, -76, 200, rot=-10)))
    S.add(taches(130, 790, 1.3))
    return S


def p10():
    S = Scene()
    champ_tournoi(S, 520)
    mare_boue(S, 600)
    S.add(planche(160, 700, 200, rot=-4), planche(320, 694, 200, rot=3))
    S.add(myrtille(590, 660, 1.15, expr="inquiet", bras="joues", regard=(-1, 0)))
    S.add(boue_devant(590, 620, 120, 40))
    S.add(chemin("M 520 470 Q 500 420 530 400 Q 560 380 540 340", stroke="#ced4da", sw=10, opacity=0.8))
    S.add(capu(330, 690, 1.3, robe=True, expr="sourire", bras="donne", regard=(1, 0), chaussures="#fbd9bd"))
    S.add(taches(330, 690, 1.3))
    S.add(bulle(330, 110, 560, 110, "N'aie pas peur.\nMoi, c'est Capucine.", 40, pointe=(330, 350)))
    return S


def p11():
    S = Scene()
    champ_tournoi(S, 520)
    mare_boue(S, 600)
    S.add(myrtille(620, 650, 1.0, expr="joie", bras="haut"))
    S.add(boue_devant(620, 610, 110, 36))
    S.add(chemin("M 40 740 L 207 723 L 347 723 L 506 686 Q 560 650 600 590", stroke="#e9c46a", sw=8))
    S.add(roi(110, 790, 1.05, expr="concentre", bras="tire", **ROI))
    S.add(chevalier(250, 790, 1.05, plumet="#fa5252", expr="concentre", bras="tire"))
    S.add(capu(400, 760, 1.15, robe=True, expr="rire", bras="tire", chaussures="#fbd9bd"))
    S.add(taches(400, 760, 1.15))
    S.add(texte(400, 230, "Un, deux, trois…", 56, "#495057", contour="#fff"))
    S.add(texte(400, 310, "HISSEZ !", 76, "#c2255c", contour="#fff"))
    return S


def p12():
    S = Scene()
    jardin_chateau(S, "#ffd8a8", "#fff4e6", chateau_s=0.7, chateau_x=400, y=600)
    S.add(flaque_boue(400, 780, 1.0, rx=300, ry=30))
    S.add(roi(130, 780, 1.25, expr="rire", bras="salut", **ROI))
    S.add(personne(660, 780, 1.3, expr="content", bras="ouverts", acc=("couronne",), **REINE))
    S.add(myrtille(470, 780, 1.05, expr="rire", bras="calin", regard=(-1, 0)))
    S.add(capu(310, 780, 1.3, robe=True, expr="rire", bras="haut", chaussures="#fbd9bd"))
    S.add(taches(310, 780, 1.3))
    S.add(coeur(400, 150, 1.6), coeur(460, 100, 1.0, "#ff8787"), coeur(340, 110, 0.9, "#f783ac"))
    S.cachette(730, 240, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("epee-couronne.svg", vignette),
    ("01-la-boue.svg", p01), ("02-pas-ca.svg", p02), ("03-reverence.svg", p03),
    ("04-la-cabane.svg", p04), ("05-le-tournoi.svg", p05), ("06-plouf.svg", p06),
    ("07-chevaliers.svg", p07), ("08-celle-ci-si.svg", p08), ("09-les-planches.svg", p09),
    ("10-n-aie-pas-peur.svg", p10), ("11-hissez.svg", p11), ("12-princesse-chevalier.svg", p12),
]
