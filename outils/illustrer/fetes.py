"""Illustrations SVG des dix histoires de fêtes, dans le style du catalogue."""

import math

from base import (Scene, ciel, sol, interieur, sapin, fleur, nuage, lune, etoiles,
                  etoile5, coeur, notes, paillettes, perso, rect, cercle, ellipse,
                  trait, chemin, poly, place, g)
from objets import gateau, ballon_air
from livres_fetes import LIVRES

PAR_ID = {livre["id"]: livre for livre in LIVRES}


def objet(nom, x, y, s=1):
    """Un accessoire lisible au centre de l'image ; y est son point d'appui."""
    if nom == "sapin":
        return g([sapin(x, y, s * 1.15), etoile5(x, y - 300 * s, 23 * s),
                  cercle(x - 55 * s, y - 95 * s, 9 * s, "#fa5252"),
                  cercle(x + 42 * s, y - 146 * s, 9 * s, "#ffd43b"),
                  cercle(x - 14 * s, y - 210 * s, 9 * s, "#74c0fc")])
    if nom == "brouette":
        return g([trait(x-130*s, y-65*s, x-175*s, y-145*s, "#8d5524", 13*s),
                  poly([(x-120*s, y-95*s), (x+120*s, y-95*s), (x+80*s, y-20*s),
                        (x-75*s, y-20*s)], "#a05a2c"),
                  objet("citrouille", x, y-35*s, 0.65*s),
                  cercle(x+80*s, y-12*s, 23*s, "#343a40"),
                  cercle(x+80*s, y-12*s, 9*s, "#adb5bd")])
    if nom == "table-vide":
        return g([rect(x-135*s, y-100*s, 270*s, 24*s, "#c68642", rx=8*s),
                  rect(x-110*s, y-76*s, 22*s, 80*s, "#8d5524"),
                  rect(x+90*s, y-76*s, 22*s, 80*s, "#8d5524")])
    if nom == "fleur":
        return g([fleur(x - 65*s, y, 1.3*s, "#ff8787", tige=105),
                  fleur(x, y, 1.6*s, "#ffd43b", tige=110),
                  fleur(x + 70*s, y, 1.2*s, "#b197fc", tige=90)])
    if nom == "nuage":
        return nuage(x, y - 170*s, 1.5*s, "#f8f9fa", "#ced4da") + g([
            trait(x - 65*s, y - 80*s, x - 80*s, y - 15*s, "#74c0fc", 7),
            trait(x, y - 80*s, x - 12*s, y - 10*s, "#74c0fc", 7),
            trait(x + 65*s, y - 80*s, x + 50*s, y - 15*s, "#74c0fc", 7)])
    if nom == "gateau":
        return gateau(x, y, 1.5*s, bougies=3, fruits="#fa5252")
    if nom == "ballon":
        return g([ballon_air(x - 55*s, y, s, "#ff6b6b"),
                  ballon_air(x + 60*s, y, s, "#74c0fc")])
    if nom == "coeur":
        return coeur(x, y - 110*s, 2*s, "#f06595")
    if nom == "note":
        return notes(x, y - 120*s, 2.2*s, "#364fc7")
    if nom == "etoile":
        return etoile5(x, y - 125*s, 105*s, "#ffd43b")
    if nom == "oeuf":
        m = [ellipse(0, -105, 75, 105, "#fff9db", stroke="#e67700", stroke_width=5),
             chemin("M -68 -90 Q 0 -60 68 -90", stroke="#f06595", sw=12),
             chemin("M -58 -145 Q 0 -120 58 -145", stroke="#74c0fc", sw=11)]
    elif nom == "panier":
        m = [chemin("M -110 -80 Q -100 -225 0 -225 Q 100 -225 110 -80", stroke="#a05a2c", sw=16),
             ellipse(-52, -99, 32, 43, "#ff8787"), ellipse(15, -105, 32, 43, "#a5d8ff"),
             ellipse(68, -90, 29, 39, "#ffd43b"),
             chemin("M -125 -105 L 125 -105 L 100 0 L -100 0 Z", "#c68642", stroke="#8d5524", sw=5),
             trait(-105, -65, 105, -65, "#f8d9a0", 8), trait(-99, -35, 99, -35, "#f8d9a0", 8)]
    elif nom == "citrouille":
        m = [rect(-7, -175, 14, 33, "#2f9e44", rx=5),
             ellipse(-60, -73, 65, 73, "#e8590c"), ellipse(60, -73, 65, 73, "#e8590c"),
             ellipse(0, -75, 72, 77, "#ff922b"),
             poly([(-52, -106), (-18, -106), (-35, -76)], "#2b2b3a"),
             poly([(18, -106), (52, -106), (35, -76)], "#2b2b3a"),
             chemin("M -43 -45 Q 0 -15 43 -45", stroke="#2b2b3a", sw=9)]
    elif nom == "cadeau":
        m = [rect(-100, -145, 200, 145, "#fa5252", rx=8), rect(-115, -158, 230, 35, "#ff8787", rx=6),
             rect(-15, -158, 30, 158, "#ffd43b"),
             ellipse(-24, -166, 29, 17, "none", stroke="#ffd43b", stroke_width=10, rot=25),
             ellipse(24, -166, 29, 17, "none", stroke="#ffd43b", stroke_width=10, rot=-25)]
    elif nom == "guirlande":
        m = [chemin("M -160 -140 Q 0 -45 160 -140", stroke="#2f9e44", sw=9)]
        for px, py, col in [(-125, -120, "#ff6b6b"), (-65, -90, "#ffd43b"), (0, -75, "#74c0fc"), (65, -90, "#ff6b6b"), (125, -120, "#ffd43b")]:
            m.append(cercle(px, py, 16, col))
    elif nom == "masque":
        m = [chemin("M -130 -130 Q 0 -210 130 -130 L 110 -45 Q 0 0 -110 -45 Z", "#e599f7", stroke="#862e9c", sw=7),
             ellipse(-55, -105, 32, 22, "#fff"), ellipse(55, -105, 32, 22, "#fff"),
             chemin("M -20 -40 Q 0 -25 20 -40", stroke="#862e9c", sw=5),
             poly([(-90, -155), (-115, -260), (-55, -162)], "#74c0fc"),
             poly([(0, -175), (0, -280), (30, -172)], "#ffd43b"),
             poly([(85, -155), (115, -260), (55, -162)], "#ff8787")]
    elif nom == "lanterne":
        m = [rect(-80, -178, 160, 150, "#495057", rx=14), rect(-55, -156, 110, 104, "#ffe066", rx=10),
             chemin("M -36 -178 Q -36 -235 0 -235 Q 36 -235 36 -178", stroke="#495057", sw=10),
             rect(-93, -30, 186, 28, "#343a40", rx=8),
             ellipse(0, -102, 25, 37, "#ff922b")]
    elif nom == "bonbon":
        m = [ellipse(0, -95, 75, 47, "#e599f7"),
             poly([(-70, -120), (-145, -150), (-145, -40), (-70, -70)], "#b197fc"),
             poly([(70, -120), (145, -150), (145, -40), (70, -70)], "#b197fc"),
             chemin("M -38 -125 Q -5 -70 25 -122 M 0 -135 Q 35 -78 60 -128", stroke="#fff", sw=10)]
    elif nom == "horloge":
        m = [cercle(0, -120, 112, "#fff", stroke="#364fc7", stroke_width=13),
             trait(0, -120, 0, -194, "#364fc7", 9), trait(0, -120, 57, -120, "#364fc7", 9),
             cercle(0, -120, 10, "#364fc7")]
        for a in range(0, 360, 30):
            t = math.radians(a)
            m.append(cercle(94*math.sin(t), -120-94*math.cos(t), 4, "#364fc7"))
    elif nom == "fanion":
        m = [chemin("M -170 -210 Q 0 -125 170 -210", stroke="#495057", sw=5)]
        for px, py, col in [(-140, -190, "#ff6b6b"), (-70, -155, "#ffd43b"), (0, -144, "#74c0fc"), (70, -155, "#b197fc"), (140, -190, "#69db7c")]:
            m.append(poly([(px-23, py), (px+23, py), (px, py+60)], col))
    elif nom == "ruban":
        m = [chemin("M -120 -175 Q -25 -220 10 -130 Q 75 -65 130 -185", stroke="#f06595", sw=24),
             chemin("M -100 -205 Q -130 -270 -35 -225 Q 0 -200 -10 -172", stroke="#74c0fc", sw=21),
             chemin("M 30 -160 Q 90 -260 140 -210", stroke="#ffd43b", sw=21)]
    elif nom == "carte":
        m = [rect(-115, -200, 230, 190, "#fff", rx=8, stroke="#f06595", stroke_width=6),
             coeur(0, -110, 0.85, "#f06595"),
             trait(-75, -55, 75, -55, "#adb5bd", 6), trait(-75, -34, 40, -34, "#adb5bd", 6)]
    elif nom == "tambour":
        m = [ellipse(0, -125, 105, 27, "#f8f9fa", stroke="#1864ab", stroke_width=6),
             rect(-104, -125, 208, 108, "#4dabf7"), ellipse(0, -17, 104, 23, "#1864ab"),
             ellipse(0, -125, 105, 27, "#f8f9fa", stroke="#1864ab", stroke_width=6),
             trait(-140, -230, -20, -132, "#8d5524", 10), trait(135, -235, 20, -128, "#8d5524", 10)]
    elif nom == "pot":
        m = [rect(-85, -90, 170, 87, "#ff922b", rx=10),
             rect(-98, -105, 196, 25, "#e8590c", rx=8),
             fleur(0, -105, 1.4, "#ff8787", tige=70),
             fleur(-35, -95, 1.0, "#ffd43b", tige=55)]
    elif nom == "graine":
        m = [rect(-85, -80, 170, 78, "#ff922b", rx=10),
             rect(-97, -95, 194, 25, "#e8590c", rx=8),
             chemin("M 0 -94 Q -12 -155 0 -190", stroke="#40c057", sw=9),
             ellipse(-27, -157, 28, 13, "#69db7c", rot=25),
             ellipse(27, -180, 28, 13, "#69db7c", rot=-25)]
    elif nom == "cerf-volant":
        m = [poly([(0, -280), (105, -165), (0, -60), (-105, -165)], "#ff6b6b", stroke="#c92a2a", stroke_width=6),
             trait(0, -280, 0, -60, "#fff", 5), trait(-105, -165, 105, -165, "#fff", 5),
             chemin("M 0 -60 Q 65 20 15 70", stroke="#495057", sw=5)]
        for px, py, col in [(28, -20, "#ffd43b"), (40, 22, "#74c0fc"), (15, 62, "#ffd43b")]:
            m.append(poly([(px-15, py-8), (px, py), (px-15, py+8)], col))
            m.append(poly([(px+15, py-8), (px, py), (px+15, py+8)], col))
    elif nom == "bougie":
        m = [rect(-25, -170, 50, 145, "#74c0fc", rx=9),
             ellipse(0, -193, 20, 32, "#ffd43b"), ellipse(0, -188, 10, 18, "#ff922b"),
             rect(-50, -30, 100, 18, "#f06595", rx=7)]
    else:
        raise ValueError(f"Objet inconnu : {nom}")
    return place(m, x, y, s)


def decor(scene, livre, numero):
    theme = livre["theme"]
    if theme in ("noel", "halloween"):
        fonds = {"noel": ("#2b6cb0", "#d0ebff", "#f1f3f5"),
                 "halloween": ("#5f3dc4", "#d0bfff", "#6741d9")}
        haut, bas, terre = fonds[theme]
        ciel(scene, haut, bas)
        scene.add(lune(675, 140, 58))
        etoiles(scene, 16, graine=numero+4)
        sol(scene, 650, terre, bosse=8)
        if theme == "noel":
            scene.add(sapin(80, 680, 0.8, neige=True), sapin(740, 670, 0.7, neige=True))
    elif theme == "nouvel-an":
        interieur(scene, "#e7f5ff", "#d0bfff", 650)
        scene.add(rect(475, 75, 260, 265, "#1c3b83", rx=15, stroke="#8d5524", stroke_width=12),
                  lune(650, 170, 45), etoile5(530, 140, 11), etoile5(575, 235, 9),
                  etoile5(700, 280, 8))
    elif theme in ("paques", "fete-meres", "fete-peres", "musique"):
        haut = {"paques": "#74c0fc", "fete-meres": "#a5d8ff", "fete-peres": "#74c0fc", "musique": "#91a7ff"}[theme]
        ciel(scene, haut, "#f8f9fa")
        scene.add(nuage(140, 145, 0.7), nuage(680, 210, 0.65))
        sol(scene, 650, "#8ce99a", bosse=12)
        if theme in ("paques", "fete-meres"):
            for px in (55, 110, 690, 745):
                scene.add(fleur(px, 690, 0.8, "#ff8787" if px % 2 else "#ffd43b"))
    else:
        mur = {"carnaval": "#fff0db", "saint-valentin": "#ffe3ec", "anniversaire": "#fff3bf"}[theme]
        interieur(scene, mur, "#e8c39e", 650)
        if theme == "carnaval":
            scene.add(objet("fanion", 400, 280, 1.5))
        elif theme == "saint-valentin":
            scene.add(coeur(115, 180, 0.7), coeur(700, 220, 0.6))
        else:
            scene.add(ballon_air(100, 570, 0.8, "#ff8787"), ballon_air(710, 570, 0.8, "#74c0fc"))


def dessiner(livre, numero=None, vignette=False):
    if vignette:
        scene = Scene(400, 270)
        scene.add(objet(livre["pages"][0][0], 200, 255, 0.82))
        return scene
    scene = Scene()
    decor(scene, livre, 0 if numero is None else numero)
    index = 0 if numero is None else numero
    nom = livre["pages"][index][0]
    taille = 1.2 if numero is not None else 1.45
    scene.add(ellipse(400, 695, 190, 27, "#495057", opacity=0.12))
    scene.add(objet(nom, 400, 630, taille))
    a, b = livre["enfants"]
    theme = livre["theme"]
    if theme == "noel" and index in (3, 4):
        b = "ours"
    elif theme == "halloween" and index in (3, 4):
        b = "renard"
    elif theme == "fete-meres" and index == 5:
        b = "lapin"
    elif theme == "fete-peres" and index >= 3:
        b = "renard"
    # Le personnage principal change de posture au fil du récit.
    poses = ("salut", "joues", "montre", "porte", "haut", "large")
    expressions = ("sourire", "surpris", "concentre", "sourire", "joie", "rire")
    scene.add(perso(a, 150 if index % 2 == 0 else 205, 735, 1.25,
                    expr=expressions[index], bras=poses[index], regard=(1, 0),
                    habit=livre["couleur"]))
    adulte = (theme == "noel" and index in (3, 4)) or (theme == "halloween" and index in (3, 4)) or (theme == "fete-meres" and index == 5) or (theme == "fete-peres" and index >= 3)
    scene.add(perso(b, 655 if index % 2 == 0 else 700, 745, 1.4 if adulte else 1.12,
                    expr="rire" if index == 5 else "sourire", bras="salut" if index % 2 == 0 else "haut",
                    regard=(-1, 0), habit="#ffd43b", acc=("lunettes",) if adulte else ()))
    if numero is None or numero == 5:
        scene.add(paillettes(300, 260, 0.7), paillettes(560, 300, 0.55))
    return scene


def images_pour(identifiant):
    livre = PAR_ID[identifiant]
    images = [("couverture.svg", lambda: dessiner(livre)),
              ("vignette.svg", lambda: dessiner(livre, vignette=True))]
    images.extend((f"{i+1:02d}.svg", lambda i=i: dessiner(livre, i)) for i in range(6))
    return images
