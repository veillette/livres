"""Mon premier dodo chez Mamie — dormir pour la première fois loin de chez soi.

Lilou la renarde passe sa première nuit chez sa grand-mère. La journée est
joyeuse ; le soir, les bruits inconnus et l'absence des parents lui font
peur. Un petit appel, le doudou qui sent la maison et la chanson de Mamie
sous les étoiles l'aident à s'endormir. Au matin, elle est fière.
"""
from base import *
from objets import *

ID = "dodo-mamie"


def lilou(x, y, s=1.0, **k):
    return perso("renard", x, y, s, **{**dict(habit="#ffd43b", motif="rayures", couleur_motif="#fab005"), **k})


def mamie(x, y, s=1.2, **k):
    return perso("renard", x, y, s, **{**dict(couleur="#e8a87c", habit="#2f9e44", acc=("lunettes",)), **k})


def papa(x, y, s=1.3, **k):
    return perso("renard", x, y, s, **{**dict(habit="#4dabf7"), **k})


def doudou(x, y, s=0.3, **k):
    return perso("lapin", x, y, s, **{**dict(couleur="#d0ebff", habit="#74c0fc", joues=False), **k})


def sac_dos(x, y, s=1.0, couleur="#7048e8"):
    return place([rect(-60, -150, 120, 150, couleur, rx=30), rect(-44, -80, 88, 60, eclaircir(couleur, 0.3), rx=14),
                  chemin("M -30 -150 Q 0 -190 30 -150", stroke=couleur, sw=10)], x, y, s)


def brosse_dents(x, y, s=1.0, rot=0):
    return place([rect(-6, -80, 12, 80, "#4dabf7", rx=6), rect(-8, -110, 16, 30, "#fff", rx=4, stroke="#dee2e6", stroke_width=2)], x, y, s, rot=rot)


def pyjama_plie(x, y, s=1.0):
    return place([rect(-60, -40, 120, 40, "#b197fc", rx=8), g([etoile5(-30 + k * 30, -20, 7, "#fff3bf") for k in range(3)])], x, y, s)


def poele(x, y, s=1.0, crepe_en_lair=True):
    m = [ellipse(0, 0, 70, 18, "#343a40"), rect(60, -8, 120, 16, "#495057", rx=8)]
    if crepe_en_lair:
        m.append(ellipse(-10, -150, 56, 16, "#f6c453", rot=-12, stroke="#e8a200", stroke_width=3))
        m.append(mouvement(-60, -120, 0.7, rot=-90))
    return place(m, x, y, s)


def pile_crepes(x, y, s=1.0):
    m = [ellipse(0, 0, 90, 22, "#fff", stroke="#dee2e6", stroke_width=3)]
    m += [ellipse(0, -8 - k * 9, 70, 16, "#f6c453", stroke="#e8a200", stroke_width=2) for k in range(5)]
    return place(m, x, y, s)


def telephone(x, y, s=1.0):
    return place([rect(-30, -56, 60, 112, "#343a40", rx=10), rect(-24, -46, 48, 88, "#a5d8ff", rx=4)], x, y, s, rot=-15)


def dans_lit(S, x, y, w, couv, qui, oreiller="#fff"):
    S.add(lit(x, y, w, "#e5dbff", couv))
    S.add(qui)
    S.add(rect(x - w / 2 + 60, y - 125, w - 60, 85, couv, rx=18))


def chambre_mamie(S, nuit=True):
    if nuit:
        interieur(S, "#3b2a7a", "#2b1f5c", y=600, papier="#4c3a8a")
    else:
        interieur(S, "#fff9db", "#e8c39e", y=600, papier="#ffe8a3")


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 40, 4, (0, 0, 800, 500))
    S.add(lune(640, 140, 50, visage=True))
    S.add(mamie(500, 790, 1.4, expr="content", bras="calin"))
    S.add(lilou(330, 790, 1.15, expr="content", bras="calin", objet=doudou(0, -40, 0.35)))
    S.add(coeur(420, 360, 1.3, "#ff8787"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lilou(200, 264, 1.0, expr="content", bras="porte", objet=doudou(0, -64, 0.45)))
    return S


def p01():
    S = Scene()
    chambre_mamie(S, nuit=False)
    S.add(fenetre(560, 80, 170, 150, "#a5d8ff", rideaux="#ffa8a8"))
    S.add(sac_dos(520, 760, 1.2))
    S.add(pyjama_plie(680, 760, 0.9), brosse_dents(720, 700, 0.8, rot=70))
    S.add(lilou(240, 790, 1.2, expr="joie", bras="porte", objet=doudou(0, -64, 0.5)))
    S.add(texte(420, 330, "Prête !", 64, "#f76707", contour="#fff"))
    return S


def p02():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=2)
    sol(S, 640, "#8ce99a")
    S.add(maison(560, 640, 1.4, mur="#d0ebff", toit="#5f3dc4"))
    S.add(fleur(380, 650, 0.8), fleur(730, 660, 0.8, "#cc5de8"))
    S.add(mamie(580, 790, 1.1, expr="rire", bras="ouverts"))
    S.add(lilou(360, 790, 0.95, expr="content", bras="porte", objet=doudou(0, -64, 0.45)))
    S.add(papa(130, 790, 1.15, expr="sourire", bras="salut"))
    return S


def p03():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 560, papier="#ffd8a8")
    S.add(fenetre(80, 80, 200, 170, "#a5d8ff", rideaux="#69db7c",
                  contenu=g([rect(80, 200, 200, 50, "#8ce99a"), arbre(220, 250, 0.4)])))
    S.add(table(560, 760, 300, 120, "#c68642"))
    S.add(pile_crepes(560, 622, 0.9))
    S.add(mamie(330, 790, 1.15, expr="rire", bras="tient", objet=poele(70, -146, 0.6)))
    S.add(lilou(610, 790, 0.95, expr="rire", bras="haut", regard=(-1, -1)))
    S.add(texte(560, 150, "Hop !", 70, "#f76707", contour="#fff"))
    return S


def p04():
    S = Scene()
    chambre_mamie(S)
    S.add(fenetre(530, 70, 180, 170, "#141c3a", nuit_=True))
    S.add(oiseau(620, 230, 0.5, "#a9805b"))
    S.add(horloge(140, 160, 44, heure=9))
    dans_lit(S, 330, 780, 420, "#ffd43b", lilou(230, 725, 0.75, expr="surpris", regard=(1, -1)))
    S.add(texte(140, 260, "Tic-tac", 38, "#fff3bf"), texte(640, 300, "Hou-hou !", 38, "#fff3bf"), texte(620, 560, "Crac…", 38, "#fff3bf"))
    return S


def p05():
    S = Scene()
    chambre_mamie(S)
    S.add(fenetre(530, 70, 180, 170, "#141c3a", nuit_=True))
    dans_lit(S, 300, 780, 420, "#ffd43b", lilou(195, 725, 0.75, expr="pleure", larmes=True))
    S.add(rect(0, 0, 800, 800, "#ffe066", opacity=0.08))
    S.add(mamie(640, 790, 1.15, expr="inquiet", bras="ouverts", flip=True))
    S.add(bulle(300, 180, 420, 120, "Je veux Papa\net Maman…", 40, pointe=(220, 540)))
    return S


def p06():
    S = Scene()
    chambre_mamie(S)
    S.add(lampe(680, 620, 0.9))
    dans_lit(S, 320, 780, 420, "#ffd43b", lilou(210, 725, 0.75, expr="sourire", bras="joues"))
    S.add(doudou(330, 660, 0.3, expr="dort"))
    S.add(mamie(560, 790, 1.1, expr="sourire", bras="tient", flip=True, objet=telephone(68, -146, 0.8)))
    S.add(pensee(300, 230, 140, g([papa(260, 300, 0.5, expr="rire", bras="salut"), perso("renard", 340, 300, 0.5, habit="#f783ac", expr="rire", bras="salut")]),
                 depuis=(240, 540)))
    S.add(texte(300, 70, "Bonne nuit, ma Lilou !", 36, "#fff3bf"))
    return S


def p07():
    S = Scene()
    nuit(S, "#141c3a", "#3b2a7a")
    etoiles(S, 60, 7, (0, 0, 800, 460))
    S.add(lune(130, 120, 40, croissant=True, fond_ciel="#1c2a52"))
    S.add(rect(0, 460, 800, 340, "#5f3dc4"), rect(0, 440, 800, 30, "#7950f2"))
    S.add(mamie(470, 790, 1.15, expr="chante", bras="montre", regard=(-1, -1)))
    S.add(lilou(300, 790, 0.95, expr="content", bras="porte", regard=(0, -1), objet=doudou(0, -64, 0.45)))
    S.add(notes(560, 360, 1.0, "#fff3bf"))
    # la petite casserole (Grande Ourse) que Mamie montre du doigt
    pts = [(470, 130), (530, 120), (585, 140), (630, 170), (640, 230), (720, 235), (715, 175)]
    S.add(chemin("M " + " L ".join(f"{x} {y}" for x, y in pts) + " L 630 170", stroke="#fff3bf", sw=2, opacity=0.5))
    S.add(g([etoile5(x, y, 9, "#fff3bf") for x, y in pts]))
    return S


def p08():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(680, 110, 50))
    collines(S, 600, "#b2f2bb", graine=3)
    sol(S, 640, "#8ce99a")
    S.add(maison(170, 640, 1.2, mur="#d0ebff", toit="#5f3dc4"))
    S.add(mamie(540, 790, 1.15, expr="rire", bras="calin"))
    S.add(lilou(420, 790, 1.0, expr="fier", bras="calin"))
    S.add(papa(720, 790, 1.1, expr="rire", bras="salut", flip=True))
    S.add(bulle(420, 230, 440, 90, "Je reviens bientôt !", 40, pointe=(420, 560)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lilou-seule.svg", vignette),
    ("01-le-sac.svg", p01), ("02-chez-mamie.svg", p02), ("03-les-crepes.svg", p03), ("04-les-bruits.svg", p04),
    ("05-je-veux-papa.svg", p05), ("06-le-coup-de-fil.svg", p06), ("07-les-etoiles.svg", p07), ("08-fiere.svg", p08),
]
