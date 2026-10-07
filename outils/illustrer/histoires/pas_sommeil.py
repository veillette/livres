"""Je n'ai pas sommeil ! — une histoire du soir à refrain.

Bao, le petit panda, répète à chaque étape du coucher qu'il n'a pas sommeil…
mais ses bâillements grandissent de page en page, jusqu'au dodo.
"""
from base import *
from objets import *

ID = "pas-sommeil"
PYJAMA = dict(habit="#74c0fc", motif="pois", couleur_motif="#fff3bf")


def bao(x, y, s=1.0, pyjama=True, **k):
    reglages = dict(PYJAMA) if pyjama else dict(habit="#fab005")
    return perso("panda", x, y, s, **{**reglages, **k})


def maman(x, y, s=1.35, **k):
    return perso("panda", x, y, s, **{**dict(habit="#e64980", acc=("noeud",), couleur_acc="#f783ac"), **k})


def papa(x, y, s=1.45, **k):
    return perso("panda", x, y, s, **{**dict(habit="#2f9e44", acc=("lunettes",)), **k})


def doudou(x, y, s=0.32, **k):
    return perso("lapin", x, y, s, **{**dict(couleur="#ffd8a8", habit="#ffa94d", joues=False), **k})


def chambre(S, nuit_=False):
    if nuit_:
        interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    else:
        interieur(S, "#e7f5ff", "#e8c39e", y=600, papier="#d0ebff")


def salle_de_bain(S):
    interieur(S, "#e3fafc", "#99e9f2", y=580, plinthe="#66d9e8")
    for x in range(0, 800, 80):
        for y in range(0, 580, 80):
            S.add(rect(x + 2, y + 2, 76, 76, "#ffffff", opacity=0.4, rx=6))


def baignoire(x, y, s=1.0):
    return place([rect(-200, -150, 400, 130, "#ffffff", rx=50, stroke="#ced4da", stroke_width=6),
                  rect(-170, -30, 30, 30, "#ced4da", rx=6), rect(140, -30, 30, 30, "#ced4da", rx=6)], x, y, s)


def mousse(x, y, s=1.0, graine=1):
    r = random.Random(graine)
    return place([cercle(r.uniform(-180, 180), r.uniform(-20, 10), r.uniform(18, 34), "#ffffff", stroke="#e3fafc", stroke_width=3)
                  for _ in range(22)], x, y, s)


def brosse(x, y, s=1.0, rot=0):
    return place([rect(-6, -80, 12, 80, "#e64980", rx=6), rect(-8, -110, 16, 30, "#fff", rx=4, stroke="#dee2e6", stroke_width=2)], x, y, s, rot=rot)


def livre_ouvert(x, y, s=1.0):
    return place([chemin("M 0 0 Q -50 -20 -100 -6 L -100 -76 Q -50 -90 0 -70 Z", "#fff", stroke="#adb5bd", sw=3),
                  chemin("M 0 0 Q 50 -20 100 -6 L 100 -76 Q 50 -90 0 -70 Z", "#fff", stroke="#adb5bd", sw=3),
                  etoile5(-50, -44, 14, "#fcc419"), lune(50, -44, 14, "#fcc419", croissant=True, fond_ciel="#fff")], x, y, s)


def dans_le_lit(S, qui, x=330, y=760, w=460, couette="#7048e8", hauteur_couette=680):
    """Lit vu de face, avec un personnage dont on ne voit que la tête."""
    S.add(lit(x, y, w, "#e5dbff", couette))
    cid = uid("c")
    S.add(el("clipPath", rect(0, 0, 800, hauteur_couette + 20, "#000"), id=cid))
    S.add(g(qui, clip_path=f"url(#{cid})"))
    S.add(rect(x - w / 2 + 40, hauteur_couette, w - 40, 70, couette, rx=18))
    S.add(g([etoile5(x - w / 2 + 110 + k * 70, hauteur_couette + 34, 9, "#fff3bf") for k in range(int((w - 120) / 70))]))


def baille_txt(x, y, taille, n_a=3):
    return texte(x, y, "A" + "a" * n_a + "h !", taille, "#5f3dc4", contour="#fff", rot=-6)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(fenetre(500, 110, 200, 180, "#1c2a52", "#e5dbff", nuit_=True))
    S.add(lit(400, 780, 520, "#e5dbff", "#7048e8"))
    S.add(bao(400, 700, 1.45, expr="fache", bras="croises"))
    S.add(doudou(560, 690, 0.4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bao(200, 262, 1.0, expr="baille", bras="haut"))
    return S


def p01():
    S = Scene()
    chambre(S)
    S.add(fenetre(80, 100, 200, 180, "#ffa94d", rideaux="#b197fc"))
    S.add(tour_cubes(620, 600, 0.9))
    S.add(maman(570, 770, 1.7, expr="sourire", bras="hanches", regard=(-1, 0)))
    S.add(bao(250, 770, 1.15, pyjama=False, expr="fache", bras="poing", regard=(1, 0)))
    S.add(bulle(200, 380, 380, 80, "Je n'ai pas sommeil !", 34, pointe=(260, 500)))
    return S


def p02():
    S = Scene()
    salle_de_bain(S)
    S.add(bao(400, 640, 1.2, pyjama=False, habit=None, expr="rire", bras="haut"))
    S.add(baignoire(400, 760, 1.2))
    S.add(rect(400 - 230, 560, 460, 40, "#99e9f2", opacity=0.7))
    S.add(mousse(400, 590, 1.1))
    S.add(bulle(560, 120, 300, 70, "Pas sommeil !", 34, pointe=(470, 370)))
    S.add(texte(200, 250, "Aah…", 36, "#5f3dc4", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(fenetre(80, 100, 200, 180, "#5f3dc4", rideaux="#b197fc", nuit_=True))
    S.add(bao(420, 760, 1.4, expr="baille", bras="etire", rot=-8))
    S.add(mouvement(270, 520, 1.1, rot=-20), mouvement(570, 520, 1.1, rot=20))
    S.add(baille_txt(640, 280, 50, 3))
    return S


def p04():
    S = Scene()
    salle_de_bain(S)
    S.add(rect(470, 120, 260, 220, "#d0ebff", rx=20, stroke="#ffffff", stroke_width=12))
    S.add(rect(460, 480, 280, 40, "#ffffff", rx=10), rect(560, 520, 80, 260, "#ffffff"), rect(590, 450, 20, 34, "#adb5bd", rx=6))
    S.add(bao(320, 780, 1.35, expr="concentre", bras="tient", objet=brosse(68, -146, 0.6, 30)))
    S.add(baille_txt(250, 300, 54, 4))
    return S


def p05():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(lampe(670, 600, 1.2))
    S.add(papa(250, 780, 1.7, expr="sourire", bras="porte", objet=livre_ouvert(0, -40, 0.65), regard=(1, 1)))
    S.add(bao(510, 770, 1.15, expr="baille", bras="joues"))
    S.add(baille_txt(530, 330, 60, 5))
    return S


def p06():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(bao(380, 760, 1.4, expr="baille", bras="tient", objet=place([rect(-22, -36, 44, 60, "#d0ebff", rx=6, opacity=0.9),
                                                                     rect(-22, -6, 44, 30, "#74c0fc", rx=6)], 68, -146)))
    S.add(bulle(250, 150, 220, 70, "Soif !", 36, pointe=(320, 380)))
    S.add(baille_txt(600, 300, 64, 6))
    return S


def p07():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(lit(420, 760, 480, "#e5dbff", "#7048e8"))
    S.add(doudou(640, 790, 0.38, expr="sourire"))
    S.add(bao(250, 790, 1.2, expr="surpris", bras="montre", regard=(1, 1)))
    S.add(bulle(420, 230, 360, 80, "Doudou, te voilà !", 36, pointe=(280, 470)))
    return S


def p08():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(cercle(150, 560, 120, "#ffe066", opacity=0.2), lune(150, 560, 26, "#ffe066", visage=True))
    dans_le_lit(S, g([bao(400, 790, 1.2, expr="baille", bras="calin"), doudou(470, 690, 0.32)]))
    S.add(maman(650, 790, 1.5, expr="content", bras="calin", flip=True))
    S.add(coeur(560, 340, 1.2, "#f783ac"))
    S.add(baille_txt(330, 260, 70, 7))
    return S


def p09():
    S = Scene()
    chambre(S, nuit_=True)
    ciel_ = g([rect(300, 90, 380, 300, "#1c2a52")] + [etoile5(330 + (k * 67) % 330, 120 + (k * 53) % 240, 10, "#fff3bf") for k in range(9)])
    S.add(fenetre(300, 90, 380, 300, "#1c2a52", "#e5dbff", contenu=ciel_))
    S.add(bao(240, 770, 1.3, expr="dort", bras="montre"))
    S.add(texte(560, 470, "1, 2, 3…", 50, "#fff3bf", contour="#3b2a7a"))
    S.add(baille_txt(560, 560, 60, 9))
    return S


def p10():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(cercle(150, 560, 120, "#ffe066", opacity=0.2), lune(150, 560, 26, "#ffe066", visage=True))
    dans_le_lit(S, g([bao(360, 800, 1.2, expr="dort"), doudou(430, 700, 0.32, expr="dort")]))
    S.add(zzz(470, 380, 1.4, "#e5dbff"))
    S.add(maman(650, 790, 1.5, expr="content", bras="chut", flip=True))
    S.add(texte(400, 160, "Chut…", 60, "#fff3bf", contour="#3b2a7a"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bao-seul.svg", vignette),
    ("01-au-lit.svg", p01), ("02-le-bain.svg", p02), ("03-le-pyjama.svg", p03),
    ("04-les-dents.svg", p04), ("05-l-histoire.svg", p05), ("06-un-verre-d-eau.svg", p06),
    ("07-doudou.svg", p07), ("08-le-calin.svg", p08), ("09-les-etoiles.svg", p09),
    ("10-chut.svg", p10),
]
