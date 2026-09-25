"""Oups, une tache ! — les erreurs peuvent devenir des idées."""
from base import *
from objets import *

ID = "chat-tache"
ZOU = dict(acc=("tablier",))
PAPA = dict(couleur="#e8590c", habit="#20c997")
MAMIE = dict(couleur="#ced4da", acc=("lunettes",), habit="#e599f7")
BLEU = "#4dabf7"


def tache(x, y, r=60, graine=1, couleur=BLEU, n_=14):
    rnd = random.Random(graine)
    pts = []
    for k in range(n_):
        a = k * 2 * math.pi / n_
        rr = r * rnd.uniform(0.75, 1.2)
        pts.append((x + math.cos(a) * rr, y + math.sin(a) * rr * 0.8))
    d = f"M {n(pts[0][0])} {n(pts[0][1])} " + " ".join(
        f"Q {n(p[0])} {n(p[1])} {n((p[0] + q[0]) / 2)} {n((p[1] + q[1]) / 2)}" for p, q in zip(pts, pts[1:] + pts[:1]))
    m = [chemin(d + " Z", couleur)]
    for k in range(5):
        a = rnd.uniform(0, 2 * math.pi)
        m.append(cercle(x + math.cos(a) * r * 1.4, y + math.sin(a) * r * 1.1, rnd.uniform(4, 9), couleur))
    return g(m)


def dessin_soleil(x, y, s=1.0):
    return soleil(x, y, 40 * s, "#ffd43b", visage=True)


def feuille(x, y, w, h, contenu="", rot=0, froissee=False):
    m = [rect(-w / 2 + 6, -h / 2 + 8, w, h, "#000", opacity=0.1), rect(-w / 2, -h / 2, w, h, "#fff")]
    if froissee:
        for k in range(6):
            m.append(trait(-w / 2 + k * w / 6, -h / 2, -w / 2 + (k + 1) * w / 6 - 20, h / 2, "#dee2e6", 3))
    m.append(contenu)
    return place(m, x, y, 1.0, rot=rot)


def baleine(x, y, s=1.0):
    m = [tache(0, 0, 70, graine=3),
         chemin("M 70 -10 Q 110 -50 120 -20 Q 110 0 120 20 Q 110 40 70 10 Z", BLEU),
         cercle(-38, -10, 8, "#fff"), cercle(-38, -10, 4, ENCRE),
         chemin("M -60 20 Q -40 34 -20 24", stroke=ENCRE, sw=4)]
    for k in (-1, 0, 1):
        m.append(chemin(f"M -10 -60 Q {k * 20 - 10} -100 {k * 40 - 10} -110", stroke="#74c0fc", sw=6))
    return place(m, x, y, s)


def poisson_tache(x, y, s=1.0, couleur="#ff922b"):
    m = [tache(0, 0, 24, graine=8, couleur=couleur, n_=10), poly([(22, 0), (44, -16), (44, 16)], couleur),
         cercle(-10, -4, 4, "#fff"), cercle(-10, -4, 2, ENCRE)]
    return place(m, x, y, s)


def vague(x, y, w=300, couleur="#1c7ed6"):
    d = f"M {x - w / 2} {y} " + " ".join(f"q 25 -30 50 0" for _ in range(int(w / 50)))
    return chemin(d, stroke=couleur, sw=6)


def atelier(S):
    interieur(S, "#fff9db", "#d9a066", 610, papier="#fff3bf")
    S.add(fenetre(600, 100, 150, 140, "#a5d8ff", rideaux="#69db7c"))


def couverture():
    S = Scene()
    atelier(S)
    S.add(feuille(560, 480, 260, 200, baleine(0, 10, 0.8), rot=6))
    S.add(tache(180, 520, 40, graine=5, couleur="#ff6b6b"), tache(640, 700, 34, graine=6, couleur="#ffd43b"))
    S.add(perso("chat", 330, 760, 1.6, expr="rire", bras="montre", **ZOU, objet=pinceau(84, -126, 1.0, BLEU, rot=20)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(perso("chat", 180, 265, 0.9, expr="content", bras="donne", **ZOU, objet=pinceau(84, -96, 1.0, BLEU, rot=20)))
    S.add(tache(330, 150, 26, graine=4))
    return S


def chevalet(x, y, contenu, s=1.0):
    m = [trait(-110, 0, -60, -420, "#a0693a", 12), trait(110, 0, 60, -420, "#a0693a", 12), trait(0, -20, 0, -400, "#a0693a", 10),
         rect(-150, -190, 300, 16, "#a0693a", rx=4),
         feuille(0, -300, 280, 210, contenu)]
    return place(m, x, y, s)


def p01():
    S = Scene()
    atelier(S)
    S.add(chevalet(530, 760, dessin_soleil(-40, -10, 1.3), 1.05))
    S.add(pot_peinture(700, 760, 1.0, BLEU), pot_peinture(380, 770, 0.8, "#ff6b6b"))
    S.add(perso("chat", 230, 770, 1.5, expr="concentre", bras="montre", regard=(1, -0.5), **ZOU,
                objet=pinceau(86, -128, 1.0, "#ffd43b", rot=50)))
    S.add(texte(250, 200, "Pour Mamie", 54, "#e8590c", contour="#fff"))
    return S


def p02():
    S = Scene()
    atelier(S)
    S.add(feuille(420, 330, 420, 300, dessin_soleil(-80, -40, 1.2) + tache(40, 30, 90, graine=2)))
    S.add(pot_peinture(640, 560, 1.4, BLEU, renverse=True))
    S.add(perso("chat", 200, 770, 1.5, expr="oups", bras="joues", regard=(1, -0.5), **ZOU))
    S.add(texte(560, 130, "SPLATCH !", 80, BLEU, contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    atelier(S)
    S.add(perso("chat", 380, 760, 1.8, expr="pleure", bras="bas", larmes=True, **ZOU))
    S.add(g([cercle(640, 720, 60, "#fff"), chemin("M 600 700 L 650 730 L 620 760 M 660 680 L 680 740", stroke="#dee2e6", sw=4),
             tache(660, 700, 16, graine=9)]))
    S.add(texte(400, 200, "C'est raté !", 64, "#495057"))
    return S


def p04():
    S = Scene()
    atelier(S)
    S.add(perso("chat", 560, 760, 2.0, expr="sourire", bras="large", regard=(-1, 0), **PAPA,
                objet=feuille(0, -40, 200, 140, dessin_soleil(-50, -20, 0.6) + tache(20, 20, 44, graine=2), froissee=True)))
    S.add(perso("chat", 200, 770, 1.4, expr="triste", bras="bas", regard=(1, -0.5), **ZOU))
    S.add(bulle(300, 150, 460, 110, "Moi, je vois un nuage.\nEt toi ?", 34, pointe=(480, 300)))
    return S


def p05():
    S = Scene()
    fond(S, "#fff9db")
    S.add(feuille(400, 360, 640, 460, dessin_soleil(-210, -130, 1.2) + baleine(40, 30, 1.4), froissee=True))
    S.add(perso("chat", 640, 800, 1.3, expr="bouche_bee", bras="donne", flip=True, **ZOU,
                objet=pinceau(84, -96, 1.0, "#343a40", rot=40)))
    S.add(texte(250, 720, "Une baleine !", 56, "#1c7ed6", contour="#fff"))
    return S


def p06():
    S = Scene()
    fond(S, "#fff9db")
    mer = (rect(-320, 60, 640, 170, "#d0ebff") + vague(0, 60, 640) + dessin_soleil(-210, -130, 1.2) + baleine(40, -20, 1.2)
           + poisson_tache(-180, 140, 1.0) + poisson_tache(200, 150, 0.9, "#f783ac") + poisson_tache(-40, 180, 0.8, "#ffd43b"))
    S.add(feuille(400, 360, 640, 460, mer, froissee=True))
    S.add(perso("chat", 160, 800, 1.3, expr="rire", bras="haut", **ZOU))
    S.add(texte(520, 720, "Et un poisson !", 50, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    atelier(S)
    for k, (x, y, c) in enumerate([(150, 200, "#ff6b6b"), (320, 140, "#ffd43b"), (480, 220, "#69db7c"), (650, 360, "#cc5de8"), (130, 420, BLEU), (640, 560, "#ff922b")]):
        S.add(tache(x, y, 40 + (k % 3) * 8, graine=10 + k, couleur=c))
    S.add(perso("chat", 400, 760, 1.7, expr="rire", bras="haut", **ZOU))
    S.add(texte(400, 330, "Oups = idée !", 64, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    interieur(S, "#f3f0ff", "#d9a066", 600, papier="#e5dbff")
    mer = (rect(-160, 30, 320, 90, "#d0ebff") + vague(0, 30, 320) + baleine(0, -10, 0.7) + dessin_soleil(-110, -70, 0.6)
           + poisson_tache(-90, 80, 0.6) + poisson_tache(100, 80, 0.5, "#f783ac"))
    S.add(rect(230, 90, 340, 260, "#c68642", rx=8))
    S.add(feuille(400, 220, 300, 220, mer))
    S.add(perso("chat", 580, 760, 1.8, expr="content", bras="joues", regard=(-1, -0.5), **MAMIE))
    S.add(perso("chat", 240, 770, 1.4, expr="fier", bras="montre", regard=(1, -0.5), **ZOU))
    S.add(gateau(400, 780, 0.6, bougies=3))
    S.add(bulle(680, 420, 220, 70, "Magnifique !", 30, pointe=(620, 470)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("zou-seul.svg", vignette),
    ("01-le-dessin.svg", p01), ("02-splatch.svg", p02), ("03-rate.svg", p03),
    ("04-un-nuage.svg", p04), ("05-baleine.svg", p05), ("06-la-mer.svg", p06),
    ("07-oups-idee.svg", p07), ("08-anniversaire.svg", p08),
]
