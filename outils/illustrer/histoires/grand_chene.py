"""Les saisons de Grand Chêne — le cycle des saisons."""
from base import *
from objets import *
from sciences import *

ID = "grand-chene"
TRONC, TRONC2 = "#8d5524", "#6f4218"
NOISETTE = dict(expr="content")

FEUILLAGES = {
    "printemps": ("#b2f2bb", "#8ce99a", "#d8f5a2"),
    "ete": ("#40c057", "#2f9e44", "#51cf66"),
    "automne": ("#fab005", "#f76707", "#e03131", "#ffd43b", "#fd7e14"),
}
BRANCHES = [(-190, -370), (-110, -450), (0, -500), (110, -455), (195, -375), (-150, -300), (160, -300)]
AMAS = [(-190, -380, 80), (-110, -460, 85), (0, -510, 90), (110, -465, 85), (195, -385, 80),
        (-60, -420, 90), (60, -420, 90), (-160, -300, 70), (160, -300, 70), (0, -380, 90)]


def gland(x, y, s=1.0, rot=0):
    m = [ellipse(0, 10, 14, 19, "#c9a227"), ellipse(-4, 6, 4, 8, "#fff", opacity=0.35),
         chemin("M -17 0 Q -16 -16 0 -16 Q 16 -16 17 0 Z", "#7c4a1e"),
         chemin("M -12 -6 L 12 -6 M -14 -1 L 14 -1 M -8 -12 L 8 -12", stroke="#5c3a1e", sw=2),
         trait(0, -16, 3, -24, "#5c3a1e", 4)]
    return place(m, x, y, s, rot=rot)


def feuille_chene(x, y, s=1.0, couleur="#40c057", rot=0):
    d = ("M 0 30 Q -4 20 -12 18 Q -20 12 -12 6 Q -22 0 -14 -8 Q -22 -16 -10 -20 Q -10 -30 0 -32 "
         "Q 10 -30 10 -20 Q 22 -16 14 -8 Q 22 0 12 6 Q 20 12 12 18 Q 4 20 0 30 Z")
    return place([chemin(d, couleur), trait(0, 30, 0, -26, assombrir(couleur, 0.8), 2)], x, y, s, rot=rot)


def chene(x, y, s=1.0, saison="ete", visage=None, creux=False, glands=False, neige=False, densite=1.0, graine=1):
    """Grand Chêne ; (x, y) = pied du tronc. saison : printemps, ete, automne, nu."""
    r = random.Random(graine)
    m = []
    for k, (bx, by) in enumerate(BRANCHES):
        sx, sy = (bx > 0) * 16 - 8, -200 - (k % 3) * 30
        m.append(chemin(f"M {sx} {sy} Q {bx * 0.35} {by * 0.8} {bx} {by}", stroke=TRONC, sw=24 if abs(bx) > 150 else 20))
        sg = 1 if bx >= 0 else -1
        for fx, fy, ep in [(bx + sg * 40, by - 50, 8), (bx - sg * 10, by - 70, 7), (bx * 0.75 + sg * 50, by * 0.8 - 20, 7)]:
            ox, oy = (bx, by) if ep != 7 or fx != bx * 0.75 + sg * 50 else (bx * 0.7, by * 0.85)
            m.append(chemin(f"M {n(ox)} {n(oy)} Q {n((ox + fx) / 2)} {n((oy + fy) / 2 - 8)} {n(fx)} {n(fy)}", stroke=TRONC, sw=ep))
    m.append(chemin("M -70 0 Q -40 -10 -40 -80 L -32 -260 Q 0 -280 32 -260 L 40 -80 Q 40 -10 70 0 Z", TRONC))
    m.append(chemin("M -14 -40 Q -20 -140 -8 -230 M 16 -60 Q 20 -150 12 -220", stroke=TRONC2, sw=5, opacity=0.6))
    if neige:
        for bx, by in BRANCHES:
            m.append(chemin(f"M {bx * 0.3} {by * 0.72 - 10} Q {bx * 0.6} {by * 0.85 - 14} {bx} {by - 12}", stroke="#fff", sw=10))
        m.append(ellipse(0, -266, 34, 10, "#fff"))
    if saison in FEUILLAGES:
        cols = FEUILLAGES[saison]
        for k, (ax, ay, ar) in enumerate(AMAS):
            if r.random() > densite:
                continue
            m.append(cercle(ax, ay, ar * (0.8 if saison == "printemps" else 1.0), cols[k % len(cols)]))
        for k in range(int(26 * densite)):
            ax, ay, ar = AMAS[k % len(AMAS)]
            a = r.uniform(0, 2 * math.pi)
            m.append(feuille_chene(ax + math.cos(a) * ar * 0.8, ay + math.sin(a) * ar * 0.8, 1.2, cols[(k + 1) % len(cols)], rot=math.degrees(a) + 90))
    if glands:
        for gx, gy in [(-150, -330), (-60, -370), (40, -350), (130, -330), (-10, -440), (170, -410), (-190, -420)]:
            m.append(gland(gx, gy, 1.3, rot=r.uniform(-20, 20)))
    if creux:
        m.append(ellipse(0, -130, 34, 46, "#3b2410"))
        m.append(ellipse(0, -130, 34, 46, "none", stroke=TRONC2, stroke_width=6))
    if visage:
        ys, bs, ss = EXPRESSIONS[visage]
        vy = -200 if not creux else -214
        m.append(oeil(-15, vy, ys, (0, 0), taille=1.4) + oeil(15, vy, ys, (0, 0), taille=1.4))
        m.append(ellipse(-27, vy + 20, 8, 5, ROSE, opacity=0.6) + ellipse(27, vy + 20, 8, 5, ROSE, opacity=0.6))
        if not creux:
            m.append(place(bouche(0, 0, bs, 1.1), 0, vy + 26))
    return place(m, x, y, s)


def pre(S, haut="#74c0fc", bas="#e7f5ff", herbe_="#8ce99a", herbe2="#69db7c", graine=1):
    ciel(S, haut, bas)
    collines(S, 640, eclaircir(herbe_, 0.3), graine=graine)
    sol(S, 640, herbe_, couleur2=herbe2, y2=720)


def ecureuil(x, y, s=1.0, **k):
    return perso("ecureuil", x, y, s, **k)


def couverture():
    S = Scene()
    pre(S, graine=3)
    S.add(soleil(680, 110, 50))
    cid = uid("c")
    S.defs.append(el("clipPath", rect(0, 0, 400, 800, "#000"), id=cid))
    S.add(g(chene(400, 700, 1.1, "ete", visage="content", graine=2), clip_path=f"url(#{cid})"))
    cid2 = uid("c")
    S.defs.append(el("clipPath", rect(400, 0, 400, 800, "#000"), id=cid2))
    S.add(g(chene(400, 700, 1.1, "automne", visage="content", graine=2), clip_path=f"url(#{cid2})"))
    for x, y, c in [(560, 560, "#f76707"), (640, 640, "#e03131"), (700, 520, "#fab005")]:
        S.add(feuille_chene(x, y, 1.3, c, rot=x))
    S.add(ecureuil(220, 760, 1.2, expr="rire", bras="porte", objet=gland(0, -72, 1.8)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ecureuil(190, 262, 1.0, expr="content", bras="porte", objet=gland(0, -74, 1.1)))
    return S


def nid(x, y, s=1.0):
    m = [chemin("M -70 -10 Q -60 40 0 44 Q 60 40 70 -10 Z", "#a47148"),
         chemin("M -70 -10 Q 0 6 70 -10", stroke="#7c4a1e", sw=8)]
    m += [chemin(f"M {-60 + k * 20} {6 + (k % 2) * 10} q 20 10 40 0", stroke="#7c4a1e", sw=3) for k in range(6)]
    return place(m, x, y, s)


def p01():
    S = Scene()
    pre(S, "#a5d8ff", "#f3faff", "#b2f2bb", "#8ce99a", 1)
    S.add(soleil(680, 110, 50, visage=True))
    S.add(chene(360, 720, 1.05, "printemps", visage="content", densite=0.75, graine=4))
    S.add(nid(510, 330, 0.8))
    S.add(mesange(600, 300, 0.8, expr="content", ailes="ouvertes", pattes=False, flip=True))
    S.add(trait(560, 285, 610, 270, "#7c4a1e", 4))
    for x, c in [(90, "#ffd43b"), (160, "#ff8787"), (620, "#cc5de8"), (720, "#ffd43b")]:
        S.add(fleur(x, 770, 1.1, c, tige=50))
    return S


def p02():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin("M -20 620 Q 400 560 820 600", stroke=TRONC, sw=70))
    for x, y, rr in [(120, 520, 90), (680, 500, 100), (60, 350, 70), (740, 300, 80)]:
        S.add(cercle(x, y, rr, "#b2f2bb"), cercle(x + 30, y - 20, rr * 0.7, "#d8f5a2"))
    S.add(nid(380, 540, 2.2))
    for k, x in enumerate((300, 380, 460)):
        S.add(oiseau(x, 540, 0.8, "#adb5bd", "#f1f3f5", bec_ouvert=True, ailes="haut" if k == 1 else "bas", pattes=False, regard=(0, -1)))
    S.add(mesange(610, 250, 1.1, expr="content", ailes="ouvertes", pattes=False, flip=True))
    S.add(chemin("M 520 262 q 10 -12 20 0 q 10 12 20 0", stroke="#82c91e", sw=8))
    S.add(texte(160, 160, "Piou !", 60, "#1c7ed6", contour="#fff", rot=-10), texte(420, 110, "Piou !", 50, "#1c7ed6", contour="#fff", rot=6))
    return S


def p03():
    S = Scene()
    pre(S, "#4dabf7", "#d0ebff", "#8ce99a", "#69db7c", 3)
    # Soleil haut : l'ombre du feuillage est juste sous l'arbre
    S.add(soleil(620, 70, 45))
    S.add(ellipse(380, 725, 250, 36, "#2b8a3e", opacity=0.35))
    S.add(chene(380, 720, 1.05, "ete", visage="sourire", graine=5))
    S.add(ecureuil(560, 760, 1.0, expr="dort", bras="bas"))
    S.add(zzz(610, 520, 1.1))
    S.add(papillon(160, 540, 0.9))
    return S


def p04():
    S = Scene()
    pre(S, "#74c0fc", "#e7f5ff", "#8ce99a", "#69db7c", 4)
    S.add(chene(300, 720, 1.1, "ete", glands=True, visage="content", graine=6))
    for k in range(9):
        S.add(gland(560 + (k % 4) * 34 + (k // 4) * 17, 770 - (k // 4) * 28, 1.2))
    S.add(ecureuil(620, 700, 1.1, expr="rire", bras="porte", objet=gland(0, -72, 1.8)))
    return S


def feuilles_qui_tombent(S, graine, zone, nb=18):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    cols = FEUILLAGES["automne"]
    for k in range(nb):
        S.add(feuille_chene(r.uniform(x0, x1), r.uniform(y0, y1), 1.2, cols[k % len(cols)], rot=r.uniform(0, 360)))


def p05():
    S = Scene()
    pre(S, "#91c3f0", "#fff4e6", "#c0d77f", "#a9c36a", 5)
    S.add(chene(380, 700, 1.05, "automne", densite=0.8, visage="sourire", graine=7))
    feuilles_qui_tombent(S, 5, (60, 300, 760, 700))
    for k in range(10):
        S.add(feuille_chene(160 + k * 55, 740 + (k % 3) * 14, 1.1, FEUILLAGES["automne"][k % 5], rot=k * 50))
    S.add(ecureuil(640, 770, 1.1, expr="inquiet", bras="joues", regard=(-1, -1)))
    return S


def p06():
    S = Scene()
    pre(S, "#91c3f0", "#fff4e6", "#c0d77f", "#a9c36a", 6)
    S.add(chene(160, 700, 0.95, "automne", densite=0.3, visage="content", graine=8))
    cols = FEUILLAGES["automne"]
    r = random.Random(3)
    for k in range(70):
        a = r.uniform(math.pi, 2 * math.pi)
        rr = r.uniform(0, 1) ** 0.5
        S.add(feuille_chene(500 + math.cos(a) * 230 * rr, 760 + math.sin(a) * 110 * rr, 1.3, cols[k % 5], rot=r.uniform(0, 360)))
    feuilles_qui_tombent(S, 9, (330, 280, 700, 560), 14)
    S.add(ecureuil(500, 580, 1.2, expr="rire", bras="haut", pieds_haut=True))
    S.add(bulle(250, 130, 400, 80, "N'aie pas peur !", 38, pointe=(170, 280)))
    return S


def p07():
    S = Scene()
    ciel(S, "#a5b4d4", "#e9ecef")
    sol(S, 640, "#f8f9fa", couleur2="#edf2ff", y2=720)
    S.add(chene(400, 700, 1.1, "nu", neige=True, creux=True, visage="dort", graine=9))
    # Noisette roulée en boule dans le creux, sa queue en guise de couverture
    S.add(cercle(400, 562, 32, "#d9692b"), ellipse(386, 580, 34, 18, "#e8590c", rot=-10))
    for sgn in (-1, 1):
        S.add(poly([(400 + sgn * 14, 540), (400 + sgn * 26, 516), (400 + sgn * 30, 546)], "#d9692b"))
    S.add(ellipse(400, 570, 16, 10, "#fff0dc"), oeil(389, 558, "fermes", taille=0.8), oeil(411, 558, "fermes", taille=0.8))
    S.add(zzz(460, 500, 0.9, "#5c7cfa"))
    flocons(S, 70, 7, (0, 0, 800, 760))
    return S


def p08():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(640, 140, 70, visage=True))
    S.add(rayons_soleil(580, 190, 450, 380, "#fcc419", 3, 28))
    S.add(chemin("M -20 560 Q 300 470 560 450", stroke=TRONC, sw=60))
    S.add(chemin("M 380 485 Q 420 420 440 400", stroke=TRONC, sw=18))
    # bourgeon qui s'ouvre
    S.add(ellipse(446, 394, 22, 32, "#a47148", rot=30))
    for rot, c in [(-50, "#8ce99a"), (5, "#b2f2bb"), (55, "#69db7c")]:
        S.add(place(feuille_chene(0, -40, 2.4, c), 452, 380, rot=rot))
    S.add(ecureuil(220, 550, 1.2, expr="joie", bras="haut", regard=(1, -1)))
    S.add(mesange(120, 220, 0.8, ailes="ouvertes", pattes=False))
    S.add(rect(0, 640, 800, 160, "#b2f2bb"))
    for x in range(40, 800, 90):
        S.add(fleur(x, 780, 0.9, ["#ffd43b", "#ff8787", "#cc5de8"][(x // 90) % 3], tige=60))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ecureuil-seul.svg", vignette),
    ("01-printemps.svg", p01), ("02-oisillons.svg", p02), ("03-ete.svg", p03), ("04-glands.svg", p04),
    ("05-automne.svg", p05), ("06-tas-de-feuilles.svg", p06), ("07-hiver.svg", p07), ("08-bourgeon.svg", p08),
]
