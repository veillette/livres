"""Le Cerf se voyant dans l'eau — on admire le beau, on oublie l'utile."""
from fables import *
from contes import foret

ID = "cerf-eau"

VERT = "#2b8a3e"
EAU_Y = 470


def source(S, soir=False, graine=121):
    """Clairière avec une source claire ; le bord de l'eau est en y = EAU_Y."""
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#ebfbee")
    for k in range(6):
        S.add(arbre(-20 + k * 170, 400 + (k % 2) * 16, 0.75, "#51cf66", "#40c057"))
    sol(S, 400, "#8ce99a")
    S.add(rect(0, EAU_Y, 800, 800 - EAU_Y, "#74c0fc"))
    S.add(rect(0, EAU_Y - 6, 800, 12, "#69db7c"))


def reflet(dessin, opacity=0.45):
    """Le même dessin, retourné sous la ligne d'eau (dessin fait avec ses pieds en y = EAU_Y)."""
    return g(dessin, transform=f"translate(0 {2 * EAU_Y}) scale(1 -1)", opacity=opacity)


def ondes_eau():
    return g([chemin(f"M {80 + k * 160} {EAU_Y + 60 + (k % 3) * 90} q 25 -8 50 0", stroke="#d0ebff", sw=4) for k in range(5)])


def cerf_et_reflet(S, x, s=1.2, **k):
    # deux dessins distincts : chacun garde ses propres identifiants SVG
    S.add(reflet(cerf_profil(x, EAU_Y, s, **k)))
    S.add(ondes_eau())
    S.add(cerf_profil(x, EAU_Y, s, **k))


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def couverture():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 340, 1.0, expr="fier", regard=(1, 1))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cerf_profil(170, 262, 0.62, expr="fier"))
    return S


def p01():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 330, 1.0, expr="content", tete_basse=True)
    return S


def p02():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 330, 1.0, expr="bouche_bee", tete_basse=True, regard=(1, 1))
    S.add(texte(530, 110, "Oh ! Quels beaux bois !", 40, VERT, contour="#fff"))
    return S


def p03():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 320, 1.0, expr="fier", regard=(1, 1))
    S.add(paillettes(560, 110, 1.2))
    S.add(texte(620, 200, "Magnifique !", 44, VERT, contour="#fff"))
    return S


def p04():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 320, 1.0, expr="degoute", regard=(1, 1))
    S.add(cercle(320, EAU_Y - 50, 100, "none", stroke="#fa5252", stroke_width=6, stroke_dasharray="16 12"))
    S.add(texte(620, 150, "Quelles pattes", 42, VERT, contour="#fff"))
    S.add(texte(620, 200, "de fuseau !", 42, VERT, contour="#fff"))
    return S


def p05():
    S = Scene()
    source(S)
    cerf_et_reflet(S, 320, 1.0, expr="triste", regard=(1, 1))
    S.add(bulle(400, 70, 640, 110, "Si seulement elles étaient\naussi belles que mes bois !", 34))
    return S


def p06():
    S = Scene()
    source(S)
    S.add(cerf_profil(520, EAU_Y, 1.0, expr="surpris", flip=True, regard=(1, 0)))
    S.add(buisson(140, 470, 1.4))
    S.add(loup(180, 450, 1.0, expr="furieux", bras="ouverts", regard=(1, 0)))
    S.add(texte(600, 640, "Un loup !", 56, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    collines(S, 540, "#b2f2bb", graine=122)
    sol(S, 560, "#8ce99a")
    S.add(cerf_profil(470, 720, 1.2, expr="concentre", course=True))
    S.add(mouvement(240, 560, 1.6), mouvement(260, 640, 1.2))
    S.add(texte(470, 200, "Ses jambes l'emportent !", 44, VERT, contour="#fff"))
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    collines(S, 540, "#b2f2bb", graine=123)
    sol(S, 560, "#8ce99a")
    S.add(cerf_profil(560, 740, 1.1, expr="rire", course=True))
    S.add(mouvement(360, 600, 1.4))
    S.add(loup(110, 650, 0.55, expr="fache", bras="course", flip=True))
    S.add(texte(400, 200, "Plus vite que le vent !", 44, VERT, contour="#fff"))
    return S


def branches(x, y, s=1.0):
    return place([chemin("M -200 -60 Q -60 -120 40 -60 Q 120 -20 220 -80", stroke="#6d4424", sw=18),
                  chemin("M -120 -200 Q -40 -100 10 -40", stroke="#6d4424", sw=12),
                  chemin("M 160 -220 Q 120 -120 60 -60", stroke="#6d4424", sw=12),
                  cercle(-170, -110, 40, "#2f9e44"), cercle(190, -120, 46, "#2f9e44"), cercle(-60, -150, 30, "#40c057")], x, y, s)


def p09():
    S = Scene()
    foret(S, graine=124, sombre=True)
    S.add(cerf_profil(380, 760, 1.2, expr="oups"))
    S.add(branches(470, 450, 1.0))
    S.add(texte(400, 140, "Coincé !", 56, "#fff3bf", contour="#2b8a3e"))
    return S


def p10():
    S = Scene()
    foret(S, graine=124, sombre=True)
    S.add(cerf_profil(360, 760, 1.2, expr="concentre", rot=-6))
    S.add(branches(450, 450, 1.0))
    S.add(loup(700, 760, 0.7, expr="furieux", bras="course", flip=True))
    S.add(texte(250, 140, "Tire ! Tire !", 52, "#fff3bf", contour="#2b8a3e"))
    return S


def p11():
    S = Scene()
    foret(S, graine=125, sombre=True)
    S.add(cerf_profil(260, 760, 1.15, expr="joie", course=True, flip=True))
    S.add(place(chemin("M -80 0 Q 0 -30 80 0", stroke="#6d4424", sw=16), 600, 400, rot=40))
    S.add(eclat(560, 380, 1.2, "#ffd43b"))
    S.add(texte(560, 220, "CRAC !", 64, "#fff3bf", contour="#2b8a3e"))
    return S


def p12():
    S = Scene()
    foret(S, graine=126)
    S.add(cerf_profil(220, 760, 1.0, expr="timide", regard=(1, 0)))
    S.add(buisson(200, 790, 2.2), buisson(420, 800, 1.6, baies="#fa5252"))
    S.add(loup(660, 720, 0.5, expr="triste", bras="bas", flip=True))
    S.add(texte(560, 300, "Perdu de vue !", 44, VERT, contour="#fff"))
    return S


def p13():
    S = Scene()
    source(S, soir=True)
    cerf_et_reflet(S, 320, 1.0, expr="content", regard=(1, 1))
    S.add(cercle(320, EAU_Y - 50, 100, "none", stroke="#ffd43b", stroke_width=6))
    S.add(bulle(580, 90, 420, 110, "Merci, mes jambes !\nVous m'avez sauvé.", 34))
    return S


def p14():
    S = Scene()
    source(S, soir=True)
    cerf_et_reflet(S, 320, 1.0, expr="sourire", regard=(1, 1))
    S.add(coeur(180, 200, 1.0), coeur(620, 150, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cerf-seul.svg", vignette),
    ("01-la-source.svg", p01), ("02-quels-beaux-bois.svg", p02), ("03-magnifique.svg", p03),
    ("04-pattes-de-fuseau.svg", p04), ("05-si-seulement.svg", p05), ("06-un-loup.svg", p06),
    ("07-ses-jambes.svg", p07), ("08-plus-vite.svg", p08), ("09-coince.svg", p09),
    ("10-tire.svg", p10), ("11-crac.svg", p11), ("12-perdu-de-vue.svg", p12),
    ("13-merci-mes-jambes.svg", p13), ("14-tout-compte.svg", p14),
]
