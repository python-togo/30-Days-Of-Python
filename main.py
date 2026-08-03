from interface import choisir_transport, demander_distance, demander_heure, afficher_resultat
from calculateur import calculer_prix

def main():

    print(" ------ BIENVENUE DANS LE CALCULATEUR DE TRAJET ------- ")
    print(" Zemidjan / Taxi - Lomé")

    while True:
        transport = choisir_transport()
        distance = demander_distance()
        heure = demander_heure()

        prix = calculer_prix(transport, distance, heure)

        afficher_resultat(transport, distance, heure, prix)

        while True:
            reponse = input("Voulez-vous calculer un autre trajet ? (o/n) : ")
            reponse = reponse.lower().strip()
            if reponse in ["o", "n"]:
                break
            print(" Repondez par 'o' ou 'n' .")

        if reponse == "n":
            print('  Merci d\'avoir utilisé le calculateur de trajet !')
            print(" A Bientôt sur la route ")
            break


if __name__ == "__main__":
    main()



     