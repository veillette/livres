"""L'orignal du marais — un an avec la famille orignal.

L'orignal est le plus grand cerf du monde (le mâle peut dépasser deux mètres
au garrot). Ses longues pattes l'aident à marcher dans le marais et dans la
neige profonde. L'été, il plonge la tête sous l'eau pour manger des plantes
aquatiques, et il nage très bien. Au printemps naît un veau, souvent deux,
roux et sans taches. Seuls les mâles ont des bois, un large panache : ils
repoussent chaque printemps, couverts de velours, et tombent au début de
l'hiver. Sous la gorge pend la cloche. L'hiver, il broute les rameaux et
l'écorce.

Plans : 1 large (le lac au petit matin) · 2 gros plan (la tête sous l'eau)
· 3 moyen (les jumeaux) · 4 moyen (la baignade des veaux) · 5 gros plan
(les bois de velours) · 6 large (il nage) · 7 schéma (sa taille) · 8 large
(l'automne) · 9 moyen (les bois tombent) · 10 gros plan (les rameaux
d'hiver) · 11 large (le printemps revient).
"""
from base import *
from base import _assombrir
from animaux import etiquette, roseau
from fantastique import personne

ID = "orignal"

BRUN = "#6d4c3a"
BRUN_FONCE = "#3b2a20"
ROUX = "#b5653a"
BOIS = "#d9c4a0"


def panache(sgn=1, taille=1.0, velours=False):
    """Un bois palmé (repère : base sur la tête en (0, 0), vers sgn)."""
    c = "#8d6e4f" if velours else BOIS
    k = taille
    d = (f"M 0 0 Q {sgn * 20 * k} {-10 * k} {sgn * 40 * k} {-20 * k} L {sgn * 50 * k} {-60 * k} L {sgn * 62 * k} {-40 * k} L {sgn * 74 * k} {-78 * k} "
         f"L {sgn * 86 * k} {-52 * k} L {sgn * 100 * k} {-84 * k} L {sgn * 108 * k} {-54 * k} L {sgn * 124 * k} {-70 * k} "
         f"Q {sgn * 120 * k} {-26 * k} {sgn * 70 * k} {-10 * k} Q {sgn * 36 * k} {4 * k} 0 8 Z")
    m = [chemin(d, volume(c, 0.35, 0.75), stroke=_assombrir(c, 0.7), sw=2)]
    if velours:
        m.append(chemin(d, "none", stroke="#a9906f", sw=5, opacity=0.5))
    return g(m)


def orignal(x, y, s=1.0, flip=False, bois=1.0, velours=False, veau=False, tete_basse=False, mange=False, expr="sourire", rot=0):
    """Orignal de profil, tête à droite ; (x, y) = sous les sabots. bois : taille du panache (0 = sans)."""
    c = ROUX if veau else BRUN
    fonce = _assombrir(c, 0.7)
    m = []
    # pattes du fond
    for px in (-70, 60):
        m.append(rect(px - 8, -170, 16, 170, fonce, rx=6))
        m.append(ellipse(px, -2, 12, 6, BRUN_FONCE))
    # corps et bosse du garrot
    m += [chemin("M -110 -170 Q -120 -260 -40 -270 Q 30 -300 80 -260 Q 120 -240 110 -170 Q 60 -140 -20 -150 Q -80 -140 -110 -170 Z", volume(c, 0.3, 0.8)),
          chemin("M -112 -210 Q -126 -200 -118 -186", stroke=fonce, sw=8)]
    # pattes de devant (claires en bas)
    for px in (-50, 80):
        m.append(rect(px - 9, -175, 18, 175, cylindre(c, 0.3, 0.75), rx=7))
        m.append(rect(px - 8, -70, 16, 66, "#c9b29b", rx=6))
        m.append(ellipse(px, -2, 13, 6, BRUN_FONCE))
    # cou et tête
    if tete_basse:
        tete = (150, -110)
        m.append(chemin("M 70 -260 Q 130 -240 160 -140 L 120 -110 Q 90 -180 50 -220 Z", volume(c, 0.3, 0.8)))
    else:
        tete = (150, -290)
        m.append(chemin("M 60 -250 Q 110 -320 150 -320 L 160 -270 Q 120 -250 90 -190 Z", volume(c, 0.3, 0.8)))
    tx, ty = tete
    museau = chemin(f"M {tx - 30} {ty - 20} Q {tx + 20} {ty - 30} {tx + 70} {ty + 10} Q {tx + 80} {ty + 40} {tx + 50} {ty + 46} Q {tx + 10} {ty + 40} {tx - 20} {ty + 20} Z",
                    volume(c, 0.35, 0.8))
    m.append(museau)
    m += [ellipse(tx + 64, ty + 28, 6, 4, BRUN_FONCE), chemin(f"M {tx + 40} {ty + 42} q 10 4 20 0", stroke=BRUN_FONCE, sw=2)]
    if not veau:
        m.append(chemin(f"M {tx + 6} {ty + 40} Q {tx + 4} {ty + 90} {tx - 6} {ty + 96} Q {tx - 14} {ty + 70} {tx - 10} {ty + 34} Z", fonce))   # la cloche
    m.append(ellipse(tx - 20, ty - 28, 10, 20, c, rot=-30))
    m.append(ellipse(tx - 36, ty - 22, 10, 20, fonce, rot=-50))
    yeux = "fermes" if expr == "dort" else ("heureux" if expr == "content" else "normal")
    m.append(oeil(tx + 6, ty - 8, yeux, (1, 0), taille=0.7))
    if bois and not veau:
        m.append(place([panache(-1, bois * 0.9, velours), panache(1, bois, velours)], tx - 24, ty - 34, 1.0, rot=-10 if not tete_basse else 20))
    if mange:
        m.append(place([chemin("M 0 0 q -10 30 -4 60 M 6 0 q 6 30 2 64 M 12 0 q 16 26 14 54", stroke="#69db7c", sw=5)], tx + 56, ty + 40))
    largeur = 220
    return place(m, x, y, s, flip=flip, rot=rot) + occuper(x - 130 * s, y - 400 * s, x + largeur * s, y)


def marais(S, horizon=520, graine=1, haut="#74c0fc", bas="#e7f5ff", brume=False, automne=False, hiver=False):
    ciel(S, haut, bas)
    r = random.Random(graine)
    for k in range(9):
        x = r.uniform(-20, 820)
        if automne and k % 2:
            S.add(arbre(x, horizon, r.uniform(0.5, 0.7), "#fd7e14", "#fab005"))
        else:
            S.add(sapin(x, horizon + r.uniform(-6, 6), r.uniform(0.5, 0.8), "#2b8a3e", "#2f9e44", neige=hiver))
    if hiver:
        S.add(rect(0, horizon, 800, 800 - horizon, lineaire([(0, "#ffffff"), (1, "#dbe4ff")])))
        for x in (64, 736, 150, 650):
            S.proposer_cachette(x, horizon + 200)
        return
    S.add(rect(0, horizon, 800, 30, terrain("#8ce99a")))
    S.add(rect(0, horizon + 20, 800, 800 - horizon - 20, lineaire([(0, "#74c0fc"), (1, "#339af0")])))
    for k in range(6):
        S.add(chemin(f"M {80 + k * 130} {horizon + 80 + (k % 2) * 90} q 20 -8 40 0", stroke="#a5d8ff", sw=4))
    for x in (30, 70, 730, 770):
        S.add(roseau(x, 800, 1.2, 260, rot=-6 if x < 400 else 6))
    if brume:
        S.add(rect(0, horizon - 80, 800, 160, lineaire([(0, "#fff", 0), (0.5, "#fff", 0.6), (1, "#fff", 0)])))


def eau_devant(S, y_ligne, couleur="#4dabf7"):
    S.add(rect(0, y_ligne, 800, 800 - y_ligne, couleur, opacity=0.6))
    S.add(chemin(f"M 0 {y_ligne} " + " ".join("q 15 -6 30 0" for _ in range(27)), stroke="#e7f5ff", sw=3, opacity=0.8))


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    marais(S, 500, graine=2)
    S.add(orignal(320, 760, 1.25, bois=1.1))
    eau_devant(S, 700)
    S.add(orignal(620, 740, 0.6, veau=True, flip=True))
    eau_devant(S, 720)
    S.cachette(70, 780, "poisson")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(orignal(170, 262, 0.62, bois=1.0))
    return S


def p01():
    """Plan large : au petit matin, dans la brume du lac, un grand orignal mâle avance dans le marais."""
    S = Scene()
    marais(S, 520, graine=3, haut="#ffc9c9", bas="#fff4e6", brume=True)
    S.add(orignal(380, 720, 0.95, bois=1.1))
    eau_devant(S, 680)
    S.cachette(70, 780, "poisson")
    return S


def p02():
    """Gros plan : l'orignal relève la tête de l'eau, la bouche pleine de plantes qui dégoulinent."""
    S = Scene()
    marais(S, 460, graine=4)
    S.add(orignal(300, 860, 1.7, bois=1.1, mange=True))
    eau_devant(S, 780)
    for k in range(6):
        S.add(goutte(600 + k * 12, 600 + k * 30, 0.7, "#a5d8ff"))
    S.camera(1.2, 460, 470)
    S.dessus(texte(250, 120, "Slurp !", 64, "#2b8a3e", contour="#fff"))
    S.cachette(70, 780, "poisson")
    return S


def p03():
    """Plan moyen : au printemps, dans l'herbe haute, la maman et ses deux veaux roux."""
    S = Scene()
    paysage(S, 540, 600, "#8ce99a", "#b2f2bb", graine=5)
    S.add(orignal(260, 780, 1.1, bois=0))
    S.add(orignal(520, 790, 0.6, veau=True, flip=True, expr="content"), orignal(640, 790, 0.55, veau=True, flip=True))
    for k in range(10):
        S.add(touffe(40 + k * 80, 800, 2.2, "#40c057", graine=k))
    S.add(texte(400, 140, "Des jumeaux !", 56, ROUX, contour="#fff"))
    return S


def p04():
    """Plan moyen : les veaux suivent leur mère dans l'eau et apprennent à nager."""
    S = Scene()
    marais(S, 480, graine=6)
    S.add(orignal(560, 740, 1.0, bois=0, flip=True))
    S.add(orignal(300, 730, 0.55, veau=True, flip=True, expr="content"), orignal(180, 740, 0.5, veau=True, flip=True))
    eau_devant(S, 650)
    S.add(texte(400, 150, "Plouf ! On nage !", 52, "#1864ab", contour="#fff"))
    S.cachette(70, 780, "poisson")
    return S


def p05():
    """Gros plan : les bois du mâle repoussent, couverts de velours."""
    S = Scene()
    paysage(S, 540, 600, "#8ce99a", "#b2f2bb", graine=7)
    S.add(orignal(260, 900, 1.9, bois=0.8, velours=True))
    S.camera(1.6, 520, 360)
    S.dessus(texte(400, 110, "Des bois tout doux, en velours", 42, ROUX, contour="#fff"))
    S.cachette(726, 422, "air")
    return S


def p06():
    """Plan large : l'orignal traverse le lac à la nage ; seuls la tête et le dos dépassent."""
    S = Scene()
    marais(S, 440, graine=8)
    S.add(orignal(380, 700, 0.9, bois=1.1, rot=-4))
    eau_devant(S, 520)
    S.add(chemin("M 80 540 Q 200 520 300 540", stroke="#fff", sw=4, opacity=0.7))
    S.cachette(70, 780, "poisson")
    return S


def p07():
    """Schéma : l'orignal à côté d'une grande personne : il est bien plus haut !"""
    S = Scene()
    fond(S, "#fff4e6")
    S.add(rect(0, 720, 800, 80, "#e9d8a6"))
    S.add(orignal(280, 720, 1.25, bois=1.1))
    S.add(personne(640, 720, 1.2, stature="adulte", peau="rosee", cheveux="chatain", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7",
                   expr="bouche_bee", bras="bas", regard=(-1, -0.6)))
    S.add(trait(80, 720 - 270 * 1.25, 80, 720, "#e8590c", 5), trait(66, 720 - 270 * 1.25, 94, 720 - 270 * 1.25, "#e8590c", 5), trait(66, 720, 94, 720, "#e8590c", 5))
    S.add(etiquette(80, 720 - 270 * 1.25 - 20, "2 mètres", 30, "#e8590c"))
    S.add(texte(400, 110, "Le plus grand cerf du monde", 44, BRUN, contour="#fff"))
    S.cachette(740, 760)
    return S


def p08():
    """Plan large : l'automne, le mâle aux grands bois appelle ; les feuilles sont rouges et orange."""
    S = Scene()
    marais(S, 520, graine=9, automne=True, haut="#a5d8ff", bas="#fff4e6")
    S.add(orignal(360, 780, 1.15, bois=1.25))
    eau_devant(S, 740)
    S.add(texte(560, 150, "Ouaaaah !", 52, BRUN, contour="#fff"))
    S.cachette(70, 785, "poisson")
    return S


def p09():
    """Plan moyen : au début de l'hiver, les bois du mâle sont tombés dans la neige."""
    S = Scene()
    marais(S, 540, graine=10, hiver=True, haut="#a5d8ff", bas="#f1f3f5")
    flocons(S, 40, 3, (0, 0, 800, 540))
    S.add(orignal(320, 780, 1.1, bois=0, expr="surpris"))
    S.add(place(panache(1, 1.0), 600, 760, 1.2, rot=20), place(panache(-1, 0.9), 700, 780, 1.2, rot=-10))
    S.add(bulle(600, 300, 300, 90, "Mes bois !", 38, pointe=(560, 420)))
    return S


def p10():
    """Gros plan : l'hiver, dans la neige profonde, l'orignal broute les rameaux d'un arbuste."""
    S = Scene()
    marais(S, 520, graine=11, hiver=True, haut="#a5d8ff", bas="#f1f3f5")
    S.add(orignal(280, 800, 1.5, bois=0))
    S.add(rect(0, 700, 800, 100, "#fff"))
    for k in range(6):
        S.add(chemin(f"M {560 + k * 20} 800 Q {580 + k * 30} 600 {600 + k * 40} 480", stroke="#8d5524", sw=6))
    S.camera(1.25, 470, 470)
    S.dessus(texte(400, 110, "Crunch ! Des rameaux pour l'hiver", 40, BRUN, contour="#fff"))
    return S


def p11():
    """Plan large : au printemps, la maman et son veau d'un an ; les bois du mâle repoussent déjà."""
    S = Scene()
    paysage(S, 540, 600, "#8ce99a", "#b2f2bb", graine=12)
    S.add(orignal(170, 760, 0.8, bois=0.4, velours=True))
    S.add(orignal(560, 780, 0.95, bois=0, flip=True))
    S.add(orignal(420, 790, 0.7, veau=True, flip=True, expr="content"))
    S.add(texte(400, 140, "Et tout recommence…", 50, "#2b8a3e", contour="#fff"))
    S.cachette(730, 220, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("orignal-seul.svg", vignette),
    ("01-le-lac.svg", p01), ("02-slurp.svg", p02), ("03-les-jumeaux.svg", p03),
    ("04-on-nage.svg", p04), ("05-le-velours.svg", p05), ("06-il-nage.svg", p06),
    ("07-sa-taille.svg", p07), ("08-l-automne.svg", p08), ("09-les-bois-tombent.svg", p09),
    ("10-les-rameaux.svg", p10), ("11-le-printemps.svg", p11),
]
