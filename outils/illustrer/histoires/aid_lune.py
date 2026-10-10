"""La lune de l'Aïd — l'Aïd el-Fitr avec Yasmine.

Pendant le ramadan, les grands jeûnent du lever au coucher du soleil (pas
les enfants) ; au coucher du soleil, on rompt le jeûne avec une datte et de
l'eau. Le dernier soir, on guette le premier croissant de lune : juste après
le coucher du soleil, très fin, bas dans le ciel de l'ouest, sa partie
éclairée tournée vers le Soleil qui vient de se coucher. Henné la veille,
habits neufs, dons pour ceux qui en ont besoin, prière à la mosquée, « Aïd
moubarak ! », douceurs, visite aux grands-parents. Le lendemain soir, le
croissant est un peu plus épais et un peu plus haut.

Plans : 1 moyen (on attend le coucher du soleil) · 2 gros plan (la datte)
· 3 large (on guette la lune) · 4 gros plan (le croissant) · 5 moyen (le
henné) · 6 moyen (la robe neuve) · 7 moyen (le don) · 8 large (la mosquée)
· 9 gros plan (les douceurs) · 10 large (chez les grands-parents) ·
11 moyen (le croissant a grandi).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre

ID = "aid-lune"
PAPIER_PEINT = "losanges"

VERT = "#2b8a3e"
OR_ = "#fcc419"


def hijab(c="#e64980"):
    """Foulard qui couvre les cheveux et le cou, en laissant le visage libre (coiffe)."""
    d = ("M -62 -150 Q -66 -224 0 -226 Q 66 -224 62 -150 Q 64 -100 40 -92 L -40 -92 Q -64 -100 -62 -150 Z "
         "M -44 -142 Q -46 -194 0 -196 Q 46 -194 44 -142 Q 44 -106 0 -102 Q -44 -106 -44 -142 Z")
    return g([chemin(d, c, fill_rule="evenodd"), chemin("M -40 -206 Q 0 -218 40 -206", stroke=eclaircir(c, 0.4), sw=4, opacity=0.6)])


def kufi(c="#f8f9fa"):
    return g([chemin("M -48 -186 Q -48 -222 0 -222 Q 48 -222 48 -186 Z", c), rect(-50, -192, 100, 10, _assombrir(c, 0.9), rx=4),
              chemin("M -30 -206 l 10 6 l 10 -6 l 10 6 l 10 -6 l 10 6", stroke=OR_, sw=2)])


YASMINE = dict(peau="doree", cheveux="noir", coiffure="boucles", habit="#cc5de8", motif_robe=OR_, yeux="cils", nez="rond")
MAMAN = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chauve", habit="#1098ad", coiffe=hijab("#e64980"))
PAPA = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#f8f9fa", robe=True, barbe="#2b2b3a", coiffe=kufi())
FRERE = dict(stature="ado", peau="doree", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#343a40")
JEDDA = dict(stature="ancien", peau="doree", cheveux="gris", coiffure="chauve", habit="#7048e8", coiffe=hijab("#f8f9fa"), carrure="ronde")
JEDDI = dict(stature="ancien", peau="doree", cheveux="blanc", coiffure="chauve_cote", habit="#e9ecef", barbe="#e9ecef", coiffe=kufi("#fff3bf"))


def yasmine(x, y, s=1.2, **k):
    return personne(x, y, s, **{**YASMINE, **k})


def croissant(x, y, r=40, epais=0.18, angle=135, couleur="#fff3bf", S=None):
    """Mince croissant de lune ; sa partie éclairée regarde dans la direction `angle`
    (degrés, 0 = droite, 90 = bas), vers le Soleil couché."""
    cid = uid("c")
    a = math.radians(angle)
    ox, oy = -math.cos(a) * r * epais * 2, -math.sin(a) * r * epais * 2
    m = [el("mask", rect(-r * 2, -r * 2, r * 4, r * 4, "#000") + cercle(0, 0, r, "#fff") + cercle(ox, oy, r * 1.02, "#000"), id=cid),
         cercle(0, 0, r, couleur, mask=f"url(#{cid})")]
    if S is not None:
        S.lumiere(x, y, r * 1.5, "#e7f5ff", 0.2)
    return sans_relief(place(m, x, y))


def datte(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 22, 12, volume("#7c4a1e", 0.4, 0.7)), chemin("M -14 -2 Q 0 -8 14 -2", stroke="#a0693a", sw=2)], x, y, s, rot=rot)


def plat_dattes(x, y, s=1.0):
    m = [ellipse(0, 0, 90, 22, volume("#e9d8a6", 0.4, 0.75))]
    for k, (dx, dy) in enumerate(((-50, -8), (-20, -12), (10, -8), (40, -12), (-34, -22), (0, -26), (26, -22))):
        m.append(datte(dx, dy, 1.0, rot=(k % 3 - 1) * 15))
    return place(m, x, y, s)


def verre_eau(x, y, s=1.0):
    return place([rect(-18, -60, 36, 60, "#e7f5ff", rx=4, opacity=0.8, stroke="#a5d8ff", stroke_width=2), rect(-15, -44, 30, 42, "#a5d8ff", rx=3, opacity=0.8)], x, y, s)


def mosquee(x, y, s=1.0):
    """Mosquée : salle à coupole, minaret, portail en arc ; (x, y) = pied."""
    m = [rect(-220, -200, 440, 200, volume("#f8f9fa", 0.2, 0.85)),
         chemin("M -130 -200 Q -130 -330 0 -340 Q 130 -330 130 -200 Z", volume(VERT, 0.3, 0.8)),
         rect(-6, -380, 12, 44, OR_), place(croissant(0, 0, 16, 0.3, 0, OR_), 0, -392),
         rect(240, -440, 60, 440, volume("#f8f9fa", 0.2, 0.85)), rect(232, -330, 76, 16, "#ced4da"),
         chemin("M 240 -440 Q 270 -510 300 -440 Z", VERT), place(croissant(0, 0, 12, 0.3, 0, OR_), 270, -520),
         chemin("M -50 0 L -50 -110 Q 0 -170 50 -110 L 50 0 Z", "#1864ab"),
         chemin("M -60 0 L -60 -110 Q 0 -184 60 -110 L 60 0", stroke=OR_, sw=6)]
    for fx in (-170, 120):
        m.append(chemin(f"M {fx} -60 L {fx} -130 Q {fx + 25} -160 {fx + 50} -130 L {fx + 50} -60 Z", "#a5d8ff"))
    return place(m, x, y, s)


def salon(S, y=600, soir=False, nuit_=False):
    piece(S, "manoir", y)
    if nuit_:
        S.ambiance("nuit")
    couleur = "#ff922b" if soir else ("#1c2a52" if nuit_ else "#a5d8ff")
    S.add(fenetre(470, 100, 200, 170, couleur, rideaux=VERT, contenu=g([rect(0, 0, 800, 800, couleur)])))
    S.add(chemin("M 0 40 Q 200 80 400 40 T 800 40", stroke=OR_, sw=4))
    for k in range(7):
        S.add(etoile5(60 + k * 115, 60 + (k % 2) * 14, 10, OR_))


def ciel_ouest(S, horizon=560, apres=True):
    """Ciel de l'ouest juste après le coucher du soleil : lueur orange au ras de l'horizon."""
    ciel(S, "#1c2a52", "#ff922b")
    S.add(ellipse(560, horizon, 360, 120, radial([(0, "#ffd8a8", 0.9), (1, "#ff922b", 0)])))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel_ouest(S, 560)
    etoiles(S, 12, 3, (0, 0, 800, 250))
    S.add(croissant(380, 220, 50, 0.16, 62, S=S))
    S.add(rect(0, 560, 800, 240, "#343a40"))
    S.add(mosquee(160, 600, 0.6))
    S.add(yasmine(470, 790, 1.35, expr="rire", bras="designe", regard=(-0.5, -1)))
    S.add(personne(650, 790, 1.35, expr="content", bras="epaule", flip=True, regard=(-1, -0.6), **MAMAN))
    S.cachette(320, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(croissant(200, 130, 80, 0.22, 50))
    S.add(etoile5(310, 70, 14, OR_), etoile5(90, 200, 10, OR_))
    return S


def p01():
    """Plan moyen : pendant le ramadan, au soleil couchant, Yasmine met les dattes sur la table."""
    S = Scene()
    salon(S, soir=True)
    S.add(table(400, 790, 540, 150, "#c68642", nappe="#fff4e6"))
    S.add(plat_dattes(330, 622, 0.9), verre_eau(460, 628, 0.9), verre_eau(520, 628, 0.9))
    S.add(yasmine(160, 790, 1.25, expr="content", bras="donne", regard=(1, 0.3), objet=datte(96, -100, 1.2)))
    S.add(personne(660, 790, 1.35, expr="content", bras="mains_jointes", regard=(-1, 0), **FRERE))
    S.add(horloge(330, 200, 40, 7, 40))
    S.add(bulle(560, 330, 360, 100, "Le soleil se couche…\non va manger !", 30, pointe=(650, 470)))
    return S


def p02():
    """Gros plan : au coucher du soleil, Karim rompt le jeûne avec une datte et un verre d'eau."""
    S = Scene()
    salon(S, soir=True)
    S.add(table(400, 790, 600, 150, "#c68642", nappe="#fff4e6"))
    S.add(personne(420, 900, 1.9, expr="miam", bras="donne", regard=(0.4, 0.2), objet=datte(*ancre(96, -100, "donne", "ado"), 1.4), **FRERE))
    S.add(plat_dattes(250, 620, 1.0), verre_eau(580, 630, 1.1))
    S.camera(1.25, 420, 520)
    S.dessus(texte(400, 100, "D'abord une datte et de l'eau.", 40, "#e8590c", contour="#fff"))
    return S


def p03():
    """Plan large : le dernier soir, sur la colline, la famille guette le premier croissant de lune, à l'ouest."""
    S = Scene()
    ciel_ouest(S, 560)
    S.add(croissant(430, 300, 34, 0.12, 63, S=S))
    S.add(chemin("M 0 600 Q 400 540 800 600 L 800 800 L 0 800 Z", "#2b3a2f"))
    S.add(personne(140, 780, 1.1, expr="content", bras="epaule", regard=(1, -1), **PAPA))
    S.add(yasmine(260, 780, 1.0, expr="joie", bras="designe", regard=(1, -1)))
    S.add(personne(380, 780, 1.1, expr="bouche_bee", bras="mains_jointes", regard=(1, -1), **MAMAN))
    S.add(personne(520, 780, 1.1, expr="surpris", bras="joues", regard=(0.5, -1), **FRERE))
    S.add(bulle(260, 140, 360, 90, "Là ! La lune !", 38, pointe=(260, 490)))
    S.cachette(720, 700)
    return S


def p04():
    """Gros plan : le croissant, très fin, tourné vers le Soleil qui vient de se coucher."""
    S = Scene()
    ciel_ouest(S, 640)
    S.add(croissant(360, 320, 110, 0.14, 58, S=S))
    S.add(chemin("M 0 650 Q 400 620 800 650 L 800 800 L 0 800 Z", "#2b3a2f"))
    from sciences import fleche
    S.add(fleche(440, 400, 560, 560, "#fff3bf", sw=6, tete=20))
    S.add(texte(620, 600, "le Soleil vient", 26, "#fff3bf"), texte(620, 630, "de se coucher", 26, "#fff3bf"))
    S.add(texte(400, 120, "Le premier croissant de lune", 42, "#fff3bf", contour="#5f3dc4"))
    S.cachette(740, 720)
    return S


def mains_henne(x, y, s=1.0):
    """Une main ouverte décorée de henné ; (x, y) = poignet."""
    m = [ellipse(0, -50, 40, 46, "#dca36f")]
    for k, (dx, L) in enumerate(((-30, 50), (-12, 64), (6, 66), (24, 58))):
        m.append(rect(dx - 8, -100 - L * 0.6, 16, L, "#dca36f", rx=8))
    m.append(place(rect(-8, -30, 16, 46, "#dca36f", rx=8), 38, -40, rot=-40))
    m += [cercle(0, -54, 12, "none", stroke="#a0522d", stroke_width=3), cercle(0, -54, 4, "#a0522d")]
    for a in range(0, 360, 45):
        r_ = math.radians(a)
        m.append(cercle(math.cos(r_) * 22, -54 + math.sin(r_) * 22, 3, "#a0522d"))
    for dx in (-30, -12, 6, 24):
        m.append(trait(dx, -110, dx, -130, "#a0522d", 3))
    return place(m, x, y, s)


def p05():
    """Plan moyen : la veille, Jedda dessine du henné sur la main de Yasmine."""
    S = Scene()
    salon(S, nuit_=True)
    S.add(lampe(700, 610, 0.8))
    S.add(personne(230, 790, 1.4, expr="concentre", bras="tend", regard=(1, 0.4), **JEDDA))
    S.add(yasmine(500, 790, 1.3, expr="content", bras="tend", flip=True, regard=(-1, 0.3)))
    S.add(mains_henne(380, 600, 0.9))
    S.add(bulle(400, 160, 420, 90, "Des fleurs, pour la fête !", 32, pointe=(260, 430)))
    return S


def p06():
    """Plan moyen : le matin de l'Aïd, Yasmine tourne dans sa robe neuve."""
    S = Scene()
    salon(S)
    S.add(yasmine(400, 790, 1.5, expr="rire", bras="danse"))
    S.add(paillettes(560, 380, 1.1, OR_), paillettes(230, 330, 0.9, OR_))
    S.add(mouvement(250, 640, 1.0, "#cc5de8", rot=180), mouvement(560, 640, 1.0, "#cc5de8"))
    S.add(texte(400, 160, "C'est l'Aïd !", 64, "#cc5de8", contour="#fff"))
    return S


def sac_nourriture(x, y, s=1.0):
    return place([rect(-50, -100, 100, 100, volume("#e9d8a6", 0.35, 0.8), rx=8), rect(-40, -126, 24, 40, "#fa5252", rx=4),
                  rect(-6, -122, 30, 34, "#fcc419", rx=4), ellipse(30, -110, 14, 20, "#ffa94d"), rect(-48, -100, 96, 10, "#c68642")], x, y, s)


def p07():
    """Plan moyen : avant la prière, Papa et Yasmine apportent un sac de nourriture à la banque alimentaire."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(rect(0, 620, 800, 180, "#ced4da"))
    S.add(rect(400, 260, 380, 360, "#ffe8cc"), rect(400, 230, 380, 40, "#e8590c"))
    S.add(texte(590, 258, "BANQUE ALIMENTAIRE", 22, "#fff"))
    S.add(rect(540, 440, 100, 180, "#a0693a", rx=4))
    S.add(personne(640, 790, 1.3, stature="adulte", peau="claire", cheveux="roux", coiffure="queue", habit="#20c997", robe=False,
                   jambes="#495057", expr="content", bras="tend", flip=True, regard=(-1, 0)))
    S.add(personne(230, 790, 1.4, expr="content", bras="porte", regard=(1, 0), objet=sac_nourriture(*ancre(0, -60, "porte", "adulte"), 0.9), **PAPA))
    S.add(yasmine(400, 790, 1.15, expr="fier", bras="porte", regard=(1, 0), objet=sac_nourriture(0, -60, 0.6)))
    S.add(bulle(330, 140, 420, 100, "Pour que tout le monde\nfasse la fête !", 32, pointe=(380, 470)))
    return S


def p08():
    """Plan large : devant la mosquée, les gens en habits de fête se saluent : « Aïd moubarak ! »."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 600, 800, 200, "#e9ecef"))
    S.add(mosquee(380, 610, 0.9))
    S.add(personne(120, 790, 1.15, expr="rire", bras="ouverts", regard=(1, 0), **PAPA))
    S.add(personne(260, 790, 1.15, stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#fff3bf", robe=True,
                   barbe="#2b2b3a", coiffe=kufi("#2b8a3e"), expr="rire", bras="ouverts", flip=True, regard=(-1, 0)))
    S.add(yasmine(470, 790, 1.0, expr="rire", bras="coucou", regard=(1, 0)))
    S.add(personne(600, 790, 1.15, expr="content", bras="mains_jointes", regard=(-1, 0), **MAMAN))
    S.add(personne(720, 790, 1.05, stature="adulte", peau="claire", cheveux="noir", coiffure="chauve", habit="#f783ac", coiffe=hijab("#ffd43b"),
                   expr="rire", bras="salut", regard=(-1, 0)))
    S.add(bulle(300, 120, 360, 90, "Aïd moubarak !", 40, pointe=(200, 470)))
    S.cachette(730, 430, "air")
    return S


def corne_gazelle(x, y, s=1.0, rot=0):
    return place([chemin("M -30 6 Q 0 -30 30 6 Q 0 -14 -30 6 Z", volume("#fff4e6", 0.3, 0.85), stroke="#e9d8a6", sw=2)], x, y, s, rot=rot)


def baklava(x, y, s=1.0):
    return place([poly([(0, -20), (24, 0), (0, 20), (-24, 0)], volume("#e8a33d", 0.4, 0.75)), cercle(0, 0, 5, "#69db7c")], x, y, s)


def p09():
    """Gros plan : le plateau de douceurs : cornes de gazelle, baklavas et dattes."""
    S = Scene()
    salon(S)
    S.add(table(400, 790, 600, 150, "#c68642", nappe="#d3f9d8"))
    S.add(ellipse(400, 620, 220, 44, volume("#dee2e6", 0.5, 0.75)))
    for k in range(5):
        S.add(corne_gazelle(260 + k * 30, 610 - (k % 2) * 10, 1.0, rot=(k % 2) * 180))
    for k in range(5):
        S.add(baklava(440 + (k % 3) * 46, 606 + (k // 3) * 24, 1.0))
    S.add(plat_dattes(400, 640, 0.5))
    S.camera(1.35, 400, 560)
    S.dessus(texte(400, 110, "Des douceurs pour tout le monde !", 40, "#e8590c", contour="#fff"))
    return S


def enveloppe(x, y, s=1.0):
    return place([rect(-36, -24, 72, 48, "#fff", rx=4, stroke=VERT, stroke_width=3), chemin("M -36 -24 L 0 6 L 36 -24", stroke=VERT, sw=3),
                  place(croissant(0, 0, 8, 0.3, 0, OR_), 22, 12)], x, y, s)


def p10():
    """Plan large : chez Jedda et Jeddi, tout le monde s'embrasse ; Yasmine reçoit une petite enveloppe."""
    S = Scene()
    salon(S)
    S.add(personne(140, 790, 1.25, expr="rire", bras="calin", regard=(1, 0), **JEDDA))
    S.add(personne(270, 790, 1.25, expr="rire", bras="calin", flip=True, regard=(-1, 0), **MAMAN))
    S.add(personne(520, 790, 1.3, expr="content", bras="donne", flip=True, regard=(-1, 0.3), objet=enveloppe(*ancre(84, -92, "donne", "ancien"), 0.8), **JEDDI))
    S.add(yasmine(390, 790, 1.15, expr="rire", bras="tend", regard=(1, -0.2)))
    S.add(personne(680, 790, 1.3, expr="joie", bras="applaudit", regard=(-1, 0), **FRERE))
    S.add(texte(400, 170, "Aïd moubarak, Jeddi !", 46, VERT, contour="#fff"))
    S.cachette(70, 140, "air")
    return S


def p11():
    """Plan moyen : le lendemain soir, à la fenêtre, le croissant est un peu plus épais et plus haut."""
    S = Scene()
    piece(S, "chambre", 600)
    S.ambiance("soir")
    cid_ciel = g([rect(0, 0, 800, 800, lineaire([(0, "#1c2a52"), (1, "#ff922b")])), croissant(380, 170, 30, 0.22, 60),
                  etoile5(300, 140, 5, "#fff3bf"), etoile5(450, 120, 4, "#fff3bf")])
    S.add(fenetre(220, 90, 360, 280, "#1c2a52", cadre="#fff", rideaux="#cc5de8", contenu=cid_ciel))
    S.add(yasmine(400, 790, 1.45, expr="content", bras="designe", regard=(0, -0.8)))
    S.add(bulle(620, 470, 280, 100, "Elle a grandi\ndepuis hier !", 28, pointe=(480, 520)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("croissant-seul.svg", vignette),
    ("01-on-attend.svg", p01), ("02-la-datte.svg", p02), ("03-on-guette-la-lune.svg", p03),
    ("04-le-croissant.svg", p04), ("05-le-henne.svg", p05), ("06-la-robe-neuve.svg", p06),
    ("07-le-don.svg", p07), ("08-aid-moubarak.svg", p08), ("09-les-douceurs.svg", p09),
    ("10-chez-jedda-et-jeddi.svg", p10), ("11-elle-a-grandi.svg", p11),
]
