"""Morpion (tic-tac-toe) contre l'ordinateur.

La grille est une liste de 3 listes de 3 cases. L'IA suit des règles simples :
gagner si possible, sinon bloquer, sinon prendre le centre, un coin, puis le reste.

Lancer avec : python morpion.py
"""

import random

VIDE = " "


def creer_grille():
    return [[VIDE] * 3 for _ in range(3)]


def afficher(grille):
    print()
    for i, ligne in enumerate(grille):
        print(" " + " | ".join(ligne))
        if i < 2:
            print("---+---+---")
    print()


def lignes_gagnantes(grille):
    """Renvoie les 8 alignements possibles (3 lignes, 3 colonnes, 2 diagonales)."""
    lignes = [grille[i] for i in range(3)]
    colonnes = [[grille[i][j] for i in range(3)] for j in range(3)]
    diagonales = [[grille[i][i] for i in range(3)], [grille[i][2 - i] for i in range(3)]]
    return lignes + colonnes + diagonales


def gagnant(grille):
    for alignement in lignes_gagnantes(grille):
        if alignement[0] != VIDE and alignement.count(alignement[0]) == 3:
            return alignement[0]
    return None


def cases_libres(grille):
    return [(i, j) for i in range(3) for j in range(3) if grille[i][j] == VIDE]


def demander_case(grille):
    """Le joueur saisit un numéro de case de 1 à 9 (comme un pavé numérique de téléphone)."""
    libres = cases_libres(grille)
    while True:
        saisie = input("Ta case (1-9) : ")
        if saisie.isdigit() and 1 <= int(saisie) <= 9:
            numero = int(saisie) - 1
            case = (numero // 3, numero % 3)
            if case in libres:
                return case
        print("Case invalide ou déjà prise.")


def coup_gagnant(grille, symbole):
    """Renvoie une case qui fait gagner `symbole` immédiatement, ou None."""
    for i, j in cases_libres(grille):
        grille[i][j] = symbole
        gagne = gagnant(grille) == symbole
        grille[i][j] = VIDE
        if gagne:
            return (i, j)
    return None


def coup_ordi(grille, ordi="O", joueur="X"):
    for symbole in (ordi, joueur):           # 1. gagner, 2. bloquer
        case = coup_gagnant(grille, symbole)
        if case:
            return case
    if grille[1][1] == VIDE:                  # 3. centre
        return (1, 1)
    coins = [c for c in [(0, 0), (0, 2), (2, 0), (2, 2)] if c in cases_libres(grille)]
    if coins:                                 # 4. un coin
        return random.choice(coins)
    return random.choice(cases_libres(grille))  # 5. le reste


def jouer():
    grille = creer_grille()
    tour_joueur = True
    print("Tu joues les X. Cases numérotées de 1 (en haut à gauche) à 9 (en bas à droite).")

    while cases_libres(grille) and not gagnant(grille):
        afficher(grille)
        if tour_joueur:
            i, j = demander_case(grille)
            grille[i][j] = "X"
        else:
            i, j = coup_ordi(grille)
            grille[i][j] = "O"
            print(f"L'ordinateur joue la case {i * 3 + j + 1}.")
        tour_joueur = not tour_joueur

    afficher(grille)
    vainqueur = gagnant(grille)
    if vainqueur == "X":
        print("🎉 Tu as gagné !")
    elif vainqueur == "O":
        print("🤖 L'ordinateur a gagné.")
    else:
        print("🤝 Match nul.")


if __name__ == "__main__":
    jouer()
