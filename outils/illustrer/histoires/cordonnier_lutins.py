"""Le cordonnier et les lutins — dire merci avec un cadeau."""
from contes import *

ID = "cordonnier-lutins"
CORDONNIER = dict(coiffure="chauve_cote", cheveux="gris", barbe="#ced4da", peau="rosee", habit="#1864ab", robe=False, jambes="#495057", acc=("lunettes",))
FEMME = dict(coiffure="chignon", cheveux="gris", peau="rosee", habit="#c2255c")
CLIENTE = dict(coiffure="boucles", cheveux="noir", peau="brune", habit="#fcc419", acc=("fleur",), couleur_acc="#fa5252")


def cordonnier(x, y, s=1.2, **k):
    return personne(x, y, s, **{**CORDONNIER, **k})


def femme(x, y, s=1.15, **k):
    return personne(x, y, s, **{**FEMME, **k})


def lutin_(x, y, s=0.45, habille=False, **k):
    if habille:
        return lutin(x, y, s, bonnet="#e03131", habit="#2f9e44", jambes="#1864ab", **k)
    d = dict(coiffure="herisses", cheveux="brun", habit="#ced4da", robe=False, jambes="#ced4da", chaussures="#fbd9bd", peau="rosee")
    d.update(k)
    corps = personne(0, 0, 1.0, **d)
    trous = [cercle(-14, -80, 6, "#fbd9bd"), cercle(16, -60, 5, "#fbd9bd"), cercle(-10, -30, 5, "#fbd9bd")]
    return place([corps] + trous, x, y, s)


def atelier(S, nuit_=False):
    interieur(S, "#ffe8cc", "#a0693a", 560, papier="#ffd8a8")
    S.add(fenetre(560, 90, 170, 150, nuit_=nuit_, dehors="#1c2a52" if nuit_ else "#a5d8ff", rideaux="#e8590c"))
    S.add(etagere(170, 200, 240, objets=g([chaussure(80, 200, 0.5, "#c92a2a"), chaussure(160, 200, 0.5, "#1c7ed6"), chaussure(240, 200, 0.5, "#2f9e44")])))
    if nuit_:
        S.add(rect(0, 0, 800, 800, "#1c2a52", opacity=0.35))


def etabli_(S, x=420, y=790, contenu=""):
    S.add(etabli(x, y, 380))
    if contenu:
        S.add(contenu)


def cuir(x, y, s=1.0):
    return place([chemin("M -60 -10 Q -70 -40 -30 -44 Q 20 -52 60 -30 Q 70 -6 40 0 Q -10 8 -60 -10 Z", "#a0693a"),
                  chemin("M -40 -24 Q 0 -36 40 -20", stroke="#fff4e6", sw=2, stroke_dasharray="6 6")], x, y, s)


def paire(x, y, s=1.0, couleur="#c92a2a"):
    return g([chaussure(x - 34 * s, y, s, couleur), chaussure(x + 34 * s, y + 6 * s, s, couleur)])


def couverture():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S, 400, 800)
    S.add(paire(400, 650, 1.1))
    S.add(lutin_(250, 650, 0.8, habille=True, expr="rire", bras="haut"), lutin_(560, 650, 0.8, habille=True, expr="rire", bras="tient", objet=marteau(68, -146, 0.7, rot=-20)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(paire(200, 220, 1.4))
    return S


def p01():
    S = Scene()
    atelier(S)
    etabli_(S)
    S.add(cuir(420, 648, 1.2))
    S.add(cordonnier(180, 790, expr="triste"), femme(660, 790, expr="inquiet"))
    return S


def p02():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S)
    S.add(cuir(420, 648, 1.2))
    S.add(bougie(560, 648, 1.0))
    S.add(cordonnier(180, 790, expr="baille", bras="etire", acc=("lunettes", "bonnet_nuit"), couleur_acc="#74c0fc"))
    S.add(bulle(420, 150, 460, 100, "Je coudrai les souliers\ndemain matin…", 32, pointe=(200, 470)))
    return S


def p03():
    S = Scene()
    atelier(S)
    etabli_(S)
    S.add(paire(420, 648, 1.0))
    S.add(etincelles(420, 580, 1.0, graine=3))
    S.add(cordonnier(180, 790, expr="bouche_bee", bras="joues"))
    S.add(texte(440, 440, "Surprise !", 60, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    atelier(S)
    etabli_(S, 520)
    S.add(personne(260, 790, 1.2, expr="rire", bras="donne", objet=paire(120, -110, 0.6), **CLIENTE))
    S.add(cordonnier(620, 790, expr="rire", bras="ouverts"))
    S.add(bulle(360, 150, 420, 100, "Oh, quels jolis\nsouliers !", 36, pointe=(280, 470)))
    return S


def p05():
    S = Scene()
    atelier(S)
    etabli_(S)
    S.add(paire(340, 648, 0.9, "#1c7ed6"), paire(500, 648, 0.9, "#2f9e44"))
    S.add(cordonnier(150, 790, expr="rire", bras="haut"), femme(680, 790, expr="rire", bras="joues"))
    S.add(texte(420, 440, "Deux paires !", 56, "#1c7ed6", contour="#fff"))
    return S


def p06():
    S = Scene()
    atelier(S)
    for k, (x, d) in enumerate(((120, CLIENTE), (300, dict(coiffure="courts", cheveux="roux", peau="claire", habit="#51cf66", robe=False, jambes="#495057")),
                                (470, dict(coiffure="queue", cheveux="blond", peau="claire", habit="#cc5de8")),
                                (640, dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="doree", habit="#e8590c", robe=False, jambes="#343a40")))):
        S.add(personne(x, 790, 1.05, expr="rire", bras="porte", objet=chaussure(0, -60, 0.7, ["#c92a2a", "#1c7ed6", "#2f9e44", "#fcc419"][k]), **d))
    S.add(texte(400, 300, "Quelle boutique !", 56, "#e8590c", contour="#fff"))
    S.cachette(640, 254)
    return S


def p07():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S, 520)
    S.add(cuir(520, 648, 1.2))
    S.add(rect(40, 260, 200, 540, "#e64980", rx=6), rect(40, 250, 210, 20, "#adb5bd", rx=8))
    S.add(cordonnier(140, 790, 1.0, expr="malin", bras="bouche"), femme(220, 790, 0.95, expr="malin", bras="bouche"))
    S.add(rect(40, 260, 90, 540, "#e64980", rx=6))
    S.add(bulle(460, 150, 480, 100, "Cachons-nous pour voir\nqui nous aide !", 32, pointe=(220, 470)))
    return S


def p08():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S)
    S.add(cuir(330, 648, 0.9), chaussure(500, 650, 0.8, finie=False))
    S.add(lutin_(270, 650, 0.7, expr="concentre", bras="tient", objet=marteau(68, -146, 0.8, rot=-20)))
    S.add(lutin_(570, 650, 0.7, expr="chante", bras="ouverts"))
    S.add(texte(420, 420, "Tap, tap, tap !", 54, "#fcc419", contour="#1c2a52"))
    S.add(notes(620, 440, 0.7, "#fcc419"))
    return S


def p09():
    S = Scene()
    atelier(S)
    etabli_(S)
    S.add(paire(420, 648, 0.9, "#2f9e44"))
    S.add(femme(560, 790, expr="triste", bras="joues"), cordonnier(300, 790, expr="inquiet"))
    S.add(place(g([lutin_(0, 0, 0.3, expr="triste", bras="course"), lutin_(60, 0, 0.3, expr="triste", bras="course")]), 610, 250))
    S.add(bulle(420, 120, 480, 90, "Les pauvres, ils ont si froid !", 30, pointe=(540, 480)))
    return S


def p10():
    S = Scene()
    atelier(S, nuit_=True)
    S.add(lampe(620, 560, 1.0))
    S.add(table(400, 790, 360, 120, nappe="#fff"))
    for k in range(2):
        S.add(place(g([rect(-26, -36, 52, 50, "#2f9e44", rx=8), rect(-22, 14, 18, 30, "#1864ab", rx=4), rect(4, 14, 18, 30, "#1864ab", rx=4)]), 330 + k * 80, 610))
        S.add(poly([(470 + k * 50 - 18, 640), (470 + k * 50, 600), (470 + k * 50 + 18, 640)], "#e03131"))
    S.add(chaussure(560, 652, 0.3, "#fcc419"), chaussure(590, 652, 0.3, "#fcc419"))
    S.add(femme(150, 790, expr="concentre", bras="porte"), cordonnier(680, 790, expr="content", bras="tient", objet=marteau(68, -146, 0.7, rot=-20)))
    return S


def p11():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S)
    for k in range(2):
        S.add(place(g([rect(-26, -36, 52, 50, "#2f9e44", rx=8), rect(-22, 14, 18, 30, "#1864ab", rx=4), rect(4, 14, 18, 30, "#1864ab", rx=4)]), 340 + k * 80, 614))
        S.add(poly([(480 + k * 50 - 18, 648), (480 + k * 50, 608), (480 + k * 50 + 18, 648)], "#e03131"))
    S.add(g([cercle(420, 540, 70, "#fff3bf", opacity=0.3)]), coeur(420, 520, 1.0))
    S.add(rect(40, 260, 200, 540, "#e64980", rx=6), rect(40, 250, 210, 20, "#adb5bd", rx=8))
    return S


def p12():
    S = Scene()
    atelier(S, nuit_=True)
    etabli_(S)
    S.add(lutin_(320, 650, 0.75, habille=True, expr="rire", bras="danse"), lutin_(520, 650, 0.75, habille=True, expr="rire", bras="ouverts"))
    S.add(notes(420, 380, 0.9, "#fcc419"))
    S.add(texte(420, 300, "Que nous sommes beaux !", 44, "#fcc419", contour="#1c2a52"))
    return S


def p13():
    S = Scene()
    atelier(S)
    S.add(fenetre(560, 90, 170, 150, dehors="#ffd8a8", rideaux="#e8590c", contenu=g([place(lutin_(0, 0, 0.3, habille=True, expr="rire", bras="salut"), 610, 230),
                                                                                       place(lutin_(0, 0, 0.3, habille=True, expr="rire", bras="salut"), 680, 230)])))
    etabli_(S, 380)
    S.add(paire(380, 648, 0.9, "#fcc419"))
    S.add(cordonnier(160, 790, expr="rire", bras="coucou"), femme(620, 790, expr="rire", bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("souliers-seuls.svg", vignette),
    ("01-un-morceau-de-cuir.svg", p01), ("02-demain-matin.svg", p02), ("03-surprise.svg", p03), ("04-la-cliente.svg", p04),
    ("05-deux-paires.svg", p05), ("06-la-boutique.svg", p06), ("07-caches.svg", p07), ("08-les-lutins.svg", p08),
    ("09-ils-ont-froid.svg", p09), ("10-les-habits.svg", p10), ("11-les-cadeaux.svg", p11), ("12-que-nous-sommes-beaux.svg", p12),
    ("13-au-revoir.svg", p13),
]
