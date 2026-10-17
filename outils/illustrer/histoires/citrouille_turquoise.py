"""La citrouille turquoise — un Halloween avec une allergie aux arachides.

Léa, allergique aux arachides, part frapper aux portes déguisée en dragon,
avec sa pochette de médicament d'urgence et une promesse : ne rien manger
avant que Papa ait vérifié. Elle refuse le chocolat au beurre d'arachide que
lui tend Hugo, découvre chez Madame Inès la citrouille turquoise (des
surprises qui ne se mangent pas), puis ses amis lui proposent un échange.
Halloween est le décor ; l'histoire parle d'une allergie qu'on apprend à
vivre, et d'amis qui veillent.

Plans : 1 moyen (le costume, la pochette) · 2 gros plan (la promesse) ·
3 large (la rue) · 4 moyen (les chocolats) · 5 gros plan (non merci) ·
6 large (la citrouille turquoise) · 7 moyen (Madame Inès) · 8 large (les
bracelets qui brillent) · 9 gros plan (le tri) · 10 moyen (l'échange) ·
11 gros plan (le seau plein) · 12 moyen (on peint la citrouille).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from objets import lampe_poche, pinceau, pot_peinture
from fetes import citrouille_creusee, seau_bonbons, bonbon, chauve_souris_papier

ID = "citrouille-turquoise"
PAPIER_PEINT = "losanges"

TURQUOISE = "#20c997"
TURQUOISE_F = "#0ca678"
DRAGON = "#69db7c"
DRAGON_F = "#2f9e44"


def capuche_dragon():
    """Capuche verte du costume : crête de piquants et deux petites cornes."""
    m = [chemin("M -58 -150 Q -60 -222 0 -226 Q 60 -222 58 -150 Q 52 -186 0 -190 Q -52 -186 -58 -150 Z", volume(DRAGON, 0.3, 0.75))]
    for k, (px, py) in enumerate(((-30, -214), (0, -230), (30, -214))):
        m.append(poly([(px - 12, py + 6), (px, py - 22), (px + 12, py + 6)], "#ffd43b"))
    for sgn in (-1, 1):
        m.append(poly([(sgn * 40, -196), (sgn * 58, -226), (sgn * 52, -190)], "#fff4e6"))
    return g(m)


def ailes_queue():
    """Petites ailes et longue queue du costume de dragon (derrière)."""
    m = [chemin("M 20 -30 Q 100 -20 104 -70 Q 106 -96 128 -100", stroke=DRAGON, sw=16),
         poly([(118, -112), (142, -104), (124, -88)], "#ffd43b")]
    for sgn in (-1, 1):
        m.append(chemin(f"M {sgn * 22} -100 Q {sgn * 90} -150 {sgn * 112} -110 Q {sgn * 92} -104 {sgn * 88} -84 "
                        f"Q {sgn * 70} -96 {sgn * 62} -76 Q {sgn * 46} -90 {sgn * 24} -70 Z", volume(DRAGON_F, 0.3, 0.75)))
    return g(m)


def ventre_dragon():
    m = [ellipse(0, -72, 24, 30, "#d8f5a2")]
    for k in range(3):
        m.append(trait(-16, -90 + k * 14, 16, -90 + k * 14, "#a9e34b", 2.5))
    return g(m)


def pochette(x=-34, y=-58):
    """Petite pochette rouge du médicament d'urgence, à la ceinture."""
    return g([rect(x - 13, y - 10, 26, 22, "#e03131", rx=5), rect(x - 3, y - 7, 6, 16, "#fff"), rect(x - 8, y - 2, 16, 6, "#fff")])


def bandana(c="#e03131"):
    """Foulard de pirate noué sur la tête, et cache-œil."""
    return g([chemin("M -54 -168 Q -52 -214 0 -214 Q 52 -214 54 -168 Q 0 -186 -54 -168 Z", c),
              *[cercle(px, py, 4, "#fff") for px, py in ((-24, -196), (6, -204), (30, -190))],
              chemin("M 50 -176 l 22 10 l -4 18 M 50 -176 l 26 -4", stroke=c, sw=8),
              chemin("M -48 -168 L 42 -138", stroke=ENCRE, sw=3), ellipse(18, -150, 13, 11, ENCRE)])


LEA = dict(peau="claire", cheveux="blond", coiffure="queue", habit=DRAGON, robe=False, jambes=DRAGON_F,
           chaussures="#ffd43b", taches=True, nez="retrousse")
PAPA = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="courts", habit="#1c7ed6", robe=False, jambes="#343a40",
            barbe="#c2410c", carrure="normale", nez="rond")
MAMAN = dict(stature="adulte", peau="claire", cheveux="chatain", coiffure="carre", habit="#f783ac", carrure="fine", nez="pointu")
HUGO = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#f8f9fa", robe=False, jambes=ENCRE, chaussures="#5c3d2e")
ZIA = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#7048e8", acc=("chapeau_pointu",), couleur_acc=ENCRE, yeux="cils")
LAPOINTE = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#e8590c", robe=False,
                jambes="#495057", barbe="#e9ecef", nez="long", carrure="ronde")
INES = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chignon", habit=TURQUOISE_F, carrure="ronde", yeux="cils",
            acc=("lunettes",))


def lea(x, y, s=1.2, costume=True, **k):
    if costume:
        k = {"coiffe": capuche_dragon(), "derriere": ailes_queue(), "tenue": g([ventre_dragon(), pochette()]), **k}
    else:
        k = {"habit": "#ffa94d", "jambes": "#364fc7", "tenue": pochette(), **k}
    return personne(x, y, s, **{**LEA, **k})


def papa(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PAPA, **k})


def hugo(x, y, s=1.15, **k):
    return personne(x, y, s, **{**HUGO, "coiffe": bandana(),
                                "tenue": chemin("M -32 -100 L 32 -60 M -32 -80 L 32 -40", stroke="#e03131", sw=6), **k})


def zia(x, y, s=1.15, **k):
    return personne(x, y, s, **{**ZIA, **k})


def citrouille_turquoise(x, y, s=0.5, S=None):
    """La citrouille peinte en turquoise, et sa lueur."""
    if S is not None:
        S.lumiere(x, y - 55 * s, 150 * s, TURQUOISE, 0.55)
    return citrouille_creusee(x, y, s, couleur=TURQUOISE)


def citrouille_posee(S, x, y, s=0.5):
    S.add(citrouille_creusee(x, y, s))
    S.lumiere(x, y - 55 * s, 120 * s, "#ff922b", 0.6)


def barre_chocolat(x, y, s=1.0, rot=0, ouverte=False):
    """Barre de chocolat aux arachides : emballage brun et dessin d'arachide."""
    m = [rect(-40, -14, 80, 28, "#7c4a1e", rx=4), rect(-40, -14, 14, 28, "#e8590c", rx=3), rect(26, -14, 14, 28, "#e8590c", rx=3),
         ellipse(0, 0, 13, 8, "#e3b57a", stroke="#a0693a", stroke_width=2), trait(0, -7, 0, 7, "#a0693a", 1.5)]
    if ouverte:
        m += [rect(-58, -12, 22, 24, "#5c3a1e", rx=4)]
    return place(m, x, y, s, rot=rot)


def coupelle(x, y, s=1.0, rot=0):
    """Petit chocolat au beurre d'arachide, dans sa coupelle plissée."""
    return place([chemin("M -22 -6 L 22 -6 L 16 14 L -16 14 Z", "#ffa94d"),
                  chemin("M -16 -6 L -12 14 M -6 -6 L -4 14 M 6 -6 L 4 14 M 16 -6 L 12 14", stroke="#e8590c", sw=2),
                  ellipse(0, -8, 23, 9, "#7c4a1e")], x, y, s, rot=rot)


def sucon(x, y, s=1.0, c="#f06595", rot=0):
    return place([rect(-2.5, 0, 5, 50, "#fff", rx=2), cercle(0, 0, 18, c), chemin("M -10 -4 Q 0 -16 10 -4 Q 0 8 -6 2", stroke="#fff", sw=3, opacity=0.7)],
                 x, y, s, rot=rot)


def jujube(x, y, s=1.0, c="#69db7c"):
    return place([chemin("M -12 8 Q -14 -12 0 -12 Q 14 -12 12 8 Z", c), ellipse(-4, -6, 3, 4, "#fff", opacity=0.6)], x, y, s)


def bracelet(x, y, r=22, c="#69db7c", S=None):
    """Bracelet lumineux autour d'un poignet ; (x, y) = centre."""
    if S is not None:
        S.lumiere(x, y, r * 3, c, 0.6)
    return g([ellipse(x, y, r, r * 0.45, "none", stroke=c, stroke_width=7), ellipse(x, y, r, r * 0.45, "none", stroke="#fff", stroke_width=2, opacity=0.8)])


def rue_nuit(S, sol_y=650, lune_=(650, 120), graine=5):
    nuit(S, "#1a1238", "#4b2f7a")
    etoiles(S, 34, graine, (0, 0, 800, sol_y - 240))
    if lune_:
        S.add(lune(*lune_, 46))
    sol(S, sol_y, "#4a3f6b", bosse=8)


def facade(S, x0, x1, y0, y1, couleur, porte_x):
    """Pan de façade au plan moyen, porte ouverte sur un intérieur éclairé."""
    S.add(rect(x0, y0, x1 - x0, y1 - y0, couleur), planches(x0, y0, x1 - x0, y1 - y0, couleur, larg=30))
    S.add(rect(porte_x - 100, y1 - 400, 200, 400, "#ffe8a3"), rect(porte_x - 112, y1 - 412, 224, 14, "#3b2a5e"),
          rect(porte_x - 112, y1 - 412, 12, 412, "#3b2a5e"), rect(porte_x + 100, y1 - 412, 12, 412, "#3b2a5e"))
    S.add(poly([(porte_x + 100, y1 - 400), (porte_x + 60, y1 - 384), (porte_x + 60, y1 - 12), (porte_x + 100, y1)],
               cylindre("#5f3dc4", 0.2, 0.7)))
    S.lumiere(porte_x, y1 - 200, 220, "#ffd43b", 0.55)
    S.lumiere(porte_x, y1 + 40, 200, "#ffd43b", 0.4, ry=50)


def toile_coton(x, y, s=1.0):
    """Fausse toile d'araignée en coton, décoration d'Halloween."""
    m = []
    for a in range(0, 181, 30):
        t = math.radians(a)
        m.append(trait(0, 0, 90 * math.cos(t), 90 * math.sin(t), "#f8f9fa", 2.5, opacity=0.8))
    for r in (30, 55, 80):
        m.append(chemin(" ".join(f"{'M' if k == 0 else 'L'} {n(r * math.cos(math.radians(a)))} {n(r * math.sin(math.radians(a)))}"
                                 for k, a in enumerate(range(0, 181, 30))), stroke="#f8f9fa", sw=2.5, opacity=0.8))
    return place(m, x, y, s)


def cuisine_soir(S, y=600):
    piece(S, "cuisine", y)
    S.ambiance("interieur")
    S.add(fenetre(560, 90, 170, 150, "#1a1238", nuit_=True, rideaux="#e8590c"))
    S.add(lampe(110, y - 10, 0.9))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_nuit(S, 640, lune_=(140, 150))
    S.add(maison(640, 640, 0.75, mur="#8c7ab8", toit="#212529", lumiere=True))
    S.add(chauve_souris_papier(300, 200, 0.9, rot=-10), chauve_souris_papier(450, 260, 0.7, rot=14))
    S.add(rect(500, 690, 280, 26, "#6c5f8d"), rect(520, 664, 240, 26, "#7a6aa8"))
    S.add(citrouille_turquoise(650, 666, 0.62, S))
    citrouille_posee(S, 560, 668, 0.36)
    citrouille_posee(S, 740, 690, 0.3)
    S.add(lea(320, 780, 1.55, expr="rire", bras="victoire", regard=(1, 0), objet=None))
    bx, by = mains_personne(320, 780, 1.55, "victoire")[1]
    S.add(bracelet(bx, by + 6, 20, "#ff6b6b", S))
    gx, gy = mains_personne(320, 780, 1.55, "victoire")[0]
    S.add(seau_bonbons(gx, gy - 8, 1.1))
    S.cachette(60, 760)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 170, 110, radial([(0, TURQUOISE, 0.4), (1, TURQUOISE, 0)])))
    S.add(citrouille_turquoise(200, 262, 0.8))
    return S


def p01():
    """Plan moyen : dans l'entrée, le costume de dragon et la pochette."""
    S = Scene()
    piece(S, "manoir", 620)
    S.ambiance("interieur")
    S.add(porte(640, 640, 170, 340, "#5f3dc4"))
    S.add(rect(80, 140, 120, 160, "#adb5bd", rx=60), rect(92, 152, 96, 136, "#e7f5ff", rx=48))
    S.add(cadre_mur(300, 150, 110, 90, "#b2f2bb"))
    S.add(lea(320, 780, 1.25, expr="content", bras="hanches", regard=(1, 0)))
    S.add(personne(520, 780, 1.45, expr="sourire", bras="tend", flip=True, regard=(-1, 0.3), **MAMAN))
    S.add(bulle(560, 120, 380, 100, "Ton médicament d'urgence.\nOn ne l'oublie jamais.", 28, pointe=(520, 420)))
    S.cachette(770, 780)
    return S


def p02():
    """Gros plan : la promesse, petit doigt contre petit doigt."""
    S = Scene()
    piece(S, "manoir", 600)
    S.ambiance("interieur")
    S.add(lea(270, 800, 1.5, expr="fier", bras="tend", regard=(1, 0)))
    # Papa, accroupi : on le pose plus bas, la tête à la hauteur de celle de Léa
    S.add(papa(560, 900, 1.5, expr="sourire", bras="tend", flip=True, regard=(-1, 0)))
    S.add(chemin("M 408 640 q 6 -14 14 -4", stroke=ENCRE, sw=3))
    S.camera(1.3, 410, 520)
    S.dessus(bulle(400, 100, 500, 100, "Je ne mange rien avant\nque tu aies vérifié. Promis !", 30, pointe=S.vers_page(290, 450)))
    S.cachette(80, 760)
    return S


def p03():
    """Plan large : la rue d'Halloween ; c'est parti !"""
    S = Scene()
    rue_nuit(S, 600, lune_=(670, 110), graine=7)
    for k, (x, s, mur, toit) in enumerate(((120, 0.62, "#ffa94d", "#3b2a5e"), (390, 0.68, "#8c7ab8", "#212529"),
                                            (660, 0.6, "#74c0fc", "#5f3dc4"))):
        S.add(maison(x, 600, s, mur=mur, toit=toit, lumiere=True, cheminee=k != 1))
        citrouille_posee(S, x + 90 * s, 620, 0.26)
    S.add(chemin("M 0 800 Q 400 690 800 720 L 800 760 Q 420 740 0 800 Z", "#6c5f8d"))
    S.add(zia(560, 730, 0.95, expr="rire", bras="court", regard=(1, 0), objet=None))
    S.add(hugo(430, 745, 0.95, expr="rire", bras="tient", regard=(1, 0), objet=seau_bonbons(68, -146, 0.8)))
    S.add(lea(300, 760, 1.0, expr="rire", bras="tient", regard=(1, 0), objet=seau_bonbons(68, -146, 0.8, "#0ca678")))
    S.add(papa(120, 770, 1.2, expr="sourire", bras="tient", regard=(1, 0), pas="marche",
               objet=lampe_poche(*ancre(68, -146, "tient", "adulte"), 0.8, rot=-30)))
    S.add(bulle(330, 170, 380, 90, "Des bonbons ou un sort !", 30))
    S.cachette(770, 780)
    return S


def p04():
    """Plan moyen : les chocolats de Monsieur Lapointe."""
    S = Scene()
    rue_nuit(S, 680, lune_=None)
    facade(S, 330, 800, 110, 690, "#ffa94d", 580)
    S.add(toile_coton(800, 110, 1.0), toile_coton(330, 110, 0.8))
    citrouille_posee(S, 390, 720, 0.4)
    bx, by = ancre(84, -92, "donne", "ancien", "ronde")
    S.add(personne(600, 700, 1.2, expr="rire", bras="donne", flip=True, regard=(-1, 0),
                   objet=g([barre_chocolat(bx, by, 0.9, rot=-10), barre_chocolat(bx + 6, by - 20, 0.9, rot=8)]), **LAPOINTE))
    S.add(hugo(160, 790, 1.15, expr="miam", bras="bouche", regard=(1, 0), objet=None))
    S.add(barre_chocolat(*mains_personne(160, 790, 1.15, "bouche")[1], 0.8, rot=-70, ouverte=True))
    S.add(lea(360, 790, 1.2, expr="concentre", bras="ramasse", regard=(0, 1),
              objet=g([seau_bonbons(-30, -60, 0.9, "#0ca678"), barre_chocolat(-26, -40, 0.6, rot=20)])))
    S.add(bulle(170, 150, 260, 80, "Miam !", 40, pointe=(170, 480)))
    S.cachette(770, 780)
    return S


def p05():
    """Gros plan : « Non merci, je suis allergique. »"""
    S = Scene()
    rue_nuit(S, 640, lune_=(120, 120))
    S.add(maison(660, 640, 0.6, mur="#74c0fc", toit="#5f3dc4", lumiere=True))
    citrouille_posee(S, 330, 670, 0.3)
    S.add(hugo(560, 800, 1.45, expr="surpris", bras="donne", flip=True, regard=(-1, 0),
               objet=coupelle(84, -92, 1.0)))
    S.add(lea(260, 800, 1.5, expr="sourire", bras="leve_doigt", regard=(1, 0)))
    S.camera(1.3, 410, 520)
    S.dessus(bulle(240, 100, 400, 110, "Non merci,\nje suis allergique.", 32, pointe=S.vers_page(260, 430)))
    S.cachette(760, 770)
    return S


def p06():
    """Plan large : tout au bout de la rue, la citrouille turquoise."""
    S = Scene()
    rue_nuit(S, 620, lune_=(110, 100), graine=9)
    S.add(maison(520, 610, 1.1, mur="#d0bfff", toit="#212529", lumiere=True, volets="#0ca678"))
    S.add(toile_coton(400, 380, 0.7), toile_coton(640, 380, 0.7))
    S.add(rect(400, 610, 240, 22, "#6c5f8d"), rect(420, 592, 200, 20, "#7a6aa8"))
    S.add(citrouille_turquoise(560, 600, 0.55, S))
    citrouille_posee(S, 460, 610, 0.36)
    citrouille_posee(S, 690, 630, 0.32)
    S.add(arbre(760, 620, 1.0, feuillage="#3b2a5e", feuillage2="#2b1f45", tronc="#2b1f45"))
    S.add(zia(140, 780, 0.95, expr="surpris", bras="joues", regard=(1, -0.5)))
    S.add(hugo(250, 790, 0.95, expr="bouche_bee", bras="bas", regard=(1, -0.5)))
    S.add(lea(360, 790, 1.0, expr="joie", bras="designe", regard=(1, -0.5)))
    S.add(bulle(220, 170, 320, 90, "Une citrouille bleue ?", 30, pointe=(150, 560)))
    S.cachette(760, 780)
    return S


def panier_surprises(x, y, s=1.0):
    """Panier plein d'autocollants, de crayons et de bracelets lumineux ; (x, y) = fond."""
    m = [chemin("M -70 -70 Q -70 -140 0 -140 Q 70 -140 70 -70", stroke="#a0693a", sw=8)]
    for k, c in enumerate(("#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8")):
        m.append(rect(-56 + k * 22, -110 + (k % 2) * 8, 8, 50, c, rx=3, transform=f"rotate({(k - 2) * 10} {-52 + k * 22} -80)"))
    for k, c in enumerate(("#69db7c", "#f783ac", "#4dabf7")):
        m.append(ellipse(-30 + k * 30, -74, 18, 8, "none", stroke=c, stroke_width=5))
    m += [etoile5(30, -96, 10, "#ffd43b"), coeur(-30, -92, 0.25, "#e64980"),
          chemin("M -72 -70 L 72 -70 L 58 0 L -58 0 Z", volume("#c68642", 0.3, 0.75)),
          chemin("M -68 -48 H 68 M -64 -26 H 64", stroke="#8d5524", sw=3, opacity=0.6)]
    return place(m, x, y, s)


def p07():
    """Plan moyen : Madame Inès et son panier de surprises."""
    S = Scene()
    rue_nuit(S, 680, lune_=None)
    facade(S, 0, 800, 100, 690, "#d0bfff", 540)
    S.add(toile_coton(0, 100, 1.0))
    S.add(citrouille_turquoise(760, 730, 0.5, S))
    px, py = ancre(84, -92, "donne", "adulte", "ronde")
    S.add(personne(560, 700, 1.25, expr="rire", bras="donne", flip=True, regard=(-1, 0.3),
                   objet=panier_surprises(px, py + 40, 0.8), **INES))
    S.add(zia(120, 760, 1.05, expr="joie", bras="mains_jointes", regard=(1, 0)))
    S.add(hugo(220, 775, 1.05, expr="bouche_bee", bras="bas", regard=(1, 0)))
    hx, hy = mains_personne(350, 790, 1.2, "tend")[1]
    S.add(lea(350, 790, 1.2, expr="rire", bras="tend", regard=(1, 0)))
    S.add(bracelet(hx + 10, hy - 6, 18, "#69db7c", S))
    S.add(bulle(250, 130, 420, 110, "Ici, des surprises\nqui ne se mangent pas !", 30, pointe=(530, 420)))
    S.cachette(30, 780)
    return S


def p08():
    """Plan large : les bracelets dessinent des ronds de lumière."""
    S = Scene()
    nuit(S, "#120c2a", "#2f2360")
    etoiles(S, 50, 13, (0, 0, 800, 380))
    S.add(lune(660, 110, 44))
    sol(S, 640, "#3b2f5c", bosse=8)
    S.add(maison(120, 640, 0.6, mur="#8c7ab8", toit="#212529", lumiere=True))
    citrouille_posee(S, 230, 670, 0.3)
    for k, (x, c, bras) in enumerate(((260, "#ff6b6b", "danse"), (420, "#69db7c", "saute"), (590, "#4dabf7", "danse"))):
        qui = (zia, lea, hugo)[k]
        S.add(qui(x, 780, 1.05, expr="rire", bras=bras, flip=k == 2, regard=(0, -0.5)))
        for hx, hy in mains_personne(x, 780, 1.05, bras, flip=k == 2):
            S.add(chemin(f"M {n(hx - 70)} {n(hy + 30)} Q {n(hx)} {n(hy - 70)} {n(hx + 70)} {n(hy + 20)}", stroke=c, sw=6, opacity=0.8))
            S.add(bracelet(hx, hy, 16, c, S))
    S.add(papa(730, 790, 1.0, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.cachette(40, 780)
    return S


def p09():
    """Gros plan : le tri ; le tas des « non » est bien plus gros."""
    S = Scene()
    cuisine_soir(S, 560)
    S.add(lea(200, 660, 1.3, expr="triste", bras="joues", regard=(1, 1)))
    S.add(papa(650, 660, 1.2, expr="concentre", bras="porte", regard=(-1, 1), objet=barre_chocolat(*ancre(0, -84, "porte", "adulte"), 0.8, rot=-15)))
    S.add(table(400, 800, 760, 200, "#c68642", nappe="#ffc9c9"))
    # le petit tas des « oui »
    for k, (px, py, c) in enumerate(((290, 590, "#f06595"), (330, 594, "#74c0fc"), (310, 578, "#ffd43b"))):
        S.add(bonbon(px, py, 1.0, c, rot=k * 40))
    S.add(texte(310, 640, "oui", 30, "#2f9e44"))
    # le gros tas des « non »
    for k in range(9):
        S.add(barre_chocolat(470 + (k % 3) * 50, 596 - (k // 3) * 22, 0.75, rot=(k * 23) % 40 - 20))
    for k in range(4):
        S.add(coupelle(450 + k * 40, 610, 0.8))
    S.add(texte(520, 650, "non", 30, "#e03131"))
    S.camera(1.3, 400, 520)
    S.cachette(720, 760)
    return S


def p10():
    """Plan moyen : l'échange."""
    S = Scene()
    cuisine_soir(S, 600)
    S.add(papa(680, 700, 1.15, expr="rire", bras="hanches", regard=(-1, 0)))
    S.add(table(400, 800, 520, 110, "#c68642", nappe="#fff3bf"))
    S.add(hugo(500, 720, 1.1, expr="rire", bras="donne", flip=True, regard=(-1, 0),
               objet=g([sucon(84, -110, 0.9, "#f06595", rot=-20), sucon(96, -104, 0.9, "#4dabf7", rot=10)])))
    S.add(zia(640, 760, 1.0, expr="rire", bras="tend", flip=True, regard=(-1, 0),
              objet=g([jujube(96, -110, 1.2, "#69db7c"), jujube(110, -100, 1.2, "#ff922b")])))
    S.add(lea(250, 730, 1.15, costume=True, expr="rire", bras="donne", regard=(1, 0),
              objet=g([barre_chocolat(84, -96, 0.75, rot=10), barre_chocolat(90, -116, 0.75, rot=-6)])))
    S.add(bulle(330, 130, 380, 90, "On fait un échange !", 34, pointe=(480, 420)))
    S.cachette(770, 790)
    return S


def p11():
    """Gros plan : le seau plein de bonbons sans arachides."""
    S = Scene()
    cuisine_soir(S, 560)
    S.add(lea(400, 640, 1.4, costume=True, expr="content", bras="joues", regard=(0, 1)))
    S.add(table(400, 800, 760, 220, "#c68642", nappe="#ffc9c9"))
    S.add(seau_bonbons(400, 470, 2.0, "#0ca678"))
    for k, c in enumerate(("#f06595", "#4dabf7", "#ffd43b", "#cc5de8")):
        S.add(sucon(330 + k * 46, 520, 0.9, c, rot=(k - 1.5) * 18))
    S.add(bracelet(400, 548, 46, "#ff6b6b", S))
    S.add(jujube(270, 620, 1.2, "#69db7c"), jujube(530, 620, 1.2, "#ff922b"), bonbon(560, 640, 1.1, "#ffd43b"))
    S.camera(1.35, 400, 520)
    S.cachette(150, 700)
    return S


def p12():
    """Plan moyen : le lendemain, on peint une citrouille en turquoise."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff4e6")
    collines(S, 520, "#ffc078", graine=4, bosquets=False)
    sol(S, 600, "#d8a35d", bosse=8)
    S.add(maison(640, 600, 0.9, mur="#ffe8cc", toit="#1c7ed6", volets="#0ca678"))
    S.add(arbre(110, 600, 1.1, feuillage="#ff922b", feuillage2="#e8590c", tronc="#7c4a1e"))
    S.add(rect(240, 680, 340, 30, "#c68642"), planches(240, 680, 340, 30, "#c68642", larg=30, vertical=False))
    S.add(lea(220, 790, 1.2, costume=False, expr="concentre", bras="tend", regard=(1, 0.3),
              objet=pinceau(96, -104, 1.0, TURQUOISE, rot=60)))
    S.add(papa(610, 790, 1.2, expr="rire", bras="tend", flip=True, regard=(-1, 0.3),
               objet=pinceau(*ancre(96, -104, "tend", "adulte"), 1.0, TURQUOISE, rot=60)))
    S.add(citrouille_creusee(410, 700, 1.05, visage=False, couleur="#ff922b"))
    S.add(chemin("M 326 650 Q 312 580 350 540 Q 384 520 420 526 Q 404 590 420 660 Q 380 630 326 650 Z", TURQUOISE))
    S.add(goutte(352, 660, 0.6, TURQUOISE), goutte(470, 668, 0.5, TURQUOISE))
    S.add(pot_peinture(520, 760, 0.8, TURQUOISE))
    S.add(bulle(400, 140, 460, 100, "L'an prochain, chez nous aussi !", 30, pointe=(300, 420)))
    S.cachette(770, 780)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("citrouille-seule.svg", vignette),
    ("01-le-dragon.svg", p01), ("02-la-promesse.svg", p02), ("03-c-est-parti.svg", p03),
    ("04-les-chocolats.svg", p04), ("05-non-merci.svg", p05), ("06-la-citrouille-turquoise.svg", p06),
    ("07-madame-ines.svg", p07), ("08-ca-brille.svg", p08), ("09-le-tri.svg", p09),
    ("10-l-echange.svg", p10), ("11-le-seau-plein.svg", p11), ("12-l-an-prochain.svg", p12),
]
