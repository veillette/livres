"""Les dents de Timéo — une première visite chez la dentiste."""
from base import *
from objets import *
from metiers import *
from base import _assombrir
from fables import fromage
from sciences import verre

ID = "chez-la-dentiste"
CLARA = dict(peau="doree", cheveux="noir", coiffure="chignon", habit="#66d9e8", jambes="#3bc9db",
             chaussures="#f8f9fa", tenue=badge(20, -90, "#ffffff", "rond"))
CLARA_MASQUE = dict(CLARA, coiffe=calot("#99e9f2") + masque_soin("#d0ebff"), coiffure="courts")
TIMEO = dict(peau="foncee", cheveux="noir", coiffure="boucles", habit="#fcc419", jambes="#1c7ed6",
             chaussures="#e03131")


def clara(x, y, s=1.6, masque=False, **k):
    return pro(x, y, s, **{**(CLARA_MASQUE if masque else CLARA), **k})


def timeo(x, y, s=1.2, **k):
    return petit(x, y, s, **{**TIMEO, **k})


def piece(S):
    cabinet(S, "#e6fcf5", "#c3fae8", 600, "#96f2d7")
    S.add(fenetre(60, 110, 170, 150, "#a5d8ff", rideaux="#63e6be", contenu=nuage(130, 200, 0.5)))


def fauteuil(x, y, couche=False, c="#1c7ed6"):
    """Fauteuil de dentiste vu de face ; couché, le dossier s'abaisse vers la gauche."""
    m = [rect(x - 60, y - 16, 120, 16, "#adb5bd", rx=6), rect(x - 14, y - 110, 28, 100, "#ced4da")]
    if couche:
        m += [rect(x - 200, y - 170, 400, 56, c, rx=24), rect(x - 250, y - 180, 70, 56, c, rx=24)]
    else:
        m += [rect(x - 110, y - 160, 220, 56, c, rx=24), rect(x - 100, y - 400, 200, 250, c, rx=30),
              rect(x - 60, y - 450, 120, 60, c, rx=24),
              rect(x - 140, y - 220, 40, 90, _assombrir(c, 0.85), rx=16), rect(x + 100, y - 220, 40, 90, _assombrir(c, 0.85), rx=16)]
    return g(m)


def scialytique(x, y, bras_x=None, allumee=True):
    """Grosse lampe accrochée au plafond ; (x, y) = centre de la lampe."""
    bx = x if bras_x is None else bras_x
    m = [trait(bx, 0, bx, y - 80, "#adb5bd", 10), trait(bx, y - 80, x, y - 30, "#adb5bd", 10)]
    if allumee:
        m.append(poly([(x - 60, y + 10), (x + 60, y + 10), (x + 120, y + 260), (x - 120, y + 260)], "#fff9db", opacity=0.5))
    m += [ellipse(x, y, 80, 34, "#e9ecef", stroke="#adb5bd", stroke_width=4),
          ellipse(x, y + 8, 60, 18, "#fff3bf" if allumee else "#dee2e6")]
    return g(m)


def miroir_dentaire(x, y, s=1.0, rot=0):
    return place([rect(-3, 0, 6, 80, "#adb5bd", rx=3), cercle(0, -6, 11, "#e7f5ff", stroke="#868e96", stroke_width=3)],
                 x, y, s, rot=rot)


def brosse_dents(x, y, s=1.0, rot=0, c="#e64980"):
    """Brosse à dents horizontale, la tête à droite ; (x, y) = bout du manche."""
    m = [rect(0, -8, 150, 16, c, rx=8), rect(130, -14, 46, 10, "#fff", rx=3, stroke="#ced4da", stroke_width=1.5)]
    for k in range(6):
        m.append(rect(134 + k * 7, -30, 4, 18, "#a5d8ff"))
    return place(m, x, y, s, rot=rot)


def dent(x, y, s=1.0, expr="content", brille=True):
    """Une dent souriante."""
    m = [chemin("M -50 -40 Q -60 -90 -20 -90 Q 0 -80 20 -90 Q 60 -90 50 -40 Q 46 0 36 50 Q 28 70 18 50 Q 10 20 0 20 "
                "Q -10 20 -18 50 Q -28 70 -36 50 Q -46 0 -50 -40 Z", "#fff", stroke="#ced4da", sw=4)]
    ys, bs, _ = EXPRESSIONS[expr]
    m.append(oeil(-16, -42, ys) + oeil(16, -42, ys))
    m.append(bouche(0, -20, bs))
    m.append(ellipse(-32, -26, 8, 5, ROSE, opacity=0.6) + ellipse(32, -26, 8, 5, ROSE, opacity=0.6))
    if brille:
        m.append(eclat(52, -82, 0.5, "#74c0fc"))
    return place(m, x, y, s)


def arcade(cx, cy, rx, ry, nb=10, haut=True, w=26, h=34):
    """Rangée de dents en arc ; haut=True : dents du haut."""
    m = []
    for k in range(nb):
        a = math.radians(200 + k * 140 / (nb - 1)) if haut else math.radians(160 - k * 140 / (nb - 1))
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a) * (1 if haut else 1)
        larg = w * (1.25 if k in (nb // 2 - 1, nb // 2) else 1.0)
        m.append(rect(x - larg / 2, y - h / 2, larg, h, "#fff", rx=9, stroke="#ced4da", stroke_width=2))
    return g(m)


def machoire(x, y, s=1.0):
    """Grande mâchoire de démonstration : gencives roses et 20 dents."""
    m = [ellipse(0, -60, 150, 62, "#ffa8a8"), ellipse(0, 60, 150, 62, "#ffa8a8"),
         ellipse(0, -48, 118, 40, "#e64980", opacity=0.25), ellipse(0, 48, 118, 40, "#e64980", opacity=0.25),
         arcade(0, -10, 120, 46, 10, True), arcade(0, 10, 120, 46, 10, False)]
    return place(m, x, y, s)


def sablier(x, y, s=1.0):
    return place([rect(-40, -150, 80, 12, "#c68642", rx=4), rect(-40, -12, 80, 12, "#c68642", rx=4),
                  chemin("M -32 -138 L 32 -138 L 4 -76 L 32 -12 L -32 -12 L -4 -76 Z", "#e7f5ff", stroke="#adb5bd", sw=3),
                  poly([(-14, -110), (14, -110), (2, -80), (-2, -80)], "#fcc419"),
                  poly([(-22, -12), (22, -12), (0, -40)], "#fcc419"), trait(0, -78, 0, -14, "#fcc419", 2)], x, y, s)


def brosse_bouche(x, y, s, c="#e64980"):
    """Brosse tenue dans la bouche d'un enfant dessiné en (x, y) à l'échelle s."""
    k = s * 0.5
    return brosse_dents(x + 172 * k, y - 122 * s, k, rot=180, c=c)


def bonbon(x, y, s=1.0, c="#e64980", rot=0):
    return place([poly([(-30, -14), (-14, 0), (-30, 14)], c), poly([(30, -14), (14, 0), (30, 14)], c),
                  ellipse(0, 0, 18, 14, c), chemin("M -8 -8 Q 0 0 -6 8", stroke="#fff", sw=3)], x, y, s, rot=rot)


def salle_de_bain(S):
    interieur(S, "#e7f5ff", "#dee2e6", 620, plinthe="#ced4da")
    for x in range(0, 800, 50):
        S.add(trait(x, 0, x, 606, "#d0ebff", 2))
    for y in range(50, 600, 50):
        S.add(trait(0, y, 800, y, "#d0ebff", 2))


def couverture():
    S = Scene()
    piece(S)
    S.add(clara(220, 780, 1.85, expr="content", bras="salut", objet=""))
    S.add(miroir_dentaire(220 + 72 * 1.85, 780 - 160 * 1.85, 1.2, rot=10))
    S.add(timeo(530, 780, 1.5, expr="rire", bras="tient"))
    S.add(brosse_dents(530 + 68 * 1.5 - 20, 780 - 146 * 1.5 + 40, 1.3, rot=-80))
    S.add(eclat(680, 330, 0.7, "#74c0fc"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(dent(170, 175, 1.25))
    S.add(brosse_dents(230, 250, 0.9, rot=-70))
    S.add(eclat(320, 60, 0.6, "#74c0fc"))
    return S


def p01():
    S = Scene()
    salle_de_bain(S)
    S.add(rect(420, 110, 260, 300, "#e7f5ff", rx=20, stroke="#adb5bd", stroke_width=10))
    S.add(rect(400, 470, 300, 40, "#f8f9fa", rx=14), rect(520, 510, 60, 110, "#f1f3f5"))
    S.add(tasse(470, 470, 0.9, "#74c0fc"))
    S.add(timeo(330, 780, 1.6, expr="inquiet", bras="bouche", regard=(1, 0)))
    S.add(brosse_bouche(330, 780, 1.6))
    S.add(pensee(170, 170, 110, texte(170, 160, "Ça fait", 34, "#1c7ed6") + texte(170, 202, "mal ?", 34, "#1c7ed6"),
                 depuis=(290, 400)))
    return S


def p02():
    S = Scene()
    piece(S)
    S.add(fauteuil(560, 760))
    S.add(clara(230, 780, 1.75, expr="content", bras="montre", regard=(1, 0)))
    S.add(timeo(400, 790, 1.15, expr="surpris", bras="bas", regard=(1, -0.5)))
    S.add(bulle(360, 110, 340, 90, "Installe-toi !", 40, pointe=(260, 320)))
    return S


def p03():
    S = Scene()
    piece(S)
    S.add(fauteuil(430, 760, couche=True))
    S.add(timeo(410, 600, 1.25, expr="rire", bras="haut", rot=-90))
    S.add(texte(560, 330, "Bzzz…", 60, "#1c7ed6", contour="#fff"))
    from sciences import fleche
    S.add(fleche(650, 520, 650, 420, "#1c7ed6"))
    return S


def p04():
    S = Scene()
    piece(S)
    S.add(scialytique(440, 170, bras_x=640))
    S.add(fauteuil(400, 790, couche=True))
    S.add(timeo(380, 630, 1.25, expr="bouche_bee", bras="bas", rot=-90))
    S.add(clara(610, 790, 1.7, masque=True, expr="sourire", bras="donne", flip=True, regard=(-1, 0.5)))
    S.add(miroir_dentaire(610 - 84 * 1.7, 790 - 92 * 1.7, 1.2, rot=-70))
    S.cachette(490, 70, "air")
    return S


def p05():
    S = Scene()
    piece(S)
    S.add(rect(240, 70, 500, 380, "#fff", rx=24, stroke="#96f2d7", stroke_width=6))
    S.add(arcade(490, 250, 170, 100, 10, True, 30, 40), arcade(490, 270, 170, 100, 10, False, 30, 40))
    S.add(texte(490, 285, "20", 80, "#0ca678"))
    S.add(clara(150, 790, 1.6, expr="content", bras="montre", regard=(1, -1)))
    S.add(timeo(560, 790, 1.25, expr="rire", bras="haut"))
    return S


def p06():
    S = Scene()
    piece(S)
    S.add(machoire(430, 330, 1.2))
    S.add(brosse_dents(560, 470, 1.6, rot=-150, c="#20c997"))
    S.add(chemin("M 300 330 a 30 30 0 1 1 1 1", stroke="#0ca678", sw=5))
    S.add(clara(150, 790, 1.6, expr="sourire", bras="montre", regard=(1, -1)))
    S.add(timeo(650, 790, 1.2, expr="bouche_bee", bras="bas", regard=(-1, -1)))
    return S


def p07():
    S = Scene()
    piece(S)
    S.add(fauteuil(400, 790, couche=True))
    S.add(timeo(380, 630, 1.25, expr="rire", bras="bas", rot=-90))
    S.add(clara(640, 790, 1.6, masque=True, expr="content", bras="donne", flip=True, regard=(-1, 0.5)))
    S.add(rect(640 - 84 * 1.6 - 70, 790 - 92 * 1.6 - 8, 80, 16, "#ced4da", rx=6))
    for k in range(5):
        S.add(goutte(330 + k * 22, 420 - (k % 2) * 20, 0.4, "#74c0fc"))
    S.add(texte(220, 300, "Pschitt !", 50, "#1c7ed6", contour="#fff", rot=-10))
    S.add(texte(600, 300, "Slurp !", 50, "#0ca678", contour="#fff", rot=8))
    S.cachette(490, 70, "air")
    return S


def p08():
    S = Scene()
    piece(S)
    S.add(rect(60, 330, 300, 230, "#ebfbee", rx=24, stroke="#69db7c", stroke_width=5))
    S.add(texte(210, 380, "Tous les jours", 30, "#2b8a3e"))
    S.add(pomme(120, 480, 1.3), fromage(220, 500, 0.8), verre(300, 530, 60, 90, niveau=0.7))
    S.add(rect(440, 330, 300, 230, "#fff0f6", rx=24, stroke="#f783ac", stroke_width=5))
    S.add(texte(590, 380, "Jours de fête", 30, "#c2255c"))
    S.add(bonbon(510, 470, 1.0), bonbon(600, 500, 1.0, "#7950f2", rot=30), bonbon(680, 460, 1.0, "#fd7e14", rot=-20))
    S.add(clara(400, 790, 1.15, expr="content", bras="ouverts"))
    S.add(timeo(140, 790, 0.95, expr="joie", bras="bas", regard=(1, -1)))
    return S


def p09():
    S = Scene()
    salle_de_bain(S)
    S.add(soleil(120, 130, 50), lune(680, 130, 44))
    S.add(texte(120, 260, "matin", 36, "#f08c00"), texte(680, 260, "soir", 36, "#5c7cfa"))
    S.add(timeo(380, 790, 1.7, expr="concentre", bras="bouche", regard=(1, 0)))
    S.add(brosse_bouche(380, 790, 1.7, "#20c997"))
    S.add(sablier(640, 640, 1.2), texte(640, 430, "2 minutes", 32, "#0ca678"))
    return S


def p10():
    S = Scene()
    salle_de_bain(S)
    S.add(rect(380, 100, 320, 340, "#e7f5ff", rx=20, stroke="#adb5bd", stroke_width=10))
    S.add(rect(400, 470, 280, 40, "#f8f9fa", rx=14))
    S.add(timeo(260, 790, 1.75, expr="rire", bras="tient", regard=(1, 0)))
    S.add(brosse_dents(260 + 68 * 1.75 - 20, 790 - 146 * 1.75 + 50, 1.1, rot=-80, c="#20c997"))
    S.add(bulle(540, 200, 360, 90, "Même pas peur !", 38))
    S.add(eclat(150, 260, 0.7, "#74c0fc"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("dent-seule.svg", vignette),
    ("01-brossage.svg", p01), ("02-fauteuil.svg", p02), ("03-fauteuil-magique.svg", p03),
    ("04-petit-miroir.svg", p04), ("05-vingt-dents.svg", p05), ("06-machoire-geante.svg", p06),
    ("07-pschitt.svg", p07), ("08-amis-des-dents.svg", p08), ("09-deux-minutes.svg", p09),
    ("10-meme-pas-peur.svg", p10),
]
