"""La cheffe Rosalie — une journée dans la cuisine d'un restaurant.

Au marché à l'aube, Rosalie choisit ses légumes ; en cuisine, on se lave les
mains et on met sa toque ; la brigade (commis, pâtissier, plongeur) se met
au travail ; l'oignon pique les yeux, on goûte la soupe, on dresse la tarte ;
« Service ! » ; Théo et sa grand-mère se régalent ; on nettoie tout ; Théo
reçoit une petite toque.

Plans : 1 large (le marché) · 2 moyen (les mains, la toque) · 3 large (la
brigade) · 4 gros plan (l'oignon) · 5 moyen (goûter la soupe) · 6 gros plan
(la tarte) · 7 large (« Service ! ») · 8 moyen (Théo se régale) · 9 moyen
(la plonge) · 10 gros plan (la petite toque).
"""
from base import *
from base import _assombrir
from fantastique import personne, mains_personne, ancre
from metiers import pro, petit, tablier
from contes import carotte, oignon, chou
from objets import bol, assiette, pomme

ID = "cheffe-cuisine"
PAPIER_PEINT = "losanges"

ROSALIE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chignon", habit="#ffffff", jambes="#343a40",
               chaussures="#212529", tenue=tablier("#f1f3f5"), acc=("toque",), carrure="ronde", nez="rond")
COMMIS = dict(stature="ado", peau="claire", cheveux="roux", coiffure="courts", habit="#ffffff", jambes="#343a40",
              tenue=tablier("#f1f3f5"), taches=True, robe=False)
PATISSIER = dict(stature="adulte", peau="foncee", cheveux="noir", coiffure="courts", habit="#ffffff", jambes="#343a40",
                 tenue=tablier("#ffc9c9", "#ffa8a8"), barbe="#2b2b3a", acc=("toque",))
PLONGEUSE = dict(stature="adulte", peau="rosee", cheveux="blond", coiffure="queue", habit="#74c0fc", jambes="#343a40",
                 tenue=tablier("#d0ebff", "#a5d8ff"), robe=False)
THEO = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#40c057", robe=False, jambes="#1864ab")
MAMIE = dict(stature="ancien", peau="brune", cheveux="gris", coiffure="chignon", habit="#ae3ec9", acc=("lunettes",))


def rosalie(x, y, s=1.4, **k):
    k.setdefault("robe", False)
    return personne(x, y, s, **{**ROSALIE, **k})


def couteau(x, y, s=1.0, rot=0):
    return place([rect(-6, -20, 12, 40, "#343a40", rx=4), chemin("M -8 -20 L -8 -110 Q 4 -110 10 -60 L 10 -20 Z", "#ced4da", stroke="#868e96", sw=2)],
                 x, y, s, rot=rot)


def marmite(x, y, s=1.0, fumee=True, contenu="#ff922b"):
    m = [rect(-90, -120, 180, 120, cylindre("#adb5bd", 0.3, 0.75), rx=10), ellipse(0, -120, 90, 18, "#868e96"),
         ellipse(0, -120, 80, 14, contenu), rect(-112, -100, 26, 14, "#495057", rx=6), rect(86, -100, 26, 14, "#495057", rx=6)]
    if fumee:
        for k in (-40, 0, 40):
            m.append(chemin(f"M {k} -140 q -14 -24 0 -48 q 14 -24 0 -48", stroke="#fff", sw=7, opacity=0.8))
    return place(m, x, y, s)


def tarte(x, y, s=1.0):
    m = [ellipse(0, 0, 130, 30, "#fff", stroke="#dee2e6", stroke_width=3), ellipse(0, -10, 112, 24, "#e8a33d"),
         ellipse(0, -14, 100, 20, "#ffd8a8")]
    for k in range(10):
        a = math.radians(k * 36)
        m.append(ellipse(math.cos(a) * 60, -14 + math.sin(a) * 11, 28, 9, "#fcc419", rot=k * 36, stroke="#f59f00", stroke_width=1.5))
    m.append(ellipse(0, -14, 20, 6, "#fab005"))
    return place(m, x, y, s)


def cuisine_resto(S, y=600):
    """Cuisine professionnelle : carrelage, hotte, plans de travail en inox."""
    piece(S, "cuisine", y)
    S.add(poly([(160, 60), (640, 60), (600, 170), (200, 170)], volume("#ced4da", 0.3, 0.8)))
    S.add(rect(200, 166, 400, 14, "#868e96"))
    S.add(rect(0, y - 130, 800, 20, "#dee2e6"))
    S.add(trait(40, 250, 300, 250, "#868e96", 4))
    for k, xx in enumerate(range(60, 300, 50)):
        S.add(trait(xx, 250, xx, 290, "#868e96", 2), place(chemin("M -10 0 Q 0 20 10 0 Z", "#adb5bd"), xx, 296))


def plan_travail(x, y, w=500, s=1.0):
    """Plan de travail en inox ; (x, y) = milieu du pied ; le dessus est à y - 180 s."""
    return place([rect(-w / 2, -180, w, 180, cylindre("#dee2e6", 0.3, 0.8, vertical=True), rx=4),
                  rect(-w / 2 - 6, -190, w + 12, 16, "#adb5bd", rx=4), rect(-w / 2 + 20, -150, w - 40, 110, "none", stroke="#ced4da", stroke_width=3)],
                 x, y, s)


def salle_resto(S, y=600):
    interieur(S, "#fff4e6", "#a0693a", y, papier="#ffd8a8")
    S.add(fenetre(80, 90, 180, 160, "#a5d8ff", rideaux="#c92a2a",
                  contenu=g([rect(0, 0, 800, 800, "#a5d8ff"), arbre(180, 330, 0.5)])))
    S.add(cadre_mur(560, 120, 130, 100, "#ffd8a8"))


def etal(x, y, s=1.0):
    """Étal de légumes au marché ; (x, y) = milieu du pied."""
    m = [rect(-220, -150, 440, 150, volume("#c68642", 0.3, 0.8)), rect(-240, -170, 480, 26, "#a0693a", rx=4),
         trait(-220, -170, -220, -390, "#8d5524", 10), trait(220, -170, 220, -390, "#8d5524", 10)]
    for k in range(8):
        c = "#e03131" if k % 2 == 0 else "#fff"
        m.append(poly([(-240 + k * 60, -400), (-180 + k * 60, -400), (-180 + k * 60, -360), (-210 + k * 60, -340), (-240 + k * 60, -360)], c))
    for k in range(6):
        m.append(cercle(-190 + k * 26, -180, 14, volume("#fa5252", 0.4, 0.75)))
    m.append(carotte(40, -180, 0.5, rot=-90) + carotte(60, -190, 0.5, rot=-80) + carotte(80, -178, 0.5, rot=-95))
    m.append(chou(170, -200, 0.5))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    cuisine_resto(S)
    S.add(plan_travail(400, 800, 760))
    S.add(marmite(560, 610, 0.9))
    S.add(rosalie(300, 790, 1.55, expr="rire", bras="tient", regard=(1, 0), objet=place(bol(0, 0, 0.5, "#fff", "#ff922b", True), *ancre(70, -146, "tient", "adulte"))))
    S.lumiere(560, 480, 120, "#ffd43b", 0.3)
    return S


def vignette():
    S = Scene(400, 270)
    toque = [cercle(-26, -218, 27.5, "#dee2e6"), cercle(26, -218, 27.5, "#dee2e6"), cercle(0, -232, 31.5, "#dee2e6"),
             cercle(-26, -218, 26, "#fff"), cercle(26, -218, 26, "#fff"), cercle(0, -232, 30, "#fff"),
             rect(-40, -208, 80, 26, "#fff", rx=6, stroke="#e9ecef", stroke_width=2)]
    S.add(place(toque, 120, 462, 1.6))
    S.add(marmite(290, 250, 0.85))
    return S


def p01():
    """Plan large : à l'aube, au marché, Rosalie choisit les légumes."""
    S = Scene()
    ciel(S, "#ffa8a8", "#fff4e6")
    S.add(rect(0, 640, 800, 160, "#ced4da"))
    immeubles = [immeuble(20, 640, 160, 4, "#ffd8a8", "mansarde"), immeuble(600, 640, 180, 4, "#d3f9d8", "pignon")]
    S.add(*immeubles)
    S.add(etal(400, 760, 1.0))
    S.add(personne(240, 790, 1.2, stature="ancien", peau="claire", cheveux="blanc", coiffure="chauve_cote", habit="#2f9e44", robe=False,
                   jambes="#5c3a1e", expr="content", bras="donne", regard=(1, 0), objet=carotte(*ancre(84, -92, "donne", "ancien"), 0.6, rot=-80)))
    S.add(rosalie(620, 790, 1.25, expr="content", bras="pense", regard=(-1, 0), tenue=None, acc=(), habit="#c92a2a"))
    S.add(texte(400, 120, "Bonjour, les légumes !", 44, "#c92a2a", contour="#fff"))
    return S


def p02():
    """Plan moyen : en cuisine, Rosalie se lave les mains et met sa toque."""
    S = Scene()
    cuisine_resto(S)
    S.add(rect(120, 520, 260, 30, "#adb5bd", rx=6), rect(150, 550, 200, 60, "#ced4da", rx=10))
    S.add(chemin("M 250 420 Q 250 380 290 380", stroke="#868e96", sw=12))
    for k in range(4):
        S.add(goutte(258 + k * 6, 470 + k * 20, 0.6, "#74c0fc"))
    S.add(rosalie(260, 790, 1.4, expr="content", bras="mains_jointes", regard=(0, 0.6)))
    for x, y in ((230, 600), (280, 590), (250, 570)):
        S.add(cercle(x, y, 9, "#fff", stroke="#a5d8ff", stroke_width=2))
    S.add(bulle(570, 260, 340, 110, "D'abord,\non se lave les mains !", 30, pointe=(330, 420)))
    return S


def p03():
    """Plan large : la brigade au travail : commis, pâtissier, plongeuse et la cheffe."""
    S = Scene()
    cuisine_resto(S)
    S.add(personne(130, 640, 1.0, expr="concentre", bras="porte", regard=(0, 0.5), **COMMIS))
    S.add(personne(330, 640, 1.0, expr="content", bras="tient", regard=(1, 0), objet=couteau(*ancre(68, -146, "tient", "adulte"), 0.5),
                   **{**ROSALIE, "robe": False}))
    S.add(personne(530, 640, 1.0, expr="joie", bras="porte", regard=(0, 0.5), robe=False, **PATISSIER))
    S.add(personne(710, 640, 1.0, expr="rire", bras="salut", regard=(-1, 0), **PLONGEUSE))
    S.add(plan_travail(400, 800, 760))
    S.add(marmite(232, 612, 0.5), tarte(600, 616, 0.6))
    S.add(texte(400, 250, "La brigade", 48, "#e8590c", contour="#fff"))
    return S


def p04():
    """Gros plan : Rosalie coupe un oignon, les doigts repliés ; l'oignon pique les yeux."""
    S = Scene()
    cuisine_resto(S)
    S.add(plan_travail(400, 800, 760))
    S.add(rect(240, 600, 320, 30, "#c68642", rx=8))
    S.add(oignon(380, 596, 1.0), place(chemin("M 0 -40 Q -30 -20 -24 10 L 24 10 Q 30 -20 0 -40 Z", "#f3d9b1"), 470, 596))
    S.add(rosalie(400, 900, 2.0, expr="pleure", bras="porte", larmes=True, regard=(0, 0.6),
                  objet=couteau(*ancre(26, -74, "porte", "adulte"), 0.9, rot=-10)))
    S.camera(1.25, 400, 520)
    S.dessus(bulle(580, 120, 340, 90, "Ça pique les yeux !", 32, pointe=S.vers_page(440, 500)))
    return S


def p05():
    """Plan moyen : Rosalie goûte la soupe avec une cuillère."""
    S = Scene()
    cuisine_resto(S)
    S.add(plan_travail(440, 800, 600))
    S.add(marmite(560, 620, 1.1))
    S.add(rosalie(270, 790, 1.45, expr="miam", bras="bouche", regard=(1, 0)))
    S.add(personne(680, 790, 1.15, expr="content", bras="bas", regard=(-1, 0), **COMMIS))
    S.add(bulle(330, 150, 380, 100, "Une pincée de sel…\nParfait !", 32, pointe=(300, 400)))
    return S


def p06():
    """Gros plan : le pâtissier dresse une tarte aux pommes."""
    S = Scene()
    cuisine_resto(S)
    S.add(personne(400, 760, 1.6, expr="concentre", bras="large", regard=(0, 0.6), robe=False, **PATISSIER))
    S.add(plan_travail(400, 800, 760))
    S.add(tarte(400, 620, 1.3))
    S.add(pomme(220, 600, 1.4, "#94d82d"), pomme(600, 604, 1.4, "#fa5252"))
    S.camera(1.3, 400, 540)
    S.dessus(texte(400, 110, "La tarte aux pommes", 48, "#e8590c", contour="#fff"))
    return S


def vadrouille(x, y, s=1.0):
    """Balai à franges tenu en main ; (x, y) = la main."""
    return place([trait(0, -40, 30, 160, "#a0693a", 8), chemin("M 0 150 Q 30 140 60 150 L 74 200 L -14 200 Z", "#e9ecef"),
                  chemin("M 6 160 L -2 200 M 22 158 L 18 200 M 38 158 L 40 200 M 54 160 L 62 200", stroke="#ced4da", sw=3)], x, y, s)


def clochette(x, y, s=1.0):
    return place([ellipse(0, 0, 40, 10, "#adb5bd"), chemin("M -30 0 Q -30 -40 0 -44 Q 30 -40 30 0 Z", volume("#fcc419", 0.4, 0.7)),
                  rect(-4, -56, 8, 14, "#f59f00", rx=3)], x, y, s)


def p07():
    """Plan large : « Service ! » ; le serveur emporte les assiettes vers la salle."""
    S = Scene()
    cuisine_resto(S)
    S.add(plan_travail(400, 800, 760))
    for k, x in enumerate((240, 340, 440)):
        S.add(assiette(x, 610, 0.9, "#fff", "#e8590c"), ellipse(x, 600, 22, 8, "#ff922b"))
    S.add(clochette(560, 612, 0.9))
    S.add(rosalie(150, 790, 1.3, expr="joie", bras="leve_doigt", regard=(1, 0)))
    serveur = dict(stature="adulte", peau="claire", cheveux="brun", coiffure="raie", habit="#ffffff", jambes="#212529",
                   tenue=g([rect(-34, -86, 68, 60, "#212529", rx=6), chemin("M -8 -106 L 0 -96 L 8 -106", stroke="#e03131", sw=6)]), robe=False)
    S.add(personne(680, 790, 1.3, expr="content", bras="porte", regard=(-1, 0), flip=True,
                   objet=place(assiette(0, 0, 0.8, "#fff", "#e8590c"), *ancre(0, -86, "porte", "adulte")), **serveur))
    S.add(texte(400, 300, "Service !", 70, "#c92a2a", contour="#fff"))
    return S


def p08():
    """Plan moyen : dans la salle, Théo et sa grand-mère mangent la soupe ; Théo dit : « Miam ! »."""
    S = Scene()
    salle_resto(S)
    S.add(table(400, 790, 520, 170, "#c68642", nappe="#ffe3e3"))
    S.add(personne(240, 640, 1.15, expr="miam", bras="porte", regard=(1, 0.3), **THEO))
    S.add(personne(560, 640, 1.1, expr="content", bras="mains_jointes", regard=(-1, 0.3), **MAMIE))
    S.add(table(400, 790, 520, 170, "#c68642", nappe="#ffe3e3"))
    S.add(bol(270, 610, 0.6, "#fff", "#ff922b", True), bol(530, 610, 0.6, "#fff", "#ff922b", False))
    S.add(tarte(400, 616, 0.55))
    S.add(bulle(260, 150, 240, 90, "Miam !", 44, pointe=(250, 390)))
    return S


def p09():
    """Plan moyen : après le service, la plongeuse lave une montagne de vaisselle ; tout le monde nettoie."""
    S = Scene()
    cuisine_resto(S)
    S.add(rect(420, 520, 340, 30, "#adb5bd", rx=6), rect(440, 550, 300, 90, "#ced4da", rx=10))
    for k in range(8):
        S.add(ellipse(560 + (k % 2) * 30, 510 - k * 18, 60, 10, "#fff", stroke="#ced4da", stroke_width=2))
    for x, y, r in ((470, 470, 14), (500, 440, 10), (680, 460, 16), (720, 430, 9), (620, 380, 12)):
        S.add(cercle(x, y, r, "#fff", stroke="#a5d8ff", stroke_width=2))
    S.add(personne(600, 790, 1.35, expr="rire", bras="porte", regard=(0, 0.5), **PLONGEUSE))
    S.add(rosalie(240, 790, 1.35, expr="content", bras="pousse", regard=(1, 0.5),
                  objet=vadrouille(*ancre(90, -114, "pousse", "adulte"))))
    S.add(bulle(260, 160, 360, 100, "Une cuisine propre,\nc'est important !", 30, pointe=(260, 420)))
    return S


def p10():
    """Gros plan : Rosalie pose une petite toque sur la tête de Théo."""
    S = Scene()
    salle_resto(S)
    S.add(personne(500, 800, 1.6, expr="rire", bras="joues", regard=(-1, -0.3), acc=("toque",), **THEO))
    S.add(rosalie(250, 800, 1.6, expr="content", bras="donne", regard=(1, 0)))
    S.camera(1.3, 380, 470)
    S.dessus(bulle(560, 110, 380, 100, "Plus tard, je serai\nchef, moi aussi !", 30, pointe=S.vers_page(500, 470)))
    S.cachette(634, 316, "air")
    return S


IMAGES = [
    ("couverture.svg", couverture), ("toque-seule.svg", vignette),
    ("01-le-marche.svg", p01), ("02-les-mains.svg", p02), ("03-la-brigade.svg", p03),
    ("04-l-oignon.svg", p04), ("05-gouter.svg", p05), ("06-la-tarte.svg", p06),
    ("07-service.svg", p07), ("08-miam.svg", p08), ("09-la-plonge.svg", p09),
    ("10-la-petite-toque.svg", p10),
]
