"""Hugo, infirmier — Camille se casse le bras.

Camille tombe de sa trottinette. À l'hôpital, Hugo, infirmier, l'accueille
(bracelet à son nom), prend sa température et sa tension (« ça serre comme
un câlin »). La radio montre l'os cassé ; la médecin et Hugo posent un
plâtre, que Camille choisit violet. Les infirmiers veillent aussi la nuit.
Hugo dessine sur le plâtre ; six semaines plus tard, la scie à plâtre, qui
vibre sans couper la peau, l'enlève. Camille repart, casquée.

Plans : 1 large (la chute) · 2 moyen (le bracelet) · 3 gros plan (la
température, la tension) · 4 moyen (la radio) · 5 moyen (le plâtre) ·
6 gros plan (la couleur) · 7 large (la nuit à l'hôpital) · 8 gros plan
(le dessin) · 9 moyen (la scie à plâtre) · 10 large (avec un casque).
"""
from base import *
from base import _assombrir, POSES, COUDES
from fantastique import personne, mains_personne, ancre
from metiers import pro, stethoscope, badge, blouse, cabinet
from objets import velo

ID = "infirmier-hugo"

VERT_SOIN = "#38d9a9"
HUGO = dict(stature="adulte", peau="claire", cheveux="brun", coiffure="courts", habit=VERT_SOIN, jambes=VERT_SOIN,
            chaussures="#f8f9fa", tenue=g([stethoscope(), badge(22, -92, "#fff", "rond")]), nez="long", carrure="fine")
DOCTEURE = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="afro", habit="#ffffff", jambes="#495057",
                tenue=blouse(), acc=("lunettes",), robe=False)
CAMILLE = dict(peau="rosee", cheveux="roux", coiffure="tresses", habit="#ffd43b", robe=False, jambes="#1c7ed6", taches=True)
PAPA = dict(stature="adulte", peau="rosee", cheveux="chatain", coiffure="courts", habit="#495057", robe=False, jambes="#364fc7",
            barbe="#8d5524", carrure="ronde")
VIOLET = "#9775fa"


def hugo(x, y, s=1.35, **k):
    return pro(x, y, s, **{**HUGO, **k})


def platre(bras="bas", couleur=VIOLET, dessin=False):
    """Plâtre sur l'avant-bras gauche d'un enfant (repère local du personnage)."""
    (mx, my), _ = POSES[bras]
    coude = (COUDES.get(bras, (None, None))[0]) or (-28 + (mx + 28) * 0.5, -98 + (my + 98) * 0.5)
    ax, ay = coude[0] + (mx - coude[0]) * 0.1, coude[1] + (my - coude[1]) * 0.1
    bx, by = coude[0] + (mx - coude[0]) * 0.86, coude[1] + (my - coude[1]) * 0.86
    m = [trait(ax, ay, bx, by, _assombrir(couleur, 0.8), 26), trait(ax, ay, bx, by, couleur, 22),
         trait(ax, ay, bx, by, eclaircir(couleur, 0.4), 6, opacity=0.6)]
    if dessin:
        cx, cy = (ax + bx) / 2, (ay + by) / 2
        m += [cercle(cx, cy, 8, "none", stroke="#fff", stroke_width=2), cercle(cx - 3, cy - 2, 1.2, "#fff"), cercle(cx + 3, cy - 2, 1.2, "#fff"),
              chemin(f"M {n(cx - 4)} {n(cy + 2)} Q {n(cx)} {n(cy + 6)} {n(cx + 4)} {n(cy + 2)}", stroke="#fff", sw=1.5)]
    return g(m)


def camille(x, y, s=1.2, platre_=None, **k):
    bras = k.get("bras", "bas")
    if platre_:
        k["objet"] = g([k.get("objet") or "", platre(bras, *platre_)])
    return personne(x, y, s, **{**CAMILLE, **k})


def lit_hopital(x, y, s=1.0, couverture="#a5d8ff"):
    """Lit d'hôpital à barrières ; (x, y) = milieu du pied ; le matelas est à y - 150 s."""
    m = [ellipse(0, 6, 230, 12, "#000", opacity=0.1),
         rect(-210, -150, 420, 40, "#fff", rx=10), rect(-210, -120, 420, 20, "#adb5bd", rx=6),
         rect(-200, -168, 110, 36, "#fff", rx=16, stroke="#e9ecef", stroke_width=3),
         rect(-90, -170, 300, 50, lineaire([(0, couverture), (1, _assombrir(couverture, 0.85))]), rx=14),
         trait(-200, -110, -200, -10, "#868e96", 8), trait(200, -110, 200, -10, "#868e96", 8),
         cercle(-200, -6, 10, "#343a40"), cercle(200, -6, 10, "#343a40"),
         rect(-224, -260, 18, 160, "#ced4da", rx=6), rect(206, -210, 18, 110, "#ced4da", rx=6)]
    for k in range(5):
        m.append(trait(-150 + k * 70, -196, -150 + k * 70, -150, "#adb5bd", 4))
    m.append(trait(-170, -196, 150, -196, "#adb5bd", 5))
    return place(m, x, y, s)


def trottinette(x, y, s=1.0, rot=0):
    return place([trait(-90, 0, 90, 0, "#fa5252", 12), trait(80, 0, 100, -170, "#495057", 8), trait(78, -170, 122, -170, "#495057", 8),
                  cercle(-80, 10, 14, "#343a40"), cercle(90, 10, 14, "#343a40")], x, y, s, rot=rot)


def hopital(S, y=600):
    cabinet(S, "#e6fcf5", "#c3fae8", y, plinthe="#63e6be")
    S.add(fenetre(80, 100, 170, 150, "#a5d8ff", rideaux="#63e6be",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), arbre(170, 330, 0.5)])))


def negatoscope(x, y, s=1.0):
    """Écran lumineux qui montre la radio de l'avant-bras : deux os, l'un fendu."""
    m = [rect(-130, -100, 260, 200, "#343a40", rx=10), rect(-118, -88, 236, 176, "#1c2a52", rx=6),
         chemin("M -90 -40 Q 0 -30 90 -50", stroke="#e9ecef", sw=14), chemin("M -90 20 Q 0 30 90 10", stroke="#e9ecef", sw=16),
         chemin("M 10 -44 L 4 -32 L 14 -30 L 8 -18", stroke="#fa5252", sw=4)]
    return place(m, x, y, s)


def machine_radio(x, y, s=1.0):
    return place([rect(-20, -420, 40, 420, "#ced4da", rx=8), rect(-140, -440, 280, 40, "#adb5bd", rx=10),
                  rect(60, -470, 120, 100, volume("#e9ecef", 0.3, 0.8), rx=14), cercle(120, -370, 36, "#495057"),
                  rect(-200, -190, 400, 30, "#dee2e6", rx=8)], x, y, s)


def scie(x, y, s=1.0, rot=0):
    return place([rect(-20, -90, 40, 90, "#fab005", rx=12), cercle(0, -110, 26, "#ced4da", stroke="#868e96", stroke_width=3),
                  chemin("M -40 -110 l 8 0 M 40 -110 l -8 0 M 0 -150 l 0 8", stroke="#495057", sw=3)], x, y, s, rot=rot)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    hopital(S)
    S.add(lit_hopital(540, 790, 1.2))
    S.add(camille(540, 640, 1.3, platre_=(VIOLET, True), expr="rire", bras="bas", regard=(-1, 0)))
    S.add(rect(540 - 90 * 1.2, 790 - 170 * 1.2, 300 * 1.2, 60, lineaire([(0, "#a5d8ff"), (1, _assombrir("#a5d8ff", 0.85))]), rx=14))
    S.add(hugo(250, 790, 1.5, expr="content", bras="salut", regard=(1, 0)))
    S.cachette(740, 780)
    return S


def vignette():
    S = Scene(400, 270)
    croix = g([rect(-20, -60, 40, 120, "#fa5252", rx=6), rect(-60, -20, 120, 40, "#fa5252", rx=6)])
    S.add(place(croix, 110, 140, 1.0))
    S.add(coeur(290, 150, 3.0, "#38d9a9"))
    return S


def p01():
    """Plan large : au parc, Camille est tombée de sa trottinette ; Papa la console."""
    S = Scene()
    paysage(S, 540, 610, graine=3)
    S.add(arbre(120, 640, 1.0), arbre(700, 630, 0.9))
    S.add(chemin("M 0 700 Q 400 660 800 700 L 800 760 Q 400 720 0 760 Z", "#e9c99a"))
    S.add(trottinette(560, 730, 0.9, rot=12))
    S.add(camille(330, 760, 1.15, expr="pleure", bras="calin", larmes=True, regard=(1, 0)))
    S.add(personne(450, 770, 1.3, expr="inquiet", bras="epaule", flip=True, regard=(-1, 0.3), **PAPA))
    S.add(bulle(330, 150, 300, 90, "Aïe, mon bras !", 36, pointe=(330, 460)))
    return S


def p02():
    """Plan moyen : à l'hôpital, Hugo l'infirmier accueille Camille et lui met un bracelet."""
    S = Scene()
    hopital(S)
    S.add(hugo(520, 790, 1.45, expr="content", bras="donne", flip=True, regard=(-1, 0.3)))
    hx, hy = mains_personne(520, 790, 1.45, "donne", flip=True, stature="adulte")[0]
    S.add(place(rect(-26, -8, 52, 16, "#fff", rx=8, stroke="#74c0fc", stroke_width=3), hx - 10, hy))
    S.add(camille(280, 790, 1.25, expr="timide", bras="tend", regard=(1, 0)))
    S.add(personne(130, 790, 1.35, expr="content", bras="bas", regard=(1, 0), **PAPA))
    S.add(bulle(520, 140, 420, 110, "Bonjour, Camille !\nMoi, c'est Hugo.", 34, pointe=(520, 420)))
    return S


def p03():
    """Gros plan : le thermomètre dans l'oreille ; le brassard qui serre le bras."""
    S = Scene()
    hopital(S)
    S.add(lit_hopital(400, 820, 1.2))
    S.add(camille(400, 660, 1.4, expr="surpris", bras="bas", regard=(1, -0.2)))
    S.add(rect(400 + 30 * 1.4, 660 - 90 * 1.4, 34, 40, "#4dabf7", rx=8))
    S.add(hugo(620, 860, 1.6, expr="content", bras="tient", flip=True, regard=(-1, 0),
               objet=place(rect(-12, -40, 24, 60, "#fff", rx=8, stroke="#adb5bd", stroke_width=2), *ancre(68, -146, "tient", "adulte"))))
    S.camera(1.35, 470, 450)
    S.dessus(bulle(240, 110, 380, 100, "Ça serre…\ncomme un câlin !", 32, pointe=S.vers_page(440, 520)))
    return S


def p04():
    """Plan moyen : la radio ; sur l'écran lumineux, on voit l'os fendu."""
    S = Scene()
    hopital(S)
    S.add(machine_radio(240, 790, 1.0))
    S.add(negatoscope(560, 300, 1.1))
    S.add(camille(200, 600, 0.95, expr="bouche_bee", bras="bas", regard=(1, -0.5), ombre=False))
    S.add(personne(600, 790, 1.4, expr="content", bras="designe", flip=True, regard=(-1, -0.5), **DOCTEURE))
    S.add(bulle(420, 470, 260, 80, "Voici ton os !", 32, pointe=(580, 520)))
    return S


def p05():
    """Plan moyen : la médecin et Hugo posent le plâtre."""
    S = Scene()
    hopital(S)
    S.add(lit_hopital(400, 800, 1.1))
    S.add(camille(400, 640, 1.2, expr="concentre", bras="tend", regard=(-1, 0.3)))
    S.add(hugo(160, 790, 1.4, expr="concentre", bras="tend", regard=(1, 0.2)))
    S.add(personne(650, 790, 1.4, expr="content", bras="tend", flip=True, regard=(-1, 0.2), **DOCTEURE))
    S.add(rect(320, 480, 70, 34, "#f8f9fa", rx=14, stroke="#dee2e6", stroke_width=3))
    S.add(texte(400, 140, "Le plâtre durcit en séchant.", 36, "#0ca678", contour="#fff"))
    return S


def p06():
    """Gros plan : Camille choisit la couleur de son plâtre : violet !"""
    S = Scene()
    hopital(S)
    for k, c in enumerate(("#ff8787", "#74c0fc", VIOLET, "#69db7c", "#ffd43b")):
        S.add(rect(200 + k * 90, 520, 70, 120, volume(c, 0.3, 0.8), rx=30))
    S.add(camille(400, 900, 1.9, expr="rire", bras="designe", regard=(1, -0.5)))
    S.camera(1.2, 420, 520)
    S.dessus(bulle(560, 110, 300, 90, "Violet !", 44, pointe=S.vers_page(400 + 140, 560)))
    return S


def p07():
    """Plan large : la nuit, Hugo fait sa ronde dans le couloir ; tout le monde dort."""
    S = Scene()
    hopital(S)
    S.ambiance("nuit")
    S.add(lit_hopital(250, 790, 0.9))
    S.add(camille(250, 790 - 150 * 0.9 + 6, 0.75, expr="dort", rot=-90, platre_=(VIOLET,), ombre=False))
    S.add(rect(110, 640, 310, 50, "#a5d8ff", rx=14))
    S.add(lampe(470, 720, 0.6))
    S.add(hugo(640, 790, 1.35, expr="content", bras="chut", regard=(-1, 0.2)))
    S.add(lune(170, 150, 22))
    S.add(zzz(330, 560, 0.8, "#5c7cfa"))
    S.add(texte(600, 120, "Chut…", 56, "#5c7cfa", contour="#fff"))
    return S


def p08():
    """Gros plan : Hugo dessine un sourire sur le plâtre violet de Camille."""
    S = Scene()
    hopital(S)
    S.add(camille(330, 850, 1.9, expr="rire", bras="bas", platre_=(VIOLET, True), regard=(1, 0.4)))
    S.add(hugo(620, 870, 1.8, expr="content", bras="tend", flip=True, regard=(-1, 0.4),
               objet=place(rect(-4, -40, 8, 50, "#212529", rx=3), *ancre(40, -94, "tend", "adulte"), rot=-30)))
    S.camera(1.25, 400, 560)
    S.dessus(texte(400, 110, "Un plâtre qui sourit !", 46, VIOLET, contour="#fff"))
    return S


def p09():
    """Plan moyen : six semaines plus tard, la scie à plâtre ouvre le plâtre, sans couper la peau."""
    S = Scene()
    hopital(S)
    S.add(lit_hopital(380, 800, 1.1))
    S.add(camille(380, 640, 1.2, expr="surpris", bras="tend", platre_=(VIOLET, True), regard=(1, 0.3)))
    S.add(hugo(600, 790, 1.4, expr="content", bras="tend", flip=True, regard=(-1, 0.3), objet=scie(*ancre(40, -94, "tend", "adulte"), 0.8, rot=-60)))
    S.add(mouvement(440, 470, 0.7, "#fab005"))
    S.add(bulle(260, 140, 420, 100, "Ça chatouille !", 36, pointe=(370, 400)))
    return S


def p10():
    """Plan large : de retour au parc, Camille, casque sur la tête, file sur sa trottinette."""
    S = Scene()
    paysage(S, 540, 610, graine=7)
    S.add(arbre(110, 640, 0.9))
    S.add(chemin("M 0 700 Q 400 660 800 700 L 800 760 Q 400 720 0 760 Z", "#e9c99a"))
    casque = g([chemin("M -60 -170 Q -62 -236 0 -236 Q 62 -236 60 -170 Q 0 -182 -60 -170 Z", VIOLET),
                chemin("M -30 -222 Q 0 -232 30 -222", stroke="#fff", sw=6, opacity=0.7)])
    S.add(trottinette(450, 745, 1.0))
    S.add(camille(430, 735, 1.15, expr="rire", bras="guidon", coiffe=casque, regard=(1, 0)))
    S.add(personne(160, 770, 1.3, expr="rire", bras="applaudit", regard=(1, 0), **PAPA))
    S.add(mouvement(330, 640, 1.0, "#868e96", rot=180))
    S.add(texte(440, 150, "Avec un casque, cette fois !", 38, "#0ca678", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("croix-seule.svg", vignette),
    ("01-la-chute.svg", p01), ("02-le-bracelet.svg", p02), ("03-ca-serre.svg", p03),
    ("04-la-radio.svg", p04), ("05-le-platre.svg", p05), ("06-violet.svg", p06),
    ("07-la-nuit.svg", p07), ("08-le-dessin.svg", p08), ("09-la-scie.svg", p09),
    ("10-avec-un-casque.svg", p10),
]
