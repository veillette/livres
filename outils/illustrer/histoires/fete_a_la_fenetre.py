"""La fête à la fenêtre — malade le jour de l'An, et la famille qui vient à elle.

Le matin du jour de l'An, Romane a de la fièvre : elle reste au lit avec
Papa pendant que Maman et Louis partent fêter chez Grand-papa. Une
pancarte « BONNE ANNÉE » à colorier, une sieste, un appel sur la tablette…
et le soir, toute la famille vient chanter dans la neige sous sa fenêtre, en
laissant un panier sur le paillasson (pour ne pas attraper sa fièvre). Le
jour de l'An est le décor ; l'histoire parle d'être malade un jour de fête,
et de ceux qui pensent à nous.

Plans : 1 moyen (la fièvre) · 2 gros plan (c'est pas juste) · 3 large (ils
partent) · 4 moyen (la pancarte) · 5 gros plan (la sieste) · 6 moyen
(l'appel) · 7 gros plan (le secret sur la tablette) · 8 large (des lumières
dans la rue) · 9 moyen, vu d'en bas (sous la fenêtre) · 10 moyen (le
panier) · 11 gros plan (la tourtière) · 12 large (la maison dans la nuit).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from objets import bol, lampe_poche
from fetes import lanterne, chapeau_fete, guirlande_lumineuse, cadeau

ID = "fete-a-la-fenetre"
PAPIER_PEINT = "etoiles"

NEIGE = "#f1f3f5"
NUIT_H, NUIT_B = "#14204a", "#4c5b9a"
COUETTE = "#f783ac"

ROMANE = dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#ffd43b", robe=False, jambes="#ffd43b",
              chaussures="#fab005", yeux="cils", nez="petit")
PAPA = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#e8590c", robe=False, jambes="#343a40",
            barbe="#2b2b3a", carrure="ronde", nez="rond")
MAMAN = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="tresses", habit="#1098ad", carrure="fine", yeux="cils",
             nez="pointu")
LOUIS = dict(stature="petit", peau="brune", cheveux="noir", coiffure="courts", habit="#69db7c", robe=False, jambes="#2b8a3e")
GRAND_PAPA = dict(stature="ancien", peau="foncee", cheveux="blanc", coiffure="chauve_cote", habit="#c92a2a", robe=False,
                  jambes="#495057", barbe="#e9ecef", nez="long")
TANTE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="chignon", habit="#ae3ec9", carrure="ronde")
COUSINS = (dict(peau="brune", cheveux="noir", coiffure="couettes", habit="#4dabf7"),
           dict(peau="foncee", cheveux="noir", coiffure="herisses", habit="#ff922b", robe=False, jambes="#364fc7"),
           dict(peau="doree", cheveux="brun", coiffure="queue", habit="#e64980"))


def tuque(c="#e03131", c2="#ffffff"):
    """Tuque à pompon (coiffe d'une personne)."""
    return g([chemin("M -54 -178 Q -56 -240 0 -242 Q 56 -240 54 -178 Z", volume(c, 0.3, 0.75)),
              rect(-58, -194, 116, 22, c2, rx=10), cercle(0, -250, 16, c2)])


def romane(x, y, s=1.15, **k):
    return personne(x, y, s, **{**ROMANE, **k})


def papa(x, y, s=1.15, **k):
    return personne(x, y, s, **{**PAPA, **k})


def toutou(x, y, s=1.0):
    """Le toutou de Romane : un lapin en peluche rose ; (x, y) = bas."""
    return perso("lapin", x, y, 0.36 * s, couleur="#fcc2d7", visage="#fff0f6", habit="#faa2c1", expr="content", ombre=False)


def thermometre(x, y, s=1.0, rot=0):
    return place([rect(-5, -60, 10, 60, "#f8f9fa", rx=5, stroke="#adb5bd", stroke_width=2), rect(-2, -30, 4, 30, "#e03131"),
                  cercle(0, 4, 8, "#e03131")], x, y, s, rot=rot)


def pancarte(x, y, s=1.0, rot=0, finie=True):
    """Grande pancarte « BONNE ANNÉE » coloriée aux feutres ; (x, y) = centre."""
    m = [rect(-170, -70, 340, 140, "#ffffff", rx=6, stroke="#dee2e6", stroke_width=3)]
    lettres = "BONNE" if not finie else "BONNE"
    cols = ("#e03131", "#f08c00", "#2f9e44", "#1c7ed6", "#ae3ec9", "#e64980")
    for k, l in enumerate(lettres):
        m.append(texte(-120 + k * 60, -6, l, 52, cols[k % len(cols)]))
    if finie:
        for k, l in enumerate("ANNÉE"):
            m.append(texte(-120 + k * 60, 56, l, 52, cols[(k + 3) % len(cols)]))
    else:
        m.append(texte(-120, 56, "AN", 52, "#ced4da", anchor="start"))
    m.append(etoile5(150, -50, 12, "#fcc419"))
    return place(m, x, y, s, rot=rot)


def tablette(x, y, s=1.0, contenu=None):
    """Tablette dont l'écran montre la fête chez Grand-papa ; (x, y) = centre."""
    m = [rect(-130, -90, 260, 180, "#343a40", rx=14), rect(-118, -78, 236, 156, "#fff4e6", rx=4)]
    if contenu is not None:
        cid = uid("ecran")
        m.append(el("clipPath", rect(-118, -78, 236, 156, "#000"), id=cid))
        m.append(g(contenu, clip_path=f"url(#{cid})"))
    m.append(cercle(122, 0, 3, "#868e96"))
    return place(m, x, y, s)


def ecran_fete(secret=False):
    """Ce qu'on voit sur la tablette : Grand-papa et les cousins, en fête."""
    m = [rect(-118, -78, 236, 156, "#ffe8cc"), guirlande_lumineuse(-118, -70, 118, -70, creux=8, nb=6)]
    if not secret:
        m.append(place(personne(0, 0, 1.0, expr="rire", bras="coucou", **GRAND_PAPA), -60, 140, 0.55))
    for k, cx in enumerate((10, 70) if not secret else (-60, 10, 80)):
        c = COUSINS[k % len(COUSINS)]
        if secret:
            m.append(place(personne(0, 0, 1.0, expr="malin", bras="chut", **c), cx, 150, 0.62))
        else:
            m.append(place(personne(0, 0, 1.0, expr="rire", bras="haut", coiffe=chapeau_fete(("#e03131", "#4dabf7")[k], y=-198), **c), cx, 150, 0.5))
    return g(m)


def tourtiere(x, y, s=1.0, part=False):
    """Tourtière dorée ; part : une seule pointe, sur une assiette."""
    croute = "#e3a857"
    if part:
        return place([ellipse(0, 0, 60, 14, "#fff", stroke="#dee2e6", stroke_width=2),
                      poly([(-40, -6), (40, -14), (34, -34), (-40, -18)], volume(croute, 0.4, 0.75)),
                      poly([(-40, -6), (40, -14), (40, -4), (-40, 4)], "#a0522d")], x, y, s)
    return place([chemin("M -80 -26 L 80 -26 L 68 0 L -68 0 Z", volume("#adb5bd", 0.3, 0.75)),
                  ellipse(0, -28, 82, 24, volume(croute, 0.4, 0.75)),
                  chemin("M -20 -34 l 8 8 M 0 -38 l 0 12 M 20 -34 l -8 8", stroke=_assombrir(croute, 0.6), sw=4)], x, y, s)


def chambre(S, y=600, soir=False):
    piece(S, "chambre", y)
    if soir:
        S.ambiance("nuit")
        S.add(fenetre(560, 110, 160, 150, NUIT_H, nuit_=True, rideaux="#f783ac"))
    else:
        dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 200, 800, 300, NEIGE), sapin(660, 210, 0.3, neige=True)])
        S.add(fenetre(560, 110, 160, 150, "#d0ebff", rideaux="#f783ac", contenu=dehors))


def au_lit(S, qui, x=380, y=770, w=480, h_couette=650, objets_devant=""):
    """Romane couchée : le lit, le haut du corps au-dessus de la couette."""
    S.add(lit(x, y, w, "#fff0f6", COUETTE))
    cid = uid("lit")
    S.add(el("clipPath", rect(0, 0, 800, h_couette + 16, "#000"), id=cid))
    S.add(g(qui, clip_path=f"url(#{cid})"))
    S.add(rect(x - w / 2 + 40, h_couette, w - 40, y - 40 - h_couette, volume(COUETTE, 0.3, 0.8), rx=20))
    S.add(chemin(f"M {x - w / 2 + 70} {h_couette + 30} q 40 14 80 0 q 40 -14 80 0 q 40 14 80 0", stroke="#fff", sw=4, opacity=0.6))
    if objets_devant:
        S.add(objets_devant)


def rue_nuit(S, sol_y=640):
    nuit(S, NUIT_H, NUIT_B)
    etoiles(S, 34, 6, (0, 0, 800, sol_y - 260))
    collines(S, sol_y - 50, "#c5d0f0", graine=6, bosquets=False)
    sol(S, sol_y, NEIGE, bosse=10)
    flocons(S, 30, 6, (0, 0, 800, sol_y))


def porte_lanterne(S, qui, x, y, s, flip=False, stature="adulte", **k):
    ax, ay = ancre(68, -146, "tient", stature)
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=lanterne(ax, ay, 0.85), **k))
    S.lumiere(x + (-ax if flip else ax) * s, y + (ay + 47) * s, 90 * s, "#ffd43b", 0.65)


def famille(i, x, y, s, **k):
    """Les membres de la famille qui viennent chanter (dans l'ordre)."""
    gens = [(GRAND_PAPA, "ancien"), (MAMAN, "adulte"), (TANTE, "adulte"), (COUSINS[0], "enfant"), (COUSINS[1], "enfant"),
            (LOUIS, "petit"), (COUSINS[2], "enfant")]
    d, stature = gens[i % len(gens)]
    return personne(x, y, s, **{**d, "coiffe": tuque(("#e03131", "#1c7ed6", "#2f9e44", "#fab005", "#ae3ec9", "#f76707", "#e64980")[i % 7]), **k}), stature


# ---------------------------------------------------------------------------

def facade_romane(S, y_sol=720, fenetre_y=160, contenu=None):
    """La façade de la maison de Romane vue d'en bas : sa fenêtre éclairée à l'étage."""
    S.add(rect(140, 40, 520, y_sol - 40, "#e7f5ff"), planches(140, 40, 520, y_sol - 40, "#e7f5ff", larg=26, vertical=False))
    S.add(poly([(110, 60), (400, -60), (690, 60)], "#495057"), rect(110, 40, 580, 24, "#f8f9fa"))
    fx, fy, fw, fh = 240, fenetre_y, 320, 260
    S.add(fenetre(fx, fy, fw, fh, "#ffe8a3", cadre="#ffffff", rideaux="#f783ac", contenu=contenu or ""))
    S.lumiere(400, fy + fh + 40, 260, "#ffd43b", 0.4)
    S.add(rect(fx - 20, fy + fh + 10, fw + 40, 16, "#ffffff"))
    S.add(chemin(f"M {fx - 20} {fy + fh + 12} Q {fx + fw / 2} {fy + fh} {fx + fw + 20} {fy + fh + 12}", stroke=NEIGE, sw=10))


def vue_fenetre(fx=240, fy=160, fw=320, fh=260):
    """Dans la fenêtre : Romane en pyjama, sa pancarte contre la vitre."""
    return g([rect(0, 0, 800, 800, "#ffe8a3"), cadre_mur(fx + 200, fy + 20, 80, 60, "#d0ebff"),
              romane(fx + fw / 2, fy + fh + 20, 1.0, expr="rire", bras="porte", regard=(0, 1)),
              pancarte(fx + fw / 2, fy + fh - 34, 0.6)])


def couverture():
    S = Scene()
    rue_nuit(S, 700)
    facade_romane(S, 740, 120, contenu=g([rect(0, 0, 800, 800, "#ffe8a3"),
                                          romane(400, 470, 1.05, expr="rire", bras="calin", objet=toutou(0, -60, 1.2))]))
    for k, x in enumerate((110, 230, 570, 690)):
        q, st = famille(k, 0, 0, 1.0)
        porte_lanterne(S, lambda xx, yy, ss, **kk: famille(k, xx, yy, ss, **kk)[0], x, 790, 0.95, flip=k >= 2, stature=st,
                       expr="rire", regard=(0, -1))
    S.add(chemin("M 0 800 L 0 770 Q 400 750 800 770 L 800 800 Z", NEIGE))
    S.cachette(400, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(toutou(200, 265, 2.0))
    return S


def p01():
    """Plan moyen : la fièvre ; la robe de fête attend sur la chaise."""
    S = Scene()
    chambre(S)
    # la chaise et la robe de fête
    S.add(rect(680, 520, 14, 200, "#c68642"), rect(770, 520, 14, 200, "#c68642"), rect(670, 600, 124, 16, "#c68642"),
          rect(680, 440, 14, 170, "#c68642"))
    S.add(chemin("M 700 450 L 756 450 L 774 520 Q 790 600 798 620 L 660 620 Q 668 600 684 520 Z", volume("#e64980", 0.3, 0.75)))
    S.add(chemin("M 684 470 Q 728 490 772 470", stroke="#fff", sw=4))
    au_lit(S, romane(400, 734, 1.25, expr="triste", bras="bas", regard=(-1, 0)), x=420, h_couette=640)
    S.add(papa(150, 790, 1.2, expr="inquiet", bras="tient", regard=(1, 0),
               objet=thermometre(*ancre(68, -146, "tient", "adulte", "ronde"), 1.2, rot=20)))
    S.add(bulle(330, 130, 300, 80, "38,9 °C…", 40, pointe=(230, 420)))
    S.cachette(770, 780)
    return S


def p02():
    """Gros plan : « C'est pas juste ! »"""
    S = Scene()
    chambre(S)
    au_lit(S, romane(380, 810, 1.6, expr="pleure", larmes=True, bras="calin", regard=(0, 0), objet=toutou(0, -40, 1.6)),
           x=400, w=640, h_couette=690)
    S.camera(1.35, 400, 560)
    S.dessus(bulle(400, 100, 380, 90, "C'est pas juste !", 40, pointe=S.vers_page(400, 450)))
    S.cachette(90, 780)
    return S


def voiture(x, y, s=1.0, couleur="#1098ad", flip=False):
    m = [ellipse(0, 0, 160, 10, "#000", opacity=0.15),
         chemin("M -150 -28 Q -152 -72 -110 -76 L -70 -78 Q -42 -132 16 -134 L 58 -134 Q 100 -132 122 -82 L 140 -78 "
                "Q 162 -72 162 -40 L 162 -26 Q 162 -14 150 -14 L -140 -14 Q -150 -14 -150 -28 Z", volume(couleur, 0.3, 0.75)),
         chemin("M -56 -82 Q -36 -122 6 -122 L 6 -82 Z", "#a5d8ff"), chemin("M 20 -82 L 20 -122 L 56 -122 Q 92 -120 108 -82 Z", "#a5d8ff"),
         rect(146, -66, 14, 12, "#fff3bf", rx=3), rect(-150, -64, 10, 12, "#fa5252", rx=3),
         chemin("M -40 -128 Q 16 -146 64 -134 Q 30 -136 16 -132 Q -10 -132 -40 -128 Z", "#ffffff")]
    for wx in (-92, 100):
        m += [cercle(wx, -14, 32, "#343a40"), cercle(wx, -14, 15, "#ced4da"), cercle(wx, -14, 5, "#868e96")]
    return place(m, x, y, s, flip=flip)


def p03():
    """Plan large : Maman et Louis partent ; Romane à la fenêtre."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f1f3f5")
    collines(S, 540, "#e7f5ff", graine=4, bosquets=False)
    sol(S, 600, NEIGE, bosse=10)
    S.add(maison(220, 610, 1.15, mur="#e7f5ff", toit="#495057", porte="#d6336c", volets="#d6336c"))
    # Romane, toute petite, le nez à la vitre de la fenêtre de droite
    fx, fy = 220 + 64 * 1.15, 610 - 100 * 1.15
    S.add(cercle(fx, fy + 6, 13, PEAU_ROMANE), cercle(fx, fy - 4, 15, "#2b2b3a"), cercle(fx, fy + 8, 11, PEAU_ROMANE))
    S.add(cercle(fx - 4, fy + 6, 1.8, ENCRE), cercle(fx + 4, fy + 6, 1.8, ENCRE))
    S.add(sapin(60, 620, 0.8, neige=True))
    S.add(chemin("M 380 800 Q 520 680 800 660 L 800 720 Q 560 730 480 800 Z", "#dee2e6"))
    S.add(voiture(600, 720, 0.85, "#1098ad"))
    S.add(personne(470, 770, 1.0, expr="triste", bras="coucou", regard=(-1, -0.5), **MAMAN))
    S.add(personne(400, 780, 0.8, expr="sourire", bras="coucou", regard=(-1, -0.5), **LOUIS))
    S.add(texte(560, 200, "Au revoir…", 40, "#1098ad", contour="#fff", rot=-6))
    S.cachette(30, 780)
    return S


PEAU_ROMANE = "#6f4428"


def p04():
    """Plan moyen : la pancarte, au lit, avec Papa ; la soupe fume."""
    S = Scene()
    chambre(S)
    S.add(rect(80, 560, 120, 160, "#c68642", rx=6), rect(70, 550, 140, 18, "#a0693a", rx=4))
    S.add(bol(140, 550, 0.9, "#4dabf7", "#ffe066"))
    S.add(chemin("M 130 500 q 10 -18 0 -36 M 150 500 q 10 -18 0 -36", stroke="#fff", sw=4, opacity=0.6))
    au_lit(S, romane(380, 750, 1.2, expr="concentre", bras="porte", regard=(0.5, 1)), x=430, w=560, h_couette=660)
    S.add(papa(640, 790, 1.2, expr="content", bras="designe", flip=True, regard=(-1, 1)))
    S.add(pancarte(460, 690, 0.8, rot=-4, finie=False))
    for k, c in enumerate(("#e03131", "#2f9e44", "#1c7ed6", "#ae3ec9")):
        S.add(rect(640 + k * 22, 690, 10, 60, c, rx=4, transform=f"rotate({k * 12 - 10} {645 + k * 22} 720)"))
    S.cachette(240, 70, "air")
    return S


def p05():
    """Gros plan : la sieste ; Papa remonte la couverture."""
    S = Scene()
    chambre(S)
    S.ambiance("interieur")
    au_lit(S, romane(360, 785, 1.4, expr="dort", bras="calin", objet=toutou(0, -40, 1.4)), x=400, w=600, h_couette=680)
    S.add(pancarte(560, 690, 0.5, rot=10, finie=False))
    S.add(papa(650, 800, 1.35, expr="content", bras="tend", flip=True, regard=(-1, 0.6)))
    S.add(zzz(240, 470, 1.0))
    S.camera(1.3, 440, 560)
    S.dessus(texte(560, 120, "Chut…", 50, "#748ffc", contour="#fff"))
    S.cachette(110, 790)
    return S


def p06():
    """Plan moyen : l'appel sur la tablette."""
    S = Scene()
    chambre(S, soir=True)
    S.add(lampe(110, 600, 0.9))
    au_lit(S, romane(400, 750, 1.2, expr="content", bras="porte", regard=(0, 0.3)), x=440, w=560, h_couette=660)
    S.add(papa(650, 790, 1.2, expr="rire", bras="hanches", flip=True, regard=(-1, 0.5)))
    S.add(tablette(410, 600, 0.6, ecran_fete()))
    S.add(bulle(380, 130, 380, 90, "Bonne année, Romane !", 30, pointe=(400, 480)))
    S.cachette(70, 670, "air")
    return S


def p07():
    """Gros plan sur la tablette : les cousins chuchotent un secret."""
    S = Scene()
    chambre(S, soir=True)
    au_lit(S, romane(400, 820, 1.6, expr="surpris", bras="porte", regard=(0, 0.3)), x=400, w=700, h_couette=700)
    S.add(tablette(400, 520, 1.55, ecran_fete(secret=True)))
    S.camera(1.15, 400, 500)
    S.dessus(texte(160, 120, "Chut !", 46, "#d6336c", contour="#fff", rot=-8),
             texte(640, 140, "C'est une surprise !", 30, "#d6336c", contour="#fff", rot=6))
    S.cachette(90, 790)
    return S


def p08():
    """Plan large : des lumières dans la rue, devant la maison."""
    S = Scene()
    rue_nuit(S, 600)
    S.add(maison(620, 610, 0.9, mur="#e7f5ff", toit="#495057", porte="#d6336c", volets="#d6336c", lumiere=True))
    S.add(maison(170, 590, 0.55, mur="#ffe8cc", toit="#c92a2a", lumiere=True))
    S.add(sapin(400, 610, 0.6, neige=True))
    S.add(chemin("M 0 720 Q 400 690 800 700 L 800 760 Q 400 740 0 780 Z", "#dbe4ff"))
    for k, (x, y, s) in enumerate(((80, 760, 0.55), (150, 750, 0.55), (220, 745, 0.6), (290, 740, 0.62), (360, 740, 0.6), (430, 742, 0.5))):
        q, st = famille(k, 0, 0, 1.0)
        porte_lanterne(S, lambda xx, yy, ss, k=k, **kk: famille(k, xx, yy, ss, **kk)[0], 480 - x, y, s * 1.3, stature=st,
                       expr="malin", regard=(1, 0), pas="marche")
    S.cachette(770, 790)
    return S


def p09():
    """Plan moyen, vu d'en bas : la famille chante sous la fenêtre."""
    S = Scene()
    rue_nuit(S, 720)
    facade_romane(S, 740, 110, contenu=vue_fenetre(240, 110, 320, 260))
    S.add(notes(220, 470, 1.0, "#ffd43b"), notes(580, 460, 0.9, "#ffd43b"))
    for k, x in enumerate((90, 200, 320, 480, 600, 710)):
        q, st = famille(k, 0, 0, 1.0)
        fl = k >= 3
        if k == 0:
            hx, hy = ancre(10, -120, "bouche", "ancien")
            S.add(famille(0, x, 800, 1.0, expr="chante", bras="bouche", regard=(0.5, -1),
                          objet=rect(hx - 18, hy - 6, 36, 12, "#adb5bd", rx=3))[0])
            continue
        porte_lanterne(S, lambda xx, yy, ss, k=k, **kk: famille(k, xx, yy, ss, **kk)[0], x, 800, 0.95 if st != "petit" else 1.0,
                       flip=fl, stature=st, expr="chante", regard=(0, -1))
    S.add(texte(400, 470, "Bonne année, Romane !", 34, "#ffd43b", contour=NUIT_H))
    S.cachette(730, 240, "air")
    return S


def panier(x, y, s=1.0):
    """Panier sur le paillasson : tourtière, dessin roulé, petit cadeau."""
    m = [chemin("M -80 -60 Q -80 -150 0 -150 Q 80 -150 80 -60", stroke="#a0693a", sw=9),
         tourtiere(-24, -56, 0.55), cadeau(44, -54, 0.4, "#ae3ec9"),
         place(rect(-10, -60, 20, 70, "#fff", rx=8) + rect(-10, -24, 20, 8, "#e03131"), 10, -60, 1.0, rot=30),
         chemin("M -84 -60 L 84 -60 L 68 0 L -68 0 Z", volume("#c68642", 0.3, 0.75)),
         chemin("M -78 -40 H 78 M -74 -20 H 74", stroke="#8d5524", sw=3, opacity=0.6)]
    return place(m, x, y, s)


def p10():
    """Plan moyen : le panier sur le paillasson ; la famille repart."""
    S = Scene()
    rue_nuit(S, 660)
    # l'entrée de la maison, porte ouverte, et la lumière qui sort
    S.add(rect(0, 120, 300, 560, "#e7f5ff"), planches(0, 120, 300, 560, "#e7f5ff", larg=26, vertical=False))
    S.add(rect(60, 260, 180, 420, "#ffe8a3"), rect(50, 250, 200, 12, "#adb5bd"))
    S.add(poly([(240, 260), (280, 276), (280, 664), (240, 680)], cylindre("#d6336c", 0.2, 0.7)))
    S.lumiere(150, 470, 220, "#ffd43b", 0.55)
    S.lumiere(260, 740, 220, "#ffd43b", 0.45, ry=50)
    S.add(papa(150, 690, 1.25, expr="content", bras="mains_jointes", regard=(1, 0.5)))
    S.add(rect(220, 700, 220, 40, "#8d5524", rx=6))
    S.add(panier(330, 730, 0.95))
    for k, x in enumerate((520, 600, 680, 750)):
        q, st = famille(k, 0, 0, 1.0)
        porte_lanterne(S, lambda xx, yy, ss, k=k, **kk: famille(k, xx, yy, ss, **kk)[0], x, 700, 0.7, stature=st,
                       expr="rire", regard=(-1, 0), pas="marche")
    S.add(bulle(560, 160, 300, 90, "Guéris vite !", 36, pointe=(600, 470)))
    S.cachette(770, 790)
    return S


def dessin_cousins(x, y, s=1.0, rot=-4):
    """Le dessin des cousins : Romane au milieu de toute la famille."""
    m = [rect(-120, -80, 240, 160, "#fff", rx=4, stroke="#dee2e6", stroke_width=3)]
    for k, (cx, c) in enumerate(((-80, "#c92a2a"), (-40, "#1098ad"), (0, "#ffd43b"), (40, "#4dabf7"), (80, "#ff922b"))):
        h = 40 if k == 2 else 52
        m += [cercle(cx, 10 - h, 13, "#6f4428" if k != 2 else "#2b2b3a"), cercle(cx, 12 - h, 10, "#a86a3f"),
              rect(cx - 12, 22 - h, 24, h + 10, c, rx=6)]
    m += [coeur(0, -60, 0.3, "#e64980"), texte(0, 70, "ROMANE", 16, "#d6336c")]
    return place(m, x, y, s, rot=rot)


def p11():
    """Gros plan : la tourtière, et le dessin des cousins."""
    S = Scene()
    chambre(S, soir=True)
    S.add(lampe(110, 600, 0.9))
    au_lit(S, romane(360, 802, 1.5, expr="miam", bras="porte", regard=(1, 0.3)),
           x=400, w=640, h_couette=690, objets_devant=tourtiere(360, 700, 1.0, part=True))
    S.add(dessin_cousins(590, 660, 0.85, rot=8))
    S.camera(1.3, 440, 560)
    S.dessus(texte(200, 140, "Mmm !", 50, "#d6336c", contour="#fff"))
    S.cachette(110, 790)
    return S


def p12():
    """Plan large : la maison dans la nuit, la pancarte à la fenêtre."""
    S = Scene()
    rue_nuit(S, 620)
    S.add(lune(150, 120, 40))
    S.add(maison(400, 640, 1.6, mur="#e7f5ff", toit="#495057", porte="#d6336c", volets="#d6336c", lumiere=True))
    # la pancarte dans la fenêtre de droite
    S.add(place(pancarte(0, 0, 1.0), 400 + 64 * 1.6, 640 - 100 * 1.6, 0.17))
    S.add(sapin(120, 660, 0.9, neige=True), sapin(700, 660, 1.0, neige=True))
    S.add(chemin("M 0 760 Q 400 720 800 740 L 800 780 Q 400 760 0 800 Z", "#dbe4ff"))
    for k, x in enumerate((640, 680, 715, 745)):
        S.add(lanterne(x, 700 - k * 6, 0.35))
        S.lumiere(x, 718 - k * 6, 40, "#ffd43b", 0.6)
    S.cachette(30, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("toutou-seul.svg", vignette),
    ("01-la-fievre.svg", p01), ("02-c-est-pas-juste.svg", p02), ("03-ils-partent.svg", p03),
    ("04-la-pancarte.svg", p04), ("05-la-sieste.svg", p05), ("06-l-appel.svg", p06),
    ("07-le-secret.svg", p07), ("08-des-lumieres.svg", p08), ("09-sous-la-fenetre.svg", p09),
    ("10-le-panier.svg", p10), ("11-la-tourtiere.svg", p11), ("12-la-fete-est-venue.svg", p12),
]
