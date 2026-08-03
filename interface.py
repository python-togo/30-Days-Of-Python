from calculateur import est_heure_pointe, arrondir_prix


def choisir_transport():

    while True:
        choix = input('Choisissez votre transport (z pour zemidjan, t pour taxi) : ')
        choix = choix.lower().strip()
        if choix == "z":
            return "zemidjan"
        elif choix == "t":
            return "taxi"
        else:
            print("Choix invalide. Veuillez saisir 'z' ou 't'.")



def demander_distance():

    while True:
        try:
            distance = float(input("Entrez la distance en km : "))
            if distance <= 0:
                print("La distance doit être positive")
            else:
                return distance
        except:
            print("Veuillez entrer un nombre valide (ex: 5, 15, 3.5).")

def demander_heure():

    while True:
        heure = input("Entrez l'heure (format HH:MM) : ")
        if ":" not in heure:
            print("Format invalide ! utilisez HH:MM (ex: 07:30).")
            continue

        try:
            parties = heure.split(":")
            heures = int(parties[0])
            minutes = int(parties[1])

            if  0 <= heures <= 23 and 0 <= minutes <= 59:
                return heure
            else:
                print("Heure invalide ! Heures: 0-23, Minutes: 0-59.")
        except ValueError:
            print("Veuillez entrez des nombres valides pour l'heure et les minutes.")


def afficher_resultat(transport, distance, heure, prix):
    pointe = "OUI" if est_heure_pointe(heure) else "NON"
    prix_arrondi = arrondir_prix(prix)

    print(" 🚗------ RESULTAT DE VOTRE TRAJET ------- 🚗")

    print(f" Transport : {transport.capitalize()}")
    print(f" Distance : {distance:.1f} km")
    print(f" Heure : {heure} (pointe : {pointe})")
    print(f" Prix : {prix_arrondi} FCFA")

