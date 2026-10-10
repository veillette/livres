"""Pierre et le Loup — d'après le conte musical de Sergueï Prokofiev.

Pierre ouvre la barrière et va dans la prairie. Chaque personnage a son
instrument : l'oiseau la flûte, le canard le hautbois, le chat la
clarinette, le grand-père le basson, le loup trois cors, les chasseurs les
timbales, et Pierre les violons et tout le quatuor à cordes. L'oiseau et le
canard se disputent, le chat guette, le grand-père ramène Pierre. Le loup
sort de la forêt ; le chat grimpe dans l'arbre et le canard file se cacher
dans les roseaux (ici, il n'est pas avalé). Avec une corde, Pierre grimpe
sur le mur et la branche ; l'oiseau étourdit le loup en lui tournant autour
du nez ; Pierre l'attrape par la queue. Les chasseurs arrivent : « Ne tirez
pas ! » ; on emmène le loup au zoo, et le canard sort des roseaux.

Plans : 1 large (la prairie) · 2 schéma (les instruments) · 3 moyen (la
dispute) · 4 moyen (le chat) · 5 moyen (le grand-père) · 6 large (le loup !)
· 7 moyen (les roseaux) · 8 large (autour de l'arbre) · 9 large (la corde) ·
10 gros plan (attrapé !) · 11 large (ne tirez pas !) · 12 large (le cortège).
"""
from contes import *
from base import _assombrir
from objets import chat_profil
from animaux import roseau, etiquette, disque

ID = "pierre-loup"

PIERRE = dict(peau="rosee", cheveux="blond", coiffure="courts", habit="#e03131", robe=False, jambes="#1c7ed6")
GRAND_PERE = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chauve_cote", habit="#795548", robe=False, jambes="#495057",
                  barbe="#f8f9fa", nez="rond", carrure="ronde")
CHASSEURS = [dict(stature="adulte", peau=p, cheveux=c, coiffure="courts", habit="#2b8a3e", robe=False, jambes="#795548", barbe=b, nez=nz)
             for p, c, b, nz in (("doree", "brun", "#4a2c17", "long"), ("claire", "roux", None, "rond"), ("brune", "noir", "#2b2b3a", "pointu"))]
JAUNE_CANARD = "#ffffff"


def pierre(x, y, s=1.45, **k):
    return personne(x, y, s, **{**PIERRE, **k})


def grand_pere(x, y, s=1.7, **k):
    return personne(x, y, s, **{**GRAND_PERE, **k})


def loup_(x, y, s=1.4, **k):
    return perso("loup", x, y, s, **k)


def oiseau_(x, y, s=0.6, **k):
    k.setdefault("ailes", "haut")
    return oiseau(x, y, s, "#4dabf7", **k)


def canard_(x, y, s=0.9, **k):
    return canard(x, y, s, couleur="#f8f9fa", **k)


def chat_(x, y, s=1.0, **k):
    return chat_profil(x, y, s, couleur="#495057", rayures=False, **k)


def corde(x1, y1, x2, y2, mou=30):
    return chemin(f"M {x1} {y1} Q {(x1 + x2) / 2} {max(y1, y2) + mou} {x2} {y2}", stroke="#c9a24a", sw=6)


def prairie(S, horizon=430, arbre_=True, mur=True, mare_=True, roseaux=True):
    """La prairie : la forêt au fond, le mur du jardin à gauche, le grand arbre, la mare à droite."""
    ciel(S, "#74c0fc", "#e7f5ff")
    for k in range(10):
        S.add(sapin(-20 + k * 90, horizon + 10 * (k % 2), 0.75, "#2b8a3e", "#2f9e44"))
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#8ce99a")))
    if mare_:
        S.add(ellipse(600, 720, 220, 70, volume("#4dabf7", 0.3, 0.8)), ellipse(600, 700, 180, 40, "#74c0fc", opacity=0.6))
    if roseaux:
        for x in (400, 420, 445, 780, 800):
            S.add(roseau(x, 760, 1.0, 200, rot=-4 if x < 600 else 4))
    if mur:
        S.add(rect(0, 360, 130, 440, "#adb5bd"), pierres(0, 360, 130, 440, "#adb5bd", opacite=0.45), rect(0, 350, 140, 20, "#868e96"))
    if arbre_:
        S.add(rect(215, 300, 60, 470, cylindre("#8d5524", 0.3, 0.75)), chemin("M 245 340 Q 360 330 470 300", stroke="#8d5524", sw=24))
        for px, py, r in ((245, 220, 120), (150, 280, 80), (340, 260, 90), (470, 270, 60)):
            S.add(cercle(px, py, r, volume("#40c057", 0.35, 0.8)))


def cache_roseaux(S, x=430, y=760):
    for k in range(8):
        S.add(roseau(x - 50 + k * 14, y, 1.1, 230, rot=-6 + k * 2))


# --- instruments (pour le schéma) -------------------------------------------

def flute(x, y, s=1.0):
    return place([rect(-70, -5, 140, 10, "#ced4da", rx=4)] + [cercle(-40 + k * 18, 0, 3, "#868e96") for k in range(6)], x, y, s)


def hautbois(x, y, s=1.0):
    return place([poly([(-5, -70), (5, -70), (12, 60), (-12, 60)], "#212529"), trait(0, -70, 0, -86, "#e9c46a", 3)] +
                 [cercle(0, -40 + k * 20, 3, "#ced4da") for k in range(5)], x, y, s)


def clarinette(x, y, s=1.0):
    return place([rect(-7, -70, 14, 120, "#212529", rx=4), poly([(-7, 50), (7, 50), (18, 74), (-18, 74)], "#343a40")] +
                 [cercle(0, -50 + k * 20, 3, "#ced4da") for k in range(5)], x, y, s)


def basson(x, y, s=1.0):
    return place([rect(-10, -90, 20, 170, "#8d5524", rx=6), chemin("M 0 -60 Q -30 -70 -34 -96", stroke="#adb5bd", sw=4)], x, y, s)


def cor(x, y, s=1.0):
    return place([cercle(0, 0, 34, "none", stroke=OR_FONCE, stroke_width=8), cercle(0, 0, 20, "none", stroke=OR, stroke_width=5),
                  poly([(24, -24), (62, -50), (66, -10)], OR)], x, y, s)


def timbale(x, y, s=1.0):
    return place([chemin("M -50 -20 Q -46 40 0 44 Q 46 40 50 -20 Z", volume("#d9480f", 0.3, 0.8)), ellipse(0, -20, 50, 12, "#f8f9fa"),
                  trait(-60, -60, -20, -26, "#8d5524", 4), cercle(-60, -60, 7, "#fff"), trait(60, -60, 20, -26, "#8d5524", 4),
                  cercle(60, -60, 7, "#fff")], x, y, s)


def violon(x, y, s=1.0):
    return place([ellipse(0, 20, 26, 32, "#c46a1a"), ellipse(0, -16, 20, 24, "#c46a1a"), rect(-4, -80, 8, 70, "#212529"),
                  trait(-40, -60, 50, 50, "#e9c46a", 3)], x, y, s, rot=20)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    prairie(S, mare_=False, roseaux=False, arbre_=False)
    S.add(loup_(620, 560, 1.0, expr="malin", bras="bas", regard=(-1, 0)))
    S.add(pierre(330, 800, 1.75, expr="rire", bras="tient", regard=(1, -0.3),
                 objet=g([corde(60, -150, 110, -40, 40), cercle(110, -40, 26, "none", stroke="#c9a24a", stroke_width=6)])))
    S.add(oiseau_(520, 260, 0.8, flip=True))
    S.cachette(760, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chemin("M 0 200 Q 200 180 400 150", stroke="#8d5524", sw=16))
    S.add(oiseau_(200, 186, 0.8, ailes="bas"))
    return S


def p01():
    """Plan large : un beau matin, Pierre ouvre la barrière du jardin et s'en va dans la prairie verte."""
    S = Scene()
    prairie(S, mur=False)
    S.add(rect(0, 470, 200, 20, "#a0693a"), rect(0, 530, 200, 20, "#a0693a"))
    for x in (10, 190):
        S.add(rect(x - 8, 440, 16, 140, "#8d5524"))
    S.add(poly([(190, 450), (300, 420), (300, 570), (190, 580)], "#c68642"))
    S.add(pierre(420, 800, 1.5, expr="rire", bras="ouverts", regard=(1, -0.3), pas="marche"))
    S.add(oiseau_(330, 160, 0.6))
    S.add(texte(560, 140, "Un beau matin…", 48, "#2b8a3e", contour="#fff"))
    return S


def p02():
    """Schéma : chaque personnage a son instrument : oiseau-flûte, canard-hautbois, chat-clarinette, grand-père-basson, loup-cors, chasseurs-timbales, Pierre-violons."""
    S = Scene()
    fond(S, "#fff9db")
    S.add(texte(400, 70, "Chacun son instrument", 42, "#e8590c"))
    cases = [
        (140, 200, "l'oiseau", "la flûte"), (400, 200, "le canard", "le hautbois"), (660, 200, "le chat", "la clarinette"),
        (140, 440, "le grand-père", "le basson"), (400, 440, "le loup", "les cors"), (660, 440, "les chasseurs", "les timbales"),
        (400, 680, "Pierre", "les violons"),
    ]
    for k, (x, y, qui, quoi) in enumerate(cases):
        S.add(rect(x - 120, y - 90, 240, 200, "#fff", stroke="#ffe066", stroke_width=4, rx=18))
        if k == 0:
            S.add(oiseau_(x - 50, y + 20, 0.55, ailes="bas"), flute(x + 50, y - 10, 0.55))
        elif k == 1:
            S.add(canard_(x - 50, y + 30, 0.55, nage=False), hautbois(x + 60, y, 0.7))
        elif k == 2:
            S.add(chat_(x - 50, y + 40, 0.6), clarinette(x + 60, y, 0.7))
        elif k == 3:
            S.add(grand_pere(x - 50, y + 60, 0.5), basson(x + 60, y, 0.7))
        elif k == 4:
            S.add(loup_(x - 50, y + 60, 0.45), cor(x + 60, y - 10, 0.7))
        elif k == 5:
            S.add(personne(x - 50, y + 60, 0.45, **CHASSEURS[0]), timbale(x + 60, y, 0.7))
        else:
            S.add(pierre(x - 50, y + 60, 0.55), violon(x + 60, y, 0.75))
        S.add(texte(x, y + 76, qui, 22, "#495057"), texte(x, y + 100, quoi, 22, "#e8590c"))
    S.cachette(740, 790)
    return S


def p03():
    """Plan moyen : au bord de la mare, l'oiseau et le canard se disputent : « Tu ne sais pas voler ! » « Tu ne sais pas nager ! »"""
    S = Scene()
    prairie(S, arbre_=False, mur=False, roseaux=False)
    S.add(canard_(600, 712, 1.4, expr="fache", flip=True))
    S.add(oiseau_(330, 640, 1.1, expr="fache", ailes="haut"))
    S.add(bulle(240, 260, 320, 90, "Tu ne sais pas voler !", 30, pointe=(320, 560)))
    S.add(bulle(600, 400, 340, 90, "Tu ne sais pas nager !", 30, pointe=(580, 620)))
    return S


def p04():
    """Plan moyen : à pas de velours, le chat s'approche ; Pierre crie « Attention ! » et l'oiseau s'envole dans l'arbre."""
    S = Scene()
    prairie(S)
    S.add(chat_(560, 790, 1.4, pose="debout", expr="sourire"))
    S.add(oiseau_(380, 280, 0.7, flip=True))
    S.add(pierre(120, 800, 1.3, expr="surpris", bras="haut", regard=(1, -0.3)))
    S.add(bulle(330, 470, 240, 80, "Attention !", 34, pointe=(180, 560)))
    return S


def p05():
    """Plan moyen : le grand-père, fâché, ramène Pierre : « Et si le loup sortait de la forêt ? »"""
    S = Scene()
    prairie(S, mare_=False, roseaux=False, mur=False)
    S.add(grand_pere(480, 800, 1.75, expr="fache", bras="main", flip=True, regard=(-1, 0.3)))
    S.add(pierre(300, 800, 1.4, expr="triste", bras="main", regard=(1, -0.3)))
    S.add(bulle(500, 140, 440, 110, "La prairie, c'est dangereux !\nEt si le loup sortait ?", 30, pointe=(500, 300)))
    return S


def p06():
    """Plan large : le grand loup gris sort de la forêt ! le chat grimpe dans l'arbre, le canard sort de la mare en criant."""
    S = Scene()
    prairie(S)
    S.add(loup_(560, 560, 1.15, expr="malin", bras="bas", regard=(-1, 0.3)))
    S.add(chat_(420, 320, 0.8, expr="surpris"))
    S.add(canard_(680, 760, 1.0, expr="surpris", nage=False, ailes="haut"))
    S.add(texte(560, 140, "Le loup !", 64, "#495057", contour="#fff"))
    return S


def p07():
    """Plan moyen : le canard file se cacher dans les roseaux ; le loup renifle partout mais ne le trouve pas."""
    S = Scene()
    prairie(S, arbre_=False, mur=False, roseaux=False)
    S.add(loup_(250, 800, 1.5, expr="concentre", bras="bas", regard=(1, 0.5)))
    S.add(canard_(560, 760, 0.9, expr="inquiet", nage=False))
    cache_roseaux(S, 560, 790)
    S.add(texte(560, 140, "Chut… il est caché !", 46, "#2b8a3e", contour="#fff"))
    return S


def p08():
    """Plan large : le loup tourne autour de l'arbre ; sur une branche, le chat ; sur une autre, l'oiseau."""
    S = Scene()
    prairie(S)
    S.add(chat_(300, 330, 0.8, expr="inquiet"))
    S.add(oiseau_(440, 300, 0.6, ailes="bas", flip=True))
    S.add(loup_(420, 800, 1.5, expr="malin", bras="bas", regard=(-0.5, -1)))
    S.add(bulle(600, 400, 220, 80, "Miam…", 36, pointe=(500, 520)))
    return S


def p09():
    """Plan large : Pierre a pris une corde ; il grimpe sur le mur, puis sur la branche ; l'oiseau vole autour du nez du loup."""
    S = Scene()
    prairie(S)
    S.add(pierre(140, 360, 1.0, expr="concentre", bras="tient", regard=(1, 0.3),
                 objet=g([cercle(80, -120, 26, "none", stroke="#c9a24a", stroke_width=6), corde(70, -146, 80, -96, 0)])))
    S.add(loup_(520, 800, 1.45, expr="fache", bras="haut", regard=(0, -1)))
    S.add(oiseau_(520, 360, 0.7))
    for k in range(3):
        S.add(chemin(f"M {460 + k * 30} {420 + k * 10} q 30 -20 60 0", stroke="#fff", sw=4, opacity=0.8))
    S.add(texte(560, 120, "Hop, sur la branche !", 46, "#e03131", contour="#fff"))
    return S


def p10():
    """Gros plan : Pierre fait descendre un nœud coulant et attrape le loup par la queue !"""
    S = Scene()
    prairie(S)
    S.add(pierre(360, 330, 0.9, expr="rire", bras="tient", regard=(0, 1)))
    S.add(loup_(560, 860, 1.7, expr="surpris", bras="haut", regard=(0, -1)))
    S.add(chemin("M 430 214 Q 800 300 712 668", stroke="#c9a24a", sw=6))
    S.add(cercle(712, 690, 22, "none", stroke="#c9a24a", stroke_width=6))
    S.camera(1.05, 420, 500)
    S.dessus(texte(400, 100, "Attrapé !", 70, "#e03131", contour="#fff"))
    return S


def p11():
    """Plan large : les chasseurs sortent de la forêt ; Pierre : « Ne tirez pas ! Emmenons-le au zoo ! »"""
    S = Scene()
    prairie(S, arbre_=False, mur=False, mare_=False, roseaux=False)
    for k, x in enumerate((420, 560, 700)):
        S.add(personne(x, 790, 1.35, expr="surpris", bras="porte", flip=True, regard=(-1, 0), **CHASSEURS[k]))
    S.add(loup_(240, 800, 1.2, expr="triste", bras="bas", regard=(1, 0)))
    S.add(corde(250, 700, 120, 520, 40))
    S.add(pierre(110, 800, 1.35, expr="content", bras="tient", regard=(1, 0)))
    S.add(bulle(420, 160, 440, 110, "Ne tirez pas !\nEmmenons-le au zoo !", 32, pointe=(160, 480)))
    S.cachette(140, 70, "air")
    return S


def p12():
    """Plan large : le cortège vers le zoo : Pierre en tête, le loup tenu par la corde, les chasseurs, le grand-père, le chat et l'oiseau ; le canard sort des roseaux."""
    S = Scene()
    prairie(S, arbre_=False, mur=False, roseaux=False)
    S.add(personne(80, 720, 1.0, expr="rire", bras="porte", **CHASSEURS[0]), personne(170, 730, 1.0, expr="rire", bras="porte", **CHASSEURS[1]))
    S.add(grand_pere(270, 740, 1.15, expr="content", bras="hanches"))
    S.add(loup_(420, 760, 1.0, expr="triste", bras="bas", regard=(1, 0)))
    S.add(corde(450, 640, 560, 600, 30))
    S.add(pierre(590, 770, 1.25, expr="rire", bras="tient", regard=(1, 0)))
    S.add(chat_(360, 790, 0.6, pose="debout"))
    S.add(oiseau_(600, 330, 0.7))
    S.add(canard_(720, 760, 0.8, expr="rire", nage=False, flip=True, ailes="haut"))
    cache_roseaux(S, 760, 800)
    S.add(bulle(620, 180, 300, 90, "Coin ! Me voilà !", 32, pointe=(710, 640)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("oiseau-seul.svg", vignette),
    ("01-la-prairie.svg", p01), ("02-les-instruments.svg", p02), ("03-la-dispute.svg", p03),
    ("04-le-chat.svg", p04), ("05-le-grand-pere.svg", p05), ("06-le-loup.svg", p06),
    ("07-les-roseaux.svg", p07), ("08-autour-de-l-arbre.svg", p08), ("09-la-corde.svg", p09),
    ("10-attrape.svg", p10), ("11-ne-tirez-pas.svg", p11), ("12-le-cortege.svg", p12),
]
