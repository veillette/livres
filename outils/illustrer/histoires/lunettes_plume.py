"""Les lunettes de Plume — porter des lunettes pour la première fois.

Plume voit flou de loin. La docteure Ourse lui prescrit des lunettes rouges ;
elle a peur qu'on se moque d'elle, mais Tom les trouve formidables, et c'est
grâce à elles que Plume retrouve le ballon coincé dans l'arbre.
Les scènes « vues par Plume » sans lunettes utilisent un flou gaussien.
"""
from base import *
from objets import *

ID = "lunettes-plume"
ROUGE = "#e03131"


def lunettes_rouges(x, y, s=1.0, flip=False, rot=0):
    """Lunettes rouges à superposer à perso(…) placé aux mêmes x, y, s."""
    m = [cercle(-19, -152, 16, "#e7f5ff", opacity=0.25), cercle(19, -152, 16, "#e7f5ff", opacity=0.25),
         cercle(-19, -152, 16, "none", stroke=ROUGE, stroke_width=5), cercle(19, -152, 16, "none", stroke=ROUGE, stroke_width=5),
         trait(-4, -152, 4, -152, ROUGE, 4), trait(-35, -154, -50, -160, ROUGE, 4), trait(35, -154, 50, -160, ROUGE, 4)]
    return place(m, x, y, s, flip=flip, rot=rot)


def plume(x, y, s=1.0, lunettes=False, **k):
    corps = perso("chat", x, y, s, **{**dict(habit="#4dabf7", motif="pois", couleur_motif="#d0ebff"), **k})
    if not lunettes:
        return corps
    return g([corps, lunettes_rouges(x, y, s, flip=k.get("flip", False), rot=k.get("rot", 0))])


def tom(x, y, s=0.95, **k):
    return perso("lapin", x, y, s, **{**dict(habit="#69db7c"), **k})


def maman(x, y, s=1.2, **k):
    return perso("chat", x, y, s, **{**dict(habit="#f783ac", couleur="#ffc078"), **k})


def docteure(x, y, s=1.25, **k):
    return perso("ours", x, y, s, **{**dict(habit="#ffffff", acc=("lunettes",)), **k})


def flou(S, contenu, force=6):
    fid = uid("f")
    S.defs.append(el("filter", el("feGaussianBlur", stdDeviation=force), id=fid, x="-20%", y="-20%", width="140%", height="140%"))
    return g(contenu, filter=f"url(#{fid})")


def oiseau_branche(S, net=True):
    scene = [chemin("M 380 250 Q 560 230 800 260 L 800 280 Q 560 252 380 270 Z", "#8d5524"),
             grande_feuille(450, 252, 0.5, rot=-30), grande_feuille(720, 262, 0.5, rot=20),
             oiseau(520, 250, 0.5, "#4dabf7"), oiseau(640, 250, 0.5, "#ff922b", flip=True)]
    return g(scene) if net else flou(S, scene, 7)


def jardin(S, y=640, graine=1):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(160, 100, 0.55))
    collines(S, y - 40, "#b2f2bb", graine=graine)
    sol(S, y, "#8ce99a")


def grand_arbre(x, y, s=1.0, ballon=False):
    m = [rect(-30, -330, 60, 330, "#8d5524", rx=12),
         cercle(0, -400, 150, "#51cf66"), cercle(-120, -330, 90, "#40c057"), cercle(120, -330, 90, "#40c057")]
    if ballon:
        m.append(ballon_jeu(70, -380, 34, "#fa5252", "#ffd43b"))
    return place(m, x, y, s)


def tableau_lettres(x, y):
    """Tableau de la docteure : des images de plus en plus petites."""
    m = [rect(x - 120, y - 170, 240, 340, "#fff", rx=10, stroke="#adb5bd", stroke_width=4)]
    m.append(maison(x, y - 80, 0.4))
    m.append(pomme(x - 40, y + 10, 0.8))
    m.append(etoile5(x + 40, y + 10, 18, "#fab005"))
    m += [coeur(x - 50, y + 80, 0.6, "#fa5252"), cercle(x, y + 80, 10, "#4dabf7"), etoile5(x + 50, y + 80, 9, "#fab005")]
    m += [cercle(x - 40 + k * 20, y + 130, 4, ENCRE) for k in range(5)]
    return g(m)


def cabinet(S):
    interieur(S, "#e3fafc", "#c5f6fa", 600, plinthe="#99e9f2")
    S.add(cadre_mur(560, 120, 120, 90, "#d0ebff"))


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    jardin(S, 640, 2)
    S.add(grand_arbre(620, 700, 0.9))
    S.add(coccinelle(330, 430, 1.4), papillon(520, 360, 0.9))
    S.add(plume(320, 790, 1.5, lunettes=True, expr="rire", bras="ouverts"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(plume(200, 264, 1.0, lunettes=True, expr="content", bras="salut"))
    return S


def p01():
    S = Scene()
    jardin(S, 640, 1)
    S.add(oiseau_branche(S, net=False))
    S.add(plume(220, 790, 1.3, expr="concentre", bras="bas", regard=(1, -1)))
    S.add(texte(560, 460, "Flou, flou, flou…", 48, "#1971c2", contour="#fff"))
    return S


def p02():
    S = Scene()
    cabinet(S)
    S.add(tableau_lettres(620, 330))
    S.add(docteure(420, 790, 1.15, expr="sourire", bras="montre", regard=(1, -1)))
    S.add(plume(150, 790, 1.0, expr="inquiet", regard=(1, -1)))
    S.add(bulle(220, 160, 300, 90, "Une… pomme ?", 38, pointe=(170, 520)))
    return S


def p03():
    S = Scene()
    cabinet(S)
    S.add(table(400, 760, 340, 120, "#c68642"))
    S.add(rect(300, 600, 200, 30, "#495057", rx=12), g([cercle(360, 590, 30, "none", stroke=ROUGE, stroke_width=8),
                                                          cercle(440, 590, 30, "none", stroke=ROUGE, stroke_width=8), trait(390, 590, 410, 590, ROUGE, 6)]))
    S.add(plume(160, 790, 1.15, expr="triste", bras="joues"))
    S.add(pensee(560, 230, 130, g([perso("lapin", 520, 300, 0.4, expr="rire", bras="bas"),
                                   perso("souris", 610, 300, 0.35, expr="rire")]), depuis=(250, 520)))
    S.add(texte(560, 120, "Ha ha ha ?", 40, "#868e96", contour="#fff"))
    return S


def p04():
    S = Scene()
    jardin(S, 640, 3)
    S.add(oiseau_branche(S, net=True))
    S.add(coccinelle(560, 470, 1.3), g([perso("fourmi", 660 + k * 40, 660, 0.15) for k in range(3)]))
    S.add(plume(220, 790, 1.3, lunettes=True, expr="bouche_bee", bras="ouverts", regard=(1, -1)))
    S.add(paillettes(420, 380, 1.0, "#fab005"))
    S.add(texte(560, 430, "Tout est net !", 52, "#1971c2", contour="#fff"))
    return S


def p05():
    S = Scene()
    jardin(S, 620, 4)
    S.add(barriere(400, 640, 1.0, largeur=800))
    S.add(tom(560, 790, 1.1, expr="surpris", bras="montre", flip=True))
    S.add(plume(230, 790, 1.15, lunettes=True, expr="timide", bras="joues"))
    S.add(bulle(560, 200, 400, 90, "Tu as des lunettes !", 40, pointe=(560, 520)))
    return S


def p06():
    S = Scene()
    jardin(S, 620, 5)
    S.add(barriere(400, 640, 1.0, largeur=800))
    S.add(tom(540, 790, 1.1, expr="rire", bras="ouverts", flip=True))
    S.add(plume(250, 790, 1.15, lunettes=True, expr="content"))
    S.add(bulle(520, 180, 440, 130, "Elles sont super !\nJe peux voir ?", 40, pointe=(530, 520)))
    S.add(coeur(380, 420, 1.2, "#ff8787"))
    return S


def p07():
    S = Scene()
    jardin(S, 640, 6)
    S.add(grand_arbre(560, 700, 1.0, ballon=True))
    S.add(tom(740, 790, 0.8, expr="inquiet", regard=(-1, 0), flip=True))
    S.add(perso("souris", 380, 790, 0.6, habit="#ff922b", expr="inquiet", regard=(-1, 0)))
    S.add(plume(170, 790, 1.15, lunettes=True, expr="joie", bras="montre", regard=(1, -1)))
    S.add(texte(250, 230, "Là-haut !", 64, ROUGE, contour="#fff"))
    return S


def p08():
    S = Scene()
    interieur(S, "#3b2a7a", "#2b1f5c", y=600)
    S.add(fenetre(80, 80, 180, 170, "#141c3a", nuit_=True))
    S.add(lit(380, 780, 440, "#e5dbff", "#74c0fc"))
    S.add(plume(280, 720, 0.6, expr="dort"))
    S.add(rect(220, 655, 380, 85, "#74c0fc", rx=18))
    S.add(rect(650, 640, 120, 160, "#c68642", rx=6), rect(640, 630, 140, 18, "#a0693a", rx=6))
    S.add(g([cercle(685, 616, 16, "none", stroke=ROUGE, stroke_width=5), cercle(725, 616, 16, "none", stroke=ROUGE, stroke_width=5), trait(700, 616, 710, 616, ROUGE, 4)]))
    S.add(lampe(752, 630, 0.45, allumee=False), zzz(330, 520, 1.0, "#e5dbff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("plume-seule.svg", vignette),
    ("01-flou.svg", p01), ("02-la-docteure.svg", p02), ("03-on-va-se-moquer.svg", p03), ("04-tout-est-net.svg", p04),
    ("05-tu-as-des-lunettes.svg", p05), ("06-elles-sont-super.svg", p06), ("07-la-haut.svg", p07), ("08-bonne-nuit.svg", p08),
]
