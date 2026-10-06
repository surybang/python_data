"""Blackjack simplifié contre le croupier.

Règles : as = 1 ou 11, figures = 10. Le joueur tire tant qu'il veut,
le croupier tire jusqu'à atteindre au moins 17. Au-delà de 21, on perd.

Lancer avec : python blackjack.py
"""

import random

VALEURS = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
           "10": 10, "V": 10, "D": 10, "R": 10, "A": 11}
COULEURS = ["♠", "♥", "♦", "♣"]


def creer_paquet():
    """Renvoie un paquet de 52 cartes mélangé, sous forme de tuples (rang, couleur)."""
    paquet = []
    for couleur in COULEURS:
        for rang in VALEURS:
            paquet.append((rang, couleur))
    random.shuffle(paquet)
    return paquet


def valeur_main(main):
    """Calcule la valeur d'une main, en comptant les as à 1 si nécessaire."""
    total = 0
    nb_as = 0
    for rang, _ in main:
        total += VALEURS[rang]
        if rang == "A":
            nb_as += 1
    while total > 21 and nb_as > 0:
        total -= 10        # un as passe de 11 à 1
        nb_as -= 1
    return total


def afficher_main(nom, main):
    cartes = " ".join(f"{rang}{couleur}" for rang, couleur in main)
    print(f"{nom} : {cartes}  → {valeur_main(main)}")


def tour_croupier(paquet, main):
    while valeur_main(main) < 17:
        main.append(paquet.pop())
    return main


def resultat(main_joueur, main_croupier):
    """Renvoie "gagné", "perdu" ou "égalité"."""
    joueur, croupier = valeur_main(main_joueur), valeur_main(main_croupier)
    if joueur > 21:
        return "perdu"
    if croupier > 21 or joueur > croupier:
        return "gagné"
    if joueur == croupier:
        return "égalité"
    return "perdu"


def jouer():
    paquet = creer_paquet()
    main_joueur = [paquet.pop(), paquet.pop()]
    main_croupier = [paquet.pop(), paquet.pop()]
    print(f"Le croupier montre : {main_croupier[0][0]}{main_croupier[0][1]}")

    while valeur_main(main_joueur) < 21:
        afficher_main("Ta main", main_joueur)
        choix = input("(t)irer ou (r)ester ? ").strip().lower()
        if choix == "t":
            main_joueur.append(paquet.pop())
        elif choix == "r":
            break

    afficher_main("Ta main", main_joueur)
    if valeur_main(main_joueur) <= 21:
        tour_croupier(paquet, main_croupier)
    afficher_main("Croupier", main_croupier)
    print(f"Résultat : {resultat(main_joueur, main_croupier)}")


if __name__ == "__main__":
    jouer()
