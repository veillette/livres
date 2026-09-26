"""Petit Hibou et la Lune — les phases de la Lune.

Les phases sont dessinées telles qu'on les voit depuis l'hémisphère Nord :
la Lune qui décroît est éclairée à gauche, celle qui grandit à droite.
"""
from base import *
from objets import *
from sciences import *

ID = "hibou-lune"
HIBOU = dict(couleur="#b0835a", visage="#f3dcc3")
MAMIE = dict(couleur="#8d8f99", visage="#e9ecef", acc=("lunettes", "echarpe"))
CIEL_SOMBRE = "#26325e"


def decor(S, graine=1, haut="#141c3a", bas="#34427a", nb=45):
    nuit(S, haut, bas)
    etoiles(S, nb, graine, (0, 0, 800, 520))
    r = random.Random(graine)
    for k in range(11):
        x = k * 80 + r.uniform(-20, 20)
        S.add(place(poly([(-50, 0), (0, -r.uniform(170, 260)), (50, 0)], "#101733"), x, 700))
    S.add(rect(0, 690, 800, 110, "#0c1229"))


def branche(S, y=610, x0=-20, x1=560):
    S.add(chemin(f"M {x0} {y + 20} Q {(x0 + x1) / 2} {y - 10} {x1} {y}", stroke="#5c3a1e", sw=28))
    S.add(chemin(f"M {x1 - 120} {y + 2} Q {x1 - 60} {y - 50} {x1 - 20} {y - 70}", stroke="#5c3a1e", sw=12))
    for fx, fy, rot in [(x1 - 10, y - 76, -30), (x1 + 6, y - 6, 10), (x1 - 200, y + 20, 40), (60, y + 34, 30)]:
        S.add(ellipse(fx, fy, 26, 12, "#2f9e44", rot=rot))


def petit_hibou(x, y, s=1.0, **k):
    return chouette(x, y, s, **{**HIBOU, **k})


def couverture():
    S = Scene()
    decor(S, 1, nb=35)
    S.add(lune_phase(430, 360, 190, 1.0))
    branche(S, 640, -20, 700)
    S.add(petit_hibou(400, 640, 1.9, expr="content", ailes="bas"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lune_phase(270, 110, 70, 1.0, halo=False))
    S.add(petit_hibou(170, 255, 1.2, expr="content", regard=(1, -1)))
    return S


def page_phase(graine, eclairee, croissante, expr, regard=(0.6, -1), extra=None, lune_xy=(560, 220), lune_r=110):
    S = Scene()
    decor(S, graine)
    S.add(lune_phase(*lune_xy, lune_r, eclairee, croissante))
    branche(S)
    S.add(petit_hibou(300, 610, 1.7, expr=expr, regard=regard))
    if extra:
        S.add(extra)
    return S


def p01():
    return page_phase(1, 1.0, True, "content", regard=(1, -1))


def p02():
    # gibbeuse décroissante : il manque un morceau à droite
    S = page_phase(2, 0.8, False, "surpris", regard=(1, -1))
    S.add(texte(250, 150, "?", 110, "#ffe066", contour="#141c3a"))
    return S


def p03():
    # dernier quartier : moitié gauche éclairée
    S = page_phase(3, 0.5, False, "inquiet", regard=(1, 0))
    S.add(chauve_souris(620, 470, 1.3, expr="rire", regard=(-1, 0)))
    S.add(bulle(620, 620, 250, 80, "Mais non !", 40, pointe=(620, 520)))
    return S


def p04():
    # fin croissant décroissant, éclairé à gauche (il se voit à l'aube)
    S = page_phase(4, 0.13, False, "triste", regard=(1, -1))
    return S


def p05():
    # nouvelle lune : la Lune est du côté du Soleil, elle n'est pas dans le ciel de la nuit
    S = Scene()
    decor(S, 5, "#070b1c", "#1b2348", nb=90)
    branche(S, 610, -20, 620)
    S.add(petit_hibou(360, 610, 1.9, expr="surpris", regard=(0, -1)))
    return S


def schema_phases(cx, cy, R=150):
    """Le Soleil éclaire toujours une moitié de la Lune ; depuis la Terre on en voit plus ou moins."""
    m = [cercle(cx, cy, R, "none", stroke="#adb5bd", stroke_width=3, stroke_dasharray="8 10")]
    m.append(soleil(cx - R - 110, cy, 44))
    for k in range(3):
        m.append(trait(cx - R - 50, cy - 60 + k * 60, cx - R + 10, cy - 60 + k * 60, "#fcc419", 5, stroke_dasharray="12 8"))
    m.append(boule_eclairee(cx, cy, 34, "#4dabf7", "#1c2a52", 180))
    m.append(ellipse(cx - 8, cy - 6, 14, 10, "#51cf66"))
    for a in (0, 90, 180, 270):
        ang = math.radians(a)
        m.append(boule_eclairee(cx + math.cos(ang) * R, cy + math.sin(ang) * R, 24, "#fff3bf", "#1c2a52", 180, opacity=0.85))
    return g(m)


def p06():
    S = Scene()
    decor(S, 6)
    S.add(rect(30, 30, 740, 360, "#fff9db", rx=40, stroke="#fcc419", stroke_width=5))
    S.add(schema_phases(520, 210, 125))
    S.add(texte(165, 290, "Soleil", 30, "#e67700"), texte(520, 290, "Terre", 26, "#1c7ed6"), texte(700, 160, "Lune", 26, "#868e96"))
    branche(S, 700, -20, 760)
    S.add(chouette(580, 700, 1.5, expr="sourire", regard=(-1, 0), ailes="ouvertes", **MAMIE))
    S.add(petit_hibou(260, 700, 1.25, expr="bouche_bee", regard=(1, -1)))
    return S


def p07():
    # fin croissant du soir, éclairé à droite, près de l'horizon où le Soleil vient de se coucher
    S = Scene()
    ciel(S, "#141c3a", "#6a5aa8")
    S.add(ellipse(760, 700, 360, 170, "#ff922b", opacity=0.35))
    etoiles(S, 40, 7, (0, 0, 800, 380))
    for k, f in enumerate((0.25, 0.5, 0.8)):
        S.add(lune_phase(130 + k * 110, 90, 34, f, True, sombre="#2a3563", halo=False))
    S.add(fleche(90, 150, 400, 150, "#ffe066", 5, 16))
    S.add(lune_phase(600, 330, 70, 0.12, True, sombre="#3c3f78"))
    r = random.Random(7)
    for k in range(11):
        x = k * 80 + r.uniform(-20, 20)
        S.add(place(poly([(-50, 0), (0, -r.uniform(170, 260)), (50, 0)], "#101733"), x, 700))
    S.add(rect(0, 690, 800, 110, "#0c1229"))
    branche(S)
    S.add(petit_hibou(300, 610, 1.7, expr="rire", regard=(1, -0.5)))
    return S


def p08():
    S = page_phase(8, 1.0, True, "rire", regard=(1, -1), lune_xy=(560, 230), lune_r=130)
    S.add(chouette(120, 612, 1.1, expr="content", **MAMIE))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("hibou-seul.svg", vignette),
    ("01-pleine-lune.svg", p01), ("02-gibbeuse.svg", p02), ("03-quartier.svg", p03), ("04-croissant.svg", p04),
    ("05-nouvelle-lune.svg", p05), ("06-grand-maman.svg", p06), ("07-croissant-revient.svg", p07), ("08-retour.svg", p08),
]
