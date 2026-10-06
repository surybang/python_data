"""Pierre-feuille-ciseaux contre l'ordinateur.

Lancer avec : python pierre_feuille_ciseaux.py
"""

import random

COUPS = ["pierre", "feuille", "ciseaux"]
BAT = {"pierre": "ciseaux", "feuille": "pierre", "ciseaux": "feuille"}  # clé bat valeur
CONTRE = {"pierre": "feuille", "feuille": "ciseaux", "ciseaux": "pierre"}  # coup qui bat la clé


def demander_coup():
    """Redemande tant que le coup saisi n'est pas valide."""
    coup = input("pierre, feuille ou ciseaux ? ").strip().lower()
    while coup not in COUPS:
        coup = input("Coup invalide. pierre, feuille ou ciseaux ? ").strip().lower()
    return coup


def gagnant(coup_joueur, coup_ordi):
    """Renvoie "joueur", "ordi" ou "égalité"."""
    if coup_joueur == coup_ordi:
        return "égalité"
    if BAT[coup_joueur] == coup_ordi:
        return "joueur"
    return "ordi"


# Bonus pour les plus curieux
def coup_ordi_malin(historique):
    """Joue le coup qui bat le coup préféré du joueur jusqu'ici."""
    if not historique:
        return random.choice(COUPS)
    compteur = {}
    for coup in historique:
        compteur[coup] = compteur.get(coup, 0) + 1
    favori = None
    for coup, nb in compteur.items():
        if favori is None or nb > compteur[favori]:
            favori = coup
    return CONTRE[favori]


def jouer(nb_manches=5, ia_maligne=True):
    scores = {"joueur": 0, "ordi": 0, "égalité": 0}
    historique = []

    for manche in range(1, nb_manches + 1):
        print(f"\n--- Manche {manche}/{nb_manches} ---")
        coup_ordi = coup_ordi_malin(historique) if ia_maligne else random.choice(COUPS)
        coup_joueur = demander_coup()
        historique.append(coup_joueur)

        resultat = gagnant(coup_joueur, coup_ordi)
        scores[resultat] += 1
        print(f"L'ordinateur a joué {coup_ordi} → {resultat}")

    print(f"\nScore final : toi {scores['joueur']} - {scores['ordi']} ordi ({scores['égalité']} égalité(s))")


if __name__ == "__main__":
    jouer()
