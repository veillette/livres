"""Le cerf-volant de papa — la patience, le vent, et une journée à deux.

Pour la fête des pères, Léo a fabriqué un cerf-volant. En haut de la
colline : pas un souffle de vent, plouf ! On pique-nique en attendant. Le
vent se lève, Léo court contre le vent… le cerf-volant tourne et pique du
nez : il lui manque une queue pour rester droit. La cravate de Papa, le
foulard de Léo et une chaussette font l'affaire. Le cerf-volant monte plus
haut que les oiseaux… et se prend dans le grand chêne. Sur les épaules de
Papa, Léo le décroche.

Plans : 1 moyen (le cadeau) · 2 large (plouf) · 3 moyen (le pique-nique) ·
4 large en diagonale (le vent, la vrille) · 5 gros plan (la cravate) ·
6 gros plan (la queue) · 7 contre-plongée (tout là-haut) · 8 moyen (ça
tire !) · 9 large (dans le chêne) · 10 moyen (sur les épaules) · 11 large,
soir (main dans la main).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre, mains_personne
from fetes import cerf_volant_losange

ID = "papas-cerf-volant"

LEO = dict(peau="brune", cheveux="noir", coiffure="afro", habit="#fab005", robe=False, jambes="#1c7ed6", nez="rond")


def cravate(c="#1c7ed6", pois="#fff"):
    """Cravate à pois sur la chemise (tenue= d'un adulte)."""
    return g([poly([(-8, -104), (8, -104), (5, -96), (12, -50), (0, -38), (-12, -50), (-5, -96)], c),
              cercle(-3, -80, 2.5, pois), cercle(4, -64, 2.5, pois), cercle(-4, -54, 2.5, pois)])


PAPA = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#f8f9fa", robe=False, jambes="#495057",
            stature="adulte", carrure="ronde", nez="rond", barbe="#2b2b3a")
ROUGE, JAUNE = "#e03131", "#ffd43b"
QUEUE = [("#1c7ed6", "cravate"), ("#fab005", "foulard"), ("#e64980", "chaussette")]


def leo(x, y, s=1.3, foulard=True, **k):
    if foulard:
        k.setdefault("tenue", g([rect(-30, -110, 60, 16, "#fab005", rx=8), poly([(-6, -100), (16, -100), (6, -76)], "#f59f00")]))
    return personne(x, y, s, **{**LEO, "habit": "#20c997", **k})


def papa(x, y, s=1.3, cravate_=True, **k):
    """Papa, nettement plus grand que Léo : son échelle est majorée d'un cinquième."""
    if cravate_:
        k.setdefault("tenue", cravate())
    return personne(x, y, s * 1.2, **{**PAPA, **k})


def main_droite(x, y, s, bras, stature="enfant", carrure="normale", flip=False):
    return mains_personne(x, y, s, bras, flip=flip, stature=stature, carrure=carrure)[1]


def colline(S, haut="#74c0fc", bas="#e7f5ff", graine=4, sol_y=640):
    ciel(S, haut, bas)
    S.add(nuage(150, 120, 0.8), nuage(600, 160, 0.6))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, sol_y, "#8ce99a")


def vent(S, x, y, s=1.0, nb=3):
    for k in range(nb):
        S.add(chemin(f"M {x} {y + k * 40} q 60 -30 120 0 t 120 0 q 30 -20 10 -40", stroke="#fff", sw=6 * s, opacity=0.8))


def feuille_vole(x, y, rot=0, c="#69db7c"):
    return place([ellipse(0, 0, 14, 7, c), trait(-14, 0, 14, 0, _assombrir(c, 0.7), 2)], x, y, 1.0, rot=rot)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    colline(S)
    S.add(arbre(700, 640, 0.9))
    hx, hy = main_droite(330, 770, 1.5, "tient")
    S.add(cerf_volant_losange(560, 210, 0.9, ROUGE, JAUNE, rot=-15, queue=QUEUE, fil_vers=(hx, hy)))
    S.add(papa(530, 770, 1.3, expr="rire", bras="epaule", flip=True, regard=(-1, -0.5)))
    S.add(leo(330, 770, 1.5, expr="rire", bras="tient", regard=(1, -1)))
    S.add(oiseau(220, 260, 0.4), oiseau(280, 300, 0.3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cerf_volant_losange(170, 110, 0.75, ROUGE, JAUNE, rot=-30, queue=QUEUE))
    return S


def p01():
    """Plan moyen : le cadeau de Léo ; « Bonne fête, Papa ! »"""
    S = Scene()
    piece(S, "chaumiere", 600)
    S.add(fenetre(530, 100, 180, 160, "#a5d8ff", rideaux="#1c7ed6"))
    S.add(papa(560, 770, 1.45, expr="bouche_bee", bras="joues", regard=(-1, 0)))
    S.add(cerf_volant_losange(300, 400, 1.1, ROUGE, JAUNE, rot=-8))
    S.add(leo(260, 780, 1.4, expr="rire", bras="haut", regard=(1, 0)))
    S.add(bulle(300, 110, 380, 90, "Bonne fête, Papa !", 38, pointe=(300, 240)))
    return S


def p02():
    """Plan large : pas un brin de vent ; plouf ! dans l'herbe."""
    S = Scene()
    colline(S, "#74c0fc", "#fff9db")
    S.add(arbre(680, 640, 1.0))
    S.add(cerf_volant_losange(470, 700, 0.55, ROUGE, JAUNE, rot=60))
    S.add(texte(470, 600, "Plouf !", 50, "#495057", contour="#fff", rot=-8))
    S.add(leo(250, 760, 1.25, expr="oups", bras="lance", regard=(1, 0.5)))
    S.add(papa(110, 760, 1.25, expr="sourire", bras="croises", regard=(1, 0)))
    # le drapeau du sommet pend, tout mou
    S.add(trait(600, 640, 600, 470, "#868e96", 5), chemin("M 600 474 Q 612 520 604 560 L 600 560 Z", "#e03131"))
    S.cachette(760, 770)
    return S


def p03():
    """Plan moyen : on pique-nique en regardant les nuages."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff9db")
    S.add(nuage(560, 160, 1.3))
    S.add(cercle(500, 120, 30, "#fff"), cercle(530, 90, 14, "#fff"), cercle(475, 90, 14, "#fff"))
    collines(S, 560, "#b2f2bb", graine=8)
    sol(S, 620, "#8ce99a")
    S.add(chemin("M 120 760 L 680 760 L 640 680 L 160 680 Z", "#ff8787"),
          chemin("M 120 760 L 680 760 L 640 680 L 160 680 Z", "none", stroke="#fff", sw=3, stroke_dasharray="20 20"))
    S.add(papa(250, 720, 1.25, expr="sourire", bras="designe", regard=(1, -1)))
    S.add(leo(470, 730, 1.2, expr="content", bras="mains_jointes", regard=(1, -1)))
    S.add(cerf_volant_losange(640, 690, 0.4, ROUGE, JAUNE, rot=-80))
    S.add(rect(340, 690, 80, 50, "#c68642", rx=8), rect(345, 680, 70, 14, "#a0693a", rx=6))
    S.add(bulle(240, 320, 320, 100, "Le vent viendra.\nPatience !", 32, pointe=(250, 440)))
    S.cachette(760, 780)
    return S


def p04():
    """Plan large en diagonale : le vent arrive, Léo court, le cerf-volant tourne et pique du nez."""
    S = Scene()
    colline(S)
    vent(S, 20, 300)
    for k, (x, y) in enumerate(((150, 260), (230, 360), (90, 420), (330, 300))):
        S.add(feuille_vole(x, y, 30 * k))
    hx, hy = main_droite(420, 760, 1.25, "tient")
    S.add(cerf_volant_losange(640, 330, 0.6, ROUGE, JAUNE, rot=150, fil_vers=(hx, hy)))
    S.add(chemin("M 600 200 Q 720 190 700 270 Q 680 330 620 300", stroke="#495057", sw=3, opacity=0.6, stroke_dasharray="8 8"))
    S.add(leo(420, 760, 1.25, expr="surpris", bras="tient", regard=(1, -1), pas="court"))
    S.add(papa(170, 760, 1.25, expr="surpris", bras="designe", regard=(1, -1)))
    S.add(texte(620, 520, "Oh non !", 44, "#e03131", contour="#fff", rot=8))
    return S


def p05():
    """Gros plan : « Il lui manque une queue ! » Papa enlève sa cravate."""
    S = Scene()
    colline(S)
    S.add(papa(430, 900, 2.0, expr="malin", bras="tient", cravate_=False, regard=(-1, 0),
               objet=place(cravate(), *ancre(68, -40, "tient", "adulte", "ronde"), 1.6)))
    S.add(leo(170, 900, 1.8, expr="rire", bras="joues", regard=(1, 0)))
    S.camera(1.2, 360, 480)
    S.dessus(bulle(560, 100, 400, 110, "Il lui manque une queue\npour rester bien droit !", 30, pointe=S.vers_page(470, 360)))
    S.cachette(85, 267, "air")
    return S


def p06():
    """Gros plan : la queue — cravate, foulard, chaussette."""
    S = Scene()
    colline(S)
    S.add(cerf_volant_losange(400, 260, 1.15, ROUGE, JAUNE, rot=0, queue=QUEUE))
    S.add(texte(600, 480, "la cravate !", 34, "#1c7ed6", contour="#fff"),
          texte(220, 560, "le foulard !", 34, "#f59f00", contour="#fff"),
          texte(600, 640, "une chaussette !", 34, "#e64980", contour="#fff"))
    S.cachette(740, 770)
    return S


def p07():
    """Contre-plongée : le cerf-volant monte plus haut que les arbres, plus haut que les oiseaux."""
    S = Scene()
    ciel(S, "#1c7ed6", "#a5d8ff")
    S.add(nuage(160, 260, 1.0), nuage(620, 420, 0.8))
    S.add(cerf_volant_losange(470, 170, 0.8, ROUGE, JAUNE, rot=-12, queue=QUEUE, fil_vers=(330, 820)))
    S.add(oiseau(260, 420, 0.5), oiseau(330, 470, 0.4), oiseau(200, 500, 0.35))
    S.add(arbre(80, 980, 2.0), arbre(760, 1000, 2.2))
    S.cachette(150, 380, "air")
    return S


def p08():
    """Plan moyen : Léo tient la ficelle tout seul ; ça tire fort !"""
    S = Scene()
    colline(S)
    vent(S, 40, 420, 0.8, 2)
    hx, hy = main_droite(380, 760, 1.45, "tire")
    S.add(cerf_volant_losange(680, 170, 0.5, ROUGE, JAUNE, rot=-20, queue=QUEUE, fil_vers=(hx, hy)))
    S.add(papa(170, 760, 1.4, expr="content", bras="ouverts", regard=(1, 0)))
    S.add(leo(380, 760, 1.45, expr="concentre", bras="tire", regard=(1, -0.5), pas="pointe"))
    S.add(texte(560, 480, "Ça tire !", 48, "#e8590c", contour="#fff", rot=-8))
    S.cachette(760, 770)
    return S


def p09():
    """Plan large : crac ! le cerf-volant dans le grand chêne."""
    S = Scene()
    colline(S)
    S.add(arbre(470, 700, 2.4))
    S.add(cerf_volant_losange(560, 220, 0.5, ROUGE, JAUNE, rot=35, queue=QUEUE[:2]))
    S.add(texte(640, 120, "Crac !", 54, "#8d5524", contour="#fff", rot=10))
    S.add(leo(130, 770, 1.2, expr="pleure", bras="joues", regard=(1, -1)))
    S.add(papa(320, 770, 1.2, expr="inquiet", bras="hanches", regard=(1, -1)))
    S.cachette(760, 770)
    return S


def p10():
    """Plan moyen : sur les épaules de Papa, Léo décroche le cerf-volant."""
    S = Scene()
    colline(S)
    S.add(arbre(560, 980, 3.4))
    S.add(cerf_volant_losange(470, 140, 0.45, ROUGE, JAUNE, rot=20, queue=QUEUE[:2]))
    S.add(leo(400, 470, 1.15, expr="concentre", bras="haut", regard=(0.5, -1)))
    S.add(papa(400, 800, 1.45, expr="rire", bras="tete", regard=(0, -1)))
    S.cachette(90, 770)
    return S


def p11():
    """Plan large, soir : main dans la main, ils regardent le soleil se coucher."""
    S = Scene()
    ciel(S, "#f76707", "#ffd8a8")
    S.add(soleil(640, 470, 70, couleur="#ff922b", rayons=False))
    collines(S, 540, "#94d82d", graine=9)
    sol(S, 600, "#74b816")
    S.add(cerf_volant_losange(560, 700, 0.45, ROUGE, JAUNE, rot=-100, queue=QUEUE))
    S.add(leo(250, 770, 1.2, expr="content", bras="main", regard=(1, -0.3)))
    S.add(papa(465, 765, 1.2, expr="content", bras="main", flip=True, regard=(-1, -0.3)))
    S.add(bulle(400, 150, 520, 110, "Le plus beau cadeau,\nc'est cette journée avec toi.", 30, pointe=(420, 380)))
    S.cachette(760, 770)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cerf-volant-seul.svg", vignette),
    ("01-le-cadeau.svg", p01), ("02-plouf.svg", p02), ("03-le-pique-nique.svg", p03),
    ("04-oh-non.svg", p04), ("05-la-cravate.svg", p05), ("06-la-queue.svg", p06),
    ("07-tout-la-haut.svg", p07), ("08-ca-tire.svg", p08), ("09-dans-le-chene.svg", p09),
    ("10-sur-les-epaules.svg", p10), ("11-main-dans-la-main.svg", p11),
]
