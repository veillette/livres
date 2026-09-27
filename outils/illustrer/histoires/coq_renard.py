"""Le Coq et le Renard — c'est double plaisir de tromper le trompeur."""
from fables import *

ID = "coq-renard"


def renard(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **k)


def ferme(S, soir=False):
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#e7f5ff")
    S.add(nuage(160, 110, 0.6))
    collines(S, 600, "#b2f2bb", graine=31)
    sol(S, 620, "#8ce99a")
    S.add(barriere(620, 680, 0.8, largeur=360))


def arbre_perchoir(S, x=560, branche_y=370, branche_x=320):
    S.add(rect(x - 40, 0, 80, 700, "#8d5524"))
    S.add(chemin(f"M {x - 36} {branche_y + 24} Q {(x + branche_x) / 2} {branche_y + 8} {branche_x} {branche_y + 4} L {branche_x} {branche_y + 24} Q {(x + branche_x) / 2} {branche_y + 36} {x - 36} {branche_y + 52} Z", "#8d5524"))
    for fx, fy, r in [(x - 10, 50, 130), (x + 130, 120, 110), (x - 160, 110, 90), (x + 60, -20, 120), (branche_x - 10, branche_y - 20, 46)]:
        S.add(cercle(fx, fy, r, "#40c057"))
    S.add(cercle(x - 90, 170, 60, "#51cf66"), cercle(x + 70, 220, 70, "#51cf66"))
    S.add(ellipse(x, 700, 80, 12, "#6d4424", opacity=0.4))


def scene_arbre(S, soir=False, **k):
    ferme(S, soir)
    arbre_perchoir(S, **k)


def poulailler(x, y, s=1.0):
    m = [rect(-110, -130, 220, 130, "#e8590c"), poly([(-130, -120), (0, -200), (130, -120)], "#c92a2a"),
         chemin("M -30 0 L -30 -60 Q -30 -90 0 -90 Q 30 -90 30 -60 L 30 0 Z", "#343a40"),
         chemin("M -20 0 L 60 60", stroke="#a0522d", sw=10)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    scene_arbre(S, x=610, branche_y=450, branche_x=340)
    S.add(coq(470, 456, 1.2, expr="malin", regard=(-1, 1)))
    S.add(renard(270, 790, 1.3, expr="malin", bras="ouverts", regard=(1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(coq(200, 255, 1.6, expr="fier"))
    return S


def p01():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.6, expr="fier", regard=(-1, 0)))
    S.add(paillettes(300, 170, 1.0))
    return S


def p02():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="surpris", regard=(-1, 1)))
    S.add(renard(230, 760, 1.45, expr="sourire", bras="salut", regard=(1, -1)))
    S.add(bulle(250, 110, 380, 100, "Frère !\nGrande nouvelle !", 36, pointe=(240, 440)))
    return S


def p03():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="neutre", regard=(-1, 1)))
    S.add(renard(230, 760, 1.45, expr="rire", bras="ouverts", regard=(1, -1)))
    S.add(bulle(240, 110, 400, 110, "C'est la paix !\nTous les animaux\nsont amis !", 30, pointe=(240, 440)))
    S.add(coeur(110, 380, 0.8), coeur(380, 400, 0.6))
    return S


def p04():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="neutre", regard=(-1, 1)))
    S.add(renard(230, 760, 1.45, expr="malin", bras="ouverts", regard=(1, -1)))
    S.add(bulle(250, 110, 420, 110, "Descends vite,\nque je t'embrasse !", 34, pointe=(240, 440)))
    return S


def p05():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.6, expr="malin", regard=(-1, 1)))
    S.add(pensee(170, 150, 110, depuis=(330, 230), contenu=g([perso("renard", 150, 220, 0.45, expr="malin", bras="ouverts"), texte(230, 130, "?", 50, "#b02a37")])))
    return S


def p06():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="rire", ailes="haut", regard=(-1, 1)))
    S.add(renard(230, 760, 1.45, expr="content", bras="bas", regard=(1, -1)))
    S.add(bulle(260, 110, 440, 110, "Quelle merveilleuse\nnouvelle !", 34, pointe=(390, 250)))
    return S


def p07():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 370, 1.4, expr="malin", regard=(1, 0), ailes="ouvertes"))
    S.add(renard(230, 760, 1.35, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(chemin("M 480 230 L 780 400", stroke="#fff", sw=5, stroke_dasharray="12 14"))
    S.add(bulle(250, 110, 440, 110, "Tiens ! Je vois deux\nchiens qui arrivent !", 32, pointe=(380, 250)))
    return S


def p08():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="malin", regard=(-1, 1)))
    S.add(renard(230, 760, 1.35, expr="oups", bras="joues", regard=(1, 0)))
    S.add(bulle(250, 100, 460, 120, "Attendons-les ! Nous nous\nembrasserons tous\nensemble !", 30, pointe=(380, 250)))
    return S


def p09():
    S = Scene()
    ferme(S)
    S.add(renard(400, 760, 1.8, expr="oups", bras="joues", couleur="#ffa94d"))
    S.add(texte(620, 300, "Des chiens ?", 50, "#b02a37", contour="#fff"))
    S.add(goutte(520, 420, 1.2, "#74c0fc"))
    return S


def p10():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.3, expr="malin", regard=(-1, 1)))
    S.add(renard(230, 760, 1.35, expr="oups", bras="salut", regard=(1, -1)))
    S.add(bulle(250, 110, 460, 110, "Adieu ! Ma route\nest longue !", 34, pointe=(240, 440)))
    return S


def p11():
    S = Scene()
    ferme(S)
    S.add(chemin("M 0 760 Q 400 690 800 720 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(renard(260, 740, 1.5, expr="oups", bras="course", flip=True, rot=14))
    S.add(mouvement(460, 560, 1.4, rot=180), mouvement(480, 460, 1.1, rot=180))
    S.add(texte(620, 300, "Zou !", 60, "#b02a37", contour="#fff"))
    return S


def p12():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.6, expr="rire", ailes="haut"))
    S.add(texte(200, 520, "Ha ha ha !", 56, "#b02a37", contour="#fff"))
    return S


def p13():
    S = Scene()
    scene_arbre(S)
    S.add(coq(420, 376, 1.6, expr="chante", ailes="ouvertes", bec_ouvert=True))
    S.add(texte(200, 180, "Cocorico !", 56, "#b02a37", contour="#fff", rot=-8))
    S.add(notes(260, 280, 1.0))
    return S


def p14():
    S = Scene()
    ferme(S)
    S.add(poulailler(160, 660, 0.9))
    S.add(coq(420, 740, 1.5, expr="rire", ailes="haut"))
    S.add(coq(620, 750, 1.0, poule=True, expr="surpris"))
    S.add(coq(260, 770, 0.9, poule=True, expr="rire", couleur="#f8f9fa", ventre="#fff"))
    S.add(coq(720, 770, 0.8, poule=True, expr="bouche_bee"))
    return S


def p15():
    S = Scene()
    scene_arbre(S, soir=True)
    S.add(coq(420, 376, 1.3, expr="malin", regard=(-1, 1)))
    S.add(renard(230, 760, 1.35, expr="fache", bras="croises", regard=(1, -1)))
    S.add(bulle(260, 110, 440, 110, "Alors, renard,\ntoujours pressé ?", 34, pointe=(390, 250)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("coq-seul.svg", vignette),
    ("01-le-vieux-coq.svg", p01), ("02-grande-nouvelle.svg", p02), ("03-la-paix.svg", p03),
    ("04-descends.svg", p04), ("05-mefiance.svg", p05), ("06-quelle-nouvelle.svg", p06),
    ("07-deux-chiens.svg", p07), ("08-attendons-les.svg", p08), ("09-des-chiens.svg", p09),
    ("10-adieu.svg", p10), ("11-zou.svg", p11), ("12-ha-ha-ha.svg", p12),
    ("13-cocorico.svg", p13), ("14-les-poules.svg", p14), ("15-toujours-presse.svg", p15),
]
