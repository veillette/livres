"""Escargot prend son temps — ralentir et s'émerveiller."""
from base import *
from objets import *

ID = "escargot-promenade"
LEON = dict(coquille="#f59f00", corps="#ffe3c2")


def pre(S, graine=1, y=620, soir=False):
    if soir:
        ciel(S, "#5f3dc4", "#ffa8a8")
    else:
        ciel(S, "#74c0fc", "#e7f5ff")
    collines(S, y, "#b2f2bb" if not soir else "#9775fa", graine=graine)
    sol(S, y, "#8ce99a" if not soir else "#748ffc", couleur2="#69db7c" if not soir else "#5c7cfa", y2=y + 100)


def guirlande(x0, x1, y, eteinte=False):
    m = [chemin(f"M {x0} {y} Q {(x0 + x1) / 2} {y + 60} {x1} {y}", stroke="#495057", sw=3)]
    cols = ["#ff6b6b", "#ffd43b", "#4dabf7", "#69db7c", "#cc5de8"]
    for k in range(9):
        t = (k + 0.5) / 9
        x = x0 + (x1 - x0) * t
        yy = y + 60 * 4 * t * (1 - t) * 0.5 + 6
        m.append(poly([(x - 14, yy), (x + 14, yy), (x, yy + 30)], cols[k % 5] if not eteinte else "#adb5bd"))
    return g(m)


def panneau(x, y, contenu):
    return g([rect(x - 6, y - 10, 12, 120, "#8d5524"), rect(x - 110, y - 60, 220, 60, "#fff4e6", rx=10, stroke="#8d5524", stroke_width=5),
              texte(x, y - 20, contenu, 26, "#8d5524")])


def couverture():
    S = Scene()
    pre(S, 2)
    S.add(fleur(160, 740, 2.0, "#f783ac", tige=90), fleur(640, 720, 1.6, "#ffd43b", "#fff", tige=80))
    S.add(papillon(250, 470, 1.3, rot=-15))
    S.add(escargot(380, 760, 2.4, expr="content", **LEON))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(escargot(200, 262, 1.5, expr="sourire", **LEON))
    return S


def p01():
    S = Scene()
    pre(S, 1)
    S.add(guirlande(560, 800, 300))
    S.add(panneau(660, 560, "Fête de l'été →"))
    S.add(perso("herisson", 110, 760, 0.95, expr="joie", bras="course"))
    S.add(perso("lapin", 260, 780, 1.05, expr="joie", bras="course"))
    S.add(perso("renard", 420, 770, 1.0, expr="rire", bras="course"))
    S.add(perso("ours", 590, 800, 1.1, expr="rire", bras="course"))
    for x in (190, 350, 510):
        S.add(mouvement(x, 610, 0.9))
    S.add(texte(280, 200, "Vite, vite !", 64, "#e8590c", contour="#fff"))
    return S


def p02():
    S = Scene()
    pre(S, 3)
    S.add(perso("lapin", 600, 760, 1.4, expr="rire", bras="course", pieds_haut=True))
    S.add(mouvement(480, 560, 1.5))
    S.add(escargot(250, 760, 1.6, expr="sourire", **LEON))
    S.add(bulle(560, 170, 460, 100, "Tu vas arriver\ntrop tard !", 36, pointe=(600, 330)))
    return S


def p03():
    S = Scene()
    pre(S, 4)
    S.add(fleur(480, 760, 4.2, "#ff8787", tige=90))
    S.add(escargot(260, 760, 1.8, expr="content", **LEON))
    for k in range(3):
        S.add(chemin(f"M {410 - k * 20} {420 + k * 30} q -20 -20 -40 0 q -20 20 -40 0", stroke="#ff8787", sw=4, opacity=0.7))
    S.add(texte(260, 240, "Mmm…", 64, "#e64980", contour="#fff"))
    S.add(texte(560, 250, "ça sent la fraise !", 38, "#e64980", contour="#fff"))
    return S


def p04():
    S = Scene()
    pre(S, 5)
    S.add(chemin("M 380 760 Q 400 500 560 420", stroke="#2f9e44", sw=10))
    S.add(ellipse(560, 430, 150, 60, "#51cf66", rot=-15), trait(420, 470, 690, 390, "#2f9e44", 4))
    S.add(coccinelle(560, 400, 2.4, rot=10))
    S.add(texte(560, 250, "…six, sept !", 50, "#e03131", contour="#fff"))
    S.add(escargot(220, 770, 1.6, expr="bouche_bee", regard=(1, -1), **LEON))
    S.add(notes(640, 600, 0.9, "#2f9e44"))
    return S


def p05():
    S = Scene()
    pre(S, 6)
    S.add(trait(170, 620, 180, 120, "#8d5524", 10), trait(650, 620, 640, 100, "#8d5524", 10))
    S.add(toile(410, 330, 220))
    for k in range(8):
        S.add(etoile5(250 + (k * 71) % 330, 200 + (k * 53) % 260, 6, "#fff"))
    S.add(escargot(360, 770, 1.5, expr="bouche_bee", regard=(0.5, -1), **LEON))
    S.add(texte(410, 90, "Des perles de rosée !", 44, "#1c7ed6", contour="#fff"))
    return S


def p06():
    S = Scene()
    pre(S, 7)
    S.add(scarabee(520, 700, 2.6, rot=170))
    for k in range(3):
        S.add(trait(470 + k * 50, 600, 480 + k * 50, 570, ENCRE, 3, opacity=0.4))
    S.add(escargot(270, 760, 1.6, expr="sourire", **LEON))
    S.add(bulle(560, 180, 420, 100, "Je vais t'aider,\npetit scarabée !", 34, pointe=(360, 560)))
    return S


def p07():
    S = Scene()
    pre(S, 8, soir=True)
    S.add(guirlande(0, 800, 180, eteinte=True))
    for k in range(20):
        S.add(rect(50 + (k * 97) % 700, 660 + (k * 31) % 120, 10, 6, ["#ff6b6b", "#ffd43b", "#4dabf7"][k % 3], rot=None))
    S.add(perso("lapin", 540, 720, 1.2, expr="neutre", bras="bas", regard=(-1, 0)))
    S.add(perso("renard", 700, 740, 1.0, expr="baille", bras="haut"))
    S.add(perso("ours", 380, 740, 1.1, expr="dort"))
    S.add(escargot(170, 770, 1.4, expr="sourire", **LEON))
    S.add(bulle(560, 330, 330, 80, "Tu as tout raté !", 32, pointe=(540, 460)))
    return S


def p08():
    S = Scene()
    ciel(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 40, 9, (0, 0, 800, 480))
    S.add(lune(120, 110, 45))
    sol(S, 620, "#364fc7", couleur2="#3b5bdb", y2=720)
    S.add(g([ellipse(400, 690, 130, 30, "#6b4226"), rect(270, 610, 260, 80, "#8d5524"), ellipse(400, 610, 130, 30, "#c68642"),
             ellipse(400, 610, 90, 18, "#a0693a", opacity=0.5)]))
    S.add(escargot(390, 612, 1.4, expr="rire", **LEON))
    for k, (esp, x, s_) in enumerate([("lapin", 150, 1.0), ("ours", 640, 1.15), ("renard", 250, 0.9), ("herisson", 540, 0.85)]):
        S.add(perso(esp, x, 790, s_, expr="bouche_bee" if k % 2 else "content", regard=(1 if x < 400 else -1, -0.5)))
    for x, y in [(300, 400), (520, 360), (690, 470), (90, 500)]:
        S.add(cercle(x, y, 6, "#ffe066"), cercle(x, y, 16, "#ffe066", opacity=0.3))
    S.add(pensee(560, 200, 110, papillon(520, 200, 0.9) + toile(610, 200, 40, perles=False) + coccinelle(570, 240, 0.9), depuis=(520, 440)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("escargot-seul.svg", vignette),
    ("01-vite-vite.svg", p01), ("02-trop-tard.svg", p02), ("03-la-fleur.svg", p03),
    ("04-coccinelle.svg", p04), ("05-la-toile.svg", p05), ("06-scarabee.svg", p06),
    ("07-la-fete-est-finie.svg", p07), ("08-raconter.svg", p08),
]
