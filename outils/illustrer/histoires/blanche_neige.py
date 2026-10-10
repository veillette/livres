"""Blanche-Neige — d'après les frères Grimm, en version douce.

La reine demande chaque jour à son miroir qui est la plus belle. Un jour, le
miroir répond : Blanche-Neige. Jalouse, la reine ordonne au chasseur
d'emmener la jeune fille au fond de la forêt ; le chasseur, au bon cœur, la
laisse partir. Les animaux la guident jusqu'à une petite maison où tout est
petit : celle des sept nains, qui rentrent de la mine et l'accueillent. La
reine, déguisée en vieille marchande, lui offre une pomme ; Blanche-Neige y
croque et tombe dans un profond sommeil. Les nains veillent sur elle. Un
prince passe ; en la soulevant, le morceau de pomme tombe de sa bouche, et
elle se réveille (comme chez Grimm, sans baiser). La reine s'enfuit si loin
qu'on ne la revoit jamais, et l'on danse dans la forêt.

Plans : 1 moyen (le miroir) · 2 moyen (le jardin et les oiseaux) · 3 gros
plan (la reine jalouse) · 4 moyen (le chasseur) · 5 large (la forêt) · 6
moyen (la petite maison) · 7 large (les nains rentrent) · 8 moyen (on
danse) · 9 moyen (la vieille marchande) · 10 large (les nains veillent) ·
11 moyen (le réveil) · 12 large (la fête).
"""
from contes import *

ID = "blanche-neige"

BLANCHE = dict(coiffure="carre", cheveux="noir", peau="claire", habit="#1c7ed6", motif_robe="#ffe066", stature="ado", yeux="cils",
               acc=("noeud",), couleur_acc="#e03131")
REINE_ = dict(stature="adulte", peau="claire", cheveux="noir", coiffure="chignon", habit="#5f3dc4", cape="#212529", nez="pointu",
              acc=("grande_couronne",), carrure="fine", yeux="cils")
MARCHANDE = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="sorciere", habit="#495057", cape="#343a40", nez="long",
                 carrure="fine")
CHASSEUR = dict(stature="adulte", peau="doree", cheveux="brun", coiffure="courts", habit="#2b8a3e", robe=False, jambes="#795548",
                barbe="#4a2c17", carrure="ronde")
PRINCE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="boucles", habit="#c92a2a", robe=False, jambes="#f8f9fa",
              cape="#1864ab", acc=("couronne",))
COULEURS_NAINS = ("#e03131", "#f08c00", "#fab005", "#40c057", "#1c7ed6", "#7048e8", "#c2255c")
PEAUX_NAINS = ("rosee", "doree", "claire", "brune", "rosee", "foncee", "claire")
BARBES = ("#e9ecef", "#adb5bd", "#e8590c", "#495057", "#f8f9fa", "#868e96", "#8d5524")


def blanche(x, y, s=1.45, **k):
    return personne(x, y, s, **{**BLANCHE, **k})


def reine_(x, y, s=1.5, **k):
    return personne(x, y, s, **{**REINE_, **k})


def nain(i, x, y, s=1.0, **k):
    d = dict(stature="petit", peau=PEAUX_NAINS[i], cheveux="blanc" if i % 2 else "brun", coiffure="chauve_cote", habit=COULEURS_NAINS[i],
             robe=False, jambes="#795548", barbe=BARBES[i], acc=("bonnet_nuit",), couleur_acc=COULEURS_NAINS[(i + 3) % 7],
             carrure="ronde" if i % 3 == 0 else "normale", nez=("rond", "long", "retrousse", "rond", "pointu", "rond", "long")[i])
    return personne(x, y, s, **{**d, **k})


def pioche(x, y, s=1.0, rot=0):
    return place([trait(0, 30, 0, -60, "#8d5524", 6), chemin("M -40 -50 Q 0 -76 40 -50", stroke="#868e96", sw=8)], x, y, s, rot=rot)


def visage_miroir(content=True):
    """Le visage qui parle dans le miroir (repère du miroir)."""
    return g([ellipse(0, -250, 60, 80, "#d0ebff", opacity=0.8), ellipse(-20, -270, 10, 6, "#4dabf7"), ellipse(20, -270, 10, 6, "#4dabf7"),
              chemin("M -20 -220 Q 0 -206 20 -220" if content else "M -20 -214 Q 0 -226 20 -214", stroke="#4dabf7", sw=4)])


def chambre_reine(S):
    piece(S, "chateau", y=600)
    S.ambiance("soir")


def maisonnette(x, y, s=1.0):
    m = [rect(-170, -200, 340, 200, volume("#f4e6cc", 0.2, 0.85)), poly([(-200, -190), (0, -330), (200, -190)], "#a0693a"),
         rect(-30, -120, 60, 120, "#8d5524", rx=26), cercle(16, -60, 5, OR)]
    for k, px in enumerate((-130, -80, 80, 130)):
        m.append(rect(px - 18, -160, 36, 36, "#ffe066", stroke="#8d5524", stroke_width=4))
    m.append(rect(80, -330, 30, 80, "#868e96"))
    return place(m, x, y, s)


def petit_lit(x, y, s=1.0, couleur="#ff8787"):
    return place([rect(-50, -70, 100, 70, "#c68642", rx=6), rect(-46, -60, 92, 30, "#fff", rx=6), rect(-46, -40, 92, 30, couleur, rx=6),
                  rect(-56, -90, 14, 90, "#a0693a", rx=5), rect(42, -80, 14, 80, "#a0693a", rx=5)], x, y, s)


def lit_fleurs(S, x, y, s=1.0):
    m = [ellipse(0, 0, 220, 40, "#69db7c")]
    r = random.Random(4)
    for k in range(24):
        m.append(cercle(r.uniform(-200, 200), r.uniform(-24, 24), 9, r.choice(("#ffd43b", "#f783ac", "#fff", "#b197fc"))))
    S.add(place(m, x, y, s))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret(S, y=600, graine=3)
    S.add(maisonnette(620, 600, 0.8))
    S.add(blanche(330, 790, 1.7, expr="rire", bras="ouverts", regard=(0, -0.5)))
    S.add(oiseau(160, 300, 0.7, "#4dabf7", ailes="haut"), oiseau(500, 260, 0.6, "#ffd43b", ailes="haut", flip=True))
    for k in range(3):
        S.add(nain(k, 540 + k * 80, 790, 0.85, expr="rire", bras="haut" if k % 2 else "salut"))
    S.cachette(60, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(miroir(200, 262, 0.7, visage_miroir()))
    return S


def p01():
    """Plan moyen : au château, la reine interroge son miroir : « Miroir, mon beau miroir, qui est la plus belle ? »"""
    S = Scene()
    chambre_reine(S)
    S.add(miroir(560, 790, 1.4, visage_miroir()))
    S.add(reine_(260, 790, 1.55, expr="fier", bras="hanches", regard=(1, 0)))
    S.add(bulle(300, 140, 480, 110, "Miroir, mon beau miroir,\nqui est la plus belle ?", 32, pointe=(270, 300)))
    return S


def p02():
    """Plan moyen : dans le jardin du château, Blanche-Neige chante et les oiseaux viennent se poser près d'elle."""
    S = Scene()
    jardin_chateau(S, chateau_x=640, chateau_s=0.55)
    S.add(blanche(320, 790, 1.55, expr="chante", bras="ouverts", regard=(1, -0.5)))
    for x, y, c, f in ((150, 400, "#4dabf7", False), (480, 380, "#ffd43b", True), (520, 500, "#ff8787", True)):
        S.add(oiseau(x, y, 0.6, c, ailes="haut", flip=f))
    S.add(notes(420, 300, 1.0, "#7048e8"))
    return S


def p03():
    """Gros plan : le miroir répond : « Blanche-Neige est mille fois plus belle. » ; la reine devient verte de jalousie."""
    S = Scene()
    chambre_reine(S)
    S.add(miroir(590, 860, 1.6, visage_miroir(False)))
    S.add(reine_(280, 880, 1.8, expr="furieux", bras="poing", regard=(1, 0)))
    S.camera(1.12, 420, 520)
    S.dessus(bulle(560, 120, 420, 110, "Blanche-Neige est mille fois\nplus belle que vous !", 28, pointe=(600, 230)))
    return S


def p04():
    """Plan moyen : au bord de la forêt, le chasseur, au bon cœur, dit à Blanche-Neige : « Fuis, et ne reviens pas ! »"""
    S = Scene()
    foret(S, y=600, graine=4)
    S.add(personne(560, 790, 1.6, expr="triste", bras="designe", flip=True, regard=(-1, 0), **CHASSEUR))
    S.add(blanche(260, 790, 1.5, expr="inquiet", bras="mains_jointes", regard=(1, -0.2)))
    S.add(bulle(560, 150, 380, 110, "Fuis, petite, et ne\nreviens pas au château !", 30, pointe=(560, 310)))
    return S


def p05():
    """Plan large : seule dans la forêt sombre, Blanche-Neige est guidée par un lapin, un écureuil et des oiseaux."""
    S = Scene()
    foret(S, y=600, graine=5, sombre=True)
    S.add(blanche(330, 790, 1.5, expr="inquiet", bras="bas", regard=(1, 0.3)))
    S.add(perso("lapin", 560, 790, 0.6, expr="content", bras="designe", flip=True), perso("ecureuil", 650, 790, 0.5, expr="content", bras="salut"))
    S.add(oiseau(520, 380, 0.6, "#ffd43b", ailes="haut"))
    for x, y in ((120, 360), (700, 300)):
        S.add(luciole(x, y, 0.8))
    S.add(texte(400, 120, "Par ici !", 52, "#ffd43b", contour="#364fc7"))
    return S


def p06():
    """Plan moyen : dans la petite maison, sept petites assiettes, sept petites chaises, sept petits lits ; Blanche-Neige s'endort."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(fenetre(580, 110, 150, 140, "#a5d8ff", rideaux="#ffc9c9"))
    S.add(table(300, 600, 440, 100, nappe="#fff3bf"))
    for k in range(7):
        S.add(ellipse(110 + k * 64, 486, 22, 6, "#fff", stroke="#dee2e6", stroke_width=2), rect(126 + k * 64, 466, 12, 16, COULEURS_NAINS[k], rx=3))
    for k in range(3):
        S.add(petit_lit(230 + k * 170, 800, 1.6, COULEURS_NAINS[k + 2]))
    S.add(place(personne(0, 0, 1.0, expr="dort", bras="bas", **BLANCHE), 590, 700, 1.05, rot=-90))
    S.add(zzz(260, 600, 0.9))
    S.add(texte(400, 120, "Tout est tout petit !", 48, "#a0693a", contour="#fff"))
    return S


def p07():
    """Plan large : le soir, les sept nains rentrent de la mine en file, pioche sur l'épaule : « Qui dort dans nos lits ? »"""
    S = Scene()
    foret(S, y=600, graine=6)
    S.ambiance("soir")
    S.add(maisonnette(660, 600, 0.75))
    for k in range(7):
        S.add(nain(k, 60 + k * 82, 790 - (k % 2) * 10, 0.95, expr="surpris" if k > 4 else "content", bras="porte",
                   objet=pioche(-20, -90, 0.6, rot=-30)))
    S.add(bulle(400, 160, 380, 90, "Qui dort dans nos lits ?", 32, pointe=(560, 560)))
    return S


def p08():
    """Plan moyen : dans la petite maison, Blanche-Neige danse avec les nains ; un nain joue de l'accordéon."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(blanche(400, 790, 1.5, expr="rire", bras="ouverts", regard=(0, 0)))
    for k, (x, b) in enumerate(((130, "haut"), (240, "danse"), (560, "danse"), (670, "haut"))):
        S.add(nain(k, x, 790, 0.95, expr="rire", bras=b, flip=x > 400))
    S.add(notes(400, 300, 1.2, "#e8590c"))
    S.add(bulle(400, 130, 360, 90, "N'ouvre à personne !", 32, pointe=(640, 540)))
    S.cachette(70, 220, "air")
    return S


def p09():
    """Plan moyen : à la fenêtre, une vieille marchande (la reine déguisée) tend une pomme rouge : « Une belle pomme, ma jolie ? »"""
    S = Scene()
    foret(S, y=600, graine=7)
    S.add(maisonnette(240, 600, 0.9))
    S.add(blanche(200, 790, 1.4, expr="content", bras="tend", regard=(1, 0)))
    S.add(personne(560, 790, 1.55, expr="malin", bras="donne", flip=True, regard=(-1, 0),
                   objet=pomme(*ancre(84, -92, "donne", "ancien", "fine"), 1.0), **MARCHANDE))
    S.add(bulle(560, 150, 380, 90, "Une belle pomme, ma jolie ?", 30, pointe=(560, 330)))
    return S


def p10():
    """Plan large : Blanche-Neige a croqué la pomme et dort profondément sur un lit de fleurs ; les sept nains la veillent."""
    S = Scene()
    foret(S, y=600, graine=8)
    for k in range(7):
        x = 100 + k * 100
        S.add(nain(k, x, 650 if k % 2 else 640, 0.72, expr="triste", bras="mains_jointes"))
    lit_fleurs(S, 400, 730, 1.1)
    S.add(place(personne(0, 0, 1.0, expr="dort", bras="bas", **BLANCHE), 560, 720, 1.05, rot=-90))
    return S


def p11():
    """Plan moyen : un prince soulève Blanche-Neige ; le morceau de pomme tombe de sa bouche ; elle ouvre les yeux."""
    S = Scene()
    foret(S, y=600, graine=9)
    lit_fleurs(S, 400, 720, 1.0)
    S.add(personne(560, 790, 1.55, expr="joie", bras="tend", flip=True, regard=(-1, 0.3), **PRINCE))
    S.add(blanche(330, 790, 1.45, expr="bouche_bee", bras="bas", regard=(1, 0)))
    S.add(pomme(300, 760, 0.5))
    S.add(nain(4, 120, 790, 0.85, expr="joie", bras="haut"), nain(6, 720, 800, 0.8, expr="joie", bras="haut", flip=True))
    S.add(bulle(340, 150, 260, 80, "Où suis-je ?", 34, pointe=(330, 320)))
    S.cachette(70, 520, "air")
    return S


def p12():
    """Plan large : grande fête dans la clairière ; Blanche-Neige, le prince et les sept nains dansent."""
    S = Scene()
    foret(S, y=600, graine=10)
    for k in range(6):
        S.add(cercle(110 + k * 115, 180 + (k % 2) * 20, 16, COULEURS_NAINS[k]))
    S.add(chemin("M 80 170 Q 400 230 720 170", stroke="#868e96", sw=2))
    S.add(personne(330, 790, 1.45, expr="rire", bras="main", regard=(1, 0), **PRINCE))
    S.add(blanche(480, 790, 1.4, expr="rire", bras="main", flip=True, regard=(-1, 0)))
    for k, x in enumerate((60, 150, 240, 580, 660, 740)):
        S.add(nain(k, x, 800 if k % 2 else 790, 0.75, expr="rire", bras=("haut", "danse", "applaudit")[k % 3], flip=x > 400))
    S.cachette(730, 540, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("miroir-seul.svg", vignette),
    ("01-le-miroir.svg", p01), ("02-les-oiseaux.svg", p02), ("03-la-jalousie.svg", p03),
    ("04-le-chasseur.svg", p04), ("05-la-foret.svg", p05), ("06-la-petite-maison.svg", p06),
    ("07-les-sept-nains.svg", p07), ("08-on-danse.svg", p08), ("09-la-pomme.svg", p09),
    ("10-le-sommeil.svg", p10), ("11-le-reveil.svg", p11), ("12-la-fete.svg", p12),
]
