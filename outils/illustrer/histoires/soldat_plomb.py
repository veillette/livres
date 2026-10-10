"""Le Stoïque Soldat de plomb — d'après Hans Christian Andersen, avec une fin heureuse.

Le dernier des vingt-cinq soldats de plomb n'a qu'une jambe : il n'y avait
plus assez de plomb. Sur la table, devant un château de papier, une
danseuse se tient sur une jambe, l'autre levée si haut derrière elle qu'il
croit qu'elle n'en a qu'une, comme lui. La nuit, le diable à ressort
grogne. Le lendemain, le soldat tombe de la fenêtre ; deux garçons le
mettent dans un bateau de papier ; un rat lui réclame son passeport ; le
bateau coule et un poisson l'avale. Le poisson est vendu au marché… et la
cuisinière de la même maison retrouve le soldat dedans ! De retour sur la
table, un coup de vent emporte la danseuse, qui se pose juste à côté de
lui. Ici, ni feu ni fonte : ils restent ensemble.

Plans : 1 moyen (les soldats) · 2 moyen (le château de papier) · 3 moyen
(minuit, le diable à ressort) · 4 large (la chute) · 5 large (le bateau de
papier) · 6 moyen (le rat) · 7 large (le poisson) · 8 moyen (le marché) · 9
moyen (la cuisine) · 10 gros plan (de retour) · 11 moyen (le coup de vent) ·
12 gros plan (ensemble).
"""
from contes import *
from base import _assombrir

ID = "soldat-plomb"

GARCON = dict(peau="claire", cheveux="blond", coiffure="raie", habit="#4dabf7", robe=False, jambes="#495057")
CUISINIERE = dict(stature="adulte", peau="rosee", cheveux="roux", coiffure="chignon", habit="#ffe8cc", robe=True, carrure="ronde",
                  nez="rond")
PECHEUR = dict(stature="adulte", peau="doree", cheveux="gris", coiffure="chauve_cote", habit="#1864ab", robe=False, jambes="#495057",
               barbe="#adb5bd", carrure="ronde")


def soldat(x, y, s=1.0, rot=0, expr="sourire", flip=False, deux_jambes=False):
    """Le soldat de plomb, sur une seule jambe, le fusil à l'épaule ; (x, y) = sous son socle.
    deux_jambes : ses vingt-quatre frères, eux, en ont deux."""
    peau = "#f3c3a0"
    m = [ellipse(0, -6, 40, 12, volume("#2f9e44", 0.3, 0.8)), rect(-40, -8, 80, 8, "#2b8a3e")]
    if deux_jambes:
        m += [rect(-20, -100, 18, 90, cylindre("#1c2a52", 0.3, 0.7)), rect(2, -100, 18, 90, cylindre("#1c2a52", 0.3, 0.7)),
              rect(-22, -26, 22, 18, "#212529", rx=4), rect(0, -26, 22, 18, "#212529", rx=4)]
    else:
        m += [rect(-11, -100, 22, 90, cylindre("#1c2a52", 0.3, 0.7)), rect(-13, -26, 26, 18, "#212529", rx=4)]
    m += [rect(-32, -176, 64, 84, volume("#e03131", 0.3, 0.8), rx=12),
         trait(-28, -170, 26, -100, "#fff", 6), trait(28, -170, -26, -100, "#fff", 6),
         cercle(0, -150, 4, OR), cercle(0, -130, 4, OR), cercle(0, -112, 4, OR),
         rect(-46, -172, 16, 70, volume("#e03131", 0.3, 0.8), rx=8), cercle(-38, -100, 8, peau),
         rect(30, -172, 16, 60, volume("#e03131", 0.3, 0.8), rx=8),
         trait(46, -96, 50, -260, "#8d5524", 6), trait(50, -260, 50, -290, "#adb5bd", 3), cercle(40, -108, 8, peau),
         cercle(0, -204, 26, volume(peau, 0.3, 0.85)),
         cercle(-9, -208, 3, ENCRE), cercle(9, -208, 3, ENCRE), chemin("M -12 -196 Q -6 -192 0 -196 Q 6 -192 12 -196", stroke="#4a2c17", sw=3)]
    if expr in ("sourire", "content"):
        m.append(chemin("M -6 -188 Q 0 -184 6 -188", stroke=ENCRE, sw=2))
    m += [rect(-24, -282, 48, 66, volume("#212529", 0.3, 0.8), rx=8), rect(-28, -222, 56, 8, "#495057", rx=3),
          cercle(0, -248, 6, OR), ellipse(0, -290, 10, 16, "#e03131")]
    return place(m, x, y, s, rot=rot, flip=flip) + occuper(x - 50 * s, y - 300 * s, x + 56 * s, y)


def danseuse(x, y, s=1.0, rot=0, expr="sourire"):
    """La danseuse de papier, sur la pointe d'un pied, l'autre jambe cachée derrière son tutu ; (x, y) = sous son pied."""
    peau = "#ffe3d3"
    m = [ellipse(0, -4, 26, 6, "#000", opacity=0.08),
         rect(-6, -100, 12, 96, peau, rx=5), ellipse(0, -4, 8, 5, "#f783ac"),
         chemin("M -70 -110 Q 0 -150 70 -110 Q 50 -86 0 -84 Q -50 -86 -70 -110 Z", "#fff0f6", stroke="#fcc2d7", sw=3),
         chemin("M -60 -112 Q 0 -96 60 -112", stroke="#fcc2d7", sw=2),
         rect(-18, -170, 36, 64, volume("#ffdeeb", 0.2, 0.85), rx=10),
         chemin("M -16 -160 Q -60 -200 -40 -250", stroke=peau, sw=9), chemin("M 16 -160 Q 60 -200 40 -250", stroke=peau, sw=9),
         chemin("M -20 -162 Q 0 -150 20 -162 L 34 -120", stroke="#4dabf7", sw=5), place(etoile5(0, 0, 9, OR), 34, -118),
         cercle(0, -194, 22, volume(peau, 0.3, 0.88)), chemin("M -22 -200 Q -20 -224 0 -224 Q 20 -224 22 -200 Q 10 -212 0 -212 Q -10 -212 -22 -200 Z", "#4a2c17"),
         cercle(0, -228, 10, "#4a2c17"),
         chemin("M -10 -194 q 4 4 8 0 M 2 -194 q 4 4 8 0" if expr == "dort" else "M -9 -196 l 0 1 M 9 -196 l 0 1", stroke=ENCRE, sw=3),
         chemin("M -5 -184 Q 0 -180 5 -184", stroke="#e64980", sw=2), cercle(-12, -186, 4, "#ffa8a8", opacity=0.6), cercle(12, -186, 4, "#ffa8a8", opacity=0.6)]
    return place(m, x, y, s, rot=rot) + occuper(x - 70 * s, y - 260 * s, x + 70 * s, y)


def chateau_papier(x, y, s=1.0):
    m = [rect(-160, -200, 320, 200, "#fff", stroke="#dee2e6", stroke_width=3)]
    for px in (-160, 100):
        m += [rect(px, -290, 60, 290, "#fff", stroke="#dee2e6", stroke_width=3), poly([(px - 6, -290), (px + 30, -350), (px + 66, -290)], "#ffdeeb", stroke="#fcc2d7", stroke_width=3)]
    for px in (-130, -60, 30, 120):
        m.append(rect(px, -150, 30, 40, "#d0ebff", stroke="#a5d8ff", stroke_width=2))
    m += [rect(-40, -110, 80, 110, "#fff0f6", stroke="#fcc2d7", stroke_width=3, rx=36),
          ellipse(240, -14, 80, 16, "#a5d8ff", stroke="#74c0fc", stroke_width=2),
          chemin("M 220 -20 q 10 -24 20 -6 q 6 -4 14 0 L 244 -12 Z", "#fff", stroke="#adb5bd", sw=2)]
    for k in range(4):
        m.append(place([trait(0, 0, 0, -24, "#2f9e44", 3), ellipse(0, -28, 10, 6, "#51cf66")], -200 + k * 20 if k < 2 else 180 + k * 30, 0))
    return place(m, x, y, s)


def diable(x, y, s=1.0, sorti=True, expr="malin"):
    """Le diable à ressort : une boîte d'où jaillit un petit lutin vert à bonnet pointu."""
    m = [rect(-60, -100, 120, 100, volume("#7048e8", 0.3, 0.8), rx=8), place(etoile5(0, 0, 14, OR), 0, -50)]
    if sorti:
        m += [chemin("M 0 -100 " + " ".join(f"q {14 if k % 2 else -14} -10 0 -20" for k in range(6)), stroke="#adb5bd", sw=5),
              cercle(0, -250, 40, volume("#69db7c", 0.3, 0.8)), poly([(-34, -270), (0, -340), (34, -270)], "#e03131"), cercle(0, -342, 8, OR),
              cercle(-14, -256, 6, ENCRE), cercle(14, -256, 6, ENCRE), chemin("M -16 -232 Q 0 -218 16 -232", stroke=ENCRE, sw=3),
              chemin("M -26 -270 l 14 6 M 26 -270 l -14 6", stroke=ENCRE, sw=3) if expr == "fache" else ""]
        m.append(rect(-80, -120, 70, 14, "#5f3dc4", rx=4))
    else:
        m.append(rect(-64, -112, 128, 14, "#5f3dc4", rx=4))
    return place(m, x, y, s)


def bateau_papier(x, y, s=1.0, rot=0):
    m = [poly([(-80, -30), (80, -30), (50, 10), (-50, 10)], "#f8f9fa", stroke="#adb5bd", stroke_width=3),
         poly([(-30, -30), (0, -90), (30, -30)], "#fff", stroke="#adb5bd", stroke_width=3), trait(0, -90, 0, -30, "#dee2e6", 2)]
    for k in range(4):
        m.append(trait(-60 + k * 30, -20, -40 + k * 30, -4, "#ced4da", 2))
    return place(m, x, y, s, rot=rot)


def gros_poisson(x, y, s=1.0, flip=False, bouche=False):
    m = [poly([(-130, 0), (-200, -60), (-190, 0), (-200, 60)], "#5c7cfa"),
         ellipse(0, 0, 150, 80, volume("#748ffc", 0.35, 0.8)), ellipse(10, 30, 110, 36, "#dbe4ff"),
         chemin("M -20 -76 Q 20 -120 60 -74", "#5c7cfa"), cercle(90, -20, 16, "#fff"), cercle(94, -20, 8, ENCRE)]
    if bouche:
        m.append(ellipse(140, 14, 20, 24, "#364fc7"))
    else:
        m.append(chemin("M 120 20 Q 136 24 146 14", stroke="#364fc7", sw=4))
    for k in range(5):
        m.append(chemin(f"M {-60 + k * 30} -40 q 10 10 0 20", stroke="#5c7cfa", sw=3, opacity=0.6))
    return place(m, x, y, s, flip=flip)


def chambre(S, nuit_=False):
    piece(S, "chambre", y=600)
    if nuit_:
        S.ambiance("nuit")
    S.add(fenetre(560, 80, 180, 200, "#364fc7" if nuit_ else "#a5d8ff", nuit_=nuit_, rideaux="#ffc9c9"))


def table_jouets(S, y=640):
    """Le dessus de la table, vu de près : c'est le monde des jouets."""
    S.add(rect(0, y, 800, 800 - y, volume("#c68642", 0.2, 0.8)), rect(0, y, 800, 14, "#deb887"))


def rue_pluie(S):
    ciel(S, "#868e96", "#ced4da")
    S._decor("pluie")
    for k, (bx, c) in enumerate(((0, "#ffd8a8"), (260, "#d3f9d8"), (520, "#e5dbff"))):
        S.add(rect(bx, 120, 260, 420, c), rect(bx, 100, 260, 26, _assombrir(c, 0.8)))
        for j in range(2):
            for i in range(3):
                S.add(rect(bx + 30 + i * 76, 170 + j * 130, 48, 70, "#a5d8ff", stroke="#fff", stroke_width=4))
    S.add(rect(0, 540, 800, 120, "#adb5bd"), rect(0, 660, 800, 140, "#868e96"))
    S.add(chemin("M 0 680 L 800 700 L 800 740 L 0 720 Z", "#74c0fc"))
    pluie(S, 70, graine=3)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    chambre(S)
    table_jouets(S, 600)
    S.add(chateau_papier(560, 640, 0.9))
    S.add(danseuse(560, 640, 1.1))
    S.add(soldat(230, 760, 1.5, expr="content"))
    S.add(coeur(390, 330, 1.0, "#ff8787"))
    S.cachette(740, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(soldat(200, 262, 0.82))
    return S


def p01():
    """Plan moyen : pour son anniversaire, un garçon ouvre une boîte : vingt-cinq soldats de plomb ; le dernier n'a qu'une jambe."""
    S = Scene()
    chambre(S)
    S.add(personne(160, 800, 1.5, expr="joie", bras="joues", regard=(1, 0.5), **GARCON))
    S.add(table(520, 800, 520, 170, nappe="#fff3bf"))
    S.add(rect(290, 540, 460, 80, volume("#4dabf7", 0.3, 0.8), rx=6))
    for k in range(9):
        S.add(soldat(320 + k * 46, 600, 0.32, deux_jambes=k < 8))
    S.add(texte(500, 140, "Vingt-cinq soldats !", 50, "#c92a2a", contour="#fff"))
    S.add(bulle(560, 330, 400, 90, "Celui-là n'a qu'une jambe !", 28, pointe=(690, 520)))
    return S


def p02():
    """Plan moyen : sur la table, devant un château de papier, la danseuse sur une jambe ; le soldat la regarde."""
    S = Scene()
    chambre(S)
    table_jouets(S, 620)
    S.add(chateau_papier(560, 660, 0.95))
    S.add(danseuse(560, 660, 1.15))
    S.add(soldat(210, 780, 1.4, expr="content"))
    S.add(coeur(350, 330, 0.9, "#ff8787"), coeur(400, 280, 0.6, "#ffa8a8"))
    return S


def p03():
    """Plan moyen : à minuit, les jouets s'animent ; le diable à ressort jaillit de sa boîte : « Ne la regarde pas ! »"""
    S = Scene()
    chambre(S, nuit_=True)
    table_jouets(S, 620)
    S.add(chateau_papier(600, 660, 0.8), danseuse(600, 660, 0.95))
    S.add(diable(400, 760, 1.1, expr="fache"))
    S.add(soldat(170, 780, 1.3))
    S.add(horloge(110, 130, 50, 12, 0, "#fff9db", OR_FONCE))
    S.add(bulle(420, 130, 340, 90, "Ne la regarde pas !", 34, pointe=(420, 330)))
    return S


def p04():
    """Plan large : le matin, sur le rebord de la fenêtre ouverte, un courant d'air fait tomber le soldat dans la rue."""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 0, 800, 800, "#ffe8cc"))
    S.add(rect(160, 120, 480, 480, "#a5d8ff"), rect(150, 590, 500, 30, "#fff"))
    S.add(rect(160, 120, 30, 480, "#fff"), rect(610, 120, 30, 480, "#fff"))
    S.add(poly([(610, 120), (760, 80), (760, 640), (610, 600)], "#e7f5ff", stroke="#fff", stroke_width=8))
    for k in range(3):
        S.add(chemin(f"M {300 + k * 40} {300 + k * 40} q 60 -20 120 0 q 60 20 120 0", stroke="#fff", sw=5, opacity=0.8))
    S.add(soldat(420, 470, 0.9, rot=150))
    S.add(texte(400, 70, "Oh non !", 56, "#c92a2a", contour="#fff"))
    S.cachette(80, 780)
    return S


def p05():
    """Plan large : sous la pluie, deux garçons posent le soldat dans un bateau de papier sur le ruisseau du caniveau."""
    S = Scene()
    rue_pluie(S)
    S.add(personne(180, 800, 1.35, expr="rire", bras="designe", regard=(1, 0.6), **GARCON))
    S.add(personne(640, 800, 1.35, expr="rire", bras="applaudit", flip=True, regard=(-1, 0.6), peau="foncee", cheveux="noir", coiffure="courts",
                   habit="#fab005", robe=False, jambes="#495057"))
    S.add(bateau_papier(420, 712, 1.0, rot=3))
    S.add(soldat(420, 690, 0.42))
    S.add(texte(400, 70, "En bateau !", 52, "#1c7ed6", contour="#fff"))
    return S


def p06():
    """Plan moyen : sous le pont, dans le noir, un rat d'eau : « Ton passeport ! » ; le soldat reste bien droit."""
    S = Scene()
    fond(S, "#212529")
    S.add(chemin("M 0 0 L 800 0 L 800 300 Q 400 120 0 300 Z", "#495057"), pierres(0, 0, 800, 240, "#495057", opacite=0.4))
    S.add(rect(0, 560, 800, 240, lineaire([(0, "#364fc7"), (1, "#1c2a52")])))
    S.add(bateau_papier(500, 600, 1.6))
    S.add(soldat(500, 560, 0.75))
    S.add(perso("rat", 210, 560, 0.75, expr="fache", bras="designe", regard=(1, 0)))
    S.add(rect(80, 560, 260, 20, "#868e96"))
    S.add(bulle(260, 150, 300, 90, "Ton passeport !", 36, pointe=(230, 330)))
    S.cachette(740, 540, "air")
    return S


def p07():
    """Plan large : dans le canal, le bateau coule… et un gros poisson avale le soldat. Gloup !"""
    S = Scene()
    S._decor("eau")
    S.add(rect(0, 0, 800, 800, lineaire([(0, "#4dabf7"), (1, "#1864ab")])))
    S.add(bateau_papier(200, 220, 1.0, rot=40))
    S.add(gros_poisson(460, 480, 1.4, bouche=True))
    S.add(soldat(670, 500, 0.4, rot=-60))
    for k in range(6):
        S.add(cercle(250 + k * 30, 300 - k * 30, 6 + k % 3 * 2, "#fff", opacity=0.6))
    S.add(texte(400, 100, "Gloup !", 64, "#fff", contour="#1864ab"))
    S.cachette(90, 720, "poisson")
    return S


def p08():
    """Plan moyen : au marché, le pêcheur vend le gros poisson à la cuisinière."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(rect(0, 560, 800, 240, "#ced4da"))
    S.add(rect(240, 380, 340, 200, volume("#e8c39e", 0.2, 0.85)), poly([(220, 380), (600, 380), (560, 300), (260, 300)], "#fa5252"))
    for k in range(5):
        S.add(poly([(260 + k * 68, 300), (294 + k * 68, 300), (300 + k * 68, 380), (254 + k * 68, 380)], "#fff", opacity=0.6 if k % 2 else 0))
    S.add(personne(410, 600, 1.2, expr="content", bras="tend", **PECHEUR))
    S.add(rect(240, 540, 340, 60, "#a0693a"))
    S.add(gros_poisson(400, 520, 0.5))
    S.add(personne(660, 800, 1.5, expr="content", bras="designe", flip=True, regard=(-1, -0.3), **CUISINIERE))
    S.add(texte(400, 120, "Au marché", 52, "#c92a2a", contour="#fff"))
    return S


def p09():
    """Plan moyen : dans la cuisine de la même maison, la cuisinière ouvre le poisson et y trouve le soldat : « Ça alors ! »"""
    S = Scene()
    piece(S, "cuisine", y=600)
    S.add(personne(470, 800, 1.6, expr="surpris", bras="tient", regard=(-0.5, -0.3), objet=soldat(68, -150, 0.25), **CUISINIERE))
    S.add(table(380, 800, 420, 130, nappe="#e7f5ff"))
    S.add(gros_poisson(330, 640, 0.6))
    S.add(personne(160, 800, 1.45, expr="bouche_bee", bras="joues", regard=(1, -0.3), **GARCON))
    S.add(bulle(560, 150, 260, 90, "Ça alors !", 38, pointe=(520, 310)))
    return S


def p10():
    """Gros plan : de retour sur la table, le soldat revoit le château de papier et la danseuse."""
    S = Scene()
    chambre(S)
    table_jouets(S, 600)
    S.add(chateau_papier(600, 640, 1.0), danseuse(590, 640, 1.2))
    S.add(soldat(240, 800, 1.8, expr="content"))
    S.add(coeur(400, 300, 1.2, "#ff8787"))
    S.add(texte(400, 120, "Te revoilà !", 54, "#c92a2a", contour="#fff"))
    return S


def p11():
    """Plan moyen : la fenêtre s'ouvre, un coup de vent emporte la danseuse comme une plume… vers le soldat."""
    S = Scene()
    chambre(S)
    table_jouets(S, 620)
    S.add(chateau_papier(620, 660, 0.8))
    for k in range(4):
        S.add(chemin(f"M {720 - k * 20} {200 + k * 40} q -80 -20 -160 10 q -80 30 -160 0", stroke="#fff", sw=6, opacity=0.8))
    S.add(danseuse(420, 470, 1.0, rot=-25))
    S.add(soldat(220, 780, 1.4, expr="content"))
    S.add(texte(400, 100, "Hop, un coup de vent !", 48, "#1c7ed6", contour="#fff"))
    return S


def p12():
    """Gros plan : la danseuse s'est posée juste à côté du soldat ; ils restent ensemble, pour toujours."""
    S = Scene()
    chambre(S, nuit_=True)
    table_jouets(S, 600)
    S.add(coeur(400, 330, 3.2, "#ffdeeb"))
    S.add(soldat(330, 790, 1.6, expr="content"))
    S.add(danseuse(470, 790, 1.5))
    S.add(diable(680, 740, 0.7, sorti=False))
    S.add(texte(400, 110, "Ensemble", 60, "#c2255c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("soldat-seul.svg", vignette),
    ("01-vingt-cinq-soldats.svg", p01), ("02-la-danseuse.svg", p02), ("03-minuit.svg", p03),
    ("04-la-chute.svg", p04), ("05-le-bateau.svg", p05), ("06-le-rat.svg", p06),
    ("07-le-poisson.svg", p07), ("08-le-marche.svg", p08), ("09-la-cuisine.svg", p09),
    ("10-te-revoila.svg", p10), ("11-le-coup-de-vent.svg", p11), ("12-ensemble.svg", p12),
]
