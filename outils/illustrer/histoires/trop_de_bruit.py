"""Trop de bruit à minuit — un réveillon pour un enfant que le bruit dérange.

Le 31 décembre, chez Grand-maman, la famille fait la fête : rires,
musique, mirlitons. Théo n'aime pas les bruits forts ; il se cache sous les
manteaux de la chambre d'amis. Sa cousine Noémie lui prête ses
cache-oreilles en peluche, et Grand-maman l'emmène voir les feux de minuit
depuis la fenêtre de l'étage, loin des casseroles. En redescendant, toute
la famille lui souhaite la bonne année… en chuchotant. Le jour de l'An est
le décor ; l'histoire parle d'une sensibilité qu'on respecte.

Plans : 1 moyen (l'arrivée) · 2 gros plan (trop fort) · 3 large (la fête) ·
4 moyen (sous les manteaux) · 5 gros plan (Noémie) · 6 moyen (les
cache-oreilles) · 7 large (ça va mieux) · 8 moyen (les casseroles) · 9 gros
plan (Grand-maman) · 10 large (minuit à la fenêtre) · 11 moyen (tout bas) ·
12 gros plan (la cabane de manteaux).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import guirlande_lumineuse, confettis, serpentin, mirliton, feu_artifice, chapeau_fete

ID = "trop-de-bruit"
PAPIER_PEINT = "fleurs"

ROSE_PELUCHE = "#faa2c1"


def cache_oreilles(c=ROSE_PELUCHE):
    """Cache-oreilles en peluche, sur la tête d'une personne (coiffe)."""
    m = [chemin("M -50 -150 Q -54 -222 0 -224 Q 54 -222 50 -150", stroke="#868e96", sw=7)]
    for sgn in (-1, 1):
        m.append(cercle(sgn * 52, -148, 24, volume(c, 0.35, 0.8)))
        for k in range(8):
            a = math.radians(k * 45)
            m.append(cercle(sgn * 52 + 21 * math.cos(a), -148 + 21 * math.sin(a), 6, c))
    return g(m)


def ondes(x, y, s=1.0, couleur="#e03131", cote=1):
    """Lignes de bruit en zigzag, qui piquent."""
    m = []
    for k in range(3):
        m.append(chemin(f"M {cote * (k * 18)} {-30 + k * 4} l {cote * 10} 10 l {cote * -6} 10 l {cote * 10} 10 l {cote * -6} 10 l {cote * 10} 10",
                        stroke=couleur, sw=4))
    return place(m, x, y, s)


THEO = dict(peau="rosee", cheveux="chatain", coiffure="herisses", habit="#4dabf7", robe=False, jambes="#364fc7",
            acc=("col",), nez="petit")
NOEMIE = dict(stature="ado", peau="doree", cheveux="noir", coiffure="queue", habit="#e64980", robe=False, jambes="#343a40",
              yeux="cils", nez="pointu")
GRAND_MAMAN = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="boucles", habit="#7048e8", carrure="ronde",
                   acc=("lunettes",), nez="rond")
PAPA = dict(stature="adulte", peau="rosee", cheveux="chatain", coiffure="courts", habit="#1971c2", robe=False, jambes="#343a40",
            nez="long")
PAUL = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="chauve_cote", habit="#f08c00", robe=False, jambes="#495057",
            barbe="#d9480f", carrure="ronde", nez="rond")
TANTE = dict(stature="adulte", peau="claire", cheveux="blond", coiffure="longs", habit="#2f9e44", carrure="fine", yeux="cils")
COUSINS = (dict(peau="claire", cheveux="roux", coiffure="couettes", habit="#ffd43b"),
           dict(peau="doree", cheveux="noir", coiffure="courts", habit="#69db7c", robe=False, jambes="#2b8a3e"),
           dict(peau="claire", cheveux="blond", coiffure="raie", habit="#ff8787", robe=False, jambes="#495057"))


def theo(x, y, s=1.15, oreilles=False, **k):
    if oreilles:
        k.setdefault("coiffe", cache_oreilles())
    return personne(x, y, s, **{**THEO, **k})


def noemie(x, y, s=1.15, **k):
    return personne(x, y, s, **{**NOEMIE, **k})


def grand_maman(x, y, s=1.15, oreilles=False, **k):
    if oreilles:
        k.setdefault("coiffe", cache_oreilles("#b197fc"))
    return personne(x, y, s, **{**GRAND_MAMAN, **k})


def papa(x, y, s=1.15, **k):
    return personne(x, y, s, **{**PAPA, **k})


def paul(x, y, s=1.15, **k):
    return personne(x, y, s, **{**PAUL, **k})


def cousin(i, x, y, s=0.95, **k):
    return personne(x, y, s, **{**COUSINS[i % len(COUSINS)], **k})


def enceinte(x, y, s=1.0):
    """Grosse enceinte qui fait boum boum ; (x, y) = sol."""
    m = [rect(-50, -170, 100, 170, volume("#343a40", 0.25, 0.75), rx=10),
         cercle(0, -115, 32, "#495057"), cercle(0, -115, 18, "#868e96"), cercle(0, -40, 22, "#495057"), cercle(0, -40, 10, "#868e96")]
    return place(m, x, y, s)


def casserole(x, y, s=1.0, rot=0):
    """Casserole et sa cuillère de bois ; (x, y) = centre."""
    return place([rect(30, -6, 70, 12, "#495057", rx=6), ellipse(0, 0, 40, 14, "#868e96"),
                  chemin("M -40 0 Q -40 40 0 40 Q 40 40 40 0 Z", volume("#adb5bd", 0.3, 0.7))], x, y, s, rot=rot)


def cuillere_bois(x, y, s=1.0, rot=0):
    return place([rect(-4, -60, 8, 60, "#c68642", rx=4), ellipse(0, -66, 12, 16, "#c68642")], x, y, s, rot=rot)


def manteaux(x, y, s=1.0):
    """Pile de manteaux d'hiver sur le lit ; (x, y) = bas de la pile."""
    cols = ("#c92a2a", "#1864ab", "#2b8a3e", "#e8590c", "#5f3dc4", "#343a40")
    m = []
    for k, c in enumerate(cols):
        dx, dy = (k % 3 - 1) * 70, -k * 22
        m.append(chemin(f"M {dx - 90} {dy} Q {dx - 96} {dy - 60} {dx - 30} {dy - 56} L {dx + 40} {dy - 60} Q {dx + 100} {dy - 50} {dx + 90} {dy} Z",
                        volume(c, 0.3, 0.75)))
        m.append(trait(dx - 10, dy - 54, dx - 10, dy - 6, _assombrir(c, 0.7), 3))
        m.append(cercle(dx - 2, dy - 40, 4, "#ffd43b"))
    return place(m, x, y, s)


def salon(S, y=600, soir=True):
    """Le salon de Grand-maman le soir du réveillon."""
    piece(S, "manoir", y)
    S.ambiance("interieur")
    dehors = g([rect(0, 0, 800, 800, "#14204a"), rect(0, 210, 800, 300, "#dbe4ff"),
                *[cercle(560 + (k * 37) % 160, 110 + (k * 29) % 80, 2, "#fff") for k in range(10)]])
    S.add(fenetre(560, 100, 170, 150, "#14204a", rideaux="#c92a2a", contenu=dehors))
    S.add(guirlande_lumineuse(10, 40, 790, 40, creux=18, nb=14))


def chambre_amis(S, y=600):
    piece(S, "chambre", y)
    S.ambiance("nuit")
    S.add(fenetre(570, 110, 150, 140, "#14204a", nuit_=True, rideaux="#748ffc"))
    # le rai de lumière qui vient du couloir
    S.add(poly([(40, 0), (140, 0), (330, 800), (0, 800), (0, 380)], "#fff3bf", opacity=0.25))
    S.lumiere(120, 300, 200, "#ffd43b", 0.35)


def lit_manteaux(S, x=430, y=760, w=500):
    S.add(lit(x, y, w, "#dbe4ff", "#748ffc"))
    S.add(manteaux(x + 40, y - 110, 1.15))


# ---------------------------------------------------------------------------

def vue_feux(x0, y0, w, h, graine=1):
    """Ce qu'on voit par la fenêtre : toits enneigés et feux d'artifice au loin."""
    r = random.Random(graine)
    m = [rect(0, 0, 800, 800, lineaire([(0, "#0b1433"), (1, "#2b3a78")])),
         *[cercle(x0 + r.uniform(0, w), y0 + r.uniform(0, h * 0.6), 1.8, "#fff") for _ in range(20)],
         feu_artifice(x0 + w * 0.3, y0 + h * 0.28, 50, "#ffd43b"), feu_artifice(x0 + w * 0.7, y0 + h * 0.2, 40, "#f783ac"),
         feu_artifice(x0 + w * 0.52, y0 + h * 0.42, 30, "#69db7c")]
    for k in range(5):
        hx = x0 + k * w / 4.5
        m.append(poly([(hx, y0 + h), (hx, y0 + h * 0.8), (hx + w / 9, y0 + h * 0.68), (hx + w / 4.5, y0 + h * 0.8), (hx + w / 4.5, y0 + h)], "#1c2a52"))
        m.append(poly([(hx - 4, y0 + h * 0.8), (hx + w / 9, y0 + h * 0.66), (hx + w / 4.5 + 4, y0 + h * 0.8), (hx + w / 9, y0 + h * 0.72)], "#dbe4ff"))
        m.append(rect(hx + w / 14, y0 + h * 0.86, 10, 12, "#ffd43b"))
    return g(m)


def couverture():
    S = Scene()
    piece(S, "chambre", 640)
    S.ambiance("nuit")
    fx, fy, fw, fh = 140, 90, 520, 400
    S.add(fenetre(fx, fy, fw, fh, "#0b1433", rideaux="#748ffc", contenu=vue_feux(fx, fy, fw, fh, 3)))
    S.lumiere(fx + fw * 0.3, fy + fh * 0.28, 100, "#ffd43b", 0.5)
    S.lumiere(fx + fw * 0.7, fy + fh * 0.2, 90, "#f783ac", 0.5)
    S.add(grand_maman(500, 800, 1.45, oreilles=True, expr="content", bras="epaule", flip=True, regard=(-1, -0.6)))
    S.add(theo(320, 800, 1.4, oreilles=True, expr="rire", bras="mains_jointes", regard=(1, -1)))
    S.cachette(60, 760)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(place(cache_oreilles(), 200, 380, 1.5))
    return S


def p01():
    """Plan moyen : l'arrivée de toute la famille, dans l'entrée."""
    S = Scene()
    piece(S, "manoir", 610)
    S.ambiance("interieur")
    S.add(porte(120, 640, 160, 340, "#8d5524", ouverte=True))
    S.add(rect(40, 300, 160, 340, "#14204a", opacity=0.0))
    S.add(paul(180, 760, 1.2, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(personne(330, 770, 1.15, expr="rire", bras="porte", regard=(1, 0), objet=place(chemin("M -40 -20 h 80 v 40 h -80 Z", "#ffd43b"), 0, -70), **TANTE))
    S.add(cousin(0, 440, 790, 0.9, expr="rire", bras="haut", regard=(1, 0)))
    S.add(papa(630, 780, 1.2, expr="sourire", bras="main", flip=True, regard=(-1, 0)))
    S.add(theo(520, 790, 0.95, expr="surpris", bras="main", regard=(-1, 0)))
    S.add(texte(250, 290, "Ha ha ha !", 44, "#e8590c", contour="#fff", rot=-8))
    S.add(texte(520, 220, "Bonsoir !", 38, "#c92a2a", contour="#fff", rot=6))
    S.add(texte(130, 160, "BLAM !", 40, "#495057", contour="#fff", rot=-14))
    S.cachette(770, 790)
    return S


def p02():
    """Gros plan : Théo se bouche les oreilles."""
    S = Scene()
    salon(S, 620)
    S.add(theo(400, 800, 1.6, expr="degoute", bras="joues", regard=(0, 0)))
    S.add(ondes(250, 470, 1.4, cote=-1), ondes(550, 470, 1.4, cote=1), ondes(240, 380, 1.0, "#f08c00", -1), ondes(560, 380, 1.0, "#f08c00", 1))
    S.camera(1.35, 400, 520)
    S.dessus(bulle(400, 100, 360, 90, "Trop de bruit…", 38, pointe=S.vers_page(400, 450)))
    S.cachette(720, 780)
    return S


def p03():
    """Plan large : la fête bat son plein."""
    S = Scene()
    salon(S, 590)
    S.add(enceinte(110, 640, 1.1))
    S.add(notes(170, 400, 1.1, "#5f3dc4"), notes(90, 350, 0.9, "#5f3dc4"))
    S.add(texte(110, 300, "BOUM BOUM", 34, "#5f3dc4", contour="#fff", rot=-8))
    S.add(paul(300, 700, 1.15, expr="rire", bras="danse", regard=(1, 0), coiffe=chapeau_fete("#e03131", y=-198)))
    S.add(personne(470, 700, 1.1, expr="rire", bras="danse", flip=True, regard=(-1, 0), **TANTE))
    S.add(papa(640, 700, 1.15, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(cousin(1, 230, 790, 0.85, expr="rire", bras="tient", regard=(1, 0), objet=mirliton(68, -126, 1.0, rot=-10)))
    S.add(cousin(2, 560, 790, 0.85, expr="rire", bras="tient", flip=True, regard=(-1, 0), objet=mirliton(68, -126, 1.0, rot=-10, couleur="#ffd43b")))
    S.add(cousin(0, 400, 795, 0.8, expr="joie", bras="saute"))
    S.add(texte(320, 560, "Pouêêêt !", 34, "#e64980", contour="#fff", rot=8))
    S.add(confettis(150, 120, 700, 420, 40, graine=5))
    S.add(serpentin(250, 260, 1.0, "#f783ac", rot=10), serpentin(470, 200, 0.9, "#4dabf7", rot=-14))
    S.cachette(770, 790)
    return S


def p04():
    """Plan moyen : sous la pile de manteaux, dans la chambre d'amis."""
    S = Scene()
    chambre_amis(S)
    S.add(lit(430, 760, 500, "#dbe4ff", "#748ffc"))
    # Théo sous les manteaux : on ne voit que ses yeux et ses chaussures
    S.add(manteaux(470, 650, 1.25))
    S.add(rect(350, 560, 90, 46, "#1b1f3b", rx=20))
    S.add(oeil(380, 584, "normal", (0, 0), taille=1.2), oeil(410, 584, "normal", (0, 0), taille=1.2))
    S.add(ellipse(600, 640, 18, 12, "#2b5c9e"), ellipse(632, 644, 18, 12, "#2b5c9e"))
    S.add(texte(560, 400, "Ouf.", 50, "#fff3bf", contour="#1b1f3b"))
    S.cachette(760, 780)
    return S


def p05():
    """Gros plan : Noémie soulève un manteau ; « Trop de bruit ? »"""
    S = Scene()
    chambre_amis(S)
    S.add(lit(430, 790, 600, "#dbe4ff", "#748ffc"))
    S.add(theo(330, 700, 1.25, expr="timide", bras="croises", regard=(1, -0.5)))
    S.add(manteaux(300, 720, 1.2))
    S.add(noemie(560, 800, 1.35, expr="sourire", bras="tend", flip=True, regard=(-1, 0.3),
                 objet=place(chemin("M -60 -10 Q -40 -60 30 -50 L 60 0 Z", volume("#c92a2a", 0.3, 0.75)), *ancre(96, -104, "tend", "ado"))))
    S.camera(1.3, 440, 520)
    S.dessus(bulle(470, 100, 460, 100, "Trop de bruit ?\nMoi aussi, parfois.", 32, pointe=S.vers_page(560, 430)))
    S.cachette(720, 780)
    return S


def p06():
    """Plan moyen : les cache-oreilles en peluche."""
    S = Scene()
    chambre_amis(S)
    S.add(lit(450, 760, 520, "#dbe4ff", "#748ffc"))
    S.add(manteaux(560, 650, 0.9))
    S.add(noemie(520, 790, 1.3, expr="content", bras="tend", flip=True, regard=(-1, 0.5)))
    S.add(theo(330, 790, 1.2, oreilles=True, expr="bouche_bee", bras="joues", regard=(1, -0.3)))
    S.add(paillettes(330, 430, 0.8, "#faa2c1"))
    S.add(bulle(230, 140, 360, 100, "Les bruits deviennent\ntout ronds !", 30, pointe=(330, 480)))
    S.cachette(770, 790)
    return S


def biscuit(x, y, s=1.0):
    return place([cercle(0, 0, 14, "#e3a857"), cercle(-4, -3, 2.5, "#7c4a1e"), cercle(5, 3, 2.5, "#7c4a1e")], x, y, s)


def p07():
    """Plan large : avec ses cache-oreilles, Théo revient au bord de la fête."""
    S = Scene()
    salon(S, 590)
    S.add(enceinte(720, 640, 0.9))
    S.add(rect(0, 0, 150, 640, "#e8d5c4"), rect(140, 120, 14, 520, "#8d5524"))
    S.add(paul(400, 690, 1.05, expr="rire", bras="danse", regard=(1, 0), coiffe=chapeau_fete("#e03131", y=-198)))
    S.add(personne(560, 690, 1.0, expr="rire", bras="danse", flip=True, regard=(-1, 0), **TANTE))
    S.add(cousin(1, 480, 790, 0.8, expr="rire", bras="saute"))
    S.add(noemie(300, 780, 1.05, expr="malin", bras="hanches", regard=(-1, 0)))
    S.add(theo(170, 790, 1.0, oreilles=True, expr="content", bras="tient", regard=(1, 0), objet=biscuit(68, -146, 1.0)))
    S.add(confettis(300, 120, 700, 360, 25, graine=8))
    S.cachette(770, 790)
    return S


def p08():
    """Plan moyen : dans la cuisine, les casseroles de minuit."""
    S = Scene()
    piece(S, "cuisine", 600)
    S.ambiance("interieur")
    S.add(horloge(400, 140, 56, heure=11, minute=55))
    S.add(texte(400, 240, "23 h 55", 30, "#495057"))
    S.add(cousin(1, 200, 760, 1.0, expr="rire", bras="tient", regard=(1, 0), objet=g([casserole(50, -150, 1.0, rot=-20), cuillere_bois(86, -150, 1.0, rot=20)])))
    S.add(cousin(2, 360, 770, 0.95, expr="rire", bras="haut", regard=(1, 0), objet=cuillere_bois(70, -165, 1.0, rot=10)))
    S.add(papa(560, 770, 1.2, expr="rire", bras="designe", regard=(-1, -1), flip=True))
    S.add(theo(690, 790, 1.0, oreilles=True, expr="inquiet", bras="croises", regard=(-1, 0)))
    S.add(texte(250, 470, "Bing ! Bang !", 40, "#e03131", contour="#fff", rot=-8))
    S.add(bulle(560, 330, 300, 80, "Les casseroles !", 30, pointe=(560, 500)))
    S.cachette(40, 790)
    return S


def p09():
    """Gros plan : Grand-maman tend la main à Théo."""
    S = Scene()
    piece(S, "manoir", 600)
    S.ambiance("interieur")
    S.add(grand_maman(520, 800, 1.6, oreilles=True, expr="content", bras="tend", flip=True, regard=(-1, 0.4)))
    S.add(theo(250, 800, 1.45, oreilles=True, expr="surpris", bras="tend", regard=(1, -0.3)))
    S.camera(1.3, 400, 520)
    S.dessus(bulle(400, 100, 500, 100, "Je connais la place\nla plus tranquille.", 32, pointe=S.vers_page(520, 440)))
    S.cachette(80, 760)
    return S


def p10():
    """Plan large : à minuit, à la fenêtre de l'étage, les feux au loin."""
    S = Scene()
    piece(S, "chambre", 620)
    S.ambiance("nuit")
    fx, fy, fw, fh = 100, 80, 600, 420
    S.add(fenetre(fx, fy, fw, fh, "#0b1433", rideaux="#748ffc", contenu=vue_feux(fx, fy, fw, fh, 5)))
    S.lumiere(fx + fw * 0.3, fy + fh * 0.28, 110, "#ffd43b", 0.5)
    S.lumiere(fx + fw * 0.7, fy + fh * 0.2, 90, "#f783ac", 0.5)
    S.add(theo(330, 790, 1.15, oreilles=True, expr="bouche_bee", bras="bas", regard=(0, -1)))
    S.add(grand_maman(480, 790, 1.2, oreilles=True, expr="content", bras="epaule", flip=True, regard=(-1, -0.5)))
    S.add(texte(660, 580, "bonne année !", 20, "#adb5bd"))
    S.add(texte(150, 620, "bonne année !", 16, "#adb5bd"))
    S.cachette(770, 790)
    return S


def p11():
    """Plan moyen : toute la famille chuchote « bonne année »."""
    S = Scene()
    salon(S, 600)
    S.add(paul(160, 760, 1.15, expr="sourire", bras="chut", regard=(1, 0.5)))
    S.add(personne(300, 750, 1.1, expr="sourire", bras="chut", regard=(1, 0.5), **TANTE))
    S.add(papa(540, 750, 1.15, expr="sourire", bras="chut", flip=True, regard=(-1, 0.5)))
    S.add(noemie(660, 765, 1.05, expr="content", bras="chut", flip=True, regard=(-1, 0.5)))
    S.add(cousin(0, 240, 800, 0.85, expr="content", bras="chut", regard=(1, 0)))
    S.add(cousin(1, 570, 800, 0.85, expr="content", bras="chut", flip=True, regard=(-1, 0)))
    S.add(theo(410, 800, 1.05, oreilles=True, expr="rire", bras="mains_jointes"))
    S.add(texte(320, 240, "bonne année, Théo…", 34, "#5f3dc4", contour="#fff", poids=500))
    S.add(texte(200, 320, "chut…", 26, "#868e96", contour="#fff", rot=-8), texte(620, 320, "chut…", 26, "#868e96", contour="#fff", rot=8))
    S.cachette(770, 790)
    return S


def p12():
    """Gros plan : Théo dort dans sa cabane de manteaux."""
    S = Scene()
    chambre_amis(S)
    S.add(lit(400, 790, 640, "#dbe4ff", "#748ffc"))
    S.add(noemie(640, 760, 1.25, expr="content", bras="tend", flip=True, regard=(-1, 0.6)))
    S.add(theo(380, 690, 1.2, oreilles=True, expr="dort", bras="calin", ombre=False))
    S.add(manteaux(390, 760, 1.3))
    S.add(zzz(250, 450, 0.9))
    S.camera(1.3, 420, 560)
    S.cachette(110, 780)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cache-oreilles-seuls.svg", vignette),
    ("01-on-arrive.svg", p01), ("02-trop-fort.svg", p02), ("03-la-fete.svg", p03),
    ("04-la-chambre.svg", p04), ("05-noemie.svg", p05), ("06-les-cache-oreilles.svg", p06),
    ("07-ca-va-mieux.svg", p07), ("08-les-casseroles.svg", p08), ("09-grand-maman.svg", p09),
    ("10-minuit.svg", p10), ("11-tout-bas.svg", p11), ("12-la-cabane.svg", p12),
]
