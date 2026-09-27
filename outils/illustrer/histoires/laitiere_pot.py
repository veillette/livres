"""La Laitière et le Pot au lait — rêver, mais regarder où l'on marche."""
from fables import *

ID = "laitiere-pot"

PERRETTE = dict(coiffure="tresses", cheveux="blond", peau="claire", habit="#f06595", chaussures="#a61e4d")


def perrette(x, y, s=1.0, pot=True, **k):
    if pot:
        k.setdefault("bras", "tete")
        k["objet"] = pot_lait(0, -202, 1.0)
    return personne(x, y, s, **{**PERRETTE, **k})


def poussin(x, y, s=1.0, **k):
    k.setdefault("couleur", "#ffe066")
    k.setdefault("ventre", "#fff9db")
    return oiseau(x, y, s, **k)


def panier_oeufs(x, y, s=1.0):
    m = [chemin("M -80 -60 Q -80 -130 0 -130 Q 80 -130 80 -60", stroke="#a0522d", sw=8)]
    for k in range(7):
        m.append(oeuf(-60 + k * 20, -46 - (k % 2) * 10, 0.7))
    m += [chemin("M -90 -60 L 90 -60 L 70 0 L -70 0 Z", "#d9a066"),
          trait(-84, -40, 84, -40, "#a0522d", 4), trait(-78, -20, 78, -20, "#a0522d", 4)]
    return place(m, x, y, s)


def campagne(S, soleil_=True, chemin_=True):
    ciel(S, "#a5d8ff", "#fff9db")
    if soleil_:
        S.add(soleil(680, 110, 46))
    S.add(nuage(160, 120, 0.6))
    collines(S, 560, "#b2f2bb", graine=21)
    sol(S, 580, "#8ce99a")
    if chemin_:
        S.add(chemin("M 0 700 Q 400 640 800 690 L 800 800 L 0 800 Z", "#f3d9a4"))
    S.add(fleur(60, 640, 0.8, "#ff8787"), fleur(740, 620, 0.8, "#cc5de8"))


def reve(S, contenu, depuis=(360, 380)):
    S.add(pensee(430, 200, 190, depuis=depuis, contenu=contenu))


def couverture():
    S = Scene()
    campagne(S)
    S.add(perrette(400, 760, 1.55, expr="content", regard=(1, -1)))
    S.add(pensee(640, 250, 110, depuis=(470, 420), contenu=g([perso("boeuf", 610, 310, 0.45, expr="content"), perso("cochon", 690, 310, 0.3, expr="rire")])))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(pot_lait(200, 250, 2.2))
    return S


def p01():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    sol(S, 600, "#8ce99a")
    S.add(maison(640, 620, 1.0, mur="#fff4e6", toit="#c2255c"))
    S.add(barriere(200, 640, 0.8, largeur=360))
    S.add(perso("boeuf", 190, 760, 1.3, expr="content"))
    S.add(perrette(430, 760, 1.35, pot=False, bras="porte", objet=pot_lait(0, -40, 0.9), expr="content"))
    return S


def p02():
    S = Scene()
    campagne(S)
    S.add(maison(120, 600, 0.6, mur="#fff4e6", toit="#c2255c"))
    S.add(perrette(430, 760, 1.55, expr="sourire"))
    S.add(fleche(620, 520, 760, 520, "#fff", 8, 22))
    S.add(texte(690, 490, "marché", 30, "#fff"))
    return S


def p03():
    S = Scene()
    campagne(S)
    S.add(perrette(400, 760, 1.55, expr="rire", rot=4))
    S.add(mouvement(220, 620, 1.2), mouvement(230, 520, 1.0))
    S.add(texte(620, 380, "Tip-tap !", 56, "#c2255c", contour="#fff"))
    return S


def p04():
    S = Scene()
    campagne(S)
    S.add(perrette(240, 760, 1.45, expr="content", regard=(1, -1)))
    reve(S, panier_oeufs(470, 290, 1.2), depuis=(320, 400))
    return S


def p05():
    S = Scene()
    campagne(S)
    S.add(perrette(240, 760, 1.45, expr="rire", regard=(1, -1)))
    reve(S, g([poussin(380, 270, 0.5, expr="rire"), poussin(460, 250, 0.55, expr="content", ailes="haut"),
               poussin(540, 280, 0.5, expr="joie"), poussin(430, 330, 0.45, expr="content"), poussin(510, 335, 0.42)]),
         depuis=(320, 400))
    return S


def p06():
    S = Scene()
    campagne(S)
    S.add(perrette(240, 760, 1.45, expr="rire", regard=(1, -1)))
    reve(S, perso("cochon", 470, 330, 0.75, expr="rire", bras="haut"), depuis=(320, 400))
    return S


def p07():
    S = Scene()
    campagne(S)
    S.add(perrette(240, 760, 1.45, expr="fier", regard=(1, -1)))
    reve(S, g([perso("boeuf", 420, 340, 0.65, expr="content"),
               perso("boeuf", 540, 340, 0.42, expr="rire")]), depuis=(320, 400))
    return S


def p08():
    S = Scene()
    campagne(S)
    S.add(perrette(400, 700, 1.5, expr="rire"))
    S.add(mouvement(400, 760, 1.0, rot=90))
    S.add(texte(160, 330, "Hop !", 64, "#c2255c", contour="#fff"))
    S.add(texte(640, 360, "Hop !", 50, "#c2255c", contour="#fff"))
    return S


def p09():
    S = Scene()
    campagne(S)
    S.add(perrette(360, 720, 1.5, pot=False, expr="surpris", bras="haut", regard=(1, -1)))
    S.add(pot_lait(560, 330, 1.3, rot=50))
    S.add(g([chemin("M 600 300 q 30 -20 50 10", stroke="#f8f9fa", sw=10)]))
    S.add(mouvement(510, 260, 1.0, rot=-40))
    return S


def p10():
    S = Scene()
    campagne(S)
    S.add(ellipse(430, 740, 200, 40, "#f8f9fa"))
    S.add(pot_lait(430, 740, 1.6, casse=True))
    S.add(perrette(200, 760, 1.2, pot=False, expr="bouche_bee", bras="joues", regard=(1, 1)))
    S.add(texte(560, 380, "CRAC !", 80, "#c2255c", contour="#fff"))
    return S


def p11():
    S = Scene()
    campagne(S)
    S.add(ellipse(560, 740, 180, 36, "#f8f9fa"))
    S.add(perrette(260, 760, 1.35, pot=False, expr="triste", bras="bas", regard=(1, -1)))
    for bx, by, r, dessin in [(480, 420, 95, perso("boeuf", 0, 50, 0.5, expr="triste")),
                               (650, 300, 85, perso("cochon", 0, 50, 0.45, expr="triste")),
                               (470, 200, 75, poussin(0, 40, 0.65, expr="triste")),
                               (640, 110, 60, oeuf(0, 30, 1.2))]:
        S.add(cercle(bx, by, r, "#e7f5ff", opacity=0.6, stroke="#fff", stroke_width=4))
        S.add(place(dessin, bx, by))
    return S


def p12():
    S = Scene()
    campagne(S)
    S.add(ellipse(560, 740, 180, 36, "#f8f9fa"))
    S.add(pot_lait(560, 740, 1.2, casse=True))
    S.add(perrette(290, 760, 1.4, pot=False, expr="pleure", bras="yeux"))
    return S


def p13():
    S = Scene()
    campagne(S)
    S.add(ellipse(540, 740, 180, 36, "#f8f9fa"))
    S.add(perso("chat", 560, 750, 0.9, expr="miam", bras="bas"))
    S.add(perrette(260, 760, 1.4, pot=False, expr="timide", bras="bas", regard=(1, 1)))
    S.add(bulle(580, 320, 220, 90, "Miaou !", 44, pointe=(560, 540)))
    return S


def p14():
    S = Scene()
    campagne(S)
    S.add(perrette(400, 760, 1.6, pot=False, expr="fier", bras="hanches"))
    S.add(bulle(400, 120, 540, 110, "La prochaine fois, je regarderai\noù je mets les pieds !", 32, pointe=(400, 380)))
    return S


def p15():
    S = Scene()
    campagne(S)
    S.add(perrette(400, 760, 1.55, expr="content", regard=(1, 0)))
    S.add(pensee(640, 230, 90, depuis=(500, 410), contenu=poussin(640, 270, 0.5, expr="rire")))
    S.add(fleche(120, 700, 250, 700, "#fff", 8, 22))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("pot-seul.svg", vignette),
    ("01-le-lait.svg", p01), ("02-en-route.svg", p02), ("03-tip-tap.svg", p03),
    ("04-cent-oeufs.svg", p04), ("05-les-poussins.svg", p05), ("06-le-cochon.svg", p06),
    ("07-la-vache.svg", p07), ("08-hop.svg", p08), ("09-le-pot-glisse.svg", p09),
    ("10-crac.svg", p10), ("11-adieu.svg", p11), ("12-perrette-pleure.svg", p12),
    ("13-le-chat.svg", p13), ("14-la-prochaine-fois.svg", p14), ("15-le-lendemain.svg", p15),
]
