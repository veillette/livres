"""Le voyage de Petit Nuage — le cycle de l'eau."""
from base import *
from objets import *
from sciences import *

ID = "petit-nuage"
BLANC_N, OMBRE_N = "#ffffff", "#dbe4ff"
GRIS_N, OMBRE_G = "#adb5bd", "#868e96"


def prairie(S, graine=1, y=620):
    collines(S, y, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a", couleur2="#69db7c", y2=y + 80)


def couverture():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    arc_en_ciel_vrai(S, 400, 820, 420, 22, horizon=640)
    prairie(S, 4, 640)
    for x, c in [(90, "#ff6b6b"), (170, "#cc5de8"), (640, "#ffd43b"), (720, "#ff922b")]:
        S.add(fleur(x, 760, 1.3, c, tige=70))
    S.add(nuage(120, 170, 0.5), nuage(690, 130, 0.6))
    S.add(nuage_perso(400, 430, 1.9, expr="rire"))
    for x in (330, 400, 470):
        S.add(goutte(x, 560 + (x % 3) * 12, 0.9, "#74c0fc"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 140, 185, 120, "#d0ebff"))
    S.add(nuage_perso(195, 150, 1.25, expr="content"))
    return S


def p01():
    S = Scene()
    ciel(S, "#4dabf7", "#d0ebff")
    prairie(S, 1, 650)
    S.add(soleil(660, 130, 55, visage=True))
    S.add(nuage(130, 150, 0.45, opacity=0.9), nuage(560, 330, 0.35, opacity=0.9))
    for x, y in [(150, 330), (200, 300), (250, 340)]:
        S.add(chemin(f"M {x - 16} {y} q 8 -10 16 0 q 8 -10 16 0", stroke="#364fc7", sw=4))
    S.add(nuage_perso(360, 380, 1.8, expr="sourire", regard=(1, 0.3)))
    S.add(arbre(640, 700, 0.6), arbre(120, 700, 0.5, "#69db7c", "#51cf66"))
    return S


def p02():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    prairie(S, 2, 640)
    S.add(vent_visage(170, 250, 1.5, "#ffffff"))
    S.add(nuage_perso(560, 280, 1.5, expr="joie", regard=(-1, 0)))
    # arbres et feuilles poussés vers la droite, comme le nuage
    for x, s in [(560, 0.75), (700, 0.6)]:
        S.add(place([rect(-14, -140, 28, 140, "#8d5524", rx=8),
                     ellipse(40, -200, 90, 66, "#51cf66"), ellipse(70, -150, 60, 40, "#40c057")], x, 720, s, rot=10))
    for x, y, r in [(330, 470, 20), (420, 520, -30), (260, 560, 50), (470, 440, 10)]:
        S.add(ellipse(x, y, 16, 8, "#40c057", rot=r))
    S.add(rafales(160, 520, 0.9, "#ffffff"))
    return S


def p03():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(montagnes(None, 700, ("#9775fa", "#7048e8")))
    sol(S, 720, "#8ce99a", bosse=10)
    for x in (80, 180, 640, 740):
        S.add(sapin(x, 780, 0.55))
    S.add(nuage_perso(420, 190, 1.35, expr="bouche_bee", regard=(0, 1)))
    S.add(rafales(80, 150, 0.7, "#ffffff"))
    S.add(oiseau(150, 340, 0.4, "#495057", "#dee2e6", ailes="ouvertes", pattes=False))
    return S


def baleine(x, y, s=1.0, jet=True):
    """Baleine qui fait un jet d'eau ; (x, y) = ligne d'eau au milieu du dos."""
    m = [chemin("M -150 20 Q -150 -60 -40 -70 Q 90 -76 130 -20 L 130 30 Z", "#4263eb"),
         chemin("M 120 -10 Q 180 -40 200 -80 Q 190 -30 210 -10 Q 170 10 120 10 Z", "#4263eb"),
         ellipse(-60, -20, 8, 10, ENCRE), cercle(-58, -24, 3, "#fff"),
         chemin("M -120 0 Q -80 16 -40 4", stroke="#364fc7", sw=4),
         ellipse(-90, -8, 12, 7, ROSE, opacity=0.8)]
    if jet:
        m += [chemin("M -40 -72 Q -44 -130 -80 -150", stroke="#a5d8ff", sw=9),
              chemin("M -40 -72 Q -38 -140 -4 -160", stroke="#a5d8ff", sw=9),
              chemin("M -40 -72 L -40 -170", stroke="#d0ebff", sw=10)]
        m += [goutte(-80 + k * 38, -150 - (k % 2) * 20, 0.8, "#a5d8ff") for k in range(3)]
    cid = uid("w")
    return place([el("clipPath", rect(-300, -400, 600, 400, "#000"), id=cid), g(m, clip_path=f"url(#{cid})")], x, y, s)


def p04():
    S = Scene()
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(soleil(700, 110, 50))
    eau(S, 500, "#1c7ed6", "#4dabf7")
    S.add(baleine(300, 600, 1.9))
    S.add(nuage_perso(540, 200, 1.6, expr="rire", regard=(-1, 1)))
    S.add(place([chemin("M -60 0 L 60 0 L 44 30 L -44 30 Z", "#e8590c"), trait(0, 0, 0, -110, "#495057", 5),
                 poly([(4, -108), (4, -10), (60, -10)], "#fff")], 660, 520, 0.8))
    return S


def vapeur(x, y, h=160, s=1.0, opacity=0.55):
    """Vapeur d'eau invisible qui monte : on la montre par des vaguelettes pâles."""
    d = f"M 0 0 q -14 {-h / 6} 0 {-h / 3} q 14 {-h / 6} 0 {-h / 3} q -14 {-h / 6} 0 {-h / 3}"
    return place(g([chemin(d, stroke="#ffffff", sw=6, opacity=opacity), poly([(-10, -h + 4), (10, -h + 4), (0, -h - 12)], "#fff", opacity=opacity)]), x, y, s)


def p05():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff3bf")
    S.add(soleil(110, 120, 60, visage=True))
    eau(S, 560, "#1c7ed6", "#4dabf7")
    for x, y in [(160, 540), (300, 520), (440, 540), (580, 520), (700, 540)]:
        S.add(vapeur(x, y, 170))
    rayons = [trait(170, 170, 330, 470, "#fcc419", 5, stroke_dasharray="16 12"), trait(150, 190, 220, 480, "#fcc419", 5, stroke_dasharray="16 12")]
    S.add(g(rayons, opacity=0.8))
    S.add(nuage_perso(470, 220, 1.9, GRIS_N, expr="surpris", ombre=OMBRE_G))
    return S


def p06():
    S = Scene()
    ciel(S, "#91a7c7", "#dbe4f0")
    sol(S, 600, "#9c6b3f", bosse=8)
    S.add(rect(0, 680, 800, 120, "#8a5a33"))
    pluie(S, 60, 6, (130, 300, 700, 600), "#4dabf7")
    fleurs = [(130, "#ff6b6b"), (250, "#cc5de8"), (370, "#ffd43b"), (490, "#ff922b"), (610, "#f06595"), (720, "#4dabf7")]
    for k, (x, c) in enumerate(fleurs):
        S.add(fleur(x, 700, 1.4, c, tige=100))
        S.add(place(g([oeil(-8, 0, "heureux"), oeil(8, 0, "heureux"), bouche(0, 8, "ouverte", 0.6)]), x, 700 - 140, 0.8))
    S.add(nuage_perso(420, 200, 1.9, GRIS_N, expr="content", ombre=OMBRE_G))
    S.add(texte(160, 110, "Plic !", 54, "#1c7ed6", contour="#fff", rot=-8), texte(650, 110, "Ploc !", 54, "#1c7ed6", contour="#fff", rot=8))
    return S


def p07():
    # Le Soleil est dans le dos de celui qui regarde : l'arc-en-ciel se forme
    # toujours du côté opposé au Soleil, dans la pluie qui tombe encore.
    S = Scene()
    ciel(S, "#8fb6e8", "#e7f5ff")
    pluie(S, 45, 7, (430, 150, 790, 600), "#a5d8ff")
    arc_en_ciel_vrai(S, 400, 760, 400, 20, horizon=620)
    prairie(S, 7, 620)
    for k, (x, c) in enumerate([(90, "#ff6b6b"), (210, "#cc5de8"), (330, "#ffd43b"), (470, "#ff922b"), (590, "#f06595"), (710, "#4dabf7")]):
        S.add(ellipse(x + 4, 708, 22, 7, "#2b8a3e", opacity=0.35))
        S.add(fleur(x, 740, 1.3, c, tige=90))
        S.add(place(g([oeil(-8, 0, "heureux"), oeil(8, 0, "heureux"), bouche(0, 8, "ouverte", 0.6)]), x, 740 - 117, 0.8))
    S.add(notes(120, 520, 0.8, "#e64980"), notes(560, 500, 0.8, "#7048e8"))
    S.add(nuage_perso(600, 140, 1.2, "#f1f3f5", expr="rire", ombre=OMBRE_N))
    return S


def p08():
    S = Scene()
    nuit(S, "#141c3a", "#3b4a8a")
    etoiles(S, 60, 8, (0, 0, 800, 560))
    # fin croissant du soir : éclairé à droite, bas vers l'ouest après le coucher du Soleil
    S.add(lune_phase(650, 170, 50, 0.2, True, sombre="#2a3563"))
    collines(S, 660, "#2b3a6b", graine=8)
    sol(S, 660, "#23305c")
    S.add(maison(150, 720, 0.6, "#495057", "#343a40", lumiere=True))
    S.add(nuage_perso(400, 400, 2.0, "#e5dbff", expr="dort", ombre="#b197fc"))
    S.add(zzz(560, 300, 1.3, "#e5dbff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("nuage-seul.svg", vignette),
    ("01-ciel.svg", p01), ("02-vent.svg", p02), ("03-montagnes.svg", p03), ("04-mer.svg", p04),
    ("05-nuage-gris.svg", p05), ("06-pluie.svg", p06), ("07-arc-en-ciel.svg", p07), ("08-nuit.svg", p08),
]
