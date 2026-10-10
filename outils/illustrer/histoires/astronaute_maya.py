"""Maya, astronaute — un métier dans l'espace, raconté par sa fille Nina.

Maya s'entraîne dans une piscine géante, décolle, rejoint la Station
spatiale, à 400 km au-dessus de la Terre, qu'elle contourne en une heure et
demie (seize levers de soleil par jour). Là-haut, on ne sent plus son
poids : tout flotte, l'eau fait des boules, on mange des tortillas (pas de
miettes), on dort attaché au mur, on court sur un tapis avec des
élastiques. Sortie dans l'espace, attachée par un câble. Le soir, Nina voit
passer la station comme une étoile qui file sans clignoter. Retour en
capsule sous parachutes, dans la mer ; les jambes ont désappris la marche.

Plans : 1 moyen (la maquette) · 2 large (la piscine) · 3 large (le
décollage) · 4 gros plan (le hublot) · 5 large (la station au-dessus de la
Terre) · 6 moyen (tout flotte) · 7 gros plan (la tortilla) · 8 moyen (le
tapis de course) · 9 moyen (dormir au mur) · 10 large (la sortie) ·
11 large (Nina voit passer la station) · 12 large (les parachutes) ·
13 moyen (le câlin).

Les pages dans l'espace sont hors du jeu de la coccinelle (S.cachette(None)).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre, STATURES
from sciences import fusee

ID = "astronaute-maya"

MAYA = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="afro", nez="rond", yeux="cils")
NINA = dict(peau="brune", cheveux="noir", coiffure="couettes", habit="#ffd43b", robe=False, jambes="#1c7ed6", nez="rond")
PAPA = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="courts", habit="#2f9e44", robe=False, jambes="#364fc7", barbe="#e8590c")
POLO = "#1c7ed6"
TETE_ADULTE = (0, -180)       # centre de la tête d'un adulte (repère local)


def maya(x, y, s=1.3, **k):
    """Maya en polo bleu (dans la station ou à la maison)."""
    k.setdefault("habit", POLO)
    k.setdefault("robe", False)
    k.setdefault("jambes", "#495057")
    return personne(x, y, s, **{**MAYA, **k})


def combinaison(x, y, s=1.3, casque=True, rot=0, flip=False, **k):
    """Maya en combinaison spatiale blanche, sac dorsal et casque à visière."""
    sac = rect(-64, -176, 128, 122, "#ced4da", rx=16)
    corps = personne(0, 0, 1.0, habit="#f8f9fa", jambes="#e9ecef", robe=False, chaussures="#868e96", derriere=sac,
                     ceinture="#adb5bd", **{**MAYA, **k})
    m = [corps, rect(-24, -128, 48, 30, "#4dabf7", rx=5), cercle(-10, -113, 5, "#fa5252"), cercle(10, -113, 5, "#51cf66"),
         rect(-38, -150, 22, 10, "#fa5252", rx=3)]
    if casque:
        cx, cy = TETE_ADULTE
        m += [cercle(cx, cy, 66, "#d0ebff", opacity=0.28), cercle(cx, cy, 66, "none", stroke="#adb5bd", stroke_width=7),
              chemin(f"M {cx - 40} {cy - 42} Q {cx - 8} {cy - 62} {cx + 24} {cy - 54}", stroke="#fff", sw=8, opacity=0.7),
              rect(-50, -122 + 6, 100, 12, "#adb5bd", rx=6, transform="translate(0 -14)")]
    return place(m, x, y, s, rot=rot, flip=flip) + (occuper(x - 80 * s, y - 250 * s, x + 80 * s, y) if not rot else "")


def espace(S, graine=1, nb=60):
    fond(S, "#0b1433")
    S.ambiance("nuit")
    r = random.Random(graine)
    for _ in range(nb):
        S.add(cercle(r.uniform(0, 800), r.uniform(0, 800), r.uniform(1, 2.6), "#fff", opacity=r.uniform(0.5, 1)))
    S.cachette(None)          # dans l'espace : pas de coccinelle


def terre_arc(S, cy=1750, R=1250, nuit_=False):
    """La Terre vue de la station : un grand arc, la mer, les nuages, le liseré bleu de l'atmosphère."""
    cid = uid("t")
    terre = cercle(400, cy, R, "#000")
    S.add(cercle(400, cy, R + 26, "#74c0fc", opacity=0.35), cercle(400, cy, R + 12, "#a5d8ff", opacity=0.5))
    r = random.Random(5)
    contenu = [cercle(400, cy, R, "#1864ab" if not nuit_ else "#0b2545")]
    for k in range(5):
        contenu.append(ellipse(r.uniform(0, 800), cy - R + r.uniform(60, 300), r.uniform(80, 180), r.uniform(30, 70),
                               "#5c940d" if not nuit_ else "#1b2a4a", rot=r.uniform(-20, 20)))
    for k in range(14):
        contenu.append(ellipse(r.uniform(-50, 850), cy - R + r.uniform(20, 340), r.uniform(30, 90), r.uniform(10, 22), "#fff", opacity=0.85 if not nuit_ else 0.15))
    if nuit_:
        for k in range(40):
            contenu.append(cercle(r.uniform(0, 800), cy - R + r.uniform(30, 300), r.uniform(1.5, 3.5), "#ffd43b", opacity=0.9))
    S.add(el("clipPath", terre, id=cid), g(contenu, clip_path=f"url(#{cid})"))


def station(x, y, s=1.0):
    """La Station spatiale, schématique : poutre, panneaux solaires, modules ; (x, y) = centre."""
    m = [rect(-330, -8, 660, 16, "#adb5bd")]
    for dx in (-290, -200, 200, 290):
        for sy in (-1, 1):
            m.append(rect(dx - 34, sy * 20 if sy > 0 else -150, 68, 130, "#1c3d6e", stroke="#fcc419", stroke_width=3))
            for k in range(1, 5):
                m.append(trait(dx - 34, (sy * 20 if sy > 0 else -150) + k * 26, dx + 34, (sy * 20 if sy > 0 else -150) + k * 26, "#4c6ef5", 1.5))
    m += [rect(-130, -26, 260, 52, cylindre("#f1f3f5", 0.3, 0.8, vertical=True), rx=24),
          rect(-24, -140, 48, 280, cylindre("#f1f3f5", 0.3, 0.8), rx=22),
          rect(-90, 40, 60, 80, "#f8f9fa", stroke="#dee2e6", stroke_width=2), rect(30, -120, 60, 80, "#f8f9fa", stroke="#dee2e6", stroke_width=2)]
    return place(m, x, y, s)


def dedans_station(S, graine=1):
    """Un module de la station : panneaux, poignées jaunes, câbles, ordinateur."""
    fond(S, "#e9ecef")
    S.add(rect(0, 0, 800, 800, lineaire([(0, "#ced4da"), (0.5, "#f1f3f5"), (1, "#ced4da")])))
    r = random.Random(graine)
    for k in range(4):
        for j in range(4):
            S.add(rect(20 + k * 195, 30 + j * 190, 180, 170, "#f8f9fa", rx=8, stroke="#dee2e6", stroke_width=3))
            if r.random() < 0.5:
                S.add(rect(50 + k * 195, 60 + j * 190, 60, 30, r.choice(("#4dabf7", "#fab005", "#69db7c")), rx=4))
    for x0 in (140, 560):
        S.add(rect(x0, 80, 18, 120, "#fcc419", rx=8), rect(x0 + 60, 580, 120, 18, "#fcc419", rx=8))
    S.add(chemin("M 0 420 Q 200 380 360 440 T 800 400", stroke="#495057", sw=6), chemin("M 0 450 Q 240 420 400 470 T 800 440", stroke="#fa5252", sw=4))
    S.add(rect(600, 200, 130, 86, "#343a40", rx=6), rect(608, 208, 114, 70, "#74c0fc", rx=3), rect(620, 286, 90, 10, "#495057", rx=3))
    S.ambiance("interieur")
    S.cachette(None)


def maison_dedans(S, nuit_=False):
    piece(S, "chambre", 600)
    if nuit_:
        S.ambiance("nuit")


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    espace(S, 2)
    terre_arc(S, 1700, 1250)
    S.add(station(560, 200, 0.5))
    S.add(trait(470, 230, 380, 380, "#dee2e6", 3))
    S.add(combinaison(380, 640, 1.25, expr="rire", bras="coucou", rot=-12))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fusee(200, 120, 0.55, rot=30, flamme=True))
    S.add(etoile5(70, 60, 10, "#fcc419"), etoile5(340, 200, 8, "#fcc419"), etoile5(330, 50, 6, "#fcc419"))
    return S


def p01():
    """Plan moyen : à la maison, Maya montre à Nina une maquette de fusée."""
    S = Scene()
    maison_dedans(S)
    S.add(fenetre(470, 90, 200, 160, "#a5d8ff", rideaux="#ffd43b",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), lune(620, 150, 16, halo=False)])))
    S.add(cadre_mur(120, 120, 120, 90, "#1c2a52"))
    S.add(maya(300, 790, 1.35, bras="tient", expr="content", regard=(1, 0.3),
               objet=fusee(*ancre(70, -150, "tient", "adulte"), 0.32, flamme=False)))
    S.add(personne(560, 790, 1.25, expr="bouche_bee", bras="joues", regard=(-1, -0.5), **NINA))
    return S


def p02():
    """Plan large : l'entraînement dans une piscine géante, en combinaison."""
    S = Scene()
    fond(S, "#1c7ed6")
    S.add(rect(0, 0, 800, 800, lineaire([(0, "#74c0fc"), (1, "#1864ab")])))
    for k in range(0, 800, 80):
        S.add(trait(k, 0, k - 60, 800, "#a5d8ff", 2, opacity=0.4))
        S.add(trait(0, k, 800, k + 30, "#a5d8ff", 2, opacity=0.25))
    S.add(rect(80, 560, 640, 30, "#adb5bd"), rect(120, 420, 80, 140, "#ced4da"), rect(600, 380, 80, 180, "#ced4da"))
    S.add(combinaison(400, 520, 1.25, expr="concentre", bras="tend", rot=-70))
    for x, y, rr in ((300, 200, 10), (330, 150, 7), (360, 110, 5), (520, 260, 9), (540, 210, 6)):
        S.add(cercle(x, y, rr, "none", stroke="#e7f5ff", stroke_width=3))
    plongeur = personne(0, 0, 1.0, stature="adulte", peau="claire", cheveux="blond", coiffure="courts", habit="#212529", robe=False,
                        jambes="#212529", acc=("lunettes",), bras="ouverts", expr="neutre",
                        derriere=rect(-30, -170, 60, 110, "#fab005", rx=20))
    S.add(place(plongeur, 650, 700, 0.8, rot=-30))
    S.add(texte(400, 90, "Une piscine géante !", 48, "#fff", contour="#1864ab"))
    S.cachette(None)          # dans une piscine, pas de petite bête
    return S


def p03():
    """Plan large : 3, 2, 1… décollage ! Nina et Papa regardent de loin."""
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    S.add(rect(0, 640, 800, 160, "#adb5bd"))
    S.add(rect(500, 160, 40, 480, "none", stroke="#e03131", stroke_width=6))
    for k in range(10):
        S.add(trait(500, 160 + k * 48, 540, 208 + k * 48, "#e03131", 4))
    S.add(fusee(400, 300, 1.0, flamme=True))
    for k, (x, y, s) in enumerate(((330, 600, 1.3), (470, 610, 1.2), (250, 640, 1.0), (560, 650, 1.0), (400, 640, 1.4))):
        S.add(nuage(x, y, s, "#dee2e6"))
    S.add(personne(110, 790, 0.9, expr="bouche_bee", bras="joues", regard=(1, -1), **NINA))
    S.add(personne(200, 790, 0.85, expr="joie", bras="haut", regard=(1, -1), **PAPA))
    S.add(texte(620, 120, "3, 2, 1…", 52, "#e03131", contour="#fff"), texte(620, 180, "décollage !", 52, "#e03131", contour="#fff"))
    S.cachette(740, 700)
    return S


def p04():
    """Gros plan : par le hublot de la capsule, Maya voit la Terre toute ronde et bleue."""
    S = Scene()
    espace(S, 3, 40)
    S.add(rect(0, 0, 800, 800, "#495057"))
    S.add(cercle(420, 360, 250, "#212529"))
    cid = uid("h")
    vue = g([rect(0, 0, 800, 800, "#0b1433")] + [cercle(150 + k * 61 % 500, 160 + k * 37 % 200, 2, "#fff") for k in range(14)])
    S.add(el("clipPath", cercle(420, 360, 230, "#000"), id=cid), g([vue], clip_path=f"url(#{cid})"))
    S2 = Scene()
    terre_arc(S2, 1150, 700)
    S.add(g(S2.els, clip_path=f"url(#{cid})"))
    S.add(cercle(420, 360, 230, "none", stroke="#868e96", stroke_width=16))
    S.add(chemin("M 260 230 Q 320 170 400 160", stroke="#fff", sw=10, opacity=0.35))
    S.add(combinaison(150, 900, 1.6, casque=False, expr="bouche_bee", bras="pense", regard=(1, -0.5)))
    S.cachette(None)
    return S


def p05():
    """Plan large : la Station spatiale, au-dessus de la Terre."""
    S = Scene()
    espace(S, 4)
    terre_arc(S, 1800, 1300)
    S.add(station(400, 300, 0.95))
    S.add(soleil(80, 90, 34, "#fff3bf", rayons=False))
    S.add(texte(400, 590, "400 km au-dessus de la Terre", 34, "#fff", contour="#1864ab"))
    return S


def p06():
    """Plan moyen : dans la station, tout flotte : Maya, la tête en bas, et une boule d'eau."""
    S = Scene()
    dedans_station(S, 2)
    S.add(maya(330, 220, 1.3, expr="rire", bras="ouverts", rot=160, regard=(0.5, 0)))
    S.add(cercle(560, 470, 46, "#a5d8ff", opacity=0.8, stroke="#74c0fc", stroke_width=3))
    S.add(ellipse(546, 452, 14, 9, "#fff", opacity=0.8), cercle(620, 400, 12, "#a5d8ff", opacity=0.8), cercle(640, 540, 8, "#a5d8ff", opacity=0.8))
    S.add(place(rect(-50, -6, 100, 12, "#fab005", rx=3), 200, 620, rot=30), place(rect(-30, -40, 60, 80, "#fff", stroke="#adb5bd", stroke_width=2), 640, 640, rot=-20))
    S.add(texte(400, 760, "Tout flotte !", 52, "#1c7ed6", contour="#fff"))
    return S


def tortilla(x, y, s=1.0, rot=0):
    return place([ellipse(0, 0, 70, 66, volume("#f6d38b", 0.35, 0.8)), cercle(-20, -10, 6, "#e8a33d", opacity=0.7),
                  cercle(24, 16, 5, "#e8a33d", opacity=0.7), cercle(10, -30, 4, "#e8a33d", opacity=0.7)], x, y, s, rot=rot)


def sachet(x, y, s=1.0, rot=0, c="#fa5252"):
    return place([rect(-36, -50, 72, 100, "#e9ecef", rx=8, stroke="#adb5bd", stroke_width=3), rect(-26, -20, 52, 40, c, rx=4),
                  rect(-8, -62, 16, 14, "#868e96", rx=3)], x, y, s, rot=rot)


def p07():
    """Gros plan : Maya mange une tortilla ; un sachet et une cuillère flottent."""
    S = Scene()
    dedans_station(S, 3)
    S.add(maya(380, 860, 2.0, expr="miam", bras="donne", regard=(0.6, 0.2), objet=tortilla(*ancre(96, -96, "donne", "adulte"), 0.55, rot=20)))
    S.add(sachet(630, 360, 1.3, rot=25), place(rect(-60, -6, 120, 12, "#adb5bd", rx=6), 160, 330, rot=-40))
    for k in range(5):
        S.add(cercle(560 + k * 30, 520 - k * 20, 10 - k, "#e8590c", opacity=0.9))
    S.add(texte(400, 110, "Pas de pain : les miettes s'envoleraient !", 30, "#1c7ed6", contour="#fff"))
    return S


def p08():
    """Plan moyen : Maya court sur un tapis, retenue par des élastiques."""
    S = Scene()
    dedans_station(S, 4)
    S.add(rect(170, 690, 460, 40, "#343a40", rx=16), rect(170, 680, 460, 14, "#495057", rx=6))
    S.add(maya(400, 690, 1.45, expr="concentre", bras="court", pas="court", regard=(1, 0)))
    S.add(chemin("M 290 710 Q 330 560 360 470", stroke="#fab005", sw=8), chemin("M 510 710 Q 470 560 440 470", stroke="#fab005", sw=8))
    S.add(texte(400, 110, "Des élastiques pour rester sur le tapis !", 30, "#1c7ed6", contour="#fff"))
    return S


def p09():
    """Plan moyen : Maya dort dans un sac de couchage attaché au mur."""
    S = Scene()
    dedans_station(S, 5)
    S.ambiance("nuit")
    S.add(rect(290, 140, 220, 560, "#5c7cfa", rx=90))
    S.add(maya(400, 690, 1.45, expr="dort", bras="bas", ombre=False))
    S.add(rect(290, 505, 220, 195, lineaire([(0, "#748ffc"), (1, "#4263eb")]), rx=60))
    for yy in (180, 640):
        S.add(rect(270, yy, 260, 14, "#fcc419", rx=6))
    S.add(zzz(560, 230, 1.0, "#5c7cfa"))
    S.add(cercle(650, 500, 40, "#adb5bd"), cercle(650, 500, 32, "#0b1433"), cercle(640, 492, 6, "#fff3bf"))
    return S


def p10():
    """Plan large : sortie dans l'espace ; Maya, attachée par un câble, travaille sur la station."""
    S = Scene()
    espace(S, 6)
    terre_arc(S, 1500, 1050)
    S.add(station(560, 210, 0.75))
    S.add(chemin("M 520 230 Q 420 330 340 380", stroke="#dee2e6", sw=4))
    S.add(combinaison(300, 560, 1.15, expr="concentre", bras="tend", rot=20, regard=(1, -0.5)))
    S.add(texte(240, 130, "Attachée !", 46, "#fff", contour="#1864ab"))
    return S


def p11():
    """Plan large : la nuit, à la fenêtre, Nina voit passer la station comme une étoile qui file."""
    S = Scene()
    nuit(S, "#0b1433", "#364fc7")
    etoiles(S, 50, 9, (0, 0, 800, 520))
    S.add(cercle(430, 170, 9, "#fff"), cercle(430, 170, 22, "#fff", opacity=0.2))
    S.add(chemin("M 220 290 Q 320 220 418 176", stroke="#fff", sw=3, opacity=0.5, stroke_dasharray="6 10"))
    S.add(maison(400, 760, 1.6, mur="#ffe8cc", toit="#c92a2a", lumiere=True, cote=False))
    S.add(personne(400 - 80 * 1.6 + 20, 760 - 100 * 1.6 + 46, 0.42, expr="content", bras="coucou", ombre=False, **NINA))
    S.add(bulle(560, 330, 360, 90, "Bonne nuit, Maman !", 34, pointe=(310, 560)))
    S.add(rect(0, 760, 800, 40, "#2b8a3e"))
    S.cachette(740, 790)
    return S


def capsule(x, y, s=1.0, parachutes=True):
    m = []
    if parachutes:
        for dx, ang in ((-160, -20), (0, 0), (160, 20)):
            px, py = dx, -420
            m.append(trait(-30, -110, px - 70, py + 40, "#868e96", 2) + trait(30, -110, px + 70, py + 40, "#868e96", 2))
            dome = chemin(f"M {px - 90} {py + 40} Q {px} {py - 110} {px + 90} {py + 40} Q {px} {py + 10} {px - 90} {py + 40} Z", "#fff")
            m.append(dome)
            for k in (-1, 1):
                m.append(chemin(f"M {px + k * 30} {py + 26} Q {px + k * 34} {py - 40} {px} {py - 72}", stroke="#ff922b", sw=10))
    m += [chemin("M -90 0 L -60 -120 Q 0 -150 60 -120 L 90 0 Z", volume("#f8f9fa", 0.3, 0.8)), rect(-96, -10, 192, 24, "#343a40", rx=10),
          cercle(-20, -70, 14, "#495057"), cercle(26, -70, 14, "#495057")]
    return place(m, x, y, s)


def p12():
    """Plan large : la capsule descend sous ses parachutes vers la mer ; un bateau l'attend."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(nuage(140, 140, 0.7), nuage(680, 220, 0.5))
    eau(S, 640)
    S.add(capsule(400, 520, 0.85))
    bateau = g([chemin("M -120 0 L 120 0 L 90 40 L -90 40 Z", "#e03131"), rect(-60, -50, 90, 50, "#fff"), rect(-50, -40, 24, 20, "#a5d8ff"),
                rect(-14, -40, 24, 20, "#a5d8ff")])
    S.add(place(bateau, 650, 690, 1.0))
    S.cachette(None)          # au-dessus de la mer, rien où se poser
    return S


def p13():
    """Plan moyen : de retour à la maison, Maya, un peu chancelante, serre Nina dans ses bras."""
    S = Scene()
    maison_dedans(S)
    S.add(fenetre(470, 90, 200, 160, "#a5d8ff", rideaux="#ffd43b",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), nuage(560, 160, 0.4)])))
    S.add(maya(330, 790, 1.4, expr="content", bras="calin", regard=(1, 0.4)))
    S.add(personne(470, 790, 1.2, expr="rire", bras="calin", flip=True, regard=(-1, -0.4), **NINA))
    S.add(personne(640, 790, 1.35, expr="content", bras="applaudit", regard=(-1, 0), **PAPA))
    for x, y in ((380, 230), (470, 200), (420, 160)):
        S.add(coeur(x, y, 0.8, "#ff6b6b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fusee-seule.svg", vignette),
    ("01-la-maquette.svg", p01), ("02-la-piscine.svg", p02), ("03-decollage.svg", p03),
    ("04-le-hublot.svg", p04), ("05-la-station.svg", p05), ("06-tout-flotte.svg", p06),
    ("07-la-tortilla.svg", p07), ("08-le-tapis.svg", p08), ("09-dormir-au-mur.svg", p09),
    ("10-la-sortie.svg", p10), ("11-une-etoile-qui-file.svg", p11), ("12-les-parachutes.svg", p12),
    ("13-le-calin.svg", p13),
]
