"""Petit Ours ne veut pas dormir — le jour et la nuit.

La lampe (le Soleil) est à gauche, le nord de l'orange (la Terre) en haut :
la face avant de l'orange tourne de la gauche vers la droite (vers l'est).
L'autocollant passe donc de midi (face à la lampe) au coucher du Soleil,
puis à la nuit. Dehors, on regarde vers le sud : le Soleil se lève à gauche
(est), passe au sud à midi et se couche à droite (ouest). À midi, en France,
le Soleil n'est jamais tout à fait au-dessus de la tête : l'ombre est courte
mais pas nulle, tournée vers le nord.
"""
from base import *
from objets import *
from sciences import *

ID = "ours-nuit"
PETIT = dict(habit="#9775fa", motif="pois", couleur_motif="#e5dbff")
PYJAMA = dict(habit="#9775fa", motif="pois", couleur_motif="#e5dbff", acc=("bonnet",), couleur_acc="#9775fa")
MAMAN = dict(habit="#f783ac", acc=("fleur",), couleur_acc="#fcc2d7")


def petit_ours(x, y, s=1.0, pyjama=False, **k):
    return perso("ours", x, y, s, **{**(PYJAMA if pyjama else PETIT), **k})


def maman(x, y, s=1.0, **k):
    return perso("ours", x, y, s, **{**MAMAN, **k})


def paysage(S, haut, bas, graine=1, y=600, herbe_="#8ce99a", herbe2="#69db7c"):
    ciel(S, haut, bas)
    collines(S, y, eclaircir(herbe_, 0.3), graine=graine)
    sol(S, y, herbe_, couleur2=herbe2, y2=y + 90)


def orange(S, x, y, r, angle_autocollant=180, lumiere=180, fleche_=False):
    """L'orange-Terre éclairée par la lampe ; l'autocollant est à `angle_autocollant`
    (180 = face à la lampe à gauche, 270 = face à nous, 0 = côté opposé)."""
    m = [cercle(x, y, r, "#ff922b")]
    cid = uid("o")
    m.append(el("clipPath", cercle(x, y, r, "#000"), id=cid))
    m.append(g([cercle(x + r * 0.2 * math.cos(k), y + r * 0.2 * math.sin(k), 3, "#e8590c") for k in range(12)], clip_path=f"url(#{cid})"))
    # position de l'autocollant vue de face : x = r·cos(a), visible si 180 ≤ a ≤ 360 (face avant)
    a = math.radians(angle_autocollant)
    visible = math.sin(a) <= 0.05
    ax = x + r * 0.9 * math.cos(a)
    if visible:
        k = max(1.0, r / 90)
        m.append(place([rect(-14, -8, 28, 22, "#fff"), poly([(-18, -8), (0, -24), (18, -8)], "#fa5252"), rect(-4, 4, 8, 10, "#a0693a")], ax, y - 6, k))
    m.append(g(rect(x, y - r - 2, r + 2, 2 * r + 4, "#1b1f3b", opacity=0.65), clip_path=f"url(#{cid})",
               transform=f"rotate({n(lumiere + 180)} {n(x)} {n(y)})"))
    m.append(trait(x, y - r - 40, x, y + r + 40, "#868e96", 5))
    m.append(chemin(f"M {x - 10} {y - r + 4} q 10 -14 20 0", "#2f9e44"))
    if fleche_:
        m.append(fleche_courbe(f"M {x - r * 0.8} {y + r * 0.55} Q {x} {y + r * 1.0} {x + r * 0.8} {y + r * 0.55}", (x + r * 0.8, y + r * 0.55), -30, "#fff", 6))
    return g(m)


def couverture():
    S = Scene()
    S.add(rect(0, 0, 400, 800, S.degrade(["#74c0fc", "#fff3bf"])), rect(400, 0, 400, 800, S.degrade(["#1c2a52", "#5f3dc4"])))
    S.add(soleil(170, 170, 60, visage=True))
    etoiles(S, 25, 1, (420, 0, 800, 500))
    S.add(lune_phase(640, 170, 60, 0.25, True, sombre="#3b3d8a"))
    S.add(chemin("M 0 640 Q 200 610 400 640 L 400 800 L 0 800 Z", "#8ce99a"), chemin("M 400 640 Q 600 610 800 640 L 800 800 L 400 800 Z", "#364fc7"))
    S.add(petit_ours(400, 770, 1.8, pyjama=True, expr="baille", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(petit_ours(200, 262, 1.0, pyjama=True, expr="content", bras="bas"))
    S.add(lune_phase(330, 70, 34, 0.3, True, halo=False))
    return S


def p01():
    S = Scene()
    paysage(S, "#f76707", "#ffd8a8", 1, 620)
    S.add(cercle(640, 600, 70, "#ffd43b"))
    collines(S, 620, "#b2f2bb", graine=21)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=710)
    S.add(maison(150, 690, 0.8, lumiere=True))
    S.add(maman(560, 770, 1.6, expr="content", bras="montre", flip=True, regard=(-1, 0)))
    S.add(petit_ours(350, 770, 1.3, expr="fache", bras="croises"))
    S.add(bulle(330, 150, 320, 80, "Oh non !", 44, pointe=(340, 480)))
    return S


def p02():
    S = Scene()
    paysage(S, "#e8590c", "#ffc078", 2, 620)
    S.add(cercle(560, 610, 70, "#ffd43b"))
    collines(S, 620, "#b2f2bb", graine=22)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=710)
    S.add(petit_ours(230, 770, 1.4, expr="surpris", regard=(1, 0), bras="montre"))
    S.add(maman(430, 770, 1.6, expr="sourire", regard=(-1, 0)))
    S.add(bulle(420, 130, 560, 90, "C'est la Terre qui tourne !", 38, pointe=(450, 420)))
    return S


def p03():
    S = Scene()
    interieur(S, "#5f3dc4", "#3b2a7a", y=620)
    S.add(cercle(200, 350, 260, "#fff3bf", opacity=0.25))
    S.add(table(220, 790, 220, 170, "#a0693a"))
    S.add(lampe(220, 622, 1.3, allumee=False), cercle(220, 440, 36, "#ffe066"))
    S.add(orange(S, 520, 340, 70, 200))
    S.add(maman(560, 780, 1.4, expr="sourire", bras="haut", regard=(0, -1)))
    S.add(petit_ours(360, 790, 1.0, expr="bouche_bee", regard=(1, -1)))
    S.add(texte(220, 150, "le Soleil", 40, "#ffe066"), texte(520, 200, "la Terre", 40, "#ffc078"))
    return S


def page_orange(angle, texte_=None, fleche_=False, couleur_t="#ffe066"):
    S = Scene()
    fond(S, "#15183a")
    etoiles(S, 30, int(angle), (0, 0, 800, 800))
    S.add(cercle(80, 400, 330, "#fff3bf", opacity=0.12), cercle(80, 400, 220, "#fff3bf", opacity=0.15))
    S.add(cercle(80, 400, 110, "#ffe066"))
    S.add(orange(S, 470, 400, 220, angle, fleche_=fleche_))
    if texte_:
        S.add(texte(470, 730, texte_, 56, couleur_t))
    return S


def p04():
    # maison face à la lampe : il fait jour chez nous
    return page_orange(200, "le jour")


def p05():
    # l'orange tourne : la face avant va de gauche à droite, l'autocollant s'en va vers l'ombre
    return page_orange(262, fleche_=True)


def p06():
    return page_orange(330, "la nuit", couleur_t="#b197fc")


def p07():
    S = Scene()
    S.add(rect(0, 0, 400, 800, "#1c2a52"), rect(400, 0, 400, 800, "#a5d8ff"))
    etoiles(S, 20, 7, (0, 0, 400, 400))
    S.add(lune_phase(300, 100, 36, 0.6, True))
    S.add(lit(200, 760, 330, "#e5dbff", "#9775fa"))
    S.add(cercle(110, 600, 48, "#b07a4f"), cercle(80, 562, 16, "#b07a4f"), cercle(140, 562, 16, "#b07a4f"))
    S.add(oeil(96, 600, "fermes"), oeil(124, 600, "fermes"), zzz(160, 520, 0.9, "#e5dbff"))
    S.add(soleil(700, 110, 50, visage=True))
    S.add(rect(400, 620, 400, 180, "#ffe8cc"))
    S.add(enfant(610, 740, 1.2, peau="foncee", cheveux="noir", coiffure="tresses", habit="#20c997", expr="rire", bras="ouverts"))
    S.add(table(610, 800, 330, 150, "#c68642", nappe="#ffc9c9"))
    S.add(tasse(540, 630, 1.1), assiette(670, 645, 1.0))
    S.add(rect(396, 0, 8, 800, "#fff"))
    return S


def p08():
    S = Scene()
    paysage(S, "#91a7ff", "#ffe8cc", 8, 600)
    S.add(cercle(120, 580, 150, "#ffe066", opacity=0.3), soleil(120, 560, 50, visage=True))
    collines(S, 600, "#b2f2bb", graine=28)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=690)
    S.add(maison(620, 690, 0.8))
    S.add(ombre_portee(S, petit_ours(0, 0, 1.5, expr="rire", bras="haut"), 360, 770, 1.6, 1))
    S.add(petit_ours(360, 770, 1.5, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(texte(120, 440, "est", 50, "#e8590c", contour="#fff"))
    return S


def p09():
    S = Scene()
    paysage(S, "#339af0", "#d0ebff", 9, 600)
    S.add(soleil(400, 90, 60, visage=True))
    S.add(texte(560, 110, "midi", 50, "#1c7ed6", contour="#fff"), texte(400, 210, "sud", 36, "#1c7ed6", contour="#fff"))
    S.add(ellipse(400, 790, 55, 22, "#1b1f3b", opacity=0.3))
    S.add(petit_ours(400, 770, 1.7, expr="surpris", regard=(0, 1)))
    return S


def p10():
    S = Scene()
    ciel(S, "#5f3dc4", "#ff922b")
    S.add(rect(0, 300, 800, 300, S.degrade(["#f783ac00", "#f783ac"]), opacity=0.5))
    S.add(cercle(680, 580, 150, "#ffe066", opacity=0.25), cercle(680, 580, 55, "#ffd43b"))
    collines(S, 600, "#9775fa", graine=10)
    sol(S, 600, "#7048e8", couleur2="#5f3dc4", y2=690)
    S.add(ombre_portee(S, petit_ours(0, 0, 1.5, expr="content", bras="salut"), 360, 770, 1.6, -1))
    S.add(petit_ours(360, 770, 1.5, expr="content", bras="salut", regard=(1, 0)))
    S.add(texte(680, 460, "ouest", 50, "#fff3bf", contour="#5f3dc4"))
    return S


def p11():
    S = Scene()
    nuit(S, "#141c3a", "#34427a")
    etoiles(S, 50, 11, (0, 0, 800, 480))
    S.add(lune_phase(660, 110, 45, 0.7, True))
    collines(S, 600, "#243463", graine=11)
    sol(S, 600, "#1d2a52")
    S.add(arbre(130, 620, 1.0, "#2b8a3e", "#237032"))
    S.add(chouette(150, 400, 0.8, expr="content"))
    S.add(chauve_souris(430, 220, 0.9, expr="rire"))
    S.add(perso("renard", 560, 760, 1.2, expr="malin", regard=(-1, 0)))
    S.add(perso("herisson", 320, 770, 1.0, expr="content", regard=(1, 0)))
    return S


def p12():
    S = Scene()
    nuit(S, "#070b1c", "#1b2348")
    etoiles(S, 140, 12, (0, 0, 800, 620))
    r = random.Random(12)
    for _ in range(12):
        S.add(etoile5(r.uniform(0, 800), r.uniform(0, 560), r.uniform(8, 14), "#fff3bf"))
    collines(S, 640, "#1b2348", graine=12)
    sol(S, 640, "#141c3a")
    S.add(petit_ours(400, 770, 1.6, pyjama=True, expr="bouche_bee", bras="ouverts", regard=(0, -1)))
    return S


def p13():
    S = Scene()
    fond(S, "#15183a")
    etoiles(S, 40, 13, (0, 0, 800, 800))
    S.add(cercle(80, 400, 330, "#fff3bf", opacity=0.12), cercle(80, 400, 110, "#ffe066"))
    S.add(orange(S, 440, 470, 150, 250))
    S.add(boule_eclairee(680, 260, 50, "#e9ecef", "#1b1f3b", 170, opacity=0.8))
    S.add(g([trait(190, 360 + k * 30, 620, 250 + k * 18, "#ffe066", 3, stroke_dasharray="12 10", opacity=0.7) for k in range(3)]))
    S.add(texte(680, 180, "la Lune", 44, "#e9ecef"))
    return S


def p14():
    S = Scene()
    S.add(rect(0, 0, 400, 800, S.degrade(["#74c0fc", "#ffd8a8"])))
    S.add(soleil(200, 330, 45))
    S.add(rect(0, 560, 400, 240, "#8ce99a"))
    S.add(horloge(90, 110, 50, 9, 0), texte(90, 205, "21 h", 40, "#e8590c", contour="#fff"))
    S.add(texte(290, 110, "été", 56, "#e8590c", contour="#fff"))
    S.add(petit_ours(210, 760, 1.2, expr="rire", bras="haut"))
    S.add(rect(400, 0, 400, 800, S.degrade(["#141c3a", "#3b4a8a"])))
    etoiles(S, 25, 14, (410, 0, 800, 480))
    S.add(lune_phase(700, 330, 40, 0.5, True, sombre="#2a3563"))
    S.add(rect(400, 560, 400, 240, "#f1f3f5"))
    flocons(S, 25, 14, (410, 0, 800, 560))
    S.add(horloge(510, 110, 50, 5, 0), texte(510, 205, "17 h", 40, "#b197fc"))
    S.add(texte(700, 110, "hiver", 56, "#e5dbff"))
    S.add(petit_ours(600, 760, 1.2, expr="surpris", acc=("bonnet", "echarpe"), couleur_acc="#fa5252", habit="#4dabf7"))
    S.add(rect(396, 0, 8, 800, "#fff"))
    return S


def p15():
    S = Scene()
    interieur(S, "#e5dbff", "#b197fc", y=620)
    S.add(fenetre(90, 90, 170, 160, "#1c2a52", nuit_=True, rideaux="#9775fa"))
    S.add(orange(S, 610, 300, 70, 330))
    S.add(rect(560, 400, 100, 14, "#a0693a", rx=4))
    S.add(petit_ours(380, 780, 1.7, pyjama=True, expr="fier", bras="hanches"))
    return S


def p16():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=620)
    S.add(fenetre(530, 80, 180, 170, "#141c3a", nuit_=True))
    S.add(lit(330, 780, 440, "#e5dbff", "#9775fa"))
    S.add(cercle(210, 628, 50, "#b07a4f"), cercle(176, 588, 17, "#b07a4f"), cercle(244, 588, 17, "#b07a4f"))
    S.add(g([chemin("M 160 612 Q 170 560 210 556 Q 260 556 262 604 Q 210 586 160 612 Z", "#9775fa"), cercle(270, 560, 12, "#fff")]))
    S.add(ellipse(210, 648, 24, 18, "#ecd0ae"), ellipse(210, 640, 9, 6, ENCRE))
    S.add(oeil(193, 622, "fermes"), oeil(227, 622, "fermes"))
    S.add(zzz(270, 520, 1.0, "#e5dbff"))
    # rêve : de l'autre côté de la Terre, le Soleil brille
    S.add(pensee(400, 260, 150, "", "#fff9db", depuis=(270, 520)))
    S.add(cercle(300, 260, 26, "#ffd43b"))
    S.add(boule_eclairee(430, 260, 70, "#1c7ed6", "#141c3a", 180))
    S.add(cercle(410, 240, 22, "#51cf66"), cercle(455, 285, 18, "#51cf66", opacity=0.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("ours-seul.svg", vignette),
    ("01-au-lit.svg", p01), ("02-question.svg", p02), ("03-lampe-orange.svg", p03), ("04-le-jour.svg", p04),
    ("05-elle-tourne.svg", p05), ("06-la-nuit.svg", p06), ("07-autre-cote.svg", p07), ("08-matin.svg", p08),
    ("09-midi.svg", p09), ("10-couchant.svg", p10), ("11-animaux-de-nuit.svg", p11), ("12-etoiles.svg", p12),
    ("13-la-lune.svg", p13), ("14-ete-hiver.svg", p14), ("15-pyjama.svg", p15), ("16-bonne-nuit.svg", p16),
]
