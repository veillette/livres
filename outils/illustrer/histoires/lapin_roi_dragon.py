"""Le lapin et le Roi Dragon — d'après un conte coréen (Tokki-jeon, Byeoljubu-jeon).

Au fond de la mer de l'Est, le Roi Dragon tombe malade ; le médecin du
palais (ici un poulpe savant) déclare que seul le foie d'un lapin peut le
guérir. La tortue, qui peut aller sur la terre, part chercher un lapin avec
un portrait peint par le crabe du palais. Elle le séduit avec des promesses
(gâteaux de riz, place de ministre) et l'emmène sur son dos. Au palais, le
lapin comprend le piège et invente une ruse : il a laissé son foie sécher
sur un rocher, là-haut. De retour sur la plage, il se moque de la tortue…
puis, pris de pitié, lui donne une racine de ginseng de la montagne, qui
guérit le roi (comme dans les versions où l'esprit de la montagne offre un
remède à la tortue fidèle).

Décors coréens : palais aux toits de tuiles recourbés, colonnes rouges, pins
tordus de la montagne.

Plans : couverture moyen · 1 large (le palais, le roi malade) · 2 gros plan
(le médecin) · 3 moyen (le portrait) · 4 large (la montagne aux pins) ·
5 moyen (les promesses) · 6 moyen en diagonale (la plongée) · 7 large
(l'accueil au palais) · 8 gros plan (ton foie !) · 9 moyen (la ruse) ·
10 large (la plage) · 11 moyen (le rire) · 12 gros plan (le ginseng) ·
13 large (le roi guéri).
"""
from base import *
from base import _assombrir
from fantastique import (ocean, algue, corail, coquillage, bulles_eau, poulpe, crabe, perle, OR, OR_FONCE)
from objets import pinceau
from animaux import plage
from dragons import *

ID = "lapin-roi-dragon"

ROI = dict(couleur="#20c997", ventre="#c3fae8", couronne=OR, moustaches="#fff3bf", barbe="#fff3bf")
LAPIN = dict(couleur="#f1f3f5", visage="#ffffff")
TORTUE = dict(carapace="#2b8a3e", peau="#a9e34b")
ROUGE = "#c92a2a"
TUILE = "#2b8a3e"


def roi_dragon(x, y, s=1.7, **k):
    return dragon_habille(x, y, s, **{**ROI, **k})


def lapin(x, y, s=1.0, **k):
    return perso("lapin", x, y, s, **{**LAPIN, **k})


def tortue_(x, y, s=1.2, **k):
    return tortue(x, y, s, **{**TORTUE, **k})


# --- Personnages et objets ------------------------------------------------------

def medecin(x, y, s=1.0, expr="concentre", regard=(0, 0)):
    """Le médecin du palais : un poulpe à lunettes."""
    m = [poulpe(0, 0, 1.0, "#e599f7", expr=expr, regard=regard)]
    return place(m, x, y, s)


def meduse(x, y, s=1.0, couleur="#fcc2d7"):
    m = [chemin("M -40 0 Q -40 -50 0 -52 Q 40 -50 40 0 Q 20 -8 0 0 Q -20 -8 -40 0 Z", volume(couleur, 0.4, 0.8), opacity=0.85)]
    for k in range(5):
        dx = -28 + k * 14
        m.append(chemin(f"M {dx} -2 q 8 20 0 40 q -8 20 0 40", stroke=couleur, sw=4, opacity=0.8))
    m += [cercle(-12, -26, 3.5, ENCRE), cercle(12, -26, 3.5, ENCRE), chemin("M -6 -16 Q 0 -10 6 -16", stroke=ENCRE, sw=2)]
    return place(m, x, y, s)


def portrait_lapin(x, y, s=1.0, rot=0):
    """Rouleau de papier peint : le portrait du lapin ; (x, y) = centre."""
    m = [rect(-90, -110, 180, 220, "#fff9db", stroke="#e9d8a6", stroke_width=4, rx=4),
         rect(-104, -122, 208, 18, "#a0522d", rx=8), rect(-104, 104, 208, 18, "#a0522d", rx=8),
         place(perso("lapin", 0, 0, 0.5, expr="sourire", **LAPIN), 0, 96)]
    return place(m, x, y, s, rot=rot)


def ginseng(x, y, s=1.0, rot=0):
    """Racine de ginseng : racine claire à petites « jambes », tige, feuilles et
    baies rouges ; (x, y) = haut de la racine."""
    m = [chemin("M 0 0 L 0 -90", stroke="#5c940d", sw=5)]
    for a in (-60, -20, 20, 60):
        m.append(place([ellipse(0, -26, 9, 26, "#74b816"), chemin("M 0 0 L 0 -46", stroke="#5c940d", sw=2)], 0, -90, 1.0, rot=a))
    for bx, by in ((-6, -96), (4, -100), (0, -92), (8, -94)):
        m.append(cercle(bx, by, 6, "#e03131"))
    m += [chemin("M -16 0 Q -24 40 -10 80 Q -2 100 -8 130 M 16 0 Q 24 40 12 80 Q 4 100 14 136", stroke="#e9d8a6", sw=10),
          chemin("M -18 0 Q -22 50 0 70 Q 22 50 18 0 Z", volume("#f3e3c3", 0.3, 0.8)),
          chemin("M -10 20 l 20 0 M -12 36 l 22 0 M -8 52 l 16 0", stroke="#d9c49b", sw=2),
          chemin("M -14 60 Q -40 80 -48 100 M 14 64 Q 36 90 44 98", stroke="#e9d8a6", sw=4)]
    return place(m, x, y, s, rot=rot)


def gateaux_riz(x, y, s=1.0):
    """Assiette de gâteaux de riz colorés (tteok)."""
    m = [ellipse(0, 0, 70, 16, "#f8f9fa", stroke="#ced4da", stroke_width=3)]
    for k, (gx, gy, c) in enumerate([(-34, -10, "#ffc9c9"), (0, -14, "#d8f5a2"), (34, -10, "#fff3bf"),
                                     (-16, -30, "#e5dbff"), (18, -30, "#ffffff")]):
        m.append(ellipse(gx, gy, 18, 12, volume(c, 0.3, 0.85), stroke="#dee2e6", stroke_width=1.5))
    return place(m, x, y, s)


def pin(x, y, s=1.0, graine=1):
    """Pin coréen au tronc tordu et au feuillage en nuages plats ; (x, y) = pied."""
    r = random.Random(graine)
    m = [chemin("M -14 0 Q -30 -90 10 -150 Q 50 -210 0 -280 L 20 -284 Q 70 -210 30 -150 Q -6 -90 14 0 Z", "#7c4a1e"),
         chemin("M 20 -200 Q 70 -220 110 -210", stroke="#7c4a1e", sw=12),
         chemin("M 8 -140 Q -50 -160 -90 -150", stroke="#7c4a1e", sw=10)]
    for cx, cy, rx in ((110, -214, 70), (-90, -156, 66), (10, -290, 80), (40, -240, 50)):
        rx *= r.uniform(0.9, 1.1)
        m.append(ellipse(cx, cy, rx, rx * 0.32, volume("#2b8a3e", 0.25, 0.75)))
        m.append(ellipse(cx, cy - rx * 0.12, rx * 0.8, rx * 0.18, "#40c057", opacity=0.6))
    return place(m, x, y, s)


def montagnes_coree(S, y=520):
    """Montagnes en lignes douces, du lointain au plan moyen."""
    S.add(chemin(f"M 0 {y - 120} Q 120 {y - 300} 260 {y - 190} Q 360 {y - 340} 500 {y - 210} Q 640 {y - 330} 800 {y - 170} L 800 {y} L 0 {y} Z",
                 "#b2d8c6", opacity=0.8))
    S.add(chemin(f"M 0 {y - 40} Q 160 {y - 200} 320 {y - 90} Q 480 {y - 220} 640 {y - 80} Q 720 {y - 140} 800 {y - 60} L 800 {y + 20} L 0 {y + 20} Z",
                 "#8cc5a5"))


def palais_mer(x, y, s=1.0):
    """Palais du Roi Dragon : soubassement de pierre, colonnes rouges, toit de
    tuiles vertes aux coins relevés, à deux étages ; (x, y) = milieu du sol."""
    m = [rect(-300, -40, 600, 40, volume("#dee2e6", 0.2, 0.8)),
         rect(-260, -250, 520, 210, "#fff4e6")]
    for k in range(-2, 3):
        m.append(rect(k * 110 - 12, -250, 24, 210, cylindre(ROUGE, 0.25, 0.7)))
    for k in (-1, 0, 1):
        m.append(rect(k * 110 + 20 - 55, -200, 70, 110, "#fab005" if k == 0 else "#ffe8cc", rx=4, stroke=ROUGE, stroke_width=4))
        m.append(chemin(f"M {k * 110 - 35} -145 h 70 M {k * 110} -200 v 110", stroke=ROUGE, sw=3, opacity=0.6))
    # toit bas
    m.append(rect(-280, -270, 560, 22, "#1098ad"))
    m.append(chemin("M -360 -268 Q -300 -270 -270 -330 L 270 -330 Q 300 -270 360 -268 Q 330 -290 300 -300 L -300 -300 Q -330 -290 -360 -268 Z",
                    volume(TUILE, 0.25, 0.75)))
    m.append(chemin(" ".join(f"M {xx} -330 L {xx * 1.12} -284" for xx in range(-240, 260, 30)), stroke=_assombrir(TUILE, 0.7), sw=3))
    # étage
    m.append(rect(-150, -420, 300, 100, "#fff4e6"))
    for k in (-1, 0, 1):
        m.append(rect(k * 100 - 10, -420, 20, 100, cylindre(ROUGE, 0.25, 0.7)))
    m.append(rect(-170, -436, 340, 18, "#1098ad"))
    m.append(chemin("M -240 -434 Q -190 -436 -160 -490 L 160 -490 Q 190 -436 240 -434 Q 210 -456 190 -464 L -190 -464 Q -210 -456 -240 -434 Z",
                    volume(TUILE, 0.25, 0.75)))
    m.append(chemin(" ".join(f"M {xx} -490 L {xx * 1.12} -446" for xx in range(-140, 160, 28)), stroke=_assombrir(TUILE, 0.7), sw=3))
    m.append(rect(-170, -500, 340, 14, _assombrir(TUILE, 0.8), rx=6))
    m.append(perle(0, -520, 0.7))
    return place(m, x, y, s)


def fond_mer(S, sombre=False, sable=660):
    ocean(S, "#15aabf" if not sombre else "#1864ab", "#0b4f8a", y_sable=sable)
    S.add(algue(60, sable + 30, 1.0, "#2f9e44", graine=2), algue(750, sable + 20, 0.9, "#37b24d", graine=3))
    S.add(corail(150, sable + 40, 0.8, "#ff8787"), corail(680, sable + 50, 0.7, "#f783ac"))


def lit_royal(x, y, s=1.0):
    """Lit du roi : tête de lit en corail, couverture brodée ; renvoie (fond, devant)."""
    fond = place([rect(-200, -300, 400, 300, "#ff8787", rx=60), rect(-180, -280, 360, 260, "#ffa8a8", rx=50),
                  perle(0, -250, 0.8)], x, y, s)
    devant = place([rect(-220, -140, 440, 140, volume("#ffd43b", 0.2, 0.8), rx=24),
                    chemin("M -200 -110 Q 0 -90 200 -110", stroke="#e67700", sw=5),
                    chemin("M -180 -60 l 30 -20 l 30 20 l 30 -20 l 30 20 l 30 -20 l 30 20 l 30 -20 l 30 20 l 30 -20 l 30 20 l 30 -20 l 30 20",
                           stroke=ROUGE, sw=4),
                    rect(-220, -10, 440, 10, "#e67700", rx=4)], x, y, s)
    return fond, devant


def tortue_nage(x, y, s=1.0, rot=0, passager=None, expr="content"):
    """Tortue qui nage, pattes en rames, éventuellement un lapin sur le dos ;
    (x, y) = sous le ventre."""
    m = [place(chemin("M 0 0 Q 40 30 90 20 Q 60 0 0 0 Z", "#82c91e"), 40, -18, 1.0, rot=30),
         place(chemin("M 0 0 Q -40 30 -90 30 Q -60 0 0 0 Z", "#82c91e"), -50, -16, 1.0, rot=-20),
         tortue_(0, 0, 1.0, expr=expr)]
    if passager:
        m.append(passager)
    return place(m, x, y, s, rot=rot)


# --- Pages ----------------------------------------------------------------------

def couverture():
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(400, 620, 0.75))
    S.add(roi_dragon(640, 760, 1.3, expr="content", bras="salut"))
    S.add(tortue_nage(330, 640, 1.5, rot=-8, passager=lapin(0, -110, 0.9, expr="joie", bras="haut")))
    S.add(poisson(130, 300, 0.8, "#ffd43b"), poisson(700, 230, 0.6, "#ff922b", flip=True))
    S.add(bulles_eau(260, 280, 1.0))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(tortue_(200, 262, 1.0))
    S.add(lapin(195, 262 - 110 * 1.0, 0.45, expr="rire", bras="haut"))
    return S


def p01():
    """Plan large : le palais au fond de la mer ; le roi malade dans son lit."""
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(400, 600, 0.95))
    fond, devant = lit_royal(400, 790, 1.0)
    S.add(fond)
    S.add(roi_dragon(400, 760, 1.4, expr="triste", bras="bas"))
    S.add(devant)
    S.add(poisson(120, 520, 0.8, "#ffd43b", expr="inquiet"), poisson(690, 500, 0.7, "#ff922b", expr="inquiet", flip=True))
    S.add(crabe(700, 780, 0.6, expr="inquiet", pinces_haut=False))
    S.add(texte(620, 430, "Keuf ! Keuf !", 40, "#1864ab", contour="#fff"))
    return S


def p02():
    """Gros plan : le médecin poulpe et son remède."""
    S = Scene()
    fond_mer(S)
    fond, devant = lit_royal(560, 790, 1.0)
    S.add(fond)
    S.add(roi_dragon(560, 760, 1.4, expr="inquiet", regard=(-1, 0)))
    S.add(devant)
    S.add(medecin(250, 760, 1.3, expr="fier", regard=(1, 0)))
    S.cachette(150, 420, "poisson")
    S.camera(1.3, 400, 520)
    S.dessus(bulle(330, 110, 560, 110, "Il n'y a qu'un remède :\nle foie d'un lapin !", 34, pointe=S.vers_page(250, 520)))
    return S


def p03():
    """Plan moyen : la tortue part, avec le portrait peint par le crabe."""
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(560, 600, 0.6))
    S.add(tortue_(300, 760, 1.8, expr="fier", regard=(1, 0)))
    S.add(portrait_lapin(560, 560, 1.0, rot=4))
    S.add(crabe(690, 790, 0.9, expr="content"))
    S.add(pinceau(740, 720, 1.2, "#1c7ed6", rot=30))
    S.dessus(bulle(300, 120, 440, 100, "Moi, je peux aller\nsur la terre !", 34, pointe=(340, 520)))
    return S


def p04():
    """Plan large : la montagne aux pins ; le lapin sous un pin."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(160, 110, 0.7), nuage(620, 150, 0.5))
    montagnes_coree(S, 560)
    sol(S, 560, "#a9e34b", couleur2="#94d82d", y2=680)
    S.add(pin(600, 690, 1.3, graine=2), pin(90, 640, 0.8, graine=5))
    S.add(lapin(560, 760, 1.0, expr="miam", bras="bouche"))
    S.add(herbe(500, 770, 1.0), herbe(640, 780, 0.9))
    S.add(tortue_(200, 780, 1.1, expr="surpris", regard=(1, 0)))
    S.add(fleur(380, 740, 0.7, "#ff8787"), fleur(730, 760, 0.8, "#cc5de8"))
    S.dessus(bulle(260, 140, 360, 110, "C'est lui ! Comme\nsur le dessin !", 30, pointe=(220, 600)))
    return S


def p05():
    """Plan moyen : la tortue vante le palais ; le lapin rêve."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    montagnes_coree(S, 560)
    sol(S, 560, "#a9e34b", couleur2="#94d82d", y2=680)
    S.add(pin(720, 680, 1.0, graine=7))
    S.add(tortue_(220, 780, 1.7, expr="malin", regard=(1, 0)))
    S.add(lapin(530, 790, 1.4, expr="joie", bras="joues", regard=(0, -1)))
    reve = g([gateaux_riz(560, 230, 1.0), couronne_simple(640, 190, 2.0, OR), etoile5(500, 170, 14, OR)])
    S.add(pensee(580, 200, 130, reve, depuis=(540, 480)))
    S.dessus(bulle(220, 380, 340, 90, "Des gâteaux de riz,\nune place de ministre…", 26, pointe=(240, 560)))
    return S


def p06():
    """Plan moyen en diagonale : plouf ! la plongée."""
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#74c0fc", "#1864ab"])))
    S._decor("eau")
    S.add(chemin("M 0 140 Q 100 120 200 140 T 400 140 T 600 140 T 800 140 L 800 0 L 0 0 Z", "#d0ebff"))
    S.add(chemin("M 0 140 Q 100 120 200 140 T 400 140 T 600 140 T 800 140", stroke="#ffffff", sw=8))
    for k in range(5):
        S.add(poly([(80 + k * 160, 140), (130 + k * 160, 140), (200 + k * 160, 800), (120 + k * 160, 800)], "#ffffff", opacity=0.06))
    S.add(tortue_nage(420, 520, 1.6, rot=34, passager=lapin(0, -110, 0.85, expr="surpris", bras="haut")))
    S.add(bulles_eau(220, 220, 1.4, nb=6, graine=3), bulles_eau(260, 330, 1.0, nb=4, graine=4))
    S.add(poisson(150, 470, 0.7, "#ffd43b"), poisson(140, 660, 0.6, "#ff922b"))
    S.add(texte(220, 90, "Plouf !", 70, "#1864ab", contour="#fff"))
    S.cachette(680, 680, "poisson")
    return S


def p07():
    """Plan large : l'accueil au palais."""
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(400, 620, 0.9))
    S.add(tortue_(400, 790, 1.4))
    S.add(lapin(400, 790 - 110 * 1.4 + 10, 0.85, expr="bouche_bee", bras="joues"))
    S.add(poisson(120, 480, 0.8, "#ffd43b", expr="rire"), poisson(690, 470, 0.7, "#ff922b", expr="rire", flip=True))
    S.add(meduse(150, 300, 1.0), meduse(660, 260, 0.8, "#d0bfff"))
    S.add(crabe(140, 780, 0.7, expr="rire"), crabe(660, 790, 0.7, "#ff922b", expr="rire"))
    S.add(bulles_eau(500, 300, 1.0, graine=7))
    S.cachette(700, 620, "poisson")
    return S


def p08():
    """Gros plan : « Donne-moi ton foie ! » — le lapin a très peur."""
    S = Scene()
    fond_mer(S, sombre=True)
    S.add(palais_mer(400, 600, 0.95))
    S.add(roi_dragon(560, 800, 1.9, expr="neutre", bras="tend", regard=(-1, 0)))
    S.add(lapin(260, 790, 1.4, expr="oups", bras="bouche", regard=(1, 0)))
    S.cachette(120, 775, "eau")
    S.camera(1.35, 380, 560)
    S.dessus(bulle(520, 110, 500, 110, "Maintenant, petit lapin,\ndonne-moi ton foie !", 32, pointe=S.vers_page(560, 520)))
    return S


def p09():
    """Plan moyen : la ruse du lapin."""
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(400, 600, 0.8))
    S.add(roi_dragon(600, 790, 1.5, expr="surpris", regard=(-1, 0)))
    S.add(lapin(270, 790, 1.35, expr="malin", bras="designe", regard=(1, 0)))
    S.add(tortue_(110, 790, 0.9, expr="surpris", regard=(1, 0)))
    S.add(pensee(260, 150, 120, g([caillou(260, 190, 1.4, "#adb5bd"),
                                   place(chemin("M -30 0 Q -40 -30 -10 -36 Q 0 -50 20 -36 Q 44 -30 30 0 Z", "#c2255c"), 260, 150, 1.0),
                                   soleil(310, 110, 18)]), depuis=(280, 470)))
    S.cachette(440, 70, "air")
    S.dessus(bulle(570, 270, 400, 110, "Mon foie ? Je l'ai laissé\nsécher sur un rocher !", 26, pointe=(330, 520)))
    return S


def p10():
    """Plan large : retour sur la plage ; le lapin saute à terre."""
    S = Scene()
    plage(S, 470)
    S.add(pin(680, 520, 0.9, graine=3), pin(780, 530, 0.7, graine=8))
    S.add(tortue_(250, 620, 1.2, expr="content"))
    S.add(lapin(500, 640, 1.2, expr="rire", bras="haut", pas="saute", rot=-8))
    S.add(mouvement(380, 560, 1.2, rot=200))
    S.add(texte(560, 200, "Hop !", 70, "#e8590c", contour="#fff"))
    return S


def p11():
    """Plan moyen : le lapin, sur son rocher, éclate de rire."""
    S = Scene()
    plage(S, 470)
    S.add(caillou(560, 720, 3.6, "#adb5bd"))
    S.add(lapin(560, 640, 1.3, expr="rire", bras="hanches"))
    S.add(tortue_(200, 760, 1.4, expr="triste", regard=(1, -1)))
    S.dessus(bulle(400, 120, 600, 110, "Personne ne peut sortir son foie\nde son ventre ! Ha ha ha !", 30, pointe=(560, 380)))
    return S


def p12():
    """Gros plan : le lapin offre la racine de ginseng à la tortue."""
    S = Scene()
    plage(S, 470)
    S.add(pin(120, 520, 0.9, graine=4))
    S.add(tortue_(220, 770, 1.8, expr="surpris", regard=(1, -1)))
    S.add(eclat(445, 560, 1.3, "#ffe066"))
    S.add(lapin(600, 780, 1.5, expr="sourire", bras="tend", regard=(-1, 0), flip=True))
    S.add(ginseng(445, 640, 1.1, rot=-8))
    S.camera(1.3, 420, 560)
    S.dessus(bulle(430, 100, 520, 110, "Tiens : du ginseng, le meilleur\nremède de la montagne.", 30, pointe=S.vers_page(560, 520)))
    return S


def p13():
    """Plan large : le roi guéri danse ; tout le palais fait la fête."""
    S = Scene()
    fond_mer(S)
    S.add(palais_mer(400, 600, 0.85))
    S.add(roi_dragon(400, 790, 1.5, expr="rire", bras="danse"))
    S.add(tortue_(170, 790, 1.2, expr="rire", regard=(1, 0)))
    S.add(medecin(650, 790, 0.9, expr="rire"))
    S.add(poisson(130, 460, 0.8, "#ffd43b", expr="rire"), poisson(690, 420, 0.7, "#ff922b", expr="rire", flip=True))
    S.add(meduse(250, 300, 0.8), meduse(560, 250, 0.7, "#d0bfff"))
    S.add(notes(560, 380, 1.0, "#fff3bf"), notes(240, 420, 0.9, "#fff3bf"))
    S.cachette(80, 300, "poisson")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lapin-tortue-seuls.svg", vignette),
    ("01-le-roi-malade.svg", p01), ("02-le-remede.svg", p02), ("03-le-portrait.svg", p03), ("04-la-montagne.svg", p04),
    ("05-les-promesses.svg", p05), ("06-plouf.svg", p06), ("07-le-palais.svg", p07), ("08-ton-foie.svg", p08),
    ("09-la-ruse.svg", p09), ("10-la-plage.svg", p10), ("11-ha-ha-ha.svg", p11), ("12-le-ginseng.svg", p12),
    ("13-le-roi-gueri.svg", p13),
]
