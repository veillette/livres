"""Raiponce — découvrir le monde."""
from contes import *

ID = "raiponce"
RAIPONCE = dict(coiffure="longs", cheveux="blond", peau="claire", habit="#9775fa", chaussures="#5f3dc4", acc=("fleur",), couleur_acc="#ff8787")
PRINCE = dict(coiffure="courts", cheveux="noir", peau="doree", habit="#2f9e44", robe=False, jambes="#5c3a1e", cape="#1864ab", acc=("couronne",))
BLOND = "#f6c453"
TX, TY, TH = 520, 780, 520


def raiponce(x, y, s=1.0, **k):
    return personne(x, y, s, **{**RAIPONCE, **k})


def prince(x, y, s=1.0, **k):
    return personne(x, y, s, **{**PRINCE, **k})


def la_sorciere(x, y, s=1.0, **k):
    return sorciere(x, y, s, chapeau="#343a40", **{**dict(habit="#343a40", peau="#d8f5a2", cheveux="gris", motif_robe="#9775fa"), **k})


def foret_tour(S, soir=False, th=TH):
    if soir:
        ciel(S, "#1c2a52", "#5f3dc4")
        etoiles(S, 25, graine=4)
        S.add(lune(120, 110, 40))
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(nuage(160, 110, 0.6))
    for x in (60, 190, 760):
        S.add(sapin(x, 700, 1.4, "#2b8a3e", "#2f9e44"))
    sol(S, 690, "#69db7c" if not soir else "#2f9e44")
    S.add(tour_seule(TX, TY, 1.0, mur="#dee2e6", toit="#5f3dc4", h=th))


def fenetre_haut(th=TH):
    """Point d'où pend la tresse, sous la fenêtre."""
    return TX, TY - th + 110


def tete_fenetre(expr="sourire", th=TH, **k):
    """Raiponce penchée à la fenêtre de la tour."""
    fx, fy = fenetre_haut(th)
    return place(raiponce(0, 0, 0.5, expr=expr, **k), fx, fy + 16)


def tresse_pendue(y_bas=720, th=TH):
    fx, fy = fenetre_haut(th)
    return tresse(fx, fy, fx + 6, y_bas, BLOND, 24)


def echelle_soie(x, y0, y1, couleur="#e64980"):
    m = [trait(x - 26, y0, x - 26, y1, couleur, 5), trait(x + 26, y0, x + 26, y1, couleur, 5)]
    k = y0 + 30
    while k < y1:
        m.append(trait(x - 26, k, x + 26, k, couleur, 5))
        k += 44
    return g(m)


def chambre_tour(S):
    S.add(rect(0, 0, 800, 800, "#e5dbff"))
    for row in range(10):
        for col in range(6):
            S.add(rect(col * 140 - (row % 2) * 70, row * 80, 132, 72, "#d0bfff", rx=6, opacity=0.5))
    S.add(rect(0, 600, 800, 200, "#b197fc"))
    S.add(chemin("M 480 120 L 480 330 L 720 330 L 720 120 Q 600 40 480 120 Z", "#a5d8ff"))
    S.add(chemin("M 480 120 L 480 330 L 720 330 L 720 120 Q 600 40 480 120 Z", "none", stroke="#9775fa", sw=14))


def couverture():
    S = Scene()
    foret_tour(S, th=340)
    S.add(tresse_pendue(760, th=340))
    S.add(tete_fenetre("rire", th=340, bras="salut"))
    S.add(prince(220, 790, 1.3, expr="bouche_bee", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tour_seule(200, 262, 0.35, mur="#dee2e6", toit="#5f3dc4"))
    return S


def p01():
    S = Scene()
    foret_tour(S)
    S.add(tete_fenetre("triste"))
    S.add(la_sorciere(240, 790, 1.3, expr="malin", bras="croises"))
    return S


def p02():
    S = Scene()
    foret_tour(S)
    S.add(tete_fenetre("inquiet"))
    S.add(texte(240, 300, "Pas de porte…", 44, "#5f3dc4", contour="#fff"))
    S.add(texte(240, 380, "pas d'escalier !", 44, "#5f3dc4", contour="#fff"))
    return S


def p03():
    S = Scene()
    foret_tour(S)
    S.add(tresse_pendue(760))
    S.add(tete_fenetre("sourire"))
    S.add(la_sorciere(240, 790, 1.2, expr="furieux", bras="joues"))
    S.add(bulle(240, 400, 400, 100, "Raiponce, descends-moi\ntes cheveux !", 30, pointe=(240, 560)))
    return S


def p04():
    S = Scene()
    foret_tour(S)
    S.add(tresse_pendue(760))
    S.add(tete_fenetre("oups"))
    S.add(la_sorciere(TX + 6, 640, 0.8, expr="concentre", bras="haut"))
    S.add(texte(700, 200, "Aïe !", 60, "#c92a2a", contour="#fff"))
    return S


def p05():
    S = Scene()
    foret_tour(S)
    S.add(tete_fenetre("chante", bras="ouverts"))
    S.add(notes(580, 180, 0.9, "#9775fa"), notes(400, 230, 0.8, "#e64980"))
    S.add(oiseau(680, 300, 0.5, "#4dabf7", expr="content", ailes="haut"), oiseau(380, 350, 0.45, "#ff922b", expr="content", ailes="haut"))
    return S


def p06():
    S = Scene()
    foret_tour(S)
    S.add(tete_fenetre("chante"))
    S.add(notes(420, 180, 0.9, "#9775fa"))
    S.add(prince(190, 700, 0.9, expr="surpris", regard=(1, -1)))
    S.add(cheval(170, 790, 1.4, "#f8f9fa"))
    S.add(bulle(220, 300, 360, 90, "Qui chante si bien ?", 30, pointe=(240, 440)))
    return S


def p07():
    S = Scene()
    foret_tour(S)
    S.add(tresse_pendue(760))
    S.add(tete_fenetre("sourire"))
    S.add(la_sorciere(TX + 6, 520, 0.8, expr="concentre", bras="haut"))
    S.add(prince(170, 790, 1.2, expr="malin", regard=(1, -1)))
    S.add(buisson(170, 800, 1.3, "#2f9e44", "#40c057"))
    return S


def p08():
    S = Scene()
    foret_tour(S, soir=True)
    S.add(tresse_pendue(760))
    S.add(tete_fenetre("surpris"))
    S.add(prince(240, 790, 1.3, expr="rire", bras="joues"))
    S.add(bulle(240, 380, 400, 100, "Raiponce, descends-moi\ntes cheveux !", 30, pointe=(250, 540)))
    return S


def p09():
    S = Scene()
    chambre_tour(S)
    S.add(raiponce(260, 790, 1.4, expr="rire", bras="joues"))
    S.add(prince(540, 790, 1.4, expr="rire", bras="ouverts"))
    S.add(coeur(400, 250, 1.2))
    return S


def p10():
    S = Scene()
    chambre_tour(S)
    S.add(raiponce(260, 790, 1.4, expr="concentre", bras="porte", objet=g([rect(-40, -80, 80, 20, "#e64980", rx=6), rect(-40, -60, 80, 20, "#74c0fc", rx=6)])))
    S.add(echelle_soie(560, 400, 800))
    S.add(bulle(420, 120, 540, 100, "Je vais tresser\nune échelle de soie !", 34, pointe=(280, 460)))
    return S


def p11():
    S = Scene()
    foret_tour(S, soir=True)
    fx, fy = fenetre_haut()
    S.add(echelle_soie(fx + 6, fy + 10, 780))
    S.add(raiponce(fx + 6, 470, 0.8, expr="concentre", bras="haut"))
    S.add(prince(250, 790, 1.3, expr="content", bras="ouverts"))
    return S


def p12():
    S = Scene()
    foret_tour(S)
    S.add(la_sorciere(260, 790, 1.35, expr="furieux", bras="joues"))
    S.add(bulle(250, 360, 420, 100, "Raiponce ?\nRaiponce ?!", 38, pointe=(250, 520)))
    S.add(texte(620, 300, "Personne !", 44, "#5f3dc4", contour="#fff"))
    return S


def p13():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 100, 44))
    collines(S, 600, "#b2f2bb", graine=41)
    sol(S, 600, "#94d82d")
    S.add(chemin("M 0 800 Q 300 640 800 690 L 800 800 Z", "#4dabf7"))
    for k in range(6):
        S.add(fleur(60 + k * 120, 640 + (k % 2) * 20, 0.8, ["#ff8787", "#fcc419", "#cc5de8"][k % 3]))
    S.add(cheval(420, 700, 1.4, "#f8f9fa"))
    S.add(raiponce(260, 790, 1.3, expr="rire", bras="ouverts"))
    S.add(prince(560, 790, 1.2, expr="rire", bras="salut"))
    return S


def p14():
    S = Scene()
    village_(S)
    S.add(raiponce(400, 790, 1.4, expr="chante", bras="ouverts"))
    S.add(notes(300, 360, 1.0, "#9775fa"), notes(480, 330, 0.9, "#e64980"))
    for k, (x, d) in enumerate(((140, dict(coiffure="courts", cheveux="brun", habit="#fa5252", robe=False, peau="brune")),
                                (660, dict(coiffure="tresses", cheveux="noir", habit="#51cf66", peau="doree")))):
        S.add(personne(x, 790, 0.9, expr="content", bras="joues", **d))
    S.cachette(730, 420, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("tour-seule.svg", vignette),
    ("01-la-tour.svg", p01), ("02-pas-de-porte.svg", p02), ("03-tes-cheveux.svg", p03), ("04-aie.svg", p04),
    ("05-elle-chante.svg", p05), ("06-le-prince.svg", p06), ("07-cache.svg", p07), ("08-le-prince-appelle.svg", p08),
    ("09-amis.svg", p09), ("10-l-echelle.svg", p10), ("11-la-descente.svg", p11), ("12-personne.svg", p12),
    ("13-le-monde.svg", p13), ("14-elle-chante.svg", p14),
]
