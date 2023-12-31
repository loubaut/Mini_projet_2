from affichage import fonction_affichage

def calculer_rendu_monnaie(somme):
    """
    Calcule le rendu de monnaie en gallions, mornilles et noises.

    Paramètres:
    - somme (int): La somme totale pour laquelle le rendu de monnaie est calculé.

    Return:
    tuple: Un tuple contenant le nombre de gallions, de mornilles et de noises nécessaires pour le rendu.
    """

    gallions = somme // 17  # 1 gallion => 17 mornilles
    reste = somme % 17      # Gallions qui ne sont pas entiers
    mornilles = reste // 29 # 1 mornille => 29 noises
    noises = reste % 29     # Ce qui ne peut faire des mornilles donc des noises

    return gallions, mornilles, noises

def olivander():
    """
    Fonction principale d'Olivander pour traiter des sommes prédéfinies.
    """
    sommes = [0, 654, 23 * 29 + 78, 2 * 17 + 11 * 29 + 9, 7 * 17 + 531 * 29 + 451] #Tout convertis en noises

    for somme in sommes:
        rendu = calculer_rendu_monnaie(somme)
        fonction_affichage(rendu, somme)