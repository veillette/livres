"""Inès et les trois souhaits — le plus beau des vœux."""
from base import *
from base import _assombrir
from objets import *
from fantastique import *
from fables import araignee_perso

ID = "ines-souhaits"
INES = dict(peau="doree", cheveux="chatain", coiffure="boucles", habit="#ffa94d",
            chaussures="#e8590c", acc=("noeud",), couleur_acc="#f06595")
PLUMETTE = dict(peau="claire", cheveux="#9775fa", coiffure="chignon", habit="#e599f7",
                ailes="#f3f0ff")
PAPI = dict(peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#1c7ed6",
            robe=False, jambes="#364fc7", chaussures="#5c3a1e", barbe="#e9ecef", acc=("lunettes",))
FORMULE = "Abracadabri,\nabracadabra !"


def ines(x, y, s=1.0, **k):
    return personne(x, y, s, **{**INES, **k})


def plumette(x, y, s=0.32, baguette_=True, **k):
    """La minuscule fée ; (x, y) = ses pieds."""
    k.setdefault("bras", "tient")
    obj = baguette(68, -146, 0.9, rot=15) if baguette_ and k["bras"] in ("tient", "montre", "salut") else None
    return personne(x, y, s, objet=obj, **{**PLUMETTE, **k})


def casquette_marin():
    return g([chemin("M -50 -176 Q -48 -214 0 -216 Q 48 -214 50 -176 Z", "#f8f9fa"),
              rect(-52, -184, 104, 14, "#1c2a52", rx=6),
              chemin("M -46 -172 Q 0 -160 46 -172 L 40 -162 Q 0 -152 -40 -162 Z", "#1c2a52"),
              cercle(0, -194, 7, "#fab005")])


def papi_jo(x, y, s=1.0, flip=False, **k):
    return place([personne(0, 0, 1.0, **{**PAPI, **k}), casquette_marin()], x, y, s, flip=flip)


def jardin(S, soir=False, y=640):
    if soir:
        ciel(S, "#ff8787", "#ffd8a8")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(nuage(150, 120, 0.7), nuage(640, 90, 0.55))
    sol(S, y, "#8ce99a" if not soir else "#69db7c")
    S.add(herbe(90, y + 30, 1.2), herbe(720, y + 40, 1.0))


def haie(S, y=520, x0=-40, x1=840):
    for k, x in enumerate(range(x0, x1, 90)):
        S.add(buisson(x, y, 1.1, "#2f9e44" if k % 2 else "#37b24d", "#40c057"))


def bonbon(x, y, s=1.0, couleur="#f06595", rot=0):
    m = [poly([(-30, -14), (-16, 0), (-30, 14)], _assombrir(couleur, 0.85)),
         poly([(30, -14), (16, 0), (30, 14)], _assombrir(couleur, 0.85)),
         ellipse(0, 0, 20, 15, couleur),
         chemin("M -8 -10 Q 0 0 -8 10", stroke="#fff", sw=3, opacity=0.6)]
    return place(m, x, y, s, rot=rot)


def sucette(x, y, s=1.0, couleur="#ff6b6b", rot=0):
    m = [rect(-3, 0, 6, 70, "#f8f9fa", rx=3), cercle(0, -10, 26, couleur),
         chemin("M 0 -10 m -16 0 a 16 16 0 1 1 16 16 a 10 10 0 1 1 -10 -10", stroke="#fff", sw=5)]
    return place(m, x, y, s, rot=rot)


COULEURS_BONBONS = ["#f06595", "#ffd43b", "#69db7c", "#4dabf7", "#ff922b", "#cc5de8", "#ff6b6b"]


def montagne_bonbons(x, y, s=1.0, graine=3, h=300, w=320):
    """Tas de bonbons en forme de montagne ; (x, y) = milieu de la base."""
    r = random.Random(graine)
    m = [chemin(f"M {-w} 0 Q {-w * 0.4} {-h * 0.9} 0 {-h} Q {w * 0.4} {-h * 0.9} {w} 0 Z", "#ffe3ec")]
    rangs = 9
    for i in range(rangs):
        yy = -i * h / rangs - 14
        demi = w * (1 - i / rangs) * 0.95
        nb = max(1, int(demi / 26))
        for j in range(nb):
            xx = -demi + (j + 0.5) * 2 * demi / nb + r.uniform(-8, 8)
            c = r.choice(COULEURS_BONBONS)
            if r.random() < 0.18:
                m.append(cercle(xx, yy, 16, c) + cercle(xx - 5, yy - 5, 5, "#fff", opacity=0.6))
            else:
                m.append(bonbon(xx, yy, 0.8, c, rot=r.uniform(-40, 40)))
    m.append(sucette(-w * 0.35, -h * 0.55, 1.1, "#ff6b6b", rot=-15))
    m.append(sucette(w * 0.3, -h * 0.6, 1.0, "#4dabf7", rot=20))
    m.append(sucette(0, -h - 20, 1.3, "#cc5de8"))
    return place(m, x, y, s)


def bateau(x, y, s=1.0, coque="#e03131", voile="#fff"):
    m = [chemin("M -70 0 L 70 0 L 50 30 L -50 30 Z", coque), rect(-3, -110, 6, 112, "#8d5524"),
         poly([(4, -104), (4, -6), (64, -6)], voile), poly([(-4, -90), (-4, -6), (-50, -6)], "#ffe066")]
    return place(m, x, y, s)


def mouette(x, y, s=1.0):
    return place([chemin("M -30 0 Q -16 -18 0 0 Q 16 -18 30 0", stroke=ENCRE, sw=4)], x, y, s)


def photo_bateau(x, y, s=1.0, rot=0):
    """Petite photo dans un cadre ; (x, y) = centre."""
    m = [rect(-46, -38, 92, 76, "#fff", rx=4, stroke="#c68642", stroke_width=5), rect(-38, -30, 76, 40, "#a5d8ff"),
         rect(-38, 6, 76, 24, "#4dabf7"), place(bateau(0, 0, 0.32), 0, 10)]
    return place(m, x, y, s, rot=rot)


def maison_ines(S, x=400, y=780, w=640, h=560, porte_h=300, porte_w=190, px=None):
    """Façade de la maison d'Inès en gros plan, avec la porte ouverte."""
    S.add(rect(x - w / 2, y - h, w, h, "#ffe8cc"))
    S.add(poly([(x - w / 2 - 40, y - h + 4), (x, y - h - 120), (x + w / 2 + 40, y - h + 4)], "#e8590c"))
    S.add(fenetre(x - w / 2 + 40, y - h + 60, 120, 110, rideaux="#ffc9c9"))
    S.add(fenetre(x + w / 2 - 160, y - h + 60, 120, 110, rideaux="#ffc9c9"))
    px = x if px is None else px
    S.add(rect(px - porte_w / 2 - 14, y - porte_h - 14, porte_w + 28, porte_h + 14, "#a0522d", rx=8))
    S.add(rect(px - porte_w / 2, y - porte_h, porte_w, porte_h, "#495057"))
    S.add(rect(px - porte_w / 2, y - porte_h, porte_w, porte_h, "#ffd8a8", opacity=0.35))
    S.add(rect(px - porte_w / 2, y - porte_h, porte_w, porte_h * 0.25, "#000", opacity=0.15))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S)
    S.add(arbre(110, 660, 1.3), fleur(700, 700, 1.8, "#f06595", tige=70), fleur(620, 720, 1.4, "#ffd43b", tige=60))
    S.add(ines(340, 770, 2.0, expr="rire", bras="donne2", regard=(1, -1)))
    S.add(plumette(510, 588, 0.5, expr="rire", bras="salut"))
    S.add(etincelles(560, 420, 1.4, graine=4), etincelles(640, 300, 1.0, graine=7, couleur="#f783ac"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 140, 150, 110, "#f3f0ff"))
    S.add(plumette(200, 240, 0.95, expr="content", bras="salut"))
    for k, (px, py) in enumerate([(70, 80), (330, 70), (340, 190)]):
        S.add(etoile5(px, py, 20 - k * 2, OR))
    return S


def p01():
    S = Scene()
    jardin(S)
    S.add(arbre(130, 660, 1.4, fruits="#fa5252"))
    S.add(rect(560, 440, 8, 210, "#adb5bd"), rect(752, 440, 8, 210, "#adb5bd"))
    S.add(toile(660, 470, 90, perles=True))
    S.add(cercle(660, 470, 9, "#e599f7"))
    S.add(ines(360, 740, 1.6, expr="surpris", bras="bas", regard=(1, -1)))
    S.add(bulle(620, 210, 280, 90, "Au secours !", 40, pointe=(655, 455)))
    S.add(papillon(250, 230, 0.9))
    return S


def p02():
    S = Scene()
    jardin(S)
    S.add(rect(150, 0, 12, 640, "#adb5bd"), rect(740, 0, 12, 640, "#adb5bd"))
    S.add(toile(450, 300, 260, perles=True))
    S.add(plumette(450, 360, 0.55, expr="pleure", bras="haut", baguette_=False))
    S.add(baguette(370, 380, 0.7, rot=-40, brille=False))
    S.add(araignee_perso(640, 220, 0.9, expr="surpris", fil=220, regard=(-1, 0)))
    S.add(ines(200, 790, 1.7, expr="concentre", bras="montre", regard=(1, -1)))
    # la brindille qui décroche délicatement les fils
    S.add(trait(200 + 86 * 1.7, 790 - 130 * 1.7, 425, 400, "#8d5524", 7))
    S.add(bulle(560, 600, 380, 100, "Pardon, madame l'araignée,\nje fais tout doucement !", 28, pointe=(320, 620)))
    return S


def p03():
    S = Scene()
    jardin(S)
    S.add(fleur(90, 700, 2.2, "#ff8787", tige=80), fleur(720, 690, 2.0, "#ffd43b", tige=80))
    S.add(ines(300, 790, 2.1, expr="bouche_bee", bras="donne2", regard=(1, -1)))
    S.add(plumette(483, 597, 0.6, expr="rire", bras="tient"))
    S.add(etincelles(540, 440, 1.0, graine=2))
    S.add(bulle(400, 110, 560, 120, "Merci, Inès ! Pour te remercier,\nje t'offre trois souhaits !", 32, pointe=(500, 470)))
    for k in range(3):
        S.add(etoile5(580 + k * 70, 260, 22, OR))
    return S


def p04():
    S = Scene()
    jardin(S)
    S.add(montagne_bonbons(520, 700, 1.0, h=430, w=300))
    S.add(ines(170, 760, 1.5, expr="rire", bras="haut"))
    S.add(plumette(330, 330, 0.4, expr="malin", bras="tient"))
    S.add(etincelles(480, 220, 1.3, graine=5))
    S.add(texte(400, 110, "Abracadabri, abracadabra !", 42, "#fff", contour="#ae3ec9"))
    return S


def p05():
    S = Scene()
    jardin(S)
    S.add(montagne_bonbons(560, 690, 0.8, graine=6, h=360, w=260))
    for k in range(9):
        S.add(bonbon(80 + k * 75, 735 + (k % 3) * 18, 0.7, COULEURS_BONBONS[k % 7], rot=k * 37))
    S.add(ines(250, 720, 1.6, expr="oups", bras="porte"))
    S.add(bulle(250, 150, 420, 110, "Ouille, mon ventre !\nJe n'en veux plus !", 36, pointe=(260, 380)))
    S.add(plumette(560, 280, 0.38, expr="inquiet", bras="tient"))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(130, 170, 0.6), nuage(680, 240, 0.5))
    sol(S, 680, "#8ce99a")
    for x, c in [(70, "#e8590c"), (650, "#5c7cfa"), (750, "#e8590c")]:
        S.add(maison(x, 700, 0.42, toit=c))
    S.add(arbre(160, 700, 0.5), arbre(560, 705, 0.45))
    S.add(ines(390, 790, 3.05, expr="rire", bras="ouverts"))
    S.add(oiseau(250, 140, 0.45, "#ffd43b", ailes="haut"), oiseau(560, 120, 0.4, "#ff8787", ailes="haut", flip=True))
    S.add(plumette(660, 420, 0.3, expr="surpris", bras="tient"))
    S.add(texte(400, 60, "La plus grande du monde !", 46, "#fff", contour="#ae3ec9"))
    return S


def p07():
    S = Scene()
    jardin(S, y=700)
    maison_ines(S, 400, 790, 680, 520, porte_h=280, porte_w=170, px=580)
    S.add(ines(250, 790, 2.6, expr="oups", bras="tete", regard=(1, 0)))
    S.add(eclat(420, 300, 1.2, "#ffd43b"), etoile5(440, 290, 16, "#fff"))
    S.add(texte(600, 300, "BONG !", 70, "#fff", contour="#e03131", rot=-12))
    S.add(plumette(700, 560, 0.34, expr="inquiet", bras="tient"))
    return S


def p08():
    S = Scene()
    jardin(S, y=600)
    haie(S, 600)
    S.add(arbre(700, 660, 1.0))
    S.add(ines(260, 770, 1.6, expr="neutre", bras="pense", regard=(1, -1)))
    S.add(plumette(160, 580, 0.36, expr="sourire", bras="tient"))
    contenu = g([chateau(470, 260, 0.16), sucette(580, 220, 0.8, "#cc5de8"), texte(530, 160, "?", 60, "#ae3ec9")])
    S.add(pensee(530, 200, 150, contenu, depuis=(330, 470)))
    S.add(etoile5(640, 420, 26, OR))
    S.add(texte(640, 476, "plus qu'un !", 30, "#ae3ec9"))
    return S


def p09():
    S = Scene()
    jardin(S, y=620)
    S.add(papi_jo(560, 760, 1.6, expr="triste", bras="donne", flip=True, regard=(-1, 0),
                  objet=photo_bateau(96, -96, 0.75)))
    S.add(ines(210, 770, 1.4, expr="triste", bras="bas", regard=(1, 0)))
    S.add(bulle(470, 120, 600, 140, "Quand j'étais marin, je voyais\nla mer tous les jours. Maintenant,\nelle est bien trop loin pour moi…", 30, pointe=(560, 410)))
    return S


def p10():
    S = Scene()
    jardin(S, y=620)
    haie(S, 620)
    S.add(ines(300, 790, 2.3, expr="malin", bras="donne2", regard=(1, -1)))
    S.add(plumette(490, 578, 0.6, expr="surpris", bras="tient"))
    S.add(bulle(470, 110, 560, 110, "Mon dernier souhait,\nc'est pour Papi Jo !", 40, pointe=(400, 300)))
    return S


def p11():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(680, 110, 50), nuage(200, 130, 0.6))
    S.add(rect(0, 330, 800, 200, "#1c7ed6"))
    S.add(bateau(220, 360, 0.6), mouette(420, 200, 1.0), mouette(500, 240, 0.7), mouette(290, 220, 0.8))
    S.add(chemin("M 0 500 Q 200 470 400 500 T 800 490 L 800 800 L 0 800 Z", "#f4d58d"))
    S.add(chemin("M 0 470 Q 120 520 260 480 Q 400 450 520 490 Q 660 530 800 470 L 800 330 L 0 330 Z", "#339af0"))
    for k in range(5):
        S.add(chemin(f"M {40 + k * 160} 420 q 20 -12 40 0", stroke="#a5d8ff", sw=5))
    S.add(coquillage(110, 740, 1.0), coquillage(700, 750, 0.9, "#ffe066"))
    S.add(papi_jo(510, 720, 1.6, expr="rire", bras="haut"))
    S.add(ines(250, 740, 1.4, expr="rire", bras="ouverts"))
    S.add(plumette(390, 440, 0.32, expr="rire", bras="tient"))
    S.add(etincelles(390, 380, 1.0, graine=9))
    S.add(texte(400, 300, "La mer !", 56, "#fff", contour="#1864ab"))
    return S


def p12():
    S = Scene()
    ciel(S, "#ff8787", "#ffe066")
    S.add(cercle(400, 400, 90, "#fff3bf", opacity=0.9))
    S.add(rect(0, 400, 800, 120, "#4c6ef5"))
    S.add(chemin("M 0 500 Q 200 470 400 500 T 800 490 L 800 800 L 0 800 Z", "#f4d58d"))
    for k in range(4):
        S.add(chemin(f"M {80 + k * 200} 450 q 20 -12 40 0", stroke="#bac8ff", sw=5))
    S.add(papi_jo(500, 740, 1.5, expr="content", bras="calin", regard=(-1, 0)))
    S.add(ines(310, 750, 1.35, expr="content", bras="calin", regard=(1, 0)))
    S.add(plumette(660, 520, 0.4, expr="content", bras="tient"))
    S.add(coeur(400, 260, 1.4), coeur(460, 220, 0.9, "#ff8787"))
    S.add(bulle(560, 110, 420, 110, "C'est le plus beau\ndes vœux, Inès.", 36, pointe=(660, 440)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("fee-plumette.svg", vignette),
    ("01-au-secours.svg", p01), ("02-la-toile.svg", p02), ("03-trois-souhaits.svg", p03),
    ("04-bonbons.svg", p04), ("05-mal-au-ventre.svg", p05), ("06-la-plus-grande.svg", p06),
    ("07-la-porte.svg", p07), ("08-plus-qu-un.svg", p08), ("09-papi-jo.svg", p09),
    ("10-dernier-souhait.svg", p10), ("11-la-mer.svg", p11), ("12-le-plus-beau.svg", p12),
]
