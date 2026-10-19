"""Le hibou et le corbeau — d'après un conte inuit.

Il y a très longtemps, le Hibou (le harfang des neiges) et le Corbeau
étaient tout blancs. Un soir d'hiver, près de la lampe à huile de phoque,
le qulliq, ils décident de se faire de beaux habits. Le Corbeau peint le
Hibou avec la suie de la lampe, point par point, patiemment : le Hibou
reçoit ses belles taches noires. Puis c'est au Hibou de peindre le
Corbeau… mais le Corbeau ne tient pas en place : « C'est fini ? C'est
fini ? » Il gigote tant que la lampe se renverse sur lui : le voilà tout
noir ! « Gaq ! Gaq ! » Depuis, le harfang est blanc tacheté de noir, et le
corbeau est noir de la tête aux pattes. Une grand-mère raconte l'histoire
dans l'iglou.

Plans : 1 large (la banquise, deux oiseaux blancs) · 2 moyen (l'idée,
près du qulliq) · 3 gros plan (point par point) · 4 moyen (le reflet) · 5
moyen (« C'est fini ? ») · 6 gros plan (il gigote) · 7 large (la lampe se
renverse) · 8 moyen (« Gaq ! ») · 9 moyen (dans l'iglou, la grand-mère
raconte).
"""
from contes import *
from animaux import banquise
from base import _assombrir

ID = "hibou-corbeau"

GRAND_MERE = dict(stature="ancien", peau="doree", cheveux="noir", coiffure="tresses", habit="#c5a07a", robe=True, nez="rond",
                  carrure="ronde", ceinture="#e03131")
ENFANTS = [dict(peau="doree", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#8d5524", yeux="petits"),
           dict(peau="doree", cheveux="noir", coiffure="couettes", habit="#e03131", robe=False, jambes="#8d5524")]
SUIE = "#212529"


def harfang(x, y, s=1.0, taches=1.0, expr="sourire", ailes="bas", regard=(0, 0), flip=False):
    """Le hibou, un harfang des neiges : blanc, tacheté de noir selon `taches` (0 à 1)."""
    m = [chouette(0, 0, 1.0, "#f1f3f5", "#ffffff", expr=expr, ailes=ailes, regard=regard)]
    r = random.Random(11)
    points = []
    while len(points) < 40:
        px, py = r.uniform(-52, 52), r.uniform(-150, -14)
        if math.hypot(px / 54, (py + 80) / 74) > 0.9 or math.hypot(px / 52, (py + 120) / 32) < 1.15:   # dans le corps, hors du visage
            continue
        points.append((px, py, r.uniform(2.4, 4.4), r.uniform(-30, 30)))
    for px, py, rr, rot in points[:int(len(points) * taches)]:
        m.append(ellipse(px, py, rr * 1.5, rr, SUIE, rot=rot))
    return place(m, x, y, s, flip=flip) + occuper(x - 75 * s, y - 210 * s, x + 75 * s, y)


def corbeau_b(x, y, s=1.0, noir=0.0, expr="sourire", ailes="bas", flip=False, rot=0, regard=(0, 0), coulures=False):
    """Le corbeau : blanc (noir=0), à moitié peint, ou tout noir (noir=1)."""
    if noir >= 1:
        m = [corbeau(0, 0, 1.0, expr=expr, ailes=ailes, regard=regard)]
    else:
        m = [oiseau(0, 0, 1.0, "#f1f3f5", "#ffffff", expr=expr, ailes=ailes, regard=regard), poly([(-13, -74), (13, -74), (0, -44)], "#495057")]
        if noir > 0:
            m.append(chemin("M -44 -60 Q -30 -30 -10 -30 Q -30 -60 -40 -90 Z", SUIE, opacity=0.9))
            m.append(chemin("M -30 -40 l -4 18 M -20 -32 l -2 12", stroke=SUIE, sw=4))
    if coulures:
        for k in range(5):
            m.append(goutte(-40 + k * 20, 10 + (k % 2) * 16, 0.4, "#343a40"))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 75 * s, y - 180 * s, x + 75 * s, y)


def qulliq(x, y, s=1.0, allumee=True, renverse=False, S=None):
    """La lampe à huile des Inuit : une pierre en demi-lune, une rangée de petites flammes ; (x, y) = dessous."""
    if allumee and S is not None:
        S.lumiere(x, y - 30 * s, 170 * s, "#ffa94d", 0.6)
    m = [chemin("M -90 -30 Q 0 20 90 -30 Z", volume("#868e96", 0.3, 0.75)), ellipse(0, -30, 90, 10, "#5c3d24")]
    if allumee:
        for k in range(7):
            xx = -60 + k * 20
            m.append(chemin(f"M {xx - 6} -34 Q {xx} -60 {xx} -66 Q {xx + 4} -52 {xx + 6} -34 Z", "#ffa94d"))
            m.append(chemin(f"M {xx - 3} -34 Q {xx} -48 {xx} -52 Q {xx + 2} -44 {xx + 3} -34 Z", "#ffe066"))
    if renverse:
        m = [g(m, "rotate(-70 0 -10)"), chemin("M 20 -10 Q 120 30 200 0 Q 220 20 140 30 Q 40 30 20 -10 Z", "#5c3d24", opacity=0.9)]
    return place(m, x, y, s)


def iglou(x, y, s=1.0, lumiere=False, S=None):
    """Iglou de blocs de neige, son tunnel d'entrée ; (x, y) = milieu de la base."""
    m = [chemin("M -180 0 Q -180 -190 0 -190 Q 180 -190 180 0 Z", volume("#f8f9fa", 0.3, 0.85))]
    for k in range(1, 5):
        yy = -k * 38
        w = 180 * math.sqrt(max(0, 1 - (yy / 190) ** 2))
        m.append(chemin(f"M {n(-w)} {yy} Q 0 {yy - 10} {n(w)} {yy}", stroke="#c5d6e8", sw=3))
        for j in range(-3, 4):
            m.append(trait(j * w / 3.6 + (k % 2) * 18, yy, j * w / 3.6 + (k % 2) * 18, yy + 38, "#c5d6e8", 2))
    m += [chemin("M 60 0 L 60 -80 Q 130 -100 200 -70 L 200 0 Z", volume("#f1f3f5", 0.3, 0.8)),
          chemin("M 170 0 L 170 -50 Q 185 -66 200 -50 L 200 0 Z", "#ffd43b" if lumiere else "#495057")]
    if lumiere and S is not None:
        S.lumiere(x + 185 * s, y - 30 * s, 90 * s, "#ffd43b", 0.6)
    return place(m, x, y, s)


def aurore(S, y=60, graine=2):
    """Aurore boréale : de grands rubans verts et violets."""
    r = random.Random(graine)
    for k, c in enumerate(("#63e6be", "#96f2d7", "#b197fc")):
        y0 = y + k * 50
        pts = " ".join(f"T {80 + j * 120} {n(y0 + r.uniform(-40, 40))}" for j in range(7))
        S.add(chemin(f"M -20 {y0} Q 20 {y0 - 30} 40 {y0} {pts} L 820 {y0 + 140} L -20 {y0 + 140} Z",
                     lineaire([(0, c, 0.55), (1, c, 0)]), opacity=0.75))


def nuit_arctique(S, horizon=520, aurore_=True, graine=1):
    banquise(S, horizon, nuit_=True, graine=graine)
    if aurore_:
        aurore(S, 70, graine)
    S.proposer_cachette(60, 780)


def dedans_iglou(S):
    """L'intérieur de l'iglou : voûte de neige, banc couvert de peaux, lampe allumée."""
    S.add(rect(0, 0, 800, 800, "#dbe4ff"))
    for k in range(9):
        S.add(chemin(f"M -40 {k * 90} Q 400 {k * 90 - 80} 840 {k * 90}", stroke="#bac8ff", sw=3))
    S.add(rect(0, 600, 800, 200, terrain("#c5a07a")), rect(0, 600, 800, 30, "#a07c58"))
    for k in range(6):
        S.add(ellipse(80 + k * 130, 660, 70, 22, "#e9d8c4", opacity=0.6))
    S.ambiance("interieur")
    S.proposer_cachette(60, 790)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit_arctique(S, 560)
    S.add(harfang(270, 760, 1.7, taches=1.0, expr="fier", regard=(1, 0)))
    S.add(corbeau_b(540, 760, 1.6, noir=1, expr="oups", ailes="ouvertes", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(harfang(200, 262, 1.15, taches=1.0, expr="content"))
    return S


def p01():
    """Plan large : autrefois, sur la banquise, le hibou et le corbeau étaient tout blancs, sans une seule tache."""
    S = Scene()
    banquise(S, 520)
    S.add(iglou(640, 600, 0.8))
    S.add(harfang(250, 760, 1.2, taches=0, expr="sourire", regard=(1, 0)))
    S.add(corbeau_b(430, 760, 1.15, noir=0, expr="sourire", regard=(-1, 0), flip=True))
    S.add(texte(400, 150, "Tout blancs !", 54, "#1864ab", contour="#fff"))
    S.cachette(60, 790)
    return S


def p02():
    """Plan moyen : le soir, près de l'iglou, à la lumière de la lampe à huile, le corbeau a une idée : « Si on se faisait de beaux habits ? »"""
    S = Scene()
    nuit_arctique(S, 520, aurore_=True)
    S.add(iglou(620, 620, 0.9, lumiere=True, S=S))
    S.add(qulliq(400, 740, 1.0, S=S))
    S.add(corbeau_b(260, 760, 1.3, expr="joie", ailes="haut", regard=(1, 0)))
    S.add(harfang(540, 760, 1.25, taches=0, expr="content", regard=(-1, 0), flip=True))
    S.add(bulle(330, 230, 480, 90, "Si on se faisait de beaux habits ?", 30, pointe=(270, 560)))
    return S


def p03():
    """Gros plan : avec une plume trempée dans la suie de la lampe, le corbeau peint le hibou, point par point, très patiemment."""
    S = Scene()
    nuit_arctique(S, 520, aurore_=False)
    S.add(qulliq(160, 780, 0.9, S=S))
    S.add(harfang(440, 770, 1.6, taches=0.6, expr="dort", regard=(0, 0)))
    S.add(corbeau_b(220, 650, 1.0, expr="concentre", ailes="haut", regard=(1, 0)))
    S.add(place([trait(0, 0, 70, -30, "#495057", 4), ellipse(72, -30, 7, 5, SUIE)], 260, 600))
    S.camera(1.5, 380, 560)
    S.cachette(620, 795)
    S.dessus(texte(560, 110, "Un point… et encore un point…", 34, "#fff3bf", contour="#16213e"))
    return S


def p04():
    """Plan moyen : le hibou se regarde dans l'eau, entre deux plaques de glace : ses belles taches noires lui plaisent beaucoup."""
    S = Scene()
    banquise(S, 470)
    S.add(chemin("M 240 650 Q 420 632 600 650 Q 620 712 460 732 Q 280 732 240 650 Z", "#1c7ed6"))
    S.add(g([harfang(420, 0, 1.3, taches=1.0, expr="fier", ailes="ouvertes")], "translate(0 650) scale(1 -0.35)", opacity=0.45))
    S.add(harfang(420, 646, 1.3, taches=1.0, expr="fier", ailes="ouvertes", regard=(0, 1)))
    S.add(corbeau_b(660, 760, 1.1, expr="content", flip=True, regard=(-1, -0.4)))
    S.add(bulle(260, 170, 360, 90, "Magnifique !", 38, pointe=(380, 420)))
    S.cachette(110, 780)
    return S


def p05():
    """Plan moyen : à son tour, le hibou peint le corbeau ; mais le corbeau tourne la tête : « C'est fini ? C'est fini ? »"""
    S = Scene()
    nuit_arctique(S, 520)
    S.add(qulliq(620, 780, 0.9, S=S))
    S.add(corbeau_b(300, 770, 1.4, noir=0.4, expr="oups", ailes="haut", regard=(1, -0.3)))
    S.add(harfang(520, 770, 1.3, taches=1.0, expr="concentre", flip=True, regard=(-1, 0)))
    S.add(bulle(320, 200, 400, 90, "C'est fini ? C'est fini ?", 32, pointe=(300, 560)))
    return S


def p06():
    """Gros plan : le corbeau sautille, gigote, bat des ailes ; la lampe vacille ; le hibou lève les ailes : « Ne bouge pas ! »"""
    S = Scene()
    nuit_arctique(S, 520, aurore_=False)
    S.add(qulliq(560, 790, 1.0, S=S))
    S.add(corbeau_b(380, 700, 1.6, noir=0.4, expr="rire", ailes="ouvertes", rot=-12, regard=(0, -1)))
    S.add(mouvement(240, 560, 1.2), mouvement(520, 540, 1.2, rot=180))
    S.add(harfang(640, 780, 1.2, taches=1.0, expr="inquiet", ailes="haut", flip=True, regard=(-1, 0)))
    S.camera(1.35, 450, 560)
    S.cachette(200, 795)
    S.dessus(bulle(420, 110, 380, 86, "Ne bouge pas !", 36))
    return S


def p07():
    """Plan large : patatras ! La lampe se renverse : l'huile et la suie éclaboussent le corbeau, devenu tout noir des pieds à la tête."""
    S = Scene()
    nuit_arctique(S, 520)
    S.add(iglou(660, 600, 0.7, lumiere=True, S=S))
    S.add(qulliq(260, 770, 1.0, allumee=False, renverse=True))
    S.add(corbeau_b(420, 770, 1.5, noir=1, expr="surpris", ailes="ouvertes", coulures=True))
    S.add(harfang(640, 790, 1.0, taches=1.0, expr="surpris", ailes="haut", flip=True, regard=(-1, 0)))
    S.add(texte(400, 300, "Patatras !", 64, "#fff3bf", contour="#16213e"))
    return S


def p08():
    """Plan moyen : le corbeau, tout noir et furieux, crie « Gaq ! Gaq ! » ; le hibou s'envole dans la nuit, sous l'aurore boréale."""
    S = Scene()
    nuit_arctique(S, 560)
    S.add(lune(660, 120, 32))
    S.add(harfang(560, 330, 0.9, taches=1.0, expr="oups", ailes="haut", flip=True))
    S.add(corbeau_b(300, 780, 1.6, noir=1, expr="furieux", ailes="ouvertes", regard=(1, -1)))
    S.add(texte(560, 520, "Gaq ! Gaq !", 56, "#fff3bf", contour="#16213e"))
    return S


def p09():
    """Plan moyen : dans l'iglou, à la lueur du qulliq, une grand-mère inuk raconte l'histoire à deux enfants ; on voit dehors un harfang et un corbeau."""
    S = Scene()
    dedans_iglou(S)
    S.add(qulliq(400, 700, 1.1, S=S))
    S.add(personne(600, 790, 1.5, expr="content", bras="ouverts", flip=True, regard=(-1, 0), **GRAND_MERE))
    S.add(personne(170, 790, 1.15, expr="bouche_bee", bras="joues", regard=(1, 0), **ENFANTS[0]))
    S.add(personne(300, 790, 1.1, expr="rire", bras="ventre", regard=(1, 0), **ENFANTS[1]))
    S.add(pensee(310, 230, 120, "", depuis=(560, 440)))
    S.add(harfang(260, 300, 0.55, taches=1.0, expr="fier"), corbeau_b(370, 300, 0.55, noir=1, expr="oups"))
    S.cachette(60, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("hibou-seul.svg", vignette),
    ("01-tout-blancs.svg", p01), ("02-l-idee.svg", p02), ("03-point-par-point.svg", p03),
    ("04-magnifique.svg", p04), ("05-c-est-fini.svg", p05), ("06-ne-bouge-pas.svg", p06),
    ("07-patatras.svg", p07), ("08-gaq-gaq.svg", p08), ("09-dans-l-iglou.svg", p09),
]
