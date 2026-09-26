"""La princesse au petit pois — d'après le conte d'Andersen."""
from base import *
from objets import *
from fantastique import *

ID = "princesse-petit-pois"
PRINCESSE = dict(coiffure="tres_longs", cheveux="blond", peau="claire", habit="#a61e4d")
PRINCE = dict(coiffure="courts", cheveux="brun", peau="doree", habit="#1c7ed6", robe=False, jambes="#343a40",
              acc=("couronne",), cape="#c92a2a")
VIEILLE_REINE = dict(habit="#7048e8", cape="#fab005", cheveux="blanc", acc=("lunettes",))
COULEURS_MATELAS = ("#ff8787", "#74c0fc", "#ffd43b", "#69db7c", "#b197fc", "#ffa94d")


def princesse_(x, y, s=1.0, mouillee=False, **k):
    d = {**PRINCESSE, **k}
    if mouillee:
        d["cheveux"] = "#c9a227"
    return personne(x, y, s, **d)


def chambre(S, nuit_=False):
    interieur(S, "#f3f0ff" if not nuit_ else "#5f3dc4", "#b08968" if not nuit_ else "#7c5c3b", 640,
              papier="#e5dbff" if not nuit_ else "#7048e8")
    S.add(fenetre(620, 90, 130, 150, "#a5d8ff" if not nuit_ else "#1c2a52", rideaux="#a61e4d", nuit_=nuit_))


def pile_matelas(x, y, n=20, w=300, h=16, avec_edredons=0, graine=1):
    """Pile de `n` matelas (et d'édredons) ; (x, y) = milieu du bas."""
    r = random.Random(graine)
    m = [rect(x - w / 2 - 20, y - 30, w + 40, 30, "#8d5524", rx=8)]
    yy = y - 30
    for k in range(n):
        c = COULEURS_MATELAS[k % len(COULEURS_MATELAS)]
        dx = r.uniform(-8, 8)
        m.append(rect(x - w / 2 + dx, yy - h, w, h, c, rx=h / 2))
        m.append(trait(x - w / 2 + dx + 14, yy - h / 2, x + w / 2 + dx - 14, yy - h / 2, "#fff", 2, opacity=0.5, stroke_dasharray="6 8"))
        yy -= h - 1
    for k in range(avec_edredons):
        c = eclaircir(COULEURS_MATELAS[(k + 2) % len(COULEURS_MATELAS)], 0.4)
        dx = r.uniform(-10, 10)
        m.append(rect(x - w / 2 - 6 + dx, yy - h * 1.2, w + 12, h * 1.2, c, rx=h * 0.6))
        yy -= h * 1.2 - 2
    return g(m), yy


def petit_pois(x, y, r=12):
    return g([cercle(x, y, r, "#51cf66"), cercle(x - r * 0.3, y - r * 0.3, r * 0.3, "#b2f2bb")])


def couverture():
    S = Scene()
    chambre(S)
    pile, haut = pile_matelas(400, 790, 12, 320, 18, avec_edredons=3)
    S.add(pile)
    S.add(princesse_(400, haut + 4, 1.2, expr="inquiet", bras="joues", acc=("diademe",)))
    S.add(petit_pois(400, 740, 13))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 140, 90, "#d3f9d8"))
    S.add(petit_pois(200, 140, 46))
    return S


def p01():
    S = Scene()
    jardin_chateau(S, "#a5d8ff", "#fff0f6", chateau_s=0.7, chateau_x=560)
    S.add(personne(230, 760, 1.5, expr="triste", bras="pense", **PRINCE))
    S.add(pensee(230, 200, 110, g([personne(200, 250, 0.35, coiffure="longs", cheveux="roux", habit="#4dabf7", acc=("diademe",)),
                                   personne(260, 250, 0.35, coiffure="chignon", cheveux="noir", habit="#51cf66", acc=("diademe",)),
                                   texte(230, 170, "?", 40, "#a61e4d")]), depuis=(240, 460)))
    return S


def p02():
    S = Scene()
    ciel(S, "#343a40", "#868e96")
    S.add(chateau(400, 700, 0.9, nuit_=True, mur="#ced4da", mur2="#adb5bd", toit="#495057"))
    sol(S, 690, "#2b8a3e")
    S.add(nuage_orage(200, 120, 0.9), nuage_orage(600, 90, 0.8))
    pluie(S, 90, graine=4, zone=(0, 120, 800, 800), couleur="#a5d8ff")
    S.add(texte(400, 300, "BOUM !", 90, "#ffd43b", contour="#343a40", rot=-8))
    return S


def p03():
    S = Scene()
    ciel(S, "#495057", "#868e96")
    S.add(rect(0, 0, 800, 640, "#adb5bd"))
    for k in range(6):
        for j in range(5):
            S.add(rect(k * 140 + (j % 2) * 70 - 30, j * 130, 130, 120, "#ced4da", rx=6))
    S.add(porte(560, 660, 220, 420, "#8d5524"))
    S.add(rect(0, 640, 800, 160, "#495057"))
    pluie(S, 80, graine=9, zone=(0, 0, 800, 800), couleur="#d0ebff")
    S.add(princesse_(260, 780, 1.5, mouillee=True, expr="triste", bras="montre", regard=(1, 0), habit="#862e9c"))
    S.add(texte(560, 160, "Toc, toc, toc !", 56, "#fff", contour="#343a40"))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff3bf", "#b08968", 640, papier="#ffe066")
    S.add(flaque(300, 790, 1.8))
    S.add(princesse_(300, 780, 1.6, mouillee=True, expr="timide", bras="bas", habit="#862e9c"))
    for gx, gy in [(230, 450), (380, 420), (250, 620), (360, 600)]:
        S.add(goutte(gx, gy, 1.2, "#74c0fc"))
    S.add(personne(600, 780, 1.3, expr="surpris", **PRINCE))
    S.add(bulle(400, 130, 440, 110, "Je suis une princesse.\nJe me suis perdue.", 34, pointe=(320, 300)))
    return S


def p05():
    S = Scene()
    interieur(S, "#fff3bf", "#b08968", 640, papier="#ffe066")
    S.add(reine(400, 780, 1.7, expr="malin", bras="pense", **VIEILLE_REINE))
    S.add(bulle(400, 110, 420, 100, "Une vraie princesse ?", 38, pointe=(360, 250)))
    return S


def p06():
    S = Scene()
    chambre(S)
    S.add(lit(400, 790, 420, couverture="#e599f7"))
    S.add(petit_pois(420, 680, 14))
    S.add(eclat(420, 680, 1.1, "#51cf66"))
    S.add(reine(170, 780, 1.3, expr="malin", bras="donne", **VIEILLE_REINE))
    return S


def p07():
    S = Scene()
    chambre(S)
    pile, haut = pile_matelas(430, 790, 20, 320, 22)
    S.add(pile)
    S.add(petit_pois(430, 757, 11))
    S.add(reine(120, 780, 1.1, expr="rire", bras="ouverts", **VIEILLE_REINE))
    S.add(texte(160, 230, "… dix-neuf,", 44, "#7048e8", contour="#fff"), texte(160, 290, "vingt !", 60, "#7048e8", contour="#fff"))
    return S


def p08():
    S = Scene()
    chambre(S)
    pile, haut = pile_matelas(430, 790, 18, 320, 20, avec_edredons=6)
    S.add(pile)
    S.add(reine(120, 780, 1.1, expr="content", bras="porte", objet=rect(-40, -100, 80, 40, "#fff3bf", rx=16), **VIEILLE_REINE))
    S.add(texte(170, 230, "Et vingt", 50, "#7048e8", contour="#fff"), texte(170, 290, "édredons !", 50, "#7048e8", contour="#fff"))
    return S


def p09():
    S = Scene()
    chambre(S, nuit_=True)
    pile, haut = pile_matelas(460, 790, 18, 300, 20, avec_edredons=5)
    S.add(pile)
    S.add(echelle(260, 790, 1.0, h=520, rot=12))
    S.add(princesse_(460, haut + 4, 1.15, expr="content", bras="salut", acc=("bonnet_nuit",), couleur_acc="#b197fc", habit="#e599f7"))
    S.add(bulle(250, 150, 320, 90, "Bonne nuit !", 44, pointe=(400, 220)))
    return S


def p10():
    S = Scene()
    chambre(S, nuit_=True)
    pile, haut = pile_matelas(420, 790, 18, 320, 20, avec_edredons=5)
    S.add(pile)
    S.add(princesse_(420, haut + 4, 1.15, expr="fache", bras="tete", acc=("bonnet_nuit",), couleur_acc="#b197fc", habit="#e599f7", rot=-12))
    S.add(mouvement(290, haut - 150, 1.2), mouvement(560, haut - 120, 1.2, rot=180))
    S.add(petit_pois(420, 750, 11))
    S.add(texte(170, 470, "Aïe !", 56, "#fff3bf", contour="#5f3dc4"), texte(660, 520, "Ouille !", 50, "#fff3bf", contour="#5f3dc4"))
    return S


def p11():
    S = Scene()
    interieur(S, "#fff3bf", "#b08968", 640, papier="#ffe066")
    S.add(soleil(680, 130, 50))
    S.add(reine(210, 780, 1.4, expr="surpris", bras="joues", **VIEILLE_REINE))
    S.add(princesse_(560, 780, 1.45, expr="fache", bras="hanches", acc=("bonnet_nuit",), couleur_acc="#b197fc", habit="#e599f7"))
    for bx, by in [(520, 580), (610, 640), (560, 700)]:
        S.add(cercle(bx, by, 12, "#748ffc", opacity=0.8))
    S.add(bulle(400, 150, 520, 110, "Très mal ! Il y avait quelque\nchose de dur dans le lit !", 32, pointe=(540, 390)))
    return S


def p12():
    S = Scene()
    jardin_chateau(S, "#ffdeeb", "#fff0f6", chateau_s=0.55, chateau_x=330)
    S.add(personne(160, 770, 1.35, expr="rire", bras="haut", **PRINCE))
    S.add(princesse_(360, 770, 1.35, expr="rire", bras="haut", acc=("diademe",)))
    S.add(rect(560, 600, 150, 170, "#e7f5ff", stroke="#adb5bd", stroke_width=6, opacity=0.9))
    S.add(rect(540, 770, 190, 30, "#c68642", rx=6))
    S.add(petit_pois(635, 700, 14), eclat(635, 700, 1.0, "#51cf66"))
    S.add(rect(555, 548, 160, 40, "#fff", rx=10, stroke="#adb5bd", stroke_width=3))
    S.add(texte(635, 576, "Le petit pois", 24, "#495057"))
    S.add(coeur(280, 360, 1.6), coeur(340, 300, 1.0, "#e64980"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("petit-pois-seul.svg", vignette),
    ("01-le-prince.svg", p01), ("02-l-orage.svg", p02), ("03-toc-toc.svg", p03),
    ("04-trempee.svg", p04), ("05-la-reine.svg", p05), ("06-un-petit-pois.svg", p06),
    ("07-vingt-matelas.svg", p07), ("08-vingt-edredons.svg", p08), ("09-bonne-nuit.svg", p09),
    ("10-aie-ouille.svg", p10), ("11-tres-mal.svg", p11), ("12-le-musee.svg", p12),
]
