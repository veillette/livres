"""La tempête de Noël — une panne de courant, et tout un quartier qui se réchauffe.

La veille de Noël, la tempête souffle sur le village ; clic ! plus de
lumière, plus de four, plus de chauffage. Le gâteau reste à moitié cuit et
Pompon le lapin pleure : « Noël est fichu ! » Monsieur Ours, le vieux voisin,
a un poêle à bois : la famille lapin traverse la rue dans la neige, puis les
Castor et Madame Mouton arrivent à leur tour. Le gâteau cuit sur le poêle,
on chante et on danse aux chandelles. Noël n'est que le décor : l'histoire
parle d'entraide entre voisins.

Plans : 1 moyen (la veille) · 2 large (la tempête) · 3 gros plan (clic !
dans le noir) · 4 moyen (à la bougie) · 5 moyen (Monsieur Ours à la porte) ·
6 large (dans la neige) · 7 moyen (on frappe encore) · 8 large (tous
ensemble) · 9 gros plan (le gâteau sur le poêle) · 10 large (le violon) ·
11 gros plan (le plus beau Noël) · 12 large (le matin).
"""
from base import *
from base import _assombrir
from objets import gateau, bougie, four
from fables import violon, archet
from fetes import lanterne, sapin_decore, boule_noel, guirlande_lumineuse, cadeau

ID = "noel-tempete"
PAPIER_PEINT = "rayures"

NEIGE = "#f1f3f5"
NUIT_H, NUIT_B = "#0f1b3d", "#3d4f86"

POMPON = dict(habit="#e03131", motif="rayures", couleur_motif="#ffc9c9")
MAMAN = dict(couleur="#e8d5c4", visage="#fff4e6", habit="#7048e8", acc=("tablier",))
PAPA = dict(couleur="#ced4da", habit="#1c7ed6", acc=("lunettes",))
OURS = dict(couleur="#8f5f3a", habit="#2b8a3e", acc=("bonnet", "echarpe", "lunettes"), couleur_acc="#e03131")
CASTOR_M = dict(habit="#f08c00", acc=("echarpe",), couleur_acc="#1c7ed6")
CASTOR_P = dict(habit="#ffd43b", acc=("bonnet",), couleur_acc="#1c7ed6")
MOUTON = dict(habit="#e64980", acc=("echarpe",), couleur_acc="#ffd43b")
AGNEAU = dict(habit="#74c0fc", acc=("bonnet",), couleur_acc="#e64980")


def pompon(x, y, s=1.0, **k):
    return perso("lapin", x, y, s, **{**POMPON, **k})


def maman(x, y, s=1.3, **k):
    return perso("lapin", x, y, s, **{**MAMAN, **k})


def papa(x, y, s=1.35, **k):
    return perso("lapin", x, y, s, **{**PAPA, **k})


def ours(x, y, s=1.6, **k):
    return perso("ours", x, y, s, **{**OURS, **k})


def castor(x, y, s=1.2, petit=False, **k):
    return perso("castor", x, y, s, **{**(CASTOR_P if petit else CASTOR_M), **k})


def mouton(x, y, s=1.25, agneau=False, **k):
    return perso("mouton", x, y, s, **{**(AGNEAU if agneau else MOUTON), **k})


def porte_lanterne(S, qui, x, y, s, flip=False, **k):
    """Un personnage qui lève sa lanterne allumée, et son halo."""
    hx = x + (-68 if flip else 68) * s
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=lanterne(68, -146, 0.9), **k))
    S.lumiere(hx, y - 146 * s + 47 * s, 120 * s, "#ffd43b", 0.65)


def tourbillons(S, nb=10, graine=3, zone=(0, 0, 800, 600), couleur="#dbe4ff"):
    """Rafales de vent chargées de neige, en diagonale."""
    r = random.Random(graine)
    for _ in range(nb):
        x, y = r.uniform(zone[0], zone[2]), r.uniform(zone[1], zone[3])
        L = r.uniform(70, 150)
        S.add(chemin(f"M {n(x)} {n(y)} q {n(L / 2)} {n(-18)} {n(L)} {n(10)} q {n(16)} 8 {n(4)} 22",
                     stroke=couleur, sw=r.uniform(3, 5), opacity=0.55))


def tempete(S, sol_y=620, graine=3, collines_=True):
    """Nuit de tempête : ciel bas, neige qui vole, collines blanches."""
    nuit(S, NUIT_H, NUIT_B)
    if collines_:
        collines(S, sol_y - 50, "#b6c2e6", graine=graine, bosquets=False)
    sol(S, sol_y, NEIGE, bosse=14)
    flocons(S, 70, graine, (0, 0, 800, 800))
    tourbillons(S, 9, graine, (0, 40, 700, sol_y - 40))


def fenetre_tempete(x, y, w=170, h=150, rideaux="#e03131"):
    dehors = g([rect(0, 0, 800, 800, NUIT_H),
                *[cercle(x + (k * 37) % w, y + (k * 53) % h, 3 + k % 3, "#fff", opacity=0.8) for k in range(24)],
                chemin(f"M {x} {y + h - 24} Q {x + w / 2} {y + h - 46} {x + w} {y + h - 20} L {x + w} {y + h} L {x} {y + h} Z", "#fff")])
    return fenetre(x, y, w, h, NUIT_H, rideaux=rideaux, contenu=dehors)


def salon_lapins(S, y=620, eteint=False):
    """Le salon de la famille lapin : papier peint rayé, fenêtre sur la neige."""
    interieur(S, "#fff0f6", "#c08552", y, papier="#fcc2d7")
    S.add(fenetre_tempete(540, 110, 180, 160))
    if eteint:
        S.ambiance("nuit")


def poele(x, y, s=1.0, feu=True, gateau_=None):
    """Vieux poêle à bois en fonte, sur pieds, avec son tuyau ; (x, y) = sol."""
    fonte = "#343a40"
    m = [ellipse(0, 0, 120, 12, "#000", opacity=0.15),
         rect(-14, -330, 28, 210, cylindre("#495057", 0.3, 0.7), rx=4) if True else "",
         rect(-20, -150, 40, 16, fonte, rx=4),
         rect(-100, -40, 18, 40, fonte, rx=4), rect(82, -40, 18, 40, fonte, rx=4),
         rect(-110, -140, 220, 104, volume(fonte, 0.25, 0.75), rx=14),
         rect(-120, -150, 240, 18, cylindre("#495057", 0.3, 0.7, vertical=True), rx=6),
         rect(-70, -118, 140, 64, "#1b1b24", rx=30)]
    if feu:
        m += [rect(-62, -110, 124, 50, radial([(0, "#fff3bf"), (0.4, "#ffd43b"), (1, "#e8590c")]), rx=24),
              chemin("M -40 -62 Q -30 -100 -16 -76 Q -6 -108 6 -78 Q 18 -104 30 -66 Z", "#ff922b"),
              chemin("M -20 -62 Q -10 -86 0 -70 Q 10 -88 18 -62 Z", "#fff3bf")]
    m += [cercle(80, -88, 7, "#adb5bd"), trait(-60, -36, 60, -36, "#495057", 4)]
    if gateau_:
        m.append(gateau_)
    return place(m, x, y, s)


def salon_ours(S, y=600):
    """Le petit salon de Monsieur Ours : chaumière, poutres, poêle à bois."""
    piece(S, "chaumiere", y)
    S.ambiance("nuit")
    S.add(fenetre_tempete(560, 120, 160, 140, rideaux="#2b8a3e"))


def bougie_halo(S, x, y, s=1.0):
    S.add(bougie(x, y, s, couleur="#fff3bf"))
    S.lumiere(x, y - 50 * s, 110 * s, "#ffd43b", 0.6)


def couverture_pliee(x, y, s=1.0, c="#4dabf7", c2="#ffd43b"):
    return place([rect(-60, -30, 120, 30, c, rx=8), chemin("M -60 -18 H 60", stroke=c2, sw=5), rect(-56, -50, 112, 22, _assombrir(c, 0.85), rx=8)], x, y, s)


def marmite(x, y, s=1.0):
    return place([ellipse(0, -60, 50, 12, "#868e96"), chemin("M -50 -60 Q -52 0 0 0 Q 52 0 50 -60 Z", volume("#495057", 0.3, 0.75)),
                  chemin("M -50 -50 q -16 0 -16 10 M 50 -50 q 16 0 16 10", stroke="#495057", sw=6),
                  chemin("M -16 -80 q 8 -14 0 -26 M 12 -82 q 8 -14 0 -26", stroke="#fff", sw=4, opacity=0.5)], x, y, s)


def gateau_plat(x, y, s=1.0):
    """Le gâteau à moitié cuit : tout plat, pâle, dans son moule."""
    return place([chemin("M -70 -26 L 70 -26 L 60 0 L -60 0 Z", volume("#adb5bd", 0.3, 0.75)),
                  ellipse(0, -26, 70, 14, "#fff3bf"), ellipse(-20, -28, 14, 4, "#ffe8a3")], x, y, s)


def gateau_gonfle(x, y, s=1.0):
    """Le gâteau qui a fini de cuire : doré et bien gonflé."""
    return place([chemin("M -70 -26 L 70 -26 L 60 0 L -60 0 Z", volume("#adb5bd", 0.3, 0.75)),
                  chemin("M -70 -26 Q -70 -86 0 -88 Q 70 -86 70 -26 Z", volume("#e3a857", 0.4, 0.75)),
                  chemin("M -30 -70 q 10 -10 20 0 M 10 -76 q 10 -10 20 0", stroke="#c68642", sw=3)], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    tempete(S, 640, graine=5)
    S.add(maison(640, 610, 0.55, mur="#ffe8cc", toit="#c92a2a", lumiere=True))
    S.add(sapin(90, 650, 0.9, neige=True), sapin(760, 660, 0.7, neige=True))
    porte_lanterne(S, ours, 560, 760, 1.25, regard=(-1, 0), expr="rire")
    S.add(papa(430, 765, 1.05, expr="sourire", bras="main", regard=(1, 0), pas="marche"))
    S.add(maman(300, 775, 1.0, expr="sourire", bras="main", regard=(1, 0), pas="marche"))
    S.add(pompon(190, 785, 0.85, expr="rire", bras="main", regard=(1, 0), pas="marche", acc=("bonnet", "echarpe"), couleur_acc="#ffd43b"))
    S.add(chemin("M 0 800 L 0 760 Q 100 744 200 768 Q 320 750 420 770 Q 540 752 640 772 Q 720 756 800 768 L 800 800 Z", NEIGE))
    S.cachette(750, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 140, 110, radial([(0, "#ffe066", 0.55), (1, "#ffe066", 0)])))
    S.add(lanterne(200, 40, 2.1))
    return S


def p01():
    """Plan moyen : la veille de Noël ; le sapin, le four, la neige qui tombe."""
    S = Scene()
    salon_lapins(S)
    S.add(guirlande_lumineuse(10, 60, 790, 60, creux=22, nb=14))
    S.add(four(110, 640, 0.9, allume=True, gateau_dedans=True, ouvert=False))
    S.add(maman(280, 760, 1.3, expr="content", bras="tient", regard=(-1, 0), flip=True))
    S.add(tapis(560, 720, 220, 40, "#ffc9c9", "#e03131"))
    S.add(sapin_decore(560, 690, 1.25))
    S.add(cadeau(470, 720, 0.45, "#4dabf7"), cadeau(660, 725, 0.4, "#ffd43b", "#e03131"))
    S.add(pompon(420, 780, 1.1, expr="content", bras="tient", regard=(1, -0.5), objet=boule_noel(68, -146, 16, "#e03131")))
    S.cachette(770, 770)
    return S


def p02():
    """Plan large : la tempête sur le village."""
    S = Scene()
    nuit(S, NUIT_H, NUIT_B)
    collines(S, 520, "#b6c2e6", graine=4, bosquets=False)
    sol(S, 600, NEIGE, bosse=16)
    for k, (x, y, s, mur, toit) in enumerate(((140, 590, 0.6, "#ffe8cc", "#c92a2a"), (380, 570, 0.5, "#e7f5ff", "#1c7ed6"),
                                               (600, 600, 0.65, "#fff3bf", "#5f3dc4"))):
        S.add(maison(x, y, s, mur=mur, toit=toit, lumiere=True, cheminee=k != 1))
    for x, y, s in ((40, 640, 0.9), (720, 650, 1.0), (280, 620, 0.6)):
        S.add(place(sapin(0, 0, s, neige=True), x, y, 1.0, rot=12))
    flocons(S, 110, 7, (0, 0, 800, 800))
    tourbillons(S, 16, 7, (0, 40, 760, 600))
    S.add(texte(250, 230, "Hou… hou…", 52, "#dbe4ff", contour=NUIT_H, rot=-10))
    S.add(texte(560, 320, "HOUUU !", 64, "#ffffff", contour=NUIT_H, rot=-14))
    S.cachette(770, 770)
    return S


def yeux_noir(x, y, s=1.0, regard=(0, 0)):
    """Deux grands yeux qui brillent dans le noir."""
    dx, dy = regard
    return place([ellipse(-22, 0, 17, 22, "#fff"), ellipse(22, 0, 17, 22, "#fff"),
                  cercle(-22 + dx * 6, 4 + dy * 6, 9, ENCRE), cercle(22 + dx * 6, 4 + dy * 6, 9, ENCRE),
                  cercle(-25 + dx * 6, 0 + dy * 6, 3, "#fff"), cercle(19 + dx * 6, 0 + dy * 6, 3, "#fff")], x, y, s)


def p03():
    """Gros plan, dans le noir : clic !"""
    S = Scene()
    fond(S, "#0b1022")
    S.ambiance("sombre")
    # la fenêtre, à peine bleutée par la neige : seule chose qu'on devine
    S.add(fenetre_tempete(560, 160, 180, 160, rideaux="#3b2a5e"))
    S.add(rect(0, 0, 800, 800, "#0b1022", opacity=0.55))
    S.add(rect(520, 330, 260, 16, "#495057"))
    S.add(yeux_noir(250, 420, 1.6, (1, 0)), yeux_noir(420, 330, 1.3, (-1, 0.5)), yeux_noir(330, 560, 1.0, (0, -1)))
    S.add(texte(400, 160, "CLIC !", 90, "#ffd43b", contour="#0b1022", rot=-6))
    S.cachette(740, 330)
    return S


def p04():
    """Plan moyen : à la lueur de la bougie ; « Noël est fichu ! »"""
    S = Scene()
    salon_lapins(S, eteint=True)
    S.add(rect(0, 0, 800, 800, "#0b1022", opacity=0.35))
    S.add(papa(170, 760, 1.3, expr="inquiet", bras="tient", regard=(1, 0), objet=bougie(68, -146, 0.9, couleur="#fff3bf")))
    S.lumiere(170 + 68 * 1.3, 760 - (146 + 45) * 1.3, 220, "#ffd43b", 0.6)
    S.add(maman(620, 760, 1.3, expr="triste", bras="porte", regard=(-1, 0), flip=True, objet=gateau_plat(0, -66, 0.75)))
    couv = chemin("M -70 -10 Q -80 -120 0 -140 Q 80 -120 70 -10 Z", volume("#4dabf7", 0.3, 0.75))
    S.add(pompon(400, 790, 1.2, expr="pleure", larmes=True, bras="bas", derriere=couv))
    S.add(bulle(400, 160, 360, 90, "Noël est fichu !", 38, pointe=(400, 470)))
    S.cachette(40, 770)
    return S


def p05():
    """Plan moyen : Monsieur Ours à la porte, dans la tempête."""
    S = Scene()
    salon_lapins(S, eteint=True)
    S.add(rect(0, 0, 800, 800, "#0b1022", opacity=0.3))
    # la porte grande ouverte sur la nuit blanche
    S.add(rect(80, 150, 300, 470, NUIT_H))
    S.add(g([cercle(90 + (k * 41) % 290, 160 + (k * 67) % 440, 3 + k % 3, "#fff", opacity=0.85) for k in range(40)]))
    S.add(rect(80, 560, 300, 60, NEIGE))
    S.add(rect(68, 140, 324, 14, "#8d5524"), rect(68, 140, 12, 480, "#8d5524"), rect(380, 140, 12, 480, "#8d5524"))
    porte_lanterne(S, ours, 230, 640, 1.35, expr="rire", regard=(1, 0))
    S.add(g([ellipse(230 + dx, 640 - 240 * 1.35 + dy, 20, 8, "#fff") for dx, dy in ((-40, 30), (30, 26), (0, 18))]))
    S.add(papa(520, 770, 1.25, expr="surpris", bras="bas", regard=(-1, 0), flip=True))
    S.add(maman(680, 775, 1.2, expr="sourire", bras="mains_jointes", regard=(-1, 0)))
    S.add(pompon(430, 790, 0.95, expr="surpris", bras="bas", regard=(-1, -0.5)))
    S.add(bulle(560, 140, 360, 110, "J'ai un poêle à bois.\nVenez !", 32, pointe=(330, 380)))
    S.cachette(30, 780)
    return S


def p06():
    """Plan large : la traversée, dans la neige jusqu'aux genoux."""
    S = Scene()
    tempete(S, 600, graine=9)
    S.add(maison(140, 590, 0.55, mur="#fff0f6", toit="#c92a2a", lumiere=False))
    S.add(maison(660, 580, 0.6, mur="#ffe8cc", toit="#2f9e44", lumiere=True))
    S.add(sapin(380, 600, 0.6, neige=True))
    porte_lanterne(S, ours, 610, 720, 1.05, regard=(1, 0), expr="concentre", pas="marche")
    S.add(papa(470, 735, 0.95, expr="concentre", bras="porte", regard=(1, 0), objet=gateau_plat(0, -66, 0.6)))
    S.add(maman(330, 745, 0.9, expr="concentre", bras="main", regard=(1, 0), pas="marche"))
    S.add(pompon(220, 755, 0.75, expr="inquiet", bras="main", regard=(1, -0.3), pas="marche", acc=("bonnet", "echarpe"), couleur_acc="#ffd43b"))
    # la neige épaisse, devant les jambes
    S.add(chemin("M 0 800 L 0 720 Q 120 700 220 724 Q 330 700 420 716 Q 520 694 620 712 Q 720 696 800 708 L 800 800 Z",
                 lineaire([(0, "#ffffff"), (1, "#dbe4ff")])))
    S.add(texte(130, 160, "Brrr…", 44, "#dbe4ff", contour=NUIT_H, rot=-8))
    S.cachette(760, 780)
    return S


def p07():
    """Plan moyen : on frappe encore ; les Castor et Madame Mouton."""
    S = Scene()
    salon_ours(S)
    S.add(poele(120, 640, 0.8))
    S.lumiere(120, 560, 170, "#ff922b", 0.6)
    # la porte ouverte, et ceux qui arrivent dans la neige
    S.add(rect(330, 150, 420, 450, NUIT_H))
    S.add(g([cercle(340 + (k * 47) % 400, 160 + (k * 61) % 420, 3 + k % 3, "#fff", opacity=0.85) for k in range(40)]))
    S.add(rect(330, 540, 420, 60, NEIGE))
    S.add(rect(318, 140, 444, 14, "#6d4424"), rect(318, 140, 12, 460, "#6d4424"), rect(750, 140, 12, 460, "#6d4424"))
    S.add(castor(400, 640, 1.0, expr="sourire", bras="porte", regard=(-1, 0), objet=couverture_pliee(0, -60, 0.6)))
    S.add(castor(480, 650, 0.7, petit=True, expr="joie", bras="coucou", regard=(-1, 0)))
    S.add(mouton(600, 640, 1.05, expr="rire", bras="porte", regard=(-1, 0), objet=marmite(0, -40, 0.6)))
    S.add(mouton(690, 650, 0.62, agneau=True, expr="sourire", bras="bas"))
    S.add(mouton(530, 655, 0.55, agneau=True, expr="joie", bras="haut"))
    S.add(ours(240, 790, 1.4, expr="rire", bras="ouverts", regard=(1, 0)))
    S.add(bulle(560, 90, 360, 90, "Entrez, entrez !", 36, pointe=(300, 380)))
    S.cachette(770, 780)
    return S


def p08():
    """Plan large : le petit salon plein comme un œuf."""
    S = Scene()
    salon_ours(S, 560)
    S.add(poele(110, 610, 0.75))
    S.lumiere(110, 540, 170, "#ff922b", 0.6)
    S.add(tapis(420, 720, 360, 70, "#ffd8a8", "#e8590c"))
    bougie_halo(S, 400, 470, 0.8)
    S.add(rect(320, 470, 160, 12, "#8d5524"))
    S.add(papa(240, 680, 1.0, expr="rire", bras="hanches", regard=(1, 0)))
    S.add(mouton(370, 680, 1.0, expr="rire", bras="mains_jointes", regard=(-1, 0)))
    S.add(castor(520, 680, 1.0, expr="content", bras="calin", regard=(1, 0)))
    S.add(ours(660, 690, 1.25, expr="rire", bras="hanches", regard=(-1, 0)))
    S.add(couverture_pliee(290, 760, 0.9, "#ffd43b", "#e03131"), couverture_pliee(560, 770, 0.9, "#4dabf7", "#fff"))
    S.add(pompon(330, 790, 0.85, expr="rire", bras="haut", regard=(1, 0)))
    S.add(castor(470, 790, 0.6, petit=True, expr="rire", bras="applaudit", regard=(-1, 0)))
    S.add(mouton(590, 790, 0.55, agneau=True, expr="joie", bras="saute"))
    S.add(maman(170, 790, 1.05, expr="content", bras="calin", regard=(1, 0)))
    S.cachette(770, 780)
    return S


def p09():
    """Gros plan : le gâteau qui cuit sur le poêle."""
    S = Scene()
    salon_ours(S, 600)
    S.add(poele(400, 760, 1.4, gateau_=gateau_gonfle(0, -150, 1.0)))
    S.lumiere(400, 620, 240, "#ff922b", 0.6)
    for k in range(3):
        S.add(chemin(f"M {360 + k * 40} 450 q 14 -24 0 -48 q -14 -24 0 -48", stroke="#fff", sw=5, opacity=0.5))
    S.add(pompon(180, 790, 1.15, expr="miam", bras="joues", regard=(1, -1)))
    S.add(castor(630, 790, 0.95, petit=True, expr="miam", bras="mains_jointes", regard=(-1, -1)))
    S.camera(1.25, 400, 560)
    S.dessus(texte(400, 110, "Mmm…", 64, "#ffd43b", contour=NUIT_H))
    S.cachette(60, 790)
    return S


def p10():
    """Plan large : le violon de Monsieur Ours ; on danse en rond."""
    S = Scene()
    salon_ours(S, 560)
    S.add(poele(90, 600, 0.65))
    S.lumiere(90, 540, 150, "#ff922b", 0.55)
    bougie_halo(S, 700, 440, 0.7)
    S.add(rect(640, 440, 120, 12, "#8d5524"))
    S.add(ours(190, 760, 1.25, expr="chante", bras="porte", regard=(1, 0),
               objet=g([violon(-14, -96, 0.9, rot=-60), archet(34, -104, 0.8, rot=30)])))
    S.add(notes(300, 330, 1.1, "#ffd43b"), notes(380, 260, 0.9, "#ffd43b"), notes(170, 300, 0.8, "#ffd43b"))
    # la ronde des grands, puis celle des petits, main dans la main
    S.add(mouton(420, 680, 0.9, expr="rire", bras="main", regard=(1, 0), pas="pointe"))
    S.add(maman(540, 680, 0.95, expr="rire", bras="ouverts", pas="pointe"))
    S.add(castor(660, 680, 0.9, expr="rire", bras="main", flip=True, regard=(-1, 0), pas="pointe"))
    S.add(mouton(410, 790, 0.6, agneau=True, expr="rire", bras="main", regard=(1, 0), pas="pointe"))
    S.add(pompon(530, 790, 0.8, expr="rire", bras="ouverts", regard=(0, 0), pas="pointe"))
    S.add(castor(650, 790, 0.6, petit=True, expr="rire", bras="main", flip=True, regard=(-1, 0), pas="pointe"))
    S.cachette(30, 780)
    return S


def p11():
    """Gros plan : Pompon s'endort, blotti contre Maman."""
    S = Scene()
    salon_ours(S, 600)
    S.add(poele(110, 660, 0.7))
    S.lumiere(140, 560, 260, "#ff922b", 0.6)
    couv = chemin("M -120 -20 Q -130 -160 0 -170 Q 130 -160 120 -20 Z", volume("#4dabf7", 0.3, 0.75))
    S.add(maman(470, 790, 1.5, expr="content", bras="calin", regard=(-1, 0.3), derriere=couv))
    S.add(pompon(380, 800, 1.2, expr="dort", bras="calin", regard=(1, 0)))
    S.add(chemin("M 240 800 Q 250 690 380 690 Q 520 690 540 800 Z", volume("#ffd43b", 0.3, 0.75)))
    S.add(chemin("M 260 740 H 520 M 252 770 H 532", stroke="#e03131", sw=6, opacity=0.6))
    S.add(zzz(230, 560, 0.9))
    S.camera(1.35, 420, 560)
    S.dessus(bulle(560, 110, 400, 100, "C'est le plus beau\nde tous les Noëls.", 32, pointe=S.vers_page(380, 560)))
    S.cachette(700, 760)
    return S


def bonhomme_neige(x, y, s=1.0):
    m = [ellipse(0, -60, 70, 62, volume("#ffffff", 0.1, 0.85)), ellipse(0, -160, 52, 48, volume("#ffffff", 0.1, 0.85)),
         ellipse(0, -240, 38, 36, volume("#ffffff", 0.1, 0.85)),
         chemin("M -36 -206 Q 0 -192 36 -206 L 34 -194 Q 0 -180 -34 -194 Z", "#e03131"), rect(14, -200, 16, 50, "#e03131", rx=5),
         cercle(-12, -250, 4, ENCRE), cercle(12, -250, 4, ENCRE), poly([(0, -240), (36, -232), (0, -230)], "#ff922b"),
         chemin("M -14 -222 Q 0 -214 14 -222", stroke=ENCRE, sw=3), cercle(0, -170, 5, ENCRE), cercle(0, -145, 5, ENCRE),
         chemin("M -48 -170 L -110 -210", stroke="#6d4424", sw=6), chemin("M 48 -170 L 110 -200", stroke="#6d4424", sw=6),
         rect(-34, -300, 68, 36, ENCRE, rx=4), rect(-46, -270, 92, 10, ENCRE, rx=4),
         occuper(-110, -310, 110, 0)]
    return place(m, x, y, s)


def p12():
    """Plan large : le matin de Noël, sous le soleil ; le bonhomme de neige."""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(680, 110, 50))
    collines(S, 520, "#e7f5ff", graine=6, bosquets=False)
    sol(S, 600, NEIGE, bosse=14)
    S.add(maison(170, 600, 0.75, mur="#ffe8cc", toit="#2f9e44", lumiere=True))
    S.add(maison(560, 580, 0.55, mur="#fff0f6", toit="#c92a2a", lumiere=True))
    S.add(sapin(380, 610, 0.7, neige=True), sapin(760, 620, 0.8, neige=True))
    S.add(bonhomme_neige(420, 760, 1.0))
    S.add(ours(240, 760, 1.15, expr="rire", bras="tend", regard=(1, 0)))
    S.add(castor(590, 760, 0.95, expr="rire", bras="coucou", regard=(-1, 0)))
    S.add(mouton(710, 770, 0.95, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(papa(90, 780, 0.95, expr="rire", bras="hanches", regard=(1, 0)))
    S.add(mouton(170, 795, 0.5, agneau=True, expr="rire", bras="lance"))
    S.add(pompon(320, 795, 0.75, expr="rire", bras="saute", regard=(1, 0), acc=("bonnet", "echarpe"), couleur_acc="#ffd43b"))
    S.add(castor(530, 800, 0.55, petit=True, expr="rire", bras="ramasse"))
    S.add(bulle(330, 150, 420, 90, "Joyeux Noël, les voisins !", 34))
    S.cachette(730, 220, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lanterne-seule.svg", vignette),
    ("01-la-veille.svg", p01), ("02-la-tempete.svg", p02), ("03-clic.svg", p03),
    ("04-fichu.svg", p04), ("05-monsieur-ours.svg", p05), ("06-dans-la-neige.svg", p06),
    ("07-on-frappe.svg", p07), ("08-tous-ensemble.svg", p08), ("09-le-gateau.svg", p09),
    ("10-le-violon.svg", p10), ("11-le-plus-beau.svg", p11), ("12-joyeux-noel.svg", p12),
]
