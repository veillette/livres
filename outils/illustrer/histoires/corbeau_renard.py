"""Le Corbeau et le Renard — se méfier des flatteurs."""
from fables import *

ID = "corbeau-renard"


def foret(S, ciel_haut="#a5d8ff", ciel_bas="#e7f5ff"):
    ciel(S, ciel_haut, ciel_bas)
    S.add(nuage(150, 120, 0.7), nuage(420, 90, 0.5))
    collines(S, 620, "#b2f2bb", graine=4)
    sol(S, 640, "#8ce99a")
    S.add(sapin(70, 660, 0.9), sapin(160, 650, 0.7, "#37b24d", "#2f9e44"))


def grand_arbre(S, x=620, branche_y=330, branche_x=300):
    """Tronc à droite et longue branche horizontale vers la gauche."""
    S.add(rect(x - 45, 0, 90, 700, "#8d5524"))
    S.add(chemin(f"M {x - 40} {branche_y + 26} Q {(x + branche_x) / 2} {branche_y + 10} {branche_x} {branche_y + 4} L {branche_x} {branche_y + 26} Q {(x + branche_x) / 2} {branche_y + 40} {x - 40} {branche_y + 56} Z", "#8d5524"))
    for fx, fy, r in [(x - 20, 60, 130), (x + 110, 130, 110), (x - 170, 120, 90), (x + 60, -10, 120), (branche_x + 10, branche_y - 20, 50)]:
        S.add(cercle(fx, fy, r, "#40c057"))
    for fx, fy, r in [(x - 90, 170, 60), (x + 60, 230, 70)]:
        S.add(cercle(fx, fy, r, "#51cf66"))
    S.add(chemin(f"M {x - 30} 500 Q {x - 20} 580 {x - 30} 690", stroke="#6d4424", sw=4))
    S.add(ellipse(x, 700, 90, 14, "#6d4424", opacity=0.4))


def scene_arbre(S, **k):
    foret(S)
    grand_arbre(S, **k)


def couverture():
    S = Scene()
    scene_arbre(S, x=630, branche_y=480, branche_x=330)
    S.add(corbeau(480, 486, 1.2, expr="fier", fromage_bec=True))
    S.add(perso("renard", 280, 790, 1.25, expr="malin", bras="ouverts", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(fromage(200, 150, 3.0))
    return S


def p01():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.65, expr="fier"))
    S.add(paillettes(300, 200, 1.0))
    return S


def p02():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 640, "#8ce99a")
    S.add(maison(520, 700, 1.9, mur="#ffe8cc", toit="#c92a2a"))
    S.add(barriere(160, 700, 0.8, largeur=320))
    S.add(corbeau(250, 330, 1.3, expr="joie", ailes="ouvertes", fromage_bec=True, rot=-10))
    S.add(mouvement(120, 380, 1.2, rot=10))
    return S


def p03():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.65, expr="content", fromage_bec=True))
    S.add(coeur(310, 200, 0.8))
    return S


def p04():
    S = Scene()
    foret(S)
    S.add(buisson(640, 660, 1.0, baies="#fa5252"))
    S.add(perso("renard", 380, 760, 1.6, expr="surpris", bras="bas", regard=(-1, -1)))
    for k in range(3):
        S.add(chemin(f"M {300 - k * 30} {330 - k * 40} q 20 -20 0 -40 q -20 -20 0 -40", stroke="#fab005", sw=5))
    S.add(bulle(560, 160, 300, 100, "Mmmh…", 50, pointe=(440, 360)))
    return S


def p05():
    S = Scene()
    scene_arbre(S, branche_y=160, branche_x=280)
    S.add(corbeau(400, 164, 1.1, expr="fier", fromage_bec=True))
    S.add(perso("renard", 300, 770, 1.45, expr="bouche_bee", bras="bas", regard=(1, -1)))
    S.add(pensee(140, 470, 70, depuis=(250, 540)))
    S.add(fromage(140, 470, 1.3))
    return S


def p06():
    S = Scene()
    scene_arbre(S, branche_y=160, branche_x=280)
    S.add(corbeau(400, 164, 1.1, expr="rire", fromage_bec=True))
    S.add(perso("renard", 320, 560, 1.3, expr="concentre", bras="haut", regard=(1, -1), pieds_haut=True))
    S.add(mouvement(320, 660, 1.2, rot=-90))
    S.add(texte(160, 330, "Hop !", 60, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.2, expr="surpris", fromage_bec=True, regard=(0, 1)))
    S.add(perso("renard", 260, 770, 1.45, expr="malin", bras="coucou", regard=(1, -1)))
    S.add(bulle(230, 120, 370, 110, "Eh ! Bonjour,\nMonsieur du Corbeau !", 32, pointe=(250, 470)))
    return S


def p08():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.2, expr="timide", fromage_bec=True, regard=(0, 1)))
    S.add(perso("renard", 260, 770, 1.45, expr="content", bras="joues", regard=(1, -1)))
    S.add(bulle(220, 120, 380, 110, "Que vous êtes joli !\nQue vous êtes beau !", 32, pointe=(240, 470)))
    S.add(coeur(120, 460, 0.8), coeur(170, 420, 0.6))
    return S


def p09():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.55, expr="fier", fromage_bec=True, ailes="haut"))
    S.add(paillettes(290, 170, 1.2), paillettes(540, 190, 1.0))
    S.add(etoile5(300, 300, 16, "#ffd43b"), etoile5(560, 320, 12, "#ffd43b"))
    return S


def p10():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.2, expr="fier", fromage_bec=True, regard=(0, 1)))
    S.add(perso("renard", 260, 770, 1.45, expr="malin", bras="ouverts", regard=(1, -1)))
    S.add(bulle(210, 110, 400, 120, "Et votre chant doit\nêtre encore plus beau !", 30, pointe=(240, 470)))
    return S


def p11():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.35, expr="chante", bec_ouvert=True, ailes="ouvertes"))
    S.add(fromage(430, 400, 1.1, rot=40))
    S.add(texte(210, 190, "CROÂ !", 72, "#343a40", contour="#fff", rot=-8))
    S.add(notes(280, 290, 1.0))
    return S


def p12():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.2, expr="bouche_bee", regard=(0, 1)))
    S.add(perso("renard", 400, 770, 1.45, expr="joie", bras="haut", regard=(0, -1)))
    S.add(fromage(400, 430, 1.2, rot=20))
    S.add(mouvement(400, 350, 1.0, rot=90))
    return S


def p13():
    S = Scene()
    foret(S)
    S.add(perso("renard", 450, 770, 1.55, expr="malin", bras="tient", objet=fromage(68, -150, 1.0)))
    S.add(bulle(360, 130, 520, 130, "Cette leçon vaut bien\nun fromage, non ?", 36, pointe=(420, 380)))
    return S


def p14():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.65, expr="triste"))
    S.add(nuage_orage(420, 130, 0.5))
    S.add(rect(0, 0, 800, 800, "#1c2a52", opacity=0.12))
    return S


def p15():
    S = Scene()
    scene_arbre(S)
    S.add(corbeau(420, 334, 1.3, expr="malin", fromage_bec=True))
    S.add(pie(200, 334, 1.0, expr="malin", regard=(1, 0)))
    S.add(bulle(220, 120, 320, 90, "Que tu es beau !", 34, pointe=(220, 210)))
    S.add(texte(430, 470, "Mmm-mmm !", 40, "#343a40", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fromage-seul.svg", vignette),
    ("01-maitre-corbeau.svg", p01), ("02-le-fromage.svg", p02), ("03-perche.svg", p03),
    ("04-le-flair.svg", p04), ("05-trop-haut.svg", p05), ("06-hop.svg", p06),
    ("07-bonjour.svg", p07), ("08-compliments.svg", p08), ("09-fier.svg", p09),
    ("10-le-chant.svg", p10), ("11-croa.svg", p11), ("12-attrape.svg", p12),
    ("13-la-lecon.svg", p13), ("14-honteux.svg", p14), ("15-bec-ferme.svg", p15),
]
