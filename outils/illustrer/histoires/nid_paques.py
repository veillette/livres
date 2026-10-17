"""Le nid de Pâques — une chasse aux œufs qui découvre un vrai nid.

Le matin de Pâques, Élio et Maëlle cherchent les œufs en chocolat dans le
jardin de Mamie Odette. Sous le lilas, quatre œufs bleu ciel : un nid de
merle d'Amérique. Mamie arrête Maëlle avant qu'elle n'en prenne un : la
maman merle surveille, et si on reste trop près, elle n'ose pas revenir
couver. On recule, on plante une pancarte « CHUT ! NID DE MERLE », la chasse
continue de l'autre côté du jardin ; deux semaines plus tard, quatre petits
becs ouverts ; encore deux semaines, et les jeunes merles tachetés sautillent
sur la pelouse. Pâques est le décor ; l'histoire parle de respecter la
nature. (Œufs bleu ciel, poitrine orange de l'adulte, poitrine tachetée des
jeunes, environ deux semaines de couvaison et deux semaines au nid.)

Plans : 1 large (le jardin) · 2 moyen (la chasse) · 3 moyen (sous le lilas) ·
4 gros plan (quatre œufs bleus) · 5 moyen (stop !) · 6 gros plan (la maman
merle) · 7 moyen (on recule) · 8 moyen (la pancarte) · 9 large (de l'autre
côté) · 10 gros plan (les bébés) · 11 large (premiers vols) · 12 moyen (le
plus beau trésor).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import oeuf_decore, panier_osier
from objets import pot_fleurs

ID = "nid-paques"
PAPIER_PEINT = "fleurs"

BLEU_MERLE = "#9ad7e6"
LILAS = "#b197fc"

ELIO = dict(peau="doree", cheveux="brun", coiffure="herisses", habit="#69db7c", robe=False, jambes="#364fc7", nez="rond")
MAELLE = dict(peau="claire", cheveux="blond", coiffure="couettes", habit="#ffd43b", couleur_acc="#e64980", yeux="cils", taches=True)
MAMIE = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="chignon", habit="#e64980", carrure="ronde", acc=("lunettes",),
             nez="pointu")


def elio(x, y, s=1.1, **k):
    return personne(x, y, s, **{**ELIO, **k})


def maelle(x, y, s=1.05, **k):
    return personne(x, y, s, **{**MAELLE, **k})


def mamie(x, y, s=1.2, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def panier(x, y, s=0.6, oeufs=("#ff8787", "#ffd43b", "#74c0fc")):
    return panier_osier(x, y, s, oeufs=oeufs)


def oeuf_choco(x, y, s=1.0, c="#e03131", motif="pois", rot=0):
    return oeuf_decore(x, y, s, c, motif, rot=rot)


# --- Le merle d'Amérique (de profil, tête à droite) --------------------------

def merle(x, y, s=1.0, flip=False, jeune=False, ver=False, ailes="bas", rot=0):
    """Merle d'Amérique : dos gris-brun, tête sombre, cercle blanc autour de
    l'œil, bec jaune, poitrine orange (tachetée chez le jeune) ; (x, y) = pattes."""
    dos, tete = ("#8d7b68", "#6b5a48") if jeune else ("#6c6560", "#343a40")
    m = [chemin("M -40 -50 L -110 -30 L -104 -14 L -34 -34 Z", _assombrir(dos, 0.8)),
         trait(-4, -26, -8, 0, "#c9a37a", 4), trait(14, -26, 12, 0, "#c9a37a", 4),
         ellipse(0, -52, 50, 34, dos, rot=-14),
         ellipse(12, -42, 38, 24, "#e8590c" if not jeune else "#f3d9b1", rot=-14)]
    if jeune:
        r = random.Random(3)
        for _ in range(12):
            m.append(cercle(r.uniform(-8, 34), r.uniform(-58, -28), 3, "#6b5a48"))
    if ailes == "haut":
        m.append(chemin("M -14 -64 Q -60 -150 20 -150 Q 10 -100 14 -64 Z", _assombrir(dos, 0.85)))
    else:
        m.append(ellipse(-16, -56, 34, 16, _assombrir(dos, 0.85), rot=-16))
    m += [cercle(38, -88, 24, tete),
          poly([(56, -94), (86, -86), (56, -80)], "#fcc419"),
          cercle(44, -92, 7, "#fff"), cercle(45, -92, 3.6, ENCRE),
          chemin("M 52 -78 Q 46 -70 38 -72", stroke="#fff", sw=2, opacity=0.7)]
    if ver:
        m.append(chemin("M 80 -86 q 10 10 0 20 q -10 10 4 18", stroke="#f783ac", sw=5))
    return place(m + [occuper(-110, -150 if ailes == "haut" else -112, 86, 0)], x, y, s, flip=flip, rot=rot)


def nid(x, y, s=1.0, oeufs=4, bebes=0):
    """Nid d'herbes sèches et de boue ; oeufs bleu ciel, ou bébés au bec ouvert."""
    m = [ellipse(0, 0, 90, 36, "#8d6e4a"), ellipse(0, -10, 70, 22, "#5c3a1e")]
    for k in range(oeufs):
        dx = -42 + k * 28
        m.append(ellipse(dx, -16, 15, 19, volume(BLEU_MERLE, 0.4, 0.78)))
        m.append(ellipse(dx - 5, -24, 4, 6, "#fff", opacity=0.6))
    for k in range(bebes):
        dx = -42 + k * 28
        m += [ellipse(dx, -18, 16, 14, "#868e96"), chemin(f"M {dx - 10} -30 l 4 -8 l 4 6 l 4 -8 l 4 6", stroke="#ced4da", sw=2),
              poly([(dx - 12, -26), (dx, -62), (dx + 12, -26)], "#ffd43b"), poly([(dx - 8, -28), (dx, -50), (dx + 8, -28)], "#ff922b"),
              cercle(dx - 6, -22, 2.2, ENCRE), cercle(dx + 6, -22, 2.2, ENCRE)]
    for k in range(11):
        a = math.radians(180 + k * 18)
        m.append(trait(math.cos(a) * 90, math.sin(a) * 12 + 4, math.cos(a + 0.5) * 78, 28, "#a0693a", 3))
    m.append(chemin("M -90 0 Q 0 52 90 0", stroke="#7c4a1e", sw=7))
    return place(m, x, y, s)


def lilas(x, y, s=1.0, nid_=None):
    """Gros lilas en fleurs ; nid_ : dessin d'un nid posé dans une fourche."""
    m = [trait(0, 0, -20, -160, "#7c4a1e", 16), trait(-6, -60, 50, -170, "#7c4a1e", 12), trait(-10, -110, -80, -190, "#7c4a1e", 10)]
    feuilles = [(-110, -200, 70), (0, -250, 90), (100, -200, 70), (-60, -140, 60), (70, -130, 60)]
    m.append(feuillage([(px, py, r, "#40c057") for px, py, r in feuilles]))
    r = random.Random(5)
    for _ in range(18):
        px, py = r.uniform(-150, 150), r.uniform(-300, -110)
        if any((px - fx) ** 2 + (py - fy) ** 2 < (fr * 0.9) ** 2 for fx, fy, fr in feuilles):
            m.append(ellipse(px, py, 12, 20, LILAS, rot=r.uniform(-20, 20)))
            m.append(ellipse(px - 3, py - 6, 5, 8, "#d0bfff"))
    if nid_:
        m.append(nid_)
    return place(m, x, y, s)


def cloture(S, y, x0=0, x1=800, c="#c68642"):
    for x in range(x0 + 10, x1, 60):
        S.add(rect(x, y - 140, 26, 140, cylindre(c, 0.3, 0.75), rx=4), poly([(x, y - 140), (x + 13, y - 156), (x + 26, y - 140)], c))
    S.add(rect(x0, y - 110, x1 - x0, 14, c), rect(x0, y - 50, x1 - x0, 14, c))


def jardin(S, horizon=520, sol_y=600, graine=3):
    paysage(S, horizon, sol_y, herbe_="#8ce99a", colline="#b2f2bb", graine=graine)


def tulipes(S, x0, x1, y, nb=7, graine=1):
    r = random.Random(graine)
    for k in range(nb):
        x = x0 + (x1 - x0) * (k + 0.5) / nb
        c = ("#fa5252", "#fcc419", "#f783ac", "#ff922b")[k % 4]
        h = r.uniform(50, 80)
        S.add(trait(x, y, x, y - h, "#2f9e44", 4), ellipse(x - 8, y - h * 0.5, 6, 16, "#40c057", rot=-30))
        S.add(chemin(f"M {n(x - 12)} {n(y - h)} Q {n(x - 14)} {n(y - h - 28)} {n(x - 6)} {n(y - h - 26)} L {n(x)} {n(y - h - 18)} "
                     f"L {n(x + 6)} {n(y - h - 26)} Q {n(x + 14)} {n(y - h - 28)} {n(x + 12)} {n(y - h)} Z", c))


def arrosoir(x, y, s=1.0):
    return place([rect(-40, -70, 80, 70, volume("#4dabf7", 0.3, 0.75), rx=10), chemin("M 40 -50 L 90 -90 L 98 -84 L 46 -36", "#4dabf7"),
                  ellipse(94, -88, 8, 12, "#339af0", rot=-40), chemin("M -40 -60 Q -70 -40 -40 -16", stroke="#339af0", sw=7)], x, y, s)


def jumelles(x, y, s=1.0):
    return place([rect(-26, -18, 22, 36, ENCRE, rx=8), rect(4, -18, 22, 36, ENCRE, rx=8), rect(-6, -8, 12, 14, "#495057"),
                  cercle(-15, 14, 8, "#74c0fc"), cercle(15, 14, 8, "#74c0fc")], x, y, s)


def brouette(x, y, s=1.0):
    return place([cercle(70, -20, 22, "#343a40"), cercle(70, -20, 8, "#adb5bd"),
                  chemin("M -80 -90 L 80 -80 L 60 -30 L -60 -36 Z", volume("#2f9e44", 0.3, 0.75)),
                  trait(-60, -36, -120, -60, "#a0693a", 8), trait(-60, -36, -50, 0, "#a0693a", 8)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S, 520, 600, graine=4)
    cloture(S, 600, 420, 800)
    S.add(lilas(560, 640, 1.25, nid_=g([nid(-20, -150, 0.7, oeufs=0), merle(-30, -160, 0.65)])))
    tulipes(S, 30, 330, 640, 6, graine=2)
    S.add(elio(200, 780, 1.25, expr="bouche_bee", bras="tient", regard=(1, -0.5), objet=panier(68, -146 + 130, 0.45)))
    S.add(maelle(340, 790, 1.15, expr="content", bras="mains_jointes", regard=(1, -0.5)))
    S.add(panier(340, 800, 0.45, ("#ffd43b", "#e64980")))
    S.cachette(760, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trait(20, 200, 380, 180, "#7c4a1e", 14))
    S.add(nid(200, 220, 1.3))
    return S


def p01():
    """Plan large : le jardin de Mamie Odette, le matin de Pâques."""
    S = Scene()
    jardin(S, 500, 580, graine=6)
    S.add(maison(140, 600, 1.0, mur="#fff3bf", toit="#5c3d2e", porte="#2f9e44", volets="#2f9e44"))
    cloture(S, 580, 300, 800)
    S.add(lilas(620, 620, 1.0))
    tulipes(S, 280, 520, 640, 6, graine=3)
    S.add(mamie(250, 650, 0.85, expr="rire", bras="coucou", regard=(1, 0)))
    S.add(elio(420, 770, 0.95, expr="rire", bras="court", regard=(1, 0), objet=None))
    S.add(maelle(560, 780, 0.9, expr="rire", bras="tient", regard=(1, 0), objet=panier(68, -146 + 130, 0.4)))
    S.add(bulle(560, 140, 380, 90, "Le lapin de Pâques\nest passé !", 32, pointe=(260, 470)))
    S.cachette(30, 780)
    return S


def p02():
    """Plan moyen : la chasse aux œufs."""
    S = Scene()
    jardin(S, 520, 600, graine=7)
    cloture(S, 600)
    tulipes(S, 450, 760, 700, 7, graine=4)
    S.add(arrosoir(180, 730, 1.1))
    S.add(elio(300, 790, 1.2, expr="rire", bras="haut", regard=(0, -0.5), objet=oeuf_choco(-70, -170, 1.0, "#e03131")))
    S.add(maelle(560, 790, 1.15, expr="joie", bras="ramasse", flip=True, regard=(0, 1), objet=oeuf_choco(-36, -20, 1.0, "#fcc419", "zigzag")))
    S.add(panier(420, 790, 0.6, ("#ff8787", "#ffd43b", "#74c0fc", "#69db7c")))
    S.cachette(30, 790)
    return S


def p03():
    """Plan moyen : sous le lilas, quelque chose de bleu."""
    S = Scene()
    jardin(S, 520, 620, graine=8)
    cloture(S, 620)
    S.add(lilas(470, 700, 1.4, nid_=g([nid(-30, -170, 0.6), rect(-80, -230, 120, 70, "#40c057", opacity=0.75, rx=30)])))
    S.add(elio(250, 790, 1.2, expr="surpris", bras="tend", regard=(1, -0.5)))
    S.add(panier(140, 795, 0.5))
    S.add(bulle(250, 150, 340, 90, "Encore un œuf !\nUn bleu !", 32, pointe=(260, 470)))
    S.cachette(760, 790)
    return S


def p04():
    """Gros plan : quatre œufs bleu ciel dans le nid."""
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(feuillage([(120, 160, 160, "#40c057"), (640, 140, 180, "#40c057"), (380, 60, 150, "#51cf66"), (60, 600, 140, "#2f9e44"),
                     (760, 640, 150, "#2f9e44")]))
    S.add(trait(0, 640, 380, 520, "#7c4a1e", 30), trait(800, 600, 420, 520, "#7c4a1e", 26), trait(400, 800, 400, 520, "#7c4a1e", 34))
    S.add(nid(400, 520, 2.6))
    S.add(paillettes(560, 330, 0.8))
    S.cachette(110, 700)
    return S


def p05():
    """Plan moyen : « Stop ! Ne touchez pas ! »"""
    S = Scene()
    jardin(S, 520, 620, graine=9)
    cloture(S, 620)
    S.add(lilas(560, 700, 1.3, nid_=nid(-30, -160, 0.6)))
    S.add(maelle(440, 790, 1.1, expr="content", bras="tend", regard=(1, -0.5)))
    S.add(elio(300, 790, 1.1, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(mamie(120, 790, 1.2, expr="surpris", bras="leve_doigt", regard=(1, 0)))
    S.add(bulle(170, 150, 220, 90, "STOP !", 44, pointe=(140, 480)))
    S.cachette(770, 790)
    return S


def p06():
    """Gros plan : la maman merle sur la clôture, un ver dans le bec."""
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(feuillage([(700, 650, 200, "#40c057"), (790, 500, 120, "#51cf66")]))
    S.add(rect(0, 470, 800, 26, "#c68642"), rect(0, 600, 800, 26, "#c68642"))
    for x in range(30, 800, 120):
        S.add(rect(x, 380, 44, 420, cylindre("#c68642", 0.3, 0.75), rx=4), poly([(x, 380), (x + 22, 356), (x + 44, 380)], "#c68642"))
    S.add(merle(330, 470, 2.2, ver=True))
    S.add(texte(600, 200, "?", 70, "#e8590c", contour="#fff"))
    S.cachette(360, 730, "air")
    return S


def p07():
    """Plan moyen : on recule sur la pointe des pieds ; la maman revient."""
    S = Scene()
    jardin(S, 520, 620, graine=10)
    cloture(S, 620)
    S.add(lilas(600, 700, 1.3, nid_=g([nid(-30, -160, 0.6, oeufs=0), merle(-40, -168, 0.6)])))
    S.add(merle(470, 300, 0.5, ailes="haut", rot=-20))
    S.add(mamie(110, 790, 1.15, expr="sourire", bras="chut", regard=(1, 0), pas="pointe"))
    S.add(maelle(230, 790, 1.0, expr="sourire", bras="chut", regard=(1, 0), pas="pointe"))
    S.add(elio(340, 790, 1.05, expr="concentre", bras="equilibre", regard=(1, 0)))
    S.add(texte(470, 230, "Frrt !", 40, "#6c6560", contour="#fff", rot=-8))
    S.cachette(770, 790)
    return S


def pancarte_merle(x, y, s=1.0):
    """Pancarte plantée : « CHUT ! NID DE MERLE », avec un petit merle dessiné."""
    m = [rect(-8, -40, 16, 140, "#a0693a"), rect(-110, -150, 220, 120, "#fff9db", rx=6, stroke="#a0693a", stroke_width=6),
         texte(-30, -104, "CHUT !", 30, "#e03131"), texte(-30, -64, "NID DE", 22, ENCRE), texte(-30, -40, "MERLE", 22, ENCRE),
         place(merle(0, 0, 1.0), 64, -60, 0.4)]
    return place(m, x, y, s)


def pinceau_(x, y):
    return place([rect(-4, 0, 8, 50, "#a0693a", rx=3), rect(-6, -14, 12, 16, "#adb5bd"), chemin("M -6 -14 Q 0 -34 6 -14 Z", "#e03131")], x, y)


def p08():
    """Plan moyen : la pancarte « CHUT ! NID DE MERLE »."""
    S = Scene()
    jardin(S, 520, 620, graine=11)
    S.add(lilas(700, 660, 0.8, nid_=nid(-30, -160, 0.6, oeufs=0)))
    S.add(maison(110, 600, 0.75, mur="#fff3bf", toit="#5c3d2e", porte="#2f9e44", volets="#2f9e44"))
    S.add(elio(110, 790, 1.05, expr="fier", bras="hanches", regard=(1, 0)))
    S.add(maelle(230, 795, 1.0, expr="rire", bras="tient", regard=(1, 0), objet=pinceau_(68, -150)))
    S.add(pancarte_merle(420, 760, 1.0))
    S.add(mamie(590, 790, 1.15, expr="content", bras="ramasse", flip=True, regard=(-1, 0.4)))
    S.cachette(770, 790)
    return S


def p09():
    """Plan large : la chasse continue de l'autre côté du jardin."""
    S = Scene()
    jardin(S, 500, 580, graine=12)
    cloture(S, 580, 0, 500)
    S.add(lilas(690, 600, 0.65))
    S.add(pancarte_merle(600, 640, 0.45))
    # la balançoire
    S.add(trait(80, 640, 120, 380, "#a0693a", 12), trait(300, 640, 260, 380, "#a0693a", 12), trait(100, 380, 280, 380, "#a0693a", 12))
    S.add(trait(170, 380, 170, 560, "#495057", 3), trait(210, 380, 210, 560, "#495057", 3), rect(160, 556, 60, 12, "#e03131", rx=4))
    S.add(oeuf_choco(250, 650, 0.8, "#69db7c", "rayures"))
    S.add(brouette(420, 730, 0.9))
    S.add(oeuf_choco(410, 650, 0.7, "#e64980", "coeur"))
    S.add(pot_fleurs(560, 760, 0.6))
    S.add(elio(300, 790, 1.0, expr="rire", bras="tient", regard=(1, 0), objet=oeuf_choco(68, -150, 0.8, "#e03131")))
    S.add(maelle(520, 795, 0.95, expr="joie", bras="ramasse", flip=True, objet=oeuf_choco(-30, -18, 0.8, "#fcc419", "zigzag")))
    S.cachette(30, 790)
    return S


def p10():
    """Gros plan : quatre petits becs grands ouverts."""
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(feuillage([(120, 160, 160, "#40c057"), (680, 120, 170, "#40c057"), (60, 640, 140, "#2f9e44"), (760, 640, 150, "#2f9e44")]))
    S.add(trait(0, 660, 380, 560, "#7c4a1e", 30), trait(800, 620, 420, 560, "#7c4a1e", 26), trait(400, 800, 400, 560, "#7c4a1e", 34))
    S.add(nid(400, 560, 2.4, oeufs=0, bebes=4))
    S.add(merle(620, 360, 1.3, ver=True, flip=True, ailes="haut"))
    S.add(texte(250, 250, "Cuic ! Cuic !", 46, "#e8590c", contour="#fff", rot=-6))
    S.cachette(110, 720)
    return S


def p11():
    """Plan large : les jeunes merles sautillent sur la pelouse."""
    S = Scene()
    jardin(S, 500, 580, graine=13)
    cloture(S, 580, 300, 800)
    S.add(lilas(640, 600, 0.8, nid_=nid(-30, -160, 0.6, oeufs=0)))
    for k, (x, y, s, fl, ail) in enumerate(((330, 700, 0.5, False, "bas"), (430, 690, 0.45, True, "haut"), (520, 720, 0.5, False, "bas"),
                                             (610, 700, 0.45, True, "bas"))):
        S.add(merle(x, y, s, flip=fl, jeune=True, ailes=ail))
    S.add(merle(470, 610, 0.5, ver=True))
    S.add(maison(60, 590, 0.6, mur="#fff3bf", toit="#5c3d2e", porte="#2f9e44", cote=False))
    S.add(elio(130, 790, 1.05, expr="bouche_bee", bras="yeux", regard=(1, 0)))
    S.add(jumelles(130, 790 - 152 * 1.05, 1.05))
    S.add(maelle(250, 795, 0.95, expr="content", bras="chut", regard=(1, 0)))
    S.cachette(770, 790)
    return S


def p12():
    """Plan moyen : quatre jeunes merles en rang sur la clôture."""
    S = Scene()
    jardin(S, 520, 640, graine=14)
    cloture(S, 520)
    for k in range(4):
        S.add(merle(220 + k * 120, 410, 0.55, jeune=True, flip=k % 2 == 1))
    S.add(mamie(560, 800, 1.2, expr="content", bras="epaule", flip=True, regard=(-1, -0.5)))
    S.add(maelle(400, 800, 1.05, expr="rire", bras="tient", regard=(0, -1), objet=oeuf_choco(68, -150, 0.8, "#e64980", "coeur")))
    S.add(elio(250, 800, 1.1, expr="content", bras="tient", regard=(1, -1), objet=oeuf_choco(68, -150, 0.8, "#4dabf7", "pois")))
    S.add(texte(400, 160, "Un, deux, trois, quatre !", 36, "#2f9e44", contour="#fff", rot=-4))
    S.cachette(760, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("nid-seul.svg", vignette),
    ("01-le-jardin.svg", p01), ("02-la-chasse.svg", p02), ("03-sous-le-lilas.svg", p03),
    ("04-quatre-oeufs-bleus.svg", p04), ("05-stop.svg", p05), ("06-la-maman-merle.svg", p06),
    ("07-on-recule.svg", p07), ("08-la-pancarte.svg", p08), ("09-de-l-autre-cote.svg", p09),
    ("10-les-bebes.svg", p10), ("11-premiers-vols.svg", p11), ("12-le-plus-beau-tresor.svg", p12),
]
