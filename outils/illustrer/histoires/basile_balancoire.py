"""Basile se balance — le pendule.

Une balançoire ou un pendule oscille autour de sa position basse. Pour de
petits élans, la durée d'un aller-retour ne dépend presque pas de l'amplitude
ni de la masse, mais de la longueur : fil court, oscillations rapides (traces
nombreuses et serrées) ; fil long, oscillations lentes.
"""
import math

from base import *
from objets import *
from sciences import *
from contes import horloge_comtoise

ID = "basile-balancoire"
BASILE = dict(acc=("casque",), couleur_acc="#fab005")
MAMIE = dict(couleur="#a47148", acc=("lunettes", "echarpe"), couleur_acc="#cc5de8")
ROSALIE = dict(acc=("noeud",), couleur_acc="#f783ac")


def basile(x, y, s=1.0, **k):
    return perso("singe", x, y, s, **{**dict(acc=(), habit="#fab005"), **k})


def rosalie(x, y, s=0.95, **k):
    return perso("lapin", x, y, s, **{**ROSALIE, **k})


def mamie(x, y, s=1.15, **k):
    return perso("singe", x, y, s, **{**MAMIE, **k})


# ---------------------------------------------------------------------------
# Balançoires et pendules
# ---------------------------------------------------------------------------

def portique(x, y_haut, y_sol, l=420, couleur="#e8590c"):
    """Portique vu de côté : un « A » dont le sommet porte la balançoire."""
    h = y_sol - y_haut
    m = []
    for sgn in (-1, 1):
        m.append(poly([(x - 10, y_haut), (x + 10, y_haut), (x + sgn * l / 2 + 14, y_sol), (x + sgn * l / 2 - 14, y_sol)], couleur))
    m.append(rect(x - l * 0.28, y_haut + h * 0.55, l * 0.56, 16, couleur, rx=6))
    m.append(cercle(x, y_haut, 22, _fonce(couleur)))
    return g(m)


def _fonce(c):
    from base import _assombrir
    return _assombrir(c, 0.8)


def siege(x, y_haut, longueur, angle=0, passager="", couleur="#fab005", opacity=None, ecart=70):
    """Cordes + planche accrochées en (x, y_haut), inclinées de `angle` degrés.

    `passager` est dessiné en coordonnées locales, la planche étant en (0, longueur).
    """
    m = [trait(-ecart, 0, -ecart, longueur, "#495057", 6), trait(ecart, 0, ecart, longueur, "#495057", 6)]
    if passager:
        m.append(passager)
    m.append(rect(-ecart - 20, longueur - 8, 2 * ecart + 40, 22, couleur, rx=8))
    a = {"opacity": opacity} if opacity is not None else {}
    return g([place(m, x, y_haut, rot=-angle)], **a)


def assis(longueur, s=1.0, quoi=None, **k):
    """Un personnage assis sur la planche (jambes sous la planche)."""
    quoi = quoi or basile
    return quoi(0, longueur + 70 * s, s, bras="haut", **k)


def ecrou(x, y, s=1.0, couleur="#adb5bd"):
    pts = [(math.cos(math.radians(a)) * 26, math.sin(math.radians(a)) * 26) for a in range(0, 360, 60)]
    return place([poly(pts, couleur, stroke="#868e96", stroke_width=3), cercle(0, 0, 10, "#fff", stroke="#868e96", stroke_width=3)], x, y, s)


def gomme(x, y, s=1.0):
    return place([rect(-22, -16, 44, 32, "#ff8fab", rx=6), rect(4, -16, 18, 32, "#4dabf7", rx=4)], x, y, s)


def pendule(x, y, longueur, angle=0, objet=None, opacity=None, couleur_fil="#495057"):
    objet = objet if objet is not None else ecrou(0, 0)
    m = [trait(0, 0, 0, longueur, couleur_fil, 3), place(objet, 0, longueur)]
    a = {"opacity": opacity} if opacity is not None else {}
    return g([place(m, x, y, rot=-angle)], **a)


def fantomes(fn, angles, opacite=0.3):
    """Positions successives en transparence, la dernière bien visible."""
    m = [fn(a, opacite) for a in angles[:-1]]
    m.append(fn(angles[-1], None))
    return g(m)


def arc_fleche(x, y, r, a0, a1, couleur="#f76707", sw=6):
    """Flèche en arc de cercle centrée en (x, y), de l'angle a0 à a1 (0 = vers le bas)."""
    def pt(a):
        return x + r * math.sin(math.radians(a)), y + r * math.cos(math.radians(a))
    x0, y0 = pt(a0)
    x1, y1 = pt(a1)
    sens = 0 if a1 > a0 else 1
    direction = math.degrees(math.atan2(-(math.sin(math.radians(a1)) * (1 if a1 < a0 else -1)), math.cos(math.radians(a1)) * (1 if a1 > a0 else -1)))
    d = f"M {x0:.1f} {y0:.1f} A {r} {r} 0 0 {sens} {x1:.1f} {y1:.1f}"
    # tangente au point d'arrivée
    t = math.radians(a1)
    tx, ty = (math.cos(t), -math.sin(t)) if a1 > a0 else (-math.cos(t), math.sin(t))
    return fleche_courbe(d, (x1, y1), math.degrees(math.atan2(ty, tx)), couleur, sw, 20)


def parc(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(690, 100, 45))
    S.add(nuage(160, 110, 0.6))
    collines(S, 600, "#b2f2bb", graine=graine)
    sol(S, 640, "#8ce99a")
    S.add(arbre(80, 650, 0.9), buisson(740, 660, 0.8))


def salon(S):
    interieur(S, "#fff4e6", "#c68642", 600, papier="#ffe8cc")


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    parc(S, 2)
    S.add(portique(400, 170, 700, 460))
    S.add(siege(400, 170, 360, angle=28, passager=assis(360, 1.25, expr="rire")))
    S.add(mouvement(180, 520, 1.2, rot=200))
    S.add(texte(620, 300, "Youpi !", 76, "#e8590c", contour="#fff", rot=8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trait(80, 12, 320, 12, "#e8590c", 14))
    S.add(siege(200, 12, 150, angle=0, passager=assis(150, 0.62, expr="content"), ecart=40))
    return S


def p01():
    S = Scene()
    parc(S, 1)
    S.add(portique(400, 170, 700, 460))
    S.add(siege(400, 170, 360, angle=-30, passager=assis(360, 1.2, expr="rire")))
    S.add(texte(230, 320, "Plus haut !", 64, "#e8590c", contour="#fff", rot=-6))
    return S


def p02():
    S = Scene()
    parc(S, 3)
    S.add(portique(400, 150, 700, 460))
    S.add(fantomes(lambda a, o: siege(400, 150, 360, a, assis(360, 1.0, expr="joie"), opacity=o), [-32, 32, 0]))
    S.add(arc_fleche(400, 150, 470, -32, 32), arc_fleche(400, 150, 500, 32, -32, "#1c7ed6"))
    S.add(texte(160, 720, "aller", 56, "#f76707"), texte(650, 720, "retour", 56, "#1c7ed6"))
    return S


def p03():
    S = Scene()
    parc(S, 4)
    S.add(portique(400, 170, 700, 460))
    S.add(siege(400, 170, 360, 0, assis(360, 1.2, expr="inquiet")))
    for k, a in enumerate([30, 18, 8]):
        S.add(arc_fleche(400, 170, 520 + k * 14, -a, a, "#adb5bd", 5))
    S.add(texte(650, 300, "Oh…", 64, "#868e96", contour="#fff"))
    return S


def p04():
    S = Scene()
    parc(S, 5)
    S.add(portique(430, 170, 700, 460))
    S.add(siege(430, 170, 360, -30, assis(360, 1.15, expr="rire")))
    S.add(rosalie(150, 780, 1.1, expr="concentre", bras="donne", regard=(1, -0.3)))
    S.add(fleche(250, 520, 360, 470, "#e8590c", 8, 26))
    S.add(texte(560, 300, "Hop !", 70, "#e8590c", contour="#fff"))
    return S


def p05():
    S = Scene()
    parc(S, 6)
    S.add(portique(400, 170, 700, 460))
    S.add(siege(400, 170, 360, 40, assis(360, 1.15, expr="fier")))
    S.add(rosalie(680, 780, 0.9, expr="rire", bras="haut"))
    S.add(texte(560, 290, "Tout seul !", 60, "#e8590c", contour="#fff", rot=6))
    S.add(mouvement(470, 560, 1.0, rot=10))
    return S


def support(S, x0=150, x1=650, y=180):
    """Crayon posé entre deux piles de livres, d'où pendent les ficelles."""
    S.add(livres_pile(x0, 560, 1.4), livres_pile(x1, 560, 1.4))
    S.add(rect(x0 - 20, 560 - 360, 40, 360, "#c68642"), rect(x1 - 20, 560 - 360, 40, 360, "#c68642"))
    S.add(rect(x0 - 30, y - 12, x1 - x0 + 60, 18, "#ffd43b", rx=6), poly([(x1 + 30, y - 12), (x1 + 60, y - 3), (x1 + 30, y + 6)], "#f3d9b1"))


def p06():
    S = Scene()
    salon(S)
    S.add(table(400, 790, 700, 140, "#a0693a"))
    support(S, 200, 600, 200)
    S.add(fantomes(lambda a, o: pendule(400, 200, 330, a, opacity=o), [-25, 25, 0]))
    S.add(basile(680, 780, 0.9, expr="joie", bras="montre", regard=(-1, -0.4)))
    return S


def p07():
    S = Scene()
    fond(S, "#fff9db")
    S.add(rect(397, 60, 6, 680, "#dee2e6"))
    for x, amp, mot in [(200, 12, "petit élan"), (600, 35, "grand élan")]:
        S.add(trait(x - 120, 140, x + 120, 140, "#a0693a", 14))
        S.add(fantomes(lambda a, o, x=x: pendule(x, 140, 330, a, opacity=o), [-amp, amp, 0]))
        S.add(arc_fleche(x, 140, 380, -amp, amp, "#f76707", 5))
        S.add(texte(x, 100, mot, 44, "#495057"))
        S.add(horloge(x, 640, 48, heure=12, minute=10, bord="#f08c00"))
    S.add(texte(400, 760, "presque pareil !", 50, "#e8590c"))
    S.cachette(430, 70, "air")
    return S


def p08():
    S = Scene()
    fond(S, "#e7f5ff")
    S.add(trait(120, 160, 680, 160, "#a0693a", 14))
    for x, obj in [(240, ecrou(0, 0, 1.6)), (580, gomme(0, 0, 1.6))]:
        S.add(fantomes(lambda a, o, x=x, obj=obj: pendule(x, 160, 380, a, objet=obj, opacity=o), [-15, 15, -8]))
    S.add(texte(220, 690, "lourd", 50, "#495057"), texte(590, 690, "léger", 50, "#e64980"))
    S.add(texte(400, 100, "Même rythme !", 56, "#1c7ed6"))
    S.cachette(450, 730, "air")
    return S


def p09():
    S = Scene()
    fond(S, "#fff4e6")
    S.add(trait(80, 140, 720, 140, "#a0693a", 14))
    S.add(fantomes(lambda a, o: pendule(230, 140, 160, a, opacity=o), [-30, -10, 10, 30, 0], 0.25))
    S.add(fantomes(lambda a, o: pendule(560, 140, 460, a, opacity=o), [-20, 20, 0], 0.25))
    S.add(texte(230, 440, "court :", 46, "#e03131"), texte(230, 500, "vite !", 56, "#e03131"))
    S.add(texte(560, 720, "long : lentement", 46, "#1c7ed6"))
    S.add(basile(130, 790, 0.7, expr="surpris", bras="joues"))
    S.cachette(400, 70, "air")
    return S


def p10():
    S = Scene()
    parc(S, 10)
    S.add(portique(250, 130, 700, 300, "#4c6ef5"))
    S.add(siege(250, 130, 430, -10, "", "#74c0fc"))
    S.add(arc_fleche(250, 130, 520, -14, 14, "#1c7ed6", 6))
    S.add(portique(600, 380, 700, 220, "#e8590c"))
    S.add(siege(600, 380, 200, 20, "", "#fab005", ecart=50))
    S.add(arc_fleche(600, 380, 270, -24, 24, "#f76707", 6))
    S.add(texte(250, 90, "lentement", 46, "#1c7ed6", contour="#fff"), texte(600, 340, "vite", 46, "#e8590c", contour="#fff"))
    S.add(basile(450, 790, 0.75, expr="fier", bras="montre", regard=(-1, -1)))
    return S


def p11():
    S = Scene()
    salon(S)
    S.add(cadre_mur(160, 200), cadre_mur(640, 230, contenu_couleur="#ffd8a8"))
    S.add(horloge_comtoise(400, 760, 1.15))
    S.add(mamie(150, 780, 1.0, expr="sourire", bras="montre", regard=(1, -0.3)))
    S.add(basile(650, 780, 0.85, expr="bouche_bee", bras="bas", regard=(-1, -0.3)))
    S.add(texte(250, 360, "tic…", 54, "#e8590c", contour="#fff"), texte(560, 400, "tac…", 54, "#e8590c", contour="#fff"))
    return S


def metronome(x, y, s=1.0, angle=20):
    m = [poly([(-70, 0), (70, 0), (30, -260), (-30, -260)], "#a0693a"),
         poly([(-46, -20), (46, -20), (20, -230), (-20, -230)], "#ffe8cc"),
         place([trait(0, 0, 0, -230, "#495057", 6), rect(-14, -170, 28, 30, "#495057", rx=4)], 0, -30, rot=angle)]
    return place(m, x, y, s)


def tambour(x, y, s=1.0):
    return place([rect(-70, -90, 140, 90, "#e03131", rx=10), ellipse(0, -90, 70, 20, "#fff4e6", stroke="#c92a2a", stroke_width=4),
                  g([trait(-70 + k * 35, -80, -52 + k * 35, -10, "#ffd43b", 4) for k in range(4)])], x, y, s)


def p12():
    S = Scene()
    salon(S)
    S.add(table(220, 790, 300, 160, "#a0693a"))
    S.add(metronome(220, 612, 0.9, 20), place(metronome(0, 0, 0.9, -20), 220, 612), )
    S.add(basile(540, 760, 1.2, expr="chante", bras="large"))
    S.add(tambour(540, 790, 1.2))
    S.add(notes(420, 260, 1.2, "#e8590c"), texte(620, 300, "boum !", 50, "#e03131", contour="#fff"))
    return S


def p13():
    S = Scene()
    ciel(S, "#c3fae8", "#ebfbee")
    S.add(rect(0, 0, 800, 120, "#2f9e44"), g([cercle(k * 90, 110, 70, "#37b24d") for k in range(10)]))
    S.add(place([chemin("M 0 0 L 0 380", stroke="#2b8a3e", sw=10), perso("singe", 0, 590, 1.0, expr="rire", bras="haut")], 220, 110, rot=-25))
    S.add(place([chemin("M 0 0 L 0 330", stroke="#2b8a3e", sw=10)], 560, 110, rot=15))
    S.add(basile(600, 640, 0.95, expr="joie", bras="haut", rot=-12))
    S.add(arc_fleche(220, 110, 560, -30, 10, "#f76707", 6))
    S.add(g([herbe(60 + k * 120, 790, 1.4) for k in range(7)]))
    S.cachette(730, 260, "air")
    return S


def p14():
    S = Scene()
    parc(S, 14)
    S.add(rect(0, 690, 800, 70, "#e9c38c"))
    for k, (x, o) in enumerate([(220, 0.3), (400, 0.55), (580, None)]):
        a = {"opacity": o} if o else {}
        S.add(g([basile(x, 760, 1.0, expr="content", bras="course" if k % 2 else "bas", flip=bool(k % 2))], **a))
    S.add(texte(400, 300, "Balance, balance…", 56, "#e8590c", contour="#fff"))
    return S


def p15():
    S = Scene()
    parc(S, 15)
    S.add(trait(70, 170, 730, 170, "#e8590c", 22))
    for x, quoi, extra in [(170, rosalie, {}), (400, basile, {}), (630, lambda *a, **k: perso("cochon", *a, **k), {})]:
        S.add(siege(x, 170, 340, -22, assis(340, 0.9, quoi=quoi, expr="rire", **extra), ecart=60))
    S.add(texte(400, 120, "Tous ensemble !", 56, "#e8590c", contour="#fff"))
    return S


def p16():
    S = Scene()
    nuit(S)
    etoiles(S, 30, 16, (0, 0, 800, 420))
    S.add(lune(650, 120, 45))
    sol(S, 640, "#2b8a3e")
    S.add(arbre(110, 660, 1.1, "#2f9e44", "#2b8a3e"), arbre(690, 660, 1.1, "#2f9e44", "#2b8a3e"))
    S.add(chemin("M 140 420 Q 400 640 660 420", stroke="#fff4e6", sw=6))
    S.add(chemin("M 160 430 Q 400 700 640 430 Q 400 610 160 430 Z", "#ff922b"))
    S.add(place(basile(0, 0, 0.8, expr="dort"), 400, 590, rot=0))
    S.add(chemin("M 160 430 Q 400 700 640 430 Q 400 650 160 430 Z", "#ff922b"))
    S.add(zzz(520, 380, 1.2, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("basile-seul.svg", vignette),
    ("01-au-parc.svg", p01), ("02-aller-retour.svg", p02), ("03-ca-s-arrete.svg", p03), ("04-pousser.svg", p04),
    ("05-tout-seul.svg", p05), ("06-le-pendule.svg", p06), ("07-petit-grand-elan.svg", p07), ("08-lourd-leger.svg", p08),
    ("09-court-long.svg", p09), ("10-deux-balancoires.svg", p10), ("11-l-horloge.svg", p11), ("12-metronome.svg", p12),
    ("13-les-lianes.svg", p13), ("14-les-bras.svg", p14), ("15-tous-ensemble.svg", p15), ("16-le-hamac.svg", p16),
]
