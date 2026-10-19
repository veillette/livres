"""Le corbeau et la lumière — d'après une légende haïda de la côte Nord-Ouest.

Au commencement, le monde est tout noir. Un vieux chef garde la lumière
dans des boîtes de cèdre, rangées les unes dans les autres, au fond de sa
maison longue. Corbeau, qui est alors blanc comme la neige, veut la
lumière pour tout le monde. Il se change en petit enfant que la fille du
chef recueille ; le grand-père l'adore et ne lui refuse rien. L'enfant
pleure pour avoir les boîtes : de la première sortent les étoiles, qu'il
lance par le trou à fumée ; de la deuxième, la lune ; de la dernière, le
soleil. Alors il redevient Corbeau, saisit le soleil et s'envole par le
trou à fumée : la suie le rend tout noir. Depuis, le soleil éclaire le
monde, et le corbeau est noir.

Plans : 1 large (le monde noir) · 2 moyen (la maison du chef) · 3 moyen
(l'enfant recueilli) · 4 gros plan (« La boîte ! ») · 5 moyen (les
étoiles) · 6 moyen (la lune) · 7 gros plan (le soleil) · 8 large (l'envol)
· 9 large (le monde éclairé).
"""
from contes import *
from base import _assombrir

ID = "corbeau-lumiere"

ROUGE = "#c92a2a"
NOIR = "#212529"
CEDRE = "#a0522d"
CHEF = dict(stature="ancien", peau="brune", cheveux="gris", coiffure="longs", habit="#343a40", robe=True, cape=ROUGE, carrure="ronde",
            nez="long", ceinture=ROUGE)
FILLE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="tresses", habit="#1864ab", robe=True, cape="#e03131", nez="petit",
             carrure="fine")
ENFANT = dict(stature="petit", peau="brune", cheveux="noir", coiffure="courts", habit="#f1f3f5", robe=False, jambes="#868e96", yeux="petits")


def corbeau_h(x, y, s=1.0, blanc=False, ailes="bas", expr="malin", flip=False, rot=0, regard=(0, 0)):
    """Corbeau : tout blanc au début de l'histoire, noir à la fin ; (x, y) = sous les pattes."""
    if not blanc:
        return corbeau(x, y, s, expr=expr, ailes=ailes, flip=flip, rot=rot, regard=regard)
    ys, bs, ss = EXPRESSIONS[expr]
    m = [oiseau(0, 0, 1.0, "#f1f3f5", "#ffffff", expr=expr, ailes=ailes, regard=regard),
         poly([(-13, -74), (13, -74), (0, -44)], "#495057")]
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 75 * s, y - 180 * s, x + 75 * s, y)


def corbeau_vol(x, y, s=1.0, blanc=False, flip=False, objet=None, rot=0):
    """Corbeau en plein vol, ailes déployées ; (x, y) = centre du corps ; objet tenu sous le bec."""
    c = "#f1f3f5" if blanc else "#343a40"
    f = "#ced4da" if blanc else NOIR
    m = [chemin("M -10 -10 Q -90 -110 -190 -60 Q -120 -40 -100 0 Q -60 -10 -10 10 Z", volume(f, 0.3, 0.8)),
         chemin("M -60 -60 L -150 -66 M -60 -40 L -130 -30", stroke=_assombrir(f, 0.7), sw=2, opacity=0.6),
         poly([(-60, 10), (-140, 40), (-130, 0)], f),
         ellipse(0, 0, 70, 36, volume(c, 0.3, 0.8)),
         chemin("M 10 -10 Q 80 -120 180 -90 Q 120 -60 110 -10 Q 70 -10 20 10 Z", volume(c, 0.3, 0.85)),
         cercle(70, -14, 30, volume(c, 0.3, 0.8)), cercle(80, -20, 9, "#fff"), cercle(82, -20, 5, ENCRE),
         poly([(94, -20), (140, -4), (96, -2)], "#495057")]
    if objet:
        m.append(objet)
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 190 * s, y - 120 * s, x + 190 * s, y + 60 * s)


def boule_lumiere(x, y, r=40, couleur="#ffd43b", S=None, force=0.8):
    """Une boule de lumière (soleil, lune) tenue ou lancée."""
    if S is not None:
        S.lumiere(x, y, r * 3.2, couleur, force)
    return g([cercle(x, y, r * 2, radial([(0.4, couleur, 0.5), (1, couleur, 0)])), cercle(x, y, r, radial([(0, "#fffbe6"), (0.6, couleur), (1, _assombrir(couleur, 0.92))]))])


def ovoide(x, y, w, h, c=NOIR, c2=ROUGE):
    """Motif « formline » de la côte Nord-Ouest : un ovoïde et son œil."""
    return g([chemin(f"M {x - w} {y + h * 0.3} Q {x - w} {y - h} {x} {y - h} Q {x + w} {y - h} {x + w} {y + h * 0.3} Q {x} {y + h * 0.2} {x - w} {y + h * 0.3} Z", c),
              ellipse(x, y - h * 0.3, w * 0.55, h * 0.4, "#f8f9fa"), ellipse(x, y - h * 0.3, w * 0.3, h * 0.25, c2)])


def boite_cedre(x, y, s=1.0, ouverte=False, lueur_=None):
    """Boîte de cèdre peinte ; (x, y) = milieu du fond."""
    m = [rect(-90, -150, 180, 150, volume(CEDRE, 0.3, 0.8), rx=6), planches(-90, -150, 180, 150, CEDRE, larg=30),
         ovoide(-42, -80, 34, 34), ovoide(42, -80, 34, 34), chemin("M -60 -30 Q 0 0 60 -30", stroke=ROUGE, sw=10),
         rect(-90, -150, 180, 10, NOIR)]
    if ouverte:
        m += [poly([(-96, -150), (96, -150), (110, -200), (-80, -190)], volume(_assombrir(CEDRE, 0.85), 0.3, 0.8))]
    else:
        m.append(rect(-98, -170, 196, 24, volume(_assombrir(CEDRE, 0.85), 0.3, 0.8), rx=4))
    if lueur_:
        m.append(ellipse(0, -150, 80, 16, lueur_, opacity=0.9))
    return place(m, x, y, s)


def totem(x, y, s=1.0, h=520):
    """Mât totémique : visages sculptés empilés, corbeau en haut ; (x, y) = pied du mât."""
    m = [rect(-46, -h, 92, h, cylindre(CEDRE, 0.25, 0.75))]
    nb = int(h // 130)
    for k in range(nb):
        yy = -60 - k * 130
        m += [ovoide(-20, yy - 30, 18, 18), ovoide(20, yy - 30, 18, 18), rect(-30, yy, 60, 16, ROUGE, rx=6),
              poly([(-6, yy - 20), (6, yy - 20), (0, yy + 2)], "#2b8a3e"), trait(-46, yy + 30, 46, yy + 30, NOIR, 4)]
    m += [poly([(-46, -h), (0, -h - 70), (46, -h)], NOIR), poly([(10, -h - 40), (90, -h - 20), (10, -h - 14)], NOIR),
          chemin(f"M -46 {-h + 10} Q -120 {-h - 30} -150 {-h + 30} L -46 {-h + 60} Z", NOIR),
          chemin(f"M 46 {-h + 10} Q 120 {-h - 30} 150 {-h + 30} L 46 {-h + 60} Z", NOIR)]
    return place(m, x, y, s)


def maison_longue(x, y, s=1.0, lueur_=False):
    """Maison de planches de cèdre, façade peinte, trou à fumée ; (x, y) = milieu du seuil."""
    m = [poly([(-260, 0), (-260, -220), (0, -320), (260, -220), (260, 0)], volume(CEDRE, 0.3, 0.8)),
         planches(-260, -320, 520, 320, CEDRE, forme=poly([(-260, 0), (-260, -220), (0, -320), (260, -220), (260, 0)], "#000"), larg=34),
         chemin("M -280 -220 L 0 -330 L 280 -220", stroke=NOIR, sw=16),
         ovoide(-120, -170, 60, 50), ovoide(120, -170, 60, 50), chemin("M -170 -90 Q 0 -10 170 -90", stroke=ROUGE, sw=16),
         ellipse(0, -60, 40, 60, NOIR)]
    if lueur_:
        m += [ellipse(0, -60, 30, 50, "#ffd43b", opacity=0.85), rect(-20, -334, 40, 14, "#ffd43b", opacity=0.8)]
        for k in range(5):
            m.append(trait(-200 + k * 100, -40, -200 + k * 100, -200, "#ffd43b", 2, opacity=0.6))
    return place(m, x, y, s)


def cotes(S, horizon=520, nuit_=False, eclaire=True, etoiles_=False):
    """La côte Nord-Ouest : montagnes, forêt de cèdres, mer, plage de galets ;
    la nuit d'avant les étoiles n'a pas une seule étoile (etoiles_=False)."""
    if nuit_ and etoiles_:
        nuit(S, "#0b0f1f", "#1f2747")
    elif nuit_:
        S.add(rect(0, 0, 800, 800, lineaire([(0, "#0b0f1f"), (1, "#1f2747")])))
        S.ambiance("nuit")
    else:
        ciel(S, "#74c0fc", "#fff3bf")
    lointain(S, horizon - 20, "#5c7cfa" if eclaire else "#2b3150", 160, graine=4, opacite=0.6)
    S.add(rect(0, horizon, 800, 120, lineaire([(0, "#1c7ed6" if eclaire else "#1b2440"), (1, "#4dabf7" if eclaire else "#222b4a")])))
    for k in range(9):
        S.add(sapin(40 + k * 95, horizon + 10, 0.55 + (k % 3) * 0.12, couleur="#2b8a3e" if eclaire else "#16222c",
                    couleur2="#2f9e44" if eclaire else "#1c2a36"))


def plage(S, y=640, eclaire=True):
    c = "#ced4da" if eclaire else "#3b4256"
    S.add(chemin(f"M 0 {y} Q 400 {y - 30} 800 {y} L 800 800 L 0 800 Z", terrain(c)))
    r = random.Random(4)
    for _ in range(40):
        S.add(ellipse(r.uniform(0, 800), r.uniform(y + 10, 800), r.uniform(4, 10), r.uniform(3, 6), _assombrir(c, 0.85)))


def maison_dedans(S, feu_=True):
    """Intérieur de la maison longue, la nuit : planches de cèdre, feu au centre, trou à fumée."""
    interieur(S, "#8d5524", "#6d4424", 560, plinthe="#4a2c17")
    S.add(planches(0, 0, 800, 560, "#8d5524", larg=40))
    S.add(rect(320, 0, 160, 40, "#0b0f1f"), rect(300, 36, 200, 14, NOIR))
    S.ambiance("nuit")
    if feu_:
        S.add(ellipse(400, 720, 120, 22, "#495057"))
        S.add(flammes(400, 720, 1.1, graine=2))
        S.lumiere(400, 660, 320, "#ffa94d", 0.7)
    for x in (110, 690):
        S.add(ovoide(x, 220, 60, 50))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cotes(S, 560)
    plage(S, 700)
    S.add(totem(120, 780, 0.9, h=520))
    S.add(corbeau_vol(450, 330, 1.25, objet=boule_lumiere(150, 10, 46)))
    S.lumiere(640, 340, 180, "#ffd43b", 0.6)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(corbeau_vol(170, 150, 0.7, objet=boule_lumiere(150, 10, 40)))
    return S


def p01():
    """Plan large : au commencement, tout est noir ; on devine à peine la forêt ; Corbeau, tout blanc, cherche son chemin à tâtons."""
    S = Scene()
    cotes(S, 520, nuit_=True, eclaire=False)
    plage(S, 640, eclaire=False)
    S.add(corbeau_h(400, 760, 1.6, blanc=True, expr="inquiet", ailes="ouvertes"))
    S.add(texte(400, 200, "Tout est noir…", 54, "#adb5bd", contour="#0b0f1f"))
    S.cachette(None)  # dans le noir complet, la petite bête n'a pas encore de lumière pour se montrer
    return S


def p02():
    """Plan moyen : au bord de la rivière, la maison du vieux chef ; un peu de lumière filtre par les fentes des planches ; Corbeau la regarde."""
    S = Scene()
    cotes(S, 480, nuit_=True, eclaire=False)
    plage(S, 620, eclaire=False)
    S.add(maison_longue(460, 700, 0.95, lueur_=True))
    S.lumiere(460, 640, 140, "#ffd43b", 0.6)
    S.lumiere(460, 390, 80, "#ffd43b", 0.5)
    S.add(totem(150, 720, 0.75, h=520))
    S.add(corbeau_h(700, 780, 1.0, blanc=True, expr="malin", flip=True, regard=(-1, -0.2)))
    S.cachette(None)  # monde encore sans lumière
    return S


def p03():
    """Plan moyen : dans la maison, près du feu, la fille du chef berce un petit enfant aux yeux brillants (c'est Corbeau !) ; le grand-père sourit."""
    S = Scene()
    maison_dedans(S)
    S.add(boite_cedre(640, 560, 0.6), boite_cedre(640, 470, 0.45))
    S.add(personne(230, 790, 1.35, expr="content", bras="calin", regard=(1, 0.3), **FILLE))
    S.add(personne(248, 650, 0.75, expr="malin", bras="bas", regard=(1, 0), **ENFANT))
    S.add(personne(560, 790, 1.35, expr="rire", bras="ventre", flip=True, regard=(-1, 0), **CHEF))
    S.cachette(60, 790)
    return S


def p04():
    """Gros plan : l'enfant pleure, pleure, et montre du doigt les boîtes de cèdre : « La boîte ! Je veux la boîte ! »"""
    S = Scene()
    maison_dedans(S)
    S.add(boite_cedre(600, 640, 1.0))
    S.add(personne(320, 780, 1.6, expr="pleure", bras="designe", larmes=True, regard=(1, 0), **ENFANT))
    S.camera(1.5, 430, 560)
    S.dessus(bulle(400, 110, 520, 90, "La boîte ! Je veux la boîte !", 34))
    S.cachette(150, 790)
    return S


def p05():
    """Plan moyen : le grand-père ouvre la première boîte : des étoiles en sortent ; l'enfant les lance par le trou à fumée."""
    S = Scene()
    maison_dedans(S, feu_=False)
    S.add(boite_cedre(520, 760, 0.9, ouverte=True, lueur_="#fff3bf"))
    for k, (x, y) in enumerate(((420, 60), (360, 160), (470, 210), (300, 260), (430, 320), (520, 120))):
        S.add(etoile5(x, y, 16 - (k % 3) * 3, "#ffe066"))
        S.lumiere(x, y, 40, "#fff3bf", 0.5)
    S.lumiere(520, 620, 180, "#fff3bf", 0.6)
    S.add(personne(640, 790, 1.3, expr="sourire", bras="tend", flip=True, regard=(-1, -0.3), **CHEF))
    S.add(personne(270, 790, 1.2, expr="rire", bras="lance", regard=(1, -1), **ENFANT))
    S.add(texte(160, 180, "Hop !", 50, "#fff3bf", contour="#4a2c17"))
    S.cachette(60, 790)
    return S


def p06():
    """Plan moyen : dans la deuxième boîte, la lune ; l'enfant la lance par le trou à fumée, et elle monte dans le ciel."""
    S = Scene()
    maison_dedans(S)
    S.add(boite_cedre(560, 760, 0.8, ouverte=True))
    S.add(boule_lumiere(400, 90, 50, "#fff3bf", S=S, force=0.6))
    S.add(mouvement(400, 200, 1.4, "#fff3bf", rot=-90))
    S.add(personne(280, 790, 1.35, expr="joie", bras="saute", regard=(1, -1), **ENFANT))
    S.add(personne(640, 790, 1.3, expr="surpris", bras="surprise", flip=True, regard=(-1, -0.6), **CHEF))
    S.add(personne(130, 790, 1.2, expr="bouche_bee", bras="joues", regard=(1, -0.5), **FILLE))
    S.cachette(730, 70, "air")
    return S


def p07():
    """Gros plan : la toute dernière boîte s'ouvre : le soleil ! Une lumière éblouissante remplit la maison."""
    S = Scene()
    maison_dedans(S, feu_=False)
    S.ambiance("interieur")
    S.add(boite_cedre(400, 760, 1.2, ouverte=True))
    S.add(boule_lumiere(400, 450, 90, "#ffd43b", S=S, force=0.9))
    for k in range(16):
        a = k * math.pi / 8
        S.add(trait(400 + math.cos(a) * 120, 450 + math.sin(a) * 120, 400 + math.cos(a) * 260, 450 + math.sin(a) * 260, "#ffe066", 10, opacity=0.6))
    S.camera(1.3, 400, 500)
    S.dessus(texte(400, 100, "Le soleil !", 60, "#e8590c", contour="#fff3bf"))
    S.cachette(140, 790)
    return S


def p08():
    """Plan large : l'enfant est redevenu Corbeau ; le soleil dans le bec, il s'envole par le trou à fumée ; la suie noircit ses plumes blanches."""
    S = Scene()
    cotes(S, 520, nuit_=True, eclaire=False, etoiles_=True)
    plage(S, 640, eclaire=False)
    S.add(lune(130, 130, 34))
    S.add(maison_longue(420, 760, 0.85))
    for k in range(6):
        S.add(cercle(420 + (k % 2) * 30 - 15, 460 - k * 40, 20 + k * 4, "#495057", opacity=0.6))
    S.add(corbeau_vol(500, 200, 1.0, rot=-12, objet=boule_lumiere(150, 10, 40, S=None)))
    S.lumiere(640, 200, 260, "#ffd43b", 0.8)
    S.add(texte(250, 120, "Corbeau devient noir !", 38, "#fff3bf", contour="#0b0f1f"))
    S.cachette(740, 790)
    return S


def p09():
    """Plan large : le soleil brille sur la mer, les cèdres et les montagnes ; les gens du village sortent dans la lumière ; Corbeau, tout noir, plane, fier."""
    S = Scene()
    cotes(S, 520)
    S.add(soleil(630, 140, 60))
    plage(S, 640)
    S.add(totem(90, 760, 0.7, h=520))
    S.add(corbeau_vol(330, 220, 0.75))
    S.add(personne(300, 790, 1.0, peau="brune", cheveux="noir", coiffure="couettes", habit="#fab005", robe=True, expr="rire", bras="saute", regard=(0, -1)))
    S.add(personne(480, 790, 1.15, expr="content", bras="ouverts", flip=True, regard=(-1, -0.5), **FILLE))
    S.add(personne(680, 790, 1.15, expr="rire", bras="applaudit", flip=True, regard=(-1, -0.5), **CHEF))
    S.cachette(140, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("corbeau-seul.svg", vignette),
    ("01-tout-est-noir.svg", p01), ("02-la-maison-du-chef.svg", p02), ("03-l-enfant.svg", p03),
    ("04-la-boite.svg", p04), ("05-les-etoiles.svg", p05), ("06-la-lune.svg", p06),
    ("07-le-soleil.svg", p07), ("08-l-envol.svg", p08), ("09-la-lumiere.svg", p09),
]
