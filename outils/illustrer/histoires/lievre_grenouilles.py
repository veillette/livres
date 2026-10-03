"""Le Lièvre et les Grenouilles — il y a toujours plus peureux que soi, et à deux on a moins peur."""
from fables import *

ID = "lievre-grenouilles"

VERT = "#5c940d"


def lievre(x, y, s=1.0, **k):
    return perso("lievre", x, y, s, **k)


def grenouille(x, y, s=1.0, **k):
    return perso("grenouille", x, y, s, **k)


def le_ciel(S, soir=False, nuit_=False):
    if nuit_:
        nuit(S)
        etoiles(S, 18, 54, zone=(0, 0, 800, 380))
        S.add(lune(660, 130, 40))
    else:
        ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#f4fce3")


def prairie(S, soir=False, graine=51, nuit_=False):
    le_ciel(S, soir, nuit_)
    collines(S, 560, "#364fc7" if nuit_ else "#b2f2bb", graine=graine)
    sol(S, 580, "#2f9e44" if nuit_ else "#8ce99a")


def gite(x, y, s=1.0):
    """Creux d'herbes hautes où le lièvre se repose ; (x, y) = milieu du creux."""
    m = [ellipse(0, 0, 170, 36, "#69db7c"), ellipse(0, -4, 130, 22, "#2f9e44", opacity=0.35)]
    for k in range(9):
        m.append(herbe(-160 + k * 40, 18 + (k % 2) * 8, 1.2 + (k % 3) * 0.2, "#40c057"))
    return place(m, x, y, s)


def mare(S, y=560, soir=False, graine=52, nuit_=False):
    le_ciel(S, soir, nuit_)
    collines(S, y - 10, "#364fc7" if nuit_ else "#b2f2bb", graine=graine)
    sol(S, y, "#2f9e44" if nuit_ else "#8ce99a")
    S.add(ellipse(580, y + 180, 300, 110, "#4dabf7"))
    for k in range(4):
        S.add(chemin(f"M {360 + k * 110} {y + 140 + (k % 2) * 40} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    S.add(nenuphar(420, y + 200, 0.8, "#ffc9d6"), nenuphar(660, y + 130, 0.7))
    for k in range(5):
        S.add(roseau(830 - k * 26, y + 100 + k * 6, 0.45 + (k % 2) * 0.1, penche=-6 + k * 3, visage_=False))


def plouf(x, y, s=1.0):
    return place([ellipse(0, 0, 60, 16, "none", stroke="#d0ebff", stroke_width=5),
                  goutte(-34, -40, 1.0, "#a5d8ff"), goutte(0, -56, 1.2, "#a5d8ff"), goutte(34, -40, 1.0, "#a5d8ff")], x, y, s)


def couverture():
    S = Scene()
    mare(S)
    S.add(lievre(190, 690, 1.35, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(grenouille(520, 690, 0.8, expr="oups", bras="haut", pieds_haut=True, rot=12))
    S.add(plouf(650, 720, 1.0))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(lievre(200, 262, 0.72, expr="timide", bras="calin"))
    return S


def p01():
    S = Scene()
    prairie(S)
    S.add(lievre(400, 720, 1.5, expr="inquiet", bras="pense", regard=(1, -1)))
    S.add(gite(400, 720, 1.2))
    S.add(papillon(640, 300, 1.0))
    return S


def p02():
    S = Scene()
    prairie(S)
    S.add(arbre(620, 600, 1.4, "#ffa94d", "#ff922b"))
    S.add(lievre(360, 720, 1.5, expr="oups", bras="ouverts", pieds_haut=True, regard=(1, -1)))
    S.add(gite(360, 720, 1.2))
    S.add(grande_feuille(480, 380, 0.35, "#ff922b", "#e8590c", rot=30))
    S.add(texte(200, 260, "Iiih !", 56, VERT, contour="#fff"))
    return S


def p03():
    S = Scene()
    prairie(S, nuit_=True)
    S.add(lievre(380, 720, 1.5, expr="inquiet", bras="calin", regard=(-1, 0)))
    S.add(gite(380, 720, 1.2))
    S.add(rafales(140, 420, 1.0, "#fff"), vent(620, 470, 1.0, "#fff"))
    S.add(texte(590, 330, "Fffff…", 46, VERT, contour="#fff"))
    return S


def p04():
    S = Scene()
    prairie(S)
    S.add(lievre(400, 740, 1.6, expr="pleure", bras="tete"))
    S.add(gite(400, 740, 1.2))
    S.add(bulle(400, 140, 600, 120, "Que je suis malheureux !\nJ'ai peur de tout !", 38))
    return S


def p05():
    S = Scene()
    prairie(S)
    S.add(arbre(160, 610, 1.3))
    S.add(baton(120, 440, 230, 400, ep=14))
    S.add(texte(180, 360, "CRAC !", 54, "#c92a2a", contour="#fff"))
    S.add(lievre(520, 700, 1.4, expr="oups", bras="course", flip=True, pieds_haut=True, rot=8))
    S.add(mouvement(420, 580, 1.3))
    return S


def p06():
    S = Scene()
    prairie(S, graine=53)
    S.add(lievre(400, 730, 1.4, expr="oups", bras="course", flip=True, rot=6))
    S.add(mouvement(300, 600, 1.3), mouvement(320, 680, 1.0))
    S.add(texte(560, 260, "Vite ! Vite !", 52, VERT, contour="#fff"))
    return S


def p07():
    S = Scene()
    mare(S)
    S.add(lievre(140, 690, 1.2, expr="oups", bras="course", flip=True))
    for k, (xx, yy, rot) in enumerate([(420, 640, 20), (560, 620, 30), (700, 660, 40)]):
        S.add(grenouille(xx, yy, 0.6, expr="oups", bras="haut", pieds_haut=True, rot=rot))
    S.add(plouf(450, 720, 0.9), plouf(640, 700, 0.9))
    S.add(texte(520, 250, "Plouf ! Plouf ! Plouf !", 48, "#1971c2", contour="#fff"))
    return S


def p08():
    S = Scene()
    mare(S)
    S.add(lievre(180, 700, 1.4, expr="bouche_bee", bras="joues", regard=(1, 1)))
    S.add(texte(560, 270, "Elles ont peur…", 46, VERT, contour="#fff"))
    S.add(texte(560, 330, "de MOI ?", 52, VERT, contour="#fff"))
    for xx in (470, 600):
        S.add(ellipse(xx, 720, 34, 10, "none", stroke="#d0ebff", stroke_width=4))
    return S


def p09():
    S = Scene()
    mare(S)
    S.add(lievre(190, 710, 1.45, expr="fier", bras="hanches"))
    S.add(paillettes(500, 330, 1.0))
    S.add(bulle(420, 120, 620, 120, "Moi aussi, je fais peur !\nJe suis un vrai lion !", 38, pointe=(220, 260)))
    return S


def p10():
    S = Scene()
    mare(S)
    S.add(lievre(170, 700, 1.25, expr="surpris", bras="bas", regard=(1, 1)))
    S.add(nenuphar(500, 740, 0.9))
    S.add(grenouille(480, 732, 0.55, expr="inquiet", bras="calin", regard=(-1, 0)))
    S.add(bulle(520, 300, 400, 110, "Tu… tu vas\nnous manger ?", 34, pointe=(480, 580)))
    return S


def p11():
    S = Scene()
    mare(S)
    S.add(lievre(170, 720, 1.3, expr="sourire", bras="ouverts", regard=(1, 1)))
    S.add(nenuphar(500, 740, 0.9))
    S.add(grenouille(480, 732, 0.55, expr="surpris", bras="bas", regard=(-1, 0)))
    S.add(bulle(330, 170, 560, 130, "Mais non ! Je mange de l'herbe.\nEt moi aussi, j'ai peur de tout.", 32, pointe=(190, 400)))
    return S


def p12():
    S = Scene()
    mare(S)
    S.add(lievre(160, 720, 1.25, expr="content", bras="bas", regard=(1, 1)))
    for k, (xx, yy) in enumerate([(400, 740), (520, 750), (640, 700), (470, 680)]):
        S.add(grenouille(xx, yy, 0.5, expr=["timide", "sourire", "surpris", "timide"][k], regard=(-1, 0)))
    S.add(texte(500, 260, "Une, deux, trois…", 46, VERT, contour="#fff"))
    return S


def p13():
    S = Scene()
    mare(S, soir=True)
    S.add(soleil(680, 140, 40, "#ffa94d"))
    S.add(lievre(170, 720, 1.25, expr="rire", bras="calin", regard=(1, 0)))
    for k, (xx, yy) in enumerate([(420, 740), (540, 750), (650, 700)]):
        S.add(grenouille(xx, yy, 0.5, expr="rire", bras="haut" if k == 1 else "calin", regard=(-1, 0)))
    S.add(grande_feuille(420, 360, 0.35, "#ff922b", "#e8590c", rot=-20))
    S.add(texte(560, 270, "Ha ha ha !", 48, VERT, contour="#fff"))
    return S


def p14():
    S = Scene()
    mare(S, nuit_=True)
    S.add(lievre(200, 720, 1.3, expr="dort", bras="calin"))
    S.add(grenouille(320, 712, 0.5, expr="dort", bras="calin"))
    S.add(nenuphar(470, 740, 0.7))
    S.add(grenouille(450, 734, 0.5, expr="dort", bras="calin"))
    S.add(zzz(270, 400, 1.0, "#e5dbff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("lievre-seul.svg", vignette),
    ("01-dans-son-gite.svg", p01), ("02-une-feuille.svg", p02), ("03-le-vent.svg", p03),
    ("04-malheureux.svg", p04), ("05-crac.svg", p05), ("06-vite.svg", p06),
    ("07-plouf.svg", p07), ("08-de-moi.svg", p08), ("09-un-vrai-lion.svg", p09),
    ("10-tu-vas-nous-manger.svg", p10), ("11-moi-aussi.svg", p11), ("12-une-deux-trois.svg", p12),
    ("13-ha-ha.svg", p13), ("14-bonne-nuit.svg", p14),
]
