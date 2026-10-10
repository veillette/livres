"""Cinq petits singes — la comptine à rebours, de cinq à zéro.

Cinq petits singes sautent sur le lit ; l'un tombe et se fait une bosse ;
Maman appelle le docteur : « Plus de petits singes qui sautent sur le
lit ! » Puis quatre, trois, deux, un… À la fin, plus personne sur le lit :
cinq singes à pansement dorment, et le lendemain, au jardin, un trampoline
les attend.

Plans : 1 large (cinq singes) · 2 moyen (quatre) · 3 gros plan (trois : la
bosse) · 4 large (deux, vus de la porte) · 5 moyen (un) · 6 gros plan (plus
personne, cinq pansements) · 7 moyen (la nuit, tout le monde dort) ·
8 large (le trampoline du jardin).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from objets import pansement
from metiers import blouse, stethoscope

ID = "cinq-singes"
PAPIER_PEINT = "rayures"

PYJAMAS = ("#fa5252", "#ff922b", "#fcc419", "#51cf66", "#4dabf7")
MAMAN = dict(habit="#cc5de8", acc=("noeud",), couleur_acc="#f783ac")
DOCTEUR = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#ffffff", robe=False,
               jambes="#495057", tenue=blouse() + stethoscope(), acc=("lunettes",))


def singe(k, x, y, s=0.9, **kw):
    """Le petit singe numéro k (0 à 4), en pyjama de sa couleur."""
    return perso("singe", x, y, s, habit=PYJAMAS[k], motif="pois", couleur_motif="#ffffff", **kw)


def telephone(x, y, s=1.0, rot=0):
    return place([rect(-12, -24, 24, 48, "#343a40", rx=5), rect(-9, -19, 18, 34, "#74c0fc", rx=2),
                  cercle(0, 19, 2.5, "#adb5bd")], x, y, s, rot=rot)


def maman(x, y, s=1.4, phone=True, **kw):
    objet = telephone(64, -150, 1.0, rot=20) if phone else None
    return perso("singe", x, y, s, bras="tient" if phone else kw.pop("bras", "bas"), objet=objet, **{**MAMAN, **kw})


def medaillon(x, y, r, bulle_texte=None):
    """Le docteur au téléphone, dans un médaillon rond (coin de page)."""
    cid = uid("m")
    dedans = g([rect(x - r, y - r, 2 * r, 2 * r, "#e7f5ff"),
                rect(x - r, y + r * 0.35, 2 * r, r, "#d0ebff"),
                personne(x, y + r * 1.25, r / 130, bras="tient", expr="neutre", regard=(-1, 0),
                         objet=telephone(*ancre(64, -150, "tient", "adulte"), 1.0, rot=20), **DOCTEUR)])
    m = [cercle(x, y, r + 8, "#fff", stroke="#74c0fc", stroke_width=5),
         el("clipPath", cercle(x, y, r, "#000"), id=cid), g(dedans, clip_path=f"url(#{cid})")]
    return g(m) + occuper(x - r - 8, y - r - 8, x + r + 8, y + r + 8)


def chambre(S, y=600, soir=True):
    piece(S, "chambre", y)
    dehors = g([rect(0, 0, 800, 800, "#ff922b" if soir else "#a5d8ff"), cercle(140, 230, 30, "#ffd43b")])
    S.add(fenetre(60, 100, 160, 150, "#ffa94d", rideaux="#4dabf7", contenu=dehors))
    S.add(lampe(730, y + 10, 0.8))


def grand_lit(x, y, s=1.0):
    """Lit double vu de face ; le dessus du matelas est à y - 125 s."""
    return place(lit(0, 0, 560, couleur="#fff", couverture="#9775fa", bois="#a0693a"), x, y, s)


def chute(k, x, y, s=0.85, flip=False):
    """Le singe k qui bascule du lit, la tête la première ; (x, y) = ses pieds, en l'air."""
    return g([singe(k, x, y, s, expr="oups", bras="haut", rot=-130 if flip else 130, pieds_haut=True),
              eclat(x + (150 if flip else -150) * s, y + 120 * s, 0.7, "#fcc419")])


def bosse(x, y, s=1.0, rot=0):
    """Pansement en croix sur une bosse."""
    return place([rect(-26, -8, 52, 16, "#ffffff", rx=6, stroke="#ced4da", stroke_width=2),
                  rect(-8, -26, 16, 52, "#ffffff", rx=6, stroke="#ced4da", stroke_width=2),
                  rect(-7, -7, 14, 14, "#ffc9c9", rx=3)], x, y, s, rot=rot)


def numero(x, y, k):
    return g([cercle(x, y, 44, "#fff3bf", stroke="#f08c00", stroke_width=5), texte(x, y + 20, str(k), 58, "#e8590c")])


def page_compte(nb, graine=1, miroir=False, ls=1.0):
    """N singes sur le lit (le dernier bascule), Maman au téléphone, le docteur en médaillon.
    miroir : Maman à droite et le singe tombe à gauche."""
    S = Scene()
    chambre(S)
    lx, ly = 400, 760
    S.add(grand_lit(lx, ly, ls))
    haut = ly - 125 * ls
    sg = -1 if miroir else 1
    restants = nb - 1
    places = [lx - sg * 120 + sg * (i - (restants - 1) / 2) * 120 for i in range(restants)]
    for i in range(restants):
        saute = (i + graine) % 2 == 0
        S.add(singe(i, places[i], haut - (60 if saute else 0), 0.75 * ls, expr="rire", bras="saute" if saute else "haut",
                    pieds_haut=saute))
    fx = lx + sg * 200 * ls
    S.add(chute(nb - 1, fx, haut - 120, 0.75 * ls, flip=miroir))
    S.add(texte(fx + sg * 40, haut - 230, "Boum !", 48, "#e03131", contour="#fff"))
    S.add(maman(700 if miroir else 100, 790, 1.35, expr="inquiet", regard=(-sg, 0), flip=miroir))
    S.add(medaillon(130 if miroir else 670, 140, 100))
    S.add(numero(400, 120, nb))
    return S


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    chambre(S)
    S.add(grand_lit(400, 780, 1.1))
    haut = 780 - 125 * 1.1
    for i, x in enumerate((150, 275, 400, 525, 650)):
        saute = i % 2 == 0
        S.add(singe(i, x, haut - (70 if saute else 10), 0.85, expr="rire", bras="saute" if saute else "haut", pieds_haut=saute))
    S.cachette(760, 770)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(singe(4, 200, 262, 0.95, expr="rire", bras="saute", pieds_haut=True))
    return S


def p01():
    """Plan large : cinq singes sautent ; le cinquième tombe."""
    return page_compte(5, graine=1)


def p02():
    """Plan moyen : quatre singes ; le lit plus grand, Maman à droite."""
    return page_compte(4, graine=2, miroir=True, ls=1.12)


def p03():
    """Gros plan : trois singes ; celui qui est tombé a une bosse."""
    S = Scene()
    chambre(S)
    S.add(grand_lit(250, 760, 1.0))
    haut = 760 - 125
    S.add(singe(0, 110, haut - 60, 0.75, expr="rire", bras="saute", pieds_haut=True))
    S.add(singe(1, 290, haut, 0.75, expr="surpris", bras="joues"))
    S.add(singe(2, 570, 800, 1.75, expr="pleure", bras="tete", larmes=True))
    S.add(cercle(560, 800 - 212 * 1.75, 18, "#ff8787"))
    S.add(eclat(560, 800 - 214 * 1.75, 0.8, "#fcc419"))
    S.add(medaillon(140, 140, 100))
    S.add(numero(400, 110, 3))
    S.add(bulle(640, 200, 280, 70, "Ouille, ma tête !", 30, pointe=(620, 330)))
    return S


def p04():
    """Plan large : deux singes ; Maman au téléphone."""
    return page_compte(2, graine=3)


def p05():
    """Plan moyen : un seul singe… et boum !"""
    return page_compte(1, graine=4, miroir=True, ls=1.12)


def p06():
    """Gros plan : plus personne sur le lit ; cinq singes à pansement, assis par terre."""
    S = Scene()
    chambre(S)
    S.add(grand_lit(400, 640, 0.9))
    for i, x in enumerate((130, 265, 400, 535, 670)):
        S.add(singe(i, x, 790, 0.95, expr=("timide", "content", "rire", "malin", "sourire")[i], bras="bas", regard=(0, -0.2)))
        S.add(bosse(x - 14, 790 - 192 * 0.95, 0.9, rot=-20 + i * 10))
    S.add(numero(400, 110, 0))
    S.add(texte(400, 240, "Plus personne sur le lit !", 40, "#e8590c", contour="#fff"))
    S.cachette(280, 70, "air")
    return S


def p07():
    """Plan moyen : la nuit, les cinq singes dorment dans le grand lit ; Maman fait chut."""
    S = Scene()
    chambre(S, soir=False)
    S.ambiance("nuit")
    lx, ly, ls = 360, 780, 1.15
    S.add(grand_lit(lx, ly, ls))
    xs = [lx - 250 + 30 + i * 95 for i in range(5)]
    for i, x in enumerate(xs):
        S.add(singe(i, x, ly - 112 * ls, 0.6, expr="dort", bras="bas", ombre=False))
    S.add(rect(lx - 280 * ls, ly - 140 * ls, 560 * ls, 100 * ls, lineaire([(0, "#b197fc"), (1, "#7048e8")]), rx=18))
    for i, x in enumerate(xs):
        S.add(bosse(x - 10, ly - 112 * ls - 192 * 0.6, 0.6, rot=-20 + i * 10))
    S.add(maman(690, 790, 1.3, phone=False, bras="chut", expr="content", regard=(-1, 0)))
    S.add(zzz(520, 470, 0.9, "#fff3bf"))
    S.add(texte(400, 200, "Chut…", 64, "#5f3dc4", contour="#fff"))
    return S


def trampoline(x, y, s=1.0):
    m = [ellipse(0, 0, 260, 22, "#000", opacity=0.12)]
    for dx in (-220, -80, 80, 220):
        m.append(trait(dx, -120, dx * 1.05, 0, "#495057", 8))
    m += [ellipse(0, -120, 250, 46, "#343a40"), ellipse(0, -120, 226, 36, "#1c7ed6"),
          ellipse(0, -126, 250, 46, "none", stroke="#fa5252", stroke_width=14)]
    return place(m, x, y, s)


def p08():
    """Plan large : le lendemain, au jardin, les cinq singes sautent sur un trampoline."""
    S = Scene()
    paysage(S, 540, 610, graine=5, nuages=((620, 130, 0.7),))
    S.add(arbre(110, 640, 1.0, fruits="#ffd43b"))
    S.add(trampoline(430, 760, 1.0))
    for i, (x, h) in enumerate(((260, 140), (350, 40), (440, 200), (530, 70), (610, 150))):
        S.add(singe(i, x, 640 - h, 0.7, expr="rire", bras="saute", pieds_haut=True))
    S.add(maman(700, 790, 1.2, phone=False, bras="applaudit", expr="rire", regard=(-1, -0.3)))
    S.add(texte(400, 150, "Boing ! Boing !", 60, "#1c7ed6", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("singe-seul.svg", vignette),
    ("01-cinq-singes.svg", p01), ("02-quatre-singes.svg", p02), ("03-trois-singes.svg", p03),
    ("04-deux-singes.svg", p04), ("05-un-singe.svg", p05), ("06-plus-personne.svg", p06),
    ("07-dodo.svg", p07), ("08-trampoline.svg", p08),
]
