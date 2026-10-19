"""Pourquoi le Soleil et la Lune vivent dans le ciel — d'après un conte efik du Nigéria.

Autrefois, le Soleil et sa femme la Lune habitaient sur la Terre. Le
meilleur ami du Soleil était l'Eau. Le Soleil allait souvent la voir,
mais l'Eau ne venait jamais : « Ta maison est trop petite pour moi et
pour tout mon peuple. » Alors le Soleil et la Lune construisent une maison
immense. L'Eau arrive, avec les poissons, les crabes et tous les animaux
de l'eau : « Puis-je entrer ? » « Entre ! » L'eau monte aux genoux, à la
taille, jusqu'au toit. Le Soleil et la Lune grimpent sur le toit… puis,
quand l'eau le recouvre, ils montent dans le ciel. Ils y sont restés.

Plans : 1 large (le village) · 2 moyen (chez l'Eau) · 3 moyen (« trop
petite ») · 4 large (on construit) · 5 moyen (« Puis-je entrer ? ») · 6
gros plan (l'eau aux genoux) · 7 large (sur le toit) · 8 moyen (dans le
ciel) · 9 large (depuis ce jour).
"""
from contes import *
from base import _assombrir

ID = "soleil-lune-eau"

OR_ = "#fab005"


def rayons_dos(c="#ffd43b"):
    """Couronne de rayons derrière la tête du Soleil (derriere=)."""
    m = [cercle(0, -150, 120, radial([(0.5, c, 0.6), (1, c, 0)]))]
    for k in range(14):
        a = k * math.pi / 7
        m.append(poly([(math.cos(a - 0.12) * 80, -150 + math.sin(a - 0.12) * 80), (math.cos(a) * 128, -150 + math.sin(a) * 128),
                       (math.cos(a + 0.12) * 80, -150 + math.sin(a + 0.12) * 80)], c))
    return g(m)


def croissant_tete(c="#e7f5ff"):
    """Croissant de lune posé sur la tête de la Lune (coiffe)."""
    return g([chemin("M -40 -236 A 44 44 0 1 0 40 -236 A 36 36 0 1 1 -40 -236 Z", c, stroke="#a5d8ff", sw=2),
              cercle(-50, -210, 4, "#fff"), cercle(52, -214, 3, "#fff")])


SOLEIL = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit=OR_, robe=False, jambes="#e8590c", ceinture="#e8590c",
              carrure="ronde", nez="rond", derriere=rayons_dos())
LUNE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="tresses", habit="#d0ebff", robe=True, ceinture="#74c0fc", yeux="cils",
            nez="petit", coiffe=croissant_tete(), derriere=g([cercle(0, -150, 110, radial([(0.5, "#e7f5ff", 0.6), (1, "#e7f5ff", 0)]))]))
EAU = dict(stature="adulte", peau="#74c0fc", cheveux="#1c7ed6", coiffure="tres_longs", habit="#339af0", robe=True, ceinture="#d0ebff",
           nez="petit", yeux="cils", carrure="ronde")
VOISINS = [dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#2f9e44", robe=False, jambes="#495057"),
           dict(stature="ancien", peau="foncee", cheveux="blanc", coiffure="chignon", habit="#e64980", robe=True)]


def maison_terre(x, y, s=1.0, w=180, h=150, toit_h=120, c="#c9844a"):
    """Maison de terre aux murs décorés, toit de chaume ; (x, y) = milieu du seuil."""
    toit = poly([(-w - 40, -h), (0, -h - toit_h), (w + 40, -h)], "#000")
    m = [rect(-w, -h, 2 * w, h, terrain(c)),
         chemin(" ".join(f"M {-w + 10 + k * 40} {-h + 30} l 20 20 l 20 -20" for k in range(int(w / 20))), stroke=_assombrir(c, 0.75), sw=4),
         rect(-34, -110, 68, 110, "#5c3d24", rx=30), rect(-w + 30, -100, 46, 40, "#5c3d24", rx=10), rect(w - 76, -100, 46, 40, "#5c3d24", rx=10),
         poly([(-w - 40, -h), (0, -h - toit_h), (w + 40, -h)], volume("#d9b46a", 0.3, 0.8)), chaume(-w - 40, -h - toit_h, 2 * w + 80, toit_h, "#d9b46a", forme=toit)]
    return place(m, x, y, s)


def niveau_eau(S, y, vagues=True, poissons=0, graine=1):
    """L'eau qui monte, transparente, jusqu'à la hauteur y."""
    S.add(rect(0, y, 800, 800 - y, lineaire([(0, "#4dabf7", 0.7), (1, "#1971c2", 0.85)])))
    if vagues:
        S.add(chemin(f"M 0 {y} " + " ".join(f"q 25 -14 50 0" for _ in range(17)), stroke="#d0ebff", sw=4))
    r = random.Random(graine)
    for k in range(poissons):
        S.add(poisson(r.uniform(60, 740), r.uniform(y + 40, 780), r.uniform(0.35, 0.55), ("#ff922b", "#fcc419", "#f783ac", "#63e6be")[k % 4],
                      flip=k % 2 == 0))


def village(S, horizon=540, moment="jour"):
    if moment == "soir":
        ciel(S, "#ff922b", "#ffe8cc")
    else:
        ciel(S, "#74c0fc", "#fff9db")
    lointain(S, horizon, "#94d82d", 90, graine=2, opacite=0.45)
    for x in (80, 720):
        S.add(chemin(f"M {x} {horizon + 20} Q {x + 10} {horizon - 140} {x + 24} {horizon - 220}", stroke="#8d5524", sw=12))
        for a in (-150, -115, -80, -45, -10):
            S.add(place([chemin("M 0 0 Q 40 -24 90 10 Q 40 0 0 0 Z", "#2f9e44", stroke="#2b8a3e", sw=2)], x + 24, horizon - 220, 1.0, rot=a + 90))
    sol(S, horizon, "#e9b872", bosse=10)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(maison_terre(400, 760, 1.0, w=220, h=170))
    niveau_eau(S, 640, poissons=5, graine=2)
    S.add(personne(320, 540, 1.15, expr="rire", bras="ouverts", regard=(1, 0), **SOLEIL))
    S.add(personne(490, 540, 1.1, expr="surpris", bras="surprise", flip=True, regard=(-1, 0), **LUNE))
    S.cachette(560, 120, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(personne(140, 262, 0.75, expr="content", bras="main", regard=(1, 0), **SOLEIL))
    S.add(personne(260, 262, 0.72, expr="content", bras="main", flip=True, regard=(-1, 0), **LUNE))
    return S


def p01():
    """Plan large : autrefois, le Soleil et la Lune vivaient sur la Terre, dans une petite maison de terre, parmi les gens du village."""
    S = Scene()
    village(S, 540)
    S.add(maison_terre(400, 640, 0.6))
    S.add(personne(300, 780, 1.15, expr="content", bras="main", regard=(1, 0), **SOLEIL))
    S.add(personne(450, 780, 1.1, expr="content", bras="main", flip=True, regard=(-1, 0), **LUNE))
    S.add(personne(640, 790, 0.95, expr="rire", bras="coucou", flip=True, regard=(-1, 0), **VOISINS[0]))
    S.add(personne(140, 790, 1.0, expr="sourire", bras="dos", regard=(1, 0), **VOISINS[1]))
    S.cachette(740, 790)
    return S


def p02():
    """Plan moyen : au bord du fleuve, le Soleil rend visite à son amie l'Eau, aux longs cheveux bleus : « Pourquoi ne viens-tu jamais chez nous ? »"""
    S = Scene()
    village(S, 520)
    S.add(chemin("M 380 520 Q 520 600 460 800 L 800 800 L 800 520 Z", lineaire([(0, "#74c0fc"), (1, "#1971c2")])))
    S.add(personne(600, 790, 1.35, expr="sourire", bras="mains_jointes", flip=True, regard=(-1, 0), **EAU))
    S.add(poisson(720, 700, 0.5, "#fcc419", flip=True), crabe(500, 780, 0.5))
    S.add(personne(230, 790, 1.35, expr="sourire", bras="tend", regard=(1, 0), **SOLEIL))
    S.add(bulle(330, 150, 520, 100, "Pourquoi ne viens-tu\njamais chez nous ?", 32, pointe=(250, 330)))
    S.cachette(40, 790)
    return S


def p03():
    """Plan moyen : l'Eau répond : « Ta maison est trop petite pour moi et tout mon peuple ! » ; poissons et crabes acquiescent."""
    S = Scene()
    village(S, 520)
    S.add(chemin("M 300 520 Q 440 600 380 800 L 800 800 L 800 520 Z", lineaire([(0, "#74c0fc"), (1, "#1971c2")])))
    S.add(personne(560, 790, 1.5, expr="rire", bras="ouverts", flip=True, regard=(-1, 0), **EAU))
    r = random.Random(3)
    for k in range(6):
        S.add(poisson(r.uniform(420, 760), r.uniform(600, 770), 0.45, ("#ff922b", "#fcc419", "#f783ac")[k % 3], flip=True))
    S.add(crabe(430, 780, 0.55), crabe(740, 790, 0.45))
    S.add(personne(160, 790, 1.2, expr="surpris", bras="gratte", regard=(1, 0), **SOLEIL))
    S.add(bulle(420, 150, 600, 100, "Ta maison est trop petite\npour moi et tout mon peuple !", 30, pointe=(540, 330)))
    S.cachette(80, 70, "air")
    return S


def p04():
    """Plan large : le Soleil et la Lune construisent une maison immense ; on porte la terre, on monte les murs, tout le village aide."""
    S = Scene()
    village(S, 520)
    S.add(rect(170, 520, 520, 200, terrain("#c9844a")), rect(170, 500, 520, 24, "#a0693a"))
    S.add(echelle(640, 720, 0.8, h=300, rot=10))
    S.add(personne(330, 500, 0.9, expr="concentre", bras="porte", objet=rect(-40, -100, 80, 40, terrain("#c9844a"), rx=8), **SOLEIL))
    S.add(personne(160, 790, 1.15, expr="rire", bras="porte", objet=g([ellipse(0, -74, 46, 30, "#a0693a")]), regard=(1, 0), **LUNE))
    S.add(personne(560, 790, 1.0, expr="content", bras="ramasse", regard=(-1, 0.5), flip=True, **VOISINS[0]))
    S.cachette(740, 790)
    return S


def p05():
    """Plan moyen : la grande maison est finie ; devant la porte, l'Eau arrive avec ses poissons : « Puis-je entrer ? » « Entre ! »"""
    S = Scene()
    village(S, 540, "soir")
    S.add(maison_terre(400, 700, 1.0, w=300, h=200, toit_h=160))
    S.add(chemin("M 800 640 Q 640 700 600 800 L 800 800 Z", "#339af0", opacity=0.85))
    S.add(personne(620, 790, 1.25, expr="sourire", bras="tend", flip=True, regard=(-1, 0), **EAU))
    S.add(poisson(740, 720, 0.45, "#fcc419", flip=True), poisson(700, 770, 0.4, "#ff922b", flip=True))
    S.add(personne(230, 790, 1.25, expr="rire", bras="ouverts", regard=(1, 0), **SOLEIL))
    S.add(bulle(560, 130, 340, 80, "Puis-je entrer ?", 32, pointe=(600, 470)))
    S.add(bulle(200, 230, 220, 80, "Entre !", 34, pointe=(230, 470)))
    S.cachette(40, 790)
    return S


def p06():
    """Gros plan : dans la maison, l'eau monte jusqu'aux genoux du Soleil et de la Lune ; des poissons nagent entre leurs jambes : « Encore ? Entre ! »"""
    S = Scene()
    interieur(S, "#e8b27a", "#a0693a", 560, plinthe="#7c4a1e")
    S.add(personne(320, 790, 1.4, expr="surpris", bras="surprise", regard=(1, 0), **SOLEIL))
    S.add(personne(500, 790, 1.35, expr="inquiet", bras="mains_jointes", flip=True, regard=(-1, 0), **LUNE))
    niveau_eau(S, 670, poissons=6, graine=4)
    S.camera(1.3, 410, 560)
    S.dessus(bulle(400, 100, 560, 90, "Encore du monde ? Entre…", 32))
    S.cachette(150, 470, "air")
    return S


def p07():
    """Plan large : l'eau arrive en haut des murs ; le Soleil et la Lune ont grimpé sur le toit de chaume ; poissons et crabes nagent tout autour."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(maison_terre(400, 800, 1.0, w=300, h=200, toit_h=160))
    niveau_eau(S, 600, poissons=7, graine=7)
    S.add(personne(340, 520, 0.95, expr="oups", bras="haut", regard=(0, -1), **SOLEIL))
    S.add(personne(460, 520, 0.9, expr="surpris", bras="tend", flip=True, regard=(-1, 0), **LUNE))
    S.add(personne(640, 790, 1.0, expr="sourire", bras="ouverts", flip=True, regard=(-1, -1), **EAU))
    S.add(texte(400, 140, "Glou, glou, glou !", 52, "#1864ab", contour="#fff"))
    S.cachette(110, 260, "air")
    return S


def p08():
    """Plan large : l'eau recouvre tout le toit ; le Soleil et la Lune s'envolent haut dans le ciel, en se tenant la main."""
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    niveau_eau(S, 540, poissons=8, graine=8)
    S.add(personne(320, 380, 0.9, expr="rire", bras="main", regard=(1, 0), rot=-12, **SOLEIL))
    S.add(personne(470, 330, 0.85, expr="joie", bras="main", flip=True, regard=(-1, 0), rot=12, **LUNE))
    S.add(mouvement(330, 470, 1.4, rot=90), mouvement(470, 420, 1.4, rot=90))
    S.camera(1.35, 400, 380)
    S.dessus(texte(400, 90, "Hop, dans le ciel !", 52, "#e8590c", contour="#fff"))
    S.cachette(644, 491, "air")
    return S


def p09():
    """Plan large : depuis, le Soleil brille dans le ciel du jour et la Lune dans celui de la nuit ; en bas, l'Eau couvre la mer, et les gens les saluent."""
    S = Scene()
    S.add(rect(0, 0, 400, 560, lineaire([(0, "#4dabf7"), (1, "#fff3bf")])), rect(400, 0, 400, 560, lineaire([(0, "#1c2a52"), (1, "#5c7cfa")])))
    S.ambiance("jour")
    etoiles(S, 18, 4, (420, 20, 780, 420))
    S.add(soleil(200, 180, 70, visage=True))
    S.add(lune(600, 180, 60, visage=True))
    S.add(rect(0, 520, 800, 120, lineaire([(0, "#339af0"), (1, "#1864ab")])))
    for k in range(6):
        S.add(chemin(f"M {k * 140 + 20} {560 + (k % 2) * 30} q 20 -8 40 0 t 40 0", stroke="#d0ebff", sw=3))
    sol(S, 640, "#e9b872", bosse=8)
    S.add(personne(300, 790, 1.1, expr="rire", bras="coucou", regard=(-1, -1), **VOISINS[0]))
    S.add(personne(500, 790, 1.1, expr="content", bras="salut", flip=True, regard=(1, -1), **VOISINS[1]))
    S.cachette(740, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("soleil-et-lune.svg", vignette),
    ("01-sur-la-terre.svg", p01), ("02-chez-l-eau.svg", p02), ("03-trop-petite.svg", p03),
    ("04-on-construit.svg", p04), ("05-puis-je-entrer.svg", p05), ("06-aux-genoux.svg", p06),
    ("07-sur-le-toit.svg", p07), ("08-dans-le-ciel.svg", p08), ("09-depuis-ce-jour.svg", p09),
]
