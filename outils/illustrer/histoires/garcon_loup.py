"""Le garçon qui criait au loup — dire la vérité pour être cru."""
from contes import *

ID = "garcon-loup"
PIERRE = dict(coiffure="herisses", cheveux="brun", peau="doree", habit="#1c7ed6", robe=False, jambes="#5c3a1e", chaussures="#343a40")
GENS = [dict(coiffure="courts", cheveux="noir", peau="brune", habit="#e8590c", robe=False, jambes="#495057"),
        dict(coiffure="chignon", cheveux="roux", peau="claire", habit="#9775fa"),
        dict(coiffure="chauve_cote", cheveux="gris", barbe="#adb5bd", peau="rosee", habit="#2f9e44", robe=False, jambes="#5c3a1e"),
        dict(coiffure="tresses", cheveux="brun", peau="foncee", habit="#fcc419")]
BERGER = dict(coiffure="chauve_cote", cheveux="blanc", barbe="#f1f3f5", peau="rosee", habit="#a0522d", robe=False, jambes="#5c3a1e")


def pierre(x, y, s=1.0, **k):
    k.setdefault("objet", "")
    return personne(x, y, s, **{**PIERRE, **k})


def villageois(i, x, y, s=1.0, outil=True, **k):
    if outil and "objet" not in k:
        k["bras"] = k.get("bras", "tient")
        k["objet"] = baton(68, -146, 68, -30, "#a0522d", 10) if i % 2 == 0 else place(g([trait(0, 0, 0, -150, "#a0522d", 8), chemin("M -24 -150 L -24 -190 M 0 -150 L 0 -196 M 24 -150 L 24 -190 M -24 -150 L 24 -150", stroke="#868e96", sw=6)]), 68, -80)
    return personne(x, y, s, **{**GENS[i % 4], **k})


def mouton(x, y, s=0.8, **k):
    return perso("mouton", x, y, s, **k)


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def colline(S, soir=False):
    if soir:
        ciel(S, "#5f3dc4", "#ffa8a8")
    else:
        ciel(S, "#a5d8ff", "#fff9db")
        S.add(soleil(680, 100, 40))
    S.add(nuage(160, 110, 0.6))
    S.add(maison(620, 450, 0.35, toit="#e8590c"), maison(720, 460, 0.3, toit="#1c7ed6"), maison(540, 465, 0.28, toit="#c2255c"))
    sol(S, 470, "#b2f2bb")
    S.add(chemin("M -40 800 Q 200 480 820 540 L 820 800 Z", "#94d82d" if not soir else "#74b816"))
    for xx in (40, 120):
        S.add(sapin(xx, 560, 0.9, "#2b8a3e", "#2f9e44"))


def troupeau(S, pos=((430, 700), (560, 740), (680, 700)), expr="sourire"):
    for x, y in pos:
        S.add(mouton(x, y, 0.8, expr=expr))


def village(S):
    village_(S)


def lanterne(x, y, s=1.0):
    m = [cercle(0, 0, 50, "#ffe066", opacity=0.3), rect(-16, -24, 32, 44, "#ffe066", rx=6, stroke="#495057", stroke_width=4),
         chemin("M -12 -24 Q 0 -44 12 -24", stroke="#495057", sw=4)]
    return place(m, x, y, s)


def couverture():
    S = Scene()
    colline(S)
    troupeau(S, ((520, 720), (650, 760)))
    S.add(loup(730, 600, 0.7, expr="malin", flip=True))
    S.add(pierre(300, 790, 1.45, expr="furieux", bras="joues"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(mouton(200, 262, 0.95, expr="content"))
    return S


def p01():
    S = Scene()
    colline(S)
    troupeau(S)
    S.add(pierre(250, 790, 1.4, expr="baille", bras="tete"))
    S.add(texte(300, 280, "Bof…", 52, "#495057", contour="#fff"))
    return S


def p02():
    S = Scene()
    colline(S)
    troupeau(S)
    S.add(pierre(250, 790, 1.4, expr="furieux", bras="joues"))
    S.add(texte(420, 240, "Au loup ! Au loup !", 58, "#c92a2a", contour="#fff", rot=-4))
    return S


def p03():
    S = Scene()
    colline(S)
    S.add(villageois(0, 200, 790, 1.2, expr="inquiet"), villageois(1, 360, 800, 1.15, expr="surpris"),
          villageois(2, 520, 790, 1.2, expr="inquiet"), villageois(3, 680, 800, 1.1, expr="surpris"))
    S.add(bulle(420, 180, 380, 90, "Où est le loup ?", 38, pointe=(360, 470)))
    return S


def p04():
    S = Scene()
    colline(S)
    S.add(pierre(220, 790, 1.4, expr="rire", bras="hanches"))
    S.add(villageois(0, 450, 790, 1.1, expr="fache"), villageois(2, 600, 790, 1.1, expr="fache", bras="croises"))
    S.add(texte(220, 300, "Ha ha ha !", 60, "#1c7ed6", contour="#fff"))
    S.add(bulle(560, 140, 380, 100, "Pas de loup ?\nC'était une blague ?!", 30, pointe=(540, 480)))
    return S


def p05():
    S = Scene()
    colline(S)
    troupeau(S, ((600, 720), (700, 760)))
    S.add(pierre(230, 790, 1.4, expr="malin", bras="joues"))
    S.add(texte(430, 260, "Au loup !", 70, "#c92a2a", contour="#fff", rot=-4))
    S.add(villageois(1, 480, 620, 0.6, expr="surpris", outil=False, bras="course"), villageois(3, 560, 610, 0.55, expr="inquiet", outil=False, bras="course"))
    return S


def p06():
    S = Scene()
    colline(S)
    S.add(pierre(220, 790, 1.4, expr="rire", bras="haut"))
    S.add(villageois(1, 440, 790, 1.15, expr="furieux", bras="montre"), villageois(3, 620, 790, 1.1, expr="furieux", bras="croises"))
    S.add(texte(560, 250, "Menteur !", 70, "#c92a2a", contour="#fff"))
    return S


def p07():
    S = Scene()
    colline(S, soir=True)
    troupeau(S, ((460, 720), (600, 750), (700, 700)))
    S.add(loup(180, 720, 1.3, expr="malin", regard=(1, 0)))
    S.add(buisson(80, 760, 1.2, "#2b8a3e", "#2f9e44"))
    return S


def p08():
    S = Scene()
    village(S)
    S.add(villageois(0, 180, 790, 1.2, expr="neutre", outil=False, bras="croises"), villageois(1, 380, 800, 1.15, expr="neutre", outil=False))
    S.add(villageois(2, 590, 790, 1.2, expr="degoute", outil=False, bras="croises"))
    S.add(bulle(420, 120, 520, 100, "« Au loup ! Au secours ! »\nEncore une blague…", 30))
    return S


def p09():
    S = Scene()
    colline(S, soir=True)
    S.add(loup(260, 760, 1.2, expr="furieux", bras="course"))
    for x, y, rot in ((460, 700, -10), (600, 760, 12), (700, 640, -16)):
        S.add(mouton(x, y, 0.75, expr="oups", bras="haut", rot=rot))
    S.add(mouvement(400, 620, 1.2), mouvement(540, 680, 1.2))
    return S


def p10():
    S = Scene()
    village(S)
    S.add(pierre(260, 790, 1.4, expr="pleure", larmes=True, bras="ouverts"))
    S.add(villageois(1, 540, 790, 1.2, expr="surpris", outil=False), villageois(2, 680, 790, 1.15, expr="inquiet", outil=False))
    S.add(bulle(360, 150, 480, 100, "C'était un vrai loup !", 38, pointe=(280, 460)))
    return S


def p11():
    S = Scene()
    village(S)
    S.add(personne(520, 790, 1.4, expr="sourire", bras="donne", **BERGER))
    S.add(pierre(260, 790, 1.2, expr="triste", regard=(1, 0)))
    S.add(bulle(420, 140, 520, 120, "Quand on ment, on ne\nnous croit plus… même quand\non dit la vérité.", 28, pointe=(520, 460)))
    return S


def p12():
    S = Scene()
    nuit(S, "#1c2a52", "#364fc7")
    etoiles(S, 30, graine=12)
    S.add(lune(660, 110, 40))
    for k in range(6):
        S.add(sapin(-20 + k * 170, 560, 1.2, "#2b8a3e", "#237032"))
    sol(S, 560, "#2b8a3e")
    S.add(pierre(200, 790, 1.2, expr="inquiet", bras="tient", objet=lanterne(68, -140, 0.9)))
    S.add(villageois(0, 380, 790, 1.1, bras="tient", objet=lanterne(68, -140, 0.9)), villageois(2, 560, 790, 1.1, bras="tient", objet=lanterne(68, -140, 0.9)))
    S.add(mouton(700, 640, 0.6, expr="timide"))
    return S


def p13():
    S = Scene()
    colline(S)
    troupeau(S, ((420, 690), (540, 740), (660, 700), (720, 780), (470, 790)), expr="content")
    S.add(pierre(220, 790, 1.35, expr="timide", bras="montre"))
    S.add(texte(500, 280, "Un, deux, trois…", 50, "#2b8a3e", contour="#fff"))
    return S


def p14():
    S = Scene()
    colline(S)
    troupeau(S, ((560, 720), (680, 750)), expr="content")
    S.add(pierre(260, 790, 1.35, expr="rire", bras="salut"))
    S.add(villageois(1, 440, 790, 1.1, expr="rire", outil=False, bras="salut"))
    S.add(coeur(350, 280, 1.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("mouton-seul.svg", vignette),
    ("01-il-s-ennuie.svg", p01), ("02-au-loup.svg", p02), ("03-ou-est-le-loup.svg", p03), ("04-une-blague.svg", p04),
    ("05-encore.svg", p05), ("06-menteur.svg", p06), ("07-le-vrai-loup.svg", p07), ("08-personne-ne-vient.svg", p08),
    ("09-les-moutons-fuient.svg", p09), ("10-un-vrai-loup.svg", p10), ("11-le-vieux-berger.svg", p11),
    ("12-les-lanternes.svg", p12), ("13-tous-la.svg", p13), ("14-la-verite.svg", p14),
]
