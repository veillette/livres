"""Le premier Noël de Samir — une famille qui ne fête pas Noël, et un ami qui l'invite.

En décembre, à l'école, tout le monde parle du père Noël ; chez Samir, on
fête l'Aïd. Émile l'invite à décorer son sapin le 24 décembre : Samir
arrive avec les maamouls de Teta, sa grand-mère, pose l'étoile au sommet
et apprend à tout le monde à dire « choukrane ». Quelques mois plus tard,
à l'Aïd, c'est Émile qui est invité. Noël est le décor ; l'histoire parle
d'amitié et de traditions qu'on partage.

Plans : 1 large (la classe) · 2 gros plan (chez nous, on ne fête pas Noël) ·
3 moyen (la pensée de l'Aïd) · 4 moyen (l'invitation) · 5 gros plan (les
maamouls) · 6 large (la rue illuminée) · 7 moyen (bienvenue) · 8 large (le
sapin) · 9 gros plan (l'étoile) · 10 moyen (choukrane) · 11 large (l'Aïd
chez Samir) · 12 moyen (deux fêtes).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne, echelle
from fetes import sapin_decore, boule_noel, guirlande_lumineuse, cadeau, guirlande_fanions, lanterne

ID = "noel-samir"
PAPIER_PEINT = "rayures"

OR_ = "#fcc419"
VERT = "#2b8a3e"


def foulard(c="#7048e8", c2="#9775fa"):
    """Le haut du foulard de Teta, sur le front (coiffe)."""
    return g([chemin("M -56 -156 Q -58 -216 0 -218 Q 58 -216 56 -156 Q 46 -196 0 -198 Q -46 -196 -56 -156 Z", c),
              chemin("M -40 -196 Q 0 -212 40 -196", stroke=c2, sw=3)])


def foulard_derriere(c="#7048e8"):
    """Le pan du foulard qui encadre le visage et tombe sur les épaules
    (dessiné derrière la tête d'une personne âgée)."""
    return chemin("M -58 -170 Q -62 -230 0 -232 Q 62 -230 58 -170 Q 66 -110 44 -100 L -44 -100 Q -66 -110 -58 -170 Z", c)


SAMIR = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#f08c00", robe=False, jambes="#364fc7", nez="rond")
EMILE = dict(peau="claire", cheveux="blond", coiffure="raie", habit="#e03131", robe=False, jambes="#495057", taches=True)
PAPA_S = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#1971c2", robe=False, jambes="#343a40",
              barbe="#2b2b3a", carrure="normale", nez="long")
TETA = dict(stature="ancien", peau="brune", cheveux="noir", coiffure="chauve", habit="#9775fa", carrure="ronde", nez="rond",
            coiffe=foulard(), derriere=foulard_derriere())
MAMAN_E = dict(stature="adulte", peau="claire", cheveux="chatain", coiffure="queue", habit="#2f9e44", carrure="fine", nez="pointu")
PAPI_E = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#c92a2a", robe=False,
              jambes="#495057", barbe="#e9ecef", carrure="ronde", acc=("lunettes",))
CLAIRE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="carre", habit="#ae3ec9", carrure="fine", yeux="cils")
CAMARADES = (dict(peau="claire", cheveux="roux", coiffure="couettes", habit="#f783ac"),
             dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#69db7c", robe=False, jambes="#2b8a3e"),
             dict(peau="rosee", cheveux="chatain", coiffure="longs", habit="#74c0fc"),
             dict(peau="doree", cheveux="noir", coiffure="herisses", habit="#ffd43b", robe=False, jambes="#495057"))


def samir(x, y, s=1.15, **k):
    return personne(x, y, s, **{**SAMIR, **k})


def emile(x, y, s=1.15, **k):
    return personne(x, y, s, **{**EMILE, **k})


def papa(x, y, s=1.15, **k):
    return personne(x, y, s, **{**PAPA_S, **k})


def teta(x, y, s=1.15, **k):
    return personne(x, y, s, **{**TETA, **k})


def camarade(i, x, y, s=0.95, **k):
    return personne(x, y, s, **{**CAMARADES[i % len(CAMARADES)], **k})


def croissant_soir(x, y, r, fond="#1c2a52"):
    """Fin croissant de lune du soir (lune croissante, éclairée à droite,
    du côté du Soleil couché), qui annonce la fin du ramadan et l'Aïd."""
    return g([cercle(x, y, r * 1.8, radial([(0.4, "#fff3bf", 0.3), (1, "#fff3bf", 0)])), cercle(x, y, r, "#fff3bf"),
              sans_relief(cercle(x - r * 0.42, y - r * 0.18, r * 0.92, fond))])


def maamoul(x, y, s=1.0):
    """Maamoul : petit gâteau rond et bombé, décoré au moule, poudré de sucre."""
    m = [ellipse(0, -10, 24, 15, volume("#e9c48f", 0.4, 0.75)),
         chemin("M -16 -14 Q 0 -26 16 -14 M -10 -8 Q 0 -18 10 -8 M -18 -6 Q 0 0 18 -6", stroke="#c08552", sw=2),
         ellipse(-4, -18, 14, 6, "#fff", opacity=0.7)]
    return place(m, x, y, s)


def boite_maamouls(x, y, s=1.0):
    """Boîte ouverte pleine de maamouls ; (x, y) = milieu du fond."""
    m = [rect(-70, -40, 140, 40, volume("#e64980", 0.3, 0.75), rx=6),
         *[maamoul(-46 + (k % 4) * 31, -34 - (k // 4) * 12, 0.8) for k in range(8)],
         rect(-70, -26, 140, 26, "#e64980", rx=6), chemin("M -70 -16 H 70", stroke=OR_, sw=4)]
    return place(m, x, y, s)


def moule_bois(x, y, s=1.0):
    return place([rect(-70, -14, 100, 28, "#a0693a", rx=10), cercle(0, 0, 26, "#8d5524"), cercle(0, 0, 18, "#a0693a"),
                  chemin("M -12 0 L 12 0 M 0 -12 L 0 12 M -8 -8 L 8 8 M -8 8 L 8 -8", stroke="#6d4424", sw=2.5)], x, y, s)


def escabeau(x, y, s=1.0):
    """Petit escabeau de bois ; (x, y) = sol, au milieu ; marche du haut à -150."""
    m = [trait(-50, 0, -20, -170, "#c68642", 10), trait(50, 0, 20, -170, "#c68642", 10)]
    for k, yy in enumerate((-50, -100, -150)):
        w = 46 - k * 9
        m.append(rect(-w, yy - 8, 2 * w, 14, cylindre("#e3a857", 0.3, 0.75, vertical=True), rx=4))
    return place(m, x, y, s)


def flocon_papier(x, y, s=1.0):
    m = []
    for a in range(0, 180, 30):
        t = math.radians(a)
        m.append(trait(-30 * math.cos(t), -30 * math.sin(t), 30 * math.cos(t), 30 * math.sin(t), "#fff", 5))
    m.append(cercle(0, 0, 8, "#fff"))
    return place(m, x, y, s)


def classe(S, y=600):
    """La classe en décembre : flocons de papier aux fenêtres, petit sapin."""
    interieur(S, "#fff9db", "#d9a066", y, plinthe="#c68642")
    S.add(rect(240, 80, 320, 200, "#8d5524", rx=8), rect(252, 92, 296, 176, "#2b8a3e", rx=4))
    S.add(texte(400, 160, "décembre", 40, "#f8f9fa", police="Andika, sans-serif", poids=400))
    S.add(flocon_papier(320, 220, 0.8), flocon_papier(480, 220, 0.8), flocon_papier(400, 235, 0.6))
    for fx in (40, 620):
        S.add(fenetre(fx, 110, 140, 150, "#d0ebff", contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 220, 800, 100, "#fff")])))
        S.add(flocon_papier(fx + 40, 150, 0.6), flocon_papier(fx + 100, 210, 0.5))


def bureau(x, y, w=200, c="#74c0fc"):
    return g([rect(x - w / 2 + 10, y - 90, 12, 90, "#868e96"), rect(x + w / 2 - 22, y - 90, 12, 90, "#868e96"),
              rect(x - w / 2, y - 108, w, 22, volume(c, 0.3, 0.75), rx=5)])


def salon_emile(S, y=600, soir=True):
    """Le salon d'Émile : boiseries, fenêtre sur la neige, guirlande."""
    piece(S, "manoir", y)
    dehors = g([rect(0, 0, 800, 800, "#1c2a52" if soir else "#d0ebff"), rect(0, 200, 800, 300, "#f1f3f5"),
                sapin(660, 210, 0.3, neige=True)])
    S.add(fenetre(580, 100, 160, 150, "#1c2a52", rideaux="#c92a2a", contenu=dehors))
    S.ambiance("interieur")


def rue_neige(S, sol_y=620):
    nuit(S, "#1c2a52", "#5c6fb0")
    etoiles(S, 30, 4, (0, 0, 800, 260))
    collines(S, sol_y - 60, "#c5d0f0", graine=5, bosquets=False)
    sol(S, sol_y, "#f1f3f5", bosse=10)
    flocons(S, 30, 4, (0, 0, 800, sol_y))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon_emile(S, 640)
    S.add(guirlande_lumineuse(10, 50, 790, 50, creux=20, nb=14))
    S.add(sapin_decore(400, 640, 1.55, etoile=etoile5(0, 0, 30, OR_)))
    S.add(tapis(400, 720, 300, 50, "#ffc9c9", "#e03131"))
    S.add(cadeau(300, 720, 0.45, "#4dabf7"), cadeau(510, 725, 0.4, OR_, "#e03131"))
    S.add(samir(230, 790, 1.35, expr="rire", bras="tient", regard=(1, -0.5), objet=boite_maamouls(68, -146, 0.75)))
    S.add(emile(580, 790, 1.35, expr="rire", bras="coucou", flip=True, regard=(-1, -0.5)))
    S.cachette(760, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(boite_maamouls(200, 240, 1.6))
    return S


def p01():
    """Plan large : la classe en décembre ; tout le monde parle du père Noël."""
    S = Scene()
    classe(S, 580)
    S.add(sapin_decore(700, 600, 0.75))
    S.add(personne(120, 640, 1.05, expr="sourire", bras="mains_jointes", regard=(1, 0), **CLAIRE))
    for k, (x, y) in enumerate(((250, 680), (400, 680), (560, 680))):
        S.add(camarade(k, x, y, 0.85, expr=("rire", "joie", "rire")[k], bras=("haut", "ouverts", "lance")[k], regard=((1, 0), (-1, 0), (-1, 0))[k]))
        S.add(bureau(x, y + 70, 170, ("#ffa8a8", "#69db7c", "#74c0fc")[k]))
    S.add(samir(400, 790, 0.95, expr="neutre", bras="porte", regard=(0, -0.3)))
    S.add(bureau(400, 860, 200, "#ffd43b"))
    S.add(bulle(220, 400, 240, 70, "Un vélo !", 30, pointe=(250, 500)), bulle(600, 380, 260, 70, "Un dinosaure !", 28, pointe=(560, 490)))
    S.cachette(770, 780)
    return S


def p02():
    """Gros plan : « Chez nous, on ne fête pas Noël. »"""
    S = Scene()
    classe(S, 580)
    S.add(camarade(0, 170, 760, 1.15, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(camarade(3, 640, 760, 1.15, expr="bouche_bee", bras="bas", regard=(-1, 0)))
    S.add(samir(400, 800, 1.5, expr="sourire", bras="pense", regard=(0, 0)))
    S.camera(1.3, 400, 540)
    S.dessus(bulle(400, 95, 520, 90, "Chez nous, on ne fête pas Noël.", 30, pointe=S.vers_page(400, 440)))
    S.cachette(760, 770)
    return S


def scene_aid():
    """Ce que Samir imagine : sa famille le soir de l'Aïd (dans une bulle)."""
    m = [rect(-150, -100, 300, 200, "#fff4e6"),
         rect(60, -86, 70, 70, "#1c2a52", rx=6), croissant_soir(100, -54, 20),
         rect(-150, 40, 300, 60, "#e8c39e"),
         rect(-120, 10, 140, 14, "#c68642"), *[maamoul(-110 + k * 26, 12, 0.5) for k in range(5)],
         cadeau(80, 60, 0.35, "#e64980"), cadeau(115, 64, 0.3, OR_, "#7048e8"),
         place(personne(0, 0, 1.0, **{**TETA, "expr": "rire", "bras": "ouverts"}), -110, 60, 0.42),
         place(personne(0, 0, 1.0, **{**SAMIR, "habit": "#fff", "expr": "rire", "bras": "haut"}), 30, 70, 0.38)]
    return m


def p03():
    """Plan moyen : dans la cour, Samir raconte l'Aïd à Émile."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f1f3f5")
    collines(S, 520, "#e7f5ff", graine=3, bosquets=False)
    sol(S, 600, "#f8f9fa", bosse=10)
    S.add(rect(0, 360, 800, 160, "#e9a66b"), briques(0, 360, 800, 160, "#e9a66b"))
    S.add(sapin(720, 610, 0.8, neige=True))
    S.add(samir(270, 780, 1.25, expr="rire", bras="ouverts", regard=(1, 0), acc=()))
    S.add(emile(540, 780, 1.25, expr="bouche_bee", bras="bas", flip=True, regard=(-1, 0)))
    S.add(pensee(360, 200, 190, "", depuis=(280, 440)))
    S.add(place(scene_aid(), 360, 200, 1.1))
    S.cachette(40, 780)
    return S


def p04():
    """Plan moyen : à la sortie de l'école, l'invitation."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f1f3f5")
    sol(S, 620, "#f8f9fa", bosse=8)
    S.add(rect(0, 300, 560, 330, "#e9a66b"), briques(0, 300, 560, 330, "#e9a66b"))
    S.add(rect(170, 400, 160, 220, "#1c7ed6"), rect(160, 390, 180, 14, "#1864ab"))
    S.add(texte(440, 360, "École", 34, "#fff"))
    for x in range(560, 800, 30):
        S.add(rect(x, 520, 8, 110, "#495057"))
    S.add(rect(560, 520, 240, 8, "#495057"), rect(560, 570, 240, 6, "#495057"))
    flocons(S, 40, 9, (0, 0, 800, 620))
    S.add(papa(680, 790, 1.2, expr="sourire", bras="coucou", flip=True, regard=(-1, 0)))
    S.add(samir(430, 790, 1.15, expr="surpris", bras="bas", regard=(1, 0)))
    S.add(emile(250, 790, 1.15, expr="rire", bras="main", regard=(1, 0)))
    S.add(bulle(260, 130, 380, 100, "Le 24, viens décorer\nnotre sapin !", 32, pointe=(260, 430)))
    S.cachette(40, 780)
    return S


def p05():
    """Gros plan : dans la cuisine de Teta, les maamouls."""
    S = Scene()
    piece(S, "cuisine", 560)
    S.add(fenetre(570, 90, 160, 140, "#d0ebff", rideaux="#7048e8"))
    S.add(teta(560, 720, 1.4, expr="content", bras="porte", regard=(-1, 0.6),
               objet=moule_bois(*ancre(0, -74, "porte", "ancien", "ronde"), 1.0)))
    S.add(samir(230, 730, 1.3, expr="rire", bras="tient", regard=(1, 0.5), objet=rect(56, -160, 24, 30, "#fff", rx=4)))
    S.add(table(400, 800, 760, 170, "#c68642"))
    S.add(rect(240, 600, 300, 24, "#adb5bd", rx=6))
    for k in range(10):
        S.add(maamoul(270 + (k % 5) * 56, 610 - (k // 5) * 2, 0.95))
    S.add(g([cercle(300 + (k * 37) % 220, 520 + (k * 23) % 80, 3 + k % 3, "#fff", opacity=0.9) for k in range(22)]))
    S.camera(1.3, 400, 560)
    S.dessus(texte(250, 130, "Pfff !", 54, "#fff", contour="#7048e8", rot=-8))
    S.cachette(120, 780)
    return S


def p06():
    """Plan large : la rue illuminée, le soir du 24 décembre."""
    S = Scene()
    rue_neige(S, 600)
    for k, (x, s, mur, toit) in enumerate(((130, 0.65, "#ffe8cc", "#c92a2a"), (400, 0.6, "#e7f5ff", "#2f9e44"),
                                            (660, 0.7, "#fff3bf", "#1c7ed6"))):
        S.add(maison(x, 600, s, mur=mur, toit=toit, lumiere=True))
        S.add(guirlande_lumineuse(x - 125 * s, 600 - 146 * s, x + 125 * s, 600 - 146 * s, creux=8, nb=7, graine=k))
    S.add(sapin(270, 620, 0.6, neige=True), sapin(540, 630, 0.55, neige=True))
    S.add(chemin("M 0 760 Q 400 690 800 720 L 800 760 Q 400 730 0 800 Z", "#dbe4ff"))
    S.add(papa(470, 760, 1.05, expr="sourire", bras="main", regard=(-1, 0), flip=True, pas="marche"))
    S.add(samir(360, 770, 0.95, expr="content", bras="porte", regard=(1, -0.5), pas="marche",
                objet=boite_maamouls(0, -60, 0.55)))
    S.add(bulle(560, 130, 300, 80, "C'est joli, Noël.", 32, pointe=(380, 470)))
    S.cachette(40, 780)
    return S


def p07():
    """Plan moyen : bienvenue chez Émile ; le sapin tout nu attend."""
    S = Scene()
    salon_emile(S, 600)
    S.add(sapin(640, 620, 1.2))
    S.add(personne(470, 760, 1.15, expr="rire", bras="ouverts", regard=(-1, 0), **MAMAN_E))
    S.add(personne(600, 770, 1.1, expr="content", bras="hanches", regard=(-1, 0), **PAPI_E))
    S.add(emile(330, 790, 1.05, expr="rire", bras="saute", regard=(-1, 0)))
    S.add(papa(90, 780, 1.15, expr="sourire", bras="bas", regard=(1, 0)))
    S.add(samir(200, 790, 1.05, expr="timide", bras="porte", regard=(1, 0), objet=boite_maamouls(0, -60, 0.5)))
    S.add(bulle(330, 130, 300, 90, "Il est là !", 40, pointe=(330, 420)))
    S.cachette(770, 790)
    return S


def p08():
    """Plan large : on décore le sapin ; les guirlandes emmêlées."""
    S = Scene()
    salon_emile(S, 580)
    S.add(tapis(400, 720, 340, 56, "#ffc9c9", "#e03131"))
    S.add(sapin_decore(400, 640, 1.4, lumieres=False))
    S.add(emile(270, 760, 1.0, expr="rire", bras="tient", regard=(1, -0.5), objet=boule_noel(68, -150, 14, "#4dabf7")))
    S.add(samir(530, 760, 1.0, expr="rire", bras="tient", flip=True, regard=(-1, -0.5), objet=boule_noel(68, -150, 14, "#e03131")))
    # les deux papas et la guirlande lumineuse toute emmêlée
    S.add(papa(110, 790, 1.05, expr="rire", bras="large", regard=(1, 0)))
    S.add(personne(690, 790, 1.0, expr="rire", bras="large", flip=True, regard=(-1, 0), **PAPI_E))
    S.add(chemin("M 50 720 Q 160 640 230 720 Q 300 790 400 700 Q 480 640 560 730 Q 640 800 760 720", stroke=VERT, sw=4))
    S.add(guirlande_lumineuse(170, 690, 400, 700, creux=20, nb=6), guirlande_lumineuse(400, 700, 630, 690, creux=-20, nb=6, graine=3))
    S.add(chemin("M 380 760 c -30 -20 30 -30 10 -10 c -20 20 30 20 20 -6", stroke=VERT, sw=4))
    S.cachette(260, 70, "air")
    return S


def p09():
    """Gros plan : Samir pose l'étoile, perché sur l'escabeau."""
    S = Scene()
    salon_emile(S, 640)
    S.add(sapin_decore(430, 790, 1.45, etoile=None))
    S.add(escabeau(530, 790, 1.4))
    S.add(samir(530, 580, 1.2, expr="concentre", bras="haut", regard=(-1, -1),
                objet=etoile5(-76, -172, 28, OR_)))
    S.add(emile(680, 800, 1.15, expr="rire", bras="tend", flip=True, regard=(-1, -1)))
    S.add(paillettes(400, 330, 0.9))
    S.camera(1.3, 500, 470)
    S.dessus(bulle(220, 680, 300, 90, "C'est toi, l'invité.", 30, pointe=S.vers_page(700, 560)))
    S.cachette(60, 300, "air")
    return S


def p10():
    """Plan moyen : on goûte les maamouls ; « Choukrane ! »"""
    S = Scene()
    salon_emile(S, 600)
    S.add(sapin_decore(110, 610, 1.1, etoile=etoile5(0, 0, 22, OR_)))
    S.add(personne(560, 740, 1.2, expr="miam", bras="victoire", regard=(-1, 0), **PAPI_E))
    S.add(g([cercle(560 + dx, 740 - 175 * 1.2 + dy, 3, "#fff") for dx, dy in ((-14, 30), (8, 34), (16, 28), (-4, 36))]))
    S.add(personne(700, 750, 1.1, expr="rire", bras="mains_jointes", regard=(-1, 0), **MAMAN_E))
    S.add(table(420, 790, 420, 80, "#a0693a", nappe="#fff3bf"))
    S.add(boite_maamouls(420, 700, 0.9), maamoul(320, 702, 0.8), maamoul(520, 704, 0.8))
    S.add(samir(260, 800, 1.15, expr="rire", bras="leve_doigt", regard=(1, 0)))
    S.add(emile(400, 800, 1.1, expr="chante", bras="bouche", regard=(-1, 0)))
    S.add(bulle(330, 130, 320, 90, "Choukrane !", 40, pointe=(380, 460)))
    S.cachette(70, 670, "air")
    return S


def p11():
    """Plan large : l'Aïd chez Samir ; Émile est invité à son tour."""
    S = Scene()
    piece(S, "manoir", 580)
    S.ambiance("nuit")
    S.add(fenetre(300, 90, 200, 160, "#1c2a52", rideaux="#7048e8",
                  contenu=g([rect(0, 0, 800, 800, "#1c2a52"), croissant_soir(430, 140, 30),
                             *[cercle(320 + (k * 41) % 170, 100 + (k * 29) % 130, 2, "#fff") for k in range(10)]])))
    S.lumiere(430, 140, 90, "#fff3bf", 0.5)
    S.add(guirlande_fanions(10, 40, 790, 40, creux=24, nb=12, couleurs=("#7048e8", OR_, "#2b8a3e", "#e64980")))
    for lx in (120, 680):
        S.add(lanterne(lx, 80, 1.0, couleur="#9775fa", verre="#ffd43b"))
        S.lumiere(lx, 132, 120, "#ffd43b", 0.6)
    S.add(teta(400, 660, 1.15, expr="rire", bras="ouverts", regard=(0, 0.3)))
    S.add(table(400, 760, 560, 110, "#a0693a", nappe="#e5dbff"))
    S.add(boite_maamouls(300, 640, 0.8), boite_maamouls(500, 640, 0.8))
    S.add(personne(650, 790, 1.1, expr="rire", bras="mains_jointes", flip=True, regard=(-1, 0), **MAMAN_E))
    S.add(papa(130, 790, 1.15, expr="rire", bras="hanches", regard=(1, 0), habit="#ffffff"))
    S.add(emile(500, 800, 1.0, expr="joie", bras="tient", regard=(-1, -0.5), objet=boite_etoiles(68, -146, 0.6)))
    S.add(samir(280, 800, 1.0, expr="rire", bras="ouverts", regard=(1, 0), habit="#ffffff", jambes="#7048e8"))
    S.cachette(770, 790)
    return S


def biscuit_etoile(x, y, s=1.0):
    return place([etoile5(0, 0, 18, "#e3a857"), etoile5(0, 0, 8, "#f6c453")], x, y, s)


def boite_etoiles(x, y, s=1.0):
    """Boîte de biscuits de Noël en forme d'étoile ; (x, y) = milieu du fond."""
    m = [rect(-70, -40, 140, 40, volume(VERT, 0.3, 0.75), rx=6),
         *[biscuit_etoile(-46 + k * 31, -42 - (k % 2) * 6, 0.9) for k in range(4)],
         rect(-70, -26, 140, 26, VERT, rx=6), chemin("M -70 -16 H 70", stroke="#e03131", sw=4)]
    return place(m, x, y, s)


def p12():
    """Plan moyen : deux fêtes, deux fois plus de gâteaux."""
    S = Scene()
    piece(S, "manoir", 600)
    S.ambiance("interieur")
    S.add(guirlande_fanions(10, 40, 790, 40, creux=24, nb=12, couleurs=("#7048e8", OR_, "#2b8a3e", "#e64980")))
    S.add(lanterne(120, 80, 1.0, couleur="#9775fa"), lanterne(680, 80, 1.0, couleur="#9775fa"))
    S.add(samir(310, 790, 1.4, expr="rire", bras="epaule", regard=(1, 0), habit="#ffffff", jambes="#7048e8"))
    S.add(emile(500, 790, 1.4, expr="rire", bras="donne", flip=True, regard=(-1, 0), objet=boite_etoiles(84, -92, 0.55)))
    S.add(maamoul(*mains_personne(310, 790, 1.4, "epaule")[0], 1.0))
    S.add(bulle(400, 130, 460, 100, "Une fête chez toi,\nune fête chez moi !", 34, pointe=(330, 430)))
    S.cachette(770, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("maamouls-seuls.svg", vignette),
    ("01-en-decembre.svg", p01), ("02-chez-nous.svg", p02), ("03-chez-moi.svg", p03),
    ("04-l-invitation.svg", p04), ("05-les-maamouls.svg", p05), ("06-dans-la-rue.svg", p06),
    ("07-bienvenue.svg", p07), ("08-le-sapin.svg", p08), ("09-l-etoile.svg", p09),
    ("10-choukrane.svg", p10), ("11-l-aid.svg", p11), ("12-deux-fetes.svg", p12),
]
