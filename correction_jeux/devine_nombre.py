"""Le génie : devine le nombre.

Partie 1 : le joueur devine un nombre tiré au hasard par l'ordinateur.
Partie 2 : l'ordinateur devine, avec la stratégie de son choix.

Lancer avec : python devine_nombre.py
"""

import random

BORNE_MIN = 1
BORNE_MAX = 100
ESSAIS_MAX = 10


# --- Utilitaires de saisie ------------------------------------------------

def demander_nombre(message, min_val=None, max_val=None):
    """Redemande une saisie tant que ce n'est pas un entier valide.

    Args:
        message: Le texte affiché à l'utilisateur.
        min_val: Borne minimale acceptée (incluse), ou None.
        max_val: Borne maximale acceptée (incluse), ou None.

    Returns:
        Le nombre saisi, converti en int.
    """
    while True:
        saisie = input(message)
        if not saisie.lstrip("-").isdigit():
            print("Ce n'est pas un nombre entier, réessaie.")
            continue
        valeur = int(saisie)
        if min_val is not None and valeur < min_val:
            print(f"Le nombre doit être supérieur ou égal à {min_val}.")
            continue
        if max_val is not None and valeur > max_val:
            print(f"Le nombre doit être inférieur ou égal à {max_val}.")
            continue
        return valeur


def demander_choix(message, choix_valides):
    """Demande à l'utilisateur de choisir parmi une liste de choix.

    Args:
        message: Le texte affiché.
        choix_valides: Une liste de chaînes acceptées (comparaison insensible à la casse).

    Returns:
        Le choix validé (en minuscules).
    """
    while True:
        saisie = input(message).strip().lower()
        if saisie in choix_valides:
            return saisie
        print(f"Choix invalide. Options : {', '.join(choix_valides)}")


# --- Partie 1 : le joueur devine ------------------------------------------

def jouer():
    """Lance une partie où le joueur devine le nombre secret."""
    secret = random.randint(BORNE_MIN, BORNE_MAX)
    historique = []
    print(f"🧞 Je pense à un nombre entre {BORNE_MIN} et {BORNE_MAX}. Tu as {ESSAIS_MAX} essais.")

    while len(historique) < ESSAIS_MAX:
        essai = demander_nombre(
            f"Essai n°{len(historique) + 1} : ",
            min_val=BORNE_MIN,
            max_val=BORNE_MAX,
        )
        historique.append(essai)

        if essai < secret:
            print("C'est plus grand ⬆️")
        elif essai > secret:
            print("C'est plus petit ⬇️")
        else:
            print(f"🎉 Bravo, trouvé en {len(historique)} essai(s) !")
            break
    else:
        print(f"😢 Perdu, le nombre était {secret}.")

    print(f"Tes essais : {historique}")


# --- Partie 2 : l'ordinateur devine ---------------------------------------

def strategie_lineaire(bas, haut):
    """Propose toujours le plus petit nombre encore possible."""
    return bas


def strategie_hasard(bas, haut):
    """Propose un nombre au hasard parmi ceux encore possibles."""
    return random.randint(bas, haut)


def strategie_dichotomie(bas, haut):
    """Propose le milieu de l'intervalle encore possible."""
    return (bas + haut) // 2


STRATEGIES = {
    "lineaire": ("Dans l'ordre", strategie_lineaire),
    "hasard": ("Au hasard", strategie_hasard),
    "dichotomie": ("Dichotomie", strategie_dichotomie),
}


def devine_auto(secret, strategie, verbose=False):
    """Fait deviner `secret` à l'ordinateur avec la stratégie donnée.

    Args:
        secret: Le nombre à trouver.
        strategie: Une fonction (bas, haut) -> proposition.
        verbose: Si True, affiche chaque proposition.

    Returns:
        Le nombre d'essais nécessaires.
    """
    bas, haut = BORNE_MIN, BORNE_MAX
    essais = 0
    while True:
        proposition = strategie(bas, haut)
        essais += 1
        if verbose:
            print(f"  Essai {essais} : {proposition}", end="")
        if proposition == secret:
            if verbose:
                print("  ✅ trouvé !")
            return essais
        if proposition < secret:
            if verbose:
                print("  → c'est plus grand")
            bas = proposition + 1
        else:
            if verbose:
                print("  → c'est plus petit")
            haut = proposition - 1


def lancer_strategie_unique():
    """Laisse l'utilisateur choisir une stratégie et fait deviner l'ordinateur."""
    print("\nStratégies disponibles :")
    for i, (cle, (nom, _)) in enumerate(STRATEGIES.items(), start=1):
        print(f"  {i}. {nom} ({cle})")

    choix = demander_choix(
        "Ton choix (nom ou numéro) : ",
        [cle for cle in STRATEGIES] + [str(i) for i in range(1, len(STRATEGIES) + 1)],
    )

    # Si l'utilisateur a tapé un numéro, on le convertit en clé
    if choix.isdigit():
        cle = list(STRATEGIES.keys())[int(choix) - 1]
    else:
        cle = choix

    nom, strategie = STRATEGIES[cle]
    secret = random.randint(BORNE_MIN, BORNE_MAX)
    print(f"\n🤖 L'ordinateur doit deviner un nombre entre {BORNE_MIN} et {BORNE_MAX}.")
    print(f"Stratégie choisie : {nom}")
    print(f"(Pour info, le nombre secret est {secret} — chut !)\n")

    essais = devine_auto(secret, strategie, verbose=True)
    print(f"\nL'ordinateur a trouvé en {essais} essai(s) avec la stratégie « {nom} ».")


def comparer_strategies(nb_parties=1000):
    """Fait jouer chaque stratégie et affiche le nombre moyen et maximal d'essais."""
    print(f"\nComparaison sur {nb_parties} parties (secret aléatoire à chaque fois) :\n")
    for cle, (nom, strategie) in STRATEGIES.items():
        resultats = []
        for _ in range(nb_parties):
            secret = random.randint(BORNE_MIN, BORNE_MAX)
            resultats.append(devine_auto(secret, strategie))
        moyenne = sum(resultats) / len(resultats)
        print(f"{nom:<14} moyenne : {moyenne:5.1f} essais   pire cas : {max(resultats)}")


# --- Menu principal --------------------------------------------------------

def menu():
    """Affiche le menu principal et dispatche vers les différentes options."""
    while True:
        print("\n=== Le génie : devine le nombre ===")
        print("1. Jouer (le joueur devine)")
        print("2. L'ordinateur devine (choix de la stratégie)")
        print("3. Comparer toutes les stratégies")
        print("4. Quitter")

        choix = demander_choix("Ton choix : ", ["1", "2", "3", "4"])

        if choix == "1":
            jouer()
        elif choix == "2":
            lancer_strategie_unique()
        elif choix == "3":
            comparer_strategies()
        elif choix == "4":
            print("À bientôt ! 👋")
            break


if __name__ == "__main__":
    menu()