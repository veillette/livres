#!/usr/bin/env python3
"""Écrire `livres/nouveautes.js` : les vingt livres ajoutés ou revus le plus récemment.

La date d'un livre se lit dans l'historique git : dernier commit qui touche
son texte (`livres/<id>/livre.js`) ou son script de dessin
(`outils/illustrer/histoires/<id>.py`, tirets → soulignés). Un commit qui
touche plus de SEUIL livres à la fois (finition partagée, rangement…) n'est
pas compté comme une reprise, sauf pour les livres qu'il crée. Les fichiers
modifiés mais pas encore validés comptent pour aujourd'hui : on peut donc
lancer ce script avant le commit qui ajoute un livre.

    python3 outils/nouveautes.py            # réécrire livres/nouveautes.js
    python3 outils/nouveautes.py --verifier # dire si le fichier est à jour

Sans historique complet (clone superficiel), le fichier n'est pas réécrit.
"""

import datetime
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "livres" / "nouveautes.js"
NOMBRE = 20
SEUIL = 10  # au-delà, un commit est une retouche d'ensemble

MOTIF_LIVRE = re.compile(r"^livres/([a-z0-9-]+)/livre\.js$")
MOTIF_HISTOIRE = re.compile(r"^outils/illustrer/histoires/([a-z0-9_]+)\.py$")


def git(*args):
    return subprocess.run(["git", *args], cwd=RACINE, capture_output=True, text=True, check=True).stdout


def catalogue():
    texte = (RACINE / "livres" / "catalogue.js").read_text(encoding="utf-8")
    liste = re.search(r"CATALOGUE\s*=\s*\[([\s\S]*?)\]", texte)
    return re.findall(r"[\"']([a-z0-9-]+)[\"']", liste.group(1))


def livre_du_fichier(chemin, ids):
    m = MOTIF_LIVRE.match(chemin)
    if m:
        return m.group(1)
    m = MOTIF_HISTOIRE.match(chemin)
    if m:
        return ids.get(m.group(1))
    return None


def commits(ids):
    """Liste (horodatage, {id: statut}) du plus récent au plus ancien ; statut A = créé."""
    sortie = git(
        "log", "--no-merges", "--format=@%ct", "--name-status", "--no-renames",
        "--", "livres/*/livre.js", "outils/illustrer/histoires/*.py",
    )
    resultat = []
    for bloc in sortie.split("@")[1:]:
        lignes = bloc.strip().splitlines()
        touches = {}
        for ligne in lignes[1:]:
            statut, _, chemin = ligne.partition("\t")
            livre = livre_du_fichier(chemin, ids)
            if livre:
                # Création du texte du livre : c'est sa naissance.
                cree = statut == "A" and MOTIF_LIVRE.match(chemin)
                touches[livre] = "A" if cree or touches.get(livre) == "A" else "M"
        if touches:
            resultat.append((int(lignes[0]), touches))
    return resultat


def en_cours(ids):
    """Livres dont le texte ou le dessin est modifié sans être validé."""
    sortie = git("status", "--porcelain", "--untracked-files=all", "--", "livres", "outils/illustrer/histoires")
    touches = {}
    for ligne in sortie.splitlines():
        livre = livre_du_fichier(ligne[3:], ids)
        if livre:
            nouveau = ligne[:2] in ("??", "A ") and MOTIF_LIVRE.match(ligne[3:])
            touches[livre] = "A" if nouveau or touches.get(livre) == "A" else "M"
    return touches


def jour(horodatage):
    return datetime.datetime.fromtimestamp(horodatage, datetime.timezone.utc).date()


def nouveautes():
    liste = catalogue()
    ids = {i.replace("-", "_"): i for i in liste}
    maintenant = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
    lots = [(maintenant, en_cours(ids))] + commits(ids)  # du plus récent au plus ancien
    dates, naissances = {}, {}
    for horodatage, touches in lots:
        retouche = len(touches) > SEUIL
        for livre, statut in touches.items():
            if statut == "A":
                naissances.setdefault(livre, horodatage)
            if livre not in dates and (statut == "A" or not retouche):
                dates[livre] = horodatage
    ordre = {livre: rang for rang, livre in enumerate(liste)}
    tries = sorted((l for l in dates if l in ordre), key=lambda l: (-dates[l], ordre[l]))
    return [
        {
            "id": livre,
            "date": jour(dates[livre]).isoformat(),
            # « nouveau » s'il est né le jour de sa dernière modification.
            "etat": "nouveau" if livre in naissances and jour(naissances[livre]) == jour(dates[livre]) else "revu",
        }
        for livre in tries[:NOMBRE]
    ]


def contenu(liste):
    lignes = "".join(f'  {{ id: "{e["id"]}", date: "{e["date"]}", etat: "{e["etat"]}" }},\n' for e in liste)
    return (
        "/*\n"
        " * Nouveautés : les livres ajoutés ou revus le plus récemment, du plus\n"
        " * récent au plus ancien. Fichier écrit par `python3 outils/nouveautes.py`\n"
        " * d'après l'historique git : ne pas le modifier à la main.\n"
        " */\n"
        f"window.NOUVEAUTES = [\n{lignes}];\n"
    )


def main():
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        print("Historique git incomplet (clone superficiel) : livres/nouveautes.js n'est pas réécrit.")
        return 0
    texte = contenu(nouveautes())
    ancien = SORTIE.read_text(encoding="utf-8") if SORTIE.exists() else ""
    if "--verifier" in sys.argv:
        if texte != ancien:
            print("livres/nouveautes.js n'est pas à jour : lancer python3 outils/nouveautes.py")
            return 1
        print("livres/nouveautes.js est à jour.")
        return 0
    SORTIE.write_text(texte, encoding="utf-8")
    print(f"livres/nouveautes.js écrit ({texte.count('id:')} livres).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
