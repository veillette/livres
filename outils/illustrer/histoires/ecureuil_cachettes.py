"""L'écureuil et ses cachettes — l'écureuil roux au fil des saisons.

En automne, l'écureuil roux cache des centaines de noisettes et de glands,
un par un, dans la terre et dans les creux des arbres. Il n'hiberne pas :
par grand froid il reste dans son nid de brindilles, enroulé dans sa queue,
et sort manger ses réserves, qu'il retrouve grâce à sa mémoire et à son
odorat. Ses incisives poussent toute sa vie. Les fruits oubliés germent au
printemps : l'écureuil plante des arbres.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche
from histoires.grand_chene import gland

ID = "ecureuil-cachettes"
ROUX = "#d9692b"
VENTRE = "#fff0dc"
AUTOMNE = [("#ffa94d", "#fd7e14"), ("#ffd43b", "#fab005"), ("#ff8787", "#fa5252")]


# --- Personnages ------------------------------------------------------------

def ecureuil(x, y, s=1.0, **k):
    """L'écureuil roux assis, vu de face (personnage de base.py)."""
    return perso("ecureuil", x, y, s, **k)


def ecureuil_profil(x, y, s=1.0, flip=False, rot=0, expr="sourire", regard=(1, 0), saut=False, queue_haut=True,
                    flaire=False):
    """Écureuil à quatre pattes, de profil, tête à droite ; (x, y) = sous les
    pattes. `saut` : pattes étirées, en plein bond."""
    ys, bs, ss = EXPRESSIONS[expr]
    c, fonce = ROUX, _assombrir(ROUX, 0.85)
    m = []
    if queue_haut:
        queue = "M -40 -50 C -110 -60 -150 -130 -120 -190 C -100 -230 -40 -220 -50 -170 C -56 -140 -90 -150 -84 -120 C -78 -90 -40 -96 -36 -64 Z"
    else:
        queue = "M -40 -50 C -100 -40 -170 -60 -200 -100 C -210 -130 -170 -150 -150 -120 C -130 -90 -90 -80 -40 -70 Z"
    m.append(chemin(queue, c))
    if queue_haut:
        m.append(chemin("M -50 -64 C -100 -80 -130 -140 -106 -184", stroke=eclaircir(c, 0.35), sw=10, opacity=0.7))
    if saut:
        m.append(chemin("M -30 -40 Q -70 -16 -96 -8", stroke=fonce, sw=16))
        m.append(chemin("M 30 -50 Q 70 -46 96 -60", stroke=fonce, sw=12))
    else:
        m.append(ellipse(-26, -10, 22, 12, fonce))
        m.append(chemin("M 26 -36 L 30 -6", stroke=fonce, sw=12))
    m.append(ellipse(-4, -50, 46, 30, c, rot=-10 if not saut else 0))
    m.append(ellipse(4, -40, 30, 16, VENTRE, rot=-10 if not saut else 0))
    if not saut:
        m.append(ellipse(-26, -36, 24, 22, c))
        m.append(ellipse(-20, -6, 20, 8, fonce))
        m.append(ellipse(30, -4, 10, 6, fonce))
    hx, hy = (48, -82) if not saut else (52, -66)
    if flaire:
        hx, hy = 56, -50
    m.append(poly([(hx - 16, hy - 22), (hx - 18, hy - 56), (hx - 2, hy - 28)], c))
    m.append(poly([(hx - 22, hy - 54), (hx - 28, hy - 70), (hx - 14, hy - 52)], fonce))
    m.append(ellipse(hx, hy, 30, 26, c))
    m.append(ellipse(hx + 14, hy + 8, 18, 14, VENTRE))
    m.append(ellipse(hx + 30, hy + 2, 6, 4.5, "#5c3a1e"))
    m.append(oeil(hx + 8, hy - 6, ys, regard, taille=0.85))
    m.append(joue(hx + 14, hy + 10, 0.7))
    if flaire:
        m.append(g([chemin(f"M {hx + 40} {hy - 6 + k * 8} q 10 -4 20 0", stroke="#868e96", sw=2.5) for k in range(3)]))
    return place(m, x, y, s, flip=flip, rot=rot)


def noisette(x, y, s=1.0, rot=0, ouverte=False):
    """Noisette ; (x, y) = centre. `ouverte` : coquille cassée en deux."""
    if ouverte:
        m = [chemin("M -26 4 Q -24 -22 -4 -22 L -4 4 Z", "#a0693a"), chemin("M 6 6 Q 8 -20 28 -20 Q 34 4 26 18 Z", "#a0693a"),
             ellipse(10, 14, 12, 9, "#f3d9b1")]
        return place(m, x, y, s, rot=rot)
    m = [ellipse(0, 4, 18, 20, "#a0693a"), chemin("M -16 -6 Q 0 -20 16 -6 Q 0 -14 -16 -6 Z", "#d9b48f"),
         ellipse(-6, 0, 4, 9, "#ffffff", opacity=0.3), trait(0, -14, 2, -22, "#5c3a1e", 3)]
    return place(m, x, y, s, rot=rot)


def nid(x, y, s=1.0, coupe=False, dedans=""):
    """Nid d'écureuil : grosse boule de brindilles ; `coupe` montre l'intérieur."""
    r = random.Random(3)
    m = [ellipse(0, 0, 90, 74, "#8d5524")]
    for _ in range(36):
        a = r.uniform(0, 2 * math.pi)
        d = r.uniform(0.75, 1.0) if coupe else r.uniform(0.2, 1.0)
        px, py = math.cos(a) * 86 * d, math.sin(a) * 70 * d
        ang = r.uniform(0, 180)
        dx, dy = math.cos(math.radians(ang)) * 26, math.sin(math.radians(ang)) * 26
        m.append(trait(px - dx, py - dy, px + dx, py + dy, r.choice(["#5c3a1e", "#a0693a", "#7c4a1e"]), 4))
    if coupe:
        m.append(ellipse(0, 6, 64, 50, "#e9c46a"))
        m.append(ellipse(0, 6, 54, 40, "#b5835a"))
        m.append(dedans)
    return place(m, x, y, s)


def arbre_automne(x, y, s=1.0, k=0, neige=False):
    f1, f2 = AUTOMNE[k % 3]
    if neige:
        f1, f2 = "#f8f9fa", "#e9ecef"
    return arbre(x, y, s, feuillage=f1, feuillage2=f2)


def foret_automne(S, y=600, graine=1, neige=False):
    if neige:
        ciel(S, "#a5d8ff", "#f1f3f5")
    else:
        ciel(S, "#a5d8ff", "#fff4e6")
    for k, (x, sc) in enumerate([(80, 1.0), (300, 0.8), (520, 0.9), (740, 1.05)]):
        if neige:
            S.add(sapin(x, y + 10, sc * 1.2, neige=True))
        else:
            S.add(arbre_automne(x, y + 10, sc, k + graine))
    S.add(rect(0, y, 800, 800 - y, "#f8f9fa" if neige else "#c0a36e"))
    r = random.Random(graine)
    if not neige:
        for _ in range(26):
            c = r.choice(["#fd7e14", "#fab005", "#fa5252", "#e8590c"])
            S.add(ellipse(r.uniform(0, 800), r.uniform(y + 20, 790), 12, 6, c, rot=r.uniform(0, 180)))


def tronc(S, x=400, w=200, couleur="#8d5524"):
    S.add(rect(x - w / 2, 0, w, 800, couleur))
    for k in range(7):
        S.add(chemin(f"M {x - w / 2 + 20 + (k * 37) % (w - 40)} {k * 120} q 10 40 0 80", stroke=_assombrir(couleur, 0.8), sw=5))


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    foret_automne(S, 620)
    S.add(ecureuil(400, 750, 1.9, expr="rire", bras="porte", objet=noisette(0, -76, 1.5)))
    S.add(noisette(180, 730, 1.2), gland(640, 720, 1.4, rot=20), noisette(600, 760, 1.0, rot=30))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ecureuil(200, 262, 0.95, expr="content", bras="porte", objet=noisette(0, -76, 1.5)))
    return S


def p01():
    S = Scene()
    foret_automne(S, 600)
    S.add(chemin("M 0 260 Q 300 280 520 220", stroke="#7c4a1e", sw=20))
    for k, (x, y) in enumerate([(120, 290), (250, 300), (380, 270), (470, 245)]):
        S.add(ellipse(x, y - 24, 28, 18, "#51cf66", rot=-20))
        S.add(noisette(x + 10, y + 20, 1.0))
    S.add(ecureuil(520, 740, 1.6, expr="joie", bras="tient", objet=noisette(68, -140, 1.2), regard=(-1, -1)))
    S.add(noisette(250, 720, 1.1), gland(330, 750, 1.2, rot=-20), noisette(700, 760, 1.0, rot=40))
    return S


def p02():
    S = Scene()
    foret_automne(S, 560, graine=2)
    S.add(ellipse(330, 690, 60, 18, "#7c4a1e"))
    S.add(noisette(330, 680, 1.2))
    for k in range(5):
        S.add(cercle(270 + k * 26, 664 - (k % 2) * 10, 7, "#7c4a1e"))
    S.add(ecureuil_profil(480, 720, 1.5, flip=True, expr="concentre", regard=(1, 0.6)))
    S.add(texte(400, 300, "Une ici…", 50, "#e8590c", contour="#fff"))
    return S


def p03():
    S = Scene()
    coupe_terre(S, 320, graine=6, terre="#a0693a")
    S.add(arbre_automne(620, 320, 1.0, 1))
    S.add(arbre_automne(140, 320, 0.8, 2))
    r = random.Random(3)
    for k in range(14):
        x, y = 40 + k * 55, r.uniform(380, 760)
        S.add(ellipse(x, y, 26, 22, "#6d4424"))
        S.add(noisette(x, y, 0.8) if k % 3 else gland(x, y, 0.85))
    S.add(ecureuil(380, 314, 1.0, expr="fier", bras="hanches"))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(arbre_automne(-20, 800, 2.6, 0), arbre_automne(840, 800, 2.6, 1))
    S.add(chemin("M 0 470 Q 120 450 250 480", stroke="#7c4a1e", sw=22))
    S.add(chemin("M 800 380 Q 680 360 560 390", stroke="#7c4a1e", sw=22))
    S.add(chemin("M 220 440 Q 400 230 560 340", stroke="#868e96", sw=4, stroke_dasharray="14 12"))
    S.add(ecureuil_profil(400, 330, 1.4, saut=True, queue_haut=False, rot=-8, expr="rire"))
    S.cachette(730, 620, "air")
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff4e6")
    tronc(S, 400, 240)
    S.add(ecureuil_profil(420, 400, 1.5, rot=90, expr="joie", regard=(1, 0)))
    S.add(loupe(650, 640, 100, [rect(550, 540, 200, 200, "#8d5524")] +
                [chemin(f"M {600 + k * 24} 620 q 14 10 6 30", stroke="#f8f9fa", sw=6) for k in range(4)] +
                [ellipse(640, 600, 60, 30, ROUX)], fond="#8d5524", rot=40))
    S.add(etiquette(650, 500, "griffes", 36, "#e8590c"))
    S.cachette(70, 620, "air")
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(rect(360, 300, 70, 500, "#8d5524"))
    S.add(chemin("M 400 460 Q 520 380 640 300", stroke="#8d5524", sw=26))
    S.add(chemin("M 390 420 Q 260 350 170 300", stroke="#8d5524", sw=24))
    S.add(arbre_automne(400, 420, 1.6, 0))
    S.add(nid(420, 360, 1.3))
    S.add(ecureuil_profil(580, 360, 1.0, flip=True, expr="content", regard=(1, 0)))
    S.add(place(trait(-30, 0, 30, -10, "#5c3a1e", 5), 520, 290))
    S.add(rect(0, 700, 800, 100, "#c0a36e"))
    return S


def p07():
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#a5d8ff"))
    flocons(S, 60, 7)
    S.add(chemin("M 0 520 Q 400 440 800 520", stroke="#8d5524", sw=40))
    S.add(chemin("M 0 500 Q 400 420 800 500", stroke="#ffffff", sw=12))
    dedans = place(perso("ecureuil", 0, 0, 0.42, expr="dort", bras="calin"), -10, 40) + \
        chemin("M 30 34 C 70 20 70 -40 30 -50 C 0 -54 -40 -40 -50 -10", stroke=ROUX, sw=22)
    S.add(nid(400, 380, 2.6, coupe=True, dedans=dedans))
    S.add(chemin("M 190 250 Q 400 150 610 250", stroke="#ffffff", sw=18))
    S.add(zzz(560, 200, 1.0))
    S.cachette(400, 70, "air")
    return S


def p08():
    S = Scene()
    foret_automne(S, 560, neige=True)
    flocons(S, 30, 8, (0, 0, 800, 560))
    S.add(ellipse(500, 700, 60, 20, "#c0a36e"))
    S.add(noisette(510, 690, 1.2))
    S.add(g([cercle(450 + k * 22, 680 - (k % 2) * 16, 8, "#ffffff", stroke="#dee2e6", stroke_width=2) for k in range(6)]))
    S.add(ecureuil_profil(300, 720, 1.6, expr="concentre", flaire=True, regard=(1, 0.5)))
    return S


def p09():
    S = Scene()
    foret_automne(S, 560, neige=True, graine=3)
    S.add(ecureuil(400, 760, 2.0, expr="miam", bras="porte", objet=noisette(0, -84, 1.8, ouverte=True)))
    S.add(noisette(180, 740, 1.2, ouverte=True, rot=30), noisette(620, 750, 1.1, ouverte=True, rot=-40))
    S.add(texte(400, 160, "Crac !", 80, "#e8590c", contour="#fff", rot=-6))
    return S


def pousse(x, y, s=1.0, feuilles=4):
    m = [chemin("M 0 0 Q -4 -40 0 -80", stroke="#2f9e44", sw=7)]
    for k in range(feuilles):
        sgn = -1 if k % 2 else 1
        m.append(ellipse(sgn * 22, -30 - k * 14, 20, 10, "#51cf66", rot=sgn * -30))
    return place(m, x, y, s)


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(arbre(120, 560, 1.2, "#69db7c", "#51cf66"), arbre(700, 560, 1.1, "#8ce99a", "#69db7c"))
    S.add(rect(0, 560, 800, 240, "#8ce99a"))
    for x, y, sc in [(250, 700, 1.1), (420, 650, 0.9), (560, 730, 1.3), (330, 770, 0.8)]:
        S.add(pousse(x, y, sc))
        S.add(noisette(x + 6, y + 6, 0.5, ouverte=True))
    S.add(ecureuil(660, 760, 1.2, expr="surpris", bras="joues", regard=(-1, 0)))
    for x, y in [(240, 440), (300, 420)]:
        S.add(fleur(x, 560, 0.7, "#ffd43b", tige=40))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ecureuil-seul.svg", vignette),
    ("01-l-automne.svg", p01), ("02-cacher.svg", p02), ("03-les-cachettes.svg", p03),
    ("04-le-saut.svg", p04), ("05-tete-en-bas.svg", p05), ("06-le-nid.svg", p06),
    ("07-l-hiver.svg", p07), ("08-retrouver.svg", p08), ("09-crac.svg", p09),
    ("10-les-arbres.svg", p10),
]
