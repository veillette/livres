"""Deux galettes pour Gaspard — la fête des Rois, quand on a deux maisons.

Gaspard vit une semaine chez Papa, une semaine chez Maman. Quand la
maîtresse raconte la fête des Rois, il s'inquiète : où la fêtera-t-il ?
Chez Papa, une galette feuilletée, la tradition de l'enfant sous la table,
la fève : roi ! (et il choisit Papa pour second roi). Chez Maman, un gâteau
des rois à la québécoise, avec la fève du roi et le pois de la reine : il
trouve le pois. Le soir, deux couronnes et un appel à Papa. La fête des
Rois est le décor ; l'histoire parle des familles qui vivent dans deux
maisons.

Plans : 1 large, coupé en deux (deux maisons) · 2 moyen (la maîtresse) ·
3 gros plan (je la fête où ?) · 4 moyen (la galette chez Papa) · 5 moyen
(sous la table) · 6 gros plan (la fève) · 7 moyen (deux rois) · 8 large (le
voyage) · 9 moyen (le gâteau des rois) · 10 gros plan (le pois) · 11 moyen
(l'appel) · 12 gros plan (deux couronnes au lit).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne, _couronne_tete

ID = "deux-galettes"
PAPIER_PEINT = "losanges"

OR_ = "#fcc419"
BLEU_PAPA = "#74c0fc"
JAUNE_MAMAN = "#ffe066"

GASPARD = dict(peau="claire", cheveux="roux", coiffure="courts", habit="#2f9e44", robe=False, jambes="#364fc7", taches=True,
               nez="retrousse")
PAPA = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="courts", habit="#1971c2", robe=False, jambes="#495057",
            barbe="#c2410c", carrure="fine", nez="long")
MAMAN = dict(stature="adulte", peau="claire", cheveux="brun", coiffure="queue", habit="#e64980", carrure="normale",
             yeux="cils", nez="petit")
MAMIE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="boucles", habit="#7048e8", carrure="ronde",
             acc=("lunettes",), nez="rond")
SOPHIE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="tresses", habit="#f08c00", carrure="fine", yeux="cils")
ELEVES = (dict(peau="doree", cheveux="noir", coiffure="couettes", habit="#f783ac"),
          dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#ffd43b", robe=False, jambes="#495057"),
          dict(peau="rosee", cheveux="blond", coiffure="longs", habit="#74c0fc"))


def gaspard(x, y, s=1.15, couronnes=0, sac=False, **k):
    if couronnes == 1:
        k.setdefault("acc", ("couronne",))
    elif couronnes == 2:
        k.setdefault("acc", ("couronne",))
        k.setdefault("coiffe", place(_couronne_tete(OR_), 0, -30))
    if sac:
        k.setdefault("derriere", g([rect(-46, -104, 92, 74, volume("#e8590c", 0.3, 0.75), rx=16), rect(-36, -60, 72, 22, "#d9480f", rx=8)]))
    return personne(x, y, s, **{**GASPARD, **k})


def papa(x, y, s=1.15, **k):
    return personne(x, y, s, **{**PAPA, **k})


def maman(x, y, s=1.15, **k):
    return personne(x, y, s, **{**MAMAN, **k})


def mamie(x, y, s=1.1, **k):
    return personne(x, y, s, **{**MAMIE, **k})


def galette(x, y, s=1.0, part=False):
    """Galette des rois feuilletée et dorée, décorée en losanges ; (x, y) = base."""
    m = [ellipse(0, 0, 110, 26, "#fff", stroke="#dee2e6", stroke_width=3),
         ellipse(0, -12, 92, 26, "#d9a440"), ellipse(0, -20, 90, 24, volume("#f0b84d", 0.4, 0.75)),
         chemin(" ".join(f"M {-70 + k * 28} -36 L {-40 + k * 28} -4" for k in range(5)) + " "
                + " ".join(f"M {-40 + k * 28} -36 L {-70 + k * 28} -4" for k in range(5)), stroke="#c68642", sw=2, opacity=0.7)]
    if part:
        m.append(poly([(0, -20), (90, -24), (80, 0)], "#fff3bf"))
    return place(m, x, y, s)


def gateau_rois(x, y, s=1.0):
    """Gâteau des rois à la québécoise : rond, glacé, avec ses petits bonbons."""
    m = [ellipse(0, 0, 110, 26, "#fff", stroke="#dee2e6", stroke_width=3),
         rect(-84, -70, 168, 64, volume("#e9b98a", 0.3, 0.75), rx=10), ellipse(0, -70, 84, 22, "#fff4e6"),
         chemin("M -84 -66 Q -70 -40 -56 -64 Q -42 -36 -28 -64 Q -14 -40 0 -64 Q 14 -36 28 -64 Q 42 -40 56 -64 Q 70 -36 84 -66",
                "#fff4e6")]
    for k, c in enumerate(("#e03131", "#2f9e44", OR_, "#e03131", "#2f9e44")):
        m.append(cercle(-50 + k * 25, -74 + (k % 2) * 6, 5, c))
    return place(m, x, y, s)


def feve(x, y, s=1.0):
    """La fève : une toute petite couronne en porcelaine ; (x, y) = centre."""
    return place([poly([(-14, 8), (-16, -10), (-8, -2), (0, -14), (8, -2), (16, -10), (14, 8)], "#fff", stroke="#adb5bd", stroke_width=2),
                  cercle(0, -14, 3, OR_), rect(-14, 4, 28, 6, OR_, rx=2)], x, y, s)


def pois(x, y, s=1.0):
    return place([cercle(0, 0, 10, volume("#69db7c", 0.4, 0.7)), ellipse(-3, -4, 3, 2, "#fff", opacity=0.6)], x, y, s)


def couronne_carton(x, y, s=1.0):
    """Couronne de carton dorée posée seule ; (x, y) = base."""
    m = [poly([(-60, 0), (-64, -60), (-36, -30), (0, -74), (36, -30), (64, -60), (60, 0)], volume(OR_, 0.4, 0.72)),
         rect(-60, -14, 120, 14, "#f59f00", rx=3)]
    for k, c in enumerate(("#e03131", "#1c7ed6", "#2f9e44")):
        m.append(cercle(-30 + k * 30, -8, 5, c))
    m += [cercle(-64, -64, 6, "#e03131"), cercle(0, -78, 6, "#1c7ed6"), cercle(64, -64, 6, "#e03131")]
    return place(m, x, y, s)


def couteau(x, y, s=1.0, rot=0):
    return place([rect(-5, -10, 10, 34, "#8d5524", rx=4), poly([(-5, -10), (5, -10), (4, -80), (-2, -70)], "#ced4da")], x, y, s, rot=rot)


def cuisine(S, mur="#e7f5ff", y=600, papier=None):
    """La cuisine d'une des deux maisons (bleue chez Papa, jaune chez Maman)."""
    interieur(S, mur, "#c68642", y, papier=papier)
    S.ambiance("interieur")


def cuisine_papa(S, y=600):
    piece(S, "cuisine", y)
    S.add(fenetre(560, 90, 170, 150, "#d0ebff", rideaux="#1971c2",
                  contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 200, 800, 100, "#f8f9fa")])))


def cuisine_maman(S, y=600):
    interieur(S, "#fff9db", "#d9a066", y, papier="#ffe066")
    S.add(fenetre(80, 90, 170, 150, "#d0ebff", rideaux="#e64980",
                  contenu=g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 200, 800, 100, "#f8f9fa")])))


def voiture(x, y, s=1.0, couleur="#1971c2", flip=False):
    m = [ellipse(0, 0, 160, 10, "#000", opacity=0.15),
         chemin("M -150 -28 Q -152 -72 -110 -76 L -70 -78 Q -42 -132 16 -134 L 58 -134 Q 100 -132 122 -82 L 140 -78 "
                "Q 162 -72 162 -40 L 162 -26 Q 162 -14 150 -14 L -140 -14 Q -150 -14 -150 -28 Z", volume(couleur, 0.3, 0.75)),
         chemin("M -56 -82 Q -36 -122 6 -122 L 6 -82 Z", "#a5d8ff"), chemin("M 20 -82 L 20 -122 L 56 -122 Q 92 -120 108 -82 Z", "#a5d8ff"),
         rect(146, -66, 14, 12, "#fff3bf", rx=3), rect(-150, -64, 10, 12, "#fa5252", rx=3)]
    for wx in (-92, 100):
        m += [cercle(wx, -14, 32, "#343a40"), cercle(wx, -14, 15, "#ced4da"), cercle(wx, -14, 5, "#868e96")]
    return place(m, x, y, s, flip=flip)


def hiver_jour(S, sol_y=620, graine=3):
    ciel(S, "#a5d8ff", "#f8f9fa")
    collines(S, sol_y - 50, "#e7f5ff", graine=graine, bosquets=False)
    sol(S, sol_y, "#f8f9fa", bosse=10)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    S.add(rect(0, 0, 400, 800, "#d0ebff"), rect(400, 0, 400, 800, "#fff3bf"))
    motif = [cercle(40 + (k % 5) * 80, 40 + (k // 5) * 80, 6, "#a5d8ff") for k in range(35)]
    motif += [etoile5(440 + (k % 5) * 80, 40 + (k // 5) * 80, 8, "#ffe066") for k in range(35)]
    S.add(g(motif))
    S.add(rect(0, 640, 800, 160, "#c68642"), planches(0, 640, 800, 160, "#c68642", larg=40, vertical=False))
    S.add(trait(400, 0, 400, 800, "#fff", 8))
    S.add(papa(110, 720, 1.15, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(maman(690, 720, 1.15, expr="rire", bras="applaudit", flip=True, regard=(-1, 0)))
    S.add(table(220, 790, 220, 110, "#a0693a", nappe="#d0ebff"), table(580, 790, 220, 110, "#a0693a", nappe="#fff3bf"))
    S.add(galette(220, 668, 0.85), gateau_rois(580, 668, 0.8))
    S.add(gaspard(400, 790, 1.45, couronnes=1, expr="rire", bras="saute"))
    S.ambiance("interieur")
    S.cachette(40, 300, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(couronne_carton(200, 220, 1.6))
    S.add(feve(110, 240, 1.4), pois(300, 240, 1.4))
    return S


def p01():
    """Plan large, coupé en deux : la maison bleue, la maison jaune."""
    S = Scene()
    hiver_jour(S, 620)
    S.add(rect(0, 0, 400, 620, BLEU_PAPA, opacity=0.25), rect(400, 0, 400, 620, JAUNE_MAMAN, opacity=0.25))
    S.add(maison(190, 620, 1.05, mur="#a5d8ff", toit="#1864ab", porte="#1971c2", volets="#1971c2"))
    S.add(maison(610, 620, 1.05, mur="#ffec99", toit="#e8590c", porte="#e64980", volets="#e64980"))
    S.add(trait(400, 0, 400, 800, "#fff", 6, opacity=0.8))
    S.add(papa(90, 770, 1.05, expr="sourire", bras="coucou", regard=(1, 0)))
    S.add(maman(720, 770, 1.05, expr="sourire", bras="coucou", flip=True, regard=(-1, 0)))
    S.add(gaspard(400, 790, 1.15, sac=True, expr="sourire", bras="ouverts"))
    S.add(texte(200, 200, "chez Papa", 40, "#1864ab", contour="#fff"), texte(610, 200, "chez Maman", 40, "#e8590c", contour="#fff"))
    S.cachette(250, 780)
    return S


def p02():
    """Plan moyen : la maîtresse raconte la fête des Rois."""
    S = Scene()
    interieur(S, "#fff9db", "#d9a066", 600, plinthe="#c68642")
    S.add(rect(220, 80, 380, 230, "#8d5524", rx=8), rect(232, 92, 356, 206, "#2b8a3e", rx=4))
    S.add(place(galette(0, 0, 1.0), 330, 230, 0.8), place(couronne_carton(0, 0, 1.0), 490, 210, 0.7), feve(410, 270, 1.4))
    S.add(personne(130, 760, 1.15, expr="rire", bras="designe", regard=(1, -0.3), **SOPHIE))
    for k, x in enumerate((330, 470, 610)):
        S.add(personne(x, 790, 0.95, expr=("rire", "joie", "rire")[k], bras="leve_doigt", flip=k == 1, regard=(-1, -0.3), **ELEVES[k]))
    S.add(gaspard(730, 795, 0.95, expr="inquiet", bras="bas", regard=(-1, 0)))
    S.cachette(30, 780)
    return S


def p03():
    """Gros plan : « Je la fête où, moi ? »"""
    S = Scene()
    interieur(S, "#fff9db", "#d9a066", 600, plinthe="#c68642")
    S.add(gaspard(400, 800, 1.6, expr="inquiet", bras="joues", regard=(0, -0.3)))
    contenu = g([maison(-70, 40, 0.42, mur="#a5d8ff", toit="#1864ab", porte="#1971c2", cheminee=False),
                 maison(80, 40, 0.42, mur="#ffec99", toit="#e8590c", porte="#e64980", cheminee=False),
                 texte(6, -10, "?", 64, "#e8590c", contour="#fff")])
    S.add(pensee(560, 310, 130, place(contenu, 560, 310, 0.9), depuis=(470, 440)))
    S.camera(1.2, 450, 470)
    S.cachette(90, 760)
    return S


def p04():
    """Plan moyen : la galette chez Papa ; la fève cachée."""
    S = Scene()
    cuisine_papa(S, 600)
    S.add(papa(500, 700, 1.25, expr="malin", bras="tend", flip=True, regard=(-1, 0.6),
               objet=feve(*ancre(96, -104, "tend", "adulte", "fine"), 1.0)))
    S.add(gaspard(250, 710, 1.15, expr="rire", bras="yeux"))
    S.add(table(400, 800, 560, 130, "#a0693a", nappe="#d0ebff"))
    S.add(ellipse(400, 655, 110, 30, "#f6d38b"), ellipse(400, 650, 84, 22, "#fff3bf"))
    S.add(rect(560, 625, 90, 30, "#868e96", rx=12), rect(550, 634, 110, 12, "#495057", rx=6))
    S.add(texte(230, 420, "Je ne triche pas !", 26, "#2f9e44", contour="#fff", rot=-6))
    S.cachette(770, 790)
    return S


def p05():
    """Plan moyen : sous la table ; « Celle-là, pour qui ? »"""
    S = Scene()
    cuisine_papa(S, 600)
    S.add(papa(470, 680, 1.25, expr="rire", bras="tient", regard=(0, 1),
               objet=couteau(*ancre(68, -146, "tient", "adulte", "fine"), 1.0, rot=160)))
    S.add(table(400, 760, 560, 200, "#a0693a"))
    S.add(galette(400, 545, 0.9, part=True))
    # Gaspard sous la table : on le voit sous le bord de la nappe
    cid = uid("dessous")
    S.add(el("clipPath", rect(0, 690, 800, 110, "#000"), id=cid))
    S.add(g(gaspard(300, 900, 1.0, expr="rire", bras="leve_doigt", regard=(1, -1)), clip_path=f"url(#{cid})"))
    S.add(rect(110, 560, 580, 140, "#d0ebff"), chemin("M 110 700 " + " ".join(f"Q {130 + k * 40} 720 {150 + k * 40} 700" for k in range(14)) + " L 690 560 L 110 560 Z", "#d0ebff"))
    S.add(chemin(" ".join(f"M {150 + k * 80} 570 V 700" for k in range(7)), stroke="#a5d8ff", sw=5, opacity=0.6))
    S.add(bulle(220, 140, 320, 90, "Celle-là, pour qui ?", 30, pointe=(420, 400)))
    S.add(bulle(620, 760, 220, 60, "Pour Papa !", 28, pointe=(330, 760)))
    S.cachette(40, 790)
    return S


def p06():
    """Gros plan : la fève !"""
    S = Scene()
    cuisine_papa(S, 600)
    S.add(gaspard(400, 800, 1.6, expr="bouche_bee", bras="montre", regard=(1, -0.5),
                  objet=feve(86, -132, 1.4)))
    S.add(g([cercle(400 + dx, 800 - 1.6 * 125 + dy, 3, "#f0b84d") for dx, dy in ((-30, 0), (24, 6), (-18, 10), (34, -6))]))
    S.add(paillettes(570, 560, 0.8))
    S.camera(1.35, 450, 520)
    S.dessus(texte(560, 120, "LA FÈVE !", 64, OR_, contour="#7c4a1e", rot=-6))
    S.cachette(110, 760)
    return S


def p07():
    """Plan moyen : deux rois dans la cuisine."""
    S = Scene()
    cuisine_papa(S, 600)
    S.add(table(620, 790, 300, 120, "#a0693a", nappe="#d0ebff"))
    S.add(galette(620, 658, 0.7, part=True))
    S.add(papa(420, 790, 1.25, acc=("couronne",), expr="rire", bras="ouverts", regard=(-1, 0), flip=True))
    S.add(gaspard(230, 790, 1.2, couronnes=1, expr="rire", bras="designe", regard=(1, 0)))
    S.add(bulle(330, 130, 420, 100, "Je choisis… un roi !\nToi, Papa !", 32, pointe=(250, 440)))
    S.cachette(770, 790)
    return S


def p08():
    """Plan large : le voyage du dimanche, jusqu'à la maison jaune."""
    S = Scene()
    hiver_jour(S, 600, graine=6)
    S.add(maison(560, 610, 1.15, mur="#ffec99", toit="#e8590c", porte="#e64980", volets="#e64980"))
    S.add(sapin(330, 620, 0.7, neige=True), sapin(780, 630, 0.8, neige=True))
    S.add(chemin("M 0 720 Q 400 690 800 700 L 800 800 L 0 800 Z", "#dee2e6"))
    S.add(voiture(160, 740, 0.85, "#1971c2"))
    S.add(papa(120, 780, 0.95, expr="sourire", bras="coucou", regard=(1, 0)))
    S.add(gaspard(380, 780, 1.0, couronnes=1, sac=True, expr="rire", bras="court", regard=(1, 0)))
    S.add(maman(560, 770, 1.05, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.cachette(770, 790)
    return S


def p09():
    """Plan moyen : chez Maman, le gâteau des rois."""
    S = Scene()
    cuisine_maman(S, 600)
    S.add(maman(560, 700, 1.25, expr="rire", bras="ouverts", regard=(-1, 0.4), flip=True))
    S.add(mamie(700, 710, 1.15, expr="content", bras="mains_jointes", regard=(-1, 0.4)))
    S.add(table(470, 800, 520, 130, "#a0693a", nappe="#fff3bf"))
    S.add(gateau_rois(470, 668, 1.0))
    S.add(gaspard(200, 790, 1.15, couronnes=1, expr="bouche_bee", bras="joues", regard=(1, 0)))
    S.add(bulle(320, 140, 420, 100, "Une fève pour le roi…\net un pois pour la reine !", 28, pointe=(690, 440)))
    S.cachette(30, 790)
    return S


def fourchette(x, y, s=1.0, rot=0):
    return place([rect(-4, 0, 8, 70, "#adb5bd", rx=3), rect(-12, -26, 24, 28, "#adb5bd", rx=3),
                  rect(-10, -40, 4, 16, "#adb5bd"), rect(-2, -40, 4, 16, "#adb5bd"), rect(6, -40, 4, 16, "#adb5bd")], x, y, s, rot=rot)


def p10():
    """Gros plan : c'est le pois !"""
    S = Scene()
    cuisine_maman(S, 600)
    S.add(maman(170, 790, 1.35, expr="rire", bras="applaudit", regard=(1, 0)))
    S.add(mamie(650, 790, 1.3, expr="rire", bras="joues", regard=(-1, 0), flip=True))
    hx, hy = mains_personne(410, 800, 1.55, "montre")[1]
    S.add(gaspard(410, 800, 1.55, couronnes=1, expr="rire", bras="montre", regard=(1, -0.5),
                  objet=fourchette(86, -110, 1.1, rot=0)))
    S.add(pois(hx + 2, hy - 64, 1.6))
    S.camera(1.25, 420, 520)
    S.dessus(texte(600, 110, "Le pois !", 56, "#2f9e44", contour="#fff", rot=-6))
    S.cachette(156, 328, "air")
    return S


def telephone(x, y, s=1.0):
    """Téléphone de Maman : Papa à l'écran, sa couronne sur la tête."""
    ecran = personne(0, 0, 1.0, **{**PAPA, "acc": ("couronne",), "expr": "rire", "bras": "coucou"})
    cid = uid("tel")
    m = [rect(-60, -110, 120, 220, "#343a40", rx=16), rect(-52, -96, 104, 188, "#d0ebff", rx=6),
         el("clipPath", rect(-52, -96, 104, 188, "#000"), id=cid),
         g(place(ecran, 0, 210, 0.85), clip_path=f"url(#{cid})")]
    return place(m, x, y, s)


def p11():
    """Plan moyen : l'appel du soir ; deux couronnes."""
    S = Scene()
    cuisine_maman(S, 600)
    S.ambiance("interieur")
    S.add(maman(600, 790, 1.25, expr="content", bras="tient", flip=True, regard=(-1, 0),
                objet=telephone(*ancre(68, -146, "tient", "adulte"), 0.8)))
    S.add(gaspard(330, 790, 1.3, couronnes=2, expr="rire", bras="designe", regard=(1, -0.3)))
    S.add(bulle(300, 130, 400, 100, "Papa, regarde !\nJ'ai deux couronnes !", 30, pointe=(330, 400)))
    S.cachette(30, 790)
    return S


def p12():
    """Gros plan : Gaspard s'endort ; les deux couronnes au montant du lit."""
    S = Scene()
    piece(S, "chambre", 600)
    S.ambiance("nuit")
    S.add(fenetre(560, 110, 160, 150, "#1c2a52", nuit_=True, rideaux="#e64980"))
    S.add(lampe(720, 610, 0.9))
    S.add(lit(420, 780, 520, "#fff9db", "#ffd43b"))
    cid = uid("lit")
    S.add(el("clipPath", rect(0, 0, 800, 676, "#000"), id=cid))
    S.add(g(gaspard(260, 790, 1.35, expr="dort", bras="calin", objet=perso("ours", 0, -30, 0.32, habit="#e8590c", expr="dort", ombre=False)),
            clip_path=f"url(#{cid})"))
    S.add(rect(200, 660, 460, 90, volume("#ffd43b", 0.3, 0.8), rx=20))
    S.add(couronne_carton(160, 548, 0.6), couronne_carton(160, 590, 0.6))
    S.add(rect(690, 700, 90, 70, volume("#e8590c", 0.3, 0.75), rx=16), rect(700, 740, 70, 20, "#d9480f", rx=8))
    S.add(zzz(380, 420, 0.9))
    S.camera(1.3, 380, 560)
    S.cachette(720, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("couronne-seule.svg", vignette),
    ("01-deux-maisons.svg", p01), ("02-la-maitresse.svg", p02), ("03-ou-ca.svg", p03),
    ("04-chez-papa.svg", p04), ("05-sous-la-table.svg", p05), ("06-crac.svg", p06),
    ("07-roi-chez-papa.svg", p07), ("08-le-voyage.svg", p08), ("09-chez-maman.svg", p09),
    ("10-le-pois.svg", p10), ("11-l-appel.svg", p11), ("12-deux-fois-roi.svg", p12),
]
