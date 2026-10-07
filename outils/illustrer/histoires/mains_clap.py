"""Mes mains font clap ! — une comptine pour découvrir son corps.

Cinq enfants différents (couleurs de peau, coiffures, lunettes) font chacun
une action avec une partie du corps : mains, pieds, nez, yeux, oreilles,
bouche, ventre, bras, tout le corps… jusqu'au dodo.
"""
from base import *
from objets import *
from fantastique import personne
from contes import pain

ID = "mains-clap"
ENFANTS = {
    "ines": dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#f783ac"),
    "malo": dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#1c7ed6"),
    "lin": dict(peau="doree", cheveux="noir", coiffure="queue", habit="#ffd43b", robe=False, jambes="#2f9e44", acc=("lunettes",)),
    "sami": dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#69db7c", robe=False, jambes="#495057"),
    "jade": dict(peau="rosee", cheveux="blond", coiffure="chignon", habit="#cc5de8"),
}


def enfant_(qui, x, y, s=1.0, **k):
    return personne(x, y, s, **{**ENFANTS[qui], **k})


def fond_couleur(S, haut, bas, graine=1, motif="#ffffff"):
    ciel(S, haut, bas)
    rnd = random.Random(graine)
    for _ in range(14):
        S.add(cercle(rnd.uniform(0, 800), rnd.uniform(0, 600), rnd.uniform(14, 40), motif, opacity=0.25))
    S.add(rect(0, 640, 800, 160, eclaircir(bas, 0.0)), ellipse(400, 642, 460, 26, "#fff", opacity=0.35))


def gros_mot(x, y, mot, couleur, taille=86, rot=-6):
    return texte(x, y, mot, taille, couleur, contour="#fff", rot=rot)


def flute(x, y, s=1.0, rot=-20):
    return place([rect(-90, -9, 180, 18, "#c68642", rx=9), g([cercle(-50 + k * 26, 0, 4, "#5c3a1e") for k in range(5)])], x, y, s, rot=rot)


def crepe_assiette(x, y, s=1.0):
    return place([ellipse(0, 0, 80, 20, "#fff", stroke="#dee2e6", stroke_width=3), ellipse(0, -6, 60, 14, "#f6c453", stroke="#e8a200", stroke_width=2)], x, y, s)


def coussin(x, y, couleur):
    return ellipse(x, y, 110, 34, couleur)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fond_couleur(S, "#ffe3e3", "#fff3bf", 1)
    S.add(enfant_("malo", 130, 790, 0.95, expr="rire", bras="haut"))
    S.add(enfant_("lin", 290, 790, 1.0, expr="rire", bras="porte"), eclat(290, 714, 0.9, "#fab005"))
    S.add(enfant_("ines", 450, 790, 1.05, expr="rire", bras="ouverts"))
    S.add(enfant_("sami", 610, 790, 1.0, expr="rire", bras="tete"))
    S.add(enfant_("jade", 730, 800, 0.85, expr="rire", bras="salut", flip=True))
    S.add(gros_mot(420, 330, "Clap !", "#e64980", 100))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(enfant_("ines", 200, 264, 0.95, expr="rire", bras="porte"), eclat(200, 192, 0.8, "#fab005"))
    return S


def p01():
    S = Scene()
    fond_couleur(S, "#ffdeeb", "#fff0f6", 1, "#f783ac")
    S.add(enfant_("ines", 400, 790, 1.6, expr="rire", bras="applaudit"), eclat(400, 632, 1.4, "#fab005"))
    S.add(gros_mot(200, 220, "Clap !", "#e64980"), gros_mot(600, 300, "Clap !", "#e64980", rot=8))
    return S


def p02():
    S = Scene()
    fond_couleur(S, "#d0ebff", "#e7f5ff", 2, "#74c0fc")
    S.add(enfant_("malo", 400, 760, 1.55, expr="joie", bras="large"))
    S.add(mouvement(330, 760, 1.0, rot=90), mouvement(480, 760, 1.0, rot=90))
    S.add(gros_mot(170, 600, "Tap !", "#1c7ed6", 76), gros_mot(640, 620, "Tap !", "#1c7ed6", 76, rot=8))
    return S


def p03():
    S = Scene()
    fond_couleur(S, "#d3f9d8", "#ebfbee", 3, "#8ce99a")
    S.add(enfant_("sami", 380, 790, 1.55, expr="souffle", bras="bouche", rot=-6))
    S.add(eclat(430, 580, 1.2, "#74c0fc"), g([goutte(470 + k * 30, 560 - k * 20, 0.7, "#a5d8ff") for k in range(3)]))
    S.add(gros_mot(560, 260, "Atchoum !", "#2f9e44", 84, rot=10))
    return S


def p04():
    S = Scene()
    fond_couleur(S, "#fff3bf", "#fff9db", 4, "#ffe066")
    S.add(enfant_("lin", 240, 790, 1.3, expr="surpris"), enfant_("jade", 560, 790, 1.3, expr="content"))
    S.add(gros_mot(240, 330, "Clic…", "#f08c00", 70), gros_mot(560, 330, "… clac !", "#f08c00", 70, rot=6))
    return S


def p05():
    S = Scene()
    fond_couleur(S, "#e5dbff", "#f3f0ff", 5, "#b197fc")
    S.add(enfant_("jade", 250, 790, 1.35, expr="content", bras="joues", regard=(1, 0)))
    S.add(enfant_("malo", 580, 790, 1.2, expr="chante", bras="tient", flip=True, objet=flute(60, -150, 0.7, rot=30)))
    S.add(notes(390, 380, 1.3, "#7048e8"), texte(250, 300, "Chut…", 60, "#7048e8", contour="#fff"))
    return S


def p06():
    S = Scene()
    fond_couleur(S, "#ffe8cc", "#fff4e6", 6, "#ffc078")
    S.add(table(400, 790, 420, 130, "#c68642"))
    S.add(enfant_("sami", 400, 640, 1.2, expr="miam", bras="large"))
    S.add(rect(170, 640, 460, 30, "#c68642", rx=6), crepe_assiette(400, 650, 1.1))
    S.add(gros_mot(640, 260, "Miam !", "#e8590c", 80, rot=8))
    S.add(place(g([ellipse(0, 0, 12, 7, "#495057"), ellipse(-6, -6, 9, 6, "#e7f5ff", opacity=0.8), ellipse(6, -6, 9, 6, "#e7f5ff", opacity=0.8)]), 140, 230, 1.6))
    S.add(texte(140, 300, "Pas toi !", 34, "#868e96", contour="#fff"))
    return S


def p07():
    S = Scene()
    fond_couleur(S, "#c5f6fa", "#e3fafc", 7, "#66d9e8")
    S.add(enfant_("ines", 330, 790, 1.5, expr="oups", bras="calin"))
    S.add(gros_mot(600, 520, "Glouglou !", "#0c8599", 64, rot=-8))
    S.add(pomme(620, 250, 1.4), pain(690, 330, 1.0))
    return S


def p08():
    S = Scene()
    fond_couleur(S, "#ffe3e3", "#fff5f5", 8, "#ffa8a8")
    S.add(enfant_("lin", 330, 790, 1.35, expr="content", bras="calin"))
    S.add(enfant_("sami", 470, 790, 1.35, expr="content", bras="calin", flip=True))
    S.add(coeur(400, 300, 2.2, "#ff6b6b"), coeur(250, 360, 1.0, "#ffa8a8"), coeur(560, 380, 1.2, "#ffa8a8"))
    return S


def p09():
    S = Scene()
    fond_couleur(S, "#fff3bf", "#d3f9d8", 9, "#ffd43b")
    S.add(enfant_("malo", 120, 790, 1.0, expr="rire", bras="danse", rot=-10))
    S.add(enfant_("ines", 280, 760, 1.05, expr="rire", bras="ouverts", rot=8))
    S.add(enfant_("lin", 430, 790, 1.0, expr="rire", bras="tete"))
    S.add(enfant_("sami", 580, 740, 1.05, expr="rire", bras="victoire", rot=-8))
    S.add(enfant_("jade", 720, 790, 0.95, expr="rire", bras="salut", rot=10))
    S.add(notes(180, 280, 1.2, "#e64980"), notes(560, 240, 1.2, "#7048e8"))
    S.add(gros_mot(400, 160, "On danse !", "#f08c00", 76))
    return S


def p10():
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 40, 10, (0, 0, 800, 420))
    S.add(lune(660, 120, 44, visage=True))
    S.add(rect(0, 660, 800, 140, "#7048e8"))
    for x, qui, c in ((120, "malo", "#4dabf7"), (280, "ines", "#f783ac"), (440, "lin", "#ffd43b"), (600, "sami", "#69db7c"), (730, "jade", "#cc5de8")):
        S.add(coussin(x, 740, c))
        S.add(enfant_(qui, x, 740, 0.75, expr="dort", bras="calin"))
    S.add(zzz(360, 420, 1.2, "#e5dbff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("enfant-seule.svg", vignette),
    ("01-les-mains.svg", p01), ("02-les-pieds.svg", p02), ("03-le-nez.svg", p03), ("04-les-yeux.svg", p04),
    ("05-les-oreilles.svg", p05), ("06-la-bouche.svg", p06), ("07-le-ventre.svg", p07), ("08-les-bras.svg", p08),
    ("09-tout-le-corps.svg", p09), ("10-dodo.svg", p10),
]
