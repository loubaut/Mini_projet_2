def madame_guipure(somme_a_rendre):
    """
    Doc-String : Cet fonction permet de calculer une somme a rendre avec un dictionnaire de valeurs limité
    Entrée : La somme que l'on doit rentre au client
    Sorti : Le nombre de valeurs demander pour atteindre la somme a rendre au client
    """
    somme = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
    dico_somme = {}
    monnaie_disponible = True  # Variable pour vérifier si la monnaie est disponible

    for billet, quantite_dispo in somme.items():
        if somme_a_rendre >= billet and quantite_dispo > 0:
            nb_billets_a_rendre = somme_a_rendre // billet
            if nb_billets_a_rendre > quantite_dispo:
                nb_billets_a_rendre = quantite_dispo
            dico_somme[billet] = nb_billets_a_rendre
            somme_a_rendre -= nb_billets_a_rendre * billet
            quantite_dispo -= nb_billets_a_rendre  # Met à jour la quantité disponible
    monnaie_disponible = all(quantite_dispo == 0 for quantite_dispo in somme.values())

    if monnaie_disponible:
        print(f'Monnaie rendue avec succès: {dico_somme}')
    else:
        print("Désolé, nous n'avons pas suffisamment de monnaie pour vous rembourser correctement.")

    return dico_somme