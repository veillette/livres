"""Anansi et la boîte à histoires — un conte ashanti du Ghana.

Autrefois, toutes les histoires appartenaient à Nyamé, le dieu du ciel, qui
les gardait dans un coffre. Anansi, la petite araignée, monte au ciel sur
son fil pour les acheter. Le prix : Onini le python, Osebo le léopard, les
frelons Mmoboro et Mmoatia, la petite fée de la forêt. Tout le monde rit :
qui pourrait les attraper ? Mais Anansi est malin. Il demande au python de
se mesurer contre une branche et l'y attache ; il aide le léopard tombé
dans un trou… avec un fil de toile ; il fait croire aux frelons qu'il pleut
et les abrite dans sa calebasse ; et une poupée collante attrape la petite
fée gourmande. Nyamé, émerveillé, lui donne les histoires, qu'Anansi
répand dans le monde entier. Ici, personne n'est blessé.

Plans : 1 large (les soirs sans histoires) · 2 moyen (Nyamé) · 3 moyen (le
python) · 4 moyen (le léopard) · 5 moyen (les frelons) · 6 moyen (la petite
fée) · 7 large (le coffre) · 8 large (les histoires s'envolent) · 9 moyen
(au coin du feu).
"""
from contes import *
from base import _assombrir
from animaux import abeille

ID = "anansi-histoires"

KENTE = ("#fab005", "#2b8a3e", "#e03131", "#212529")
NYAME = dict(stature="adulte", peau="foncee", cheveux="blanc", coiffure="chauve_cote", habit="#fab005", robe=True, barbe="#f8f9fa",
             acc=("couronne",), carrure="ronde", nez="rond")
MAMIE = dict(stature="ancien", peau="foncee", cheveux="blanc", coiffure="chignon", habit="#e8590c", robe=True, nez="rond")
ENFANTS = [dict(peau="brune", cheveux="noir", coiffure="afro", habit="#40c057", robe=False, jambes="#495057"),
           dict(peau="foncee", cheveux="noir", coiffure="couettes", habit="#fab005", robe=True),
           dict(peau="brune", cheveux="noir", coiffure="courts", habit="#4dabf7", robe=False, jambes="#495057")]


def kente(x, y, w, h):
    """Bandes de tissu kente."""
    m = []
    for k in range(int(w // 16)):
        m.append(rect(x + k * 16, y, 16, h, KENTE[k % 4]))
        for j in range(int(h // 20)):
            m.append(rect(x + k * 16 + 3, y + j * 20 + 6, 10, 6, KENTE[(k + j + 1) % 4], opacity=0.9))
    return g(m)


def anansi(x, y, s=1.0, expr="malin", flip=False, rot=0, chapeau=True, couleur="#8d5524"):
    """Anansi, la petite araignée malicieuse, avec son petit bonnet kente ; (x, y) = centre du corps."""
    c = couleur
    m = []
    for sgn in (-1, 1):
        for k, (a, b) in enumerate(((-40, -36), (-50, -6), (-48, 22), (-36, 46))):
            m.append(chemin(f"M {sgn * 20} {b * 0.4} Q {sgn * (60 + k * 6)} {b - 20} {sgn * (78 + k * 4)} {b + 26}", stroke=_assombrir(c, 0.75), sw=7))
    m += [ellipse(0, 26, 46, 40, volume(c, 0.3, 0.8)), cercle(0, -30, 34, volume(c, 0.3, 0.85))]
    if chapeau:
        cid = uid("k")
        m += [el("clipPath", chemin("M -30 -50 Q 0 -96 30 -50 Z", "#000"), id=cid), g(kente(-30, -96, 64, 50), clip_path=f"url(#{cid})"),
              rect(-32, -54, 64, 8, "#fab005", rx=3)]
    yeux = "heureux" if expr in ("content", "rire") else "normal"
    m += [cercle(-12, -32, 9, "#fff"), cercle(12, -32, 9, "#fff"), oeil(-12, -32, yeux, (0.3, 0), taille=0.55), oeil(12, -32, yeux, (0.3, 0), taille=0.55)]
    if expr == "malin":
        m += [chemin("M -10 -14 Q 2 -6 14 -16", stroke=ENCRE, sw=3), trait(-20, -46, -4, -42, ENCRE, 3)]
    elif expr == "surpris":
        m.append(ellipse(0, -12, 5, 6, ENCRE))
    else:
        m.append(chemin("M -10 -16 Q 0 -6 10 -16", stroke=ENCRE, sw=3))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 90 * s, y - 100 * s, x + 90 * s, y + 80 * s)


def python(x, y, s=1.0, droit=False, attache=False):
    """Onini, le grand python vert ; droit : allongé tout du long contre la branche."""
    c = "#5c940d"
    if droit:
        corps = "M -320 0 L 300 0"
    else:
        corps = "M -260 20 Q -200 -60 -120 0 Q -40 60 40 0 Q 120 -60 200 0"
    m = [chemin(corps, stroke=c, sw=40), chemin(corps, stroke="#d8f5a2", sw=12, opacity=0.6, stroke_dasharray="14 18")]
    tx = 300 if droit else 200
    m += [ellipse(tx + 20, 0, 40, 26, volume(c, 0.3, 0.8)), cercle(tx + 30, -10, 7, "#fff"), cercle(tx + 32, -10, 3.5, ENCRE),
          chemin(f"M {tx + 56} 4 l 16 -4 l -4 6 l 8 4", stroke="#e03131", sw=2)]
    if attache:
        for k in range(6):
            m.append(trait(-280 + k * 110, -30, -280 + k * 110, 30, "#f8f9fa", 3))
    return place(m, x, y, s)


def leopard(x, y, s=1.0, **k):
    corps = perso("chat", x, y, s, couleur="#f59f00", **k)
    r = random.Random(3)
    taches = [cercle(x + r.uniform(-60, 60) * s, y + r.uniform(-260, -30) * s, r.uniform(6, 10) * s, "#5c3d24", opacity=0.85) for _ in range(20)]
    return corps + g(taches)


def calebasse(x, y, s=1.0, ouverte=False):
    m = [cercle(0, 0, 60, volume("#e9b872", 0.3, 0.8)), cercle(0, -66, 26, volume("#e9b872", 0.3, 0.8)), chemin("M -40 -10 Q 0 10 40 -10", stroke="#c9a24a", sw=4)]
    if ouverte:
        m.append(ellipse(0, -90, 16, 6, "#5c3d24"))
    else:
        m.append(rect(-14, -100, 28, 18, "#a0693a", rx=6))
    return place(m, x, y, s)


def poupee_gomme(x, y, s=1.0):
    m = [ellipse(0, -60, 44, 60, volume("#495057", 0.2, 0.7)), cercle(0, -140, 32, volume("#495057", 0.2, 0.7)),
         cercle(-10, -146, 4, "#fff"), cercle(10, -146, 4, "#fff"), chemin("M -8 -128 Q 0 -122 8 -128", stroke="#fff", sw=2),
         ellipse(70, -20, 50, 14, "#fff", stroke="#dee2e6", stroke_width=2), ellipse(70, -28, 40, 14, "#ffe066")]
    for k in range(4):
        m.append(cercle(-30 + k * 20, -40 + (k % 2) * 30, 3, "#fff", opacity=0.5))
    return place(m, x, y, s)


def coffre_histoires(x, y, s=1.0, ouvert=False):
    m = [rect(-90, -80, 180, 80, volume("#a0693a", 0.3, 0.8), rx=8), rect(-90, -40, 180, 12, OR)]
    if ouvert:
        m += [poly([(-90, -80), (90, -80), (100, -160), (-80, -150)], volume("#8d5524", 0.3, 0.8)), ellipse(0, -80, 80, 14, "#fff3bf"),
              cercle(0, -90, 60, radial([(0, "#fff3bf", 0.9), (1, "#fff3bf", 0)]))]
    else:
        m += [chemin("M -96 -80 Q 0 -130 96 -80 Z", volume("#8d5524", 0.3, 0.8)), rect(-12, -60, 24, 24, OR, rx=4)]
    return place(m, x, y, s)


def histoire_volante(x, y, s=1.0, couleur="#ffd43b", rot=0):
    """Une histoire qui s'envole : un petit livre ouvert aux pages battantes."""
    m = [chemin("M 0 0 Q -30 -20 -60 -6 L -60 30 Q -30 16 0 36 Z", "#fff", stroke=couleur, sw=4),
         chemin("M 0 0 Q 30 -20 60 -6 L 60 30 Q 30 16 0 36 Z", "#fff", stroke=couleur, sw=4)]
    for k in range(3):
        m.append(trait(-46, 4 + k * 8, -12, 10 + k * 8, "#ced4da", 2))
        m.append(trait(12, 10 + k * 8, 46, 4 + k * 8, "#ced4da", 2))
    return place(m, x, y, s, rot=rot)


def feu(x, y, s=1.0):
    """Un petit feu de bois, au sol ; (x, y) = sous les bûches."""
    return place([ellipse(0, 0, 80, 14, "#495057"), trait(-60, -4, 60, -16, "#8d5524", 12), trait(-60, -16, 60, -4, "#a0693a", 12),
                  chemin("M -40 -10 Q -20 -100 0 -130 Q 20 -80 40 -10 Z", "#ff922b"), chemin("M -20 -10 Q -5 -70 5 -90 Q 20 -60 25 -10 Z", "#ffd43b")], x, y, s)


def savane(S, horizon=520, soir=False, nuit_=False):
    if nuit_:
        nuit(S, "#1c2a52", "#4c5b9a")
    else:
        ciel(S, "#ffa94d" if soir else "#74c0fc", "#fff4e6")
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#e9b872" if not nuit_ else "#8d6e4a")))
    for x, sc in ((90, 1.0), (700, 1.2)):
        S.add(place([rect(-24, -260, 48, 260, cylindre("#8d5524", 0.3, 0.75)), cercle(0, -300, 110, volume("#2f9e44", 0.35, 0.8)),
                     cercle(-80, -260, 70, volume("#40c057", 0.35, 0.8)), cercle(80, -260, 70, volume("#40c057", 0.35, 0.8))], x, horizon + 40, sc))


def ciel_nyame(S):
    ciel(S, "#4263eb", "#a5d8ff")
    for x, y, sc in ((140, 650, 1.6), (420, 700, 2.0), (690, 640, 1.6), (300, 180, 0.8), (620, 150, 0.7)):
        S.add(nuage(x, y, sc))


def trone_nyame(S, x=560, y=700, s=1.0, expr="rire", bras="ouverts"):
    S.add(place([rect(-120, -360, 240, 360, volume("#fab005", 0.3, 0.8), rx=30)], x, y - 40, s))
    S.add(personne(x, y, 1.9 * s, expr=expr, bras=bras, tenue=kente(-34, -110, 68, 70), flip=True, regard=(-1, 0.3), **NYAME))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    savane(S, 560, soir=True)
    S.add(coffre_histoires(400, 760, 1.5, ouvert=True))
    for k, (x, y, c, r) in enumerate(((260, 300, "#fab005", -20), (420, 220, "#e03131", 10), (560, 320, "#2b8a3e", 20), (340, 420, "#4dabf7", -10))):
        S.add(histoire_volante(x, y, 0.9, c, r))
    S.add(trait(640, 0, 640, 520, "#f8f9fa", 2))
    S.add(anansi(640, 560, 1.4, expr="rire"))
    S.cachette(60, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trait(200, 0, 200, 110, "#adb5bd", 2))
    S.add(anansi(200, 160, 1.0, expr="malin"))
    return S


def p01():
    """Plan large : autrefois, sur la Terre, il n'y avait pas d'histoires : le soir, autour du feu, tout le monde s'ennuie."""
    S = Scene()
    savane(S, 560, nuit_=True)
    S.add(lune(640, 130, 40))
    etoiles(S, 30, graine=1, zone=(0, 0, 800, 400))
    S.add(feu(400, 770))
    S.lumiere(400, 720, 260, "#ffa94d", 0.6)
    for k, (x, f) in enumerate(((200, False), (600, True), (300, False))):
        S.add(personne(x, 800 if k < 2 else 790, 1.3, expr="triste" if k != 2 else "baille", bras="joues" if k == 0 else "bas", flip=f, **ENFANTS[k]))
    S.add(texte(400, 300, "Pas une seule histoire…", 44, "#fff3bf", contour="#1c2a52"))
    return S


def p02():
    """Plan moyen : Anansi monte au ciel sur son fil ; sur son trône, Nyamé, le dieu du ciel, annonce le prix des histoires."""
    S = Scene()
    ciel_nyame(S)
    trone_nyame(S, 600, 760, 1.0, expr="rire", bras="ouverts")
    S.add(coffre_histoires(400, 740, 0.9))
    S.add(trait(170, 0, 170, 420, "#f8f9fa", 2))
    S.add(anansi(170, 480, 1.2, expr="surpris"))
    S.add(bulle(360, 150, 560, 130, "Apporte-moi Onini le python, Osebo le léopard,\nles frelons Mmoboro et Mmoatia la petite fée.\nAlors, les histoires seront à toi !", 24,
                pointe=(520, 320)))
    S.cachette(70, 620, "air")
    return S


def p03():
    """Plan moyen : « Il est plus long que cette branche ! » « Non ! » Le python s'allonge contre la branche… et Anansi l'y attache."""
    S = Scene()
    savane(S, 560)
    S.add(rect(60, 590, 680, 22, "#a0693a", rx=10))
    for k in range(6):
        S.add(ellipse(120 + k * 110, 584, 50, 14, "#40c057", rot=-20))
    S.add(python(390, 560, 1.0, droit=True, attache=True))
    S.add(anansi(160, 720, 1.0, expr="malin"))
    S.add(anansi(640, 720, 0.85, expr="content", chapeau=False, couleur="#a0693a"))
    S.add(bulle(400, 150, 460, 110, "« Mesure-moi, tu verras ! »\nOnini s'allonge tout du long…", 28, pointe=(560, 520)))
    return S


def p04():
    """Plan moyen : le léopard est tombé dans un trou caché sous les feuilles ; Anansi lui lance un fil… et l'enroule dans sa toile."""
    S = Scene()
    savane(S, 520)
    S.add(ellipse(400, 700, 220, 60, "#5c3d24"), ellipse(400, 690, 200, 46, "#3b2a1a"))
    S.add(leopard(400, 760, 1.1, expr="surpris", bras="haut", regard=(0, -1)))
    S.add(ellipse(400, 760, 220, 40, terrain("#e9b872")))
    for k in range(10):
        S.add(trait(300 + k * 22, 420, 320 + k * 18, 640, "#f8f9fa", 2, opacity=0.8))
    S.add(anansi(400, 360, 1.1, expr="malin"))
    S.add(bulle(620, 160, 300, 90, "Je t'aide à sortir…", 30, pointe=(470, 330)))
    return S


def p05():
    """Plan moyen : Anansi arrose le nid et crie « Il pleut ! » ; les frelons se réfugient dans sa calebasse, qu'il referme."""
    S = Scene()
    savane(S, 520)
    S.add(ellipse(160, 300, 60, 80, volume("#adb5bd", 0.3, 0.8)), trait(160, 220, 160, 180, "#8d5524", 6))
    for k in range(8):
        S.add(abeille(260 + k * 50, 380 + (k % 3) * 40, 0.4, flip=True, marque="#212529"))
    S.add(calebasse(640, 760, 1.2, ouverte=True))
    S.add(anansi(420, 720, 1.1, expr="rire"))
    for k in range(10):
        S.add(goutte(120 + k * 22, 420 + (k % 3) * 30, 0.4))
    S.add(bulle(420, 140, 460, 90, "Il pleut ! Abritez-vous ici !", 32, pointe=(560, 560)))
    return S


def p06():
    """Plan moyen : sous l'arbre, une poupée collante et un bol d'igname ; la petite fée gourmande s'y colle : « Lâche-moi ! »"""
    S = Scene()
    savane(S, 520)
    S.add(poupee_gomme(360, 790, 1.4))
    S.add(personne(530, 790, 0.95, stature="petit", peau="foncee", cheveux="noir", coiffure="afro", habit="#69db7c", robe=True,
                   ailes="#d3f9d8", expr="fache", bras="tend", flip=True, regard=(-1, 0)))
    S.add(anansi(700, 400, 0.9, expr="malin"), trait(700, 0, 700, 340, "#f8f9fa", 2))
    S.add(bulle(560, 150, 260, 90, "Lâche-moi !", 36, pointe=(540, 500)))
    return S


def p07():
    """Plan large : Anansi remonte au ciel avec le python, le léopard, les frelons et la fée ; Nyamé, émerveillé, lui donne le coffre."""
    S = Scene()
    ciel_nyame(S)
    trone_nyame(S, 640, 760, 0.95, expr="rire", bras="applaudit")
    S.add(python(220, 560, 0.5, attache=True), leopard(160, 720, 0.6, expr="triste"), calebasse(320, 740, 0.6))
    S.add(personne(80, 740, 0.6, stature="petit", peau="foncee", cheveux="noir", coiffure="afro", habit="#69db7c", robe=True, ailes="#d3f9d8",
                   expr="triste"))
    S.add(coffre_histoires(450, 760, 0.9))
    S.add(anansi(450, 560, 1.0, expr="rire"))
    S.add(bulle(380, 150, 480, 110, "Bravo, Anansi ! Désormais, ce seront\nles histoires d'Anansi !", 26, pointe=(600, 330)))
    S.cachette(70, 520, "air")
    return S


def p08():
    """Plan large : Anansi ouvre le coffre : les histoires s'envolent comme des oiseaux, partout dans le monde."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff3bf")
    S.add(chemin("M -100 800 Q 400 560 900 800 Z", "#e9b872"))
    S.add(coffre_histoires(400, 760, 1.6, ouvert=True))
    r = random.Random(8)
    for k in range(11):
        S.add(histoire_volante(r.uniform(80, 720), r.uniform(100, 520), r.uniform(0.6, 1.0), KENTE[k % 3] if k % 4 != 3 else "#4dabf7", r.uniform(-30, 30)))
    S.add(anansi(600, 680, 1.1, expr="rire"))
    S.add(texte(400, 90, "Les histoires s'envolent !", 44, "#e8590c", contour="#fff"))
    S.cachette(70, 610, "air")
    return S


def p09():
    """Plan moyen : ce soir, autour du feu, une grand-mère raconte : « Il était une fois Anansi… » ; les enfants écoutent."""
    S = Scene()
    savane(S, 560, nuit_=True)
    etoiles(S, 30, graine=9, zone=(0, 0, 800, 400))
    S.add(feu(400, 770))
    S.lumiere(400, 720, 280, "#ffa94d", 0.7)
    S.add(personne(600, 800, 1.6, expr="content", bras="ouverts", flip=True, regard=(-1, 0), **MAMIE))
    S.add(personne(160, 800, 1.25, expr="bouche_bee", bras="joues", regard=(1, 0), **ENFANTS[0]),
          personne(280, 800, 1.2, expr="rire", bras="bas", regard=(1, 0), **ENFANTS[1]))
    S.add(anansi(560, 330, 0.6, expr="malin"), trait(560, 0, 560, 290, "#f8f9fa", 2))
    S.add(bulle(330, 170, 380, 90, "Il était une fois Anansi…", 30, pointe=(560, 420)))
    S.cachette(190, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("anansi-seul.svg", vignette),
    ("01-sans-histoires.svg", p01), ("02-nyame.svg", p02), ("03-le-python.svg", p03),
    ("04-le-leopard.svg", p04), ("05-les-frelons.svg", p05), ("06-la-petite-fee.svg", p06),
    ("07-le-coffre.svg", p07), ("08-les-histoires-s-envolent.svg", p08), ("09-au-coin-du-feu.svg", p09),
]
