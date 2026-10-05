"""Où est passé le sucre ? — dissoudre et retrouver.

Le sucre et le sel se dissolvent dans l'eau : ils se séparent en morceaux
trop petits pour être vus, mais ils sont toujours là (l'eau est sucrée ou
salée). Le sable ne se dissout pas : il tombe au fond. L'huile ne se mélange
pas : elle flotte au-dessus. Le sucre se dissout plus vite dans l'eau chaude.
Quand l'eau s'évapore, le sel réapparaît en cristaux (marais salants). Un
filtre retient le sable, mais pas le sel dissous.
"""
from base import *
from objets import *
from sciences import fleche, verre
from fantastique import personne

ID = "sucre-disparu"
EAU = "#d0ebff"
SABLE = "#e0b860"
HUILE = "#ffe066"


def pistache(x, y, s=1.0, **k):
    return perso("panda", x, y, s, **{**dict(habit="#20c997", acc=("noeud",), couleur_acc="#ff6b6b"), **k})


def papi(x, y, s=1.2, **k):
    return perso("panda", x, y, s, **{**dict(habit="#f08c00", acc=("lunettes",)), **k})


def ami(x, y, s=0.9, **k):
    return perso("castor", x, y, s, **{**dict(habit="#4dabf7"), **k})


# ---------------------------------------------------------------------------
# Objets
# ---------------------------------------------------------------------------

def cuisine(S, y=560):
    interieur(S, "#fff9db", "#e8c39e", y)
    for i in range(0, 800, 50):
        for j in range(y - 190, y - 14, 50):
            S.add(rect(i + 2, j + 2, 46, 46, "#e3fafc", rx=4, opacity=0.8))
    S.add(fenetre(580, 70, 160, 140, "#a5d8ff", rideaux="#69db7c"))


def plan_travail(S, y=600):
    S.add(rect(0, y, 800, 30, "#c68642"), rect(0, y + 30, 800, 800 - y - 30, "#e8c39e"))


def morceau_sucre(x, y, s=1.0, rot=0):
    return place([rect(-12, -12, 24, 24, "#fff", rx=3, stroke="#dee2e6", stroke_width=2), rect(-12, -12, 24, 6, "#f1f3f5", rx=2)], x, y, s, rot=rot)


def sucrier(x, y, s=1.0):
    m = [chemin("M -50 0 Q -60 -60 -46 -80 L 46 -80 Q 60 -60 50 0 Z", "#74c0fc"),
         ellipse(0, -80, 46, 10, "#a5d8ff"), ellipse(0, -84, 40, 7, "#fff")]
    m += [texte(0, -30, "SUCRE", 22, "#fff")]
    return place(m, x, y, s)


def pot_sel(x, y, s=1.0):
    m = [rect(-30, -90, 60, 90, "#fff", rx=10, stroke="#adb5bd", stroke_width=3), rect(-30, -104, 60, 18, "#adb5bd", rx=6),
         texte(0, -36, "SEL", 22, "#495057")]
    return place(m, x, y, s)


def pichet(x, y, s=1.0, niveau=0.7, couleur=EAU):
    """Pichet transparent ; (x, y) = milieu du bas."""
    m = [chemin(f"M -60 {-200 * niveau} L 60 {-200 * niveau} L 58 -8 Q 0 0 -58 -8 Z", couleur, opacity=0.9),
         chemin("M -64 -200 L -60 -4 Q 0 6 60 -4 L 64 -200 L 82 -214", stroke="#adb5bd", sw=4, fill="#e7f5ff", fill_opacity=0.25),
         chemin("M 62 -170 Q 112 -150 104 -90 Q 100 -60 60 -50", stroke="#adb5bd", sw=10),
         chemin("M -48 -180 L -42 -60", stroke="#fff", sw=7, opacity=0.8)]
    return place(m, x, y, s)


def citron(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 30, 22, "#ffd43b"), ellipse(31, 0, 5, 4, "#fab005"), ellipse(-8, -8, 8, 4, "#fff", opacity=0.6)], x, y, s, rot=rot)


def cuillere(x, y, s=1.0, rot=0, sucre=False):
    m = [rect(-4, 0, 8, 120, "#adb5bd", rx=4), ellipse(0, -10, 16, 22, "#ced4da")]
    if sucre:
        m.append(ellipse(0, -14, 13, 12, "#fff", stroke="#dee2e6", stroke_width=1.5))
    return place(m, x, y, s, rot=rot)


def grains(x0, y0, x1, y1, nb=30, graine=1, couleur="#fff", r=3, contour="#ced4da"):
    rnd = random.Random(graine)
    return g([cercle(rnd.uniform(x0, x1), rnd.uniform(y0, y1), r, couleur, stroke=contour, stroke_width=1) for _ in range(nb)])


def tas(x, y, w=40, h=14, couleur=SABLE):
    """Petit tas au fond d'un verre ; (x, y) = milieu du fond."""
    return chemin(f"M {x - w} {y} Q {x} {y - 2 * h} {x + w} {y} Z", couleur)


def tasse_fumante(x, y, s=1.0, couleur="#ff8787", fumee=True, depot=False):
    m = [chemin("M -60 -110 L 60 -110 L 50 0 Q 0 8 -50 0 Z", couleur),
         chemin("M 58 -90 Q 100 -86 92 -50 Q 86 -24 52 -26", stroke=couleur, sw=10),
         ellipse(0, -110, 60, 12, "#f8f0e3")]
    if depot:
        m.append(grains(-30, -118, 30, -104, 14, 3, r=3.5))
    if fumee:
        m += [chemin(f"M {dx} -130 q -14 -24 0 -46 q 14 -24 0 -48", stroke="#dee2e6", sw=6, opacity=0.9) for dx in (-24, 4, 32)]
    return place(m, x, y, s)


def glacon_cube(x, y, s=1.0):
    return place([rect(-16, -16, 32, 32, "#e7f5ff", rx=6, stroke="#a5d8ff", stroke_width=3)], x, y, s, rot=12)


def bouilloire(x, y, s=1.0):
    m = [chemin("M -70 0 Q -80 -90 -40 -120 L 40 -120 Q 80 -90 70 0 Z", "#868e96"),
         chemin("M -60 -60 Q -110 -80 -116 -120", stroke="#868e96", sw=16),
         chemin("M -40 -130 Q 0 -170 40 -130", stroke="#343a40", sw=10), ellipse(0, -122, 42, 8, "#495057"),
         ellipse(-20, -70, 14, 30, "#fff", opacity=0.35)]
    return place(m, x, y, s)


def assiette_eau(x, y, s=1.0, cristaux=False, graine=1):
    m = [ellipse(0, 0, 150, 34, "#fff", stroke="#ced4da", stroke_width=4), ellipse(0, -2, 118, 24, "#f1f3f5")]
    if cristaux:
        rnd = random.Random(graine)
        for _ in range(26):
            cx, cy = rnd.uniform(-100, 100), rnd.uniform(-14, 12)
            m.append(place(rect(-6, -6, 12, 12, "#fff", stroke="#a5d8ff", stroke_width=2), cx, cy, rnd.uniform(0.7, 1.4), rot=rnd.uniform(0, 45)))
        m.append(paillettes(60, -40, 0.8, "#74c0fc"))
    else:
        m.append(ellipse(0, -2, 110, 20, "#a5d8ff", opacity=0.8))
    return place(m, x, y, s)


def calendrier(x, y, jour="3"):
    return g([rect(x - 50, y - 60, 100, 110, "#fff", rx=8, stroke="#adb5bd", stroke_width=3), rect(x - 50, y - 60, 100, 30, "#fa5252", rx=8),
              texte(x, y + 34, jour, 56, ENCRE), texte(x, y - 38, "jours", 20, "#fff")])


def entonnoir(x, y, s=1.0):
    """Entonnoir avec filtre ; (x, y) = bout du goulot."""
    m = [rect(-10, -60, 20, 60, "#adb5bd"),
         poly([(-110, -200), (110, -200), (10, -60), (-10, -60)], "#ced4da", opacity=0.9),
         poly([(-96, -196), (96, -196), (0, -76)], "#fff"),
         tas(0, -90, 40, 16, SABLE), grains(-30, -120, 30, -96, 18, 7, SABLE, 4, "#c99a2e")]
    return place(m, x, y, s)


def saunier(x, y, s=1.0, **k):
    rateau = g([trait(70, -150, 150, 20, "#8d5524", 8), trait(110, 20, 190, 20, "#8d5524", 10)])
    return personne(x, y, s, **{**dict(peau="brune", cheveux="noir", coiffure="courts", habit="#1971c2", robe=False, jambes="#495057",
                                     bras="tient", objet=rateau), **k})


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cuisine(S, 520)
    plan_travail(S, 600)
    S.add(pichet(400, 600, 1.2, 0.7))
    S.add(sucrier(620, 600, 0.9), morceau_sucre(560, 588), morceau_sucre(540, 588, rot=20))
    S.add(pistache(200, 790, 1.3, expr="surpris", bras="joues", regard=(1, -1)))
    S.add(texte(560, 320, "?", 160, "#20c997", contour="#fff", rot=10))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(morceau_sucre(300, 120, 1.6, rot=15))
    S.add(pistache(170, 264, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(pichet(400, 600, 1.1, 0.75), citron(560, 580), citron(600, 586, rot=30), sucrier(690, 600, 0.8))
    S.add(cuillere(330, 380, 1.0, rot=-140, sucre=True))
    S.add(pistache(180, 790, 1.15, expr="content", bras="tient", regard=(1, 0)))
    S.add(papi(680, 800, 1.0, expr="sourire", bras="montre", flip=True))
    return S


def p02():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(pichet(400, 600, 1.1, 0.75))
    S.add(cuillere(400, 470, 1.0, rot=-15))
    S.add(chemin("M 320 520 Q 400 560 480 520", stroke="#4dabf7", sw=5, opacity=0.7), chemin("M 330 540 Q 400 500 470 540", stroke="#4dabf7", sw=5, opacity=0.7))
    S.add(pistache(170, 790, 1.15, expr="bouche_bee", bras="joues", regard=(1, -1)))
    S.add(bulle(560, 200, 380, 90, "Il a disparu !", 44, pointe=(260, 470)))
    return S


def p03():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(verre(250, 600, 100, 140, niveau=0.75, couleur_contenu=EAU))
    S.add(pistache(130, 790, 1.0, expr="miam", bras="bouche"))
    # loupe géante : les petits morceaux de sucre entre les gouttes d'eau
    S.add(cercle(560, 330, 190, "#e7f5ff", stroke="#495057", stroke_width=14))
    S.add(grains(400, 180, 720, 480, 70, 5, "#74c0fc", 9, "#4dabf7"))
    S.add(grains(420, 200, 700, 460, 28, 9, "#fff", 7, "#495057"))
    S.add(cercle(560, 330, 190, "none", stroke="#495057", stroke_width=14))
    S.add(trait(420, 470, 340, 560, "#495057", 22))
    S.add(texte(540, 700, "gouttes d'eau", 34, "#1971c2"), texte(540, 745, "et miettes de sucre", 34, "#495057"))
    return S


def p04():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(verre(260, 600, 130, 180, niveau=0.75, couleur_contenu=EAU))
    S.add(verre(540, 600, 130, 180, niveau=0.75, couleur_contenu="#e3d7a8", contenu=g([tas(0, -8, 50, 16), grains(-40, -26, 40, -10, 20, 4, SABLE, 4, "#c99a2e")])))
    S.add(texte(260, 380, "sucre", 40, "#1971c2"), texte(540, 380, "sable", 40, "#c99a2e"))
    S.add(texte(260, 680, "invisible", 34, ENCRE), texte(540, 680, "au fond !", 34, ENCRE))
    S.add(pistache(700, 800, 0.8, expr="concentre", bras="pense", flip=True))
    return S


def p05():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(pot_sel(110, 600, 0.9))
    S.add(verre(260, 600, 130, 180, niveau=0.75, couleur_contenu=EAU))
    S.add(verre(530, 600, 130, 180, niveau=0.75, couleur_contenu=EAU,
                contenu=chemin("M -59 -135 L 59 -135 L 58 -110 L -58 -110 Z", HUILE, opacity=0.95)))
    S.add(texte(260, 380, "sel", 40, "#1971c2"), texte(530, 380, "huile", 40, "#e67700"))
    S.add(texte(260, 680, "il disparaît", 34, ENCRE), texte(530, 680, "elle flotte", 34, ENCRE))
    S.add(papi(700, 800, 0.95, expr="content", bras="montre", flip=True))
    return S


def p06():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(bouilloire(140, 600, 0.9))
    S.add(tasse_fumante(330, 600, 1.0), texte(330, 380, "chaud", 40, "#e03131"))
    S.add(tasse_fumante(560, 600, 1.0, "#74c0fc", fumee=False, depot=True), glacon_cube(540, 500), texte(560, 380, "froid", 40, "#1971c2"))
    S.add(texte(300, 690, "plus vite !", 34, ENCRE), texte(600, 690, "tout lentement…", 34, ENCRE))
    return S


def p07():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(verre(400, 600, 140, 200, niveau=0.75, couleur_contenu=EAU,
                contenu=g([tas(0, -8, 56, 20, "#fff"), grains(-46, -30, 46, -10, 30, 6, "#fff", 4)])))
    S.add(sucrier(620, 600, 0.8), cuillere(430, 330, 1.0, rot=-160, sucre=True))
    S.add(pistache(170, 790, 1.1, expr="oups", bras="tient", regard=(1, 0)))
    S.add(texte(300, 170, "9, 10 cuillères…", 44, "#20c997", contour="#fff"))
    S.add(texte(500, 700, "Ça ne disparaît plus !", 38, ENCRE))
    return S


def p08():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", 600)
    S.add(rect(140, 80, 520, 420, "#a5d8ff"), soleil(560, 170, 50))
    S.add(rect(130, 70, 540, 440, "none", stroke="#fff", stroke_width=20))
    S.add(rect(100, 500, 600, 30, "#ced4da"))
    S.add(assiette_eau(400, 480, 1.1))
    S.add(g([trait(470 - k * 50, 230 + k * 30, 430 - k * 50, 420, "#fcc419", 4, opacity=0.6) for k in range(3)]))
    S.add(pistache(220, 790, 1.0, expr="content", bras="montre", regard=(1, -1)))
    S.add(papi(600, 800, 1.0, expr="sourire", bras="pense", flip=True))
    return S


def p09():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", 600)
    S.add(rect(140, 80, 520, 420, "#a5d8ff"), soleil(560, 170, 50))
    S.add(rect(130, 70, 540, 440, "none", stroke="#fff", stroke_width=20))
    S.add(rect(100, 500, 600, 30, "#ced4da"))
    S.add(assiette_eau(400, 480, 1.1, cristaux=True))
    S.add(calendrier(230, 230))
    S.add(pistache(400, 790, 1.15, expr="bouche_bee", bras="haut"))
    S.add(texte(640, 660, "Du sel !", 60, "#1971c2", contour="#fff"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 100, 50))
    S.add(rect(0, 260, 800, 80, "#4dabf7"), rect(0, 340, 800, 460, "#d9c7a7"))
    for k, (x, y) in enumerate([(30, 380), (290, 380), (550, 380), (30, 560), (290, 560), (550, 560)]):
        S.add(rect(x, y, 220, 140, "#a5d8ff" if k % 2 else "#d0ebff", stroke="#b39a74", stroke_width=10))
    for x in (130, 190, 640):
        S.add(poly([(x - 50, 365), (x, 300), (x + 50, 365)], "#fff", stroke="#dee2e6", stroke_width=3))
    S.add(saunier(420, 790, 1.0, expr="content"))
    S.add(texte(400, 230, "Les marais salants", 44, "#1971c2", contour="#fff"))
    return S


def p11():
    S = Scene()
    cuisine(S)
    plan_travail(S)
    S.add(verre(400, 600, 150, 200, niveau=0.6, couleur_contenu=EAU))
    S.add(entonnoir(400, 440, 1.0))
    S.add(g([goutte(400, 470 + k * 20, 0.6, "#74c0fc") for k in range(2)]))
    S.add(texte(530, 240, "Le sable reste", 32, "#c99a2e", anchor="start"), fleche(520, 250, 450, 330, "#c99a2e", sw=5, tete=14))
    S.add(texte(560, 520, "le sel passe !", 34, "#1971c2", anchor="start"), fleche(550, 510, 470, 520, "#1971c2", sw=5, tete=14))
    S.add(pistache(130, 790, 1.0, expr="concentre", bras="pense", regard=(1, -1)))
    return S


def p12():
    S = Scene()
    cuisine(S)
    plan_travail(S, 640)
    S.add(pichet(400, 640, 0.9, 0.5, "#fff3bf"), citron(520, 620))
    S.add(pistache(170, 800, 1.05, expr="rire", bras="tient", objet=verre(68, -130, 60, 80, niveau=0.7, couleur_contenu="#fff3bf")))
    S.add(ami(420, 800, 0.95, expr="rire", bras="tient", objet=verre(68, -130, 60, 80, niveau=0.7, couleur_contenu="#fff3bf")))
    S.add(papi(650, 800, 1.05, expr="rire", bras="tient", flip=True, objet=verre(68, -130, 60, 80, niveau=0.7, couleur_contenu="#fff3bf")))
    S.add(texte(400, 300, "Santé !", 80, "#20c997", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pistache-seule.svg", vignette),
    ("01-la-limonade.svg", p01), ("02-disparu.svg", p02), ("03-c-est-sucre.svg", p03), ("04-le-sable.svg", p04),
    ("05-sel-et-huile.svg", p05), ("06-chaud-froid.svg", p06), ("07-trop-de-sucre.svg", p07), ("08-au-soleil.svg", p08),
    ("09-les-cristaux.svg", p09), ("10-marais-salants.svg", p10), ("11-le-filtre.svg", p11), ("12-sante.svg", p12),
]
