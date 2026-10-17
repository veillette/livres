"""Le poisson d'avril de Mathis — la blague qui fait rire, et celle qui fait pleurer.

Le 1er avril, Mathis le chat colle un poisson de papier dans le dos de
Papa : toute la famille rit. À l'école, il fait croire à son ami Jules que
la sortie à la ferme est annulée ; Jules pleure, les autres se moquent, et
Mathis comprend qu'une blague n'est drôle que si tout le monde rit, même
celui qu'on attrape. Il demande pardon, puis tous deux cachent des poissons
dans la classe pour Madame Chouette, qui leur répond par un poisson d'avril.
Le 1er avril est le décor ; l'histoire parle d'empathie.

Plans : 1 moyen (les ciseaux) · 2 moyen (dans le dos) · 3 gros plan (tu m'as
eu !) · 4 large (la cour) · 5 moyen (la blague) · 6 gros plan (les larmes) ·
7 moyen (il l'a cru) · 8 gros plan (pas drôle) · 9 moyen (pardon) · 10 moyen
(le plan) · 11 large (des poissons partout) · 12 moyen (pas de devoirs).
"""
from base import *
from base import _assombrir
from objets import tasse

ID = "poisson-avril"
PAPIER_PEINT = "rayures"

COULEURS = ("#4dabf7", "#ffd43b", "#ff922b", "#69db7c", "#f783ac", "#9775fa")

MATHIS = dict(couleur="#ff922b", habit="#1098ad", motif="rayures", couleur_motif="#99e9f2")
JULES = dict(couleur="#e3b57a", habit="#fab005")
PAPA = dict(couleur="#e8590c", habit="#495057", acc=("lunettes",))
MAMAN = dict(couleur="#ffc078", habit="#e64980")
CAMARADES = (("herisson", dict(habit="#2f9e44")), ("souris", dict(habit="#ae3ec9")), ("castor", dict(habit="#f08c00")),
             ("cochon", dict(habit="#4dabf7")), ("lapin", dict(habit="#ff6b6b")), ("ecureuil", dict(habit="#20c997")))


def poisson_papier(x, y, s=1.0, c="#4dabf7", rot=0, scotch=True):
    """Poisson découpé dans du papier de couleur ; (x, y) = centre."""
    f = _assombrir(c, 0.8)
    m = [chemin("M -40 0 Q -10 -26 24 -8 L 44 -22 L 40 0 L 44 22 L 24 8 Q -10 26 -40 0 Z", c),
         chemin("M -6 -14 Q 2 0 -6 14 M 8 -12 Q 16 0 8 12", stroke=f, sw=2.5),
         cercle(-26, -4, 4, "#fff"), cercle(-27, -4, 2, ENCRE)]
    if scotch:
        m.append(rect(-8, -32, 16, 22, "#fff", opacity=0.6, transform="rotate(12)"))
    return place(m, x, y, s, rot=rot)


def mathis(x, y, s=1.15, **k):
    return perso("chat", x, y, s, **{**MATHIS, **k})


def jules(x, y, s=1.15, **k):
    return perso("chien", x, y, s, **{**JULES, **k})


def papa(x, y, s=1.55, **k):
    return perso("chat", x, y, s, **{**PAPA, **k})


def maman(x, y, s=1.5, **k):
    return perso("chat", x, y, s, **{**MAMAN, **k})


def camarade(i, x, y, s=0.95, **k):
    espece, d = CAMARADES[i % len(CAMARADES)]
    return perso(espece, x, y, s, **{**d, **k})


def chouette_maitresse(x, y, s=1.5, **k):
    k.setdefault("acc", ("lunettes",))
    return chouette(x, y, s, couleur="#a9805b", **k)


def cuisine(S, y=600):
    piece(S, "cuisine", y)
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#15aabf",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), rect(0, 200, 800, 200, "#8ce99a"), arbre(640, 230, 0.35)])))


def ecole_dehors(S, sol_y=600):
    """La cour au printemps : mur de briques, arbres en fleurs, marelle."""
    ciel(S, "#74c0fc", "#e7f5ff")
    S.add(rect(0, 300, 800, 240, "#e9a66b"), briques(0, 300, 800, 240, "#e9a66b"))
    for fx in (80, 330, 580):
        S.add(fenetre(fx, 340, 140, 110, "#a5d8ff"))
    sol(S, sol_y, "#ced4da", bosse=0, premier=False)
    S.add(arbre(740, sol_y, 1.0, feuillage="#fcc2d7", feuillage2="#f783ac"))
    for k in range(4):
        S.add(rect(200 + k * 70, 690, 64, 54, "none", stroke="#fff", stroke_width=4))
        S.add(texte(232 + k * 70, 728, str(k + 1), 28, "#fff"))


def classe(S, y=600):
    interieur(S, "#fff9db", "#d9a066", y, plinthe="#c68642")
    S.add(rect(220, 80, 360, 220, "#8d5524", rx=8), rect(232, 92, 336, 196, "#2b8a3e", rx=4))
    S.add(texte(400, 170, "1er avril", 44, "#f8f9fa", police="Andika, sans-serif", poids=400))
    S.add(horloge(680, 140, 44, heure=9, minute=0))
    S.add(fenetre(30, 110, 140, 150, "#a5d8ff"))


def banc(x, y, s=1.0):
    return place([rect(-120, -60, 240, 18, "#a0693a", rx=4), rect(-120, -100, 240, 16, "#a0693a", rx=4),
                  rect(-100, -42, 12, 42, "#495057"), rect(88, -42, 12, 42, "#495057"),
                  rect(-104, -100, 10, 60, "#495057"), rect(94, -100, 10, 60, "#495057")], x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    ecole_dehors(S, 620)
    for k in range(9):
        S.add(poisson_papier(80 + (k * 97) % 660, 120 + (k * 53) % 260, 0.9, COULEURS[k % 6], rot=(k * 37) % 60 - 30, scotch=False))
    S.add(jules(540, 790, 1.4, expr="rire", bras="ouverts", regard=(-1, 0),
                derriere=poisson_papier(-76, -110, 1.0, "#ff922b", rot=20)))
    S.add(mathis(280, 790, 1.45, expr="malin", bras="hanches", regard=(1, 0),
                 derriere=poisson_papier(-80, -70, 1.2, "#4dabf7", rot=-30)))
    S.cachette(60, 780)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(poisson_papier(200, 140, 3.0, "#4dabf7", rot=-8))
    return S


def p01():
    """Plan moyen : à l'aube, Mathis découpe des poissons."""
    S = Scene()
    cuisine(S, 600)
    S.add(mathis(400, 720, 1.25, expr="malin", bras="porte", regard=(0, 1)))
    S.add(table(400, 800, 600, 120, "#c68642", nappe="#e3fafc"))
    for k, c in enumerate(COULEURS[:4]):
        S.add(poisson_papier(200 + k * 120, 662, 0.8, c, rot=(k - 1.5) * 12, scotch=False))
    S.add(cercle(640, 650, 22, "none", stroke="#dee2e6", stroke_width=12), cercle(640, 650, 10, "#adb5bd"))
    S.add(texte(560, 330, "Hé, hé, hé…", 40, "#1098ad", contour="#fff", rot=-6))
    S.cachette(30, 790)
    return S


def p02():
    """Plan moyen : un poisson bleu dans le dos de Papa."""
    S = Scene()
    cuisine(S, 600)
    S.add(rect(420, 560, 380, 40, "#adb5bd"), rect(420, 600, 380, 200, "#e9ecef"))
    S.add(tasse(640, 556, 1.0, "#e03131"))
    S.add(papa(560, 790, 1.5, expr="sourire", bras="porte", regard=(1, 0),
               derriere=poisson_papier(-70, -110, 0.9, "#4dabf7", rot=-20)))
    S.add(mathis(340, 790, 1.1, expr="malin", bras="tend", regard=(1, -0.5), pas="pointe"))
    S.add(maman(130, 790, 1.45, expr="rire", bras="bouche", regard=(1, 0)))
    S.add(texte(320, 320, "Hop !", 50, "#1098ad", contour="#fff", rot=-8))
    S.cachette(30, 790)
    return S


def p03():
    """Gros plan : « Tu m'as bien eu ! »"""
    S = Scene()
    cuisine(S, 600)
    S.add(papa(520, 800, 1.7, expr="rire", bras="tient", flip=True, regard=(-1, 0), objet=poisson_papier(68, -150, 1.1, "#4dabf7")))
    S.add(mathis(240, 800, 1.35, expr="rire", bras="saute", regard=(1, 0)))
    S.camera(1.3, 400, 500)
    S.dessus(texte(400, 110, "POISSON D'AVRIL !", 58, "#1098ad", contour="#fff", rot=-4))
    S.cachette(90, 780)
    return S


def p04():
    """Plan large : la cour d'école pleine de poissons."""
    S = Scene()
    ecole_dehors(S, 600)
    for k, (x, y, s, bras) in enumerate(((110, 700, 0.75, "court"), (260, 680, 0.7, "saute"), (430, 690, 0.72, "rire_"),
                                          (590, 700, 0.75, "court"), (680, 770, 0.8, "haut"))):
        b = "applaudit" if bras == "rire_" else bras
        S.add(camarade(k, x, y, s, expr="rire", bras=b, flip=k % 2 == 1,
                       derriere=poisson_papier(-70 if k % 2 == 0 else 70, -100, 0.7, COULEURS[k % 6], rot=-20)))
    S.add(mathis(330, 790, 0.95, expr="rire", bras="court", regard=(1, 0), derriere=poisson_papier(-60, -60, 0.8, "#69db7c", rot=30)))
    S.add(jules(500, 790, 0.95, expr="rire", bras="coucou", regard=(-1, 0)))
    S.cachette(30, 790)
    return S


def p05():
    """Plan moyen : Mathis chuchote sa blague à Jules."""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(jules(480, 790, 1.3, expr="inquiet", bras="bas", regard=(-1, 0)))
    S.add(mathis(300, 790, 1.3, expr="malin", bras="chut", regard=(1, 0)))
    S.add(bulle(380, 140, 440, 110, "La sortie à la ferme…\nelle est annulée.", 32, pointe=(330, 450)))
    S.add(camarade(1, 680, 720, 0.8, expr="rire", bras="haut"))
    S.cachette(40, 790)
    return S


def p06():
    """Gros plan : les larmes de Jules."""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(jules(400, 800, 1.8, expr="pleure", larmes=True, bras="bas", regard=(0, 1)))
    S.camera(1.4, 400, 500)
    S.dessus(bulle(400, 100, 500, 100, "Je voulais tellement voir\nles petits agneaux…", 30, pointe=S.vers_page(400, 430)))
    S.cachette(110, 790)
    return S


def p07():
    """Plan moyen : « Il l'a cru ! » ; Jules s'en va en pleurant."""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(mathis(220, 790, 1.2, expr="rire", bras="designe", regard=(1, 0)))
    S.add(camarade(0, 90, 760, 0.95, expr="rire", bras="designe", regard=(1, 0)))
    S.add(camarade(4, 360, 760, 0.95, expr="rire", bras="bouche", regard=(1, 0)))
    S.add(jules(600, 790, 1.15, expr="pleure", larmes=True, bras="bas", regard=(1, 0), pas="marche"))
    S.add(bulle(250, 140, 380, 90, "POISSON D'AVRIL !", 34, pointe=(230, 450)))
    S.add(bulle(560, 330, 240, 70, "Il l'a cru !", 28, pointe=(380, 500)))
    S.cachette(770, 790)
    return S


def p08():
    """Gros plan : Mathis ne rit plus."""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(jules(700, 640, 0.6, expr="pleure", bras="bas", regard=(1, 0)))
    S.add(mathis(360, 800, 1.7, expr="triste", bras="tient", regard=(1, 0.3), objet=poisson_papier(68, -130, 0.8, "#69db7c", rot=80, scotch=False)))
    S.camera(1.35, 420, 520)
    S.cachette(110, 790)
    return S


def p09():
    """Plan moyen : près du banc, « Pardon, Jules. »"""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(banc(420, 720, 1.4))
    S.add(jules(500, 790, 1.15, expr="triste", bras="bas", regard=(-1, 0)))
    S.add(mathis(290, 790, 1.15, expr="inquiet", bras="tend", regard=(1, 0)))
    S.add(bulle(300, 140, 440, 110, "Pardon, Jules. C'était\nune mauvaise blague.", 30, pointe=(300, 450)))
    S.cachette(40, 790)
    return S


def p10():
    """Plan moyen : tête contre tête, le plan de la bonne blague."""
    S = Scene()
    ecole_dehors(S, 620)
    S.add(banc(400, 720, 1.4))
    S.add(mathis(320, 790, 1.25, expr="malin", bras="porte", regard=(1, 0), objet=g([poisson_papier(0, -80, 0.6, c, rot=k * 15) for k, c in enumerate(COULEURS[:3])])))
    S.add(jules(480, 790, 1.25, expr="rire", bras="mains_jointes", regard=(-1, 0)))
    S.add(texte(400, 300, "chuchote, chuchote…", 32, "#1098ad", contour="#fff", rot=-4))
    S.cachette(40, 790)
    return S


def p11():
    """Plan large : la classe pleine de poissons ; Madame Chouette rit."""
    S = Scene()
    classe(S, 580)
    S.add(poisson_papier(680, 100, 0.7, "#ff922b", rot=10), poisson_papier(300, 130, 0.7, "#f783ac", rot=-20),
          poisson_papier(520, 240, 0.7, "#69db7c", rot=14), poisson_papier(100, 200, 0.7, "#ffd43b", rot=30))
    S.add(place([rect(-24, -50, 48, 50, "#e8590c", rx=6), ellipse(0, -90, 40, 50, "#40c057")], 740, 600, 1.0))
    S.add(poisson_papier(740, 500, 0.6, "#4dabf7", rot=-10))
    S.add(chouette_maitresse(400, 640, 1.5, expr="rire", ailes="haut"))
    for k, (x, y) in enumerate(((120, 780), (250, 790), (550, 790), (680, 780))):
        S.add(camarade(k + 1, x, y, 0.85, expr="rire", bras="applaudit"))
    S.add(mathis(330, 800, 0.9, expr="rire", bras="haut"))
    S.add(jules(460, 800, 0.95, expr="rire", bras="saute"))
    S.add(bulle(560, 380, 320, 90, "D'où sortent tous\nces poissons ?", 26, pointe=(450, 500)))
    S.cachette(30, 790)
    return S


def p12():
    """Plan moyen : « Plus jamais de devoirs ! … Poisson d'avril ! »"""
    S = Scene()
    classe(S, 600)
    S.add(chouette_maitresse(400, 680, 1.7, expr="malin", ailes="haut"))
    S.add(poisson_papier(400, 430, 0.8, "#ffd43b", rot=-6))
    for k, (x, y) in enumerate(((110, 790), (250, 800), (550, 800), (690, 790))):
        S.add(camarade(k, x, y, 0.9, expr="rire", bras="applaudit"))
    S.add(mathis(330, 800, 0.95, expr="bouche_bee", bras="joues"))
    S.add(jules(470, 800, 0.95, expr="rire", bras="haut"))
    S.add(bulle(400, 130, 480, 100, "Plus jamais de devoirs !\n… POISSON D'AVRIL !", 32, pointe=(400, 400)))
    S.cachette(110, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("poisson-seul.svg", vignette),
    ("01-les-ciseaux.svg", p01), ("02-dans-le-dos.svg", p02), ("03-tu-m-as-eu.svg", p03),
    ("04-la-cour.svg", p04), ("05-la-blague.svg", p05), ("06-les-larmes.svg", p06),
    ("07-il-l-a-cru.svg", p07), ("08-pas-drole.svg", p08), ("09-pardon.svg", p09),
    ("10-le-plan.svg", p10), ("11-des-poissons-partout.svg", p11), ("12-pas-de-devoirs.svg", p12),
]
