"""La girafe au long cou — le plus haut des animaux.

La girafe mesure environ cinq mètres. Elle mange les feuilles en haut des
acacias en enroulant sa longue langue bleu foncé autour des épines. Son cou
n'a que sept os, comme le nôtre, mais très longs. Pour boire, elle écarte
ses pattes de devant. Le girafon naît en tombant de haut, sa mère étant
debout, et tient sur ses pattes en moins d'une heure. Le dessin des taches
est différent pour chaque girafe. Elle dort très peu, souvent debout. Les
zèbres restent près d'elle : de là-haut, elle voit le danger arriver de loin.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant

ID = "girafe-cou"
FOND = "#f6d49a"
TACHE = "#c46a2a"


# --- Personnages ------------------------------------------------------------

def _taches(graine, zone, nb=40, couleur=TACHE):
    """Taches polygonales (réseau de « pavés ») sur une zone (x0, y0, x1, y1)."""
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    m = []
    pas = 34
    j = 0
    y = y0
    while y < y1:
        x = x0 + (pas / 2 if j % 2 else 0)
        while x < x1:
            cx, cy = x + r.uniform(-6, 6), y + r.uniform(-6, 6)
            pts = []
            for k in range(6):
                a = math.radians(k * 60 + r.uniform(-15, 15))
                d = r.uniform(11, 15)
                pts.append((cx + math.cos(a) * d, cy + math.sin(a) * d))
            m.append(poly(pts, couleur))
            x += pas
        y += pas * 0.86
        j += 1
    return m


def girafe(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), cou=0, langue=False, graine=1, boit=False,
           tache=TACHE, dort=False):
    """Girafe de profil, tête à droite ; (x, y) = sous les sabots.
    cou : rotation du cou (degrés, vers l'avant si > 0) ; boit : pattes de
    devant écartées, cou baissé jusqu'au sol."""
    ys, bs, ss = EXPRESSIONS[expr if not dort else "dort"]
    fonce = _assombrir(FOND, 0.8)
    m = []
    # queue
    m.append(chemin("M -96 -300 Q -112 -250 -110 -200", stroke=fonce, sw=5) + ellipse(-110, -192, 6, 14, "#5c3a1e"))
    # pattes du fond
    for px in (-56, 46):
        m.append(rect(px - 8, -280, 16, 280, fonce, rx=7))
        m.append(rect(px - 9, -14, 18, 14, "#5c3a1e", rx=4))
    # pattes de devant
    pattes = [(-80, 0), (66, 0)]
    for k, (px, dx) in enumerate(pattes):
        if boit and k == 1:
            m.append(chemin("M 66 -270 L 150 0", stroke=FOND, sw=17))
            m.append(rect(141, -14, 18, 14, "#5c3a1e", rx=4))
            continue
        m.append(rect(px - 9, -280, 18, 280, FOND, rx=8))
        m.append(cercle(px, -150, 11, FOND))
        m.append(rect(px - 10, -14, 20, 14, "#5c3a1e", rx=4))
    # corps
    corps = "M -110 -300 Q -100 -350 -20 -356 Q 60 -364 100 -340 Q 120 -300 100 -270 Q 0 -250 -100 -264 Q -114 -280 -110 -300 Z"
    cid = uid("gc")
    m.append(el("clipPath", chemin(corps, "#000"), id=cid))
    m.append(chemin(corps, FOND))
    m.append(g(_taches(graine, (-120, -370, 120, -250), couleur=tache), clip_path=f"url(#{cid})"))
    # cou et tête (qui pivotent ensemble autour de la base du cou)
    angle = cou if not boit else 112
    C = []
    cou_d = "M 50 -320 Q 90 -360 104 -440 L 150 -600 Q 160 -616 176 -600 Q 150 -470 130 -330 Q 110 -300 70 -290 Z"
    cid2 = uid("gn")
    C.append(chemin("M 54 -340 Q 80 -380 96 -440 L 146 -600", stroke="#a0522d", sw=10))
    C.append(el("clipPath", chemin(cou_d, "#000"), id=cid2))
    C.append(chemin(cou_d, FOND))
    C.append(g(_taches(graine + 7, (40, -620, 190, -280), couleur=tache), clip_path=f"url(#{cid2})"))
    # tête
    hx, hy = 186, -616
    for dx in (-18, -4):
        C.append(rect(hx + dx - 4, hy - 46, 8, 30, fonce, rx=4) + cercle(hx + dx, hy - 48, 7, "#5c3a1e"))
    C.append(ellipse(hx - 30, hy - 18, 20, 7, FOND, rot=-20))
    C.append(ellipse(hx, hy, 34, 24, FOND, rot=24))
    C.append(ellipse(hx + 34, hy + 18, 22, 16, eclaircir(FOND, 0.3), rot=24))
    C.append(ellipse(hx + 48, hy + 18, 3, 4, "#5c3a1e"))
    C.append(oeil(hx + 4, hy - 6, ys, regard, taille=0.9))
    if ys not in ("heureux", "fermes"):
        C.append(chemin(f"M {hx - 6} {hy - 16} l -4 -6 M {hx} {hy - 18} l 0 -7 M {hx + 6} {hy - 17} l 4 -6", stroke=ENCRE, sw=2))
    C.append(joue(hx + 16, hy + 10, 0.7))
    if langue:
        C.append(chemin(f"M {hx + 46} {hy + 30} Q {hx + 80} {hy + 10} {hx + 80} {hy - 30} Q {hx + 76} {hy - 50} {hx + 60} {hy - 44}",
                        stroke="#364fc7", sw=10))
    else:
        C.append(place(bouche(0, 0, bs, 0.6), hx + 40, hy + 26))
    m.append(g(C, transform=f"rotate({n(angle)} 90 -320)" if angle else None))
    return place(m, x, y, s, flip=flip)


def zebre(x, y, s=1.0, flip=False, expr="sourire"):
    """Petit zèbre de profil, tête à droite ; (x, y) = sous les sabots."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = [chemin("M -70 -110 Q -84 -80 -80 -50", stroke=ENCRE, sw=4)]
    for px in (-50, -30, 40, 60):
        m.append(rect(px - 7, -100, 14, 100, "#f8f9fa", rx=5))
        m.append(rect(px - 7, -12, 14, 12, ENCRE, rx=3))
    corps = "M -76 -110 Q -70 -150 0 -150 Q 60 -150 74 -120 Q 70 -80 0 -84 Q -70 -80 -76 -110 Z"
    cid = uid("z")
    m.append(el("clipPath", chemin(corps, "#000") + chemin("M 50 -120 L 100 -190 L 130 -170 L 80 -100 Z", "#000"), id=cid))
    m.append(chemin(corps, "#f8f9fa"))
    m.append(chemin("M 50 -120 L 100 -190 L 130 -170 L 80 -100 Z", "#f8f9fa"))
    m.append(g([rect(-80 + k * 16, -200, 7, 140, ENCRE, transform=f"rotate(15 {-80 + k * 16} -130)") for k in range(14)],
               clip_path=f"url(#{cid})"))
    m.append(chemin("M 96 -196 L 76 -150 L 56 -124", stroke=ENCRE, sw=8))
    m.append(ellipse(130, -170, 30, 18, "#f8f9fa", rot=30) + ellipse(150, -158, 12, 10, ENCRE, rot=30))
    m.append(poly([(106, -196), (112, -224), (120, -192)], "#f8f9fa"))
    m.append(oeil(124, -178, ys, (1, 0), taille=0.7) + joue(138, -166, 0.5))
    return place(m, x, y, s, flip=flip)


def grand_acacia(x, y, s=1.0, graine=1):
    m = [chemin("M -20 0 Q -10 -200 -10 -300 Q -60 -360 -150 -380 L -144 -394 Q -60 -380 0 -340 Q 40 -400 140 -420 L 146 -406 "
                "Q 60 -380 20 -300 Q 16 -150 24 0 Z", "#7c4a1e")]
    m.append(ellipse(-80, -400, 170, 40, "#74b816"))
    m.append(ellipse(60, -430, 180, 44, "#82c91e"))
    m.append(ellipse(-10, -460, 130, 34, "#94d82d"))
    r = random.Random(graine)
    for _ in range(14):
        px, py = r.uniform(-200, 200), r.uniform(-470, -380)
        m.append(trait(px, py, px + 8, py + 12, "#5c3a1e", 2))
    return place(m, x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    savane(S, 640)
    S.add(grand_acacia(660, 700, 1.0))
    S.add(girafe(300, 770, 0.88, expr="content", langue=True))
    S.add(girafe(520, 775, 0.4, expr="rire", graine=4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(girafe(150, 262, 0.36, expr="content"))
    S.add(girafe(290, 262, 0.18, expr="rire", graine=4))
    return S


def p01():
    S = Scene()
    savane(S, 640)
    S.add(girafe(300, 780, 1.1, expr="fier"))
    S.add(maison(620, 780, 0.9))
    S.add(enfant(520, 780, 0.5, expr="bouche_bee", habit="#e67700", jambes="#364fc7", regard=(-1, -1)))
    return S


def p02():
    S = Scene()
    savane(S, 640, arbres=False)
    S.add(grand_acacia(560, 780, 1.3, graine=2))
    S.add(girafe(240, 780, 1.12, expr="miam", cou=8))
    S.add(zebre(620, 780, 0.7, flip=True), zebre(720, 790, 0.6, flip=True))
    return S


def p03():
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#d0ebff"))
    S.add(chemin("M 800 120 Q 600 140 480 220", stroke="#7c4a1e", sw=26))
    for k in range(6):
        x0 = 520 + k * 50
        S.add(trait(x0, 170 + k * -6, x0 + 6, 130 + k * -6, "#f8f9fa", 4))
        S.add(ellipse(x0 + 20, 205 - k * 4, 26, 12, "#74b816"))
    S.add(place(girafe(0, 0, 1.0, expr="miam", langue=True), -40, 1310, 2.0))
    return S


def p04():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(girafe(260, 780, 1.12, expr="content"))
    for k in range(7):
        t = k / 6
        bx, by = 260 + 1.12 * (70 + t * 90), 780 + 1.12 * (-330 - t * 260)
        S.add(place(rect(-11, -14, 22, 28, "#ffffff", rx=6, stroke="#e67700", stroke_width=3), bx, by, 1, rot=20))
    S.add(enfant(620, 780, 1.0, expr="content", habit="#4dabf7", jambes="#364fc7", regard=(-1, 0)))
    for k in range(7):
        S.add(rect(612, 642 - k * 4.5, 16, 3.5, "#e67700", rx=1.5))
    S.add(etiquette(620, 520, "7 os", 40, "#e67700"), etiquette(600, 150, "7 os !", 40, "#e67700"))
    return S


def p05():
    S = Scene()
    savane(S, 600, arbres=False)
    S.add(ellipse(500, 760, 260, 50, "#74c0fc"))
    S.add(girafe(300, 760, 1.05, expr="miam", boit=True))
    return S


def p06():
    S = Scene()
    savane(S, 640)
    S.add(girafe(340, 780, 1.05, expr="content", cou=40, regard=(1, 1)))
    S.add(place(girafe(0, 0, 0.42, expr="surpris", graine=6), 560, 780, 1.0, rot=-10))
    S.add(mouvement(470, 620, 0.8, "#495057", rot=180))
    S.add(ellipse(560, 782, 80, 10, "#d9a441", opacity=0.6))
    S.add(texte(600, 200, "Boum ! Coucou !", 44, "#e67700", contour="#fff"))
    return S


def p07():
    S = Scene()
    savane(S, 640)
    S.add(girafe(300, 780, 1.05, expr="content", cou=24, regard=(1, 1)))
    S.add(girafe(460, 780, 0.45, expr="miam", graine=6, cou=-30))
    S.add(horloge(650, 180, 60, 1, 0))
    return S


def p08():
    S = Scene()
    fond(S, "#fff9db")
    for k, (x, gr, t) in enumerate([(160, 1, TACHE), (400, 5, "#a0522d"), (640, 9, "#d9822b")]):
        S.add(disque(x, 380, 105, FOND))
        cid = uid("t")
        S.add(el("clipPath", cercle(x, 380, 105, "#000"), id=cid))
        S.add(g(_taches(gr, (x - 120, 260, x + 120, 500), couleur=t), clip_path=f"url(#{cid})"))
    S.add(texte(400, 640, "Toutes différentes !", 48, "#e67700", contour="#fff"))
    return S


def p09():
    S = Scene()
    nuit(S)
    etoiles(S, 40, 3, (0, 0, 800, 500))
    S.add(lune(640, 110, 40))
    S.add(rect(0, 640, 800, 160, "#8c7b55"))
    S.add(acacia(140, 660, 0.9, "#2b3a55", "#33415c", "#2b2238"))
    S.add(girafe(380, 780, 1.05, dort=True))
    S.add(zzz(640, 260, 1.0, "#ffe066"))
    return S


def p10():
    S = Scene()
    savane(S, 620)
    S.add(girafe(240, 780, 1.12, expr="concentre", cou=-8, regard=(1, 0)))
    S.add(zebre(520, 780, 0.8), zebre(660, 790, 0.7, flip=True))
    S.add(texte(560, 150, "Je vois loin !", 50, "#e67700", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("girafes-seules.svg", vignette),
    ("01-la-plus-haute.svg", p01), ("02-en-haut-des-arbres.svg", p02), ("03-la-langue.svg", p03),
    ("04-sept-os.svg", p04), ("05-boire.svg", p05), ("06-le-girafon.svg", p06),
    ("07-debout.svg", p07), ("08-les-taches.svg", p08), ("09-dormir.svg", p09),
    ("10-la-sentinelle.svg", p10),
]
