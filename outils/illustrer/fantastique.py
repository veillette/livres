"""
Personnages et décors des contes : princesses, princes, rois et reines,
chevaliers, fées, sorcières, sirènes, géants, dragons, licornes, étoiles
qui parlent, châteaux, fonds marins…

Même conventions que `base.py` : page de 800 × 800, personnages dessinés de
face, les pieds en (0, 0) et la tête vers y = -150.

    S.add(personne(400, 740, 1.5, coiffure="longs", habit="#f783ac",
                   acc=("couronne",), expr="rire", bras="haut"))
"""
from base import *
from base import POSES, COUDES, DEVANT_VISAGE, EXPRESSIONS, INCLINE, PAS_POSE, PENCHE, _bras, _main, _assombrir, _cachettes_sol

PEAUX = {
    "claire": "#fbd9bd",
    "rosee": "#f3c3a0",
    "doree": "#dca36f",
    "brune": "#a86a3f",
    "foncee": "#6f4428",
}
CHEVEUX = {
    "blond": "#f6c453",
    "roux": "#e8590c",
    "chatain": "#8d5524",
    "brun": "#4a2c17",
    "noir": "#2b2b3a",
    "blanc": "#e9ecef",
    "gris": "#adb5bd",
}
OR = "#ffd43b"
OR_FONCE = "#f59f00"


# ---------------------------------------------------------------------------
# Personnages humains
# ---------------------------------------------------------------------------

def _cheveux_derriere(coiffure, c):
    """Cheveux placés derrière la tête (et parfois derrière le corps)."""
    if coiffure == "longs":
        return chemin("M -58 -156 Q -70 -96 -56 -70 Q 0 -60 56 -70 Q 70 -96 58 -156 Z", c)
    if coiffure == "tres_longs":
        return chemin("M -58 -156 Q -76 -70 -62 -24 Q 0 -10 62 -24 Q 76 -70 58 -156 Z", c)
    if coiffure == "queue":
        return chemin("M 40 -186 Q 96 -190 86 -120 Q 80 -90 96 -70 Q 60 -80 62 -120 Q 64 -160 40 -170 Z", c)
    if coiffure == "tresses":
        m = []
        for sgn in (-1, 1):
            for k in range(4):
                m.append(ellipse(sgn * 54, -128 + k * 20, 12, 13, c))
            m.append(poly([(sgn * 48, -54), (sgn * 60, -54), (sgn * 54, -42)], c))
            m.append(rect(sgn * 54 - 9, -66, 18, 8, "#fa5252", rx=4))
        return g(m)
    if coiffure == "boucles":
        m = []
        for k in range(12):
            a = math.radians(-200 + k * 20)
            m.append(cercle(math.cos(a) * 54, -150 + math.sin(a) * 54, 20, c))
        for sgn in (-1, 1):
            m.append(cercle(sgn * 56, -110, 18, c))
            m.append(cercle(sgn * 50, -90, 15, c))
        return g(m)
    if coiffure == "chignon":
        return cercle(0, -210, 26, c)
    if coiffure == "carre":
        return chemin("M -60 -158 Q -68 -112 -60 -96 Q -40 -92 -30 -100 L 30 -100 Q 40 -92 60 -96 Q 68 -112 60 -158 Z", c)
    if coiffure == "afro":
        m = [cercle(0, -164, 72, c)]
        for k in range(14):
            a = math.radians(k * 360 / 14)
            m.append(cercle(math.cos(a) * 66, -164 + math.sin(a) * 64, 16, c))
        return g(m)
    if coiffure == "couettes":
        m = []
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 74, -164, 18, 32, c, rot=sgn * 35))
            m.append(chemin(f"M {sgn * 66} -150 Q {sgn * 84} -156 {sgn * 88} -184", stroke=_assombrir(c, 0.78), sw=2.5, opacity=0.7))
        return g(m)
    if coiffure == "sorciere":
        return chemin("M -56 -160 Q -84 -110 -74 -60 Q -60 -80 -52 -100 Q -46 -80 -40 -96 L 40 -96 Q 46 -80 52 -100 Q 60 -80 74 -60 Q 84 -110 56 -160 Z", c)
    return ""


def _cheveux_devant(coiffure, c):
    """Frange et dessus de la tête."""
    if coiffure in ("chauve", "aucun"):
        return ""
    if coiffure == "chauve_cote":
        return g([ellipse(-48, -150, 12, 22, c), ellipse(48, -150, 12, 22, c)])
    if coiffure == "courts":
        return g([chemin("M -52 -146 Q -58 -208 0 -208 Q 58 -208 52 -146 Q 46 -170 24 -176 Q 30 -186 18 -188 Q 6 -174 -20 -178 Q -44 -174 -52 -146 Z", c),
                  _meches(c)])
    if coiffure == "boucles":
        m = []
        for k in range(7):
            a = math.radians(-165 + k * 25)
            m.append(cercle(math.cos(a) * 44, -160 + math.sin(a) * 40, 19, c))
        return g(m)
    if coiffure == "carre":
        return g([chemin("M -56 -142 Q -62 -212 0 -212 Q 62 -212 56 -142 L 52 -166 Q 26 -172 0 -170 Q -26 -172 -52 -166 Z", c),
                  _meches(c)])
    if coiffure == "afro":
        m = [chemin("M -54 -144 Q -64 -220 0 -220 Q 64 -220 54 -144 Q 44 -176 0 -180 Q -44 -176 -54 -144 Z", c)]
        fonce = _assombrir(c, 0.75)
        for k in range(9):
            a = math.radians(-160 + k * 17.5)
            m.append(cercle(math.cos(a) * 44, -168 + math.sin(a) * 34, 3, fonce, opacity=0.5))
        return g(m)
    if coiffure == "raie":
        return g([chemin("M -52 -146 Q -60 -208 -12 -210 Q 58 -212 54 -146 Q 48 -176 20 -188 Q 2 -186 -14 -198 Q -40 -182 -52 -146 Z", c),
                  chemin("M -14 -198 Q -10 -208 -4 -210", stroke=_assombrir(c, 0.7), sw=2.5, opacity=0.8),
                  chemin("M 0 -204 Q 24 -206 38 -190", stroke=eclaircir(c, 0.45), sw=4, opacity=0.7)])
    if coiffure == "herisses":
        return chemin("M -52 -150 L -56 -184 L -36 -176 L -30 -212 L -10 -186 L 4 -218 L 16 -186 L 36 -208 L 36 -176 L 56 -182 L 52 -150 Q 30 -172 0 -172 Q -30 -172 -52 -150 Z", c)
    # frange arrondie commune (longs, tres_longs, queue, tresses, chignon, sorciere)
    return g([chemin("M -54 -144 Q -60 -210 0 -210 Q 60 -210 54 -144 Q 50 -168 30 -178 Q 22 -164 4 -178 Q -12 -164 -24 -178 Q -46 -170 -54 -144 Z", c),
              _meches(c)])


def _meches(c):
    """Quelques mèches plus foncées et un reflet sur le dessus des cheveux."""
    fonce = _assombrir(c, 0.78)
    return g([chemin("M -36 -190 Q -20 -202 -4 -200", stroke=eclaircir(c, 0.45), sw=5, opacity=0.8),
              chemin("M -40 -168 Q -36 -188 -16 -196", stroke=fonce, sw=2.5, opacity=0.8),
              chemin("M 14 -196 Q 36 -192 42 -170", stroke=fonce, sw=2.5, opacity=0.8),
              chemin("M 2 -204 Q 12 -196 14 -184", stroke=fonce, sw=2.5, opacity=0.8)])


def _chapeau_pointu(c, bande="#9775fa"):
    return g([ellipse(0, -196, 86, 16, c),
              chemin("M -46 -198 Q -30 -260 -4 -300 Q 18 -334 58 -326 Q 22 -312 28 -262 Q 34 -228 46 -198 Z", c),
              chemin("M -44 -206 Q 0 -218 44 -206 L 42 -196 Q 0 -206 -42 -196 Z", bande),
              etoile5(20, -250, 10, OR)])


def _casque_chevalier(c="#ced4da", plumet="#fa5252"):
    fonce = _assombrir(c, 0.8)
    return g([chemin("M 0 -206 Q 18 -250 50 -244 Q 26 -236 20 -206 Z", plumet),
              chemin("M -58 -146 Q -62 -212 0 -214 Q 62 -212 58 -146 L 46 -146 L 46 -174 L -46 -174 L -46 -146 Z", c),
              rect(-58, -180, 116, 12, fonce, rx=6),
              trait(0, -212, 0, -182, fonce, 5),
              rect(-60, -150, 16, 40, c, rx=6), rect(44, -150, 16, 40, c, rx=6)])


def _couronne_tete(ca=OR, grande=False):
    k = 1.25 if grande else 1.0
    pts = [(-34, -196), (-34, -232), (-17, -212), (0, -240), (17, -212), (34, -232), (34, -196)]
    pts = [(x * k, -196 + (y + 196) * k) for x, y in pts]
    return g([poly(pts, ca, stroke=OR_FONCE, stroke_width=3),
              cercle(0, -208, 5, "#fa5252"), cercle(-20 * k, -204, 4, "#4dabf7"), cercle(20 * k, -204, 4, "#4dabf7")])


def _diademe(ca=OR):
    return g([chemin("M -40 -190 Q 0 -206 40 -190", stroke=ca, sw=6),
              poly([(-12, -198), (0, -222), (12, -198)], ca, stroke=OR_FONCE, stroke_width=2),
              cercle(0, -206, 5, "#e64980")])


def _barbe(c):
    return g([chemin("M -48 -146 Q -52 -96 -20 -76 Q 0 -60 20 -76 Q 52 -96 48 -146 Q 40 -116 20 -112 Q 0 -104 -20 -112 Q -40 -116 -48 -146 Z", c),
              chemin("M -26 -126 Q -12 -136 0 -128 Q 12 -136 26 -126 Q 14 -118 0 -122 Q -14 -118 -26 -126 Z", _assombrir(c, 0.9))])


def _ailes_fee(c="#d0ebff"):
    m = []
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 66, -130, 44, 64, c, rot=sgn * 30, opacity=0.8, stroke="#a5d8ff", stroke_width=3))
        m.append(ellipse(sgn * 58, -64, 30, 40, c, rot=sgn * -30, opacity=0.8, stroke="#a5d8ff", stroke_width=3))
    return g(m)


def _queue_sirene(c, c2):
    fonce = _assombrir(c, 0.8)
    m = [chemin("M -40 -96 Q -52 -40 -20 -10 Q 0 10 18 30 L 30 20 Q 40 -20 40 -96 Z", c)]
    for k in range(4):
        yy = -80 + k * 20
        m.append(chemin(f"M {-32 + k * 4} {yy} q 10 8 20 0 q 10 8 20 0", stroke=fonce, sw=3))
    m.append(chemin("M 20 22 Q -20 30 -44 16 Q -20 54 22 34 Q 50 60 84 44 Q 56 30 30 22 Z", c2))
    return g(m)


# Stature : (largeur du corps, hauteur du corps, taille de la tête). Les
# adultes ont un corps plus long et une tête un peu plus petite que les
# enfants ; les tout-petits, des jambes courtes.
STATURES = {
    "petit": (0.94, 0.82, 1.0),
    "enfant": (1.0, 1.0, 1.0),
    "ado": (1.0, 1.16, 0.95),
    "adulte": (1.06, 1.3, 0.9),
    "ancien": (1.08, 1.2, 0.9),
}
CARRURES = {"fine": 0.86, "normale": 1.0, "ronde": 1.24}
COU = -112          # jonction du cou et de la tête (repère local)


def _etire(pt, lx, ly, kh):
    """Point du repère « enfant » → repère du personnage selon sa stature :
    au-dessus du cou, il suit la tête ; en dessous, le corps."""
    if pt is None:
        return None
    x, y = pt
    if y < COU:
        x, y = x * kh, COU * ly + (y - COU) * kh
    else:
        x, y = x * lx, y * ly
    return tuple(int(v) if float(v).is_integer() else round(v, 1) for v in (x, y))


def mains_personne(x, y, s=1.0, bras="bas", flip=False, stature="enfant", carrure="normale"):
    """Position (dans la page) des mains d'un personnage humain."""
    lx, ly, kh = STATURES[stature]
    lx *= CARRURES[carrure]
    out = []
    for main in POSES[bras]:
        hx, hy = _etire(main, lx, ly, kh)
        out.append((x + (-hx if flip else hx) * s, y + hy * s))
    if flip:
        out.reverse()
    return out


def ancre(x, y, bras="tient", stature="enfant", carrure="normale", main=1):
    """Point (x, y) d'un objet tenu, placé pour un enfant, recalé pour une autre
    stature : l'objet suit la main (main = 0 gauche, 1 droite)."""
    lx, ly, kh = STATURES[stature]
    h0 = POSES[bras][main]
    h1 = _etire(h0, lx * CARRURES[carrure], ly, kh)
    return x + h1[0] - h0[0], y + h1[1] - h0[1]


def _nez(style, p, bord_p):
    if style == "rond":
        return g([ellipse(0, -134, 7.5, 6, _assombrir(p, 0.9)), ellipse(-2, -136, 2.5, 1.8, "#fff", opacity=0.45)])
    if style == "pointu":
        return chemin("M -1 -144 Q 7 -134 0 -130", stroke=bord_p, sw=3)
    if style == "long":
        return chemin("M -2 -148 Q 9 -134 -1 -128 Q -4 -128 -5 -131", stroke=bord_p, sw=3)
    if style == "retrousse":
        return g([chemin("M -5 -134 Q 0 -128 5 -134", stroke=bord_p, sw=3), cercle(0, -137, 3, _assombrir(p, 0.92))])
    return chemin("M -4 -134 Q 0 -130 4 -134", stroke=bord_p, sw=3)


def personne(x=0, y=0, s=1.0, peau="rosee", cheveux="chatain", coiffure="longs", habit="#f783ac",
             robe=True, jambes="#495057", chaussures=None, expr="sourire", bras="bas", regard=(0, 0),
             flip=False, acc=(), couleur_acc=OR, objet=None, derriere=None, larmes=False, rot=0,
             barbe=None, cape=None, sirene=None, motif_robe=None, joues=True, sy=None, ailes=None,
             ceinture=None, tenue=None, coiffe=None, pas=None, penche=None, ombre=None,
             stature="enfant", carrure="normale", nez="petit", yeux="ronds", taches=False, rides=None):
    """Un personnage humain vu de face (princesse, prince, roi, fée, sorcière…).

    peau / cheveux : clé de PEAUX / CHEVEUX ou couleur ; coiffure : "longs",
    "tres_longs", "queue", "tresses", "boucles", "chignon", "courts", "herisses",
    "carre", "afro", "couettes", "raie", "sorciere", "chauve", "chauve_cote".
    robe : True (robe évasée) ou False (tunique et pantalon `jambes`).
    acc : "couronne", "grande_couronne", "diademe", "chapeau_pointu", "casque",
          "noeud", "fleur", "bonnet_nuit", "toque", "lunettes", "col".
    cape : couleur d'une cape ; barbe : couleur d'une barbe ;
    sirene : (couleur, couleur_nageoire) remplace les jambes par une queue ;
    ailes : couleur d'ailes de fée.
    tenue : dessin (coordonnées locales) posé sur le vêtement, sous les bras
            (blouse, gilet, badge…) ; coiffe : dessin posé sur la tête, par-dessus
            les cheveux (casque, casquette, masque…).
    pas : "marche", "pointe" ou "saute" (déduit de la pose si absent) ;
    penche : inclinaison de la tête en degrés (déduite de l'expression si
    absente) ; ombre : ombre douce au sol.
    stature : clé de STATURES ("petit", "enfant", "ado", "adulte", "ancien") ;
    carrure : "fine", "normale" ou "ronde" ; nez : "petit", "rond", "pointu",
    "long" ou "retrousse" ; yeux : "ronds", "petits" ou "cils" ; taches :
    taches de rousseur ; rides : petites rides (par défaut pour "ancien").
    Avec une autre stature que "enfant", placer les objets tenus d'après
    mains_personne().
    """
    p = PEAUX.get(peau, peau)
    ch = CHEVEUX.get(cheveux, cheveux)
    chaussures = chaussures or _assombrir(habit, 0.7)
    ys, bs, ss = EXPRESSIONS[expr]
    if pas is None:
        pas = PAS_POSE.get(bras)
    devant = bras in DEVANT_VISAGE
    if penche is None:
        penche = 0 if devant or bras in ("porte", "tete") or sirene else PENCHE.get(expr, 0)
    lx, ly, kh = STATURES[stature]
    lx *= CARRURES[carrure]
    etire = (lx, ly, kh) != (1.0, 1.0, 1.0)
    if rides is None:
        rides = stature == "ancien"

    def tourne(contenu):
        return g(contenu, f"rotate({n(penche)} 0 -112)") if penche else contenu

    def corps(contenu):
        """Vêtement, jambes, cou : étirés selon la stature et la carrure."""
        return g(contenu, f"scale({n(lx, 3)} {n(ly, 3)})") if etire else g(contenu)

    def tete(contenu):
        """Tête et cheveux : posés sur le cou, à leur taille."""
        contenu = tourne(contenu)
        if not etire:
            return contenu
        return g(contenu, f"translate(0 {n(COU * ly, 2)}) scale({n(kh, 3)}) translate(0 {-COU})")

    fonce_h = _assombrir(habit, 0.75)
    # vue de trois quarts quand le regard part de côté ; corps penché selon la pose
    tourne_ = max(-1.0, min(1.0, regard[0])) * 9
    incline = 0 if rot or sirene else INCLINE.get(bras, 0) + (4 if stature == "ancien" else 0)
    m = []
    if derriere:
        m.append(derriere)
    arriere = []
    if ailes:
        arriere.append(_ailes_fee(ailes))
    if cape:
        arriere.append(chemin("M -34 -106 Q -76 -40 -72 -4 L 72 -4 Q 76 -40 34 -106 Z", cylindre(cape, 0.2, 0.72)))
        arriere.append(chemin("M -40 -60 Q -52 -30 -54 -6 M 40 -60 Q 52 -30 54 -6", stroke=_assombrir(cape, 0.8), sw=3))
    if arriere:
        m.append(corps(arriere))
    m.append(tete(_cheveux_derriere(coiffure, ch)))

    # --- jambes, robe ou queue de sirène
    haut_corps = None
    c = []
    if sirene:
        c.append(_queue_sirene(*sirene))
        c.append(ellipse(0, -80, 34, 30, p))
        c.append(g([cercle(-14, -92, 11, sirene[1]), cercle(14, -92, 11, sirene[1])]))
    elif robe:
        m += _chaussures(pas, chaussures, 14, 8, 16 * lx, -6)
        forme = "M -26 -106 Q 0 -112 26 -106 L 32 -74 Q 60 -34 66 -12 Q 0 2 -66 -12 Q -60 -34 -32 -74 Z"
        c.append(chemin(forme, cylindre(habit, 0.24, 0.78)))
        if motif_robe:
            c.append(chemin("M -66 -12 Q 0 2 66 -12 L 64 -22 Q 0 -8 -64 -22 Z", motif_robe))
            for k in range(-2, 3):
                c.append(etoile5(k * 22, -46 + abs(k) * 4, 5, motif_robe))
        # plis de la jupe et modelé
        for x0, x1 in ((-14, -30), (0, 0), (14, 30)):
            c.append(chemin(f"M {x0} -70 Q {n((x0 + x1) / 2 + (x1 - x0) * 0.1)} -40 {x1} -8", stroke=fonce_h, sw=2.5, opacity=0.45))
        c.append(ombrage(chemin(forme, "#000"), sombre=[(54, -40, 34, 70), (0, -6, 70, 10)], clair=[(-24, -90, 6, 12, 20), (-48, -36, 4, 22, 30)],
                         reflets=[(64, -24, 8, 30, -30)]))
        haut = [rect(-32, -80, 64, 10, ceinture or _assombrir(habit, 0.85), rx=5),
                chemin("M -20 -106 Q 0 -94 20 -106", stroke=fonce_h, sw=2.5)]
    else:
        jambe_d = rect(6, -52, 20, 46, cylindre(jambes, 0.25, 0.7), rx=8)
        c.append(rect(-26, -52, 20, 46, cylindre(jambes, 0.25, 0.7), rx=8))
        c.append(trait(-16, -40, -16, -12, _assombrir(jambes, 0.8), 2, opacity=0.6))
        if pas in ("marche", "pointe"):
            c.append(g(jambe_d, "rotate(-22 16 -50)"))
        elif pas == "court":
            # genou plié, pied ramené derrière
            c.append(g(rect(31, -33, 16, 22, cylindre(_assombrir(jambes, 0.9), 0.25, 0.7), rx=8), "rotate(20 39 -31)"))
            c.append(g(rect(6, -54, 20, 32, cylindre(jambes, 0.25, 0.7), rx=9), "rotate(-50 16 -50)"))
        else:
            c.append(jambe_d)
            c.append(trait(16, -40, 16, -12, _assombrir(jambes, 0.8), 2, opacity=0.6))
        m.append(corps(c))
        c = []
        m += _chaussures(pas, chaussures, 16, 9, 17 * lx, -6)
        forme = "M -32 -106 Q 0 -112 32 -106 L 40 -46 Q 0 -36 -40 -46 Z"
        haut = [chemin(forme, cylindre(habit, 0.24, 0.78)),
                ombrage(chemin(forme, "#000"), sombre=[(40, -70, 22, 46), (0, -40, 44, 8)], clair=[(-22, -92, 6, 11, 20), (-33, -70, 3, 16, 6)],
                        reflets=[(42, -66, 6, 30)]),
                chemin("M -20 -106 Q 0 -92 20 -106", stroke=fonce_h, sw=2.5),
                rect(-38, -62, 76, 10, ceinture or _assombrir(habit, 0.75), rx=5)]
        if ceinture:
            haut.append(rect(-8, -64, 16, 14, OR, rx=3))
    if c:
        m.append(corps(c))
    if not sirene:
        haut_corps = len(m)
        if "col" in acc:
            haut.append(chemin("M -30 -108 Q 0 -86 30 -108 Q 0 -96 -30 -108 Z", "#fff"))
        if tenue:
            haut.append(tenue)
        m.append(corps(haut))
    elif "col" in acc or tenue:
        m.append(corps([chemin("M -30 -108 Q 0 -86 30 -108 Q 0 -96 -30 -108 Z", "#fff") if "col" in acc else "", tenue or ""]))

    # --- bras (calculés dans le repère du personnage : ils ne se déforment pas)
    main_g, main_d = POSES[bras]
    coude_g, coude_d = COUDES.get(bras, (None, None))
    if bras == "croises":
        coude_g, coude_d = (-40, -60), (40, -64)
    main_g, main_d = _etire(main_g, lx, ly, kh), _etire(main_d, lx, ly, kh)
    coude_g, coude_d = _etire(coude_g, lx, ly, kh), _etire(coude_d, lx, ly, kh)
    ex_, ey_ = _etire((28, -98), lx, ly, kh)
    manche = p if sirene else habit
    bord = _assombrir(manche, 0.72)
    poignet = None if sirene else _assombrir(habit, 0.82)
    lb = 14 * (1 + (lx - 1) * 0.5)
    bras_svg = (_bras(-ex_, ey_, main_g, coude_g, manche, lb, bord=bord, poignet=poignet)
                + _bras(ex_, ey_, main_d, coude_d, manche, lb, bord=bord, poignet=poignet))
    bord_p = _assombrir(p, 0.8)
    rm = 10.5 * (1.08 if stature in ("adulte", "ancien") else 1)
    mains_svg = _main(*main_g, rm, p, bord_p) + _main(*main_d, rm, p, bord_p)
    if not devant:
        m.append(bras_svg)
        if objet:
            m.append(objet)
        m.append(mains_svg)
    elif objet:
        m.append(objet)

    # --- cou et tête
    m.append(corps([rect(-9, -116, 18, 16, p), ellipse(0, -106, 10, 4, _assombrir(p, 0.8), opacity=0.7)]))
    t = []
    oreilles = []
    for sgn in (-1, 1):
        oreilles.append(cercle(sgn * 49, -148, 11, p))
        oreilles.append(chemin(f"M {sgn * 50} -154 Q {sgn * 55} -148 {sgn * 50} -142", stroke=bord_p, sw=2.5))
    t.append(g(oreilles, f"translate({n(-tourne_ * 0.45)} 0)") if tourne_ else g(oreilles))
    t.append(cercle(0, -150, 50, volume(p, 0.25, 0.84)))
    t.append(ombrage(cercle(0, -150, 50, "#000"), sombre=[(36, -124, 40, 38)], clair=[(-22, -180, 13, 7, -30)], opacite=0.07,
                     reflets=[(51, -140, 8, 26, -15)]))
    debut_visage = len(t)
    if barbe:
        t.append(_barbe(barbe))
    if joues:
        rouge = expr in ("fache", "furieux", "timide")
        jc = "#ff6b6b" if expr in ("fache", "furieux") else ROSE
        jr = 1.3 if rouge else 1.0
        for sgn in (-1, 1):
            t.append(ellipse(sgn * 30, -128, 9 * jr, 5.5 * jr, jc, opacity=0.6))
    if taches:
        tc = _assombrir(p, 0.72)
        for sgn in (-1, 1):
            for dx, dy in ((22, -134), (30, -138), (36, -131), (26, -128), (16, -137)):
                t.append(cercle(sgn * dx, dy, 1.6, tc, opacity=0.75))
    t.append(yeux_trois_quarts(18, -150, ys, regard, tourne=tourne_, taille=0.82 if yeux == "petits" else 1.0))
    if yeux == "cils" and ys in ("normal", "grand", "bas"):
        # deux cils au coin extérieur de chaque œil (l'œil lointain, en trois
        # quarts, est plus petit et plus près du nez : voir yeux_trois_quarts)
        k = min(abs(tourne_) / 10, 1) * 0.16
        loin = -1 if tourne_ > 0 else 1
        for sgn in (-1, 1):
            f = 1 - k if (tourne_ and sgn == loin) else 1
            ox = sgn * (18 * f + 5.5 * f)
            t.append(chemin(f"M {n(ox)} -155 l {n(sgn * 4 * f)} {n(-4 * f)} M {n(ox + sgn * 1.5)} -150 l {n(sgn * 5 * f)} {n(-1.5 * f)}",
                            stroke=ENCRE, sw=2))
    if rides:
        rc = _assombrir(p, 0.78)
        for sgn in (-1, 1):
            t.append(chemin(f"M {sgn * 34} -156 l {sgn * 6} -2 M {sgn * 34} -150 l {sgn * 7} 1", stroke=rc, sw=1.8, opacity=0.8))
            t.append(chemin(f"M {sgn * 14} -128 Q {sgn * 20} -122 {sgn * 18} -114", stroke=rc, sw=1.8, opacity=0.6))
        t.append(chemin("M -14 -182 Q 0 -186 14 -182", stroke=rc, sw=1.8, opacity=0.5))
    t.append(sourcils(18, -150, ss))
    if larmes:
        for sgn in (-1, 1):
            t.append(goutte(sgn * 22, -124, 0.8, "#74c0fc"))
    t.append(_nez(nez, p, _assombrir(p, 0.75)))
    t.append(bouche(0, -121, bs, 0.9))
    if "lunettes" in acc:
        t.append(g([cercle(-18, -150, 14, "none", stroke=ENCRE, stroke_width=3), cercle(18, -150, 14, "none", stroke=ENCRE, stroke_width=3), trait(-4, -150, 4, -150, ENCRE, 3)]))
    if tourne_:
        t = t[:debut_visage] + [g(t[debut_visage:], f"translate({n(tourne_)} 0)")]

    # --- cheveux devant et coiffes
    if "casque" in acc:
        t.append(_casque_chevalier(plumet=couleur_acc))
    else:
        t.append(_cheveux_devant(coiffure, ch))
        if coiffure == "chignon":
            t.append(cercle(0, -210, 26, ch))
            t.append(chemin("M -14 -220 Q 0 -230 14 -220", stroke=_assombrir(ch, 0.8), sw=2.5))
        if coiffure == "couettes":
            for sgn in (-1, 1):
                t.append(cercle(sgn * 58, -186, 6, couleur_acc if couleur_acc != OR else "#fa5252"))
    if "couronne" in acc:
        t.append(_couronne_tete(OR))
    if "grande_couronne" in acc:
        t.append(_couronne_tete(OR, grande=True))
    if "diademe" in acc:
        t.append(_diademe())
    if "chapeau_pointu" in acc:
        t.append(_chapeau_pointu(couleur_acc if couleur_acc != OR else "#343a40"))
    if "noeud" in acc:
        t.append(g([poly([(32, -196), (12, -212), (12, -180)], couleur_acc), poly([(32, -196), (52, -212), (52, -180)], couleur_acc), cercle(32, -196, 7, _assombrir(couleur_acc, 0.8))]))
    if "fleur" in acc:
        t.append(fleur(36, -186, 0.8, couleur_acc, tige=0))
    if "toque" in acc:
        t.append(g([cercle(-26, -218, 27.5, "#dee2e6"), cercle(26, -218, 27.5, "#dee2e6"), cercle(0, -232, 31.5, "#dee2e6"),
                    cercle(-26, -218, 26, "#fff"), cercle(26, -218, 26, "#fff"), cercle(0, -232, 30, "#fff"),
                    rect(-40, -208, 80, 26, "#fff", rx=6, stroke="#e9ecef", stroke_width=2)]))
    if "bonnet_nuit" in acc:
        t.append(g([chemin("M -54 -168 Q -40 -226 20 -224 Q 70 -220 84 -150 Q 60 -196 30 -200 Q 0 -196 54 -168 Z", couleur_acc),
                    chemin("M -56 -166 Q 0 -196 56 -166", stroke="#fff", sw=10), cercle(86, -146, 12, "#fff")]))
    if coiffe:
        t.append(coiffe)
    m.append(tete(g(t)))

    if devant:
        m.append(bras_svg + mains_svg)
    if incline and haut_corps is not None:
        # le haut du corps penche autour des hanches ; jambes et pieds restent au sol
        m = m[:haut_corps] + [g(m[haut_corps:], f"rotate({n(incline)} 0 {n((-80 if robe else -46) * ly)})")]
    dessin = avec_contour(m, s)
    if (OMBRE_SOL[0] if ombre is None else ombre) and not rot and not sirene:
        dessin = ombre_sol(incline * 0.8, -3, 52 * lx) + dessin
    occuper(x - 80 * lx * s, y - (112 * ly + 125 * kh) * s * (sy or 1), x + 80 * lx * s, y + 8 * s)
    return place(dessin, x, y, s, flip=flip, rot=rot, sy=sy)


def _chaussures(pas, couleur, rx, ry, ecart, y):
    """Deux chaussures avec leur semelle ; la droite levée si l'on marche."""
    bord = _assombrir(couleur, 0.7)
    m = []
    for sgn in (-1, 1):
        x, yy, rot = sgn * ecart, y, 0
        if pas in ("marche", "pointe") and sgn > 0:
            x, yy, rot = ecart + 18, y - 12, -24
        elif pas == "court" and sgn > 0:
            x, yy, rot = ecart + 18, y - 8, -15
        elif pas == "saute":
            yy, rot = y + 2, sgn * 22
        m.append(ellipse(x, yy, rx, ry, couleur, rot=rot or None, stroke=bord, stroke_width=2))
        m.append(ellipse(x - sgn * 3, yy - ry * 0.35, rx * 0.4, ry * 0.25, "#fff", rot=rot or None, opacity=0.3))
    return m


def princesse(x=0, y=0, s=1.0, **k):
    k.setdefault("acc", ("diademe",))
    return personne(x, y, s, **k)


def chevalier(x=0, y=0, s=1.0, plumet="#fa5252", **k):
    k.setdefault("habit", "#ced4da")
    k.setdefault("jambes", "#adb5bd")
    k.setdefault("chaussures", "#868e96")
    k.setdefault("robe", False)
    k.setdefault("coiffure", "courts")
    return personne(x, y, s, acc=("casque",) + tuple(k.pop("acc", ())), couleur_acc=plumet, **k)


def roi(x=0, y=0, s=1.0, **k):
    k.setdefault("habit", "#c92a2a")
    k.setdefault("robe", False)
    k.setdefault("jambes", "#1c2a52")
    k.setdefault("cape", "#862e9c")
    k.setdefault("barbe", "#e9ecef")
    k.setdefault("coiffure", "chauve_cote")
    k.setdefault("cheveux", "blanc")
    k.setdefault("ceinture", "#f59f00")
    return personne(x, y, s, acc=("grande_couronne",) + tuple(k.pop("acc", ())), **k)


def reine(x=0, y=0, s=1.0, **k):
    k.setdefault("habit", "#7048e8")
    k.setdefault("cape", "#c92a2a")
    k.setdefault("coiffure", "chignon")
    k.setdefault("cheveux", "gris")
    return personne(x, y, s, acc=("couronne",) + tuple(k.pop("acc", ())), **k)


def sorciere(x=0, y=0, s=1.0, chapeau="#5f3dc4", **k):
    k.setdefault("habit", "#7048e8")
    k.setdefault("coiffure", "sorciere")
    k.setdefault("cheveux", "roux")
    k.setdefault("motif_robe", OR)
    return personne(x, y, s, acc=("chapeau_pointu",) + tuple(k.pop("acc", ())), couleur_acc=chapeau, **k)


def baguette(x, y, s=1.0, rot=0, couleur="#343a40", etoile=OR, brille=True):
    """Baguette magique ; (x, y) = poignée."""
    m = [trait(0, 0, 0, -70, couleur, 6), trait(0, 0, 0, -18, OR_FONCE, 7)]
    if brille:
        m.append(cercle(0, -82, 22, etoile, opacity=0.3))
    m.append(etoile5(0, -82, 15, etoile))
    return place(m, x, y, s, rot=rot)


def etincelles(x, y, s=1.0, couleur=OR, graine=1, nb=9, r=70):
    """Nuage de petites étoiles magiques autour de (x, y)."""
    rr = random.Random(graine)
    m = []
    for k in range(nb):
        a = rr.uniform(0, 2 * math.pi)
        d = rr.uniform(0.2, 1.0) * r
        px, py = math.cos(a) * d, math.sin(a) * d
        if k % 3 == 0:
            m.append(cercle(px, py, rr.uniform(3, 5), couleur))
        else:
            m.append(etoile5(px, py, rr.uniform(6, 12), couleur, rot=rr.uniform(0, 40)))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Créatures
# ---------------------------------------------------------------------------

def dragon(x=0, y=0, s=1.0, couleur="#69db7c", ventre="#d8f5a2", expr="sourire", bras="bas",
           ailes="bas", regard=(0, 0), flip=False, larmes=False, rot=0, objet=None):
    """Dragon tout rond vu de face, les pieds en (0, 0)."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.78)
    m = []
    # queue
    m.append(chemin("M 30 -34 Q 96 -20 104 -70 Q 108 -100 128 -108", stroke=couleur, sw=22))
    m.append(poly([(118, -104), (146, -134), (142, -96)], fonce))
    # ailes
    for sgn in (-1, 1):
        if ailes == "ouvertes":
            d = (f"M {sgn * 30} -110 L {sgn * 150} -200 Q {sgn * 140} -150 {sgn * 156} -120 "
                 f"Q {sgn * 120} -126 {sgn * 118} -96 Q {sgn * 90} -110 {sgn * 76} -80 Q {sgn * 56} -100 {sgn * 36} -80 Z")
        else:
            d = (f"M {sgn * 30} -110 L {sgn * 100} -170 Q {sgn * 98} -130 {sgn * 110} -110 "
                 f"Q {sgn * 84} -114 {sgn * 84} -90 Q {sgn * 64} -100 {sgn * 36} -80 Z")
        m.append(chemin(d, fonce))
    # pieds
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 24, -10, 22, 13, fonce))
        for k in (-1, 0, 1):
            m.append(cercle(sgn * 24 + k * 11, -2, 4, "#fff"))
    # corps
    m.append(ellipse(0, -66, 48, 58, couleur))
    m.append(ellipse(0, -58, 30, 42, ventre))
    for k in range(4):
        yy = -86 + k * 16
        m.append(chemin(f"M -22 {yy} Q 0 {yy + 6} 22 {yy}", stroke=_assombrir(ventre, 0.85), sw=3))
    # bras
    main_g, main_d = POSES[bras]
    coude_g, coude_d = COUDES.get(bras, (None, None))
    bras_svg = _bras(-34, -98, main_g, coude_g, couleur, 16) + _bras(34, -98, main_d, coude_d, couleur, 16)
    mains_svg = cercle(main_g[0], main_g[1], 12, couleur) + cercle(main_d[0], main_d[1], 12, couleur)
    devant = bras in DEVANT_VISAGE
    if not devant:
        m.append(bras_svg)
        if objet:
            m.append(objet)
        m.append(mains_svg)
    # tête
    for sgn in (-1, 1):
        m.append(poly([(sgn * 24, -196), (sgn * 40, -236), (sgn * 44, -190)], "#fff4e6", stroke="#e9d5b5", stroke_width=2))
    for k, hx in enumerate((-18, 0, 18)):
        h = 26 if hx == 0 else 18
        m.append(poly([(hx - 10, -196), (hx, -196 - h), (hx + 10, -196)], fonce))
    m.append(ellipse(0, -154, 60, 50, couleur))
    m.append(ellipse(0, -124, 36, 22, ventre))
    m.append(ellipse(-10, -130, 4, 3, fonce) + ellipse(10, -130, 4, 3, fonce))
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 40, -136, 9, 5.5, ROSE, opacity=0.7))
    m.append(oeil(-24, -164, ys, regard, sclere=True) + oeil(24, -164, ys, regard, sclere=True))
    m.append(sourcils(24, -164, ss))
    if larmes:
        for sgn in (-1, 1):
            m.append(goutte(sgn * 30, -134, 0.9, "#74c0fc"))
    m.append(bouche(0, -116, bs, 1.1))
    if devant:
        m.append(bras_svg + mains_svg)
    occuper(x - 110 * s, y - 270 * s, x + 110 * s, y)
    return place(m, x, y, s, flip=flip, rot=rot)


def dragon_vol(x, y, s=1.0, couleur="#69db7c", ventre="#d8f5a2", flip=False, expr="sourire"):
    """Dragon qui vole, de profil (tête à droite). (x, y) = centre du corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.78)
    m = [chemin("M -80 0 Q -160 10 -200 -30 Q -220 -50 -250 -46", stroke=couleur, sw=30),
         poly([(-240, -50), (-282, -70), (-268, -30)], fonce),
         chemin("M -30 -30 L -120 -190 Q -80 -150 -40 -170 Q -30 -120 10 -140 Q 10 -80 40 -40 Z", fonce),
         ellipse(0, 0, 100, 56, couleur),
         ellipse(10, 24, 70, 26, ventre),
         chemin("M 70 -20 Q 110 -60 140 -70", stroke=couleur, sw=46),
         ellipse(170, -84, 56, 40, couleur),
         ellipse(210, -70, 30, 24, ventre),
         poly([(140, -114), (126, -160), (160, -118)], "#fff4e6"),
         poly([(170, -120), (170, -168), (190, -122)], fonce),
         chemin("M 30 -60 L 44 -84 L 58 -58 L 72 -82 L 84 -56", fonce),
         chemin("M 30 30 L 90 -110 Q 110 -60 150 -70", "none"),
         ellipse(-40, 50, 16, 24, fonce), ellipse(40, 50, 16, 24, fonce)]
    m.append(chemin("M 20 -40 L 110 -200 Q 110 -140 150 -130 Q 110 -110 110 -70 Q 80 -80 60 -40 Z", fonce))
    m.append(oeil(176, -96, ys, (1, 0), sclere=True))
    m.append(ellipse(184, -70, 9, 5.5, ROSE, opacity=0.7))
    m.append(bouche(214, -56, bs, 0.9))
    return place(m, x, y, s, flip=flip)


def bulles_savon(x, y, s=1.0, graine=4, nb=8, r=90):
    rr = random.Random(graine)
    m = []
    for _ in range(nb):
        a = rr.uniform(-math.pi, 0)
        d = rr.uniform(0.3, 1.0) * r
        bx, by, br = math.cos(a) * d * 1.4, math.sin(a) * d, rr.uniform(10, 26)
        m.append(cercle(bx, by, br, "#e7f5ff", opacity=0.35, stroke="#74c0fc", stroke_width=3))
        m.append(cercle(bx - br * 0.35, by - br * 0.35, br * 0.22, "#fff", opacity=0.9))
    return place(m, x, y, s)


ARC_EN_CIEL = ("#fa5252", "#ff922b", "#fcc419", "#51cf66", "#339af0", "#9775fa")


def licorne(x=0, y=0, s=1.0, robe="#ffffff", criniere=ARC_EN_CIEL, expr="sourire", flip=False,
            galop=False, corne=OR, regard=(1, 0), larmes=False, rot=0, ombre="#dee2e6"):
    """Licorne de profil, la tête à droite ; (x, y) = au sol, sous le ventre."""
    ys, bs, ss = EXPRESSIONS[expr]
    sabot = "#adb5bd" if robe == "#ffffff" else _assombrir(robe, 0.7)
    cols = list(criniere) or ["#adb5bd"]
    m = []
    # queue
    for k, c in enumerate(cols):
        m.append(chemin(f"M -84 -130 Q {-130 - k * 4} {-120 + k * 6} {-120 + k * 3} {-60 + k * 8} Q {-116 + k * 2} {-40 + k * 6} {-136 + k * 2} {-20 + k * 4}", stroke=c, sw=12))
    # pattes
    if galop:
        pattes = [(-62, -80, 40), (-38, -80, 60), (46, -80, -50), (70, -80, -30)]
    else:
        pattes = [(-62, -80, 0), (-36, -80, 0), (46, -80, 0), (72, -80, 0)]
    for k, (px, py, a) in enumerate(pattes):
        c = ombre if k in (1, 2) else robe
        m.append(place([rect(-11, 0, 22, 74, c, rx=9, stroke=ombre, stroke_width=2), rect(-12, 62, 24, 16, sabot, rx=5)], px, py, 1.0, rot=a))
    # cou, corps et tête (avec un léger contour pour les fonds clairs)
    cou = [(26, -136), (74, -228), (134, -206), (100, -110)]
    m.append(poly(cou, robe, stroke=ombre, stroke_width=3))
    m.append(ellipse(0, -112, 96, 50, robe, stroke=ombre, stroke_width=3))
    m.append(poly([(32, -134), (76, -222), (130, -206), (98, -116)], robe))
    m.append(ellipse(122, -214, 50, 32, robe, rot=24, stroke=ombre, stroke_width=3))
    m.append(ellipse(152, -196, 26, 22, "#ffe3ec"))
    m.append(ellipse(160, -200, 3.5, 3, "#c2255c"))
    # oreille
    m.append(poly([(90, -238), (96, -272), (112, -240)], robe, stroke=ombre, stroke_width=2))
    m.append(poly([(96, -242), (99, -262), (107, -242)], "#ffc9d6"))
    # corne
    m.append(poly([(110, -244), (136, -304), (126, -238)], corne, stroke=OR_FONCE, stroke_width=2))
    for k in range(3):
        yy = -254 - k * 14
        m.append(trait(114 + k * 5, yy + 4, 128 + k * 3, yy - 2, OR_FONCE, 2))
    # crinière
    pts = [(92, -254), (76, -240), (66, -222), (58, -204), (48, -186), (40, -168), (32, -150)]
    for k, (px, py) in enumerate(pts):
        c = cols[k * len(cols) // len(pts)]
        m.append(cercle(px - 8, py - 4, 14, c))
    m.append(cercle(102, -252, 11, cols[0]))
    # visage
    m.append(ellipse(128, -198, 9, 5.5, ROSE, opacity=0.7))
    m.append(oeil(116, -222, ys, regard, taille=1.0))
    m.append(sourcils(0, -222, None))
    if ss:
        m.append(place(sourcils(10, 0, ss), 106, -222))
    if larmes:
        m.append(goutte(118, -196, 0.8, "#74c0fc"))
    m.append(place(bouche(0, 0, bs, 0.6), 150, -180))
    occuper(x - 150 * s, y - 270 * s, x + 150 * s, y + 90 * s)
    return place(m, x, y, s, flip=flip, rot=rot)


def etoile_perso(x, y, r=60, couleur=OR, expr="sourire", halo=True, rot=0, larmes=False, eteinte=False):
    """Petite étoile qui parle."""
    ys, bs, ss = EXPRESSIONS[expr]
    c = "#e9ecef" if eteinte else couleur
    m = []
    if halo and not eteinte:
        lumiere_auto(x, y, r * 2.4, couleur, 0.45)
        m.append(cercle(0, 0, r * 1.5, eclaircir(couleur, 0.7), opacity=0.25))
    pts = []
    for k in range(10):
        a = math.radians(rot - 90 + k * 36)
        rr = r if k % 2 == 0 else r * 0.52
        pts.append((math.cos(a) * rr, math.sin(a) * rr))
    m.append(poly(pts, c, stroke=c, stroke_width=r * 0.28, stroke_linejoin="round"))
    k = r / 60
    m.append(ellipse(-20 * k, 10 * k, 7 * k, 4.5 * k, ROSE, opacity=0.7))
    m.append(ellipse(20 * k, 10 * k, 7 * k, 4.5 * k, ROSE, opacity=0.7))
    m.append(place(oeil(-12, 0, ys, (0, 0)) + oeil(12, 0, ys, (0, 0)) + sourcils(12, 0, ss)
                   + bouche(0, 18, bs, 0.7), 0, -6 * k, k * 0.9))
    if larmes:
        m.append(goutte(-16 * k, 14 * k, 0.6 * k, "#74c0fc"))
        m.append(goutte(16 * k, 14 * k, 0.6 * k, "#74c0fc"))
    return place(m, x, y)


def poulpe(x, y, s=1.0, couleur="#f783ac", expr="sourire", regard=(0, 0)):
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    m = []
    for k in range(8):
        a = -30 + k * 26
        dx = -112 + k * 32
        m.append(chemin(f"M {dx * 0.35} -40 Q {dx * 0.8} 0 {dx} 20 Q {dx + 20} 40 {dx + (10 if k % 2 else -10)} 58", stroke=couleur, sw=18))
    m.append(ellipse(0, -90, 72, 80, couleur))
    for px, py in [(-30, -140), (20, -150), (40, -110)]:
        m.append(cercle(px, py, 8, fonce))
    m.append(ellipse(-38, -68, 10, 6, ROSE, opacity=0.8) + ellipse(38, -68, 10, 6, ROSE, opacity=0.8))
    m.append(oeil(-24, -86, ys, regard, sclere=True) + oeil(24, -86, ys, regard, sclere=True))
    m.append(sourcils(24, -86, ss))
    m.append(bouche(0, -62, bs))
    return place(m, x, y, s)


def crabe(x, y, s=1.0, couleur="#ff6b6b", expr="sourire", pinces_haut=True):
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = []
    for sgn in (-1, 1):
        for k in range(3):
            m.append(chemin(f"M {sgn * 30} {-20 + k * 10} Q {sgn * 70} {-24 + k * 12} {sgn * 80} {4 + k * 6}", stroke=fonce, sw=6))
        hy = -110 if pinces_haut else -40
        m.append(chemin(f"M {sgn * 44} -44 Q {sgn * 76} -60 {sgn * 76} {hy + 20}", stroke=couleur, sw=10))
        m.append(chemin(f"M {sgn * 76} {hy + 22} Q {sgn * 50} {hy - 10} {sgn * 72} {hy - 30} Q {sgn * 80} {hy - 6} {sgn * 90} {hy - 26} Q {sgn * 104} {hy + 10} {sgn * 76} {hy + 22} Z", couleur))
    m.append(ellipse(0, -30, 60, 38, couleur))
    for sgn in (-1, 1):
        m.append(trait(sgn * 16, -60, sgn * 20, -86, fonce, 5))
        m.append(cercle(sgn * 20, -92, 12, "#fff", stroke=ENCRE, stroke_width=1.5))
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * 20, -92, ys, (0, 0), taille=0.7))
        else:
            m.append(cercle(sgn * 20, -92, 6, ENCRE))
    m.append(bouche(0, -26, bs, 0.9))
    m.append(ellipse(-34, -26, 8, 5, ROSE, opacity=0.8) + ellipse(34, -26, 8, 5, ROSE, opacity=0.8))
    return place(m, x, y, s)


def pie(x, y, s=1.0, expr="malin", flip=False, ailes="bas", objet=None, regard=(0, 0)):
    """Une pie : oiseau noir et blanc à longue queue ; (x, y) = sous les pattes."""
    m = [chemin("M -30 -50 L -120 -20 L -110 -2 L -24 -36 Z", "#364fc7"),
         oiseau(0, 0, 1.0, "#343a40", "#ffffff", expr=expr, ailes=ailes, regard=regard)]
    if objet:
        m.append(place(objet, 0, -60))
    return place(m, x, y, s, flip=flip)


def luciole(x, y, s=1.0, allumee=True, expr="sourire", flip=False):
    ys, bs, ss = EXPRESSIONS[expr]
    if allumee:
        lumiere_auto(x + (26 if flip else -26) * s, y + 10 * s, 90 * s, "#ffe066", 0.55)
    m = []
    if allumee:
        m.append(cercle(-26, 10, 44, "#ffec99", opacity=0.35))
        m.append(cercle(-26, 10, 24, "#ffe066", opacity=0.6))
    m += [ellipse(-24, 10, 20, 16, "#fff3bf" if allumee else "#adb5bd"),
          ellipse(0, 0, 26, 20, "#5c7cfa"),
          ellipse(-6, -18, 22, 12, "#d0ebff", opacity=0.8, rot=-20),
          ellipse(10, -20, 22, 12, "#d0ebff", opacity=0.8, rot=20),
          cercle(28, -4, 18, "#4263eb"),
          trait(30, -20, 26, -40, ENCRE, 2.5), trait(36, -18, 44, -36, ENCRE, 2.5),
          cercle(26, -41, 3.5, ENCRE), cercle(45, -37, 3.5, ENCRE)]
    m.append(oeil(26, -6, ys, (1, 0), taille=0.6) + oeil(38, -6, ys, (1, 0), taille=0.6))
    m.append(place(bouche(0, 0, bs, 0.5), 33, 4))
    return place(m, x, y, s, flip=flip)


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def chateau(x, y, s=1.0, mur="#f3d9fa", mur2="#e5dbff", toit="#e64980", drapeau="#fab005",
            porte_c="#a0522d", fenetres="#ffe066", nuit_=False):
    """Château de conte ; (x, y) = milieu de la base. Largeur ≈ 520, hauteur ≈ 520."""
    vitre = "#ffe066" if nuit_ else fenetres
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(20, 0, 300, 18, 0.15))

    def fenetre_tour(tx, fy):
        return [rect(tx - 14, fy - 4, 28, 42, _assombrir(mur2, 0.8), rx=13),
                rect(tx - 10, fy, 20, 34, vitre, rx=10),
                rect(tx - 10, fy, 20, 8, "#000", opacity=0.18, rx=4),
                rect(tx - 14, fy + 34, 28, 6, eclaircir(mur2, 0.5), rx=2)]

    def tourelle(tx, base, h, w, toit_h):
        haut = base - h
        cone = [(tx - w / 2 - 14, haut + 2), (tx, haut - toit_h), (tx + w / 2 + 14, haut + 2)]
        cid = uid("k")
        tuiles = " ".join(f"M {n(tx - w)} {n(yy)} " + " ".join("q 7 8 14 0" for _ in range(int(w * 2 / 14) + 1))
                          for yy in range(int(haut - toit_h + 24), int(haut + 2), 14))
        t = [rect(tx - w / 2, haut, w, h, cylindre(mur2, 0.3, 0.74)),
             pierres(tx - w / 2, haut, w, h, mur2),
             rect(tx - w / 2, haut, w, 16, "#000", opacity=0.16),
             poly(cone, cylindre(toit, 0.3, 0.68)),
             el("clipPath", poly(cone, "#000"), id=cid) + g(chemin(tuiles, stroke=_assombrir(toit, 0.7), sw=1.8, opacity=0.5), clip_path=f"url(#{cid})"),
             rect(tx - w / 2 - 16, haut - 2, w + 32, 8, _assombrir(toit, 0.65), rx=4),
             trait(tx, haut - toit_h, tx, haut - toit_h - 40, "#495057", 4),
             chemin(f"M {n(tx)} {n(haut - toit_h - 40)} Q {n(tx + 20)} {n(haut - toit_h - 42)} {n(tx + 38)} {n(haut - toit_h - 30)} Q {n(tx + 20)} {n(haut - toit_h - 26)} {n(tx)} {n(haut - toit_h - 20)} Z", cylindre(drapeau, 0.3, 0.75, vertical=True))]
        t += fenetre_tour(tx, haut + 40)
        return t

    # donjon central
    m += tourelle(0, -170, 190, 120, 120)
    # corps de logis, créneaux et leur ombre
    m.append(rect(-190, -220, 380, 220, lineaire([(0, eclaircir(mur, 0.25)), (0.5, mur), (1, _assombrir(mur, 0.86))], 0, 0, 1, 0)))
    m.append(pierres(-190, -220, 380, 220, mur, pas_=26, larg=44, opacite=0.28))
    for k in range(8):
        cx = -190 + k * 50
        m.append(rect(cx, -244, 30, 26, cylindre(mur, 0.3, 0.8)))
        m.append(rect(cx, -244, 30, 4, eclaircir(mur, 0.5)))
    m.append(rect(-190, -220, 380, 12, "#000", opacity=0.14))
    m.append(rect(-190, -14, 380, 14, _assombrir(mur, 0.8)))
    # tours latérales
    m += tourelle(-210, 0, 300, 100, 110)
    m += tourelle(210, 0, 300, 100, 110)
    # porte : claveaux de l'arc, planches, ferrures
    m.append(chemin("M -62 0 L -62 -82 Q 0 -156 62 -82 L 62 0 Z", _assombrir(mur, 0.8)))
    m.append(chemin("M -50 0 L -50 -80 Q 0 -140 50 -80 L 50 0 Z", cylindre(porte_c, 0.2, 0.7)))
    m.append(chemin("M -56 -80 Q 0 -150 56 -80", stroke=eclaircir(mur, 0.5), sw=3, opacity=0.8))
    m.append(chemin("M -25 -6 V -110 M 25 -6 V -110", stroke=_assombrir(porte_c, 0.75), sw=2.5, opacity=0.7))
    m.append(chemin("M -40 0 L -40 -78 Q 0 -126 40 -78 L 40 0", stroke=_assombrir(porte_c, 0.7), sw=4))
    m.append(trait(0, -118, 0, 0, _assombrir(porte_c, 0.7), 4))
    m.append(chemin("M -46 -30 H -6 M 6 -30 H 46 M -46 -70 H -6 M 6 -70 H 46", stroke="#495057", sw=4, opacity=0.8))
    m += [cercle(-10, -50, 4, volume(OR, 0.6, 0.7)), cercle(10, -50, 4, volume(OR, 0.6, 0.7))]
    for fx in (-120, 120):
        m.append(chemin(f"M {fx - 24} -114 L {fx - 24} -150 Q {fx} -184 {fx + 24} -150 L {fx + 24} -114 Z", _assombrir(mur, 0.82)))
        m.append(chemin(f"M {fx - 18} -120 L {fx - 18} -150 Q {fx} -176 {fx + 18} -150 L {fx + 18} -120 Z", vitre))
        m.append(chemin(f"M {fx - 18} -120 L {fx - 18} -150 Q {fx} -176 {fx + 18} -150 L {fx + 12} -146 Q {fx} -166 {fx - 12} -146 L {fx - 12} -120 Z", "#000", opacity=0.16))
        m.append(trait(fx, -168, fx, -120, _assombrir(mur, 0.75), 3))
        m.append(rect(fx - 26, -120, 52, 7, eclaircir(mur, 0.5), rx=2))
        if nuit_:
            m.append(ellipse(fx, -146, 46, 44, radial([(0, "#ffe066", 0.4), (1, "#ffe066", 0)])))
    return place(m, x, y, s)


def tour_seule(x, y, s=1.0, mur="#e5dbff", toit="#e64980", fenetre_c="#ffe066", h=420):
    m = [rect(-70, -h, 140, h, cylindre(mur, 0.3, 0.74)),
         pierres(-70, -h, 140, h, mur, pas_=24, larg=36, opacite=0.3),
         rect(-70, -h, 140, 18, "#000", opacity=0.16),
         poly([(-90, -h + 2), (0, -h - 150), (90, -h + 2)], cylindre(toit, 0.3, 0.68)),
         rect(-92, -h - 2, 184, 9, _assombrir(toit, 0.65), rx=4),
         chemin(f"M -32 {-h + 114} L -32 {-h + 58} Q 0 {-h + 22} 32 {-h + 58} L 32 {-h + 114} Z", _assombrir(mur, 0.8)),
         chemin(f"M -26 {-h + 110} L -26 {-h + 60} Q 0 {-h + 30} 26 {-h + 60} L 26 {-h + 110} Z", fenetre_c),
         chemin(f"M -26 {-h + 110} L -26 {-h + 60} Q 0 {-h + 30} 26 {-h + 60} L 18 {-h + 64} Q 0 {-h + 42} -18 {-h + 64} L -18 {-h + 110} Z", "#000", opacity=0.15),
         rect(-40, -h + 106, 80, 12, _assombrir(mur, 0.85), rx=4)]
    for k in range(6):
        m.append(rect(-70 + (k % 2) * 60, -h + 160 + k * 40, 40, 14, _assombrir(mur, 0.93), rx=3))
    return place(m, x, y, s)


def jardin_chateau(S, ciel_haut="#a5d8ff", ciel_bas="#fff0f6", herbe="#8ce99a", y=620, chateau_s=0.8, chateau_x=400):
    ciel(S, ciel_haut, ciel_bas)
    S.add(nuage(160, 130, 0.8), nuage(650, 90, 0.6))
    collines(S, y, "#b2f2bb", graine=4)
    S.add(chateau(chateau_x, y + 10, chateau_s))
    sol(S, y, herbe)


def couronne_objet(x, y, s=1.0, rot=0, brille=False):
    m = []
    if brille:
        m.append(eclat(0, -30, 1.4, OR))
    m += [poly([(-44, 0), (-50, -56), (-24, -30), (0, -66), (24, -30), (50, -56), (44, 0)], OR, stroke=OR_FONCE, stroke_width=4),
          rect(-46, -14, 92, 16, OR_FONCE, rx=6),
          cercle(0, -30, 7, "#fa5252"), cercle(-28, -8, 5, "#4dabf7"), cercle(28, -8, 5, "#4dabf7"), cercle(0, -8, 5, "#51cf66")]
    return place(m, x, y, s, rot=rot)


def chaudron(x, y, s=1.0, contenu="#8ce99a", fumee=True, feu=True, bulles_=True):
    m = []
    if feu:
        for k, c in enumerate(("#ff922b", "#ffd43b")):
            k2 = 1 - k * 0.45
            m.append(chemin(f"M {-60 * k2} 20 Q {-70 * k2} -20 {-30 * k2} -40 Q {-20 * k2} -10 0 {-60 * k2} Q {20 * k2} -10 {30 * k2} -40 Q {70 * k2} -20 {60 * k2} 20 Z", c))
        for k in range(3):
            m.append(rect(-70 + k * 40, 10, 60, 16, "#8d5524", rx=8))
    if fumee:
        m.append(chemin("M -30 -170 Q -60 -210 -20 -240 Q 10 -270 -20 -310", stroke="#dee2e6", sw=14, opacity=0.8))
        m.append(chemin("M 30 -170 Q 60 -220 20 -250 Q 0 -280 30 -320", stroke="#dee2e6", sw=12, opacity=0.7))
    m += [trait(-80, 10, -60, -30, "#343a40", 8), trait(80, 10, 60, -30, "#343a40", 8),
          chemin("M -110 -150 Q -120 -20 0 -20 Q 120 -20 110 -150 Z", "#343a40"),
          ellipse(0, -150, 112, 22, "#495057"),
          ellipse(0, -150, 96, 15, contenu)]
    if bulles_:
        m += [cercle(-40, -156, 9, eclaircir(contenu, 0.4)), cercle(20, -152, 12, eclaircir(contenu, 0.4)), cercle(56, -158, 7, eclaircir(contenu, 0.4))]
    m.append(chemin("M -80 -110 Q -70 -60 -40 -50", stroke="#868e96", sw=5, opacity=0.6))
    return place(m, x, y, s)


def echelle(x, y, s=1.0, h=400, rot=0, couleur="#c68642"):
    m = [rect(-40, -h, 12, h, couleur, rx=4), rect(28, -h, 12, h, couleur, rx=4)]
    for k in range(int(h // 50)):
        m.append(rect(-32, -30 - k * 50, 64, 10, couleur, rx=3))
    return place(m, x, y, s, rot=rot)


def cerf_volant(x, y, s=1.0, couleur="#fa5252", couleur2="#ffd43b", fil_vers=None, rot=0):
    m = [poly([(0, -70), (46, 0), (0, 90), (-46, 0)], couleur),
         poly([(0, -70), (46, 0), (0, 0)], couleur2), poly([(0, 90), (-46, 0), (0, 0)], couleur2),
         chemin("M 0 90 Q 20 120 0 150 Q -20 180 0 210", stroke="#495057", sw=3)]
    for k, yy in enumerate((120, 160, 200)):
        m.append(poly([(-12, yy - 8), (12, yy + 8), (12, yy - 8), (-12, yy + 8)], couleur if k % 2 else couleur2))
    fig = place(m, x, y, s, rot=rot)
    if fil_vers:
        fx, fy = fil_vers
        return g([chemin(f"M {x} {y + 20 * s} Q {n((x + fx) / 2)} {n(max(y, fy) + 40)} {fx} {fy}", stroke="#868e96", sw=2), fig])
    return fig


def fontaine(x, y, s=1.0, pierre="#ced4da", eau_c="#74c0fc"):
    m = [ellipse(0, -10, 150, 30, _assombrir(pierre, 0.85)), rect(-150, -60, 300, 50, pierre, rx=10),
         ellipse(0, -60, 150, 26, eau_c), rect(-14, -170, 28, 110, pierre),
         ellipse(0, -170, 60, 14, pierre),
         chemin("M 0 -176 Q -40 -230 -80 -150", stroke=eau_c, sw=6), chemin("M 0 -176 Q 40 -230 80 -150", stroke=eau_c, sw=6),
         chemin("M 0 -176 L 0 -210", stroke=eau_c, sw=6)]
    return place(m, x, y, s)


def nenuphar(x, y, s=1.0, fleur_c=None):
    m = [chemin("M 0 0 L 79 -5 A 80 26 0 1 0 79 5 Z", "#40c057"),
         chemin("M 0 0 L 79 -5 M 0 0 L -60 -14 M 0 0 L -50 16", stroke="#2f9e44", sw=3)]
    if fleur_c:
        for k in range(6):
            a = math.radians(-90 + k * 60)
            m.append(ellipse(-20 + math.cos(a) * 12, -14 + math.sin(a) * 8, 12, 7, fleur_c, rot=k * 60))
        m.append(cercle(-20, -14, 6, "#ffd43b"))
    return place(m, x, y, s)


def etang(S, y=520, couleur="#4dabf7", couleur2="#74c0fc"):
    S.add(ellipse(400, y + 150, 520, 200, couleur))
    for k in range(5):
        S.add(chemin(f"M {150 + k * 120} {y + 60 + (k % 2) * 60} q 20 -10 40 0", stroke=couleur2, sw=5))


# --- Fonds marins -----------------------------------------------------------

def ocean(S, haut="#1c7ed6", bas="#0b4f8a", sable="#f4d58d", y_sable=660, rayons=True):
    S._decor("eau")
    _cachettes_sol(S, y_sable, 20, nature="eau")
    S.add(rect(0, 0, S.w, S.h, S.degrade([haut, bas])))
    if rayons:
        for k in range(4):
            x0 = 80 + k * 200
            S.add(poly([(x0, 0), (x0 + 70, 0), (x0 + 160, y_sable), (x0 + 40, y_sable)], "#ffffff", opacity=0.06))
    S.add(chemin(f"M 0 {y_sable} Q 200 {y_sable - 30} 400 {y_sable} T 800 {y_sable - 10} L 800 800 L 0 800 Z", terrain(sable)))
    for k in range(18):
        S.add(cercle(30 + (k * 91) % 760, y_sable + 30 + (k * 47) % 110, 3, "#e8c170"))


def algue(x, y, s=1.0, couleur="#40c057", h=220, graine=1):
    r = random.Random(graine)
    m = []
    for k in range(3):
        dx = (k - 1) * 18
        hh = h * r.uniform(0.7, 1.1)
        m.append(chemin(f"M {dx} 0 Q {dx - 30} {-hh * 0.25} {dx} {-hh * 0.5} Q {dx + 30} {-hh * 0.75} {dx} {-hh}", stroke=couleur if k != 1 else _assombrir(couleur, 0.85), sw=14))
    return place(m, x, y, s)


def corail(x, y, s=1.0, couleur="#ff8787"):
    m = [chemin("M 0 0 L 0 -80 M 0 -50 Q -40 -70 -40 -120 M 0 -60 Q 40 -80 36 -140 M -20 -86 Q -60 -100 -64 -80 M 20 -110 Q 50 -120 60 -100", stroke=couleur, sw=16)]
    for px, py in [(-40, -120), (36, -140), (-64, -80), (60, -100), (0, -80)]:
        m.append(cercle(px, py, 10, couleur))
    return place(m, x, y, s)


def coquillage(x, y, s=1.0, couleur="#ffc9d6", rot=0):
    m = [chemin("M -40 0 Q -50 -60 0 -64 Q 50 -60 40 0 Z", couleur)]
    for k in range(-2, 3):
        m.append(chemin(f"M {k * 5} -2 L {k * 16} -58", stroke=_assombrir(couleur, 0.85), sw=3))
    m.append(rect(-14, -6, 28, 12, _assombrir(couleur, 0.9), rx=5))
    return place(m, x, y, s, rot=rot)


def perle(x, y, s=1.0, brille=True):
    m = []
    if brille:
        m += [cercle(0, 0, 44, "#fff9db", opacity=0.35), cercle(0, 0, 30, "#fff9db", opacity=0.5)]
    m += [cercle(0, 0, 20, "#f8f9fa", stroke="#dee2e6", stroke_width=2), cercle(-6, -7, 6, "#fff")]
    return place(m, x, y, s)


def bulles_eau(x, y, s=1.0, nb=5, graine=2):
    r = random.Random(graine)
    m = []
    for k in range(nb):
        m.append(cercle(r.uniform(-20, 20), -k * 36, r.uniform(6, 14), "none", stroke="#d0ebff", stroke_width=3, opacity=0.8))
    return place(m, x, y, s)


def palais_coquillage(x, y, s=1.0):
    m = [chemin("M -200 0 Q -220 -180 -120 -220 Q -80 -330 0 -330 Q 80 -330 120 -220 Q 220 -180 200 0 Z", "#fcc2d7"),
         chemin("M -60 0 L -60 -100 Q 0 -170 60 -100 L 60 0 Z", "#862e9c")]
    for k in range(-3, 4):
        m.append(chemin(f"M {k * 20} -20 L {k * 56} -310", stroke="#f783ac", sw=4, opacity=0.6))
    for tx in (-150, 150):
        m.append(poly([(tx - 30, -150), (tx, -280), (tx + 30, -150)], "#e599f7"))
    m.append(perle(0, -250, 0.8))
    return place(m, x, y, s)
