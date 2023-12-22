def fonction_affichage(resultat, somme_a_rendre, monnaie_disponible):
    """
    Affiche le rendu de monnaie en détaillant le nombre de billets et pièces pour une somme donnée.

    Paramètres:
    - resultat (dict): Un dictionnaire représentant le rendu de monnaie, avec les valeurs des billets ou pièces en clé
                      et le nombre correspondant en valeur.
    - somme_a_rendre (int): La somme totale pour laquelle le rendu de monnaie est effectué.

    Return:
    None
    """

    print(f"Pour une somme à rendre de {somme_a_rendre} :")
    for key, value in resultat.items():
        print(f"Voilà {value} billets de {key}.")
    if monnaie_disponible > 0:
        print(f"Désolé, nous n'avons pas suffisamment de monnaie pour vous rembourser correctement, il reste {monnaie_disponible}.")
        
    