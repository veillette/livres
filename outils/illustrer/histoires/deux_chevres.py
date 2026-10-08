"""Les Deux Chèvres — céder le passage, ce n'est pas perdre."""
from fables import *
from contes import pre_vert

ID = "deux-chevres"

BLEU = "#1098ad"


def blanchette(x, y, s=1.0, **k):
    """La chèvre blanche, qui vient de la gauche."""
    k.setdefault("couleur", "#f8f9fa")
    k.setdefault("acc", ("echarpe",))
    k.setdefault("couleur_acc", "#4dabf7")
    return perso("chevre", x, y, s, **k)


def biquette(x, y, s=1.0, **k):
    """La chèvre rousse, qui vient de la droite."""
    k.setdefault("couleur", "#d8a47f")
    k.setdefault("acc", ("noeud",))
    k.setdefault("couleur_acc", "#e64980")
    return perso("chevre", x, y, s, **k)


def merle(x, y, s=1.0, **k):
    k.setdefault("couleur", "#343a40")
    k.setdefault("ventre", "#495057")
    return oiseau(x, y, s, **k)


def montagne(S, graine=61):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(montagnes(None, 520, ("#b2c4ff", "#91a7ff"), neige=True))
    collines(S, 600, "#8ce99a", graine=graine)
    sol(S, 620, "#69db7c")


def gerbe(x, y, s=1.0):
    m = [ellipse(0, 0, 110, 24, "#d0ebff")]
    for k, (dx, h) in enumerate([(-70, 60), (-30, 100), (10, 120), (50, 90), (84, 50)]):
        m.append(goutte(dx, -h, 1.4, "#a5d8ff"))
    return place(m, x, y, s)


def couverture():
    S = Scene()
    pont_tronc(S, y=560)
    S.add(blanchette(300, 560, 1.25, expr="fache", bras="poing", regard=(1, 0)))
    S.add(biquette(500, 560, 1.25, expr="fache", bras="poing", regard=(-1, 0)))
    S.cachette(70, 370, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(blanchette(130, 262, 0.75, expr="sourire"))
    S.add(biquette(270, 262, 0.75, expr="sourire"))
    return S


def p01():
    S = Scene()
    montagne(S)
    S.add(blanchette(220, 730, 1.2, expr="rire", bras="saute"))
    S.add(biquette(580, 730, 1.2, expr="rire", bras="saute"))
    S.add(texte(400, 300, "Hop ! Hop !", 54, BLEU, contour="#fff"))
    return S


def p02():
    S = Scene()
    montagne(S, graine=62)
    for k in range(6):
        S.add(fleur(60 + k * 140, 740 + (k % 2) * 30, 0.8, ["#ff8787", "#fcc419", "#fff"][k % 3]))
    S.add(blanchette(400, 720, 1.4, expr="miam", bras="pense", regard=(1, -1)))
    S.add(pensee(640, 260, 120, g([herbe(610, 290, 1.4), herbe(660, 290, 1.4), fleur(640, 300, 0.7, "#ff8787")]), depuis=(470, 420)))
    return S


def p03():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(90, 506, 0.9, expr="surpris", regard=(1, 0)))
    S.add(biquette(710, 506, 0.9, expr="surpris", regard=(-1, 0)))
    S.add(texte(400, 360, "Un seul passage…", 46, BLEU, contour="#fff"))
    S.cachette(650, 70, "air")
    return S


def p04():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(230, 520, 0.9, expr="fier", bras="bas", regard=(1, 0)))
    S.add(biquette(570, 520, 0.9, expr="fier", bras="bas", regard=(-1, 0)))
    S.add(texte(400, 200, "Un pas… puis un autre…", 40, BLEU, contour="#fff"))
    S.cachette(70, 370, "air")
    return S


def p05():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(330, 520, 0.95, expr="fache", bras="hanches", regard=(1, 0)))
    S.add(biquette(470, 520, 0.95, expr="fache", bras="hanches", regard=(-1, 0)))
    S.add(bulle(210, 130, 300, 90, "Recule !", 40, pointe=(300, 250)))
    S.add(bulle(590, 130, 360, 90, "Non, toi !", 40, pointe=(500, 250)))
    S.cachette(70, 370, "air")
    return S


def p06():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(330, 520, 0.95, expr="fier", bras="montre", regard=(1, 0)))
    S.add(biquette(470, 520, 0.95, expr="fache", bras="croises", regard=(-1, 0)))
    S.add(bulle(400, 110, 620, 120, "Ma grand-mère était la chèvre\nla plus célèbre du pays !", 32, pointe=(320, 250)))
    S.cachette(70, 370, "air")
    return S


def p07():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(330, 520, 0.95, expr="fache", bras="croises", regard=(1, 0)))
    S.add(biquette(470, 520, 0.95, expr="fier", bras="montre", regard=(-1, 0), flip=True))
    S.add(bulle(400, 110, 620, 120, "Et la mienne était\nla plus belle du royaume !", 32, pointe=(480, 250)))
    S.cachette(70, 370, "air")
    return S


def p08():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(330, 520, 0.95, expr="furieux", bras="poing", regard=(1, 0), rot=14))
    S.add(biquette(470, 520, 0.95, expr="furieux", bras="poing", regard=(-1, 0), rot=-14))
    S.add(eclat(400, 300, 1.0, "#fab005"))
    S.add(texte(160, 330, "Pousse !", 44, BLEU, contour="#fff"))
    S.add(texte(650, 330, "Pousse !", 44, BLEU, contour="#fff"))
    S.add(mouvement(400, 548, 0.8, rot=90), mouvement(240, 548, 0.8, rot=90))
    S.cachette(650, 70, "air")
    return S


def p09():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(330, 548, 0.8, expr="oups", bras="haut", rot=-160))
    S.add(mouvement(310, 500, 1.0, rot=-90), mouvement(500, 500, 1.0, rot=-90))
    S.add(biquette(490, 556, 0.8, expr="oups", bras="haut", rot=165))
    S.add(texte(400, 200, "Patatras !", 60, "#c92a2a", contour="#fff"))
    S.cachette(70, 370, "air")
    return S


def p10():
    S = Scene()
    pont_tronc(S)
    S.add(gerbe(400, 690, 1.3))
    S.add(texte(400, 320, "PLOUF !", 72, "#1971c2", contour="#fff"))
    S.cachette(70, 370, "air")
    return S


def p11():
    S = Scene()
    montagne(S, graine=63)
    S.add(rect(0, 680, 800, 120, "#4dabf7"))
    S.add(blanchette(260, 720, 1.2, expr="pleure", bras="bas", regard=(1, 0)))
    S.add(biquette(540, 720, 1.2, expr="degoute", bras="bas", regard=(-1, 0)))
    for xx in (220, 300, 500, 580):
        S.add(goutte(xx, 600, 1.0, "#74c0fc"))
    S.add(texte(400, 270, "Atchoum !", 50, BLEU, contour="#fff"))
    return S


def p12():
    S = Scene()
    montagne(S, graine=63)
    S.add(caillou(620, 640, 2.4, "#868e96"))
    S.add(merle(620, 570, 0.9, expr="rire", bec_ouvert=True, regard=(-1, 1)))
    S.add(blanchette(200, 730, 1.1, expr="triste", bras="bas", regard=(1, -1)))
    S.add(biquette(400, 730, 1.1, expr="triste", bras="bas", regard=(1, -1)))
    S.add(bulle(400, 150, 640, 140, "Si l'une avait laissé passer l'autre,\nvous seriez sèches,\net le ventre plein !", 30, pointe=(600, 440)))
    return S


def p13():
    S = Scene()
    montagne(S, graine=64)
    S.add(blanchette(250, 730, 1.3, expr="rire", bras="calin", regard=(1, 0)))
    S.add(biquette(550, 730, 1.3, expr="rire", bras="calin", regard=(-1, 0)))
    S.add(texte(400, 280, "Ha ha ha !", 54, BLEU, contour="#fff"))
    return S


def p14():
    S = Scene()
    pont_tronc(S)
    S.add(blanchette(560, 520, 0.9, expr="content", bras="salut", regard=(-1, 0)))
    S.add(biquette(90, 506, 0.9, expr="sourire", bras="donne", regard=(1, 0)))
    S.add(bulle(250, 130, 380, 100, "Passe la première !", 34, pointe=(110, 260)))
    S.add(bulle(560, 260, 240, 80, "Merci !", 34, pointe=(560, 300)))
    S.cachette(730, 480, "air")
    return S


def p15():
    S = Scene()
    pre_vert(S, 600)
    S.add(blanchette(260, 740, 1.3, expr="miam", bras="porte", objet=fleur(0, -66, 0.8, "#ff8787", tige=30)))
    S.add(biquette(540, 740, 1.3, expr="miam", bras="porte", objet=fleur(0, -66, 0.8, "#fcc419", tige=30)))
    S.add(coeur(400, 360, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chevres-seules.svg", vignette),
    ("01-deux-chevres.svg", p01), ("02-l-herbe-fraiche.svg", p02), ("03-le-torrent.svg", p03),
    ("04-un-pas.svg", p04), ("05-recule.svg", p05), ("06-ma-grand-mere.svg", p06),
    ("07-et-la-mienne.svg", p07), ("08-pousse.svg", p08), ("09-patatras.svg", p09),
    ("10-plouf.svg", p10), ("11-trempees.svg", p11), ("12-le-merle.svg", p12),
    ("13-elles-rient.svg", p13), ("14-passe-la-premiere.svg", p14), ("15-dans-le-pre.svg", p15),
]
