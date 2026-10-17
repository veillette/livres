"""Le chaton d'Halloween — un chaton perdu, et toute une rue pour le ramener.

Le soir d'Halloween, Nina, déguisée en chat noir, trouve derrière une
citrouille un vrai petit chat, perdu et tremblant. Avec Papa, elle frappe à
toutes les portes : « Des bonbons ou un sort ! … Est-ce votre chaton ? »
Des bonbons, oui ; un chaton, personne n'en a perdu. Tout au bout de la
rue, Madame Rose appelle « Mistigri ! » : le chaton bondit dans ses bras.
Halloween n'est que le décor : l'histoire est celle d'un animal qu'on aide
à rentrer chez lui, et d'une nouvelle amitié.

Plans : 1 moyen (le costume, au crépuscule) · 2 large (la rue) · 3 gros
plan (le chaton derrière la citrouille) · 4 moyen (sous le réverbère) ·
5 moyen (Monsieur Ben, le vampire) · 6 gros plan (Wouf !) · 7 large (toute
la rue) · 8 contre-plongée (la petite maison au bout) · 9 gros plan (le
saut) · 10 moyen (Madame Rose) · 11 moyen, intérieur (chocolat chaud) ·
12 large (le retour).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from objets import _tete_chat, chat_profil, tasse, assiette
from fables import cheminee
from fetes import (citrouille_creusee, citrouille_anse, seau_bonbons, bonbon, chauve_souris_papier,
                   drap_fantome, chapeau_sorciere, chien_profil, lanterne)

ID = "halloween-chaton"
PAPIER_PEINT = "fleurs"

NOIR = "#2b2b3a"
GRIS = "#adb5bd"          # Mistigri
ECHARPE = "#ff922b"


def oreilles_chat(c=NOIR, rose="#f783ac"):
    """Serre-tête à oreilles de chat (coiffe d'une personne)."""
    m = [chemin("M -50 -176 Q 0 -214 50 -176", stroke=c, sw=7)]
    for sgn in (-1, 1):
        m.append(poly([(sgn * 18, -196), (sgn * 40, -248), (sgn * 52, -184)], c))
        m.append(poly([(sgn * 26, -198), (sgn * 40, -232), (sgn * 46, -190)], rose))
    return g(m)


def moustaches():
    """Moustaches dessinées au crayon et petit nez noir (sur le visage)."""
    m = [ellipse(0, -136, 6, 4.5, NOIR)]
    for sgn in (-1, 1):
        for dy in (-4, 3):
            m.append(trait(sgn * 16, -130 + dy, sgn * 44, -134 + dy * 2.2, NOIR, 2.2))
    return g(m)


def queue_costume():
    return chemin("M 22 -40 Q 92 -30 86 -96 Q 82 -128 104 -138", stroke=NOIR, sw=12)


def echarpe(chaton=None):
    """Grosse écharpe orange nouée sur la poitrine ; chaton : None, "regarde"
    ou "dort" (la tête de Mistigri dépasse du nœud)."""
    m = [chemin("M -36 -108 Q 0 -86 36 -108 L 34 -92 Q 0 -70 -34 -92 Z", ECHARPE)]
    if chaton:
        # la tête de Mistigri sort de la poche que fait l'écharpe sur la poitrine
        m.append(place(_tete_chat(GRIS, True, "dort" if chaton == "dort" else "surpris", (0, 0)), 0, -82, 0.6))
    m += [chemin("M -30 -76 Q 0 -66 30 -76 L 26 -44 Q 0 -36 -26 -44 Z", _assombrir(ECHARPE, 0.9)),
          chemin("M -28 -74 Q 0 -64 28 -74", stroke=eclaircir(ECHARPE, 0.4), sw=3),
          rect(18, -100, 16, 62, ECHARPE, rx=6), chemin("M 20 -46 h 12 M 20 -40 h 12", stroke="#fff", sw=2, opacity=0.6)]
    return g(m)


NINA = dict(peau="brune", cheveux="noir", coiffure="carre", habit=NOIR, robe=False, jambes=NOIR,
            chaussures="#e64980", nez="retrousse", yeux="cils")
PAPA = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#2f9e44", robe=False,
            jambes="#495057", carrure="ronde", nez="rond")
ROSE_ = dict(stature="ancien", peau="claire", cheveux="blanc", coiffure="chignon", habit="#da77f2",
             acc=("lunettes",), carrure="fine", nez="pointu")
BEN = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#f8f9fa", robe=False,
           jambes=NOIR, cape="#c92a2a", carrure="fine", nez="long")
SOEUR1 = dict(stature="ado", peau="claire", cheveux="roux", coiffure="tresses", habit="#5f3dc4", taches=True)
SOEUR2 = dict(stature="ado", peau="claire", cheveux="roux", coiffure="longs", habit="#2f9e44", nez="pointu")


def nina(x, y, s=1.2, chaton=None, **k):
    tenue = g([moustaches_tenue(), echarpe(chaton)]) if chaton is not False else moustaches_tenue()
    return personne(x, y, s, **{**NINA, "coiffe": g([oreilles_chat(), moustaches()]), "tenue": tenue,
                                "derriere": queue_costume(), **k})


def moustaches_tenue():
    """Le ventre blanc du costume de chat."""
    return ellipse(0, -66, 22, 26, "#495057", opacity=0.6)


def papa(x, y, s=1.2, **k):
    return personne(x, y, s, **{**PAPA, **k})


def rose(x, y, s=1.2, **k):
    return personne(x, y, s, **{**ROSE_, **k})


def grisou(x, y, s=0.4, **k):
    k.setdefault("pose", "assis")
    return chat_profil(x, y, s, couleur=GRIS, **k)


def nina_porte(x, y, s=1.2, **k):
    """Nina qui serre Mistigri contre elle, à deux mains."""
    k.setdefault("bras", "porte")
    chat = place(_tete_chat(GRIS, True, k.pop("chat_expr", "sourire"), (0, 0)), 0, -92, 0.62)
    corps_chat = ellipse(0, -66, 24, 18, volume(GRIS, 0.3, 0.8))
    return nina(x, y, s, chaton=False, objet=g([corps_chat, chat]), **k)


def porte_citrouille(S, qui, x, y, s, flip=False, stature="adulte", **k):
    """Un personnage qui tient une citrouille-lanterne par l'anse, et son halo."""
    ax, ay = ancre(68, -146, "tient", stature)
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=citrouille_anse(ax, ay, 0.45), **k))
    S.lumiere(x + (-ax if flip else ax) * s, y + (ay + 92 * 0.45) * s, 80 * s, "#ff922b", 0.6)


def lampadaire(x, y, s=1.0):
    """Réverbère allumé ; halo à poser avec S.lumiere(x, y - 300 s)."""
    m = [rect(-7, -290, 14, 290, "#343a40", rx=4), rect(-22, -6, 44, 10, "#343a40", rx=3),
         poly([(-26, -300), (26, -300), (18, -330), (-18, -330)], "#343a40"),
         rect(-18, -300, 36, 26, "#ffe066"), poly([(-30, -330), (30, -330), (0, -350)], "#343a40")]
    return place(m, x, y, s)


def rue_nuit(S, sol_y=650, lune_=(650, 120), graine=5, crepuscule=False):
    if crepuscule:
        ciel(S, "#5f3dc4", "#ff922b")
    else:
        nuit(S, "#1a1238", "#4b2f7a")
    etoiles(S, 18 if crepuscule else 34, graine, (0, 0, 800, sol_y - 240))
    if lune_:
        S.add(lune(*lune_, 50))
    sol(S, sol_y, "#4a3f6b", bosse=8)
    # le trottoir
    S.add(rect(0, sol_y + 30, 800, 24, "#6c5f8d", opacity=0.7))


def citrouille_posee(S, x, y, s=0.5, allumee=True):
    S.add(citrouille_creusee(x, y, s, allumee=allumee))
    if allumee:
        S.lumiere(x, y - 55 * s, 120 * s, "#ff922b", 0.6)


def petite_maison(x, y, s=1.0, lumiere=True):
    """La maison de Madame Rose : petite, bleu lavande, sans citrouille."""
    return maison(x, y, s, mur="#d0bfff", toit="#495057", porte="#5f3dc4", volets="#7048e8",
                  lumiere=lumiere, cheminee=True)


def perron(S, x, y, w=300, couleur="#8c7ab8"):
    """Marches de bois devant une porte ; (x, y) = milieu de la marche du bas."""
    S.add(rect(x - w / 2, y - 24, w, 24, couleur), rect(x - w / 2 + 20, y - 48, w - 40, 24, eclaircir(couleur, 0.15)))
    S.add(planches(x - w / 2, y - 48, w, 48, couleur, larg=24, vertical=False))


def facade(S, x0, x1, y0, y1, couleur, porte_x, ouverte=True, lumiere=True):
    """Pan de façade au plan moyen, avec une porte (ouverte sur un intérieur éclairé)."""
    S.add(rect(x0, y0, x1 - x0, y1 - y0, couleur), planches(x0, y0, x1 - x0, y1 - y0, couleur, larg=30))
    S.add(rect(porte_x - 100, y1 - 400, 200, 400, "#ffe8a3" if ouverte else "#5f3dc4"),
          rect(porte_x - 112, y1 - 412, 224, 14, "#3b2a5e"),
          rect(porte_x - 112, y1 - 412, 12, 412, "#3b2a5e"), rect(porte_x + 100, y1 - 412, 12, 412, "#3b2a5e"))
    if ouverte:
        # la porte rabattue contre le mur intérieur, et la lumière qui sort
        S.add(poly([(porte_x + 100, y1 - 400), (porte_x + 60, y1 - 384), (porte_x + 60, y1 - 12), (porte_x + 100, y1)],
                   cylindre("#7048e8", 0.2, 0.7)))
        if lumiere:
            S.lumiere(porte_x, y1 - 200, 220, "#ffd43b", 0.55)
            S.lumiere(porte_x, y1 + 40, 200, "#ffd43b", 0.4, ry=50)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue_nuit(S, 640, lune_=(620, 150))
    S.add(maison(140, 640, 0.85, mur="#8c7ab8", toit="#3b2a5e", lumiere=True, cheminee=False))
    S.add(maison(690, 630, 0.6, mur="#ffa94d", toit="#5f3dc4", lumiere=True))
    citrouille_posee(S, 70, 700, 0.45)
    citrouille_posee(S, 250, 690, 0.4)
    S.add(chauve_souris_papier(330, 240, 1.0, rot=-10), chauve_souris_papier(450, 170, 0.75, rot=12))
    porte_citrouille(S, papa, 560, 780, 1.4, expr="rire", regard=(-1, 0))
    S.add(nina_porte(330, 790, 1.35, expr="joie", regard=(1, 0)))
    S.cachette(760, 330, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 170, 110, radial([(0, "#ffe066", 0.55), (1, "#ffe066", 0)])))
    S.add(citrouille_creusee(250, 262, 0.75))
    S.add(grisou(140, 262, 0.75, regard=(1, 0)))
    return S


def p01():
    """Plan moyen : le costume, sur le perron, au crépuscule."""
    S = Scene()
    rue_nuit(S, 660, lune_=None, crepuscule=True)
    S.add(maison(620, 610, 0.55, mur="#ffd8a8", toit="#5f3dc4", lumiere=True))
    facade(S, 0, 300, 160, 700, "#8c7ab8", 150, ouverte=True)
    perron(S, 150, 724, 320)
    citrouille_posee(S, 330, 720, 0.42)
    citrouille_posee(S, 30, 690, 0.32)
    S.add(nina(420, 780, 1.25, chaton=False, expr="rire", bras="poing", regard=(1, 0)))
    porte_citrouille(S, papa, 610, 790, 1.3, expr="rire", regard=(-1, 0))
    S.add(bulle(430, 130, 220, 90, "Miaou !", 46, pointe=(430, 400)))
    S.cachette(770, 760)
    return S


def enfant_deguise(S, x, y, s, costume, **k):
    """Les autres enfants de la rue : fantôme, petite sorcière, dragon."""
    if costume == "fantome":
        S.add(drap_fantome(x, y, s * 0.85))
    elif costume == "sorciere":
        S.add(personne(x, y, s, peau="claire", cheveux="blond", coiffure="longs", habit="#5f3dc4", acc=("chapeau_pointu",),
                       couleur_acc=NOIR, bras="tient", objet=seau_bonbons(68, -146, 0.8), **k))
    else:
        S.add(perso("lapin", x, y, s, habit="#40c057", couleur="#69db7c", visage="#d8f5a2", expr="rire", bras="haut",
                    derriere=g([poly([(-60, -120), (-150, -170), (-110, -90)], "#2f9e44"), poly([(60, -120), (150, -170), (110, -90)], "#2f9e44")]), **k))


def p02():
    """Plan large : la rue d'Halloween, et une petite voix derrière la citrouille."""
    S = Scene()
    rue_nuit(S, 600, lune_=(120, 110), graine=7)
    for k, (x, s, mur, toit) in enumerate(((140, 0.62, "#ffa94d", "#3b2a5e"), (400, 0.7, "#8c7ab8", "#212529"),
                                            (660, 0.62, "#74c0fc", "#5f3dc4"))):
        S.add(maison(x, 600, s, mur=mur, toit=toit, lumiere=True, cheminee=k != 1))
        citrouille_posee(S, x + 90 * s, 620, 0.26)
    S.add(lampadaire(540, 660, 1.0))
    S.lumiere(540, 360, 120, "#ffe066", 0.6)
    enfant_deguise(S, 330, 660, 0.62, "fantome")
    enfant_deguise(S, 410, 670, 0.62, "sorciere", regard=(1, 0))
    enfant_deguise(S, 480, 665, 0.55, "dragon")
    # la grosse citrouille, au premier plan, et la petite voix
    citrouille_posee(S, 660, 780, 0.8)
    S.add(texte(650, 600, "Miou !", 44, "#ffd43b", contour="#1a1238", rot=-6))
    S.add(nina(250, 780, 1.1, chaton=False, expr="surpris", bras="tient", regard=(1, 0), pas="marche",
               objet=seau_bonbons(68, -146, 0.8)))
    S.add(papa(110, 780, 1.15, expr="sourire", bras="bas", regard=(1, 0), pas="marche"))
    S.cachette(570, 70, "air")
    return S


def p03():
    """Gros plan : un vrai chaton, tout petit, derrière la citrouille."""
    S = Scene()
    rue_nuit(S, 600, lune_=None)
    S.add(maison(160, 600, 0.6, mur="#ffa94d", toit="#3b2a5e", lumiere=True))
    S.add(nina(250, 800, 1.4, chaton=False, expr="bouche_bee", bras="joues", regard=(1, 1)))
    citrouille_posee(S, 560, 790, 0.95)
    S.add(grisou(430, 790, 0.62, expr="surpris", regard=(-1, 0)))
    # le chaton tremble
    S.add(mouvement(372, 700, 0.6, "#ced4da", rot=180), mouvement(486, 700, 0.6, "#ced4da"))
    S.camera(1.45, 400, 620)
    S.dessus(bulle(560, 110, 400, 100, "Un vrai chat,\nplus petit que moi !", 32, pointe=S.vers_page(300, 470)))
    S.cachette(720, 720)
    return S


def p04():
    """Plan moyen : sous le réverbère, Nina serre le chaton ; Papa lui parle."""
    S = Scene()
    rue_nuit(S, 640, lune_=(650, 110), graine=9)
    S.add(maison(660, 640, 0.65, mur="#8c7ab8", toit="#212529", lumiere=True))
    S.add(lampadaire(150, 720, 1.5))
    S.lumiere(150, 260, 180, "#ffe066", 0.6)
    S.lumiere(260, 760, 220, "#ffe066", 0.35, ry=50)
    S.add(nina_porte(310, 780, 1.25, expr="sourire", regard=(1, -0.5), chat_expr="sourire"))
    S.add(papa(510, 780, 1.4, expr="sourire", bras="leve_doigt", regard=(-1, 0), flip=True))
    S.add(bulle(560, 130, 380, 100, "Il s'est sûrement\nperdu.", 34, pointe=(520, 400)))
    S.cachette(740, 770)
    return S


def p05():
    """Plan moyen : à la porte de Monsieur Ben, le vampire."""
    S = Scene()
    rue_nuit(S, 680, lune_=None)
    facade(S, 300, 800, 120, 690, "#ffa94d", 560)
    citrouille_posee(S, 360, 720, 0.4)
    bx, by = ancre(84, -92, "donne", "adulte", "fine")
    bol_bonbons = g([ellipse(bx, by - 4, 46, 14, "#f8f9fa"),
                     *[bonbon(bx - 26 + j * 18, by - 14 - (j % 2) * 6, 0.7, c) for j, c in enumerate(("#f06595", "#74c0fc", "#ffd43b", "#69db7c"))],
                     chemin(f"M {bx - 46} {by - 4} Q {bx} {by + 40} {bx + 46} {by - 4} Z", "#c92a2a")])
    S.add(personne(600, 690, 1.3, expr="rire", bras="donne", flip=True, regard=(-1, 0), objet=bol_bonbons, **BEN))
    S.add(nina_porte(340, 780, 1.15, expr="sourire", regard=(1, -0.4)))
    S.add(papa(140, 780, 1.3, expr="sourire", bras="hanches", regard=(1, 0)))
    S.add(bulle(220, 140, 380, 110, "Est-ce que c'est\nvotre chaton ?", 32, pointe=(300, 440)))
    S.cachette(570, 70, "air")
    return S


def p06():
    """Gros plan : Wouf ! Le chaton se cache dans l'écharpe."""
    S = Scene()
    rue_nuit(S, 680, lune_=None)
    facade(S, 0, 800, 100, 690, "#74c0fc", 520)
    S.add(personne(420, 700, 1.15, expr="rire", bras="bouche", regard=(1, 0), acc=("chapeau_pointu",), couleur_acc=NOIR, **SOEUR1))
    S.add(personne(660, 700, 1.15, expr="rire", bras="hanches", regard=(-1, 0), flip=True, acc=("chapeau_pointu",), couleur_acc=NOIR, **SOEUR2))
    S.add(chien_profil(500, 700, 1.15, couleur="#a0693a", oreille="#5c3a1e", flip=True, expr="content"))
    S.add(nina(250, 790, 1.3, chaton="regarde", expr="surpris", bras="epaules", regard=(1, 0)))
    S.camera(1.25, 420, 560)
    S.dessus(texte(560, 110, "Wouf ! Wouf !", 56, "#ffd43b", contour="#1a1238", rot=-8))
    S.cachette(110, 760)
    return S


def p07():
    """Plan large : maison après maison, le seau se remplit."""
    S = Scene()
    rue_nuit(S, 560, lune_=(680, 100), graine=11)
    for k, (x, s, mur, toit) in enumerate(((90, 0.5, "#ffa94d", "#3b2a5e"), (260, 0.55, "#74c0fc", "#5f3dc4"),
                                            (450, 0.5, "#8c7ab8", "#212529"), (640, 0.55, "#ffd8a8", "#3b2a5e"))):
        S.add(maison(x, 560, s, mur=mur, toit=toit, lumiere=k % 2 == 0, cheminee=k % 2 == 1))
        citrouille_posee(S, x + 80 * s, 580, 0.22, allumee=k != 3)
    # le chemin qui monte en diagonale, Nina et Papa le remontent
    S.add(chemin("M 0 800 Q 300 700 800 640 L 800 680 Q 360 740 120 800 Z", "#6c5f8d"))
    S.add(lampadaire(660, 680, 0.9))
    S.lumiere(660, 410, 110, "#ffe066", 0.55)
    S.add(papa(470, 720, 1.05, expr="sourire", bras="main", regard=(-1, 0), flip=True, pas="marche"))
    S.add(nina(360, 740, 0.95, chaton="dort", expr="triste", bras="main", regard=(1, 0), pas="marche",
               objet=None))
    S.add(seau_bonbons(*mains_personne(360, 740, 0.95, "main")[0], 0.75))
    S.add(texte(250, 250, "Toc, toc, toc…", 44, "#ffd43b", contour="#1a1238", rot=-6))
    S.cachette(740, 760)
    return S


def p08():
    """Contre-plongée : la petite maison au bout de la rue ; « Mistigri ! »"""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a6e")
    etoiles(S, 40, 13, (0, 0, 800, 330))
    S.add(lune(130, 120, 44))
    sol(S, 600, "#4a3f6b", bosse=10)
    S.add(arbre(700, 600, 1.2, feuillage="#3b2a5e", feuillage2="#2b1f45", tronc="#2b1f45"))
    S.add(petite_maison(380, 600, 1.35, lumiere=True))
    S.add(chemin("M 330 600 L 440 600 L 620 800 L 160 800 Z", "#6c5f8d"))
    lx, ly = ancre(80, -168, "coucou", "ancien", "fine")
    S.add(rose(300, 620, 0.9, expr="inquiet", bras="coucou", regard=(1, 0), objet=lanterne(lx, ly, 0.9)))
    S.lumiere(300 + lx * 0.9, 620 + (ly + 52 * 0.9) * 0.9, 90, "#ffd43b", 0.65)
    S.add(nina(470, 790, 0.85, chaton="dort", expr="surpris", bras="bas", regard=(-1, -1)))
    S.add(papa(590, 790, 0.85, expr="surpris", bras="bas", regard=(-1, -1)))
    S.add(bulle(600, 130, 300, 90, "Mistigri ! Mistigri !", 34, pointe=(370, 450)))
    S.cachette(90, 760)
    return S


def p09():
    """Gros plan : Mistigri bondit, droit dans les bras de la vieille dame."""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a6e")
    facade(S, 0, 800, 60, 700, "#d0bfff", 640, ouverte=True)
    sol(S, 700, "#4a3f6b", bosse=0)
    S.add(rose(600, 790, 1.5, expr="joie", bras="ouverts", regard=(-1, 0), flip=True))
    S.add(nina(200, 800, 1.3, chaton=False, expr="rire", bras="haut", regard=(1, -0.5)))
    # Mistigri en plein saut, en diagonale
    S.add(place([chat_profil(0, 0, 1.0, couleur=GRIS, pose="debout", expr="content")], 400, 380, 0.75, rot=-18))
    S.add(mouvement(290, 460, 0.9, "#ced4da", rot=160))
    S.add(texte(420, 230, "Miou !", 54, "#ffd43b", contour="#120c2a", rot=-10))
    S.camera(1.15, 400, 470)
    S.cachette(60, 760)
    return S


def p10():
    """Plan moyen : Madame Rose serre Mistigri ; elle ouvre grand sa porte."""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a6e")
    etoiles(S, 20, 15, (0, 0, 800, 100))
    facade(S, 180, 800, 90, 680, "#d0bfff", 470, ouverte=True)
    S.add(fenetre(640, 220, 120, 120, "#ffe066", cadre="#7048e8"))
    S.lumiere(700, 280, 90, "#ffd43b", 0.5)
    perron(S, 470, 700, 360, "#7a6aa8")
    chat = g([ellipse(0, -76, 24, 18, volume(GRIS, 0.3, 0.8)),
              place(_tete_chat(GRIS, True, "content", (0, 0)), -6, -116, 0.62)])
    S.add(rose(480, 680, 1.25, expr="content", larmes=True, bras="calin", regard=(0, 0), objet=place(chat, 0, 0, 1.0)))
    S.add(nina(250, 790, 1.1, chaton=False, expr="rire", bras="mains_jointes", regard=(1, -0.5)))
    S.add(papa(100, 790, 1.2, expr="content", bras="hanches", regard=(1, -0.3)))
    S.add(bulle(170, 120, 300, 100, "Entrez donc\nvous réchauffer !", 30, pointe=(420, 400)))
    S.cachette(740, 760)
    return S


def biscuit_chauve_souris(x, y, s=1.0):
    return chauve_souris_papier(x, y, s, couleur="#c68642")


def p11():
    """Plan moyen, intérieur : chocolat chaud et biscuits chauve-souris."""
    S = Scene()
    piece(S, "manoir", 600)
    S.ambiance("interieur")
    S.add(cheminee(130, 600, 0.6, feu=True))
    S.lumiere(130, 550, 170, "#ff922b", 0.55)
    S.add(fenetre(560, 100, 170, 150, "#1a1238", nuit_=True, rideaux="#da77f2"))
    S.add(cadre_mur(330, 120, 110, 90, "#d0bfff"))
    S.add(tapis(420, 730, 320, 50, "#e5dbff", "#9775fa"))
    S.add(papa(500, 700, 1.05, expr="content", bras="calin", regard=(-1, 0.4)))
    S.add(table(500, 740, 220, 100, "#a0693a", nappe="#f3d9fa"))
    S.add(assiette(470, 625, 0.9), biscuit_chauve_souris(450, 615, 0.5), biscuit_chauve_souris(492, 610, 0.45))
    S.add(tasse(550, 615, 0.9, "#e64980"))
    S.add(nina_porte(300, 790, 1.15, expr="content", regard=(1, -0.3), chat_expr="content"))
    tx, ty = ancre(96, -104, "tend", "ancien", "fine")
    S.add(rose(680, 790, 1.15, expr="rire", bras="tend", flip=True, regard=(-1, 0),
               objet=tasse(tx, ty + 10, 0.8, "#4dabf7")))
    S.add(texte(300, 470, "rrr… rrr…", 32, "#9775fa", contour="#fff"))
    return S


def p12():
    """Plan large : le retour, main dans la main ; Madame Rose et Mistigri à la fenêtre."""
    S = Scene()
    nuit(S, "#120c2a", "#3b2a6e")
    etoiles(S, 50, 17, (0, 0, 800, 330))
    S.add(lune(660, 110, 50))
    sol(S, 640, "#4a3f6b", bosse=8)
    S.add(chemin("M 300 800 Q 520 690 800 660 L 800 700 Q 560 730 420 800 Z", "#6c5f8d"))
    S.add(maison(700, 640, 0.5, mur="#ffa94d", toit="#3b2a5e", lumiere=True))
    citrouille_posee(S, 610, 660, 0.25)
    # le mur de Madame Rose, au premier plan, et sa grande fenêtre éclairée
    S.add(rect(0, 120, 330, 560, "#d0bfff"), planches(0, 120, 330, 560, "#d0bfff", larg=30))
    S.add(poly([(0, 120), (330, 120), (360, 90), (0, 90)], "#495057"))
    vue = g([rect(40, 260, 240, 220, "#ffe8a3"), cadre_mur(190, 280, 70, 60, "#ffd8a8"),
             rose(150, 600, 1.05, expr="rire", bras="coucou", regard=(1, 0)),
             place(chat_profil(0, 0, 1.0, couleur=GRIS, pose="assis", expr="content", regard=(1, 0)), 240, 480, 0.55)])
    S.add(fenetre(40, 260, 240, 220, "#ffe8a3", cadre="#7048e8", contenu=vue))
    S.lumiere(160, 370, 200, "#ffd43b", 0.55)
    S.lumiere(160, 720, 200, "#ffd43b", 0.35, ry=50)
    S.add(papa(600, 740, 0.95, expr="content", bras="main", regard=(-1, 0), flip=True, pas="marche"))
    S.add(nina(490, 760, 0.85, chaton=False, expr="content", bras="main", regard=(-1, 0), pas="marche"))
    S.add(seau_bonbons(*mains_personne(490, 760, 0.85, "main")[0], 0.65))
    S.add(bulle(560, 330, 300, 80, "À bientôt, Mistigri !", 30, pointe=(500, 540)))
    S.cachette(760, 780)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chaton-seul.svg", vignette),
    ("01-le-costume.svg", p01), ("02-dans-la-rue.svg", p02), ("03-un-vrai-chat.svg", p03),
    ("04-il-est-perdu.svg", p04), ("05-monsieur-vampire.svg", p05), ("06-wouf.svg", p06),
    ("07-toute-la-rue.svg", p07), ("08-grisou.svg", p08), ("09-miou.svg", p09),
    ("10-madame-rose.svg", p10), ("11-chocolat-chaud.svg", p11), ("12-le-retour.svg", p12),
]
