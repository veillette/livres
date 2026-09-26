"""Pétille, la petite fée — on apprend en s'entraînant."""
from base import *
from objets import *
from fantastique import *

ID = "fee-petille"
PETILLE = dict(coiffure="chignon", cheveux="#f783ac", habit="#12b886", ailes="#e6fcf5", peau="claire")
AZUR = dict(coiffure="longs", cheveux="blanc", habit="#4dabf7", ailes="#d0ebff", peau="rosee", acc=("lunettes",))
AMIES = [dict(coiffure="tresses", cheveux="blond", habit="#ffa94d", ailes="#fff4e6", peau="doree"),
         dict(coiffure="boucles", cheveux="brun", habit="#cc5de8", ailes="#f3d9fa", peau="foncee"),
         dict(coiffure="queue", cheveux="roux", habit="#ff8787", ailes="#fff0f6", peau="claire")]


def petille(x, y, s=1.0, bras="tient", baguette_=True, **k):
    obj = baguette(68, -146, 0.9, rot=15) if baguette_ and bras in ("tient", "montre", "salut") else None
    return personne(x, y, s, bras=bras, objet=obj, **{**PETILLE, **k})


def jardin(S, soir=False):
    if soir:
        nuit(S, "#1c2a52", "#5f3dc4")
        etoiles(S, 30, graine=7)
    else:
        ciel(S, "#c3fae8", "#fff9db")
    sol(S, 640, "#8ce99a" if not soir else "#2b8a3e")
    for x, c, s in [(70, "#ff8787", 3.2), (740, "#ffd43b", 3.6)]:
        S.add(fleur(x, 700, s, c if not soir else assombrir(c, 0.6), tige=80))
    S.add(herbe(200, 660, 1.4, "#51cf66" if not soir else "#2f9e44"), herbe(600, 660, 1.2, "#51cf66" if not soir else "#2f9e44"))


def rose_fleur(x, y, s=1.0, ouverte=True, couleur="#f06595"):
    m = [trait(0, 0, 0, -120, "#40c057", 8), ellipse(18, -60, 22, 9, "#51cf66", rot=-30)]
    if ouverte:
        for k in range(6):
            a = math.radians(k * 60)
            m.append(ellipse(math.cos(a) * 28, -150 + math.sin(a) * 24, 30, 22, couleur, rot=k * 60))
        m.append(cercle(0, -150, 24, assombrir(couleur, 0.85)))
        m.append(chemin("M -12 -150 Q 0 -168 12 -150 Q 0 -140 -12 -150", stroke=assombrir(couleur, 0.7), sw=3))
    else:
        m.append(chemin("M -20 -120 Q -26 -170 0 -186 Q 26 -170 20 -120 Z", couleur))
        m.append(chemin("M -22 -120 Q -10 -140 0 -120 Q 10 -140 22 -120 Z", "#40c057"))
    return place(m, x, y, s)


def citrouille(x, y, s=1.0, rot=0):
    m = [ellipse(-30, -50, 40, 48, "#fd7e14"), ellipse(30, -50, 40, 48, "#fd7e14"),
         ellipse(0, -50, 38, 52, "#ff922b"), rect(-6, -114, 12, 20, "#5c940d", rx=4),
         chemin("M 6 -108 Q 30 -120 34 -100", stroke="#74b816", sw=4)]
    return place(m, x, y, s, rot=rot)


def plume(x, y, s=1.0, rot=0, couleur="#74c0fc"):
    m = [chemin("M 0 60 Q -34 0 0 -70 Q 34 0 0 60 Z", couleur), trait(0, 76, 0, -60, assombrir(couleur, 0.75), 3)]
    return place(m, x, y, s, rot=rot)


def fumee(x, y, s=1.0):
    m = [cercle(-40, 0, 44, "#868e96"), cercle(20, -30, 54, "#adb5bd"), cercle(60, 10, 40, "#868e96"),
         cercle(0, 30, 40, "#ced4da"), cercle(-70, 36, 26, "#adb5bd")]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    jardin(S)
    S.add(rose_fleur(620, 770, 2.4))
    S.add(petille(330, 700, 1.7, expr="rire", bras="tient"))
    S.add(etincelles(470, 330, 1.3, graine=4), etincelles(200, 420, 0.9, graine=6, couleur="#f783ac"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(petille(200, 262, 0.95, expr="content", bras="tient"))
    S.add(etincelles(270, 90, 0.6, graine=3))
    return S


def p01():
    S = Scene()
    jardin(S)
    S.add(fleur(400, 800, 5.0, "#ffa8a8", tige=90))
    S.add(petille(400, 440, 1.2, expr="rire", bras="tient"))
    S.add(papillon(640, 280, 1.0), coccinelle(170, 560, 1.4))
    return S


def p02():
    S = Scene()
    jardin(S)
    S.add(rect(240, 90, 320, 100, "#fff", rx=16, stroke="#b2f2bb", stroke_width=6))
    S.add(texte(400, 158, "École des fées", 40, "#0ca678"))
    S.add(personne(230, 760, 1.4, expr="sourire", bras="montre", objet=baguette(86, -130, 0.9, rot=30), **AZUR))
    S.add(rose_fleur(480, 770, 1.7))
    S.add(etincelles(480, 520, 1.0, graine=12))
    S.add(petille(670, 770, 1.1, expr="bouche_bee", bras="bas", regard=(-1, 0)))
    return S


def p03():
    S = Scene()
    jardin(S)
    S.add(petille(260, 760, 1.4, expr="oups", bras="montre"))
    S.add(chaussette(540, 560, 3.0, "#f06595", rot=-10))
    S.add(texte(540, 250, "Pling !", 80, "#12b886", contour="#fff"))
    S.add(etincelles(540, 470, 1.0, graine=2))
    return S


def p04():
    S = Scene()
    jardin(S)
    S.add(personne(160, 770, 1.1, expr="rire", bras="bouche", **AMIES[0]))
    S.add(personne(640, 770, 1.1, expr="rire", bras="joues", **AMIES[1]))
    S.add(petille(400, 770, 1.45, expr="timide", bras="bas", baguette_=False))
    S.add(bulle(400, 150, 460, 100, "Je ne serai jamais\nune vraie fée !", 38, pointe=(400, 380)))
    return S


def p05():
    S = Scene()
    jardin(S)
    S.add(personne(290, 770, 1.5, expr="content", bras="calin", **AZUR))
    S.add(petille(500, 770, 1.1, expr="triste", bras="bas", regard=(-1, -1)))
    S.add(coeur(420, 360, 1.5))
    S.add(bulle(400, 140, 480, 110, "La magie, ça s'apprend…\nen s'entraînant !", 36))
    return S


def p06():
    S = Scene()
    jardin(S)
    S.add(plume(200, 700, 1.1, rot=70))
    S.add(petille(330, 770, 1.3, expr="surpris", bras="montre", regard=(1, -1)))
    S.add(citrouille(580, 330, 1.6, rot=15))
    S.add(mouvement(470, 420, 1.2, rot=-40), etincelles(580, 420, 1.0, graine=8))
    return S


def p07():
    S = Scene()
    jardin(S)
    S.add(champignon(520, 770, 3.3, "#9775fa"))
    S.add(petille(200, 770, 1.3, expr="bouche_bee", bras="montre", regard=(1, -1)))
    S.add(etincelles(520, 340, 1.2, graine=5))
    return S


def p08():
    S = Scene()
    jardin(S)
    S.add(fumee(460, 330, 1.8))
    S.add(personne(400, 770, 1.4, expr="oups", bras="bouche", **{**PETILLE, "habit": "#868e96"}))
    S.add(texte(560, 110, "Pouf !", 80, "#495057", contour="#fff"))
    return S


def p09():
    S = Scene()
    jardin(S)
    for k, (x, ok) in enumerate([(180, 0), (340, 1), (500, 2)]):
        if ok == 0:
            S.add(chaussette(x, 700, 1.4, "#f06595", rot=-10))
        elif ok == 1:
            S.add(rose_fleur(x, 760, 1.0, ouverte=False))
        else:
            S.add(rose_fleur(x, 760, 1.1))
    S.add(petille(630, 770, 1.25, expr="concentre", bras="montre", flip=True))
    S.add(etincelles(500, 540, 0.8, graine=3))
    S.add(texte(400, 140, "Encore… et encore !", 50, "#0ca678", contour="#fff"))
    return S


def p10():
    S = Scene()
    jardin(S, soir=True)
    S.add(luciole(470, 450, 2.2, allumee=False, expr="pleure", flip=True))
    S.add(petille(230, 770, 1.3, expr="inquiet", bras="bas", regard=(1, -1)))
    S.add(bulle(560, 170, 420, 100, "Je ne vois plus rien !", 36, pointe=(500, 390)))
    return S


def p11():
    S = Scene()
    jardin(S, soir=True)
    S.add(cercle(500, 440, 190, "#fff3bf", opacity=0.15))
    S.add(luciole(500, 450, 2.2, allumee=True, expr="rire", flip=True))
    S.add(petille(230, 770, 1.3, expr="souffle", bras="montre"))
    S.add(etincelles(420, 440, 1.2, graine=14))
    S.add(texte(560, 150, "Pling !", 80, "#ffd43b", contour="#5f3dc4"))
    return S


def p12():
    S = Scene()
    jardin(S, soir=True)
    S.add(luciole(640, 220, 1.2), luciole(140, 260, 1.0, flip=True), luciole(420, 140, 0.9))
    S.add(personne(150, 770, 1.0, expr="rire", bras="haut", **AMIES[0]))
    S.add(personne(650, 770, 1.0, expr="rire", bras="haut", **AMIES[1]))
    S.add(personne(530, 780, 0.9, expr="rire", bras="haut", **AMIES[2]))
    S.add(petille(360, 760, 1.4, expr="fier", bras="tient"))
    S.add(etincelles(430, 360, 1.3, graine=21))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("petille-seule.svg", vignette),
    ("01-petite-fee.svg", p01), ("02-ecole.svg", p02), ("03-chaussette.svg", p03),
    ("04-rire.svg", p04), ("05-s-entrainer.svg", p05), ("06-citrouille.svg", p06),
    ("07-champignon.svg", p07), ("08-pouf.svg", p08), ("09-encore.svg", p09),
    ("10-luciole.svg", p10), ("11-lumiere.svg", p11), ("12-bravo.svg", p12),
]
