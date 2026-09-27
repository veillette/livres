"""La Cigale et la Fourmi — penser à demain, et savoir partager."""
from fables import *

ID = "cigale-fourmi"


def cigale(x, y, s=1.0, **k):
    return perso("cigale", x, y, s, **k)


def fourmi(x, y, s=1.0, **k):
    k.setdefault("acc", ("tablier",))
    return perso("fourmi", x, y, s, **k)


def avec_violon(**k):
    return dict(bras="porte", objet=g([violon(-6, -96, 0.9, rot=-55), archet(18, -84, 0.8, rot=60)]), **k)


def ete(S):
    ciel(S, "#74c0fc", "#fff9db")
    S.add(soleil(680, 120, 55))
    collines(S, 600, "#b2f2bb", graine=2)
    sol(S, 620, "#8ce99a")
    for fx in (60, 140, 700, 760):
        S.add(fleur(fx, 700 + (fx % 3) * 20, 0.9, "#ff8787" if fx % 2 else "#fcc419"))
    S.add(herbe(250, 720, 1.2), herbe(560, 740, 1.0))


def automne(S):
    ciel(S, "#ffd8a8", "#fff4e6")
    collines(S, 600, "#ffc078", graine=2)
    sol(S, 620, "#d9a066")
    S.add(arbre(140, 640, 1.2, feuillage="#fd7e14", feuillage2="#f59f00"))
    S.add(arbre(700, 630, 0.9, feuillage="#e8590c", feuillage2="#fab005"))
    rr = random.Random(5)
    for _ in range(9):
        S.add(grande_feuille(rr.uniform(0, 800), rr.uniform(150, 600), 0.16, rr.choice(["#fd7e14", "#fab005", "#e8590c"]), "#c2410c", rot=rr.uniform(0, 360)))


def hiver(S, neige_y=620):
    ciel(S, "#a5b4c8", "#e9ecef")
    sol(S, neige_y, "#f8f9fa")
    S.add(sapin(90, neige_y + 40, 1.0, neige=True), sapin(720, neige_y + 30, 0.8, neige=True))
    flocons(S, 50, graine=3)


def maison_fourmi(x, y, s=1.0, ouverte=False, neige=False, dedans=None):
    """Fourmilière avec une porte ronde en bois et une fenêtre allumée ; (x, y) = milieu au sol."""
    m = [chemin("M -260 0 Q -220 -300 0 -310 Q 220 -300 260 0 Z", "#c49a6c"),
         chemin("M -200 -60 q 14 -8 28 0 M 120 -180 q 14 -8 28 0 M 170 -60 q 14 -8 28 0 M -120 -220 q 14 -8 28 0", stroke="#9c7650", sw=5)]
    if neige:
        m.append(chemin("M -150 -250 Q 0 -340 150 -250 Q 100 -270 60 -250 Q 20 -275 -20 -250 Q -70 -272 -150 -250 Z", "#fff"))
    m.append(rect(90, -210, 90, 80, "#ffe066", rx=40, stroke="#8d5524", stroke_width=8))
    m.append(trait(135, -210, 135, -130, "#8d5524", 5))
    m.append(chemin("M -80 0 L -80 -130 Q -80 -200 0 -200 Q 80 -200 80 0 Z", "#3b2412" if ouverte else "#a0522d"))
    if ouverte:
        m.append(chemin("M -80 0 L -80 -130 Q -80 -200 0 -200 Q 80 -200 80 0 Z", "#ffd8a8", opacity=0.6))
        if dedans:
            m.append(dedans)
        m.append(chemin("M -80 0 L -80 -130 Q -80 -200 -40 -196 L -120 -190 L -130 0 Z", "#a0522d"))
    else:
        for k in (-40, 0, 40):
            m.append(trait(k, -190, k, 0, "#7c4a1e", 4))
        m.append(cercle(50, -90, 9, "#fcc419"))
    return place(m, x, y, s)


def cheminee(x, y, s=1.0):
    m = [rect(-130, -260, 260, 260, "#c92a2a"), rect(-150, -280, 300, 30, "#a61e1e", rx=6),
         rect(-80, -170, 160, 170, "#343a40", rx=10)]
    for bx in (-50, 0, 50):
        m.append(rect(bx - 30, -30, 60, 18, "#8d5524", rx=8))
    m += [chemin("M -60 -24 Q -50 -110 -10 -130 Q -20 -80 10 -70 Q 30 -120 20 -150 Q 70 -100 60 -24 Z", "#ff922b"),
          chemin("M -30 -24 Q -20 -70 0 -80 Q 10 -50 20 -60 Q 40 -40 30 -24 Z", "#ffe066")]
    return place(m, x, y, s)


def salon(S):
    interieur(S, "#ffe8cc", "#c9a27e", 600, papier="#ffd8a8")
    S.add(cheminee(620, 600, 0.9))
    S.add(tapis(360, 700, 240, 50, "#ffc9c9", "#ff8787"))
    S.add(etagere(170, 200, 220, objets=g([sac(120, 196, 0.45, plein=True), sac(170, 196, 0.45), tas_grains(230, 196, 0.5)])))


def couverture():
    S = Scene()
    ete(S)
    S.add(maison_fourmi(620, 700, 0.8))
    S.add(cigale(300, 740, 1.6, expr="chante", **avec_violon()))
    S.add(notes(170, 330, 1.2), notes(420, 280, 1.0))
    S.add(fourmi(560, 740, 1.15, expr="concentre", bras="tete", objet=grain(0, -230, 2.6)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(violon(200, 150, 2.2, rot=-30), archet(250, 140, 1.8, rot=40))
    return S


def p01():
    S = Scene()
    ete(S)
    S.add(cigale(400, 740, 1.8, expr="chante", **avec_violon()))
    S.add(notes(220, 300, 1.3), notes(600, 250, 1.1), notes(560, 400, 0.9))
    S.add(texte(210, 190, "Cri-cri !", 56, "#5c940d", contour="#fff", rot=-8))
    return S


def p02():
    S = Scene()
    ete(S)
    S.add(maison_fourmi(620, 700, 0.8))
    S.add(fourmi(330, 740, 1.4, expr="concentre", bras="tete", objet=grain(0, -230, 2.6)))
    for k, gx in enumerate((110, 160, 210)):
        S.add(grain(gx, 700 - k * 6, 1.6))
    S.add(mouvement(210, 580, 1.0))
    return S


def p03():
    S = Scene()
    ete(S)
    S.add(cigale(230, 740, 1.45, expr="rire", bras="salut"))
    S.add(fourmi(590, 740, 1.3, expr="concentre", bras="tete", objet=grain(0, -230, 2.6), regard=(-1, 0)))
    S.add(bulle(220, 130, 330, 90, "Viens chanter !", 36, pointe=(230, 380)))
    S.add(bulle(580, 230, 300, 90, "Pas le temps !", 36, pointe=(580, 360)))
    return S


def p04():
    S = Scene()
    ete(S)
    S.add(grande_feuille(400, 640, 2.6, "#69db7c", "#40c057", rot=-10))
    S.add(cigale(400, 700, 1.55, expr="rire", bras="tete"))
    S.add(bulle(400, 140, 480, 100, "L'hiver ? C'est si loin !", 38, pointe=(400, 330)))
    S.add(notes(620, 380, 1.0))
    return S


def p05():
    S = Scene()
    automne(S)
    S.add(cigale(430, 740, 1.6, expr="inquiet", **avec_violon(regard=(-1, -1))))
    S.add(notes(600, 360, 0.7))
    return S


def p06():
    S = Scene()
    hiver(S)
    S.add(cigale(400, 750, 1.6, expr="triste", bras="calin", larmes=False))
    S.add(texte(620, 300, "Brrr !", 64, "#4263eb", contour="#fff"))
    S.add(rafales(160, 330, 1.0, "#ffffff"))
    return S


def p07():
    S = Scene()
    hiver(S)
    S.add(maison_fourmi(500, 720, 0.95, neige=True))
    S.add(cigale(200, 750, 1.35, expr="inquiet", bras="salut", regard=(1, 0)))
    S.add(texte(360, 380, "Toc, toc !", 50, "#7c4a1e", contour="#fff"))
    return S


def p08():
    S = Scene()
    hiver(S)
    S.add(maison_fourmi(560, 720, 0.95, neige=True, ouverte=True,
                        dedans=fourmi(0, 0, 0.95, expr="neutre", regard=(-1, 0))))
    S.add(cigale(210, 750, 1.35, expr="triste", bras="donne", regard=(1, 0)))
    S.add(bulle(250, 130, 420, 110, "Prête-moi quelques\ngraines, s'il te plaît !", 32, pointe=(220, 420)))
    return S


def p09():
    S = Scene()
    hiver(S)
    S.add(maison_fourmi(560, 720, 0.95, neige=True, ouverte=True,
                        dedans=fourmi(0, 0, 0.95, expr="fache", bras="croises", regard=(-1, 0))))
    S.add(cigale(210, 750, 1.35, expr="timide", bras="bas", regard=(1, 0)))
    S.add(bulle(560, 150, 460, 100, "Que faisais-tu cet été ?", 34, pointe=(560, 360)))
    return S


def p10():
    S = Scene()
    hiver(S)
    S.add(maison_fourmi(560, 720, 0.95, neige=True))
    S.add(cigale(210, 750, 1.35, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(texte(560, 350, "BLAM !", 80, "#c92a2a", contour="#fff"))
    S.add(eclat(560, 560, 1.2, "#fff3bf"))
    return S


def p11():
    S = Scene()
    hiver(S)
    S.add(rect(0, 0, 800, 800, "#1c2a52", opacity=0.18))
    S.add(cigale(400, 750, 1.6, expr="pleure", **avec_violon()))
    S.add(notes(560, 360, 0.8, "#5c7cfa"), notes(240, 320, 0.7, "#5c7cfa"))
    return S


def p12():
    S = Scene()
    salon(S)
    S.add(porte(170, 620, 150, 330, "#a0522d"))
    S.add(fourmi(420, 720, 1.4, expr="inquiet", bras="pense", regard=(-1, -1)))
    S.add(notes(240, 360, 0.9, "#5c7cfa"), notes(110, 260, 0.7, "#5c7cfa"))
    return S


def p13():
    S = Scene()
    hiver(S)
    S.add(maison_fourmi(560, 720, 0.95, neige=True, ouverte=True,
                        dedans=fourmi(0, 0, 0.95, expr="content", bras="ouverts", regard=(-1, 0))))
    S.add(cigale(210, 750, 1.35, expr="surpris", bras="joues", regard=(1, 0)))
    S.add(bulle(520, 140, 440, 110, "Entre ! Il y en a\nassez pour deux.", 34, pointe=(560, 370)))
    return S


def p14():
    S = Scene()
    salon(S)
    S.add(cigale(260, 740, 1.4, expr="chante", **avec_violon()))
    S.add(fourmi(480, 740, 1.2, expr="rire", bras="haut", pieds_haut=True))
    S.add(notes(380, 330, 1.0), notes(150, 300, 0.8))
    return S


def p15():
    S = Scene()
    ete(S)
    S.add(maison_fourmi(660, 700, 0.7))
    S.add(cigale(260, 740, 1.35, expr="chante", bras="tete", objet=grain(0, -230, 2.6)))
    S.add(fourmi(470, 740, 1.2, expr="rire", bras="tete", objet=grain(0, -230, 2.6)))
    S.add(notes(360, 300, 1.0), notes(140, 330, 0.8))
    S.add(fleur(560, 740, 0.9, "#cc5de8"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("violon-seul.svg", vignette),
    ("01-tout-l-ete.svg", p01), ("02-la-fourmi.svg", p02), ("03-pas-le-temps.svg", p03),
    ("04-si-loin.svg", p04), ("05-l-automne.svg", p05), ("06-la-bise.svg", p06),
    ("07-toc-toc.svg", p07), ("08-prete-moi.svg", p08), ("09-que-faisais-tu.svg", p09),
    ("10-blam.svg", p10), ("11-chanson-triste.svg", p11), ("12-la-fourmi-ecoute.svg", p12),
    ("13-entre.svg", p13), ("14-l-hiver-en-musique.svg", p14), ("15-le-printemps.svg", p15),
]
