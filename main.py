'''
Mini-projet 2 : Projet Harry se fait la malle
Coding in UTF8
Author : Tampigny Thibault , Isabelle Amara, Chaïma
'''

#-----------------------------------------------------------------------------
#Partie : A
'''
def flurry_et_bott(somme_a_rendre):
    somme = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    dico_somme = {}

    for billet in somme:
        if somme_a_rendre >= billet:
            nb_billets_a_rendre = somme_a_rendre // billet
            dico_somme[billet] = nb_billets_a_rendre
            somme_a_rendre -= billet * nb_billets_a_rendre
    return dico_somme
print(Flurry_et_Bott(50045))
'''
#------------------------------------------------------------------------------
#Partie : B
'''
def madame_guipure(somme_a_rendre):
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
#Corrigé avec chat-GPT
    monnaie_disponible = all(quantite_dispo == 0 for quantite_dispo in somme.values())

    if monnaie_disponible:
        print(f'Monnaie rendue avec succès: {dico_somme}')
    else:
        print("Désolé, nous n'avons pas suffisamment de monnaie pour vous rembourser correctement.")

    return dico_somme
print(madame_guipure(100))
'''
#-------------------------------------------------------------------------------
#Partie : C
'''
def olivander():
'''
#-------------------------------------------------------------------------------
#Demander le chemin

'''
user = input("Où allez vous ? :\n")

if user == '1':
    sommes_a_rendre = (0, 60, 63, 231, 899)
    for i in range(len(sommes_a_rendre)):
        resultat = somme_a_donner(sommes_a_rendre[i])
        for keys, values in resultat.items():
            print(f"Voilà {values} billets de {keys} pour une somme totale de {sommes_a_rendre[i]} :")

if user == '2':
    somme_a_rendre = (0, 8, 62, 231, 497, 842)
    for i in range (len(somme_a_rendre)):
        resultat2 = somme_a_donner(somme_a_rendre[i])
        for key, values in resultat.items():
            print(f"Voilà {values} billets de {keys} pour une somme totale de {sommes_a_rendre[i]} :")

'''

#----------------------------------------------------------------------------------
#Partie : Fonction de l'affichage du traitement de donnée