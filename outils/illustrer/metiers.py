"""
Tenues, coiffes et décors partagés par les livres du rayon « Les métiers »
(docteur, dentiste, pompiers, boulanger, factrice, vétérinaire, policière,
agricultrice, maître d'école, chantier).

Les personnages sont ceux de `fantastique.personne` : les morceaux de tenue se
dessinent en coordonnées locales (pieds en (0, 0), tête de rayon 50 centrée en
(0, -150), buste entre y = -106 et y = -46) et se passent à `personne` par ses
paramètres `tenue=` (sur le vêtement, sous les bras) et `coiffe=` (sur la
tête).

    S.add(pro(400, 740, 1.6, peau="brune", habit=BLANC, tenue=blouse() + stethoscope()))

Ce qui ne sert qu'à un seul livre (camion de pompiers, four, tracteur…) se
dessine dans le script de ce livre.
"""
import math

from base import *
from base import _assombrir
from fantastique import personne, PEAUX, CHEVEUX, OR

MARINE = "#243b6b"
FLUO = "#ff922b"
ARGENT = "#dee2e6"


def pro(x=0, y=0, s=1.0, **k):
    """Un adulte au travail : tunique et pantalon par défaut."""
    k.setdefault("robe", False)
    k.setdefault("coiffure", "courts")
    return personne(x, y, s, **k)


def petit(x=0, y=0, s=0.8, **k):
    """Un enfant (même dessin qu'un adulte, plus petit)."""
    k.setdefault("robe", False)
    k.setdefault("coiffure", "courts")
    k.setdefault("jambes", "#364fc7")
    return personne(x, y, s, **k)


# ---------------------------------------------------------------------------
# Tenues (coordonnées locales du personnage)
# ---------------------------------------------------------------------------

def blouse(bouton="#ced4da", stylo="#1c7ed6"):
    """Blouse blanche : revers, boutons et poche à stylo."""
    return g([chemin("M -18 -107 L 0 -78 L 18 -107", stroke="#ced4da", sw=4),
              cercle(0, -68, 3.5, bouton), cercle(0, -54, 3.5, bouton),
              rect(-30, -92, 16, 14, "none", rx=3, stroke="#ced4da", stroke_width=2.5),
              rect(-26, -100, 4, 12, stylo, rx=2)])


def stethoscope(c="#495057"):
    """Stéthoscope autour du cou : le pavillon d'un côté, les embouts de l'autre."""
    return g([chemin("M -20 -108 Q -26 -88 -16 -74", stroke=c, sw=4),
              cercle(-15, -68, 8, "#adb5bd", stroke=c, stroke_width=3),
              chemin("M 20 -108 Q 26 -92 18 -82", stroke=c, sw=4),
              chemin("M 18 -82 Q 12 -78 10 -84", stroke=c, sw=3),
              cercle(10, -86, 3.5, c), cercle(20, -80, 3.5, c)])


def badge(x=20, y=-90, c=OR, forme="ecu"):
    if forme == "rond":
        return cercle(x, y, 7, c, stroke=_assombrir(c, 0.75), stroke_width=2)
    return chemin(f"M {x - 8} {y - 8} L {x + 8} {y - 8} L {x + 8} {y + 1} Q {x} {y + 10} {x - 8} {y + 1} Z",
                  c, stroke=_assombrir(c, 0.75), sw=2)


def bandes(y1=-74, y2=-58, c1="#fcc419", c2=ARGENT, large=40):
    """Bandes réfléchissantes horizontales sur une veste."""
    m = []
    for yy in (y1, y2):
        if yy is None:
            continue
        m.append(rect(-large, yy - 4, 2 * large, 8, c1))
        m.append(rect(-large, yy - 1.5, 2 * large, 3, c2))
    return g(m)


def veste_pompier():
    """Col montant, fermeture et bandes jaunes et grises de la veste de feu."""
    return g([chemin("M -22 -108 L -14 -96 L 14 -96 L 22 -108", stroke="#1b2a4a", sw=6),
              trait(0, -96, 0, -48, "#1b2a4a", 3),
              bandes(-80, -56), rect(-26, -46, 20, 8, "#fcc419"), rect(6, -46, 20, 8, "#fcc419")])


def gilet_chantier(c=FLUO):
    """Gilet orange bien visible, avec bandes grises."""
    return g([chemin("M -32 -106 L -14 -106 L 0 -80 L 14 -106 L 32 -106 L 40 -46 Q 0 -36 -40 -46 Z", c),
              rect(-40, -74, 80, 7, ARGENT), rect(-40, -58, 80, 7, ARGENT)])


def salopette(c="#2f9e44", poche="#2b8a3e"):
    """Bavette et bretelles d'une salopette (le pantalon se règle avec `jambes`)."""
    return g([rect(-24, -92, 48, 48, c, rx=4),
              trait(-20, -92, -26, -106, c, 7), trait(20, -92, 26, -106, c, 7),
              cercle(-18, -88, 4, OR), cercle(18, -88, 4, OR),
              rect(-12, -80, 24, 16, poche, rx=3)])


def tablier(c="#ffffff", bord="#e9ecef", poche=True):
    """Grand tablier noué à la taille, qui descend sur les jambes."""
    m = [chemin("M -24 -104 L 24 -104 L 26 -74 L 40 -70 L 44 -16 Q 0 -8 -44 -16 L -40 -70 L -26 -74 Z",
                c, stroke=bord, sw=2),
         trait(-40, -72, 40, -72, bord, 4)]
    if poche:
        m.append(rect(-16, -56, 32, 20, "none", rx=4, stroke=bord, stroke_width=3))
    return g(m)


def uniforme_police():
    """Écusson, badge, poches et radio de l'uniforme bleu marine."""
    return g([rect(-30, -86, 20, 14, "none", rx=3, stroke="#1b2a4a", stroke_width=2.5),
              rect(10, -86, 20, 14, "none", rx=3, stroke="#1b2a4a", stroke_width=2.5),
              badge(-20, -94, OR), trait(0, -106, 0, -48, "#1b2a4a", 2.5),
              rect(18, -108, 12, 18, "#343a40", rx=3), trait(26, -108, 28, -118, "#343a40", 3),
              rect(-38, -62, 76, 10, "#1b2a4a", rx=5), rect(-6, -63, 12, 12, "#adb5bd", rx=2)])


def veste_factrice(c="#1971c2"):
    """Bandes et poche de la veste de la factrice."""
    return g([rect(-38, -74, 76, 9, c), rect(-38, -74, 76, 3, ARGENT),
              rect(8, -96, 20, 14, "none", rx=3, stroke=c, stroke_width=2.5),
              chemin("M -16 -107 L 0 -94 L 16 -107", stroke=c, sw=4)])


def bandouliere(c="#5c3a1e"):
    """Courroie en travers du buste (pour une sacoche portée sur le côté)."""
    return trait(-26, -104, 34, -54, c, 6)


def sacoche(x, y, s=1.0, c="#5c3a1e", lettre=True):
    """Sacoche de courrier ; (x, y) = bas de la sacoche."""
    m = [rect(-34, -54, 68, 54, c, rx=8),
         chemin("M -34 -54 L 34 -54 L 34 -30 Q 0 -20 -34 -30 Z", _assombrir(c, 0.8)),
         rect(-6, -32, 12, 10, OR, rx=2)]
    if lettre:
        m.insert(0, rect(-24, -70, 40, 26, "#fff", rx=2, rot=None, stroke="#dee2e6", stroke_width=2))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Coiffes (coordonnées locales du personnage)
# ---------------------------------------------------------------------------

def casque_pompier(c="#e03131", visiere=True):
    fonce = _assombrir(c, 0.75)
    m = [chemin("M -62 -152 Q -66 -226 0 -228 Q 66 -226 62 -152 Z", c),
         chemin("M -10 -226 Q 0 -236 10 -226 L 8 -160 L -8 -160 Z", fonce),
         ellipse(0, -154, 70, 11, fonce),
         chemin("M 0 -210 L 14 -204 L 12 -186 Q 0 -178 -12 -186 L -14 -204 Z", OR, stroke="#f59f00", sw=2)]
    if visiere:
        m.append(chemin("M -48 -168 Q 0 -178 48 -168 L 48 -160 Q 0 -168 -48 -160 Z", "#fff3bf", opacity=0.75))
    # remonté pour laisser voir les yeux et les sourcils
    return g(m, "translate(0 -24)")


def casque_chantier(c="#fcc419"):
    fonce = _assombrir(c, 0.8)
    return g([chemin("M -56 -162 Q -58 -224 0 -226 Q 58 -224 56 -162 Z", c),
              chemin("M -8 -224 Q 0 -230 8 -224 L 8 -166 L -8 -166 Z", fonce),
              ellipse(0, -164, 68, 10, fonce),
              trait(-30, -214, -40, -176, "#fff", 4, opacity=0.5)], "translate(0 -12)")


def casquette(c="#1971c2", insigne=None, visiere=None):
    """Casquette vue de face ; insigne = couleur d'un petit écusson."""
    visiere = visiere or _assombrir(c, 0.7)
    m = [chemin("M -54 -170 Q -54 -220 0 -222 Q 54 -220 54 -170 Z", c),
         ellipse(0, -168, 52, 11, visiere),
         rect(-54, -182, 108, 12, _assombrir(c, 0.85), rx=4)]
    if insigne:
        m.append(badge(0, -200, insigne, "ecu"))
    return g(m, "translate(0 -12)")


def casquette_police():
    """Casquette bleu marine à bande et écusson doré."""
    return g([chemin("M -62 -184 Q -60 -222 0 -224 Q 60 -222 62 -184 Z", MARINE),
              rect(-54, -186, 108, 18, "#1b2a4a", rx=4),
              rect(-54, -180, 108, 5, ARGENT),
              ellipse(0, -168, 52, 10, "#111827"),
              badge(0, -204, OR)])


def chapeau_paille(c="#f6d38b", ruban="#e03131"):
    fonce = _assombrir(c, 0.85)
    return g([ellipse(0, -182, 98, 20, c, stroke=fonce, stroke_width=3),
              chemin("M -50 -184 Q -50 -238 0 -240 Q 50 -238 50 -184 Z", c, stroke=fonce, sw=3),
              rect(-50, -200, 100, 14, ruban, rx=4)])


def calot(c="#74c0fc", pois="#ffffff"):
    """Calot de soins (dentiste, vétérinaire)."""
    m = [chemin("M -56 -156 Q -64 -224 0 -228 Q 64 -224 56 -156 Q 0 -178 -56 -156 Z", c)]
    for x, y in ((-30, -200), (0, -214), (30, -200), (-16, -180), (18, -182)):
        m.append(cercle(x, y, 4.5, pois, opacity=0.8))
    return g(m)


def masque_soin(c="#a5d8ff", baisse=False):
    """Masque de soin : sur la bouche, ou baissé sous le menton."""
    y = -100 if baisse else -128
    m = [trait(-30, y - 6, -48, -150, "#e7f5ff", 2.5), trait(30, y - 6, 48, -150, "#e7f5ff", 2.5),
         rect(-30, y - 16, 60, 32, c, rx=10)]
    for k in (-6, 2, 10):
        m.append(trait(-24, y + k - 2, 24, y + k - 2, _assombrir(c, 0.85), 1.5))
    return g(m)


def lampe_frontale(c="#495057"):
    return g([chemin("M -52 -176 Q 0 -196 52 -176", stroke=c, sw=7),
              rect(-14, -200, 28, 22, c, rx=6), cercle(0, -189, 7, "#fff3bf")])


# ---------------------------------------------------------------------------
# Petits objets et décors communs
# ---------------------------------------------------------------------------

def roue(x, y, r=40, pneu="#343a40", jante="#ced4da"):
    return g([cercle(x, y, r, pneu), cercle(x, y, r * 0.55, jante), cercle(x, y, r * 0.18, "#868e96")])


def gyrophare(x, y, s=1.0, c="#4dabf7", allume=True):
    m = [rect(-18, -4, 36, 8, "#495057", rx=3), chemin("M -14 -4 Q -14 -26 0 -26 Q 14 -26 14 -4 Z", c)]
    if allume:
        for a in (-150, -120, -60, -30):
            r = math.radians(a)
            m.append(trait(math.cos(r) * 26, -14 + math.sin(r) * 26, math.cos(r) * 40, -14 + math.sin(r) * 40, c, 4))
    return place(m, x, y, s)


def lettre(x, y, s=1.0, c="#ffffff", rot=0, timbre="#fa5252"):
    """Enveloppe fermée ; (x, y) = centre."""
    return place([rect(-40, -26, 80, 52, c, rx=4, stroke="#ced4da", stroke_width=2),
                  chemin("M -40 -24 L 0 4 L 40 -24", stroke="#ced4da", sw=2),
                  rect(22, -20, 12, 14, timbre, rx=1)], x, y, s, rot=rot)


def colis(x, y, s=1.0, w=120, h=90, c="#d9a066", rot=0):
    """Paquet fermé de ruban adhésif ; (x, y) = milieu de la base."""
    return place([rect(-w / 2, -h, w, h, c, rx=4), rect(-w / 2, -h, w, h * 0.12, _assombrir(c, 0.88)),
                  rect(-8, -h, 16, h, "#e9c58b"), rect(w / 2 - 44, -h + 22, 34, 22, "#fff", rx=2)],
                 x, y, s, rot=rot)


def autocollant(x, y, s=1.0, c="#fcc419", forme="etoile"):
    if forme == "coeur":
        return coeur(x, y, s, c)
    return place([cercle(0, 0, 26, "#fff", stroke="#dee2e6", stroke_width=2), etoile5(0, 1, 20, c)], x, y, s)


def cabinet(S, mur="#e7f5ff", sol_c="#d0ebff", y=600, plinthe="#a5d8ff"):
    """Pièce claire d'un cabinet de soins."""
    interieur(S, mur, sol_c, y, plinthe=plinthe)
    for x in range(0, 800, 80):
        S.add(trait(x, y, x - 40, 800, "#ffffff", 2, opacity=0.6))


def rue(S, y=600, trottoir="#ced4da", chaussee="#868e96", passage=False, graine=4):
    """Rue de ville : immeubles, trottoir et chaussée."""
    from fables import ville
    S.add(rect(0, 0, 800, 800, S.degrade(["#74c0fc", "#e7f5ff"])))
    ville(S, y - 40)
    S.add(rect(0, y - 40, 800, 50, trottoir))
    S.add(rect(0, y + 10, 800, 800 - y - 10, chaussee))
    for x in range(20, 800, 140):
        S.add(rect(x, y + 120, 70, 10, "#f8f9fa", rx=3))
    if passage:
        for k in range(6):
            S.add(rect(250 + k * 50, y + 20, 30, 180, "#f8f9fa", rx=3))
