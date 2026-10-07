"""Sur le chantier — tous les métiers qui construisent une maison."""
from base import *
from base import _assombrir
from objets import *
from metiers import *
from fantastique import echelle
from sciences import cle

ID = "chantier-maison"
FATOU = dict(peau="foncee", cheveux="noir", coiffure="tresses", habit="#1c7ed6", jambes="#1c7ed6",
             chaussures="#5c3a1e", tenue=gilet_chantier(), coiffe=casque_chantier("#f8f9fa"))
MARCO = dict(peau="claire", cheveux="chatain", coiffure="courts", habit="#868e96", jambes="#495057",
             chaussures="#5c3a1e", barbe="#8d5524", tenue=gilet_chantier(), coiffe=casque_chantier())
BRIQUE = "#e8590c"


def fatou(x, y, s=1.6, **k):
    return pro(x, y, s, **{**FATOU, **k})


def marco(x, y, s=1.6, **k):
    return pro(x, y, s, **{**MARCO, **k})


def terrain(S, y=600):
    ciel(S)
    collines(S, y, "#b2f2bb", graine=11)
    S.add(rect(0, y, 800, 800 - y, "#d9a066"))
    for k in range(12):
        S.add(cercle(30 + k * 67, y + 60 + (k % 3) * 50, 6, "#a0693a"))


def mur(x, y, w, h, brique=BRIQUE, joint="#ffe8cc", rangs=None):
    """Mur de briques ; (x, y) = coin bas gauche ; rangs = nombre de rangées posées."""
    m = []
    bh, bw = 26, 60
    nb = int(h // bh) if rangs is None else rangs
    for r in range(nb):
        yy = y - (r + 1) * bh
        dec = 0 if r % 2 == 0 else bw / 2
        m.append(rect(x, yy, w, bh, joint))
        xx = x - dec
        while xx < x + w:
            x0, x1 = max(xx, x), min(xx + bw, x + w)
            if x1 - x0 > 4:
                m.append(rect(x0 + 2, yy + 2, x1 - x0 - 4, bh - 4, brique, rx=2))
            xx += bw
    return g(m)


def truelle(x, y, s=1.0, rot=0):
    return place([rect(-6, -60, 12, 40, "#a0693a", rx=4), trait(0, -20, 0, -4, "#868e96", 4),
                  poly([(-24, -4), (24, -4), (0, 40)], "#ced4da", stroke="#868e96", stroke_width=2)], x, y, s, rot=rot)


def niveau(x, y, w=260, s=1.0, rot=0):
    return place([rect(-w / 2, -20, w, 40, "#fcc419", rx=6, stroke="#f08c00", stroke_width=3),
                  rect(-50, -12, 100, 24, "#d3f9d8", rx=12, stroke="#2f9e44", stroke_width=3),
                  trait(-16, -12, -16, 12, "#2b8a3e", 3), trait(16, -12, 16, 12, "#2b8a3e", 3),
                  ellipse(0, 0, 13, 8, "#fff")], x, y, s, rot=rot)


def pelleteuse(x, y, s=1.0):
    m = [rect(-200, -60, 280, 50, "#495057", rx=24)]
    for k in range(6):
        m.append(cercle(-176 + k * 46, -35, 14, "#868e96"))
    m += [rect(-170, -170, 220, 110, "#fab005", rx=12), rect(-160, -260, 110, 100, "#fab005", rx=10),
          rect(-148, -248, 86, 70, "#a5d8ff", rx=6),
          chemin("M 30 -150 L 150 -280 L 260 -160", stroke="#f08c00", sw=26),
          chemin("M 240 -170 L 300 -110 L 250 -70 L 220 -120 Z", "#868e96")]
    return place(m, x, y, s)


def betonniere(x, y, s=1.0, rot_=0):
    m = [trait(-60, 0, -20, -110, "#495057", 10), trait(60, 0, 20, -110, "#495057", 10), roue(-70, -20, 24), roue(70, -20, 24),
         place([ellipse(0, 0, 90, 70, "#e03131"), poly([(60, -40), (120, -30), (120, 30), (60, 40)], "#c92a2a"),
                trait(-60, -30, 40, -50, "#ffa8a8", 6), trait(-60, 20, 40, 0, "#ffa8a8", 6)], 0, -150, rot=-20)]
    return place(m, x, y, s)


def tas(x, y, s=1.0, c="#ffe066", grains=None):
    m = [chemin("M -90 0 Q -40 -90 0 -90 Q 40 -90 90 0 Z", c)]
    if grains:
        for k in range(12):
            m.append(cercle(-60 + (k * 37) % 120, -14 - (k * 23) % 60, 7, grains))
    return place(m, x, y, s)


def grue(x, y, s=1.0, charge=None, cable=360):
    """Grue à tour ; (x, y) = pied ; la flèche part vers la droite."""
    m = [rect(-24, -620, 48, 620, "none", stroke="#fab005", stroke_width=8)]
    for k in range(12):
        m.append(trait(-24, -k * 52, 24, -(k + 1) * 52, "#fab005", 6))
    m += [rect(-120, -660, 520, 40, "none", stroke="#fab005", stroke_width=8),
          rect(-140, -660, 60, 60, "#868e96"), rect(18, -700, 70, 60, "#fab005", rx=6), rect(28, -690, 50, 34, "#a5d8ff", rx=4),
          rect(260, -626, 30, 16, "#495057"), trait(275, -610, 275, -610 + cable, "#495057", 3)]
    if charge:
        m.append(place(charge, 275, -610 + cable))
    return place(m, x, y, s)


def poutre(w=220):
    return g([trait(-30, 0, 0, -30, "#495057", 3), trait(30, 0, 0, -30, "#495057", 3),
              rect(-w / 2, 0, w, 26, "#c68642", rx=4)])


def maison_chantier(x, y, s=1.0, etape=1):
    """Maison en construction : 1 murs bas, 2 murs, 3 toit en cours, 4 finie."""
    m = []
    if etape == 1:
        m.append(mur(-200, 0, 400, 0, rangs=4))
    else:
        m.append(mur(-200, 0, 400, 0, rangs=9))
        m.append(rect(-150, -170, 90, 80, "#343a40") if etape < 4 else rect(-150, -170, 90, 80, "#a5d8ff", stroke="#fff", stroke_width=6))
        m.append(rect(40, -170, 90, 80, "#343a40") if etape < 4 else rect(40, -170, 90, 80, "#a5d8ff", stroke="#fff", stroke_width=6))
    if etape >= 3:
        m.append(poly([(-230, -234), (0, -380), (230, -234)], "#c68642"))
        for r in range(6 if etape >= 4 else 3):
            yy = -244 - r * 22
            demi = 220 - r * 33
            m.append(rect(-demi, yy, 2 * demi, 20, "#c92a2a", rx=4))
    if etape >= 4:
        m.append(rect(-200, -234, 400, 234, "#ffe8cc", opacity=0.0))
        m.append(rect(-30, -110, 60, 110, "#1c7ed6", rx=4))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    terrain(S)
    S.add(grue(80, 640, 0.65, charge=poutre(160), cable=200))
    S.add(maison_chantier(500, 640, 0.75, etape=2))
    S.add(fatou(230, 790, 1.6, expr="rire", bras="salut"))
    S.add(marco(650, 790, 1.4, expr="content", bras="hanches"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(place(casque_chantier(), 120, 420, 0.95))
    S.add(mur(220, 260, 140, 0, rangs=4))
    S.add(truelle(330, 110, 1.2, rot=30))
    return S


def p01():
    S = Scene()
    terrain(S)
    S.add(trait(80, 620, 720, 620, "#fff", 4), trait(80, 620, 80, 700, "#fff", 4), trait(720, 620, 720, 700, "#fff", 4))
    plan = g([rect(-130, -100, 260, 170, "#1c7ed6", rx=6), rect(-80, -50, 160, 100, "none", stroke="#fff", stroke_width=4),
              poly([(-90, -50), (0, -90), (90, -50)], "none", stroke="#fff", stroke_width=4),
              rect(-15, 10, 30, 40, "none", stroke="#fff", stroke_width=3)])
    S.add(fatou(300, 790, 1.6, expr="content", bras="large", objet=place(plan, 0, -40, 0.6)))
    S.add(marco(560, 790, 1.6, expr="bouche_bee", bras="pense", regard=(-1, 0)))
    S.add(texte(400, 170, "Au travail !", 60, "#f08c00", contour="#fff"))
    return S


def p02():
    S = Scene()
    terrain(S)
    S.add(ellipse(560, 680, 200, 50, "#7c4a1e"))
    S.add(pelleteuse(320, 740, 1.0))
    S.add(tas(130, 620, 1.0, "#a0693a"))
    S.add(texte(250, 200, "Vroum !", 64, "#f08c00", contour="#fff"))
    return S


def p03():
    S = Scene()
    terrain(S)
    S.add(tas(100, 640, 0.85, "#ffe066"), tas(260, 640, 0.75, "#adb5bd", grains="#868e96"))
    S.add(texte(100, 680, "sable", 30, "#495057"), texte(260, 680, "graviers", 30, "#495057"))
    S.add(rect(350, 540, 80, 100, "#dee2e6", rx=6), texte(390, 680, "ciment", 30, "#495057"))
    S.add(betonniere(660, 700, 1.3))
    S.add(texte(620, 320, "Ça tourne !", 44, "#e03131", contour="#fff"))
    S.add(mouvement(530, 420, 0.8, rot=200))
    S.add(marco(500, 790, 1.15, expr="concentre", bras="porte", objet=g([rect(-30, -100, 60, 70, "#74c0fc", rx=8)])))
    S.add(texte(500, 520, "eau", 30, "#1c7ed6", contour="#fff"))
    return S


def p04():
    S = Scene()
    terrain(S)
    S.add(mur(140, 640, 520, 0, rangs=7))
    S.add(marco(400, 790, 1.6, expr="concentre", bras="donne", regard=(1, -0.3)))
    S.add(truelle(400 + 84 * 1.6, 790 - 92 * 1.6, 1.0, rot=-40))
    S.add(rect(620, 420, 56, 22, BRIQUE, rx=2))
    S.add(texte(400, 180, "Une rangée, puis une autre…", 36, "#e8590c", contour="#fff"))
    return S


def p05():
    S = Scene()
    terrain(S)
    S.add(mur(60, 700, 680, 0, rangs=12))
    S.add(niveau(400, 360, 420, 1.0))
    S.add(loupe_bulle())
    S.add(marco(650, 790, 1.2, expr="content", bras="montre", flip=True, regard=(-1, -1)))
    return S


def loupe_bulle():
    from animaux import loupe
    contenu = g([rect(270, 100, 260, 200, "#fcc419"), rect(300, 150, 200, 100, "#d3f9d8", rx=50, stroke="#2f9e44", stroke_width=6),
                 trait(355, 150, 355, 250, "#2b8a3e", 6), trait(445, 150, 445, 250, "#2b8a3e", 6), ellipse(400, 200, 34, 22, "#fff")])
    return loupe(400, 200, 110, contenu, rot=120)


def p06():
    S = Scene()
    terrain(S)
    S.add(maison_chantier(520, 640, 0.9, etape=2))
    S.add(grue(150, 640, 0.9, charge=poutre(240), cable=330))
    S.add(fatou(640, 790, 1.4, expr="concentre", bras="salut", regard=(-1, -1)))
    S.add(texte(560, 120, "Doucement !", 44, "#f08c00", contour="#fff"))
    return S


def p07():
    S = Scene()
    terrain(S)
    S.add(fatou(400, 790, 2.0, expr="fier", bras="hanches"))
    from sciences import fleche
    S.add(fleche(170, 170, 300, 300, "#e8590c"), texte(140, 150, "casque", 36, "#e8590c", contour="#fff"))
    S.add(fleche(630, 330, 470, 470, "#e8590c"), texte(650, 310, "gilet", 36, "#e8590c", contour="#fff"))
    S.add(fleche(160, 620, 320, 740, "#e8590c"), texte(130, 600, "chaussures", 34, "#e8590c", contour="#fff"))
    S.add(fleche(640, 560, 500, 670, "#e8590c"), texte(650, 540, "gants", 34, "#e8590c", contour="#fff"))
    S.add(cercle(400 - 40 * 2, 790 - 50 * 2, 15, "#fcc419"), cercle(400 + 40 * 2, 790 - 50 * 2, 15, "#fcc419"))
    return S


def p08():
    S = Scene()
    terrain(S)
    S.add(maison_chantier(400, 680, 1.15, etape=3))
    S.add(echelle(150, 700, 0.9, h=430, rot=12))
    S.add(marco(300, 360, 0.7, expr="concentre", bras="porte", objet=rect(-30, -80, 60, 20, "#c92a2a", rx=4)))
    S.add(texte(620, 170, "Plus de pluie dedans !", 34, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    terrain(S)
    S.add(maison_chantier(400, 600, 0.75, etape=4))
    ouvriers = [
        (110, dict(peau="doree", cheveux="noir", coiffure="queue", habit="#fcc419"), "électricité",
         chemin("M 0 0 q 20 -40 40 0 t 40 0", stroke="#fa5252", sw=6)),
        (300, dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7"), "plomberie",
         g([rect(-40, -8, 80, 16, "#adb5bd", rx=6), rect(30, -20, 16, 40, "#adb5bd", rx=4)])),
        (500, dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#69db7c"), "peinture",
         g([rect(-30, -14, 60, 28, "#ffc9e3", rx=8), rect(-4, 14, 8, 50, "#868e96")])),
        (690, dict(peau="rosee", cheveux="blond", coiffure="chignon", habit="#da77f2"), "fenêtres",
         rect(-36, -40, 72, 70, "#a5d8ff", stroke="#fff", stroke_width=6)),
    ]
    for x, perso_, mot, outil in ouvriers:
        S.add(pro(x, 760, 0.95, **perso_, jambes="#495057", chaussures="#5c3a1e", coiffe=casque_chantier(),
                  bras="porte", expr="content", objet=place(outil, 0, -80, 0.9)))
        S.add(texte(x, 795, mot, 26, "#495057", contour="#fff"))
    return S


def p10():
    S = Scene()
    terrain(S)
    S.add(rect(0, 600, 800, 200, "#8ce99a"))
    S.add(maison_chantier(480, 600, 0.95, etape=4))
    S.add(fleur(260, 640, 0.6), fleur(720, 640, 0.6, "#cc5de8"))
    S.add(fatou(160, 790, 1.5, expr="content", bras="donne"))
    S.add(cle(160 + 84 * 1.5 + 6, 790 - 92 * 1.5, 1.0, rot=-20))
    S.add(pro(420, 790, 1.45, peau="doree", cheveux="brun", coiffure="longs", habit="#ff922b", jambes="#495057",
              expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(petit(560, 790, 1.05, peau="doree", cheveux="brun", coiffure="queue", habit="#f783ac", expr="rire", bras="haut"))
    S.add(carton(700, 790, 0.8, w=160, h=120, ouvert=False))
    S.add(bulle(420, 120, 420, 90, "Bienvenue chez vous !", 36, pointe=(220, 480)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("casque-seul.svg", vignette),
    ("01-le-plan.svg", p01), ("02-la-pelleteuse.svg", p02), ("03-le-beton.svg", p03),
    ("04-les-briques.svg", p04), ("05-le-niveau.svg", p05), ("06-la-grue.svg", p06),
    ("07-la-securite.svg", p07), ("08-le-toit.svg", p08), ("09-tous-les-metiers.svg", p09),
    ("10-bienvenue.svg", p10),
]
