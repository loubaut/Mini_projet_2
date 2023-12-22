'''
Coding in UTF8
Mini-projet 2 : Projet Harry se fait la malle
Author : Tampigny Thibault , Isabelle Amara, Chaïma Saidi
'''
from affichage import fonction_affichage
from flurry_et_bott import flurry_et_bott
from madame_guipure import madame_guipure
from olivander import calculer_rendu_monnaie
from olivander import olivander
#----------------------------------------------------------------------------------
#Partie : Fonction de ihm du traitement de donnée
def fonction_ihm():
    """
    Doc-String: Text basée sur une interaction homme machine permettant de choisir entre 3 fonction crée précédement.
    Entrée: vide
    Sorti: vide
    """
    reponse = input("Bonjour, vous êtes sur le chemin de traverse. Les choix sont les suivants voici vos choix\n1: Flurry et bott\n 2:Madame Guipure\n 3: Olivander\nEnter votre choix : ")

    while reponse in ('1', '2', '3'):
        if reponse == '1':
            choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
            while choix_inter in ('1', '2'):
                if choix_inter == '1':
                    values = [0, 60, 63, 231, 899]
                    for value in values:
                        resultat = flurry_et_bott(value)
                        fonction_affichage(resultat, value)
                        
                else:
                    choix_monaie_utilisateur_fb = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
                    aff_rendu_utilisateur_fb = flurry_et_bott(choix_monaie_utilisateur_fb)
                    fonction_affichage(aff_rendu_utilisateur_fb, choix_monaie_utilisateur_fb)
                    choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
                choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
                
        elif reponse == '2':
            choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
            if choix_inter == '1':
                values = [0, 17, 68, 231, 497, 842]
                for value in values:
                    resultat = madame_guipure(value)
                    fonction_affichage(resultat, value)
                    
            else:
                choix_monaie_utilisateur_mg = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
                aff_rendu_utilisateur_mg = madame_guipure(choix_monaie_utilisateur_mg)
                fonction_affichage(aff_rendu_utilisateur_mg, choix_monaie_utilisateur_mg)
            choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")   
             
        elif reponse == '3':
            choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
            if choix_inter == '1':
                    olivander()
                    
            else:
                choix_monaie_utilisateur_ol = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
                aff_rendu_utilisateur_ol = calculer_rendu_monnaie(choix_monaie_utilisateur_ol)
                fonction_affichage(aff_rendu_utilisateur_ol, choix_monaie_utilisateur_ol)
            choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
            
        reponse = input("Bonjour, vous êtes sur le chemin de traverse. Les choix sont les suivants voici vos choix\n1: Flurry et bott\n 2:Madame Guipure\n 3: Olivander\nEnter votre choix")
    else:
        print("Choix invalide. Retour au chemin de traverse.")

fonction_ihm()
#Entièrement réaliser par TAMPIGNY thibault