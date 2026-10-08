"""Le loup et les sept chevreaux — n'ouvrir qu'à ceux qu'on connaît."""
from contes import *

ID = "loup-sept-chevreaux"
PETITS = [dict(couleur="#f8f9fa", acc=("noeud",), couleur_acc="#fa5252"), dict(couleur="#e9d8c4"),
          dict(couleur="#f1e3d3", acc=("echarpe",), couleur_acc="#4dabf7"), dict(couleur="#d9c2a5"),
          dict(couleur="#f8f9fa", acc=("fleur",), couleur_acc="#cc5de8"), dict(couleur="#e9d8c4", acc=("noeud",), couleur_acc="#fcc419"),
          dict(couleur="#fff9f0", acc=("echarpe",), couleur_acc="#51cf66")]


def maman(x, y, s=1.3, **k):
    k.setdefault("acc", ("tablier",))
    return perso("chevre", x, y, s, couleur="#f1f3f5", **k)


def chevreau(i, x, y, s=0.55, **k):
    d = dict(PETITS[i])
    d.update(k)
    return perso("chevre", x, y, s, **d)


def loup(x, y, s=1.2, patte_blanche=False, **k):
    corps = perso("loup", 0, 0, 1.0, **k)
    extras = []
    if patte_blanche:
        (gx, gy), (dx, dy) = mains(0, 0, 1.0, k.get("bras", "bas"), k.get("flip", False))
        extras.append(cercle(dx, dy, 14, "#fff", stroke="#dee2e6", stroke_width=2))
    return place([corps] + extras, x, y, s)


def rangee(S, y=790, expr="sourire", nb=7, x0=90, dx=62, **k):
    for i in range(nb):
        S.add(chevreau(i, x0 + i * dx, y + (i % 2) * 8, expr=expr, **k))


def salle(S):
    interieur(S, "#fff4e6", "#c9a27e", 560, papier="#ffe8cc")
    S.add(porte(640, 700, 170, 330, "#a0522d"))


def dehors(S, soir=False):
    ciel(S, "#a5d8ff", "#fff9db") if not soir else ciel(S, "#ffa8a8", "#fff4e6")
    S.add(nuage(160, 110, 0.6))
    collines(S, 580, "#b2f2bb", graine=15)
    sol(S, 580, "#94d82d")
    S.add(maison(200, 600, 0.9, mur="#fff4e6", toit="#e8590c", porte="#a0522d"))


def bord_riviere(S):
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 520, "#94d82d")
    S.add(chemin("M 0 690 Q 400 660 800 700 L 800 800 L 0 800 Z", "#4dabf7"))
    for k in range(5):
        S.add(chemin(f"M {60 + k * 160} {740 + (k % 2) * 30} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    S.add(arbre(160, 560, 1.4))


def gros_sac(x, y, s=1.0, plein=True, cailloux=False):
    m = [sac(0, 0, 1.6, "#c49a6c", plein=plein)]
    if cailloux:
        m.append(g([caillou(-30, -90, 0.5), caillou(20, -100, 0.6), caillou(-4, -120, 0.45)]))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    dehors(S)
    S.add(maman(560, 780, 1.3, expr="content", bras="ouverts"))
    rangee(S, 790, "rire", nb=7, x0=90, dx=68)
    S.add(loup(740, 640, 0.6, expr="malin", flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    for i in range(7):
        S.add(chevreau(i, 50 + i * 50, 262, 0.45, expr="rire"))
    return S


def p01():
    S = Scene()
    salle(S)
    S.add(maman(280, 790, 1.35, expr="content", bras="ouverts"))
    rangee(S, 790, "rire", x0=420, dx=58, s=0.5)
    return S


def p02():
    S = Scene()
    salle(S)
    S.add(maman(560, 790, 1.3, expr="inquiet", bras="montre", flip=True, objet=""))
    S.add(panier(640, 640, 0.8, contenu="legumes"))
    rangee(S, 790, "surpris", nb=7, x0=70, dx=62, s=0.5)
    S.add(bulle(420, 140, 500, 110, "N'ouvrez à personne !\nLe loup a les pattes noires.", 30, pointe=(560, 470)))
    return S


def porte_fermee(S):
    salle(S)
    rangee(S, 790, "inquiet", nb=7, x0=70, dx=62, s=0.5)


def p03():
    S = Scene()
    porte_fermee(S)
    S.add(texte(640, 320, "Toc, toc !", 50, "#6d4424", contour="#fff"))
    S.add(bulle(320, 150, 480, 110, "Non ! Maman a une voix\ndouce. Tu es le loup !", 32, pointe=(250, 600)))
    return S


def p04():
    S = Scene()
    dehors(S)
    S.add(loup(480, 780, 1.3, expr="miam", bras="bouche", objet=""))
    S.add(place(g([rect(-26, -60, 52, 60, "#fcc419", rx=10), rect(-30, -70, 60, 14, "#e67700", rx=5), texte(0, -20, "miel", 18, "#e67700")]), 610, 780))
    S.add(bulle(480, 150, 400, 100, "Ouvrez, c'est maman !", 34, pointe=(470, 460)))
    S.add(texte(480, 250, "(toute petite voix)", 28, "#495057"))
    return S


def p05():
    S = Scene()
    porte_fermee(S)
    S.add(rect(560, 692, 160, 8, "#343a40"))
    S.add(ellipse(640, 698, 40, 12, "#495057"))
    S.add(bulle(320, 150, 480, 110, "Non ! Maman a les pattes\nblanches. Tu es le loup !", 32, pointe=(250, 600)))
    return S


def p06():
    S = Scene()
    dehors(S)
    S.add(sac(600, 790, 1.0, "#f8f9fa", ecrit="farine"))
    S.add(loup(440, 780, 1.3, expr="malin", bras="donne", patte_blanche=True))
    S.add(g([cercle(560 + k * 10, 650 - k * 14, 6, "#f8f9fa", opacity=0.7) for k in range(4)]))
    return S


def p07():
    S = Scene()
    salle(S)
    S.add(porte(640, 700, 170, 330, "#a0522d", ouverte=True))
    S.add(loup(640, 700, 1.1, expr="furieux", bras="haut"))
    S.add(table(260, 790, 260, 120, nappe="#ffc9c9"))
    S.add(chevreau(0, 200, 790, 0.45, expr="oups"), chevreau(1, 300, 790, 0.45, expr="oups"))
    S.add(chevreau(2, 450, 790, 0.55, expr="oups", bras="haut"), chevreau(3, 80, 790, 0.5, expr="oups", bras="course"))
    S.add(texte(320, 200, "Vite, cachez-vous !", 50, "#c92a2a", contour="#fff"))
    return S


def p08():
    S = Scene()
    salle(S)
    S.add(horloge_comtoise(120, 790, 1.0, ouverte=True, dedans=chevreau(6, 0, -44, 0.55, expr="oups", bras="bouche")))
    S.add(gros_sac(560, 790, 1.2))
    for i, (dx, dy) in enumerate(((-40, -200), (0, -210), (40, -200))):
        S.add(chevreau(i, 560 + dx, 790 + dy, 0.35, expr="pleure"))
    S.add(loup(360, 790, 1.2, expr="malin", bras="hanches"))
    return S


def p09():
    S = Scene()
    bord_riviere(S)
    S.add(loup(260, 640, 1.1, expr="dort", bras="croises"))
    S.add(gros_sac(420, 640, 1.0))
    S.add(zzz(330, 300, 1.4))
    return S


def p10():
    S = Scene()
    salle(S)
    S.add(maman(380, 790, 1.3, expr="pleure", bras="calin", larmes=True))
    S.add(chevreau(6, 540, 790, 0.6, expr="pleure", larmes=True, bras="montre", flip=True))
    S.add(horloge_comtoise(120, 790, 1.0, ouverte=True))
    return S


def p11():
    S = Scene()
    bord_riviere(S)
    S.add(loup(160, 640, 1.0, expr="dort", bras="croises"))
    S.add(zzz(230, 320, 1.2))
    S.add(gros_sac(420, 660, 0.9))
    for i in range(6):
        S.add(chevreau(i, 360 + (i % 3) * 70, 520 - (i // 3) * 70, 0.4, expr="rire", bras="haut"))
    S.add(maman(640, 660, 1.1, expr="rire", bras="ouverts"), chevreau(6, 740, 660, 0.45, expr="rire", bras="haut"))
    return S


def p12():
    S = Scene()
    bord_riviere(S)
    S.add(loup(160, 640, 1.0, expr="dort", bras="croises"))
    S.add(gros_sac(420, 660, 0.9, cailloux=True))
    S.add(chevreau(0, 540, 660, 0.55, expr="malin", bras="porte", objet=caillou(0, -60, 0.5)))
    S.add(chevreau(1, 620, 660, 0.55, expr="rire", bras="porte", objet=caillou(0, -60, 0.5)))
    S.add(maman(730, 660, 1.0, expr="malin", bras="chut"))
    S.add(texte(500, 200, "Chut !", 70, "#1c7ed6", contour="#fff"))
    return S


def p13():
    S = Scene()
    bord_riviere(S)
    S.add(loup(460, 760, 1.1, expr="oups", bras="haut", rot=25))
    S.add(gros_sac(560, 770, 0.8, cailloux=False))
    S.add(texte(500, 200, "PLOUF !", 90, "#1c7ed6", contour="#fff"))
    S.add(ellipse(500, 770, 160, 20, "#fff", opacity=0.6))
    return S


def p14():
    S = Scene()
    dehors(S)
    S.add(maman(420, 780, 1.3, expr="rire", bras="danse"))
    for i in range(7):
        x = 110 + i * 95 if i < 3 else 330 + i * 65
        S.add(chevreau(i, x, 790 - (i % 2) * 30, 0.55, expr="rire", bras=("haut", "danse")[i % 2], rot=(-8 if i % 2 else 8)))
    S.add(notes(250, 420, 0.9, "#e64980"), notes(560, 400, 0.9, "#1c7ed6"))
    S.cachette(730, 240, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chevreaux-seuls.svg", vignette),
    ("01-maman-chevre.svg", p01), ("02-n-ouvrez-a-personne.svg", p02), ("03-grosse-voix.svg", p03), ("04-le-miel.svg", p04),
    ("05-patte-noire.svg", p05), ("06-la-farine.svg", p06), ("07-cachez-vous.svg", p07), ("08-le-sac.svg", p08),
    ("09-le-loup-dort.svg", p09), ("10-le-plus-petit.svg", p10), ("11-sauves.svg", p11), ("12-les-cailloux.svg", p12),
    ("13-plouf.svg", p13), ("14-la-danse.svg", p14),
]
