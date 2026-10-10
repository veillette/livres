"""L'autobus de Madame Nadia — une journée de chauffeuse d'autobus.

Au garage, Nadia vérifie son autobus ; à chaque arrêt, des passagers
montent (« Bonjour ! », bip de la carte) ; au volant, elle surveille ses
miroirs ; l'autobus s'abaisse et déroule sa rampe pour Jacques, en fauteuil
roulant ; Zack laisse sa place à une dame âgée ; au feu rouge, on s'arrête
même sous la pluie ; au terminus, Nadia trouve un doudou oublié et le rend
à sa propriétaire ; le soir, l'autobus passe au lavage.

Plans : 1 moyen (au garage) · 2 large (le premier arrêt) · 3 moyen (bip !)
· 4 gros plan (le volant, les miroirs) · 5 large (la rampe) · 6 moyen (la
place) · 7 large (le feu rouge sous la pluie) · 8 gros plan (le doudou) ·
9 moyen (« Mon doudou ! ») · 10 large (le lavage, le soir).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit, roue, casquette

ID = "autobus-nadia"

NADIA = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="carre", habit="#1971c2", jambes="#1c2a52",
             chaussures="#212529", nez="pointu", yeux="cils",
             tenue=g([rect(-30, -96, 20, 14, "none", rx=3, stroke="#fcc419", stroke_width=2.5), chemin("M -16 -107 L 0 -94 L 16 -107", stroke="#fff", sw=4)]))
ZACK = dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#fa5252", robe=False, jambes="#495057", nez="rond")
LILA = dict(stature="petit", peau="claire", cheveux="blond", coiffure="couettes", habit="#be4bdb", robe=True)
MAMAN_LILA = dict(stature="adulte", peau="claire", cheveux="blond", coiffure="longs", habit="#20c997", robe=True)
DAME = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chignon", habit="#e64980", acc=("lunettes",), carrure="ronde")
JACQUES = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#fd7e14", robe=False, jambes="#364fc7", barbe="#2b2b3a")

JAUNE_BUS = "#fab005"


def nadia(x, y, s=1.35, **k):
    return pro(x, y, s, **{**NADIA, **k})


def autobus(x, y, s=1.0, flip=False, numero="12", porte_ouverte=False, abaisse=False, rampe=False, phares=False):
    """Autobus de ville vu de côté, l'avant à droite ; (x, y) = au sol, sous le milieu."""
    dy = 10 if abaisse else 0
    c = "#1c7ed6"
    m = [ellipse(0, 6, 360, 16, "#000", opacity=0.14)]
    caisse = [rect(-340, -300, 680, 260, volume(c, 0.25, 0.8), rx=30),
              rect(-340, -110, 680, 34, "#fff"), rect(-340, -96, 680, 6, JAUNE_BUS),
              rect(-310, -280, 470, 120, "#1c2a52", rx=10)]
    for k in range(5):
        caisse.append(rect(-300 + k * 94, -272, 84, 104, "#a5d8ff", rx=6))
        caisse.append(poly([(-290 + k * 94, -168), (-260 + k * 94, -272), (-246 + k * 94, -272), (-276 + k * 94, -168)], "#fff", opacity=0.3))
    # pare-brise et girouette
    caisse += [chemin("M 200 -290 L 330 -290 Q 340 -290 340 -270 L 340 -160 L 200 -160 Z", "#a5d8ff"),
               rect(210, -290, 120, 30, "#212529", rx=4)]
    caisse.append(texte(270, -267, f"{numero} École", 22, "#ffd43b"))
    # portes : avant (droite) et milieu
    for px in (170, -30):
        if porte_ouverte and px == 170:
            caisse.append(rect(px - 40, -250, 80, 210, "#343a40", rx=4))
        else:
            caisse += [rect(px - 40, -250, 80, 210, "#a5d8ff", rx=4, stroke="#1864ab", stroke_width=4), trait(px, -250, px, -40, "#1864ab", 4)]
    if phares:
        caisse.append(cercle(336, -70, 12, "#fff3bf"))
    caisse += [rect(330, -80, 14, 20, "#fff3bf", rx=4), rect(-344, -80, 10, 24, "#fa5252", rx=3)]
    if rampe:
        caisse.append(poly([(130, -40), (210, -40), (250, 10), (90, 10)], "#868e96"))
    m.append(place(caisse, 0, dy))
    m += [roue(-220, -40, 46), roue(220, -40, 46)]
    return place(m, x, y, s, flip=flip) + occuper(x - 350 * s, y - 300 * s, x + 350 * s, y)


def fauteuil(x, y, s=1.0, flip=False):
    """Fauteuil roulant vu de côté ; (x, y) = au sol, sous le siège. Le personnage s'assoit sur le siège (y - 110 s)."""
    m = [cercle(-10, -60, 60, "none", stroke="#343a40", stroke_width=10), cercle(-10, -60, 52, "none", stroke="#adb5bd", stroke_width=3),
         trait(-10, -60, -10, -112, "#adb5bd", 3), trait(-52, -60, 32, -60, "#adb5bd", 3), cercle(-10, -60, 8, "#495057"),
         cercle(70, -14, 14, "#343a40"), trait(-60, -110, 60, -110, "#495057", 10), trait(-60, -110, -70, -200, "#495057", 10),
         trait(60, -110, 70, -30, "#495057", 6), trait(70, -30, 100, -30, "#495057", 6)]
    return place(m, x, y, s, flip=flip)


def jacques_fauteuil(x, y, s=1.0, flip=False, **k):
    """Jacques assis dans son fauteuil roulant (jambes pliées, de profil)."""
    sg = -1 if flip else 1
    corps = personne(0, 0, 1.0, expr=k.pop("expr", "content"), bras=k.pop("bras", "bas"), regard=k.pop("regard", (sg, 0)), **JACQUES)
    cid = uid("j")
    haut = el("clipPath", rect(-150, -400, 300, 340, "#000"), id=cid) + g(corps, clip_path=f"url(#{cid})")
    m = [fauteuil(0, 0, 1.0),
         place(haut, 0, -50, 0.9),
         rect(-30, -126, 100, 30, cylindre("#364fc7", 0.3, 0.7, vertical=True), rx=12),
         rect(56, -126, 26, 96, cylindre("#364fc7", 0.3, 0.7), rx=10), ellipse(84, -28, 22, 10, "#212529")]
    return place(m, x, y, s, flip=flip) + occuper(x - 90 * s, y - 330 * s, x + 110 * s, y)


def arret(x, y, s=1.0):
    """Poteau d'arrêt d'autobus."""
    return place([trait(0, 0, 0, -260, "#868e96", 8), rect(-50, -320, 100, 70, "#1c7ed6", rx=10),
                  texte(0, -296, "ARRÊT", 22, "#fff"), texte(0, -266, "12", 26, "#ffd43b")], x, y, s)


def rue_ville(S, y=640, pluie_=False, soir=False, graine=1):
    if pluie_:
        ciel(S, "#868e96", "#ced4da")
    elif soir:
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    for k, (bx, coul, toit) in enumerate(((10, "#ffd8a8", "mansarde"), (200, "#d3f9d8", "plat"), (420, "#e5dbff", "pignon"), (620, "#ffe3e3", "mansarde"))):
        S.add(immeuble(bx, y - 60, 170, 4, coul, toit, rdc="boutique" if k % 2 else "porte", graine=graine + k, lumiere=soir))
    S.add(rect(0, y - 60, 800, 40, "#ced4da"), rect(0, y - 64, 800, 6, "#adb5bd"))
    S.add(rect(0, y - 20, 800, 820 - y, "#868e96"))
    for xx in range(40, 800, 160):
        S.add(rect(xx, y + 80, 80, 10, "#f8f9fa", rx=3))
    S.proposer_cachette(40, y - 30)
    S.proposer_cachette(760, y - 30)


def dedans_bus(S, graine=1):
    """L'intérieur de l'autobus : fenêtres sur la ville, sièges, barres jaunes."""
    fond(S, "#dee2e6")
    S.add(rect(0, 0, 800, 800, lineaire([(0, "#ced4da"), (1, "#f1f3f5")])))
    for k in range(3):
        x0 = 30 + k * 260
        ville_ = g([rect(0, 0, 800, 800, "#a5d8ff"), immeuble(x0 + 20, 380, 120, 3, "#ffd8a8", "plat", graine=graine + k)])
        S.add(fenetre(x0, 90, 220, 200, "#a5d8ff", cadre="#adb5bd", contenu=ville_))
    S.add(rect(0, 600, 800, 200, "#868e96"), rect(0, 600, 800, 10, "#495057"))
    for x0 in (140, 400, 660):
        S.add(rect(x0 - 8, 0, 16, 600, cylindre(JAUNE_BUS, 0.3, 0.7), rx=6))
    S.add(rect(0, 40, 800, 14, cylindre(JAUNE_BUS, 0.3, 0.7, vertical=True), rx=6))
    S.ambiance("interieur")
    S.proposer_cachette(60, 640)
    S.proposer_cachette(740, 640)


def siege(x, y, s=1.0, c="#c92a2a"):
    return place([rect(-70, -140, 140, 140, volume(c, 0.3, 0.8), rx=16), rect(-80, -40, 160, 40, volume(_assombrir(c, 0.85), 0.3, 0.8), rx=10),
                  trait(-50, 0, -50, 40, "#495057", 8), trait(50, 0, 50, 40, "#495057", 8)], x, y, s)


def doudou(x, y, s=1.0, rot=0):
    return place(perso("lapin", 0, 0, 1.0, couleur="#ffc9e3", visage="#fff0f6", expr="sourire", acc=("noeud",), couleur_acc="#be4bdb", ombre=False),
                 x, y, s, rot=rot)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_ville(S, 640)
    S.add(arret(80, 610, 0.9))
    S.add(autobus(420, 760, 1.0, porte_ouverte=True))
    S.add(nadia(600, 790, 1.3, expr="rire", bras="coucou", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(autobus(200, 240, 0.52))
    return S


def p01():
    """Plan moyen : au garage, à l'aube, Nadia vérifie les pneus de son autobus."""
    S = Scene()
    interieur(S, "#adb5bd", "#868e96", 600, plinthe="#495057")
    for k in range(4):
        S.add(rect(40 + k * 190, 60, 150, 90, "#ffd8a8", stroke="#495057", stroke_width=6))
    S.add(autobus(500, 780, 1.0))
    S.add(nadia(130, 790, 1.4, expr="concentre", bras="designe", regard=(1, 0.4)))
    S.add(bulle(400, 380, 330, 90, "Tout est prêt ?", 36, pointe=(200, 470)))
    S.cachette(70, 120, "air")
    return S


def p02():
    """Plan large : au premier arrêt, des gens attendent ; l'autobus arrive."""
    S = Scene()
    rue_ville(S, 640, graine=2)
    S.add(arret(110, 600, 0.9))
    S.add(personne(170, 600, 0.75, stature="adulte", peau="foncee", cheveux="noir", coiffure="chignon", habit="#fcc419", expr="content", regard=(1, 0)))
    S.add(personne(230, 600, 0.6, **ZACK, expr="rire", bras="coucou", regard=(1, 0)))
    S.add(personne(290, 600, 0.75, **DAME, expr="content", regard=(1, 0)))
    S.add(autobus(560, 770, 0.85))
    S.add(texte(560, 150, "Pfffff…", 50, "#1c7ed6", contour="#fff"))
    return S


def p03():
    """Plan moyen : Zack monte et passe sa carte : bip ! « Bonjour, Madame Nadia ! »."""
    S = Scene()
    dedans_bus(S)
    S.add(rect(540, 300, 240, 300, "#495057", rx=8))
    S.add(nadia(660, 640, 1.2, expr="content", bras="salut", regard=(-1, 0)))
    S.add(rect(530, 520, 260, 90, "#343a40", rx=10))
    S.add(rect(400, 420, 70, 110, "#495057", rx=8), rect(410, 440, 50, 30, "#69db7c", rx=4))
    S.add(personne(290, 790, 1.35, expr="rire", bras="donne", regard=(1, -0.3), **ZACK,
                   objet=place(rect(-26, -16, 52, 32, "#fcc419", rx=6), 100, -110)))
    S.add(texte(450, 380, "Bip !", 48, "#2f9e44", contour="#fff"))
    S.add(bulle(250, 150, 420, 90, "Bonjour, Madame Nadia !", 32, pointe=(290, 440)))
    return S


def p04():
    """Gros plan : au volant, Nadia regarde dans son grand miroir."""
    S = Scene()
    dedans_bus(S, 4)
    S.add(nadia(380, 860, 1.9, expr="concentre", bras="porte", regard=(1, -0.3)))
    S.add(cercle(380, 690, 150, "none", stroke="#343a40", stroke_width=26), trait(380, 690, 380, 840, "#343a40", 20), trait(240, 690, 520, 690, "#343a40", 14))
    S.add(rect(600, 160, 150, 110, "#495057", rx=20), rect(612, 172, 126, 86, "#a5d8ff", rx=14))
    S.add(cercle(660, 220, 12, "#fa5252"), rect(690, 210, 30, 16, "#fcc419", rx=4))
    S.camera(1.15, 450, 500)
    S.dessus(bulle(250, 110, 380, 90, "Personne derrière ?", 34, pointe=S.vers_page(440, 420)))
    return S


def p05():
    """Plan large : l'autobus s'abaisse, la rampe se déroule ; Jacques monte en fauteuil roulant."""
    S = Scene()
    rue_ville(S, 640, graine=5)
    S.add(arret(70, 600, 0.9))
    S.add(autobus(400, 770, 0.95, porte_ouverte=True, abaisse=True, rampe=False))
    rampe = poly([(400 - 40 * 0.95 - 30, 770 - 40 * 0.95 + 10), (400 + 40 * 0.95 + 30, 770 - 40 * 0.95 + 10), (400 + 230, 790), (400 + 90, 790)], "#868e96")
    S.add(place(rampe, 0, 0))
    S.add(jacques_fauteuil(560, 790, 0.95, flip=True, expr="rire", bras="salut"))
    S.add(nadia(200, 790, 1.25, expr="content", bras="designe", regard=(1, 0)))
    S.add(bulle(600, 150, 340, 90, "Merci, Nadia !", 36, pointe=(560, 460)))
    return S


def p06():
    """Plan moyen : Zack se lève et laisse sa place à une dame âgée."""
    S = Scene()
    dedans_bus(S, 6)
    S.add(siege(250, 690, 1.0), siege(560, 690, 1.0, "#1c7ed6"))
    S.add(personne(330, 790, 1.3, expr="content", bras="designe", flip=True, regard=(-1, 0), **ZACK))
    S.add(personne(500, 790, 1.25, expr="content", bras="mains_jointes", regard=(-1, 0), **DAME))
    S.add(personne(680, 790, 1.2, expr="sourire", bras="porte", regard=(-1, 0), **MAMAN_LILA))
    S.add(personne(690, 640, 0.8, expr="content", bras="bas", regard=(-1, 0), ombre=False, **LILA))
    S.add(bulle(260, 150, 380, 90, "Prenez ma place !", 36, pointe=(290, 440)))
    return S


def feu(x, y, s=1.0, couleur="rouge"):
    m = [trait(0, 0, 0, -260, "#495057", 10), rect(-34, -400, 68, 160, "#212529", rx=12)]
    for k, (c, nom) in enumerate((("#fa5252", "rouge"), ("#fcc419", "jaune"), ("#40c057", "vert"))):
        m.append(cercle(0, -370 + k * 50, 18, c if couleur == nom else _assombrir(c, 0.4)))
    return place(m, x, y, s)


def p07():
    """Plan large : sous la pluie, au feu rouge, l'autobus s'arrête ; un chat traverse."""
    S = Scene()
    rue_ville(S, 640, pluie_=True, graine=7)
    pluie(S, 90, 7)
    S.add(feu(690, 620, 0.9, "rouge"))
    S.lumiere(690, 620 - 370 * 0.9, 60, "#fa5252", 0.5)
    S.add(autobus(330, 770, 0.9, phares=True))
    for k in range(6):
        S.add(rect(560 + k * 40, 660, 26, 130, "#f8f9fa", opacity=0.8))
    S.add(perso("chat", 640, 760, 0.55, expr="content", bras="marche", couleur="#495057", regard=(1, 0)))
    S.add(texte(560, 150, "Au feu rouge, on s'arrête !", 38, "#e03131", contour="#fff"))
    return S


def p08():
    """Gros plan : au terminus, sur un siège vide, Nadia trouve un doudou lapin."""
    S = Scene()
    dedans_bus(S, 8)
    S.add(siege(400, 700, 1.4, "#c92a2a"))
    S.add(doudou(400, 640, 0.6, rot=-10))
    S.add(nadia(620, 800, 1.6, expr="surpris", bras="joues", regard=(-1, 0.3)))
    S.camera(1.3, 460, 520)
    S.dessus(bulle(260, 120, 360, 90, "Oh ! Un doudou !", 36, pointe=S.vers_page(400, 520)))
    S.cachette(414, 746, "air")
    return S


def p09():
    """Plan moyen : à l'arrêt, Lila retrouve son doudou : « Mon doudou ! »."""
    S = Scene()
    rue_ville(S, 640, graine=9)
    S.add(arret(720, 610, 0.9))
    S.add(nadia(260, 790, 1.4, expr="content", bras="donne", regard=(1, 0.4),
                objet=doudou(*ancre(96, -100, "donne", "adulte"), 0.35)))
    S.add(personne(470, 790, 1.4, expr="rire", bras="tend", regard=(-1, -0.4), flip=True, **LILA))
    S.add(personne(600, 790, 1.3, expr="content", bras="mains_jointes", regard=(-1, 0), **MAMAN_LILA))
    S.add(bulle(460, 150, 340, 90, "Mon doudou !", 40, pointe=(460, 470)))
    return S


def p10():
    """Plan large : le soir, l'autobus passe sous les brosses du lavage, au garage."""
    S = Scene()
    rue_ville(S, 640, soir=True, graine=10)
    S.add(rect(150, 300, 500, 340, "#495057", rx=8), rect(170, 320, 460, 320, "#343a40"))
    S.add(autobus(400, 760, 0.8, phares=True))
    for x0 in (220, 580):
        S.add(rect(x0 - 30, 330, 60, 300, "#4dabf7", rx=30, opacity=0.85))
        for k in range(8):
            S.add(trait(x0 - 30, 340 + k * 36, x0 + 30, 352 + k * 36, "#d0ebff", 4))
    for x, y, r in ((300, 400, 16), (360, 360, 10), (480, 390, 14), (520, 340, 9)):
        S.add(cercle(x, y, r, "#fff", stroke="#a5d8ff", stroke_width=2))
    S.add(nadia(720, 790, 1.15, expr="content", bras="coucou", regard=(-1, 0)))
    S.add(texte(400, 150, "Bonne nuit, l'autobus !", 44, "#fff3bf", contour="#e8590c"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("autobus-seul.svg", vignette),
    ("01-au-garage.svg", p01), ("02-le-premier-arret.svg", p02), ("03-bip.svg", p03),
    ("04-les-miroirs.svg", p04), ("05-la-rampe.svg", p05), ("06-ma-place.svg", p06),
    ("07-le-feu-rouge.svg", p07), ("08-le-doudou.svg", p08), ("09-mon-doudou.svg", p09),
    ("10-le-lavage.svg", p10),
]
