"""La Belle au bois dormant — d'après Charles Perrault, en version douce.

Pour la naissance de la princesse Aurore, le roi et la reine invitent les
fées, qui lui offrent leurs dons. Mais une vieille fée, oubliée, arrive en
colère : à seize ans, la princesse se piquera le doigt à un fuseau et
tombera dans un sommeil sans fin. La plus jeune fée adoucit le sort : cent
ans seulement, et elle se réveillera. Le roi fait enfermer tous les fuseaux,
mais seize ans plus tard, au fond d'une vieille tour, Aurore trouve une
fileuse… Elle s'endort, et la bonne fée endort tout le château avec elle.
Les ronces poussent. Cent ans plus tard, un prince arrive ; les ronces
fleurissent et s'écartent ; au moment où il entre, les cent ans sont finis
et Aurore ouvre les yeux (comme chez Perrault, sans baiser) : « Est-ce vous,
mon prince ? Vous vous êtes bien fait attendre ! » Le château se réveille,
et pour la fête, on n'oublie personne, pas même la vieille fée.

Plans : 1 large (la fête de la naissance) · 2 moyen (les dons des fées) · 3
moyen (la fée oubliée) · 4 moyen (on enferme les fuseaux) · 5 moyen (la
vieille tour) · 6 gros plan (aïe !) · 7 large (le château endormi) · 8 large
(les ronces) · 9 large (le prince et les roses) · 10 moyen (le réveil) · 11
large (atchoum !) · 12 large (la fête).
"""
from contes import *

ID = "belle-bois-dormant"

AURORE = dict(coiffure="tres_longs", cheveux="brun", peau="doree", habit="#f783ac", motif_robe="#fff0f6", stature="ado", yeux="cils",
              acc=("diademe",))
ROI = dict(stature="adulte", peau="claire", cheveux="roux", coiffure="courts", barbe="#e8590c", carrure="ronde", nez="rond")
REINE = dict(stature="adulte", peau="doree", cheveux="brun", yeux="cils")
FEES = [dict(coiffure="chignon", cheveux="blond", peau="rosee", habit="#74c0fc", ailes="#d0ebff", motif_robe="#fff", stature="adulte"),
        dict(coiffure="boucles", cheveux="roux", peau="claire", habit="#69db7c", ailes="#d3f9d8", motif_robe="#fff", stature="adulte"),
        dict(coiffure="couettes", cheveux="noir", peau="brune", habit="#ffd43b", ailes="#fff3bf", motif_robe="#fff", stature="ado")]
VIEILLE_FEE = dict(coiffure="chignon", cheveux="gris", peau="rosee", habit="#5f3dc4", ailes="#adb5bd", stature="ancien", nez="long",
                   carrure="fine")
PRINCE = dict(stature="adulte", peau="brune", cheveux="noir", coiffure="courts", habit="#1971c2", robe=False, jambes="#495057",
              cape="#c92a2a", nez="long")
FILEUSE = dict(stature="ancien", peau="rosee", cheveux="blanc", coiffure="chignon", habit="#868e96", robe=True, nez="rond")
CUISINIER = dict(stature="adulte", peau="rosee", cheveux="brun", coiffure="courts", habit="#fff", robe=False, jambes="#495057",
                 acc=("toque",), carrure="ronde", barbe="#4a2c17")
GARDE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="courts", habit="#c92a2a", robe=False, jambes="#1c2a52",
             acc=("casque",))
ROSE = "#f06595"


def aurore(x, y, s=1.4, **k):
    return personne(x, y, s, **{**AURORE, **k})


def fee_(i, x, y, s=1.4, rot_baguette=20, **k):
    d = FEES[i]
    k.setdefault("bras", "tient")
    k.setdefault("objet", baguette(*ancre(68, -146, "tient", d["stature"]), 0.9, rot=rot_baguette))
    return personne(x, y, s, **{**d, **k})


def vieille_fee(x, y, s=1.4, **k):
    return personne(x, y, s, **{**VIEILLE_FEE, **k})


def prince(x, y, s=1.5, **k):
    return personne(x, y, s, **{**PRINCE, **k})


def berceau_royal(x, y, s=1.0, bebe=True):
    m = [trait(-70, 0, -60, -90, "#c68642", 8), trait(70, 0, 60, -90, "#c68642", 8),
         chemin("M -100 -150 Q -96 -84 0 -80 Q 96 -84 100 -150 Z", volume("#fff0f6", 0.2, 0.85), stroke="#fcc2d7", sw=3),
         chemin("M -90 -150 Q -60 -260 0 -270 Q 60 -260 90 -150", "none", stroke="#fcc2d7", sw=6),
         chemin("M -20 -268 Q -100 -200 -96 -140 L -70 -140 Q -70 -210 -10 -260 Z", "#ffdeeb", opacity=0.8)]
    if bebe:
        m += [ellipse(0, -150, 70, 14, "#fff"), cercle(-30, -160, 14, "#f0c39a"), chemin("M -36 -162 q 3 3 6 0 M -26 -162 q 3 3 6 0", stroke=ENCRE, sw=1.5),
              ellipse(10, -152, 40, 12, "#fcc2d7")]
    return place(m, x, y, s)


def rouet(x, y, s=1.0):
    """Rouet de fileuse, avec son fuseau pointu ; (x, y) = au sol."""
    m = [trait(-80, 0, -40, -80, "#8d5524", 8), trait(60, 0, 20, -80, "#8d5524", 8), rect(-80, -90, 160, 18, "#a0693a", rx=6),
         cercle(-10, -170, 70, "none", stroke="#a0693a", stroke_width=8)]
    for k in range(8):
        a = math.radians(k * 45)
        m.append(trait(-10, -170, -10 + math.cos(a) * 66, -170 + math.sin(a) * 66, "#c68642", 4))
    m += [cercle(-10, -170, 8, "#8d5524"), trait(-10, -170, -10, -90, "#8d5524", 6),
          trait(70, -90, 70, -150, "#8d5524", 5), trait(70, -150, 120, -150, "#495057", 4), poly([(120, -153), (138, -150), (120, -147)], "#495057"),
          ellipse(90, -150, 18, 8, "#f8f9fa")]
    return place(m, x, y, s)


def fuseau(x, y, s=1.0, rot=0):
    return place([trait(-40, 0, 40, 0, "#a0693a", 5), ellipse(-6, 0, 16, 8, "#f8f9fa"), poly([(40, -3), (54, 0), (40, 3)], "#495057")], x, y, s, rot=rot)


def ronces(S, y0=400, y1=800, graine=1, densite=26, fleurs=True, x0=0, x1=800):
    r = random.Random(graine)
    for k in range(densite):
        x = r.uniform(x0, x1)
        yb = r.uniform(y0 + 100, y1)
        d = f"M {x} {yb} q {r.uniform(-60, 60)} {-r.uniform(60, 120)} {r.uniform(-30, 30)} {-r.uniform(140, 260)}"
        S.add(chemin(d, stroke="#2b8a3e", sw=r.uniform(6, 10)))
        for j in range(4):
            px, py = x + r.uniform(-30, 30), yb - r.uniform(30, 220)
            S.add(poly([(px, py), (px + 8, py - 4), (px + 2, py + 6)], "#1b5e20"))
        if fleurs and k % 2:
            px, py = x + r.uniform(-20, 20), yb - r.uniform(120, 240)
            S.add(cercle(px, py, 14, volume(ROSE, 0.35, 0.8)), cercle(px, py, 5, "#c2255c"))


def chambre_royale(S, nuit_=False):
    piece(S, "chateau", y=600)
    if nuit_:
        S.ambiance("nuit")


def lit_baldaquin(x, y, s=1.0):
    m = [rect(-200, -330, 16, 330, "#a0693a"), rect(184, -330, 16, 330, "#a0693a"),
         chemin("M -210 -340 L 210 -340 L 200 -300 Q 0 -270 -200 -300 Z", "#c2255c"),
         rect(-200, -110, 400, 70, "#fff", rx=10), rect(-180, -150, 120, 50, "#fff", rx=20, stroke="#e9ecef", stroke_width=3)]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    nuit(S, "#3b2d6b", "#a37ad8")
    etoiles(S, 30, graine=2, zone=(0, 0, 800, 380))
    S.add(lune(660, 120, 44))
    S.add(chateau(400, 690, 1.05, mur="#e5dbff", mur2="#d0bfff", toit="#c2255c", nuit_=True))
    ronces(S, 330, 820, graine=3, densite=40)
    S.add(rect(0, 690, 800, 110, "#2b8a3e"))
    ronces(S, 600, 860, graine=5, densite=20)
    S.cachette(740, 790)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rouet(200, 255, 0.9))
    S.add(cercle(330, 120, 18, volume(ROSE, 0.35, 0.8)), chemin("M 330 138 q -6 40 -20 70", stroke="#2b8a3e", sw=5))
    return S


def p01():
    """Plan large : grande fête au château pour la naissance de la princesse ; le roi et la reine près du berceau."""
    S = Scene()
    salle_bal(S)
    S.add(berceau_royal(400, 780, 1.1))
    S.add(roi(200, 790, 1.5, expr="rire", bras="ouverts", regard=(1, 0), **ROI))
    S.add(reine(610, 790, 1.5, expr="joie", bras="joues", flip=True, regard=(-1, 0.5), **REINE))
    for k in range(6):
        S.add(cercle(110 + k * 115, 210 + (k % 2) * 20, 16, ("#ff8787", "#ffd43b", "#74c0fc")[k % 3]))
    S.add(chemin("M 80 200 Q 400 260 720 200", stroke="#adb5bd", sw=2))
    S.add(texte(400, 340, "Bienvenue, Aurore !", 44, "#c2255c", contour="#fff"))
    S.cachette(290, 70, "air")
    return S


def p02():
    """Plan moyen : au-dessus du berceau, trois fées penchent leur baguette : la douceur, le chant, la danse."""
    S = Scene()
    salle_bal(S)
    S.add(berceau_royal(400, 790, 1.1))
    S.add(fee_(0, 160, 790, 1.4, expr="content", regard=(1, 0.5)))
    S.add(fee_(1, 640, 790, 1.4, expr="content", flip=True, regard=(-1, 0.5), rot_baguette=-20))
    S.add(fee_(2, 420, 520, 1.0, expr="rire", regard=(0, 1)))
    S.add(etincelles(400, 600, 1.3, OR, graine=2), etincelles(300, 520, 0.8, "#74c0fc", graine=3), etincelles(520, 540, 0.8, "#69db7c", graine=4))
    S.add(texte(400, 120, "Les dons des fées", 48, "#7048e8", contour="#fff"))
    return S


def p03():
    """Plan moyen : la vieille fée oubliée surgit, furieuse : « À seize ans, elle se piquera le doigt à un fuseau ! »"""
    S = Scene()
    salle_bal(S)
    S.add(rect(0, 0, 800, 800, "#3b2d6b", opacity=0.25))
    S.add(berceau_royal(560, 790, 1.0))
    S.add(nuage_orage(240, 160, 1.0))
    S.add(vieille_fee(240, 790, 1.5, expr="furieux", bras="designe", regard=(1, 0.3)))
    S.add(fee_(2, 690, 790, 1.15, expr="inquiet", flip=True, regard=(-1, 0)))
    S.add(bulle(530, 160, 440, 130, "À seize ans, elle se piquera\nle doigt à un fuseau, et elle\ns'endormira pour toujours !", 26,
                pointe=(380, 300)))
    return S


def p04():
    """Plan moyen : le roi fait enfermer tous les fuseaux du royaume dans un grand coffre."""
    S = Scene()
    piece(S, "chateau", y=600)
    S.add(rect(320, 640, 240, 140, volume("#a0693a", 0.3, 0.8), rx=10), rect(320, 640, 240, 26, "#8d5524"),
          rect(420, 680, 40, 40, OR, rx=6))
    for k in range(7):
        S.add(fuseau(360 + k * 28, 630 - (k % 3) * 8, 0.9, rot=-30 + k * 8))
    S.add(roi(170, 790, 1.5, expr="fache", bras="designe", regard=(1, 0.4), **ROI))
    S.add(personne(650, 790, 1.4, expr="concentre", bras="porte", flip=True, regard=(-1, 0.4),
                   objet=g([fuseau(-30, -90, 0.9, rot=-20), fuseau(0, -84, 0.9, rot=10), fuseau(26, -94, 0.9, rot=30)]), **GARDE))
    S.add(bulle(260, 150, 420, 110, "Plus un seul fuseau\ndans tout le royaume !", 32, pointe=(220, 300)))
    return S


def p05():
    """Plan moyen : seize ans plus tard, tout en haut d'une vieille tour, Aurore découvre une vieille dame qui file."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(fenetre(80, 100, 120, 160, "#a5d8ff"))
    S.add(rouet(520, 790, 1.3))
    S.add(personne(680, 790, 1.4, expr="content", bras="tend", flip=True, regard=(-1, 0), **FILEUSE))
    S.add(aurore(230, 790, 1.45, expr="bouche_bee", bras="designe", regard=(1, 0.2)))
    S.add(bulle(260, 150, 380, 90, "Qu'est-ce que c'est ?", 34, pointe=(240, 300)))
    return S


def p06():
    """Gros plan : Aurore touche le fuseau… Aïe ! elle se pique le doigt et s'endort aussitôt."""
    S = Scene()
    piece(S, "chaumiere", y=600)
    S.add(rouet(560, 860, 1.6))
    S.add(aurore(330, 880, 1.8, expr="dort", bras="tend", regard=(1, 0)))
    S.camera(1.15, 420, 520)
    S.dessus(texte(430, 120, "Aïe !", 80, "#c92a2a", contour="#fff"))
    S.dessus(zzz(220, 300, 1.2))
    return S


def p07():
    """Plan large : tout le château s'endort : le roi sur son trône, le cuisinier, le garde, le chat et le chien."""
    S = Scene()
    piece(S, "chateau", y=600)
    S.ambiance("nuit")
    S.add(rect(320, 360, 160, 250, volume("#c92a2a", 0.3, 0.8), rx=20), rect(300, 560, 200, 60, "#a0693a", rx=10))
    S.add(roi(400, 760, 1.25, expr="dort", bras="bas", **ROI))
    S.add(personne(150, 790, 1.35, expr="dort", bras="porte", objet=trait(-40, -110, 60, -150, "#adb5bd", 6), **CUISINIER))
    S.add(personne(660, 790, 1.35, expr="dort", bras="bas", rot=8, **GARDE))
    S.add(perso("chat", 320, 790, 0.45, expr="dort"), perso("chien", 500, 790, 0.5, expr="dort"))
    for x, y in ((150, 420), (420, 340), (660, 420)):
        S.add(zzz(x, y, 0.8))
    S.cachette(630, 70, "air")
    return S


def p08():
    """Plan large : autour du château endormi, les ronces poussent, poussent, et couvrent tout de leurs roses."""
    S = Scene()
    ciel(S, "#a5d8ff", "#fff0f6")
    S.add(chateau(400, 700, 0.95, mur="#e5dbff", mur2="#d0bfff", toit="#c2255c"))
    ronces(S, 260, 820, graine=8, densite=50)
    S.add(rect(0, 700, 800, 100, "#2b8a3e"))
    ronces(S, 560, 860, graine=9, densite=24)
    S.add(texte(400, 110, "Cent ans passent…", 52, "#c2255c", contour="#fff"))
    S.cachette(40, 790)
    return S


def p09():
    """Plan large : cent ans plus tard, un prince arrive ; devant lui, les ronces fleurissent et s'écartent."""
    S = Scene()
    ciel(S, "#74c0fc", "#fff0f6")
    S.add(chateau(560, 600, 0.6, mur="#e5dbff", mur2="#d0bfff", toit="#c2255c"))
    S.add(rect(0, 600, 800, 200, "#8ce99a"))
    ronces(S, 380, 820, graine=10, densite=18, x0=0, x1=260)
    ronces(S, 380, 820, graine=11, densite=18, x0=560, x1=800)
    S.add(chemin("M 300 800 Q 380 680 470 600 L 530 600 Q 520 680 520 800 Z", "#e9c46a"))
    S.add(prince(400, 790, 1.5, expr="bouche_bee", bras="ouverts", regard=(0.5, -0.5)))
    for x, y in ((250, 520), (300, 460), (560, 500), (600, 440)):
        S.add(cercle(x, y, 16, volume(ROSE, 0.35, 0.8)), cercle(x, y, 6, "#c2255c"))
    return S


def p10():
    """Plan moyen : dans la chambre, la princesse ouvre les yeux au moment où le prince entre : les cent ans sont finis."""
    S = Scene()
    chambre_royale(S)
    S.add(lit_baldaquin(300, 760, 1.0))
    S.add(place(personne(0, 0, 1.0, expr="content", bras="bas", regard=(1, -0.3), **AURORE), 420, 640, 0.95, rot=-90))
    S.add(rect(240, 600, 250, 90, "#f783ac", rx=18))
    S.add(prince(630, 790, 1.5, expr="bouche_bee", bras="joues", flip=True, regard=(-1, 0.2)))
    S.camera(1.15, 380, 560)
    S.dessus(bulle(330, 130, 480, 110, "Est-ce vous, mon prince ? Vous\nvous êtes bien fait attendre !", 28, pointe=(200, 420)))
    return S


def p11():
    """Plan large : tout le château se réveille : le cuisinier éternue, le chat s'étire, le roi bâille : « Atchoum ! »"""
    S = Scene()
    piece(S, "chateau", y=600)
    S.add(rect(320, 360, 160, 250, volume("#c92a2a", 0.3, 0.8), rx=20), rect(300, 560, 200, 60, "#a0693a", rx=10))
    S.add(roi(400, 760, 1.25, expr="baille", bras="etire", **ROI))
    S.add(personne(150, 790, 1.35, expr="souffle", bras="bouche", **CUISINIER))
    S.add(personne(660, 790, 1.35, expr="surpris", bras="haut", **GARDE))
    S.add(perso("chat", 320, 790, 0.45, expr="baille", bras="haut"), perso("chien", 500, 790, 0.5, expr="rire", bras="haut"))
    for k in range(10):
        S.add(cercle(120 + k * 60, 300 + (k % 3) * 40, 6 + k % 3 * 3, "#dee2e6", opacity=0.7))
    S.add(texte(160, 330, "Atchoum !", 44, "#495057", contour="#fff"))
    S.cachette(230, 70, "air")
    return S


def p12():
    """Plan large : grande fête au château ; cette fois, toutes les fées sont invitées, même la vieille fée, qui sourit."""
    S = Scene()
    salle_bal(S)
    S.add(fee_(0, 90, 790, 1.15, expr="rire", regard=(1, 0)), vieille_fee(700, 790, 1.2, expr="content", bras="applaudit", flip=True))
    S.add(prince(300, 790, 1.4, expr="rire", bras="main", regard=(1, 0)))
    S.add(aurore(480, 790, 1.4, expr="rire", bras="main", flip=True, regard=(-1, 0)))
    S.add(etincelles(400, 300, 1.4, OR, graine=7))
    S.add(texte(400, 150, "On n'oublie plus personne !", 44, "#7048e8", contour="#fff"))
    S.cachette(290, 70, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("rouet-seul.svg", vignette),
    ("01-la-fete.svg", p01), ("02-les-dons.svg", p02), ("03-la-fee-oubliee.svg", p03),
    ("04-les-fuseaux.svg", p04), ("05-la-vieille-tour.svg", p05), ("06-aie.svg", p06),
    ("07-tout-dort.svg", p07), ("08-les-ronces.svg", p08), ("09-le-prince.svg", p09),
    ("10-le-reveil.svg", p10), ("11-atchoum.svg", p11), ("12-la-grande-fete.svg", p12),
]
