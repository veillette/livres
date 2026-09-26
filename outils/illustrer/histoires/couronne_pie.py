"""Qui a pris la couronne ? — ne pas accuser trop vite."""
from base import *
from objets import *
from fantastique import *

ID = "couronne-pie"
MIA = dict(coiffure="queue", cheveux="noir", peau="claire", habit="#f76707", acc=("diademe",))
REINE = dict(habit="#7048e8", cape="#c92a2a", coiffure="chignon", cheveux="gris", peau="rosee")
PACHA = dict(couleur="#adb5bd")
BISCUIT = dict(tache=True)
CUISINIER = dict(coiffure="courts", cheveux="chatain", habit="#f8f9fa", robe=False, jambes="#495057",
                 peau="brune", acc=("toque",))


def mia(x, y, s=1.0, **k):
    return personne(x, y, s, **{**MIA, **k})


def salle(S, mur="#fff3bf", papier="#ffe066"):
    interieur(S, mur, "#c9a27e", 600, papier=papier)
    S.add(rect(80, 90, 120, 200, "#c92a2a", rx=10), rect(600, 90, 120, 200, "#c92a2a", rx=10))
    for x in (140, 660):
        S.add(couronne_objet(x, 180, 0.6))


def jardin(S):
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(chateau(400, 560, 0.55))
    sol(S, 560, "#8ce99a")
    S.add(buisson(80, 620, 0.8, baies="#fa5252"), buisson(720, 620, 0.7))


def cuisine(S):
    interieur(S, "#e6fcf5", "#c9a27e", 600, papier="#c3fae8")
    S.add(etagere(640, 170, 240, objets=g([tasse(580, 170, 1.0, "#4dabf7"), tasse(640, 170, 1.0, "#ffd43b"), tasse(700, 170, 1.0, "#ff8787")])))


def loupe(x, y, s=1.0, rot=-30):
    m = [rect(-7, 30, 14, 70, "#a0522d", rx=6), cercle(0, 0, 36, "#d0ebff", opacity=0.6),
         cercle(0, 0, 36, "none", stroke="#495057", stroke_width=8), chemin("M -16 -14 Q -8 -24 4 -24", stroke="#fff", sw=5)]
    return place(m, x, y, s, rot=rot)


def coussin(x, y, s=1.0, couleur="#e64980"):
    m = [chemin("M -110 0 Q -120 -50 -100 -60 Q 0 -80 100 -60 Q 120 -50 110 0 Q 0 16 -110 0 Z", couleur)]
    for sx in (-1, 1):
        m.append(cercle(sx * 108, -30, 12, "#ffd43b"))
    return place(m, x, y, s)


def os_(x, y, s=1.0, rot=0):
    m = [rect(-40, -8, 80, 16, "#fff9db", rx=8)]
    for sx in (-1, 1):
        for sy in (-1, 1):
            m.append(cercle(sx * 42, sy * 10, 13, "#fff9db"))
    return place(m, x, y, s, rot=rot)


def trou(x, y, s=1.0):
    return place([ellipse(0, 0, 110, 34, "#5c3a1e"), ellipse(0, 4, 90, 24, "#3b2412"),
                  chemin("M 100 -10 Q 150 -40 180 -6 Q 150 6 110 4 Z", "#8d5524")], x, y, s)


def nid(x, y, s=1.0, tresors=True, couronne_=True):
    m = [ellipse(0, 0, 150, 56, "#8d5524")]
    for k in range(9):
        m.append(chemin(f"M {-140 + k * 30} {-20 + (k % 2) * 12} q 30 -16 60 6", stroke="#5c3a1e", sw=5))
    m.append(ellipse(0, -30, 120, 28, "#5c3a1e"))
    if tresors:
        m += [place([ellipse(0, 0, 10, 26, "#ced4da"), rect(-4, 20, 8, 50, "#ced4da", rx=3)], -80, -50, 1.0, rot=-50),
              cercle(70, -44, 16, "none", stroke="#fab005", stroke_width=6), cercle(70, -60, 7, "#4dabf7"),
              cercle(-30, -38, 10, "#fa5252"), cercle(-4, -44, 9, "#51cf66"), cercle(100, -30, 9, "#cc5de8")]
    if couronne_:
        m.append(couronne_objet(10, -40, 0.9, brille=True))
    return place(m, x, y, s)


def clochette(x, y, s=1.0):
    m = [trait(0, -60, 0, -36, "#fa5252", 4), chemin("M -24 0 Q -26 -40 0 -40 Q 26 -40 24 0 Z", "#ffd43b"),
         rect(-28, -4, 56, 8, "#f59f00", rx=4), cercle(0, 8, 7, "#f59f00")]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    salle(S)
    S.add(tapis(400, 740, 260, 50, "#ffc9c9", "#ff8787"))
    S.add(mia(300, 760, 1.6, expr="malin", bras="tient", objet=loupe(70, -150, 0.8)))
    S.add(pie(580, 470, 1.3, expr="malin", flip=True, objet=couronne_objet(-40, 0, 0.5)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(couronne_objet(200, 200, 1.8, brille=True))
    return S


def p01():
    S = Scene()
    salle(S)
    S.add(coussin(560, 700, 0.9, "#7048e8"))
    S.add(texte(560, 580, "?", 90, "#c92a2a"))
    S.add(personne(260, 770, 1.55, expr="surpris", bras="joues", **REINE))
    S.add(texte(400, 380, "Ma couronne !", 60, "#c92a2a", contour="#fff"))
    return S


def p02():
    S = Scene()
    salle(S)
    S.add(mia(400, 770, 1.7, expr="concentre", bras="tient", objet=loupe(70, -150, 0.8)))
    S.add(bulle(400, 120, 480, 100, "Je vais trouver le voleur !", 36, pointe=(380, 300)))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff0f6", "#c9a27e", 600, papier="#ffdeeb")
    S.add(fenetre(80, 110, 160, 160, "#a5d8ff", rideaux="#e64980"))
    S.add(coussin(530, 760, 1.2))
    S.add(perso("chat", 530, 720, 1.1, expr="dort", **PACHA))
    S.add(zzz(600, 480, 1.0))
    S.add(mia(220, 770, 1.45, expr="fache", bras="montre", regard=(1, 0)))
    S.add(bulle(420, 150, 420, 100, "C'est toi, le voleur !", 38, pointe=(260, 360)))
    return S


def p04():
    S = Scene()
    jardin(S)
    S.add(trou(520, 740, 1.0))
    S.add(os_(560, 640, 1.0, rot=-20))
    S.add(perso("chien", 600, 760, 1.2, expr="joie", bras="haut", flip=True, **BISCUIT))
    S.add(mia(220, 770, 1.45, expr="fache", bras="montre", regard=(1, 0)))
    S.add(bulle(400, 150, 460, 100, "Tu l'as enterrée !", 40, pointe=(260, 360)))
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(table(560, 770, 320, 130, nappe="#ffc9c9"))
    S.add(gateau(560, 620, 1.0, couleur="#f8c291", glacage="#ffe066", fruits="#fa5252"))
    S.add(personne(640, 760, 1.2, expr="surpris", bras="bas", regard=(-1, 0), **CUISINIER))
    S.add(mia(220, 770, 1.45, expr="fache", bras="montre", regard=(1, 0)))
    S.add(bulle(400, 150, 480, 110, "Tu l'as cachée\ndans le gâteau !", 38, pointe=(260, 360)))
    return S


def p06():
    S = Scene()
    salle(S)
    S.add(perso("chat", 180, 770, 1.1, expr="fache", bras="croises", **PACHA))
    S.add(perso("chien", 400, 770, 1.1, expr="fache", bras="croises", **BISCUIT))
    S.add(personne(620, 770, 1.1, expr="fache", bras="croises", **CUISINIER))
    S.add(texte(400, 380, "Hmpf !", 80, "#e03131", contour="#fff"))
    return S


def p07():
    S = Scene()
    salle(S)
    S.add(tapis(400, 740, 260, 50, "#ffc9c9", "#ff8787"))
    S.add(mia(400, 760, 1.6, expr="triste", bras="joues", regard=(0, 1)))
    S.add(nuage_orage(400, 230, 0.6))
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(tour_seule(560, 800, 1.0, h=440))
    S.add(pie(540, 330, 1.0, expr="malin", flip=True, ailes="ouvertes", objet=couronne_objet(-40, 0, 0.45, brille=True)))
    S.add(fenetre(40, 460, 260, 300, "#e7f5ff", cadre="#c68642"))
    S.add(mia(170, 800, 1.3, expr="surpris", bras="montre", regard=(1, -1)))
    return S


def p09():
    S = Scene()
    ciel(S, "#74c0fc", "#d0ebff")
    S.add(nuage(160, 140, 0.8), nuage(660, 120, 0.6))
    S.add(rect(0, 640, 800, 160, "#e5dbff"))
    for k in range(8):
        S.add(rect(k * 110, 600, 70, 50, "#e5dbff"))
    S.add(nid(520, 620, 1.2))
    S.add(mia(200, 760, 1.4, expr="bouche_bee", bras="joues", regard=(1, 0)))
    return S


def p10():
    S = Scene()
    ciel(S, "#74c0fc", "#d0ebff")
    S.add(rect(0, 640, 800, 160, "#e5dbff"))
    for k in range(8):
        S.add(rect(k * 110, 600, 70, 50, "#e5dbff"))
    S.add(nid(560, 640, 1.0, couronne_=False))
    S.add(pie(560, 560, 1.2, expr="timide", flip=True))
    S.add(mia(220, 760, 1.4, expr="sourire", bras="porte", regard=(1, 0), objet=couronne_objet(0, -60, 0.8)))
    S.add(bulle(520, 150, 500, 110, "J'adore ce qui brille !\nMais j'aurais dû demander.", 32, pointe=(560, 400)))
    return S


def p11():
    S = Scene()
    salle(S)
    S.add(perso("chat", 470, 770, 1.0, expr="content", **PACHA))
    S.add(perso("chien", 620, 780, 1.0, expr="rire", bras="haut", **BISCUIT))
    S.add(personne(720, 770, 0.95, expr="content", bras="porte", objet=part_gateau(0, -70, 0.7), **CUISINIER))
    S.add(mia(220, 770, 1.4, expr="timide", bras="calin", regard=(1, 0)))
    S.add(bulle(330, 150, 360, 90, "Pardon…", 50, pointe=(250, 380)))
    S.add(coeur(520, 480, 1.2))
    return S


def p12():
    S = Scene()
    salle(S)
    S.add(reine(300, 770, 1.55, expr="rire", bras="ouverts", habit="#7048e8", cheveux="gris"))
    S.add(mia(520, 770, 1.2, expr="rire", bras="haut"))
    S.add(pie(660, 420, 1.1, expr="rire", flip=True, ailes="ouvertes", objet=clochette(-40, 10, 0.8)))
    S.add(paillettes(640, 280, 1.2), paillettes(160, 300, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("couronne-seule.svg", vignette),
    ("01-disparue.svg", p01), ("02-l-enquete.svg", p02), ("03-le-chat.svg", p03),
    ("04-le-chien.svg", p04), ("05-le-cuisinier.svg", p05), ("06-hmpf.svg", p06),
    ("07-aucune-preuve.svg", p07), ("08-la-pie.svg", p08), ("09-le-nid.svg", p09),
    ("10-j-adore-ce-qui-brille.svg", p10), ("11-pardon.svg", p11), ("12-la-clochette.svg", p12),
]
