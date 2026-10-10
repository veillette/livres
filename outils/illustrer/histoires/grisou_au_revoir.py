"""Au revoir, Grisou — dire au revoir à un animal qu'on aime.

Grisou, le vieux chat, était là avant la naissance de Nathan. Il dort au
soleil, ronronne… puis il devient très fatigué et ne mange plus. La
vétérinaire explique qu'il est très vieux et très malade. Un matin, Maman
le dit avec des mots vrais : Grisou est mort cette nuit ; son corps s'est
arrêté, il ne respire plus, il n'a plus mal, et il ne reviendra pas. Nathan
pleure ; ce n'est pas sa faute. Au jardin, on plante un rosier pour Grisou,
chacun lui dit merci. Le panier est vide, on est triste, et on a aussi le
droit de rire en se souvenant. Au printemps, le rosier fleurit : Grisou est
dans le cœur de Nathan, pour toujours.

Plans : 1 moyen (Grisou au soleil) · 2 moyen (il ne mange plus) · 3 moyen
(chez la vétérinaire) · 4 moyen (Maman explique) · 5 gros plan (ce n'est
pas ta faute) · 6 large (le rosier) · 7 moyen (merci, Grisou) · 8 moyen (le
panier vide) · 9 moyen (la boîte à souvenirs) · 10 gros plan (le dessin) ·
11 large (le printemps) · 12 moyen (dans mon cœur).
"""
from base import *
from base import _assombrir
from objets import chat_profil, papillon
from fantastique import personne, mains_personne
from metiers import blouse, stethoscope

ID = "grisou-au-revoir"

NATHAN = dict(peau="claire", cheveux="chatain", coiffure="raie", habit="#748ffc", robe=False, jambes="#495057")
MAMAN = dict(stature="adulte", peau="claire", cheveux="brun", coiffure="longs", habit="#ffa94d", robe=True, yeux="cils")
PAPA = dict(stature="adulte", peau="claire", cheveux="blond", coiffure="courts", habit="#69db7c", robe=False, jambes="#364fc7",
            barbe="#e9c46a", nez="long")
VETO = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="chignon", habit="#ffffff", robe=False, jambes="#495057",
            tenue=g([blouse(), stethoscope()]), acc=("lunettes",))
GRIS = "#868e96"


def nathan(x, y, s=1.6, **k):
    return personne(x, y, s, **{**NATHAN, **k})


def maman(x, y, s=1.95, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def papa(x, y, s=1.95, **k):
    return personne(x, y, s, **{**PAPA, **k})


def grisou(x, y, s=1.0, **k):
    return chat_profil(x, y, s, couleur=GRIS, rayures=True, collier="#1c7ed6", **k)


def panier_chat(x, y, s=1.0, coussin="#ffc9c9"):
    m = [ellipse(0, -20, 110, 26, coussin), chemin("M -116 -30 Q -110 10 0 12 Q 110 10 116 -30 Q 0 -6 -116 -30 Z", volume("#e9c46a", 0.3, 0.8))]
    for k in range(-5, 6):
        m.append(trait(k * 20, -20, k * 19, 8, "#c9a24a", 2, opacity=0.6))
    return place(m, x, y, s)


def gamelle(x, y, s=1.0, pleine=True):
    m = [chemin("M -40 -20 L 40 -20 L 32 0 L -32 0 Z", "#4dabf7")]
    if pleine:
        for k in range(6):
            m.append(cercle(-24 + k * 10, -22 - (k % 2) * 4, 5, "#c68642"))
    return place(m, x, y, s)


def rosier(x, y, s=1.0, fleurs=False):
    m = [trait(0, 0, 0, -110, "#5c940d", 8), trait(0, -60, -40, -100, "#5c940d", 6), trait(0, -80, 36, -120, "#5c940d", 6)]
    for px, py in ((-40, -100), (36, -120), (0, -120), (-20, -70), (24, -80)):
        m.append(ellipse(px, py, 22, 14, "#51cf66", rot=30))
    if fleurs:
        for px, py in ((-40, -110), (36, -132), (2, -134), (24, -86)):
            m += [cercle(px, py, 16, volume("#f783ac", 0.35, 0.8)), cercle(px, py, 6, "#e64980")]
    return place(m, x, y, s)


def souris_laine(x, y, s=1.0):
    return place([ellipse(0, 0, 22, 14, "#e599f7"), cercle(16, -8, 6, "#e599f7"), chemin("M -20 0 Q -40 6 -44 -8", stroke="#be4bdb", sw=3),
                  cercle(20, -4, 2, ENCRE)], x, y, s)


def salon(S, soleil_=True):
    interieur(S, "#fff4e6", "#c9a27a", y=600, papier="#ffe8cc")
    S.add(fenetre(470, 100, 220, 210, "#a5d8ff", rideaux="#ffd8a8"))
    if soleil_:
        S.add(poly([(470, 310), (690, 310), (760, 760), (360, 760)], "#fff3bf", opacity=0.45))
    S.add(tapis(420, 730, 300, 56, "#d0ebff", "#74c0fc"))


def jardin(S, printemps=False, horizon=480):
    ciel(S, "#a5d8ff" if printemps else "#ffd8a8", "#fff4e6")
    collines(S, horizon, "#d8f5a2" if printemps else "#c0eb75", graine=12)
    S.add(rect(0, horizon + 60, 800, 800 - horizon - 60, terrain("#8ce99a")))
    S.add(arbre(620, 640, 1.5, "#69db7c" if printemps else "#94d82d", "#51cf66", fruits=None))
    if printemps:
        for x, y in ((120, 700), (200, 760), (720, 760), (90, 600)):
            S.add(fleur(x, y, 0.9, "#ffd43b"))


def canape(x, y, w=420, couleur="#748ffc", dossier=True, assise=True):
    m = []
    if dossier:
        m += [rect(x - w / 2, y - 210, w, 120, volume(couleur, 0.3, 0.8), rx=30)]
    if assise:
        m += [rect(x - w / 2 + 10, y - 110, w - 20, 70, volume(couleur, 0.25, 0.75), rx=18),
              rect(x - w / 2 - 30, y - 150, 60, 140, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=24),
              rect(x + w / 2 - 30, y - 150, 60, 140, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=24)]
    return g(m)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S)
    lx, ly, t = 330, 800, 1.75
    S.add(nathan(lx, ly, t, expr="content", bras="porte", regard=(1, 0.3),
                 objet=place(chat_profil(0, 0, 0.85, couleur=GRIS, rayures=True, collier="#1c7ed6", pose="dort"), 0, -52)))
    S.add(rosier(560, 780, 1.2, fleurs=True))
    S.cachette(760, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(grisou(200, 240, 1.4, pose="dort"))
    S.add(zzz(270, 120, 0.7))
    return S


def p01():
    """Plan moyen : au soleil, sur le tapis, Grisou le vieux chat dort ; Nathan le caresse doucement."""
    S = Scene()
    salon(S)
    S.add(grisou(560, 720, 1.5, pose="dort"))
    S.add(nathan(300, 800, 1.6, expr="content", bras="tend", regard=(1, 0.5)))
    S.add(zzz(640, 560, 0.9))
    S.add(cadre_mur(120, 130, 130, 110, "#d0ebff"))
    return S


def p02():
    """Plan moyen : Grisou est couché dans son panier, très fatigué ; sa gamelle est pleine ; Nathan s'inquiète."""
    S = Scene()
    salon(S, soleil_=False)
    S.add(panier_chat(540, 760, 1.2))
    S.add(grisou(540, 740, 1.2, pose="couche", expr="dort"))
    S.add(gamelle(700, 790, 0.9))
    S.add(nathan(250, 800, 1.6, expr="inquiet", bras="joues", regard=(1, 0.6)))
    S.add(texte(400, 130, "Grisou ne mange plus.", 44, "#495057", contour="#fff"))
    return S


def p03():
    """Plan moyen : chez la vétérinaire, Grisou sur la table ; la vétérinaire parle doucement ; Maman tient la main de Nathan."""
    S = Scene()
    interieur(S, "#e3fafc", "#dee2e6", y=600)
    S.add(rect(80, 120, 160, 200, "#fff", stroke="#ced4da", stroke_width=4), texte(160, 220, "+", 80, "#38d9a9"))
    S.add(personne(640, 800, 1.95, expr="triste", bras="tend", flip=True, regard=(-1, 0.6), **VETO))
    S.add(rect(330, 560, 300, 24, "#ced4da", rx=6), rect(460, 584, 40, 216, "#adb5bd"))
    S.add(grisou(470, 560, 0.95, pose="couche", expr="dort"))
    S.add(maman(250, 800, 1.95, expr="triste", bras="main", regard=(1, 0.3)))
    S.add(nathan(120, 810, 1.4, expr="triste", bras="main", flip=True, regard=(1, 0)))
    S.add(bulle(560, 150, 400, 110, "Grisou est très vieux\net très malade.", 30, pointe=(610, 300)))
    S.cachette(250, 70, "air")
    return S


def p04():
    """Plan moyen : le matin, sur le canapé, Maman prend Nathan contre elle pour lui dire que Grisou est mort."""
    S = Scene()
    salon(S, soleil_=False)
    S.add(panier_chat(680, 790, 0.8))
    S.add(canape(330, 790, 460, assise=False))
    S.add(maman(270, 770, 1.8, expr="triste", bras="epaule", regard=(1, 0.4)))
    S.add(nathan(430, 780, 1.35, expr="triste", bras="bas", flip=True, regard=(-1, -0.4)))
    S.add(canape(330, 790, 460, dossier=False))
    return S


def p05():
    """Gros plan : Nathan pleure dans les bras de Papa : « C'est ma faute ? » « Non, ce n'est la faute de personne. »"""
    S = Scene()
    salon(S, soleil_=False)
    S.add(papa(470, 960, 2.3, expr="triste", bras="calin", regard=(-0.5, 0.6)))
    S.add(nathan(340, 960, 1.9, expr="pleure", bras="calin", larmes=True, regard=(1, -0.3)))
    S.camera(1.1, 400, 520)
    S.dessus(bulle(220, 130, 300, 90, "C'est ma faute ?", 34, pointe=(270, 250)))
    S.dessus(bulle(600, 130, 330, 110, "Non. Ce n'est la faute\nde personne.", 28, pointe=(560, 250)))
    return S


def p06():
    """Plan large : au jardin, sous l'arbre, Papa et Nathan plantent un petit rosier ; Maman tient la boîte de Grisou."""
    S = Scene()
    jardin(S)
    S.add(ellipse(545, 740, 80, 20, "#8d5f3a"))
    S.add(rosier(545, 740, 0.9))
    S.add(papa(730, 800, 1.9, expr="triste", bras="ramasse", flip=True, regard=(-1, 0.7),
               objet=g([trait(80, -220, 60, 10, "#c68642", 7), rect(40, 0, 50, 36, "#868e96", rx=6)])))
    S.add(nathan(400, 800, 1.55, expr="triste", bras="porte", regard=(1, 0.5), objet=place(souris_laine(0, 0, 1.2), 0, -80)))
    S.add(maman(170, 800, 1.9, expr="triste", bras="porte", regard=(1, 0.3), objet=rect(-60, -130, 120, 70, volume("#c68642", 0.3, 0.8), rx=8)))
    S.add(texte(400, 130, "Un rosier pour Grisou", 46, "#5c940d", contour="#fff"))
    S.cachette(730, 230, "air")
    return S


def p07():
    """Plan moyen : autour du rosier, chacun dit merci à Grisou : « Merci, Grisou, pour les ronrons. »"""
    S = Scene()
    jardin(S)
    S.add(ellipse(400, 740, 90, 22, "#8d5f3a"))
    S.add(rosier(400, 740, 1.1))
    S.add(souris_laine(440, 744, 0.8))
    for x in (330, 470):
        S.add(fleur(x, 760, 0.7, "#ffd43b"))
    S.add(maman(150, 800, 1.85, expr="triste", bras="mains_jointes", regard=(1, 0.4)))
    S.add(papa(650, 800, 1.85, expr="triste", bras="mains_jointes", flip=True, regard=(-1, 0.4)))
    S.add(nathan(270, 800, 1.45, expr="timide", bras="mains_jointes", regard=(1, 0.6)))
    S.add(bulle(330, 150, 420, 110, "Merci, Grisou,\npour les ronrons.", 32, pointe=(290, 330)))
    S.cachette(730, 230, "air")
    return S


def p08():
    """Plan moyen : quelques jours plus tard, Nathan est assis près du panier vide, son dessin à la main."""
    S = Scene()
    salon(S)
    S.add(panier_chat(540, 760, 1.3))
    S.add(nathan(300, 800, 1.6, expr="triste", bras="calin", regard=(1, 0.6)))
    S.add(texte(400, 130, "Le panier est vide.", 46, "#495057", contour="#fff"))
    return S


def p09():
    """Plan moyen : avec Papa, Nathan regarde les photos de Grisou ; ils rient : Grisou dans le sapin de Noël !"""
    S = Scene()
    salon(S, soleil_=False)
    S.add(canape(400, 790, 520, assise=False))
    S.add(papa(500, 770, 1.8, expr="rire", bras="porte", flip=True, regard=(-1, 0.3),
               objet=g([rect(-70, -140, 140, 100, "#fff", stroke="#dee2e6", stroke_width=4)])))
    S.add(nathan(300, 780, 1.4, expr="rire", bras="designe", regard=(1, 0)))
    S.add(canape(400, 790, 520, dossier=False))
    S.add(rect(60, 110, 300, 230, "#fff", stroke="#dee2e6", stroke_width=6))
    S.add(poly([(210, 140), (140, 310), (280, 310)], "#2f9e44"), rect(200, 310, 20, 24, "#8d5524"))
    for px, py, c in ((180, 250, "#fa5252"), (230, 220, "#ffd43b"), (250, 290, "#4dabf7")):
        S.add(cercle(px, py, 8, c))
    S.add(chat_profil(210, 250, 0.45, couleur=GRIS, rayures=True, pose="assis", expr="content"))
    S.add(texte(580, 90, "Tu te souviens ?", 42, "#e8590c", contour="#fff"))
    return S


def p10():
    """Gros plan : à la table, Nathan dessine Grisou endormi au soleil, avec un grand cœur."""
    S = Scene()
    salon(S, soleil_=False)
    S.add(nathan(400, 900, 2.0, expr="content", bras="porte", regard=(0, 1)))
    S.add(rect(140, 770, 520, 30, "#c68642", rx=6))
    S.add(rect(250, 690, 300, 82, "#fff", stroke="#dee2e6", stroke_width=3))
    S.add(chat_profil(390, 764, 0.45, couleur=GRIS, rayures=True, pose="dort"), coeur(490, 716, 0.6, "#ff8787"),
          soleil(300, 716, 14, "#ffd43b"))
    S.cachette(60, 790)
    return S


def p11():
    """Plan large : au printemps, le rosier est couvert de fleurs roses ; Nathan est assis à côté : « Bonjour, Grisou. »"""
    S = Scene()
    jardin(S, printemps=True)
    S.add(rosier(470, 740, 1.4, fleurs=True))
    S.add(papillon(570, 520, 0.8, "#ffa94d", "#ffd43b"))
    S.add(nathan(280, 800, 1.6, expr="content", bras="tend", regard=(1, 0.2)))
    S.add(bulle(300, 150, 300, 90, "Bonjour, Grisou.", 34, pointe=(290, 330)))
    return S


def p12():
    """Plan moyen : Nathan serre contre lui la photo de Grisou : « Grisou est dans mon cœur. Pour toujours. »"""
    S = Scene()
    jardin(S, printemps=True)
    S.add(coeur(400, 330, 4.0, "#ffdeeb"))
    S.add(nathan(400, 800, 1.8, expr="content", bras="porte", regard=(0, -0.2),
                 objet=g([rect(-60, -140, 120, 100, "#fff", stroke="#dee2e6", stroke_width=4),
                          place(chat_profil(0, 0, 0.35, couleur=GRIS, rayures=True, pose="assis", expr="content"), 0, -52)])))
    S.add(rosier(640, 780, 1.1, fleurs=True))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("grisou-seul.svg", vignette),
    ("01-au-soleil.svg", p01), ("02-il-ne-mange-plus.svg", p02), ("03-la-veterinaire.svg", p03),
    ("04-maman-explique.svg", p04), ("05-pas-ta-faute.svg", p05), ("06-le-rosier.svg", p06),
    ("07-merci-grisou.svg", p07), ("08-le-panier-vide.svg", p08), ("09-les-photos.svg", p09),
    ("10-le-dessin.svg", p10), ("11-le-printemps.svg", p11), ("12-dans-mon-coeur.svg", p12),
]
