"""Où est passé mon dinosaure ? — Inès range sa chambre.

Dans la chambre d'Inès, c'est le grand bazar, et Dino, son dinosaure
préféré, a disparu. Ranger ? « C'est trop long ! » Maman a une idée : chaque
jouet a sa maison (la boîte bleue pour les cubes, la rouge pour les
voitures, le panier pour les peluches, l'étagère pour les livres), et on
range en chantant, plus vite que la chanson. Sous le lit : une chaussette,
un crayon… et Dino ! Dans la chambre rangée, il y a enfin de la place pour
construire un grand château. Le soir, chaque jouet dort dans sa maison.

Plans : 1 large (le bazar) · 2 moyen (où est Dino ?) · 3 moyen (c'est trop
long !) · 4 schéma (chaque jouet a sa maison) · 5 moyen (prêts ? partez !)
· 6 gros plan (clac, clac !) · 7 moyen (les livres) · 8 moyen (les
peluches) · 9 moyen (sous le lit) · 10 gros plan (te voilà !) · 11 large (de
la place pour jouer) · 12 moyen (bonne nuit).
"""
from base import *
from base import _assombrir
from objets import cube, chaussette
from animaux import etiquette
from fantastique import personne, mains_personne

ID = "ines-range"

INES = dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#9775fa", robe=False, jambes="#495057", taches=True)
MAMAN = dict(stature="adulte", peau="claire", cheveux="chatain", coiffure="carre", habit="#20c997", robe=False, jambes="#364fc7",
             nez="pointu", yeux="cils")
VERT_DINO = "#69db7c"
COULEURS = ("#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8", "#ff922b")


def ines(x, y, s=1.45, **k):
    return personne(x, y, s, **{**INES, **k})


def maman(x, y, s=1.75, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def dino(x, y, s=1.0, rot=0, flip=False, expr="content"):
    """Dino, le dinosaure en peluche (de profil, tête à droite) ; (x, y) = sous les pattes."""
    c = VERT_DINO
    m = [chemin("M -50 -40 Q -110 -30 -130 -6 Q -96 -14 -50 -16 Z", volume(c, 0.3, 0.8)),
         ellipse(-14, -26, 22, 24, _assombrir(c, 0.85)), ellipse(26, -26, 22, 24, _assombrir(c, 0.85)),
         ellipse(0, -46, 56, 38, volume(c, 0.3, 0.8)),
         ellipse(0, -36, 34, 22, "#d3f9d8")]
    for k in range(4):
        m.append(poly([(-40 + k * 22, -78 + abs(k - 1.5) * 4), (-30 + k * 22, -98 + abs(k - 1.5) * 4), (-20 + k * 22, -78 + abs(k - 1.5) * 4)], "#ffd43b"))
    m += [ellipse(-14, -4, 16, 8, _assombrir(c, 0.75)), ellipse(26, -4, 16, 8, _assombrir(c, 0.75)),
          chemin("M 34 -66 Q 40 -100 70 -102 Q 100 -100 98 -80 Q 96 -62 70 -62 Q 50 -60 46 -46 Z", volume(c, 0.3, 0.8)),
          cercle(72, -86, 7, "#fff"), cercle(74, -86, 4, ENCRE), chemin("M 76 -70 Q 86 -66 94 -72", stroke=ENCRE, sw=2.5),
          cercle(90, -82, 2, _assombrir(c, 0.6)), ellipse(40, -50, 8, 12, _assombrir(c, 0.85), rot=-20)]
    if expr == "dort":
        m[-7:-5] = [chemin("M 66 -86 q 6 5 12 0", stroke=ENCRE, sw=2.5)]
    return place(m, x, y, s, rot=rot, flip=flip)


def voiture(x, y, s=1.0, couleur="#fa5252", rot=0):
    m = [rect(-40, -34, 80, 24, volume(couleur, 0.3, 0.8), rx=8), chemin("M -24 -34 L -14 -52 L 16 -52 L 26 -34 Z", couleur),
         rect(-10, -48, 20, 12, "#d0ebff", rx=3), cercle(-24, -10, 10, "#343a40"), cercle(24, -10, 10, "#343a40"),
         cercle(-24, -10, 4, "#ced4da"), cercle(24, -10, 4, "#ced4da")]
    return place(m, x, y, s, rot=rot)


def livre_jouet(x, y, s=1.0, couleur="#4dabf7", rot=0):
    return place([rect(-36, -10, 72, 20, couleur, rx=3), rect(-36, -10, 72, 5, "#fff", opacity=0.5)], x, y, s, rot=rot)


def crayon(x, y, s=1.0, couleur="#fa5252", rot=0):
    return place([rect(-30, -5, 50, 10, couleur, rx=2), poly([(20, -5), (34, 0), (20, 5)], "#ffe8cc"), cercle(33, 0, 2, ENCRE)], x, y, s, rot=rot)


def peluche(x, y, s=1.0, espece="ours", couleur=None, expr="sourire"):
    return perso(espece, x, y, s, expr=expr, bras="bas", couleur=couleur)


def bac(x, y, s=1.0, couleur="#4dabf7", image=""):
    """Bac de rangement vu de face, avec son étiquette dessinée ; (x, y) = au sol."""
    m = [rect(-80, -110, 160, 110, volume(couleur, 0.3, 0.8), rx=10), rect(-84, -116, 168, 16, _assombrir(couleur, 0.85), rx=6),
         rect(-36, -86, 72, 56, "#fff", rx=6), image]
    return place(m, x, y, s)


def panier(x, y, s=1.0, contenu=""):
    m = [contenu, chemin("M -90 -100 L 90 -100 L 74 0 L -74 0 Z", volume("#e9c46a", 0.3, 0.8))]
    for k in range(-4, 5):
        m.append(trait(k * 20, -98, k * 17, -2, "#c9a24a", 2.5))
    m.append(rect(-94, -106, 188, 14, "#d4a73a", rx=6))
    return place(m, x, y, s)


def bazar(S, graine=1, nb=16, zone=(40, 640, 760, 790)):
    r = random.Random(graine)
    for k in range(nb):
        x, y = r.uniform(zone[0], zone[2]), r.uniform(zone[1], zone[3])
        quoi = k % 5
        if quoi == 0:
            S.add(cube(x, y, 0.6, COULEURS[k % 6], "ABCDEF"[k % 6], rot=r.uniform(-40, 40)))
        elif quoi == 1:
            S.add(voiture(x, y, 0.7, COULEURS[(k + 2) % 6], rot=r.uniform(-30, 30)))
        elif quoi == 2:
            S.add(livre_jouet(x, y, 0.9, COULEURS[(k + 4) % 6], rot=r.uniform(-40, 40)))
        elif quoi == 3:
            S.add(crayon(x, y, 1.0, COULEURS[(k + 1) % 6], rot=r.uniform(-90, 90)))
        else:
            S.add(cube(x, y, 0.55, COULEURS[(k + 3) % 6], "XYZ"[k % 3], rot=r.uniform(-40, 40)))


def chambre(S, nuit_=False):
    piece(S, "chambre", y=590)
    if nuit_:
        S.ambiance("nuit")
    S.add(fenetre(70, 90, 160, 150, "#364fc7" if nuit_ else "#a5d8ff", nuit_=nuit_, rideaux="#e5dbff"))
    S.add(etagere(620, 250, 220))
    S.add(lit(560, 760, 360, "#e5dbff", "#b197fc"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    chambre(S)
    bazar(S, 2, 12, zone=(40, 700, 760, 790))
    for x, y, r, k in ((150, 260, -30, 0), (650, 380, 20, 1), (220, 450, 40, 2), (560, 200, -20, 3)):
        S.add(cube(x, y, 0.7, COULEURS[k], "DINO"[k], rot=r))
    lx, ly, t = 380, 800, 1.75
    S.add(ines(lx, ly, t, expr="rire", bras="porte", regard=(0, -0.2), objet=place(dino(0, 0, 0.9), -10, -70)))
    S.cachette(200, 730, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(dino(200, 250, 1.6))
    return S


def p01():
    """Plan large : la chambre d'Inès est un grand bazar : cubes, voitures, livres et crayons partout."""
    S = Scene()
    chambre(S)
    S.add(ines(330, 800, 1.7, expr="bouche_bee", bras="ouverts", regard=(0, 0.4)))
    bazar(S, 1, 22)
    S.add(chaussette(700, 540, 0.7))
    S.add(texte(400, 120, "Quel bazar !", 56, "#7048e8", contour="#fff"))
    return S


def p02():
    """Plan moyen : Inès soulève sa couverture et cherche partout : « Où est passé mon dinosaure ? »"""
    S = Scene()
    chambre(S)
    bazar(S, 3, 14, zone=(40, 700, 400, 790))
    S.add(ines(420, 800, 1.7, expr="inquiet", bras="haut", regard=(1, 0.3)))
    for x, y in ((250, 330), (600, 300), (680, 420)):
        S.add(texte(x, y, "?", 64, "#7048e8", contour="#fff"))
    S.add(bulle(380, 140, 480, 90, "Où est passé mon dinosaure ?", 34, pointe=(400, 330)))
    return S


def p03():
    """Plan moyen : Maman, à la porte : « Et si on rangeait ensemble ? » ; Inès : « C'est trop long ! »"""
    S = Scene()
    chambre(S)
    S.add(porte(330, 590, 160, 320, "#b5835a", ouverte=True))
    S.add(maman(330, 800, 2.0, expr="content", bras="hanches", regard=(1, 0.3)))
    bazar(S, 4, 14, zone=(420, 700, 780, 790))
    S.add(ines(600, 800, 1.7, expr="fache", bras="croises", flip=True, regard=(-1, 0)))
    S.add(bulle(250, 150, 360, 110, "Et si on rangeait\nensemble ?", 32, pointe=(310, 300)))
    S.add(bulle(610, 330, 280, 80, "C'est trop long !", 32, pointe=(610, 430)))
    return S


def p04():
    """Schéma : chaque jouet a sa maison : la boîte bleue pour les cubes, la rouge pour les voitures, le panier pour les peluches, l'étagère pour les livres."""
    S = Scene()
    fond(S, "#f3f0ff")
    S.add(texte(400, 100, "Chaque jouet a sa maison", 44, "#7048e8"))
    S.add(bac(200, 420, 1.3, "#4dabf7", cube(0, -50, 0.45, "#ffd43b", "A")))
    S.add(etiquette(200, 470, "les cubes", 30, "#1c7ed6"))
    S.add(bac(600, 420, 1.3, "#fa5252", voiture(0, -40, 0.6, "#4dabf7")))
    S.add(etiquette(600, 470, "les voitures", 30, "#c92a2a"))
    S.add(panier(200, 720, 1.2, g([peluche(-30, -70, 0.3, "lapin"), peluche(30, -70, 0.3, "ours", "#ffa94d")])))
    S.add(etiquette(200, 770, "les peluches", 30, "#b08a20"))
    S.add(rect(470, 700, 260, 14, "#c68642", rx=4))
    for k, c in enumerate(COULEURS):
        S.add(rect(490 + k * 36, 600, 28, 100, volume(c, 0.3, 0.8), rx=3))
    S.add(etiquette(600, 770, "les livres", 30, "#8d5524"))
    S.cachette(740, 790)
    return S


def p05():
    """Plan moyen : Maman chante, Inès ramasse les cubes à toute vitesse : « Prêts ? Partez ! »"""
    S = Scene()
    chambre(S)
    bazar(S, 5, 10, zone=(340, 700, 780, 790))
    S.add(maman(150, 800, 2.0, expr="chante", bras="ouverts", regard=(1, 0)))
    S.add(notes(240, 300, 1.0, "#7048e8"))
    S.add(ines(480, 800, 1.7, expr="rire", bras="ramasse", regard=(0, 1), pas="marche"))
    S.add(texte(500, 160, "Prêts ? Partez !", 56, "#e8590c", contour="#fff"))
    return S


def p06():
    """Gros plan : un à un, les cubes sautent dans la boîte bleue : « Clac, clac, clac ! »"""
    S = Scene()
    chambre(S)
    S.add(bac(520, 840, 2.0, "#4dabf7", cube(0, -50, 0.45, "#ffd43b", "A")))
    for k, (x, y, r) in enumerate(((420, 470, -20), (500, 400, 15), (600, 450, 35))):
        S.add(cube(x, y, 0.8, COULEURS[k], "ABC"[k], rot=r))
    S.add(ines(220, 880, 1.8, expr="rire", bras="lance", regard=(1, -0.3)))
    S.camera(1.12, 400, 520)
    S.dessus(texte(560, 140, "Clac, clac, clac !", 52, "#1c7ed6", contour="#fff"))
    return S


def p07():
    """Plan moyen : Inès range les livres sur l'étagère, bien debout, les uns à côté des autres."""
    S = Scene()
    piece(S, "chambre", y=590)
    S.add(rect(380, 380, 360, 16, "#c68642", rx=4), rect(380, 230, 360, 16, "#c68642", rx=4))
    for k, c in enumerate(COULEURS + COULEURS[:3]):
        S.add(rect(400 + k * 36, 280, 30, 100, volume(c, 0.3, 0.8), rx=3))
    for k, c in enumerate(COULEURS[:4]):
        S.add(rect(400 + k * 36, 130, 30, 100, volume(c, 0.3, 0.8), rx=3))
    lx, ly, t = 280, 800, 1.7
    S.add(ines(lx, ly, t, expr="concentre", bras="tient", regard=(1, -0.5),
               objet=place(livre_jouet(0, 0, 1.0, "#cc5de8", rot=-80), 68, -150)))
    S.add(texte(560, 520, "Tout droits !", 44, "#7048e8", contour="#fff"))
    return S


def p08():
    """Plan moyen : Inès couche les peluches dans le panier : « Bonne nuit, Lapin ! »"""
    S = Scene()
    chambre(S)
    S.add(panier(520, 800, 1.6, g([peluche(-50, -60, 0.4, "lapin"), peluche(10, -70, 0.42, "ours", "#ffa94d"), peluche(60, -60, 0.36, "chat")])))
    S.add(ines(250, 800, 1.7, expr="content", bras="donne", regard=(1, 0.5)))
    S.add(bulle(330, 150, 330, 90, "Bonne nuit, Lapin !", 34, pointe=(300, 300)))
    return S


def p09():
    """Plan moyen : allongée par terre, Inès regarde sous le lit avec sa lampe : une chaussette, un crayon… et Dino !"""
    S = Scene()
    piece(S, "chambre", y=590)
    S.add(rect(240, 560, 520, 180, "#2b2b3a", opacity=0.75))
    S.add(lit(500, 740, 520, "#e5dbff", "#b197fc"))
    S.add(rect(240, 690, 520, 50, "#2b2b3a", opacity=0.75))
    S.add(chaussette(320, 712, 0.6), crayon(400, 724, 1.0, "#ffd43b", rot=10))
    S.add(dino(620, 736, 0.55))
    S.add(poly([(300, 716), (680, 680), (680, 760)], "#fff3bf", opacity=0.35))
    S.add(place(personne(0, 0, 1.0, expr="surpris", bras="tend", regard=(-1, 0), **INES), 20, 706, 1.3, rot=90))
    S.add(texte(500, 200, "Te voilà !", 60, "#7048e8", contour="#fff"))
    return S


def p10():
    """Gros plan : Inès serre Dino très fort dans ses bras : « Mon Dino ! »"""
    S = Scene()
    chambre(S)
    S.add(ines(400, 930, 2.3, expr="joie", bras="calin", regard=(0, 0), objet=place(dino(0, 0, 0.8), -6, -50)))
    S.add(coeur(220, 300, 1.2, "#ff8787"), coeur(600, 260, 0.9, "#ffa8a8"), coeur(640, 360, 0.6, "#ff8787"))
    S.add(texte(400, 120, "Mon Dino !", 64, "#2b8a3e", contour="#fff"))
    S.cachette(60, 790)
    return S


def p11():
    """Plan large : la chambre est rangée ; Inès et Maman construisent un grand château de cubes au milieu du tapis."""
    S = Scene()
    chambre(S)
    S.add(tapis(400, 740, 300, 56, "#fff3bf", "#ffd43b"))
    S.add(bac(110, 790, 0.8, "#4dabf7"), bac(250, 790, 0.7, "#fa5252"))
    for etage in range(4):
        for k in range(4 - etage):
            S.add(cube(340 + k * 52 + etage * 26, 730 - etage * 50, 0.6, COULEURS[(k + etage) % 6], ""))
    S.add(maman(660, 800, 2.0, expr="rire", bras="applaudit", flip=True, regard=(-1, 0.3)))
    S.add(ines(150, 800, 1.6, expr="rire", bras="donne", regard=(1, 0.3)))
    S.add(texte(400, 130, "De la place pour jouer !", 46, "#7048e8", contour="#fff"))
    return S


def p12():
    """Plan moyen : le soir, Inès dort avec Dino ; chaque jouet dort dans sa maison ; Maman éteint la lumière."""
    S = Scene()
    chambre(S, nuit_=True)
    S.add(bac(110, 790, 0.8, "#4dabf7"), bac(250, 790, 0.7, "#fa5252"))
    S.add(place(personne(0, 0, 1.0, expr="dort", bras="calin", **INES), 650, 600, 0.85, rot=-90))
    S.add(dino(500, 640, 0.4, rot=-10, expr="dort"))
    S.add(rect(480, 600, 250, 100, "#b197fc", rx=18))
    S.add(zzz(420, 450, 1.0))
    S.add(lampe(360, 800, 0.8))
    S.cachette(40, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("dino-seul.svg", vignette),
    ("01-quel-bazar.svg", p01), ("02-ou-est-dino.svg", p02), ("03-trop-long.svg", p03),
    ("04-chaque-jouet.svg", p04), ("05-partez.svg", p05), ("06-clac.svg", p06),
    ("07-les-livres.svg", p07), ("08-les-peluches.svg", p08), ("09-sous-le-lit.svg", p09),
    ("10-mon-dino.svg", p10), ("11-de-la-place.svg", p11), ("12-bonne-nuit.svg", p12),
]
