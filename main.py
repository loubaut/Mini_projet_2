'''
Coding in UTF8
Mini-projet 2 : Projet Harry se fait la malle
Author : Tampigny Thibault , Isabelle Amara, Chaïma
'''
# Constantes pour le système de monnaie magique
NOISE = 1
MORNILLE = NOISE * 29
GALLION = MORNILLE * 17


def flurry_et_bott(somme_totale: int) -> dict:
	"""Calcule le rendu de monnaie chez le libraire.

    Paramètres:
    - somme_totale (int): Le montant total à payer.

    Returns:
    dict: Un dictionnaire représentant le rendu de monnaie, avec les valeurs des billets ou pièces en clé
          et le nombre correspondant en valeur.
    """
	billets_pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1]
	rendu = {}

	for billet_piece in billets_pieces:
		nombre_billets_pieces = somme_totale // billet_piece
		if nombre_billets_pieces > 0:
			rendu[billet_piece] = nombre_billets_pieces
			somme_totale -= nombre_billets_pieces * billet_piece

	return rendu


def madame_guipure(somme_totale: int) -> dict or str:
	"""Calcule le rendu de monnaie chez le prêt-à-porter.

    Paramètres:
    - somme_totale (int): Le montant total à payer.

    Returns:
    Union[dict, str]: Un dictionnaire représentant le rendu de monnaie avec les valeurs des billets ou pièces en clé
                     et le nombre correspondant en valeur, ou une chaîne de caractères indiquant que le rendu est incomplet.
    """
	billets_pieces_limitees = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 5: 1, 2: 5}
	rendu = {}

	for billet_piece, nombre_limite in billets_pieces_limitees.items():
		nombre_billets_pieces = min(somme_totale // billet_piece, nombre_limite)
		if nombre_billets_pieces > 0:
			rendu[billet_piece] = nombre_billets_pieces
			somme_totale -= nombre_billets_pieces * billet_piece

	if somme_totale == 0:
		return rendu
	else:
		return f"Rendu de monnaie incomplet : {somme_totale} €"


def olivander(gallions_donnees: int, mornilles_donnees: int, noises_donnees: int, prix_baguette_g: int, prix_baguette_m: int, prix_baguette_n: int) -> dict:
	"""Calcule le rendu de monnaie chez le prêt-à-porter.

    Paramètres:
    - somme_totale (int): Le montant total à payer.

    Returns:
    Union[dict, str]: Un dictionnaire représentant le rendu de monnaie avec les valeurs des billets ou pièces en clé
                     et le nombre correspondant en valeur, ou une chaîne de caractères indiquant que le rendu est incomplet.
    """
	somme_totale_donnee = (gallions_donnees * prix_baguette_g) + (mornilles_donnees * prix_baguette_m) + (noises_donnees * prix_baguette_n)
	somme_totale_due = 5 * prix_baguette_g + 17 * prix_baguette_m + 29 * prix_baguette_n

	somme_totale_rendue = somme_totale_donnee - somme_totale_due

	billets_pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1]
	rendu = {}

	for billet_piece in billets_pieces:
		nombre_billets_pieces = somme_totale_rendue // billet_piece
		if nombre_billets_pieces > 0:
			rendu[billet_piece] = nombre_billets_pieces
			somme_totale_rendue -= nombre_billets_pieces * billet_piece

	return rendu

def fonction_affichage(resultat, somme_a_rendre):
    """
    Doc-String:
    Entrée: 
    Sortie: 
    """
    for key, value in resultat.items():
        print(f"Voilà {value} billets de {key} pour une somme totale de {somme_a_rendre}:")

def fonction_ihm():
    """
    Doc-String: Text basée sur une interaction homme machine permettant de choisir entre 3 fonction crée précédement.
    Entrée: vide
    Sorti: vide
    """
    
       
    reponse = input("Bonjour vous êtes sur le chemin de traverse les choix sont les suivants: Vos choix  1: Flurry et bott,\n 2:Madame Guipure,\n 3: Olivander")
    while reponse in ('1', '2', '3'):
		if reponse == '1':
			choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
			while choix_inter in ('1', '2'):
				if choix_inter == '1':
					print(flurry_et_bott(0, 60, 63, 231, 899))
				else:
					choix_monaie_utilisateur_fb = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
					aff_rendu_utilisateur_fb = flurry_et_bott(choix_monaie_utilisateur_fb)
					fonction_affichage(aff_rendu_utilisateur_fb, choix_monaie_utilisateur_fb)
					choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
				
		elif reponse == '2':
			choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
			if choix_inter == '1':
				print(madame_guipure(0, 17, 68, 231, 497, 842))
			else:
				choix_monaie_utilisateur_mg = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
				aff_rendu_utilisateur_mg = madame_guipure(choix_monaie_utilisateur_mg)
				fonction_affichage(aff_rendu_utilisateur_mg, choix_monaie_utilisateur_mg)
				
		elif reponse == '3':
			choix_inter = input("Choisissez entre le choix imposé ou la monnaie que je dois vous rendre\n1: Choix imposé\n2: Monnaie que je dois vous rendre")
			if choix_inter == '1':
				print(olivander)
			else:
				choix_monaie_utilisateur_ol = int(input("Veuillez renseigner le montant que je dois vous rendre: "))
				aff_rendu_utilisateur_ol = olivander(choix_monaie_utilisateur_ol)
				fonction_affichage(aff_rendu_utilisateur_ol, choix_monaie_utilisateur_ol)
				
	else:
        print("Choix invalide. Retour au chemin de traverse.")
           
