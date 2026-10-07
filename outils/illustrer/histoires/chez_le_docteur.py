"""Chez le docteur — une visite de contrôle, sans peur."""
from base import *
from objets import *
from metiers import *

ID = "chez-le-docteur"
DOC = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#ffffff", jambes="#495057",
           chaussures="#343a40", tenue=blouse() + stethoscope())
DOC_SANS = dict(DOC, tenue=blouse())          # quand il tient son stéthoscope
LOU = dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#f783ac", jambes="#5c7cfa",
           chaussures="#e64980")
PAPA = dict(peau="claire", cheveux="chatain", coiffure="courts", habit="#69db7c", jambes="#364fc7",
            barbe="#8d5524")


def doc(x, y, s=1.5, **k):
    return pro(x, y, s, **{**DOC, **k})


def lou(x, y, s=1.05, **k):
    return petit(x, y, s, **{**LOU, **k})


def papa(x, y, s=1.5, **k):
    return pro(x, y, s, **{**PAPA, **k})


def piece(S, affiche=True):
    cabinet(S)
    if affiche:
        S.add(rect(560, 90, 150, 190, "#fff", rx=8, stroke="#a5d8ff", stroke_width=4))
        S.add(coeur(635, 170, 1.4, "#fa5252"))
        S.add(texte(635, 255, "boum-boum", 22, "#1c7ed6"))


def table_examen(x, y, w=300):
    """Table d'examen avec son rouleau de papier ; (x, y) = milieu au sol."""
    return g([rect(x - w / 2 + 20, y - 150, 16, 150, "#adb5bd"), rect(x + w / 2 - 36, y - 150, 16, 150, "#adb5bd"),
              rect(x - w / 2, y - 180, w, 40, "#4dabf7", rx=12),
              rect(x - w / 2 + 30, y - 186, w - 60, 10, "#fff", rx=4),
              rect(x - w / 2 - 10, y - 200, 40, 40, "#4dabf7", rx=14)])


def toise(x, y_sol, h=520):
    m = [rect(x - 22, y_sol - h, 44, h, "#fff9db", stroke="#fcc419", stroke_width=3)]
    for k in range(0, h, 26):
        m.append(trait(x - 22, y_sol - k, x - (4 if k % 52 else -6), y_sol - k, "#f08c00", 3))
    return g(m)


def balance(x, y):
    return g([rect(x - 70, y - 26, 140, 26, "#e9ecef", rx=10, stroke="#ced4da", stroke_width=3),
              rect(x - 30, y - 22, 60, 16, "#343a40", rx=4), texte(x, y - 9, "18 kg", 13, "#69db7c")])


def stetho_tenu(xm, ym, xp, yp):
    """Tuyau de stéthoscope de la main (xm, ym) au pavillon posé en (xp, yp)."""
    return g([chemin(f"M {xm} {ym} Q {(xm + xp) / 2} {max(ym, yp) + 30} {xp} {yp}", stroke="#495057", sw=5),
              cercle(xp, yp, 12, "#adb5bd", stroke="#495057", stroke_width=4)])


def otoscope(x, y, s=1.0, rot=0):
    return place([rect(-8, 0, 16, 60, "#343a40", rx=6), poly([(-12, 0), (12, 0), (4, -34), (-4, -34)], "#ced4da"),
                  cercle(0, 6, 5, "#fff3bf")], x, y, s, rot=rot)


def marteau_reflexe(x, y, s=1.0, rot=0):
    return place([rect(-3, 0, 6, 70, "#adb5bd", rx=3), poly([(-26, -2), (26, -2), (16, 14), (-16, 14)], "#fa5252")],
                 x, y, s, rot=rot)


def couverture():
    S = Scene()
    piece(S)
    S.add(doc(240, 780, 1.9, expr="content", bras="donne", tenue=blouse(), regard=(1, 0.3)))
    S.add(lou(560, 780, 1.45, expr="rire", bras="ouverts"))
    S.add(stetho_tenu(240 + 84 * 1.9, 780 - 92 * 1.9, 552, 670))
    S.add(texte(560, 380, "boum-boum !", 44, "#fa5252", contour="#fff"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(otoscope(80, 150, 1.2, rot=-20), marteau_reflexe(320, 150, 1.2, rot=20))
    S.add(g([chemin("M 130 120 Q 120 200 200 214 Q 280 200 270 120", stroke="#495057", sw=8),
             cercle(130, 112, 9, "#495057"), cercle(270, 112, 9, "#495057"),
             chemin("M 200 214 L 200 236", stroke="#495057", sw=8),
             cercle(200, 246, 22, "#adb5bd", stroke="#495057", stroke_width=6)]))
    S.add(coeur(200, 90, 1.1, "#fa5252"))
    return S


def p01():
    S = Scene()
    piece(S, affiche=False)
    S.add(rect(60, 120, 200, 140, "#fff", rx=8, stroke="#a5d8ff", stroke_width=4))
    S.add(texte(160, 175, "Salle", 30, "#1c7ed6"), texte(160, 215, "d'attente", 30, "#1c7ed6"))
    # banc
    S.add(rect(80, 560, 520, 30, "#74c0fc", rx=10), rect(100, 590, 16, 70, "#adb5bd"), rect(564, 590, 16, 70, "#adb5bd"))
    S.add(papa(220, 680, 1.5, expr="sourire", bras="calin", regard=(1, 0)))
    S.add(lou(430, 690, 1.15, expr="inquiet", bras="porte", regard=(-1, 0),
              objet=livres_pile(0, -50, 0.8)))
    S.add(tour_cubes(680, 720, 0.9, n_=4))
    S.add(plante(740, 590, 0.9))
    return S


def p02():
    S = Scene()
    piece(S)
    S.add(porte(130, 600, 160, 330, "#a5d8ff", ouverte=True))
    S.add(doc(360, 760, 1.6, expr="content", bras="salut", regard=(1, 0)))
    S.add(lou(600, 760, 1.15, expr="timide", bras="bas", regard=(-1, 0)))
    S.add(bulle(330, 120, 330, 90, "Bonjour, Lou !", 40, pointe=(350, 330)))
    return S


def p03():
    S = Scene()
    piece(S, affiche=False)
    S.add(toise(330, 700))
    S.add(lou(330, 700, 1.25, expr="fier", bras="bas"))
    S.add(rect(270, 430, 120, 10, "#fa5252", rx=4))
    S.add(balance(560, 720))
    S.add(doc(620, 760, 1.4, expr="rire", bras="montre", flip=True, regard=(-1, -0.5)))
    S.add(bulle(560, 130, 380, 90, "Tu as grandi !", 40, pointe=(600, 360)))
    return S


def p04():
    S = Scene()
    piece(S)
    S.add(table_examen(430, 760, 360))
    S.add(lou(430, 580, 1.15, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(doc(170, 760, 1.55, expr="content", bras="donne", tenue=blouse(), regard=(1, 0)))
    S.add(stetho_tenu(170 + 84 * 1.55, 760 - 92 * 1.55, 425, 497))
    S.add(texte(560, 360, "Fffff…", 44, "#4dabf7", contour="#fff"))
    S.add(texte(250, 300, "boum-boum", 40, "#fa5252", contour="#fff", rot=-8))
    return S


def p05():
    S = Scene()
    piece(S)
    S.add(papa(480, 760, 1.6, expr="rire", bras="hanches"))
    # Lou porte les embouts aux oreilles et pose le pavillon sur Papa
    S.add(lou(250, 760, 1.15, expr="bouche_bee", bras="donne", regard=(1, 0)))
    xm, ym = 250 + 84 * 1.15, 760 - 92 * 1.15
    S.add(chemin(f"M {250 - 50} {760 - 150 * 1.15} Q 250 {700} {xm} {ym}", stroke="#495057", sw=5))
    S.add(chemin(f"M {250 + 50} {760 - 150 * 1.15} Q 260 {690} {xm} {ym}", stroke="#495057", sw=5))
    S.add(stetho_tenu(xm, ym, 470, 640))
    S.add(notes(380, 420, 1.0, "#fa5252"), coeur(470, 640, 0.6, "#fa5252"))
    S.add(bulle(250, 140, 400, 90, "Il fait de la musique !", 34, pointe=(260, 520)))
    S.add(doc(700, 760, 1.2, expr="content", bras="croises", flip=True))
    return S


def p06():
    S = Scene()
    piece(S, affiche=False)
    S.add(cercle(400, 420, 300, "#fff9db"))
    S.add(lou(470, 780, 1.9, expr="timide", bras="bas", regard=(1, 0)))
    S.add(doc(170, 790, 1.8, expr="concentre", bras="donne", regard=(1, -0.3)))
    xm, ym = 170 + 84 * 1.8, 790 - 92 * 1.8
    S.add(otoscope(xm + 10, ym + 6, 1.2, rot=60))
    S.add(texte(650, 260, "Ça chatouille !", 36, "#e64980", contour="#fff", rot=8))
    return S


def p07():
    S = Scene()
    piece(S, affiche=False)
    S.add(lou(480, 770, 1.8, expr="baille", bras="bas"))
    S.add(doc(200, 770, 1.75, expr="sourire", bras="donne", regard=(1, -0.2)))
    xm, ym = 200 + 84 * 1.75, 770 - 92 * 1.75
    S.add(lampe_poche(xm + 6, ym - 4, 1.0, rot=-25, faisceau=0))
    S.add(poly([(xm + 40, ym - 30), (480 - 14, 770 - 112 * 1.8), (480 + 14, 770 - 106 * 1.8)], "#fff3bf", opacity=0.6))
    S.add(texte(560, 260, "Aaaah !", 70, "#e64980", contour="#fff"))
    return S


def p08():
    S = Scene()
    piece(S, affiche=False)
    S.add(table_examen(400, 780, 400))
    # Lou assise au bord de la table : une jambe pend, l'autre se lève toute seule
    k = 1.4
    S.add(rect(400 - 26 * k, 600, 20 * k, 70, LOU["jambes"], rx=9), ellipse(400 - 16 * k, 672, 22, 12, LOU["chaussures"]))
    S.add(g([rect(400 + 6 * k, 600, 20 * k, 70, LOU["jambes"], rx=9), ellipse(400 + 16 * k, 672, 22, 12, LOU["chaussures"])],
            transform=f"rotate(-55 {400 + 16 * k} 604)"))
    S.add(lou(400, 610, k, expr="rire", bras="haut", jambes="none", chaussures="none"))
    S.add(mouvement(560, 560, 1.0, rot=-40))
    S.add(doc(660, 780, 1.7, expr="rire", bras="donne", flip=True, regard=(-1, 0)))
    S.add(marteau_reflexe(660 - 84 * 1.7, 780 - 92 * 1.7, 1.0, rot=-120))
    S.add(texte(200, 260, "Toc !", 80, "#1c7ed6", contour="#fff", rot=-10))
    return S


def p09():
    S = Scene()
    piece(S, affiche=False)
    S.add(doc(220, 760, 1.6, expr="content", bras="montre", regard=(1, -0.5)))
    S.add(lou(560, 760, 1.2, expr="joie", bras="hanches"))
    pensees = [(470, 150, pomme(0, 0, 1.1) + g([cercle(60, 10, 26, "#fab005"), cercle(-60, 14, 20, "#51cf66")])),
               (690, 260, zzz(0, 0, 1.0)),
               (500, 330, ballon_jeu(0, 0, 34)),
               (690, 450, g([rect(-40, -20, 80, 40, "#ffc9e3", rx=14), bulles_lavage()]))]
    for x, y, contenu in pensees:
        S.add(cercle(x, y, 70, "#fff", stroke="#a5d8ff", stroke_width=4))
        S.add(place(contenu, x, y))
    return S


def bulles_lavage():
    return g([cercle(-30, -30, 10, "#e7f5ff", stroke="#74c0fc", stroke_width=2),
              cercle(10, -38, 13, "#e7f5ff", stroke="#74c0fc", stroke_width=2),
              cercle(38, -24, 8, "#e7f5ff", stroke="#74c0fc", stroke_width=2)])


def p10():
    S = Scene()
    piece(S, affiche=False)
    S.add(porte(670, 600, 160, 330, "#a5d8ff", ouverte=True))
    S.add(doc(650, 760, 1.3, expr="content", bras="salut", flip=True))
    S.add(papa(150, 760, 1.5, expr="sourire", bras="bas"))
    S.add(lou(380, 760, 1.25, expr="rire", bras="haut",
              tenue=autocollant(10, -80, 0.55)))
    S.add(pensee(400, 170, 140, doc(400, 300, 0.7, peau="claire", cheveux="roux", coiffure="tresses"),
                 depuis=(390, 430)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("stethoscope-seul.svg", vignette),
    ("01-salle-d-attente.svg", p01), ("02-bonjour.svg", p02), ("03-toise.svg", p03),
    ("04-coeur.svg", p04), ("05-coeur-de-papa.svg", p05), ("06-oreilles.svg", p06),
    ("07-gorge.svg", p07), ("08-reflexe.svg", p08), ("09-conseils.svg", p09),
    ("10-autocollant.svg", p10),
]
