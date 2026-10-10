"""Le castor bâtisseur — un documentaire sur le castor du Canada.

Le castor, le plus gros rongeur d'Amérique du Nord, a des incisives orange
(le fer les rend dures) qui poussent toute sa vie ; il les use en rongeant
des arbres (peupliers, saules). Il construit un barrage de branches, de
boue et de pierres : l'eau monte et forme un étang assez profond pour que
l'entrée de sa hutte soit sous l'eau et que l'étang ne gèle pas jusqu'au
fond. Dans la hutte, une pièce sèche au-dessus de l'eau, où vit la famille
(les parents, les petits de l'année et ceux de l'an passé). Sous l'eau, il
ferme le nez et les oreilles, ses paupières transparentes protègent ses
yeux, et il peut rester un quart d'heure sans respirer. Un coup de queue
sur l'eau donne l'alerte. À l'automne, il plante des branches dans la vase
près de la hutte : sa réserve pour l'hiver, sous la glace.

Plans : 1 large (la rivière au crépuscule) · 2 gros plan (les dents) ·
3 large (l'arbre tombe) · 4 moyen (la branche à la nage) · 5 large (le
barrage) · 6 schéma en coupe (la hutte) · 7 moyen (la famille) · 8 moyen
(sous l'eau) · 9 gros plan (le coup de queue) · 10 large (la réserve
d'automne) · 11 large en coupe (l'hiver sous la glace).
"""
from base import *
from base import _assombrir, _decoupe
from animaux import loupe, etiquette, roseau
from sciences import fleche
from fables import riviere

ID = "castor-batisseur"

BRUN = "#8f5b34"
BRUN_FONCE = "#5c3a1e"
QUEUE = "#4a3427"
NOIR_ = "#212529"


def castor(x, y, s=1.0, flip=False, rot=0, nage=False, branche=False, expr="sourire", ronge=False):
    """Castor de profil, tête à droite ; (x, y) = sous les pattes (ou ligne d'eau s'il nage)."""
    m = []
    # queue plate écailleuse
    queue = chemin("M -80 -30 Q -150 -40 -200 -20 Q -210 0 -190 10 Q -140 14 -80 -6 Z", QUEUE)
    m.append(queue)
    m.append(_decoupe_ecailles())
    if not nage:
        m += [ellipse(-40, -6, 26, 10, BRUN_FONCE), ellipse(60, -6, 20, 9, BRUN_FONCE)]
    m += [ellipse(0, -60, 100, 60, volume(BRUN, 0.3, 0.8)),
          ellipse(20, -40, 60, 26, eclaircir(BRUN, 0.15), opacity=0.5),
          ellipse(96, -92, 46, 40, volume(BRUN, 0.3, 0.8)),
          ellipse(132, -82, 22, 18, eclaircir(BRUN, 0.25)),
          cercle(146, -90, 7, NOIR_), cercle(80, -128, 10, BRUN_FONCE), cercle(82, -126, 5, "#d9a066"),
          chemin("M 128 -66 L 128 -48 L 142 -48 L 142 -66 Z", "#f76707", stroke="#d9480f", sw=1.5),
          trait(135, -66, 135, -48, "#d9480f", 1.5)]
    yeux = "fermes" if expr == "dort" else ("heureux" if expr == "content" else "normal")
    m.append(oeil(108, -104, yeux, (1, 0), taille=0.75))
    m.append(chemin("M 140 -80 l 20 -4 M 140 -76 l 22 2", stroke=BRUN_FONCE, sw=1.5))
    if not nage:
        m.append(ellipse(110, -40, 12, 18, BRUN_FONCE, rot=20))
    if branche:
        m.append(place([trait(-60, 0, 120, 0, "#8d5524", 10), ellipse(110, -14, 22, 9, "#69db7c", rot=-20), ellipse(80, 12, 20, 8, "#51cf66", rot=20)],
                       136, -56, 1.0, rot=-6))
    if ronge:
        for k in range(4):
            m.append(place(rect(-6, -3, 12, 6, "#e9c46a", rx=2), 170 + k * 14, -20 + (k % 2) * 16, rot=k * 40))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 210 * s, y - 140 * s, x + 170 * s, y)





def _decoupe_ecailles():
    forme = chemin("M -80 -30 Q -150 -40 -200 -20 Q -210 0 -190 10 Q -140 14 -80 -6 Z", "#000")
    traits = chemin(" ".join(f"M {x} -40 L {x - 10} 20" for x in range(-190, -80, 14)) + " " +
                    " ".join(f"M -210 {y} L -70 {y + 4}" for y in (-24, -12, 0)), stroke="#2b2118", sw=1.5, opacity=0.6)
    return _decoupe(traits, forme)


def arbre_ronge(x, y, s=1.0, entaille=0.5, couche=False):
    """Peuplier : tronc à moitié rongé en sablier ; (x, y) = pied."""
    tronc = "#d6d0c2"
    if couche:
        m = [rect(0, -40, 520, 40, cylindre(tronc, 0.3, 0.75, vertical=True), rx=16)]
        for k in range(5):
            m.append(cercle(420 + k * 30, -60 - (k % 2) * 30, 40, volume("#82c91e", 0.3, 0.75)))
        m.append(chemin("M 0 -40 L -30 -20 L 0 0", "#e9c46a"))
        return place(m, x, y, s)
    e = 26 * entaille
    m = [chemin(f"M -26 0 L -26 -60 Q {-26 + e} -80 -26 -100 L -26 -460 L 26 -460 L 26 -100 Q {26 - e} -80 26 -60 L 26 0 Z", cylindre(tronc, 0.3, 0.75)),
         chemin(f"M {-26 + e} -80 L {26 - e} -80", stroke="#e9c46a", sw=10),
         chemin("M -10 -200 l 6 -10 M 8 -300 l -6 -12 M -6 -390 l 4 -10", stroke="#495057", sw=3)]
    for cx, cy, r in ((0, -520, 100), (-80, -460, 70), (80, -470, 70)):
        m.append(cercle(cx, cy, r, volume("#94d82d", 0.3, 0.75)))
    return place(m, x, y, s)


def copeaux(x, y, nb=12, graine=1):
    r = random.Random(graine)
    return g([place(rect(-7, -3, 14, 6, "#e9c46a", rx=2), x + r.uniform(-90, 90), y + r.uniform(-10, 14), rot=r.uniform(0, 180)) for _ in range(nb)])


def barrage(x, y, w=500, s=1.0, graine=1):
    """Barrage de branches et de boue ; (x, y) = milieu du pied."""
    r = random.Random(graine)
    m = [chemin(f"M {-w / 2} 0 Q {-w / 2 + 40} -90 0 -110 Q {w / 2 - 40} -90 {w / 2} 0 Z", "#6d4c3a")]
    for k in range(40):
        bx = r.uniform(-w / 2 + 30, w / 2 - 30)
        by = r.uniform(-100, -10)
        L = r.uniform(60, 140)
        a = r.uniform(-30, 30)
        m.append(place(trait(-L / 2, 0, L / 2, 0, r.choice(("#8d5524", "#a0693a", "#6d4424", "#d6d0c2")), r.uniform(6, 11)), bx, by, rot=a))
    for k in range(6):
        m.append(ellipse(r.uniform(-w / 2 + 40, w / 2 - 40), -8, r.uniform(16, 26), r.uniform(10, 16), "#adb5bd"))
    return place(m, x, y, s)


def hutte(x, y, s=1.0, neige=False, graine=2):
    """Hutte de castor vue de dehors : dôme de branches et de boue ; (x, y) = milieu à la ligne d'eau."""
    r = random.Random(graine)
    m = [chemin("M -200 0 Q -170 -170 0 -190 Q 170 -170 200 0 Z", "#6d4c3a")]
    for k in range(36):
        a = r.uniform(-170, -10)
        rr = r.uniform(40, 180)
        bx, by = math.cos(math.radians(a)) * rr, math.sin(math.radians(a)) * rr * 0.95
        m.append(place(trait(-40, 0, 40, 0, r.choice(("#8d5524", "#a0693a", "#6d4424", "#d6d0c2")), r.uniform(5, 9)), bx, by, rot=r.uniform(-60, 60)))
    if neige:
        m.append(chemin("M -170 -70 Q -110 -180 0 -190 Q 110 -180 170 -70 Q 90 -130 0 -136 Q -90 -130 -170 -70 Z", "#f8f9fa"))
    return place(m, x, y, s)


def coupe_etang(S, y_eau=420, y_fond=720, hiver=False):
    """Coupe de l'étang : ciel, berge, eau, vase ; avec ou sans glace."""
    if hiver:
        ciel(S, "#a5d8ff", "#f1f3f5")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, y_eau, 800, y_fond - y_eau, lineaire([(0, "#74c0fc"), (1, "#1864ab")])))
    S.add(chemin(f"M 0 {y_fond} Q 400 {y_fond - 30} 800 {y_fond} L 800 800 L 0 800 Z", "#5c4033"))
    if hiver:
        S.add(rect(0, y_eau - 6, 800, 30, "#e7f5ff", opacity=0.9), rect(0, y_eau - 16, 800, 14, "#fff"))
    for k in range(5):
        S.add(chemin(f"M {80 + k * 150} {y_eau + 40 + (k % 2) * 60} q 20 -8 40 0", stroke="#a5d8ff", sw=4, opacity=0.6))


def eau_devant(S, y_ligne, x0=0, x1=800, couleur="#4dabf7"):
    """Eau par-dessus le bas du corps d'un castor qui nage (seuls la tête et le dos dépassent)."""
    S.add(rect(x0, y_ligne, x1 - x0, 800 - y_ligne, couleur, opacity=0.6))
    S.add(chemin(f"M {x0} {y_ligne} " + " ".join(f"q 15 -6 30 0" for _ in range(int((x1 - x0) / 30))), stroke="#e7f5ff", sw=3, opacity=0.8))


def foret_riviere(S, y=520, soir=False, graine=1, automne=False):
    if soir:
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    f1, f2 = ("#fd7e14", "#fab005") if automne else ("#40c057", "#69db7c")
    r = random.Random(graine)
    for k in range(8):
        S.add(sapin(r.uniform(0, 800), y - 10 + r.uniform(-10, 10), r.uniform(0.5, 0.8), "#2b8a3e", "#2f9e44") if k % 2 else
              arbre(r.uniform(0, 800), y + r.uniform(-10, 10), r.uniform(0.5, 0.7), f1, f2))
    S.add(rect(0, y, 800, 40, terrain("#8ce99a")))
    riviere(S, y + 30, "#4dabf7", "#a5d8ff")


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret_riviere(S, 480, graine=2)
    S.add(barrage(650, 600, 300, 0.7))
    S.add(castor(320, 760, 1.6, nage=True, branche=True))
    eau_devant(S, 760 - 60 * 1.6)
    S.cachette(70, 770, "poisson")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(castor(200, 250, 0.95))
    return S


def p01():
    """Plan large : au crépuscule, sur la rivière, un castor nage, la tête hors de l'eau."""
    S = Scene()
    foret_riviere(S, 500, soir=True, graine=3)
    S.add(castor(400, 640, 0.9, nage=True))
    eau_devant(S, 640 - 56 * 0.9)
    S.add(chemin("M 140 650 Q 250 620 330 650", stroke="#fff", sw=4, opacity=0.7), chemin("M 120 680 Q 240 650 330 676", stroke="#fff", sw=3, opacity=0.5))
    S.cachette(720, 760, "poisson")
    return S


def p02():
    """Gros plan : le castor ronge le tronc d'un peuplier avec ses grandes dents orange."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    sol(S, 640, "#8ce99a")
    S.add(arbre_ronge(520, 700, 1.4, entaille=0.6))
    S.add(castor(330, 720, 1.4, ronge=True, expr="concentre"))
    S.add(copeaux(470, 720, 14))
    S.camera(1.45, 470, 560)
    S.dessus(texte(400, 110, "Crr, crr, crr…", 56, BRUN_FONCE, contour="#fff"))
    return S


def p03():
    """Plan large : craaac ! le peuplier tombe ; le castor s'est écarté."""
    S = Scene()
    foret_riviere(S, 520, graine=4)
    S.add(place(arbre_ronge(0, 0, 1.0, entaille=1.0), 360, 640, rot=55))
    S.add(castor(180, 700, 0.8))
    S.add(texte(520, 200, "Craaac !", 72, BRUN_FONCE, contour="#fff"))
    S.add(mouvement(470, 340, 1.2, BRUN_FONCE, rot=40))
    S.cachette(730, 220, "air")
    return S


def p04():
    """Plan moyen : le castor tire une branche en nageant."""
    S = Scene()
    foret_riviere(S, 420, graine=5)
    S.add(castor(380, 600, 1.4, nage=True, branche=True))
    eau_devant(S, 600 - 56 * 1.4)
    S.add(chemin("M 80 610 Q 200 580 300 610", stroke="#fff", sw=4, opacity=0.7))
    S.cachette(720, 760, "poisson")
    return S


def p05():
    """Plan large : le barrage de branches et de boue ; derrière, l'eau monte et forme un étang."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 360, 800, 60, terrain("#8ce99a")))
    for k in range(6):
        S.add(sapin(60 + k * 140, 380, 0.6, "#2b8a3e", "#2f9e44"))
    S.add(rect(0, 410, 800, 180, lineaire([(0, "#74c0fc"), (1, "#339af0")])))
    S.add(texte(400, 470, "l'étang", 34, "#fff", contour="#1864ab"))
    S.add(barrage(400, 650, 760, 1.0))
    S.add(rect(0, 650, 800, 150, "#4dabf7"))
    S.add(chemin("M 0 660 Q 200 690 400 660 T 800 660", stroke="#a5d8ff", sw=5))
    S.add(texte(400, 740, "la rivière", 30, "#fff", contour="#1864ab"))
    S.add(castor(560, 560, 0.7, branche=True))
    S.add(castor(250, 560, 0.6, flip=True))
    S.add(texte(400, 140, "Un barrage !", 56, BRUN_FONCE, contour="#fff"))
    S.cachette(70, 760, "poisson")
    return S


def p06():
    """Schéma en coupe : la hutte : une pièce sèche au-dessus de l'eau, des entrées sous l'eau."""
    S = Scene()
    coupe_etang(S, 360, 700)
    S.add(hutte(420, 360, 1.5))
    S.add(chemin("M 280 360 Q 300 220 420 210 Q 540 220 560 360 Z", "#3b2a20"))
    S.add(ellipse(420, 340, 120, 30, "#a0693a"))
    S.add(castor(390, 335, 0.45, expr="dort"), castor(470, 335, 0.35, expr="dort", flip=True))
    S.add(chemin("M 330 360 Q 300 480 240 640", stroke="#3b2a20", sw=46), chemin("M 520 360 Q 560 500 620 650", stroke="#3b2a20", sw=46))
    S.add(castor(250, 600, 0.45, nage=True, rot=-60))
    S.add(etiquette(420, 160, "la pièce au sec", 30, BRUN_FONCE))
    S.add(etiquette(160, 540, "l'entrée", 28, "#fff", fond="#1864ab"), etiquette(680, 560, "sous l'eau", 28, "#fff", fond="#1864ab"))
    return S


def p07():
    """Plan moyen : dans la hutte, la famille castor : les parents et les petits."""
    S = Scene()
    fond(S, "#3b2a20")
    S.add(chemin("M 0 800 L 0 300 Q 400 40 800 300 L 800 800 Z", "#4a3427"))
    r = random.Random(3)
    for k in range(30):
        S.add(place(trait(-40, 0, 40, 0, r.choice(("#6d4424", "#8d5524", "#5c3a1e")), 8), r.uniform(0, 800), r.uniform(100, 400), rot=r.uniform(-60, 60)))
    S.add(rect(0, 600, 800, 200, "#a0693a"))
    S.add(castor(260, 680, 1.1, expr="content"))
    S.add(castor(560, 690, 1.1, flip=True, expr="content"))
    S.add(castor(400, 720, 0.55, expr="content"), castor(470, 760, 0.5, flip=True, expr="dort"), castor(330, 770, 0.5, expr="content"))
    S.ambiance("interieur")
    S.add(texte(400, 170, "Toute la famille au chaud", 42, "#ffd8a8"))
    return S


def p08():
    """Plan moyen : sous l'eau, le castor nage avec ses pattes palmées."""
    S = Scene()
    from animaux import sous_l_eau
    sous_l_eau(S, "#74c0fc", "#1864ab", "#5c4033", 700)
    S.add(castor(380, 440, 1.5, nage=True, rot=8))
    for x, y, rr in ((560, 320, 10), (590, 270, 7), (610, 230, 5)):
        S.add(cercle(x, y, rr, "none", stroke="#e7f5ff", stroke_width=3))
    S.add(texte(400, 110, "Un quart d'heure sous l'eau !", 42, "#fff", contour="#1864ab"))
    return S


def p09():
    """Gros plan : un renard approche ; le castor frappe l'eau de sa queue : pouf !"""
    S = Scene()
    foret_riviere(S, 460, graine=9)
    S.add(perso("renard", 660, 492, 0.6, expr="surpris", flip=True, regard=(-1, 0.3)))
    S.add(castor(330, 640, 1.4, nage=True, rot=-14))
    eau_devant(S, 640 - 50 * 1.4)
    for k in range(8):
        a = math.radians(-160 + k * 20)
        S.add(goutte(330 - 230 + math.cos(a) * 80, 640 + math.sin(a) * 60, 0.8, "#a5d8ff"))
    S.camera(1.15, 430, 520)
    S.dessus(texte(250, 120, "POUF !", 80, "#1864ab", contour="#fff"))
    S.cachette(720, 760, "poisson")
    return S


def p10():
    """Plan large : à l'automne, le castor plante des branches dans la vase, près de la hutte : sa réserve d'hiver."""
    S = Scene()
    foret_riviere(S, 420, graine=10, automne=True)
    S.add(hutte(500, 600, 1.0))
    r = random.Random(4)
    for k in range(14):
        S.add(place(trait(0, 0, 0, -r.uniform(60, 120), "#8d5524", 7), 240 + r.uniform(-90, 90), 620 + r.uniform(0, 40), rot=r.uniform(-20, 20)))
    S.add(castor(150, 640, 0.8, nage=True, branche=True))
    eau_devant(S, 640 - 50 * 0.8)
    S.add(texte(400, 150, "Une réserve pour l'hiver", 44, BRUN_FONCE, contour="#fff"))
    S.cachette(720, 760, "poisson")
    return S


def p11():
    """Plan large en coupe : l'hiver, l'étang gèle en surface ; sous la glace, le castor mange une branche de sa réserve."""
    S = Scene()
    coupe_etang(S, 380, 720, hiver=True)
    S.add(hutte(600, 380, 1.0, neige=True))
    r = random.Random(5)
    for k in range(12):
        S.add(place(trait(0, 0, 0, -r.uniform(120, 220), "#8d5524", 7), 300 + r.uniform(-80, 80), 720, rot=r.uniform(-15, 15)))
    S.add(castor(260, 580, 1.0, nage=True, branche=True, rot=-6))
    flocons(S, 30, 4, (0, 0, 800, 360))
    S.add(etiquette(170, 450, "la glace", 30, "#1864ab"), etiquette(620, 300, "la hutte", 30, BRUN_FONCE))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("castor-seul.svg", vignette),
    ("01-la-riviere.svg", p01), ("02-les-dents.svg", p02), ("03-craaac.svg", p03),
    ("04-la-branche.svg", p04), ("05-le-barrage.svg", p05), ("06-la-hutte.svg", p06),
    ("07-la-famille.svg", p07), ("08-sous-l-eau.svg", p08), ("09-pouf.svg", p09),
    ("10-la-reserve.svg", p10), ("11-sous-la-glace.svg", p11),
]
