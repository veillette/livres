"""Le masque du carnaval — inventer son propre personnage.

Mardi gras : ça sent les crêpes, et l'après-midi passe le grand défilé.
Mais Nina n'a pas de déguisement ! Lion ? La crinière tombe sur les yeux.
Super-héroïne ? Elle s'emmêle dans la cape. Pirate ? Le chapeau est bien
trop grand. « Et si tu inventais le tien ? » propose Papa. Nina découpe,
colle, peint… et devient la Lionne-Pirate-Volante, qui donne à tous les
enfants du défilé l'envie d'inventer.

Plans : 1 moyen (les crêpes) · 2 moyen (le coffre) · 3 moyen (la chute) ·
4 gros plan (le chapeau) · 5 large (au milieu des costumes) · 6 moyen
(l'atelier) · 7 gros plan (la révélation) · 8 large (le défilé) · 9 moyen
(« Tu es quoi ? ») · 10 large (tout le monde invente) · 11 moyen (le soir).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import confettis, serpentin, guirlande_fanions, pile_crepes, poele_crepe

ID = "carnaval-masque"
PAPIER_PEINT = "pois"

NINA = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#fab005", robe=False, jambes="#e64980",
            nez="petit", yeux="cils")
PAPA = dict(peau="doree", cheveux="brun", coiffure="courts", habit="#1098ad", robe=False, jambes="#343a40",
            stature="adulte", carrure="normale", nez="long", barbe="#4a2c17")
ROUGE_CAPE = "#e03131"


def nina(x, y, s=1.4, **k):
    return personne(x, y, s, **{**NINA, **k})


def papa(x, y, s=1.4, **k):
    return personne(x, y, s, **{**PAPA, **k})


def enfant_(x, y, s, peau, cheveux, coiffure, habit, **k):
    return personne(x, y, s, peau=peau, cheveux=cheveux, coiffure=coiffure, habit=habit, **k)


# --- Morceaux de costumes (repère de la tête d'un enfant) -----------------------

def criniere(c="#f08c00", c2="#e8590c", tombe=False):
    """Crinière de lion autour du visage (derriere=) ; tombe : elle glisse sur
    les yeux (coiffe=)."""
    if tombe:
        m = [chemin("M -92 -120 Q -110 -250 0 -262 Q 110 -250 92 -120 Q 60 -150 0 -138 Q -60 -150 -92 -120 Z", c),
             chemin("M -70 -136 L -60 -112 L -40 -136 L -24 -110 L -6 -134 L 10 -110 L 28 -134 L 46 -110 L 64 -134 L 76 -116",
                    stroke=c2, sw=10)]
        m += [ellipse(-58, -238, 18, 22, c2), ellipse(58, -238, 18, 22, c2)]
        return g(m)
    m = []
    for k in range(18):
        a = math.radians(k * 20)
        m.append(poly([(70 * math.cos(a - 0.2), -156 + 70 * math.sin(a - 0.2)), (106 * math.cos(a), -156 + 106 * math.sin(a)),
                       (70 * math.cos(a + 0.2), -156 + 70 * math.sin(a + 0.2))], c2 if k % 2 else c))
    m.append(cercle(0, -156, 80, c))
    m += [ellipse(-56, -226, 18, 20, c2), ellipse(56, -226, 18, 20, c2)]
    return g(m)


def tricorne(s=1.0, plume="#e03131", bord=-176):
    """Chapeau de pirate noir à tête de mort, dans le repère de la tête ; son
    bord passe à la hauteur `bord` (-176 : posé sur le front)."""
    m = [chemin("M -96 -176 Q -60 -196 0 -190 Q 60 -196 96 -176 Q 70 -260 0 -262 Q -70 -260 -96 -176 Z", "#212529"),
         chemin("M -96 -176 Q 0 -150 96 -176", stroke="#fab005", sw=6),
         cercle(0, -222, 15, "#f8f9fa"), trait(-14, -200, 14, -190, "#f8f9fa", 5), trait(14, -200, -14, -190, "#f8f9fa", 5),
         cercle(-5, -224, 3.5, "#212529"), cercle(5, -224, 3.5, "#212529"),
         chemin("M 60 -240 Q 110 -300 130 -250", stroke=plume, sw=12)]
    return place(m, 0, bord + 176 * s, s)


def epee_carton(x, y, s=1.0, rot=-40):
    """Épée en carton peint ; (x, y) = la poignée."""
    return place([rect(-6, -150, 12, 140, "#ced4da", rx=4), poly([(-6, -150), (0, -170), (6, -150)], "#ced4da"),
                  rect(-24, -14, 48, 10, "#d9a066", rx=4), rect(-6, -4, 12, 30, "#8d5524", rx=3)], x, y, s, rot=rot)


def nina_costume(x, y, s=1.4, cape=True, **k):
    """La Lionne-Pirate-Volante : crinière, petit tricorne, cape à étoiles."""
    return nina(x, y, s, derriere=criniere(), coiffe=tricorne(0.62, bord=-212), cape=ROUGE_CAPE if cape else None, **k)


def coffre(x, y, s=1.0, ouvert=True):
    m = [rect(-130, -110, 260, 110, volume("#a0693a", 0.3, 0.75), rx=10),
         rect(-130, -70, 260, 14, "#6d4424"), rect(-20, -84, 40, 30, "#fab005", rx=4)]
    if ouvert:
        m.insert(0, chemin("M -130 -110 L -150 -230 L 150 -230 L 130 -110 Z", _assombrir("#a0693a", 0.75)))
        m.insert(1, place([chemin("M 0 0 q 30 -60 60 0", stroke="#cc5de8", sw=14)], -90, -110))
        m.insert(1, place([poly([(0, 0), (30, -50), (60, 0)], "#40c057")], 10, -110))
    return place(m, x, y, s)


def chambre(S, y=600):
    piece(S, "chambre", y)
    S.add(fenetre(560, 100, 160, 140, "#a5d8ff", rideaux="#fab005"))


def char_carnaval(x, y, s=1.0):
    """Char du défilé : une grosse tête de Monsieur Carnaval sur un plateau fleuri."""
    m = [rect(-220, -90, 440, 70, volume("#7048e8", 0.3, 0.7), rx=12),
         cercle(-150, -14, 30, "#343a40"), cercle(150, -14, 30, "#343a40"),
         cercle(-150, -14, 12, "#adb5bd"), cercle(150, -14, 12, "#adb5bd")]
    for k in range(9):
        m.append(cercle(-200 + k * 50, -90, 18, ("#ff6b6b", "#ffd43b", "#69db7c")[k % 3]))
    m += [chemin("M -120 -100 Q -130 -330 0 -340 Q 130 -330 120 -100 Z", volume("#ffd8a8", 0.3, 0.8)),
          poly([(-90, -320), (0, -470), (90, -320)], "#e64980"), cercle(0, -476, 18, "#ffd43b"),
          ellipse(-42, -240, 18, 24, "#fff"), ellipse(42, -240, 18, 24, "#fff"),
          cercle(-40, -236, 9, ENCRE), cercle(44, -236, 9, ENCRE),
          cercle(0, -200, 20, "#fa5252"), chemin("M -60 -160 Q 0 -110 60 -160", stroke=ENCRE, sw=8),
          cercle(-80, -180, 16, "#ff8787", opacity=0.6), cercle(80, -180, 16, "#ff8787", opacity=0.6)]
    return place(m, x, y, s)


def tambour_majorette(x, y, s=1.0):
    """Musicien de fanfare au tambour (adulte), de face."""
    tambour = g([rect(-50, -110, 100, 70, volume("#e03131", 0.3, 0.7), rx=6), ellipse(0, -110, 50, 12, "#f8f9fa"),
                 chemin("M -50 -100 L 50 -50 M 50 -100 L -50 -50", stroke="#fab005", sw=4)])
    return personne(x, y, s, peau="foncee", cheveux="noir", coiffure="courts", habit="#1c7ed6", robe=False,
                    jambes="#f8f9fa", stature="adulte", bras="applaudit", objet=tambour,
                    coiffe=g([rect(-40, -260, 80, 70, "#1c7ed6", rx=8), rect(-44, -196, 88, 12, "#fab005"), cercle(0, -270, 14, "#fa5252")]))


def rue_fete(S, y=640):
    ciel(S, "#74c0fc", "#fff9db")
    S.add(immeuble(110, y, 200, 3, "#ffd8a8", toit="mansarde"), immeuble(360, y, 180, 4, "#d0ebff", toit="pignon"),
          immeuble(610, y, 220, 3, "#ffe3e3", toit="mansarde"))
    S.add(rect(0, y, 800, 800 - y, "#ced4da"))
    S.add(rect(0, y + 40, 800, 800 - y - 40, "#adb5bd"))
    S.add(guirlande_fanions(0, 150, 800, 150, creux=40, nb=16))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_fete(S)
    S.add(char_carnaval(620, 700, 0.75))
    S.add(confettis(20, 200, 780, 760, 70, graine=3))
    S.add(serpentin(40, 360, 1.0, "#f783ac", rot=-10))
    S.add(nina_costume(330, 780, 1.6, expr="rire", bras="lance", regard=(1, 0),
                       objet=epee_carton(80, -202, 1.0, rot=10)))
    S.cachette(60, 770)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(nina_costume(200, 262, 0.82, expr="rire", bras="lance", objet=epee_carton(80, -202, 1.0, rot=10)))
    return S


def p01():
    """Plan moyen : Mardi gras, ça sent les crêpes… mais pas de déguisement."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.add(papa(560, 760, 1.4, expr="rire", bras="tient", regard=(-1, 0),
               objet=poele_crepe(*ancre(-40, -146, "tient", "adulte"), 0.9)))
    S.add(table(260, 780, 360, 150, "#c68642", nappe="#fff3bf"))
    S.add(pile_crepes(220, 620, 0.9))
    S.add(nina(330, 760, 1.25, expr="inquiet", bras="epaules", regard=(1, 0)))
    S.add(bulle(250, 150, 420, 110, "Je n'ai pas\nde déguisement !", 36, pointe=(320, 420)))
    S.add(texte(620, 180, "Mardi gras !", 46, "#e64980", contour="#fff", rot=6))
    return S


def p02():
    """Plan moyen : la crinière de lion tombe sur les yeux."""
    S = Scene()
    chambre(S)
    S.add(coffre(600, 700, 1.0))
    S.add(nina(330, 760, 1.5, expr="rire", bras="poing", regard=(1, 0), coiffe=criniere(tombe=True)))
    S.add(texte(160, 300, "Grrr !", 60, "#e8590c", contour="#fff", rot=-10))
    S.add(bulle(590, 180, 240, 80, "Pas lion…", 36, pointe=(420, 380)))
    return S


def p03():
    """Plan moyen : emmêlée dans la cape, Nina tombe sur les fesses."""
    S = Scene()
    chambre(S)
    S.add(coffre(640, 700, 0.9))
    S.add(nina(330, 770, 1.45, expr="oups", bras="ouverts", rot=-18, cape=ROUGE_CAPE,
               objet=chemin("M -70 -100 Q 0 -40 70 -110 L 60 -10 Q 0 10 -60 -10 Z", cylindre(ROUGE_CAPE, 0.2, 0.7))))
    S.add(texte(170, 720, "Boum !", 50, "#495057", rot=-6))
    S.add(mouvement(180, 520, 1.2, rot=-30))
    S.add(bulle(560, 180, 360, 80, "Pas super-héroïne…", 32, pointe=(420, 400)))
    S.cachette(740, 760)
    return S


def p04():
    """Gros plan : le chapeau de pirate, bien trop grand."""
    S = Scene()
    chambre(S)
    S.add(nina(400, 830, 1.9, expr="rire", bras="tete", coiffe=tricorne(1.9, bord=-104)))
    S.camera(1.25, 400, 480)
    S.dessus(bulle(400, 90, 360, 90, "Pas pirate !", 44))
    S.cachette(100, 770)
    return S


def p05():
    """Plan large : assise au milieu des costumes ; Papa s'accroupit près d'elle."""
    S = Scene()
    chambre(S)
    S.add(coffre(170, 690, 0.8))
    S.add(place(criniere(), 160, 820, 0.5), place(tricorne(), 560, 820, 0.6))
    S.add(chemin("M 620 700 Q 700 660 760 720 L 740 760 Q 680 720 640 740 Z", ROUGE_CAPE))
    S.add(place(nina(0, 0, 1.2, expr="triste", bras="croises"), 340, 760, 1.0))
    S.add(papa(530, 780, 1.25, expr="sourire", bras="tend", flip=True, regard=(-1, 0.5)))
    S.add(bulle(560, 170, 380, 110, "Et si tu inventais\nle tien ?", 34, pointe=(540, 370)))
    return S


def p06():
    """Plan moyen : découper, coller, peindre."""
    S = Scene()
    chambre(S)
    S.add(nina(400, 700, 1.6, expr="concentre", bras="porte", regard=(0, 1)))
    S.add(table(400, 800, 640, 140, "#c68642", nappe="#e7f5ff"))
    S.add(place(criniere(), 250, 790, 0.5))
    S.add(place(tricorne(), 560, 770, 0.55))
    S.add(rect(380, 630, 120, 30, ROUGE_CAPE, rx=6))
    for k, c in enumerate(("#e03131", "#fab005", "#1c7ed6")):
        S.add(rect(120 + k * 40, 620, 30, 36, c, rx=4), ellipse(135 + k * 40, 620, 15, 5, _assombrir(c, 0.7)))
    S.add(paillettes(470, 560, 1.0), paillettes(320, 520, 0.8, "#f783ac"))
    S.add(texte(160, 210, "découpe…", 40, "#1c7ed6", rot=-8), texte(400, 160, "colle…", 40, "#e64980"),
          texte(640, 210, "peint !", 40, "#2f9e44", rot=8))
    return S


def p07():
    """Gros plan : la révélation, devant le miroir."""
    S = Scene()
    chambre(S)
    S.add(nina_costume(400, 810, 1.9, expr="fier", bras="lance", regard=(0, 0),
                       objet=epee_carton(80, -202, 1.0, rot=10)))
    S.add(paillettes(180, 300, 1.2), paillettes(640, 260, 1.0))
    S.camera(1.15, 400, 470)
    S.dessus(bulle(400, 80, 560, 100, "Je suis la Lionne-\nPirate-Volante !", 36))
    S.cachette(90, 770)
    return S


def p08():
    """Plan large : le défilé, le char, la fanfare, les confettis."""
    S = Scene()
    rue_fete(S)
    S.add(char_carnaval(420, 700, 0.9))
    S.add(tambour_majorette(150, 760, 1.05))
    S.add(confettis(20, 180, 780, 760, 90, graine=8))
    S.add(texte(160, 330, "Boum, boum !", 40, "#e03131", contour="#fff", rot=-8))
    S.add(papa(700, 790, 1.15, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(nina_costume(600, 790, 1.0, expr="rire", bras="saute", regard=(-1, 0)))
    S.cachette(320, 770)
    return S


def p09():
    """Plan moyen : « Tu es déguisée en quoi ? » — la Lionne rugit."""
    S = Scene()
    rue_fete(S)
    S.add(confettis(20, 180, 780, 760, 50, graine=11))
    S.add(enfant_(160, 780, 1.25, "foncee", "noir", "courts", "#2f9e44", robe=False, jambes="#495057",
                  expr="bouche_bee", bras="joues", regard=(1, 0), acc=("couronne",)))
    S.add(enfant_(640, 780, 1.25, "claire", "blond", "couettes", "#cc5de8", expr="surpris", regard=(-1, 0),
                  ailes="#d0bfff", bras="joues"))
    S.add(nina_costume(400, 790, 1.45, expr="furieux", bras="lance", regard=(0, 0),
                       objet=epee_carton(80, -202, 1.0, rot=10)))
    S.add(texte(400, 230, "ROARRR !", 70, "#e8590c", contour="#fff", rot=-4))
    S.add(bulle(170, 360, 260, 100, "Tu es déguisée\nen quoi ?", 28, pointe=(170, 470)))
    S.cachette(730, 260, "air")
    return S


def p10():
    """Plan large : tout le monde invente son personnage."""
    S = Scene()
    rue_fete(S)
    S.add(confettis(20, 180, 780, 760, 60, graine=13))
    S.add(enfant_(120, 780, 1.1, "foncee", "noir", "courts", "#2f9e44", robe=False, jambes="#495057",
                  expr="rire", bras="haut", acc=("couronne",), cape="#7048e8"))
    S.add(enfant_(290, 790, 1.1, "claire", "blond", "couettes", "#cc5de8", expr="rire", bras="danse",
                  ailes="#d0bfff", coiffe=tricorne(0.62, bord=-212)))
    S.add(nina_costume(460, 795, 1.15, expr="rire", bras="saute"))
    S.add(enfant_(630, 790, 1.1, "rosee", "roux", "boucles", "#1c7ed6", robe=False, jambes="#343a40",
                  expr="rire", bras="victoire", derriere=criniere("#ced4da", "#868e96")))
    S.add(texte(400, 280, "Chacun invente le sien !", 40, "#7048e8", contour="#fff"))
    S.cachette(740, 770)
    return S


def p11():
    """Plan moyen : le soir, couverte de confettis, Nina mange sa crêpe."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.ambiance("soir")
    S.add(fenetre(560, 100, 170, 150, "#ff922b", rideaux="#fab005"))
    S.add(lampe(130, 580, 1.0))
    S.add(papa(600, 700, 1.3, expr="rire", bras="mains_jointes", regard=(-1, 0)))
    S.add(nina_costume(330, 700, 1.3, expr="miam", bras="porte", regard=(1, 0), cape=False,
                       objet=ellipse(0, -80, 40, 12, "#f6c453")))
    S.add(table(420, 800, 600, 120, "#c68642", nappe="#fff3bf"))
    S.add(pile_crepes(480, 670, 0.7))
    S.add(confettis(200, 380, 460, 680, 30, graine=17))
    S.add(bulle(330, 150, 520, 120, "L'an prochain, je serai une\nDragonne-Boulangère-Sous-Marine !", 26, pointe=(330, 340)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("costume-seul.svg", vignette),
    ("01-mardi-gras.svg", p01), ("02-pas-lion.svg", p02), ("03-pas-super-heroine.svg", p03),
    ("04-pas-pirate.svg", p04), ("05-et-si.svg", p05), ("06-l-atelier.svg", p06),
    ("07-la-lionne.svg", p07), ("08-le-defile.svg", p08), ("09-roarrr.svg", p09),
    ("10-chacun-le-sien.svg", p10), ("11-les-crepes.svg", p11),
]
