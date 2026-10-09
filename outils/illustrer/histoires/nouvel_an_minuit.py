"""Le vœu de minuit — veiller jusqu'au Nouvel An, et ce qu'on souhaite vraiment.

Le 31 décembre, Milo annonce qu'il restera éveillé jusqu'à minuit. Huit
heures, neuf heures, dix heures : il décore, il trinque, il danse pour ne
pas dormir. À onze heures et demie, il s'endort sur le canapé, son vœu à la
main. Papi le réveille juste à temps pour le compte à rebours : dix, neuf…
Bonne année ! Milo lit son vœu… et se rendort aussitôt.

Plans : 1 moyen (le défi) · 2 large (les décorations) · 3 moyen (la
table) · 4 large en diagonale (la danse) · 5 moyen (le vœu) · 6 gros plan
(endormi) · 7 moyen (réveil) · 8 large (dix, neuf…) · 9 large (bonne
année) · 10 gros plan (le vœu lu) · 11 large (dans son lit).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from objets import assiette, tasse
from fetes import confettis, serpentin, feu_artifice, guirlande_lumineuse, mirliton, guirlande_fanions

ID = "nouvel-an-minuit"
PAPIER_PEINT = "losanges"

MILO = dict(peau="claire", cheveux="roux", coiffure="herisses", habit="#364fc7", robe=False, jambes="#495057",
            taches=True, nez="retrousse")
JADE = dict(peau="brune", cheveux="noir", coiffure="afro", habit="#e64980", stature="ado", carrure="fine",
            yeux="cils")
PAPI = dict(peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#fab005", robe=False, jambes="#5c3d2e",
            stature="ancien", carrure="ronde", nez="rond", acc=("lunettes",), barbe="#e9ecef")
MAMAN = dict(peau="claire", cheveux="roux", coiffure="carre", habit="#12b886", stature="adulte", nez="pointu")


def milo(x, y, s=1.3, **k):
    return personne(x, y, s, **{**MILO, **k})


def jade(x, y, s=1.3, **k):
    return personne(x, y, s, **{**JADE, **k})


def papi(x, y, s=1.3, **k):
    return personne(x, y, s, **{**PAPI, **k})


def maman(x, y, s=1.3, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def grande_horloge(x, y, r, heure, minute=0, bord="#364fc7"):
    """Horloge murale ronde, bien lisible ; (x, y) = centre."""
    m = [cercle(x + 4, y + 6, r + 12, "#000", opacity=0.12), cercle(x, y, r + 12, bord), cercle(x, y, r, "#fff")]
    for k in range(12):
        a = math.radians(k * 30 - 60)
        m.append(texte(x + math.cos(a) * r * 0.78, y + math.sin(a) * r * 0.78 + r * 0.1, str(k + 1), r * 0.26, "#495057"))
    ah = math.radians((heure % 12 + minute / 60) * 30 - 90)
    am = math.radians(minute * 6 - 90)
    m.append(trait(x, y, x + math.cos(ah) * r * 0.5, y + math.sin(ah) * r * 0.5, ENCRE, r * 0.09))
    m.append(trait(x, y, x + math.cos(am) * r * 0.72, y + math.sin(am) * r * 0.72, ENCRE, r * 0.06))
    m.append(cercle(x, y, r * 0.07, "#e03131"))
    return g(m)


def canape(x, y, s=1.0, couleur="#7048e8"):
    """Canapé vu de face ; (x, y) = milieu du pied."""
    f = _assombrir(couleur, 0.8)
    m = [rect(-200, -190, 400, 120, volume(couleur, 0.25, 0.8), rx=30),
         rect(-230, -110, 460, 90, volume(couleur, 0.3, 0.75), rx=24),
         rect(-240, -150, 60, 140, f, rx=26), rect(180, -150, 60, 140, f, rx=26),
         rect(-210, -20, 20, 20, "#5c3d2e"), rect(190, -20, 20, 20, "#5c3d2e"),
         trait(0, -104, 0, -30, f, 3, opacity=0.6)]
    return place(m, x, y, s)


def coussin(x, y, s=1.0, couleur="#ffd43b", rot=0):
    return place([rect(-40, -30, 80, 60, volume(couleur, 0.3, 0.75), rx=18), cercle(0, 0, 5, _assombrir(couleur, 0.75))], x, y, s, rot=rot)


def papier_voeu(x, y, s=1.0, rot=0, ecrit=True):
    m = [rect(-34, -24, 68, 48, "#fff9db", rx=4, stroke="#fab005", stroke_width=2)]
    if ecrit:
        m += [trait(-24, -10, 22, -10, "#5c7cfa", 3), trait(-24, 0, 18, 0, "#5c7cfa", 3), trait(-24, 10, 10, 10, "#5c7cfa", 3)]
    return place(m, x, y, s, rot=rot)


def salon(S, y=620, nuit_dehors=True, feux=False, fenetre_x=470):
    """Le salon de Papi, un soir d'hiver : grande fenêtre sur la ville."""
    piece(S, "manoir", y)
    dehors = [rect(0, 0, 800, 800, lineaire([(0, "#0b1433"), (1, "#3b4a8a")]))]
    for k in range(18):
        dehors.append(cercle(fenetre_x + 10 + (k * 71) % 250, 90 + (k * 37) % 120, 2, "#fff3bf"))
    for k, (bx, bh) in enumerate(((0, 80), (60, 120), (120, 70), (170, 140), (230, 90))):
        bx += fenetre_x
        dehors.append(rect(bx, 300 - bh, 55, bh + 20, "#1c2a52"))
        for j in range(int(bh / 30)):
            dehors.append(rect(bx + 10 + (j % 2) * 22, 300 - bh + 10 + j * 28, 12, 14, "#ffe066" if (j + k) % 3 else "#3b4a8a"))
    if feux:
        dehors += [feu_artifice(fenetre_x + 70, 150, 55, "#ffd43b"), feu_artifice(fenetre_x + 200, 110, 45, "#f783ac"),
                   feu_artifice(fenetre_x + 160, 220, 35, "#69db7c")]
    S.add(fenetre(fenetre_x, 80, 260, 230, "#0b1433", cadre="#f8f9fa", rideaux="#364fc7", contenu=g(dehors)))
    S.add(tapis(400, y + 110, 300, 50, "#d0bfff", "#7048e8"))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S, feux=True)
    S.lumiere(600, 190, 140, "#ffe066", 0.4)
    S.add(grande_horloge(180, 190, 80, 12, 0))
    S.add(confettis(30, 300, 770, 700, 60, graine=2))
    S.add(serpentin(60, 420, 1.0, "#f783ac", rot=-15), serpentin(560, 380, 0.9, "#ffd43b", rot=20))
    S.add(milo(400, 780, 1.75, expr="rire", bras="saute", regard=(0, 0), acc=()))
    S.add(place(mirliton(0, 0, 1.0, couleur="#cc5de8"), 400 + 90 * 1.75, 780 - 196 * 1.75, 1.2, rot=-30))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(grande_horloge(200, 135, 95, 12, 0))
    S.add(confettis(20, 20, 380, 250, 26, graine=5))
    return S


def p01():
    """Plan moyen : le défi de Milo, devant Papi qui rit."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(190, 180, 70, 7, 0))
    S.add(canape(560, 760, 0.9, "#7048e8"))
    S.add(papi(560, 740, 1.3, expr="rire", bras="hanches", regard=(-1, 0)))
    S.add(milo(250, 780, 1.45, expr="fier", bras="poing", regard=(1, 0)))
    S.add(bulle(300, 410, 340, 110, "Cette fois, je reste\néveillé jusqu'à minuit !", 26, pointe=(250, 470)))
    return S


def p02():
    """Plan large : huit heures, les décorations."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(180, 170, 75, 8, 0))
    S.add(guirlande_fanions(20, 60, 780, 60, creux=40, nb=14))
    S.add(guirlande_lumineuse(20, 330, 440, 330, creux=30, nb=8))
    S.add(jade(560, 770, 1.3, expr="rire", bras="haut", regard=(-1, 0),
               objet=serpentin(-90, -210, 1.0, "#ffd43b")))
    S.add(_escabeau(260, 780))
    S.add(milo(260, 640, 1.2, expr="joie", bras="tient", regard=(1, -0.3), objet=serpentin(68, -146, 0.8, "#f783ac", rot=40)))
    S.add(texte(180, 300, "8 heures", 44, "#364fc7", contour="#fff"))
    return S


def _escabeau(x, y):
    return place([trait(-50, 0, -30, -150, "#adb5bd", 10), trait(50, 0, 30, -150, "#adb5bd", 10),
                  rect(-40, -150, 80, 14, "#868e96", rx=4), trait(-44, -50, 44, -50, "#adb5bd", 8),
                  trait(-38, -100, 38, -100, "#adb5bd", 8)], x, y)


def p03():
    """Plan moyen : neuf heures, on trinque ; Milo bâille un tout petit peu."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(180, 170, 75, 9, 0))
    S.add(maman(170, 680, 1.25, expr="rire", bras="leve_doigt", regard=(1, 0)))
    S.add(papi(620, 680, 1.25, expr="rire", bras="leve_doigt", flip=True, regard=(-1, 0)))
    S.add(jade(470, 680, 1.15, expr="sourire", bras="leve_doigt", flip=True, regard=(-1, 0)))
    S.add(table(400, 800, 640, 150, "#a0693a", nappe="#f8f9fa"))
    for x in (230, 360, 480, 600):
        S.add(assiette(x, 640, 1.2, bord="#364fc7"))
    S.add(_bougie_table(400, 640))
    S.add(milo(320, 720, 1.1, expr="baille", bras="leve_doigt", regard=(1, 0)))
    S.add(texte(180, 300, "9 heures", 44, "#364fc7", contour="#fff"))
    return S


def _bougie_table(x, y):
    S_ = [rect(x - 8, y - 70, 16, 60, "#fff9db", rx=3), ellipse(x, y - 82, 7, 13, "#ffd43b"), rect(x - 20, y - 12, 40, 12, "#fab005", rx=4)]
    return g(S_)


def p04():
    """Plan large en diagonale : dix heures, Milo danse pour ne pas dormir."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(180, 170, 75, 10, 0))
    S.add(canape(560, 760, 0.85, "#7048e8"))
    S.add(papi(620, 720, 1.1, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(jade(480, 735, 1.05, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(milo(250, 700, 1.35, expr="rire", bras="equilibre", regard=(1, 0), pas="pointe", rot=-14))
    S.add(mouvement(120, 520, 1.3, "#364fc7"), mouvement(140, 610, 1.0, "#364fc7"))
    S.add(texte(330, 400, "Vroum !", 54, "#e03131", contour="#fff", rot=-10))
    S.cachette(260, 70, "air")
    S.add(texte(180, 300, "10 heures", 44, "#364fc7", contour="#fff"))
    return S


def p05():
    """Plan moyen : onze heures, le papier des vœux ; les paupières lourdes."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(180, 170, 75, 11, 0))
    S.add(canape(420, 790, 1.0, "#7048e8"))
    S.add(coussin(230, 680, 1.0, "#ffd43b", rot=-10))
    S.add(jade(560, 770, 1.3, expr="sourire", bras="tend", flip=True, regard=(-1, 0), objet=papier_voeu(96, -104, 1.0)))
    S.add(milo(360, 790, 1.3, expr="dort", bras="pense", regard=(1, 0)))
    S.add(pensee(320, 400, 70, texte(320, 418, "?", 60, "#5c7cfa"), depuis=(360, 480)))
    S.add(texte(180, 300, "11 heures", 44, "#364fc7", contour="#fff"))
    return S


def p06():
    """Gros plan : onze heures et demie, Milo s'est endormi, son vœu à la main."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(210, 370, 55, 11, 30))
    S.add(canape(400, 800, 1.3, "#7048e8"))
    S.add(coussin(300, 640, 1.4, "#ffd43b", rot=-25))
    S.add(place(milo(0, 0, 1.3, expr="dort", bras="bas"), 360, 700, 1.0, rot=-62))
    S.add(papier_voeu(470, 720, 1.2, rot=12))
    S.add(zzz(470, 470, 1.5))
    S.camera(1.35, 400, 560)
    S.cachette(363, 259, "air")
    return S


def p07():
    """Plan moyen : « C'est l'heure ! » Papi chatouille, Milo ouvre un œil."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(400, 170, 90, 11, 58))
    S.add(canape(400, 800, 1.1, "#7048e8"))
    S.add(place(milo(0, 0, 1.2, expr="surpris", bras="bas"), 380, 700, 1.0, rot=-45))
    S.add(papi(600, 780, 1.35, expr="rire", bras="tend", flip=True, regard=(-1, 0.4)))
    S.add(jade(110, 780, 1.2, expr="joie", bras="saute", regard=(1, 0)))
    S.add(texte(330, 450, "guili guili !", 36, "#e64980", rot=-8))
    S.add(bulle(620, 330, 300, 80, "C'est l'heure !", 36, pointe=(580, 430)))
    S.cachette(750, 700)
    return S


def p08():
    """Plan large : tout le monde compte à rebours."""
    S = Scene()
    salon(S)
    S.add(grande_horloge(400, 170, 90, 11, 59))
    nombres = ("10", "9", "8", "7", "6", "5", "4", "3", "2", "1")
    for k, nb in enumerate(nombres):
        x, y = 100 + (k % 5) * 150, 330 + (k // 5) * 75
        S.add(texte(x, y, nb, 44 + k * 4, ("#e03131", "#f08c00", "#fab005", "#40c057", "#1c7ed6", "#7048e8")[k % 6], contour="#fff"))
    S.add(maman(110, 770, 1.15, expr="chante", bras="haut", regard=(1, 0)))
    S.add(papi(680, 770, 1.15, expr="chante", bras="haut", regard=(-1, 0)))
    S.add(jade(540, 780, 1.1, expr="chante", bras="applaudit", regard=(-1, 0)))
    S.add(milo(310, 785, 1.25, expr="chante", bras="poing", regard=(1, 0)))
    S.cachette(190, 70, "air")
    return S


def p09():
    """Plan large : BONNE ANNÉE ! feux d'artifice, confettis, bises."""
    S = Scene()
    salon(S, feux=True, fenetre_x=270)
    S.lumiere(400, 190, 200, "#ffe066", 0.45)
    S.add(confettis(20, 40, 780, 760, 90, graine=7))
    S.add(serpentin(30, 380, 1.0, "#ffd43b", rot=-10), serpentin(620, 360, 0.9, "#69db7c", rot=15))
    S.add(maman(150, 770, 1.2, expr="rire", bras="calin", regard=(1, 0)))
    S.add(milo(270, 790, 1.15, expr="rire", bras="calin", regard=(-1, 0)))
    S.add(papi(580, 770, 1.2, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(jade(700, 780, 1.1, expr="rire", bras="saute", regard=(-1, 0)))
    S.add(place(mirliton(0, 0, 1.0, couleur="#e64980"), 700 - 90 * 1.1 * 1.16, 780 - 196 * 1.1 * 1.16, 1.0, rot=210))
    S.add(texte(400, 430, "BONNE ANNÉE !", 76, "#fab005", contour="#7048e8", rot=-4))
    S.add(coeur(350, 690, 0.8, "#e64980"))
    S.cachette(190, 70, "air")
    return S


def p10():
    """Gros plan : Milo lit son vœu à voix haute."""
    S = Scene()
    salon(S, feux=True)
    S.add(confettis(20, 40, 780, 760, 40, graine=9))
    S.add(papi(150, 790, 1.5, expr="content", bras="mains_jointes", regard=(1, 0)))
    S.add(jade(650, 790, 1.4, expr="content", bras="mains_jointes", regard=(-1, 0)))
    S.add(milo(400, 800, 1.7, expr="sourire", bras="porte", regard=(0, 0.3), objet=papier_voeu(0, -76, 1.5)))
    S.camera(1.25, 400, 480)
    S.cachette(352, 216, "air")
    return S


def p11():
    """Plan large : Milo dort déjà, un serpentin sur la tête."""
    S = Scene()
    piece(S, "chambre", 600)
    S.ambiance("nuit")
    dehors = rect(0, 0, 800, 800, "#0b1433") + g([feu_artifice(560, 150, 30, "#f783ac"), feu_artifice(640, 200, 22, "#ffd43b")])
    S.add(fenetre(500, 90, 200, 170, "#0b1433", rideaux="#364fc7", contenu=dehors))
    S.add(lampe(130, 620, 0.9, abat="#ffd8a8"))
    S.add(lit(400, 760, 460, "#e7f5ff", "#364fc7"))
    S.add(place(milo(0, 0, 0.9, expr="dort", bras="bas"), 380, 625, 1.0, rot=-90))
    S.add(rect(305, 590, 330, 100, lineaire([(0, "#4c6ef5"), (1, "#364fc7")]), rx=24))
    S.add(serpentin(190, 560, 0.5, "#ffd43b", rot=-50))
    S.add(papier_voeu(560, 535, 0.9, rot=-8))
    S.add(zzz(330, 430, 1.2))
    S.cachette(720, 680)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("horloge-seule.svg", vignette),
    ("01-le-defi.svg", p01), ("02-huit-heures.svg", p02), ("03-neuf-heures.svg", p03),
    ("04-dix-heures.svg", p04), ("05-onze-heures.svg", p05), ("06-endormi.svg", p06),
    ("07-c-est-l-heure.svg", p07), ("08-dix-neuf-huit.svg", p08), ("09-bonne-annee.svg", p09),
    ("10-le-voeu.svg", p10), ("11-bonne-nuit.svg", p11),
]
