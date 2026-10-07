"""
Génère les illustrations SVG des livres.

    python3 outils/illustrer/generer.py              # tous les livres
    python3 outils/illustrer/generer.py ours-gateau  # un seul livre

Chaque livre est décrit dans `histoires/<id_avec_soulignés>.py` : une
variable ID et une liste IMAGES de couples (nom de fichier, fonction qui
renvoie une Scene). Les images sont écrites dans `livres/<id>/images/`.
"""
import importlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)

import base  # noqa: E402


def modules():
    for nom in sorted(os.listdir(os.path.join(ICI, "histoires"))):
        if nom.endswith(".py") and not nom.startswith("_"):
            yield importlib.import_module(f"histoires.{nom[:-3]}")


def rayon(id_livre):
    """Rayon du livre, lu dans son livre.js (None s'il n'existe pas encore)."""
    chemin = os.path.join(RACINE, "livres", id_livre, "livre.js")
    if not os.path.exists(chemin):
        return None
    with open(chemin, encoding="utf-8") as fh:
        m = re.search(r'rayon:\s*"([^"]+)"', fh.read())
    return m.group(1) if m else None


def generer(module):
    # numérotation des identifiants SVG propre à chaque livre : le résultat ne
    # dépend pas des autres livres générés en même temps
    base._compteur[0] = 0
    # pas d'ombre douce sous les personnages si le livre dessine ses ombres
    base.OMBRE_SOL[0] = getattr(module, "OMBRES_DOUCES", True)
    # modelé automatique des aplats, sauf si le livre le refuse
    base.RELIEF_AUTO[0] = getattr(module, "RELIEF", True)
    # ombre douce orientée (lumière à gauche), sauf dans les livres de sciences
    base.OMBRE_SENS[0] = getattr(module, "SENS_OMBRE", 0 if rayon(module.ID) == "sciences" else 1)
    dossier = os.path.join(RACINE, "livres", module.ID, "images")
    for nom, fabrique in module.IMAGES:
        fabrique().enregistrer(os.path.join(dossier, nom))
    print(f"{module.ID} : {len(module.IMAGES)} images")


if __name__ == "__main__":
    voulus = set(sys.argv[1:])
    for m in modules():
        if not voulus or m.ID in voulus:
            generer(m)
