def flurry_et_bott(somme_a_rendre):
    """
    Doc-string : Dans cet fonction nous avons un algorithme glouton avec un dictionnaire de valeurs illimité qui calcule une 
    somme a rendre a l'utilisateur
    Entrée : 
    Sorti :
    """
    somme = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    dico_somme = {}

    for billet in somme:
        if somme_a_rendre >= billet:
            nb_billets_a_rendre = somme_a_rendre // billet
            dico_somme[billet] = nb_billets_a_rendre
            somme_a_rendre -= billet * nb_billets_a_rendre
    return dico_somme