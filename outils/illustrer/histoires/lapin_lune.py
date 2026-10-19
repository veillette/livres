"""Le lapin dans la lune — d'après une légende aztèque du Mexique.

Quetzalcoatl, le grand serpent à plumes, veut connaître la Terre. Il prend
la forme d'un homme et marche, marche, à travers le désert et les
montagnes. Un soir, épuisé, affamé, il s'assoit sur une pierre. Un petit
lapin qui grignote son herbe s'approche : « Veux-tu partager mon herbe ? »
« Merci, mais je ne mange pas d'herbe. » Le lapin réfléchit : « Je n'ai
rien d'autre que moi. Si tu as si faim, mange-moi. » Ému par ce cadeau,
Quetzalcoatl soulève le lapin jusqu'à la lune et y laisse son image, pour
que tout le monde se souvienne de sa bonté. Puis il le repose doucement
dans l'herbe. Les soirs de pleine lune, on voit le lapin.

Plans : 1 large (le serpent à plumes dans le ciel) · 2 large (le voyage)
· 3 moyen (épuisé) · 4 moyen (le lapin) · 5 gros plan (« Mange-moi ») · 6
moyen (dans ses bras) · 7 large (jusqu'à la lune) · 8 gros plan (l'image
du lapin) · 9 moyen (les soirs de pleine lune).
"""
from contes import *
from base import _assombrir

ID = "lapin-lune"

LAPIN = dict(couleur="#d9b48f")
TURQUOISE = "#0ca678"
QUETZAL = "#2b8a3e"


def plumes_quetzal(c=QUETZAL):
    """Coiffe de longues plumes vertes de quetzal, bandeau doré (coiffe)."""
    m = []
    for k, a in enumerate((-50, -30, -10, 10, 30, 50)):
        m.append(place([chemin("M 0 0 Q -14 -60 0 -130 Q 14 -60 0 0 Z", c if k % 2 else "#37b24d"), trait(0, 0, 0, -120, "#1c7c3c", 2)], 0, -196, 1.0, rot=a))
    m += [rect(-54, -206, 108, 20, "#fab005", rx=6), cercle(0, -196, 10, TURQUOISE), cercle(-30, -196, 6, "#e03131"), cercle(30, -196, 6, "#e03131")]
    return g(m)


VOYAGEUR = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="longs", habit=TURQUOISE, robe=False, jambes="#8d5524",
                cape=QUETZAL, ceinture="#fab005", nez="long", carrure="fine", coiffe=plumes_quetzal())


def serpent_plumes(x, y, s=1.0, flip=False, rot=0):
    """Quetzalcoatl, le serpent à plumes, qui ondule dans le ciel ; (x, y) = milieu du corps."""
    corps = "M -320 60 Q -240 -60 -140 20 Q -40 100 60 10 Q 160 -80 250 -20"
    m = [chemin(corps, stroke="#2f9e44", sw=46), chemin(corps, stroke="#8ce99a", sw=16, stroke_dasharray="10 14", opacity=0.8)]
    for k in range(9):
        t = -300 + k * 62
        yy = 60 * math.sin((t + 320) / 110) - 10
        m.append(place([chemin("M 0 0 Q -10 -30 0 -60 Q 10 -30 0 0 Z", "#fab005" if k % 2 else "#e03131")], t, yy - 20, 0.7, rot=-20))
    m += [ellipse(280, -30, 54, 36, volume("#2f9e44", 0.3, 0.8)), cercle(300, -44, 9, "#fff"), cercle(303, -44, 5, ENCRE),
          chemin("M 320 -20 Q 340 -14 330 -6", stroke=ENCRE, sw=3)]
    for k, a in enumerate((-80, -55, -30, -5)):
        m.append(place([chemin("M 0 0 Q -14 -50 0 -110 Q 14 -50 0 0 Z", QUETZAL if k % 2 else "#e03131")], 260, -50, 1.0, rot=a))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 340 * s, y - 150 * s, x + 340 * s, y + 90 * s)


def cactus(x, y, s=1.0, c="#5c940d"):
    """Grand cactus à bras (saguaro) ; (x, y) = pied."""
    m = [rect(-22, -220, 44, 220, cylindre(c, 0.25, 0.75), rx=22),
         chemin("M -20 -110 Q -70 -110 -70 -150 L -70 -180", stroke=c, sw=30), chemin("M 20 -140 Q 66 -140 66 -170 L 66 -200", stroke=c, sw=28)]
    for k in range(-1, 2):
        m.append(trait(k * 10, -210, k * 10, -10, _assombrir(c, 0.8), 2))
    return place(m, x, y, s)


def nopal(x, y, s=1.0, fleurs=True):
    m = [ellipse(0, -40, 30, 42, volume("#74b816", 0.3, 0.8)), ellipse(-34, -96, 24, 34, volume("#82c91e", 0.3, 0.8), rot=-20),
         ellipse(30, -100, 24, 34, volume("#82c91e", 0.3, 0.8), rot=20)]
    if fleurs:
        m += [cercle(-40, -130, 8, "#f06595"), cercle(36, -136, 8, "#fab005")]
    return place(m, x, y, s)


def pyramide(x, y, s=1.0, c="#d9a066"):
    """Pyramide à degrés, au loin ; (x, y) = milieu de la base."""
    m = []
    for k in range(5):
        w = 220 - k * 40
        m.append(rect(-w, -40 * (k + 1), 2 * w, 40, _assombrir(c, 1 - k * 0.03)))
    m += [rect(-20, -200, 40, 200, _assombrir(c, 0.8)), rect(-40, -240, 80, 40, _assombrir(c, 0.85))]
    return place(m, x, y, s)


def desert(S, horizon=520, moment="jour", graine=1):
    if moment == "nuit":
        nuit(S, "#1c2a52", "#5f3dc4")
        etoiles(S, 40, graine, (0, 0, 800, horizon - 60))
    elif moment == "soir":
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#4dabf7", "#fff3bf")
    sombre = moment == "nuit"
    S.add(pic(-60, horizon, 120, horizon - 160, 320, horizon, "#9775fa" if not sombre else "#3b2a7a", False),
          pic(420, horizon, 640, horizon - 200, 860, horizon, "#b197fc" if not sombre else "#4c3a8f", False))
    sol(S, horizon, "#e9b872" if not sombre else "#8d6e4a", bosse=12)


def lune_lapin(x, y, r=120, S=None, image=True, force=0.5):
    """La pleine lune et l'image du lapin (ses taches sombres)."""
    if S is not None:
        S.lumiere(x, y, r * 2.4, "#fff3bf", force)
    m = [lune(x, y, r, halo=False)]
    if image:
        k = r / 120
        m.append(place([ellipse(0, 20, 46, 40, "#e0c873"), cercle(30, -24, 26, "#e0c873"), ellipse(10, -74, 9, 34, "#e0c873", rot=-15),
                        ellipse(34, -76, 9, 34, "#e0c873", rot=15), cercle(-44, 40, 12, "#e0c873")], x - 10 * k, y + 10 * k, k))
    return g(m)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    desert(S, 600, "nuit")
    S.add(lune_lapin(520, 260, 160, S=S))
    S.add(cactus(100, 680, 0.9), nopal(700, 700, 0.9))
    S.add(perso("lapin", 300, 760, 1.4, expr="content", regard=(1, -1), bras="mains_jointes", **LAPIN))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lune_lapin(200, 135, 110))
    return S


def p01():
    """Plan large : dans le ciel, au-dessus des montagnes, Quetzalcoatl, le grand serpent à plumes, regarde la Terre."""
    S = Scene()
    desert(S, 600)
    S.add(nuage(160, 140, 1.2), nuage(640, 360, 0.9))
    S.add(serpent_plumes(400, 260, 1.0))
    S.add(pyramide(560, 600, 0.5), cactus(120, 700, 0.8), nopal(690, 720, 0.8))
    S.cachette(40, 790)
    return S


def p02():
    """Plan large : Quetzalcoatl a pris la forme d'un homme coiffé de plumes ; il marche à travers le désert, entre les cactus."""
    S = Scene()
    desert(S, 560)
    S.add(soleil(640, 120, 50))
    S.add(pyramide(640, 560, 0.4), cactus(110, 690, 1.0), cactus(720, 640, 0.6))
    S.add(chemin("M 260 800 Q 360 680 520 560", stroke="#d9a066", sw=40, opacity=0.5))
    S.add(personne(390, 760, 1.15, expr="sourire", bras="marche", regard=(1, 0), **VOYAGEUR))
    S.cachette(40, 790)
    return S


def p03():
    """Plan moyen : au soir, épuisé, affamé, le voyageur s'est assis sur une pierre ; il a faim et soif."""
    S = Scene()
    desert(S, 560, "soir")
    S.add(cactus(680, 680, 0.9), nopal(130, 690, 0.8))
    S.add(ellipse(400, 760, 110, 40, volume("#adb5bd", 0.3, 0.75)))
    S.add(personne(400, 790, 1.3, expr="triste", bras="joues", sy=0.82, regard=(0, 1), **VOYAGEUR))
    S.add(texte(400, 160, "Que j'ai faim…", 50, "#fff4e6", contour="#d9480f"))
    S.cachette(40, 790)
    return S


def p04():
    """Plan moyen : un petit lapin qui grignote son herbe s'approche : « Bonsoir, voyageur ! Veux-tu partager mon herbe ? »"""
    S = Scene()
    desert(S, 560, "soir")
    S.add(nopal(720, 690, 0.8))
    S.add(ellipse(560, 760, 110, 40, volume("#adb5bd", 0.3, 0.75)))
    S.add(personne(560, 790, 1.3, expr="surpris", bras="mains_basses", sy=0.82, flip=True, regard=(-1, 0.5), **VOYAGEUR))
    for k in range(5):
        S.add(touffe(150 + k * 50, 770, 1.0, "#69db7c", graine=k))
    S.add(perso("lapin", 270, 770, 1.05, expr="content", bras="tend", regard=(1, -0.5), **LAPIN))
    S.add(bulle(300, 200, 440, 110, "Bonsoir, voyageur !\nVeux-tu partager mon herbe ?", 28, pointe=(270, 560)))
    return S


def p05():
    """Gros plan : le lapin, tout petit et très sérieux : « Je n'ai rien d'autre que moi. Si tu as si faim… mange-moi. »"""
    S = Scene()
    desert(S, 560, "soir")
    for k in range(5):
        S.add(touffe(220 + k * 70, 780, 1.0, "#69db7c", graine=k + 3))
    S.add(perso("lapin", 400, 770, 1.3, expr="timide", bras="mains_basses", regard=(1, -1), **LAPIN))
    S.camera(1.7, 400, 600)
    S.dessus(bulle(400, 110, 560, 110, "Je n'ai rien d'autre que moi.\nSi tu as si faim… mange-moi.", 30))
    S.cachette(560, 790)
    return S


def p06():
    """Plan moyen : la nuit tombe ; ému, le voyageur prend doucement le petit lapin dans ses bras : « Quel grand cœur tu as ! »"""
    S = Scene()
    desert(S, 560, "nuit", graine=3)
    S.add(cactus(120, 690, 0.9), nopal(700, 700, 0.8))
    S.add(personne(400, 790, 1.5, expr="content", bras="calin", regard=(0, 0.5),
                   objet=perso("lapin", 0, -40, 0.42, expr="content", **LAPIN), **VOYAGEUR))
    S.add(bulle(400, 150, 440, 90, "Quel grand cœur tu as !", 32, pointe=(400, 320)))
    S.cachette(40, 790)
    return S


def p07():
    """Plan large : redevenu le grand serpent à plumes, Quetzalcoatl soulève le lapin jusqu'à la pleine lune."""
    S = Scene()
    desert(S, 660, "nuit", graine=5)
    S.add(lune_lapin(590, 180, 120, S=S, image=False))
    S.add(serpent_plumes(330, 470, 0.9, rot=-28))
    S.add(perso("lapin", 520, 300, 0.6, expr="bouche_bee", bras="haut", **LAPIN))
    S.add(cactus(100, 760, 0.7))
    S.cachette(740, 790)
    return S


def p08():
    """Gros plan : sur la pleine lune, l'image du lapin est apparue : on la voit encore aujourd'hui."""
    S = Scene()
    desert(S, 700, "nuit", graine=7)
    S.add(lune_lapin(400, 360, 230, S=S, force=0.7))
    S.camera(1.15, 400, 380)
    S.dessus(texte(400, 740, "Pour que tout le monde se souvienne de toi.", 30, "#fff3bf", contour="#1c2a52"))
    S.cachette(None)  # tout près de la lune, une coccinelle n'a rien à faire
    return S


def p09():
    """Plan moyen : de retour dans l'herbe, le petit lapin lève les yeux vers la pleine lune où l'on voit son image ; il est fier."""
    S = Scene()
    desert(S, 600, "nuit", graine=9)
    S.add(lune_lapin(560, 210, 110, S=S))
    S.add(cactus(120, 700, 0.9), nopal(690, 730, 0.7))
    for k in range(6):
        S.add(touffe(200 + k * 60, 780, 1.0, "#51cf66", graine=k + 9))
    S.add(perso("lapin", 340, 770, 1.35, expr="fier", regard=(1, -1), **LAPIN))
    S.cachette(40, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lune-seule.svg", vignette),
    ("01-le-serpent-a-plumes.svg", p01), ("02-le-voyage.svg", p02), ("03-epuise.svg", p03),
    ("04-le-lapin.svg", p04), ("05-mange-moi.svg", p05), ("06-dans-ses-bras.svg", p06),
    ("07-jusqu-a-la-lune.svg", p07), ("08-l-image.svg", p08), ("09-pleine-lune.svg", p09),
]
