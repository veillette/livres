"""La chouette qui vole sans bruit — l'effraie des clochers.

L'effraie a un visage blanc en forme de cœur qui guide les sons vers ses
oreilles : elle entend un campagnol trotter sous l'herbe, même dans le noir.
Ses plumes douces, aux bords frangés, la font voler sans bruit. Ses yeux ne
bougent pas dans leurs orbites : elle tourne la tête, jusqu'aux trois quarts
d'un tour. Elle avale ses proies entières et recrache une pelote de poils et
d'os. Elle ne hulule pas, elle « chuinte ». Elle niche dans les clochers et
les granges et mange beaucoup de rongeurs des champs.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, fleche_courbe, ondes, enfant

ID = "chouette-effraie"
DORE = "#e3b26b"
DORE_F = "#c08a52"
GRIS = "#adb5bd"
VISAGE = "#ffffff"
COEUR = "M 0 -126 C -32 -124 -58 -150 -54 -190 C -50 -214 -22 -216 0 -196 C 22 -216 50 -214 54 -190 C 58 -150 32 -124 0 -126 Z"


# --- Personnages ------------------------------------------------------------

def _visage(expr, regard):
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin(COEUR, VISAGE, stroke=DORE_F, sw=6)]
    for sgn in (-1, 1):
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * 20, -174, ys, (0, 0), taille=1.0))
        else:
            k = 1.25 if ys == "grand" else 1.0
            m.append(ellipse(sgn * 20 + regard[0] * 3, -174 + regard[1] * 3, 8 * k, 10 * k, ENCRE))
            m.append(cercle(sgn * 20 + regard[0] * 3 + 2.5, -178 + regard[1] * 3, 2.6, "#fff"))
        m.append(joue(sgn * 32, -152, 0.8))
    m.append(chemin("M -4 -168 Q 0 -146 4 -168 Z", "#f3d9c4"))
    m.append(ellipse(0, -156, 5, 12, "#f3d9c4"))
    if bs in ("ouverte", "o", "crie", "baille"):
        m.append(ellipse(0, -138, 6, 6, "#c92a2a"))
    m.append(sourcils(20, -172, ss))
    return m


def effraie(x, y, s=1.0, flip=False, expr="sourire", regard=(0, 0), dos=False, ailes="bas", proie=False, bebe=False):
    """Effraie posée, vue de face ; (x, y) = sous les pattes. `dos` : vue de dos,
    la tête tournée vers nous ; ailes : "bas" ou "ouvertes" ; `bebe` : poussin
    couvert de duvet blanc."""
    DORE = "#f1f3f5" if bebe else globals()["DORE"]
    m = []
    if bebe:
        for k in range(12):
            a = math.radians(k * 30)
            m.append(cercle(math.cos(a) * 50, -96 + math.sin(a) * 76, 16, "#f8f9fa"))
    for sgn in (-1, 1):
        m.append(trait(sgn * 16, -40, sgn * 18, -6, "#f8f9fa", 10))
        for k in (-1, 0, 1):
            m.append(trait(sgn * 18, -6, sgn * 18 + k * 10, 2, "#868e96", 3.5))
    if ailes == "ouvertes":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 30} -130 Q {sgn * 120} -200 {sgn * 170} -150 Q {sgn * 150} -120 {sgn * 160} -96 "
                            f"Q {sgn * 120} -100 {sgn * 110} -70 Q {sgn * 70} -80 {sgn * 34} -60 Z", DORE))
            for k in range(3):
                m.append(trait(sgn * (60 + k * 30), -140 + k * 6, sgn * (70 + k * 30), -100 + k * 6, GRIS, 3))
    if dos:
        m.append(poly([(-20, -20), (20, -20), (0, 10)], DORE_F))
        m.append(ellipse(0, -92, 54, 82, DORE))
        for sgn in (-1, 1):
            m.append(chemin(f"M 0 -150 Q {sgn * 60} -140 {sgn * 50} -60 Q {sgn * 30} -14 0 -10 Z", eclaircir(DORE_F, 0.25)))
            m.append(chemin(f"M {sgn * 10} -130 Q {sgn * 44} -110 {sgn * 36} -40", stroke=GRIS, sw=3))
        for px, py in [(-24, -120), (20, -100), (-10, -70), (28, -60), (-34, -80), (8, -140)]:
            m.append(cercle(px, py, 3.5, GRIS))
    else:
        m.append(ellipse(0, -90, 50, 80, "#fff9f0"))
        for px, py in [(-14, -90), (16, -70), (-6, -50), (10, -110)]:
            m.append(cercle(px, py, 2.5, DORE_F))
        if ailes == "bas":
            for sgn in (-1, 1):
                m.append(ellipse(sgn * 48, -96, 22, 70, DORE, rot=sgn * -8))
                m.append(trait(sgn * 44, -120, sgn * 52, -60, GRIS, 3, opacity=0.8))
    if proie:
        m.append(place(souris_champs(0, 0, 1.0), -40, -10, 0.9))
    m.append(ellipse(0, -172, 60, 54, DORE))
    m += _visage(expr, regard)
    return place(m, x, y, s, flip=flip)


def effraie_vol(x, y, s=1.0, rot=0, expr="sourire", regard=(0, 1), serres=False):
    """Effraie en vol, ailes grandes ouvertes, vue de face ; (x, y) = centre."""
    m = []
    for sgn in (-1, 1):
        aile = (f"M {sgn * 20} -30 Q {sgn * 120} -110 {sgn * 250} -70 Q {sgn * 240} -50 {sgn * 250} -30 "
                f"Q {sgn * 210} -30 {sgn * 210} -10 Q {sgn * 170} -16 {sgn * 160} 10 Q {sgn * 110} 0 {sgn * 30} 20 Z")
        m.append(chemin(aile, DORE))
        m.append(chemin(f"M {sgn * 40} 6 Q {sgn * 120} -50 {sgn * 220} -48", stroke="#fff9f0", sw=16, opacity=0.6))
        for k in range(4):
            m.append(trait(sgn * (90 + k * 36), -62 + k * 2, sgn * (100 + k * 36), -30 + k * 4, GRIS, 3))
    m.append(ellipse(0, 20, 38, 56, "#fff9f0"))
    if serres:
        for sgn in (-1, 1):
            m.append(trait(sgn * 14, 60, sgn * 20, 96, "#f8f9fa", 9))
            for k in (-1, 0, 1):
                m.append(trait(sgn * 20, 96, sgn * 20 + k * 10, 108, "#868e96", 3.5))
    head = place(g([ellipse(0, -172, 60, 54, DORE)] + _visage(expr, regard)), 0, 130, 0.8)
    m.append(head)
    return place(m, x, y, s, rot=rot)


def pelote(x, y, s=1.0, rot=0):
    """Pelote de réjection : boule grise de poils, avec des petits os."""
    m = [ellipse(0, 0, 50, 30, "#868e96"), ellipse(-10, -6, 30, 16, "#adb5bd", opacity=0.6),
         chemin("M 20 -10 L 46 -24", stroke="#f8f9fa", sw=6), chemin("M -30 10 L -50 22", stroke="#f8f9fa", sw=5),
         cercle(48, -26, 5, "#f8f9fa"), cercle(-52, 24, 4, "#f8f9fa")]
    for k in range(8):
        m.append(chemin(f"M {-36 + k * 9} {-14 + (k % 3) * 8} q 4 -6 8 0", stroke="#495057", sw=2))
    return place(m, x, y, s, rot=rot)


def clocher(S, nuit_=False):
    """Intérieur d'un clocher : pierres, cloche, ouverture en arc."""
    S.add(rect(0, 0, 800, 800, "#c9b79c" if not nuit_ else "#5c5470"))
    r = random.Random(2)
    for j in range(10):
        for i in range(6):
            x = i * 150 + (75 if j % 2 else 0) - 40
            S.add(rect(x, j * 80, 144, 74, "#d8c7aa" if not nuit_ else "#6b6380", rx=8))
    ciel_c = "#a5d8ff" if not nuit_ else "#1c2a52"
    S.add(chemin("M 520 520 L 520 250 Q 520 150 620 150 Q 720 150 720 250 L 720 520 Z", ciel_c))
    if nuit_:
        S.add(lune(660, 240, 30))
    S.add(rect(0, 640, 800, 160, "#8d5524"))
    S.add(rect(0, 640, 800, 16, "#6d4424"))


def cloche(x, y, s=1.0):
    m = [rect(-12, -30, 24, 30, "#8d5524"), chemin("M -70 160 Q -70 40 -40 0 Q 0 -20 40 0 Q 70 40 70 160 Q 0 140 -70 160 Z", "#fab005"),
         ellipse(0, 158, 74, 14, "#e67700"), cercle(0, 170, 14, "#e67700")]
    return place(m, x, y, s)


def champ_nuit(S, y=560, lune_x=650):
    nuit(S, "#1c2a52", "#4c5b9a")
    etoiles(S, 30, 9, (0, 0, 800, y - 40))
    S.add(lune(lune_x, 120, 42))
    S.add(rect(0, y, 800, 800 - y, "#2b3a2f"))
    r = random.Random(4)
    for _ in range(40):
        x0 = r.uniform(0, 800)
        y0 = r.uniform(y + 10, 800)
        S.add(chemin(f"M {n(x0)} {n(y0)} l -6 -30 M {n(x0)} {n(y0)} l 0 -36 M {n(x0)} {n(y0)} l 6 -28", stroke="#3d5a40", sw=4))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    champ_nuit(S, 600, lune_x=630)
    S.add(effraie_vol(380, 420, 1.35, expr="content"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(effraie(200, 262, 1.05, expr="content"))
    return S


def p01():
    S = Scene()
    clocher(S)
    S.add(cloche(260, 120, 1.3))
    S.add(rect(460, 520, 300, 22, "#8d5524"))
    S.add(effraie(600, 520, 1.3, expr="dort"))
    S.add(zzz(720, 260, 1.0, "#5c7cfa"))
    return S


def p02():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(cercle(400, 380, 300, "#ffe8cc"))
    S.add(effraie(400, 770, 2.3, expr="sourire"))
    S.add(texte(160, 170, "Chhhh !", 54, "#c08a52", contour="#fff", rot=-8))
    S.add(etiquette(640, 150, "un visage", 34, "#e67700"), etiquette(640, 190, "en cœur", 34, "#e67700"))
    return S


def p03():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#364fc7", "#9775fa", "#ffc078"])))
    S.add(rect(0, 560, 800, 240, "#5c7a3a"))
    S.add(maison(170, 580, 1.1, mur="#c9b79c", toit="#7c4a1e"))
    S.add(place([rect(-50, -320, 100, 320, "#c9b79c"), poly([(-64, -320), (64, -320), (0, -430)], "#7c4a1e"),
                 chemin("M -20 -200 L -20 -250 Q 0 -280 20 -250 L 20 -200 Z", "#343a40")], 120, 600))
    S.add(effraie_vol(500, 300, 0.9, expr="content", regard=(1, 1)))
    return S


def p04():
    S = Scene()
    champ_nuit(S, 600)
    S.add(effraie_vol(320, 330, 1.1, expr="sourire"))
    plume = [chemin("M 640 700 Q 600 560 660 420 Q 720 560 640 700 Z", DORE),
             trait(640, 700, 660, 420, DORE_F, 4)]
    for k in range(10):
        plume.append(trait(612 + (k % 2) * 4, 640 - k * 22, 590 + (k % 2) * 4, 650 - k * 22, "#ffe8cc", 3))
    S.add(loupe(640, 560, 130, [rect(500, 420, 280, 280, "#fff4e6")] + plume, fond="#fff4e6", rot=135))
    S.add(texte(250, 650, "… chut …", 44, "#ffffff"))
    return S


def p05():
    S = Scene()
    champ_nuit(S, 520)
    S.add(effraie(250, 500, 1.5, expr="concentre", regard=(1, 1)))
    S.add(rect(140, 500, 220, 20, "#5c3a1e"))
    S.add(souris_champs(620, 700, 1.3))
    S.add(ondes(620, 680, 40, 4, 50, 200, 50, "#ffd43b", 5))
    S.add(texte(620, 610, "trotte, trotte…", 32, "#ffd43b"))
    return S


def p06():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(effraie(250, 760, 1.5, expr="sourire"))
    S.add(effraie(560, 760, 1.5, expr="malin", dos=True))
    S.add(fleche_courbe("M 470 330 A 110 50 0 1 0 650 320", (650, 320), 20, "#e67700", 6, 22))
    S.add(texte(400, 120, "Coucou, je suis là !", 44, "#e67700", contour="#fff"))
    return S


def p07():
    S = Scene()
    champ_nuit(S, 560)
    S.add(effraie_vol(420, 400, 1.0, expr="concentre", serres=True))
    S.add(souris_champs(430, 700, 1.3, flip=True))
    S.add(mouvement(430, 230, 1.2, "#ffffff", rot=-90))
    return S


def p08():
    S = Scene()
    clocher(S)
    S.add(rect(80, 470, 360, 22, "#8d5524"))
    S.add(effraie(250, 470, 1.25, expr="oups"))
    S.add(pelote(530, 690, 1.6))
    S.add(fleche(320, 360, 480, 640, "#495057", 5, 18))
    S.add(etiquette(560, 610, "une pelote", 34, "#495057"))
    return S


def p09():
    S = Scene()
    fond(S, "#f8f9fa")
    S.add(rect(0, 560, 800, 240, "#e8c39e"))
    S.add(rect(380, 600, 360, 160, "#ffffff", rx=10))
    os_ = [(430, 640, 30, 0), (500, 660, 40, 20), (580, 640, 34, -10), (660, 680, 26, 40), (460, 710, 44, 0), (620, 720, 36, -20)]
    for x, y, L, rot in os_:
        S.add(place([trait(-L / 2, 0, L / 2, 0, "#dee2e6", 7), cercle(-L / 2, 0, 5, "#dee2e6"), cercle(L / 2, 0, 5, "#dee2e6")], x, y, rot=rot))
    S.add(place([ellipse(0, 0, 22, 14, "#dee2e6"), ellipse(18, 4, 12, 6, "#dee2e6"), cercle(-4, -2, 4, "#868e96")], 690, 630))
    S.add(pelote(250, 650, 1.0))
    S.add(enfant(220, 760, 1.5, expr="concentre", bras="porte", regard=(1, 0.6), habit="#ffa94d", jambes="#495057",
                 coiffure="boucles", peau="brune", cheveux="noir"))
    S.add(loupe(560, 360, 90, [rect(470, 270, 180, 180, "#ffffff"),
                               place([ellipse(0, 0, 22, 14, "#dee2e6"), ellipse(18, 4, 12, 6, "#dee2e6"), cercle(-4, -2, 4, "#868e96")], 560, 360, 3.0)],
                rot=130))
    return S


def p10():
    S = Scene()
    clocher(S, nuit_=True)
    S.add(cloche(150, 100, 1.0))
    S.add(rect(240, 520, 520, 24, "#8d5524"))
    for k, x in enumerate([300, 400, 500]):
        S.add(effraie(x, 520, 0.7, expr="rire" if k == 1 else "content", ailes="bas", bebe=True))
    S.add(effraie(640, 520, 1.15, expr="content", proie=True))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chouette-seule.svg", vignette),
    ("01-le-clocher.svg", p01), ("02-le-visage-en-coeur.svg", p02), ("03-le-soir.svg", p03),
    ("04-sans-bruit.svg", p04), ("05-les-oreilles.svg", p05), ("06-la-tete-tourne.svg", p06),
    ("07-la-chasse.svg", p07), ("08-la-pelote.svg", p08), ("09-dans-la-pelote.svg", p09),
    ("10-les-petits.svg", p10),
]
