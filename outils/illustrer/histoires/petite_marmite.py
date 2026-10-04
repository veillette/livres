"""La petite marmite — d'après « La Bouillie sucrée » des frères Grimm.

Lisette partage ses mûres avec une vieille dame, qui lui offre une marmite
magique : « Petite marmite, cuis ! » et « Petite marmite, arrête ! ». Un
jour, Maman oublie le mot pour l'arrêter : la bouillie envahit la maison,
la rue, le village… jusqu'au retour de Lisette. Tout le village se régale.
"""
from contes import *

ID = "petite-marmite"
BOUILLIE = "#ffe8a3"
BOUILLIE_F = "#f6c453"
LISETTE = dict(peau="doree", cheveux="chatain", coiffure="tresses", habit="#f76707")
MAMAN = dict(peau="doree", cheveux="chatain", coiffure="chignon", habit="#1c7ed6")
DAME = dict(peau="foncee", cheveux="blanc", coiffure="chignon", habit="#7048e8", cape="#5c3a1e")


def lisette(x, y, s=1.0, **k):
    return personne(x, y, s, **{**LISETTE, **k})


def maman(x, y, s=1.2, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def dame(x, y, s=1.15, **k):
    return personne(x, y, s, **{**DAME, **k})


def villageois(x, y, s=1.0, n_=0, **k):
    modeles = [dict(peau="claire", cheveux="roux", coiffure="courts", habit="#2f9e44", robe=False, jambes="#495057"),
               dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#e64980"),
               dict(peau="rosee", cheveux="gris", coiffure="chauve_cote", habit="#868e96", robe=False, jambes="#343a40", barbe="#ced4da"),
               dict(peau="doree", cheveux="noir", coiffure="queue", habit="#fab005")]
    return personne(x, y, s, **{**modeles[n_ % 4], **k})


def marmite(x, y, s=1.0, cuit=False, deborde=False):
    """Petite marmite en cuivre ; (x, y) = dessous."""
    m = [ellipse(0, 0, 80, 12, "#000", opacity=0.1),
         chemin("M -70 -90 Q -80 -10 -40 0 L 40 0 Q 80 -10 70 -90 Z", "#e8590c"),
         chemin("M -70 -90 Q -80 -10 -40 0", stroke="#d9480f", sw=6),
         rect(-84, -100, 168, 18, "#d9480f", rx=8),
         chemin("M -84 -84 Q -110 -84 -104 -60", stroke="#495057", sw=8), chemin("M 84 -84 Q 110 -84 104 -60", stroke="#495057", sw=8),
         ellipse(-30, -50, 12, 26, "#ffa94d", opacity=0.6)]
    if cuit or deborde:
        m.append(ellipse(0, -100, 74, 14, BOUILLIE))
        m += [cercle(-26, -110, 9, BOUILLIE, stroke=BOUILLIE_F, stroke_width=2), cercle(20, -114, 12, BOUILLIE, stroke=BOUILLIE_F, stroke_width=2)]
        m += [chemin(f"M {dx} -130 q -12 -20 0 -40 q 12 -20 0 -40", stroke="#fff", sw=5, opacity=0.7) for dx in (-20, 20)]
    if deborde:
        m.append(chemin("M -84 -100 Q -110 -60 -100 -20 Q -96 0 -120 4 L -60 4 Q -84 -40 -60 -96 Z", BOUILLIE))
        m.append(chemin("M 84 -100 Q 116 -50 104 -10 Q 100 4 130 4 L 60 4 Q 84 -50 60 -96 Z", BOUILLIE))
    return place(m, x, y, s)


def flot(S, y, couleur=BOUILLIE, graine=1, vagues=True):
    """Bouillie qui recouvre tout ce qui est sous y."""
    rnd = random.Random(graine)
    d = f"M 0 {y}"
    for k in range(9):
        d += f" Q {k * 100 + 50} {y - rnd.uniform(10, 40)} {(k + 1) * 100} {y}"
    d += " L 800 800 L 0 800 Z"
    S.add(chemin(d, couleur, stroke=BOUILLIE_F, sw=4))
    if vagues:
        for k in range(10):
            S.add(cercle(rnd.uniform(20, 780), rnd.uniform(y + 20, 790), rnd.uniform(6, 14), "#fff3bf", stroke=BOUILLIE_F, stroke_width=2))


def cuillere(x, y, s=1.0, rot=0):
    return place([rect(-4, 0, 8, 90, "#adb5bd", rx=4), ellipse(0, -10, 14, 20, "#ced4da")], x, y, s, rot=rot)


def mures(x, y, s=1.0):
    m = []
    for dx, dy in ((-10, 0), (8, -4), (0, -14), (14, 8), (-6, 12)):
        m.append(cercle(dx, dy, 8, "#5f3dc4"))
    return place(m, x, y, s)


def panier_mures(x, y, s=1.0):
    return place([chemin("M -60 -60 Q 0 -140 60 -60", stroke="#8d5524", sw=6), mures(-24, -64, 0.8), mures(18, -66, 0.8),
                  chemin("M -66 -60 L 66 -60 L 52 0 L -52 0 Z", "#c68642"), trait(-60, -36, 60, -36, "#8d5524", 3)], x, y, s)


def cuisine(S, y=560):
    interieur(S, "#fff4e6", "#c9a27a", y, papier="#ffe8cc", plinthe="#a0693a")
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#ffa94d"))
    S.add(rect(70, 130, 180, 170, "#c68642", rx=8), rect(80, 140, 160, 150, "#a0693a", rx=6), cercle(225, 215, 6, "#ffd43b"))


def placard_vide(x, y):
    return g([rect(x, y, 180, 170, "#c68642", rx=8), rect(x + 10, y + 10, 160, 150, "#5c3a1e", rx=6),
              rect(x + 10, y + 80, 160, 8, "#a0693a"), araignee(x + 120, y + 40, 0.5)])


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    village_(S, 600, graine=5)
    flot(S, 680, graine=2)
    S.add(marmite(400, 700, 1.3, deborde=True))
    S.add(lisette(180, 790, 1.15, expr="rire", bras="haut"))
    S.add(villageois(640, 790, 1.0, 1, expr="miam", bras="tient", objet=cuillere(68, -146, 0.8)))
    S.add(texte(420, 230, "Petite marmite, cuis !", 52, "#e8590c", contour="#fff", rot=-4))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(marmite(200, 262, 1.2, cuit=True))
    return S


def p01():
    S = Scene()
    interieur(S, "#e9ecef", "#c9a27a", 560, plinthe="#a0693a")
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff"))
    S.add(placard_vide(70, 130))
    S.add(table(420, 760, 300, 120, "#a0693a"), bol_porridge(420, 628, 1.0, vide=True))
    S.add(maman(600, 790, 1.15, expr="triste", bras="calin"))
    S.add(lisette(250, 790, 1.0, expr="triste", bras="calin"))
    S.add(texte(250, 470, "Glouglou…", 40, "#868e96", contour="#fff"))
    return S


def p02():
    S = Scene()
    foret(S, graine=3)
    S.add(buisson(120, 640, 1.0, baies="#5f3dc4"), buisson(700, 650, 0.9, baies="#5f3dc4"))
    S.add(lisette(300, 790, 1.05, expr="content", bras="donne", objet=panier_mures(84, -92, 0.7)))
    S.add(dame(560, 790, 1.1, expr="sourire", bras="donne2", flip=True))
    return S


def p03():
    S = Scene()
    foret(S, graine=4)
    S.add(dame(520, 790, 1.15, expr="content", bras="donne", flip=True, objet=marmite(84, -80, 0.5)))
    S.add(lisette(260, 790, 1.05, expr="surpris", bras="joues"))
    S.add(bulle(400, 180, 560, 130, "« Petite marmite, cuis ! »\n« Petite marmite, arrête ! »", 34, pointe=(520, 500)))
    S.add(etincelles(470, 640, 0.9))
    return S


def p04():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 360, 130, "#a0693a"))
    S.add(marmite(400, 640, 1.0, cuit=True))
    S.add(lisette(150, 790, 1.0, expr="rire", bras="haut"), maman(660, 800, 1.1, expr="miam", bras="tient", objet=cuillere(68, -146, 0.8)))
    S.add(texte(400, 340, "Blop, blop !", 58, "#e8590c", contour="#fff"))
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(table(470, 790, 300, 130, "#a0693a"), marmite(470, 640, 0.9))
    S.add(porte(150, 560, 140, 300, ouverte=True))
    S.add(lisette(150, 560, 0.75, expr="content", bras="salut"))
    S.add(maman(660, 800, 1.1, expr="malin", bras="montre", flip=True))
    S.add(bulle(470, 200, 460, 90, "Petite marmite, cuis !", 36, pointe=(620, 480)))
    return S


def p06():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 360, 130, "#a0693a"), marmite(400, 640, 1.0, deborde=True))
    S.add(maman(640, 800, 1.1, expr="surpris", bras="ouverts", flip=True))
    S.add(bulle(330, 200, 460, 120, "Assez ! Stop !\nÇa suffit !", 40, pointe=(600, 480)))
    return S


def p07():
    S = Scene()
    cuisine(S)
    S.add(table(400, 790, 360, 130, "#a0693a"), marmite(400, 640, 1.0, deborde=True))
    flot(S, 700, graine=3)
    S.add(maman(640, 790, 1.1, expr="oups", bras="tete", flip=True))
    S.add(texte(300, 250, "Holà ! Halte !", 54, "#e8590c", contour="#fff"), texte(300, 330, "Arrête-toi ?", 46, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(maison(400, 620, 2.0, mur="#ffe8cc", toit="#c92a2a"))
    flot(S, 620, graine=4)
    S.add(chemin("M 350 450 L 350 620 L 450 620 L 450 450 Z", BOUILLIE, stroke=BOUILLIE_F, sw=4))
    S.add(perso("chat", 640, 380, 0.6, expr="surpris", bras="haut"))
    S.add(texte(400, 160, "Glop, glop, glop !", 54, "#e8590c", contour="#fff"))
    return S


def p09():
    S = Scene()
    village_(S, 560, graine=6)
    flot(S, 600, graine=5)
    for k, x in enumerate((110, 320, 520, 700)):
        S.add(villageois(x, 790 - (k % 2) * 20, 0.85, k, expr="surpris", bras="joues" if k % 2 else "haut"))
    flot(S, 740, graine=6, vagues=False)
    return S


def p10():
    S = Scene()
    village_(S, 560, graine=7)
    flot(S, 640, graine=8)
    S.add(lisette(420, 790, 1.3, expr="fache", bras="montre", regard=(1, 0)))
    S.add(marmite(680, 700, 0.9, cuit=True))
    S.add(bulle(380, 200, 520, 90, "Petite marmite, arrête !", 38, pointe=(430, 500)))
    return S


def p11():
    S = Scene()
    village_(S, 560, graine=8)
    flot(S, 680, graine=9)
    S.add(villageois(100, 790, 0.9, 0, expr="miam", bras="tient", objet=cuillere(68, -146, 0.8)))
    S.add(villageois(260, 790, 0.9, 1, expr="rire", bras="tient", objet=cuillere(68, -146, 0.8)))
    S.add(lisette(420, 790, 1.0, expr="rire", bras="haut"))
    S.add(villageois(580, 790, 0.9, 2, expr="miam", bras="tient", objet=cuillere(68, -146, 0.8)))
    S.add(maman(720, 800, 1.0, expr="rire", bras="tient", flip=True, objet=cuillere(68, -146, 0.8)))
    S.add(texte(400, 200, "Miam !", 80, "#e8590c", contour="#fff"))
    return S


def p12():
    S = Scene()
    cuisine(S)
    S.add(rect(80, 132, 170, 40, "#fff", rx=6), texte(165, 162, "ARRÊTE !", 26, "#c92a2a"))
    S.add(table(600, 790, 300, 130, "#a0693a"), marmite(600, 640, 0.9))
    S.add(lisette(260, 790, 1.0, expr="rire", bras="calin"), maman(370, 800, 1.1, expr="rire", bras="calin", flip=True))
    S.add(coeur(320, 380, 1.2, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("marmite-seule.svg", vignette),
    ("01-le-placard-vide.svg", p01), ("02-les-mures.svg", p02), ("03-la-marmite.svg", p03), ("04-blop-blop.svg", p04),
    ("05-maman-a-faim.svg", p05), ("06-assez.svg", p06), ("07-ca-deborde.svg", p07), ("08-la-maison.svg", p08),
    ("09-le-village.svg", p09), ("10-arrete.svg", p10), ("11-le-festin.svg", p11), ("12-le-mot-magique.svg", p12),
]
