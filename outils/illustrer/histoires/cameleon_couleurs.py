"""Le caméléon change de couleur — le caméléon panthère de Madagascar.

Ses yeux bougent chacun de son côté. Il avance lentement en se balançant
comme une feuille, ses pattes serrent les branches comme des pinces et sa
queue s'y enroule. Sa langue jaillit, plus longue que son corps, avec un bout
collant. Il change de couleur surtout pour montrer ce qu'il ressent et pour
régler sa température (plus foncé quand il a froid, pour mieux chauffer au
soleil), et pâlit la nuit en dormant. Sa couleur verte suffit déjà à le
cacher dans les feuilles.
"""
from base import *
from base import _assombrir
from animaux import *
from sciences import fleche, enfant, fleche_courbe

ID = "cameleon-couleurs"
VERT = "#69db7c"
VERT_F = "#2f9e44"


# --- Personnages ------------------------------------------------------------

def cameleon(x, y, s=1.0, flip=False, rot=0, corps=VERT, bandes="#94d82d", ventre="#d8f5a2", yeux=((1, 0), (1, 0)),
             expr="sourire", langue=0, gonfle=False, dort=False):
    """Caméléon de profil sur une branche, tête à droite ; (x, y) = sous les
    pattes, sur la branche. yeux : regard de chacun des deux yeux (on voit
    l'œil de devant et le bout de l'autre) ; langue : longueur de la langue
    tirée vers la droite."""
    ys, bs, ss = EXPRESSIONS[expr if not dort else "dort"]
    fonce = _assombrir(corps, 0.8)
    m = []
    # queue enroulée
    m.append(chemin("M -110 -60 Q -170 -40 -170 20 Q -170 70 -130 70 Q -96 70 -96 40 Q -96 18 -118 18 Q -136 18 -134 36",
                    stroke=corps, sw=18))
    # pattes du fond
    for px in (-60, 70):
        m.append(chemin(f"M {px} -50 L {px - 10} -20 L {px} 0", stroke=fonce, sw=14))
    # corps
    corps_d = "M -120 -70 Q -110 -150 0 -160 Q 80 -164 110 -120 Q 120 -70 90 -40 Q 0 -20 -100 -40 Q -124 -50 -120 -70 Z"
    cid = uid("cm")
    m.append(el("clipPath", chemin(corps_d, "#000"), id=cid))
    m.append(chemin(corps_d, corps))
    deco = [ellipse(0, -40, 130, 26, ventre)]
    for k in range(6):
        deco.append(chemin(f"M {-90 + k * 36} -150 Q {-80 + k * 36} -100 {-96 + k * 36} -50", stroke=bandes, sw=12))
    m.append(g(deco, clip_path=f"url(#{cid})"))
    if gonfle:
        m.insert(3, chemin("M -110 -120 Q 0 -230 100 -130", stroke=fonce, sw=16))
    # crête
    for k in range(8):
        m.append(poly([(-100 + k * 26, -150 + (k - 4) ** 2 * 0.4), (-88 + k * 26, -168 + (k - 4) ** 2 * 0.4), (-76 + k * 26, -150 + (k - 4) ** 2 * 0.4)], fonce))
    # tête avec casque
    m.append(chemin("M 80 -150 Q 110 -200 150 -170 Q 200 -150 200 -110 Q 190 -76 140 -74 Q 96 -76 80 -110 Z", corps))
    m.append(chemin("M 82 -150 Q 120 -210 150 -172", stroke=fonce, sw=6))
    m.append(chemin("M 196 -104 Q 160 -90 120 -100", stroke=ENCRE, sw=3.5))
    m.append(joue(180, -96, 0.8))
    if langue:
        L = langue
        m.append(chemin(f"M 196 -104 L {196 + L} -110", stroke="#ff8fab", sw=8))
        m.append(cercle(196 + L, -110, 14, "#f06595"))
    # œil en tourelle
    (gx, gy), (dx_, dy_) = yeux
    m.append(cercle(150, -130, 24, corps))
    m.append(cercle(150, -130, 24, "none", stroke=fonce, stroke_width=3))
    if dort:
        m.append(oeil(150, -130, "fermes", taille=1.1))
    else:
        m.append(cercle(150 + gx * 12, -130 + gy * 12, 9, "#ffffff"))
        m.append(cercle(150 + gx * 14, -130 + gy * 14, 5.5, ENCRE))
    # bout de l'autre œil, de l'autre côté de la tête
    m.append(chemin("M 132 -154 Q 140 -170 154 -162", stroke=fonce, sw=8))
    # pattes de devant, en pince
    for px in (-40, 90):
        m.append(chemin(f"M {px} -50 L {px + 14} -20 L {px} 0", stroke=corps, sw=16))
        m.append(chemin(f"M {px - 12} 4 Q {px} -8 {px + 12} 4", stroke=corps, sw=8))
    return place(m, x, y, s, flip=flip, rot=rot)


def branche(S, y=520, x0=-20, x1=820, ep=26, feuilles=True):
    S.add(chemin(f"M {x0} {y + 10} Q {(x0 + x1) / 2} {y - 10} {x1} {y}", stroke="#7c4a1e", sw=ep))
    if feuilles:
        for k, x in enumerate(range(60, 800, 140)):
            S.add(place([chemin("M 0 0 Q 30 -30 70 -10 Q 34 14 0 0 Z", "#40c057"), trait(4, 0, 66, -8, "#2f9e44", 2)],
                        x, y + 10, 1.1, rot=-30 if k % 2 else 150))


def foret(S, haut="#c3fae8", bas="#ebfbee", nuit_=False):
    if nuit_:
        nuit(S, "#1c2a52", "#364fc7")
        etoiles(S, 30, 2, (0, 0, 800, 400))
        S.add(lune(660, 110, 38))
    else:
        S.add(rect(0, 0, 800, 800, S.degrade([haut, bas])))
    r = random.Random(3)
    for _ in range(9):
        cx, cy = r.uniform(0, 800), r.uniform(0, 300)
        S.add(ellipse(cx, cy, r.uniform(80, 160), r.uniform(50, 90), "#8ce99a" if not nuit_ else "#2b3a55", opacity=0.6))


def grillon(x, y, s=1.0, rot=0):
    m = [chemin("M -10 -6 L -40 -30 L -50 4", stroke="#5c3a1e", sw=4), ellipse(0, 0, 30, 12, "#8d5524"),
         cercle(28, -2, 10, "#6d4424"), chemin("M 34 -8 Q 60 -40 80 -36 M 34 -8 Q 64 -30 86 -16", stroke="#5c3a1e", sw=2),
         cercle(32, -5, 2.5, ENCRE)]
    return place(m, x, y, s, rot=rot)


# --- Pages ------------------------------------------------------------------

def couverture():
    S = Scene()
    foret(S)
    branche(S, 600)
    S.add(cameleon(380, 590, 1.6, corps="#4dabf7", bandes="#ff922b", ventre="#ffe066", expr="content"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(chemin("M 0 212 Q 200 196 400 208", stroke="#7c4a1e", sw=14))
    S.add(cameleon(195, 204, 0.8, corps="#4dabf7", bandes="#ff922b", ventre="#ffe066", expr="content"))
    return S


def p01():
    S = Scene()
    foret(S)
    branche(S, 560)
    S.add(cameleon(380, 552, 1.5, expr="sourire"))
    S.add(texte(400, 160, "Madagascar", 50, "#2b8a3e", contour="#fff"))
    return S


def p02():
    S = Scene()
    foret(S)
    branche(S, 600)
    S.add(cameleon(330, 592, 1.7, yeux=((-1, 0), (1, 0)), expr="malin"))
    S.add(fleche(560, 360, 720, 330, "#e8590c", 6, 22), fleche(100, 360, 40, 330, "#e8590c", 6, 22))
    S.add(coccinelle_(720, 260))
    S.add(mouche(60, 260, 1.4))
    return S


def coccinelle_(x, y):
    from objets import coccinelle
    return coccinelle(x, y, 1.6)


def p03():
    S = Scene()
    foret(S)
    branche(S, 560, ep=30)
    S.add(cameleon(330, 552, 1.3, rot=-6, expr="concentre"))
    S.add(texte(560, 260, "Doucement…", 50, "#2b8a3e", contour="#fff"))
    S.add(loupe(640, 680, 90, [rect(550, 590, 180, 180, "#7c4a1e"), chemin("M 620 640 L 640 680 L 620 720", stroke=VERT, sw=26),
                                chemin("M 600 730 Q 640 700 680 730", stroke=VERT, sw=14)], fond="#c3fae8", rot=-140))
    return S


def p04():
    S = Scene()
    foret(S)
    branche(S, 560)
    S.add(cameleon(220, 552, 1.2, yeux=((1, 0), (1, 0)), expr="concentre"))
    S.add(grillon(620, 450, 1.6))
    S.add(chemin("M 450 470 L 520 460", stroke="#868e96", sw=3, stroke_dasharray="8 8"))
    return S


def p05():
    S = Scene()
    foret(S)
    branche(S, 560)
    S.add(cameleon(160, 552, 1.0, expr="concentre", langue=380))
    S.add(grillon(560, 450, 1.4))
    S.add(texte(420, 300, "Flip !", 80, "#e64980", contour="#fff", rot=-6))
    return S


def p06():
    S = Scene()
    fond(S, "#fff9db")
    S.add(cameleon(220, 330, 0.8, corps="#69db7c", bandes="#94d82d", ventre="#d8f5a2"))
    S.add(cameleon(560, 330, 0.8, corps="#4dabf7", bandes="#ff922b", ventre="#ffe066"))
    S.add(cameleon(220, 680, 0.8, corps="#ff6b6b", bandes="#ffd43b", ventre="#ffe3e3"))
    S.add(cameleon(560, 680, 0.8, corps="#845ef7", bandes="#20c997", ventre="#e5dbff"))
    return S


def p07():
    S = Scene()
    S.add(rect(0, 0, 800, 800, S.degrade(["#ffd8a8", "#fff9db"])))
    S.add(soleil(640, 160, 80, visage=True))
    branche(S, 600)
    S.add(cameleon(320, 592, 1.4, corps="#2b8a3e", bandes="#1b5e20", ventre="#69db7c", expr="content"))
    S.add(texte(280, 200, "Brrr… le soleil !", 44, "#e8590c", contour="#fff"))
    return S


def p08():
    S = Scene()
    foret(S)
    branche(S, 600)
    S.add(cameleon(220, 592, 1.0, corps="#fa5252", bandes="#ffd43b", ventre="#ffe066", expr="fache", gonfle=True))
    S.add(cameleon(590, 592, 1.0, flip=True, corps="#4dabf7", bandes="#ff922b", ventre="#ffe066", expr="surpris"))
    S.add(texte(400, 200, "C'est ma branche !", 46, "#c92a2a", contour="#fff"))
    return S


def p09():
    S = Scene()
    foret(S, nuit_=True)
    branche(S, 600)
    S.add(cameleon(360, 592, 1.4, corps="#e9fac8", bandes="#f4fce3", ventre="#ffffff", dort=True))
    S.add(zzz(600, 330, 1.2, "#ffe066"))
    return S


def p10():
    S = Scene()
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(rect(0, 600, 800, 200, "#8ce99a"))
    S.add(enfant(560, 760, 1.6, expr="timide", bras="joues", habit="#ffa94d", jambes="#364fc7", regard=(-1, 0)))
    S.add(chemin("M 0 380 Q 200 360 380 380", stroke="#7c4a1e", sw=20))
    for x in (60, 200, 320):
        S.add(place([chemin("M 0 0 Q 30 -30 70 -10 Q 34 14 0 0 Z", "#40c057")], x, 384, 1.2, rot=150))
    S.add(cameleon(200, 374, 0.9, expr="rire", yeux=((1, 0.3), (1, 0))))
    S.add(texte(400, 160, "Toi aussi, tu rougis !", 44, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("cameleon-seul.svg", vignette),
    ("01-sur-sa-branche.svg", p01), ("02-les-yeux.svg", p02), ("03-tout-doucement.svg", p03),
    ("04-un-grillon.svg", p04), ("05-la-langue.svg", p05), ("06-les-couleurs.svg", p06),
    ("07-il-a-froid.svg", p07), ("08-en-colere.svg", p08), ("09-la-nuit.svg", p09),
    ("10-et-toi.svg", p10),
]
