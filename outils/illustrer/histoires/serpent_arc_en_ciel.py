"""Le Serpent arc-en-ciel — d'après une légende des Aborigènes d'Australie.

Au Temps du Rêve, la terre est plate, vide et silencieuse ; les animaux
dorment dessous. Le Serpent arc-en-ciel se réveille, sort de terre et
parcourt le pays : son corps creuse les vallées et les lits des rivières,
pousse les collines. Il appelle les grenouilles, qui dorment le ventre plein
d'eau, et les chatouille : elles rient, l'eau jaillit et remplit rivières et
trous d'eau. L'herbe et les arbres poussent, les animaux s'éveillent et
trouvent leur place. Le Serpent leur demande de prendre soin de la terre et
de partager l'eau, puis il se repose au fond d'un trou d'eau. L'arc-en-ciel,
après la pluie, c'est lui qui passe d'un trou d'eau à l'autre.

Les peuples aborigènes racontent ce récit de bien des façons ; ce livre en
donne une version simple, sans imiter leurs peintures sacrées.
Arc-en-ciel exact : rouge à l'extérieur, et jamais du côté du Soleil (le
Soleil est dans le dos de qui le regarde, hors de l'image).

Plans : couverture large · 1 large (la terre plate et vide) · 2 coupe du sol
(les animaux endormis) · 3 gros plan (le réveil) · 4 plongée large (les
vallées et les collines) · 5 moyen (les grenouilles) · 6 gros plan (les
chatouilles) · 7 large (la terre verte) · 8 large (les animaux) · 9 moyen
(la promesse) · 10 moyen au soir (le trou d'eau) · 11 large (l'arc-en-ciel).
"""
from base import *
from base import _assombrir
from objets import arc_en_ciel
from animaux import coupe_terre
from histoires.kangourou_poche import kangourou, eucalyptus

ID = "serpent-arc-en-ciel"

ARC = ("#ff6b6b", "#ffa94d", "#ffd43b", "#69db7c", "#4dabf7", "#9775fa")
TERRE = "#e8a35a"
OCRE = "#d9822b"


# --- Le Serpent ------------------------------------------------------------------

def corps_serpent(d, ep=60):
    """Corps rayé aux couleurs de l'arc-en-ciel le long du chemin `d` :
    rouge sur les bords, violet au milieu."""
    m = [chemin(d, stroke="#5f3dc4", sw=ep + 8)]
    for k, c in enumerate(ARC):
        m.append(chemin(d, stroke=c, sw=ep * (1 - k / len(ARC))))
    m.append(chemin(d, stroke="#ffffff", sw=ep * 0.06, opacity=0.5, stroke_dasharray=f"{n(ep * 0.3)} {n(ep * 0.5)}"))
    return g(m)


def tete_serpent(x, y, s=1.0, angle=0, expr="sourire", regard=(1, 0), langue=False):
    """Tête du Serpent, le museau dans la direction `angle` (degrés, 0 = vers
    la droite) ; (x, y) = cou. Les yeux restent en haut."""
    ys, bs, ss = EXPRESSIONS[expr]
    m = []
    if langue:
        m.append(chemin("M 110 14 L 150 14 L 166 2 M 150 14 L 166 24", stroke="#e03131", sw=4))
    # crête aux couleurs de l'arc-en-ciel
    for k, c in enumerate(ARC):
        m.append(ellipse(10 + k * 9, -40 + abs(k - 2.5) * 3, 9, 16, c, rot=-20))
    m.append(ellipse(56, 0, 70, 50, volume("#9775fa", 0.35, 0.75), stroke="#5f3dc4", stroke_width=4))
    m.append(ellipse(74, 18, 46, 24, "#e5dbff"))
    m.append(ellipse(112, 6, 4, 3, "#5f3dc4") + ellipse(112, 18, 4, 3, "#5f3dc4"))
    m.append(oeil(46, -18, ys, regard, sclere=True, taille=1.5))
    m.append(oeil(84, -16, ys, regard, sclere=True, taille=1.3))
    m.append(ellipse(30, 14, 10, 6, ROSE, opacity=0.8))
    m.append(place(bouche(0, 0, bs, 0.9), 78, 28))
    # la tête ne s'incline pas plus de 35° : le cou se courbe, le visage reste lisible
    a = (angle + 180) % 360 - 180
    if abs(a) > 90:
        r = (180 - a) if a > 0 else (-180 - a)
        return place(m, x, y, s, flip=True, rot=-max(-35, min(35, r)))
    return place(m, x, y, s, rot=max(-35, min(35, a)))


def serpent(d, ep, tete, angle, s_tete=None, **k):
    """Le Serpent entier : corps sur `d`, tête au point `tete` vers `angle`."""
    m = [corps_serpent(d, ep), tete_serpent(tete[0], tete[1], s_tete or ep / 60, angle, **k)]
    xs = [float(v) for v in d.replace("M", " ").replace("Q", " ").replace("T", " ").replace("C", " ").replace("L", " ").split()]
    zone = occuper(min(xs[0::2]) - ep, min(xs[1::2]) - ep, max(xs[0::2]) + ep, max(xs[1::2]) + ep)
    return g(m) + zone


# --- Animaux ---------------------------------------------------------------------

def grenouille(x, y, s=1.0, plein=True, expr="sourire", flip=False, **k):
    """Grenouille, le ventre gonflé d'eau si `plein`."""
    m = [perso("grenouille", 0, 0, 1.0, expr=expr, **k)]
    if plein:
        m.append(ellipse(0, -64, 50, 46, volume("#74c0fc", 0.4, 0.8), opacity=0.85))
        m.append(chemin("M -26 -76 Q -10 -96 10 -90", stroke="#ffffff", sw=5, opacity=0.7))
    return place(m, x, y, s, flip=flip)


def emeu(x, y, s=1.0, flip=False, expr="sourire", regard=(1, 0), dort=False):
    """Émeu de profil, tête à droite ; (x, y) = pieds."""
    ys, bs, ss = EXPRESSIONS["dort" if dort else expr]
    c, f = "#8d6e5a", "#5c4033"
    m = [chemin("M -20 -150 L -30 -60 L -40 0 M 20 -150 L 24 -60 L 34 0", stroke="#868e96", sw=8),
         chemin("M -52 0 L -28 0 M 22 0 L 46 0", stroke="#868e96", sw=6),
         ellipse(0, -190, 90, 66, volume(c, 0.25, 0.75))]
    r = random.Random(3)
    for _ in range(14):
        px, py = r.uniform(-70, 60), r.uniform(-230, -150)
        m.append(chemin(f"M {n(px)} {n(py)} q 10 14 -2 26", stroke=f, sw=3, opacity=0.6))
    m += [chemin("M 60 -220 Q 80 -300 92 -350", stroke="#5c7cfa", sw=22),
          ellipse(100, -366, 26, 20, "#495057"),
          poly([(120, -372), (150, -364), (120, -356)], "#343a40"),
          oeil(104, -372, ys, regard, taille=0.8)]
    m.append(occuper(-100, -390, 160, 0))
    return place(m, x, y, s, flip=flip)


def koala(x, y, s=1.0, flip=False, expr="sourire", regard=(0, 0)):
    """Koala assis, vu de face ; (x, y) = sous le corps."""
    ys, bs, ss = EXPRESSIONS[expr]
    c = "#adb5bd"
    m = [ellipse(0, -60, 54, 62, volume(c, 0.3, 0.75)), ellipse(0, -50, 32, 40, "#f1f3f5"),
         ellipse(-26, -6, 22, 12, c), ellipse(26, -6, 22, 12, c)]
    for sgn in (-1, 1):
        m += [cercle(sgn * 56, -170, 34, volume(c, 0.3, 0.75)), cercle(sgn * 56, -170, 20, "#f1f3f5")]
    m += [ellipse(0, -150, 58, 50, volume(c, 0.3, 0.75)), ellipse(0, -140, 16, 22, "#343a40"),
          oeil(-26, -160, ys, regard), oeil(26, -160, ys, regard),
          ellipse(-36, -130, 8, 5, ROSE, opacity=0.7), ellipse(36, -130, 8, 5, ROSE, opacity=0.7),
          place(bouche(0, 0, bs, 0.7), 0, -112)]
    m.append(occuper(-90, -210, 90, 0))
    return place(m, x, y, s, flip=flip)


def lezard(x, y, s=1.0, flip=False, expr="sourire", couleur="#94d82d"):
    """Lézard vu de profil, tête à droite ; (x, y) = sous le ventre."""
    ys, bs, ss = EXPRESSIONS[expr]
    f = _assombrir(couleur, 0.75)
    m = [chemin("M -40 -14 Q -120 -10 -190 10", stroke=couleur, sw=16),
         chemin("M -30 -4 L -50 10 M 30 -4 L 50 10", stroke=f, sw=10),
         ellipse(0, -18, 60, 18, volume(couleur, 0.3, 0.75)),
         ellipse(72, -26, 30, 16, volume(couleur, 0.3, 0.75))]
    for k in range(5):
        m.append(cercle(-36 + k * 18, -24, 4, f))
    m += [oeil(78, -32, ys, (1, 0), taille=0.7), place(bouche(0, 0, bs, 0.5), 92, -18)]
    m.append(occuper(-190, -50, 110, 10))
    return place(m, x, y, s, flip=flip)


# --- Décors ----------------------------------------------------------------------

def terre_plate(S, y=520, couleur=TERRE, haut="#ffd8a8", bas="#fff3bf"):
    ciel(S, haut, bas)
    sol(S, y, couleur, bosse=4, couleur2=_assombrir(couleur, 0.92), y2=y + 160)


def riviere_(S, d, ep=60):
    S.add(chemin(d, stroke=_assombrir(TERRE, 0.8), sw=ep + 14))
    S.add(chemin(d, stroke="#4dabf7", sw=ep))
    S.add(chemin(d, stroke="#a5d8ff", sw=ep * 0.25, opacity=0.6))


def pays_vert(S, y=520, eau=True, soir=False):
    """Le pays après la pluie : collines, herbe, eucalyptus, rivière."""
    if soir:
        ciel(S, "#f76707", "#ffd8a8")
    else:
        ciel(S, "#74c0fc", "#fff3bf")
    S.add(chemin(f"M 0 {y - 40} Q 140 {y - 170} 300 {y - 60} Q 460 {y - 200} 620 {y - 70} Q 720 {y - 130} 800 {y - 60} L 800 {y + 10} L 0 {y + 10} Z",
                 "#d9822b", opacity=0.55))
    sol(S, y, "#a9e34b", couleur2="#94d82d", y2=y + 160)
    if eau:
        riviere_(S, f"M -20 {y + 40} Q 200 {y + 70} 360 {y + 120} T 820 {y + 210}", 50)


def trou_eau(S, x, y, rx=230, ry=60):
    S.add(ellipse(x, y, rx + 16, ry + 10, _assombrir(TERRE, 0.75)))
    S.add(ellipse(x, y, rx, ry, S.degrade(["#1971c2", "#4dabf7"])))
    S.add(ellipse(x - rx * 0.3, y - ry * 0.3, rx * 0.4, ry * 0.2, "#d0ebff", opacity=0.4))


# --- Pages -----------------------------------------------------------------------

def couverture():
    S = Scene()
    pays_vert(S, 560)
    S.add(eucalyptus(80, 600, 0.9), eucalyptus(720, 610, 0.8))
    S.add(serpent("M 90 700 Q 120 330 400 300 Q 640 280 650 470", 64, (650, 470), 80, expr="content", regard=(-1, 1)))
    S.add(kangourou(250, 780, 0.8, expr="rire"))
    S.add(grenouille(480, 780, 0.6, expr="rire"), grenouille(560, 790, 0.5, expr="rire", plein=False))
    S.cachette(740, 420, "air")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(serpent("M 60 250 Q 90 160 200 170 Q 300 180 300 110", 40, (300, 110), -70, expr="content", regard=(1, 0)))
    return S


def p01():
    """Plan large : la terre plate et vide, toute silencieuse."""
    S = Scene()
    terre_plate(S, 520)
    S.add(soleil(640, 160, 50, "#ffd43b", rayons=False))
    S.add(caillou(200, 640, 1.0, "#c08a52"), caillou(560, 700, 0.8, "#c08a52"), caillou(700, 600, 0.6, "#c08a52"))
    S.dessus(texte(400, 300, "Chut…", 64, "#d9822b", contour="#fff"))
    return S


def p02():
    """Coupe du sol : sous la terre, les animaux dorment ; le Serpent aussi."""
    S = Scene()
    coupe_terre(S, 260, herbe_c="#e8a35a", terre="#c97a3a", terre2="#8d4f1e")
    S.ambiance("jour")
    for x, y, rx, ry in [(170, 420, 120, 70), (560, 400, 130, 70), (420, 640, 300, 110), (130, 640, 80, 50)]:
        S.add(ellipse(x, y, rx, ry, "#6d3a14", opacity=0.55))
    S.add(kangourou(160, 470, 0.45, expr="dort"))
    S.add(emeu(540, 450, 0.42, dort=True))
    S.add(grenouille(110, 680, 0.45, expr="dort"))
    S.add(serpent("M 180 650 Q 260 560 420 600 Q 600 640 640 690 Q 520 730 360 700", 50, (360, 700), 190, expr="dort"))
    S.add(zzz(300, 360, 1.0, "#fff3bf"), zzz(660, 330, 0.8, "#fff3bf"))
    return S


def p03():
    """Gros plan : le Serpent arc-en-ciel pousse la terre et sort au soleil."""
    S = Scene()
    terre_plate(S, 560)
    S.add(soleil(150, 150, 50, "#ffd43b"))
    S.add(chemin("M 300 600 Q 340 520 420 530 Q 500 520 540 600 Z", _assombrir(TERRE, 0.8)))
    S.add(serpent("M 420 640 Q 420 520 470 430", 90, (470, 430), -60, expr="joie", regard=(1, -1)))
    for dx in (-140, -80, 120, 170):
        S.add(caillou(420 + dx, 610 + abs(dx) * 0.2, 0.6, "#c08a52"))
    S.add(mouvement(300, 520, 1.0, rot=200), mouvement(650, 520, 1.0))
    S.add(eclat(250, 330, 1.2, "#fff3bf"))
    S.camera(1.3, 440, 470)
    return S


def p04():
    """Plongée large : son corps creuse les vallées, pousse les collines."""
    S = Scene()
    ciel(S, "#ffd8a8", "#fff3bf")
    S.add(chemin("M 0 330 Q 120 190 240 300 Q 330 170 450 290 Q 560 150 700 270 Q 760 220 800 260 L 800 360 L 0 360 Z", "#c97a3a"))
    S.add(chemin("M 0 350 Q 160 250 320 330 Q 460 240 620 320 Q 720 280 800 320 L 800 380 L 0 380 Z", "#d9822b"))
    sol(S, 360, TERRE, bosse=6, couleur2=_assombrir(TERRE, 0.9), y2=520)
    # vallée creusée derrière lui
    S.add(chemin("M -20 420 Q 200 380 300 470 Q 400 560 560 520 Q 700 490 820 560", stroke=_assombrir(TERRE, 0.75), sw=110))
    S.add(chemin("M -20 420 Q 200 380 300 470 Q 400 560 560 520", stroke=_assombrir(TERRE, 0.6), sw=40,
                 opacity=0.6))
    S.add(serpent("M 300 470 Q 400 560 560 520 Q 680 490 700 600 Q 710 700 560 720", 70, (560, 720), 170,
                  expr="content", regard=(-1, 0)))
    S.add(caillou(120, 720, 0.8, "#c08a52"))
    S.add(caillou(380, 760, 0.6, "#c08a52"))
    return S


def p05():
    """Plan moyen : « Grenouilles, sortez ! » — elles sortent, le ventre plein."""
    S = Scene()
    terre_plate(S, 500)
    S.add(serpent("M -40 720 Q 160 640 220 520 Q 260 420 200 340", 80, (200, 340), -100, expr="sourire", regard=(1, 0)))
    for x, y, s, fl in [(420, 740, 0.85, False), (560, 700, 0.7, True), (690, 760, 0.9, False), (520, 790, 0.6, False)]:
        S.add(ellipse(x, y + 4, 60 * s, 14 * s, _assombrir(TERRE, 0.75)))
        S.add(grenouille(x, y, s, expr="baille", flip=fl))
    S.cachette(200, 70, "air")
    S.dessus(bulle(470, 150, 440, 100, "Grenouilles, sortez !", 40, pointe=(260, 300)))
    return S


def p06():
    """Gros plan : les chatouilles ; les grenouilles rient, l'eau jaillit."""
    S = Scene()
    terre_plate(S, 500)
    S.add(serpent("M -40 760 Q 140 700 180 600 Q 220 480 250 470", 80, (250, 470), -10, expr="rire", regard=(1, 0)))
    # bout de la queue qui chatouille
    S.add(corps_serpent("M 800 760 Q 600 700 560 620", 40))
    for x, y, s in [(500, 640, 1.1), (680, 600, 0.9)]:
        S.add(grenouille(x, y, s, plein=False, expr="rire", bras="haut"))
        S.add(chemin(f"M {x} {y - 92 * s} Q {x - 210 * s} {y - 140 * s} {x - 270 * s} {y + 20 * s}", stroke="#74c0fc", sw=22 * s,
                     opacity=0.85))
        S.add(chemin(f"M {x} {y - 92 * s} Q {x + 210 * s} {y - 140 * s} {x + 270 * s} {y + 20 * s}", stroke="#74c0fc", sw=20 * s,
                     opacity=0.85))
        for k in range(6):
            S.add(goutte(x + (k - 2.5) * 70 * s, y - 200 * s + (k % 2) * 40, 1.0 * s, "#4dabf7"))
    S.add(chemin("M 380 800 Q 500 720 640 740 Q 760 760 820 720 L 820 820 L 380 820 Z", "#4dabf7", opacity=0.9))
    S.camera(1.15, 470, 520)
    S.dessus(texte(420, 120, "Hi hi hi ! Ha ha ha !", 52, "#1c7ed6", contour="#fff"))
    return S


def p07():
    """Plan large : la terre devient verte."""
    S = Scene()
    pays_vert(S, 500)
    S.add(eucalyptus(160, 560, 1.1), eucalyptus(640, 540, 0.9), eucalyptus(420, 520, 0.6))
    for k, (x, y) in enumerate([(100, 700), (300, 740), (520, 700), (700, 760), (240, 620), (600, 620)]):
        S.add(fleur(x, y, 0.8, ("#ff8787", "#ffd43b", "#cc5de8")[k % 3]))
    S.add(serpent("M 820 740 Q 640 800 560 760", 50, (560, 760), 170, expr="content", regard=(-1, 0)))
    S.add(oiseau(260, 200, 0.6, "#fa5252"), oiseau(520, 160, 0.5, "#fcc419", flip=True))
    return S


def p08():
    """Plan large : les animaux s'éveillent et trouvent leur place."""
    S = Scene()
    pays_vert(S, 500)
    S.add(eucalyptus(640, 560, 1.4))
    S.add(koala(700, 290, 0.45, expr="content"))
    S.add(kangourou(140, 790, 0.95, expr="rire"))
    S.add(emeu(380, 780, 0.85, expr="content"))
    S.add(lezard(600, 760, 0.8))
    S.add(grenouille(320, 790, 0.45, plein=False, expr="rire"))
    S.add(oiseau(280, 180, 0.6, "#fa5252"), oiseau(470, 140, 0.5, "#4dabf7", flip=True))
    return S


def p09():
    """Plan moyen : « Prenez soin de cette terre, et partagez l'eau. »"""
    S = Scene()
    pays_vert(S, 520, eau=False)
    trou_eau(S, 400, 640, 260, 60)
    S.add(serpent("M 820 640 Q 680 620 640 520 Q 600 420 560 380", 80, (560, 380), -120, expr="sourire", regard=(-1, 1)))
    S.add(kangourou(140, 790, 0.8, expr="content"))
    S.add(emeu(320, 790, 0.7, expr="content"))
    S.add(koala(460, 790, 0.6, expr="content", regard=(1, -1)))
    S.add(lezard(600, 790, 0.6))
    S.add(grenouille(240, 700, 0.4, plein=False))
    S.dessus(bulle(330, 140, 560, 110, "Cette terre est à vous tous.\nPrenez-en soin, et partagez l'eau.", 30, pointe=(520, 340)))
    return S


def p10():
    """Plan moyen, au soir : le Serpent se repose au fond du trou d'eau."""
    S = Scene()
    pays_vert(S, 480, eau=False, soir=True)
    S.add(soleil(640, 380, 46, "#ffa94d", rayons=False))
    S.add(eucalyptus(110, 520, 1.0), eucalyptus(720, 510, 0.8))
    trou_eau(S, 400, 650, 330, 110)
    # le Serpent enroulé, vu sous l'eau
    S.add(g([corps_serpent("M 250 650 Q 320 590 420 610 Q 540 640 520 690 Q 480 720 380 700 Q 300 680 330 650", 44)], opacity=0.55))
    S.add(tete_serpent(330, 650, 0.6, 20, expr="dort"))
    S.add(ellipse(400, 650, 330, 110, "#4dabf7", opacity=0.25))
    S.add(zzz(470, 520, 0.9, "#fff3bf"))
    S.cachette(720, 760)
    return S


def p11():
    """Plan large : l'arc-en-ciel après la pluie, d'un trou d'eau à l'autre."""
    S = Scene()
    pays_vert(S, 520, eau=False)
    S.add(nuage(160, 110, 1.0, "#ced4da"), nuage(620, 90, 0.9, "#dee2e6"))
    S.add(g(arc_en_ciel(400, 610, 360, 22), opacity=0.85))
    trou_eau(S, 80, 620, 110, 30)
    trou_eau(S, 720, 620, 110, 30)
    S.add(eucalyptus(400, 560, 0.7))
    S.add(kangourou(220, 790, 0.85, expr="rire", regard=(1, -1)))
    S.add(emeu(560, 790, 0.75, expr="content", regard=(1, -1)))
    S.add(grenouille(400, 790, 0.5, plein=False, expr="rire", bras="haut"))
    for x in range(40, 800, 70):
        S.add(goutte(x, 760 + (x % 3) * 10, 0.5, "#a5d8ff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("serpent-seul.svg", vignette),
    ("01-la-terre-vide.svg", p01), ("02-sous-la-terre.svg", p02), ("03-le-reveil.svg", p03),
    ("04-les-vallees.svg", p04), ("05-les-grenouilles.svg", p05), ("06-les-chatouilles.svg", p06),
    ("07-la-terre-verte.svg", p07), ("08-les-animaux.svg", p08), ("09-la-promesse.svg", p09),
    ("10-le-trou-d-eau.svg", p10), ("11-l-arc-en-ciel.svg", p11),
]
