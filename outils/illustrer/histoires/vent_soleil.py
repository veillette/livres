"""Le Vent et le Soleil — d'après Ésope et La Fontaine (« Phébus et Borée »).

Le Vent et le Soleil se disputent : lequel est le plus fort ? Un voyageur
passe, bien emmitouflé dans son manteau : celui qui le lui fera ôter aura
gagné. Le Vent souffle de toutes ses forces ; plus il souffle, plus le
voyageur serre son manteau. Le Soleil, lui, brille doucement ; il fait
chaud, et le voyageur ôte son manteau de lui-même. « Plus fait douceur que
violence. »

Plans : 1 large (la dispute) · 2 large (le voyageur) · 3 large (le Vent
souffle) · 4 gros plan (il serre son manteau) · 5 moyen (le Vent est
épuisé) · 6 large (le Soleil brille) · 7 moyen (il ôte son manteau) · 8
large (le Soleil a gagné).
"""
from fables import *
from base import _assombrir

ID = "vent-soleil"

VOYAGEUR = dict(stature="adulte", peau="doree", cheveux="brun", coiffure="courts", habit="#495057", robe=False, jambes="#795548",
                barbe="#4a2c17", carrure="ronde", nez="long")
MANTEAU = "#c92a2a"


def voyageur(x, y, s=1.6, manteau=True, serre=False, **k):
    d = dict(VOYAGEUR)
    if manteau:
        d["cape"] = MANTEAU
        d["habit"] = MANTEAU
    k.setdefault("bras", "croises" if serre else "bas")
    return personne(x, y, s, **{**d, **k})


def vent(x, y, s=1.0, expr="souffle", flip=False, joues=True):
    """Le Vent : un gros nuage gris qui gonfle les joues ; (x, y) = centre."""
    m = [nuage(0, 0, 1.6, "#dee2e6", ombre="#adb5bd")]
    m += [cercle(-30, -10, 9, ENCRE), cercle(30, -10, 9, ENCRE), cercle(-28, -13, 3, "#fff"), cercle(32, -13, 3, "#fff")]
    if expr == "souffle":
        m += [cercle(-56, 18, 20, "#ffc9c9", opacity=0.7), cercle(56, 18, 20, "#ffc9c9", opacity=0.7), ellipse(0, 26, 12, 14, ENCRE),
              trait(-44, -32, -18, -26, ENCRE, 4), trait(44, -32, 18, -26, ENCRE, 4)]
    elif expr == "fatigue":
        m += [chemin("M -14 30 Q 0 22 14 30", stroke=ENCRE, sw=4), ellipse(60, -30, 6, 10, "#74c0fc")]
    elif expr == "boude":
        m += [chemin("M -14 30 Q 0 24 14 30", stroke=ENCRE, sw=4), trait(-44, -28, -18, -32, ENCRE, 4), trait(44, -28, 18, -32, ENCRE, 4)]
    else:
        m += [chemin("M -16 24 Q 0 36 16 24", stroke=ENCRE, sw=4)]
    return place(m, x, y, s, flip=flip) + occuper(x - 150 * s, y - 90 * s, x + 150 * s, y + 70 * s)


def souffle(S, x, y, s=1.0, nb=5):
    for k in range(nb):
        S.add(chemin(f"M {x} {y + k * 40 * s} q {80 * s} -20 {160 * s} 0 q {80 * s} 20 {160 * s} 0 q {40 * s} -10 {80 * s} 0", stroke="#fff",
                     sw=6 * s, opacity=0.85))


def soleil_visage(x, y, r=70, expr="sourire"):
    m = [soleil(0, 0, r)]
    m += [cercle(-r * 0.3, -r * 0.1, r * 0.1, ENCRE), cercle(r * 0.3, -r * 0.1, r * 0.1, ENCRE),
          cercle(-r * 0.5, r * 0.2, r * 0.14, "#ff922b", opacity=0.6), cercle(r * 0.5, r * 0.2, r * 0.14, "#ff922b", opacity=0.6)]
    if expr == "rire":
        m.append(chemin(f"M {-r * 0.3} {r * 0.25} Q 0 {r * 0.6} {r * 0.3} {r * 0.25} Z", "#c92a2a"))
    else:
        m.append(chemin(f"M {-r * 0.3} {r * 0.25} Q 0 {r * 0.5} {r * 0.3} {r * 0.25}", stroke=ENCRE, sw=4))
    return place(m, x, y)


def route(S, horizon=520, vent_fort=False, chaud=False):
    ciel(S, "#ffd8a8" if chaud else ("#adb5bd" if vent_fort else "#74c0fc"), "#fff9db" if chaud else "#e7f5ff")
    collines(S, horizon, "#b2f2bb", graine=3)
    sol(S, horizon + 40, "#8ce99a")
    S.add(chemin("M 0 780 Q 300 700 520 640 Q 680 600 800 600 L 800 640 Q 680 650 540 690 Q 320 760 0 800 Z", "#f3d9a4"))


def arbre_plie(x, y, s=1.0, rot=0):
    return place([rect(-14, -200, 28, 200, cylindre("#7c4a1e", 0.3, 0.75)),
                  place([cercle(0, -240, 90, volume("#40c057", 0.35, 0.8)), cercle(-60, -200, 60, volume("#51cf66", 0.35, 0.8))], 0, 0, rot=rot)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    route(S)
    S.add(soleil_visage(620, 160, 80))
    S.add(vent(200, 180, 0.9, expr="souffle"))
    S.add(voyageur(400, 790, 1.75, expr="inquiet", serre=True))
    S.cachette(740, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(soleil_visage(120, 130, 60), vent(290, 130, 0.5, expr="sourire"))
    return S


def p01():
    """Plan large : dans le ciel, le Vent et le Soleil se disputent : « C'est moi le plus fort ! » « Non, c'est moi ! »"""
    S = Scene()
    route(S)
    S.add(vent(230, 360, 1.4, expr="boude"))
    S.add(soleil_visage(590, 340, 110))
    S.add(bulle(230, 140, 340, 90, "C'est moi le plus fort !", 30, pointe=(230, 250)))
    S.add(bulle(590, 140, 280, 90, "Non, c'est moi !", 32, pointe=(590, 210)))
    return S


def p02():
    """Plan large : un voyageur passe sur la route, bien emmitouflé dans son grand manteau rouge."""
    S = Scene()
    route(S)
    S.add(vent(200, 180, 0.7, expr="sourire"), soleil_visage(630, 160, 60))
    S.add(voyageur(420, 780, 1.6, expr="content", bras="marche", pas="marche", regard=(1, 0)))
    S.add(bulle(400, 330, 520, 110, "Celui qui lui fera enlever son\nmanteau sera le plus fort !", 30, pointe=(250, 220)))
    return S


def p03():
    """Plan large : le Vent souffle de toutes ses forces : Fffffou ! les arbres plient, le chapeau s'envole."""
    S = Scene()
    route(S, vent_fort=True)
    S.add(vent(170, 200, 1.0, expr="souffle"))
    souffle(S, 280, 200, 1.0, 6)
    S.add(arbre_plie(680, 640, 0.9, rot=20))
    S.add(voyageur(480, 780, 1.55, expr="inquiet", serre=True, penche=10))
    S.add(place([ellipse(0, 0, 40, 12, "#795548"), ellipse(0, -10, 24, 16, "#795548")], 680, 300, rot=30))
    S.add(texte(400, 90, "Fffffou !", 64, "#495057", contour="#fff"))
    return S


def p04():
    """Gros plan : plus le Vent souffle, plus le voyageur serre son manteau contre lui."""
    S = Scene()
    route(S, vent_fort=True)
    souffle(S, 0, 300, 1.2, 6)
    S.add(voyageur(400, 900, 2.3, expr="fache", serre=True, penche=8))
    S.camera(1.05, 400, 520)
    S.dessus(texte(400, 100, "Brrr ! Je garde mon manteau !", 40, MANTEAU, contour="#fff"))
    return S


def p05():
    """Plan moyen : le Vent, épuisé, n'a plus de souffle ; il abandonne : à toi, Soleil !"""
    S = Scene()
    route(S)
    S.add(vent(240, 300, 1.1, expr="fatigue"))
    S.add(soleil_visage(620, 200, 80))
    S.add(voyageur(560, 790, 1.5, expr="content", serre=True))
    S.add(bulle(260, 120, 360, 90, "Pfff… À toi, Soleil !", 34, pointe=(250, 220)))
    return S


def p06():
    """Plan large : le Soleil brille doucement ; il fait bon, puis chaud ; le voyageur s'éponge le front."""
    S = Scene()
    route(S, chaud=True)
    S.add(soleil_visage(600, 170, 100, expr="rire"))
    for k in range(5):
        S.add(chemin(f"M {200 + k * 100} 380 q 10 -20 0 -40 q -10 -20 0 -40", stroke="#ffa94d", sw=4, opacity=0.6))
    S.add(voyageur(420, 790, 1.6, expr="souffle", bras="tete", manteau=True))
    S.add(texte(260, 160, "Qu'il fait chaud !", 44, "#e8590c", contour="#fff"))
    return S


def p07():
    """Plan moyen : le voyageur ôte son manteau et s'assoit à l'ombre d'un arbre."""
    S = Scene()
    route(S, chaud=True)
    S.add(soleil_visage(660, 140, 70, expr="rire"))
    S.add(arbre(240, 700, 1.4, "#51cf66", "#40c057"))
    S.add(voyageur(380, 790, 1.6, expr="content", manteau=False, bras="hanches", regard=(1, 0)))
    S.add(chemin("M 500 790 Q 520 740 580 736 Q 650 734 670 780 Q 600 800 500 790 Z", volume(MANTEAU, 0.3, 0.8)),
          chemin("M 560 740 Q 580 760 610 742", stroke=_assombrir(MANTEAU, 0.75), sw=4))
    return S


def p08():
    """Plan large : le Soleil a gagné, sans forcer ; le Vent boude dans son coin."""
    S = Scene()
    route(S)
    S.add(soleil_visage(560, 200, 90, expr="rire"))
    S.add(vent(160, 140, 0.6, expr="boude"))
    S.add(voyageur(400, 790, 1.5, expr="rire", manteau=False, bras="salut", regard=(0.5, -1)))
    S.add(texte(560, 360, "Bravo, Soleil !", 46, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vent-soleil-seuls.svg", vignette),
    ("01-la-dispute.svg", p01), ("02-le-voyageur.svg", p02), ("03-fffou.svg", p03),
    ("04-le-manteau.svg", p04), ("05-a-toi-soleil.svg", p05), ("06-il-fait-chaud.svg", p06),
    ("07-a-l-ombre.svg", p07), ("08-le-soleil-a-gagne.svg", p08),
]
