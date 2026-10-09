"""Des cartes pour les amis — oser dire « je t'aime bien ».

Pour la Saint-Valentin, Lou la souris découpe des cœurs : un pour Maman
(« tu fais les meilleurs câlins »), un pour Papi Gus (« les meilleures
histoires »), un pour Tim (« les meilleures grimaces »). Avec le dernier
morceau de papier, elle pense à Bibi, le hérisson qui joue toujours seul :
personne n'ose approcher de ses piquants. Dans la cour, le cœur battant,
elle lui donne sa carte… et Bibi en sort une de sa poche, pour elle.

Plans : 1 moyen (le matériel) · 2 moyen (pour Maman) · 3 gros plan (pour
Papi) · 4 large (pour Tim) · 5 gros plan (le dernier papier) · 6 large (la
classe) · 7 large (la cour) · 8 gros plan (la carte) · 9 moyen (la carte
froissée) · 10 large (la corde à sauter) · 11 moyen (au-dessus du lit).
"""
from base import *
from base import _assombrir
from objets import corde_sauter
from fetes import carte_coeur, coeur_papier

ID = "saint-valentin-cartes"
PAPIER_PEINT = "pois"

LOU = dict(habit="#ffd43b", acc=("noeud",), couleur_acc="#e64980")
MAMAN = dict(couleur="#bfc6cf", habit="#7048e8")
PAPI = dict(couleur="#d0d4d9", habit="#2f9e44", acc=("lunettes",))
TIM = dict(habit="#1c7ed6")
BIBI = dict(habit="#4dabf7", motif="rayures", couleur_motif="#74c0fc")
MAITRESSE = dict(couleur="#a5703f", habit="#12b886", acc=("lunettes",))


def lou(x, y, s=1.3, **k):
    return perso("souris", x, y, s, **{**LOU, **k})


def maman(x, y, s=1.6, **k):
    return perso("souris", x, y, s, **{**MAMAN, **k})


def papi(x, y, s=1.55, **k):
    return perso("souris", x, y, s, **{**PAPI, **k})


def tim(x, y, s=1.2, **k):
    return perso("lapin", x, y, s, **{**TIM, **k})


def bibi(x, y, s=1.2, **k):
    return perso("herisson", x, y, s, **{**BIBI, **k})


def maitresse(x, y, s=1.7, **k):
    return perso("ours", x, y, s, **{**MAITRESSE, **k})


def ciseaux(x, y, s=1.0, rot=0):
    return place([trait(-6, 0, 30, -44, "#adb5bd", 6), trait(6, 0, -30, -44, "#adb5bd", 6),
                  cercle(-12, 12, 11, "none", stroke="#e64980", stroke_width=5),
                  cercle(12, 12, 11, "none", stroke="#e64980", stroke_width=5)], x, y, s, rot=rot)


def pot_colle(x, y, s=1.0):
    return place([rect(-18, -46, 36, 46, "#f8f9fa", rx=6, stroke="#dee2e6", stroke_width=3),
                  rect(-12, -64, 24, 20, "#fab005", rx=4)], x, y, s)


def chambre(S, y=600):
    interieur(S, "#fff0f6", "#e8c39e", y, papier="#fcc2d7")
    S.add(fenetre(560, 100, 160, 140, "#a5d8ff", rideaux="#f783ac"))


def table_bricolage(S, x=400, y=800, w=620):
    S.add(table(x, y, w, 150, "#c68642", nappe="#fff3bf"))
    S.add(ciseaux(x - 200, y - 168, 1.0, rot=-20), pot_colle(x + 210, y - 165))
    for k, c in enumerate(("#e64980", "#fa5252", "#f783ac")):
        S.add(rect(x - 120 + k * 22, y - 182 - k * 3, 90, 60, c, rx=3, transform=f"rotate({-8 + k * 6} {x - 75 + k * 22} {y - 150})"))


def ecole(S, y=620):
    """La classe : tableau, dessins aux murs."""
    interieur(S, "#e6fcf5", "#d9a066", y, papier="#c3fae8")
    S.add(rect(220, 80, 360, 200, "#2b8a3e", rx=8, stroke="#8d5524", stroke_width=12))
    S.add(texte(400, 160, "14 février", 44, "#f8f9fa", poids=500))
    S.add(coeur(400, 230, 1.3, "#ffc9c9"))
    for k, (x, c) in enumerate(((80, "#ffd43b"), (680, "#74c0fc"))):
        S.add(rect(x - 40, 110, 80, 100, "#fff", rx=4), cercle(x, 150, 22, c), trait(x - 20, 190, x + 20, 190, c, 6))


def cour(S, y=620):
    """La cour de l'école, avec son marronnier et son muret."""
    ciel(S, "#a5d8ff", "#fff0f6")
    S.add(nuage(150, 120, 0.7), nuage(620, 90, 0.55))
    S.add(rect(0, y - 120, 800, 120, "#e9d8c4"), pierres(0, y - 120, 800, 120, "#e9d8c4", pas_=26, larg=48, opacite=0.35))
    S.add(rect(0, y - 128, 800, 12, "#ced4da"))
    sol(S, y, "#ced4da", bosse=4)


def coeur_bat(x, y, s=1.0):
    return g([coeur(x, y, 1.4 * s, "#fa5252"), texte(x + 70 * s, y - 10 * s, "boum", 28 * s, "#fa5252", rot=-10),
              texte(x + 90 * s, y + 24 * s, "boum", 22 * s, "#fa5252", rot=10)])


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cour(S)
    for k, (x, y, c) in enumerate(((120, 200, "#f783ac"), (650, 160, "#fa5252"), (520, 300, "#e64980"), (220, 340, "#ffc9c9"))):
        S.add(coeur(x, y, 1.1 + (k % 2) * 0.4, c, rot=(-1) ** k * 12))
    S.add(lou(280, 760, 1.6, expr="timide", bras="donne", regard=(1, 0), objet=carte_coeur(84, -92, 0.9, rot=-8)))
    S.add(bibi(560, 760, 1.5, expr="content", bras="joues", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(carte_coeur(200, 140, 2.0, rot=-6))
    S.add(coeur(330, 60, 0.9, "#fa5252", rot=15), coeur(70, 220, 0.7, "#f783ac", rot=-15))
    return S


def p01():
    """Plan moyen : ciseaux, colle et papier rouge."""
    S = Scene()
    chambre(S)
    S.add(texte(240, 170, "14 février", 50, "#e64980", contour="#fff", rot=-6))
    S.add(lou(400, 640, 1.4, expr="joie", bras="haut", regard=(0, 0.3)))
    table_bricolage(S)
    return S


def pour(S, qui, x=600, y=250, r=120):
    """Bulle de pensée qui montre la personne à qui la carte est destinée."""
    S.add(pensee(x, y, r, qui, depuis=(430, 420)))


def p02():
    """Plan moyen : un cœur pour Maman."""
    S = Scene()
    chambre(S)
    S.add(lou(330, 650, 1.4, expr="concentre", bras="porte", regard=(1, 0.3), objet=coeur_papier(0, -52, 1.7)))
    table_bricolage(S)
    S.add(texte(180, 280, "Snip, snip !", 44, "#e64980", contour="#fff", rot=-8))
    S.add(pensee(600, 250, 150, place(maman(0, 0, 1.0, expr="content", bras="calin"), 600, 390, 0.95)
                 + place(lou(0, 0, 0.62, expr="content", bras="calin"), 600, 390, 0.95), depuis=(400, 420)))
    return S


def p03():
    """Gros plan : un cœur pour Papi Gus, qui raconte des histoires."""
    S = Scene()
    chambre(S)
    S.add(lou(300, 800, 1.9, expr="content", bras="porte", regard=(1, 0), objet=coeur_papier(0, -52, 1.7, ecrit="Papi")))
    S.add(pensee(590, 250, 150, place(papi(0, 0, 1.0, expr="rire", bras="porte",
                                           objet=place([rect(-46, -20, 92, 56, "#1c7ed6", rx=4), rect(-2, -20, 4, 56, "#fff")], 0, -80)),
                                      590, 390, 0.85), depuis=(380, 380)))
    S.camera(1.15, 430, 440)
    S.cachette(90, 760)
    return S


def p04():
    """Plan large : un cœur pour Tim, roi des grimaces ; la table se couvre de cœurs."""
    S = Scene()
    chambre(S)
    S.add(lou(250, 640, 1.2, expr="rire", bras="porte", regard=(1, 0), objet=coeur_papier(0, -52, 1.6)))
    table_bricolage(S)
    for k, (x, c) in enumerate(((350, "#fa5252"), (450, "#f783ac"), (540, "#e64980"))):
        S.add(coeur_papier(x, 630 - (k % 2) * 6, 0.7, c, rot=(-1) ** k * 14))
    S.add(pensee(590, 250, 140, place(tim(0, 0, 1.0, expr="malin", bras="tete"), 590, 380, 0.85), depuis=(330, 400)))
    S.add(texte(160, 290, "Snip, snip !", 44, "#e64980", contour="#fff", rot=-8))
    return S


def p05():
    """Gros plan : le dernier petit morceau de papier ; Lou pense à Bibi, seul."""
    S = Scene()
    chambre(S)
    S.add(lou(320, 820, 2.0, expr="inquiet", bras="porte", regard=(1, -0.3),
              objet=rect(-26, -110, 52, 40, "#fa5252", rx=3, transform="rotate(-8 0 -90)")))
    S.add(pensee(590, 250, 150, g([ellipse(600, 382, 60, 10, "#000", opacity=0.12),
                                    place(bibi(0, 0, 1.0, expr="triste", bras="croises"), 600, 380, 0.8)]), depuis=(390, 340)))
    S.camera(1.15, 430, 440)
    S.cachette(90, 760)
    return S


def p06():
    """Plan large : dans la classe, Lou distribue ses cartes."""
    S = Scene()
    ecole(S)
    S.add(maitresse(660, 720, 1.5, expr="content", bras="porte", regard=(-1, 0), objet=carte_coeur(0, -80, 0.7)))
    S.add(tim(450, 760, 1.15, expr="rire", bras="porte", regard=(-1, 0), objet=carte_coeur(0, -80, 0.6, rot=8)))
    S.add(lou(250, 770, 1.25, expr="rire", bras="donne", regard=(1, 0), objet=carte_coeur(84, -92, 0.6, rot=-8)))
    S.add(bibi(90, 780, 1.0, expr="timide", bras="croises", regard=(1, 0)))
    S.cachette(760, 760)
    return S


def p07():
    """Plan large : Bibi seul dans le coin de la cour ; Lou s'approche, le cœur battant."""
    S = Scene()
    cour(S)
    S.add(arbre(650, 640, 1.4))
    S.add(bibi(650, 740, 0.9, expr="triste", bras="croises", regard=(-1, 0)))
    S.add(lou(250, 780, 1.1, expr="inquiet", bras="porte", regard=(1, 0), pas="marche",
              objet=carte_coeur(0, -80, 0.6)))
    S.add(coeur_bat(250, 420, 1.0))
    for k, (x, esp, c) in enumerate(((120, "lapin", "#1c7ed6"), (420, "chat", "#e8590c"))):
        S.add(perso(esp, x, 610, 0.6, habit=c, expr="rire", bras="saute"))
    S.cachette(40, 770)
    return S


def p08():
    """Gros plan : la carte de Lou pour Bibi."""
    S = Scene()
    cour(S)
    S.add(lou(170, 880, 2.0, expr="timide", bras="donne", regard=(1, 0)))
    m = [rect(-170, -120, 340, 240, "#fff", rx=10, stroke="#f783ac", stroke_width=6),
         coeur(-110, -55, 1.3, "#fa5252"),
         texte(40, -60, "Pour Bibi", 34, "#e64980"),
         texte(0, 0, "Tu es piquant dehors", 26, "#495057", poids=500),
         texte(0, 36, "et tout doux dedans.", 26, "#495057", poids=500),
         texte(0, 82, "Tu veux jouer avec moi ?", 26, "#1c7ed6")]
    S.add(bibi(690, 900, 1.8, expr="surpris", bras="bas", regard=(-1, -0.5)))
    S.add(place(m, 420, 390, 1.0, rot=-4))
    S.camera(1.1, 420, 470)
    S.cachette(720, 418, "air")
    return S


def p09():
    """Plan moyen : Bibi rougit et sort de sa poche une carte toute froissée."""
    S = Scene()
    cour(S)
    S.add(lou(250, 770, 1.45, expr="bouche_bee", bras="joues", regard=(1, 0)))
    froissee = place([poly([(-50, -36), (-10, -42), (46, -34), (52, 0), (44, 36), (0, 30), (-48, 38), (-54, 4)], "#fff4e6",
                           stroke="#ced4da", stroke_width=2),
                      chemin("M -30 -20 L -10 10 L 20 -16 M 0 -30 L 10 20", stroke="#dee2e6", sw=2),
                      coeur(0, 2, 0.6, "#e64980"), texte(0, -14, "Lou", 16, "#1c7ed6")], 0, 0, 1.2, rot=8)
    S.add(bibi(550, 770, 1.45, expr="timide", bras="donne", flip=True, regard=(-1, 0),
               objet=place(froissee, 84, -92, 1.0, flip=True)))
    for x, y in ((470, 380), (640, 360), (690, 430)):
        S.add(coeur(x, y, 0.6, "#fa5252"))
    S.cachette(740, 770)
    return S


def p10():
    """Plan large : tous ensemble à la corde à sauter."""
    S = Scene()
    cour(S)
    S.add(arbre(700, 630, 1.1))
    S.add(tim(150, 740, 1.15, expr="rire", bras="tient", regard=(1, 0)))
    S.add(perso("chat", 650, 740, 1.15, habit="#e8590c", expr="rire", bras="tient", flip=True, regard=(-1, 0)))
    S.add(corde_sauter(150 + 68 * 1.15, 740 - 146 * 1.15, 650 - 68 * 1.15, 740 - 146 * 1.15, bas=160, couleur="#fa5252"))
    S.add(lou(340, 700, 1.1, expr="rire", bras="saute", pas="saute"))
    S.add(bibi(470, 690, 1.05, expr="rire", bras="saute", pas="saute"))
    S.add(texte(400, 250, "Un, deux, trois… sautez !", 40, "#e64980", contour="#fff"))
    S.cachette(40, 770)
    return S


def p11():
    """Plan moyen : le soir, la carte de Bibi au-dessus du lit."""
    S = Scene()
    piece(S, "chambre", 620)
    S.ambiance("nuit")
    S.add(fenetre(580, 90, 150, 140, "#1c2a52", nuit_=True, rideaux="#f783ac"))
    S.add(lampe(100, 640, 0.9))
    S.add(lit(380, 790, 460, "#fff0f6", "#e64980"))
    S.add(place([poly([(-50, -36), (-10, -42), (46, -34), (52, 0), (44, 36), (0, 30), (-48, 38), (-54, 4)], "#fff4e6",
                      stroke="#ced4da", stroke_width=2), coeur(0, 2, 0.6, "#e64980")], 330, 300, 1.4, rot=-6))
    S.add(lou(560, 780, 1.3, expr="content", bras="mains_jointes", regard=(-1, -0.5)))
    S.add(coeur(250, 230, 0.6, "#ffc9c9"), coeur(420, 220, 0.5, "#ffc9c9"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("carte-seule.svg", vignette),
    ("01-le-materiel.svg", p01), ("02-pour-maman.svg", p02), ("03-pour-papi.svg", p03),
    ("04-pour-tim.svg", p04), ("05-le-dernier-papier.svg", p05), ("06-en-classe.svg", p06),
    ("07-dans-la-cour.svg", p07), ("08-la-carte.svg", p08), ("09-la-carte-froissee.svg", p09),
    ("10-tous-ensemble.svg", p10), ("11-au-dessus-du-lit.svg", p11),
]
