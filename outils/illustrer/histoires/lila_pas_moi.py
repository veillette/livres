"""Ce n'est pas moi ! — Lila accuse le chat, puis dit la vérité.

Lila dessine… et la feuille est trop petite : elle dessine sur le mur. Papa
arrive : « Qui a dessiné sur le mur ? » « Ce n'est pas moi, c'est
Pompon ! » Un chat qui tient un crayon ? Alors c'est un dragon invisible !
Mais Pompon s'en va, vexé, et Lila a tout bizarre dans le ventre. Elle dit
la vérité ; Papa la remercie (« C'est courageux »), ils nettoient le mur
ensemble, Lila demande pardon à Pompon, et Papa colle au mur une immense
feuille où l'on peut dessiner aussi grand qu'on veut.

Plans : 1 moyen (Lila dessine) · 2 large (le mur) · 3 moyen (qui a
dessiné ?) · 4 moyen (c'est Pompon !) · 5 moyen (un chat qui tient un
crayon ?) · 6 moyen (le dragon invisible) · 7 moyen (tout bizarre dans le
ventre) · 8 gros plan (c'est moi) · 9 moyen (merci) · 10 large (on nettoie)
· 11 gros plan (pardon, Pompon) · 12 large (la grande feuille).
"""
from base import *
from base import _assombrir
from objets import chat_profil
from fantastique import personne, mains_personne

ID = "lila-pas-moi"

LILA = dict(peau="brune", cheveux="noir", coiffure="couettes", habit="#ff8787", robe=True)
PAPA = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#4dabf7", robe=False, jambes="#495057",
            barbe="#2b2b3a", carrure="ronde", nez="rond")
GRIS_POMPON = "#ced4da"
CRAYONS = ("#fa5252", "#fab005", "#40c057", "#4dabf7", "#be4bdb")


def lila(x, y, s=1.6, **k):
    return personne(x, y, s, **{**LILA, **k})


def papa(x, y, s=1.95, **k):
    return personne(x, y, s, **{**PAPA, **k})


def pompon(x, y, s=1.0, **k):
    return chat_profil(x, y, s, couleur=GRIS_POMPON, rayures=True, collier="#e64980", **k)


def crayons_main():
    """Trois crayons tenus (repère local du personnage, main droite de la pose « tient »)."""
    return g([place([rect(-5, -40, 10, 50, c, rx=2), poly([(-5, -40), (5, -40), (0, -52)], "#ffe8cc")], 68 + k * 8, -146, rot=-10 + k * 10)
              for k, c in enumerate(CRAYONS[:3])])


def dessins_mur(S, x=400, y=330, s=1.0, effaces=0.0):
    """Les dessins de Lila sur le mur, au crayon de couleur."""
    o = 1 - effaces
    m = [cercle(-180, -80, 46, "none", stroke=CRAYONS[1], stroke_width=8)]
    for k in range(10):
        a = math.radians(k * 36)
        m.append(trait(-180 + math.cos(a) * 60, -80 + math.sin(a) * 60, -180 + math.cos(a) * 84, -80 + math.sin(a) * 84, CRAYONS[1], 7))
    m += [chemin("M -40 80 L -40 -10 L 20 -60 L 80 -10 L 80 80 Z", "none", stroke=CRAYONS[0], sw=8),
          rect(5, 20, 30, 60, "none", stroke=CRAYONS[3], stroke_width=7)]
    m += [cercle(200, 0, 40, "none", stroke="#868e96", stroke_width=7),
          chemin("M 168 -24 L 172 -64 L 190 -36 M 210 -36 L 228 -64 L 232 -24", stroke="#868e96", sw=7),
          cercle(186, -6, 5, "#868e96"), cercle(214, -6, 5, "#868e96"), chemin("M 192 14 Q 200 22 208 14", stroke="#868e96", sw=5)]
    m += [trait(150, 120, 150, 60, CRAYONS[2], 7), cercle(150, 50, 16, "none", stroke=CRAYONS[4], stroke_width=7),
          chemin("M -200 120 q 30 -30 60 0 q 30 30 60 0 q 30 -30 60 0", stroke=CRAYONS[4], sw=7)]
    return place(g(m, opacity=o), x, y, s)


def salon(S, dessins=True, effaces=0.0):
    interieur(S, "#fff9db", "#d9b48f", y=600, papier=None)
    if dessins:
        S.add(dessins_mur(S, 400, 330, 1.0, effaces))
    S.add(tapis(400, 730, 300, 56, "#e5dbff", "#b197fc"))


def canape(x, y, w=360, couleur="#ffa94d"):
    return g([rect(x - w / 2, y - 200, w, 110, volume(couleur, 0.3, 0.8), rx=28),
              rect(x - w / 2 + 10, y - 110, w - 20, 70, volume(couleur, 0.25, 0.75), rx=18),
              rect(x - w / 2 - 26, y - 140, 52, 130, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=22),
              rect(x + w / 2 - 26, y - 140, 52, 130, volume(_assombrir(couleur, 0.9), 0.3, 0.8), rx=22)])


def table_basse(x, y, w=260):
    return g([rect(x - w / 2, y - 80, w, 18, "#c68642", rx=6), rect(x - w / 2 + 12, y - 62, 14, 62, "#a0693a"), rect(x + w / 2 - 26, y - 62, 14, 62, "#a0693a")])


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    salon(S)
    S.add(pompon(630, 790, 1.7, expr="vexe", flip=True))
    S.add(lila(300, 800, 1.75, expr="malin", bras="designe", regard=(1, 0.2)))
    S.cachette(60, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pompon(200, 250, 1.2, expr="vexe"))
    return S


def p01():
    """Plan moyen : Lila dessine à la table basse ; Pompon dort sur le canapé."""
    S = Scene()
    salon(S, dessins=False)
    S.add(cadre_mur(130, 140, 120, 100, "#ffe066"), fenetre(560, 110, 170, 160, "#a5d8ff", rideaux="#ffc9c9"))
    S.add(canape(560, 790, 380))
    S.add(pompon(560, 680, 1.0, pose="dort"))
    S.add(lila(260, 800, 1.6, expr="concentre", bras="porte", regard=(0, 1)))
    S.add(table_basse(260, 800, 300))
    S.add(rect(190, 700, 140, 20, "#fff", rx=3), cercle(240, 708, 6, CRAYONS[1]), cercle(280, 710, 5, CRAYONS[0]))
    for k, c in enumerate(CRAYONS):
        S.add(place([rect(-4, -26, 8, 34, c, rx=2)], 350 + k * 12, 714, rot=80 + k * 4))
    S.add(zzz(600, 560, 0.9))
    return S


def p02():
    """Plan large : la feuille est trop petite : Lila dessine sur le mur, un grand soleil, une maison, un chat."""
    S = Scene()
    salon(S)
    S.add(lila(560, 800, 1.6, expr="rire", bras="tient", regard=(-1, -0.6), flip=True, objet=crayons_main()))
    S.add(texte(230, 560, "Encore plus grand !", 36, "#e64980", contour="#fff"))
    return S


def p03():
    """Plan moyen : Papa entre : « Oh ! Qui a dessiné sur le mur ? » ; Lila cache ses crayons dans son dos."""
    S = Scene()
    salon(S)
    S.add(papa(600, 800, 1.95, expr="surpris", bras="joues", flip=True, regard=(-1, -0.3)))
    S.add(lila(250, 800, 1.6, expr="oups", bras="croises", regard=(1, -0.2)))
    for k, c in enumerate(CRAYONS[:3]):
        S.add(place([rect(-4, -26, 8, 34, c, rx=2)], 300 + k * 8, 690, rot=20 + k * 12))
    S.add(bulle(560, 150, 380, 110, "Oh ! Qui a dessiné\nsur le mur ?", 32, pointe=(590, 330)))
    return S


def p04():
    """Plan moyen : Lila montre le chat du doigt : « Ce n'est pas moi ! C'est Pompon ! » ; Pompon est vexé."""
    S = Scene()
    salon(S)
    S.add(papa(680, 800, 1.95, expr="neutre", bras="croises", flip=True, regard=(-1, 0.3)))
    S.add(pompon(440, 790, 1.4, expr="vexe", flip=True))
    S.add(lila(190, 800, 1.6, expr="malin", bras="designe", regard=(1, 0.4)))
    S.add(bulle(250, 150, 380, 110, "Ce n'est pas moi !\nC'est Pompon !", 34, pointe=(220, 330)))
    S.cachette(570, 70, "air")
    return S


def p05():
    """Plan moyen : Papa : « Pompon sait tenir un crayon ? » ; dans une bulle, Pompon dessine, un crayon dans la patte."""
    S = Scene()
    salon(S)
    S.add(papa(600, 800, 1.95, expr="malin", bras="pense", flip=True, regard=(-1, 0.3)))
    S.add(lila(220, 800, 1.6, expr="inquiet", bras="bas", regard=(1, -0.3)))
    S.add(pensee(310, 240, 140, depuis=(560, 400)))
    S.add(chat_profil(300, 320, 0.9, couleur=GRIS_POMPON, collier="#e64980", pose="assis", expr="content"))
    S.add(place([rect(-4, -30, 8, 40, CRAYONS[0], rx=2)], 342, 276, rot=30), texte(240, 200, "?", 40, "#868e96"))
    S.add(bulle(640, 130, 290, 110, "Pompon sait tenir\nun crayon ?", 30, pointe=(610, 300)))
    return S


def p06():
    """Plan moyen : « Alors… c'est un dragon invisible ! » ; Lila agite les bras ; on devine un dragon transparent ; Papa lève un sourcil."""
    S = Scene()
    salon(S)
    dragon = g([chemin("M -120 40 Q -60 -60 20 -40 Q 80 -100 120 -60 Q 150 -30 110 0 Q 140 40 80 50 Q 0 80 -120 40 Z", "#fff", stroke="#74c0fc", sw=5),
                chemin("M -20 -40 L -40 -110 L 10 -60 Z M 20 -50 L 30 -120 L 50 -60 Z", "#fff", stroke="#74c0fc", sw=4),
                cercle(100, -40, 6, "#74c0fc")], opacity=0.55)
    S.add(place(dragon, 380, 300, 1.2))
    S.add(papa(640, 800, 1.95, expr="malin", bras="hanches", flip=True, regard=(-1, 0)))
    S.add(lila(260, 800, 1.6, expr="joie", bras="haut", regard=(1, -0.5)))
    S.add(texte(380, 120, "C'est un dragon invisible !", 42, "#1c7ed6", contour="#fff"))
    return S


def p07():
    """Plan moyen : Pompon s'en va, la queue basse ; Lila le regarde partir, les mains sur le ventre : tout bizarre."""
    S = Scene()
    salon(S)
    S.add(pompon(620, 790, 1.4, pose="debout", expr="vexe"))
    S.add(lila(280, 800, 1.6, expr="triste", bras="calin", regard=(1, 0.2)))
    S.add(chemin("M 250 620 q 10 -16 24 0 q 12 16 26 0 q 10 -14 22 0", stroke="#e64980", sw=4, opacity=0.8))
    S.add(texte(400, 130, "Ça fait tout bizarre…", 46, "#e64980", contour="#fff"))
    return S


def p08():
    """Gros plan : Lila, les yeux baissés, tire Papa par la manche : « Papa… c'est moi. »"""
    S = Scene()
    salon(S)
    S.add(papa(620, 940, 2.3, expr="content", bras="bas", flip=True, regard=(-1, 0.8)))
    S.add(lila(300, 900, 2.0, expr="timide", bras="main", regard=(1, 0.5)))
    S.camera(1.1, 420, 520)
    S.dessus(bulle(300, 150, 420, 110, "Papa… c'est moi. Je voulais\nfaire un beau dessin.", 30, pointe=(310, 270)))
    S.cachette(611, 136, "air")
    return S


def p09():
    """Plan moyen : Papa serre Lila dans ses bras : « Merci de m'avoir dit la vérité. C'est courageux. »"""
    S = Scene()
    salon(S)
    S.add(coeur(400, 280, 2.6, "#ffdeeb"))
    S.add(papa(470, 800, 1.95, expr="content", bras="calin", regard=(-0.5, 0.5)))
    S.add(lila(350, 810, 1.45, expr="content", bras="calin", regard=(1, -0.5)))
    S.add(bulle(560, 140, 420, 110, "Merci de m'avoir dit la vérité.\nC'est courageux.", 28, pointe=(520, 300)))
    return S


def p10():
    """Plan large : Papa et Lila frottent le mur avec une éponge ; les dessins s'effacent ; Pompon regarde."""
    S = Scene()
    salon(S, effaces=0.6)
    S.add(rect(380, 700, 80, 90, volume("#74c0fc", 0.3, 0.8), rx=10), ellipse(420, 700, 40, 10, "#d0ebff"))
    S.add(papa(600, 800, 1.95, expr="content", bras="salut", flip=True, regard=(-1, -0.5),
               objet=place([rect(-26, -16, 52, 32, "#ffd43b", rx=8)], 74, -160)))
    S.add(lila(220, 800, 1.6, expr="concentre", bras="salut", regard=(1, -0.5),
               objet=place([rect(-22, -14, 44, 28, "#69db7c", rx=8)], 74, -160)))
    S.add(pompon(730, 790, 0.9, expr="sourire", flip=True))
    for k in range(6):
        S.add(cercle(300 + k * 40, 260 + (k % 2) * 30, 10, "#fff", stroke="#a5d8ff", stroke_width=2))
    S.add(texte(400, 120, "Frotte, frotte !", 52, "#1c7ed6", contour="#fff"))
    return S


def p11():
    """Gros plan : Lila caresse Pompon : « Pardon, Pompon. » ; Pompon ronronne : « Ronron ! »"""
    S = Scene()
    salon(S, dessins=False)
    S.add(pompon(570, 820, 2.2, expr="content", flip=True))
    S.add(lila(240, 900, 2.0, expr="content", bras="tend", regard=(1, 0.4)))
    S.camera(1.1, 420, 540)
    S.dessus(bulle(260, 150, 300, 90, "Pardon, Pompon.", 34, pointe=(270, 260)))
    S.dessus(texte(620, 300, "Ronron !", 48, "#868e96", contour="#fff"))
    S.cachette(193, 136, "air")
    return S


def p12():
    """Plan large : Papa a collé une immense feuille au mur ; Lila y dessine Pompon et un dragon, aussi grand qu'elle veut."""
    S = Scene()
    salon(S, dessins=False)
    S.add(rect(120, 120, 560, 420, "#fff", stroke="#dee2e6", stroke_width=4))
    for x, y in ((120, 120), (680, 120), (120, 540), (680, 540)):
        S.add(rect(x - 18, y - 8, 36, 16, "#ffe066", opacity=0.8, rot=30))
    S.add(cercle(300, 300, 60, "none", stroke="#868e96", stroke_width=8),
          chemin("M 254 260 L 260 210 L 284 246 M 316 246 L 340 210 L 346 260", stroke="#868e96", sw=8),
          cercle(282, 292, 6, "#868e96"), cercle(318, 292, 6, "#868e96"))
    S.add(place(g([chemin("M -120 40 Q -60 -60 20 -40 Q 80 -100 120 -60 Q 150 -30 110 0 Q 140 40 80 50 Q 0 80 -120 40 Z", "none", stroke=CRAYONS[2], sw=8),
                   chemin("M -20 -40 L -40 -110 L 10 -60 Z", "none", stroke=CRAYONS[0], sw=6), cercle(100, -40, 6, CRAYONS[2])]), 520, 330, 0.9))
    S.add(papa(680, 800, 1.95, expr="rire", bras="hanches", flip=True, regard=(-1, -0.3)))
    S.add(lila(330, 800, 1.6, expr="rire", bras="tient", regard=(0, -1), objet=crayons_main()))
    S.add(pompon(110, 790, 0.9, expr="content"))
    S.cachette(240, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pompon-seul.svg", vignette),
    ("01-lila-dessine.svg", p01), ("02-sur-le-mur.svg", p02), ("03-qui-a-dessine.svg", p03),
    ("04-c-est-pompon.svg", p04), ("05-un-crayon.svg", p05), ("06-le-dragon.svg", p06),
    ("07-tout-bizarre.svg", p07), ("08-c-est-moi.svg", p08), ("09-merci.svg", p09),
    ("10-frotte.svg", p10), ("11-pardon-pompon.svg", p11), ("12-la-grande-feuille.svg", p12),
]
