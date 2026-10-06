"""Le poulpe aux huit bras — le poulpe commun.

Le poulpe a huit bras couverts de ventouses, avec lesquelles il touche et
goûte. Il n'a pas d'os (seulement un petit bec dur) et peut se faufiler par
un trou minuscule. Il change de couleur et de texture pour se cacher ; en
danger, il lâche un nuage d'encre et file par jet d'eau. Il chasse les crabes
la nuit. Il a trois cœurs et le sang bleu. Il sait ouvrir un bocal. La mère
garde ses œufs en guirlandes dans sa grotte et les nettoie ; les petits, à
peine éclos, dérivent vers la surface.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant
from fantastique import ocean, algue, corail, crabe, bulles_eau, coquillage

ID = "poulpe-malin"
ROUGE = "#e8590c"
PEAU = "#ff8787"


# --- Personnages ------------------------------------------------------------

def _bras(x0, y0, angle, L, courbe, couleur, ventouses=True, ep=22, k=0):
    """Un bras qui part de (x0, y0) dans la direction `angle`, en s'enroulant
    (`courbe` > 0 : vers la droite)."""
    pts = []
    a = math.radians(angle)
    x, y = x0, y0
    pas = L / 14
    for i in range(15):
        pts.append((x, y))
        a += math.radians(courbe) / 14 * (1 + i / 10)
        x += math.cos(a) * pas
        y += math.sin(a) * pas
    m = []
    for i in range(14):
        (xa, ya), (xb, yb) = pts[i], pts[i + 1]
        w = ep * (1 - i / 16)
        m.append(trait(xa, ya, xb, yb, couleur, w))
    if ventouses:
        for i in range(2, 14, 2):
            (xa, ya), (xb, yb) = pts[i], pts[i + 1]
            dx, dy = xb - xa, yb - ya
            L2 = math.hypot(dx, dy) or 1
            nx, ny = -dy / L2, dx / L2
            w = ep * (1 - i / 16)
            m.append(cercle(xa + nx * w * 0.35, ya + ny * w * 0.35, w * 0.22, "#ffe3e3"))
    return m


def poulpe_(x, y, s=1.0, rot=0, couleur=PEAU, expr="sourire", regard=(0, 0), pose="etale", texture=False):
    """Poulpe ; (x, y) = centre du manteau (la « tête »). pose : "etale" (bras
    étalés au fond), "nage" (bras en arrière, il file vers le haut), "rentre"
    (bras repliés sous lui)."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    m = []
    if pose == "etale":
        for k, (a, c, L) in enumerate([(160, -60, 220), (140, -40, 240), (115, 60, 220), (100, -60, 200),
                                       (80, 60, 200), (65, -60, 220), (40, 40, 240), (20, 60, 220)]):
            m += _bras(0, 70, a, L, c, couleur if k % 2 else fonce)
    elif pose == "nage":
        for k in range(8):
            a = 90 + (k - 3.5) * 7
            m += _bras(0, 70, a, 260, (k - 3.5) * 6, couleur if k % 2 else fonce, ventouses=False, ep=20)
    else:
        for k in range(8):
            a = 90 + (k - 3.5) * 18
            m += _bras(0, 60, a, 110, (k - 3.5) * 30, couleur if k % 2 else fonce, ep=20)
    m.append(ellipse(0, -20, 74, 96, couleur))
    m.append(ellipse(-24, -60, 22, 34, eclaircir(couleur, 0.25), opacity=0.6))
    if texture:
        r = random.Random(4)
        for _ in range(14):
            m.append(cercle(r.uniform(-60, 60), r.uniform(-90, 50), r.uniform(5, 10), fonce))
    else:
        for px, py in [(-30, -70), (20, -84), (40, -40)]:
            m.append(cercle(px, py, 8, fonce))
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 40, 40, 22, 20, couleur))
        m.append(cercle(sgn * 40, 36, 16, "#fff9db"))
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * 40, 38, ys, (0, 0), taille=0.9))
        else:
            m.append(rect(sgn * 40 - 9 + regard[0] * 4, 32 + regard[1] * 4, 18, 8, ENCRE, rx=4))
    m.append(joue(-24, 64, 0.8) + joue(24, 64, 0.8))
    m.append(place(bouche(0, 0, bs, 0.6), 0, 62))
    return place(m, x, y, s, rot=rot)


def fond_mer(S, y=660, nuit_=False, graine=1):
    if nuit_:
        ocean(S, "#1b2a5c", "#0b1433", "#8c7b55", y)
    else:
        ocean(S, "#3bc9db", "#1864ab", "#f4d58d", y)
    r = random.Random(graine)
    S.add(algue(60, y + 20, 1.0, graine=graine), algue(760, y + 30, 0.8, "#37b24d", graine=graine + 1))


def rocher(x, y, s=1.0, couleur="#868e96"):
    m = [chemin("M -160 0 Q -170 -120 -60 -150 Q 40 -180 120 -120 Q 180 -60 160 0 Z", couleur),
         ellipse(-60, -100, 30, 14, eclaircir(couleur, 0.3), opacity=0.6), ellipse(60, -60, 40, 16, _assombrir(couleur, 0.85))]
    return place(m, x, y, s)


def bocal_(x, y, s=1.0, ouvert=False, contenu=""):
    m = [rect(-70, -170, 140, 170, "#e7f5ff", rx=24, opacity=0.6, stroke="#a5d8ff", stroke_width=5), contenu]
    if ouvert:
        m.append(place(rect(-60, -10, 120, 24, "#fa5252", rx=6), 110, -150, rot=40))
    else:
        m.append(rect(-60, -190, 120, 26, "#fa5252", rx=6))
    return place(m, x, y, s)


def coeur_schema(x, y, s=1.0):
    return place([chemin("M 0 30 C -50 -10 -40 -50 0 -26 C 40 -50 50 -10 0 30 Z", "#4dabf7")], x, y, s)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    fond_mer(S, 680)
    S.add(corail(640, 700, 1.2, "#ff8787"), coquillage(180, 740, 1.2))
    S.add(poulpe_(400, 470, 1.25, expr="rire"))
    S.add(bulles_eau(560, 260, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(poulpe_(200, 110, 0.55, expr="content"))
    return S


def p01():
    S = Scene()
    fond_mer(S, 680)
    S.add(poulpe_(400, 430, 1.3, expr="content"))
    S.add(texte(400, 110, "1, 2, 3, 4, 5, 6, 7, 8 !", 46, "#ffffff", contour="#1864ab"))
    return S


def p02():
    S = Scene()
    fond_mer(S, 680, graine=2)
    S.add(poulpe_(300, 380, 1.2, expr="concentre", regard=(1, 1)))
    S.add(coquillage(600, 700, 1.6))
    S.add(loupe(620, 330, 110, [rect(510, 220, 220, 220, PEAU)] + [cercle(560 + (k % 3) * 50, 280 + (k // 3) * 60, 20, "#ffe3e3",
                                                                               stroke="#fa5252", stroke_width=3) for k in range(6)],
                fond=PEAU, rot=130))
    S.add(etiquette(620, 490, "les ventouses", 34, "#c2255c"))
    return S


def p03():
    S = Scene()
    fond_mer(S, 680, graine=3)
    S.add(rocher(500, 720, 2.0))
    S.add(ellipse(470, 600, 26, 20, "#212529"))
    S.add(poulpe_(330, 560, 0.55, rot=60, pose="nage", expr="concentre"))
    S.add(texte(320, 200, "Je me faufile…", 48, "#ffffff", contour="#1864ab"))
    return S


def p04():
    S = Scene()
    fond_mer(S, 660, graine=4)
    S.add(rocher(400, 720, 2.4, "#868e96"))
    S.add(poulpe_(420, 470, 0.9, couleur="#8f959b", expr="malin", texture=True, pose="rentre"))
    S.add(poisson_simple(640, 220, 1.2, flip=True, couleur="#ffd43b"))
    S.add(texte(620, 140, "Où est le poulpe ?", 36, "#ffffff", contour="#1864ab"))
    return S


def p05():
    S = Scene()
    fond_mer(S, 680, graine=5)
    r = random.Random(5)
    for _ in range(26):
        S.add(cercle(r.uniform(150, 450), r.uniform(450, 700), r.uniform(30, 70), "#212529", opacity=0.35))
    S.add(poulpe_(560, 260, 0.75, rot=30, pose="nage", expr="surpris"))
    S.add(mouvement(470, 380, 1.2, "#ffffff", rot=-150))
    S.add(poisson_simple(150, 520, 2.4, couleur="#5c7cfa"))
    S.add(texte(250, 160, "Pschitt !", 64, "#ffffff", contour="#1864ab"))
    return S


def p06():
    S = Scene()
    fond_mer(S, 680, nuit_=True, graine=6)
    S.add(poulpe_(300, 420, 1.1, expr="concentre", regard=(1, 1)))
    S.add(crabe(620, 700, 1.1, expr="surpris"))
    return S


def p07():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(poulpe_(400, 380, 1.4, expr="content"))
    S.add(coeur_schema(340, 290, 0.9), coeur_schema(460, 290, 0.9), coeur_schema(400, 360, 1.1))
    S.add(etiquette(400, 120, "3 cœurs et du sang bleu !", 44, "#1864ab"))
    return S


def p08():
    S = Scene()
    fond(S, "#d0ebff")
    S.add(rect(0, 0, 800, 800, "#a5d8ff", opacity=0.4))
    S.add(rect(0, 680, 800, 120, "#f4d58d"))
    S.add(bocal_(560, 700, 1.6, ouvert=True, contenu=crabe(0, -40, 0.7, expr="surpris")))
    S.add(poulpe_(300, 420, 1.0, rot=20, expr="malin", regard=(1, 1)))
    S.add(texte(250, 130, "Facile !", 60, "#e8590c", contour="#fff"))
    return S


def p09():
    S = Scene()
    fond(S, "#1b2a5c")
    S.add(chemin("M 0 0 L 800 0 L 800 800 L 0 800 Z M 120 760 Q 80 300 400 220 Q 720 300 680 760 Z", "#495057", fill_rule="evenodd"))
    for k in range(7):
        x = 260 + k * 45
        S.add(trait(x, 260, x + 10, 420, "#f8f9fa", 2))
        for j in range(8):
            S.add(ellipse(x + j * 1.3, 280 + j * 18, 6, 9, "#fff9db"))
    S.add(poulpe_(420, 600, 1.0, expr="content", pose="rentre", regard=(0, -1)))
    S.add(g([chemin(f"M {340 + k * 40} 520 q 10 -20 0 -40", stroke="#a5d8ff", sw=4, opacity=0.7) for k in range(4)]))
    return S


def p10():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#74c0fc", "#1864ab"])))
    S.add(rect(0, 0, 800, 40, "#d0ebff"))
    r = random.Random(10)
    for _ in range(16):
        S.add(poulpe_(r.uniform(60, 740), r.uniform(120, 720), r.uniform(0.12, 0.18), rot=r.uniform(-20, 20), pose="nage",
                      expr=r.choice(["rire", "content", "sourire"])))
    S.add(fleche(400, 700, 400, 560, "#ffffff", 6, 22))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("poulpe-seul.svg", vignette),
    ("01-huit-bras.svg", p01), ("02-les-ventouses.svg", p02), ("03-pas-d-os.svg", p03),
    ("04-cache-cache.svg", p04), ("05-l-encre.svg", p05), ("06-la-chasse.svg", p06),
    ("07-trois-coeurs.svg", p07), ("08-le-bocal.svg", p08), ("09-les-oeufs.svg", p09),
    ("10-les-bebes.svg", p10),
]
