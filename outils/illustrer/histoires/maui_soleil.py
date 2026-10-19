"""Maui et le soleil — d'après une légende maorie de Nouvelle-Zélande.

Autrefois, le soleil courait si vite dans le ciel que les journées étaient
toutes petites : on n'avait pas le temps de cuire le repas, de pêcher, ni
de faire sécher le linge. Maui, le plus jeune et le plus malin de ses
frères, décide de ralentir le soleil. Avec ses frères et les femmes du
village, il tresse des cordes très solides en feuilles de lin (harakeke).
Ils marchent toute la nuit vers l'est, jusqu'au trou d'où le soleil sort
chaque matin, et se cachent. Quand le soleil se lève, ils lancent les
cordes : le voilà attrapé ! Maui lui parle : « Va plus lentement, pour que
les gens aient le temps de vivre. » Le soleil promet. Depuis, les
journées sont longues. Ici, personne ne frappe le soleil : on discute.

Plans : 1 large (le soleil trop rapide) · 2 moyen (« Déjà la nuit ! ») · 3
moyen (l'idée de Maui) · 4 gros plan (tresser les cordes) · 5 large (la
marche de nuit) · 6 moyen (cachés) · 7 large (le lasso) · 8 gros plan
(« Ralentis ! ») · 9 large (les longues journées).
"""
from contes import *
from base import _assombrir
from fetes import cerf_volant_losange

ID = "maui-soleil"

MAUI = dict(stature="ado", peau="brune", cheveux="noir", coiffure="chignon", habit="#c5a07a", robe=False, jambes="#8d5524",
            ceinture="#e03131", nez="rond")
FRERES = [dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#a07c58", robe=False, jambes="#5c3d24",
               carrure="ronde", nez="rond", barbe="#343a40"),
          dict(stature="adulte", peau="brune", cheveux="noir", coiffure="chignon", habit="#e9d8a6", robe=False, jambes="#5c3d24", carrure="fine",
               nez="long"),
          dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="afro", habit="#8d5524", robe=False, jambes="#495057")]
KUIA = dict(stature="ancien", peau="brune", cheveux="blanc", coiffure="chignon", habit="#343a40", robe=True, cape="#e9d8a6", nez="rond",
            carrure="ronde")
FEMME = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="longs", habit="#c92a2a", robe=True, nez="petit")
LIN = "#c5a07a"


def corde(x0, y0, x1, y1, creux=30, ep=8):
    """Corde de lin tressée, un peu lâche."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + creux
    d = f"M {n(x0)} {n(y0)} Q {n(mx)} {n(my)} {n(x1)} {n(y1)}"
    return g([chemin(d, stroke="#8d6e4a", sw=ep), chemin(d, stroke=LIN, sw=ep * 0.5, stroke_dasharray="6 6")])


def lasso(x, y, r):
    """La boucle d'une corde passée autour d'un cercle (le soleil), sous son visage."""
    y += r * 0.35
    return g([ellipse(x, y, r * 1.05, r * 0.32, "none", stroke="#8d6e4a", stroke_width=10),
              ellipse(x, y, r * 1.05, r * 0.32, "none", stroke=LIN, stroke_width=5, stroke_dasharray="6 6")])


def soleil_perso(x, y, r=90, expr="rire", S=None):
    """Le soleil, avec un visage."""
    if S is not None:
        S.lumiere(x, y, r * 3, "#ffd43b", 0.6)
    m = [soleil(x, y, r), yeux_simples(x, y - r * 0.2, r * 0.32, r * 0.1),
         ellipse(x - r * 0.55, y + r * 0.05, r * 0.14, r * 0.09, ROSE, opacity=0.6), ellipse(x + r * 0.55, y + r * 0.05, r * 0.14, r * 0.09, ROSE, opacity=0.6)]
    if expr == "surpris":
        m.append(ellipse(x, y + r * 0.2, r * 0.12, r * 0.15, "#e67700"))
    else:
        m.append(chemin(f"M {n(x - r * 0.28)} {n(y + r * 0.1)} Q {n(x)} {n(y + r * 0.38)} {n(x + r * 0.28)} {n(y + r * 0.1)}", stroke="#e67700", sw=r * 0.07))
    return g(m) + occuper(x - r * 1.3, y - r * 1.3, x + r * 1.3, y + r * 1.3)


def wharenui(x, y, s=1.0):
    """Maison commune maorie : pignon aux planches sculptées rouges, figure au sommet ; (x, y) = milieu du seuil."""
    rouge = "#a61e1e"
    m = [rect(-200, -200, 400, 200, volume("#8d5524", 0.3, 0.8)), planches(-200, -200, 400, 200, "#8d5524", larg=28),
         poly([(-260, -180), (0, -330), (260, -180), (230, -170), (0, -300), (-230, -170)], rouge),
         chemin("M -240 -186 L 0 -322 L 240 -186", stroke="#f8f9fa", sw=3, stroke_dasharray="10 8"),
         rect(-40, -140, 80, 140, "#3b2a1a"), rect(-50, -150, 100, 12, rouge), rect(-50, -150, 12, 150, rouge), rect(38, -150, 12, 150, rouge),
         rect(-150, -130, 60, 50, "#3b2a1a"), rect(-156, -136, 72, 8, rouge)]
    m += [cercle(0, -320, 26, rouge), cercle(-9, -324, 6, "#f8f9fa"), cercle(9, -324, 6, "#f8f9fa"), cercle(-9, -324, 3, ENCRE), cercle(9, -324, 3, ENCRE),
          rect(-8, -310, 16, 10, "#f8f9fa", rx=3)]
    for sgn in (-1, 1):
        m.append(rect(sgn * 216 - 12, -200, 24, 200, rouge))
        for k in range(4):
            m.append(chemin(f"M {sgn * 216 - 8} {-180 + k * 48} q 8 -14 16 0 q -8 14 -16 0", stroke="#f8f9fa", sw=2))
    return place(m, x, y, s)


def harakeke(x, y, s=1.0):
    """Une touffe de lin de Nouvelle-Zélande : longues feuilles en éventail."""
    m = []
    for k, a in enumerate(range(-50, 60, 14)):
        m.append(place([chemin("M -6 0 Q -10 -90 0 -170 Q 10 -90 6 0 Z", "#5c940d" if k % 2 else "#74b816")], 0, 0, 1.0, rot=a))
    m += [trait(-8, -150, -14, -230, "#5c3d24", 3), cercle(-14, -232, 6, "#c92a2a")]
    return place(m, x, y, s)


def aotearoa(S, horizon=500, moment="jour", graine=1):
    """Collines vertes, mer au loin, fougères et lin."""
    if moment == "nuit":
        nuit(S, "#16213e", "#3b4a7a")
        etoiles(S, 50, graine, (0, 0, 800, horizon - 40))
    elif moment == "aube":
        ciel(S, "#ff8787", "#ffe066")
    elif moment == "soir":
        ciel(S, "#e8590c", "#ffc078")
    else:
        ciel(S, "#4dabf7", "#e7f5ff")
    sombre = moment == "nuit"
    S.add(rect(0, horizon - 40, 800, 60, "#1971c2" if not sombre else "#1b2a5c"))
    collines(S, horizon, "#69db7c" if not sombre else "#2b4a3a", graine=graine)
    sol(S, horizon + 120, "#8ce99a" if not sombre else "#3a5c46")


def fosse_aube(S):
    """Le bord du monde, à l'est : une falaise devant la mer, et le trou d'où sort le soleil."""
    ciel(S, "#ff8787", "#ffe066")
    S.add(rect(0, 460, 800, 120, lineaire([(0, "#f783ac"), (1, "#5c7cfa")])))
    S.add(chemin("M 0 580 Q 400 540 800 580 L 800 800 L 0 800 Z", terrain("#8d6e4a")))
    S.add(ellipse(560, 590, 180, 40, "#3b2a1a"))
    S.proposer_cachette(60, 790)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    fosse_aube(S)
    S.add(soleil_perso(560, 260, 110, expr="surpris", S=S))
    S.add(lasso(560, 300, 110))
    hx, hy = mains_personne(220, 790, 1.5, "tire", stature="ado")[1]
    S.add(personne(220, 790, 1.5, expr="fier", bras="tire", flip=False, regard=(1, -1), **MAUI))
    S.add(corde(452, 340, hx, hy, creux=20, ep=10))
    S.cachette(720, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(soleil_perso(200, 135, 80, expr="content"))
    S.add(lasso(200, 170, 80))
    return S


def p01():
    """Plan large : le soleil file dans le ciel à toute vitesse ; au village, devant la maison commune, les gens n'ont le temps de rien."""
    S = Scene()
    aotearoa(S, 480)
    S.add(soleil_perso(600, 140, 60, expr="rire", S=S), mouvement(500, 150, 1.6, rot=0), mouvement(470, 120, 1.0))
    S.add(wharenui(260, 660, 0.85), harakeke(700, 700, 0.8))
    S.add(personne(530, 790, 1.0, expr="inquiet", bras="court", regard=(1, -1), **FRERES[1]))
    S.add(personne(660, 790, 1.0, expr="surpris", bras="surprise", regard=(-1, -1), flip=True, **FEMME))
    S.add(texte(250, 150, "Zzzoum !", 56, "#e8590c", contour="#fff"))
    S.cachette(70, 230, "air")
    return S


def p02():
    """Plan moyen : à peine midi passé, déjà le soir ; la grand-mère n'a pas fini de cuire le repas sur les pierres chaudes : « Déjà la nuit ! »"""
    S = Scene()
    aotearoa(S, 480, "soir")
    S.add(wharenui(620, 640, 0.7))
    S.add(ellipse(330, 740, 120, 26, "#495057"))
    for k in range(5):
        S.add(cercle(260 + k * 34, 730, 16, volume("#868e96", 0.3, 0.8)))
    S.add(rect(250, 690, 160, 30, "#40c057", rx=10), ellipse(330, 690, 70, 16, "#2f9e44"))
    S.add(personne(160, 790, 1.4, expr="fache", bras="hanches", regard=(1, -1), **KUIA))
    S.add(personne(480, 790, 1.15, expr="triste", bras="bas", flip=True, regard=(-1, 0), **MAUI))
    S.add(bulle(330, 160, 360, 90, "Déjà la nuit !", 40, pointe=(180, 480)))
    return S


def p03():
    """Plan moyen : Maui lève le poing : « J'attraperai le soleil ! » ; ses grands frères éclatent de rire."""
    S = Scene()
    aotearoa(S, 480)
    S.add(wharenui(400, 600, 0.6))
    S.add(personne(400, 790, 1.4, expr="fier", bras="poing", regard=(0, 0), **MAUI))
    S.add(personne(160, 790, 1.15, expr="rire", bras="ventre", regard=(1, 0), **FRERES[0]))
    S.add(personne(640, 790, 1.15, expr="rire", bras="applaudit", flip=True, regard=(-1, 0), **FRERES[1]))
    S.add(bulle(400, 140, 440, 90, "J'attraperai le soleil !", 34, pointe=(400, 340)))
    S.cachette(730, 220, "air")
    return S


def p04():
    """Gros plan : les femmes et les frères tressent de longues cordes avec les feuilles de lin ; Maui tire pour vérifier qu'elles sont solides."""
    S = Scene()
    aotearoa(S, 480)
    S.add(harakeke(80, 700, 1.0), harakeke(720, 700, 1.0))
    for k in range(3):
        S.add(corde(140, 720 + k * 20, 660, 720 + k * 20, creux=10))
    S.add(personne(250, 790, 1.2, expr="concentre", bras="ramasse", regard=(1, 0.5), **FEMME))
    S.add(personne(540, 790, 1.25, expr="concentre", bras="tire", regard=(1, 0), **MAUI))
    S.add(personne(400, 790, 1.15, expr="content", bras="ramasse", regard=(1, 0.5), **FRERES[2]))
    S.camera(1.3, 400, 560)
    S.dessus(texte(400, 90, "On tresse, on tresse…", 44, "#2b8a3e", contour="#fff"))
    S.cachette(654, 377, "air")
    return S


def p05():
    """Plan large : la nuit, sous les étoiles, Maui et ses frères marchent vers l'est, les cordes enroulées sur l'épaule."""
    S = Scene()
    aotearoa(S, 520, "nuit", graine=3)
    S.add(lune(130, 120, 30))
    for k, (x, d) in enumerate(((240, FRERES[0]), (380, FRERES[1]), (520, FRERES[2]), (660, MAUI))):
        S.add(personne(x, 760 - k * 6, 0.95, expr="sourire", bras="marche", regard=(1, 0), **d))
    S.add(texte(400, 300, "Vers l'est…", 50, "#fff3bf", contour="#16213e"))
    S.cachette(40, 790)
    return S


def p06():
    """Plan moyen : juste avant l'aube, au bord du trou d'où sort le soleil, Maui et ses frères se cachent derrière un muret, les cordes prêtes."""
    S = Scene()
    fosse_aube(S)
    S.ambiance("soir")
    S.add(personne(180, 790, 1.15, expr="malin", bras="chut", regard=(1, 0), **MAUI))
    S.add(personne(330, 790, 1.1, expr="inquiet", bras="mains_jointes", regard=(1, -0.5), **FRERES[0]))
    S.add(rect(80, 680, 400, 120, terrain("#a07c58"), rx=30))
    S.add(corde(100, 690, 460, 690, creux=-20))
    S.add(texte(560, 420, "Chut…", 50, "#fff", contour="#d9480f"))
    S.cachette(720, 790)
    return S


def p07():
    """Plan large : le soleil sort de son trou ; hop ! Maui et ses frères lancent les cordes et l'attrapent au lasso."""
    S = Scene()
    fosse_aube(S)
    S.add(soleil_perso(560, 430, 120, expr="surpris", S=S))
    S.add(lasso(560, 470, 120))
    for k, (x, d) in enumerate(((120, FRERES[0]), (240, MAUI), (340, FRERES[2]))):
        st = d.get("stature", "enfant")
        hx, hy = mains_personne(x, 790, 1.05, "tire", stature=st, carrure=d.get("carrure", "normale"))[1]
        S.add(personne(x, 790, 1.05, expr="concentre", bras="tire", regard=(1, -1), **d))
        S.add(corde(445, 512, hx, hy, creux=-10))
    hx, hy = mains_personne(760, 790, 1.05, "tire", flip=True, stature="adulte", carrure="fine")[0]
    S.add(personne(760, 790, 1.05, expr="concentre", bras="tire", flip=True, regard=(-1, -1), **FRERES[1]))
    S.add(corde(675, 512, hx, hy, creux=-10))
    S.add(texte(560, 140, "Attrapé !", 60, "#c92a2a", contour="#fff"))
    S.cachette(560, 790)
    return S


def p08():
    """Gros plan : Maui parle au soleil, gentiment mais fermement : « Ralentis, soleil, pour qu'on ait le temps de vivre ! »"""
    S = Scene()
    fosse_aube(S)
    S.add(soleil_perso(520, 380, 150, expr="surpris", S=S))
    S.add(lasso(520, 430, 150))
    S.add(personne(200, 790, 1.5, expr="fier", bras="leve_doigt", regard=(1, -1), **MAUI))
    S.camera(1.3, 400, 480)
    S.dessus(bulle(400, 100, 600, 110, "Ralentis, soleil, pour qu'on ait\nle temps de vivre !", 32))
    S.cachette(60, 790)
    return S


def p09():
    """Plan large : depuis, le soleil marche lentement ; au village, on cuit, on pêche, le linge sèche, un cerf-volant vole ; Maui sourit."""
    S = Scene()
    aotearoa(S, 480)
    S.add(soleil_perso(640, 140, 60, expr="content", S=S))
    S.add(wharenui(220, 640, 0.75))
    S.add(cerf_volant_losange(470, 180, 0.8, "#c92a2a", "#fff3bf", rot=-10, fil_vers=(560, 640)))
    S.add(personne(560, 790, 1.15, expr="rire", bras="tient", regard=(-1, -1), **MAUI))
    S.add(personne(700, 790, 1.1, expr="content", bras="ventre", flip=True, regard=(-1, 0), **KUIA))
    S.add(personne(380, 790, 1.0, expr="joie", bras="saute", **FEMME))
    S.cachette(40, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("soleil-seul.svg", vignette),
    ("01-le-soleil-trop-rapide.svg", p01), ("02-deja-la-nuit.svg", p02), ("03-l-idee-de-maui.svg", p03),
    ("04-les-cordes.svg", p04), ("05-vers-l-est.svg", p05), ("06-caches.svg", p06),
    ("07-attrape.svg", p07), ("08-ralentis.svg", p08), ("09-les-longues-journees.svg", p09),
]
