"""Le Loup et la Cigogne — quand on nous rend service, on dit merci."""
from fables import *
from contes import foret, panier

ID = "loup-cigogne"


def loup(x, y, s=1.0, **k):
    return perso("loup", x, y, s, **k)


def clairiere(S, soir=False, graine=41):
    foret(S, "#ffc078" if soir else "#a5d8ff", "#fff4e6" if soir else "#ebfbee", y=600, graine=graine)
    S.add(herbe(120, 700), herbe(680, 720), herbe(330, 760, 0.8))


def tas_os(x, y, s=1.0):
    rr = random.Random(4)
    return place([os_(rr.uniform(-60, 60), -10 - k * 12, 0.7, rot=rr.uniform(-40, 40)) for k in range(6)], x, y, s)


def soigne(S, objet=None, expr_c="concentre"):
    """La cigogne plonge son bec dans la gueule grande ouverte du loup."""
    S.add(loup(560, 790, 1.7, expr="bouche_bee", bras="large", regard=(0, -1)))
    S.add(cigogne(394, 776, 1.2, cou="table", expr=expr_c, objet=objet))


def couverture():
    S = Scene()
    clairiere(S)
    soigne(S)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(ellipse(200, 138, 192, 132, "#e7f5ff"))
    S.add(cigogne(140, 262, 0.68, expr="sourire"))
    return S


def p01():
    S = Scene()
    clairiere(S)
    S.add(tas_os(250, 760, 1.0))
    S.add(loup(450, 760, 1.5, expr="miam", bras="porte", objet=os_(0, -84, 0.9, rot=-20)))
    S.add(texte(620, 300, "Miam ! Miam !", 50, "#e8590c", contour="#fff"))
    return S


def p02():
    S = Scene()
    clairiere(S)
    S.add(loup(400, 760, 1.6, expr="oups", bras="bouche"))
    S.add(os_(400, 600, 0.55, rot=20))
    S.add(eclat(400, 600, 1.0, "#fa5252"))
    S.add(texte(620, 300, "Crac !", 60, "#c92a2a", contour="#fff"))
    return S


def p03():
    S = Scene()
    clairiere(S)
    S.add(loup(380, 760, 1.5, expr="oups", bras="tete", rot=-6))
    S.add(mouvement(250, 580, 1.0), mouvement(560, 580, 1.0, rot=180))
    S.add(texte(600, 270, "Kof ! Kof !", 54, "#e8590c", contour="#fff"))
    S.cachette(650, 70, "air")
    return S


def p04():
    S = Scene()
    clairiere(S)
    S.add(cigogne(180, 740, 0.95, expr="surpris", regard=(1, 0)))
    S.add(loup(560, 760, 1.4, expr="oups", bras="bouche", regard=(-1, 0)))
    return S


def p05():
    S = Scene()
    clairiere(S)
    S.add(cigogne(140, 740, 0.95, expr="inquiet", regard=(1, 0)))
    S.add(loup(540, 760, 1.4, expr="triste", bras="ouverts", regard=(-1, 0)))
    S.add(bulle(520, 160, 520, 130, "Ôtez-moi cet os…\nje vous paierai bien !", 36, pointe=(540, 390)))
    return S


def p06():
    S = Scene()
    clairiere(S)
    S.add(cigogne(150, 740, 0.95, expr="inquiet", regard=(1, 0)))
    S.add(loup(540, 760, 1.5, expr="bouche_bee", bras="large", regard=(-1, -1)))
    S.add(texte(560, 230, "Aaaah…", 54, "#e8590c", contour="#fff"))
    return S


def p07():
    S = Scene()
    clairiere(S)
    soigne(S)
    S.add(texte(240, 230, "Tout doux…", 46, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    clairiere(S)
    S.add(loup(560, 780, 1.5, expr="surpris", bras="large", regard=(-1, -1)))
    S.add(cigogne(220, 740, 1.0, expr="fier", objet=os_(10, 0, 0.6, rot=10)))
    S.add(texte(560, 250, "Hop !", 60, "#e8590c", contour="#fff"))
    return S


def p09():
    S = Scene()
    clairiere(S)
    S.add(loup(450, 760, 1.6, expr="content", bras="ouverts"))
    S.add(texte(450, 220, "Ahhh ! Que ça fait du bien !", 44, "#e8590c", contour="#fff"))
    return S


def p10():
    S = Scene()
    clairiere(S)
    S.add(cigogne(150, 740, 0.95, expr="sourire", regard=(1, 0)))
    S.add(loup(560, 760, 1.4, expr="content", bras="hanches", regard=(-1, 0)))
    S.add(bulle(330, 170, 480, 120, "Et mon salaire,\ns'il vous plaît ?", 36, pointe=(260, 360)))
    return S


def p11():
    S = Scene()
    clairiere(S)
    S.add(cigogne(150, 740, 0.95, expr="surpris", regard=(1, 0)))
    S.add(loup(560, 760, 1.45, expr="rire", bras="hanches", regard=(-1, 0)))
    S.add(bulle(500, 160, 580, 150, "Ta tête est sortie de ma\ngueule tout entière :\nc'est bien assez !", 32, pointe=(560, 410)))
    return S


def p12():
    S = Scene()
    clairiere(S)
    S.add(loup(220, 760, 1.2, expr="rire", bras="hanches", regard=(1, 0)))
    S.add(cigogne(520, 740, 0.95, expr="fache", flip=True))
    S.add(texte(560, 250, "Hmpf !", 56, "#e8590c", contour="#fff"))
    return S


def p13():
    S = Scene()
    clairiere(S, graine=42)
    S.add(perso("lapin", 140, 760, 0.95, expr="fache", bras="croises"))
    S.add(perso("ecureuil", 300, 760, 0.9, expr="fache", bras="croises"))
    S.add(perso("ours", 470, 760, 1.1, expr="fache", bras="croises"))
    S.add(loup(680, 760, 1.0, expr="triste", bras="bas", regard=(-1, 0)))
    S.add(cigogne(110, 600, 0.5, expr="sourire", flip=True))
    S.cachette(215, 775)
    return S


def p14():
    S = Scene()
    clairiere(S, soir=True, graine=43)
    S.add(lune(660, 130, 40))
    S.add(loup(400, 760, 1.5, expr="pleure", bras="calin"))
    S.add(texte(400, 260, "Tout seul…", 50, "#e8590c", contour="#fff"))
    return S


def p15():
    S = Scene()
    clairiere(S, graine=44)
    poissons = g([poisson_riviere(-18, -64, 0.4, rot=-20), poisson_riviere(18, -70, 0.4, rot=20, flip=True)])
    S.add(cigogne(160, 740, 0.95, expr="surpris", regard=(1, 0)))
    S.add(loup(540, 760, 1.4, expr="timide", bras="donne", regard=(-1, 0)))
    S.add(place([poissons, panier(0, 0, 1.0, contenu=None)], 420, 690, 1.0))
    S.add(bulle(560, 160, 440, 120, "Pardon…\net merci !", 38, pointe=(560, 390)))
    return S


def p16():
    S = Scene()
    clairiere(S, graine=44)
    S.add(cigogne(180, 740, 0.95, expr="rire", regard=(1, 0)))
    S.add(loup(540, 760, 1.4, expr="content", bras="calin", regard=(-1, 0)))
    S.add(coeur(360, 300, 1.1))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cigogne-seule.svg", vignette),
    ("01-le-loup-mange.svg", p01), ("02-crac.svg", p02), ("03-kof.svg", p03),
    ("04-la-cigogne.svg", p04), ("05-otez-moi-cet-os.svg", p05), ("06-aaah.svg", p06),
    ("07-tout-doux.svg", p07), ("08-hop.svg", p08), ("09-ca-fait-du-bien.svg", p09),
    ("10-mon-salaire.svg", p10), ("11-c-est-bien-assez.svg", p11), ("12-hmpf.svg", p12),
    ("13-plus-personne.svg", p13), ("14-tout-seul.svg", p14), ("15-pardon.svg", p15),
    ("16-amis.svg", p16),
]
