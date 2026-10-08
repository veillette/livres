"""Le jour où j'ai perdu ma dent — la première dent de lait qui tombe.

Sofia sent sa dent de devant bouger ; Maman lui explique qu'une dent
définitive pousse dessous. La dent tombe dans une pomme, à la récréation.
Le soir, elle la glisse sous l'oreiller, et la petite souris laisse une pièce.
"""
from base import *
from objets import *
from fantastique import personne
from sciences import fleche

ID = "dent-perdue"
SOFIA = dict(peau="rosee", cheveux="chatain", coiffure="tresses", habit="#0ca678", robe=False, jambes="#364fc7")
MAMAN = dict(peau="rosee", cheveux="chatain", coiffure="longs", habit="#f76707", robe=True)


def sofia(x=0, y=0, s=1.0, dents=None, **k):
    """Sofia ; dents = "bouge" (une dent penchée), "trou" (il en manque une) ou None."""
    m = [personne(x, y, s, **{**SOFIA, **k})]
    if dents:
        m.append(place(bouche_dents(dents), x, y - 121 * s, s, flip=k.get("flip", False)))
    return g(m)


def maman(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def bouche_dents(etat="trou"):
    """Grand sourire avec les dents du haut, centré sur la bouche."""
    m = [chemin("M -20 -4 Q 0 -8 20 -4 Q 18 20 0 22 Q -18 20 -20 -4 Z", "#c92a2a", stroke=ENCRE, sw=2.5)]
    for k, dx in enumerate((-12, -4, 4, 12)):
        if etat == "trou" and k == 1:
            continue
        rot = 14 if (etat == "bouge" and k == 1) else 0
        m.append(place(rect(-4, 0, 8, 10, "#ffffff", rx=1.5, stroke="#dee2e6", stroke_width=0.8), dx, -5, 1, rot=rot))
    return g(m)


def pomme_croquee(x, y, s=1.0, dent=True):
    m = [pomme(0, 0, 1.0)]
    m.append(chemin("M 26 -30 Q 12 -14 22 4 Q 8 14 26 28 L 50 30 L 50 -30 Z", "#fff9db"))
    if dent:
        m.append(rect(14, -6, 10, 13, "#ffffff", rx=3, stroke="#dee2e6", stroke_width=1.5))
    return place(m, x, y, s)


def piece(x, y, s=1.0):
    return place([cercle(0, 0, 22, "#fcc419", stroke="#f59f00", stroke_width=4), texte(0, 9, "1", 24, "#e67700")], x, y, s)


def petite_souris(x, y, s=0.45, **k):
    return perso("souris", x, y, s, **{**dict(habit="#e64980", acc=("noeud",), couleur_acc="#ffd43b"), **k})


def boite(x, y, s=1.0):
    return place([rect(-40, -40, 80, 40, "#e64980", rx=8), rect(-44, -48, 88, 14, "#f783ac", rx=6),
                  rect(-10, -48, 20, 48, "#ffd43b")], x, y, s)


def chambre(S, nuit_=True):
    if nuit_:
        interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    else:
        interieur(S, "#fff4e6", "#e8c39e", y=600, papier="#ffe8cc")


def lit_et_tete(S, tete, x=360, w=480, y=760, couette="#20c997", h_couette=680):
    S.add(lit(x, y, w, "#e5dbff", couette))
    cid = uid("c")
    S.add(el("clipPath", rect(0, 0, 800, h_couette + 20, "#000"), id=cid))
    S.add(g(tete, clip_path=f"url(#{cid})"))
    S.add(rect(x - w / 2 + 40, h_couette, w - 40, 70, couette, rx=18))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#c3fae8")
    for k in range(12):
        S.add(etoile5(60 + (k * 137) % 700, 260 + (k * 91) % 300, 12, "#ffffff", opacity=0.7))
    S.add(sofia(330, 780, 2.0, dents="trou", expr="rire", bras="montre", regard=(1, 0)))
    S.add(petite_souris(620, 760, 0.8, expr="content", bras="salut"))
    S.add(piece(640, 520, 1.3))
    S.cachette(730, 650, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(sofia(200, 330, 1.25, dents="trou", expr="rire", bras="salut"))
    return S


def p01():
    S = Scene()
    interieur(S, "#e3fafc", "#99e9f2", y=600, plinthe="#66d9e8")
    S.add(rect(460, 120, 260, 300, "#d0ebff", rx=24, stroke="#ffffff", stroke_width=12))
    cid = uid("c")
    S.add(el("clipPath", rect(460, 120, 260, 300, "#000", rx=24), id=cid))
    S.add(g(sofia(590, 480, 1.2, dents="bouge", expr="surpris", bras="bouche", regard=(-1, 0), flip=True), clip_path=f"url(#{cid})"))
    S.add(rect(470, 130, 60, 280, "#ffffff", opacity=0.25, rx=20))
    S.add(sofia(260, 770, 1.4, dents="bouge", expr="surpris", bras="bouche", regard=(1, 0)))
    S.add(texte(150, 220, "gling…", 50, "#0ca678", contour="#fff", rot=-8), texte(330, 160, "glang !", 50, "#0ca678", contour="#fff", rot=6))
    return S


def p02():
    S = Scene()
    chambre(S, nuit_=False)
    S.add(fenetre(560, 100, 180, 170, "#a5d8ff", rideaux="#ffa94d"))
    S.add(table(400, 760, 560, 180, "#c68642"))
    S.add(sofia(400, 680, 1.25, expr="inquiet", bras="bouche", regard=(0, 0)))
    S.add(rect(400 - 280, 760 - 198, 560, 30, "#c68642", rx=6))
    S.add(bol(560, 556, 0.8), assiette(260, 556, 0.8))
    S.add(rect(230, 520, 60, 30, "#e9b872", rx=8))
    S.add(texte(620, 380, "tout doux…", 40, "#0ca678", contour="#fff"))
    return S


def p03():
    S = Scene()
    fond(S, "#fff0f6")
    # coupe de la gencive : la dent de lait au-dessus, la grande dent qui pousse dessous
    cx, cy = 400, 400
    S.add(ellipse(cx, cy + 40, 260, 170, "#ffa8a8"))
    S.add(chemin(f"M {cx - 260} {cy - 60} Q {cx} {cy - 120} {cx + 260} {cy - 60} L {cx + 260} {cy - 200} L {cx - 260} {cy - 200} Z", "#fff0f6"))
    S.add(chemin(f"M {cx - 50} {cy - 210} L {cx + 50} {cy - 210} L {cx + 44} {cy - 70} Q {cx} {cy - 60} {cx - 44} {cy - 70} Z", "#ffffff", stroke="#dee2e6", sw=4))
    S.add(chemin(f"M {cx - 22} {cy - 70} L {cx - 10} {cy - 40} M {cx + 22} {cy - 70} L {cx + 10} {cy - 40}", stroke="#f8f9fa", sw=8))
    S.add(chemin(f"M {cx - 60} {cy + 10} L {cx + 60} {cy + 10} L {cx + 52} {cy + 160} Q {cx} {cy + 176} {cx - 52} {cy + 160} Z", "#f8f9fa", stroke="#ced4da", sw=4))
    S.add(fleche(cx + 150, cy + 120, cx + 150, cy - 20, "#c2255c", 8, 24))
    S.add(texte(cx, 120, "la dent de lait", 40, "#c2255c"))
    S.add(texte(340, 690, "la grande dent pousse !", 40, "#0ca678"))
    S.add(maman(700, 790, 0.95, expr="content", bras="montre", flip=True, regard=(-1, -1)))
    S.cachette(610, 70, "air")
    return S


def p04():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600, papier="#ffe8a3")
    S.add(rect(150, 90, 500, 240, "#2b8a3e", rx=10, stroke="#a0693a", stroke_width=14))
    S.add(texte(400, 200, "a b c", 60, "#ffffff", poids=500), texte(400, 280, "1 2 3", 50, "#ffffff", poids=500))
    S.add(personne(140, 770, 1.15, peau="foncee", cheveux="noir", coiffure="courts", habit="#fab005", robe=False, expr="bouche_bee", regard=(1, 0)))
    S.add(sofia(400, 780, 1.3, dents="bouge", expr="rire", bras="bouche"))
    S.add(personne(660, 770, 1.15, peau="doree", cheveux="noir", coiffure="queue", habit="#7048e8", robe=True, expr="surpris", flip=True, regard=(-1, 0)))
    S.add(bulle(560, 380, 260, 70, "Elle bouge !", 34, pointe=(470, 520)))
    S.cachette(70, 140, "air")
    return S


def p05():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(arbre(130, 600, 1.0, fruits="#fa5252"), arbre(690, 590, 0.8))
    S.add(rect(0, 590, 800, 210, "#ced4da"))
    S.add(sofia(380, 770, 1.4, dents="trou", expr="surpris", bras="tient", objet=pomme_croquee(68, -146, 0.9)))
    S.add(texte(600, 260, "Crac !", 80, "#e03131", contour="#fff", rot=8))
    return S


def p06():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 590, 800, 210, "#ced4da"))
    S.add(arbre(690, 590, 0.8))
    S.add(sofia(380, 780, 1.6, dents="trou", expr="rire", bras="hanches"))
    S.add(bulle(400, 110, 520, 90, "Ssssaucisssson !", 42, pointe=(360, 380)))
    for k in range(3):
        S.add(chemin(f"M {480 + k * 16} {470 - k * 8} q 30 -10 60 0", stroke="#4dabf7", sw=4, opacity=0.8 - k * 0.2))
    return S


def p07():
    S = Scene()
    interieur(S, "#fff9db", "#e8c39e", y=600, papier="#ffe8a3")
    S.add(rect(150, 90, 500, 240, "#2b8a3e", rx=10, stroke="#a0693a", stroke_width=14))
    maitresse = personne(560, 790, 1.5, peau="claire", cheveux="blond", coiffure="chignon", habit="#1971c2", robe=True,
                         expr="content", bras="donne", flip=True, acc=("lunettes",), regard=(-1, 1))
    S.add(maitresse)
    S.add(boite(434, 652, 0.9))
    S.add(sofia(270, 780, 1.3, dents="trou", expr="content", bras="donne", regard=(1, 0)))
    return S


def p08():
    S = Scene()
    chambre(S)
    S.add(fenetre(520, 100, 200, 180, "#1c2a52", "#e5dbff", nuit_=True))
    S.add(lit(490, 760, 480, "#e5dbff", "#20c997"))
    S.add(sofia(170, 770, 1.2, dents="trou", expr="content", bras="donne", regard=(1, 1)))
    S.add(rect(270, 636, 10, 13, "#ffffff", rx=3, stroke="#adb5bd", stroke_width=2))
    S.add(fleche(330, 560, 300, 610, "#ffd43b", 5, 14))
    return S


def p09():
    S = Scene()
    chambre(S)
    S.add(fenetre(520, 100, 200, 180, "#1c2a52", "#e5dbff", nuit_=True))
    lit_et_tete(S, sofia(230, 770, 0.95, expr="dort"), h_couette=670)
    S.add(cercle(330, 610, 90, "#ffe066", opacity=0.15))
    S.add(petite_souris(330, 640, 0.55, expr="content", bras="tient", objet=place([cercle(0, 0, 18, "#fcc419", stroke="#f59f00", stroke_width=4)], 68, -146)))
    S.add(rect(214, 578, 10, 13, "#ffffff", rx=3, stroke="#adb5bd", stroke_width=2))
    S.add(texte(500, 470, "chut…", 44, "#fff3bf", contour="#3b2a7a"))
    S.add(zzz(160, 470, 1.0, "#e5dbff"))
    S.cachette(70, 670, "air")
    return S


def p10():
    S = Scene()
    chambre(S, nuit_=False)
    S.add(fenetre(520, 100, 200, 180, "#a5d8ff", rideaux="#63e6be"))
    S.add(soleil(640, 160, 30, rayons=False))
    S.add(lit(360, 760, 480, "#e5dbff", "#20c997"))
    S.add(sofia(330, 760, 1.35, dents="trou", expr="rire", bras="haut"))
    S.add(piece(330 - 70 * 1.35, 760 - 165 * 1.35, 1.1))
    S.add(texte(600, 420, "Merci,", 48, "#0ca678", contour="#fff"), texte(600, 480, "petite souris !", 48, "#0ca678", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("sofia-seule.svg", vignette),
    ("01-elle-bouge.svg", p01), ("02-tout-doux.svg", p02), ("03-la-grande-dent.svg", p03),
    ("04-a-l-ecole.svg", p04), ("05-la-pomme.svg", p05), ("06-le-trou.svg", p06),
    ("07-la-petite-boite.svg", p07), ("08-sous-l-oreiller.svg", p08), ("09-la-petite-souris.svg", p09),
    ("10-merci.svg", p10),
]
