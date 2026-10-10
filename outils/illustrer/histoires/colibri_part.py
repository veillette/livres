"""La légende du colibri — d'après une légende amérindienne.

Un grand feu prend dans la forêt. Tous les animaux s'enfuient jusqu'à la
rivière et regardent, terrifiés. Seul le petit colibri s'active : il prend
une goutte d'eau dans son bec, la jette sur le feu, et recommence. Le tatou
se moque : « Tu es fou ! Ce n'est pas avec ces gouttes que tu éteindras le
feu ! » « Je le sais, répond le colibri, mais je fais ma part. » Dans cette
version, les autres l'imitent : le toucan remplit son grand bec, le tapir
sa trompe, les singes des feuilles en coupe, le tatou creuse une tranchée ;
la pluie arrive, le feu s'éteint, et la forêt repousse. Et toi, quelle est
ta part ?

Plans : 1 large (la forêt) · 2 large (le feu) · 3 large (tous à la rivière)
· 4 gros plan (une goutte) · 5 large (l'aller-retour) · 6 moyen (le tatou)
· 7 gros plan (je fais ma part) · 8 large (le toucan, le tapir, les singes)
· 9 large (tous ensemble, la pluie) · 10 large (la forêt repousse) · 11
moyen (et toi ?).
"""
from contes import *
from base import _assombrir

ID = "colibri-part"

ENFANTS = [dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#fab005", robe=True),
           dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#495057"),
           dict(peau="foncee", cheveux="noir", coiffure="afro", habit="#e64980", robe=False, jambes="#364fc7")]


def colibri(x, y, s=1.0, flip=False, goutte_=False, rot=0, expr="sourire"):
    """Le colibri, ailes battantes, long bec fin, tête à droite ; (x, y) = centre du corps."""
    m = [ellipse(-24, -24, 30, 12, "#e7f5ff", opacity=0.7, rot=-50), ellipse(-30, -18, 30, 12, "#d0ebff", opacity=0.6, rot=-30),
         poly([(-30, 4), (-60, -6), (-58, 18)], "#2b8a3e"),
         ellipse(0, 0, 32, 18, volume("#20c997", 0.35, 0.8)), ellipse(10, 8, 16, 8, "#e03131"),
         cercle(24, -8, 13, volume("#12b886", 0.35, 0.8)), trait(34, -8, 74, -2, "#343a40", 3),
         cercle(28, -11, 3.5, ENCRE), cercle(29, -12, 1, "#fff")]
    if expr == "content":
        m[-2] = chemin("M 24 -11 q 4 -4 8 0", stroke=ENCRE, sw=2)
    if goutte_:
        m.append(chemin("M 76 -6 q 6 10 0 14 q -6 -4 0 -14 Z", "#74c0fc", stroke="#4dabf7", sw=1.5))
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 60 * s, y - 50 * s, x + 80 * s, y + 24 * s)


def toucan(x, y, s=1.0, flip=False, eau=False):
    m = [ellipse(0, 0, 34, 44, volume("#212529", 0.3, 0.8)), ellipse(6, -10, 16, 20, "#fff3bf"), cercle(4, -40, 22, "#212529"),
         chemin("M 18 -50 Q 80 -56 96 -34 Q 70 -24 18 -30 Z", volume("#fd7e14", 0.35, 0.8)), cercle(12, -44, 6, "#74c0fc"), cercle(13, -44, 3, ENCRE),
         trait(-6, 40, -10, 56, "#495057", 4), trait(8, 40, 10, 56, "#495057", 4)]
    if eau:
        m.append(chemin("M 30 -36 Q 60 -38 86 -34", stroke="#74c0fc", sw=6))
    return place(m, x, y, s, flip=flip)


def tatou(x, y, s=1.0, flip=False, expr="malin"):
    """Tatou de profil, tête à droite ; (x, y) = au sol."""
    m = [ellipse(-20, -6, 16, 8, "#868e96"), ellipse(30, -6, 16, 8, "#868e96"),
         chemin("M -80 -10 Q -76 -80 0 -84 Q 70 -80 76 -10 Z", volume("#adb5bd", 0.3, 0.8))]
    for k in range(5):
        m.append(chemin(f"M {-50 + k * 24} -78 Q {-46 + k * 24} -40 {-50 + k * 24} -10", stroke="#868e96", sw=4))
    m += [chemin("M -80 -20 Q -120 -10 -130 -30", stroke="#adb5bd", sw=10),
          chemin("M 70 -50 Q 120 -50 130 -24 Q 100 -14 70 -20 Z", volume("#ced4da", 0.3, 0.8)), ellipse(80, -60, 8, 16, "#ced4da", rot=-20),
          cercle(100, -38, 4, ENCRE)]
    if expr == "malin":
        m.append(trait(92, -48, 106, -46, ENCRE, 2.5))
    return place(m, x, y, s, flip=flip)


def tapir(x, y, s=1.0, flip=False, eau=False):
    m = [rect(-60, -50, 20, 50, "#343a40", rx=8), rect(40, -50, 20, 50, "#343a40", rx=8),
         ellipse(0, -80, 90, 50, volume("#495057", 0.3, 0.8)), ellipse(90, -90, 34, 28, volume("#495057", 0.3, 0.8)),
         chemin("M 116 -86 Q 146 -80 150 -60", stroke="#495057", sw=12), cercle(94, -100, 4, ENCRE), ellipse(76, -116, 8, 12, "#343a40")]
    if eau:
        for k in range(5):
            m.append(trait(150 + k * 6, -56 + k * 2, 170 + k * 8, -20 + k * 6, "#74c0fc", 3))
    return place(m, x, y, s, flip=flip)


def feuille_coupe(x, y, s=1.0):
    return place([chemin("M -40 0 Q 0 30 40 0 Q 0 10 -40 0 Z", "#2f9e44"), ellipse(0, 4, 30, 6, "#74c0fc")], x, y, s)


def flammes(S, x, y, s=1.0, graine=1, nb=5):
    r = random.Random(graine)
    for k in range(nb):
        px = x + (k - nb / 2) * 60 * s
        h = r.uniform(120, 200) * s
        S.add(chemin(f"M {px - 40 * s} {y} Q {px - 20 * s} {y - h * 0.6} {px} {y - h} Q {px + 20 * s} {y - h * 0.6} {px + 40 * s} {y} Z", "#ff922b"))
        S.add(chemin(f"M {px - 20 * s} {y} Q {px - 8 * s} {y - h * 0.4} {px} {y - h * 0.6} Q {px + 10 * s} {y - h * 0.4} {px + 20 * s} {y} Z", "#ffd43b"))
    S.lumiere(x, y - 80 * s, 260 * s, "#ff922b", 0.5)


def fumee(S, x, y, s=1.0):
    for k in range(5):
        S.add(cercle(x + k * 30 * s, y - k * 60 * s, (40 + k * 10) * s, "#868e96", opacity=0.35))


def jungle(S, horizon=540, brule=False, repousse=False, graine=1, riviere=False):
    """La forêt ; brule : en feu (ciel orangé, troncs noircis) ; repousse : après la pluie (ciel bleu, cendre et pousses vertes)."""
    rougeoie = brule and not repousse
    ciel(S, "#ffc078" if rougeoie else "#74c0fc", "#fff4e6" if rougeoie else "#e7f5ff")
    r = random.Random(graine)
    for k in range(8):
        x = -40 + k * 120 + r.uniform(-20, 20)
        if brule and 300 < x < 700:
            S.add(rect(x - 10, horizon - 200, 20, 200, "#495057"))
            continue
        S.add(rect(x - 14, horizon - 240, 28, 240, cylindre("#7c4a1e", 0.3, 0.75)))
        for j in range(4):
            a = -150 + j * 40
            S.add(place([ellipse(60, 0, 70, 22, volume("#2b8a3e" if j % 2 else "#37b24d", 0.35, 0.8))], x, horizon - 240, rot=a))
    S.add(rect(0, horizon, 800, 800 - horizon, terrain("#5c940d" if not brule else ("#8a9a5b" if repousse else "#868e96"))))
    if repousse:
        for k in range(16):
            px = 260 + (k * 37) % 460
            S.add(chemin(f"M {px} {horizon + 80 + (k % 4) * 40} q -8 -16 -14 -22 M {px} {horizon + 80 + (k % 4) * 40} q 6 -18 12 -24", stroke="#8ce99a", sw=4))
    if riviere:
        S.add(chemin(f"M 0 {horizon + 140} Q 400 {horizon + 100} 800 {horizon + 160} L 800 {horizon + 260} Q 400 {horizon + 220} 0 {horizon + 260} Z",
                     volume("#4dabf7", 0.3, 0.8)))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jungle(S, 600, graine=2)
    fumee(S, 600, 420, 1.0)
    S.add(colibri(400, 380, 3.2, goutte_=True, expr="content"))
    S.add(fleur(120, 720, 1.4, "#e64980"), fleur(680, 740, 1.2, "#fab005"))
    S.cachette(740, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(colibri(200, 140, 1.8))
    return S


def p01():
    """Plan large : la grande forêt ; le toucan, les singes, le tatou, la tortue… et le petit colibri qui butine une fleur."""
    S = Scene()
    jungle(S, 540, graine=1)
    S.add(toucan(140, 420, 1.2), perso("singe", 620, 800, 0.9, expr="rire", bras="haut"))
    S.add(tatou(330, 790, 1.0, expr="sourire"), tortue(500, 790, 0.9))
    S.add(fleur(260, 640, 1.5, "#e64980"))
    S.add(colibri(340, 500, 1.4))
    S.add(texte(400, 120, "La grande forêt", 52, "#2b8a3e", contour="#fff"))
    return S


def p02():
    """Plan large : un jour, de la fumée s'élève au-dessus des arbres : le feu !"""
    S = Scene()
    jungle(S, 560, brule=True, graine=3)
    fumee(S, 380, 380, 1.2)
    flammes(S, 480, 600, 1.1, graine=3, nb=6)
    S.add(colibri(140, 300, 1.0, expr="sourire"))
    S.add(texte(400, 110, "Le feu !", 70, "#c92a2a", contour="#fff"))
    return S


def p03():
    """Plan large : tous les animaux s'enfuient jusqu'à la rivière et regardent le feu, terrifiés."""
    S = Scene()
    jungle(S, 420, brule=True, graine=4, riviere=True)
    flammes(S, 560, 420, 0.7, graine=4, nb=5)
    S.add(perso("singe", 140, 760, 0.8, expr="inquiet", bras="joues"), toucan(280, 690, 0.9), tatou(400, 780, 0.8, expr="sourire"),
          tortue(560, 780, 0.8, expr="inquiet"), tapir(680, 790, 0.7, flip=True))
    S.add(texte(400, 110, "Tous à la rivière !", 52, "#c92a2a", contour="#fff"))
    return S


def p04():
    """Gros plan : le colibri plonge son bec dans la rivière et prend une goutte d'eau."""
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    S.add(rect(0, 500, 800, 300, volume("#4dabf7", 0.3, 0.8)))
    for k in range(6):
        S.add(chemin(f"M {60 + k * 130} {560 + (k % 2) * 60} q 20 -8 40 0", stroke="#d0ebff", sw=4))
    S.add(colibri(360, 440, 3.6, rot=40, goutte_=True))
    for k in range(3):
        S.add(ellipse(560, 510, 40 + k * 30, 8 + k * 4, "none", stroke="#d0ebff", stroke_width=3, opacity=0.8 - k * 0.2))
    S.add(texte(400, 110, "Une goutte d'eau", 54, "#1c7ed6", contour="#fff"))
    S.cachette(740, 300, "air")
    return S


def p05():
    """Plan large : le colibri vole jusqu'au feu, lâche sa goutte… et repart en chercher une autre, encore et encore."""
    S = Scene()
    jungle(S, 540, brule=True, graine=5, riviere=False)
    flammes(S, 600, 600, 1.0, graine=5, nb=4)
    S.add(chemin("M 120 700 Q 300 300 560 420", stroke="#495057", sw=3, stroke_dasharray="8 10"))
    S.add(chemin("M 560 440 Q 320 560 140 720", stroke="#495057", sw=3, stroke_dasharray="8 10"))
    S.add(colibri(520, 400, 1.2, goutte_=True))
    S.add(chemin("M 610 420 q 6 10 0 14 q -6 -4 0 -14 Z", "#74c0fc"))
    S.add(rect(0, 700, 260, 100, volume("#4dabf7", 0.3, 0.8)))
    S.add(texte(400, 110, "Aller, retour, aller, retour…", 44, "#c92a2a", contour="#fff"))
    return S


def p06():
    """Plan moyen : sur la rive, le tatou se moque : « Colibri, tu es fou ! Ce n'est pas avec tes gouttes que tu vas éteindre le feu ! »"""
    S = Scene()
    jungle(S, 480, brule=True, graine=6, riviere=True)
    S.add(tatou(300, 790, 1.8, expr="malin"))
    S.add(colibri(620, 420, 1.4, flip=True, goutte_=True))
    S.add(bulle(330, 150, 500, 130, "Colibri, tu es fou ! Ce n'est pas\navec tes gouttes que tu vas\néteindre le feu !", 28, pointe=(420, 600)))
    return S


def p07():
    """Gros plan : le petit colibri répond : « Je le sais. Mais je fais ma part. »"""
    S = Scene()
    ciel(S, "#ffc078", "#fff4e6")
    S.add(colibri(380, 470, 4.2, flip=True, goutte_=True, expr="content"))
    S.add(bulle(400, 150, 460, 120, "Je le sais.\nMais je fais ma part.", 40, pointe=(330, 330)))
    S.cachette(740, 790, "air")
    return S


def p08():
    """Plan large : le toucan remplit son grand bec, le tapir sa trompe, les singes des feuilles en coupe : ils font leur part, eux aussi."""
    S = Scene()
    jungle(S, 460, brule=True, graine=7, riviere=True)
    S.add(toucan(160, 420, 1.3, eau=True), tapir(560, 700, 1.0, flip=False, eau=True))
    S.add(perso("singe", 300, 790, 0.9, expr="concentre", bras="porte", objet=feuille_coupe(0, -80, 1.0)),
          perso("singe", 400, 800, 0.8, expr="rire", bras="porte", objet=feuille_coupe(0, -80, 0.9)))
    S.add(colibri(560, 300, 1.0, goutte_=True))
    S.add(texte(400, 110, "Moi aussi ! Moi aussi !", 52, "#2b8a3e", contour="#fff"))
    return S


def p09():
    """Plan large : tous ensemble, ils portent l'eau ; le tatou creuse une tranchée ; et la pluie se met à tomber."""
    S = Scene()
    jungle(S, 540, brule=True, graine=8)
    S._decor("pluie")
    S.add(rect(0, 0, 800, 300, "#868e96", opacity=0.5))
    for x, y, sc in ((140, 120, 1.4), (420, 100, 1.6), (680, 130, 1.4)):
        S.add(nuage(x, y, sc, "#ced4da", ombre="#adb5bd"))
    flammes(S, 620, 640, 0.5, graine=8, nb=3)
    S.add(chemin("M 0 720 Q 300 700 520 740", stroke="#5c3d24", sw=18))
    S.add(tatou(420, 760, 0.8, expr="sourire"))
    S.add(toucan(200, 460, 0.9, eau=True), perso("singe", 120, 800, 0.7, expr="rire", bras="porte", objet=feuille_coupe(0, -80, 0.9)),
          tapir(540, 790, 0.7, eau=True))
    S.add(colibri(560, 400, 1.0, goutte_=True))
    pluie(S, 70, graine=9)
    S.add(texte(400, 290, "Tous ensemble !", 52, "#fff", contour="#1c7ed6"))
    return S


def p10():
    """Plan large : le feu est éteint ; sur la cendre, les premières pousses vertes ; les animaux fêtent le colibri."""
    S = Scene()
    jungle(S, 540, graine=10, repousse=True, brule=True)
    S.add(perso("singe", 120, 800, 0.85, expr="rire", bras="haut"), toucan(260, 480, 1.0), tatou(420, 790, 0.9, expr="sourire"),
          tortue(560, 790, 0.8), tapir(690, 790, 0.6, flip=True))
    S.add(colibri(400, 300, 1.6, expr="content"))
    S.add(texte(400, 110, "La forêt est sauvée !", 50, "#2b8a3e", contour="#fff"))
    return S


def p11():
    """Plan moyen : aujourd'hui, des enfants font leur part : planter un arbre, ramasser un papier, fermer le robinet. « Et toi ? »"""
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, 480, "#b2f2bb", graine=11)
    S.add(rect(0, 540, 800, 260, terrain("#8ce99a")))
    S.add(ellipse(290, 770, 60, 12, "#8d5f3a"), place([trait(0, 0, 0, -110, "#7c4a1e", 7), cercle(0, -140, 46, volume("#51cf66", 0.35, 0.8)),
                                                        cercle(-30, -120, 30, volume("#40c057", 0.35, 0.8))], 290, 770, 1.0))
    S.add(personne(140, 800, 1.5, expr="rire", bras="donne", regard=(1, 0.5), **ENFANTS[0]))
    S.add(rect(500, 660, 80, 130, volume("#40c057", 0.3, 0.8), rx=8), rect(494, 650, 92, 16, "#2f9e44", rx=4),
          texte(540, 740, "♻", 40, "#fff"))
    S.add(personne(430, 800, 1.5, expr="content", bras="ramasse", regard=(0.5, 0.8), **ENFANTS[1]))
    S.add(rect(456, 770, 30, 22, "#fff", rx=3, rot=20))
    S.add(personne(680, 800, 1.5, expr="rire", bras="salut", flip=True, regard=(-0.5, -1), **ENFANTS[2]))
    S.add(colibri(620, 320, 1.2, flip=True, expr="content"))
    S.add(texte(400, 120, "Et toi, quelle est ta part ?", 46, "#2b8a3e", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("colibri-seul.svg", vignette),
    ("01-la-foret.svg", p01), ("02-le-feu.svg", p02), ("03-a-la-riviere.svg", p03),
    ("04-une-goutte.svg", p04), ("05-aller-retour.svg", p05), ("06-le-tatou.svg", p06),
    ("07-je-fais-ma-part.svg", p07), ("08-moi-aussi.svg", p08), ("09-tous-ensemble.svg", p09),
    ("10-la-foret-repousse.svg", p10), ("11-et-toi.svg", p11),
]
