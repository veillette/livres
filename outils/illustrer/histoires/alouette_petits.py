"""L'Alouette et ses Petits, avec le Maître d'un champ — d'après La Fontaine.

Une alouette a fait son nid dans un champ de blé. Le blé mûrit ; avant de
partir chercher à manger, elle dit à ses petits d'écouter le maître du
champ. « Va dire à nos amis de venir moissonner demain. » La mère ne
s'inquiète pas : s'il compte sur ses amis, rien ne presse. Le lendemain,
personne ne vient : « Demande à nos parents. » Toujours personne. « Demain,
nous moissonnerons nous-mêmes ! » « Cette fois, partons ! » dit l'alouette.
« Ne t'attends qu'à toi seul : c'est un commun proverbe. »

Plans : 1 large (le nid dans le blé vert) · 2 moyen (le blé est mûr) · 3
large (le maître du champ) · 4 gros plan (rien ne presse) · 5 large (le
lendemain) · 6 large (nous-mêmes !) · 7 moyen (partons !) · 8 large (la
moisson).
"""
from base import *
from base import _assombrir
from fantastique import personne

ID = "alouette-petits"

# L'alouette, son épi et le champ : repris du livre « alouette » (comptine),
# pour que ce soit la même alouette.
BRUN = "#b9875a"
BRUN_FONCE = "#8a5a3b"
CREME = "#f6e7cf"
PATTES = "#d9a07a"

MAITRE = dict(stature="adulte", peau="rosee", cheveux="gris", coiffure="chauve_cote", habit="#4dabf7", robe=False, jambes="#795548",
              barbe="#adb5bd", carrure="ronde", nez="rond")
FILS = dict(stature="ado", peau="rosee", cheveux="chatain", coiffure="courts", habit="#ffd43b", robe=False, jambes="#495057")


def alouette(x, y, s=1.0, expr="sourire", ailes="bas", flip=False, rot=0, regard=(1, 0), epi_bec=False):
    """L'alouette des champs, de trois quarts, tournée vers la droite
    (flip=True : vers la gauche) ; (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    # pattes
    for dx in (-12, 12):
        m.append(trait(dx, -34, dx + 2, -4, PATTES, 4))
        m.append(chemin(f"M {dx - 8} 0 L {dx + 2} -5 L {dx + 13} 0 M {dx + 2} -5 L {dx - 3} 2", stroke=PATTES, sw=3.5))
    # queue : trois plumes en éventail
    for k, (a, L) in enumerate(((-26, 62), (-14, 68), (-2, 60))):
        m.append(ellipse(-60 - L / 2 * math.cos(math.radians(a)), -76 + L / 2 * math.sin(math.radians(a)), L / 2, 11,
                         volume(BRUN_FONCE if k != 1 else _assombrir(BRUN, 0.88), 0.3, 0.8), rot=-a))
    m.append(chemin("M -112 -90 L -118 -84 M -108 -70 L -114 -66", stroke=CREME, sw=3, opacity=0.8))
    # ailes levées (derrière le corps)
    if ailes == "haut":
        for dx, rot_, k in ((-30, -24, 0.9), (6, -4, 1.0)):
            aile = chemin("M 0 0 Q -30 -70 -6 -128 Q 14 -96 26 -70 Q 34 -40 22 0 Z", volume(_assombrir(BRUN, 0.9 if k == 1 else 0.8), 0.3, 0.8))
            plumes = chemin("M -4 -120 L 4 -96 M 8 -110 L 12 -88 M 18 -94 L 18 -74", stroke=CREME, sw=3, opacity=0.8)
            m.append(place([aile, plumes], dx, -96, k, rot=rot_))
    # corps
    m.append(ellipse(0, -72, 60, 44, volume(BRUN, 0.3, 0.8)))
    m.append(ellipse(12, -58, 44, 28, volume(CREME, 0.35, 0.9)))
    tirets = " ".join(f"M {px} {py} l 3 6" for px, py in ((26, -88), (36, -82), (18, -80), (30, -74), (42, -72), (22, -68), (10, -84), (-2, -96), (-14, -104), (8, -100)))
    m.append(chemin(tirets, stroke=BRUN_FONCE, sw=3, opacity=0.75))
    m.append(ombrage(ellipse(0, -72, 60, 44, "#000"), sombre=[(-10, -36, 60, 18)], clair=[(-10, -104, 24, 10, -10)]))
    # aile repliée
    if ailes != "haut":
        m.append(ellipse(-12, -80, 46, 26, volume(_assombrir(BRUN, 0.88), 0.3, 0.8), rot=-12))
        m.append(chemin("M -46 -70 Q -16 -64 22 -86 M -50 -80 Q -20 -76 14 -96 M -38 -92 Q -14 -92 6 -104",
                        stroke=CREME, sw=3, opacity=0.75))
    # tête, huppe, bec
    m.append(ellipse(30, -106, 22, 24, BRUN))
    # huppe : quelques plumes relevées vers l'arrière du crâne
    m.append(chemin("M 24 -146 Q 16 -170 0 -178 Q 12 -168 10 -160 Q 22 -168 30 -174 Q 26 -162 38 -154 Z", BRUN_FONCE))
    m.append(cercle(50, -126, 34, volume(BRUN, 0.3, 0.82)))
    m.append(chemin("M 50 -150 l 3 6 M 40 -144 l 3 6 M 30 -134 l 3 6", stroke=BRUN_FONCE, sw=3, opacity=0.7))
    m.append(ellipse(58, -112, 16, 10, "#e3c49e"))
    m.append(ellipse(46, -110, 9, 6, ROSE, opacity=0.6))
    if bs in ("ouverte", "o", "crie", "langue"):
        m.append(poly([(78, -130), (108, -127), (80, -120)], volume(PATTES, 0.4, 0.75)))
        m.append(poly([(80, -117), (102, -110), (78, -111)], _assombrir(PATTES, 0.85)))
        m.append(poly([(80, -120), (100, -118), (80, -117)], ROUGE_BOUCHE))
    else:
        m.append(poly([(78, -130), (106, -121), (78, -113)], volume(PATTES, 0.4, 0.75)))
        m.append(trait(80, -121, 102, -121, _assombrir(PATTES, 0.7), 1.5))
    # sourcil clair (comme les vraies alouettes) et œil
    m.append(chemin("M 52 -142 Q 64 -148 76 -140", stroke=CREME, sw=4))
    m.append(oeil(64, -130, ys, regard, taille=0.95))
    if ss:
        m.append(place(sourcils(0, 0, ss), 64 - 18, -128, 0.8))
    if epi_bec:
        m.append(epi(96, -122, 200, -150))
    contenu = avec_contour(m, s, 0.4)
    contenu += occuper(-125, -186, 112, 0)
    return place(contenu, x, y, s, flip=flip, rot=rot)


def epi(x0, y0, x1, y1, ep=1.0):
    """Épi de blé tenu en (x0, y0), sa pointe en (x1, y1)."""
    L = math.hypot(x1 - x0, y1 - y0)
    a = math.degrees(math.atan2(y1 - y0, x1 - x0))
    m = [trait(0, 0, L - 6, 0, "#e0a93a", 4 * ep)]
    nb = 6
    for k in range(nb):
        t = L * 0.6 + k * (L * 0.36) / nb
        m.append(ellipse(t, -7 * ep, 9 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75), rot=-30))
        m.append(ellipse(t, 7 * ep, 9 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75), rot=30))
        m.append(trait(t + 6 * ep, -9 * ep, t + 22 * ep, -16 * ep, "#e0a93a", 1.5))
    m.append(ellipse(L - 2 * ep, 0, 10 * ep, 5 * ep, volume("#f6c453", 0.4, 0.75)))
    return place(m, x0, y0, 1, rot=a)


def champ(S, horizon=520, haut="#74c0fc", bas="#fff3bf", graine=1, soleil_=None, ble_devant=True):
    """Champ de blé sous le ciel, avec des coquelicots."""
    ciel(S, haut, bas)
    if soleil_:
        S.add(soleil(*soleil_))
    collines(S, horizon, "#c0eb75", graine=graine, hauteur=80)
    sol(S, horizon + 40, "#e9c46a", bosse=10, premier=False)
    r = random.Random(graine)
    for k in range(int(70 * (800 - horizon) / 300)):
        yy = r.uniform(horizon + 50, 790)
        prof = (yy - horizon) / (800 - horizon)
        S.add(epi_droit(r.uniform(0, 800), yy, 0.35 + prof * 0.75, r.uniform(-12, 12)))
        if r.random() < 0.12:
            S.add(coquelicot(r.uniform(0, 800), yy + 4, 0.4 + prof * 0.6))


def epi_droit(x, y, s=1.0, rot=0):
    """Tige de blé debout ; (x, y) = pied."""
    m = [trait(0, 0, 0, -110, "#d4a017", 4)]
    for k in range(5):
        yy = -112 + k * 9
        m.append(ellipse(-6, yy, 4.5, 8, "#f6c453", rot=-30) + ellipse(6, yy, 4.5, 8, "#f6c453", rot=30))
    m.append(ellipse(0, -122, 4, 8, "#f6c453"))
    m.append(chemin("M 0 -40 Q 16 -54 22 -72", stroke="#c0a03a", sw=3))
    return place(m, x, y, s, rot=rot)


def coquelicot(x, y, s=1.0):
    return place([trait(0, 0, 0, -80, "#5c940d", 3), cercle(-8, -86, 11, "#f03e3e"), cercle(8, -86, 11, "#e03131"),
                  cercle(0, -94, 11, "#fa5252"), cercle(0, -86, 4, ENCRE)], x, y, s)


def ble_devant(S, graine=5, y0=700):
    """Quelques épis au tout premier plan, dans les coins (repoussoir)."""
    r = random.Random(graine)
    for k in range(8):
        x = r.uniform(-30, 90) if k % 2 else r.uniform(710, 830)
        S.add(epi_droit(x, r.uniform(y0, 830), r.uniform(1.4, 1.9), r.uniform(-10, 10)))


# ---------------------------------------------------------------------------


def maitre(x, y, s=1.7, **k):
    return personne(x, y, s, **{**MAITRE, **k})


def fils(x, y, s=1.55, **k):
    return personne(x, y, s, **{**FILS, **k})


def petit(x, y, s=0.4, **k):
    """Un alouetteau, tout petit et tout rond."""
    return alouette(x, y, s, **k)


def nid(x, y, s=1.0, petits=3, graine=1, expr="sourire"):
    m = [ellipse(0, 0, 110, 34, volume("#a0693a", 0.3, 0.8))]
    r = random.Random(graine)
    for k in range(14):
        m.append(trait(r.uniform(-100, 100), r.uniform(-20, 20), r.uniform(-100, 100), r.uniform(-20, 20), "#c9a24a", 3))
    out = [place(m, x, y, s)]
    for k in range(petits):
        out.append(petit(x - 50 * s + k * 50 * s, y - 6 * s, 0.38 * s, expr=expr, flip=k == 2))
    out.append(place([chemin("M -110 0 Q 0 40 110 0", "#8d5524")], x, y + 4 * s, s))
    return "".join(out)


def faucille(x, y, s=1.0, rot=0):
    return place([trait(0, 0, 0, 60, "#8d5524", 8), chemin("M 0 0 Q 60 -10 70 -60 Q 40 -20 0 -10 Z", "#adb5bd")], x, y, s, rot=rot)


def champ_vert(S, horizon=520, graine=1):
    """Le champ au printemps : le blé est encore vert."""
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, horizon, "#c0eb75", graine=graine, hauteur=80)
    sol(S, horizon + 40, "#8ce99a", bosse=10, premier=False)
    r = random.Random(graine)
    for k in range(70):
        yy = r.uniform(horizon + 50, 790)
        prof = (yy - horizon) / (800 - horizon)
        S.add(place([trait(0, 0, 0, -100, "#69db7c", 4), ellipse(0, -110, 5, 14, "#8ce99a")], r.uniform(0, 800), yy, 0.35 + prof * 0.75,
                    rot=r.uniform(-12, 12)))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    champ(S, 520, graine=2)
    S.add(nid(400, 720, 1.6, graine=2))
    S.add(alouette(560, 680, 1.4, expr="content", flip=True))
    S.add(maitre(120, 560, 0.6, expr="content"))
    ble_devant(S, 4)
    S.cachette(740, 300, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(alouette(200, 250, 1.2, expr="content"))
    return S


def p01():
    """Plan large : au printemps, l'alouette fait son nid au milieu du blé encore vert."""
    S = Scene()
    champ_vert(S, 520, graine=1)
    S.add(nid(400, 720, 1.5, petits=0, graine=1))
    S.add(alouette(380, 690, 1.3, expr="content", epi_bec=False))
    S.add(texte(400, 130, "Un nid dans le blé", 52, "#5c940d", contour="#fff"))
    return S


def p02():
    """Plan moyen : les petits sont nés, le blé est doré ; l'alouette s'envole : « Écoutez bien ce que dira le maître du champ ! »"""
    S = Scene()
    champ(S, 520, graine=3)
    S.add(nid(360, 740, 1.6, graine=3, expr="content"))
    S.add(alouette(560, 380, 1.1, expr="sourire", ailes="haut", flip=True))
    S.add(bulle(400, 150, 480, 110, "Écoutez bien ce que dira\nle maître du champ !", 30, pointe=(530, 280)))
    return S


def p03():
    """Plan large : le maître du champ et son fils regardent le blé : « Va dire à nos amis de venir moissonner demain ! »"""
    S = Scene()
    champ(S, 520, graine=4)
    S.add(maitre(300, 790, 1.7, expr="content", bras="designe", regard=(1, 0)))
    S.add(fils(560, 790, 1.5, expr="content", bras="bas", flip=True, regard=(-1, 0)))
    S.add(nid(700, 770, 0.8, graine=4, expr="surpris"))
    ble_devant(S, 5)
    S.add(bulle(330, 150, 460, 110, "Le blé est mûr. Va dire à nos\namis de venir nous aider demain !", 28, pointe=(320, 300)))
    return S


def p04():
    """Gros plan : les petits, affolés, racontent tout à leur mère ; elle reste calme : « Rien ne presse. »"""
    S = Scene()
    champ(S, 520, graine=5)
    S.add(nid(380, 760, 2.2, graine=5, expr="surpris"))
    S.add(alouette(620, 700, 1.6, expr="content", flip=True))
    S.add(bulle(330, 170, 420, 130, "S'il compte sur ses amis,\nrien ne presse.\nDormez tranquilles !", 30, pointe=(560, 420)))
    S.cachette(60, 300, "air")
    return S


def p05():
    """Plan large : le lendemain, personne n'est venu ; le maître dit à son fils : « Va demander à nos cousins ! »"""
    S = Scene()
    champ(S, 520, graine=6)
    S.ambiance("soir")
    S.add(maitre(320, 790, 1.7, expr="fache", bras="hanches", regard=(1, 0)))
    S.add(fils(560, 790, 1.5, expr="inquiet", bras="bas", flip=True, regard=(-1, 0)))
    S.add(nid(700, 770, 0.8, graine=6, expr="surpris"))
    S.add(bulle(330, 150, 440, 110, "Nos amis ne sont pas venus.\nVa demander à nos cousins !", 28, pointe=(320, 300)))
    return S


def p06():
    """Plan large : personne, encore ; le maître décide : « Demain, nous moissonnerons nous-mêmes ! »"""
    S = Scene()
    champ(S, 520, graine=7)
    S.add(maitre(320, 790, 1.7, expr="concentre", bras="poing", regard=(1, -0.2)))
    S.add(fils(560, 790, 1.5, expr="content", bras="hanches", flip=True, regard=(-1, 0)))
    S.add(faucille(150, 700, 0.9, rot=-20), faucille(660, 690, 0.9, rot=20))
    S.add(nid(720, 780, 0.7, graine=7, expr="surpris"))
    S.add(bulle(360, 150, 460, 110, "Puisque c'est comme ça,\ndemain, nous le ferons nous-mêmes !", 28, pointe=(320, 300)))
    return S


def p07():
    """Plan moyen : l'alouette : « Cette fois, partons ! » ; la mère et ses petits s'envolent du nid."""
    S = Scene()
    champ(S, 520, graine=8)
    S.add(nid(380, 760, 1.4, petits=0, graine=8))
    S.add(alouette(420, 420, 1.2, expr="concentre", ailes="haut", flip=True))
    for k, (x, y) in enumerate(((250, 520), (330, 470), (520, 500))):
        S.add(petit(x, y, 0.5, expr="rire", ailes="haut", flip=k == 2))
    S.add(texte(400, 140, "Cette fois, partons !", 54, "#e8590c", contour="#fff"))
    return S


def p08():
    """Plan large : le lendemain, le maître et son fils moissonnent ; le nid est vide ; les alouettes chantent dans un autre champ."""
    S = Scene()
    champ(S, 560, graine=9)
    S.add(maitre(250, 790, 1.6, expr="content", bras="tient", regard=(1, 0.3), objet=faucille(68, -150, 0.8, rot=10)))
    S.add(fils(470, 790, 1.45, expr="content", bras="tient", regard=(1, 0.3), objet=faucille(68, -150, 0.8, rot=10)))
    S.add(nid(680, 790, 0.7, petits=0, graine=9))
    S.add(alouette(640, 260, 0.6, ailes="haut", flip=True), petit(700, 300, 0.32, ailes="haut", flip=True), petit(580, 300, 0.3, ailes="haut", flip=True))
    S.add(notes(560, 200, 0.8, BRUN_FONCE))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("alouette-seule.svg", vignette),
    ("01-le-nid.svg", p01), ("02-ecoutez-bien.svg", p02), ("03-le-maitre.svg", p03),
    ("04-rien-ne-presse.svg", p04), ("05-le-lendemain.svg", p05), ("06-nous-memes.svg", p06),
    ("07-partons.svg", p07), ("08-la-moisson.svg", p08),
]
