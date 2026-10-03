"""Le Cochet, le Chat et le Souriceau — ne pas juger les gens sur la mine."""
from fables import *

ID = "cochet-chat-souriceau"

ROSE_F = "#d6336c"


def souriceau(x, y, s=1.0, **k):
    k.setdefault("acc", ("echarpe",))
    k.setdefault("couleur_acc", "#d6336c")
    return perso("souris", x, y, s, **k)


def maman(x, y, s=1.0, **k):
    k.setdefault("acc", ("tablier",))
    return perso("souris", x, y, s, **k)


def chat(x, y, s=1.0, **k):
    k.setdefault("couleur", "#adb5bd")
    return perso("chat", x, y, s, **k)


def mur_trou(S, souriceau_=None):
    """Le bas d'un mur de grange, percé du trou de la souris."""
    S.add(rect(0, 0, 800, 800, "#e9d8c4"))
    for row in range(10):
        for k in range(6):
            S.add(rect(-60 + k * 160 + (row % 2) * 80, row * 66, 150, 58, "#dcc6ad", rx=10))
    S.add(rect(0, 640, 800, 160, "#c9a27e"))
    S.add(chemin("M 260 640 L 260 520 Q 260 430 360 430 Q 460 430 460 520 L 460 640 Z", "#3b2412"))
    if souriceau_:
        S.add(souriceau_)
    S.add(rect(0, 630, 800, 16, "#a0693a"))


def chez_souris(S):
    """L'intérieur douillet du terrier."""
    fond(S, "#a0693a")
    S.add(ellipse(400, 420, 470, 380, "#d9a066"))
    S.add(ellipse(400, 440, 420, 330, "#f3d9b1"))
    S.add(rect(0, 640, 800, 160, "#c49a6c"))
    S.add(tapis(400, 700, 260, 50))
    S.add(lit(640, 640, 220, couverture="#ffc9d6"))
    S.add(bougie(180, 560, 1.0))
    S.add(table(180, 640, 140, 80, nappe="#ffc9d6"))


def cour(S, graine=91):
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 580, "#d8f5a2")
    S.add(barriere(400, 640, 1.0, largeur=800))


def souvenir(contenu):
    """Grande bulle de souvenir, au-dessus de la souris qui raconte."""
    return pensee(420, 300, 270, contenu, fill="#fff9db", depuis=(220, 560))


def couverture():
    S = Scene()
    cour(S)
    S.add(coq(210, 760, 1.6, expr="fier", ailes="haut", bec_ouvert=True))
    S.add(chat(640, 760, 1.3, expr="malin", bras="calin", regard=(-1, 0)))
    S.add(souriceau(410, 760, 0.85, expr="surpris", bras="joues", regard=(-1, -1)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(souriceau(200, 262, 0.85, expr="content"))
    return S


def p01():
    S = Scene()
    mur_trou(S, souriceau(360, 650, 0.9, expr="surpris", bras="bas"))
    S.add(texte(600, 300, "Oh !", 70, ROSE_F, contour="#fff"))
    return S


def p02():
    S = Scene()
    cour(S)
    S.add(souriceau(400, 760, 0.7, expr="bouche_bee", bras="joues", regard=(0, -1)))
    S.add(texte(400, 280, "Comme le monde est grand !", 44, ROSE_F, contour="#fff"))
    return S


def p03():
    S = Scene()
    chez_souris(S)
    S.add(maman(260, 740, 1.35, expr="surpris", bras="ouverts", regard=(1, 0)))
    S.add(souriceau(530, 740, 1.1, expr="oups", bras="haut", regard=(-1, 0)))
    S.add(texte(400, 170, "Maman ! Maman !", 54, ROSE_F, contour="#fff"))
    return S


def p04():
    S = Scene()
    chez_souris(S)
    S.add(souriceau(200, 760, 1.0, expr="oups", bras="haut", regard=(1, -1)))
    S.add(souvenir(coq(440, 470, 1.65, expr="fache", ailes="haut")))
    return S


def p05():
    S = Scene()
    cour(S)
    S.add(coq(470, 760, 2.0, expr="furieux", ailes="haut", bec_ouvert=True))
    S.add(souriceau(150, 770, 0.7, expr="oups", bras="course", regard=(-1, 0)))
    S.add(texte(470, 200, "COCORICO !", 72, "#c92a2a", contour="#fff"))
    S.add(mouvement(230, 680, 1.0, rot=180))
    return S


def p06():
    S = Scene()
    chez_souris(S)
    S.add(souriceau(200, 760, 1.0, expr="content", bras="joues", regard=(1, -1)))
    S.add(souvenir(chat(420, 480, 1.3, expr="dort", bras="calin")))
    return S


def p07():
    S = Scene()
    cour(S, graine=92)
    S.add(chat(520, 760, 1.6, expr="sourire", bras="calin", regard=(-1, 1)))
    S.add(souriceau(200, 770, 0.75, expr="content", bras="salut", regard=(1, -1)))
    S.add(coeur(330, 520, 0.7))
    return S


def p08():
    S = Scene()
    chez_souris(S)
    S.add(maman(300, 740, 1.4, expr="oups", bras="joues", regard=(1, 0)))
    S.add(souriceau(540, 740, 1.0, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(400, 140, 560, 120, "Mon petit, ce doucet,\nc'est un chat !", 40, pointe=(320, 360)))
    return S


def p09():
    S = Scene()
    chez_souris(S)
    S.add(maman(200, 760, 1.2, expr="inquiet", bras="montre", regard=(1, -1)))
    S.add(pensee(480, 300, 250, g([chat(480, 500, 1.25, expr="miam", bras="haut", regard=(1, 1)),
                                   texte(480, 170, "Miam, une souris…", 30, ROSE_F)]), fill="#fff9db", depuis=(260, 520)))
    return S


def p10():
    S = Scene()
    chez_souris(S)
    S.add(maman(200, 760, 1.2, expr="sourire", bras="montre", regard=(1, -1)))
    S.add(pensee(480, 300, 250, g([coq(480, 480, 1.5, expr="content", ailes="bas"),
                                   grain(380, 470, 1.2), grain(590, 476, 1.2)]), fill="#fff9db", depuis=(260, 520)))
    return S


def p11():
    S = Scene()
    cour(S, graine=93)
    S.add(chat(560, 760, 1.5, expr="malin", bras="ouverts", regard=(-1, 1)))
    S.add(souriceau(200, 770, 0.75, expr="malin", bras="salut", regard=(1, -1)))
    S.add(bulle(560, 140, 360, 100, "Viens, petit…", 38, pointe=(560, 380)))
    S.add(bulle(220, 360, 360, 110, "Non merci,\nmonsieur le chat !", 32, pointe=(200, 560)))
    return S


def p12():
    S = Scene()
    cour(S, graine=94)
    S.add(coq(520, 760, 1.6, expr="content", ailes="bas", regard=(-1, 1)))
    S.add(grain(390, 760, 1.2))
    S.add(souriceau(240, 770, 0.8, expr="rire", bras="salut", regard=(1, -1)))
    S.add(bulle(280, 280, 380, 110, "Bonjour,\nmonsieur le coq !", 34, pointe=(240, 520)))
    return S


def p13():
    S = Scene()
    chez_souris(S)
    S.add(maman(330, 740, 1.35, expr="content", bras="calin", regard=(1, 0)))
    S.add(souriceau(480, 740, 0.95, expr="content", bras="calin", regard=(-1, 0)))
    S.add(coeur(410, 300, 1.2))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("souriceau-seul.svg", vignette),
    ("01-le-trou.svg", p01), ("02-le-monde.svg", p02), ("03-maman.svg", p03),
    ("04-un-animal-terrible.svg", p04), ("05-cocorico.svg", p05), ("06-si-doux.svg", p06),
    ("07-il-m-a-souri.svg", p07), ("08-c-est-un-chat.svg", p08), ("09-miam-une-souris.svg", p09),
    ("10-le-coq.svg", p10), ("11-non-merci.svg", p11), ("12-bonjour-monsieur-le-coq.svg", p12),
    ("13-a-la-maison.svg", p13),
]
