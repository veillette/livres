"""L'Ours et les Deux Compagnons — d'après La Fontaine.

Gaspard et Mathis vendent la peau d'un ours qu'ils n'ont pas encore vu.
Face à l'ours, Gaspard grimpe dans un arbre et abandonne son ami ; Mathis
fait le mort. L'ours le renifle et s'en va. Adaptation douce : l'ours n'est
pas chassé, les deux compagnons rendent l'argent et Gaspard demande pardon.
"""
from fables import *

ID = "ours-compagnons"
GASPARD = dict(peau="claire", cheveux="blond", coiffure="herisses", habit="#e8590c", robe=False, jambes="#495057",
               chaussures="#5c3a1e")
MATHIS = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#5c3a1e",
              chaussures="#343a40")
MARCHANDE = dict(peau="doree", cheveux="gris", coiffure="chignon", habit="#9c36b5", acc=("lunettes",))


def gaspard(x, y, s=1.0, **k):
    return personne(x, y, s, **{**GASPARD, **k})


def mathis(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MATHIS, **k})


def marchande(x, y, s=1.1, **k):
    return personne(x, y, s, **{**MARCHANDE, **k})


def ours(x, y, s=2.0, **k):
    return perso("ours", x, y, s, **{**dict(couleur="#7a4f2d", visage="#c9a27a", joues=False), **k})


def bourse(x, y, s=1.0):
    return place([chemin("M -30 0 Q -40 -40 -14 -54 L 14 -54 Q 40 -40 30 0 Z", "#c68642"), rect(-18, -60, 36, 10, "#8d5524", rx=4),
                  cercle(0, -24, 9, "#ffd43b")], x, y, s)


def piece(x, y, r=12):
    return g([cercle(x, y, r, "#fcc419", stroke="#f08c00", stroke_width=2), cercle(x - r * 0.3, y - r * 0.3, r * 0.25, "#fff", opacity=0.6)])


def boutique(S):
    interieur(S, "#fff4e6", "#c9a27a", 560, papier="#ffd8a8", plinthe="#a0693a")
    S.add(rect(80, 150, 640, 16, "#8d5524", rx=6))
    for k, c in enumerate(["#a0693a", "#fa5252", "#495057", "#7048e8", "#2f9e44"]):
        S.add(chapeau(150 + k * 125, 230, 0.9, c, "#ffd43b"))
    S.add(rect(80, 560, 640, 30, "#8d5524"))


def foret_sombre(S, graine=1, sombre=False):
    ciel(S, "#74c0fc" if not sombre else "#4c6ef5", "#d3f9d8")
    for k in range(6):
        S.add(sapin(60 + k * 140, 620, 1.4 + (k % 2) * 0.4, "#2b8a3e", "#2f9e44"))
    S.add(rect(0, 620, 800, 180, "#69db7c"))
    rnd = random.Random(graine)
    for _ in range(8):
        S.add(herbe(rnd.uniform(0, 800), rnd.uniform(650, 790), 1.0, "#40c057"))


def grand_arbre(x, y, s=1.0):
    m = [rect(-34, -480, 68, 480, "#8d5524", rx=12), chemin("M 0 -300 Q -90 -320 -170 -360", stroke="#8d5524", sw=26),
         cercle(0, -500, 150, "#2f9e44"), cercle(-130, -420, 90, "#37b24d"), cercle(130, -420, 90, "#37b24d")]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret_sombre(S, 1)
    S.add(grand_arbre(620, 800, 1.0))
    S.add(gaspard(520, 410, 0.7, expr="oups", bras="haut", rot=10))
    S.add(ours(170, 760, 1.4, expr="neutre", bras="bas", regard=(1, 1)))
    S.add(mathis(540, 720, 1.0, expr="dort", rot=-90))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(gaspard(130, 264, 0.95, expr="content", bras="salut"), mathis(270, 264, 0.95, expr="content", bras="salut", flip=True))
    return S


def p01():
    S = Scene()
    boutique(S)
    S.add(marchande(570, 790, 1.15, expr="sourire", bras="hanches"))
    S.add(gaspard(170, 790, 1.05, expr="content", bras="salut"), mathis(330, 790, 1.05, expr="sourire"))
    S.add(bourse(700, 590, 0.9))
    return S


def p02():
    S = Scene()
    boutique(S)
    S.add(marchande(600, 790, 1.15, expr="surpris", bras="donne", flip=True))
    S.add(piece(470, 600), piece(500, 584), piece(486, 616))
    S.add(gaspard(200, 790, 1.1, expr="fier", bras="montre", regard=(1, -1)), mathis(350, 790, 1.0, expr="content"))
    S.add(bulle(330, 170, 520, 120, "La peau de l'ours ?\nElle est à vous !", 38, pointe=(220, 500)))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=3)
    sol(S, 640, "#8ce99a")
    S.add(gaspard(240, 790, 1.1, expr="rire", bras="pense", regard=(1, -1)))
    S.add(mathis(560, 790, 1.1, expr="rire", bras="pense", regard=(-1, -1)))
    S.add(pensee(400, 230, 170, g([chapeau(330, 240, 0.8, "#fa5252"), bourse(470, 270, 1.0), piece(400, 200, 16), piece(430, 300, 12)]), depuis=(300, 520)))
    return S


def p04():
    S = Scene()
    foret_sombre(S, 4)
    S.add(gaspard(250, 790, 1.15, expr="fier", bras="poing"))
    S.add(mathis(500, 790, 1.1, expr="fier", bras="hanches"))
    S.add(bulle(400, 200, 460, 90, "Peur ? Jamais !", 44, pointe=(290, 520)))
    return S


def p05():
    S = Scene()
    foret_sombre(S, 5, sombre=True)
    S.add(ours(540, 800, 2.5, expr="furieux", bras="haut"))
    S.add(gaspard(150, 790, 0.9, expr="surpris", bras="joues"), mathis(280, 790, 0.9, expr="surpris", bras="joues"))
    S.add(texte(250, 230, "GRRRR !", 90, "#c92a2a", contour="#fff", rot=-8))
    return S


def p06():
    S = Scene()
    foret_sombre(S, 6)
    S.add(grand_arbre(560, 800, 1.0))
    S.add(gaspard(420, 470, 0.75, expr="oups", bras="haut"))
    S.add(mouvement(470, 520, 0.9, rot=-90))
    S.add(mathis(170, 790, 1.0, expr="pleure", bras="ouverts", regard=(1, -1)))
    S.add(bulle(220, 200, 320, 90, "Attends-moi !", 40, pointe=(180, 520)))
    return S


def p07():
    S = Scene()
    foret_sombre(S, 7)
    S.add(mathis(420, 700, 1.2, expr="dort", rot=-90))
    S.add(texte(560, 260, "Chut…", 60, "#495057", contour="#fff"))
    S.add(ours(700, 790, 1.2, expr="neutre", regard=(-1, 0)))
    return S


def p08():
    S = Scene()
    foret_sombre(S, 8)
    S.add(ours(330, 800, 1.8, expr="concentre", bras="bas", regard=(1, 1), rot=18))
    S.add(mathis(640, 700, 1.2, expr="dort", rot=-90))
    S.add(texte(560, 300, "Snif, snif…", 56, "#7a4f2d", contour="#fff"))
    S.add(grand_arbre(760, 800, 0.7))
    return S


def p09():
    S = Scene()
    foret_sombre(S, 9)
    S.add(mathis(330, 700, 1.0, expr="dort", rot=-90))
    S.add(ours(640, 790, 1.4, expr="neutre", flip=True, regard=(1, 0)))
    S.add(texte(500, 280, "Pfff… il dort.", 48, "#7a4f2d", contour="#fff"))
    return S


def p10():
    S = Scene()
    foret_sombre(S, 10)
    S.add(grand_arbre(620, 800, 0.8))
    S.add(gaspard(470, 790, 1.05, expr="inquiet", bras="ouverts", flip=True))
    S.add(mathis(220, 790, 1.05, expr="neutre", bras="croises"))
    S.add(bulle(500, 190, 480, 120, "Qu'est-ce que l'ours\nt'a dit à l'oreille ?", 36, pointe=(480, 500)))
    return S


def p11():
    S = Scene()
    foret_sombre(S, 11)
    S.add(gaspard(540, 790, 1.05, expr="timide", bras="joues"))
    S.add(mathis(260, 790, 1.1, expr="sourire", bras="montre", regard=(1, 0)))
    S.add(bulle(400, 200, 600, 160, "Ne vends jamais la peau\nde l'ours… et ne laisse jamais\nun ami tout seul !", 34, pointe=(290, 520)))
    return S


def p12():
    S = Scene()
    boutique(S)
    S.add(marchande(620, 790, 1.15, expr="rire", bras="ouverts", flip=True))
    S.add(gaspard(200, 790, 1.05, expr="content", bras="calin"), mathis(330, 790, 1.05, expr="content", bras="donne", objet=bourse(84, -80, 0.6)))
    S.add(coeur(260, 380, 1.2, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("deux-compagnons.svg", vignette),
    ("01-plus-un-sou.svg", p01), ("02-la-peau-de-l-ours.svg", p02), ("03-on-sera-riches.svg", p03), ("04-peur-jamais.svg", p04),
    ("05-l-ours.svg", p05), ("06-dans-l-arbre.svg", p06), ("07-faire-le-mort.svg", p07), ("08-snif-snif.svg", p08),
    ("09-il-s-en-va.svg", p09), ("10-a-l-oreille.svg", p10), ("11-ce-que-l-ours-a-dit.svg", p11), ("12-pardon.svg", p12),
]
