"""Le prince grenouille qui ne voulait pas de bisou — on a le droit de dire non."""
from base import *
from objets import *
from fantastique import *

ID = "prince-grenouille"
LEA = dict(coiffure="longs", cheveux="blond", peau="doree", habit="#9775fa", acc=("diademe",))
CONSEILLERS = [dict(coiffure="chauve_cote", cheveux="gris", habit="#495057", robe=False, acc=("lunettes", "col"), peau="rosee"),
               dict(coiffure="chignon", cheveux="brun", habit="#1098ad", acc=("col",), peau="brune")]


def crapouille(x, y, s=1.0, **k):
    k.setdefault("acc", ("couronne",))
    return perso("grenouille", x, y, s, **k)


def etang_chateau(S, nuit_=False):
    if nuit_:
        nuit(S, "#1c2a52", "#364fc7")
        etoiles(S, 35, graine=11)
        S.add(lune(640, 130, 50))
    else:
        ciel(S, "#a5d8ff", "#f4fce3")
        S.add(chateau(610, 470, 0.45))
        S.add(nuage(160, 110, 0.7))
    sol(S, 470, "#94d82d" if not nuit_ else "#2b8a3e")
    S.add(ellipse(520, 750, 380, 140, "#4dabf7" if not nuit_ else "#1c7ed6"))
    for k in range(4):
        S.add(chemin(f"M {300 + k * 120} {690 + (k % 2) * 70} q 20 -10 40 0", stroke="#a5d8ff", sw=5))
    for x in (40, 760):
        for dx in (-20, 0, 20):
            S.add(trait(x + dx, 560, x + dx * 1.4, 440, "#5c940d", 7))
            S.add(ellipse(x + dx * 1.4, 440, 8, 22, "#8d5524"))


def pensee_prince(x, y):
    """Crapouille quand il était prince : des bottes qui serrent et l'air de s'ennuyer."""
    return place(personne(0, 0, 0.6, coiffure="courts", cheveux="#74b816", habit="#1864ab", robe=False,
                          acc=("couronne", "col"), expr="degoute", bras="croises", peau="claire"), x, y)


def couverture():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(470, 700, 1.9, "#ffc9d6"))
    S.add(crapouille(480, 700, 1.4, expr="rire", bras="haut"))
    S.add(personne(190, 640, 1.4, expr="rire", bras="joues", **LEA))
    S.add(texte(560, 330, "Croa !", 60, "#5c940d", contour="#fff"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(crapouille(200, 262, 1.0, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(400, 690, 1.8, "#ffc9d6"), nenuphar(300, 790, 1.0), nenuphar(660, 760, 1.1))
    S.add(crapouille(410, 690, 1.3, expr="content", bras="salut"))
    return S


def p02():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(520, 700, 1.6))
    S.add(crapouille(530, 700, 1.1, expr="surpris", regard=(-1, -1)))
    S.add(personne(220, 640, 1.4, expr="bouche_bee", bras="montre", regard=(1, 1), **LEA))
    S.add(eclat(560, 420, 1.2, "#ffd43b"))
    return S


def p03():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(540, 700, 1.6))
    S.add(crapouille(550, 700, 1.1, expr="oups", bras="ouverts", regard=(-1, 0)))
    S.add(personne(240, 640, 1.4, expr="content", bras="calin", regard=(1, 0), **LEA))
    S.add(coeur(360, 290, 1.4))
    S.add(bulle(600, 140, 330, 90, "Ah non, merci !", 40, pointe=(570, 480)))
    return S


def p04():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(560, 720, 1.6))
    S.add(crapouille(570, 720, 1.1, expr="degoute", bras="pense", regard=(-1, -1)))
    S.add(pensee(330, 250, 170, pensee_prince(330, 330), depuis=(520, 560)))
    S.add(personne(140, 650, 1.1, expr="surpris", **LEA))
    return S


def p05():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(260, 740, 1.2), nenuphar(620, 700, 1.3))
    S.add(crapouille(260, 740, 0.8, expr="rire", bras="haut"))
    S.add(crapouille(410, 480, 0.9, expr="joie", bras="haut", rot=20))
    S.add(chemin("M 280 640 Q 340 380 400 440", stroke="#fff", sw=4, opacity=0.7, stroke_dasharray="10 12"))
    S.add(crapouille(620, 700, 0.8, expr="chante", bras="ouverts"), notes(680, 520, 0.9))
    S.add(texte(400, 150, "Plouf ! Hop ! Croa !", 52, "#2b8a3e", contour="#fff"))
    return S


def p06():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(640, 720, 1.4))
    S.add(crapouille(650, 720, 0.9, expr="inquiet", regard=(-1, 0)))
    S.add(personne(120, 620, 1.0, expr="neutre", **CONSEILLERS[0]))
    S.add(personne(470, 600, 1.0, expr="neutre", **CONSEILLERS[1]))
    S.add(roi(300, 620, 1.3, expr="fier", bras="montre"))
    S.add(bulle(360, 120, 480, 110, "Princesse, embrassez-la !\nC'est la tradition !", 34, pointe=(320, 290)))
    return S


def p07():
    S = Scene()
    etang_chateau(S)
    S.add(roi(140, 630, 1.1, expr="surpris"))
    S.add(personne(380, 600, 1.4, expr="fache", bras="hanches", **LEA))
    S.add(nenuphar(620, 720, 1.4))
    S.add(crapouille(630, 720, 0.95, expr="timide", regard=(-1, 0)))
    S.add(bulle(420, 120, 460, 110, "Non ! Il a dit non.\nUn bisou, ça se demande !", 32, pointe=(390, 300)))
    return S


def p08():
    S = Scene()
    etang_chateau(S)
    S.add(personne(110, 630, 1.0, expr="rire", bras="haut", **CONSEILLERS[0]))
    S.add(personne(640, 600, 1.0, expr="rire", bras="haut", **CONSEILLERS[1]))
    S.add(roi(380, 600, 1.4, expr="concentre", bras="tete"))
    S.add(texte(400, 150, "Hum… elle a raison !", 50, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(530, 700, 1.5))
    S.add(crapouille(540, 700, 1.1, expr="rire", bras="salut", regard=(-1, 0)))
    S.add(personne(230, 640, 1.4, expr="rire", bras="joues", regard=(1, 0), **LEA))
    S.add(bulle(560, 130, 460, 110, "Je t'apprends à sauter\ncomme une grenouille ?", 32, pointe=(560, 460)))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#f4fce3")
    S.add(chateau(620, 520, 0.5))
    sol(S, 520, "#94d82d")
    S.add(flaque(360, 720, 2.2, eclabousse=True))
    S.add(personne(360, 560, 1.35, expr="rire", bras="haut", **LEA))
    S.add(crapouille(620, 740, 0.9, expr="rire", bras="haut"))
    S.add(texte(360, 130, "PLOUF !", 90, "#1c7ed6", contour="#fff", rot=-6))
    return S


def p11():
    S = Scene()
    etang_chateau(S, nuit_=True)
    S.add(nenuphar(520, 720, 1.5))
    S.add(crapouille(530, 720, 1.0, expr="chante", bras="ouverts"))
    S.add(personne(250, 640, 1.3, expr="chante", bras="ouverts", **LEA))
    S.add(notes(360, 300, 1.1, "#ffe066"), notes(560, 380, 0.9, "#ffe066"))
    return S


def p12():
    S = Scene()
    etang_chateau(S)
    S.add(nenuphar(470, 700, 1.4))
    S.add(personne(260, 640, 1.4, expr="rire", bras="salut", **LEA))
    S.add(crapouille(480, 700, 1.0, expr="rire", bras="salut", flip=True))
    S.add(coeur(380, 250, 1.6), coeur(440, 190, 1.0, "#94d82d"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("crapouille-seul.svg", vignette),
    ("01-l-etang.svg", p01), ("02-une-couronne.svg", p02), ("03-non-merci.svg", p03),
    ("04-prince.svg", p04), ("05-grenouille.svg", p05), ("06-le-roi.svg", p06),
    ("07-il-a-dit-non.svg", p07), ("08-elle-a-raison.svg", p08), ("09-sauter.svg", p09),
    ("10-plouf.svg", p10), ("11-chanter.svg", p11), ("12-amis.svg", p12),
]
