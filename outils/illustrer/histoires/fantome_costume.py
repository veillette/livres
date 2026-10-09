"""Boubou cherche un costume — un petit fantôme le soir d'Halloween.

Dans le grenier de la vieille maison vit Boubou, un tout petit fantôme. Le
soir d'Halloween, il voit passer les enfants déguisés et veut un costume,
lui aussi. Le chapeau de sorcière est trop grand, la citrouille trop lourde,
la cape l'emmêle… Minuit, le chat noir du grenier, lui souffle : « Et si tu
sortais comme tu es ? » Dans la rue, les enfants trouvent son « costume »
magnifique, et quand le vent souffle les lanternes, c'est Boubou qui brille
dans la nuit pour les ramener chez eux.

Plans : 1 moyen (la fenêtre ronde) · 2 large (la malle) · 3 gros plan (le
chapeau) · 4 moyen (la citrouille) · 5 large (la cape) · 6 gros plan
(triste) · 7 large en diagonale (il descend vers la rue) · 8 moyen (quel
beau costume !) · 9 moyen (chez Madame Lucie) · 10 large (le vent, Boubou
brille) · 11 large (au revoir sous la fenêtre ronde).
"""
from base import *
from base import _assombrir
from fantastique import personne, ancre
from fetes import (citrouille_creusee, chapeau_sorciere, drap_fantome, lanterne, bonbon,
                   chauve_souris_papier, seau_bonbons)

ID = "fantome-costume"
PAPIER_PEINT = "etoiles"

BLANC_FANTOME = "#f8f9fa"
BORD_FANTOME = "#c5cbe3"

MINUIT = dict(couleur="#495057", visage="#adb5bd", acc=("noeud",), couleur_acc="#fd7e14")
LEA = dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#7048e8", acc=("chapeau_pointu",),
           couleur_acc="#343a40", yeux="cils")
LUCIE = dict(peau="claire", cheveux="blanc", coiffure="chignon", habit="#e64980", stature="ancien",
             carrure="ronde", nez="rond", acc=("lunettes",))

# bras du petit fantôme : (épaule, main) de chaque côté, repère local
BRAS_FANTOME = {
    "bas": ((-62, -104, -86, -70), (62, -104, 86, -70)),
    "haut": ((-62, -120, -92, -196), (62, -120, 92, -196)),
    "salut": ((-62, -104, -86, -70), (62, -120, 98, -190)),
    "ouverts": ((-62, -116, -116, -136), (62, -116, 116, -136)),
    "joues": ((-60, -110, -42, -126), (60, -110, 42, -126)),
    "yeux": ((-60, -112, -28, -150), (60, -112, 28, -150)),
    "tend": ((-62, -104, -86, -70), (62, -110, 116, -110)),
    "montre": ((-62, -104, -86, -70), (62, -114, 112, -160)),
}


def boubou(x, y, s=1.0, expr="sourire", bras="bas", regard=(0, 0), flip=False, rot=0,
           brille=False, larmes=False, rougit=False):
    """Boubou, le petit fantôme ; (x, y) = bas de sa traîne (il flotte)."""
    m = []
    if brille:
        m.append(cercle(0, -110, 190, radial([(0, "#e7f5ff", 0.85), (0.5, "#d0ebff", 0.35), (1, "#d0ebff", 0)])))
    corps = ("M -66 -8 Q -80 -90 -72 -140 Q -62 -224 0 -226 Q 62 -224 72 -140 Q 80 -90 66 -8 "
             "Q 54 -26 40 -6 Q 26 -26 12 -6 Q 0 -24 -12 -6 Q -26 -26 -40 -6 Q -54 -26 -66 -8 Z")
    m.append(chemin(corps, volume(BLANC_FANTOME, 0.15, 0.86), stroke=BORD_FANTOME, sw=3))
    m.append(chemin("M -44 -180 Q -30 -208 0 -212", stroke="#fff", sw=8, opacity=0.8))
    ys, bs, ss = EXPRESSIONS[expr]
    joues = "#ffc9c9" if not rougit else "#ff8787"
    m += [ellipse(-42, -122, 12 if rougit else 9, 6, joues, opacity=0.7),
          ellipse(42, -122, 12 if rougit else 9, 6, joues, opacity=0.7),
          oeil(-24, -150, ys, regard), oeil(24, -150, ys, regard), sourcils(24, -150, ss),
          bouche(0, -126, bs, 0.9)]
    if larmes:
        m.append(chemin("M -30 -138 Q -36 -120 -30 -112 Q -24 -120 -30 -138 Z", "#74c0fc"))
    for (ex, ey, hx, hy) in BRAS_FANTOME[bras]:
        mx, my = (ex + hx) / 2 + (8 if hx > 0 else -8), (ey + hy) / 2 + 8
        d = f"M {ex} {ey} Q {n(mx)} {n(my)} {hx} {hy}"
        m += [chemin(d, stroke=BORD_FANTOME, sw=27), chemin(d, stroke=BLANC_FANTOME, sw=22)]
    m.append(occuper(-90, -228, 90, 0))
    return place(m, x, y, s, flip=flip, rot=rot)


def minuit(x, y, s=0.9, **k):
    return perso("chat", x, y, s, **{**MINUIT, **k})


def lea(x, y, s=1.2, **k):
    return personne(x, y, s, **{**LEA, **k})


def _costume_citrouille():
    """Costume de citrouille posé sur le ventre (repère local d'un enfant)."""
    c = "#fd7e14"
    return g([ellipse(0, -62, 54, 50, volume(c, 0.35, 0.75)),
              chemin("M -26 -108 Q -40 -62 -26 -16 M 26 -108 Q 40 -62 26 -16 M 0 -112 V -12", stroke=_assombrir(c, 0.8), sw=3),
              poly([(-30, -84), (-12, -84), (-21, -70)], "#2b2b3a"), poly([(12, -84), (30, -84), (21, -70)], "#2b2b3a"),
              chemin("M -26 -52 Q 0 -30 26 -52 L 16 -46 L 8 -40 L 0 -44 L -8 -40 L -16 -46 Z", "#2b2b3a")])


def _tige():
    return g([rect(-7, -226, 14, 30, "#2f9e44", rx=5), ellipse(18, -214, 18, 8, "#40c057", rot=-20)])


def hugo(x, y, s=1.2, **k):
    return personne(x, y, s, **{**dict(peau="claire", cheveux="roux", coiffure="herisses", habit="#fd7e14", robe=False,
                                       jambes="#2b8a3e", taches=True, nez="retrousse", tenue=_costume_citrouille(),
                                       coiffe=_tige()), **k})


def sami(x, y, s=0.62, **k):
    """Le plus petit, caché sous un drap blanc percé de deux trous."""
    return drap_fantome(x, y, s, **k)


def lucie(x, y, s=1.2, **k):
    return personne(x, y, s, **{**LUCIE, **k})


def porte_lanterne(S, qui, x, y, s, flip=False, allumee=True, **k):
    """Un enfant qui porte sa lanterne (et son halo)."""
    S.add(qui(x, y, s, bras="tient", flip=flip, objet=lanterne(68, -146, 0.75, allumee=allumee), **k))
    if allumee:
        S.lumiere(x + (-68 if flip else 68) * s, y - (146 - 40) * s, 80 * s, "#ffd43b", 0.6)


# --- Décors --------------------------------------------------------------------

def oeil_de_boeuf(x, y, r, contenu="", cadre="#6b4f3a"):
    """Fenêtre ronde du grenier ; (x, y) = centre."""
    cid = uid("c")
    m = [cercle(x + 5, y + 7, r + 18, "#000", opacity=0.18), cercle(x, y, r + 18, volume(cadre, 0.3, 0.75)),
         cercle(x, y, r, "#1a1238"),
         el("clipPath", cercle(x, y, r, "#000"), id=cid), g(contenu, clip_path=f"url(#{cid})"),
         poly([(x - r * 0.5, y + r * 0.8), (x - r * 0.05, y - r * 0.95), (x + r * 0.2, y - r * 0.95), (x - r * 0.25, y + r * 0.8)], "#fff", opacity=0.08),
         rect(x - 5, y - r, 10, 2 * r, cadre), rect(x - r, y - 5, 2 * r, 10, cadre),
         cercle(x, y, r, "none", stroke=_assombrir(cadre, 0.8), stroke_width=4)]
    return g(m)


def dehors_nuit(cx, cy, r, enfants=True):
    """La rue vue par la fenêtre ronde : ciel, lune, toits, enfants déguisés."""
    m = [rect(cx - r, cy - r, 2 * r, 2 * r, lineaire([(0, "#1a1238"), (1, "#4b2f7a")])),
         lune(cx + r * 0.5, cy - r * 0.5, r * 0.16, halo=False)]
    for k in range(9):
        m.append(cercle(cx - r + (k * 73) % (2 * r), cy - r + 20 + (k * 41) % (r * 0.8), 2.2, "#fff3bf"))
    for k, (bx, bw, bh, c) in enumerate(((-1.0, 0.6, 0.5, "#2b1f45"), (-0.45, 0.5, 0.7, "#3b2a5e"), (0.1, 0.55, 0.45, "#2b1f45"), (0.6, 0.5, 0.65, "#3b2a5e"))):
        x0, w, h = cx + bx * r, bw * r, bh * r
        m.append(rect(x0, cy + r * 0.45 - h, w, h + r, c))
        m.append(poly([(x0 - 6, cy + r * 0.45 - h), (x0 + w / 2, cy + r * 0.45 - h - r * 0.22), (x0 + w + 6, cy + r * 0.45 - h)], c))
        m.append(rect(x0 + w * 0.35, cy + r * 0.45 - h * 0.7, w * 0.3, h * 0.25, "#ffe066"))
    m.append(rect(cx - r, cy + r * 0.45, 2 * r, r, "#3b2f5a"))
    if enfants:
        sy = cy + r * 0.78
        m.append(lea(cx - r * 0.45, sy, 0.3, bras="tient", objet=lanterne(68, -146, 0.75)))
        m.append(hugo(cx - r * 0.05, sy + 4, 0.3, bras="bas"))
        m.append(sami(cx + r * 0.3, sy + 6, 0.2))
    return g(m)


def grenier(S, y=610):
    """Le grenier de la vieille maison, la nuit : planches, toit en pente, poutre."""
    interieur(S, "#8a7259", "#7a5c43", y, plinthe="#5c4433")
    S.add(planches(0, 0, 800, y - 14, "#8a7259", larg=44))
    bois = "#4a3628"
    S.add(poly([(0, 0), (300, 0), (0, 300)], cylindre("#5c4433", 0.2, 0.8)))
    S.add(poly([(800, 0), (500, 0), (800, 300)], cylindre("#5c4433", 0.2, 0.8)))
    S.add(planches(0, 0, 300, 300, "#5c4433", forme=poly([(0, 0), (300, 0), (0, 300)], "#000"), larg=30, vertical=False))
    S.add(planches(500, 0, 300, 300, "#5c4433", forme=poly([(800, 0), (500, 0), (800, 300)], "#000"), larg=30, vertical=False))
    S.add(trait(0, 300, 300, 0, bois, 14), trait(800, 300, 500, 0, bois, 14))
    S.add(rect(0, 0, 800, 36, cylindre(bois, 0.2, 0.8, vertical=True)))
    S.add(planches(0, y + 4, 800, 800 - y, "#7a5c43", larg=50, vertical=False))
    S.ambiance("nuit")


def toile_coin(x, y, s=1.0, flip=False):
    """Petite toile d'araignée dans un coin (décor du grenier)."""
    m = [trait(0, 0, 90, 0, "#e9ecef", 1.5, opacity=0.6), trait(0, 0, 0, 90, "#e9ecef", 1.5, opacity=0.6),
         trait(0, 0, 70, 70, "#e9ecef", 1.5, opacity=0.6), trait(0, 0, 85, 40, "#e9ecef", 1.5, opacity=0.6),
         trait(0, 0, 40, 85, "#e9ecef", 1.5, opacity=0.6)]
    for r in (30, 55, 80):
        m.append(chemin(f"M {r} 0 Q {r * 0.75} {r * 0.25} {r * 0.92} {r * 0.42} Q {r * 0.6} {r * 0.6} {r * 0.42} {r * 0.92} "
                        f"Q {r * 0.25} {r * 0.75} 0 {r}", stroke="#e9ecef", sw=1.5, opacity=0.6))
    return place(m, x, y, s, flip=flip)


def lanterne_poutre(S, x, y_fil=36, long=110, s=0.9):
    """Lanterne suspendue à la poutre, et sa lumière."""
    S.add(trait(x, y_fil, x, y_fil + long, "#343a40", 3))
    S.add(lanterne(x, y_fil + long, s))
    S.lumiere(x, y_fil + long + 52 * s, 170, "#ffd43b", 0.55)


def malle(x, y, s=1.0, ouverte=True, debordante=True):
    """Vieille malle de grenier ; (x, y) = milieu du bas."""
    bois, fer = "#8d5524", "#495057"
    m = []
    if ouverte:
        m.append(chemin("M -150 -150 L 150 -150 L 160 -270 Q 0 -310 -160 -270 Z", volume(_assombrir(bois, 0.85), 0.25, 0.8)))
        m.append(chemin("M -140 -160 L 140 -160 L 148 -260 Q 0 -294 -148 -260 Z", "#5c3a1e"))
    if debordante:
        m += [chemin("M -110 -150 Q -150 -190 -120 -220 Q -90 -190 -70 -150 Z", "#e03131"),
              ellipse(-20, -158, 70, 22, "#9775fa"), chemin("M 30 -150 Q 70 -210 120 -170 Q 100 -150 110 -130 Z", "#ffd43b"),
              chemin("M 100 -150 Q 150 -150 170 -90", stroke="#f783ac", sw=10)]
    m += [rect(-150, -150, 300, 150, volume(bois, 0.25, 0.75), rx=10),
          planches(-150, -150, 300, 150, bois, larg=30, vertical=False),
          rect(-150, -150, 300, 16, fer, rx=4), rect(-110, -150, 18, 150, fer), rect(92, -150, 18, 150, fer),
          rect(-16, -136, 32, 30, "#fab005", rx=4), cercle(0, -118, 5, "#495057")]
    return place(m, x, y, s)


def rue(S, sol_y=650, lune_=(650, 130), graine=5):
    nuit(S, "#1a1238", "#4b2f7a")
    etoiles(S, 34, graine, (0, 0, 800, sol_y - 220))
    if lune_:
        S.add(lune(*lune_, 48))
    sol(S, sol_y, "#4a3f6b", bosse=8)


def vieille_maison(x, y, s=1.0, lumiere=True):
    """La vieille maison et sa fenêtre ronde au grenier ; (x, y) = bas de la
    façade. La fenêtre ronde est en (x, y - 470 s), rayon 46 s."""
    mur = "#6f5c96"
    m = [rect(-190, -360, 380, 360, mur), planches(-190, -360, 380, 360, mur, larg=28),
         poly([(-220, -360), (0, -560), (220, -360)], "#3b2a5e"),
         tuiles(-220, -560, 440, 200, "#3b2a5e", forme=poly([(-220, -360), (0, -560), (220, -360)], "#000")),
         rect(110, -520, 40, 110, "#3b2a5e"),
         cercle(0, -440, 56, "#4a3f6b"), cercle(0, -440, 46, "#ffe066" if lumiere else "#1a1238"),
         rect(-4, -486, 8, 92, "#4a3f6b"), rect(-46, -444, 92, 8, "#4a3f6b"),
         rect(-46, -150, 92, 150, "#3b2a5e", rx=8), cercle(28, -76, 6, "#ffd43b")]
    for fx in (-150, 80):
        m += [rect(fx, -290, 70, 84, "#ffe066" if lumiere else "#2b1f45"), rect(fx - 6, -296, 82, 8, "#3b2a5e"),
              rect(fx + 31, -290, 8, 84, "#3b2a5e")]
    return place(m, x, y, s)


def citrouille_deco(S, x, y, s=0.5, allumee=True):
    S.add(citrouille_creusee(x, y, s, allumee=allumee))
    if allumee:
        S.lumiere(x, y - 55 * s, 120 * s, "#ff922b", 0.6)


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rue(S, 660, lune_=(640, 150))
    S.add(vieille_maison(150, 660, 0.75))
    S.lumiere(150, 330, 60, "#ffe066", 0.6)
    S.add(chauve_souris_papier(560, 280, 0.9, rot=-12), chauve_souris_papier(700, 330, 0.7, rot=10))
    S.add(boubou(420, 560, 1.45, expr="rire", bras="haut", regard=(0, 0), brille=True))
    porte_lanterne(S, lea, 250, 780, 1.1, expr="rire", regard=(1, -0.6))
    S.add(hugo(600, 780, 1.1, expr="rire", bras="applaudit", regard=(-1, -0.6)))
    S.add(sami(720, 790, 0.6, expr="rire"))
    citrouille_deco(S, 80, 720, 0.45)
    S.cachette(740, 470, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(cercle(200, 150, 120, radial([(0, "#e5dbff", 0.8), (1, "#e5dbff", 0)])))
    S.add(boubou(200, 262, 1.05, expr="content", bras="salut"))
    return S


def p01():
    """Plan moyen : Boubou regarde passer les enfants par la fenêtre ronde."""
    S = Scene()
    grenier(S)
    S.add(oeil_de_boeuf(500, 270, 150, dehors_nuit(500, 270, 150)))
    S.lumiere(500, 270, 160, "#9775fa", 0.25)
    S.add(toile_coin(36, 36, 0.9))
    lanterne_poutre(S, 150, long=120)
    S.add(malle(680, 760, 0.6, ouverte=False, debordante=False))
    S.add(minuit(680, 670, 0.75, expr="dort", bras="bas", regard=(0, 0)))
    S.add(boubou(250, 660, 1.3, expr="bouche_bee", bras="joues", regard=(1, -0.8)))
    S.add(bulle(260, 230, 300, 100, "Moi aussi, je veux\nun costume !", 28, pointe=(250, 360)))
    return S


def p02():
    """Plan large : la vieille malle pleine de déguisements ; Minuit s'étire."""
    S = Scene()
    grenier(S)
    S.add(toile_coin(764, 36, 0.9, flip=True))
    lanterne_poutre(S, 400, long=90)
    S.add(malle(380, 760, 1.1))
    S.add(boubou(560, 560, 1.15, expr="joie", bras="ouverts", regard=(-1, 0.6)))
    S.add(minuit(140, 760, 1.0, expr="sourire", bras="etire", regard=(1, 0)))
    S.add(bulle(170, 410, 300, 100, "Qu'est-ce que tu\ncherches, Boubou ?", 26, pointe=(150, 520)))
    S.add(bulle(620, 230, 240, 80, "Un costume !", 34, pointe=(580, 320)))
    return S


def p03():
    """Gros plan : le chapeau de sorcière, bien trop grand, tombe sur ses yeux."""
    S = Scene()
    grenier(S)
    lanterne_poutre(S, 640, long=100)
    S.add(malle(160, 780, 0.9))
    S.add(boubou(420, 700, 1.5, expr="oups", bras="haut", regard=(0, 0)))
    # le chapeau, deux fois trop grand, posé jusque sur les yeux
    sh = 1.5 * 1.75
    S.add(place(chapeau_sorciere("#2b2b3a", "#7950f2"), 420, 700 - 150 * 1.5 + 205 * sh, sh))
    S.camera(1.4, 420, 470)
    S.dessus(bulle(400, 90, 420, 80, "Je ne vois plus rien !", 34, pointe=S.vers_page(400, 520)))
    S.cachette(140, 600, "air")
    return S


def p04():
    """Plan moyen : dans la grosse citrouille, Boubou ne peut plus s'envoler."""
    S = Scene()
    grenier(S)
    S.add(toile_coin(36, 36, 0.9))
    lanterne_poutre(S, 620, long=100)
    S.add(malle(660, 790, 0.7))
    S.add(minuit(170, 770, 0.95, expr="malin", bras="hanches", regard=(1, 0)))
    S.add(boubou(420, 640, 1.2, expr="concentre", bras="haut", regard=(0, 0)))
    S.add(citrouille_creusee(420, 780, 2.0, allumee=False, visage=False))
    S.add(mouvement(300, 520, 1.0, "#f8f9fa"), mouvement(560, 540, 1.0, "#f8f9fa", rot=180))
    S.add(texte(420, 330, "Hmpf !", 56, "#fd7e14", contour="#fff", rot=-6))
    S.add(bulle(560, 200, 330, 80, "Elle est trop lourde !", 30, pointe=(470, 420)))
    return S


def p05():
    """Plan large : emmêlé dans la grande cape rouge ; Minuit rit."""
    S = Scene()
    grenier(S)
    lanterne_poutre(S, 160, long=100)
    S.add(malle(640, 780, 0.8))
    S.add(boubou(380, 650, 1.15, expr="oups", bras="ouverts", regard=(0, 0), rot=-24))
    cape = "#e03131"
    S.add(chemin("M 250 470 Q 330 400 430 430 Q 520 470 500 560 Q 470 640 520 720 Q 560 780 640 790 "
                 "L 600 800 Q 470 790 420 700 Q 380 640 300 640 Q 230 620 250 560 Q 300 520 250 470 Z",
                 volume(cape, 0.25, 0.75)))
    S.add(chemin("M 300 470 Q 370 520 330 600 M 430 450 Q 470 520 440 600", stroke=_assombrir(cape, 0.75), sw=4, opacity=0.6))
    S.add(minuit(140, 770, 0.95, expr="rire", bras="joues", regard=(1, 0)))
    S.add(texte(420, 250, "Oups !", 60, "#e03131", contour="#fff", rot=8))
    S.add(mouvement(240, 360, 1.1, "#f8f9fa", rot=-30))
    return S


def p06():
    """Gros plan : Boubou tout triste, une larme ; Minuit se frotte contre lui."""
    S = Scene()
    grenier(S)
    lanterne_poutre(S, 640, long=80)
    S.add(boubou(370, 700, 1.5, expr="triste", bras="bas", regard=(0, 0.5), larmes=True))
    S.add(minuit(560, 780, 1.05, expr="content", bras="tend", flip=True, regard=(-1, -0.5)))
    S.camera(1.3, 440, 520)
    S.dessus(bulle(220, 110, 280, 70, "Rien ne me va…", 30, pointe=S.vers_page(360, 430)),
             bulle(560, 190, 380, 110, "Et si tu sortais comme tu es ?\nTu es déjà un fantôme !", 24, pointe=S.vers_page(560, 520)))
    S.cachette(110, 640, "air")
    return S


def p07():
    """Plan large en diagonale : Boubou descend de la fenêtre ronde vers la rue."""
    S = Scene()
    rue(S, 660, lune_=(680, 110))
    S.add(vieille_maison(200, 660, 1.0))
    S.lumiere(200, 220, 70, "#ffe066", 0.6)
    S.add(chemin("M 210 230 Q 260 250 290 290", stroke="#e7f5ff", sw=6, opacity=0.35, stroke_dasharray="4 14"))
    S.add(boubou(340, 440, 0.85, expr="timide", bras="bas", regard=(1, 1), rot=-12, brille=True))
    porte_lanterne(S, lea, 520, 760, 0.85, expr="sourire", regard=(1, 0))
    S.add(hugo(630, 765, 0.85, expr="rire", bras="marche", regard=(-1, 0)))
    S.add(sami(730, 775, 0.48))
    citrouille_deco(S, 400, 720, 0.4)
    return S


def p08():
    """Plan moyen : les enfants admirent le « costume » de Boubou."""
    S = Scene()
    rue(S, 650, lune_=(110, 110))
    S.add(maison(660, 650, 0.8, mur="#8c7ab8", toit="#3b2a5e", lumiere=True, cheminee=False))
    S.add(boubou(400, 540, 1.15, expr="timide", bras="joues", regard=(0, 0.5), rougit=True, brille=True))
    porte_lanterne(S, lea, 170, 780, 1.15, expr="rire", regard=(1, -0.5))
    S.add(hugo(670, 785, 1.1, expr="joie", bras="applaudit", regard=(-1, -0.5)))
    S.add(sami(520, 790, 0.62, expr="rire"))
    S.add(bulle(190, 150, 320, 100, "Quel beau costume !\nIl flotte, en plus !", 26, pointe=(170, 500)))
    S.add(bulle(620, 170, 300, 100, "Un fantôme,\ncomme moi !", 32, pointe=(520, 640)))
    return S


def p09():
    """Plan moyen : chez Madame Lucie, « Des bonbons ou un sort ! »"""
    S = Scene()
    rue(S, 660, lune_=None)
    S.add(rect(360, 120, 440, 560, "#7a6aa8"), planches(360, 120, 440, 560, "#7a6aa8", larg=30))
    S.add(rect(470, 250, 210, 430, "#ffe8a3"), rect(460, 240, 230, 12, "#3b2a5e"))
    S.lumiere(575, 450, 210, "#ffd43b", 0.55)
    S.add(chauve_souris_papier(420, 190, 0.7), chauve_souris_papier(740, 200, 0.8, rot=12))
    S.add(lucie(590, 690, 1.25, expr="rire", bras="tend", flip=True, regard=(-1, 0.3),
                objet=g([ellipse(96, -100, 46, 16, "#74c0fc"), cercle(80, -110, 9, "#f06595"), cercle(100, -114, 9, "#ffd43b"),
                         cercle(116, -108, 9, "#69db7c")])))
    for k, c in enumerate(("#f06595", "#74c0fc", "#ffd43b")):
        S.add(bonbon(380 + k * 40, 420 + (k % 2) * 30, 1.0, c, rot=k * 50))
    S.add(boubou(330, 600, 1.0, expr="malin", bras="tend", regard=(1, -0.3), brille=True))
    porte_lanterne(S, lea, 140, 780, 1.05, expr="rire", regard=(1, -0.3))
    S.add(hugo(250, 790, 0.95, expr="rire", bras="tient", regard=(1, -0.3), objet=seau_bonbons(68, -146, 0.8)))
    S.add(sami(60, 795, 0.5))
    S.add(bulle(200, 150, 330, 100, "Des bonbons\nou un sort !", 34, pointe=(200, 500)))
    S.add(bulle(620, 120, 330, 80, "On dirait un vrai !", 30))
    S.cachette(760, 740)
    return S


def p10():
    """Plan large : le vent souffle les lanternes ; Boubou brille dans le noir."""
    S = Scene()
    nuit(S, "#0b0820", "#1f1640")
    etoiles(S, 20, 9, (0, 0, 800, 300))
    sol(S, 660, "#2b2445", bosse=8)
    S.add(maison(120, 660, 0.7, mur="#3b2a5e", toit="#1f1640", lumiere=False, cheminee=False))
    S.add(maison(700, 660, 0.6, mur="#3b2a5e", toit="#1f1640", lumiere=False))
    for k in range(5):
        S.add(chemin(f"M {40 + k * 30} {200 + k * 40} q 120 -30 240 0 q 60 14 100 -10", stroke="#adb5bd", sw=4, opacity=0.4))
    S.add(texte(240, 160, "Pfiou !", 52, "#adb5bd", rot=-8))
    S.add(boubou(560, 560, 1.15, expr="rire", bras="montre", regard=(-1, 0), brille=True))
    S.lumiere(560, 450, 330, "#d0ebff", 0.55)
    S.lumiere(470, 760, 260, "#d0ebff", 0.35, ry=60)
    porte_lanterne(S, lea, 230, 780, 1.0, allumee=False, expr="surpris", regard=(1, -0.5))
    S.add(hugo(370, 785, 1.0, expr="inquiet", bras="joues", regard=(1, -0.5)))
    S.add(sami(110, 790, 0.55))
    S.add(bulle(640, 230, 260, 80, "Suivez-moi !", 34, pointe=(590, 340)))
    S.cachette(760, 740)
    return S


def p11():
    """Plan large : au revoir sous la fenêtre ronde ; Boubou dans son grenier."""
    S = Scene()
    rue(S, 660, lune_=(640, 120))
    S.add(vieille_maison(400, 690, 1.05))
    S.lumiere(400, 228, 80, "#ffe066", 0.6)
    S.add(boubou(400, 266, 0.32, expr="rire", bras="salut", regard=(0, 1)))
    S.add(lea(140, 790, 0.95, expr="rire", bras="coucou", regard=(1, -1)))
    S.add(hugo(650, 790, 0.95, expr="rire", bras="coucou", flip=True, regard=(-1, -1)))
    S.add(sami(250, 795, 0.5, expr="rire"))
    citrouille_deco(S, 740, 790, 0.4)
    S.add(bulle(200, 120, 320, 80, "À l'an prochain !", 32))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("boubou-seul.svg", vignette),
    ("01-la-fenetre-ronde.svg", p01), ("02-la-malle.svg", p02), ("03-le-chapeau.svg", p03),
    ("04-la-citrouille.svg", p04), ("05-la-cape.svg", p05), ("06-rien-ne-me-va.svg", p06),
    ("07-vers-la-rue.svg", p07), ("08-quel-beau-costume.svg", p08), ("09-des-bonbons.svg", p09),
    ("10-le-vent.svg", p10), ("11-a-l-an-prochain.svg", p11),
]
