'''
Coding in UTF8
Mini-projet 2 : Projet Harry se fait la malle
Author : Tampigny Thibault , Isabelle Amara, Chaïma
'''

#-----------------------------------------------------------------------------
#Partie : A
'''
def flurry_et_bott(somme_a_rendre):
    """
    Doc-string : Dans cet fonction nous avons un algorithme glouton avec un dictionnaire de valeurs illimité qui calcule une 
    somme a rendre a l'utilisateur
    Entrée : 
    Sorti :
    """"
    somme = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    dico_somme = {}

    for billet in somme:
        if somme_a_rendre >= billet:
            nb_billets_a_rendre = somme_a_rendre // billet
            dico_somme[billet] = nb_billets_a_rendre
            somme_a_rendre -= billet * nb_billets_a_rendre
    return dico_somme
print(flurry_et_bott())
'''
#------------------------------------------------------------------------------
#Partie : B
'''
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
#Corrigé avec chat-GPT
    monnaie_disponible = all(quantite_dispo == 0 for quantite_dispo in somme.value())

    if monnaie_disponible:
        print(f'Monnaie rendue avec succès: {dico_somme}')
    else:
        print("Désolé, nous n'avons pas suffisamment de monnaie pour vous rembourser correctement.")

    return dico_somme
print(madame_guipure())
'''
#-------------------------------------------------------------------------------
#Partie : C
'''
def rendre_monnaie(somme):
    """
    Doc-String :
    Entrée : 
    Sorti :
    """
    gallions = somme // 17 # 1 gallion => 17 mornilles
    reste = somme % 17 #Gallions qui ne sont pas entiers
    mornilles = reste // 29 # 1 mornille => 29 noises
    noises = reste % 29 #Ce qui ne peut faire des mornilles donc des noises
    return gallions, mornilles, noises

def olivander(somme_a_rendre):
    """
    Doc-String :
    Entrée : 
    Sorti : 
    """
    sommes = {0, 654, 23 * 29 + 78, 2 * 17 + 11 * 29 + 9, 7 * 17 + 531 * 29 + 451}

    for somme in sommes:
        gallions, mornilles, noises = rendre_monnaie(somme)
        print(f"Somme à rendre est : {somme} en gallions, {gallions} en mornilles, {mornilles} en noises et {noises} en noises.")

    return gallions, mornilles, noises
'''
#---------------------------------------------------------------------------------
#Fonction d'affichage
def fonction_affichage(resultat, somme_a_rendre):
    """
    Doc-String :
    Entrée : 
    Sorti : 
    """
    for key, value in resultat.items():
        print(f"Voilà {value} billets de {key} pour une somme totale de {sommes_a_rendre} :")

    zqdqdqzdd

#----------------------------------------------------------------------------------
#Partie : Fonction de ihm du traitement de donnée
def fonction_ihm():
    """
    Doc-String :
    Entrée : 
    Sorti : 
    """
    reponse = input("Bonjour chère monsieur où allez-vous?:\nLes choix de boutiques sont les suivants\n1 :Fleury & Bott\n2 :"+
        "Madame Guipire\n3 :Ollivander\nJe tiens a vous prévenir que tout autre choix vous ramenera au chemin de travverse.")
    while reponse in ('1', '2', '3'):
        if reponse == '1':
            choix_inter = input("Choisissez entre le choix imposé ou la monaie que je doit vous rendre\n1 :Choix imposé\n2 :Monaie que je doit vous rendre")
            while choix_inter in ('1', '2'):
                if choix_inter == '1':
                    pass
                else:
                    pass
            reponse = input("Bonjour chère monsieur où allez-vous?:\nLes choix de boutiques sont les suivants\n1 :Fleury & Bott\n2 :"+
        "Madame Guipire\n3 :Ollivander\nJe tiens a vous prévenir que tout autre choix vous ramenera au chemin de travverse.")    
        elif reponse == '2':
            choix_inter = input("Choisissez entre le choix imposé ou la monaie que je doit vous rendre\n1 :"+
            "Choix imposé\n2 :Monaie que je doit vous rendre")
            if choix_inter == '1':
                pass
            else:
                pass
        else:
            pass
    reponse = input("Bonjour chère monsieur où allez-vous?:\nLes choix de boutiques sont les suivants\n1 :Fleury & Bott\n2 :"+
        "Madame Guipire\n3 :Ollivander\nJe tiens a vous prévenir que tout autre choix vous ramenera au chemin de travverse.")








