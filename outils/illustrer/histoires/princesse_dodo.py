"""La princesse qui ne voulait pas dormir — une histoire pour le soir.

La princesse Léa refuse d'aller au lit. Elle parcourt le château endormi :
le garde, le cuisinier, le chat, le dragon du donjon et même la lune bâillent
l'un après l'autre, et chacun lui confie un petit rituel du soir (un doudou,
un verre d'eau, une grande étirée, une berceuse, une étoile). Revenue dans sa
chambre, Léa les essaie tous… et finit par s'endormir.
"""
from base import *
from base import EXPRESSIONS
from objets import *
from fantastique import *
from fables import cheminee

ID = "princesse-dodo"

# Léa : peau brune, cheveux noirs ; chignon et robe le jour, tresses et
# chemise de nuit rose étoilée le soir.
LEA_JOUR = dict(peau="brune", cheveux="noir", coiffure="chignon", habit="#7048e8", acc=("diademe",))
LEA = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#fcc2d7", motif_robe="#fff3bf")
REINE = dict(peau="brune", cheveux="noir", coiffure="chignon", habit="#ae3ec9", cape="#5f3dc4")
DRAGON = dict(couleur="#b197fc", ventre="#e5dbff")
NUIT_HAUT, NUIT_BAS = "#141b3d", "#3b3f8f"


def lea(x, y, s=1.0, **k):
    return personne(x, y, s, **{**LEA, **k})


def doudou(x, y, s=0.3, **k):
    return perso("lapin", x, y, s, **{**dict(couleur="#d0ebff", habit="#74c0fc", joues=False, expr="content"), **k})


def petite_etoile(x, y, r=26, expr="content"):
    return etoile_perso(x, y, r, expr=expr)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def ciel_nuit(S, nb=40, graine=3):
    nuit(S, NUIT_HAUT, NUIT_BAS)
    etoiles(S, nb, graine)


def chambre(S, sombre=True):
    if sombre:
        interieur(S, "#2e2a6b", "#241e52", y=600, papier="#3a3580", plinthe="#1b1640")
    else:
        interieur(S, "#e5dbff", "#c9a27e", y=600, papier="#d0bfff")


def murs_pierre(S, mur="#3d4677", joint="#323a66", y=600, sol_c="#262c50"):
    """Couloir de château, la nuit : grosses pierres et dalles."""
    S.add(rect(0, 0, S.w, y, mur))
    for row in range(int(y / 60) + 1):
        for k in range(-1, 9):
            bx = k * 110 + (row % 2) * 55
            S.add(rect(bx + 4, row * 60 + 4, 102, 52, joint, rx=8, opacity=0.6))
    S.add(rect(0, y, S.w, S.h - y, sol_c))
    for k in range(1, 5):
        S.add(trait(0, y + k * 50, S.w, y + k * 50, "#000", 2, opacity=0.15))


def torche(x, y, s=1.0, allumee=True):
    m = []
    if allumee:
        m.append(cercle(0, -70, 90, "#ffd43b", opacity=0.12))
        m.append(cercle(0, -70, 50, "#ffd43b", opacity=0.15))
    m += [poly([(-10, 0), (10, 0), (6, -60), (-6, -60)], "#8d5524"),
          rect(-16, -66, 32, 12, "#495057", rx=4)]
    if allumee:
        m += [ellipse(0, -88, 16, 26, "#ff922b"), ellipse(0, -84, 9, 15, "#ffd43b")]
    return place(m, x, y, s)


def fenetre_arc(x, y, w=150, h=220, lune_=True):
    """Fenêtre en ogive ouverte sur la nuit ; (x, y) = coin haut gauche."""
    d = f"M {x} {y + h} L {x} {y + w / 2} Q {x} {y} {x + w / 2} {y} Q {x + w} {y} {x + w} {y + w / 2} L {x + w} {y + h} Z"
    m = [chemin(d, "#1c2350", stroke="#8c94c7", sw=12)]
    m += [cercle(x + w * 0.25, y + h * 0.55, 2.5, "#fff"), cercle(x + w * 0.7, y + h * 0.8, 2, "#fff"),
          etoile5(x + w * 0.35, y + h * 0.3, 6, "#fff3bf")]
    if lune_:
        m.append(cercle(x + w * 0.65, y + h * 0.35, 18, "#fff3bf"))
    m.append(rect(x - 14, y + h, w + 28, 14, "#8c94c7", rx=4))
    return g(m)


def lune_perso(x, y, r=110, expr="sourire", halo=True):
    """La lune qui parle ; (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    k = r / 50
    m = []
    if halo:
        m += [cercle(x, y, r * 1.6, "#fff3bf", opacity=0.08), cercle(x, y, r * 1.3, "#fff3bf", opacity=0.12)]
    m.append(cercle(x, y, r, "#fff3bf"))
    m += [cercle(x - r * 0.5, y - r * 0.5, r * 0.13, "#ffe8a3"), cercle(x + r * 0.55, y - r * 0.35, r * 0.09, "#ffe8a3"),
          cercle(x + r * 0.45, y + r * 0.55, r * 0.11, "#ffe8a3")]
    visage = [ellipse(-24, 12, 8, 5, ROSE, opacity=0.7), ellipse(24, 12, 8, 5, ROSE, opacity=0.7),
              oeil(-14, -4, ys) + oeil(14, -4, ys), sourcils(14, -4, ss), bouche(0, 10, bs, 0.8)]
    m.append(place(visage, x, y, k))
    return g(m)


def nuage_couverture(x, y, s=1.0):
    return place([nuage(0, 0, 1.0, "#d0bfff", ombre="#9775fa"),
                  chemin("M -90 30 Q 0 50 100 30", stroke="#e5dbff", sw=5, opacity=0.8)], x, y, s)


def chateau_nuit(x, y, s=1.0):
    return chateau(x, y, s, mur="#4c3f91", mur2="#3f3480", toit="#2b2463", drapeau="#9775fa",
                   porte_c="#2b2463", nuit_=True)


def remparts(S, y=620, couleur="#5c5299"):
    """Haut d'une tour : créneaux au premier plan."""
    S.add(rect(0, y, S.w, S.h - y, couleur))
    for k in range(0, 9):
        S.add(rect(k * 100 - 10, y - 60, 60, 64, couleur, rx=4))
    for row in range(3):
        for k in range(-1, 9):
            S.add(rect(k * 100 + (row % 2) * 50 + 4, y + 10 + row * 60, 92, 50, "#4f4689", rx=6, opacity=0.7))


def lit_lea(S, x=430, y=770, w=420, qui=None, couv="#9775fa"):
    S.add(lit(x, y, w, "#e5dbff", couv, bois="#8d5b34"))
    if qui:
        S.add(qui)
    S.add(rect(x - w / 2 + 60, y - 125, w - 60, 85, couv, rx=18))
    for k in range(4):
        S.add(etoile5(x - w / 2 + 120 + k * 80, y - 85, 9, "#fff3bf"))


def verre_eau(x, y, s=1.0):
    return place([chemin("M -22 -60 L -16 0 L 16 0 L 22 -60 Z", "#a5d8ff", stroke="#e7f5ff", sw=4, opacity=0.9),
                  rect(-19, -60, 38, 14, "#e7f5ff", opacity=0.6)], x, y, s)


def coussin(x, y, s=1.0, couleur="#e64980"):
    return place([ellipse(0, 0, 120, 34, _sombre(couleur)), ellipse(0, -8, 112, 30, couleur),
                  cercle(-112, 0, 10, "#fab005"), cercle(112, 0, 10, "#fab005")], x, y, s)


def _sombre(c):
    from base import _assombrir
    return _assombrir(c, 0.8)


def paille(x, y, s=1.0):
    m = [ellipse(0, 0, 230, 40, "#e8b931"), ellipse(0, -8, 210, 30, "#f6c453")]
    for k in range(14):
        a = -200 + k * 30
        m.append(trait(a, -4, a + 26, -24 + (k % 3) * 6, "#d9a514", 3))
    return place(m, x, y, s)


def marmite(x, y, s=1.0):
    return place([ellipse(0, 0, 60, 14, "#343a40"), chemin("M -60 -60 Q -66 0 0 0 Q 66 0 60 -60 Z", "#495057"),
                  ellipse(0, -60, 62, 14, "#343a40"), rect(-80, -60, 20, 8, "#343a40", rx=4), rect(60, -60, 20, 8, "#343a40", rx=4)], x, y, s)


def cuisine(S):
    interieur(S, "#4a3b6b", "#3a2c4f", y=600, papier=None, plinthe="#2e2240")
    S.add(cheminee(620, 600, 0.7, feu=True, graine=3))
    S.add(rect(30, 260, 260, 14, "#8d5b34", rx=4))
    for k, c in enumerate(["#e8590c", "#c92a2a", "#f59f00"]):
        S.add(cercle(70 + k * 80, 236, 24, c))
    S.add(table(220, 700, 300, 120, "#8d5b34"))
    S.add(pomme(160, 572, 0.8), pomme(200, 574, 0.8, "#ffd43b"), pain_rond(270, 576))


def pain_rond(x, y):
    return g([ellipse(x, y, 40, 22, "#d9a066"), chemin(f"M {x - 20} {y - 10} q 10 -6 20 0 q 10 -6 20 0", stroke="#a0693a", sw=3)])


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ciel_nuit(S, 50, 7)
    S.add(lune_perso(620, 170, 90, "content"))
    S.add(chateau_nuit(400, 700, 0.9))
    S.add(rect(0, 690, 800, 110, "#2b2463"))
    S.add(lea(380, 780, 1.6, expr="malin", bras="hanches"))
    S.add(doudou(560, 770, 0.55, expr="baille"))
    S.add(petite_etoile(170, 360, 34, "rire"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#1c2350", rx=30))
    etoiles(S, 14, 4, (10, 10, 390, 260))
    S.add(lune_perso(200, 140, 70, "dort", halo=False))
    S.add(nuage_couverture(220, 210, 0.9))
    S.add(zzz(300, 110, 0.8, "#d0bfff"))
    return S


def p01():
    S = Scene()
    ciel(S, "#5f3dc4", "#ff922b")
    S.add(cercle(150, 520, 70, "#ffd43b", opacity=0.9))
    collines(S, 600, "#7048e8", graine=2)
    S.add(chateau(560, 640, 0.75, mur="#d0bfff", mur2="#b197fc", toit="#7048e8", drapeau="#fab005", nuit_=True))
    sol(S, 620, "#5f3dc4")
    S.add(personne(230, 760, 1.5, expr="fache", bras="croises", **LEA_JOUR))
    S.add(bulle(260, 150, 360, 100, "Pas sommeil !", 52, pointe=(250, 340)))
    return S


def p02():
    S = Scene()
    chambre(S)
    S.add(fenetre_arc(70, 110, 150, 220))
    S.add(lit(250, 770, 340, "#e5dbff", "#9775fa", bois="#8d5b34"))
    S.add(reine(480, 690, 1.55, expr="content", bras="porte", **REINE))
    S.add(lea(390, 760, 1.3, expr="fache", bras="croises"))
    S.add(bulle(560, 90, 420, 90, "Bonne nuit, ma princesse.", 32, pointe=(540, 300)))
    return S


def p03():
    S = Scene()
    chambre(S)
    S.add(porte(640, 600, 160, 320, ouverte=True))
    S.add(poly([(600, 600), (680, 600), (800, 800), (560, 800)], "#ffd43b", opacity=0.18))
    S.add(lit(250, 770, 340, "#e5dbff", "#9775fa", bois="#8d5b34"))
    S.add(lea(470, 720, 1.4, expr="malin", bras="haut"))
    S.add(mouvement(330, 560, 0.9))
    S.add(bulle(330, 120, 520, 100, "Qui veut jouer avec moi ?", 40, pointe=(430, 330)))
    return S


def p04():
    S = Scene()
    murs_pierre(S)
    S.add(torche(110, 330), torche(690, 330))
    S.add(chevalier(470, 760, 1.6, plumet="#4dabf7", expr="baille", bras="donne",
                    objet=doudou(84, -82, 0.28)))
    S.add(lea(220, 770, 1.2, expr="surpris", regard=(1, -1)))
    S.add(texte(560, 120, "Aaaah…", 64, "#fff3bf", contour="#3d4677"))
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(personne(470, 760, 1.55, peau="doree", cheveux="brun", coiffure="courts", robe=False,
                   habit="#f8f9fa", jambes="#495057", acc=("toque",), expr="baille", bras="donne",
                   objet=verre_eau(84, -86, 0.9)))
    S.add(lea(230, 770, 1.2, expr="sourire", regard=(1, -1), objet=doudou(0, -66, 0.26), bras="porte"))
    S.add(texte(560, 110, "Aaaah…", 64, "#fff3bf", contour="#4a3b6b"))
    return S


def p06():
    S = Scene()
    interieur(S, "#4a3b6b", "#3a2c4f", y=600, papier="#56467a", plinthe="#2e2240")
    S.add(cheminee(400, 600, 0.75, feu=True, graine=5))
    S.add(tapis(470, 720, 260, 50, "#c2255c", "#862e9c"))
    S.add(coussin(560, 720, 0.9))
    S.add(perso("chat", 560, 712, 1.1, expr="baille", bras="haut"))
    S.add(lea(200, 770, 1.2, expr="rire", bras="haut"))
    S.add(texte(600, 110, "Miaaah…", 64, "#fff3bf", contour="#4a3b6b"))
    return S


def p07():
    S = Scene()
    murs_pierre(S, mur="#32396a", joint="#282e58", sol_c="#1f2447")
    S.add(fenetre_arc(80, 100, 140, 200))
    S.add(paille(500, 740, 1.2))
    S.add(dragon(500, 730, 1.8, expr="chante", bras="calin", **DRAGON))
    S.add(notes(300, 260, 1.1, "#fff3bf"), notes(680, 200, 0.9, "#fff3bf"))
    S.add(lea(170, 770, 1.15, expr="content", bras="porte", objet=doudou(0, -66, 0.26)))
    S.add(texte(460, 110, "Lalala, lalalou…", 54, "#fff3bf", contour="#32396a"))
    return S


def p08():
    S = Scene()
    ciel_nuit(S, 45, 11)
    S.add(lune_perso(470, 280, 150, "baille"))
    S.add(nuage_couverture(560, 420, 1.3))
    S.add(petite_etoile(250, 470, 34, "rire"))
    S.add(paillettes(300, 430, 1.0, "#fff3bf"))
    remparts(S, 640)
    S.add(lea(170, 790, 1.2, expr="bouche_bee", bras="haut", regard=(1, -1)))
    return S


def p09():
    S = Scene()
    murs_pierre(S)
    S.add(torche(110, 330, allumee=False), torche(690, 330, allumee=False))
    S.add(chevalier(600, 760, 1.4, plumet="#4dabf7", expr="dort", bras="bas"))
    S.add(zzz(690, 280, 1.0, "#d0bfff"))
    S.add(perso("chat", 140, 790, 0.6, expr="dort", bras="calin"))
    S.add(zzz(200, 600, 0.6, "#d0bfff"))
    S.add(lea(340, 770, 1.35, expr="timide", bras="porte",
              objet=g([doudou(-10, -60, 0.28), petite_etoile(30, -110, 22)])))
    return S


def p10():
    S = Scene()
    chambre(S)
    S.add(fenetre_arc(560, 110, 150, 220))
    S.add(petite_etoile(635, 300, 26, "content"))
    lit_lea(S, 330, 780, 420)
    S.add(doudou(230, 690, 0.32))
    S.add(lea(480, 790, 1.3, expr="content", bras="bouche"))
    S.add(verre_eau(495, 668, 0.75))
    return S


def p11():
    S = Scene()
    chambre(S)
    S.add(fenetre_arc(560, 110, 150, 220))
    S.add(petite_etoile(635, 300, 26, "dort"))
    lit_lea(S, 400, 780, 460, qui=g([lea(290, 735, 1.0, expr="baille"), doudou(380, 676, 0.3, expr="dort")]))
    S.add(notes(340, 380, 0.8, "#fff3bf"))
    S.add(texte(330, 180, "Aaaah…", 64, "#fff3bf", contour="#2e2a6b"))
    return S


def p12():
    S = Scene()
    chambre(S)
    S.add(fenetre_arc(80, 110, 150, 220))
    S.add(petite_etoile(155, 300, 26, "dort"))
    lit_lea(S, 400, 780, 460, qui=g([lea(290, 735, 1.0, expr="dort"), doudou(380, 676, 0.3, expr="dort")]))
    S.add(reine(620, 700, 1.4, expr="content", bras="calin", **REINE))
    S.add(coeur(420, 420, 1.3, "#f783ac"), coeur(470, 380, 0.8, "#fcc2d7"))
    S.add(zzz(330, 470, 0.9, "#d0bfff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lune-endormie.svg", vignette),
    ("01-pas-sommeil.svg", p01), ("02-les-tresses.svg", p02), ("03-qui-veut-jouer.svg", p03),
    ("04-le-garde.svg", p04), ("05-le-cuisinier.svg", p05), ("06-le-chat.svg", p06),
    ("07-le-dragon.svg", p07), ("08-la-lune.svg", p08), ("09-tout-dort.svg", p09),
    ("10-le-verre-d-eau.svg", p10), ("11-aaaah.svg", p11), ("12-bonne-nuit.svg", p12),
]
