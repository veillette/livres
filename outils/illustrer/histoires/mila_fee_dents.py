"""Mila, la petite fée des dents — pas peur du noir."""
from base import *
from objets import *
from fantastique import *

ID = "mila-fee-dents"
MILA = dict(coiffure="queue", cheveux="brun", peau="doree", habit="#9775fa", ailes="#d0ebff",
            motif_robe="#fff3bf")
MAMIE = dict(coiffure="chignon", cheveux="blanc", peau="claire", habit="#4dabf7", ailes="#d0ebff",
             acc=("lunettes",))
SAMI = dict(coiffure="courts", cheveux="noir", peau="brune", habit="#74c0fc", robe=False,
            jambes="#74c0fc", chaussures="#4dabf7")
MOUSTACHE = "#868e96"

MUR_NUIT = "#2f3b73"
SOL_NUIT = "#3d3466"


def mila(x, y, s=1.0, halo=True, **k):
    m = []
    if halo:
        m.append(cercle(x, y - 110 * s, 150 * s, "#fff3bf", opacity=0.16))
        m.append(cercle(x, y - 110 * s, 105 * s, "#fff3bf", opacity=0.18))
    m.append(personne(x, y, s, **{**MILA, **k}))
    return g(m)


def sami(x, y, s=1.0, **k):
    return personne(x, y, s, **{**SAMI, **k})


def dent(x, y, s=1.0, rot=0):
    """Petite dent de lait ; (x, y) = son centre."""
    m = [chemin("M -26 -24 Q -30 -40 -14 -40 Q 0 -34 14 -40 Q 30 -40 26 -24 Q 24 0 18 22 Q 12 36 6 20 "
                "Q 0 8 -6 20 Q -12 36 -18 22 Q -24 0 -26 -24 Z", "#ffffff", stroke="#ced4da", sw=3),
         chemin("M -16 -28 Q -18 -10 -14 4", stroke="#e9ecef", sw=5)]
    return place(m, x, y, s, rot=rot)


def piece(x, y, s=1.0, brille=True):
    """Pièce d'or brillante ; (x, y) = son centre."""
    m = []
    if brille:
        m.append(cercle(0, 0, 46, "#fff3bf", opacity=0.35))
    m += [cercle(0, 0, 30, OR, stroke=OR_FONCE, stroke_width=4), cercle(0, 0, 21, "none", stroke=OR_FONCE, stroke_width=2),
          etoile5(0, 1, 11, OR_FONCE)]
    return place(m, x, y, s)


def veilleuse(x, y, s=1.0, allumee=True):
    """Veilleuse en forme de lune posée sur un petit socle ; (x, y) = base."""
    m = []
    if allumee:
        m += [cercle(0, -60, 150, "#ffe066", opacity=0.12), cercle(0, -60, 95, "#ffe066", opacity=0.18),
              cercle(0, -60, 60, "#fff3bf", opacity=0.3)]
    c = "#fff3bf" if allumee else "#adb5bd"
    m += [rect(-34, -16, 68, 16, "#e9ecef", rx=6), rect(-8, -24, 16, 10, "#ced4da", rx=3),
          chemin("M 8 -104 A 44 44 0 1 0 22 -26 A 34 34 0 1 1 8 -104 Z", c),
          cercle(-12, -60, 3, "#868e96" if not allumee else "#f59f00"),
          chemin("M -22 -48 Q -14 -42 -6 -48", stroke="#868e96" if not allumee else "#f59f00", sw=3)]
    return place(m, x, y, s)


def table_nuit(x, y, s=1.0, couleur="#8d6e63"):
    m = [rect(-60, -110, 120, 110, couleur, rx=8), rect(-66, -118, 132, 16, assombrir(couleur, 0.85), rx=6),
         rect(-46, -86, 92, 34, assombrir(couleur, 0.9), rx=5), cercle(0, -69, 5, "#ffd43b")]
    return place(m, x, y, s)


def champi_maison(x, y, s=1.0, chapeau_c="#e64980", lumiere=True):
    """Maison-champignon des fées ; (x, y) = au sol."""
    m = [rect(-46, -120, 92, 120, "#fff4e6", rx=18),
         chemin("M -110 -100 Q -100 -220 0 -224 Q 100 -220 110 -100 Q 0 -80 -110 -100 Z", chapeau_c)]
    for px, py, r in [(-50, -150, 14), (20, -190, 12), (60, -130, 10)]:
        m.append(cercle(px, py, r, "#fff"))
    m += [chemin("M -16 0 L -16 -44 Q 0 -60 16 -44 L 16 0 Z", "#8d5524"),
          cercle(-24, -82, 14, "#ffe066" if lumiere else "#adb5bd", stroke="#8d5524", stroke_width=4)]
    return place(m, x, y, s)


def cubes_tas(x, y, s=1.0):
    m = [cube(-60, 0, 1.0, "#ff6b6b", "A"), cube(10, 0, 1.0, "#4dabf7", "B"), cube(-24, -60, 1.0, "#ffd43b", "C")]
    return place(m, x, y, s)


def chambre(S, eclairee=False, fenetre_x=520):
    """Chambre de Sami la nuit."""
    interieur(S, mur=MUR_NUIT if not eclairee else "#4c5b9a", plancher=SOL_NUIT if not eclairee else "#5c4d7d",
              y=600, plinthe="#241d44" if not eclairee else "#3b2f5c")
    S.add(fenetre(fenetre_x, 110, 190, 170, dehors="#1c2a52", cadre="#dbe4ff", nuit_=True, rideaux="#748ffc"))


def lit_sami(S, x=330, y=740, w=420, sami_k=None, couche=False, couverture="#ffa94d", oreiller_objet=None):
    """Lit vu de face, la tête du lit à gauche. Sami assis (ou couché) dedans."""
    bois = "#a0693a"
    gx = x - w / 2
    S.add(rect(gx - 16, y - 300, 32, 300, bois, rx=12), cercle(gx, y - 300, 22, bois))
    S.add(rect(x + w / 2 - 16, y - 190, 32, 190, bois, rx=12), cercle(x + w / 2, y - 190, 20, bois))
    S.add(rect(gx, y - 150, w, 60, "#f1f3f5", rx=12))
    S.add(rect(gx + 18, y - 200, 130, 62, "#ffffff", rx=26, stroke="#dee2e6", stroke_width=3))
    if oreiller_objet:
        S.add(oreiller_objet)
    if sami_k is not None:
        if couche:
            S.add(sami(gx + 270, y - 165, 0.95, rot=-90, **{**sami_k, "bras": "calin"}))
        else:
            S.add(sami(gx + 150, y - 70, 1.45, **sami_k))
    if couche:
        S.add(rect(gx + 125, y - 205, w - 119, 155, couverture, rx=40))
    else:
        S.add(rect(gx + 80, y - 160, w - 74, 110, couverture, rx=22))
    for k in range(4):
        S.add(cercle(gx + 150 + k * 70, y - 105, 9, "#fff3bf", opacity=0.8))
    S.add(rect(gx - 4, y - 60, w + 8, 36, bois, rx=8))


def ombre_nuit(S, trous, opacity=0.6):
    obscurite(S, trous=trous, couleur="#0b1433", opacity=opacity)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 40, graine=11)
    S.add(lune(640, 150, 60, croissant=True, fond_ciel="#22306a"))
    collines(S, 640, "#3b2f7a", graine=3, hauteur=80)
    S.add(maison(170, 760, 0.9, mur="#dbe4ff", toit="#1c7ed6", lumiere=False))
    S.add(mila(400, 660, 1.7, expr="content", bras="tient", objet=dent(86, -180, 0.85, rot=12)))
    S.add(etincelles(650, 560, 1.0, graine=5), etincelles(170, 300, 0.8, graine=9, couleur="#d0ebff"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 140, 120, "#e5dbff"))
    S.add(etincelles(200, 140, 1.4, graine=2, couleur="#fab005"))
    S.add(dent(140, 145, 1.5, rot=-10), piece(265, 145, 1.5))
    return S


def p01():
    S = Scene()
    nuit(S, "#1c2a52", "#4c5b9a")
    etoiles(S, 40, graine=3)
    S.add(lune(130, 130, 55, croissant=True, fond_ciel="#1e2c58"))
    sol(S, 680, "#2b8a3e")
    S.add(champi_maison(130, 720, 1.0, "#e64980"), champi_maison(660, 730, 1.2, "#7950f2"))
    S.add(champi_maison(380, 700, 0.6, "#f76707"))
    S.add(herbe(260, 700, 1.2, "#37b24d"), herbe(520, 710, 1.0, "#37b24d"))
    S.add(mila(420, 470, 1.3, expr="rire", bras="haut"))
    S.add(etincelles(640, 300, 1.0, graine=7), etincelles(200, 330, 0.8, graine=2, couleur="#d0ebff"))
    return S


def p02():
    S = Scene()
    nuit(S, "#1c2a52", "#4c5b9a")
    etoiles(S, 30, graine=4, zone=(0, 0, 800, 300))
    sol(S, 680, "#2b8a3e")
    S.add(champi_maison(400, 700, 1.3, "#e64980"))
    S.add(personne(580, 760, 1.4, expr="sourire", bras="donne2", flip=True,
                   objet=piece(90, -92, 0.7), **MAMIE))
    S.add(mila(230, 760, 1.25, expr="inquiet", bras="bas", regard=(1, 0)))
    S.add(bulle(420, 120, 560, 140, "Chez Sami, la maison au toit bleu.\nTu prends la dent, tu laisses\nla pièce. Et pas un bruit !", 32, pointe=(560, 360)))
    return S


def p03():
    S = Scene()
    nuit(S, "#141d3f", "#2f3b73")
    etoiles(S, 40, graine=8, zone=(0, 0, 800, 400))
    S.add(lune(660, 110, 45, croissant=True, fond_ciel="#18224a"))
    sol(S, 700, "#1f5130")
    # grande façade de la maison au toit bleu, fenêtre entrouverte et noire
    S.add(rect(80, 260, 640, 460, "#dbe4ff"))
    S.add(poly([(40, 280), (400, 120), (760, 280)], "#1c7ed6"))
    S.add(rect(250, 360, 300, 260, "#e9ecef"), rect(262, 372, 276, 236, "#0b1433"))
    S.add(poly([(538, 372), (600, 350), (600, 630), (538, 608)], "#ced4da"))
    S.add(rect(400 - 4, 372, 8, 236, "#e9ecef"))
    S.add(mila(320, 590, 0.75, expr="inquiet", bras="porte", regard=(-1, 0)))
    S.add(bulle(400, 730, 740, 84, "Les fées n'ont pas peur… enfin, presque pas.", 30))
    return S


def p04():
    S = Scene()
    chambre(S)
    S.add(porte(140, 600, 170, 380, "#6d4c41"))
    S.add(robe_chambre(140, 270, 0.9, "#7950f2"))
    # ombre immense sur le mur
    S.add(place(monstre_ombre(0, 0, 1.0, "#0b1433", yeux=False), 470, 190, 1.7, sy=1.6))
    ombre_nuit(S, [trou_doux(560, 640, 200, "#555")], 0.55)
    S.add(mila(520, 720, 0.7, expr="surpris", bras="joues", regard=(-1, -1)))
    S.add(cubes_tas(640, 770, 1.2))
    S.add(texte(400, 90, "Boum, boum, boum !", 50, "#fff3bf", contour="#1c2a52"))
    return S


def p05():
    S = Scene()
    chambre(S)
    S.add(etagere(620, 300, 300, "#a0693a", livres_pile(560, 300, 0.9)))
    S.add(perso("chat", 300, 790, 1.5, couleur=MOUSTACHE, expr="neutre", regard=(1, -1)))
    ombre_nuit(S, [trou_doux(680, 230, 170, "#555")], 0.75)
    # yeux jaunes qui brillent dans le noir
    for sgn in (-1, 1):
        S.add(cercle(300 + sgn * 19 * 1.5, 790 - 152 * 1.5, 26, "#ffe066", opacity=0.25))
        S.add(ellipse(300 + sgn * 19 * 1.5, 790 - 152 * 1.5, 15, 13, "#ffe066"))
        S.add(ellipse(300 + sgn * 19 * 1.5 + 3, 790 - 152 * 1.5 - 3, 4, 9, ENCRE))
    S.add(mila(690, 296, 0.75, expr="oups", bras="joues", regard=(-1, 1)))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(table_nuit(700, 760, 1.0))
    S.add(veilleuse(700, 642, 0.9, allumee=False))
    lit_sami(S, 330, 780, sami_k=dict(expr="inquiet", bras="porte", regard=(1, 0)))
    ombre_nuit(S, [trou_doux(560, 480, 220, "#333")], 0.6)
    S.add(mila(560, 560, 0.6, expr="surpris", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(250, 150, 300, 90, "Qui est là ?", 40, pointe=(250, 400)))
    return S


def p07():
    S = Scene()
    chambre(S)
    S.add(table_nuit(700, 760, 1.0))
    S.add(veilleuse(700, 642, 0.9, allumee=False))
    lit_sami(S, 330, 780, sami_k=dict(expr="timide", bras="porte", regard=(1, 0)))
    ombre_nuit(S, [trou_doux(450, 470, 280, "#333")], 0.55)
    S.add(mila(520, 560, 0.6, expr="sourire", bras="salut", regard=(-1, 0)))
    S.add(bulle(250, 110, 420, 120, "Ce n'est pas toi qui\nme fais peur, c'est le noir.", 30, pointe=(250, 330)))
    S.add(bulle(620, 290, 250, 80, "Moi aussi !", 36, pointe=(540, 430)))
    return S


def p08():
    S = Scene()
    chambre(S, eclairee=True)
    S.add(table_nuit(660, 760, 1.0))
    S.add(veilleuse(660, 642, 1.1, allumee=True))
    lit_sami(S, 290, 780, sami_k=dict(expr="bouche_bee", bras="bas", regard=(1, 0)))
    S.add(mila(588, 642, 0.6, expr="concentre", bras="large", regard=(1, 0), halo=False))
    S.add(texte(620, 470, "Clic !", 60, "#fff3bf", contour="#5f3dc4"))
    return S


def p09():
    S = Scene()
    chambre(S, eclairee=True, fenetre_x=560)
    S.add(porte(170, 600, 170, 380, "#8d6e63"))
    S.add(robe_chambre(170, 270, 0.9, "#7950f2"))
    S.add(place(monstre_ombre(0, 0, 1.0, "#1c2a52", yeux=False), 330, 280, 0.8, sy=0.8), )
    S.add(sami(470, 780, 1.4, expr="rire", bras="montre", regard=(-1, 0)))
    S.add(veilleuse(700, 780, 0.9))
    S.add(mila(640, 520, 0.6, expr="rire", bras="haut", halo=False))
    S.add(bulle(400, 70, 600, 80, "Bonsoir, Madame Robe de Chambre !", 32))
    return S


def p10():
    S = Scene()
    chambre(S, eclairee=True)
    S.add(table_nuit(700, 760, 1.0))
    S.add(veilleuse(700, 642, 0.9, allumee=True))
    lit_sami(S, 320, 780, sami_k=dict(expr="content", bras="bas", regard=(1, 1)))
    S.add(perso("chat", 470, 640, 0.75, couleur=MOUSTACHE, expr="content"))
    S.add(mila(540, 470, 0.5, expr="rire", bras="salut", regard=(-1, 0), halo=False))
    S.add(texte(560, 330, "Rrrr… rrrr…", 44, "#fff3bf", contour="#3b2f5c"))
    return S


def p11():
    S = Scene()
    chambre(S, eclairee=True, fenetre_x=440)
    S.add(etoile5(470, 150, 12, "#ffe066"), etoile5(600, 230, 10, "#ffe066"), etoile5(500, 250, 8, "#ffe066"))
    S.add(veilleuse(720, 780, 0.8))
    lit_sami(S, 300, 780, sami_k=dict(expr="baille", bras="bas", regard=(1, -1)))
    S.add(mila(500, 520, 0.5, expr="sourire", bras="montre", regard=(1, -1), halo=False))
    for k, (tx, ty) in enumerate([(120, 120), (230, 90), (340, 130)]):
        S.add(texte(tx, ty, str(k + 1), 56, "#fff3bf", contour="#3b2f5c"))
    S.add(texte(250, 210, "… sept !", 46, "#fff3bf", contour="#3b2f5c"))
    return S


def p12():
    S = Scene()
    chambre(S, eclairee=True, fenetre_x=540)
    S.add(veilleuse(110, 780, 0.8))
    # lit vu depuis le pied : Sami dort, la couverture jusqu'au menton
    bois = "#a0693a"
    S.add(rect(190, 330, 360, 330, bois, rx=30), rect(215, 360, 310, 290, assombrir(bois, 0.85), rx=24))
    S.add(rect(240, 470, 260, 110, "#ffffff", rx=44, stroke="#dee2e6", stroke_width=3))
    S.add(sami(370, 700, 1.35, expr="dort", bras="bas"))
    S.add(piece(495, 528, 0.6))
    S.add(chemin("M 160 800 L 170 600 Q 175 560 230 556 L 510 556 Q 565 560 570 600 L 580 800 Z", "#ffa94d"))
    for k in range(4):
        S.add(cercle(240 + k * 85, 650 + (k % 2) * 40, 11, "#fff3bf", opacity=0.8))
    S.add(rect(150, 740, 440, 60, bois, rx=10))
    S.add(zzz(470, 380, 1.0, "#d0ebff"))
    S.add(mila(640, 290, 0.6, expr="content", bras="tient", objet=dent(76, -168, 0.7, rot=10)))
    S.add(etincelles(700, 360, 0.6, graine=3))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("dent-piece.svg", vignette),
    ("01-premiere-nuit.svg", p01), ("02-mamie-plume.svg", p02), ("03-la-fenetre.svg", p03),
    ("04-l-ombre.svg", p04), ("05-les-yeux.svg", p05), ("06-qui-est-la.svg", p06),
    ("07-moi-aussi.svg", p07), ("08-la-veilleuse.svg", p08), ("09-robe-de-chambre.svg", p09),
    ("10-moustache.svg", p10), ("11-les-etoiles.svg", p11), ("12-bonne-nuit.svg", p12),
]
