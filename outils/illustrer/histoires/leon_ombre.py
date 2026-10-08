"""L'ombre de Léon — l'ombre au fil de la journée.

On regarde vers le sud : le Soleil se lève à gauche (est), passe haut dans
le ciel à midi et se couche à droite (ouest). L'ombre part toujours du côté
opposé au Soleil : longue vers la droite le matin, toute petite à midi,
longue vers la gauche le soir. Sous un nuage elle pâlit ; sans Soleil elle
disparaît ; sous un lampadaire, elle revient (côté opposé à la lampe).
"""
from base import *
from objets import *
from sciences import *
from sciences import _filtre_ombre
from fantastique import personne

ID = "leon-ombre"
# les ombres de ce livre sont de vraies ombres portées
OMBRES_DOUCES = False
LEON = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#40c057", robe=False, jambes="#1971c2")
ROSE_ = dict(peau="claire", cheveux="blond", coiffure="queue", habit="#f783ac", robe=True)
MAMAN = dict(peau="brune", cheveux="noir", coiffure="chignon", habit="#7048e8", robe=True)


def leon(x=0, y=0, s=1.0, **k):
    return personne(x, y, s, **{**LEON, **k})


def avec_ombre(S, x, y, s, longueur, cote=1, alpha=0.42, qui=leon, **k):
    S.add(ombre_portee(S, qui(0, 0, s, **k), x, y, longueur, cote, alpha=alpha))
    S.add(qui(x, y, s, **k))


def trace_craie(S, x, y, s, longueur, cote=1, **k):
    """Silhouette de l'ombre tracée et coloriée à la craie sur le sol."""
    fid = _filtre_ombre(S, 0.55, (1, 1, 1))
    return g(leon(0, 0, s, **k), filter=f"url(#{fid})",
             transform=f"matrix(0 0.42 {n(-cote * longueur)} 0 {n(x)} {n(y)})")


def croix(x, y, c="#ffffff"):
    return g([trait(x - 18, y - 8, x + 18, y + 8, c, 6), trait(x - 18, y + 8, x + 18, y - 8, c, 6)])


def pre(S, haut="#74c0fc", bas="#e7f5ff", y=600, graine=1):
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#7bd88a", y2=y + 90)


def cour(S, haut="#74c0fc", bas="#e7f5ff", y=560, graine=1):
    """Ciel, une haie et le sol gris de la cour, où l'on dessine à la craie."""
    ciel(S, haut, bas)
    collines(S, y, "#b2f2bb", graine=graine)
    for k in range(9):
        S.add(buisson(50 + k * 95, y + 10, 0.8))
    S.add(rect(0, y, 800, 800 - y, "#ced4da"))
    for k in range(1, 4):
        S.add(trait(0, y + k * 70, 800, y + k * 70, "#adb5bd", 3))


def soleil_bas(S, x, y):
    S.add(cercle(x, y, 140, "#ffe066", opacity=0.35), soleil(x, y, 50, visage=True))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    pre(S, "#ffc078", "#fff4e6", 640, 2)
    soleil_bas(S, 90, 520)
    avec_ombre(S, 240, 730, 1.3, 2.2, 1, expr="rire", bras="haut")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ombre_sous(200, 262, 70, 0.25))
    S.add(leon(200, 262, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    pre(S, "#ffa94d", "#fff4e6", 600, 3)
    soleil_bas(S, 80, 470)
    S.add(maison(110, 600, 0.75, "#ffe8cc", "#e8590c"))
    avec_ombre(S, 240, 730, 1.25, 2.0, 1, expr="bouche_bee", regard=(1, 1))
    S.add(bulle(500, 160, 330, 80, "Je suis un géant !", 38, pointe=(330, 420)))
    return S


def p02():
    S = Scene()
    pre(S, "#ffc078", "#fff4e6", 600, 4)
    soleil_bas(S, 80, 420)
    avec_ombre(S, 230, 730, 1.25, 1.7, 1, expr="rire", bras="ouverts")
    S.add(mouvement(110, 560, 1.0, rot=-30), mouvement(350, 560, 1.0, rot=30))
    S.add(texte(600, 280, "Pareil !", 70, "#e8590c", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    pre(S, "#74c0fc", "#e7f5ff", 600, 5)
    sx, sy = 90, 300
    S.add(soleil(sx, sy, 50, visage=True))
    x, y, s = 330, 730, 1.25
    tete_y = y - 210 * s
    L = 1.5
    bout = x + L * 210 * s
    S.add(rayons_soleil(sx + 60, sy + 20, 760, 620, nb=1))
    S.add(trait(sx + 55, sy + 30, bout, y, "#fcc419", 5, stroke_dasharray="14 10"))
    S.add(trait(sx + 60, sy + 50, x - 20, y - 60, "#fcc419", 5, stroke_dasharray="14 10"))
    avec_ombre(S, x, y, s, L, 1, expr="sourire", regard=(-1, -1))
    S.add(texte(580, 680, "l'ombre", 44, "#495057", contour="#fff"))
    S.add(texte(560, 200, "La lumière ne passe pas", 32, "#e8590c", contour="#fff"))
    S.add(texte(560, 240, "à travers Léon.", 32, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    cour(S, "#91a7ff", "#e7f5ff", graine=2)
    soleil_bas(S, 90, 380)
    S.add(trace_craie(S, 250, 720, 1.2, 1.6, 1))
    S.add(croix(250, 722))
    avec_ombre(S, 250, 720, 1.2, 1.6, 1, expr="concentre", regard=(1, 1))
    maman = personne(620, 760, 1.25, **MAMAN, expr="sourire", bras="montre", regard=(-1, 1), flip=True)
    S.add(maman)
    S.add(horloge(680, 110, 48, heure=9))
    return S


def p05():
    S = Scene()
    cour(S, "#339af0", "#d0ebff", graine=3)
    S.add(soleil(400, 90, 55, visage=True))
    S.add(trace_craie(S, 330, 720, 1.2, 1.6, 1))
    S.add(croix(330, 722))
    S.add(ellipse(330, 728, 46, 13, "#1b1f3b", opacity=0.35))
    S.add(leon(330, 720, 1.2, expr="surpris", regard=(0, 1)))
    S.add(horloge(680, 110, 48, heure=12))
    return S


def p06():
    S = Scene()
    cour(S, "#adb5bd", "#e9ecef", graine=4)
    S.add(soleil(430, 110, 50))
    S.add(nuage(430, 130, 1.7, "#ced4da", ombre="#adb5bd"))
    S.add(ombre_portee(S, leon(0, 0, 1.2), 330, 720, 0.3, 1, alpha=0.1))
    S.add(leon(330, 720, 1.2, expr="inquiet", regard=(1, 1), bras="joues"))
    S.add(texte(600, 520, "?", 90, "#495057", contour="#fff"))
    return S


def p07():
    S = Scene()
    cour(S, "#f76707", "#ffd8a8", graine=5)
    soleil_bas(S, 720, 400)
    S.add(trace_craie(S, 400, 720, 1.2, 1.6, 1))
    S.add(croix(400, 722))
    avec_ombre(S, 400, 720, 1.2, 1.6, -1, expr="rire", regard=(-1, 1))
    S.add(horloge(90, 110, 48, heure=5))
    return S


def p08():
    S = Scene()
    pre(S, "#ffc078", "#fff4e6", 600, 6)
    soleil_bas(S, 720, 380)
    rose = lambda x=0, y=0, s=1.0, **k: personne(x, y, s, **{**ROSE_, **k})
    avec_ombre(S, 560, 700, 1.15, 1.4, -1, qui=rose, expr="rire", bras="haut")
    avec_ombre(S, 170, 740, 1.15, 1.4, -1, expr="rire", bras="course", regard=(1, 1))
    S.add(bulle(380, 140, 420, 80, "Je marche sur ton ombre !", 32, pointe=(220, 430)))
    return S


def p09():
    S = Scene()
    pre(S, "#5f3dc4", "#ffa94d", 600, 7)
    S.add(cercle(640, 600, 60, "#ff922b", opacity=0.6))
    collines(S, 600, "#8ce99a", graine=7)
    sol(S, 600, "#69db7c", couleur2="#5cc86c", y2=690)
    S.add(leon(400, 730, 1.3, expr="baille", bras="bas"))
    etoiles(S, 8, 2, zone=(0, 0, 800, 200))
    S.add(texte(400, 200, "Plus de soleil, plus d'ombre…", 38, "#fff3bf", contour="#5f3dc4"))
    return S


def p10():
    S = Scene()
    nuit(S)
    etoiles(S, 40, 3, zone=(0, 0, 800, 400))
    S.add(lune_phase(660, 110, 36, 0.4, croissante=True))
    S.add(rect(0, 600, 800, 200, "#495057"))
    # lampadaire à gauche ; la lumière vient d'en haut à gauche
    lx = 150
    S.add(poly([(lx + 40, 160), (lx - 90, 720), (lx + 330, 720)], "#fff3bf", opacity=0.22))
    S.add(rect(lx - 8, 160, 16, 560, "#343a40"), rect(lx - 8, 160, 70, 14, "#343a40", rx=6))
    S.add(chemin(f"M {lx + 30} 172 L {lx + 80} 172 L {lx + 70} 200 L {lx + 40} 200 Z", "#343a40"), cercle(lx + 55, 206, 14, "#ffe066"))
    avec_ombre(S, 360, 730, 1.25, 1.1, 1, alpha=0.55, expr="rire", bras="salut")
    S.add(bulle(560, 260, 260, 80, "La revoilà !", 38, pointe=(480, 470)))
    return S


def p11():
    S = Scene()
    fond(S, "#ced4da")
    for k in range(1, 8):
        S.add(trait(0, k * 100, 800, k * 100, "#adb5bd", 3))
    # vue de dessus : trois ombres tracées autour de la même croix
    cx, cy = 400, 440
    fid = _filtre_ombre(S, 0.85, (1, 1, 1))
    # un dessin neuf par ombre : chaque personnage porte ses propres identifiants
    S.add(g(leon(0, 0, 0.9), filter=f"url(#{fid})", transform=f"translate({cx} {cy}) rotate(90) scale(0.9 1.5)"))
    S.add(g(leon(0, 0, 0.9), filter=f"url(#{fid})", transform=f"translate({cx} {cy}) rotate(-90) scale(0.9 1.5)"))
    S.add(g(leon(0, 0, 0.9), filter=f"url(#{fid})", transform=f"translate({cx} {cy}) rotate(180) scale(0.9 0.35)"))
    S.add(croix(cx, cy, "#e8590c"))
    S.add(texte(700, 380, "9 h", 50, "#e8590c"), texte(100, 380, "17 h", 50, "#e8590c"), texte(400, 560, "12 h", 50, "#e8590c"))
    S.add(texte(400, 120, "Le tour de l'ombre de Léon", 40, ENCRE))
    S.add(texte(400, 170, "vu d'en haut", 32, "#495057", poids=600))
    S.cachette(430, 730, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("leon-seul.svg", vignette),
    ("01-le-geant.svg", p01), ("02-pareil.svg", p02), ("03-pourquoi.svg", p03),
    ("04-la-craie.svg", p04), ("05-midi.svg", p05), ("06-le-nuage.svg", p06),
    ("07-le-soir.svg", p07), ("08-le-jeu.svg", p08), ("09-le-coucher.svg", p09),
    ("10-le-lampadaire.svg", p10), ("11-vu-d-en-haut.svg", p11),
]
