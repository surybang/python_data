"""Le pendu.

Bonus : quelles lettres proposer en premier ? On compte leurs fréquences.

Lancer avec : python pendu.py
"""

import random

MOTS = ["python", "variable", "boucle", "fonction", "liste", "dictionnaire",
        "tuple", "ensemble", "condition", "algorithme", "donnees", "script"]
ERREURS_MAX = 7


def afficher_mot(mot, lettres_trouvees):
    """Renvoie le mot avec des _ à la place des lettres non trouvées."""
    affichage = []
    for lettre in mot:
        affichage.append(lettre if lettre in lettres_trouvees else "_")
    return " ".join(affichage)


def mot_trouve(mot, lettres_trouvees):
    """Renvoie True si toutes les lettres du mot ont été trouvées."""
    for lettre in mot:
        if lettre not in lettres_trouvees:
            return False
    return True


def demander_lettre(deja_jouees):
    """Redemande tant que la saisie n'est pas une lettre nouvelle."""
    lettre = input("Une lettre : ").strip().lower()
    while len(lettre) != 1 or not lettre.isalpha() or lettre in deja_jouees:
        if lettre in deja_jouees:
            lettre = input("Déjà jouée ! Une autre lettre : ").strip().lower()
        else:
            lettre = input("Une seule lettre, s'il te plaît : ").strip().lower()
    return lettre


def jouer():
    mot = random.choice(MOTS)
    deja_jouees = set()
    erreurs = 0

    while erreurs < ERREURS_MAX:
        print(f"\n{afficher_mot(mot, deja_jouees)}   (erreurs : {erreurs}/{ERREURS_MAX})")
        lettre = demander_lettre(deja_jouees)
        deja_jouees.add(lettre)

        if lettre in mot:
            print("Bien vu ✅")
        else:
            erreurs += 1
            print("Raté ❌")

        if mot_trouve(mot, deja_jouees):
            print(f"\n🎉 Gagné ! Le mot était « {mot} ».")
            return
    print(f"\n💀 Pendu ! Le mot était « {mot} ».")


if __name__ == "__main__":
    jouer()
