"""Le Loup, la Chèvre et le Chevreau — deux sûretés valent mieux qu'une."""
from fables import *

ID = "loup-chevre-chevreau"

VIOLET = "#ae3ec9"


def maman(x, y, s=1.0, **k):
    k.setdefault("acc", ("tablier",))
    return perso("chevre", x, y, s, **k)


def chevreau(x, y, s=1.0, **k):
    k.setdefault("couleur", "#f8f9fa")
    k.setdefault("acc", ("echarpe",))
    k.setdefault("couleur_acc", "#ae3ec9")
    return perso("chevre", x, y, s, **k)


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def patte(x, y, s=1.0, couleur="#868e96", rot=0):
    """Patte levée, vue de face ; (x, y) = centre de la paume."""
    c2 = assombrir(couleur, 0.75) if couleur != "#f8f9fa" else "#ffc9c9"
    m = [rect(-22, 0, 44, 90, couleur, rx=18), cercle(0, 0, 34, couleur), ellipse(0, 8, 16, 12, c2)]
    for dx, dy in ((-22, -22), (-8, -32), (8, -32), (22, -22)):
        m.append(ellipse(dx, dy, 7, 9, c2))
    return place(m, x, y, s, rot=rot)


def chaumiere(S, soir=False, regard_fenetre=None, porte_ouverte=False):
    """La maison des chèvres, vue de face : fenêtre à gauche, porte à droite."""
    ciel(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#fff9db")
    collines(S, 600, "#b2f2bb", graine=81)
    sol(S, 700, "#8ce99a")
    S.add(rect(240, 380, 520, 340, "#ffe8cc"))
    S.add(poly([(210, 390), (500, 190), (790, 390)], "#c2703d"))
    S.add(chemin("M 230 380 Q 500 360 770 380", stroke="#a85a2c", sw=10))
    S.add(fenetre(300, 430, 140, 120, contenu=regard_fenetre or "", rideaux="#ae3ec9"))
    S.add(porte(640, 720, 130, 230, "#8d5524", ouverte=porte_ouverte))
    S.add(fleur(270, 720, 0.8, "#ff8787"), fleur(470, 720, 0.7, "#fcc419"))


def dans_la_maison(S, soir=False):
    interieur(S, "#f3f0ff", "#c9a27e", 580, papier="#e5dbff")
    S.add(porte(600, 580, 170, 330, "#8d5524"))
    S.add(rect(590, 360, 22, 10, "#495057", rx=3))
    S.add(fenetre(90, 150, 170, 150, "#ffc078" if soir else "#a5d8ff", rideaux="#ae3ec9"))


def tete_chevreau_fenetre(expr="surpris", regard=(1, 0)):
    return chevreau(370, 600, 0.75, expr=expr, regard=regard)


def couverture():
    S = Scene()
    chaumiere(S, regard_fenetre=tete_chevreau_fenetre("malin", (1, 0)))
    S.add(loup(540, 760, 1.25, expr="malin", bras="tient", regard=(-1, 0)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chevreau(200, 262, 0.85, expr="content"))
    return S


def p01():
    S = Scene()
    chaumiere(S)
    S.add(maman(300, 770, 1.3, expr="sourire", bras="bas", regard=(1, 0)))
    S.add(chevreau(520, 770, 0.9, expr="content", bras="bas", regard=(-1, 0)))
    return S


def p02():
    S = Scene()
    chaumiere(S)
    S.add(maman(300, 770, 1.3, expr="sourire", bras="montre", regard=(1, 0)))
    S.add(chevreau(540, 770, 0.9, expr="concentre", bras="bas", regard=(-1, -1)))
    S.add(bulle(400, 110, 640, 130, "N'ouvre qu'à qui dira :\n« Foin du loup et de sa race ! »", 32, pointe=(320, 400)))
    return S


def p03():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=82)
    sol(S, 640, "#8ce99a")
    S.add(maman(640, 760, 0.9, expr="sourire", bras="salut", flip=True))
    S.add(loup(250, 770, 1.3, expr="malin", bras="bouche", regard=(1, 0)))
    S.add(buisson(250, 790, 1.7), buisson(90, 790, 1.2))
    S.add(texte(250, 260, "J'ai tout entendu…", 42, VIOLET, contour="#fff"))
    return S


def p04():
    S = Scene()
    dans_la_maison(S)
    S.add(chevreau(520, 760, 1.2, expr="concentre", bras="tient", regard=(1, -1)))
    S.add(texte(300, 420, "Clic !", 56, VIOLET, contour="#fff"))
    return S


def p05():
    S = Scene()
    chaumiere(S)
    S.add(loup(530, 760, 1.25, expr="malin", bras="bouche", regard=(1, 0)))
    S.add(texte(650, 340, "Toc ! Toc !", 46, VIOLET, contour="#fff"))
    S.add(bulle(300, 160, 500, 120, "Foin du loup\net de sa race !", 36, pointe=(500, 420)))
    return S


def p06():
    S = Scene()
    dans_la_maison(S)
    S.add(chevreau(470, 760, 1.25, expr="inquiet", bras="pense", regard=(1, 0)))
    S.add(texte(530, 190, "C'est bien le mot de passe…", 34, VIOLET, contour="#fff"))
    S.add(texte(530, 240, "mais quelle grosse voix !", 34, VIOLET, contour="#fff"))
    return S


def p07():
    S = Scene()
    chaumiere(S, regard_fenetre=tete_chevreau_fenetre("malin", (1, 0)))
    S.add(loup(560, 760, 1.2, expr="surpris", bras="bas", regard=(-1, -1)))
    S.add(bulle(360, 160, 560, 120, "Montrez-moi patte blanche,\nou je n'ouvre point !", 34, pointe=(370, 440)))
    return S


def p08():
    S = Scene()
    chaumiere(S, regard_fenetre=tete_chevreau_fenetre("malin", (1, 0)))
    S.add(loup(560, 760, 1.2, expr="oups", bras="bas", regard=(1, -1)))
    S.add(patte(690, 470, 0.9))
    S.add(texte(400, 140, "Patte… blanche ?", 46, VIOLET, contour="#fff"))
    return S


def p09():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    collines(S, 600, "#b2f2bb", graine=83)
    sol(S, 640, "#8ce99a")
    S.add(sapin(600, 640, 1.3), sapin(720, 650, 1.1))
    S.add(loup(400, 760, 1.35, expr="furieux", bras="poing", flip=True))
    S.add(texte(320, 250, "Grrr ! Raté !", 52, "#c92a2a", contour="#fff"))
    return S


def p10():
    S = Scene()
    chaumiere(S, soir=True, regard_fenetre=tete_chevreau_fenetre("surpris", (1, 0)))
    S.add(maman(560, 770, 1.15, expr="sourire", bras="salut", regard=(-1, -1)))
    S.add(patte(700, 470, 0.9, "#f8f9fa", rot=10))
    S.add(bulle(380, 160, 560, 120, "Foin du loup et de sa race !\nVoici ma patte blanche.", 32, pointe=(520, 430)))
    return S


def p11():
    S = Scene()
    chaumiere(S, soir=True, porte_ouverte=True)
    S.add(maman(470, 770, 1.25, expr="content", bras="calin", regard=(1, 0)))
    S.add(chevreau(620, 770, 0.9, expr="rire", bras="ouverts", regard=(-1, 0)))
    S.add(coeur(540, 400, 1.1))
    return S


def p12():
    S = Scene()
    dans_la_maison(S, soir=True)
    S.add(maman(260, 760, 1.35, expr="fier", bras="hanches", regard=(1, 0)))
    S.add(chevreau(520, 760, 1.0, expr="rire", bras="haut", regard=(-1, 0)))
    S.add(bulle(380, 120, 560, 120, "Deux sûretés valent\nmieux qu'une !", 38, pointe=(300, 340)))
    return S


def p13():
    S = Scene()
    dans_la_maison(S, soir=True)
    S.add(lampe(170, 580, 1.0))
    S.add(maman(380, 760, 1.3, expr="dort", bras="calin"))
    S.add(chevreau(470, 770, 0.8, expr="dort", bras="calin"))
    S.add(zzz(560, 330, 1.0))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("chevreau-seul.svg", vignette),
    ("01-la-maison.svg", p01), ("02-le-mot-de-passe.svg", p02), ("03-le-loup-ecoute.svg", p03),
    ("04-clic.svg", p04), ("05-toc-toc.svg", p05), ("06-quelle-grosse-voix.svg", p06),
    ("07-patte-blanche.svg", p07), ("08-patte-grise.svg", p08), ("09-rate.svg", p09),
    ("10-maman-revient.svg", p10), ("11-calin.svg", p11), ("12-deux-suretes.svg", p12),
    ("13-bonne-nuit.svg", p13),
]
