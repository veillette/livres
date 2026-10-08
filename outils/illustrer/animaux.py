"""
Décors, petites bêtes et schémas partagés par les livres du rayon « Les
animaux » (documentaires : comment vivent les animaux).

Les grands animaux propres à un seul livre (girafe, baleine, kangourou…) sont
dessinés dans le script de leur livre ; ce module ne contient que ce qui sert
à plusieurs livres.
"""
import math
import random

from base import *
from base import _cachettes_sol
from base import _assombrir
from sciences import fleche_courbe


# ---------------------------------------------------------------------------
# Petits outils de dessin
# ---------------------------------------------------------------------------

def joue(x, y, s=1.0):
    """Petite joue rose, comme celle des personnages de base.py."""
    return ellipse(x, y, 8 * s, 5 * s, ROSE, opacity=0.7)


def etiquette(x, y, contenu, taille=30, couleur=ENCRE, fond="#ffffff", anchor="middle"):
    """Mot court posé sur un schéma, détouré de blanc pour rester lisible."""
    return texte(x, y, contenu, taille, couleur, anchor=anchor, contour=fond)


def cycle(cx, cy, r, couleur="#495057", nb=4, ecart=28, sw=7):
    """Flèches courbes disposées en cercle (sens des aiguilles d'une montre),
    entre `nb` étapes placées en haut, à droite, en bas, à gauche…"""
    m = []
    for k in range(nb):
        a0 = math.radians(-90 + k * 360 / nb + ecart)
        a1 = math.radians(-90 + (k + 1) * 360 / nb - ecart)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        d = f"M {n(x0)} {n(y0)} A {r} {r} 0 0 1 {n(x1)} {n(y1)}"
        direction = math.degrees(a1) + 90
        m.append(fleche_courbe(d, (x1, y1), direction, couleur, sw, 22))
    return g(m)


def disque(x, y, r, fond="#ffffff", bord="#dee2e6", ep=8):
    """Médaillon rond (zoom, étape d'un cycle)."""
    return cercle(x, y, r + ep, bord) + cercle(x, y, r, fond)


def loupe(x, y, r, contenu, fond="#ffffff", bord="#495057", manche=True, rot=40):
    """Loupe : un disque où l'on montre `contenu` (déjà placé en coordonnées
    de la page), avec un manche."""
    cid = uid("l")
    m = [el("clipPath", cercle(x, y, r, "#000"), id=cid)]
    if manche:
        a = math.radians(rot)
        m.append(trait(x + math.cos(a) * r, y + math.sin(a) * r,
                       x + math.cos(a) * (r + 90), y + math.sin(a) * (r + 90), "#7c4a1e", 22))
    m.append(cercle(x, y, r + 12, bord))
    m.append(cercle(x, y, r, fond))
    m.append(g(contenu, clip_path=f"url(#{cid})"))
    m.append(chemin(f"M {n(x - r * 0.62)} {n(y - r * 0.3)} A {n(r * 0.7)} {n(r * 0.7)} 0 0 1 {n(x - r * 0.25)} {n(y - r * 0.65)}",
                    stroke="#ffffff", sw=8, opacity=0.7))
    return g(m)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def herbes(S, y0, y1, nb=24, graine=1, couleur="#40c057", s=0.7):
    r = random.Random(graine)
    for _ in range(nb):
        S.add(herbe(r.uniform(10, 790), r.uniform(y0, y1), r.uniform(0.6, 1.0) * s, couleur))


def acacia(x, y, s=1.0, feuillage="#82c91e", feuillage2="#74b816", tronc="#7c4a1e"):
    """Acacia de la savane, au sommet plat ; (x, y) = pied du tronc."""
    branches = ("M -14 0 Q -8 -90 -4 -150 Q -40 -190 -90 -204 L -84 -214 Q -36 -200 0 -170 Q 20 -210 70 -226 L 76 -216 "
                "Q 34 -196 14 -150 Q 12 -80 16 0 Z")
    m = [ombre_sol(30, 0, 120, 12, 0.12) if OMBRE_SOL[0] else "",
         chemin(branches, lineaire([(0, eclaircir(tronc, 0.25)), (0.5, tronc), (1, _assombrir(tronc, 0.65))], 0, 0, 1, 0)),
         chemin("M -4 -20 q 3 -30 0 -60 M 6 -70 q -3 -24 2 -50", stroke=_assombrir(tronc, 0.6), sw=2.5, opacity=0.5)]
    nappes = [(-60, -228, 120, 34, feuillage2), (30, -246, 130, 36, feuillage), (-20, -262, 90, 26, feuillage)]
    for cx, cy, rx, ry, c in nappes:
        m.append(ellipse(cx, cy, rx, ry, volume(c, 0.3, 0.72)))
    # dessous de la couronne dans l'ombre, dessus éclairé, touffes de feuilles
    m.append(ombrage(g([ellipse(cx, cy, rx, ry, "#000") for cx, cy, rx, ry, _ in nappes]),
                     sombre=[(cx + 10, cy + ry * 0.8, rx * 0.95, ry * 0.45) for cx, cy, rx, ry, _ in nappes],
                     clair=[(-40, -280, 40, 7, -4)], opacite=0.14))
    m.append(chemin(" ".join(f"M {cx + dx} {cy - 4} q 4 -8 9 -4 q 5 -7 10 0" for cx, cy, rx, ry, _ in nappes for dx in (-rx * 0.6, -rx * 0.1, rx * 0.4)),
                    stroke=_assombrir(feuillage, 0.7), sw=2.5, opacity=0.45))
    return place(m, x, y, s)


def savane(S, y=560, haut="#74c0fc", bas="#fff3bf", sol_c="#f4d58d", graine=2, arbres=True):
    """Savane africaine : ciel chaud, herbe sèche, acacias au loin."""
    S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))
    # trois plans : collines lointaines fondues dans la brume, plaine, sol
    S.add(chemin(f"M 0 {y - 70} Q 120 {y - 150} 260 {y - 96} Q 420 {y - 40} 560 {y - 120} Q 680 {y - 170} 800 {y - 90} L 800 {y} L 0 {y} Z",
                 melange("#e9d8a6", bas, 0.5), opacity=0.7))
    S.add(chemin(f"M 0 {y - 40} Q 180 {y - 90} 360 {y - 50} T 800 {y - 60} L 800 {y + 10} L 0 {y + 10} Z", terrain("#e9d8a6")))
    if arbres:
        S.add(acacia(130, y - 20, 0.45), acacia(660, y - 30, 0.55))
    S.add(chemin(f"M 0 {y} Q 200 {y - 18} 400 {y} T 800 {y - 6} L 800 800 L 0 800 Z", terrain(sol_c)))
    S.add(chemin(f"M 0 {y} Q 200 {y - 18} 400 {y} T 800 {y - 6}", stroke=eclaircir(sol_c, 0.45), sw=4, opacity=0.6))
    r = random.Random(graine)
    for _ in range(28):
        x, yy = r.uniform(10, 790), r.uniform(y + 20, 790)
        # herbes sèches plus grandes et plus contrastées au premier plan
        k = 0.6 + 0.9 * (yy - y) / max(800 - y, 1)
        S.add(chemin(f"M {n(x - 8 * k)} {n(yy)} L {n(x - 12 * k)} {n(yy - 20 * k)} M {n(x)} {n(yy)} L {n(x)} {n(yy - 26 * k)} M {n(x + 8 * k)} {n(yy)} L {n(x + 13 * k)} {n(yy - 19 * k)}",
                     stroke=melange("#e9c46a", "#b07d2b", min(k - 0.5, 1)), sw=3.5 * k ** 0.5))


def banquise(S, y=520, haut="#a5d8ff", bas="#e7f5ff", mer=True, nuit_=False, graine=1):
    """Banquise : ciel froid, mer sombre au loin, glace au premier plan."""
    if nuit_:
        nuit(S, "#16213e", "#3b4a7a")
        etoiles(S, 40, graine, (0, 0, 800, y - 60))
    else:
        S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))
    glace_loin = "#d0ebff" if not nuit_ else "#748ffc"
    S.add(pic(-20, y - 40, 90, y - 130, 200, y - 40, glace_loin, False),
          pic(520, y - 40, 650, y - 150, 820, y - 40, glace_loin, False))
    if mer:
        mer_c = "#1c7ed6" if not nuit_ else "#1b2a5c"
        S.add(rect(0, y - 44, 800, 60, lineaire([eclaircir(mer_c, 0.3), mer_c, _assombrir(mer_c, 0.8)])))
    blanc = "#f8f9fa" if not nuit_ else "#bac8ff"
    ombre_ = "#d0ebff" if not nuit_ else "#91a7ff"
    S.add(chemin(f"M 0 {y} Q 200 {y - 14} 400 {y} T 800 {y - 4} L 800 800 L 0 800 Z", lineaire([(0, blanc), (0.5, blanc), (1, ombre_)])))
    S.add(chemin(f"M 0 {y} Q 200 {y - 14} 400 {y} T 800 {y - 4}", stroke="#ffffff", sw=5, opacity=0.8))
    r = random.Random(graine)
    for _ in range(6):
        x, yy = r.uniform(40, 760), r.uniform(y + 60, 780)
        S.add(chemin(f"M {n(x - 60)} {n(yy)} Q {n(x)} {n(yy - 10)} {n(x + 60)} {n(yy)}", stroke=ombre_, sw=5))


def roseau(x, y, s=1.0, h=220, couleur="#5c940d", epi="#7c4a1e", rot=0):
    """Massette (roseau à épi brun) au bord de la mare ; (x, y) = pied."""
    m = [chemin(f"M 0 0 Q 6 {-h / 2} 0 {-h}", stroke=couleur, sw=6),
         ellipse(1, -h + 34, 9, 30, epi),
         chemin(f"M 0 -20 Q -30 {-h * 0.45} -44 {-h * 0.7}", stroke="#74b816", sw=7)]
    return place(m, x, y, s, rot=rot)


def mare(S, y=500, graine=1, nenuphars=True):
    """Mare vue de la berge : ciel, herbe, eau, roseaux et nénuphars."""
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(chemin(f"M 0 {y - 100} Q 150 {y - 160} 330 {y - 110} Q 520 {y - 60} 800 {y - 130} L 800 {y} L 0 {y} Z", "#a5d8c0", opacity=0.45))
    S.add(chemin(f"M 0 {y - 60} Q 200 {y - 120} 400 {y - 70} T 800 {y - 80} L 800 {y + 20} L 0 {y + 20} Z", terrain("#b2f2bb")))
    S.add(rect(0, y - 10, 800, 810 - y, terrain("#69db7c")))
    S.add(ellipse(400, y + 190, 470, 190, "#2f9e44", opacity=0.35))
    S.add(ellipse(400, y + 190, 470, 184, radial([(0, "#74c0fc"), (0.7, "#4dabf7"), (1, "#339af0")], cy=0.4)))
    S.add(ellipse(400, y + 190, 440, 165, "#74c0fc", opacity=0.35))
    for k in range(5):
        S.add(chemin(f"M {150 + k * 120} {y + 90 + (k % 2) * 80} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    for k, (x, h) in enumerate([(-6, 230), (22, 270), (48, 200), (770, 240), (800, 200), (740, 180)]):
        S.add(roseau(x, y + 60, 1, h, rot=(-6 if x < 400 else 6)))
    if nenuphars:
        S.add(place(_nenuphar_simple("#ffc9d6"), 210, y + 250, 0.9), place(_nenuphar_simple(None), 600, y + 140, 0.75))


def _nenuphar_simple(fleur_c):
    m = [chemin("M 0 0 L 79 -5 A 80 26 0 1 0 79 5 Z", "#40c057"),
         chemin("M 0 0 L 79 -5 M 0 0 L -60 -14 M 0 0 L -50 16", stroke="#2f9e44", sw=3)]
    if fleur_c:
        for k in range(6):
            a = math.radians(-90 + k * 60)
            m.append(ellipse(-20 + math.cos(a) * 12, -14 + math.sin(a) * 8, 12, 7, fleur_c, rot=k * 60))
        m.append(cercle(-20, -14, 6, "#ffd43b"))
    return m


def nenuphar_haut(x, y, s=1.0, fleur_c=None):
    """Feuille de nénuphar vue de dessus (grande et ronde, avec son encoche)."""
    return place(_nenuphar_simple(fleur_c), x, y, s)


def sous_l_eau(S, haut="#a9e34b", bas="#2b8a3e", fond_c="#8d6e4a", y_fond=690, graine=3, plantes=True):
    """Vue sous l'eau d'une mare : eau verte, vase au fond, plantes."""
    S._decor("eau")
    _cachettes_sol(S, y_fond, 12)
    S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))
    S.add(rect(0, 0, 800, 36, "#d3f9d8", opacity=0.5))
    S.add(chemin(f"M 0 {y_fond} Q 200 {y_fond - 24} 400 {y_fond} T 800 {y_fond - 10} L 800 800 L 0 800 Z", fond_c))
    r = random.Random(graine)
    for _ in range(14):
        S.add(cercle(r.uniform(10, 790), r.uniform(y_fond + 20, 790), r.uniform(4, 9), _assombrir(fond_c, 0.85)))
    if plantes:
        for x in (60, 150, 690, 760):
            S.add(_herbe_eau(x, y_fond + 10, r.uniform(0.9, 1.3), r.randint(1, 9)))


def _herbe_eau(x, y, s=1.0, graine=1):
    r = random.Random(graine)
    m = []
    for k in range(4):
        dx = (k - 1.5) * 14
        hh = 260 * r.uniform(0.6, 1.0)
        m.append(chemin(f"M {n(dx)} 0 Q {n(dx - 26)} {n(-hh * 0.3)} {n(dx)} {n(-hh * 0.6)} Q {n(dx + 24)} {n(-hh * 0.8)} {n(dx + 4)} {n(-hh)}",
                        stroke="#2f9e44" if k % 2 else "#37b24d", sw=9))
    return place(m, x, y, s)


def coupe_terre(S, y=300, ciel_=True, graine=4, herbe_c="#69db7c", terre="#a0693a", terre2="#6d4424"):
    """Coupe du sol : un peu de ciel et d'herbe en haut, la terre en dessous,
    avec des cailloux et des racines."""
    if ciel_:
        ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(rect(0, y, 800, 800 - y, S.degrade([terre, terre2])))
    S.add(chemin(f"M 0 {y + 6} Q 200 {y - 8} 400 {y + 6} T 800 {y} L 800 {y + 26} L 0 {y + 26} Z", "#4a2e16", opacity=0.25))
    S.add(chemin(f"M 0 {y - 10} Q 200 {y - 26} 400 {y - 10} T 800 {y - 16} L 800 {y + 12} L 0 {y + 12} Z", herbe_c))
    # la petite bête se pose sur l'herbe, jamais dans la terre
    _cachettes_sol(S, y - 4, dy=0)
    r = random.Random(graine)
    for _ in range(14):
        S.add(ellipse(r.uniform(10, 790), r.uniform(y + 60, 790), r.uniform(8, 22), r.uniform(6, 14),
                      r.choice(["#ced4da", "#adb5bd", "#c9a27a"]), rot=r.uniform(-30, 30)))
    for _ in range(18):
        S.add(cercle(r.uniform(0, 800), r.uniform(y + 30, 800), r.uniform(2, 4), "#4a2e16", opacity=0.4))


def racines(x, y, s=1.0, couleur="#e9d8a6", graine=1):
    """Racines fines qui descendent dans la terre depuis (x, y)."""
    r = random.Random(graine)
    m = []
    for k in range(5):
        dx = (k - 2) * 26
        L = r.uniform(120, 200)
        m.append(chemin(f"M 0 0 Q {n(dx * 0.5)} {n(L * 0.4)} {n(dx)} {n(L * 0.6)} T {n(dx * 1.3)} {n(L)}", stroke=couleur, sw=5 - k % 2))
    return place(m, x, y, s)


def montagnes_fond(S, y=420, couleurs=("#b197fc", "#9775fa"), neige=True):
    """Chaîne de montagnes au loin, sommets enneigés."""
    pics = [(-60, y + 40, 150, y - 230, 360, y + 40), (220, y + 40, 470, y - 300, 720, y + 40),
            (560, y + 40, 760, y - 200, 940, y + 40)]
    for k, (x0, y0, xs, ys, x1, y1) in enumerate(pics):
        S.add(pic(x0, y0, xs, ys, x1, y1, couleurs[k % 2], neige))


def plage(S, y=470, haut="#74c0fc", bas="#e7f5ff", nuit_=False, sable_c="#f4d58d", lune_=None):
    """Plage : mer au fond, sable au premier plan."""
    if nuit_:
        nuit(S, "#1c2a52", "#4c5b9a")
        etoiles(S, 40, 5, (0, 0, 800, y - 40))
    else:
        S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))
    mer = "#1864ab" if nuit_ else "#339af0"
    # la mer pâlit vers l'horizon (perspective atmosphérique)
    S.add(rect(0, y - 110, 800, 130, lineaire([eclaircir(mer, 0.35), mer, _assombrir(mer, 0.85)])))
    if lune_:
        lx = lune_
        S.add(lune(lx, y - 300, 42))
        for k in range(6):
            S.add(rect(lx - 50 + (k % 2) * 16, y - 100 + k * 18, 100 - k * 8, 6, "#fff3bf", rx=3, opacity=0.8 - k * 0.1))
    S.add(chemin(f"M 0 {y} Q 200 {y - 34} 400 {y - 10} T 800 {y - 20} L 800 800 L 0 800 Z", "#ffffff", opacity=0.75 if not nuit_ else 0.35))
    S.add(chemin(f"M 0 {y + 14} Q 200 {y - 20} 400 {y + 4} T 800 {y - 6} L 800 800 L 0 800 Z",
                 terrain(sable_c if not nuit_ else "#a39470")))
    r = random.Random(6)
    for _ in range(26):
        S.add(cercle(r.uniform(0, 800), r.uniform(y + 40, 790), r.uniform(2, 4), "#e0b85a" if not nuit_ else "#857a5c"))

# ---------------------------------------------------------------------------
# Petites bêtes
# ---------------------------------------------------------------------------

def mouche(x, y, s=1.0, rot=0, couleur="#495057"):
    """Mouche vue de dessus, tête vers le haut ; (x, y) = centre."""
    m = [ellipse(-14, -4, 14, 22, "#e7f5ff", rot=-30, opacity=0.85, stroke="#a5d8ff", stroke_width=2),
         ellipse(14, -4, 14, 22, "#e7f5ff", rot=30, opacity=0.85, stroke="#a5d8ff", stroke_width=2),
         ellipse(0, 6, 9, 15, couleur), cercle(0, -12, 8, couleur),
         cercle(-5, -15, 4, "#c92a2a"), cercle(5, -15, 4, "#c92a2a")]
    return place(m, x, y, s, rot=rot)


def moustique(x, y, s=1.0, rot=0):
    """Moustique de profil, tête à droite ; (x, y) = centre."""
    m = []
    for k in range(3):
        m.append(chemin(f"M {-6 + k * 8} 4 Q {-12 + k * 10} 20 {-20 + k * 12} 34", stroke="#495057", sw=2))
    m += [ellipse(-6, -14, 8, 20, "#e7f5ff", rot=-60, opacity=0.85, stroke="#a5d8ff", stroke_width=1.5),
          ellipse(-16, 2, 20, 5, "#868e96", rot=-8), ellipse(6, 0, 8, 6, "#495057"), cercle(16, -2, 5, "#495057"),
          trait(20, 0, 34, 6, "#495057", 2)]
    return place(m, x, y, s, rot=rot)


def papillon_nuit(x, y, s=1.0, rot=0, couleur="#d9b48f"):
    """Papillon de nuit, ailes beiges ; (x, y) = centre."""
    fonce = _assombrir(couleur, 0.8)
    m = [chemin("M 0 -4 Q -40 -34 -46 -6 Q -40 18 0 6 Z", couleur), chemin("M 0 -4 Q 40 -34 46 -6 Q 40 18 0 6 Z", couleur),
         cercle(-26, -6, 5, fonce), cercle(26, -6, 5, fonce),
         ellipse(0, 0, 5, 16, fonce), chemin("M -2 -14 Q -10 -26 -16 -26 M 2 -14 Q 10 -26 16 -26", stroke=fonce, sw=2)]
    return place(m, x, y, s, rot=rot)


def abeille(x, y, s=1.0, rot=0, flip=False, expr="sourire", regard=(1, 0), pelotes=False, ailes=True, dard=True,
            abdomen=1.0, trompe=False, marque=None):
    """Abeille de profil, tête à droite ; (x, y) = centre du corps.
    Trois parties (tête, thorax, abdomen rayé), six pattes, deux paires d'ailes.
    abdomen : allongement de l'abdomen (1.5 pour une reine) ; marque : couleur
    de la pastille que l'apiculteur peint sur le dos de la reine."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if trompe:
        m.append(chemin("M 38 6 Q 50 20 50 34", stroke="#8d5524", sw=3))
    for k in range(3):
        px = -2 + k * 10
        m.append(chemin(f"M {px} 10 Q {px - 6} 22 {px - 4} 30", stroke=ENCRE, sw=3))
    if pelotes:
        m.append(ellipse(-6, 28, 8, 6, "#ff922b"))
    A = abdomen
    ventre = []
    if dard:
        ventre.append(poly([(-52, 2), (-66, 6), (-52, 10)], ENCRE))
    ventre.append(ellipse(-26, 4, 30, 22, "#fcc419"))
    cid = uid("ab")
    ventre.append(el("clipPath", ellipse(-26, 4, 30, 22, "#000"), id=cid))
    ventre.append(g([rect(-44, -20, 7, 50, ENCRE), rect(-30, -20, 7, 50, ENCRE), rect(-16, -20, 7, 50, ENCRE)],
                    clip_path=f"url(#{cid})"))
    m.append(g(ventre) if A == 1 else g(ventre, f"translate(-4 0) scale({n(A, 3)} 1)"))
    m.append(ellipse(8, 0, 16, 15, "#8d5524"))
    if marque:
        m.append(cercle(8, -10, 6, marque))
    m.append(cercle(30, -4, 15, "#fcc419"))
    m.append(chemin("M 34 -18 Q 38 -32 48 -34", stroke=ENCRE, sw=2.5))
    m.append(chemin("M 28 -18 Q 26 -34 34 -40", stroke=ENCRE, sw=2.5))
    m.append(oeil(34, -7, ys, regard, taille=0.55))
    m.append(ellipse(38, 3, 4, 2.5, ROSE, opacity=0.8))
    if ailes:
        m.append(ellipse(-4, -26, 13, 24, "#e7f5ff", rot=-30, opacity=0.85, stroke="#a5d8ff", stroke_width=1.5))
        m.append(ellipse(10, -26, 10, 20, "#e7f5ff", rot=20, opacity=0.85, stroke="#a5d8ff", stroke_width=1.5))
    return place(m, x, y, s, flip=flip, rot=rot)


def poisson_simple(x, y, s=1.0, couleur="#adb5bd", flip=False, rot=0):
    """Petit poisson argenté sans visage, tête à droite ; (x, y) = centre."""
    m = [poly([(-34, 0), (-54, -16), (-54, 16)], _assombrir(couleur, 0.85)),
         ellipse(0, 0, 38, 15, couleur), ellipse(4, 5, 28, 6, "#ffffff", opacity=0.45),
         cercle(24, -3, 3.5, ENCRE)]
    return place(m, x, y, s, flip=flip, rot=rot)


def souris_champs(x, y, s=1.0, flip=False, couleur="#a9805b"):
    """Petite souris (ou campagnol) à quatre pattes, de profil, tête à droite ;
    (x, y) = sous les pattes."""
    m = [chemin("M -30 -12 Q -60 -10 -70 -30", stroke="#e8a798", sw=3),
         ellipse(-14, -4, 6, 4, "#e8a798"), ellipse(14, -4, 6, 4, "#e8a798"),
         ellipse(-4, -18, 32, 18, couleur), cercle(26, -24, 14, couleur),
         cercle(20, -38, 9, couleur), cercle(20, -38, 5, "#ffc9c9"),
         cercle(40, -22, 3, ENCRE), cercle(31, -27, 2.8, ENCRE)]
    return place(m, x, y, s, flip=flip)


def ver(x, y, s=1.0, longueur=200, couleur="#f783ac", ondule=1.0, rot=0, visage=True, expr="sourire", flip=False,
        regard=(1, 0), ep=26):
    """Ver de terre de profil, tête à droite ; (x, y) = milieu du ver.
    Pas d'yeux en vrai : le visage est seulement un sourire et des joues."""
    ys, bs, ss = EXPRESSIONS[expr]
    L = longueur
    pts = []
    for k in range(25):
        t = k / 24
        pts.append((-L / 2 + t * L, -math.sin(t * math.pi * 2) * 14 * ondule))
    d = "M " + " L ".join(f"{n(px)} {n(py)}" for px, py in pts)
    fonce = _assombrir(couleur, 0.85)
    e = ep / 26
    m = [chemin(d, stroke=couleur, sw=ep),
         ]
    for k in range(3, 22, 2):
        px, py = pts[k]
        m.append(trait(px, py - 11 * e, px, py + 11 * e, fonce, 2))
    # clitellum (anneau plus clair)
    px, py = pts[17]
    m.append(ellipse(px, py, 16 * e, 14 * e, eclaircir(couleur, 0.3)))
    hx, hy = pts[-1]
    m.append(cercle(hx, hy, 13 * e, couleur))
    if visage:
        m.append(ellipse(hx + 2, hy + 4, 5, 3, "#c2255c", opacity=0.6))
        m.append(place(bouche(0, 0, bs, 0.45), hx + 6, hy - 2))
    return place(m, x, y, s, rot=rot, flip=flip)
