"""Le tambour de la fête — la Fête de la musique, et le rythme qui rassemble.

Le 21 juin, jour le plus long de l'année, toute la rue de Sami joue de la
musique : le violon de Madame Lin, l'accordéon de Papi Jo, la guitare de
Lila. Sami n'a pas d'instrument. Il fabrique un tambour avec une casserole
et deux cuillères en bois. Quand tous les musiciens jouent en même temps et
pas la même chanson, c'est le charivari ! Sami tape un rythme lent et
régulier, comme un cœur — boum… tac — et tout le monde le suit.

Plans : 1 large (la rue) · 2 moyen (violon et accordéon) · 3 moyen (la
guitare ; « Et moi ? ») · 4 moyen (la cuisine) · 5 gros plan (boum, tac,
bing !) · 6 large (charivari) · 7 contre-plongée (sur le muret) · 8 moyen
(on le suit) · 9 large (on danse) · 10 large, soir (bravo) · 11 moyen, nuit
(le cœur).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from fables import violon, archet
from objets import bol
from fetes import guirlande_fanions, guirlande_lumineuse, chien_profil

ID = "musique-tambour"
PAPIER_PEINT = "rayures"

SAMI = dict(peau="doree", cheveux="noir", coiffure="boucles", habit="#1971c2", robe=False, jambes="#495057",
            nez="rond")
PAPA = dict(peau="doree", cheveux="noir", coiffure="courts", habit="#f08c00", robe=False, jambes="#343a40",
            stature="adulte", carrure="ronde", barbe="#2b2b3a", nez="rond")
LIN = dict(peau="claire", cheveux="noir", coiffure="chignon", habit="#e64980", stature="adulte", carrure="fine",
           yeux="cils", nez="petit")
JO = dict(peau="foncee", cheveux="blanc", coiffure="chauve_cote", habit="#2f9e44", robe=False, jambes="#5c3d2e",
          stature="ancien", carrure="ronde", acc=("lunettes",))
LILA = dict(peau="rosee", cheveux="roux", coiffure="queue", habit="#7048e8", robe=False, jambes="#1c7ed6",
            stature="ado", taches=True)


def sami(x, y, s=1.3, **k):
    return personne(x, y, s, **{**SAMI, **k})


def papa(x, y, s=1.3, **k):
    return personne(x, y, s, **{**PAPA, **k})


def lin(x, y, s=1.2, violon_=True, **k):
    if violon_:
        k.setdefault("bras", "tient")
        k.setdefault("objet", place(violon(0, 0, 1.0, rot=-60) + archet(30, 30, 1.0, rot=60), *ancre(40, -150, "tient", "adulte", "fine"), 1.1))
    return personne(x, y, s, **{**LIN, **k})


def jo(x, y, s=1.2, accordeon_=True, ferme=False, **k):
    if accordeon_:
        k.setdefault("bras", "large")
        k.setdefault("objet", place(accordeon(ferme=ferme), 0, -82, 1.0))
    return personne(x, y, s, **{**JO, **k})


def lila(x, y, s=1.2, guitare_=True, **k):
    if guitare_:
        k.setdefault("bras", "porte")
        k.setdefault("objet", place(guitare(), 0, -60, 1.0, rot=-30))
    return personne(x, y, s, **{**LILA, **k})


def accordeon(ferme=False):
    """Accordéon tenu à deux mains ; repère : le centre."""
    w = 40 if ferme else 66
    m = [rect(-w - 20, -40, 22, 80, "#c92a2a", rx=4), rect(w - 2, -40, 22, 80, "#c92a2a", rx=4)]
    for k in range(int(w / 7)):
        xx = -w + k * 14
        m.append(poly([(xx, -36), (xx + 7, -40), (xx + 14, -36), (xx + 14, 36), (xx + 7, 40), (xx, 36)],
                      "#f8f9fa" if k % 2 else "#dee2e6"))
    for j in range(4):
        m.append(cercle(w + 9, -26 + j * 17, 4, "#f8f9fa"))
        m.append(rect(-w - 16, -32 + j * 17, 14, 10, "#f8f9fa", rx=2))
    return g(m)


def guitare():
    """Guitare ; repère : le centre de la caisse."""
    return g([ellipse(0, 12, 40, 34, "#e67700"), ellipse(0, -26, 30, 26, "#e67700"), cercle(0, -4, 11, "#5c3a1e"),
              rect(-6, -130, 12, 110, "#8d5524"), rect(-10, -150, 20, 24, "#5c3a1e", rx=4),
              trait(-3, -128, -3, 30, "#f1f3f5", 1.2), trait(3, -128, 3, 30, "#f1f3f5", 1.2), rect(-14, 26, 28, 6, "#5c3a1e")])


def casserole(x, y, s=1.0, rot=0, retournee=True):
    """Casserole retournée qui sert de tambour ; (x, y) = milieu du fond."""
    if retournee:
        m = [rect(-56, -50, 112, 50, cylindre("#adb5bd", 0.4, 0.7), rx=6), ellipse(0, -50, 56, 12, "#dee2e6"),
             rect(54, -32, 70, 12, "#343a40", rx=6), ellipse(0, -50, 30, 5, "#fff", opacity=0.5)]
    else:
        m = [rect(-56, -50, 112, 50, cylindre("#adb5bd", 0.4, 0.7), rx=6), ellipse(0, -50, 56, 12, "#495057"),
             rect(54, -46, 70, 12, "#343a40", rx=6)]
    return place(m, x, y, s, rot=rot)


def cuillere_bois(x, y, s=1.0, rot=0):
    return place([rect(-4, -60, 8, 70, "#c68642", rx=4), ellipse(0, -70, 12, 18, "#c68642")], x, y, s, rot=rot)


def seau(x, y, s=1.0, couleur="#1c7ed6"):
    return place([chemin("M -40 0 L -50 -90 L 50 -90 L 40 0 Z", volume(couleur, 0.3, 0.75)), ellipse(0, -90, 50, 10, _assombrir(couleur, 0.7))], x, y, s)


def tambour_sami(dy=0):
    """La casserole et les deux cuillères, dans les mains de Sami (pose « porte »)."""
    return g([casserole(0, -38 + dy, 0.62), cuillere_bois(-28, -76 + dy, 0.8, rot=-30), cuillere_bois(28, -76 + dy, 0.8, rot=30)])


def rue(S, y=640, soir=False, fanions=True):
    if soir:
        ciel(S, "#f76707", "#ffd8a8")
        S.add(soleil(640, 470, 60, couleur="#ff922b", rayons=False))
    else:
        ciel(S, "#4dabf7", "#e7f5ff")
        S.add(soleil(680, 90, 46))
    S.add(immeuble(-40, y, 250, 4, "#ffe8cc", toit="mansarde", lumiere=soir, graine=2),
          immeuble(250, y, 220, 4, "#e7f5ff", toit="pignon", rdc="boutique", store="#e64980", lumiere=soir, graine=3),
          immeuble(520, y, 260, 4, "#fff3bf", toit="mansarde", lumiere=soir, graine=4))
    S.add(rect(0, y, 800, 30, "#ced4da"), rect(0, y + 30, 800, 800 - y, "#adb5bd"))
    if fanions:
        S.add(guirlande_fanions(0, 120, 800, 120, creux=40, nb=16))
    if soir:
        S.add(guirlande_lumineuse(0, 200, 800, 200, creux=30, nb=14))


def notes_volantes(S, x, y, couleur="#1971c2", s=1.0, rot=0):
    S.add(place(notes(0, 0, 1.0, couleur), x, y, s, rot=rot))


def muret(S, x0=0, x1=800, y=700, h=70):
    S.add(rect(x0, y - h, x1 - x0, h, "#e9d8c4"), pierres(x0, y - h, x1 - x0, h, "#e9d8c4", pas_=20, larg=40, opacite=0.4))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue(S)
    muret(S, 200, 600, 710, 80)
    S.add(lin(110, 760, 1.15, expr="content", regard=(1, 0)))
    S.add(jo(690, 760, 1.15, expr="rire", regard=(-1, 0)))
    S.add(sami(400, 640, 1.45, expr="rire", bras="porte", objet=tambour_sami(), regard=(0, 0)))
    for k, (x, y, c) in enumerate(((250, 300, "#e64980"), (530, 270, "#2f9e44"), (400, 210, "#1971c2"))):
        notes_volantes(S, x, y, c, 1.2, rot=(-1) ** k * 10)
    S.add(texte(640, 350, "Boum, tac !", 46, "#e03131", contour="#fff", rot=8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(casserole(200, 240, 1.5))
    S.add(cuillere_bois(120, 160, 1.3, rot=-35), cuillere_bois(280, 160, 1.3, rot=35))
    S.add(notes(300, 60, 0.9, "#1971c2"))
    return S


def p01():
    """Plan large : le 21 juin, toute la rue sort ses instruments."""
    S = Scene()
    rue(S)
    S.add(texte(400, 230, "21 juin", 60, "#1971c2", contour="#fff", rot=-4))
    S.add(lin(130, 740, 0.95, expr="content", regard=(1, 0), pas="marche"))
    S.add(jo(330, 750, 0.95, accordeon_=True, expr="rire", regard=(1, 0)))
    S.add(lila(520, 755, 0.95, expr="rire", regard=(-1, 0)))
    S.add(sami(680, 770, 1.0, expr="bouche_bee", bras="joues", regard=(-1, 0)))
    for k, (x, y, c) in enumerate(((160, 420, "#e64980"), (360, 440, "#2f9e44"), (560, 420, "#7048e8"))):
        notes_volantes(S, x, y, c, 0.9, rot=(-1) ** k * 12)
    S.cachette(40, 780)
    return S


def p02():
    """Plan moyen : le violon au balcon, l'accordéon à la terrasse du café."""
    S = Scene()
    ciel(S, "#4dabf7", "#e7f5ff")
    S.add(rect(0, 0, 420, 800, "#ffe8cc"), briques(0, 0, 420, 640, "#ffe8cc", hb=22, lb=44))
    S.add(rect(60, 120, 260, 260, "#a5d8ff"), rect(50, 110, 280, 14, "#8d5524"))
    S.add(lin(190, 420, 1.15, expr="content", regard=(1, 0)))
    S.add(rect(30, 420, 320, 20, "#495057"), garde_corps(30, 420, 320, "#343a40", 80))
    S.add(texte(250, 90, "zing, zing !", 44, "#e64980", contour="#fff", rot=-6))
    S.add(rect(0, 640, 800, 160, "#adb5bd"))
    S.add(store_banne(430, 300, 370, "#2f9e44", "#fff"))
    S.add(table(640, 770, 160, 110, "#868e96"))
    S.add(jo(530, 780, 1.3, expr="rire", regard=(-1, 0)))
    S.add(texte(620, 450, "flon, flon !", 44, "#2f9e44", contour="#fff", rot=6))
    notes_volantes(S, 300, 250, "#e64980", 1.0)
    notes_volantes(S, 600, 380, "#2f9e44", 1.0, rot=10)
    S.cachette(760, 780)
    return S


def p03():
    """Plan moyen : la guitare de Lila ; Sami n'a rien. « Et moi ? »"""
    S = Scene()
    rue(S, fanions=True)
    S.add(lila(260, 770, 1.45, expr="rire", regard=(1, 0)))
    S.add(texte(240, 300, "dzing !", 50, "#7048e8", contour="#fff", rot=-8))
    S.add(sami(560, 780, 1.4, expr="triste", bras="epaules", regard=(-1, 0)))
    S.add(bulle(580, 290, 340, 100, "Et moi ? Je n'ai pas\nd'instrument !", 30, pointe=(570, 400)))
    notes_volantes(S, 330, 380, "#7048e8", 1.1)
    S.cachette(740, 770)
    return S


def p04():
    """Plan moyen : dans la cuisine, Sami cherche partout."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(etagere(560, 260, 300, objets=g([bol(470, 260, 0.7, "#e64980"), casserole(560, 260, 0.6, retournee=False),
                                           bol(650, 260, 0.7, "#1c7ed6")])))
    S.add(seau(140, 720, 0.9))
    S.add(sami(380, 760, 1.45, expr="concentre", bras="porte", regard=(1, -0.5),
               objet=g([casserole(0, -40, 0.6), cuillere_bois(-30, -80, 0.8, rot=-20), cuillere_bois(30, -80, 0.8, rot=20)])))
    S.add(texte(640, 420, "?", 70, "#1971c2"))
    S.add(papa(650, 760, 1.25, expr="surpris", bras="hanches", regard=(-1, 0)))
    return S


def p05():
    """Gros plan : Boum ! Tac ! Bing ! Papa se bouche les oreilles en riant."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(sami(330, 840, 2.0, expr="rire", bras="porte", objet=tambour_sami(), regard=(1, 0)))
    S.add(papa(650, 860, 1.7, expr="rire", bras="joues", regard=(-1, 0)))
    S.camera(1.15, 430, 470)
    S.dessus(texte(180, 130, "Boum !", 64, "#e03131", contour="#fff", rot=-10),
             texte(420, 90, "Tac !", 64, "#1971c2", contour="#fff"),
             texte(640, 140, "Bing !", 64, "#f08c00", contour="#fff", rot=10))
    S.cachette(120, 760)
    return S


def p06():
    """Plan large : tout le monde joue en même temps… et pas la même chanson."""
    S = Scene()
    rue(S)
    r = __import__("random").Random(4)
    for k in range(9):
        x, y = r.uniform(60, 740), r.uniform(220, 440)
        notes_volantes(S, x, y, ("#e64980", "#2f9e44", "#7048e8", "#e03131")[k % 4], r.uniform(0.7, 1.2), rot=r.uniform(-60, 60))
    S.add(chemin("M 120 300 C 200 200 260 420 340 300 S 480 200 540 340 S 680 260 700 360", stroke="#495057", sw=4, opacity=0.5))
    S.add(lin(110, 760, 1.05, expr="concentre", regard=(1, 0)))
    S.add(jo(300, 770, 1.05, expr="concentre", regard=(1, 0)))
    S.add(lila(480, 775, 1.05, expr="concentre", regard=(-1, 0)))
    S.add(personne(660, 780, 1.05, peau="brune", cheveux="noir", coiffure="afro", habit="#fab005", robe=False,
                   jambes="#343a40", stature="adulte", expr="concentre", bras="bouche",
                   objet=place([rect(-6, -20, 70, 14, "#fcc419", rx=4), poly([(60, -30), (90, -44), (90, 4), (60, -6)], "#fcc419")], 0, -112)))
    S.add(chien_profil(560, 790, 0.6, expr="ouvert"))
    S.add(texte(400, 560, "Quel charivari !", 52, "#495057", contour="#fff", rot=-4))
    S.cachette(770, 785)
    return S


def p07():
    """Contre-plongée : Sami debout sur le muret, boum… tac."""
    S = Scene()
    ciel(S, "#228be6", "#a5d8ff")
    S.add(nuage(150, 140, 0.8), nuage(640, 100, 0.6))
    S.add(immeuble(-60, 800, 260, 7, "#ffe8cc", toit="mansarde", graine=5, h_etage=90),
          immeuble(600, 800, 260, 7, "#fff3bf", toit="mansarde", graine=6, h_etage=90))
    muret(S, 120, 680, 800, 150)
    S.add(sami(400, 650, 1.8, expr="concentre", bras="porte", objet=tambour_sami(), regard=(0, 0)))
    S.add(texte(250, 230, "Boum…", 64, "#e03131", contour="#fff", rot=-6))
    S.add(texte(560, 260, "tac.", 64, "#1971c2", contour="#fff", rot=6))
    S.cachette(150, 600, "air")
    return S


def p08():
    """Plan moyen : un à un, les musiciens suivent le rythme de Sami."""
    S = Scene()
    rue(S)
    muret(S, 280, 520, 700, 70)
    S.add(sami(400, 630, 1.15, expr="rire", bras="porte", objet=tambour_sami(), regard=(0, 0)))
    S.add(lin(140, 770, 1.05, expr="content", regard=(1, -0.3)))
    S.add(jo(650, 775, 1.05, expr="rire", regard=(-1, -0.3)))
    S.add(lila(400, 790, 0.95, expr="rire", regard=(0, -0.5)))
    for k in range(7):
        notes_volantes(S, 70 + k * 105, 300 + (k % 2) * 20, ("#e64980", "#2f9e44", "#7048e8")[k % 3], 0.8)
    S.cachette(270, 730, "air")
    return S


def p09():
    """Plan large : la rue danse ; même le chien remue la queue en rythme."""
    S = Scene()
    rue(S)
    S.add(personne(120, 760, 1.05, peau="claire", cheveux="blond", coiffure="longs", habit="#12b886", stature="adulte",
                   expr="rire", bras="danse"))
    S.add(personne(270, 770, 1.05, peau="foncee", cheveux="noir", coiffure="courts", habit="#e8590c", robe=False,
                   jambes="#343a40", stature="adulte", expr="rire", bras="danse", flip=True))
    S.add(papa(450, 770, 1.05, expr="rire", bras="epaule", regard=(1, 0)))
    S.add(personne(560, 785, 1.0, peau="rosee", cheveux="chatain", coiffure="couettes", habit="#f783ac",
                   stature="petit", expr="rire", bras="applaudit"))
    S.add(chien_profil(680, 790, 0.7, flip=True, queue_haute=True))
    S.add(mouvement(760, 690, 0.6, rot=-60))
    S.add(sami(330, 790, 0.95, expr="rire", bras="porte", objet=tambour_sami(), regard=(1, 0)))
    for k in range(5):
        notes_volantes(S, 100 + k * 150, 380 + (k % 2) * 40, ("#e64980", "#1971c2", "#2f9e44")[k % 3], 0.9, rot=(-1) ** k * 10)
    S.cachette(140, 70, "air")
    return S


def p10():
    """Plan large, soir : le soleil se couche enfin ; « Bravo, chef d'orchestre ! »"""
    S = Scene()
    rue(S, soir=True, fanions=False)
    muret(S, 260, 540, 710, 70)
    S.add(sami(400, 640, 1.2, expr="fier", bras="victoire", regard=(0, 0)))
    S.add(papa(150, 780, 1.15, expr="rire", bras="applaudit", regard=(1, -0.3)))
    S.add(lin(640, 780, 1.05, violon_=False, expr="rire", bras="applaudit", regard=(-1, -0.3)))
    S.add(jo(520, 790, 1.0, accordeon_=False, expr="rire", bras="applaudit", regard=(-1, -0.3)))
    S.add(bulle(170, 330, 300, 100, "Bravo, chef\nd'orchestre !", 32, pointe=(160, 460)))
    S.cachette(760, 770)
    return S


def p11():
    """Plan moyen, nuit : dans son lit, Sami entend son cœur : boum, tac."""
    S = Scene()
    piece(S, "chambre", 620)
    S.ambiance("nuit")
    S.add(fenetre(560, 100, 160, 140, "#1c2a52", nuit_=True, rideaux="#1971c2"))
    S.add(lampe(110, 640, 0.85, allumee=False, halo=False))
    S.add(lit(420, 790, 460, "#e7f5ff", "#1971c2"))
    S.add(place(sami(0, 0, 0.95, expr="content", bras="bas"), 380, 655, 1.0, rot=-90))
    S.add(rect(320, 625, 330, 100, lineaire([(0, "#339af0"), (1, "#1971c2")]), rx=24))
    S.add(casserole(640, 790, 0.6), cuillere_bois(700, 780, 0.6, rot=80))
    S.add(coeur(330, 450, 1.3, "#fa5252"))
    S.add(texte(440, 430, "boum, tac", 40, "#fa5252", rot=-6))
    S.cachette(760, 700)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("casserole-seule.svg", vignette),
    ("01-le-21-juin.svg", p01), ("02-violon-accordeon.svg", p02), ("03-et-moi.svg", p03),
    ("04-dans-la-cuisine.svg", p04), ("05-boum-tac-bing.svg", p05), ("06-charivari.svg", p06),
    ("07-sur-le-muret.svg", p07), ("08-on-le-suit.svg", p08), ("09-on-danse.svg", p09),
    ("10-bravo.svg", p10), ("11-le-coeur.svg", p11),
]
