"""Oups ! — Renardeau et le pot cassé (l'honnêteté)."""
from base import *
from objets import *

ID = "renard-pot"
PETIT = dict(habit="#4dabf7", motif="rayures", couleur_motif="#a5d8ff")
MAMAN = dict(acc=("echarpe",), couleur_acc="#9775fa")
MINOU = dict(couleur="#868e96")


def salon(S, sombre=False):
    interieur(S, "#e3fafc" if not sombre else "#c5d0d6", "#d8b48a", 580, papier="#c5f6fa" if not sombre else None)
    S.add(fenetre(90, 110, 170, 170, "#a5d8ff", rideaux="#ffa8a8", contenu=nuage(80, 60, 0.4) + soleil(140, 40, 18, rayons=False)))
    S.add(cadre_mur(560, 120, 130, 100))


def gueridon(x, y, s=1.0):
    return place([rect(-8, -150, 16, 150, "#a0693a"), ellipse(0, -2, 50, 10, "#a0693a"), ellipse(0, -150, 70, 14, "#c68642")], x, y, s)


def couverture():
    S = Scene()
    salon(S)
    S.add(tapis(400, 740, 260, 50, "#d0bfff", "#b197fc"))
    S.add(pot_fleurs(260, 700, 0.9, etat="repare"))
    S.add(perso("renard", 480, 750, 1.6, expr="oups", bras="bouche", regard=(-1, 0), **PETIT))
    S.add(ballon_jeu(640, 710, 34))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("renard", 170, 265, 0.95, expr="malin", bras="bas", regard=(1, 0), **PETIT))
    S.add(ballon_jeu(300, 235, 28))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(tapis(420, 730, 260, 50, "#d0bfff", "#b197fc"))
    S.add(gueridon(640, 600, 1.0))
    S.add(pot_fleurs(640, 452, 0.6))
    S.add(perso("renard", 330, 740, 1.5, expr="rire", bras="haut", regard=(1, -0.5), pieds_haut=True, **PETIT))
    S.add(ballon_jeu(500, 330, 34))
    S.add(mouvement(460, 360, 0.8, rot=-30))
    S.add(texte(560, 260, "Boing !", 50, "#1971c2", contour="#fff"))
    return S


def p02():
    S = Scene()
    salon(S)
    S.add(gueridon(560, 600, 1.0))
    S.add(pot_fleurs(560, 720, 1.0, etat="casse"))
    S.add(ballon_jeu(700, 690, 34))
    S.add(perso("renard", 240, 750, 1.5, expr="oups", bras="joues", regard=(1, 0), **PETIT))
    S.add(texte(560, 330, "CRAC !", 110, "#e03131", contour="#fff", rot=-8))
    S.add(eclat(560, 640, 1.8, "#fab005"))
    return S


def p03():
    S = Scene()
    salon(S)
    S.add(gueridon(640, 600, 1.0))
    S.add(tapis(400, 740, 280, 50, "#d0bfff", "#b197fc"))
    S.add(chemin("M 380 725 Q 430 665 480 725", "#d0bfff", stroke="#9775fa", sw=4), chemin("M 500 730 Q 545 690 590 730", "#d0bfff", stroke="#9775fa", sw=4))
    S.add(poly([(580, 712), (604, 694), (612, 718)], "#e8590c"), poly([(462, 716), (474, 700), (486, 718)], "#e8590c"))
    S.add(perso("renard", 250, 730, 1.4, expr="inquiet", bras="donne", regard=(-1, 0), **PETIT))
    S.add(texte(400, 200, "Chut…", 60, "#5f3dc4"))
    return S


def p04():
    S = Scene()
    salon(S)
    S.add(tapis(400, 750, 280, 50, "#d0bfff", "#b197fc"))
    S.add(perso("renard", 600, 760, 2.0, expr="surpris", bras="hanches", regard=(-1, 0.3), **MAMAN))
    S.add(perso("renard", 280, 760, 1.25, expr="inquiet", bras="bas", regard=(-1, 0), **PETIT))
    S.add(perso("chat", 110, 770, 0.95, expr="surpris", regard=(1, 0), **MINOU))
    S.add(bulle(520, 150, 470, 90, "Qui a cassé mon pot ?", 38, pointe=(600, 260)))
    return S


def p05():
    S = Scene()
    fond(S, "#dee2e6")
    S.add(cercle(400, 430, 320, "#ced4da"))
    S.add(nuage_orage(610, 170, 0.8))
    S.add(perso("renard", 400, 720, 1.8, expr="triste", bras="bas", regard=(0, 1), **PETIT,
                derriere=sac_cailloux(-10, -140, 1.15)))
    return S


def p06():
    S = Scene()
    salon(S)
    S.add(tapis(400, 750, 280, 50, "#d0bfff", "#b197fc"))
    S.add(perso("renard", 580, 760, 2.0, expr="sourire", bras="bas", regard=(-1, 0.3), **MAMAN))
    S.add(perso("renard", 290, 760, 1.35, expr="timide", bras="bas", regard=(1, 0), **PETIT))
    S.add(pot_fleurs(120, 760, 0.5, etat="casse"))
    S.add(bulle(300, 170, 400, 110, "C'est moi, Maman.\nPardon.", 36, pointe=(290, 400)))
    return S


def p07():
    S = Scene()
    salon(S)
    S.add(tapis(400, 750, 280, 50, "#d0bfff", "#b197fc"))
    petit = perso("renard", 0, 34, 0.62, expr="content", bras="bas", **PETIT)
    S.add(perso("renard", 400, 740, 2.2, expr="content", bras="calin", objet=petit))
    S.add(coeur(200, 280, 1.5), coeur(600, 250, 1.2, "#ff8787"), coeur(640, 420, 0.9))
    S.add(paillettes(190, 460))
    return S


def p08():
    S = Scene()
    salon(S)
    S.add(table(400, 780, 360, 160, "#c68642"))
    S.add(pot_fleurs(400, 600, 1.1, etat="repare"))
    S.add(perso("renard", 150, 770, 1.5, expr="rire", bras="bas", regard=(1, 0), **PETIT))
    S.add(perso("renard", 660, 770, 1.8, expr="content", bras="bas", regard=(-1, 0), **MAMAN))
    S.add(paillettes(400, 300), paillettes(290, 470, 0.7))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("renardeau-seul.svg", vignette),
    ("01-ballon.svg", p01), ("02-crac.svg", p02), ("03-cacher.svg", p03),
    ("04-qui.svg", p04), ("05-lourd.svg", p05), ("06-verite.svg", p06),
    ("07-calin.svg", p07), ("08-repare.svg", p08),
]
