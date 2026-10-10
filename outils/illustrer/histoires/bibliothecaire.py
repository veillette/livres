"""Une journée à la bibliothèque — Monsieur Ali, bibliothécaire.

Emma vient avec Grand-papa chercher sa première carte de bibliothèque.
Monsieur Ali lui montre les rayons, l'étiquette (la cote) qui dit où habite
chaque livre, l'heure du conte, l'emprunt au lecteur de cartes, l'hôpital
des livres et la chute à livres. Emma repart avec trois livres, qu'elle
rapportera dans trois semaines.

Plans : 1 large (la façade) · 2 moyen (la carte) · 3 large (les rayons) ·
4 gros plan (la cote) · 5 moyen (l'escabeau) · 6 large (l'heure du conte) ·
7 gros plan (bip ! l'emprunt) · 8 moyen (l'hôpital des livres) · 9 large
(la chute à livres, le soir) · 10 moyen (lire au lit).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit
from fantastique import echelle

ID = "bibliothecaire"
PAPIER_PEINT = "losanges"

ALI = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#5f3dc4", jambes="#495057",
           acc=("lunettes",), barbe="#2b2b3a", nez="rond")
EMMA = dict(peau="claire", cheveux="blond", coiffure="queue", habit="#f06595", jambes="#5f3dc4", yeux="cils")
GRAND_PAPA = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#2b8a3e", robe=False,
                  jambes="#5c3a1e", carrure="ronde", nez="rond")

COULEURS_LIVRES = ("#fa5252", "#4dabf7", "#fcc419", "#51cf66", "#cc5de8", "#ff922b", "#20c997", "#f06595", "#748ffc")


def ali(x, y, s=1.4, **k):
    return pro(x, y, s, **{**ALI, **k})


def emma(x, y, s=1.2, **k):
    return personne(x, y, s, **{**EMMA, **k})


def grand_papa(x, y, s=1.3, **k):
    return personne(x, y, s, **{**GRAND_PAPA, **k})


def livre(x, y, s=1.0, couleur="#fa5252", rot=0, ouvert=False, titre=""):
    """Un livre vu de face (couverture), ou ouvert ; (x, y) = centre."""
    if ouvert:
        m = [chemin("M 0 -40 Q -40 -50 -80 -40 L -80 40 Q -40 30 0 40 Z", "#fff", stroke="#dee2e6", sw=2),
             chemin("M 0 -40 Q 40 -50 80 -40 L 80 40 Q 40 30 0 40 Z", "#fff", stroke="#dee2e6", sw=2),
             trait(0, -40, 0, 40, "#ced4da", 2)]
        for k in range(4):
            m.append(trait(-66, -22 + k * 14, -14, -24 + k * 14, "#ced4da", 3))
            m.append(trait(14, -24 + k * 14, 66, -22 + k * 14, "#ced4da", 3))
        m.append(rect(-84, 36, 168, 8, couleur, rx=3))
    else:
        m = [rect(-40, -54, 80, 108, volume(couleur, 0.3, 0.8), rx=4), rect(-40, -54, 10, 108, _assombrir(couleur, 0.8), rx=3),
             rect(-22, -36, 52, 26, "#fff", rx=3, opacity=0.85)]
        if titre:
            m.append(titre)
    return place(m, x, y, s, rot=rot)


def dino(x, y, s=1.0, c="#51cf66"):
    """Petit dinosaure dessiné sur une couverture."""
    return place([ellipse(0, 0, 22, 14, c), chemin("M 16 -6 Q 30 -30 34 -30 Q 40 -28 34 -22 Q 28 -18 22 -2 Z", c),
                  chemin("M -18 0 Q -34 6 -40 0", stroke=c, sw=6), trait(-8, 10, -8, 22, c, 5), trait(8, 10, 8, 22, c, 5)], x, y, s)


def etageres(x, y, w=300, h=420, rangs=4, graine=1, bois="#a0693a"):
    """Bibliothèque pleine de livres ; (x, y) = coin bas gauche."""
    r = random.Random(graine)
    m = [rect(x, y - h, w, h, volume(bois, 0.3, 0.8), rx=6), rect(x + 10, y - h + 10, w - 20, h - 20, _assombrir(bois, 0.7))]
    hr = (h - 20) / rangs
    for k in range(rangs):
        base_ = y - 10 - k * hr
        xx = x + 14
        while xx < x + w - 24:
            lw = r.uniform(14, 26)
            lh = hr - r.uniform(12, 30)
            c = r.choice(COULEURS_LIVRES)
            if r.random() < 0.08 and xx > x + 40:
                m.append(place(rect(-lw / 2, -lh, lw, lh, c, rx=2), xx + lw / 2, base_ - 2, rot=-14))
                xx += lw + 8
                continue
            m.append(rect(xx, base_ - lh, lw, lh, volume(c, 0.3, 0.8), rx=2))
            m.append(rect(xx + 2, base_ - lh * 0.35, lw - 4, 8, "#fff", rx=2, opacity=0.8))
            xx += lw + 1.5
        m.append(rect(x + 6, base_ - 2, w - 12, 10, volume(bois, 0.4, 0.75), rx=2))
    return g(m)


def salle(S, y=600, graine=1):
    piece(S, "manoir", y)
    S.add(etageres(20, y + 10, 240, 430, 4, graine))
    S.add(etageres(540, y + 10, 240, 430, 4, graine + 1))


def comptoir(x, y, s=1.0):
    """Comptoir de prêt ; (x, y) = milieu du pied ; le dessus est à y - 200 s."""
    return place([rect(-220, -200, 440, 200, volume("#c68642", 0.3, 0.8), rx=8), rect(-236, -214, 472, 22, volume("#8d5524", 0.35, 0.75), rx=6),
                  rect(-200, -170, 400, 140, "none", rx=6, stroke=_assombrir("#c68642", 0.8), stroke_width=3)], x, y, s)


def carte_biblio(x, y, s=1.0, rot=0):
    return place([rect(-50, -32, 100, 64, "#fff", rx=8, stroke="#5f3dc4", stroke_width=4), rect(-50, -32, 100, 18, "#5f3dc4", rx=6),
                  cercle(-26, 6, 12, "#ffc9c9"), trait(-6, 0, 36, 0, "#adb5bd", 4), trait(-6, 14, 30, 14, "#adb5bd", 4),
                  chemin("M -40 26 h 4 m 3 0 h 2 m 3 0 h 6 m 3 0 h 2 m 4 0 h 5", stroke=ENCRE, sw=3)], x, y, s, rot=rot)


def lecteur(x, y, s=1.0, bip=True):
    """Lecteur de codes-barres sur le comptoir."""
    m = [rect(-50, -30, 100, 30, "#343a40", rx=6), rect(-34, -26, 68, 6, "#fa5252", rx=3)]
    if bip:
        m.append(poly([(-34, -26), (34, -26), (60, -120), (-60, -120)], "#fa5252", opacity=0.18))
    return place(m, x, y, s)


def chariot(x, y, s=1.0, graine=2):
    m = [rect(-120, -150, 240, 16, "#868e96", rx=4), rect(-120, -70, 240, 16, "#868e96", rx=4), trait(-110, -150, -110, -10, "#495057", 6),
         trait(110, -150, 110, -10, "#495057", 6), cercle(-100, -6, 12, "#343a40"), cercle(100, -6, 12, "#343a40")]
    r = random.Random(graine)
    for base_ in (-150, -70):
        xx = -110
        while xx < 100:
            lw = r.uniform(14, 24)
            m.append(rect(xx, base_ - 60, lw, 60, r.choice(COULEURS_LIVRES), rx=2))
            xx += lw + 2
    return place(m, x, y, s)


def facade(S, y=640, nuit_=False):
    """La bibliothèque vue de la rue."""
    if nuit_:
        nuit(S, "#1c2a52", "#4c5b9a")
        etoiles(S, 25, 4, (0, 0, 800, 300))
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    S.add(arbre(80, y, 1.0), arbre(730, y, 0.9))
    mur = "#f3d9fa" if not nuit_ else "#d0bfff"
    m = [rect(150, y - 330, 500, 330, volume(mur, 0.2, 0.85)), poly([(130, y - 330), (400, y - 440), (670, y - 330)], volume("#ae3ec9", 0.3, 0.8)),
         rect(130, y - 340, 540, 16, "#862e9c"), rect(250, y - 300, 300, 50, "#fff", rx=8, stroke="#ae3ec9", stroke_width=4)]
    S.add(g(m))
    S.add(texte(400, y - 263, "BIBLIOTHÈQUE", 34, "#862e9c"))
    for fx in (180, 540):
        vitre = "#ffe066" if nuit_ else "#a5d8ff"
        S.add(rect(fx, y - 220, 80, 120, vitre, stroke="#fff", stroke_width=6), rect(fx + 37, y - 220, 6, 120, "#fff"))
        if nuit_:
            S.lumiere(fx + 40, y - 160, 100, "#ffd43b", 0.6)
    S.add(rect(350, y - 180, 100, 180, cylindre("#862e9c", 0.25, 0.75), rx=6), cercle(434, y - 90, 6, "#fcc419"))
    S.add(rect(0, y, 800, 800 - y, "#ced4da"))
    S.add(rect(0, y, 800, 8, "#adb5bd"))
    S.proposer_cachette(60, y + 40)
    S.proposer_cachette(740, y + 40)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salle(S, 620, graine=3)
    S.add(tapis(400, 760, 320, 50, "#d0bfff", "#9775fa"))
    S.add(ali(270, 790, 1.5, expr="content", bras="tient", regard=(1, 0.2),
              objet=livre(*ancre(70, -150, "tient", "adulte"), 0.8, "#fa5252", titre=dino(4, -18, 0.6))))
    S.add(emma(520, 790, 1.4, expr="rire", bras="porte", regard=(-1, -0.3), objet=livre(0, -80, 0.7, "#4dabf7")))
    return S


def vignette():
    S = Scene(400, 270)
    for k, c in enumerate(("#fa5252", "#4dabf7", "#fcc419")):
        S.add(livre(120 + k * 80, 160 + (k % 2) * 10, 1.1, c, rot=(k - 1) * 8))
    return S


def p01():
    """Plan large : Emma et Grand-papa arrivent devant la bibliothèque."""
    S = Scene()
    facade(S, 640)
    S.add(grand_papa(220, 780, 1.1, expr="content", bras="main", regard=(1, 0)))
    S.add(emma(330, 785, 1.0, expr="rire", bras="main", flip=True, regard=(-1, -0.3)))
    return S


def p02():
    """Plan moyen : au comptoir, Monsieur Ali tend à Emma sa toute première carte."""
    S = Scene()
    salle(S, 600, graine=4)
    S.add(ali(270, 640, 1.25, expr="content", bras="donne", regard=(1, 0.3)))
    S.add(comptoir(300, 790, 1.0))
    hx, hy = mains_personne(270, 640, 1.25, "donne", stature="adulte")[1]
    S.add(carte_biblio(hx + 40, hy + 10, 1.0, rot=-8))
    S.add(emma(580, 790, 1.35, expr="surpris", bras="joues", regard=(-1, -0.3)))
    S.add(grand_papa(720, 790, 1.2, expr="content", bras="bas", regard=(-1, 0)))
    S.add(bulle(330, 120, 360, 90, "Voici ta carte !", 38, pointe=(300, 380)))
    return S


def p03():
    """Plan large : les rayons pleins de livres ; des enfants lisent sur des coussins."""
    S = Scene()
    piece(S, "manoir", 600)
    for k, x in enumerate((10, 280, 550)):
        S.add(etageres(x, 610, 240, 470, 5, 10 + k))
    S.add(tapis(400, 740, 340, 50, "#ffe066", "#fab005"))
    S.add(ellipse(200, 760, 80, 24, "#ff8787"), ellipse(600, 760, 80, 24, "#74c0fc"))
    S.add(petit(200, 760, 1.0, peau="foncee", cheveux="noir", coiffure="afro", habit="#ffd43b", expr="content", bras="porte",
                regard=(0, 0.6), objet=livre(0, -80, 0.6, "#51cf66", ouvert=True)))
    S.add(petit(600, 760, 1.0, peau="doree", cheveux="brun", coiffure="couettes", habit="#ff922b", expr="rire", bras="porte",
                regard=(0, 0.6), objet=livre(0, -80, 0.6, "#cc5de8", ouvert=True)))
    S.add(emma(400, 790, 1.15, expr="bouche_bee", bras="ouverts", regard=(0, -0.6)))
    return S


def p04():
    """Gros plan : l'étiquette au dos du livre dit où il habite sur l'étagère."""
    S = Scene()
    piece(S, "manoir", 600)
    S.add(etageres(80, 760, 640, 560, 4, 21))
    S.add(rect(330, 300, 90, 330, volume("#fa5252", 0.3, 0.8), rx=6))
    S.add(rect(340, 520, 70, 70, "#fff", rx=6, stroke="#adb5bd", stroke_width=3))
    S.add(texte(375, 548, "DIN", 22, ENCRE), texte(375, 576, "567", 22, ENCRE))
    S.add(dino(375, 400, 1.0, "#ffe066"))
    S.add(ali(640, 800, 1.6, expr="content", bras="designe", flip=True, regard=(-1, -0.2)))
    S.camera(1.25, 420, 470)
    S.dessus(bulle(240, 110, 400, 90, "Ici, les dinosaures !", 34, pointe=S.vers_page(375, 520)))
    S.cachette(170, 178, "air")
    return S


def p05():
    """Plan moyen : sur un escabeau, Monsieur Ali attrape un livre tout en haut."""
    S = Scene()
    piece(S, "manoir", 600)
    S.add(etageres(240, 620, 340, 580, 5, 31))
    S.add(rect(330, 640, 140, 20, "#868e96", rx=4), rect(350, 540, 100, 20, "#868e96", rx=4),
          trait(320, 790, 360, 540, "#495057", 8), trait(480, 790, 440, 540, "#495057", 8))
    S.add(ali(400, 545, 1.15, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(livre(400 + 70 * 1.15, 545 - 175 * 1.15, 0.7, "#51cf66", titre=dino(4, -18, 0.6)))
    S.add(emma(160, 790, 1.3, expr="joie", bras="joues", regard=(1, -1)))
    return S


def p06():
    """Plan large : l'heure du conte ; Monsieur Ali lit aux enfants assis sur le tapis."""
    S = Scene()
    salle(S, 600, graine=5)
    S.add(tapis(400, 740, 360, 60, "#d0bfff", "#9775fa"))
    S.add(ali(400, 650, 1.2, expr="joie", bras="porte", objet=livre(0, -80, 0.85, "#fcc419", ouvert=True)))
    for k, (x, pk) in enumerate(((180, dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#ffd43b")),
                                 (300, EMMA), (500, dict(peau="doree", cheveux="brun", coiffure="couettes", habit="#ff922b")),
                                 (620, dict(peau="rosee", cheveux="roux", coiffure="courts", habit="#20c997", robe=False)))):
        S.add(personne(x, 790, 0.95, expr=("rire", "bouche_bee", "content", "surpris")[k], bras="bas", regard=(0, -0.6), **{**pk, "stature": "petit"}))
    S.add(texte(400, 90, "L'heure du conte", 48, "#5f3dc4", contour="#fff"))
    return S


def p07():
    """Gros plan : bip ! Le lecteur lit la carte et les livres d'Emma."""
    S = Scene()
    salle(S, 600, graine=6)
    S.add(comptoir(400, 800, 1.2))
    S.add(lecteur(400, 800 - 200 * 1.2 - 14, 1.3))
    S.add(livre(240, 520, 0.9, "#51cf66", titre=dino(4, -18, 0.6)), livre(310, 520, 0.9, "#4dabf7", rot=6), livre(580, 530, 0.9, "#fcc419", rot=-6))
    S.add(carte_biblio(400, 470, 1.1))
    S.add(texte(400, 300, "Bip !", 70, "#fa5252", contour="#fff"))
    S.camera(1.2, 400, 480)
    return S


def p08():
    """Plan moyen : l'hôpital des livres ; Monsieur Ali répare une page déchirée."""
    S = Scene()
    salle(S, 600, graine=7)
    S.add(table(400, 790, 420, 150, "#c68642"))
    S.add(ali(400, 640, 1.2, expr="concentre", bras="porte", regard=(0, 0.6)))
    S.add(livre(400, 610, 1.0, "#cc5de8", ouvert=True))
    S.add(trait(360, 580, 380, 640, "#fa5252", 2), rect(350, 595, 60, 14, "#e7f5ff", opacity=0.8, rx=2))
    S.add(rect(520, 610, 50, 30, "#74c0fc", rx=6), cercle(545, 625, 10, "#e7f5ff"))
    S.add(emma(660, 790, 1.25, expr="content", bras="mains_jointes", regard=(-1, -0.3)))
    S.add(bulle(250, 130, 400, 100, "L'hôpital\ndes livres !", 36, pointe=(360, 380)))
    return S


def p09():
    """Plan large : le soir, des livres glissent dans la chute à livres ; Monsieur Ali les range sur son chariot."""
    S = Scene()
    facade(S, 640, nuit_=True)
    S.add(rect(600, 520, 110, 120, volume("#343a40", 0.3, 0.8), rx=8), rect(615, 540, 80, 16, "#212529", rx=4))
    S.add(texte(655, 600, "RETOUR", 20, "#fff"))
    S.add(livre(655, 500, 0.55, "#fa5252", rot=-70))
    S.add(personne(520, 790, 1.15, stature="adulte", peau="foncee", cheveux="noir", coiffure="chignon", habit="#e8590c", expr="content",
                   bras="tient", regard=(1, -0.3), objet=livre(*ancre(70, -150, "tient", "adulte"), 0.6, "#4dabf7")))
    S.add(ali(230, 790, 1.15, expr="content", bras="pousse", regard=(1, 0)))
    S.add(chariot(350, 790, 0.7))
    S.lumiere(400, 520, 110, "#ffd43b", 0.5)
    return S


def p10():
    """Plan moyen : le soir, Emma lit au lit avec ses trois livres."""
    S = Scene()
    piece(S, "chambre", 600)
    S.ambiance("nuit")
    S.add(fenetre(80, 90, 170, 160, "#1c2a52", nuit_=True, rideaux="#f06595"))
    S.add(lit(420, 790, 520, couverture="#f06595"))
    S.add(emma(380, 700, 1.0, expr="content", bras="porte", regard=(0, 0.5), objet=livre(0, -80, 0.6, "#51cf66", ouvert=True)))
    S.add(rect(240, 690, 460, 90, lineaire([(0, "#f783ac"), (1, "#d6336c")]), rx=18))
    S.add(lampe(720, 600, 0.75))
    S.add(livre(600, 560, 0.5, "#4dabf7", rot=10), livre(650, 560, 0.5, "#fcc419", rot=-8))
    S.add(texte(540, 170, "Encore un !", 44, "#fff3bf", contour="#5f3dc4"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("livres-seuls.svg", vignette),
    ("01-la-bibliotheque.svg", p01), ("02-ma-carte.svg", p02), ("03-les-rayons.svg", p03),
    ("04-la-cote.svg", p04), ("05-l-escabeau.svg", p05), ("06-l-heure-du-conte.svg", p06),
    ("07-bip.svg", p07), ("08-l-hopital-des-livres.svg", p08), ("09-la-chute-a-livres.svg", p09),
    ("10-au-lit.svg", p10),
]
