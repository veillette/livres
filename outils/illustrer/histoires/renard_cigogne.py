"""Le Renard et la Cigogne — tel est pris qui croyait prendre."""
from fables import *

ID = "renard-cigogne"

TABLE_Y = 610  # hauteur du dessus de la table


def renard(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **k)


def chez_renard(S):
    interieur(S, "#fff4e6", "#c9a27e", 600, papier="#ffe8cc")
    S.add(fenetre(80, 110, 170, 160, "#9775fa", rideaux="#fd7e14"))
    S.add(cadre_mur(640, 180, 120, 100, "#ffc078"))


def chez_cigogne(S):
    interieur(S, "#e7f5ff", "#c9a27e", 600, papier="#d0ebff")
    S.add(fenetre(560, 110, 170, 160, "#ffc078", rideaux="#4dabf7"))
    S.add(cadre_mur(160, 180, 120, 100, "#b2f2bb"))


def dehors(S, soir=False):
    ciel(S, "#9775fa" if soir else "#a5d8ff", "#ffc9c9" if soir else "#e7f5ff")
    collines(S, 600, "#b2f2bb", graine=7)
    sol(S, 620, "#8ce99a")


def maison_renard(x, y, s=1.0):
    return maison(x, y, s, mur="#ffd8a8", toit="#e8590c", porte="#a0522d", lumiere=True)


def maison_cigogne(x, y, s=1.0):
    m = [maison(0, 0, 1.0, mur="#e7f5ff", toit="#1c7ed6", porte="#495057", lumiere=True),
         ellipse(68, -250, 40, 14, "#8d5524")]
    return place(m, x, y, s)


def table_repas(x=380, w=440):
    return table(x, 800, w, 800 - TABLE_Y, couleur="#c68642", nappe="#ffc9c9")


def carton_invitation(x, y, s=1.0, rot=-8):
    m = [rect(-80, -54, 160, 108, "#fff", rx=8, stroke="#fab005", stroke_width=5), coeur(0, -12, 0.9, "#fa5252"),
         trait(-50, 24, 50, 24, "#adb5bd", 4), trait(-40, 38, 40, 38, "#adb5bd", 4)]
    return place(m, x, y, s, rot=rot)


def couverture():
    S = Scene()
    chez_renard(S)
    S.add(renard(270, 760, 1.35, expr="rire", bras="bas"))
    S.add(table_repas(360, 420))
    S.add(assiette_plate(290, TABLE_Y + 4, 0.9))
    S.add(cigogne(640, TABLE_Y + 160, 1.05, cou="table", flip=True, expr="fache"))
    S.add(assiette_plate(495, TABLE_Y + 4, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(vase_long(110, 250, 0.7, contenu=False), assiette_plate(275, 230, 0.95))
    return S


def p01():
    S = Scene()
    dehors(S)
    S.add(maison_renard(650, 650, 0.8))
    S.add(renard(230, 760, 1.4, expr="malin", bras="donne", objet=carton_invitation(88, -100, 0.5)))
    S.add(cigogne(480, 760, 0.95, expr="surpris", flip=True, regard=(1, 0)))
    return S


def p02():
    S = Scene()
    dehors(S)
    S.add(maison_cigogne(620, 650, 0.8))
    S.add(cigogne(330, 760, 1.2, expr="rire"))
    S.add(bulle(270, 130, 400, 90, "Avec plaisir !", 40, pointe=(380, 330)))
    S.add(coeur(560, 330, 0.8))
    return S


def p03():
    S = Scene()
    dehors(S, soir=True)
    S.add(maison_renard(560, 650, 1.2))
    S.add(cigogne(230, 760, 1.1, expr="content"))
    for k in range(3):
        S.add(chemin(f"M {540 + k * 24} 450 q 12 -16 0 -32 q -12 -16 0 -32", stroke="#fff", sw=4, opacity=0.8))
    return S


def p04():
    S = Scene()
    chez_renard(S)
    S.add(renard(270, 760, 1.35, expr="malin", bras="bas"))
    S.add(table_repas())
    S.add(assiette_plate(290, TABLE_Y + 4, 0.9))
    S.add(assiette_plate(495, TABLE_Y + 4, 0.8))
    S.add(cigogne(660, TABLE_Y + 160, 1.05, cou="droit", flip=True, expr="surpris", regard=(1, 1)))
    return S


def p05():
    S = Scene()
    chez_renard(S)
    S.add(renard(270, 760, 1.35, expr="miam", bras="bas", regard=(0, 1)))
    S.add(table_repas())
    S.add(assiette_plate(290, TABLE_Y + 4, 0.9))
    S.add(assiette_plate(495, TABLE_Y + 4, 0.8))
    S.add(cigogne(660, TABLE_Y + 160, 1.05, flip=True, expr="inquiet", regard=(1, 1)))
    S.add(texte(250, 360, "Slurp !", 60, "#e8590c", contour="#fff"))
    return S


def p06():
    S = Scene()
    chez_renard(S)
    S.add(renard(270, 760, 1.35, expr="malin", bras="bas", regard=(1, 0)))
    S.add(table_repas())
    S.add(assiette_plate(290, TABLE_Y + 4, 0.9, vide=True))
    S.add(assiette_plate(495, TABLE_Y + 4, 0.8))
    S.add(cigogne(640, TABLE_Y + 160, 1.05, cou="table", flip=True, expr="concentre"))
    S.add(texte(560, 300, "Toc ! Toc !", 50, "#1c7ed6", contour="#fff"))
    return S


def p07():
    S = Scene()
    chez_renard(S)
    S.add(renard(300, 760, 1.4, expr="rire", bras="calin"))
    S.add(table_repas())
    S.add(assiette_plate(290, TABLE_Y + 4, 0.9, vide=True))
    S.add(assiette_plate(495, TABLE_Y + 4, 0.8, vide=True))
    S.add(cigogne(660, TABLE_Y + 160, 1.05, flip=True, expr="fache"))
    S.add(bulle(300, 130, 420, 90, "Vous n'avez pas faim ?", 34, pointe=(300, 440)))
    return S


def p08():
    S = Scene()
    chez_cigogne(S)
    S.add(cigogne(380, 760, 1.15, expr="malin", regard=(1, -1)))
    S.add(pensee(570, 200, 110, depuis=(470, 330), contenu=vase_long(570, 270, 0.4, contenu=False)))
    return S


def p09():
    S = Scene()
    dehors(S)
    S.add(maison_cigogne(660, 650, 0.8))
    S.add(cigogne(250, 760, 1.0, expr="malin", regard=(1, 0)))
    S.add(renard(500, 760, 1.35, expr="rire", bras="salut", flip=True))
    S.add(bulle(420, 130, 460, 100, "Venez dîner chez moi !", 36, pointe=(300, 380)))
    return S


def p10():
    S = Scene()
    dehors(S, soir=True)
    S.add(maison_cigogne(560, 650, 1.2))
    S.add(renard(240, 760, 1.45, expr="miam", bras="joues", regard=(1, -1)))
    for k in range(3):
        S.add(chemin(f"M {560 + k * 24} 470 q 12 -16 0 -32 q -12 -16 0 -32", stroke="#fff", sw=4, opacity=0.8))
    return S


def p11():
    S = Scene()
    chez_cigogne(S)
    S.add(cigogne(180, 760, 1.15, expr="malin"))
    S.add(vase_long(420, 760, 0.62))
    S.add(vase_long(620, 760, 0.62))
    S.add(renard(700, 770, 1.1, expr="surpris", bras="joues", regard=(-1, 0)))
    return S


def p12():
    S = Scene()
    chez_cigogne(S)
    S.add(vase_long(410, 760, 0.63))
    S.add(cigogne(244, 768, 1.2, cou="table", expr="content"))
    S.add(texte(560, 260, "Miam !", 64, "#1c7ed6", contour="#fff"))
    return S


def p13():
    S = Scene()
    chez_cigogne(S)
    S.add(vase_long(440, 760, 0.9, contenu=True))
    S.add(renard(300, 760, 1.35, expr="concentre", bras="large", regard=(1, -1)))
    S.add(mouvement(560, 420, 0.9))
    S.add(texte(640, 300, "Grrr !", 56, "#e8590c", contour="#fff"))
    return S


def p14():
    S = Scene()
    dehors(S, soir=True)
    S.add(lune(660, 110, 36))
    S.add(renard(400, 760, 1.5, expr="triste", bras="bas", regard=(0, 1)))
    S.add(nuage_orage(400, 230, 0.5))
    return S


def p15():
    S = Scene()
    chez_cigogne(S)
    S.add(table_repas())
    S.add(renard(230, 760, 1.25, expr="timide", bras="donne", regard=(1, 0)))
    S.add(bol(380, TABLE_Y + 4, 1.0, "#ffa94d", "#ffe066"))
    S.add(cigogne(660, TABLE_Y + 160, 1.05, cou="table", flip=True, expr="content"))
    S.add(bol(510, TABLE_Y + 4, 1.0, "#74c0fc", "#ffe066"))
    S.add(coeur(420, 320, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("assiette-et-vase.svg", vignette),
    ("01-l-invitation.svg", p01), ("02-avec-plaisir.svg", p02), ("03-ca-sent-bon.svg", p03),
    ("04-assiettes-plates.svg", p04), ("05-slurp.svg", p05), ("06-toc-toc.svg", p06),
    ("07-pas-faim.svg", p07), ("08-une-idee.svg", p08), ("09-a-mon-tour.svg", p09),
    ("10-miam.svg", p10), ("11-les-vases.svg", p11), ("12-le-bec.svg", p12),
    ("13-le-museau.svg", p13), ("14-la-queue-basse.svg", p14), ("15-pardon.svg", p15),
]
