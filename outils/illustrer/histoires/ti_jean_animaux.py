"""Ti-Jean et les animaux — un conte de tradition québécoise.

Ti-Jean, le plus jeune de trois frères, part chercher fortune avec Pierre et
Jacques. En chemin, ses frères veulent écraser une fourmilière, attraper
les canards du lac et secouer l'arbre des abeilles pour voler leur miel ;
chaque fois, Ti-Jean les en empêche. Au château, le roi propose trois
épreuves : ramasser avant le soir les mille perles du collier de la
princesse, perdues dans la mousse ; rapporter la clé d'or tombée au fond du
lac ; et, parmi trois princesses pareilles comme trois gouttes d'eau,
reconnaître la plus jeune, qui a mangé une cuillerée de sirop d'érable. Les
fourmis, les canards et l'abeille reconnaissants l'aident tour à tour. (Le
conte des animaux reconnaissants, raconté à la manière des contes de Ti-Jean.)

Plans : 1 large (le départ) · 2 moyen (la fourmilière) · 3 moyen (les
canards) · 4 moyen (les abeilles) · 5 large (le château du roi) · 6 moyen
(les mille perles) · 7 moyen (la clé d'or) · 8 moyen (les trois
princesses) · 9 gros plan (l'abeille) · 10 large (la fête).
"""
from contes import *
from base import _assombrir
from animaux import abeille

ID = "ti-jean-animaux"

TIJEAN = dict(peau="rosee", cheveux="roux", coiffure="herisses", habit="#c92a2a", robe=False, jambes="#1864ab", acc=("bonnet_nuit",),
              couleur_acc="#1864ab", ceinture="#f59f00", taches=True)
PIERRE = dict(stature="ado", peau="rosee", cheveux="brun", coiffure="courts", habit="#495057", robe=False, jambes="#795548", nez="long")
JACQUES = dict(stature="ado", peau="rosee", cheveux="noir", coiffure="raie", habit="#2b8a3e", robe=False, jambes="#795548", nez="pointu",
               carrure="ronde")
ROI_ = dict(stature="adulte", peau="rosee", cheveux="gris", coiffure="courts", barbe="#adb5bd", carrure="ronde", nez="rond")
PRINCESSE = dict(stature="ado", peau="claire", cheveux="blond", coiffure="tresses", habit="#4dabf7", motif_robe="#d0ebff", yeux="cils",
                 acc=("diademe",))
ERABLE = ("#e8590c", "#f08c00", "#e03131", "#fab005")


def tijean(x, y, s=1.45, **k):
    return personne(x, y, s, **{**TIJEAN, **k})


def frere(i, x, y, s=1.55, **k):
    return personne(x, y, s, **{**(PIERRE, JACQUES)[i], **k})


def princesse_(x, y, s=1.4, **k):
    return personne(x, y, s, **{**PRINCESSE, **k})


def fourmi_mini(x, y, s=1.0, rot=0, perle=False):
    m = []
    for k in range(3):
        for sgn in (-1, 1):
            m.append(trait(-4 + k * 6, 0, -8 + k * 8, sgn * 9, "#343a40", 1.5))
    m += [ellipse(-9, 0, 6, 4, "#5c2b1e"), ellipse(0, 0, 4, 3, "#5c2b1e"), cercle(7, 0, 4, "#5c2b1e"),
          trait(9, -2, 14, -6, "#343a40", 1.2), trait(9, 2, 14, 6, "#343a40", 1.2)]
    if perle:
        m.append(cercle(14, 0, 4, "#f8f9fa", stroke="#ced4da", stroke_width=1))
    return place(m, x, y, s, rot=rot)


def fourmiliere(x, y, s=1.0):
    return place([chemin("M -90 0 Q -40 -80 0 -84 Q 40 -80 90 0 Z", volume("#a0693a", 0.3, 0.8)), ellipse(0, -76, 10, 6, "#4a2c17")], x, y, s)


def erable(x, y, s=1.0, couleurs=ERABLE, graine=1):
    r = random.Random(graine)
    m = [rect(-18, -220, 36, 220, cylindre("#7c4a1e", 0.3, 0.75))]
    for k in range(9):
        m.append(cercle(r.uniform(-110, 110), -230 + r.uniform(-90, 60), r.uniform(50, 80), volume(r.choice(couleurs), 0.35, 0.8)))
    return place(m, x, y, s)


def ruche_creuse(x, y, s=1.0):
    return place([ellipse(0, 0, 24, 32, "#4a2c17"), chemin("M -16 -10 L 16 -10 M -18 4 L 18 4", stroke="#fab005", sw=4)], x, y, s)


def foret_erables(S, horizon=520, graine=1, lac=False):
    ciel(S, "#74c0fc", "#fff4e6")
    collines(S, horizon, "#c0eb75", graine=graine)
    S.add(rect(0, horizon + 40, 800, 800 - horizon - 40, terrain("#94d82d")))
    if lac:
        S.add(ellipse(480, 700, 360, 90, volume("#4dabf7", 0.3, 0.8)), ellipse(480, 680, 300, 50, "#74c0fc", opacity=0.6))


def perles(S, x, y, nb=30, graine=1, zone=(200, 40)):
    r = random.Random(graine)
    for k in range(nb):
        S.add(cercle(x + r.uniform(-zone[0], zone[0]), y + r.uniform(-zone[1], zone[1]), 5, "#f8f9fa", stroke="#ced4da", stroke_width=1.5))


def mousse(S, y=640):
    r = random.Random(3)
    S.add(rect(0, y, 800, 800 - y, "#5c940d"))
    for k in range(60):
        S.add(cercle(r.uniform(0, 800), r.uniform(y, 800), r.uniform(10, 26), r.choice(("#74b816", "#66a80f", "#82c91e")), opacity=0.8))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    foret_erables(S, 480, graine=2)
    S.add(chateau(640, 520, 0.4))
    for x, g_ in ((90, 1), (720, 2)):
        S.add(erable(x, 620, 1.1, graine=g_))
    S.add(tijean(380, 800, 1.75, expr="rire", bras="ouverts", regard=(0, -0.3)))
    S.add(canard(600, 790, 0.9, nage=False, flip=True, couleur="#f8f9fa"))
    S.add(abeille(560, 330, 0.7, flip=True), abeille(220, 360, 0.6))
    for k in range(5):
        S.add(fourmi_mini(150 + k * 26, 780 - (k % 2) * 6, 1.2))
    S.cachette(740, 700)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(abeille(200, 130, 1.4))
    return S


def p01():
    """Plan large : Ti-Jean et ses deux grands frères, Pierre et Jacques, partent chercher fortune sur le chemin de la forêt d'érables."""
    S = Scene()
    foret_erables(S, 500, graine=1)
    for x, g_ in ((80, 3), (720, 4), (400, 5)):
        S.add(erable(x, 600, 0.9, graine=g_))
    S.add(chemin("M 300 800 Q 380 650 420 560 L 470 560 Q 520 650 560 800 Z", "#e9c46a"))
    S.add(frere(0, 220, 790, 1.5, expr="fier", bras="porte", regard=(1, 0)))
    S.add(frere(1, 600, 790, 1.5, expr="fier", bras="hanches", flip=True, regard=(-1, 0)))
    S.add(tijean(410, 800, 1.35, expr="rire", bras="salut", regard=(0, -0.3), pas="marche"))
    S.add(texte(400, 110, "Partir chercher fortune", 46, "#c92a2a", contour="#fff"))
    return S


def p02():
    """Plan moyen : Pierre lève son bâton au-dessus d'une fourmilière ; Ti-Jean l'arrête : « Laissez-les tranquilles ! »"""
    S = Scene()
    foret_erables(S, 500, graine=6)
    S.add(fourmiliere(400, 790, 1.4))
    for k in range(12):
        S.add(fourmi_mini(300 + k * 18, 780 - (k % 3) * 20, 1.0, rot=k * 30))
    S.add(frere(0, 620, 790, 1.55, expr="malin", bras="salut", flip=True, regard=(-1, 0.6),
                objet=trait(-80, -160, -60, 40, "#8d5524", 8)))
    S.add(tijean(170, 800, 1.45, expr="fache", bras="designe", regard=(1, 0)))
    S.add(bulle(250, 150, 380, 90, "Laissez-les tranquilles !", 32, pointe=(200, 330)))
    S.cachette(660, 70, "air")
    return S


def p03():
    """Plan moyen : au bord du lac, Jacques veut attraper les canards pour le souper ; Ti-Jean les protège."""
    S = Scene()
    foret_erables(S, 480, graine=7, lac=True)
    for k, x in enumerate((420, 520, 620)):
        S.add(canard(x, 690 - (k % 2) * 16, 0.8, couleur="#f8f9fa", flip=k % 2 == 1))
    S.add(frere(1, 700, 800, 1.5, expr="malin", bras="tend", flip=True, regard=(-1, 0.4)))
    S.add(tijean(150, 800, 1.45, expr="fache", bras="ouverts", regard=(1, 0)))
    S.add(bulle(260, 150, 400, 110, "Non ! Laissez\nles canards tranquilles !", 30, pointe=(180, 330)))
    return S


def p04():
    """Plan moyen : sous un vieil érable creux plein d'abeilles, les frères veulent secouer l'arbre pour voler le miel ; Ti-Jean refuse."""
    S = Scene()
    foret_erables(S, 500, graine=8)
    S.add(erable(400, 760, 1.4, graine=9))
    S.add(ruche_creuse(400, 560, 1.2))
    for k in range(6):
        S.add(abeille(330 + k * 30, 500 + (k % 2) * 30, 0.35, flip=k % 2 == 0))
    S.add(frere(0, 620, 800, 1.5, expr="malin", bras="tient", flip=True, regard=(-1, -0.3)))
    S.add(frere(1, 730, 800, 1.45, expr="miam", bras="hanches", flip=True))
    S.add(tijean(160, 800, 1.45, expr="fache", bras="designe", regard=(1, -0.3)))
    S.add(bulle(240, 150, 360, 110, "Le miel est à elles !\nLaissez-les !", 30, pointe=(190, 330)))
    return S


def p05():
    """Plan large : au château, le roi annonce trois épreuves ; les deux frères essaient… et abandonnent."""
    S = Scene()
    jardin_chateau(S, chateau_x=400, chateau_s=0.7)
    S.add(roi(400, 790, 1.5, expr="triste", bras="ouverts", **ROI_))
    S.add(frere(0, 640, 800, 1.4, expr="triste", bras="tete", flip=True), frere(1, 740, 800, 1.35, expr="fache", bras="croises", flip=True))
    S.add(tijean(150, 800, 1.35, expr="concentre", bras="pense", regard=(1, -0.3)))
    S.add(bulle(400, 130, 480, 110, "Qui réussira les trois épreuves\naura toute ma reconnaissance !", 28, pointe=(400, 330)))
    S.cachette(730, 410, "air")
    return S


def p06():
    """Plan moyen : dans la mousse, il faut ramasser les mille perles avant le soir ; Ti-Jean désespère… et les fourmis arrivent."""
    S = Scene()
    ciel(S, "#ffa94d", "#fff4e6")
    S.ambiance("soir")
    mousse(S, 600)
    perles(S, 400, 700, 30, graine=1, zone=(360, 80))
    S.add(rect(320, 560, 160, 50, volume("#a0693a", 0.3, 0.8), rx=10))
    for k in range(22):
        S.add(fourmi_mini(120 + (k * 37) % 580, 640 + (k * 53) % 140, 1.3, rot=(k * 47) % 360, perle=k % 2 == 0))
    S.add(tijean(160, 800, 1.45, expr="joie", bras="joues", regard=(1, 0.6)))
    S.add(texte(470, 140, "Mille perles avant le soir !", 42, "#c92a2a", contour="#fff"))
    return S


def p07():
    """Plan moyen : la clé d'or est au fond du lac ; les canards plongent et la rapportent à Ti-Jean."""
    S = Scene()
    foret_erables(S, 480, graine=10, lac=True)
    S.add(canard(470, 690, 0.9, couleur="#f8f9fa", flip=True), canard(620, 676, 0.8, couleur="#f8f9fa", flip=True))
    S.add(place([cercle(0, 0, 10, "none", stroke=OR, stroke_width=4), rect(8, -3, 30, 6, OR), rect(30, -3, 4, 12, OR)], 420, 668, 1.0))
    for k in range(5):
        S.add(cercle(520 + k * 20, 720 + (k % 2) * 10, 6, "#fff", opacity=0.7))
    S.add(tijean(180, 800, 1.45, expr="rire", bras="tend", regard=(1, 0.3)))
    S.add(texte(470, 140, "La clé d'or !", 54, OR_FONCE, contour="#fff"))
    return S


def p08():
    """Plan moyen : trois princesses, pareilles comme trois gouttes d'eau ; laquelle est la plus jeune, celle qui a mangé du sirop d'érable ?"""
    S = Scene()
    salle_bal(S)
    for k, x in enumerate((220, 400, 580)):
        S.add(princesse_(x, 790, 1.4, expr="sourire", bras="mains_jointes", regard=(0, 0.3)))
        S.add(texte(x, 290, "?", 56, "#7048e8", contour="#fff"))
    S.add(roi(720, 790, 1.2, expr="malin", bras="pense", flip=True, **ROI_))
    S.add(tijean(80, 800, 1.15, expr="concentre", bras="pense", regard=(1, -0.2)))
    S.add(texte(400, 130, "Laquelle est la plus jeune ?", 44, "#7048e8", contour="#fff"))
    S.cachette(100, 260, "air")
    return S


def p09():
    """Gros plan : l'abeille vole droit vers la princesse du milieu et se pose sur ses lèvres sucrées : « C'est elle ! »"""
    S = Scene()
    salle_bal(S)
    S.add(princesse_(400, 900, 2.0, expr="rire", bras="joues", regard=(0, -0.3)))
    S.add(chemin("M 720 160 Q 640 420 466 626", stroke="#495057", sw=3, stroke_dasharray="8 8"))
    S.add(abeille(440, 640, 0.5, flip=True))
    S.add(tijean(110, 940, 1.6, expr="joie", bras="designe", regard=(1, -0.5)))
    S.camera(1.1, 420, 520)
    S.dessus(texte(400, 110, "C'est elle !", 64, "#c92a2a", contour="#fff"))
    return S


def p10():
    """Plan large : grande fête au château : Ti-Jean joue du violon, la princesse danse la gigue, les animaux font la fête."""
    S = Scene()
    jardin_chateau(S, chateau_x=400, chateau_s=0.65)
    S.add(tijean(250, 800, 1.45, expr="rire", bras="tient", regard=(1, 0),
                 objet=g([ellipse(70, -150, 18, 22, "#c46a1a"), rect(66, -200, 8, 50, "#212529"), trait(40, -190, 110, -130, "#e9c46a", 3)])))
    S.add(princesse_(480, 790, 1.4, expr="rire", bras="danse", flip=True))
    S.add(roi(680, 790, 1.25, expr="rire", bras="applaudit", flip=True, **ROI_))
    S.add(canard(130, 790, 0.7, nage=False, couleur="#f8f9fa", ailes="haut"), abeille(560, 300, 0.5), abeille(620, 340, 0.4, flip=True))
    for k in range(6):
        S.add(fourmi_mini(360 + k * 20, 786, 1.1))
    S.add(notes(360, 340, 1.1, "#c92a2a"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("abeille-seule.svg", vignette),
    ("01-le-depart.svg", p01), ("02-la-fourmiliere.svg", p02), ("03-les-canards.svg", p03),
    ("04-les-abeilles.svg", p04), ("05-le-roi.svg", p05), ("06-les-perles.svg", p06),
    ("07-la-cle-d-or.svg", p07), ("08-trois-princesses.svg", p08), ("09-c-est-elle.svg", p09),
    ("10-la-fete.svg", p10),
]
