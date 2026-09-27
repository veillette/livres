"""Le Chêne et le Roseau — je plie, et ne romps pas."""
from fables import *

ID = "chene-roseau"


def roitelet(x, y, s=1.0, **k):
    k.setdefault("couleur", "#c68642")
    k.setdefault("ventre", "#fff4e6")
    return oiseau(x, y, s, **k)


def etang_(S, ciel_haut="#a5d8ff", ciel_bas="#e7f5ff", orage=False):
    ciel(S, ciel_haut, ciel_bas)
    if not orage:
        S.add(nuage(620, 120, 0.6))
    collines(S, 560, "#8ce99a" if not orage else "#5c7c6a", graine=13)
    sol(S, 580, "#69db7c" if not orage else "#4f7a5b")
    S.add(ellipse(560, 720, 360, 110, "#4dabf7" if not orage else "#3b5b8a"))
    S.add(chemin("M 300 720 q 30 -10 60 0 q 30 10 60 0 M 620 760 q 30 -10 60 0 q 30 10 60 0", stroke="#a5d8ff" if not orage else "#748ffc", sw=5))


def roseaux(S, x=560, y=720, s=1.0, penche=0, expr="sourire", regard=(0, 0)):
    for dx, h in ((-70, 170), (80, 190), (-30, 150)):
        S.add(roseau(x + dx, y + 10, s * 0.7, penche=penche * 0.9, h=h, visage_=False))
    S.add(roseau(x, y, s, expr=expr, penche=penche, regard=regard))


def ciel_orage(S):
    ciel(S, "#343a40", "#868e96")
    S.add(nuage(160, 110, 1.0, "#495057"), nuage(520, 80, 1.2, "#495057"), nuage(740, 160, 0.8, "#495057"))


def couverture():
    S = Scene()
    etang_(S)
    S.add(chene(270, 640, 0.95, expr="fier"))
    roseaux(S, 560, 730, 1.1, penche=15, expr="rire")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(roseau(190, 262, 0.8, expr="content", penche=12))
    return S


def p01():
    S = Scene()
    etang_(S)
    S.add(chene(300, 650, 1.05, expr="fier"))
    S.add(oiseau(560, 250, 0.6, "#4dabf7", ailes="ouvertes"))
    return S


def p02():
    S = Scene()
    etang_(S)
    S.add(chene(-40, 650, 0.9, expr="neutre"))
    roseaux(S, 520, 740, 1.3, penche=5, expr="content")
    return S


def p03():
    S = Scene()
    etang_(S)
    S.add(chene(215, 660, 1.05, expr="malin", regard=(1, 1)))
    roseaux(S, 545, 740, 1.05, penche=30, expr="timide")
    S.add(roitelet(660, 470, 0.45, expr="content"))
    S.add(bulle(330, 110, 480, 110, "Mon pauvre ami !\nUn oiseau te fait plier !", 32, pointe=(260, 330)))
    return S


def p04():
    S = Scene()
    etang_(S)
    S.add(chene(215, 660, 1.05, expr="malin", regard=(1, 1)))
    roseaux(S, 545, 740, 1.05, penche=35, expr="sourire")
    S.add(vent(480, 520, 0.8, "#fff"))
    S.add(bulle(330, 110, 480, 110, "Le moindre petit vent\nte fait baisser la tête !", 32, pointe=(260, 330)))
    return S


def p05():
    S = Scene()
    etang_(S)
    S.add(soleil(640, 110, 50))
    S.add(chene(360, 660, 1.05, expr="fier"))
    S.add(rayons_soleil(560, 150, 480, 240))
    S.add(bulle(620, 330, 280, 100, "Moi, je suis\nle plus fort !", 32, pointe=(460, 470)))
    return S


def p06():
    S = Scene()
    etang_(S)
    S.add(chene(215, 660, 1.05, expr="triste", regard=(1, 1)))
    roseaux(S, 545, 740, 1.05, penche=10, expr="surpris")
    S.add(bulle(330, 110, 500, 110, "Si tu poussais à mon ombre,\nje te protégerais.", 30, pointe=(260, 330)))
    return S


def p07():
    S = Scene()
    etang_(S)
    S.add(chene(215, 660, 1.05, expr="surpris", regard=(1, 1)))
    roseaux(S, 545, 740, 1.05, penche=0, expr="content", regard=(-1, 0))
    S.add(bulle(560, 150, 380, 110, "Je plie,\net ne romps pas.", 38, pointe=(610, 360)))
    return S


def p08():
    S = Scene()
    etang_(S)
    S.add(chene(215, 660, 1.05, expr="rire", regard=(1, 1)))
    roseaux(S, 545, 740, 1.05, penche=-6, expr="malin", regard=(-1, 0))
    S.add(texte(250, 90, "Ha ha ha !", 50, "#2d6a4f", contour="#fff"))
    S.add(bulle(560, 190, 380, 90, "Attendons la fin…", 34, pointe=(600, 380)))
    return S


def p09():
    S = Scene()
    ciel_orage(S)
    collines(S, 560, "#5c7c6a", graine=13)
    sol(S, 580, "#4f7a5b")
    S.add(ellipse(560, 720, 360, 110, "#3b5b8a"))
    S.add(chene(215, 660, 1.05, expr="inquiet", regard=(1, -1)))
    roseaux(S, 545, 740, 1.05, penche=0, expr="inquiet", regard=(0, -1))
    S.add(chemin("M 620 40 L 580 150 L 620 150 L 570 280", stroke="#ffe066", sw=10))
    S.add(texte(700, 260, "Grondement…", 30, "#ffe066"))
    return S


def p10():
    S = Scene()
    ciel_orage(S)
    collines(S, 560, "#5c7c6a", graine=13)
    sol(S, 580, "#4f7a5b")
    S.add(ellipse(560, 720, 360, 110, "#3b5b8a"))
    S.add(vent_visage(170, 300, 1.4, "#dee2e6"))
    S.add(rafales(360, 420, 1.2, "#dee2e6"), rafales(420, 560, 1.0, "#dee2e6"))
    S.add(texte(560, 200, "FIOUUUU !", 70, "#f8f9fa"))
    pluie(S, 50, graine=4, couleur="#a5d8ff")
    return S


def p11():
    S = Scene()
    ciel_orage(S)
    pluie(S, 60, graine=6, couleur="#a5d8ff")
    S.add(ellipse(400, 760, 500, 130, "#3b5b8a"))
    roseaux(S, 240, 700, 1.3, penche=96, expr="concentre", regard=(1, 1))
    S.add(rafales(80, 250, 1.3, "#dee2e6"), rafales(120, 450, 1.0, "#dee2e6"))
    return S


def p12():
    S = Scene()
    ciel_orage(S)
    pluie(S, 60, graine=7, couleur="#a5d8ff")
    sol(S, 600, "#4f7a5b")
    S.add(chene(420, 700, 1.05, expr="furieux", penche=4))
    rr = random.Random(3)
    for _ in range(10):
        S.add(grande_feuille(rr.uniform(500, 800), rr.uniform(100, 500), 0.12, "#40c057", "#2f9e44", rot=rr.uniform(0, 360)))
    S.add(rafales(40, 250, 1.1, "#dee2e6"))
    S.add(bulle(640, 620, 280, 90, "Je ne plierai pas !", 26, pointe=(470, 560)))
    return S


def p13():
    S = Scene()
    ciel_orage(S)
    pluie(S, 60, graine=8, couleur="#a5d8ff")
    sol(S, 640, "#4f7a5b")
    S.add(chene(420, 720, 1.0, expr="oups", penche=28))
    S.add(chemin("M 380 720 L 400 680 L 420 720 L 440 690 L 460 720", stroke="#343a40", sw=5))
    S.add(texte(220, 170, "CRAAAC !", 80, "#ffe066", contour="#343a40"))
    S.add(rafales(40, 350, 1.1, "#dee2e6"))
    return S


def p14():
    S = Scene()
    ciel(S, "#868e96", "#dee2e6")
    sol(S, 600, "#4f7a5b")
    S.add(ellipse(640, 730, 260, 80, "#3b5b8a"))
    S.add(chene(520, 640, 0.9, expr="triste", tombe=True))
    S.add(g([chemin("M 520 640 q -30 30 -60 40 M 520 640 q 10 40 -10 70 M 520 640 q 40 20 60 60", stroke="#8d5524", sw=10)]))
    roseaux(S, 700, 740, 0.9, penche=5, expr="triste", regard=(-1, 0))
    return S


def p15():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(640, 110, 50))
    sol(S, 600, "#69db7c")
    S.add(ellipse(600, 730, 300, 90, "#4dabf7"))
    S.add(chene(360, 640, 0.75, expr="dort", tombe=True))
    roseaux(S, 620, 740, 1.1, penche=0, expr="content", regard=(-1, 0))
    S.add(roitelet(640, 520, 0.5, expr="rire"))
    # un gland a germé
    S.add(g([trait(200, 720, 200, 670, "#40c057", 5), ellipse(186, 668, 14, 7, "#51cf66", rot=-30), ellipse(214, 664, 14, 7, "#51cf66", rot=30),
             ellipse(200, 728, 10, 12, "#c68642")]))
    S.add(coeur(200, 620, 0.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("roseau-seul.svg", vignette),
    ("01-le-chene.svg", p01), ("02-le-roseau.svg", p02), ("03-mon-pauvre-ami.svg", p03),
    ("04-le-moindre-vent.svg", p04), ("05-le-plus-fort.svg", p05), ("06-a-mon-ombre.svg", p06),
    ("07-je-plie.svg", p07), ("08-attendons.svg", p08), ("09-l-orage.svg", p09),
    ("10-le-vent-du-nord.svg", p10), ("11-le-roseau-plie.svg", p11), ("12-le-chene-resiste.svg", p12),
    ("13-craaac.svg", p13), ("14-deracine.svg", p14), ("15-le-matin.svg", p15),
]
