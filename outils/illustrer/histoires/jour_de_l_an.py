"""Bonne année, grosse santé ! — le jour de l'An chez les grands-parents.

Le premier janvier, Léon et Maman vont fêter le jour de l'An chez
Grand-papa et Grand-maman. Tout le monde s'embrasse : « Bonne année, grosse
santé ! » Léon, intimidé, demande à Grand-papa ce qu'est un souhait. Alors
il en offre un à chacun : des tourtières toujours aussi bonnes pour
Grand-maman, de belles glissades pour Tante Julie, un gros os pour Biscotte,
un violon qui chante pour Grand-papa… et pour la petite Lili, de marcher
bientôt. Le soir, c'est à son tour de recevoir des souhaits — et Lili fait
ses trois premiers pas, droit dans ses bras.

Plans : 1 large (la route enneigée) · 2 moyen (les bises à la porte) ·
3 gros plan (c'est quoi, un souhait ?) · 4 moyen (la tourtière) · 5 gros
plan (Lili) · 6 large (la glissade) · 7 moyen (Biscotte et le bonhomme de
neige) · 8 large (le violon et la danse) · 9 large (à ton tour !) · 10 gros
plan (les premiers pas) · 11 large (le retour sous les étoiles).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fables import violon, archet
from fetes import chien_profil, guirlande_lumineuse, confettis, serpentin

ID = "jour-de-l-an"
PAPIER_PEINT = "rayures"

ROUGE = "#c92a2a"


def _tuque(c="#1098ad", c2="#ffffff"):
    """Tuque à pompon, posée sur la tête d'un personnage humain (repère local)."""
    return g([chemin("M -54 -178 Q -56 -240 0 -242 Q 56 -240 54 -178 Z", volume(c, 0.3, 0.75)),
              chemin("M -40 -222 Q 0 -232 40 -222 M -50 -202 Q 0 -212 50 -202", stroke=c2, sw=5, opacity=0.8),
              rect(-58, -194, 116, 22, c2, rx=10), chemin("M -50 -184 H 50", stroke=_assombrir(c2, 0.85), sw=2),
              cercle(0, -250, 16, c2)])


LEON = dict(peau="doree", cheveux="brun", coiffure="courts", habit="#1098ad", robe=False, jambes="#364fc7", nez="petit")
MAMAN = dict(peau="doree", cheveux="noir", coiffure="queue", habit="#e64980", stature="adulte", carrure="fine",
             yeux="cils", nez="pointu")
GRAND_PAPA = dict(peau="claire", cheveux="blanc", coiffure="chauve_cote", habit=ROUGE, robe=False, jambes="#495057",
                  stature="ancien", carrure="normale", nez="long", barbe="#e9ecef")
GRAND_MAMAN = dict(peau="claire", cheveux="gris", coiffure="boucles", habit="#7048e8", stature="ancien",
                   carrure="ronde", nez="rond", acc=("lunettes",))
JULIE = dict(peau="claire", cheveux="roux", coiffure="carre", habit="#f08c00", robe=False, jambes="#343a40",
             stature="adulte", taches=True, nez="retrousse")
LILI = dict(peau="claire", cheveux="roux", coiffure="couettes", habit="#ffc9c9", stature="petit", acc=("noeud",),
            couleur_acc="#e64980")


def leon(x, y, s=1.2, tuque=False, **k):
    if tuque:
        k.setdefault("coiffe", _tuque("#1098ad"))
    return personne(x, y, s, **{**LEON, **k})


def maman(x, y, s=1.2, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def grand_papa(x, y, s=1.2, **k):
    return personne(x, y, s, **{**GRAND_PAPA, **k})


def grand_maman(x, y, s=1.2, **k):
    return personne(x, y, s, **{**GRAND_MAMAN, **k})


def julie(x, y, s=1.2, tuque=False, **k):
    if tuque:
        k.setdefault("coiffe", _tuque("#f08c00"))
    return personne(x, y, s, **{**JULIE, **k})


def lili(x, y, s=0.9, **k):
    return personne(x, y, s, **{**LILI, **k})


def biscotte(x, y, s=0.8, **k):
    return chien_profil(x, y, s, couleur="#f1f3f5", oreille="#868e96", collier=ROUGE, **k)


# --- Objets ----------------------------------------------------------------------

def voiture(x, y, s=1.0, couleur="#1098ad", flip=False, dormeur=False, neige=True):
    """Petite voiture vue de côté ; (x, y) = sol, au milieu. dormeur : Léon
    endormi derrière la vitre arrière."""
    fonce = _assombrir(couleur, 0.75)
    m = [ellipse(0, 0, 160, 10, "#000", opacity=0.15),
         chemin("M -150 -28 Q -152 -72 -110 -76 L -70 -78 Q -42 -132 16 -134 L 58 -134 Q 100 -132 122 -82 L 140 -78 "
                "Q 162 -72 162 -40 L 162 -26 Q 162 -14 150 -14 L -140 -14 Q -150 -14 -150 -28 Z", volume(couleur, 0.3, 0.75)),
         chemin("M -56 -82 Q -36 -122 6 -122 L 6 -82 Z", "#a5d8ff"), chemin("M 20 -82 L 20 -122 L 56 -122 Q 92 -120 108 -82 Z", "#a5d8ff")]
    if dormeur:
        m += [cercle(-22, -96, 18, PEAU_LEON), chemin("M -40 -100 Q -22 -124 -4 -100 Q -22 -112 -40 -100 Z", "#4a2c17"),
              chemin("M -30 -96 q 4 4 8 0 M -18 -96 q 4 4 8 0", stroke=ENCRE, sw=2)]
    m += [trait(-150, -48, 160, -48, fonce, 3, opacity=0.6), rect(146, -66, 14, 12, "#fff3bf", rx=3), rect(-150, -64, 10, 12, "#fa5252", rx=3)]
    if neige:
        m.append(chemin("M -40 -128 Q 16 -146 64 -134 Q 30 -136 16 -132 Q -10 -132 -40 -128 Z", "#ffffff"))
    for wx in (-92, 100):
        m += [cercle(wx, -14, 32, "#343a40"), cercle(wx, -14, 15, "#ced4da"), cercle(wx, -14, 5, "#868e96")]
    return place(m, x, y, s, flip=flip)


PEAU_LEON = "#dca36f"


def tourtiere(x, y, s=1.0):
    """Tourtière dorée, croûte fendue ; (x, y) = dessous du moule."""
    croute = "#e3a857"
    m = [chemin("M -80 -26 L 80 -26 L 68 0 L -68 0 Z", volume("#adb5bd", 0.3, 0.75)),
         ellipse(0, -28, 82, 24, volume(croute, 0.4, 0.75)),
         chemin(" ".join(f"M {-60 + k * 10} {-28 + (k % 2) * 4} l 6 -4" for k in range(13)), stroke=_assombrir(croute, 0.75), sw=3),
         chemin("M -20 -34 l 8 8 M 0 -38 l 0 12 M 20 -34 l -8 8", stroke=_assombrir(croute, 0.6), sw=4),
         ellipse(-26, -40, 20, 6, "#fff", opacity=0.3)]
    for k in range(3):
        m.append(chemin(f"M {-24 + k * 24} -56 q 10 -16 0 -32 q -10 -16 0 -32", stroke="#fff", sw=4, opacity=0.5))
    return place(m, x, y, s)


def fauteuil(x, y, s=1.0, couleur="#2b8a3e"):
    """Gros fauteuil de face ; (x, y) = milieu du pied."""
    f = _assombrir(couleur, 0.8)
    m = [ellipse(0, 0, 150, 10, "#000", opacity=0.12),
         rect(-110, -300, 220, 220, volume(couleur, 0.25, 0.8), rx=60),
         rect(-140, -170, 280, 130, volume(couleur, 0.3, 0.75), rx=30),
         rect(-160, -210, 60, 180, f, rx=28), rect(100, -210, 60, 180, f, rx=28),
         rect(-130, -36, 18, 36, "#5c3d2e"), rect(112, -36, 18, 36, "#5c3d2e")]
    return place(m, x, y, s)


def canape(x, y, s=1.0, couleur="#a61e4d"):
    f = _assombrir(couleur, 0.8)
    m = [ellipse(0, 0, 260, 10, "#000", opacity=0.12),
         rect(-220, -200, 440, 120, volume(couleur, 0.25, 0.8), rx=30),
         rect(-240, -110, 480, 90, volume(couleur, 0.3, 0.75), rx=24),
         rect(-260, -150, 60, 140, f, rx=26), rect(200, -150, 60, 140, f, rx=26),
         rect(-230, -20, 20, 20, "#5c3d2e"), rect(210, -20, 20, 20, "#5c3d2e")]
    return place(m, x, y, s)


def toboggan(x, y, s=1.0, couleur="#c68642"):
    """Traîne sauvage en bois, l'avant recourbé à droite ; (x, y) = milieu du dessous."""
    m = [chemin("M -120 0 L 110 0 Q 150 0 150 -40 Q 150 -64 128 -62", stroke=_assombrir(couleur, 0.8), sw=16),
         chemin("M -120 0 L 110 0 Q 150 0 150 -40 Q 150 -64 128 -62", stroke=couleur, sw=10),
         rect(-120, -56, 230, 54, volume(couleur, 0.3, 0.75), rx=8),
         planches(-120, -56, 230, 54, couleur, larg=18, vertical=False), trait(-110, -40, 100, -40, ROUGE, 4)]
    return place(m, x, y, s)


def bonhomme_neige(x, y, s=1.0):
    """Bonhomme de neige, tuque et foulard ; (x, y) = pied."""
    m = [ellipse(0, -60, 70, 62, volume("#ffffff", 0.1, 0.85)), ellipse(0, -160, 52, 48, volume("#ffffff", 0.1, 0.85)),
         ellipse(0, -240, 38, 36, volume("#ffffff", 0.1, 0.85)),
         chemin("M -36 -206 Q 0 -192 36 -206 L 34 -194 Q 0 -180 -34 -194 Z", ROUGE), rect(14, -200, 16, 50, ROUGE, rx=5),
         cercle(-12, -250, 4, ENCRE), cercle(12, -250, 4, ENCRE), poly([(0, -240), (36, -232), (0, -230)], "#ff922b"),
         chemin("M -14 -222 Q 0 -214 14 -222", stroke=ENCRE, sw=3),
         cercle(0, -170, 5, ENCRE), cercle(0, -145, 5, ENCRE),
         chemin("M -48 -170 L -110 -210 M -90 -198 L -104 -230", stroke="#6d4424", sw=6),
         chemin("M 48 -170 L 110 -200", stroke="#6d4424", sw=6),
         place(chemin("M -40 -10 Q -40 -64 0 -66 Q 40 -64 40 -10 Z", volume("#1098ad", 0.3, 0.75)), 0, -258, 0.95),
         rect(-42, -276, 84, 18, "#fff", rx=8), cercle(0, -326, 12, "#fff"),
         occuper(-110, -345, 110, 0)]
    return place(m, x, y, s)


def os_(x, y, s=1.0, rot=0):
    return place([rect(-30, -6, 60, 12, "#fff9db", rx=5), cercle(-30, -8, 9, "#fff9db"), cercle(-30, 8, 9, "#fff9db"),
                  cercle(30, -8, 9, "#fff9db"), cercle(30, 8, 9, "#fff9db")], x, y, s, rot=rot)


# --- Décors ----------------------------------------------------------------------

def hiver(S, sol_y=620, graine=3, flocons_=24):
    """Campagne sous la neige : ciel d'hiver, collines blanches, sapins enneigés."""
    ciel(S, "#a5d8ff", "#f8f9fa")
    collines(S, sol_y - 40, "#e7f5ff", graine=graine, bosquets=False)
    sol(S, sol_y, "#f8f9fa", bosse=10)
    if flocons_:
        flocons(S, flocons_, graine, zone=(0, 0, 800, sol_y))


def maison_grands_parents(x, y, s=1.0, lumiere=False):
    return maison(x, y, s, mur="#ffe8cc", toit="#dee2e6", porte=ROUGE, volets=ROUGE, lumiere=lumiere)


def salon(S, y=620, soir=False):
    """Le salon des grands-parents : boiseries, fenêtre sur la neige, guirlande."""
    piece(S, "manoir", y)
    dehors = g([rect(0, 0, 800, 800, "#1c2a52" if soir else "#d0ebff"), rect(0, 240, 800, 200, "#f1f3f5"),
                sapin(560, 250, 0.32, neige=True), sapin(650, 260, 0.26, neige=True)])
    S.add(fenetre(500, 90, 200, 170, "#d0ebff", cadre="#fff", rideaux=ROUGE, contenu=dehors))
    S.add(guirlande_lumineuse(10, 36, 790, 36, creux=18, nb=14))
    if soir:
        S.ambiance("interieur")


def cuisine(S, y=620):
    piece(S, "cuisine", y)
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 220, 800, 200, "#f8f9fa"), sapin(170, 230, 0.3, neige=True)])
    S.add(fenetre(100, 90, 180, 150, "#d0ebff", cadre="#fff", rideaux="#7048e8", contenu=dehors))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    hiver(S, 640, graine=4, flocons_=30)
    S.add(maison_grands_parents(560, 640, 0.95, lumiere=True))
    S.add(guirlande_lumineuse(430, 470, 690, 470, creux=10, nb=8))
    S.add(sapin(120, 650, 1.1, neige=True), sapin(240, 640, 0.75, neige=True))
    S.add(bonhomme_neige(110, 770, 0.6))
    S.add(confettis(200, 260, 640, 520, 30, graine=3))
    S.add(grand_papa(600, 780, 1.1, expr="rire", bras="porte",
                     objet=g([violon(*ancre(-10, -90, "porte", "ancien"), 0.9, rot=-60),
                              archet(*ancre(30, -100, "porte", "ancien"), 0.8, rot=30)])))
    S.add(biscotte(720, 790, 0.6, expr="rire"))
    S.add(leon(380, 790, 1.4, tuque=True, expr="rire", bras="saute", regard=(0, 0)))
    S.cachette(220, 300, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(confettis(20, 20, 380, 150, 24, graine=8))
    S.add(tourtiere(130, 250, 0.9), bonhomme_neige(330, 262, 0.62))
    S.add(texte(150, 110, "Bonne année !", 34, "#1098ad", contour="#fff"))
    return S


def p01():
    """Plan large : la route enneigée jusque chez les grands-parents."""
    S = Scene()
    hiver(S, 600, graine=5)
    S.add(maison_grands_parents(560, 600, 0.9))
    for k in range(3):
        S.add(chemin(f"M {586 + k * 6} 300 q 18 -30 0 -60 q -18 -30 0 -60", stroke="#ced4da", sw=10 - k * 2, opacity=0.6))
    S.add(sapin(90, 610, 1.0, neige=True), sapin(200, 600, 0.75, neige=True), sapin(760, 620, 0.9, neige=True))
    S.add(chemin("M 0 720 Q 300 690 520 640 L 600 640 Q 380 720 0 800 Z", "#dee2e6"))
    S.add(voiture(280, 730, 0.9, "#1098ad"))
    S.add(texte(280, 560, "Vroum…", 40, "#1098ad", contour="#fff", rot=-4))
    S.add(texte(400, 150, "1er janvier", 52, "#c92a2a", contour="#fff"))
    S.cachette(740, 760)
    return S


def p02():
    """Plan moyen : à la porte, les bises ; Léon se cache derrière Maman."""
    S = Scene()
    salon(S)
    S.add(porte(140, 620, 170, 380, ROUGE))
    S.add(grand_maman(320, 760, 1.15, expr="rire", bras="calin", regard=(1, 0)))
    S.add(leon(510, 790, 1.0, tuque=True, expr="timide", bras="joues", regard=(-1, 0)))
    S.add(maman(430, 760, 1.15, expr="rire", bras="calin", flip=True, regard=(-1, 0)))
    S.add(grand_papa(680, 760, 1.15, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(330, 170, 440, 100, "Bonne année,\ngrosse santé !", 40, pointe=(330, 450)))
    S.add(texte(620, 330, "smack !", 34, "#e64980", rot=10))
    S.cachette(60, 760)
    return S


def p03():
    """Gros plan : dans le fauteuil, Léon demande ce qu'est un souhait."""
    S = Scene()
    salon(S)
    S.add(fauteuil(420, 820, 1.4))
    S.add(grand_papa(470, 760, 1.4, expr="content", bras="epaule", flip=True, regard=(-1, 0.4)))
    S.add(leon(330, 790, 1.15, expr="surpris", bras="pense", regard=(1, -0.6)))
    S.camera(1.3, 420, 520)
    S.dessus(bulle(220, 110, 340, 90, "C'est quoi,\nun souhait ?", 32, pointe=S.vers_page(330, 520)),
             bulle(560, 200, 400, 120, "C'est un cadeau en mots :\non souhaite à quelqu'un\nce qui le rendra heureux.", 22,
                   pointe=S.vers_page(500, 440)))
    S.cachette(120, 300, "air")
    return S


def p04():
    """Plan moyen : la tourtière de Grand-maman ; le premier souhait de Léon."""
    S = Scene()
    cuisine(S)
    S.add(grand_maman(540, 690, 1.35, expr="rire", bras="porte", regard=(-1, 0.3),
                      objet=tourtiere(*ancre(0, -60, "porte", "ancien", "ronde"), 0.85)))
    S.add(table(400, 800, 620, 150, "#c68642", nappe="#e5dbff"))
    S.add(tourtiere(260, 640, 0.6))
    S.add(leon(170, 770, 1.2, expr="fier", bras="leve_doigt", regard=(1, -0.3)))
    S.add(bulle(330, 170, 460, 110, "Grand-maman, je te souhaite\ndes tourtières toujours\naussi bonnes !", 24, pointe=(200, 440)))
    return S


def p05():
    """Gros plan : Lili, debout contre le canapé ; le souhait de Léon."""
    S = Scene()
    salon(S)
    S.add(canape(360, 800, 1.2))
    S.add(lili(300, 790, 1.2, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(leon(560, 800, 1.35, expr="content", bras="tend", flip=True, regard=(-1, 0.3)))
    S.camera(1.35, 420, 560)
    S.dessus(bulle(400, 100, 460, 90, "Lili, je te souhaite\nde marcher bientôt !", 30, pointe=S.vers_page(540, 480)))
    S.dessus(texte(160, 330, "Areu !", 40, "#e64980", contour="#fff", rot=-8))
    S.cachette(720, 660, "air")
    return S


def p06():
    """Plan large : la glissade ; « Plein de belles glissades ! »"""
    S = Scene()
    ciel(S, "#74c0fc", "#f8f9fa")
    S.add(soleil(680, 110, 46))
    S.add(chemin("M 0 330 Q 200 320 420 470 Q 600 600 800 620 L 800 800 L 0 800 Z", lineaire([(0, "#ffffff"), (1, "#e7f5ff")])))
    S.add(sapin(90, 360, 0.8, neige=True), sapin(190, 350, 0.6, neige=True))
    S.add(chemin("M 120 400 Q 330 430 470 520 Q 620 610 790 650", stroke="#d0ebff", sw=40, opacity=0.8))
    S.add(julie(220, 460, 0.95, tuque=True, expr="rire", bras="haut", regard=(1, 0)))
    S.add(place(g([leon(-20, 20, 0.9, tuque=True, expr="rire", bras="haut"), toboggan(0, 0, 1.0)]), 520, 590, 1.0, rot=22))
    S.add(mouvement(380, 480, 1.4, "#74c0fc", rot=22))
    S.add(texte(560, 400, "Youpi !", 54, "#1098ad", contour="#fff", rot=20))
    S.add(bulle(220, 200, 380, 100, "Tante Julie, je te souhaite\nplein de belles glissades !", 22, pointe=(470, 380)))
    S.cachette(70, 600, "air")
    return S


def p07():
    """Plan moyen : Biscotte saute dans la neige, près du bonhomme de neige."""
    S = Scene()
    hiver(S, 620, graine=6, flocons_=18)
    S.add(maison_grands_parents(130, 620, 0.55))
    S.add(bonhomme_neige(600, 760, 1.0))
    S.add(biscotte(330, 740, 1.1, expr="rire", course=True, gueule=os_(10, 4, 0.8, rot=-10)))
    S.add(leon(170, 790, 1.2, tuque=True, expr="rire", bras="designe", regard=(1, 0)))
    S.add(texte(420, 470, "Wouf !", 54, "#e8590c", contour="#fff", rot=-8))
    S.add(bulle(330, 170, 460, 100, "Biscotte, je te souhaite\nplein de gros os !", 28, pointe=(200, 470)))
    return S


def p08():
    """Plan large : le soir, Grand-papa joue du violon, tout le monde danse."""
    S = Scene()
    salon(S, soir=True)
    S.add(lampe(80, 620, 0.9, abat="#ffd8a8"))
    S.add(grand_papa(400, 700, 1.15, expr="chante", bras="porte",
                     objet=g([violon(*ancre(-14, -96, "porte", "ancien"), 0.95, rot=-60),
                              archet(*ancre(28, -96, "porte", "ancien"), 0.85, rot=30)])))
    S.add(notes(300, 330, 1.3, "#1098ad"), notes(520, 300, 1.1, "#e64980"))
    S.add(maman(130, 790, 1.05, expr="rire", bras="danse", regard=(1, 0)))
    S.add(julie(620, 790, 1.05, expr="rire", bras="danse", flip=True, regard=(-1, 0)))
    S.add(grand_maman(720, 780, 0.95, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(leon(300, 800, 0.95, expr="rire", bras="danse", regard=(1, -0.4)))
    S.add(bulle(560, 160, 400, 100, "Grand-papa, je te souhaite\nun violon qui chante\ntoute l'année !", 22, pointe=(340, 690)))
    S.cachette(70, 140, "air")
    return S


def p09():
    """Plan large : « Et toi, Léon ? À ton tour ! » Tout le monde l'entoure."""
    S = Scene()
    salon(S, soir=True)
    S.add(serpentin(30, 140, 0.9, "#ffd43b", rot=-10), serpentin(620, 330, 0.8, "#69db7c", rot=12))
    S.add(grand_papa(150, 780, 1.1, expr="content", bras="tend", regard=(1, 0)))
    S.add(grand_maman(650, 780, 1.1, expr="content", bras="tend", flip=True, regard=(-1, 0)))
    S.add(maman(280, 760, 1.05, expr="rire", bras="mains_jointes", regard=(1, 0.3)))
    S.add(julie(530, 760, 1.05, expr="rire", bras="applaudit", regard=(-1, 0.3)))
    S.add(leon(400, 800, 1.1, expr="bouche_bee", bras="joues", regard=(0, -0.3)))
    S.add(bulle(200, 150, 330, 90, "Et toi, Léon ?\nÀ ton tour !", 30, pointe=(160, 500)))
    S.add(bulle(600, 220, 330, 100, "Plein de câlins\net de beaux rêves !", 28, pointe=(640, 500)))
    S.cachette(70, 270, "air")
    return S


def p10():
    """Gros plan : Lili lâche le canapé et fait trois pas jusqu'à Léon."""
    S = Scene()
    salon(S, soir=True)
    S.add(canape(140, 800, 1.1))
    for k, px in enumerate((210, 270, 330)):
        S.add(texte(px, 770 - k * 6, str(k + 1), 40, "#e64980", contour="#fff"))
    S.add(lili(430, 800, 1.2, expr="rire", bras="ouverts", regard=(1, 0), pas="marche"))
    S.add(leon(620, 810, 1.35, expr="rire", bras="ouverts", flip=True, regard=(-1, 0.3)))
    S.add(mouvement(350, 680, 1.0, "#e64980"))
    S.camera(1.3, 480, 560)
    S.dessus(bulle(400, 100, 460, 90, "Elle marche !\nMon souhait s'est réalisé !", 28, pointe=S.vers_page(620, 470)))
    S.cachette(760, 330, "air")
    return S


def p11():
    """Plan large : le retour, la nuit ; Léon s'endort dans la voiture."""
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 40, 4, (0, 0, 800, 380))
    S.add(lune(660, 110, 44))
    collines(S, 560, "#c5d0e6", graine=7, bosquets=False)
    sol(S, 620, "#dbe4ff", bosse=8)
    S.add(maison_grands_parents(130, 610, 0.55, lumiere=True))
    S.add(sapin(300, 620, 0.6, neige=True), sapin(740, 630, 0.8, neige=True))
    S.add(chemin("M 0 760 Q 400 690 800 700 L 800 760 Q 400 750 0 800 Z", "#c5d0e6"))
    S.add(voiture(470, 740, 1.1, "#1098ad", dormeur=True))
    S.lumiere(470 + 160 * 1.1, 740 - 60 * 1.1, 90, "#fff3bf", 0.6)
    S.add(zzz(420, 560, 1.0, "#ffe066"))
    flocons(S, 20, 9, zone=(0, 0, 800, 600))
    S.add(texte(400, 400, "Bonne année, grosse santé !", 38, "#ffe066", contour="#1c2a52"))
    S.cachette(60, 680)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bonne-annee-seule.svg", vignette),
    ("01-la-route.svg", p01), ("02-les-bises.svg", p02), ("03-un-souhait.svg", p03),
    ("04-la-tourtiere.svg", p04), ("05-lili.svg", p05), ("06-la-glissade.svg", p06),
    ("07-biscotte.svg", p07), ("08-le-violon.svg", p08), ("09-a-ton-tour.svg", p09),
    ("10-trois-pas.svg", p10), ("11-le-retour.svg", p11),
]
