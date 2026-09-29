"""Vérifie les images de tous les livres, y compris les livres hors catalogue.

    python3 outils/verifier-images.py

Python et Node suffisent ; aucune dépendance à installer.
"""
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

RACINE = Path(__file__).resolve().parents[1]
INVENTAIRE = r"""
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = process.argv[1];
const context = {window: {}};
vm.runInNewContext(fs.readFileSync(path.join(root, 'livres/catalogue.js'), 'utf8'), context);
const books = [];
for (const folder of fs.readdirSync(path.join(root, 'livres')).sort()) {
  const filename = path.join(root, 'livres', folder, 'livre.js');
  if (!fs.existsSync(filename)) continue;
  vm.runInNewContext(fs.readFileSync(filename, 'utf8'), {
    Bibliotheque: {ajouter(book) {books.push({...book, folder});}}
  }, {filename, timeout: 1000});
}
process.stdout.write(JSON.stringify({catalogue: context.window.CATALOGUE, books}));
"""


def verifier():
    resultat = subprocess.run(
        ["node", "-e", INVENTAIRE, str(RACINE)],
        capture_output=True, text=True, check=True,
    )
    inventaire = json.loads(resultat.stdout)
    erreurs = []
    catalogue = inventaire["catalogue"]
    livres = inventaire["books"]
    ids = [livre["id"] for livre in livres]
    if len(catalogue) != len(set(catalogue)):
        erreurs.append("Identifiant répété dans le catalogue.")
    if len(ids) != len(set(ids)):
        erreurs.append("Identifiant de livre répété.")
    for identifiant in set(catalogue) - set(ids):
        erreurs.append(f"{identifiant} : livre du catalogue introuvable.")

    images = set()
    for livre in livres:
        dossier = RACINE / "livres" / livre["folder"]
        if livre["id"] != livre["folder"]:
            erreurs.append(f"{livre['folder']} : identifiant différent du dossier.")
        for page in livre["pages"]:
            source = page.get("image")
            if not source:
                continue
            image = (dossier / source).resolve()
            if not image.is_relative_to(dossier):
                erreurs.append(f"{livre['id']} : image extérieure au dossier ({source}).")
            elif not image.is_file():
                erreurs.append(f"{livre['id']} : image manquante ({source}).")
            else:
                images.add(image)

    # Vérifier aussi les fichiers présents qui ne sont pas référencés.
    svgs = sorted((RACINE / "livres").glob("*/images/*.svg"))
    for image in svgs:
        nom = image.relative_to(RACINE)
        try:
            svg = ET.parse(image).getroot()
            if svg.tag != "{http://www.w3.org/2000/svg}svg":
                raise ValueError("racine SVG ou espace de noms absent")
            cadre = [float(v) for v in svg.attrib.get("viewBox", "").split()]
            if len(cadre) != 4 or not all(math.isfinite(v) for v in cadre) or cadre[2] <= 0 or cadre[3] <= 0:
                raise ValueError("viewBox absent ou invalide")
            identifiers = [el.attrib["id"] for el in svg.iter() if "id" in el.attrib]
            if len(identifiers) != len(set(identifiers)):
                raise ValueError("identifiant SVG répété")
            refs = set()
            for el in svg.iter():
                for attr, value in el.attrib.items():
                    refs.update(re.findall(r"url\(#([^)]*)\)", value))
                    if attr in ("href", "{http://www.w3.org/1999/xlink}href") and value.startswith("#"):
                        refs.add(value[1:])
            if refs - set(identifiers):
                raise ValueError(f"référence SVG absente : {', '.join(sorted(refs - set(identifiers)))}")
        except (ET.ParseError, ValueError) as erreur:
            erreurs.append(f"{nom} : {erreur}.")

    for erreur in erreurs:
        print(erreur, file=sys.stderr)
    pages = sum(len(livre["pages"]) for livre in livres)
    print(f"{len(livres)} livres, {pages} pages, {len(images)} images référencées, {len(svgs)} SVG vérifiés.")
    hors_catalogue = sorted(set(ids) - set(catalogue))
    if hors_catalogue:
        print(f"Livres hors catalogue : {', '.join(hors_catalogue)}.")
    print(f"{len(erreurs)} erreur(s).")
    return bool(erreurs)


if __name__ == "__main__":
    sys.exit(verifier())
