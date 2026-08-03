from constantes import ZEMIDJAN , TAXI, HEURE_POINTE


# La fonction pour convertir l'heure saisie

def convertir_heure(heure_str):

    parties = heure_str.split(":")
    heures = int(parties[0])
    minutes = int(parties[1])

    return heures + (minutes / 60)




# La fonction qui permet de verifier si l'heure saisie correspond à l'heure de pointe

def est_heure_pointe(heure_str):

    heure_decimale = convertir_heure(heure_str)
    for debut, fin in HEURE_POINTE:
        if debut <= heure_decimale <= fin:
            return True
        else:
            return False




def calculer_prix(transport, distance, heure):

    if transport == "zemidjan":
        tarifs = ZEMIDJAN
    else:
        tarifs = TAXI

    prix_de_base = tarifs["tarif_de_base"] + (tarifs["prix_au_km"] * distance)

    if est_heure_pointe(heure):
        prix_final = prix_de_base * tarifs["majoration"]
    else:
        prix_final = prix_de_base
    return prix_final




def arrondir_prix(prix):
    return round(prix / 25) * 25










