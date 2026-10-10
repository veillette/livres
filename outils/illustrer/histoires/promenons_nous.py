"""Promenons-nous dans les bois — la comptine, et un loup qui veut jouer.

Trois enfants se promènent dans les bois et appellent le loup. Dans sa
cabane, le loup s'habille : culotte, chemise, chaussettes, écharpe, chapeau,
lunettes… « J'arrive ! » Les enfants s'enfuient en riant : le loup ne veut
pas les manger, il veut jouer au loup, puis goûter avec eux.

Plans : 1 large (le chemin des bois) · 2 moyen (sur la pointe des pieds) ·
3 large (la cabane du loup) · 4 moyen (la culotte) · 5 gros plan (la
chemise) · 6 moyen (les chaussettes) · 7 large (derrière l'arbre ; la
fenêtre) · 8 gros plan (les lunettes, au miroir) · 9 large (« J'arrive ! »)
· 10 moyen (le panier du goûter) · 11 large (on joue au loup) · 12 moyen
(le goûter).
"""
from base import *
from base import _assombrir
from fantastique import personne
from contes import maison_bois, panier, miroir, pain

ID = "promenons-nous"
PAPIER_PEINT = "losanges"

INES = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#f783ac", nez="rond", yeux="cils")
TOM = dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#495057", taches=True)
LOU = dict(stature="petit", peau="doree", cheveux="brun", coiffure="boucles", habit="#ffd43b", robe=False, jambes="#2f9e44")

CHEMISE = "#e7f5ff"
ACC = "#2f9e44"


def enfant(qui, x, y, s=1.2, **k):
    return personne(x, y, s, **{**qui, **k})


def culotte():
    rouge = "#fa5252"
    forme = "M -41 -48 Q 0 -38 41 -48 Q 42 -24 30 -10 Q 14 -6 6 -18 Q 0 -10 -6 -18 Q -14 -6 -30 -10 Q -42 -24 -41 -48 Z"
    rayures = chemin(" ".join(f"M {x} -50 L {x - 4} -4" for x in range(-36, 40, 14)), stroke="#fff", sw=6)
    cid = uid("c")
    return g([chemin(forme, volume(rouge, 0.3, 0.8)), el("clipPath", chemin(forme, "#000"), id=cid),
              g(rayures, clip_path=f"url(#{cid})"), chemin("M -41 -48 Q 0 -38 41 -48", stroke="#c92a2a", sw=4)])


def chaussettes():
    m = []
    for sgn in (-1, 1):
        x, yy = sgn * 21, -9 + sgn * 1.5
        m.append(ellipse(x, yy, 20, 12, volume("#ffd43b", 0.35, 0.8), rot=sgn * 7))
        m.append(chemin(f"M {x - 14} {yy - 4} Q {x} {yy + 2} {x + 14} {yy - 4}", stroke="#e64980", sw=4))
        m.append(rect(x - 12, yy - 20, 24, 12, "#ffd43b", rx=4, stroke="#f08c00", stroke_width=1.5))
    return g(m)


def loup(x, y, s=1.3, etape=6, **k):
    """Le loup, habillé jusqu'à l'étape voulue : 1 culotte, 2 chemise,
    3 chaussettes, 4 écharpe, 5 chapeau, 6 lunettes."""
    acc = []
    if etape >= 4:
        acc.append("echarpe")
    if etape >= 5:
        acc.append("chapeau")
    if etape >= 6:
        acc.append("lunettes")
    objets = [culotte()] if etape >= 1 else []
    if etape >= 3:
        objets.append(chaussettes())
    if "objet" in k:
        objets.append(k.pop("objet"))
    return perso("loup", x, y, s, habit=CHEMISE if etape >= 2 else None, acc=tuple(acc), couleur_acc=ACC,
                 objet=g(objets) if objets else None, **k)


def bois(S, y=620, graine=2, haut="#a5d8ff", bas="#ebfbee", sentier=True):
    """Sous-bois : grands arbres, fougères, sentier qui serpente."""
    ciel(S, haut, bas)
    r = random.Random(graine)
    for k in range(6):
        xx = -60 + k * 170 + r.uniform(-30, 30)
        S.add(arbre(xx, y - 40 + r.uniform(-20, 10), r.uniform(0.85, 1.05), "#69db7c", "#51cf66", "#8d5524"))
    sol(S, y, "#8ce99a", premier=False)
    if sentier:
        S.add(chemin(f"M 330 {y} Q 300 {y + 60} 360 {y + 100} Q 480 {y + 150} 380 800 L 620 800 Q 640 {y + 140} 470 {y + 100} Q 400 {y + 60} 430 {y} Z",
                     "#e9c99a"))
    for k in range(5):
        S.add(champignon(r.uniform(40, 760), r.uniform(y + 40, y + 120), r.uniform(0.35, 0.55)))
    premier_plan_sol(S, "#8ce99a", y + 18, graine=graine)


def fougere(x, y, s=1.0, flip=False):
    m = []
    for k, a in enumerate((-50, -25, 0, 25, 50)):
        L = 150 - abs(a)
        tx, ty = math.sin(math.radians(a)) * L, -math.cos(math.radians(a)) * L
        m.append(chemin(f"M 0 0 Q {n(tx * 0.3)} {n(ty * 0.7)} {n(tx)} {n(ty)}", stroke="#2b8a3e", sw=5))
        for t in (0.35, 0.55, 0.75):
            px, py = tx * t, ty * t
            m.append(ellipse(px - 10, py, 14, 5, "#37b24d", rot=a - 20) + ellipse(px + 10, py, 14, 5, "#37b24d", rot=a + 20))
    return place(m, x, y, s, flip=flip)


def gros_tronc(x, y, s=1.0):
    """Gros arbre du premier plan derrière lequel on se cache."""
    return place([rect(-60, -500, 120, 500, cylindre("#8d5524", 0.25, 0.75), rx=20),
                  chemin("M -20 -60 q 8 -40 0 -80 M 24 -200 q -6 -30 2 -60 M -14 -320 q 6 -20 0 -40", stroke="#5c3a1e", sw=4, opacity=0.6),
                  chemin("M -60 0 Q -90 4 -110 10 L 110 10 Q 90 4 60 0 Z", "#6d4424"),
                  cercle(0, -560, 170, volume("#40c057", 0.28, 0.75)), cercle(-130, -470, 110, volume("#37b24d", 0.28, 0.75)),
                  cercle(130, -470, 110, volume("#37b24d", 0.28, 0.75))], x, y, s)


def cabane_dedans(S):
    piece(S, "chaumiere", 570)
    S.add(fenetre(530, 110, 170, 150, "#a5d8ff", cadre="#8d5524",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), arbre(580, 330, 0.6), arbre(690, 340, 0.5)])))
    S.add(cadre_mur(120, 130, 110, 90, "#b2f2bb"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    bois(S, 600, graine=3)
    S.add(gros_tronc(700, 640, 0.8))
    S.add(loup(660, 780, 1.4, expr="malin", bras="coucou", regard=(-1, 0), flip=True))
    S.add(enfant(TOM, 130, 790, 1.25, expr="rire", bras="court", regard=(1, 0)))
    S.add(enfant(INES, 290, 790, 1.25, expr="rire", bras="main", regard=(1, 0)))
    S.add(enfant(LOU, 430, 795, 1.25, expr="joie", bras="haut", regard=(1, 0)))
    S.add(fougere(40, 800, 1.1), fougere(790, 810, 1.0, flip=True))
    S.cachette(100, 360, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(loup(200, 262, 0.85, etape=6, expr="rire", bras="salut"))
    return S


def p01():
    """Plan large : les trois enfants marchent sur le sentier des bois en chantant."""
    S = Scene()
    bois(S, 560, graine=4)
    S.add(enfant(TOM, 300, 720, 1.0, expr="chante", bras="marche", regard=(1, 0)))
    S.add(enfant(INES, 430, 700, 1.0, expr="chante", bras="main", regard=(1, 0)))
    S.add(enfant(LOU, 540, 690, 1.0, expr="content", bras="marche", regard=(1, 0)))
    S.add(notes(240, 470, 0.8, "#2b8a3e"), notes(600, 440, 0.7, "#2b8a3e"))
    S.add(fougere(40, 800, 1.2), fougere(780, 810, 1.1, flip=True))
    return S


def p02():
    """Plan moyen : sur la pointe des pieds, chut !"""
    S = Scene()
    bois(S, 520, graine=5, sentier=False)
    S.add(enfant(TOM, 190, 790, 1.5, expr="malin", bras="chut", pas="pointe", regard=(1, 0)))
    S.add(enfant(INES, 420, 790, 1.5, expr="inquiet", bras="joues", pas="pointe", regard=(1, 0)))
    S.add(enfant(LOU, 630, 790, 1.5, expr="surpris", bras="bouche", regard=(-1, 0)))
    S.add(texte(400, 150, "Chut…", 64, "#2b8a3e", contour="#fff"))
    S.cachette(730, 420, "air")
    return S


def p03():
    """Plan large : la cabane du loup au fond des bois ; les enfants l'appellent."""
    S = Scene()
    bois(S, 580, graine=6, sentier=True)
    S.add(maison_bois(520, 640, 1.2))
    S.add(cercle(520 + 72 * 1.2, 640 - 92 * 1.2, 4, ENCRE))
    S.add(enfant(TOM, 150, 780, 1.15, expr="joie", bras="joues", regard=(1, -0.3)))
    S.add(enfant(INES, 280, 780, 1.15, expr="joie", bras="joues", regard=(1, -0.3)))
    S.add(enfant(LOU, 380, 785, 1.15, expr="surpris", bras="bas", regard=(1, -0.3)))
    S.add(bulle(260, 150, 420, 110, "Loup, y es-tu ?\nQue fais-tu ?", 36, pointe=(230, 470)))
    S.add(fougere(780, 810, 1.1, flip=True))
    return S


def p04():
    """Plan moyen : dans sa cabane, le loup met sa culotte."""
    S = Scene()
    cabane_dedans(S)
    S.add(loup(380, 780, 1.8, etape=1, expr="rire", bras="hanches", regard=(1, 0)))
    S.add(bulle(560, 400, 360, 90, "Je mets\nma culotte !", 34, pointe=(470, 480)))
    return S


def p05():
    """Gros plan : la chemise."""
    S = Scene()
    cabane_dedans(S)
    S.add(loup(400, 780, 1.8, etape=2, expr="fier", bras="montre", regard=(1, 0)))
    S.camera(1.6, 420, 460)
    S.dessus(bulle(560, 130, 380, 100, "Je mets\nma chemise !", 36, pointe=S.vers_page(470, 420)))
    return S


def p06():
    """Plan moyen : les chaussettes jaunes."""
    S = Scene()
    cabane_dedans(S)
    S.add(loup(330, 780, 1.7, etape=3, expr="content", bras="designe", regard=(0.5, 0.6)))
    S.add(bulle(590, 380, 340, 100, "Je mets mes\nchaussettes !", 34, pointe=(450, 470)))
    return S


def p07():
    """Plan large : cachés derrière un gros arbre, les enfants rappellent ; le loup répond par la fenêtre."""
    S = Scene()
    bois(S, 580, graine=7, sentier=False)
    S.add(maison_bois(560, 620, 1.1))
    S.add(loup(560 + 72 * 1.1, 620 - 70 * 1.1, 0.45, etape=5, expr="rire", bras="salut", ombre=False))
    S.add(gros_tronc(170, 800, 0.85))
    S.add(enfant(INES, 300, 790, 1.15, expr="malin", bras="joues", regard=(1, -0.3)))
    S.add(enfant(LOU, 90, 795, 1.15, expr="surpris", bras="bouche", regard=(1, 0)))
    S.add(bulle(560, 140, 460, 110, "Je mets mon écharpe…\net mon chapeau !", 32, pointe=(640, 480)))
    return S


def p08():
    """Gros plan : devant le miroir, le loup met ses lunettes."""
    S = Scene()
    cabane_dedans(S)
    reflet = place(loup(0, 0, 1.0, etape=6, expr="fier", flip=True), 0, 0, 1)
    S.add(miroir(570, 790, 1.15, reflet=place(reflet, 10, -96, 1.2)))
    S.add(loup(300, 790, 1.7, etape=6, expr="fier", bras="tient", regard=(1, 0)))
    S.camera(1.4, 410, 470)
    S.dessus(bulle(360, 110, 420, 100, "Je mets\nmes lunettes !", 36, pointe=S.vers_page(320, 450)))
    S.cachette(174, 327, "air")
    return S


def p09():
    """Plan large : la porte s'ouvre — « J'arrive ! » ; les enfants s'enfuient en riant."""
    S = Scene()
    bois(S, 580, graine=8)
    S.add(maison_bois(600, 640, 1.2))
    S.add(loup(600, 700, 1.15, etape=6, expr="rire", bras="haut"))
    S.add(enfant(TOM, 140, 790, 1.15, expr="rire", bras="court", flip=True))
    S.add(enfant(INES, 290, 780, 1.15, expr="rire", bras="court", flip=True))
    S.add(enfant(LOU, 410, 790, 1.15, expr="joie", bras="haut", flip=True))
    S.add(texte(560, 160, "J'arrive !", 72, "#e03131", contour="#fff"))
    S.cachette(70, 450, "air")
    return S


def p10():
    """Plan moyen : le loup tend son panier : il ne veut pas manger les enfants, il veut goûter."""
    S = Scene()
    bois(S, 540, graine=9, sentier=False)
    S.add(loup(520, 790, 1.6, etape=6, expr="rire", bras="donne", flip=True, regard=(-1, 0),
               objet=panier(84, -60, 0.9)))
    S.add(enfant(INES, 130, 790, 1.35, expr="surpris", bras="bouche", regard=(1, 0)))
    S.add(enfant(LOU, 290, 795, 1.35, expr="joie", bras="bas", regard=(1, -0.3)))
    S.add(bulle(420, 130, 560, 120, "Vous manger ? Pouah !\nMoi, je veux jouer… et goûter !", 32, pointe=(560, 430)))
    return S


def p11():
    """Plan large : dans la clairière, on joue au loup ; le loup touche Tom."""
    S = Scene()
    bois(S, 560, graine=10, sentier=False, haut="#74c0fc")
    S.add(loup(330, 760, 1.2, etape=6, expr="rire", bras="court", regard=(1, 0)))
    S.add(enfant(TOM, 470, 760, 1.15, expr="rire", bras="court", regard=(-1, 0)))
    S.add(enfant(INES, 640, 740, 1.05, expr="rire", bras="saute", regard=(-1, 0)))
    S.add(enfant(LOU, 150, 780, 1.1, expr="joie", bras="applaudit", regard=(1, 0)))
    S.add(texte(470, 260, "Touché !", 56, "#e03131", contour="#fff"))
    S.add(texte(470, 330, "C'est toi le loup !", 40, "#5f3dc4", contour="#fff"))
    S.cachette(730, 450, "air")
    return S


def p12():
    """Plan moyen : le goûter tous ensemble sur une nappe, sous les arbres."""
    S = Scene()
    bois(S, 540, graine=11, sentier=False, haut="#ffd8a8", bas="#fff4e6")
    S.add(ellipse(400, 720, 330, 60, "#ff8787"))
    for k in range(-4, 5):
        S.add(trait(400 + k * 70, 664, 400 + k * 80, 778, "#fff", 4, opacity=0.5))
    S.add(panier(400, 720, 1.0))
    S.add(pain(270, 718, 0.8), pain(530, 722, 0.7, rot=20))
    S.add(loup(560, 700, 1.25, etape=6, expr="miam", bras="porte", regard=(-1, 0), objet=pain(0, -76, 0.7)))
    S.add(enfant(TOM, 180, 720, 1.1, expr="rire", bras="bas", regard=(1, 0)))
    S.add(enfant(INES, 300, 740, 1.1, expr="content", bras="applaudit", regard=(1, 0)))
    S.add(enfant(LOU, 680, 760, 1.1, expr="miam", bras="porte", regard=(-1, 0)))
    S.add(texte(400, 150, "Bon appétit !", 56, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("loup-seul.svg", vignette),
    ("01-promenons-nous.svg", p01), ("02-chut.svg", p02), ("03-loup-y-es-tu.svg", p03),
    ("04-la-culotte.svg", p04), ("05-la-chemise.svg", p05), ("06-les-chaussettes.svg", p06),
    ("07-chapeau-echarpe.svg", p07), ("08-les-lunettes.svg", p08), ("09-j-arrive.svg", p09),
    ("10-le-panier.svg", p10), ("11-on-joue-au-loup.svg", p11), ("12-le-gouter.svg", p12),
]
