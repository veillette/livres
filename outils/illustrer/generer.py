"""
Génère les illustrations SVG des livres.

    python3 outils/illustrer/generer.py              # tous les livres
    python3 outils/illustrer/generer.py ours-gateau  # un seul livre

Chaque livre est décrit dans `histoires/<id_avec_soulignés>.py` : une
variable ID et une liste IMAGES de couples (nom de fichier, fonction qui
renvoie une Scene). Les images sont écrites dans `livres/<id>/images/`.

Les SVG ne sont pas suivis par git : la publication les régénère. Le fichier
`empreintes.txt`, lui, est suivi : une ligne par image (empreinte SHA-256
abrégée, puis `<id>/<nom>`), réécrite à chaque génération. Son diff montre
quelles images ont changé ; un changement inattendu dans un autre livre est
une régression.
"""
import hashlib
import importlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)

import base  # noqa: E402

EMPREINTES = os.path.join(ICI, "empreintes.txt")


def empreinte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()[:16]


def lire_empreintes():
    """{"<id>/<nom>": empreinte} du fichier suivi par git (vide s'il manque)."""
    if not os.path.exists(EMPREINTES):
        return {}
    with open(EMPREINTES, encoding="utf-8") as fh:
        return {chemin: valeur for valeur, chemin in (ligne.split() for ligne in fh if ligne.strip())}


def ecrire_empreintes(empreintes):
    with open(EMPREINTES, "w", encoding="utf-8", newline="\n") as fh:
        for chemin in sorted(empreintes):
            fh.write(f"{empreintes[chemin]}  {chemin}\n")


def modules():
    for nom in sorted(os.listdir(os.path.join(ICI, "histoires"))):
        if nom.endswith(".py") and not nom.startswith("_"):
            yield importlib.import_module(f"histoires.{nom[:-3]}")


def champ(id_livre, nom):
    """Champ simple du livre.js (rayon, couleur…) ; None s'il n'existe pas encore."""
    chemin = os.path.join(RACINE, "livres", id_livre, "livre.js")
    if not os.path.exists(chemin):
        return None
    with open(chemin, encoding="utf-8") as fh:
        m = re.search(rf'\n  {nom}:\s*"([^"]+)"', fh.read())
    return m.group(1) if m else None


def rayon(id_livre):
    return champ(id_livre, "rayon")


# Patine de vieux papier (glacis de la finition, voir base.py) : seulement
# pour les récits anciens, et presque blanche pour garder des couleurs vives.
GLACIS_RAYON = {
    "fables": "#fdf5e4",
    "contes": "#fef7ee",
}


MOTIFS_PAPIER = ("rayures", "pois", "fleurs", "losanges", "etoiles")


def glacis(id_livre, module):
    if hasattr(module, "GLACIS"):
        return module.GLACIS
    return GLACIS_RAYON.get(rayon(id_livre))


def regler(module):
    """Réglages partagés propres au livre, avant de dessiner ses pages."""
    # numérotation des identifiants SVG propre à chaque livre : le résultat ne
    # dépend pas des autres livres générés en même temps
    base._compteur[0] = 0
    # pas d'ombre douce sous les personnages si le livre dessine ses ombres
    base.OMBRE_SOL[0] = getattr(module, "OMBRES_DOUCES", True)
    # modelé automatique des aplats, sauf si le livre le refuse
    base.RELIEF_AUTO[0] = getattr(module, "RELIEF", True)
    # ombre douce orientée (lumière à gauche), sauf dans les livres de sciences
    sciences = rayon(module.ID) == "sciences"
    base.OMBRE_SENS[0] = getattr(module, "SENS_OMBRE", 0 if sciences else 1)
    # finition : glacis du livre, lumière d'ambiance (ni halo ni teinte en
    # sciences : l'éclairage et les couleurs y sont physiques), petite bête cachée
    base.GLACIS_PAGE[0] = glacis(module.ID, module)
    base.LUMIERE_PAGE[0] = getattr(module, "LUMIERE", not sciences)
    base.BETE_CACHEE[0] = getattr(module, "CACHE", "coccinelle")
    # papier peint propre au livre : les intérieurs ne se ressemblent plus tous
    base.MOTIF_PAPIER[0] = getattr(module, "PAPIER_PEINT", MOTIFS_PAPIER[int(hashlib.md5(module.ID.encode()).hexdigest()[:6], 16) % len(MOTIFS_PAPIER)])


def generer(module):
    regler(module)
    dossier = os.path.join(RACINE, "livres", module.ID, "images")
    scenes = [(nom, fabrique()) for nom, fabrique in module.IMAGES]
    note = ""
    if base.BETE_CACHEE[0]:
        # la petite bête est un jeu : elle doit être sur toutes les pages
        # pleines du livre, sinon elle n'est sur aucune (S.cachette(x, y)
        # complète une page sans cachette proposée par le décor)
        # (une page peut se mettre hors du jeu avec S.cachette(None) : une
        # page dans l'espace, où une coccinelle n'a rien à faire)
        pleines = [(nom, S) for nom, S in scenes if S.w >= 600 and S._cachette is not False]
        sans = [nom for nom, S in pleines if not S._bete(nom)]
        if sans:
            base.BETE_CACHEE[0] = None
            note = f" (petite bête absente : pas de cachette sur {', '.join(sans)})"
    empreintes = {}
    for nom, S in scenes:
        empreintes[f"{module.ID}/{nom}"] = empreinte(S.enregistrer(os.path.join(dossier, nom)))
    print(f"{module.ID} : {len(module.IMAGES)} images{note}")
    return empreintes


if __name__ == "__main__":
    voulus = set(sys.argv[1:])
    # tous les livres : le fichier est réécrit en entier (un livre retiré en
    # disparaît) ; quelques livres : seules leurs lignes sont remplacées
    empreintes = {} if not voulus else {
        chemin: valeur for chemin, valeur in lire_empreintes().items()
        if chemin.split("/")[0] not in voulus
    }
    for m in modules():
        if not voulus or m.ID in voulus:
            empreintes.update(generer(m))
    ecrire_empreintes(empreintes)
