"""Crée les fichiers livre.js et les modules de dessin des dix fêtes.

    python3 outils/illustrer/creer_livres_fetes.py
    python3 outils/illustrer/generer.py

Les textes et indications d'images se modifient dans livres_fetes.py.
"""

import json
from pathlib import Path

from livres_fetes import LIVRES

RACINE = Path(__file__).resolve().parents[2]
HISTOIRES = Path(__file__).resolve().parent / "histoires"


def creer(livre):
    identifiant = livre["id"]
    pages = [
        {"type": "couverture", "image": "images/couverture.svg",
         "description": livre["pages"][0][2]},
        {"type": "titre", "image": "images/vignette.svg", "texte": livre["dedicace"]},
    ]
    for numero, (_, texte, description) in enumerate(livre["pages"], 1):
        pages.append({"image": f"images/{numero:02d}.svg", "description": description,
                      "texte": texte})
    pages.extend([{"type": "texte", "texte": "Fin"},
                  {"type": "quatrieme", "image": "images/vignette.svg"}])
    contenu = {"id": identifiant, "rayon": "fetes", "titre": livre["titre"],
               "sousTitre": livre["sousTitre"], "age": livre["age"],
               "couleur": livre["couleur"], "resume": livre["resume"],
               "pages": pages}
    dossier = RACINE / "livres" / identifiant
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "livre.js").write_text(
        "Bibliotheque.ajouter(" + json.dumps(contenu, ensure_ascii=False, indent=2) + ");\n",
        encoding="utf-8")
    module = HISTOIRES / f"{identifiant.replace('-', '_')}.py"
    module.write_text(
        f'"""Illustrations du livre {livre["titre"]}."""\n'
        'from fetes import images_pour\n\n'
        f'ID = "{identifiant}"\n'
        'IMAGES = images_pour(ID)\n', encoding="utf-8")
    print(identifiant)


if __name__ == "__main__":
    for livre in LIVRES:
        creer(livre)
