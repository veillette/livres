"""La citrouille d'Halloween — avoir un peu peur du noir, et y aller quand même.

Tao le chaton creuse sa première citrouille avec Maman. Le soir
d'Halloween, déguisé en chauve-souris, il part frapper aux portes avec son
amie Zoé : « Des bonbons ou un sort ! » Chaque frayeur cache un ami — une
ombre géante (Pic le hérisson et sa lampe), un fantôme à la fenêtre (Papi
Renard sous un drap)… et la citrouille qui sourit lui donne du courage.

Plans : 1 moyen (creuser) · 2 gros plan (la citrouille s'allume) · 3 moyen
(sur le seuil) · 4 large (l'ombre géante) · 5 moyen (ce n'est que Pic) ·
6 moyen (chez Madame Chouette) · 7 contre-plongée (la vieille maison) ·
8 gros plan (courage) · 9 moyen (le fantôme ouvre) · 10 moyen (la soupe) ·
11 large (le retour).
"""
from base import *
from base import _assombrir
from objets import lampe_poche, bol
from fetes import (citrouille_creusee, citrouille_anse, seau_bonbons, bonbon, chauve_souris_papier,
                   ailes_chauve_souris, chapeau_sorciere, drap_fantome, guirlande_lumineuse)

ID = "halloween-citrouille"
PAPIER_PEINT = "losanges"

TAO = dict(habit="#5f3dc4", derriere=ailes_chauve_souris("#5f3dc4"))
TAO_MAISON = dict(habit="#ffd43b", motif="rayures", couleur_motif="#fab005")
MAMAN = dict(couleur="#e8a35c", habit="#1098ad", acc=("tablier",))
ZOE = dict(habit="#2b2b3a")
PIC = dict(habit="#2f9e44")
PAPI = dict(couleur="#d9692b", habit="#e8590c", acc=("lunettes",))
CHEMIN_Y = 640


def tao(x, y, s=1.25, costume=True, **k):
    return perso("chat", x, y, s, **{**(TAO if costume else TAO_MAISON), **k})


def maman(x, y, s=1.6, **k):
    return perso("chat", x, y, s, **{**MAMAN, **k})


def zoe(x, y, s=1.25, **k):
    k.setdefault("objet", None)
    m = perso("renard", x, y, s, **{**ZOE, **k})
    return g([m, place(chapeau_sorciere("#2b2b3a", "#ae3ec9"), x, y + 18 * s, s)])


def pic(x, y, s=0.9, **k):
    return perso("herisson", x, y, s, **{**PIC, **k})


def papi(x, y, s=1.6, **k):
    return perso("renard", x, y, s, **{**PAPI, **k})


def porte_citrouille(S, x, y, s, qui, flip=False, **k):
    """Un personnage qui porte sa citrouille-lanterne par l'anse (et son halo)."""
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=citrouille_anse(68, -146, 0.5), **k))
    S.lumiere(x + (-68 if flip else 68) * s, y - (146 - 46) * s, 90 * s, "#ff922b", 0.6)


def rue_nuit(S, sol_y=CHEMIN_Y, lune_=(650, 120), graine=5):
    nuit(S, "#1a1238", "#4b2f7a")
    etoiles(S, 34, graine, (0, 0, 800, sol_y - 220))
    if lune_:
        S.add(lune(*lune_, 50))
    sol(S, sol_y, "#4a3f6b", bosse=10)


def lampadaire(x, y, s=1.0):
    """Réverbère allumé ; halo à poser avec S.lumiere(x, y - 300 s)."""
    m = [rect(-7, -290, 14, 290, "#343a40", rx=4), rect(-22, -6, 44, 10, "#343a40", rx=3),
         poly([(-26, -300), (26, -300), (18, -330), (-18, -330)], "#343a40"),
         rect(-18, -300, 36, 26, "#ffe066"), poly([(-30, -330), (30, -330), (0, -350)], "#343a40")]
    return place(m, x, y, s)


def ombre_piquante(x, y, s=1.0, couleur="#120c2a"):
    """Silhouette énorme et hérissée, projetée sur un mur ; (x, y) = bas."""
    m = [ellipse(0, -150, 150, 150, couleur)]
    for k in range(13):
        a = math.radians(180 + k * 15)
        bx, by = 140 * math.cos(a), -150 + 140 * math.sin(a)
        tx, ty = 230 * math.cos(a), -150 + 230 * math.sin(a)
        m.append(poly([(bx - 22 * math.sin(a), by + 22 * math.cos(a)), (tx, ty), (bx + 22 * math.sin(a), by - 22 * math.cos(a))], couleur))
    m += [ellipse(-50, -200, 22, 14, "#ffe066"), ellipse(50, -200, 22, 14, "#ffe066"),
          rect(-90, -20, 50, 30, couleur, rx=10), rect(40, -20, 50, 30, couleur, rx=10)]
    return place(m, x, y, s)


def mur_pierre(S, y0, y1, c="#6c5f8d"):
    S.add(rect(0, y0, 800, y1 - y0, c))
    S.add(pierres(0, y0, 800, y1 - y0, c, pas_=30, larg=60, opacite=0.4))


def vieille_maison(x, y, s=1.0, fantome=True):
    """Grande maison au bout du chemin, une fenêtre allumée où flotte un drap."""
    m = [rect(-180, -330, 360, 330, "#5f4b8b"), planches(-180, -330, 360, 330, "#5f4b8b", larg=26),
         poly([(-210, -330), (0, -500), (210, -330)], "#3b2a5e"),
         rect(120, -470, 34, 90, "#3b2a5e"),
         rect(-40, -130, 80, 130, "#2b1f45", rx=6), cercle(24, -66, 5, "#ffd43b")]
    for fx in (-130, 70):
        m.append(rect(fx, -270, 60, 70, "#2b1f45"))
    m.append(rect(-40, -440, 80, 70, "#ffe066"))
    m.append(chemin("M -40 -405 H 40 M 0 -440 V -370", stroke="#3b2a5e", sw=5))
    if fantome:
        m.append(chemin("M -26 -372 Q -30 -430 0 -436 Q 30 -430 26 -372 L 14 -380 L 4 -372 L -6 -380 L -16 -372 Z", "#f8f9fa"))
        m += [ellipse(-9, -414, 4, 6, "#2b2b3a"), ellipse(9, -414, 4, 6, "#2b2b3a"), ellipse(0, -398, 5, 6, "#2b2b3a")]
    return place(m, x, y, s)


def cuisine_soir(S, y=600):
    piece(S, "cuisine", y)
    S.add(fenetre(560, 90, 170, 150, "#1a1238", nuit_=True, rideaux="#e8590c"))
    S.add(lampe(120, y - 20, 1.0))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_nuit(S, 650, lune_=(620, 140))
    S.add(maison(130, 650, 0.9, mur="#8c7ab8", toit="#3b2a5e", lumiere=True, cheminee=False))
    S.add(citrouille_creusee(250, 690, 0.55), citrouille_creusee(70, 700, 0.45))
    S.lumiere(250, 655, 70, "#ff922b", 0.6)
    S.lumiere(70, 670, 60, "#ff922b", 0.6)
    S.add(chauve_souris_papier(330, 220, 1.1, rot=-10), chauve_souris_papier(470, 160, 0.8, rot=12))
    porte_citrouille(S, 400, 770, 1.6, tao, expr="rire", regard=(1, 0))
    S.add(zoe(620, 770, 1.35, expr="malin", bras="tient", regard=(-1, 0), objet=seau_bonbons(68, -146, 0.9)))
    S.cachette(730, 410, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 175, 110, radial([(0, "#ffe066", 0.6), (1, "#ffe066", 0)])))
    S.add(citrouille_creusee(200, 262, 1.6))
    return S


def p01():
    """Plan moyen : Tao et Maman creusent la citrouille."""
    S = Scene()
    cuisine_soir(S)
    S.add(maman(560, 690, 1.55, expr="sourire", bras="porte", regard=(-1, 0.6), objet=_cuillere(30, -70)))
    S.add(table(400, 790, 520, 170, "#c68642", nappe="#fff4e6"))
    S.add(citrouille_creusee(400, 610, 1.15, allumee=False))
    S.add(bol(560, 610, 0.9, "#ffa94d", "#ff922b"))
    S.add(tao(220, 700, 1.25, costume=False, expr="concentre", bras="tient", regard=(1, 0.5), objet=_cuillere(68, -146)))
    S.add(texte(400, 300, "Scritch, scratch !", 54, "#e8590c", contour="#fff", rot=-6))
    return S


def _cuillere(x, y):
    return place([rect(-5, -10, 10, 70, "#adb5bd", rx=4), ellipse(0, -18, 16, 22, "#ced4da")], x, y, 1.0, rot=-20)


def p02():
    """Gros plan : la citrouille s'allume et sourit."""
    S = Scene()
    cuisine_soir(S)
    S.add(table(400, 900, 760, 260, "#c68642", nappe="#fff4e6"))
    S.add(citrouille_creusee(400, 660, 2.1))
    S.lumiere(400, 540, 300, "#ff922b", 0.75)
    S.add(tao(150, 740, 1.4, costume=False, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(maman(680, 760, 1.6, expr="content", bras="mains_jointes", regard=(-1, 0)))
    S.camera(1.2, 400, 480)
    S.cachette(700, 330, "air")
    return S


def p03():
    """Plan moyen : sur le seuil, Tao hésite ; Zoé l'attend dehors."""
    S = Scene()
    rue_nuit(S, 650)
    S.add(maison(600, 650, 1.0, mur="#8c7ab8", toit="#3b2a5e", lumiere=True))
    # la porte ouverte de chez Tao, à gauche, et sa lumière
    S.add(rect(0, 120, 300, 560, "#e7dcc8"), rect(40, 200, 200, 480, "#ffe8a3"))
    S.add(rect(30, 190, 220, 10, "#8d5524"), rect(30, 190, 10, 490, "#8d5524"), rect(240, 190, 10, 490, "#8d5524"))
    S.lumiere(140, 450, 220, "#ffd43b", 0.55)
    porte_citrouille(S, 150, 690, 1.25, tao, expr="inquiet", regard=(1, 0))
    S.add(zoe(470, 760, 1.25, expr="rire", bras="coucou", regard=(-1, 0)))
    S.add(texte(160, 330, "Gloups…", 40, "#5f3dc4", contour="#fff"))
    S.add(bulle(560, 170, 260, 90, "On y va ?", 38, pointe=(500, 470)))
    S.cachette(740, 720)
    return S


def p04():
    """Plan large : une ombre immense glisse sur le mur."""
    S = Scene()
    rue_nuit(S, 680, lune_=(110, 100))
    mur_pierre(S, 260, 690)
    S.add(ombre_piquante(470, 640, 1.25, "#1a1238"))
    S.add(lampadaire(80, 700, 1.4))
    S.lumiere(80, 260, 160, "#ffe066", 0.6)
    porte_citrouille(S, 300, 780, 1.0, tao, expr="surpris", regard=(1, -0.5))
    S.add(zoe(180, 785, 1.0, expr="inquiet", bras="joues", regard=(1, -0.5)))
    S.add(bulle(640, 140, 260, 80, "Qui est là ?", 36))
    S.cachette(740, 760)
    return S


def p05():
    """Plan moyen : ce n'est que Pic, avec sa lampe de poche."""
    S = Scene()
    rue_nuit(S, 680, lune_=(110, 100))
    mur_pierre(S, 260, 690)
    S.add(lampadaire(80, 700, 1.4))
    S.lumiere(80, 260, 160, "#ffe066", 0.6)
    S.add(pic(500, 770, 1.1, expr="rire", bras="tient", regard=(-1, 0), flip=True,
              objet=lampe_poche(66, -150, 0.9, rot=-120, faisceau=0)))
    S.lumiere(450, 610, 90, "#fff3bf", 0.6)
    porte_citrouille(S, 270, 780, 1.1, tao, expr="rire", regard=(1, 0))
    S.add(zoe(130, 785, 1.05, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(bulle(580, 150, 340, 100, "Je vous ai fait\npeur, hein ?", 34, pointe=(520, 440)))
    S.cachette(740, 760)
    return S


def p06():
    """Plan moyen : chez Madame Chouette, « Des bonbons ou un sort ! »"""
    S = Scene()
    rue_nuit(S, 660, lune_=None)
    S.add(rect(380, 140, 420, 540, "#7a6aa8"), planches(380, 140, 420, 540, "#7a6aa8", larg=30))
    S.add(rect(470, 260, 200, 420, "#ffe8a3"), rect(460, 250, 220, 12, "#3b2a5e"))
    S.add(guirlande_lumineuse(380, 220, 800, 220, creux=20, nb=8, couleurs=("#ff922b", "#cc5de8", "#ffd43b")))
    S.lumiere(570, 460, 200, "#ffd43b", 0.55)
    S.add(chouette(570, 680, 1.6, couleur="#a9805b", expr="rire", ailes="haut", acc=("lunettes",)))
    for k, c in enumerate(("#f06595", "#74c0fc", "#ffd43b", "#69db7c")):
        S.add(bonbon(500 + k * 46, 330 + (k % 2) * 30, 1.0, c, rot=k * 40))
    S.add(tao(270, 760, 1.2, expr="rire", bras="tend", regard=(1, 0), objet=seau_bonbons(96, -104, 0.9)))
    S.add(pic(130, 770, 0.9, expr="joie", bras="saute", regard=(1, 0)))
    S.add(zoe(390, 770, 1.15, expr="rire", bras="tient", regard=(1, -0.3), objet=seau_bonbons(68, -146, 0.8)))
    S.add(bulle(220, 160, 360, 100, "Des bonbons\nou un sort !", 36, pointe=(260, 440)))
    S.cachette(160, 70, "air")
    return S


def p07():
    """Contre-plongée : la vieille maison au bout du chemin, un fantôme à la fenêtre."""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a5e")
    etoiles(S, 40, 7, (0, 0, 800, 300))
    S.add(lune(150, 110, 60))
    S.add(gros_arbre_nu(80, 640, 1.2))
    S.add(chemin("M 0 800 L 0 640 Q 400 600 800 640 L 800 800 Z", terrain("#3b2f5a")))
    S.add(vieille_maison(470, 650, 1.15))
    S.lumiere(470, 160, 120, "#ffe066", 0.6)
    S.add(texte(650, 120, "Hou… hou…", 46, "#e9ecef", rot=8))
    S.add(chemin("M 360 800 Q 420 720 470 650", stroke="#5c4f7d", sw=60))
    porte_citrouille(S, 300, 830, 0.85, tao, expr="inquiet", regard=(1, -1))
    S.add(pic(180, 830, 0.7, expr="inquiet", bras="joues", regard=(1, -1)))
    S.add(zoe(620, 835, 0.85, expr="inquiet", bras="joues", regard=(-1, -1)))
    S.cachette(740, 760)
    return S


def gros_arbre_nu(x, y, s=1.0):
    c = "#2b1f45"
    m = [chemin("M -26 0 Q -20 -200 -10 -300 L 14 -300 Q 22 -200 30 0 Z", c),
         chemin("M 0 -240 Q 60 -300 120 -320", stroke=c, sw=16), chemin("M -6 -200 Q -60 -260 -110 -270", stroke=c, sw=14),
         chemin("M 4 -290 Q 10 -360 -20 -420", stroke=c, sw=12), chemin("M 80 -306 Q 110 -350 100 -380", stroke=c, sw=8)]
    return place(m, x, y, s)


def p08():
    """Gros plan : Tao serre sa citrouille qui sourit ; il prend son courage."""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a5e")
    etoiles(S, 30, 8, (0, 0, 800, 400))
    S.add(chemin("M 0 800 L 0 680 Q 400 650 800 680 L 800 800 Z", terrain("#3b2f5a")))
    porte_citrouille(S, 400, 820, 2.1, tao, expr="concentre", regard=(0, 0))
    S.camera(1.15, 400, 470)
    S.dessus(texte(400, 90, "Toc, toc.", 64, "#ffd43b", contour="#120c2a"))
    S.cachette(720, 760)
    return S


def p09():
    """Plan moyen : la porte s'ouvre… c'est Papi Renard sous un drap !"""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a5e")
    S.add(rect(0, 0, 800, 680, "#5f4b8b"), planches(0, 0, 800, 680, "#5f4b8b", larg=30))
    S.add(rect(300, 140, 280, 540, "#ffe8a3"), rect(290, 130, 300, 14, "#3b2a5e"))
    S.lumiere(440, 420, 240, "#ffd43b", 0.55)
    S.add(rect(0, 680, 800, 120, terrain("#3b2f5a")))
    S.add(drap_fantome(440, 680, 1.55, expr="rire"))
    S.add(chemin("M 500 660 Q 560 640 580 600", stroke="#f76707", sw=18))
    S.add(chemin("M 572 610 Q 586 590 582 576", stroke="#fff4e6", sw=14))
    porte_citrouille(S, 160, 780, 1.2, tao, expr="rire", regard=(1, -0.3))
    S.add(zoe(680, 780, 1.15, expr="rire", bras="applaudit", regard=(-1, -0.3)))
    S.add(pic(60, 790, 0.8, expr="rire", bras="haut", regard=(1, 0)))
    S.add(bulle(440, 70, 280, 80, "Hou ! Hou !", 40, pointe=(440, 290)))
    S.cachette(560, 730, "air")
    return S


def p10():
    """Plan moyen : la soupe au potiron, toute chaude, autour de la table."""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.add(guirlande_lumineuse(20, 80, 780, 80, creux=24, nb=12, couleurs=("#ff922b", "#cc5de8", "#ffd43b")))
    S.add(chauve_souris_papier(200, 200, 0.8), chauve_souris_papier(620, 180, 0.9, rot=10))
    S.add(papi(400, 680, 1.5, expr="rire", bras="ouverts", regard=(0, 0.3)))
    S.add(drap_plie(400, 470))
    S.add(table(400, 800, 640, 150, "#a0693a", nappe="#fff4e6"))
    S.add(_marmite(400, 640))
    S.lumiere(400, 560, 120, "#ff922b", 0.4)
    for k, (x, qui) in enumerate(((180, "tao"), (300, "pic"), (530, "zoe"))):
        S.add(bol(x, 646, 0.8, "#4dabf7", "#ff922b", cuillere=True))
    S.add(citrouille_creusee(660, 650, 0.6), citrouille_creusee(120, 650, 0.5))
    S.lumiere(660, 610, 70, "#ff922b", 0.6)
    S.lumiere(120, 615, 60, "#ff922b", 0.6)
    S.add(tao(200, 800, 1.0, expr="miam", bras="porte", regard=(1, -0.5)))
    S.add(pic(320, 805, 0.75, expr="rire", bras="applaudit", regard=(1, -0.5)))
    S.add(zoe(560, 800, 1.0, expr="miam", bras="porte", regard=(-1, -0.5)))
    return S


def drap_plie(x, y):
    return g([])


def _marmite(x, y):
    m = [ellipse(0, -60, 90, 18, "#ff922b"), rect(-90, -60, 180, 60, cylindre("#495057", 0.3, 0.7), rx=10),
         ellipse(0, -60, 90, 18, "none", stroke="#343a40", stroke_width=6)]
    for k in range(3):
        m.append(chemin(f"M {-40 + k * 40} -90 q 12 -20 0 -40 q -12 -20 0 -40", stroke="#fff", sw=5, opacity=0.6))
    return place(m, x, y)


def p11():
    """Plan large : le retour sous la lune ; la nuit ne fait plus peur."""
    S = Scene()
    rue_nuit(S, 640, lune_=(620, 140))
    S.add(maison(140, 640, 0.75, mur="#8c7ab8", toit="#3b2a5e", lumiere=True, cheminee=False))
    S.add(maison(690, 650, 0.6, mur="#a597c9", toit="#5f3dc4", lumiere=True))
    S.add(lampadaire(400, 650, 1.0))
    S.lumiere(400, 340, 120, "#ffe066", 0.55)
    S.add(chauve_souris_papier(300, 230, 0.7), chauve_souris_papier(520, 260, 0.6, rot=-12))
    porte_citrouille(S, 300, 770, 1.15, tao, expr="fier", regard=(1, 0))
    S.add(zoe(470, 775, 1.1, expr="rire", bras="tient", regard=(-1, 0), objet=seau_bonbons(68, -146, 0.8)))
    S.add(pic(600, 780, 0.85, expr="rire", bras="tient", regard=(-1, 0), objet=seau_bonbons(68, -146, 0.8)))
    S.add(bulle(250, 140, 400, 110, "L'an prochain, c'est moi\nqui ferai le fantôme !", 28, pointe=(290, 470)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("citrouille-seule.svg", vignette),
    ("01-creuser.svg", p01), ("02-elle-s-allume.svg", p02), ("03-sur-le-seuil.svg", p03),
    ("04-l-ombre.svg", p04), ("05-c-est-pic.svg", p05), ("06-des-bonbons.svg", p06),
    ("07-la-vieille-maison.svg", p07), ("08-toc-toc.svg", p08), ("09-le-fantome.svg", p09),
    ("10-la-soupe.svg", p10), ("11-le-retour.svg", p11),
]
