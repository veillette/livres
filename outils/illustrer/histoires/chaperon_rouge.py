"""Le Petit Chaperon rouge — ne pas parler aux inconnus."""
from contes import *

ID = "chaperon-rouge"
MAMAN = dict(coiffure="chignon", cheveux="chatain", peau="claire", habit="#ffa94d", stature="adulte", nez="pointu")
BUCHERON = dict(coiffure="courts", cheveux="roux", barbe="#d9480f", peau="rosee", habit="#2f9e44", robe=False, jambes="#5c3a1e",
                stature="adulte", carrure="ronde", nez="rond")
MERE_GRAND = dict(stature="ancien", nez="long")


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def loup_mere_grand(x, y, s=1.0, **k):
    """Le loup déguisé : bonnet de nuit et chemise à fleurs."""
    k.setdefault("acc", ("bonnet",))
    return perso("loup", x, y, s, habit="#b197fc", motif="pois", couleur_acc="#fcc2d7", **k)


def bucheron(x, y, s=1.0, **k):
    return personne(x, y, s, **{**BUCHERON, **k})


def bois(S, graine=3):
    foret(S, graine=graine)
    S.add(chemin("M 0 760 Q 400 650 800 720 L 800 800 L 0 800 Z", "#f3d9a4"))


def mere_grand_(x, y, s=1.0, **k):
    return mere_grand(x, y, s, **{**MERE_GRAND, **k})


def chambre(S):
    """La chaumière de la mère-grand : murs chaulés, poutres, larges planches."""
    piece(S, "chaumiere", 560)
    S.add(fenetre(560, 100, 170, 150, dehors="#b2f2bb", rideaux="#e64980"))
    S.add(cadre_mur(110, 120))


def armoire(x, y, s=1.0, ouverte=False, dedans=""):
    m = [rect(-110, -380, 220, 380, "#a0522d", rx=10), rect(-120, -400, 240, 30, "#8d5524", rx=8)]
    if ouverte:
        m += [rect(-96, -360, 192, 340, "#343a40", rx=6), dedans,
              poly([(-96, -360), (-150, -340), (-150, -40), (-96, -20)], "#c68642")]
    else:
        m += [rect(-96, -360, 94, 340, "#c68642", rx=6), rect(2, -360, 94, 340, "#c68642", rx=6),
              cercle(-14, -190, 7, OR), cercle(14, -190, 7, OR)]
    return place(m, x, y, s)


def lit_loup(x, y, s=1.0, dormeur=""):
    m = [lit(0, 0, 360, "#e64980", "#f783ac")]
    if dormeur:
        m.append(dormeur)
    m.append(rect(-180, -110, 360, 70, "#f783ac", rx=18))
    for k in range(5):
        m.append(fleur(-140 + k * 70, -60, 0.4, "#fff", tige=0))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    bois(S)
    S.add(loup(620, 760, 1.2, expr="malin", regard=(-1, 0), flip=True))
    S.add(chaperon(330, 790, 1.4, expr="rire", bras="porte", objet=panier(0, -44, 0.8)))
    S.add(fleur(120, 770, 1.0, "#ff8787"), fleur(180, 790, 0.9, "#fcc419"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(panier(200, 250, 2.0))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=3)
    sol(S, 600, "#94d82d")
    S.add(maison(170, 620, 0.9, toit="#e03131"))
    S.add(chaperon(470, 790, 1.5, expr="content", bras="coucou"))
    S.add(fleur(680, 740, 0.9), fleur(740, 760, 0.8, "#cc5de8"))
    return S


def p02():
    S = Scene()
    piece(S, "cuisine", 580)
    S.add(fenetre(80, 110, 160, 150, dehors="#b2f2bb", rideaux="#fa5252"))
    hx, hy = mains_personne(0, 0, 1, "donne", stature="adulte")[1]
    S.add(personne(250, 790, 1.2, expr="sourire", bras="donne", regard=(1, 0), objet=panier(hx, hy + 32, 0.7), **MAMAN))
    S.add(chaperon(520, 790, 1.25, expr="content"))
    S.add(bulle(460, 150, 420, 100, "Porte cette galette\nà ta mère-grand !", 32, pointe=(300, 470)))
    return S


def p03():
    S = Scene()
    bois(S, graine=5)
    S.add(chaperon(250, 780, 1.3, expr="sourire", bras="porte", objet=panier(0, -44, 0.7)))
    S.add(loup(560, 780, 1.35, expr="malin", bras="salut", flip=True))
    S.add(bulle(560, 150, 380, 90, "Où vas-tu, petite ?", 36, pointe=(560, 420)))
    return S


def p04():
    S = Scene()
    bois(S, graine=8)
    for k in range(7):
        S.add(fleur(60 + k * 70, 720 + (k % 2) * 30, 0.9, ["#ff8787", "#fcc419", "#cc5de8", "#fff"][k % 4]))
    S.add(chaperon(220, 790, 1.2, expr="content", bras="donne2", objet=fleur(100, -80, 0.7, "#ff8787")))
    S.add(loup(620, 700, 1.0, expr="malin", bras="course", flip=True))
    S.add(mouvement(720, 580, 1.2, rot=180))
    return S


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff0f6")
    for xx in (60, 740):
        S.add(sapin(xx, 610, 1.2))
    sol(S, 600, "#94d82d")
    S.add(maison(420, 640, 1.3, mur="#fff0f6", toit="#c2255c"))
    S.add(loup(200, 790, 1.3, expr="malin", bras="montre", regard=(1, 0)))
    S.add(texte(440, 150, "Toc, toc !", 64, "#862e9c", contour="#fff"))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(fenetre(560, 90, 170, 150, dehors="#b2f2bb", rideaux="#e64980", contenu=place(loup(0, 0, 0.6, expr="malin"), 640, 260)))
    S.add(armoire(250, 790, 1.1, ouverte=True, dedans=mere_grand_(0, -40, 1.05, expr="surpris", bras="bouche", acc=("lunettes", "bonnet_nuit"), couleur_acc="#fcc2d7")))
    S.add(texte(560, 330, "Vite !", 60, "#c2255c", contour="#fff"))
    return S


def p07():
    S = Scene()
    chambre(S)
    S.add(armoire(120, 790, 0.9))
    S.add(lit_loup(500, 790, 1.2, dormeur=loup_mere_grand(-100, -60, 0.9, expr="malin", regard=(1, 0))))
    return S


def question(S, partie, pose="bas", rep="", cadre=None):
    """Chaperon devant le lit du loup ; cadre = (zoom, cx, cy) pour se
    rapprocher à chaque question, jusqu'au gros plan sur les yeux."""
    chambre(S)
    S.add(lit_loup(560, 790, 1.2, dormeur=loup_mere_grand(-100, -60, 0.9, expr="malin" if partie != "dents" else "rire", bras="bas", regard=(-1, 0))))
    S.add(chaperon(170, 790, 1.2, expr="surpris", bras=pose, regard=(1, 0)))
    if partie == "oreilles":
        S.add(eclat(386, 470, 0.8, "#fa5252"), eclat(494, 470, 0.8, "#fa5252"))
    elif partie == "yeux":
        S.add(eclat(420, 554, 0.6, "#fcc419"), eclat(460, 554, 0.6, "#fcc419"))
    if cadre:
        S.camera(*cadre)
    if rep:
        # la pointe de la bulle vise la bouche du loup, même en gros plan
        S.dessus(bulle(560, 150, 420, 100, rep, 32, pointe=S.vers_page(440, 590)))


def p08():
    S = Scene()
    question(S, "oreilles", "porte", "C'est pour mieux\nt'écouter, mon enfant !", cadre=(1.3, 380, 560))
    return S


def p09():
    S = Scene()
    question(S, "yeux", "joues", "C'est pour mieux\nte voir, mon enfant !", cadre=(1.9, 400, 560))
    return S


def p10():
    S = Scene()
    chambre(S)
    S.add(lit_loup(600, 790, 1.1))
    S.add(loup_mere_grand(470, 700, 1.3, expr="furieux", bras="haut", acc=()))
    S.add(chaperon(160, 790, 1.2, expr="oups", bras="haut"))
    S.add(bulle(400, 150, 420, 100, "C'est pour mieux\nte manger !", 36, pointe=(470, 420)))
    return S


def p11():
    S = Scene()
    bois(S, graine=12)
    S.add(maison(160, 620, 0.8, mur="#fff0f6", toit="#c2255c"))
    S.add(bulle(180, 180, 280, 90, "Au secours !", 38, pointe=(150, 460)))
    hx, hy = mains_personne(0, 0, 1, "tient", stature="adulte", carrure="ronde")[1]
    S.add(bucheron(560, 790, 1.2, expr="surpris", bras="tient", objet=hache(hx, hy, 0.9, rot=10), regard=(-1, 0)))
    return S


def p12():
    S = Scene()
    chambre(S)
    S.add(loup(620, 420, 1.0, expr="oups", bras="haut", rot=20))
    hx, hy = mains_personne(0, 0, 1, "tient", stature="adulte", carrure="ronde")[1]
    S.add(bucheron(250, 790, 1.2, expr="furieux", bras="tient", objet=hache(hx, hy, 0.9, rot=10)))
    S.add(chaperon(460, 790, 1.0, expr="surpris", bras="joues"))
    S.add(mouvement(560, 360, 1.3))
    return S


def p13():
    S = Scene()
    chambre(S)
    S.add(armoire(150, 790, 0.9, ouverte=True))
    S.add(mere_grand_(340, 790, 1.1, expr="rire", bras="ouverts"))
    S.add(chaperon(560, 790, 1.2, expr="rire", bras="haut"))
    S.add(texte(450, 360, "Merci !", 56, "#c2255c", contour="#fff"))
    return S


def p14():
    S = Scene()
    chambre(S)
    S.add(table(400, 760, 360, 140, nappe="#fff"))
    S.add(ellipse(400, 604, 70, 22, "#e8a15c"), rect(470, 560, 34, 44, "#a5d8ff", rx=6))
    S.add(mere_grand_(170, 790, 1.0, expr="rire", regard=(1, 0)), bucheron(640, 790, 1.05, expr="rire", regard=(-1, 0)))
    S.add(chaperon(400, 800, 1.0, expr="miam", bras="bouche"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("panier-seul.svg", vignette),
    ("01-le-chaperon.svg", p01), ("02-la-galette.svg", p02), ("03-le-loup.svg", p03), ("04-les-fleurs.svg", p04),
    ("05-toc-toc.svg", p05), ("06-l-armoire.svg", p06), ("07-dans-le-lit.svg", p07), ("08-grandes-oreilles.svg", p08),
    ("09-grands-yeux.svg", p09), ("10-grandes-dents.svg", p10), ("11-au-secours.svg", p11), ("12-le-bucheron.svg", p12),
    ("13-merci.svg", p13), ("14-la-galette.svg", p14),
]
