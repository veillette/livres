"""Filou et le miroir — la lumière.

Le reflet dans le lac est le symétrique du paysage par rapport à la surface
de l'eau. Dans le creux d'une cuillère (miroir concave) on se voit la tête en
bas ; sur le dos (convexe), à l'endroit. La lumière repart d'un miroir avec
le même angle qu'elle est arrivée. Les deux miroirs du périscope sont
parallèles, à 45°. Dans le prisme, le violet est plus dévié que le rouge. Le
catadioptre renvoie la lumière vers la voiture. Le kaléidoscope répète six
fois un même secteur, une fois sur deux retourné.
"""
from base import *
from objets import *
from sciences import *

ID = "filou-miroir"
CHOUETTE = dict(couleur="#adb5bd", visage="#f1f3f5", acc=("lunettes",))
RAYON = "#fab005"


def filou(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **k)


def foret(S, graine=1, y=620):
    ciel(S, "#a5d8ff", "#e7f5ff")
    for x in (40, 160, 660, 780):
        S.add(arbre(x, y + 20, 0.9, "#40c057", "#2f9e44"))
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 90)


def miroir_pied(x, y, s=1.0, reflet=None, w=150, h=230):
    """Miroir ovale sur pied ; (x, y) = pied au sol. `reflet` = dessin (coordonnées de page) vu dans la glace."""
    cx, cy = x, y - 60 * s - h * s / 2
    m = [trait(x, y, x, y - 70 * s, "#a0693a", 10 * s), ellipse(x, y, 60 * s, 12 * s, "#a0693a"),
         ellipse(cx, cy, w * s / 2 + 12 * s, h * s / 2 + 12 * s, "#c68642"), ellipse(cx, cy, w * s / 2, h * s / 2, "#d0ebff")]
    if reflet:
        cid = uid("m")
        m.append(el("clipPath", ellipse(cx, cy, w * s / 2, h * s / 2, "#000"), id=cid))
        m.append(g(reflet, clip_path=f"url(#{cid})", opacity=0.9))
    m.append(chemin(f"M {n(cx - w * s * 0.3)} {n(cy - h * s * 0.25)} Q {n(cx - w * s * 0.2)} {n(cy - h * s * 0.38)} {n(cx)} {n(cy - h * s * 0.4)}", stroke="#fff", sw=8 * s, opacity=0.7))
    m.append(ellipse(cx, cy, w * s / 2, h * s / 2, "#a5d8ff", opacity=0.2))
    return g(m)


def couverture():
    S = Scene()
    foret(S, 3)
    mx = 560
    S.add(miroir_pied(mx, 760, 1.5, reflet=filou(mx, 700, 0.95, expr="rire", flip=True, regard=(-1, 0))))
    S.add(filou(290, 770, 1.7, expr="rire", regard=(1, 0), bras="salut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(filou(140, 262, 0.95, expr="content", bras="salut"))
    S.add(miroir_pied(300, 262, 0.75, reflet=filou(300, 225, 0.55, expr="content", bras="salut", flip=True)))
    return S


def p01():
    S = Scene()
    foret(S, 1)
    S.add(miroir_pied(560, 770, 1.5, reflet=filou(560, 710, 0.95, expr="surpris", flip=True, regard=(-1, 0))))
    S.add(filou(270, 780, 1.6, expr="surpris", regard=(1, 0)))
    S.add(bulle(250, 150, 300, 80, "Bonjour ?", 42, pointe=(270, 330)))
    return S


def p02():
    S = Scene()
    foret(S, 2)
    S.add(soleil(90, 90, 45))
    mx = 590
    S.add(miroir_pied(mx, 770, 1.4, reflet=filou(mx, 715, 0.9, expr="content", flip=True, regard=(-1, 0))))
    S.add(filou(350, 780, 1.5, expr="content", regard=(1, 0)))
    # la lumière éclaire Filou, rebondit sur lui, touche le miroir et revient vers ses yeux
    S.add(fleche(130, 130, 330, 470, RAYON, 5), fleche(390, 470, 520, 440, RAYON, 5), fleche(520, 400, 390, 430, RAYON, 5))
    S.add(arbre(170, 640, 0.9), chouette(200, 420, 0.9, expr="sourire", ailes="ouvertes", regard=(1, 0), **CHOUETTE))
    return S


def p03():
    S = Scene()
    foret(S, 3)
    # Filou lève sa patte droite (à gauche sur l'image) ; son reflet lève la patte du même côté du miroir
    S.add(filou(230, 780, 1.5, expr="concentre", bras="salut", flip=True))
    S.add(miroir_pied(560, 780, 1.55, reflet=filou(560, 720, 0.95, expr="concentre", bras="salut")))
    S.add(texte(130, 280, "droite", 40, "#1c7ed6", contour="#fff"), texte(640, 280, "gauche ?", 40, "#e64980", contour="#fff"))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=600)
    S.add(rect(80, 180, 280, 170, "#fff", stroke="#dee2e6", stroke_width=3), texte(220, 290, "FILOU", 64, "#e8590c"))
    S.add(rect(460, 100, 280, 360, "#c68642", rx=14), rect(476, 116, 248, 328, "#d0ebff"))
    S.add(g([rect(-140, -85, 280, 170, "#fff", stroke="#dee2e6", stroke_width=3), texte(0, 25, "FILOU", 64, "#e8590c")], transform="translate(600 265) scale(-1 1)"))
    S.add(fleche(370, 265, 450, 265, "#495057", 5))
    S.add(filou(220, 790, 1.2, expr="bouche_bee", bras="haut", regard=(1, -1)))
    return S


def paysage_lac(x_, graine=5):
    m = [poly([(-20, 460), (200, 190), (420, 460)], "#9775fa"), poly([(200, 190), (240, 240), (160, 240)], "#fff"),
         poly([(300, 460), (520, 140), (740, 460)], "#7048e8"), poly([(520, 140), (570, 210), (470, 210)], "#fff"),
         nuage(160, 90, 0.7), nuage(620, 70, 0.6)]
    for x in (60, 130, 680, 750):
        m.append(sapin(x, 470, 0.8))
    return g(m)


def p05():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(paysage_lac(0))
    S.add(rect(0, 470, 800, 330, "#4dabf7"))
    # reflet : symétrique par rapport à la surface de l'eau (y = 470)
    S.add(g(paysage_lac(0), transform="translate(0 940) scale(1 -1)", opacity=0.55))
    S.add(rect(0, 470, 800, 330, "#1c7ed6", opacity=0.2))
    S.add(g([trait(100 + k * 130, 520 + (k % 3) * 80, 160 + k * 130, 520 + (k % 3) * 80, "#e7f5ff", 3, opacity=0.6) for k in range(5)]))
    return S


def cuillere_reflet(x, y, s, retourne):
    m = [ellipse(0, 0, 90, 120, "#ced4da"), rect(-14, 110, 28, 220, "#adb5bd", rx=10), ellipse(0, 0, 80, 110, "#e9ecef")]
    cid = uid("c")
    m.append(el("clipPath", ellipse(0, 0, 78, 108, "#000"), id=cid))
    visage = filou(0, 0, 1.0, expr="rire")
    if retourne:
        m.append(g(place(visage, 0, -40, 0.55, rot=180), clip_path=f"url(#{cid})"))
    else:
        m.append(g(place(visage, 0, 150, 1.0, sy=1.0), clip_path=f"url(#{cid})"))
    m.append(ellipse(-30, -50, 16, 34, "#fff", opacity=0.6))
    return place(m, x, y, s)


def p06():
    S = Scene()
    fond(S, "#fff9db")
    S.add(cuillere_reflet(220, 330, 1.4, True), cuillere_reflet(580, 330, 1.4, False))
    S.add(texte(220, 110, "le creux", 48, "#e8590c"), texte(580, 110, "le dos", 48, "#e8590c"))
    return S


def p07():
    S = Scene()
    foret(S, 7)
    S.add(soleil(120, 100, 55))
    S.add(rect(600, 100, 90, 560, "#8d5524"), cercle(645, 80, 150, "#40c057"))
    x, y, s = 300, 780, 1.4
    S.add(filou(x, y, s, expr="malin", bras="tient", regard=(1, -1)))
    hx, hy = max(mains(x, y, s, "tient"), key=lambda p: p[0])
    S.add(place(g([ellipse(0, 0, 26, 34, "#c68642"), ellipse(0, 0, 20, 28, "#d0ebff")]), hx + 10, hy - 30, rot=30))
    S.add(fleche(160, 140, hx + 4, hy - 34, RAYON, 5), fleche(hx + 16, hy - 34, 612, 330, RAYON, 5))
    S.add(cercle(640, 330, 34, "#fff3bf", opacity=0.9), cercle(640, 330, 50, "#ffe066", opacity=0.35))
    S.add(perso("lapin", 700, 780, 1.1, expr="rire", bras="haut", regard=(-1, -1), flip=True))
    return S


def p08():
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(rect(80, 600, 640, 24, "#adb5bd"), rect(80, 624, 640, 12, "#868e96"))
    S.add(texte(400, 690, "miroir", 44, "#495057"))
    px, py = 400, 600
    S.add(trait(px, py, px, 160, "#868e96", 3, stroke_dasharray="10 10"))
    S.add(fleche(140, 200, px - 4, py - 6, RAYON, 8), fleche(px + 4, py - 6, 660, 200, RAYON, 8))
    ang = math.degrees(math.atan2(py - 200, px - 140))
    S.add(chemin(f"M {px} {py - 110} A 110 110 0 0 0 {px - 110 * math.cos(math.radians(ang))} {py - 110 * math.sin(math.radians(ang))}", stroke="#e64980", sw=5))
    S.add(chemin(f"M {px} {py - 110} A 110 110 0 0 1 {px + 110 * math.cos(math.radians(ang))} {py - 110 * math.sin(math.radians(ang))}", stroke="#e64980", sw=5))
    return S


def p09():
    S = Scene()
    foret(S, 9)
    # périscope : deux miroirs parallèles à 45°
    tx = 470
    S.add(buisson(560, 690, 1.8, "#2f9e44", "#40c057"))
    S.add(rect(tx - 40, 230, 80, 450, "#fab005", rx=6), rect(tx - 40, 230, 110, 70, "#fab005", rx=6), rect(tx - 110, 610, 110, 70, "#fab005", rx=6))
    S.add(trait(tx - 34, 304, tx + 34, 236, "#adb5bd", 8), trait(tx - 34, 674, tx + 34, 606, "#adb5bd", 8))
    S.add(fleche(700, 265, tx + 6, 265, RAYON, 5), fleche(tx, 275, tx, 630, RAYON, 5), fleche(tx - 6, 640, tx - 130, 640, RAYON, 5))
    S.add(filou(300, 780, 1.2, expr="malin", regard=(1, -1)))
    S.add(perso("lapin", 700, 400, 0.9, expr="content", flip=True))
    S.add(bulle(250, 150, 300, 80, "Coucou, Lapin !", 36, pointe=(300, 450)))
    return S


def p10():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(rect(0, 640, 800, 160, "#e8c39e"))
    S.add(rect(40, 120, 40, 540, "#c68642"), rect(720, 120, 40, 540, "#c68642"))
    S.add(rect(80, 120, 20, 540, "#d0ebff"), rect(700, 120, 20, 540, "#d0ebff"))
    # reflets de reflets : de plus en plus petits et lointains, un sur deux retourné
    for k in range(5, 0, -1):
        s = 1.2 * 0.74 ** k
        dx = 300 * (1 - 0.62 ** k)
        for sgn in (-1, 1):
            S.add(g(filou(400 + sgn * dx, 720 - 90 * (1 - 0.74 ** k), s, expr="rire", flip=(k % 2 == 1)), opacity=0.9 - k * 0.1))
    S.add(filou(400, 740, 1.2, expr="rire", bras="ouverts"))
    return S


def p11():
    S = Scene()
    fond(S, "#343a40")
    S.add(cercle(400, 400, 330, "#adb5bd"), cercle(400, 400, 300, "#1c1f2b"))
    r = random.Random(11)
    secteur = []
    cols = ["#fa5252", "#fcc419", "#51cf66", "#339af0", "#cc5de8", "#ff922b"]
    for k in range(9):
        a = math.radians(r.uniform(4, 56))
        d = r.uniform(50, 270)
        forme = r.choice(["rond", "etoile", "losange"])
        c = cols[k % len(cols)]
        x, y = math.cos(a) * d, math.sin(a) * d
        if forme == "rond":
            secteur.append(cercle(x, y, r.uniform(12, 24), c))
        elif forme == "etoile":
            secteur.append(etoile5(x, y, r.uniform(14, 24), c, rot=r.uniform(0, 70)))
        else:
            secteur.append(place(poly([(0, -20), (12, 0), (0, 20), (-12, 0)], c), x, y, rot=math.degrees(a)))
    wedge = g(secteur)
    cid = uid("k")
    S.defs.append(el("clipPath", chemin("M 0 0 L 300 0 A 300 300 0 0 1 150 259.8 Z", "#000"), id=cid))
    wedge = g(wedge, clip_path=f"url(#{cid})")
    for k in range(6):
        t = f"translate(400 400) rotate({k * 60})" + (" scale(1 -1) rotate(-60)" if k % 2 else "")
        S.add(g(wedge, transform=t))
    for k in range(3):
        S.add(place(trait(-300, 0, 300, 0, "#fff", 2, opacity=0.25), 400, 400, rot=k * 60))
    return S


def p12():
    S = Scene()
    foret(S, 12)
    S.add(ellipse(400, 690, 120, 30, "#69db7c"))
    S.add(coccinelle(420, 680, 0.6))
    # la loupe fait dévier la lumière : on voit la coccinelle en grand
    S.add(cercle(430, 440, 120, "#e7f5ff", opacity=0.5))
    cid = uid("l")
    S.defs.append(el("clipPath", cercle(430, 440, 116, "#000"), id=cid))
    S.add(g([rect(300, 300, 260, 280, "#b2f2bb"), coccinelle(430, 460, 2.4)], clip_path=f"url(#{cid})"))
    S.add(cercle(430, 440, 120, "none", stroke="#495057", stroke_width=14), place(rect(-12, 0, 24, 170, "#a0693a", rx=8), 520, 530, rot=-40))
    S.add(filou(160, 780, 1.2, expr="bouche_bee", regard=(1, -1)))
    S.add(chouette(680, 780, 1.0, expr="sourire", regard=(-1, -1), **CHOUETTE))
    return S


def p13():
    S = Scene()
    foret(S, 13)
    fid = uid("f")
    S.defs.append(el("filter", el("feGaussianBlur", stdDeviation=7), id=fid))
    S.add(g([rect(60, 110, 300, 360, "#fff", rx=10), texte(210, 220, "A B C", 56, ENCRE), fleur(210, 420, 1.2, "#fa5252", tige=80)], filter=f"url(#{fid})"))
    S.add(rect(440, 110, 300, 360, "#fff", rx=10), texte(590, 220, "A B C", 56, ENCRE), fleur(590, 420, 1.2, "#fa5252", tige=80))
    S.add(texte(210, 510, "sans lunettes", 32, "#495057"), texte(590, 510, "avec lunettes", 32, "#2f9e44"))
    S.add(chouette(400, 790, 1.2, expr="content", **CHOUETTE))
    return S


def p14():
    S = Scene()
    fond(S, "#212529")
    S.add(rect(0, 100, 150, 220, "#fff3bf"), rect(20, 120, 110, 180, "#a5d8ff"))
    # le prisme dévie le violet plus que le rouge : rouge en haut, violet en bas (pointe du prisme en haut)
    px, py = 360, 380
    S.add(poly([(px, py - 130), (px - 120, py + 90), (px + 120, py + 90)], "#e7f5ff", opacity=0.55, stroke="#fff", stroke_width=3))
    S.add(trait(130, 220, px - 60, py - 10, "#fff", 12))
    cols = ARC_COULEURS
    for k, c in enumerate(cols):
        S.add(poly([(px - 60, py - 10), (px + 60, py + 8 + k * 3), (780, 300 + k * 60), (780, 300 + (k + 1) * 60 - 6), (px + 60, py + 12 + k * 3)], c, opacity=0.85))
    S.add(filou(160, 790, 1.1, expr="bouche_bee", regard=(1, -1)))
    return S


def p15():
    S = Scene()
    ciel(S, "#0b1433", "#1b2459")
    etoiles(S, 40, 15, (0, 0, 800, 380))
    S.add(rect(0, 560, 800, 240, "#343a40"), g([rect(k * 160 + 20, 690, 90, 10, "#fff") for k in range(5)]))
    # la voiture éclaire ; le catadioptre renvoie la lumière vers la voiture
    S.add(poly([(700, 600), (330, 520), (330, 600)], "#fff3bf", opacity=0.35))
    S.add(place(g([rect(-110, -70, 220, 70, "#fa5252", rx=18), rect(-70, -120, 140, 60, "#fa5252", rx=18), rect(-56, -110, 112, 42, "#a5d8ff", rx=8),
                   cercle(-60, 0, 26, ENCRE), cercle(60, 0, 26, ENCRE), ellipse(-110, -40, 12, 16, "#fff3bf")]), 810, 640))
    # Filou roule vers la gauche ; le catadioptre rouge, à l'arrière, fait face à la voiture
    S.add(velo(260, 680, 1.2, couleur="#339af0", flip=True))
    S.add(filou(265, 555, 0.85, expr="content", bras="guidon", flip=True))
    S.add(rect(345, 590, 20, 26, "#fa5252", rx=4), eclat(355, 603, 0.9, "#ffa8a8"))
    S.add(fleche(380, 575, 640, 575, "#ff8787", 5))
    return S


def p16():
    S = Scene()
    fond(S, "#e8c39e")
    S.add(chemin("M 0 0 L 800 0 L 800 800 L 0 800 Z M 80 120 Q 400 -40 720 120 L 720 800 L 80 800 Z", "#a0693a", fill_rule="evenodd"))
    S.add(g([cercle(160 + k * 110, 80 + (k % 2) * 20, 10, "#8d5524") for k in range(6)]))
    S.add(soleil(640, 180, 36))
    mx = 560
    S.add(trait(mx, 170, mx, 220, "#495057", 3))
    S.add(g([ellipse(mx, 360, 100, 140, "#c68642"), ellipse(mx, 360, 86, 126, "#d0ebff")]))
    cid = uid("m")
    S.defs.append(el("clipPath", ellipse(mx, 360, 86, 126, "#000"), id=cid))
    S.add(g(filou(mx, 480, 0.85, expr="rire", flip=True, bras="salut"), clip_path=f"url(#{cid})", opacity=0.9))
    S.add(filou(290, 780, 1.6, expr="rire", bras="salut", regard=(1, -1)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("filou-seul.svg", vignette),
    ("01-un-autre-renard.svg", p01), ("02-reflet.svg", p02), ("03-droite-gauche.svg", p03), ("04-ecriture.svg", p04),
    ("05-lac.svg", p05), ("06-cuillere.svg", p06), ("07-tache-de-soleil.svg", p07), ("08-rebond.svg", p08),
    ("09-periscope.svg", p09), ("10-deux-miroirs.svg", p10), ("11-kaleidoscope.svg", p11), ("12-loupe.svg", p12),
    ("13-lunettes.svg", p13), ("14-arc-en-ciel.svg", p14), ("15-catadioptre.svg", p15), ("16-bonjour.svg", p16),
]
