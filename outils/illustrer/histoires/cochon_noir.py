"""Qui a peur du noir ? — Pistache le cochon (le courage)."""
from base import *
from objets import *

ID = "cochon-noir"
PYJAMA = dict(habit="#74c0fc", motif="pois", couleur_motif="#e7f5ff")
MINOU = dict(couleur="#495057")


def chambre(S, fen_nuit=True):
    interieur(S, "#d3f9d8", "#c9a47e", 590, papier="#b2f2bb")
    S.add(fenetre(560, 100, 170, 160, "#1c2a52", nuit_=fen_nuit, rideaux="#ffd43b"))
    S.add(tapis(420, 760, 220, 36, "#ffe066", "#fcc419"))


def lit_pistache(S, x=260, y=720, expr="sourire", cache=False, regard=(0, 0), chat=False, k=1.4):
    """Pistache couché dans son lit ; (x, y) = milieu du bas du lit."""
    m = [rect(-200, -250, 28, 250, "#c68642", rx=10), rect(-180, -120, 380, 60, "#fff", rx=10),
         rect(-165, -165, 110, 55, "#fff", rx=24, stroke="#e9ecef", stroke_width=3),
         perso("cochon", -105, -8, 1.0, expr=expr, bras="bas", regard=regard, **PYJAMA)]
    if chat:
        m.append(perso("chat", 40, -100, 0.5, expr="dort", **MINOU))
    haut = -150 if cache else -130
    m.append(chemin(f"M -170 {haut + 20} Q -110 {haut - 10} -40 {haut + 16} L 200 {haut + 20} L 200 -40 L -170 -40 Z", "#ff8787"))
    m += [cercle(-120 + j * 80, -80, 10, "#ffc9c9") for j in range(4)]
    m += [rect(186, -180, 28, 180, "#c68642", rx=10), rect(-200, -50, 414, 30, "#c68642", rx=6)]
    S.add(place(m, x, y, k))


def couverture():
    S = Scene()
    chambre(S)
    S.add(lampe(150, 600, 0.9, allumee=False))
    S.add(robe_chambre(640, 330, 1.0))
    mg, md = mains(360, 750, 1.6, "donne")
    S.add(perso("cochon", 360, 750, 1.6, expr="fier", bras="donne", regard=(1, 0), **PYJAMA,
                objet=lampe_poche(84, -92, 1.0)))
    S.add(perso("chat", 210, 760, 0.85, expr="content", **MINOU))
    obscurite(S, [faisceau(md[0] + 30, md[1], 640, 420, 110), trou_doux(320, 620, 240, "#777")], opacity=0.72)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("cochon", 200, 265, 0.95, expr="content", bras="porte", **PYJAMA,
                objet=lampe_poche(0, -74, 0.9, rot=-90)))
    return S


def p01():
    S = Scene()
    chambre(S, fen_nuit=True)
    S.add(lampe(560, 590, 0.9, allumee=True))
    lit_pistache(S, 300, 760, expr="sourire", k=1.3)
    S.add(porte(700, 590, 140, 300, "#b5835a"))
    S.add(perso("cochon", 700, 760, 1.6, expr="sourire", bras="salut", regard=(-1, 0), acc=("lunettes",)))
    S.add(bulle(420, 130, 330, 80, "Bonne nuit !", 38, pointe=(600, 330)))
    return S


def p02():
    S = Scene()
    chambre(S)
    lit_pistache(S, 310, 770, expr="surpris", regard=(1, -0.3))
    S.add(monstre_ombre(640, 330, 1.2, "#1b1f3b"))
    obscurite(S, [trou_doux(150, 560, 150, "#666")], opacity=0.8)
    S.add(ellipse(626, 276, 12, 7, "#ffe066"), ellipse(666, 276, 12, 7, "#ffe066"))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(rect(600, 560, 130, 200, "#c68642", rx=8))
    S.add(lampe_poche(665, 548, 1.2))
    lit_pistache(S, 290, 770, expr="inquiet", cache=True, regard=(1, 0), k=1.3)
    S.add(chemin("M 560 600 Q 600 560 630 546", stroke="#74c0fc", sw=18))
    S.add(cercle(632, 546, 15, "#ffc9d6"))
    obscurite(S, [trou_doux(160, 570, 160, "#555")], opacity=0.75)
    S.add(texte(250, 300, "boum… boum…", 44, "#ff8787"))
    S.add(coeur(250, 380, 1.4, "#ff8787"))
    return S


def p04():
    S = Scene()
    chambre(S)
    S.add(porte(620, 590, 180, 330, "#b5835a"))
    S.add(robe_chambre(620, 330, 1.2))
    mg, md = mains(230, 760, 1.5, "donne")
    S.add(perso("cochon", 230, 760, 1.5, expr="surpris", bras="donne", regard=(1, -0.3), **PYJAMA,
                objet=lampe_poche(84, -92, 1.0, rot=-15)))
    obscurite(S, [faisceau(md[0] + 30, md[1] - 10, 620, 440, 150)], opacity=0.8)
    S.add(texte(620, 170, "Clic !", 60, "#ffe066", contour="#0b1433"))
    return S


def p05():
    S = Scene()
    chambre(S)
    S.add(plante(640, 560, 1.1))
    S.add(rect(560, 556, 170, 14, "#fff"))
    mg, md = mains(240, 760, 1.5, "montre")
    S.add(perso("cochon", 240, 760, 1.5, expr="joie", bras="montre", regard=(1, -0.5), **PYJAMA,
                objet=lampe_poche(86, -130, 1.0, rot=-30)))
    obscurite(S, [faisceau(md[0] + 25, md[1] - 15, 640, 420, 130)], opacity=0.8)
    for k, (x, rt) in enumerate([(140, -30), (230, -10), (330, 20)]):
        S.add(ellipse(x, 200, 22, 90, "#050a1c", rot=rt, opacity=0.8))
    S.add(texte(640, 150, "Clic !", 60, "#ffe066", contour="#0b1433"))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(rect(80, 560, 660, 60, "#c68642", rx=8))
    S.add(rect(80, 530, 660, 40, "#ff8787", rx=10))
    S.add(rect(80, 620, 20, 120, "#c68642"), rect(720, 620, 20, 120, "#c68642"))
    S.add(perso("chat", 330, 750, 0.95, expr="content", bras="bas", **MINOU))
    mg, md = mains(640, 780, 1.4, "donne", flip=True)
    S.add(perso("cochon", 640, 780, 1.4, expr="rire", bras="donne", flip=True, **PYJAMA,
                objet=lampe_poche(84, -92, 1.0, rot=10)))
    obscurite(S, [faisceau(md[0] - 25, md[1] + 5, 330, 690, 110)], opacity=0.82)
    S.add(texte(320, 460, "Miaou !", 56, "#ffe066", contour="#0b1433"))
    return S


def p07():
    S = Scene()
    chambre(S)
    S.add(cercle(430, 280, 190, "#fff3bf"))
    ombre = "#2b2b3a"
    S.add(g([ellipse(430, 320, 90, 60, ombre), ellipse(390, 190, 20, 80, ombre, rot=-15), ellipse(460, 190, 20, 80, ombre, rot=15),
             cercle(470, 300, 8, "#fff3bf"), ellipse(360, 370, 40, 18, ombre)]))
    S.add(perso("cochon", 250, 770, 1.45, expr="rire", bras="haut", regard=(1, -1), **PYJAMA))
    S.add(lampe_poche(560, 700, 1.3, rot=-120, couleur="#ffd43b"))
    obscurite(S, [cercle(430, 280, 200, "#000"), trou_doux(250, 620, 260, "#222")], opacity=0.7)
    S.add(texte(620, 520, "Un lapin !", 44, "#ffe066", contour="#0b1433"))
    return S


def p08():
    S = Scene()
    chambre(S)
    S.add(g([cercle(90, 470, 30, "#ffe066", opacity=0.5), ellipse(90, 490, 18, 24, "#ffe066")]))
    lit_pistache(S, 460, 770, expr="dort", chat=True, k=1.45)
    obscurite(S, [trou_doux(90, 480, 170, "#000"), trou_doux(330, 560, 220, "#444")], opacity=0.6)
    S.add(zzz(330, 400, 1.0, "#ffe066"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pistache-seul.svg", vignette),
    ("01-bonne-nuit.svg", p01), ("02-monstre.svg", p02), ("03-sous-la-couette.svg", p03),
    ("04-robe-de-chambre.svg", p04), ("05-plante.svg", p05), ("06-sous-le-lit.svg", p06),
    ("07-ombres.svg", p07), ("08-dodo.svg", p08),
]
