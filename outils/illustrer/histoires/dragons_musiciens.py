"""Les dragons musiciens — Les musiciens de Brême, avec quatre dragons.

Tison, un vieux dragon rouge qui ne crache plus que des ronds de fumée, part
pour Brême devenir musicien. En chemin il emmène Brume (une dragonne bleue
qui ne souffle que du brouillard), Plume (un dragon vert aux ailes trop
petites pour voler) et Étincelle (un tout petit dragon jaune qui a le
hoquet : à chaque « hic ! », des étincelles). La nuit, ils trouvent la
maison des brigands qui ont volé le trésor du roi ; montés les uns sur les
autres, ils chantent : fumée, brouillard et étincelles font fuir les
brigands. Ils rapportent le trésor au roi et deviennent les musiciens du
château.

Plans : couverture moyen · 1 moyen (Tison et son rond de fumée) · 2 moyen
(Brume dans le brouillard) · 3 large (Plume sur son rocher) · 4 gros plan
(hic !) · 5 large (la forêt au soir) · 6 contre-plongée (une lumière !) ·
7 moyen (les brigands et le trésor) · 8 large (la pyramide) · 9 gros plan
(le concert) · 10 large (la fuite) · 11 moyen (dodo) · 12 gros plan (dans le
noir) · 13 moyen (le brigand raconte) · 14 large (concert au château).
"""
from base import *
from base import _assombrir
from fantastique import personne, roi, chateau, jardin_chateau, etincelles, OR
from contes import voleur, foret, baluchon
from fables import festin
from fetes import lanterne
from dragons import *

ID = "dragons-musiciens"
PAPIER_PEINT = "losanges"

TISON = dict(couleur="#e03131", ventre="#ffc9c9", barbe="#f1f3f5")
BRUME = dict(couleur="#4dabf7", ventre="#d0ebff", echarpe="#e7f5ff")
PLUME = dict(couleur="#40c057", ventre="#d8f5a2", ailes="bas")
ETINCELLE = dict(couleur="#fcc419", ventre="#fff9db")
BRIGAND = dict(stature="adulte", carrure="ronde", nez="rond")
BRIGAND2 = dict(stature="adulte", carrure="fine", nez="long", cheveux="roux", habit="#862e9c")
BRIGAND3 = dict(stature="adulte", carrure="normale", nez="pointu", cheveux="blond", habit="#1864ab")


def tison(x, y, s=1.5, **k):
    return dragon_habille(x, y, s, **{**TISON, **k})


def brume(x, y, s=1.25, **k):
    return dragon_habille(x, y, s, **{**BRUME, **k})


def plume(x, y, s=1.1, **k):
    return dragon_habille(x, y, s, **{**PLUME, **k})


def etincelle(x, y, s=0.75, **k):
    return dragon_habille(x, y, s, **{**ETINCELLE, **k})


def tambour(x, y, s=1.0):
    m = [ellipse(0, 0, 40, 12, "#7048e8"), rect(-40, 0, 80, 50, volume("#7048e8", 0.25, 0.75)),
         ellipse(0, 50, 40, 12, "#5f3dc4"), ellipse(0, 0, 36, 9, "#fff4e6"),
         chemin("M -40 10 L -20 46 L 0 10 L 20 46 L 40 10", stroke="#ffd43b", sw=3)]
    return place(m, x, y, s)


def pyramide(x, y, s=1.0, expr="chante"):
    """Tison, Brume, Plume et Étincelle les uns sur les autres ; (x, y) = pieds de Tison."""
    m = [tison(0, 0, 1.2, expr=expr, bras="haut"),
         brume(0, -232, 0.9, expr=expr, bras="haut"),
         plume(0, -420, 0.75, expr=expr, bras="haut"),
         etincelle(0, -578, 0.55, expr=expr, bras="haut")]
    return place(m, x, y, s)


# --- Décors -------------------------------------------------------------------

def route(S, graine=3, soir=False):
    if soir:
        ciel(S, "#7048e8", "#ffa8a8")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(soleil(690, 100, 40))
        S.add(nuage(160, 110, 0.6))
    lointain(S, 540, "#b2f2bb", graine=graine)
    collines(S, 590, "#b2f2bb", graine=graine)
    sol(S, 590, "#94d82d", couleur2="#82c91e", y2=700)
    S.add(chemin("M 0 760 Q 400 680 800 720 L 800 800 L 0 800 Z", terrain("#f3d9a4")))


def repaire(S, lumiere=True):
    """La maison des brigands, la nuit, au fond des bois."""
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 25, graine=9)
    S.add(lune(660, 110, 40, croissant=True))
    for x in (40, 760):
        S.add(sapin(x, 620, 1.3, "#2b8a3e", "#237032"))
    sol(S, 600, "#2b8a3e")
    S.add(maison(400, 660, 1.5, mur="#a0693a", toit="#5c3a1e", porte="#343a40", lumiere=lumiere))


def salle(S, nuit_=True):
    """La salle des brigands : planches, poutres, une fenêtre sur la nuit."""
    piece(S, "chaumiere", 600)
    S.add(fenetre(90, 110, 170, 160, nuit_=nuit_, dehors="#1c2a52"))
    S.ambiance("nuit" if nuit_ else "interieur")


def chateau_fete(S, soir=False):
    if soir:
        jardin_chateau(S, "#5f3dc4", "#ffa8a8", chateau_s=0.75, chateau_x=400, y=600)
    else:
        jardin_chateau(S, "#a5d8ff", "#fff0f6", chateau_s=0.75, chateau_x=400, y=600)


# --- Pages --------------------------------------------------------------------

def couverture():
    S = Scene()
    route(S)
    S.add(tison(150, 790, 1.35, expr="chante", bras="ouverts"))
    S.add(brume(340, 790, 1.1, expr="rire", bras="haut"))
    S.add(brouillard(330, 480, 0.6, graine=3))
    S.add(plume(510, 790, 0.95, expr="rire", bras="porte", objet=tambour(0, -70, 0.6)))
    S.add(etincelle(660, 790, 0.7, expr="chante", bras="haut"))
    S.add(etincelles(660, 560, 1.0, "#ffd43b", graine=4))
    S.add(rond_fumee(140, 420, 1.0), rond_fumee(190, 360, 0.7))
    S.add(notes(260, 470, 1.0, "#e64980"), notes(560, 450, 0.9, "#1c7ed6"))
    S.cachette(740, 420, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tison(80, 262, 0.75, expr="rire"), brume(175, 262, 0.62, expr="rire"),
          plume(258, 262, 0.55, expr="rire"), etincelle(330, 262, 0.45, expr="rire"))
    return S


def p01():
    """Plan moyen : Tison devant le château, un rond de fumée en guise de feu."""
    S = Scene()
    chateau_fete(S)
    S.add(tison(300, 790, 1.6, expr="triste", bras="hanches", objet=None))
    S.add(rond_fumee(470, 570, 1.0), rond_fumee(530, 505, 0.8), rond_fumee(570, 450, 0.6))
    S.add(texte(560, 640, "Pff…", 48, "#868e96", contour="#fff"))
    S.add(baluchon(600, 770, 0.9))
    S.dessus(bulle(420, 110, 520, 100, "Je vais partir à Brême\net devenir musicien !", 32, pointe=(330, 400)))
    return S


def p02():
    """Plan moyen : Brume, triste, dans son brouillard."""
    S = Scene()
    route(S, graine=5)
    S.add(tison(200, 790, 1.35, expr="sourire", bras="donne", regard=(1, 0)))
    S.add(brume(560, 790, 1.25, expr="triste", larmes=True, regard=(-1, 0)))
    S.add(brouillard(560, 770, 0.9, graine=5), brouillard(740, 600, 0.6, graine=6))
    S.dessus(bulle(400, 110, 520, 100, "Viens avec moi ! Tu siffleras\ncomme le vent !", 30, pointe=(230, 420)))
    return S


def p03():
    """Plan large : Plume sur son rocher, qui ne sait pas voler."""
    S = Scene()
    route(S, graine=7)
    S.add(caillou(620, 730, 3.0, "#adb5bd"))
    S.add(plume(620, 660, 1.0, expr="triste", bras="bas", regard=(-1, 0)))
    S.add(tison(150, 790, 1.15, expr="sourire", regard=(1, 0)))
    S.add(brume(330, 790, 0.95, expr="content", bras="salut", regard=(1, 0)))
    S.add(tambour(470, 720, 0.9))
    S.dessus(bulle(420, 110, 520, 100, "Viens avec nous ! Tu taperas\nsur le tambour !", 30, pointe=(330, 520)))
    return S


def p04():
    """Gros plan : Étincelle et son hoquet d'étincelles."""
    S = Scene()
    route(S, graine=9)
    S.add(tison(130, 790, 1.15, expr="sourire", regard=(1, 0)))
    S.add(brume(290, 790, 0.95, expr="surpris", regard=(1, 0)))
    S.add(plume(420, 790, 0.85, expr="rire", regard=(1, 0)))
    S.add(etincelle(590, 790, 0.95, expr="pleure", larmes=True, bras="bouche"))
    S.add(etincelles(590, 560, 1.4, "#ffd43b", graine=2), etincelles(640, 520, 0.9, "#ff922b", graine=7))
    S.camera(1.45, 500, 600)
    S.dessus(texte(600, 140, "Hic !", 90, "#f08c00", contour="#fff", rot=-6))
    return S


def p05():
    """Plan large : la forêt au coucher du soleil."""
    S = Scene()
    foret(S, "#7048e8", "#ffa8a8", graine=21)
    S.add(tison(220, 790, 1.15, expr="inquiet", regard=(1, 0)))
    S.add(brume(390, 790, 0.95, expr="inquiet"))
    S.add(plume(520, 790, 0.82, expr="inquiet"))
    S.add(etincelle(630, 790, 0.6, expr="inquiet"))
    S.dessus(texte(400, 160, "La nuit tombe…", 56, "#fff", contour="#5f3dc4"))
    return S


def p06():
    """Contre-plongée : Étincelle, sur la tête de Tison, voit une lumière."""
    S = Scene()
    nuit(S, "#1c2a52", "#5f3dc4")
    etoiles(S, 30, graine=4)
    for x, s in [(70, 1.6), (760, 1.5)]:
        S.add(sapin(x, 800, s, "#2b8a3e", "#237032"))
    sol(S, 740, "#2b8a3e")
    # la maison au loin, fenêtre allumée
    S.add(maison(640, 560, 0.35, mur="#a0693a", toit="#5c3a1e", porte="#343a40", lumiere=True))
    S.add(tison(300, 820, 2.2, expr="surpris", regard=(1, -1)))
    S.add(etincelle(300, 820 - 230 * 2.2, 0.8, expr="joie", bras="montre", regard=(1, 0)))
    S.dessus(bulle(560, 130, 380, 100, "Une lumière !\nUne maison !", 36, pointe=(360, 260)))
    return S


def p07():
    """Plan moyen : par la fenêtre, les brigands, le festin et le trésor."""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.ambiance("nuit")
    tetes = g([place(dragon_habille(0, 0, 0.62, expr="surpris", **TISON), 120, 390),
               place(dragon_habille(0, 0, 0.5, expr="miam", **ETINCELLE), 225, 390)])
    S.add(fenetre(50, 130, 230, 220, dehors="#1c2a52", contenu=tetes))
    S.add(trait(480, 0, 480, 72, "#495057", 4), trait(700, 0, 700, 72, "#495057", 4))
    S.add(lanterne(480, 70, 1.0), lanterne(700, 70, 0.9))
    S.lumiere(480, 122, 160, "#ffd43b", 0.7)
    S.lumiere(700, 117, 140, "#ffd43b", 0.7)
    S.add(coffre(680, 790, 1.15))
    S.add(festin(420, 800, 1.05))
    S.add(voleur(190, 800, 1.35, expr="rire", bras="haut", **BRIGAND))
    S.add(voleur(580, 800, 1.35, expr="miam", bras="bouche", **BRIGAND2))
    S.lumiere(420, 600, 300, "#ffd43b", 0.45)
    return S


def p08():
    """Plan large : la pyramide de dragons devant la maison."""
    S = Scene()
    repaire(S)
    S.add(pyramide(650, 790, 0.95, expr="malin"))
    return S


def p09():
    """Gros plan : le concert ! Fumée, brouillard et étincelles."""
    S = Scene()
    repaire(S)
    S.add(pyramide(560, 790, 0.95))
    S.add(brouillard(330, 520, 1.0, graine=8, couleur="#d0ebff"))
    S.add(rond_fumee(380, 640, 1.2), rond_fumee(320, 700, 0.9))
    S.add(etincelles(480, 200, 1.6, "#ffd43b", graine=3), etincelles(640, 170, 1.2, "#ff922b", graine=5))
    S.add(notes(350, 380, 1.2, "#ffe066"), notes(700, 380, 1.0, "#ffe066"))
    S.camera(1.15, 520, 440)
    S.dessus(texte(230, 150, "Rrrooar ! Pfiouuu !", 48, "#ffe066", contour="#5f3dc4"),
             texte(230, 230, "Boum ! Hic !", 48, "#ffe066", contour="#5f3dc4"))
    return S


def p10():
    """Plan large : les brigands s'enfuient dans la nuit."""
    S = Scene()
    foret(S, "#1c2a52", "#5f3dc4", graine=23, sombre=True)
    S.ambiance("nuit")
    S.add(voleur(240, 790, 1.2, expr="oups", bras="haut", flip=True, **BRIGAND))
    S.add(voleur(520, 790, 1.2, expr="furieux", bras="course", flip=True, **BRIGAND2))
    S.add(mouvement(650, 620, 1.4, rot=180), mouvement(380, 620, 1.4, rot=180))
    S.dessus(texte(400, 160, "Au secours ! Un monstre !", 48, "#fff", contour="#c92a2a"))
    return S


def p11():
    """Plan moyen : les quatre amis dorment ; Tison garde le coffre."""
    S = Scene()
    salle(S)
    S.add(coffre(650, 700, 0.8))
    S.add(tapis(400, 760, 330, 50, "#ffc9c9", "#ff8787"))
    S.add(dragon_couche(560, 770, 0.95, **{k: v for k, v in TISON.items() if k != "barbe"}))
    S.add(dragon_couche(250, 740, 0.8, flip=True, **{k: v for k, v in BRUME.items() if k != "echarpe"}))
    S.add(dragon_couche(390, 800, 0.6, **PLUME_COUCHE))
    S.add(dragon_couche(250, 640, 0.4, **ETINCELLE))
    S.add(zzz(420, 560, 1.2))
    S.cachette(560, 470, "air")
    S.camera(1.1, 420, 620)
    return S


PLUME_COUCHE = dict(couleur=PLUME["couleur"], ventre=PLUME["ventre"])


def p12():
    """Gros plan : dans le noir, le brigand est accueilli par les dragons."""
    S = Scene()
    salle(S)
    S.add(voleur(400, 790, 1.3, expr="oups", bras="haut", **BRIGAND3))
    S.add(brouillard(560, 600, 0.8, graine=12))
    S.add(etincelle(200, 790, 0.7, expr="furieux", bras="poing"))
    S.add(etincelles(200, 580, 1.0, "#ffd43b", graine=9))
    S.add(plume(600, 800, 0.9, expr="furieux", bras="poing", regard=(-1, 0)))
    S.add(tison(720, 820, 1.2, expr="furieux", regard=(-1, 0)))
    S.cachette(660, 440, "air")
    obscurite(S, [trou_doux(400, 560, 400)], opacity=0.55)
    S.camera(1.15, 430, 520)
    S.dessus(texte(400, 160, "Hic ! Pfiouuu ! Rrrooar !", 46, "#ffe066", contour="#c92a2a"))
    return S


def p13():
    """Plan moyen : le brigand raconte ce qu'il a vu."""
    S = Scene()
    foret(S, "#1c2a52", "#5f3dc4", graine=25, sombre=True)
    S.ambiance("nuit")
    S.add(voleur(200, 790, 1.15, expr="inquiet", **BRIGAND))
    S.add(voleur(400, 790, 1.25, expr="oups", bras="haut", **BRIGAND3))
    S.add(voleur(610, 790, 1.15, expr="bouche_bee", bras="joues", **BRIGAND2))
    S.dessus(bulle(420, 130, 580, 110, "Il y a une sorcière, un géant\net un monstre là-dedans !", 30, pointe=(400, 440)))
    return S


def p14():
    """Plan large : le trésor rendu, le concert au château."""
    S = Scene()
    chateau_fete(S, soir=True)
    S.add(coffre(130, 780, 0.7))
    S.add(roi(250, 790, 1.15, expr="rire", bras="danse", stature="adulte", carrure="ronde"))
    S.add(tison(420, 790, 1.05, expr="chante", bras="ouverts"))
    S.add(brume(560, 790, 0.9, expr="chante", bras="haut"))
    S.add(plume(670, 790, 0.78, expr="rire", bras="porte", objet=tambour(0, -70, 0.55)))
    S.add(etincelle(740, 700, 0.5, expr="rire", bras="haut"))
    S.add(etincelles(600, 280, 1.6, "#ffd43b", graine=13), etincelles(300, 260, 1.2, "#ff922b", graine=14))
    S.add(notes(220, 420, 1.0, "#e64980"), notes(520, 400, 1.0, "#1c7ed6"))
    S.cachette(60, 300, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("musiciens-seuls.svg", vignette),
    ("01-tison.svg", p01), ("02-brume.svg", p02), ("03-plume.svg", p03), ("04-etincelle.svg", p04),
    ("05-la-nuit.svg", p05), ("06-une-lumiere.svg", p06), ("07-les-brigands.svg", p07), ("08-la-pyramide.svg", p08),
    ("09-le-concert.svg", p09), ("10-un-monstre.svg", p10), ("11-dodo.svg", p11), ("12-dans-le-noir.svg", p12),
    ("13-le-brigand-raconte.svg", p13), ("14-au-chateau.svg", p14),
]
