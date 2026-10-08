"""Le cardinal rouge — l'oiseau du Kentucky au fil des saisons.

Faits retenus : le cardinal rouge ne migre pas ; le mâle est rouge vif avec
un masque noir, la femelle brun-beige avec des touches de rouge et un bec
orangé ; les deux chantent ; le mâle offre des graines à la femelle bec à
bec ; la femelle bâtit le nid dans un buisson dense et couve 3 œufs
environ 12 jours ; les deux parents nourrissent les petits d'insectes ;
les jeunes quittent le nid vers 10 jours, bruns avec un bec foncé, et les
jeunes mâles deviennent rouges à l'automne. Le mâle attaque parfois son
reflet dans une vitre.
"""
from base import *
from objets import *
from fantastique import personne

ID = "cardinal-rouge"
ROUGE = "#e03131"
BRUN = "#c9a37a"
JEUNE = "#a68a6d"
MAYA = dict(peau="claire", cheveux="noir", coiffure="queue", habit="#4c6ef5", robe=False, jambes="#495057")


def cardinal(x, y, s=1.0, sexe="male", flip=False, bec_ouvert=False, expr="sourire", vol=False, regard=(1, 0), rot=0):
    """Cardinal de profil, tête à droite ; (x, y) = sous les pattes."""
    if sexe == "male":
        corps, aile, queue, bec, masque, huppe = ROUGE, "#c92a2a", "#c92a2a", "#ff6b6b", ENCRE, ROUGE
    elif sexe == "femelle":
        corps, aile, queue, bec, masque, huppe = BRUN, "#e8590c", "#e8590c", "#ff922b", "#868e96", "#f08c00"
    else:
        corps, aile, queue, bec, masque, huppe = JEUNE, "#8d6e52", "#8d6e52", "#495057", JEUNE, JEUNE
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    # queue
    m.append(chemin("M -30 -40 L -110 -2 L -100 14 L -20 -24 Z", queue))
    # pattes
    if not vol:
        for dx in (-6, 12):
            m.append(trait(dx, -24, dx - 2, 0, "#c2255c", 4))
    # corps et tête
    m.append(ellipse(0, -46, 46, 32, corps, rot=-15))
    m.append(cercle(34, -86, 26, corps))
    m.append(poly([(18, -104), (-12, -140), (34, -110)], huppe))
    # aile
    if vol:
        m.append(chemin("M -10 -60 Q -40 -150 30 -150 Q 20 -100 20 -60 Z", aile))
    else:
        m.append(ellipse(-12, -48, 34, 18, aile, rot=-18))
        for k in range(3):
            m.append(trait(-34 + k * 10, -44 + k * 2, -10 + k * 10, -48, eclaircir(aile, 0.25), 2))
    # masque, bec, œil
    m.append(chemin("M 36 -98 Q 54 -104 66 -94 L 66 -72 Q 54 -60 42 -68 Q 30 -84 36 -98 Z", masque))
    if bec_ouvert:
        m.append(poly([(58, -92), (86, -88), (60, -82)], bec))
        m.append(poly([(58, -80), (82, -74), (58, -72)], _sombre(bec)))
    else:
        m.append(poly([(58, -94), (88, -82), (58, -72)], bec))
    m.append(cercle(44, -88, 9, "#ffffff" if masque == ENCRE else corps))
    m.append(place(oeil(0, 0, ys, regard, taille=0.65), 44, -88))
    if ss:
        m.append(place(sourcils(0, 0, ss), 42, -88, 0.5))
    return place(m + [occuper(-110, -140, 88, 14)], x, y, s, flip=flip, rot=rot)


def _sombre(c):
    return "#" + "".join("%02x" % int(int(c[i:i + 2], 16) * 0.8) for i in (1, 3, 5))


def branche(x0, y0, x1, y1, ep=16, neige=False, feuilles=None, graine=1):
    m = [chemin(f"M {x0} {y0} Q {(x0 + x1) / 2} {(y0 + y1) / 2 + 20} {x1} {y1}", stroke="#7c4a1e", sw=ep)]
    if neige:
        m.append(chemin(f"M {x0} {y0 - ep * 0.6} Q {(x0 + x1) / 2} {(y0 + y1) / 2 + 20 - ep * 0.6} {x1} {y1 - ep * 0.6}", stroke="#ffffff", sw=ep * 0.7))
    if feuilles:
        r = random.Random(graine)
        for k in range(7):
            t = (k + 0.5) / 7
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t + 20 * 4 * t * (1 - t) / 2
            m.append(ellipse(x, y - 14, 18, 9, r.choice(feuilles), rot=r.uniform(-60, 60)))
    return g(m)


def arbre_nu(x, y, s=1.0, neige=False):
    """Arbre sans feuilles (fin d'hiver) ; (x, y) = pied du tronc."""
    m = [chemin("M -26 0 L -14 -260 L 14 -260 L 26 0 Z", "#7c4a1e")]
    for x0, y0, x1, y1, ep in ((-8, -200, -120, -330, 14), (8, -230, 130, -350, 14), (0, -250, -20, -400, 12),
                                (-70, -270, -150, -280, 8), (80, -300, 170, -300, 8), (-12, -340, 50, -420, 8)):
        m.append(trait(x0, y0, x1, y1, "#7c4a1e", ep))
        if neige:
            m.append(trait(x0, y0 - ep * 0.5, x1, y1 - ep * 0.5, "#ffffff", ep * 0.5))
    return place(m, x, y, s)


def mangeoire(x, y, s=1.0, graines=True):
    """Mangeoire suspendue ; (x, y) = point d'accroche en haut."""
    m = [trait(0, 0, 0, 40, "#495057", 3),
         poly([(-90, 70), (0, 30), (90, 70)], "#c92a2a"),
         rect(-60, 70, 120, 80, "#d0ebff", opacity=0.8, stroke="#adb5bd", stroke_width=3),
         rect(-90, 150, 180, 18, "#a0693a", rx=4)]
    if graines:
        r = random.Random(3)
        for _ in range(20):
            m.append(ellipse(r.uniform(-50, 50), r.uniform(100, 145), 5, 3, "#343a40", rot=r.uniform(0, 180)))
        for _ in range(8):
            m.append(ellipse(r.uniform(-80, 80), 148, 5, 3, "#343a40", rot=r.uniform(0, 180)))
    return place(m, x, y, s)


def nid(x, y, s=1.0, contenu=None):
    m = [ellipse(0, 0, 80, 34, "#8d6e4a"), ellipse(0, -10, 62, 20, "#5c3a1e")]
    if contenu:
        m.append(contenu)
    for k in range(9):
        a = math.radians(180 + k * 20)
        m.append(trait(math.cos(a) * 80, math.sin(a) * 10 + 4, math.cos(a + 0.5) * 70, 26, "#a0693a", 3))
    m.append(chemin("M -80 0 Q 0 46 80 0", stroke="#7c4a1e", sw=6))
    return place(m, x, y, s)


def oeufs():
    m = []
    for dx in (-30, 0, 30):
        m.append(ellipse(dx, -16, 15, 19, "#f1f3f5", stroke="#dee2e6", stroke_width=2))
        m += [cercle(dx - 5, -20, 2.5, "#a68a6d"), cercle(dx + 5, -10, 2, "#868e96"), cercle(dx + 2, -26, 2, "#a68a6d")]
    return g(m)


def oisillon(x, y, s=1.0):
    return place([ellipse(0, 0, 22, 18, "#ced4da"), cercle(0, -18, 14, "#ced4da"),
                  poly([(-12, -30), (0, -58), (12, -30)], "#ffd43b"), poly([(-9, -30), (0, -46), (9, -30)], "#ff922b"),
                  cercle(-6, -20, 2.5, ENCRE), cercle(6, -20, 2.5, ENCRE)], x, y, s)


def chenille_verte(x, y, s=1.0):
    return place([cercle(k * 7, 0, 5, "#82c91e") for k in range(5)], x, y, s)


def paysage_neige(S, graine=1):
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(rect(0, 600, 800, 200, "#f8f9fa"))
    for x in (90, 690):
        S.add(sapin(x, 640, 1.0, neige=True))
    flocons(S, 30, graine, zone=(0, 0, 800, 600))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    paysage_neige(S, 2)
    S.add(branche(-20, 560, 820, 520, 26, neige=True))
    S.add(cardinal(380, 545, 2.6, expr="content"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(branche(20, 250, 380, 240, 14))
    S.add(cardinal(190, 245, 1.7, expr="content"))
    return S


def p01():
    S = Scene()
    paysage_neige(S, 3)
    S.add(arbre_nu(590, 650, 1.3, neige=True))
    S.add(branche(0, 420, 520, 380, 20, neige=True))
    S.add(cardinal(300, 400, 1.9, expr="sourire"))
    return S


def p02():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", y=640)
    dehors = g([rect(80, 80, 640, 470, "#e7f5ff"), rect(80, 470, 640, 80, "#f8f9fa"), sapin(170, 520, 0.8, neige=True),
                mangeoire(500, 80, 1.2),
                cardinal(440, 278, 0.9, expr="miam"), cardinal(590, 278, 0.85, "femelle", flip=True, regard=(1, 0))])
    S.add(fenetre(80, 80, 640, 470, "#e7f5ff", "#ffffff", contenu=dehors))
    S.add(personne(230, 800, 1.25, **MAYA, expr="rire", bras="montre", regard=(1, -1)))
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 640, "#b2f2bb", graine=3)
    S.add(rect(0, 620, 800, 180, "#d8f5a2"))
    S.add(arbre_nu(400, 720, 1.5))
    S.add(branche(380, 260, 640, 210, 14))
    S.add(cardinal(520, 236, 1.3, bec_ouvert=True, expr="chante", regard=(1, -1)))
    S.add(notes(640, 120, 1.0, ROUGE))
    S.add(texte(600, 90, "Tiou ! Tiou !", 44, ROUGE, contour="#fff"))
    S.add(branche(150, 470, 400, 450, 12))
    S.add(cardinal(240, 455, 1.0, "femelle", bec_ouvert=True, expr="chante"))
    S.add(notes(120, 380, 0.7, "#e8590c"))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff0f6")
    S.add(arbre(120, 760, 1.6, "#ffc9c9", "#fcc2d7", "#7c4a1e"))
    S.add(branche(-20, 560, 820, 530, 22, feuilles=("#8ce99a", "#69db7c")))
    S.add(cardinal(310, 548, 1.6, bec_ouvert=False, expr="content"))
    S.add(cardinal(490, 545, 1.6, "femelle", flip=True, bec_ouvert=True, expr="content"))
    S.add(ellipse(440, 412, 6, 4, "#343a40"))
    S.add(coeur(400, 260, 1.2, "#ff8787"))
    S.cachette(70, 390, "air")
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(rect(0, 640, 800, 160, "#8ce99a"))
    S.add(buisson(400, 720, 3.2, "#2f9e44", "#40c057"))
    S.add(nid(400, 520, 1.3))
    S.add(cardinal(560, 470, 1.2, "femelle", flip=True, expr="concentre"))
    S.add(trait(470, 400, 520, 384, "#a0693a", 4))
    S.add(cardinal(150, 300, 0.9, vol=True, expr="sourire"))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(rect(0, 640, 800, 160, "#8ce99a"))
    S.add(buisson(400, 760, 3.4, "#2f9e44", "#40c057"))
    S.add(loupe_oeufs(S))
    S.add(cardinal(560, 760 - 270, 1.3, "femelle", expr="dort"))
    S.add(cardinal(220, 300, 1.0, bec_ouvert=False, expr="sourire", vol=True))
    S.add(chenille_verte(300, 222, 1.0))
    return S


def loupe_oeufs(S):
    from animaux import loupe
    return loupe(260, 560, 120, g([rect(140, 440, 240, 240, "#d3f9d8"), nid(260, 600, 1.3, oeufs())]), rot=140)


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(buisson(400, 820, 4.0, "#2f9e44", "#40c057"))
    petits = g([oisillon(-40, -24, 1.3), oisillon(0, -30, 1.4), oisillon(40, -24, 1.3)])
    S.add(nid(400, 520, 1.6, petits))
    S.add(cardinal(200, 470, 1.4, expr="content", bec_ouvert=True))
    S.add(chenille_verte(330, 380, 1.4))
    S.add(cardinal(620, 470, 1.4, "femelle", flip=True, expr="content", bec_ouvert=True))
    S.add(texte(400, 160, "Cui ! Cui !", 60, "#e8590c", contour="#fff"))
    S.cachette(730, 590, "air")
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, 600, 800, 200, "#8ce99a"))
    S.add(rect(400, 100, 400, 520, "#ffe8cc"), poly([(380, 110), (600, 0), (820, 110)], "#c92a2a"))
    S.add(rect(452, 232, 276, 296, "#ffffff", rx=6), rect(470, 250, 240, 260, "#d0ebff"))
    S.add(g(cardinal(600, 460, 1.3, flip=True, vol=True, expr="fache"), opacity=0.5))
    S.add(rect(486, 262, 40, 236, "#ffffff", opacity=0.35))
    S.add(rect(586, 250, 8, 260, "#ffffff"))
    S.add(cardinal(340, 460, 1.3, vol=True, expr="fache"))
    S.add(texte(250, 220, "Toc ! Toc !", 50, ROUGE, contour="#fff", rot=-8))
    S.add(buisson(560, 640, 1.4))
    return S


def p09():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 620, 800, 180, "#8ce99a"))
    herbe_ = [herbe(40 + k * 60, 640 + (k % 3) * 30, 1.0) for k in range(13)]
    S.add(g(herbe_))
    S.add(cardinal(560, 690, 1.5, expr="content", flip=True, regard=(1, 1)))
    S.add(cardinal(230, 690, 1.2, "jeune", expr="surpris", regard=(1, 1)))
    S.add(cardinal(360, 720, 1.1, "jeune", expr="content", regard=(1, 1)))
    for k in range(5):
        S.add(ellipse(440 + k * 18, 720, 5, 3, "#343a40"))
    S.add(soleil(680, 100, 45))
    return S


def p10():
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    S.add(rect(0, 640, 800, 160, "#e9c46a"))
    S.add(arbre(650, 720, 1.6, "#ff922b", "#f76707", "#7c4a1e"), arbre(140, 700, 1.2, "#fcc419", "#fab005", "#7c4a1e"))
    S.add(branche(-20, 480, 820, 460, 20, feuilles=("#ff922b", "#fab005", "#e8590c")))
    S.add(cardinal(240, 468, 1.4, "jeune", expr="content"))
    S.add(cardinal(420, 466, 1.4, "male", expr="fier"))
    S.add(cardinal(600, 466, 1.4, "femelle", flip=True, expr="content"))
    S.add(feuille_tombe(330, 650), feuille_tombe(520, 600))
    return S


def feuille_tombe(x, y):
    return ellipse(x, y, 16, 8, "#e8590c", rot=30)


def p11():
    S = Scene()
    paysage_neige(S, 4)
    S.add(maison(170, 640, 1.4, "#ffe8cc", "#1971c2", lumiere=True))
    S.add(trait(360, 160, 760, 160, "#7c4a1e", 14))
    S.add(mangeoire(560, 160, 1.4))
    S.add(cardinal(470, 395, 0.9, expr="content"))
    S.add(cardinal(650, 395, 0.9, "femelle", flip=True))
    S.add(cardinal(420, 640, 1.0, expr="content"))
    S.add(cardinal(560, 650, 1.0, "femelle", expr="sourire"))
    S.add(cardinal(690, 650, 1.0, flip=True, expr="sourire"))
    S.add(personne(240, 800, 1.0, **{**MAYA, "habit": "#c92a2a"}, expr="rire", bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cardinal-seul.svg", vignette),
    ("01-dans-la-neige.svg", p01), ("02-la-mangeoire.svg", p02), ("03-le-chant.svg", p03),
    ("04-bec-a-bec.svg", p04), ("05-le-nid.svg", p05), ("06-les-oeufs.svg", p06),
    ("07-les-oisillons.svg", p07), ("08-le-reflet.svg", p08), ("09-les-jeunes.svg", p09),
    ("10-l-automne.svg", p10), ("11-l-hiver-revient.svg", p11),
]
