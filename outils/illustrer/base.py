"""
Petite boîte à outils pour dessiner les illustrations des livres en SVG.

Tout est en coordonnées d'une page carrée de 800 × 800. Les fonctions
renvoient des chaînes SVG que l'on ajoute à une `Scene`, puis
`Scene.enregistrer(chemin)` écrit le fichier.

    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 640, "#8ce99a")
    S.add(arbre(150, 650))
    S.add(perso("ours", 400, 700, 1.4, expr="rire", bras="haut"))
    S.enregistrer("livres/mon-livre/images/01.svg")
"""
import hashlib
import math
import os
import random
import re

ENCRE = "#2b2b3a"
ROSE = "#ff8fab"
ROUGE_BOUCHE = "#c92a2a"
BLANC = "#ffffff"

_compteur = [0]


def uid(prefixe="i"):
    _compteur[0] += 1
    return f"{prefixe}{_compteur[0]}"


def n(v, precision=1):
    """Nombre compact : 12.0 → 12, 3.14159 → 3.1."""
    if isinstance(v, str):
        return v
    s = f"{v:.{precision}f}".rstrip("0").rstrip(".") if precision else f"{v:.0f}"
    if s == "-0":
        s = "0"
    return s


def _attrs(a):
    out = []
    for k, v in a.items():
        if v is None or v is False:
            continue
        k = k.rstrip("_").replace("_", "-")
        # Garder les rapports précis : une opacité de 0,04 reste visible.
        precision = 3 if k in ("opacity", "fill-opacity", "stroke-opacity", "stop-opacity", "offset") else 1
        out.append(f'{k}="{n(v, precision)}"')
    return (" " + " ".join(out)) if out else ""


def el(tag, contenu=None, **a):
    if contenu is None:
        return f"<{tag}{_attrs(a)}/>"
    return f"<{tag}{_attrs(a)}>{contenu}</{tag}>"


def rect(x, y, w, h, fill, rx=None, **a):
    return el("rect", x=x, y=y, width=w, height=h, rx=rx, fill=fill, **a)


def cercle(x, y, r, fill, **a):
    return el("circle", cx=x, cy=y, r=r, fill=fill, **a)


def ellipse(x, y, rx, ry, fill, rot=None, **a):
    t = f"rotate({n(rot)} {n(x)} {n(y)})" if rot else None
    return el("ellipse", cx=x, cy=y, rx=rx, ry=ry, fill=fill, transform=t, **a)


def chemin(d, fill="none", stroke=None, sw=None, **a):
    extra = {}
    if stroke:
        extra = dict(stroke=stroke, stroke_width=sw or 4, stroke_linecap="round", stroke_linejoin="round")
    return el("path", d=d, fill=fill, **extra, **a)


def trait(x1, y1, x2, y2, stroke=ENCRE, sw=4, **a):
    return el("line", x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke, stroke_width=sw, stroke_linecap="round", **a)


def poly(points, fill, **a):
    return el("polygon", points=" ".join(f"{n(x)},{n(y)}" for x, y in points), fill=fill, **a)


def g(contenu, transform=None, **a):
    if isinstance(contenu, (list, tuple)):
        contenu = "".join(contenu)
    return el("g", contenu, transform=transform, **a)


def place(contenu, x=0, y=0, s=1.0, flip=False, rot=0, sy=None):
    """Place un dessin fait autour de (0, 0) au point (x, y)."""
    t = []
    if x or y:
        t.append(f"translate({n(x)} {n(y)})")
    if rot:
        t.append(f"rotate({n(rot)})")
    sx = -s if flip else s
    sy = s if sy is None else sy
    if sx != 1 or sy != 1:
        t.append(f"scale({n(sx, 3)} {n(sy, 3)})")
    return g(contenu, " ".join(t) or None)


def texte(x, y, contenu, taille=48, fill=ENCRE, anchor="middle", poids=700, contour=None, rot=None, police="Fredoka, Andika, sans-serif"):
    a = dict(x=x, y=y, font_family=police, font_weight=poids, font_size=taille, text_anchor=anchor, fill=fill)
    if contour:
        a.update(stroke=contour, stroke_width=taille / 7, stroke_linejoin="round", paint_order="stroke")
    if rot:
        a["transform"] = f"rotate({n(rot)} {n(x)} {n(y)})"
    return el("text", contenu, **a)


# --- Dégradés partagés -------------------------------------------------------
# Les dessins renvoient des chaînes SVG sans accès à la Scene : un dégradé
# reçoit donc un identifiant tiré de sa définition (même dégradé → même
# identifiant, quel que soit l'ordre de génération) et Scene.svg() ajoute aux
# <defs> ceux que la page emploie.
_DEGRADES = {}


def _arrets(couleurs):
    """Liste de couleurs, ou de (position, couleur[, opacité]) → arrêts complets."""
    out = []
    for k, c in enumerate(couleurs):
        if isinstance(c, str):
            out.append((k / max(len(couleurs) - 1, 1), c, 1))
        else:
            out.append((c[0], c[1], c[2] if len(c) > 2 else 1))
    return out


def _degrade(balise, couleurs, **a):
    arrets = "".join(el("stop", offset=o, stop_color=c, stop_opacity=None if op == 1 else op)
                     for o, c, op in _arrets(couleurs))
    corps = el(balise, arrets, **a)
    i = "vol" + hashlib.md5(corps.encode()).hexdigest()[:7]
    _DEGRADES[i] = corps.replace(f"<{balise}", f'<{balise} id="{i}"', 1)
    return f"url(#{i})"


def lineaire(couleurs, x1=0, y1=0, x2=0, y2=1, espace=None):
    """Dégradé linéaire (vertical par défaut) ; espace="userSpaceOnUse" pour des
    coordonnées locales au dessin plutôt que relatives à la forme."""
    return _degrade("linearGradient", couleurs, x1=x1, y1=y1, x2=x2, y2=y2, gradientUnits=espace)


def radial(couleurs, cx=0.5, cy=0.5, r=0.5, fx=None, fy=None, espace=None):
    return _degrade("radialGradient", couleurs, cx=cx, cy=cy, r=r, fx=fx, fy=fy, gradientUnits=espace)


def volume(c, clair=0.3, sombre=0.78):
    """Remplissage « en relief » : reflet en haut à gauche, bord ombré."""
    if _rvb(c) is None:
        return c
    return radial([(0, eclaircir(c, clair)), (0.55, c), (1, _assombrir(c, sombre))], cx=0.42, cy=0.38, r=0.62, fx=0.32, fy=0.26)


def cylindre(c, clair=0.22, sombre=0.76, vertical=False):
    """Remplissage d'une forme ronde vue de face (tronc, jambe, robe) : clair à
    gauche, sombre à droite."""
    if _rvb(c) is None:
        return c
    arrets = [(0, eclaircir(c, clair)), (0.38, c), (1, _assombrir(c, sombre))]
    return lineaire(arrets, 0, 0, 0, 1) if vertical else lineaire(arrets, 0, 0, 1, 0)


def melange(c1, c2, k=0.5):
    a, b = _rvb(c1), _rvb(c2)
    if a is None or b is None:
        return c1
    return "#%02x%02x%02x" % tuple(int(x + (y - x) * k) for x, y in zip(a, b))


def luminance(c):
    rvb = _rvb(c)
    return 0.5 if rvb is None else (0.299 * rvb[0] + 0.587 * rvb[1] + 0.114 * rvb[2]) / 255


# --- Modelé automatique -------------------------------------------------------
# Les dessins propres à chaque livre sont faits d'aplats ; à l'écriture de la
# page, chaque forme pleine reçoit un léger dégradé (lumière en haut à gauche).
# Restent plates : formes semi-transparentes, contenus de masques, de découpes
# et de textes, groupes marqués data-relief="non" (éclairage physique des
# livres de sciences) et formes de la couleur du fond (fausses découpes).
RELIEF_AUTO = [True]
_BALISE = re.compile(r"<(/?)([a-zA-Z]+)([^>]*?)(/?)>")
_SANS_RELIEF = {"clipPath", "mask", "defs", "linearGradient", "radialGradient", "filter", "text", "pattern"}
_FORMES = {"rect", "circle", "ellipse", "polygon", "path"}


def sans_relief(contenu):
    """Garde un dessin en aplats (éclairage voulu, découpe de la couleur du fond)."""
    return el("g", "".join(contenu) if isinstance(contenu, (list, tuple)) else contenu, data_relief="non")


def _valeur(attrs, nom):
    m = re.search(rf'\s{nom}="([^"]*)"', attrs)
    return m.group(1) if m else None


def _relief_auto(texte_svg, w, h, fonds):
    out, pos, pile, saut = [], 0, [], 0
    for m in _BALISE.finditer(texte_svg):
        ferme, tag, attrs, auto = m.groups()
        if ferme:
            if pile:
                saut -= pile.pop()
            continue
        bloque = tag in _SANS_RELIEF or 'data-relief="non"' in attrs
        if not auto:
            pile.append(1 if bloque else 0)
            saut += 1 if bloque else 0
        if saut or bloque or tag not in _FORMES:
            continue
        fill = _valeur(attrs, "fill")
        if not fill or not fill.startswith("#") or _rvb(fill) is None or fill.lower() in fonds:
            continue
        if " opacity=" in attrs or "fill-opacity=" in attrs or luminance(fill) < 0.1:
            continue
        large = tag == "rect" and float(_valeur(attrs, "width") or 0) >= 0.9 * w
        if large and float(_valeur(attrs, "height") or 0) >= 0.9 * h:
            continue
        if large:
            remp = lineaire([(0, eclaircir(fill, 0.1)), (1, _assombrir(fill, 0.88))])
        else:
            remp = lineaire([(0, eclaircir(fill, 0.16)), (0.5, fill), (1, _assombrir(fill, 0.84))], 0, 0, 1, 1)
        debut = m.start(3) + attrs.index(f'fill="{fill}"')
        out.append(texte_svg[pos:debut] + f'fill="{remp}"')
        pos = debut + len(f'fill="{fill}"')
    out.append(texte_svg[pos:])
    return "".join(out)


def _couleurs_fond(scene):
    """Couleurs du fond de la page : arrêts des dégradés du ciel, grands aplats."""
    fonds = set()
    for d in scene.defs:
        fonds.update(c.lower() for c in re.findall(r'stop-color="(#[0-9a-fA-F]{3,6})"', d))
    for e in scene.els:
        if e.startswith("<rect") and float(_valeur(e, "width") or 0) >= 0.9 * scene.w:
            f = _valeur(e, "fill")
            if f and f.startswith("#"):
                fonds.add(f.lower())
    return fonds


# --- Finition de la page -------------------------------------------------------
# À l'écriture, chaque page reçoit par-dessus le dessin (hors cadrage) :
#   - un glacis éventuel : aplat très pâle en mode « produit » (multiply), une
#     patine de vieux papier pour les fables et les contes ; il désature les
#     couleurs complémentaires (un glacis chaud grise le bleu du ciel) : le
#     garder presque blanc ;
#   - la lumière de son moment (AMBIANCES) : teinte en mode « produit » (nuit
#     bleutée, soir doré) sous les halos des sources de lumière, halo coloré
#     en « lumière douce » et vignettage qui ramène le regard vers le centre ;
#     le jour n'a qu'un vignettage très léger.
# Le grain du papier n'est pas dans les SVG : css/pages.css le pose sur
# chaque page à l'échelle de l'écran (un bruit dessiné dans le SVG devient
# du « bruit de télévision » sur les petites couvertures).
# generer.py règle ces valeurs livre par livre (rayon et variables GLACIS,
# LUMIERE et CACHE du script).
GLACIS_PAGE = [None]        # couleur pâle du glacis, None = aucun
LUMIERE_PAGE = [True]       # halo et teinte d'ambiance ; False pour les livres de sciences
BETE_CACHEE = [None]        # petite bête cachée sur chaque page (CACHETTES), None = aucune
MOTIF_PAPIER = ["rayures"]  # papier peint des intérieurs (interieur(papier=…))

# Lumière de chaque moment : halo (couleur, force, centre x, centre y, rayon)
# fondu en « lumière douce » (soft-light), vignette (couleur, force).
AMBIANCES = {
    "jour": dict(halo=None, vignette=("#1c2a52", 0.08)),
    "soir": dict(halo=("#ffb35c", 0.7, 0.2, 0.25, 1.0), vignette=("#5f3dc4", 0.22), teinte="#fff0dc"),
    "nuit": dict(halo=("#91a7ff", 0.35, 0.75, 0.1, 0.8), vignette=("#060b24", 0.42), teinte="#cdd5f4"),
    "interieur": dict(halo=("#ffe2a8", 0.6, 0.3, 0.15, 0.9), vignette=("#3b2414", 0.24)),
    "eau": dict(halo=("#c5f6fa", 0.6, 0.5, -0.1, 0.9), vignette=("#04263d", 0.34)),
    "neutre": dict(halo=None, vignette=("#1c2a52", 0.05)),
    # fond uni sombre (salle noire d'une expérience, espace) : pas de teinte,
    # les couleurs d'un schéma restent justes
    "sombre": dict(halo=None, vignette=("#000000", 0.25)),
}


def _teinte(scene):
    """Teinte du moment (nuit bleutée, soir doré) et glacis du livre, en mode
    « produit » : posés avant les lumières de la scène, qui restent vives."""
    m = []
    amb = AMBIANCES.get(scene.moment or "neutre", AMBIANCES["neutre"])
    if amb.get("teinte") and LUMIERE_PAGE[0]:
        m.append(rect(0, 0, scene.w, scene.h, amb["teinte"], style="mix-blend-mode:multiply"))
    if GLACIS_PAGE[0]:
        m.append(rect(0, 0, scene.w, scene.h, GLACIS_PAGE[0], style="mix-blend-mode:multiply"))
    return m


def _finition(scene):
    """Halo et vignette du moment, posés sur la page : (définitions, éléments)."""
    w, h = scene.w, scene.h
    defs, m = [], []
    amb = AMBIANCES.get(scene.moment or "neutre", AMBIANCES["neutre"])
    if amb.get("halo") and LUMIERE_PAGE[0]:
        c, force, cx, cy, r = amb["halo"]
        m.append(rect(0, 0, w, h, radial([(0, c, force), (0.55, c, force * 0.45), (1, c, 0)], cx=cx, cy=cy, r=r),
                      style="mix-blend-mode:soft-light"))
    if amb.get("vignette"):
        c, force = amb["vignette"]
        m.append(rect(0, 0, w, h, radial([(0.5, c, 0), (0.8, c, force * 0.45), (1, c, force)], cx=0.5, cy=0.46, r=0.74)))
    return defs, m


# --- Petite bête cachée ----------------------------------------------------------
# Les enfants aiment chercher un petit personnage qui revient à chaque page.
# Les décors qui reçoivent la Scene (sol, interieur, ocean…) proposent des
# cachettes ; à l'écriture, une cachette visible est choisie d'après le nom
# du fichier (toujours la même pour une page donnée). Une page peut imposer
# la sienne avec S.cachette(x, y) ou n'en vouloir aucune avec S.cachette(None).

def coccinelle_cachee(x, y, s=1.0, flip=False):
    """Coccinelle de profil, (x, y) = sous ses pattes ; environ 30 de large."""
    m = [ellipse(1, 1, 15, 3, "#000", opacity=0.18)]
    for dx in (-7, 0, 7):
        m.append(trait(dx, -4, dx + 2, 1, ENCRE, 1.8))
    m.append(cercle(11, -9, 6.5, ENCRE))
    m.append(cercle(13.2, -10.6, 1.6, "#fff"))
    m.append(chemin("M 9 -14 Q 12 -21 16 -21 M 12 -14 Q 17 -19 20 -17", stroke=ENCRE, sw=1.4))
    m.append(chemin("M -13 -2 A 13 12 0 0 1 13 -2 Z", radial([(0, "#ff8787"), (0.6, "#f03e3e"), (1, "#a61e1e")], cx=0.4, cy=0.3, r=0.75)))
    m.append(trait(0, -14, 1, -2, ENCRE, 1.4))
    for px, py, pr in ((-6, -7, 2.6), (6, -9, 2.4), (-2, -11.5, 1.8), (8, -4, 1.8), (-9, -3.5, 1.6)):
        m.append(cercle(px, py, pr, ENCRE))
    m.append(ellipse(-5, -10, 3.5, 1.6, "#fff", rot=-25, opacity=0.55))
    return place(sans_relief(m), x, y, s, flip=flip)


def etoile_mer_cachee(x, y, s=1.0, flip=False):
    """Petite étoile de mer posée sur le sable, avec deux yeux."""
    m = [ellipse(0, 1, 16, 3.5, "#000", opacity=0.18),
         place(etoile5(0, 0, 15, "#ff922b", rot=8), 0, -9, sy=0.85),
         cercle(-3.5, -11, 2, ENCRE), cercle(3.5, -11, 2, ENCRE),
         cercle(-3, -11.6, 0.7, "#fff"), cercle(4, -11.6, 0.7, "#fff")]
    for px, py in ((-8, -4), (8, -5), (0, -18), (-1, -2), (5, -14)):
        m.append(cercle(px, py, 1.2, "#ffe8cc"))
    return place(sans_relief(m), x, y, s, flip=flip)


def souris_cachee(x, y, s=1.0, flip=False):
    """Petite souris grise vue de profil, (x, y) = sous ses pattes."""
    m = [ellipse(1, 1, 15, 3, "#000", opacity=0.18),
         chemin("M -12 -5 Q -24 -4 -26 -14", stroke="#ffa8a8", sw=1.8),
         ellipse(-1, -7, 12, 8, volume("#ced4da", 0.3, 0.8)),
         cercle(9, -11, 6.5, volume("#ced4da", 0.3, 0.8)),
         cercle(6, -18, 4.5, "#ced4da"), cercle(6, -18, 2.6, "#ffc9c9"),
         cercle(11.5, -12, 1.6, ENCRE), cercle(15.5, -10, 1.6, "#ff8787"),
         trait(-6, -1, -6, 1, "#ffa8a8", 1.6), trait(4, -1, 4, 1, "#ffa8a8", 1.6)]
    return place(sans_relief(m), x, y, s, flip=flip)


CACHETTES = {"coccinelle": coccinelle_cachee, "souris": souris_cachee, "etoile_mer": etoile_mer_cachee}

# Scène en cours de dessin : les sources de lumière courantes (lune, maison
# éclairée, lampe, luciole…) y inscrivent leur halo, dessiné au-dessus de la
# teinte de la nuit ou du soir seulement. Elles sont presque toujours placées
# en coordonnées de la page ; un halo mal placé (source dessinée dans un repère
# local) se corrige avec halo=False sur la source et S.lumiere().
_SCENE = [None]


def lumiere_auto(x, y, r, couleur="#ffd43b", force=0.6):
    if _SCENE[0] is not None:
        _SCENE[0].lumieres_auto.append(lueur(x, y, r, couleur, force))


def occuper(x0, y0, x1, y1):
    """Zone de la page prise par un personnage : la petite bête n'y va pas
    (elle ne doit pas se poser sur un visage)."""
    if _SCENE[0] is not None:
        _SCENE[0].occupe.append((min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))


class Scene:
    def __init__(self, w=800, h=800):
        self.w, self.h = w, h
        self.defs = []
        self.els = []
        self.moment = None          # clé de AMBIANCES : jour, soir, nuit, interieur, eau, neutre, sombre
        self._moment_impose = False
        self.cadre = None           # (zoom, cx, cy) : voir camera()
        self.cachettes = []         # (x, y, nature) proposés par les décors
        self._cachette = None       # cachette imposée, ou False pour aucune
        self.lumieres = []          # halos posés par-dessus la teinte du moment
        self.lumieres_auto = []     # halos des sources courantes (nuit et soir)
        self.hors_cadre = []        # bulles et textes posés sur la page, sans zoom
        self.occupe = []            # zones des personnages (x0, y0, x1, y1)
        _SCENE[0] = self

    def ambiance(self, moment):
        """Impose la lumière de la page (clé de AMBIANCES)."""
        self.moment, self._moment_impose = moment, True
        return self

    def _decor(self, moment):
        """Moment suggéré par un décor ; le dernier décor posé l'emporte."""
        if not self._moment_impose:
            self.moment = moment

    def camera(self, zoom, cx=None, cy=None):
        """Cadre la page : gros plan (zoom > 1) centré sur (cx, cy), en
        coordonnées de la scène. Le cadre reste dans la scène : aucun bord vide."""
        cx = self.w / 2 if cx is None else cx
        cy = self.h / 2 if cy is None else cy
        dw, dh = self.w / (2 * zoom), self.h / (2 * zoom)
        self.cadre = (zoom, min(max(cx, dw), self.w - dw), min(max(cy, dh), self.h - dh))
        return self

    def vers_page(self, x, y):
        """Point de la scène → point de la page, une fois le cadrage appliqué
        (pour viser un personnage avec la pointe d'une bulle)."""
        if not self.cadre:
            return x, y
        z, cx, cy = self.cadre
        return self.w / 2 + (x - cx) * z, self.h / 2 + (y - cy) * z

    def dessus(self, *morceaux):
        """Ajoute des éléments en coordonnées de la page, au-dessus du dessin et
        hors cadrage : bulles, onomatopées, titres restent à leur taille."""
        for m in morceaux:
            if isinstance(m, (list, tuple)):
                self.dessus(*m)
            elif m:
                self.hors_cadre.append(m)
        return self

    def visible(self, x, y, marge=30):
        """Le point (x, y) de la scène est-il dans le cadre (à `marge` près) ?"""
        if not self.cadre:
            return marge <= x <= self.w - marge and marge <= y <= self.h - marge
        z, cx, cy = self.cadre
        X, Y = self.w / 2 + (x - cx) * z, self.h / 2 + (y - cy) * z
        return marge <= X <= self.w - marge and marge <= Y <= self.h - marge

    def lumiere(self, x, y, r=120, couleur="#ffd43b", force=0.7, ry=None):
        """Halo d'une source de lumière (fenêtre éclairée, lampe, feu, lune),
        posé après la teinte de la nuit ou du soir : la lumière reste chaude et
        vive dans une scène assombrie. Coordonnées de la scène."""
        self.lumieres.append(lueur(x, y, r, couleur, force, ry))
        return self

    def cachette(self, x, y=None, nature=None, s=1.0, flip=None):
        """Impose la cachette de la page ; S.cachette(None) : aucune."""
        self._cachette = False if x is None else (x, y, nature, s, flip)
        return self

    def proposer_cachette(self, x, y, nature="sol"):
        self.cachettes.append((x, y, nature))

    def _bete(self, nom_fichier):
        if not BETE_CACHEE[0] or self._cachette is False or self.w < 600:
            return ""
        graine = int(hashlib.md5(os.path.basename(nom_fichier).encode()).hexdigest()[:8], 16)
        if self._cachette:
            x, y, nature, s, flip = self._cachette
        else:
            def libre(c):
                x, y = c[0], c[1]
                return not any(x0 - 24 < x < x1 + 24 and y0 - 30 < y < y1 + 10 for x0, y0, x1, y1 in self.occupe)
            places = [c for c in self.cachettes if self.visible(c[0], c[1] - 20, 40) and libre(c)]
            if not places:
                return ""
            # au plus près d'un bord (gauche ou droite selon la page) : les
            # personnages s'y tiennent rarement, et les petits savent où chercher
            cote = 1 if graine % 2 else -1
            x, y, nature = min(places, key=lambda c: (round(min(c[0], self.w - c[0])), cote * c[0], c[1]))
            s, flip = None, None
        if flip is None:
            flip = x > self.w / 2
        if s is None:
            s = 1.0 / (self.cadre[0] if self.cadre else 1.0) ** 0.5
        bete = CACHETTES["etoile_mer" if nature == "eau" else BETE_CACHEE[0]]
        return bete(x, y, s, flip=flip)

    def add(self, *morceaux):
        for m in morceaux:
            if isinstance(m, (list, tuple)):
                self.add(*m)
            elif m:
                self.els.append(m)
        return self

    def degrade(self, couleurs, vertical=True, radial=False, **a):
        i = uid("d")
        stops = "".join(
            el("stop", offset=n(k / (len(couleurs) - 1), 3), stop_color=c) for k, c in enumerate(couleurs)
        )
        if radial:
            self.defs.append(el("radialGradient", stops, id=i, **a))
        elif vertical:
            self.defs.append(el("linearGradient", stops, id=i, x1=0, y1=0, x2=0, y2=1))
        else:
            self.defs.append(el("linearGradient", stops, id=i, x1=0, y1=0, x2=1, y2=0))
        return f"url(#{i})"

    def _a_un_fond(self):
        """Un décor plein (ciel, intérieur, océan…) ou un premier aplat qui
        couvre la page."""
        if self.moment is not None:
            return True
        if not self.els or not self.els[0].startswith("<rect"):
            return False
        return (float(_valeur(self.els[0], "width") or 0) >= 0.9 * self.w
                and float(_valeur(self.els[0], "height") or 0) >= 0.9 * self.h)

    def svg(self, nom_fichier=""):
        corps = "\n".join(self.els)
        if RELIEF_AUTO[0]:
            corps = _relief_auto(corps, self.w, self.h, _couleurs_fond(self))
        bete = self._bete(nom_fichier) if nom_fichier else ""
        if bete:
            corps += "\n" + bete
        auto = self.lumieres_auto if self.moment in ("nuit", "soir") else []
        lumieres = "\n".join(auto + self.lumieres)
        if self.cadre:
            z, cx, cy = self.cadre
            cadrage = f"translate({n(self.w / 2 - cx * z, 2)} {n(self.h / 2 - cy * z, 2)}) scale({n(z, 3)})"
            corps = g(corps, cadrage)
            lumieres = g(lumieres, cadrage) if lumieres else ""
        # les calques de finition ne vont que sur une scène qui a un fond : sur
        # une vignette transparente, ils dessineraient un rectangle visible
        fini = self._a_un_fond()
        teinte = _teinte(self) if fini else []
        if teinte:
            corps += "\n" + g(teinte, data_finition="teinte")
        if lumieres:
            corps += "\n" + lumieres
        if self.hors_cadre:
            corps += "\n" + "\n".join(self.hors_cadre)
        defs_fin, finition = _finition(self) if fini else ([], [])
        if finition:
            corps += "\n" + g(finition, data_finition="oui")
        propres = "".join(self.defs) + "".join(defs_fin)
        partages = sorted(set(re.findall(r"url\(#(vol[0-9a-f]{7})\)", propres + corps)))
        tous = propres + "".join(_DEGRADES[i] for i in partages)
        defs = f"<defs>{tous}</defs>" if tous else ""
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}">\n{defs}\n{corps}\n</svg>\n'
        )

    def enregistrer(self, chemin_fichier):
        os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)
        with open(chemin_fichier, "w", encoding="utf-8") as fh:
            fh.write(self.svg(chemin_fichier))


# ---------------------------------------------------------------------------
# Décors
# ---------------------------------------------------------------------------

def _moment_ciel(haut, bas):
    """Moment de la journée d'après les couleurs du ciel."""
    if luminance(haut) < 0.3:
        return "nuit"
    # couchant : une teinte chaude (orange, rose, rouge) franche, pas un
    # simple voile crème ou rosé à l'horizon (très clair, donc exclu)
    chaud = [t for t in (_tsl(haut), _tsl(bas)) if t and t[1] > 0.5 and t[2] < 0.82 and (t[0] < 0.12 or t[0] > 0.88)]
    return "soir" if chaud else "jour"


def ciel(S, haut="#74c0fc", bas="#e7f5ff"):
    S._decor(_moment_ciel(haut, bas))
    S.add(rect(0, 0, S.w, S.h, S.degrade([haut, melange(haut, bas, 0.6), bas])))
    # brume claire vers l'horizon : les lointains se fondent dans le ciel
    S.add(rect(0, 0, S.w, S.h, lineaire([(0.35, eclaircir(bas, 0.4), 0), (0.75, eclaircir(bas, 0.4), 0.35), (1, eclaircir(bas, 0.4), 0.1)])))


def fond(S, couleur):
    S._decor("sombre" if luminance(couleur) < 0.25 else "neutre")
    S.add(rect(0, 0, S.w, S.h, couleur))


def sol(S, y, couleur="#8ce99a", bosse=18, couleur2=None, y2=None, premier=True):
    """Sol de la scène ; `premier=False` retire les touffes, cailloux ou congères
    du premier plan."""
    w = S.w
    S.add(chemin(f"M 0 {y} Q {w * 0.3} {y - bosse} {w / 2} {y} T {w} {y} L {w} {S.h} L 0 {S.h} Z", terrain(couleur)))
    relief_sol(S, f"M 0 {y} Q {w * 0.3} {y - bosse} {w / 2} {y} T {w} {y}", couleur, y + bosse + 12, S.h - 6, graine=int(y))
    devant, haut = couleur, y
    if couleur2:
        y2 = y2 or y + 70
        S.add(chemin(f"M 0 {y2} Q {w * 0.4} {y2 - bosse} {w * 0.7} {y2} T {w + 200} {y2} L {w} {S.h} L 0 {S.h} Z", terrain(couleur2)))
        relief_sol(S, f"M 0 {y2} Q {w * 0.4} {y2 - bosse} {w * 0.7} {y2} T {w + 200} {y2}", couleur2, y2 + bosse + 12, S.h - 6, graine=int(y2) + 1)
        devant, haut = couleur2, y2
    _cachettes_sol(S, haut, bosse)
    if premier:
        premier_plan_sol(S, devant, haut + bosse, graine=int(haut) + 3)


def _cachettes_sol(S, y, bosse=0, plinthe=False, nature="sol"):
    """Cachettes de la petite bête : au pied des côtés du sol (ou du mur)."""
    e = S.w / 800
    dy = 14 * e if plinthe else min(34 * e, (S.h - y) * 0.45)
    if S.h - y - dy < 24 * e:
        return
    for x in (64, 736, 150, 650, 250, 550, 340, 460):
        S.proposer_cachette(x * e, y + dy + (0 if plinthe else bosse * 0.15), nature)


# --- Teintes -------------------------------------------------------------------

def _tsl(c):
    """Couleur → (teinte 0-1, saturation, luminosité), ou None."""
    rvb = _rvb(c)
    if rvb is None:
        return None
    r, v, b = (x / 255 for x in rvb)
    hi, lo = max(r, v, b), min(r, v, b)
    l_ = (hi + lo) / 2
    if hi == lo:
        return 0.0, 0.0, l_
    d = hi - lo
    s_ = d / (2 - hi - lo) if l_ > 0.5 else d / (hi + lo)
    if hi == r:
        t = ((v - b) / d) % 6
    elif hi == v:
        t = (b - r) / d + 2
    else:
        t = (r - v) / d + 4
    return t / 6, s_, l_


def nature_sol(c):
    """« herbe », « sable » (sable, terre, blé), « neige » ou None (route, pierre…)."""
    tsl = _tsl(c)
    if tsl is None:
        return None
    t, s_, l_ = tsl
    if l_ > 0.9 and s_ < 0.6:
        return "neige"
    if s_ < 0.18:
        return None
    if 0.17 <= t <= 0.47:
        return "herbe"
    if 0.03 <= t < 0.17:
        return "sable"
    return None


# --- Premier plan ----------------------------------------------------------------

def touffe(x, y, s=1.0, couleur="#40c057", graine=1):
    """Touffe d'herbe en relief : brins du fond plus sombres, brins de devant
    éclairés à la pointe. (x, y) = pied de la touffe."""
    r = random.Random(graine)
    if _rvb(couleur) is None:
        return place(herbe(0, 0, 1, couleur), x, y, s)
    m = []
    for rang, (nb, teinte) in enumerate(((4, _assombrir(couleur, 0.72)), (5, couleur))):
        remp = lineaire([(0, eclaircir(teinte, 0.35 if rang else 0.12)), (1, _assombrir(teinte, 0.7))])
        d = []
        for k in range(nb):
            a = -60 + 120 * (k + r.uniform(0.2, 0.8)) / nb
            L = r.uniform(26, 44) * (0.85 if rang == 0 else 1)
            bx = a * 0.18
            px, py = bx + a * 0.32 + r.uniform(-4, 4), -L
            d.append(f"M {n(bx - 4)} 0 Q {n(bx - 3 + a * 0.12)} {n(-L * 0.55)} {n(px)} {n(py)} Q {n(bx + 2 + a * 0.1)} {n(-L * 0.5)} {n(bx + 4)} 0 Z")
        m.append(chemin(" ".join(d), remp))
    return place(m, x, y, s)


def premier_plan_sol(S, couleur, y_haut, graine=1):
    """Détails du premier plan, plus grands et plus contrastés près du bas de
    l'image : touffes d'herbe, cailloux sur le sable ou ombres de congères."""
    nature = nature_sol(couleur)
    if not nature or S.h - y_haut < 70:
        return
    r = random.Random(graine)
    e = S.w / 800
    y0 = max(y_haut + 30 * e, S.h - 110 * e)
    nb = max(3, int(6 * e + 0.5))
    m = []
    for k in range(nb):
        x = (k + r.uniform(0.15, 0.85)) * S.w / nb
        yy = r.uniform(y0, S.h - 4 * e)
        prof = (yy - y0) / max(S.h - y0, 1)
        if nature == "herbe":
            m.append(touffe(x, yy + 3 * e, e * (0.7 + 0.6 * prof), _assombrir(couleur, 0.8), graine=graine + k))
        elif nature == "sable":
            rx = e * r.uniform(9, 16) * (0.7 + 0.5 * prof)
            m.append(ellipse(x + rx * 0.3, yy + rx * 0.25, rx * 1.1, rx * 0.35, "#000", opacity=0.12))
            m.append(chemin(f"M {n(x - rx)} {n(yy)} Q {n(x - rx)} {n(yy - rx * 0.8)} {n(x)} {n(yy - rx * 0.75)} Q {n(x + rx)} {n(yy - rx * 0.7)} {n(x + rx)} {n(yy)} Z",
                            volume(melange(couleur, "#868e96", 0.55), 0.45, 0.7)))
        else:
            L = e * r.uniform(50, 90) * (0.7 + 0.5 * prof)
            m.append(chemin(f"M {n(x - L)} {n(yy)} Q {n(x)} {n(yy - L * 0.22)} {n(x + L)} {n(yy)}", stroke="#a5b4fc", sw=3 * e, opacity=0.45))
    S.add(g(m))


def terrain(c):
    """Sol plus clair au loin (en haut), plus sombre et plus contrasté devant."""
    if _rvb(c) is None:
        return c
    return lineaire([(0, eclaircir(c, 0.16)), (0.22, c), (1, _assombrir(c, 0.8))])


def relief_sol(S, crete, c, y0, y1, graine=1):
    """Liseré lumineux sur la crête et petites touches de texture, plus grandes
    au premier plan (perspective)."""
    if _rvb(c) is None or y1 <= y0:
        return
    S.add(chemin(crete, stroke=eclaircir(c, 0.45), sw=4, opacity=0.55))
    r = random.Random(graine)
    fonce = _assombrir(c, 0.78)
    m = []
    for _ in range(int(S.w / 30)):
        yy = r.uniform(y0, y1)
        k = 0.6 + 1.2 * (yy - y0) / max(y1 - y0, 1)
        xx = r.uniform(0, S.w)
        m.append(f"M {n(xx)} {n(yy)} q {n(4 * k)} {n(-6 * k)} {n(8 * k)} 0 m {n(3 * k)} 0 q {n(3 * k)} {n(-4 * k)} {n(6 * k)} 0")
    S.add(chemin(" ".join(m), stroke=fonce, sw=2.5, opacity=0.35))


def lointain(S, y, couleur="#b2f2bb", hauteur=110, graine=1, opacite=0.4, voile="#a5b4c8"):
    """Arrière-plan : une chaîne de collines lointaines, bleuie et à demi fondue
    dans le ciel (perspective atmosphérique)."""
    r2 = random.Random(graine)
    w = S.w
    d = [f"M -60 {n(y)} L -60 {n(y - hauteur * 0.55)}"]
    x0 = -60
    while x0 < w + 60:
        pas_ = r2.uniform(170, 260)
        hs, hb = y - hauteur * r2.uniform(1.9, 2.6), y - hauteur * r2.uniform(0.45, 0.7)
        d.append(f"Q {n(x0 + pas_ / 2)} {n(hs)} {n(x0 + pas_)} {n(hb)}")
        x0 += pas_
    d.append(f"L {n(x0)} {n(y)} Z")
    c = melange(couleur, voile, 0.25)
    S.add(chemin(" ".join(d), c, opacity=opacite))


def bosquet(x, y, s=1.0, couleur="#69db7c", graine=1, nb=3, lointain=False):
    """Petit groupe d'arbres (plan moyen) ; (x, y) = pied du groupe. lointain :
    contrastes adoucis, comme voilés par l'air (perspective atmosphérique)."""
    r = random.Random(graine)
    fonce = _assombrir(couleur, 0.85 if lointain else 0.62)
    clair, sombre = (0.12, 0.88) if lointain else (0.22, 0.72)
    m = [ellipse(6, 0, 16 + nb * 7, 5, "#000", opacity=0.05 if lointain else 0.1)]
    for k in range(nb):
        dx = (k - (nb - 1) / 2) * 15 + r.uniform(-4, 4)
        rr = r.uniform(10, 15) * (1.15 if k == nb // 2 else 1)
        m.append(rect(dx - 2, -10, 4, 10, _assombrir(couleur, 0.75 if lointain else 0.4)))
        m.append(ellipse(dx, -8 - rr, rr * 0.9, rr * 1.1, volume(couleur if k % 2 else fonce, clair, sombre)))
    return place(m, x, y, s)


def collines(S, y, couleur="#b2f2bb", graine=1, n_=3, hauteur=110, bosquets=True):
    """Collines du plan moyen, précédées d'une chaîne lointaine (arrière-plan) ;
    versant droit à l'ombre et, sur l'herbe, quelques bosquets lointains."""
    r = random.Random(graine)
    w = S.w
    hexa = _rvb(couleur) is not None
    if hexa and not getattr(S, "_lointain", False):
        S._lointain = True
        lointain(S, y, couleur, hauteur, graine + 101)
    remplissage = lineaire([(0, eclaircir(couleur, 0.28)), (0.5, couleur), (1, _assombrir(couleur, 0.88))]) if hexa else couleur
    if hexa:
        # plaine du plan moyen, au pied des collines, jusqu'au sol du premier plan
        clair = melange(couleur, "#e7f5ff", 0.3) if luminance(couleur) > 0.35 else eclaircir(couleur, 0.08)
        S.add(rect(0, y - 2, w, 140, lineaire([(0, clair), (1, couleur)])))
    ombre_versant = lineaire([(0.45, "#1c2a52", 0), (1, "#1c2a52", 0.16)], 0, 0, 1, 0)
    rb = random.Random(graine + 202)
    vert = hexa and bosquets and nature_sol(couleur) == "herbe"
    for i in range(n_):
        cx = (i + 0.5) * w / n_ + r.uniform(-60, 60)
        lw = w / n_ * r.uniform(0.8, 1.3)
        h = hauteur * r.uniform(0.7, 1.2)
        forme = f"M {n(cx - lw)} {y} Q {n(cx)} {n(y - h * 2)} {n(cx + lw)} {y} Z"
        S.add(chemin(forme, remplissage))
        if hexa:
            S.add(chemin(forme, ombre_versant))
            S.add(chemin(f"M {n(cx - lw * 0.7)} {n(y - h * 0.5)} Q {n(cx - lw * 0.35)} {n(y - h * 0.95)} {n(cx)} {n(y - h)}",
                         stroke=eclaircir(couleur, 0.5), sw=4, opacity=0.5))
        if vert and rb.random() < 0.75:
            # un bosquet posé sur la pente, petit et voilé : il est loin
            t = rb.uniform(0.28, 0.72)
            bx = (1 - t) ** 2 * (cx - lw) + 2 * (1 - t) * t * cx + t * t * (cx + lw)
            by = y - 2 * (1 - t) * t * h * 2 + 6
            k = (w / 800) * min(h / 110, 1.2) * 0.95
            S.add(bosquet(bx, by, k, melange(_assombrir(couleur, 0.8), "#a5b4c8", 0.22), graine=graine + i, nb=rb.choice((2, 3, 3, 4)), lointain=True))
    if hexa and luminance(couleur) > 0.35:
        # brume au pied des collines : elles reculent derrière le sol
        S.add(rect(0, y - hauteur * 0.7, w, hauteur * 0.7 + 4, lineaire([(0, "#ffffff", 0), (1, "#ffffff", 0.3)])))


def paysage(S, horizon=590, sol_y=650, herbe_="#8ce99a", colline="#b2f2bb", haut="#74c0fc", bas="#e7f5ff",
            graine=1, montagnes=False, soleil_=None, nuages=((150, 140, 0.8),)):
    """Paysage complet sur trois plans : ciel brumeux à l'horizon, montagnes ou
    collines lointaines (arrière-plan), collines et bosquets (plan moyen), sol
    texturé avec ses touffes (premier plan). soleil_ = (x, y) éventuel."""
    ciel(S, haut, bas)
    if soleil_:
        S.add(soleil(*soleil_))
    for nx, ny, ns in nuages:
        S.add(nuage(nx, ny, ns))
    if montagnes:
        S._lointain = True
        brume = eclaircir(bas, 0.2)
        for k, x0 in enumerate(range(-120, S.w + 120, 260)):
            hs = horizon - 230 - (k % 2) * 60
            S.add(g(pic(x0, horizon, x0 + 150, hs, x0 + 330, horizon, melange("#91a7ff", brume, 0.45)), opacity=0.75))
        S.add(rect(0, horizon - 140, S.w, 144, lineaire([(0, brume, 0), (1, brume, 0.6)])))
    collines(S, horizon, colline, graine=graine)
    sol(S, sol_y, herbe_)


def repoussoir(S, cote="gauche", couleur="#2b8a3e", graine=1, haut=None):
    """Feuillage sombre au tout premier plan, dans un coin du bas : il cadre la
    scène et creuse la profondeur. À poser en dernier."""
    r = random.Random(graine)
    e = S.w / 800
    sgn, x0 = (1, 0) if cote == "gauche" else (-1, S.w)
    haut = haut or S.h - 170 * e
    m = []
    for k in range(7):
        L = r.uniform(110, 190) * e
        a = math.radians(r.uniform(5, 62))
        bx = x0 + sgn * r.uniform(0, 90) * e
        by = S.h + 10
        tx, ty = bx + sgn * L * math.sin(a), max(by - L * math.cos(a), haut)
        c = _assombrir(couleur, r.uniform(0.6, 0.9))
        mx, my = (bx + tx) / 2, (by + ty) / 2
        largeur = L * 0.22
        m.append(chemin(f"M {n(bx)} {n(by)} Q {n(mx - largeur)} {n(my - largeur * 0.4)} {n(tx)} {n(ty)} Q {n(mx + largeur)} {n(my + largeur * 0.4)} {n(bx)} {n(by)} Z",
                        lineaire([(0, eclaircir(c, 0.25)), (1, _assombrir(c, 0.7))])))
        m.append(chemin(f"M {n(bx)} {n(by)} Q {n(mx)} {n(my)} {n(tx)} {n(ty)}", stroke=_assombrir(c, 0.6), sw=2 * e, opacity=0.6))
    S.add(g(m))


def soleil(x, y, r=55, couleur="#ffd43b", rayons=True, visage=False):
    m = [cercle(x, y, r * 1.6, radial([(0.55, couleur, 0.35), (1, couleur, 0)]))]
    if rayons:
        for k in range(12):
            a = k * math.pi / 6
            m.append(trait(x + math.cos(a) * (r + 12), y + math.sin(a) * (r + 12),
                           x + math.cos(a) * (r + 32), y + math.sin(a) * (r + 32), couleur, 8))
    m.append(cercle(x, y, r, radial([(0, eclaircir(couleur, 0.7)), (0.6, couleur), (1, _assombrir(couleur, 0.92))], fx=0.4, fy=0.38)
                    if _rvb(couleur) else couleur))
    if visage:
        m.append(yeux_simples(x, y - r * 0.1, r * 0.32, r * 0.1))
        m.append(chemin(f"M {n(x - r * 0.3)} {n(y + r * 0.25)} Q {n(x)} {n(y + r * 0.5)} {n(x + r * 0.3)} {n(y + r * 0.25)}", stroke="#e67700", sw=r * 0.08))
        m.append(ellipse(x - r * 0.55, y + r * 0.2, r * 0.14, r * 0.09, ROSE, opacity=0.6))
        m.append(ellipse(x + r * 0.55, y + r * 0.2, r * 0.14, r * 0.09, ROSE, opacity=0.6))
    return g(m)


def yeux_simples(x, y, ecart, r, couleur=ENCRE):
    return cercle(x - ecart, y, r, couleur) + cercle(x + ecart, y, r, couleur)


def lune(x, y, r=45, couleur="#fff3bf", fond_ciel=None, croissant=False, visage=False, halo=True):
    if halo:
        lumiere_auto(x, y, r * 2.6, "#e7f5ff", 0.4)
    m = [cercle(x, y, r * 1.9, radial([(0.45, couleur, 0.22), (1, couleur, 0)])), cercle(x, y, r * 1.5, couleur, opacity=0.15),
         cercle(x, y, r, volume(couleur, 0.6, 0.88))]
    if croissant and fond_ciel:
        m.append(sans_relief(cercle(x + r * 0.45, y - r * 0.2, r * 0.9, fond_ciel)))
    else:
        m.append(cercle(x - r * 0.3, y - r * 0.25, r * 0.16, "#ffe066", opacity=0.6))
        m.append(cercle(x + r * 0.35, y + r * 0.3, r * 0.11, "#ffe066", opacity=0.6))
        m.append(cercle(x + r * 0.05, y - r * 0.55, r * 0.08, "#ffe066", opacity=0.5))
        m.append(chemin(f"M {n(x - r * 0.3 - r * 0.13)} {n(y - r * 0.25 + r * 0.06)} a {n(r * 0.14)} {n(r * 0.14)} 0 0 0 {n(r * 0.26)} 0",
                        stroke="#ffffff", sw=max(r * 0.04, 1), opacity=0.6))
    if visage and not croissant:
        m.append(chemin(f"M {n(x - r * .45)} {n(y - r * .05)} q {n(r * .15)} {n(r * .15)} {n(r * .3)} 0", stroke="#b08900", sw=r * .07))
        m.append(chemin(f"M {n(x + r * .15)} {n(y - r * .05)} q {n(r * .15)} {n(r * .15)} {n(r * .3)} 0", stroke="#b08900", sw=r * .07))
        m.append(chemin(f"M {n(x - r * .2)} {n(y + r * .35)} q {n(r * .2)} {n(r * .15)} {n(r * .4)} 0", stroke="#b08900", sw=r * .07))
    return g(m)


def etoile5(x, y, r, couleur="#ffe066", rot=0, **a):
    pts = []
    for k in range(10):
        ang = math.radians(rot - 90 + k * 36)
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((x + rr * math.cos(ang), y + rr * math.sin(ang)))
    return poly(pts, couleur, stroke=couleur, stroke_width=r * 0.18, stroke_linejoin="round", **a)


def etoiles(S, nb=30, graine=3, zone=(0, 0, 800, 450), couleur="#fff3bf"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        if r.random() < 0.3:
            S.add(etoile5(x, y, r.uniform(6, 11), couleur, rot=r.uniform(0, 30)))
        else:
            S.add(cercle(x, y, r.uniform(1.5, 3.5), couleur))


def nuit(S, haut="#1c2a52", bas="#4c5b9a"):
    ciel(S, haut, bas)
    S._decor("nuit")


def nuage(x, y, s=1.0, couleur="#ffffff", ombre=None, opacity=None):
    forme = (
        cercle(-55, 10, 38, couleur) + cercle(-15, -18, 50, couleur) + cercle(40, -8, 42, couleur)
        + cercle(78, 18, 30, couleur) + rect(-95, 5, 200, 50, couleur, rx=25)
    )
    m = []
    if ombre:
        m.append(g(forme.replace(f'fill="{couleur}"', f'fill="{ombre}"'), "translate(0 8)"))
    m.append(forme)
    # modelé : dessus éclairé, ventre du nuage dans l'ombre
    modele = lineaire([(0, "#ffffff", 0.5), (0.4, "#ffffff", 0), (0.62, "#1c2a52", 0), (1, "#1c2a52", 0.16)], 0, -68, 0, 55, espace="userSpaceOnUse")
    m.append(forme.replace(f'fill="{couleur}"', f'fill="{modele}"'))
    m.append(ellipse(-22, -46, 22, 9, "#ffffff", opacity=0.55, rot=-12))
    return place(g(m, opacity=opacity), x, y, s)


def arbre(x, y, s=1.0, feuillage="#51cf66", feuillage2="#40c057", tronc="#8d5524", fruits=None):
    fonce = _assombrir(tronc, 0.68)
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(4, 0, 58, 9, 0.14))
    m += [rect(-16, -140, 32, 140, cylindre(tronc), rx=8),
          chemin("M -17 -2 Q -24 2 -34 4 L 34 4 Q 24 2 17 -2 Z", _assombrir(tronc, 0.85)),
          chemin("M 0 -100 Q 22 -118 46 -150", stroke=tronc, sw=11),
          chemin("M -2 -112 Q -22 -128 -40 -160", stroke=tronc, sw=9),
          chemin("M -6 -24 q 4 -18 0 -36 M 7 -60 q -4 -16 2 -34 M -4 -100 q 3 -10 0 -18", stroke=fonce, sw=2.5, opacity=0.55)]
    couronne = [(0, -200, 80, feuillage), (-60, -160, 52, feuillage2), (60, -160, 52, feuillage2)]
    for cx, cy, rr, c in couronne:
        m.append(cercle(cx, cy, rr, volume(c, 0.28, 0.8)))
    m.append(cercle(-25, -235, 45, eclaircir(feuillage2, 0.12), opacity=0.5))
    # ombre portée de la couronne sur elle-même et touches de feuilles
    m.append(ombrage(g([cercle(cx, cy, rr, "#000") for cx, cy, rr, _ in couronne]),
                     sombre=[(30, -132, 110, 40)], clair=[(-30, -250, 34, 18, -20)], opacite=0.14))
    feuilles = _assombrir(feuillage, 0.78)
    touffe = "q 3 -7 8 -4 q 4 -6 9 -1"
    m.append(chemin(" ".join(f"M {fx} {fy} {touffe}" for fx, fy in ((-50, -190), (16, -226), (34, -180), (-80, -146), (60, -140), (-16, -160), (-30, -124), (40, -118))),
                    stroke=feuilles, sw=2.5, opacity=0.45))
    if fruits:
        for fx, fy in [(-40, -200), (35, -230), (55, -170), (-10, -160), (10, -265)]:
            m.append(cercle(fx, fy, 10, volume(fruits, 0.45, 0.75)))
            m.append(cercle(fx - 3, fy - 4, 2.5, "#ffffff", opacity=0.7))
    return place(m, x, y, s)


def sapin(x, y, s=1.0, couleur="#2f9e44", couleur2="#37b24d", neige=False):
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(4, 0, 70, 9, 0.14))
    m.append(rect(-12, -40, 24, 40, cylindre("#7c4a1e"), rx=4))
    etages = [(90, -40), (72, -110), (52, -170)]
    for k, (w, yy) in enumerate(etages):
        c = couleur if k % 2 == 0 else couleur2
        m.append(poly([(-w, yy), (0, yy - 110), (w, yy)], cylindre(c, 0.2, 0.7)))
        # bord inférieur dentelé, un peu plus sombre
        dents = " ".join(f"L {n(-w + (i + 0.5) * w / 4)} {n(yy + 7)} L {n(-w + (i + 1) * w / 4)} {n(yy)}" for i in range(8))
        m.append(chemin(f"M {-w} {yy} {dents} Z", _assombrir(c, 0.82)))
        if k + 1 < len(etages):
            # ombre de l'étage du dessus
            yh = etages[k + 1][1]
            a, b = w * (yy - 110 - yh) / -110, w * (yy - 110 - yh - 16) / -110
            m.append(poly([(-a, yh), (a, yh), (b, yh + 16), (-b, yh + 16)], "#000", opacity=0.16))
        if neige:
            m.append(poly([(-w * 0.35, yy - 72), (0, yy - 110), (w * 0.35, yy - 72)], "#fff"))
            m.append(poly([(w * 0.1, yy - 72), (0, yy - 110), (w * 0.35, yy - 72)], "#dbe4ff"))
    return place(m, x, y, s)


def fleur(x, y, s=1.0, couleur="#ff6b6b", coeur="#ffd43b", tige=60):
    m = [trait(0, 0, 0, -tige, "#40c057", 5),
         ellipse(10, -tige * 0.45, 12, 5, "#51cf66", rot=-30)]
    petale = volume(couleur, 0.35, 0.8)
    for k in range(5):
        a = k * 2 * math.pi / 5
        m.append(cercle(math.cos(a) * 11, -tige + math.sin(a) * 11, 10, petale))
    m.append(cercle(0, -tige, 8, volume(coeur, 0.5, 0.75)))
    return place(m, x, y, s)


def herbe(x, y, s=1.0, couleur="#40c057"):
    remplissage = lineaire([(0, eclaircir(couleur, 0.25)), (1, _assombrir(couleur, 0.75))]) if _rvb(couleur) else couleur
    return place(chemin("M -14 0 Q -12 -18 -20 -30 Q -6 -16 -4 0 Q -2 -26 4 -40 Q 6 -18 6 0 Q 10 -16 22 -26 Q 14 -12 14 0 Z", remplissage), x, y, s)


def buisson(x, y, s=1.0, couleur="#40c057", couleur2="#51cf66", baies=None):
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(4, 0, 84, 9, 0.13))
    boules = [(-45, -30, 38, couleur), (45, -30, 38, couleur), (0, -55, 48, couleur2)]
    m.append(rect(-80, -32, 160, 32, _assombrir(couleur, 0.9)))
    m += [cercle(cx, cy, rr, volume(c, 0.3, 0.8)) for cx, cy, rr, c in boules]
    m.append(chemin("M -56 -40 q 3 -7 8 -4 q 4 -6 9 -1 M -8 -78 q 3 -7 8 -4 q 4 -6 9 -1 M 30 -46 q 3 -7 8 -4 q 4 -6 9 -1", stroke=_assombrir(couleur, 0.75), sw=3, opacity=0.5))
    if baies:
        for bx, by in [(-40, -45), (-5, -75), (30, -50), (55, -25), (-20, -20)]:
            m.append(cercle(bx, by, 7, volume(baies, 0.5, 0.75)))
            m.append(cercle(bx - 2, by - 2.5, 1.8, "#ffffff", opacity=0.7))
    return place(m, x, y, s)


def champignon(x, y, s=1.0, couleur="#fa5252", pied="#fff4e6"):
    m = [rect(-18, -55, 36, 55, cylindre(pied, 0.3, 0.82), rx=12),
         ellipse(0, -46, 52, 9, _assombrir(pied, 0.8)),
         chemin("M -60 -45 Q -60 -115 0 -115 Q 60 -115 60 -45 Z", volume(couleur, 0.35, 0.72)),
         chemin("M -60 -45 Q 0 -36 60 -45", stroke=_assombrir(couleur, 0.7), sw=4),
         cercle(-28, -75, 9, "#fff"), cercle(12, -95, 8, "#fff"), cercle(30, -62, 7, "#fff"),
         ellipse(-26, -98, 14, 6, "#fff", opacity=0.35, rot=-30)]
    return place(m, x, y, s)


def caillou(x, y, s=1.0, couleur="#adb5bd"):
    d = "M -40 0 Q -45 -30 -10 -34 Q 30 -40 42 -12 Q 46 0 40 0 Z"
    return place([ellipse(4, 0, 46, 6, "#000", opacity=0.12), chemin(d, volume(couleur, 0.4, 0.7)),
                  chemin("M -22 -24 Q -10 -30 4 -28", stroke="#fff", sw=3, opacity=0.45),
                  chemin("M 12 -20 l 6 6 l -2 8", stroke=_assombrir(couleur, 0.65), sw=2, opacity=0.6)], x, y, s)


# Profondeur des bâtiments vus de trois quarts : le côté droit fuit vers le
# haut à droite (lumière venue de la gauche : ce côté est dans l'ombre).
FUITE = (30, -15)


def volet(x, y, w, h, c, lames=True):
    """Volet ouvert en bois peint, (x, y) = coin haut gauche : cadre, lames et
    petite ombre portée sur le mur."""
    m = [rect(x + 2, y + 3, w, h, "#000", opacity=0.14),
         rect(x, y, w, h, cylindre(c, 0.25, 0.8), rx=2),
         rect(x, y, w, h, "none", rx=2, stroke=_assombrir(c, 0.68), stroke_width=1.5)]
    if lames:
        m.append(chemin(" ".join(f"M {n(x + 2)} {n(yy)} h {n(w - 4)}" for yy in [y + h * (k + 1) / 7 for k in range(6)]),
                        stroke=_assombrir(c, 0.7), sw=1.5, opacity=0.6))
    return g(m)


def fenetre_facade(x, y, w, h, mur, vitre="#a5d8ff", volets=None, cadre="#ffffff", lumiere=False, arc=False):
    """Fenêtre d'une façade, (x, y) = coin haut gauche du vitrage : linteau,
    ébrasement dans l'ombre, croisillons, reflet, appui saillant, volets."""
    fonce = _assombrir(mur, 0.76)
    m = []
    if volets:
        lv = w * 0.3
        m += [volet(x - lv - 3, y - 2, lv, h + 4, volets), volet(x + w + 3, y - 2, lv, h + 4, volets)]
    haut = f"M {n(x)} {n(y + w * 0.5)} A {n(w / 2)} {n(w / 2)} 0 0 1 {n(x + w)} {n(y + w * 0.5)}" if arc else None
    if arc:
        forme = f"{haut} V {n(y + h)} H {n(x)} Z"
        m += [chemin(f"M {n(x - 6)} {n(y + w * 0.5)} A {n(w / 2 + 6)} {n(w / 2 + 6)} 0 0 1 {n(x + w + 6)} {n(y + w * 0.5)} V {n(y + h)} H {n(x - 6)} Z", fonce),
              chemin(forme, vitre)]
    else:
        m += [rect(x - 6, y - 9, w + 12, 8, fonce, rx=2),
              rect(x - 3, y - 3, w + 6, h + 6, fonce, rx=2),
              rect(x, y, w, h, vitre)]
    if lumiere:
        m.append(rect(x, y, w, h, radial([(0, "#fff3bf", 0.7), (1, "#fff3bf", 0)])))
    m += [poly([(x, y), (x + w, y), (x + w, y + 6), (x + 6, y + 6), (x + 6, y + h), (x, y + h)], "#000", opacity=0.2),
          poly([(x + w * 0.2, y + h), (x + w * 0.55, y), (x + w * 0.72, y), (x + w * 0.37, y + h)], "#fff", opacity=0.22 if not lumiere else 0.12),
          trait(x + w / 2, y + 2, x + w / 2, y + h, cadre, max(2.5, w / 14)),
          trait(x, y + h * 0.45, x + w, y + h * 0.45, cadre, max(2.5, w / 14))]
    if arc:
        m.append(chemin(f"{haut} V {n(y + h)} H {n(x)} Z", stroke=cadre, sw=max(3, w / 10)))
    else:
        m.append(rect(x, y, w, h, "none", stroke=cadre, stroke_width=max(3, w / 10)))
    m += [rect(x - 7, y + h, w + 14, 7, eclaircir(mur, 0.6), rx=2),
          rect(x - 5, y + h + 7, w + 10, 5, "#000", opacity=0.13)]
    if lumiere:
        m.append(ellipse(x + w / 2, y + h / 2, w * 1.1, h, radial([(0, "#ffe066", 0.4), (1, "#ffe066", 0)])))
    return g(m)


def chainage(x, y, h, c, cote=1, hb=18):
    """Pierres d'angle en harpe le long d'un coin de mur (cote = 1 : bord
    gauche, -1 : bord droit)."""
    m = []
    for k, yy in enumerate(range(int(y), int(y + h) - 4, hb)):
        lw = 22 if k % 2 == 0 else 14
        xx = x if cote > 0 else x - lw
        m.append(rect(xx, yy + 1, lw, hb - 2, cylindre(c, 0.3, 0.8), rx=1.5))
        m.append(rect(xx, yy + hb - 3, lw, 2, "#000", opacity=0.15))
    return g(m)


def cote_batiment(x, y, h, mur, toit_haut=None, fuite=FUITE, textures=True):
    """Mur latéral en perspective, accroché au bord droit (x) d'une façade dont
    le haut est en y et le pied en y + h ; il fuit selon `fuite` et reste dans
    l'ombre."""
    dx, dy = fuite
    m = [poly([(x, y), (x + dx, y + dy), (x + dx, y + h + dy), (x, y + h)],
              lineaire([(0, _assombrir(mur, 0.74)), (1, _assombrir(mur, 0.62))], 0, 0, 1, 0))]
    if textures:
        pas_ = 14
        m.append(chemin(" ".join(f"M {n(x)} {n(yy)} l {n(dx)} {n(dy)}" for yy in range(int(y + pas_), int(y + h), pas_)),
                        stroke=_assombrir(mur, 0.5), sw=1.2, opacity=0.3))
    m.append(trait(x, y, x, y + h, _assombrir(mur, 0.55), 1.5, opacity=0.6))
    return g(m)


def maison(x, y, s=1.0, mur="#ffe8cc", toit="#e8590c", porte="#a0522d", fenetre="#a5d8ff", lumiere=False,
           cote=True, volets=None, cheminee=True, halo=True):
    """Maison vue de trois quarts ; (x, y) = milieu du pied de la façade.
    cote : mur latéral et pan de toit en perspective ; volets : couleur des
    volets ouverts de part et d'autre des fenêtres."""
    vitre = "#ffe066" if lumiere else fenetre
    fonce_m = _assombrir(mur, 0.78)
    fonce_t = _assombrir(toit, 0.68)
    dx, dy = FUITE
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(24 if cote else 14, 0, 160 if cote else 150, 16, 0.16))
    # cheminée en briques, qui sort du pan de toit
    che = [rect(55, -235, 26, 75, cylindre("#c92a2a", 0.2, 0.7)),
           rect(81, -235, 9, 75, "#7a1a1a"),
           chemin("M 55 -222 H 81 M 55 -209 H 81 M 55 -196 H 81 M 68 -235 V -222 M 62 -222 V -209 M 74 -209 V -196",
                  stroke="#8f1d1d", sw=1.5, opacity=0.6),
           rect(51, -242, 42, 9, "#a61e1e", rx=2), rect(51, -242, 42, 3, "#e03131", rx=1.5)] if cheminee else []
    if not cote:
        m += che
    if cote:
        # pan de toit qui fuit, puis mur latéral dans l'ombre
        pan = [(0, -250), (dx, -250 + dy), (125 + dx, -145 + dy), (125, -145)]
        m.append(poly(pan, lineaire([(0, _assombrir(toit, 0.82)), (1, _assombrir(toit, 0.66))], 0, 0, 1, 1)))
        m.append(_decoupe(chemin(" ".join(f"M {n(t * 125 - 4)} {n(-250 + t * 105)} l {n(dx + 8)} {n(dy)}" for t in [k / 7 for k in range(1, 7)]),
                                 stroke=_assombrir(toit, 0.5), sw=2, opacity=0.5), poly(pan, "#000")))
        m.append(chemin(f"M 0 -250 l {dx} {dy} M 125 -145 l {dx} {dy}", stroke=_assombrir(toit, 0.55), sw=4))
        m += che
        m.append(cote_batiment(100, -150, 150, mur))
        m.append(poly([(100, -150), (100 + dx, -150 + dy), (100 + dx, -132 + dy), (100, -132)], "#000", opacity=0.2))
        m.append(poly([(100, -16), (100 + dx, -16 + dy), (100 + dx, dy), (100, 0)], _assombrir("#ced4da", 0.7)))
    # murs : bardage, coins et soubassement
    m.append(rect(-100, -150, 200, 150, cylindre(mur, 0.15, 0.86)))
    m.append(chemin(" ".join(f"M -100 {yy} H 100" for yy in range(-136, -12, 14)), stroke=fonce_m, sw=1.5, opacity=0.3))
    m += [chainage(-100, -146, 130, eclaircir(mur, 0.4), 1), chainage(100, -146, 130, _assombrir(mur, 0.9), -1),
          rect(-104, -16, 208, 16, cylindre("#ced4da", 0.2, 0.8), rx=2),
          chemin("M -70 -16 V 0 M -30 -16 V -8 M 10 -16 V 0 M 50 -16 V -8 M -104 -8 H 104", stroke="#868e96", sw=1.5, opacity=0.7)]
    # ombre sous l'avancée du toit
    m.append(poly([(-100, -150), (100, -150), (100, -128), (-100, -138)], "#000", opacity=0.18))
    # toit en tuiles
    triangle = [(-125, -145), (0, -250), (125, -145)]
    m.append(poly(triangle, lineaire([(0, eclaircir(toit, 0.22)), (0.5, toit), (1, _assombrir(toit, 0.8))], 0, 0, 1, 1)))
    cid = uid("k")
    tuiles = " ".join(f"M {x0} {yy} " + " ".join("q 8 9 16 0" for _ in range(17))
                      for k, yy in enumerate(range(-232, -146, 15)) for x0 in [-136 + (k % 2) * 8])
    m.append(el("clipPath", poly(triangle, "#000"), id=cid) + g(chemin(tuiles, stroke=fonce_t, sw=2, opacity=0.55), clip_path=f"url(#{cid})"))
    m += [rect(-129, -149, 258, 7, fonce_t, rx=3),
          # gouttière et descente d'eau
          rect(-127, -143, 254, 6, cylindre("#adb5bd", 0.4, 0.7, vertical=True), rx=3),
          rect(106, -140, 6, 136, cylindre("#adb5bd", 0.4, 0.7), rx=3),
          chemin("M -125 -145 L 0 -250 L 125 -145", stroke=_assombrir(toit, 0.6), sw=6),
          chemin("M -112 -150 L 0 -243", stroke=eclaircir(toit, 0.4), sw=3, opacity=0.6)]
    # porte : encadrement, panneaux, marche, auvent
    m += [rect(-31, -92, 62, 92, eclaircir(mur, 0.55), rx=4),
          rect(-25, -85, 50, 85, cylindre(porte, 0.2, 0.75), rx=6),
          rect(-25, -85, 50, 8, "#000", opacity=0.18, rx=4),
          rect(-17, -76, 34, 28, "none", rx=3, stroke=_assombrir(porte, 0.7), stroke_width=2.5),
          rect(-17, -42, 34, 30, "none", rx=3, stroke=_assombrir(porte, 0.7), stroke_width=2.5),
          trait(-15, -74, 15, -74, eclaircir(porte, 0.4), 1.5, opacity=0.7),
          cercle(14, -42, 4.5, volume("#ffd43b", 0.6, 0.7)), cercle(13, -43.5, 1.5, "#fff"),
          rect(-36, -7, 72, 9, cylindre("#adb5bd", 0.3, 0.8), rx=2),
          rect(-36, 1, 72, 3, "#000", opacity=0.15),
          rect(-36, -100, 72, 8, fonce_m, rx=2)]
    # fenêtres : linteau, ébrasement, reflets, appui, volets
    for fx in ((-82, 46) if volets else (-80, 40)):
        m.append(fenetre_facade(fx, -120, 36 if volets else 40, 40, mur, vitre, volets=volets))
        if lumiere:
            m.append(ellipse(fx + 20, -100, 44, 40, radial([(0, "#ffe066", 0.45), (1, "#ffe066", 0)])))
            if halo:
                lumiere_auto(x + (fx + 20) * s, y - 100 * s, 95 * s, "#ffd43b", 0.55)
    return place(m, x, y, s)


def garde_corps(x, y, w, c="#343a40", h=20):
    """Balcon en fer forgé, (x, y) = coin haut gauche : dalle, barreaux et
    main courante, avec l'ombre de la dalle sur le mur."""
    m = [rect(x - 4, y + h, w + 8, 6, "#adb5bd", rx=1.5), rect(x - 2, y + h + 6, w + 4, 6, "#000", opacity=0.16),
         chemin(" ".join(f"M {n(xx)} {n(y)} v {h}" for xx in [x + 4 + k * 7 for k in range(int((w - 4) / 7) + 1)]), stroke=c, sw=1.8),
         chemin(f"M {n(x)} {n(y + h * 0.5)} h {n(w)}", stroke=c, sw=1.2, opacity=0.6),
         rect(x - 2, y - 3, w + 4, 4, c, rx=2)]
    return g(m)


def store_banne(x, y, w, c="#fa5252", c2="#ffffff", h=26):
    """Store rayé au-dessus d'une vitrine, (x, y) = coin haut gauche ; ombre
    portée sous le lambrequin."""
    bandes = int(w / 14)
    m = [rect(x, y + h + 4, w, 14, "#000", opacity=0.14)]
    for k in range(bandes):
        cc = c if k % 2 == 0 else c2
        x0, x1 = x + k * w / bandes, x + (k + 1) * w / bandes
        m.append(poly([(x0 + 6, y), (x1 + 6, y), (x1, y + h), (x0, y + h)], lineaire([(0, eclaircir(cc, 0.2)), (1, _assombrir(cc, 0.85))])))
        m.append(chemin(f"M {n(x0)} {n(y + h)} Q {n((x0 + x1) / 2)} {n(y + h + 9)} {n(x1)} {n(y + h)} Z", _assombrir(cc, 0.92)))
    m.append(trait(x + 6, y, x + w + 6, y, _assombrir(c, 0.6), 3))
    return g(m)


def immeuble(x, y, w=150, etages=3, couleur="#ffd8a8", toit="mansarde", toit_c=None, rdc="porte",
             volets=None, balcons=True, cote=True, lumiere=False, graine=1, h_etage=70, store=None, fuite=(22, -11)):
    """Immeuble de ville vu de trois quarts ; (x, y) = coin bas gauche de la façade.

    toit : "mansarde" (ardoises et lucarnes), "pignon" (tuiles), "plat" (corniche) ;
    rdc : "porte", "boutique" (vitrine et store) ou None ; volets : couleur ;
    balcons : garde-corps au premier étage ; lumiere : fenêtres éclairées (soir)."""
    r = random.Random(graine)
    toit_c = toit_c or ("#5c6b8a" if toit == "mansarde" else "#c2410c" if toit == "pignon" else _assombrir(couleur, 0.7))
    h = etages * h_etage + 20
    haut = y - h
    dx, dy = fuite
    fonce = _assombrir(couleur, 0.78)
    vitre = "#ffe066" if lumiere else "#a5d8ff"
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(x + w / 2 + dx, y, w * 0.6, 10, 0.14))
    # toit (derrière la corniche)
    if toit == "mansarde":
        ht = 46
        m.append(poly([(x - 2, haut), (x + 12, haut - ht), (x + w - 12, haut - ht), (x + w + 2, haut)], lineaire([eclaircir(toit_c, 0.2), toit_c, _assombrir(toit_c, 0.75)], 0, 0, 1, 0)))
        if cote:
            m.append(poly([(x + w + 2, haut), (x + w - 12, haut - ht), (x + w - 12 + dx, haut - ht + dy), (x + w + 2 + dx, haut + dy)], _assombrir(toit_c, 0.62)))
        m.append(_decoupe(chemin(" ".join(f"M {n(x - 4)} {n(haut - k * 9)} h {n(w + 8)}" for k in range(1, 6)), stroke=_assombrir(toit_c, 0.6), sw=1.5, opacity=0.5),
                          poly([(x - 2, haut), (x + 12, haut - ht), (x + w - 12, haut - ht), (x + w + 2, haut)], "#000")))
        m.append(rect(x + 8, haut - ht - 4, w - 16, 6, _assombrir(toit_c, 0.7), rx=2))
        for k in range(max(1, int(w / 70))):
            lx = x + (k + 0.5) * w / max(1, int(w / 70)) - 13
            m += [poly([(lx - 4, haut - 22), (lx + 13, haut - 40), (lx + 30, haut - 22)], _assombrir(toit_c, 0.85)),
                  rect(lx, haut - 22, 26, 22, eclaircir(couleur, 0.4)),
                  rect(lx + 5, haut - 18, 16, 16, vitre), rect(lx + 5, haut - 18, 16, 4, "#000", opacity=0.2)]
    elif toit == "pignon":
        ht = 58
        tri = [(x - 8, haut), (x + w / 2, haut - ht), (x + w + 8, haut)]
        if cote:
            m.append(poly([(x + w / 2, haut - ht), (x + w / 2 + dx, haut - ht + dy), (x + w + 8 + dx, haut + dy), (x + w + 8, haut)], _assombrir(toit_c, 0.66)))
        m.append(poly(tri, lineaire([(0, eclaircir(toit_c, 0.2)), (1, _assombrir(toit_c, 0.8))], 0, 0, 1, 1)))
        m.append(tuiles(x - 10, haut - ht, w + 20, ht, toit_c, forme=poly(tri, "#000"), pas_=12))
        m.append(chemin(f"M {n(x - 8)} {n(haut)} L {n(x + w / 2)} {n(haut - ht)} L {n(x + w + 8)} {n(haut)}", stroke=_assombrir(toit_c, 0.6), sw=4))
        ht = ht * 0.6
    else:
        ht = 0
    # cheminées
    for k in range(r.choice((1, 2))):
        cx = x + w * r.uniform(0.15, 0.75)
        m += [rect(cx, haut - ht - 30, 18, 34 + ht * 0.3, cylindre("#b5835a", 0.25, 0.7)), rect(cx - 3, haut - ht - 34, 24, 6, "#8d5b34", rx=1.5)]
    # mur latéral, façade et enduit
    if cote:
        m.append(cote_batiment(x + w, haut, h, couleur, fuite=fuite))
    m.append(rect(x, haut, w, h, cylindre(couleur, 0.18, 0.86)))
    m.append(rect(x, y - h_etage + 10, w, h_etage - 10, _assombrir(couleur, 0.92)))
    m.append(chemin(" ".join(f"M {n(x)} {n(yy)} h {n(w)}" for yy in range(int(y - h_etage + 22), int(y), 12)), stroke=_assombrir(couleur, 0.66), sw=1.3, opacity=0.45))
    m.append(chainage(x, haut + 22, h - h_etage - 14, eclaircir(couleur, 0.4), 1, hb=16))
    # corniche du haut et bandeaux entre les étages, chacun avec son ombre
    m += [rect(x - 6, haut, w + 12, 12, eclaircir(couleur, 0.35), rx=2), rect(x - 6, haut + 9, w + 12, 3, _assombrir(couleur, 0.7)),
          ombre_avancee(x, haut + 12, w, 16, 0.22)]
    for k in range(1, etages):
        yy = y - k * h_etage + 10
        m += [rect(x - 3, yy - 6, w + 6, 7, eclaircir(couleur, 0.3), rx=1.5), ombre_avancee(x, yy + 1, w, 8, 0.15)]
    # fenêtres
    cols = max(2, int(w / 55))
    fw = min(34, w / cols - 26)
    for k in range(1, etages):
        fy = y - (k + 1) * h_etage + 24
        for c_ in range(cols):
            fx = x + (c_ + 0.5) * w / cols - fw / 2
            allume = lumiere and r.random() < 0.7
            m.append(fenetre_facade(fx, fy, fw, h_etage - 36, couleur, "#ffe066" if allume else "#a5d8ff", volets=volets,
                                    lumiere=allume, arc=(k == etages - 1 and toit == "plat")))
        if balcons and k == 1:
            m.append(garde_corps(x + w / cols * 0.5 - fw / 2 - 8, y - 2 * h_etage + h_etage - 34, w - w / cols + fw + 16))
    # rez-de-chaussée
    if rdc == "boutique":
        vw = w * 0.55
        m += [rect(x + 10, y - h_etage + 22, vw, h_etage - 22, fonce),
              rect(x + 14, y - h_etage + 26, vw - 8, h_etage - 30, vitre if lumiere else "#d0ebff"),
              poly([(x + 14 + vw * 0.2, y - 4), (x + 14 + vw * 0.45, y - h_etage + 26), (x + 14 + vw * 0.6, y - h_etage + 26), (x + 14 + vw * 0.35, y - 4)], "#fff", opacity=0.3),
              store_banne(x + 4, y - h_etage + 2, vw + 8, store or r.choice(("#fa5252", "#228be6", "#40c057", "#fab005")))]
        px = x + w * 0.75
    else:
        px = x + w / 2
    if rdc:
        m += [chemin(f"M {n(px - 19)} {y} V {n(y - 40)} A 19 19 0 0 1 {n(px + 19)} {n(y - 40)} V {y} Z", fonce),
              chemin(f"M {n(px - 14)} {y} V {n(y - 38)} A 14 14 0 0 1 {n(px + 14)} {n(y - 38)} V {y} Z", cylindre("#8d5b34", 0.25, 0.7)),
              trait(px, y - 50, px, y, "#5c3a1e", 1.5, opacity=0.6), cercle(px + 8, y - 22, 2.5, "#ffd43b"),
              rect(px - 22, y - 4, 44, 5, "#adb5bd", rx=1.5)]
    return g(m)


def feuillage(boules, opacite=None):
    """Couronne d'arbre en relief : boules (x, y, r, couleur) éclairées en haut
    à gauche, touffes de feuilles et ombre du dessous."""
    m = [cercle(x, y, r, volume(c, 0.28, 0.72)) for x, y, r, c in boules]
    m.append(ombrage(g([cercle(x, y, r, "#000") for x, y, r, _ in boules]),
                     sombre=[(x + r * 0.3, y + r * 0.75, r * 0.95, r * 0.4) for x, y, r, _ in boules], opacite=0.1))
    touffe = "q 4 -9 10 -5 q 5 -8 11 -1"
    for x, y, r, c in boules:
        k = r / 90
        m.append(chemin(" ".join(f"M {n(x + dx * r)} {n(y + dy * r)} q {n(4 * k)} {n(-9 * k)} {n(10 * k)} {n(-5 * k)} q {n(5 * k)} {n(-8 * k)} {n(11 * k)} {n(-1 * k)}"
                                 for dx, dy in [(-0.45, 0.05), (0.15, -0.35), (0.05, 0.4), (-0.15, -0.6)]),
                        stroke=_assombrir(c, 0.72), sw=max(2, 3 * k), opacity=0.45))
    return g(m, opacity=opacite)


def tronc(x, y, w, h, c="#8d5524", rx=12):
    """Tronc vertical en relief ; (x, y) = coin haut gauche."""
    r = random.Random(int(x * 3 + h))
    fentes = " ".join(f"M {n(x + w * (k + 0.5) / 4 + r.uniform(-4, 4))} {n(y0)} q {n(r.uniform(-5, 5))} {n(L / 2)} 0 {n(L)}"
                      for k in range(4) for y0, L in [(y + r.uniform(0.1, 0.5) * h, r.uniform(0.12, 0.25) * h)])
    return g([rect(x, y, w, h, cylindre(c, 0.25, 0.65), rx=rx),
              chemin(fentes, stroke=_assombrir(c, 0.62), sw=max(2, w / 22), opacity=0.55)])


def arbre_branche(S, x, branche_y, branche_x, w, feuillage, clairs, tronc="#8d5524", sol_y=700):
    """Grand arbre coupé par le haut de la page, une longue branche horizontale
    vers la gauche (perchoir) ; feuillage / clairs : listes de (x, y, r)."""
    fonce = _assombrir(tronc, 0.65)
    S.add(ombre_sol(x + 10, sol_y, w * 1.25, 15, 0.2))
    S.add(rect(x - w / 2, 0, w, sol_y, cylindre(tronc, 0.25, 0.65)))
    S.add(chemin(f"M {n(x - w / 2 - 14)} {sol_y + 2} Q {n(x - w / 2)} {sol_y - 20} {n(x - w / 2)} {sol_y - 60} L {n(x + w / 2)} {sol_y - 60} "
                 f"Q {n(x + w / 2)} {sol_y - 20} {n(x + w / 2 + 18)} {sol_y + 2} Z", cylindre(tronc, 0.25, 0.65)))
    # écorce : longues fentes et nœud
    r = random.Random(int(x))
    fentes = " ".join(f"M {n(x - w / 2 + k * w / 5)} {n(y0)} q {n(r.uniform(-6, 6))} {n(L / 2)} 0 {n(L)}"
                      for k in range(1, 5) for y0, L in [(r.uniform(20, 300), r.uniform(80, 160)), (r.uniform(380, 560), r.uniform(60, 120))])
    S.add(chemin(fentes, stroke=fonce, sw=3, opacity=0.55))
    S.add(ellipse(x + w * 0.12, 470, w * 0.14, w * 0.2, fonce, opacity=0.6), ellipse(x + w * 0.12, 472, w * 0.07, w * 0.11, _assombrir(tronc, 0.45)))
    branche = (f"M {n(x - w / 2 + 4)} {branche_y + 24} Q {n((x + branche_x) / 2)} {branche_y + 8} {branche_x} {branche_y + 4} "
               f"L {branche_x} {branche_y + 24} Q {n((x + branche_x) / 2)} {branche_y + 38} {n(x - w / 2 + 4)} {branche_y + 54} Z")
    S.add(chemin(branche, lineaire([eclaircir(tronc, 0.25), tronc, fonce])))
    S.add(chemin(f"M {n(x - w / 2 + 4)} {branche_y + 26} Q {n((x + branche_x) / 2)} {branche_y + 10} {branche_x} {branche_y + 6}",
                 stroke=eclaircir(tronc, 0.4), sw=3, opacity=0.7))
    # ombre de la couronne sur le tronc
    S.add(rect(x - w / 2, 0, w, 300, lineaire([(0, "#000", 0.35), (1, "#000", 0)])))
    vert = feuillage[0][3] if len(feuillage[0]) > 3 else "#40c057"
    for f in feuillage:
        S.add(cercle(f[0], f[1], f[2], volume(f[3] if len(f) > 3 else vert, 0.28, 0.72)))
    for f in clairs:
        S.add(cercle(f[0], f[1], f[2], volume(f[3] if len(f) > 3 else eclaircir(vert, 0.15), 0.3, 0.8)))
    touffe = "q 4 -9 10 -5 q 5 -8 11 -1"
    S.add(chemin(" ".join(f"M {n(fx + dx)} {n(fy + dy)} {touffe}" for fx, fy, rr, *_ in feuillage + clairs
                          for dx, dy in [(-rr * 0.4, rr * 0.1), (rr * 0.2, -rr * 0.3), (rr * 0.1, rr * 0.45)]),
                 stroke=_assombrir(vert, 0.72), sw=3, opacity=0.45))


def pic(x0, y0, xs, ys, x1, y1, c, neige=True):
    """Montagne en relief : versant gauche éclairé, versant droit dans l'ombre,
    arêtes et calotte de neige ombrée elle aussi."""
    m = [poly([(x0, y0), (xs, ys), (x1, y1)], lineaire([(0, eclaircir(c, 0.12)), (1, c)]) if _rvb(c) else c)]
    # versant à l'ombre : de la crête jusqu'à un pied décalé vers la droite
    pied = xs + (x1 - xs) * 0.25
    m.append(poly([(xs, ys), (x1, y1), (pied, y1)], "#1c2a52", opacity=0.2))
    h = y0 - ys
    m.append(chemin(f"M {n(xs)} {n(ys)} L {n(xs - (xs - x0) * 0.18)} {n(ys + h * 0.45)} M {n(xs + (x1 - xs) * 0.12)} {n(ys + h * 0.3)} L {n(xs + (x1 - xs) * 0.3)} {n(ys + h * 0.7)}",
                    stroke=_assombrir(c, 0.75) if _rvb(c) else "#000", sw=2.5, opacity=0.4))
    if neige:
        hh, fx, fx2 = h * 0.28, (xs - x0) * 0.28, (x1 - xs) * 0.28
        m.append(poly([(xs - fx, ys + hh), (xs, ys), (xs + fx2, ys + hh), (xs + fx2 * 0.4, ys + hh * 0.8),
                       (xs, ys + hh * 1.05), (xs - fx * 0.5, ys + hh * 0.8)], "#ffffff"))
        m.append(poly([(xs, ys), (xs + fx2, ys + hh), (xs + fx2 * 0.4, ys + hh * 0.8), (xs + fx2 * 0.1, ys + hh * 0.95)], "#a5b4fc", opacity=0.45))
    return g(m)


def eau(S, y, couleur="#4dabf7", couleur2="#74c0fc", vagues=True):
    S.add(rect(0, y, S.w, S.h - y, lineaire([(0, eclaircir(couleur, 0.25)), (0.3, couleur), (1, _assombrir(couleur, 0.78))]) if _rvb(couleur) else couleur))
    if vagues:
        for k in range(8):
            yy = y + 30 + k * 35
            if yy > S.h:
                break
            x0 = (k % 2) * 60
            d = " ".join(f"M {x0 + i * 120} {yy} q 20 -12 40 0" for i in range(8))
            S.add(chemin(d, stroke=couleur2, sw=5))
        r = random.Random(int(y) + 7)
        reflets = " ".join(f"M {n(r.uniform(0, S.w))} {n(yy)} h {n(r.uniform(10, 26))}"
                           for yy in [r.uniform(y + 12, S.h - 8) for _ in range(14)])
        S.add(chemin(reflets, stroke="#ffffff", sw=3, opacity=0.45))


def pluie(S, nb=60, graine=5, zone=(0, 0, 800, 800), couleur="#4dabf7"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        S.add(trait(x, y, x - 6, y + 22, couleur, 4, opacity=0.8))


def goutte(x, y, s=1.0, couleur="#4dabf7"):
    return place(chemin("M 0 -16 Q 12 0 8 8 Q 0 16 -8 8 Q -12 0 0 -16 Z", couleur), x, y, s)


def flocons(S, nb=40, graine=6, zone=(0, 0, 800, 800), couleur="#ffffff"):
    r = random.Random(graine)
    x0, y0, x1, y1 = zone
    for _ in range(nb):
        S.add(cercle(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(3, 7), couleur, opacity=0.9))


def coeur(x, y, s=1.0, couleur="#ff6b6b", rot=0):
    return place(chemin("M 0 12 C -30 -8 -18 -32 0 -16 C 18 -32 30 -8 0 12 Z", couleur), x, y, s, rot=rot)


def notes(x, y, s=1.0, couleur=ENCRE):
    m = [ellipse(0, 0, 9, 7, couleur, rot=-20), trait(8, -2, 8, -34, couleur, 3.5),
         chemin("M 8 -34 Q 20 -28 20 -16", stroke=couleur, sw=3.5),
         ellipse(34, 10, 9, 7, couleur, rot=-20), ellipse(64, 2, 9, 7, couleur, rot=-20),
         trait(42, 8, 42, -24, couleur, 3.5), trait(72, 0, 72, -32, couleur, 3.5),
         trait(42, -24, 72, -32, couleur, 6)]
    return place(m, x, y, s)


def zzz(x, y, s=1.0, couleur="#5c7cfa"):
    return g([texte(x, y, "z", 26 * s, couleur), texte(x + 24 * s, y - 26 * s, "z", 34 * s, couleur),
              texte(x + 54 * s, y - 60 * s, "Z", 44 * s, couleur)])


def mouvement(x, y, s=1.0, couleur=ENCRE, rot=0, nb=3):
    m = [trait(0, k * 16, -40 + k * 6, k * 16, couleur, 4, opacity=0.5) for k in range(nb)]
    return place(m, x, y, s, rot=rot)


def eclat(x, y, s=1.0, couleur="#ffd43b", nb=8):
    m = []
    for k in range(nb):
        a = k * 2 * math.pi / nb
        m.append(trait(math.cos(a) * 22, math.sin(a) * 22, math.cos(a) * 40, math.sin(a) * 40, couleur, 6))
    return place(m, x, y, s)


def paillettes(x, y, s=1.0, couleur="#ffd43b"):
    """Petites étincelles de joie."""
    m = [etoile5(0, 0, 12, couleur), etoile5(34, -26, 8, couleur), etoile5(-26, -34, 7, couleur)]
    return place(m, x, y, s)


def bulle(x, y, w, h, contenu, taille=36, pointe=None, fill="#ffffff", couleur=ENCRE):
    """Bulle de dialogue centrée en (x, y). `pointe` = (px, py) vers le personnage."""
    m = []
    if pointe:
        px, py = pointe
        m.append(poly([(x - 20, y + h / 2 - 14), (px, py), (x + 20, y + h / 2 - 14)], fill, stroke="#dee2e6", stroke_width=3))
    m.append(rect(x - w / 2, y - h / 2, w, h, fill, rx=min(h / 2, 40), stroke="#dee2e6", stroke_width=3))
    if pointe:
        m.append(poly([(x - 18, y + h / 2 - 16), (px, py), (x + 18, y + h / 2 - 16)], fill))
    lignes = contenu.split("\n")
    for k, ligne in enumerate(lignes):
        yy = y + taille * 0.35 + (k - (len(lignes) - 1) / 2) * taille * 1.15
        m.append(texte(x, yy, ligne, taille, couleur))
    return g(m)


def pensee(x, y, r, contenu="", fill="#ffffff", depuis=None):
    """Bulle de pensée ronde ; `depuis` = (px, py) point d'où partent les petites bulles."""
    m = []
    if depuis:
        px, py = depuis
        for k, rr in enumerate([7, 11, 16]):
            t = (k + 1) / 4
            m.append(cercle(px + (x - px) * t, py + (y - py) * t, rr, fill, stroke="#dee2e6", stroke_width=2))
    for a in range(0, 360, 40):
        m.append(cercle(x + math.cos(math.radians(a)) * r * 0.8, y + math.sin(math.radians(a)) * r * 0.62, r * 0.35, fill))
    m.append(ellipse(x, y, r * 0.95, r * 0.75, fill))
    m.append(contenu)
    return g(m)


# --- Intérieurs -------------------------------------------------------------

def interieur(S, mur="#fff4e6", plancher="#e8c39e", y=560, papier=None, plinthe="#d9a066"):
    S._decor("interieur")
    _cachettes_sol(S, y, 0, plinthe=True)
    S.add(rect(0, 0, S.w, y, mur))
    if papier:
        # chaque livre a son papier peint (MOTIF_PAPIER, choisi par generer.py)
        motif = MOTIF_PAPIER[0]
        motif_mural(S, y, motif, papier, 0.35 if motif == "rayures" else 0.75)
    # pénombre vers le plafond et dans les coins : la pièce a du volume
    S.add(rect(0, 0, S.w, y, lineaire([(0, "#000", 0.09), (0.35, "#000", 0)])))
    S.add(rect(0, 0, S.w, y, lineaire([(0, "#000", 0.08), (0.18, "#000", 0), (0.82, "#000", 0), (1, "#000", 0.08)], 0, 0, 1, 0)))
    S.add(rect(0, y, S.w, S.h - y, lineaire([(0, _assombrir(plancher, 0.86)), (0.45, plancher), (1, eclaircir(plancher, 0.1))])
                                     if _rvb(plancher) else plancher))
    # lames du parquet en perspective : écart croissant vers le lecteur,
    # joints qui convergent vers le fond de la pièce
    h = S.h - y
    for k in range(1, 6):
        yy = y + h * (k / 6) ** 1.35
        S.add(trait(0, n(yy), S.w, n(yy), "#000", 2, opacity=0.06))
    mx, e = S.w / 2, S.w / 800
    d = " ".join(f"M {n(mx + i * 70 * e)} {y} L {n(mx + i * 70 * e * 2.4)} {S.h}" for i in range(-7, 8))
    S.add(chemin(d, stroke="#000", sw=1.5, opacity=0.05))
    S.add(rect(0, y, S.w, 18 * e + 6, lineaire([(0, "#000", 0.16), (1, "#000", 0)])))
    S.add(rect(0, y - 14, S.w, 16, plinthe))
    S.add(rect(0, y - 14, S.w, 3, eclaircir(plinthe, 0.4), opacity=0.8))


def motif_mural(S, y, motif="pois", couleur="#ffc9c9", opacite=0.5):
    """Papier peint à motif sur le mur (de 0 à y) : "pois", "etoiles",
    "fleurs", "losanges" ou "rayures"."""
    e = S.w / 800
    m = []
    pas_ = 64 * e
    for k, yy in enumerate(range(int(pas_ * 0.6), int(y - 20 * e), int(pas_))):
        for xx in range(int(-pas_ / 2 + (k % 2) * pas_ / 2), int(S.w + pas_), int(pas_)):
            if motif == "pois":
                m.append(cercle(xx, yy, 6 * e, couleur))
            elif motif == "etoiles":
                m.append(etoile5(xx, yy, 9 * e, couleur, rot=(k * 17 + xx) % 36))
            elif motif == "fleurs":
                for a in range(5):
                    ang = math.radians(a * 72)
                    m.append(cercle(xx + math.cos(ang) * 7 * e, yy + math.sin(ang) * 7 * e, 5 * e, couleur))
                m.append(cercle(xx, yy, 3.5 * e, _assombrir(couleur, 0.8)))
            elif motif == "losanges":
                m.append(poly([(xx, yy - 14 * e), (xx + 9 * e, yy), (xx, yy + 14 * e), (xx - 9 * e, yy)], couleur))
                m.append(cercle(xx + pas_ / 2, yy + pas_ / 2 - pas_ / 2, 2.5 * e, couleur))
    if motif == "rayures":
        m = [rect(k, 0, 24 * e, y, couleur) for k in range(0, S.w, int(60 * e))]
    S.add(g(sans_relief(m), opacity=opacite))


def piece(S, style="chaumiere", y=560):
    """Pièce complète au caractère marqué, pour ne pas reprendre partout le même
    mur rayé : "chaumiere" (murs chaulés, poutres, larges planches), "manoir"
    (boiseries, papier peint damassé, corniche), "chateau" (pierre de taille,
    tentures), "chambre" (papier peint étoilé) ou "cuisine" (carrelage)."""
    e = S.w / 800
    if style == "chaumiere":
        interieur(S, "#f4e6cc", "#b98552", y, plinthe="#8d5a35")
        r = random.Random(7)
        for _ in range(7):
            px, py = r.uniform(60, S.w - 60), r.uniform(90 * e, y - 80 * e)
            pierre = ellipse(px, py, r.uniform(30, 50) * e, r.uniform(16, 26) * e, "#e3cfac")
            S.add(sans_relief([pierre, pierres(px - 50 * e, py - 26 * e, 100 * e, 52 * e, "#e3cfac", forme=pierre, pas_=int(13 * e) or 1, larg=24 * e, opacite=0.5)]))
        S.add(planches(0, y + 4, S.w, S.h - y, "#b98552", larg=46 * e, vertical=False))
        bois = "#6b4226"
        # poutre du plafond, poteaux d'angle et jambes de force
        S.add(rect(0, 0, S.w, 48 * e, lineaire([(0, _assombrir(bois, 0.8)), (0.5, bois), (1, _assombrir(bois, 0.75))])))
        S.add(planches(0, 0, S.w, 48 * e, bois, larg=24 * e, vertical=False))
        S.add(rect(0, 48 * e, S.w, 14 * e, lineaire([(0, "#000", 0.22), (1, "#000", 0)])))
        for x0, sgn in ((0, 1), (S.w, -1)):
            S.add(rect(x0 - (34 * e if sgn < 0 else 0), 0, 34 * e, y - 12, cylindre(bois, 0.2, 0.7)))
            S.add(poly([(x0 + sgn * 34 * e, 150 * e), (x0 + sgn * 34 * e, 120 * e), (x0 + sgn * 150 * e, 48 * e), (x0 + sgn * 190 * e, 48 * e)], bois))
    elif style == "manoir":
        interieur(S, "#f6e9da", "#a8754a", y, plinthe="#6d4424")
        motif_mural(S, y - 190 * e, "losanges", "#e2c9ad", 0.6)
        bois = "#b07a4f"
        haut = y - 190 * e
        S.add(rect(0, haut, S.w, 190 * e - 14, cylindre(bois, 0.1, 0.85, vertical=True)))
        for k in range(int(S.w / (130 * e)) + 1):
            px = 18 * e + k * 130 * e
            S.add(rect(px, haut + 24 * e, 100 * e, 190 * e - 66 * e, _assombrir(bois, 0.9), rx=4 * e,
                       stroke=_assombrir(bois, 0.7), stroke_width=3 * e))
            S.add(trait(px + 4 * e, haut + 28 * e, px + 96 * e, haut + 28 * e, eclaircir(bois, 0.35), 2 * e, opacity=0.7))
        S.add(rect(0, haut - 10 * e, S.w, 14 * e, eclaircir(bois, 0.15)))
        S.add(rect(0, haut + 4 * e, S.w, 8 * e, lineaire([(0, "#000", 0.2), (1, "#000", 0)])))
        S.add(rect(0, 0, S.w, 26 * e, lineaire([(0, "#fff8f0"), (1, "#e9d5bd")])))
        S.add(rect(0, 26 * e, S.w, 12 * e, lineaire([(0, "#000", 0.14), (1, "#000", 0)])))
    elif style == "chateau":
        interieur(S, "#ddd3c6", "#a39486", y, plinthe="#7d7064")
        S.add(pierres(0, 0, S.w, y - 14, "#ddd3c6", pas_=int(38 * e), larg=66 * e, opacite=0.45))
        S.add(pierres(0, y + 4, S.w, S.h - y, "#a39486", pas_=int(30 * e), larg=90 * e, opacite=0.3))
        for x0 in (40 * e, S.w - 130 * e):
            tenture = chemin(f"M {n(x0)} {n(30 * e)} H {n(x0 + 90 * e)} V {n(y - 190 * e)} L {n(x0 + 45 * e)} {n(y - 160 * e)} L {n(x0)} {n(y - 190 * e)} Z",
                             cylindre("#c92a2a", 0.2, 0.75))
            S.add(rect(x0 - 12 * e, 22 * e, 114 * e, 10 * e, "#8d5524", rx=5 * e))
            S.add(tenture)
            S.add(chemin(f"M {n(x0 + 8 * e)} {n(34 * e)} V {n(y - 196 * e)} L {n(x0 + 45 * e)} {n(y - 170 * e)} L {n(x0 + 82 * e)} {n(y - 196 * e)} V {n(34 * e)}",
                         stroke="#fcc419", sw=4 * e))
            S.add(couronne_simple(x0 + 45 * e, 150 * e, 1.1 * e))
    elif style == "chambre":
        interieur(S, "#e7f5ff", "#d9a066", y, plinthe="#c08552")
        motif_mural(S, y, "etoiles", "#a5d8ff", 0.7)
    elif style == "cuisine":
        interieur(S, "#fff9db", "#ced4da", y, plinthe="#868e96")
        haut = y - 200 * e
        S.add(rect(0, haut, S.w, 200 * e - 14, "#f8f9fa"))
        pas_ = 40 * e
        d = " ".join(f"M 0 {n(haut + k * pas_)} H {S.w}" for k in range(int(200 * e / pas_) + 1))
        d += " " + " ".join(f"M {n(k * pas_)} {n(haut)} V {n(y - 14)}" for k in range(int(S.w / pas_) + 1))
        S.add(chemin(d, stroke="#a5d8ff", sw=2.5 * e))
        S.add(rect(0, haut - 8 * e, S.w, 10 * e, "#74c0fc"))
    else:
        raise ValueError(f"style de pièce inconnu : {style}")


def couronne_simple(x, y, s=1.0, couleur="#fcc419"):
    """Petite couronne brodée (blason d'une tenture)."""
    return place([poly([(-20, 10), (-22, -12), (-10, 0), (0, -16), (10, 0), (22, -12), (20, 10)], couleur),
                  cercle(0, -16, 3.5, couleur), cercle(-22, -12, 3, couleur), cercle(22, -12, 3, couleur)], x, y, s)


def lueur(x, y, r, couleur="#ffd43b", force=0.55, ry=None):
    """Halo d'une source de lumière (lampe, bougie, fenêtre éclairée) fondu en
    « superposition » (screen) : il éclaire ce qui l'entoure sans le cacher."""
    return ellipse(x, y, r, ry or r, radial([(0, couleur, force), (0.4, couleur, force * 0.5), (1, couleur, 0)]),
                   style="mix-blend-mode:screen")


def fenetre(x, y, w=160, h=150, dehors="#a5d8ff", cadre="#ffffff", nuit_=False, rideaux=None, contenu=""):
    m = [rect(x - 8, y - 8, w + 16, h + 16, cadre, rx=6), rect(x, y, w, h, dehors)]
    if contenu:
        cid = uid("c")
        m.append(el("clipPath", rect(x, y, w, h, "#000"), id=cid))
        m.append(g(contenu, clip_path=f"url(#{cid})"))
    if nuit_:
        m.append(cercle(x + w * 0.7, y + h * 0.3, 16, "#fff3bf"))
        m += [cercle(x + w * 0.2, y + h * 0.25, 2.5, "#fff"), cercle(x + w * 0.4, y + h * 0.6, 2, "#fff"), cercle(x + w * 0.85, y + h * 0.75, 2.5, "#fff")]
    # profondeur de l'embrasure et reflets sur la vitre
    m.append(poly([(x, y), (x + w, y), (x + w - 10, y + 10), (x + 10, y + 10), (x + 10, y + h), (x, y + h)], "#000", opacity=0.16))
    m.append(poly([(x + w * 0.12, y + h), (x + w * 0.42, y), (x + w * 0.56, y), (x + w * 0.26, y + h)], "#fff", opacity=0.16))
    m.append(poly([(x + w * 0.62, y + h), (x + w * 0.82, y), (x + w * 0.87, y), (x + w * 0.67, y + h)], "#fff", opacity=0.12))
    m += [rect(x + w / 2 - 4, y, 8, h, cadre), rect(x, y + h / 2 - 4, w, 8, cadre)]
    m.append(rect(x - 8, y - 8, w + 16, h + 16, "none", rx=6, stroke=_assombrir(cadre, 0.82), stroke_width=2))
    # appui de fenêtre et son ombre
    m += [rect(x - 16, y + h + 4, w + 32, 11, cadre, rx=3, stroke=_assombrir(cadre, 0.82), stroke_width=1.5),
          rect(x - 12, y + h + 15, w + 24, 7, "#000", opacity=0.1, rx=3)]
    if rideaux:
        m.append(chemin(f"M {x - 20} {y - 14} L {x + 30} {y - 14} Q {x + 10} {y + h / 2} {x + 30} {y + h + 20} L {x - 20} {y + h + 20} Z", cylindre(rideaux, 0.25, 0.8)))
        m.append(chemin(f"M {x + w + 20} {y - 14} L {x + w - 30} {y - 14} Q {x + w - 10} {y + h / 2} {x + w - 30} {y + h + 20} L {x + w + 20} {y + h + 20} Z", cylindre(rideaux, 0.25, 0.8)))
        fonce = _assombrir(rideaux, 0.75)
        m.append(chemin(f"M {x - 6} {y - 10} Q {x - 10} {y + h / 2} {x - 4} {y + h + 18} M {x + 10} {y - 10} Q {x + 2} {y + h / 2} {x + 12} {y + h + 18} "
                        f"M {x + w + 6} {y - 10} Q {x + w + 10} {y + h / 2} {x + w + 4} {y + h + 18} M {x + w - 10} {y - 10} Q {x + w - 2} {y + h / 2} {x + w - 12} {y + h + 18}",
                        stroke=fonce, sw=2.5, opacity=0.5))
        m.append(rect(x - 30, y - 22, w + 60, 12, cylindre("#adb5bd", 0.4, 0.75, vertical=True), rx=6))
    return g(m)


def tapis(x, y, rx=220, ry=45, couleur="#ffc9c9", bord="#ff8787"):
    return g([ellipse(x, y, rx, ry, bord), ellipse(x, y, rx - 14, ry - 8, couleur)])


def table(x, y, w=260, h=130, couleur="#c68642", nappe=None):
    pied = cylindre(couleur, 0.2, 0.72)
    m = [ellipse(x, y, w * 0.55, 10, "#000", opacity=0.1),
         rect(x - w / 2 + 14, y - h, 16, h, pied), rect(x + w / 2 - 30, y - h, 16, h, pied),
         rect(x - w / 2 + 6, y - h + 4, w - 12, 10, "#000", opacity=0.15),
         rect(x - w / 2, y - h - 18, w, 22, lineaire([(0, eclaircir(couleur, 0.3)), (0.35, couleur), (1, _assombrir(couleur, 0.75))]) if _rvb(couleur) else couleur, rx=6),
         trait(x - w / 2 + 8, y - h - 15, x + w / 2 - 8, y - h - 15, eclaircir(couleur, 0.5), 2, opacity=0.7)]
    if nappe:
        m.append(chemin(f"M {x - w / 2 - 10} {y - h - 20} L {x + w / 2 + 10} {y - h - 20} L {x + w / 2 + 16} {y - h + 30} L {x - w / 2 - 16} {y - h + 30} Z",
                        lineaire([(0, nappe), (1, _assombrir(nappe, 0.88))]) if _rvb(nappe) else nappe))
        m.append(chemin(" ".join(f"M {n(x + k * w / 8)} {y - h - 2} l {n(k * 1.5)} 30" for k in range(-3, 4)), stroke=_assombrir(nappe, 0.8), sw=2, opacity=0.5))
    return g(m)


def lit(x, y, w=360, couleur="#74c0fc", couverture="#4dabf7", bois="#c68642", motif=None):
    """Lit vu de face, (x, y) = milieu du pied du lit au sol."""
    b = cylindre(bois, 0.25, 0.72)
    m = [ellipse(x, y, w * 0.58, 12, "#000", opacity=0.1),
         rect(x - w / 2 - 14, y - 230, 28, 230, b, rx=10), rect(x + w / 2 - 14, y - 170, 28, 170, b, rx=10),
         rect(x - w / 2, y - 110, w, 60, "#fff", rx=10),
         rect(x - w / 2 + 20, y - 150, 110, 50, volume("#ffffff", 0, 0.88), rx=22, stroke="#e9ecef", stroke_width=3),
         chemin(f"M {x - w / 2 + 50} {y - 128} q 20 6 40 0", stroke="#dee2e6", sw=2.5),
         rect(x - w / 2 + 110, y - 125, w - 110, 85, lineaire([(0, eclaircir(couverture, 0.25)), (0.4, couverture), (1, _assombrir(couverture, 0.8))]) if _rvb(couverture) else couverture, rx=18),
         chemin(f"M {x - w / 2 + 160} {y - 118} q 10 30 0 70 M {x + 40} {y - 120} q -8 34 4 72 M {x + w / 2 - 50} {y - 118} q 10 30 0 70",
                stroke=_assombrir(couverture, 0.78), sw=2.5, opacity=0.6),
         rect(x - w / 2 + 110, y - 125, w - 110, 10, "#fff", rx=5, opacity=0.35),
         rect(x - w / 2, y - 50, w, 30, lineaire([(0, eclaircir(bois, 0.2)), (1, _assombrir(bois, 0.75))]) if _rvb(bois) else bois, rx=6)]
    for bx in (x - w / 2, x + w / 2):
        m.append(cercle(bx, y - 232 if bx < x else y - 172, 16, volume(bois, 0.35, 0.72)))
    return g(m)


def lampe(x, y, s=1.0, abat="#ffd8a8", allumee=True, halo=True):
    if allumee and halo:
        lumiere_auto(x, y - 120 * s, 190 * s, "#ffd43b", 0.6)
    m = []
    if allumee:
        m.append(cercle(0, -130, 120, radial([(0, "#fff3bf", 0.55), (1, "#fff3bf", 0)])))
        m.append(poly([(-40, -150), (40, -150), (110, 0), (-110, 0)], lineaire([(0, "#fff3bf", 0.5), (1, "#fff3bf", 0.1)])))
    m += [ellipse(0, 0, 40, 6, "#000", opacity=0.12), rect(-30, -10, 60, 10, cylindre("#868e96", 0.4, 0.7), rx=4), rect(-4, -120, 8, 110, cylindre("#868e96", 0.4, 0.7)),
          poly([(-40, -150), (40, -150), (55, -110), (-55, -110)], cylindre(abat, 0.3, 0.8)),
          ellipse(0, -110, 55, 5, _assombrir(abat, 0.8))]
    return place(m, x, y, s)


def etagere(x, y, w=220, couleur="#c68642", objets=None):
    m = [rect(x - w / 2, y, w, 14, couleur, rx=4)]
    if objets:
        m.append(objets)
    return g(m)


def livres_pile(x, y, s=1.0):
    cols = ["#ff6b6b", "#4dabf7", "#ffd43b", "#69db7c"]
    m = [rect(-30 + (k % 2) * 6, -18 * (k + 1), 64, 16, c, rx=3) for k, c in enumerate(cols)]
    return place(m, x, y, s)


def cadre_mur(x, y, w=110, h=90, contenu_couleur="#b2f2bb"):
    return g([rect(x, y, w, h, "#c68642", rx=4), rect(x + 10, y + 10, w - 20, h - 20, contenu_couleur),
              chemin(f"M {x + 10} {y + h - 10} L {x + w * 0.4} {y + h * 0.45} L {x + w * 0.6} {y + h * 0.7} L {x + w * 0.75} {y + h * 0.5} L {x + w - 10} {y + h - 10} Z", "#51cf66")])


def horloge(x, y, r=40, heure=3, minute=0, couleur="#fff", bord="#f08c00"):
    ah = math.radians((heure % 12 + minute / 60) * 30 - 90)
    am = math.radians(minute * 6 - 90)
    m = [cercle(x, y, r + 6, bord), cercle(x, y, r, couleur)]
    for k in range(12):
        a = math.radians(k * 30)
        m.append(cercle(x + math.cos(a) * r * 0.8, y + math.sin(a) * r * 0.8, 2.5, ENCRE))
    m.append(trait(x, y, x + math.cos(ah) * r * 0.5, y + math.sin(ah) * r * 0.5, ENCRE, 5))
    m.append(trait(x, y, x + math.cos(am) * r * 0.75, y + math.sin(am) * r * 0.75, ENCRE, 3.5))
    m.append(cercle(x, y, 4, ENCRE))
    return g(m)


def porte(x, y, w=150, h=300, couleur="#b5835a", ouverte=False):
    m = [rect(x - w / 2 - 10, y - h - 10, w + 20, h + 10, "#e9ecef"),
         rect(x - w / 2 - 10, y - h - 10, w + 20, h + 10, "none", stroke="#ced4da", stroke_width=2)]
    if ouverte:
        m.append(rect(x - w / 2, y - h, w, h, lineaire([(0, "#212529"), (1, "#495057")])))
        m.append(poly([(x - w / 2, y - h), (x - w / 2 - 40, y - h + 20), (x - w / 2 - 40, y - 10), (x - w / 2, y)], cylindre(couleur, 0.15, 0.7)))
    else:
        m += [rect(x - w / 2, y - h, w, h, cylindre(couleur, 0.15, 0.8)),
              rect(x - w / 2, y - h, w, 8, "#000", opacity=0.12)]
        for py, ph in ((y - h + 20, h * 0.35), (y - h * 0.5, h * 0.4)):
            px, pw = x - w / 2 + 18, w - 36
            m += [rect(px, py, pw, ph, "#000", opacity=0.08, rx=6),
                  chemin(f"M {n(px + 3)} {n(py + ph - 3)} V {n(py + 3)} H {n(px + pw - 3)}", stroke="#000", sw=3, opacity=0.14),
                  chemin(f"M {n(px + 3)} {n(py + ph - 2)} H {n(px + pw - 2)} V {n(py + 3)}", stroke="#fff", sw=3, opacity=0.25)]
        m += [cercle(x + w / 2 - 22, y - h / 2, 8, volume("#ffd43b", 0.6, 0.65)), cercle(x + w / 2 - 24, y - h / 2 - 2.5, 2.5, "#fff")]
    return g(m)


# --- Textures de construction -------------------------------------------------
# Pour les bâtiments dessinés dans les scripts des livres : chaque fonction
# renvoie un calque à poser par-dessus une forme déjà remplie, découpé à sa
# silhouette quand `forme` (élément SVG) est donné.

def _decoupe(contenu, forme):
    if not forme:
        return contenu
    cid = uid("k")
    return el("clipPath", forme, id=cid) + g(contenu, clip_path=f"url(#{cid})")


def briques(x, y, w, h, c, forme=None, hb=16, lb=34):
    """Joints de briques décalés d'un rang à l'autre et reflet sur chaque rang."""
    joints, reflets = [], []
    for k, yy in enumerate(range(int(y), int(y + h), hb)):
        joints.append(f"M {n(x)} {yy} h {n(w)}")
        reflets.append(f"M {n(x)} {yy + 2.5} h {n(w)}")
        xx = x + (k % 2) * lb / 2
        while xx < x + w:
            joints.append(f"M {n(xx)} {yy} v {hb}")
            xx += lb
    return _decoupe(chemin(" ".join(reflets), stroke=eclaircir(c, 0.4), sw=1.5, opacity=0.45)
                    + chemin(" ".join(joints), stroke=_assombrir(c, 0.6), sw=2, opacity=0.6), forme)


def planches(x, y, w, h, c, forme=None, larg=22, vertical=True):
    """Planches de bois : joints, veinures et nœuds."""
    r = random.Random(int(x * 7 + y * 3 + w))
    fonce = _assombrir(c, 0.62)
    joints, veines = [], []
    if vertical:
        xx = x
        while xx < x + w:
            joints.append(f"M {n(xx)} {n(y)} v {n(h)}")
            for _ in range(2):
                vy = r.uniform(y, y + h * 0.8)
                veines.append(f"M {n(xx + r.uniform(5, larg - 5))} {n(vy)} q 3 {n(h * 0.08)} 0 {n(h * 0.16)}")
            xx += larg
    else:
        yy = y
        while yy < y + h:
            joints.append(f"M {n(x)} {n(yy)} h {n(w)}")
            for _ in range(2):
                vx = r.uniform(x, x + w * 0.8)
                veines.append(f"M {n(vx)} {n(yy + r.uniform(5, larg - 5))} q {n(w * 0.08)} 3 {n(w * 0.16)} 0")
            yy += larg
    return _decoupe(chemin(" ".join(joints), stroke=fonce, sw=2.5, opacity=0.6)
                    + chemin(" ".join(veines), stroke=fonce, sw=1.5, opacity=0.35), forme)


def chaume(x, y, w, h, c, forme=None, graine=1):
    """Paille ou chaume : brins obliques serrés, plus sombres en bas de chaque rang."""
    r = random.Random(graine)
    clairs, fonces = [], []
    for yy in range(int(y), int(y + h), 14):
        for _ in range(int(w / 9)):
            xx = r.uniform(x, x + w)
            L = r.uniform(12, 22)
            (clairs if r.random() < 0.5 else fonces).append(f"M {n(xx)} {yy} l {n(r.uniform(-3, 3))} {n(L)}")
    return _decoupe(chemin(" ".join(clairs), stroke=eclaircir(c, 0.45), sw=2, opacity=0.7)
                    + chemin(" ".join(fonces), stroke=_assombrir(c, 0.7), sw=2, opacity=0.6), forme)


def tuiles(x, y, w, h, c, forme=None, pas_=15):
    """Rangs de tuiles arrondies."""
    d = " ".join(f"M {n(x - (k % 2) * pas_ / 2)} {yy} " + " ".join(f"q {n(pas_ / 2)} {n(pas_ * 0.6)} {pas_} 0" for _ in range(int(w / pas_) + 2))
                 for k, yy in enumerate(range(int(y + pas_), int(y + h + pas_), pas_)))
    return _decoupe(chemin(d, stroke=_assombrir(c, 0.68), sw=2, opacity=0.55), forme)


def pierres(x, y, w, h, c, forme=None, pas_=22, larg=34, opacite=0.32):
    """Appareil de pierres : assises horizontales et joints décalés."""
    d = []
    for k, yy in enumerate(range(int(y + pas_), int(y + h), pas_)):
        d.append(f"M {n(x)} {yy} H {n(x + w)}")
        xx = x + (k % 2) * larg / 2 + larg / 2
        while xx < x + w - 4:
            d.append(f"M {n(xx)} {yy} v {-pas_}")
            xx += larg
    return _decoupe(chemin(" ".join(d), stroke=_assombrir(c, 0.72), sw=1.5, opacity=opacite), forme)


def ombre_avancee(x, y, w, h=16, opacite=0.18):
    """Ombre portée sous un toit, une corniche ou un balcon (bord haut en y)."""
    return rect(x, y, w, h, lineaire([(0, "#000", opacite), (1, "#000", 0)]))


# ---------------------------------------------------------------------------
# Personnages
# ---------------------------------------------------------------------------
# Tous les personnages « debout » sont dessinés de face, les pieds en (0, 0),
# la tête vers y = -150 (rayon 55). Hauteur totale ≈ 210 à l'échelle 1.

ESPECES = {
    "ours": dict(c="#b07a4f", c2="#ecd0ae", pieds="#8f5f3a", ventre=True),
    "lapin": dict(c="#f1f3f5", c2="#ffffff", pieds="#dee2e6", ventre=True, interieur="#ffc9c9"),
    "souris": dict(c="#ced4da", c2="#f1f3f5", pieds="#ffa8a8", ventre=True, interieur="#ffc9c9"),
    "renard": dict(c="#f76707", c2="#fff4e6", pieds="#5c3d2e", ventre=True),
    "chat": dict(c="#ffa94d", c2="#fff4e6", pieds="#ffa94d", ventre=True, interieur="#ffc9c9"),
    "chien": dict(c="#e3b57a", c2="#fff4e6", pieds="#e3b57a", ventre=True, oreilles="#a0693a"),
    "cochon": dict(c="#ffc9d6", c2="#ffe3ea", pieds="#f7a1b5", ventre=True, groin="#f78fa7"),
    "mouton": dict(c="#f8f9fa", c2="#f1dcc3", pieds="#495057", ventre=False),
    "herisson": dict(c="#d9a57b", c2="#f3dcc3", pieds="#b98556", ventre=True, piquants="#7a5230"),
    "grenouille": dict(c="#69db7c", c2="#d8f5a2", pieds="#51cf66", ventre=True),
    "fourmi": dict(c="#9c3d2e", c2="#c9604e", pieds="#6d2a1f", ventre=False),
    "elephant": dict(c="#adb5bd", c2="#ced4da", pieds="#868e96", ventre=True, interieur="#ffc9c9"),
    "castor": dict(c="#8f5b34", c2="#d9b48f", pieds="#5c3a1e", ventre=True),
    "panda": dict(c="#ffffff", c2="#ffffff", pieds="#343a40", ventre=False),
    "ecureuil": dict(c="#d9692b", c2="#fff0dc", pieds="#b4531c", ventre=True, interieur="#ffd8a8"),
    # animaux des fables
    "loup": dict(c="#868e96", c2="#f1f3f5", pieds="#495057", ventre=True),
    "lion": dict(c="#fcc419", c2="#fff3bf", pieds="#e8a200", ventre=True, criniere="#e8590c"),
    "lievre": dict(c="#c49a6c", c2="#f6e7d3", pieds="#9c7650", ventre=True, interieur="#ffc9c9"),
    "rat": dict(c="#a39382", c2="#e9e1d8", pieds="#ffa8a8", ventre=True, interieur="#ffc9c9"),
    "ane": dict(c="#9aa1a8", c2="#e9ecef", pieds="#495057", ventre=True, interieur="#ffe3e3"),
    "chevre": dict(c="#e9d8c4", c2="#fff9f0", pieds="#6d5a47", ventre=True, interieur="#ffc9c9", cornes="#a68a64"),
    "boeuf": dict(c="#a0693a", c2="#f3dcc3", pieds="#6d4424", ventre=True, cornes="#fff4e6", mufle="#ffc9d6"),
    "cigale": dict(c="#82c91e", c2="#d8f5a2", pieds="#5c940d", ventre=True),
    "cerf": dict(c="#b5753c", c2="#f6e2c8", pieds="#6d4424", ventre=True, interieur="#ffd8a8", bois="#8d5524"),
    "singe": dict(c="#8d5b34", c2="#f3d9b1", pieds="#6d4424", ventre=True, interieur="#e8b98a"),
}

# Position des mains (gauche, droite) pour chaque pose, et coudes éventuels.
POSES = {
    "bas": ((-52, -40), (52, -40)),
    "haut": ((-70, -165), (70, -165)),
    "salut": ((-52, -40), (72, -160)),
    "porte": ((-26, -74), (26, -74)),
    "large": ((-64, -70), (64, -70)),
    "guidon": ((62, -40), (84, -34)),
    "tient": ((-52, -40), (68, -146)),
    "calin": ((-30, -46), (30, -46)),
    "ouverts": ((-88, -108), (88, -108)),
    "donne": ((-52, -40), (84, -92)),
    "donne2": ((58, -86), (92, -92)),
    "montre": ((-52, -40), (86, -130)),
    "hanches": ((-40, -50), (40, -50)),
    "croises": ((26, -72), (-26, -80)),
    "joues": ((-44, -128), (44, -128)),
    "yeux": ((-20, -152), (20, -152)),
    "bouche": ((-8, -118), (10, -120)),
    "pense": ((-52, -40), (18, -112)),
    "tete": ((-52, -196), (52, -196)),
    "course": ((-66, -112), (56, -44)),
    "tire": ((72, -70), (92, -64)),
    "poing": ((-60, -150), (60, -150)),
    # poses plus vivantes
    "danse": ((-84, -150), (70, -62)),
    "applaudit": ((-8, -98), (12, -102)),
    "victoire": ((-52, -40), (54, -186)),
    "epaules": ((-82, -112), (82, -112)),
    "etire": ((-58, -214), (58, -214)),
    "coucou": ((-52, -40), (82, -176)),
    "marche": ((-58, -56), (50, -44)),
    "chut": ((-52, -40), (4, -118)),
    # poses dynamiques : course rapide, saut, lancer, doigt tendu, poussée, équilibre
    "court": ((-48, -122), (58, -56)),
    "saute": ((-90, -196), (90, -196)),
    "lance": ((-74, -100), (80, -202)),
    "designe": ((-40, -50), (106, -122)),
    "pousse": ((60, -100), (90, -114)),
    "equilibre": ((-104, -124), (102, -100)),
    # poses d'échange : tenir la main du voisin, l'entourer de son bras, tendre
    # les bras vers lui, joindre les mains, ramasser, lever le doigt
    "main": ((-52, -40), (88, -58)),
    "epaule": ((-52, -40), (116, -116)),
    "tend": ((40, -94), (96, -104)),
    "mains_jointes": ((-7, -94), (7, -94)),
    "ramasse": ((-30, -22), (36, -18)),
    "leve_doigt": ((-52, -40), (52, -216)),
}
COUDES = {
    "haut": ((-84, -124), (84, -124)),
    "course": ((-84, -94), (70, -82)),
    "hanches": ((-66, -74), (66, -74)),
    "tete": ((-78, -140), (78, -140)),
    "poing": ((-66, -104), (66, -104)),
    "calin": ((-72, -84), (72, -84)),
    "danse": ((-76, -100), (78, -84)),
    "applaudit": ((-66, -66), (66, -70)),
    "victoire": ((-60, -70), (78, -118)),
    "epaules": ((-60, -64), (60, -64)),
    "etire": ((-70, -150), (70, -150)),
    "coucou": ((-60, -70), (86, -112)),
    "chut": ((-60, -70), (44, -72)),
    "court": ((-78, -96), (64, -86)),
    "saute": ((-76, -150), (76, -150)),
    "lance": ((-66, -76), (100, -150)),
    "designe": ((-66, -74), None),
    "pousse": ((14, -76), (58, -80)),
    "equilibre": ((-70, -108), (70, -96)),
    "main": (None, (62, -74)),
    "epaule": (None, (72, -128)),
    "tend": ((2, -76), (62, -98)),
    "mains_jointes": ((-50, -66), (50, -66)),
    "ramasse": ((-60, -58), (62, -56)),
    "leve_doigt": (None, (68, -150)),
}
DEVANT_VISAGE = {"joues", "yeux", "bouche", "pense", "tete", "chut"}
# Pas des pieds associé par défaut à une pose de bras.
PAS_POSE = {"course": "court", "marche": "marche", "danse": "pointe", "victoire": "saute",
            "court": "court", "saute": "saute", "lance": "marche", "pousse": "marche", "equilibre": "pointe"}
# Inclinaison de la tête (en degrés) selon l'expression : un peu de vie.
# Inclinaison du corps (en degrés) selon la pose : on se penche en avant pour
# courir, en arrière pour tirer, vers le bras levé pour danser.
INCLINE = {"course": 11, "marche": 3, "danse": -5, "victoire": -3, "tire": -6, "montre": 2, "salut": -2,
           "court": 13, "lance": -7, "designe": 3, "pousse": 11, "equilibre": -6,
           "main": 3, "epaule": 6, "tend": 7, "ramasse": 8, "leve_doigt": -2}
PENCHE = {"timide": -7, "triste": 6, "pleure": 6, "inquiet": -5, "malin": 6, "content": 4,
          "chante": -5, "miam": 4, "oups": -6, "degoute": -6, "fier": -3, "dort": 7}

EXPRESSIONS = {
    # yeux, bouche, sourcils
    "sourire": ("normal", "sourire", None),
    "content": ("heureux", "sourire", None),
    "rire": ("heureux", "ouverte", None),
    "joie": ("normal", "ouverte", None),
    "surpris": ("grand", "o", "hauts"),
    "triste": ("normal", "triste", "tristes"),
    "pleure": ("fermes", "triste", "tristes"),
    "fache": ("normal", "boude", "faches"),
    "furieux": ("normal", "crie", "faches"),
    "inquiet": ("normal", "vague", "tristes"),
    "timide": ("bas", "petit_sourire", None),
    "dort": ("fermes", "petite", None),
    "neutre": ("normal", "ligne", None),
    "miam": ("heureux", "langue", None),
    "souffle": ("fermes", "souffle", None),
    "concentre": ("normal", "langue_cote", "plats"),
    "malin": ("normal", "coin", "malin"),
    "oups": ("grand", "grimace", "tristes"),
    "chante": ("heureux", "o", None),
    "bouche_bee": ("grand", "ouverte", "hauts"),
    "baille": ("fermes", "baille", None),
    "fier": ("heureux", "sourire", "hauts"),
    "degoute": ("fermes", "vague", "faches"),
}


def oeil(x, y, style="normal", regard=(0, 0), sclere=False, taille=1.0):
    dx, dy = regard
    t = taille
    if style == "heureux":
        return chemin(f"M {n(x - 8 * t)} {n(y + 3)} Q {n(x)} {n(y - 9 * t)} {n(x + 8 * t)} {n(y + 3)}", stroke=ENCRE, sw=3.8 * t)
    if style == "fermes":
        return chemin(f"M {n(x - 8 * t)} {n(y - 1)} Q {n(x)} {n(y + 7 * t)} {n(x + 8 * t)} {n(y - 1)}", stroke=ENCRE, sw=3.8 * t)
    if style == "bas":
        dy = dy + 1.2
    k = 1.3 if style == "grand" else 1.0
    m = []
    if sclere:
        m.append(cercle(x, y, 12 * t * k, "#fff", stroke=ENCRE, stroke_width=1.5))
        m.append(cercle(x + dx * 4, y + dy * 4, 6.5 * t * k, ENCRE))
        m.append(cercle(x + dx * 4 + 2, y + dy * 4 - 2.5, 2 * t, "#fff"))
    else:
        m.append(ellipse(x + dx * 3, y + dy * 3, 6.5 * t * k, 8.5 * t * k, ENCRE))
        m.append(cercle(x + dx * 3 + 2, y + dy * 3 - 3, 2.2 * t * k, "#fff"))
        m.append(cercle(x + dx * 3 - 2.2 * t, y + dy * 3 + 3.6 * t, 1.1 * t * k, "#fff", opacity=0.75))
    return "".join(m)


def yeux_trois_quarts(ex, ey, style, regard, sclere=False, tourne=0, taille=1.0):
    """Les deux yeux ; en trois quarts (tourne ≠ 0), l'œil le plus loin est un
    peu plus petit et plus proche du nez."""
    k = min(abs(tourne) / 10, 1) * 0.16
    loin = -1 if tourne > 0 else 1
    m = []
    for sgn in (-1, 1):
        f = 1 - k if (tourne and sgn == loin) else 1
        m.append(oeil(sgn * ex * f, ey, style, regard, sclere, taille * f))
    return "".join(m)


def bouche(x, y, style="sourire", l=1.0):
    L = l
    if style == "sourire":
        return chemin(f"M {n(x - 12 * L)} {y} Q {x} {y + 12} {n(x + 12 * L)} {y}", stroke=ENCRE, sw=3.8)
    if style == "petit_sourire":
        return chemin(f"M {n(x - 7 * L)} {y + 1} Q {x} {y + 7} {n(x + 7 * L)} {y + 1}", stroke=ENCRE, sw=3.5)
    if style == "ouverte":
        return (chemin(f"M {n(x - 13 * L)} {y - 2} Q {x} {y + 22} {n(x + 13 * L)} {y - 2} Z", ROUGE_BOUCHE, stroke=ENCRE, sw=3)
                + ellipse(x, y + 9, 6 * L, 3.5, "#ff8787"))
    if style == "triste":
        return chemin(f"M {n(x - 11 * L)} {y + 7} Q {x} {y - 4} {n(x + 11 * L)} {y + 7}", stroke=ENCRE, sw=3.8)
    if style == "boude":
        return chemin(f"M {n(x - 11 * L)} {y + 6} Q {x} {y - 1} {n(x + 11 * L)} {y + 6}", stroke=ENCRE, sw=4.2)
    if style == "o":
        return ellipse(x, y + 4, 5.5, 7.5, ENCRE)
    if style == "souffle":
        return cercle(x, y + 3, 5, ENCRE)
    if style == "vague":
        return chemin(f"M {n(x - 12 * L)} {y + 3} q {n(4 * L)} -5 {n(8 * L)} 0 q {n(4 * L)} 5 {n(8 * L)} 0 q {n(4 * L)} -5 {n(8 * L)} 0", stroke=ENCRE, sw=3.5)
    if style == "crie":
        return (chemin(f"M {n(x - 15 * L)} {y - 3} L {n(x + 15 * L)} {y - 3} Q {n(x + 12 * L)} {y + 18} {x} {y + 18} Q {n(x - 12 * L)} {y + 18} {n(x - 15 * L)} {y - 3} Z", ROUGE_BOUCHE, stroke=ENCRE, sw=3)
                + rect(x - 11 * L, y - 3, 22 * L, 5, "#fff"))
    if style == "ligne":
        return trait(x - 8 * L, y + 3, x + 8 * L, y + 3, ENCRE, 3.8)
    if style == "petite":
        return ellipse(x, y + 3, 3.5, 4.5, ENCRE)
    if style == "langue":
        return (chemin(f"M {n(x - 12 * L)} {y} Q {x} {y + 12} {n(x + 12 * L)} {y}", stroke=ENCRE, sw=3.8)
                + ellipse(x + 5, y + 9, 5.5, 7, "#ff8787", stroke=ENCRE, stroke_width=1.5))
    if style == "langue_cote":
        return (trait(x - 9 * L, y + 3, x + 7 * L, y + 3, ENCRE, 3.8)
                + ellipse(x + 9, y + 7, 5, 6, "#ff8787", stroke=ENCRE, stroke_width=1.5))
    if style == "coin":
        return chemin(f"M {n(x - 10 * L)} {y + 3} Q {n(x + 2 * L)} {y + 9} {n(x + 13 * L)} {y - 3}", stroke=ENCRE, sw=3.8)
    if style == "grimace":
        return (rect(x - 14 * L, y - 3, 28 * L, 12, "#fff", rx=4, stroke=ENCRE, stroke_width=2.5)
                + trait(x - 13 * L, y + 3, x + 13 * L, y + 3, ENCRE, 1.5))
    if style == "baille":
        return ellipse(x, y + 7, 10, 14, ROUGE_BOUCHE, stroke=ENCRE, stroke_width=3)
    return ""


def sourcils(ex, ey, style):
    """ex = écart horizontal des yeux, ey = hauteur des yeux."""
    if not style:
        return ""
    y = ey - 20
    m = []
    for sgn in (-1, 1):
        xo, xi = sgn * (ex + 10), sgn * (ex - 9)
        if style == "tristes":
            m.append(trait(xo, y + 4, xi, y - 4, ENCRE, 3.5))
        elif style == "faches":
            m.append(trait(xo, y - 5, xi, y + 5, ENCRE, 4.5))
        elif style == "hauts":
            m.append(chemin(f"M {xo} {y - 2} Q {n((xo + xi) / 2)} {y - 11} {xi} {y - 2}", stroke=ENCRE, sw=3.5))
        elif style == "plats":
            m.append(trait(xo, y, xi, y, ENCRE, 3.5))
        elif style == "malin":
            if sgn < 0:
                m.append(trait(xo, y + 2, xi, y + 2, ENCRE, 3.5))
            else:
                m.append(chemin(f"M {xi} {y - 2} Q {n((xo + xi) / 2)} {y - 12} {xo} {y - 4}", stroke=ENCRE, sw=3.5))
    return "".join(m)


def _controle(x0, y0, main, coude):
    """Point de contrôle de la courbe d'un bras (épaule → main)."""
    if coude:
        return coude
    hx, hy = main
    sgn = 1 if hx >= x0 else -1
    return ((x0 + hx) / 2 + sgn * 8, (y0 + hy) / 2 + 6)


def _bras(x0, y0, main, coude, couleur, largeur=15, bord=None, poignet=None):
    """Bras courbe de l'épaule (x0, y0) à la main ; `bord` : liseré plus foncé,
    `poignet` : couleur d'un revers de manche près de la main."""
    hx, hy = main
    cx, cy = _controle(x0, y0, main, coude)
    d = f"M {x0} {y0} Q {n(cx)} {n(cy)} {hx} {hy}"
    m = []
    if bord:
        m.append(chemin(d, stroke=bord, sw=largeur + 4))
    m.append(chemin(d, stroke=couleur, sw=largeur))
    if bord:
        # pli du coude : petit trait au milieu de la courbe
        px, py = (x0 + 2 * cx + hx) / 4, (y0 + 2 * cy + hy) / 4
        tx, ty = hx - x0, hy - y0
        L = math.hypot(tx, ty) or 1
        nx, ny = -ty / L, tx / L
        if math.hypot(cx - (x0 + hx) / 2, cy - (y0 + hy) / 2) > 14:
            m.append(trait(n(px + nx * 3 - tx / L * 3), n(py + ny * 3 - ty / L * 3), n(px + nx * 3 + tx / L * 3), n(py + ny * 3 + ty / L * 3), bord, 2, opacity=0.6))
    if poignet:
        k = 0.24
        bx, by = hx + (cx - hx) * k, hy + (cy - hy) * k
        m.append(cercle(n(bx), n(by), largeur * 0.6, poignet))
    return "".join(m)


def _main(hx, hy, r, couleur, bord=None):
    """Main (ou patte) ronde avec un petit pouce tourné vers le corps."""
    sgn = 1 if hx >= 0 else -1
    a = dict(stroke=bord, stroke_width=2) if bord else {}
    return (ellipse(n(hx - sgn * r * 0.72), n(hy - r * 0.5), r * 0.45, r * 0.55, couleur, rot=sgn * -30, **a)
            + cercle(hx, hy, r, couleur, **a))


def filtre_contour(epaisseur=2.4, couleur=ENCRE, opacite=0.5):
    """Filtre SVG qui entoure une silhouette d'un liseré ; renvoie (définition, url)."""
    fid = uid("c")
    f = el("filter", el("feMorphology", in_="SourceAlpha", operator="dilate", radius=n(epaisseur, 2), result="e")
           + el("feFlood", flood_color=couleur, flood_opacity=opacite)
           + el("feComposite", in2="e", operator="in", result="o")
           + el("feMerge", el("feMergeNode", in_="o") + el("feMergeNode", in_="SourceGraphic")),
           id=fid, x="-15%", y="-15%", width="130%", height="130%")
    return f, f"url(#{fid})"


def avec_contour(m, s=1.0, opacite=0.5):
    """Entoure un dessin (coordonnées locales, échelle s) d'un liseré foncé."""
    f, url = filtre_contour(2.3 / max(s, 0.3) ** 0.45, opacite=opacite)
    return f + g(m, filter=url)


# Ombres douces sous les personnages ; un livre qui dessine de vraies ombres
# portées (livres de sciences) les coupe avec `OMBRES_DOUCES = False`.
OMBRE_SOL = [True]


# Sens de l'ombre portée douce : 1 = vers la droite (lumière venue d'en haut
# à gauche), 0 = ombre centrée. Les livres de sciences gardent 0 : une ombre
# n'y est dessinée dans un sens que si le Soleil est placé en conséquence.
OMBRE_SENS = [1]


def ombre_sol(x=0, y=0, rx=50, ry=9, opacite=0.13):
    """Ombre au sol : ombre portée allongée du côté opposé à la lumière
    (OMBRE_SENS), puis ombre de contact plus dense sous l'objet."""
    return (ellipse(x + rx * 0.4 * OMBRE_SENS[0], y - ry * 0.2, rx * (1.4 if OMBRE_SENS[0] else 1.2), ry * 1.25, radial([(0, "#1c2a52", opacite * 0.9), (0.6, "#1c2a52", opacite * 0.45), (1, "#1c2a52", 0)]))
            + ellipse(x, y, rx * 1.05, ry * 1.3, radial([(0, "#000", min(opacite * 2.2, 0.5)), (0.55, "#000", opacite * 1.1), (1, "#000", 0)])))


def ombrage(forme, sombre=(), clair=(), opacite=0.11, reflets=()):
    """Ombre et reflet découpés dans `forme` (élément SVG servant de masque).

    sombre / clair : listes de (x, y, rx, ry[, rot]) d'ellipses ; reflets :
    lumière réfléchie, très douce, au bord de la partie dans l'ombre. L'ombre
    est froide (bleu nuit) plutôt que noire."""
    cid = uid("k")
    m = []
    # ombres à bord fondu : le modelé tourne doucement avec la forme
    flou = radial([(0, "#1c2a52", min(opacite * 1.35, 1)), (0.62, "#1c2a52", min(opacite * 1.2, 1)), (1, "#1c2a52", 0)])
    for e in sombre:
        m.append(ellipse(*e[:4], flou, rot=e[4] if len(e) > 4 else None))
    for e in reflets:
        m.append(ellipse(*e[:4], "#fff4e6", rot=e[4] if len(e) > 4 else None, opacity=0.16))
    for e in clair:
        m.append(ellipse(*e[:4], "#fff", rot=e[4] if len(e) > 4 else None, opacity=0.24))
    return el("clipPath", forme, id=cid) + g(m, clip_path=f"url(#{cid})")


def mains(x, y, s=1.0, bras="bas", flip=False):
    """Position (dans la page) des mains gauche et droite d'un personnage."""
    out = []
    for hx, hy in POSES[bras]:
        if flip:
            hx = -hx
        out.append((x + hx * s, y + hy * s))
    if flip:
        out.reverse()
    return out


def _motif(forme_clip, motif, couleur_motif):
    if not motif:
        return ""
    cid = uid("m")
    m = [el("clipPath", forme_clip, id=cid)]
    if motif == "rayures":
        lignes = "".join(rect(-60, y, 120, 8, couleur_motif) for y in range(-118, 0, 18))
    elif motif == "pois":
        lignes = "".join(cercle(x, y, 5, couleur_motif) for y in range(-110, 0, 20) for x in range(-50 + (y // 20 % 2) * 10, 60, 22))
    else:
        lignes = ""
    m.append(g(lignes, clip_path=f"url(#{cid})"))
    return "".join(m)


# Espèces à poils qui reçoivent une petite mèche sur le haut de la tête.
TOUPET = {"ours", "chat", "chien", "renard", "loup", "ecureuil", "singe", "castor", "lapin", "souris",
          "lievre", "rat", "chevre", "cerf", "panda", "ane"}
COIFFES = {"chapeau", "toque", "bonnet", "casque", "couronne"}
# Espèces aux joues ébouriffées.
JOUES_POILUES = {"chat", "renard", "loup", "ecureuil"}


def _pieds(pas, pieds, bord, haut=False):
    """Les deux pieds, posés, en marche, sur la pointe ou en l'air."""
    m = []
    if haut:
        return [ellipse(-30, -14, 12, 18, pieds, rot=30, stroke=bord, stroke_width=2),
                ellipse(30, -14, 12, 18, pieds, rot=-30, stroke=bord, stroke_width=2)]
    for sgn in (-1, 1):
        # au repos, le poids sur un pied : le droit un peu en avant (plus bas,
        # plus grand), les deux pointes légèrement ouvertes
        x, yy, rot, rx = sgn * 21, -9 + sgn * 1.5, sgn * 7, 19 + sgn * 0.8
        if pas == "marche" and sgn > 0:
            x, yy, rot, rx = 26, -20, -24, 19
        elif pas == "pointe" and sgn > 0:
            x, yy, rot, rx = 24, -12, -40, 19
        elif pas == "court":
            x, yy, rot, rx = (-18, -8, -6, 20) if sgn < 0 else (30, -38, -58, 17)
        elif pas == "saute":
            x, yy, rot, rx = sgn * 20, -6, sgn * 28, 19
        m.append(ellipse(x, yy, rx, 11, pieds, rot=rot or None, stroke=bord, stroke_width=2))
        # doigts : deux petits plis à l'avant
        for dx in (-6, 6):
            ang = math.radians(rot)
            px, py = x + dx * math.cos(ang), yy + 5 + dx * math.sin(ang)
            m.append(trait(n(px), n(py), n(px - 2 * math.sin(ang)), n(py - 6 * math.cos(ang)), bord, 2, opacity=0.7))
    return m


def perso(espece, x=0, y=0, s=1.0, flip=False, expr="sourire", bras="bas", regard=(0, 0),
          couleur=None, habit=None, motif=None, couleur_motif="#ffffff", acc=(), objet=None,
          derriere=None, rot=0, larmes=False, joues=True, couleur_acc=None, tache=False,
          sy=None, pieds_haut=False, visage=None, pas=None, penche=None, ombre=None):
    """Un personnage animal, dessiné de face.

    espece : clé de ESPECES ; expr : clé de EXPRESSIONS ; bras : clé de POSES.
    habit : couleur d'un vêtement sur le corps (et les bras) ; motif : "rayures" | "pois".
    acc : accessoires parmi "noeud", "chapeau", "toque", "bonnet", "casque",
          "lunettes", "echarpe", "tablier", "couronne", "fleur".
    objet : dessin (coordonnées locales) tenu devant le corps, entre les bras et les mains.
    derriere : dessin (coordonnées locales) placé derrière le personnage.
    pas : position des pieds, "marche", "pointe" ou "saute" (déduite de la pose
          si absente) ; penche : inclinaison de la tête en degrés (déduite de
          l'expression si absente) ; ombre : ombre douce au sol (par défaut
          OMBRE_SOL).
    """
    K = ESPECES[espece]
    c = couleur or K["c"]
    c2 = visage or K["c2"]
    pieds = K["pieds"] if not couleur else _assombrir(c, 0.85)
    if espece in ("mouton", "panda", "fourmi"):
        pieds = K["pieds"]
    if couleur_acc is None:
        couleur_acc = "#fa5252"
    if pas is None:
        pas = PAS_POSE.get(bras)
    yeux_style, bouche_style, sourcils_style = EXPRESSIONS[expr]
    manche = habit or c
    peau_main = c if espece != "panda" else "#343a40"
    if espece == "mouton":
        peau_main = "#495057"
        manche = habit or "#868e96"
    if espece == "panda":
        manche = habit or "#343a40"
    bord_manche = _assombrir(manche, 0.72)
    bord_main = _assombrir(peau_main, 0.72)
    # vue de trois quarts : quand le personnage regarde de côté, son ventre
    # et son visage glissent un peu de ce côté-là
    tourne = max(-1.0, min(1.0, regard[0])) * 10
    incline = 0 if pieds_haut or rot else INCLINE.get(bras, 0)
    m = []
    if derriere:
        m.append(derriere)

    # --- derrière : queue, grandes oreilles
    if espece == "chat":
        m.append(chemin("M 28 -40 Q 80 -40 78 -95 Q 76 -120 92 -126", stroke=c, sw=13))
        m.append(chemin("M 84 -112 Q 86 -122 92 -126", stroke=_assombrir(c, 0.8), sw=13))
    elif espece == "renard":
        m.append(ellipse(62, -58, 26, 58, c, rot=40))
        m.append(chemin("M 46 -40 Q 64 -60 70 -90", stroke=_assombrir(c, 0.85), sw=3, opacity=0.6))
        m.append(ellipse(95, -95, 14, 20, "#fff4e6", rot=40))
    elif espece in ("souris", "rat"):
        m.append(chemin("M 22 -20 Q 80 -8 76 -64 Q 72 -96 98 -104", stroke="#ffa8a8", sw=6))
    elif espece == "loup":
        m.append(ellipse(62, -58, 26, 58, c, rot=40))
        m.append(chemin("M 46 -40 Q 64 -60 70 -90", stroke=_assombrir(c, 0.8), sw=3, opacity=0.6))
        m.append(ellipse(95, -95, 14, 20, "#dee2e6", rot=40))
    elif espece in ("lion", "ane", "boeuf"):
        touffe = K.get("criniere") or _assombrir(c, 0.6)
        m.append(chemin("M 28 -40 Q 84 -34 84 -86", stroke=c, sw=9))
        m.append(ellipse(84, -96, 11, 16, touffe))
    elif espece == "cigale":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 46, -70, 26, 74, "#e7f5ff", rot=sgn * -22, opacity=0.8, stroke="#91a7ff", stroke_width=3))
            m.append(chemin(f"M {sgn * 34} -130 Q {sgn * 50} -80 {sgn * 66} -10", stroke="#91a7ff", sw=2))
    elif espece == "singe":
        m.append(chemin("M 30 -30 Q 96 -20 92 -90 Q 88 -132 56 -124 Q 36 -116 52 -98", stroke=c, sw=10))
    elif espece == "cerf":
        m.append(ellipse(30, -36, 12, 16, "#fff", rot=-30))
    elif espece == "cochon":
        m.append(chemin("M 34 -44 q 16 -2 14 -14 q -2 -10 -10 -6 q -6 6 4 12 q 10 4 18 -4", stroke=K["groin"], sw=5))
    elif espece == "chien":
        m.append(chemin("M 30 -48 Q 58 -60 62 -94", stroke=c, sw=12))
    elif espece == "fourmi":
        m.append(ellipse(42, -42, 40, 32, _assombrir(c, 0.85), rot=-25))
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 30} -60 Q {sgn * 62} -62 {sgn * 70} -36", stroke=pieds, sw=7))
    elif espece == "castor":
        m.append(ellipse(40, -16, 30, 50, "#5c3a1e", rot=60))
        m.append(g([trait(22, -28, 62, -6, "#4a2e16", 2, opacity=0.5), trait(30, -40, 68, -20, "#4a2e16", 2, opacity=0.5)]))
    elif espece == "elephant":
        m.append(chemin("M 30 -30 Q 50 -30 52 -10", stroke=pieds, sw=5))
    elif espece == "ecureuil":
        queue = "M 18 -34 C 112 -22 138 -128 104 -184 C 82 -222 22 -226 26 -186 C 30 -160 76 -164 76 -130 C 76 -88 34 -80 18 -58 Z"
        m.append(chemin(queue, c))
        m.append(chemin("M 40 -52 C 96 -52 118 -130 96 -172 C 84 -196 50 -204 44 -190", stroke=eclaircir(c, 0.35), sw=10, opacity=0.8))
    elif espece == "herisson":
        for k in range(9):
            a = math.radians(-160 + k * 17.5)
            if -110 < math.degrees(a) < -70:
                continue
            cx, cy = math.cos(a) * 44, -64 + math.sin(a) * 52
            m.append(poly([(cx - 10, cy), (cx + math.cos(a) * 26, cy + math.sin(a) * 26), (cx + 10, cy)], K["piquants"]))

    # --- pieds
    debut_pieds = len(m)
    m += _pieds(pas, pieds, _assombrir(pieds, 0.7), haut=pieds_haut)
    fin_pieds = len(m)

    # --- corps
    corps = ellipse(0, -62, 42, 52, "#000")
    if espece == "mouton" and not habit:
        for k in range(10):
            a = math.radians(k * 36)
            m.append(cercle(math.cos(a) * 36, -62 + math.sin(a) * 44, 18, "#f8f9fa", stroke="#dee2e6", stroke_width=3))
        m.append(ellipse(0, -62, 42, 50, "#f8f9fa"))
        for k in range(5):
            a = math.radians(30 + k * 70)
            m.append(chemin(f"M {n(math.cos(a) * 18 - 6)} {n(-62 + math.sin(a) * 24)} q 6 -7 12 0", stroke="#dee2e6", sw=3))
    else:
        m.append(ellipse(0, -62, 42, 52, volume(habit or c, 0.28, 0.8)))
        if habit:
            m.append(_motif(corps, motif, couleur_motif))
            fonce_h = _assombrir(habit, 0.78)
            # encolure et boutons
            m.append(chemin("M -24 -106 Q 0 -90 24 -106", stroke=fonce_h, sw=3))
            if not motif and "tablier" not in acc:
                for yy in (-80, -60):
                    m.append(cercle(0, yy, 3.6, eclaircir(habit, 0.55), stroke=fonce_h, stroke_width=1.5))
        elif K.get("ventre"):
            m.append(ellipse(tourne * 0.8, -54, 27 - abs(tourne) * 0.25, 35, volume(c2, 0.3, 0.88)))
            if espece == "cigale":
                for yy in (-72, -56, -40):
                    m.append(chemin(f"M -20 {yy} Q 0 {yy + 6} 20 {yy}", stroke=_assombrir(c2, 0.8), sw=3))
            elif espece not in ("grenouille", "elephant", "cochon", "fourmi"):
                # quelques poils au bord du ventre
                for sgn in (-1, 1):
                    m.append(chemin(f"M {sgn * 25} -66 l {sgn * 5} -4 l {sgn * -1} 6", stroke=_assombrir(c2, 0.85), sw=2))
                    m.append(chemin(f"M {sgn * 24} -42 l {sgn * 5} -4 l {sgn * -1} 6", stroke=_assombrir(c2, 0.85), sw=2))
        if espece == "panda" and not habit:
            m.append(ellipse(0, -62, 42, 52, "#fff"))
            m.append(chemin("M -40 -80 Q 0 -60 40 -80 L 36 -104 Q 0 -118 -36 -104 Z", "#343a40"))
    # modelé : côté droit plus sombre, ombre de la tête, reflet
    m.append(ombrage(ellipse(0, -62, 42, 52, "#000"), sombre=[(40, -46, 34, 62), (0, -104, 36, 14), (0, -6, 40, 12)],
                     clair=[(-24, -84, 7, 13, 30), (-36, -56, 3.5, 18, 8)], reflets=[(46, -52, 9, 34)]))
    if "tablier" in acc:
        m.append(chemin("M -26 -96 L 26 -96 L 30 -30 Q 0 -18 -30 -30 Z", "#fff", stroke="#e9ecef", sw=2))
        m.append(rect(-14, -64, 28, 18, "#ffe3e3", rx=4))
        m.append(trait(-36, -92, 36, -92, "#fff", 5))
    if "cape" in acc:
        debut_pieds, fin_pieds = debut_pieds + 2, fin_pieds + 2
        m.insert(0, chemin("M -40 -100 Q -70 -40 -64 -4 L 64 -4 Q 70 -40 40 -100 Z", cylindre(couleur_acc, 0.2, 0.75)))
        m.insert(1, chemin("M -20 -96 Q -36 -50 -30 -6 M 20 -96 Q 36 -50 30 -6", stroke=_assombrir(couleur_acc, 0.8), sw=3))

    # --- bras
    main_g, main_d = POSES[bras]
    coude_g, coude_d = COUDES.get(bras, (None, None))
    if bras == "croises":
        coude_g, coude_d = (-40, -60), (40, -64)
    poignet = _assombrir(habit, 0.85) if habit else None

    def un_bras(x0, main, coude):
        return _bras(x0, -96, main, coude, manche, bord=bord_manche, poignet=poignet)

    bras_svg = un_bras(-32, main_g, coude_g) + un_bras(32, main_d, coude_d)
    mains_svg = _main(*main_g, 11.5, peau_main, bord_main) + _main(*main_d, 11.5, peau_main, bord_main)
    devant = bras in DEVANT_VISAGE
    if not devant:
        m.append(bras_svg)
        if objet:
            m.append(objet)
        m.append(mains_svg)
    elif objet:
        m.append(objet)

    # --- tête, un peu penchée selon l'humeur
    tete = _tete(espece, K, c, c2, yeux_style, bouche_style, sourcils_style, regard, joues, expr, larmes, acc, couleur_acc, tache)
    if penche is None:
        penche = 0 if devant or bras in ("porte", "tete") else PENCHE.get(expr, 0)
    m.append(g(tete, f"rotate({n(penche)} 0 -100)") if penche else tete)
    if "echarpe" in acc:
        m.append(_echarpe(couleur_acc))

    if devant:
        if bras == "pense":
            m.append(_bras(-32, -96, main_g, None, manche, bord=bord_manche, poignet=poignet) + _main(*main_g, 11.5, peau_main, bord_main))
            m.append(_bras(32, -96, main_d, (40, -80), manche, bord=bord_manche, poignet=poignet) + _main(*main_d, 11.5, peau_main, bord_main))
        else:
            m.append(bras_svg + mains_svg)

    if incline:
        pivot = f"rotate({n(incline)} 0 -16)"
        m = [g(m[:debut_pieds], pivot)] + m[debut_pieds:fin_pieds] + [g(m[fin_pieds:], pivot)]
    dessin = avec_contour(m, s)
    if (OMBRE_SOL[0] if ombre is None else ombre) and not rot and not pieds_haut:
        dessin = ombre_sol(incline * 0.8, -3 if pas != "saute" else 4, 54 if pas != "saute" else 40) + dessin
    if rot:
        occuper(x - 250 * s, y - 250 * s, x + 250 * s, y + 250 * s)
    else:
        occuper(x - 85 * s, y - 250 * s * (sy or 1), x + 85 * s, y + 8 * s)
    return place(dessin, x, y, s, flip=flip, rot=rot, sy=sy)


def _echarpe(ca):
    return g([rect(-42, -104, 84, 18, ca, rx=9), chemin("M 18 -94 L 30 -48 L 14 -48 L 8 -94 Z", ca),
              trait(15, -56, 29, -56, "#fff", 3, opacity=0.6), trait(-30, -95, 30, -95, _assombrir(ca, 0.8), 2, opacity=0.6)])


def _rvb(hexa):
    """« #rrggbb » ou « #rgb » → (r, v, b) ; None pour une autre couleur."""
    h = hexa.lstrip("#") if isinstance(hexa, str) else ""
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) if len(h) == 6 else None
    except ValueError:
        return None


def _assombrir(hexa, k=0.8):
    rvb = _rvb(hexa)
    if rvb is None:
        return hexa
    r, gg, b = rvb
    return "#%02x%02x%02x" % (int(r * k), int(gg * k), int(b * k))


def eclaircir(hexa, k=0.5):
    rvb = _rvb(hexa)
    if rvb is None:
        return hexa
    r, gg, b = rvb
    return "#%02x%02x%02x" % (int(r + (255 - r) * k), int(gg + (255 - gg) * k), int(b + (255 - b) * k))


def _tete(espece, K, c, c2, ys, bs, ss, regard, joues, expr, larmes, acc, ca, tache):
    m = []
    hy = -150
    ex, ey = 19, -152
    my = -121
    sclere = False
    tete_c = c
    r = 55
    tourne = max(-1.0, min(1.0, regard[0])) * 10

    # oreilles derrière la tête
    if espece == "ours" or espece == "castor":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 40, -194, 19, c))
            m.append(cercle(sgn * 40, -194, 10, c2))
    elif espece == "panda":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 40, -194, 20, "#343a40"))
    elif espece == "lapin" and "casque" not in acc:
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 23, -228, 15, 48, c, rot=sgn * 8))
            m.append(ellipse(sgn * 23, -226, 7, 36, K["interieur"], rot=sgn * 8))
    elif espece == "lievre":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 26, -242, 15, 62, c, rot=sgn * 12))
            m.append(ellipse(sgn * 26, -240, 7, 48, K["interieur"], rot=sgn * 12))
            m.append(ellipse(sgn * 38, -294, 9, 12, "#4a2c17", rot=sgn * 12))
    elif espece == "rat":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 46, -190, 25, c))
            m.append(cercle(sgn * 46, -190, 15, K["interieur"]))
    elif espece == "lion":
        for k in range(16):
            a = math.radians(k * 22.5)
            m.append(cercle(math.cos(a) * 66, hy - 8 + math.sin(a) * 50, 24, K["criniere"]))
        m.append(ellipse(0, hy - 8, 76, 64, K["criniere"]))
        for sgn in (-1, 1):
            m.append(cercle(sgn * 40, -196, 16, c))
            m.append(cercle(sgn * 40, -196, 8, c2))
    elif espece == "ane":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 36, -222, 15, 50, c, rot=sgn * 24))
            m.append(ellipse(sgn * 36, -220, 7, 38, K["interieur"], rot=sgn * 24))
            m.append(ellipse(sgn * 54, -262, 8, 11, "#495057", rot=sgn * 24))
    elif espece == "chevre":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 18} -190 Q {sgn * 26} -246 {sgn * 64} -238", stroke=K["cornes"], sw=13))
            m.append(ellipse(sgn * 62, -156, 26, 11, c, rot=sgn * 18))
            m.append(ellipse(sgn * 62, -156, 15, 6, K["interieur"], rot=sgn * 18))
    elif espece == "cerf":
        for sgn in (-1, 1):
            b = K["bois"]
            m.append(chemin(f"M {sgn * 22} -194 Q {sgn * 34} -250 {sgn * 74} -300", stroke=b, sw=11))
            m.append(chemin(f"M {sgn * 30} -236 Q {sgn * 10} -262 {sgn * 14} -292", stroke=b, sw=9))
            m.append(chemin(f"M {sgn * 50} -270 Q {sgn * 40} -300 {sgn * 46} -324", stroke=b, sw=8))
            m.append(chemin(f"M {sgn * 34} -222 Q {sgn * 66} -230 {sgn * 92} -252", stroke=b, sw=8))
            m.append(ellipse(sgn * 62, -170, 28, 12, c, rot=sgn * 26))
            m.append(ellipse(sgn * 62, -170, 17, 6, K["interieur"], rot=sgn * 26))
    elif espece == "singe":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 58, -150, 22, c))
            m.append(cercle(sgn * 58, -150, 12, K["interieur"]))
    elif espece == "boeuf":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 34} -188 Q {sgn * 88} -192 {sgn * 86} -240", stroke=K["cornes"], sw=15))
            m.append(ellipse(sgn * 66, -162, 24, 12, c, rot=sgn * 20))
            m.append(ellipse(sgn * 66, -162, 14, 6, "#ffc9c9", rot=sgn * 20))
    elif espece == "cigale":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 14} -198 Q {sgn * 20} -226 {sgn * 34} -232", stroke=_assombrir(c, 0.6), sw=4))
        sclere = True
        ex = 30
    elif espece == "souris":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 48, -192, 31, c))
            m.append(cercle(sgn * 48, -192, 20, K["interieur"]))
    elif espece in ("chat", "renard", "ecureuil", "loup"):
        inter = K.get("interieur", "#fff4e6") if espece not in ("renard", "loup") else ("#fff4e6" if espece == "renard" else "#dee2e6")
        for sgn in (-1, 1):
            m.append(poly([(sgn * 52, -170), (sgn * 48, -228), (sgn * 12, -200)], c))
            m.append(poly([(sgn * 44, -178), (sgn * 43, -216), (sgn * 20, -198)], inter))
            if espece in ("renard", "loup"):
                m.append(poly([(sgn * 50.5, -212), (sgn * 48, -228), (sgn * 36, -219)], "#5c3d2e" if espece == "renard" else "#495057"))
            if espece == "ecureuil":
                m.append(poly([(sgn * 42, -224), (sgn * 50, -246), (sgn * 54, -222)], _assombrir(c, 0.8)))
    elif espece == "elephant":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 66, -148, 42, 54, c, rot=sgn * -10))
            m.append(ellipse(sgn * 70, -146, 28, 40, K["interieur"], rot=sgn * -10))
    elif espece == "herisson":
        for k in range(13):
            a = math.radians(180 + k * 15)
            cx, cy = math.cos(a) * 50, hy + math.sin(a) * 50
            m.append(poly([(cx - math.sin(a) * 12, cy + math.cos(a) * 12), (cx + math.cos(a) * 34, cy + math.sin(a) * 34), (cx + math.sin(a) * 12, cy - math.cos(a) * 12)], K["piquants"]))
        tete_c = c2
    elif espece == "fourmi":
        for sgn in (-1, 1):
            m.append(chemin(f"M {sgn * 16} -198 Q {sgn * 24} -236 {sgn * 44} -244", stroke=_assombrir(c, 0.7), sw=5))
            m.append(cercle(sgn * 46, -246, 8, _assombrir(c, 0.7)))
        sclere = True
    elif espece == "mouton":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 52, -150, 22, 10, "#d6bfa3", rot=sgn * 20))
        tete_c = c2
        r = 46
    elif espece == "grenouille":
        for sgn in (-1, 1):
            m.append(cercle(sgn * 27, -192, 23, c))
        ex, ey = 27, -194
        sclere = True
        my = -125

    debut_tete = len(m)
    m.append(cercle(0, hy, r, volume(tete_c, 0.25, 0.82)))
    # modelé de la tête : joue droite dans l'ombre, reflet sur le front
    m.append(ombrage(cercle(0, hy, r, "#000"), sombre=[(r * 0.75, hy + r * 0.45, r * 0.8, r * 0.75)],
                     clair=[(-r * 0.45, hy - r * 0.58, r * 0.26, r * 0.14, -30)], opacite=0.08,
                     reflets=[(r * 1.02, hy + r * 0.25, r * 0.16, r * 0.55, -15)]))
    if espece in JOUES_POILUES:
        # touffes de poils ébouriffées sur les joues
        for sgn in (-1, 1):
            m.append(poly([(sgn * (r - 9), hy + 4), (sgn * (r + 9), hy + 12), (sgn * (r - 2), hy + 18), (sgn * (r + 7), hy + 27),
                           (sgn * (r - 8), hy + 30)], tete_c))
    if espece in TOUPET and not (COIFFES & set(acc)):
        m.append(chemin(f"M -14 {hy - r + 6} Q -12 {hy - r - 12} -2 {hy - r - 2} Q 2 {hy - r - 18} 9 {hy - r - 1} Q 16 {hy - r - 10} 16 {hy - r + 6} Z", tete_c))
    debut_visage = len(m)

    if espece == "mouton":
        for k, (wx, wy) in enumerate([(-30, -192), (-10, -202), (12, -202), (32, -190), (0, -188)]):
            m.append(cercle(wx, wy, 17, "#f8f9fa"))
    if espece == "panda":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 20, -150, 14, 18, "#343a40", rot=sgn * -25))
        sclere = False
    if espece == "herisson":
        m.append(chemin("M -44 -175 Q 0 -215 44 -175 Q 20 -186 0 -178 Q -20 -186 -44 -175 Z", K["piquants"]))
        for sgn in (-1, 1):
            m.append(cercle(sgn * 42, -180, 9, c2))

    # museaux et nez (avant les yeux pour que les yeux restent visibles)
    if espece in ("renard", "loup"):
        m.append(chemin("M -54 -140 Q -30 -142 0 -120 Q 30 -142 54 -140 Q 44 -98 0 -96 Q -44 -98 -54 -140 Z", "#fff4e6" if espece == "renard" else c2))
    if espece == "lion":
        m.append(ellipse(0, -126, 27, 20, c2))
    if espece == "ane":
        m.append(chemin("M -30 -200 Q -12 -222 0 -204 Q 12 -222 30 -200 Q 0 -190 -30 -200 Z", "#495057"))
        m.append(ellipse(0, -118, 34, 27, c2))
    if espece == "chevre":
        m.append(poly([(-14, -104), (14, -104), (0, -62)], "#d6c2a8"))
        m.append(ellipse(0, -124, 24, 18, c2))
    if espece == "cerf":
        m.append(ellipse(0, -122, 26, 20, c2))
    if espece == "singe":
        m.append(chemin("M 0 -176 Q -14 -198 -30 -190 Q -50 -180 -44 -150 Q -40 -136 -30 -134 Q -40 -104 0 -100 Q 40 -104 30 -134 Q 40 -136 44 -150 Q 50 -180 30 -190 Q 14 -198 0 -176 Z", c2))
    if espece == "boeuf":
        for k, dx in enumerate((-18, 0, 18)):
            m.append(cercle(dx, -202 + (k % 2) * -4, 13, _assombrir(c, 0.75)))
        m.append(ellipse(0, -114, 40, 27, K["mufle"]))
    if espece in ("ours", "castor"):
        m.append(ellipse(0, -126, 25, 19, c2))
    if espece == "chien":
        m.append(ellipse(0, -125, 23, 18, c2))
        if tache:
            m.append(ellipse(-19, -155, 15, 16, K["oreilles"], opacity=0.7))
    if espece == "panda":
        m.append(ellipse(0, -125, 20, 15, "#f1f3f5"))

    if joues:
        rouge = expr in ("fache", "furieux", "timide")
        jc = "#ff6b6b" if expr in ("fache", "furieux") else ROSE
        jr = 1.35 if rouge or expr == "souffle" else 1.0
        jx = 36 if espece != "grenouille" else 38
        jy = -128 if espece != "cochon" else -134
        for sgn in (-1, 1):
            m.append(ellipse(sgn * jx, jy, 9 * jr, 5.5 * jr, jc, opacity=0.7))

    # yeux
    if espece == "panda":
        pass
    m.append(yeux_trois_quarts(ex, ey, ys, regard, sclere, tourne))
    m.append(sourcils(ex, ey if espece != "grenouille" else -200, ss))
    if larmes:
        for sgn in (-1, 1):
            m.append(goutte(sgn * (ex + 4), ey + 26, 0.8, "#74c0fc"))

    # nez
    if espece in ("ours", "castor"):
        m.append(ellipse(0, -134, 10, 7, ENCRE))
        my = -120
    elif espece == "chien":
        m.append(ellipse(0, -136, 11, 8, ENCRE))
        m.append(cercle(-3, -139, 2.5, "#fff"))
        my = -120
    elif espece == "panda":
        m.append(ellipse(0, -131, 8, 5.5, ENCRE))
        my = -120
    elif espece in ("renard", "loup"):
        m.append(ellipse(0, -128, 8, 6, ENCRE))
        my = -118
    elif espece == "lion":
        m.append(poly([(-10, -138), (10, -138), (0, -127)], "#7c4a1e"))
        my = -121
    elif espece == "ane":
        m.append(ellipse(-13, -122, 4.5, 6, _assombrir(c2, 0.55)) + ellipse(13, -122, 4.5, 6, _assombrir(c2, 0.55)))
        my = -110
    elif espece == "chevre":
        m.append(ellipse(0, -132, 7, 5, "#8a6d4f"))
        my = -122
    elif espece == "boeuf":
        m.append(ellipse(-15, -118, 5, 7, "#c2255c") + ellipse(15, -118, 5, 7, "#c2255c"))
        my = -106
    elif espece == "cerf":
        m.append(ellipse(0, -130, 9, 6.5, ENCRE))
        my = -118
    elif espece == "singe":
        m.append(ellipse(-5, -128, 2.5, 3.5, _assombrir(c, 0.7)) + ellipse(5, -128, 2.5, 3.5, _assombrir(c, 0.7)))
        my = -118
    elif espece == "cigale":
        my = -124
    elif espece in ("lapin", "souris", "lievre", "rat"):
        m.append(ellipse(0, -132, 6, 4.5, ROSE))
        my = -122
    elif espece == "chat":
        m.append(poly([(-6, -134), (6, -134), (0, -127)], ROSE))
        my = -122
    elif espece == "ecureuil":
        m.append(ellipse(0, -132, 7, 5, "#5c3a1e"))
        my = -122
    elif espece == "herisson":
        m.append(cercle(0, -130, 8, ENCRE))
        my = -116
    elif espece == "cochon":
        m.append(ellipse(0, -128, 21, 15, K["groin"]))
        m.append(ellipse(-7, -128, 3.5, 5, "#c2255c"))
        m.append(ellipse(7, -128, 3.5, 5, "#c2255c"))
        my = -107
    elif espece == "mouton":
        m.append(ellipse(0, -132, 7, 5, "#8a6d4f"))
        my = -122
    elif espece == "elephant":
        my = -112

    # bouche
    if espece == "elephant":
        m.append(bouche(-22, -114, bs, 0.8))
        trompe = "M 0 -142 Q 2 -110 12 -92 Q 22 -76 40 -82"
        m.append(chemin(trompe, stroke=_assombrir(c, 0.8), sw=25))
        m.append(chemin(trompe, stroke=c, sw=20))
        for k in range(3):
            m.append(chemin(f"M {-6 + k * 5} {-122 + k * 12} q 9 3 16 -2", stroke=_assombrir(c, 0.8), sw=2))
    else:
        L = 2.0 if espece == "grenouille" else 1.0
        m.append(bouche(0, my, bs, L))

    # moustaches
    if espece in ("chat", "souris", "lapin", "lievre", "rat", "lion"):
        for sgn in (-1, 1):
            m.append(trait(sgn * 14, -130, sgn * 46, -136, "#868e96", 2))
            m.append(trait(sgn * 14, -126, sgn * 46, -122, "#868e96", 2))
    if espece == "castor":
        m.append(rect(-9, my + 6, 18, 14, "#fff", rx=3, stroke=ENCRE, stroke_width=1.5))
        m.append(trait(0, my + 6, 0, my + 20, ENCRE, 1.5))

    if tourne:
        # trois quarts : traits du visage décalés, oreilles de derrière un peu à l'opposé
        visage_ = g(m[debut_visage:], f"translate({n(tourne)} 0)")
        oreilles = g(m[:debut_tete], f"translate({n(-tourne * 0.45)} 0)") if debut_tete else ""
        m = [oreilles] + m[debut_tete:debut_visage] + [visage_]
    # oreilles devant (chien, cochon)
    if espece == "chien":
        for sgn in (-1, 1):
            m.append(ellipse(sgn * 55, -146, 15, 32, K["oreilles"], rot=sgn * 14))
    elif espece == "cochon":
        for sgn in (-1, 1):
            m.append(poly([(sgn * 20, -198), (sgn * 52, -214), (sgn * 46, -176)], K["groin"]))

    # accessoires de tête
    if "noeud" in acc:
        m.append(g([poly([(28, -196), (8, -212), (8, -180)], ca), poly([(28, -196), (48, -212), (48, -180)], ca), cercle(28, -196, 7, _assombrir(ca, 0.8))]))
    if "fleur" in acc:
        m.append(fleur(34, -184, 0.8, ca, tige=0))
    if "chapeau" in acc:
        m.append(chapeau(0, -193, 1.0, ca))
    if "toque" in acc:
        m.append(g([cercle(-26, -222, 27.5, "#dee2e6"), cercle(26, -222, 27.5, "#dee2e6"), cercle(0, -236, 31.5, "#dee2e6"),
                    cercle(-26, -222, 26, "#fff"), cercle(26, -222, 26, "#fff"), cercle(0, -236, 30, "#fff"),
                    rect(-40, -212, 80, 26, "#fff", rx=6, stroke="#e9ecef", stroke_width=2)]))
    if "bonnet" in acc:
        m.append(g([chemin("M -56 -160 Q -56 -222 0 -222 Q 56 -222 56 -160 Z", ca), rect(-60, -172, 120, 20, "#fff", rx=10), cercle(0, -226, 16, "#fff")]))
    if "casque" in acc:
        m.append(g([trait(-50, -174, -40, -108, ENCRE, 3), trait(50, -174, 40, -108, ENCRE, 3),
                    chemin("M -60 -170 Q -62 -236 0 -236 Q 62 -236 60 -170 Q 0 -182 -60 -170 Z", ca),
                    chemin("M -30 -222 Q 0 -232 30 -222", stroke="#fff", sw=6, opacity=0.7)]))
        if espece == "lapin":
            for sgn in (-1, 1):
                m.append(ellipse(sgn * 22, -262, 14, 40, c, rot=sgn * 8))
                m.append(ellipse(sgn * 22, -260, 6, 30, K["interieur"], rot=sgn * 8))
    if "lunettes" in acc:
        m.append(g([cercle(-ex, ey, 15, "none", stroke=ENCRE, stroke_width=3.5), cercle(ex, ey, 15, "none", stroke=ENCRE, stroke_width=3.5), trait(-ex + 15, ey, ex - 15, ey, ENCRE, 3)],
                   f"translate({n(tourne)} 0)" if tourne else None))
    if "couronne" in acc:
        m.append(poly([(-34, -196), (-34, -232), (-17, -212), (0, -240), (17, -212), (34, -232), (34, -196)], "#ffd43b", stroke="#f59f00", stroke_width=3))
    return g(m)


def chapeau(x, y, s=1.0, couleur="#fa5252", ruban="#ffd43b", rot=0, fleur_=True):
    """Chapeau rond ; (x, y) = milieu du bord."""
    m = [ellipse(0, 0, 64, 13, couleur), chemin("M -36 0 Q -38 -52 0 -52 Q 38 -52 36 0 Z", couleur),
         rect(-37, -16, 74, 12, ruban)]
    if fleur_:
        m.append(g([cercle(28, -12, 8, "#fff"), cercle(28, -12, 4, "#ffd43b")]))
    return place(m, x, y, s, rot=rot)


# --- Personnages de forme différente ----------------------------------------

def _plumes(cx, cy, rx, ry, rot, c, nb=3):
    """Aile en relief : ellipse modelée et bouts de plumes marqués."""
    fonce = _assombrir(c, 0.68)
    m = [ellipse(cx, cy, rx, ry, volume(c, 0.32, 0.72), rot=rot)]
    a = math.radians(rot or 0)
    for k in range(nb):
        t = (k + 1) / (nb + 1)
        # petites encoches vers le bout de l'aile
        px, py = 0, ry * (0.25 + 0.6 * t)
        dx = (t - 0.5) * rx * 1.2
        x0, y0 = cx + (dx * math.cos(a) - py * math.sin(a)), cy + (dx * math.sin(a) + py * math.cos(a))
        x1, y1 = cx + (dx * 0.6 * math.cos(a) - (py - ry * 0.35) * math.sin(a)), cy + (dx * 0.6 * math.sin(a) + (py - ry * 0.35) * math.cos(a))
        m.append(trait(n(x0), n(y0), n(x1), n(y1), fonce, max(1.5, rx * 0.12), opacity=0.55))
    return "".join(m)


def oiseau(x, y, s=1.0, couleur="#4dabf7", ventre="#e7f5ff", expr="sourire", ailes="bas",
           bec_ouvert=False, flip=False, regard=(0, 0), rot=0, pattes=True, acc=()):
    """Petit oiseau tout rond, (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    aile = _assombrir(couleur, 0.85)
    fonce = _assombrir(couleur, 0.8)
    m = []
    if pattes:
        for sgn in (-1, 1):
            m.append(trait(sgn * 12, -30, sgn * 12, -4, "#f08c00", 4))
            m.append(chemin(f"M {sgn * 12 - 9} 0 L {sgn * 12} -6 L {sgn * 12 + 9} 0", stroke="#f08c00", sw=3.5))
    # queue : trois plumes en éventail
    m.append(poly([(38, -70), (66, -86), (62, -60)], lineaire([(0, eclaircir(fonce, 0.2)), (1, _assombrir(fonce, 0.75))], 0, 0, 1, 1)))
    m.append(chemin("M 42 -70 L 63 -80 M 42 -68 L 62 -66", stroke=_assombrir(fonce, 0.7), sw=1.5, opacity=0.6))
    if ailes == "haut":
        m.append(_plumes(-50, -88, 14, 30, -40, aile))
        m.append(_plumes(50, -88, 14, 30, 40, aile))
    m.append(cercle(0, -68, 44, volume(couleur, 0.32, 0.78)))
    m.append(ellipse(0, -52, 28, 26, volume(ventre, 0.4, 0.88)))
    m.append(chemin("M -14 -40 q 4 4 8 0 M 2 -38 q 4 4 8 0 M -6 -30 q 4 4 8 0", stroke=_assombrir(ventre, 0.8), sw=1.6, opacity=0.6))
    m.append(ombrage(cercle(0, -68, 44, "#000"), sombre=[(30, -40, 40, 34)], clair=[(-20, -98, 12, 7, -30)], reflets=[(44, -60, 7, 26)]))
    if ailes == "bas":
        m.append(_plumes(-40, -60, 12, 24, 20, aile))
        m.append(_plumes(40, -60, 12, 24, -20, aile))
    elif ailes == "ouvertes":
        m.append(_plumes(-58, -72, 12, 30, 60, aile))
        m.append(_plumes(58, -72, 12, 30, -60, aile))
    m.append(chemin("M -6 -112 Q -2 -124 6 -118 Q 2 -126 12 -124", stroke=_assombrir(couleur, 0.8), sw=4))
    m.append(ellipse(-26, -70, 7, 4.5, ROSE, opacity=0.7) + ellipse(26, -70, 7, 4.5, ROSE, opacity=0.7))
    m.append(oeil(-15, -82, ys, regard, taille=0.85) + oeil(15, -82, ys, regard, taille=0.85))
    m.append(sourcils(15, -80, ss))
    bec_h, bec_b = lineaire(["#ffc078", "#f76707"]), lineaire(["#ff922b", "#d9480f"])
    if bec_ouvert or bs in ("ouverte", "o", "crie"):
        m.append(poly([(-9, -70), (9, -70), (0, -80)], bec_h))
        m.append(poly([(-8, -66), (8, -66), (0, -54)], bec_b))
    else:
        m.append(poly([(-9, -70), (9, -70), (0, -58)], bec_h))
        m.append(trait(-2, -68, 2, -68, "#fff", 1.5, opacity=0.6))
    if "noeud" in acc:
        m.append(g([poly([(20, -108), (6, -118), (6, -98)], "#fa5252"), poly([(20, -108), (34, -118), (34, -98)], "#fa5252"), cercle(20, -108, 5, "#c92a2a")]))
    occuper(x - 60 * s, y - 120 * s, x + 60 * s, y)
    return place(avec_contour(m, s, 0.35), x, y, s, flip=flip, rot=rot)


def chouette(x, y, s=1.0, couleur="#a9805b", visage="#f3dcc3", expr="sourire", ailes="bas",
             regard=(0, 0), flip=False, acc=(), yeux_grands=True):
    """Chouette debout, (x, y) = sous les pattes."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.8)
    m = []
    for sgn in (-1, 1):
        m.append(ellipse(sgn * 18, -4, 14, 7, volume("#f08c00", 0.4, 0.75)))
        m.append(chemin(f"M {sgn * 18 - 8} -2 v 5 M {sgn * 18} -1 v 6 M {sgn * 18 + 8} -2 v 5", stroke="#c25e00", sw=2))
    if ailes == "haut":
        m.append(_plumes(-56, -110, 18, 44, -35, fonce, 4))
        m.append(_plumes(56, -110, 18, 44, 35, fonce, 4))
    m.append(ellipse(0, -80, 58, 78, volume(couleur, 0.28, 0.78)))
    for sgn in (-1, 1):
        m.append(poly([(sgn * 30, -140), (sgn * 52, -178), (sgn * 52, -130)], cylindre(couleur, 0.25, 0.75)))
        m.append(chemin(f"M {sgn * 38} -142 L {sgn * 50} -168", stroke=fonce, sw=2, opacity=0.6))
    m.append(ellipse(0, -62, 36, 46, volume(eclaircir(couleur, 0.55), 0.35, 0.88)))
    for row in range(3):
        for k in range(3 - (row % 2)):
            xx = -18 + k * 18 + (row % 2) * 9
            yy = -80 + row * 16
            m.append(chemin(f"M {xx - 5} {yy} Q {xx} {yy + 6} {xx + 5} {yy}", stroke=fonce, sw=2.5))
    m.append(ombrage(ellipse(0, -80, 58, 78, "#000"), sombre=[(40, -40, 46, 70)], clair=[(-30, -128, 14, 8, -30)], reflets=[(58, -70, 8, 36)]))
    if ailes == "bas":
        m.append(_plumes(-54, -78, 16, 42, 10, fonce, 4))
        m.append(_plumes(54, -78, 16, 42, -10, fonce, 4))
    elif ailes == "ouvertes":
        m.append(_plumes(-76, -96, 16, 44, 60, fonce, 4))
        m.append(_plumes(76, -96, 16, 44, -60, fonce, 4))
    for sgn in (-1, 1):
        m.append(cercle(sgn * 22, -120, 26, radial([(0, eclaircir(visage, 0.5)), (0.75, visage), (1, _assombrir(visage, 0.85))])))
        m.append(cercle(sgn * 22, -120, 26, "none", stroke=_assombrir(visage, 0.8), stroke_width=2))
    ex, ey = 22, -120
    for sgn in (-1, 1):
        if ys in ("heureux", "fermes"):
            m.append(oeil(sgn * ex, ey, ys, regard, taille=1.3))
        else:
            k = 1.2 if ys == "grand" else 1.0
            m.append(cercle(sgn * ex, ey, 14 * k, "#fff", stroke=ENCRE, stroke_width=1.5))
            dy = 1.2 if ys == "bas" else 0
            m.append(cercle(sgn * ex + regard[0] * 4, ey + (regard[1] + dy) * 4, 8 * k, radial([(0, "#4a3418"), (0.6, ENCRE), (1, ENCRE)])))
            m.append(cercle(sgn * ex + regard[0] * 4 + 3, ey + (regard[1] + dy) * 4 - 3, 2.5, "#fff"))
    m.append(sourcils(22, -114, ss))
    m.append(poly([(-7, -108), (7, -108), (0, -94)], lineaire(["#ffc078", "#e67700"])))
    if bs in ("ouverte", "o", "crie", "baille"):
        m.append(poly([(-6, -96), (6, -96), (0, -88)], "#e67700"))
    elif bs in ("triste",):
        m.append(chemin("M -8 -84 Q 0 -90 8 -84", stroke=ENCRE, sw=2.5))
    if "lunettes" in acc:
        m.append(g([cercle(-ex, ey, 20, "none", stroke=ENCRE, stroke_width=3.5), cercle(ex, ey, 20, "none", stroke=ENCRE, stroke_width=3.5)]))
    if "echarpe" in acc:
        m.append(g([rect(-46, -100, 92, 16, cylindre("#fa5252", 0.3, 0.75, vertical=True), rx=8), chemin("M 18 -90 L 30 -48 L 14 -48 L 8 -90 Z", cylindre("#fa5252", 0.3, 0.75))]))
    occuper(x - 75 * s, y - 210 * s, x + 75 * s, y)
    return place(avec_contour(m, s, 0.35), x, y, s, flip=flip)


def escargot(x, y, s=1.0, coquille="#f59f00", corps="#b2f2bb", expr="sourire", flip=False, regard=(1, 0), acc=()):
    """Escargot de profil, la tête à droite. (x, y) = au sol, au milieu."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(coquille, 0.75)
    pied = "M -80 0 Q -84 -26 -50 -28 L 50 -30 Q 62 -30 66 -60 Q 70 -96 92 -96 Q 116 -96 116 -60 Q 116 -20 96 -6 Q 86 0 60 0 Z"
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(10, 0, 96, 8, 0.12))
    m += [chemin(pied, lineaire([(0, eclaircir(corps, 0.35)), (0.5, corps), (1, _assombrir(corps, 0.78))])),
          ombrage(chemin(pied, "#000"), sombre=[(10, 2, 100, 12), (112, -40, 14, 40)], clair=[(84, -84, 8, 5, -30)]),
          chemin("M -70 -8 Q 0 -14 60 -10", stroke=eclaircir(corps, 0.5), sw=2.5, opacity=0.6)]
    for dx, ang in ((82, -20), (104, 16)):
        a = math.radians(ang - 90)
        tx, ty = dx + math.cos(a) * 44, -92 + math.sin(a) * 44
        m.append(trait(dx, -92, tx, ty, _assombrir(corps, 0.85) if dx < 90 else corps, 7))
        m.append(cercle(tx, ty, 11, volume("#ffffff", 0, 0.85), stroke=ENCRE, stroke_width=1.5))
        if ys in ("heureux", "fermes"):
            m.append(oeil(tx, ty, ys, (0, 0), taille=0.7))
        else:
            m.append(cercle(tx + regard[0] * 3, ty + regard[1] * 3, 5.5, ENCRE))
            m.append(cercle(tx + regard[0] * 3 + 2, ty + regard[1] * 3 - 2, 1.8, "#fff"))
    m.append(ellipse(102, -58, 8, 5, ROSE, opacity=0.7))
    m.append(bouche(96, -48, bs, 0.8))
    # coquille bombée : spirale, stries de croissance, reflet
    m.append(cercle(-12, -72, 60, volume(coquille, 0.4, 0.68)))
    m.append(_decoupe(chemin(" ".join(f"M {n(-12 + math.cos(math.radians(a)) * 20)} {n(-72 + math.sin(math.radians(a)) * 20)} "
                                      f"L {n(-12 + math.cos(math.radians(a)) * 62)} {n(-72 + math.sin(math.radians(a)) * 62)}" for a in range(0, 360, 24)),
                             stroke=fonce, sw=2, opacity=0.25), cercle(-12, -72, 60, "#000")))
    m.append(chemin("M -12 -72 m 0 -8 a 8 8 0 1 1 -8 8 a 18 18 0 1 1 18 18 a 30 30 0 1 1 -30 -30 a 44 44 0 1 1 44 44", stroke=fonce, sw=7))
    m.append(chemin("M -12 -72 m 0 -8 a 8 8 0 1 1 -8 8 a 18 18 0 1 1 18 18 a 30 30 0 1 1 -30 -30 a 44 44 0 1 1 44 44",
                    stroke=eclaircir(coquille, 0.45), sw=2, opacity=0.6, transform="translate(-2 -3)"))
    m.append(chemin("M -56 -96 A 50 50 0 0 1 -20 -124", stroke="#fff", sw=6, opacity=0.4))
    if "chapeau" in acc:
        m.append(chapeau(92, -100, 0.6, "#4dabf7"))
    occuper(x - 90 * s, y - 120 * s, x + 90 * s, y)
    return place(avec_contour(m, s, 0.35), x, y, s, flip=flip)


def poisson(x, y, s=1.0, couleur="#ff922b", expr="sourire", flip=False, rot=0, bulles=False):
    """Poisson rouge, tête à droite. (x, y) = centre."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(couleur, 0.85)
    nageoire = lineaire([(0, (eclaircir(couleur, 0.35))), (1, _assombrir(couleur, 0.7))], 1, 0, 0, 0)
    corps = ellipse(0, 0, 48, 34, "#000")
    m = [chemin("M -40 0 L -80 -30 Q -70 0 -80 30 Z", nageoire),
         chemin("M -44 0 L -76 -20 M -44 0 L -78 0 M -44 0 L -76 20", stroke=_assombrir(couleur, 0.65), sw=1.5, opacity=0.6),
         chemin("M -10 -30 Q 5 -55 25 -34 Z", lineaire([eclaircir(couleur, 0.3), fonce])),
         ellipse(0, 0, 48, 34, volume(couleur, 0.38, 0.75))]
    # écailles en arcs, découpées au corps
    ecailles = " ".join(f"M {n(xx)} {n(yy)} q 6 6 0 12" for xx in range(-30, 14, 10) for yy in range(-24 + (xx // 10 % 2) * 6, 22, 12))
    m.append(_decoupe(chemin(ecailles, stroke=_assombrir(couleur, 0.7), sw=1.6, opacity=0.45), corps))
    m.append(ombrage(corps, sombre=[(10, 26, 50, 16)], clair=[(-6, -20, 20, 6, -8)], reflets=[(4, 32, 30, 4)]))
    m += [chemin("M -6 18 Q 4 30 16 22 Z", nageoire),
          chemin("M 8 -26 Q -2 0 8 26", stroke=fonce, sw=3)]
    m.append(oeil(26, -8, ys, (0.5, 0), taille=0.9))
    m.append(bouche(40, 8, bs, 0.5))
    if bulles:
        m += [cercle(62, -30, 6, "none", stroke="#fff", stroke_width=2.5), cercle(74, -54, 9, "none", stroke="#fff", stroke_width=2.5),
              cercle(60, -32, 1.8, "#fff"), cercle(71, -57, 2.5, "#fff")]
    return place(avec_contour(m, s, 0.35), x, y, s, flip=flip, rot=rot)


def tortue(x, y, s=1.0, carapace="#40c057", peau="#b2f2bb", expr="sourire", flip=False, regard=(1, 0)):
    """Tortue de profil, tête à droite. (x, y) = au sol, au milieu."""
    ys, bs, ss = EXPRESSIONS[expr]
    fonce = _assombrir(carapace, 0.75)
    peau_v = volume(peau, 0.35, 0.78)
    dome = "M -88 -24 Q -80 -120 0 -120 Q 80 -120 88 -24 Z"
    cou = "M 50 -40 Q 70 -60 90 -76 Q 124 -96 136 -64 Q 144 -36 110 -34 Q 84 -32 60 -24 Z"
    m = []
    if OMBRE_SOL[0]:
        m.append(ombre_sol(10, 0, 110, 10, 0.13))
    m += [ellipse(-50, -10, 16, 14, volume(_assombrir(peau, 0.85), 0.3, 0.75)), ellipse(40, -10, 16, 14, volume(_assombrir(peau, 0.85), 0.3, 0.75)),
          chemin(cou, lineaire([(0, eclaircir(peau, 0.3)), (0.5, peau), (1, _assombrir(peau, 0.8))])),
          chemin("M 70 -50 q 10 4 18 0 M 74 -40 q 10 4 18 0", stroke=_assombrir(peau, 0.75), sw=2, opacity=0.6),
          chemin(dome, volume(carapace, 0.3, 0.7))]
    # écailles bombées : chacune son reflet
    for px, py in [(-44, -60), (0, -84), (44, -60), (-6, -44)]:
        hexa = [(px - 20, py), (px - 10, py - 18), (px + 10, py - 18), (px + 20, py), (px + 10, py + 18), (px - 10, py + 18)]
        m.append(poly(hexa, fonce, opacity=0.55))
        m.append(poly([(px - 14, py), (px - 7, py - 12), (px + 7, py - 12), (px + 14, py), (px + 7, py + 12), (px - 7, py + 12)],
                      volume(eclaircir(carapace, 0.1), 0.35, 0.8)))
    m.append(ombrage(chemin(dome, "#000"), sombre=[(60, -30, 60, 40)], clair=[(-40, -100, 26, 9, -20)], reflets=[(86, -40, 8, 20)]))
    m += [rect(-94, -30, 188, 14, cylindre(fonce, 0.3, 0.7, vertical=True), rx=7),
          chemin(" ".join(f"M {xx} -30 v 14" for xx in range(-70, 90, 28)), stroke=_assombrir(fonce, 0.7), sw=2, opacity=0.6)]
    m.append(ellipse(-24, -14, 16, 14, peau_v))
    m.append(ellipse(22, -14, 16, 14, peau_v))
    m.append(chemin("M -32 -2 v 4 M -24 -1 v 4 M 14 -2 v 4 M 22 -1 v 4", stroke=_assombrir(peau, 0.6), sw=2))
    m.append(oeil(114, -70, ys, regard, taille=0.9))
    m.append(ellipse(124, -52, 7, 4.5, ROSE, opacity=0.7))
    m.append(bouche(126, -46, bs, 0.7))
    occuper(x - 110 * s, y - 110 * s, x + 110 * s, y)
    return place(avec_contour(m, s, 0.35), x, y, s, flip=flip)


def faisceau(x0, y0, x1, y1, r, fill="#000", **a):
    """Cône de lumière d'une lampe (x0, y0) vers un disque de rayon r en (x1, y1)."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    px, py = -dy / L, dx / L
    pts = [(x0 + px * 8, y0 + py * 8), (x1 + px * r, y1 + py * r), (x1 - px * r, y1 - py * r), (x0 - px * 8, y0 - py * 8)]
    return poly(pts, fill, **a) + cercle(x1, y1, r, fill, **a)


def obscurite(S, trous=(), couleur="#0b1433", opacity=0.82):
    """Assombrit toute la scène, sauf les formes `trous` (dessinées en noir)."""
    mid = uid("k")
    S.defs.append(el("mask", rect(0, 0, S.w, S.h, "#fff") + "".join(trous), id=mid))
    S.add(rect(0, 0, S.w, S.h, couleur, opacity=opacity, mask=f"url(#{mid})"))


def trou_doux(x, y, r, force="#000"):
    """Trou à bords flous pour obscurite() : `force` = #000 (plein jour) à #fff (rien)."""
    i = uid("t")
    grad = el("radialGradient", el("stop", offset="0", stop_color=force) + el("stop", offset="0.55", stop_color=force)
              + el("stop", offset="1", stop_color="#fff"), id=i)
    return grad + cercle(x, y, r, f"url(#{i})")


assombrir = _assombrir
