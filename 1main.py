'''
Coding in UTF8
Mini-projet 2 : Projet Harry se fait la malle
Author : Tampigny Thibault , Isabelle Amara, Chaïma
'''
import fonction_affichage
import flurry_et_bott
import olivander
import madame_guipure
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
                    choix_monaie_utilisateur_fb = int(input("Veuillez renseignez le montant que je dois vous rendre: "))
                    aff_rendu_utilisateur_fb = flurry_et_bott(choix_monaie_utilisateur_fb)
                    fonction_affichage(aff_rendu_utilisateur_fb, choix_monaie_utilisateur_fb)
                choix_inter = input("Choisissez entre le choix imposé ou la monaie que je doit vous rendre\n1 :Choix imposé\n2 :Monaie que je doit vous rendre")
            reponse = input("Bonjour chère monsieur où allez-vous?:\nLes choix de boutiques sont les suivants\n1 :Fleury & Bott\n2 :"+
            "Madame Guipire\n3 :Ollivander\nJe tiens a vous prévenir que tout autre choix vous ramenera au chemin de travverse.")    
        elif reponse == '2':
            choix_inter = input("Choisissez entre le choix imposé ou la monaie que je doit vous rendre\n1 :"+
            "Choix imposé\n2 :Monaie que je doit vous rendre")
            if choix_inter == '1':
                pass
            else:
                choix_monaie_utilisateur_mg = int(input("Veuillez renseignez le montant que je dois vous rendre: "))
                aff_rendu_utilisateur_mg = madame_guipure(choix_monaie_utilisateur_mg)
        else:
            choix_inter = input("Choisissez entre le choix imposé ou la monaie que je doit vous rendre\n1 :"+
            "Choix imposé\n2 :Monaie que je doit vous rendre")
            if choix_inter == '1':
                pass
            else:
                pass
    reponse = input("Bonjour chère monsieur où allez-vous?:\nLes choix de boutiques sont les suivants\n1 :Fleury & Bott\n2 :"+
        "Madame Guipire\n3 :Ollivander\nJe tiens a vous prévenir que tout autre choix vous ramenera au chemin de travverse.")

fonction_ihm()








