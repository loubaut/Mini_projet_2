def rendre_monnaie(somme):
    """
    Doc-String :
    Entrée : 
    Sorti :
    """
    gallions = somme // 17  # 1 gallion => 17 mornilles
    reste = somme % 17      #Gallions qui ne sont pas entiers
    mornilles = reste // 29 # 1 mornille => 29 noises
    noises = reste % 29     #Ce qui ne peut faire des mornilles donc des noises
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

print(olivander)