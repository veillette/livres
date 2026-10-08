"""Les musiciens de Brême — ensemble, on est plus forts."""
from contes import *

ID = "musiciens-breme"


def ane(x, y, s=1.2, **k):
    return perso("ane", x, y, s, **k)


def chien(x, y, s=1.0, **k):
    return perso("chien", x, y, s, tache=True, **k)


def chat(x, y, s=0.85, **k):
    return perso("chat", x, y, s, couleur="#495057", visage="#dee2e6", **k)


def coq_(x, y, s=0.9, **k):
    return coq(x, y, s, **k)


def pyramide(x, y, s=1.0, expr="chante", bec=True):
    """Âne, chien, chat et coq les uns sur les autres ; (x, y) = pieds de l'âne."""
    m = [ane(0, 0, 1.2, expr=expr, bras="haut"),
         chien(0, -250, 0.9, expr=expr, bras="haut"),
         chat(0, -430, 0.75, expr=expr, bras="haut"),
         coq_(0, -580, 0.7, expr=expr, bec_ouvert=bec, ailes="haut")]
    return place(m, x, y, s)


def route(S, soir=False, graine=3):
    if soir:
        ciel(S, "#5f3dc4", "#ffa8a8")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(soleil(690, 100, 40))
    S.add(nuage(160, 110, 0.6))
    collines(S, 580, "#b2f2bb", graine=graine)
    sol(S, 580, "#94d82d")
    S.add(chemin("M 0 760 Q 400 680 800 720 L 800 800 L 0 800 Z", "#f3d9a4"))


def tambour(x, y, s=1.0):
    m = [ellipse(0, 0, 40, 12, "#fa5252"), rect(-40, 0, 80, 50, "#fa5252"), ellipse(0, 50, 40, 12, "#c92a2a"), ellipse(0, 0, 36, 9, "#fff4e6"),
         chemin("M -40 10 L -20 46 L 0 10 L 20 46 L 40 10", stroke="#ffd43b", sw=3)]
    return place(m, x, y, s)


def repaire(S, fenetre_lumiere=True):
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 25, graine=9)
    for x in (40, 760):
        S.add(sapin(x, 620, 1.3, "#2b8a3e", "#237032"))
    sol(S, 600, "#2b8a3e")
    S.add(maison(400, 660, 1.5, mur="#a0693a", toit="#5c3a1e", porte="#343a40", lumiere=fenetre_lumiere))


def salle(S):
    interieur(S, "#e9d8c4", "#8d5524", 600, plinthe="#5c3a1e")
    S.add(fenetre(80, 100, 170, 160, nuit_=True, dehors="#1c2a52"))


def couverture():
    S = Scene()
    route(S)
    S.add(ane(160, 790, 1.35, expr="chante", bras="ouverts"), chien(360, 790, 1.05, expr="rire", bras="porte", objet=tambour(0, -70, 0.6)))
    S.add(chat(530, 790, 0.95, expr="chante", bras="ouverts"), coq_(680, 790, 1.0, expr="chante", bec_ouvert=True, ailes="haut"))
    S.add(notes(250, 440, 1.0, "#e64980"), notes(560, 420, 0.9, "#1c7ed6"))
    S.cachette(730, 410, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ane(80, 262, 0.75, expr="rire"), chien(170, 262, 0.6, expr="rire"), chat(250, 262, 0.55, expr="rire"), coq_(330, 262, 0.55, expr="rire"))
    return S


def p01():
    S = Scene()
    route(S)
    S.add(moulin(640, 620, 0.8))
    S.add(sac(560, 780, 0.8, ecrit="farine"))
    S.add(ane(300, 790, 1.4, expr="fier", bras="montre"))
    S.add(bulle(360, 140, 480, 100, "Je vais partir à Brême\net devenir musicien !", 32, pointe=(310, 440)))
    return S


def p02():
    S = Scene()
    route(S, graine=5)
    S.add(ane(220, 790, 1.3, expr="sourire", bras="donne"))
    S.add(chien(520, 790, 1.1, expr="triste", larmes=True, flip=True))
    S.add(tambour(640, 740, 0.9))
    S.add(bulle(400, 140, 460, 100, "Viens avec moi ! Tu joueras\ndu tambour !", 30, pointe=(250, 460)))
    return S


def p03():
    S = Scene()
    route(S, graine=7)
    S.add(barriere(600, 700, 0.7, largeur=360))
    S.add(ane(160, 790, 1.15, expr="sourire"), chien(330, 790, 0.95, expr="content", bras="salut"))
    S.add(chat(600, 690, 0.8, expr="triste", flip=True))
    S.add(bulle(420, 140, 460, 100, "Viens avec nous ! Tu chantes\nsi bien la nuit !", 30, pointe=(340, 520)))
    return S


def p04():
    S = Scene()
    route(S, graine=9)
    S.add(barriere(640, 700, 0.7, largeur=300))
    S.add(coq_(640, 640, 1.0, expr="pleure", bec_ouvert=True))
    S.add(ane(140, 790, 1.1, expr="sourire"), chien(290, 790, 0.9, expr="content"), chat(420, 790, 0.8, expr="content", bras="salut"))
    S.add(bulle(400, 140, 480, 100, "Viens avec nous !\nTu as une si belle voix !", 30, pointe=(420, 560)))
    return S


def p05():
    S = Scene()
    foret(S, "#5f3dc4", "#ffa8a8", graine=21)
    S.add(ane(250, 790, 1.1, expr="inquiet"), chien(400, 790, 0.9, expr="inquiet"), chat(520, 790, 0.75, expr="inquiet"))
    S.add(coq_(630, 780, 0.75, expr="inquiet"))
    S.add(texte(400, 170, "La nuit tombe…", 56, "#fff", contour="#5f3dc4"))
    return S


def p06():
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 25, graine=4)
    S.add(gros_arbre_sombre(260, 800, 1.2))
    S.add(coq_(250, 390, 0.7, expr="surpris", ailes="haut"))
    S.add(cercle(660, 520, 36, "#ffe066", opacity=0.4), rect(640, 500, 40, 40, "#ffe066"))
    S.add(texte(620, 420, "Une lumière !", 40, "#ffe066"))
    sol(S, 700, "#2b8a3e")
    return S


def p07():
    S = Scene()
    salle(S)
    S.add(festin(430, 790, 1.0))
    S.add(voleur(200, 790, 1.2, expr="rire", bras="haut"), voleur(660, 790, 1.2, expr="miam", bras="bouche", cheveux="roux", habit="#862e9c"))
    S.add(fenetre(80, 100, 170, 160, dehors="#1c2a52", contenu=g([place(ane(0, 0, 0.6, expr="miam"), 130, 300), place(chat(0, 0, 0.5, expr="miam"), 200, 290)])))
    return S


def p08():
    S = Scene()
    repaire(S)
    S.add(pyramide(650, 790, 0.75, expr="malin", bec=False))
    return S


def p09():
    S = Scene()
    repaire(S)
    S.add(pyramide(650, 790, 0.75))
    S.add(texte(200, 180, "Hi-han ! Ouaf !", 48, "#ffe066", contour="#5f3dc4"), texte(220, 260, "Miaou ! Cocorico !", 48, "#ffe066", contour="#5f3dc4"))
    S.add(notes(180, 380, 1.0, "#ffe066"))
    return S


def p10():
    S = Scene()
    foret(S, "#1c2a52", "#5f3dc4", graine=23)
    S.add(voleur(240, 790, 1.3, expr="oups", bras="haut"), voleur(520, 790, 1.3, expr="furieux", bras="course", cheveux="roux", habit="#862e9c"))
    S.add(mouvement(420, 620, 1.4), mouvement(700, 620, 1.4))
    S.add(texte(400, 170, "Au secours ! Un monstre !", 48, "#fff", contour="#c92a2a"))
    return S


def p11():
    S = Scene()
    salle(S)
    S.add(festin(430, 700, 0.8))
    S.add(ane(150, 790, 1.1, expr="dort"), chien(330, 800, 0.8, expr="dort"), chat(560, 800, 0.7, expr="dort"))
    S.add(coq_(700, 800, 0.7, expr="dort"))
    S.add(zzz(420, 260, 1.4))
    return S


def p12():
    S = Scene()
    salle(S)
    S.add(voleur(400, 790, 1.3, expr="oups", bras="haut"))
    S.add(chat(250, 700, 0.8, expr="furieux", bras="poing"), chien(560, 790, 0.9, expr="furieux"), coq_(620, 480, 0.8, expr="furieux", bec_ouvert=True, ailes="haut"))
    S.add(texte(400, 290, "Pfff ! Ouaf ! Cocorico !", 48, "#c92a2a", contour="#fff"))
    obscurite(S, [trou_doux(400, 560, 380)], opacity=0.5)
    return S


def p13():
    S = Scene()
    foret(S, "#1c2a52", "#5f3dc4", graine=25)
    S.add(voleur(220, 790, 1.2, expr="oups", bras="course"), voleur(420, 790, 1.2, expr="oups", bras="course", cheveux="roux", habit="#862e9c"),
          voleur(620, 790, 1.2, expr="pleure", bras="course", cheveux="blond", habit="#1864ab"))
    S.add(bulle(420, 160, 560, 110, "Il y a un monstre, une sorcière\net un géant là-dedans !", 30, pointe=(260, 480)))
    return S


def p14():
    S = Scene()
    salle(S)
    S.add(tapis(400, 740, 330, 50))
    S.add(ane(170, 790, 1.2, expr="chante", bras="ouverts"), chien(340, 790, 0.9, expr="rire", objet=tambour(0, -70, 0.6), bras="porte"))
    S.add(chat(500, 790, 0.8, expr="chante", bras="ouverts"), coq_(650, 790, 0.85, expr="chante", bec_ouvert=True, ailes="haut"))
    S.add(notes(260, 380, 1.0, "#e64980"), notes(520, 360, 1.0, "#1c7ed6"))
    S.cachette(310, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("musiciens-seuls.svg", vignette),
    ("01-l-ane.svg", p01), ("02-le-chien.svg", p02), ("03-le-chat.svg", p03), ("04-le-coq.svg", p04),
    ("05-la-nuit.svg", p05), ("06-une-lumiere.svg", p06), ("07-les-brigands.svg", p07), ("08-la-pyramide.svg", p08),
    ("09-le-concert.svg", p09), ("10-un-monstre.svg", p10), ("11-dodo.svg", p11), ("12-dans-le-noir.svg", p12),
    ("13-les-brigands-s-enfuient.svg", p13), ("14-concert.svg", p14),
]
