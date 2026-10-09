"""Le bouquet de maman — une surprise qui ne se passe pas comme prévu.

Pour la fête des mères, Zoé et Papa préparent en secret le petit déjeuner
au lit. Zoé cueille un bouquet : une marguerite, un coquelicot, un bleuet…
mais Biscotte le chien l'attrape et s'enfuit ! Après une grande course
dans le jardin, il ne rend qu'une fleur toute mâchouillée. Alors Zoé
dessine la famille, et Maman reçoit le plus beau bouquet du monde : il y a
même un peu de Biscotte dedans.

Plans : 1 moyen (chut !) · 2 large (la cueillette) · 3 moyen (le vol) ·
4 large en diagonale (la course) · 5 moyen (la fleur mâchouillée) · 6 gros
plan (le câlin de Papa) · 7 moyen (le dessin) · 8 moyen (sur la pointe des
pieds) · 9 large (surprise !) · 10 gros plan (le rire de Maman) · 11 large
(le câlin).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from objets import assiette, tasse
from fetes import chien_profil

ID = "mamans-bouquet"
PAPIER_PEINT = "fleurs"

ZOE = dict(peau="claire", cheveux="blond", coiffure="tresses", habit="#40c057", robe=True, nez="retrousse", taches=True)
PAPA = dict(peau="claire", cheveux="chatain", coiffure="courts", habit="#4c6ef5", robe=False, jambes="#343a40",
            stature="adulte", carrure="normale", nez="pointu", acc=("lunettes",))
MAMAN = dict(peau="claire", cheveux="blond", coiffure="longs", habit="#f783ac", stature="adulte", carrure="fine",
             yeux="cils", nez="petit")
BISCOTTE = dict(couleur="#e3b57a", oreille="#8d5524")


def zoe(x, y, s=1.35, **k):
    return personne(x, y, s, **{**ZOE, **k})


def papa(x, y, s=1.35, **k):
    return personne(x, y, s, **{**PAPA, **k})


def maman(x, y, s=1.35, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def biscotte(x, y, s=0.9, **k):
    return chien_profil(x, y, s, **{**BISCOTTE, **k})


def marguerite(x, y, s=1.0, tige=80, rot=0):
    m = [trait(0, 0, 0, -tige, "#2f9e44", 4)]
    for k in range(10):
        a = k * 36
        m.append(place(ellipse(0, -13, 4.5, 12, "#fff"), 0, -tige, 1.0, rot=a))
    m.append(cercle(0, -tige, 7, "#fcc419"))
    return place(m, x, y, s, rot=rot)


def coquelicot(x, y, s=1.0, tige=80, rot=0):
    m = [trait(0, 0, 0, -tige, "#2f9e44", 4),
         cercle(-8, -tige, 12, "#e03131"), cercle(8, -tige, 12, "#e03131"), cercle(0, -tige - 8, 12, "#fa5252"),
         cercle(0, -tige, 5, "#212529")]
    return place(m, x, y, s, rot=rot)


def bleuet(x, y, s=1.0, tige=80, rot=0):
    m = [trait(0, 0, 0, -tige, "#2f9e44", 4)]
    for k in range(8):
        a = math.radians(k * 45)
        m.append(poly([(0, -tige), (14 * math.cos(a - 0.3), -tige + 14 * math.sin(a - 0.3)),
                       (16 * math.cos(a), -tige + 16 * math.sin(a)), (14 * math.cos(a + 0.3), -tige + 14 * math.sin(a + 0.3))], "#4263eb"))
    m.append(cercle(0, -tige, 5, "#364fc7"))
    return place(m, x, y, s, rot=rot)


def bouquet(x, y, s=1.0, rot=0):
    """Petit bouquet noué d'un ruban ; (x, y) = le bas des tiges."""
    m = [marguerite(-10, 0, 1.0, 90, rot=-14), coquelicot(0, 0, 1.0, 100), bleuet(12, 0, 1.0, 88, rot=14),
         marguerite(18, 0, 0.9, 80, rot=24), coquelicot(-18, 0, 0.9, 82, rot=-26),
         rect(-14, -36, 28, 12, "#f783ac", rx=4)]
    return place(m, x, y, s, rot=rot)


def fleur_machee(x, y, s=1.0, rot=0):
    """Une seule fleur, la tige tordue, les pétales en désordre."""
    m = [chemin("M 0 0 Q 10 -30 -6 -50 Q -20 -70 2 -86", stroke="#2f9e44", sw=4),
         cercle(-6, -88, 11, "#e03131"), cercle(10, -92, 9, "#fa5252"), ellipse(-14, -98, 6, 9, "#e03131", rot=-30),
         cercle(0, -90, 4, "#212529"), ellipse(18, -60, 6, 3, "#2f9e44", rot=30)]
    return place(m, x, y, s, rot=rot)


def dessin_famille(x, y, s=1.0, rot=0):
    """Le dessin de Zoé : Maman, Papa, Zoé, Biscotte et des cœurs ; (x, y) = centre."""
    m = [rect(-150, -100, 300, 200, "#fff", rx=4, stroke="#dee2e6", stroke_width=3),
         texte(0, -62, "Bonne fête, Maman !", 24, "#e64980")]
    for k, (px, c, h) in enumerate(((-100, "#f783ac", 1.0), (-40, "#4c6ef5", 1.05), (20, "#40c057", 0.75))):
        m += [cercle(px, -20 + (1 - h) * 50, 13, "#ffe3c4", stroke="#495057", stroke_width=2),
              poly([(px - 14, 50), (px, -6 + (1 - h) * 50), (px + 14, 50)], c),
              trait(px - 6, 50, px - 8, 76, "#495057", 3), trait(px + 6, 50, px + 8, 76, "#495057", 3)]
    m += [ellipse(90, 50, 30, 14, "#e3b57a"), cercle(118, 36, 12, "#e3b57a"), trait(64, 46, 52, 30, "#e3b57a", 4),
          coeur(80, -10, 0.6, "#fa5252"), coeur(120, -30, 0.45, "#f783ac")]
    return place(m, x, y, s, rot=rot)


def plateau(x, y, s=1.0):
    """Le plateau du petit déjeuner ; (x, y) = milieu du plateau."""
    m = [rect(-120, -10, 240, 20, "#c68642", rx=6),
         assiette(-60, -10, 1.1, bord="#f783ac"),
         rect(-84, -34, 48, 18, "#f6c453", rx=6), rect(-80, -40, 40, 8, "#e9b98a", rx=4),
         rect(10, -60, 34, 50, "#ffd43b", rx=4, opacity=0.9), rect(10, -60, 34, 10, "#fff", opacity=0.5),
         rect(60, -54, 28, 44, "#e7f5ff", rx=4, opacity=0.8), fleur_machee(74, -30, 0.8)]
    return place(m, x, y, s)


def jardin(S, sol_y=650):
    ciel(S, "#74c0fc", "#fff9db")
    S.add(nuage(160, 120, 0.7), nuage(620, 90, 0.5))
    collines(S, 580, "#b2f2bb", graine=6)
    sol(S, sol_y, "#8ce99a")


def pre_fleuri(S, y0=660, y1=790, nb=26, graine=3):
    import random
    r = random.Random(graine)
    for k in range(nb):
        x, y = r.uniform(20, 780), r.uniform(y0, y1)
        f = (marguerite, coquelicot, bleuet)[k % 3]
        S.add(f(x, y, 0.5 + 0.4 * (y - y0) / (y1 - y0), tige=60))


def balancoire(x, y, s=1.0):
    return place([trait(-110, 0, -80, -300, "#8d5524", 12), trait(110, 0, 80, -300, "#8d5524", 12),
                  trait(-100, -300, 100, -300, "#8d5524", 14), trait(-40, -300, -40, -90, "#868e96", 3),
                  trait(40, -300, 40, -90, "#868e96", 3), rect(-50, -94, 100, 12, "#e03131", rx=4)], x, y, s)


def chambre_parents(S, y=600):
    interieur(S, "#fff5f5", "#d9a066", y, papier="#ffc9c9")
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#f783ac", contenu=soleil(700, 140, 22, rayons=False)))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S)
    pre_fleuri(S, 680, 790, 18, graine=7)
    S.add(arbre(130, 650, 1.0, feuillage="#ffdeeb", feuillage2="#fcc2d7"))
    S.add(zoe(380, 770, 1.6, expr="rire", bras="haut", regard=(1, 0), objet=place(bouquet(0, 0, 1.0), 0, -170)))
    S.add(biscotte(620, 780, 1.05, flip=True, expr="content"))
    for k, (x, y) in enumerate(((560, 300), (650, 230), (250, 260))):
        S.add(coeur(x, y, 0.9, ("#fa5252", "#f783ac", "#e64980")[k], rot=(-1) ** k * 12))
    S.cachette(70, 620, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(170, 130, 60, 120, "#e7f5ff", rx=8, opacity=0.9))
    S.add(fleur_machee(200, 190, 1.4))
    S.add(dessin_famille(310, 190, 0.4, rot=8))
    return S


def p01():
    """Plan moyen : dimanche matin, « Chut ! On prépare une surprise. »"""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(fenetre(80, 100, 170, 150, "#ffe8cc", rideaux="#f783ac", contenu=soleil(150, 230, 30, rayons=False)))
    S.add(horloge(620, 160, 44, 7, 30))
    S.add(papa(530, 770, 1.4, expr="malin", bras="chut", regard=(-1, 0.3)))
    S.add(zoe(300, 780, 1.35, expr="malin", bras="chut", regard=(1, -0.3)))
    S.add(biscotte(120, 780, 0.75, expr="content"))
    S.add(texte(410, 300, "Chut !", 72, "#e64980", contour="#fff", rot=-6))
    return S


def p02():
    """Plan large : la cueillette — une marguerite, un coquelicot, un bleuet."""
    S = Scene()
    jardin(S)
    pre_fleuri(S)
    S.add(zoe(400, 760, 1.25, expr="content", bras="porte", regard=(1, 0.3), objet=place(bouquet(0, 0, 0.9), 0, -60)))
    S.add(marguerite(560, 770, 2.0, tige=90), coquelicot(650, 760, 2.0, tige=100), bleuet(740, 770, 2.0, tige=90))
    S.add(texte(560, 520, "une…", 34, "#495057"), texte(650, 480, "deux…", 34, "#e03131"), texte(740, 520, "trois !", 34, "#4263eb"))
    S.add(biscotte(170, 770, 0.8, expr="content"))
    return S


def p03():
    """Plan moyen : Biscotte attrape le bouquet et s'enfuit."""
    S = Scene()
    jardin(S)
    pre_fleuri(S, 690, 790, 14, graine=5)
    S.add(zoe(230, 770, 1.45, expr="surpris", bras="tend", regard=(1, 0)))
    S.add(biscotte(560, 760, 1.25, course=True, gueule=place(bouquet(0, 0, 0.7), 0, 0, 1.0, rot=80)))
    S.add(mouvement(430, 640, 1.2), mouvement(430, 700, 1.0))
    S.add(bulle(260, 170, 360, 100, "Biscotte,\nrends-moi ça !", 36, pointe=(240, 400)))
    return S


def p04():
    """Plan large en diagonale : la course autour du cerisier et de la balançoire."""
    S = Scene()
    jardin(S)
    S.add(arbre(560, 640, 1.2, feuillage="#ffdeeb", feuillage2="#fcc2d7"))
    S.add(balancoire(180, 650, 0.9))
    S.add(chemin("M 80 780 Q 300 640 520 700 Q 700 760 760 680", stroke="#fff", sw=6, opacity=0.6, stroke_dasharray="14 14"))
    S.add(biscotte(640, 720, 0.85, course=True, gueule=place(bouquet(0, 0, 0.6), 0, 0, 1.0, rot=80)))
    S.add(zoe(330, 760, 1.15, expr="joie", bras="court", regard=(1, 0)))
    S.add(texte(400, 300, "Autour du cerisier…", 34, "#e64980", contour="#fff", rot=-4))
    S.add(texte(250, 380, "sous la balançoire…", 30, "#4263eb", contour="#fff", rot=-4))
    S.cachette(760, 780)
    return S


def p05():
    """Plan moyen : Biscotte rend une seule fleur, toute mâchouillée."""
    S = Scene()
    jardin(S)
    S.add(zoe(300, 780, 1.75, expr="triste", bras="porte", regard=(1, 0.5), objet=fleur_machee(8, -26, 0.95, rot=8)))
    S.add(biscotte(560, 770, 1.1, flip=True, expr="content", queue_haute=True))
    for x, y, r in ((620, 700, 20), (680, 730, -40), (520, 760, 60)):
        S.add(ellipse(x, y, 7, 4, "#fff", rot=r), ellipse(x + 14, y - 6, 6, 4, "#e03131", rot=r))
    S.cachette(760, 780)
    return S


def p06():
    """Gros plan : Papa console Zoé. « Une fleur, c'est déjà un bouquet. »"""
    S = Scene()
    jardin(S)
    S.add(papa(500, 900, 1.9, expr="sourire", bras="epaule", flip=True, regard=(-1, 0.3)))
    S.add(zoe(330, 900, 1.9, expr="triste", bras="porte", regard=(1, -0.3), objet=fleur_machee(0, -50, 1.0)))
    S.camera(1.25, 420, 470)
    S.dessus(bulle(560, 100, 400, 110, "Une fleur, c'est déjà\nun bouquet !", 32, pointe=S.vers_page(530, 330)))
    S.cachette(130, 740)
    return S


def p07():
    """Plan moyen : Zoé dessine toute la famille."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(fenetre(330, 90, 170, 150, "#a5d8ff", rideaux="#f783ac"))
    S.add(horloge(650, 150, 40, 8, 0))
    S.add(papa(620, 700, 1.4, expr="content", bras="mains_jointes", regard=(-1, 0.5)))
    S.add(zoe(260, 700, 1.4, expr="concentre", bras="porte", regard=(1, 1)))
    S.add(table(420, 800, 640, 140, "#c68642", nappe="#fff9db"))
    S.add(dessin_famille(420, 600, 0.95, rot=-3))
    for k, c in enumerate(("#fa5252", "#4c6ef5", "#40c057", "#fab005")):
        S.add(rect(150 + k * 26, 640, 12, 70, c, rx=4, transform=f"rotate({-30 + k * 12} {156 + k * 26} {675})"))
    S.add(biscotte(720, 790, 0.6, flip=True))
    return S


def p08():
    """Plan moyen : sur la pointe des pieds, avec le plateau."""
    S = Scene()
    interieur(S, "#fff5f5", "#d9a066", 600, papier="#ffc9c9")
    S.add(porte(620, 600, 160, 330, "#b5835a"))
    S.add(cadre_mur(120, 150, 120, 100, "#a5d8ff"))
    S.add(papa(250, 770, 1.35, expr="malin", bras="porte", regard=(1, 0), pas="pointe",
               objet=plateau(*ancre(0, -74, "porte", "adulte"), 0.85)))
    S.add(zoe(440, 780, 1.3, expr="malin", bras="porte", regard=(1, 0), pas="pointe", objet=dessin_famille(0, -70, 0.35)))
    S.add(biscotte(120, 780, 0.7))
    S.add(texte(420, 330, "chut… chut…", 44, "#e64980", rot=-6))
    S.cachette(760, 700)
    return S


def p09():
    """Plan large : « SURPRISE ! » Maman ouvre les yeux, Biscotte saute sur le lit."""
    S = Scene()
    chambre_parents(S)
    S.add(lit(420, 790, 480, "#fff5f5", "#f783ac"))
    S.add(maman(260, 690, 1.25, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(rect(270, 650, 380, 90, lineaire([(0, "#faa2c1"), (1, "#f783ac")]), rx=20))
    S.add(biscotte(470, 640, 0.8, flip=True, course=True))
    S.add(papa(660, 790, 1.3, expr="rire", bras="porte", regard=(-1, 0), objet=plateau(*ancre(0, -74, "porte", "adulte"), 0.85)))
    S.add(zoe(110, 790, 1.2, expr="rire", bras="haut", regard=(1, 0)))
    S.add(texte(420, 230, "SURPRISE !", 76, "#e64980", contour="#fff", rot=-4))
    return S


def p10():
    """Gros plan : Maman tient la fleur mâchouillée et rit aux larmes."""
    S = Scene()
    chambre_parents(S)
    S.add(lit(400, 900, 700, "#fff5f5", "#f783ac"))
    S.add(maman(400, 860, 1.9, expr="rire", bras="porte", regard=(0, 0), objet=fleur_machee(30, -40, 1.05, rot=20)))
    S.add(dessin_famille(640, 700, 0.6, rot=10))
    S.add(biscotte(150, 760, 0.9))
    S.camera(1.2, 400, 480)
    S.dessus(bulle(400, 90, 640, 110, "C'est le plus beau bouquet du monde :\nil y a même un peu de Biscotte dedans !", 28))
    S.cachette(720, 400, "air")
    return S


def p11():
    """Plan large : le grand câlin, tous ensemble dans le lit."""
    S = Scene()
    chambre_parents(S)
    S.add(cadre_mur(100, 140, 140, 110, "#fff"))
    S.add(dessin_famille(170, 195, 0.36))
    S.add(lit(420, 790, 520, "#fff5f5", "#f783ac"))
    S.add(papa(520, 690, 1.15, expr="rire", bras="calin", regard=(-1, 0)))
    S.add(maman(300, 690, 1.15, expr="rire", bras="calin", regard=(1, 0)))
    S.add(zoe(410, 700, 1.05, expr="rire", bras="calin"))
    S.add(rect(220, 650, 440, 90, lineaire([(0, "#faa2c1"), (1, "#f783ac")]), rx=20))
    S.add(biscotte(640, 660, 0.6, flip=True))
    for x, y in ((330, 330), (420, 300), (510, 330)):
        S.add(coeur(x, y, 0.8, "#fa5252"))
    S.cachette(760, 760)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fleur-seule.svg", vignette),
    ("01-chut.svg", p01), ("02-la-cueillette.svg", p02), ("03-biscotte.svg", p03),
    ("04-la-course.svg", p04), ("05-une-seule-fleur.svg", p05), ("06-papa-console.svg", p06),
    ("07-le-dessin.svg", p07), ("08-sur-la-pointe-des-pieds.svg", p08), ("09-surprise.svg", p09),
    ("10-le-plus-beau-bouquet.svg", p10), ("11-le-calin.svg", p11),
]
