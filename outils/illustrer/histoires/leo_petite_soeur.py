"""Et moi, alors ? — Léo et sa petite sœur : la jalousie d'un grand frère.

Léo attend sa petite sœur avec impatience : il va enfin avoir quelqu'un pour
jouer au ballon. Mais Rose arrive, tout le monde se penche sur elle, elle
pleure, elle dort, on dit « Chut, Léo ! »… Léo est fâché, fait le bébé à son
tour. Maman le prend sur ses genoux : l'amour, c'est comme le soleil, il y
en a pour tout le monde. Léo apprend à aider, chante pour Rose, a son moment
rien qu'à lui avec Papa… et Rose lui serre le doigt en souriant.

Plans : 1 moyen (on prépare le couffin) · 2 large (l'arrivée) · 3 moyen (les
visiteurs) · 4 gros plan (Ouiiin !) · 5 moyen (Chut, Léo !) · 6 moyen (la
colère dans la chambre) · 7 moyen (moi aussi, je suis un bébé) · 8 moyen
(sur le canapé) · 9 moyen (il chante) · 10 large (rien que nous deux) · 11
gros plan (elle m'a souri) · 12 moyen (je t'apprendrai).
"""
from base import *
from base import _assombrir
from objets import ballon_jeu, nuage_orage
from fantastique import personne, mains_personne

ID = "leo-petite-soeur"

LEO = dict(peau="doree", cheveux="brun", coiffure="boucles", habit="#4dabf7", robe=False, jambes="#495057")
MAMAN = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="longs", habit="#e599f7", robe=True, nez="petit", yeux="cils")
PAPA = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="courts", habit="#69db7c", robe=False, jambes="#364fc7",
            barbe="#e8590c", nez="rond", carrure="ronde")
MAMIE = dict(stature="ancien", peau="doree", cheveux="blanc", coiffure="chignon", habit="#ffa94d", robe=True, acc=("lunettes",))
PEAU_ROSE = "#f0c39a"


def leo(x, y, s=1.3, **k):
    return personne(x, y, s, **{**LEO, **k})


def maman(x, y, s=1.25, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def papa(x, y, s=1.25, **k):
    return personne(x, y, s, **{**PAPA, **k})


def bebe(x, y, s=1.0, rot=0, expr="dort", couverture="#ffc9c9"):
    """Rose, emmaillotée dans sa couverture ; (x, y) = centre, tête à gauche."""
    m = [ellipse(14, 0, 46, 25, volume(couverture, 0.3, 0.8)),
         chemin("M -10 -22 Q 10 0 -6 24", stroke=_assombrir(couverture, 0.8), sw=3),
         chemin("M -42 -18 Q -20 -30 -8 -18 L -8 18 Q -24 28 -42 18 Z", eclaircir(couverture, 0.3)),
         cercle(-28, -1, 18, volume(PEAU_ROSE, 0.3, 0.85)),
         chemin("M -36 -17 Q -30 -24 -24 -18", stroke="#4a2c17", sw=3),
         cercle(-38, 6, 4, "#ffa8a8", opacity=0.6), cercle(-18, 6, 4, "#ffa8a8", opacity=0.6)]
    if expr == "dort":
        m += [chemin("M -36 -2 q 3 3 6 0 M -26 -2 q 3 3 6 0", stroke=ENCRE, sw=1.8), chemin("M -31 7 q 3 2 6 0", stroke=ENCRE, sw=1.6)]
    elif expr == "pleure":
        m += [chemin("M -36 -3 q 3 -3 6 0 M -26 -3 q 3 -3 6 0", stroke=ENCRE, sw=1.8), ellipse(-28, 8, 5, 6, "#c92a2a"),
              chemin("M -38 0 q -3 6 -1 10", stroke="#74c0fc", sw=2.5)]
    else:
        m += [cercle(-33, -2, 2.4, ENCRE), cercle(-23, -2, 2.4, ENCRE), chemin("M -33 6 Q -28 11 -23 6", stroke=ENCRE, sw=1.8)]
    m.append(cercle(-8, 10, 6, PEAU_ROSE))
    return place(m, x, y, s, rot=rot) + occuper(x - 46 * s, y - 26 * s, x + 60 * s, y + 26 * s)


def bebe_dans_les_bras(S, x, y, s, perso_k, expr_bebe="dort", flip=False):
    """Un adulte (personne) qui berce Rose : le bébé posé entre ses mains."""
    S.add(personne(x, y, s, bras="porte", flip=flip, **perso_k))
    (gx, gy), (dx, dy) = mains_personne(x, y, s, "porte", flip=flip, stature=perso_k.get("stature", "enfant"))
    S.add(bebe((gx + dx) / 2, (gy + dy) / 2 - 18 * s, 0.95 * s, rot=-8 if not flip else 8, expr=expr_bebe))


def couffin(x, y, s=1.0, bebe_expr=None, couleur="#e9c46a", drap="#fff0f6"):
    """Couffin d'osier sur son pied ; (x, y) = au sol."""
    m = [trait(-50, 0, 40, -120, "#c68642", 8), trait(50, 0, -40, -120, "#c68642", 8),
         ellipse(0, -130, 92, 22, drap)]
    if bebe_expr:
        m.append(bebe(0, -140, 0.8, expr=bebe_expr))
    m += [chemin("M -96 -136 Q -90 -84 0 -80 Q 90 -84 96 -136 Q 0 -120 -96 -136 Z", volume(couleur, 0.3, 0.8))]
    for k in range(-4, 5):
        m.append(trait(k * 20, -128, k * 19, -84, _assombrir(couleur, 0.8), 2, opacity=0.6))
    m.append(chemin("M -96 -136 Q 0 -120 96 -136", stroke=_assombrir(couleur, 0.75), sw=4))
    return place(m, x, y, s)


def canape(x, y, w=420, couleur="#748ffc", dossier=True, assise=True):
    """Canapé vu de face ; (x, y) = au sol, au milieu. dossier / assise : pour
    poser des personnages « assis » entre les deux."""
    m = []
    if dossier:
        m += [rect(x - w / 2, y - 210, w, 120, volume(couleur, 0.3, 0.8), rx=30)]
    if assise:
        m += [rect(x - w / 2 + 10, y - 110, w - 20, 70, volume(couleur, 0.25, 0.75), rx=18),
              rect(x - w / 2 - 30, y - 150, 60, 140, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=24),
              rect(x + w / 2 - 30, y - 150, 60, 140, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=24),
              rect(x - w / 2 + 20, y - 40, 20, 40, "#8d5524"), rect(x + w / 2 - 40, y - 40, 20, 40, "#8d5524")]
    return g(m)


def tambour(x, y, s=1.0):
    return place([ellipse(0, 0, 46, 14, "#f8f9fa", stroke="#c92a2a", stroke_width=4), rect(-46, 0, 92, 50, cylindre("#e03131", 0.3, 0.7)),
                  chemin("M -46 4 L -20 46 L 6 4 L 32 46", stroke="#ffd43b", sw=4), ellipse(0, 50, 46, 12, "#c92a2a")], x, y, s)


def salon(S):
    interieur(S, "#e7f5ff", "#d9b48f", y=580, papier="#d0ebff")
    S.add(fenetre(570, 110, 170, 160, "#a5d8ff", rideaux="#ffc9c9"))
    S.add(cadre_mur(150, 150, 110, 90, "#ffe066"))
    S.add(tapis(400, 720, 300, 60, "#fff3bf", "#ffd43b"))


def chambre_leo(S):
    piece(S, "chambre", y=580)
    S.add(lit(610, 700, 300, "#74c0fc", "#4dabf7"))
    S.add(etagere(170, 260, 200, objets=livres_pile(130, 260, 0.8)))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond(S, "#fff0f6")
    S.add(coeur(400, 300, 5.2, "#ffdeeb"))
    bebe_dans_les_bras(S, 540, 800, 2.0, {**MAMAN, "expr": "content", "regard": (-1, 0.3)}, "sourire", flip=True)
    S.add(leo(230, 800, 1.65, expr="malin", bras="croises", regard=(1, -0.3)))
    S.cachette(740, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(couffin(270, 262, 0.9, "dort"))
    S.add(leo(120, 262, 0.75, expr="content", regard=(1, 0.2), bras="donne"))
    return S


def p01():
    """Plan moyen : Léo et Papa préparent le couffin ; Léo s'imagine jouer au ballon avec sa petite sœur."""
    S = Scene()
    salon(S)
    S.add(couffin(520, 780, 1.3))
    S.add(papa(680, 800, 1.75, expr="content", bras="designe", flip=True, regard=(-1, 0.3)))
    S.add(leo(250, 800, 1.45, expr="joie", bras="ouverts", regard=(0, -1)))
    S.add(pensee(250, 170, 130, depuis=(260, 340)))
    S.add(personne(190, 222, 0.38, expr="rire", bras="ouverts", **LEO), personne(310, 224, 0.32, expr="rire", bras="haut", peau=PEAU_ROSE,
                                                                              cheveux="chatain", coiffure="couettes", habit="#ff8787"))
    S.add(ballon_jeu(252, 140, 18))
    return S


def p02():
    """Plan large : la porte s'ouvre ; Maman arrive avec Rose dans les bras, Papa porte le sac ; Léo saute de joie."""
    S = Scene()
    salon(S)
    S.add(porte(420, 580, 180, 330, "#b5835a", ouverte=True))
    S.add(texte(400, 110, "Bienvenue, Rose !", 46, "#e64980", contour="#fff"))
    for k in range(7):
        S.add(cercle(120 + k * 95, 165 + (k % 2) * 16, 14, ("#ff8787", "#ffd43b", "#74c0fc", "#b197fc")[k % 4]))
    S.add(chemin("M 100 160 Q 400 210 720 160", stroke="#adb5bd", sw=2))
    bebe_dans_les_bras(S, 420, 800, 1.75, {**MAMAN, "expr": "content", "regard": (-1, 0.4)}, "dort")
    S.add(papa(650, 800, 1.7, expr="rire", bras="porte", flip=True, regard=(-1, 0.2),
               objet=rect(-50, -110, 100, 70, "#495057", rx=12)))
    S.add(leo(160, 800, 1.4, expr="joie", bras="haut", regard=(1, -0.3), pas="saute"))
    S.cachette(140, 70, "air")
    return S


def p03():
    """Plan moyen : Mamie et Papa se penchent sur le couffin ; Léo, avec son dessin, attend tout seul : « Et moi, alors ? »"""
    S = Scene()
    salon(S)
    S.add(personne(400, 800, 1.65, expr="joie", bras="joues", regard=(1, 0.8), **MAMIE))
    S.add(papa(690, 800, 1.7, expr="content", bras="bas", flip=True, regard=(-1, 0.8)))
    S.add(couffin(560, 790, 1.2, "dort"))
    for x, y in ((500, 470), (590, 440), (640, 500)):
        S.add(coeur(x, y, 0.5, "#ff8787"))
    S.add(leo(130, 800, 1.3, expr="triste", bras="porte", regard=(1, 0), objet=rect(-50, -120, 100, 76, "#fff", stroke="#adb5bd", stroke_width=3)))
    S.add(bulle(470, 150, 330, 90, "Oh, qu'elle est mignonne !", 30, pointe=(450, 290)))
    S.add(bulle(150, 330, 230, 80, "Et moi, alors ?", 30, pointe=(140, 430)))
    S.cachette(240, 70, "air")
    return S


def p04():
    """Gros plan : Rose pleure très fort ; Maman la berce, fatiguée ; Léo se bouche les oreilles."""
    S = Scene()
    salon(S)
    bebe_dans_les_bras(S, 540, 900, 2.0, {**MAMAN, "expr": "inquiet", "regard": (0, 0.6)}, "pleure")
    S.add(leo(190, 880, 1.65, expr="fache", bras="tete", regard=(1, 0)))
    S.camera(1.1, 400, 500)
    for k in range(3):
        S.dessus(chemin(f"M {610 + k * 30} {380 - k * 26} q 20 -20 0 -44", stroke="#e64980", sw=5, opacity=0.8))
    S.dessus(texte(560, 120, "OUIIIN !", 80, "#e64980", contour="#fff"))
    S.cachette(745, 700)
    return S


def p05():
    """Plan moyen : Léo joue du tambour ; Papa, Rose endormie dans le couffin, lui fait « chut »."""
    S = Scene()
    salon(S)
    S.add(couffin(660, 790, 1.15, "dort"))
    S.add(papa(500, 800, 1.75, expr="inquiet", bras="chut", flip=True, regard=(-1, 0.2)))
    lx, ly, t = 200, 800, 1.45
    S.add(leo(lx, ly, t, expr="joie", bras="ouverts", regard=(0, 0.6)))
    (gx, gy), (dx, dy) = mains_personne(lx, ly, t, "ouverts")
    S.add(tambour(lx, ly - 104, 1.0), trait(gx, gy, lx - 26, ly - 110, "#c68642", 6), trait(dx, dy, lx + 26, ly - 110, "#c68642", 6))
    S.add(texte(200, 300, "BOUM ! BOUM !", 40, "#e03131", contour="#fff"))
    S.add(bulle(600, 140, 260, 90, "Chut, Léo !", 38, pointe=(540, 280)))
    return S


def p06():
    """Plan moyen : dans sa chambre, Léo serre son doudou ; un gros nuage de colère au-dessus de sa tête."""
    S = Scene()
    chambre_leo(S)
    S.add(leo(330, 800, 1.6, expr="furieux", bras="calin", regard=(0, 0.3),
              objet=g([ellipse(0, -66, 36, 30, volume("#ffa94d", 0.3, 0.8)), cercle(-20, -94, 12, "#ffa94d"), cercle(20, -94, 12, "#ffa94d"),
                       cercle(-8, -70, 3, ENCRE), cercle(8, -70, 3, ENCRE)])))
    S.add(nuage_orage(330, 180, 1.2))
    S.add(bulle(620, 250, 280, 120, "On n'a qu'à\nla rapporter !", 32, pointe=(470, 350)))
    return S


def p07():
    """Plan moyen : Léo fait le bébé avec un biberon : « Ouin ! Moi aussi, je suis un bébé ! » ; Papa sourit."""
    S = Scene()
    salon(S)
    biberon = g([rect(56, -170, 28, 60, "#e7f5ff", stroke="#74c0fc", stroke_width=3, rx=8), rect(56, -150, 28, 40, "#fff", rx=6),
                 rect(58, -182, 24, 14, "#ffa8a8", rx=4), ellipse(70, -188, 6, 8, "#ffa8a8")])
    S.add(leo(300, 800, 1.55, expr="pleure", bras="tient", regard=(1, 0), objet=biberon))
    S.add(papa(610, 800, 1.75, expr="rire", bras="hanches", flip=True, regard=(-1, 0.2)))
    S.add(bulle(300, 130, 400, 110, "Ouin ! Moi aussi,\nje suis un bébé !", 34, pointe=(300, 280)))
    return S


def p08():
    """Plan moyen : sur le canapé, Maman serre Léo contre elle ; Rose dort dans son couffin ; un grand cœur."""
    S = Scene()
    salon(S)
    S.add(coeur(380, 250, 3.0, "#ffe3e3"))
    S.add(canape(370, 790, 500, assise=False))
    S.add(maman(300, 760, 1.7, expr="content", bras="epaule", regard=(1, 0.4)))
    S.add(leo(470, 760, 1.35, expr="content", bras="calin", regard=(-1, -0.4), flip=True))
    S.add(canape(370, 790, 500, dossier=False))
    S.add(couffin(710, 790, 0.85, "dort"))
    return S


def p09():
    """Plan moyen : Léo chante pour Rose, dans le couffin ; elle arrête de pleurer et le regarde : « Elle m'écoute ! »"""
    S = Scene()
    chambre_leo(S)
    S.add(maman(700, 800, 1.65, expr="joie", bras="joues", flip=True, regard=(-1, 0.3)))
    S.add(couffin(500, 790, 1.2, "sourire"))
    S.add(leo(250, 800, 1.5, expr="chante", bras="ouverts", regard=(1, 0.4)))
    S.add(notes(360, 400, 1.0, "#4dabf7"))
    S.add(texte(400, 120, "Elle m'écoute !", 54, "#1c7ed6", contour="#fff"))
    return S


def p10():
    """Plan large : au parc, Papa et Léo, rien que tous les deux, mangent une glace."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 470, "#b2f2bb", graine=10)
    S.add(rect(0, 560, 800, 240, terrain("#8ce99a")))
    S.add(arbre(110, 580, 1.1), arbre(710, 590, 0.9))
    glace = lambda c: g([poly([(52, -150), (84, -150), (68, -100)], "#e9c46a"), cercle(68, -158, 18, c)])
    S.add(papa(520, 800, 1.8, expr="rire", bras="tient", flip=True, regard=(-1, 0.3), objet=glace("#ffa8a8")))
    S.add(leo(290, 800, 1.45, expr="rire", bras="tient", regard=(1, -0.4), objet=glace("#8ce99a")))
    S.add(texte(400, 120, "Rien que nous deux !", 52, "#2b8a3e", contour="#fff"))
    return S


def p11():
    """Gros plan : Rose serre le doigt de Léo dans sa petite main et lui sourit : « Elle m'a souri ! »"""
    S = Scene()
    salon(S)
    S.add(couffin(480, 880, 1.8, "sourire"))
    S.add(leo(240, 880, 1.6, expr="joie", bras="donne", regard=(1, 0.6)))
    S.camera(1.15, 400, 560)
    S.dessus(texte(400, 110, "Elle m'a souri !", 60, "#e64980", contour="#fff"))
    S.dessus(coeur(640, 250, 0.8, "#ff8787"), coeur(700, 310, 0.5, "#ffa8a8"))
    return S


def p12():
    """Plan moyen : Léo montre son ballon à Rose, dans les bras de Papa : « Quand tu seras grande, je t'apprendrai ! »"""
    S = Scene()
    salon(S)
    bebe_dans_les_bras(S, 570, 800, 1.75, {**PAPA, "expr": "content", "regard": (-1, 0.3)}, "sourire", flip=True)
    S.add(leo(250, 800, 1.45, expr="rire", bras="donne", regard=(1, -0.2)))
    (_, _), (mx, my) = mains_personne(250, 800, 1.45, "donne")
    S.add(ballon_jeu(mx + 20, my - 20, 36))
    S.add(bulle(300, 140, 460, 110, "Quand tu seras grande,\nje t'apprendrai !", 34, pointe=(280, 300)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("leo-seul.svg", vignette),
    ("01-bientot.svg", p01), ("02-bienvenue.svg", p02), ("03-et-moi.svg", p03),
    ("04-ouiiin.svg", p04), ("05-chut.svg", p05), ("06-la-colere.svg", p06),
    ("07-moi-aussi.svg", p07), ("08-le-soleil.svg", p08), ("09-il-chante.svg", p09),
    ("10-nous-deux.svg", p10), ("11-elle-m-a-souri.svg", p11), ("12-je-t-apprendrai.svg", p12),
]
