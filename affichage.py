def fonction_affichage(resultat, somme_a_rendre):
    """
    Affiche le rendu de monnaie en détaillant le nombre de billets et pièces pour une somme donnée.

    Paramètres:
    - resultat (dict): Un dictionnaire représentant le rendu de monnaie, avec les valeurs des billets ou pièces en clé
                      et le nombre correspondant en valeur.
    - somme_a_rendre (int): La somme totale pour laquelle le rendu de monnaie est effectué.

    Return:
    None
    """
    for key, value in resultat.items():
        print(f"Voilà {value} villets de {key} pour une somme totale de {somme_a_rendre}: ")