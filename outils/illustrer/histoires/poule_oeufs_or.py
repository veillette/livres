"""La Poule aux œufs d'or — l'avarice perd tout en voulant tout gagner."""
from fables import *

ID = "poule-oeufs-or"

MATHURIN = dict(coiffure="courts", cheveux="chatain", peau="rosee", habit="#e8590c", robe=False, jambes="#5c3a1e",
                barbe="#8d5524")
VOISINE = dict(coiffure="chignon", cheveux="gris", peau="brune", habit="#12b886", acc=("tablier",))


def mathurin(x, y, s=1.0, chapeau_=False, **k):
    m = [personne(x, y, s, **{**MATHURIN, **k})]
    if chapeau_:
        m.append(chapeau(x, y - 188 * s, s * 1.05, "#495057", "#fab005", fleur_=False))
    return g(m)


def voisine(x, y, s=1.0, **k):
    k.pop("acc", None)
    return personne(x, y, s, **{**{kk: v for kk, v in VOISINE.items() if kk != "acc"}, **k})


def cocotte(x, y, s=1.0, **k):
    return coq(x, y, s, poule=True, **k)


def nid_paille(x, y, s=1.0, oeufs=(), vide_desordre=False):
    m = [ellipse(0, -10, 110, 36, "#e0a93a")]
    for k in range(9):
        m.append(chemin(f"M {-100 + k * 24} {-20 + (k % 2) * 10} q 20 -16 44 4", stroke="#c9901c", sw=5))
    for o in oeufs:
        m.append(o)
    m.append(chemin("M -110 -10 Q 0 30 110 -10 Q 90 20 0 26 Q -90 20 -110 -10 Z", "#c9901c"))
    if vide_desordre:
        rr = random.Random(4)
        for _ in range(14):
            a = rr.uniform(0, 2 * math.pi)
            px, py = math.cos(a) * rr.uniform(60, 220), -20 + math.sin(a) * rr.uniform(20, 80)
            m.append(trait(px, py, px + rr.uniform(-30, 30), py + rr.uniform(-12, 12), "#e0a93a", 4))
    return place(m, x, y, s)


def lanterne(x, y, s=1.0):
    m = [chemin("M -14 -80 Q 0 -100 14 -80", stroke="#495057", sw=4), rect(-22, -76, 44, 10, "#495057", rx=3),
         cercle(0, -46, 38, "#ffe066", opacity=0.35), rect(-18, -66, 36, 50, "#fff3bf", stroke="#495057", stroke_width=4),
         chemin("M -4 -30 Q 0 -54 4 -30 Z", "#ff922b"), rect(-22, -18, 44, 10, "#495057", rx=3)]
    return place(m, x, y, s)


def charrette(x, y, s=1.0):
    m = [rect(-120, -110, 220, 70, "#c68642", rx=6), trait(100, -70, 190, -60, "#a0522d", 8),
         cercle(-60, -30, 36, "#8d5524"), cercle(-60, -30, 12, "#fab005"), cercle(50, -30, 36, "#8d5524"), cercle(50, -30, 12, "#fab005")]
    return place(m, x, y, s)


def cour(S, soir=False, nuit_=False):
    if nuit_:
        nuit(S)
        etoiles(S, 30, graine=17)
        S.add(lune(660, 110, 38))
    else:
        ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#fff9db")
        S.add(soleil(680, 110, 46))
    collines(S, 560, "#b2f2bb" if not nuit_ else "#2b8a3e", graine=71)
    sol(S, 580, "#e9d8a6" if not nuit_ else "#8d7a5a")
    S.add(barriere(620, 640, 0.8, largeur=360))


def poulailler_dedans(S):
    interieur(S, "#ffe8cc", "#d9a066", 580, papier="#ffd8a8")
    for k in range(5):
        S.add(rect(40 + k * 170, 0, 20, 580, "#c68642"))
    S.add(rect(0, 120, 800, 20, "#a0522d"))
    S.add(fenetre(560, 180, 150, 130, "#a5d8ff"))


def couverture():
    S = Scene()
    cour(S)
    S.add(nid_paille(470, 740, 1.2, oeufs=[oeuf_or(-30, -8, 1.0), oeuf_or(40, -4, 0.9)]))
    S.add(cocotte(470, 650, 1.6, expr="content"))
    S.add(mathurin(210, 760, 1.35, expr="bouche_bee", bras="joues", regard=(1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(oeuf_or(200, 205, 2.2))
    return S


def p01():
    S = Scene()
    cour(S)
    S.add(maison(160, 600, 0.7, mur="#fff4e6", toit="#a0522d"))
    S.add(mathurin(330, 760, 1.4, expr="content", bras="salut"))
    S.add(cocotte(560, 760, 1.5, expr="content"))
    return S


def p02():
    S = Scene()
    poulailler_dedans(S)
    S.add(nid_paille(430, 720, 1.5, oeufs=[oeuf_or(0, -6, 1.2)]))
    S.add(mathurin(200, 760, 1.35, expr="bouche_bee", bras="joues", regard=(1, 1)))
    S.add(cocotte(620, 760, 1.1, expr="fier"))
    return S


def p03():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff4e6")
    ville(S, 600)
    sol(S, 600, "#adb5bd")
    S.add(mathurin(400, 760, 1.5, chapeau_=True, expr="fier", bras="hanches"))
    S.add(bulle(400, 130, 400, 90, "Je suis riche !", 44, pointe=(400, 380)))
    return S


def p04():
    S = Scene()
    poulailler_dedans(S)
    S.add(nid_paille(400, 720, 1.6, oeufs=[oeuf_or(-50, -10, 0.9), oeuf_or(0, -14, 1.0), oeuf_or(50, -8, 0.9)]))
    S.add(cocotte(400, 600, 1.2, expr="content"))
    S.add(texte(400, 250, "Un œuf d'or par jour !", 48, "#a0522d", contour="#fff"))
    return S


def p05():
    S = Scene()
    cour(S)
    S.add(charrette(560, 740, 1.2))
    S.add(perso("boeuf", 180, 740, 1.0, expr="content"))
    S.add(mathurin(390, 760, 1.35, chapeau_=True, habit="#c92a2a", expr="rire", bras="ouverts"))
    return S


def p06():
    S = Scene()
    cour(S)
    S.add(mathurin(330, 760, 1.45, chapeau_=True, expr="fache", bras="croises"))
    S.add(oeuf_or(590, 740, 1.1))
    S.add(bulle(360, 130, 460, 110, "Un seul œuf ?\nC'est trop lent !", 38, pointe=(340, 400)))
    return S


def p07():
    S = Scene()
    cour(S)
    S.add(mathurin(260, 760, 1.45, chapeau_=True, expr="furieux", bras="montre", regard=(1, 0)))
    S.add(cocotte(580, 760, 1.2, expr="surpris", flip=True))
    S.add(bulle(420, 130, 460, 110, "Ponds plus vite !\nDeux ! Trois ! Dix !", 36, pointe=(300, 400)))
    return S


def p08():
    S = Scene()
    poulailler_dedans(S)
    S.add(tas_grains(430, 760, 2.2))
    S.add(cocotte(430, 640, 1.2, expr="miam"))
    S.add(mathurin(170, 760, 1.35, chapeau_=True, expr="malin", bras="donne"))
    for k in range(5):
        S.add(grain(620 + k * 25, 700 - k * 30, 1.0))
    return S


def p09():
    S = Scene()
    poulailler_dedans(S)
    S.add(nid_paille(430, 740, 1.5, vide_desordre=True))
    S.add(mathurin(400, 700, 1.4, chapeau_=True, expr="concentre", bras="large"))
    S.add(cocotte(680, 760, 0.9, expr="inquiet", flip=True))
    S.add(texte(400, 200, "Où est le trésor ?", 48, "#a0522d", contour="#fff"))
    return S


def p10():
    S = Scene()
    cour(S, nuit_=True)
    S.add(cocotte(560, 760, 1.2, expr="triste", flip=True))
    S.add(mathurin(280, 760, 1.4, chapeau_=True, expr="concentre", bras="tient", objet=lanterne(68, -140, 1.0), regard=(1, 0)))
    return S


def p11():
    S = Scene()
    poulailler_dedans(S)
    S.add(nid_paille(430, 740, 1.5))
    S.add(cocotte(640, 760, 1.1, expr="pleure", flip=True))
    S.add(mathurin(220, 760, 1.35, chapeau_=True, expr="surpris", bras="joues", regard=(1, 1)))
    S.add(texte(430, 520, "?", 90, "#c92a2a"))
    return S


def p12():
    S = Scene()
    cour(S, soir=True)
    S.add(chemin("M 380 800 Q 500 680 800 640 L 800 700 Q 520 720 460 800 Z", "#f3d9a4"))
    S.add(cocotte(620, 690, 1.0, expr="triste", flip=True))
    S.add(mathurin(200, 760, 1.35, chapeau_=True, expr="inquiet", bras="ouverts", regard=(1, 0)))
    return S


def p13():
    S = Scene()
    cour(S, soir=True)
    S.add(mathurin(400, 760, 1.55, chapeau_=True, expr="pleure", bras="bas"))
    S.add(nuage_orage(400, 200, 0.5))
    return S


def p14():
    S = Scene()
    cour(S)
    S.add(maison(660, 620, 0.8, mur="#e6fcf5", toit="#12b886"))
    S.add(voisine(450, 760, 1.3, expr="content", bras="porte", objet=cocotte(0, -50, 0.5, expr="content")))
    S.add(mathurin(200, 760, 1.35, expr="timide", bras="calin", regard=(1, 0)))
    S.add(bulle(250, 130, 420, 100, "Pardon, Cocotte.\nJ'ai été trop gourmand.", 32, pointe=(210, 400)))
    return S


def p15():
    S = Scene()
    cour(S)
    S.add(nid_paille(620, 740, 1.2, oeufs=[oeuf(-30, -6, 1.0), oeuf_or(30, -8, 0.9, brille=False)]))
    S.add(cocotte(430, 760, 1.3, expr="content"))
    S.add(mathurin(200, 760, 1.35, expr="content", bras="donne", regard=(1, 0)))
    S.add(soleil(680, 110, 46))
    S.add(coeur(330, 450, 0.8))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("oeuf-d-or.svg", vignette),
    ("01-mathurin-et-cocotte.svg", p01), ("02-l-oeuf-d-or.svg", p02), ("03-riche.svg", p03),
    ("04-un-par-jour.svg", p04), ("05-les-achats.svg", p05), ("06-trop-lent.svg", p06),
    ("07-plus-vite.svg", p07), ("08-le-grain.svg", p08), ("09-le-tresor.svg", p09),
    ("10-la-lanterne.svg", p10), ("11-plus-d-oeuf.svg", p11), ("12-cocotte-s-en-va.svg", p12),
    ("13-tout-perdu.svg", p13), ("14-pardon.svg", p14), ("15-merci.svg", p15),
]
