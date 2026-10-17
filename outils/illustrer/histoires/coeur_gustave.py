"""Un cœur pour Monsieur Gustave — une Saint-Valentin à la résidence pour aînés.

La classe d'Anouk offre des cœurs en papier aux aînés de la résidence des
Érables. Monsieur Gustave, seul près de la fenêtre, n'en veut pas. Mais
Anouk reconnaît la mésange à tête noire sur la mangeoire, puis le cardinal :
Monsieur Gustave connaît tous les chants (« fi-bi » !). La semaine suivante,
elle lui apporte une carte au cardinal ; il lui montre la photo de
Lucienne, sa femme, qui aimait les oiseaux. Puis il apprend à la classe à
faire des mangeoires en cocottes de pin. La Saint-Valentin est le décor ;
l'histoire parle de solitude des aînés et d'amitié entre les âges.

Plans : 1 large (la sortie) · 2 moyen (les cœurs) · 3 moyen (pas pour moi) ·
4 gros plan (Anouk) · 5 moyen (une mésange !) · 6 gros plan (la mangeoire) ·
7 moyen (fi-bi) · 8 moyen (la carte au cardinal) · 9 gros plan (Lucienne) ·
10 large (l'atelier des cocottes) · 11 large (dans l'érable) · 12 moyen (mon
ami).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import coeur_papier, carte_coeur

ID = "coeur-gustave"
PAPIER_PEINT = "fleurs"

ROUGE = "#e03131"
NEIGE = "#f8f9fa"

ANOUK = dict(peau="claire", cheveux="noir", coiffure="carre", habit="#e64980", robe=False, jambes="#364fc7", yeux="cils",
             taches=True, nez="retrousse")
GUSTAVE = dict(stature="ancien", peau="rosee", cheveux="gris", coiffure="chauve_cote", habit="#5c7cfa", robe=False,
               jambes="#5c3d2e", nez="long", carrure="fine", acc=("lunettes",))
HELENE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="afro", habit="#2f9e44", carrure="normale", yeux="cils")
YVETTE = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="boucles", habit="#f783ac", carrure="ronde", nez="rond")
PAUL = dict(stature="ancien", peau="foncee", cheveux="blanc", coiffure="courts", habit="#f08c00", robe=False, jambes="#495057",
            barbe="#e9ecef", carrure="normale")
MAMAN = dict(stature="adulte", peau="claire", cheveux="noir", coiffure="queue", habit="#7048e8", carrure="fine", yeux="cils")
ENFANTS = (dict(peau="foncee", cheveux="noir", coiffure="couettes", habit="#ffd43b"),
           dict(peau="doree", cheveux="noir", coiffure="courts", habit="#69db7c", robe=False, jambes="#2b8a3e"),
           dict(peau="rosee", cheveux="blond", coiffure="herisses", habit="#4dabf7", robe=False, jambes="#495057"),
           dict(peau="brune", cheveux="brun", coiffure="queue", habit="#ff922b"))


def casquette_moustache():
    """La casquette de tweed et la grosse moustache de Monsieur Gustave (coiffe)."""
    return g([chemin("M -54 -178 Q -50 -214 0 -216 Q 50 -214 54 -178 Z", volume("#868e96", 0.3, 0.75)),
              chemin("M 30 -184 Q 70 -186 76 -172 Q 50 -170 26 -174 Z", "#495057"),
              chemin("M -2 -130 Q -22 -140 -38 -124 Q -20 -118 -2 -124 Z", "#ced4da"),
              chemin("M 2 -130 Q 22 -140 38 -124 Q 20 -118 2 -124 Z", "#ced4da")])


def anouk(x, y, s=1.15, **k):
    return personne(x, y, s, **{**ANOUK, **k})


def gustave(x, y, s=1.2, **k):
    return personne(x, y, s, **{**GUSTAVE, "coiffe": casquette_moustache(), **k})


def enfant(i, x, y, s=0.95, **k):
    return personne(x, y, s, **{**ENFANTS[i % len(ENFANTS)], **k})


# --- Oiseaux d'hiver (de profil, tête à droite) ------------------------------

def mesange(x, y, s=1.0, flip=False, rot=0, bec_ouvert=False):
    """Mésange à tête noire : calotte et bavette noires, joues blanches,
    dos gris, flancs chamois ; (x, y) = sous les pattes."""
    m = [chemin("M -26 -30 L -76 -10 L -70 2 L -20 -18 Z", "#868e96"),
         trait(-4, -20, -6, 0, "#495057", 3), trait(8, -20, 8, 0, "#495057", 3),
         ellipse(0, -36, 34, 24, "#e9ecef", rot=-12), ellipse(4, -28, 26, 14, "#f3d9b1", rot=-12),
         ellipse(-10, -40, 26, 14, "#adb5bd", rot=-16),
         chemin("M -30 -38 L -4 -42 M -28 -32 L -2 -36", stroke="#f8f9fa", sw=2),
         cercle(28, -64, 20, "#f8f9fa"),
         chemin("M 8 -66 Q 10 -88 30 -86 Q 46 -84 48 -66 Q 30 -72 8 -66 Z", ENCRE),
         chemin("M 30 -56 Q 44 -58 46 -46 Q 34 -40 26 -48 Z", ENCRE),
         cercle(36, -68, 3.5, ENCRE), cercle(37, -69, 1.2, "#fff")]
    if bec_ouvert:
        m += [poly([(46, -66), (58, -66), (46, -62)], ENCRE), poly([(46, -60), (56, -58), (46, -58)], ENCRE)]
    else:
        m.append(poly([(46, -66), (58, -62), (46, -58)], ENCRE))
    return place(m + [occuper(-76, -90, 58, 0)], x, y, s, flip=flip, rot=rot)


def cardinal(x, y, s=1.0, flip=False, femelle=False):
    """Cardinal rouge (le mâle ; la femelle est beige) ; (x, y) = sous les pattes."""
    corps, aile, bec, masque = (("#c9a37a", "#e8590c", "#ff922b", "#868e96") if femelle else (ROUGE, "#c92a2a", "#ff6b6b", ENCRE))
    m = [chemin("M -30 -40 L -110 -2 L -100 14 L -20 -24 Z", aile),
         trait(-6, -24, -8, 0, "#c2255c", 4), trait(12, -24, 10, 0, "#c2255c", 4),
         ellipse(0, -46, 46, 32, corps, rot=-15), cercle(34, -86, 26, corps), poly([(18, -104), (-12, -140), (34, -110)], corps),
         ellipse(-12, -48, 34, 18, aile, rot=-18),
         chemin("M 36 -98 Q 54 -104 66 -94 L 66 -72 Q 54 -60 42 -68 Q 30 -84 36 -98 Z", masque),
         poly([(58, -94), (88, -82), (58, -72)], bec), cercle(44, -88, 8, "#fff" if not femelle else corps), cercle(45, -88, 4, ENCRE)]
    return place(m + [occuper(-110, -140, 88, 14)], x, y, s, flip=flip)


def mangeoire(x, y, s=1.0, neige=True):
    """Mangeoire en bois sur son poteau, pleine de graines de tournesol ; (x, y) = sol."""
    r = random.Random(4)
    m = [rect(-8, -300, 16, 300, "#7c4a1e"),
         rect(-80, -320, 160, 20, "#a0693a", rx=4),
         rect(-60, -400, 120, 80, "#d0ebff", opacity=0.8, stroke="#adb5bd", stroke_width=3),
         poly([(-96, -400), (0, -450), (96, -400)], "#c92a2a")]
    for _ in range(22):
        m.append(ellipse(r.uniform(-50, 50), r.uniform(-370, -326), 5, 3, "#343a40", rot=r.uniform(0, 180)))
    for _ in range(10):
        m.append(ellipse(r.uniform(-74, 74), -322, 5, 3, "#343a40", rot=r.uniform(0, 180)))
    if neige:
        m.append(chemin("M -98 -398 Q -50 -432 0 -452 Q 50 -432 98 -398 Q 50 -420 0 -440 Q -50 -420 -98 -398 Z", "#fff"))
    return place(m, x, y, s)


def cocotte(x, y, s=1.0, ficelle=0):
    """Cocotte de pin roulée dans la graisse et les graines ; (x, y) = haut."""
    m = []
    if ficelle:
        m.append(trait(0, -ficelle, 0, 0, "#c92a2a", 2.5))
    m.append(ellipse(0, 34, 22, 34, "#8d5524"))
    for k in range(5):
        m.append(chemin(f"M -20 {10 + k * 12} Q 0 {18 + k * 12} 20 {10 + k * 12}", stroke="#5c3a1e", sw=3))
    r = random.Random(int(x * 7 + y))
    for _ in range(12):
        m.append(ellipse(r.uniform(-16, 16), r.uniform(6, 62), 3.5, 2.2, ("#343a40", "#f6c453")[_ % 2], rot=r.uniform(0, 180)))
    return place(m, x, y, s)


def carte_cardinal(x, y, s=1.0, rot=0):
    """La carte d'Anouk : un cœur rouge, un cardinal dessiné au milieu."""
    m = [coeur(0, 0, 4.4, ROUGE), coeur(0, -4, 3.8, "#fff5f5"),
         place(cardinal(0, 0, 0.5), -2, 20, 1.0)]
    return place(m, x, y, s, rot=rot)


def photo(x, y, s=1.0, rot=0):
    """Vieille photo de Lucienne qui donne des graines aux oiseaux."""
    m = [rect(-80, -100, 160, 200, "#f8f9fa", rx=4, stroke="#dee2e6", stroke_width=3),
         rect(-66, -86, 132, 150, "#e9dcc9"),
         place(personne(0, 0, 1.0, stature="ancien", peau="claire", cheveux="gris", coiffure="chignon", habit="#c2a37a",
                        expr="rire", bras="tend", regard=(1, -0.5)), -20, 64, 0.62),
         place(mesange(0, 0, 1.0), 44, -24, 0.45)]
    return place(m, x, y, s, rot=rot)


def livre_oiseaux(x, y, s=1.0):
    m = [poly([(-110, -6), (0, 4), (110, -6), (110, -100), (0, -90), (-110, -100)], "#2f9e44"),
         poly([(-104, -12), (0, -2), (0, -92), (-104, -102)], "#fffaf0"), poly([(104, -12), (0, -2), (0, -92), (104, -102)], "#fff4e6"),
         place(mesange(0, 0, 0.7), -50, -30, 1.0), place(cardinal(0, 0, 0.4), 50, -26, 1.0)]
    return place(m, x, y, s)


def salle(S, y=600, fenetre_=True):
    """La grande salle de la résidence : boiseries, grande fenêtre sur le jardin."""
    piece(S, "manoir", y)
    S.ambiance("interieur")
    if fenetre_:
        dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 300, 800, 300, NEIGE),
                    sapin(650, 330, 0.4, neige=True), mangeoire(560, 360, 0.36)])
        S.add(fenetre(470, 100, 260, 220, "#d0ebff", rideaux="#c2255c", contenu=dehors))


def guirlande_coeurs(S, x0, x1, y, nb=9):
    S.add(chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y + 40} {x1} {y}", stroke="#c2255c", sw=3))
    for k in range(nb):
        t = (k + 0.5) / nb
        px = x0 + (x1 - x0) * t
        py = y + 40 * 4 * t * (1 - t) / 2 + 14
        S.add(coeur(px, py, 0.35, ("#e03131", "#f783ac", "#fcc419")[k % 3]))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    piece(S, "manoir", 640)
    S.ambiance("interieur")
    fx, fy, fw, fh = 110, 80, 580, 420
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 380, 800, 300, NEIGE), sapin(620, 400, 0.6, neige=True),
                arbre(200, 420, 0.8, feuillage="#ced4da", feuillage2="#adb5bd", tronc="#7c4a1e"),
                mangeoire(420, 500, 0.7), mesange(380, 280, 0.9), mesange(470, 282, 0.9, flip=True), cardinal(440, 190, 0.8)])
    S.add(fenetre(fx, fy, fw, fh, "#d0ebff", rideaux="#c2255c", contenu=dehors))
    S.add(gustave(470, 800, 1.45, expr="content", bras="tient", regard=(-1, 0), flip=True,
                  objet=carte_cardinal(*ancre(68, -146, "tient", "ancien", "fine"), 0.6)))
    S.add(anouk(260, 800, 1.3, expr="rire", bras="designe", regard=(1, -1)))
    S.cachette(760, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(trait(60, 230, 340, 220, "#7c4a1e", 12), trait(60, 222, 340, 212, "#fff", 6))
    S.add(mesange(200, 224, 1.6))
    return S


def p01():
    """Plan large : la sortie, vers la résidence des Érables."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    collines(S, 520, "#e7f5ff", graine=5, bosquets=False)
    sol(S, 600, NEIGE, bosse=8)
    S.add(immeuble(380, 600, w=380, etages=3, couleur="#e9a66b", toit="plat", balcons=False, lumiere=False, volets="#c2255c"))
    S.add(rect(470, 300, 200, 40, "#fff"), texte(570, 330, "Résidence des Érables", 18, "#c2255c"))
    S.add(arbre(250, 610, 1.0, feuillage="#ced4da", feuillage2="#adb5bd", tronc="#7c4a1e"))
    S.add(chemin("M 0 760 Q 300 690 560 640 L 620 640 Q 360 720 120 800 L 0 800 Z", "#dee2e6"))
    flocons(S, 30, 4, (0, 0, 800, 600))
    S.add(personne(470, 690, 0.85, expr="sourire", bras="coucou", regard=(1, -0.5), **HELENE))
    for k, (x, y) in enumerate(((380, 715), (310, 735), (240, 755))):
        S.add(enfant(k, x, y, 0.7, expr="rire", bras="marche", regard=(1, -0.5), pas="marche"))
    bx, by = mains_personne(160, 775, 0.8, "porte")[0]
    S.add(anouk(160, 775, 0.8, expr="content", bras="porte", regard=(1, -0.5),
                objet=g([rect(-40, -100, 80, 50, "#fff", rx=4), coeur(-14, -98, 0.25, ROUGE), coeur(14, -100, 0.25, "#f783ac")])))
    S.cachette(30, 780)
    return S


def p02():
    """Plan moyen : la fête des cœurs ; tout au fond, quelqu'un tourne le dos."""
    S = Scene()
    salle(S, 600)
    guirlande_coeurs(S, 10, 450, 60)
    S.add(gustave(600, 620, 0.8, expr="fache", bras="croises", regard=(1, -0.5), flip=True))
    S.add(personne(180, 760, 1.15, expr="rire", bras="calin", regard=(1, 0), **YVETTE))
    S.add(enfant(0, 290, 790, 0.9, expr="rire", bras="calin", regard=(-1, 0), flip=True))
    S.add(personne(440, 770, 1.1, expr="content", bras="tient", flip=True, regard=(-1, 0.4),
                   objet=carte_coeur(*ancre(68, -146, "tient", "ancien"), 0.5), **PAUL))
    S.add(enfant(2, 330, 795, 0.85, expr="joie", bras="tend", regard=(1, -0.3), objet=coeur_papier(96, -104, 0.5, ROUGE)))
    S.add(enfant(3, 720, 790, 0.85, expr="rire", bras="tient", flip=True, objet=coeur_papier(68, -146, 0.5, "#f783ac")))
    S.add(bulle(220, 380, 250, 70, "Oh, merci !", 30, pointe=(190, 470)))
    S.cachette(30, 790)
    return S


def p03():
    """Plan moyen : « Pas de cœur pour moi. »"""
    S = Scene()
    salle(S, 620)
    S.add(gustave(560, 790, 1.35, expr="fache", bras="croises", regard=(1, -0.3)))
    S.add(anouk(300, 790, 1.15, expr="sourire", bras="tend", regard=(1, 0), objet=coeur_papier(96, -104, 0.7, ROUGE)))
    S.add(bulle(250, 130, 360, 100, "Non merci.\nPas de cœur pour moi.", 30, pointe=(560, 420)))
    S.cachette(30, 790)
    return S


def p04():
    """Gros plan : Anouk, déçue, serre son cœur contre elle."""
    S = Scene()
    salle(S, 620)
    S.add(anouk(400, 800, 1.7, expr="triste", bras="calin", regard=(0, 1), objet=coeur_papier(0, -70, 0.9, ROUGE)))
    S.camera(1.4, 400, 520)
    S.cachette(110, 790)
    return S


def p05():
    """Plan moyen : à la fenêtre ; « Une mésange à tête noire ! »"""
    S = Scene()
    piece(S, "manoir", 640)
    S.ambiance("interieur")
    fx, fy, fw, fh = 140, 90, 520, 380
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 360, 800, 300, NEIGE), sapin(560, 380, 0.5, neige=True),
                mangeoire(380, 470, 0.6), mesange(350, 250, 0.8)])
    S.add(fenetre(fx, fy, fw, fh, "#d0ebff", rideaux="#c2255c", contenu=dehors))
    S.add(gustave(560, 800, 1.3, expr="surpris", bras="bas", regard=(-1, 0), flip=True))
    S.add(anouk(300, 800, 1.2, expr="joie", bras="designe", regard=(0.5, -1)))
    S.add(bulle(560, 160, 300, 90, "Tu connais\nles mésanges ?", 28, pointe=(570, 520)))
    S.cachette(30, 790)
    return S


def p06():
    """Gros plan : la mangeoire, deux mésanges et un cardinal."""
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(arbre(130, 700, 1.4, feuillage="#ced4da", feuillage2="#adb5bd", tronc="#7c4a1e"))
    sol(S, 700, NEIGE, bosse=8)
    flocons(S, 20, 8, (0, 0, 800, 700))
    S.add(mangeoire(420, 840, 1.6))
    S.add(mesange(330, 330, 1.3), mesange(520, 330, 1.3, flip=True, bec_ouvert=True))
    S.add(cardinal(400, 156, 1.1))
    S.cachette(700, 760)
    return S


def p07():
    """Plan moyen : « Fi-bi… » ; la mésange répond."""
    S = Scene()
    piece(S, "manoir", 640)
    S.ambiance("interieur")
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 300, 800, 300, NEIGE), mangeoire(580, 420, 0.5), mesange(560, 200, 0.7, bec_ouvert=True)])
    S.add(fenetre(420, 90, 300, 260, "#d0ebff", rideaux="#c2255c", contenu=dehors))
    S.add(gustave(300, 790, 1.35, expr="chante", bras="porte", regard=(1, -0.5),
                  objet=livre_oiseaux(*ancre(0, -74, "porte", "ancien", "fine"), 0.6)))
    S.add(anouk(520, 790, 1.15, expr="bouche_bee", bras="mains_jointes", regard=(-1, 0)))
    S.add(notes(420, 400, 0.9, "#5c7cfa"))
    S.add(texte(250, 300, "Fi-bi… fi-bi…", 36, "#5c7cfa", contour="#fff", rot=-6))
    S.add(texte(600, 380, "Fi-bi !", 34, "#2f9e44", contour="#fff", rot=6))
    S.cachette(770, 790)
    return S


def p08():
    """Plan moyen : la semaine suivante, la carte au cardinal."""
    S = Scene()
    salle(S, 620)
    S.add(personne(120, 780, 1.15, expr="content", bras="mains_jointes", regard=(1, 0), **MAMAN))
    S.add(anouk(310, 790, 1.15, expr="content", bras="donne", regard=(1, 0), objet=carte_cardinal(84, -110, 0.5)))
    S.add(gustave(560, 790, 1.3, expr="surpris", bras="tend", flip=True, regard=(-1, 0.3)))
    S.add(bulle(560, 380, 300, 90, "Pour moi ?", 34, pointe=(560, 450)))
    S.cachette(770, 790)
    return S


def p09():
    """Gros plan : la photo de Lucienne."""
    S = Scene()
    salle(S, 640, fenetre_=False)
    S.add(gustave(520, 820, 1.7, expr="content", larmes=True, bras="montre", flip=True, regard=(-1, 0.3),
                  objet=photo(*ancre(86, -130, "montre", "ancien", "fine"), 0.7)))
    S.add(anouk(220, 820, 1.45, expr="sourire", bras="mains_jointes", regard=(1, -0.3)))
    S.camera(1.25, 400, 500)
    S.dessus(bulle(400, 100, 520, 100, "Lucienne adorait les oiseaux.\nElle aurait aimé ta carte.", 30, pointe=S.vers_page(500, 420)))
    S.cachette(80, 790)
    return S


def p10():
    """Plan large : l'atelier des mangeoires, dans la grande salle."""
    S = Scene()
    salle(S, 580)
    S.add(gustave(400, 650, 1.0, expr="rire", bras="tient", regard=(0, 0.5), objet=cocotte(*ancre(68, -146, "tient", "ancien", "fine"), 0.8)))
    S.add(personne(600, 660, 0.95, expr="rire", bras="porte", flip=True, regard=(-1, 0.5), **YVETTE))
    S.add(table(400, 790, 700, 110, "#a0693a", nappe="#fff3bf"))
    S.add(ellipse(300, 668, 50, 14, "#e9ecef"), ellipse(300, 664, 40, 9, "#f1f3f5"))
    S.add(ellipse(500, 668, 50, 14, "#343a40"), *[ellipse(480 + k * 8, 662 + (k % 2) * 4, 4, 2.5, "#f6c453") for k in range(6)])
    for k, x in enumerate((140, 640)):
        S.add(cocotte(x, 620, 0.9))
    S.add(enfant(0, 120, 800, 0.85, expr="concentre", bras="porte", regard=(1, 0)))
    S.add(anouk(260, 800, 0.9, expr="rire", bras="haut", regard=(1, 0)))
    S.add(enfant(1, 540, 800, 0.85, expr="rire", bras="porte", regard=(-1, 0)))
    S.add(enfant(2, 690, 800, 0.85, expr="miam", bras="bouche", regard=(-1, 0)))
    S.add(texte(250, 260, "On roule, on roule…", 34, "#a0693a", contour="#fff", rot=-4))
    S.cachette(770, 790)
    return S


def p11():
    """Plan large : les cocottes dans l'érable ; les mésanges arrivent."""
    S = Scene()
    ciel(S, "#a5d8ff", "#f8f9fa")
    S.add(immeuble(0, 560, w=800, etages=3, couleur="#e9a66b", toit="plat", balcons=False, volets="#c2255c"))
    sol(S, 600, NEIGE, bosse=8)
    # un grand érable nu au milieu du jardin, et ses branches
    S.add(chemin("M 380 640 L 392 300 L 418 300 L 430 640 Z", "#7c4a1e"))
    for x0, y0, x1, y1 in ((400, 360, 220, 230), (410, 340, 600, 220), (405, 320, 380, 120), (300, 300, 230, 330), (520, 290, 640, 330)):
        S.add(trait(x0, y0, x1, y1, "#7c4a1e", 14), trait(x0, y0 - 7, x1, y1 - 7, "#fff", 6))
    for k, (x, y, f) in enumerate(((260, 252, 30), (330, 300, 50), (520, 268, 40), (600, 232, 26), (390, 170, 30))):
        S.add(cocotte(x, y + f, 0.7, ficelle=f))
    S.add(mesange(240, 240, 0.55), mesange(560, 226, 0.55, flip=True), mesange(420, 140, 0.5), mesange(140, 160, 0.5, rot=-20))
    S.add(gustave(110, 780, 0.95, expr="rire", bras="leve_doigt", regard=(1, -1)))
    S.add(personne(230, 785, 0.9, expr="content", bras="mains_jointes", regard=(1, -1), **YVETTE))
    S.add(anouk(560, 790, 0.95, expr="rire", bras="leve_doigt", regard=(-1, -1)))
    S.add(enfant(1, 680, 780, 0.85, expr="joie", bras="saute", regard=(-1, -1)))
    S.cachette(730, 260, "air")
    return S


def p12():
    """Plan moyen : à la fenêtre, deux amis qui sifflent aux oiseaux."""
    S = Scene()
    piece(S, "manoir", 640)
    S.ambiance("interieur")
    fx, fy, fw, fh = 140, 90, 520, 380
    dehors = g([rect(0, 0, 800, 800, "#d0ebff"), rect(0, 380, 800, 300, NEIGE),
                trait(160, 260, 660, 230, "#7c4a1e", 16), trait(160, 252, 660, 222, "#fff", 6),
                cocotte(300, 262, 0.6, ficelle=10), cocotte(520, 250, 0.6, ficelle=14),
                mesange(240, 252, 0.6), mesange(400, 246, 0.6, flip=True), cardinal(600, 230, 0.55)])
    S.add(fenetre(fx, fy, fw, fh, "#d0ebff", rideaux="#c2255c", contenu=dehors))
    S.add(carte_cardinal(610, 470, 0.6, rot=-8))
    S.add(gustave(460, 800, 1.35, expr="chante", bras="mains_jointes", regard=(-0.5, -0.6)))
    S.add(anouk(260, 800, 1.2, expr="rire", bras="applaudit", regard=(1, -0.5)))
    S.add(notes(400, 520, 0.8, "#5c7cfa"))
    S.cachette(760, 790)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("mesange-seule.svg", vignette),
    ("01-la-sortie.svg", p01), ("02-les-coeurs.svg", p02), ("03-pas-pour-moi.svg", p03),
    ("04-anouk.svg", p04), ("05-une-mesange.svg", p05), ("06-la-mangeoire.svg", p06),
    ("07-fi-bi.svg", p07), ("08-la-carte.svg", p08), ("09-lucienne.svg", p09),
    ("10-l-atelier.svg", p10), ("11-dans-l-arbre.svg", p11), ("12-mon-ami.svg", p12),
]
