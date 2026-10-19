"""Le bambou aux cent nœuds — d'après un conte du Viêt Nam (Cây tre trăm đốt).

Khoai, un jeune paysan courageux, travaille pour un riche propriétaire
qui lui promet : « Travaille trois ans pour moi, et tu épouseras ma
fille. » Les trois ans passés, le riche, qui veut la marier à un autre,
invente une épreuve : « Rapporte-moi un bambou de cent nœuds ! » Dans la
forêt, aucun bambou n'en a autant. Khoai pleure ; un vieux sage (Bụt)
apparaît : « Coupe cent morceaux et dis : Khắc nhập ! » Les morceaux
s'emboîtent ; « Khắc xuất ! », ils se séparent. À la fête, le riche touche
le bambou : « Khắc nhập ! » et le voilà collé ! Il promet de tenir parole ;
« Khắc xuất ! », il est libre. Khoai et la jeune fille, qui l'aime aussi,
se marient. Tout se finit dans les rires.

Plans : 1 large (la rizière, la promesse) · 2 moyen (l'épreuve) · 3 large
(la forêt de bambous) · 4 moyen (le vieux sage) · 5 gros plan (Khắc nhập !)
· 6 large (le bambou géant) · 7 moyen (la fête) · 8 gros plan (collé !) ·
9 moyen (le mariage).
"""
from contes import *
from base import _assombrir

ID = "bambou-cent-noeuds"


def non_la(c="#f1d9a6"):
    """Chapeau conique vietnamien en feuilles (coiffe)."""
    return g([poly([(-96, -176), (0, -270), (96, -176)], volume(c, 0.3, 0.8)), chemin("M -96 -176 Q 0 -164 96 -176", stroke=_assombrir(c, 0.75), sw=4),
              chemin("M -64 -208 Q 0 -200 64 -208 M -34 -238 Q 0 -232 34 -238", stroke=_assombrir(c, 0.8), sw=2)])


def khan(c="#212529"):
    """Turban noir enroulé du riche propriétaire (coiffe)."""
    return g([ellipse(0, -204, 62, 26, c), chemin("M -60 -204 Q 0 -230 60 -204 M -58 -196 Q 0 -218 58 -196", stroke="#495057", sw=3)])


KHOAI = dict(stature="ado", peau="doree", cheveux="noir", coiffure="courts", habit="#5c940d", robe=False, jambes="#343a40", nez="rond",
             coiffe=non_la())
RICHE = dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chauve_cote", habit="#7048e8", robe=True, carrure="ronde",
             barbe="#343a40", nez="long", ceinture="#fab005", coiffe=khan())
FILLE = dict(stature="ado", peau="doree", cheveux="noir", coiffure="tres_longs", habit="#f06595", robe=True, yeux="cils", nez="petit")
SAGE = dict(stature="ancien", peau="doree", cheveux="blanc", coiffure="chauve", habit="#f8f9fa", robe=True, barbe="#f8f9fa", carrure="fine",
            nez="long")
VILLAGEOIS = [dict(stature="adulte", peau="doree", cheveux="noir", coiffure="chignon", habit="#1c7ed6", robe=False, jambes="#495057"),
              dict(stature="ancien", peau="doree", cheveux="gris", coiffure="chignon", habit="#e8590c", robe=True, carrure="ronde")]
BAMBOU = "#94d82d"


def bambou(x0, y0, x1, y1, nb=10, ep=18, c=BAMBOU, ecarte=0.0):
    """Un bambou droit de nb nœuds, de (x0, y0) à (x1, y1) ; ecarte > 0 : morceaux séparés."""
    m = []
    dx, dy = (x1 - x0) / nb, (y1 - y0) / nb
    long_ = math.hypot(dx, dy)
    ux, uy = dx / long_, dy / long_
    for k in range(nb):
        ax, ay = x0 + k * dx + k * ux * ecarte, y0 + k * dy + k * uy * ecarte
        bx, by = ax + dx * 0.96, ay + dy * 0.96
        m.append(trait(ax, ay, bx, by, c, ep))
        m.append(trait(ax, ay, bx, by, eclaircir(c, 0.4), ep * 0.25, opacity=0.6))
        m.append(trait(bx - ux * 2, by - uy * 2, bx + ux * 2, by + uy * 2, _assombrir(c, 0.7), ep * 1.15))
    return g(m)


def touffe_bambous(x, y, s=1.0, h=520, graine=1):
    """Une touffe de bambous qui montent tout droit, avec leurs feuilles ; (x, y) = pied."""
    r = random.Random(graine)
    m = []
    for k in range(5):
        bx = -60 + k * 30 + r.uniform(-6, 6)
        hh = h * r.uniform(0.75, 1.0)
        m.append(bambou(bx, 0, bx + r.uniform(-20, 20), -hh, nb=int(hh // 60), ep=14, c=r.choice(("#82c91e", "#94d82d", "#74b816"))))
        for j in range(4):
            yy = -hh * (0.5 + j * 0.15)
            sgn = 1 if (j + k) % 2 else -1
            m.append(place([ellipse(30, 0, 34, 7, "#40c057"), ellipse(26, 10, 28, 6, "#2f9e44", rot=20)], bx, yy, 1.0, flip=sgn < 0, rot=-20))
    return place(m, x, y, s)


def maison_paysanne(x, y, s=1.0, mur="#e9d8a6", lumiere=False):
    """Maison de terre au toit de chaume ; (x, y) = milieu du seuil."""
    toit = poly([(-170, -150), (0, -260), (170, -150)], "#000")
    m = [rect(-140, -150, 280, 150, terrain(mur)), rect(-34, -110, 68, 110, "#8d5524"),
         rect(-110, -110, 50, 44, "#ffe066" if lumiere else "#495057"), rect(60, -110, 50, 44, "#ffe066" if lumiere else "#495057"),
         poly([(-170, -150), (0, -260), (170, -150)], volume("#c5a07a", 0.3, 0.8)), chaume(-170, -260, 340, 110, "#c5a07a", forme=toit)]
    return place(m, x, y, s)


def rizieres(S, horizon=500, soir=False):
    ciel(S, "#ff922b" if soir else "#74c0fc", "#fff4e6")
    lointain(S, horizon - 10, "#8ce99a", 120, graine=5, opacite=0.5)
    for k in range(4):
        yy = horizon + k * 70
        S.add(chemin(f"M -20 {yy} Q 400 {yy - 24} 820 {yy} L 820 800 L -20 800 Z", "#9be3c4" if k % 2 else "#8ce99a"))
        S.add(chemin(f"M -20 {yy} Q 400 {yy - 24} 820 {yy}", stroke="#5c940d", sw=6))
        for j in range(18):
            S.add(chemin(f"M {j * 46 + (k % 2) * 20} {yy + 40} l -4 -14 M {j * 46 + (k % 2) * 20} {yy + 40} l 4 -16", stroke="#2f9e44", sw=3))
    S.cachette(40, 790)


def foret_bambous(S, graine=2):
    ciel(S, "#a9e34b", "#f4fce3")
    S.add(rect(0, 0, 800, 800, "#d8f5a2", opacity=0.3))
    for k in range(7):
        S.add(touffe_bambous(60 + k * 115, 640, 0.9 + (k % 2) * 0.2, h=640, graine=graine + k))
    sol(S, 640, "#a9e34b")


# ---------------------------------------------------------------------------

def couverture():
    S = Scene()
    rizieres(S, 520)
    S.add(maison_paysanne(650, 560, 0.6))
    S.add(bambou(80, 760, 560, 40, nb=24, ep=20))
    S.add(personne(320, 790, 1.5, expr="rire", bras="ouverts", regard=(1, -1), **KHOAI))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(bambou(60, 220, 340, 50, nb=8, ep=22))
    return S


def p01():
    """Plan large : dans la rizière, Khoai, coiffé de son chapeau conique, repique le riz ; le riche propriétaire lui fait une promesse."""
    S = Scene()
    rizieres(S, 480)
    S.add(maison_paysanne(150, 520, 0.55))
    S.add(personne(330, 790, 1.2, expr="concentre", bras="ramasse", regard=(1, 0.5), **KHOAI))
    S.add(personne(600, 790, 1.2, expr="malin", bras="leve_doigt", flip=True, regard=(-1, 0), **RICHE))
    S.add(bulle(450, 160, 560, 110, "Travaille trois ans pour moi,\net tu épouseras ma fille !", 30, pointe=(590, 420)))
    return S


def p02():
    """Plan moyen : trois ans ont passé ; le riche, qui veut marier sa fille à un autre, invente une épreuve : « Rapporte-moi un bambou de cent nœuds ! »"""
    S = Scene()
    rizieres(S, 480, soir=True)
    S.add(maison_paysanne(620, 600, 0.75, lumiere=True))
    S.add(personne(560, 790, 1.35, expr="malin", bras="designe", flip=True, regard=(-1, 0), **RICHE))
    S.add(personne(240, 790, 1.25, expr="surpris", bras="surprise", regard=(1, 0), **KHOAI))
    S.add(personne(760, 790, 1.0, expr="triste", bras="mains_basses", flip=True, regard=(-1, 0), **FILLE))
    S.add(bulle(400, 150, 560, 90, "Un bambou de cent nœuds !", 34, pointe=(500, 400)))
    return S


def p03():
    """Plan large : dans la forêt de bambous, Khoai compte les nœuds d'une tige : « … dix-neuf, vingt… » ; aucun bambou n'en a cent."""
    S = Scene()
    foret_bambous(S)
    S.add(personne(400, 780, 1.1, expr="concentre", bras="montre", regard=(0.5, -1), **KHOAI))
    S.add(texte(400, 110, "… dix-neuf, vingt…", 44, "#2b8a3e", contour="#fff"))
    return S


def p04():
    """Plan moyen : Khoai, assis, pleure ; un vieux sage à la longue barbe blanche apparaît dans une lumière : « Pourquoi pleures-tu ? »"""
    S = Scene()
    foret_bambous(S, graine=8)
    S.lumiere(560, 600, 220, "#fff3bf", 0.7)
    S.add(personne(560, 780, 1.35, expr="sourire", bras="tend", flip=True, regard=(-1, 0.3), **SAGE))
    S.add(etincelles(560, 560, 1.6, "#fff3bf", graine=4))
    S.add(personne(260, 790, 1.2, expr="pleure", bras="yeux", larmes=True, sy=0.85, **KHOAI))
    S.add(bulle(400, 150, 420, 90, "Pourquoi pleures-tu ?", 34, pointe=(540, 380)))
    return S


def p05():
    """Gros plan : cent petits morceaux de bambou en tas ; Khoai crie « Khắc nhập ! » et les morceaux s'envolent pour s'emboîter."""
    S = Scene()
    foret_bambous(S, graine=3)
    r = random.Random(5)
    for k in range(18):
        x, y = r.uniform(380, 700), r.uniform(680, 770)
        a = r.uniform(0, math.pi)
        S.add(bambou(x, y, x + 50 * math.cos(a), y - 50 * math.sin(a), nb=1, ep=16))
    S.add(bambou(420, 640, 720, 300, nb=6, ep=16, ecarte=14))
    S.add(mouvement(600, 420, 1.0, rot=-50), etincelles(560, 460, 1.0, "#ffd43b"))
    S.add(personne(240, 790, 1.4, expr="joie", bras="designe", regard=(1, -0.3), **KHOAI))
    S.camera(1.3, 420, 560)
    S.dessus(texte(400, 100, "Khắc nhập ! Khắc nhập !", 46, "#e8590c", contour="#fff"))
    S.cachette(720, 795)
    return S


def p06():
    """Plan large : voilà un bambou immense de cent nœuds, si long qu'il dépasse les arbres ; Khoai rit : « Khắc xuất ! » pour le porter en morceaux."""
    S = Scene()
    rizieres(S, 520)
    S.add(bambou(60, 770, 760, 30, nb=40, ep=18))
    S.add(personne(500, 790, 1.15, expr="rire", bras="ventre", regard=(-1, -1), **KHOAI))
    S.add(oiseau(560, 240, 0.45, "#ffd43b", ailes="haut", flip=True))
    S.add(bulle(250, 420, 400, 90, "Cent nœuds… et plus !", 32, pointe=(470, 560)))
    return S


def p07():
    """Plan moyen : à la fête, devant la maison décorée, Khoai pose le bambou ; le riche ricane et pose la main dessus : « Ce n'est qu'un bâton ! »"""
    S = Scene()
    rizieres(S, 480)
    S.add(maison_paysanne(400, 560, 0.75))
    for k in range(5):
        S.add(cercle(260 + k * 70, 330 + (k % 2) * 16, 14, "#e03131"))
    S.add(bambou(60, 690, 760, 610, nb=14, ep=18))
    S.add(personne(180, 790, 1.2, expr="malin", bras="dos", regard=(1, 0), **KHOAI))
    S.add(personne(560, 790, 1.25, expr="malin", bras="pousse", flip=True, regard=(-1, 0.5), **RICHE))
    S.add(personne(720, 790, 1.0, expr="inquiet", bras="mains_jointes", flip=True, regard=(-1, 0), **FILLE))
    S.add(bulle(520, 160, 440, 90, "Ce n'est qu'un bâton !", 34, pointe=(560, 440)))
    return S


def p08():
    """Gros plan : « Khắc nhập ! » Le riche est collé au bambou, les mains et le ventre dessus ; il gigote : « Au secours ! Décolle-moi ! »"""
    S = Scene()
    rizieres(S, 480)
    S.add(personne(420, 790, 1.5, expr="oups", bras="tend", regard=(0, 1), **RICHE))
    S.add(bambou(80, 650, 760, 640, nb=14, ep=22))
    S.add(mouvement(240, 520, 1.2), mouvement(600, 520, 1.2, rot=180))
    S.camera(1.35, 420, 540)
    S.dessus(bulle(400, 100, 560, 90, "Au secours ! Décolle-moi !", 34))
    S.cachette(700, 795)
    return S


def p09():
    """Plan moyen : « Khắc xuất ! » Le riche, libéré, tient enfin parole ; Khoai et la jeune fille se tiennent la main ; les villageois rient."""
    S = Scene()
    rizieres(S, 480, soir=True)
    S.add(maison_paysanne(400, 560, 0.75, lumiere=True))
    for k in range(5):
        S.add(cercle(260 + k * 70, 330 + (k % 2) * 16, 14, "#e03131"))
        S.lumiere(260 + k * 70, 330 + (k % 2) * 16, 30, "#ffa94d", 0.5)
    S.add(personne(340, 790, 1.25, expr="content", bras="main", regard=(1, 0), **KHOAI))
    S.add(personne(470, 790, 1.15, expr="rire", bras="main", flip=True, regard=(-1, 0), **FILLE))
    S.add(personne(640, 790, 1.15, expr="timide", bras="gratte", flip=True, regard=(-1, 0), **RICHE))
    S.add(personne(150, 790, 1.1, expr="rire", bras="applaudit", regard=(1, 0), **VILLAGEOIS[0]))
    S.add(personne(760, 790, 1.0, expr="rire", bras="ventre", flip=True, regard=(-1, 0), **VILLAGEOIS[1]))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("bambou-seul.svg", vignette),
    ("01-la-promesse.svg", p01), ("02-l-epreuve.svg", p02), ("03-la-foret.svg", p03),
    ("04-le-vieux-sage.svg", p04), ("05-khac-nhap.svg", p05), ("06-cent-noeuds.svg", p06),
    ("07-la-fete.svg", p07), ("08-colle.svg", p08), ("09-le-mariage.svg", p09),
]
