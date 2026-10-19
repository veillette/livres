"""Le pinceau magique — un conte de Chine (Ma Liang).

Ma Liang, un petit garçon pauvre, adore dessiner, mais il n'a pas de
pinceau : il dessine avec un bâton dans la terre. Une nuit, un vieil homme à
la barbe blanche lui offre un pinceau d'or. Tout ce que Ma Liang peint
devient vrai : un oiseau s'envole, un ruisseau arrose les champs secs. Il
peint pour les pauvres du village. L'empereur, très gourmand d'or, le fait
venir : « Peins-moi une montagne d'or ! » Ma Liang peint d'abord une mer,
puis, tout au loin, une île avec une montagne d'or. L'empereur monte dans un
bateau ; Ma Liang peint le vent, qui le pousse tout au bout de la mer. Là,
l'empereur garde son or, tout seul (personne n'est blessé), et Ma Liang
rentre peindre pour ceux qui en ont besoin.

Plans : 1 large (le village, le bâton) · 2 moyen (le vieil homme, la nuit)
· 3 gros plan (l'oiseau s'envole) · 4 large (le ruisseau) · 5 moyen
(l'empereur) · 6 gros plan (le pinceau refuse) · 7 large (la mer et l'île)
· 8 large (le vent) · 9 moyen (retour au village).
"""
from contes import *
from base import _assombrir

ID = "pinceau-magique"

MA_LIANG = dict(peau="doree", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#343a40", ceinture="#e03131")
VIEIL_HOMME = dict(stature="ancien", peau="doree", cheveux="blanc", coiffure="chauve_cote", habit="#f8f9fa", robe=True,
                   barbe="#f8f9fa", carrure="fine", nez="long")
PAYSANNE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chignon", habit="#2f9e44", robe=False, jambes="#495057", nez="rond")
PAYSAN = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#e8590c", robe=False, jambes="#343a40",
              carrure="ronde")
ENFANT2 = dict(peau="doree", cheveux="noir", coiffure="couettes", habit="#f783ac", robe=True)
ROUGE_LAQUE = "#c92a2a"
OR_ = "#fab005"


def chapeau_empereur(c="#212529"):
    """Coiffe d'empereur : une planchette plate et ses rangs de perles (coiffe)."""
    m = [rect(-40, -232, 80, 36, c, rx=8), rect(-70, -246, 140, 14, c, rx=4)]
    for sgn in (-1, 1):
        for k in range(3):
            m.append(trait(sgn * (46 + k * 10), -232, sgn * (46 + k * 10), -196, OR_, 2))
            m.append(cercle(sgn * (46 + k * 10), -194, 4, ROUGE_LAQUE))
    return g(m)


EMPEREUR = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chauve_cote", habit="#fcc419", robe=True, barbe="#343a40",
                carrure="ronde", nez="rond", ceinture=ROUGE_LAQUE, coiffe=chapeau_empereur())


def pinceau_or(x, y, s=1.0, rot=0, brille=True):
    """Le pinceau magique ; (x, y) = bout des poils."""
    m = [rect(-7, -150, 14, 120, cylindre(OR_, 0.25, 0.75), rx=6), rect(-9, -40, 18, 14, ROUGE_LAQUE, rx=3),
         chemin("M -10 -28 Q -12 -8 0 0 Q 12 -8 10 -28 Z", "#212529"), cercle(0, -152, 8, ROUGE_LAQUE)]
    if brille:
        m.append(etincelles(0, -90, 0.8, OR_, graine=3, nb=7, r=60))
    return place(m, x, y, s, rot=rot)


def rouleau(x, y, w, h, contenu=(), fond_="#fff9db"):
    """Un rouleau de papier déroulé, (x, y) = coin haut gauche ; contenu en coordonnées de la page."""
    return g([rect(x, y, w, h, fond_, stroke="#e9d8a6", stroke_width=3), rect(x - 10, y - 12, w + 20, 14, "#8d5524", rx=6),
              rect(x - 10, y + h - 2, w + 20, 14, "#8d5524", rx=6), *contenu])


def oiseau_peint(x, y, s=1.0, trace=False, flip=False):
    """L'oiseau de Ma Liang : rouge, longue queue ; trace : encore à l'encre sur le papier."""
    if trace:
        m = [chemin("M -60 0 Q -20 -40 30 -20 Q 60 -10 70 -30 M -10 -20 Q 0 -70 30 -60 M -60 0 L -110 20 M -60 0 L -110 0",
                    stroke="#212529", sw=4)]
        return place(m, x, y, s, flip=flip)
    m = [chemin("M -50 0 Q -100 30 -140 20 Q -100 10 -60 -6 Z", "#e8590c"), ellipse(0, 0, 60, 34, volume("#e03131", 0.3, 0.8)),
         chemin("M -10 -10 Q 10 -90 60 -80 Q 30 -40 30 -6 Z", volume("#ff8787", 0.3, 0.8)), cercle(50, -16, 24, volume("#e03131", 0.3, 0.8)),
         cercle(58, -22, 5, ENCRE), poly([(72, -16), (94, -10), (72, -6)], OR_)]
    return place(m, x, y, s, flip=flip)


def maison_chinoise(x, y, s=1.0, mur="#f8f9fa", toit="#495057", porte_c=ROUGE_LAQUE, lumiere=False):
    """Petite maison au toit courbe, aux bouts relevés ; (x, y) = milieu du seuil."""
    vitre = "#ffe066" if lumiere else "#a5d8ff"
    m = [rect(-130, -170, 260, 170, mur), rect(-130, -14, 260, 14, "#ced4da"),
         rect(-40, -120, 80, 120, porte_c, rx=4), cercle(-10, -60, 4, OR_), cercle(10, -60, 4, OR_),
         rect(-110, -130, 50, 50, vitre, stroke="#8d5524", stroke_width=5), rect(60, -130, 50, 50, vitre, stroke="#8d5524", stroke_width=5),
         trait(-85, -130, -85, -80, "#8d5524", 3), trait(85, -130, 85, -80, "#8d5524", 3),
         chemin("M -190 -150 Q -170 -170 -150 -166 L -120 -230 L 120 -230 L 150 -166 Q 170 -170 190 -150 Q 150 -180 0 -174 Q -150 -180 -190 -150 Z",
                volume(toit, 0.3, 0.8)),
         rect(-120, -246, 240, 20, _assombrir(toit, 0.8), rx=6),
         poly([(-130, -246), (-150, -262), (-110, -246)], _assombrir(toit, 0.8)), poly([(130, -246), (150, -262), (110, -246)], _assombrir(toit, 0.8))]
    for k in range(9):
        m.append(trait(-110 + k * 27, -228, -128 + k * 32, -172, _assombrir(toit, 0.7), 3, opacity=0.6))
    return place(m, x, y, s)


def lampion(x, y, s=1.0, S=None):
    """Lanterne de papier rouge suspendue ; (x, y) = point d'accroche."""
    if S is not None:
        S.lumiere(x, y + 60 * s, 70 * s, "#ffa94d", 0.5)
    m = [trait(0, 0, 0, 20, ENCRE, 2), ellipse(0, 60, 34, 40, volume("#e03131", 0.3, 0.8)), rect(-18, 18, 36, 8, OR_), rect(-18, 96, 36, 8, OR_),
         trait(0, 104, 0, 128, OR_, 3)]
    for k in (-20, 0, 20):
        m.append(chemin(f"M {k * 0.5} 22 Q {k * 1.6} 60 {k * 0.5} 98", stroke="#a61e4d", sw=2, opacity=0.6))
    return place(m, x, y, s)


def montagnes_karst(S, y=520, couleurs=("#c5d8d0", "#a3c4b5", "#7fae9a"), graine=1):
    """Les pitons arrondis des montagnes de Chine, sur trois plans fondus dans la brume."""
    r = random.Random(graine)
    for k, c in enumerate(couleurs):
        base_y = y + k * 30
        x = -40 + r.uniform(0, 60)
        while x < 840:
            w = r.uniform(70, 130)
            h = r.uniform(160, 300) - k * 50
            S.add(chemin(f"M {n(x - w)} {n(base_y)} Q {n(x - w * 0.7)} {n(base_y - h)} {n(x)} {n(base_y - h)} "
                         f"Q {n(x + w * 0.7)} {n(base_y - h)} {n(x + w)} {n(base_y)} Z", c))
            x += w * r.uniform(1.0, 1.6)
        S.add(rect(0, base_y - 40, 800, 50, "#ffffff", opacity=0.25))


def rizieres(S, y=600, couleur="#8ce99a", seches=False):
    """Champs en terrasses jusqu'en bas de l'image."""
    c = "#e9c46a" if seches else couleur
    for k in range(5):
        yy = y + k * 44
        S.add(chemin(f"M 0 {yy} Q 400 {yy - 20} 800 {yy} L 800 800 L 0 800 Z", terrain(_assombrir(c, 1 - k * 0.04))))
        S.add(chemin(f"M 0 {yy} Q 400 {yy - 20} 800 {yy}", stroke=_assombrir(c, 0.75), sw=3))
        if seches:
            for j in range(6):
                S.add(chemin(f"M {60 + j * 130} {yy + 20} l 18 10 l -8 12 l 20 6", stroke="#bc8a3c", sw=2))
        else:
            for j in range(16):
                S.add(trait(20 + j * 50, yy + 14, 24 + j * 50, yy + 2, "#2f9e44", 3))


def paysage_chine(S, horizon=520, seches=False, soir=False):
    if soir:
        ciel(S, "#ff922b", "#ffe8cc")
    else:
        ciel(S, "#a5d8ff", "#f1f8f5")
    montagnes_karst(S, horizon)
    rizieres(S, horizon + 80, seches=seches)


def palais(S):
    """Salle du palais : colonnes laquées, tentures d'or, dallage."""
    piece(S, "chateau", 600)
    for x in (90, 710):
        S.add(rect(x - 30, 0, 60, 600, cylindre(ROUGE_LAQUE, 0.25, 0.75)), rect(x - 40, 560, 80, 40, OR_))
    S.add(rect(0, 0, 800, 50, "#862e9c"), rect(0, 50, 800, 10, OR_))
    for k in range(8):
        S.add(chemin(f"M {k * 100} 60 Q {k * 100 + 50} 110 {k * 100 + 100} 60", "#862e9c"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    paysage_chine(S, 560)
    S.add(maison_chinoise(140, 700, 0.7), maison_chinoise(680, 690, 0.55, toit="#1864ab"))
    S.add(rouleau(470, 380, 200, 260, [oiseau_peint(570, 540, 0.6, trace=True)]))
    S.add(oiseau_peint(560, 260, 1.0))
    S.add(personne(330, 780, 1.6, expr="rire", bras="tient", objet=pinceau_or(68, -146, 0.9, rot=30), regard=(1, -0.5), **MA_LIANG))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pinceau_or(200, 240, 1.4, rot=35))
    return S


def p01():
    """Plan large : un village au pied des montagnes ; Ma Liang dessine un poisson dans la terre avec un bâton."""
    S = Scene()
    paysage_chine(S, 500)
    S.add(maison_chinoise(150, 640, 0.75), maison_chinoise(640, 630, 0.6, toit="#1864ab"))
    S.add(chemin("M 0 760 Q 400 690 800 740 L 800 800 L 0 800 Z", terrain("#d9b48f")))
    S.add(chemin("M 470 760 q 40 -30 80 0 q -40 30 -80 0 Z M 470 760 l -24 -16 l 0 32 Z", stroke="#7c4a1e", sw=4))
    S.add(personne(330, 770, 1.35, expr="concentre", bras="ramasse", objet=baton(36, -18, 120, 10, "#8d5524", 8), regard=(1, 0.5), **MA_LIANG))
    S.add(personne(640, 770, 1.0, expr="sourire", bras="dos", flip=True, regard=(-1, 0.3), **ENFANT2))
    S.cachette(40, 790)
    return S


def p02():
    """Plan moyen : la nuit, dans la petite maison, un vieil homme à la barbe blanche tend un pinceau d'or à Ma Liang, émerveillé."""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.ambiance("nuit")
    S.add(fenetre(400, 200, 180, 160, dehors="#1c2a52", nuit_=True))
    S.add(lune(450, 170, 22, halo=False))
    S.lumiere(400, 200, 160, "#a5d8ff", 0.25)
    S.add(lampion(110, 60, 1.0, S=S))
    S.add(personne(560, 790, 1.4, expr="sourire", bras="tend", flip=True, regard=(-1, 0),
                   objet=pinceau_or(*ancre(96, -84, "tend", "ancien", "fine"), 0.8, rot=-80), **VIEIL_HOMME))
    hx, hy = mains_personne(560, 790, 1.4, "tend", flip=True, stature="ancien", carrure="fine")[0]
    S.lumiere(hx, hy, 120, "#ffe066", 0.6)
    S.add(personne(250, 790, 1.4, expr="bouche_bee", bras="surprise", regard=(1, -0.3), **MA_LIANG))
    return S


def p03():
    """Gros plan : Ma Liang peint un oiseau sur un rouleau ; l'oiseau sort du papier et s'envole !"""
    S = Scene()
    piece(S, "chaumiere", 620)
    S.add(rouleau(330, 160, 300, 380, [chemin("M 400 470 Q 480 440 560 470", stroke="#adb5bd", sw=3)]))
    S.add(personne(230, 800, 1.6, expr="rire", bras="lance", objet=pinceau_or(80, -202, 1.0, rot=50), regard=(1, -0.8), **MA_LIANG))
    S.add(oiseau_peint(520, 330, 1.1), mouvement(410, 360, 1.0, rot=-20))
    S.add(etincelles(460, 350, 1.2, OR_, graine=5))
    S.camera(1.25, 420, 420)
    S.dessus(texte(400, 70, "Il s'envole !", 50, "#e03131", contour="#fff"))
    return S


def p04():
    """Plan large : les champs sont secs ; Ma Liang peint un ruisseau qui coule pour de vrai ; une paysanne et un paysan se réjouissent."""
    S = Scene()
    paysage_chine(S, 460)
    S.add(chemin("M 300 540 Q 360 620 300 680 Q 250 740 330 800 L 470 800 Q 400 740 440 680 Q 500 610 420 540 Z", "#4dabf7"))
    S.add(chemin("M 330 560 Q 380 620 340 680", stroke="#d0ebff", sw=6, opacity=0.8), chemin("M 360 720 Q 380 760 390 800", stroke="#d0ebff", sw=6))
    S.add(personne(160, 780, 1.25, expr="concentre", bras="ramasse", objet=pinceau_or(36, -18, 0.8, rot=-30), regard=(1, 0.5), **MA_LIANG))
    S.add(personne(590, 790, 1.15, expr="rire", bras="saute", flip=True, regard=(-1, 0), **PAYSANNE))
    S.add(personne(720, 790, 1.15, expr="joie", bras="applaudit", flip=True, regard=(-1, 0), **PAYSAN))
    S.cachette(740, 470, "air")
    return S


def p05():
    """Plan moyen : dans son palais, l'empereur, gros et gourmand, pointe le doigt : « Peins-moi une montagne d'or ! » ; Ma Liang croise les bras."""
    S = Scene()
    palais(S)
    S.add(rect(460, 380, 260, 240, volume(OR_, 0.3, 0.8), rx=30))
    S.add(personne(590, 760, 1.5, expr="furieux", bras="designe", flip=True, regard=(-1, 0), **EMPEREUR))
    S.add(personne(220, 790, 1.35, expr="fache", bras="croises", regard=(1, -0.3), **MA_LIANG))
    S.add(bulle(500, 140, 470, 90, "Peins-moi une montagne d'or !", 32, pointe=(560, 290)))
    return S


def p06():
    """Gros plan : Ma Liang, le pinceau levé, sourit d'un air malin : il commence par peindre… une mer, toute bleue."""
    S = Scene()
    palais(S)
    S.add(rouleau(380, 180, 360, 320, [rect(380, 360, 360, 140, "#4dabf7"),
                                         chemin("M 390 380 q 20 -14 40 0 t 40 0 t 40 0 t 40 0 t 40 0 t 40 0 t 40 0 t 40 0", stroke="#d0ebff", sw=4)]))
    S.add(personne(260, 800, 1.6, expr="malin", bras="tient", objet=pinceau_or(68, -146, 1.0, rot=20), regard=(1, -0.3), **MA_LIANG))
    S.camera(1.6, 380, 420)
    S.dessus(bulle(560, 110, 400, 80, "D'abord… une mer.", 32))
    return S


def p07():
    """Plan large : la mer peinte est devenue vraie ; tout au loin, une île porte une montagne d'or ; l'empereur monte dans un bateau rouge."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 420, 800, 380, lineaire([(0, "#4dabf7"), (1, "#1864ab")])))
    for k in range(7):
        S.add(chemin(f"M {k * 120} {470 + k * 40} q 30 -14 60 0 t 60 0", stroke="#d0ebff", sw=4, opacity=0.7))
    S.add(chemin("M 560 430 Q 620 300 680 430 Z", volume(OR_, 0.2, 0.8)), ellipse(620, 432, 110, 14, "#e9c46a"))
    S.add(etincelles(620, 360, 0.8, "#fff3bf", graine=2))
    S.add(trait(330, 650, 330, 400, "#8d5524", 8), chemin("M 336 410 Q 440 480 336 600 Z", "#fff3bf"))
    S.add(personne(230, 700, 0.9, expr="miam", bras="designe", regard=(1, -0.5), **EMPEREUR))
    S.add(chemin("M 120 650 L 460 650 L 420 720 L 160 720 Z", volume(ROUGE_LAQUE, 0.3, 0.8)))
    S.add(chemin("M 0 760 Q 120 730 240 760 L 240 800 L 0 800 Z", terrain("#e9c46a")))
    S.add(personne(120, 790, 0.9, expr="malin", bras="tient", objet=pinceau_or(68, -146, 0.8, rot=20), **MA_LIANG))
    S.cachette(560, 220, "air")
    return S


def p08():
    """Plan large : Ma Liang peint du vent ; les vagues grossissent et poussent le bateau de l'empereur très loin, vers l'île d'or."""
    S = Scene()
    ciel(S, "#868e96", "#dee2e6")
    S.add(rect(0, 440, 800, 360, lineaire([(0, "#339af0"), (1, "#1864ab")])))
    for k in range(6):
        y0 = 480 + k * 55
        S.add(chemin(f"M -20 {y0} q 40 -40 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0", "none",
                     stroke="#e7f5ff", sw=5, opacity=0.8))
    S.add(chemin("M 690 450 Q 730 380 770 450 Z", volume(OR_, 0.2, 0.8)))
    S.add(place([chemin("M -100 0 L 100 0 L 80 40 L -80 40 Z", volume(ROUGE_LAQUE, 0.3, 0.8)), trait(0, 0, 0, -160, "#8d5524", 6),
                 chemin("M 6 -150 Q 90 -100 6 -20 Z", "#fff3bf"), personne(-40, 10, 0.55, expr="oups", bras="gratte", **EMPEREUR)], 560, 520, 1.0, rot=-8))
    for k in range(4):
        S.add(chemin(f"M {80 + k * 30} {200 + k * 50} q 120 -30 240 0 q 40 10 30 -20", stroke="#f8f9fa", sw=6, opacity=0.9))
    S.add(chemin("M 0 740 Q 150 700 300 740 L 300 800 L 0 800 Z", terrain("#e9c46a")))
    S.add(personne(140, 780, 1.05, expr="concentre", bras="lance", objet=pinceau_or(80, -202, 0.8, rot=50), regard=(1, -0.5), **MA_LIANG))
    S.add(texte(560, 120, "Fffouuuu !", 52, "#f8f9fa", contour="#495057"))
    S.cachette(40, 790)
    return S


def p09():
    """Plan moyen : au soir, de retour au village, Ma Liang peint une charrue et un buffle pour les villageois ; les enfants l'entourent."""
    S = Scene()
    paysage_chine(S, 520, soir=True)
    S.add(maison_chinoise(160, 650, 0.75, lumiere=True), maison_chinoise(660, 640, 0.6, toit="#1864ab", lumiere=True))
    S.lumiere(160 - 64, 650 - 79, 60, "#ffe066", 0.5)
    S.lumiere(160 + 64, 650 - 79, 60, "#ffe066", 0.5)
    S.add(lampion(300, 390, 0.8, S=S), lampion(520, 380, 0.8, S=S), chemin("M 260 390 Q 410 420 560 380", stroke=ENCRE, sw=2))
    S.add(rouleau(420, 470, 200, 200, [oiseau_peint(520, 590, 0.55, trace=True)]))
    S.add(personne(330, 790, 1.3, expr="content", bras="tient", objet=pinceau_or(68, -146, 0.8, rot=30), regard=(1, -0.2), **MA_LIANG))
    S.add(personne(620, 790, 1.0, expr="rire", bras="applaudit", flip=True, regard=(-1, -0.2), **ENFANT2))
    S.add(personne(720, 790, 0.95, stature="petit", peau="doree", cheveux="noir", coiffure="courts", habit="#fab005", robe=False,
                   jambes="#495057", expr="bouche_bee", flip=True, regard=(-1, 0)))
    S.add(personne(140, 790, 1.15, expr="content", bras="mains_jointes", regard=(1, 0), **PAYSANNE))
    S.cachette(70, 380, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pinceau-seul.svg", vignette),
    ("01-le-baton.svg", p01), ("02-le-vieil-homme.svg", p02), ("03-l-oiseau.svg", p03),
    ("04-le-ruisseau.svg", p04), ("05-l-empereur.svg", p05), ("06-une-mer.svg", p06),
    ("07-l-ile-d-or.svg", p07), ("08-le-vent.svg", p08), ("09-retour-au-village.svg", p09),
]
