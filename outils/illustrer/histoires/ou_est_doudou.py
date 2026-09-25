"""Où est Doudou ? — ranger sa chambre (en jouant)."""
from base import *
from objets import *

ID = "ou-est-doudou"
CASTORIN = dict(habit="#69db7c", motif="rayures", couleur_motif="#b2f2bb")
MAMAN = dict(couleur="#a0693a", acc=("noeud",), couleur_acc="#f783ac", habit="#ffd43b")
DOUDOU_C = "#fcc2d7"


def doudou(x, y, s=1.0, rot=0, expr="content"):
    return perso("lapin", x, y, s * 0.42, expr=expr, couleur=DOUDOU_C, rot=rot)


def chambre(S, rangee=False, nuit_=False):
    interieur(S, "#e3fafc" if not nuit_ else "#aab8c8", "#d9a066", 590, papier="#c5f6fa" if not nuit_ else None)
    S.add(fenetre(560, 100, 160, 150, "#1c2a52" if nuit_ else "#a5d8ff", nuit_=nuit_, rideaux="#ffa94d"))
    S.add(etagere(170, 260, 220, objets=(livres_pile(120, 260, 0.9) + camion(210, 260, 0.6) if rangee else "")))


def lit_castor(x, y, k=1.3, expr="dort", avec_doudou=True, assis=False, bras="bas"):
    m = [rect(-200, -250, 28, 250, "#4dabf7", rx=10), rect(-180, -120, 380, 60, "#fff", rx=10),
         rect(-165, -165, 110, 55, "#fff", rx=24, stroke="#e9ecef", stroke_width=3)]
    if assis:
        m.append(perso("castor", -90, -40, 1.0, expr=expr, bras=bras, **CASTORIN))
    else:
        m.append(perso("castor", -105, -8, 1.0, expr=expr, **CASTORIN))
        if avec_doudou:
            m.append(doudou(-40, -110, 1.3, rot=20))
    m.append(chemin("M -170 -110 Q -110 -140 -40 -114 L 200 -110 L 200 -40 L -170 -40 Z", "#74c0fc"))
    m += [etoile5(-100 + j * 80, -80, 12, "#e7f5ff") for j in range(4)]
    m += [rect(186, -180, 28, 180, "#4dabf7", rx=10), rect(-200, -50, 414, 30, "#4dabf7", rx=6)]
    return place(m, x, y, k)


def bazar(S, graine=1, zone=(40, 620, 760, 790)):
    r = random.Random(graine)
    cols = ["#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c", "#cc5de8"]
    x0, y0, x1, y1 = zone
    for k in range(10):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        choix = k % 5
        if choix == 0:
            S.add(cube(x, y, 0.7, cols[k % 5], "ABCDE"[k % 5], rot=r.uniform(-30, 30)))
        elif choix == 1:
            S.add(chaussette(x, y, 1.0, cols[(k + 2) % 5], rot=r.uniform(-60, 60)))
        elif choix == 2:
            S.add(place(livres_pile(0, 0, 0.8), x, y, 1.0, rot=r.uniform(-20, 20)))
        elif choix == 3:
            S.add(ballon_jeu(x, y, 24, cols[(k + 1) % 5]))
        else:
            S.add(place(rect(-40, -10, 80, 20, cols[(k + 3) % 5], rx=8), x, y, 1.0, rot=r.uniform(-40, 40)))


def coffre(x, y, s=1.0, ouvert=True):
    m = [rect(-120, -120, 240, 120, "#e8590c", rx=10), rect(-120, -70, 240, 12, "#d9480f")]
    if ouvert:
        m.insert(0, poly([(-120, -120), (-110, -220), (130, -220), (120, -120)], "#d9480f"))
    return place(m, x, y, s)


def panier(x, y, s=1.0, contenu=""):
    m = [contenu, chemin("M -80 -70 L 80 -70 L 64 0 L -64 0 Z", "#e8a354")]
    for k in range(5):
        m.append(trait(-70 + k * 35, -66, -58 + k * 30, -4, "#c47b3f", 3))
    m.append(trait(-80, -70, 80, -70, "#c47b3f", 8))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    chambre(S)
    bazar(S, 5, (160, 640, 680, 790))
    S.add(perso("castor", 400, 760, 1.6, expr="inquiet", bras="tete", regard=(1, 0.3), **CASTORIN))
    S.add(g([ellipse(655, 570, 12, 32, DOUDOU_C, rot=20), ellipse(655, 572, 5, 22, "#ffc9c9", rot=20),
             chemin("M 540 740 Q 550 620 610 600 Q 690 580 730 640 Q 760 700 750 740 Z", "#ced4da"),
             chemin("M 570 660 Q 620 630 690 650", stroke="#adb5bd", sw=6), chaussette(720, 650, 0.9, "#4dabf7", rot=40)]))
    S.add(texte(250, 470, "?", 90, "#1c7ed6", contour="#fff", rot=-10), texte(580, 440, "?", 70, "#1c7ed6", contour="#fff", rot=12))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("castor", 180, 265, 0.9, expr="content", bras="calin", objet=doudou(0, -20, 1.4), **CASTORIN))
    return S


def p01():
    S = Scene()
    chambre(S, nuit_=True)
    S.add(lit_castor(300, 770, 1.3, expr="inquiet", assis=True, bras="joues"))
    S.add(porte(680, 590, 140, 300, "#b5835a", ouverte=True))
    S.add(perso("castor", 680, 760, 1.6, expr="surpris", bras="bas", regard=(-1, 0), **MAMAN))
    S.add(bulle(300, 150, 380, 90, "Où est Doudou ?", 42, pointe=(260, 400)))
    return S


def p02():
    S = Scene()
    chambre(S)
    S.add(lampe(620, 590, 1.0, allumee=False))
    S.add(chaussette(620, 420, 1.3, "#fa5252", rot=10))
    bazar(S, 2)
    S.add(perso("castor", 330, 760, 1.5, expr="oups", bras="tete", **CASTORIN))
    S.add(texte(330, 280, "Quel bazar !", 56, "#e8590c", contour="#fff"))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(coffre(480, 740, 1.3))
    S.add(perso("castor", 260, 760, 1.5, expr="neutre", bras="haut", regard=(1, -0.5), **CASTORIN))
    S.add(camion(260, 760 - 160 * 1.5 - 20, 1.3))
    S.add(bulle(560, 190, 420, 90, "Non… c'est le camion.", 34, pointe=(360, 380)))
    return S


def p04():
    S = Scene()
    chambre(S)
    S.add(rect(60, 480, 680, 90, "#fff", rx=10), rect(60, 450, 680, 50, "#74c0fc", rx=10))
    S.add(rect(60, 570, 680, 30, "#4dabf7"), rect(60, 600, 20, 160, "#4dabf7"), rect(720, 600, 20, 160, "#4dabf7"))
    S.add(rect(80, 600, 640, 160, "#495057", opacity=0.35))
    S.add(chaussette(200, 720, 1.2, "#4dabf7", rot=80), pomme(330, 730, 1.0, "#a47148"))
    S.add(araignee(600, 690, 1.3))
    S.add(texte(600, 400, "Bonjour, l'araignée !", 38, "#495057", contour="#fff"))
    S.add(perso("castor", 440, 800, 1.1, expr="surpris", bras="joues", regard=(1, -0.2), **CASTORIN))
    return S


def p05():
    S = Scene()
    chambre(S)
    bazar(S, 3, (380, 680, 760, 790))
    voitures = camion(-20, -60, 0.6) + cube(40, -70, 0.6, "#ffd43b", "A")
    S.add(panier(180, 780, 1.2, contenu=voitures))
    S.add(perso("castor", 560, 760, 1.8, expr="sourire", bras="porte", regard=(-1, 0), **MAMAN,
                objet=place(livres_pile(0, 0, 1.0), 0, -50, 1.0)))
    S.add(perso("castor", 330, 770, 1.3, expr="concentre", bras="porte", **CASTORIN, objet=chaussette(0, -60, 1.0, "#fa5252")))
    S.add(bulle(400, 150, 380, 90, "Et si on rangeait ?", 38, pointe=(520, 370)))
    return S


def p06():
    S = Scene()
    chambre(S, rangee=True)
    S.add(panier(640, 780, 1.1, contenu=cube(-30, -70, 0.6, "#4dabf7", "B") + ballon_jeu(30, -80, 22)))
    S.add(perso("castor", 380, 770, 1.6, expr="rire", bras="course", pieds_haut=True, **CASTORIN))
    S.add(mouvement(230, 560, 1.4))
    S.add(horloge(400, 130, 50, 7, 0))
    S.add(texte(400, 340, "Qui range le plus vite ?", 44, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    chambre(S, rangee=True)
    S.add(g([chemin("M 460 790 Q 470 640 560 620 Q 660 600 720 660 Q 760 720 750 790 Z", "#ced4da"),
             chemin("M 500 700 Q 560 660 640 690", stroke="#adb5bd", sw=6), chaussette(700, 690, 1.0, "#fa5252", rot=40)]))
    S.add(perso("castor", 280, 770, 1.6, expr="joie", bras="haut", **CASTORIN))
    S.add(doudou(280, 770 - 165 * 1.6 + 20, 1.6, rot=-10, expr="rire"))
    S.add(texte(560, 250, "DOUDOU !", 80, "#d6336c", contour="#fff", rot=-6))
    S.add(coeur(560, 380, 1.3), coeur(680, 320, 0.9, "#ff8787"))
    return S


def p08():
    S = Scene()
    chambre(S, rangee=True, nuit_=True)
    S.add(panier(680, 790, 0.9, contenu=camion(0, -60, 0.6)))
    S.add(lit_castor(360, 770, 1.45, expr="dort"))
    S.add(zzz(330, 390, 1.0, "#5c7cfa"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("castorin-seul.svg", vignette),
    ("01-ou-est-doudou.svg", p01), ("02-bazar.svg", p02), ("03-le-coffre.svg", p03),
    ("04-sous-le-lit.svg", p04), ("05-ranger.svg", p05), ("06-le-plus-vite.svg", p06),
    ("07-doudou.svg", p07), ("08-bonne-nuit.svg", p08),
]
