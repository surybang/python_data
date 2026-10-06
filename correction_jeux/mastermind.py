"""Mastermind.

L'ordinateur choisit une combinaison secrète de 4 couleurs (répétitions
possibles) parmi 6. Le joueur a 10 essais. Après chaque essai, il apprend
combien de couleurs sont bien placées, et combien sont présentes mais mal placées.

Lancer avec : python mastermind.py
"""

import random

COULEURS = ["R", "V", "B", "J", "O", "N"]   # rouge, vert, bleu, jaune, orange, noir
LONGUEUR = 4
ESSAIS_MAX = 10


def evaluer(secret, essai):
    """Renvoie le tuple (bien_places, mal_places)."""
    bien_places = 0
    restes_secret = []
    restes_essai = []
    for s, e in zip(secret, essai):
        if s == e:
            bien_places += 1
        else:
            restes_secret.append(s)
            restes_essai.append(e)

    mal_places = 0
    for couleur in restes_essai:
        if couleur in restes_secret:
            mal_places += 1
            restes_secret.remove(couleur)
    return bien_places, mal_places


def combinaison_valide(saisie):
    return len(saisie) == LONGUEUR and all(c in COULEURS for c in saisie)


def demander_combinaison():
    texte = f"Ta combinaison ({LONGUEUR} lettres parmi {' '.join(COULEURS)}) : "
    saisie = input(texte).strip().upper().replace(" ", "")
    while not combinaison_valide(saisie):
        saisie = input("Combinaison invalide. " + texte).strip().upper().replace(" ", "")
    return list(saisie)


def afficher_indices(bien, mal):
    return f"{'●' * bien}{'○' * mal}  ({bien} bien placée(s), {mal} mal placée(s))"


def jouer():
    secret = [random.choice(COULEURS) for _ in range(LONGUEUR)]
    historique = []

    for numero in range(1, ESSAIS_MAX + 1):
        essai = demander_combinaison()
        bien, mal = evaluer(secret, essai)
        historique.append((essai, bien, mal))

        print(f"\nEssai {numero} : {''.join(essai)}  ->  {afficher_indices(bien, mal)}")

        if bien == LONGUEUR:
            print(f"🎉 Trouvé en {numero} essai(s) !")
            return

    print(f"\n😢 Perdu, la combinaison était {''.join(secret)}.")
    print("Historique de tes essais :")
    for essai, bien, mal in historique:
        print(f"  {''.join(essai)}  ->  {afficher_indices(bien, mal)}")


if __name__ == "__main__":
    jouer()
