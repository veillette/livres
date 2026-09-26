"""L'étoile tombée du ciel — aider quelqu'un jusqu'au bout."""
from base import *
from objets import *
from fantastique import *

ID = "etoile-tombee"
NORA = dict(coiffure="tresses", cheveux="chatain", peau="doree", habit="#91a7ff", motif_robe="#fff3bf")


def nora(x, y, s=1.0, **k):
    return personne(x, y, s, **{**NORA, **k})


def jardin_nuit(S, chateau_=True, arbre_=False):
    nuit(S, "#141e46", "#3b5bdb")
    etoiles(S, 45, graine=21, zone=(0, 0, 800, 480))
    if chateau_:
        S.add(chateau(640, 600, 0.5, nuit_=True, mur="#bac8ff", mur2="#91a7ff", toit="#5f3dc4"))
    if arbre_:
        S.add(arbre(170, 640, 1.9, "#2b8a3e", "#2f9e44", tronc="#5c3a1e"))
    sol(S, 600, "#2f9e44", couleur2="#2b8a3e", y2=700)
    for x in (80, 420, 720):
        S.add(fleur(x, 760, 0.8, "#b197fc"))


def couverture():
    S = Scene()
    jardin_nuit(S)
    S.add(nora(280, 760, 1.6, expr="rire", bras="haut"))
    S.add(etoile_perso(480, 400, 70, expr="rire"))
    S.add(lune(170, 330, 40))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(etoile_perso(200, 135, 80, expr="content"))
    return S


def p01():
    S = Scene()
    interieur(S, "#dbe4ff", "#a5b4fc", 600, papier="#bac8ff")
    S.add(fenetre(420, 110, 260, 240, "#1c2a52", cadre="#fff", rideaux="#7048e8",
                  contenu=etoiles_fenetre()))
    S.add(lit(260, 760, 380, couverture="#7048e8"))
    S.add(nora(560, 760, 1.4, expr="content", bras="calin", regard=(0, -1)))
    return S


def etoiles_fenetre():
    m = []
    for x, y, r in [(460, 150, 9), (520, 200, 7), (600, 140, 10), (640, 260, 8), (480, 280, 6), (570, 300, 7)]:
        m.append(etoile5(x, y, r, "#ffe066"))
    m.append(lune(640, 170, 18))
    return "".join(m)


def p02():
    S = Scene()
    jardin_nuit(S)
    S.add(chemin("M 120 80 Q 300 180 380 560", stroke="#fff3bf", sw=10, opacity=0.5))
    S.add(chemin("M 120 80 Q 300 180 380 560", stroke="#fff", sw=3, opacity=0.9))
    S.add(etoile_perso(380, 580, 40, expr="surpris"))
    S.add(eclat(380, 580, 1.4, "#ffe066"))
    S.add(texte(560, 250, "Pouf !", 80, "#ffe066", contour="#1c2a52"))
    return S


def p03():
    S = Scene()
    jardin_nuit(S)
    S.add(nora(240, 770, 1.45, expr="surpris", bras="joues", regard=(1, 1)))
    S.add(etoile_perso(500, 680, 55, expr="pleure", larmes=True))
    S.add(bulle(520, 170, 420, 110, "Je suis tombée.\nJe veux rentrer !", 38, pointe=(510, 590)))
    return S


def p04():
    S = Scene()
    jardin_nuit(S)
    S.add(cercle(400, 420, 190, "#fff3bf", opacity=0.12))
    S.add(nora(400, 780, 1.7, expr="content", bras="porte", regard=(0, 1),
               objet=etoile_perso(0, -58, 34, expr="sourire", halo=False)))
    return S


def p05():
    S = Scene()
    jardin_nuit(S, chateau_=False)
    S.add(echelle(430, 740, 1.0, h=520, rot=6))
    S.add(nora(470, 330, 1.2, expr="concentre", bras="haut", regard=(0, -1)))
    S.add(etoile_perso(560, 170, 34, expr="inquiet"))
    S.add(texte(200, 170, "Trop haut !", 56, "#ffe066", contour="#1c2a52"))
    return S


def p06():
    S = Scene()
    jardin_nuit(S)
    S.add(cerf_volant(470, 470, 0.9, rot=40, fil_vers=(310, 620)))
    S.add(etoile_perso(500, 420, 30, expr="oups"))
    S.add(nora(250, 770, 1.4, expr="oups", bras="tient"))
    S.add(mouvement(560, 380, 1.0, rot=-110))
    return S


def p07():
    S = Scene()
    jardin_nuit(S, chateau_=False, arbre_=True)
    S.add(ballon_air(230, 300, 1.3, "#fa5252", fil=120))
    S.add(etoile_perso(230, 420, 26, expr="inquiet", halo=False))
    S.add(nora(520, 770, 1.45, expr="triste", bras="bas", regard=(-1, -1)))
    return S


def p08():
    S = Scene()
    jardin_nuit(S)
    S.add(nora(380, 780, 1.6, expr="triste", bras="porte", regard=(0, 1),
               objet=etoile_perso(0, -58, 34, expr="dort", halo=False, eteinte=True)))
    S.add(bulle(420, 150, 460, 100, "Loin du ciel,\nje m'éteins…", 38))
    return S


def p09():
    S = Scene()
    jardin_nuit(S, chateau_=False, arbre_=True)
    S.add(chouette(230, 330, 1.0, expr="sourire", regard=(1, 0.5)))
    S.add(nora(560, 780, 1.4, expr="surpris", bras="porte", regard=(-1, -1),
               objet=etoile_perso(0, -58, 30, expr="dort", halo=False, eteinte=True)))
    S.add(bulle(520, 150, 460, 110, "Hou hou ! Demande donc\nà la Lune !", 34, pointe=(310, 270)))
    return S


def p10():
    S = Scene()
    nuit(S, "#141e46", "#364fc7")
    etoiles(S, 40, graine=33, zone=(0, 0, 800, 520))
    S.add(lune(400, 280, 170, visage=True))
    S.add(chemin("M -40 800 Q 400 520 840 800 Z", "#2b8a3e"))
    S.add(nora(400, 740, 1.2, expr="bouche_bee", bras="porte", regard=(0, -1),
               objet=etoile_perso(0, -58, 30, expr="dort", halo=False, eteinte=True)))
    return S


def p11():
    S = Scene()
    nuit(S, "#141e46", "#364fc7")
    etoiles(S, 40, graine=33, zone=(0, 0, 800, 520))
    S.add(lune(560, 170, 110, visage=True))
    S.add(poly([(500, 250), (620, 250), (440, 700), (330, 700)], "#e7f5ff", opacity=0.35))
    S.add(etoile_perso(470, 420, 38, expr="rire"))
    S.add(chemin("M -40 800 Q 400 560 840 800 Z", "#2b8a3e"))
    S.add(nora(250, 760, 1.2, expr="content", bras="salut", regard=(1, -1)))
    S.add(bulle(210, 240, 300, 90, "Merci, Nora !", 40, pointe=(420, 380)))
    return S


def p12():
    S = Scene()
    nuit(S, "#141e46", "#3b5bdb")
    etoiles(S, 40, graine=8, zone=(0, 0, 800, 380))
    S.add(etoile_perso(400, 120, 50, expr="rire"))
    S.add(etincelles(400, 120, 1.2, "#fff3bf", graine=2))
    sol(S, 640, "#2f9e44")
    S.add(chateau(400, 700, 0.9, nuit_=True, mur="#bac8ff", mur2="#91a7ff", toit="#5f3dc4"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("etoile-seule.svg", vignette),
    ("01-la-fenetre.svg", p01), ("02-pouf.svg", p02), ("03-je-suis-tombee.svg", p03),
    ("04-toute-tiede.svg", p04), ("05-l-echelle.svg", p05), ("06-cerf-volant.svg", p06),
    ("07-le-ballon.svg", p07), ("08-elle-s-eteint.svg", p08), ("09-la-chouette.svg", p09),
    ("10-la-lune.svg", p10), ("11-le-rayon.svg", p11), ("12-bonne-nuit.svg", p12),
]
