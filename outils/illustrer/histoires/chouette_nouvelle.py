"""Coline la nouvelle — la différence et l'amitié."""
from base import *
from objets import *

ID = "chouette-nouvelle"
COLINE = dict(couleur="#b08968", visage="#f3dcc3")
MAITRESSE = dict(couleur="#8f5f3a", acc=("lunettes",), habit="#9775fa")


def clairiere(S, soir=False):
    if soir:
        ciel(S, "#364fc7", "#f783ac")
    else:
        ciel(S, "#99e9f2", "#f3f9ff")
    collines(S, 580, "#8ce99a" if not soir else "#5c7cfa", graine=3)
    sol(S, 580, "#b2f2bb" if not soir else "#748ffc", couleur2="#8ce99a" if not soir else "#5c7cfa", y2=690)


def branche(x, y, w=260, flip=False):
    m = [chemin(f"M 0 0 Q {w * 0.5} -14 {w} 6", stroke="#8d5524", sw=22),
         ellipse(w * 0.7, -20, 30, 12, "#51cf66", rot=-20), ellipse(w * 0.9, -6, 26, 10, "#40c057", rot=20)]
    return place(m, x, y, 1.0, flip=flip)


def gros_arbre(x, y, s=1.0):
    return arbre(x, y, s, "#40c057", "#2f9e44", "#7c4a1e")


def tableau(x, y, contenu, s=1.0):
    m = [trait(-90, 0, -60, -230, "#8d5524", 10), trait(90, 0, 60, -230, "#8d5524", 10),
         rect(-120, -260, 240, 150, "#2b8a3e", rx=8, stroke="#8d5524", stroke_width=10),
         texte(0, -176, contenu, 24, "#fff", poids=500)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(660, 640, 1.2))
    S.add(branche(430, 560, 330))
    S.add(chouette(520, 550, 1.45, expr="sourire", regard=(-1, 0.3), **COLINE))
    S.add(perso("souris", 260, 750, 1.1, expr="rire", bras="salut", regard=(1, -0.5)))
    S.add(perso("lapin", 400, 760, 1.15, expr="content", regard=(1, -0.5)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chouette(200, 265, 1.2, expr="sourire", **COLINE))
    return S


def p01():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(90, 600, 0.9))
    S.add(tableau(560, 590, "Bienvenue Coline !", 1.1))
    S.add(perso("ours", 330, 640, 1.5, expr="sourire", bras="montre", **MAITRESSE))
    S.add(chouette(470, 620, 1.1, expr="timide", **COLINE))
    for k, (esp, x) in enumerate([("lapin", 150), ("herisson", 310), ("souris", 480), ("renard", 650)]):
        S.add(perso(esp, x, 790, 0.95, expr="surpris", regard=(0.4, -1)))
    return S


def p02():
    S = Scene()
    clairiere(S)
    S.add(chouette(560, 700, 1.5, expr="surpris", regard=(-1, 0), **COLINE))
    for k in (-1, 1):
        S.add(chemin(f"M {560 + k * 120} 420 A 130 90 0 0 {1 if k > 0 else 0} {560 + k * 40} 330", stroke="#ffffff", sw=7))
        S.add(poly([(560 + k * 40, 318), (560 + k * 40, 342), (560 + k * 58, 330)] if k > 0 else [(520, 318), (520, 342), (502, 330)], "#fff"))
    S.add(perso("souris", 240, 760, 1.2, expr="surpris", regard=(-1, 0)))
    S.add(perso("lapin", 120, 760, 1.25, expr="malin", bras="bouche", regard=(1, 0)))
    S.add(bulle(260, 190, 380, 90, "Qu'elle est bizarre !", 36, pointe=(160, 450)))
    return S


def p03():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(160, 640, 1.2))
    S.add(branche(150, 420, 280))
    S.add(chouette(300, 410, 1.1, expr="dort", **COLINE))
    S.add(zzz(360, 250, 1.1, "#5c7cfa"))
    S.add(perso("renard", 480, 760, 1.0, expr="rire", bras="haut"))
    S.add(ballon_jeu(590, 470, 30))
    S.add(perso("herisson", 680, 760, 0.95, expr="rire", bras="haut", regard=(-1, -1)))
    S.add(perso("lapin", 580, 790, 0.9, expr="joie", bras="course"))
    return S


def p04():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(620, 640, 1.3))
    S.add(branche(640, 480, 330, flip=True))
    S.add(chouette(460, 470, 1.35, expr="triste", regard=(-1, 0.5), **COLINE))
    S.add(perso("renard", 120, 700, 0.55, expr="rire", bras="haut"))
    S.add(perso("lapin", 200, 700, 0.55, expr="rire", bras="haut"))
    S.add(perso("herisson", 270, 700, 0.5, expr="rire", bras="haut"))
    S.add(ballon_jeu(190, 540, 16))
    return S


def p05():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(640, 640, 1.2))
    S.add(branche(640, 520, 300, flip=True))
    S.add(chouette(470, 510, 1.2, expr="surpris", regard=(-1, 0.6), **COLINE))
    S.add(perso("souris", 250, 760, 1.4, expr="sourire", bras="donne", regard=(1, -0.6)))
    S.add(bulle(300, 170, 460, 110, "Tu veux jouer\nà cache-cache ?", 38, pointe=(260, 410)))
    return S


def p06():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(640, 660, 1.3))
    S.add(perso("lapin", 700, 520, 0.9, expr="malin", regard=(1, 0)))
    S.add(rect(600, 380, 50, 300, "#7c4a1e", rx=10))
    S.add(perso("herisson", 180, 780, 1.0, expr="rire"))
    for k in range(14):
        S.add(ellipse(110 + (k * 23) % 160, 720 + (k * 17) % 60, 26, 12, ["#f08c00", "#e8590c", "#fab005"][k % 3], rot=(k * 40) % 180))
    S.add(chouette(400, 740, 1.3, expr="rire", ailes="ouvertes", regard=(-1, 0), **COLINE))
    S.add(bulle(400, 150, 380, 90, "Je vous vois !", 44, pointe=(400, 450)))
    return S


def p07():
    S = Scene()
    clairiere(S, soir=True)
    S.add(lune(640, 130, 45))
    etoiles(S, 18, 3, (0, 0, 800, 300))
    S.add(chemin("M 0 780 Q 300 700 520 640 T 800 600", stroke="#dbe4ff", sw=40, opacity=0.6))
    S.add(chouette(560, 470, 1.2, expr="rire", ailes="haut", regard=(-1, 0.5), **COLINE))
    S.add(perso("souris", 330, 720, 0.85, expr="content", regard=(1, -1)))
    S.add(perso("lapin", 210, 760, 0.95, expr="sourire", regard=(1, -1)))
    S.add(perso("herisson", 100, 790, 0.85, expr="sourire", regard=(1, -1)))
    for x, y in [(420, 400), (300, 520), (700, 560), (150, 460)]:
        S.add(cercle(x, y, 6, "#ffe066"), cercle(x, y, 14, "#ffe066", opacity=0.3))
    S.add(texte(330, 380, "Par ici !", 48, "#fff3bf"))
    return S


def p08():
    S = Scene()
    clairiere(S)
    S.add(gros_arbre(400, 590, 1.3))
    S.add(branche(400, 440, 220))
    S.add(chouette(520, 430, 1.1, expr="rire", ailes="ouvertes", **COLINE))
    for k, (esp, x, ex) in enumerate([("lapin", 130, "rire"), ("herisson", 270, "content"), ("souris", 410, "rire"),
                                      ("renard", 550, "content"), ("ours", 690, "sourire")]):
        S.add(perso(esp, x, 780, 1.0 if esp != "ours" else 1.2, expr=ex, bras="haut" if k % 2 == 0 else "salut",
                    **(MAITRESSE if esp == "ours" else {})))
    S.add(coeur(260, 300, 1.2), coeur(700, 280, 0.9, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("coline-seule.svg", vignette),
    ("01-la-nouvelle.svg", p01), ("02-bizarre.svg", p02), ("03-sieste.svg", p03),
    ("04-toute-seule.svg", p04), ("05-souris.svg", p05), ("06-cache-cache.svg", p06),
    ("07-par-ici.svg", p07), ("08-amis.svg", p08),
]
