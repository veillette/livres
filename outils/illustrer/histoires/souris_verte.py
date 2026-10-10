"""Une souris verte — la comptine, version douce, et sa suite.

Jules attrape la souris verte, la montre à trois vieux messieurs qui lui
conseillent un bain moussant (« ça fera un escargot tout chaud » : une
serviette enroulée en coquille), puis cherche où la loger : le tiroir (trop
noir), le chapeau (trop chaud), la poche (une brioche !), et enfin le lit
(« Bonne nuit ! »). Au matin, on recommence.

Plans : 1 large (la prairie) · 2 moyen (dans les mains) · 3 large (le banc
des messieurs) · 4 moyen (le bain dans la tasse) · 5 gros plan (l'escargot
en serviette) · 6 moyen (le tiroir) · 7 large (le chapeau au soleil) ·
8 gros plan (la poche) · 9 moyen (au lit, la nuit) · 10 large (le matin).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne
from objets import tasse

ID = "souris-verte"
PAPIER_PEINT = "fleurs"

JULES = dict(peau="doree", cheveux="noir", coiffure="herisses", habit="#ffd43b", robe=False, jambes="#1971c2", nez="rond")
VERTE = dict(couleur="#51cf66", visage="#ebfbee", acc=("noeud",), couleur_acc="#f783ac")
MONSIEUR_1 = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#495057", robe=False,
                  jambes="#343a40", nez="long", carrure="fine")
MONSIEUR_2 = dict(stature="ancien", peau="foncee", cheveux="gris", coiffure="courts", habit="#2b8a3e", robe=False,
                  jambes="#495057", barbe="#e9ecef", acc=("lunettes",))
MONSIEUR_3 = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve", habit="#a61e4d", robe=False,
                  jambes="#5c3a1e", nez="rond", carrure="ronde")


def jules(x, y, s=1.4, **k):
    return personne(x, y, s, **{**JULES, **k})


def souris(x, y, s=0.4, **k):
    return perso("souris", x, y, s, **{**VERTE, **k})


def melon(c="#343a40"):
    """Chapeau melon (coiffe de personne)."""
    return g([ellipse(0, -190, 70, 12, c), chemin("M -44 -192 Q -46 -250 0 -250 Q 46 -250 44 -192 Z", c),
              rect(-44, -204, 88, 10, "#868e96")])


def beret(c="#1c7ed6"):
    return g([ellipse(0, -196, 62, 22, c), cercle(0, -218, 5, c)])


def dans_les_mains(S, x, y, s, souris_k=None, flip=False, **k):
    """Jules tient la souris sur sa main tendue, à côté de son visage."""
    S.add(jules(x, y, s, bras="donne", flip=flip, **k))
    (gx, gy), (dx, dy) = mains_personne(x, y, s, "donne", flip=flip)
    hx, hy = (gx, gy) if flip else (dx, dy)
    S.add(souris(hx, hy - 8 * s, 0.34 * s, **(souris_k or {})))


def prairie(S, horizon=540, graine=1, haut="#74c0fc", bas="#e7f5ff"):
    paysage(S, horizon, horizon + 70, "#8ce99a", "#b2f2bb", haut, bas, graine=graine, nuages=((620, 130, 0.7),))
    r = random.Random(graine)
    for k in range(9):
        S.add(fleur(r.uniform(20, 780), r.uniform(horizon + 90, 790), r.uniform(0.35, 0.6), r.choice(("#ff8787", "#ffd43b", "#cc5de8", "#fff"))))


def herbes_hautes(S, graine=3, y0=700, cotes=True):
    r = random.Random(graine)
    for k in range(16):
        x = r.uniform(-20, 160) if (k % 2 or not cotes) else r.uniform(640, 820)
        S.add(touffe(x, r.uniform(y0, 820), r.uniform(1.6, 2.6), "#2f9e44", graine=graine + k))


def banc(x, y, s=1.0):
    """Banc public vert ; (x, y) = milieu du pied, assise à y - 90 s."""
    bois = "#2b8a3e"
    m = [ellipse(0, 4, 260, 12, "#000", opacity=0.1)]
    for dx in (-200, 200):
        m.append(rect(dx - 8, -90, 16, 90, "#343a40", rx=4))
    m += [rect(-240, -100, 480, 22, volume(bois, 0.35, 0.75), rx=6),
          rect(-240, -190, 480, 20, volume(bois, 0.35, 0.75), rx=6), rect(-240, -160, 480, 20, volume(bois, 0.35, 0.75), rx=6),
          rect(-216, -190, 12, 100, "#343a40", rx=4), rect(204, -190, 12, 100, "#343a40", rx=4)]
    return place(m, x, y, s)


def escargot_serviette(x, y, s=1.0, expr="rire"):
    """La souris roulée dans une serviette en coquille d'escargot ; (x, y) = au sol."""
    rose, raie = "#ffc9c9", "#ffffff"
    m = [chemin("M -70 0 Q -74 -24 -40 -24 L 60 -26 Q 80 -26 84 -10 Q 84 0 60 0 Z", volume("#ebfbee", 0.35, 0.85)),
         cercle(-6, -74, 62, volume(rose, 0.4, 0.75)),
         chemin("M -6 -74 m 0 -8 a 8 8 0 1 1 -8 8 a 18 18 0 1 1 18 18 a 30 30 0 1 1 -30 -30 a 44 44 0 1 1 44 44",
                stroke=raie, sw=9),
         chemin("M -6 -74 m 0 -8 a 8 8 0 1 1 -8 8 a 18 18 0 1 1 18 18 a 30 30 0 1 1 -30 -30 a 44 44 0 1 1 44 44",
                stroke="#ff8787", sw=3, transform="translate(3 4)"),
         chemin("M -56 -10 l -6 14 M -40 -8 l -4 14 M -24 -6 l -2 14", stroke="#ffa8a8", sw=4)]
    contenu = avec_contour(m, s, 0.35)
    tete = perso("souris", 0, 0, 1.0, expr=expr, **{k: v for k, v in VERTE.items()}, ombre=False)
    # la tête seule dépasse : on ne garde que le haut du personnage, posé à droite
    cid = uid("c")
    tete = el("clipPath", rect(-120, -260, 240, 150, "#000"), id=cid) + g(tete, clip_path=f"url(#{cid})")
    contenu += place(tete, 80, 31, 0.62)
    return place(contenu, x, y, s) + occuper(x - 80 * s, y - 140 * s, x + 130 * s, y)


def bain_tasse(x, y, s=1.0):
    """La souris dans une tasse pleine de mousse ; (x, y) = pied de la tasse."""
    m = [ellipse(0, 4, 110, 16, "#e9ecef"), ellipse(0, 4, 96, 10, "#fff"),
         chemin("M -80 -110 Q -80 0 0 0 Q 80 0 80 -110 Z", volume("#74c0fc", 0.35, 0.75)),
         chemin("M 78 -90 Q 130 -90 120 -50 Q 112 -24 70 -30", stroke="#4dabf7", sw=14),
         ellipse(0, -110, 80, 16, "#d0ebff")]
    contenu = avec_contour(m, s, 0.35)
    contenu += place(perso("souris", 0, 0, 1.0, expr="rire", bras="haut", **VERTE, ombre=False), 0, -60, 0.55)
    mousse = []
    r = random.Random(4)
    for k in range(14):
        mousse.append(cercle(-70 + k * 11, -110 + r.uniform(-14, 8), r.uniform(12, 20), "#fff", stroke="#e7f5ff", stroke_width=2))
    for bx, by, br in ((60, -170, 10), (90, -210, 7), (-60, -190, 8), (20, -240, 6)):
        mousse.append(cercle(bx, by, br, "#e7f5ff", opacity=0.7, stroke="#fff", stroke_width=2))
    contenu += g(mousse)
    return place(contenu, x, y, s) + occuper(x - 120 * s, y - 180 * s, x + 130 * s, y)


def commode(x, y, s=1.0, ouvert=True, devant=False):
    """Commode en bois, le tiroir du haut tiré ; (x, y) = milieu du pied."""
    bois = "#c68642"
    if devant:
        # la façade du tiroir tiré, à poser par-dessus ce qu'il contient
        return place([rect(-190, -186, 380, 86, volume(eclaircir(bois, 0.15), 0.3, 0.8), rx=4, stroke=_assombrir(bois, 0.75), stroke_width=3),
                      ellipse(0, -143, 26, 9, "#868e96")], x, y, s)
    m = [ellipse(0, 4, 190, 12, "#000", opacity=0.12), rect(-170, -300, 340, 300, volume(bois, 0.3, 0.8), rx=8),
         rect(-180, -316, 360, 22, volume(_assombrir(bois, 0.9), 0.35, 0.75), rx=6)]
    for k, yy in enumerate((-280, -190, -100)):
        if k == 0 and ouvert:
            m.append(rect(-150, yy, 300, 76, "#2b2b3a", rx=4))
            continue
        m += [rect(-150, yy, 300, 76, volume(eclaircir(bois, 0.15), 0.3, 0.8), rx=4, stroke=_assombrir(bois, 0.75), stroke_width=3),
              ellipse(0, yy + 38, 22, 8, "#868e96")]
    if ouvert:
        m.append(poly([(-170, -270), (170, -270), (190, -186), (-190, -186)], "#1b1f3b"))
    return place(m, x, y, s)


def brioche(x, y, s=1.0):
    return place([ellipse(0, 0, 30, 20, volume("#e8a33d", 0.45, 0.7)), cercle(0, -20, 14, volume("#e8a33d", 0.45, 0.7)),
                  ellipse(-8, -4, 6, 3, "#fff", opacity=0.5)], x, y, s)


def chambre(S, nuit_=False):
    piece(S, "chambre", 580)
    dehors = g([rect(0, 0, 800, 800, "#1c2a52" if nuit_ else "#a5d8ff")] +
               ([lune(560, 160, 24, halo=False)] if nuit_ else [nuage(580, 170, 0.4)]))
    S.add(fenetre(470, 90, 180, 160, "#a5d8ff", rideaux="#ffd43b", contenu=dehors))
    if nuit_:
        S.ambiance("nuit")


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    prairie(S, 560, graine=2)
    dans_les_mains(S, 330, 800, 2.1, souris_k=dict(expr="rire", bras="salut"), expr="rire", regard=(1, -0.3))
    S.add(escargot(650, 780, 0.9, expr="content", flip=True, regard=(-1, 0)))
    herbes_hautes(S, 4, 740)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(souris(200, 255, 0.95, expr="rire", bras="salut"))
    return S


def p01():
    """Plan large : la souris verte court dans l'herbe."""
    S = Scene()
    prairie(S, 520, graine=3)
    S.add(arbre(640, 620, 1.2, fruits="#fa5252"))
    S.add(souris(300, 720, 0.75, expr="rire", bras="court"))
    S.add(mouvement(190, 650, 0.9, "#2b8a3e", rot=180))
    S.add(jules(620, 790, 1.5, expr="surpris", bras="bas", regard=(-1, 0.3)))
    herbes_hautes(S, 5, 730)
    return S


def p02():
    """Plan moyen : dans les mains de Jules ; « un, deux ! »."""
    S = Scene()
    prairie(S, 500, graine=4)
    dans_les_mains(S, 330, 810, 2.3, souris_k=dict(expr="rire", bras="haut"), expr="content", regard=(1, -0.3))
    S.add(texte(170, 230, "Un…", 60, "#2b8a3e", contour="#fff"))
    S.add(texte(620, 230, "deux !", 60, "#2b8a3e", contour="#fff"))
    herbes_hautes(S, 6, 750)
    return S


def p03():
    """Plan large : trois messieurs sur un banc, dans le parc."""
    S = Scene()
    prairie(S, 500, graine=5)
    S.add(arbre(110, 610, 1.1))
    S.add(banc(470, 690, 0.9))
    S.add(personne(330, 690, 1.0, expr="surpris", regard=(-1, 0.2), coiffe=melon(), **MONSIEUR_1))
    S.add(personne(470, 690, 1.0, expr="bouche_bee", regard=(-1, 0.2), **MONSIEUR_2))
    S.add(personne(610, 690, 1.0, expr="content", regard=(-1, 0.2), coiffe=beret(), **MONSIEUR_3))
    dans_les_mains(S, 150, 790, 1.3, souris_k=dict(expr="content", bras="salut"), expr="fier", regard=(1, 0))
    return S


def p04():
    """Plan moyen : la souris dans un bain moussant, dans une tasse posée sur le banc."""
    S = Scene()
    prairie(S, 480, graine=6)
    S.add(banc(400, 720, 1.1))
    S.add(personne(150, 720, 1.25, expr="rire", bras="designe", regard=(1, 0.2), coiffe=melon(), **MONSIEUR_1))
    S.add(personne(660, 720, 1.25, expr="content", bras="applaudit", regard=(-1, 0.2), coiffe=beret(), **MONSIEUR_3))
    S.add(bain_tasse(400, 610, 1.0))
    S.add(bulle(400, 130, 520, 110, "Trempez-la dans la mousse !\nTrempez-la dans l'eau !", 32, pointe=(220, 420)))
    return S


def p05():
    """Gros plan : la souris roulée dans sa serviette, comme un escargot, à côté d'un vrai escargot."""
    S = Scene()
    prairie(S, 500, graine=7)
    S.add(escargot_serviette(290, 700, 1.3))
    S.add(escargot(610, 700, 1.0, expr="surpris", flip=True, regard=(-1, 0)))
    S.camera(1.35, 450, 590)
    S.dessus(texte(400, 120, "Un escargot tout chaud !", 50, "#e64980", contour="#fff"))
    return S


def p06():
    """Plan moyen : dans le tiroir de la commode, il fait trop noir."""
    S = Scene()
    chambre(S)
    S.add(commode(310, 760, 1.25))
    S.add(souris(310, 760 - 140 * 1.25, 0.62, expr="inquiet", bras="joues"))
    S.add(commode(310, 760, 1.25, devant=True))
    S.add(jules(640, 790, 1.7, expr="oups", bras="bouche", regard=(-1, 0)))
    S.add(bulle(330, 150, 400, 90, "Il fait trop noir !", 38, pointe=(320, 470)))
    return S


def p07():
    """Plan large : au jardin, en plein soleil, la souris a trop chaud dans le chapeau."""
    S = Scene()
    prairie(S, 540, graine=8, haut="#4dabf7", bas="#fff3bf")
    S.add(soleil(660, 130, 70, visage=True))
    S.add(jules(300, 800, 1.9, expr="inquiet", bras="porte", regard=(0.5, -0.4)))
    (gx, gy), (dx, dy) = mains_personne(300, 800, 1.9, "porte")
    cx = (gx + dx) / 2
    S.add(souris(cx, gy - 10, 0.55, expr="oups", bras="joues"))
    S.add(chapeau(cx, gy + 20, 1.6, "#f6d38b", "#e03131", rot=180, fleur_=False))
    for k in range(3):
        S.add(goutte(cx + 56 + k * 16, gy - 120 + k * 24, 0.8, "#74c0fc"))
    S.add(bulle(570, 330, 380, 90, "Il fait trop chaud !", 36, pointe=(370, 520)))
    herbes_hautes(S, 9, 740)
    return S


def p08():
    """Gros plan : dans la poche de Jules, la souris a trouvé une brioche."""
    S = Scene()
    prairie(S, 480, graine=10)
    poche = g([rect(-24, -82, 48, 36, "#fcc419", rx=8, stroke="#f08c00", stroke_width=2), rect(-24, -82, 48, 6, "#f08c00", rx=3)])
    x, y, s = 400, 900, 2.6
    S.add(jules(x, y, s, expr="rire", bras="bas", regard=(0, 0.6), tenue=g([])))
    S.add(souris(x + 2 * s, y - 70 * s, 0.32 * s, expr="miam", bras="porte", objet=brioche(0, -74, 0.9)))
    S.add(place(poche, x, y, s))
    S.dessus(bulle(600, 380, 260, 90, "Miam !", 44, pointe=(440, 560)))
    return S


def p09():
    """Plan moyen : la nuit, Jules au lit ; la souris dort dans une boîte d'allumettes."""
    S = Scene()
    chambre(S, nuit_=True)
    S.add(lit(330, 760, 400, couverture="#ffd43b"))
    S.add(jules(355, 635, 1.0, expr="dort", rot=-90, ombre=False))
    couverture_ = rect(255, 622, 275, 98, lineaire([(0, "#ffe066"), (1, "#f08c00")]), rx=18)
    S.add(couverture_, chemin("M 300 630 q 10 30 0 80 M 420 628 q -8 34 4 84", stroke="#e8590c", sw=2.5, opacity=0.5))
    S.add(rect(600, 610, 160, 150, volume("#c68642", 0.3, 0.8), rx=6))
    S.add(lampe(700, 610, 0.6))
    S.add(rect(596, 566, 110, 44, "#e03131", rx=4), rect(602, 572, 98, 34, "#fff4e6", rx=3))
    S.add(souris(628, 600, 0.34, expr="dort", bras="bas"))
    S.add(rect(600, 580, 102, 26, "#74c0fc", rx=8), chemin("M 610 588 h 86", stroke="#fff", sw=3, opacity=0.6))
    S.add(zzz(640, 500, 0.8, "#fff3bf"))
    S.add(bulle(330, 230, 340, 90, "Bonne nuit !", 40, pointe=(620, 550)))
    S.camera(1.15, 420, 560)
    return S


def p10():
    """Plan large : au matin, la souris court de nouveau dans l'herbe ; Jules la suit."""
    S = Scene()
    prairie(S, 520, graine=11, haut="#a5d8ff", bas="#fff9db")
    S.add(soleil(140, 140, 50))
    S.add(souris(560, 720, 0.75, expr="rire", bras="court"))
    S.add(jules(260, 790, 1.6, expr="rire", bras="court", regard=(1, 0)))
    S.add(texte(560, 330, "On recommence ?", 50, "#2b8a3e", contour="#fff"))
    herbes_hautes(S, 12, 740)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("souris-seule.svg", vignette),
    ("01-dans-l-herbe.svg", p01), ("02-un-deux.svg", p02), ("03-ces-messieurs.svg", p03),
    ("04-la-mousse.svg", p04), ("05-escargot.svg", p05), ("06-le-tiroir.svg", p06),
    ("07-le-chapeau.svg", p07), ("08-la-poche.svg", p08), ("09-bonne-nuit.svg", p09),
    ("10-on-recommence.svg", p10),
]
