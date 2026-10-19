"""Le singe et le crocodile — d'après un conte de l'Inde (Jataka, Panchatantra).

Un singe vit dans un manguier, au bord d'un grand fleuve. Il offre chaque
jour des mangues bien sucrées à un crocodile, qui devient son ami. La
femme du crocodile goûte les mangues et se dit : « Si ses fruits sont si
sucrés, comme son cœur doit être doux ! » Elle veut le cœur du singe. Le
crocodile invite le singe chez lui, sur son dos ; au milieu du fleuve, il
avoue tout. Le singe ne s'affole pas : « Mon cœur ? Je l'ai laissé dans
le manguier ! Ramène-moi vite le chercher. » Le crocodile fait demi-tour,
et le singe bondit dans son arbre : « Personne ne laisse son cœur dans un
arbre ! » Garder son calme sauve des mauvais pas. Personne n'est mangé.

Plans : 1 large (le fleuve et le manguier) · 2 moyen (les mangues) · 3
moyen (chez la femme du crocodile) · 4 gros plan (« Je veux son cœur ! »)
· 5 moyen (l'invitation) · 6 large (au milieu du fleuve) · 7 gros plan
(l'idée du singe) · 8 large (le bond) · 9 moyen (la leçon).
"""
from contes import *
from base import _assombrir

ID = "singe-crocodile"

SINGE = dict(expr="content")
VERT_CROCO = "#5c940d"
MANGUE = "#ffa94d"


def mangue(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 22, 16, radial([(0, "#ffe066"), (0.6, MANGUE), (1, "#e8590c")], fx=0.35, fy=0.35)),
                  trait(18, -8, 26, -14, "#5c3d24", 3), ellipse(30, -18, 10, 5, "#40c057", rot=-30)], x, y, s, rot=rot)


def crocodile(x, y, s=1.0, expr="sourire", flip=False, bouche=False, couleur=VERT_CROCO, dame=False, nage=True, rot=0, regard=(1, 0)):
    """Crocodile de profil, la tête à droite ; (x, y) = ligne d'eau (nage) ou sol, au milieu du corps."""
    c = couleur
    fonce = _assombrir(c, 0.75)
    ventre = "#d8f5a2"
    m = [chemin("M -120 -10 Q -260 -20 -360 10 Q -260 20 -120 30 Z", volume(c, 0.3, 0.8))]
    for k in range(7):
        xx = -340 + k * 34
        m.append(poly([(xx, -2 + k * 1.5), (xx + 12, -18 - k * 2), (xx + 24, -2 + k * 1.5)], fonce))
    if not nage:
        for xx in (-90, 60):
            m.append(chemin(f"M {xx} 20 l -10 40 l 30 0 l -4 -40 Z", fonce))
    m += [ellipse(0, 0, 175, 54, volume(c, 0.3, 0.8)), ellipse(10, 30, 150, 20, ventre, opacity=0.8)]
    for k in range(8):
        m.append(ellipse(-130 + k * 36, -46, 12, 8, fonce))
    # tête et museau
    if bouche:
        m += [chemin("M 130 -30 Q 220 -60 330 -40 Q 340 -24 320 -16 L 150 4 Z", volume(c, 0.3, 0.8)),
              chemin("M 150 10 L 310 30 Q 320 44 300 48 Q 200 50 140 30 Z", volume(c, 0.3, 0.8)),
              chemin("M 150 2 L 312 -16 L 306 30 L 150 12 Z", "#c92a2a")]
        for k in range(7):
            m.append(poly([(170 + k * 20, -2 - k * 2), (178 + k * 20, 10 - k * 2), (186 + k * 20, -3 - k * 2)], "#fff"))
    else:
        m += [chemin("M 130 -30 Q 220 -50 320 -30 Q 340 -10 320 10 Q 220 24 130 24 Z", volume(c, 0.3, 0.8))]
        sourit = expr in ("sourire", "content", "rire", "malin", "miam", "fier")
        m.append(chemin("M 160 6 Q 240 14 318 0" if not sourit else "M 160 0 Q 240 18 318 -4 Q 324 -14 330 -10", stroke=_assombrir(c, 0.55), sw=4))
        for k in range(6):
            m.append(poly([(184 + k * 22, 8 - k), (190 + k * 22, 18 - k), (196 + k * 22, 8 - k)], "#fff"))
    m += [cercle(306, -34, 5, _assombrir(c, 0.5)), cercle(290, -36, 4, _assombrir(c, 0.5))]
    # œil sur sa bosse
    ys = EXPRESSIONS[expr][0]
    m += [ellipse(160, -44, 26, 22, volume(c, 0.3, 0.8)), ellipse(164, -48, 15, 13, "#fff3bf"), oeil(166, -48, ys, regard, taille=0.6),
          sourcils(166, -50, EXPRESSIONS[expr][2])]
    if dame:
        m += [g([ellipse(150 + dx, -82, 10, 18, "#f783ac", rot=dx * 2) for dx in (-14, 0, 14)]), cercle(150, -70, 6, "#ffd43b"),
              chemin("M 150 -62 l -8 -8 M 160 -62 l -2 -10 M 170 -60 l 4 -10", stroke=ENCRE, sw=2)]
    if nage:
        m.append(chemin("M -380 20 Q -200 10 0 22 Q 200 30 360 18 L 360 70 L -380 70 Z", "#339af0", opacity=0.55))
        m.append(chemin("M -360 20 q 30 -10 60 0 t 60 0 M 200 26 q 30 -10 60 0 t 60 0", stroke="#d0ebff", sw=3))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 360 * s, y - 100 * s, x + 340 * s, y + 50 * s)


def manguier(x, y, s=1.0, nb_fruits=10):
    """Grand manguier aux branches basses, plein de fruits ; (x, y) = pied du tronc."""
    m = [rect(-34, -380, 68, 380, cylindre("#8d5524", 0.3, 0.75), rx=14),
         chemin("M 0 -260 Q 120 -300 220 -280", stroke="#8d5524", sw=26), chemin("M 0 -300 Q -90 -330 -170 -320", stroke="#8d5524", sw=22),
         feuillage([(0, -450, 170, "#2b8a3e"), (-140, -380, 120, "#2f9e44"), (150, -380, 130, "#2f9e44"), (220, -300, 90, "#37b24d"),
                    (-60, -520, 110, "#37b24d"), (80, -510, 110, "#40c057")])]
    r = random.Random(5)
    for _ in range(nb_fruits):
        m.append(mangue(r.uniform(-200, 260), r.uniform(-560, -300), 0.9, rot=r.uniform(-30, 30)))
    return place(m, x, y, s)


def fleuve(S, horizon=430, rive_y=600, soir=False):
    """Un grand fleuve de l'Inde : ciel chaud, palmiers sur l'autre rive, eau large, rive de terre rouge."""
    ciel(S, "#ff922b" if soir else "#74c0fc", "#fff3bf")
    lointain(S, horizon, "#94d82d", 60, graine=3, opacite=0.5)
    for k in range(6):
        x = 60 + k * 140
        S.add(chemin(f"M {x} {horizon} Q {x + 10} {horizon - 80} {x + 20} {horizon - 120}", stroke="#8d5524", sw=6))
        for a in (-160, -125, -90, -55, -20):
            S.add(place([chemin("M 0 0 Q 22 -12 46 6 Q 22 -2 0 0 Z", "#2f9e44", stroke="#2b8a3e", sw=2)], x + 20, horizon - 120, 1.0, rot=a + 90))
    S.add(rect(0, horizon, 800, 800 - horizon, lineaire([(0, "#74c0fc"), (1, "#1971c2")])))
    for k in range(10):
        S.add(chemin(f"M {(k * 157) % 760} {horizon + 30 + k * 34} q 20 -8 40 0 t 40 0", stroke="#d0ebff", sw=3, opacity=0.8))


def rive(S, y=650, x0=0, x1=330):
    """La rive de terre rouge où pousse le manguier (à gauche)."""
    S.add(chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y - 30} {x1} {y + 20} Q {x1 + 40} 800 {x1 + 60} 800 L {x0} 800 Z", terrain("#d9a066")))
    S.cachette(x0 + 40, 790)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fleuve(S, 420)
    S.add(crocodile(470, 640, 1.0, expr="sourire"))
    rive(S, 640, 0, 260)
    S.add(manguier(110, 640, 0.9, nb_fruits=12))
    S.add(perso("singe", 470, 610, 1.15, expr="rire", bras="haut", regard=(1, 0)))
    S.cachette(30, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("singe", 200, 262, 0.95, expr="miam", bras="porte", objet=mangue(0, -74, 1.2)))
    return S


def p01():
    """Plan large : au bord d'un grand fleuve de l'Inde, un manguier plein de fruits ; un petit singe y vit, tout content."""
    S = Scene()
    fleuve(S, 440)
    rive(S, 620, 0, 420)
    S.add(manguier(220, 650, 1.0, nb_fruits=14))
    S.add(perso("singe", 370, 380, 0.75, expr="content", bras="tient", objet=mangue(68, -146, 1.2)))
    S.add(oiseau(660, 220, 0.5, "#ffd43b", ailes="haut"))
    return S


def p02():
    """Plan moyen : du bout d'une branche, le singe lance des mangues au crocodile, qui ouvre grand la gueule : « Goûte, elles sont sucrées ! »"""
    S = Scene()
    fleuve(S, 400)
    S.add(crocodile(530, 680, 0.95, bouche=True, expr="joie", regard=(-1, -1), flip=False))
    rive(S, 640, 0, 220)
    S.add(manguier(60, 660, 1.0, nb_fruits=10))
    S.add(perso("singe", 290, 400, 0.9, expr="rire", bras="lance", regard=(1, 1)))
    S.add(mangue(400, 440, 1.2, rot=20), mouvement(360, 420, 0.8, rot=30))
    S.add(bulle(560, 160, 420, 90, "Goûte, elles sont sucrées !", 30, pointe=(330, 330)))
    return S


def p03():
    """Plan moyen : sur un banc de sable, le crocodile apporte des mangues à sa femme, qui porte une fleur de lotus sur la tête."""
    S = Scene()
    fleuve(S, 420, soir=True)
    S.add(chemin("M 0 640 Q 400 580 800 640 L 800 800 L 0 800 Z", terrain("#f4d58d")))
    S.add(crocodile(260, 690, 0.8, expr="content", nage=False))
    S.add(crocodile(560, 750, 0.8, expr="miam", nage=False, dame=True, flip=True, couleur="#82c91e"))
    for k in range(3):
        S.add(mangue(380 + k * 34, 740, 0.9))
    S.cachette(730, 460, "air")
    return S


def p04():
    """Gros plan : la femme du crocodile, gourmande : « Si ses mangues sont si sucrées, son cœur doit l'être encore plus ! Je veux son cœur ! »"""
    S = Scene()
    fleuve(S, 420, soir=True)
    S.add(chemin("M 0 640 Q 400 580 800 640 L 800 800 L 0 800 Z", terrain("#f4d58d")))
    S.add(crocodile(560, 700, 1.0, expr="malin", nage=False, dame=True, flip=True, couleur="#82c91e", regard=(-1, 0)))
    S.add(crocodile(140, 720, 0.7, expr="inquiet", nage=False))
    S.add(pensee(330, 470, 70, "", depuis=(470, 620)), coeur(330, 470, 1.4, "#e64980"))
    S.camera(1.45, 400, 560)
    S.dessus(bulle(400, 110, 600, 120, "Son cœur doit être encore plus sucré\nque ses mangues ! Je le veux !", 30))
    S.cachette(250, 770)
    return S


def p05():
    """Plan moyen : au pied du manguier, le crocodile, tout gentil, invite le singe : « Viens dîner chez moi ! Monte sur mon dos ! »"""
    S = Scene()
    fleuve(S, 400)
    S.add(crocodile(560, 700, 0.9, expr="malin", regard=(-1, -0.5)))
    rive(S, 640, 0, 300)
    S.add(manguier(120, 660, 0.95, nb_fruits=8))
    S.add(perso("singe", 250, 680, 1.05, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(bulle(540, 200, 440, 110, "Viens dîner chez moi !\nMonte sur mon dos !", 32, pointe=(640, 600)))
    return S


def p06():
    """Plan large : au milieu du fleuve, le singe est assis sur le dos du crocodile ; le crocodile avoue : « Ma femme veut ton cœur… »"""
    S = Scene()
    fleuve(S, 360)
    S.add(manguier(60, 400, 0.4, nb_fruits=5))
    S.add(perso("singe", 380, 600, 1.0, expr="inquiet", bras="mains_jointes", regard=(1, 0)))
    S.add(crocodile(380, 630, 0.95, expr="triste"))
    S.add(bulle(560, 200, 420, 90, "Ma femme veut ton cœur…", 30, pointe=(650, 560)))
    S.cachette(740, 260, "air")
    return S


def p07():
    """Gros plan : le singe ne s'affole pas ; il a une idée : « Mon cœur ? Oh non ! Je l'ai laissé dans le manguier ! »"""
    S = Scene()
    fleuve(S, 360)
    S.add(perso("singe", 380, 600, 1.0, expr="malin", bras="leve_doigt", regard=(1, 0)))
    S.add(crocodile(380, 630, 0.95, expr="surpris", regard=(-1, -1)))
    S.camera(1.8, 400, 500)
    S.dessus(bulle(400, 110, 560, 110, "Mon cœur ? Je l'ai laissé\ndans le manguier !", 32))
    S.cachette(560, 330, "air")
    return S


def p08():
    """Plan large : le crocodile a fait demi-tour ; d'un bond, le singe saute de son dos jusque dans le manguier."""
    S = Scene()
    fleuve(S, 400)
    S.add(crocodile(560, 700, 0.85, expr="surpris", regard=(-1, -1)))
    rive(S, 640, 0, 300)
    S.add(manguier(150, 660, 1.0, nb_fruits=10))
    S.add(perso("singe", 380, 380, 0.85, expr="rire", bras="saute", rot=-20))
    S.add(mouvement(470, 450, 1.2, rot=-140))
    S.add(texte(560, 200, "Hop !", 64, "#e8590c", contour="#fff"))
    return S


def p09():
    """Plan moyen : bien à l'abri dans son arbre, le singe rit : « Personne ne laisse son cœur dans un arbre ! » ; le crocodile repart, penaud."""
    S = Scene()
    fleuve(S, 400)
    S.add(crocodile(620, 720, 0.7, expr="triste", flip=True, regard=(1, 0)))
    rive(S, 640, 0, 360)
    S.add(manguier(210, 660, 1.0, nb_fruits=12))
    S.add(perso("singe", 330, 410, 0.85, expr="rire", bras="ventre"))
    S.add(bulle(560, 150, 420, 110, "Personne ne laisse\nson cœur dans un arbre !", 30, pointe=(380, 300)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("singe-seul.svg", vignette),
    ("01-le-manguier.svg", p01), ("02-les-mangues.svg", p02), ("03-la-femme-du-crocodile.svg", p03),
    ("04-je-veux-son-coeur.svg", p04), ("05-l-invitation.svg", p05), ("06-au-milieu-du-fleuve.svg", p06),
    ("07-l-idee-du-singe.svg", p07), ("08-le-bond.svg", p08), ("09-la-lecon.svg", p09),
]
